import datetime
import typing
from autoboto import ShapeBase, OutputShapeBase, TypeInfo
import dataclasses


@dataclasses.dataclass
class AccessDeniedException(ShapeBase):
    """
    Access to a resource was denied.
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

    # A message describing the problem.
    message: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class Action(ShapeBase):
    """
    Defines an action to be initiated by a trigger.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "job_name",
                "JobName",
                TypeInfo(str),
            ),
            (
                "arguments",
                "Arguments",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "timeout",
                "Timeout",
                TypeInfo(int),
            ),
            (
                "notification_property",
                "NotificationProperty",
                TypeInfo(NotificationProperty),
            ),
            (
                "security_configuration",
                "SecurityConfiguration",
                TypeInfo(str),
            ),
        ]

    # The name of a job to be executed.
    job_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Arguments to be passed to the job run.

    # You can specify arguments here that your own job-execution script consumes,
    # as well as arguments that AWS Glue itself consumes.

    # For information about how to specify and consume your own Job arguments,
    # see the [Calling AWS Glue APIs in
    # Python](http://docs.aws.amazon.com/glue/latest/dg/aws-glue-programming-
    # python-calling.html) topic in the developer guide.

    # For information about the key-value pairs that AWS Glue consumes to set up
    # your job, see the [Special Parameters Used by AWS
    # Glue](http://docs.aws.amazon.com/glue/latest/dg/aws-glue-programming-etl-
    # glue-arguments.html) topic in the developer guide.
    arguments: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The JobRun timeout in minutes. This is the maximum time that a job run can
    # consume resources before it is terminated and enters `TIMEOUT` status. The
    # default is 2,880 minutes (48 hours). This overrides the timeout value set
    # in the parent job.
    timeout: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Specifies configuration properties of a job run notification.
    notification_property: "NotificationProperty" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The name of the SecurityConfiguration structure to be used with this
    # action.
    security_configuration: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class AlreadyExistsException(ShapeBase):
    """
    A resource to be created or added already exists.
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

    # A message describing the problem.
    message: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class BatchCreatePartitionRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "database_name",
                "DatabaseName",
                TypeInfo(str),
            ),
            (
                "table_name",
                "TableName",
                TypeInfo(str),
            ),
            (
                "partition_input_list",
                "PartitionInputList",
                TypeInfo(typing.List[PartitionInput]),
            ),
            (
                "catalog_id",
                "CatalogId",
                TypeInfo(str),
            ),
        ]

    # The name of the metadata database in which the partition is to be created.
    database_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The name of the metadata table in which the partition is to be created.
    table_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A list of `PartitionInput` structures that define the partitions to be
    # created.
    partition_input_list: typing.List["PartitionInput"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The ID of the catalog in which the partion is to be created. Currently,
    # this should be the AWS account ID.
    catalog_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class BatchCreatePartitionResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "errors",
                "Errors",
                TypeInfo(typing.List[PartitionError]),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Errors encountered when trying to create the requested partitions.
    errors: typing.List["PartitionError"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class BatchDeleteConnectionRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "connection_name_list",
                "ConnectionNameList",
                TypeInfo(typing.List[str]),
            ),
            (
                "catalog_id",
                "CatalogId",
                TypeInfo(str),
            ),
        ]

    # A list of names of the connections to delete.
    connection_name_list: typing.List[str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The ID of the Data Catalog in which the connections reside. If none is
    # supplied, the AWS account ID is used by default.
    catalog_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class BatchDeleteConnectionResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "succeeded",
                "Succeeded",
                TypeInfo(typing.List[str]),
            ),
            (
                "errors",
                "Errors",
                TypeInfo(typing.Dict[str, ErrorDetail]),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A list of names of the connection definitions that were successfully
    # deleted.
    succeeded: typing.List[str] = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A map of the names of connections that were not successfully deleted to
    # error details.
    errors: typing.Dict[str, "ErrorDetail"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class BatchDeletePartitionRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "database_name",
                "DatabaseName",
                TypeInfo(str),
            ),
            (
                "table_name",
                "TableName",
                TypeInfo(str),
            ),
            (
                "partitions_to_delete",
                "PartitionsToDelete",
                TypeInfo(typing.List[PartitionValueList]),
            ),
            (
                "catalog_id",
                "CatalogId",
                TypeInfo(str),
            ),
        ]

    # The name of the catalog database in which the table in question resides.
    database_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The name of the table where the partitions to be deleted is located.
    table_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A list of `PartitionInput` structures that define the partitions to be
    # deleted.
    partitions_to_delete: typing.List["PartitionValueList"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The ID of the Data Catalog where the partition to be deleted resides. If
    # none is supplied, the AWS account ID is used by default.
    catalog_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class BatchDeletePartitionResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "errors",
                "Errors",
                TypeInfo(typing.List[PartitionError]),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Errors encountered when trying to delete the requested partitions.
    errors: typing.List["PartitionError"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class BatchDeleteTableRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "database_name",
                "DatabaseName",
                TypeInfo(str),
            ),
            (
                "tables_to_delete",
                "TablesToDelete",
                TypeInfo(typing.List[str]),
            ),
            (
                "catalog_id",
                "CatalogId",
                TypeInfo(str),
            ),
        ]

    # The name of the catalog database where the tables to delete reside. For
    # Hive compatibility, this name is entirely lowercase.
    database_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A list of the table to delete.
    tables_to_delete: typing.List[str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The ID of the Data Catalog where the table resides. If none is supplied,
    # the AWS account ID is used by default.
    catalog_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class BatchDeleteTableResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "errors",
                "Errors",
                TypeInfo(typing.List[TableError]),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A list of errors encountered in attempting to delete the specified tables.
    errors: typing.List["TableError"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class BatchDeleteTableVersionRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "database_name",
                "DatabaseName",
                TypeInfo(str),
            ),
            (
                "table_name",
                "TableName",
                TypeInfo(str),
            ),
            (
                "version_ids",
                "VersionIds",
                TypeInfo(typing.List[str]),
            ),
            (
                "catalog_id",
                "CatalogId",
                TypeInfo(str),
            ),
        ]

    # The database in the catalog in which the table resides. For Hive
    # compatibility, this name is entirely lowercase.
    database_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The name of the table. For Hive compatibility, this name is entirely
    # lowercase.
    table_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A list of the IDs of versions to be deleted.
    version_ids: typing.List[str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The ID of the Data Catalog where the tables reside. If none is supplied,
    # the AWS account ID is used by default.
    catalog_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class BatchDeleteTableVersionResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "errors",
                "Errors",
                TypeInfo(typing.List[TableVersionError]),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A list of errors encountered while trying to delete the specified table
    # versions.
    errors: typing.List["TableVersionError"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class BatchGetPartitionRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "database_name",
                "DatabaseName",
                TypeInfo(str),
            ),
            (
                "table_name",
                "TableName",
                TypeInfo(str),
            ),
            (
                "partitions_to_get",
                "PartitionsToGet",
                TypeInfo(typing.List[PartitionValueList]),
            ),
            (
                "catalog_id",
                "CatalogId",
                TypeInfo(str),
            ),
        ]

    # The name of the catalog database where the partitions reside.
    database_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The name of the partitions' table.
    table_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A list of partition values identifying the partitions to retrieve.
    partitions_to_get: typing.List["PartitionValueList"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The ID of the Data Catalog where the partitions in question reside. If none
    # is supplied, the AWS account ID is used by default.
    catalog_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class BatchGetPartitionResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "partitions",
                "Partitions",
                TypeInfo(typing.List[Partition]),
            ),
            (
                "unprocessed_keys",
                "UnprocessedKeys",
                TypeInfo(typing.List[PartitionValueList]),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A list of the requested partitions.
    partitions: typing.List["Partition"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A list of the partition values in the request for which partions were not
    # returned.
    unprocessed_keys: typing.List["PartitionValueList"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class BatchStopJobRunError(ShapeBase):
    """
    Records an error that occurred when attempting to stop a specified job run.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "job_name",
                "JobName",
                TypeInfo(str),
            ),
            (
                "job_run_id",
                "JobRunId",
                TypeInfo(str),
            ),
            (
                "error_detail",
                "ErrorDetail",
                TypeInfo(ErrorDetail),
            ),
        ]

    # The name of the job definition used in the job run in question.
    job_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The JobRunId of the job run in question.
    job_run_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Specifies details about the error that was encountered.
    error_detail: "ErrorDetail" = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class BatchStopJobRunRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "job_name",
                "JobName",
                TypeInfo(str),
            ),
            (
                "job_run_ids",
                "JobRunIds",
                TypeInfo(typing.List[str]),
            ),
        ]

    # The name of the job definition for which to stop job runs.
    job_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A list of the JobRunIds that should be stopped for that job definition.
    job_run_ids: typing.List[str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class BatchStopJobRunResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "successful_submissions",
                "SuccessfulSubmissions",
                TypeInfo(typing.List[BatchStopJobRunSuccessfulSubmission]),
            ),
            (
                "errors",
                "Errors",
                TypeInfo(typing.List[BatchStopJobRunError]),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A list of the JobRuns that were successfully submitted for stopping.
    successful_submissions: typing.List["BatchStopJobRunSuccessfulSubmission"
                                       ] = dataclasses.field(
                                           default=ShapeBase.NOT_SET,
                                       )

    # A list of the errors that were encountered in tryng to stop JobRuns,
    # including the JobRunId for which each error was encountered and details
    # about the error.
    errors: typing.List["BatchStopJobRunError"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class BatchStopJobRunSuccessfulSubmission(ShapeBase):
    """
    Records a successful request to stop a specified JobRun.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "job_name",
                "JobName",
                TypeInfo(str),
            ),
            (
                "job_run_id",
                "JobRunId",
                TypeInfo(str),
            ),
        ]

    # The name of the job definition used in the job run that was stopped.
    job_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The JobRunId of the job run that was stopped.
    job_run_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )


class CatalogEncryptionMode(str):
    DISABLED = "DISABLED"
    SSE_KMS = "SSE-KMS"


@dataclasses.dataclass
class CatalogEntry(ShapeBase):
    """
    Specifies a table definition in the Data Catalog.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "database_name",
                "DatabaseName",
                TypeInfo(str),
            ),
            (
                "table_name",
                "TableName",
                TypeInfo(str),
            ),
        ]

    # The database in which the table metadata resides.
    database_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The name of the table in question.
    table_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class CatalogImportStatus(ShapeBase):
    """
    A structure containing migration status information.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "import_completed",
                "ImportCompleted",
                TypeInfo(bool),
            ),
            (
                "import_time",
                "ImportTime",
                TypeInfo(datetime.datetime),
            ),
            (
                "imported_by",
                "ImportedBy",
                TypeInfo(str),
            ),
        ]

    # True if the migration has completed, or False otherwise.
    import_completed: bool = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The time that the migration was started.
    import_time: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The name of the person who initiated the migration.
    imported_by: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class Classifier(ShapeBase):
    """
    Classifiers are triggered during a crawl task. A classifier checks whether a
    given file is in a format it can handle, and if it is, the classifier creates a
    schema in the form of a `StructType` object that matches that data format.

    You can use the standard classifiers that AWS Glue supplies, or you can write
    your own classifiers to best categorize your data sources and specify the
    appropriate schemas to use for them. A classifier can be a `grok` classifier, an
    `XML` classifier, or a `JSON` classifier, as specified in one of the fields in
    the `Classifier` object.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "grok_classifier",
                "GrokClassifier",
                TypeInfo(GrokClassifier),
            ),
            (
                "xml_classifier",
                "XMLClassifier",
                TypeInfo(XMLClassifier),
            ),
            (
                "json_classifier",
                "JsonClassifier",
                TypeInfo(JsonClassifier),
            ),
        ]

    # A `GrokClassifier` object.
    grok_classifier: "GrokClassifier" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # An `XMLClassifier` object.
    xml_classifier: "XMLClassifier" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A `JsonClassifier` object.
    json_classifier: "JsonClassifier" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class CloudWatchEncryption(ShapeBase):
    """
    Specifies how CloudWatch data should be encrypted.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "cloud_watch_encryption_mode",
                "CloudWatchEncryptionMode",
                TypeInfo(typing.Union[str, CloudWatchEncryptionMode]),
            ),
            (
                "kms_key_arn",
                "KmsKeyArn",
                TypeInfo(str),
            ),
        ]

    # The encryption mode to use for CloudWatch data.
    cloud_watch_encryption_mode: typing.Union[str, "CloudWatchEncryptionMode"
                                             ] = dataclasses.field(
                                                 default=ShapeBase.NOT_SET,
                                             )

    # The AWS ARN of the KMS key to be used to encrypt the data.
    kms_key_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )


class CloudWatchEncryptionMode(str):
    DISABLED = "DISABLED"
    SSE_KMS = "SSE-KMS"


@dataclasses.dataclass
class CodeGenEdge(ShapeBase):
    """
    Represents a directional edge in a directed acyclic graph (DAG).
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "source",
                "Source",
                TypeInfo(str),
            ),
            (
                "target",
                "Target",
                TypeInfo(str),
            ),
            (
                "target_parameter",
                "TargetParameter",
                TypeInfo(str),
            ),
        ]

    # The ID of the node at which the edge starts.
    source: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The ID of the node at which the edge ends.
    target: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The target of the edge.
    target_parameter: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class CodeGenNode(ShapeBase):
    """
    Represents a node in a directed acyclic graph (DAG)
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
                "node_type",
                "NodeType",
                TypeInfo(str),
            ),
            (
                "args",
                "Args",
                TypeInfo(typing.List[CodeGenNodeArg]),
            ),
            (
                "line_number",
                "LineNumber",
                TypeInfo(int),
            ),
        ]

    # A node identifier that is unique within the node's graph.
    id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The type of node this is.
    node_type: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Properties of the node, in the form of name-value pairs.
    args: typing.List["CodeGenNodeArg"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The line number of the node.
    line_number: int = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class CodeGenNodeArg(ShapeBase):
    """
    An argument or property of a node.
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
                "value",
                "Value",
                TypeInfo(str),
            ),
            (
                "param",
                "Param",
                TypeInfo(bool),
            ),
        ]

    # The name of the argument or property.
    name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The value of the argument or property.
    value: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # True if the value is used as a parameter.
    param: bool = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class Column(ShapeBase):
    """
    A column in a `Table`.
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
                "type",
                "Type",
                TypeInfo(str),
            ),
            (
                "comment",
                "Comment",
                TypeInfo(str),
            ),
        ]

    # The name of the `Column`.
    name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The datatype of data in the `Column`.
    type: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Free-form text comment.
    comment: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ConcurrentModificationException(ShapeBase):
    """
    Two processes are trying to modify a resource simultaneously.
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

    # A message describing the problem.
    message: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ConcurrentRunsExceededException(ShapeBase):
    """
    Too many jobs are being run concurrently.
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

    # A message describing the problem.
    message: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class Condition(ShapeBase):
    """
    Defines a condition under which a trigger fires.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "logical_operator",
                "LogicalOperator",
                TypeInfo(typing.Union[str, LogicalOperator]),
            ),
            (
                "job_name",
                "JobName",
                TypeInfo(str),
            ),
            (
                "state",
                "State",
                TypeInfo(typing.Union[str, JobRunState]),
            ),
        ]

    # A logical operator.
    logical_operator: typing.Union[str, "LogicalOperator"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The name of the Job to whose JobRuns this condition applies and on which
    # this trigger waits.
    job_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The condition state. Currently, the values supported are SUCCEEDED,
    # STOPPED, TIMEOUT and FAILED.
    state: typing.Union[str, "JobRunState"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class Connection(ShapeBase):
    """
    Defines a connection to a data source.
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
                "connection_type",
                "ConnectionType",
                TypeInfo(typing.Union[str, ConnectionType]),
            ),
            (
                "match_criteria",
                "MatchCriteria",
                TypeInfo(typing.List[str]),
            ),
            (
                "connection_properties",
                "ConnectionProperties",
                TypeInfo(
                    typing.Dict[typing.Union[str, ConnectionPropertyKey], str]
                ),
            ),
            (
                "physical_connection_requirements",
                "PhysicalConnectionRequirements",
                TypeInfo(PhysicalConnectionRequirements),
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
            (
                "last_updated_by",
                "LastUpdatedBy",
                TypeInfo(str),
            ),
        ]

    # The name of the connection definition.
    name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Description of the connection.
    description: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The type of the connection. Currently, only JDBC is supported; SFTP is not
    # supported.
    connection_type: typing.Union[str, "ConnectionType"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A list of criteria that can be used in selecting this connection.
    match_criteria: typing.List[str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # These key-value pairs define parameters for the connection:

    #   * `HOST` \- The host URI: either the fully qualified domain name (FQDN) or the IPv4 address of the database host.

    #   * `PORT` \- The port number, between 1024 and 65535, of the port on which the database host is listening for database connections.

    #   * `USER_NAME` \- The name under which to log in to the database.

    #   * `PASSWORD` \- A password, if one is used, for the user name.

    #   * `JDBC_DRIVER_JAR_URI` \- The S3 path of the a jar file that contains the JDBC driver to use.

    #   * `JDBC_DRIVER_CLASS_NAME` \- The class name of the JDBC driver to use.

    #   * `JDBC_ENGINE` \- The name of the JDBC engine to use.

    #   * `JDBC_ENGINE_VERSION` \- The version of the JDBC engine to use.

    #   * `CONFIG_FILES` \- (Reserved for future use).

    #   * `INSTANCE_ID` \- The instance ID to use.

    #   * `JDBC_CONNECTION_URL` \- The URL for the JDBC connection.

    #   * `JDBC_ENFORCE_SSL` \- A Boolean string (true, false) specifying whether SSL with hostname matching will be enforced for the JDBC connection on the client. The default is false.
    connection_properties: typing.Dict[
        typing.Union[str, "ConnectionPropertyKey"], str] = dataclasses.field(
            default=ShapeBase.NOT_SET,
        )

    # A map of physical connection requirements, such as VPC and SecurityGroup,
    # needed for making this connection successfully.
    physical_connection_requirements: "PhysicalConnectionRequirements" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The time this connection definition was created.
    creation_time: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The last time this connection definition was updated.
    last_updated_time: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The user, group or role that last updated this connection definition.
    last_updated_by: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ConnectionInput(ShapeBase):
    """
    A structure used to specify a connection to create or update.
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
                "connection_type",
                "ConnectionType",
                TypeInfo(typing.Union[str, ConnectionType]),
            ),
            (
                "connection_properties",
                "ConnectionProperties",
                TypeInfo(
                    typing.Dict[typing.Union[str, ConnectionPropertyKey], str]
                ),
            ),
            (
                "description",
                "Description",
                TypeInfo(str),
            ),
            (
                "match_criteria",
                "MatchCriteria",
                TypeInfo(typing.List[str]),
            ),
            (
                "physical_connection_requirements",
                "PhysicalConnectionRequirements",
                TypeInfo(PhysicalConnectionRequirements),
            ),
        ]

    # The name of the connection.
    name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The type of the connection. Currently, only JDBC is supported; SFTP is not
    # supported.
    connection_type: typing.Union[str, "ConnectionType"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # These key-value pairs define parameters for the connection.
    connection_properties: typing.Dict[
        typing.Union[str, "ConnectionPropertyKey"], str] = dataclasses.field(
            default=ShapeBase.NOT_SET,
        )

    # Description of the connection.
    description: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A list of criteria that can be used in selecting this connection.
    match_criteria: typing.List[str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A map of physical connection requirements, such as VPC and SecurityGroup,
    # needed for making this connection successfully.
    physical_connection_requirements: "PhysicalConnectionRequirements" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


class ConnectionPropertyKey(str):
    HOST = "HOST"
    PORT = "PORT"
    USERNAME = "USERNAME"
    PASSWORD = "PASSWORD"
    JDBC_DRIVER_JAR_URI = "JDBC_DRIVER_JAR_URI"
    JDBC_DRIVER_CLASS_NAME = "JDBC_DRIVER_CLASS_NAME"
    JDBC_ENGINE = "JDBC_ENGINE"
    JDBC_ENGINE_VERSION = "JDBC_ENGINE_VERSION"
    CONFIG_FILES = "CONFIG_FILES"
    INSTANCE_ID = "INSTANCE_ID"
    JDBC_CONNECTION_URL = "JDBC_CONNECTION_URL"
    JDBC_ENFORCE_SSL = "JDBC_ENFORCE_SSL"


class ConnectionType(str):
    JDBC = "JDBC"
    SFTP = "SFTP"


@dataclasses.dataclass
class ConnectionsList(ShapeBase):
    """
    Specifies the connections used by a job.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "connections",
                "Connections",
                TypeInfo(typing.List[str]),
            ),
        ]

    # A list of connections used by the job.
    connections: typing.List[str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class Crawler(ShapeBase):
    """
    Specifies a crawler program that examines a data source and uses classifiers to
    try to determine its schema. If successful, the crawler records metadata
    concerning the data source in the AWS Glue Data Catalog.
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
                "role",
                "Role",
                TypeInfo(str),
            ),
            (
                "targets",
                "Targets",
                TypeInfo(CrawlerTargets),
            ),
            (
                "database_name",
                "DatabaseName",
                TypeInfo(str),
            ),
            (
                "description",
                "Description",
                TypeInfo(str),
            ),
            (
                "classifiers",
                "Classifiers",
                TypeInfo(typing.List[str]),
            ),
            (
                "schema_change_policy",
                "SchemaChangePolicy",
                TypeInfo(SchemaChangePolicy),
            ),
            (
                "state",
                "State",
                TypeInfo(typing.Union[str, CrawlerState]),
            ),
            (
                "table_prefix",
                "TablePrefix",
                TypeInfo(str),
            ),
            (
                "schedule",
                "Schedule",
                TypeInfo(Schedule),
            ),
            (
                "crawl_elapsed_time",
                "CrawlElapsedTime",
                TypeInfo(int),
            ),
            (
                "creation_time",
                "CreationTime",
                TypeInfo(datetime.datetime),
            ),
            (
                "last_updated",
                "LastUpdated",
                TypeInfo(datetime.datetime),
            ),
            (
                "last_crawl",
                "LastCrawl",
                TypeInfo(LastCrawlInfo),
            ),
            (
                "version",
                "Version",
                TypeInfo(int),
            ),
            (
                "configuration",
                "Configuration",
                TypeInfo(str),
            ),
            (
                "crawler_security_configuration",
                "CrawlerSecurityConfiguration",
                TypeInfo(str),
            ),
        ]

    # The crawler name.
    name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The IAM role (or ARN of an IAM role) used to access customer resources,
    # such as data in Amazon S3.
    role: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A collection of targets to crawl.
    targets: "CrawlerTargets" = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The database where metadata is written by this crawler.
    database_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A description of the crawler.
    description: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A list of custom classifiers associated with the crawler.
    classifiers: typing.List[str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Sets the behavior when the crawler finds a changed or deleted object.
    schema_change_policy: "SchemaChangePolicy" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Indicates whether the crawler is running, or whether a run is pending.
    state: typing.Union[str, "CrawlerState"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The prefix added to the names of tables that are created.
    table_prefix: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # For scheduled crawlers, the schedule when the crawler runs.
    schedule: "Schedule" = dataclasses.field(default=ShapeBase.NOT_SET, )

    # If the crawler is running, contains the total time elapsed since the last
    # crawl began.
    crawl_elapsed_time: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The time when the crawler was created.
    creation_time: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The time the crawler was last updated.
    last_updated: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The status of the last crawl, and potentially error information if an error
    # occurred.
    last_crawl: "LastCrawlInfo" = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The version of the crawler.
    version: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Crawler configuration information. This versioned JSON string allows users
    # to specify aspects of a Crawler's behavior.

    # You can use this field to force partitions to inherit metadata such as
    # classification, input format, output format, serde information, and schema
    # from their parent table, rather than detect this information separately for
    # each partition. Use the following JSON string to specify that behavior:

    # Example: `'{ "Version": 1.0, "CrawlerOutput": { "Partitions": {
    # "AddOrUpdateBehavior": "InheritFromTable" } } }'`
    configuration: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The name of the SecurityConfiguration structure to be used by this Crawler.
    crawler_security_configuration: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class CrawlerMetrics(ShapeBase):
    """
    Metrics for a specified crawler.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "crawler_name",
                "CrawlerName",
                TypeInfo(str),
            ),
            (
                "time_left_seconds",
                "TimeLeftSeconds",
                TypeInfo(float),
            ),
            (
                "still_estimating",
                "StillEstimating",
                TypeInfo(bool),
            ),
            (
                "last_runtime_seconds",
                "LastRuntimeSeconds",
                TypeInfo(float),
            ),
            (
                "median_runtime_seconds",
                "MedianRuntimeSeconds",
                TypeInfo(float),
            ),
            (
                "tables_created",
                "TablesCreated",
                TypeInfo(int),
            ),
            (
                "tables_updated",
                "TablesUpdated",
                TypeInfo(int),
            ),
            (
                "tables_deleted",
                "TablesDeleted",
                TypeInfo(int),
            ),
        ]

    # The name of the crawler.
    crawler_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The estimated time left to complete a running crawl.
    time_left_seconds: float = dataclasses.field(default=ShapeBase.NOT_SET, )

    # True if the crawler is still estimating how long it will take to complete
    # this run.
    still_estimating: bool = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The duration of the crawler's most recent run, in seconds.
    last_runtime_seconds: float = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The median duration of this crawler's runs, in seconds.
    median_runtime_seconds: float = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The number of tables created by this crawler.
    tables_created: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The number of tables updated by this crawler.
    tables_updated: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The number of tables deleted by this crawler.
    tables_deleted: int = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class CrawlerNotRunningException(ShapeBase):
    """
    The specified crawler is not running.
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

    # A message describing the problem.
    message: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class CrawlerRunningException(ShapeBase):
    """
    The operation cannot be performed because the crawler is already running.
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

    # A message describing the problem.
    message: str = dataclasses.field(default=ShapeBase.NOT_SET, )


class CrawlerState(str):
    READY = "READY"
    RUNNING = "RUNNING"
    STOPPING = "STOPPING"


@dataclasses.dataclass
class CrawlerStoppingException(ShapeBase):
    """
    The specified crawler is stopping.
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

    # A message describing the problem.
    message: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class CrawlerTargets(ShapeBase):
    """
    Specifies data stores to crawl.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "s3_targets",
                "S3Targets",
                TypeInfo(typing.List[S3Target]),
            ),
            (
                "jdbc_targets",
                "JdbcTargets",
                TypeInfo(typing.List[JdbcTarget]),
            ),
            (
                "dynamo_db_targets",
                "DynamoDBTargets",
                TypeInfo(typing.List[DynamoDBTarget]),
            ),
        ]

    # Specifies Amazon S3 targets.
    s3_targets: typing.List["S3Target"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Specifies JDBC targets.
    jdbc_targets: typing.List["JdbcTarget"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Specifies DynamoDB targets.
    dynamo_db_targets: typing.List["DynamoDBTarget"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class CreateClassifierRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "grok_classifier",
                "GrokClassifier",
                TypeInfo(CreateGrokClassifierRequest),
            ),
            (
                "xml_classifier",
                "XMLClassifier",
                TypeInfo(CreateXMLClassifierRequest),
            ),
            (
                "json_classifier",
                "JsonClassifier",
                TypeInfo(CreateJsonClassifierRequest),
            ),
        ]

    # A `GrokClassifier` object specifying the classifier to create.
    grok_classifier: "CreateGrokClassifierRequest" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # An `XMLClassifier` object specifying the classifier to create.
    xml_classifier: "CreateXMLClassifierRequest" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A `JsonClassifier` object specifying the classifier to create.
    json_classifier: "CreateJsonClassifierRequest" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class CreateClassifierResponse(OutputShapeBase):
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
class CreateConnectionRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "connection_input",
                "ConnectionInput",
                TypeInfo(ConnectionInput),
            ),
            (
                "catalog_id",
                "CatalogId",
                TypeInfo(str),
            ),
        ]

    # A `ConnectionInput` object defining the connection to create.
    connection_input: "ConnectionInput" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The ID of the Data Catalog in which to create the connection. If none is
    # supplied, the AWS account ID is used by default.
    catalog_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class CreateConnectionResponse(OutputShapeBase):
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
class CreateCrawlerRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "name",
                "Name",
                TypeInfo(str),
            ),
            (
                "role",
                "Role",
                TypeInfo(str),
            ),
            (
                "database_name",
                "DatabaseName",
                TypeInfo(str),
            ),
            (
                "targets",
                "Targets",
                TypeInfo(CrawlerTargets),
            ),
            (
                "description",
                "Description",
                TypeInfo(str),
            ),
            (
                "schedule",
                "Schedule",
                TypeInfo(str),
            ),
            (
                "classifiers",
                "Classifiers",
                TypeInfo(typing.List[str]),
            ),
            (
                "table_prefix",
                "TablePrefix",
                TypeInfo(str),
            ),
            (
                "schema_change_policy",
                "SchemaChangePolicy",
                TypeInfo(SchemaChangePolicy),
            ),
            (
                "configuration",
                "Configuration",
                TypeInfo(str),
            ),
            (
                "crawler_security_configuration",
                "CrawlerSecurityConfiguration",
                TypeInfo(str),
            ),
        ]

    # Name of the new crawler.
    name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The IAM role (or ARN of an IAM role) used by the new crawler to access
    # customer resources.
    role: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The AWS Glue database where results are written, such as:
    # `arn:aws:daylight:us-east-1::database/sometable/*`.
    database_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A list of collection of targets to crawl.
    targets: "CrawlerTargets" = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A description of the new crawler.
    description: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A `cron` expression used to specify the schedule (see [Time-Based Schedules
    # for Jobs and Crawlers](http://docs.aws.amazon.com/glue/latest/dg/monitor-
    # data-warehouse-schedule.html). For example, to run something every day at
    # 12:15 UTC, you would specify: `cron(15 12 * * ? *)`.
    schedule: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A list of custom classifiers that the user has registered. By default, all
    # built-in classifiers are included in a crawl, but these custom classifiers
    # always override the default classifiers for a given classification.
    classifiers: typing.List[str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The table prefix used for catalog tables that are created.
    table_prefix: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Policy for the crawler's update and deletion behavior.
    schema_change_policy: "SchemaChangePolicy" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Crawler configuration information. This versioned JSON string allows users
    # to specify aspects of a Crawler's behavior.

    # You can use this field to force partitions to inherit metadata such as
    # classification, input format, output format, serde information, and schema
    # from their parent table, rather than detect this information separately for
    # each partition. Use the following JSON string to specify that behavior:

    # Example: `'{ "Version": 1.0, "CrawlerOutput": { "Partitions": {
    # "AddOrUpdateBehavior": "InheritFromTable" } } }'`
    configuration: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The name of the SecurityConfiguration structure to be used by this Crawler.
    crawler_security_configuration: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class CreateCrawlerResponse(OutputShapeBase):
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
class CreateDatabaseRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "database_input",
                "DatabaseInput",
                TypeInfo(DatabaseInput),
            ),
            (
                "catalog_id",
                "CatalogId",
                TypeInfo(str),
            ),
        ]

    # A `DatabaseInput` object defining the metadata database to create in the
    # catalog.
    database_input: "DatabaseInput" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The ID of the Data Catalog in which to create the database. If none is
    # supplied, the AWS account ID is used by default.
    catalog_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class CreateDatabaseResponse(OutputShapeBase):
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
class CreateDevEndpointRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "endpoint_name",
                "EndpointName",
                TypeInfo(str),
            ),
            (
                "role_arn",
                "RoleArn",
                TypeInfo(str),
            ),
            (
                "security_group_ids",
                "SecurityGroupIds",
                TypeInfo(typing.List[str]),
            ),
            (
                "subnet_id",
                "SubnetId",
                TypeInfo(str),
            ),
            (
                "public_key",
                "PublicKey",
                TypeInfo(str),
            ),
            (
                "public_keys",
                "PublicKeys",
                TypeInfo(typing.List[str]),
            ),
            (
                "number_of_nodes",
                "NumberOfNodes",
                TypeInfo(int),
            ),
            (
                "extra_python_libs_s3_path",
                "ExtraPythonLibsS3Path",
                TypeInfo(str),
            ),
            (
                "extra_jars_s3_path",
                "ExtraJarsS3Path",
                TypeInfo(str),
            ),
            (
                "security_configuration",
                "SecurityConfiguration",
                TypeInfo(str),
            ),
        ]

    # The name to be assigned to the new DevEndpoint.
    endpoint_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The IAM role for the DevEndpoint.
    role_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Security group IDs for the security groups to be used by the new
    # DevEndpoint.
    security_group_ids: typing.List[str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The subnet ID for the new DevEndpoint to use.
    subnet_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The public key to be used by this DevEndpoint for authentication. This
    # attribute is provided for backward compatibility, as the recommended
    # attribute to use is public keys.
    public_key: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A list of public keys to be used by the DevEndpoints for authentication.
    # The use of this attribute is preferred over a single public key because the
    # public keys allow you to have a different private key per client.

    # If you previously created an endpoint with a public key, you must remove
    # that key to be able to set a list of public keys: call the
    # `UpdateDevEndpoint` API with the public key content in the
    # `deletePublicKeys` attribute, and the list of new keys in the
    # `addPublicKeys` attribute.
    public_keys: typing.List[str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The number of AWS Glue Data Processing Units (DPUs) to allocate to this
    # DevEndpoint.
    number_of_nodes: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Path(s) to one or more Python libraries in an S3 bucket that should be
    # loaded in your DevEndpoint. Multiple values must be complete paths
    # separated by a comma.

    # Please note that only pure Python libraries can currently be used on a
    # DevEndpoint. Libraries that rely on C extensions, such as the
    # [pandas](http://pandas.pydata.org/) Python data analysis library, are not
    # yet supported.
    extra_python_libs_s3_path: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Path to one or more Java Jars in an S3 bucket that should be loaded in your
    # DevEndpoint.
    extra_jars_s3_path: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The name of the SecurityConfiguration structure to be used with this
    # DevEndpoint.
    security_configuration: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class CreateDevEndpointResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "endpoint_name",
                "EndpointName",
                TypeInfo(str),
            ),
            (
                "status",
                "Status",
                TypeInfo(str),
            ),
            (
                "security_group_ids",
                "SecurityGroupIds",
                TypeInfo(typing.List[str]),
            ),
            (
                "subnet_id",
                "SubnetId",
                TypeInfo(str),
            ),
            (
                "role_arn",
                "RoleArn",
                TypeInfo(str),
            ),
            (
                "yarn_endpoint_address",
                "YarnEndpointAddress",
                TypeInfo(str),
            ),
            (
                "zeppelin_remote_spark_interpreter_port",
                "ZeppelinRemoteSparkInterpreterPort",
                TypeInfo(int),
            ),
            (
                "number_of_nodes",
                "NumberOfNodes",
                TypeInfo(int),
            ),
            (
                "availability_zone",
                "AvailabilityZone",
                TypeInfo(str),
            ),
            (
                "vpc_id",
                "VpcId",
                TypeInfo(str),
            ),
            (
                "extra_python_libs_s3_path",
                "ExtraPythonLibsS3Path",
                TypeInfo(str),
            ),
            (
                "extra_jars_s3_path",
                "ExtraJarsS3Path",
                TypeInfo(str),
            ),
            (
                "failure_reason",
                "FailureReason",
                TypeInfo(str),
            ),
            (
                "security_configuration",
                "SecurityConfiguration",
                TypeInfo(str),
            ),
            (
                "created_timestamp",
                "CreatedTimestamp",
                TypeInfo(datetime.datetime),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The name assigned to the new DevEndpoint.
    endpoint_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The current status of the new DevEndpoint.
    status: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The security groups assigned to the new DevEndpoint.
    security_group_ids: typing.List[str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The subnet ID assigned to the new DevEndpoint.
    subnet_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The AWS ARN of the role assigned to the new DevEndpoint.
    role_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The address of the YARN endpoint used by this DevEndpoint.
    yarn_endpoint_address: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The Apache Zeppelin port for the remote Apache Spark interpreter.
    zeppelin_remote_spark_interpreter_port: int = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The number of AWS Glue Data Processing Units (DPUs) allocated to this
    # DevEndpoint.
    number_of_nodes: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The AWS availability zone where this DevEndpoint is located.
    availability_zone: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The ID of the VPC used by this DevEndpoint.
    vpc_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Path(s) to one or more Python libraries in an S3 bucket that will be loaded
    # in your DevEndpoint.
    extra_python_libs_s3_path: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Path to one or more Java Jars in an S3 bucket that will be loaded in your
    # DevEndpoint.
    extra_jars_s3_path: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The reason for a current failure in this DevEndpoint.
    failure_reason: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The name of the SecurityConfiguration structure being used with this
    # DevEndpoint.
    security_configuration: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The point in time at which this DevEndpoint was created.
    created_timestamp: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class CreateGrokClassifierRequest(ShapeBase):
    """
    Specifies a `grok` classifier for `CreateClassifier` to create.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "classification",
                "Classification",
                TypeInfo(str),
            ),
            (
                "name",
                "Name",
                TypeInfo(str),
            ),
            (
                "grok_pattern",
                "GrokPattern",
                TypeInfo(str),
            ),
            (
                "custom_patterns",
                "CustomPatterns",
                TypeInfo(str),
            ),
        ]

    # An identifier of the data format that the classifier matches, such as
    # Twitter, JSON, Omniture logs, Amazon CloudWatch Logs, and so on.
    classification: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The name of the new classifier.
    name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The grok pattern used by this classifier.
    grok_pattern: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Optional custom grok patterns used by this classifier.
    custom_patterns: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class CreateJobRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "name",
                "Name",
                TypeInfo(str),
            ),
            (
                "role",
                "Role",
                TypeInfo(str),
            ),
            (
                "command",
                "Command",
                TypeInfo(JobCommand),
            ),
            (
                "description",
                "Description",
                TypeInfo(str),
            ),
            (
                "log_uri",
                "LogUri",
                TypeInfo(str),
            ),
            (
                "execution_property",
                "ExecutionProperty",
                TypeInfo(ExecutionProperty),
            ),
            (
                "default_arguments",
                "DefaultArguments",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "connections",
                "Connections",
                TypeInfo(ConnectionsList),
            ),
            (
                "max_retries",
                "MaxRetries",
                TypeInfo(int),
            ),
            (
                "allocated_capacity",
                "AllocatedCapacity",
                TypeInfo(int),
            ),
            (
                "timeout",
                "Timeout",
                TypeInfo(int),
            ),
            (
                "notification_property",
                "NotificationProperty",
                TypeInfo(NotificationProperty),
            ),
            (
                "security_configuration",
                "SecurityConfiguration",
                TypeInfo(str),
            ),
        ]

    # The name you assign to this job definition. It must be unique in your
    # account.
    name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The name or ARN of the IAM role associated with this job.
    role: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The JobCommand that executes this job.
    command: "JobCommand" = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Description of the job being defined.
    description: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # This field is reserved for future use.
    log_uri: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # An ExecutionProperty specifying the maximum number of concurrent runs
    # allowed for this job.
    execution_property: "ExecutionProperty" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The default arguments for this job.

    # You can specify arguments here that your own job-execution script consumes,
    # as well as arguments that AWS Glue itself consumes.

    # For information about how to specify and consume your own Job arguments,
    # see the [Calling AWS Glue APIs in
    # Python](http://docs.aws.amazon.com/glue/latest/dg/aws-glue-programming-
    # python-calling.html) topic in the developer guide.

    # For information about the key-value pairs that AWS Glue consumes to set up
    # your job, see the [Special Parameters Used by AWS
    # Glue](http://docs.aws.amazon.com/glue/latest/dg/aws-glue-programming-etl-
    # glue-arguments.html) topic in the developer guide.
    default_arguments: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The connections used for this job.
    connections: "ConnectionsList" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The maximum number of times to retry this job if it fails.
    max_retries: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The number of AWS Glue data processing units (DPUs) to allocate to this
    # Job. From 2 to 100 DPUs can be allocated; the default is 10. A DPU is a
    # relative measure of processing power that consists of 4 vCPUs of compute
    # capacity and 16 GB of memory. For more information, see the [AWS Glue
    # pricing page](https://aws.amazon.com/glue/pricing/).
    allocated_capacity: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The job timeout in minutes. This is the maximum time that a job run can
    # consume resources before it is terminated and enters `TIMEOUT` status. The
    # default is 2,880 minutes (48 hours).
    timeout: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Specifies configuration properties of a job notification.
    notification_property: "NotificationProperty" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The name of the SecurityConfiguration structure to be used with this job.
    security_configuration: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class CreateJobResponse(OutputShapeBase):
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

    # The unique name that was provided for this job definition.
    name: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class CreateJsonClassifierRequest(ShapeBase):
    """
    Specifies a JSON classifier for `CreateClassifier` to create.
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
                "json_path",
                "JsonPath",
                TypeInfo(str),
            ),
        ]

    # The name of the classifier.
    name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A `JsonPath` string defining the JSON data for the classifier to classify.
    # AWS Glue supports a subset of JsonPath, as described in [Writing JsonPath
    # Custom Classifiers](https://docs.aws.amazon.com/glue/latest/dg/custom-
    # classifier.html#custom-classifier-json).
    json_path: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class CreatePartitionRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "database_name",
                "DatabaseName",
                TypeInfo(str),
            ),
            (
                "table_name",
                "TableName",
                TypeInfo(str),
            ),
            (
                "partition_input",
                "PartitionInput",
                TypeInfo(PartitionInput),
            ),
            (
                "catalog_id",
                "CatalogId",
                TypeInfo(str),
            ),
        ]

    # The name of the metadata database in which the partition is to be created.
    database_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The name of the metadata table in which the partition is to be created.
    table_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A `PartitionInput` structure defining the partition to be created.
    partition_input: "PartitionInput" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The ID of the catalog in which the partion is to be created. Currently,
    # this should be the AWS account ID.
    catalog_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class CreatePartitionResponse(OutputShapeBase):
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
class CreateScriptRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "dag_nodes",
                "DagNodes",
                TypeInfo(typing.List[CodeGenNode]),
            ),
            (
                "dag_edges",
                "DagEdges",
                TypeInfo(typing.List[CodeGenEdge]),
            ),
            (
                "language",
                "Language",
                TypeInfo(typing.Union[str, Language]),
            ),
        ]

    # A list of the nodes in the DAG.
    dag_nodes: typing.List["CodeGenNode"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A list of the edges in the DAG.
    dag_edges: typing.List["CodeGenEdge"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The programming language of the resulting code from the DAG.
    language: typing.Union[str, "Language"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class CreateScriptResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "python_script",
                "PythonScript",
                TypeInfo(str),
            ),
            (
                "scala_code",
                "ScalaCode",
                TypeInfo(str),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The Python script generated from the DAG.
    python_script: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The Scala code generated from the DAG.
    scala_code: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class CreateSecurityConfigurationRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "name",
                "Name",
                TypeInfo(str),
            ),
            (
                "encryption_configuration",
                "EncryptionConfiguration",
                TypeInfo(EncryptionConfiguration),
            ),
        ]

    # The name for the new security configuration.
    name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The encryption configuration for the new security configuration.
    encryption_configuration: "EncryptionConfiguration" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class CreateSecurityConfigurationResponse(OutputShapeBase):
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
                "created_timestamp",
                "CreatedTimestamp",
                TypeInfo(datetime.datetime),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The name assigned to the new security configuration.
    name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The time at which the new security configuration was created.
    created_timestamp: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class CreateTableRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "database_name",
                "DatabaseName",
                TypeInfo(str),
            ),
            (
                "table_input",
                "TableInput",
                TypeInfo(TableInput),
            ),
            (
                "catalog_id",
                "CatalogId",
                TypeInfo(str),
            ),
        ]

    # The catalog database in which to create the new table. For Hive
    # compatibility, this name is entirely lowercase.
    database_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The `TableInput` object that defines the metadata table to create in the
    # catalog.
    table_input: "TableInput" = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The ID of the Data Catalog in which to create the `Table`. If none is
    # supplied, the AWS account ID is used by default.
    catalog_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class CreateTableResponse(OutputShapeBase):
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
class CreateTriggerRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "name",
                "Name",
                TypeInfo(str),
            ),
            (
                "type",
                "Type",
                TypeInfo(typing.Union[str, TriggerType]),
            ),
            (
                "actions",
                "Actions",
                TypeInfo(typing.List[Action]),
            ),
            (
                "schedule",
                "Schedule",
                TypeInfo(str),
            ),
            (
                "predicate",
                "Predicate",
                TypeInfo(Predicate),
            ),
            (
                "description",
                "Description",
                TypeInfo(str),
            ),
            (
                "start_on_creation",
                "StartOnCreation",
                TypeInfo(bool),
            ),
        ]

    # The name of the trigger.
    name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The type of the new trigger.
    type: typing.Union[str, "TriggerType"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The actions initiated by this trigger when it fires.
    actions: typing.List["Action"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A `cron` expression used to specify the schedule (see [Time-Based Schedules
    # for Jobs and Crawlers](http://docs.aws.amazon.com/glue/latest/dg/monitor-
    # data-warehouse-schedule.html). For example, to run something every day at
    # 12:15 UTC, you would specify: `cron(15 12 * * ? *)`.

    # This field is required when the trigger type is SCHEDULED.
    schedule: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A predicate to specify when the new trigger should fire.

    # This field is required when the trigger type is CONDITIONAL.
    predicate: "Predicate" = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A description of the new trigger.
    description: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Set to true to start SCHEDULED and CONDITIONAL triggers when created. True
    # not supported for ON_DEMAND triggers.
    start_on_creation: bool = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class CreateTriggerResponse(OutputShapeBase):
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

    # The name of the trigger.
    name: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class CreateUserDefinedFunctionRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "database_name",
                "DatabaseName",
                TypeInfo(str),
            ),
            (
                "function_input",
                "FunctionInput",
                TypeInfo(UserDefinedFunctionInput),
            ),
            (
                "catalog_id",
                "CatalogId",
                TypeInfo(str),
            ),
        ]

    # The name of the catalog database in which to create the function.
    database_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A `FunctionInput` object that defines the function to create in the Data
    # Catalog.
    function_input: "UserDefinedFunctionInput" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The ID of the Data Catalog in which to create the function. If none is
    # supplied, the AWS account ID is used by default.
    catalog_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class CreateUserDefinedFunctionResponse(OutputShapeBase):
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
class CreateXMLClassifierRequest(ShapeBase):
    """
    Specifies an XML classifier for `CreateClassifier` to create.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "classification",
                "Classification",
                TypeInfo(str),
            ),
            (
                "name",
                "Name",
                TypeInfo(str),
            ),
            (
                "row_tag",
                "RowTag",
                TypeInfo(str),
            ),
        ]

    # An identifier of the data format that the classifier matches.
    classification: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The name of the classifier.
    name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The XML tag designating the element that contains each record in an XML
    # document being parsed. Note that this cannot identify a self-closing
    # element (closed by `/>`). An empty row element that contains only
    # attributes can be parsed as long as it ends with a closing tag (for
    # example, `<row item_a="A" item_b="B"></row>` is okay, but `<row item_a="A"
    # item_b="B" />` is not).
    row_tag: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DataCatalogEncryptionSettings(ShapeBase):
    """
    Contains configuration information for maintaining Data Catalog security.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "encryption_at_rest",
                "EncryptionAtRest",
                TypeInfo(EncryptionAtRest),
            ),
        ]

    # Specifies encryption-at-rest configuration for the Data Catalog.
    encryption_at_rest: "EncryptionAtRest" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class Database(ShapeBase):
    """
    The `Database` object represents a logical grouping of tables that may reside in
    a Hive metastore or an RDBMS.
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
                "location_uri",
                "LocationUri",
                TypeInfo(str),
            ),
            (
                "parameters",
                "Parameters",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "create_time",
                "CreateTime",
                TypeInfo(datetime.datetime),
            ),
        ]

    # Name of the database. For Hive compatibility, this is folded to lowercase
    # when it is stored.
    name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Description of the database.
    description: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The location of the database (for example, an HDFS path).
    location_uri: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # These key-value pairs define parameters and properties of the database.
    parameters: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The time at which the metadata database was created in the catalog.
    create_time: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class DatabaseInput(ShapeBase):
    """
    The structure used to create or update a database.
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
                "location_uri",
                "LocationUri",
                TypeInfo(str),
            ),
            (
                "parameters",
                "Parameters",
                TypeInfo(typing.Dict[str, str]),
            ),
        ]

    # Name of the database. For Hive compatibility, this is folded to lowercase
    # when it is stored.
    name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Description of the database
    description: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The location of the database (for example, an HDFS path).
    location_uri: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Thes key-value pairs define parameters and properties of the database.
    parameters: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


class DeleteBehavior(str):
    LOG = "LOG"
    DELETE_FROM_DATABASE = "DELETE_FROM_DATABASE"
    DEPRECATE_IN_DATABASE = "DEPRECATE_IN_DATABASE"


@dataclasses.dataclass
class DeleteClassifierRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "name",
                "Name",
                TypeInfo(str),
            ),
        ]

    # Name of the classifier to remove.
    name: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DeleteClassifierResponse(OutputShapeBase):
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
class DeleteConnectionRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "connection_name",
                "ConnectionName",
                TypeInfo(str),
            ),
            (
                "catalog_id",
                "CatalogId",
                TypeInfo(str),
            ),
        ]

    # The name of the connection to delete.
    connection_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The ID of the Data Catalog in which the connection resides. If none is
    # supplied, the AWS account ID is used by default.
    catalog_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DeleteConnectionResponse(OutputShapeBase):
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
class DeleteCrawlerRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "name",
                "Name",
                TypeInfo(str),
            ),
        ]

    # Name of the crawler to remove.
    name: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DeleteCrawlerResponse(OutputShapeBase):
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
class DeleteDatabaseRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "name",
                "Name",
                TypeInfo(str),
            ),
            (
                "catalog_id",
                "CatalogId",
                TypeInfo(str),
            ),
        ]

    # The name of the Database to delete. For Hive compatibility, this must be
    # all lowercase.
    name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The ID of the Data Catalog in which the database resides. If none is
    # supplied, the AWS account ID is used by default.
    catalog_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DeleteDatabaseResponse(OutputShapeBase):
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
class DeleteDevEndpointRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "endpoint_name",
                "EndpointName",
                TypeInfo(str),
            ),
        ]

    # The name of the DevEndpoint.
    endpoint_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DeleteDevEndpointResponse(OutputShapeBase):
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
class DeleteJobRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "job_name",
                "JobName",
                TypeInfo(str),
            ),
        ]

    # The name of the job definition to delete.
    job_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DeleteJobResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "job_name",
                "JobName",
                TypeInfo(str),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The name of the job definition that was deleted.
    job_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DeletePartitionRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "database_name",
                "DatabaseName",
                TypeInfo(str),
            ),
            (
                "table_name",
                "TableName",
                TypeInfo(str),
            ),
            (
                "partition_values",
                "PartitionValues",
                TypeInfo(typing.List[str]),
            ),
            (
                "catalog_id",
                "CatalogId",
                TypeInfo(str),
            ),
        ]

    # The name of the catalog database in which the table in question resides.
    database_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The name of the table where the partition to be deleted is located.
    table_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The values that define the partition.
    partition_values: typing.List[str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The ID of the Data Catalog where the partition to be deleted resides. If
    # none is supplied, the AWS account ID is used by default.
    catalog_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DeletePartitionResponse(OutputShapeBase):
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
class DeleteSecurityConfigurationRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "name",
                "Name",
                TypeInfo(str),
            ),
        ]

    # The name of the security configuration to delete.
    name: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DeleteSecurityConfigurationResponse(OutputShapeBase):
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
class DeleteTableRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "database_name",
                "DatabaseName",
                TypeInfo(str),
            ),
            (
                "name",
                "Name",
                TypeInfo(str),
            ),
            (
                "catalog_id",
                "CatalogId",
                TypeInfo(str),
            ),
        ]

    # The name of the catalog database in which the table resides. For Hive
    # compatibility, this name is entirely lowercase.
    database_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The name of the table to be deleted. For Hive compatibility, this name is
    # entirely lowercase.
    name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The ID of the Data Catalog where the table resides. If none is supplied,
    # the AWS account ID is used by default.
    catalog_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DeleteTableResponse(OutputShapeBase):
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
class DeleteTableVersionRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "database_name",
                "DatabaseName",
                TypeInfo(str),
            ),
            (
                "table_name",
                "TableName",
                TypeInfo(str),
            ),
            (
                "version_id",
                "VersionId",
                TypeInfo(str),
            ),
            (
                "catalog_id",
                "CatalogId",
                TypeInfo(str),
            ),
        ]

    # The database in the catalog in which the table resides. For Hive
    # compatibility, this name is entirely lowercase.
    database_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The name of the table. For Hive compatibility, this name is entirely
    # lowercase.
    table_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The ID of the table version to be deleted.
    version_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The ID of the Data Catalog where the tables reside. If none is supplied,
    # the AWS account ID is used by default.
    catalog_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DeleteTableVersionResponse(OutputShapeBase):
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
class DeleteTriggerRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "name",
                "Name",
                TypeInfo(str),
            ),
        ]

    # The name of the trigger to delete.
    name: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DeleteTriggerResponse(OutputShapeBase):
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

    # The name of the trigger that was deleted.
    name: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DeleteUserDefinedFunctionRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "database_name",
                "DatabaseName",
                TypeInfo(str),
            ),
            (
                "function_name",
                "FunctionName",
                TypeInfo(str),
            ),
            (
                "catalog_id",
                "CatalogId",
                TypeInfo(str),
            ),
        ]

    # The name of the catalog database where the function is located.
    database_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The name of the function definition to be deleted.
    function_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The ID of the Data Catalog where the function to be deleted is located. If
    # none is supplied, the AWS account ID is used by default.
    catalog_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DeleteUserDefinedFunctionResponse(OutputShapeBase):
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
class DevEndpoint(ShapeBase):
    """
    A development endpoint where a developer can remotely debug ETL scripts.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "endpoint_name",
                "EndpointName",
                TypeInfo(str),
            ),
            (
                "role_arn",
                "RoleArn",
                TypeInfo(str),
            ),
            (
                "security_group_ids",
                "SecurityGroupIds",
                TypeInfo(typing.List[str]),
            ),
            (
                "subnet_id",
                "SubnetId",
                TypeInfo(str),
            ),
            (
                "yarn_endpoint_address",
                "YarnEndpointAddress",
                TypeInfo(str),
            ),
            (
                "private_address",
                "PrivateAddress",
                TypeInfo(str),
            ),
            (
                "zeppelin_remote_spark_interpreter_port",
                "ZeppelinRemoteSparkInterpreterPort",
                TypeInfo(int),
            ),
            (
                "public_address",
                "PublicAddress",
                TypeInfo(str),
            ),
            (
                "status",
                "Status",
                TypeInfo(str),
            ),
            (
                "number_of_nodes",
                "NumberOfNodes",
                TypeInfo(int),
            ),
            (
                "availability_zone",
                "AvailabilityZone",
                TypeInfo(str),
            ),
            (
                "vpc_id",
                "VpcId",
                TypeInfo(str),
            ),
            (
                "extra_python_libs_s3_path",
                "ExtraPythonLibsS3Path",
                TypeInfo(str),
            ),
            (
                "extra_jars_s3_path",
                "ExtraJarsS3Path",
                TypeInfo(str),
            ),
            (
                "failure_reason",
                "FailureReason",
                TypeInfo(str),
            ),
            (
                "last_update_status",
                "LastUpdateStatus",
                TypeInfo(str),
            ),
            (
                "created_timestamp",
                "CreatedTimestamp",
                TypeInfo(datetime.datetime),
            ),
            (
                "last_modified_timestamp",
                "LastModifiedTimestamp",
                TypeInfo(datetime.datetime),
            ),
            (
                "public_key",
                "PublicKey",
                TypeInfo(str),
            ),
            (
                "public_keys",
                "PublicKeys",
                TypeInfo(typing.List[str]),
            ),
            (
                "security_configuration",
                "SecurityConfiguration",
                TypeInfo(str),
            ),
        ]

    # The name of the DevEndpoint.
    endpoint_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The AWS ARN of the IAM role used in this DevEndpoint.
    role_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A list of security group identifiers used in this DevEndpoint.
    security_group_ids: typing.List[str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The subnet ID for this DevEndpoint.
    subnet_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The YARN endpoint address used by this DevEndpoint.
    yarn_endpoint_address: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A private DNS to access the DevEndpoint within a VPC, if the DevEndpoint is
    # created within one.
    private_address: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The Apache Zeppelin port for the remote Apache Spark interpreter.
    zeppelin_remote_spark_interpreter_port: int = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The public VPC address used by this DevEndpoint.
    public_address: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The current status of this DevEndpoint.
    status: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The number of AWS Glue Data Processing Units (DPUs) allocated to this
    # DevEndpoint.
    number_of_nodes: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The AWS availability zone where this DevEndpoint is located.
    availability_zone: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The ID of the virtual private cloud (VPC) used by this DevEndpoint.
    vpc_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Path(s) to one or more Python libraries in an S3 bucket that should be
    # loaded in your DevEndpoint. Multiple values must be complete paths
    # separated by a comma.

    # Please note that only pure Python libraries can currently be used on a
    # DevEndpoint. Libraries that rely on C extensions, such as the
    # [pandas](http://pandas.pydata.org/) Python data analysis library, are not
    # yet supported.
    extra_python_libs_s3_path: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Path to one or more Java Jars in an S3 bucket that should be loaded in your
    # DevEndpoint.

    # Please note that only pure Java/Scala libraries can currently be used on a
    # DevEndpoint.
    extra_jars_s3_path: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The reason for a current failure in this DevEndpoint.
    failure_reason: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The status of the last update.
    last_update_status: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The point in time at which this DevEndpoint was created.
    created_timestamp: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The point in time at which this DevEndpoint was last modified.
    last_modified_timestamp: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The public key to be used by this DevEndpoint for authentication. This
    # attribute is provided for backward compatibility, as the recommended
    # attribute to use is public keys.
    public_key: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A list of public keys to be used by the DevEndpoints for authentication.
    # The use of this attribute is preferred over a single public key because the
    # public keys allow you to have a different private key per client.

    # If you previously created an endpoint with a public key, you must remove
    # that key to be able to set a list of public keys: call the
    # `UpdateDevEndpoint` API with the public key content in the
    # `deletePublicKeys` attribute, and the list of new keys in the
    # `addPublicKeys` attribute.
    public_keys: typing.List[str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The name of the SecurityConfiguration structure to be used with this
    # DevEndpoint.
    security_configuration: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DevEndpointCustomLibraries(ShapeBase):
    """
    Custom libraries to be loaded into a DevEndpoint.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "extra_python_libs_s3_path",
                "ExtraPythonLibsS3Path",
                TypeInfo(str),
            ),
            (
                "extra_jars_s3_path",
                "ExtraJarsS3Path",
                TypeInfo(str),
            ),
        ]

    # Path(s) to one or more Python libraries in an S3 bucket that should be
    # loaded in your DevEndpoint. Multiple values must be complete paths
    # separated by a comma.

    # Please note that only pure Python libraries can currently be used on a
    # DevEndpoint. Libraries that rely on C extensions, such as the
    # [pandas](http://pandas.pydata.org/) Python data analysis library, are not
    # yet supported.
    extra_python_libs_s3_path: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Path to one or more Java Jars in an S3 bucket that should be loaded in your
    # DevEndpoint.

    # Please note that only pure Java/Scala libraries can currently be used on a
    # DevEndpoint.
    extra_jars_s3_path: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DynamoDBTarget(ShapeBase):
    """
    Specifies a DynamoDB table to crawl.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "path",
                "Path",
                TypeInfo(str),
            ),
        ]

    # The name of the DynamoDB table to crawl.
    path: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class EncryptionAtRest(ShapeBase):
    """
    Specifies encryption-at-rest configuration for the Data Catalog.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "catalog_encryption_mode",
                "CatalogEncryptionMode",
                TypeInfo(typing.Union[str, CatalogEncryptionMode]),
            ),
            (
                "sse_aws_kms_key_id",
                "SseAwsKmsKeyId",
                TypeInfo(str),
            ),
        ]

    # The encryption-at-rest mode for encrypting Data Catalog data.
    catalog_encryption_mode: typing.Union[str, "CatalogEncryptionMode"
                                         ] = dataclasses.field(
                                             default=ShapeBase.NOT_SET,
                                         )

    # The ID of the AWS KMS key to use for encryption at rest.
    sse_aws_kms_key_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class EncryptionConfiguration(ShapeBase):
    """
    Specifies an encryption configuration.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "s3_encryption",
                "S3Encryption",
                TypeInfo(typing.List[S3Encryption]),
            ),
            (
                "cloud_watch_encryption",
                "CloudWatchEncryption",
                TypeInfo(CloudWatchEncryption),
            ),
            (
                "job_bookmarks_encryption",
                "JobBookmarksEncryption",
                TypeInfo(JobBookmarksEncryption),
            ),
        ]

    # The encryption configuration for S3 data.
    s3_encryption: typing.List["S3Encryption"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The encryption configuration for CloudWatch.
    cloud_watch_encryption: "CloudWatchEncryption" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The encryption configuration for Job Bookmarks.
    job_bookmarks_encryption: "JobBookmarksEncryption" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class EntityNotFoundException(ShapeBase):
    """
    A specified entity does not exist
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

    # A message describing the problem.
    message: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ErrorDetail(ShapeBase):
    """
    Contains details about an error.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
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

    # The code associated with this error.
    error_code: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A message describing the error.
    error_message: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ExecutionProperty(ShapeBase):
    """
    An execution property of a job.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "max_concurrent_runs",
                "MaxConcurrentRuns",
                TypeInfo(int),
            ),
        ]

    # The maximum number of concurrent runs allowed for the job. The default is
    # 1. An error is returned when this threshold is reached. The maximum value
    # you can specify is controlled by a service limit.
    max_concurrent_runs: int = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class GetCatalogImportStatusRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "catalog_id",
                "CatalogId",
                TypeInfo(str),
            ),
        ]

    # The ID of the catalog to migrate. Currently, this should be the AWS account
    # ID.
    catalog_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class GetCatalogImportStatusResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "import_status",
                "ImportStatus",
                TypeInfo(CatalogImportStatus),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The status of the specified catalog migration.
    import_status: "CatalogImportStatus" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class GetClassifierRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "name",
                "Name",
                TypeInfo(str),
            ),
        ]

    # Name of the classifier to retrieve.
    name: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class GetClassifierResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "classifier",
                "Classifier",
                TypeInfo(Classifier),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The requested classifier.
    classifier: "Classifier" = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class GetClassifiersRequest(ShapeBase):
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

    # Size of the list to return (optional).
    max_results: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # An optional continuation token.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class GetClassifiersResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "classifiers",
                "Classifiers",
                TypeInfo(typing.List[Classifier]),
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

    # The requested list of classifier objects.
    classifiers: typing.List["Classifier"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A continuation token.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    def paginate(self,
                ) -> typing.Generator["GetClassifiersResponse", None, None]:
        yield from super()._paginate()


@dataclasses.dataclass
class GetConnectionRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "name",
                "Name",
                TypeInfo(str),
            ),
            (
                "catalog_id",
                "CatalogId",
                TypeInfo(str),
            ),
        ]

    # The name of the connection definition to retrieve.
    name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The ID of the Data Catalog in which the connection resides. If none is
    # supplied, the AWS account ID is used by default.
    catalog_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class GetConnectionResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "connection",
                "Connection",
                TypeInfo(Connection),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The requested connection definition.
    connection: "Connection" = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class GetConnectionsFilter(ShapeBase):
    """
    Filters the connection definitions returned by the `GetConnections` API.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "match_criteria",
                "MatchCriteria",
                TypeInfo(typing.List[str]),
            ),
            (
                "connection_type",
                "ConnectionType",
                TypeInfo(typing.Union[str, ConnectionType]),
            ),
        ]

    # A criteria string that must match the criteria recorded in the connection
    # definition for that connection definition to be returned.
    match_criteria: typing.List[str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The type of connections to return. Currently, only JDBC is supported; SFTP
    # is not supported.
    connection_type: typing.Union[str, "ConnectionType"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class GetConnectionsRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "catalog_id",
                "CatalogId",
                TypeInfo(str),
            ),
            (
                "filter",
                "Filter",
                TypeInfo(GetConnectionsFilter),
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

    # The ID of the Data Catalog in which the connections reside. If none is
    # supplied, the AWS account ID is used by default.
    catalog_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A filter that controls which connections will be returned.
    filter: "GetConnectionsFilter" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A continuation token, if this is a continuation call.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The maximum number of connections to return in one response.
    max_results: int = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class GetConnectionsResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "connection_list",
                "ConnectionList",
                TypeInfo(typing.List[Connection]),
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

    # A list of requested connection definitions.
    connection_list: typing.List["Connection"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A continuation token, if the list of connections returned does not include
    # the last of the filtered connections.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    def paginate(self,
                ) -> typing.Generator["GetConnectionsResponse", None, None]:
        yield from super()._paginate()


@dataclasses.dataclass
class GetCrawlerMetricsRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "crawler_name_list",
                "CrawlerNameList",
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

    # A list of the names of crawlers about which to retrieve metrics.
    crawler_name_list: typing.List[str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The maximum size of a list to return.
    max_results: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A continuation token, if this is a continuation call.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class GetCrawlerMetricsResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "crawler_metrics_list",
                "CrawlerMetricsList",
                TypeInfo(typing.List[CrawlerMetrics]),
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

    # A list of metrics for the specified crawler.
    crawler_metrics_list: typing.List["CrawlerMetrics"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A continuation token, if the returned list does not contain the last metric
    # available.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    def paginate(self,
                ) -> typing.Generator["GetCrawlerMetricsResponse", None, None]:
        yield from super()._paginate()


@dataclasses.dataclass
class GetCrawlerRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "name",
                "Name",
                TypeInfo(str),
            ),
        ]

    # Name of the crawler to retrieve metadata for.
    name: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class GetCrawlerResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "crawler",
                "Crawler",
                TypeInfo(Crawler),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The metadata for the specified crawler.
    crawler: "Crawler" = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class GetCrawlersRequest(ShapeBase):
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

    # The number of crawlers to return on each call.
    max_results: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A continuation token, if this is a continuation request.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class GetCrawlersResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "crawlers",
                "Crawlers",
                TypeInfo(typing.List[Crawler]),
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

    # A list of crawler metadata.
    crawlers: typing.List["Crawler"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A continuation token, if the returned list has not reached the end of those
    # defined in this customer account.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    def paginate(self, ) -> typing.Generator["GetCrawlersResponse", None, None]:
        yield from super()._paginate()


@dataclasses.dataclass
class GetDatabaseRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "name",
                "Name",
                TypeInfo(str),
            ),
            (
                "catalog_id",
                "CatalogId",
                TypeInfo(str),
            ),
        ]

    # The name of the database to retrieve. For Hive compatibility, this should
    # be all lowercase.
    name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The ID of the Data Catalog in which the database resides. If none is
    # supplied, the AWS account ID is used by default.
    catalog_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class GetDatabaseResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "database",
                "Database",
                TypeInfo(Database),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The definition of the specified database in the catalog.
    database: "Database" = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class GetDatabasesRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "catalog_id",
                "CatalogId",
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

    # The ID of the Data Catalog from which to retrieve `Databases`. If none is
    # supplied, the AWS account ID is used by default.
    catalog_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A continuation token, if this is a continuation call.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The maximum number of databases to return in one response.
    max_results: int = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class GetDatabasesResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "database_list",
                "DatabaseList",
                TypeInfo(typing.List[Database]),
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

    # A list of `Database` objects from the specified catalog.
    database_list: typing.List["Database"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A continuation token for paginating the returned list of tokens, returned
    # if the current segment of the list is not the last.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    def paginate(self,
                ) -> typing.Generator["GetDatabasesResponse", None, None]:
        yield from super()._paginate()


