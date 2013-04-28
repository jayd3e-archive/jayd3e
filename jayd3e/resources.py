from pyramid.security import Allow
from pyramid.security import Everyone


class Site(object):
    __acl__ = [
        (Allow, Everyone, 'view'),
        (Allow, 'group:admins', 'edit')
    ]

    def __init__(self, request):
        pass
