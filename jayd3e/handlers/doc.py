from pyramid_handlers import action
from jayd3e.models.doc import DocModel
from jayd3e.handlers.handler import Handler

class DocHandler(Handler):
    set = {}
    
    def __init__(self, request):
        self.request = request
        self.set['here'] = self.request.environ['PATH_INFO']
    
    @action(renderer='doc/index.mako')
    def index(self):
        self.set['title']='Design Documents'
        return self.set
    
    @action(renderer='doc/stug.mako')
    def stug(self):
        self.set['title']='Student Underground - Design Document'
        return self.set
    
    @action(renderer='doc/dd.mako')
    def dd(self):
        self.set['title']='Design Documentor - Design Document'
        return self.set
