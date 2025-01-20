from pydantic import BaseModel
from typing import List
from uuid import uuid4, UUID

class QuestionsBase(BaseModel):
    #id: str
    question: str
    topic: str
    answer:str

class Questions_Input(QuestionsBase):
    pass

class Questions_Output(QuestionsBase):
    id: int

class Quiz_Output(BaseModel):
    id: int
    questions:List[Questions_Output]