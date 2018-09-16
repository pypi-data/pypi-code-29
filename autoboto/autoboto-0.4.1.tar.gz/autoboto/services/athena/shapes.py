import datetime
import typing
from autoboto import ShapeBase, OutputShapeBase, TypeInfo
import dataclasses


@dataclasses.dataclass
class BatchGetNamedQueryInput(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "named_query_ids",
                "NamedQueryIds",
                TypeInfo(typing.List[str]),
            ),
        ]

    # An array of query IDs.
    named_query_ids: typing.List[str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class BatchGetNamedQueryOutput(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "named_queries",
                "NamedQueries",
                TypeInfo(typing.List[NamedQuery]),
            ),
            (
                "unprocessed_named_query_ids",
                "UnprocessedNamedQueryIds",
                TypeInfo(typing.List[UnprocessedNamedQueryId]),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Information about the named query IDs submitted.
    named_queries: typing.List["NamedQuery"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Information about provided query IDs.
    unprocessed_named_query_ids: typing.List["UnprocessedNamedQueryId"
                                            ] = dataclasses.field(
                                                default=ShapeBase.NOT_SET,
                                            )


@dataclasses.dataclass
class BatchGetQueryExecutionInput(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "query_execution_ids",
                "QueryExecutionIds",
                TypeInfo(typing.List[str]),
            ),
        ]

    # An array of query execution IDs.
    query_execution_ids: typing.List[str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class BatchGetQueryExecutionOutput(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "query_executions",
                "QueryExecutions",
                TypeInfo(typing.List[QueryExecution]),
            ),
            (
                "unprocessed_query_execution_ids",
                "UnprocessedQueryExecutionIds",
                TypeInfo(typing.List[UnprocessedQueryExecutionId]),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Information about a query execution.
    query_executions: typing.List["QueryExecution"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Information about the query executions that failed to run.
    unprocessed_query_execution_ids: typing.List["UnprocessedQueryExecutionId"
                                                ] = dataclasses.field(
                                                    default=ShapeBase.NOT_SET,
                                                )


@dataclasses.dataclass
class ColumnInfo(ShapeBase):
    """
    Information about the columns in a query execution result.
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
                "catalog_name",
                "CatalogName",
                TypeInfo(str),
            ),
            (
                "schema_name",
                "SchemaName",
                TypeInfo(str),
            ),
            (
                "table_name",
                "TableName",
                TypeInfo(str),
            ),
            (
                "label",
                "Label",
                TypeInfo(str),
            ),
            (
                "precision",
                "Precision",
                TypeInfo(int),
            ),
            (
                "scale",
                "Scale",
                TypeInfo(int),
            ),
            (
                "nullable",
                "Nullable",
                TypeInfo(typing.Union[str, ColumnNullable]),
            ),
            (
                "case_sensitive",
                "CaseSensitive",
                TypeInfo(bool),
            ),
        ]

    # The name of the column.
    name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The data type of the column.
    type: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The catalog to which the query results belong.
    catalog_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The schema name (database name) to which the query results belong.
    schema_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The table name for the query results.
    table_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A column label.
    label: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # For `DECIMAL` data types, specifies the total number of digits, up to 38.
    # For performance reasons, we recommend up to 18 digits.
    precision: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # For `DECIMAL` data types, specifies the total number of digits in the
    # fractional part of the value. Defaults to 0.
    scale: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Indicates the column's nullable status.
    nullable: typing.Union[str, "ColumnNullable"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Indicates whether values in the column are case-sensitive.
    case_sensitive: bool = dataclasses.field(default=ShapeBase.NOT_SET, )


class ColumnNullable(str):
    NOT_NULL = "NOT_NULL"
    NULLABLE = "NULLABLE"
    UNKNOWN = "UNKNOWN"


@dataclasses.dataclass
class CreateNamedQueryInput(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "name",
                "Name",
                TypeInfo(str),
            ),
            (
                "database",
                "Database",
                TypeInfo(str),
            ),
            (
                "query_string",
                "QueryString",
                TypeInfo(str),
            ),
            (
                "description",
                "Description",
                TypeInfo(str),
            ),
            (
                "client_request_token",
                "ClientRequestToken",
                TypeInfo(str),
            ),
        ]

    # The plain language name for the query.
    name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The database to which the query belongs.
    database: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The text of the query itself. In other words, all query statements.
    query_string: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A brief explanation of the query.
    description: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A unique case-sensitive string used to ensure the request to create the
    # query is idempotent (executes only once). If another `CreateNamedQuery`
    # request is received, the same response is returned and another query is not
    # created. If a parameter has changed, for example, the `QueryString`, an
    # error is returned.

    # This token is listed as not required because AWS SDKs (for example the AWS
    # SDK for Java) auto-generate the token for users. If you are not using the
    # AWS SDK or the AWS CLI, you must provide this token or the action will
    # fail.
    client_request_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class CreateNamedQueryOutput(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "named_query_id",
                "NamedQueryId",
                TypeInfo(str),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The unique ID of the query.
    named_query_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class Datum(ShapeBase):
    """
    A piece of data (a field in the table).
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "var_char_value",
                "VarCharValue",
                TypeInfo(str),
            ),
        ]

    # The value of the datum.
    var_char_value: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DeleteNamedQueryInput(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "named_query_id",
                "NamedQueryId",
                TypeInfo(str),
            ),
        ]

    # The unique ID of the query to delete.
    named_query_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DeleteNamedQueryOutput(OutputShapeBase):
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
class EncryptionConfiguration(ShapeBase):
    """
    If query results are encrypted in Amazon S3, indicates the Amazon S3 encryption
    option used.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "encryption_option",
                "EncryptionOption",
                TypeInfo(typing.Union[str, EncryptionOption]),
            ),
            (
                "kms_key",
                "KmsKey",
                TypeInfo(str),
            ),
        ]

    # Indicates whether Amazon S3 server-side encryption with Amazon S3-managed
    # keys (`SSE-S3`), server-side encryption with KMS-managed keys (`SSE-KMS`),
    # or client-side encryption with KMS-managed keys (CSE-KMS) is used.
    encryption_option: typing.Union[str, "EncryptionOption"
                                   ] = dataclasses.field(
                                       default=ShapeBase.NOT_SET,
                                   )

    # For `SSE-KMS` and `CSE-KMS`, this is the KMS key ARN or ID.
    kms_key: str = dataclasses.field(default=ShapeBase.NOT_SET, )


class EncryptionOption(str):
    SSE_S3 = "SSE_S3"
    SSE_KMS = "SSE_KMS"
    CSE_KMS = "CSE_KMS"


@dataclasses.dataclass
class GetNamedQueryInput(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "named_query_id",
                "NamedQueryId",
                TypeInfo(str),
            ),
        ]

    # The unique ID of the query. Use ListNamedQueries to get query IDs.
    named_query_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class GetNamedQueryOutput(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "named_query",
                "NamedQuery",
                TypeInfo(NamedQuery),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Information about the query.
    named_query: "NamedQuery" = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class GetQueryExecutionInput(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "query_execution_id",
                "QueryExecutionId",
                TypeInfo(str),
            ),
        ]

    # The unique ID of the query execution.
    query_execution_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class GetQueryExecutionOutput(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "query_execution",
                "QueryExecution",
                TypeInfo(QueryExecution),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Information about the query execution.
    query_execution: "QueryExecution" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class GetQueryResultsInput(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "query_execution_id",
                "QueryExecutionId",
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

    # The unique ID of the query execution.
    query_execution_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The token that specifies where to start pagination if a previous request
    # was truncated.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The maximum number of results (rows) to return in this request.
    max_results: int = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class GetQueryResultsOutput(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "result_set",
                "ResultSet",
                TypeInfo(ResultSet),
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

    # The results of the query execution.
    result_set: "ResultSet" = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A token to be used by the next request if this request is truncated.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    def paginate(self,
                ) -> typing.Generator["GetQueryResultsOutput", None, None]:
        yield from super()._paginate()


@dataclasses.dataclass
class InternalServerException(ShapeBase):
    """
    Indicates a platform issue, which may be due to a transient condition or outage.
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
    Indicates that something is wrong with the input to the request. For example, a
    required parameter may be missing or out of range.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "athena_error_code",
                "AthenaErrorCode",
                TypeInfo(str),
            ),
            (
                "message",
                "Message",
                TypeInfo(str),
            ),
        ]

    athena_error_code: str = dataclasses.field(default=ShapeBase.NOT_SET, )
    message: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ListNamedQueriesInput(ShapeBase):
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

    # The token that specifies where to start pagination if a previous request
    # was truncated.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The maximum number of queries to return in this request.
    max_results: int = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ListNamedQueriesOutput(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "named_query_ids",
                "NamedQueryIds",
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

    # The list of unique query IDs.
    named_query_ids: typing.List[str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A token to be used by the next request if this request is truncated.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    def paginate(self,
                ) -> typing.Generator["ListNamedQueriesOutput", None, None]:
        yield from super()._paginate()


@dataclasses.dataclass
class ListQueryExecutionsInput(ShapeBase):
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

    # The token that specifies where to start pagination if a previous request
    # was truncated.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The maximum number of query executions to return in this request.
    max_results: int = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ListQueryExecutionsOutput(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "query_execution_ids",
                "QueryExecutionIds",
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

    # The unique IDs of each query execution as an array of strings.
    query_execution_ids: typing.List[str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A token to be used by the next request if this request is truncated.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    def paginate(self,
                ) -> typing.Generator["ListQueryExecutionsOutput", None, None]:
        yield from super()._paginate()


@dataclasses.dataclass
class NamedQuery(ShapeBase):
    """
    A query, where `QueryString` is the SQL query statements that comprise the
    query.
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
                "database",
                "Database",
                TypeInfo(str),
            ),
            (
                "query_string",
                "QueryString",
                TypeInfo(str),
            ),
            (
                "description",
                "Description",
                TypeInfo(str),
            ),
            (
                "named_query_id",
                "NamedQueryId",
                TypeInfo(str),
            ),
        ]

    # The plain-language name of the query.
    name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The database to which the query belongs.
    database: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The SQL query statements that comprise the query.
    query_string: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A brief description of the query.
    description: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The unique identifier of the query.
    named_query_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class QueryExecution(ShapeBase):
    """
    Information about a single instance of a query execution.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "query_execution_id",
                "QueryExecutionId",
                TypeInfo(str),
            ),
            (
                "query",
                "Query",
                TypeInfo(str),
            ),
            (
                "result_configuration",
                "ResultConfiguration",
                TypeInfo(ResultConfiguration),
            ),
            (
                "query_execution_context",
                "QueryExecutionContext",
                TypeInfo(QueryExecutionContext),
            ),
            (
                "status",
                "Status",
                TypeInfo(QueryExecutionStatus),
            ),
            (
                "statistics",
                "Statistics",
                TypeInfo(QueryExecutionStatistics),
            ),
        ]

    # The unique identifier for each query execution.
    query_execution_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The SQL query statements which the query execution ran.
    query: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The location in Amazon S3 where query results were stored and the
    # encryption option, if any, used for query results.
    result_configuration: "ResultConfiguration" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The database in which the query execution occurred.
    query_execution_context: "QueryExecutionContext" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The completion date, current state, submission time, and state change
    # reason (if applicable) for the query execution.
    status: "QueryExecutionStatus" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The amount of data scanned during the query execution and the amount of
    # time that it took to execute.
    statistics: "QueryExecutionStatistics" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class QueryExecutionContext(ShapeBase):
    """
    The database in which the query execution occurs.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "database",
                "Database",
                TypeInfo(str),
            ),
        ]

    # The name of the database.
    database: str = dataclasses.field(default=ShapeBase.NOT_SET, )


class QueryExecutionState(str):
    QUEUED = "QUEUED"
    RUNNING = "RUNNING"
    SUCCEEDED = "SUCCEEDED"
    FAILED = "FAILED"
    CANCELLED = "CANCELLED"


@dataclasses.dataclass
class QueryExecutionStatistics(ShapeBase):
    """
    The amount of data scanned during the query execution and the amount of time
    that it took to execute.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "engine_execution_time_in_millis",
                "EngineExecutionTimeInMillis",
                TypeInfo(int),
            ),
            (
                "data_scanned_in_bytes",
                "DataScannedInBytes",
                TypeInfo(int),
            ),
        ]

    # The number of milliseconds that the query took to execute.
    engine_execution_time_in_millis: int = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The number of bytes in the data that was queried.
    data_scanned_in_bytes: int = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class QueryExecutionStatus(ShapeBase):
    """
    The completion date, current state, submission time, and state change reason (if
    applicable) for the query execution.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "state",
                "State",
                TypeInfo(typing.Union[str, QueryExecutionState]),
            ),
            (
                "state_change_reason",
                "StateChangeReason",
                TypeInfo(str),
            ),
            (
                "submission_date_time",
                "SubmissionDateTime",
                TypeInfo(datetime.datetime),
            ),
            (
                "completion_date_time",
                "CompletionDateTime",
                TypeInfo(datetime.datetime),
            ),
        ]

    # The state of query execution. `SUBMITTED` indicates that the query is
    # queued for execution. `RUNNING` indicates that the query is scanning data
    # and returning results. `SUCCEEDED` indicates that the query completed
    # without error. `FAILED` indicates that the query experienced an error and
    # did not complete processing. `CANCELLED` indicates that user input
    # interrupted query execution.
    state: typing.Union[str, "QueryExecutionState"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Further detail about the status of the query.
    state_change_reason: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The date and time that the query was submitted.
    submission_date_time: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The date and time that the query completed.
    completion_date_time: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class ResultConfiguration(ShapeBase):
    """
    The location in Amazon S3 where query results are stored and the encryption
    option, if any, used for query results.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "output_location",
                "OutputLocation",
                TypeInfo(str),
            ),
            (
                "encryption_configuration",
                "EncryptionConfiguration",
                TypeInfo(EncryptionConfiguration),
            ),
        ]

    # The location in S3 where query results are stored.
    output_location: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # If query results are encrypted in S3, indicates the S3 encryption option
    # used (for example, `SSE-KMS` or `CSE-KMS` and key information.
    encryption_configuration: "EncryptionConfiguration" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class ResultSet(ShapeBase):
    """
    The metadata and rows that comprise a query result set. The metadata describes
    the column structure and data types.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "rows",
                "Rows",
                TypeInfo(typing.List[Row]),
            ),
            (
                "result_set_metadata",
                "ResultSetMetadata",
                TypeInfo(ResultSetMetadata),
            ),
        ]

    # The rows in the table.
    rows: typing.List["Row"] = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The metadata that describes the column structure and data types of a table
    # of query results.
    result_set_metadata: "ResultSetMetadata" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class ResultSetMetadata(ShapeBase):
    """
    The metadata that describes the column structure and data types of a table of
    query results.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "column_info",
                "ColumnInfo",
                TypeInfo(typing.List[ColumnInfo]),
            ),
        ]

    # Information about the columns in a query execution result.
    column_info: typing.List["ColumnInfo"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class Row(ShapeBase):
    """
    The rows that comprise a query result table.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "data",
                "Data",
                TypeInfo(typing.List[Datum]),
            ),
        ]

    # The data that populates a row in a query result table.
    data: typing.List["Datum"] = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class StartQueryExecutionInput(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "query_string",
                "QueryString",
                TypeInfo(str),
            ),
            (
                "result_configuration",
                "ResultConfiguration",
                TypeInfo(ResultConfiguration),
            ),
            (
                "client_request_token",
                "ClientRequestToken",
                TypeInfo(str),
            ),
            (
                "query_execution_context",
                "QueryExecutionContext",
                TypeInfo(QueryExecutionContext),
            ),
        ]

    # The SQL query statements to be executed.
    query_string: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Specifies information about where and how to save the results of the query
    # execution.
    result_configuration: "ResultConfiguration" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A unique case-sensitive string used to ensure the request to create the
    # query is idempotent (executes only once). If another `StartQueryExecution`
    # request is received, the same response is returned and another query is not
    # created. If a parameter has changed, for example, the `QueryString`, an
    # error is returned.

    # This token is listed as not required because AWS SDKs (for example the AWS
    # SDK for Java) auto-generate the token for users. If you are not using the
    # AWS SDK or the AWS CLI, you must provide this token or the action will
    # fail.
    client_request_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The database within which the query executes.
    query_execution_context: "QueryExecutionContext" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class StartQueryExecutionOutput(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "query_execution_id",
                "QueryExecutionId",
                TypeInfo(str),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The unique ID of the query that ran as a result of this request.
    query_execution_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class StopQueryExecutionInput(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "query_execution_id",
                "QueryExecutionId",
                TypeInfo(str),
            ),
        ]

    # The unique ID of the query execution to stop.
    query_execution_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class StopQueryExecutionOutput(OutputShapeBase):
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


class ThrottleReason(str):
    CONCURRENT_QUERY_LIMIT_EXCEEDED = "CONCURRENT_QUERY_LIMIT_EXCEEDED"


@dataclasses.dataclass
class TooManyRequestsException(ShapeBase):
    """
    Indicates that the request was throttled.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "message",
                "Message",
                TypeInfo(str),
            ),
            (
                "reason",
                "Reason",
                TypeInfo(typing.Union[str, ThrottleReason]),
            ),
        ]

    message: str = dataclasses.field(default=ShapeBase.NOT_SET, )
    reason: typing.Union[str, "ThrottleReason"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class UnprocessedNamedQueryId(ShapeBase):
    """
    Information about a named query ID that could not be processed.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "named_query_id",
                "NamedQueryId",
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

    # The unique identifier of the named query.
    named_query_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The error code returned when the processing request for the named query
    # failed, if applicable.
    error_code: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The error message returned when the processing request for the named query
    # failed, if applicable.
    error_message: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class UnprocessedQueryExecutionId(ShapeBase):
    """
    Describes a query execution that failed to process.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "query_execution_id",
                "QueryExecutionId",
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

    # The unique identifier of the query execution.
    query_execution_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The error code returned when the query execution failed to process, if
    # applicable.
    error_code: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The error message returned when the query execution failed to process, if
    # applicable.
    error_message: str = dataclasses.field(default=ShapeBase.NOT_SET, )
