from pydantic import BaseModel
from datetime import datetime
from typing import List
from uuid import uuid4


class UserBase(BaseModel):
    username: str
    email: str
    createdAt: datetime

class UserInput(UserBase):
    pass

class UserOutput(UserBase):
    id: uuid4

class QuestionsBase(BaseModel):
    question: str
    answer:str
    mediaURL: str
    topic: str
    sub_topic:str

class QuestionsInput(QuestionsBase):
    pass

class QuestionsOutput(QuestionsBase):
    id: uuid4

class ExamBase(BaseModel):
    topics: List[str]
    questionID: List[uuid4]
    submittedAt: datetime

class ExamOutput(ExamBase):
    id: uuid4

class ResultBase(BaseModel):
    userID: uuid4
    examID: uuid4
    correctQuestionID: List[uuid4]
    incorrectQuestionID:List[uuid4]

class ResultOutput(ResultBase):
    id: uuid4