from sqlalchemy import Column, Integer, String, Boolean
from .database import Base

class Product(Base):
    __tablename__ = "products"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    price = Column(Integer, index= True)
    description = Column(String, index=True)
    stock = Column(Boolean, index= True)
