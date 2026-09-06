import pytest

from app.config.settings import AI_PROVIDER
from app.providers.exceptions import UnsupportedProviderError
from app.providers.factory import ProviderFactory
from app.providers.mock_provider import MockProvider


def test_provider_factory_returns_mock_provider():
    provider = ProviderFactory.create()

    assert isinstance(provider, MockProvider)


def test_provider_factory_rejects_unsupported_provider(monkeypatch):
    monkeypatch.setattr(
        "app.providers.factory.AI_PROVIDER",
        "unsupported"
    )

    with pytest.raises(UnsupportedProviderError):
        ProviderFactory.create()