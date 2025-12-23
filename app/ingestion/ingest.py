from typing import List
from langchain.schema import Document

from app.ingestion.loaders import load_documents
from app.ingestion.splitter import split_documents


def ingest(path: str) -> List[Document]:
    """
    Full ingestion pipeline:
    load → split → return chunks
    """
    raw_docs = load_documents(path)

    if not raw_docs:
        raise ValueError("No supported documents found to ingest.")

    chunks = split_documents(raw_docs)
    return chunks
