from app.providers.mock_provider import MockProvider


def test_mock_provider_generates_response():
    provider = MockProvider()

    result = provider.generate("Hello")

    assert result == "Mock AI response for: Hello"