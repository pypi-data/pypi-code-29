import datetime
import typing
from autoboto import ShapeBase, OutputShapeBase, TypeInfo
import dataclasses


@dataclasses.dataclass
class BadRequestException(ShapeBase):
    """
    Returns information about an error.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "error_attribute",
                "ErrorAttribute",
                TypeInfo(str),
            ),
            (
                "message",
                "Message",
                TypeInfo(str),
            ),
        ]

    # The attribute which caused the error.
    error_attribute: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The explanation of the error.
    message: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class BrokerInstance(ShapeBase):
    """
    Returns information about all brokers.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "console_url",
                "ConsoleURL",
                TypeInfo(str),
            ),
            (
                "endpoints",
                "Endpoints",
                TypeInfo(typing.List[str]),
            ),
            (
                "ip_address",
                "IpAddress",
                TypeInfo(str),
            ),
        ]

    # The URL of the broker's ActiveMQ Web Console.
    console_url: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The broker's wire-level protocol endpoints.
    endpoints: typing.List[str] = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The IP address of the ENI attached to the broker.
    ip_address: str = dataclasses.field(default=ShapeBase.NOT_SET, )


class BrokerState(str):
    """
    The status of the broker.
    """
    CREATION_IN_PROGRESS = "CREATION_IN_PROGRESS"
    CREATION_FAILED = "CREATION_FAILED"
    DELETION_IN_PROGRESS = "DELETION_IN_PROGRESS"
    RUNNING = "RUNNING"
    REBOOT_IN_PROGRESS = "REBOOT_IN_PROGRESS"


