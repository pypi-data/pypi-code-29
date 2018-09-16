import datetime
import typing
from autoboto import ShapeBase, OutputShapeBase, TypeInfo
import dataclasses


@dataclasses.dataclass
class BadRequestException(ShapeBase):
    """
    The request does not comply with validation rules that are defined for the
    request parameters.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "message",
                "Message",
                TypeInfo(str),
            ),
        ]

    message: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class CreateGroupInput(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "name",
                "Name",
                TypeInfo(str),
            ),
            (
                "resource_query",
                "ResourceQuery",
                TypeInfo(ResourceQuery),
            ),
            (
                "description",
                "Description",
                TypeInfo(str),
            ),
            (
                "tags",
                "Tags",
                TypeInfo(typing.Dict[str, str]),
            ),
        ]

    # The name of the group, which is the identifier of the group in other
    # operations. A resource group name cannot be updated after it is created. A
    # resource group name can have a maximum of 128 characters, including
    # letters, numbers, hyphens, dots, and underscores. The name cannot start
    # with `AWS` or `aws`; these are reserved. A resource group name must be
    # unique within your account.
    name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The resource query that determines which AWS resources are members of this
    # group.
    resource_query: "ResourceQuery" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The description of the resource group. Descriptions can have a maximum of
    # 511 characters, including letters, numbers, hyphens, underscores,
    # punctuation, and spaces.
    description: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The tags to add to the group. A tag is a string-to-string map of key-value
    # pairs. Tag keys can have a maximum character length of 128 characters, and
    # tag values can have a maximum length of 256 characters.
    tags: typing.Dict[str, str] = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class CreateGroupOutput(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "group",
                "Group",
                TypeInfo(Group),
            ),
            (
                "resource_query",
                "ResourceQuery",
                TypeInfo(ResourceQuery),
            ),
            (
                "tags",
                "Tags",
                TypeInfo(typing.Dict[str, str]),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A full description of the resource group after it is created.
    group: "Group" = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The resource query associated with the group.
    resource_query: "ResourceQuery" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The tags associated with the group.
    tags: typing.Dict[str, str] = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DeleteGroupInput(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "group_name",
                "GroupName",
                TypeInfo(str),
            ),
        ]

    # The name of the resource group to delete.
    group_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DeleteGroupOutput(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "group",
                "Group",
                TypeInfo(Group),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A full description of the deleted resource group.
    group: "Group" = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ForbiddenException(ShapeBase):
    """
    The caller is not authorized to make the request.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "message",
                "Message",
                TypeInfo(str),
            ),
        ]

    message: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class GetGroupInput(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "group_name",
                "GroupName",
                TypeInfo(str),
            ),
        ]

    # The name of the resource group.
    group_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class GetGroupOutput(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "group",
                "Group",
                TypeInfo(Group),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A full description of the resource group.
    group: "Group" = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class GetGroupQueryInput(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "group_name",
                "GroupName",
                TypeInfo(str),
            ),
        ]

    # The name of the resource group.
    group_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class GetGroupQueryOutput(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "group_query",
                "GroupQuery",
                TypeInfo(GroupQuery),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The resource query associated with the specified group.
    group_query: "GroupQuery" = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class GetTagsInput(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "arn",
                "Arn",
                TypeInfo(str),
            ),
        ]

    # The ARN of the resource for which you want a list of tags. The resource
    # must exist within the account you are using.
    arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class GetTagsOutput(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "arn",
                "Arn",
                TypeInfo(str),
            ),
            (
                "tags",
                "Tags",
                TypeInfo(typing.Dict[str, str]),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The ARN of the tagged resource.
    arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The tags associated with the specified resource.
    tags: typing.Dict[str, str] = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class Group(ShapeBase):
    """
    A resource group.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "group_arn",
                "GroupArn",
                TypeInfo(str),
            ),
            (
                "name",
                "Name",
                TypeInfo(str),
            ),
            (
                "description",
                "Description",
                TypeInfo(str),
            ),
        ]

    # The ARN of a resource group.
    group_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The name of a resource group.
    name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The description of the resource group.
    description: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class GroupQuery(ShapeBase):
    """
    The underlying resource query of a resource group. Resources that match query
    results are part of the group.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "group_name",
                "GroupName",
                TypeInfo(str),
            ),
            (
                "resource_query",
                "ResourceQuery",
                TypeInfo(ResourceQuery),
            ),
        ]

    # The name of a resource group that is associated with a specific resource
    # query.
    group_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The resource query which determines which AWS resources are members of the
    # associated resource group.
    resource_query: "ResourceQuery" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class InternalServerErrorException(ShapeBase):
    """
    An internal error occurred while processing the request.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "message",
                "Message",
                TypeInfo(str),
            ),
        ]

    message: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ListGroupResourcesInput(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "group_name",
                "GroupName",
                TypeInfo(str),
            ),
            (
                "filters",
                "Filters",
                TypeInfo(typing.List[ResourceFilter]),
            ),
            (
                "max_results",
                "MaxResults",
                TypeInfo(int),
            ),
            (
                "next_token",
                "NextToken",
                TypeInfo(str),
            ),
        ]

    # The name of the resource group.
    group_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Filters, formatted as ResourceFilter objects, that you want to apply to a
    # ListGroupResources operation.

    #   * `resource-type` \- Filter resources by their type. Specify up to five resource types in the format AWS::ServiceCode::ResourceType. For example, AWS::EC2::Instance, or AWS::S3::Bucket.
    filters: typing.List["ResourceFilter"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The maximum number of group member ARNs that are returned in a single call
    # by ListGroupResources, in paginated output. By default, this number is 50.
    max_results: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The NextToken value that is returned in a paginated ListGroupResources
    # request. To get the next page of results, run the call again, add the
    # NextToken parameter, and specify the NextToken value.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ListGroupResourcesOutput(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "resource_identifiers",
                "ResourceIdentifiers",
                TypeInfo(typing.List[ResourceIdentifier]),
            ),
            (
                "next_token",
                "NextToken",
                TypeInfo(str),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The ARNs and resource types of resources that are members of the group that
    # you specified.
    resource_identifiers: typing.List["ResourceIdentifier"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The NextToken value to include in a subsequent `ListGroupResources`
    # request, to get more results.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    def paginate(self,
                ) -> typing.Generator["ListGroupResourcesOutput", None, None]:
        yield from super()._paginate()


@dataclasses.dataclass
class ListGroupsInput(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "max_results",
                "MaxResults",
                TypeInfo(int),
            ),
            (
                "next_token",
                "NextToken",
                TypeInfo(str),
            ),
        ]

    # The maximum number of resource group results that are returned by
    # ListGroups in paginated output. By default, this number is 50.
    max_results: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The NextToken value that is returned in a paginated `ListGroups` request.
    # To get the next page of results, run the call again, add the NextToken
    # parameter, and specify the NextToken value.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ListGroupsOutput(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "groups",
                "Groups",
                TypeInfo(typing.List[Group]),
            ),
            (
                "next_token",
                "NextToken",
                TypeInfo(str),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A list of resource groups.
    groups: typing.List["Group"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The NextToken value to include in a subsequent `ListGroups` request, to get
    # more results.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    def paginate(self, ) -> typing.Generator["ListGroupsOutput", None, None]:
        yield from super()._paginate()


@dataclasses.dataclass
class MethodNotAllowedException(ShapeBase):
    """
    The request uses an HTTP method which is not allowed for the specified resource.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "message",
                "Message",
                TypeInfo(str),
            ),
        ]

    message: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class NotFoundException(ShapeBase):
    """
    One or more resources specified in the request do not exist.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "message",
                "Message",
                TypeInfo(str),
            ),
        ]

    message: str = dataclasses.field(default=ShapeBase.NOT_SET, )


class QueryType(str):
    TAG_FILTERS_1_0 = "TAG_FILTERS_1_0"


@dataclasses.dataclass
class ResourceFilter(ShapeBase):
    """
    A filter name and value pair that is used to obtain more specific results from a
    list of resources.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "name",
                "Name",
                TypeInfo(typing.Union[str, ResourceFilterName]),
            ),
            (
                "values",
                "Values",
                TypeInfo(typing.List[str]),
            ),
        ]

    # The name of the filter. Filter names are case-sensitive.
    name: typing.Union[str, "ResourceFilterName"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # One or more filter values. Allowed filter values vary by resource filter
    # name, and are case-sensitive.
    values: typing.List[str] = dataclasses.field(default=ShapeBase.NOT_SET, )


class ResourceFilterName(str):
    resource_type = "resource-type"


@dataclasses.dataclass
class ResourceIdentifier(ShapeBase):
    """
    The ARN of a resource, and its resource type.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "resource_arn",
                "ResourceArn",
                TypeInfo(str),
            ),
            (
                "resource_type",
                "ResourceType",
                TypeInfo(str),
            ),
        ]

    # The ARN of a resource.
    resource_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The resource type of a resource, such as `AWS::EC2::Instance`.
    resource_type: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ResourceQuery(ShapeBase):
    """
    The query that is used to define a resource group or a search for resources.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "type",
                "Type",
                TypeInfo(typing.Union[str, QueryType]),
            ),
            (
                "query",
                "Query",
                TypeInfo(str),
            ),
        ]

    # The type of the query. The valid value in this release is
    # `TAG_FILTERS_1_0`.

    # _`TAG_FILTERS_1_0:` _ A JSON syntax that lets you specify a collection of
    # simple tag filters for resource types and tags, as supported by the AWS
    # Tagging API GetResources operation. When more than one element is present,
    # only resources that match all filters are part of the result. If a filter
    # specifies more than one value for a key, a resource matches the filter if
    # its tag value matches any of the specified values.
    type: typing.Union[str, "QueryType"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The query that defines a group or a search.
    query: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class SearchResourcesInput(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "resource_query",
                "ResourceQuery",
                TypeInfo(ResourceQuery),
            ),
            (
                "max_results",
                "MaxResults",
                TypeInfo(int),
            ),
            (
                "next_token",
                "NextToken",
                TypeInfo(str),
            ),
        ]

    # The search query, using the same formats that are supported for resource
    # group definition.
    resource_query: "ResourceQuery" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The maximum number of group member ARNs returned by `SearchResources` in
    # paginated output. By default, this number is 50.
    max_results: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The NextToken value that is returned in a paginated `SearchResources`
    # request. To get the next page of results, run the call again, add the
    # NextToken parameter, and specify the NextToken value.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class SearchResourcesOutput(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "resource_identifiers",
                "ResourceIdentifiers",
                TypeInfo(typing.List[ResourceIdentifier]),
            ),
            (
                "next_token",
                "NextToken",
                TypeInfo(str),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The ARNs and resource types of resources that are members of the group that
    # you specified.
    resource_identifiers: typing.List["ResourceIdentifier"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The NextToken value to include in a subsequent `SearchResources` request,
    # to get more results.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    def paginate(self,
                ) -> typing.Generator["SearchResourcesOutput", None, None]:
        yield from super()._paginate()


@dataclasses.dataclass
class TagInput(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "arn",
                "Arn",
                TypeInfo(str),
            ),
            (
                "tags",
                "Tags",
                TypeInfo(typing.Dict[str, str]),
            ),
        ]

    # The ARN of the resource to which to add tags.
    arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The tags to add to the specified resource. A tag is a string-to-string map
    # of key-value pairs. Tag keys can have a maximum character length of 128
    # characters, and tag values can have a maximum length of 256 characters.
    tags: typing.Dict[str, str] = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class TagOutput(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "arn",
                "Arn",
                TypeInfo(str),
            ),
            (
                "tags",
                "Tags",
                TypeInfo(typing.Dict[str, str]),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The ARN of the tagged resource.
    arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The tags that have been added to the specified resource.
    tags: typing.Dict[str, str] = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class TooManyRequestsException(ShapeBase):
    """
    The caller has exceeded throttling limits.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "message",
                "Message",
                TypeInfo(str),
            ),
        ]

    message: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class UnauthorizedException(ShapeBase):
    """
    The request has not been applied because it lacks valid authentication
    credentials for the target resource.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "message",
                "Message",
                TypeInfo(str),
            ),
        ]

    message: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class UntagInput(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "arn",
                "Arn",
                TypeInfo(str),
            ),
            (
                "keys",
                "Keys",
                TypeInfo(typing.List[str]),
            ),
        ]

    # The ARN of the resource from which to remove tags.
    arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The keys of the tags to be removed.
    keys: typing.List[str] = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class UntagOutput(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "arn",
                "Arn",
                TypeInfo(str),
            ),
            (
                "keys",
                "Keys",
                TypeInfo(typing.List[str]),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The ARN of the resource from which tags have been removed.
    arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The keys of tags that have been removed.
    keys: typing.List[str] = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class UpdateGroupInput(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "group_name",
                "GroupName",
                TypeInfo(str),
            ),
            (
                "description",
                "Description",
                TypeInfo(str),
            ),
        ]

    # The name of the resource group for which you want to update its
    # description.
    group_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The description of the resource group. Descriptions can have a maximum of
    # 511 characters, including letters, numbers, hyphens, underscores,
    # punctuation, and spaces.
    description: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class UpdateGroupOutput(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "group",
                "Group",
                TypeInfo(Group),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The full description of the resource group after it has been updated.
    group: "Group" = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class UpdateGroupQueryInput(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "group_name",
                "GroupName",
                TypeInfo(str),
            ),
            (
                "resource_query",
                "ResourceQuery",
                TypeInfo(ResourceQuery),
            ),
        ]

    # The name of the resource group for which you want to edit the query.
    group_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The resource query that determines which AWS resources are members of the
    # resource group.
    resource_query: "ResourceQuery" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class UpdateGroupQueryOutput(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "group_query",
                "GroupQuery",
                TypeInfo(GroupQuery),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The resource query associated with the resource group after the update.
    group_query: "GroupQuery" = dataclasses.field(default=ShapeBase.NOT_SET, )
