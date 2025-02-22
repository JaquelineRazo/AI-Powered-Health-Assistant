from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database.database import get_db
from app.models.user import User
from pydantic import BaseModel
from typing import List
import json

router = APIRouter()

class UserProfile(BaseModel): #Duplicate because it is used by the API endpoints
    userId: str
    healthGoals: List[str]
    dietaryRestrictions: List[str]
    preferences: dict
    exerciseRoutine: str = "Moderate"

@router.get("/{user_id}", response_model=UserProfile)
async def get_user_profile(user_id: str, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.user_id == user_id).first()
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")

    #Convert database columns (which are stored as strings) to lists/dicts for the pydantic model
    health_goals = json.loads(user.health_goals) if user.health_goals else []
    dietary_restrictions = json.loads(user.dietary_restrictions) if user.dietary_restrictions else []
    preferences = json.loads(user.preferences) if user.preferences else {}

    return UserProfile(userId=user.user_id, healthGoals=health_goals, dietaryRestrictions=dietaryRestrictions, preferences=preferences, exerciseRoutine=user.exercise_routine)


@router.put("/{user_id}", response_model=UserProfile)
async def update_user_profile(user_id: str, user_profile: UserProfile, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.user_id == user_id).first()
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")

    #Store the lists and dicts as JSON strings in the database
    user.health_goals = json.dumps(user_profile.healthGoals)
    user.dietary_restrictions = json.dumps(user_profile.dietaryRestrictions)
    user.preferences = json.dumps(user_profile.preferences)
    user.exercise_routine = user_profile.exerciseRoutine

    db.commit()
    db.refresh(user)

    return user_profile #Return the original pydantic model