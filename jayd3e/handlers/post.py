from pyramid_handlers import action
from pyramid.security import authenticated_userid
from jayd3e.models.post import PostModel
from jayd3e.handlers.handler import Handler
from pyramid.httpexceptions import HTTPFound

class PostHandler(Handler):
    def __init__(self, request):
        self.request = request
        self.here = self.request.environ['PATH_INFO']
        self.POST = self.request.str_POST
        self.logged_in = authenticated_userid(request)

    @action(renderer='post/add.mako', permission='edit')
    def add(self):
        self.title = 'Post Add'
        if self.POST:
            new_post = PostModel(title=self.POST['title'], body=self.POST['body'])
            self.session.add(new_post)
            self.session.commit()
            return HTTPFound(location='/blog')
        return {'here':self.here,
                'logged_in':self.logged_in,
                'title':self.title}
