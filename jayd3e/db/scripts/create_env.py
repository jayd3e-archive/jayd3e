from sqlalchemy import Table, Column, Integer, String, Date, DateTime, MetaData, ForeignKey
from sqlalchemy import create_engine
from jayd3e.db.config import DbConfig

class CreateEnv(object):
    def __init__(self):
        self.create_db(Config)
        
    def create_db(self, config):
        create = config.engine + '://' + config.user + ':' + config.pw + '@' + config.host 
        self.db = create_engine(create, pool_recycle=3600)

    def create_schema(self):
        metadata = BoundMetaData(self.db)

        posts = Table('posts', metadata,
                      Column('id', Integer, primary_key=True),
                      Column('title', String(40)),
                      Column('body', String(2000)),
                      Column('date', Date),
                      Column('created', DateTime),
        )
        
        posts.create()
