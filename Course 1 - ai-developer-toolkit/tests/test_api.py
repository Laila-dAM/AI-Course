from fastapi.testclient import TestClient

from app.main import app


client = TestClient(app)


def test_health():
    response = client.get("/health")

    assert response.status_code == 200
    assert response.json() == {"status": "healthy"}

def test_generate():
    response = client.post(
        "/generate",
        json={"prompt": "Hello AI"}
    )

    assert response.status_code == 200
    assert response.json() == {
        "result": "Mock AI response for: Hello AI"
    }

def test_summarize():
    response = client.post(
        "/summarize",
        json={
            "text": "Artificial intelligence is transforming modern software development."
        }
    )

    assert response.status_code == 200
    assert response.json() == {
        "summary": "Mock summary for: Artificial intelligence is transforming modern software development."
    }
def test_classify():
    response = client.post(
        "/classify",
        json={
            "text": "I love this application. It is fast and easy to use."
        }
    )

    assert response.status_code == 200
    assert response.json() == {
        "category": "positive"
    }
def test_extract():
    response = client.post(
        "/extract",
        json={
            "text": "OpenAI was founded in 2015 and develops artificial intelligence technologies."
        }
    )

    assert response.status_code == 200
    assert response.json() == {
        "information": "Mock extracted information from: OpenAI was founded in 2015 and develops artificial intelligence technologies."
    }