from fastapi import FastAPI
from app.core.config import settings
from pydantic import BaseModel
from app.api.routes.chat import router as chat_router

app = FastAPI(
    title=settings.app_name,
    debug=settings.debug,
    version="0.1.0"
)

app.include_router(chat_router)



class User(BaseModel):
    fname: str
    lname: str
    email: str
    no_of_house: int
    is_avail : bool = True


car_list = []

@app.get("/", tags=["General"])
async def root() -> dict[str, str]:
    """Return basic information about the API."""
    return {
        "message":"LLM Chatbot API is running."
    }

@app.get("/health", tags=["Health"])
async def health_check() -> dict[str, str]:
    """Check whether the application is responding."""
    return{
        "status":"ok"
    }

@app.post("/user", tags=["General"])
async def add_user(user: User):
    """Get user info from request body"""
    return {
        "name": user.fname + " " +user.lname,
        "email": user.email,
        "no_of_house": user.no_of_house,
        "is_available": user.is_avail
    }
