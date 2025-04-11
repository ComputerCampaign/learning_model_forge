import os
from dotenv import load_dotenv

load_dotenv()

CONFIG = {
    "base_url": os.getenv("OLLAMA_BASE_URL"),
    "llm_model": os.getenv("LLM_MODEL"),
    "embed_model": os.getenv("EMBEDDING_MODEL"),
    "chunk_size": 1000,
    "chunk_overlap": 200
}