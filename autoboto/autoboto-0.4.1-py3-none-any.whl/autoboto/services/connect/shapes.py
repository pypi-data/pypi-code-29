import datetime
import typing
from autoboto import ShapeBase, OutputShapeBase, TypeInfo
import dataclasses


@dataclasses.dataclass
class ContactNotFoundException(ShapeBase):
    """
    The contact with the specified ID is not active or does not exist.
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

    # The message.
    message: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class CreateUserRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "username",
                "Username",
                TypeInfo(str),
            ),
            (
                "phone_config",
                "PhoneConfig",
                TypeInfo(UserPhoneConfig),
            ),
            (
                "security_profile_ids",
                "SecurityProfileIds",
                TypeInfo(typing.List[str]),
            ),
            (
                "routing_profile_id",
                "RoutingProfileId",
                TypeInfo(str),
            ),
            (
                "instance_id",
                "InstanceId",
                TypeInfo(str),
            ),
            (
                "password",
                "Password",
                TypeInfo(str),
            ),
            (
                "identity_info",
                "IdentityInfo",
                TypeInfo(UserIdentityInfo),
            ),
            (
                "directory_user_id",
                "DirectoryUserId",
                TypeInfo(str),
            ),
            (
                "hierarchy_group_id",
                "HierarchyGroupId",
                TypeInfo(str),
            ),
        ]

    # The user name in Amazon Connect for the user to create.
    username: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Specifies the phone settings for the user, including
    # AfterContactWorkTimeLimit, AutoAccept, DeskPhoneNumber, and PhoneType.
    phone_config: "UserPhoneConfig" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The unique identifier of the security profile to assign to the user
    # created.
    security_profile_ids: typing.List[str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The unique identifier for the routing profile to assign to the user
    # created.
    routing_profile_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The identifier for your Amazon Connect instance. To find the ID of your
    # instance, open the AWS console and select Amazon Connect. Select the alias
    # of the instance in the Instance alias column. The instance ID is displayed
    # in the Overview section of your instance settings. For example, the
    # instance ID is the set of characters at the end of the instance ARN, after
    # instance/, such as 10a4c4eb-f57e-4d4c-b602-bf39176ced07.
    instance_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The password for the user account to create. This is required if you are
    # using Amazon Connect for identity management. If you are using SAML for
    # identity management and include this parameter, an
    # `InvalidRequestException` is returned.
    password: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Information about the user, including email address, first name, and last
    # name.
    identity_info: "UserIdentityInfo" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The unique identifier for the user account in the directory service
    # directory used for identity management. If Amazon Connect is unable to
    # access the existing directory, you can use the `DirectoryUserId` to
    # authenticate users. If you include the parameter, it is assumed that Amazon
    # Connect cannot access the directory. If the parameter is not included, the
    # UserIdentityInfo is used to authenticate users from your existing
    # directory.

    # This parameter is required if you are using an existing directory for
    # identity management in Amazon Connect when Amazon Connect cannot access
    # your directory to authenticate users. If you are using SAML for identity
    # management and include this parameter, an `InvalidRequestException` is
    # returned.
    directory_user_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The unique identifier for the hierarchy group to assign to the user
    # created.
    hierarchy_group_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )


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
            (
                "user_arn",
                "UserArn",
                TypeInfo(str),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The unique identifier for the user account in Amazon Connect
    user_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The Amazon Resource Name (ARN) of the user account created.
    user_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class Credentials(ShapeBase):
    """
    The credentials to use for federation.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "access_token",
                "AccessToken",
                TypeInfo(str),
            ),
            (
                "access_token_expiration",
                "AccessTokenExpiration",
                TypeInfo(datetime.datetime),
            ),
            (
                "refresh_token",
                "RefreshToken",
                TypeInfo(str),
            ),
            (
                "refresh_token_expiration",
                "RefreshTokenExpiration",
                TypeInfo(datetime.datetime),
            ),
        ]

    # An access token generated for a federated user to access Amazon Connect
    access_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A token generated with an expiration time for the session a user is logged
    # in to Amazon Connect
    access_token_expiration: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Renews a token generated for a user to access the Amazon Connect instance.
    refresh_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Renews the expiration timer for a generated token.
    refresh_token_expiration: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class DeleteUserRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "instance_id",
                "InstanceId",
                TypeInfo(str),
            ),
            (
                "user_id",
                "UserId",
                TypeInfo(str),
            ),
        ]

    # The identifier for your Amazon Connect instance. To find the ID of your
    # instance, open the AWS console and select Amazon Connect. Select the alias
    # of the instance in the Instance alias column. The instance ID is displayed
    # in the Overview section of your instance settings. For example, the
    # instance ID is the set of characters at the end of the instance ARN, after
    # instance/, such as 10a4c4eb-f57e-4d4c-b602-bf39176ced07.
    instance_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The unique identifier of the user to delete.
    user_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DescribeUserHierarchyGroupRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "hierarchy_group_id",
                "HierarchyGroupId",
                TypeInfo(str),
            ),
            (
                "instance_id",
                "InstanceId",
                TypeInfo(str),
            ),
        ]

    # The identifier for the hierarchy group to return.
    hierarchy_group_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The identifier for your Amazon Connect instance. To find the ID of your
    # instance, open the AWS console and select Amazon Connect. Select the alias
    # of the instance in the Instance alias column. The instance ID is displayed
    # in the Overview section of your instance settings. For example, the
    # instance ID is the set of characters at the end of the instance ARN, after
    # instance/, such as 10a4c4eb-f57e-4d4c-b602-bf39176ced07.
    instance_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DescribeUserHierarchyGroupResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "hierarchy_group",
                "HierarchyGroup",
                TypeInfo(HierarchyGroup),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Returns a `HierarchyGroup` object.
    hierarchy_group: "HierarchyGroup" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class DescribeUserHierarchyStructureRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "instance_id",
                "InstanceId",
                TypeInfo(str),
            ),
        ]

    # The identifier for your Amazon Connect instance. To find the ID of your
    # instance, open the AWS console and select Amazon Connect. Select the alias
    # of the instance in the Instance alias column. The instance ID is displayed
    # in the Overview section of your instance settings. For example, the
    # instance ID is the set of characters at the end of the instance ARN, after
    # instance/, such as 10a4c4eb-f57e-4d4c-b602-bf39176ced07.
    instance_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DescribeUserHierarchyStructureResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "hierarchy_structure",
                "HierarchyStructure",
                TypeInfo(HierarchyStructure),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A `HierarchyStructure` object.
    hierarchy_structure: "HierarchyStructure" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class DescribeUserRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "user_id",
                "UserId",
                TypeInfo(str),
            ),
            (
                "instance_id",
                "InstanceId",
                TypeInfo(str),
            ),
        ]

    # Unique identifier for the user account to return.
    user_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The identifier for your Amazon Connect instance. To find the ID of your
    # instance, open the AWS console and select Amazon Connect. Select the alias
    # of the instance in the Instance alias column. The instance ID is displayed
    # in the Overview section of your instance settings. For example, the
    # instance ID is the set of characters at the end of the instance ARN, after
    # instance/, such as 10a4c4eb-f57e-4d4c-b602-bf39176ced07.
    instance_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )


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
                "user",
                "User",
                TypeInfo(User),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A `User` object that contains information about the user account and
    # configuration settings.
    user: "User" = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DestinationNotAllowedException(ShapeBase):
    """
    Outbound calls to the destination number are not allowed.
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

    # The message.
    message: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DuplicateResourceException(ShapeBase):
    """
    A resource with that name already exisits.
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
class GetFederationTokenRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "instance_id",
                "InstanceId",
                TypeInfo(str),
            ),
        ]

    # The identifier for your Amazon Connect instance. To find the ID of your
    # instance, open the AWS console and select Amazon Connect. Select the alias
    # of the instance in the Instance alias column. The instance ID is displayed
    # in the Overview section of your instance settings. For example, the
    # instance ID is the set of characters at the end of the instance ARN, after
    # instance/, such as 10a4c4eb-f57e-4d4c-b602-bf39176ced07.
    instance_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class GetFederationTokenResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "credentials",
                "Credentials",
                TypeInfo(Credentials),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The credentials to use for federation.
    credentials: "Credentials" = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class HierarchyGroup(ShapeBase):
    """
    A `HierarchyGroup` object that contains information about a hierarchy group in
    your Amazon Connect instance.
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
                "arn",
                "Arn",
                TypeInfo(str),
            ),
            (
                "name",
                "Name",
                TypeInfo(str),
            ),
            (
                "level_id",
                "LevelId",
                TypeInfo(str),
            ),
            (
                "hierarchy_path",
                "HierarchyPath",
                TypeInfo(HierarchyPath),
            ),
        ]

    # The identifier for the hierarchy group.
    id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The Amazon Resource Name (ARN) for the hierarchy group.
    arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The name of the hierarchy group in your instance.
    name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The identifier for the level in the hierarchy group.
    level_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A `HierarchyPath` object that contains information about the levels in the
    # hierarchy group.
    hierarchy_path: "HierarchyPath" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class HierarchyGroupSummary(ShapeBase):
    """
    A `HierarchyGroupSummary` object that contains information about the hierarchy
    group, including ARN, Id, and Name.
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
                "arn",
                "Arn",
                TypeInfo(str),
            ),
            (
                "name",
                "Name",
                TypeInfo(str),
            ),
        ]

    # The identifier of the hierarchy group.
    id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The ARN for the hierarchy group.
    arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The name of the hierarchy group.
    name: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class HierarchyLevel(ShapeBase):
    """
    A `HierarchyLevel` object that contains information about the levels in a
    hierarchy group, including ARN, Id, and Name.
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
                "arn",
                "Arn",
                TypeInfo(str),
            ),
            (
                "name",
                "Name",
                TypeInfo(str),
            ),
        ]

    # The identifier for the hierarchy group level.
    id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The ARN for the hierarchy group level.
    arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The name of the hierarchy group level.
    name: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class HierarchyPath(ShapeBase):
    """
    A `HierarchyPath` object that contains information about the levels of the
    hierarchy group.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "level_one",
                "LevelOne",
                TypeInfo(HierarchyGroupSummary),
            ),
            (
                "level_two",
                "LevelTwo",
                TypeInfo(HierarchyGroupSummary),
            ),
            (
                "level_three",
                "LevelThree",
                TypeInfo(HierarchyGroupSummary),
            ),
            (
                "level_four",
                "LevelFour",
                TypeInfo(HierarchyGroupSummary),
            ),
            (
                "level_five",
                "LevelFive",
                TypeInfo(HierarchyGroupSummary),
            ),
        ]

    # A `HierarchyGroupSummary` object that contains information about the level
    # of the hierarchy group, including ARN, Id, and Name.
    level_one: "HierarchyGroupSummary" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A `HierarchyGroupSummary` object that contains information about the level
    # of the hierarchy group, including ARN, Id, and Name.
    level_two: "HierarchyGroupSummary" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A `HierarchyGroupSummary` object that contains information about the level
    # of the hierarchy group, including ARN, Id, and Name.
    level_three: "HierarchyGroupSummary" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A `HierarchyGroupSummary` object that contains information about the level
    # of the hierarchy group, including ARN, Id, and Name.
    level_four: "HierarchyGroupSummary" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A `HierarchyGroupSummary` object that contains information about the level
    # of the hierarchy group, including ARN, Id, and Name.
    level_five: "HierarchyGroupSummary" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class HierarchyStructure(ShapeBase):
    """
    A `HierarchyStructure` object that contains information about the hierarchy
    group structure.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "level_one",
                "LevelOne",
                TypeInfo(HierarchyLevel),
            ),
            (
                "level_two",
                "LevelTwo",
                TypeInfo(HierarchyLevel),
            ),
            (
                "level_three",
                "LevelThree",
                TypeInfo(HierarchyLevel),
            ),
            (
                "level_four",
                "LevelFour",
                TypeInfo(HierarchyLevel),
            ),
            (
                "level_five",
                "LevelFive",
                TypeInfo(HierarchyLevel),
            ),
        ]

    # A `HierarchyLevel` object that contains information about the hierarchy
    # group level.
    level_one: "HierarchyLevel" = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A `HierarchyLevel` object that contains information about the hierarchy
    # group level.
    level_two: "HierarchyLevel" = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A `HierarchyLevel` object that contains information about the hierarchy
    # group level.
    level_three: "HierarchyLevel" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A `HierarchyLevel` object that contains information about the hierarchy
    # group level.
    level_four: "HierarchyLevel" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A `HierarchyLevel` object that contains information about the hierarchy
    # group level.
    level_five: "HierarchyLevel" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class InternalServiceException(ShapeBase):
    """
    Request processing failed due to an error or failure with the service.
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

    # The message.
    message: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class InvalidParameterException(ShapeBase):
    """
    One or more of the parameters provided to the operation are not valid.
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

    # The message.
    message: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class InvalidRequestException(ShapeBase):
    """
    The request is not valid.
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

    # The message.
    message: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class LimitExceededException(ShapeBase):
    """
    The allowed limit for the resource has been reached.
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

    # The message.
    message: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ListRoutingProfilesRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "instance_id",
                "InstanceId",
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

    # The identifier for your Amazon Connect instance. To find the ID of your
    # instance, open the AWS console and select Amazon Connect. Select the alias
    # of the instance in the Instance alias column. The instance ID is displayed
    # in the Overview section of your instance settings. For example, the
    # instance ID is the set of characters at the end of the instance ARN, after
    # instance/, such as 10a4c4eb-f57e-4d4c-b602-bf39176ced07.
    instance_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The token for the next set of results. Use the value returned in the
    # previous response in the next request to retrieve the next set of results.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The maximum number of routing profiles to return in the response.
    max_results: int = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ListRoutingProfilesResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "routing_profile_summary_list",
                "RoutingProfileSummaryList",
                TypeInfo(typing.List[RoutingProfileSummary]),
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

    # An array of `RoutingProfileSummary` objects that include the ARN, Id, and
    # Name of the routing profile.
    routing_profile_summary_list: typing.List["RoutingProfileSummary"
                                             ] = dataclasses.field(
                                                 default=ShapeBase.NOT_SET,
                                             )

    # A string returned in the response. Use the value returned in the response
    # as the value of the NextToken in a subsequent request to retrieve the next
    # set of results.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ListSecurityProfilesRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "instance_id",
                "InstanceId",
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

    # The identifier for your Amazon Connect instance. To find the ID of your
    # instance, open the AWS console and select Amazon Connect. Select the alias
    # of the instance in the Instance alias column. The instance ID is displayed
    # in the Overview section of your instance settings. For example, the
    # instance ID is the set of characters at the end of the instance ARN, after
    # instance/, such as 10a4c4eb-f57e-4d4c-b602-bf39176ced07.
    instance_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The token for the next set of results. Use the value returned in the
    # previous response in the next request to retrieve the next set of results.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The maximum number of security profiles to return.
    max_results: int = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ListSecurityProfilesResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "security_profile_summary_list",
                "SecurityProfileSummaryList",
                TypeInfo(typing.List[SecurityProfileSummary]),
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

    # An array of `SecurityProfileSummary` objects.
    security_profile_summary_list: typing.List["SecurityProfileSummary"
                                              ] = dataclasses.field(
                                                  default=ShapeBase.NOT_SET,
                                              )

    # A string returned in the response. Use the value returned in the response
    # as the value of the NextToken in a subsequent request to retrieve the next
    # set of results.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ListUserHierarchyGroupsRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "instance_id",
                "InstanceId",
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

    # The identifier for your Amazon Connect instance. To find the ID of your
    # instance, open the AWS console and select Amazon Connect. Select the alias
    # of the instance in the Instance alias column. The instance ID is displayed
    # in the Overview section of your instance settings. For example, the
    # instance ID is the set of characters at the end of the instance ARN, after
    # instance/, such as 10a4c4eb-f57e-4d4c-b602-bf39176ced07.
    instance_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The token for the next set of results. Use the value returned in the
    # previous response in the next request to retrieve the next set of results.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The maximum number of hierarchy groups to return.
    max_results: int = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ListUserHierarchyGroupsResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "user_hierarchy_group_summary_list",
                "UserHierarchyGroupSummaryList",
                TypeInfo(typing.List[HierarchyGroupSummary]),
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

    # An array of `HierarchyGroupSummary` objects.
    user_hierarchy_group_summary_list: typing.List["HierarchyGroupSummary"
                                                  ] = dataclasses.field(
                                                      default=ShapeBase.NOT_SET,
                                                  )

    # A string returned in the response. Use the value returned in the response
    # as the value of the NextToken in a subsequent request to retrieve the next
    # set of results.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ListUsersRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "instance_id",
                "InstanceId",
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

    # The identifier for your Amazon Connect instance. To find the ID of your
    # instance, open the AWS console and select Amazon Connect. Select the alias
    # of the instance in the Instance alias column. The instance ID is displayed
    # in the Overview section of your instance settings. For example, the
    # instance ID is the set of characters at the end of the instance ARN, after
    # instance/, such as 10a4c4eb-f57e-4d4c-b602-bf39176ced07.
    instance_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The token for the next set of results. Use the value returned in the
    # previous response in the next request to retrieve the next set of results.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The maximum number of results to return in the response.
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
                "user_summary_list",
                "UserSummaryList",
                TypeInfo(typing.List[UserSummary]),
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

    # An array of `UserSummary` objects that contain information about the users
    # in your instance.
    user_summary_list: typing.List["UserSummary"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A string returned in the response. Use the value returned in the response
    # as the value of the NextToken in a subsequent request to retrieve the next
    # set of results.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class OutboundContactNotPermittedException(ShapeBase):
    """
    The contact is not permitted.
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

    # The message.
    message: str = dataclasses.field(default=ShapeBase.NOT_SET, )


