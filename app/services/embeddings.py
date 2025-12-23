from langchain_openai import OpenAIEmbeddings
from app.core.config import settings


def get_embedding_model() -> OpenAIEmbeddings:
    """
    Factory method for embedding model.
    Centralized to avoid duplication and misconfiguration.
    """
    return OpenAIEmbeddings(
        model=settings.embedding_model,
        api_key=settings.openai_api_key,
    )
