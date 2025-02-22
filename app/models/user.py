from sqlalchemy import Column, Integer, String, Float
from sqlalchemy.orm import relationship
from .database import Base  # Relative import for the Base class

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(String, unique=True, index=True)  # Use this for linking to Firestore data
    health_goals = Column(String, nullable=True) # Store as JSON string.
    dietary_restrictions = Column(String, nullable=True) #Store as JSON string
    preferences = Column(String, nullable=True)  #Store as JSON string
    exercise_routine = Column(String, nullable=True)
    weight_kg = Column(Float, nullable=True)
    age = Column(Integer, nullable=True)

    meals = relationship("Meal", back_populates="owner")  #Relationship with Meal