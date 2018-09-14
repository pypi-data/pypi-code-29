from flask import json


class RestApiTestMixin:

    def _query(self, path, method='get', data={}):
        request = getattr(self._client, method)(
            path, content_type='application/json', data=json.dumps(data))
        response = next(request.response)
        return json.loads(response)['response']

__all__ = ('RestApiTestMixin',)
