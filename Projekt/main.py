from fastapi import FastAPI
import schemas, models
from sqlalchemy.orm import Session
from database import Base, engine, Rating, User, Restaurant

Base.metadata.create_all(engine)

app = FastAPI()

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/")
def read_all():
    """
    Default page
    (Treba dodat funkcije za izpis vseh restavracij, profilne slike, povprečne ocene in najaktualnejši komentar)
    """
    return "Default page"

@app.get("/restaurants/{food_type}") # stran za vrste prehrane (kitajska, indijska...)
def read_type(food_type: str)
    return {"food_type": food_type}

@app.get("/restaurants/{restaurant_id}") # stran za posamezno restavracijo
def read_id(restaurant_id: int, db: Session = Depends(get_db)):
    """
    Treba dodat, da se izpišejo vse ocene uporabnikov (kot post s slikami, ocenami, skupno povprečno oceno in komentarjem)
    """

    return {"restaurant_id": restaurant_id}

@app.post("/ratings/", response_model=schemas.rating)
def add_rating(rating: schemas.rating, db: Session = Depends(get_db)):

    session = Session(bind = engine, expire_on_commit=False)
    ratingdb = Rating(task = todo.task)

    session.add(tododb)
    session.commit()
    id = tododb.id
    session.close()
    return f"Created new todo with id: {id}"
    """
    Treba dodat še, da se request podatki zapišejo še v DB in poračunajo nove povprečne ocene
    """
    return {"Adding rating and comment": rating}

