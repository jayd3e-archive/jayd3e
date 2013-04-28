from pyramid.config import Configurator
from pyramid.exceptions import NotFound
from pyramid.exceptions import Forbidden
from pyramid.authentication import AuthTktAuthenticationPolicy
from pyramid.authorization import ACLAuthorizationPolicy
from jayd3e.security import groupfinder
from jayd3e.exceptions import notFound
from jayd3e.exceptions import forbidden
from jayd3e.resources import Site


def main(global_config, **settings):
    '''This function configures the application and returns a WSGI application'''
    authn_policy = AuthTktAuthenticationPolicy('sosecret',
                                               callback=groupfinder)
    authz_policy = ACLAuthorizationPolicy()
    config = Configurator(settings=settings,
                          root_factory=Site,
                          authentication_policy=authn_policy,
                          authorization_policy=authz_policy,
                          default_permission='view')

    config.add_static_view(name='static', path='jayd3e:static')

    # Routes
    config.add_route('index', '/')
    config.add_route('login', '/login')
    config.add_route('logout', '/logout')
    config.add_route('archive', '/archive')
    config.add_route('archive_month', '/archive/{year}/{month}')
    config.add_route('blog', '/blog')
    config.add_route('hackeyes', '/hackeyes')
    config.add_route('contact', '/contact')
    config.add_route('feed', '/feed')

    config.add_route('post', '/post')
    config.add_route('post_add', '/post/add')
    config.add_route('post_edit', '/post/edit')
    config.add_route('post_delete', '/post/delete')

    # Exceptions
    config.add_view(notFound,
                    context=NotFound,
                    permission='__no_permission_required__',
                    renderer='exceptions/not_found.mako')
    config.add_view(forbidden,
                    context=Forbidden,
                    permission='__no_permission_required__')

    config.scan('jayd3e')
    return config.make_wsgi_app()
