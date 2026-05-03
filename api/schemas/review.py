from pydantic import BaseModel
from typing import Optional

class ReviewCreate(BaseModel):
    order_id: int
    user_id: Optional[int] = None
    rating: int
    comment: Optional[str] = None

class ReviewUpdate(BaseModel):
    rating: Optional[int] = None
    comment: Optional[str] = None

class ReviewOut(BaseModel):
    id: int
    order_id: int
    user_id: Optional[int]
    rating: int
    comment: Optional[str]

    class Config:
        from_attributes = True