class PhoneType(str):
    SOFT_PHONE = "SOFT_PHONE"
    DESK_PHONE = "DESK_PHONE"


@dataclasses.dataclass
class ResourceNotFoundException(ShapeBase):
    """
    The specified resource was not found.
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

    # The message.
    message: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class RoutingProfileSummary(ShapeBase):
    """
    A `RoutingProfileSummary` object that contains information about a routing
    profile, including ARN, Id, and Name.
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
                "arn",
                "Arn",
                TypeInfo(str),
            ),
            (
                "name",
                "Name",
                TypeInfo(str),
            ),
        ]

    # The identifier of the routing profile.
    id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The ARN of the routing profile.
    arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The name of the routing profile.
    name: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class SecurityProfileSummary(ShapeBase):
    """
    A `SecurityProfileSummary` object that contains information about a security
    profile, including ARN, Id, Name.
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
                "arn",
                "Arn",
                TypeInfo(str),
            ),
            (
                "name",
                "Name",
                TypeInfo(str),
            ),
        ]

    # The identifier of the security profile.
    id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The ARN of the security profile.
    arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The name of the security profile.
    name: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class StartOutboundVoiceContactRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "destination_phone_number",
                "DestinationPhoneNumber",
                TypeInfo(str),
            ),
            (
                "contact_flow_id",
                "ContactFlowId",
                TypeInfo(str),
            ),
            (
                "instance_id",
                "InstanceId",
                TypeInfo(str),
            ),
            (
                "client_token",
                "ClientToken",
                TypeInfo(str),
            ),
            (
                "source_phone_number",
                "SourcePhoneNumber",
                TypeInfo(str),
            ),
            (
                "queue_id",
                "QueueId",
                TypeInfo(str),
            ),
            (
                "attributes",
                "Attributes",
                TypeInfo(typing.Dict[str, str]),
            ),
        ]

    # The phone number of the customer in E.164 format.
    destination_phone_number: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The identifier for the contact flow to connect the outbound call to.

    # To find the `ContactFlowId`, open the contact flow you want to use in the
    # Amazon Connect contact flow editor. The ID for the contact flow is
    # displayed in the address bar as part of the URL. For example, the contact
    # flow ID is the set of characters at the end of the URL, after 'contact-
    # flow/' such as `78ea8fd5-2659-4f2b-b528-699760ccfc1b`.
    contact_flow_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The identifier for your Amazon Connect instance. To find the ID of your
    # instance, open the AWS console and select Amazon Connect. Select the alias
    # of the instance in the Instance alias column. The instance ID is displayed
    # in the Overview section of your instance settings. For example, the
    # instance ID is the set of characters at the end of the instance ARN, after
    # instance/, such as 10a4c4eb-f57e-4d4c-b602-bf39176ced07.
    instance_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A unique, case-sensitive identifier that you provide to ensure the
    # idempotency of the request. The token is valid for 7 days after creation.
    # If a contact is already started, the contact ID is returned. If the contact
    # is disconnected, a new contact is started.
    client_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The phone number, in E.164 format, associated with your Amazon Connect
    # instance to use for the outbound call.
    source_phone_number: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The queue to add the call to. If you specify a queue, the phone displayed
    # for caller ID is the phone number specified in the queue. If you do not
    # specify a queue, the queue used will be the queue defined in the contact
    # flow.

    # To find the `QueueId`, open the queue you want to use in the Amazon Connect
    # Queue editor. The ID for the queue is displayed in the address bar as part
    # of the URL. For example, the queue ID is the set of characters at the end
    # of the URL, after 'queue/' such as
    # `queue/aeg40574-2d01-51c3-73d6-bf8624d2168c`.
    queue_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Specify a custom key-value pair using an attribute map. The attributes are
    # standard Amazon Connect attributes, and can be accessed in contact flows
    # just like any other contact attributes.

    # There can be up to 32,768 UTF-8 bytes across all key-value pairs. Attribute
    # keys can include only alphanumeric, dash, and underscore characters.

    # For example, if you want play a greeting when the customer answers the
    # call, you can pass the customer name in attributes similar to the
    # following:
    attributes: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class StartOutboundVoiceContactResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "contact_id",
                "ContactId",
                TypeInfo(str),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The unique identifier of this contact within your Amazon Connect instance.
    contact_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class StopContactRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "contact_id",
                "ContactId",
                TypeInfo(str),
            ),
            (
                "instance_id",
                "InstanceId",
                TypeInfo(str),
            ),
        ]

    # The unique identifier of the contact to end.
    contact_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The identifier for your Amazon Connect instance. To find the ID of your
    # instance, open the AWS console and select Amazon Connect. Select the alias
    # of the instance in the Instance alias column. The instance ID is displayed
    # in the Overview section of your instance settings. For example, the
    # instance ID is the set of characters at the end of the instance ARN, after
    # instance/, such as 10a4c4eb-f57e-4d4c-b602-bf39176ced07.
    instance_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class StopContactResponse(OutputShapeBase):
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
class ThrottlingException(ShapeBase):
    """
    The throttling limit has been exceeded.
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
class UpdateContactAttributesRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "initial_contact_id",
                "InitialContactId",
                TypeInfo(str),
            ),
            (
                "instance_id",
                "InstanceId",
                TypeInfo(str),
            ),
            (
                "attributes",
                "Attributes",
                TypeInfo(typing.Dict[str, str]),
            ),
        ]

    # The unique identifier of the contact for which to update attributes. This
    # is the identifier for the contact associated with the first interaction
    # with the contact center.
    initial_contact_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The identifier for your Amazon Connect instance. To find the ID of your
    # Amazon Connect instance, open the AWS console and select Amazon Connect.
    # Select the instance alias of the instance. The instance ID is displayed in
    # the Overview section of your instance settings. For example, the instance
    # ID is the set of characters at the end of the instance ARN, after
    # instance/, such as 10a4c4eb-f57e-4d4c-b602-bf39176ced07.
    instance_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The key-value pairs for the attribute to update.
    attributes: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class UpdateContactAttributesResponse(OutputShapeBase):
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
class UpdateUserHierarchyRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "user_id",
                "UserId",
                TypeInfo(str),
            ),
            (
                "instance_id",
                "InstanceId",
                TypeInfo(str),
            ),
            (
                "hierarchy_group_id",
                "HierarchyGroupId",
                TypeInfo(str),
            ),
        ]

    # The identifier of the user account to assign the hierarchy group to.
    user_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The identifier for your Amazon Connect instance. To find the ID of your
    # instance, open the AWS console and select Amazon Connect. Select the alias
    # of the instance in the Instance alias column. The instance ID is displayed
    # in the Overview section of your instance settings. For example, the
    # instance ID is the set of characters at the end of the instance ARN, after
    # instance/, such as 10a4c4eb-f57e-4d4c-b602-bf39176ced07.
    instance_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The identifier for the hierarchy group to assign to the user.
    hierarchy_group_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class UpdateUserIdentityInfoRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "identity_info",
                "IdentityInfo",
                TypeInfo(UserIdentityInfo),
            ),
            (
                "user_id",
                "UserId",
                TypeInfo(str),
            ),
            (
                "instance_id",
                "InstanceId",
                TypeInfo(str),
            ),
        ]

    # A `UserIdentityInfo` object.
    identity_info: "UserIdentityInfo" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The identifier for the user account to update identity information for.
    user_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The identifier for your Amazon Connect instance. To find the ID of your
    # instance, open the AWS console and select Amazon Connect. Select the alias
    # of the instance in the Instance alias column. The instance ID is displayed
    # in the Overview section of your instance settings. For example, the
    # instance ID is the set of characters at the end of the instance ARN, after
    # instance/, such as 10a4c4eb-f57e-4d4c-b602-bf39176ced07.
    instance_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class UpdateUserPhoneConfigRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "phone_config",
                "PhoneConfig",
                TypeInfo(UserPhoneConfig),
            ),
            (
                "user_id",
                "UserId",
                TypeInfo(str),
            ),
            (
                "instance_id",
                "InstanceId",
                TypeInfo(str),
            ),
        ]

    # A `UserPhoneConfig` object that contains settings for
    # `AfterContactWorkTimeLimit`, `AutoAccept`, `DeskPhoneNumber`, and
    # `PhoneType` to assign to the user.
    phone_config: "UserPhoneConfig" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The identifier for the user account to change phone settings for.
    user_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The identifier for your Amazon Connect instance. To find the ID of your
    # instance, open the AWS console and select Amazon Connect. Select the alias
    # of the instance in the Instance alias column. The instance ID is displayed
    # in the Overview section of your instance settings. For example, the
    # instance ID is the set of characters at the end of the instance ARN, after
    # instance/, such as 10a4c4eb-f57e-4d4c-b602-bf39176ced07.
    instance_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class UpdateUserRoutingProfileRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "routing_profile_id",
                "RoutingProfileId",
                TypeInfo(str),
            ),
            (
                "user_id",
                "UserId",
                TypeInfo(str),
            ),
            (
                "instance_id",
                "InstanceId",
                TypeInfo(str),
            ),
        ]

    # The identifier of the routing profile to assign to the user.
    routing_profile_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The identifier for the user account to assign the routing profile to.
    user_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The identifier for your Amazon Connect instance. To find the ID of your
    # instance, open the AWS console and select Amazon Connect. Select the alias
    # of the instance in the Instance alias column. The instance ID is displayed
    # in the Overview section of your instance settings. For example, the
    # instance ID is the set of characters at the end of the instance ARN, after
    # instance/, such as 10a4c4eb-f57e-4d4c-b602-bf39176ced07.
    instance_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class UpdateUserSecurityProfilesRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "security_profile_ids",
                "SecurityProfileIds",
                TypeInfo(typing.List[str]),
            ),
            (
                "user_id",
                "UserId",
                TypeInfo(str),
            ),
            (
                "instance_id",
                "InstanceId",
                TypeInfo(str),
            ),
        ]

    # The identifiers for the security profiles to assign to the user.
    security_profile_ids: typing.List[str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The identifier of the user account to assign the security profiles.
    user_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The identifier for your Amazon Connect instance. To find the ID of your
    # instance, open the AWS console and select Amazon Connect. Select the alias
    # of the instance in the Instance alias column. The instance ID is displayed
    # in the Overview section of your instance settings. For example, the
    # instance ID is the set of characters at the end of the instance ARN, after
    # instance/, such as 10a4c4eb-f57e-4d4c-b602-bf39176ced07.
    instance_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class User(ShapeBase):
    """
    A `User` object that contains information about a user account in your Amazon
    Connect instance, including configuration settings.
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
                "arn",
                "Arn",
                TypeInfo(str),
            ),
            (
                "username",
                "Username",
                TypeInfo(str),
            ),
            (
                "identity_info",
                "IdentityInfo",
                TypeInfo(UserIdentityInfo),
            ),
            (
                "phone_config",
                "PhoneConfig",
                TypeInfo(UserPhoneConfig),
            ),
            (
                "directory_user_id",
                "DirectoryUserId",
                TypeInfo(str),
            ),
            (
                "security_profile_ids",
                "SecurityProfileIds",
                TypeInfo(typing.List[str]),
            ),
            (
                "routing_profile_id",
                "RoutingProfileId",
                TypeInfo(str),
            ),
            (
                "hierarchy_group_id",
                "HierarchyGroupId",
                TypeInfo(str),
            ),
        ]

    # The identifier of the user account.
    id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The ARN of the user account.
    arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The user name assigned to the user account.
    username: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A `UserIdentityInfo` object.
    identity_info: "UserIdentityInfo" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A `UserPhoneConfig` object.
    phone_config: "UserPhoneConfig" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The directory Id for the user account in the existing directory used for
    # identity management.
    directory_user_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The identifier(s) for the security profile assigned to the user.
    security_profile_ids: typing.List[str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The identifier of the routing profile assigned to the user.
    routing_profile_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The identifier for the hierarchy group assigned to the user.
    hierarchy_group_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class UserIdentityInfo(ShapeBase):
    """
    A `UserIdentityInfo` object that contains information about the user's identity,
    including email address, first name, and last name.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "first_name",
                "FirstName",
                TypeInfo(str),
            ),
            (
                "last_name",
                "LastName",
                TypeInfo(str),
            ),
            (
                "email",
                "Email",
                TypeInfo(str),
            ),
        ]

    # The first name used in the user account. This is required if you are using
    # Amazon Connect or SAML for identity management.
    first_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The last name used in the user account. This is required if you are using
    # Amazon Connect or SAML for identity management.
    last_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The email address added to the user account. If you are using SAML for
    # identity management and include this parameter, an
    # `InvalidRequestException` is returned.
    email: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class UserNotFoundException(ShapeBase):
    """
    No user with the specified credentials was found in the Amazon Connect instance.
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
class UserPhoneConfig(ShapeBase):
    """
    A `UserPhoneConfig` object that contains information about the user phone
    configuration settings.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "phone_type",
                "PhoneType",
                TypeInfo(typing.Union[str, PhoneType]),
            ),
            (
                "auto_accept",
                "AutoAccept",
                TypeInfo(bool),
            ),
            (
                "after_contact_work_time_limit",
                "AfterContactWorkTimeLimit",
                TypeInfo(int),
            ),
            (
                "desk_phone_number",
                "DeskPhoneNumber",
                TypeInfo(str),
            ),
        ]

    # The phone type selected for the user, either Soft phone or Desk phone.
    phone_type: typing.Union[str, "PhoneType"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The Auto accept setting for the user, Yes or No.
    auto_accept: bool = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The After Call Work (ACW) timeout setting, in seconds, for the user.
    after_contact_work_time_limit: int = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The phone number for the user's desk phone.
    desk_phone_number: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class UserSummary(ShapeBase):
    """
    A `UserSummary` object that contains Information about a user, including ARN,
    Id, and user name.
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
                "arn",
                "Arn",
                TypeInfo(str),
            ),
            (
                "username",
                "Username",
                TypeInfo(str),
            ),
        ]

    # The identifier for the user account.
    id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The ARN for the user account.
    arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The Amazon Connect user name for the user account.
    username: str = dataclasses.field(default=ShapeBase.NOT_SET, )
