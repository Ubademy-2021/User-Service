from fastapi.testclient import TestClient
from random import randint

from app.main import app

client = TestClient(app)


def test_get_users():
    response = client.get("/api/users")
    assert response.status_code == 200


def test_get_sprecific_user():
    response = client.get("/api/users/1")
    assert response.status_code == 200


"""
def test_post_users():
    randomString = "test" + str(randint(0, 10000000000))
    response = client.post("/api/users",
                           json={"email": randomString,
                                 "userName": randomString,
                                 "name": randomString,
                                 "surname": randomString,
                                 "phoneNumber": randomString,
                                 "city": randomString,
                                 "state": randomString,
                                 "country": randomString,
                                 "address": randomString})
    assert response.status_code == 200


def test_put_users():
    randomString = "test" + str(randint(0, 10000000000))
    response = client.put("/api/users/5",
                          json={"email": randomString,
                                "userName": randomString,
                                "name": randomString,
                                "surname": randomString,
                                "phoneNumber": randomString,
                                "city": randomString,
                                "state": randomString,
                                "country": randomString,
                                "address": randomString})
    assert response.status_code == 200
"""
