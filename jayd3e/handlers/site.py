from pyramid_handlers import action
from jayd3e.models.site import SiteModel
from jayd3e.handlers.handler import Handler

class SiteHandler(Handler):
    def __init__(self, request):
        self.request = request

    @action(renderer='site/index.mako')
    def index(self):
        return {}
