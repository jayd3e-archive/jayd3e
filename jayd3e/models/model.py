from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from jayd3e.db.config import DbConfig

def base():
    return declarative_base()

def engine(config):        
    create = config.engine + '://' + config.user + ':' + config.pw + '@' + config.host + '/' + config.db
    return create_engine(create, pool_recycle=3600) 

def session():
    return sessionmaker(bind=Engine)

#Base Model Class
class Model(object):
    pass

Base = base()
Engine = engine(DbConfig)
Session = session()

