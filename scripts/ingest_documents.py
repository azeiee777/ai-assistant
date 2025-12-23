import sys
from pathlib import Path

from app.ingestion.ingest import ingest
from app.services.vectorstore import create_vectorstore


def main():
    if len(sys.argv) != 2:
        print("Usage: python ingest_documents.py <path_to_docs>")
        sys.exit(1)

    path = sys.argv[1]

    if not Path(path).exists():
        print(f"Path not found: {path}")
        sys.exit(1)

    print("Starting ingestion...")
    documents = ingest(path)

    print(f"Loaded and split into {len(documents)} chunks")

    create_vectorstore(documents)

    print("Vector store created successfully")


if __name__ == "__main__":
    main()