@dataclasses.dataclass
class GetDataflowGraphRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "python_script",
                "PythonScript",
                TypeInfo(str),
            ),
        ]

    # The Python script to transform.
    python_script: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class GetDataflowGraphResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "dag_nodes",
                "DagNodes",
                TypeInfo(typing.List[CodeGenNode]),
            ),
            (
                "dag_edges",
                "DagEdges",
                TypeInfo(typing.List[CodeGenEdge]),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A list of the nodes in the resulting DAG.
    dag_nodes: typing.List["CodeGenNode"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A list of the edges in the resulting DAG.
    dag_edges: typing.List["CodeGenEdge"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class GetDevEndpointRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "endpoint_name",
                "EndpointName",
                TypeInfo(str),
            ),
        ]

    # Name of the DevEndpoint for which to retrieve information.
    endpoint_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class GetDevEndpointResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "dev_endpoint",
                "DevEndpoint",
                TypeInfo(DevEndpoint),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A DevEndpoint definition.
    dev_endpoint: "DevEndpoint" = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class GetDevEndpointsRequest(ShapeBase):
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

    # The maximum size of information to return.
    max_results: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A continuation token, if this is a continuation call.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class GetDevEndpointsResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "dev_endpoints",
                "DevEndpoints",
                TypeInfo(typing.List[DevEndpoint]),
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

    # A list of DevEndpoint definitions.
    dev_endpoints: typing.List["DevEndpoint"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A continuation token, if not all DevEndpoint definitions have yet been
    # returned.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    def paginate(self,
                ) -> typing.Generator["GetDevEndpointsResponse", None, None]:
        yield from super()._paginate()


@dataclasses.dataclass
class GetJobRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "job_name",
                "JobName",
                TypeInfo(str),
            ),
        ]

    # The name of the job definition to retrieve.
    job_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class GetJobResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "job",
                "Job",
                TypeInfo(Job),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The requested job definition.
    job: "Job" = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class GetJobRunRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "job_name",
                "JobName",
                TypeInfo(str),
            ),
            (
                "run_id",
                "RunId",
                TypeInfo(str),
            ),
            (
                "predecessors_included",
                "PredecessorsIncluded",
                TypeInfo(bool),
            ),
        ]

    # Name of the job definition being run.
    job_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The ID of the job run.
    run_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # True if a list of predecessor runs should be returned.
    predecessors_included: bool = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class GetJobRunResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "job_run",
                "JobRun",
                TypeInfo(JobRun),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The requested job-run metadata.
    job_run: "JobRun" = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class GetJobRunsRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "job_name",
                "JobName",
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

    # The name of the job definition for which to retrieve all job runs.
    job_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A continuation token, if this is a continuation call.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The maximum size of the response.
    max_results: int = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class GetJobRunsResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "job_runs",
                "JobRuns",
                TypeInfo(typing.List[JobRun]),
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

    # A list of job-run metatdata objects.
    job_runs: typing.List["JobRun"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A continuation token, if not all reequested job runs have been returned.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    def paginate(self, ) -> typing.Generator["GetJobRunsResponse", None, None]:
        yield from super()._paginate()


@dataclasses.dataclass
class GetJobsRequest(ShapeBase):
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

    # A continuation token, if this is a continuation call.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The maximum size of the response.
    max_results: int = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class GetJobsResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "jobs",
                "Jobs",
                TypeInfo(typing.List[Job]),
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

    # A list of job definitions.
    jobs: typing.List["Job"] = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A continuation token, if not all job definitions have yet been returned.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    def paginate(self, ) -> typing.Generator["GetJobsResponse", None, None]:
        yield from super()._paginate()


@dataclasses.dataclass
class GetMappingRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "source",
                "Source",
                TypeInfo(CatalogEntry),
            ),
            (
                "sinks",
                "Sinks",
                TypeInfo(typing.List[CatalogEntry]),
            ),
            (
                "location",
                "Location",
                TypeInfo(Location),
            ),
        ]

    # Specifies the source table.
    source: "CatalogEntry" = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A list of target tables.
    sinks: typing.List["CatalogEntry"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Parameters for the mapping.
    location: "Location" = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class GetMappingResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "mapping",
                "Mapping",
                TypeInfo(typing.List[MappingEntry]),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A list of mappings to the specified targets.
    mapping: typing.List["MappingEntry"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class GetPartitionRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "database_name",
                "DatabaseName",
                TypeInfo(str),
            ),
            (
                "table_name",
                "TableName",
                TypeInfo(str),
            ),
            (
                "partition_values",
                "PartitionValues",
                TypeInfo(typing.List[str]),
            ),
            (
                "catalog_id",
                "CatalogId",
                TypeInfo(str),
            ),
        ]

    # The name of the catalog database where the partition resides.
    database_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The name of the partition's table.
    table_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The values that define the partition.
    partition_values: typing.List[str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The ID of the Data Catalog where the partition in question resides. If none
    # is supplied, the AWS account ID is used by default.
    catalog_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class GetPartitionResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "partition",
                "Partition",
                TypeInfo(Partition),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The requested information, in the form of a `Partition` object.
    partition: "Partition" = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class GetPartitionsRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "database_name",
                "DatabaseName",
                TypeInfo(str),
            ),
            (
                "table_name",
                "TableName",
                TypeInfo(str),
            ),
            (
                "catalog_id",
                "CatalogId",
                TypeInfo(str),
            ),
            (
                "expression",
                "Expression",
                TypeInfo(str),
            ),
            (
                "next_token",
                "NextToken",
                TypeInfo(str),
            ),
            (
                "segment",
                "Segment",
                TypeInfo(Segment),
            ),
            (
                "max_results",
                "MaxResults",
                TypeInfo(int),
            ),
        ]

    # The name of the catalog database where the partitions reside.
    database_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The name of the partitions' table.
    table_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The ID of the Data Catalog where the partitions in question reside. If none
    # is supplied, the AWS account ID is used by default.
    catalog_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # An expression filtering the partitions to be returned.
    expression: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A continuation token, if this is not the first call to retrieve these
    # partitions.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The segment of the table's partitions to scan in this request.
    segment: "Segment" = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The maximum number of partitions to return in a single response.
    max_results: int = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class GetPartitionsResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "partitions",
                "Partitions",
                TypeInfo(typing.List[Partition]),
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

    # A list of requested partitions.
    partitions: typing.List["Partition"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A continuation token, if the returned list of partitions does not does not
    # include the last one.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    def paginate(self,
                ) -> typing.Generator["GetPartitionsResponse", None, None]:
        yield from super()._paginate()


