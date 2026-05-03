from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_create_order():
    res = client.post("/orders/", json={
        "customer_name": "John",
        "customer_phone": "1234567890",
        "order_type": "takeout",
        "status": "pending",
        "total_price": 20.0
    })
    assert res.status_code in [200, 201]

def test_get_orders():
    res = client.get("/orders/")
    assert res.status_code == 200

def test_get_order():
    create = client.post("/orders/", json={
        "customer_name": "Alice",
        "customer_phone": "1111111111",
        "order_type": "delivery",
        "status": "pending",
        "total_price": 30.0
    })
    order_id = create.json()["id"]

    res = client.get(f"/orders/{order_id}")
    assert res.status_code == 200

def test_update_order():
    create = client.post("/orders/", json={
        "customer_name": "Bob",
        "customer_phone": "2222222222",
        "order_type": "takeout",
        "status": "pending",
        "total_price": 10.0
    })
    order_id = create.json()["id"]

    res = client.put(f"/orders/{order_id}", json={"status": "preparing"})
    assert res.status_code == 200

def test_delete_order():
    create = client.post("/orders/", json={
        "customer_name": "Delete",
        "customer_phone": "0000000000",
        "order_type": "takeout",
        "status": "pending",
        "total_price": 10.0
    })
    order_id = create.json()["id"]

    res = client.delete(f"/orders/{order_id}")
    assert res.status_code == 200