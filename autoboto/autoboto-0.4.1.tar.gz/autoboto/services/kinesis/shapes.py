import datetime
import typing
from autoboto import ShapeBase, OutputShapeBase, TypeInfo
import botocore.response
import dataclasses


@dataclasses.dataclass
class AddTagsToStreamInput(ShapeBase):
    """
    Represents the input for `AddTagsToStream`.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "stream_name",
                "StreamName",
                TypeInfo(str),
            ),
            (
                "tags",
                "Tags",
                TypeInfo(typing.Dict[str, str]),
            ),
        ]

    # The name of the stream.
    stream_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A set of up to 10 key-value pairs to use to create the tags.
    tags: typing.Dict[str, str] = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class Consumer(ShapeBase):
    """
    An object that represents the details of the consumer you registered.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "consumer_name",
                "ConsumerName",
                TypeInfo(str),
            ),
            (
                "consumer_arn",
                "ConsumerARN",
                TypeInfo(str),
            ),
            (
                "consumer_status",
                "ConsumerStatus",
                TypeInfo(typing.Union[str, ConsumerStatus]),
            ),
            (
                "consumer_creation_timestamp",
                "ConsumerCreationTimestamp",
                TypeInfo(datetime.datetime),
            ),
        ]

    # The name of the consumer is something you choose when you register the
    # consumer.
    consumer_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # When you register a consumer, Kinesis Data Streams generates an ARN for it.
    # You need this ARN to be able to call SubscribeToShard.

    # If you delete a consumer and then create a new one with the same name, it
    # won't have the same ARN. That's because consumer ARNs contain the creation
    # timestamp. This is important to keep in mind if you have IAM policies that
    # reference consumer ARNs.
    consumer_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A consumer can't read data while in the `CREATING` or `DELETING` states.
    consumer_status: typing.Union[str, "ConsumerStatus"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    consumer_creation_timestamp: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class ConsumerDescription(ShapeBase):
    """
    An object that represents the details of a registered consumer.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "consumer_name",
                "ConsumerName",
                TypeInfo(str),
            ),
            (
                "consumer_arn",
                "ConsumerARN",
                TypeInfo(str),
            ),
            (
                "consumer_status",
                "ConsumerStatus",
                TypeInfo(typing.Union[str, ConsumerStatus]),
            ),
            (
                "consumer_creation_timestamp",
                "ConsumerCreationTimestamp",
                TypeInfo(datetime.datetime),
            ),
            (
                "stream_arn",
                "StreamARN",
                TypeInfo(str),
            ),
        ]

    # The name of the consumer is something you choose when you register the
    # consumer.
    consumer_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # When you register a consumer, Kinesis Data Streams generates an ARN for it.
    # You need this ARN to be able to call SubscribeToShard.

    # If you delete a consumer and then create a new one with the same name, it
    # won't have the same ARN. That's because consumer ARNs contain the creation
    # timestamp. This is important to keep in mind if you have IAM policies that
    # reference consumer ARNs.
    consumer_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A consumer can't read data while in the `CREATING` or `DELETING` states.
    consumer_status: typing.Union[str, "ConsumerStatus"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    consumer_creation_timestamp: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The ARN of the stream with which you registered the consumer.
    stream_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )


class ConsumerStatus(str):
    CREATING = "CREATING"
    DELETING = "DELETING"
    ACTIVE = "ACTIVE"


@dataclasses.dataclass
class CreateStreamInput(ShapeBase):
    """
    Represents the input for `CreateStream`.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "stream_name",
                "StreamName",
                TypeInfo(str),
            ),
            (
                "shard_count",
                "ShardCount",
                TypeInfo(int),
            ),
        ]

    # A name to identify the stream. The stream name is scoped to the AWS account
    # used by the application that creates the stream. It is also scoped by AWS
    # Region. That is, two streams in two different AWS accounts can have the
    # same name. Two streams in the same AWS account but in two different Regions
    # can also have the same name.
    stream_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The number of shards that the stream will use. The throughput of the stream
    # is a function of the number of shards; more shards are required for greater
    # provisioned throughput.

    # DefaultShardLimit;
    shard_count: int = dataclasses.field(default=ShapeBase.NOT_SET, )


class Data(botocore.response.StreamingBody):
    pass


