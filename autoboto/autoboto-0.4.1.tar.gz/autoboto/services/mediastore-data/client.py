import datetime
import typing
import boto3
from autoboto import ClientBase, ShapeBase, OutputShapeBase
from . import shapes


class Client(ClientBase):
    def __init__(self, *args, **kwargs):
        super().__init__("mediastore-data", *args, **kwargs)

    def delete_object(
        self,
        _request: shapes.DeleteObjectRequest = None,
        *,
        path: str,
    ) -> shapes.DeleteObjectResponse:
        """
        Deletes an object at the specified path.
        """
        if _request is None:
            _params = {}
            if path is not ShapeBase.NOT_SET:
                _params['path'] = path
            _request = shapes.DeleteObjectRequest(**_params)
        response = self._boto_client.delete_object(**_request.to_boto())

        return shapes.DeleteObjectResponse.from_boto(response)

    def describe_object(
        self,
        _request: shapes.DescribeObjectRequest = None,
        *,
        path: str,
    ) -> shapes.DescribeObjectResponse:
        """
        Gets the headers for an object at the specified path.
        """
        if _request is None:
            _params = {}
            if path is not ShapeBase.NOT_SET:
                _params['path'] = path
            _request = shapes.DescribeObjectRequest(**_params)
        response = self._boto_client.describe_object(**_request.to_boto())

        return shapes.DescribeObjectResponse.from_boto(response)

    def get_object(
        self,
        _request: shapes.GetObjectRequest = None,
        *,
        path: str,
        range: str = ShapeBase.NOT_SET,
    ) -> shapes.GetObjectResponse:
        """
        Downloads the object at the specified path.
        """
        if _request is None:
            _params = {}
            if path is not ShapeBase.NOT_SET:
                _params['path'] = path
            if range is not ShapeBase.NOT_SET:
                _params['range'] = range
            _request = shapes.GetObjectRequest(**_params)
        response = self._boto_client.get_object(**_request.to_boto())

        return shapes.GetObjectResponse.from_boto(response)

    def list_items(
        self,
        _request: shapes.ListItemsRequest = None,
        *,
        path: str = ShapeBase.NOT_SET,
        max_results: int = ShapeBase.NOT_SET,
        next_token: str = ShapeBase.NOT_SET,
    ) -> shapes.ListItemsResponse:
        """
        Provides a list of metadata entries about folders and objects in the specified
        folder.
        """
        if _request is None:
            _params = {}
            if path is not ShapeBase.NOT_SET:
                _params['path'] = path
            if max_results is not ShapeBase.NOT_SET:
                _params['max_results'] = max_results
            if next_token is not ShapeBase.NOT_SET:
                _params['next_token'] = next_token
            _request = shapes.ListItemsRequest(**_params)
        response = self._boto_client.list_items(**_request.to_boto())

        return shapes.ListItemsResponse.from_boto(response)

    def put_object(
        self,
        _request: shapes.PutObjectRequest = None,
        *,
        body: typing.Any,
        path: str,
        content_type: str = ShapeBase.NOT_SET,
        cache_control: str = ShapeBase.NOT_SET,
        storage_class: typing.Union[str, shapes.StorageClass] = ShapeBase.
        NOT_SET,
    ) -> shapes.PutObjectResponse:
        """
        Uploads an object to the specified path. Object sizes are limited to 10 MB.
        """
        if _request is None:
            _params = {}
            if body is not ShapeBase.NOT_SET:
                _params['body'] = body
            if path is not ShapeBase.NOT_SET:
                _params['path'] = path
            if content_type is not ShapeBase.NOT_SET:
                _params['content_type'] = content_type
            if cache_control is not ShapeBase.NOT_SET:
                _params['cache_control'] = cache_control
            if storage_class is not ShapeBase.NOT_SET:
                _params['storage_class'] = storage_class
            _request = shapes.PutObjectRequest(**_params)
        response = self._boto_client.put_object(**_request.to_boto())

        return shapes.PutObjectResponse.from_boto(response)
