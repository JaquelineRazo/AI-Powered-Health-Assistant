from fastapi import FastAPI
from app.api import router as api_router #Import the aggregated router
from app.database.database import engine
from app.database.database import Base #Import


Base.metadata.create_all(bind=engine) # Add this line!

app = FastAPI()

app.include_router(api_router) #Include the aggregated router

@app.get("/")
async def read_root():
    return {"message": "FastAPI API - Jackie Health"}