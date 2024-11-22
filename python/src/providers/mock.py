from provider import BaseLLMProvider
from provider_config import ProviderConfig
from eval_utils.chat_history import serialize_chat_history

import re
from typing import AsyncGenerator, List, Dict, Tuple


class MockProvider(ProviderConfig):
    """Provider for the mock interface used for testing"""

    def __init__(
            self,
            rules: List[Tuple[re.Pattern | Dict[str, re.Pattern], str]],
            models=["mock"],
            *args,
            **kwargs
    ):
        super().__init__(self, *args, **kwargs)
        if len(models) == 0:
            raise ValueError("MockProvider expects at least one model name")
        self.default_model = models[0]
        for model in models:
            self.add(
                model,
                MockLLMProvider(rules)
            )

    def get_default_model(self):
        return self.default_model


class MockLLMProvider(BaseLLMProvider):
    def __init__(self, rules):
        super().__init__()
        self.rules = rules

    @staticmethod
    def match_rule(rule, history, chat):
        chat_text = serialize_chat_history(chat)
        history_text = serialize_chat_history(history)
        if isinstance(rule, re.Pattern):
            all_text = serialize_chat_history(history + chat)
            if re.search(rule, all_text):
                return True
            return False
        else:
            if "chat" in rule:
                if not re.search(rule["chat"], chat_text):
                    return False
            if "history" in rule:
                if not re.search(rule["history"], history_text):
                    return False
            return True

    async def ainvoke(
        self,
        chat: List[{ "role": str, "content": str }],
        history: List[{ "role": str, "content": str }] = [],
        runtime = None,
    ) -> AsyncGenerator[str, None]:
        """Asynchronously invoke the OpenAI API and yield results in chunks.

        Args:
            chat: The input prompt for the language model.

        Yields:
            str: Chunks of the response as they're received.
        """
        chat_text = serialize_chat_history(chat)
        history_text = serialize_chat_history(history)

        selected_rules = []
        for rule, response in self.rules:
            if MockLLMProvider.match_rule(rule, history, chat):
                selected_rules.append((rule, response))
        if len(selected_rules) == 0:
            raise ValueError(
                "MockLLMProvider failed to match rules for:\nchat = " + chat_text
                + "\nhistory = " + history_text
                + "\n-------------------rules: " + str(selected_rules)
            )
        elif len(selected_rules) > 1:
            raise ValueError(
                "MockLLMProvider matched more than one rule for:\nchat = " + chat_text
                + "\nhistory = " + history_text
                + "\n-------------------rules: " + str(selected_rules)
            )
        else:
            yield selected_rules[0][1]
