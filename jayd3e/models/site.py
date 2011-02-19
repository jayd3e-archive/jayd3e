from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

Engine = create_engine('mysql+mysqldb://jayd3e:sharp7&7@localhost/jayd3e_db', 
                       pool_recycle=3600)
Session = sessionmaker(bind=Engine)
Base = declarative_base()
class Site(object):
    __parent__ = None
    __name__ = None
    
    def __init__(self, request):
        pass