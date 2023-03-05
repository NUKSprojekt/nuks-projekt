from typing import Union
from fastapi import FastAPI
from database import Base, engine, ToDO
import schemas
from sqlalchemy.orm import Session # orm povezuje objekte (maps) v kodi z database tabele (relations)


Base.metadata.create_all(engine)


app = FastAPI()


@app.get("/")
def read_root():
    """
    Default API calli
    """
    return {"TODO app"}


@app.post("/add")
def create_todo(todo: schemas.ToDoTask):
    session = Session(bind = engine, expire_on_commit=False)
    tododb = ToDO(task = todo.task)

    session.add(tododb)
    session.commit()
    id = tododb.id
    session.close()
    return f"Created new todo with id: {id}"

    return "Create TODO"

@app.get("/get/{id}")
def read_todo(id: int):
    return "Read todo item with id {id}"

@app.put("/change/{id}")
def change_todo(id: int):
    return "Read todo item with id {id}"

@app.delete("/delete/{id}")
def change_todo(id: int):
    return "Delete todo item with id {id}"

@app.get("list")
def read_todo_list():
    return "All todos"