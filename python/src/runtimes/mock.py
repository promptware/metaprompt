from runtime import BaseRuntime
from provider import BaseLLMProvider
from parse_metaprompt import parse_metaprompt

from typing import AsyncGenerator, List
import os

class MockRuntime(BaseRuntime):
    def __init__(self, modules):
        # TODO: implement relative module loading in the mock
        self.modules = modules

    def set_status(self, status: str):
        self.status = status

    def load_module(self, module_name: str):
        if module_name in self.modules:
            return parse_metaprompt(self.modules[module_name])

        raise ImportError(
            f"Module {module_name} not found"
        )

    def print_chunk(self, chunk: str):
        pass

    def input(self, prompt):
        pass # TODO: implement

    def finalize(self):
        pass
