from pydantic import BaseModel, Field


class GenerationRequest(BaseModel):
    prompt: str = Field(
        min_length=1,
        max_length=5000
    )


class GenerationResponse(BaseModel):
    result: str