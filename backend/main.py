from fastapi import FastAPI, Depends, HTTPException
from pydantic import BaseModel
import uvicorn
from utils.models import sessionLocal, Questions, Session, Base, engine
from typing import List

app = FastAPI()
Base.metadata.create_all(engine)

def get_db():
    db = sessionLocal()
    try:
        yield db
    finally:
        db.close()

class QuestionsBase(BaseModel):
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

@app.post('/Questions', response_model= Questions_Output)
async def post_questions(question : Questions_Input, db: Session=Depends(get_db)):
    db_item = Questions(**question.model_dump())
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return question

@app.get('/Questions', response_model= List[Questions_Output])
async def get_questions(db: Session = Depends(get_db)):
    db_item = db.query(Questions).all()
    return db_item

@app.get('/Questions/{topic}', response_model=List[Questions_Output])
async def get_topic_questions(topic:str, db: Session = Depends(get_db)):
    db_item = db.query(Questions).filter(Questions.topic == topic).all()
    if not db_item:
        raise HTTPException(status_code= 404, detail='Topic not found')
    return db_item

if __name__ == '__main__':
    uvicorn.run(app, host='127.0.0.1', port=8000)