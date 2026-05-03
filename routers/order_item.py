from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from db import get_db
from models.order_item import OrderItem
from models.order import Order
from schemas.order_item import OrderItemCreate, OrderItemUpdate, OrderItemOut
from typing import List

router = APIRouter(prefix="/order-items", tags=["Order Items"])

@router.post("/", response_model=OrderItemOut)
def create_order_item(item: OrderItemCreate, db: Session = Depends(get_db)):
    order = db.query(Order).filter(Order.id == item.order_id).first()
    if not order:
        raise HTTPException(status_code=404, detail="Order not found")
    db_item = OrderItem(**item.dict())
    db.add(db_item)
    order.total_price += item.unit_price * item.quantity
    db.commit()
    db.refresh(db_item)
    return db_item

@router.get("/", response_model=List[OrderItemOut])
def get_order_items(db: Session = Depends(get_db)):
    return db.query(OrderItem).all()

@router.get("/{item_id}", response_model=OrderItemOut)
def get_order_item(item_id: int, db: Session = Depends(get_db)):
    item = db.query(OrderItem).filter(OrderItem.id == item_id).first()
    if not item:
        raise HTTPException(status_code=404, detail="Order item not found")
    return item

@router.get("/order/{order_id}", response_model=List[OrderItemOut])
def get_items_by_order(order_id: int, db: Session = Depends(get_db)):
    return db.query(OrderItem).filter(OrderItem.order_id == order_id).all()

@router.put("/{item_id}", response_model=OrderItemOut)
def update_order_item(item_id: int, updates: OrderItemUpdate, db: Session = Depends(get_db)):
    item = db.query(OrderItem).filter(OrderItem.id == item_id).first()
    if not item:
        raise HTTPException(status_code=404, detail="Order item not found")
    for key, value in updates.dict(exclude_none=True).items():
        setattr(item, key, value)
    db.commit()
    db.refresh(item)
    return item

@router.delete("/{item_id}")
def delete_order_item(item_id: int, db: Session = Depends(get_db)):
    item = db.query(OrderItem).filter(OrderItem.id == item_id).first()
    if not item:
        raise HTTPException(status_code=404, detail="Order item not found")
    db.delete(item)
    db.commit()
    return {"message": f"Order item {item_id} deleted"}