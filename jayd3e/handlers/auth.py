from pyramid.httpexceptions import HTTPFound
from pyramid.security import remember
from pyramid.security import forget
from pyramid.url import route_url
from pyramid_handlers import action
from jayd3e.security import USERS

class AuthHandler(object):
    def __init__(self, request):
        self.request = request
        login_url = route_url('auth_action', request, action='login')
        referrer = request.url
        if referrer == login_url:
            referrer = '/'
        self.came_from = request.POST.get('referrer', referrer)
        self.here = request.environ['PATH_INFO']

    @action(renderer='auth/login.mako')
    def login(self):
        title = 'Login Page'
        message = ''
        username = ''
        password = ''

        if 'submit' in self.request.POST:
            username = self.request.POST['username']
            password = self.request.POST['password']
            if USERS.get(username) == password:
                self.headers = remember(self.request, username)
                return HTTPFound(location = self.came_from,
                                 headers = self.headers) 
            message = 'Failed login'

        return {'came_from':self.came_from,
                'title':title,
                'here':self.here,
                'url':self.request.application_url + '/auth/login',
                'username':username,
                'password':password,
                'message':message}

    @action()
    def logout(self):
        headers = forget(self.request)
        return HTTPFound(location = '/',
                         headers = headers)
