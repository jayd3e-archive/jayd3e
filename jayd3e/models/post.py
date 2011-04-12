from jayd3e.models.model import Base, Model
from sqlalchemy import Column, Integer, String, Date, DateTime

class PostModel(Base, Model):
    __tablename__ = 'posts'
    
    id = Column(Integer, primary_key=True)
    title = Column(String(50))
    body = Column(String(2000))
    date = Column(Date)
    created = Column(DateTime)
    change_time = Column(DateTime)

    def __init__(self, **fields):
        self.__dict__.update(fields)

    def __repr__(self):
        return "<Post('%s', '%s', '%s', '%s', '%s')>" % (self.id, self.title, self.date, self.created, self.change_time)
