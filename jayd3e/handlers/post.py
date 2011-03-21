from pyramid_handlers import action
from jayd3e.models.post import Post as PostModel
from jayd3e.handlers.handler import Handler
from pyramid.httpexceptions import HTTPFound

class Post(Handler):
    set = {}
    
    def __init__(self, request):
        self.request = request
        self.set['here'] = self.request.environ['PATH_INFO']
        self.request = request
        self.POST = self.request.str_POST

    @action(renderer='post/add.mako')
    def add(self):
        self.set['title'] = 'Post Add'
        if self.POST:
            new_post = PostModel(title=self.POST['title'], body=self.POST['body'])
            self.session.add(new_post)
            self.session.commit()
            return HTTPFound(location='/blog')
        return self.set
