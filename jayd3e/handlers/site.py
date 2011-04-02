from pyramid_handlers import action
from pyramid.httpexceptions import HTTPFound
from jayd3e.handlers.handler import Handler

class SiteHandler(Handler):
    def setup(self):
        pass

    @action()
    def index(self):
        return HTTPFound(location='/blog')
