from fastapi import APIRouter, HTTPException
from app.models.schemas import AskRequest, AskResponse
from app.rag.chain import run_rag
from app.rag.chain import detect_intent_llm
from app.core.utils import is_greeting
from app.core.utils import is_invalid_input

router = APIRouter(prefix="/api", tags=["RAG"])

@router.post("/ask", response_model=AskResponse)
def ask_question(payload: AskRequest):
    if is_invalid_input(payload.question):
        return {
            "answer":"I didn’t understand that input.\n"
            "Please type a clear question or say hello to get started."
        }
    
    intent = detect_intent_llm(payload.question)
    print(intent)

    if intent == "invalid":
        return {
            "answer":
                "I didn’t understand that input.\n"
                "Please type a clear question or say hello to get started."
            
        }
        
    if intent == "how_are_you":
        return {
            "answer": (
                "I’m doing well, thank you for asking.\n"
                "How can I help you today?"
            )
        }

    if intent == "greeting":
        return {
            "answer": 
                "Hello! I’m your AI assistant.\n"
                "How can I help you today?"
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
