from pyramid.config import Configurator
from pyramid.exceptions import NotFound
from pyramid.exceptions import Forbidden
from pyramid.authentication import AuthTktAuthenticationPolicy
from pyramid.authorization import ACLAuthorizationPolicy
from jayd3e.security import groupfinder
from jayd3e.models.site import SiteModel
from jayd3e.handlers.site import SiteHandler
from jayd3e.handlers.blog import BlogHandler
from jayd3e.handlers.doc import DocHandler
from jayd3e.handlers.post import PostHandler
from jayd3e.handlers.auth import AuthHandler
from jayd3e.handlers.feed import FeedHandler
from jayd3e.handlers.archive import ArchiveHandler
from jayd3e.handlers.contact import ContactHandler
from jayd3e.exceptions import notFound
from jayd3e.exceptions import forbidden
from jayd3e.models.model import initializeDb
from jayd3e.models.model import engine
from jayd3e.db.config import DbConfig

def main(global_config, **settings):
    '''This function configures the application and returns a WSGI application'''
    initializeDb(engine(DbConfig))

    authn_policy = AuthTktAuthenticationPolicy('sosecret',
                                               callback=groupfinder)
    authz_policy = ACLAuthorizationPolicy()
    config = Configurator(settings=settings,
                          root_factory=SiteModel,
                          authentication_policy=authn_policy,
                          authorization_policy=authz_policy,
                          default_permission='view')

    config.add_static_view(name='static', path='jayd3e:static')

    #Handlers
    config.include('pyramid_handlers')
    #Handler Root Routes
    config.add_handler('site_root', '/', handler=SiteHandler, action='index')
    config.add_handler('blog_root', '/blog', handler=BlogHandler, action='index')
    config.add_handler('doc_root', '/doc', handler=DocHandler, action='index')
    config.add_handler('post_root', '/post', handler=PostHandler, action='index')
    config.add_handler('feed_root', '/feed', handler=FeedHandler, action='atom')
    config.add_handler('archive_root', '/archive', handler=ArchiveHandler, action='index')
    config.add_handler('contact_root', '/contact', handler=ContactHandler, action='index')

    #Handler Action Routes
    config.add_handler('site_action', '/{action}', handler=SiteHandler)
    config.add_handler('blog_action', '/blog/{action}', handler=BlogHandler)
    config.add_handler('doc_action', '/doc/{action}', handler=DocHandler)
    config.add_handler('post_action', '/post/{action}', handler=PostHandler)
    config.add_handler('post_action_id', '/post/{action}/{id}', handler=PostHandler)
    config.add_handler('auth_action', '/auth/{action}', handler=AuthHandler)
    config.add_handler('feed_action', '/feed/{action}', handler=FeedHandler)
    config.add_handler('archive_action', '/archive/{month}', handler=ArchiveHandler, action='month')

    #Exception Views
    config.add_view(notFound,
                    context=NotFound,
                    permission='__no_permission_required__',
                    renderer='exceptions/not_found.mako')
    config.add_view(forbidden,
                    context=Forbidden,
                    permission='__no_permission_required__')

    return config.make_wsgi_app()
