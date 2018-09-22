# -*- coding: utf-8 -*-
from json.encoder import JSONEncoder
import uuid

from pyramid.security import forget, remember
from pyramid.testing import testConfig, DummyRequest, DummySecurityPolicy
from pyramid.interfaces import IAuthenticationPolicy
import pytest
from webob import Request
from zope.interface.verify import verifyObject

from pyramid_jwt_policy.policy import JWTAuthenticationPolicy
from pyramid_jwt_policy.exception import InvalidTokenGetter


def test_interface(get_token):
    verifyObject(IAuthenticationPolicy, JWTAuthenticationPolicy('secret', get_token))


def test_token_most_be_str(get_token):
    policy = JWTAuthenticationPolicy('secret', get_token)
    token = policy.create_token(15)
    assert isinstance(token, str)


def test_get_token_is_not_a_callable():
    with pytest.raises(InvalidTokenGetter):
        JWTAuthenticationPolicy('secret', 'not a callable')


def test_minimal_roundtrip(get_token):
    policy = JWTAuthenticationPolicy('secret', get_token)
    request = Request.blank('/')
    request.headers['X-Token'] = policy.create_token(15)
    policy.get_claims(request)
    assert policy.unauthenticated_userid(request) == 15


def test_audience_valid(get_token):
    policy = JWTAuthenticationPolicy('secret', get_token, audience='example.org')
    token = policy.create_token(15, name=u'Jöhn', admin=True, audience='example.org')
    request = Request.blank('/')
    request.headers['X-Token'] = token
    jwt_claims = policy.get_claims(request)
    assert jwt_claims['aud'] == 'example.org'


def test_audience_invalid(get_token):
    policy = JWTAuthenticationPolicy('secret', get_token, audience='example.org')
    token = policy.create_token(15, name=u'Jöhn', admin=True, audience='example.com')
    request = Request.blank('/')
    request.headers['X-Token'] = token
    jwt_claims = policy.get_claims(request)
    assert jwt_claims == {}


def test_algorithm_unsupported(get_token):
    with pytest.raises(NotImplementedError):
        JWTAuthenticationPolicy('secret', get_token, algorithm='SHA1')


def test_missing_pubkey(get_token):
    with pytest.raises(ValueError):
        JWTAuthenticationPolicy('secret', get_token, algorithm='RS256')


def test_extra_claims(get_token):
    policy = JWTAuthenticationPolicy('secret', get_token)
    token = policy.create_token(15, name=u'Jöhn', admin=True)
    request = Request.blank('/')
    request.headers['X-Token'] = token
    jwt_claims = policy.get_claims(request)
    assert jwt_claims['name'] == u'Jöhn'
    assert jwt_claims['admin']


def test_expired_token(get_token):
    policy = JWTAuthenticationPolicy('secret', get_token, expiration=-1)
    request = Request.blank('/')
    token = policy.create_token(15)
    request.headers['X-Token'] = token
    policy.get_claims(request)
    assert policy.unauthenticated_userid(request) is None
    policy.leeway = 5
    policy.get_claims(request)
    assert policy.unauthenticated_userid(request) == 15


def test_dynamic_expired_token(get_token):
    policy = JWTAuthenticationPolicy('secret', get_token, expiration=-1)
    request = Request.blank('/')
    request.headers['X-Token'] = policy.create_token(15, expiration=5)
    policy.get_claims(request)
    assert policy.unauthenticated_userid(request) == 15

    policy = JWTAuthenticationPolicy('secret', get_token)
    request.headers['X-Token'] = policy.create_token(15, expiration=-1)
    policy.get_claims(request)
    assert policy.unauthenticated_userid(request) is None
    request.headers['X-Token'] = policy.create_token(15)
    policy.get_claims(request)
    assert policy.unauthenticated_userid(request) == 15


def test_remember_warning(get_token):
    policy = JWTAuthenticationPolicy('secret', get_token)
    with testConfig() as config:
        config.set_authorization_policy(DummySecurityPolicy())
        config.set_authentication_policy(policy)
        request = DummyRequest()
        result = remember(request, 15)
    assert result == []


def test_forget_warning(get_token):
    policy = JWTAuthenticationPolicy('secret', get_token)
    with testConfig() as config:
        config.set_authorization_policy(DummySecurityPolicy())
        config.set_authentication_policy(policy)
        request = DummyRequest()
        result = forget(request)
    assert result == []


class MyCustomJsonEncoder(JSONEncoder):

    def default(self, o):
        if type(o) is uuid.UUID:
            return str(o)
        # Let the base class default method raise the TypeError
        return JSONEncoder.default(self, o)


def test_custom_json_encoder(get_token):
    policy = JWTAuthenticationPolicy('secret', get_token)
    principal_id = uuid.uuid4()
    claim_value = uuid.uuid4()
    with pytest.raises(TypeError):
        policy.create_token('subject', uuid_value=claim_value)
    policy = JWTAuthenticationPolicy('secret', get_token, json_encoder=MyCustomJsonEncoder)
    
    request = Request.blank('/')
    request.headers['X-Token'] = policy.create_token(principal_id, uuid_value=claim_value)
    jwt_claims = policy.get_claims(request)
    assert policy.unauthenticated_userid(request) == str(principal_id)
    assert jwt_claims['uuid_value'] == str(claim_value)
