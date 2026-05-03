from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_create_review():
    res = client.post("/reviews/", json={
        "order_id": 1,
        "user_id": 1,
        "rating": 5,
        "comment": "Good"
    })
    assert res.status_code in [200, 201]

def test_invalid_review():
    res = client.post("/reviews/", json={
        "order_id": 1,
        "user_id": 1,
        "rating": 10,
        "comment": "Bad"
    })
    assert res.status_code == 400

def test_get_reviews():
    res = client.get("/reviews/")
    assert res.status_code == 200

def test_get_review():
    create = client.post("/reviews/", json={
        "order_id": 1,
        "user_id": 1,
        "rating": 4,
        "comment": "Nice"
    })

    review_id = create.json()["id"]

    res = client.get(f"/reviews/{review_id}")
    assert res.status_code == 200

def test_delete_review():
    create = client.post("/reviews/", json={
        "order_id": 1,
        "user_id": 1,
        "rating": 2,
        "comment": "Delete"
    })

    review_id = create.json()["id"]

    res = client.delete(f"/reviews/{review_id}")
    assert res.status_code == 200