from pydantic import BaseModel
from typing import List, Optional, Dict


class AskRequest(BaseModel):
    question: str


class Source(BaseModel):
    content: str
    metadata: Dict


class AskResponse(BaseModel):
    answer: str
    sources: Optional[List[Source]] = []
