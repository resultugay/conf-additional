from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.sql import func

Base = declarative_base()    
engine = create_engine('postgresql://rsltgy:123456@localhost:5432/ubmk')
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()


class Decision(Base):
    __tablename__ = 'decisions'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    user_email = Column(String(40), nullable=False)
    abstract_id = Column(Integer)
    accept = Column(Integer)
    poster = Column(Integer)
    reject = Column(Integer)



    def __init__(self, user_email,abstract_id,accept,poster,reject):
        self.user_email = user_email
        self.abstract_id = abstract_id
        self.accept = accept
        self.poster = poster
        self.reject = reject


def get_accept_decisions(email):
    decisions = session.query(Decision.abstract_id).filter(Decision.user_email==email).\
                                                    filter(Decision.accept==1).order_by("id") if Decision else None
    return decisions

def get_poster_decisions(email):
    decisions = session.query(Decision.abstract_id).filter(Decision.user_email==email).\
                                                    filter(Decision.poster==1).order_by("id") if Decision else None
    return decisions

def get_reject_decisions(email):
    decisions = session.query(Decision.abstract_id).filter(Decision.user_email==email).\
                                                    filter(Decision.reject==1).order_by("id") if Decision else None
    return decisions



def get_all_accept_decisions():    
    all_accept = session.query(Decision.abstract_id,func.sum(Decision.accept).label('total')).group_by(Decision.abstract_id).order_by("abstract_id").all() if Decision else None
    return all_accept


def get_all_poster_decisions():    
    all_accept = session.query(Decision.abstract_id,func.sum(Decision.poster).label('total')).group_by(Decision.abstract_id).order_by("abstract_id").all() if Decision else None
    return all_accept

def get_all_reject_decisions():        
    all_accept = session.query(Decision.abstract_id,func.sum(Decision.reject).label('total')).group_by(Decision.abstract_id).order_by("abstract_id").all() if Decision else None
    return all_accept







