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
    id = Column(String(36), primary_key=True, default=lambda: str(uuid4()))
    question = Column(String(200))
    answer = Column(String)
    topic = Column(String, index=True)

Base.metadata.create_all(engine)
