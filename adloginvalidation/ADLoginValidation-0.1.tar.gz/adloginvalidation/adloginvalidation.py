from flask import request, abort

import jwt, requests
from cryptography.x509 import load_pem_x509_certificate
from cryptography.hazmat.backends import default_backend

class ADLoginValidation(object):
    def __init__(self, app_id, authority_url='https://login.microsoftonline.com/common/.well-known/openid-configuration'):
        self.authority_url = authority_url
        self.app_id = app_id

    def _get_access_token(self, request):
        if 'Authorization' not in request.headers:
            return None
        if len(request.headers['Authorization']) < 7:
            return None
        return request.headers['Authorization'][7:]

    def _validate_request(self, request):
        access_token = self._get_access_token(request)
        token_header = jwt.get_unverified_header(access_token)
        res = requests.get(self.authority_url)
        jwk_uri = res.json()['jwks_uri']
        res = requests.get(jwk_uri)
        jwk_keys = res.json()

        # Iterate JWK keys and extract matching x5c chain
        x5c = None
        for key in jwk_keys['keys']:
            if key['kid'] == token_header['kid']:
                x5c = key['x5c']

        cert = ''.join(['-----BEGIN CERTIFICATE-----\n', x5c[0], '\n-----END CERTIFICATE-----\n',])
        public_key =  load_pem_x509_certificate(cert.encode(), default_backend()).public_key()
        try:
            jwt.decode(access_token, public_key, algorithms=token_header['alg'], audience=self.app_id,)
            return True
        except jwt.exceptions.InvalidTokenError as ex:
            print(ex)
            return False

    def validate_token_decorator(self, func):
        def func_wrapper(*args, **kws):
            if not self._validate_request(request):
                abort(403)
            else:
                return func(*args, **kws)
        return func_wrapper
