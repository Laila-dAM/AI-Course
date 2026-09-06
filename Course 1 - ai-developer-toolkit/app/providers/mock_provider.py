from app.providers.base import AIProvider


class MockProvider(AIProvider):

    def generate(self, prompt: str) -> str:
        return f"Mock AI response for: {prompt}"