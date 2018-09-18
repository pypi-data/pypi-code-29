import datetime
import typing
from autoboto import ShapeBase, OutputShapeBase, TypeInfo
import dataclasses


@dataclasses.dataclass
class AcceptMatchInput(ShapeBase):
    """
    Represents the input for a request action.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "ticket_id",
                "TicketId",
                TypeInfo(str),
            ),
            (
                "player_ids",
                "PlayerIds",
                TypeInfo(typing.List[str]),
            ),
            (
                "acceptance_type",
                "AcceptanceType",
                TypeInfo(typing.Union[str, AcceptanceType]),
            ),
        ]

    # Unique identifier for a matchmaking ticket. The ticket must be in status
    # `REQUIRES_ACCEPTANCE`; otherwise this request will fail.
    ticket_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Unique identifier for a player delivering the response. This parameter can
    # include one or multiple player IDs.
    player_ids: typing.List[str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Player response to the proposed match.
    acceptance_type: typing.Union[str, "AcceptanceType"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class AcceptMatchOutput(OutputShapeBase):
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


class AcceptanceType(str):
    ACCEPT = "ACCEPT"
    REJECT = "REJECT"


@dataclasses.dataclass
class Alias(ShapeBase):
    """
    Properties describing a fleet alias.

    Alias-related operations include:

      * CreateAlias

      * ListAliases

      * DescribeAlias

      * UpdateAlias

      * DeleteAlias

      * ResolveAlias
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "alias_id",
                "AliasId",
                TypeInfo(str),
            ),
            (
                "name",
                "Name",
                TypeInfo(str),
            ),
            (
                "alias_arn",
                "AliasArn",
                TypeInfo(str),
            ),
            (
                "description",
                "Description",
                TypeInfo(str),
            ),
            (
                "routing_strategy",
                "RoutingStrategy",
                TypeInfo(RoutingStrategy),
            ),
            (
                "creation_time",
                "CreationTime",
                TypeInfo(datetime.datetime),
            ),
            (
                "last_updated_time",
                "LastUpdatedTime",
                TypeInfo(datetime.datetime),
            ),
        ]

    # Unique identifier for an alias; alias IDs are unique within a region.
    alias_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Descriptive label that is associated with an alias. Alias names do not need
    # to be unique.
    name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Unique identifier for an alias; alias ARNs are unique across all regions.
    alias_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Human-readable description of an alias.
    description: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Alias configuration for the alias, including routing type and settings.
    routing_strategy: "RoutingStrategy" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Time stamp indicating when this data object was created. Format is a number
    # expressed in Unix time as milliseconds (for example "1469498468.057").
    creation_time: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Time stamp indicating when this data object was last modified. Format is a
    # number expressed in Unix time as milliseconds (for example
    # "1469498468.057").
    last_updated_time: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class AttributeValue(ShapeBase):
    """
    Values for use in Player attribute key:value pairs. This object lets you specify
    an attribute value using any of the valid data types: string, number, string
    array or data map. Each `AttributeValue` object can use only one of the
    available properties.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "s",
                "S",
                TypeInfo(str),
            ),
            (
                "n",
                "N",
                TypeInfo(float),
            ),
            (
                "sl",
                "SL",
                TypeInfo(typing.List[str]),
            ),
            (
                "sdm",
                "SDM",
                TypeInfo(typing.Dict[str, float]),
            ),
        ]

    # For single string values. Maximum string length is 100 characters.
    s: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # For number values, expressed as double.
    n: float = dataclasses.field(default=ShapeBase.NOT_SET, )

    # For a list of up to 10 strings. Maximum length for each string is 100
    # characters. Duplicate values are not recognized; all occurrences of the
    # repeated value after the first of a repeated value are ignored.
    sl: typing.List[str] = dataclasses.field(default=ShapeBase.NOT_SET, )

    # For a map of up to 10 data type:value pairs. Maximum length for each string
    # value is 100 characters.
    sdm: typing.Dict[str, float] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class AwsCredentials(ShapeBase):
    """
    Temporary access credentials used for uploading game build files to Amazon
    GameLift. They are valid for a limited time. If they expire before you upload
    your game build, get a new set by calling RequestUploadCredentials.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "access_key_id",
                "AccessKeyId",
                TypeInfo(str),
            ),
            (
                "secret_access_key",
                "SecretAccessKey",
                TypeInfo(str),
            ),
            (
                "session_token",
                "SessionToken",
                TypeInfo(str),
            ),
        ]

    # Temporary key allowing access to the Amazon GameLift S3 account.
    access_key_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Temporary secret key allowing access to the Amazon GameLift S3 account.
    secret_access_key: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Token used to associate a specific build ID with the files uploaded using
    # these credentials.
    session_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class Build(ShapeBase):
    """
    Properties describing a game build.

    Build-related operations include:

      * CreateBuild

      * ListBuilds

      * DescribeBuild

      * UpdateBuild

      * DeleteBuild
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "build_id",
                "BuildId",
                TypeInfo(str),
            ),
            (
                "name",
                "Name",
                TypeInfo(str),
            ),
            (
                "version",
                "Version",
                TypeInfo(str),
            ),
            (
                "status",
                "Status",
                TypeInfo(typing.Union[str, BuildStatus]),
            ),
            (
                "size_on_disk",
                "SizeOnDisk",
                TypeInfo(int),
            ),
            (
                "operating_system",
                "OperatingSystem",
                TypeInfo(typing.Union[str, OperatingSystem]),
            ),
            (
                "creation_time",
                "CreationTime",
                TypeInfo(datetime.datetime),
            ),
        ]

    # Unique identifier for a build.
    build_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Descriptive label that is associated with a build. Build names do not need
    # to be unique. It can be set using CreateBuild or UpdateBuild.
    name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Version that is associated with this build. Version strings do not need to
    # be unique. This value can be set using CreateBuild or UpdateBuild.
    version: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Current status of the build.

    # Possible build statuses include the following:

    #   * **INITIALIZED** \-- A new build has been defined, but no files have been uploaded. You cannot create fleets for builds that are in this status. When a build is successfully created, the build status is set to this value.

    #   * **READY** \-- The game build has been successfully uploaded. You can now create new fleets for this build.

    #   * **FAILED** \-- The game build upload failed. You cannot create new fleets for this build.
    status: typing.Union[str, "BuildStatus"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # File size of the uploaded game build, expressed in bytes. When the build
    # status is `INITIALIZED`, this value is 0.
    size_on_disk: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Operating system that the game server binaries are built to run on. This
    # value determines the type of fleet resources that you can use for this
    # build.
    operating_system: typing.Union[str, "OperatingSystem"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Time stamp indicating when this data object was created. Format is a number
    # expressed in Unix time as milliseconds (for example "1469498468.057").
    creation_time: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


class BuildStatus(str):
    INITIALIZED = "INITIALIZED"
    READY = "READY"
    FAILED = "FAILED"


class ComparisonOperatorType(str):
    GreaterThanOrEqualToThreshold = "GreaterThanOrEqualToThreshold"
    GreaterThanThreshold = "GreaterThanThreshold"
    LessThanThreshold = "LessThanThreshold"
    LessThanOrEqualToThreshold = "LessThanOrEqualToThreshold"


@dataclasses.dataclass
class ConflictException(ShapeBase):
    """
    The requested operation would cause a conflict with the current state of a
    service resource associated with the request. Resolve the conflict before
    retrying this request.
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
class CreateAliasInput(ShapeBase):
    """
    Represents the input for a request action.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "name",
                "Name",
                TypeInfo(str),
            ),
            (
                "routing_strategy",
                "RoutingStrategy",
                TypeInfo(RoutingStrategy),
            ),
            (
                "description",
                "Description",
                TypeInfo(str),
            ),
        ]

    # Descriptive label that is associated with an alias. Alias names do not need
    # to be unique.
    name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Object that specifies the fleet and routing type to use for the alias.
    routing_strategy: "RoutingStrategy" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Human-readable description of an alias.
    description: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class CreateAliasOutput(OutputShapeBase):
    """
    Represents the returned data in response to a request action.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "alias",
                "Alias",
                TypeInfo(Alias),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Object that describes the newly created alias record.
    alias: "Alias" = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class CreateBuildInput(ShapeBase):
    """
    Represents the input for a request action.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "name",
                "Name",
                TypeInfo(str),
            ),
            (
                "version",
                "Version",
                TypeInfo(str),
            ),
            (
                "storage_location",
                "StorageLocation",
                TypeInfo(S3Location),
            ),
            (
                "operating_system",
                "OperatingSystem",
                TypeInfo(typing.Union[str, OperatingSystem]),
            ),
        ]

    # Descriptive label that is associated with a build. Build names do not need
    # to be unique. You can use UpdateBuild to change this value later.
    name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Version that is associated with this build. Version strings do not need to
    # be unique. You can use UpdateBuild to change this value later.
    version: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Information indicating where your game build files are stored. Use this
    # parameter only when creating a build with files stored in an Amazon S3
    # bucket that you own. The storage location must specify an Amazon S3 bucket
    # name and key, as well as a role ARN that you set up to allow Amazon
    # GameLift to access your Amazon S3 bucket. The S3 bucket must be in the same
    # region that you want to create a new build in.
    storage_location: "S3Location" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Operating system that the game server binaries are built to run on. This
    # value determines the type of fleet resources that you can use for this
    # build. If your game build contains multiple executables, they all must run
    # on the same operating system. If an operating system is not specified when
    # creating a build, Amazon GameLift uses the default value (WINDOWS_2012).
    # This value cannot be changed later.
    operating_system: typing.Union[str, "OperatingSystem"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class CreateBuildOutput(OutputShapeBase):
    """
    Represents the returned data in response to a request action.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "build",
                "Build",
                TypeInfo(Build),
            ),
            (
                "upload_credentials",
                "UploadCredentials",
                TypeInfo(AwsCredentials),
            ),
            (
                "storage_location",
                "StorageLocation",
                TypeInfo(S3Location),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The newly created build record, including a unique build ID and status.
    build: "Build" = dataclasses.field(default=ShapeBase.NOT_SET, )

    # This element is returned only when the operation is called without a
    # storage location. It contains credentials to use when you are uploading a
    # build file to an Amazon S3 bucket that is owned by Amazon GameLift.
    # Credentials have a limited life span. To refresh these credentials, call
    # RequestUploadCredentials.
    upload_credentials: "AwsCredentials" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Amazon S3 location for your game build file, including bucket name and key.
    storage_location: "S3Location" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class CreateFleetInput(ShapeBase):
    """
    Represents the input for a request action.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "name",
                "Name",
                TypeInfo(str),
            ),
            (
                "build_id",
                "BuildId",
                TypeInfo(str),
            ),
            (
                "ec2_instance_type",
                "EC2InstanceType",
                TypeInfo(typing.Union[str, EC2InstanceType]),
            ),
            (
                "description",
                "Description",
                TypeInfo(str),
            ),
            (
                "server_launch_path",
                "ServerLaunchPath",
                TypeInfo(str),
            ),
            (
                "server_launch_parameters",
                "ServerLaunchParameters",
                TypeInfo(str),
            ),
            (
                "log_paths",
                "LogPaths",
                TypeInfo(typing.List[str]),
            ),
            (
                "ec2_inbound_permissions",
                "EC2InboundPermissions",
                TypeInfo(typing.List[IpPermission]),
            ),
            (
                "new_game_session_protection_policy",
                "NewGameSessionProtectionPolicy",
                TypeInfo(typing.Union[str, ProtectionPolicy]),
            ),
            (
                "runtime_configuration",
                "RuntimeConfiguration",
                TypeInfo(RuntimeConfiguration),
            ),
            (
                "resource_creation_limit_policy",
                "ResourceCreationLimitPolicy",
                TypeInfo(ResourceCreationLimitPolicy),
            ),
            (
                "metric_groups",
                "MetricGroups",
                TypeInfo(typing.List[str]),
            ),
            (
                "peer_vpc_aws_account_id",
                "PeerVpcAwsAccountId",
                TypeInfo(str),
            ),
            (
                "peer_vpc_id",
                "PeerVpcId",
                TypeInfo(str),
            ),
            (
                "fleet_type",
                "FleetType",
                TypeInfo(typing.Union[str, FleetType]),
            ),
        ]

    # Descriptive label that is associated with a fleet. Fleet names do not need
    # to be unique.
    name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Unique identifier for a build to be deployed on the new fleet. The build
    # must have been successfully uploaded to Amazon GameLift and be in a `READY`
    # status. This fleet setting cannot be changed once the fleet is created.
    build_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Name of an EC2 instance type that is supported in Amazon GameLift. A fleet
    # instance type determines the computing resources of each instance in the
    # fleet, including CPU, memory, storage, and networking capacity. Amazon
    # GameLift supports the following EC2 instance types. See [Amazon EC2
    # Instance Types](http://aws.amazon.com/ec2/instance-types/) for detailed
    # descriptions.
    ec2_instance_type: typing.Union[str, "EC2InstanceType"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Human-readable description of a fleet.
    description: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # This parameter is no longer used. Instead, specify a server launch path
    # using the `RuntimeConfiguration` parameter. (Requests that specify a server
    # launch path and launch parameters instead of a run-time configuration will
    # continue to work.)
    server_launch_path: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # This parameter is no longer used. Instead, specify server launch parameters
    # in the `RuntimeConfiguration` parameter. (Requests that specify a server
    # launch path and launch parameters instead of a run-time configuration will
    # continue to work.)
    server_launch_parameters: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # This parameter is no longer used. Instead, to specify where Amazon GameLift
    # should store log files once a server process shuts down, use the Amazon
    # GameLift server API `ProcessReady()` and specify one or more directory
    # paths in `logParameters`. See more information in the [Server API
    # Reference](http://docs.aws.amazon.com/gamelift/latest/developerguide/gamelift-
    # sdk-server-api-ref.html#gamelift-sdk-server-api-ref-dataypes-process).
    log_paths: typing.List[str] = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Range of IP addresses and port settings that permit inbound traffic to
    # access server processes running on the fleet. If no inbound permissions are
    # set, including both IP address range and port range, the server processes
    # in the fleet cannot accept connections. You can specify one or more sets of
    # permissions for a fleet.
    ec2_inbound_permissions: typing.List["IpPermission"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Game session protection policy to apply to all instances in this fleet. If
    # this parameter is not set, instances in this fleet default to no
    # protection. You can change a fleet's protection policy using
    # UpdateFleetAttributes, but this change will only affect sessions created
    # after the policy change. You can also set protection for individual
    # instances using UpdateGameSession.

    #   * **NoProtection** \-- The game session can be terminated during a scale-down event.

    #   * **FullProtection** \-- If the game session is in an `ACTIVE` status, it cannot be terminated during a scale-down event.
    new_game_session_protection_policy: typing.Union[
        str, "ProtectionPolicy"] = dataclasses.field(
            default=ShapeBase.NOT_SET,
        )

    # Instructions for launching server processes on each instance in the fleet.
    # The run-time configuration for a fleet has a collection of server process
    # configurations, one for each type of server process to run on an instance.
    # A server process configuration specifies the location of the server
    # executable, launch parameters, and the number of concurrent processes with
    # that configuration to maintain on each instance. A CreateFleet request must
    # include a run-time configuration with at least one server process
    # configuration; otherwise the request fails with an invalid request
    # exception. (This parameter replaces the parameters `ServerLaunchPath` and
    # `ServerLaunchParameters`; requests that contain values for these parameters
    # instead of a run-time configuration will continue to work.)
    runtime_configuration: "RuntimeConfiguration" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Policy that limits the number of game sessions an individual player can
    # create over a span of time for this fleet.
    resource_creation_limit_policy: "ResourceCreationLimitPolicy" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Name of a metric group to add this fleet to. A metric group tracks metrics
    # across all fleets in the group. Use an existing metric group name to add
    # this fleet to the group, or use a new name to create a new metric group. A
    # fleet can only be included in one metric group at a time.
    metric_groups: typing.List[str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Unique identifier for the AWS account with the VPC that you want to peer
    # your Amazon GameLift fleet with. You can find your Account ID in the AWS
    # Management Console under account settings.
    peer_vpc_aws_account_id: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Unique identifier for a VPC with resources to be accessed by your Amazon
    # GameLift fleet. The VPC must be in the same region where your fleet is
    # deployed. To get VPC information, including IDs, use the Virtual Private
    # Cloud service tools, including the VPC Dashboard in the AWS Management
    # Console.
    peer_vpc_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Indicates whether to use on-demand instances or spot instances for this
    # fleet. If empty, the default is ON_DEMAND. Both categories of instances use
    # identical hardware and configurations, based on the instance type selected
    # for this fleet. You can acquire on-demand instances at any time for a fixed
    # price and keep them as long as you need them. Spot instances have lower
    # prices, but spot pricing is variable, and while in use they can be
    # interrupted (with a two-minute notification). Learn more about Amazon
    # GameLift spot instances with at [ Choose Computing
    # Resources](http://docs.aws.amazon.com/gamelift/latest/developerguide/gamelift-
    # ec2-instances.html).
    fleet_type: typing.Union[str, "FleetType"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class CreateFleetOutput(OutputShapeBase):
    """
    Represents the returned data in response to a request action.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "fleet_attributes",
                "FleetAttributes",
                TypeInfo(FleetAttributes),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Properties for the newly created fleet.
    fleet_attributes: "FleetAttributes" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class CreateGameSessionInput(ShapeBase):
    """
    Represents the input for a request action.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "maximum_player_session_count",
                "MaximumPlayerSessionCount",
                TypeInfo(int),
            ),
            (
                "fleet_id",
                "FleetId",
                TypeInfo(str),
            ),
            (
                "alias_id",
                "AliasId",
                TypeInfo(str),
            ),
            (
                "name",
                "Name",
                TypeInfo(str),
            ),
            (
                "game_properties",
                "GameProperties",
                TypeInfo(typing.List[GameProperty]),
            ),
            (
                "creator_id",
                "CreatorId",
                TypeInfo(str),
            ),
            (
                "game_session_id",
                "GameSessionId",
                TypeInfo(str),
            ),
            (
                "idempotency_token",
                "IdempotencyToken",
                TypeInfo(str),
            ),
            (
                "game_session_data",
                "GameSessionData",
                TypeInfo(str),
            ),
        ]

    # Maximum number of players that can be connected simultaneously to the game
    # session.
    maximum_player_session_count: int = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Unique identifier for a fleet to create a game session in. Each request
    # must reference either a fleet ID or alias ID, but not both.
    fleet_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Unique identifier for an alias associated with the fleet to create a game
    # session in. Each request must reference either a fleet ID or alias ID, but
    # not both.
    alias_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Descriptive label that is associated with a game session. Session names do
    # not need to be unique.
    name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Set of custom properties for a game session, formatted as key:value pairs.
    # These properties are passed to a game server process in the GameSession
    # object with a request to start a new game session (see [Start a Game
    # Session](http://docs.aws.amazon.com/gamelift/latest/developerguide/gamelift-
    # sdk-server-api.html#gamelift-sdk-server-startsession)).
    game_properties: typing.List["GameProperty"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Unique identifier for a player or entity creating the game session. This ID
    # is used to enforce a resource protection policy (if one exists) that limits
    # the number of concurrent active game sessions one player can have.
    creator_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # _This parameter is no longer preferred. Please use`IdempotencyToken`
    # instead._ Custom string that uniquely identifies a request for a new game
    # session. Maximum token length is 48 characters. If provided, this string is
    # included in the new game session's ID. (A game session ARN has the
    # following format: `arn:aws:gamelift:<region>::gamesession/<fleet
    # ID>/<custom ID string or idempotency token>`.)
    game_session_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Custom string that uniquely identifies a request for a new game session.
    # Maximum token length is 48 characters. If provided, this string is included
    # in the new game session's ID. (A game session ARN has the following format:
    # `arn:aws:gamelift:<region>::gamesession/<fleet ID>/<custom ID string or
    # idempotency token>`.) Idempotency tokens remain in use for 30 days after a
    # game session has ended; game session objects are retained for this time
    # period and then deleted.
    idempotency_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Set of custom game session properties, formatted as a single string value.
    # This data is passed to a game server process in the GameSession object with
    # a request to start a new game session (see [Start a Game
    # Session](http://docs.aws.amazon.com/gamelift/latest/developerguide/gamelift-
    # sdk-server-api.html#gamelift-sdk-server-startsession)).
    game_session_data: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class CreateGameSessionOutput(OutputShapeBase):
    """
    Represents the returned data in response to a request action.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "game_session",
                "GameSession",
                TypeInfo(GameSession),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Object that describes the newly created game session record.
    game_session: "GameSession" = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class CreateGameSessionQueueInput(ShapeBase):
    """
    Represents the input for a request action.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "name",
                "Name",
                TypeInfo(str),
            ),
            (
                "timeout_in_seconds",
                "TimeoutInSeconds",
                TypeInfo(int),
            ),
            (
                "player_latency_policies",
                "PlayerLatencyPolicies",
                TypeInfo(typing.List[PlayerLatencyPolicy]),
            ),
            (
                "destinations",
                "Destinations",
                TypeInfo(typing.List[GameSessionQueueDestination]),
            ),
        ]

    # Descriptive label that is associated with game session queue. Queue names
    # must be unique within each region.
    name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Maximum time, in seconds, that a new game session placement request remains
    # in the queue. When a request exceeds this time, the game session placement
    # changes to a `TIMED_OUT` status.
    timeout_in_seconds: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Collection of latency policies to apply when processing game sessions
    # placement requests with player latency information. Multiple policies are
    # evaluated in order of the maximum latency value, starting with the lowest
    # latency values. With just one policy, it is enforced at the start of the
    # game session placement for the duration period. With multiple policies,
    # each policy is enforced consecutively for its duration period. For example,
    # a queue might enforce a 60-second policy followed by a 120-second policy,
    # and then no policy for the remainder of the placement. A player latency
    # policy must set a value for MaximumIndividualPlayerLatencyMilliseconds; if
    # none is set, this API requests will fail.
    player_latency_policies: typing.List["PlayerLatencyPolicy"
                                        ] = dataclasses.field(
                                            default=ShapeBase.NOT_SET,
                                        )

    # List of fleets that can be used to fulfill game session placement requests
    # in the queue. Fleets are identified by either a fleet ARN or a fleet alias
    # ARN. Destinations are listed in default preference order.
    destinations: typing.List["GameSessionQueueDestination"
                             ] = dataclasses.field(
                                 default=ShapeBase.NOT_SET,
                             )


@dataclasses.dataclass
class CreateGameSessionQueueOutput(OutputShapeBase):
    """
    Represents the returned data in response to a request action.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "game_session_queue",
                "GameSessionQueue",
                TypeInfo(GameSessionQueue),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Object that describes the newly created game session queue.
    game_session_queue: "GameSessionQueue" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class CreateMatchmakingConfigurationInput(ShapeBase):
    """
    Represents the input for a request action.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "name",
                "Name",
                TypeInfo(str),
            ),
            (
                "game_session_queue_arns",
                "GameSessionQueueArns",
                TypeInfo(typing.List[str]),
            ),
            (
                "request_timeout_seconds",
                "RequestTimeoutSeconds",
                TypeInfo(int),
            ),
            (
                "acceptance_required",
                "AcceptanceRequired",
                TypeInfo(bool),
            ),
            (
                "rule_set_name",
                "RuleSetName",
                TypeInfo(str),
            ),
            (
                "description",
                "Description",
                TypeInfo(str),
            ),
            (
                "acceptance_timeout_seconds",
                "AcceptanceTimeoutSeconds",
                TypeInfo(int),
            ),
            (
                "notification_target",
                "NotificationTarget",
                TypeInfo(str),
            ),
            (
                "additional_player_count",
                "AdditionalPlayerCount",
                TypeInfo(int),
            ),
            (
                "custom_event_data",
                "CustomEventData",
                TypeInfo(str),
            ),
            (
                "game_properties",
                "GameProperties",
                TypeInfo(typing.List[GameProperty]),
            ),
            (
                "game_session_data",
                "GameSessionData",
                TypeInfo(str),
            ),
        ]

    # Unique identifier for a matchmaking configuration. This name is used to
    # identify the configuration associated with a matchmaking request or ticket.
    name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Amazon Resource Name
    # ([ARN](http://docs.aws.amazon.com/AmazonS3/latest/dev/s3-arn-format.html))
    # that is assigned to a game session queue and uniquely identifies it. Format
    # is
    # `arn:aws:gamelift:<region>::fleet/fleet-a1234567-b8c9-0d1e-2fa3-b45c6d7e8912`.
    # These queues are used when placing game sessions for matches that are
    # created with this matchmaking configuration. Queues can be located in any
    # region.
    game_session_queue_arns: typing.List[str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Maximum duration, in seconds, that a matchmaking ticket can remain in
    # process before timing out. Requests that time out can be resubmitted as
    # needed.
    request_timeout_seconds: int = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Flag that determines whether or not a match that was created with this
    # configuration must be accepted by the matched players. To require
    # acceptance, set to TRUE.
    acceptance_required: bool = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Unique identifier for a matchmaking rule set to use with this
    # configuration. A matchmaking configuration can only use rule sets that are
    # defined in the same region.
    rule_set_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Meaningful description of the matchmaking configuration.
    description: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Length of time (in seconds) to wait for players to accept a proposed match.
    # If any player rejects the match or fails to accept before the timeout, the
    # ticket continues to look for an acceptable match.
    acceptance_timeout_seconds: int = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # SNS topic ARN that is set up to receive matchmaking notifications.
    notification_target: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Number of player slots in a match to keep open for future players. For
    # example, if the configuration's rule set specifies a match for a single
    # 12-person team, and the additional player count is set to 2, only 10
    # players are selected for the match.
    additional_player_count: int = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Information to attached to all events related to the matchmaking
    # configuration.
    custom_event_data: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Set of custom properties for a game session, formatted as key:value pairs.
    # These properties are passed to a game server process in the GameSession
    # object with a request to start a new game session (see [Start a Game
    # Session](http://docs.aws.amazon.com/gamelift/latest/developerguide/gamelift-
    # sdk-server-api.html#gamelift-sdk-server-startsession)). This information is
    # added to the new GameSession object that is created for a successful match.
    game_properties: typing.List["GameProperty"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Set of custom game session properties, formatted as a single string value.
    # This data is passed to a game server process in the GameSession object with
    # a request to start a new game session (see [Start a Game
    # Session](http://docs.aws.amazon.com/gamelift/latest/developerguide/gamelift-
    # sdk-server-api.html#gamelift-sdk-server-startsession)). This information is
    # added to the new GameSession object that is created for a successful match.
    game_session_data: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class CreateMatchmakingConfigurationOutput(OutputShapeBase):
    """
    Represents the returned data in response to a request action.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "configuration",
                "Configuration",
                TypeInfo(MatchmakingConfiguration),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Object that describes the newly created matchmaking configuration.
    configuration: "MatchmakingConfiguration" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class CreateMatchmakingRuleSetInput(ShapeBase):
    """
    Represents the input for a request action.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "name",
                "Name",
                TypeInfo(str),
            ),
            (
                "rule_set_body",
                "RuleSetBody",
                TypeInfo(str),
            ),
        ]

    # Unique identifier for a matchmaking rule set. This name is used to identify
    # the rule set associated with a matchmaking configuration.
    name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Collection of matchmaking rules, formatted as a JSON string. (Note that
    # comments are not allowed in JSON, but most elements support a description
    # field.)
    rule_set_body: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class CreateMatchmakingRuleSetOutput(OutputShapeBase):
    """
    Represents the returned data in response to a request action.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "rule_set",
                "RuleSet",
                TypeInfo(MatchmakingRuleSet),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Object that describes the newly created matchmaking rule set.
    rule_set: "MatchmakingRuleSet" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class CreatePlayerSessionInput(ShapeBase):
    """
    Represents the input for a request action.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "game_session_id",
                "GameSessionId",
                TypeInfo(str),
            ),
            (
                "player_id",
                "PlayerId",
                TypeInfo(str),
            ),
            (
                "player_data",
                "PlayerData",
                TypeInfo(str),
            ),
        ]

    # Unique identifier for the game session to add a player to.
    game_session_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Unique identifier for a player. Player IDs are developer-defined.
    player_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Developer-defined information related to a player. Amazon GameLift does not
    # use this data, so it can be formatted as needed for use in the game.
    player_data: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class CreatePlayerSessionOutput(OutputShapeBase):
    """
    Represents the returned data in response to a request action.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "player_session",
                "PlayerSession",
                TypeInfo(PlayerSession),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Object that describes the newly created player session record.
    player_session: "PlayerSession" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class CreatePlayerSessionsInput(ShapeBase):
    """
    Represents the input for a request action.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "game_session_id",
                "GameSessionId",
                TypeInfo(str),
            ),
            (
                "player_ids",
                "PlayerIds",
                TypeInfo(typing.List[str]),
            ),
            (
                "player_data_map",
                "PlayerDataMap",
                TypeInfo(typing.Dict[str, str]),
            ),
        ]

    # Unique identifier for the game session to add players to.
    game_session_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # List of unique identifiers for the players to be added.
    player_ids: typing.List[str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Map of string pairs, each specifying a player ID and a set of developer-
    # defined information related to the player. Amazon GameLift does not use
    # this data, so it can be formatted as needed for use in the game. Player
    # data strings for player IDs not included in the `PlayerIds` parameter are
    # ignored.
    player_data_map: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class CreatePlayerSessionsOutput(OutputShapeBase):
    """
    Represents the returned data in response to a request action.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "player_sessions",
                "PlayerSessions",
                TypeInfo(typing.List[PlayerSession]),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Collection of player session objects created for the added players.
    player_sessions: typing.List["PlayerSession"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class CreateVpcPeeringAuthorizationInput(ShapeBase):
    """
    Represents the input for a request action.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "game_lift_aws_account_id",
                "GameLiftAwsAccountId",
                TypeInfo(str),
            ),
            (
                "peer_vpc_id",
                "PeerVpcId",
                TypeInfo(str),
            ),
        ]

    # Unique identifier for the AWS account that you use to manage your Amazon
    # GameLift fleet. You can find your Account ID in the AWS Management Console
    # under account settings.
    game_lift_aws_account_id: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Unique identifier for a VPC with resources to be accessed by your Amazon
    # GameLift fleet. The VPC must be in the same region where your fleet is
    # deployed. To get VPC information, including IDs, use the Virtual Private
    # Cloud service tools, including the VPC Dashboard in the AWS Management
    # Console.
    peer_vpc_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class CreateVpcPeeringAuthorizationOutput(OutputShapeBase):
    """
    Represents the returned data in response to a request action.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "vpc_peering_authorization",
                "VpcPeeringAuthorization",
                TypeInfo(VpcPeeringAuthorization),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Details on the requested VPC peering authorization, including expiration.
    vpc_peering_authorization: "VpcPeeringAuthorization" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class CreateVpcPeeringConnectionInput(ShapeBase):
    """
    Represents the input for a request action.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "fleet_id",
                "FleetId",
                TypeInfo(str),
            ),
            (
                "peer_vpc_aws_account_id",
                "PeerVpcAwsAccountId",
                TypeInfo(str),
            ),
            (
                "peer_vpc_id",
                "PeerVpcId",
                TypeInfo(str),
            ),
        ]

    # Unique identifier for a fleet. This tells Amazon GameLift which GameLift
    # VPC to peer with.
    fleet_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Unique identifier for the AWS account with the VPC that you want to peer
    # your Amazon GameLift fleet with. You can find your Account ID in the AWS
    # Management Console under account settings.
    peer_vpc_aws_account_id: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Unique identifier for a VPC with resources to be accessed by your Amazon
    # GameLift fleet. The VPC must be in the same region where your fleet is
    # deployed. To get VPC information, including IDs, use the Virtual Private
    # Cloud service tools, including the VPC Dashboard in the AWS Management
    # Console.
    peer_vpc_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class CreateVpcPeeringConnectionOutput(OutputShapeBase):
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
class DeleteAliasInput(ShapeBase):
    """
    Represents the input for a request action.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "alias_id",
                "AliasId",
                TypeInfo(str),
            ),
        ]

    # Unique identifier for a fleet alias. Specify the alias you want to delete.
    alias_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DeleteBuildInput(ShapeBase):
    """
    Represents the input for a request action.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "build_id",
                "BuildId",
                TypeInfo(str),
            ),
        ]

    # Unique identifier for a build to delete.
    build_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DeleteFleetInput(ShapeBase):
    """
    Represents the input for a request action.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "fleet_id",
                "FleetId",
                TypeInfo(str),
            ),
        ]

    # Unique identifier for a fleet to be deleted.
    fleet_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DeleteGameSessionQueueInput(ShapeBase):
    """
    Represents the input for a request action.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "name",
                "Name",
                TypeInfo(str),
            ),
        ]

    # Descriptive label that is associated with game session queue. Queue names
    # must be unique within each region.
    name: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DeleteGameSessionQueueOutput(OutputShapeBase):
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
class DeleteMatchmakingConfigurationInput(ShapeBase):
    """
    Represents the input for a request action.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "name",
                "Name",
                TypeInfo(str),
            ),
        ]

    # Unique identifier for a matchmaking configuration
    name: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DeleteMatchmakingConfigurationOutput(OutputShapeBase):
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
class DeleteScalingPolicyInput(ShapeBase):
    """
    Represents the input for a request action.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "name",
                "Name",
                TypeInfo(str),
            ),
            (
                "fleet_id",
                "FleetId",
                TypeInfo(str),
            ),
        ]

    # Descriptive label that is associated with a scaling policy. Policy names do
    # not need to be unique.
    name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Unique identifier for a fleet to be deleted.
    fleet_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DeleteVpcPeeringAuthorizationInput(ShapeBase):
    """
    Represents the input for a request action.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "game_lift_aws_account_id",
                "GameLiftAwsAccountId",
                TypeInfo(str),
            ),
            (
                "peer_vpc_id",
                "PeerVpcId",
                TypeInfo(str),
            ),
        ]

    # Unique identifier for the AWS account that you use to manage your Amazon
    # GameLift fleet. You can find your Account ID in the AWS Management Console
    # under account settings.
    game_lift_aws_account_id: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Unique identifier for a VPC with resources to be accessed by your Amazon
    # GameLift fleet. The VPC must be in the same region where your fleet is
    # deployed. To get VPC information, including IDs, use the Virtual Private
    # Cloud service tools, including the VPC Dashboard in the AWS Management
    # Console.
    peer_vpc_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DeleteVpcPeeringAuthorizationOutput(OutputShapeBase):
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
class DeleteVpcPeeringConnectionInput(ShapeBase):
    """
    Represents the input for a request action.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "fleet_id",
                "FleetId",
                TypeInfo(str),
            ),
            (
                "vpc_peering_connection_id",
                "VpcPeeringConnectionId",
                TypeInfo(str),
            ),
        ]

    # Unique identifier for a fleet. This value must match the fleet ID
    # referenced in the VPC peering connection record.
    fleet_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Unique identifier for a VPC peering connection. This value is included in
    # the VpcPeeringConnection object, which can be retrieved by calling
    # DescribeVpcPeeringConnections.
    vpc_peering_connection_id: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class DeleteVpcPeeringConnectionOutput(OutputShapeBase):
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
class DescribeAliasInput(ShapeBase):
    """
    Represents the input for a request action.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "alias_id",
                "AliasId",
                TypeInfo(str),
            ),
        ]

    # Unique identifier for a fleet alias. Specify the alias you want to
    # retrieve.
    alias_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DescribeAliasOutput(OutputShapeBase):
    """
    Represents the returned data in response to a request action.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "alias",
                "Alias",
                TypeInfo(Alias),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Object that contains the requested alias.
    alias: "Alias" = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DescribeBuildInput(ShapeBase):
    """
    Represents the input for a request action.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "build_id",
                "BuildId",
                TypeInfo(str),
            ),
        ]

    # Unique identifier for a build to retrieve properties for.
    build_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DescribeBuildOutput(OutputShapeBase):
    """
    Represents the returned data in response to a request action.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "build",
                "Build",
                TypeInfo(Build),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Set of properties describing the requested build.
    build: "Build" = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DescribeEC2InstanceLimitsInput(ShapeBase):
    """
    Represents the input for a request action.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "ec2_instance_type",
                "EC2InstanceType",
                TypeInfo(typing.Union[str, EC2InstanceType]),
            ),
        ]

    # Name of an EC2 instance type that is supported in Amazon GameLift. A fleet
    # instance type determines the computing resources of each instance in the
    # fleet, including CPU, memory, storage, and networking capacity. Amazon
    # GameLift supports the following EC2 instance types. See [Amazon EC2
    # Instance Types](http://aws.amazon.com/ec2/instance-types/) for detailed
    # descriptions. Leave this parameter blank to retrieve limits for all types.
    ec2_instance_type: typing.Union[str, "EC2InstanceType"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class DescribeEC2InstanceLimitsOutput(OutputShapeBase):
    """
    Represents the returned data in response to a request action.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "ec2_instance_limits",
                "EC2InstanceLimits",
                TypeInfo(typing.List[EC2InstanceLimit]),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Object that contains the maximum number of instances for the specified
    # instance type.
    ec2_instance_limits: typing.List["EC2InstanceLimit"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class DescribeFleetAttributesInput(ShapeBase):
    """
    Represents the input for a request action.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "fleet_ids",
                "FleetIds",
                TypeInfo(typing.List[str]),
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

    # Unique identifier for a fleet(s) to retrieve attributes for. To request
    # attributes for all fleets, leave this parameter empty.
    fleet_ids: typing.List[str] = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Maximum number of results to return. Use this parameter with `NextToken` to
    # get results as a set of sequential pages. This parameter is ignored when
    # the request specifies one or a list of fleet IDs.
    limit: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Token that indicates the start of the next sequential page of results. Use
    # the token that is returned with a previous call to this action. To start at
    # the beginning of the result set, do not specify a value. This parameter is
    # ignored when the request specifies one or a list of fleet IDs.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DescribeFleetAttributesOutput(OutputShapeBase):
    """
    Represents the returned data in response to a request action.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "fleet_attributes",
                "FleetAttributes",
                TypeInfo(typing.List[FleetAttributes]),
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

    # Collection of objects containing attribute metadata for each requested
    # fleet ID.
    fleet_attributes: typing.List["FleetAttributes"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Token that indicates where to resume retrieving results on the next call to
    # this action. If no token is returned, these results represent the end of
    # the list.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DescribeFleetCapacityInput(ShapeBase):
    """
    Represents the input for a request action.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "fleet_ids",
                "FleetIds",
                TypeInfo(typing.List[str]),
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

    # Unique identifier for a fleet(s) to retrieve capacity information for. To
    # request capacity information for all fleets, leave this parameter empty.
    fleet_ids: typing.List[str] = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Maximum number of results to return. Use this parameter with `NextToken` to
    # get results as a set of sequential pages. This parameter is ignored when
    # the request specifies one or a list of fleet IDs.
    limit: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Token that indicates the start of the next sequential page of results. Use
    # the token that is returned with a previous call to this action. To start at
    # the beginning of the result set, do not specify a value. This parameter is
    # ignored when the request specifies one or a list of fleet IDs.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DescribeFleetCapacityOutput(OutputShapeBase):
    """
    Represents the returned data in response to a request action.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "fleet_capacity",
                "FleetCapacity",
                TypeInfo(typing.List[FleetCapacity]),
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

    # Collection of objects containing capacity information for each requested
    # fleet ID. Leave this parameter empty to retrieve capacity information for
    # all fleets.
    fleet_capacity: typing.List["FleetCapacity"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Token that indicates where to resume retrieving results on the next call to
    # this action. If no token is returned, these results represent the end of
    # the list.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DescribeFleetEventsInput(ShapeBase):
    """
    Represents the input for a request action.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "fleet_id",
                "FleetId",
                TypeInfo(str),
            ),
            (
                "start_time",
                "StartTime",
                TypeInfo(datetime.datetime),
            ),
            (
                "end_time",
                "EndTime",
                TypeInfo(datetime.datetime),
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

    # Unique identifier for a fleet to get event logs for.
    fleet_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Earliest date to retrieve event logs for. If no start time is specified,
    # this call returns entries starting from when the fleet was created to the
    # specified end time. Format is a number expressed in Unix time as
    # milliseconds (ex: "1469498468.057").
    start_time: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Most recent date to retrieve event logs for. If no end time is specified,
    # this call returns entries from the specified start time up to the present.
    # Format is a number expressed in Unix time as milliseconds (ex:
    # "1469498468.057").
    end_time: datetime.datetime = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Maximum number of results to return. Use this parameter with `NextToken` to
    # get results as a set of sequential pages.
    limit: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Token that indicates the start of the next sequential page of results. Use
    # the token that is returned with a previous call to this action. To start at
    # the beginning of the result set, do not specify a value.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DescribeFleetEventsOutput(OutputShapeBase):
    """
    Represents the returned data in response to a request action.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "events",
                "Events",
                TypeInfo(typing.List[Event]),
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

    # Collection of objects containing event log entries for the specified fleet.
    events: typing.List["Event"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Token that indicates where to resume retrieving results on the next call to
    # this action. If no token is returned, these results represent the end of
    # the list.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DescribeFleetPortSettingsInput(ShapeBase):
    """
    Represents the input for a request action.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "fleet_id",
                "FleetId",
                TypeInfo(str),
            ),
        ]

    # Unique identifier for a fleet to retrieve port settings for.
    fleet_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DescribeFleetPortSettingsOutput(OutputShapeBase):
    """
    Represents the returned data in response to a request action.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "inbound_permissions",
                "InboundPermissions",
                TypeInfo(typing.List[IpPermission]),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Object that contains port settings for the requested fleet ID.
    inbound_permissions: typing.List["IpPermission"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class DescribeFleetUtilizationInput(ShapeBase):
    """
    Represents the input for a request action.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "fleet_ids",
                "FleetIds",
                TypeInfo(typing.List[str]),
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

    # Unique identifier for a fleet(s) to retrieve utilization data for. To
    # request utilization data for all fleets, leave this parameter empty.
    fleet_ids: typing.List[str] = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Maximum number of results to return. Use this parameter with `NextToken` to
    # get results as a set of sequential pages. This parameter is ignored when
    # the request specifies one or a list of fleet IDs.
    limit: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Token that indicates the start of the next sequential page of results. Use
    # the token that is returned with a previous call to this action. To start at
    # the beginning of the result set, do not specify a value. This parameter is
    # ignored when the request specifies one or a list of fleet IDs.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DescribeFleetUtilizationOutput(OutputShapeBase):
    """
    Represents the returned data in response to a request action.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "fleet_utilization",
                "FleetUtilization",
                TypeInfo(typing.List[FleetUtilization]),
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

    # Collection of objects containing utilization information for each requested
    # fleet ID.
    fleet_utilization: typing.List["FleetUtilization"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Token that indicates where to resume retrieving results on the next call to
    # this action. If no token is returned, these results represent the end of
    # the list.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DescribeGameSessionDetailsInput(ShapeBase):
    """
    Represents the input for a request action.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "fleet_id",
                "FleetId",
                TypeInfo(str),
            ),
            (
                "game_session_id",
                "GameSessionId",
                TypeInfo(str),
            ),
            (
                "alias_id",
                "AliasId",
                TypeInfo(str),
            ),
            (
                "status_filter",
                "StatusFilter",
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

    # Unique identifier for a fleet to retrieve all game sessions active on the
    # fleet.
    fleet_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Unique identifier for the game session to retrieve.
    game_session_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Unique identifier for an alias associated with the fleet to retrieve all
    # game sessions for.
    alias_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Game session status to filter results on. Possible game session statuses
    # include `ACTIVE`, `TERMINATED`, `ACTIVATING` and `TERMINATING` (the last
    # two are transitory).
    status_filter: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Maximum number of results to return. Use this parameter with `NextToken` to
    # get results as a set of sequential pages.
    limit: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Token that indicates the start of the next sequential page of results. Use
    # the token that is returned with a previous call to this action. To start at
    # the beginning of the result set, do not specify a value.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DescribeGameSessionDetailsOutput(OutputShapeBase):
    """
    Represents the returned data in response to a request action.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "game_session_details",
                "GameSessionDetails",
                TypeInfo(typing.List[GameSessionDetail]),
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

    # Collection of objects containing game session properties and the protection
    # policy currently in force for each session matching the request.
    game_session_details: typing.List["GameSessionDetail"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Token that indicates where to resume retrieving results on the next call to
    # this action. If no token is returned, these results represent the end of
    # the list.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DescribeGameSessionPlacementInput(ShapeBase):
    """
    Represents the input for a request action.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "placement_id",
                "PlacementId",
                TypeInfo(str),
            ),
        ]

    # Unique identifier for a game session placement to retrieve.
    placement_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DescribeGameSessionPlacementOutput(OutputShapeBase):
    """
    Represents the returned data in response to a request action.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "game_session_placement",
                "GameSessionPlacement",
                TypeInfo(GameSessionPlacement),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Object that describes the requested game session placement.
    game_session_placement: "GameSessionPlacement" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class DescribeGameSessionQueuesInput(ShapeBase):
    """
    Represents the input for a request action.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "names",
                "Names",
                TypeInfo(typing.List[str]),
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

    # List of queue names to retrieve information for. To request settings for
    # all queues, leave this parameter empty.
    names: typing.List[str] = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Maximum number of results to return. Use this parameter with `NextToken` to
    # get results as a set of sequential pages.
    limit: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Token that indicates the start of the next sequential page of results. Use
    # the token that is returned with a previous call to this action. To start at
    # the beginning of the result set, do not specify a value.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DescribeGameSessionQueuesOutput(OutputShapeBase):
    """
    Represents the returned data in response to a request action.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "game_session_queues",
                "GameSessionQueues",
                TypeInfo(typing.List[GameSessionQueue]),
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

    # Collection of objects that describes the requested game session queues.
    game_session_queues: typing.List["GameSessionQueue"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Token that indicates where to resume retrieving results on the next call to
    # this action. If no token is returned, these results represent the end of
    # the list.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DescribeGameSessionsInput(ShapeBase):
    """
    Represents the input for a request action.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "fleet_id",
                "FleetId",
                TypeInfo(str),
            ),
            (
                "game_session_id",
                "GameSessionId",
                TypeInfo(str),
            ),
            (
                "alias_id",
                "AliasId",
                TypeInfo(str),
            ),
            (
                "status_filter",
                "StatusFilter",
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

    # Unique identifier for a fleet to retrieve all game sessions for.
    fleet_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Unique identifier for the game session to retrieve. You can use either a
    # `GameSessionId` or `GameSessionArn` value.
    game_session_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Unique identifier for an alias associated with the fleet to retrieve all
    # game sessions for.
    alias_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Game session status to filter results on. Possible game session statuses
    # include `ACTIVE`, `TERMINATED`, `ACTIVATING`, and `TERMINATING` (the last
    # two are transitory).
    status_filter: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Maximum number of results to return. Use this parameter with `NextToken` to
    # get results as a set of sequential pages.
    limit: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Token that indicates the start of the next sequential page of results. Use
    # the token that is returned with a previous call to this action. To start at
    # the beginning of the result set, do not specify a value.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DescribeGameSessionsOutput(OutputShapeBase):
    """
    Represents the returned data in response to a request action.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "game_sessions",
                "GameSessions",
                TypeInfo(typing.List[GameSession]),
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

    # Collection of objects containing game session properties for each session
    # matching the request.
    game_sessions: typing.List["GameSession"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Token that indicates where to resume retrieving results on the next call to
    # this action. If no token is returned, these results represent the end of
    # the list.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DescribeInstancesInput(ShapeBase):
    """
    Represents the input for a request action.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "fleet_id",
                "FleetId",
                TypeInfo(str),
            ),
            (
                "instance_id",
                "InstanceId",
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

    # Unique identifier for a fleet to retrieve instance information for.
    fleet_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Unique identifier for an instance to retrieve. Specify an instance ID or
    # leave blank to retrieve all instances in the fleet.
    instance_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Maximum number of results to return. Use this parameter with `NextToken` to
    # get results as a set of sequential pages.
    limit: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Token that indicates the start of the next sequential page of results. Use
    # the token that is returned with a previous call to this action. To start at
    # the beginning of the result set, do not specify a value.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DescribeInstancesOutput(OutputShapeBase):
    """
    Represents the returned data in response to a request action.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "instances",
                "Instances",
                TypeInfo(typing.List[Instance]),
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

    # Collection of objects containing properties for each instance returned.
    instances: typing.List["Instance"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Token that indicates where to resume retrieving results on the next call to
    # this action. If no token is returned, these results represent the end of
    # the list.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DescribeMatchmakingConfigurationsInput(ShapeBase):
    """
    Represents the input for a request action.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "names",
                "Names",
                TypeInfo(typing.List[str]),
            ),
            (
                "rule_set_name",
                "RuleSetName",
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

    # Unique identifier for a matchmaking configuration(s) to retrieve. To
    # request all existing configurations, leave this parameter empty.
    names: typing.List[str] = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Unique identifier for a matchmaking rule set. Use this parameter to
    # retrieve all matchmaking configurations that use this rule set.
    rule_set_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Maximum number of results to return. Use this parameter with `NextToken` to
    # get results as a set of sequential pages. This parameter is limited to 10.
    limit: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Token that indicates the start of the next sequential page of results. Use
    # the token that is returned with a previous call to this action. To start at
    # the beginning of the result set, do not specify a value.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DescribeMatchmakingConfigurationsOutput(OutputShapeBase):
    """
    Represents the returned data in response to a request action.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "configurations",
                "Configurations",
                TypeInfo(typing.List[MatchmakingConfiguration]),
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

    # Collection of requested matchmaking configuration objects.
    configurations: typing.List["MatchmakingConfiguration"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Token that indicates where to resume retrieving results on the next call to
    # this action. If no token is returned, these results represent the end of
    # the list.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DescribeMatchmakingInput(ShapeBase):
    """
    Represents the input for a request action.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "ticket_ids",
                "TicketIds",
                TypeInfo(typing.List[str]),
            ),
        ]

    # Unique identifier for a matchmaking ticket. You can include up to 10 ID
    # values.
    ticket_ids: typing.List[str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class DescribeMatchmakingOutput(OutputShapeBase):
    """
    Represents the returned data in response to a request action.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "ticket_list",
                "TicketList",
                TypeInfo(typing.List[MatchmakingTicket]),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Collection of existing matchmaking ticket objects matching the request.
    ticket_list: typing.List["MatchmakingTicket"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class DescribeMatchmakingRuleSetsInput(ShapeBase):
    """
    Represents the input for a request action.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "names",
                "Names",
                TypeInfo(typing.List[str]),
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

    # Unique identifier for a matchmaking rule set. This name is used to identify
    # the rule set associated with a matchmaking configuration.
    names: typing.List[str] = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Maximum number of results to return. Use this parameter with `NextToken` to
    # get results as a set of sequential pages.
    limit: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Token that indicates the start of the next sequential page of results. Use
    # the token that is returned with a previous call to this action. To start at
    # the beginning of the result set, do not specify a value.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DescribeMatchmakingRuleSetsOutput(OutputShapeBase):
    """
    Represents the returned data in response to a request action.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "rule_sets",
                "RuleSets",
                TypeInfo(typing.List[MatchmakingRuleSet]),
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

    # Collection of requested matchmaking rule set objects.
    rule_sets: typing.List["MatchmakingRuleSet"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Token that indicates where to resume retrieving results on the next call to
    # this action. If no token is returned, these results represent the end of
    # the list.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DescribePlayerSessionsInput(ShapeBase):
    """
    Represents the input for a request action.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "game_session_id",
                "GameSessionId",
                TypeInfo(str),
            ),
            (
                "player_id",
                "PlayerId",
                TypeInfo(str),
            ),
            (
                "player_session_id",
                "PlayerSessionId",
                TypeInfo(str),
            ),
            (
                "player_session_status_filter",
                "PlayerSessionStatusFilter",
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

    # Unique identifier for the game session to retrieve player sessions for.
    game_session_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Unique identifier for a player to retrieve player sessions for.
    player_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Unique identifier for a player session to retrieve.
    player_session_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Player session status to filter results on.

    # Possible player session statuses include the following:

    #   * **RESERVED** \-- The player session request has been received, but the player has not yet connected to the server process and/or been validated.

    #   * **ACTIVE** \-- The player has been validated by the server process and is currently connected.

    #   * **COMPLETED** \-- The player connection has been dropped.

    #   * **TIMEDOUT** \-- A player session request was received, but the player did not connect and/or was not validated within the timeout limit (60 seconds).
    player_session_status_filter: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Maximum number of results to return. Use this parameter with `NextToken` to
    # get results as a set of sequential pages. If a player session ID is
    # specified, this parameter is ignored.
    limit: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Token that indicates the start of the next sequential page of results. Use
    # the token that is returned with a previous call to this action. To start at
    # the beginning of the result set, do not specify a value. If a player
    # session ID is specified, this parameter is ignored.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DescribePlayerSessionsOutput(OutputShapeBase):
    """
    Represents the returned data in response to a request action.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "player_sessions",
                "PlayerSessions",
                TypeInfo(typing.List[PlayerSession]),
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

    # Collection of objects containing properties for each player session that
    # matches the request.
    player_sessions: typing.List["PlayerSession"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Token that indicates where to resume retrieving results on the next call to
    # this action. If no token is returned, these results represent the end of
    # the list.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DescribeRuntimeConfigurationInput(ShapeBase):
    """
    Represents the input for a request action.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "fleet_id",
                "FleetId",
                TypeInfo(str),
            ),
        ]

    # Unique identifier for a fleet to get the run-time configuration for.
    fleet_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DescribeRuntimeConfigurationOutput(OutputShapeBase):
    """
    Represents the returned data in response to a request action.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "runtime_configuration",
                "RuntimeConfiguration",
                TypeInfo(RuntimeConfiguration),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Instructions describing how server processes should be launched and
    # maintained on each instance in the fleet.
    runtime_configuration: "RuntimeConfiguration" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class DescribeScalingPoliciesInput(ShapeBase):
    """
    Represents the input for a request action.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "fleet_id",
                "FleetId",
                TypeInfo(str),
            ),
            (
                "status_filter",
                "StatusFilter",
                TypeInfo(typing.Union[str, ScalingStatusType]),
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

    # Unique identifier for a fleet to retrieve scaling policies for.
    fleet_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Scaling policy status to filter results on. A scaling policy is only in
    # force when in an `ACTIVE` status.

    #   * **ACTIVE** \-- The scaling policy is currently in force.

    #   * **UPDATEREQUESTED** \-- A request to update the scaling policy has been received.

    #   * **UPDATING** \-- A change is being made to the scaling policy.

    #   * **DELETEREQUESTED** \-- A request to delete the scaling policy has been received.

    #   * **DELETING** \-- The scaling policy is being deleted.

    #   * **DELETED** \-- The scaling policy has been deleted.

    #   * **ERROR** \-- An error occurred in creating the policy. It should be removed and recreated.
    status_filter: typing.Union[str, "ScalingStatusType"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Maximum number of results to return. Use this parameter with `NextToken` to
    # get results as a set of sequential pages.
    limit: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Token that indicates the start of the next sequential page of results. Use
    # the token that is returned with a previous call to this action. To start at
    # the beginning of the result set, do not specify a value.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DescribeScalingPoliciesOutput(OutputShapeBase):
    """
    Represents the returned data in response to a request action.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "scaling_policies",
                "ScalingPolicies",
                TypeInfo(typing.List[ScalingPolicy]),
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

    # Collection of objects containing the scaling policies matching the request.
    scaling_policies: typing.List["ScalingPolicy"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Token that indicates where to resume retrieving results on the next call to
    # this action. If no token is returned, these results represent the end of
    # the list.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DescribeVpcPeeringAuthorizationsInput(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class DescribeVpcPeeringAuthorizationsOutput(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "vpc_peering_authorizations",
                "VpcPeeringAuthorizations",
                TypeInfo(typing.List[VpcPeeringAuthorization]),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Collection of objects that describe all valid VPC peering operations for
    # the current AWS account.
    vpc_peering_authorizations: typing.List["VpcPeeringAuthorization"
                                           ] = dataclasses.field(
                                               default=ShapeBase.NOT_SET,
                                           )


@dataclasses.dataclass
class DescribeVpcPeeringConnectionsInput(ShapeBase):
    """
    Represents the input for a request action.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "fleet_id",
                "FleetId",
                TypeInfo(str),
            ),
        ]

    # Unique identifier for a fleet.
    fleet_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DescribeVpcPeeringConnectionsOutput(OutputShapeBase):
    """
    Represents the returned data in response to a request action.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "vpc_peering_connections",
                "VpcPeeringConnections",
                TypeInfo(typing.List[VpcPeeringConnection]),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Collection of VPC peering connection records that match the request.
    vpc_peering_connections: typing.List["VpcPeeringConnection"
                                        ] = dataclasses.field(
                                            default=ShapeBase.NOT_SET,
                                        )


@dataclasses.dataclass
class DesiredPlayerSession(ShapeBase):
    """
    Player information for use when creating player sessions using a game session
    placement request with StartGameSessionPlacement.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "player_id",
                "PlayerId",
                TypeInfo(str),
            ),
            (
                "player_data",
                "PlayerData",
                TypeInfo(str),
            ),
        ]

    # Unique identifier for a player to associate with the player session.
    player_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Developer-defined information related to a player. Amazon GameLift does not
    # use this data, so it can be formatted as needed for use in the game.
    player_data: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class EC2InstanceCounts(ShapeBase):
    """
    Current status of fleet capacity. The number of active instances should match or
    be in the process of matching the number of desired instances. Pending and
    terminating counts are non-zero only if fleet capacity is adjusting to an
    UpdateFleetCapacity request, or if access to resources is temporarily affected.

    Fleet-related operations include:

      * CreateFleet

      * ListFleets

      * DeleteFleet

      * Describe fleets:

        * DescribeFleetAttributes

        * DescribeFleetCapacity

        * DescribeFleetPortSettings

        * DescribeFleetUtilization

        * DescribeRuntimeConfiguration

        * DescribeEC2InstanceLimits

        * DescribeFleetEvents

      * Update fleets:

        * UpdateFleetAttributes

        * UpdateFleetCapacity

        * UpdateFleetPortSettings

        * UpdateRuntimeConfiguration

      * Manage fleet actions:

        * StartFleetActions

        * StopFleetActions
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "desired",
                "DESIRED",
                TypeInfo(int),
            ),
            (
                "minimum",
                "MINIMUM",
                TypeInfo(int),
            ),
            (
                "maximum",
                "MAXIMUM",
                TypeInfo(int),
            ),
            (
                "pending",
                "PENDING",
                TypeInfo(int),
            ),
            (
                "active",
                "ACTIVE",
                TypeInfo(int),
            ),
            (
                "idle",
                "IDLE",
                TypeInfo(int),
            ),
            (
                "terminating",
                "TERMINATING",
                TypeInfo(int),
            ),
        ]

    # Ideal number of active instances in the fleet.
    desired: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Minimum value allowed for the fleet's instance count.
    minimum: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Maximum value allowed for the fleet's instance count.
    maximum: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Number of instances in the fleet that are starting but not yet active.
    pending: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Actual number of active instances in the fleet.
    active: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Number of active instances in the fleet that are not currently hosting a
    # game session.
    idle: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Number of instances in the fleet that are no longer active but haven't yet
    # been terminated.
    terminating: int = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class EC2InstanceLimit(ShapeBase):
    """
    Maximum number of instances allowed based on the Amazon Elastic Compute Cloud
    (Amazon EC2) instance type. Instance limits can be retrieved by calling
    DescribeEC2InstanceLimits.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "ec2_instance_type",
                "EC2InstanceType",
                TypeInfo(typing.Union[str, EC2InstanceType]),
            ),
            (
                "current_instances",
                "CurrentInstances",
                TypeInfo(int),
            ),
            (
                "instance_limit",
                "InstanceLimit",
                TypeInfo(int),
            ),
        ]

    # Name of an EC2 instance type that is supported in Amazon GameLift. A fleet
    # instance type determines the computing resources of each instance in the
    # fleet, including CPU, memory, storage, and networking capacity. Amazon
    # GameLift supports the following EC2 instance types. See [Amazon EC2
    # Instance Types](http://aws.amazon.com/ec2/instance-types/) for detailed
    # descriptions.
    ec2_instance_type: typing.Union[str, "EC2InstanceType"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Number of instances of the specified type that are currently in use by this
    # AWS account.
    current_instances: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Number of instances allowed.
    instance_limit: int = dataclasses.field(default=ShapeBase.NOT_SET, )


class EC2InstanceType(str):
    t2_micro = "t2.micro"
    t2_small = "t2.small"
    t2_medium = "t2.medium"
    t2_large = "t2.large"
    c3_large = "c3.large"
    c3_xlarge = "c3.xlarge"
    c3_2xlarge = "c3.2xlarge"
    c3_4xlarge = "c3.4xlarge"
    c3_8xlarge = "c3.8xlarge"
    c4_large = "c4.large"
    c4_xlarge = "c4.xlarge"
    c4_2xlarge = "c4.2xlarge"
    c4_4xlarge = "c4.4xlarge"
    c4_8xlarge = "c4.8xlarge"
    r3_large = "r3.large"
    r3_xlarge = "r3.xlarge"
    r3_2xlarge = "r3.2xlarge"
    r3_4xlarge = "r3.4xlarge"
    r3_8xlarge = "r3.8xlarge"
    r4_large = "r4.large"
    r4_xlarge = "r4.xlarge"
    r4_2xlarge = "r4.2xlarge"
    r4_4xlarge = "r4.4xlarge"
    r4_8xlarge = "r4.8xlarge"
    r4_16xlarge = "r4.16xlarge"
    m3_medium = "m3.medium"
    m3_large = "m3.large"
    m3_xlarge = "m3.xlarge"
    m3_2xlarge = "m3.2xlarge"
    m4_large = "m4.large"
    m4_xlarge = "m4.xlarge"
    m4_2xlarge = "m4.2xlarge"
    m4_4xlarge = "m4.4xlarge"
    m4_10xlarge = "m4.10xlarge"


@dataclasses.dataclass
class Event(ShapeBase):
    """
    Log entry describing an event that involves Amazon GameLift resources (such as a
    fleet). In addition to tracking activity, event codes and messages can provide
    additional information for troubleshooting and debugging problems.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "event_id",
                "EventId",
                TypeInfo(str),
            ),
            (
                "resource_id",
                "ResourceId",
                TypeInfo(str),
            ),
            (
                "event_code",
                "EventCode",
                TypeInfo(typing.Union[str, EventCode]),
            ),
            (
                "message",
                "Message",
                TypeInfo(str),
            ),
            (
                "event_time",
                "EventTime",
                TypeInfo(datetime.datetime),
            ),
            (
                "pre_signed_log_url",
                "PreSignedLogUrl",
                TypeInfo(str),
            ),
        ]

    # Unique identifier for a fleet event.
    event_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Unique identifier for an event resource, such as a fleet ID.
    resource_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Type of event being logged. The following events are currently in use:

    # **Fleet creation events:**

    #   * FLEET_CREATED -- A fleet record was successfully created with a status of `NEW`. Event messaging includes the fleet ID.

    #   * FLEET_STATE_DOWNLOADING -- Fleet status changed from `NEW` to `DOWNLOADING`. The compressed build has started downloading to a fleet instance for installation.

    #   * FLEET_BINARY_DOWNLOAD_FAILED -- The build failed to download to the fleet instance.

    #   * FLEET_CREATION_EXTRACTING_BUILD – The game server build was successfully downloaded to an instance, and the build files are now being extracted from the uploaded build and saved to an instance. Failure at this stage prevents a fleet from moving to `ACTIVE` status. Logs for this stage display a list of the files that are extracted and saved on the instance. Access the logs by using the URL in _PreSignedLogUrl_.

    #   * FLEET_CREATION_RUNNING_INSTALLER – The game server build files were successfully extracted, and the Amazon GameLift is now running the build's install script (if one is included). Failure in this stage prevents a fleet from moving to `ACTIVE` status. Logs for this stage list the installation steps and whether or not the install completed successfully. Access the logs by using the URL in _PreSignedLogUrl_.

    #   * FLEET_CREATION_VALIDATING_RUNTIME_CONFIG -- The build process was successful, and the Amazon GameLift is now verifying that the game server launch paths, which are specified in the fleet's run-time configuration, exist. If any listed launch path exists, Amazon GameLift tries to launch a game server process and waits for the process to report ready. Failures in this stage prevent a fleet from moving to `ACTIVE` status. Logs for this stage list the launch paths in the run-time configuration and indicate whether each is found. Access the logs by using the URL in _PreSignedLogUrl_.

    #   * FLEET_STATE_VALIDATING -- Fleet status changed from `DOWNLOADING` to `VALIDATING`.

    #   * FLEET_VALIDATION_LAUNCH_PATH_NOT_FOUND -- Validation of the run-time configuration failed because the executable specified in a launch path does not exist on the instance.

    #   * FLEET_STATE_BUILDING -- Fleet status changed from `VALIDATING` to `BUILDING`.

    #   * FLEET_VALIDATION_EXECUTABLE_RUNTIME_FAILURE -- Validation of the run-time configuration failed because the executable specified in a launch path failed to run on the fleet instance.

    #   * FLEET_STATE_ACTIVATING -- Fleet status changed from `BUILDING` to `ACTIVATING`.

    #   * FLEET_ACTIVATION_FAILED - The fleet failed to successfully complete one of the steps in the fleet activation process. This event code indicates that the game build was successfully downloaded to a fleet instance, built, and validated, but was not able to start a server process. A possible reason for failure is that the game server is not reporting "process ready" to the Amazon GameLift service.

    #   * FLEET_STATE_ACTIVE -- The fleet's status changed from `ACTIVATING` to `ACTIVE`. The fleet is now ready to host game sessions.

    # **VPC peering events:**

    #   * FLEET_VPC_PEERING_SUCCEEDED -- A VPC peering connection has been established between the VPC for an Amazon GameLift fleet and a VPC in your AWS account.

    #   * FLEET_VPC_PEERING_FAILED -- A requested VPC peering connection has failed. Event details and status information (see DescribeVpcPeeringConnections) provide additional detail. A common reason for peering failure is that the two VPCs have overlapping CIDR blocks of IPv4 addresses. To resolve this, change the CIDR block for the VPC in your AWS account. For more information on VPC peering failures, see <http://docs.aws.amazon.com/AmazonVPC/latest/PeeringGuide/invalid-peering-configurations.html>

    #   * FLEET_VPC_PEERING_DELETED -- A VPC peering connection has been successfully deleted.

    # **Spot instance events:**

    #   * INSTANCE_INTERRUPTED -- A spot instance was interrupted by EC2 with a two-minute notification.

    # **Other fleet events:**

    #   * FLEET_SCALING_EVENT -- A change was made to the fleet's capacity settings (desired instances, minimum/maximum scaling limits). Event messaging includes the new capacity settings.

    #   * FLEET_NEW_GAME_SESSION_PROTECTION_POLICY_UPDATED -- A change was made to the fleet's game session protection policy setting. Event messaging includes both the old and new policy setting.

    #   * FLEET_DELETED -- A request to delete a fleet was initiated.

    #   * GENERIC_EVENT -- An unspecified event has occurred.
    event_code: typing.Union[str, "EventCode"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Additional information related to the event.
    message: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Time stamp indicating when this event occurred. Format is a number
    # expressed in Unix time as milliseconds (for example "1469498468.057").
    event_time: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Location of stored logs with additional detail that is related to the
    # event. This is useful for debugging issues. The URL is valid for 15
    # minutes. You can also access fleet creation logs through the Amazon
    # GameLift console.
    pre_signed_log_url: str = dataclasses.field(default=ShapeBase.NOT_SET, )


class EventCode(str):
    GENERIC_EVENT = "GENERIC_EVENT"
    FLEET_CREATED = "FLEET_CREATED"
    FLEET_DELETED = "FLEET_DELETED"
    FLEET_SCALING_EVENT = "FLEET_SCALING_EVENT"
    FLEET_STATE_DOWNLOADING = "FLEET_STATE_DOWNLOADING"
    FLEET_STATE_VALIDATING = "FLEET_STATE_VALIDATING"
    FLEET_STATE_BUILDING = "FLEET_STATE_BUILDING"
    FLEET_STATE_ACTIVATING = "FLEET_STATE_ACTIVATING"
    FLEET_STATE_ACTIVE = "FLEET_STATE_ACTIVE"
    FLEET_STATE_ERROR = "FLEET_STATE_ERROR"
    FLEET_INITIALIZATION_FAILED = "FLEET_INITIALIZATION_FAILED"
    FLEET_BINARY_DOWNLOAD_FAILED = "FLEET_BINARY_DOWNLOAD_FAILED"
    FLEET_VALIDATION_LAUNCH_PATH_NOT_FOUND = "FLEET_VALIDATION_LAUNCH_PATH_NOT_FOUND"
    FLEET_VALIDATION_EXECUTABLE_RUNTIME_FAILURE = "FLEET_VALIDATION_EXECUTABLE_RUNTIME_FAILURE"
    FLEET_VALIDATION_TIMED_OUT = "FLEET_VALIDATION_TIMED_OUT"
    FLEET_ACTIVATION_FAILED = "FLEET_ACTIVATION_FAILED"
    FLEET_ACTIVATION_FAILED_NO_INSTANCES = "FLEET_ACTIVATION_FAILED_NO_INSTANCES"
    FLEET_NEW_GAME_SESSION_PROTECTION_POLICY_UPDATED = "FLEET_NEW_GAME_SESSION_PROTECTION_POLICY_UPDATED"
    SERVER_PROCESS_INVALID_PATH = "SERVER_PROCESS_INVALID_PATH"
    SERVER_PROCESS_SDK_INITIALIZATION_TIMEOUT = "SERVER_PROCESS_SDK_INITIALIZATION_TIMEOUT"
    SERVER_PROCESS_PROCESS_READY_TIMEOUT = "SERVER_PROCESS_PROCESS_READY_TIMEOUT"
    SERVER_PROCESS_CRASHED = "SERVER_PROCESS_CRASHED"
    SERVER_PROCESS_TERMINATED_UNHEALTHY = "SERVER_PROCESS_TERMINATED_UNHEALTHY"
    SERVER_PROCESS_FORCE_TERMINATED = "SERVER_PROCESS_FORCE_TERMINATED"
    SERVER_PROCESS_PROCESS_EXIT_TIMEOUT = "SERVER_PROCESS_PROCESS_EXIT_TIMEOUT"
    GAME_SESSION_ACTIVATION_TIMEOUT = "GAME_SESSION_ACTIVATION_TIMEOUT"
    FLEET_CREATION_EXTRACTING_BUILD = "FLEET_CREATION_EXTRACTING_BUILD"
    FLEET_CREATION_RUNNING_INSTALLER = "FLEET_CREATION_RUNNING_INSTALLER"
    FLEET_CREATION_VALIDATING_RUNTIME_CONFIG = "FLEET_CREATION_VALIDATING_RUNTIME_CONFIG"
    FLEET_VPC_PEERING_SUCCEEDED = "FLEET_VPC_PEERING_SUCCEEDED"
    FLEET_VPC_PEERING_FAILED = "FLEET_VPC_PEERING_FAILED"
    FLEET_VPC_PEERING_DELETED = "FLEET_VPC_PEERING_DELETED"
    INSTANCE_INTERRUPTED = "INSTANCE_INTERRUPTED"


class FleetAction(str):
    AUTO_SCALING = "AUTO_SCALING"


@dataclasses.dataclass
class FleetAttributes(ShapeBase):
    """
    General properties describing a fleet.

    Fleet-related operations include:

      * CreateFleet

      * ListFleets

      * DeleteFleet

      * Describe fleets:

        * DescribeFleetAttributes

        * DescribeFleetCapacity

        * DescribeFleetPortSettings

        * DescribeFleetUtilization

        * DescribeRuntimeConfiguration

        * DescribeEC2InstanceLimits

        * DescribeFleetEvents

      * Update fleets:

        * UpdateFleetAttributes

        * UpdateFleetCapacity

        * UpdateFleetPortSettings

        * UpdateRuntimeConfiguration

      * Manage fleet actions:

        * StartFleetActions

        * StopFleetActions
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "fleet_id",
                "FleetId",
                TypeInfo(str),
            ),
            (
                "fleet_arn",
                "FleetArn",
                TypeInfo(str),
            ),
            (
                "fleet_type",
                "FleetType",
                TypeInfo(typing.Union[str, FleetType]),
            ),
            (
                "instance_type",
                "InstanceType",
                TypeInfo(typing.Union[str, EC2InstanceType]),
            ),
            (
                "description",
                "Description",
                TypeInfo(str),
            ),
            (
                "name",
                "Name",
                TypeInfo(str),
            ),
            (
                "creation_time",
                "CreationTime",
                TypeInfo(datetime.datetime),
            ),
            (
                "termination_time",
                "TerminationTime",
                TypeInfo(datetime.datetime),
            ),
            (
                "status",
                "Status",
                TypeInfo(typing.Union[str, FleetStatus]),
            ),
            (
                "build_id",
                "BuildId",
                TypeInfo(str),
            ),
            (
                "server_launch_path",
                "ServerLaunchPath",
                TypeInfo(str),
            ),
            (
                "server_launch_parameters",
                "ServerLaunchParameters",
                TypeInfo(str),
            ),
            (
                "log_paths",
                "LogPaths",
                TypeInfo(typing.List[str]),
            ),
            (
                "new_game_session_protection_policy",
                "NewGameSessionProtectionPolicy",
                TypeInfo(typing.Union[str, ProtectionPolicy]),
            ),
            (
                "operating_system",
                "OperatingSystem",
                TypeInfo(typing.Union[str, OperatingSystem]),
            ),
            (
                "resource_creation_limit_policy",
                "ResourceCreationLimitPolicy",
                TypeInfo(ResourceCreationLimitPolicy),
            ),
            (
                "metric_groups",
                "MetricGroups",
                TypeInfo(typing.List[str]),
            ),
            (
                "stopped_actions",
                "StoppedActions",
                TypeInfo(typing.List[typing.Union[str, FleetAction]]),
            ),
        ]

    # Unique identifier for a fleet.
    fleet_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Identifier for a fleet that is unique across all regions.
    fleet_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Indicates whether the fleet uses on-demand or spot instances. A spot
    # instance in use may be interrupted with a two-minute notification.
    fleet_type: typing.Union[str, "FleetType"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # EC2 instance type indicating the computing resources of each instance in
    # the fleet, including CPU, memory, storage, and networking capacity. See
    # [Amazon EC2 Instance Types](http://aws.amazon.com/ec2/instance-types/) for
    # detailed descriptions.
    instance_type: typing.Union[str, "EC2InstanceType"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Human-readable description of the fleet.
    description: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Descriptive label that is associated with a fleet. Fleet names do not need
    # to be unique.
    name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Time stamp indicating when this data object was created. Format is a number
    # expressed in Unix time as milliseconds (for example "1469498468.057").
    creation_time: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Time stamp indicating when this data object was terminated. Format is a
    # number expressed in Unix time as milliseconds (for example
    # "1469498468.057").
    termination_time: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Current status of the fleet.

    # Possible fleet statuses include the following:

    #   * **NEW** \-- A new fleet has been defined and desired instances is set to 1.

    #   * **DOWNLOADING/VALIDATING/BUILDING/ACTIVATING** \-- Amazon GameLift is setting up the new fleet, creating new instances with the game build and starting server processes.

    #   * **ACTIVE** \-- Hosts can now accept game sessions.

    #   * **ERROR** \-- An error occurred when downloading, validating, building, or activating the fleet.

    #   * **DELETING** \-- Hosts are responding to a delete fleet request.

    #   * **TERMINATED** \-- The fleet no longer exists.
    status: typing.Union[str, "FleetStatus"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Unique identifier for a build.
    build_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Path to a game server executable in the fleet's build, specified for fleets
    # created before 2016-08-04 (or AWS SDK v. 0.12.16). Server launch paths for
    # fleets created after this date are specified in the fleet's
    # RuntimeConfiguration.
    server_launch_path: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Game server launch parameters specified for fleets created before
    # 2016-08-04 (or AWS SDK v. 0.12.16). Server launch parameters for fleets
    # created after this date are specified in the fleet's RuntimeConfiguration.
    server_launch_parameters: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Location of default log files. When a server process is shut down, Amazon
    # GameLift captures and stores any log files in this location. These logs are
    # in addition to game session logs; see more on game session logs in the
    # [Amazon GameLift Developer
    # Guide](http://docs.aws.amazon.com/gamelift/latest/developerguide/gamelift-
    # sdk-server-api.html#gamelift-sdk-server-api-server-code). If no default log
    # path for a fleet is specified, Amazon GameLift automatically uploads logs
    # that are stored on each instance at `C:\game\logs` (for Windows) or
    # `/local/game/logs` (for Linux). Use the Amazon GameLift console to access
    # stored logs.
    log_paths: typing.List[str] = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Type of game session protection to set for all new instances started in the
    # fleet.

    #   * **NoProtection** \-- The game session can be terminated during a scale-down event.

    #   * **FullProtection** \-- If the game session is in an `ACTIVE` status, it cannot be terminated during a scale-down event.
    new_game_session_protection_policy: typing.Union[
        str, "ProtectionPolicy"] = dataclasses.field(
            default=ShapeBase.NOT_SET,
        )

    # Operating system of the fleet's computing resources. A fleet's operating
    # system depends on the OS specified for the build that is deployed on this
    # fleet.
    operating_system: typing.Union[str, "OperatingSystem"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Fleet policy to limit the number of game sessions an individual player can
    # create over a span of time.
    resource_creation_limit_policy: "ResourceCreationLimitPolicy" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Names of metric groups that this fleet is included in. In Amazon
    # CloudWatch, you can view metrics for an individual fleet or aggregated
    # metrics for fleets that are in a fleet metric group. A fleet can be
    # included in only one metric group at a time.
    metric_groups: typing.List[str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # List of fleet actions that have been suspended using StopFleetActions. This
    # includes auto-scaling.
    stopped_actions: typing.List[typing.Union[str, "FleetAction"]
                                ] = dataclasses.field(
                                    default=ShapeBase.NOT_SET,
                                )


@dataclasses.dataclass
class FleetCapacity(ShapeBase):
    """
    Information about the fleet's capacity. Fleet capacity is measured in EC2
    instances. By default, new fleets have a capacity of one instance, but can be
    updated as needed. The maximum number of instances for a fleet is determined by
    the fleet's instance type.

    Fleet-related operations include:

      * CreateFleet

      * ListFleets

      * DeleteFleet

      * Describe fleets:

        * DescribeFleetAttributes

        * DescribeFleetCapacity

        * DescribeFleetPortSettings

        * DescribeFleetUtilization

        * DescribeRuntimeConfiguration

        * DescribeEC2InstanceLimits

        * DescribeFleetEvents

      * Update fleets:

        * UpdateFleetAttributes

        * UpdateFleetCapacity

        * UpdateFleetPortSettings

        * UpdateRuntimeConfiguration

      * Manage fleet actions:

        * StartFleetActions

        * StopFleetActions
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "fleet_id",
                "FleetId",
                TypeInfo(str),
            ),
            (
                "instance_type",
                "InstanceType",
                TypeInfo(typing.Union[str, EC2InstanceType]),
            ),
            (
                "instance_counts",
                "InstanceCounts",
                TypeInfo(EC2InstanceCounts),
            ),
        ]

    # Unique identifier for a fleet.
    fleet_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Name of an EC2 instance type that is supported in Amazon GameLift. A fleet
    # instance type determines the computing resources of each instance in the
    # fleet, including CPU, memory, storage, and networking capacity. Amazon
    # GameLift supports the following EC2 instance types. See [Amazon EC2
    # Instance Types](http://aws.amazon.com/ec2/instance-types/) for detailed
    # descriptions.
    instance_type: typing.Union[str, "EC2InstanceType"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Current status of fleet capacity.
    instance_counts: "EC2InstanceCounts" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class FleetCapacityExceededException(ShapeBase):
    """
    The specified fleet has no available instances to fulfill a `CreateGameSession`
    request. Clients can retry such requests immediately or after a waiting period.
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


class FleetStatus(str):
    NEW = "NEW"
    DOWNLOADING = "DOWNLOADING"
    VALIDATING = "VALIDATING"
    BUILDING = "BUILDING"
    ACTIVATING = "ACTIVATING"
    ACTIVE = "ACTIVE"
    DELETING = "DELETING"
    ERROR = "ERROR"
    TERMINATED = "TERMINATED"


class FleetType(str):
    ON_DEMAND = "ON_DEMAND"
    SPOT = "SPOT"


@dataclasses.dataclass
class FleetUtilization(ShapeBase):
    """
    Current status of fleet utilization, including the number of game and player
    sessions being hosted.

    Fleet-related operations include:

      * CreateFleet

      * ListFleets

      * DeleteFleet

      * Describe fleets:

        * DescribeFleetAttributes

        * DescribeFleetCapacity

        * DescribeFleetPortSettings

        * DescribeFleetUtilization

        * DescribeRuntimeConfiguration

        * DescribeEC2InstanceLimits

        * DescribeFleetEvents

      * Update fleets:

        * UpdateFleetAttributes

        * UpdateFleetCapacity

        * UpdateFleetPortSettings

        * UpdateRuntimeConfiguration

      * Manage fleet actions:

        * StartFleetActions

        * StopFleetActions
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "fleet_id",
                "FleetId",
                TypeInfo(str),
            ),
            (
                "active_server_process_count",
                "ActiveServerProcessCount",
                TypeInfo(int),
            ),
            (
                "active_game_session_count",
                "ActiveGameSessionCount",
                TypeInfo(int),
            ),
            (
                "current_player_session_count",
                "CurrentPlayerSessionCount",
                TypeInfo(int),
            ),
            (
                "maximum_player_session_count",
                "MaximumPlayerSessionCount",
                TypeInfo(int),
            ),
        ]

    # Unique identifier for a fleet.
    fleet_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Number of server processes in an `ACTIVE` status currently running across
    # all instances in the fleet
    active_server_process_count: int = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Number of active game sessions currently being hosted on all instances in
    # the fleet.
    active_game_session_count: int = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Number of active player sessions currently being hosted on all instances in
    # the fleet.
    current_player_session_count: int = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Maximum players allowed across all game sessions currently being hosted on
    # all instances in the fleet.
    maximum_player_session_count: int = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class GameProperty(ShapeBase):
    """
    Set of key-value pairs that contain information about a game session. When
    included in a game session request, these properties communicate details to be
    used when setting up the new game session, such as to specify a game mode,
    level, or map. Game properties are passed to the game server process when
    initiating a new game session; the server process uses the properties as
    appropriate. For more information, see the [ Amazon GameLift Developer
    Guide](http://docs.aws.amazon.com/gamelift/latest/developerguide/gamelift-sdk-
    client-api.html#gamelift-sdk-client-api-create).
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

    # Game property identifier.
    key: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Game property value.
    value: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class GameSession(ShapeBase):
    """
    Properties describing a game session.

    A game session in ACTIVE status can host players. When a game session ends, its
    status is set to `TERMINATED`.

    Once the session ends, the game session object is retained for 30 days. This
    means you can reuse idempotency token values after this time. Game session logs
    are retained for 14 days.

    Game-session-related operations include:

      * CreateGameSession

      * DescribeGameSessions

      * DescribeGameSessionDetails

      * SearchGameSessions

      * UpdateGameSession

      * GetGameSessionLogUrl

      * Game session placements

        * StartGameSessionPlacement

        * DescribeGameSessionPlacement

        * StopGameSessionPlacement
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "game_session_id",
                "GameSessionId",
                TypeInfo(str),
            ),
            (
                "name",
                "Name",
                TypeInfo(str),
            ),
            (
                "fleet_id",
                "FleetId",
                TypeInfo(str),
            ),
            (
                "creation_time",
                "CreationTime",
                TypeInfo(datetime.datetime),
            ),
            (
                "termination_time",
                "TerminationTime",
                TypeInfo(datetime.datetime),
            ),
            (
                "current_player_session_count",
                "CurrentPlayerSessionCount",
                TypeInfo(int),
            ),
            (
                "maximum_player_session_count",
                "MaximumPlayerSessionCount",
                TypeInfo(int),
            ),
            (
                "status",
                "Status",
                TypeInfo(typing.Union[str, GameSessionStatus]),
            ),
            (
                "status_reason",
                "StatusReason",
                TypeInfo(typing.Union[str, GameSessionStatusReason]),
            ),
            (
                "game_properties",
                "GameProperties",
                TypeInfo(typing.List[GameProperty]),
            ),
            (
                "ip_address",
                "IpAddress",
                TypeInfo(str),
            ),
            (
                "port",
                "Port",
                TypeInfo(int),
            ),
            (
                "player_session_creation_policy",
                "PlayerSessionCreationPolicy",
                TypeInfo(typing.Union[str, PlayerSessionCreationPolicy]),
            ),
            (
                "creator_id",
                "CreatorId",
                TypeInfo(str),
            ),
            (
                "game_session_data",
                "GameSessionData",
                TypeInfo(str),
            ),
            (
                "matchmaker_data",
                "MatchmakerData",
                TypeInfo(str),
            ),
        ]

    # Unique identifier for the game session. A game session ARN has the
    # following format: `arn:aws:gamelift:<region>::gamesession/<fleet
    # ID>/<custom ID string or idempotency token>`.
    game_session_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Descriptive label that is associated with a game session. Session names do
    # not need to be unique.
    name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Unique identifier for a fleet that the game session is running on.
    fleet_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Time stamp indicating when this data object was created. Format is a number
    # expressed in Unix time as milliseconds (for example "1469498468.057").
    creation_time: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Time stamp indicating when this data object was terminated. Format is a
    # number expressed in Unix time as milliseconds (for example
    # "1469498468.057").
    termination_time: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Number of players currently in the game session.
    current_player_session_count: int = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Maximum number of players that can be connected simultaneously to the game
    # session.
    maximum_player_session_count: int = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Current status of the game session. A game session must have an `ACTIVE`
    # status to have player sessions.
    status: typing.Union[str, "GameSessionStatus"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Provides additional information about game session status. `INTERRUPTED`
    # indicates that the game session was hosted on a spot instance that was
    # reclaimed, causing the active game session to be terminated.
    status_reason: typing.Union[str, "GameSessionStatusReason"
                               ] = dataclasses.field(
                                   default=ShapeBase.NOT_SET,
                               )

    # Set of custom properties for a game session, formatted as key:value pairs.
    # These properties are passed to a game server process in the GameSession
    # object with a request to start a new game session (see [Start a Game
    # Session](http://docs.aws.amazon.com/gamelift/latest/developerguide/gamelift-
    # sdk-server-api.html#gamelift-sdk-server-startsession)). You can search for
    # active game sessions based on this custom data with SearchGameSessions.
    game_properties: typing.List["GameProperty"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # IP address of the game session. To connect to a Amazon GameLift game
    # server, an app needs both the IP address and port number.
    ip_address: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Port number for the game session. To connect to a Amazon GameLift game
    # server, an app needs both the IP address and port number.
    port: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Indicates whether or not the game session is accepting new players.
    player_session_creation_policy: typing.Union[
        str, "PlayerSessionCreationPolicy"] = dataclasses.field(
            default=ShapeBase.NOT_SET,
        )

    # Unique identifier for a player. This ID is used to enforce a resource
    # protection policy (if one exists), that limits the number of game sessions
    # a player can create.
    creator_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Set of custom game session properties, formatted as a single string value.
    # This data is passed to a game server process in the GameSession object with
    # a request to start a new game session (see [Start a Game
    # Session](http://docs.aws.amazon.com/gamelift/latest/developerguide/gamelift-
    # sdk-server-api.html#gamelift-sdk-server-startsession)).
    game_session_data: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Information about the matchmaking process that was used to create the game
    # session. It is in JSON syntax, formatted as a string. In addition the
    # matchmaking configuration used, it contains data on all players assigned to
    # the match, including player attributes and team assignments. For more
    # details on matchmaker data, see [Match
    # Data](http://docs.aws.amazon.com/gamelift/latest/developerguide/match-
    # server.html#match-server-data). Matchmaker data is useful when requesting
    # match backfills, and is updated whenever new players are added during a
    # successful backfill (see StartMatchBackfill).
    matchmaker_data: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class GameSessionConnectionInfo(ShapeBase):
    """
    Connection information for the new game session that is created with
    matchmaking. (with StartMatchmaking). Once a match is set, the FlexMatch engine
    places the match and creates a new game session for it. This information,
    including the game session endpoint and player sessions for each player in the
    original matchmaking request, is added to the MatchmakingTicket, which can be
    retrieved by calling DescribeMatchmaking.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "game_session_arn",
                "GameSessionArn",
                TypeInfo(str),
            ),
            (
                "ip_address",
                "IpAddress",
                TypeInfo(str),
            ),
            (
                "port",
                "Port",
                TypeInfo(int),
            ),
            (
                "matched_player_sessions",
                "MatchedPlayerSessions",
                TypeInfo(typing.List[MatchedPlayerSession]),
            ),
        ]

    # Amazon Resource Name
    # ([ARN](http://docs.aws.amazon.com/AmazonS3/latest/dev/s3-arn-format.html))
    # that is assigned to a game session and uniquely identifies it.
    game_session_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # IP address of the game session. To connect to a Amazon GameLift game
    # server, an app needs both the IP address and port number.
    ip_address: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Port number for the game session. To connect to a Amazon GameLift game
    # server, an app needs both the IP address and port number.
    port: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Collection of player session IDs, one for each player ID that was included
    # in the original matchmaking request.
    matched_player_sessions: typing.List["MatchedPlayerSession"
                                        ] = dataclasses.field(
                                            default=ShapeBase.NOT_SET,
                                        )


@dataclasses.dataclass
class GameSessionDetail(ShapeBase):
    """
    A game session's properties plus the protection policy currently in force.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "game_session",
                "GameSession",
                TypeInfo(GameSession),
            ),
            (
                "protection_policy",
                "ProtectionPolicy",
                TypeInfo(typing.Union[str, ProtectionPolicy]),
            ),
        ]

    # Object that describes a game session.
    game_session: "GameSession" = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Current status of protection for the game session.

    #   * **NoProtection** \-- The game session can be terminated during a scale-down event.

    #   * **FullProtection** \-- If the game session is in an `ACTIVE` status, it cannot be terminated during a scale-down event.
    protection_policy: typing.Union[str, "ProtectionPolicy"
                                   ] = dataclasses.field(
                                       default=ShapeBase.NOT_SET,
                                   )


@dataclasses.dataclass
class GameSessionFullException(ShapeBase):
    """
    The game instance is currently full and cannot allow the requested player(s) to
    join. Clients can retry such requests immediately or after a waiting period.
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
class GameSessionPlacement(ShapeBase):
    """
    Object that describes a StartGameSessionPlacement request. This object includes
    the full details of the original request plus the current status and start/end
    time stamps.

    Game session placement-related operations include:

      * StartGameSessionPlacement

      * DescribeGameSessionPlacement

      * StopGameSessionPlacement
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "placement_id",
                "PlacementId",
                TypeInfo(str),
            ),
            (
                "game_session_queue_name",
                "GameSessionQueueName",
                TypeInfo(str),
            ),
            (
                "status",
                "Status",
                TypeInfo(typing.Union[str, GameSessionPlacementState]),
            ),
            (
                "game_properties",
                "GameProperties",
                TypeInfo(typing.List[GameProperty]),
            ),
            (
                "maximum_player_session_count",
                "MaximumPlayerSessionCount",
                TypeInfo(int),
            ),
            (
                "game_session_name",
                "GameSessionName",
                TypeInfo(str),
            ),
            (
                "game_session_id",
                "GameSessionId",
                TypeInfo(str),
            ),
            (
                "game_session_arn",
                "GameSessionArn",
                TypeInfo(str),
            ),
            (
                "game_session_region",
                "GameSessionRegion",
                TypeInfo(str),
            ),
            (
                "player_latencies",
                "PlayerLatencies",
                TypeInfo(typing.List[PlayerLatency]),
            ),
            (
                "start_time",
                "StartTime",
                TypeInfo(datetime.datetime),
            ),
            (
                "end_time",
                "EndTime",
                TypeInfo(datetime.datetime),
            ),
            (
                "ip_address",
                "IpAddress",
                TypeInfo(str),
            ),
            (
                "port",
                "Port",
                TypeInfo(int),
            ),
            (
                "placed_player_sessions",
                "PlacedPlayerSessions",
                TypeInfo(typing.List[PlacedPlayerSession]),
            ),
            (
                "game_session_data",
                "GameSessionData",
                TypeInfo(str),
            ),
            (
                "matchmaker_data",
                "MatchmakerData",
                TypeInfo(str),
            ),
        ]

    # Unique identifier for a game session placement.
    placement_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Descriptive label that is associated with game session queue. Queue names
    # must be unique within each region.
    game_session_queue_name: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Current status of the game session placement request.

    #   * **PENDING** \-- The placement request is currently in the queue waiting to be processed.

    #   * **FULFILLED** \-- A new game session and player sessions (if requested) have been successfully created. Values for _GameSessionArn_ and _GameSessionRegion_ are available.

    #   * **CANCELLED** \-- The placement request was canceled with a call to StopGameSessionPlacement.

    #   * **TIMED_OUT** \-- A new game session was not successfully created before the time limit expired. You can resubmit the placement request as needed.
    status: typing.Union[str, "GameSessionPlacementState"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Set of custom properties for a game session, formatted as key:value pairs.
    # These properties are passed to a game server process in the GameSession
    # object with a request to start a new game session (see [Start a Game
    # Session](http://docs.aws.amazon.com/gamelift/latest/developerguide/gamelift-
    # sdk-server-api.html#gamelift-sdk-server-startsession)).
    game_properties: typing.List["GameProperty"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Maximum number of players that can be connected simultaneously to the game
    # session.
    maximum_player_session_count: int = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Descriptive label that is associated with a game session. Session names do
    # not need to be unique.
    game_session_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Unique identifier for the game session. This value is set once the new game
    # session is placed (placement status is `FULFILLED`).
    game_session_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Identifier for the game session created by this placement request. This
    # value is set once the new game session is placed (placement status is
    # `FULFILLED`). This identifier is unique across all regions. You can use
    # this value as a `GameSessionId` value as needed.
    game_session_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Name of the region where the game session created by this placement request
    # is running. This value is set once the new game session is placed
    # (placement status is `FULFILLED`).
    game_session_region: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Set of values, expressed in milliseconds, indicating the amount of latency
    # that a player experiences when connected to AWS regions.
    player_latencies: typing.List["PlayerLatency"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Time stamp indicating when this request was placed in the queue. Format is
    # a number expressed in Unix time as milliseconds (for example
    # "1469498468.057").
    start_time: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Time stamp indicating when this request was completed, canceled, or timed
    # out.
    end_time: datetime.datetime = dataclasses.field(default=ShapeBase.NOT_SET, )

    # IP address of the game session. To connect to a Amazon GameLift game
    # server, an app needs both the IP address and port number. This value is set
    # once the new game session is placed (placement status is `FULFILLED`).
    ip_address: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Port number for the game session. To connect to a Amazon GameLift game
    # server, an app needs both the IP address and port number. This value is set
    # once the new game session is placed (placement status is `FULFILLED`).
    port: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Collection of information on player sessions created in response to the
    # game session placement request. These player sessions are created only once
    # a new game session is successfully placed (placement status is
    # `FULFILLED`). This information includes the player ID (as provided in the
    # placement request) and the corresponding player session ID. Retrieve full
    # player sessions by calling DescribePlayerSessions with the player session
    # ID.
    placed_player_sessions: typing.List["PlacedPlayerSession"
                                       ] = dataclasses.field(
                                           default=ShapeBase.NOT_SET,
                                       )

    # Set of custom game session properties, formatted as a single string value.
    # This data is passed to a game server process in the GameSession object with
    # a request to start a new game session (see [Start a Game
    # Session](http://docs.aws.amazon.com/gamelift/latest/developerguide/gamelift-
    # sdk-server-api.html#gamelift-sdk-server-startsession)).
    game_session_data: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Information on the matchmaking process for this game. Data is in JSON
    # syntax, formatted as a string. It identifies the matchmaking configuration
    # used to create the match, and contains data on all players assigned to the
    # match, including player attributes and team assignments. For more details
    # on matchmaker data, see [Match
    # Data](http://docs.aws.amazon.com/gamelift/latest/developerguide/match-
    # server.html#match-server-data).
    matchmaker_data: str = dataclasses.field(default=ShapeBase.NOT_SET, )


class GameSessionPlacementState(str):
    PENDING = "PENDING"
    FULFILLED = "FULFILLED"
    CANCELLED = "CANCELLED"
    TIMED_OUT = "TIMED_OUT"


@dataclasses.dataclass
class GameSessionQueue(ShapeBase):
    """
    Configuration of a queue that is used to process game session placement
    requests. The queue configuration identifies several game features:

      * The destinations where a new game session can potentially be hosted. Amazon GameLift tries these destinations in an order based on either the queue's default order or player latency information, if provided in a placement request. With latency information, Amazon GameLift can place game sessions where the majority of players are reporting the lowest possible latency. 

      * The length of time that placement requests can wait in the queue before timing out. 

      * A set of optional latency policies that protect individual players from high latencies, preventing game sessions from being placed where any individual player is reporting latency higher than a policy's maximum.

    Queue-related operations include:

      * CreateGameSessionQueue

      * DescribeGameSessionQueues

      * UpdateGameSessionQueue

      * DeleteGameSessionQueue
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "name",
                "Name",
                TypeInfo(str),
            ),
            (
                "game_session_queue_arn",
                "GameSessionQueueArn",
                TypeInfo(str),
            ),
            (
                "timeout_in_seconds",
                "TimeoutInSeconds",
                TypeInfo(int),
            ),
            (
                "player_latency_policies",
                "PlayerLatencyPolicies",
                TypeInfo(typing.List[PlayerLatencyPolicy]),
            ),
            (
                "destinations",
                "Destinations",
                TypeInfo(typing.List[GameSessionQueueDestination]),
            ),
        ]

    # Descriptive label that is associated with game session queue. Queue names
    # must be unique within each region.
    name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Amazon Resource Name
    # ([ARN](http://docs.aws.amazon.com/AmazonS3/latest/dev/s3-arn-format.html))
    # that is assigned to a game session queue and uniquely identifies it. Format
    # is
    # `arn:aws:gamelift:<region>::fleet/fleet-a1234567-b8c9-0d1e-2fa3-b45c6d7e8912`.
    game_session_queue_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Maximum time, in seconds, that a new game session placement request remains
    # in the queue. When a request exceeds this time, the game session placement
    # changes to a `TIMED_OUT` status.
    timeout_in_seconds: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Collection of latency policies to apply when processing game sessions
    # placement requests with player latency information. Multiple policies are
    # evaluated in order of the maximum latency value, starting with the lowest
    # latency values. With just one policy, it is enforced at the start of the
    # game session placement for the duration period. With multiple policies,
    # each policy is enforced consecutively for its duration period. For example,
    # a queue might enforce a 60-second policy followed by a 120-second policy,
    # and then no policy for the remainder of the placement.
    player_latency_policies: typing.List["PlayerLatencyPolicy"
                                        ] = dataclasses.field(
                                            default=ShapeBase.NOT_SET,
                                        )

    # List of fleets that can be used to fulfill game session placement requests
    # in the queue. Fleets are identified by either a fleet ARN or a fleet alias
    # ARN. Destinations are listed in default preference order.
    destinations: typing.List["GameSessionQueueDestination"
                             ] = dataclasses.field(
                                 default=ShapeBase.NOT_SET,
                             )


@dataclasses.dataclass
class GameSessionQueueDestination(ShapeBase):
    """
    Fleet designated in a game session queue. Requests for new game sessions in the
    queue are fulfilled by starting a new game session on any destination configured
    for a queue.

    Queue-related operations include:

      * CreateGameSessionQueue

      * DescribeGameSessionQueues

      * UpdateGameSessionQueue

      * DeleteGameSessionQueue
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "destination_arn",
                "DestinationArn",
                TypeInfo(str),
            ),
        ]

    # Amazon Resource Name (ARN) assigned to fleet or fleet alias. ARNs, which
    # include a fleet ID or alias ID and a region name, provide a unique
    # identifier across all regions.
    destination_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )


class GameSessionStatus(str):
    ACTIVE = "ACTIVE"
    ACTIVATING = "ACTIVATING"
    TERMINATED = "TERMINATED"
    TERMINATING = "TERMINATING"
    ERROR = "ERROR"


class GameSessionStatusReason(str):
    INTERRUPTED = "INTERRUPTED"


@dataclasses.dataclass
class GetGameSessionLogUrlInput(ShapeBase):
    """
    Represents the input for a request action.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "game_session_id",
                "GameSessionId",
                TypeInfo(str),
            ),
        ]

    # Unique identifier for the game session to get logs for.
    game_session_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class GetGameSessionLogUrlOutput(OutputShapeBase):
    """
    Represents the returned data in response to a request action.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "pre_signed_url",
                "PreSignedUrl",
                TypeInfo(str),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Location of the requested game session logs, available for download.
    pre_signed_url: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class GetInstanceAccessInput(ShapeBase):
    """
    Represents the input for a request action.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "fleet_id",
                "FleetId",
                TypeInfo(str),
            ),
            (
                "instance_id",
                "InstanceId",
                TypeInfo(str),
            ),
        ]

    # Unique identifier for a fleet that contains the instance you want access
    # to. The fleet can be in any of the following statuses: `ACTIVATING`,
    # `ACTIVE`, or `ERROR`. Fleets with an `ERROR` status may be accessible for a
    # short time before they are deleted.
    fleet_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Unique identifier for an instance you want to get access to. You can access
    # an instance in any status.
    instance_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class GetInstanceAccessOutput(OutputShapeBase):
    """
    Represents the returned data in response to a request action.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "instance_access",
                "InstanceAccess",
                TypeInfo(InstanceAccess),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Object that contains connection information for a fleet instance, including
    # IP address and access credentials.
    instance_access: "InstanceAccess" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class IdempotentParameterMismatchException(ShapeBase):
    """
    A game session with this custom ID string already exists in this fleet. Resolve
    this conflict before retrying this request.
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
class Instance(ShapeBase):
    """
    Properties that describe an instance of a virtual computing resource that hosts
    one or more game servers. A fleet may contain zero or more instances.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "fleet_id",
                "FleetId",
                TypeInfo(str),
            ),
            (
                "instance_id",
                "InstanceId",
                TypeInfo(str),
            ),
            (
                "ip_address",
                "IpAddress",
                TypeInfo(str),
            ),
            (
                "operating_system",
                "OperatingSystem",
                TypeInfo(typing.Union[str, OperatingSystem]),
            ),
            (
                "type",
                "Type",
                TypeInfo(typing.Union[str, EC2InstanceType]),
            ),
            (
                "status",
                "Status",
                TypeInfo(typing.Union[str, InstanceStatus]),
            ),
            (
                "creation_time",
                "CreationTime",
                TypeInfo(datetime.datetime),
            ),
        ]

    # Unique identifier for a fleet that the instance is in.
    fleet_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Unique identifier for an instance.
    instance_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # IP address assigned to the instance.
    ip_address: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Operating system that is running on this instance.
    operating_system: typing.Union[str, "OperatingSystem"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # EC2 instance type that defines the computing resources of this instance.
    type: typing.Union[str, "EC2InstanceType"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Current status of the instance. Possible statuses include the following:

    #   * **PENDING** \-- The instance is in the process of being created and launching server processes as defined in the fleet's run-time configuration.

    #   * **ACTIVE** \-- The instance has been successfully created and at least one server process has successfully launched and reported back to Amazon GameLift that it is ready to host a game session. The instance is now considered ready to host game sessions.

    #   * **TERMINATING** \-- The instance is in the process of shutting down. This may happen to reduce capacity during a scaling down event or to recycle resources in the event of a problem.
    status: typing.Union[str, "InstanceStatus"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Time stamp indicating when this data object was created. Format is a number
    # expressed in Unix time as milliseconds (for example "1469498468.057").
    creation_time: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class InstanceAccess(ShapeBase):
    """
    Information required to remotely connect to a fleet instance. Access is
    requested by calling GetInstanceAccess.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "fleet_id",
                "FleetId",
                TypeInfo(str),
            ),
            (
                "instance_id",
                "InstanceId",
                TypeInfo(str),
            ),
            (
                "ip_address",
                "IpAddress",
                TypeInfo(str),
            ),
            (
                "operating_system",
                "OperatingSystem",
                TypeInfo(typing.Union[str, OperatingSystem]),
            ),
            (
                "credentials",
                "Credentials",
                TypeInfo(InstanceCredentials),
            ),
        ]

    # Unique identifier for a fleet containing the instance being accessed.
    fleet_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Unique identifier for an instance being accessed.
    instance_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # IP address assigned to the instance.
    ip_address: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Operating system that is running on the instance.
    operating_system: typing.Union[str, "OperatingSystem"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Credentials required to access the instance.
    credentials: "InstanceCredentials" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class InstanceCredentials(ShapeBase):
    """
    Set of credentials required to remotely access a fleet instance. Access
    credentials are requested by calling GetInstanceAccess and returned in an
    InstanceAccess object.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "user_name",
                "UserName",
                TypeInfo(str),
            ),
            (
                "secret",
                "Secret",
                TypeInfo(str),
            ),
        ]

    # User login string.
    user_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Secret string. For Windows instances, the secret is a password for use with
    # Windows Remote Desktop. For Linux instances, it is a private key (which
    # must be saved as a `.pem` file) for use with SSH.
    secret: str = dataclasses.field(default=ShapeBase.NOT_SET, )


class InstanceStatus(str):
    PENDING = "PENDING"
    ACTIVE = "ACTIVE"
    TERMINATING = "TERMINATING"


@dataclasses.dataclass
class InternalServiceException(ShapeBase):
    """
    The service encountered an unrecoverable internal failure while processing the
    request. Clients can retry such requests immediately or after a waiting period.
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
class InvalidFleetStatusException(ShapeBase):
    """
    The requested operation would cause a conflict with the current state of a
    resource associated with the request and/or the fleet. Resolve the conflict
    before retrying.
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
class InvalidGameSessionStatusException(ShapeBase):
    """
    The requested operation would cause a conflict with the current state of a
    resource associated with the request and/or the game instance. Resolve the
    conflict before retrying.
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
class InvalidRequestException(ShapeBase):
    """
    One or more parameter values in the request are invalid. Correct the invalid
    parameter values before retrying.
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
class IpPermission(ShapeBase):
    """
    A range of IP addresses and port settings that allow inbound traffic to connect
    to server processes on Amazon GameLift. Each game session hosted on a fleet is
    assigned a unique combination of IP address and port number, which must fall
    into the fleet's allowed ranges. This combination is included in the GameSession
    object.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "from_port",
                "FromPort",
                TypeInfo(int),
            ),
            (
                "to_port",
                "ToPort",
                TypeInfo(int),
            ),
            (
                "ip_range",
                "IpRange",
                TypeInfo(str),
            ),
            (
                "protocol",
                "Protocol",
                TypeInfo(typing.Union[str, IpProtocol]),
            ),
        ]

    # Starting value for a range of allowed port numbers.
    from_port: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Ending value for a range of allowed port numbers. Port numbers are end-
    # inclusive. This value must be higher than `FromPort`.
    to_port: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Range of allowed IP addresses. This value must be expressed in CIDR
    # notation. Example: "`000.000.000.000/[subnet mask]`" or optionally the
    # shortened version "`0.0.0.0/[subnet mask]`".
    ip_range: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Network communication protocol used by the fleet.
    protocol: typing.Union[str, "IpProtocol"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


class IpProtocol(str):
    TCP = "TCP"
    UDP = "UDP"


@dataclasses.dataclass
class LimitExceededException(ShapeBase):
    """
    The requested operation would cause the resource to exceed the allowed service
    limit. Resolve the issue before retrying.
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
class ListAliasesInput(ShapeBase):
    """
    Represents the input for a request action.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "routing_strategy_type",
                "RoutingStrategyType",
                TypeInfo(typing.Union[str, RoutingStrategyType]),
            ),
            (
                "name",
                "Name",
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

    # Type of routing to filter results on. Use this parameter to retrieve only
    # aliases of a certain type. To retrieve all aliases, leave this parameter
    # empty.

    # Possible routing types include the following:

    #   * **SIMPLE** \-- The alias resolves to one specific fleet. Use this type when routing to active fleets.

    #   * **TERMINAL** \-- The alias does not resolve to a fleet but instead can be used to display a message to the user. A terminal alias throws a TerminalRoutingStrategyException with the RoutingStrategy message embedded.
    routing_strategy_type: typing.Union[str, "RoutingStrategyType"
                                       ] = dataclasses.field(
                                           default=ShapeBase.NOT_SET,
                                       )

    # Descriptive label that is associated with an alias. Alias names do not need
    # to be unique.
    name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Maximum number of results to return. Use this parameter with `NextToken` to
    # get results as a set of sequential pages.
    limit: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Token that indicates the start of the next sequential page of results. Use
    # the token that is returned with a previous call to this action. To start at
    # the beginning of the result set, do not specify a value.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ListAliasesOutput(OutputShapeBase):
    """
    Represents the returned data in response to a request action.
    """

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
                TypeInfo(typing.List[Alias]),
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

    # Collection of alias records that match the list request.
    aliases: typing.List["Alias"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Token that indicates where to resume retrieving results on the next call to
    # this action. If no token is returned, these results represent the end of
    # the list.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ListBuildsInput(ShapeBase):
    """
    Represents the input for a request action.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "status",
                "Status",
                TypeInfo(typing.Union[str, BuildStatus]),
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

    # Build status to filter results by. To retrieve all builds, leave this
    # parameter empty.

    # Possible build statuses include the following:

    #   * **INITIALIZED** \-- A new build has been defined, but no files have been uploaded. You cannot create fleets for builds that are in this status. When a build is successfully created, the build status is set to this value.

    #   * **READY** \-- The game build has been successfully uploaded. You can now create new fleets for this build.

    #   * **FAILED** \-- The game build upload failed. You cannot create new fleets for this build.
    status: typing.Union[str, "BuildStatus"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Maximum number of results to return. Use this parameter with `NextToken` to
    # get results as a set of sequential pages.
    limit: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Token that indicates the start of the next sequential page of results. Use
    # the token that is returned with a previous call to this action. To start at
    # the beginning of the result set, do not specify a value.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ListBuildsOutput(OutputShapeBase):
    """
    Represents the returned data in response to a request action.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "builds",
                "Builds",
                TypeInfo(typing.List[Build]),
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

    # Collection of build records that match the request.
    builds: typing.List["Build"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Token that indicates where to resume retrieving results on the next call to
    # this action. If no token is returned, these results represent the end of
    # the list.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ListFleetsInput(ShapeBase):
    """
    Represents the input for a request action.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "build_id",
                "BuildId",
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

    # Unique identifier for a build to return fleets for. Use this parameter to
    # return only fleets using the specified build. To retrieve all fleets, leave
    # this parameter empty.
    build_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Maximum number of results to return. Use this parameter with `NextToken` to
    # get results as a set of sequential pages.
    limit: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Token that indicates the start of the next sequential page of results. Use
    # the token that is returned with a previous call to this action. To start at
    # the beginning of the result set, do not specify a value.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ListFleetsOutput(OutputShapeBase):
    """
    Represents the returned data in response to a request action.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "fleet_ids",
                "FleetIds",
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

    # Set of fleet IDs matching the list request. You can retrieve additional
    # information about all returned fleets by passing this result set to a call
    # to DescribeFleetAttributes, DescribeFleetCapacity, or
    # DescribeFleetUtilization.
    fleet_ids: typing.List[str] = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Token that indicates where to resume retrieving results on the next call to
    # this action. If no token is returned, these results represent the end of
    # the list.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class MatchedPlayerSession(ShapeBase):
    """
    Represents a new player session that is created as a result of a successful
    FlexMatch match. A successful match automatically creates new player sessions
    for every player ID in the original matchmaking request.

    When players connect to the match's game session, they must include both player
    ID and player session ID in order to claim their assigned player slot.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "player_id",
                "PlayerId",
                TypeInfo(str),
            ),
            (
                "player_session_id",
                "PlayerSessionId",
                TypeInfo(str),
            ),
        ]

    # Unique identifier for a player
    player_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Unique identifier for a player session
    player_session_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class MatchmakingConfiguration(ShapeBase):
    """
    Guidelines for use with FlexMatch to match players into games. All matchmaking
    requests must specify a matchmaking configuration.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
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
            (
                "game_session_queue_arns",
                "GameSessionQueueArns",
                TypeInfo(typing.List[str]),
            ),
            (
                "request_timeout_seconds",
                "RequestTimeoutSeconds",
                TypeInfo(int),
            ),
            (
                "acceptance_timeout_seconds",
                "AcceptanceTimeoutSeconds",
                TypeInfo(int),
            ),
            (
                "acceptance_required",
                "AcceptanceRequired",
                TypeInfo(bool),
            ),
            (
                "rule_set_name",
                "RuleSetName",
                TypeInfo(str),
            ),
            (
                "notification_target",
                "NotificationTarget",
                TypeInfo(str),
            ),
            (
                "additional_player_count",
                "AdditionalPlayerCount",
                TypeInfo(int),
            ),
            (
                "custom_event_data",
                "CustomEventData",
                TypeInfo(str),
            ),
            (
                "creation_time",
                "CreationTime",
                TypeInfo(datetime.datetime),
            ),
            (
                "game_properties",
                "GameProperties",
                TypeInfo(typing.List[GameProperty]),
            ),
            (
                "game_session_data",
                "GameSessionData",
                TypeInfo(str),
            ),
        ]

    # Unique identifier for a matchmaking configuration. This name is used to
    # identify the configuration associated with a matchmaking request or ticket.
    name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Descriptive label that is associated with matchmaking configuration.
    description: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Amazon Resource Name
    # ([ARN](http://docs.aws.amazon.com/AmazonS3/latest/dev/s3-arn-format.html))
    # that is assigned to a game session queue and uniquely identifies it. Format
    # is
    # `arn:aws:gamelift:<region>::fleet/fleet-a1234567-b8c9-0d1e-2fa3-b45c6d7e8912`.
    # These queues are used when placing game sessions for matches that are
    # created with this matchmaking configuration. Queues can be located in any
    # region.
    game_session_queue_arns: typing.List[str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Maximum duration, in seconds, that a matchmaking ticket can remain in
    # process before timing out. Requests that time out can be resubmitted as
    # needed.
    request_timeout_seconds: int = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Length of time (in seconds) to wait for players to accept a proposed match.
    # If any player rejects the match or fails to accept before the timeout, the
    # ticket continues to look for an acceptable match.
    acceptance_timeout_seconds: int = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Flag that determines whether or not a match that was created with this
    # configuration must be accepted by the matched players. To require
    # acceptance, set to TRUE.
    acceptance_required: bool = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Unique identifier for a matchmaking rule set to use with this
    # configuration. A matchmaking configuration can only use rule sets that are
    # defined in the same region.
    rule_set_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # SNS topic ARN that is set up to receive matchmaking notifications.
    notification_target: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Number of player slots in a match to keep open for future players. For
    # example, if the configuration's rule set specifies a match for a single
    # 12-person team, and the additional player count is set to 2, only 10
    # players are selected for the match.
    additional_player_count: int = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Information to attached to all events related to the matchmaking
    # configuration.
    custom_event_data: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Time stamp indicating when this data object was created. Format is a number
    # expressed in Unix time as milliseconds (for example "1469498468.057").
    creation_time: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Set of custom properties for a game session, formatted as key:value pairs.
    # These properties are passed to a game server process in the GameSession
    # object with a request to start a new game session (see [Start a Game
    # Session](http://docs.aws.amazon.com/gamelift/latest/developerguide/gamelift-
    # sdk-server-api.html#gamelift-sdk-server-startsession)). This information is
    # added to the new GameSession object that is created for a successful match.
    game_properties: typing.List["GameProperty"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Set of custom game session properties, formatted as a single string value.
    # This data is passed to a game server process in the GameSession object with
    # a request to start a new game session (see [Start a Game
    # Session](http://docs.aws.amazon.com/gamelift/latest/developerguide/gamelift-
    # sdk-server-api.html#gamelift-sdk-server-startsession)). This information is
    # added to the new GameSession object that is created for a successful match.
    game_session_data: str = dataclasses.field(default=ShapeBase.NOT_SET, )


class MatchmakingConfigurationStatus(str):
    CANCELLED = "CANCELLED"
    COMPLETED = "COMPLETED"
    FAILED = "FAILED"
    PLACING = "PLACING"
    QUEUED = "QUEUED"
    REQUIRES_ACCEPTANCE = "REQUIRES_ACCEPTANCE"
    SEARCHING = "SEARCHING"
    TIMED_OUT = "TIMED_OUT"


@dataclasses.dataclass
class MatchmakingRuleSet(ShapeBase):
    """
    Set of rule statements, used with FlexMatch, that determine how to build a
    certain kind of player match. Each rule set describes a type of group to be
    created and defines the parameters for acceptable player matches. Rule sets are
    used in MatchmakingConfiguration objects.

    A rule set may define the following elements for a match. For detailed
    information and examples showing how to construct a rule set, see [Build a
    FlexMatch Rule
    Set](http://docs.aws.amazon.com/gamelift/latest/developerguide/match-
    rulesets.html).

      * Teams -- Required. A rule set must define one or multiple teams for the match and set minimum and maximum team sizes. For example, a rule set might describe a 4x4 match that requires all eight slots to be filled. 

      * Player attributes -- Optional. These attributes specify a set of player characteristics to evaluate when looking for a match. Matchmaking requests that use a rule set with player attributes must provide the corresponding attribute values. For example, an attribute might specify a player's skill or level.

      * Rules -- Optional. Rules define how to evaluate potential players for a match based on player attributes. A rule might specify minimum requirements for individual players, teams, or entire matches. For example, a rule might require each player to meet a certain skill level, each team to have at least one player in a certain role, or the match to have a minimum average skill level. or may describe an entire group--such as all teams must be evenly matched or have at least one player in a certain role. 

      * Expansions -- Optional. Expansions allow you to relax the rules after a period of time when no acceptable matches are found. This feature lets you balance getting players into games in a reasonable amount of time instead of making them wait indefinitely for the best possible match. For example, you might use an expansion to increase the maximum skill variance between players after 30 seconds.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "rule_set_body",
                "RuleSetBody",
                TypeInfo(str),
            ),
            (
                "rule_set_name",
                "RuleSetName",
                TypeInfo(str),
            ),
            (
                "creation_time",
                "CreationTime",
                TypeInfo(datetime.datetime),
            ),
        ]

    # Collection of matchmaking rules, formatted as a JSON string. (Note that
    # comments14 are not allowed in JSON, but most elements support a description
    # field.)
    rule_set_body: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Unique identifier for a matchmaking rule set
    rule_set_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Time stamp indicating when this data object was created. Format is a number
    # expressed in Unix time as milliseconds (for example "1469498468.057").
    creation_time: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class MatchmakingTicket(ShapeBase):
    """
    Ticket generated to track the progress of a matchmaking request. Each ticket is
    uniquely identified by a ticket ID, supplied by the requester, when creating a
    matchmaking request with StartMatchmaking. Tickets can be retrieved by calling
    DescribeMatchmaking with the ticket ID.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "ticket_id",
                "TicketId",
                TypeInfo(str),
            ),
            (
                "configuration_name",
                "ConfigurationName",
                TypeInfo(str),
            ),
            (
                "status",
                "Status",
                TypeInfo(typing.Union[str, MatchmakingConfigurationStatus]),
            ),
            (
                "status_reason",
                "StatusReason",
                TypeInfo(str),
            ),
            (
                "status_message",
                "StatusMessage",
                TypeInfo(str),
            ),
            (
                "start_time",
                "StartTime",
                TypeInfo(datetime.datetime),
            ),
            (
                "end_time",
                "EndTime",
                TypeInfo(datetime.datetime),
            ),
            (
                "players",
                "Players",
                TypeInfo(typing.List[Player]),
            ),
            (
                "game_session_connection_info",
                "GameSessionConnectionInfo",
                TypeInfo(GameSessionConnectionInfo),
            ),
            (
                "estimated_wait_time",
                "EstimatedWaitTime",
                TypeInfo(int),
            ),
        ]

    # Unique identifier for a matchmaking ticket.
    ticket_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Name of the MatchmakingConfiguration that is used with this ticket.
    # Matchmaking configurations determine how players are grouped into a match
    # and how a new game session is created for the match.
    configuration_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Current status of the matchmaking request.

    #   * **QUEUED** \-- The matchmaking request has been received and is currently waiting to be processed.

    #   * **SEARCHING** \-- The matchmaking request is currently being processed.

    #   * **REQUIRES_ACCEPTANCE** \-- A match has been proposed and the players must accept the match (see AcceptMatch). This status is used only with requests that use a matchmaking configuration with a player acceptance requirement.

    #   * **PLACING** \-- The FlexMatch engine has matched players and is in the process of placing a new game session for the match.

    #   * **COMPLETED** \-- Players have been matched and a game session is ready to host the players. A ticket in this state contains the necessary connection information for players.

    #   * **FAILED** \-- The matchmaking request was not completed. Tickets with players who fail to accept a proposed match are placed in `FAILED` status.

    #   * **CANCELLED** \-- The matchmaking request was canceled with a call to StopMatchmaking.

    #   * **TIMED_OUT** \-- The matchmaking request was not successful within the duration specified in the matchmaking configuration.

    # Matchmaking requests that fail to successfully complete (statuses FAILED,
    # CANCELLED, TIMED_OUT) can be resubmitted as new requests with new ticket
    # IDs.
    status: typing.Union[str, "MatchmakingConfigurationStatus"
                        ] = dataclasses.field(
                            default=ShapeBase.NOT_SET,
                        )

    # Code to explain the current status. For example, a status reason may
    # indicate when a ticket has returned to `SEARCHING` status after a proposed
    # match fails to receive player acceptances.
    status_reason: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Additional information about the current status.
    status_message: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Time stamp indicating when this matchmaking request was received. Format is
    # a number expressed in Unix time as milliseconds (for example
    # "1469498468.057").
    start_time: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Time stamp indicating when this matchmaking request stopped being processed
    # due to success, failure, or cancellation. Format is a number expressed in
    # Unix time as milliseconds (for example "1469498468.057").
    end_time: datetime.datetime = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A set of `Player` objects, each representing a player to find matches for.
    # Players are identified by a unique player ID and may include latency data
    # for use during matchmaking. If the ticket is in status `COMPLETED`, the
    # `Player` objects include the team the players were assigned to in the
    # resulting match.
    players: typing.List["Player"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Identifier and connection information of the game session created for the
    # match. This information is added to the ticket only after the matchmaking
    # request has been successfully completed.
    game_session_connection_info: "GameSessionConnectionInfo" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Average amount of time (in seconds) that players are currently waiting for
    # a match. If there is not enough recent data, this property may be empty.
    estimated_wait_time: int = dataclasses.field(default=ShapeBase.NOT_SET, )


class MetricName(str):
    ActivatingGameSessions = "ActivatingGameSessions"
    ActiveGameSessions = "ActiveGameSessions"
    ActiveInstances = "ActiveInstances"
    AvailableGameSessions = "AvailableGameSessions"
    AvailablePlayerSessions = "AvailablePlayerSessions"
    CurrentPlayerSessions = "CurrentPlayerSessions"
    IdleInstances = "IdleInstances"
    PercentAvailableGameSessions = "PercentAvailableGameSessions"
    PercentIdleInstances = "PercentIdleInstances"
    QueueDepth = "QueueDepth"
    WaitTime = "WaitTime"


@dataclasses.dataclass
class NotFoundException(ShapeBase):
    """
    A service resource associated with the request could not be found. Clients
    should not retry such requests.
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


class OperatingSystem(str):
    WINDOWS_2012 = "WINDOWS_2012"
    AMAZON_LINUX = "AMAZON_LINUX"


@dataclasses.dataclass
class PlacedPlayerSession(ShapeBase):
    """
    Information about a player session that was created as part of a
    StartGameSessionPlacement request. This object contains only the player ID and
    player session ID. To retrieve full details on a player session, call
    DescribePlayerSessions with the player session ID.

    Player-session-related operations include:

      * CreatePlayerSession

      * CreatePlayerSessions

      * DescribePlayerSessions

      * Game session placements

        * StartGameSessionPlacement

        * DescribeGameSessionPlacement

        * StopGameSessionPlacement
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "player_id",
                "PlayerId",
                TypeInfo(str),
            ),
            (
                "player_session_id",
                "PlayerSessionId",
                TypeInfo(str),
            ),
        ]

    # Unique identifier for a player that is associated with this player session.
    player_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Unique identifier for a player session.
    player_session_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class Player(ShapeBase):
    """
    Represents a player in matchmaking. When starting a matchmaking request, a
    player has a player ID, attributes, and may have latency data. Team information
    is added after a match has been successfully completed.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "player_id",
                "PlayerId",
                TypeInfo(str),
            ),
            (
                "player_attributes",
                "PlayerAttributes",
                TypeInfo(typing.Dict[str, AttributeValue]),
            ),
            (
                "team",
                "Team",
                TypeInfo(str),
            ),
            (
                "latency_in_ms",
                "LatencyInMs",
                TypeInfo(typing.Dict[str, int]),
            ),
        ]

    # Unique identifier for a player
    player_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Collection of key:value pairs containing player information for use in
    # matchmaking. Player attribute keys must match the _playerAttributes_ used
    # in a matchmaking rule set. Example: `"PlayerAttributes": {"skill": {"N":
    # "23"}, "gameMode": {"S": "deathmatch"}}`.
    player_attributes: typing.Dict[str, "AttributeValue"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Name of the team that the player is assigned to in a match. Team names are
    # defined in a matchmaking rule set.
    team: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Set of values, expressed in milliseconds, indicating the amount of latency
    # that a player experiences when connected to AWS regions. If this property
    # is present, FlexMatch considers placing the match only in regions for which
    # latency is reported.

    # If a matchmaker has a rule that evaluates player latency, players must
    # report latency in order to be matched. If no latency is reported in this
    # scenario, FlexMatch assumes that no regions are available to the player and
    # the ticket is not matchable.
    latency_in_ms: typing.Dict[str, int] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class PlayerLatency(ShapeBase):
    """
    Regional latency information for a player, used when requesting a new game
    session with StartGameSessionPlacement. This value indicates the amount of time
    lag that exists when the player is connected to a fleet in the specified region.
    The relative difference between a player's latency values for multiple regions
    are used to determine which fleets are best suited to place a new game session
    for the player.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "player_id",
                "PlayerId",
                TypeInfo(str),
            ),
            (
                "region_identifier",
                "RegionIdentifier",
                TypeInfo(str),
            ),
            (
                "latency_in_milliseconds",
                "LatencyInMilliseconds",
                TypeInfo(float),
            ),
        ]

    # Unique identifier for a player associated with the latency data.
    player_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Name of the region that is associated with the latency value.
    region_identifier: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Amount of time that represents the time lag experienced by the player when
    # connected to the specified region.
    latency_in_milliseconds: float = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class PlayerLatencyPolicy(ShapeBase):
    """
    Queue setting that determines the highest latency allowed for individual players
    when placing a game session. When a latency policy is in force, a game session
    cannot be placed at any destination in a region where a player is reporting
    latency higher than the cap. Latency policies are only enforced when the
    placement request contains player latency information.

    Queue-related operations include:

      * CreateGameSessionQueue

      * DescribeGameSessionQueues

      * UpdateGameSessionQueue

      * DeleteGameSessionQueue
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "maximum_individual_player_latency_milliseconds",
                "MaximumIndividualPlayerLatencyMilliseconds",
                TypeInfo(int),
            ),
            (
                "policy_duration_seconds",
                "PolicyDurationSeconds",
                TypeInfo(int),
            ),
        ]

    # The maximum latency value that is allowed for any player, in milliseconds.
    # All policies must have a value set for this property.
    maximum_individual_player_latency_milliseconds: int = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The length of time, in seconds, that the policy is enforced while placing a
    # new game session. A null value for this property means that the policy is
    # enforced until the queue times out.
    policy_duration_seconds: int = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class PlayerSession(ShapeBase):
    """
    Properties describing a player session. Player session objects are created
    either by creating a player session for a specific game session, or as part of a
    game session placement. A player session represents either a player reservation
    for a game session (status `RESERVED`) or actual player activity in a game
    session (status `ACTIVE`). A player session object (including player data) is
    automatically passed to a game session when the player connects to the game
    session and is validated.

    When a player disconnects, the player session status changes to `COMPLETED`.
    Once the session ends, the player session object is retained for 30 days and
    then removed.

    Player-session-related operations include:

      * CreatePlayerSession

      * CreatePlayerSessions

      * DescribePlayerSessions

      * Game session placements

        * StartGameSessionPlacement

        * DescribeGameSessionPlacement

        * StopGameSessionPlacement
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "player_session_id",
                "PlayerSessionId",
                TypeInfo(str),
            ),
            (
                "player_id",
                "PlayerId",
                TypeInfo(str),
            ),
            (
                "game_session_id",
                "GameSessionId",
                TypeInfo(str),
            ),
            (
                "fleet_id",
                "FleetId",
                TypeInfo(str),
            ),
            (
                "creation_time",
                "CreationTime",
                TypeInfo(datetime.datetime),
            ),
            (
                "termination_time",
                "TerminationTime",
                TypeInfo(datetime.datetime),
            ),
            (
                "status",
                "Status",
                TypeInfo(typing.Union[str, PlayerSessionStatus]),
            ),
            (
                "ip_address",
                "IpAddress",
                TypeInfo(str),
            ),
            (
                "port",
                "Port",
                TypeInfo(int),
            ),
            (
                "player_data",
                "PlayerData",
                TypeInfo(str),
            ),
        ]

    # Unique identifier for a player session.
    player_session_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Unique identifier for a player that is associated with this player session.
    player_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Unique identifier for the game session that the player session is connected
    # to.
    game_session_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Unique identifier for a fleet that the player's game session is running on.
    fleet_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Time stamp indicating when this data object was created. Format is a number
    # expressed in Unix time as milliseconds (for example "1469498468.057").
    creation_time: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Time stamp indicating when this data object was terminated. Format is a
    # number expressed in Unix time as milliseconds (for example
    # "1469498468.057").
    termination_time: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Current status of the player session.

    # Possible player session statuses include the following:

    #   * **RESERVED** \-- The player session request has been received, but the player has not yet connected to the server process and/or been validated.

    #   * **ACTIVE** \-- The player has been validated by the server process and is currently connected.

    #   * **COMPLETED** \-- The player connection has been dropped.

    #   * **TIMEDOUT** \-- A player session request was received, but the player did not connect and/or was not validated within the timeout limit (60 seconds).
    status: typing.Union[str, "PlayerSessionStatus"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # IP address of the game session. To connect to a Amazon GameLift game
    # server, an app needs both the IP address and port number.
    ip_address: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Port number for the game session. To connect to a Amazon GameLift server
    # process, an app needs both the IP address and port number.
    port: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Developer-defined information related to a player. Amazon GameLift does not
    # use this data, so it can be formatted as needed for use in the game.
    player_data: str = dataclasses.field(default=ShapeBase.NOT_SET, )


class PlayerSessionCreationPolicy(str):
    ACCEPT_ALL = "ACCEPT_ALL"
    DENY_ALL = "DENY_ALL"


class PlayerSessionStatus(str):
    RESERVED = "RESERVED"
    ACTIVE = "ACTIVE"
    COMPLETED = "COMPLETED"
    TIMEDOUT = "TIMEDOUT"


class PolicyType(str):
    RuleBased = "RuleBased"
    TargetBased = "TargetBased"


class ProtectionPolicy(str):
    NoProtection = "NoProtection"
    FullProtection = "FullProtection"


@dataclasses.dataclass
class PutScalingPolicyInput(ShapeBase):
    """
    Represents the input for a request action.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "name",
                "Name",
                TypeInfo(str),
            ),
            (
                "fleet_id",
                "FleetId",
                TypeInfo(str),
            ),
            (
                "metric_name",
                "MetricName",
                TypeInfo(typing.Union[str, MetricName]),
            ),
            (
                "scaling_adjustment",
                "ScalingAdjustment",
                TypeInfo(int),
            ),
            (
                "scaling_adjustment_type",
                "ScalingAdjustmentType",
                TypeInfo(typing.Union[str, ScalingAdjustmentType]),
            ),
            (
                "threshold",
                "Threshold",
                TypeInfo(float),
            ),
            (
                "comparison_operator",
                "ComparisonOperator",
                TypeInfo(typing.Union[str, ComparisonOperatorType]),
            ),
            (
                "evaluation_periods",
                "EvaluationPeriods",
                TypeInfo(int),
            ),
            (
                "policy_type",
                "PolicyType",
                TypeInfo(typing.Union[str, PolicyType]),
            ),
            (
                "target_configuration",
                "TargetConfiguration",
                TypeInfo(TargetConfiguration),
            ),
        ]

    # Descriptive label that is associated with a scaling policy. Policy names do
    # not need to be unique. A fleet can have only one scaling policy with the
    # same name.
    name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Unique identifier for a fleet to apply this policy to. The fleet cannot be
    # in any of the following statuses: ERROR or DELETING.
    fleet_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Name of the Amazon GameLift-defined metric that is used to trigger a
    # scaling adjustment. For detailed descriptions of fleet metrics, see
    # [Monitor Amazon GameLift with Amazon
    # CloudWatch](http://docs.aws.amazon.com/gamelift/latest/developerguide/monitoring-
    # cloudwatch.html).

    #   * **ActivatingGameSessions** \-- Game sessions in the process of being created.

    #   * **ActiveGameSessions** \-- Game sessions that are currently running.

    #   * **ActiveInstances** \-- Fleet instances that are currently running at least one game session.

    #   * **AvailableGameSessions** \-- Additional game sessions that fleet could host simultaneously, given current capacity.

    #   * **AvailablePlayerSessions** \-- Empty player slots in currently active game sessions. This includes game sessions that are not currently accepting players. Reserved player slots are not included.

    #   * **CurrentPlayerSessions** \-- Player slots in active game sessions that are being used by a player or are reserved for a player.

    #   * **IdleInstances** \-- Active instances that are currently hosting zero game sessions.

    #   * **PercentAvailableGameSessions** \-- Unused percentage of the total number of game sessions that a fleet could host simultaneously, given current capacity. Use this metric for a target-based scaling policy.

    #   * **PercentIdleInstances** \-- Percentage of the total number of active instances that are hosting zero game sessions.

    #   * **QueueDepth** \-- Pending game session placement requests, in any queue, where the current fleet is the top-priority destination.

    #   * **WaitTime** \-- Current wait time for pending game session placement requests, in any queue, where the current fleet is the top-priority destination.
    metric_name: typing.Union[str, "MetricName"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Amount of adjustment to make, based on the scaling adjustment type.
    scaling_adjustment: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Type of adjustment to make to a fleet's instance count (see FleetCapacity):

    #   * **ChangeInCapacity** \-- add (or subtract) the scaling adjustment value from the current instance count. Positive values scale up while negative values scale down.

    #   * **ExactCapacity** \-- set the instance count to the scaling adjustment value.

    #   * **PercentChangeInCapacity** \-- increase or reduce the current instance count by the scaling adjustment, read as a percentage. Positive values scale up while negative values scale down; for example, a value of "-10" scales the fleet down by 10%.
    scaling_adjustment_type: typing.Union[str, "ScalingAdjustmentType"
                                         ] = dataclasses.field(
                                             default=ShapeBase.NOT_SET,
                                         )

    # Metric value used to trigger a scaling event.
    threshold: float = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Comparison operator to use when measuring the metric against the threshold
    # value.
    comparison_operator: typing.Union[str, "ComparisonOperatorType"
                                     ] = dataclasses.field(
                                         default=ShapeBase.NOT_SET,
                                     )

    # Length of time (in minutes) the metric must be at or beyond the threshold
    # before a scaling event is triggered.
    evaluation_periods: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Type of scaling policy to create. For a target-based policy, set the
    # parameter _MetricName_ to 'PercentAvailableGameSessions' and specify a
    # _TargetConfiguration_. For a rule-based policy set the following
    # parameters: _MetricName_ , _ComparisonOperator_ , _Threshold_ ,
    # _EvaluationPeriods_ , _ScalingAdjustmentType_ , and _ScalingAdjustment_.
    policy_type: typing.Union[str, "PolicyType"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Object that contains settings for a target-based scaling policy.
    target_configuration: "TargetConfiguration" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class PutScalingPolicyOutput(OutputShapeBase):
    """
    Represents the returned data in response to a request action.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "name",
                "Name",
                TypeInfo(str),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Descriptive label that is associated with a scaling policy. Policy names do
    # not need to be unique.
    name: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class RequestUploadCredentialsInput(ShapeBase):
    """
    Represents the input for a request action.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "build_id",
                "BuildId",
                TypeInfo(str),
            ),
        ]

    # Unique identifier for a build to get credentials for.
    build_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class RequestUploadCredentialsOutput(OutputShapeBase):
    """
    Represents the returned data in response to a request action.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "upload_credentials",
                "UploadCredentials",
                TypeInfo(AwsCredentials),
            ),
            (
                "storage_location",
                "StorageLocation",
                TypeInfo(S3Location),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # AWS credentials required when uploading a game build to the storage
    # location. These credentials have a limited lifespan and are valid only for
    # the build they were issued for.
    upload_credentials: "AwsCredentials" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Amazon S3 path and key, identifying where the game build files are stored.
    storage_location: "S3Location" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class ResolveAliasInput(ShapeBase):
    """
    Represents the input for a request action.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "alias_id",
                "AliasId",
                TypeInfo(str),
            ),
        ]

    # Unique identifier for the alias you want to resolve.
    alias_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ResolveAliasOutput(OutputShapeBase):
    """
    Represents the returned data in response to a request action.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "fleet_id",
                "FleetId",
                TypeInfo(str),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Fleet identifier that is associated with the requested alias.
    fleet_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ResourceCreationLimitPolicy(ShapeBase):
    """
    Policy that limits the number of game sessions a player can create on the same
    fleet. This optional policy gives game owners control over how players can
    consume available game server resources. A resource creation policy makes the
    following statement: "An individual player can create a maximum number of new
    game sessions within a specified time period".

    The policy is evaluated when a player tries to create a new game session. For
    example, with a policy of 10 new game sessions and a time period of 60 minutes,
    on receiving a `CreateGameSession` request, Amazon GameLift checks that the
    player (identified by `CreatorId`) has created fewer than 10 game sessions in
    the past 60 minutes.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "new_game_sessions_per_creator",
                "NewGameSessionsPerCreator",
                TypeInfo(int),
            ),
            (
                "policy_period_in_minutes",
                "PolicyPeriodInMinutes",
                TypeInfo(int),
            ),
        ]

    # Maximum number of game sessions that an individual can create during the
    # policy period.
    new_game_sessions_per_creator: int = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Time span used in evaluating the resource creation limit policy.
    policy_period_in_minutes: int = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class RoutingStrategy(ShapeBase):
    """
    Routing configuration for a fleet alias.

    Fleet-related operations include:

      * CreateFleet

      * ListFleets

      * DeleteFleet

      * Describe fleets:

        * DescribeFleetAttributes

        * DescribeFleetCapacity

        * DescribeFleetPortSettings

        * DescribeFleetUtilization

        * DescribeRuntimeConfiguration

        * DescribeEC2InstanceLimits

        * DescribeFleetEvents

      * Update fleets:

        * UpdateFleetAttributes

        * UpdateFleetCapacity

        * UpdateFleetPortSettings

        * UpdateRuntimeConfiguration

      * Manage fleet actions:

        * StartFleetActions

        * StopFleetActions
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "type",
                "Type",
                TypeInfo(typing.Union[str, RoutingStrategyType]),
            ),
            (
                "fleet_id",
                "FleetId",
                TypeInfo(str),
            ),
            (
                "message",
                "Message",
                TypeInfo(str),
            ),
        ]

    # Type of routing strategy.

    # Possible routing types include the following:

    #   * **SIMPLE** \-- The alias resolves to one specific fleet. Use this type when routing to active fleets.

    #   * **TERMINAL** \-- The alias does not resolve to a fleet but instead can be used to display a message to the user. A terminal alias throws a TerminalRoutingStrategyException with the RoutingStrategy message embedded.
    type: typing.Union[str, "RoutingStrategyType"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Unique identifier for a fleet that the alias points to.
    fleet_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Message text to be used with a terminal routing strategy.
    message: str = dataclasses.field(default=ShapeBase.NOT_SET, )


class RoutingStrategyType(str):
    SIMPLE = "SIMPLE"
    TERMINAL = "TERMINAL"


@dataclasses.dataclass
class RuntimeConfiguration(ShapeBase):
    """
    A collection of server process configurations that describe what processes to
    run on each instance in a fleet. All fleets must have a run-time configuration.
    Each instance in the fleet launches the server processes specified in the run-
    time configuration and launches new ones as existing processes end. Each
    instance regularly checks for an updated run-time configuration and follows the
    new instructions.

    The run-time configuration enables the instances in a fleet to run multiple
    processes simultaneously. Potential scenarios are as follows: (1) Run multiple
    processes of a single game server executable to maximize usage of your hosting
    resources. (2) Run one or more processes of different build executables, such as
    your game server executable and a related program, or two or more different
    versions of a game server. (3) Run multiple processes of a single game server
    but with different launch parameters, for example to run one process on each
    instance in debug mode.

    A Amazon GameLift instance is limited to 50 processes running simultaneously. A
    run-time configuration must specify fewer than this limit. To calculate the
    total number of processes specified in a run-time configuration, add the values
    of the `ConcurrentExecutions` parameter for each ` ServerProcess ` object in the
    run-time configuration.

    Fleet-related operations include:

      * CreateFleet

      * ListFleets

      * DeleteFleet

      * Describe fleets:

        * DescribeFleetAttributes

        * DescribeFleetCapacity

        * DescribeFleetPortSettings

        * DescribeFleetUtilization

        * DescribeRuntimeConfiguration

        * DescribeEC2InstanceLimits

        * DescribeFleetEvents

      * Update fleets:

        * UpdateFleetAttributes

        * UpdateFleetCapacity

        * UpdateFleetPortSettings

        * UpdateRuntimeConfiguration

      * Manage fleet actions:

        * StartFleetActions

        * StopFleetActions
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "server_processes",
                "ServerProcesses",
                TypeInfo(typing.List[ServerProcess]),
            ),
            (
                "max_concurrent_game_session_activations",
                "MaxConcurrentGameSessionActivations",
                TypeInfo(int),
            ),
            (
                "game_session_activation_timeout_seconds",
                "GameSessionActivationTimeoutSeconds",
                TypeInfo(int),
            ),
        ]

    # Collection of server process configurations that describe which server
    # processes to run on each instance in a fleet.
    server_processes: typing.List["ServerProcess"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Maximum number of game sessions with status `ACTIVATING` to allow on an
    # instance simultaneously. This setting limits the amount of instance
    # resources that can be used for new game activations at any one time.
    max_concurrent_game_session_activations: int = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Maximum amount of time (in seconds) that a game session can remain in
    # status `ACTIVATING`. If the game session is not active before the timeout,
    # activation is terminated and the game session status is changed to
    # `TERMINATED`.
    game_session_activation_timeout_seconds: int = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class S3Location(ShapeBase):
    """
    Location in Amazon Simple Storage Service (Amazon S3) where build files can be
    stored for access by Amazon GameLift. This location is specified in a
    CreateBuild request. For more details, see the [Create a Build with Files in
    Amazon S3](http://docs.aws.amazon.com/gamelift/latest/developerguide/gamelift-
    build-cli-uploading.html#gamelift-build-cli-uploading-create-build).
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "bucket",
                "Bucket",
                TypeInfo(str),
            ),
            (
                "key",
                "Key",
                TypeInfo(str),
            ),
            (
                "role_arn",
                "RoleArn",
                TypeInfo(str),
            ),
        ]

    # Amazon S3 bucket identifier. This is the name of your S3 bucket.
    bucket: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Name of the zip file containing your build files.
    key: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Amazon Resource Name
    # ([ARN](http://docs.aws.amazon.com/AmazonS3/latest/dev/s3-arn-format.html))
    # for the access role that allows Amazon GameLift to access your S3 bucket.
    role_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )


