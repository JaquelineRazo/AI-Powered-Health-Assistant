from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database.database import get_db
from pydantic import BaseModel
from typing import List

router = APIRouter()

class GroceryItem(BaseModel):
    name: str
    quantity: str
    category: str

class GroceryList(BaseModel):
    items: List[GroceryItem]

@router.get("/{user_id}", response_model=GroceryList)
async def get_grocery_list(user_id: str, db: Session = Depends(get_db)):
     sample_grocery_list = GroceryList(items=[
        GroceryItem(name="Oatmeal", quantity="1 bag", category="Grains"),
        GroceryItem(name="Berries", quantity="1 punnet", category="Produce"),
        GroceryItem(name="Chicken Breast", quantity="500g", category="Meat")
    ])
     return sample_grocery_list