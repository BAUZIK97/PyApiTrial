import imp
from typing import Union
from fastapi import FastAPI
from pydantic import BaseModel
from database import connect

app = FastAPI()

class Item(BaseModel):
    name: str
    description: Union[str, None] = None
    price: float
    tax: Union[float, None] = None

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/orders/{order_id}")
async def read_item(order_id: int):
    return {"message": order_id}

@app.get("/orders")
async def get_orders():
    return {"message": 123}

@app.get("/connect")
async def db_connect():
    return {"message": connect()}
