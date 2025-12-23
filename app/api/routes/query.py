from fastapi import APIRouter, HTTPException
from app.models.schemas import AskRequest, AskResponse
from app.rag.chain import run_rag

router = APIRouter(prefix="/api", tags=["RAG"])


@router.post("/ask", response_model=AskResponse)
def ask_question(payload: AskRequest):
    if not payload.question.strip():
        raise HTTPException(status_code=400, detail="Question cannot be empty")

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
