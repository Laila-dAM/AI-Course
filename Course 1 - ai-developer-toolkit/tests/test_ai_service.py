from app.services.ai_service import generate_text


def test_generate_text_with_mock_provider():
    result = generate_text("Explain what an API is")

    assert result == "Mock AI response for: Explain what an API is"