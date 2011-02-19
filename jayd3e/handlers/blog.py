from pyramid_handlers import action
from jayd3e.models.post import Post as PostModel
from jayd3e.models.site import Session

class Blog(object):
    def __init__(self, request):
        self.request = request
        self.session = Session()

    @action(renderer='blog/index.mako')
    def index(self):
        posts = self.session.query(PostModel).all()
        return {'posts':posts}

    @action(renderer='blog/hackeyes.mako')
    def hackeyes(self):
        return {}