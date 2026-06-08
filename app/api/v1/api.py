from fastapi import APIRouter
from app.api.v1.endpoints import auth, books, users

api_router = APIRouter()

# Keep existing URL structure by not adding extra prefixes here
api_router.include_router(auth.router, tags=["auth"])
api_router.include_router(books.router, tags=["books"])
api_router.include_router(users.router, tags=["users"])
