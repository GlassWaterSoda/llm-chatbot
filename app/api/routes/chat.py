from fastapi import APIRouter
from app.schemas.chat import ChatRequest, ChatResponse
from openai import AsyncOpenAI
from app.core.config import settings

if settings.openai_api_key is None:
    raise RuntimeError(
        "OPENAI_API_KEY is missing. "
        "Add it to your local .env file."
    )

client = AsyncOpenAI(
    api_key=settings.openai_api_key.get_secret_value()
)



router = APIRouter(
    prefix="/chat",
    tags=["Chat"]
)

@router.post("", response_model=ChatResponse)
async def create_chat(request: ChatRequest) -> ChatResponse:
    """
    Accept a user message and return a mock response
    """

    response = await client.responses.create(
        model="gpt-5.4-mini",
        instructions="You multi-knowledge based assistant who replies in breif, concise and accurately manner",
        input=request.message
    )

    return ChatResponse(
        reply=f"Response: {response.output_text}"
    )
