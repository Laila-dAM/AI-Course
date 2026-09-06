import os

from dotenv import load_dotenv


load_dotenv()


APP_NAME = "AI Developer Toolkit"

APP_DESCRIPTION = "AI-powered developer toolkit"

APP_VERSION = "1.0.0"

AI_PROVIDER = os.getenv("AI_PROVIDER", "mock")