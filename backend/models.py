from pydantic import BaseModel
from typing import List
from uuid import uuid4

class QuestionsBase(BaseModel):
    question: str
    topic: str
    sub_topic:str
    answer:str

class Questions_Input(QuestionsBase):
    pass

class Questions_Output(QuestionsBase):
    id: uuid4

class Quiz_Output(BaseModel):
    id: int
    questions:List[Questions_Output]