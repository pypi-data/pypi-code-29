import datetime
import typing
from autoboto import ShapeBase, OutputShapeBase, TypeInfo
import dataclasses


@dataclasses.dataclass
class BadRequestException(ShapeBase):
    """
    The target request is invalid.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class ConflictException(ShapeBase):
    """
    A conflict occurred.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class CreateEnvironmentEC2Request(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "name",
                "name",
                TypeInfo(str),
            ),
            (
                "instance_type",
                "instanceType",
                TypeInfo(str),
            ),
            (
                "description",
                "description",
                TypeInfo(str),
            ),
            (
                "client_request_token",
                "clientRequestToken",
                TypeInfo(str),
            ),
            (
                "subnet_id",
                "subnetId",
                TypeInfo(str),
            ),
            (
                "automatic_stop_time_minutes",
                "automaticStopTimeMinutes",
                TypeInfo(int),
            ),
            (
                "owner_arn",
                "ownerArn",
                TypeInfo(str),
            ),
        ]

    # The name of the environment to create.

    # This name is visible to other AWS IAM users in the same AWS account.
    name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The type of instance to connect to the environment (for example,
    # `t2.micro`).
    instance_type: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The description of the environment to create.
    description: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A unique, case-sensitive string that helps AWS Cloud9 to ensure this
    # operation completes no more than one time.

    # For more information, see [Client
    # Tokens](http://docs.aws.amazon.com/AWSEC2/latest/APIReference/Run_Instance_Idempotency.html)
    # in the _Amazon EC2 API Reference_.
    client_request_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The ID of the subnet in Amazon VPC that AWS Cloud9 will use to communicate
    # with the Amazon EC2 instance.
    subnet_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The number of minutes until the running instance is shut down after the
    # environment has last been used.
    automatic_stop_time_minutes: int = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The Amazon Resource Name (ARN) of the environment owner. This ARN can be
    # the ARN of any AWS IAM principal. If this value is not specified, the ARN
    # defaults to this environment's creator.
    owner_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class CreateEnvironmentEC2Result(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "environment_id",
                "environmentId",
                TypeInfo(str),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The ID of the environment that was created.
    environment_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class CreateEnvironmentMembershipRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "environment_id",
                "environmentId",
                TypeInfo(str),
            ),
            (
                "user_arn",
                "userArn",
                TypeInfo(str),
            ),
            (
                "permissions",
                "permissions",
                TypeInfo(typing.Union[str, MemberPermissions]),
            ),
        ]

    # The ID of the environment that contains the environment member you want to
    # add.
    environment_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The Amazon Resource Name (ARN) of the environment member you want to add.
    user_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The type of environment member permissions you want to associate with this
    # environment member. Available values include:

    #   * `read-only`: Has read-only access to the environment.

    #   * `read-write`: Has read-write access to the environment.
    permissions: typing.Union[str, "MemberPermissions"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class CreateEnvironmentMembershipResult(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "membership",
                "membership",
                TypeInfo(EnvironmentMember),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Information about the environment member that was added.
    membership: "EnvironmentMember" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class DeleteEnvironmentMembershipRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "environment_id",
                "environmentId",
                TypeInfo(str),
            ),
            (
                "user_arn",
                "userArn",
                TypeInfo(str),
            ),
        ]

    # The ID of the environment to delete the environment member from.
    environment_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The Amazon Resource Name (ARN) of the environment member to delete from the
    # environment.
    user_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DeleteEnvironmentMembershipResult(OutputShapeBase):
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
class DeleteEnvironmentRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "environment_id",
                "environmentId",
                TypeInfo(str),
            ),
        ]

    # The ID of the environment to delete.
    environment_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DeleteEnvironmentResult(OutputShapeBase):
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
class DescribeEnvironmentMembershipsRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "user_arn",
                "userArn",
                TypeInfo(str),
            ),
            (
                "environment_id",
                "environmentId",
                TypeInfo(str),
            ),
            (
                "permissions",
                "permissions",
                TypeInfo(typing.List[typing.Union[str, Permissions]]),
            ),
            (
                "next_token",
                "nextToken",
                TypeInfo(str),
            ),
            (
                "max_results",
                "maxResults",
                TypeInfo(int),
            ),
        ]

    # The Amazon Resource Name (ARN) of an individual environment member to get
    # information about. If no value is specified, information about all
    # environment members are returned.
    user_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The ID of the environment to get environment member information about.
    environment_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The type of environment member permissions to get information about.
    # Available values include:

    #   * `owner`: Owns the environment.

    #   * `read-only`: Has read-only access to the environment.

    #   * `read-write`: Has read-write access to the environment.

    # If no value is specified, information about all environment members are
    # returned.
    permissions: typing.List[typing.Union[str, "Permissions"]
                            ] = dataclasses.field(
                                default=ShapeBase.NOT_SET,
                            )

    # During a previous call, if there are more than 25 items in the list, only
    # the first 25 items are returned, along with a unique string called a _next
    # token_. To get the next batch of items in the list, call this operation
    # again, adding the next token to the call. To get all of the items in the
    # list, keep calling this operation with each subsequent next token that is
    # returned, until no more next tokens are returned.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The maximum number of environment members to get information about.
    max_results: int = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DescribeEnvironmentMembershipsResult(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "memberships",
                "memberships",
                TypeInfo(typing.List[EnvironmentMember]),
            ),
            (
                "next_token",
                "nextToken",
                TypeInfo(str),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Information about the environment members for the environment.
    memberships: typing.List["EnvironmentMember"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # If there are more than 25 items in the list, only the first 25 items are
    # returned, along with a unique string called a _next token_. To get the next
    # batch of items in the list, call this operation again, adding the next
    # token to the call.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    def paginate(
        self,
    ) -> typing.Generator["DescribeEnvironmentMembershipsResult", None, None]:
        yield from super()._paginate()


@dataclasses.dataclass
class DescribeEnvironmentStatusRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "environment_id",
                "environmentId",
                TypeInfo(str),
            ),
        ]

    # The ID of the environment to get status information about.
    environment_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DescribeEnvironmentStatusResult(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "status",
                "status",
                TypeInfo(typing.Union[str, EnvironmentStatus]),
            ),
            (
                "message",
                "message",
                TypeInfo(str),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The status of the environment. Available values include:

    #   * `connecting`: The environment is connecting.

    #   * `creating`: The environment is being created.

    #   * `deleting`: The environment is being deleted.

    #   * `error`: The environment is in an error state.

    #   * `ready`: The environment is ready.

    #   * `stopped`: The environment is stopped.

    #   * `stopping`: The environment is stopping.
    status: typing.Union[str, "EnvironmentStatus"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Any informational message about the status of the environment.
    message: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DescribeEnvironmentsRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "environment_ids",
                "environmentIds",
                TypeInfo(typing.List[str]),
            ),
        ]

    # The IDs of individual environments to get information about.
    environment_ids: typing.List[str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class DescribeEnvironmentsResult(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "environments",
                "environments",
                TypeInfo(typing.List[Environment]),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Information about the environments that are returned.
    environments: typing.List["Environment"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class Environment(ShapeBase):
    """
    Information about an AWS Cloud9 development environment.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "id",
                "id",
                TypeInfo(str),
            ),
            (
                "name",
                "name",
                TypeInfo(str),
            ),
            (
                "description",
                "description",
                TypeInfo(str),
            ),
            (
                "type",
                "type",
                TypeInfo(typing.Union[str, EnvironmentType]),
            ),
            (
                "arn",
                "arn",
                TypeInfo(str),
            ),
            (
                "owner_arn",
                "ownerArn",
                TypeInfo(str),
            ),
        ]

    # The ID of the environment.
    id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The name of the environment.
    name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The description for the environment.
    description: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The type of environment. Valid values include the following:

    #   * `ec2`: An Amazon Elastic Compute Cloud (Amazon EC2) instance connects to the environment.

    #   * `ssh`: Your own server connects to the environment.
    type: typing.Union[str, "EnvironmentType"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The Amazon Resource Name (ARN) of the environment.
    arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The Amazon Resource Name (ARN) of the environment owner.
    owner_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class EnvironmentMember(ShapeBase):
    """
    Information about an environment member for an AWS Cloud9 development
    environment.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "permissions",
                "permissions",
                TypeInfo(typing.Union[str, Permissions]),
            ),
            (
                "user_id",
                "userId",
                TypeInfo(str),
            ),
            (
                "user_arn",
                "userArn",
                TypeInfo(str),
            ),
            (
                "environment_id",
                "environmentId",
                TypeInfo(str),
            ),
            (
                "last_access",
                "lastAccess",
                TypeInfo(datetime.datetime),
            ),
        ]

    # The type of environment member permissions associated with this environment
    # member. Available values include:

    #   * `owner`: Owns the environment.

    #   * `read-only`: Has read-only access to the environment.

    #   * `read-write`: Has read-write access to the environment.
    permissions: typing.Union[str, "Permissions"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The user ID in AWS Identity and Access Management (AWS IAM) of the
    # environment member.
    user_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The Amazon Resource Name (ARN) of the environment member.
    user_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The ID of the environment for the environment member.
    environment_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The time, expressed in epoch time format, when the environment member last
    # opened the environment.
    last_access: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


class EnvironmentStatus(str):
    error = "error"
    creating = "creating"
    connecting = "connecting"
    ready = "ready"
    stopping = "stopping"
    stopped = "stopped"
    deleting = "deleting"


class EnvironmentType(str):
    ssh = "ssh"
    ec2 = "ec2"


@dataclasses.dataclass
class ForbiddenException(ShapeBase):
    """
    An access permissions issue occurred.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class InternalServerErrorException(ShapeBase):
    """
    An internal server error occurred.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class LimitExceededException(ShapeBase):
    """
    A service limit was exceeded.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class ListEnvironmentsRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "next_token",
                "nextToken",
                TypeInfo(str),
            ),
            (
                "max_results",
                "maxResults",
                TypeInfo(int),
            ),
        ]

    # During a previous call, if there are more than 25 items in the list, only
    # the first 25 items are returned, along with a unique string called a _next
    # token_. To get the next batch of items in the list, call this operation
    # again, adding the next token to the call. To get all of the items in the
    # list, keep calling this operation with each subsequent next token that is
    # returned, until no more next tokens are returned.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The maximum number of environments to get identifiers for.
    max_results: int = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ListEnvironmentsResult(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "next_token",
                "nextToken",
                TypeInfo(str),
            ),
            (
                "environment_ids",
                "environmentIds",
                TypeInfo(typing.List[str]),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # If there are more than 25 items in the list, only the first 25 items are
    # returned, along with a unique string called a _next token_. To get the next
    # batch of items in the list, call this operation again, adding the next
    # token to the call.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The list of environment identifiers.
    environment_ids: typing.List[str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    def paginate(self,
                ) -> typing.Generator["ListEnvironmentsResult", None, None]:
        yield from super()._paginate()


class MemberPermissions(str):
    read_write = "read-write"
    read_only = "read-only"


@dataclasses.dataclass
class NotFoundException(ShapeBase):
    """
    The target resource cannot be found.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


class Permissions(str):
    owner = "owner"
    read_write = "read-write"
    read_only = "read-only"


@dataclasses.dataclass
class TooManyRequestsException(ShapeBase):
    """
    Too many service requests were made over the given time period.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class UpdateEnvironmentMembershipRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "environment_id",
                "environmentId",
                TypeInfo(str),
            ),
            (
                "user_arn",
                "userArn",
                TypeInfo(str),
            ),
            (
                "permissions",
                "permissions",
                TypeInfo(typing.Union[str, MemberPermissions]),
            ),
        ]

    # The ID of the environment for the environment member whose settings you
    # want to change.
    environment_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The Amazon Resource Name (ARN) of the environment member whose settings you
    # want to change.
    user_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The replacement type of environment member permissions you want to
    # associate with this environment member. Available values include:

    #   * `read-only`: Has read-only access to the environment.

    #   * `read-write`: Has read-write access to the environment.
    permissions: typing.Union[str, "MemberPermissions"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class UpdateEnvironmentMembershipResult(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "membership",
                "membership",
                TypeInfo(EnvironmentMember),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Information about the environment member whose settings were changed.
    membership: "EnvironmentMember" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class UpdateEnvironmentRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "environment_id",
                "environmentId",
                TypeInfo(str),
            ),
            (
                "name",
                "name",
                TypeInfo(str),
            ),
            (
                "description",
                "description",
                TypeInfo(str),
            ),
        ]

    # The ID of the environment to change settings.
    environment_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A replacement name for the environment.
    name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Any new or replacement description for the environment.
    description: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class UpdateEnvironmentResult(OutputShapeBase):
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
