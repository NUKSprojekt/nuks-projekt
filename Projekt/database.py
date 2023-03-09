from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey 
from sqlalchemy.orm import relationship

engine = create_engine("sqlite:///appdb.db", connect_args={"check_same_thread": False})

Base = declarative_base() 

class Rating(Base):
    __tablename__ = "ratings" 
    id = Column(Integer, primary_key=True)
    restaurant_id = Column(String, ForeignKey("restaurants.id"))
    food = Column(Integer)
    ambient = Column(Integer)
    staff = Column(Integer)
    service = Column(Integer)
    price = Column(Integer)
    comment = Column(String(50)) 
    user_id = Column(Integer, ForeignKey("users.id"))

    user = relationship("User", back_populates="ratings")

class User(Base):
    __tablename__ = "users" 
    id = Column(Integer, primary_key=True)
    username = Column(String)

    rating_u = relationship("Rating", back_populates="user")

class Restaurant(Base):
    __tablename__ = "restaurants" 
    id = Column(Integer, primary_key=True)
    restaurant_name = Column(String)
    food_type = Column(String)

    rating_r = relationship("Rating", back_populates="restaurants")