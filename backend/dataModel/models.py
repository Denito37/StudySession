from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, DATETIME,UUID
from sqlalchemy.orm import sessionmaker, relationship, Session, declarative_base, mapped_column, Mapped
from typing import List

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
    id: Mapped[UUID] = mapped_column(primary_key=True)
    username = Column(String(50))
    email = Column(String(200), unique=True)
    createdAt = Column(DATETIME)
    results: Mapped[List['Results']] = relationship()

class Questions(Base):
    __tablename__= 'Questions'
    id: Mapped[UUID] = mapped_column(primary_key=True)
    question = Column(String(200))
    mediaURL = Column(String(300))
    answer = Column(String(1000))
    topic = Column(String(50), index=True)
    sub_topic = Column(String(50), index=True)
    exams: Mapped[List['Exams']] = relationship(back_populates='questions') 

class Exams(Base):
    __tablename__='Exams'
    id:Mapped[UUID] = mapped_column(primary_key=True)
    topics = Column(List[String(100)])
    questionsID: Mapped[UUID] = mapped_column(List[ForeignKey('Questions.id')])
    question: Mapped['Questions'] = relationship(back_populates='exams') 
    submittedAt = Column(DATETIME)
    results: Mapped[List['Results']] = relationship()

class Results(Base):
    __tablename__='Results'
    id: Mapped[UUID] = mapped_column(primary_key=True)
    userID: Mapped[UUID] = mapped_column(ForeignKey('Users.id'))
    examID: Mapped[UUID] = mapped_column(ForeignKey('Exams.id'))
    correctQuestionID: Mapped[UUID] = mapped_column(List[ForeignKey('Questions.id')])
    incorrectQuestionID: Mapped[UUID] = mapped_column(List[ForeignKey('Question.id')])