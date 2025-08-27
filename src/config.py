from dotenv import load_dotenv
import os

load_dotenv()

LLM_MODEL = os.getenv("LLM_MODEL", "llama3")
QDRANT_HOST = os.getenv("QDRANT_HOST", "localhost")
QDRANT_PORT = int(os.getenv("QDRANT_PORT", 6333))
MLFLOW_TRACKING_URI = os.getenv("MLFLOW_TRACKING_URI", "http://localhost:5000")
