from provider_config import ProviderConfig
from typing import Dict
from prelude import prelude


class Config:

    def __init__(
        self,
        providers: (
            ProviderConfig | None
        ) = None,  # TODO: add List[ProviderConfig] option
        model: str | None = None,
        parameters: Dict[str, str] = None,
        foreign_functions=None,
    ):
        self.providers = providers or ProviderConfig()
        self.parameters = parameters or {}
        self.model = model
        self.foreign_functions = {**prelude, **(foreign_functions or {})}
        # TODO: add logger
