from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# 1. Define a data model for POST and PUT requests
class Item(BaseModel):
    name: str
    description: str | None = None
    price: float

items_db = {}

@app.get("/items/{item_id}")
async def read_item(item_id: int):
    return {"item_id": item_id, "data": items_db.get(item_id)}

@app.post("/items/{item_id}")
async def create_item(item_id: int, item: Item):
    items_db[item_id] = item
    return {"message": "Item created", "item": item}

@app.put("/items/{item_id}")
async def update_item(item_id: int, item: Item):
    items_db[item_id] = item
    return {"message": "Item updated", "item": item}
