from sqlalchemy import Table
from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import Date
from sqlalchemy import DateTime
from sqlalchemy import MetaData
from sqlalchemy import ForeignKey
from sqlalchemy import create_engine
from jayd3e.db.config import DbConfig
from datetime import date
from datetime import datetime

class CreateEnv(object):
    def __init__(self):
        pass

    def create_db(self, config):
        create = config.engine + '://' + config.user + ':' + config.pw + '@' + config.host + '/' + config.db 
        self.db = create_engine(create, pool_recycle=3600)

    def create_schema(self):
        metadata = MetaData(self.db)

        posts = Table('posts', metadata,
                      Column('id', Integer, primary_key=True),
                      Column('title', String(40)),
                      Column('body', String(2000)),
                      Column('date', Date),
                      Column('created', DateTime),
                      Column('change_time', DateTime),
                      mysql_engine='InnoDB',
                      mysql_charset='utf8'
        )
        
        posts.create()

c = CreateEnv()
c.create_db(DbConfig)
c.create_schema()
