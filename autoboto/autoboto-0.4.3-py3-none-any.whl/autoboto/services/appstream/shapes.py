import datetime
import typing
from autoboto import ShapeBase, OutputShapeBase, TypeInfo
import dataclasses


class Action(str):
    CLIPBOARD_COPY_FROM_LOCAL_DEVICE = "CLIPBOARD_COPY_FROM_LOCAL_DEVICE"
    CLIPBOARD_COPY_TO_LOCAL_DEVICE = "CLIPBOARD_COPY_TO_LOCAL_DEVICE"
    FILE_UPLOAD = "FILE_UPLOAD"
    FILE_DOWNLOAD = "FILE_DOWNLOAD"
    PRINTING_TO_LOCAL_DEVICE = "PRINTING_TO_LOCAL_DEVICE"


@dataclasses.dataclass
class Application(ShapeBase):
    """
    Describes an application in the application catalog.
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
                "display_name",
                "DisplayName",
                TypeInfo(str),
            ),
            (
                "icon_url",
                "IconURL",
                TypeInfo(str),
            ),
            (
                "launch_path",
                "LaunchPath",
                TypeInfo(str),
            ),
            (
                "launch_parameters",
                "LaunchParameters",
                TypeInfo(str),
            ),
            (
                "enabled",
                "Enabled",
                TypeInfo(bool),
            ),
            (
                "metadata",
                "Metadata",
                TypeInfo(typing.Dict[str, str]),
            ),
        ]

    # The name of the application.
    name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The application name for display.
    display_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The URL for the application icon. This URL might be time-limited.
    icon_url: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The path to the application executable in the instance.
    launch_path: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The arguments that are passed to the application at launch.
    launch_parameters: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # If there is a problem, the application can be disabled after image
    # creation.
    enabled: bool = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Additional attributes that describe the application.
    metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class ApplicationSettings(ShapeBase):
    """
    The persistent application settings for users of a stack.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "enabled",
                "Enabled",
                TypeInfo(bool),
            ),
            (
                "settings_group",
                "SettingsGroup",
                TypeInfo(str),
            ),
        ]

    # Enables or disables persistent application settings for users during their
    # streaming sessions.
    enabled: bool = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The path prefix for the S3 bucket where users’ persistent application
    # settings are stored. You can allow the same persistent application settings
    # to be used across multiple stacks by specifying the same settings group for
    # each stack.
    settings_group: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ApplicationSettingsResponse(ShapeBase):
    """
    Describes the persistent application settings for users of a stack.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "enabled",
                "Enabled",
                TypeInfo(bool),
            ),
            (
                "settings_group",
                "SettingsGroup",
                TypeInfo(str),
            ),
            (
                "s3_bucket_name",
                "S3BucketName",
                TypeInfo(str),
            ),
        ]

    # Specifies whether persistent application settings are enabled for users
    # during their streaming sessions.
    enabled: bool = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The path prefix for the S3 bucket where users’ persistent application
    # settings are stored.
    settings_group: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The S3 bucket where users’ persistent application settings are stored. When
    # persistent application settings are enabled for the first time for an
    # account in an AWS Region, an S3 bucket is created. The bucket is unique to
    # the AWS account and the Region.
    s3_bucket_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class AssociateFleetRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "fleet_name",
                "FleetName",
                TypeInfo(str),
            ),
            (
                "stack_name",
                "StackName",
                TypeInfo(str),
            ),
        ]

    # The name of the fleet.
    fleet_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The name of the stack.
    stack_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class AssociateFleetResult(OutputShapeBase):
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


class AuthenticationType(str):
    API = "API"
    SAML = "SAML"
    USERPOOL = "USERPOOL"


@dataclasses.dataclass
class ComputeCapacity(ShapeBase):
    """
    Describes the capacity for a fleet.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "desired_instances",
                "DesiredInstances",
                TypeInfo(int),
            ),
        ]

    # The desired number of streaming instances.
    desired_instances: int = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ComputeCapacityStatus(ShapeBase):
    """
    Describes the capacity status for a fleet.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "desired",
                "Desired",
                TypeInfo(int),
            ),
            (
                "running",
                "Running",
                TypeInfo(int),
            ),
            (
                "in_use",
                "InUse",
                TypeInfo(int),
            ),
            (
                "available",
                "Available",
                TypeInfo(int),
            ),
        ]

    # The desired number of streaming instances.
    desired: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The total number of simultaneous streaming instances that are running.
    running: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The number of instances in use for streaming.
    in_use: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The number of currently available instances that can be used to stream
    # sessions.
    available: int = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ConcurrentModificationException(ShapeBase):
    """
    An API error occurred. Wait a few minutes and try again.
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

    # The error message in the exception.
    message: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class CopyImageRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "source_image_name",
                "SourceImageName",
                TypeInfo(str),
            ),
            (
                "destination_image_name",
                "DestinationImageName",
                TypeInfo(str),
            ),
            (
                "destination_region",
                "DestinationRegion",
                TypeInfo(str),
            ),
            (
                "destination_image_description",
                "DestinationImageDescription",
                TypeInfo(str),
            ),
        ]

    # The name of the image to copy.
    source_image_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The name that the image will have when it is copied to the destination.
    destination_image_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The destination region to which the image will be copied. This parameter is
    # required, even if you are copying an image within the same region.
    destination_region: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The description that the image will have when it is copied to the
    # destination.
    destination_image_description: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class CopyImageResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "destination_image_name",
                "DestinationImageName",
                TypeInfo(str),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The name of the destination image.
    destination_image_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class CreateDirectoryConfigRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "directory_name",
                "DirectoryName",
                TypeInfo(str),
            ),
            (
                "organizational_unit_distinguished_names",
                "OrganizationalUnitDistinguishedNames",
                TypeInfo(typing.List[str]),
            ),
            (
                "service_account_credentials",
                "ServiceAccountCredentials",
                TypeInfo(ServiceAccountCredentials),
            ),
        ]

    # The fully qualified name of the directory (for example, corp.example.com).
    directory_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The distinguished names of the organizational units for computer accounts.
    organizational_unit_distinguished_names: typing.List[
        str] = dataclasses.field(
            default=ShapeBase.NOT_SET,
        )

    # The credentials for the service account used by the streaming instance to
    # connect to the directory.
    service_account_credentials: "ServiceAccountCredentials" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class CreateDirectoryConfigResult(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "directory_config",
                "DirectoryConfig",
                TypeInfo(DirectoryConfig),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Information about the directory configuration.
    directory_config: "DirectoryConfig" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class CreateFleetRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "name",
                "Name",
                TypeInfo(str),
            ),
            (
                "instance_type",
                "InstanceType",
                TypeInfo(str),
            ),
            (
                "compute_capacity",
                "ComputeCapacity",
                TypeInfo(ComputeCapacity),
            ),
            (
                "image_name",
                "ImageName",
                TypeInfo(str),
            ),
            (
                "image_arn",
                "ImageArn",
                TypeInfo(str),
            ),
            (
                "fleet_type",
                "FleetType",
                TypeInfo(typing.Union[str, FleetType]),
            ),
            (
                "vpc_config",
                "VpcConfig",
                TypeInfo(VpcConfig),
            ),
            (
                "max_user_duration_in_seconds",
                "MaxUserDurationInSeconds",
                TypeInfo(int),
            ),
            (
                "disconnect_timeout_in_seconds",
                "DisconnectTimeoutInSeconds",
                TypeInfo(int),
            ),
            (
                "description",
                "Description",
                TypeInfo(str),
            ),
            (
                "display_name",
                "DisplayName",
                TypeInfo(str),
            ),
            (
                "enable_default_internet_access",
                "EnableDefaultInternetAccess",
                TypeInfo(bool),
            ),
            (
                "domain_join_info",
                "DomainJoinInfo",
                TypeInfo(DomainJoinInfo),
            ),
        ]

    # A unique name for the fleet.
    name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The instance type to use when launching fleet instances. The following
    # instance types are available:

    #   * stream.standard.medium

    #   * stream.standard.large

    #   * stream.compute.large

    #   * stream.compute.xlarge

    #   * stream.compute.2xlarge

    #   * stream.compute.4xlarge

    #   * stream.compute.8xlarge

    #   * stream.memory.large

    #   * stream.memory.xlarge

    #   * stream.memory.2xlarge

    #   * stream.memory.4xlarge

    #   * stream.memory.8xlarge

    #   * stream.graphics-design.large

    #   * stream.graphics-design.xlarge

    #   * stream.graphics-design.2xlarge

    #   * stream.graphics-design.4xlarge

    #   * stream.graphics-desktop.2xlarge

    #   * stream.graphics-pro.4xlarge

    #   * stream.graphics-pro.8xlarge

    #   * stream.graphics-pro.16xlarge
    instance_type: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The desired capacity for the fleet.
    compute_capacity: "ComputeCapacity" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The name of the image used to create the fleet.
    image_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The ARN of the public, private, or shared image to use.
    image_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The fleet type.

    # ALWAYS_ON

    # Provides users with instant-on access to their apps. You are charged for
    # all running instances in your fleet, even if no users are streaming apps.

    # ON_DEMAND

    # Provide users with access to applications after they connect, which takes
    # one to two minutes. You are charged for instance streaming when users are
    # connected and a small hourly fee for instances that are not streaming apps.
    fleet_type: typing.Union[str, "FleetType"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The VPC configuration for the fleet.
    vpc_config: "VpcConfig" = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The maximum time that a streaming session can run, in seconds. Specify a
    # value between 600 and 57600.
    max_user_duration_in_seconds: int = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The time after disconnection when a session is considered to have ended, in
    # seconds. If a user who was disconnected reconnects within this time
    # interval, the user is connected to their previous session. Specify a value
    # between 60 and 57600.
    disconnect_timeout_in_seconds: int = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The description for display.
    description: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The fleet name for display.
    display_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Enables or disables default internet access for the fleet.
    enable_default_internet_access: bool = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The information needed to join a Microsoft Active Directory domain.
    domain_join_info: "DomainJoinInfo" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class CreateFleetResult(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "fleet",
                "Fleet",
                TypeInfo(Fleet),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Information about the fleet.
    fleet: "Fleet" = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class CreateImageBuilderRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "name",
                "Name",
                TypeInfo(str),
            ),
            (
                "instance_type",
                "InstanceType",
                TypeInfo(str),
            ),
            (
                "image_name",
                "ImageName",
                TypeInfo(str),
            ),
            (
                "image_arn",
                "ImageArn",
                TypeInfo(str),
            ),
            (
                "description",
                "Description",
                TypeInfo(str),
            ),
            (
                "display_name",
                "DisplayName",
                TypeInfo(str),
            ),
            (
                "vpc_config",
                "VpcConfig",
                TypeInfo(VpcConfig),
            ),
            (
                "enable_default_internet_access",
                "EnableDefaultInternetAccess",
                TypeInfo(bool),
            ),
            (
                "domain_join_info",
                "DomainJoinInfo",
                TypeInfo(DomainJoinInfo),
            ),
            (
                "appstream_agent_version",
                "AppstreamAgentVersion",
                TypeInfo(str),
            ),
        ]

    # A unique name for the image builder.
    name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The instance type to use when launching the image builder.
    instance_type: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The name of the image used to create the builder.
    image_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The ARN of the public, private, or shared image to use.
    image_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The description for display.
    description: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The image builder name for display.
    display_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The VPC configuration for the image builder. You can specify only one
    # subnet.
    vpc_config: "VpcConfig" = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Enables or disables default internet access for the image builder.
    enable_default_internet_access: bool = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The information needed to join a Microsoft Active Directory domain.
    domain_join_info: "DomainJoinInfo" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The version of the AppStream 2.0 agent to use for this image builder. To
    # use the latest version of the AppStream 2.0 agent, specify [LATEST].
    appstream_agent_version: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class CreateImageBuilderResult(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "image_builder",
                "ImageBuilder",
                TypeInfo(ImageBuilder),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Information about the image builder.
    image_builder: "ImageBuilder" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class CreateImageBuilderStreamingURLRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "name",
                "Name",
                TypeInfo(str),
            ),
            (
                "validity",
                "Validity",
                TypeInfo(int),
            ),
        ]

    # The name of the image builder.
    name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The time that the streaming URL will be valid, in seconds. Specify a value
    # between 1 and 604800 seconds. The default is 3600 seconds.
    validity: int = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class CreateImageBuilderStreamingURLResult(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "streaming_url",
                "StreamingURL",
                TypeInfo(str),
            ),
            (
                "expires",
                "Expires",
                TypeInfo(datetime.datetime),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The URL to start the AppStream 2.0 streaming session.
    streaming_url: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The elapsed time, in seconds after the Unix epoch, when this URL expires.
    expires: datetime.datetime = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class CreateStackRequest(ShapeBase):
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
                "display_name",
                "DisplayName",
                TypeInfo(str),
            ),
            (
                "storage_connectors",
                "StorageConnectors",
                TypeInfo(typing.List[StorageConnector]),
            ),
            (
                "redirect_url",
                "RedirectURL",
                TypeInfo(str),
            ),
            (
                "feedback_url",
                "FeedbackURL",
                TypeInfo(str),
            ),
            (
                "user_settings",
                "UserSettings",
                TypeInfo(typing.List[UserSetting]),
            ),
            (
                "application_settings",
                "ApplicationSettings",
                TypeInfo(ApplicationSettings),
            ),
        ]

    # The name of the stack.
    name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The description for display.
    description: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The stack name for display.
    display_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The storage connectors to enable.
    storage_connectors: typing.List["StorageConnector"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The URL that users are redirected to after their streaming session ends.
    redirect_url: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The URL that users are redirected to after they click the Send Feedback
    # link. If no URL is specified, no Send Feedback link is displayed.
    feedback_url: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The actions that are enabled or disabled for users during their streaming
    # sessions. By default, these actions are enabled.
    user_settings: typing.List["UserSetting"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The persistent application settings for users of a stack. When these
    # settings are enabled, changes that users make to applications and Windows
    # settings are automatically saved after each session and applied to the next
    # session.
    application_settings: "ApplicationSettings" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class CreateStackResult(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "stack",
                "Stack",
                TypeInfo(Stack),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Information about the stack.
    stack: "Stack" = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class CreateStreamingURLRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "stack_name",
                "StackName",
                TypeInfo(str),
            ),
            (
                "fleet_name",
                "FleetName",
                TypeInfo(str),
            ),
            (
                "user_id",
                "UserId",
                TypeInfo(str),
            ),
            (
                "application_id",
                "ApplicationId",
                TypeInfo(str),
            ),
            (
                "validity",
                "Validity",
                TypeInfo(int),
            ),
            (
                "session_context",
                "SessionContext",
                TypeInfo(str),
            ),
        ]

    # The name of the stack.
    stack_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The name of the fleet.
    fleet_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The ID of the user.
    user_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The name of the application to launch after the session starts. This is the
    # name that you specified as **Name** in the Image Assistant.
    application_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The time that the streaming URL will be valid, in seconds. Specify a value
    # between 1 and 604800 seconds. The default is 60 seconds.
    validity: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The session context. For more information, see [Session
    # Context](http://docs.aws.amazon.com/appstream2/latest/developerguide/managing-
    # stacks-fleets.html#managing-stacks-fleets-parameters) in the _Amazon
    # AppStream 2.0 Developer Guide_.
    session_context: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class CreateStreamingURLResult(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "streaming_url",
                "StreamingURL",
                TypeInfo(str),
            ),
            (
                "expires",
                "Expires",
                TypeInfo(datetime.datetime),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The URL to start the AppStream 2.0 streaming session.
    streaming_url: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The elapsed time, in seconds after the Unix epoch, when this URL expires.
    expires: datetime.datetime = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DeleteDirectoryConfigRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "directory_name",
                "DirectoryName",
                TypeInfo(str),
            ),
        ]

    # The name of the directory configuration.
    directory_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DeleteDirectoryConfigResult(OutputShapeBase):
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
class DeleteFleetRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "name",
                "Name",
                TypeInfo(str),
            ),
        ]

    # The name of the fleet.
    name: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DeleteFleetResult(OutputShapeBase):
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
class DeleteImageBuilderRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "name",
                "Name",
                TypeInfo(str),
            ),
        ]

    # The name of the image builder.
    name: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DeleteImageBuilderResult(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "image_builder",
                "ImageBuilder",
                TypeInfo(ImageBuilder),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Information about the image builder.
    image_builder: "ImageBuilder" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class DeleteImagePermissionsRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "name",
                "Name",
                TypeInfo(str),
            ),
            (
                "shared_account_id",
                "SharedAccountId",
                TypeInfo(str),
            ),
        ]

    # The name of the private image.
    name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The 12-digit ID of the AWS account for which to delete image permissions.
    shared_account_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DeleteImagePermissionsResult(OutputShapeBase):
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
class DeleteImageRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "name",
                "Name",
                TypeInfo(str),
            ),
        ]

    # The name of the image.
    name: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DeleteImageResult(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "image",
                "Image",
                TypeInfo(Image),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Information about the image.
    image: "Image" = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DeleteStackRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "name",
                "Name",
                TypeInfo(str),
            ),
        ]

    # The name of the stack.
    name: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DeleteStackResult(OutputShapeBase):
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
class DescribeDirectoryConfigsRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "directory_names",
                "DirectoryNames",
                TypeInfo(typing.List[str]),
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

    # The directory names.
    directory_names: typing.List[str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The maximum size of each page of results.
    max_results: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The pagination token to use to retrieve the next page of results for this
    # operation. If this value is null, it retrieves the first page.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DescribeDirectoryConfigsResult(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "directory_configs",
                "DirectoryConfigs",
                TypeInfo(typing.List[DirectoryConfig]),
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

    # Information about the directory configurations. Note that although the
    # response syntax in this topic includes the account password, this password
    # is not returned in the actual response.
    directory_configs: typing.List["DirectoryConfig"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The pagination token to use to retrieve the next page of results for this
    # operation. If there are no more pages, this value is null.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DescribeFleetsRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "names",
                "Names",
                TypeInfo(typing.List[str]),
            ),
            (
                "next_token",
                "NextToken",
                TypeInfo(str),
            ),
        ]

    # The names of the fleets to describe.
    names: typing.List[str] = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The pagination token to use to retrieve the next page of results for this
    # operation. If this value is null, it retrieves the first page.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DescribeFleetsResult(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "fleets",
                "Fleets",
                TypeInfo(typing.List[Fleet]),
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

    # Information about the fleets.
    fleets: typing.List["Fleet"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The pagination token to use to retrieve the next page of results for this
    # operation. If there are no more pages, this value is null.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DescribeImageBuildersRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "names",
                "Names",
                TypeInfo(typing.List[str]),
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

    # The names of the image builders to describe.
    names: typing.List[str] = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The maximum size of each page of results.
    max_results: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The pagination token to use to retrieve the next page of results for this
    # operation. If this value is null, it retrieves the first page.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DescribeImageBuildersResult(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "image_builders",
                "ImageBuilders",
                TypeInfo(typing.List[ImageBuilder]),
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

    # Information about the image builders.
    image_builders: typing.List["ImageBuilder"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The pagination token to use to retrieve the next page of results for this
    # operation. If there are no more pages, this value is null.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DescribeImagePermissionsRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "name",
                "Name",
                TypeInfo(str),
            ),
            (
                "max_results",
                "MaxResults",
                TypeInfo(int),
            ),
            (
                "shared_aws_account_ids",
                "SharedAwsAccountIds",
                TypeInfo(typing.List[str]),
            ),
            (
                "next_token",
                "NextToken",
                TypeInfo(str),
            ),
        ]

    # The name of the private image for which to describe permissions. The image
    # must be one that you own.
    name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The maximum size of each results page.
    max_results: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The 12-digit ID of one or more AWS accounts with which the image is shared.
    shared_aws_account_ids: typing.List[str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The pagination token to use to retrieve the next page of results. If this
    # value is empty, only the first page is retrieved.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DescribeImagePermissionsResult(OutputShapeBase):
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
            (
                "shared_image_permissions_list",
                "SharedImagePermissionsList",
                TypeInfo(typing.List[SharedImagePermissions]),
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

    # The name of the private image.
    name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The permissions for a private image that you own.
    shared_image_permissions_list: typing.List["SharedImagePermissions"
                                              ] = dataclasses.field(
                                                  default=ShapeBase.NOT_SET,
                                              )

    # The pagination token to use to retrieve the next page of results. If this
    # value is empty, only the first page is retrieved.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DescribeImagesRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "names",
                "Names",
                TypeInfo(typing.List[str]),
            ),
            (
                "arns",
                "Arns",
                TypeInfo(typing.List[str]),
            ),
            (
                "type",
                "Type",
                TypeInfo(typing.Union[str, VisibilityType]),
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

    # The names of the public or private images to describe.
    names: typing.List[str] = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The ARNs of the public, private, and shared images to describe.
    arns: typing.List[str] = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The type of image (public, private, or shared) to describe.
    type: typing.Union[str, "VisibilityType"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The pagination token to use to retrieve the next page of results. If this
    # value is empty, only the first page is retrieved.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The maximum size of each page of results.
    max_results: int = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DescribeImagesResult(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "images",
                "Images",
                TypeInfo(typing.List[Image]),
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

    # Information about the images.
    images: typing.List["Image"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The pagination token to use to retrieve the next page of results. If there
    # are no more pages, this value is null.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DescribeSessionsRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "stack_name",
                "StackName",
                TypeInfo(str),
            ),
            (
                "fleet_name",
                "FleetName",
                TypeInfo(str),
            ),
            (
                "user_id",
                "UserId",
                TypeInfo(str),
            ),
            (
                "next_token",
                "NextToken",
                TypeInfo(str),
            ),
            (
                "limit",
                "Limit",
                TypeInfo(int),
            ),
            (
                "authentication_type",
                "AuthenticationType",
                TypeInfo(typing.Union[str, AuthenticationType]),
            ),
        ]

    # The name of the stack. This value is case-sensitive.
    stack_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The name of the fleet. This value is case-sensitive.
    fleet_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The user ID.
    user_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The pagination token to use to retrieve the next page of results for this
    # operation. If this value is null, it retrieves the first page.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The size of each page of results. The default value is 20 and the maximum
    # value is 50.
    limit: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The authentication method. Specify `API` for a user authenticated using a
    # streaming URL or `SAML` for a SAML federated user. The default is to
    # authenticate users using a streaming URL.
    authentication_type: typing.Union[str, "AuthenticationType"
                                     ] = dataclasses.field(
                                         default=ShapeBase.NOT_SET,
                                     )


@dataclasses.dataclass
class DescribeSessionsResult(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "sessions",
                "Sessions",
                TypeInfo(typing.List[Session]),
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

    # Information about the streaming sessions.
    sessions: typing.List["Session"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The pagination token to use to retrieve the next page of results for this
    # operation. If there are no more pages, this value is null.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DescribeStacksRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "names",
                "Names",
                TypeInfo(typing.List[str]),
            ),
            (
                "next_token",
                "NextToken",
                TypeInfo(str),
            ),
        ]

    # The names of the stacks to describe.
    names: typing.List[str] = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The pagination token to use to retrieve the next page of results for this
    # operation. If this value is null, it retrieves the first page.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DescribeStacksResult(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "stacks",
                "Stacks",
                TypeInfo(typing.List[Stack]),
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

    # Information about the stacks.
    stacks: typing.List["Stack"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The pagination token to use to retrieve the next page of results for this
    # operation. If there are no more pages, this value is null.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DirectoryConfig(ShapeBase):
    """
    Configuration information for the directory used to join domains.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "directory_name",
                "DirectoryName",
                TypeInfo(str),
            ),
            (
                "organizational_unit_distinguished_names",
                "OrganizationalUnitDistinguishedNames",
                TypeInfo(typing.List[str]),
            ),
            (
                "service_account_credentials",
                "ServiceAccountCredentials",
                TypeInfo(ServiceAccountCredentials),
            ),
            (
                "created_time",
                "CreatedTime",
                TypeInfo(datetime.datetime),
            ),
        ]

    # The fully qualified name of the directory (for example, corp.example.com).
    directory_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The distinguished names of the organizational units for computer accounts.
    organizational_unit_distinguished_names: typing.List[
        str] = dataclasses.field(
            default=ShapeBase.NOT_SET,
        )

    # The credentials for the service account used by the streaming instance to
    # connect to the directory.
    service_account_credentials: "ServiceAccountCredentials" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The time the directory configuration was created.
    created_time: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class DisassociateFleetRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "fleet_name",
                "FleetName",
                TypeInfo(str),
            ),
            (
                "stack_name",
                "StackName",
                TypeInfo(str),
            ),
        ]

    # The name of the fleet.
    fleet_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The name of the stack.
    stack_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DisassociateFleetResult(OutputShapeBase):
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
class DomainJoinInfo(ShapeBase):
    """
    Contains the information needed to join a Microsoft Active Directory domain.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "directory_name",
                "DirectoryName",
                TypeInfo(str),
            ),
            (
                "organizational_unit_distinguished_name",
                "OrganizationalUnitDistinguishedName",
                TypeInfo(str),
            ),
        ]

    # The fully qualified name of the directory (for example, corp.example.com).
    directory_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The distinguished name of the organizational unit for computer accounts.
    organizational_unit_distinguished_name: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class ExpireSessionRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "session_id",
                "SessionId",
                TypeInfo(str),
            ),
        ]

    # The ID of the streaming session.
    session_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ExpireSessionResult(OutputShapeBase):
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
class Fleet(ShapeBase):
    """
    Contains the parameters for a fleet.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
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
                "instance_type",
                "InstanceType",
                TypeInfo(str),
            ),
            (
                "compute_capacity_status",
                "ComputeCapacityStatus",
                TypeInfo(ComputeCapacityStatus),
            ),
            (
                "state",
                "State",
                TypeInfo(typing.Union[str, FleetState]),
            ),
            (
                "display_name",
                "DisplayName",
                TypeInfo(str),
            ),
            (
                "description",
                "Description",
                TypeInfo(str),
            ),
            (
                "image_name",
                "ImageName",
                TypeInfo(str),
            ),
            (
                "image_arn",
                "ImageArn",
                TypeInfo(str),
            ),
            (
                "fleet_type",
                "FleetType",
                TypeInfo(typing.Union[str, FleetType]),
            ),
            (
                "max_user_duration_in_seconds",
                "MaxUserDurationInSeconds",
                TypeInfo(int),
            ),
            (
                "disconnect_timeout_in_seconds",
                "DisconnectTimeoutInSeconds",
                TypeInfo(int),
            ),
            (
                "vpc_config",
                "VpcConfig",
                TypeInfo(VpcConfig),
            ),
            (
                "created_time",
                "CreatedTime",
                TypeInfo(datetime.datetime),
            ),
            (
                "fleet_errors",
                "FleetErrors",
                TypeInfo(typing.List[FleetError]),
            ),
            (
                "enable_default_internet_access",
                "EnableDefaultInternetAccess",
                TypeInfo(bool),
            ),
            (
                "domain_join_info",
                "DomainJoinInfo",
                TypeInfo(DomainJoinInfo),
            ),
        ]

    # The ARN for the fleet.
    arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The name of the fleet.
    name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The instance type to use when launching fleet instances.
    instance_type: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The capacity status for the fleet.
    compute_capacity_status: "ComputeCapacityStatus" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The current state for the fleet.
    state: typing.Union[str, "FleetState"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The fleet name for display.
    display_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The description for display.
    description: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The name of the image used to create the fleet.
    image_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The ARN for the public, private, or shared image.
    image_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The fleet type.

    # ALWAYS_ON

    # Provides users with instant-on access to their apps. You are charged for
    # all running instances in your fleet, even if no users are streaming apps.

    # ON_DEMAND

    # Provide users with access to applications after they connect, which takes
    # one to two minutes. You are charged for instance streaming when users are
    # connected and a small hourly fee for instances that are not streaming apps.
    fleet_type: typing.Union[str, "FleetType"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The maximum time that a streaming session can run, in seconds. Specify a
    # value between 600 and 57600.
    max_user_duration_in_seconds: int = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The time after disconnection when a session is considered to have ended, in
    # seconds. If a user who was disconnected reconnects within this time
    # interval, the user is connected to their previous session. Specify a value
    # between 60 and 57600.
    disconnect_timeout_in_seconds: int = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The VPC configuration for the fleet.
    vpc_config: "VpcConfig" = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The time the fleet was created.
    created_time: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The fleet errors.
    fleet_errors: typing.List["FleetError"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Indicates whether default internet access is enabled for the fleet.
    enable_default_internet_access: bool = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The information needed to join a Microsoft Active Directory domain.
    domain_join_info: "DomainJoinInfo" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


class FleetAttribute(str):
    """
    The fleet attribute.
    """
    VPC_CONFIGURATION = "VPC_CONFIGURATION"
    VPC_CONFIGURATION_SECURITY_GROUP_IDS = "VPC_CONFIGURATION_SECURITY_GROUP_IDS"
    DOMAIN_JOIN_INFO = "DOMAIN_JOIN_INFO"


@dataclasses.dataclass
class FleetError(ShapeBase):
    """
    Describes a fleet error.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "error_code",
                "ErrorCode",
                TypeInfo(typing.Union[str, FleetErrorCode]),
            ),
            (
                "error_message",
                "ErrorMessage",
                TypeInfo(str),
            ),
        ]

    # The error code.
    error_code: typing.Union[str, "FleetErrorCode"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The error message.
    error_message: str = dataclasses.field(default=ShapeBase.NOT_SET, )


class FleetErrorCode(str):
    IAM_SERVICE_ROLE_MISSING_ENI_DESCRIBE_ACTION = "IAM_SERVICE_ROLE_MISSING_ENI_DESCRIBE_ACTION"
    IAM_SERVICE_ROLE_MISSING_ENI_CREATE_ACTION = "IAM_SERVICE_ROLE_MISSING_ENI_CREATE_ACTION"
    IAM_SERVICE_ROLE_MISSING_ENI_DELETE_ACTION = "IAM_SERVICE_ROLE_MISSING_ENI_DELETE_ACTION"
    NETWORK_INTERFACE_LIMIT_EXCEEDED = "NETWORK_INTERFACE_LIMIT_EXCEEDED"
    INTERNAL_SERVICE_ERROR = "INTERNAL_SERVICE_ERROR"
    IAM_SERVICE_ROLE_IS_MISSING = "IAM_SERVICE_ROLE_IS_MISSING"
    SUBNET_HAS_INSUFFICIENT_IP_ADDRESSES = "SUBNET_HAS_INSUFFICIENT_IP_ADDRESSES"
    IAM_SERVICE_ROLE_MISSING_DESCRIBE_SUBNET_ACTION = "IAM_SERVICE_ROLE_MISSING_DESCRIBE_SUBNET_ACTION"
    SUBNET_NOT_FOUND = "SUBNET_NOT_FOUND"
    IMAGE_NOT_FOUND = "IMAGE_NOT_FOUND"
    INVALID_SUBNET_CONFIGURATION = "INVALID_SUBNET_CONFIGURATION"
    SECURITY_GROUPS_NOT_FOUND = "SECURITY_GROUPS_NOT_FOUND"
    IGW_NOT_ATTACHED = "IGW_NOT_ATTACHED"
    IAM_SERVICE_ROLE_MISSING_DESCRIBE_SECURITY_GROUPS_ACTION = "IAM_SERVICE_ROLE_MISSING_DESCRIBE_SECURITY_GROUPS_ACTION"
    DOMAIN_JOIN_ERROR_FILE_NOT_FOUND = "DOMAIN_JOIN_ERROR_FILE_NOT_FOUND"
    DOMAIN_JOIN_ERROR_ACCESS_DENIED = "DOMAIN_JOIN_ERROR_ACCESS_DENIED"
    DOMAIN_JOIN_ERROR_LOGON_FAILURE = "DOMAIN_JOIN_ERROR_LOGON_FAILURE"
    DOMAIN_JOIN_ERROR_INVALID_PARAMETER = "DOMAIN_JOIN_ERROR_INVALID_PARAMETER"
    DOMAIN_JOIN_ERROR_MORE_DATA = "DOMAIN_JOIN_ERROR_MORE_DATA"
    DOMAIN_JOIN_ERROR_NO_SUCH_DOMAIN = "DOMAIN_JOIN_ERROR_NO_SUCH_DOMAIN"
    DOMAIN_JOIN_ERROR_NOT_SUPPORTED = "DOMAIN_JOIN_ERROR_NOT_SUPPORTED"
    DOMAIN_JOIN_NERR_INVALID_WORKGROUP_NAME = "DOMAIN_JOIN_NERR_INVALID_WORKGROUP_NAME"
    DOMAIN_JOIN_NERR_WORKSTATION_NOT_STARTED = "DOMAIN_JOIN_NERR_WORKSTATION_NOT_STARTED"
    DOMAIN_JOIN_ERROR_DS_MACHINE_ACCOUNT_QUOTA_EXCEEDED = "DOMAIN_JOIN_ERROR_DS_MACHINE_ACCOUNT_QUOTA_EXCEEDED"
    DOMAIN_JOIN_NERR_PASSWORD_EXPIRED = "DOMAIN_JOIN_NERR_PASSWORD_EXPIRED"
    DOMAIN_JOIN_INTERNAL_SERVICE_ERROR = "DOMAIN_JOIN_INTERNAL_SERVICE_ERROR"


class FleetState(str):
    STARTING = "STARTING"
    RUNNING = "RUNNING"
    STOPPING = "STOPPING"
    STOPPED = "STOPPED"


class FleetType(str):
    ALWAYS_ON = "ALWAYS_ON"
    ON_DEMAND = "ON_DEMAND"


@dataclasses.dataclass
class Image(ShapeBase):
    """
    Describes an image.
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
                "arn",
                "Arn",
                TypeInfo(str),
            ),
            (
                "base_image_arn",
                "BaseImageArn",
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
                TypeInfo(typing.Union[str, ImageState]),
            ),
            (
                "visibility",
                "Visibility",
                TypeInfo(typing.Union[str, VisibilityType]),
            ),
            (
                "image_builder_supported",
                "ImageBuilderSupported",
                TypeInfo(bool),
            ),
            (
                "platform",
                "Platform",
                TypeInfo(typing.Union[str, PlatformType]),
            ),
            (
                "description",
                "Description",
                TypeInfo(str),
            ),
            (
                "state_change_reason",
                "StateChangeReason",
                TypeInfo(ImageStateChangeReason),
            ),
            (
                "applications",
                "Applications",
                TypeInfo(typing.List[Application]),
            ),
            (
                "created_time",
                "CreatedTime",
                TypeInfo(datetime.datetime),
            ),
            (
                "public_base_image_released_date",
                "PublicBaseImageReleasedDate",
                TypeInfo(datetime.datetime),
            ),
            (
                "appstream_agent_version",
                "AppstreamAgentVersion",
                TypeInfo(str),
            ),
            (
                "image_permissions",
                "ImagePermissions",
                TypeInfo(ImagePermissions),
            ),
        ]

    # The name of the image.
    name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The ARN of the image.
    arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The ARN of the image from which this image was created.
    base_image_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The image name for display.
    display_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The image starts in the `PENDING` state. If image creation succeeds, the
    # state is `AVAILABLE`. If image creation fails, the state is `FAILED`.
    state: typing.Union[str, "ImageState"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Indicates whether the image is public or private.
    visibility: typing.Union[str, "VisibilityType"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Indicates whether an image builder can be launched from this image.
    image_builder_supported: bool = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The operating system platform of the image.
    platform: typing.Union[str, "PlatformType"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The description for display.
    description: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The reason why the last state change occurred.
    state_change_reason: "ImageStateChangeReason" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The applications associated with the image.
    applications: typing.List["Application"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The time the image was created.
    created_time: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The release date of the public base image. For private images, this date is
    # the release date of the base image from which the image was created.
    public_base_image_released_date: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The version of the AppStream 2.0 agent to use for instances that are
    # launched from this image.
    appstream_agent_version: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The permissions to provide to the destination AWS account for the specified
    # image.
    image_permissions: "ImagePermissions" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class ImageBuilder(ShapeBase):
    """
    Describes a streaming instance used for editing an image. New images are created
    from a snapshot through an image builder.
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
                "arn",
                "Arn",
                TypeInfo(str),
            ),
            (
                "image_arn",
                "ImageArn",
                TypeInfo(str),
            ),
            (
                "description",
                "Description",
                TypeInfo(str),
            ),
            (
                "display_name",
                "DisplayName",
                TypeInfo(str),
            ),
            (
                "vpc_config",
                "VpcConfig",
                TypeInfo(VpcConfig),
            ),
            (
                "instance_type",
                "InstanceType",
                TypeInfo(str),
            ),
            (
                "platform",
                "Platform",
                TypeInfo(typing.Union[str, PlatformType]),
            ),
            (
                "state",
                "State",
                TypeInfo(typing.Union[str, ImageBuilderState]),
            ),
            (
                "state_change_reason",
                "StateChangeReason",
                TypeInfo(ImageBuilderStateChangeReason),
            ),
            (
                "created_time",
                "CreatedTime",
                TypeInfo(datetime.datetime),
            ),
            (
                "enable_default_internet_access",
                "EnableDefaultInternetAccess",
                TypeInfo(bool),
            ),
            (
                "domain_join_info",
                "DomainJoinInfo",
                TypeInfo(DomainJoinInfo),
            ),
            (
                "image_builder_errors",
                "ImageBuilderErrors",
                TypeInfo(typing.List[ResourceError]),
            ),
            (
                "appstream_agent_version",
                "AppstreamAgentVersion",
                TypeInfo(str),
            ),
        ]

    # The name of the image builder.
    name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The ARN for the image builder.
    arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The ARN of the image from which this builder was created.
    image_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The description for display.
    description: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The image builder name for display.
    display_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The VPC configuration of the image builder.
    vpc_config: "VpcConfig" = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The instance type for the image builder.
    instance_type: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The operating system platform of the image builder.
    platform: typing.Union[str, "PlatformType"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The state of the image builder.
    state: typing.Union[str, "ImageBuilderState"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The reason why the last state change occurred.
    state_change_reason: "ImageBuilderStateChangeReason" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The time stamp when the image builder was created.
    created_time: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Enables or disables default internet access for the image builder.
    enable_default_internet_access: bool = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The information needed to join a Microsoft Active Directory domain.
    domain_join_info: "DomainJoinInfo" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The image builder errors.
    image_builder_errors: typing.List["ResourceError"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The version of the AppStream 2.0 agent that is currently being used by this
    # image builder.
    appstream_agent_version: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


class ImageBuilderState(str):
    PENDING = "PENDING"
    UPDATING_AGENT = "UPDATING_AGENT"
    RUNNING = "RUNNING"
    STOPPING = "STOPPING"
    STOPPED = "STOPPED"
    REBOOTING = "REBOOTING"
    SNAPSHOTTING = "SNAPSHOTTING"
    DELETING = "DELETING"
    FAILED = "FAILED"


@dataclasses.dataclass
class ImageBuilderStateChangeReason(ShapeBase):
    """
    Describes the reason why the last image builder state change occurred.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "code",
                "Code",
                TypeInfo(typing.Union[str, ImageBuilderStateChangeReasonCode]),
            ),
            (
                "message",
                "Message",
                TypeInfo(str),
            ),
        ]

    # The state change reason code.
    code: typing.Union[str, "ImageBuilderStateChangeReasonCode"
                      ] = dataclasses.field(
                          default=ShapeBase.NOT_SET,
                      )

    # The state change reason message.
    message: str = dataclasses.field(default=ShapeBase.NOT_SET, )


class ImageBuilderStateChangeReasonCode(str):
    INTERNAL_ERROR = "INTERNAL_ERROR"
    IMAGE_UNAVAILABLE = "IMAGE_UNAVAILABLE"


@dataclasses.dataclass
class ImagePermissions(ShapeBase):
    """
    Describes the permissions for an image.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "allow_fleet",
                "allowFleet",
                TypeInfo(bool),
            ),
            (
                "allow_image_builder",
                "allowImageBuilder",
                TypeInfo(bool),
            ),
        ]

    # Indicates whether the image can be used for a fleet.
    allow_fleet: bool = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Indicates whether the image can be used for an image builder.
    allow_image_builder: bool = dataclasses.field(default=ShapeBase.NOT_SET, )


class ImageState(str):
    PENDING = "PENDING"
    AVAILABLE = "AVAILABLE"
    FAILED = "FAILED"
    COPYING = "COPYING"
    DELETING = "DELETING"


@dataclasses.dataclass
class ImageStateChangeReason(ShapeBase):
    """
    Describes the reason why the last image state change occurred.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "code",
                "Code",
                TypeInfo(typing.Union[str, ImageStateChangeReasonCode]),
            ),
            (
                "message",
                "Message",
                TypeInfo(str),
            ),
        ]

    # The state change reason code.
    code: typing.Union[str, "ImageStateChangeReasonCode"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The state change reason message.
    message: str = dataclasses.field(default=ShapeBase.NOT_SET, )


class ImageStateChangeReasonCode(str):
    INTERNAL_ERROR = "INTERNAL_ERROR"
    IMAGE_BUILDER_NOT_AVAILABLE = "IMAGE_BUILDER_NOT_AVAILABLE"
    IMAGE_COPY_FAILURE = "IMAGE_COPY_FAILURE"


@dataclasses.dataclass
class IncompatibleImageException(ShapeBase):
    """
    The image does not support storage connectors.
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

    # The error message in the exception.
    message: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class InvalidAccountStatusException(ShapeBase):
    """
    The resource cannot be created because your AWS account is suspended. For
    assistance, contact AWS Support.
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

    # The error message in the exception.
    message: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class InvalidParameterCombinationException(ShapeBase):
    """
    Indicates an incorrect combination of parameters, or a missing parameter.
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

    # The error message in the exception.
    message: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class InvalidRoleException(ShapeBase):
    """
    The specified role is invalid.
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

    # The error message in the exception.
    message: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class LimitExceededException(ShapeBase):
    """
    The requested limit exceeds the permitted limit for an account.
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

    # The error message in the exception.
    message: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ListAssociatedFleetsRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "stack_name",
                "StackName",
                TypeInfo(str),
            ),
            (
                "next_token",
                "NextToken",
                TypeInfo(str),
            ),
        ]

    # The name of the stack.
    stack_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The pagination token to use to retrieve the next page of results for this
    # operation. If this value is null, it retrieves the first page.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ListAssociatedFleetsResult(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "names",
                "Names",
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

    # The name of the fleet.
    names: typing.List[str] = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The pagination token to use to retrieve the next page of results for this
    # operation. If there are no more pages, this value is null.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ListAssociatedStacksRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "fleet_name",
                "FleetName",
                TypeInfo(str),
            ),
            (
                "next_token",
                "NextToken",
                TypeInfo(str),
            ),
        ]

    # The name of the fleet.
    fleet_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The pagination token to use to retrieve the next page of results for this
    # operation. If this value is null, it retrieves the first page.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ListAssociatedStacksResult(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "names",
                "Names",
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

    # The name of the stack.
    names: typing.List[str] = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The pagination token to use to retrieve the next page of results for this
    # operation. If there are no more pages, this value is null.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ListTagsForResourceRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "resource_arn",
                "ResourceArn",
                TypeInfo(str),
            ),
        ]

    # The Amazon Resource Name (ARN) of the resource.
    resource_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ListTagsForResourceResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
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

    # The information about the tags.
    tags: typing.Dict[str, str] = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class NetworkAccessConfiguration(ShapeBase):
    """
    The network details of the fleet instance for the streaming session.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "eni_private_ip_address",
                "EniPrivateIpAddress",
                TypeInfo(str),
            ),
            (
                "eni_id",
                "EniId",
                TypeInfo(str),
            ),
        ]

    # The private IP address of the elastic network interface that is attached to
    # instances in your VPC.
    eni_private_ip_address: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The resource identifier of the elastic network interface that is attached
    # to instances in your VPC. All network interfaces have the eni-xxxxxxxx
    # resource identifier.
    eni_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class OperationNotPermittedException(ShapeBase):
    """
    The attempted operation is not permitted.
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

    # The error message in the exception.
    message: str = dataclasses.field(default=ShapeBase.NOT_SET, )