@dataclasses.dataclass
class BrokerSummary(ShapeBase):
    """
    The Amazon Resource Name (ARN) of the broker.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "broker_arn",
                "BrokerArn",
                TypeInfo(str),
            ),
            (
                "broker_id",
                "BrokerId",
                TypeInfo(str),
            ),
            (
                "broker_name",
                "BrokerName",
                TypeInfo(str),
            ),
            (
                "broker_state",
                "BrokerState",
                TypeInfo(typing.Union[str, BrokerState]),
            ),
            (
                "created",
                "Created",
                TypeInfo(datetime.datetime),
            ),
            (
                "deployment_mode",
                "DeploymentMode",
                TypeInfo(typing.Union[str, DeploymentMode]),
            ),
            (
                "host_instance_type",
                "HostInstanceType",
                TypeInfo(str),
            ),
        ]

    # The Amazon Resource Name (ARN) of the broker.
    broker_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The unique ID that Amazon MQ generates for the broker.
    broker_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The name of the broker. This value must be unique in your AWS account, 1-50
    # characters long, must contain only letters, numbers, dashes, and
    # underscores, and must not contain whitespaces, brackets, wildcard
    # characters, or special characters.
    broker_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The status of the broker.
    broker_state: typing.Union[str, "BrokerState"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The time when the broker was created.
    created: datetime.datetime = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Required. The deployment mode of the broker.
    deployment_mode: typing.Union[str, "DeploymentMode"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The broker's instance type.
    host_instance_type: str = dataclasses.field(default=ShapeBase.NOT_SET, )


class ChangeType(str):
    """
    The type of change pending for the ActiveMQ user.
    """
    CREATE = "CREATE"
    UPDATE = "UPDATE"
    DELETE = "DELETE"


@dataclasses.dataclass
class Configuration(ShapeBase):
    """
    Returns information about all configurations.
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
                "created",
                "Created",
                TypeInfo(datetime.datetime),
            ),
            (
                "description",
                "Description",
                TypeInfo(str),
            ),
            (
                "engine_type",
                "EngineType",
                TypeInfo(typing.Union[str, EngineType]),
            ),
            (
                "engine_version",
                "EngineVersion",
                TypeInfo(str),
            ),
            (
                "id",
                "Id",
                TypeInfo(str),
            ),
            (
                "latest_revision",
                "LatestRevision",
                TypeInfo(ConfigurationRevision),
            ),
            (
                "name",
                "Name",
                TypeInfo(str),
            ),
        ]

    # Required. The ARN of the configuration.
    arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Required. The date and time of the configuration revision.
    created: datetime.datetime = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Required. The description of the configuration.
    description: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Required. The type of broker engine. Note: Currently, Amazon MQ supports
    # only ACTIVEMQ.
    engine_type: typing.Union[str, "EngineType"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Required. The version of the broker engine.
    engine_version: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Required. The unique ID that Amazon MQ generates for the configuration.
    id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Required. The latest revision of the configuration.
    latest_revision: "ConfigurationRevision" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Required. The name of the configuration. This value can contain only
    # alphanumeric characters, dashes, periods, underscores, and tildes (- . _
    # ~). This value must be 1-150 characters long.
    name: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ConfigurationId(ShapeBase):
    """
    A list of information about the configuration.
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
                "revision",
                "Revision",
                TypeInfo(int),
            ),
        ]

    # Required. The unique ID that Amazon MQ generates for the configuration.
    id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The revision number of the configuration.
    revision: int = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ConfigurationRevision(ShapeBase):
    """
    Returns information about the specified configuration revision.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "created",
                "Created",
                TypeInfo(datetime.datetime),
            ),
            (
                "description",
                "Description",
                TypeInfo(str),
            ),
            (
                "revision",
                "Revision",
                TypeInfo(int),
            ),
        ]

    # Required. The date and time of the configuration revision.
    created: datetime.datetime = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The description of the configuration revision.
    description: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Required. The revision number of the configuration.
    revision: int = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class Configurations(ShapeBase):
    """
    Broker configuration information
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "current",
                "Current",
                TypeInfo(ConfigurationId),
            ),
            (
                "history",
                "History",
                TypeInfo(typing.List[ConfigurationId]),
            ),
            (
                "pending",
                "Pending",
                TypeInfo(ConfigurationId),
            ),
        ]

    # The current configuration of the broker.
    current: "ConfigurationId" = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The history of configurations applied to the broker.
    history: typing.List["ConfigurationId"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The pending configuration of the broker.
    pending: "ConfigurationId" = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ConflictException(ShapeBase):
    """
    Returns information about an error.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "error_attribute",
                "ErrorAttribute",
                TypeInfo(str),
            ),
            (
                "message",
                "Message",
                TypeInfo(str),
            ),
        ]

    # The attribute which caused the error.
    error_attribute: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The explanation of the error.
    message: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class CreateBrokerInput(ShapeBase):
    """
    Required. The time period during which Amazon MQ applies pending updates or
    patches to the broker.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "auto_minor_version_upgrade",
                "AutoMinorVersionUpgrade",
                TypeInfo(bool),
            ),
            (
                "broker_name",
                "BrokerName",
                TypeInfo(str),
            ),
            (
                "configuration",
                "Configuration",
                TypeInfo(ConfigurationId),
            ),
            (
                "creator_request_id",
                "CreatorRequestId",
                TypeInfo(str),
            ),
            (
                "deployment_mode",
                "DeploymentMode",
                TypeInfo(typing.Union[str, DeploymentMode]),
            ),
            (
                "engine_type",
                "EngineType",
                TypeInfo(typing.Union[str, EngineType]),
            ),
            (
                "engine_version",
                "EngineVersion",
                TypeInfo(str),
            ),
            (
                "host_instance_type",
                "HostInstanceType",
                TypeInfo(str),
            ),
            (
                "logs",
                "Logs",
                TypeInfo(Logs),
            ),
            (
                "maintenance_window_start_time",
                "MaintenanceWindowStartTime",
                TypeInfo(WeeklyStartTime),
            ),
            (
                "publicly_accessible",
                "PubliclyAccessible",
                TypeInfo(bool),
            ),
            (
                "security_groups",
                "SecurityGroups",
                TypeInfo(typing.List[str]),
            ),
            (
                "subnet_ids",
                "SubnetIds",
                TypeInfo(typing.List[str]),
            ),
            (
                "users",
                "Users",
                TypeInfo(typing.List[User]),
            ),
        ]

    # Required. Enables automatic upgrades to new minor versions for brokers, as
    # Apache releases the versions. The automatic upgrades occur during the
    # maintenance window of the broker or after a manual broker reboot.
    auto_minor_version_upgrade: bool = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Required. The name of the broker. This value must be unique in your AWS
    # account, 1-50 characters long, must contain only letters, numbers, dashes,
    # and underscores, and must not contain whitespaces, brackets, wildcard
    # characters, or special characters.
    broker_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A list of information about the configuration.
    configuration: "ConfigurationId" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The unique ID that the requester receives for the created broker. Amazon MQ
    # passes your ID with the API action. Note: We recommend using a Universally
    # Unique Identifier (UUID) for the creatorRequestId. You may omit the
    # creatorRequestId if your application doesn't require idempotency.
    creator_request_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Required. The deployment mode of the broker.
    deployment_mode: typing.Union[str, "DeploymentMode"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Required. The type of broker engine. Note: Currently, Amazon MQ supports
    # only ACTIVEMQ.
    engine_type: typing.Union[str, "EngineType"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Required. The version of the broker engine. Note: Currently, Amazon MQ
    # supports only 5.15.0.
    engine_version: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Required. The broker's instance type.
    host_instance_type: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Enables Amazon CloudWatch logging for brokers.
    logs: "Logs" = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The parameters that determine the WeeklyStartTime.
    maintenance_window_start_time: "WeeklyStartTime" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Required. Enables connections from applications outside of the VPC that
    # hosts the broker's subnets.
    publicly_accessible: bool = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The list of rules (1 minimum, 125 maximum) that authorize connections to
    # brokers.
    security_groups: typing.List[str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The list of groups (2 maximum) that define which subnets and IP ranges the
    # broker can use from different Availability Zones. A SINGLE_INSTANCE
    # deployment requires one subnet (for example, the default subnet). An
    # ACTIVE_STANDBY_MULTI_AZ deployment requires two subnets.
    subnet_ids: typing.List[str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Required. The list of ActiveMQ users (persons or applications) who can
    # access queues and topics. This value can contain only alphanumeric
    # characters, dashes, periods, underscores, and tildes (- . _ ~). This value
    # must be 2-100 characters long.
    users: typing.List["User"] = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class CreateBrokerOutput(ShapeBase):
    """
    Returns information about the created broker.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "broker_arn",
                "BrokerArn",
                TypeInfo(str),
            ),
            (
                "broker_id",
                "BrokerId",
                TypeInfo(str),
            ),
        ]

    # The Amazon Resource Name (ARN) of the broker.
    broker_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The unique ID that Amazon MQ generates for the broker.
    broker_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class CreateBrokerRequest(ShapeBase):
    """
    Creates a broker using the specified properties.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "auto_minor_version_upgrade",
                "AutoMinorVersionUpgrade",
                TypeInfo(bool),
            ),
            (
                "broker_name",
                "BrokerName",
                TypeInfo(str),
            ),
            (
                "configuration",
                "Configuration",
                TypeInfo(ConfigurationId),
            ),
            (
                "creator_request_id",
                "CreatorRequestId",
                TypeInfo(str),
            ),
            (
                "deployment_mode",
                "DeploymentMode",
                TypeInfo(typing.Union[str, DeploymentMode]),
            ),
            (
                "engine_type",
                "EngineType",
                TypeInfo(typing.Union[str, EngineType]),
            ),
            (
                "engine_version",
                "EngineVersion",
                TypeInfo(str),
            ),
            (
                "host_instance_type",
                "HostInstanceType",
                TypeInfo(str),
            ),
            (
                "logs",
                "Logs",
                TypeInfo(Logs),
            ),
            (
                "maintenance_window_start_time",
                "MaintenanceWindowStartTime",
                TypeInfo(WeeklyStartTime),
            ),
            (
                "publicly_accessible",
                "PubliclyAccessible",
                TypeInfo(bool),
            ),
            (
                "security_groups",
                "SecurityGroups",
                TypeInfo(typing.List[str]),
            ),
            (
                "subnet_ids",
                "SubnetIds",
                TypeInfo(typing.List[str]),
            ),
            (
                "users",
                "Users",
                TypeInfo(typing.List[User]),
            ),
        ]

    # Required. Enables automatic upgrades to new minor versions for brokers, as
    # Apache releases the versions. The automatic upgrades occur during the
    # maintenance window of the broker or after a manual broker reboot.
    auto_minor_version_upgrade: bool = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Required. The name of the broker. This value must be unique in your AWS
    # account, 1-50 characters long, must contain only letters, numbers, dashes,
    # and underscores, and must not contain whitespaces, brackets, wildcard
    # characters, or special characters.
    broker_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A list of information about the configuration.
    configuration: "ConfigurationId" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The unique ID that the requester receives for the created broker. Amazon MQ
    # passes your ID with the API action. Note: We recommend using a Universally
    # Unique Identifier (UUID) for the creatorRequestId. You may omit the
    # creatorRequestId if your application doesn't require idempotency.
    creator_request_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Required. The deployment mode of the broker.
    deployment_mode: typing.Union[str, "DeploymentMode"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Required. The type of broker engine. Note: Currently, Amazon MQ supports
    # only ACTIVEMQ.
    engine_type: typing.Union[str, "EngineType"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Required. The version of the broker engine. Note: Currently, Amazon MQ
    # supports only 5.15.0.
    engine_version: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Required. The broker's instance type.
    host_instance_type: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Enables Amazon CloudWatch logging for brokers.
    logs: "Logs" = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The parameters that determine the WeeklyStartTime.
    maintenance_window_start_time: "WeeklyStartTime" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Required. Enables connections from applications outside of the VPC that
    # hosts the broker's subnets.
    publicly_accessible: bool = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The list of rules (1 minimum, 125 maximum) that authorize connections to
    # brokers.
    security_groups: typing.List[str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The list of groups (2 maximum) that define which subnets and IP ranges the
    # broker can use from different Availability Zones. A SINGLE_INSTANCE
    # deployment requires one subnet (for example, the default subnet). An
    # ACTIVE_STANDBY_MULTI_AZ deployment requires two subnets.
    subnet_ids: typing.List[str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Required. The list of ActiveMQ users (persons or applications) who can
    # access queues and topics. This value can contain only alphanumeric
    # characters, dashes, periods, underscores, and tildes (- . _ ~). This value
    # must be 2-100 characters long.
    users: typing.List["User"] = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class CreateBrokerResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "broker_arn",
                "BrokerArn",
                TypeInfo(str),
            ),
            (
                "broker_id",
                "BrokerId",
                TypeInfo(str),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The Amazon Resource Name (ARN) of the broker.
    broker_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The unique ID that Amazon MQ generates for the broker.
    broker_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class CreateConfigurationInput(ShapeBase):
    """
    Creates a new configuration for the specified configuration name. Amazon MQ uses
    the default configuration (the engine type and version).
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "engine_type",
                "EngineType",
                TypeInfo(typing.Union[str, EngineType]),
            ),
            (
                "engine_version",
                "EngineVersion",
                TypeInfo(str),
            ),
            (
                "name",
                "Name",
                TypeInfo(str),
            ),
        ]

    # Required. The type of broker engine. Note: Currently, Amazon MQ supports
    # only ACTIVEMQ.
    engine_type: typing.Union[str, "EngineType"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Required. The version of the broker engine. Note: Currently, Amazon MQ
    # supports only 5.15.0.
    engine_version: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Required. The name of the configuration. This value can contain only
    # alphanumeric characters, dashes, periods, underscores, and tildes (- . _
    # ~). This value must be 1-150 characters long.
    name: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class CreateConfigurationOutput(ShapeBase):
    """
    Returns information about the created configuration.
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
                "created",
                "Created",
                TypeInfo(datetime.datetime),
            ),
            (
                "id",
                "Id",
                TypeInfo(str),
            ),
            (
                "latest_revision",
                "LatestRevision",
                TypeInfo(ConfigurationRevision),
            ),
            (
                "name",
                "Name",
                TypeInfo(str),
            ),
        ]

    # Required. The Amazon Resource Name (ARN) of the configuration.
    arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Required. The date and time of the configuration.
    created: datetime.datetime = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Required. The unique ID that Amazon MQ generates for the configuration.
    id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The latest revision of the configuration.
    latest_revision: "ConfigurationRevision" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Required. The name of the configuration. This value can contain only
    # alphanumeric characters, dashes, periods, underscores, and tildes (- . _
    # ~). This value must be 1-150 characters long.
    name: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class CreateConfigurationRequest(ShapeBase):
    """
    Creates a new configuration for the specified configuration name. Amazon MQ uses
    the default configuration (the engine type and version).
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "engine_type",
                "EngineType",
                TypeInfo(typing.Union[str, EngineType]),
            ),
            (
                "engine_version",
                "EngineVersion",
                TypeInfo(str),
            ),
            (
                "name",
                "Name",
                TypeInfo(str),
            ),
        ]

    # Required. The type of broker engine. Note: Currently, Amazon MQ supports
    # only ACTIVEMQ.
    engine_type: typing.Union[str, "EngineType"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Required. The version of the broker engine. Note: Currently, Amazon MQ
    # supports only 5.15.0.
    engine_version: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Required. The name of the configuration. This value can contain only
    # alphanumeric characters, dashes, periods, underscores, and tildes (- . _
    # ~). This value must be 1-150 characters long.
    name: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class CreateConfigurationResponse(OutputShapeBase):
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
                "created",
                "Created",
                TypeInfo(datetime.datetime),
            ),
            (
                "id",
                "Id",
                TypeInfo(str),
            ),
            (
                "latest_revision",
                "LatestRevision",
                TypeInfo(ConfigurationRevision),
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

    # Required. The Amazon Resource Name (ARN) of the configuration.
    arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Required. The date and time of the configuration.
    created: datetime.datetime = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Required. The unique ID that Amazon MQ generates for the configuration.
    id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The latest revision of the configuration.
    latest_revision: "ConfigurationRevision" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Required. The name of the configuration. This value can contain only
    # alphanumeric characters, dashes, periods, underscores, and tildes (- . _
    # ~). This value must be 1-150 characters long.
    name: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class CreateUserInput(ShapeBase):
    """
    Creates a new ActiveMQ user.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "console_access",
                "ConsoleAccess",
                TypeInfo(bool),
            ),
            (
                "groups",
                "Groups",
                TypeInfo(typing.List[str]),
            ),
            (
                "password",
                "Password",
                TypeInfo(str),
            ),
        ]

    # Enables access to the the ActiveMQ Web Console for the ActiveMQ user.
    console_access: bool = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The list of groups (20 maximum) to which the ActiveMQ user belongs. This
    # value can contain only alphanumeric characters, dashes, periods,
    # underscores, and tildes (- . _ ~). This value must be 2-100 characters
    # long.
    groups: typing.List[str] = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Required. The password of the user. This value must be at least 12
    # characters long, must contain at least 4 unique characters, and must not
    # contain commas.
    password: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class CreateUserRequest(ShapeBase):
    """
    Creates a new ActiveMQ user.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "broker_id",
                "BrokerId",
                TypeInfo(str),
            ),
            (
                "username",
                "Username",
                TypeInfo(str),
            ),
            (
                "console_access",
                "ConsoleAccess",
                TypeInfo(bool),
            ),
            (
                "groups",
                "Groups",
                TypeInfo(typing.List[str]),
            ),
            (
                "password",
                "Password",
                TypeInfo(str),
            ),
        ]

    # The unique ID that Amazon MQ generates for the broker.
    broker_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The username of the ActiveMQ user. This value can contain only alphanumeric
    # characters, dashes, periods, underscores, and tildes (- . _ ~). This value
    # must be 2-100 characters long.
    username: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Enables access to the the ActiveMQ Web Console for the ActiveMQ user.
    console_access: bool = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The list of groups (20 maximum) to which the ActiveMQ user belongs. This
    # value can contain only alphanumeric characters, dashes, periods,
    # underscores, and tildes (- . _ ~). This value must be 2-100 characters
    # long.
    groups: typing.List[str] = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Required. The password of the user. This value must be at least 12
    # characters long, must contain at least 4 unique characters, and must not
    # contain commas.
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
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


