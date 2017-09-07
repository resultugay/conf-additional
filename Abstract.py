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
    session = Column(String(40))

    
    def __init__(self, abstract_id):
        self.abstract_id = abstract_id


       
def get_abstracts():
    abstracts = session.query(Abstract).order_by("id") if Abstract else None
    return abstracts

def get_abstracts2():
    abstracts = session.query(Abstract).filter(Abstract.color == '#00B050').order_by("topic") if Abstract else None
    return abstracts

def get_abstract_id():
    number = session.query(Abstract.abstract_id).order_by("id") if Abstract else None
    return number


def birinci_gun_13_1():
    abstracts = session.query(Abstract).filter(Abstract.color == '#00B050').filter(Abstract.session.like('1.gün 13:30 1.Salon%')).order_by("topic").all() if Abstract else None
    return abstracts

def birinci_gun_13_2():
    abstracts = session.query(Abstract).filter(Abstract.color == '#00B050').filter(Abstract.session.like('1.gün 13:30 2.Salon%')).order_by("topic").all() if Abstract else None
    return abstracts

def birinci_gun_13_3():
    abstracts = session.query(Abstract).filter(Abstract.color == '#00B050').filter(Abstract.session.like('1.gün 13:30 3.Salon%')).order_by("topic").all() if Abstract else None
    return abstracts

def birinci_gun_13_4():
    abstracts = session.query(Abstract).filter(Abstract.color == '#00B050').filter(Abstract.session.like('1.gün 13:30 4.Salon%')).order_by("topic").all() if Abstract else None
    return abstracts

def birinci_gun_13_5():
    abstracts = session.query(Abstract).filter(Abstract.color == '#00B050').filter(Abstract.session.like('1.gün 13:30 5.Salon%')).order_by("topic").all() if Abstract else None
    return abstracts

def birinci_gun_13_6():
    abstracts = session.query(Abstract).filter(Abstract.color == '#00B050').filter(Abstract.session.like('1.gün 13:30 6.Salon%')).order_by("topic").all() if Abstract else None
    return abstracts

def birinci_gun_13_7():
    abstracts = session.query(Abstract).filter(Abstract.color == '#00B050').filter(Abstract.session.like('1.gün 13:30 7.Salon%')).order_by("topic").all() if Abstract else None
    return abstracts

def birinci_gun_13_8():
    abstracts = session.query(Abstract).filter(Abstract.color == '#00B050').filter(Abstract.session.like('1.gün 13:30 8.Salon%')).order_by("topic").all() if Abstract else None
    return abstracts

    
    
    
    
def ikinci_gun_9_1():
    abstracts = session.query(Abstract).filter(Abstract.color == '#00B050').filter(Abstract.session.like('2.gün 09:00 1.Salon%')).order_by("topic").all() if Abstract else None
    return abstracts

def ikinci_gun_9_2():
    abstracts = session.query(Abstract).filter(Abstract.color == '#00B050').filter(Abstract.session.like('2.gün 09:00 2.Salon%')).order_by("topic").all() if Abstract else None
    return abstracts

def ikinci_gun_9_3():
    abstracts = session.query(Abstract).filter(Abstract.color == '#00B050').filter(Abstract.session.like('2.gün 09:00 3.Salon%')).order_by("topic").all() if Abstract else None
    return abstracts

def ikinci_gun_9_4():
    abstracts = session.query(Abstract).filter(Abstract.color == '#00B050').filter(Abstract.session.like('2.gün 09:00 4.Salon%')).order_by("topic").all() if Abstract else None
    return abstracts

def ikinci_gun_9_5():
    abstracts = session.query(Abstract).filter(Abstract.color == '#00B050').filter(Abstract.session.like('2.gün 09:00 5.Salon%')).order_by("topic").all() if Abstract else None
    return abstracts

def ikinci_gun_9_6():
    abstracts = session.query(Abstract).filter(Abstract.color == '#00B050').filter(Abstract.session.like('2.gün 09:00 6.Salon%')).order_by("topic").all() if Abstract else None
    return abstracts

def ikinci_gun_9_7():
    abstracts = session.query(Abstract).filter(Abstract.color == '#00B050').filter(Abstract.session.like('2.gün 09:00 7.Salon%')).order_by("topic").all() if Abstract else None
    return abstracts

