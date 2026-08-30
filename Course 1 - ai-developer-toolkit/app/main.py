from fastapi import FastAPI
from pydantic import BaseModel

from app.services.ai_service import generate_text


app = FastAPI(
    title="AI Developer Toolkit",
    description="AI-powered developer toolkit",
    version="1.0.0"
)


class GenerationRequest(BaseModel):
    prompt: str


@app.get("/")
def root():
    return {
        "message": "AI Developer Toolkit API",
        "status": "running"
    }


@app.get("/health")
def health():
    return {
        "status": "healthy"
    }


@app.post("/generate")
def generate(request: GenerationRequest):
    result = generate_text(request.prompt)

    return {
        "result": result
    }