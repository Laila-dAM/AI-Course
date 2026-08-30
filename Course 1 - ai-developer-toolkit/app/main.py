from fastapi import FastAPI

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