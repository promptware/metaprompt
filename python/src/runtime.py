from provider import BaseLLMProvider
from abc import ABC, abstractmethod
from parse_metaprompt import parse_metaprompt
from typing import Dict, AsyncGenerator, List
import os


class BaseRuntime(ABC):
    @abstractmethod
    def load_module(self, module_name: str):
        pass

    @abstractmethod
    def set_status(self, status: List[{"text": str, "color": str}]):
        pass

    @abstractmethod
    def print_chunk(self, chunk: str):
        pass

    @abstractmethod
    def input(self, prompt):
        """Used to request input from the user, which can be done by some BaseLLMProvider
        subclasses
        """
        pass
