from typing import List, Tuple
from langchain.schema import Document

from app.services.vectorstore import load_vectorstore
from app.services.llm import get_llm
from app.rag.retriever import get_retriever
from app.core.prompts import QA_PROMPT


def run_rag(question: str) -> Tuple[str, List[Document]]:
    """
    Run a single RAG query:
    retrieve → format → LLM → answer
    """
    vectorstore = load_vectorstore()
    retriever = get_retriever(vectorstore)

    docs = retriever.get_relevant_documents(question)

    context = "\n\n".join(doc.page_content for doc in docs)

    llm = get_llm()
    response = llm.invoke(
        QA_PROMPT.format(
            context=context,
            question=question,
        )
    )

    return response.content, docs
