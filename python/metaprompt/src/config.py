from provider_config import ProviderConfig
from typing import Dict

class Config:

    def __init__(
        self,
        providers: ProviderConfig,  # TODO: add List[ProviderConfig] option
        model: str,
        parameters: Dict[str, str] = {},
    ):
        self.providers = providers
        self.parameters = parameters
        self.model = model
        # TODO: add logger
