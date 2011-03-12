from pyramid.config import Configurator
from pyramid.exceptions import NotFound
from jayd3e.models.site import Site as SiteModel
from jayd3e.handlers.site import Site as SiteHandler
from jayd3e.handlers.blog import Blog as BlogHandler
from jayd3e.handlers.doc import Doc as DocHandler
from jayd3e.handlers.exceptions import notFound

def main(global_config, **settings):
    '''This function configures the application and returns a WSGI application'''

    settings = dict(settings)
    config = Configurator(settings=settings, root_factory=SiteModel)
    config.begin()
    config.add_static_view(name='static', path='jayd3e:static')

    #Handlers
    config.include('pyramid_handlers')
    #Handler Root Routes
    config.add_handler('site_root', '/', handler=SiteHandler, action='index')
    config.add_handler('blog_root', '/blog', handler=BlogHandler, action='index')
    config.add_handler('doc_root', '/doc', handler=DocHandler, action='index')

    #Handler Action Routes
    config.add_handler('site_action', '/{action}', handler=SiteHandler)
    config.add_handler('blog_action', '/blog/{action}', handler=BlogHandler)
    config.add_handler('doc_action', '/doc/{action}', handler=DocHandler)
    
    #Views
    config.add_view(notFound, context=NotFound, renderer='exceptions/not_found.mako')
    
    config.scan(__name__)
    config.end()
    return config.make_wsgi_app()

if __name__ == '__main__':
    from paste.httpserver import serve
    serve(make_app(), host="0.0.0.0", port="5432")
