from typing import List
from langchain.schema import Document
from langchain_community.document_loaders import (
    TextLoader,
    PyPDFLoader,
)
import os


def load_documents(path: str) -> List[Document]:
    """
    Load documents from a file or directory.
    Supports .txt and .pdf
    """
    documents: List[Document] = []

    if os.path.isdir(path):
        for file in os.listdir(path):
            full_path = os.path.join(path, file)
            documents.extend(_load_single_file(full_path))
    else:
        documents.extend(_load_single_file(path))

    return documents


def _load_single_file(path: str) -> List[Document]:
    if path.endswith(".txt"):
        loader = TextLoader(path, encoding="utf-8")
    elif path.endswith(".pdf"):
        loader = PyPDFLoader(path)
    else:
        return []

    return loader.load()
