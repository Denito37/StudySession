from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import sessionmaker, relationship, Session, declarative_base

url = 'sqlite:///./QA.db'

engine = create_engine(url, echo=True)

sessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

def get_db():
    db = sessionLocal()
    try:
        yield db
    finally:
        db.close()

class Users(Base):
    __tablename__='Users'
    id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String(50))
    email = Column(String(200), unique=True)
    createdAt = Column(String(20))

class Questions(Base):
    __tablename__= 'Questions'
    id = Column(Integer, primary_key=True, autoincrement=True)
    question = Column(String(200))
    answer = Column(String(1000))
    topic = Column(String(50), index=True)
    sub_topic = Column(String(50), index=True)

class Exams(Base):
    __tablename__='Exams'
    id = Column(Integer, primary_key=True, autoincrement=True)
    topics = Column(String(100))
    questionsID = Column(list[Integer])
    submittedAt = Column(String(20))

class Results(Base):
    __tablename__='Results'
    id = Column(Integer, primary_key=True, autoincrement=True)
    userID = Column(Integer)
    examID = Column(Integer)
    correctQuestionID = Column(list[Integer])
    incorrectQuestionID = Column(list[Integer])