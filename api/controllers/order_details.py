# controllers/order_details.py
from sqlalchemy.orm import Session
from ..models import models, schemas

def create(db: Session, order_detail: schemas.OrderDetailCreate):
    db_order_detail = models.OrderDetail(
        order_id=order_detail.order_id,
        sandwich_id=order_detail.sandwich_id,
        amount=order_detail.amount
    )
    db.add(db_order_detail)
    db.commit()
    db.refresh(db_order_detail)
    return db_order_detail

def read_all(db: Session):
    return db.query(models.OrderDetail).all()

def read_one(db: Session, order_detail_id: int):
    return db.query(models.OrderDetail).filter(models.OrderDetail.id == order_detail_id).first()

def update(db: Session, order_detail: schemas.OrderDetailUpdate, order_detail_id: int):
    db_order_detail = db.query(models.OrderDetail).filter(models.OrderDetail.id == order_detail_id).first()
    if db_order_detail is None:
        return None
    for var, value in vars(order_detail).items():
        if value is not None:
            setattr(db_order_detail, var, value)
    db.commit()
    db.refresh(db_order_detail)
    return db_order_detail

def delete(db: Session, order_detail_id: int):
    db_order_detail = db.query(models.OrderDetail).filter(models.OrderDetail.id == order_detail_id).first()
    if db_order_detail is None:
        return None
    db.delete(db_order_detail)
    db.commit()
    return db_order_detail