from fastapi import FastAPI, Depends
import uvicorn
import models
import database

app = FastAPI()

def get_db():
    db = database.sessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get('/Questions', response_model= models.Questions_Input)
async def get_questions(db: database.Session = Depends(get_db)):
    db_item = db.query(database.Questions).all()
    return db_item

if __name__ == '__main__':
    uvicorn.run(app, host='127.0.0.1', port=8000)