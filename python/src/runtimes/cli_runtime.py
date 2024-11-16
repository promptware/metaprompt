from runtime import BaseRuntime
from provider import BaseLLMProvider
from parse_metaprompt import parse_metaprompt

from typing import AsyncGenerator, List
import os

class CliRuntime(BaseRuntime):
    def __init__(self, config, env):
        self.cwd = os.getcwd()

    def set_status(self, status: str):
        pass

    def load_module(self, module_name: str):
        if module_name.startswith("./") or module_name.startswith("../"):
            file_path = os.path.abspath(
                os.path.join(self.cwd, module_name + ".metaprompt")
            )

            if os.path.isfile(file_path):
                with open(file_path, "r") as file:
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

    def print_chunk(self, chunk: str):
        print(chunk, end="")

    def finalize(self):
        pass
