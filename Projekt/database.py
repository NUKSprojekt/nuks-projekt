from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String 
from sqlalchemy.orm import relationship

engine = create_engine("sqlite:///appdb.db", connect_args={"check_same_thread": False})

Base = declarative_base() 

class Restaurant(Base):
    __tablename__ = "restaurants" 
    id = Column(String, primary_key=True) 
    food = Column(Integer)
    ambient = Column(Integer)
    staff = Column(Integer)
    service = Column(Integer)
    price = Column(Integer)
    rating = Column(Integer)
    comment = Column(String(50)) 

"""
Treba dodat še relationship?
"""

class User(Base):
    __tablename__ = "users" 
    id = Column(String, primary_key=True)
    restaurant = Column(String)  
    food = Column(Integer)
    ambient = Column(Integer)
    staff = Column(Integer)
    service = Column(Integer)
    price = Column(Integer)
    rating = Column(Integer)
    comment = Column(String(50)) 