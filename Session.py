from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


Base = declarative_base()    
engine = create_engine('postgresql://rsltgy:123456@localhost:5432/ubmk')
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()


class Session(Base):
    __tablename__ = 'sessions'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    session = Column(String(40))
    
    def __init__(self, session):
        self.session = session
  
def get_sessions():
    sessions = session.query(Session).order_by("id") if Session else None
    return sessions