@dataclasses.dataclass
class GetPlanRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "mapping",
                "Mapping",
                TypeInfo(typing.List[MappingEntry]),
            ),
            (
                "source",
                "Source",
                TypeInfo(CatalogEntry),
            ),
            (
                "sinks",
                "Sinks",
                TypeInfo(typing.List[CatalogEntry]),
            ),
            (
                "location",
                "Location",
                TypeInfo(Location),
            ),
            (
                "language",
                "Language",
                TypeInfo(typing.Union[str, Language]),
            ),
        ]

    # The list of mappings from a source table to target tables.
    mapping: typing.List["MappingEntry"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The source table.
    source: "CatalogEntry" = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The target tables.
    sinks: typing.List["CatalogEntry"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Parameters for the mapping.
    location: "Location" = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The programming language of the code to perform the mapping.
    language: typing.Union[str, "Language"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class GetPlanResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "python_script",
                "PythonScript",
                TypeInfo(str),
            ),
            (
                "scala_code",
                "ScalaCode",
                TypeInfo(str),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A Python script to perform the mapping.
    python_script: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Scala code to perform the mapping.
    scala_code: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class GetSecurityConfigurationRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "name",
                "Name",
                TypeInfo(str),
            ),
        ]

    # The name of the security configuration to retrieve.
    name: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class GetSecurityConfigurationResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "security_configuration",
                "SecurityConfiguration",
                TypeInfo(SecurityConfiguration),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The requested security configuration
    security_configuration: "SecurityConfiguration" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class GetSecurityConfigurationsRequest(ShapeBase):
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

    # The maximum number of results to return.
    max_results: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A continuation token, if this is a continuation call.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class GetSecurityConfigurationsResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "security_configurations",
                "SecurityConfigurations",
                TypeInfo(typing.List[SecurityConfiguration]),
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

    # A list of security configurations.
    security_configurations: typing.List["SecurityConfiguration"
                                        ] = dataclasses.field(
                                            default=ShapeBase.NOT_SET,
                                        )

    # A continuation token, if there are more security configurations to return.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class GetTableRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "database_name",
                "DatabaseName",
                TypeInfo(str),
            ),
            (
                "name",
                "Name",
                TypeInfo(str),
            ),
            (
                "catalog_id",
                "CatalogId",
                TypeInfo(str),
            ),
        ]

    # The name of the database in the catalog in which the table resides. For
    # Hive compatibility, this name is entirely lowercase.
    database_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The name of the table for which to retrieve the definition. For Hive
    # compatibility, this name is entirely lowercase.
    name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The ID of the Data Catalog where the table resides. If none is supplied,
    # the AWS account ID is used by default.
    catalog_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class GetTableResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "table",
                "Table",
                TypeInfo(Table),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The `Table` object that defines the specified table.
    table: "Table" = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class GetTableVersionRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "database_name",
                "DatabaseName",
                TypeInfo(str),
            ),
            (
                "table_name",
                "TableName",
                TypeInfo(str),
            ),
            (
                "catalog_id",
                "CatalogId",
                TypeInfo(str),
            ),
            (
                "version_id",
                "VersionId",
                TypeInfo(str),
            ),
        ]

    # The database in the catalog in which the table resides. For Hive
    # compatibility, this name is entirely lowercase.
    database_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The name of the table. For Hive compatibility, this name is entirely
    # lowercase.
    table_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The ID of the Data Catalog where the tables reside. If none is supplied,
    # the AWS account ID is used by default.
    catalog_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The ID value of the table version to be retrieved.
    version_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class GetTableVersionResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "table_version",
                "TableVersion",
                TypeInfo(TableVersion),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The requested table version.
    table_version: "TableVersion" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class GetTableVersionsRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "database_name",
                "DatabaseName",
                TypeInfo(str),
            ),
            (
                "table_name",
                "TableName",
                TypeInfo(str),
            ),
            (
                "catalog_id",
                "CatalogId",
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

    # The database in the catalog in which the table resides. For Hive
    # compatibility, this name is entirely lowercase.
    database_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The name of the table. For Hive compatibility, this name is entirely
    # lowercase.
    table_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The ID of the Data Catalog where the tables reside. If none is supplied,
    # the AWS account ID is used by default.
    catalog_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A continuation token, if this is not the first call.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The maximum number of table versions to return in one response.
    max_results: int = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class GetTableVersionsResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "table_versions",
                "TableVersions",
                TypeInfo(typing.List[TableVersion]),
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

    # A list of strings identifying available versions of the specified table.
    table_versions: typing.List["TableVersion"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A continuation token, if the list of available versions does not include
    # the last one.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    def paginate(self,
                ) -> typing.Generator["GetTableVersionsResponse", None, None]:
        yield from super()._paginate()


@dataclasses.dataclass
class GetTablesRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "database_name",
                "DatabaseName",
                TypeInfo(str),
            ),
            (
                "catalog_id",
                "CatalogId",
                TypeInfo(str),
            ),
            (
                "expression",
                "Expression",
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

    # The database in the catalog whose tables to list. For Hive compatibility,
    # this name is entirely lowercase.
    database_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The ID of the Data Catalog where the tables reside. If none is supplied,
    # the AWS account ID is used by default.
    catalog_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A regular expression pattern. If present, only those tables whose names
    # match the pattern are returned.
    expression: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A continuation token, included if this is a continuation call.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The maximum number of tables to return in a single response.
    max_results: int = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class GetTablesResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "table_list",
                "TableList",
                TypeInfo(typing.List[Table]),
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

    # A list of the requested `Table` objects.
    table_list: typing.List["Table"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A continuation token, present if the current list segment is not the last.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    def paginate(self, ) -> typing.Generator["GetTablesResponse", None, None]:
        yield from super()._paginate()


@dataclasses.dataclass
class GetTriggerRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "name",
                "Name",
                TypeInfo(str),
            ),
        ]

    # The name of the trigger to retrieve.
    name: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class GetTriggerResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "trigger",
                "Trigger",
                TypeInfo(Trigger),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The requested trigger definition.
    trigger: "Trigger" = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class GetTriggersRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "next_token",
                "NextToken",
                TypeInfo(str),
            ),
            (
                "dependent_job_name",
                "DependentJobName",
                TypeInfo(str),
            ),
            (
                "max_results",
                "MaxResults",
                TypeInfo(int),
            ),
        ]

    # A continuation token, if this is a continuation call.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The name of the job for which to retrieve triggers. The trigger that can
    # start this job will be returned, and if there is no such trigger, all
    # triggers will be returned.
    dependent_job_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The maximum size of the response.
    max_results: int = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class GetTriggersResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "triggers",
                "Triggers",
                TypeInfo(typing.List[Trigger]),
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

    # A list of triggers for the specified job.
    triggers: typing.List["Trigger"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A continuation token, if not all the requested triggers have yet been
    # returned.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    def paginate(self, ) -> typing.Generator["GetTriggersResponse", None, None]:
        yield from super()._paginate()


@dataclasses.dataclass
class GetUserDefinedFunctionRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "database_name",
                "DatabaseName",
                TypeInfo(str),
            ),
            (
                "function_name",
                "FunctionName",
                TypeInfo(str),
            ),
            (
                "catalog_id",
                "CatalogId",
                TypeInfo(str),
            ),
        ]

    # The name of the catalog database where the function is located.
    database_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The name of the function.
    function_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The ID of the Data Catalog where the function to be retrieved is located.
    # If none is supplied, the AWS account ID is used by default.
    catalog_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class GetUserDefinedFunctionResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "user_defined_function",
                "UserDefinedFunction",
                TypeInfo(UserDefinedFunction),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The requested function definition.
    user_defined_function: "UserDefinedFunction" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class GetUserDefinedFunctionsRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "database_name",
                "DatabaseName",
                TypeInfo(str),
            ),
            (
                "pattern",
                "Pattern",
                TypeInfo(str),
            ),
            (
                "catalog_id",
                "CatalogId",
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

    # The name of the catalog database where the functions are located.
    database_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # An optional function-name pattern string that filters the function
    # definitions returned.
    pattern: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The ID of the Data Catalog where the functions to be retrieved are located.
    # If none is supplied, the AWS account ID is used by default.
    catalog_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A continuation token, if this is a continuation call.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The maximum number of functions to return in one response.
    max_results: int = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class GetUserDefinedFunctionsResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "user_defined_functions",
                "UserDefinedFunctions",
                TypeInfo(typing.List[UserDefinedFunction]),
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

    # A list of requested function definitions.
    user_defined_functions: typing.List["UserDefinedFunction"
                                       ] = dataclasses.field(
                                           default=ShapeBase.NOT_SET,
                                       )

    # A continuation token, if the list of functions returned does not include
    # the last requested function.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    def paginate(
        self,
    ) -> typing.Generator["GetUserDefinedFunctionsResponse", None, None]:
        yield from super()._paginate()


