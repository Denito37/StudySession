from pydantic import BaseModel

class Questions_request(BaseModel):
    question: str
    topic: str
    sub_topic:str

class Questions_reponse(BaseModel):
    id: int
    question: str
    topic: str
    sub_topic:str
