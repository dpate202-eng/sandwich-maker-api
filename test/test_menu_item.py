from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

# -----------------------
# CREATE ITEM
# -----------------------
def test_create_menu_item():
    response = client.post("/menu/", json={
        "name": "Burger",
        "description": "Cheeseburger",
        "price": 9.99,
        "category": "food",
        "available": True
    })

    assert response.status_code in [200, 201]
    data = response.json()
    assert data["name"] == "Burger"
    assert data["price"] == 9.99


# -----------------------
# GET ALL ITEMS
# -----------------------
def test_get_menu():
    response = client.get("/menu/")
    assert response.status_code == 200
    assert isinstance(response.json(), list)


# -----------------------
# GET SINGLE ITEM
# -----------------------
def test_get_menu_item():
    # first create item
    create = client.post("/menu/", json={
        "name": "Pizza",
        "description": "Pepperoni",
        "price": 12.99,
        "category": "food",
        "available": True
    })

    item_id = create.json()["id"]

    response = client.get(f"/menu/{item_id}")
    assert response.status_code == 200
    assert response.json()["id"] == item_id


# -----------------------
# UPDATE ITEM
# -----------------------
def test_update_menu_item():
    create = client.post("/menu/", json={
        "name": "Pasta",
        "description": "Alfredo",
        "price": 11.99,
        "category": "food",
        "available": True
    })

    item_id = create.json()["id"]

    response = client.put(f"/menu/{item_id}", json={
        "price": 13.99
    })

    assert response.status_code == 200
    assert response.json()["price"] == 13.99


# -----------------------
# DELETE ITEM
# -----------------------
def test_delete_menu_item():
    create = client.post("/menu/", json={
        "name": "Salad",
        "description": "Greek salad",
        "price": 7.99,
        "category": "food",
        "available": True
    })

    item_id = create.json()["id"]

    response = client.delete(f"/menu/{item_id}")
    assert response.status_code == 200

    # confirm it's gone
    response = client.get(f"/menu/{item_id}")
    assert response.status_code == 404