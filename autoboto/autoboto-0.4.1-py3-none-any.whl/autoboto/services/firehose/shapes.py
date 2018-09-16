import datetime
import typing
from autoboto import ShapeBase, OutputShapeBase, TypeInfo
import botocore.response
import dataclasses


@dataclasses.dataclass
class BufferingHints(ShapeBase):
    """
    Describes hints for the buffering to perform before delivering data to the
    destination. These options are treated as hints, and therefore Kinesis Data
    Firehose might choose to use different values when it is optimal.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "size_in_m_bs",
                "SizeInMBs",
                TypeInfo(int),
            ),
            (
                "interval_in_seconds",
                "IntervalInSeconds",
                TypeInfo(int),
            ),
        ]

    # Buffer incoming data to the specified size, in MBs, before delivering it to
    # the destination. The default value is 5.

    # We recommend setting this parameter to a value greater than the amount of
    # data you typically ingest into the delivery stream in 10 seconds. For
    # example, if you typically ingest data at 1 MB/sec, the value should be 10
    # MB or higher.
    size_in_m_bs: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Buffer incoming data for the specified period of time, in seconds, before
    # delivering it to the destination. The default value is 300.
    interval_in_seconds: int = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class CloudWatchLoggingOptions(ShapeBase):
    """
    Describes the Amazon CloudWatch logging options for your delivery stream.
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
                "log_group_name",
                "LogGroupName",
                TypeInfo(str),
            ),
            (
                "log_stream_name",
                "LogStreamName",
                TypeInfo(str),
            ),
        ]

    # Enables or disables CloudWatch logging.
    enabled: bool = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The CloudWatch group name for logging. This value is required if CloudWatch
    # logging is enabled.
    log_group_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The CloudWatch log stream name for logging. This value is required if
    # CloudWatch logging is enabled.
    log_stream_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )


class CompressionFormat(str):
    UNCOMPRESSED = "UNCOMPRESSED"
    GZIP = "GZIP"
    ZIP = "ZIP"
    Snappy = "Snappy"


@dataclasses.dataclass
class ConcurrentModificationException(ShapeBase):
    """
    Another modification has already happened. Fetch **VersionId** again and use it
    to update the destination.
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

    # A message that provides information about the error.
    message: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class CopyCommand(ShapeBase):
    """
    Describes a `COPY` command for Amazon Redshift.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "data_table_name",
                "DataTableName",
                TypeInfo(str),
            ),
            (
                "data_table_columns",
                "DataTableColumns",
                TypeInfo(str),
            ),
            (
                "copy_options",
                "CopyOptions",
                TypeInfo(str),
            ),
        ]

    # The name of the target table. The table must already exist in the database.
    data_table_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A comma-separated list of column names.
    data_table_columns: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Optional parameters to use with the Amazon Redshift `COPY` command. For
    # more information, see the "Optional Parameters" section of [Amazon Redshift
    # COPY command](http://docs.aws.amazon.com/redshift/latest/dg/r_COPY.html).
    # Some possible examples that would apply to Kinesis Data Firehose are as
    # follows:

    # `delimiter '\t' lzop;` \- fields are delimited with "\t" (TAB character)
    # and compressed using lzop.

    # `delimiter '|'` \- fields are delimited with "|" (this is the default
    # delimiter).

    # `delimiter '|' escape` \- the delimiter should be escaped.

    # `fixedwidth
    # 'venueid:3,venuename:25,venuecity:12,venuestate:2,venueseats:6'` \- fields
    # are fixed width in the source, with each width specified after every column
    # in the table.

    # `JSON 's3://mybucket/jsonpaths.txt'` \- data is in JSON format, and the
    # path specified is the format of the data.

    # For more examples, see [Amazon Redshift COPY command
    # examples](http://docs.aws.amazon.com/redshift/latest/dg/r_COPY_command_examples.html).
    copy_options: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class CreateDeliveryStreamInput(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "delivery_stream_name",
                "DeliveryStreamName",
                TypeInfo(str),
            ),
            (
                "delivery_stream_type",
                "DeliveryStreamType",
                TypeInfo(typing.Union[str, DeliveryStreamType]),
            ),
            (
                "kinesis_stream_source_configuration",
                "KinesisStreamSourceConfiguration",
                TypeInfo(KinesisStreamSourceConfiguration),
            ),
            (
                "s3_destination_configuration",
                "S3DestinationConfiguration",
                TypeInfo(S3DestinationConfiguration),
            ),
            (
                "extended_s3_destination_configuration",
                "ExtendedS3DestinationConfiguration",
                TypeInfo(ExtendedS3DestinationConfiguration),
            ),
            (
                "redshift_destination_configuration",
                "RedshiftDestinationConfiguration",
                TypeInfo(RedshiftDestinationConfiguration),
            ),
            (
                "elasticsearch_destination_configuration",
                "ElasticsearchDestinationConfiguration",
                TypeInfo(ElasticsearchDestinationConfiguration),
            ),
            (
                "splunk_destination_configuration",
                "SplunkDestinationConfiguration",
                TypeInfo(SplunkDestinationConfiguration),
            ),
        ]

    # The name of the delivery stream. This name must be unique per AWS account
    # in the same AWS Region. If the delivery streams are in different accounts
    # or different Regions, you can have multiple delivery streams with the same
    # name.
    delivery_stream_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The delivery stream type. This parameter can be one of the following
    # values:

    #   * `DirectPut`: Provider applications access the delivery stream directly.

    #   * `KinesisStreamAsSource`: The delivery stream uses a Kinesis data stream as a source.
    delivery_stream_type: typing.Union[str, "DeliveryStreamType"
                                      ] = dataclasses.field(
                                          default=ShapeBase.NOT_SET,
                                      )

    # When a Kinesis data stream is used as the source for the delivery stream, a
    # KinesisStreamSourceConfiguration containing the Kinesis data stream Amazon
    # Resource Name (ARN) and the role ARN for the source stream.
    kinesis_stream_source_configuration: "KinesisStreamSourceConfiguration" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # [Deprecated] The destination in Amazon S3. You can specify only one
    # destination.
    s3_destination_configuration: "S3DestinationConfiguration" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The destination in Amazon S3. You can specify only one destination.
    extended_s3_destination_configuration: "ExtendedS3DestinationConfiguration" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The destination in Amazon Redshift. You can specify only one destination.
    redshift_destination_configuration: "RedshiftDestinationConfiguration" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The destination in Amazon ES. You can specify only one destination.
    elasticsearch_destination_configuration: "ElasticsearchDestinationConfiguration" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The destination in Splunk. You can specify only one destination.
    splunk_destination_configuration: "SplunkDestinationConfiguration" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class CreateDeliveryStreamOutput(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "delivery_stream_arn",
                "DeliveryStreamARN",
                TypeInfo(str),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The ARN of the delivery stream.
    delivery_stream_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )


class Data(botocore.response.StreamingBody):
    pass


