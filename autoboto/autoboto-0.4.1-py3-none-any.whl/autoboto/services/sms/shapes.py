import datetime
import typing
from autoboto import ShapeBase, OutputShapeBase, TypeInfo
import dataclasses


@dataclasses.dataclass
class Connector(ShapeBase):
    """
    Object representing a Connector
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
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
                "status",
                "status",
                TypeInfo(typing.Union[str, ConnectorStatus]),
            ),
            (
                "capability_list",
                "capabilityList",
                TypeInfo(typing.List[typing.Union[str, ConnectorCapability]]),
            ),
            (
                "vm_manager_name",
                "vmManagerName",
                TypeInfo(str),
            ),
            (
                "vm_manager_type",
                "vmManagerType",
                TypeInfo(typing.Union[str, VmManagerType]),
            ),
            (
                "vm_manager_id",
                "vmManagerId",
                TypeInfo(str),
            ),
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
            (
                "associated_on",
                "associatedOn",
                TypeInfo(datetime.datetime),
            ),
        ]

    # Unique Identifier for Connector
    connector_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Connector version string
    version: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Status of on-premise Connector
    status: typing.Union[str, "ConnectorStatus"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # List of Connector Capabilities
    capability_list: typing.List[typing.Union[str, "ConnectorCapability"]
                                ] = dataclasses.field(
                                    default=ShapeBase.NOT_SET,
                                )

    # VM Manager Name
    vm_manager_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # VM Management Product
    vm_manager_type: typing.Union[str, "VmManagerType"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Unique Identifier for VM Manager
    vm_manager_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Internet Protocol (IP) Address
    ip_address: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Hardware (MAC) address
    mac_address: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Timestamp of an operation
    associated_on: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


class ConnectorCapability(str):
    """
    Capabilities for a Connector
    """
    VSPHERE = "VSPHERE"


class ConnectorStatus(str):
    """
    Status of on-premise Connector
    """
    HEALTHY = "HEALTHY"
    UNHEALTHY = "UNHEALTHY"


@dataclasses.dataclass
class CreateReplicationJobRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "server_id",
                "serverId",
                TypeInfo(str),
            ),
            (
                "seed_replication_time",
                "seedReplicationTime",
                TypeInfo(datetime.datetime),
            ),
            (
                "frequency",
                "frequency",
                TypeInfo(int),
            ),
            (
                "license_type",
                "licenseType",
                TypeInfo(typing.Union[str, LicenseType]),
            ),
            (
                "role_name",
                "roleName",
                TypeInfo(str),
            ),
            (
                "description",
                "description",
                TypeInfo(str),
            ),
        ]

    # Unique Identifier for a server
    server_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Timestamp of an operation
    seed_replication_time: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Interval between Replication Runs. This value is specified in hours, and
    # represents the time between consecutive Replication Runs.
    frequency: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The license type to be used for the Amazon Machine Image (AMI) created
    # after a successful ReplicationRun.
    license_type: typing.Union[str, "LicenseType"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Name of service role in customer's account to be used by SMS service.
    role_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The description for a Replication Job/Run.
    description: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class CreateReplicationJobResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "replication_job_id",
                "replicationJobId",
                TypeInfo(str),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The unique identifier for a Replication Job.
    replication_job_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DeleteReplicationJobRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "replication_job_id",
                "replicationJobId",
                TypeInfo(str),
            ),
        ]

    # The unique identifier for a Replication Job.
    replication_job_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DeleteReplicationJobResponse(OutputShapeBase):
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
class DeleteServerCatalogRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class DeleteServerCatalogResponse(OutputShapeBase):
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
class DisassociateConnectorRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "connector_id",
                "connectorId",
                TypeInfo(str),
            ),
        ]

    # Unique Identifier for Connector
    connector_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DisassociateConnectorResponse(OutputShapeBase):
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
class GetConnectorsRequest(ShapeBase):
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

    # Pagination token to pass as input to API call
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The maximum number of results to return in one API call. If left empty,
    # this will default to 50.
    max_results: int = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class GetConnectorsResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "connector_list",
                "connectorList",
                TypeInfo(typing.List[Connector]),
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

    # List of connectors
    connector_list: typing.List["Connector"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Pagination token to pass as input to API call
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    def paginate(self,
                ) -> typing.Generator["GetConnectorsResponse", None, None]:
        yield from super()._paginate()


@dataclasses.dataclass
class GetReplicationJobsRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "replication_job_id",
                "replicationJobId",
                TypeInfo(str),
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

    # The unique identifier for a Replication Job.
    replication_job_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Pagination token to pass as input to API call
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The maximum number of results to return in one API call. If left empty,
    # this will default to 50.
    max_results: int = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class GetReplicationJobsResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "replication_job_list",
                "replicationJobList",
                TypeInfo(typing.List[ReplicationJob]),
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

    # List of Replication Jobs
    replication_job_list: typing.List["ReplicationJob"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Pagination token to pass as input to API call
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    def paginate(self,
                ) -> typing.Generator["GetReplicationJobsResponse", None, None]:
        yield from super()._paginate()


@dataclasses.dataclass
class GetReplicationRunsRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "replication_job_id",
                "replicationJobId",
                TypeInfo(str),
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

    # The unique identifier for a Replication Job.
    replication_job_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Pagination token to pass as input to API call
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The maximum number of results to return in one API call. If left empty,
    # this will default to 50.
    max_results: int = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class GetReplicationRunsResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "replication_job",
                "replicationJob",
                TypeInfo(ReplicationJob),
            ),
            (
                "replication_run_list",
                "replicationRunList",
                TypeInfo(typing.List[ReplicationRun]),
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

    # Object representing a Replication Job
    replication_job: "ReplicationJob" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # List of Replication Runs
    replication_run_list: typing.List["ReplicationRun"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Pagination token to pass as input to API call
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    def paginate(self,
                ) -> typing.Generator["GetReplicationRunsResponse", None, None]:
        yield from super()._paginate()


@dataclasses.dataclass
class GetServersRequest(ShapeBase):
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

    # Pagination token to pass as input to API call
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The maximum number of results to return in one API call. If left empty,
    # this will default to 50.
    max_results: int = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class GetServersResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "last_modified_on",
                "lastModifiedOn",
                TypeInfo(datetime.datetime),
            ),
            (
                "server_catalog_status",
                "serverCatalogStatus",
                TypeInfo(typing.Union[str, ServerCatalogStatus]),
            ),
            (
                "server_list",
                "serverList",
                TypeInfo(typing.List[Server]),
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

    # Timestamp of an operation
    last_modified_on: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Status of Server catalog
    server_catalog_status: typing.Union[str, "ServerCatalogStatus"
                                       ] = dataclasses.field(
                                           default=ShapeBase.NOT_SET,
                                       )

    # List of servers from catalog
    server_list: typing.List["Server"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Pagination token to pass as input to API call
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    def paginate(self, ) -> typing.Generator["GetServersResponse", None, None]:
        yield from super()._paginate()


@dataclasses.dataclass
class ImportServerCatalogRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class ImportServerCatalogResponse(OutputShapeBase):
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
class InternalError(ShapeBase):
    """
    An internal error has occured.
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

    # Error Message string
    message: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class InvalidParameterException(ShapeBase):
    """
    A parameter specified in the request is not valid, is unsupported, or cannot be
    used.
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

    # Error Message string
    message: str = dataclasses.field(default=ShapeBase.NOT_SET, )


class LicenseType(str):
    """
    The license type to be used for the Amazon Machine Image (AMI) created after a
    successful ReplicationRun.
    """
    AWS = "AWS"
    BYOL = "BYOL"


@dataclasses.dataclass
class MissingRequiredParameterException(ShapeBase):
    """
    The request is missing a required parameter. Ensure that you have supplied all
    the required parameters for the request.
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

    # Error Message string
    message: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class NoConnectorsAvailableException(ShapeBase):
    """
    No connectors are available to handle this request. Please associate
    connector(s) and verify any existing connectors are healthy and can respond to
    requests.
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

    # Error Message string
    message: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class OperationNotPermittedException(ShapeBase):
    """
    The specified operation is not allowed. This error can occur for a number of
    reasons; for example, you might be trying to start a Replication Run before seed
    Replication Run.
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

    # Error Message string
    message: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ReplicationJob(ShapeBase):
    """
    Object representing a Replication Job
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "replication_job_id",
                "replicationJobId",
                TypeInfo(str),
            ),
            (
                "server_id",
                "serverId",
                TypeInfo(str),
            ),
            (
                "server_type",
                "serverType",
                TypeInfo(typing.Union[str, ServerType]),
            ),
            (
                "vm_server",
                "vmServer",
                TypeInfo(VmServer),
            ),
            (
                "seed_replication_time",
                "seedReplicationTime",
                TypeInfo(datetime.datetime),
            ),
            (
                "frequency",
                "frequency",
                TypeInfo(int),
            ),
            (
                "next_replication_run_start_time",
                "nextReplicationRunStartTime",
                TypeInfo(datetime.datetime),
            ),
            (
                "license_type",
                "licenseType",
                TypeInfo(typing.Union[str, LicenseType]),
            ),
            (
                "role_name",
                "roleName",
                TypeInfo(str),
            ),
            (
                "latest_ami_id",
                "latestAmiId",
                TypeInfo(str),
            ),
            (
                "state",
                "state",
                TypeInfo(typing.Union[str, ReplicationJobState]),
            ),
            (
                "status_message",
                "statusMessage",
                TypeInfo(str),
            ),
            (
                "description",
                "description",
                TypeInfo(str),
            ),
            (
                "replication_run_list",
                "replicationRunList",
                TypeInfo(typing.List[ReplicationRun]),
            ),
        ]

    # The unique identifier for a Replication Job.
    replication_job_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Unique Identifier for a server
    server_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Type of server.
    server_type: typing.Union[str, "ServerType"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Object representing a VM server
    vm_server: "VmServer" = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Timestamp of an operation
    seed_replication_time: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Interval between Replication Runs. This value is specified in hours, and
    # represents the time between consecutive Replication Runs.
    frequency: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Timestamp of an operation
    next_replication_run_start_time: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The license type to be used for the Amazon Machine Image (AMI) created
    # after a successful ReplicationRun.
    license_type: typing.Union[str, "LicenseType"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Name of service role in customer's account to be used by SMS service.
    role_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The AMI id for the image resulting from a Replication Run.
    latest_ami_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Current state of Replication Job
    state: typing.Union[str, "ReplicationJobState"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # String describing current status of Replication Job
    status_message: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The description for a Replication Job/Run.
    description: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # List of Replication Runs
    replication_run_list: typing.List["ReplicationRun"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class ReplicationJobAlreadyExistsException(ShapeBase):
    """
    An active Replication Job already exists for the specified server.
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

    # Error Message string
    message: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ReplicationJobNotFoundException(ShapeBase):
    """
    The specified Replication Job cannot be found.
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

    # Error Message string
    message: str = dataclasses.field(default=ShapeBase.NOT_SET, )


class ReplicationJobState(str):
    """
    Current state of Replication Job
    """
    PENDING = "PENDING"
    ACTIVE = "ACTIVE"
    FAILED = "FAILED"
    DELETING = "DELETING"
    DELETED = "DELETED"


@dataclasses.dataclass
class ReplicationRun(ShapeBase):
    """
    Object representing a Replication Run
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "replication_run_id",
                "replicationRunId",
                TypeInfo(str),
            ),
            (
                "state",
                "state",
                TypeInfo(typing.Union[str, ReplicationRunState]),
            ),
            (
                "type",
                "type",
                TypeInfo(typing.Union[str, ReplicationRunType]),
            ),
            (
                "status_message",
                "statusMessage",
                TypeInfo(str),
            ),
            (
                "ami_id",
                "amiId",
                TypeInfo(str),
            ),
            (
                "scheduled_start_time",
                "scheduledStartTime",
                TypeInfo(datetime.datetime),
            ),
            (
                "completed_time",
                "completedTime",
                TypeInfo(datetime.datetime),
            ),
            (
                "description",
                "description",
                TypeInfo(str),
            ),
        ]

    # The unique identifier for a Replication Run.
    replication_run_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Current state of Replication Run
    state: typing.Union[str, "ReplicationRunState"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Type of Replication Run
    type: typing.Union[str, "ReplicationRunType"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # String describing current status of Replication Run
    status_message: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The AMI id for the image resulting from a Replication Run.
    ami_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Timestamp of an operation
    scheduled_start_time: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Timestamp of an operation
    completed_time: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The description for a Replication Job/Run.
    description: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ReplicationRunLimitExceededException(ShapeBase):
    """
    This user has exceeded the maximum allowed Replication Run limit.
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

    # Error Message string
    message: str = dataclasses.field(default=ShapeBase.NOT_SET, )


class ReplicationRunState(str):
    """
    Current state of Replication Run
    """
    PENDING = "PENDING"
    MISSED = "MISSED"
    ACTIVE = "ACTIVE"
    FAILED = "FAILED"
    COMPLETED = "COMPLETED"
    DELETING = "DELETING"
    DELETED = "DELETED"


class ReplicationRunType(str):
    """
    Type of Replication Run
    """
    ON_DEMAND = "ON_DEMAND"
    AUTOMATIC = "AUTOMATIC"


@dataclasses.dataclass
class Server(ShapeBase):
    """
    Object representing a server
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "server_id",
                "serverId",
                TypeInfo(str),
            ),
            (
                "server_type",
                "serverType",
                TypeInfo(typing.Union[str, ServerType]),
            ),
            (
                "vm_server",
                "vmServer",
                TypeInfo(VmServer),
            ),
            (
                "replication_job_id",
                "replicationJobId",
                TypeInfo(str),
            ),
            (
                "replication_job_terminated",
                "replicationJobTerminated",
                TypeInfo(bool),
            ),
        ]

    # Unique Identifier for a server
    server_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Type of server.
    server_type: typing.Union[str, "ServerType"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Object representing a VM server
    vm_server: "VmServer" = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The unique identifier for a Replication Job.
    replication_job_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # An indicator of the Replication Job being deleted or failed.
    replication_job_terminated: bool = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class ServerCannotBeReplicatedException(ShapeBase):
    """
    The provided server cannot be replicated.
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

    # Error Message string
    message: str = dataclasses.field(default=ShapeBase.NOT_SET, )


class ServerCatalogStatus(str):
    """
    Status of Server catalog
    """
    NOT_IMPORTED = "NOT_IMPORTED"
    IMPORTING = "IMPORTING"
    AVAILABLE = "AVAILABLE"
    DELETED = "DELETED"
    EXPIRED = "EXPIRED"


class ServerType(str):
    """
    Type of server.
    """
    VIRTUAL_MACHINE = "VIRTUAL_MACHINE"


@dataclasses.dataclass
class StartOnDemandReplicationRunRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "replication_job_id",
                "replicationJobId",
                TypeInfo(str),
            ),
            (
                "description",
                "description",
                TypeInfo(str),
            ),
        ]

    # The unique identifier for a Replication Job.
    replication_job_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The description for a Replication Job/Run.
    description: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class StartOnDemandReplicationRunResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "replication_run_id",
                "replicationRunId",
                TypeInfo(str),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The unique identifier for a Replication Run.
    replication_run_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class UnauthorizedOperationException(ShapeBase):
    """
    This user does not have permissions to perform this operation.
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

    # Error Message string
    message: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class UpdateReplicationJobRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "replication_job_id",
                "replicationJobId",
                TypeInfo(str),
            ),
            (
                "frequency",
                "frequency",
                TypeInfo(int),
            ),
            (
                "next_replication_run_start_time",
                "nextReplicationRunStartTime",
                TypeInfo(datetime.datetime),
            ),
            (
                "license_type",
                "licenseType",
                TypeInfo(typing.Union[str, LicenseType]),
            ),
            (
                "role_name",
                "roleName",
                TypeInfo(str),
            ),
            (
                "description",
                "description",
                TypeInfo(str),
            ),
        ]

    # The unique identifier for a Replication Job.
    replication_job_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Interval between Replication Runs. This value is specified in hours, and
    # represents the time between consecutive Replication Runs.
    frequency: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Timestamp of an operation
    next_replication_run_start_time: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The license type to be used for the Amazon Machine Image (AMI) created
    # after a successful ReplicationRun.
    license_type: typing.Union[str, "LicenseType"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Name of service role in customer's account to be used by SMS service.
    role_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The description for a Replication Job/Run.
    description: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class UpdateReplicationJobResponse(OutputShapeBase):
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


class VmManagerType(str):
    """
    VM Management Product
    """
    VSPHERE = "VSPHERE"


@dataclasses.dataclass
class VmServer(ShapeBase):
    """
    Object representing a VM server
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "vm_server_address",
                "vmServerAddress",
                TypeInfo(VmServerAddress),
            ),
            (
                "vm_name",
                "vmName",
                TypeInfo(str),
            ),
            (
                "vm_manager_name",
                "vmManagerName",
                TypeInfo(str),
            ),
            (
                "vm_manager_type",
                "vmManagerType",
                TypeInfo(typing.Union[str, VmManagerType]),
            ),
            (
                "vm_path",
                "vmPath",
                TypeInfo(str),
            ),
        ]

    # Object representing a server's location
    vm_server_address: "VmServerAddress" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Name of Virtual Machine
    vm_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # VM Manager Name
    vm_manager_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # VM Management Product
    vm_manager_type: typing.Union[str, "VmManagerType"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Path to VM
    vm_path: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class VmServerAddress(ShapeBase):
    """
    Object representing a server's location
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "vm_manager_id",
                "vmManagerId",
                TypeInfo(str),
            ),
            (
                "vm_id",
                "vmId",
                TypeInfo(str),
            ),
        ]

    # Unique Identifier for VM Manager
    vm_manager_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Unique Identifier for a VM
    vm_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )
