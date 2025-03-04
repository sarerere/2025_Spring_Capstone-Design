# https://fastapi.tiangolo.com/tutorial/body/#import-pydantics-basemodel
from fastapi import FastAPI
from pydantic import BaseModel

# class Item(BaseModel):
#     name: str
#     description: str | None = None
#     price: float
#     tax: float | None = None
    
class Todo(BaseModel):
    id: int
    item: str