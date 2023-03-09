from pydantic import BaseModel

class rating(BaseModel): 
    name: str
    food: int
    ambient: int
    staff: int
    service: int
    price: int
    comment: str

    class Config:
        orm_mode = True
