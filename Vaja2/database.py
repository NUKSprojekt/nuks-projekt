from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String 

engine = create_engine("sqlite:///tododatabase.db") # engine poganja DB

Base = declarative_base() # vrne class; baza za ta class, ki predstavlja tabelo v databazi

# class toDO predstavlja sql tabelo todos
# atributi v classu predstavljajo columns z imenom in tipom
# objekti v classu predstavljajo vrstico v tabeli


class ToDO(Base):
    __tablename__ = "todotable" 
    id = Column(Integer, primary_key=True) # id todos ukazov, tipa int, predstavlja primary key
    task = Column(String(50)) # taski so tipa string