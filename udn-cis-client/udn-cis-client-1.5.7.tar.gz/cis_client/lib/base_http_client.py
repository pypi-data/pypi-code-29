import json

from requests.exceptions import HTTPError

from cis_client import exception


class BaseClient(object):
    def get_auth_params(self, **kwargs):
        auth_params = {
            key: value
            for key, value in kwargs.items()
            if key in ('brand_id', 'account_id', 'group_id')
        }
        return auth_params


def with_auth(func):
    def decorator(*args, **kwargs):
        if 'token' not in kwargs:
            aaa_host = kwargs.get('aaa_host')
            username = kwargs.get('username')
            password = kwargs.get('password')
            insecure = kwargs.get('insecure', False)
            if not aaa_host or not username or not password:
                raise ValueError('Login requires following kwargs: "aaa_host", "username", "password".')
            from cis_client.lib.aaa import auth_client
            token = auth_client.get_token(aaa_host, username, password, insecure=insecure)
            kwargs['token'] = token
        if kwargs.get('context') is not None:
            kwargs['context']['token'] = kwargs['token']
        return func(*args, **kwargs)

    return decorator


def raise_for_http_response(response, message, **kwargs):
    try:
        response.raise_for_status()
    except HTTPError as e:
        reason = e.response.text
        try:
            jsonified_reason = json.loads(reason)
            reason = jsonified_reason['message']
        except Exception:
            pass
        reason += '. Request {}: "{}".'.format(e.response.request.method, e.response.url)
        raise exception.HttpClientError(response, message, reason, **kwargs)
