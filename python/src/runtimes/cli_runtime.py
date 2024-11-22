from runtime import BaseRuntime
from provider import BaseLLMProvider
from parse_metaprompt import parse_metaprompt

from typing import AsyncGenerator, List
import os

class CliRuntime(BaseRuntime):
    def __init__(self):
        self.cwd = os.getcwd()
        self.last_line = ""
        self.status = ""
        BLUE = "\033[34m"
        RESET = "\033[0m"
        self.status_left = BLUE
        self.status_right = RESET

    def print_status(self, old_status=""):
        print(
            "\r" +
            self.status_left +
            self.status +
            self.status_right +
            self.padding_for(old_status, self.status),
            end="",
            flush=True
        )

    def set_status(self, status: str):
        # normalize the status line
        status = status.replace("\n", " ").replace("\r", "")
        old_status = self.status
        self.status = status
        self.print_status(old_status)

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

    def padding_for(self, previous_line, line):
        return ' ' * (
            len(previous_line) - len(line)
        )

    def print_chunk(self, chunk: str):
        # print(self.last_line, end="")

        lines = chunk.split("\n")

        if len(lines) > 1:
            # kill status
            print("\r", end="", flush=True)
            # print the first line, prepending it with the leftover line
            first_line = self.last_line + lines[0]
            padding = self.padding_for(
                self.status,
                first_line
            )
            print(first_line + padding, flush=True)
            # print lines except the first and the last
            for line in lines[1:-1]:
                print(line, flush=True)
            # save the last line into the accumulator
            self.last_line = lines[-1]
        else:
            self.last_line += chunk
        # restore the status line
        self.print_status()

    def input(self, prompt):
        print("\r", end="", flush=True)
        res = input(prompt)
        self.print_status()
        return res


    def finalize(self):
        print("\r", end="", flush=True)
        print(self.last_line + self.padding_for(self.status, ""), flush=True)
