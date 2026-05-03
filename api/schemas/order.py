from pydantic import BaseModel
from typing import Optional

class OrderCreate(BaseModel):
    customer_name: str
    customer_phone: str
    customer_address: Optional[str] = None
    order_type: Optional[str] = "takeout"
    user_id: Optional[int] = None
    promo_code_id: Optional[int] = None

class OrderUpdate(BaseModel):
    status: Optional[str] = None
    customer_address: Optional[str] = None
    order_type: Optional[str] = None

class OrderOut(BaseModel):
    id: int
    customer_name: str
    customer_phone: str
    customer_address: Optional[str]
    order_type: str
    status: str
    total_price: float
    user_id: Optional[int]
    promo_code_id: Optional[int]

    class Config:
        from_attributes = True
