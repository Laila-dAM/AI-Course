from app.services.classification_service import classify_text


def test_classify_positive_text():
    result = classify_text("I love this application. It is fast and easy to use.")

    assert result == "positive"


def test_classify_negative_text():
    result = classify_text("This application is slow and difficult to use.")

    assert result == "negative"


def test_classify_neutral_text():
    result = classify_text("The application was released yesterday.")

    assert result == "neutral"