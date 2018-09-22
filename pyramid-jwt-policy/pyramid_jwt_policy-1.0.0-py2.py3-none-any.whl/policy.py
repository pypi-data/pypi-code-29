import datetime
import logging

import jwt
from jwt.api_jwt import _jwt_global_obj
from pyramid.authentication import CallbackAuthenticationPolicy
from pyramid.interfaces import IAuthenticationPolicy
from zope.interface import implementer

from .exception import InvalidTokenGetter


log = logging.getLogger('pyramid_jwt')


@implementer(IAuthenticationPolicy)
class JWTAuthenticationPolicy(CallbackAuthenticationPolicy):
    def __init__(self, private_key, get_token, public_key=None, algorithm='HS512',
                 leeway=0, expiration=None, audience=None,
                 default_claims=None, json_encoder=None, callback=None):
        if not callable(get_token):
            raise InvalidTokenGetter

        self.get_token = get_token
        self.callback = callback

        self.private_key = private_key
        self.public_key = public_key if public_key is not None else private_key

        self.leeway = leeway
        self.default_claims = default_claims if default_claims else {}
        self.audience = audience
        self.json_encoder = json_encoder
        if algorithm not in _jwt_global_obj.get_algorithms():
            raise NotImplementedError

        self.algorithm = algorithm

        if not self.algorithm.startswith('HS') and self.private_key == self.public_key:
            raise ValueError

        if expiration:
            expiration = datetime.timedelta(seconds=expiration)
        self.expiration = expiration

    def create_token(self, principal, expiration=None, audience=None, **claims):
        payload = self.default_claims.copy()
        payload.update(claims)
        payload['sub'] = principal
        payload['iat'] = iat = datetime.datetime.utcnow()

        expiration = expiration or self.expiration
        if expiration:
            if not isinstance(expiration, datetime.timedelta):
                expiration = datetime.timedelta(seconds=expiration)
            payload['exp'] = iat + expiration

        audience = audience or self.audience
        if audience:
            payload['aud'] = audience

        token = jwt.encode(payload,
                           self.private_key,
                           algorithm=self.algorithm,
                           json_encoder=self.json_encoder)
        if not isinstance(token, str): # pragma: no cover
            token = token.decode('ascii')
        return token

    def get_claims(self, request):
        token = self.get_token(request)
        if not token:
            return {}

        try:
            claims = jwt.decode(token, self.public_key, algorithms=[self.algorithm],
                                leeway=self.leeway, audience=self.audience)
            return claims
        except jwt.InvalidTokenError as e:
            log.warning('Invalid JWT token from %s: %s', request.remote_addr, e)
            return {}

    def unauthenticated_userid(self, request):
        return self.get_claims(request).get('sub')

    def remember(self, request, principal, **kw):
        return []

    def forget(self, request):
        return []
