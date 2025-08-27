from fastapi import FastAPI
from pydantic import BaseModel
from src.llm_pipeline import ask_llm
from src.utils.logger import logger

app = FastAPI(title="LLM API")

class Query(BaseModel):
    prompt: str

@app.post("/ask")
def ask(query: Query):
    logger.info(f"Received prompt: {query.prompt}")
    answer = ask_llm(query.prompt)
    return {"answer": answer}
