from os import listdir
from os.path import isfile, join
from sqlalchemy.ext.declarative.api import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from Attachment import Attachment
import os

Base = declarative_base()    


engine = create_engine('postgresql://rsltgy:123456@localhost:5432/ubmk')
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()


mypath = "/home/basaran/Desktop/pdf"


onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]

for a in onlyfiles:
   data = open("/home/basaran/Desktop/pdf/" + a, "rb")
   data = data.read()
   session.query(Attachment).filter_by(abstracts_id = os.path.splitext(a)[0]).update({"filecontent": data})
   session.commit()
   print(os.path.splitext(a)[0])




