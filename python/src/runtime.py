from provider import BaseLLMProvider
from typing import AsyncGenerator

class Runtime:
    def __init__(self, config, env):
        self.config = config
        self.env = env
        self.model_stack = [config.model]

    def get_current_model(self):
        return self.model_stack[-1]

    def _get_llm_provider(self):
        model_name = self.get_current_model()
        if model_name not in self.config.providers:
            raise ValueError(f"Model not available: {model_name}")

        provider : BaseLLMProvider = self.config.providers[model_name]
        return provider

    async def invoke(self, prompt: str) -> str:
        res = ""
        async for chunk in self.stream_invoke(prompt):
            res += chunk
        return res

    async def stream_invoke(self, prompt: str) -> AsyncGenerator[str, None]:
        provider = self._get_llm_provider()
        async for chunk in provider.ainvoke(prompt):
            yield chunk
