from pydantic import BaseModel
from typing import Optional

class OrderItemCreate(BaseModel):
    order_id: int
    menu_item_id: int
    quantity: Optional[int] = 1
    unit_price: float

class OrderItemUpdate(BaseModel):
    quantity: Optional[int] = None

class OrderItemOut(BaseModel):
    id: int
    order_id: int
    menu_item_id: int
    quantity: int
    unit_price: float

    class Config:
        from_attributes = True