class DayOfWeek(str):
    MONDAY = "MONDAY"
    TUESDAY = "TUESDAY"
    WEDNESDAY = "WEDNESDAY"
    THURSDAY = "THURSDAY"
    FRIDAY = "FRIDAY"
    SATURDAY = "SATURDAY"
    SUNDAY = "SUNDAY"


@dataclasses.dataclass
class DeleteBrokerOutput(ShapeBase):
    """
    Returns information about the deleted broker.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "broker_id",
                "BrokerId",
                TypeInfo(str),
            ),
        ]

    # The unique ID that Amazon MQ generates for the broker.
    broker_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DeleteBrokerRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "broker_id",
                "BrokerId",
                TypeInfo(str),
            ),
        ]

    # The name of the broker. This value must be unique in your AWS account, 1-50
    # characters long, must contain only letters, numbers, dashes, and
    # underscores, and must not contain whitespaces, brackets, wildcard
    # characters, or special characters.
    broker_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DeleteBrokerResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "broker_id",
                "BrokerId",
                TypeInfo(str),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The unique ID that Amazon MQ generates for the broker.
    broker_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DeleteUserRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "broker_id",
                "BrokerId",
                TypeInfo(str),
            ),
            (
                "username",
                "Username",
                TypeInfo(str),
            ),
        ]

    # The unique ID that Amazon MQ generates for the broker.
    broker_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The username of the ActiveMQ user. This value can contain only alphanumeric
    # characters, dashes, periods, underscores, and tildes (- . _ ~). This value
    # must be 2-100 characters long.
    username: str = dataclasses.field(default=ShapeBase.NOT_SET, )


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


class DeploymentMode(str):
    """
    The deployment mode of the broker.
    """
    SINGLE_INSTANCE = "SINGLE_INSTANCE"
    ACTIVE_STANDBY_MULTI_AZ = "ACTIVE_STANDBY_MULTI_AZ"


@dataclasses.dataclass
class DescribeBrokerOutput(ShapeBase):
    """
    The version of the broker engine. Note: Currently, Amazon MQ supports only
    5.15.0.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "auto_minor_version_upgrade",
                "AutoMinorVersionUpgrade",
                TypeInfo(bool),
            ),
            (
                "broker_arn",
                "BrokerArn",
                TypeInfo(str),
            ),
            (
                "broker_id",
                "BrokerId",
                TypeInfo(str),
            ),
            (
                "broker_instances",
                "BrokerInstances",
                TypeInfo(typing.List[BrokerInstance]),
            ),
            (
                "broker_name",
                "BrokerName",
                TypeInfo(str),
            ),
            (
                "broker_state",
                "BrokerState",
                TypeInfo(typing.Union[str, BrokerState]),
            ),
            (
                "configurations",
                "Configurations",
                TypeInfo(Configurations),
            ),
            (
                "created",
                "Created",
                TypeInfo(datetime.datetime),
            ),
            (
                "deployment_mode",
                "DeploymentMode",
                TypeInfo(typing.Union[str, DeploymentMode]),
            ),
            (
                "engine_type",
                "EngineType",
                TypeInfo(typing.Union[str, EngineType]),
            ),
            (
                "engine_version",
                "EngineVersion",
                TypeInfo(str),
            ),
            (
                "host_instance_type",
                "HostInstanceType",
                TypeInfo(str),
            ),
            (
                "logs",
                "Logs",
                TypeInfo(LogsSummary),
            ),
            (
                "maintenance_window_start_time",
                "MaintenanceWindowStartTime",
                TypeInfo(WeeklyStartTime),
            ),
            (
                "publicly_accessible",
                "PubliclyAccessible",
                TypeInfo(bool),
            ),
            (
                "security_groups",
                "SecurityGroups",
                TypeInfo(typing.List[str]),
            ),
            (
                "subnet_ids",
                "SubnetIds",
                TypeInfo(typing.List[str]),
            ),
            (
                "users",
                "Users",
                TypeInfo(typing.List[UserSummary]),
            ),
        ]

    # Required. Enables automatic upgrades to new minor versions for brokers, as
    # Apache releases the versions. The automatic upgrades occur during the
    # maintenance window of the broker or after a manual broker reboot.
    auto_minor_version_upgrade: bool = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The Amazon Resource Name (ARN) of the broker.
    broker_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The unique ID that Amazon MQ generates for the broker.
    broker_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A list of information about allocated brokers.
    broker_instances: typing.List["BrokerInstance"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The name of the broker. This value must be unique in your AWS account, 1-50
    # characters long, must contain only letters, numbers, dashes, and
    # underscores, and must not contain whitespaces, brackets, wildcard
    # characters, or special characters.
    broker_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The status of the broker.
    broker_state: typing.Union[str, "BrokerState"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The list of all revisions for the specified configuration.
    configurations: "Configurations" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The time when the broker was created.
    created: datetime.datetime = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Required. The deployment mode of the broker.
    deployment_mode: typing.Union[str, "DeploymentMode"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Required. The type of broker engine. Note: Currently, Amazon MQ supports
    # only ACTIVEMQ.
    engine_type: typing.Union[str, "EngineType"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The version of the broker engine. Note: Currently, Amazon MQ supports only
    # 5.15.0.
    engine_version: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The broker's instance type.
    host_instance_type: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The list of information about logs currently enabled and pending to be
    # deployed for the specified broker.
    logs: "LogsSummary" = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The parameters that determine the WeeklyStartTime.
    maintenance_window_start_time: "WeeklyStartTime" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Required. Enables connections from applications outside of the VPC that
    # hosts the broker's subnets.
    publicly_accessible: bool = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Required. The list of rules (1 minimum, 125 maximum) that authorize
    # connections to brokers.
    security_groups: typing.List[str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The list of groups (2 maximum) that define which subnets and IP ranges the
    # broker can use from different Availability Zones. A SINGLE_INSTANCE
    # deployment requires one subnet (for example, the default subnet). An
    # ACTIVE_STANDBY_MULTI_AZ deployment requires two subnets.
    subnet_ids: typing.List[str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The list of all ActiveMQ usernames for the specified broker.
    users: typing.List["UserSummary"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class DescribeBrokerRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "broker_id",
                "BrokerId",
                TypeInfo(str),
            ),
        ]

    # The name of the broker. This value must be unique in your AWS account, 1-50
    # characters long, must contain only letters, numbers, dashes, and
    # underscores, and must not contain whitespaces, brackets, wildcard
    # characters, or special characters.
    broker_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DescribeBrokerResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "auto_minor_version_upgrade",
                "AutoMinorVersionUpgrade",
                TypeInfo(bool),
            ),
            (
                "broker_arn",
                "BrokerArn",
                TypeInfo(str),
            ),
            (
                "broker_id",
                "BrokerId",
                TypeInfo(str),
            ),
            (
                "broker_instances",
                "BrokerInstances",
                TypeInfo(typing.List[BrokerInstance]),
            ),
            (
                "broker_name",
                "BrokerName",
                TypeInfo(str),
            ),
            (
                "broker_state",
                "BrokerState",
                TypeInfo(typing.Union[str, BrokerState]),
            ),
            (
                "configurations",
                "Configurations",
                TypeInfo(Configurations),
            ),
            (
                "created",
                "Created",
                TypeInfo(datetime.datetime),
            ),
            (
                "deployment_mode",
                "DeploymentMode",
                TypeInfo(typing.Union[str, DeploymentMode]),
            ),
            (
                "engine_type",
                "EngineType",
                TypeInfo(typing.Union[str, EngineType]),
            ),
            (
                "engine_version",
                "EngineVersion",
                TypeInfo(str),
            ),
            (
                "host_instance_type",
                "HostInstanceType",
                TypeInfo(str),
            ),
            (
                "logs",
                "Logs",
                TypeInfo(LogsSummary),
            ),
            (
                "maintenance_window_start_time",
                "MaintenanceWindowStartTime",
                TypeInfo(WeeklyStartTime),
            ),
            (
                "publicly_accessible",
                "PubliclyAccessible",
                TypeInfo(bool),
            ),
            (
                "security_groups",
                "SecurityGroups",
                TypeInfo(typing.List[str]),
            ),
            (
                "subnet_ids",
                "SubnetIds",
                TypeInfo(typing.List[str]),
            ),
            (
                "users",
                "Users",
                TypeInfo(typing.List[UserSummary]),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Required. Enables automatic upgrades to new minor versions for brokers, as
    # Apache releases the versions. The automatic upgrades occur during the
    # maintenance window of the broker or after a manual broker reboot.
    auto_minor_version_upgrade: bool = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The Amazon Resource Name (ARN) of the broker.
    broker_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The unique ID that Amazon MQ generates for the broker.
    broker_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A list of information about allocated brokers.
    broker_instances: typing.List["BrokerInstance"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The name of the broker. This value must be unique in your AWS account, 1-50
    # characters long, must contain only letters, numbers, dashes, and
    # underscores, and must not contain whitespaces, brackets, wildcard
    # characters, or special characters.
    broker_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The status of the broker.
    broker_state: typing.Union[str, "BrokerState"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The list of all revisions for the specified configuration.
    configurations: "Configurations" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The time when the broker was created.
    created: datetime.datetime = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Required. The deployment mode of the broker.
    deployment_mode: typing.Union[str, "DeploymentMode"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Required. The type of broker engine. Note: Currently, Amazon MQ supports
    # only ACTIVEMQ.
    engine_type: typing.Union[str, "EngineType"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The version of the broker engine. Note: Currently, Amazon MQ supports only
    # 5.15.0.
    engine_version: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The broker's instance type.
    host_instance_type: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The list of information about logs currently enabled and pending to be
    # deployed for the specified broker.
    logs: "LogsSummary" = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The parameters that determine the WeeklyStartTime.
    maintenance_window_start_time: "WeeklyStartTime" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Required. Enables connections from applications outside of the VPC that
    # hosts the broker's subnets.
    publicly_accessible: bool = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Required. The list of rules (1 minimum, 125 maximum) that authorize
    # connections to brokers.
    security_groups: typing.List[str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The list of groups (2 maximum) that define which subnets and IP ranges the
    # broker can use from different Availability Zones. A SINGLE_INSTANCE
    # deployment requires one subnet (for example, the default subnet). An
    # ACTIVE_STANDBY_MULTI_AZ deployment requires two subnets.
    subnet_ids: typing.List[str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The list of all ActiveMQ usernames for the specified broker.
    users: typing.List["UserSummary"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class DescribeConfigurationRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "configuration_id",
                "ConfigurationId",
                TypeInfo(str),
            ),
        ]

    # The unique ID that Amazon MQ generates for the configuration.
    configuration_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DescribeConfigurationResponse(OutputShapeBase):
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
                "created",
                "Created",
                TypeInfo(datetime.datetime),
            ),
            (
                "description",
                "Description",
                TypeInfo(str),
            ),
            (
                "engine_type",
                "EngineType",
                TypeInfo(typing.Union[str, EngineType]),
            ),
            (
                "engine_version",
                "EngineVersion",
                TypeInfo(str),
            ),
            (
                "id",
                "Id",
                TypeInfo(str),
            ),
            (
                "latest_revision",
                "LatestRevision",
                TypeInfo(ConfigurationRevision),
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

    # Required. The ARN of the configuration.
    arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Required. The date and time of the configuration revision.
    created: datetime.datetime = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Required. The description of the configuration.
    description: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Required. The type of broker engine. Note: Currently, Amazon MQ supports
    # only ACTIVEMQ.
    engine_type: typing.Union[str, "EngineType"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Required. The version of the broker engine.
    engine_version: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Required. The unique ID that Amazon MQ generates for the configuration.
    id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Required. The latest revision of the configuration.
    latest_revision: "ConfigurationRevision" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Required. The name of the configuration. This value can contain only
    # alphanumeric characters, dashes, periods, underscores, and tildes (- . _
    # ~). This value must be 1-150 characters long.
    name: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DescribeConfigurationRevisionOutput(ShapeBase):
    """
    Returns the specified configuration revision for the specified configuration.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "configuration_id",
                "ConfigurationId",
                TypeInfo(str),
            ),
            (
                "created",
                "Created",
                TypeInfo(datetime.datetime),
            ),
            (
                "data",
                "Data",
                TypeInfo(str),
            ),
            (
                "description",
                "Description",
                TypeInfo(str),
            ),
        ]

    # Required. The unique ID that Amazon MQ generates for the configuration.
    configuration_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Required. The date and time of the configuration.
    created: datetime.datetime = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Required. The base64-encoded XML configuration.
    data: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The description of the configuration.
    description: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DescribeConfigurationRevisionRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "configuration_id",
                "ConfigurationId",
                TypeInfo(str),
            ),
            (
                "configuration_revision",
                "ConfigurationRevision",
                TypeInfo(str),
            ),
        ]

    # The unique ID that Amazon MQ generates for the configuration.
    configuration_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The revision of the configuration.
    configuration_revision: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DescribeConfigurationRevisionResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "configuration_id",
                "ConfigurationId",
                TypeInfo(str),
            ),
            (
                "created",
                "Created",
                TypeInfo(datetime.datetime),
            ),
            (
                "data",
                "Data",
                TypeInfo(str),
            ),
            (
                "description",
                "Description",
                TypeInfo(str),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Required. The unique ID that Amazon MQ generates for the configuration.
    configuration_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Required. The date and time of the configuration.
    created: datetime.datetime = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Required. The base64-encoded XML configuration.
    data: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The description of the configuration.
    description: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DescribeUserOutput(ShapeBase):
    """
    Returns information about an ActiveMQ user.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "broker_id",
                "BrokerId",
                TypeInfo(str),
            ),
            (
                "console_access",
                "ConsoleAccess",
                TypeInfo(bool),
            ),
            (
                "groups",
                "Groups",
                TypeInfo(typing.List[str]),
            ),
            (
                "pending",
                "Pending",
                TypeInfo(UserPendingChanges),
            ),
            (
                "username",
                "Username",
                TypeInfo(str),
            ),
        ]

    # Required. The unique ID that Amazon MQ generates for the broker.
    broker_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Enables access to the the ActiveMQ Web Console for the ActiveMQ user.
    console_access: bool = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The list of groups (20 maximum) to which the ActiveMQ user belongs. This
    # value can contain only alphanumeric characters, dashes, periods,
    # underscores, and tildes (- . _ ~). This value must be 2-100 characters
    # long.
    groups: typing.List[str] = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The status of the changes pending for the ActiveMQ user.
    pending: "UserPendingChanges" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Required. The username of the ActiveMQ user. This value can contain only
    # alphanumeric characters, dashes, periods, underscores, and tildes (- . _
    # ~). This value must be 2-100 characters long.
    username: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DescribeUserRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "broker_id",
                "BrokerId",
                TypeInfo(str),
            ),
            (
                "username",
                "Username",
                TypeInfo(str),
            ),
        ]

    # The unique ID that Amazon MQ generates for the broker.
    broker_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The username of the ActiveMQ user. This value can contain only alphanumeric
    # characters, dashes, periods, underscores, and tildes (- . _ ~). This value
    # must be 2-100 characters long.
    username: str = dataclasses.field(default=ShapeBase.NOT_SET, )


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
                "broker_id",
                "BrokerId",
                TypeInfo(str),
            ),
            (
                "console_access",
                "ConsoleAccess",
                TypeInfo(bool),
            ),
            (
                "groups",
                "Groups",
                TypeInfo(typing.List[str]),
            ),
            (
                "pending",
                "Pending",
                TypeInfo(UserPendingChanges),
            ),
            (
                "username",
                "Username",
                TypeInfo(str),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Required. The unique ID that Amazon MQ generates for the broker.
    broker_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Enables access to the the ActiveMQ Web Console for the ActiveMQ user.
    console_access: bool = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The list of groups (20 maximum) to which the ActiveMQ user belongs. This
    # value can contain only alphanumeric characters, dashes, periods,
    # underscores, and tildes (- . _ ~). This value must be 2-100 characters
    # long.
    groups: typing.List[str] = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The status of the changes pending for the ActiveMQ user.
    pending: "UserPendingChanges" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Required. The username of the ActiveMQ user. This value can contain only
    # alphanumeric characters, dashes, periods, underscores, and tildes (- . _
    # ~). This value must be 2-100 characters long.
    username: str = dataclasses.field(default=ShapeBase.NOT_SET, )


class EngineType(str):
    """
    The type of broker engine. Note: Currently, Amazon MQ supports only ActiveMQ.
    """
    ACTIVEMQ = "ACTIVEMQ"


@dataclasses.dataclass
class Error(ShapeBase):
    """
    Returns information about an error.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "error_attribute",
                "ErrorAttribute",
                TypeInfo(str),
            ),
            (
                "message",
                "Message",
                TypeInfo(str),
            ),
        ]

    # The attribute which caused the error.
    error_attribute: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The explanation of the error.
    message: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ForbiddenException(ShapeBase):
    """
    Returns information about an error.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "error_attribute",
                "ErrorAttribute",
                TypeInfo(str),
            ),
            (
                "message",
                "Message",
                TypeInfo(str),
            ),
        ]

    # The attribute which caused the error.
    error_attribute: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The explanation of the error.
    message: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class InternalServerErrorException(ShapeBase):
    """
    Returns information about an error.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "error_attribute",
                "ErrorAttribute",
                TypeInfo(str),
            ),
            (
                "message",
                "Message",
                TypeInfo(str),
            ),
        ]

    # The attribute which caused the error.
    error_attribute: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The explanation of the error.
    message: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ListBrokersOutput(ShapeBase):
    """
    A list of information about all brokers.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "broker_summaries",
                "BrokerSummaries",
                TypeInfo(typing.List[BrokerSummary]),
            ),
            (
                "next_token",
                "NextToken",
                TypeInfo(str),
            ),
        ]

    # A list of information about all brokers.
    broker_summaries: typing.List["BrokerSummary"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The token that specifies the next page of results Amazon MQ should return.
    # To request the first page, leave nextToken empty.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ListBrokersRequest(ShapeBase):
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

    # The maximum number of brokers that Amazon MQ can return per page (20 by
    # default). This value must be an integer from 5 to 100.
    max_results: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The token that specifies the next page of results Amazon MQ should return.
    # To request the first page, leave nextToken empty.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ListBrokersResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "broker_summaries",
                "BrokerSummaries",
                TypeInfo(typing.List[BrokerSummary]),
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

    # A list of information about all brokers.
    broker_summaries: typing.List["BrokerSummary"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The token that specifies the next page of results Amazon MQ should return.
    # To request the first page, leave nextToken empty.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ListConfigurationRevisionsOutput(ShapeBase):
    """
    Returns a list of all revisions for the specified configuration.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "configuration_id",
                "ConfigurationId",
                TypeInfo(str),
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
            (
                "revisions",
                "Revisions",
                TypeInfo(typing.List[ConfigurationRevision]),
            ),
        ]

    # The unique ID that Amazon MQ generates for the configuration.
    configuration_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The maximum number of configuration revisions that can be returned per page
    # (20 by default). This value must be an integer from 5 to 100.
    max_results: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The token that specifies the next page of results Amazon MQ should return.
    # To request the first page, leave nextToken empty.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The list of all revisions for the specified configuration.
    revisions: typing.List["ConfigurationRevision"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class ListConfigurationRevisionsRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "configuration_id",
                "ConfigurationId",
                TypeInfo(str),
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

    # The unique ID that Amazon MQ generates for the configuration.
    configuration_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The maximum number of configurations that Amazon MQ can return per page (20
    # by default). This value must be an integer from 5 to 100.
    max_results: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The token that specifies the next page of results Amazon MQ should return.
    # To request the first page, leave nextToken empty.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ListConfigurationRevisionsResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "configuration_id",
                "ConfigurationId",
                TypeInfo(str),
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
            (
                "revisions",
                "Revisions",
                TypeInfo(typing.List[ConfigurationRevision]),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The unique ID that Amazon MQ generates for the configuration.
    configuration_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The maximum number of configuration revisions that can be returned per page
    # (20 by default). This value must be an integer from 5 to 100.
    max_results: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The token that specifies the next page of results Amazon MQ should return.
    # To request the first page, leave nextToken empty.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The list of all revisions for the specified configuration.
    revisions: typing.List["ConfigurationRevision"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class ListConfigurationsOutput(ShapeBase):
    """
    Returns a list of all configurations.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "configurations",
                "Configurations",
                TypeInfo(typing.List[Configuration]),
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

    # The list of all revisions for the specified configuration.
    configurations: typing.List["Configuration"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The maximum number of configurations that Amazon MQ can return per page (20
    # by default). This value must be an integer from 5 to 100.
    max_results: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The token that specifies the next page of results Amazon MQ should return.
    # To request the first page, leave nextToken empty.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ListConfigurationsRequest(ShapeBase):
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

    # The maximum number of configurations that Amazon MQ can return per page (20
    # by default). This value must be an integer from 5 to 100.
    max_results: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The token that specifies the next page of results Amazon MQ should return.
    # To request the first page, leave nextToken empty.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ListConfigurationsResponse(OutputShapeBase):
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
                TypeInfo(typing.List[Configuration]),
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

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The list of all revisions for the specified configuration.
    configurations: typing.List["Configuration"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The maximum number of configurations that Amazon MQ can return per page (20
    # by default). This value must be an integer from 5 to 100.
    max_results: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The token that specifies the next page of results Amazon MQ should return.
    # To request the first page, leave nextToken empty.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ListUsersOutput(ShapeBase):
    """
    Returns a list of all ActiveMQ users.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "broker_id",
                "BrokerId",
                TypeInfo(str),
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
            (
                "users",
                "Users",
                TypeInfo(typing.List[UserSummary]),
            ),
        ]

    # Required. The unique ID that Amazon MQ generates for the broker.
    broker_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Required. The maximum number of ActiveMQ users that can be returned per
    # page (20 by default). This value must be an integer from 5 to 100.
    max_results: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The token that specifies the next page of results Amazon MQ should return.
    # To request the first page, leave nextToken empty.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Required. The list of all ActiveMQ usernames for the specified broker.
    users: typing.List["UserSummary"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class ListUsersRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "broker_id",
                "BrokerId",
                TypeInfo(str),
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

    # The unique ID that Amazon MQ generates for the broker.
    broker_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The maximum number of ActiveMQ users that can be returned per page (20 by
    # default). This value must be an integer from 5 to 100.
    max_results: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The token that specifies the next page of results Amazon MQ should return.
    # To request the first page, leave nextToken empty.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )


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
                "broker_id",
                "BrokerId",
                TypeInfo(str),
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
            (
                "users",
                "Users",
                TypeInfo(typing.List[UserSummary]),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Required. The unique ID that Amazon MQ generates for the broker.
    broker_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Required. The maximum number of ActiveMQ users that can be returned per
    # page (20 by default). This value must be an integer from 5 to 100.
    max_results: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The token that specifies the next page of results Amazon MQ should return.
    # To request the first page, leave nextToken empty.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Required. The list of all ActiveMQ usernames for the specified broker.
    users: typing.List["UserSummary"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class Logs(ShapeBase):
    """
    The list of information about logs to be enabled for the specified broker.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "audit",
                "Audit",
                TypeInfo(bool),
            ),
            (
                "general",
                "General",
                TypeInfo(bool),
            ),
        ]

    # Enables audit logging. Every user management action made using JMX or the
    # ActiveMQ Web Console is logged.
    audit: bool = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Enables general logging.
    general: bool = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class LogsSummary(ShapeBase):
    """
    The list of information about logs currently enabled and pending to be deployed
    for the specified broker.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "audit",
                "Audit",
                TypeInfo(bool),
            ),
            (
                "audit_log_group",
                "AuditLogGroup",
                TypeInfo(str),
            ),
            (
                "general",
                "General",
                TypeInfo(bool),
            ),
            (
                "general_log_group",
                "GeneralLogGroup",
                TypeInfo(str),
            ),
            (
                "pending",
                "Pending",
                TypeInfo(PendingLogs),
            ),
        ]

    # Enables audit logging. Every user management action made using JMX or the
    # ActiveMQ Web Console is logged.
    audit: bool = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Location of CloudWatch Log group where audit logs will be sent.
    audit_log_group: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Enables general logging.
    general: bool = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Location of CloudWatch Log group where general logs will be sent.
    general_log_group: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The list of information about logs pending to be deployed for the specified
    # broker.
    pending: "PendingLogs" = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class NotFoundException(ShapeBase):
    """
    Returns information about an error.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "error_attribute",
                "ErrorAttribute",
                TypeInfo(str),
            ),
            (
                "message",
                "Message",
                TypeInfo(str),
            ),
        ]

    # The attribute which caused the error.
    error_attribute: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The explanation of the error.
    message: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class PendingLogs(ShapeBase):
    """
    The list of information about logs to be enabled for the specified broker.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "audit",
                "Audit",
                TypeInfo(bool),
            ),
            (
                "general",
                "General",
                TypeInfo(bool),
            ),
        ]

    # Enables audit logging. Every user management action made using JMX or the
    # ActiveMQ Web Console is logged.
    audit: bool = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Enables general logging.
    general: bool = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class RebootBrokerRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "broker_id",
                "BrokerId",
                TypeInfo(str),
            ),
        ]

    # The unique ID that Amazon MQ generates for the broker.
    broker_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class RebootBrokerResponse(OutputShapeBase):
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
class SanitizationWarning(ShapeBase):
    """
    Returns information about the XML element or attribute that was sanitized in the
    configuration.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "attribute_name",
                "AttributeName",
                TypeInfo(str),
            ),
            (
                "element_name",
                "ElementName",
                TypeInfo(str),
            ),
            (
                "reason",
                "Reason",
                TypeInfo(typing.Union[str, SanitizationWarningReason]),
            ),
        ]

    # The name of the XML attribute that has been sanitized.
    attribute_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The name of the XML element that has been sanitized.
    element_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Required. The reason for which the XML elements or attributes were
    # sanitized.
    reason: typing.Union[str, "SanitizationWarningReason"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


class SanitizationWarningReason(str):
    """
    The reason for which the XML elements or attributes were sanitized.
    """
    DISALLOWED_ELEMENT_REMOVED = "DISALLOWED_ELEMENT_REMOVED"
    DISALLOWED_ATTRIBUTE_REMOVED = "DISALLOWED_ATTRIBUTE_REMOVED"
    INVALID_ATTRIBUTE_VALUE_REMOVED = "INVALID_ATTRIBUTE_VALUE_REMOVED"


@dataclasses.dataclass
class UnauthorizedException(ShapeBase):
    """
    Returns information about an error.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "error_attribute",
                "ErrorAttribute",
                TypeInfo(str),
            ),
            (
                "message",
                "Message",
                TypeInfo(str),
            ),
        ]

    # The attribute which caused the error.
    error_attribute: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The explanation of the error.
    message: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class UpdateBrokerInput(ShapeBase):
    """
    Updates the broker using the specified properties.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "configuration",
                "Configuration",
                TypeInfo(ConfigurationId),
            ),
            (
                "logs",
                "Logs",
                TypeInfo(Logs),
            ),
        ]

    # A list of information about the configuration.
    configuration: "ConfigurationId" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Enables Amazon CloudWatch logging for brokers.
    logs: "Logs" = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class UpdateBrokerOutput(ShapeBase):
    """
    Returns information about the updated broker.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "broker_id",
                "BrokerId",
                TypeInfo(str),
            ),
            (
                "configuration",
                "Configuration",
                TypeInfo(ConfigurationId),
            ),
            (
                "logs",
                "Logs",
                TypeInfo(Logs),
            ),
        ]

    # Required. The unique ID that Amazon MQ generates for the broker.
    broker_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The ID of the updated configuration.
    configuration: "ConfigurationId" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The list of information about logs to be enabled for the specified broker.
    logs: "Logs" = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class UpdateBrokerRequest(ShapeBase):
    """
    Updates the broker using the specified properties.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "broker_id",
                "BrokerId",
                TypeInfo(str),
            ),
            (
                "configuration",
                "Configuration",
                TypeInfo(ConfigurationId),
            ),
            (
                "logs",
                "Logs",
                TypeInfo(Logs),
            ),
        ]

    # The name of the broker. This value must be unique in your AWS account, 1-50
    # characters long, must contain only letters, numbers, dashes, and
    # underscores, and must not contain whitespaces, brackets, wildcard
    # characters, or special characters.
    broker_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A list of information about the configuration.
    configuration: "ConfigurationId" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Enables Amazon CloudWatch logging for brokers.
    logs: "Logs" = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class UpdateBrokerResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "broker_id",
                "BrokerId",
                TypeInfo(str),
            ),
            (
                "configuration",
                "Configuration",
                TypeInfo(ConfigurationId),
            ),
            (
                "logs",
                "Logs",
                TypeInfo(Logs),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Required. The unique ID that Amazon MQ generates for the broker.
    broker_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The ID of the updated configuration.
    configuration: "ConfigurationId" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The list of information about logs to be enabled for the specified broker.
    logs: "Logs" = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class UpdateConfigurationInput(ShapeBase):
    """
    Updates the specified configuration.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "data",
                "Data",
                TypeInfo(str),
            ),
            (
                "description",
                "Description",
                TypeInfo(str),
            ),
        ]

    # Required. The base64-encoded XML configuration.
    data: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The description of the configuration.
    description: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class UpdateConfigurationOutput(ShapeBase):
    """
    Returns information about the updated configuration.
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
                "created",
                "Created",
                TypeInfo(datetime.datetime),
            ),
            (
                "id",
                "Id",
                TypeInfo(str),
            ),
            (
                "latest_revision",
                "LatestRevision",
                TypeInfo(ConfigurationRevision),
            ),
            (
                "name",
                "Name",
                TypeInfo(str),
            ),
            (
                "warnings",
                "Warnings",
                TypeInfo(typing.List[SanitizationWarning]),
            ),
        ]

    # Required. The Amazon Resource Name (ARN) of the configuration.
    arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Required. The date and time of the configuration.
    created: datetime.datetime = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Required. The unique ID that Amazon MQ generates for the configuration.
    id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The latest revision of the configuration.
    latest_revision: "ConfigurationRevision" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Required. The name of the configuration. This value can contain only
    # alphanumeric characters, dashes, periods, underscores, and tildes (- . _
    # ~). This value must be 1-150 characters long.
    name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The list of the first 20 warnings about the configuration XML elements or
    # attributes that were sanitized.
    warnings: typing.List["SanitizationWarning"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class UpdateConfigurationRequest(ShapeBase):
    """
    Updates the specified configuration.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "configuration_id",
                "ConfigurationId",
                TypeInfo(str),
            ),
            (
                "data",
                "Data",
                TypeInfo(str),
            ),
            (
                "description",
                "Description",
                TypeInfo(str),
            ),
        ]

    # The unique ID that Amazon MQ generates for the configuration.
    configuration_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Required. The base64-encoded XML configuration.
    data: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The description of the configuration.
    description: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class UpdateConfigurationResponse(OutputShapeBase):
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
                "created",
                "Created",
                TypeInfo(datetime.datetime),
            ),
            (
                "id",
                "Id",
                TypeInfo(str),
            ),
            (
                "latest_revision",
                "LatestRevision",
                TypeInfo(ConfigurationRevision),
            ),
            (
                "name",
                "Name",
                TypeInfo(str),
            ),
            (
                "warnings",
                "Warnings",
                TypeInfo(typing.List[SanitizationWarning]),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Required. The Amazon Resource Name (ARN) of the configuration.
    arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Required. The date and time of the configuration.
    created: datetime.datetime = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Required. The unique ID that Amazon MQ generates for the configuration.
    id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The latest revision of the configuration.
    latest_revision: "ConfigurationRevision" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Required. The name of the configuration. This value can contain only
    # alphanumeric characters, dashes, periods, underscores, and tildes (- . _
    # ~). This value must be 1-150 characters long.
    name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The list of the first 20 warnings about the configuration XML elements or
    # attributes that were sanitized.
    warnings: typing.List["SanitizationWarning"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class UpdateUserInput(ShapeBase):
    """
    Updates the information for an ActiveMQ user.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "console_access",
                "ConsoleAccess",
                TypeInfo(bool),
            ),
            (
                "groups",
                "Groups",
                TypeInfo(typing.List[str]),
            ),
            (
                "password",
                "Password",
                TypeInfo(str),
            ),
        ]

    # Enables access to the the ActiveMQ Web Console for the ActiveMQ user.
    console_access: bool = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The list of groups (20 maximum) to which the ActiveMQ user belongs. This
    # value can contain only alphanumeric characters, dashes, periods,
    # underscores, and tildes (- . _ ~). This value must be 2-100 characters
    # long.
    groups: typing.List[str] = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The password of the user. This value must be at least 12 characters long,
    # must contain at least 4 unique characters, and must not contain commas.
    password: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class UpdateUserRequest(ShapeBase):
    """
    Updates the information for an ActiveMQ user.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "broker_id",
                "BrokerId",
                TypeInfo(str),
            ),
            (
                "username",
                "Username",
                TypeInfo(str),
            ),
            (
                "console_access",
                "ConsoleAccess",
                TypeInfo(bool),
            ),
            (
                "groups",
                "Groups",
                TypeInfo(typing.List[str]),
            ),
            (
                "password",
                "Password",
                TypeInfo(str),
            ),
        ]

    # The unique ID that Amazon MQ generates for the broker.
    broker_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Required. The username of the ActiveMQ user. This value can contain only
    # alphanumeric characters, dashes, periods, underscores, and tildes (- . _
    # ~). This value must be 2-100 characters long.
    username: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Enables access to the the ActiveMQ Web Console for the ActiveMQ user.
    console_access: bool = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The list of groups (20 maximum) to which the ActiveMQ user belongs. This
    # value can contain only alphanumeric characters, dashes, periods,
    # underscores, and tildes (- . _ ~). This value must be 2-100 characters
    # long.
    groups: typing.List[str] = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The password of the user. This value must be at least 12 characters long,
    # must contain at least 4 unique characters, and must not contain commas.
    password: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class UpdateUserResponse(OutputShapeBase):
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
    An ActiveMQ user associated with the broker.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "console_access",
                "ConsoleAccess",
                TypeInfo(bool),
            ),
            (
                "groups",
                "Groups",
                TypeInfo(typing.List[str]),
            ),
            (
                "password",
                "Password",
                TypeInfo(str),
            ),
            (
                "username",
                "Username",
                TypeInfo(str),
            ),
        ]

    # Enables access to the the ActiveMQ Web Console for the ActiveMQ user.
    console_access: bool = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The list of groups (20 maximum) to which the ActiveMQ user belongs. This
    # value can contain only alphanumeric characters, dashes, periods,
    # underscores, and tildes (- . _ ~). This value must be 2-100 characters
    # long.
    groups: typing.List[str] = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Required. The password of the ActiveMQ user. This value must be at least 12
    # characters long, must contain at least 4 unique characters, and must not
    # contain commas.
    password: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Required. The username of the ActiveMQ user. This value can contain only
    # alphanumeric characters, dashes, periods, underscores, and tildes (- . _
    # ~). This value must be 2-100 characters long.
    username: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class UserPendingChanges(ShapeBase):
    """
    Returns information about the status of the changes pending for the ActiveMQ
    user.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "console_access",
                "ConsoleAccess",
                TypeInfo(bool),
            ),
            (
                "groups",
                "Groups",
                TypeInfo(typing.List[str]),
            ),
            (
                "pending_change",
                "PendingChange",
                TypeInfo(typing.Union[str, ChangeType]),
            ),
        ]

    # Enables access to the the ActiveMQ Web Console for the ActiveMQ user.
    console_access: bool = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The list of groups (20 maximum) to which the ActiveMQ user belongs. This
    # value can contain only alphanumeric characters, dashes, periods,
    # underscores, and tildes (- . _ ~). This value must be 2-100 characters
    # long.
    groups: typing.List[str] = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Required. The type of change pending for the ActiveMQ user.
    pending_change: typing.Union[str, "ChangeType"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class UserSummary(ShapeBase):
    """
    Returns a list of all ActiveMQ users.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "pending_change",
                "PendingChange",
                TypeInfo(typing.Union[str, ChangeType]),
            ),
            (
                "username",
                "Username",
                TypeInfo(str),
            ),
        ]

    # The type of change pending for the ActiveMQ user.
    pending_change: typing.Union[str, "ChangeType"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Required. The username of the ActiveMQ user. This value can contain only
    # alphanumeric characters, dashes, periods, underscores, and tildes (- . _
    # ~). This value must be 2-100 characters long.
    username: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class WeeklyStartTime(ShapeBase):
    """
    The scheduled time period relative to UTC during which Amazon MQ begins to apply
    pending updates or patches to the broker.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "day_of_week",
                "DayOfWeek",
                TypeInfo(typing.Union[str, DayOfWeek]),
            ),
            (
                "time_of_day",
                "TimeOfDay",
                TypeInfo(str),
            ),
            (
                "time_zone",
                "TimeZone",
                TypeInfo(str),
            ),
        ]

    # Required. The day of the week.
    day_of_week: typing.Union[str, "DayOfWeek"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Required. The time, in 24-hour format.
    time_of_day: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The time zone, UTC by default, in either the Country/City format, or the
    # UTC offset format.
    time_zone: str = dataclasses.field(default=ShapeBase.NOT_SET, )
