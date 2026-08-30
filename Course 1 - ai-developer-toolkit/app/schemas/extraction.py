from pydantic import BaseModel, Field


class ExtractionRequest(BaseModel):
    text: str = Field(
        min_length=1,
        max_length=10000
    )


class ExtractionResponse(BaseModel):
    information: str