from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from db import get_db
from models.promo_code import PromoCode
from schemas.promo_code import PromoCodeCreate, PromoCodeUpdate, PromoCodeOut
from typing import List

router = APIRouter(prefix="/promo-codes", tags=["Promo Codes"])

@router.post("/", response_model=PromoCodeOut)
def create_promo_code(promo: PromoCodeCreate, db: Session = Depends(get_db)):
    existing = db.query(PromoCode).filter(PromoCode.code == promo.code).first()
    if existing:
        raise HTTPException(status_code=400, detail="Promo code already exists")
    db_promo = PromoCode(**promo.dict())
    db.add(db_promo)
    db.commit()
    db.refresh(db_promo)
    return db_promo

@router.get("/", response_model=List[PromoCodeOut])
def get_promo_codes(db: Session = Depends(get_db)):
    return db.query(PromoCode).all()

@router.get("/{promo_id}", response_model=PromoCodeOut)
def get_promo_code(promo_id: int, db: Session = Depends(get_db)):
    promo = db.query(PromoCode).filter(PromoCode.id == promo_id).first()
    if not promo:
        raise HTTPException(status_code=404, detail="Promo code not found")
    return promo

@router.get("/validate/{code}", response_model=PromoCodeOut)
def validate_promo_code(code: str, db: Session = Depends(get_db)):
    promo = db.query(PromoCode).filter(PromoCode.code == code, PromoCode.active == True).first()
    if not promo:
        raise HTTPException(status_code=404, detail="Invalid or inactive promo code")
    return promo

@router.put("/{promo_id}", response_model=PromoCodeOut)
def update_promo_code(promo_id: int, updates: PromoCodeUpdate, db: Session = Depends(get_db)):
    promo = db.query(PromoCode).filter(PromoCode.id == promo_id).first()
    if not promo:
        raise HTTPException(status_code=404, detail="Promo code not found")
    for key, value in updates.dict(exclude_none=True).items():
        setattr(promo, key, value)
    db.commit()
    db.refresh(promo)
    return promo

@router.delete("/{promo_id}")
def delete_promo_code(promo_id: int, db: Session = Depends(get_db)):
    promo = db.query(PromoCode).filter(PromoCode.id == promo_id).first()
    if not promo:
        raise HTTPException(status_code=404, detail="Promo code not found")
    db.delete(promo)
    db.commit()
    return {"message": f"Promo code {promo_id} deleted"}