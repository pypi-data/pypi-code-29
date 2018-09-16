import datetime
import typing
from autoboto import ShapeBase, OutputShapeBase, TypeInfo
import dataclasses


@dataclasses.dataclass
class AccessDeniedException(ShapeBase):
    """
    The user is not authorized to access a resource.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "message",
                "message",
                TypeInfo(str),
            ),
        ]

    message: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class AssociateIpGroupsRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "directory_id",
                "DirectoryId",
                TypeInfo(str),
            ),
            (
                "group_ids",
                "GroupIds",
                TypeInfo(typing.List[str]),
            ),
        ]

    # The ID of the directory.
    directory_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The IDs of one or more IP access control groups.
    group_ids: typing.List[str] = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class AssociateIpGroupsResult(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class AuthorizeIpRulesRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "group_id",
                "GroupId",
                TypeInfo(str),
            ),
            (
                "user_rules",
                "UserRules",
                TypeInfo(typing.List[IpRuleItem]),
            ),
        ]

    # The ID of the group.
    group_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The rules to add to the group.
    user_rules: typing.List["IpRuleItem"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class AuthorizeIpRulesResult(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


class Compute(str):
    VALUE = "VALUE"
    STANDARD = "STANDARD"
    PERFORMANCE = "PERFORMANCE"
    POWER = "POWER"
    GRAPHICS = "GRAPHICS"


@dataclasses.dataclass
class ComputeType(ShapeBase):
    """
    Information about the compute type.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "name",
                "Name",
                TypeInfo(typing.Union[str, Compute]),
            ),
        ]

    # The compute type.
    name: typing.Union[str, "Compute"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


class ConnectionState(str):
    CONNECTED = "CONNECTED"
    DISCONNECTED = "DISCONNECTED"
    UNKNOWN = "UNKNOWN"


@dataclasses.dataclass
class CreateIpGroupRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "group_name",
                "GroupName",
                TypeInfo(str),
            ),
            (
                "group_desc",
                "GroupDesc",
                TypeInfo(str),
            ),
            (
                "user_rules",
                "UserRules",
                TypeInfo(typing.List[IpRuleItem]),
            ),
        ]

    # The name of the group.
    group_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The description of the group.
    group_desc: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The rules to add to the group.
    user_rules: typing.List["IpRuleItem"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class CreateIpGroupResult(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "group_id",
                "GroupId",
                TypeInfo(str),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The ID of the group.
    group_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class CreateTagsRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "resource_id",
                "ResourceId",
                TypeInfo(str),
            ),
            (
                "tags",
                "Tags",
                TypeInfo(typing.List[Tag]),
            ),
        ]

    # The ID of the WorkSpace. To find this ID, use DescribeWorkspaces.
    resource_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The tags. Each WorkSpace can have a maximum of 50 tags.
    tags: typing.List["Tag"] = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class CreateTagsResult(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class CreateWorkspacesRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "workspaces",
                "Workspaces",
                TypeInfo(typing.List[WorkspaceRequest]),
            ),
        ]

    # The WorkSpaces to create. You can specify up to 25 WorkSpaces.
    workspaces: typing.List["WorkspaceRequest"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class CreateWorkspacesResult(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "failed_requests",
                "FailedRequests",
                TypeInfo(typing.List[FailedCreateWorkspaceRequest]),
            ),
            (
                "pending_requests",
                "PendingRequests",
                TypeInfo(typing.List[Workspace]),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Information about the WorkSpaces that could not be created.
    failed_requests: typing.List["FailedCreateWorkspaceRequest"
                                ] = dataclasses.field(
                                    default=ShapeBase.NOT_SET,
                                )

    # Information about the WorkSpaces that were created.

    # Because this operation is asynchronous, the identifier returned is not
    # immediately available for use with other operations. For example, if you
    # call DescribeWorkspaces before the WorkSpace is created, the information
    # returned can be incomplete.
    pending_requests: typing.List["Workspace"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class DefaultWorkspaceCreationProperties(ShapeBase):
    """
    Information about defaults used to create a WorkSpace.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "enable_work_docs",
                "EnableWorkDocs",
                TypeInfo(bool),
            ),
            (
                "enable_internet_access",
                "EnableInternetAccess",
                TypeInfo(bool),
            ),
            (
                "default_ou",
                "DefaultOu",
                TypeInfo(str),
            ),
            (
                "custom_security_group_id",
                "CustomSecurityGroupId",
                TypeInfo(str),
            ),
            (
                "user_enabled_as_local_administrator",
                "UserEnabledAsLocalAdministrator",
                TypeInfo(bool),
            ),
        ]

    # Indicates whether the directory is enabled for Amazon WorkDocs.
    enable_work_docs: bool = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The public IP address to attach to all WorkSpaces that are created or
    # rebuilt.
    enable_internet_access: bool = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The organizational unit (OU) in the directory for the WorkSpace machine
    # accounts.
    default_ou: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The identifier of any security groups to apply to WorkSpaces when they are
    # created.
    custom_security_group_id: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Indicates whether the WorkSpace user is an administrator on the WorkSpace.
    user_enabled_as_local_administrator: bool = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class DeleteIpGroupRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "group_id",
                "GroupId",
                TypeInfo(str),
            ),
        ]

    # The ID of the IP access control group.
    group_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DeleteIpGroupResult(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class DeleteTagsRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "resource_id",
                "ResourceId",
                TypeInfo(str),
            ),
            (
                "tag_keys",
                "TagKeys",
                TypeInfo(typing.List[str]),
            ),
        ]

    # The ID of the WorkSpace. To find this ID, use DescribeWorkspaces.
    resource_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The tag keys.
    tag_keys: typing.List[str] = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DeleteTagsResult(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class DescribeIpGroupsRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "group_ids",
                "GroupIds",
                TypeInfo(typing.List[str]),
            ),
            (
                "next_token",
                "NextToken",
                TypeInfo(str),
            ),
            (
                "max_results",
                "MaxResults",
                TypeInfo(int),
            ),
        ]

    # The IDs of one or more IP access control groups.
    group_ids: typing.List[str] = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The token for the next set of results. (You received this token from a
    # previous call.)
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The maximum number of items to return.
    max_results: int = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DescribeIpGroupsResult(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "result",
                "Result",
                TypeInfo(typing.List[WorkspacesIpGroup]),
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

    # Information about the IP access control groups.
    result: typing.List["WorkspacesIpGroup"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The token to use to retrieve the next set of results, or null if there are
    # no more results available. This token is valid for one day and must be used
    # within that time frame.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DescribeTagsRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "resource_id",
                "ResourceId",
                TypeInfo(str),
            ),
        ]

    # The ID of the WorkSpace. To find this ID, use DescribeWorkspaces.
    resource_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DescribeTagsResult(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "tag_list",
                "TagList",
                TypeInfo(typing.List[Tag]),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The tags.
    tag_list: typing.List["Tag"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class DescribeWorkspaceBundlesRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "bundle_ids",
                "BundleIds",
                TypeInfo(typing.List[str]),
            ),
            (
                "owner",
                "Owner",
                TypeInfo(str),
            ),
            (
                "next_token",
                "NextToken",
                TypeInfo(str),
            ),
        ]

    # The IDs of the bundles. This parameter cannot be combined with any other
    # filter.
    bundle_ids: typing.List[str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The owner of the bundles. This parameter cannot be combined with any other
    # filter.

    # Specify `AMAZON` to describe the bundles provided by AWS or null to
    # describe the bundles that belong to your account.
    owner: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The token for the next set of results. (You received this token from a
    # previous call.)
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DescribeWorkspaceBundlesResult(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "bundles",
                "Bundles",
                TypeInfo(typing.List[WorkspaceBundle]),
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

    # Information about the bundles.
    bundles: typing.List["WorkspaceBundle"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The token to use to retrieve the next set of results, or null if there are
    # no more results available. This token is valid for one day and must be used
    # within that time frame.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    def paginate(
        self,
    ) -> typing.Generator["DescribeWorkspaceBundlesResult", None, None]:
        yield from super()._paginate()


@dataclasses.dataclass
class DescribeWorkspaceDirectoriesRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "directory_ids",
                "DirectoryIds",
                TypeInfo(typing.List[str]),
            ),
            (
                "next_token",
                "NextToken",
                TypeInfo(str),
            ),
        ]

    # The identifiers of the directories. If the value is null, all directories
    # are retrieved.
    directory_ids: typing.List[str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The token for the next set of results. (You received this token from a
    # previous call.)
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DescribeWorkspaceDirectoriesResult(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "directories",
                "Directories",
                TypeInfo(typing.List[WorkspaceDirectory]),
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

    # Information about the directories.
    directories: typing.List["WorkspaceDirectory"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The token to use to retrieve the next set of results, or null if there are
    # no more results available. This token is valid for one day and must be used
    # within that time frame.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    def paginate(
        self,
    ) -> typing.Generator["DescribeWorkspaceDirectoriesResult", None, None]:
        yield from super()._paginate()


@dataclasses.dataclass
class DescribeWorkspacesConnectionStatusRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "workspace_ids",
                "WorkspaceIds",
                TypeInfo(typing.List[str]),
            ),
            (
                "next_token",
                "NextToken",
                TypeInfo(str),
            ),
        ]

    # The identifiers of the WorkSpaces. You can specify up to 25 WorkSpaces.
    workspace_ids: typing.List[str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The token for the next set of results. (You received this token from a
    # previous call.)
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DescribeWorkspacesConnectionStatusResult(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "workspaces_connection_status",
                "WorkspacesConnectionStatus",
                TypeInfo(typing.List[WorkspaceConnectionStatus]),
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

    # Information about the connection status of the WorkSpace.
    workspaces_connection_status: typing.List["WorkspaceConnectionStatus"
                                             ] = dataclasses.field(
                                                 default=ShapeBase.NOT_SET,
                                             )

    # The token to use to retrieve the next set of results, or null if there are
    # no more results available.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DescribeWorkspacesRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "workspace_ids",
                "WorkspaceIds",
                TypeInfo(typing.List[str]),
            ),
            (
                "directory_id",
                "DirectoryId",
                TypeInfo(str),
            ),
            (
                "user_name",
                "UserName",
                TypeInfo(str),
            ),
            (
                "bundle_id",
                "BundleId",
                TypeInfo(str),
            ),
            (
                "limit",
                "Limit",
                TypeInfo(int),
            ),
            (
                "next_token",
                "NextToken",
                TypeInfo(str),
            ),
        ]

    # The IDs of the WorkSpaces. This parameter cannot be combined with any other
    # filter.

    # Because the CreateWorkspaces operation is asynchronous, the identifier it
    # returns is not immediately available. If you immediately call
    # DescribeWorkspaces with this identifier, no information is returned.
    workspace_ids: typing.List[str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The ID of the directory. In addition, you can optionally specify a specific
    # directory user (see `UserName`). This parameter cannot be combined with any
    # other filter.
    directory_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The name of the directory user. You must specify this parameter with
    # `DirectoryId`.
    user_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The ID of the bundle. All WorkSpaces that are created from this bundle are
    # retrieved. This parameter cannot be combined with any other filter.
    bundle_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The maximum number of items to return.
    limit: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The token for the next set of results. (You received this token from a
    # previous call.)
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DescribeWorkspacesResult(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "workspaces",
                "Workspaces",
                TypeInfo(typing.List[Workspace]),
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

    # Information about the WorkSpaces.

    # Because CreateWorkspaces is an asynchronous operation, some of the returned
    # information could be incomplete.
    workspaces: typing.List["Workspace"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The token to use to retrieve the next set of results, or null if there are
    # no more results available. This token is valid for one day and must be used
    # within that time frame.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    def paginate(self,
                ) -> typing.Generator["DescribeWorkspacesResult", None, None]:
        yield from super()._paginate()


@dataclasses.dataclass
class DisassociateIpGroupsRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "directory_id",
                "DirectoryId",
                TypeInfo(str),
            ),
            (
                "group_ids",
                "GroupIds",
                TypeInfo(typing.List[str]),
            ),
        ]

    # The ID of the directory.
    directory_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The IDs of one or more IP access control groups.
    group_ids: typing.List[str] = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DisassociateIpGroupsResult(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class FailedCreateWorkspaceRequest(ShapeBase):
    """
    Information about a WorkSpace that could not be created.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "workspace_request",
                "WorkspaceRequest",
                TypeInfo(WorkspaceRequest),
            ),
            (
                "error_code",
                "ErrorCode",
                TypeInfo(str),
            ),
            (
                "error_message",
                "ErrorMessage",
                TypeInfo(str),
            ),
        ]

    # Information about the WorkSpace.
    workspace_request: "WorkspaceRequest" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The error code.
    error_code: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The textual error message.
    error_message: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class FailedWorkspaceChangeRequest(ShapeBase):
    """
    Information about a WorkSpace that could not be rebooted (RebootWorkspaces),
    rebuilt (RebuildWorkspaces), terminated (TerminateWorkspaces), started
    (StartWorkspaces), or stopped (StopWorkspaces).
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "workspace_id",
                "WorkspaceId",
                TypeInfo(str),
            ),
            (
                "error_code",
                "ErrorCode",
                TypeInfo(str),
            ),
            (
                "error_message",
                "ErrorMessage",
                TypeInfo(str),
            ),
        ]

    # The identifier of the WorkSpace.
    workspace_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The error code.
    error_code: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The textual error message.
    error_message: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class InvalidParameterValuesException(ShapeBase):
    """
    One or more parameter values are not valid.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "message",
                "message",
                TypeInfo(str),
            ),
        ]

    # The exception error message.
    message: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class InvalidResourceStateException(ShapeBase):
    """
    The state of the resource is not valid for this operation.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "message",
                "message",
                TypeInfo(str),
            ),
        ]

    message: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class IpRuleItem(ShapeBase):
    """
    Information about a rule for an IP access control group.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "ip_rule",
                "ipRule",
                TypeInfo(str),
            ),
            (
                "rule_desc",
                "ruleDesc",
                TypeInfo(str),
            ),
        ]

    # The IP address range, in CIDR notation.
    ip_rule: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The description.
    rule_desc: str = dataclasses.field(default=ShapeBase.NOT_SET, )


