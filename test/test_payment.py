from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def create_order():
    res = client.post("/orders/", json={
        "customer_name": "Pay User",
        "customer_phone": "1234567890",
        "order_type": "takeout",
        "status": "pending",
        "total_price": 50.0
    })
    return res.json()["id"]

def test_create_payment():
    order_id = create_order()

    res = client.post("/payments/", json={
        "order_id": order_id,
        "method": "cash",
        "amount": 50.0,
        "status": "completed"
    })
    assert res.status_code in [200, 201]

def test_get_payments():
    res = client.get("/payments/")
    assert res.status_code == 200

def test_get_payment():
    order_id = create_order()

    create = client.post("/payments/", json={
        "order_id": order_id,
        "method": "cash",
        "amount": 20.0,
        "status": "pending"
    })

    payment_id = create.json()["id"]

    res = client.get(f"/payments/{payment_id}")
    assert res.status_code == 200

def test_update_payment():
    order_id = create_order()

    create = client.post("/payments/", json={
        "order_id": order_id,
        "method": "cash",
        "amount": 30.0,
        "status": "pending"
    })

    payment_id = create.json()["id"]

    res = client.put(f"/payments/{payment_id}", json={"status": "completed"})
    assert res.status_code == 200

def test_delete_payment():
    order_id = create_order()

    create = client.post("/payments/", json={
        "order_id": order_id,
        "method": "cash",
        "amount": 10.0,
        "status": "pending"
    })

    payment_id = create.json()["id"]

    res = client.delete(f"/payments/{payment_id}")
    assert res.status_code == 200