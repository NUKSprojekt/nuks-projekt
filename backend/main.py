from typing import Union
from fastapi import FastAPI, HTTPException, status, Response
import schemas
from sqlalchemy.orm import Session
from database import Base, engine, Rating, Restaurant
from fastapi_versioning import version, VersionedFastAPI
from fastapi.middleware.cors import CORSMiddleware

Base.metadata.create_all(engine)

app = FastAPI()
app = VersionedFastAPI(app, version_format='(major)', prefix_format='/v{major}')

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:8082"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/a")
@version(1)
def read_root():
    return {"Hello": "World"}

@app.get("/ratings")
@version(1)
def read_ratings():
    session = Session(bind = engine, expire_on_commit=False)
    rating_all = session.query(Rating).all()
    session.close()
    return rating_all
    """
    Default page
    (Treba dodat funkcije za izpis vseh restavracij, profilne slike, povprečne ocene in najaktualnejši komentar)
    (Zaenkrat samo lista vseh ocen)
  
"""    

@app.get("/rating/{rating_id}")
@version(1)
def read_rating(id: int):
    session = Session(bind = engine, expire_on_commit=False)
    rating = session.query(Rating).get(id)
    session.close()
    if not rating:
        raise HTTPException(status_code=404, detail=f"Rating with id {id} does not exist.")
    return rating

@app.post("/rating", status_code=status.HTTP_201_CREATED)
@version(1)
def add_rating(rating: schemas.rating):
    session = Session(bind = engine, expire_on_commit=False)
    rating = Rating(restaurant_id = rating.restaurant_id, user_id = rating.user, food = rating.food, ambient = rating.ambient, staff = rating.staff, service = rating.service, price = rating.price, comment = rating.comment)

    session.add(rating)
    session.commit()
    id = rating.id
    session.close()
    return f"Added new rating with id: {id}"

@app.delete("/rating_delete/{rating_id}")
@version(1)
def delete_rating(id: int):
    session = Session(bind = engine, expire_on_commit=False)
    rating = session.query(Rating).get(id)
    if rating:
        session.delete(rating)
        session.commit()
        session.close()
    else:
        session.close()
        raise HTTPException(status_code=404, detail=f"Rating with id {id} does not exist.")
    return {"Delete rating with id": id}

@app.get("/restaurants")
@version(1)
def read_restaurants():
    session = Session(bind = engine, expire_on_commit=False)
    restaurant_all = session.query(Restaurant).all()
    session.close()
    return restaurant_all

@app.get("/restaurant/{restaurant_id}") # stran za posamezno restavracijo
@version(1)
def read_restaurant(id: int):
    session = Session(bind = engine, expire_on_commit=False)
    restaurant = session.query(Restaurant).get(id)
    session.close()
    if not restaurant:
        raise HTTPException(status_code=404, detail=f"Restaurant with id {id} does not exist.")
    return restaurant
    """
    Treba dodat, da se izpišejo vse ocene uporabnikov (kot post s slikami, ocenami, skupno povprečno oceno in komentarjem)
    """

    #return {"restaurant_id": restaurant_id}

@app.post("/restaurant", status_code=status.HTTP_201_CREATED)
@version(1)
def add_restaurant(restaurant: schemas.restaurant):
    session = Session(bind = engine, expire_on_commit=False)
    restaurant = Restaurant(restaurant_name = restaurant.restaurant_name, food_type = restaurant.food_type)

    session.add(restaurant)
    session.commit()
    id = restaurant.id
    session.close()
    return f"Added new restaurant with id: {id}"

@app.delete("/restaurant_delete/{restaurant_id}")
@version(1)
def delete_restaurant(id: int):
    session = Session(bind = engine, expire_on_commit=False)
    restaurant = session.query(Restaurant).get(id)
    if restaurant:
        session.delete(restaurant)
        session.commit()
        session.close()
    else:
        session.close()
        raise HTTPException(status_code=404, detail=f"Restaurant with id {id} does not exist.")
    return {"Delete restaurant with id": id}

@app.get("/food_type/{food_type}") # stran za vrste prehrane (kitajska, indijska...)
@version(1)
def read_type(food_type: str):
    session = Session(bind = engine, expire_on_commit=False)
    restaurants = session.query(Restaurant).filter(Restaurant.food_type == food_type).all()
    session.close()
    if not restaurants:
        raise HTTPException(status_code=404, detail=f"There is no restaurants with food type {food_type}.")
    return f"Restaurants with food type {food_type}:", restaurants

"""
@app.get("/users")
@version(1)
def read_users():
    session = Session(bind = engine, expire_on_commit=False)
    user_all = session.query(User).all()
    session.close()
    return user_all

@app.get("/user/{user_id}")
@version(1)
def read_user(id: int):
    session = Session(bind = engine, expire_on_commit=False)
    user = session.query(User).get(id)
    session.close()
    if not user:
        raise HTTPException(status_code=404, detail=f"User with id {id} does not exist.")
    return user

@app.post("/user", status_code=status.HTTP_201_CREATED)
@version(1)
def add_user(user: schemas.user):
    session = Session(bind = engine, expire_on_commit=False)
    user = User(username = user.username)

    session.add(user)
    session.commit()
    id = user.id
    session.close()
    return f"Added new user with id: {id}"

@app.delete("/user_delete/{user_id}")
@version(1)
def delete_user(id: int):
    session = Session(bind = engine, expire_on_commit=False)
    user = session.query(User).get(id)
    if user:
        session.delete(user)
        session.commit()
        session.close()
    else:
        session.close()
        raise HTTPException(status_code=404, detail=f"User with id {id} does not exist.")
    return {"Delete user with id": id}
"""

