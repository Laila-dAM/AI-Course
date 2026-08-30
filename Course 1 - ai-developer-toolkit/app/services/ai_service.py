from app.config.settings import AI_PROVIDER
from app.providers import mock_provider


def generate_text(prompt: str) -> str:
    """
    Generate text using the configured AI provider.
    """

    if AI_PROVIDER == "mock":
        return mock_provider.generate(prompt)

    raise ValueError(f"Unsupported AI provider: {AI_PROVIDER}")