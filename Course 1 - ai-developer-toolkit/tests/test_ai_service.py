from app.providers.mock_provider import MockProvider
from app.services.ai_service import generate_text, get_provider


def test_generate_text_with_mock_provider():
    result = generate_text("Explain what an API is")

    assert result == "Mock AI response for: Explain what an API is"


def test_get_provider_returns_mock_provider():
    provider = get_provider()

    assert isinstance(provider, MockProvider)