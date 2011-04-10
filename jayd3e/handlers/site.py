from pyramid_handlers import action
from pyramid.httpexceptions import HTTPFound

class SiteHandler(object):
    def __init__(self, request):
        pass

    @action()
    def index(self):
        return HTTPFound(location='/blog')
