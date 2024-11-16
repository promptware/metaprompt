from abc import ABC
from typing import AsyncGenerator


class BaseLLMProvider(ABC):
    """Base class for a single LLM provider."""

    def __init__(self):
        pass

    async def ainvoke(
        self, prompt: str, role: str
    ) -> AsyncGenerator[str, None]:
        pass
