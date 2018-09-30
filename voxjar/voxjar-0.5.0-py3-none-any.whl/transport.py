import requests
from graphql.execution import ExecutionResult
from graphql.language.printer import print_ast


class HttpTransport(object):

    def __init__(self, url, token=None, timeout=None, headers={}):
        """
        Args:
            url (str): The GraphQL URL
            timeout (int, optional): Specifies a default timeout for requests
                                     (Default: None)
        """
        self.url = url
        self.default_timeout = timeout
        self.headers = headers
        self.inject_token(token)

    def inject_token(self, token):
        if token:
            self.headers['Authorization'] = 'Bearer {}'.format(token)

    def execute(self, document, variable_values=None, timeout=None, token=None):
        payload = {
            'query': print_ast(document),
            'variables': variable_values or {}
        }

        # TODO: check for file objects: hasattr(fp, 'read')

        self.inject_token(token)

        post_args = {
            'headers': self.headers,
            'timeout': timeout or self.default_timeout,
            'json': payload
        }

        request = requests.post(self.url, **post_args)
        request.raise_for_status()

        result = request.json()
        assert 'errors' in result or 'data' in result,\
               'Received non-compatible response "{}"'.format(result)
        return ExecutionResult(
            errors=result.get('errors'), data=result.get('data'))
