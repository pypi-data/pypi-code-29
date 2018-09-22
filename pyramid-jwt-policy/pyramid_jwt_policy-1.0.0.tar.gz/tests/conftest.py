import pytest
from pyramid.config import Configurator
from pyramid.authorization import ACLAuthorizationPolicy
from pyramid.security import Authenticated
from pyramid.security import Allow
from webtest import TestApp as App

from pyramid_jwt_policy.policy import JWTAuthenticationPolicy


def login_view(request):
    return {'token': request.create_jwt_token(1)}


def secure_view(request):
    return 'OK'


class Root:
    __acl__ = [
        (Allow, Authenticated, ('read',)),
    ]

    def __init__(self, request):
        pass


@pytest.fixture
def get_token(request):
    def getter(request):
        return request.headers.get('X-Token')
    return getter


@pytest.fixture
def app(get_token):
    policy = JWTAuthenticationPolicy('secret', get_token)
    config = Configurator()
    config.set_authorization_policy(ACLAuthorizationPolicy())
    config.set_root_factory(Root)
    config.set_authentication_policy(policy)
    config.add_route('login', '/login')
    config.add_view(login_view, route_name='login', renderer='json')
    config.add_route('secure', '/secure')
    config.add_view(secure_view, route_name='secure', renderer='string',
         permission='read')
    config.add_request_method(policy.create_token, 'create_jwt_token')
    app = config.make_wsgi_app()
    return App(app)
