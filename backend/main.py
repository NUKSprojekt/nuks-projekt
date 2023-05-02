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

origins = [
    "http://localhost",
    "http://0.0.0.0:8082",
    "http://localhost:8082",
    "http://212.101.137.104:8082",
    "http://212.101.137.104:8080",
    "http://127.0.0.1:8080",
    "*"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/ratings")
@version(1)
def read_ratings():
    session = Session(bind = engine, expire_on_commit=False)
    rating_all = session.query(Rating).all()
    session.close()
    return rating_all  

@app.get("/rating/{rating_id}")
@version(1)
def read_rating(id: int):
    session = Session(bind = engine, expire_on_commit=False)
    rating = session.query(Rating).get(id)
    session.close()
    if not rating:
        raise HTTPException(status_code=404, detail=f"Rating with id {id} does not exist.")
    return rating

@app.get("/ratings/restaurant/{restaurant_id}")
@version(1)
def read_rating(id: int):
    session = Session(bind = engine, expire_on_commit=False)
    ratings = session.query(Rating).filter_by(restaurant_id=id).all()
    session.close()

    all_ratings = []
    for rating in ratings:
        avg = round(((rating.food + rating.ambient + rating.staff + rating.service + rating.price) / 5), 1)
        avgratings = {
            'id': rating.id,
            'restaurant_id': rating.restaurant_id,
            'user_id': rating.user_id,
            'food': rating.food,
            'ambient': rating.ambient,
            'staff': rating.staff,
            'service': rating.service,
            'price': rating.price,
            'comment': rating.comment,
            'average': avg
        }
        all_ratings.append(avgratings)
    if not all_ratings:
        raise HTTPException(status_code=404, detail=f"Rating with id {id} does not exist.")
    return all_ratings

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

@app.get("/restaurants/averages")
@version(1)
def get_all_restaurants_rating_averages():
    try:
        session = Session(bind = engine, expire_on_commit=False)
        restaurants = session.query(Restaurant).all()
        session.close()

        all_averages = []
        
        for restaurant in restaurants:
            session = Session(bind = engine, expire_on_commit=False)
            ratings = session.query(Rating).filter_by(restaurant_id=restaurant.id).all()
            session.close()

            total_ratings = len(ratings)
            if total_ratings == 0:
                avg_food = 0
                avg_ambient = 0
                avg_staff = 0
                avg_service = 0
                avg_price = 0
                avg = 0
            else:
                avg_food = round((sum([rating.food for rating in ratings]) / total_ratings), 1)
                avg_ambient = round((sum([rating.ambient for rating in ratings]) / total_ratings), 1)
                avg_staff = round((sum([rating.staff for rating in ratings]) / total_ratings), 1)
                avg_service = round((sum([rating.service for rating in ratings]) / total_ratings), 1)
                avg_price = round((sum([rating.price for rating in ratings]) / total_ratings), 1)
                avg = round(((avg_food + avg_ambient + avg_staff + avg_service + avg_price) / 5), 1)

            averages = {
                'restaurant_id': restaurant.id,
                'restaurant_name': restaurant.restaurant_name,
                'food': avg_food,
                'ambient': avg_ambient,
                'staff': avg_staff,
                'service': avg_service,
                'price': avg_price,
                'average': avg
            }
            
            all_averages.append(averages)
   
        return all_averages

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.put("/rating/update/{id}")
@version(1)
def update_rating(id: int, comment: str):
    session = Session(bind = engine, expire_on_commit=False)
    rating = session.query(Rating).get(id)
    if rating:
        rating.comment = comment
        session.commit()
    session.close()
    if not rating:
        raise HTTPException(status_code=404, detail=f"Rating with id {id} does not exist.")
    return rating


@app.get("/restaurants")
@version(1)
def read_restaurants():
    session = Session(bind = engine, expire_on_commit=False)
    restaurant_all = session.query(Restaurant).all()
    session.close()
    return restaurant_all

@app.get("/restaurant/{restaurant_id}")
@version(1)
def read_restaurant(id: int):
    session = Session(bind = engine, expire_on_commit=False)
    restaurant = session.query(Restaurant).get(id)
    session.close()
    if not restaurant:
        raise HTTPException(status_code=404, detail=f"Restaurant with id {id} does not exist.")
    return restaurant

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


