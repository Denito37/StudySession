from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy.ext.declarative import declarative_base

url = 'sqlite:///./QA.db'

engine = create_engine(url)

sessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

class Questions(Base):
    __tablename__= 'Questions'
    id = Column(Integer, primary_key=True)
    question = Column(String(200))

Base.metadata.create_all(engine)
