from sqlalchemy import (
    Column,
    String,
    Integer,
    Date,
    DateTime
)
from sqlalchemy.ext.declarative import declarative_base


class BaseClass(object):
    id = Column(Integer, primary_key=True)


Base = declarative_base(cls=BaseClass)


def initializeDb(engine):
    Base.metadata.bind = engine


class Post(Base):
    __tablename__ = 'posts'

    title = Column(String(50))
    body = Column(String(2000))
    date = Column(Date)
    created = Column(DateTime)
    change_time = Column(DateTime)

    def __repr__(self):
        return "<Post('%s')>" % (self.id)