@dataclasses.dataclass
class DecreaseStreamRetentionPeriodInput(ShapeBase):
    """
    Represents the input for DecreaseStreamRetentionPeriod.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "stream_name",
                "StreamName",
                TypeInfo(str),
            ),
            (
                "retention_period_hours",
                "RetentionPeriodHours",
                TypeInfo(int),
            ),
        ]

    # The name of the stream to modify.
    stream_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The new retention period of the stream, in hours. Must be less than the
    # current retention period.
    retention_period_hours: int = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DeleteStreamInput(ShapeBase):
    """
    Represents the input for DeleteStream.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "stream_name",
                "StreamName",
                TypeInfo(str),
            ),
            (
                "enforce_consumer_deletion",
                "EnforceConsumerDeletion",
                TypeInfo(bool),
            ),
        ]

    # The name of the stream to delete.
    stream_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # If this parameter is unset (`null`) or if you set it to `false`, and the
    # stream has registered consumers, the call to `DeleteStream` fails with a
    # `ResourceInUseException`.
    enforce_consumer_deletion: bool = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class DeregisterStreamConsumerInput(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "stream_arn",
                "StreamARN",
                TypeInfo(str),
            ),
            (
                "consumer_name",
                "ConsumerName",
                TypeInfo(str),
            ),
            (
                "consumer_arn",
                "ConsumerARN",
                TypeInfo(str),
            ),
        ]

    # The ARN of the Kinesis data stream that the consumer is registered with.
    # For more information, see [Amazon Resource Names (ARNs) and AWS Service
    # Namespaces](https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-
    # namespaces.html#arn-syntax-kinesis-streams).
    stream_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The name that you gave to the consumer.
    consumer_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The ARN returned by Kinesis Data Streams when you registered the consumer.
    # If you don't know the ARN of the consumer that you want to deregister, you
    # can use the ListStreamConsumers operation to get a list of the descriptions
    # of all the consumers that are currently registered with a given data
    # stream. The description of a consumer contains its ARN.
    consumer_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DescribeLimitsInput(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class DescribeLimitsOutput(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "shard_limit",
                "ShardLimit",
                TypeInfo(int),
            ),
            (
                "open_shard_count",
                "OpenShardCount",
                TypeInfo(int),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The maximum number of shards.
    shard_limit: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The number of open shards.
    open_shard_count: int = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DescribeStreamConsumerInput(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "stream_arn",
                "StreamARN",
                TypeInfo(str),
            ),
            (
                "consumer_name",
                "ConsumerName",
                TypeInfo(str),
            ),
            (
                "consumer_arn",
                "ConsumerARN",
                TypeInfo(str),
            ),
        ]

    # The ARN of the Kinesis data stream that the consumer is registered with.
    # For more information, see [Amazon Resource Names (ARNs) and AWS Service
    # Namespaces](https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-
    # namespaces.html#arn-syntax-kinesis-streams).
    stream_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The name that you gave to the consumer.
    consumer_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The ARN returned by Kinesis Data Streams when you registered the consumer.
    consumer_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DescribeStreamConsumerOutput(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "consumer_description",
                "ConsumerDescription",
                TypeInfo(ConsumerDescription),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # An object that represents the details of the consumer.
    consumer_description: "ConsumerDescription" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class DescribeStreamInput(ShapeBase):
    """
    Represents the input for `DescribeStream`.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "stream_name",
                "StreamName",
                TypeInfo(str),
            ),
            (
                "limit",
                "Limit",
                TypeInfo(int),
            ),
            (
                "exclusive_start_shard_id",
                "ExclusiveStartShardId",
                TypeInfo(str),
            ),
        ]

    # The name of the stream to describe.
    stream_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The maximum number of shards to return in a single call. The default value
    # is 100. If you specify a value greater than 100, at most 100 shards are
    # returned.
    limit: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The shard ID of the shard to start with.
    exclusive_start_shard_id: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class DescribeStreamOutput(OutputShapeBase):
    """
    Represents the output for `DescribeStream`.
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
                "stream_description",
                "StreamDescription",
                TypeInfo(StreamDescription),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The current status of the stream, the stream Amazon Resource Name (ARN), an
    # array of shard objects that comprise the stream, and whether there are more
    # shards available.
    stream_description: "StreamDescription" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    def paginate(self,
                ) -> typing.Generator["DescribeStreamOutput", None, None]:
        yield from super()._paginate()


@dataclasses.dataclass
class DescribeStreamSummaryInput(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "stream_name",
                "StreamName",
                TypeInfo(str),
            ),
        ]

    # The name of the stream to describe.
    stream_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DescribeStreamSummaryOutput(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "stream_description_summary",
                "StreamDescriptionSummary",
                TypeInfo(StreamDescriptionSummary),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A StreamDescriptionSummary containing information about the stream.
    stream_description_summary: "StreamDescriptionSummary" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class DisableEnhancedMonitoringInput(ShapeBase):
    """
    Represents the input for DisableEnhancedMonitoring.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "stream_name",
                "StreamName",
                TypeInfo(str),
            ),
            (
                "shard_level_metrics",
                "ShardLevelMetrics",
                TypeInfo(typing.List[typing.Union[str, MetricsName]]),
            ),
        ]

    # The name of the Kinesis data stream for which to disable enhanced
    # monitoring.
    stream_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # List of shard-level metrics to disable.

    # The following are the valid shard-level metrics. The value "`ALL`" disables
    # every metric.

    #   * `IncomingBytes`

    #   * `IncomingRecords`

    #   * `OutgoingBytes`

    #   * `OutgoingRecords`

    #   * `WriteProvisionedThroughputExceeded`

    #   * `ReadProvisionedThroughputExceeded`

    #   * `IteratorAgeMilliseconds`

    #   * `ALL`

    # For more information, see [Monitoring the Amazon Kinesis Data Streams
    # Service with Amazon
    # CloudWatch](http://docs.aws.amazon.com/kinesis/latest/dev/monitoring-with-
    # cloudwatch.html) in the _Amazon Kinesis Data Streams Developer Guide_.
    shard_level_metrics: typing.List[typing.Union[str, "MetricsName"]
                                    ] = dataclasses.field(
                                        default=ShapeBase.NOT_SET,
                                    )


@dataclasses.dataclass
class EnableEnhancedMonitoringInput(ShapeBase):
    """
    Represents the input for EnableEnhancedMonitoring.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "stream_name",
                "StreamName",
                TypeInfo(str),
            ),
            (
                "shard_level_metrics",
                "ShardLevelMetrics",
                TypeInfo(typing.List[typing.Union[str, MetricsName]]),
            ),
        ]

    # The name of the stream for which to enable enhanced monitoring.
    stream_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # List of shard-level metrics to enable.

    # The following are the valid shard-level metrics. The value "`ALL`" enables
    # every metric.

    #   * `IncomingBytes`

    #   * `IncomingRecords`

    #   * `OutgoingBytes`

    #   * `OutgoingRecords`

    #   * `WriteProvisionedThroughputExceeded`

    #   * `ReadProvisionedThroughputExceeded`

    #   * `IteratorAgeMilliseconds`

    #   * `ALL`

    # For more information, see [Monitoring the Amazon Kinesis Data Streams
    # Service with Amazon
    # CloudWatch](http://docs.aws.amazon.com/kinesis/latest/dev/monitoring-with-
    # cloudwatch.html) in the _Amazon Kinesis Data Streams Developer Guide_.
    shard_level_metrics: typing.List[typing.Union[str, "MetricsName"]
                                    ] = dataclasses.field(
                                        default=ShapeBase.NOT_SET,
                                    )


class EncryptionType(str):
    NONE = "NONE"
    KMS = "KMS"


