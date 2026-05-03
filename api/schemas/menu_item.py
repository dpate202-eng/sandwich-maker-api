from pydantic import BaseModel
from typing import Optional

class MenuItemCreate(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    calories: Optional[int] = None
    category: Optional[str] = None
    available: Optional[bool] = True

class MenuItemUpdate(BaseModel):
    name: Optional[str] = None
    description: Optional[str] = None
    price: Optional[float] = None
    calories: Optional[int] = None
    category: Optional[str] = None
    available: Optional[bool] = None

class MenuItemOut(BaseModel):
    id: int
    name: str
    description: Optional[str]
    price: float
    calories: Optional[int]
    category: Optional[str]
    available: bool

    class Config:
        from_attributes = True
