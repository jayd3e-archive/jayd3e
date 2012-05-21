from pyramid.events import subscriber
from pyramid.events import BeforeRender
from jayd3e.models.post import PostModel
from jayd3e.models.model import Session

@subscriber(BeforeRender)
def add_globals(event):
    session = Session()
    posts = session.query(PostModel).order_by(PostModel.created).all()
    #Sort descending by created date
    posts.reverse()
    #Grab the five most recent posts
    posts = posts[0:10]
    session.close()

    event['recent_posts'] = posts
    