from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_create_user():
    res = client.post("/users/", json={
        "name": "John",
        "email": "john@test.com",
        "phone": "1234567890",
        "role": "customer",
        "password": "123"
    })
    assert res.status_code in [200, 201]

def test_duplicate_user():
    client.post("/users/", json={
        "name": "A",
        "email": "dup@test.com",
        "phone": "1",
        "role": "customer",
        "password": "123"
    })

    res = client.post("/users/", json={
        "name": "B",
        "email": "dup@test.com",
        "phone": "2",
        "role": "customer",
        "password": "123"
    })

    assert res.status_code == 400

def test_get_users():
    res = client.get("/users/")
    assert res.status_code == 200

def test_get_user():
    create = client.post("/users/", json={
        "name": "Alice",
        "email": "alice@test.com",
        "phone": "999",
        "role": "customer",
        "password": "123"
    })

    user_id = create.json()["id"]

    res = client.get(f"/users/{user_id}")
    assert res.status_code == 200

def test_delete_user():
    create = client.post("/users/", json={
        "name": "Del",
        "email": "del@test.com",
        "phone": "000",
        "role": "customer",
        "password": "123"
    })

    user_id = create.json()["id"]

    res = client.delete(f"/users/{user_id}")
    assert res.status_code == 200