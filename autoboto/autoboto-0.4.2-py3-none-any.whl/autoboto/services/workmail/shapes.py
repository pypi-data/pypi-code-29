import datetime
import typing
from autoboto import ShapeBase, OutputShapeBase, TypeInfo
import dataclasses


@dataclasses.dataclass
class AssociateDelegateToResourceRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "organization_id",
                "OrganizationId",
                TypeInfo(str),
            ),
            (
                "resource_id",
                "ResourceId",
                TypeInfo(str),
            ),
            (
                "entity_id",
                "EntityId",
                TypeInfo(str),
            ),
        ]

    # The organization under which the resource exists.
    organization_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The resource for which members are associated.
    resource_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The member (user or group) to associate to the resource.
    entity_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class AssociateDelegateToResourceResponse(OutputShapeBase):
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
class AssociateMemberToGroupRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "organization_id",
                "OrganizationId",
                TypeInfo(str),
            ),
            (
                "group_id",
                "GroupId",
                TypeInfo(str),
            ),
            (
                "member_id",
                "MemberId",
                TypeInfo(str),
            ),
        ]

    # The organization under which the group exists.
    organization_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The group for which the member is associated.
    group_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The member to associate to the group.
    member_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class AssociateMemberToGroupResponse(OutputShapeBase):
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
class BookingOptions(ShapeBase):
    """
    At least one delegate must be associated to the resource to disable automatic
    replies from the resource.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "auto_accept_requests",
                "AutoAcceptRequests",
                TypeInfo(bool),
            ),
            (
                "auto_decline_recurring_requests",
                "AutoDeclineRecurringRequests",
                TypeInfo(bool),
            ),
            (
                "auto_decline_conflicting_requests",
                "AutoDeclineConflictingRequests",
                TypeInfo(bool),
            ),
        ]

    # The resource's ability to automatically reply to requests. If disabled,
    # delegates must be associated to the resource.
    auto_accept_requests: bool = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The resource's ability to automatically decline any recurring requests.
    auto_decline_recurring_requests: bool = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The resource's ability to automatically decline any conflicting requests.
    auto_decline_conflicting_requests: bool = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class CreateAliasRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "organization_id",
                "OrganizationId",
                TypeInfo(str),
            ),
            (
                "entity_id",
                "EntityId",
                TypeInfo(str),
            ),
            (
                "alias",
                "Alias",
                TypeInfo(str),
            ),
        ]

    # The organization under which the member exists.
    organization_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The alias is added to this Amazon WorkMail entity.
    entity_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The alias to add to the user.
    alias: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class CreateAliasResponse(OutputShapeBase):
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
class CreateGroupRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "organization_id",
                "OrganizationId",
                TypeInfo(str),
            ),
            (
                "name",
                "Name",
                TypeInfo(str),
            ),
        ]

    # The organization under which the group is to be created.
    organization_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The name of the group.
    name: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class CreateGroupResponse(OutputShapeBase):
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
class CreateResourceRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "organization_id",
                "OrganizationId",
                TypeInfo(str),
            ),
            (
                "name",
                "Name",
                TypeInfo(str),
            ),
            (
                "type",
                "Type",
                TypeInfo(typing.Union[str, ResourceType]),
            ),
        ]

    # The identifier associated with the organization for which the resource is
    # created.
    organization_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The name of the created resource.
    name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The type of the created resource.
    type: typing.Union[str, "ResourceType"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class CreateResourceResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "resource_id",
                "ResourceId",
                TypeInfo(str),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The identifier of the created resource.
    resource_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class CreateUserRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "organization_id",
                "OrganizationId",
                TypeInfo(str),
            ),
            (
                "name",
                "Name",
                TypeInfo(str),
            ),
            (
                "display_name",
                "DisplayName",
                TypeInfo(str),
            ),
            (
                "password",
                "Password",
                TypeInfo(str),
            ),
        ]

    # The identifier of the organization for which the user is created.
    organization_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The name for the user to be created.
    name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The display name for the user to be created.
    display_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The password for the user to be created.
    password: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class CreateUserResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "user_id",
                "UserId",
                TypeInfo(str),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The information regarding the newly created user.
    user_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class Delegate(ShapeBase):
    """
    The name of the attribute, which is one of the values defined in the
    UserAttribute enumeration.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "id",
                "Id",
                TypeInfo(str),
            ),
            (
                "type",
                "Type",
                TypeInfo(typing.Union[str, MemberType]),
            ),
        ]

    # The identifier for the user or group is associated as the resource's
    # delegate.
    id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The type of the delegate: user or group.
    type: typing.Union[str, "MemberType"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class DeleteAliasRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "organization_id",
                "OrganizationId",
                TypeInfo(str),
            ),
            (
                "entity_id",
                "EntityId",
                TypeInfo(str),
            ),
            (
                "alias",
                "Alias",
                TypeInfo(str),
            ),
        ]

    # The identifier for the organization under which the user exists.
    organization_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The identifier for the Amazon WorkMail entity to have the aliases removed.
    entity_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The aliases to be removed from the user's set of aliases. Duplicate entries
    # in the list are collapsed into single entries (the list is transformed into
    # a set).
    alias: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DeleteAliasResponse(OutputShapeBase):
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
class DeleteGroupRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "organization_id",
                "OrganizationId",
                TypeInfo(str),
            ),
            (
                "group_id",
                "GroupId",
                TypeInfo(str),
            ),
        ]

    # The organization that contains the group.
    organization_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The identifier of the group to be deleted.
    group_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DeleteGroupResponse(OutputShapeBase):
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
class DeleteMailboxPermissionsRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "organization_id",
                "OrganizationId",
                TypeInfo(str),
            ),
            (
                "entity_id",
                "EntityId",
                TypeInfo(str),
            ),
            (
                "grantee_id",
                "GranteeId",
                TypeInfo(str),
            ),
        ]

    # The identifier of the organization under which the entity (user or group)
    # exists.
    organization_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The identifier of the entity (user or group) for which to delete mailbox
    # permissions.
    entity_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The identifier of the entity (user or group) for which to delete granted
    # permissions.
    grantee_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DeleteMailboxPermissionsResponse(OutputShapeBase):
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
class DeleteResourceRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "organization_id",
                "OrganizationId",
                TypeInfo(str),
            ),
            (
                "resource_id",
                "ResourceId",
                TypeInfo(str),
            ),
        ]

    # The identifier associated with the organization for which the resource is
    # deleted.
    organization_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The identifier of the resource to be deleted.
    resource_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DeleteResourceResponse(OutputShapeBase):
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
class DeleteUserRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "organization_id",
                "OrganizationId",
                TypeInfo(str),
            ),
            (
                "user_id",
                "UserId",
                TypeInfo(str),
            ),
        ]

    # The organization that contains the user.
    organization_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The identifier of the user to be deleted.
    user_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DeleteUserResponse(OutputShapeBase):
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
class DeregisterFromWorkMailRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "organization_id",
                "OrganizationId",
                TypeInfo(str),
            ),
            (
                "entity_id",
                "EntityId",
                TypeInfo(str),
            ),
        ]

    # The identifier for the organization under which the Amazon WorkMail entity
    # exists.
    organization_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The identifier for the entity to be updated.
    entity_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DeregisterFromWorkMailResponse(OutputShapeBase):
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
class DescribeGroupRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "organization_id",
                "OrganizationId",
                TypeInfo(str),
            ),
            (
                "group_id",
                "GroupId",
                TypeInfo(str),
            ),
        ]

    # The identifier for the organization under which the group exists.
    organization_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The identifier for the group to be described.
    group_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DescribeGroupResponse(OutputShapeBase):
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
            (
                "name",
                "Name",
                TypeInfo(str),
            ),
            (
                "email",
                "Email",
                TypeInfo(str),
            ),
            (
                "state",
                "State",
                TypeInfo(typing.Union[str, EntityState]),
            ),
            (
                "enabled_date",
                "EnabledDate",
                TypeInfo(datetime.datetime),
            ),
            (
                "disabled_date",
                "DisabledDate",
                TypeInfo(datetime.datetime),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The identifier of the described group.
    group_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The name of the described group.
    name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The email of the described group.
    email: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The state of the user: enabled (registered to Amazon WorkMail) or disabled
    # (deregistered or never registered to Amazon WorkMail).
    state: typing.Union[str, "EntityState"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The date and time when a user was registered to Amazon WorkMail, in UNIX
    # epoch time format.
    enabled_date: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The date and time when a user was deregistered from Amazon WorkMail, in
    # UNIX epoch time format.
    disabled_date: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class DescribeOrganizationRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "organization_id",
                "OrganizationId",
                TypeInfo(str),
            ),
        ]

    # The identifier for the organization to be described.
    organization_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DescribeOrganizationResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "organization_id",
                "OrganizationId",
                TypeInfo(str),
            ),
            (
                "alias",
                "Alias",
                TypeInfo(str),
            ),
            (
                "state",
                "State",
                TypeInfo(str),
            ),
            (
                "directory_id",
                "DirectoryId",
                TypeInfo(str),
            ),
            (
                "directory_type",
                "DirectoryType",
                TypeInfo(str),
            ),
            (
                "default_mail_domain",
                "DefaultMailDomain",
                TypeInfo(str),
            ),
            (
                "completed_date",
                "CompletedDate",
                TypeInfo(datetime.datetime),
            ),
            (
                "error_message",
                "ErrorMessage",
                TypeInfo(str),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The identifier of an organization.
    organization_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The alias for an organization.
    alias: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The state of an organization.
    state: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The identifier for the directory associated with an Amazon WorkMail
    # organization.
    directory_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The type of directory associated with the Amazon WorkMail organization.
    directory_type: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The default mail domain associated with the organization.
    default_mail_domain: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The date at which the organization became usable in the Amazon WorkMail
    # context, in UNIX epoch time format.
    completed_date: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The (optional) error message indicating if unexpected behavior was
    # encountered with regards to the organization.
    error_message: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DescribeResourceRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "organization_id",
                "OrganizationId",
                TypeInfo(str),
            ),
            (
                "resource_id",
                "ResourceId",
                TypeInfo(str),
            ),
        ]

    # The identifier associated with the organization for which the resource is
    # described.
    organization_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The identifier of the resource to be described.
    resource_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DescribeResourceResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "resource_id",
                "ResourceId",
                TypeInfo(str),
            ),
            (
                "email",
                "Email",
                TypeInfo(str),
            ),
            (
                "name",
                "Name",
                TypeInfo(str),
            ),
            (
                "type",
                "Type",
                TypeInfo(typing.Union[str, ResourceType]),
            ),
            (
                "booking_options",
                "BookingOptions",
                TypeInfo(BookingOptions),
            ),
            (
                "state",
                "State",
                TypeInfo(typing.Union[str, EntityState]),
            ),
            (
                "enabled_date",
                "EnabledDate",
                TypeInfo(datetime.datetime),
            ),
            (
                "disabled_date",
                "DisabledDate",
                TypeInfo(datetime.datetime),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The identifier of the described resource.
    resource_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The email of the described resource.
    email: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The name of the described resource.
    name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The type of the described resource.
    type: typing.Union[str, "ResourceType"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The booking options for the described resource.
    booking_options: "BookingOptions" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The state of the resource: enabled (registered to Amazon WorkMail) or
    # disabled (deregistered or never registered to Amazon WorkMail).
    state: typing.Union[str, "EntityState"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The date and time when a resource was registered to Amazon WorkMail, in
    # UNIX epoch time format.
    enabled_date: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The date and time when a resource was registered from Amazon WorkMail, in
    # UNIX epoch time format.
    disabled_date: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class DescribeUserRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "organization_id",
                "OrganizationId",
                TypeInfo(str),
            ),
            (
                "user_id",
                "UserId",
                TypeInfo(str),
            ),
        ]

    # The identifier for the organization under which the user exists.
    organization_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The identifier for the user to be described.
    user_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DescribeUserResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "user_id",
                "UserId",
                TypeInfo(str),
            ),
            (
                "name",
                "Name",
                TypeInfo(str),
            ),
            (
                "email",
                "Email",
                TypeInfo(str),
            ),
            (
                "display_name",
                "DisplayName",
                TypeInfo(str),
            ),
            (
                "state",
                "State",
                TypeInfo(typing.Union[str, EntityState]),
            ),
            (
                "user_role",
                "UserRole",
                TypeInfo(typing.Union[str, UserRole]),
            ),
            (
                "enabled_date",
                "EnabledDate",
                TypeInfo(datetime.datetime),
            ),
            (
                "disabled_date",
                "DisabledDate",
                TypeInfo(datetime.datetime),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The identifier for the described user.
    user_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The name for the user.
    name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The email of the user.
    email: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The display name of the user.
    display_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The state of a user: enabled (registered to Amazon WorkMail) or disabled
    # (deregistered or never registered to Amazon WorkMail).
    state: typing.Union[str, "EntityState"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # In certain cases other entities are modeled as users. If interoperability
    # is enabled, resources are imported into Amazon WorkMail as users. Because
    # different Amazon WorkMail organizations rely on different directory types,
    # administrators can distinguish between a user that is not registered to
    # Amazon WorkMail (is disabled and has a user role) and the administrative
    # users of the directory. The values are USER, RESOURCE, and SYSTEM_USER.
    user_role: typing.Union[str, "UserRole"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The date and time at which the user was enabled for Amazon WorkMail usage,
    # in UNIX epoch time format.
    enabled_date: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The date and time at which the user was disabled for Amazon WorkMail usage,
    # in UNIX epoch time format.
    disabled_date: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class DirectoryServiceAuthenticationFailedException(ShapeBase):
    """
    The Directory Service doesn't recognize the credentials supplied by the Amazon
    WorkMail service.
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
class DirectoryUnavailableException(ShapeBase):
    """
    The directory that you are trying to perform operations on isn't available.
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
class DisassociateDelegateFromResourceRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "organization_id",
                "OrganizationId",
                TypeInfo(str),
            ),
            (
                "resource_id",
                "ResourceId",
                TypeInfo(str),
            ),
            (
                "entity_id",
                "EntityId",
                TypeInfo(str),
            ),
        ]

    # The identifier for the organization under which the resource exists.
    organization_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The identifier of the resource from which delegates' set members are
    # removed.
    resource_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The identifier for the member (user, group) to be removed from the
    # resource's delegates.
    entity_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DisassociateDelegateFromResourceResponse(OutputShapeBase):
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
class DisassociateMemberFromGroupRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "organization_id",
                "OrganizationId",
                TypeInfo(str),
            ),
            (
                "group_id",
                "GroupId",
                TypeInfo(str),
            ),
            (
                "member_id",
                "MemberId",
                TypeInfo(str),
            ),
        ]

    # The identifier for the organization under which the group exists.
    organization_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The identifier for the group from which members are removed.
    group_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The identifier for the member to be removed to the group.
    member_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DisassociateMemberFromGroupResponse(OutputShapeBase):
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
class EmailAddressInUseException(ShapeBase):
    """
    The email address that you're trying to assign is already created for a
    different user, group, or resource.
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
class EntityAlreadyRegisteredException(ShapeBase):
    """
    The user, group, or resource that you're trying to register is already
    registered.
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
class EntityNotFoundException(ShapeBase):
    """
    The identifier supplied for the entity is valid, but it does not exist in your
    organization.
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


class EntityState(str):
    ENABLED = "ENABLED"
    DISABLED = "DISABLED"
    DELETED = "DELETED"


@dataclasses.dataclass
class EntityStateException(ShapeBase):
    """
    You are performing an operation on an entity that isn't in the expected state,
    such as trying to update a deleted user.
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
class Group(ShapeBase):
    """
    The representation of an Amazon WorkMail group.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "id",
                "Id",
                TypeInfo(str),
            ),
            (
                "email",
                "Email",
                TypeInfo(str),
            ),
            (
                "name",
                "Name",
                TypeInfo(str),
            ),
            (
                "state",
                "State",
                TypeInfo(typing.Union[str, EntityState]),
            ),
            (
                "enabled_date",
                "EnabledDate",
                TypeInfo(datetime.datetime),
            ),
            (
                "disabled_date",
                "DisabledDate",
                TypeInfo(datetime.datetime),
            ),
        ]

    # The identifier of the group.
    id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The email of the group.
    email: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The name of the group.
    name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The state of the group, which can be ENABLED, DISABLED, or DELETED.
    state: typing.Union[str, "EntityState"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The date indicating when the group was enabled for Amazon WorkMail use.
    enabled_date: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The date indicating when the group was disabled from Amazon WorkMail use.
    disabled_date: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class InvalidConfigurationException(ShapeBase):
    """
    The configuration for a resource isn't valid. A resource must either be able to
    auto-respond to requests or have at least one delegate associated that can do it
    on its behalf.
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
class InvalidParameterException(ShapeBase):
    """
    One or more of the input parameters don't match the service's restrictions.
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
class InvalidPasswordException(ShapeBase):
    """
    The supplied password doesn't match the minimum security constraints, such as
    length or use of special characters.
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
class ListAliasesRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "organization_id",
                "OrganizationId",
                TypeInfo(str),
            ),
            (
                "entity_id",
                "EntityId",
                TypeInfo(str),
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

    # The identifier for the organization under which the entity exists.
    organization_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The identifier for the entity for which to list the aliases.
    entity_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The token to use to retrieve the next page of results. The first call does
    # not contain any tokens.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The maximum number of results to return in a single call.
    max_results: int = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ListAliasesResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "aliases",
                "Aliases",
                TypeInfo(typing.List[str]),
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

    # The entity's paginated aliases.
    aliases: typing.List[str] = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The token to use to retrieve the next page of results. The value is "null"
    # when there are no more results to return.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    def paginate(self, ) -> typing.Generator["ListAliasesResponse", None, None]:
        yield from super()._paginate()


@dataclasses.dataclass
class ListGroupMembersRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "organization_id",
                "OrganizationId",
                TypeInfo(str),
            ),
            (
                "group_id",
                "GroupId",
                TypeInfo(str),
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

    # The identifier for the organization under which the group exists.
    organization_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The identifier for the group to which the members are associated.
    group_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The token to use to retrieve the next page of results. The first call does
    # not contain any tokens.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The maximum number of results to return in a single call.
    max_results: int = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ListGroupMembersResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "members",
                "Members",
                TypeInfo(typing.List[Member]),
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

    # The members associated to the group.
    members: typing.List["Member"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The token to use to retrieve the next page of results. The first call does
    # not contain any tokens.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    def paginate(self,
                ) -> typing.Generator["ListGroupMembersResponse", None, None]:
        yield from super()._paginate()


@dataclasses.dataclass
class ListGroupsRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "organization_id",
                "OrganizationId",
                TypeInfo(str),
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

    # The identifier for the organization under which the groups exist.
    organization_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The token to use to retrieve the next page of results. The first call does
    # not contain any tokens.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The maximum number of results to return in a single call.
    max_results: int = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ListGroupsResponse(OutputShapeBase):
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

    # The overview of groups for an organization.
    groups: typing.List["Group"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The token to use to retrieve the next page of results. The value is "null"
    # when there are no more results to return.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    def paginate(self, ) -> typing.Generator["ListGroupsResponse", None, None]:
        yield from super()._paginate()


@dataclasses.dataclass
class ListMailboxPermissionsRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "organization_id",
                "OrganizationId",
                TypeInfo(str),
            ),
            (
                "entity_id",
                "EntityId",
                TypeInfo(str),
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

    # The identifier of the organization under which the entity (user or group)
    # exists.
    organization_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The identifier of the entity (user or group) for which to list mailbox
    # permissions.
    entity_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The token to use to retrieve the next page of results. The first call does
    # not contain any tokens.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The maximum number of results to return in a single call.
    max_results: int = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ListMailboxPermissionsResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "permissions",
                "Permissions",
                TypeInfo(typing.List[Permission]),
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

    # One page of the entity's mailbox permissions.
    permissions: typing.List["Permission"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The token to use to retrieve the next page of results. The value is "null"
    # when there are no more results to return.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ListOrganizationsRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
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

    # The token to use to retrieve the next page of results. The first call does
    # not contain any tokens.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The maximum number of results to return in a single call.
    max_results: int = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ListOrganizationsResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "organization_summaries",
                "OrganizationSummaries",
                TypeInfo(typing.List[OrganizationSummary]),
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

    # The overview of owned organizations presented as a list of organization
    # summaries.
    organization_summaries: typing.List["OrganizationSummary"
                                       ] = dataclasses.field(
                                           default=ShapeBase.NOT_SET,
                                       )

    # The token to use to retrieve the next page of results. The value is "null"
    # when there are no more results to return.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    def paginate(self,
                ) -> typing.Generator["ListOrganizationsResponse", None, None]:
        yield from super()._paginate()


@dataclasses.dataclass
class ListResourceDelegatesRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "organization_id",
                "OrganizationId",
                TypeInfo(str),
            ),
            (
                "resource_id",
                "ResourceId",
                TypeInfo(str),
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

    # The identifier for the organization that contains the resource for which
    # delegates are listed.
    organization_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The identifier for the resource whose delegates are listed.
    resource_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The token used to paginate through the delegates associated with a
    # resource.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The number of maximum results in a page.
    max_results: int = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ListResourceDelegatesResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "delegates",
                "Delegates",
                TypeInfo(typing.List[Delegate]),
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

    # One page of the resource's delegates.
    delegates: typing.List["Delegate"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The token used to paginate through the delegates associated with a
    # resource. While results are still available, it has an associated value.
    # When the last page is reached, the token is empty.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ListResourcesRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "organization_id",
                "OrganizationId",
                TypeInfo(str),
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

    # The identifier for the organization under which the resources exist.
    organization_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The token to use to retrieve the next page of results. The first call does
    # not contain any tokens.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The maximum number of results to return in a single call.
    max_results: int = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ListResourcesResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "resources",
                "Resources",
                TypeInfo(typing.List[Resource]),
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

    # One page of the organization's resource representation.
    resources: typing.List["Resource"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The token used to paginate through all the organization's resources. While
    # results are still available, it has an associated value. When the last page
    # is reached, the token is empty.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    def paginate(self,
                ) -> typing.Generator["ListResourcesResponse", None, None]:
        yield from super()._paginate()


@dataclasses.dataclass
class ListUsersRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "organization_id",
                "OrganizationId",
                TypeInfo(str),
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

    # The identifier for the organization under which the users exist.
    organization_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # TBD
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The maximum number of results to return in a single call.
    max_results: int = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ListUsersResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "users",
                "Users",
                TypeInfo(typing.List[User]),
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

    # The overview of users for an organization.
    users: typing.List["User"] = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The token to use to retrieve the next page of results. This value is `null`
    # when there are no more results to return.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    def paginate(self, ) -> typing.Generator["ListUsersResponse", None, None]:
        yield from super()._paginate()


@dataclasses.dataclass
class MailDomainNotFoundException(ShapeBase):
    """
    For an email or alias to be created in Amazon WorkMail, the included domain must
    be defined in the organization.
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
class MailDomainStateException(ShapeBase):
    """
    After a domain has been added to the organization, it must be verified. The
    domain is not yet verified.
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
class Member(ShapeBase):
    """
    The representation of a group member (user or group).
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "id",
                "Id",
                TypeInfo(str),
            ),
            (
                "name",
                "Name",
                TypeInfo(str),
            ),
            (
                "type",
                "Type",
                TypeInfo(typing.Union[str, MemberType]),
            ),
            (
                "state",
                "State",
                TypeInfo(typing.Union[str, EntityState]),
            ),
            (
                "enabled_date",
                "EnabledDate",
                TypeInfo(datetime.datetime),
            ),
            (
                "disabled_date",
                "DisabledDate",
                TypeInfo(datetime.datetime),
            ),
        ]

    # The identifier of the member.
    id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The name of the member.
    name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A member can be a user or group.
    type: typing.Union[str, "MemberType"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The state of the member, which can be ENABLED, DISABLED, or DELETED.
    state: typing.Union[str, "EntityState"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The date indicating when the member was enabled for Amazon WorkMail use.
    enabled_date: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The date indicating when the member was disabled from Amazon WorkMail use.
    disabled_date: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


class MemberType(str):
    GROUP = "GROUP"
    USER = "USER"


@dataclasses.dataclass
class NameAvailabilityException(ShapeBase):
    """
    The entity (user, group, or user) name isn't unique in Amazon WorkMail.
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
class OrganizationNotFoundException(ShapeBase):
    """
    An operation received a valid organization identifier that either doesn't belong
    or exist in the system.
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
class OrganizationStateException(ShapeBase):
    """
    The organization must have a valid state (Active or Synchronizing) to perform
    certain operations on the organization or its entities.
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
class OrganizationSummary(ShapeBase):
    """
    The brief overview associated with an organization.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "organization_id",
                "OrganizationId",
                TypeInfo(str),
            ),
            (
                "alias",
                "Alias",
                TypeInfo(str),
            ),
            (
                "error_message",
                "ErrorMessage",
                TypeInfo(str),
            ),
            (
                "state",
                "State",
                TypeInfo(str),
            ),
        ]

    # The identifier associated with the organization.
    organization_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The alias associated with the organization.
    alias: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The error message associated with the organization. It is only present if
    # unexpected behavior has occurred with regards to the organization. It
    # provides insight or solutions regarding unexpected behavior.
    error_message: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The state associated with the organization.
    state: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class Permission(ShapeBase):
    """
    Permission granted to an entity (user, group) to access a certain aspect of
    another entity's mailbox.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "grantee_id",
                "GranteeId",
                TypeInfo(str),
            ),
            (
                "grantee_type",
                "GranteeType",
                TypeInfo(typing.Union[str, MemberType]),
            ),
            (
                "permission_values",
                "PermissionValues",
                TypeInfo(typing.List[typing.Union[str, PermissionType]]),
            ),
        ]

    # The identifier of the entity (user or group) to which the permissions are
    # granted.
    grantee_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The type of entity (user, group) of the entity referred to in GranteeId.
    grantee_type: typing.Union[str, "MemberType"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The permissions granted to the grantee. SEND_AS allows the grantee to send
    # email as the owner of the mailbox (the grantee is not mentioned on these
    # emails). SEND_ON_BEHALF allows the grantee to send email on behalf of the
    # owner of the mailbox (the grantee is not mentioned as the physical sender
    # of these emails). FULL_ACCESS allows the grantee full access to the
    # mailbox, irrespective of other folder-level permissions set on the mailbox.
    permission_values: typing.List[typing.Union[str, "PermissionType"]
                                  ] = dataclasses.field(
                                      default=ShapeBase.NOT_SET,
                                  )


class PermissionType(str):
    FULL_ACCESS = "FULL_ACCESS"
    SEND_AS = "SEND_AS"
    SEND_ON_BEHALF = "SEND_ON_BEHALF"


@dataclasses.dataclass
class PutMailboxPermissionsRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "organization_id",
                "OrganizationId",
                TypeInfo(str),
            ),
            (
                "entity_id",
                "EntityId",
                TypeInfo(str),
            ),
            (
                "grantee_id",
                "GranteeId",
                TypeInfo(str),
            ),
            (
                "permission_values",
                "PermissionValues",
                TypeInfo(typing.List[typing.Union[str, PermissionType]]),
            ),
        ]

    # The identifier of the organization under which the entity (user or group)
    # exists.
    organization_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The identifier of the entity (user or group) for which to update mailbox
    # permissions.
    entity_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The identifier of the entity (user or group) to which to grant the
    # permissions.
    grantee_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The permissions granted to the grantee. SEND_AS allows the grantee to send
    # email as the owner of the mailbox (the grantee is not mentioned on these
    # emails). SEND_ON_BEHALF allows the grantee to send email on behalf of the
    # owner of the mailbox (the grantee is not mentioned as the physical sender
    # of these emails). FULL_ACCESS allows the grantee full access to the
    # mailbox, irrespective of other folder-level permissions set on the mailbox.
    permission_values: typing.List[typing.Union[str, "PermissionType"]
                                  ] = dataclasses.field(
                                      default=ShapeBase.NOT_SET,
                                  )