@dataclasses.dataclass
class GlueEncryptionException(ShapeBase):
    """
    An encryption operation failed.
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

    # A message describing the problem.
    message: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class GrokClassifier(ShapeBase):
    """
    A classifier that uses `grok` patterns.
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
                "classification",
                "Classification",
                TypeInfo(str),
            ),
            (
                "grok_pattern",
                "GrokPattern",
                TypeInfo(str),
            ),
            (
                "creation_time",
                "CreationTime",
                TypeInfo(datetime.datetime),
            ),
            (
                "last_updated",
                "LastUpdated",
                TypeInfo(datetime.datetime),
            ),
            (
                "version",
                "Version",
                TypeInfo(int),
            ),
            (
                "custom_patterns",
                "CustomPatterns",
                TypeInfo(str),
            ),
        ]

    # The name of the classifier.
    name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # An identifier of the data format that the classifier matches, such as
    # Twitter, JSON, Omniture logs, and so on.
    classification: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The grok pattern applied to a data store by this classifier. For more
    # information, see built-in patterns in [Writing Custom
    # Classifers](http://docs.aws.amazon.com/glue/latest/dg/custom-
    # classifier.html).
    grok_pattern: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The time this classifier was registered.
    creation_time: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The time this classifier was last updated.
    last_updated: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The version of this classifier.
    version: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Optional custom grok patterns defined by this classifier. For more
    # information, see custom patterns in [Writing Custom
    # Classifers](http://docs.aws.amazon.com/glue/latest/dg/custom-
    # classifier.html).
    custom_patterns: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class IdempotentParameterMismatchException(ShapeBase):
    """
    The same unique identifier was associated with two different records.
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

    # A message describing the problem.
    message: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ImportCatalogToGlueRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "catalog_id",
                "CatalogId",
                TypeInfo(str),
            ),
        ]

    # The ID of the catalog to import. Currently, this should be the AWS account
    # ID.
    catalog_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ImportCatalogToGlueResponse(OutputShapeBase):
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
class InternalServiceException(ShapeBase):
    """
    An internal service error occurred.
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

    # A message describing the problem.
    message: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class InvalidInputException(ShapeBase):
    """
    The input provided was not valid.
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

    # A message describing the problem.
    message: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class JdbcTarget(ShapeBase):
    """
    Specifies a JDBC data store to crawl.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "connection_name",
                "ConnectionName",
                TypeInfo(str),
            ),
            (
                "path",
                "Path",
                TypeInfo(str),
            ),
            (
                "exclusions",
                "Exclusions",
                TypeInfo(typing.List[str]),
            ),
        ]

    # The name of the connection to use to connect to the JDBC target.
    connection_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The path of the JDBC target.
    path: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A list of glob patterns used to exclude from the crawl. For more
    # information, see [Catalog Tables with a
    # Crawler](http://docs.aws.amazon.com/glue/latest/dg/add-crawler.html).
    exclusions: typing.List[str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class Job(ShapeBase):
    """
    Specifies a job definition.
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
                "log_uri",
                "LogUri",
                TypeInfo(str),
            ),
            (
                "role",
                "Role",
                TypeInfo(str),
            ),
            (
                "created_on",
                "CreatedOn",
                TypeInfo(datetime.datetime),
            ),
            (
                "last_modified_on",
                "LastModifiedOn",
                TypeInfo(datetime.datetime),
            ),
            (
                "execution_property",
                "ExecutionProperty",
                TypeInfo(ExecutionProperty),
            ),
            (
                "command",
                "Command",
                TypeInfo(JobCommand),
            ),
            (
                "default_arguments",
                "DefaultArguments",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "connections",
                "Connections",
                TypeInfo(ConnectionsList),
            ),
            (
                "max_retries",
                "MaxRetries",
                TypeInfo(int),
            ),
            (
                "allocated_capacity",
                "AllocatedCapacity",
                TypeInfo(int),
            ),
            (
                "timeout",
                "Timeout",
                TypeInfo(int),
            ),
            (
                "notification_property",
                "NotificationProperty",
                TypeInfo(NotificationProperty),
            ),
            (
                "security_configuration",
                "SecurityConfiguration",
                TypeInfo(str),
            ),
        ]

    # The name you assign to this job definition.
    name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Description of the job being defined.
    description: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # This field is reserved for future use.
    log_uri: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The name or ARN of the IAM role associated with this job.
    role: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The time and date that this job definition was created.
    created_on: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The last point in time when this job definition was modified.
    last_modified_on: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # An ExecutionProperty specifying the maximum number of concurrent runs
    # allowed for this job.
    execution_property: "ExecutionProperty" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The JobCommand that executes this job.
    command: "JobCommand" = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The default arguments for this job, specified as name-value pairs.

    # You can specify arguments here that your own job-execution script consumes,
    # as well as arguments that AWS Glue itself consumes.

    # For information about how to specify and consume your own Job arguments,
    # see the [Calling AWS Glue APIs in
    # Python](http://docs.aws.amazon.com/glue/latest/dg/aws-glue-programming-
    # python-calling.html) topic in the developer guide.

    # For information about the key-value pairs that AWS Glue consumes to set up
    # your job, see the [Special Parameters Used by AWS
    # Glue](http://docs.aws.amazon.com/glue/latest/dg/aws-glue-programming-etl-
    # glue-arguments.html) topic in the developer guide.
    default_arguments: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The connections used for this job.
    connections: "ConnectionsList" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The maximum number of times to retry this job after a JobRun fails.
    max_retries: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The number of AWS Glue data processing units (DPUs) allocated to runs of
    # this job. From 2 to 100 DPUs can be allocated; the default is 10. A DPU is
    # a relative measure of processing power that consists of 4 vCPUs of compute
    # capacity and 16 GB of memory. For more information, see the [AWS Glue
    # pricing page](https://aws.amazon.com/glue/pricing/).
    allocated_capacity: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The job timeout in minutes. This is the maximum time that a job run can
    # consume resources before it is terminated and enters `TIMEOUT` status. The
    # default is 2,880 minutes (48 hours).
    timeout: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Specifies configuration properties of a job notification.
    notification_property: "NotificationProperty" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The name of the SecurityConfiguration structure to be used with this job.
    security_configuration: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class JobBookmarkEntry(ShapeBase):
    """
    Defines a point which a job can resume processing.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "job_name",
                "JobName",
                TypeInfo(str),
            ),
            (
                "version",
                "Version",
                TypeInfo(int),
            ),
            (
                "run",
                "Run",
                TypeInfo(int),
            ),
            (
                "attempt",
                "Attempt",
                TypeInfo(int),
            ),
            (
                "job_bookmark",
                "JobBookmark",
                TypeInfo(str),
            ),
        ]

    # Name of the job in question.
    job_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Version of the job.
    version: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The run ID number.
    run: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The attempt ID number.
    attempt: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The bookmark itself.
    job_bookmark: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class JobBookmarksEncryption(ShapeBase):
    """
    Specifies how Job bookmark data should be encrypted.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "job_bookmarks_encryption_mode",
                "JobBookmarksEncryptionMode",
                TypeInfo(typing.Union[str, JobBookmarksEncryptionMode]),
            ),
            (
                "kms_key_arn",
                "KmsKeyArn",
                TypeInfo(str),
            ),
        ]

    # The encryption mode to use for Job bookmarks data.
    job_bookmarks_encryption_mode: typing.Union[
        str, "JobBookmarksEncryptionMode"] = dataclasses.field(
            default=ShapeBase.NOT_SET,
        )

    # The AWS ARN of the KMS key to be used to encrypt the data.
    kms_key_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )


class JobBookmarksEncryptionMode(str):
    DISABLED = "DISABLED"
    CSE_KMS = "CSE-KMS"


@dataclasses.dataclass
class JobCommand(ShapeBase):
    """
    Specifies code executed when a job is run.
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
                "script_location",
                "ScriptLocation",
                TypeInfo(str),
            ),
        ]

    # The name of the job command: this must be `glueetl`.
    name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Specifies the S3 path to a script that executes a job (required).
    script_location: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class JobRun(ShapeBase):
    """
    Contains information about a job run.
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
                "attempt",
                "Attempt",
                TypeInfo(int),
            ),
            (
                "previous_run_id",
                "PreviousRunId",
                TypeInfo(str),
            ),
            (
                "trigger_name",
                "TriggerName",
                TypeInfo(str),
            ),
            (
                "job_name",
                "JobName",
                TypeInfo(str),
            ),
            (
                "started_on",
                "StartedOn",
                TypeInfo(datetime.datetime),
            ),
            (
                "last_modified_on",
                "LastModifiedOn",
                TypeInfo(datetime.datetime),
            ),
            (
                "completed_on",
                "CompletedOn",
                TypeInfo(datetime.datetime),
            ),
            (
                "job_run_state",
                "JobRunState",
                TypeInfo(typing.Union[str, JobRunState]),
            ),
            (
                "arguments",
                "Arguments",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "error_message",
                "ErrorMessage",
                TypeInfo(str),
            ),
            (
                "predecessor_runs",
                "PredecessorRuns",
                TypeInfo(typing.List[Predecessor]),
            ),
            (
                "allocated_capacity",
                "AllocatedCapacity",
                TypeInfo(int),
            ),
            (
                "execution_time",
                "ExecutionTime",
                TypeInfo(int),
            ),
            (
                "timeout",
                "Timeout",
                TypeInfo(int),
            ),
            (
                "notification_property",
                "NotificationProperty",
                TypeInfo(NotificationProperty),
            ),
            (
                "security_configuration",
                "SecurityConfiguration",
                TypeInfo(str),
            ),
            (
                "log_group_name",
                "LogGroupName",
                TypeInfo(str),
            ),
        ]

    # The ID of this job run.
    id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The number of the attempt to run this job.
    attempt: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The ID of the previous run of this job. For example, the JobRunId specified
    # in the StartJobRun action.
    previous_run_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The name of the trigger that started this job run.
    trigger_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The name of the job definition being used in this run.
    job_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The date and time at which this job run was started.
    started_on: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The last time this job run was modified.
    last_modified_on: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The date and time this job run completed.
    completed_on: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The current state of the job run.
    job_run_state: typing.Union[str, "JobRunState"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The job arguments associated with this run. These override equivalent
    # default arguments set for the job.

    # You can specify arguments here that your own job-execution script consumes,
    # as well as arguments that AWS Glue itself consumes.

    # For information about how to specify and consume your own job arguments,
    # see the [Calling AWS Glue APIs in
    # Python](http://docs.aws.amazon.com/glue/latest/dg/aws-glue-programming-
    # python-calling.html) topic in the developer guide.

    # For information about the key-value pairs that AWS Glue consumes to set up
    # your job, see the [Special Parameters Used by AWS
    # Glue](http://docs.aws.amazon.com/glue/latest/dg/aws-glue-programming-etl-
    # glue-arguments.html) topic in the developer guide.
    arguments: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # An error message associated with this job run.
    error_message: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A list of predecessors to this job run.
    predecessor_runs: typing.List["Predecessor"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The number of AWS Glue data processing units (DPUs) allocated to this
    # JobRun. From 2 to 100 DPUs can be allocated; the default is 10. A DPU is a
    # relative measure of processing power that consists of 4 vCPUs of compute
    # capacity and 16 GB of memory. For more information, see the [AWS Glue
    # pricing page](https://aws.amazon.com/glue/pricing/).
    allocated_capacity: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The amount of time (in seconds) that the job run consumed resources.
    execution_time: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The JobRun timeout in minutes. This is the maximum time that a job run can
    # consume resources before it is terminated and enters `TIMEOUT` status. The
    # default is 2,880 minutes (48 hours). This overrides the timeout value set
    # in the parent job.
    timeout: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Specifies configuration properties of a job run notification.
    notification_property: "NotificationProperty" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The name of the SecurityConfiguration structure to be used with this job
    # run.
    security_configuration: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The name of the log group for secure logging, that can be server-side
    # encrypted in CloudWatch using KMS. This name can be `/aws-glue/jobs/`, in
    # which case the default encryption is `NONE`. If you add a role name and
    # SecurityConfiguration name (in other words, `/aws-glue/jobs-yourRoleName-
    # yourSecurityConfigurationName/`), then that security configuration will be
    # used to encrypt the log group.
    log_group_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )


class JobRunState(str):
    STARTING = "STARTING"
    RUNNING = "RUNNING"
    STOPPING = "STOPPING"
    STOPPED = "STOPPED"
    SUCCEEDED = "SUCCEEDED"
    FAILED = "FAILED"
    TIMEOUT = "TIMEOUT"


@dataclasses.dataclass
class JobUpdate(ShapeBase):
    """
    Specifies information used to update an existing job definition. Note that the
    previous job definition will be completely overwritten by this information.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "description",
                "Description",
                TypeInfo(str),
            ),
            (
                "log_uri",
                "LogUri",
                TypeInfo(str),
            ),
            (
                "role",
                "Role",
                TypeInfo(str),
            ),
            (
                "execution_property",
                "ExecutionProperty",
                TypeInfo(ExecutionProperty),
            ),
            (
                "command",
                "Command",
                TypeInfo(JobCommand),
            ),
            (
                "default_arguments",
                "DefaultArguments",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "connections",
                "Connections",
                TypeInfo(ConnectionsList),
            ),
            (
                "max_retries",
                "MaxRetries",
                TypeInfo(int),
            ),
            (
                "allocated_capacity",
                "AllocatedCapacity",
                TypeInfo(int),
            ),
            (
                "timeout",
                "Timeout",
                TypeInfo(int),
            ),
            (
                "notification_property",
                "NotificationProperty",
                TypeInfo(NotificationProperty),
            ),
            (
                "security_configuration",
                "SecurityConfiguration",
                TypeInfo(str),
            ),
        ]

    # Description of the job being defined.
    description: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # This field is reserved for future use.
    log_uri: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The name or ARN of the IAM role associated with this job (required).
    role: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # An ExecutionProperty specifying the maximum number of concurrent runs
    # allowed for this job.
    execution_property: "ExecutionProperty" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The JobCommand that executes this job (required).
    command: "JobCommand" = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The default arguments for this job.

    # You can specify arguments here that your own job-execution script consumes,
    # as well as arguments that AWS Glue itself consumes.

    # For information about how to specify and consume your own Job arguments,
    # see the [Calling AWS Glue APIs in
    # Python](http://docs.aws.amazon.com/glue/latest/dg/aws-glue-programming-
    # python-calling.html) topic in the developer guide.

    # For information about the key-value pairs that AWS Glue consumes to set up
    # your job, see the [Special Parameters Used by AWS
    # Glue](http://docs.aws.amazon.com/glue/latest/dg/aws-glue-programming-etl-
    # glue-arguments.html) topic in the developer guide.
    default_arguments: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The connections used for this job.
    connections: "ConnectionsList" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The maximum number of times to retry this job if it fails.
    max_retries: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The number of AWS Glue data processing units (DPUs) to allocate to this
    # Job. From 2 to 100 DPUs can be allocated; the default is 10. A DPU is a
    # relative measure of processing power that consists of 4 vCPUs of compute
    # capacity and 16 GB of memory. For more information, see the [AWS Glue
    # pricing page](https://aws.amazon.com/glue/pricing/).
    allocated_capacity: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The job timeout in minutes. This is the maximum time that a job run can
    # consume resources before it is terminated and enters `TIMEOUT` status. The
    # default is 2,880 minutes (48 hours).
    timeout: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Specifies configuration properties of a job notification.
    notification_property: "NotificationProperty" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The name of the SecurityConfiguration structure to be used with this job.
    security_configuration: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class JsonClassifier(ShapeBase):
    """
    A classifier for `JSON` content.
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
                "json_path",
                "JsonPath",
                TypeInfo(str),
            ),
            (
                "creation_time",
                "CreationTime",
                TypeInfo(datetime.datetime),
            ),
            (
                "last_updated",
                "LastUpdated",
                TypeInfo(datetime.datetime),
            ),
            (
                "version",
                "Version",
                TypeInfo(int),
            ),
        ]

    # The name of the classifier.
    name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A `JsonPath` string defining the JSON data for the classifier to classify.
    # AWS Glue supports a subset of JsonPath, as described in [Writing JsonPath
    # Custom Classifiers](https://docs.aws.amazon.com/glue/latest/dg/custom-
    # classifier.html#custom-classifier-json).
    json_path: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The time this classifier was registered.
    creation_time: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The time this classifier was last updated.
    last_updated: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The version of this classifier.
    version: int = dataclasses.field(default=ShapeBase.NOT_SET, )


class Language(str):
    PYTHON = "PYTHON"
    SCALA = "SCALA"


@dataclasses.dataclass
class LastCrawlInfo(ShapeBase):
    """
    Status and error information about the most recent crawl.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "status",
                "Status",
                TypeInfo(typing.Union[str, LastCrawlStatus]),
            ),
            (
                "error_message",
                "ErrorMessage",
                TypeInfo(str),
            ),
            (
                "log_group",
                "LogGroup",
                TypeInfo(str),
            ),
            (
                "log_stream",
                "LogStream",
                TypeInfo(str),
            ),
            (
                "message_prefix",
                "MessagePrefix",
                TypeInfo(str),
            ),
            (
                "start_time",
                "StartTime",
                TypeInfo(datetime.datetime),
            ),
        ]

    # Status of the last crawl.
    status: typing.Union[str, "LastCrawlStatus"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # If an error occurred, the error information about the last crawl.
    error_message: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The log group for the last crawl.
    log_group: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The log stream for the last crawl.
    log_stream: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The prefix for a message about this crawl.
    message_prefix: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The time at which the crawl started.
    start_time: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


class LastCrawlStatus(str):
    SUCCEEDED = "SUCCEEDED"
    CANCELLED = "CANCELLED"
    FAILED = "FAILED"


@dataclasses.dataclass
class Location(ShapeBase):
    """
    The location of resources.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "jdbc",
                "Jdbc",
                TypeInfo(typing.List[CodeGenNodeArg]),
            ),
            (
                "s3",
                "S3",
                TypeInfo(typing.List[CodeGenNodeArg]),
            ),
            (
                "dynamo_db",
                "DynamoDB",
                TypeInfo(typing.List[CodeGenNodeArg]),
            ),
        ]

    # A JDBC location.
    jdbc: typing.List["CodeGenNodeArg"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # An Amazon S3 location.
    s3: typing.List["CodeGenNodeArg"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A DynamoDB Table location.
    dynamo_db: typing.List["CodeGenNodeArg"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


class Logical(str):
    AND = "AND"
    ANY = "ANY"


class LogicalOperator(str):
    EQUALS = "EQUALS"


@dataclasses.dataclass
class MappingEntry(ShapeBase):
    """
    Defines a mapping.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "source_table",
                "SourceTable",
                TypeInfo(str),
            ),
            (
                "source_path",
                "SourcePath",
                TypeInfo(str),
            ),
            (
                "source_type",
                "SourceType",
                TypeInfo(str),
            ),
            (
                "target_table",
                "TargetTable",
                TypeInfo(str),
            ),
            (
                "target_path",
                "TargetPath",
                TypeInfo(str),
            ),
            (
                "target_type",
                "TargetType",
                TypeInfo(str),
            ),
        ]

    # The name of the source table.
    source_table: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The source path.
    source_path: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The source type.
    source_type: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The target table.
    target_table: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The target path.
    target_path: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The target type.
    target_type: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class NoScheduleException(ShapeBase):
    """
    There is no applicable schedule.
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

    # A message describing the problem.
    message: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class NotificationProperty(ShapeBase):
    """
    Specifies configuration properties of a notification.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "notify_delay_after",
                "NotifyDelayAfter",
                TypeInfo(int),
            ),
        ]

    # After a job run starts, the number of minutes to wait before sending a job
    # run delay notification.
    notify_delay_after: int = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class OperationTimeoutException(ShapeBase):
    """
    The operation timed out.
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

    # A message describing the problem.
    message: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class Order(ShapeBase):
    """
    Specifies the sort order of a sorted column.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "column",
                "Column",
                TypeInfo(str),
            ),
            (
                "sort_order",
                "SortOrder",
                TypeInfo(int),
            ),
        ]

    # The name of the column.
    column: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Indicates that the column is sorted in ascending order (`== 1`), or in
    # descending order (`==0`).
    sort_order: int = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class Partition(ShapeBase):
    """
    Represents a slice of table data.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "values",
                "Values",
                TypeInfo(typing.List[str]),
            ),
            (
                "database_name",
                "DatabaseName",
                TypeInfo(str),
            ),
            (
                "table_name",
                "TableName",
                TypeInfo(str),
            ),
            (
                "creation_time",
                "CreationTime",
                TypeInfo(datetime.datetime),
            ),
            (
                "last_access_time",
                "LastAccessTime",
                TypeInfo(datetime.datetime),
            ),
            (
                "storage_descriptor",
                "StorageDescriptor",
                TypeInfo(StorageDescriptor),
            ),
            (
                "parameters",
                "Parameters",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "last_analyzed_time",
                "LastAnalyzedTime",
                TypeInfo(datetime.datetime),
            ),
        ]

    # The values of the partition.
    values: typing.List[str] = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The name of the catalog database where the table in question is located.
    database_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The name of the table in question.
    table_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The time at which the partition was created.
    creation_time: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The last time at which the partition was accessed.
    last_access_time: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Provides information about the physical location where the partition is
    # stored.
    storage_descriptor: "StorageDescriptor" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # These key-value pairs define partition parameters.
    parameters: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The last time at which column statistics were computed for this partition.
    last_analyzed_time: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class PartitionError(ShapeBase):
    """
    Contains information about a partition error.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "partition_values",
                "PartitionValues",
                TypeInfo(typing.List[str]),
            ),
            (
                "error_detail",
                "ErrorDetail",
                TypeInfo(ErrorDetail),
            ),
        ]

    # The values that define the partition.
    partition_values: typing.List[str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Details about the partition error.
    error_detail: "ErrorDetail" = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class PartitionInput(ShapeBase):
    """
    The structure used to create and update a partion.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "values",
                "Values",
                TypeInfo(typing.List[str]),
            ),
            (
                "last_access_time",
                "LastAccessTime",
                TypeInfo(datetime.datetime),
            ),
            (
                "storage_descriptor",
                "StorageDescriptor",
                TypeInfo(StorageDescriptor),
            ),
            (
                "parameters",
                "Parameters",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "last_analyzed_time",
                "LastAnalyzedTime",
                TypeInfo(datetime.datetime),
            ),
        ]

    # The values of the partition.
    values: typing.List[str] = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The last time at which the partition was accessed.
    last_access_time: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Provides information about the physical location where the partition is
    # stored.
    storage_descriptor: "StorageDescriptor" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # These key-value pairs define partition parameters.
    parameters: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The last time at which column statistics were computed for this partition.
    last_analyzed_time: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class PartitionValueList(ShapeBase):
    """
    Contains a list of values defining partitions.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "values",
                "Values",
                TypeInfo(typing.List[str]),
            ),
        ]

    # The list of values.
    values: typing.List[str] = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class PhysicalConnectionRequirements(ShapeBase):
    """
    Specifies the physical requirements for a connection.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "subnet_id",
                "SubnetId",
                TypeInfo(str),
            ),
            (
                "security_group_id_list",
                "SecurityGroupIdList",
                TypeInfo(typing.List[str]),
            ),
            (
                "availability_zone",
                "AvailabilityZone",
                TypeInfo(str),
            ),
        ]

    # The subnet ID used by the connection.
    subnet_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The security group ID list used by the connection.
    security_group_id_list: typing.List[str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The connection's availability zone. This field is redundant, since the
    # specified subnet implies the availability zone to be used. The field must
    # be populated now, but will be deprecated in the future.
    availability_zone: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class Predecessor(ShapeBase):
    """
    A job run that was used in the predicate of a conditional trigger that triggered
    this job run.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "job_name",
                "JobName",
                TypeInfo(str),
            ),
            (
                "run_id",
                "RunId",
                TypeInfo(str),
            ),
        ]

    # The name of the job definition used by the predecessor job run.
    job_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The job-run ID of the predecessor job run.
    run_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class Predicate(ShapeBase):
    """
    Defines the predicate of the trigger, which determines when it fires.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "logical",
                "Logical",
                TypeInfo(typing.Union[str, Logical]),
            ),
            (
                "conditions",
                "Conditions",
                TypeInfo(typing.List[Condition]),
            ),
        ]

    # Optional field if only one condition is listed. If multiple conditions are
    # listed, then this field is required.
    logical: typing.Union[str, "Logical"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A list of the conditions that determine when the trigger will fire.
    conditions: typing.List["Condition"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


class PrincipalType(str):
    USER = "USER"
    ROLE = "ROLE"
    GROUP = "GROUP"


@dataclasses.dataclass
class PutDataCatalogEncryptionSettingsRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "data_catalog_encryption_settings",
                "DataCatalogEncryptionSettings",
                TypeInfo(DataCatalogEncryptionSettings),
            ),
            (
                "catalog_id",
                "CatalogId",
                TypeInfo(str),
            ),
        ]

    # The security configuration to set.
    data_catalog_encryption_settings: "DataCatalogEncryptionSettings" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The ID of the Data Catalog for which to set the security configuration. If
    # none is supplied, the AWS account ID is used by default.
    catalog_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class PutDataCatalogEncryptionSettingsResponse(OutputShapeBase):
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
class ResetJobBookmarkRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "job_name",
                "JobName",
                TypeInfo(str),
            ),
        ]

    # The name of the job in question.
    job_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ResetJobBookmarkResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "job_bookmark_entry",
                "JobBookmarkEntry",
                TypeInfo(JobBookmarkEntry),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The reset bookmark entry.
    job_bookmark_entry: "JobBookmarkEntry" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class ResourceNumberLimitExceededException(ShapeBase):
    """
    A resource numerical limit was exceeded.
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

    # A message describing the problem.
    message: str = dataclasses.field(default=ShapeBase.NOT_SET, )


