from provider_config import ProviderConfig
from typing import Dict

class Config:

    def __init__(
        self,
        providers: ProviderConfig | None = None,  # TODO: add List[ProviderConfig] option
        model: str | None = None,
        parameters: Dict[str, str] = {},
    ):
        self.providers = providers or ProviderConfig()
        self.parameters = parameters
        self.model = model
        # TODO: add logger
