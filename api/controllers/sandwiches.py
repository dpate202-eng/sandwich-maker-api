# controllers/sandwiches.py

from sqlalchemy.orm import Session
from ..models import models, schemas

# CREATE
def create(db: Session, sandwich: schemas.SandwichCreate):
    db_sandwich = models.Sandwich(
        name=sandwich.name,
        description=sandwich.description,
        price=sandwich.price
    )
    db.add(db_sandwich)
    db.commit()
    db.refresh(db_sandwich)
    return db_sandwich

# READ ALL
def read_all(db: Session):
    return db.query(models.Sandwich).all()

# READ ONE
def read_one(db: Session, sandwich_id: int):
    return db.query(models.Sandwich).filter(models.Sandwich.id == sandwich_id).first()

# UPDATE
def update(db: Session, sandwich: schemas.SandwichUpdate, sandwich_id: int):
    db_sandwich = db.query(models.Sandwich).filter(models.Sandwich.id == sandwich_id).first()
    if db_sandwich is None:
        return None
    for var, value in vars(sandwich).items():
        setattr(db_sandwich, var, value) if value is not None else None
    db.commit()
    db.refresh(db_sandwich)
    return db_sandwich

# DELETE
def delete(db: Session, sandwich_id: int):
    db_sandwich = db.query(models.Sandwich).filter(models.Sandwich.id == sandwich_id).first()
    if db_sandwich is None:
        return None
    db.delete(db_sandwich)
    db.commit()
    return db_sandwich