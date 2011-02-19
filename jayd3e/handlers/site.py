from pyramid_handlers import action
from jayd3e.models.site import Site

class Site(object):
    def __init__(self, request):
        self.request = request

    @action(renderer='root/index.mako')
    def index(self):
        return {}