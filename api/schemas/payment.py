from pydantic import BaseModel
from typing import Optional

class PaymentCreate(BaseModel):
    order_id: int
    method: str
    amount: float

class PaymentUpdate(BaseModel):
    status: Optional[str] = None
    method: Optional[str] = None

class PaymentOut(BaseModel):
    id: int
    order_id: int
    method: str
    amount: float
    status: str

    class Config:
        from_attributes = True
