from sqlalchemy import Column, Integer, String, Float, Boolean
from db import Base

class MenuItem(Base):
    __tablename__ = "menu_items"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    description = Column(String, nullable=True)
    price = Column(Float, nullable=False)
    calories = Column(Integer, nullable=True)
    category = Column(String, nullable=True)
    available = Column(Boolean, default=True)