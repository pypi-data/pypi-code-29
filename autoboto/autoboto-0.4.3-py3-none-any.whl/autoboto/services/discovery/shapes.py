import datetime
import typing
from autoboto import ShapeBase, OutputShapeBase, TypeInfo
import dataclasses


@dataclasses.dataclass
class AgentConfigurationStatus(ShapeBase):
    """
    Information about agents or connectors that were instructed to start collecting
    data. Information includes the agent/connector ID, a description of the
    operation, and whether the agent/connector configuration was updated.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "agent_id",
                "agentId",
                TypeInfo(str),
            ),
            (
                "operation_succeeded",
                "operationSucceeded",
                TypeInfo(bool),
            ),
            (
                "description",
                "description",
                TypeInfo(str),
            ),
        ]

    # The agent/connector ID.
    agent_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Information about the status of the `StartDataCollection` and
    # `StopDataCollection` operations. The system has recorded the data
    # collection operation. The agent/connector receives this command the next
    # time it polls for a new command.
    operation_succeeded: bool = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A description of the operation performed.
    description: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class AgentInfo(ShapeBase):
    """
    Information about agents or connectors associated with the user’s AWS account.
    Information includes agent or connector IDs, IP addresses, media access control
    (MAC) addresses, agent or connector health, hostname where the agent or
    connector resides, and agent version for each agent.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "agent_id",
                "agentId",
                TypeInfo(str),
            ),
            (
                "host_name",
                "hostName",
                TypeInfo(str),
            ),
            (
                "agent_network_info_list",
                "agentNetworkInfoList",
                TypeInfo(typing.List[AgentNetworkInfo]),
            ),
            (
                "connector_id",
                "connectorId",
                TypeInfo(str),
            ),
            (
                "version",
                "version",
                TypeInfo(str),
            ),
            (
                "health",
                "health",
                TypeInfo(typing.Union[str, AgentStatus]),
            ),
            (
                "last_health_ping_time",
                "lastHealthPingTime",
                TypeInfo(str),
            ),
            (
                "collection_status",
                "collectionStatus",
                TypeInfo(str),
            ),
            (
                "agent_type",
                "agentType",
                TypeInfo(str),
            ),
            (
                "registered_time",
                "registeredTime",
                TypeInfo(str),
            ),
        ]

    # The agent or connector ID.
    agent_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The name of the host where the agent or connector resides. The host can be
    # a server or virtual machine.
    host_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Network details about the host where the agent or connector resides.
    agent_network_info_list: typing.List["AgentNetworkInfo"
                                        ] = dataclasses.field(
                                            default=ShapeBase.NOT_SET,
                                        )

    # The ID of the connector.
    connector_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The agent or connector version.
    version: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The health of the agent or connector.
    health: typing.Union[str, "AgentStatus"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Time since agent or connector health was reported.
    last_health_ping_time: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Status of the collection process for an agent or connector.
    collection_status: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Type of agent.
    agent_type: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Agent's first registration timestamp in UTC.
    registered_time: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class AgentNetworkInfo(ShapeBase):
    """
    Network details about the host where the agent/connector resides.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "ip_address",
                "ipAddress",
                TypeInfo(str),
            ),
            (
                "mac_address",
                "macAddress",
                TypeInfo(str),
            ),
        ]

    # The IP address for the host where the agent/connector resides.
    ip_address: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The MAC address for the host where the agent/connector resides.
    mac_address: str = dataclasses.field(default=ShapeBase.NOT_SET, )


class AgentStatus(str):
    HEALTHY = "HEALTHY"
    UNHEALTHY = "UNHEALTHY"
    RUNNING = "RUNNING"
    UNKNOWN = "UNKNOWN"
    BLACKLISTED = "BLACKLISTED"
    SHUTDOWN = "SHUTDOWN"


@dataclasses.dataclass
class AssociateConfigurationItemsToApplicationRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "application_configuration_id",
                "applicationConfigurationId",
                TypeInfo(str),
            ),
            (
                "configuration_ids",
                "configurationIds",
                TypeInfo(typing.List[str]),
            ),
        ]

    # The configuration ID of an application with which items are to be
    # associated.
    application_configuration_id: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The ID of each configuration item to be associated with an application.
    configuration_ids: typing.List[str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class AssociateConfigurationItemsToApplicationResponse(OutputShapeBase):
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
class AuthorizationErrorException(ShapeBase):
    """
    The AWS user account does not have permission to perform the action. Check the
    IAM policy associated with this account.
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


class ConfigurationItemType(str):
    SERVER = "SERVER"
    PROCESS = "PROCESS"
    CONNECTION = "CONNECTION"
    APPLICATION = "APPLICATION"


@dataclasses.dataclass
class ConfigurationTag(ShapeBase):
    """
    Tags for a configuration item. Tags are metadata that help you categorize IT
    assets.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "configuration_type",
                "configurationType",
                TypeInfo(typing.Union[str, ConfigurationItemType]),
            ),
            (
                "configuration_id",
                "configurationId",
                TypeInfo(str),
            ),
            (
                "key",
                "key",
                TypeInfo(str),
            ),
            (
                "value",
                "value",
                TypeInfo(str),
            ),
            (
                "time_of_creation",
                "timeOfCreation",
                TypeInfo(datetime.datetime),
            ),
        ]

    # A type of IT asset to tag.
    configuration_type: typing.Union[str, "ConfigurationItemType"
                                    ] = dataclasses.field(
                                        default=ShapeBase.NOT_SET,
                                    )

    # The configuration ID for the item to tag. You can specify a list of keys
    # and values.
    configuration_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A type of tag on which to filter. For example, _serverType_.
    key: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A value on which to filter. For example _key = serverType_ and _value = web
    # server_.
    value: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The time the configuration tag was created in Coordinated Universal Time
    # (UTC).
    time_of_creation: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class ConflictErrorException(ShapeBase):
    """

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
class ContinuousExportDescription(ShapeBase):
    """
    A list of continuous export descriptions.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "export_id",
                "exportId",
                TypeInfo(str),
            ),
            (
                "status",
                "status",
                TypeInfo(typing.Union[str, ContinuousExportStatus]),
            ),
            (
                "status_detail",
                "statusDetail",
                TypeInfo(str),
            ),
            (
                "s3_bucket",
                "s3Bucket",
                TypeInfo(str),
            ),
            (
                "start_time",
                "startTime",
                TypeInfo(datetime.datetime),
            ),
            (
                "stop_time",
                "stopTime",
                TypeInfo(datetime.datetime),
            ),
            (
                "data_source",
                "dataSource",
                TypeInfo(typing.Union[str, DataSource]),
            ),
            (
                "schema_storage_config",
                "schemaStorageConfig",
                TypeInfo(typing.Dict[str, str]),
            ),
        ]

    # The unique ID assigned to this export.
    export_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Describes the status of the export. Can be one of the following values:

    #   * START_IN_PROGRESS - setting up resources to start continuous export.

    #   * START_FAILED - an error occurred setting up continuous export. To recover, call start-continuous-export again.

    #   * ACTIVE - data is being exported to the customer bucket.

    #   * ERROR - an error occurred during export. To fix the issue, call stop-continuous-export and start-continuous-export.

    #   * STOP_IN_PROGRESS - stopping the export.

    #   * STOP_FAILED - an error occurred stopping the export. To recover, call stop-continuous-export again.

    #   * INACTIVE - the continuous export has been stopped. Data is no longer being exported to the customer bucket.
    status: typing.Union[str, "ContinuousExportStatus"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Contains information about any errors that may have occurred.
    status_detail: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The name of the s3 bucket where the export data parquet files are stored.
    s3_bucket: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The timestamp representing when the continuous export was started.
    start_time: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The timestamp that represents when this continuous export was stopped.
    stop_time: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The type of data collector used to gather this data (currently only offered
    # for AGENT).
    data_source: typing.Union[str, "DataSource"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # An object which describes how the data is stored.

    #   * `databaseName` \- the name of the Glue database used to store the schema.
    schema_storage_config: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


class ContinuousExportStatus(str):
    START_IN_PROGRESS = "START_IN_PROGRESS"
    START_FAILED = "START_FAILED"
    ACTIVE = "ACTIVE"
    ERROR = "ERROR"
    STOP_IN_PROGRESS = "STOP_IN_PROGRESS"
    STOP_FAILED = "STOP_FAILED"
    INACTIVE = "INACTIVE"


@dataclasses.dataclass
class CreateApplicationRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
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

    # Name of the application to be created.
    name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Description of the application to be created.
    description: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class CreateApplicationResponse(OutputShapeBase):
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
                "configurationId",
                TypeInfo(str),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Configuration ID of an application to be created.
    configuration_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class CreateTagsRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "configuration_ids",
                "configurationIds",
                TypeInfo(typing.List[str]),
            ),
            (
                "tags",
                "tags",
                TypeInfo(typing.List[Tag]),
            ),
        ]

    # A list of configuration items that you want to tag.
    configuration_ids: typing.List[str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Tags that you want to associate with one or more configuration items.
    # Specify the tags that you want to create in a _key_ - _value_ format. For
    # example:

    # `{"key": "serverType", "value": "webServer"}`
    tags: typing.List["Tag"] = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class CreateTagsResponse(OutputShapeBase):
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
class CustomerAgentInfo(ShapeBase):
    """
    Inventory data for installed discovery agents.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "active_agents",
                "activeAgents",
                TypeInfo(int),
            ),
            (
                "healthy_agents",
                "healthyAgents",
                TypeInfo(int),
            ),
            (
                "black_listed_agents",
                "blackListedAgents",
                TypeInfo(int),
            ),
            (
                "shutdown_agents",
                "shutdownAgents",
                TypeInfo(int),
            ),
            (
                "unhealthy_agents",
                "unhealthyAgents",
                TypeInfo(int),
            ),
            (
                "total_agents",
                "totalAgents",
                TypeInfo(int),
            ),
            (
                "unknown_agents",
                "unknownAgents",
                TypeInfo(int),
            ),
        ]

    # Number of active discovery agents.
    active_agents: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Number of healthy discovery agents
    healthy_agents: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Number of blacklisted discovery agents.
    black_listed_agents: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Number of discovery agents with status SHUTDOWN.
    shutdown_agents: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Number of unhealthy discovery agents.
    unhealthy_agents: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Total number of discovery agents.
    total_agents: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Number of unknown discovery agents.
    unknown_agents: int = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class CustomerConnectorInfo(ShapeBase):
    """
    Inventory data for installed discovery connectors.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "active_connectors",
                "activeConnectors",
                TypeInfo(int),
            ),
            (
                "healthy_connectors",
                "healthyConnectors",
                TypeInfo(int),
            ),
            (
                "black_listed_connectors",
                "blackListedConnectors",
                TypeInfo(int),
            ),
            (
                "shutdown_connectors",
                "shutdownConnectors",
                TypeInfo(int),
            ),
            (
                "unhealthy_connectors",
                "unhealthyConnectors",
                TypeInfo(int),
            ),
            (
                "total_connectors",
                "totalConnectors",
                TypeInfo(int),
            ),
            (
                "unknown_connectors",
                "unknownConnectors",
                TypeInfo(int),
            ),
        ]

    # Number of active discovery connectors.
    active_connectors: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Number of healthy discovery connectors.
    healthy_connectors: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Number of blacklisted discovery connectors.
    black_listed_connectors: int = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Number of discovery connectors with status SHUTDOWN,
    shutdown_connectors: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Number of unhealthy discovery connectors.
    unhealthy_connectors: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Total number of discovery connectors.
    total_connectors: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Number of unknown discovery connectors.
    unknown_connectors: int = dataclasses.field(default=ShapeBase.NOT_SET, )


class DataSource(str):
    AGENT = "AGENT"


@dataclasses.dataclass
class DeleteApplicationsRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "configuration_ids",
                "configurationIds",
                TypeInfo(typing.List[str]),
            ),
        ]

    # Configuration ID of an application to be deleted.
    configuration_ids: typing.List[str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class DeleteApplicationsResponse(OutputShapeBase):
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
                "configuration_ids",
                "configurationIds",
                TypeInfo(typing.List[str]),
            ),
            (
                "tags",
                "tags",
                TypeInfo(typing.List[Tag]),
            ),
        ]

    # A list of configuration items with tags that you want to delete.
    configuration_ids: typing.List[str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Tags that you want to delete from one or more configuration items. Specify
    # the tags that you want to delete in a _key_ - _value_ format. For example:

    # `{"key": "serverType", "value": "webServer"}`
    tags: typing.List["Tag"] = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DeleteTagsResponse(OutputShapeBase):
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
class DescribeAgentsRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "agent_ids",
                "agentIds",
                TypeInfo(typing.List[str]),
            ),
            (
                "filters",
                "filters",
                TypeInfo(typing.List[Filter]),
            ),
            (
                "max_results",
                "maxResults",
                TypeInfo(int),
            ),
            (
                "next_token",
                "nextToken",
                TypeInfo(str),
            ),
        ]

    # The agent or the Connector IDs for which you want information. If you
    # specify no IDs, the system returns information about all agents/Connectors
    # associated with your AWS user account.
    agent_ids: typing.List[str] = dataclasses.field(default=ShapeBase.NOT_SET, )

    # You can filter the request using various logical operators and a _key_ -
    # _value_ format. For example:

    # `{"key": "collectionStatus", "value": "STARTED"}`
    filters: typing.List["Filter"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The total number of agents/Connectors to return in a single page of output.
    # The maximum value is 100.
    max_results: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Token to retrieve the next set of results. For example, if you previously
    # specified 100 IDs for `DescribeAgentsRequest$agentIds` but set
    # `DescribeAgentsRequest$maxResults` to 10, you received a set of 10 results
    # along with a token. Use that token in this query to get the next set of 10.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DescribeAgentsResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "agents_info",
                "agentsInfo",
                TypeInfo(typing.List[AgentInfo]),
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

    # Lists agents or the Connector by ID or lists all agents/Connectors
    # associated with your user account if you did not specify an agent/Connector
    # ID. The output includes agent/Connector IDs, IP addresses, media access
    # control (MAC) addresses, agent/Connector health, host name where the
    # agent/Connector resides, and the version number of each agent/Connector.
    agents_info: typing.List["AgentInfo"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Token to retrieve the next set of results. For example, if you specified
    # 100 IDs for `DescribeAgentsRequest$agentIds` but set
    # `DescribeAgentsRequest$maxResults` to 10, you received a set of 10 results
    # along with this token. Use this token in the next query to retrieve the
    # next set of 10.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DescribeConfigurationsRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "configuration_ids",
                "configurationIds",
                TypeInfo(typing.List[str]),
            ),
        ]

    # One or more configuration IDs.
    configuration_ids: typing.List[str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class DescribeConfigurationsResponse(OutputShapeBase):
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
                "configurations",
                TypeInfo(typing.List[typing.Dict[str, str]]),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A key in the response map. The value is an array of data.
    configurations: typing.List[typing.Dict[str, str]] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class DescribeContinuousExportsRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "export_ids",
                "exportIds",
                TypeInfo(typing.List[str]),
            ),
            (
                "max_results",
                "maxResults",
                TypeInfo(int),
            ),
            (
                "next_token",
                "nextToken",
                TypeInfo(str),
            ),
        ]

    # The unique IDs assigned to the exports.
    export_ids: typing.List[str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A number between 1 and 100 specifying the maximum number of continuous
    # export descriptions returned.
    max_results: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The token from the previous call to `DescribeExportTasks`.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DescribeContinuousExportsResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "descriptions",
                "descriptions",
                TypeInfo(typing.List[ContinuousExportDescription]),
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

    # A list of continuous export descriptions.
    descriptions: typing.List["ContinuousExportDescription"
                             ] = dataclasses.field(
                                 default=ShapeBase.NOT_SET,
                             )

    # The token from the previous call to `DescribeExportTasks`.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DescribeExportConfigurationsRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "export_ids",
                "exportIds",
                TypeInfo(typing.List[str]),
            ),
            (
                "max_results",
                "maxResults",
                TypeInfo(int),
            ),
            (
                "next_token",
                "nextToken",
                TypeInfo(str),
            ),
        ]

    # A list of continuous export ids to search for.
    export_ids: typing.List[str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A number between 1 and 100 specifying the maximum number of continuous
    # export descriptions returned.
    max_results: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The token from the previous call to describe-export-tasks.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DescribeExportConfigurationsResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "exports_info",
                "exportsInfo",
                TypeInfo(typing.List[ExportInfo]),
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

    exports_info: typing.List["ExportInfo"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The token from the previous call to describe-export-tasks.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DescribeExportTasksRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "export_ids",
                "exportIds",
                TypeInfo(typing.List[str]),
            ),
            (
                "filters",
                "filters",
                TypeInfo(typing.List[ExportFilter]),
            ),
            (
                "max_results",
                "maxResults",
                TypeInfo(int),
            ),
            (
                "next_token",
                "nextToken",
                TypeInfo(str),
            ),
        ]

    # One or more unique identifiers used to query the status of an export
    # request.
    export_ids: typing.List[str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # One or more filters.

    #   * `AgentId` \- ID of the agent whose collected data will be exported
    filters: typing.List["ExportFilter"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The maximum number of volume results returned by `DescribeExportTasks` in
    # paginated output. When this parameter is used, `DescribeExportTasks` only
    # returns `maxResults` results in a single page along with a `nextToken`
    # response element.
    max_results: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The `nextToken` value returned from a previous paginated
    # `DescribeExportTasks` request where `maxResults` was used and the results
    # exceeded the value of that parameter. Pagination continues from the end of
    # the previous results that returned the `nextToken` value. This value is
    # null when there are no more results to return.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DescribeExportTasksResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "exports_info",
                "exportsInfo",
                TypeInfo(typing.List[ExportInfo]),
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

    # Contains one or more sets of export request details. When the status of a
    # request is `SUCCEEDED`, the response includes a URL for an Amazon S3 bucket
    # where you can view the data in a CSV file.
    exports_info: typing.List["ExportInfo"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The `nextToken` value to include in a future `DescribeExportTasks` request.
    # When the results of a `DescribeExportTasks` request exceed `maxResults`,
    # this value can be used to retrieve the next page of results. This value is
    # null when there are no more results to return.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DescribeTagsRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "filters",
                "filters",
                TypeInfo(typing.List[TagFilter]),
            ),
            (
                "max_results",
                "maxResults",
                TypeInfo(int),
            ),
            (
                "next_token",
                "nextToken",
                TypeInfo(str),
            ),
        ]

    # You can filter the list using a _key_ - _value_ format. You can separate
    # these items by using logical operators. Allowed filters include `tagKey`,
    # `tagValue`, and `configurationId`.
    filters: typing.List["TagFilter"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The total number of items to return in a single page of output. The maximum
    # value is 100.
    max_results: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A token to start the list. Use this token to get the next set of results.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DescribeTagsResponse(OutputShapeBase):
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
                "tags",
                TypeInfo(typing.List[ConfigurationTag]),
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

    # Depending on the input, this is a list of configuration items tagged with a
    # specific tag, or a list of tags for a specific configuration item.
    tags: typing.List["ConfigurationTag"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The call returns a token. Use this token to get the next set of results.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DisassociateConfigurationItemsFromApplicationRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "application_configuration_id",
                "applicationConfigurationId",
                TypeInfo(str),
            ),
            (
                "configuration_ids",
                "configurationIds",
                TypeInfo(typing.List[str]),
            ),
        ]

    # Configuration ID of an application from which each item is disassociated.
    application_configuration_id: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Configuration ID of each item to be disassociated from an application.
    configuration_ids: typing.List[str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class DisassociateConfigurationItemsFromApplicationResponse(OutputShapeBase):
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
class ExportConfigurationsResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "export_id",
                "exportId",
                TypeInfo(str),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A unique identifier that you can use to query the export status.
    export_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )


class ExportDataFormat(str):
    CSV = "CSV"
    GRAPHML = "GRAPHML"


@dataclasses.dataclass
class ExportFilter(ShapeBase):
    """
    Used to select which agent's data is to be exported. A single agent ID may be
    selected for export using the
    [StartExportTask](http://docs.aws.amazon.com/application-
    discovery/latest/APIReference/API_StartExportTask.html) action.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "name",
                "name",
                TypeInfo(str),
            ),
            (
                "values",
                "values",
                TypeInfo(typing.List[str]),
            ),
            (
                "condition",
                "condition",
                TypeInfo(str),
            ),
        ]

    # A single `ExportFilter` name. Supported filters: `agentId`.
    name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A single `agentId` for a Discovery Agent. An `agentId` can be found using
    # the [DescribeAgents](http://docs.aws.amazon.com/application-
    # discovery/latest/APIReference/API_DescribeExportTasks.html) action.
    # Typically an ADS `agentId` is in the form `o-0123456789abcdef0`.
    values: typing.List[str] = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Supported condition: `EQUALS`
    condition: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ExportInfo(ShapeBase):
    """
    Information regarding the export status of discovered data. The value is an
    array of objects.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "export_id",
                "exportId",
                TypeInfo(str),
            ),
            (
                "export_status",
                "exportStatus",
                TypeInfo(typing.Union[str, ExportStatus]),
            ),
            (
                "status_message",
                "statusMessage",
                TypeInfo(str),
            ),
            (
                "export_request_time",
                "exportRequestTime",
                TypeInfo(datetime.datetime),
            ),
            (
                "configurations_download_url",
                "configurationsDownloadUrl",
                TypeInfo(str),
            ),
            (
                "is_truncated",
                "isTruncated",
                TypeInfo(bool),
            ),
            (
                "requested_start_time",
                "requestedStartTime",
                TypeInfo(datetime.datetime),
            ),
            (
                "requested_end_time",
                "requestedEndTime",
                TypeInfo(datetime.datetime),
            ),
        ]

    # A unique identifier used to query an export.
    export_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The status of the data export job.
    export_status: typing.Union[str, "ExportStatus"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A status message provided for API callers.
    status_message: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The time that the data export was initiated.
    export_request_time: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A URL for an Amazon S3 bucket where you can review the exported data. The
    # URL is displayed only if the export succeeded.
    configurations_download_url: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # If true, the export of agent information exceeded the size limit for a
    # single export and the exported data is incomplete for the requested time
    # range. To address this, select a smaller time range for the export by using
    # `startDate` and `endDate`.
    is_truncated: bool = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The value of `startTime` parameter in the `StartExportTask` request. If no
    # `startTime` was requested, this result does not appear in `ExportInfo`.
    requested_start_time: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The `endTime` used in the `StartExportTask` request. If no `endTime` was
    # requested, this result does not appear in `ExportInfo`.
    requested_end_time: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


class ExportStatus(str):
    FAILED = "FAILED"
    SUCCEEDED = "SUCCEEDED"
    IN_PROGRESS = "IN_PROGRESS"


@dataclasses.dataclass
class Filter(ShapeBase):
    """
    A filter that can use conditional operators.

    For more information about filters, see [Querying Discovered Configuration
    Items](http://docs.aws.amazon.com/application-
    discovery/latest/APIReference/discovery-api-queries.html).
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "name",
                "name",
                TypeInfo(str),
            ),
            (
                "values",
                "values",
                TypeInfo(typing.List[str]),
            ),
            (
                "condition",
                "condition",
                TypeInfo(str),
            ),
        ]

    # The name of the filter.
    name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A string value on which to filter. For example, if you choose the
    # `destinationServer.osVersion` filter name, you could specify `Ubuntu` for
    # the value.
    values: typing.List[str] = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A conditional operator. The following operators are valid: EQUALS,
    # NOT_EQUALS, CONTAINS, NOT_CONTAINS. If you specify multiple filters, the
    # system utilizes all filters as though concatenated by _AND_. If you specify
    # multiple values for a particular filter, the system differentiates the
    # values using _OR_. Calling either _DescribeConfigurations_ or
    # _ListConfigurations_ returns attributes of matching configuration items.
    condition: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class GetDiscoverySummaryRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class GetDiscoverySummaryResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "servers",
                "servers",
                TypeInfo(int),
            ),
            (
                "applications",
                "applications",
                TypeInfo(int),
            ),
            (
                "servers_mapped_to_applications",
                "serversMappedToApplications",
                TypeInfo(int),
            ),
            (
                "servers_mappedto_tags",
                "serversMappedtoTags",
                TypeInfo(int),
            ),
            (
                "agent_summary",
                "agentSummary",
                TypeInfo(CustomerAgentInfo),
            ),
            (
                "connector_summary",
                "connectorSummary",
                TypeInfo(CustomerConnectorInfo),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The number of servers discovered.
    servers: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The number of applications discovered.
    applications: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The number of servers mapped to applications.
    servers_mapped_to_applications: int = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The number of servers mapped to tags.
    servers_mappedto_tags: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Details about discovered agents, including agent status and health.
    agent_summary: "CustomerAgentInfo" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Details about discovered connectors, including connector status and health.
    connector_summary: "CustomerConnectorInfo" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class InvalidParameterException(ShapeBase):
    """
    One or more parameters are not valid. Verify the parameters and try again.
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
class InvalidParameterValueException(ShapeBase):
    """
    The value of one or more parameters are either invalid or out of range. Verify
    the parameter values and try again.
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
class ListConfigurationsRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "configuration_type",
                "configurationType",
                TypeInfo(typing.Union[str, ConfigurationItemType]),
            ),
            (
                "filters",
                "filters",
                TypeInfo(typing.List[Filter]),
            ),
            (
                "max_results",
                "maxResults",
                TypeInfo(int),
            ),
            (
                "next_token",
                "nextToken",
                TypeInfo(str),
            ),
            (
                "order_by",
                "orderBy",
                TypeInfo(typing.List[OrderByElement]),
            ),
        ]

    # A valid configuration identified by Application Discovery Service.
    configuration_type: typing.Union[str, "ConfigurationItemType"
                                    ] = dataclasses.field(
                                        default=ShapeBase.NOT_SET,
                                    )

    # You can filter the request using various logical operators and a _key_ -
    # _value_ format. For example:

    # `{"key": "serverType", "value": "webServer"}`

    # For a complete list of filter options and guidance about using them with
    # this action, see [Querying Discovered Configuration
    # Items](http://docs.aws.amazon.com/application-
    # discovery/latest/APIReference/discovery-api-
    # queries.html#ListConfigurations).
    filters: typing.List["Filter"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The total number of items to return. The maximum value is 100.
    max_results: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Token to retrieve the next set of results. For example, if a previous call
    # to ListConfigurations returned 100 items, but you set
    # `ListConfigurationsRequest$maxResults` to 10, you received a set of 10
    # results along with a token. Use that token in this query to get the next
    # set of 10.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Certain filter criteria return output that can be sorted in ascending or
    # descending order. For a list of output characteristics for each filter, see
    # [Using the ListConfigurations
    # Action](http://docs.aws.amazon.com/application-
    # discovery/latest/APIReference/discovery-api-
    # queries.html#ListConfigurations).
    order_by: typing.List["OrderByElement"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


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
                "configurations",
                TypeInfo(typing.List[typing.Dict[str, str]]),
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

    # Returns configuration details, including the configuration ID, attribute
    # names, and attribute values.
    configurations: typing.List[typing.Dict[str, str]] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Token to retrieve the next set of results. For example, if your call to
    # ListConfigurations returned 100 items, but you set
    # `ListConfigurationsRequest$maxResults` to 10, you received a set of 10
    # results along with this token. Use this token in the next query to retrieve
    # the next set of 10.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ListServerNeighborsRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "configuration_id",
                "configurationId",
                TypeInfo(str),
            ),
            (
                "port_information_needed",
                "portInformationNeeded",
                TypeInfo(bool),
            ),
            (
                "neighbor_configuration_ids",
                "neighborConfigurationIds",
                TypeInfo(typing.List[str]),
            ),
            (
                "max_results",
                "maxResults",
                TypeInfo(int),
            ),
            (
                "next_token",
                "nextToken",
                TypeInfo(str),
            ),
        ]

    # Configuration ID of the server for which neighbors are being listed.
    configuration_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Flag to indicate if port and protocol information is needed as part of the
    # response.
    port_information_needed: bool = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # List of configuration IDs to test for one-hop-away.
    neighbor_configuration_ids: typing.List[str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Maximum number of results to return in a single page of output.
    max_results: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Token to retrieve the next set of results. For example, if you previously
    # specified 100 IDs for `ListServerNeighborsRequest$neighborConfigurationIds`
    # but set `ListServerNeighborsRequest$maxResults` to 10, you received a set
    # of 10 results along with a token. Use that token in this query to get the
    # next set of 10.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ListServerNeighborsResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "neighbors",
                "neighbors",
                TypeInfo(typing.List[NeighborConnectionDetail]),
            ),
            (
                "next_token",
                "nextToken",
                TypeInfo(str),
            ),
            (
                "known_dependency_count",
                "knownDependencyCount",
                TypeInfo(int),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # List of distinct servers that are one hop away from the given server.
    neighbors: typing.List["NeighborConnectionDetail"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Token to retrieve the next set of results. For example, if you specified
    # 100 IDs for `ListServerNeighborsRequest$neighborConfigurationIds` but set
    # `ListServerNeighborsRequest$maxResults` to 10, you received a set of 10
    # results along with this token. Use this token in the next query to retrieve
    # the next set of 10.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Count of distinct servers that are one hop away from the given server.
    known_dependency_count: int = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class NeighborConnectionDetail(ShapeBase):
    """
    Details about neighboring servers.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "source_server_id",
                "sourceServerId",
                TypeInfo(str),
            ),
            (
                "destination_server_id",
                "destinationServerId",
                TypeInfo(str),
            ),
            (
                "connections_count",
                "connectionsCount",
                TypeInfo(int),
            ),
            (
                "destination_port",
                "destinationPort",
                TypeInfo(int),
            ),
            (
                "transport_protocol",
                "transportProtocol",
                TypeInfo(str),
            ),
        ]

    # The ID of the server that opened the network connection.
    source_server_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The ID of the server that accepted the network connection.
    destination_server_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The number of open network connections with the neighboring server.
    connections_count: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The destination network port for the connection.
    destination_port: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The network protocol used for the connection.
    transport_protocol: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class OperationNotPermittedException(ShapeBase):
    """
    This operation is not permitted.
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
class OrderByElement(ShapeBase):
    """
    A field and direction for ordered output.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "field_name",
                "fieldName",
                TypeInfo(str),
            ),
            (
                "sort_order",
                "sortOrder",
                TypeInfo(typing.Union[str, orderString]),
            ),
        ]

    # The field on which to order.
    field_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Ordering direction.
    sort_order: typing.Union[str, "orderString"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class ResourceInUseException(ShapeBase):
    """

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
class ResourceNotFoundException(ShapeBase):
    """
    The specified configuration ID was not located. Verify the configuration ID and
    try again.
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
class ServerInternalErrorException(ShapeBase):
    """
    The server experienced an internal error. Try again.
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
class StartContinuousExportRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class StartContinuousExportResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "export_id",
                "exportId",
                TypeInfo(str),
            ),
            (
                "s3_bucket",
                "s3Bucket",
                TypeInfo(str),
            ),
            (
                "start_time",
                "startTime",
                TypeInfo(datetime.datetime),
            ),
            (
                "data_source",
                "dataSource",
                TypeInfo(typing.Union[str, DataSource]),
            ),
            (
                "schema_storage_config",
                "schemaStorageConfig",
                TypeInfo(typing.Dict[str, str]),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The unique ID assigned to this export.
    export_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The name of the s3 bucket where the export data parquet files are stored.
    s3_bucket: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The timestamp representing when the continuous export was started.
    start_time: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The type of data collector used to gather this data (currently only offered
    # for AGENT).
    data_source: typing.Union[str, "DataSource"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A dictionary which describes how the data is stored.

    #   * `databaseName` \- the name of the Glue database used to store the schema.
    schema_storage_config: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class StartDataCollectionByAgentIdsRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "agent_ids",
                "agentIds",
                TypeInfo(typing.List[str]),
            ),
        ]

    # The IDs of the agents or connectors from which to start collecting data. If
    # you send a request to an agent/connector ID that you do not have permission
    # to contact, according to your AWS account, the service does not throw an
    # exception. Instead, it returns the error in the _Description_ field. If you
    # send a request to multiple agents/connectors and you do not have permission
    # to contact some of those agents/connectors, the system does not throw an
    # exception. Instead, the system shows `Failed` in the _Description_ field.
    agent_ids: typing.List[str] = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class StartDataCollectionByAgentIdsResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "agents_configuration_status",
                "agentsConfigurationStatus",
                TypeInfo(typing.List[AgentConfigurationStatus]),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Information about agents or the connector that were instructed to start
    # collecting data. Information includes the agent/connector ID, a description
    # of the operation performed, and whether the agent/connector configuration
    # was updated.
    agents_configuration_status: typing.List["AgentConfigurationStatus"
                                            ] = dataclasses.field(
                                                default=ShapeBase.NOT_SET,
                                            )


@dataclasses.dataclass
class StartExportTaskRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "export_data_format",
                "exportDataFormat",
                TypeInfo(typing.List[typing.Union[str, ExportDataFormat]]),
            ),
            (
                "filters",
                "filters",
                TypeInfo(typing.List[ExportFilter]),
            ),
            (
                "start_time",
                "startTime",
                TypeInfo(datetime.datetime),
            ),
            (
                "end_time",
                "endTime",
                TypeInfo(datetime.datetime),
            ),
        ]

    # The file format for the returned export data. Default value is `CSV`.
    # **Note:** _The_ `GRAPHML` _option has been deprecated._
    export_data_format: typing.List[typing.Union[str, "ExportDataFormat"]
                                   ] = dataclasses.field(
                                       default=ShapeBase.NOT_SET,
                                   )

    # If a filter is present, it selects the single `agentId` of the Application
    # Discovery Agent for which data is exported. The `agentId` can be found in
    # the results of the `DescribeAgents` API or CLI. If no filter is present,
    # `startTime` and `endTime` are ignored and exported data includes both
    # Agentless Discovery Connector data and summary data from Application
    # Discovery agents.
    filters: typing.List["ExportFilter"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The start timestamp for exported data from the single Application Discovery
    # Agent selected in the filters. If no value is specified, data is exported
    # starting from the first data collected by the agent.
    start_time: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The end timestamp for exported data from the single Application Discovery
    # Agent selected in the filters. If no value is specified, exported data
    # includes the most recent data collected by the agent.
    end_time: datetime.datetime = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class StartExportTaskResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "export_id",
                "exportId",
                TypeInfo(str),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A unique identifier used to query the status of an export request.
    export_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class StopContinuousExportRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "export_id",
                "exportId",
                TypeInfo(str),
            ),
        ]

    # The unique ID assigned to this export.
    export_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class StopContinuousExportResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "start_time",
                "startTime",
                TypeInfo(datetime.datetime),
            ),
            (
                "stop_time",
                "stopTime",
                TypeInfo(datetime.datetime),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Timestamp that represents when this continuous export started collecting
    # data.
    start_time: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Timestamp that represents when this continuous export was stopped.
    stop_time: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class StopDataCollectionByAgentIdsRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "agent_ids",
                "agentIds",
                TypeInfo(typing.List[str]),
            ),
        ]

    # The IDs of the agents or connectors from which to stop collecting data.
    agent_ids: typing.List[str] = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class StopDataCollectionByAgentIdsResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "agents_configuration_status",
                "agentsConfigurationStatus",
                TypeInfo(typing.List[AgentConfigurationStatus]),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Information about the agents or connector that were instructed to stop
    # collecting data. Information includes the agent/connector ID, a description
    # of the operation performed, and whether the agent/connector configuration
    # was updated.
    agents_configuration_status: typing.List["AgentConfigurationStatus"
                                            ] = dataclasses.field(
                                                default=ShapeBase.NOT_SET,
                                            )


@dataclasses.dataclass
class Tag(ShapeBase):
    """
    Metadata that help you categorize IT assets.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "key",
                "key",
                TypeInfo(str),
            ),
            (
                "value",
                "value",
                TypeInfo(str),
            ),
        ]

    # The type of tag on which to filter.
    key: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A value for a tag key on which to filter.
    value: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class TagFilter(ShapeBase):
    """
    The tag filter. Valid names are: `tagKey`, `tagValue`, `configurationId`.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "name",
                "name",
                TypeInfo(str),
            ),
            (
                "values",
                "values",
                TypeInfo(typing.List[str]),
            ),
        ]

    # A name of the tag filter.
    name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Values for the tag filter.
    values: typing.List[str] = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class UpdateApplicationRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "configuration_id",
                "configurationId",
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

    # Configuration ID of the application to be updated.
    configuration_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # New name of the application to be updated.
    name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # New description of the application to be updated.
    description: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class UpdateApplicationResponse(OutputShapeBase):
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


class orderString(str):
    ASC = "ASC"
    DESC = "DESC"
