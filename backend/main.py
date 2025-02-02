from fastapi import FastAPI, Depends, HTTPException
from pydantic import BaseModel
import uvicorn
from .utils.models import Questions, Session, Base, engine, get_db
from typing import List
from  sqlalchemy.sql.expression import func

app = FastAPI(openapi_prefix="/Question")
Base.metadata.create_all(engine)

class QuestionsBase(BaseModel):
    question: str
    answer:str
    topic: str
    sub_topic:str

class Questions_Input(QuestionsBase):
    pass

class Questions_Output(QuestionsBase):
    id: int


@app.post('/', response_model = Questions_Output)
async def post_questions(question : Questions_Input, db: Session=Depends(get_db)):
    db_item = Questions(**question.model_dump())
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item

@app.post('/all', response_model = List[Questions_Output])
async def post_questions(questions : List[Questions_Input], db: Session=Depends(get_db)):
    db_items=[]
    for question in questions:
        db_item = Questions(**question.model_dump())
        db.add(db_item)
        db.commit()
        db.refresh(db_item)
        db_items.append(db_item)
    return db_items

@app.get('/', response_model = List[Questions_Output])
async def get_questions(n:int = 10,offset:int=0,db: Session = Depends(get_db)):
    db_item = db.query(Questions).limit(n).offset(offset).all()
    return db_item

@app.get('/{topic}', response_model = List[Questions_Output])
async def get_topic_questions(topic:str, n:int = 5, db: Session = Depends(get_db)):
    db_item = db.query(Questions).filter(func.lower(Questions.topic) == func.lower(topic)).order_by(func.random()).limit(n).all()
    if not db_item:
        raise HTTPException(status_code= 404, detail='Topic not found')
    return db_item

@app.get('/{topic}/{sub_topic}', response_model = List[Questions_Output])
async def get_topic_questions(topic:str, sub_topic:str, n:int = 5, db: Session = Depends(get_db)):
    db_item = db.query(Questions).filter(func.lower(Questions.topic) == func.lower(topic) and func.lower(Questions.sub_topic) == func.lower(sub_topic)).order_by(func.random()).limit(n).all()
    if not db_item:
        raise HTTPException(status_code= 404, detail='Sub-topic not found')
    return db_item

@app.put('/{question_id}', response_model=Questions_Output)
async def update_question(question_id:int, question:Questions_Input, db: Session = Depends(get_db)):
    db_item = db.query(Questions).filter(Questions.id == question_id).first()
    if not db_item:
        raise HTTPException(status_code= 404, detail='question not found')
    updated_data = question.model_dump(exclude_unset=True)

    for key, value in updated_data.items():
        setattr(db_item,key,value)

    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item

@app.delete('/{question_id}', response_model = Questions_Output)
async def delete_question(question_id:int, db: Session = Depends(get_db)):
    db_item = db.query(Questions).filter(Questions.id == question_id).first()
    if not db_item:
        raise HTTPException(status_code= 404, detail='Topic question not found')
    db.delete(db_item)
    db.commit()
    return db_item

if __name__ == '__main__':
    uvicorn.run(app, host='127.0.0.1', port=8000)