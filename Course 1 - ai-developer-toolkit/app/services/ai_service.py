from app.providers.base import AIProvider
from app.providers.factory import ProviderFactory


def get_provider() -> AIProvider:
    return ProviderFactory.create()


def generate_text(prompt: str) -> str:
    """
    Generate text using the configured AI provider.
    """

    provider = get_provider()

    return provider.generate(prompt)