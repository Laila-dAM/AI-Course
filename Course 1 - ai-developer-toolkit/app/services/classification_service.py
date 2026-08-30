def classify_text(text: str) -> str:
    text_lower = text.lower()

    positive_words = [
        "love",
        "great",
        "excellent",
        "good",
        "amazing",
        "fast",
        "easy",
    ]

    negative_words = [
        "hate",
        "bad",
        "terrible",
        "awful",
        "slow",
        "difficult",
        "bug",
        "error",
    ]

    positive_score = sum(word in text_lower for word in positive_words)
    negative_score = sum(word in text_lower for word in negative_words)

    if positive_score > negative_score:
        return "positive"

    if negative_score > positive_score:
        return "negative"

    return "neutral"