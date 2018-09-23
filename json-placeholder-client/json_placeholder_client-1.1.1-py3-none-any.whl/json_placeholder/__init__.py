from requests import request
from pathlib import Path


class Client:
    def __read_url(self):
        with (Path.cwd() / 'url.txt').open('r') as reader:
            return reader.readline()

    def __make_request(self, path):
        url = self.__read_url()
        res = request('GET', f'{url}/{path}')

        if (res.status_code >= 400 or 'json' not in res.headers.get('Content-Type','')) and self.__handle_errors:
            raise Exception

        return res.json()

    def __init__(self, handle_errors=True):
        self.__handle_errors = handle_errors

    def get_posts(self):
        return self.__make_request('posts')

    def get_comments(self):
        return self.__make_request('comments')
