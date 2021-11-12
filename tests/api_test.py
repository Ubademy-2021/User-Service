from app.main import app
from fastapi.testclient import TestClient

client = TestClient(app)


def test_get_users():
    response = client.get("/api/users")
    assert response.status_code == 200
