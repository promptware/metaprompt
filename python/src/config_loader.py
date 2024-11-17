from config import Config
from provider_config import ProviderConfig
from providers.interactive import InteractiveProvider
from providers.openai import OpenAIProvider
from dotenv import load_dotenv

import os

load_dotenv()


def load_config():
    """Load configuration from environment variables"""
    provider_config = ProviderConfig(InteractiveProvider())

    OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
    if OPENAI_API_KEY is not None:
        provider_config.merge(OpenAIProvider(api_key=OPENAI_API_KEY))

    return Config(providers=provider_config)