class ModificationResourceEnum(str):
    ROOT_VOLUME = "ROOT_VOLUME"
    USER_VOLUME = "USER_VOLUME"
    COMPUTE_TYPE = "COMPUTE_TYPE"


@dataclasses.dataclass
class ModificationState(ShapeBase):
    """
    Information about a WorkSpace modification.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "resource",
                "Resource",
                TypeInfo(typing.Union[str, ModificationResourceEnum]),
            ),
            (
                "state",
                "State",
                TypeInfo(typing.Union[str, ModificationStateEnum]),
            ),
        ]

    # The resource.
    resource: typing.Union[str, "ModificationResourceEnum"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The modification state.
    state: typing.Union[str, "ModificationStateEnum"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


class ModificationStateEnum(str):
    UPDATE_INITIATED = "UPDATE_INITIATED"
    UPDATE_IN_PROGRESS = "UPDATE_IN_PROGRESS"


@dataclasses.dataclass
class ModifyWorkspacePropertiesRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "workspace_id",
                "WorkspaceId",
                TypeInfo(str),
            ),
            (
                "workspace_properties",
                "WorkspaceProperties",
                TypeInfo(WorkspaceProperties),
            ),
        ]

    # The ID of the WorkSpace.
    workspace_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The properties of the WorkSpace.
    workspace_properties: "WorkspaceProperties" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class ModifyWorkspacePropertiesResult(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class ModifyWorkspaceStateRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "workspace_id",
                "WorkspaceId",
                TypeInfo(str),
            ),
            (
                "workspace_state",
                "WorkspaceState",
                TypeInfo(typing.Union[str, TargetWorkspaceState]),
            ),
        ]

    # The ID of the WorkSpace.
    workspace_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The WorkSpace state.
    workspace_state: typing.Union[str, "TargetWorkspaceState"
                                 ] = dataclasses.field(
                                     default=ShapeBase.NOT_SET,
                                 )


@dataclasses.dataclass
class ModifyWorkspaceStateResult(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class OperationInProgressException(ShapeBase):
    """
    The properties of this WorkSpace are currently being modified. Try again in a
    moment.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "message",
                "message",
                TypeInfo(str),
            ),
        ]

    message: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class OperationNotSupportedException(ShapeBase):
    """
    This operation is not supported.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "message",
                "message",
                TypeInfo(str),
            ),
        ]

    message: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class RebootRequest(ShapeBase):
    """
    Information used to reboot a WorkSpace.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "workspace_id",
                "WorkspaceId",
                TypeInfo(str),
            ),
        ]

    # The ID of the WorkSpace.
    workspace_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class RebootWorkspacesRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "reboot_workspace_requests",
                "RebootWorkspaceRequests",
                TypeInfo(typing.List[RebootRequest]),
            ),
        ]

    # The WorkSpaces to reboot. You can specify up to 25 WorkSpaces.
    reboot_workspace_requests: typing.List["RebootRequest"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class RebootWorkspacesResult(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "failed_requests",
                "FailedRequests",
                TypeInfo(typing.List[FailedWorkspaceChangeRequest]),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Information about the WorkSpaces that could not be rebooted.
    failed_requests: typing.List["FailedWorkspaceChangeRequest"
                                ] = dataclasses.field(
                                    default=ShapeBase.NOT_SET,
                                )


@dataclasses.dataclass
class RebuildRequest(ShapeBase):
    """
    Information used to rebuild a WorkSpace.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "workspace_id",
                "WorkspaceId",
                TypeInfo(str),
            ),
        ]

    # The ID of the WorkSpace.
    workspace_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class RebuildWorkspacesRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "rebuild_workspace_requests",
                "RebuildWorkspaceRequests",
                TypeInfo(typing.List[RebuildRequest]),
            ),
        ]

    # The WorkSpace to rebuild. You can specify a single WorkSpace.
    rebuild_workspace_requests: typing.List["RebuildRequest"
                                           ] = dataclasses.field(
                                               default=ShapeBase.NOT_SET,
                                           )


@dataclasses.dataclass
class RebuildWorkspacesResult(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "failed_requests",
                "FailedRequests",
                TypeInfo(typing.List[FailedWorkspaceChangeRequest]),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Information about the WorkSpace if it could not be rebuilt.
    failed_requests: typing.List["FailedWorkspaceChangeRequest"
                                ] = dataclasses.field(
                                    default=ShapeBase.NOT_SET,
                                )


@dataclasses.dataclass
class ResourceAlreadyExistsException(ShapeBase):
    """
    The specified resource already exists.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "message",
                "message",
                TypeInfo(str),
            ),
        ]

    message: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ResourceAssociatedException(ShapeBase):
    """
    The resource is associated with a directory.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "message",
                "message",
                TypeInfo(str),
            ),
        ]

    message: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ResourceCreationFailedException(ShapeBase):
    """
    The resource could not be created.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "message",
                "message",
                TypeInfo(str),
            ),
        ]

    message: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ResourceLimitExceededException(ShapeBase):
    """
    Your resource limits have been exceeded.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "message",
                "message",
                TypeInfo(str),
            ),
        ]

    # The exception error message.
    message: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ResourceNotFoundException(ShapeBase):
    """
    The resource could not be found.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "message",
                "message",
                TypeInfo(str),
            ),
            (
                "resource_id",
                "ResourceId",
                TypeInfo(str),
            ),
        ]

    # The resource could not be found.
    message: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The ID of the resource that could not be found.
    resource_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ResourceUnavailableException(ShapeBase):
    """
    The specified resource is not available.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "message",
                "message",
                TypeInfo(str),
            ),
            (
                "resource_id",
                "ResourceId",
                TypeInfo(str),
            ),
        ]

    # The exception error message.
    message: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The identifier of the resource that is not available.
    resource_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class RevokeIpRulesRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "group_id",
                "GroupId",
                TypeInfo(str),
            ),
            (
                "user_rules",
                "UserRules",
                TypeInfo(typing.List[str]),
            ),
        ]

    # The ID of the group.
    group_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The rules to remove from the group.
    user_rules: typing.List[str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class RevokeIpRulesResult(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class RootStorage(ShapeBase):
    """
    Information about the root volume for a WorkSpace bundle.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "capacity",
                "Capacity",
                TypeInfo(str),
            ),
        ]

    # The size of the root volume.
    capacity: str = dataclasses.field(default=ShapeBase.NOT_SET, )


