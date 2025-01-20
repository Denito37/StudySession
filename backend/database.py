from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import sessionmaker, relationship, Session
from sqlalchemy.ext.declarative import declarative_base
from uuid import uuid4

url = 'sqlite:///./QA.db'

engine = create_engine(url, echo=True)

sessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

class Questions(Base):
    __tablename__= 'Questions'
    #uuid = Column(String(36), primary_key=True, default=lambda: str(uuid4()))
    id = Column(Integer, primary_key=True, autoincrement=True)
    question = Column(String(200))
    answer = Column(String)
    topic = Column(String, index=True)

