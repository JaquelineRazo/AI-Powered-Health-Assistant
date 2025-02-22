from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database.database import get_db
from pydantic import BaseModel
from typing import List

router = APIRouter()

class MealPlan(BaseModel):
    meals: List[dict] #Each dict represents a meal (name, ingredients, recipe, nutrition info)

@router.post("/{user_id}", response_model=MealPlan)
async def request_meal_plan(user_id: str, db: Session = Depends(get_db)):
    #  Eventually, this needs to use the database
    # You'd get user info from db.query(User).filter(User.user_id == user_id).first()
    # and pass it to the Meal Planning AI

    sample_meal_plan = MealPlan(meals=[
        {"name": "Breakfast: Oatmeal with berries", "ingredients": ["oatmeal", "berries", "milk"], "recipe": "Mix ingredients and cook", "nutrition": {"calories": 300}},
        {"name": "Lunch: Salad with grilled chicken", "ingredients": ["salad", "chicken", "dressing"], "recipe": "Assemble salad", "nutrition": {"calories": 400}},
        {"name": "Dinner: Salmon with vegetables", "ingredients": ["salmon", "vegetables"], "recipe": "Bake salmon and steam vegetables", "nutrition": {"calories": 500}}
    ])
    return sample_meal_plan