from fastapi import APIRouter

from .users import router as users_router
from .meal_plans import router as meal_plans_router
from .grocery_lists import router as grocery_lists_router

router = APIRouter()
router.include_router(users_router, prefix="/users", tags=["users"])
router.include_router(meal_plans_router, prefix="/meal_plans", tags=["meal_plans"])
router.include_router(grocery_lists_router, prefix="/grocery_lists", tags=["grocery_lists"])