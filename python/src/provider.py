from abc import ABC
from typing import AsyncGenerator, List


class BaseLLMProvider(ABC):
    """Base class for a single LLM provider."""

    def __init__(self):
        pass

    async def ainvoke(
        self,
        chat: List[{"role": str, "content": str}],
        history: List[{"role": str, "content": str}] = [],
    ) -> AsyncGenerator[str, None]:
        pass
