from fastapi import FastAPI, Depends, HTTPException
import uvicorn
from utils.models import Questions_Input
from utils.database import sessionLocal, Questions, Session, Base, engine
from typing import List

app = FastAPI()
Base.metadata.create_all(engine)

def get_db():
    db = sessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post('/Questions', response_model= Questions_Input)
async def post_questions(question : Questions_Input, db: Session=Depends(get_db)):
    db_item = Questions(**question.model_dump())
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return question

@app.get('/Questions', response_model= List[Questions_Input])
async def get_questions(db: Session = Depends(get_db)):
    db_item = db.query(Questions).all()
    return db_item

@app.get('/Questions/{topic}', response_model=List[Questions_Input])
async def get_topic_questions(topic:str, db: Session = Depends(get_db)):
    db_item = db.query(Questions).filter(Questions.topic == topic).all()
    if not db_item:
        raise HTTPException(status_code= 404, detail='Topic not found')
    return db_item

if __name__ == '__main__':
    uvicorn.run(app, host='127.0.0.1', port=8000)