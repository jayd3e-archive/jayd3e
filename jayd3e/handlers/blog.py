from pyramid_handlers import action
from pyramid.security import authenticated_userid
from jayd3e.models.post import PostModel
from jayd3e.models.model import Session

class BlogHandler(object):
    def __init__(self, request):
        self.request = request
        self.here = request.environ['PATH_INFO']
        self.logged_in = authenticated_userid(request)

    @action(renderer='blog/index.mako')
    def index(self):
        title = 'Blog Index'
        session = Session()
        posts = session.query(PostModel).order_by(PostModel.created).all()
        posts.reverse()
        session.close()
        return {'here':self.here,
                'title':title,
                'logged_in':self.logged_in,
                'posts':posts}

    @action(renderer='blog/hackeyes.mako')
    def hackeyes(self):
        return {}
