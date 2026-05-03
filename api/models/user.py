from sqlalchemy import Column, Integer, String, Enum
from db import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False)
    phone = Column(String, nullable=True)
    role = Column(Enum("customer", "staff", "chef", "manager", name="user_role"), default="customer")
    password = Column(String, nullable=False)