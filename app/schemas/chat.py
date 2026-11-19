from pydantic import BaseModel, Field, field_validator

class ChatRequest(BaseModel):
    message: str = Field(
        min_length=1,
        max_length=4000,
        description="The message submitted by user.",
    )

    @field_validator("message", mode="before")
    @classmethod
    def strip_message(cls, value:object) ->object:
        if isinstance(value, str):
            return value.strip()

        return value

class ChatResponse(BaseModel):
    reply: str