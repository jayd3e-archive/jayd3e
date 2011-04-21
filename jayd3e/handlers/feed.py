from pyramid_handlers import action
from jayd3e.models.post import PostModel
from jayd3e.models.model import Session
from sqlalchemy import func

class FeedHandler(object):
    def __init__(self, request):
        self.request = request

    @action(renderer="feed/atom.mako")
    def atom(self):
        session = Session()

        posts = session.query(PostModel).order_by(PostModel.created).all()
        posts.reverse()
        posts = posts[0:5]

        max_change_time = session.query(func.max(PostModel.change_time)).first()
        updated = max_change_time[0].strftime("%Y-%m-%dT%H:%M:%SZ")

        session.close()
        return {'posts':posts,
                'updated':updated}
