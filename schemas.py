import imp
from typing import Union
from fastapi import FastAPI, Query
import database

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/orders/{order_id}")
async def read_item(order_id: int):
    return database.add_order(order_id)

@app.get("/orders")
async def get_orders(
    offset: int = Query(title="Database records offset", ge=0, default=0),
    limit: int = Query(title="Limit of records returned", ge=1, default=50)):
    return database.get_orders(offset, limit)

@app.post("/orders")
async def get_orders(email: str, owner: str, phone_number: str):
    return database.add_order(email, owner, phone_number)

@app.get("/connect")
async def db_connect():
    return {"message": database.connect()}
