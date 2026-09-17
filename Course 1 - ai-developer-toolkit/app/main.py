from fastapi import FastAPI, HTTPException

from app.config.settings import APP_NAME, APP_DESCRIPTION, APP_VERSION
from app.providers.exceptions import UnsupportedProviderError
from app.schemas.classification import ClassificationRequest, ClassificationResponse
from app.schemas.extraction import ExtractionRequest, ExtractionResponse
from app.schemas.generation import GenerationRequest, GenerationResponse
from app.schemas.summarization import SummarizationRequest, SummarizationResponse
from app.services.ai_service import generate_text
from app.services.classification_service import classify_text
from app.services.extraction_service import extract_information
from app.services.summarization_service import summarize_text


app = FastAPI(
    title=APP_NAME,
    description=APP_DESCRIPTION,
    version=APP_VERSION
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
    try:
        result = generate_text(request.prompt)
        return GenerationResponse(result=result)

    except UnsupportedProviderError as error:
        raise HTTPException(
            status_code=400,
            detail=str(error)
        )


@app.post("/summarize", response_model=SummarizationResponse)
def summarize(request: SummarizationRequest):
    result = summarize_text(request.text)

    return SummarizationResponse(summary=result)


@app.post("/classify", response_model=ClassificationResponse)
def classify(request: ClassificationRequest):
    result = classify_text(request.text)

    return ClassificationResponse(category=result)


@app.post("/extract", response_model=ExtractionResponse)
def extract(request: ExtractionRequest):
    result = extract_information(request.text)

    return ExtractionResponse(information=result)