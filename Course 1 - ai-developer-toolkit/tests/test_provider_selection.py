from app.providers.factory import ProviderFactory
from app.providers.mock_provider import MockProvider


def test_provider_factory_returns_mock_provider():
    provider = ProviderFactory.create()

    assert isinstance(provider, MockProvider)