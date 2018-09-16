import datetime
import typing
import boto3
from autoboto import ClientBase, ShapeBase, OutputShapeBase
from . import shapes


class Client(ClientBase):
    def __init__(self, *args, **kwargs):
        super().__init__("resourcegroupstaggingapi", *args, **kwargs)

    def get_resources(
        self,
        _request: shapes.GetResourcesInput = None,
        *,
        pagination_token: str = ShapeBase.NOT_SET,
        tag_filters: typing.List[shapes.TagFilter] = ShapeBase.NOT_SET,
        resources_per_page: int = ShapeBase.NOT_SET,
        tags_per_page: int = ShapeBase.NOT_SET,
        resource_type_filters: typing.List[str] = ShapeBase.NOT_SET,
    ) -> shapes.GetResourcesOutput:
        """
        Returns all the tagged resources that are associated with the specified tags
        (keys and values) located in the specified region for the AWS account. The tags
        and the resource types that you specify in the request are known as _filters_.
        The response includes all tags that are associated with the requested resources.
        If no filter is provided, this action returns a paginated resource list with the
        associated tags.
        """
        if _request is None:
            _params = {}
            if pagination_token is not ShapeBase.NOT_SET:
                _params['pagination_token'] = pagination_token
            if tag_filters is not ShapeBase.NOT_SET:
                _params['tag_filters'] = tag_filters
            if resources_per_page is not ShapeBase.NOT_SET:
                _params['resources_per_page'] = resources_per_page
            if tags_per_page is not ShapeBase.NOT_SET:
                _params['tags_per_page'] = tags_per_page
            if resource_type_filters is not ShapeBase.NOT_SET:
                _params['resource_type_filters'] = resource_type_filters
            _request = shapes.GetResourcesInput(**_params)
        paginator = self.get_paginator("get_resources").paginate(
            **_request.to_boto()
        )
        page_generator = (page for page in paginator)
        first_page = next(page_generator)
        result = shapes.GetResourcesOutput.from_boto(first_page)
        result._page_iterator = page_generator
        return result

        return shapes.GetResourcesOutput.from_boto(response)

    def get_tag_keys(
        self,
        _request: shapes.GetTagKeysInput = None,
        *,
        pagination_token: str = ShapeBase.NOT_SET,
    ) -> shapes.GetTagKeysOutput:
        """
        Returns all tag keys in the specified region for the AWS account.
        """
        if _request is None:
            _params = {}
            if pagination_token is not ShapeBase.NOT_SET:
                _params['pagination_token'] = pagination_token
            _request = shapes.GetTagKeysInput(**_params)
        paginator = self.get_paginator("get_tag_keys").paginate(
            **_request.to_boto()
        )
        page_generator = (page for page in paginator)
        first_page = next(page_generator)
        result = shapes.GetTagKeysOutput.from_boto(first_page)
        result._page_iterator = page_generator
        return result

        return shapes.GetTagKeysOutput.from_boto(response)

    def get_tag_values(
        self,
        _request: shapes.GetTagValuesInput = None,
        *,
        key: str,
        pagination_token: str = ShapeBase.NOT_SET,
    ) -> shapes.GetTagValuesOutput:
        """
        Returns all tag values for the specified key in the specified region for the AWS
        account.
        """
        if _request is None:
            _params = {}
            if key is not ShapeBase.NOT_SET:
                _params['key'] = key
            if pagination_token is not ShapeBase.NOT_SET:
                _params['pagination_token'] = pagination_token
            _request = shapes.GetTagValuesInput(**_params)
        paginator = self.get_paginator("get_tag_values").paginate(
            **_request.to_boto()
        )
        page_generator = (page for page in paginator)
        first_page = next(page_generator)
        result = shapes.GetTagValuesOutput.from_boto(first_page)
        result._page_iterator = page_generator
        return result

        return shapes.GetTagValuesOutput.from_boto(response)

    def tag_resources(
        self,
        _request: shapes.TagResourcesInput = None,
        *,
        resource_arn_list: typing.List[str],
        tags: typing.Dict[str, str],
    ) -> shapes.TagResourcesOutput:
        """
        Applies one or more tags to the specified resources. Note the following:

          * Not all resources can have tags. For a list of resources that support tagging, see [Supported Resources](http://docs.aws.amazon.com/awsconsolehelpdocs/latest/gsg/supported-resources.html) in the _AWS Resource Groups and Tag Editor User Guide_.

          * Each resource can have up to 50 tags. For other limits, see [Tag Restrictions](http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/Using_Tags.html#tag-restrictions) in the _Amazon EC2 User Guide for Linux Instances_.

          * You can only tag resources that are located in the specified region for the AWS account.

          * To add tags to a resource, you need the necessary permissions for the service that the resource belongs to as well as permissions for adding tags. For more information, see [Obtaining Permissions for Tagging](http://docs.aws.amazon.com/awsconsolehelpdocs/latest/gsg/obtaining-permissions-for-tagging.html) in the _AWS Resource Groups and Tag Editor User Guide_.
        """
        if _request is None:
            _params = {}
            if resource_arn_list is not ShapeBase.NOT_SET:
                _params['resource_arn_list'] = resource_arn_list
            if tags is not ShapeBase.NOT_SET:
                _params['tags'] = tags
            _request = shapes.TagResourcesInput(**_params)
        response = self._boto_client.tag_resources(**_request.to_boto())

        return shapes.TagResourcesOutput.from_boto(response)

    def untag_resources(
        self,
        _request: shapes.UntagResourcesInput = None,
        *,
        resource_arn_list: typing.List[str],
        tag_keys: typing.List[str],
    ) -> shapes.UntagResourcesOutput:
        """
        Removes the specified tags from the specified resources. When you specify a tag
        key, the action removes both that key and its associated value. The operation
        succeeds even if you attempt to remove tags from a resource that were already
        removed. Note the following:

          * To remove tags from a resource, you need the necessary permissions for the service that the resource belongs to as well as permissions for removing tags. For more information, see [Obtaining Permissions for Tagging](http://docs.aws.amazon.com/awsconsolehelpdocs/latest/gsg/obtaining-permissions-for-tagging.html) in the _AWS Resource Groups and Tag Editor User Guide_.

          * You can only tag resources that are located in the specified region for the AWS account.
        """
        if _request is None:
            _params = {}
            if resource_arn_list is not ShapeBase.NOT_SET:
                _params['resource_arn_list'] = resource_arn_list
            if tag_keys is not ShapeBase.NOT_SET:
                _params['tag_keys'] = tag_keys
            _request = shapes.UntagResourcesInput(**_params)
        response = self._boto_client.untag_resources(**_request.to_boto())

        return shapes.UntagResourcesOutput.from_boto(response)
