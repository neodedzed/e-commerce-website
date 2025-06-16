from sqlalchemy import Column, Integer, String
from database.db import Base

def User(Base):
    __tablename__='user'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    address = Column(String)  
    phone = Column(String, nullable=False)
    username = Column(String, nullable=False)
    password = Column(String, nullable=False)
