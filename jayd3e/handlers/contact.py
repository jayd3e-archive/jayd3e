from pyramid_handlers import action
from pyramid.security import authenticated_userid

class ContactHandler(object):
    def __init__(self, request):
        self.request = request
        self.here = request.environ['PATH_INFO']
        self.logged_in = authenticated_userid(request)

    @action(renderer='contact/index.mako')
    def index(self):
        title = 'Contact Info'
        
        return {'here':self.here,
                'title':title,
                'logged_in':self.logged_in}
        