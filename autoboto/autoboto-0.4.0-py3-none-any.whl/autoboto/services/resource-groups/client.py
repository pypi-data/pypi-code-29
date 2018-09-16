import datetime
import typing
import boto3
from autoboto import ClientBase, ShapeBase, OutputShapeBase
from . import shapes


class Client(ClientBase):
    def __init__(self, *args, **kwargs):
        super().__init__("resource-groups", *args, **kwargs)

    def create_group(
        self,
        _request: shapes.CreateGroupInput = None,
        *,
        name: str,
        resource_query: shapes.ResourceQuery,
        description: str = ShapeBase.NOT_SET,
        tags: typing.Dict[str, str] = ShapeBase.NOT_SET,
    ) -> shapes.CreateGroupOutput:
        """
        Creates a group with a specified name, description, and resource query.
        """
        if _request is None:
            _params = {}
            if name is not ShapeBase.NOT_SET:
                _params['name'] = name
            if resource_query is not ShapeBase.NOT_SET:
                _params['resource_query'] = resource_query
            if description is not ShapeBase.NOT_SET:
                _params['description'] = description
            if tags is not ShapeBase.NOT_SET:
                _params['tags'] = tags
            _request = shapes.CreateGroupInput(**_params)
        response = self._boto_client.create_group(**_request.to_boto())

        return shapes.CreateGroupOutput.from_boto(response)

    def delete_group(
        self,
        _request: shapes.DeleteGroupInput = None,
        *,
        group_name: str,
    ) -> shapes.DeleteGroupOutput:
        """
        Deletes a specified resource group. Deleting a resource group does not delete
        resources that are members of the group; it only deletes the group structure.
        """
        if _request is None:
            _params = {}
            if group_name is not ShapeBase.NOT_SET:
                _params['group_name'] = group_name
            _request = shapes.DeleteGroupInput(**_params)
        response = self._boto_client.delete_group(**_request.to_boto())

        return shapes.DeleteGroupOutput.from_boto(response)

    def get_group(
        self,
        _request: shapes.GetGroupInput = None,
        *,
        group_name: str,
    ) -> shapes.GetGroupOutput:
        """
        Returns information about a specified resource group.
        """
        if _request is None:
            _params = {}
            if group_name is not ShapeBase.NOT_SET:
                _params['group_name'] = group_name
            _request = shapes.GetGroupInput(**_params)
        response = self._boto_client.get_group(**_request.to_boto())

        return shapes.GetGroupOutput.from_boto(response)

    def get_group_query(
        self,
        _request: shapes.GetGroupQueryInput = None,
        *,
        group_name: str,
    ) -> shapes.GetGroupQueryOutput:
        """
        Returns the resource query associated with the specified resource group.
        """
        if _request is None:
            _params = {}
            if group_name is not ShapeBase.NOT_SET:
                _params['group_name'] = group_name
            _request = shapes.GetGroupQueryInput(**_params)
        response = self._boto_client.get_group_query(**_request.to_boto())

        return shapes.GetGroupQueryOutput.from_boto(response)

    def get_tags(
        self,
        _request: shapes.GetTagsInput = None,
        *,
        arn: str,
    ) -> shapes.GetTagsOutput:
        """
        Returns a list of tags that are associated with a resource, specified by an ARN.
        """
        if _request is None:
            _params = {}
            if arn is not ShapeBase.NOT_SET:
                _params['arn'] = arn
            _request = shapes.GetTagsInput(**_params)
        response = self._boto_client.get_tags(**_request.to_boto())

        return shapes.GetTagsOutput.from_boto(response)

    def list_group_resources(
        self,
        _request: shapes.ListGroupResourcesInput = None,
        *,
        group_name: str,
        filters: typing.List[shapes.ResourceFilter] = ShapeBase.NOT_SET,
        max_results: int = ShapeBase.NOT_SET,
        next_token: str = ShapeBase.NOT_SET,
    ) -> shapes.ListGroupResourcesOutput:
        """
        Returns a list of ARNs of resources that are members of a specified resource
        group.
        """
        if _request is None:
            _params = {}
            if group_name is not ShapeBase.NOT_SET:
                _params['group_name'] = group_name
            if filters is not ShapeBase.NOT_SET:
                _params['filters'] = filters
            if max_results is not ShapeBase.NOT_SET:
                _params['max_results'] = max_results
            if next_token is not ShapeBase.NOT_SET:
                _params['next_token'] = next_token
            _request = shapes.ListGroupResourcesInput(**_params)
        paginator = self.get_paginator("list_group_resources").paginate(
            **_request.to_boto()
        )
        page_generator = (page for page in paginator)
        first_page = next(page_generator)
        result = shapes.ListGroupResourcesOutput.from_boto(first_page)
        result._page_iterator = page_generator
        return result

        return shapes.ListGroupResourcesOutput.from_boto(response)

    def list_groups(
        self,
        _request: shapes.ListGroupsInput = None,
        *,
        max_results: int = ShapeBase.NOT_SET,
        next_token: str = ShapeBase.NOT_SET,
    ) -> shapes.ListGroupsOutput:
        """
        Returns a list of existing resource groups in your account.
        """
        if _request is None:
            _params = {}
            if max_results is not ShapeBase.NOT_SET:
                _params['max_results'] = max_results
            if next_token is not ShapeBase.NOT_SET:
                _params['next_token'] = next_token
            _request = shapes.ListGroupsInput(**_params)
        paginator = self.get_paginator("list_groups").paginate(
            **_request.to_boto()
        )
        page_generator = (page for page in paginator)
        first_page = next(page_generator)
        result = shapes.ListGroupsOutput.from_boto(first_page)
        result._page_iterator = page_generator
        return result

        return shapes.ListGroupsOutput.from_boto(response)

    def search_resources(
        self,
        _request: shapes.SearchResourcesInput = None,
        *,
        resource_query: shapes.ResourceQuery,
        max_results: int = ShapeBase.NOT_SET,
        next_token: str = ShapeBase.NOT_SET,
    ) -> shapes.SearchResourcesOutput:
        """
        Returns a list of AWS resource identifiers that matches a specified query. The
        query uses the same format as a resource query in a CreateGroup or
        UpdateGroupQuery operation.
        """
        if _request is None:
            _params = {}
            if resource_query is not ShapeBase.NOT_SET:
                _params['resource_query'] = resource_query
            if max_results is not ShapeBase.NOT_SET:
                _params['max_results'] = max_results
            if next_token is not ShapeBase.NOT_SET:
                _params['next_token'] = next_token
            _request = shapes.SearchResourcesInput(**_params)
        paginator = self.get_paginator("search_resources").paginate(
            **_request.to_boto()
        )
        page_generator = (page for page in paginator)
        first_page = next(page_generator)
        result = shapes.SearchResourcesOutput.from_boto(first_page)
        result._page_iterator = page_generator
        return result

        return shapes.SearchResourcesOutput.from_boto(response)

    def tag(
        self,
        _request: shapes.TagInput = None,
        *,
        arn: str,
        tags: typing.Dict[str, str],
    ) -> shapes.TagOutput:
        """
        Adds specified tags to a resource with the specified ARN. Existing tags on a
        resource are not changed if they are not specified in the request parameters.
        """
        if _request is None:
            _params = {}
            if arn is not ShapeBase.NOT_SET:
                _params['arn'] = arn
            if tags is not ShapeBase.NOT_SET:
                _params['tags'] = tags
            _request = shapes.TagInput(**_params)
        response = self._boto_client.tag(**_request.to_boto())

        return shapes.TagOutput.from_boto(response)

    def untag(
        self,
        _request: shapes.UntagInput = None,
        *,
        arn: str,
        keys: typing.List[str],
    ) -> shapes.UntagOutput:
        """
        Deletes specified tags from a specified resource.
        """
        if _request is None:
            _params = {}
            if arn is not ShapeBase.NOT_SET:
                _params['arn'] = arn
            if keys is not ShapeBase.NOT_SET:
                _params['keys'] = keys
            _request = shapes.UntagInput(**_params)
        response = self._boto_client.untag(**_request.to_boto())

        return shapes.UntagOutput.from_boto(response)

    def update_group(
        self,
        _request: shapes.UpdateGroupInput = None,
        *,
        group_name: str,
        description: str = ShapeBase.NOT_SET,
    ) -> shapes.UpdateGroupOutput:
        """
        Updates an existing group with a new or changed description. You cannot update
        the name of a resource group.
        """
        if _request is None:
            _params = {}
            if group_name is not ShapeBase.NOT_SET:
                _params['group_name'] = group_name
            if description is not ShapeBase.NOT_SET:
                _params['description'] = description
            _request = shapes.UpdateGroupInput(**_params)
        response = self._boto_client.update_group(**_request.to_boto())

        return shapes.UpdateGroupOutput.from_boto(response)

    def update_group_query(
        self,
        _request: shapes.UpdateGroupQueryInput = None,
        *,
        group_name: str,
        resource_query: shapes.ResourceQuery,
    ) -> shapes.UpdateGroupQueryOutput:
        """
        Updates the resource query of a group.
        """
        if _request is None:
            _params = {}
            if group_name is not ShapeBase.NOT_SET:
                _params['group_name'] = group_name
            if resource_query is not ShapeBase.NOT_SET:
                _params['resource_query'] = resource_query
            _request = shapes.UpdateGroupQueryInput(**_params)
        response = self._boto_client.update_group_query(**_request.to_boto())

        return shapes.UpdateGroupQueryOutput.from_boto(response)
