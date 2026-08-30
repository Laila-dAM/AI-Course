from app.config.classification import NEGATIVE_WORDS, POSITIVE_WORDS


def classify_text(text: str) -> str:
    text_lower = text.lower()

    positive_score = sum(
        word in text_lower for word in POSITIVE_WORDS
    )

    negative_score = sum(
        word in text_lower for word in NEGATIVE_WORDS
    )

    if positive_score > negative_score:
        return "positive"

    if negative_score > positive_score:
        return "negative"

    return "neutral"