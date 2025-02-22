# grocery.py
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from .database import Base

class GroceryItem(Base):
    __tablename__ = "grocery_items"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    quantity = Column(String)
    category = Column(String)
    grocery_list_id = Column(Integer, ForeignKey("grocery_lists.id"))

    grocery_list = relationship("GroceryList", back_populates="items")

class GroceryList(Base):
    __tablename__ = "grocery_lists"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id")) # Link to the user that owns the list

    items = relationship("GroceryItem", back_populates="grocery_list")
    user = relationship("User")