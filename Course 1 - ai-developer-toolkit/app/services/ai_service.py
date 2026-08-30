from app.config.settings import AI_PROVIDER


def generate_text(prompt: str) -> str:
    """
    Generate text using the configured AI provider.
    """

    if AI_PROVIDER == "mock":
        return f"Mock AI response for: {prompt}"

    raise ValueError(f"Unsupported AI provider: {AI_PROVIDER}")