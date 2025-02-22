from sqlalchemy import Column, Integer, String, ForeignKey, Text
from sqlalchemy.orm import relationship
from .database import Base  # Relative import for the Base class

class Meal(Base):
    __tablename__ = "meals"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    ingredients = Column(String, nullable=True) #Store as JSON string
    recipe = Column(Text, nullable=True)
    calories = Column(Integer, nullable=True)
    user_id = Column(Integer, ForeignKey("users.id")) #Foreign Key

    owner = relationship("User", back_populates="meals")  #Relationship with User