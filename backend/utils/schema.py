from pydantic import BaseModel

class QuestionsBase(BaseModel):
    question: str
    answer:str
    topic: str
    sub_topic:str

class Questions_Input(QuestionsBase):
    pass

class Questions_Output(QuestionsBase):
    id: int