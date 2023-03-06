from fastapi import FastAPI
import schemas
from sqlalchemy.orm import Session
from database import Base, engine

app = FastAPI()


@app.get("/")
def home():
    """
    Default page
    (Treba dodat funkcije za izpis vseh restavracij, profilne slike, povprečne ocene in najaktualnejši komentar)
    """
    return "Default page"

@app.get("/restaurants/{food_type}") # stran za vrste prehrane (kitajska, indijska...)
def read_type(food_type: str)
    return {"food_type": food_type}

@app.get("/restaurants/{restaurant_id}") # stran za posamezno restavracijo
def read_type(restaurant_id: str)
    """
    Treba dodat, da se izpišejo vse ocene uporabnikov (kot post s slikami, ocenami, skupno povprečno oceno in komentarjem)
    """
    return {"restaurant_id": restaurant_id}

@app.post("/rating")
def add_rating(rating: schemas.rating)
    """
    Treba dodat še, da se request podatki zapišejo še v DB
    """
    return {"Adding rating and comment": rating}

@app.put("/") # povprečna ocena kategorij (ambient, hrana...) in skupna povprečna ocena
def update_rating():
    """
    Treba dodat funkcijo, ki glede na vse ocene računa povprečne ocene
    """
    return ""

    
