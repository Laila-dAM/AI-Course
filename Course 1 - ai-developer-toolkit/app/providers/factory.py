from app.config.settings import AI_PROVIDER
from app.providers.base import AIProvider
from app.providers.exceptions import UnsupportedProviderError
from app.providers.mock_provider import MockProvider


class ProviderFactory:

    @staticmethod
    def create() -> AIProvider:
        if AI_PROVIDER == "mock":
            return MockProvider()

        raise UnsupportedProviderError(
            f"Unsupported AI provider: {AI_PROVIDER}"
        )