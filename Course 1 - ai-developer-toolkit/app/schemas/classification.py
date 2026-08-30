from typing import Literal

from pydantic import BaseModel


class ClassificationRequest(BaseModel):
    text: str


class ClassificationResponse(BaseModel):
    category: Literal["positive", "negative", "neutral"]