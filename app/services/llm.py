from langchain_openai import ChatOpenAI
from app.core.config import settings


def get_llm(temperature: float = 0.0) -> ChatOpenAI:
    """
    Factory method to return ChatOpenAI instance.
    Centralized to avoid scattered configuration.
    """
    return ChatOpenAI(
        model=settings.llm_model,
        api_key=settings.openai_api_key,
        temperature=temperature,
    )
