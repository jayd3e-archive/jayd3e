from pyramid.security import authenticated_userid
from pyramid.events import subscriber
from pyramid.events import BeforeRender


@subscriber(BeforeRender)
def add_globals(event):
    request = event['request']

    event['here'] = request.environ['PATH_INFO']
    event['logged_in'] = authenticated_userid(request)
