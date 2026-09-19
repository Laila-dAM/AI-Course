# AI Developer Toolkit

AI-powered developer toolkit built with Python and FastAPI.

## Features

- Text generation
- Text summarization
- Text classification
- Information extraction
- Input validation
- Mock AI provider
- Provider architecture
- Automated tests
- Docker support

## Tech Stack

- Python
- FastAPI
- Pydantic
- Pytest
- Docker
- Uvicorn

## Project Structure

```text
app/
├── config/
├── providers/
├── schemas/
├── services/
└── main.py

tests/
Running Locally

Create and activate a virtual environment:

python -m venv .venv

Install the dependencies:

pip install -r requirements.txt

Start the API:

uvicorn app.main:app --reload

The API will be available at:

http://127.0.0.1:8000

Interactive API documentation:

http://127.0.0.1:8000/docs
Running Tests
pytest
Docker

The project includes a Dockerfile and .dockerignore for containerized execution.

Docker execution is optional during development.