class ResourceType(str):
    JAR = "JAR"
    FILE = "FILE"
    ARCHIVE = "ARCHIVE"


@dataclasses.dataclass
class ResourceUri(ShapeBase):
    """
    URIs for function resources.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "resource_type",
                "ResourceType",
                TypeInfo(typing.Union[str, ResourceType]),
            ),
            (
                "uri",
                "Uri",
                TypeInfo(str),
            ),
        ]

    # The type of the resource.
    resource_type: typing.Union[str, "ResourceType"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The URI for accessing the resource.
    uri: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class S3Encryption(ShapeBase):
    """
    Specifies how S3 data should be encrypted.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "s3_encryption_mode",
                "S3EncryptionMode",
                TypeInfo(typing.Union[str, S3EncryptionMode]),
            ),
            (
                "kms_key_arn",
                "KmsKeyArn",
                TypeInfo(str),
            ),
        ]

    # The encryption mode to use for S3 data.
    s3_encryption_mode: typing.Union[str, "S3EncryptionMode"
                                    ] = dataclasses.field(
                                        default=ShapeBase.NOT_SET,
                                    )

    # The AWS ARN of the KMS key to be used to encrypt the data.
    kms_key_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )


class S3EncryptionMode(str):
    DISABLED = "DISABLED"
    SSE_KMS = "SSE-KMS"
    SSE_S3 = "SSE-S3"


