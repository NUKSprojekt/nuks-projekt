from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey 
from sqlalchemy.orm import relationship

engine = create_engine("sqlite:///appdb.db", connect_args={"check_same_thread": False})

Base = declarative_base() 

class Rating(Base):
    __tablename__ = "ratings" 
    id = Column(Integer, primary_key=True, index=True)
    food = Column(Integer)
    ambient = Column(Integer)
    staff = Column(Integer)
    service = Column(Integer)
    price = Column(Integer)
    comment = Column(String(200)) 
    user_id = Column(String(50))
    restaurant_id = Column(Integer, ForeignKey("restaurants.id"))
    
    restaurant = relationship("Restaurant", back_populates="ratings")
"""
class User(Base):
    __tablename__ = "users" 
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, index=True)

    ratings = relationship("Rating", back_populates="user")
"""
class Restaurant(Base):
    __tablename__ = "restaurants" 
    id = Column(Integer, primary_key=True, index=True)
    restaurant_name = Column(String, index=True)
    food_type = Column(String)

    ratings = relationship("Rating", back_populates="restaurant")

