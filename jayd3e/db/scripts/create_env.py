from sqlalchemy import Table
from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import Date
from sqlalchemy import DateTime
from sqlalchemy import MetaData
from sqlalchemy import create_engine
from jayd3e.db.config import DbConfig

class CreateEnv(object):
    def __init__(self):
        pass

    def create_db(self, config):
        create = config.engine + '://'  
        if config.user:
            create += config.user
        elif config.file:
            create += config.file

        if config.pw:
            create += ':' + config.pw 
        if config.host:
            create += '@' + config.host 
        if config.db:
            create += '/' + config.db 

        self.db = create_engine(create, pool_recycle=3600)

    def create_schema(self):
        metadata = MetaData(self.db)

        posts = Table('posts', metadata,
                      Column('id', Integer, primary_key=True),
                      Column('title', String(100)),
                      Column('body', String(2000)),
                      Column('date', Date),
                      Column('created', DateTime),
                      Column('change_time', DateTime),
                      mysql_engine='InnoDB',
                      mysql_charset='utf8'
        )
 
        posts.create()

if __name__ == '__main__':
    c = CreateEnv()
    c.create_db(DbConfig)
    c.create_schema()