class ScalingAdjustmentType(str):
    ChangeInCapacity = "ChangeInCapacity"
    ExactCapacity = "ExactCapacity"
    PercentChangeInCapacity = "PercentChangeInCapacity"


@dataclasses.dataclass
class ScalingPolicy(ShapeBase):
    """
    Rule that controls how a fleet is scaled. Scaling policies are uniquely
    identified by the combination of name and fleet ID.

    Operations related to fleet capacity scaling include:

      * DescribeFleetCapacity

      * UpdateFleetCapacity

      * DescribeEC2InstanceLimits

      * Manage scaling policies:

        * PutScalingPolicy (auto-scaling)

        * DescribeScalingPolicies (auto-scaling)

        * DeleteScalingPolicy (auto-scaling)

      * Manage fleet actions:

        * StartFleetActions

        * StopFleetActions
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "fleet_id",
                "FleetId",
                TypeInfo(str),
            ),
            (
                "name",
                "Name",
                TypeInfo(str),
            ),
            (
                "status",
                "Status",
                TypeInfo(typing.Union[str, ScalingStatusType]),
            ),
            (
                "scaling_adjustment",
                "ScalingAdjustment",
                TypeInfo(int),
            ),
            (
                "scaling_adjustment_type",
                "ScalingAdjustmentType",
                TypeInfo(typing.Union[str, ScalingAdjustmentType]),
            ),
            (
                "comparison_operator",
                "ComparisonOperator",
                TypeInfo(typing.Union[str, ComparisonOperatorType]),
            ),
            (
                "threshold",
                "Threshold",
                TypeInfo(float),
            ),
            (
                "evaluation_periods",
                "EvaluationPeriods",
                TypeInfo(int),
            ),
            (
                "metric_name",
                "MetricName",
                TypeInfo(typing.Union[str, MetricName]),
            ),
            (
                "policy_type",
                "PolicyType",
                TypeInfo(typing.Union[str, PolicyType]),
            ),
            (
                "target_configuration",
                "TargetConfiguration",
                TypeInfo(TargetConfiguration),
            ),
        ]

    # Unique identifier for a fleet that is associated with this scaling policy.
    fleet_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Descriptive label that is associated with a scaling policy. Policy names do
    # not need to be unique.
    name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Current status of the scaling policy. The scaling policy can be in force
    # only when in an `ACTIVE` status. Scaling policies can be suspended for
    # individual fleets (see StopFleetActions; if suspended for a fleet, the
    # policy status does not change. View a fleet's stopped actions by calling
    # DescribeFleetCapacity.

    #   * **ACTIVE** \-- The scaling policy can be used for auto-scaling a fleet.

    #   * **UPDATE_REQUESTED** \-- A request to update the scaling policy has been received.

    #   * **UPDATING** \-- A change is being made to the scaling policy.

    #   * **DELETE_REQUESTED** \-- A request to delete the scaling policy has been received.

    #   * **DELETING** \-- The scaling policy is being deleted.

    #   * **DELETED** \-- The scaling policy has been deleted.

    #   * **ERROR** \-- An error occurred in creating the policy. It should be removed and recreated.
    status: typing.Union[str, "ScalingStatusType"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Amount of adjustment to make, based on the scaling adjustment type.
    scaling_adjustment: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Type of adjustment to make to a fleet's instance count (see FleetCapacity):

    #   * **ChangeInCapacity** \-- add (or subtract) the scaling adjustment value from the current instance count. Positive values scale up while negative values scale down.

    #   * **ExactCapacity** \-- set the instance count to the scaling adjustment value.

    #   * **PercentChangeInCapacity** \-- increase or reduce the current instance count by the scaling adjustment, read as a percentage. Positive values scale up while negative values scale down.
    scaling_adjustment_type: typing.Union[str, "ScalingAdjustmentType"
                                         ] = dataclasses.field(
                                             default=ShapeBase.NOT_SET,
                                         )

    # Comparison operator to use when measuring a metric against the threshold
    # value.
    comparison_operator: typing.Union[str, "ComparisonOperatorType"
                                     ] = dataclasses.field(
                                         default=ShapeBase.NOT_SET,
                                     )

    # Metric value used to trigger a scaling event.
    threshold: float = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Length of time (in minutes) the metric must be at or beyond the threshold
    # before a scaling event is triggered.
    evaluation_periods: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Name of the Amazon GameLift-defined metric that is used to trigger a
    # scaling adjustment. For detailed descriptions of fleet metrics, see
    # [Monitor Amazon GameLift with Amazon
    # CloudWatch](http://docs.aws.amazon.com/gamelift/latest/developerguide/monitoring-
    # cloudwatch.html).

    #   * **ActivatingGameSessions** \-- Game sessions in the process of being created.

    #   * **ActiveGameSessions** \-- Game sessions that are currently running.

    #   * **ActiveInstances** \-- Fleet instances that are currently running at least one game session.

    #   * **AvailableGameSessions** \-- Additional game sessions that fleet could host simultaneously, given current capacity.

    #   * **AvailablePlayerSessions** \-- Empty player slots in currently active game sessions. This includes game sessions that are not currently accepting players. Reserved player slots are not included.

    #   * **CurrentPlayerSessions** \-- Player slots in active game sessions that are being used by a player or are reserved for a player.

    #   * **IdleInstances** \-- Active instances that are currently hosting zero game sessions.

    #   * **PercentAvailableGameSessions** \-- Unused percentage of the total number of game sessions that a fleet could host simultaneously, given current capacity. Use this metric for a target-based scaling policy.

    #   * **PercentIdleInstances** \-- Percentage of the total number of active instances that are hosting zero game sessions.

    #   * **QueueDepth** \-- Pending game session placement requests, in any queue, where the current fleet is the top-priority destination.

    #   * **WaitTime** \-- Current wait time for pending game session placement requests, in any queue, where the current fleet is the top-priority destination.
    metric_name: typing.Union[str, "MetricName"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Type of scaling policy to create. For a target-based policy, set the
    # parameter _MetricName_ to 'PercentAvailableGameSessions' and specify a
    # _TargetConfiguration_. For a rule-based policy set the following
    # parameters: _MetricName_ , _ComparisonOperator_ , _Threshold_ ,
    # _EvaluationPeriods_ , _ScalingAdjustmentType_ , and _ScalingAdjustment_.
    policy_type: typing.Union[str, "PolicyType"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Object that contains settings for a target-based scaling policy.
    target_configuration: "TargetConfiguration" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


class ScalingStatusType(str):
    ACTIVE = "ACTIVE"
    UPDATE_REQUESTED = "UPDATE_REQUESTED"
    UPDATING = "UPDATING"
    DELETE_REQUESTED = "DELETE_REQUESTED"
    DELETING = "DELETING"
    DELETED = "DELETED"
    ERROR = "ERROR"


@dataclasses.dataclass
class SearchGameSessionsInput(ShapeBase):
    """
    Represents the input for a request action.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "fleet_id",
                "FleetId",
                TypeInfo(str),
            ),
            (
                "alias_id",
                "AliasId",
                TypeInfo(str),
            ),
            (
                "filter_expression",
                "FilterExpression",
                TypeInfo(str),
            ),
            (
                "sort_expression",
                "SortExpression",
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

    # Unique identifier for a fleet to search for active game sessions. Each
    # request must reference either a fleet ID or alias ID, but not both.
    fleet_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Unique identifier for an alias associated with the fleet to search for
    # active game sessions. Each request must reference either a fleet ID or
    # alias ID, but not both.
    alias_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # String containing the search criteria for the session search. If no filter
    # expression is included, the request returns results for all game sessions
    # in the fleet that are in `ACTIVE` status.

    # A filter expression can contain one or multiple conditions. Each condition
    # consists of the following:

    #   * **Operand** \-- Name of a game session attribute. Valid values are `gameSessionName`, `gameSessionId`, `gameSessionProperties`, `maximumSessions`, `creationTimeMillis`, `playerSessionCount`, `hasAvailablePlayerSessions`.

    #   * **Comparator** \-- Valid comparators are: `=`, `<>`, `<`, `>`, `<=`, `>=`.

    #   * **Value** \-- Value to be searched for. Values may be numbers, boolean values (true/false) or strings depending on the operand. String values are case sensitive and must be enclosed in single quotes. Special characters must be escaped. Boolean and string values can only be used with the comparators `=` and `<>`. For example, the following filter expression searches on `gameSessionName`: "`FilterExpression": "gameSessionName = 'Matt\\'s Awesome Game 1'"`.

    # To chain multiple conditions in a single expression, use the logical
    # keywords `AND`, `OR`, and `NOT` and parentheses as needed. For example: `x
    # AND y AND NOT z`, `NOT (x OR y)`.

    # Session search evaluates conditions from left to right using the following
    # precedence rules:

    #   1. `=`, `<>`, `<`, `>`, `<=`, `>=`

    #   2. Parentheses

    #   3. NOT

    #   4. AND

    #   5. OR

    # For example, this filter expression retrieves game sessions hosting at
    # least ten players that have an open player slot: `"maximumSessions>=10 AND
    # hasAvailablePlayerSessions=true"`.
    filter_expression: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Instructions on how to sort the search results. If no sort expression is
    # included, the request returns results in random order. A sort expression
    # consists of the following elements:

    #   * **Operand** \-- Name of a game session attribute. Valid values are `gameSessionName`, `gameSessionId`, `gameSessionProperties`, `maximumSessions`, `creationTimeMillis`, `playerSessionCount`, `hasAvailablePlayerSessions`.

    #   * **Order** \-- Valid sort orders are `ASC` (ascending) and `DESC` (descending).

    # For example, this sort expression returns the oldest active sessions first:
    # `"SortExpression": "creationTimeMillis ASC"`. Results with a null value for
    # the sort operand are returned at the end of the list.
    sort_expression: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Maximum number of results to return. Use this parameter with `NextToken` to
    # get results as a set of sequential pages. The maximum number of results
    # returned is 20, even if this value is not set or is set higher than 20.
    limit: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Token that indicates the start of the next sequential page of results. Use
    # the token that is returned with a previous call to this action. To start at
    # the beginning of the result set, do not specify a value.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class SearchGameSessionsOutput(OutputShapeBase):
    """
    Represents the returned data in response to a request action.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "game_sessions",
                "GameSessions",
                TypeInfo(typing.List[GameSession]),
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

    # Collection of objects containing game session properties for each session
    # matching the request.
    game_sessions: typing.List["GameSession"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Token that indicates where to resume retrieving results on the next call to
    # this action. If no token is returned, these results represent the end of
    # the list.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ServerProcess(ShapeBase):
    """
    A set of instructions for launching server processes on each instance in a
    fleet. Each instruction set identifies the location of the server executable,
    optional launch parameters, and the number of server processes with this
    configuration to maintain concurrently on the instance. Server process
    configurations make up a fleet's ` RuntimeConfiguration `.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "launch_path",
                "LaunchPath",
                TypeInfo(str),
            ),
            (
                "concurrent_executions",
                "ConcurrentExecutions",
                TypeInfo(int),
            ),
            (
                "parameters",
                "Parameters",
                TypeInfo(str),
            ),
        ]

    # Location of the server executable in a game build. All game builds are
    # installed on instances at the root : for Windows instances `C:\game`, and
    # for Linux instances `/local/game`. A Windows game build with an executable
    # file located at `MyGame\latest\server.exe` must have a launch path of
    # "`C:\game\MyGame\latest\server.exe`". A Linux game build with an executable
    # file located at `MyGame/latest/server.exe` must have a launch path of
    # "`/local/game/MyGame/latest/server.exe`".
    launch_path: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Number of server processes using this configuration to run concurrently on
    # an instance.
    concurrent_executions: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Optional list of parameters to pass to the server executable on launch.
    parameters: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class StartFleetActionsInput(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "fleet_id",
                "FleetId",
                TypeInfo(str),
            ),
            (
                "actions",
                "Actions",
                TypeInfo(typing.List[typing.Union[str, FleetAction]]),
            ),
        ]

    # Unique identifier for a fleet
    fleet_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # List of actions to restart on the fleet.
    actions: typing.List[typing.Union[str, "FleetAction"]] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class StartFleetActionsOutput(OutputShapeBase):
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
class StartGameSessionPlacementInput(ShapeBase):
    """
    Represents the input for a request action.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "placement_id",
                "PlacementId",
                TypeInfo(str),
            ),
            (
                "game_session_queue_name",
                "GameSessionQueueName",
                TypeInfo(str),
            ),
            (
                "maximum_player_session_count",
                "MaximumPlayerSessionCount",
                TypeInfo(int),
            ),
            (
                "game_properties",
                "GameProperties",
                TypeInfo(typing.List[GameProperty]),
            ),
            (
                "game_session_name",
                "GameSessionName",
                TypeInfo(str),
            ),
            (
                "player_latencies",
                "PlayerLatencies",
                TypeInfo(typing.List[PlayerLatency]),
            ),
            (
                "desired_player_sessions",
                "DesiredPlayerSessions",
                TypeInfo(typing.List[DesiredPlayerSession]),
            ),
            (
                "game_session_data",
                "GameSessionData",
                TypeInfo(str),
            ),
        ]

    # Unique identifier to assign to the new game session placement. This value
    # is developer-defined. The value must be unique across all regions and
    # cannot be reused unless you are resubmitting a canceled or timed-out
    # placement request.
    placement_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Name of the queue to use to place the new game session.
    game_session_queue_name: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Maximum number of players that can be connected simultaneously to the game
    # session.
    maximum_player_session_count: int = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Set of custom properties for a game session, formatted as key:value pairs.
    # These properties are passed to a game server process in the GameSession
    # object with a request to start a new game session (see [Start a Game
    # Session](http://docs.aws.amazon.com/gamelift/latest/developerguide/gamelift-
    # sdk-server-api.html#gamelift-sdk-server-startsession)).
    game_properties: typing.List["GameProperty"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Descriptive label that is associated with a game session. Session names do
    # not need to be unique.
    game_session_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Set of values, expressed in milliseconds, indicating the amount of latency
    # that a player experiences when connected to AWS regions. This information
    # is used to try to place the new game session where it can offer the best
    # possible gameplay experience for the players.
    player_latencies: typing.List["PlayerLatency"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Set of information on each player to create a player session for.
    desired_player_sessions: typing.List["DesiredPlayerSession"
                                        ] = dataclasses.field(
                                            default=ShapeBase.NOT_SET,
                                        )

    # Set of custom game session properties, formatted as a single string value.
    # This data is passed to a game server process in the GameSession object with
    # a request to start a new game session (see [Start a Game
    # Session](http://docs.aws.amazon.com/gamelift/latest/developerguide/gamelift-
    # sdk-server-api.html#gamelift-sdk-server-startsession)).
    game_session_data: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class StartGameSessionPlacementOutput(OutputShapeBase):
    """
    Represents the returned data in response to a request action.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "game_session_placement",
                "GameSessionPlacement",
                TypeInfo(GameSessionPlacement),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Object that describes the newly created game session placement. This object
    # includes all the information provided in the request, as well as start/end
    # time stamps and placement status.
    game_session_placement: "GameSessionPlacement" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class StartMatchBackfillInput(ShapeBase):
    """
    Represents the input for a request action.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "configuration_name",
                "ConfigurationName",
                TypeInfo(str),
            ),
            (
                "game_session_arn",
                "GameSessionArn",
                TypeInfo(str),
            ),
            (
                "players",
                "Players",
                TypeInfo(typing.List[Player]),
            ),
            (
                "ticket_id",
                "TicketId",
                TypeInfo(str),
            ),
        ]

    # Name of the matchmaker to use for this request. The name of the matchmaker
    # that was used with the original game session is listed in the GameSession
    # object, `MatchmakerData` property. This property contains a matchmaking
    # configuration ARN value, which includes the matchmaker name. (In the ARN
    # value "arn:aws:gamelift:us-
    # west-2:111122223333:matchmakingconfiguration/MM-4v4", the matchmaking
    # configuration name is "MM-4v4".) Use only the name for this parameter.
    configuration_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Amazon Resource Name
    # ([ARN](http://docs.aws.amazon.com/AmazonS3/latest/dev/s3-arn-format.html))
    # that is assigned to a game session and uniquely identifies it.
    game_session_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Match information on all players that are currently assigned to the game
    # session. This information is used by the matchmaker to find new players and
    # add them to the existing game.

    #   * PlayerID, PlayerAttributes, Team -\\\\- This information is maintained in the GameSession object, `MatchmakerData` property, for all players who are currently assigned to the game session. The matchmaker data is in JSON syntax, formatted as a string. For more details, see [ Match Data](http://docs.aws.amazon.com/gamelift/latest/developerguide/match-server.html#match-server-data).

    #   * LatencyInMs -\\\\- If the matchmaker uses player latency, include a latency value, in milliseconds, for the region that the game session is currently in. Do not include latency values for any other region.
    players: typing.List["Player"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Unique identifier for a matchmaking ticket. If no ticket ID is specified
    # here, Amazon GameLift will generate one in the form of a UUID. Use this
    # identifier to track the match backfill ticket status and retrieve match
    # results.
    ticket_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class StartMatchBackfillOutput(OutputShapeBase):
    """
    Represents the returned data in response to a request action.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "matchmaking_ticket",
                "MatchmakingTicket",
                TypeInfo(MatchmakingTicket),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Ticket representing the backfill matchmaking request. This object includes
    # the information in the request, ticket status, and match results as
    # generated during the matchmaking process.
    matchmaking_ticket: "MatchmakingTicket" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class StartMatchmakingInput(ShapeBase):
    """
    Represents the input for a request action.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "configuration_name",
                "ConfigurationName",
                TypeInfo(str),
            ),
            (
                "players",
                "Players",
                TypeInfo(typing.List[Player]),
            ),
            (
                "ticket_id",
                "TicketId",
                TypeInfo(str),
            ),
        ]

    # Name of the matchmaking configuration to use for this request. Matchmaking
    # configurations must exist in the same region as this request.
    configuration_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Information on each player to be matched. This information must include a
    # player ID, and may contain player attributes and latency data to be used in
    # the matchmaking process. After a successful match, `Player` objects contain
    # the name of the team the player is assigned to.
    players: typing.List["Player"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Unique identifier for a matchmaking ticket. If no ticket ID is specified
    # here, Amazon GameLift will generate one in the form of a UUID. Use this
    # identifier to track the matchmaking ticket status and retrieve match
    # results.
    ticket_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class StartMatchmakingOutput(OutputShapeBase):
    """
    Represents the returned data in response to a request action.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "matchmaking_ticket",
                "MatchmakingTicket",
                TypeInfo(MatchmakingTicket),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Ticket representing the matchmaking request. This object include the
    # information included in the request, ticket status, and match results as
    # generated during the matchmaking process.
    matchmaking_ticket: "MatchmakingTicket" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class StopFleetActionsInput(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "fleet_id",
                "FleetId",
                TypeInfo(str),
            ),
            (
                "actions",
                "Actions",
                TypeInfo(typing.List[typing.Union[str, FleetAction]]),
            ),
        ]

    # Unique identifier for a fleet
    fleet_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # List of actions to suspend on the fleet.
    actions: typing.List[typing.Union[str, "FleetAction"]] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class StopFleetActionsOutput(OutputShapeBase):
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
class StopGameSessionPlacementInput(ShapeBase):
    """
    Represents the input for a request action.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "placement_id",
                "PlacementId",
                TypeInfo(str),
            ),
        ]

    # Unique identifier for a game session placement to cancel.
    placement_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class StopGameSessionPlacementOutput(OutputShapeBase):
    """
    Represents the returned data in response to a request action.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "game_session_placement",
                "GameSessionPlacement",
                TypeInfo(GameSessionPlacement),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Object that describes the canceled game session placement, with `CANCELLED`
    # status and an end time stamp.
    game_session_placement: "GameSessionPlacement" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class StopMatchmakingInput(ShapeBase):
    """
    Represents the input for a request action.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "ticket_id",
                "TicketId",
                TypeInfo(str),
            ),
        ]

    # Unique identifier for a matchmaking ticket.
    ticket_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class StopMatchmakingOutput(OutputShapeBase):
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
class TargetConfiguration(ShapeBase):
    """
    Settings for a target-based scaling policy (see ScalingPolicy. A target-based
    policy tracks a particular fleet metric specifies a target value for the metric.
    As player usage changes, the policy triggers Amazon GameLift to adjust capacity
    so that the metric returns to the target value. The target configuration
    specifies settings as needed for the target based policy, including the target
    value.

    Operations related to fleet capacity scaling include:

      * DescribeFleetCapacity

      * UpdateFleetCapacity

      * DescribeEC2InstanceLimits

      * Manage scaling policies:

        * PutScalingPolicy (auto-scaling)

        * DescribeScalingPolicies (auto-scaling)

        * DeleteScalingPolicy (auto-scaling)

      * Manage fleet actions:

        * StartFleetActions

        * StopFleetActions
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "target_value",
                "TargetValue",
                TypeInfo(float),
            ),
        ]

    # Desired value to use with a target-based scaling policy. The value must be
    # relevant for whatever metric the scaling policy is using. For example, in a
    # policy using the metric PercentAvailableGameSessions, the target value
    # should be the preferred size of the fleet's buffer (the percent of capacity
    # that should be idle and ready for new game sessions).
    target_value: float = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class TerminalRoutingStrategyException(ShapeBase):
    """
    The service is unable to resolve the routing for a particular alias because it
    has a terminal RoutingStrategy associated with it. The message returned in this
    exception is the message defined in the routing strategy itself. Such requests
    should only be retried if the routing strategy for the specified alias is
    modified.
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
    The client failed authentication. Clients should not retry such requests.
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
class UnsupportedRegionException(ShapeBase):
    """
    The requested operation is not supported in the region specified.
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
class UpdateAliasInput(ShapeBase):
    """
    Represents the input for a request action.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "alias_id",
                "AliasId",
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
            (
                "routing_strategy",
                "RoutingStrategy",
                TypeInfo(RoutingStrategy),
            ),
        ]

    # Unique identifier for a fleet alias. Specify the alias you want to update.
    alias_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Descriptive label that is associated with an alias. Alias names do not need
    # to be unique.
    name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Human-readable description of an alias.
    description: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Object that specifies the fleet and routing type to use for the alias.
    routing_strategy: "RoutingStrategy" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class UpdateAliasOutput(OutputShapeBase):
    """
    Represents the returned data in response to a request action.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "alias",
                "Alias",
                TypeInfo(Alias),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Object that contains the updated alias configuration.
    alias: "Alias" = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class UpdateBuildInput(ShapeBase):
    """
    Represents the input for a request action.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "build_id",
                "BuildId",
                TypeInfo(str),
            ),
            (
                "name",
                "Name",
                TypeInfo(str),
            ),
            (
                "version",
                "Version",
                TypeInfo(str),
            ),
        ]

    # Unique identifier for a build to update.
    build_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Descriptive label that is associated with a build. Build names do not need
    # to be unique.
    name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Version that is associated with this build. Version strings do not need to
    # be unique.
    version: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class UpdateBuildOutput(OutputShapeBase):
    """
    Represents the returned data in response to a request action.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "build",
                "Build",
                TypeInfo(Build),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Object that contains the updated build record.
    build: "Build" = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class UpdateFleetAttributesInput(ShapeBase):
    """
    Represents the input for a request action.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "fleet_id",
                "FleetId",
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
            (
                "new_game_session_protection_policy",
                "NewGameSessionProtectionPolicy",
                TypeInfo(typing.Union[str, ProtectionPolicy]),
            ),
            (
                "resource_creation_limit_policy",
                "ResourceCreationLimitPolicy",
                TypeInfo(ResourceCreationLimitPolicy),
            ),
            (
                "metric_groups",
                "MetricGroups",
                TypeInfo(typing.List[str]),
            ),
        ]

    # Unique identifier for a fleet to update attribute metadata for.
    fleet_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Descriptive label that is associated with a fleet. Fleet names do not need
    # to be unique.
    name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Human-readable description of a fleet.
    description: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Game session protection policy to apply to all new instances created in
    # this fleet. Instances that already exist are not affected. You can set
    # protection for individual instances using UpdateGameSession.

    #   * **NoProtection** \-- The game session can be terminated during a scale-down event.

    #   * **FullProtection** \-- If the game session is in an `ACTIVE` status, it cannot be terminated during a scale-down event.
    new_game_session_protection_policy: typing.Union[
        str, "ProtectionPolicy"] = dataclasses.field(
            default=ShapeBase.NOT_SET,
        )

    # Policy that limits the number of game sessions an individual player can
    # create over a span of time.
    resource_creation_limit_policy: "ResourceCreationLimitPolicy" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Names of metric groups to include this fleet in. Amazon CloudWatch uses a
    # fleet metric group is to aggregate metrics from multiple fleets. Use an
    # existing metric group name to add this fleet to the group. Or use a new
    # name to create a new metric group. A fleet can only be included in one
    # metric group at a time.
    metric_groups: typing.List[str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class UpdateFleetAttributesOutput(OutputShapeBase):
    """
    Represents the returned data in response to a request action.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "fleet_id",
                "FleetId",
                TypeInfo(str),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Unique identifier for a fleet that was updated.
    fleet_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class UpdateFleetCapacityInput(ShapeBase):
    """
    Represents the input for a request action.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "fleet_id",
                "FleetId",
                TypeInfo(str),
            ),
            (
                "desired_instances",
                "DesiredInstances",
                TypeInfo(int),
            ),
            (
                "min_size",
                "MinSize",
                TypeInfo(int),
            ),
            (
                "max_size",
                "MaxSize",
                TypeInfo(int),
            ),
        ]

    # Unique identifier for a fleet to update capacity for.
    fleet_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Number of EC2 instances you want this fleet to host.
    desired_instances: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Minimum value allowed for the fleet's instance count. Default if not set is
    # 0.
    min_size: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Maximum value allowed for the fleet's instance count. Default if not set is
    # 1.
    max_size: int = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class UpdateFleetCapacityOutput(OutputShapeBase):
    """
    Represents the returned data in response to a request action.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "fleet_id",
                "FleetId",
                TypeInfo(str),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Unique identifier for a fleet that was updated.
    fleet_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class UpdateFleetPortSettingsInput(ShapeBase):
    """
    Represents the input for a request action.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "fleet_id",
                "FleetId",
                TypeInfo(str),
            ),
            (
                "inbound_permission_authorizations",
                "InboundPermissionAuthorizations",
                TypeInfo(typing.List[IpPermission]),
            ),
            (
                "inbound_permission_revocations",
                "InboundPermissionRevocations",
                TypeInfo(typing.List[IpPermission]),
            ),
        ]

    # Unique identifier for a fleet to update port settings for.
    fleet_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Collection of port settings to be added to the fleet record.
    inbound_permission_authorizations: typing.List["IpPermission"
                                                  ] = dataclasses.field(
                                                      default=ShapeBase.NOT_SET,
                                                  )

    # Collection of port settings to be removed from the fleet record.
    inbound_permission_revocations: typing.List["IpPermission"
                                               ] = dataclasses.field(
                                                   default=ShapeBase.NOT_SET,
                                               )


@dataclasses.dataclass
class UpdateFleetPortSettingsOutput(OutputShapeBase):
    """
    Represents the returned data in response to a request action.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "fleet_id",
                "FleetId",
                TypeInfo(str),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Unique identifier for a fleet that was updated.
    fleet_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class UpdateGameSessionInput(ShapeBase):
    """
    Represents the input for a request action.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "game_session_id",
                "GameSessionId",
                TypeInfo(str),
            ),
            (
                "maximum_player_session_count",
                "MaximumPlayerSessionCount",
                TypeInfo(int),
            ),
            (
                "name",
                "Name",
                TypeInfo(str),
            ),
            (
                "player_session_creation_policy",
                "PlayerSessionCreationPolicy",
                TypeInfo(typing.Union[str, PlayerSessionCreationPolicy]),
            ),
            (
                "protection_policy",
                "ProtectionPolicy",
                TypeInfo(typing.Union[str, ProtectionPolicy]),
            ),
        ]

    # Unique identifier for the game session to update.
    game_session_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Maximum number of players that can be connected simultaneously to the game
    # session.
    maximum_player_session_count: int = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Descriptive label that is associated with a game session. Session names do
    # not need to be unique.
    name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Policy determining whether or not the game session accepts new players.
    player_session_creation_policy: typing.Union[
        str, "PlayerSessionCreationPolicy"] = dataclasses.field(
            default=ShapeBase.NOT_SET,
        )

    # Game session protection policy to apply to this game session only.

    #   * **NoProtection** \-- The game session can be terminated during a scale-down event.

    #   * **FullProtection** \-- If the game session is in an `ACTIVE` status, it cannot be terminated during a scale-down event.
    protection_policy: typing.Union[str, "ProtectionPolicy"
                                   ] = dataclasses.field(
                                       default=ShapeBase.NOT_SET,
                                   )


@dataclasses.dataclass
class UpdateGameSessionOutput(OutputShapeBase):
    """
    Represents the returned data in response to a request action.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "game_session",
                "GameSession",
                TypeInfo(GameSession),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Object that contains the updated game session metadata.
    game_session: "GameSession" = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class UpdateGameSessionQueueInput(ShapeBase):
    """
    Represents the input for a request action.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "name",
                "Name",
                TypeInfo(str),
            ),
            (
                "timeout_in_seconds",
                "TimeoutInSeconds",
                TypeInfo(int),
            ),
            (
                "player_latency_policies",
                "PlayerLatencyPolicies",
                TypeInfo(typing.List[PlayerLatencyPolicy]),
            ),
            (
                "destinations",
                "Destinations",
                TypeInfo(typing.List[GameSessionQueueDestination]),
            ),
        ]

    # Descriptive label that is associated with game session queue. Queue names
    # must be unique within each region.
    name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Maximum time, in seconds, that a new game session placement request remains
    # in the queue. When a request exceeds this time, the game session placement
    # changes to a `TIMED_OUT` status.
    timeout_in_seconds: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Collection of latency policies to apply when processing game sessions
    # placement requests with player latency information. Multiple policies are
    # evaluated in order of the maximum latency value, starting with the lowest
    # latency values. With just one policy, it is enforced at the start of the
    # game session placement for the duration period. With multiple policies,
    # each policy is enforced consecutively for its duration period. For example,
    # a queue might enforce a 60-second policy followed by a 120-second policy,
    # and then no policy for the remainder of the placement. When updating
    # policies, provide a complete collection of policies.
    player_latency_policies: typing.List["PlayerLatencyPolicy"
                                        ] = dataclasses.field(
                                            default=ShapeBase.NOT_SET,
                                        )

    # List of fleets that can be used to fulfill game session placement requests
    # in the queue. Fleets are identified by either a fleet ARN or a fleet alias
    # ARN. Destinations are listed in default preference order. When updating
    # this list, provide a complete list of destinations.
    destinations: typing.List["GameSessionQueueDestination"
                             ] = dataclasses.field(
                                 default=ShapeBase.NOT_SET,
                             )


@dataclasses.dataclass
class UpdateGameSessionQueueOutput(OutputShapeBase):
    """
    Represents the returned data in response to a request action.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "game_session_queue",
                "GameSessionQueue",
                TypeInfo(GameSessionQueue),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Object that describes the newly updated game session queue.
    game_session_queue: "GameSessionQueue" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class UpdateMatchmakingConfigurationInput(ShapeBase):
    """
    Represents the input for a request action.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
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
            (
                "game_session_queue_arns",
                "GameSessionQueueArns",
                TypeInfo(typing.List[str]),
            ),
            (
                "request_timeout_seconds",
                "RequestTimeoutSeconds",
                TypeInfo(int),
            ),
            (
                "acceptance_timeout_seconds",
                "AcceptanceTimeoutSeconds",
                TypeInfo(int),
            ),
            (
                "acceptance_required",
                "AcceptanceRequired",
                TypeInfo(bool),
            ),
            (
                "rule_set_name",
                "RuleSetName",
                TypeInfo(str),
            ),
            (
                "notification_target",
                "NotificationTarget",
                TypeInfo(str),
            ),
            (
                "additional_player_count",
                "AdditionalPlayerCount",
                TypeInfo(int),
            ),
            (
                "custom_event_data",
                "CustomEventData",
                TypeInfo(str),
            ),
            (
                "game_properties",
                "GameProperties",
                TypeInfo(typing.List[GameProperty]),
            ),
            (
                "game_session_data",
                "GameSessionData",
                TypeInfo(str),
            ),
        ]

    # Unique identifier for a matchmaking configuration to update.
    name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Descriptive label that is associated with matchmaking configuration.
    description: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Amazon Resource Name
    # ([ARN](http://docs.aws.amazon.com/AmazonS3/latest/dev/s3-arn-format.html))
    # that is assigned to a game session queue and uniquely identifies it. Format
    # is
    # `arn:aws:gamelift:<region>::fleet/fleet-a1234567-b8c9-0d1e-2fa3-b45c6d7e8912`.
    # These queues are used when placing game sessions for matches that are
    # created with this matchmaking configuration. Queues can be located in any
    # region.
    game_session_queue_arns: typing.List[str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Maximum duration, in seconds, that a matchmaking ticket can remain in
    # process before timing out. Requests that time out can be resubmitted as
    # needed.
    request_timeout_seconds: int = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Length of time (in seconds) to wait for players to accept a proposed match.
    # If any player rejects the match or fails to accept before the timeout, the
    # ticket continues to look for an acceptable match.
    acceptance_timeout_seconds: int = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Flag that determines whether or not a match that was created with this
    # configuration must be accepted by the matched players. To require
    # acceptance, set to TRUE.
    acceptance_required: bool = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Unique identifier for a matchmaking rule set to use with this
    # configuration. A matchmaking configuration can only use rule sets that are
    # defined in the same region.
    rule_set_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # SNS topic ARN that is set up to receive matchmaking notifications. See [
    # Setting up Notifications for
    # Matchmaking](http://docs.aws.amazon.com/gamelift/latest/developerguide/match-
    # notification.html) for more information.
    notification_target: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Number of player slots in a match to keep open for future players. For
    # example, if the configuration's rule set specifies a match for a single
    # 12-person team, and the additional player count is set to 2, only 10
    # players are selected for the match.
    additional_player_count: int = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Information to attached to all events related to the matchmaking
    # configuration.
    custom_event_data: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Set of custom properties for a game session, formatted as key:value pairs.
    # These properties are passed to a game server process in the GameSession
    # object with a request to start a new game session (see [Start a Game
    # Session](http://docs.aws.amazon.com/gamelift/latest/developerguide/gamelift-
    # sdk-server-api.html#gamelift-sdk-server-startsession)). This information is
    # added to the new GameSession object that is created for a successful match.
    game_properties: typing.List["GameProperty"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Set of custom game session properties, formatted as a single string value.
    # This data is passed to a game server process in the GameSession object with
    # a request to start a new game session (see [Start a Game
    # Session](http://docs.aws.amazon.com/gamelift/latest/developerguide/gamelift-
    # sdk-server-api.html#gamelift-sdk-server-startsession)). This information is
    # added to the new GameSession object that is created for a successful match.
    game_session_data: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class UpdateMatchmakingConfigurationOutput(OutputShapeBase):
    """
    Represents the returned data in response to a request action.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "configuration",
                "Configuration",
                TypeInfo(MatchmakingConfiguration),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Object that describes the updated matchmaking configuration.
    configuration: "MatchmakingConfiguration" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class UpdateRuntimeConfigurationInput(ShapeBase):
    """
    Represents the input for a request action.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "fleet_id",
                "FleetId",
                TypeInfo(str),
            ),
            (
                "runtime_configuration",
                "RuntimeConfiguration",
                TypeInfo(RuntimeConfiguration),
            ),
        ]

    # Unique identifier for a fleet to update run-time configuration for.
    fleet_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Instructions for launching server processes on each instance in the fleet.
    # The run-time configuration for a fleet has a collection of server process
    # configurations, one for each type of server process to run on an instance.
    # A server process configuration specifies the location of the server
    # executable, launch parameters, and the number of concurrent processes with
    # that configuration to maintain on each instance.
    runtime_configuration: "RuntimeConfiguration" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class UpdateRuntimeConfigurationOutput(OutputShapeBase):
    """
    Represents the returned data in response to a request action.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "runtime_configuration",
                "RuntimeConfiguration",
                TypeInfo(RuntimeConfiguration),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The run-time configuration currently in force. If the update was
    # successful, this object matches the one in the request.
    runtime_configuration: "RuntimeConfiguration" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class ValidateMatchmakingRuleSetInput(ShapeBase):
    """
    Represents the input for a request action.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "rule_set_body",
                "RuleSetBody",
                TypeInfo(str),
            ),
        ]

    # Collection of matchmaking rules to validate, formatted as a JSON string.
    rule_set_body: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ValidateMatchmakingRuleSetOutput(OutputShapeBase):
    """
    Represents the returned data in response to a request action.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "valid",
                "Valid",
                TypeInfo(bool),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Response indicating whether or not the rule set is valid.
    valid: bool = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class VpcPeeringAuthorization(ShapeBase):
    """
    Represents an authorization for a VPC peering connection between the VPC for an
    Amazon GameLift fleet and another VPC on an account you have access to. This
    authorization must exist and be valid for the peering connection to be
    established. Authorizations are valid for 24 hours after they are issued.

    VPC peering connection operations include:

      * CreateVpcPeeringAuthorization

      * DescribeVpcPeeringAuthorizations

      * DeleteVpcPeeringAuthorization

      * CreateVpcPeeringConnection

      * DescribeVpcPeeringConnections

      * DeleteVpcPeeringConnection
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "game_lift_aws_account_id",
                "GameLiftAwsAccountId",
                TypeInfo(str),
            ),
            (
                "peer_vpc_aws_account_id",
                "PeerVpcAwsAccountId",
                TypeInfo(str),
            ),
            (
                "peer_vpc_id",
                "PeerVpcId",
                TypeInfo(str),
            ),
            (
                "creation_time",
                "CreationTime",
                TypeInfo(datetime.datetime),
            ),
            (
                "expiration_time",
                "ExpirationTime",
                TypeInfo(datetime.datetime),
            ),
        ]

    # Unique identifier for the AWS account that you use to manage your Amazon
    # GameLift fleet. You can find your Account ID in the AWS Management Console
    # under account settings.
    game_lift_aws_account_id: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    peer_vpc_aws_account_id: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Unique identifier for a VPC with resources to be accessed by your Amazon
    # GameLift fleet. The VPC must be in the same region where your fleet is
    # deployed. To get VPC information, including IDs, use the Virtual Private
    # Cloud service tools, including the VPC Dashboard in the AWS Management
    # Console.
    peer_vpc_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Time stamp indicating when this authorization was issued. Format is a
    # number expressed in Unix time as milliseconds (for example
    # "1469498468.057").
    creation_time: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Time stamp indicating when this authorization expires (24 hours after
    # issuance). Format is a number expressed in Unix time as milliseconds (for
    # example "1469498468.057").
    expiration_time: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class VpcPeeringConnection(ShapeBase):
    """
    Represents a peering connection between a VPC on one of your AWS accounts and
    the VPC for your Amazon GameLift fleets. This record may be for an active
    peering connection or a pending connection that has not yet been established.

    VPC peering connection operations include:

      * CreateVpcPeeringAuthorization

      * DescribeVpcPeeringAuthorizations

      * DeleteVpcPeeringAuthorization

      * CreateVpcPeeringConnection

      * DescribeVpcPeeringConnections

      * DeleteVpcPeeringConnection
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "fleet_id",
                "FleetId",
                TypeInfo(str),
            ),
            (
                "ip_v4_cidr_block",
                "IpV4CidrBlock",
                TypeInfo(str),
            ),
            (
                "vpc_peering_connection_id",
                "VpcPeeringConnectionId",
                TypeInfo(str),
            ),
            (
                "status",
                "Status",
                TypeInfo(VpcPeeringConnectionStatus),
            ),
            (
                "peer_vpc_id",
                "PeerVpcId",
                TypeInfo(str),
            ),
            (
                "game_lift_vpc_id",
                "GameLiftVpcId",
                TypeInfo(str),
            ),
        ]

    # Unique identifier for a fleet. This ID determines the ID of the Amazon
    # GameLift VPC for your fleet.
    fleet_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # CIDR block of IPv4 addresses assigned to the VPC peering connection for the
    # GameLift VPC. The peered VPC also has an IPv4 CIDR block associated with
    # it; these blocks cannot overlap or the peering connection cannot be
    # created.
    ip_v4_cidr_block: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Unique identifier that is automatically assigned to the connection record.
    # This ID is referenced in VPC peering connection events, and is used when
    # deleting a connection with DeleteVpcPeeringConnection.
    vpc_peering_connection_id: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Object that contains status information about the connection. Status
    # indicates if a connection is pending, successful, or failed.
    status: "VpcPeeringConnectionStatus" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Unique identifier for a VPC with resources to be accessed by your Amazon
    # GameLift fleet. The VPC must be in the same region where your fleet is
    # deployed. To get VPC information, including IDs, use the Virtual Private
    # Cloud service tools, including the VPC Dashboard in the AWS Management
    # Console.
    peer_vpc_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Unique identifier for the VPC that contains the Amazon GameLift fleet for
    # this connection. This VPC is managed by Amazon GameLift and does not appear
    # in your AWS account.
    game_lift_vpc_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class VpcPeeringConnectionStatus(ShapeBase):
    """
    Represents status information for a VPC peering connection. Status is associated
    with a VpcPeeringConnection object. Status codes and messages are provided from
    EC2 (see
    [VpcPeeringConnectionStateReason](http://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_VpcPeeringConnectionStateReason.html)).
    Connection status information is also communicated as a fleet Event.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "code",
                "Code",
                TypeInfo(str),
            ),
            (
                "message",
                "Message",
                TypeInfo(str),
            ),
        ]

    # Code indicating the status of a VPC peering connection.
    code: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Additional messaging associated with the connection status.
    message: str = dataclasses.field(default=ShapeBase.NOT_SET, )