@dataclasses.dataclass
class DataFormatConversionConfiguration(ShapeBase):
    """
    Specifies that you want Kinesis Data Firehose to convert data from the JSON
    format to the Parquet or ORC format before writing it to Amazon S3. Kinesis Data
    Firehose uses the serializer and deserializer that you specify, in addition to
    the column information from the AWS Glue table, to deserialize your input data
    from JSON and then serialize it to the Parquet or ORC format. For more
    information, see [Kinesis Data Firehose Record Format
    Conversion](https://docs.aws.amazon.com/firehose/latest/dev/record-format-
    conversion.html).
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "schema_configuration",
                "SchemaConfiguration",
                TypeInfo(SchemaConfiguration),
            ),
            (
                "input_format_configuration",
                "InputFormatConfiguration",
                TypeInfo(InputFormatConfiguration),
            ),
            (
                "output_format_configuration",
                "OutputFormatConfiguration",
                TypeInfo(OutputFormatConfiguration),
            ),
            (
                "enabled",
                "Enabled",
                TypeInfo(bool),
            ),
        ]

    # Specifies the AWS Glue Data Catalog table that contains the column
    # information.
    schema_configuration: "SchemaConfiguration" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Specifies the deserializer that you want Kinesis Data Firehose to use to
    # convert the format of your data from JSON.
    input_format_configuration: "InputFormatConfiguration" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Specifies the serializer that you want Kinesis Data Firehose to use to
    # convert the format of your data to the Parquet or ORC format.
    output_format_configuration: "OutputFormatConfiguration" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Defaults to `true`. Set it to `false` if you want to disable format
    # conversion while preserving the configuration details.
    enabled: bool = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DeleteDeliveryStreamInput(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "delivery_stream_name",
                "DeliveryStreamName",
                TypeInfo(str),
            ),
        ]

    # The name of the delivery stream.
    delivery_stream_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DeleteDeliveryStreamOutput(OutputShapeBase):
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
class DeliveryStreamDescription(ShapeBase):
    """
    Contains information about a delivery stream.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "delivery_stream_name",
                "DeliveryStreamName",
                TypeInfo(str),
            ),
            (
                "delivery_stream_arn",
                "DeliveryStreamARN",
                TypeInfo(str),
            ),
            (
                "delivery_stream_status",
                "DeliveryStreamStatus",
                TypeInfo(typing.Union[str, DeliveryStreamStatus]),
            ),
            (
                "delivery_stream_type",
                "DeliveryStreamType",
                TypeInfo(typing.Union[str, DeliveryStreamType]),
            ),
            (
                "version_id",
                "VersionId",
                TypeInfo(str),
            ),
            (
                "destinations",
                "Destinations",
                TypeInfo(typing.List[DestinationDescription]),
            ),
            (
                "has_more_destinations",
                "HasMoreDestinations",
                TypeInfo(bool),
            ),
            (
                "create_timestamp",
                "CreateTimestamp",
                TypeInfo(datetime.datetime),
            ),
            (
                "last_update_timestamp",
                "LastUpdateTimestamp",
                TypeInfo(datetime.datetime),
            ),
            (
                "source",
                "Source",
                TypeInfo(SourceDescription),
            ),
        ]

    # The name of the delivery stream.
    delivery_stream_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The Amazon Resource Name (ARN) of the delivery stream. For more
    # information, see [Amazon Resource Names (ARNs) and AWS Service
    # Namespaces](https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-
    # namespaces.html).
    delivery_stream_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The status of the delivery stream.
    delivery_stream_status: typing.Union[str, "DeliveryStreamStatus"
                                        ] = dataclasses.field(
                                            default=ShapeBase.NOT_SET,
                                        )

    # The delivery stream type. This can be one of the following values:

    #   * `DirectPut`: Provider applications access the delivery stream directly.

    #   * `KinesisStreamAsSource`: The delivery stream uses a Kinesis data stream as a source.
    delivery_stream_type: typing.Union[str, "DeliveryStreamType"
                                      ] = dataclasses.field(
                                          default=ShapeBase.NOT_SET,
                                      )

    # Each time the destination is updated for a delivery stream, the version ID
    # is changed, and the current version ID is required when updating the
    # destination. This is so that the service knows it is applying the changes
    # to the correct version of the delivery stream.
    version_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The destinations.
    destinations: typing.List["DestinationDescription"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Indicates whether there are more destinations available to list.
    has_more_destinations: bool = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The date and time that the delivery stream was created.
    create_timestamp: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The date and time that the delivery stream was last updated.
    last_update_timestamp: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # If the `DeliveryStreamType` parameter is `KinesisStreamAsSource`, a
    # SourceDescription object describing the source Kinesis data stream.
    source: "SourceDescription" = dataclasses.field(default=ShapeBase.NOT_SET, )


class DeliveryStreamStatus(str):
    CREATING = "CREATING"
    DELETING = "DELETING"
    ACTIVE = "ACTIVE"


class DeliveryStreamType(str):
    DirectPut = "DirectPut"
    KinesisStreamAsSource = "KinesisStreamAsSource"


@dataclasses.dataclass
class DescribeDeliveryStreamInput(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "delivery_stream_name",
                "DeliveryStreamName",
                TypeInfo(str),
            ),
            (
                "limit",
                "Limit",
                TypeInfo(int),
            ),
            (
                "exclusive_start_destination_id",
                "ExclusiveStartDestinationId",
                TypeInfo(str),
            ),
        ]

    # The name of the delivery stream.
    delivery_stream_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The limit on the number of destinations to return. You can have one
    # destination per delivery stream.
    limit: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The ID of the destination to start returning the destination information.
    # Kinesis Data Firehose supports one destination per delivery stream.
    exclusive_start_destination_id: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class DescribeDeliveryStreamOutput(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "delivery_stream_description",
                "DeliveryStreamDescription",
                TypeInfo(DeliveryStreamDescription),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Information about the delivery stream.
    delivery_stream_description: "DeliveryStreamDescription" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class Deserializer(ShapeBase):
    """
    The deserializer you want Kinesis Data Firehose to use for converting the input
    data from JSON. Kinesis Data Firehose then serializes the data to its final
    format using the Serializer. Kinesis Data Firehose supports two types of
    deserializers: the [Apache Hive JSON
    SerDe](https://cwiki.apache.org/confluence/display/Hive/LanguageManual+DDL#LanguageManualDDL-
    JSON) and the [OpenX JSON SerDe](https://github.com/rcongiu/Hive-JSON-Serde).
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "open_x_json_ser_de",
                "OpenXJsonSerDe",
                TypeInfo(OpenXJsonSerDe),
            ),
            (
                "hive_json_ser_de",
                "HiveJsonSerDe",
                TypeInfo(HiveJsonSerDe),
            ),
        ]

    # The OpenX SerDe. Used by Kinesis Data Firehose for deserializing data,
    # which means converting it from the JSON format in preparation for
    # serializing it to the Parquet or ORC format. This is one of two
    # deserializers you can choose, depending on which one offers the
    # functionality you need. The other option is the native Hive / HCatalog
    # JsonSerDe.
    open_x_json_ser_de: "OpenXJsonSerDe" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The native Hive / HCatalog JsonSerDe. Used by Kinesis Data Firehose for
    # deserializing data, which means converting it from the JSON format in
    # preparation for serializing it to the Parquet or ORC format. This is one of
    # two deserializers you can choose, depending on which one offers the
    # functionality you need. The other option is the OpenX SerDe.
    hive_json_ser_de: "HiveJsonSerDe" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class DestinationDescription(ShapeBase):
    """
    Describes the destination for a delivery stream.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "destination_id",
                "DestinationId",
                TypeInfo(str),
            ),
            (
                "s3_destination_description",
                "S3DestinationDescription",
                TypeInfo(S3DestinationDescription),
            ),
            (
                "extended_s3_destination_description",
                "ExtendedS3DestinationDescription",
                TypeInfo(ExtendedS3DestinationDescription),
            ),
            (
                "redshift_destination_description",
                "RedshiftDestinationDescription",
                TypeInfo(RedshiftDestinationDescription),
            ),
            (
                "elasticsearch_destination_description",
                "ElasticsearchDestinationDescription",
                TypeInfo(ElasticsearchDestinationDescription),
            ),
            (
                "splunk_destination_description",
                "SplunkDestinationDescription",
                TypeInfo(SplunkDestinationDescription),
            ),
        ]

    # The ID of the destination.
    destination_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # [Deprecated] The destination in Amazon S3.
    s3_destination_description: "S3DestinationDescription" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The destination in Amazon S3.
    extended_s3_destination_description: "ExtendedS3DestinationDescription" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The destination in Amazon Redshift.
    redshift_destination_description: "RedshiftDestinationDescription" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The destination in Amazon ES.
    elasticsearch_destination_description: "ElasticsearchDestinationDescription" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The destination in Splunk.
    splunk_destination_description: "SplunkDestinationDescription" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class ElasticsearchBufferingHints(ShapeBase):
    """
    Describes the buffering to perform before delivering data to the Amazon ES
    destination.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "interval_in_seconds",
                "IntervalInSeconds",
                TypeInfo(int),
            ),
            (
                "size_in_m_bs",
                "SizeInMBs",
                TypeInfo(int),
            ),
        ]

    # Buffer incoming data for the specified period of time, in seconds, before
    # delivering it to the destination. The default value is 300 (5 minutes).
    interval_in_seconds: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Buffer incoming data to the specified size, in MBs, before delivering it to
    # the destination. The default value is 5.

    # We recommend setting this parameter to a value greater than the amount of
    # data you typically ingest into the delivery stream in 10 seconds. For
    # example, if you typically ingest data at 1 MB/sec, the value should be 10
    # MB or higher.
    size_in_m_bs: int = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ElasticsearchDestinationConfiguration(ShapeBase):
    """
    Describes the configuration of a destination in Amazon ES.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "role_arn",
                "RoleARN",
                TypeInfo(str),
            ),
            (
                "domain_arn",
                "DomainARN",
                TypeInfo(str),
            ),
            (
                "index_name",
                "IndexName",
                TypeInfo(str),
            ),
            (
                "type_name",
                "TypeName",
                TypeInfo(str),
            ),
            (
                "s3_configuration",
                "S3Configuration",
                TypeInfo(S3DestinationConfiguration),
            ),
            (
                "index_rotation_period",
                "IndexRotationPeriod",
                TypeInfo(typing.Union[str, ElasticsearchIndexRotationPeriod]),
            ),
            (
                "buffering_hints",
                "BufferingHints",
                TypeInfo(ElasticsearchBufferingHints),
            ),
            (
                "retry_options",
                "RetryOptions",
                TypeInfo(ElasticsearchRetryOptions),
            ),
            (
                "s3_backup_mode",
                "S3BackupMode",
                TypeInfo(typing.Union[str, ElasticsearchS3BackupMode]),
            ),
            (
                "processing_configuration",
                "ProcessingConfiguration",
                TypeInfo(ProcessingConfiguration),
            ),
            (
                "cloud_watch_logging_options",
                "CloudWatchLoggingOptions",
                TypeInfo(CloudWatchLoggingOptions),
            ),
        ]

    # The Amazon Resource Name (ARN) of the IAM role to be assumed by Kinesis
    # Data Firehose for calling the Amazon ES Configuration API and for indexing
    # documents. For more information, see [Grant Kinesis Data Firehose Access to
    # an Amazon S3
    # Destination](http://docs.aws.amazon.com/firehose/latest/dev/controlling-
    # access.html#using-iam-s3) and [Amazon Resource Names (ARNs) and AWS Service
    # Namespaces](https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-
    # namespaces.html).
    role_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The ARN of the Amazon ES domain. The IAM role must have permissions for
    # `DescribeElasticsearchDomain`, `DescribeElasticsearchDomains`, and
    # `DescribeElasticsearchDomainConfig` after assuming the role specified in
    # **RoleARN**. For more information, see [Amazon Resource Names (ARNs) and
    # AWS Service Namespaces](https://docs.aws.amazon.com/general/latest/gr/aws-
    # arns-and-namespaces.html).
    domain_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The Elasticsearch index name.
    index_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The Elasticsearch type name. For Elasticsearch 6.x, there can be only one
    # type per index. If you try to specify a new type for an existing index that
    # already has another type, Kinesis Data Firehose returns an error during run
    # time.
    type_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The configuration for the backup Amazon S3 location.
    s3_configuration: "S3DestinationConfiguration" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The Elasticsearch index rotation period. Index rotation appends a time
    # stamp to the `IndexName` to facilitate the expiration of old data. For more
    # information, see [Index Rotation for the Amazon ES
    # Destination](http://docs.aws.amazon.com/firehose/latest/dev/basic-
    # deliver.html#es-index-rotation). The default value is `OneDay`.
    index_rotation_period: typing.Union[str, "ElasticsearchIndexRotationPeriod"
                                       ] = dataclasses.field(
                                           default=ShapeBase.NOT_SET,
                                       )

    # The buffering options. If no value is specified, the default values for
    # `ElasticsearchBufferingHints` are used.
    buffering_hints: "ElasticsearchBufferingHints" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The retry behavior in case Kinesis Data Firehose is unable to deliver
    # documents to Amazon ES. The default value is 300 (5 minutes).
    retry_options: "ElasticsearchRetryOptions" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Defines how documents should be delivered to Amazon S3. When it is set to
    # `FailedDocumentsOnly`, Kinesis Data Firehose writes any documents that
    # could not be indexed to the configured Amazon S3 destination, with
    # `elasticsearch-failed/` appended to the key prefix. When set to
    # `AllDocuments`, Kinesis Data Firehose delivers all incoming records to
    # Amazon S3, and also writes failed documents with `elasticsearch-failed/`
    # appended to the prefix. For more information, see [Amazon S3 Backup for the
    # Amazon ES
    # Destination](http://docs.aws.amazon.com/firehose/latest/dev/basic-
    # deliver.html#es-s3-backup). Default value is `FailedDocumentsOnly`.
    s3_backup_mode: typing.Union[str, "ElasticsearchS3BackupMode"
                                ] = dataclasses.field(
                                    default=ShapeBase.NOT_SET,
                                )

    # The data processing configuration.
    processing_configuration: "ProcessingConfiguration" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The Amazon CloudWatch logging options for your delivery stream.
    cloud_watch_logging_options: "CloudWatchLoggingOptions" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class ElasticsearchDestinationDescription(ShapeBase):
    """
    The destination description in Amazon ES.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "role_arn",
                "RoleARN",
                TypeInfo(str),
            ),
            (
                "domain_arn",
                "DomainARN",
                TypeInfo(str),
            ),
            (
                "index_name",
                "IndexName",
                TypeInfo(str),
            ),
            (
                "type_name",
                "TypeName",
                TypeInfo(str),
            ),
            (
                "index_rotation_period",
                "IndexRotationPeriod",
                TypeInfo(typing.Union[str, ElasticsearchIndexRotationPeriod]),
            ),
            (
                "buffering_hints",
                "BufferingHints",
                TypeInfo(ElasticsearchBufferingHints),
            ),
            (
                "retry_options",
                "RetryOptions",
                TypeInfo(ElasticsearchRetryOptions),
            ),
            (
                "s3_backup_mode",
                "S3BackupMode",
                TypeInfo(typing.Union[str, ElasticsearchS3BackupMode]),
            ),
            (
                "s3_destination_description",
                "S3DestinationDescription",
                TypeInfo(S3DestinationDescription),
            ),
            (
                "processing_configuration",
                "ProcessingConfiguration",
                TypeInfo(ProcessingConfiguration),
            ),
            (
                "cloud_watch_logging_options",
                "CloudWatchLoggingOptions",
                TypeInfo(CloudWatchLoggingOptions),
            ),
        ]

    # The Amazon Resource Name (ARN) of the AWS credentials. For more
    # information, see [Amazon Resource Names (ARNs) and AWS Service
    # Namespaces](https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-
    # namespaces.html).
    role_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The ARN of the Amazon ES domain. For more information, see [Amazon Resource
    # Names (ARNs) and AWS Service
    # Namespaces](https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-
    # namespaces.html).
    domain_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The Elasticsearch index name.
    index_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The Elasticsearch type name.
    type_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The Elasticsearch index rotation period
    index_rotation_period: typing.Union[str, "ElasticsearchIndexRotationPeriod"
                                       ] = dataclasses.field(
                                           default=ShapeBase.NOT_SET,
                                       )

    # The buffering options.
    buffering_hints: "ElasticsearchBufferingHints" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The Amazon ES retry options.
    retry_options: "ElasticsearchRetryOptions" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The Amazon S3 backup mode.
    s3_backup_mode: typing.Union[str, "ElasticsearchS3BackupMode"
                                ] = dataclasses.field(
                                    default=ShapeBase.NOT_SET,
                                )

    # The Amazon S3 destination.
    s3_destination_description: "S3DestinationDescription" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The data processing configuration.
    processing_configuration: "ProcessingConfiguration" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The Amazon CloudWatch logging options.
    cloud_watch_logging_options: "CloudWatchLoggingOptions" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class ElasticsearchDestinationUpdate(ShapeBase):
    """
    Describes an update for a destination in Amazon ES.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "role_arn",
                "RoleARN",
                TypeInfo(str),
            ),
            (
                "domain_arn",
                "DomainARN",
                TypeInfo(str),
            ),
            (
                "index_name",
                "IndexName",
                TypeInfo(str),
            ),
            (
                "type_name",
                "TypeName",
                TypeInfo(str),
            ),
            (
                "index_rotation_period",
                "IndexRotationPeriod",
                TypeInfo(typing.Union[str, ElasticsearchIndexRotationPeriod]),
            ),
            (
                "buffering_hints",
                "BufferingHints",
                TypeInfo(ElasticsearchBufferingHints),
            ),
            (
                "retry_options",
                "RetryOptions",
                TypeInfo(ElasticsearchRetryOptions),
            ),
            (
                "s3_update",
                "S3Update",
                TypeInfo(S3DestinationUpdate),
            ),
            (
                "processing_configuration",
                "ProcessingConfiguration",
                TypeInfo(ProcessingConfiguration),
            ),
            (
                "cloud_watch_logging_options",
                "CloudWatchLoggingOptions",
                TypeInfo(CloudWatchLoggingOptions),
            ),
        ]

    # The Amazon Resource Name (ARN) of the IAM role to be assumed by Kinesis
    # Data Firehose for calling the Amazon ES Configuration API and for indexing
    # documents. For more information, see [Grant Kinesis Data Firehose Access to
    # an Amazon S3
    # Destination](http://docs.aws.amazon.com/firehose/latest/dev/controlling-
    # access.html#using-iam-s3) and [Amazon Resource Names (ARNs) and AWS Service
    # Namespaces](https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-
    # namespaces.html).
    role_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The ARN of the Amazon ES domain. The IAM role must have permissions for
    # `DescribeElasticsearchDomain`, `DescribeElasticsearchDomains`, and
    # `DescribeElasticsearchDomainConfig` after assuming the IAM role specified
    # in **RoleARN**. For more information, see [Amazon Resource Names (ARNs) and
    # AWS Service Namespaces](https://docs.aws.amazon.com/general/latest/gr/aws-
    # arns-and-namespaces.html).
    domain_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The Elasticsearch index name.
    index_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The Elasticsearch type name. For Elasticsearch 6.x, there can be only one
    # type per index. If you try to specify a new type for an existing index that
    # already has another type, Kinesis Data Firehose returns an error during
    # runtime.
    type_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The Elasticsearch index rotation period. Index rotation appends a time
    # stamp to `IndexName` to facilitate the expiration of old data. For more
    # information, see [Index Rotation for the Amazon ES
    # Destination](http://docs.aws.amazon.com/firehose/latest/dev/basic-
    # deliver.html#es-index-rotation). Default value is `OneDay`.
    index_rotation_period: typing.Union[str, "ElasticsearchIndexRotationPeriod"
                                       ] = dataclasses.field(
                                           default=ShapeBase.NOT_SET,
                                       )

    # The buffering options. If no value is specified,
    # **ElasticsearchBufferingHints** object default values are used.
    buffering_hints: "ElasticsearchBufferingHints" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The retry behavior in case Kinesis Data Firehose is unable to deliver
    # documents to Amazon ES. The default value is 300 (5 minutes).
    retry_options: "ElasticsearchRetryOptions" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The Amazon S3 destination.
    s3_update: "S3DestinationUpdate" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The data processing configuration.
    processing_configuration: "ProcessingConfiguration" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The CloudWatch logging options for your delivery stream.
    cloud_watch_logging_options: "CloudWatchLoggingOptions" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


