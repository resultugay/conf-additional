from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.dialects.postgresql import BYTEA

Base = declarative_base()    
engine = create_engine('postgresql://rsltgy:123456@localhost:5432/ubmk')
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()


class Attachment(Base):
    __tablename__ = 'attachments'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    attachment_id = Column(Integer)
    abstracts_id = Column(Integer)
    filecontent  = Column(BYTEA)
    filename = Column(String(40))
    filetype = Column(String(40))
    filesize  = Column(Integer)
    
    
    def __init__(self, attachment_id,abstracts_id,filecontent,filename,filetype,filesize):
        self.attachment_id = attachment_id
        self.abstracts_id = abstracts_id
        self.filecontent = filecontent
        self.filename = filename
        self.filetype = filetype
        self.filesize = filesize
        print("init ok");

       
def get_attachment(abstract_id):
    attachment = session.query(Attachment).filter(Attachment.abstracts_id==abstract_id).first() if Attachment else None
    return attachment

