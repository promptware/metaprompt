from provider import BaseLLMProvider
from provider_config import ProviderConfig

import openai
import os
from typing import AsyncGenerator, List


class OpenAIProvider(ProviderConfig):
    """Provider for all known OpenAI LLM models"""

    def __init__(self, api_key: str = None, models=None, *args, **kwargs):
        super().__init__(self, *args, **kwargs)
        openai.api_key = api_key or os.getenv("OPENAI_API_KEY")
        models = models or [
            model.id for model in openai.models.list().data
            if "gpt" in model.id or "o1" in model.id
        ]
        for model_name in models:
            self.add(
                model_name,
                OpenAILLMProvider(
                    api_key=api_key,
                    model=model_name
                )
            )

    def get_default_model(self):
        return "gpt-4o"

class OpenAILLMProvider(BaseLLMProvider):
    """Implementation of the BaseLLMProvider for OpenAI's API.

    Reads OPENAI_API_KEY if a key is not provided.
    """

    def __init__(self, api_key: str = None, model: str = "gpt-4"):
        """Initialize the provider with API key and model name."""
        super().__init__()
        self.api_key = api_key or os.getenv("OPENAI_API_KEY")
        self.model = model
        if not self.api_key:
            raise ValueError(
                "API key is required for OpenAI API. Specify OPENAI_API_KEY environment variable or provide an api_key argument"
            )

    async def ainvoke(self, prompt: str, role: str, history: List[{ "role": str, "content": str }] = []) -> AsyncGenerator[str, None]:
        """Asynchronously invoke the OpenAI API and yield results in chunks.

        Args:
            prompt (str): The input prompt for the language model.

        Yields:
            str: Chunks of the response as they're received.
        """
        client = openai.AsyncOpenAI(api_key=self.api_key)

        # TODO: use system message role for IF_PROMPT
        stream = await client.chat.completions.create(
            model="gpt-4",
            messages=history + [{"role": role, "content": prompt}],
            stream=True,
        )

        async for chunk in stream:
            yield chunk.choices[0].delta.content or ""
