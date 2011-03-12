from pyramid_handlers import action
from jayd3e.models.post import Post as PostModel
from jayd3e.handlers.handler import Handler
from datetime import date

class Blog(Handler):
    set = {}
    
    def __init__(self, request):
        self.request = request
        self.set['here'] = self.request.environ['PATH_INFO']

    @action(renderer='blog/index.mako')
    def index(self):
        self.set['title'] = 'Blog Index'
        self.set['posts'] = self.session.query(PostModel).all()
        
        for post in self.set['posts']:
            post.date = post.date.strftime('%B %d, %Y')
        
        return self.set

    @action(renderer='blog/hackeyes.mako')
    def hackeyes(self):
        return {}
