from pydantic import BaseModel

class rating(BaseModel):
    restaurant_id: int
    user: str 
    food: int 
    ambient: int
    staff: int
    service: int
    price: int
    comment: str

class restaurant(BaseModel):
    restaurant_name: str
    food_type: str

class user(BaseModel):
    username: str