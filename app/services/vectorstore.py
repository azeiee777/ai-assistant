import os
from typing import List

from langchain_community.vectorstores import FAISS
from langchain.schema import Document

from app.services.embeddings import get_embedding_model
from app.core.config import settings


def create_vectorstore(documents: List[Document]) -> FAISS:
    """
    Create and persist FAISS vector store from documents.
    Used during ingestion.
    """
    embeddings = get_embedding_model()

    vectorstore = FAISS.from_documents(
        documents=documents,
        embedding=embeddings,
    )

    os.makedirs(settings.vectorstore_path, exist_ok=True)
    vectorstore.save_local(settings.vectorstore_path)

    return vectorstore


def load_vectorstore() -> FAISS:
    """
    Load existing FAISS vector store.
    Used during query time.
    """
    if not os.path.exists(settings.vectorstore_path):
        raise RuntimeError(
            "Vector store not found. Run document ingestion first."
        )

    return FAISS.load_local(
        settings.vectorstore_path,
        get_embedding_model(),
        allow_dangerous_deserialization=True,
    )
