from pydantic import BaseModel

class UserBase(BaseModel):
    username: str
    email: str
    createdAt: str

class UserInput(UserBase):
    pass

class UserOutput(UserBase):
    id: int

class QuestionsBase(BaseModel):
    question: str
    answer:str
    mediaURL: str
    topic: str
    sub_topic:str

class QuestionsInput(QuestionsBase):
    pass

class QuestionsOutput(QuestionsBase):
    id: int

class ExamBase(BaseModel):
    topics: str
    questionID: list[int]
    submittedAt: str

class ExamOutput(ExamBase):
    id: int

class ResultBase(BaseModel):
    userID: int
    examID: int
    correctQuestionID: list[int]
    incorrectQuestionID:list[int]

class ResultOutput(ResultBase):
    id: int