@dataclasses.dataclass
class PutMailboxPermissionsResponse(OutputShapeBase):
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
class RegisterToWorkMailRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "organization_id",
                "OrganizationId",
                TypeInfo(str),
            ),
            (
                "entity_id",
                "EntityId",
                TypeInfo(str),
            ),
            (
                "email",
                "Email",
                TypeInfo(str),
            ),
        ]

    # The identifier for the organization under which the Amazon WorkMail entity
    # exists.
    organization_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The identifier for the entity to be updated.
    entity_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The email for the entity to be updated.
    email: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class RegisterToWorkMailResponse(OutputShapeBase):
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
class ReservedNameException(ShapeBase):
    """
    This entity name is not allowed in Amazon WorkMail.
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
class ResetPasswordRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "organization_id",
                "OrganizationId",
                TypeInfo(str),
            ),
            (
                "user_id",
                "UserId",
                TypeInfo(str),
            ),
            (
                "password",
                "Password",
                TypeInfo(str),
            ),
        ]

    # The identifier of the organization that contains the user for which the
    # password is reset.
    organization_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The identifier of the user for whom the password is reset.
    user_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The new password for the user.
    password: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ResetPasswordResponse(OutputShapeBase):
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
class Resource(ShapeBase):
    """
    The overview for a resource containing relevant data regarding it.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "id",
                "Id",
                TypeInfo(str),
            ),
            (
                "email",
                "Email",
                TypeInfo(str),
            ),
            (
                "name",
                "Name",
                TypeInfo(str),
            ),
            (
                "type",
                "Type",
                TypeInfo(typing.Union[str, ResourceType]),
            ),
            (
                "state",
                "State",
                TypeInfo(typing.Union[str, EntityState]),
            ),
            (
                "enabled_date",
                "EnabledDate",
                TypeInfo(datetime.datetime),
            ),
            (
                "disabled_date",
                "DisabledDate",
                TypeInfo(datetime.datetime),
            ),
        ]

    # The identifier of the resource.
    id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The email of the resource.
    email: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The name of the resource.
    name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The type of the resource: equipment or room.
    type: typing.Union[str, "ResourceType"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The state of the resource, which can be ENABLED, DISABLED, or DELETED.
    state: typing.Union[str, "EntityState"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The date indicating when the resource was enabled for Amazon WorkMail use.
    enabled_date: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The date indicating when the resource was disabled from Amazon WorkMail
    # use.
    disabled_date: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


class ResourceType(str):
    ROOM = "ROOM"
    EQUIPMENT = "EQUIPMENT"


@dataclasses.dataclass
class UnsupportedOperationException(ShapeBase):
    """
    You can't perform a write operation against a read-only directory.
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
class UpdatePrimaryEmailAddressRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "organization_id",
                "OrganizationId",
                TypeInfo(str),
            ),
            (
                "entity_id",
                "EntityId",
                TypeInfo(str),
            ),
            (
                "email",
                "Email",
                TypeInfo(str),
            ),
        ]

    # The organization that contains the entity to update.
    organization_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The entity to update (user, group, or resource).
    entity_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The value of the email to be updated as primary.
    email: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class UpdatePrimaryEmailAddressResponse(OutputShapeBase):
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
class UpdateResourceRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "organization_id",
                "OrganizationId",
                TypeInfo(str),
            ),
            (
                "resource_id",
                "ResourceId",
                TypeInfo(str),
            ),
            (
                "name",
                "Name",
                TypeInfo(str),
            ),
            (
                "booking_options",
                "BookingOptions",
                TypeInfo(BookingOptions),
            ),
        ]

    # The identifier associated with the organization for which the resource is
    # updated.
    organization_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The identifier of the resource to be updated.
    resource_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The name of the resource to be updated.
    name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The resource's booking options to be updated.
    booking_options: "BookingOptions" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class UpdateResourceResponse(OutputShapeBase):
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
class User(ShapeBase):
    """
    The representation of an Amazon WorkMail user.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "id",
                "Id",
                TypeInfo(str),
            ),
            (
                "email",
                "Email",
                TypeInfo(str),
            ),
            (
                "name",
                "Name",
                TypeInfo(str),
            ),
            (
                "display_name",
                "DisplayName",
                TypeInfo(str),
            ),
            (
                "state",
                "State",
                TypeInfo(typing.Union[str, EntityState]),
            ),
            (
                "user_role",
                "UserRole",
                TypeInfo(typing.Union[str, UserRole]),
            ),
            (
                "enabled_date",
                "EnabledDate",
                TypeInfo(datetime.datetime),
            ),
            (
                "disabled_date",
                "DisabledDate",
                TypeInfo(datetime.datetime),
            ),
        ]

    # The identifier of the user.
    id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The email of the user.
    email: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The name of the user.
    name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The display name of the user.
    display_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The state of the user, which can be ENABLED, DISABLED, or DELETED.
    state: typing.Union[str, "EntityState"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The role of the user.
    user_role: typing.Union[str, "UserRole"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The date indicating when the user was enabled for Amazon WorkMail use.
    enabled_date: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The date indicating when the user was disabled from Amazon WorkMail use.
    disabled_date: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


class UserRole(str):
    USER = "USER"
    RESOURCE = "RESOURCE"
    SYSTEM_USER = "SYSTEM_USER"