@dataclasses.dataclass
class S3Target(ShapeBase):
    """
    Specifies a data store in Amazon S3.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "path",
                "Path",
                TypeInfo(str),
            ),
            (
                "exclusions",
                "Exclusions",
                TypeInfo(typing.List[str]),
            ),
        ]

    # The path to the Amazon S3 target.
    path: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A list of glob patterns used to exclude from the crawl. For more
    # information, see [Catalog Tables with a
    # Crawler](http://docs.aws.amazon.com/glue/latest/dg/add-crawler.html).
    exclusions: typing.List[str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class Schedule(ShapeBase):
    """
    A scheduling object using a `cron` statement to schedule an event.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "schedule_expression",
                "ScheduleExpression",
                TypeInfo(str),
            ),
            (
                "state",
                "State",
                TypeInfo(typing.Union[str, ScheduleState]),
            ),
        ]

    # A `cron` expression used to specify the schedule (see [Time-Based Schedules
    # for Jobs and Crawlers](http://docs.aws.amazon.com/glue/latest/dg/monitor-
    # data-warehouse-schedule.html). For example, to run something every day at
    # 12:15 UTC, you would specify: `cron(15 12 * * ? *)`.
    schedule_expression: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The state of the schedule.
    state: typing.Union[str, "ScheduleState"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


class ScheduleState(str):
    SCHEDULED = "SCHEDULED"
    NOT_SCHEDULED = "NOT_SCHEDULED"
    TRANSITIONING = "TRANSITIONING"


@dataclasses.dataclass
class SchedulerNotRunningException(ShapeBase):
    """
    The specified scheduler is not running.
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

    # A message describing the problem.
    message: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class SchedulerRunningException(ShapeBase):
    """
    The specified scheduler is already running.
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

    # A message describing the problem.
    message: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class SchedulerTransitioningException(ShapeBase):
    """
    The specified scheduler is transitioning.
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

    # A message describing the problem.
    message: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class SchemaChangePolicy(ShapeBase):
    """
    Crawler policy for update and deletion behavior.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "update_behavior",
                "UpdateBehavior",
                TypeInfo(typing.Union[str, UpdateBehavior]),
            ),
            (
                "delete_behavior",
                "DeleteBehavior",
                TypeInfo(typing.Union[str, DeleteBehavior]),
            ),
        ]

    # The update behavior when the crawler finds a changed schema.
    update_behavior: typing.Union[str, "UpdateBehavior"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The deletion behavior when the crawler finds a deleted object.
    delete_behavior: typing.Union[str, "DeleteBehavior"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class SecurityConfiguration(ShapeBase):
    """
    Specifies a security configuration.
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
                "created_time_stamp",
                "CreatedTimeStamp",
                TypeInfo(datetime.datetime),
            ),
            (
                "encryption_configuration",
                "EncryptionConfiguration",
                TypeInfo(EncryptionConfiguration),
            ),
        ]

    # The name of the security configuration.
    name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The time at which this security configuration was created.
    created_time_stamp: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The encryption configuration associated with this security configuration.
    encryption_configuration: "EncryptionConfiguration" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class Segment(ShapeBase):
    """
    Defines a non-overlapping region of a table's partitions, allowing multiple
    requests to be executed in parallel.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "segment_number",
                "SegmentNumber",
                TypeInfo(int),
            ),
            (
                "total_segments",
                "TotalSegments",
                TypeInfo(int),
            ),
        ]

    # The zero-based index number of the this segment. For example, if the total
    # number of segments is 4, SegmentNumber values will range from zero through
    # three.
    segment_number: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The total numer of segments.
    total_segments: int = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class SerDeInfo(ShapeBase):
    """
    Information about a serialization/deserialization program (SerDe) which serves
    as an extractor and loader.
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
                "serialization_library",
                "SerializationLibrary",
                TypeInfo(str),
            ),
            (
                "parameters",
                "Parameters",
                TypeInfo(typing.Dict[str, str]),
            ),
        ]

    # Name of the SerDe.
    name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Usually the class that implements the SerDe. An example is:
    # `org.apache.hadoop.hive.serde2.columnar.ColumnarSerDe`.
    serialization_library: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # These key-value pairs define initialization parameters for the SerDe.
    parameters: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class SkewedInfo(ShapeBase):
    """
    Specifies skewed values in a table. Skewed are ones that occur with very high
    frequency.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "skewed_column_names",
                "SkewedColumnNames",
                TypeInfo(typing.List[str]),
            ),
            (
                "skewed_column_values",
                "SkewedColumnValues",
                TypeInfo(typing.List[str]),
            ),
            (
                "skewed_column_value_location_maps",
                "SkewedColumnValueLocationMaps",
                TypeInfo(typing.Dict[str, str]),
            ),
        ]

    # A list of names of columns that contain skewed values.
    skewed_column_names: typing.List[str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A list of values that appear so frequently as to be considered skewed.
    skewed_column_values: typing.List[str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A mapping of skewed values to the columns that contain them.
    skewed_column_value_location_maps: typing.Dict[str, str
                                                  ] = dataclasses.field(
                                                      default=ShapeBase.NOT_SET,
                                                  )


@dataclasses.dataclass
class StartCrawlerRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "name",
                "Name",
                TypeInfo(str),
            ),
        ]

    # Name of the crawler to start.
    name: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class StartCrawlerResponse(OutputShapeBase):
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
class StartCrawlerScheduleRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "crawler_name",
                "CrawlerName",
                TypeInfo(str),
            ),
        ]

    # Name of the crawler to schedule.
    crawler_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class StartCrawlerScheduleResponse(OutputShapeBase):
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
class StartJobRunRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "job_name",
                "JobName",
                TypeInfo(str),
            ),
            (
                "job_run_id",
                "JobRunId",
                TypeInfo(str),
            ),
            (
                "arguments",
                "Arguments",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "allocated_capacity",
                "AllocatedCapacity",
                TypeInfo(int),
            ),
            (
                "timeout",
                "Timeout",
                TypeInfo(int),
            ),
            (
                "notification_property",
                "NotificationProperty",
                TypeInfo(NotificationProperty),
            ),
            (
                "security_configuration",
                "SecurityConfiguration",
                TypeInfo(str),
            ),
        ]

    # The name of the job definition to use.
    job_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The ID of a previous JobRun to retry.
    job_run_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The job arguments specifically for this run. They override the equivalent
    # default arguments set for in the job definition itself.

    # You can specify arguments here that your own job-execution script consumes,
    # as well as arguments that AWS Glue itself consumes.

    # For information about how to specify and consume your own Job arguments,
    # see the [Calling AWS Glue APIs in
    # Python](http://docs.aws.amazon.com/glue/latest/dg/aws-glue-programming-
    # python-calling.html) topic in the developer guide.

    # For information about the key-value pairs that AWS Glue consumes to set up
    # your job, see the [Special Parameters Used by AWS
    # Glue](http://docs.aws.amazon.com/glue/latest/dg/aws-glue-programming-etl-
    # glue-arguments.html) topic in the developer guide.
    arguments: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The number of AWS Glue data processing units (DPUs) to allocate to this
    # JobRun. From 2 to 100 DPUs can be allocated; the default is 10. A DPU is a
    # relative measure of processing power that consists of 4 vCPUs of compute
    # capacity and 16 GB of memory. For more information, see the [AWS Glue
    # pricing page](https://aws.amazon.com/glue/pricing/).
    allocated_capacity: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The JobRun timeout in minutes. This is the maximum time that a job run can
    # consume resources before it is terminated and enters `TIMEOUT` status. The
    # default is 2,880 minutes (48 hours). This overrides the timeout value set
    # in the parent job.
    timeout: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Specifies configuration properties of a job run notification.
    notification_property: "NotificationProperty" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The name of the SecurityConfiguration structure to be used with this job
    # run.
    security_configuration: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class StartJobRunResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "job_run_id",
                "JobRunId",
                TypeInfo(str),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The ID assigned to this job run.
    job_run_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class StartTriggerRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "name",
                "Name",
                TypeInfo(str),
            ),
        ]

    # The name of the trigger to start.
    name: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class StartTriggerResponse(OutputShapeBase):
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

    # The name of the trigger that was started.
    name: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class StopCrawlerRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "name",
                "Name",
                TypeInfo(str),
            ),
        ]

    # Name of the crawler to stop.
    name: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class StopCrawlerResponse(OutputShapeBase):
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
class StopCrawlerScheduleRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "crawler_name",
                "CrawlerName",
                TypeInfo(str),
            ),
        ]

    # Name of the crawler whose schedule state to set.
    crawler_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class StopCrawlerScheduleResponse(OutputShapeBase):
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
class StopTriggerRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "name",
                "Name",
                TypeInfo(str),
            ),
        ]

    # The name of the trigger to stop.
    name: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class StopTriggerResponse(OutputShapeBase):
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

    # The name of the trigger that was stopped.
    name: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class StorageDescriptor(ShapeBase):
    """
    Describes the physical storage of table data.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "columns",
                "Columns",
                TypeInfo(typing.List[Column]),
            ),
            (
                "location",
                "Location",
                TypeInfo(str),
            ),
            (
                "input_format",
                "InputFormat",
                TypeInfo(str),
            ),
            (
                "output_format",
                "OutputFormat",
                TypeInfo(str),
            ),
            (
                "compressed",
                "Compressed",
                TypeInfo(bool),
            ),
            (
                "number_of_buckets",
                "NumberOfBuckets",
                TypeInfo(int),
            ),
            (
                "serde_info",
                "SerdeInfo",
                TypeInfo(SerDeInfo),
            ),
            (
                "bucket_columns",
                "BucketColumns",
                TypeInfo(typing.List[str]),
            ),
            (
                "sort_columns",
                "SortColumns",
                TypeInfo(typing.List[Order]),
            ),
            (
                "parameters",
                "Parameters",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "skewed_info",
                "SkewedInfo",
                TypeInfo(SkewedInfo),
            ),
            (
                "stored_as_sub_directories",
                "StoredAsSubDirectories",
                TypeInfo(bool),
            ),
        ]

    # A list of the `Columns` in the table.
    columns: typing.List["Column"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The physical location of the table. By default this takes the form of the
    # warehouse location, followed by the database location in the warehouse,
    # followed by the table name.
    location: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The input format: `SequenceFileInputFormat` (binary), or `TextInputFormat`,
    # or a custom format.
    input_format: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The output format: `SequenceFileOutputFormat` (binary), or
    # `IgnoreKeyTextOutputFormat`, or a custom format.
    output_format: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # True if the data in the table is compressed, or False if not.
    compressed: bool = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Must be specified if the table contains any dimension columns.
    number_of_buckets: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Serialization/deserialization (SerDe) information.
    serde_info: "SerDeInfo" = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A list of reducer grouping columns, clustering columns, and bucketing
    # columns in the table.
    bucket_columns: typing.List[str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A list specifying the sort order of each bucket in the table.
    sort_columns: typing.List["Order"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # User-supplied properties in key-value form.
    parameters: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Information about values that appear very frequently in a column (skewed
    # values).
    skewed_info: "SkewedInfo" = dataclasses.field(default=ShapeBase.NOT_SET, )

    # True if the table data is stored in subdirectories, or False if not.
    stored_as_sub_directories: bool = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class Table(ShapeBase):
    """
    Represents a collection of related data organized in columns and rows.
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
                "database_name",
                "DatabaseName",
                TypeInfo(str),
            ),
            (
                "description",
                "Description",
                TypeInfo(str),
            ),
            (
                "owner",
                "Owner",
                TypeInfo(str),
            ),
            (
                "create_time",
                "CreateTime",
                TypeInfo(datetime.datetime),
            ),
            (
                "update_time",
                "UpdateTime",
                TypeInfo(datetime.datetime),
            ),
            (
                "last_access_time",
                "LastAccessTime",
                TypeInfo(datetime.datetime),
            ),
            (
                "last_analyzed_time",
                "LastAnalyzedTime",
                TypeInfo(datetime.datetime),
            ),
            (
                "retention",
                "Retention",
                TypeInfo(int),
            ),
            (
                "storage_descriptor",
                "StorageDescriptor",
                TypeInfo(StorageDescriptor),
            ),
            (
                "partition_keys",
                "PartitionKeys",
                TypeInfo(typing.List[Column]),
            ),
            (
                "view_original_text",
                "ViewOriginalText",
                TypeInfo(str),
            ),
            (
                "view_expanded_text",
                "ViewExpandedText",
                TypeInfo(str),
            ),
            (
                "table_type",
                "TableType",
                TypeInfo(str),
            ),
            (
                "parameters",
                "Parameters",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "created_by",
                "CreatedBy",
                TypeInfo(str),
            ),
        ]

    # Name of the table. For Hive compatibility, this must be entirely lowercase.
    name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Name of the metadata database where the table metadata resides. For Hive
    # compatibility, this must be all lowercase.
    database_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Description of the table.
    description: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Owner of the table.
    owner: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Time when the table definition was created in the Data Catalog.
    create_time: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Last time the table was updated.
    update_time: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Last time the table was accessed. This is usually taken from HDFS, and may
    # not be reliable.
    last_access_time: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Last time column statistics were computed for this table.
    last_analyzed_time: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Retention time for this table.
    retention: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A storage descriptor containing information about the physical storage of
    # this table.
    storage_descriptor: "StorageDescriptor" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A list of columns by which the table is partitioned. Only primitive types
    # are supported as partition keys.
    partition_keys: typing.List["Column"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # If the table is a view, the original text of the view; otherwise `null`.
    view_original_text: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # If the table is a view, the expanded text of the view; otherwise `null`.
    view_expanded_text: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The type of this table (`EXTERNAL_TABLE`, `VIRTUAL_VIEW`, etc.).
    table_type: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # These key-value pairs define properties associated with the table.
    parameters: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Person or entity who created the table.
    created_by: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class TableError(ShapeBase):
    """
    An error record for table operations.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "table_name",
                "TableName",
                TypeInfo(str),
            ),
            (
                "error_detail",
                "ErrorDetail",
                TypeInfo(ErrorDetail),
            ),
        ]

    # Name of the table. For Hive compatibility, this must be entirely lowercase.
    table_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Detail about the error.
    error_detail: "ErrorDetail" = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class TableInput(ShapeBase):
    """
    Structure used to create or update the table.
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
                "owner",
                "Owner",
                TypeInfo(str),
            ),
            (
                "last_access_time",
                "LastAccessTime",
                TypeInfo(datetime.datetime),
            ),
            (
                "last_analyzed_time",
                "LastAnalyzedTime",
                TypeInfo(datetime.datetime),
            ),
            (
                "retention",
                "Retention",
                TypeInfo(int),
            ),
            (
                "storage_descriptor",
                "StorageDescriptor",
                TypeInfo(StorageDescriptor),
            ),
            (
                "partition_keys",
                "PartitionKeys",
                TypeInfo(typing.List[Column]),
            ),
            (
                "view_original_text",
                "ViewOriginalText",
                TypeInfo(str),
            ),
            (
                "view_expanded_text",
                "ViewExpandedText",
                TypeInfo(str),
            ),
            (
                "table_type",
                "TableType",
                TypeInfo(str),
            ),
            (
                "parameters",
                "Parameters",
                TypeInfo(typing.Dict[str, str]),
            ),
        ]

    # Name of the table. For Hive compatibility, this is folded to lowercase when
    # it is stored.
    name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Description of the table.
    description: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Owner of the table.
    owner: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Last time the table was accessed.
    last_access_time: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Last time column statistics were computed for this table.
    last_analyzed_time: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Retention time for this table.
    retention: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A storage descriptor containing information about the physical storage of
    # this table.
    storage_descriptor: "StorageDescriptor" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A list of columns by which the table is partitioned. Only primitive types
    # are supported as partition keys.
    partition_keys: typing.List["Column"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # If the table is a view, the original text of the view; otherwise `null`.
    view_original_text: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # If the table is a view, the expanded text of the view; otherwise `null`.
    view_expanded_text: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The type of this table (`EXTERNAL_TABLE`, `VIRTUAL_VIEW`, etc.).
    table_type: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # These key-value pairs define properties associated with the table.
    parameters: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class TableVersion(ShapeBase):
    """
    Specifies a version of a table.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "table",
                "Table",
                TypeInfo(Table),
            ),
            (
                "version_id",
                "VersionId",
                TypeInfo(str),
            ),
        ]

    # The table in question
    table: "Table" = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The ID value that identifies this table version.
    version_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class TableVersionError(ShapeBase):
    """
    An error record for table-version operations.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "table_name",
                "TableName",
                TypeInfo(str),
            ),
            (
                "version_id",
                "VersionId",
                TypeInfo(str),
            ),
            (
                "error_detail",
                "ErrorDetail",
                TypeInfo(ErrorDetail),
            ),
        ]

    # The name of the table in question.
    table_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The ID value of the version in question.
    version_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Detail about the error.
    error_detail: "ErrorDetail" = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class Trigger(ShapeBase):
    """
    Information about a specific trigger.
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
                "id",
                "Id",
                TypeInfo(str),
            ),
            (
                "type",
                "Type",
                TypeInfo(typing.Union[str, TriggerType]),
            ),
            (
                "state",
                "State",
                TypeInfo(typing.Union[str, TriggerState]),
            ),
            (
                "description",
                "Description",
                TypeInfo(str),
            ),
            (
                "schedule",
                "Schedule",
                TypeInfo(str),
            ),
            (
                "actions",
                "Actions",
                TypeInfo(typing.List[Action]),
            ),
            (
                "predicate",
                "Predicate",
                TypeInfo(Predicate),
            ),
        ]

    # Name of the trigger.
    name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Reserved for future use.
    id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The type of trigger that this is.
    type: typing.Union[str, "TriggerType"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The current state of the trigger.
    state: typing.Union[str, "TriggerState"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A description of this trigger.
    description: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A `cron` expression used to specify the schedule (see [Time-Based Schedules
    # for Jobs and Crawlers](http://docs.aws.amazon.com/glue/latest/dg/monitor-
    # data-warehouse-schedule.html). For example, to run something every day at
    # 12:15 UTC, you would specify: `cron(15 12 * * ? *)`.
    schedule: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The actions initiated by this trigger.
    actions: typing.List["Action"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The predicate of this trigger, which defines when it will fire.
    predicate: "Predicate" = dataclasses.field(default=ShapeBase.NOT_SET, )


class TriggerState(str):
    CREATING = "CREATING"
    CREATED = "CREATED"
    ACTIVATING = "ACTIVATING"
    ACTIVATED = "ACTIVATED"
    DEACTIVATING = "DEACTIVATING"
    DEACTIVATED = "DEACTIVATED"
    DELETING = "DELETING"
    UPDATING = "UPDATING"


class TriggerType(str):
    SCHEDULED = "SCHEDULED"
    CONDITIONAL = "CONDITIONAL"
    ON_DEMAND = "ON_DEMAND"


@dataclasses.dataclass
class TriggerUpdate(ShapeBase):
    """
    A structure used to provide information used to update a trigger. This object
    will update the the previous trigger definition by overwriting it completely.
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
                "schedule",
                "Schedule",
                TypeInfo(str),
            ),
            (
                "actions",
                "Actions",
                TypeInfo(typing.List[Action]),
            ),
            (
                "predicate",
                "Predicate",
                TypeInfo(Predicate),
            ),
        ]

    # Reserved for future use.
    name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A description of this trigger.
    description: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A `cron` expression used to specify the schedule (see [Time-Based Schedules
    # for Jobs and Crawlers](http://docs.aws.amazon.com/glue/latest/dg/monitor-
    # data-warehouse-schedule.html). For example, to run something every day at
    # 12:15 UTC, you would specify: `cron(15 12 * * ? *)`.
    schedule: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The actions initiated by this trigger.
    actions: typing.List["Action"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The predicate of this trigger, which defines when it will fire.
    predicate: "Predicate" = dataclasses.field(default=ShapeBase.NOT_SET, )


class UpdateBehavior(str):
    LOG = "LOG"
    UPDATE_IN_DATABASE = "UPDATE_IN_DATABASE"


@dataclasses.dataclass
class UpdateClassifierRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "grok_classifier",
                "GrokClassifier",
                TypeInfo(UpdateGrokClassifierRequest),
            ),
            (
                "xml_classifier",
                "XMLClassifier",
                TypeInfo(UpdateXMLClassifierRequest),
            ),
            (
                "json_classifier",
                "JsonClassifier",
                TypeInfo(UpdateJsonClassifierRequest),
            ),
        ]

    # A `GrokClassifier` object with updated fields.
    grok_classifier: "UpdateGrokClassifierRequest" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # An `XMLClassifier` object with updated fields.
    xml_classifier: "UpdateXMLClassifierRequest" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A `JsonClassifier` object with updated fields.
    json_classifier: "UpdateJsonClassifierRequest" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class UpdateClassifierResponse(OutputShapeBase):
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
class UpdateConnectionRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "name",
                "Name",
                TypeInfo(str),
            ),
            (
                "connection_input",
                "ConnectionInput",
                TypeInfo(ConnectionInput),
            ),
            (
                "catalog_id",
                "CatalogId",
                TypeInfo(str),
            ),
        ]

    # The name of the connection definition to update.
    name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A `ConnectionInput` object that redefines the connection in question.
    connection_input: "ConnectionInput" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The ID of the Data Catalog in which the connection resides. If none is
    # supplied, the AWS account ID is used by default.
    catalog_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class UpdateConnectionResponse(OutputShapeBase):
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
class UpdateCrawlerRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "name",
                "Name",
                TypeInfo(str),
            ),
            (
                "role",
                "Role",
                TypeInfo(str),
            ),
            (
                "database_name",
                "DatabaseName",
                TypeInfo(str),
            ),
            (
                "description",
                "Description",
                TypeInfo(str),
            ),
            (
                "targets",
                "Targets",
                TypeInfo(CrawlerTargets),
            ),
            (
                "schedule",
                "Schedule",
                TypeInfo(str),
            ),
            (
                "classifiers",
                "Classifiers",
                TypeInfo(typing.List[str]),
            ),
            (
                "table_prefix",
                "TablePrefix",
                TypeInfo(str),
            ),
            (
                "schema_change_policy",
                "SchemaChangePolicy",
                TypeInfo(SchemaChangePolicy),
            ),
            (
                "configuration",
                "Configuration",
                TypeInfo(str),
            ),
            (
                "crawler_security_configuration",
                "CrawlerSecurityConfiguration",
                TypeInfo(str),
            ),
        ]

    # Name of the new crawler.
    name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The IAM role (or ARN of an IAM role) used by the new crawler to access
    # customer resources.
    role: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The AWS Glue database where results are stored, such as:
    # `arn:aws:daylight:us-east-1::database/sometable/*`.
    database_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A description of the new crawler.
    description: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A list of targets to crawl.
    targets: "CrawlerTargets" = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A `cron` expression used to specify the schedule (see [Time-Based Schedules
    # for Jobs and Crawlers](http://docs.aws.amazon.com/glue/latest/dg/monitor-
    # data-warehouse-schedule.html). For example, to run something every day at
    # 12:15 UTC, you would specify: `cron(15 12 * * ? *)`.
    schedule: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A list of custom classifiers that the user has registered. By default, all
    # built-in classifiers are included in a crawl, but these custom classifiers
    # always override the default classifiers for a given classification.
    classifiers: typing.List[str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The table prefix used for catalog tables that are created.
    table_prefix: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Policy for the crawler's update and deletion behavior.
    schema_change_policy: "SchemaChangePolicy" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Crawler configuration information. This versioned JSON string allows users
    # to specify aspects of a Crawler's behavior.

    # You can use this field to force partitions to inherit metadata such as
    # classification, input format, output format, serde information, and schema
    # from their parent table, rather than detect this information separately for
    # each partition. Use the following JSON string to specify that behavior:

    # Example: `'{ "Version": 1.0, "CrawlerOutput": { "Partitions": {
    # "AddOrUpdateBehavior": "InheritFromTable" } } }'`
    configuration: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The name of the SecurityConfiguration structure to be used by this Crawler.
    crawler_security_configuration: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class UpdateCrawlerResponse(OutputShapeBase):
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
class UpdateCrawlerScheduleRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "crawler_name",
                "CrawlerName",
                TypeInfo(str),
            ),
            (
                "schedule",
                "Schedule",
                TypeInfo(str),
            ),
        ]

    # Name of the crawler whose schedule to update.
    crawler_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The updated `cron` expression used to specify the schedule (see [Time-Based
    # Schedules for Jobs and
    # Crawlers](http://docs.aws.amazon.com/glue/latest/dg/monitor-data-warehouse-
    # schedule.html). For example, to run something every day at 12:15 UTC, you
    # would specify: `cron(15 12 * * ? *)`.
    schedule: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class UpdateCrawlerScheduleResponse(OutputShapeBase):
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
class UpdateDatabaseRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "name",
                "Name",
                TypeInfo(str),
            ),
            (
                "database_input",
                "DatabaseInput",
                TypeInfo(DatabaseInput),
            ),
            (
                "catalog_id",
                "CatalogId",
                TypeInfo(str),
            ),
        ]

    # The name of the database to update in the catalog. For Hive compatibility,
    # this is folded to lowercase.
    name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A `DatabaseInput` object specifying the new definition of the metadata
    # database in the catalog.
    database_input: "DatabaseInput" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The ID of the Data Catalog in which the metadata database resides. If none
    # is supplied, the AWS account ID is used by default.
    catalog_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class UpdateDatabaseResponse(OutputShapeBase):
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
class UpdateDevEndpointRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "endpoint_name",
                "EndpointName",
                TypeInfo(str),
            ),
            (
                "public_key",
                "PublicKey",
                TypeInfo(str),
            ),
            (
                "add_public_keys",
                "AddPublicKeys",
                TypeInfo(typing.List[str]),
            ),
            (
                "delete_public_keys",
                "DeletePublicKeys",
                TypeInfo(typing.List[str]),
            ),
            (
                "custom_libraries",
                "CustomLibraries",
                TypeInfo(DevEndpointCustomLibraries),
            ),
            (
                "update_etl_libraries",
                "UpdateEtlLibraries",
                TypeInfo(bool),
            ),
        ]

    # The name of the DevEndpoint to be updated.
    endpoint_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The public key for the DevEndpoint to use.
    public_key: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The list of public keys for the DevEndpoint to use.
    add_public_keys: typing.List[str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The list of public keys to be deleted from the DevEndpoint.
    delete_public_keys: typing.List[str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Custom Python or Java libraries to be loaded in the DevEndpoint.
    custom_libraries: "DevEndpointCustomLibraries" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # True if the list of custom libraries to be loaded in the development
    # endpoint needs to be updated, or False otherwise.
    update_etl_libraries: bool = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class UpdateDevEndpointResponse(OutputShapeBase):
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
class UpdateGrokClassifierRequest(ShapeBase):
    """
    Specifies a grok classifier to update when passed to `UpdateClassifier`.
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
                "classification",
                "Classification",
                TypeInfo(str),
            ),
            (
                "grok_pattern",
                "GrokPattern",
                TypeInfo(str),
            ),
            (
                "custom_patterns",
                "CustomPatterns",
                TypeInfo(str),
            ),
        ]

    # The name of the `GrokClassifier`.
    name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # An identifier of the data format that the classifier matches, such as
    # Twitter, JSON, Omniture logs, Amazon CloudWatch Logs, and so on.
    classification: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The grok pattern used by this classifier.
    grok_pattern: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Optional custom grok patterns used by this classifier.
    custom_patterns: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class UpdateJobRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "job_name",
                "JobName",
                TypeInfo(str),
            ),
            (
                "job_update",
                "JobUpdate",
                TypeInfo(JobUpdate),
            ),
        ]

    # Name of the job definition to update.
    job_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Specifies the values with which to update the job definition.
    job_update: "JobUpdate" = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class UpdateJobResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "job_name",
                "JobName",
                TypeInfo(str),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Returns the name of the updated job definition.
    job_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class UpdateJsonClassifierRequest(ShapeBase):
    """
    Specifies a JSON classifier to be updated.
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
                "json_path",
                "JsonPath",
                TypeInfo(str),
            ),
        ]

    # The name of the classifier.
    name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A `JsonPath` string defining the JSON data for the classifier to classify.
    # AWS Glue supports a subset of JsonPath, as described in [Writing JsonPath
    # Custom Classifiers](https://docs.aws.amazon.com/glue/latest/dg/custom-
    # classifier.html#custom-classifier-json).
    json_path: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class UpdatePartitionRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "database_name",
                "DatabaseName",
                TypeInfo(str),
            ),
            (
                "table_name",
                "TableName",
                TypeInfo(str),
            ),
            (
                "partition_value_list",
                "PartitionValueList",
                TypeInfo(typing.List[str]),
            ),
            (
                "partition_input",
                "PartitionInput",
                TypeInfo(PartitionInput),
            ),
            (
                "catalog_id",
                "CatalogId",
                TypeInfo(str),
            ),
        ]

    # The name of the catalog database in which the table in question resides.
    database_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The name of the table where the partition to be updated is located.
    table_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A list of the values defining the partition.
    partition_value_list: typing.List[str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The new partition object to which to update the partition.
    partition_input: "PartitionInput" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The ID of the Data Catalog where the partition to be updated resides. If
    # none is supplied, the AWS account ID is used by default.
    catalog_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class UpdatePartitionResponse(OutputShapeBase):
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
class UpdateTableRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "database_name",
                "DatabaseName",
                TypeInfo(str),
            ),
            (
                "table_input",
                "TableInput",
                TypeInfo(TableInput),
            ),
            (
                "catalog_id",
                "CatalogId",
                TypeInfo(str),
            ),
            (
                "skip_archive",
                "SkipArchive",
                TypeInfo(bool),
            ),
        ]

    # The name of the catalog database in which the table resides. For Hive
    # compatibility, this name is entirely lowercase.
    database_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # An updated `TableInput` object to define the metadata table in the catalog.
    table_input: "TableInput" = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The ID of the Data Catalog where the table resides. If none is supplied,
    # the AWS account ID is used by default.
    catalog_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # By default, `UpdateTable` always creates an archived version of the table
    # before updating it. If `skipArchive` is set to true, however, `UpdateTable`
    # does not create the archived version.
    skip_archive: bool = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class UpdateTableResponse(OutputShapeBase):
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
class UpdateTriggerRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "name",
                "Name",
                TypeInfo(str),
            ),
            (
                "trigger_update",
                "TriggerUpdate",
                TypeInfo(TriggerUpdate),
            ),
        ]

    # The name of the trigger to update.
    name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The new values with which to update the trigger.
    trigger_update: "TriggerUpdate" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class UpdateTriggerResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "trigger",
                "Trigger",
                TypeInfo(Trigger),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The resulting trigger definition.
    trigger: "Trigger" = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class UpdateUserDefinedFunctionRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "database_name",
                "DatabaseName",
                TypeInfo(str),
            ),
            (
                "function_name",
                "FunctionName",
                TypeInfo(str),
            ),
            (
                "function_input",
                "FunctionInput",
                TypeInfo(UserDefinedFunctionInput),
            ),
            (
                "catalog_id",
                "CatalogId",
                TypeInfo(str),
            ),
        ]

    # The name of the catalog database where the function to be updated is
    # located.
    database_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The name of the function.
    function_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A `FunctionInput` object that re-defines the function in the Data Catalog.
    function_input: "UserDefinedFunctionInput" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The ID of the Data Catalog where the function to be updated is located. If
    # none is supplied, the AWS account ID is used by default.
    catalog_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class UpdateUserDefinedFunctionResponse(OutputShapeBase):
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
class UpdateXMLClassifierRequest(ShapeBase):
    """
    Specifies an XML classifier to be updated.
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
                "classification",
                "Classification",
                TypeInfo(str),
            ),
            (
                "row_tag",
                "RowTag",
                TypeInfo(str),
            ),
        ]

    # The name of the classifier.
    name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # An identifier of the data format that the classifier matches.
    classification: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The XML tag designating the element that contains each record in an XML
    # document being parsed. Note that this cannot identify a self-closing
    # element (closed by `/>`). An empty row element that contains only
    # attributes can be parsed as long as it ends with a closing tag (for
    # example, `<row item_a="A" item_b="B"></row>` is okay, but `<row item_a="A"
    # item_b="B" />` is not).
    row_tag: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class UserDefinedFunction(ShapeBase):
    """
    Represents the equivalent of a Hive user-defined function (`UDF`) definition.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "function_name",
                "FunctionName",
                TypeInfo(str),
            ),
            (
                "class_name",
                "ClassName",
                TypeInfo(str),
            ),
            (
                "owner_name",
                "OwnerName",
                TypeInfo(str),
            ),
            (
                "owner_type",
                "OwnerType",
                TypeInfo(typing.Union[str, PrincipalType]),
            ),
            (
                "create_time",
                "CreateTime",
                TypeInfo(datetime.datetime),
            ),
            (
                "resource_uris",
                "ResourceUris",
                TypeInfo(typing.List[ResourceUri]),
            ),
        ]

    # The name of the function.
    function_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The Java class that contains the function code.
    class_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The owner of the function.
    owner_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The owner type.
    owner_type: typing.Union[str, "PrincipalType"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The time at which the function was created.
    create_time: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The resource URIs for the function.
    resource_uris: typing.List["ResourceUri"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class UserDefinedFunctionInput(ShapeBase):
    """
    A structure used to create or updata a user-defined function.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "function_name",
                "FunctionName",
                TypeInfo(str),
            ),
            (
                "class_name",
                "ClassName",
                TypeInfo(str),
            ),
            (
                "owner_name",
                "OwnerName",
                TypeInfo(str),
            ),
            (
                "owner_type",
                "OwnerType",
                TypeInfo(typing.Union[str, PrincipalType]),
            ),
            (
                "resource_uris",
                "ResourceUris",
                TypeInfo(typing.List[ResourceUri]),
            ),
        ]

    # The name of the function.
    function_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The Java class that contains the function code.
    class_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The owner of the function.
    owner_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The owner type.
    owner_type: typing.Union[str, "PrincipalType"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The resource URIs for the function.
    resource_uris: typing.List["ResourceUri"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class ValidationException(ShapeBase):
    """
    A value could not be validated.
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

    # A message describing the problem.
    message: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class VersionMismatchException(ShapeBase):
    """
    There was a version conflict.
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

    # A message describing the problem.
    message: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class XMLClassifier(ShapeBase):
    """
    A classifier for `XML` content.
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
                "classification",
                "Classification",
                TypeInfo(str),
            ),
            (
                "creation_time",
                "CreationTime",
                TypeInfo(datetime.datetime),
            ),
            (
                "last_updated",
                "LastUpdated",
                TypeInfo(datetime.datetime),
            ),
            (
                "version",
                "Version",
                TypeInfo(int),
            ),
            (
                "row_tag",
                "RowTag",
                TypeInfo(str),
            ),
        ]

    # The name of the classifier.
    name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # An identifier of the data format that the classifier matches.
    classification: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The time this classifier was registered.
    creation_time: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The time this classifier was last updated.
    last_updated: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The version of this classifier.
    version: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The XML tag designating the element that contains each record in an XML
    # document being parsed. Note that this cannot identify a self-closing
    # element (closed by `/>`). An empty row element that contains only
    # attributes can be parsed as long as it ends with a closing tag (for
    # example, `<row item_a="A" item_b="B"></row>` is okay, but `<row item_a="A"
    # item_b="B" />` is not).
    row_tag: str = dataclasses.field(default=ShapeBase.NOT_SET, )
