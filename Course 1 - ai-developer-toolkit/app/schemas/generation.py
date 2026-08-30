from pydantic import BaseModel


class GenerationRequest(BaseModel):
    prompt: str


class GenerationResponse(BaseModel):
    result: str