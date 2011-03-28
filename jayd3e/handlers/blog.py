from pyramid_handlers import action
from pyramid.security import authenticated_userid
from jayd3e.models.post import PostModel
from jayd3e.handlers.handler import Handler

class BlogHandler(Handler):
    set = {}

    def __init__(self, request):
        self.request = request
        self.here = self.request.environ['PATH_INFO']
        self.logged_in = authenticated_userid(request)

    @action(renderer='blog/index.mako')
    def index(self):
        self.title = 'Blog Index'
        self.posts = self.session.query(PostModel).all() 
        return {'here':self.here,
                'title':self.title,
                'logged_in':self.logged_in,
                'posts':self.posts}

    @action(renderer='blog/hackeyes.mako')
    def hackeyes(self):
        return {}
