from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine

def base():
    return declarative_base()

def session():
    return sessionmaker()

def engine(config):        
    create = config.engine + '://' + config.user + ':' + config.pw + '@' + config.host + '/' + config.db
    return create_engine(create, pool_recycle=3600) 

Base = base()
Session = session()

def initializeDb(engine):
    Session.configure(bind=engine)
    Base.metadata.bind = engine
    Base.metadata.create_all(engine)

#Base Model Class
class Model(object):
    pass
