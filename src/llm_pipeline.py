from langchain_community.llms import Ollama
from src.config import LLM_MODEL
from src.utils.logger import logger

def get_llm():
    logger.info(f"Loading LLM model: {LLM_MODEL}")
    return Ollama(model=LLM_MODEL)

def ask_llm(prompt: str) -> str:
    llm = get_llm()
    return llm.invoke(prompt)
