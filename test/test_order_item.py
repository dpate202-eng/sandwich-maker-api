from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def create_order():
    res = client.post("/orders/", json={
        "customer_name": "Test",
        "customer_phone": "1234567890",
        "order_type": "takeout",
        "status": "pending",
        "total_price": 0
    })
    return res.json()["id"]

def test_create_order_item():
    order_id = create_order()

    res = client.post("/order-items/", json={
        "order_id": order_id,
        "menu_item_id": 1,
        "quantity": 2,
        "unit_price": 10.0
    })
    assert res.status_code in [200, 201]

def test_get_order_items():
    res = client.get("/order-items/")
    assert res.status_code == 200

def test_get_order_item():
    order_id = create_order()

    create = client.post("/order-items/", json={
        "order_id": order_id,
        "menu_item_id": 1,
        "quantity": 1,
        "unit_price": 5.0
    })

    item_id = create.json()["id"]

    res = client.get(f"/order-items/{item_id}")
    assert res.status_code == 200

def test_get_items_by_order():
    order_id = create_order()

    res = client.get(f"/order-items/order/{order_id}")
    assert res.status_code == 200

def test_update_order_item():
    order_id = create_order()

    create = client.post("/order-items/", json={
        "order_id": order_id,
        "menu_item_id": 1,
        "quantity": 1,
        "unit_price": 5.0
    })

    item_id = create.json()["id"]

    res = client.put(f"/order-items/{item_id}", json={"quantity": 3})
    assert res.status_code == 200

def test_delete_order_item():
    order_id = create_order()

    create = client.post("/order-items/", json={
        "order_id": order_id,
        "menu_item_id": 1,
        "quantity": 1,
        "unit_price": 5.0
    })

    item_id = create.json()["id"]

    res = client.delete(f"/order-items/{item_id}")
    assert res.status_code == 200