import urllib.parse
import hashlib


class Signature:
    def __init__(self, client_id, client_secret):
        self.client_id = client_id
        self.client_secret = client_secret

    def get_params_with_signature(self, params={}):
        params["client_id"] = self.client_id
        params["sign"] = self.generate_signature(params)
        return params

    def generate_signature(self, params={}):
        if 'sign' in params:
            del params["sign"]

        sort_params = [(k, params[k]) for k in sorted(params.keys())]
        string = urllib.parse.unquote_plus(urllib.parse.urlencode(sort_params)) + "&client_secret=" + self.client_secret

        return hashlib.sha256(string.encode("utf-8")).hexdigest().upper()

    def verify_signature(self, params={}):
        client_sign = params["sign"]
        del params["sign"]

        server_sign = self.generate_signature(params, self.client_secret)

        return client_sign == server_sign
