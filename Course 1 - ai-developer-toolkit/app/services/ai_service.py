from app.config.settings import AI_PROVIDER
from app.providers.base import AIProvider
from app.providers.mock_provider import MockProvider


def get_provider() -> AIProvider:
    if AI_PROVIDER == "mock":
        return MockProvider()

    raise ValueError(f"Unsupported AI provider: {AI_PROVIDER}")


def generate_text(prompt: str) -> str:
    """
    Generate text using the configured AI provider.
    """

    provider = get_provider()

    return provider.generate(prompt)