class ElasticsearchIndexRotationPeriod(str):
    NoRotation = "NoRotation"
    OneHour = "OneHour"
    OneDay = "OneDay"
    OneWeek = "OneWeek"
    OneMonth = "OneMonth"


@dataclasses.dataclass
class ElasticsearchRetryOptions(ShapeBase):
    """
    Configures retry behavior in case Kinesis Data Firehose is unable to deliver
    documents to Amazon ES.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "duration_in_seconds",
                "DurationInSeconds",
                TypeInfo(int),
            ),
        ]

    # After an initial failure to deliver to Amazon ES, the total amount of time
    # during which Kinesis Data Firehose retries delivery (including the first
    # attempt). After this time has elapsed, the failed documents are written to
    # Amazon S3. Default value is 300 seconds (5 minutes). A value of 0 (zero)
    # results in no retries.
    duration_in_seconds: int = dataclasses.field(default=ShapeBase.NOT_SET, )


class ElasticsearchS3BackupMode(str):
    FailedDocumentsOnly = "FailedDocumentsOnly"
    AllDocuments = "AllDocuments"


@dataclasses.dataclass
class EncryptionConfiguration(ShapeBase):
    """
    Describes the encryption for a destination in Amazon S3.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "no_encryption_config",
                "NoEncryptionConfig",
                TypeInfo(typing.Union[str, NoEncryptionConfig]),
            ),
            (
                "kms_encryption_config",
                "KMSEncryptionConfig",
                TypeInfo(KMSEncryptionConfig),
            ),
        ]

    # Specifically override existing encryption information to ensure that no
    # encryption is used.
    no_encryption_config: typing.Union[str, "NoEncryptionConfig"
                                      ] = dataclasses.field(
                                          default=ShapeBase.NOT_SET,
                                      )

    # The encryption key.
    kms_encryption_config: "KMSEncryptionConfig" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class ExtendedS3DestinationConfiguration(ShapeBase):
    """
    Describes the configuration of a destination in Amazon S3.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "role_arn",
                "RoleARN",
                TypeInfo(str),
            ),
            (
                "bucket_arn",
                "BucketARN",
                TypeInfo(str),
            ),
            (
                "prefix",
                "Prefix",
                TypeInfo(str),
            ),
            (
                "buffering_hints",
                "BufferingHints",
                TypeInfo(BufferingHints),
            ),
            (
                "compression_format",
                "CompressionFormat",
                TypeInfo(typing.Union[str, CompressionFormat]),
            ),
            (
                "encryption_configuration",
                "EncryptionConfiguration",
                TypeInfo(EncryptionConfiguration),
            ),
            (
                "cloud_watch_logging_options",
                "CloudWatchLoggingOptions",
                TypeInfo(CloudWatchLoggingOptions),
            ),
            (
                "processing_configuration",
                "ProcessingConfiguration",
                TypeInfo(ProcessingConfiguration),
            ),
            (
                "s3_backup_mode",
                "S3BackupMode",
                TypeInfo(typing.Union[str, S3BackupMode]),
            ),
            (
                "s3_backup_configuration",
                "S3BackupConfiguration",
                TypeInfo(S3DestinationConfiguration),
            ),
            (
                "data_format_conversion_configuration",
                "DataFormatConversionConfiguration",
                TypeInfo(DataFormatConversionConfiguration),
            ),
        ]

    # The Amazon Resource Name (ARN) of the AWS credentials. For more
    # information, see [Amazon Resource Names (ARNs) and AWS Service
    # Namespaces](https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-
    # namespaces.html).
    role_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The ARN of the S3 bucket. For more information, see [Amazon Resource Names
    # (ARNs) and AWS Service
    # Namespaces](https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-
    # namespaces.html).
    bucket_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The "YYYY/MM/DD/HH" time format prefix is automatically used for delivered
    # Amazon S3 files. You can specify an extra prefix to be added in front of
    # the time format prefix. If the prefix ends with a slash, it appears as a
    # folder in the S3 bucket. For more information, see [Amazon S3 Object Name
    # Format](http://docs.aws.amazon.com/firehose/latest/dev/basic-
    # deliver.html#s3-object-name) in the _Amazon Kinesis Data Firehose Developer
    # Guide_.
    prefix: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The buffering option.
    buffering_hints: "BufferingHints" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The compression format. If no value is specified, the default is
    # UNCOMPRESSED.
    compression_format: typing.Union[str, "CompressionFormat"
                                    ] = dataclasses.field(
                                        default=ShapeBase.NOT_SET,
                                    )

    # The encryption configuration. If no value is specified, the default is no
    # encryption.
    encryption_configuration: "EncryptionConfiguration" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The Amazon CloudWatch logging options for your delivery stream.
    cloud_watch_logging_options: "CloudWatchLoggingOptions" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The data processing configuration.
    processing_configuration: "ProcessingConfiguration" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The Amazon S3 backup mode.
    s3_backup_mode: typing.Union[str, "S3BackupMode"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The configuration for backup in Amazon S3.
    s3_backup_configuration: "S3DestinationConfiguration" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The serializer, deserializer, and schema for converting data from the JSON
    # format to the Parquet or ORC format before writing it to Amazon S3.
    data_format_conversion_configuration: "DataFormatConversionConfiguration" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class ExtendedS3DestinationDescription(ShapeBase):
    """
    Describes a destination in Amazon S3.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "role_arn",
                "RoleARN",
                TypeInfo(str),
            ),
            (
                "bucket_arn",
                "BucketARN",
                TypeInfo(str),
            ),
            (
                "buffering_hints",
                "BufferingHints",
                TypeInfo(BufferingHints),
            ),
            (
                "compression_format",
                "CompressionFormat",
                TypeInfo(typing.Union[str, CompressionFormat]),
            ),
            (
                "encryption_configuration",
                "EncryptionConfiguration",
                TypeInfo(EncryptionConfiguration),
            ),
            (
                "prefix",
                "Prefix",
                TypeInfo(str),
            ),
            (
                "cloud_watch_logging_options",
                "CloudWatchLoggingOptions",
                TypeInfo(CloudWatchLoggingOptions),
            ),
            (
                "processing_configuration",
                "ProcessingConfiguration",
                TypeInfo(ProcessingConfiguration),
            ),
            (
                "s3_backup_mode",
                "S3BackupMode",
                TypeInfo(typing.Union[str, S3BackupMode]),
            ),
            (
                "s3_backup_description",
                "S3BackupDescription",
                TypeInfo(S3DestinationDescription),
            ),
            (
                "data_format_conversion_configuration",
                "DataFormatConversionConfiguration",
                TypeInfo(DataFormatConversionConfiguration),
            ),
        ]

    # The Amazon Resource Name (ARN) of the AWS credentials. For more
    # information, see [Amazon Resource Names (ARNs) and AWS Service
    # Namespaces](https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-
    # namespaces.html).
    role_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The ARN of the S3 bucket. For more information, see [Amazon Resource Names
    # (ARNs) and AWS Service
    # Namespaces](https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-
    # namespaces.html).
    bucket_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The buffering option.
    buffering_hints: "BufferingHints" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The compression format. If no value is specified, the default is
    # `UNCOMPRESSED`.
    compression_format: typing.Union[str, "CompressionFormat"
                                    ] = dataclasses.field(
                                        default=ShapeBase.NOT_SET,
                                    )

    # The encryption configuration. If no value is specified, the default is no
    # encryption.
    encryption_configuration: "EncryptionConfiguration" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The "YYYY/MM/DD/HH" time format prefix is automatically used for delivered
    # Amazon S3 files. You can specify an extra prefix to be added in front of
    # the time format prefix. If the prefix ends with a slash, it appears as a
    # folder in the S3 bucket. For more information, see [Amazon S3 Object Name
    # Format](http://docs.aws.amazon.com/firehose/latest/dev/basic-
    # deliver.html#s3-object-name) in the _Amazon Kinesis Data Firehose Developer
    # Guide_.
    prefix: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The Amazon CloudWatch logging options for your delivery stream.
    cloud_watch_logging_options: "CloudWatchLoggingOptions" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The data processing configuration.
    processing_configuration: "ProcessingConfiguration" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The Amazon S3 backup mode.
    s3_backup_mode: typing.Union[str, "S3BackupMode"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The configuration for backup in Amazon S3.
    s3_backup_description: "S3DestinationDescription" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The serializer, deserializer, and schema for converting data from the JSON
    # format to the Parquet or ORC format before writing it to Amazon S3.
    data_format_conversion_configuration: "DataFormatConversionConfiguration" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class ExtendedS3DestinationUpdate(ShapeBase):
    """
    Describes an update for a destination in Amazon S3.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "role_arn",
                "RoleARN",
                TypeInfo(str),
            ),
            (
                "bucket_arn",
                "BucketARN",
                TypeInfo(str),
            ),
            (
                "prefix",
                "Prefix",
                TypeInfo(str),
            ),
            (
                "buffering_hints",
                "BufferingHints",
                TypeInfo(BufferingHints),
            ),
            (
                "compression_format",
                "CompressionFormat",
                TypeInfo(typing.Union[str, CompressionFormat]),
            ),
            (
                "encryption_configuration",
                "EncryptionConfiguration",
                TypeInfo(EncryptionConfiguration),
            ),
            (
                "cloud_watch_logging_options",
                "CloudWatchLoggingOptions",
                TypeInfo(CloudWatchLoggingOptions),
            ),
            (
                "processing_configuration",
                "ProcessingConfiguration",
                TypeInfo(ProcessingConfiguration),
            ),
            (
                "s3_backup_mode",
                "S3BackupMode",
                TypeInfo(typing.Union[str, S3BackupMode]),
            ),
            (
                "s3_backup_update",
                "S3BackupUpdate",
                TypeInfo(S3DestinationUpdate),
            ),
            (
                "data_format_conversion_configuration",
                "DataFormatConversionConfiguration",
                TypeInfo(DataFormatConversionConfiguration),
            ),
        ]

    # The Amazon Resource Name (ARN) of the AWS credentials. For more
    # information, see [Amazon Resource Names (ARNs) and AWS Service
    # Namespaces](https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-
    # namespaces.html).
    role_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The ARN of the S3 bucket. For more information, see [Amazon Resource Names
    # (ARNs) and AWS Service
    # Namespaces](https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-
    # namespaces.html).
    bucket_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The "YYYY/MM/DD/HH" time format prefix is automatically used for delivered
    # Amazon S3 files. You can specify an extra prefix to be added in front of
    # the time format prefix. If the prefix ends with a slash, it appears as a
    # folder in the S3 bucket. For more information, see [Amazon S3 Object Name
    # Format](http://docs.aws.amazon.com/firehose/latest/dev/basic-
    # deliver.html#s3-object-name) in the _Amazon Kinesis Data Firehose Developer
    # Guide_.
    prefix: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The buffering option.
    buffering_hints: "BufferingHints" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The compression format. If no value is specified, the default is
    # `UNCOMPRESSED`.
    compression_format: typing.Union[str, "CompressionFormat"
                                    ] = dataclasses.field(
                                        default=ShapeBase.NOT_SET,
                                    )

    # The encryption configuration. If no value is specified, the default is no
    # encryption.
    encryption_configuration: "EncryptionConfiguration" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The Amazon CloudWatch logging options for your delivery stream.
    cloud_watch_logging_options: "CloudWatchLoggingOptions" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The data processing configuration.
    processing_configuration: "ProcessingConfiguration" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Enables or disables Amazon S3 backup mode.
    s3_backup_mode: typing.Union[str, "S3BackupMode"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The Amazon S3 destination for backup.
    s3_backup_update: "S3DestinationUpdate" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The serializer, deserializer, and schema for converting data from the JSON
    # format to the Parquet or ORC format before writing it to Amazon S3.
    data_format_conversion_configuration: "DataFormatConversionConfiguration" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


class HECEndpointType(str):
    Raw = "Raw"
    Event = "Event"


@dataclasses.dataclass
class HiveJsonSerDe(ShapeBase):
    """
    The native Hive / HCatalog JsonSerDe. Used by Kinesis Data Firehose for
    deserializing data, which means converting it from the JSON format in
    preparation for serializing it to the Parquet or ORC format. This is one of two
    deserializers you can choose, depending on which one offers the functionality
    you need. The other option is the OpenX SerDe.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "timestamp_formats",
                "TimestampFormats",
                TypeInfo(typing.List[str]),
            ),
        ]

    # Indicates how you want Kinesis Data Firehose to parse the date and time
    # stamps that may be present in your input data JSON. To specify these format
    # strings, follow the pattern syntax of JodaTime's DateTimeFormat format
    # strings. For more information, see [Class
    # DateTimeFormat](https://www.joda.org/joda-
    # time/apidocs/org/joda/time/format/DateTimeFormat.html). You can also use
    # the special value `millis` to parse time stamps in epoch milliseconds. If
    # you don't specify a format, Kinesis Data Firehose uses
    # `java.sql.Timestamp::valueOf` by default.
    timestamp_formats: typing.List[str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class InputFormatConfiguration(ShapeBase):
    """
    Specifies the deserializer you want to use to convert the format of the input
    data.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "deserializer",
                "Deserializer",
                TypeInfo(Deserializer),
            ),
        ]

    # Specifies which deserializer to use. You can choose either the Apache Hive
    # JSON SerDe or the OpenX JSON SerDe. If both are non-null, the server
    # rejects the request.
    deserializer: "Deserializer" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class InvalidArgumentException(ShapeBase):
    """
    The specified input parameter has a value that is not valid.
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

    # A message that provides information about the error.
    message: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class KMSEncryptionConfig(ShapeBase):
    """
    Describes an encryption key for a destination in Amazon S3.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "awskms_key_arn",
                "AWSKMSKeyARN",
                TypeInfo(str),
            ),
        ]

    # The Amazon Resource Name (ARN) of the encryption key. Must belong to the
    # same AWS Region as the destination Amazon S3 bucket. For more information,
    # see [Amazon Resource Names (ARNs) and AWS Service
    # Namespaces](https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-
    # namespaces.html).
    awskms_key_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class KinesisStreamSourceConfiguration(ShapeBase):
    """
    The stream and role Amazon Resource Names (ARNs) for a Kinesis data stream used
    as the source for a delivery stream.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "kinesis_stream_arn",
                "KinesisStreamARN",
                TypeInfo(str),
            ),
            (
                "role_arn",
                "RoleARN",
                TypeInfo(str),
            ),
        ]

    # The ARN of the source Kinesis data stream. For more information, see
    # [Amazon Kinesis Data Streams ARN
    # Format](https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-
    # namespaces.html#arn-syntax-kinesis-streams).
    kinesis_stream_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The ARN of the role that provides access to the source Kinesis data stream.
    # For more information, see [AWS Identity and Access Management (IAM) ARN
    # Format](https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-
    # namespaces.html#arn-syntax-iam).
    role_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class KinesisStreamSourceDescription(ShapeBase):
    """
    Details about a Kinesis data stream used as the source for a Kinesis Data
    Firehose delivery stream.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "kinesis_stream_arn",
                "KinesisStreamARN",
                TypeInfo(str),
            ),
            (
                "role_arn",
                "RoleARN",
                TypeInfo(str),
            ),
            (
                "delivery_start_timestamp",
                "DeliveryStartTimestamp",
                TypeInfo(datetime.datetime),
            ),
        ]

    # The Amazon Resource Name (ARN) of the source Kinesis data stream. For more
    # information, see [Amazon Kinesis Data Streams ARN
    # Format](https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-
    # namespaces.html#arn-syntax-kinesis-streams).
    kinesis_stream_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The ARN of the role used by the source Kinesis data stream. For more
    # information, see [AWS Identity and Access Management (IAM) ARN
    # Format](https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-
    # namespaces.html#arn-syntax-iam).
    role_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Kinesis Data Firehose starts retrieving records from the Kinesis data
    # stream starting with this time stamp.
    delivery_start_timestamp: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class LimitExceededException(ShapeBase):
    """
    You have already reached the limit for a requested resource.
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

    # A message that provides information about the error.
    message: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ListDeliveryStreamsInput(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "limit",
                "Limit",
                TypeInfo(int),
            ),
            (
                "delivery_stream_type",
                "DeliveryStreamType",
                TypeInfo(typing.Union[str, DeliveryStreamType]),
            ),
            (
                "exclusive_start_delivery_stream_name",
                "ExclusiveStartDeliveryStreamName",
                TypeInfo(str),
            ),
        ]

    # The maximum number of delivery streams to list. The default value is 10.
    limit: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The delivery stream type. This can be one of the following values:

    #   * `DirectPut`: Provider applications access the delivery stream directly.

    #   * `KinesisStreamAsSource`: The delivery stream uses a Kinesis data stream as a source.

    # This parameter is optional. If this parameter is omitted, delivery streams
    # of all types are returned.
    delivery_stream_type: typing.Union[str, "DeliveryStreamType"
                                      ] = dataclasses.field(
                                          default=ShapeBase.NOT_SET,
                                      )

    # The name of the delivery stream to start the list with.
    exclusive_start_delivery_stream_name: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class ListDeliveryStreamsOutput(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "delivery_stream_names",
                "DeliveryStreamNames",
                TypeInfo(typing.List[str]),
            ),
            (
                "has_more_delivery_streams",
                "HasMoreDeliveryStreams",
                TypeInfo(bool),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The names of the delivery streams.
    delivery_stream_names: typing.List[str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Indicates whether there are more delivery streams available to list.
    has_more_delivery_streams: bool = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class ListTagsForDeliveryStreamInput(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "delivery_stream_name",
                "DeliveryStreamName",
                TypeInfo(str),
            ),
            (
                "exclusive_start_tag_key",
                "ExclusiveStartTagKey",
                TypeInfo(str),
            ),
            (
                "limit",
                "Limit",
                TypeInfo(int),
            ),
        ]

    # The name of the delivery stream whose tags you want to list.
    delivery_stream_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The key to use as the starting point for the list of tags. If you set this
    # parameter, `ListTagsForDeliveryStream` gets all tags that occur after
    # `ExclusiveStartTagKey`.
    exclusive_start_tag_key: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The number of tags to return. If this number is less than the total number
    # of tags associated with the delivery stream, `HasMoreTags` is set to `true`
    # in the response. To list additional tags, set `ExclusiveStartTagKey` to the
    # last key in the response.
    limit: int = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ListTagsForDeliveryStreamOutput(OutputShapeBase):
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
                TypeInfo(typing.List[Tag]),
            ),
            (
                "has_more_tags",
                "HasMoreTags",
                TypeInfo(bool),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A list of tags associated with `DeliveryStreamName`, starting with the
    # first tag after `ExclusiveStartTagKey` and up to the specified `Limit`.
    tags: typing.List["Tag"] = dataclasses.field(default=ShapeBase.NOT_SET, )

    # If this is `true` in the response, more tags are available. To list the
    # remaining tags, set `ExclusiveStartTagKey` to the key of the last tag
    # returned and call `ListTagsForDeliveryStream` again.
    has_more_tags: bool = dataclasses.field(default=ShapeBase.NOT_SET, )


class NoEncryptionConfig(str):
    NoEncryption = "NoEncryption"


@dataclasses.dataclass
class OpenXJsonSerDe(ShapeBase):
    """
    The OpenX SerDe. Used by Kinesis Data Firehose for deserializing data, which
    means converting it from the JSON format in preparation for serializing it to
    the Parquet or ORC format. This is one of two deserializers you can choose,
    depending on which one offers the functionality you need. The other option is
    the native Hive / HCatalog JsonSerDe.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "convert_dots_in_json_keys_to_underscores",
                "ConvertDotsInJsonKeysToUnderscores",
                TypeInfo(bool),
            ),
            (
                "case_insensitive",
                "CaseInsensitive",
                TypeInfo(bool),
            ),
            (
                "column_to_json_key_mappings",
                "ColumnToJsonKeyMappings",
                TypeInfo(typing.Dict[str, str]),
            ),
        ]

    # When set to `true`, specifies that the names of the keys include dots and
    # that you want Kinesis Data Firehose to replace them with underscores. This
    # is useful because Apache Hive does not allow dots in column names. For
    # example, if the JSON contains a key whose name is "a.b", you can define the
    # column name to be "a_b" when using this option.

    # The default is `false`.
    convert_dots_in_json_keys_to_underscores: bool = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # When set to `true`, which is the default, Kinesis Data Firehose converts
    # JSON keys to lowercase before deserializing them.
    case_insensitive: bool = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Maps column names to JSON keys that aren't identical to the column names.
    # This is useful when the JSON contains keys that are Hive keywords. For
    # example, `timestamp` is a Hive keyword. If you have a JSON key named
    # `timestamp`, set this parameter to `{"ts": "timestamp"}` to map this key to
    # a column named `ts`.
    column_to_json_key_mappings: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


class OrcCompression(str):
    NONE = "NONE"
    ZLIB = "ZLIB"
    SNAPPY = "SNAPPY"


class OrcFormatVersion(str):
    V0_11 = "V0_11"
    V0_12 = "V0_12"


@dataclasses.dataclass
class OrcSerDe(ShapeBase):
    """
    A serializer to use for converting data to the ORC format before storing it in
    Amazon S3. For more information, see [Apache ORC](https://orc.apache.org/docs/).
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "stripe_size_bytes",
                "StripeSizeBytes",
                TypeInfo(int),
            ),
            (
                "block_size_bytes",
                "BlockSizeBytes",
                TypeInfo(int),
            ),
            (
                "row_index_stride",
                "RowIndexStride",
                TypeInfo(int),
            ),
            (
                "enable_padding",
                "EnablePadding",
                TypeInfo(bool),
            ),
            (
                "padding_tolerance",
                "PaddingTolerance",
                TypeInfo(float),
            ),
            (
                "compression",
                "Compression",
                TypeInfo(typing.Union[str, OrcCompression]),
            ),
            (
                "bloom_filter_columns",
                "BloomFilterColumns",
                TypeInfo(typing.List[str]),
            ),
            (
                "bloom_filter_false_positive_probability",
                "BloomFilterFalsePositiveProbability",
                TypeInfo(float),
            ),
            (
                "dictionary_key_threshold",
                "DictionaryKeyThreshold",
                TypeInfo(float),
            ),
            (
                "format_version",
                "FormatVersion",
                TypeInfo(typing.Union[str, OrcFormatVersion]),
            ),
        ]

    # The number of bytes in each stripe. The default is 64 MiB and the minimum
    # is 8 MiB.
    stripe_size_bytes: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The Hadoop Distributed File System (HDFS) block size. This is useful if you
    # intend to copy the data from Amazon S3 to HDFS before querying. The default
    # is 256 MiB and the minimum is 64 MiB. Kinesis Data Firehose uses this value
    # for padding calculations.
    block_size_bytes: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The number of rows between index entries. The default is 10,000 and the
    # minimum is 1,000.
    row_index_stride: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Set this to `true` to indicate that you want stripes to be padded to the
    # HDFS block boundaries. This is useful if you intend to copy the data from
    # Amazon S3 to HDFS before querying. The default is `false`.
    enable_padding: bool = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A number between 0 and 1 that defines the tolerance for block padding as a
    # decimal fraction of stripe size. The default value is 0.05, which means 5
    # percent of stripe size.

    # For the default values of 64 MiB ORC stripes and 256 MiB HDFS blocks, the
    # default block padding tolerance of 5 percent reserves a maximum of 3.2 MiB
    # for padding within the 256 MiB block. In such a case, if the available size
    # within the block is more than 3.2 MiB, a new, smaller stripe is inserted to
    # fit within that space. This ensures that no stripe crosses block boundaries
    # and causes remote reads within a node-local task.

    # Kinesis Data Firehose ignores this parameter when OrcSerDe$EnablePadding is
    # `false`.
    padding_tolerance: float = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The compression code to use over data blocks. The default is `SNAPPY`.
    compression: typing.Union[str, "OrcCompression"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The column names for which you want Kinesis Data Firehose to create bloom
    # filters. The default is `null`.
    bloom_filter_columns: typing.List[str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The Bloom filter false positive probability (FPP). The lower the FPP, the
    # bigger the Bloom filter. The default value is 0.05, the minimum is 0, and
    # the maximum is 1.
    bloom_filter_false_positive_probability: float = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Represents the fraction of the total number of non-null rows. To turn off
    # dictionary encoding, set this fraction to a number that is less than the
    # number of distinct keys in a dictionary. To always use dictionary encoding,
    # set this threshold to 1.
    dictionary_key_threshold: float = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The version of the file to write. The possible values are `V0_11` and
    # `V0_12`. The default is `V0_12`.
    format_version: typing.Union[str, "OrcFormatVersion"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class OutputFormatConfiguration(ShapeBase):
    """
    Specifies the serializer that you want Kinesis Data Firehose to use to convert
    the format of your data before it writes it to Amazon S3.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "serializer",
                "Serializer",
                TypeInfo(Serializer),
            ),
        ]

    # Specifies which serializer to use. You can choose either the ORC SerDe or
    # the Parquet SerDe. If both are non-null, the server rejects the request.
    serializer: "Serializer" = dataclasses.field(default=ShapeBase.NOT_SET, )


class ParquetCompression(str):
    UNCOMPRESSED = "UNCOMPRESSED"
    GZIP = "GZIP"
    SNAPPY = "SNAPPY"


@dataclasses.dataclass
class ParquetSerDe(ShapeBase):
    """
    A serializer to use for converting data to the Parquet format before storing it
    in Amazon S3. For more information, see [Apache
    Parquet](https://parquet.apache.org/documentation/latest/).
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "block_size_bytes",
                "BlockSizeBytes",
                TypeInfo(int),
            ),
            (
                "page_size_bytes",
                "PageSizeBytes",
                TypeInfo(int),
            ),
            (
                "compression",
                "Compression",
                TypeInfo(typing.Union[str, ParquetCompression]),
            ),
            (
                "enable_dictionary_compression",
                "EnableDictionaryCompression",
                TypeInfo(bool),
            ),
            (
                "max_padding_bytes",
                "MaxPaddingBytes",
                TypeInfo(int),
            ),
            (
                "writer_version",
                "WriterVersion",
                TypeInfo(typing.Union[str, ParquetWriterVersion]),
            ),
        ]

    # The Hadoop Distributed File System (HDFS) block size. This is useful if you
    # intend to copy the data from Amazon S3 to HDFS before querying. The default
    # is 256 MiB and the minimum is 64 MiB. Kinesis Data Firehose uses this value
    # for padding calculations.
    block_size_bytes: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The Parquet page size. Column chunks are divided into pages. A page is
    # conceptually an indivisible unit (in terms of compression and encoding).
    # The minimum value is 64 KiB and the default is 1 MiB.
    page_size_bytes: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The compression code to use over data blocks. The possible values are
    # `UNCOMPRESSED`, `SNAPPY`, and `GZIP`, with the default being `SNAPPY`. Use
    # `SNAPPY` for higher decompression speed. Use `GZIP` if the compression
    # ration is more important than speed.
    compression: typing.Union[str, "ParquetCompression"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Indicates whether to enable dictionary compression.
    enable_dictionary_compression: bool = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The maximum amount of padding to apply. This is useful if you intend to
    # copy the data from Amazon S3 to HDFS before querying. The default is 0.
    max_padding_bytes: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Indicates the version of row format to output. The possible values are `V1`
    # and `V2`. The default is `V1`.
    writer_version: typing.Union[str, "ParquetWriterVersion"
                                ] = dataclasses.field(
                                    default=ShapeBase.NOT_SET,
                                )


class ParquetWriterVersion(str):
    V1 = "V1"
    V2 = "V2"


@dataclasses.dataclass
class ProcessingConfiguration(ShapeBase):
    """
    Describes a data processing configuration.
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
                "processors",
                "Processors",
                TypeInfo(typing.List[Processor]),
            ),
        ]

    # Enables or disables data processing.
    enabled: bool = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The data processors.
    processors: typing.List["Processor"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class Processor(ShapeBase):
    """
    Describes a data processor.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "type",
                "Type",
                TypeInfo(typing.Union[str, ProcessorType]),
            ),
            (
                "parameters",
                "Parameters",
                TypeInfo(typing.List[ProcessorParameter]),
            ),
        ]

    # The type of processor.
    type: typing.Union[str, "ProcessorType"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The processor parameters.
    parameters: typing.List["ProcessorParameter"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class ProcessorParameter(ShapeBase):
    """
    Describes the processor parameter.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "parameter_name",
                "ParameterName",
                TypeInfo(typing.Union[str, ProcessorParameterName]),
            ),
            (
                "parameter_value",
                "ParameterValue",
                TypeInfo(str),
            ),
        ]

    # The name of the parameter.
    parameter_name: typing.Union[str, "ProcessorParameterName"
                                ] = dataclasses.field(
                                    default=ShapeBase.NOT_SET,
                                )

    # The parameter value.
    parameter_value: str = dataclasses.field(default=ShapeBase.NOT_SET, )


class ProcessorParameterName(str):
    LambdaArn = "LambdaArn"
    NumberOfRetries = "NumberOfRetries"
    RoleArn = "RoleArn"
    BufferSizeInMBs = "BufferSizeInMBs"
    BufferIntervalInSeconds = "BufferIntervalInSeconds"


class ProcessorType(str):
    Lambda = "Lambda"


@dataclasses.dataclass
class PutRecordBatchInput(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "delivery_stream_name",
                "DeliveryStreamName",
                TypeInfo(str),
            ),
            (
                "records",
                "Records",
                TypeInfo(typing.List[Record]),
            ),
        ]

    # The name of the delivery stream.
    delivery_stream_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # One or more records.
    records: typing.List["Record"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class PutRecordBatchOutput(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "failed_put_count",
                "FailedPutCount",
                TypeInfo(int),
            ),
            (
                "request_responses",
                "RequestResponses",
                TypeInfo(typing.List[PutRecordBatchResponseEntry]),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The number of records that might have failed processing.
    failed_put_count: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The results array. For each record, the index of the response element is
    # the same as the index used in the request array.
    request_responses: typing.List["PutRecordBatchResponseEntry"
                                  ] = dataclasses.field(
                                      default=ShapeBase.NOT_SET,
                                  )


@dataclasses.dataclass
class PutRecordBatchResponseEntry(ShapeBase):
    """
    Contains the result for an individual record from a PutRecordBatch request. If
    the record is successfully added to your delivery stream, it receives a record
    ID. If the record fails to be added to your delivery stream, the result includes
    an error code and an error message.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "record_id",
                "RecordId",
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

    # The ID of the record.
    record_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The error code for an individual record result.
    error_code: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The error message for an individual record result.
    error_message: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class PutRecordInput(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "delivery_stream_name",
                "DeliveryStreamName",
                TypeInfo(str),
            ),
            (
                "record",
                "Record",
                TypeInfo(Record),
            ),
        ]

    # The name of the delivery stream.
    delivery_stream_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The record.
    record: "Record" = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class PutRecordOutput(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "record_id",
                "RecordId",
                TypeInfo(str),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The ID of the record.
    record_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class Record(ShapeBase):
    """
    The unit of data in a delivery stream.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "data",
                "Data",
                TypeInfo(typing.Any),
            ),
        ]

    # The data blob, which is base64-encoded when the blob is serialized. The
    # maximum size of the data blob, before base64-encoding, is 1,000 KB.
    data: typing.Any = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class RedshiftDestinationConfiguration(ShapeBase):
    """
    Describes the configuration of a destination in Amazon Redshift.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "role_arn",
                "RoleARN",
                TypeInfo(str),
            ),
            (
                "cluster_jdbcurl",
                "ClusterJDBCURL",
                TypeInfo(str),
            ),
            (
                "copy_command",
                "CopyCommand",
                TypeInfo(CopyCommand),
            ),
            (
                "username",
                "Username",
                TypeInfo(str),
            ),
            (
                "password",
                "Password",
                TypeInfo(str),
            ),
            (
                "s3_configuration",
                "S3Configuration",
                TypeInfo(S3DestinationConfiguration),
            ),
            (
                "retry_options",
                "RetryOptions",
                TypeInfo(RedshiftRetryOptions),
            ),
            (
                "processing_configuration",
                "ProcessingConfiguration",
                TypeInfo(ProcessingConfiguration),
            ),
            (
                "s3_backup_mode",
                "S3BackupMode",
                TypeInfo(typing.Union[str, RedshiftS3BackupMode]),
            ),
            (
                "s3_backup_configuration",
                "S3BackupConfiguration",
                TypeInfo(S3DestinationConfiguration),
            ),
            (
                "cloud_watch_logging_options",
                "CloudWatchLoggingOptions",
                TypeInfo(CloudWatchLoggingOptions),
            ),
        ]

    # The Amazon Resource Name (ARN) of the AWS credentials. For more
    # information, see [Amazon Resource Names (ARNs) and AWS Service
    # Namespaces](https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-
    # namespaces.html).
    role_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The database connection string.
    cluster_jdbcurl: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The `COPY` command.
    copy_command: "CopyCommand" = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The name of the user.
    username: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The user password.
    password: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The configuration for the intermediate Amazon S3 location from which Amazon
    # Redshift obtains data. Restrictions are described in the topic for
    # CreateDeliveryStream.

    # The compression formats `SNAPPY` or `ZIP` cannot be specified in
    # `RedshiftDestinationConfiguration.S3Configuration` because the Amazon
    # Redshift `COPY` operation that reads from the S3 bucket doesn't support
    # these compression formats.
    s3_configuration: "S3DestinationConfiguration" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The retry behavior in case Kinesis Data Firehose is unable to deliver
    # documents to Amazon Redshift. Default value is 3600 (60 minutes).
    retry_options: "RedshiftRetryOptions" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The data processing configuration.
    processing_configuration: "ProcessingConfiguration" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The Amazon S3 backup mode.
    s3_backup_mode: typing.Union[str, "RedshiftS3BackupMode"
                                ] = dataclasses.field(
                                    default=ShapeBase.NOT_SET,
                                )

    # The configuration for backup in Amazon S3.
    s3_backup_configuration: "S3DestinationConfiguration" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The CloudWatch logging options for your delivery stream.
    cloud_watch_logging_options: "CloudWatchLoggingOptions" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class RedshiftDestinationDescription(ShapeBase):
    """
    Describes a destination in Amazon Redshift.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "role_arn",
                "RoleARN",
                TypeInfo(str),
            ),
            (
                "cluster_jdbcurl",
                "ClusterJDBCURL",
                TypeInfo(str),
            ),
            (
                "copy_command",
                "CopyCommand",
                TypeInfo(CopyCommand),
            ),
            (
                "username",
                "Username",
                TypeInfo(str),
            ),
            (
                "s3_destination_description",
                "S3DestinationDescription",
                TypeInfo(S3DestinationDescription),
            ),
            (
                "retry_options",
                "RetryOptions",
                TypeInfo(RedshiftRetryOptions),
            ),
            (
                "processing_configuration",
                "ProcessingConfiguration",
                TypeInfo(ProcessingConfiguration),
            ),
            (
                "s3_backup_mode",
                "S3BackupMode",
                TypeInfo(typing.Union[str, RedshiftS3BackupMode]),
            ),
            (
                "s3_backup_description",
                "S3BackupDescription",
                TypeInfo(S3DestinationDescription),
            ),
            (
                "cloud_watch_logging_options",
                "CloudWatchLoggingOptions",
                TypeInfo(CloudWatchLoggingOptions),
            ),
        ]

    # The Amazon Resource Name (ARN) of the AWS credentials. For more
    # information, see [Amazon Resource Names (ARNs) and AWS Service
    # Namespaces](https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-
    # namespaces.html).
    role_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The database connection string.
    cluster_jdbcurl: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The `COPY` command.
    copy_command: "CopyCommand" = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The name of the user.
    username: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The Amazon S3 destination.
    s3_destination_description: "S3DestinationDescription" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The retry behavior in case Kinesis Data Firehose is unable to deliver
    # documents to Amazon Redshift. Default value is 3600 (60 minutes).
    retry_options: "RedshiftRetryOptions" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The data processing configuration.
    processing_configuration: "ProcessingConfiguration" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The Amazon S3 backup mode.
    s3_backup_mode: typing.Union[str, "RedshiftS3BackupMode"
                                ] = dataclasses.field(
                                    default=ShapeBase.NOT_SET,
                                )

    # The configuration for backup in Amazon S3.
    s3_backup_description: "S3DestinationDescription" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The Amazon CloudWatch logging options for your delivery stream.
    cloud_watch_logging_options: "CloudWatchLoggingOptions" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class RedshiftDestinationUpdate(ShapeBase):
    """
    Describes an update for a destination in Amazon Redshift.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "role_arn",
                "RoleARN",
                TypeInfo(str),
            ),
            (
                "cluster_jdbcurl",
                "ClusterJDBCURL",
                TypeInfo(str),
            ),
            (
                "copy_command",
                "CopyCommand",
                TypeInfo(CopyCommand),
            ),
            (
                "username",
                "Username",
                TypeInfo(str),
            ),
            (
                "password",
                "Password",
                TypeInfo(str),
            ),
            (
                "retry_options",
                "RetryOptions",
                TypeInfo(RedshiftRetryOptions),
            ),
            (
                "s3_update",
                "S3Update",
                TypeInfo(S3DestinationUpdate),
            ),
            (
                "processing_configuration",
                "ProcessingConfiguration",
                TypeInfo(ProcessingConfiguration),
            ),
            (
                "s3_backup_mode",
                "S3BackupMode",
                TypeInfo(typing.Union[str, RedshiftS3BackupMode]),
            ),
            (
                "s3_backup_update",
                "S3BackupUpdate",
                TypeInfo(S3DestinationUpdate),
            ),
            (
                "cloud_watch_logging_options",
                "CloudWatchLoggingOptions",
                TypeInfo(CloudWatchLoggingOptions),
            ),
        ]

    # The Amazon Resource Name (ARN) of the AWS credentials. For more
    # information, see [Amazon Resource Names (ARNs) and AWS Service
    # Namespaces](https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-
    # namespaces.html).
    role_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The database connection string.
    cluster_jdbcurl: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The `COPY` command.
    copy_command: "CopyCommand" = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The name of the user.
    username: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The user password.
    password: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The retry behavior in case Kinesis Data Firehose is unable to deliver
    # documents to Amazon Redshift. Default value is 3600 (60 minutes).
    retry_options: "RedshiftRetryOptions" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The Amazon S3 destination.

    # The compression formats `SNAPPY` or `ZIP` cannot be specified in
    # `RedshiftDestinationUpdate.S3Update` because the Amazon Redshift `COPY`
    # operation that reads from the S3 bucket doesn't support these compression
    # formats.
    s3_update: "S3DestinationUpdate" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The data processing configuration.
    processing_configuration: "ProcessingConfiguration" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The Amazon S3 backup mode.
    s3_backup_mode: typing.Union[str, "RedshiftS3BackupMode"
                                ] = dataclasses.field(
                                    default=ShapeBase.NOT_SET,
                                )

    # The Amazon S3 destination for backup.
    s3_backup_update: "S3DestinationUpdate" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The Amazon CloudWatch logging options for your delivery stream.
    cloud_watch_logging_options: "CloudWatchLoggingOptions" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class RedshiftRetryOptions(ShapeBase):
    """
    Configures retry behavior in case Kinesis Data Firehose is unable to deliver
    documents to Amazon Redshift.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "duration_in_seconds",
                "DurationInSeconds",
                TypeInfo(int),
            ),
        ]

    # The length of time during which Kinesis Data Firehose retries delivery
    # after a failure, starting from the initial request and including the first
    # attempt. The default value is 3600 seconds (60 minutes). Kinesis Data
    # Firehose does not retry if the value of `DurationInSeconds` is 0 (zero) or
    # if the first delivery attempt takes longer than the current value.
    duration_in_seconds: int = dataclasses.field(default=ShapeBase.NOT_SET, )


class RedshiftS3BackupMode(str):
    Disabled = "Disabled"
    Enabled = "Enabled"


@dataclasses.dataclass
class ResourceInUseException(ShapeBase):
    """
    The resource is already in use and not available for this operation.
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

    # A message that provides information about the error.
    message: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ResourceNotFoundException(ShapeBase):
    """
    The specified resource could not be found.
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

    # A message that provides information about the error.
    message: str = dataclasses.field(default=ShapeBase.NOT_SET, )


class S3BackupMode(str):
    Disabled = "Disabled"
    Enabled = "Enabled"


@dataclasses.dataclass
class S3DestinationConfiguration(ShapeBase):
    """
    Describes the configuration of a destination in Amazon S3.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "role_arn",
                "RoleARN",
                TypeInfo(str),
            ),
            (
                "bucket_arn",
                "BucketARN",
                TypeInfo(str),
            ),
            (
                "prefix",
                "Prefix",
                TypeInfo(str),
            ),
            (
                "buffering_hints",
                "BufferingHints",
                TypeInfo(BufferingHints),
            ),
            (
                "compression_format",
                "CompressionFormat",
                TypeInfo(typing.Union[str, CompressionFormat]),
            ),
            (
                "encryption_configuration",
                "EncryptionConfiguration",
                TypeInfo(EncryptionConfiguration),
            ),
            (
                "cloud_watch_logging_options",
                "CloudWatchLoggingOptions",
                TypeInfo(CloudWatchLoggingOptions),
            ),
        ]

    # The Amazon Resource Name (ARN) of the AWS credentials. For more
    # information, see [Amazon Resource Names (ARNs) and AWS Service
    # Namespaces](https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-
    # namespaces.html).
    role_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The ARN of the S3 bucket. For more information, see [Amazon Resource Names
    # (ARNs) and AWS Service
    # Namespaces](https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-
    # namespaces.html).
    bucket_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The "YYYY/MM/DD/HH" time format prefix is automatically used for delivered
    # Amazon S3 files. You can specify an extra prefix to be added in front of
    # the time format prefix. If the prefix ends with a slash, it appears as a
    # folder in the S3 bucket. For more information, see [Amazon S3 Object Name
    # Format](http://docs.aws.amazon.com/firehose/latest/dev/basic-
    # deliver.html#s3-object-name) in the _Amazon Kinesis Data Firehose Developer
    # Guide_.
    prefix: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The buffering option. If no value is specified, `BufferingHints` object
    # default values are used.
    buffering_hints: "BufferingHints" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The compression format. If no value is specified, the default is
    # `UNCOMPRESSED`.

    # The compression formats `SNAPPY` or `ZIP` cannot be specified for Amazon
    # Redshift destinations because they are not supported by the Amazon Redshift
    # `COPY` operation that reads from the S3 bucket.
    compression_format: typing.Union[str, "CompressionFormat"
                                    ] = dataclasses.field(
                                        default=ShapeBase.NOT_SET,
                                    )

    # The encryption configuration. If no value is specified, the default is no
    # encryption.
    encryption_configuration: "EncryptionConfiguration" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The CloudWatch logging options for your delivery stream.
    cloud_watch_logging_options: "CloudWatchLoggingOptions" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class S3DestinationDescription(ShapeBase):
    """
    Describes a destination in Amazon S3.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "role_arn",
                "RoleARN",
                TypeInfo(str),
            ),
            (
                "bucket_arn",
                "BucketARN",
                TypeInfo(str),
            ),
            (
                "buffering_hints",
                "BufferingHints",
                TypeInfo(BufferingHints),
            ),
            (
                "compression_format",
                "CompressionFormat",
                TypeInfo(typing.Union[str, CompressionFormat]),
            ),
            (
                "encryption_configuration",
                "EncryptionConfiguration",
                TypeInfo(EncryptionConfiguration),
            ),
            (
                "prefix",
                "Prefix",
                TypeInfo(str),
            ),
            (
                "cloud_watch_logging_options",
                "CloudWatchLoggingOptions",
                TypeInfo(CloudWatchLoggingOptions),
            ),
        ]

    # The Amazon Resource Name (ARN) of the AWS credentials. For more
    # information, see [Amazon Resource Names (ARNs) and AWS Service
    # Namespaces](https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-
    # namespaces.html).
    role_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The ARN of the S3 bucket. For more information, see [Amazon Resource Names
    # (ARNs) and AWS Service
    # Namespaces](https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-
    # namespaces.html).
    bucket_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The buffering option. If no value is specified, `BufferingHints` object
    # default values are used.
    buffering_hints: "BufferingHints" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The compression format. If no value is specified, the default is
    # `UNCOMPRESSED`.
    compression_format: typing.Union[str, "CompressionFormat"
                                    ] = dataclasses.field(
                                        default=ShapeBase.NOT_SET,
                                    )

    # The encryption configuration. If no value is specified, the default is no
    # encryption.
    encryption_configuration: "EncryptionConfiguration" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The "YYYY/MM/DD/HH" time format prefix is automatically used for delivered
    # Amazon S3 files. You can specify an extra prefix to be added in front of
    # the time format prefix. If the prefix ends with a slash, it appears as a
    # folder in the S3 bucket. For more information, see [Amazon S3 Object Name
    # Format](http://docs.aws.amazon.com/firehose/latest/dev/basic-
    # deliver.html#s3-object-name) in the _Amazon Kinesis Data Firehose Developer
    # Guide_.
    prefix: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The Amazon CloudWatch logging options for your delivery stream.
    cloud_watch_logging_options: "CloudWatchLoggingOptions" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class S3DestinationUpdate(ShapeBase):
    """
    Describes an update for a destination in Amazon S3.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "role_arn",
                "RoleARN",
                TypeInfo(str),
            ),
            (
                "bucket_arn",
                "BucketARN",
                TypeInfo(str),
            ),
            (
                "prefix",
                "Prefix",
                TypeInfo(str),
            ),
            (
                "buffering_hints",
                "BufferingHints",
                TypeInfo(BufferingHints),
            ),
            (
                "compression_format",
                "CompressionFormat",
                TypeInfo(typing.Union[str, CompressionFormat]),
            ),
            (
                "encryption_configuration",
                "EncryptionConfiguration",
                TypeInfo(EncryptionConfiguration),
            ),
            (
                "cloud_watch_logging_options",
                "CloudWatchLoggingOptions",
                TypeInfo(CloudWatchLoggingOptions),
            ),
        ]

    # The Amazon Resource Name (ARN) of the AWS credentials. For more
    # information, see [Amazon Resource Names (ARNs) and AWS Service
    # Namespaces](https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-
    # namespaces.html).
    role_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The ARN of the S3 bucket. For more information, see [Amazon Resource Names
    # (ARNs) and AWS Service
    # Namespaces](https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-
    # namespaces.html).
    bucket_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The "YYYY/MM/DD/HH" time format prefix is automatically used for delivered
    # Amazon S3 files. You can specify an extra prefix to be added in front of
    # the time format prefix. If the prefix ends with a slash, it appears as a
    # folder in the S3 bucket. For more information, see [Amazon S3 Object Name
    # Format](http://docs.aws.amazon.com/firehose/latest/dev/basic-
    # deliver.html#s3-object-name) in the _Amazon Kinesis Data Firehose Developer
    # Guide_.
    prefix: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The buffering option. If no value is specified, `BufferingHints` object
    # default values are used.
    buffering_hints: "BufferingHints" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The compression format. If no value is specified, the default is
    # `UNCOMPRESSED`.

    # The compression formats `SNAPPY` or `ZIP` cannot be specified for Amazon
    # Redshift destinations because they are not supported by the Amazon Redshift
    # `COPY` operation that reads from the S3 bucket.
    compression_format: typing.Union[str, "CompressionFormat"
                                    ] = dataclasses.field(
                                        default=ShapeBase.NOT_SET,
                                    )

    # The encryption configuration. If no value is specified, the default is no
    # encryption.
    encryption_configuration: "EncryptionConfiguration" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The CloudWatch logging options for your delivery stream.
    cloud_watch_logging_options: "CloudWatchLoggingOptions" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class SchemaConfiguration(ShapeBase):
    """
    Specifies the schema to which you want Kinesis Data Firehose to configure your
    data before it writes it to Amazon S3.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "role_arn",
                "RoleARN",
                TypeInfo(str),
            ),
            (
                "catalog_id",
                "CatalogId",
                TypeInfo(str),
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
                "region",
                "Region",
                TypeInfo(str),
            ),
            (
                "version_id",
                "VersionId",
                TypeInfo(str),
            ),
        ]

    # The role that Kinesis Data Firehose can use to access AWS Glue. This role
    # must be in the same account you use for Kinesis Data Firehose. Cross-
    # account roles aren't allowed.
    role_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The ID of the AWS Glue Data Catalog. If you don't supply this, the AWS
    # account ID is used by default.
    catalog_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Specifies the name of the AWS Glue database that contains the schema for
    # the output data.
    database_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Specifies the AWS Glue table that contains the column information that
    # constitutes your data schema.
    table_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # If you don't specify an AWS Region, the default is the current Region.
    region: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Specifies the table version for the output data schema. If you don't
    # specify this version ID, or if you set it to `LATEST`, Kinesis Data
    # Firehose uses the most recent version. This means that any updates to the
    # table are automatically picked up.
    version_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class Serializer(ShapeBase):
    """
    The serializer that you want Kinesis Data Firehose to use to convert data to the
    target format before writing it to Amazon S3. Kinesis Data Firehose supports two
    types of serializers: the [ORC
    SerDe](https://hive.apache.org/javadocs/r1.2.2/api/org/apache/hadoop/hive/ql/io/orc/OrcSerde.html)
    and the [Parquet
    SerDe](https://hive.apache.org/javadocs/r1.2.2/api/org/apache/hadoop/hive/ql/io/parquet/serde/ParquetHiveSerDe.html).
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "parquet_ser_de",
                "ParquetSerDe",
                TypeInfo(ParquetSerDe),
            ),
            (
                "orc_ser_de",
                "OrcSerDe",
                TypeInfo(OrcSerDe),
            ),
        ]

    # A serializer to use for converting data to the Parquet format before
    # storing it in Amazon S3. For more information, see [Apache
    # Parquet](https://parquet.apache.org/documentation/latest/).
    parquet_ser_de: "ParquetSerDe" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A serializer to use for converting data to the ORC format before storing it
    # in Amazon S3. For more information, see [Apache
    # ORC](https://orc.apache.org/docs/).
    orc_ser_de: "OrcSerDe" = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ServiceUnavailableException(ShapeBase):
    """
    The service is unavailable. Back off and retry the operation. If you continue to
    see the exception, throughput limits for the delivery stream may have been
    exceeded. For more information about limits and how to request an increase, see
    [Amazon Kinesis Data Firehose
    Limits](http://docs.aws.amazon.com/firehose/latest/dev/limits.html).
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

    # A message that provides information about the error.
    message: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class SourceDescription(ShapeBase):
    """
    Details about a Kinesis data stream used as the source for a Kinesis Data
    Firehose delivery stream.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "kinesis_stream_source_description",
                "KinesisStreamSourceDescription",
                TypeInfo(KinesisStreamSourceDescription),
            ),
        ]

    # The KinesisStreamSourceDescription value for the source Kinesis data
    # stream.
    kinesis_stream_source_description: "KinesisStreamSourceDescription" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class SplunkDestinationConfiguration(ShapeBase):
    """
    Describes the configuration of a destination in Splunk.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "hec_endpoint",
                "HECEndpoint",
                TypeInfo(str),
            ),
            (
                "hec_endpoint_type",
                "HECEndpointType",
                TypeInfo(typing.Union[str, HECEndpointType]),
            ),
            (
                "hec_token",
                "HECToken",
                TypeInfo(str),
            ),
            (
                "s3_configuration",
                "S3Configuration",
                TypeInfo(S3DestinationConfiguration),
            ),
            (
                "hec_acknowledgment_timeout_in_seconds",
                "HECAcknowledgmentTimeoutInSeconds",
                TypeInfo(int),
            ),
            (
                "retry_options",
                "RetryOptions",
                TypeInfo(SplunkRetryOptions),
            ),
            (
                "s3_backup_mode",
                "S3BackupMode",
                TypeInfo(typing.Union[str, SplunkS3BackupMode]),
            ),
            (
                "processing_configuration",
                "ProcessingConfiguration",
                TypeInfo(ProcessingConfiguration),
            ),
            (
                "cloud_watch_logging_options",
                "CloudWatchLoggingOptions",
                TypeInfo(CloudWatchLoggingOptions),
            ),
        ]

    # The HTTP Event Collector (HEC) endpoint to which Kinesis Data Firehose
    # sends your data.
    hec_endpoint: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # This type can be either "Raw" or "Event."
    hec_endpoint_type: typing.Union[str, "HECEndpointType"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # This is a GUID that you obtain from your Splunk cluster when you create a
    # new HEC endpoint.
    hec_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The configuration for the backup Amazon S3 location.
    s3_configuration: "S3DestinationConfiguration" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The amount of time that Kinesis Data Firehose waits to receive an
    # acknowledgment from Splunk after it sends it data. At the end of the
    # timeout period, Kinesis Data Firehose either tries to send the data again
    # or considers it an error, based on your retry settings.
    hec_acknowledgment_timeout_in_seconds: int = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The retry behavior in case Kinesis Data Firehose is unable to deliver data
    # to Splunk, or if it doesn't receive an acknowledgment of receipt from
    # Splunk.
    retry_options: "SplunkRetryOptions" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Defines how documents should be delivered to Amazon S3. When set to
    # `FailedDocumentsOnly`, Kinesis Data Firehose writes any data that could not
    # be indexed to the configured Amazon S3 destination. When set to
    # `AllDocuments`, Kinesis Data Firehose delivers all incoming records to
    # Amazon S3, and also writes failed documents to Amazon S3. Default value is
    # `FailedDocumentsOnly`.
    s3_backup_mode: typing.Union[str, "SplunkS3BackupMode"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The data processing configuration.
    processing_configuration: "ProcessingConfiguration" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The Amazon CloudWatch logging options for your delivery stream.
    cloud_watch_logging_options: "CloudWatchLoggingOptions" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class SplunkDestinationDescription(ShapeBase):
    """
    Describes a destination in Splunk.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "hec_endpoint",
                "HECEndpoint",
                TypeInfo(str),
            ),
            (
                "hec_endpoint_type",
                "HECEndpointType",
                TypeInfo(typing.Union[str, HECEndpointType]),
            ),
            (
                "hec_token",
                "HECToken",
                TypeInfo(str),
            ),
            (
                "hec_acknowledgment_timeout_in_seconds",
                "HECAcknowledgmentTimeoutInSeconds",
                TypeInfo(int),
            ),
            (
                "retry_options",
                "RetryOptions",
                TypeInfo(SplunkRetryOptions),
            ),
            (
                "s3_backup_mode",
                "S3BackupMode",
                TypeInfo(typing.Union[str, SplunkS3BackupMode]),
            ),
            (
                "s3_destination_description",
                "S3DestinationDescription",
                TypeInfo(S3DestinationDescription),
            ),
            (
                "processing_configuration",
                "ProcessingConfiguration",
                TypeInfo(ProcessingConfiguration),
            ),
            (
                "cloud_watch_logging_options",
                "CloudWatchLoggingOptions",
                TypeInfo(CloudWatchLoggingOptions),
            ),
        ]

    # The HTTP Event Collector (HEC) endpoint to which Kinesis Data Firehose
    # sends your data.
    hec_endpoint: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # This type can be either "Raw" or "Event."
    hec_endpoint_type: typing.Union[str, "HECEndpointType"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A GUID you obtain from your Splunk cluster when you create a new HEC
    # endpoint.
    hec_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The amount of time that Kinesis Data Firehose waits to receive an
    # acknowledgment from Splunk after it sends it data. At the end of the
    # timeout period, Kinesis Data Firehose either tries to send the data again
    # or considers it an error, based on your retry settings.
    hec_acknowledgment_timeout_in_seconds: int = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The retry behavior in case Kinesis Data Firehose is unable to deliver data
    # to Splunk or if it doesn't receive an acknowledgment of receipt from
    # Splunk.
    retry_options: "SplunkRetryOptions" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Defines how documents should be delivered to Amazon S3. When set to
    # `FailedDocumentsOnly`, Kinesis Data Firehose writes any data that could not
    # be indexed to the configured Amazon S3 destination. When set to
    # `AllDocuments`, Kinesis Data Firehose delivers all incoming records to
    # Amazon S3, and also writes failed documents to Amazon S3. Default value is
    # `FailedDocumentsOnly`.
    s3_backup_mode: typing.Union[str, "SplunkS3BackupMode"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The Amazon S3 destination.>
    s3_destination_description: "S3DestinationDescription" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The data processing configuration.
    processing_configuration: "ProcessingConfiguration" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The Amazon CloudWatch logging options for your delivery stream.
    cloud_watch_logging_options: "CloudWatchLoggingOptions" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class SplunkDestinationUpdate(ShapeBase):
    """
    Describes an update for a destination in Splunk.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "hec_endpoint",
                "HECEndpoint",
                TypeInfo(str),
            ),
            (
                "hec_endpoint_type",
                "HECEndpointType",
                TypeInfo(typing.Union[str, HECEndpointType]),
            ),
            (
                "hec_token",
                "HECToken",
                TypeInfo(str),
            ),
            (
                "hec_acknowledgment_timeout_in_seconds",
                "HECAcknowledgmentTimeoutInSeconds",
                TypeInfo(int),
            ),
            (
                "retry_options",
                "RetryOptions",
                TypeInfo(SplunkRetryOptions),
            ),
            (
                "s3_backup_mode",
                "S3BackupMode",
                TypeInfo(typing.Union[str, SplunkS3BackupMode]),
            ),
            (
                "s3_update",
                "S3Update",
                TypeInfo(S3DestinationUpdate),
            ),
            (
                "processing_configuration",
                "ProcessingConfiguration",
                TypeInfo(ProcessingConfiguration),
            ),
            (
                "cloud_watch_logging_options",
                "CloudWatchLoggingOptions",
                TypeInfo(CloudWatchLoggingOptions),
            ),
        ]

    # The HTTP Event Collector (HEC) endpoint to which Kinesis Data Firehose
    # sends your data.
    hec_endpoint: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # This type can be either "Raw" or "Event."
    hec_endpoint_type: typing.Union[str, "HECEndpointType"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A GUID that you obtain from your Splunk cluster when you create a new HEC
    # endpoint.
    hec_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The amount of time that Kinesis Data Firehose waits to receive an
    # acknowledgment from Splunk after it sends data. At the end of the timeout
    # period, Kinesis Data Firehose either tries to send the data again or
    # considers it an error, based on your retry settings.
    hec_acknowledgment_timeout_in_seconds: int = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The retry behavior in case Kinesis Data Firehose is unable to deliver data
    # to Splunk or if it doesn't receive an acknowledgment of receipt from
    # Splunk.
    retry_options: "SplunkRetryOptions" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Defines how documents should be delivered to Amazon S3. When set to
    # `FailedDocumentsOnly`, Kinesis Data Firehose writes any data that could not
    # be indexed to the configured Amazon S3 destination. When set to
    # `AllDocuments`, Kinesis Data Firehose delivers all incoming records to
    # Amazon S3, and also writes failed documents to Amazon S3. Default value is
    # `FailedDocumentsOnly`.
    s3_backup_mode: typing.Union[str, "SplunkS3BackupMode"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Your update to the configuration of the backup Amazon S3 location.
    s3_update: "S3DestinationUpdate" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The data processing configuration.
    processing_configuration: "ProcessingConfiguration" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The Amazon CloudWatch logging options for your delivery stream.
    cloud_watch_logging_options: "CloudWatchLoggingOptions" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class SplunkRetryOptions(ShapeBase):
    """
    Configures retry behavior in case Kinesis Data Firehose is unable to deliver
    documents to Splunk, or if it doesn't receive an acknowledgment from Splunk.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "duration_in_seconds",
                "DurationInSeconds",
                TypeInfo(int),
            ),
        ]

    # The total amount of time that Kinesis Data Firehose spends on retries. This
    # duration starts after the initial attempt to send data to Splunk fails. It
    # doesn't include the periods during which Kinesis Data Firehose waits for
    # acknowledgment from Splunk after each attempt.
    duration_in_seconds: int = dataclasses.field(default=ShapeBase.NOT_SET, )


