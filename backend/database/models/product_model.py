from sqlalchemy import Column, Integer, String
from database.db import Base

class Product(Base):
    __tablename__='product'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    quantity = Column(Integer, nullable=False)