class RunningMode(str):
    AUTO_STOP = "AUTO_STOP"
    ALWAYS_ON = "ALWAYS_ON"


@dataclasses.dataclass
class StartRequest(ShapeBase):
    """
    Information used to start a WorkSpace.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "workspace_id",
                "WorkspaceId",
                TypeInfo(str),
            ),
        ]

    # The ID of the WorkSpace.
    workspace_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class StartWorkspacesRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "start_workspace_requests",
                "StartWorkspaceRequests",
                TypeInfo(typing.List[StartRequest]),
            ),
        ]

    # The WorkSpaces to start. You can specify up to 25 WorkSpaces.
    start_workspace_requests: typing.List["StartRequest"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class StartWorkspacesResult(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "failed_requests",
                "FailedRequests",
                TypeInfo(typing.List[FailedWorkspaceChangeRequest]),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Information about the WorkSpaces that could not be started.
    failed_requests: typing.List["FailedWorkspaceChangeRequest"
                                ] = dataclasses.field(
                                    default=ShapeBase.NOT_SET,
                                )


@dataclasses.dataclass
class StopRequest(ShapeBase):
    """
    Information used to stop a WorkSpace.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "workspace_id",
                "WorkspaceId",
                TypeInfo(str),
            ),
        ]

    # The ID of the WorkSpace.
    workspace_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class StopWorkspacesRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "stop_workspace_requests",
                "StopWorkspaceRequests",
                TypeInfo(typing.List[StopRequest]),
            ),
        ]

    # The WorkSpaces to stop. You can specify up to 25 WorkSpaces.
    stop_workspace_requests: typing.List["StopRequest"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class StopWorkspacesResult(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "failed_requests",
                "FailedRequests",
                TypeInfo(typing.List[FailedWorkspaceChangeRequest]),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Information about the WorkSpaces that could not be stopped.
    failed_requests: typing.List["FailedWorkspaceChangeRequest"
                                ] = dataclasses.field(
                                    default=ShapeBase.NOT_SET,
                                )


@dataclasses.dataclass
class Tag(ShapeBase):
    """
    Information about a tag.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "key",
                "Key",
                TypeInfo(str),
            ),
            (
                "value",
                "Value",
                TypeInfo(str),
            ),
        ]

    # The key of the tag.
    key: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The value of the tag.
    value: str = dataclasses.field(default=ShapeBase.NOT_SET, )


class TargetWorkspaceState(str):
    AVAILABLE = "AVAILABLE"
    ADMIN_MAINTENANCE = "ADMIN_MAINTENANCE"


@dataclasses.dataclass
class TerminateRequest(ShapeBase):
    """
    Information used to terminate a WorkSpace.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "workspace_id",
                "WorkspaceId",
                TypeInfo(str),
            ),
        ]

    # The ID of the WorkSpace.
    workspace_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class TerminateWorkspacesRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "terminate_workspace_requests",
                "TerminateWorkspaceRequests",
                TypeInfo(typing.List[TerminateRequest]),
            ),
        ]

    # The WorkSpaces to terminate. You can specify up to 25 WorkSpaces.
    terminate_workspace_requests: typing.List["TerminateRequest"
                                             ] = dataclasses.field(
                                                 default=ShapeBase.NOT_SET,
                                             )


