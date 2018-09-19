"""
droplo.resource
~~~~~~~~~~~~~~~~~~~
This module implements the Resource, FolderResource and FileResource classes.
"""


class Resource(object):
    """
    Base Resource Class
    Implements common resource attributes.
    """
    def __init__(self, data):
        self.raw = data
        self.name = data.get('name')
        self.created = data.get('created')
        self.modified = data.get('modified')


class FolderResource(Resource):
    """Folder Resource Class
    """
    def __init__(self, data):
        super(FolderResource, self).__init__(data)
        self.endpoint = data.get('endpoint')


class FileResource(Resource):
    """File Resource Class
    """
    def __init__(self, data):
        super(FileResource, self).__init__(data)
        self.type = data.get('type')
        self.url = data.get('url')
