from fastapi import FastAPI, Depends
import uvicorn
from .models import Questions_Input
from .database import sessionLocal, Questions, Session
from typing import List

app = FastAPI()

def get_db():
    db = sessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get('/Questions', response_model= List[Questions_Input])
async def get_questions(db: Session = Depends(get_db)):
    db_item = db.query(Questions).all()
    return db_item

if __name__ == '__main__':
    uvicorn.run(app, host='127.0.0.1', port=8000)