def ikinci_gun_9_8():
    abstracts = session.query(Abstract).filter(Abstract.color == '#00B050').filter(Abstract.session.like('2.gün 09:00 8.Salon%')).order_by("topic").all() if Abstract else None
    return abstracts
    

def ikinci_gun_11_1():
    abstracts = session.query(Abstract).filter(Abstract.color == '#00B050').filter(Abstract.session.like('2.gün 11:00 1.Salon%')).order_by("topic").all() if Abstract else None
    return abstracts

def ikinci_gun_11_2():
    abstracts = session.query(Abstract).filter(Abstract.color == '#00B050').filter(Abstract.session.like('2.gün 11:00 2.Salon%')).order_by("topic").all() if Abstract else None
    return abstracts

def ikinci_gun_11_3():
    abstracts = session.query(Abstract).filter(Abstract.color == '#00B050').filter(Abstract.session.like('2.gün 11:00 3.Salon%')).order_by("topic").all() if Abstract else None
    return abstracts

def ikinci_gun_11_4():
    abstracts = session.query(Abstract).filter(Abstract.color == '#00B050').filter(Abstract.session.like('2.gün 11:00 4.Salon%')).order_by("topic").all() if Abstract else None
    return abstracts

def ikinci_gun_11_5():
    abstracts = session.query(Abstract).filter(Abstract.color == '#00B050').filter(Abstract.session.like('2.gün 11:00 5.Salon%')).order_by("topic").all() if Abstract else None
    return abstracts

def ikinci_gun_11_6():
    abstracts = session.query(Abstract).filter(Abstract.color == '#00B050').filter(Abstract.session.like('2.gün 11:00 6.Salon%')).order_by("topic").all() if Abstract else None
    return abstracts

def ikinci_gun_11_7():
    abstracts = session.query(Abstract).filter(Abstract.color == '#00B050').filter(Abstract.session.like('2.gün 11:00 7.Salon%')).order_by("topic").all() if Abstract else None
    return abstracts

def ikinci_gun_11_8():
    abstracts = session.query(Abstract).filter(Abstract.color == '#00B050').filter(Abstract.session.like('2.gün 11:00 8.Salon%')).order_by("topic").all() if Abstract else None
    return abstracts
    
    
def ikinci_gun_14_1():
    abstracts = session.query(Abstract).filter(Abstract.color == '#00B050').filter(Abstract.session.like('2.gün 14:00 1.Salon%')).order_by("topic").all() if Abstract else None
    return abstracts

def ikinci_gun_14_2():
    abstracts = session.query(Abstract).filter(Abstract.color == '#00B050').filter(Abstract.session.like('2.gün 14:00 2.Salon%')).order_by("topic").all() if Abstract else None
    return abstracts

def ikinci_gun_14_3():
    abstracts = session.query(Abstract).filter(Abstract.color == '#00B050').filter(Abstract.session.like('2.gün 14:00 3.Salon%')).order_by("topic").all() if Abstract else None
    return abstracts

def ikinci_gun_14_4():
    abstracts = session.query(Abstract).filter(Abstract.color == '#00B050').filter(Abstract.session.like('2.gün 14:00 4.Salon%')).order_by("topic").all() if Abstract else None
    return abstracts

def ikinci_gun_14_5():
    abstracts = session.query(Abstract).filter(Abstract.color == '#00B050').filter(Abstract.session.like('2.gün 14:00 5.Salon%')).order_by("topic").all() if Abstract else None
    return abstracts

def ikinci_gun_14_6():
    abstracts = session.query(Abstract).filter(Abstract.color == '#00B050').filter(Abstract.session.like('2.gün 14:00 6.Salon%')).order_by("topic").all() if Abstract else None
    return abstracts

def ikinci_gun_14_7():
    abstracts = session.query(Abstract).filter(Abstract.color == '#00B050').filter(Abstract.session.like('2.gün 14:00 7.Salon%')).order_by("topic").all() if Abstract else None
    return abstracts

def ikinci_gun_14_8():
    abstracts = session.query(Abstract).filter(Abstract.color == '#00B050').filter(Abstract.session.like('2.gün 14:00 8.Salon%')).order_by("topic").all() if Abstract else None
    return abstracts    
    
    