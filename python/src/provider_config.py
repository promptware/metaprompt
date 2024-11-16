from __future__ import annotations
from provider import BaseLLMProvider


class ProviderConfig(dict):
    """Conceptually, ProviderConfig is a dictionary that maps model names to
    BaseLLMProvider instances
    """

    def __init__(self, *args, **kwargs):
        """Provide a list of ProviderConfig instances as arguments to merge them
        together.
        """
        super().__init__(self, **kwargs)
        for provider_config in args:
            if isinstance(provider_config, ProviderConfig):
                self.merge(provider_config)

    def add(self, model_name: str, provider: BaseLLMProvider):
        """Add a model under a given name"""
        if model_name in self:
            raise ValueError(
                f"ProviderConfig.add: model {model_name} has already been provided"
            )
        self[model_name] = provider
        return self  # for .add() chaining

    def merge(self, other: ProviderConfig):
        for model_name in other:
            self.add(model_name, other[model_name])

    def get(self, model_name) -> BaseLLMProvider | None:
        return self[model_name] if model_name in self else None
