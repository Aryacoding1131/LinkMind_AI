from dotenv import load_dotenv
import os

load_dotenv()

OLLAMA_MODEL = os.getenv("OLLAMA_MODEL")
GROQ_API_KEY = os.getenv("GROQ_API_KEY")

MONGO_URI = os.getenv(
    "MONGO_URI"
)

DATABASE_NAME = os.getenv(
    "DATABASE_NAME"
)

