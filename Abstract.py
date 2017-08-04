from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


Base = declarative_base()    
engine = create_engine('postgresql://rsltgy:123456@localhost:5432/ubmk')
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()


class Abstract(Base):
    __tablename__ = 'abstracts'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer)
    abstract_id = Column(Integer, primary_key=True)
    title = Column(String(40))
    text = Column(String(40))
    event  = Column(Integer)
    topic = Column(String(40))
    status = Column(String(40))
    author = Column(String(40))
    author_email = Column(String(40))
    author_affiliation = Column(String(40))
    presenter = Column(String(40))
    presenter_email = Column(String(40))
    presenter_preference = Column(String(40))
    keywords = Column(String(40))
    reviewer_id1 = Column(String(40))
    reviewer_id2 = Column(String(40))
    reviewer_id3 = Column(String(40))
    submit_by = Column(Integer)
    submit_date = Column(String(40))
    customized = Column(Integer)
    color = Column(String(40))
    
    def __init__(self, abstract_id):
        self.abstract_id = abstract_id


       
def get_abstracts():
    abstracts = session.query(Abstract).order_by("id") if Abstract else None
    return abstracts

def get_abstract_id():
    number = session.query(Abstract.abstract_id).order_by("id") if Abstract else None
    return number

