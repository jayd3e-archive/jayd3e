# Exceptions views.  Such as views that deal with server overload and
# NotFound pages.
from pyramid.httpexceptions import HTTPFound

def notFound(request):
    title = 'Page Not Found'
    return set

def forbidden(request):
    return HTTPFound(location='/auth/login')
