from pyramid_handlers import action
from pyramid.security import authenticated_userid
from jayd3e.models.doc import DocModel
from jayd3e.handlers.handler import Handler

class DocHandler(Handler):
    set = {}
    
    def __init__(self, request):
        self.request = request
        self.here = self.request.environ['PATH_INFO']
        self.logged_in = authenticated_userid(request)
    
    @action(renderer='doc/index.mako')
    def index(self):
        self.title = 'Design Documents'
        return {'here':self.here,
                'logged_in':self.logged_in,
                'title':self.title}
    
    @action(renderer='doc/stug.mako')
    def stug(self):
        self.title = 'Student Underground - Design Document'
        return {'here':self.here, 
                'logged_in':self.logged_in,
                'title':self.title}
    
    @action(renderer='doc/dd.mako')
    def dd(self):
        self.title = 'Design Documentor - Design Document'
        return {'here':self.here, 
                'logged_in':self.logged_in,
                'title':self.title}