class SplunkS3BackupMode(str):
    FailedEventsOnly = "FailedEventsOnly"
    AllEvents = "AllEvents"


@dataclasses.dataclass
class Tag(ShapeBase):
    """
    Metadata that you can assign to a delivery stream, consisting of a key-value
    pair.
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

    # A unique identifier for the tag. Maximum length: 128 characters. Valid
    # characters: Unicode letters, digits, white space, _ . / = + - % @
    key: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # An optional string, which you can use to describe or define the tag.
    # Maximum length: 256 characters. Valid characters: Unicode letters, digits,
    # white space, _ . / = + - % @
    value: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class TagDeliveryStreamInput(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "delivery_stream_name",
                "DeliveryStreamName",
                TypeInfo(str),
            ),
            (
                "tags",
                "Tags",
                TypeInfo(typing.List[Tag]),
            ),
        ]

    # The name of the delivery stream to which you want to add the tags.
    delivery_stream_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A set of key-value pairs to use to create the tags.
    tags: typing.List["Tag"] = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class TagDeliveryStreamOutput(OutputShapeBase):
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
class UntagDeliveryStreamInput(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "delivery_stream_name",
                "DeliveryStreamName",
                TypeInfo(str),
            ),
            (
                "tag_keys",
                "TagKeys",
                TypeInfo(typing.List[str]),
            ),
        ]

    # The name of the delivery stream.
    delivery_stream_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A list of tag keys. Each corresponding tag is removed from the delivery
    # stream.
    tag_keys: typing.List[str] = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class UntagDeliveryStreamOutput(OutputShapeBase):
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
class UpdateDestinationInput(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "delivery_stream_name",
                "DeliveryStreamName",
                TypeInfo(str),
            ),
            (
                "current_delivery_stream_version_id",
                "CurrentDeliveryStreamVersionId",
                TypeInfo(str),
            ),
            (
                "destination_id",
                "DestinationId",
                TypeInfo(str),
            ),
            (
                "s3_destination_update",
                "S3DestinationUpdate",
                TypeInfo(S3DestinationUpdate),
            ),
            (
                "extended_s3_destination_update",
                "ExtendedS3DestinationUpdate",
                TypeInfo(ExtendedS3DestinationUpdate),
            ),
            (
                "redshift_destination_update",
                "RedshiftDestinationUpdate",
                TypeInfo(RedshiftDestinationUpdate),
            ),
            (
                "elasticsearch_destination_update",
                "ElasticsearchDestinationUpdate",
                TypeInfo(ElasticsearchDestinationUpdate),
            ),
            (
                "splunk_destination_update",
                "SplunkDestinationUpdate",
                TypeInfo(SplunkDestinationUpdate),
            ),
        ]

    # The name of the delivery stream.
    delivery_stream_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Obtain this value from the **VersionId** result of
    # DeliveryStreamDescription. This value is required, and helps the service
    # perform conditional operations. For example, if there is an interleaving
    # update and this value is null, then the update destination fails. After the
    # update is successful, the `VersionId` value is updated. The service then
    # performs a merge of the old configuration with the new configuration.
    current_delivery_stream_version_id: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The ID of the destination.
    destination_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # [Deprecated] Describes an update for a destination in Amazon S3.
    s3_destination_update: "S3DestinationUpdate" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Describes an update for a destination in Amazon S3.
    extended_s3_destination_update: "ExtendedS3DestinationUpdate" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Describes an update for a destination in Amazon Redshift.
    redshift_destination_update: "RedshiftDestinationUpdate" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Describes an update for a destination in Amazon ES.
    elasticsearch_destination_update: "ElasticsearchDestinationUpdate" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Describes an update for a destination in Splunk.
    splunk_destination_update: "SplunkDestinationUpdate" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class UpdateDestinationOutput(OutputShapeBase):
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
