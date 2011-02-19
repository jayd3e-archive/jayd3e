from pyramid_handlers import action
from jayd3e.models.doc import Doc

class Doc(object):
    def __init__(self, request):
        self.request = request
    
    @action(renderer='doc/index.mako')
    def index(self):
        return {}
    
    @action(renderer='doc/stug.mako')
    def stug(self):
        return {}
    
    @action(renderer='doc/dd.mako')
    def dd(self):
        return {}