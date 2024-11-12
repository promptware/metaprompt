from provider import BaseLLMProvider
from parse_metaprompt import parse_metaprompt
from typing import AsyncGenerator
import os


class Runtime:
    def __init__(self, config, env):
        self.config = config
        self.env = env
        self.model_stack = [config.model]
        self.cwd = os.getcwd()

    def get_current_model(self):
        return self.model_stack[-1]

    def set_variable(self, var_name, value):
        self.env.set(var_name, value)

    def load_module(self, module_name):
        if module_name.startswith("./") or module_name.startswith("../"):
            file_path = os.path.abspath(
                os.path.join(self.cwd, module_name + ".metaprompt")
            )

            if os.path.isfile(file_path):
                with open(file_path, "utf-8") as file:
                    content = file.read()
                    ast = parse_metaprompt(content)
                    return ast
            else:
                raise ImportError(
                    f"Module {module_name} not found at {file_path}"
                )
        else:
            raise ValueError(
                "Package system not implemented yet. Use [:use ./relative/import] to import ./relative/import.metaprompt"
            )

    def _get_llm_provider(self):
        model_name = self.get_current_model()
        if model_name not in self.config.providers:
            raise ValueError(f"Model not available: {model_name}")

        provider: BaseLLMProvider = self.config.providers[model_name]
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

    # TODO: add special-case `invoke` with system message for :if expansion
