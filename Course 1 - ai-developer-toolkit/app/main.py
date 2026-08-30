from fastapi import FastAPI

from app.schemas.generation import GenerationRequest, GenerationResponse
from app.services.ai_service import generate_text


app = FastAPI(
    title="AI Developer Toolkit",
    description="AI-powered developer toolkit",
    version="1.0.0"
)


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


@app.post("/generate", response_model=GenerationResponse)
def generate(request: GenerationRequest):
    result = generate_text(request.prompt)

    return GenerationResponse(result=result)