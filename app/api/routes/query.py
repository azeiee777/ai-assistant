from fastapi import APIRouter, HTTPException
from app.models.schemas import AskRequest, AskResponse
from app.rag.chain import run_rag
from app.core.utils import is_greeting
from app.core.utils import is_invalid_input

router = APIRouter(prefix="/api", tags=["RAG"])

@router.post("/ask", response_model=AskResponse)
def ask_question(payload: AskRequest):
    # 1. Invalid input handling
    if is_invalid_input(payload.question):
        return {
            "answer":"I didn’t understand that input.\n"
            "Please type a clear question or say hello to get started."
        }
    
    if is_greeting(payload.question):
        return {
            "answer": "Hello! I’m your AI assistant. How can I help you today?"
        }

    answer, docs = run_rag(payload.question)

    return AskResponse(
        answer=answer,
        sources=[
            {
                "content": doc.page_content,
                "metadata": doc.metadata,
            }
            for doc in docs
        ],
    )
