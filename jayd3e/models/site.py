from pyramid.security import Allow
from pyramid.security import Everyone

class SiteModel(object):
    __parent__ = None
    __name__ = None
    __acl__ = [ (Allow, Everyone, 'view'),
                (Allow, 'group:admins', 'edit') ]

    def __init__(self, request):
        pass
