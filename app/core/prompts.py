from langchain.prompts import ChatPromptTemplate

QA_PROMPT = ChatPromptTemplate.from_template(
    """
You are a helpful assistant.
Answer the question ONLY using the context below.
If the answer is not present in the context, say you do not know.

Context:
{context}

Question:
{question}
"""
)