@dataclasses.dataclass
class TerminateWorkspacesResult(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "failed_requests",
                "FailedRequests",
                TypeInfo(typing.List[FailedWorkspaceChangeRequest]),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Information about the WorkSpaces that could not be terminated.
    failed_requests: typing.List["FailedWorkspaceChangeRequest"
                                ] = dataclasses.field(
                                    default=ShapeBase.NOT_SET,
                                )


@dataclasses.dataclass
class UnsupportedWorkspaceConfigurationException(ShapeBase):
    """
    The configuration of this WorkSpace is not supported for this operation. For
    more information, see the [Amazon WorkSpaces Administration
    Guide](http://docs.aws.amazon.com/workspaces/latest/adminguide/).
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "message",
                "message",
                TypeInfo(str),
            ),
        ]

    message: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class UpdateRulesOfIpGroupRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "group_id",
                "GroupId",
                TypeInfo(str),
            ),
            (
                "user_rules",
                "UserRules",
                TypeInfo(typing.List[IpRuleItem]),
            ),
        ]

    # The ID of the group.
    group_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # One or more rules.
    user_rules: typing.List["IpRuleItem"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class UpdateRulesOfIpGroupResult(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class UserStorage(ShapeBase):
    """
    Information about the user storage for a WorkSpace bundle.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "capacity",
                "Capacity",
                TypeInfo(str),
            ),
        ]

    # The size of the user storage.
    capacity: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class Workspace(ShapeBase):
    """
    Information about a WorkSpace.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "workspace_id",
                "WorkspaceId",
                TypeInfo(str),
            ),
            (
                "directory_id",
                "DirectoryId",
                TypeInfo(str),
            ),
            (
                "user_name",
                "UserName",
                TypeInfo(str),
            ),
            (
                "ip_address",
                "IpAddress",
                TypeInfo(str),
            ),
            (
                "state",
                "State",
                TypeInfo(typing.Union[str, WorkspaceState]),
            ),
            (
                "bundle_id",
                "BundleId",
                TypeInfo(str),
            ),
            (
                "subnet_id",
                "SubnetId",
                TypeInfo(str),
            ),
            (
                "error_message",
                "ErrorMessage",
                TypeInfo(str),
            ),
            (
                "error_code",
                "ErrorCode",
                TypeInfo(str),
            ),
            (
                "computer_name",
                "ComputerName",
                TypeInfo(str),
            ),
            (
                "volume_encryption_key",
                "VolumeEncryptionKey",
                TypeInfo(str),
            ),
            (
                "user_volume_encryption_enabled",
                "UserVolumeEncryptionEnabled",
                TypeInfo(bool),
            ),
            (
                "root_volume_encryption_enabled",
                "RootVolumeEncryptionEnabled",
                TypeInfo(bool),
            ),
            (
                "workspace_properties",
                "WorkspaceProperties",
                TypeInfo(WorkspaceProperties),
            ),
            (
                "modification_states",
                "ModificationStates",
                TypeInfo(typing.List[ModificationState]),
            ),
        ]

    # The identifier of the WorkSpace.
    workspace_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The identifier of the AWS Directory Service directory for the WorkSpace.
    directory_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The user for the WorkSpace.
    user_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The IP address of the WorkSpace.
    ip_address: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The operational state of the WorkSpace.
    state: typing.Union[str, "WorkspaceState"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The identifier of the bundle used to create the WorkSpace.
    bundle_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The identifier of the subnet for the WorkSpace.
    subnet_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # If the WorkSpace could not be created, contains a textual error message
    # that describes the failure.
    error_message: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # If the WorkSpace could not be created, contains the error code.
    error_code: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The name of the WorkSpace, as seen by the operating system.
    computer_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The KMS key used to encrypt data stored on your WorkSpace.
    volume_encryption_key: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Indicates whether the data stored on the user volume is encrypted.
    user_volume_encryption_enabled: bool = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Indicates whether the data stored on the root volume is encrypted.
    root_volume_encryption_enabled: bool = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The properties of the WorkSpace.
    workspace_properties: "WorkspaceProperties" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The modification states of the WorkSpace.
    modification_states: typing.List["ModificationState"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class WorkspaceBundle(ShapeBase):
    """
    Information about a WorkSpace bundle.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "bundle_id",
                "BundleId",
                TypeInfo(str),
            ),
            (
                "name",
                "Name",
                TypeInfo(str),
            ),
            (
                "owner",
                "Owner",
                TypeInfo(str),
            ),
            (
                "description",
                "Description",
                TypeInfo(str),
            ),
            (
                "root_storage",
                "RootStorage",
                TypeInfo(RootStorage),
            ),
            (
                "user_storage",
                "UserStorage",
                TypeInfo(UserStorage),
            ),
            (
                "compute_type",
                "ComputeType",
                TypeInfo(ComputeType),
            ),
        ]

    # The bundle identifier.
    bundle_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The name of the bundle.
    name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The owner of the bundle. This is the account identifier of the owner, or
    # `AMAZON` if the bundle is provided by AWS.
    owner: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A description.
    description: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The size of the root volume.
    root_storage: "RootStorage" = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The size of the user storage.
    user_storage: "UserStorage" = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The compute type. For more information, see [Amazon WorkSpaces
    # Bundles](http://aws.amazon.com/workspaces/details/#Amazon_WorkSpaces_Bundles).
    compute_type: "ComputeType" = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class WorkspaceConnectionStatus(ShapeBase):
    """
    Describes the connection status of a WorkSpace.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "workspace_id",
                "WorkspaceId",
                TypeInfo(str),
            ),
            (
                "connection_state",
                "ConnectionState",
                TypeInfo(typing.Union[str, ConnectionState]),
            ),
            (
                "connection_state_check_timestamp",
                "ConnectionStateCheckTimestamp",
                TypeInfo(datetime.datetime),
            ),
            (
                "last_known_user_connection_timestamp",
                "LastKnownUserConnectionTimestamp",
                TypeInfo(datetime.datetime),
            ),
        ]

    # The ID of the WorkSpace.
    workspace_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The connection state of the WorkSpace. The connection state is unknown if
    # the WorkSpace is stopped.
    connection_state: typing.Union[str, "ConnectionState"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The timestamp of the connection state check.
    connection_state_check_timestamp: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The timestamp of the last known user connection.
    last_known_user_connection_timestamp: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class WorkspaceDirectory(ShapeBase):
    """
    Information about an AWS Directory Service directory for use with Amazon
    WorkSpaces.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "directory_id",
                "DirectoryId",
                TypeInfo(str),
            ),
            (
                "alias",
                "Alias",
                TypeInfo(str),
            ),
            (
                "directory_name",
                "DirectoryName",
                TypeInfo(str),
            ),
            (
                "registration_code",
                "RegistrationCode",
                TypeInfo(str),
            ),
            (
                "subnet_ids",
                "SubnetIds",
                TypeInfo(typing.List[str]),
            ),
            (
                "dns_ip_addresses",
                "DnsIpAddresses",
                TypeInfo(typing.List[str]),
            ),
            (
                "customer_user_name",
                "CustomerUserName",
                TypeInfo(str),
            ),
            (
                "iam_role_id",
                "IamRoleId",
                TypeInfo(str),
            ),
            (
                "directory_type",
                "DirectoryType",
                TypeInfo(typing.Union[str, WorkspaceDirectoryType]),
            ),
            (
                "workspace_security_group_id",
                "WorkspaceSecurityGroupId",
                TypeInfo(str),
            ),
            (
                "state",
                "State",
                TypeInfo(typing.Union[str, WorkspaceDirectoryState]),
            ),
            (
                "workspace_creation_properties",
                "WorkspaceCreationProperties",
                TypeInfo(DefaultWorkspaceCreationProperties),
            ),
            (
                "ip_group_ids",
                "ipGroupIds",
                TypeInfo(typing.List[str]),
            ),
        ]

    # The directory identifier.
    directory_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The directory alias.
    alias: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The name of the directory.
    directory_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The registration code for the directory. This is the code that users enter
    # in their Amazon WorkSpaces client application to connect to the directory.
    registration_code: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The identifiers of the subnets used with the directory.
    subnet_ids: typing.List[str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The IP addresses of the DNS servers for the directory.
    dns_ip_addresses: typing.List[str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The user name for the service account.
    customer_user_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The identifier of the IAM role. This is the role that allows Amazon
    # WorkSpaces to make calls to other services, such as Amazon EC2, on your
    # behalf.
    iam_role_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The directory type.
    directory_type: typing.Union[str, "WorkspaceDirectoryType"
                                ] = dataclasses.field(
                                    default=ShapeBase.NOT_SET,
                                )

    # The identifier of the security group that is assigned to new WorkSpaces.
    workspace_security_group_id: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The state of the directory's registration with Amazon WorkSpaces
    state: typing.Union[str, "WorkspaceDirectoryState"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The default creation properties for all WorkSpaces in the directory.
    workspace_creation_properties: "DefaultWorkspaceCreationProperties" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The identifiers of the IP access control groups associated with the
    # directory.
    ip_group_ids: typing.List[str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


class WorkspaceDirectoryState(str):
    REGISTERING = "REGISTERING"
    REGISTERED = "REGISTERED"
    DEREGISTERING = "DEREGISTERING"
    DEREGISTERED = "DEREGISTERED"
    ERROR = "ERROR"


class WorkspaceDirectoryType(str):
    SIMPLE_AD = "SIMPLE_AD"
    AD_CONNECTOR = "AD_CONNECTOR"


@dataclasses.dataclass
class WorkspaceProperties(ShapeBase):
    """
    Information about a WorkSpace.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "running_mode",
                "RunningMode",
                TypeInfo(typing.Union[str, RunningMode]),
            ),
            (
                "running_mode_auto_stop_timeout_in_minutes",
                "RunningModeAutoStopTimeoutInMinutes",
                TypeInfo(int),
            ),
            (
                "root_volume_size_gib",
                "RootVolumeSizeGib",
                TypeInfo(int),
            ),
            (
                "user_volume_size_gib",
                "UserVolumeSizeGib",
                TypeInfo(int),
            ),
            (
                "compute_type_name",
                "ComputeTypeName",
                TypeInfo(typing.Union[str, Compute]),
            ),
        ]

    # The running mode. For more information, see [Manage the WorkSpace Running
    # Mode](http://docs.aws.amazon.com/workspaces/latest/adminguide/running-
    # mode.html).
    running_mode: typing.Union[str, "RunningMode"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The time after a user logs off when WorkSpaces are automatically stopped.
    # Configured in 60 minute intervals.
    running_mode_auto_stop_timeout_in_minutes: int = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The size of the root volume.
    root_volume_size_gib: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The size of the user storage.
    user_volume_size_gib: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The compute type. For more information, see [Amazon WorkSpaces
    # Bundles](http://aws.amazon.com/workspaces/details/#Amazon_WorkSpaces_Bundles).
    compute_type_name: typing.Union[str, "Compute"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class WorkspaceRequest(ShapeBase):
    """
    Information used to create a WorkSpace.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "directory_id",
                "DirectoryId",
                TypeInfo(str),
            ),
            (
                "user_name",
                "UserName",
                TypeInfo(str),
            ),
            (
                "bundle_id",
                "BundleId",
                TypeInfo(str),
            ),
            (
                "volume_encryption_key",
                "VolumeEncryptionKey",
                TypeInfo(str),
            ),
            (
                "user_volume_encryption_enabled",
                "UserVolumeEncryptionEnabled",
                TypeInfo(bool),
            ),
            (
                "root_volume_encryption_enabled",
                "RootVolumeEncryptionEnabled",
                TypeInfo(bool),
            ),
            (
                "workspace_properties",
                "WorkspaceProperties",
                TypeInfo(WorkspaceProperties),
            ),
            (
                "tags",
                "Tags",
                TypeInfo(typing.List[Tag]),
            ),
        ]

    # The identifier of the AWS Directory Service directory for the WorkSpace.
    # You can use DescribeWorkspaceDirectories to list the available directories.
    directory_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The username of the user for the WorkSpace. This username must exist in the
    # AWS Directory Service directory for the WorkSpace.
    user_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The identifier of the bundle for the WorkSpace. You can use
    # DescribeWorkspaceBundles to list the available bundles.
    bundle_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The KMS key used to encrypt data stored on your WorkSpace.
    volume_encryption_key: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Indicates whether the data stored on the user volume is encrypted.
    user_volume_encryption_enabled: bool = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Indicates whether the data stored on the root volume is encrypted.
    root_volume_encryption_enabled: bool = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The WorkSpace properties.
    workspace_properties: "WorkspaceProperties" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The tags for the WorkSpace.
    tags: typing.List["Tag"] = dataclasses.field(default=ShapeBase.NOT_SET, )


class WorkspaceState(str):
    PENDING = "PENDING"
    AVAILABLE = "AVAILABLE"
    IMPAIRED = "IMPAIRED"
    UNHEALTHY = "UNHEALTHY"
    REBOOTING = "REBOOTING"
    STARTING = "STARTING"
    REBUILDING = "REBUILDING"
    MAINTENANCE = "MAINTENANCE"
    ADMIN_MAINTENANCE = "ADMIN_MAINTENANCE"
    TERMINATING = "TERMINATING"
    TERMINATED = "TERMINATED"
    SUSPENDED = "SUSPENDED"
    UPDATING = "UPDATING"
    STOPPING = "STOPPING"
    STOPPED = "STOPPED"
    ERROR = "ERROR"


@dataclasses.dataclass
class WorkspacesIpGroup(ShapeBase):
    """
    Information about an IP access control group.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "group_id",
                "groupId",
                TypeInfo(str),
            ),
            (
                "group_name",
                "groupName",
                TypeInfo(str),
            ),
            (
                "group_desc",
                "groupDesc",
                TypeInfo(str),
            ),
            (
                "user_rules",
                "userRules",
                TypeInfo(typing.List[IpRuleItem]),
            ),
        ]

    # The ID of the group.
    group_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The name of the group.
    group_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The description of the group.
    group_desc: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The rules.
    user_rules: typing.List["IpRuleItem"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )
