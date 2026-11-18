from fastapi import FastAPI
from app.core.config import settings

app = FastAPI(
    title=settings.app_name,
    debug=settings.debug,
    version="0.1.0"
)

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