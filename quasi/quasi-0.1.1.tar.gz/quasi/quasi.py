import os
import requests
import requests_cache

from collections import MutableMapping
from requests_cache.backends import registry
from requests_cache.backends import BaseCache

from sanic import Sanic
from sanic import response


try:
    import cPickle as pickle
except ImportError:
    import pickle

debug = os.getenv("QUASI_DEBUG", True)
token = os.getenv("QUASI_TOKEN", None)
domain = os.getenv("QUASI_STUBBED_DOMAIN", "http://exampe.com/")
cache_folder = os.getenv("QUASI_STORE", "/tmp/quasi/store/")
header_overrides = {"Accept": "application/json"}


class FileStoreDict(MutableMapping):
    """ FileStoreDict - a dictionary like interface for a local file cache. """

    def __init__(self, namespace, collection_name="filestore_dict_data"):
        self.path = os.path.abspath(cache_folder) + os.sep
        if not os.path.exists(self.path):
            os.makedirs(self.path)

    def __getitem__(self, key):
        if not os.path.exists(self.path + key):
            print(f"Request not available fetching from source")
            raise KeyError

        with open(self.path + key, "rb") as fp:
            print(f"Fetch request from cache {self.path}{key}")
            return pickle.loads(fp.read())

    def __setitem__(self, key, item):
        print(f"store in cache {self.path} {key}")
        with open(self.path + key, "wb") as fp:
            fp.write(pickle.dumps(item))

    def __delitem__(self, key):
        os.unlink(self.path + key)

    def __len__(self):
        return len(os.listdir(self.path))

    def __iter__(self):
        for filename in os.listdir(self.path):
            with open(self.path + filename, "rb") as fp:
                yield pickle.loads(fp.read())

    def clear(self):
        for filename in os.listdir(self.path):
            os.unlink(self.path + filename)

    def __str__(self):
        return str(dict(self.items()))


class FileStoreCache(BaseCache):

    def __init__(self, namespace="requests-cache", **options):
        super(FileStoreCache, self).__init__(**options)
        self.responses = FileStoreDict(namespace, "responses")
        self.keys_map = FileStoreDict(namespace, "urls")


registry["filestore"] = FileStoreCache
# requests_cache.install_cache('website_cache', backend='sqlite')
requests_cache.install_cache("website_cache", backend="filestore")


app = Sanic()


def make_request(url, source_request):
    s = requests.Session()
    req = requests.Request(
        source_request.method, url, data=source_request.body
    )
    prepped = req.prepare()
    prepped.headers = source_request.headers
    if token:
        prepped.headers["Authorization"] = "Token " + token
    prepped.headers.update(header_overrides)
    del prepped.headers["host"]
    return s.send(prepped, stream=True)


@app.route("/<path:path>", methods=["GET", "POST"])
async def handle_requests(request, path):
    url = domain + path
    if request.query_string:
        url += "?" + request.query_string

    remote_response = make_request(url, request)

    return response.raw(
        remote_response.content,
        headers=remote_response.headers,
        status=remote_response.status_code,
    )


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=debug)
