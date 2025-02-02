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

class Questions(Base):
    __tablename__= 'Questions'
    id = Column(Integer, primary_key=True, autoincrement=True)
    question = Column(String(200))
    answer = Column(String(1000))
    topic = Column(String(50), index=True)
    sub_topic = Column(String(50), index=True)

