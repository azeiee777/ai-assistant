from langchain_community.vectorstores import FAISS


def get_retriever(vectorstore: FAISS, k: int = 4):
    """
    Create a retriever from a vector store.
    """
    return vectorstore.as_retriever(
        search_kwargs={"k": k}
    )
