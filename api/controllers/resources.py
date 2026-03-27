# controllers/resources.py
from sqlalchemy.orm import Session
from ..models import models, schemas

def create(db: Session, resource: schemas.ResourceCreate):
    db_resource = models.Resource(
        item=resource.item,
        amount=resource.amount
    )
    db.add(db_resource)
    db.commit()
    db.refresh(db_resource)
    return db_resource

def read_all(db: Session):
    return db.query(models.Resource).all()

def read_one(db: Session, resource_id: int):
    return db.query(models.Resource).filter(models.Resource.id == resource_id).first()

def update(db: Session, resource: schemas.ResourceUpdate, resource_id: int):
    db_resource = db.query(models.Resource).filter(models.Resource.id == resource_id).first()
    if db_resource is None:
        return None
    for var, value in vars(resource).items():
        if value is not None:
            setattr(db_resource, var, value)
    db.commit()
    db.refresh(db_resource)
    return db_resource

def delete(db: Session, resource_id: int):
    db_resource = db.query(models.Resource).filter(models.Resource.id == resource_id).first()
    if db_resource is None:
        return None
    db.delete(db_resource)
    db.commit()
    return db_resource