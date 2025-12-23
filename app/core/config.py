from pydantic import BaseSettings


class Settings(BaseSettings):
    # App
    app_name: str = "rag_assistant"
    app_env: str = "development"
    app_debug: bool = True

    # OpenAI
    openai_api_key: str
    llm_model: str
    embedding_model: str

    # Vector store
    vectorstore_path: str

    class Config:
        env_file = ".env"
        case_sensitive = False


settings = Settings()
