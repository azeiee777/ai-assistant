from typing import List
from langchain.schema import Document
from langchain_community.document_loaders import TextLoader, PyPDFLoader
import os
import logging

SUPPORTED_EXTENSIONS = (".txt", ".pdf")

logger = logging.getLogger(__name__)

def load_documents(path: str) -> List[Document]:
    """
    Recursively load supported documents from a file or directory.
    """
    documents: List[Document] = []

    if os.path.isfile(path):
        documents.extend(_load_single_file(path))
        return documents

    for root, _, files in os.walk(path):
        for file in files:
            if file.lower().endswith(SUPPORTED_EXTENSIONS):
                full_path = os.path.join(root, file)
                documents.extend(_load_single_file(full_path))

    return documents


def _load_single_file(path: str) -> List[Document]:
    try:
        # Skip empty files early
        if os.path.getsize(path) == 0:
            logger.warning(f"Skipping empty file: {path}")
            return []

        if path.lower().endswith(".txt"):
            loader = TextLoader(path, encoding="utf-8")
        elif path.lower().endswith(".pdf"):
            loader = PyPDFLoader(path)
        else:
            return []

        docs = loader.load()

        # Attach source metadata
        for doc in docs:
            doc.metadata["source"] = os.path.basename(path)

        return docs

    except Exception as e:
        # Log and skip problematic files
        logger.error(f"Failed to load file {path}: {e}")
        return []
