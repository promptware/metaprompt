from provider import BaseLLMProvider
from provider_config import ProviderConfig

from typing import AsyncGenerator


class InteractiveProvider(ProviderConfig):
    """Provider for the interactive CLI interface"""

    def __init__(self, api_key: str = None, models=None, *args, **kwargs):
        super().__init__(self, *args, **kwargs)
        self.add(
            'interactive',
            InteractiveLLMProvider()
        )


class InteractiveLLMProvider(BaseLLMProvider):
    def __init__(self, api_key: str = None, model: str = "gpt-4"):
        """Initialize the provider with API key and model name."""
        super().__init__()

    async def ainvoke(self, prompt: str) -> AsyncGenerator[str, None]:
        """Asynchronously invoke the OpenAI API and yield results in chunks.

        Args:
            prompt (str): The input prompt for the language model.

        Yields:
            str: Chunks of the response as they're received.
        """
        output = input("[interactive]: " + prompt)
        yield output
