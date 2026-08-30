from pydantic import BaseModel, Field


class SummarizationRequest(BaseModel):
    text: str = Field(
        min_length=1,
        max_length=10000
    )


class SummarizationResponse(BaseModel):
    summary: str