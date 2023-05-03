from fastapi.testclient import TestClient

from app.main import app, API_KEY


client = TestClient(app)


def test_chat_post_invalid_api_key():
    """
    test chat post endpoint with invalid api key
    """
    response = client.post("/chat", json={"message": "What is Nifty Bridge?"}, headers={"X-API-KEY": "invalid"})
    assert response.status_code == 403
    assert response.json() == {"detail": "Invalid API Key"}

def test_chat():
    """
    test chat endpoint
    """
    response = client.get("/chat", headers={"X-API-KEY": API_KEY})
    assert response.status_code == 200


def test_chat_post():
    """
    test chat post endpoint
    """
    response = client.post("/chat", json={"message": "What is Nifty Bridge?"}, headers={"X-API-KEY": API_KEY})
    assert response.status_code == 200
