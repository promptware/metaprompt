from provider import BaseLLMProvider
from provider_config import ProviderConfig
from eval_utils.chat_history import serialize_chat_history

from typing import AsyncGenerator, List


class InteractiveProvider(ProviderConfig):
    """Provider for the interactive CLI interface"""

    def __init__(self, api_key: str = None, models=None, *args, **kwargs):
        super().__init__(self, *args, **kwargs)
        self.add(
            'interactive',
            InteractiveLLMProvider()
        )

    def get_default_model(self):
        return 'interactive'


class InteractiveLLMProvider(BaseLLMProvider):
    def __init__(self, api_key: str = None):
        """Initialize the provider with API key and model name."""
        super().__init__()

    async def ainvoke(
        self,
        chat: List[{ "role": str, "content": str }],
        history = [], # TODO: make interactive provider respect history?
        runtime = None,
    ) -> AsyncGenerator[str, None]:
        """Asynchronously invoke the OpenAI API and yield results in chunks.

        Args:
            chat: The input prompt for the language model.

        Yields:
            str: Chunks of the response as they're received.
        """
        prompt = serialize_chat_history(chat)
        output = (input if runtime is None else runtime.input)(prompt)
        yield output
