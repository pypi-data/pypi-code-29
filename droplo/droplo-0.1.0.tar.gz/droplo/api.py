"""
droplo.api
~~~~~~~~~~~~~~~~~

This module implements the Droplo content API Client,
allowing interaction with every method present in it.
"""

from .connection import get_json
from .resource import FolderResource, FileResource


class Api(object):
    """Constructs the API Client.

    :param access_token: API Access Token.

    Usage:

        >>> import droplo
        >>> api = droplo.Api('YOUR_ACCESS_TOKEN')
        <droplo.Api access_token="b4c0n73n7fu1">
    """

    def __init__(
        self,
        access_token,
        api_url='https://api.droplo.io',
        cache=None
    ):
        self.access_token = access_token
        self.api_url = api_url
        self.ttl = 10
        self.cache = cache

    def get(self, path='/'):
        """Fetches an api endpoint.

        :param path: (optional) The path of the endpoint.
        :return: :class:`Response <droplo.api.Response>` object.
        :rtype: droplo.api.Response

        Usage:
            >>> entries = api.get('blogposts')
            [<Entry[File] name='My First Blogpost' uuid="73f395ba-0478-4742-aeb7-f71a92f195ca">,
             <Entry[File] name='My Second Blogpost' uuid="7ced093f-436f-4935-89a4-9c86b84de3a3">]
        """

        return Response(get_json(
            self.build_url(path),
            self.access_token,
            cache=self.cache,
            ttl=self.ttl
        ))

    def build_url(self, path):
        endpoint = path[1:] if path.startswith('/') else path
        return '{0}/{1}'.format(self.api_url, endpoint)

    def __repr__(self):
        return '<droplo.api.Api access_token="{0}" api_url="{1}">'.format(self.access_token, self.api_url)


class Response(object):
    """
    Droplo's response to a query.
    :ivar list<droplo.resource.FolderResource> folders: the folders in the current path
    :ivar list<droplo.resource.FileResource> files: the files in the current path
    """

    def __init__(self, data):
        self.data = data
        self.folders = [FolderResource(d) for d in data.get("folders", [])]
        self.files = [FileResource(d) for d in data.get("files", [])]

    def __repr__(self):
        return '<droplo.api.Response>'
