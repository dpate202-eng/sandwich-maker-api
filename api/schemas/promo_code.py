from pydantic import BaseModel
from typing import Optional

class PromoCodeCreate(BaseModel):
    code: str
    discount_percent: float
    active: Optional[bool] = True

class PromoCodeUpdate(BaseModel):
    discount_percent: Optional[float] = None
    active: Optional[bool] = None

class PromoCodeOut(BaseModel):
    id: int
    code: str
    discount_percent: float
    active: bool

    class Config:
        from_attributes = True
