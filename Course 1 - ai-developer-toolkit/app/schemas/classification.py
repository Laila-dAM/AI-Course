from pydantic import BaseModel, Field


class ClassificationRequest(BaseModel):
    text: str = Field(
        min_length=1,
        max_length=5000
    )


class ClassificationResponse(BaseModel):
    category: str