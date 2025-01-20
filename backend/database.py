from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import sessionmaker, relationship, Session
from sqlalchemy.ext.declarative import declarative_base
from uuid import uuid4

url = 'sqlite:///./QA.db'

engine = create_engine(url)

sessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

class Questions(Base):
    __tablename__= 'Questions'
    id = Column(uuid4, primary_key=True)
    question = Column(String(200))
    answer = Column(String)
    topic = Column(String)

Base.metadata.create_all(engine)
