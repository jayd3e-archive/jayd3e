from pyramid.httpexceptions import HTTPFound
from pyramid.security import remember
from pyramid.security import forget
from pyramid.url import route_url
from pyramid_handlers import action
from jayd3e.security import USERS
from jayd3e.handlers.handler import Handler

class AuthHandler(Handler):
    username = ''
    password = ''
    message = ''

    def setup(self):
        self.POST = self.request.str_POST 
        login_url = route_url('auth_action', self.request, action='login')
        referrer = self.request.url
        if referrer == login_url:
            referrer = '/'
        self.came_from = self.request.POST.get('referrer', referrer)
        self.here = self.request.environ['PATH_INFO']


    @action(renderer='auth/login.mako')
    def login(self):
        self.title = 'Login Page'

        if 'submit' in self.POST:
            self.username = self.POST['username']
            self.password = self.POST['password']
            if USERS.get(self.username) == self.password:
                self.headers = remember(self.request, self.username)
                return HTTPFound(location = self.came_from,
                                 headers = self.headers) 
            self.message = 'Failed login'

        return {'came_from':self.came_from,
                'title':self.title,
                'here':self.here,
                'url':self.request.application_url + '/auth/login',
                'username':self.username,
                'password':self.password,
                'message':self.message}

    @action()
    def logout(self):
        headers = forget(self.request)
        return HTTPFound(location = '/',
                         headers = headers)
