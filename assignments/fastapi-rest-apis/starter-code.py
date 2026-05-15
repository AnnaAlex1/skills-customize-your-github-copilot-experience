from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List

app = FastAPI()

class Item(BaseModel):
    id: int
    name: str
    description: str
    price: float
    in_stock: bool

items_db: List[Item] = [
    Item(id=1, name="Notebook", description="A journal for class notes.", price=3.99, in_stock=True),
    Item(id=2, name="Pen", description="A blue ink pen.", price=1.49, in_stock=True),
]

@app.get("/")
def read_root():
    return {"message": "Welcome to the FastAPI item store API!"}

@app.get("/items/")
def read_items():
    return items_db

@app.post("/items/")
def create_item(item: Item):
    items_db.append(item)
    return item

@app.get("/items/{item_id}")
def read_item(item_id: int):
    for item in items_db:
        if item.id == item_id:
            return item
    raise HTTPException(status_code=404, detail="Item not found")

@app.put("/items/{item_id}")
def update_item(item_id: int, updated_item: Item):
    for index, item in enumerate(items_db):
        if item.id == item_id:
            items_db[index] = updated_item
            return updated_item
    raise HTTPException(status_code=404, detail="Item not found")

@app.delete("/items/{item_id}")
def delete_item(item_id: int):
    for index, item in enumerate(items_db):
        if item.id == item_id:
            del items_db[index]
            return {"detail": "Item deleted"}
    raise HTTPException(status_code=404, detail="Item not found")
