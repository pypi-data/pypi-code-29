import boto3
from botocore.paginate import Paginator


class ClientBase:
    """
    Base class for all clients
    """

    def __init__(self, service_name, *args, **kwargs):
        self._service_name = service_name
        self._boto_client = boto3.client(service_name, *args, **kwargs)
        self._boto_paginators = {}

    def get_paginator(self, operation_name: str) -> Paginator:
        if operation_name not in self._boto_paginators:
            self._boto_paginators[operation_name] = self._boto_client.get_paginator(operation_name)
        return self._boto_paginators[operation_name]

    def __getattr__(self, name):
        if hasattr(self._boto_client, name):
            return getattr(self._boto_client, name)
        raise AttributeError(name)
