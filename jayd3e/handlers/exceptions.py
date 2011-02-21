# Exceptions views.  Such as views that deal with server overload and
# NotFound pages.

def notFound(request):
    set = {}
    set['title'] = 'Page Not Found'
    return set