from requests import request


class Client:
    def __make_request(self, path):
        res = request('GET', f'https://jsonplaceholder.typicode.com/{path}')

        if (res.status_code >= 400 or 'json' in res.headers.get('Content-Type','')) and self.__handle_errors:
            raise Exception

        return res.json()

    def __init__(self, handle_errors=True):
        self.__handle_errors = handle_errors

    def get_posts(self):
        return self.__make_request('posts')

    def get_comments(self):
        return self.__make_request('comments')