class Permission(str):
    ENABLED = "ENABLED"
    DISABLED = "DISABLED"


class PlatformType(str):
    WINDOWS = "WINDOWS"


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
                "Message",
                TypeInfo(str),
            ),
        ]

    # The error message in the exception.
    message: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ResourceError(ShapeBase):
    """
    Describes a resource error.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "error_code",
                "ErrorCode",
                TypeInfo(typing.Union[str, FleetErrorCode]),
            ),
            (
                "error_message",
                "ErrorMessage",
                TypeInfo(str),
            ),
            (
                "error_timestamp",
                "ErrorTimestamp",
                TypeInfo(datetime.datetime),
            ),
        ]

    # The error code.
    error_code: typing.Union[str, "FleetErrorCode"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The error message.
    error_message: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The time the error occurred.
    error_timestamp: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class ResourceInUseException(ShapeBase):
    """
    The specified resource is in use.
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

    # The error message in the exception.
    message: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ResourceNotAvailableException(ShapeBase):
    """
    The specified resource exists and is not in use, but isn't available.
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

    # The error message in the exception.
    message: str = dataclasses.field(default=ShapeBase.NOT_SET, )


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

    # The error message in the exception.
    message: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ServiceAccountCredentials(ShapeBase):
    """
    Describes the credentials for the service account used by the streaming instance
    to connect to the directory.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "account_name",
                "AccountName",
                TypeInfo(str),
            ),
            (
                "account_password",
                "AccountPassword",
                TypeInfo(str),
            ),
        ]

    # The user name of the account. This account must have the following
    # privileges: create computer objects, join computers to the domain, and
    # change/reset the password on descendant computer objects for the
    # organizational units specified.
    account_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The password for the account.
    account_password: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class Session(ShapeBase):
    """
    Describes a streaming session.
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
                "user_id",
                "UserId",
                TypeInfo(str),
            ),
            (
                "stack_name",
                "StackName",
                TypeInfo(str),
            ),
            (
                "fleet_name",
                "FleetName",
                TypeInfo(str),
            ),
            (
                "state",
                "State",
                TypeInfo(typing.Union[str, SessionState]),
            ),
            (
                "authentication_type",
                "AuthenticationType",
                TypeInfo(typing.Union[str, AuthenticationType]),
            ),
            (
                "network_access_configuration",
                "NetworkAccessConfiguration",
                TypeInfo(NetworkAccessConfiguration),
            ),
        ]

    # The ID of the streaming session.
    id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The identifier of the user for whom the session was created.
    user_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The name of the stack for the streaming session.
    stack_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The name of the fleet for the streaming session.
    fleet_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The current state of the streaming session.
    state: typing.Union[str, "SessionState"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The authentication method. The user is authenticated using a streaming URL
    # (`API`) or SAML federation (`SAML`).
    authentication_type: typing.Union[str, "AuthenticationType"
                                     ] = dataclasses.field(
                                         default=ShapeBase.NOT_SET,
                                     )

    # The network details for the streaming session.
    network_access_configuration: "NetworkAccessConfiguration" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


class SessionState(str):
    """
    Possible values for the state of a streaming session.
    """
    ACTIVE = "ACTIVE"
    PENDING = "PENDING"
    EXPIRED = "EXPIRED"


@dataclasses.dataclass
class SharedImagePermissions(ShapeBase):
    """
    Describes the permissions that are available to the specified AWS account for a
    shared image.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "shared_account_id",
                "sharedAccountId",
                TypeInfo(str),
            ),
            (
                "image_permissions",
                "imagePermissions",
                TypeInfo(ImagePermissions),
            ),
        ]

    # The 12-digit ID of the AWS account with which the image is shared.
    shared_account_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Describes the permissions for a shared image.
    image_permissions: "ImagePermissions" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class Stack(ShapeBase):
    """
    Describes a stack.
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
                "arn",
                "Arn",
                TypeInfo(str),
            ),
            (
                "description",
                "Description",
                TypeInfo(str),
            ),
            (
                "display_name",
                "DisplayName",
                TypeInfo(str),
            ),
            (
                "created_time",
                "CreatedTime",
                TypeInfo(datetime.datetime),
            ),
            (
                "storage_connectors",
                "StorageConnectors",
                TypeInfo(typing.List[StorageConnector]),
            ),
            (
                "redirect_url",
                "RedirectURL",
                TypeInfo(str),
            ),
            (
                "feedback_url",
                "FeedbackURL",
                TypeInfo(str),
            ),
            (
                "stack_errors",
                "StackErrors",
                TypeInfo(typing.List[StackError]),
            ),
            (
                "user_settings",
                "UserSettings",
                TypeInfo(typing.List[UserSetting]),
            ),
            (
                "application_settings",
                "ApplicationSettings",
                TypeInfo(ApplicationSettingsResponse),
            ),
        ]

    # The name of the stack.
    name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The ARN of the stack.
    arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The description for display.
    description: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The stack name for display.
    display_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The time the stack was created.
    created_time: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The storage connectors to enable.
    storage_connectors: typing.List["StorageConnector"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The URL that users are redirected to after their streaming session ends.
    redirect_url: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The URL that users are redirected to after they click the Send Feedback
    # link. If no URL is specified, no Send Feedback link is displayed.
    feedback_url: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The errors for the stack.
    stack_errors: typing.List["StackError"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The actions that are enabled or disabled for users during their streaming
    # sessions. By default these actions are enabled.
    user_settings: typing.List["UserSetting"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The persistent application settings for users of the stack.
    application_settings: "ApplicationSettingsResponse" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


class StackAttribute(str):
    STORAGE_CONNECTORS = "STORAGE_CONNECTORS"
    STORAGE_CONNECTOR_HOMEFOLDERS = "STORAGE_CONNECTOR_HOMEFOLDERS"
    STORAGE_CONNECTOR_GOOGLE_DRIVE = "STORAGE_CONNECTOR_GOOGLE_DRIVE"
    STORAGE_CONNECTOR_ONE_DRIVE = "STORAGE_CONNECTOR_ONE_DRIVE"
    REDIRECT_URL = "REDIRECT_URL"
    FEEDBACK_URL = "FEEDBACK_URL"
    THEME_NAME = "THEME_NAME"
    USER_SETTINGS = "USER_SETTINGS"


@dataclasses.dataclass
class StackError(ShapeBase):
    """
    Describes a stack error.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "error_code",
                "ErrorCode",
                TypeInfo(typing.Union[str, StackErrorCode]),
            ),
            (
                "error_message",
                "ErrorMessage",
                TypeInfo(str),
            ),
        ]

    # The error code.
    error_code: typing.Union[str, "StackErrorCode"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The error message.
    error_message: str = dataclasses.field(default=ShapeBase.NOT_SET, )


class StackErrorCode(str):
    STORAGE_CONNECTOR_ERROR = "STORAGE_CONNECTOR_ERROR"
    INTERNAL_SERVICE_ERROR = "INTERNAL_SERVICE_ERROR"


@dataclasses.dataclass
class StartFleetRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "name",
                "Name",
                TypeInfo(str),
            ),
        ]

    # The name of the fleet.
    name: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class StartFleetResult(OutputShapeBase):
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
class StartImageBuilderRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "name",
                "Name",
                TypeInfo(str),
            ),
            (
                "appstream_agent_version",
                "AppstreamAgentVersion",
                TypeInfo(str),
            ),
        ]

    # The name of the image builder.
    name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The version of the AppStream 2.0 agent to use for this image builder. To
    # use the latest version of the AppStream 2.0 agent, specify [LATEST].
    appstream_agent_version: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class StartImageBuilderResult(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "image_builder",
                "ImageBuilder",
                TypeInfo(ImageBuilder),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Information about the image builder.
    image_builder: "ImageBuilder" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class StopFleetRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "name",
                "Name",
                TypeInfo(str),
            ),
        ]

    # The name of the fleet.
    name: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class StopFleetResult(OutputShapeBase):
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
class StopImageBuilderRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "name",
                "Name",
                TypeInfo(str),
            ),
        ]

    # The name of the image builder.
    name: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class StopImageBuilderResult(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "image_builder",
                "ImageBuilder",
                TypeInfo(ImageBuilder),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Information about the image builder.
    image_builder: "ImageBuilder" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class StorageConnector(ShapeBase):
    """
    Describes a connector to enable persistent storage for users.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "connector_type",
                "ConnectorType",
                TypeInfo(typing.Union[str, StorageConnectorType]),
            ),
            (
                "resource_identifier",
                "ResourceIdentifier",
                TypeInfo(str),
            ),
            (
                "domains",
                "Domains",
                TypeInfo(typing.List[str]),
            ),
        ]

    # The type of storage connector.
    connector_type: typing.Union[str, "StorageConnectorType"
                                ] = dataclasses.field(
                                    default=ShapeBase.NOT_SET,
                                )

    # The ARN of the storage connector.
    resource_identifier: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The names of the domains for the G Suite account.
    domains: typing.List[str] = dataclasses.field(default=ShapeBase.NOT_SET, )


class StorageConnectorType(str):
    """
    The type of storage connector.
    """
    HOMEFOLDERS = "HOMEFOLDERS"
    GOOGLE_DRIVE = "GOOGLE_DRIVE"
    ONE_DRIVE = "ONE_DRIVE"


@dataclasses.dataclass
class TagResourceRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "resource_arn",
                "ResourceArn",
                TypeInfo(str),
            ),
            (
                "tags",
                "Tags",
                TypeInfo(typing.Dict[str, str]),
            ),
        ]

    # The Amazon Resource Name (ARN) of the resource.
    resource_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The tags to associate. A tag is a key-value pair (the value is optional).
    # For example, `Environment=Test`, or, if you do not specify a value,
    # `Environment=`.

    # If you do not specify a value, we set the value to an empty string.
    tags: typing.Dict[str, str] = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class TagResourceResponse(OutputShapeBase):
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
class UntagResourceRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "resource_arn",
                "ResourceArn",
                TypeInfo(str),
            ),
            (
                "tag_keys",
                "TagKeys",
                TypeInfo(typing.List[str]),
            ),
        ]

    # The Amazon Resource Name (ARN) of the resource.
    resource_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The tag keys for the tags to disassociate.
    tag_keys: typing.List[str] = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class UntagResourceResponse(OutputShapeBase):
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
class UpdateDirectoryConfigRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "directory_name",
                "DirectoryName",
                TypeInfo(str),
            ),
            (
                "organizational_unit_distinguished_names",
                "OrganizationalUnitDistinguishedNames",
                TypeInfo(typing.List[str]),
            ),
            (
                "service_account_credentials",
                "ServiceAccountCredentials",
                TypeInfo(ServiceAccountCredentials),
            ),
        ]

    # The name of the Directory Config object.
    directory_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The distinguished names of the organizational units for computer accounts.
    organizational_unit_distinguished_names: typing.List[
        str] = dataclasses.field(
            default=ShapeBase.NOT_SET,
        )

    # The credentials for the service account used by the streaming instance to
    # connect to the directory.
    service_account_credentials: "ServiceAccountCredentials" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class UpdateDirectoryConfigResult(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "directory_config",
                "DirectoryConfig",
                TypeInfo(DirectoryConfig),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Information about the Directory Config object.
    directory_config: "DirectoryConfig" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class UpdateFleetRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "image_name",
                "ImageName",
                TypeInfo(str),
            ),
            (
                "image_arn",
                "ImageArn",
                TypeInfo(str),
            ),
            (
                "name",
                "Name",
                TypeInfo(str),
            ),
            (
                "instance_type",
                "InstanceType",
                TypeInfo(str),
            ),
            (
                "compute_capacity",
                "ComputeCapacity",
                TypeInfo(ComputeCapacity),
            ),
            (
                "vpc_config",
                "VpcConfig",
                TypeInfo(VpcConfig),
            ),
            (
                "max_user_duration_in_seconds",
                "MaxUserDurationInSeconds",
                TypeInfo(int),
            ),
            (
                "disconnect_timeout_in_seconds",
                "DisconnectTimeoutInSeconds",
                TypeInfo(int),
            ),
            (
                "delete_vpc_config",
                "DeleteVpcConfig",
                TypeInfo(bool),
            ),
            (
                "description",
                "Description",
                TypeInfo(str),
            ),
            (
                "display_name",
                "DisplayName",
                TypeInfo(str),
            ),
            (
                "enable_default_internet_access",
                "EnableDefaultInternetAccess",
                TypeInfo(bool),
            ),
            (
                "domain_join_info",
                "DomainJoinInfo",
                TypeInfo(DomainJoinInfo),
            ),
            (
                "attributes_to_delete",
                "AttributesToDelete",
                TypeInfo(typing.List[typing.Union[str, FleetAttribute]]),
            ),
        ]

    # The name of the image used to create the fleet.
    image_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The ARN of the public, private, or shared image to use.
    image_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A unique name for the fleet.
    name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The instance type to use when launching fleet instances. The following
    # instance types are available:

    #   * stream.standard.medium

    #   * stream.standard.large

    #   * stream.compute.large

    #   * stream.compute.xlarge

    #   * stream.compute.2xlarge

    #   * stream.compute.4xlarge

    #   * stream.compute.8xlarge

    #   * stream.memory.large

    #   * stream.memory.xlarge

    #   * stream.memory.2xlarge

    #   * stream.memory.4xlarge

    #   * stream.memory.8xlarge

    #   * stream.graphics-design.large

    #   * stream.graphics-design.xlarge

    #   * stream.graphics-design.2xlarge

    #   * stream.graphics-design.4xlarge

    #   * stream.graphics-desktop.2xlarge

    #   * stream.graphics-pro.4xlarge

    #   * stream.graphics-pro.8xlarge

    #   * stream.graphics-pro.16xlarge
    instance_type: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The desired capacity for the fleet.
    compute_capacity: "ComputeCapacity" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The VPC configuration for the fleet.
    vpc_config: "VpcConfig" = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The maximum time that a streaming session can run, in seconds. Specify a
    # value between 600 and 57600.
    max_user_duration_in_seconds: int = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The time after disconnection when a session is considered to have ended, in
    # seconds. If a user who was disconnected reconnects within this time
    # interval, the user is connected to their previous session. Specify a value
    # between 60 and 57600.
    disconnect_timeout_in_seconds: int = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Deletes the VPC association for the specified fleet.
    delete_vpc_config: bool = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The description for display.
    description: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The fleet name for display.
    display_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Enables or disables default internet access for the fleet.
    enable_default_internet_access: bool = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The information needed to join a Microsoft Active Directory domain.
    domain_join_info: "DomainJoinInfo" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The fleet attributes to delete.
    attributes_to_delete: typing.List[typing.Union[str, "FleetAttribute"]
                                     ] = dataclasses.field(
                                         default=ShapeBase.NOT_SET,
                                     )


@dataclasses.dataclass
class UpdateFleetResult(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "fleet",
                "Fleet",
                TypeInfo(Fleet),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Information about the fleet.
    fleet: "Fleet" = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class UpdateImagePermissionsRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "name",
                "Name",
                TypeInfo(str),
            ),
            (
                "shared_account_id",
                "SharedAccountId",
                TypeInfo(str),
            ),
            (
                "image_permissions",
                "ImagePermissions",
                TypeInfo(ImagePermissions),
            ),
        ]

    # The name of the private image.
    name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The 12-digit ID of the AWS account for which you want add or update image
    # permissions.
    shared_account_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The permissions for the image.
    image_permissions: "ImagePermissions" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class UpdateImagePermissionsResult(OutputShapeBase):
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
class UpdateStackRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
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
                "description",
                "Description",
                TypeInfo(str),
            ),
            (
                "storage_connectors",
                "StorageConnectors",
                TypeInfo(typing.List[StorageConnector]),
            ),
            (
                "delete_storage_connectors",
                "DeleteStorageConnectors",
                TypeInfo(bool),
            ),
            (
                "redirect_url",
                "RedirectURL",
                TypeInfo(str),
            ),
            (
                "feedback_url",
                "FeedbackURL",
                TypeInfo(str),
            ),
            (
                "attributes_to_delete",
                "AttributesToDelete",
                TypeInfo(typing.List[typing.Union[str, StackAttribute]]),
            ),
            (
                "user_settings",
                "UserSettings",
                TypeInfo(typing.List[UserSetting]),
            ),
            (
                "application_settings",
                "ApplicationSettings",
                TypeInfo(ApplicationSettings),
            ),
        ]

    # The name of the stack.
    name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The stack name for display.
    display_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The description for display.
    description: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The storage connectors to enable.
    storage_connectors: typing.List["StorageConnector"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Deletes the storage connectors currently enabled for the stack.
    delete_storage_connectors: bool = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The URL that users are redirected to after their streaming session ends.
    redirect_url: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The URL that users are redirected to after they click the Send Feedback
    # link. If no URL is specified, no Send Feedback link is displayed.
    feedback_url: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The stack attributes to delete.
    attributes_to_delete: typing.List[typing.Union[str, "StackAttribute"]
                                     ] = dataclasses.field(
                                         default=ShapeBase.NOT_SET,
                                     )

    # The actions that are enabled or disabled for users during their streaming
    # sessions. By default, these actions are enabled.
    user_settings: typing.List["UserSetting"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The persistent application settings for users of a stack. When these
    # settings are enabled, changes that users make to applications and Windows
    # settings are automatically saved after each session and applied to the next
    # session.
    application_settings: "ApplicationSettings" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class UpdateStackResult(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "stack",
                "Stack",
                TypeInfo(Stack),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Information about the stack.
    stack: "Stack" = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class UserSetting(ShapeBase):
    """
    Describes an action and whether the action is enabled or disabled for users
    during their streaming sessions.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "action",
                "Action",
                TypeInfo(typing.Union[str, Action]),
            ),
            (
                "permission",
                "Permission",
                TypeInfo(typing.Union[str, Permission]),
            ),
        ]

    # The action that is enabled or disabled.
    action: typing.Union[str, "Action"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Indicates whether the action is enabled or disabled.
    permission: typing.Union[str, "Permission"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


class VisibilityType(str):
    PUBLIC = "PUBLIC"
    PRIVATE = "PRIVATE"
    SHARED = "SHARED"


@dataclasses.dataclass
class VpcConfig(ShapeBase):
    """
    Describes VPC configuration information.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "subnet_ids",
                "SubnetIds",
                TypeInfo(typing.List[str]),
            ),
            (
                "security_group_ids",
                "SecurityGroupIds",
                TypeInfo(typing.List[str]),
            ),
        ]

    # The subnets to which a network interface is established from the fleet
    # instance.
    subnet_ids: typing.List[str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The security groups for the fleet.
    security_group_ids: typing.List[str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )
