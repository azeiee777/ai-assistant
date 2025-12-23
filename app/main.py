from fastapi import FastAPI
from app.core.config import settings
from app.core.logging import setup_logging
from app.api.deps import query_router

setup_logging()

app = FastAPI(
    title=settings.app_name,
    debug=settings.app_debug,
)

app.include_router(query_router)


@app.get("/health")
def health_check():
    return {"status": "ok", "env": settings.app_env}