@dataclasses.dataclass
class EnhancedMetrics(ShapeBase):
    """
    Represents enhanced metrics types.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "shard_level_metrics",
                "ShardLevelMetrics",
                TypeInfo(typing.List[typing.Union[str, MetricsName]]),
            ),
        ]

    # List of shard-level metrics.

    # The following are the valid shard-level metrics. The value "`ALL`" enhances
    # every metric.

    #   * `IncomingBytes`

    #   * `IncomingRecords`

    #   * `OutgoingBytes`

    #   * `OutgoingRecords`

    #   * `WriteProvisionedThroughputExceeded`

    #   * `ReadProvisionedThroughputExceeded`

    #   * `IteratorAgeMilliseconds`

    #   * `ALL`

    # For more information, see [Monitoring the Amazon Kinesis Data Streams
    # Service with Amazon
    # CloudWatch](http://docs.aws.amazon.com/kinesis/latest/dev/monitoring-with-
    # cloudwatch.html) in the _Amazon Kinesis Data Streams Developer Guide_.
    shard_level_metrics: typing.List[typing.Union[str, "MetricsName"]
                                    ] = dataclasses.field(
                                        default=ShapeBase.NOT_SET,
                                    )


@dataclasses.dataclass
class EnhancedMonitoringOutput(OutputShapeBase):
    """
    Represents the output for EnableEnhancedMonitoring and
    DisableEnhancedMonitoring.
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
                "stream_name",
                "StreamName",
                TypeInfo(str),
            ),
            (
                "current_shard_level_metrics",
                "CurrentShardLevelMetrics",
                TypeInfo(typing.List[typing.Union[str, MetricsName]]),
            ),
            (
                "desired_shard_level_metrics",
                "DesiredShardLevelMetrics",
                TypeInfo(typing.List[typing.Union[str, MetricsName]]),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The name of the Kinesis data stream.
    stream_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Represents the current state of the metrics that are in the enhanced state
    # before the operation.
    current_shard_level_metrics: typing.List[typing.Union[str, "MetricsName"]
                                            ] = dataclasses.field(
                                                default=ShapeBase.NOT_SET,
                                            )

    # Represents the list of all the metrics that would be in the enhanced state
    # after the operation.
    desired_shard_level_metrics: typing.List[typing.Union[str, "MetricsName"]
                                            ] = dataclasses.field(
                                                default=ShapeBase.NOT_SET,
                                            )


@dataclasses.dataclass
class ExpiredIteratorException(ShapeBase):
    """
    The provided iterator exceeds the maximum age allowed.
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
class ExpiredNextTokenException(ShapeBase):
    """
    The pagination token passed to the operation is expired.
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
class GetRecordsInput(ShapeBase):
    """
    Represents the input for GetRecords.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "shard_iterator",
                "ShardIterator",
                TypeInfo(str),
            ),
            (
                "limit",
                "Limit",
                TypeInfo(int),
            ),
        ]

    # The position in the shard from which you want to start sequentially reading
    # data records. A shard iterator specifies this position using the sequence
    # number of a data record in the shard.
    shard_iterator: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The maximum number of records to return. Specify a value of up to 10,000.
    # If you specify a value that is greater than 10,000, GetRecords throws
    # `InvalidArgumentException`.
    limit: int = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class GetRecordsOutput(OutputShapeBase):
    """
    Represents the output for GetRecords.
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
                "records",
                "Records",
                TypeInfo(typing.List[Record]),
            ),
            (
                "next_shard_iterator",
                "NextShardIterator",
                TypeInfo(str),
            ),
            (
                "millis_behind_latest",
                "MillisBehindLatest",
                TypeInfo(int),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The data records retrieved from the shard.
    records: typing.List["Record"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The next position in the shard from which to start sequentially reading
    # data records. If set to `null`, the shard has been closed and the requested
    # iterator does not return any more data.
    next_shard_iterator: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The number of milliseconds the GetRecords response is from the tip of the
    # stream, indicating how far behind current time the consumer is. A value of
    # zero indicates that record processing is caught up, and there are no new
    # records to process at this moment.
    millis_behind_latest: int = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class GetShardIteratorInput(ShapeBase):
    """
    Represents the input for `GetShardIterator`.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "stream_name",
                "StreamName",
                TypeInfo(str),
            ),
            (
                "shard_id",
                "ShardId",
                TypeInfo(str),
            ),
            (
                "shard_iterator_type",
                "ShardIteratorType",
                TypeInfo(typing.Union[str, ShardIteratorType]),
            ),
            (
                "starting_sequence_number",
                "StartingSequenceNumber",
                TypeInfo(str),
            ),
            (
                "timestamp",
                "Timestamp",
                TypeInfo(datetime.datetime),
            ),
        ]

    # The name of the Amazon Kinesis data stream.
    stream_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The shard ID of the Kinesis Data Streams shard to get the iterator for.
    shard_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Determines how the shard iterator is used to start reading data records
    # from the shard.

    # The following are the valid Amazon Kinesis shard iterator types:

    #   * AT_SEQUENCE_NUMBER - Start reading from the position denoted by a specific sequence number, provided in the value `StartingSequenceNumber`.

    #   * AFTER_SEQUENCE_NUMBER - Start reading right after the position denoted by a specific sequence number, provided in the value `StartingSequenceNumber`.

    #   * AT_TIMESTAMP - Start reading from the position denoted by a specific time stamp, provided in the value `Timestamp`.

    #   * TRIM_HORIZON - Start reading at the last untrimmed record in the shard in the system, which is the oldest data record in the shard.

    #   * LATEST - Start reading just after the most recent record in the shard, so that you always read the most recent data in the shard.
    shard_iterator_type: typing.Union[str, "ShardIteratorType"
                                     ] = dataclasses.field(
                                         default=ShapeBase.NOT_SET,
                                     )

    # The sequence number of the data record in the shard from which to start
    # reading. Used with shard iterator type AT_SEQUENCE_NUMBER and
    # AFTER_SEQUENCE_NUMBER.
    starting_sequence_number: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The time stamp of the data record from which to start reading. Used with
    # shard iterator type AT_TIMESTAMP. A time stamp is the Unix epoch date with
    # precision in milliseconds. For example, `2016-04-04T19:58:46.480-00:00` or
    # `1459799926.480`. If a record with this exact time stamp does not exist,
    # the iterator returned is for the next (later) record. If the time stamp is
    # older than the current trim horizon, the iterator returned is for the
    # oldest untrimmed data record (TRIM_HORIZON).
    timestamp: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class GetShardIteratorOutput(OutputShapeBase):
    """
    Represents the output for `GetShardIterator`.
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
                "shard_iterator",
                "ShardIterator",
                TypeInfo(str),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The position in the shard from which to start reading data records
    # sequentially. A shard iterator specifies this position using the sequence
    # number of a data record in a shard.
    shard_iterator: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class HashKeyRange(ShapeBase):
    """
    The range of possible hash key values for the shard, which is a set of ordered
    contiguous positive integers.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "starting_hash_key",
                "StartingHashKey",
                TypeInfo(str),
            ),
            (
                "ending_hash_key",
                "EndingHashKey",
                TypeInfo(str),
            ),
        ]

    # The starting hash key of the hash key range.
    starting_hash_key: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The ending hash key of the hash key range.
    ending_hash_key: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class IncreaseStreamRetentionPeriodInput(ShapeBase):
    """
    Represents the input for IncreaseStreamRetentionPeriod.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "stream_name",
                "StreamName",
                TypeInfo(str),
            ),
            (
                "retention_period_hours",
                "RetentionPeriodHours",
                TypeInfo(int),
            ),
        ]

    # The name of the stream to modify.
    stream_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The new retention period of the stream, in hours. Must be more than the
    # current retention period.
    retention_period_hours: int = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class InternalFailureException(ShapeBase):
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
class InvalidArgumentException(ShapeBase):
    """
    A specified parameter exceeds its restrictions, is not supported, or can't be
    used. For more information, see the returned message.
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
class KMSAccessDeniedException(ShapeBase):
    """
    The ciphertext references a key that doesn't exist or that you don't have access
    to.
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
class KMSDisabledException(ShapeBase):
    """
    The request was rejected because the specified customer master key (CMK) isn't
    enabled.
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
class KMSInvalidStateException(ShapeBase):
    """
    The request was rejected because the state of the specified resource isn't valid
    for this request. For more information, see [How Key State Affects Use of a
    Customer Master Key](http://docs.aws.amazon.com/kms/latest/developerguide/key-
    state.html) in the _AWS Key Management Service Developer Guide_.
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
class KMSNotFoundException(ShapeBase):
    """
    The request was rejected because the specified entity or resource can't be
    found.
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
class KMSOptInRequired(ShapeBase):
    """
    The AWS access key ID needs a subscription for the service.
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
class KMSThrottlingException(ShapeBase):
    """
    The request was denied due to request throttling. For more information about
    throttling, see
    [Limits](http://docs.aws.amazon.com/kms/latest/developerguide/limits.html#requests-
    per-second) in the _AWS Key Management Service Developer Guide_.
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
class LimitExceededException(ShapeBase):
    """
    The requested resource exceeds the maximum number allowed, or the number of
    concurrent stream requests exceeds the maximum number allowed.
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
class ListShardsInput(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "stream_name",
                "StreamName",
                TypeInfo(str),
            ),
            (
                "next_token",
                "NextToken",
                TypeInfo(str),
            ),
            (
                "exclusive_start_shard_id",
                "ExclusiveStartShardId",
                TypeInfo(str),
            ),
            (
                "max_results",
                "MaxResults",
                TypeInfo(int),
            ),
            (
                "stream_creation_timestamp",
                "StreamCreationTimestamp",
                TypeInfo(datetime.datetime),
            ),
        ]

    # The name of the data stream whose shards you want to list.

    # You cannot specify this parameter if you specify the `NextToken` parameter.
    stream_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # When the number of shards in the data stream is greater than the default
    # value for the `MaxResults` parameter, or if you explicitly specify a value
    # for `MaxResults` that is less than the number of shards in the data stream,
    # the response includes a pagination token named `NextToken`. You can specify
    # this `NextToken` value in a subsequent call to `ListShards` to list the
    # next set of shards.

    # Don't specify `StreamName` or `StreamCreationTimestamp` if you specify
    # `NextToken` because the latter unambiguously identifies the stream.

    # You can optionally specify a value for the `MaxResults` parameter when you
    # specify `NextToken`. If you specify a `MaxResults` value that is less than
    # the number of shards that the operation returns if you don't specify
    # `MaxResults`, the response will contain a new `NextToken` value. You can
    # use the new `NextToken` value in a subsequent call to the `ListShards`
    # operation.

    # Tokens expire after 300 seconds. When you obtain a value for `NextToken` in
    # the response to a call to `ListShards`, you have 300 seconds to use that
    # value. If you specify an expired token in a call to `ListShards`, you get
    # `ExpiredNextTokenException`.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Specify this parameter to indicate that you want to list the shards
    # starting with the shard whose ID immediately follows
    # `ExclusiveStartShardId`.

    # If you don't specify this parameter, the default behavior is for
    # `ListShards` to list the shards starting with the first one in the stream.

    # You cannot specify this parameter if you specify `NextToken`.
    exclusive_start_shard_id: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The maximum number of shards to return in a single call to `ListShards`.
    # The minimum value you can specify for this parameter is 1, and the maximum
    # is 1,000, which is also the default.

    # When the number of shards to be listed is greater than the value of
    # `MaxResults`, the response contains a `NextToken` value that you can use in
    # a subsequent call to `ListShards` to list the next set of shards.
    max_results: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Specify this input parameter to distinguish data streams that have the same
    # name. For example, if you create a data stream and then delete it, and you
    # later create another data stream with the same name, you can use this input
    # parameter to specify which of the two streams you want to list the shards
    # for.

    # You cannot specify this parameter if you specify the `NextToken` parameter.
    stream_creation_timestamp: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class ListShardsOutput(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "shards",
                "Shards",
                TypeInfo(typing.List[Shard]),
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

    # An array of JSON objects. Each object represents one shard and specifies
    # the IDs of the shard, the shard's parent, and the shard that's adjacent to
    # the shard's parent. Each object also contains the starting and ending hash
    # keys and the starting and ending sequence numbers for the shard.
    shards: typing.List["Shard"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # When the number of shards in the data stream is greater than the default
    # value for the `MaxResults` parameter, or if you explicitly specify a value
    # for `MaxResults` that is less than the number of shards in the data stream,
    # the response includes a pagination token named `NextToken`. You can specify
    # this `NextToken` value in a subsequent call to `ListShards` to list the
    # next set of shards. For more information about the use of this pagination
    # token when calling the `ListShards` operation, see
    # ListShardsInput$NextToken.

    # Tokens expire after 300 seconds. When you obtain a value for `NextToken` in
    # the response to a call to `ListShards`, you have 300 seconds to use that
    # value. If you specify an expired token in a call to `ListShards`, you get
    # `ExpiredNextTokenException`.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ListStreamConsumersInput(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "stream_arn",
                "StreamARN",
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
            (
                "stream_creation_timestamp",
                "StreamCreationTimestamp",
                TypeInfo(datetime.datetime),
            ),
        ]

    # The ARN of the Kinesis data stream for which you want to list the
    # registered consumers. For more information, see [Amazon Resource Names
    # (ARNs) and AWS Service
    # Namespaces](https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-
    # namespaces.html#arn-syntax-kinesis-streams).
    stream_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # When the number of consumers that are registered with the data stream is
    # greater than the default value for the `MaxResults` parameter, or if you
    # explicitly specify a value for `MaxResults` that is less than the number of
    # consumers that are registered with the data stream, the response includes a
    # pagination token named `NextToken`. You can specify this `NextToken` value
    # in a subsequent call to `ListStreamConsumers` to list the next set of
    # registered consumers.

    # Don't specify `StreamName` or `StreamCreationTimestamp` if you specify
    # `NextToken` because the latter unambiguously identifies the stream.

    # You can optionally specify a value for the `MaxResults` parameter when you
    # specify `NextToken`. If you specify a `MaxResults` value that is less than
    # the number of consumers that the operation returns if you don't specify
    # `MaxResults`, the response will contain a new `NextToken` value. You can
    # use the new `NextToken` value in a subsequent call to the
    # `ListStreamConsumers` operation to list the next set of consumers.

    # Tokens expire after 300 seconds. When you obtain a value for `NextToken` in
    # the response to a call to `ListStreamConsumers`, you have 300 seconds to
    # use that value. If you specify an expired token in a call to
    # `ListStreamConsumers`, you get `ExpiredNextTokenException`.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The maximum number of consumers that you want a single call of
    # `ListStreamConsumers` to return.
    max_results: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Specify this input parameter to distinguish data streams that have the same
    # name. For example, if you create a data stream and then delete it, and you
    # later create another data stream with the same name, you can use this input
    # parameter to specify which of the two streams you want to list the
    # consumers for.

    # You can't specify this parameter if you specify the NextToken parameter.
    stream_creation_timestamp: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class ListStreamConsumersOutput(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "consumers",
                "Consumers",
                TypeInfo(typing.List[Consumer]),
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

    # An array of JSON objects. Each object represents one registered consumer.
    consumers: typing.List["Consumer"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # When the number of consumers that are registered with the data stream is
    # greater than the default value for the `MaxResults` parameter, or if you
    # explicitly specify a value for `MaxResults` that is less than the number of
    # registered consumers, the response includes a pagination token named
    # `NextToken`. You can specify this `NextToken` value in a subsequent call to
    # `ListStreamConsumers` to list the next set of registered consumers. For
    # more information about the use of this pagination token when calling the
    # `ListStreamConsumers` operation, see ListStreamConsumersInput$NextToken.

    # Tokens expire after 300 seconds. When you obtain a value for `NextToken` in
    # the response to a call to `ListStreamConsumers`, you have 300 seconds to
    # use that value. If you specify an expired token in a call to
    # `ListStreamConsumers`, you get `ExpiredNextTokenException`.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ListStreamsInput(ShapeBase):
    """
    Represents the input for `ListStreams`.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "limit",
                "Limit",
                TypeInfo(int),
            ),
            (
                "exclusive_start_stream_name",
                "ExclusiveStartStreamName",
                TypeInfo(str),
            ),
        ]

    # The maximum number of streams to list.
    limit: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The name of the stream to start the list with.
    exclusive_start_stream_name: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class ListStreamsOutput(OutputShapeBase):
    """
    Represents the output for `ListStreams`.
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
                "stream_names",
                "StreamNames",
                TypeInfo(typing.List[str]),
            ),
            (
                "has_more_streams",
                "HasMoreStreams",
                TypeInfo(bool),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The names of the streams that are associated with the AWS account making
    # the `ListStreams` request.
    stream_names: typing.List[str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # If set to `true`, there are more streams available to list.
    has_more_streams: bool = dataclasses.field(default=ShapeBase.NOT_SET, )

    def paginate(self, ) -> typing.Generator["ListStreamsOutput", None, None]:
        yield from super()._paginate()


@dataclasses.dataclass
class ListTagsForStreamInput(ShapeBase):
    """
    Represents the input for `ListTagsForStream`.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "stream_name",
                "StreamName",
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

    # The name of the stream.
    stream_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The key to use as the starting point for the list of tags. If this
    # parameter is set, `ListTagsForStream` gets all tags that occur after
    # `ExclusiveStartTagKey`.
    exclusive_start_tag_key: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The number of tags to return. If this number is less than the total number
    # of tags associated with the stream, `HasMoreTags` is set to `true`. To list
    # additional tags, set `ExclusiveStartTagKey` to the last key in the
    # response.
    limit: int = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ListTagsForStreamOutput(OutputShapeBase):
    """
    Represents the output for `ListTagsForStream`.
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

    # A list of tags associated with `StreamName`, starting with the first tag
    # after `ExclusiveStartTagKey` and up to the specified `Limit`.
    tags: typing.List["Tag"] = dataclasses.field(default=ShapeBase.NOT_SET, )

    # If set to `true`, more tags are available. To request additional tags, set
    # `ExclusiveStartTagKey` to the key of the last tag returned.
    has_more_tags: bool = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class MergeShardsInput(ShapeBase):
    """
    Represents the input for `MergeShards`.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "stream_name",
                "StreamName",
                TypeInfo(str),
            ),
            (
                "shard_to_merge",
                "ShardToMerge",
                TypeInfo(str),
            ),
            (
                "adjacent_shard_to_merge",
                "AdjacentShardToMerge",
                TypeInfo(str),
            ),
        ]

    # The name of the stream for the merge.
    stream_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The shard ID of the shard to combine with the adjacent shard for the merge.
    shard_to_merge: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The shard ID of the adjacent shard for the merge.
    adjacent_shard_to_merge: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


class MetricsName(str):
    IncomingBytes = "IncomingBytes"
    IncomingRecords = "IncomingRecords"
    OutgoingBytes = "OutgoingBytes"
    OutgoingRecords = "OutgoingRecords"
    WriteProvisionedThroughputExceeded = "WriteProvisionedThroughputExceeded"
    ReadProvisionedThroughputExceeded = "ReadProvisionedThroughputExceeded"
    IteratorAgeMilliseconds = "IteratorAgeMilliseconds"
    ALL = "ALL"


@dataclasses.dataclass
class ProvisionedThroughputExceededException(ShapeBase):
    """
    The request rate for the stream is too high, or the requested data is too large
    for the available throughput. Reduce the frequency or size of your requests. For
    more information, see [Streams
    Limits](http://docs.aws.amazon.com/kinesis/latest/dev/service-sizes-and-
    limits.html) in the _Amazon Kinesis Data Streams Developer Guide_ , and [Error
    Retries and Exponential Backoff in
    AWS](http://docs.aws.amazon.com/general/latest/gr/api-retries.html) in the _AWS
    General Reference_.
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
class PutRecordInput(ShapeBase):
    """
    Represents the input for `PutRecord`.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "stream_name",
                "StreamName",
                TypeInfo(str),
            ),
            (
                "data",
                "Data",
                TypeInfo(typing.Any),
            ),
            (
                "partition_key",
                "PartitionKey",
                TypeInfo(str),
            ),
            (
                "explicit_hash_key",
                "ExplicitHashKey",
                TypeInfo(str),
            ),
            (
                "sequence_number_for_ordering",
                "SequenceNumberForOrdering",
                TypeInfo(str),
            ),
        ]

    # The name of the stream to put the data record into.
    stream_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The data blob to put into the record, which is base64-encoded when the blob
    # is serialized. When the data blob (the payload before base64-encoding) is
    # added to the partition key size, the total size must not exceed the maximum
    # record size (1 MB).
    data: typing.Any = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Determines which shard in the stream the data record is assigned to.
    # Partition keys are Unicode strings with a maximum length limit of 256
    # characters for each key. Amazon Kinesis Data Streams uses the partition key
    # as input to a hash function that maps the partition key and associated data
    # to a specific shard. Specifically, an MD5 hash function is used to map
    # partition keys to 128-bit integer values and to map associated data records
    # to shards. As a result of this hashing mechanism, all data records with the
    # same partition key map to the same shard within the stream.
    partition_key: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The hash value used to explicitly determine the shard the data record is
    # assigned to by overriding the partition key hash.
    explicit_hash_key: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Guarantees strictly increasing sequence numbers, for puts from the same
    # client and to the same partition key. Usage: set the
    # `SequenceNumberForOrdering` of record _n_ to the sequence number of record
    # _n-1_ (as returned in the result when putting record _n-1_ ). If this
    # parameter is not set, records are coarsely ordered based on arrival time.
    sequence_number_for_ordering: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class PutRecordOutput(OutputShapeBase):
    """
    Represents the output for `PutRecord`.
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
                "shard_id",
                "ShardId",
                TypeInfo(str),
            ),
            (
                "sequence_number",
                "SequenceNumber",
                TypeInfo(str),
            ),
            (
                "encryption_type",
                "EncryptionType",
                TypeInfo(typing.Union[str, EncryptionType]),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The shard ID of the shard where the data record was placed.
    shard_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The sequence number identifier that was assigned to the put data record.
    # The sequence number for the record is unique across all records in the
    # stream. A sequence number is the identifier associated with every record
    # put into the stream.
    sequence_number: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The encryption type to use on the record. This parameter can be one of the
    # following values:

    #   * `NONE`: Do not encrypt the records in the stream.

    #   * `KMS`: Use server-side encryption on the records in the stream using a customer-managed AWS KMS key.
    encryption_type: typing.Union[str, "EncryptionType"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class PutRecordsInput(ShapeBase):
    """
    A `PutRecords` request.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "records",
                "Records",
                TypeInfo(typing.List[PutRecordsRequestEntry]),
            ),
            (
                "stream_name",
                "StreamName",
                TypeInfo(str),
            ),
        ]

    # The records associated with the request.
    records: typing.List["PutRecordsRequestEntry"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The stream name associated with the request.
    stream_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class PutRecordsOutput(OutputShapeBase):
    """
    `PutRecords` results.
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
                "records",
                "Records",
                TypeInfo(typing.List[PutRecordsResultEntry]),
            ),
            (
                "failed_record_count",
                "FailedRecordCount",
                TypeInfo(int),
            ),
            (
                "encryption_type",
                "EncryptionType",
                TypeInfo(typing.Union[str, EncryptionType]),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # An array of successfully and unsuccessfully processed record results,
    # correlated with the request by natural ordering. A record that is
    # successfully added to a stream includes `SequenceNumber` and `ShardId` in
    # the result. A record that fails to be added to a stream includes
    # `ErrorCode` and `ErrorMessage` in the result.
    records: typing.List["PutRecordsResultEntry"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The number of unsuccessfully processed records in a `PutRecords` request.
    failed_record_count: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The encryption type used on the records. This parameter can be one of the
    # following values:

    #   * `NONE`: Do not encrypt the records.

    #   * `KMS`: Use server-side encryption on the records using a customer-managed AWS KMS key.
    encryption_type: typing.Union[str, "EncryptionType"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class PutRecordsRequestEntry(ShapeBase):
    """
    Represents the output for `PutRecords`.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "data",
                "Data",
                TypeInfo(typing.Any),
            ),
            (
                "partition_key",
                "PartitionKey",
                TypeInfo(str),
            ),
            (
                "explicit_hash_key",
                "ExplicitHashKey",
                TypeInfo(str),
            ),
        ]

    # The data blob to put into the record, which is base64-encoded when the blob
    # is serialized. When the data blob (the payload before base64-encoding) is
    # added to the partition key size, the total size must not exceed the maximum
    # record size (1 MB).
    data: typing.Any = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Determines which shard in the stream the data record is assigned to.
    # Partition keys are Unicode strings with a maximum length limit of 256
    # characters for each key. Amazon Kinesis Data Streams uses the partition key
    # as input to a hash function that maps the partition key and associated data
    # to a specific shard. Specifically, an MD5 hash function is used to map
    # partition keys to 128-bit integer values and to map associated data records
    # to shards. As a result of this hashing mechanism, all data records with the
    # same partition key map to the same shard within the stream.
    partition_key: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The hash value used to determine explicitly the shard that the data record
    # is assigned to by overriding the partition key hash.
    explicit_hash_key: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class PutRecordsResultEntry(ShapeBase):
    """
    Represents the result of an individual record from a `PutRecords` request. A
    record that is successfully added to a stream includes `SequenceNumber` and
    `ShardId` in the result. A record that fails to be added to the stream includes
    `ErrorCode` and `ErrorMessage` in the result.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "sequence_number",
                "SequenceNumber",
                TypeInfo(str),
            ),
            (
                "shard_id",
                "ShardId",
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

    # The sequence number for an individual record result.
    sequence_number: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The shard ID for an individual record result.
    shard_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The error code for an individual record result. `ErrorCodes` can be either
    # `ProvisionedThroughputExceededException` or `InternalFailure`.
    error_code: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The error message for an individual record result. An `ErrorCode` value of
    # `ProvisionedThroughputExceededException` has an error message that includes
    # the account ID, stream name, and shard ID. An `ErrorCode` value of
    # `InternalFailure` has the error message `"Internal Service Failure"`.
    error_message: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class Record(ShapeBase):
    """
    The unit of data of the Kinesis data stream, which is composed of a sequence
    number, a partition key, and a data blob.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "sequence_number",
                "SequenceNumber",
                TypeInfo(str),
            ),
            (
                "data",
                "Data",
                TypeInfo(typing.Any),
            ),
            (
                "partition_key",
                "PartitionKey",
                TypeInfo(str),
            ),
            (
                "approximate_arrival_timestamp",
                "ApproximateArrivalTimestamp",
                TypeInfo(datetime.datetime),
            ),
            (
                "encryption_type",
                "EncryptionType",
                TypeInfo(typing.Union[str, EncryptionType]),
            ),
        ]

    # The unique identifier of the record within its shard.
    sequence_number: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The data blob. The data in the blob is both opaque and immutable to Kinesis
    # Data Streams, which does not inspect, interpret, or change the data in the
    # blob in any way. When the data blob (the payload before base64-encoding) is
    # added to the partition key size, the total size must not exceed the maximum
    # record size (1 MB).
    data: typing.Any = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Identifies which shard in the stream the data record is assigned to.
    partition_key: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The approximate time that the record was inserted into the stream.
    approximate_arrival_timestamp: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The encryption type used on the record. This parameter can be one of the
    # following values:

    #   * `NONE`: Do not encrypt the records in the stream.

    #   * `KMS`: Use server-side encryption on the records in the stream using a customer-managed AWS KMS key.
    encryption_type: typing.Union[str, "EncryptionType"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class RegisterStreamConsumerInput(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "stream_arn",
                "StreamARN",
                TypeInfo(str),
            ),
            (
                "consumer_name",
                "ConsumerName",
                TypeInfo(str),
            ),
        ]

    # The ARN of the Kinesis data stream that you want to register the consumer
    # with. For more info, see [Amazon Resource Names (ARNs) and AWS Service
    # Namespaces](https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-
    # namespaces.html#arn-syntax-kinesis-streams).
    stream_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # For a given Kinesis data stream, each consumer must have a unique name.
    # However, consumer names don't have to be unique across data streams.
    consumer_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class RegisterStreamConsumerOutput(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "consumer",
                "Consumer",
                TypeInfo(Consumer),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # An object that represents the details of the consumer you registered. When
    # you register a consumer, it gets an ARN that is generated by Kinesis Data
    # Streams.
    consumer: "Consumer" = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class RemoveTagsFromStreamInput(ShapeBase):
    """
    Represents the input for `RemoveTagsFromStream`.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "stream_name",
                "StreamName",
                TypeInfo(str),
            ),
            (
                "tag_keys",
                "TagKeys",
                TypeInfo(typing.List[str]),
            ),
        ]

    # The name of the stream.
    stream_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A list of tag keys. Each corresponding tag is removed from the stream.
    tag_keys: typing.List[str] = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ResourceInUseException(ShapeBase):
    """
    The resource is not available for this operation. For successful operation, the
    resource must be in the `ACTIVE` state.
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
    The requested resource could not be found. The stream might not be specified
    correctly.
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


class ScalingType(str):
    UNIFORM_SCALING = "UNIFORM_SCALING"


@dataclasses.dataclass
class SequenceNumberRange(ShapeBase):
    """
    The range of possible sequence numbers for the shard.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "starting_sequence_number",
                "StartingSequenceNumber",
                TypeInfo(str),
            ),
            (
                "ending_sequence_number",
                "EndingSequenceNumber",
                TypeInfo(str),
            ),
        ]

    # The starting sequence number for the range.
    starting_sequence_number: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The ending sequence number for the range. Shards that are in the OPEN state
    # have an ending sequence number of `null`.
    ending_sequence_number: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class Shard(ShapeBase):
    """
    A uniquely identified group of data records in a Kinesis data stream.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "shard_id",
                "ShardId",
                TypeInfo(str),
            ),
            (
                "hash_key_range",
                "HashKeyRange",
                TypeInfo(HashKeyRange),
            ),
            (
                "sequence_number_range",
                "SequenceNumberRange",
                TypeInfo(SequenceNumberRange),
            ),
            (
                "parent_shard_id",
                "ParentShardId",
                TypeInfo(str),
            ),
            (
                "adjacent_parent_shard_id",
                "AdjacentParentShardId",
                TypeInfo(str),
            ),
        ]

    # The unique identifier of the shard within the stream.
    shard_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The range of possible hash key values for the shard, which is a set of
    # ordered contiguous positive integers.
    hash_key_range: "HashKeyRange" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The range of possible sequence numbers for the shard.
    sequence_number_range: "SequenceNumberRange" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The shard ID of the shard's parent.
    parent_shard_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The shard ID of the shard adjacent to the shard's parent.
    adjacent_parent_shard_id: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


class ShardIteratorType(str):
    AT_SEQUENCE_NUMBER = "AT_SEQUENCE_NUMBER"
    AFTER_SEQUENCE_NUMBER = "AFTER_SEQUENCE_NUMBER"
    TRIM_HORIZON = "TRIM_HORIZON"
    LATEST = "LATEST"
    AT_TIMESTAMP = "AT_TIMESTAMP"


@dataclasses.dataclass
class SplitShardInput(ShapeBase):
    """
    Represents the input for `SplitShard`.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "stream_name",
                "StreamName",
                TypeInfo(str),
            ),
            (
                "shard_to_split",
                "ShardToSplit",
                TypeInfo(str),
            ),
            (
                "new_starting_hash_key",
                "NewStartingHashKey",
                TypeInfo(str),
            ),
        ]

    # The name of the stream for the shard split.
    stream_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The shard ID of the shard to split.
    shard_to_split: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A hash key value for the starting hash key of one of the child shards
    # created by the split. The hash key range for a given shard constitutes a
    # set of ordered contiguous positive integers. The value for
    # `NewStartingHashKey` must be in the range of hash keys being mapped into
    # the shard. The `NewStartingHashKey` hash key value and all higher hash key
    # values in hash key range are distributed to one of the child shards. All
    # the lower hash key values in the range are distributed to the other child
    # shard.
    new_starting_hash_key: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class StartStreamEncryptionInput(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "stream_name",
                "StreamName",
                TypeInfo(str),
            ),
            (
                "encryption_type",
                "EncryptionType",
                TypeInfo(typing.Union[str, EncryptionType]),
            ),
            (
                "key_id",
                "KeyId",
                TypeInfo(str),
            ),
        ]

    # The name of the stream for which to start encrypting records.
    stream_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The encryption type to use. The only valid value is `KMS`.
    encryption_type: typing.Union[str, "EncryptionType"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The GUID for the customer-managed AWS KMS key to use for encryption. This
    # value can be a globally unique identifier, a fully specified Amazon
    # Resource Name (ARN) to either an alias or a key, or an alias name prefixed
    # by "alias/".You can also use a master key owned by Kinesis Data Streams by
    # specifying the alias `aws/kinesis`.

    #   * Key ARN example: `arn:aws:kms:us-east-1:123456789012:key/12345678-1234-1234-1234-123456789012`

    #   * Alias ARN example: `arn:aws:kms:us-east-1:123456789012:alias/MyAliasName`

    #   * Globally unique key ID example: `12345678-1234-1234-1234-123456789012`

    #   * Alias name example: `alias/MyAliasName`

    #   * Master key owned by Kinesis Data Streams: `alias/aws/kinesis`
    key_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class StartingPosition(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "type",
                "Type",
                TypeInfo(typing.Union[str, ShardIteratorType]),
            ),
            (
                "sequence_number",
                "SequenceNumber",
                TypeInfo(str),
            ),
            (
                "timestamp",
                "Timestamp",
                TypeInfo(datetime.datetime),
            ),
        ]

    type: typing.Union[str, "ShardIteratorType"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )
    sequence_number: str = dataclasses.field(default=ShapeBase.NOT_SET, )
    timestamp: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class StopStreamEncryptionInput(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "stream_name",
                "StreamName",
                TypeInfo(str),
            ),
            (
                "encryption_type",
                "EncryptionType",
                TypeInfo(typing.Union[str, EncryptionType]),
            ),
            (
                "key_id",
                "KeyId",
                TypeInfo(str),
            ),
        ]

    # The name of the stream on which to stop encrypting records.
    stream_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The encryption type. The only valid value is `KMS`.
    encryption_type: typing.Union[str, "EncryptionType"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The GUID for the customer-managed AWS KMS key to use for encryption. This
    # value can be a globally unique identifier, a fully specified Amazon
    # Resource Name (ARN) to either an alias or a key, or an alias name prefixed
    # by "alias/".You can also use a master key owned by Kinesis Data Streams by
    # specifying the alias `aws/kinesis`.

    #   * Key ARN example: `arn:aws:kms:us-east-1:123456789012:key/12345678-1234-1234-1234-123456789012`

    #   * Alias ARN example: `arn:aws:kms:us-east-1:123456789012:alias/MyAliasName`

    #   * Globally unique key ID example: `12345678-1234-1234-1234-123456789012`

    #   * Alias name example: `alias/MyAliasName`

    #   * Master key owned by Kinesis Data Streams: `alias/aws/kinesis`
    key_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class StreamDescription(ShapeBase):
    """
    Represents the output for DescribeStream.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "stream_name",
                "StreamName",
                TypeInfo(str),
            ),
            (
                "stream_arn",
                "StreamARN",
                TypeInfo(str),
            ),
            (
                "stream_status",
                "StreamStatus",
                TypeInfo(typing.Union[str, StreamStatus]),
            ),
            (
                "shards",
                "Shards",
                TypeInfo(typing.List[Shard]),
            ),
            (
                "has_more_shards",
                "HasMoreShards",
                TypeInfo(bool),
            ),
            (
                "retention_period_hours",
                "RetentionPeriodHours",
                TypeInfo(int),
            ),
            (
                "stream_creation_timestamp",
                "StreamCreationTimestamp",
                TypeInfo(datetime.datetime),
            ),
            (
                "enhanced_monitoring",
                "EnhancedMonitoring",
                TypeInfo(typing.List[EnhancedMetrics]),
            ),
            (
                "encryption_type",
                "EncryptionType",
                TypeInfo(typing.Union[str, EncryptionType]),
            ),
            (
                "key_id",
                "KeyId",
                TypeInfo(str),
            ),
        ]

    # The name of the stream being described.
    stream_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The Amazon Resource Name (ARN) for the stream being described.
    stream_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The current status of the stream being described. The stream status is one
    # of the following states:

    #   * `CREATING` \- The stream is being created. Kinesis Data Streams immediately returns and sets `StreamStatus` to `CREATING`.

    #   * `DELETING` \- The stream is being deleted. The specified stream is in the `DELETING` state until Kinesis Data Streams completes the deletion.

    #   * `ACTIVE` \- The stream exists and is ready for read and write operations or deletion. You should perform read and write operations only on an `ACTIVE` stream.

    #   * `UPDATING` \- Shards in the stream are being merged or split. Read and write operations continue to work while the stream is in the `UPDATING` state.
    stream_status: typing.Union[str, "StreamStatus"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The shards that comprise the stream.
    shards: typing.List["Shard"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # If set to `true`, more shards in the stream are available to describe.
    has_more_shards: bool = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The current retention period, in hours.
    retention_period_hours: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The approximate time that the stream was created.
    stream_creation_timestamp: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Represents the current enhanced monitoring settings of the stream.
    enhanced_monitoring: typing.List["EnhancedMetrics"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The server-side encryption type used on the stream. This parameter can be
    # one of the following values:

    #   * `NONE`: Do not encrypt the records in the stream.

    #   * `KMS`: Use server-side encryption on the records in the stream using a customer-managed AWS KMS key.
    encryption_type: typing.Union[str, "EncryptionType"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The GUID for the customer-managed AWS KMS key to use for encryption. This
    # value can be a globally unique identifier, a fully specified ARN to either
    # an alias or a key, or an alias name prefixed by "alias/".You can also use a
    # master key owned by Kinesis Data Streams by specifying the alias
    # `aws/kinesis`.

    #   * Key ARN example: `arn:aws:kms:us-east-1:123456789012:key/12345678-1234-1234-1234-123456789012`

    #   * Alias ARN example: `arn:aws:kms:us-east-1:123456789012:alias/MyAliasName`

    #   * Globally unique key ID example: `12345678-1234-1234-1234-123456789012`

    #   * Alias name example: `alias/MyAliasName`

    #   * Master key owned by Kinesis Data Streams: `alias/aws/kinesis`
    key_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class StreamDescriptionSummary(ShapeBase):
    """
    Represents the output for DescribeStreamSummary
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "stream_name",
                "StreamName",
                TypeInfo(str),
            ),
            (
                "stream_arn",
                "StreamARN",
                TypeInfo(str),
            ),
            (
                "stream_status",
                "StreamStatus",
                TypeInfo(typing.Union[str, StreamStatus]),
            ),
            (
                "retention_period_hours",
                "RetentionPeriodHours",
                TypeInfo(int),
            ),
            (
                "stream_creation_timestamp",
                "StreamCreationTimestamp",
                TypeInfo(datetime.datetime),
            ),
            (
                "enhanced_monitoring",
                "EnhancedMonitoring",
                TypeInfo(typing.List[EnhancedMetrics]),
            ),
            (
                "open_shard_count",
                "OpenShardCount",
                TypeInfo(int),
            ),
            (
                "encryption_type",
                "EncryptionType",
                TypeInfo(typing.Union[str, EncryptionType]),
            ),
            (
                "key_id",
                "KeyId",
                TypeInfo(str),
            ),
            (
                "consumer_count",
                "ConsumerCount",
                TypeInfo(int),
            ),
        ]

    # The name of the stream being described.
    stream_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The Amazon Resource Name (ARN) for the stream being described.
    stream_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The current status of the stream being described. The stream status is one
    # of the following states:

    #   * `CREATING` \- The stream is being created. Kinesis Data Streams immediately returns and sets `StreamStatus` to `CREATING`.

    #   * `DELETING` \- The stream is being deleted. The specified stream is in the `DELETING` state until Kinesis Data Streams completes the deletion.

    #   * `ACTIVE` \- The stream exists and is ready for read and write operations or deletion. You should perform read and write operations only on an `ACTIVE` stream.

    #   * `UPDATING` \- Shards in the stream are being merged or split. Read and write operations continue to work while the stream is in the `UPDATING` state.
    stream_status: typing.Union[str, "StreamStatus"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The current retention period, in hours.
    retention_period_hours: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The approximate time that the stream was created.
    stream_creation_timestamp: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Represents the current enhanced monitoring settings of the stream.
    enhanced_monitoring: typing.List["EnhancedMetrics"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The number of open shards in the stream.
    open_shard_count: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The encryption type used. This value is one of the following:

    #   * `KMS`

    #   * `NONE`
    encryption_type: typing.Union[str, "EncryptionType"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The GUID for the customer-managed AWS KMS key to use for encryption. This
    # value can be a globally unique identifier, a fully specified ARN to either
    # an alias or a key, or an alias name prefixed by "alias/".You can also use a
    # master key owned by Kinesis Data Streams by specifying the alias
    # `aws/kinesis`.

    #   * Key ARN example: `arn:aws:kms:us-east-1:123456789012:key/12345678-1234-1234-1234-123456789012`

    #   * Alias ARN example: ` arn:aws:kms:us-east-1:123456789012:alias/MyAliasName`

    #   * Globally unique key ID example: `12345678-1234-1234-1234-123456789012`

    #   * Alias name example: `alias/MyAliasName`

    #   * Master key owned by Kinesis Data Streams: `alias/aws/kinesis`
    key_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The number of enhanced fan-out consumers registered with the stream.
    consumer_count: int = dataclasses.field(default=ShapeBase.NOT_SET, )


class StreamStatus(str):
    CREATING = "CREATING"
    DELETING = "DELETING"
    ACTIVE = "ACTIVE"
    UPDATING = "UPDATING"


@dataclasses.dataclass
class SubscribeToShardEvent(ShapeBase):
    """
    After you call SubscribeToShard, Kinesis Data Streams sends events of this type
    to your consumer.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "records",
                "Records",
                TypeInfo(typing.List[Record]),
            ),
            (
                "continuation_sequence_number",
                "ContinuationSequenceNumber",
                TypeInfo(str),
            ),
            (
                "millis_behind_latest",
                "MillisBehindLatest",
                TypeInfo(int),
            ),
        ]

    records: typing.List["Record"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Use this as `StartingSequenceNumber` in the next call to SubscribeToShard.
    continuation_sequence_number: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The number of milliseconds the read records are from the tip of the stream,
    # indicating how far behind current time the consumer is. A value of zero
    # indicates that record processing is caught up, and there are no new records
    # to process at this moment.
    millis_behind_latest: int = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class SubscribeToShardEventStream(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "subscribe_to_shard_event",
                "SubscribeToShardEvent",
                TypeInfo(SubscribeToShardEvent),
            ),
            (
                "resource_not_found_exception",
                "ResourceNotFoundException",
                TypeInfo(ResourceNotFoundException),
            ),
            (
                "resource_in_use_exception",
                "ResourceInUseException",
                TypeInfo(ResourceInUseException),
            ),
            (
                "kms_disabled_exception",
                "KMSDisabledException",
                TypeInfo(KMSDisabledException),
            ),
            (
                "kms_invalid_state_exception",
                "KMSInvalidStateException",
                TypeInfo(KMSInvalidStateException),
            ),
            (
                "kms_access_denied_exception",
                "KMSAccessDeniedException",
                TypeInfo(KMSAccessDeniedException),
            ),
            (
                "kms_not_found_exception",
                "KMSNotFoundException",
                TypeInfo(KMSNotFoundException),
            ),
            (
                "kms_opt_in_required",
                "KMSOptInRequired",
                TypeInfo(KMSOptInRequired),
            ),
            (
                "kms_throttling_exception",
                "KMSThrottlingException",
                TypeInfo(KMSThrottlingException),
            ),
            (
                "internal_failure_exception",
                "InternalFailureException",
                TypeInfo(InternalFailureException),
            ),
        ]

    # After you call SubscribeToShard, Kinesis Data Streams sends events of this
    # type to your consumer.
    subscribe_to_shard_event: "SubscribeToShardEvent" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The requested resource could not be found. The stream might not be
    # specified correctly.
    resource_not_found_exception: "ResourceNotFoundException" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The resource is not available for this operation. For successful operation,
    # the resource must be in the `ACTIVE` state.
    resource_in_use_exception: "ResourceInUseException" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The request was rejected because the specified customer master key (CMK)
    # isn't enabled.
    kms_disabled_exception: "KMSDisabledException" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The request was rejected because the state of the specified resource isn't
    # valid for this request. For more information, see [How Key State Affects
    # Use of a Customer Master
    # Key](http://docs.aws.amazon.com/kms/latest/developerguide/key-state.html)
    # in the _AWS Key Management Service Developer Guide_.
    kms_invalid_state_exception: "KMSInvalidStateException" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The ciphertext references a key that doesn't exist or that you don't have
    # access to.
    kms_access_denied_exception: "KMSAccessDeniedException" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The request was rejected because the specified entity or resource can't be
    # found.
    kms_not_found_exception: "KMSNotFoundException" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The AWS access key ID needs a subscription for the service.
    kms_opt_in_required: "KMSOptInRequired" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The request was denied due to request throttling. For more information
    # about throttling, see
    # [Limits](http://docs.aws.amazon.com/kms/latest/developerguide/limits.html#requests-
    # per-second) in the _AWS Key Management Service Developer Guide_.
    kms_throttling_exception: "KMSThrottlingException" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )
    internal_failure_exception: "InternalFailureException" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class SubscribeToShardInput(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "consumer_arn",
                "ConsumerARN",
                TypeInfo(str),
            ),
            (
                "shard_id",
                "ShardId",
                TypeInfo(str),
            ),
            (
                "starting_position",
                "StartingPosition",
                TypeInfo(StartingPosition),
            ),
        ]

    # For this parameter, use the value you obtained when you called
    # RegisterStreamConsumer.
    consumer_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The ID of the shard you want to subscribe to. To see a list of all the
    # shards for a given stream, use ListShards.
    shard_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )
    starting_position: "StartingPosition" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class SubscribeToShardOutput(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "event_stream",
                "EventStream",
                TypeInfo(SubscribeToShardEventStream),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The event stream that your consumer can use to read records from the shard.
    event_stream: "SubscribeToShardEventStream" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class Tag(ShapeBase):
    """
    Metadata assigned to the stream, consisting of a key-value pair.
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

    # An optional string, typically used to describe or define the tag. Maximum
    # length: 256 characters. Valid characters: Unicode letters, digits, white
    # space, _ . / = + - % @
    value: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class UpdateShardCountInput(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "stream_name",
                "StreamName",
                TypeInfo(str),
            ),
            (
                "target_shard_count",
                "TargetShardCount",
                TypeInfo(int),
            ),
            (
                "scaling_type",
                "ScalingType",
                TypeInfo(typing.Union[str, ScalingType]),
            ),
        ]

    # The name of the stream.
    stream_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The new number of shards.
    target_shard_count: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The scaling type. Uniform scaling creates shards of equal size.
    scaling_type: typing.Union[str, "ScalingType"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class UpdateShardCountOutput(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "stream_name",
                "StreamName",
                TypeInfo(str),
            ),
            (
                "current_shard_count",
                "CurrentShardCount",
                TypeInfo(int),
            ),
            (
                "target_shard_count",
                "TargetShardCount",
                TypeInfo(int),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The name of the stream.
    stream_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The current number of shards.
    current_shard_count: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The updated number of shards.
    target_shard_count: int = dataclasses.field(default=ShapeBase.NOT_SET, )
