import pytest
import jwt
from app import schemas
from app.config import settings

def test_root(client):
    response = client.get("/")
    assert response.json().get("message") == "Welcome to my api!"
    assert response.status_code == 200

def test_create_user(client):
    res = client.post("/users/", json={"email": "hello@gmail.com", "password": "password123"})
    #print(res.json())
    assert res.status_code == 201
    assert res.json().get("email") == "hello@gmail.com"

def test_login_user(client, test_user):
    res = client.post(
      "/login",
      data={"username": test_user["email"], "password": test_user["password"]}
    )
    #print("res: ", res.json())
    login_res = schemas.Token(**res.json())
    payload = jwt.decode(login_res.access_token, key=settings.secret_key, algorithms=[settings.algorithm])
    id = payload.get("user_id")
    assert id == test_user["id"]
    assert login_res.token_type == "bearer"
    assert res.status_code == 200

@pytest.mark.parametrize("email, password, status_code", [
    ("wrongemail@gmail.com", "password123", 403),
    ("hello@gmail.com", "wrongpassword", 403),
    ("wrongemail@gmail.com", "wrongpassword", 403),
    (None, "password123", 403),
    ("hello@gmail.com", None, 403)
])
def test_incorrect_login(test_user, client, email, password, status_code):
    res = client.post(
        "/login",
        data={"username": email, "password": password}
    )
    assert res.status_code == status_code