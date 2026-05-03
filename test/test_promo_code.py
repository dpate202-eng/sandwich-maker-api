from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_create_promo():
    res = client.post("/promo-codes/", json={
        "code": "SAVE10",
        "discount_percent": 10.0,
        "active": True
    })
    assert res.status_code in [200, 201]

def test_validate_promo():
    client.post("/promo-codes/", json={
        "code": "VALID50",
        "discount_percent": 50.0,
        "active": True
    })

    res = client.get("/promo-codes/validate/VALID50")
    assert res.status_code == 200

def test_get_promos():
    res = client.get("/promo-codes/")
    assert res.status_code == 200

def test_get_promo():
    create = client.post("/promo-codes/", json={
        "code": "TEST",
        "discount_percent": 20,
        "active": True
    })

    promo_id = create.json()["id"]

    res = client.get(f"/promo-codes/{promo_id}")
    assert res.status_code == 200

def test_delete_promo():
    create = client.post("/promo-codes/", json={
        "code": "DEL",
        "discount_percent": 10,
        "active": True
    })

    promo_id = create.json()["id"]

    res = client.delete(f"/promo-codes/{promo_id}")
    assert res.status_code == 200