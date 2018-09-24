import json
import requests


class ShutterstockAPI:
    def __init__(self, token):
        self.token = token

    @property
    def headers(self):
        return {
            'Content-Type': 'application/json',
            'Authorization': 'Bearer {token}'.format(
                token=self.token
            )
        }

    def request(self, method, endpoint, data_key='params', **params):
        endpoint, params = endpoint.prepare(**params)
        data = {
            data_key: params
        }

        response = method(
            'https://api.shutterstock.com/v2{endpoint}'.format(
                endpoint=endpoint
            ),
            headers=self.headers,
            **data
        )
        return json.loads(response.content.decode('utf-8'))

    def get(self, endpoint, **params):
        return self.request(requests.get, endpoint, **params)

    def post(self, endpoint, **params):
        return self.request(requests.post, endpoint, data_key='json', **params)

    def put(self, endpoint, **params):
        return self.request(requests.put, endpoint, data_key='json', **params)

    def delete(self, endpoint, **params):
        return self.request(requests.delete, endpoint, **params)
