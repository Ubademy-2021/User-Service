from app.main import app
from fastapi.testclient import TestClient

client = TestClient(app)


def test_get_users():
    response = client.get("/api/users")
    assert response.status_code == 200


def test_get_admins():
    response = client.get("/api/admins")
    assert response.status_code == 200


def test_get_user_id_1():
    response = client.get("/api/users?user_id=1")
    assert response.status_code == 200


def test_get_user_id_not_exists():
    response = client.get("/api/users?user_id=34348634868348")
    assert response.status_code != 200


def test_get_user_email_not_exists():
    response = client.get("/api/users?email=34348634868348")
    assert response.status_code != 200


def test_get_admin_id_1():
    response = client.get("/api/admins?admin_id=1")
    assert response.status_code == 200


def test_get_admin_id_not_exists():
    response = client.get("/api/admins?admin_id=34348634868348")
    assert response.status_code != 200


def test_get_admin_email_not_exists():
    response = client.get("/api/admins?email=34348634868348")
    assert response.status_code != 200


def test_get_users_active():
    response = client.get("/api/users/active")
    assert response.status_code == 200


def test_get_users_favorite():
    response = client.get("/api/users/favorites/1")
    assert response.status_code == 200


def test_get_user_categories():
    response = client.get("/api/categories/1")
    assert response.status_code == 200
