import datetime
import typing
from autoboto import ShapeBase, OutputShapeBase, TypeInfo
import botocore.response
import dataclasses


@dataclasses.dataclass
class AttributeValue(ShapeBase):
    """
    Represents the data for an attribute. You can set one, and only one, of the
    elements.

    Each attribute in an item is a name-value pair. An attribute can be single-
    valued or multi-valued set. For example, a book item can have title and authors
    attributes. Each book has one title but can have many authors. The multi-valued
    attribute is a set; duplicate values are not allowed.
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
                TypeInfo(str),
            ),
            (
                "b",
                "B",
                TypeInfo(typing.Any),
            ),
            (
                "ss",
                "SS",
                TypeInfo(typing.List[str]),
            ),
            (
                "ns",
                "NS",
                TypeInfo(typing.List[str]),
            ),
            (
                "bs",
                "BS",
                TypeInfo(typing.List[typing.Any]),
            ),
            (
                "m",
                "M",
                TypeInfo(typing.Dict[str, AttributeValue]),
            ),
            (
                "l",
                "L",
                TypeInfo(typing.List[AttributeValue]),
            ),
            (
                "null",
                "NULL",
                TypeInfo(bool),
            ),
            (
                "bool",
                "BOOL",
                TypeInfo(bool),
            ),
        ]

    # A String data type.
    s: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A Number data type.
    n: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A Binary data type.
    b: typing.Any = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A String Set data type.
    ss: typing.List[str] = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A Number Set data type.
    ns: typing.List[str] = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A Binary Set data type.
    bs: typing.List[typing.Any] = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A Map data type.
    m: typing.Dict[str, "AttributeValue"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A List data type.
    l: typing.List["AttributeValue"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A Null data type.
    null: bool = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A Boolean data type.
    bool: bool = dataclasses.field(default=ShapeBase.NOT_SET, )


class BinaryAttributeValue(botocore.response.StreamingBody):
    pass


@dataclasses.dataclass
class DescribeStreamInput(ShapeBase):
    """
    Represents the input of a `DescribeStream` operation.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "stream_arn",
                "StreamArn",
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

    # The Amazon Resource Name (ARN) for the stream.
    stream_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The maximum number of shard objects to return. The upper limit is 100.
    limit: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The shard ID of the first item that this operation will evaluate. Use the
    # value that was returned for `LastEvaluatedShardId` in the previous
    # operation.
    exclusive_start_shard_id: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class DescribeStreamOutput(OutputShapeBase):
    """
    Represents the output of a `DescribeStream` operation.
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

    # A complete description of the stream, including its creation date and time,
    # the DynamoDB table associated with the stream, the shard IDs within the
    # stream, and the beginning and ending sequence numbers of stream records
    # within the shards.
    stream_description: "StreamDescription" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class ExpiredIteratorException(ShapeBase):
    """
    The shard iterator has expired and can no longer be used to retrieve stream
    records. A shard iterator expires 15 minutes after it is retrieved using the
    `GetShardIterator` action.
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

    # The provided iterator exceeds the maximum age allowed.
    message: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class GetRecordsInput(ShapeBase):
    """
    Represents the input of a `GetRecords` operation.
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

    # A shard iterator that was retrieved from a previous GetShardIterator
    # operation. This iterator can be used to access the stream records in this
    # shard.
    shard_iterator: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The maximum number of records to return from the shard. The upper limit is
    # 1000.
    limit: int = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class GetRecordsOutput(OutputShapeBase):
    """
    Represents the output of a `GetRecords` operation.
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
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The stream records from the shard, which were retrieved using the shard
    # iterator.
    records: typing.List["Record"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The next position in the shard from which to start sequentially reading
    # stream records. If set to `null`, the shard has been closed and the
    # requested iterator will not return any more data.
    next_shard_iterator: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class GetShardIteratorInput(ShapeBase):
    """
    Represents the input of a `GetShardIterator` operation.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "stream_arn",
                "StreamArn",
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
                "sequence_number",
                "SequenceNumber",
                TypeInfo(str),
            ),
        ]

    # The Amazon Resource Name (ARN) for the stream.
    stream_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The identifier of the shard. The iterator will be returned for this shard
    # ID.
    shard_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Determines how the shard iterator is used to start reading stream records
    # from the shard:

    #   * `AT_SEQUENCE_NUMBER` \- Start reading exactly from the position denoted by a specific sequence number.

    #   * `AFTER_SEQUENCE_NUMBER` \- Start reading right after the position denoted by a specific sequence number.

    #   * `TRIM_HORIZON` \- Start reading at the last (untrimmed) stream record, which is the oldest record in the shard. In DynamoDB Streams, there is a 24 hour limit on data retention. Stream records whose age exceeds this limit are subject to removal (trimming) from the stream.

    #   * `LATEST` \- Start reading just after the most recent stream record in the shard, so that you always read the most recent data in the shard.
    shard_iterator_type: typing.Union[str, "ShardIteratorType"
                                     ] = dataclasses.field(
                                         default=ShapeBase.NOT_SET,
                                     )

    # The sequence number of a stream record in the shard from which to start
    # reading.
    sequence_number: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class GetShardIteratorOutput(OutputShapeBase):
    """
    Represents the output of a `GetShardIterator` operation.
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

    # The position in the shard from which to start reading stream records
    # sequentially. A shard iterator specifies this position using the sequence
    # number of a stream record in a shard.
    shard_iterator: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class Identity(ShapeBase):
    """
    Contains details about the type of identity that made the request.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "principal_id",
                "PrincipalId",
                TypeInfo(str),
            ),
            (
                "type",
                "Type",
                TypeInfo(str),
            ),
        ]

    # A unique identifier for the entity that made the call. For Time To Live,
    # the principalId is "dynamodb.amazonaws.com".
    principal_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The type of the identity. For Time To Live, the type is "Service".
    type: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class InternalServerError(ShapeBase):
    """
    An error occurred on the server side.
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

    # The server encountered an internal error trying to fulfill the request.
    message: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class KeySchemaElement(ShapeBase):
    """
    Represents _a single element_ of a key schema. A key schema specifies the
    attributes that make up the primary key of a table, or the key attributes of an
    index.

    A `KeySchemaElement` represents exactly one attribute of the primary key. For
    example, a simple primary key (partition key) would be represented by one
    `KeySchemaElement`. A composite primary key (partition key and sort key) would
    require one `KeySchemaElement` for the partition key, and another
    `KeySchemaElement` for the sort key.

    The partition key of an item is also known as its _hash attribute_. The term
    "hash attribute" derives from DynamoDB's usage of an internal hash function to
    evenly distribute data items across partitions, based on their partition key
    values.

    The sort key of an item is also known as its _range attribute_. The term "range
    attribute" derives from the way DynamoDB stores items with the same partition
    key physically close together, in sorted order by the sort key value.
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
                "key_type",
                "KeyType",
                TypeInfo(typing.Union[str, KeyType]),
            ),
        ]

    # The name of a key attribute.
    attribute_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The attribute data, consisting of the data type and the attribute value
    # itself.
    key_type: typing.Union[str, "KeyType"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


class KeyType(str):
    HASH = "HASH"
    RANGE = "RANGE"


@dataclasses.dataclass
class LimitExceededException(ShapeBase):
    """
    Your request rate is too high. The AWS SDKs for DynamoDB automatically retry
    requests that receive this exception. Your request is eventually successful,
    unless your retry queue is too large to finish. Reduce the frequency of requests
    and use exponential backoff. For more information, go to [Error Retries and
    Exponential
    Backoff](http://docs.aws.amazon.com/amazondynamodb/latest/developerguide/ErrorHandling.html#APIRetries)
    in the _Amazon DynamoDB Developer Guide_.
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

    # Too many operations for a given subscriber.
    message: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ListStreamsInput(ShapeBase):
    """
    Represents the input of a `ListStreams` operation.
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
                "limit",
                "Limit",
                TypeInfo(int),
            ),
            (
                "exclusive_start_stream_arn",
                "ExclusiveStartStreamArn",
                TypeInfo(str),
            ),
        ]

    # If this parameter is provided, then only the streams associated with this
    # table name are returned.
    table_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The maximum number of streams to return. The upper limit is 100.
    limit: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The ARN (Amazon Resource Name) of the first item that this operation will
    # evaluate. Use the value that was returned for `LastEvaluatedStreamArn` in
    # the previous operation.
    exclusive_start_stream_arn: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class ListStreamsOutput(OutputShapeBase):
    """
    Represents the output of a `ListStreams` operation.
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
                "streams",
                "Streams",
                TypeInfo(typing.List[Stream]),
            ),
            (
                "last_evaluated_stream_arn",
                "LastEvaluatedStreamArn",
                TypeInfo(str),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A list of stream descriptors associated with the current account and
    # endpoint.
    streams: typing.List["Stream"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The stream ARN of the item where the operation stopped, inclusive of the
    # previous result set. Use this value to start a new operation, excluding
    # this value in the new request.

    # If `LastEvaluatedStreamArn` is empty, then the "last page" of results has
    # been processed and there is no more data to be retrieved.

    # If `LastEvaluatedStreamArn` is not empty, it does not necessarily mean that
    # there is more data in the result set. The only way to know when you have
    # reached the end of the result set is when `LastEvaluatedStreamArn` is
    # empty.
    last_evaluated_stream_arn: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


class OperationType(str):
    INSERT = "INSERT"
    MODIFY = "MODIFY"
    REMOVE = "REMOVE"


@dataclasses.dataclass
class Record(ShapeBase):
    """
    A description of a unique event within a stream.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "event_id",
                "eventID",
                TypeInfo(str),
            ),
            (
                "event_name",
                "eventName",
                TypeInfo(typing.Union[str, OperationType]),
            ),
            (
                "event_version",
                "eventVersion",
                TypeInfo(str),
            ),
            (
                "event_source",
                "eventSource",
                TypeInfo(str),
            ),
            (
                "aws_region",
                "awsRegion",
                TypeInfo(str),
            ),
            (
                "dynamodb",
                "dynamodb",
                TypeInfo(StreamRecord),
            ),
            (
                "user_identity",
                "userIdentity",
                TypeInfo(Identity),
            ),
        ]

    # A globally unique identifier for the event that was recorded in this stream
    # record.
    event_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The type of data modification that was performed on the DynamoDB table:

    #   * `INSERT` \- a new item was added to the table.

    #   * `MODIFY` \- one or more of an existing item's attributes were modified.

    #   * `REMOVE` \- the item was deleted from the table
    event_name: typing.Union[str, "OperationType"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The version number of the stream record format. This number is updated
    # whenever the structure of `Record` is modified.

    # Client applications must not assume that `eventVersion` will remain at a
    # particular value, as this number is subject to change at any time. In
    # general, `eventVersion` will only increase as the low-level DynamoDB
    # Streams API evolves.
    event_version: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The AWS service from which the stream record originated. For DynamoDB
    # Streams, this is `aws:dynamodb`.
    event_source: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The region in which the `GetRecords` request was received.
    aws_region: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The main body of the stream record, containing all of the DynamoDB-specific
    # fields.
    dynamodb: "StreamRecord" = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Items that are deleted by the Time to Live process after expiration have
    # the following fields:

    #   * Records[].userIdentity.type

    # "Service"

    #   * Records[].userIdentity.principalId

    # "dynamodb.amazonaws.com"
    user_identity: "Identity" = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ResourceNotFoundException(ShapeBase):
    """
    The operation tried to access a nonexistent stream.
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

    # The resource which is being requested does not exist.
    message: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class SequenceNumberRange(ShapeBase):
    """
    The beginning and ending sequence numbers for the stream records contained
    within a shard.
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

    # The first sequence number.
    starting_sequence_number: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The last sequence number.
    ending_sequence_number: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class Shard(ShapeBase):
    """
    A uniquely identified group of stream records within a stream.
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
                "sequence_number_range",
                "SequenceNumberRange",
                TypeInfo(SequenceNumberRange),
            ),
            (
                "parent_shard_id",
                "ParentShardId",
                TypeInfo(str),
            ),
        ]

    # The system-generated identifier for this shard.
    shard_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The range of possible sequence numbers for the shard.
    sequence_number_range: "SequenceNumberRange" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The shard ID of the current shard's parent.
    parent_shard_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )


class ShardIteratorType(str):
    TRIM_HORIZON = "TRIM_HORIZON"
    LATEST = "LATEST"
    AT_SEQUENCE_NUMBER = "AT_SEQUENCE_NUMBER"
    AFTER_SEQUENCE_NUMBER = "AFTER_SEQUENCE_NUMBER"


@dataclasses.dataclass
class Stream(ShapeBase):
    """
    Represents all of the data describing a particular stream.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "stream_arn",
                "StreamArn",
                TypeInfo(str),
            ),
            (
                "table_name",
                "TableName",
                TypeInfo(str),
            ),
            (
                "stream_label",
                "StreamLabel",
                TypeInfo(str),
            ),
        ]

    # The Amazon Resource Name (ARN) for the stream.
    stream_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The DynamoDB table with which the stream is associated.
    table_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A timestamp, in ISO 8601 format, for this stream.

    # Note that `LatestStreamLabel` is not a unique identifier for the stream,
    # because it is possible that a stream from another table might have the same
    # timestamp. However, the combination of the following three elements is
    # guaranteed to be unique:

    #   * the AWS customer ID.

    #   * the table name

    #   * the `StreamLabel`
    stream_label: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class StreamDescription(ShapeBase):
    """
    Represents all of the data describing a particular stream.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "stream_arn",
                "StreamArn",
                TypeInfo(str),
            ),
            (
                "stream_label",
                "StreamLabel",
                TypeInfo(str),
            ),
            (
                "stream_status",
                "StreamStatus",
                TypeInfo(typing.Union[str, StreamStatus]),
            ),
            (
                "stream_view_type",
                "StreamViewType",
                TypeInfo(typing.Union[str, StreamViewType]),
            ),
            (
                "creation_request_date_time",
                "CreationRequestDateTime",
                TypeInfo(datetime.datetime),
            ),
            (
                "table_name",
                "TableName",
                TypeInfo(str),
            ),
            (
                "key_schema",
                "KeySchema",
                TypeInfo(typing.List[KeySchemaElement]),
            ),
            (
                "shards",
                "Shards",
                TypeInfo(typing.List[Shard]),
            ),
            (
                "last_evaluated_shard_id",
                "LastEvaluatedShardId",
                TypeInfo(str),
            ),
        ]

    # The Amazon Resource Name (ARN) for the stream.
    stream_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A timestamp, in ISO 8601 format, for this stream.

    # Note that `LatestStreamLabel` is not a unique identifier for the stream,
    # because it is possible that a stream from another table might have the same
    # timestamp. However, the combination of the following three elements is
    # guaranteed to be unique:

    #   * the AWS customer ID.

    #   * the table name

    #   * the `StreamLabel`
    stream_label: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Indicates the current status of the stream:

    #   * `ENABLING` \- Streams is currently being enabled on the DynamoDB table.

    #   * `ENABLED` \- the stream is enabled.

    #   * `DISABLING` \- Streams is currently being disabled on the DynamoDB table.

    #   * `DISABLED` \- the stream is disabled.
    stream_status: typing.Union[str, "StreamStatus"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Indicates the format of the records within this stream:

    #   * `KEYS_ONLY` \- only the key attributes of items that were modified in the DynamoDB table.

    #   * `NEW_IMAGE` \- entire items from the table, as they appeared after they were modified.

    #   * `OLD_IMAGE` \- entire items from the table, as they appeared before they were modified.

    #   * `NEW_AND_OLD_IMAGES` \- both the new and the old images of the items from the table.
    stream_view_type: typing.Union[str, "StreamViewType"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The date and time when the request to create this stream was issued.
    creation_request_date_time: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The DynamoDB table with which the stream is associated.
    table_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The key attribute(s) of the stream's DynamoDB table.
    key_schema: typing.List["KeySchemaElement"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The shards that comprise the stream.
    shards: typing.List["Shard"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The shard ID of the item where the operation stopped, inclusive of the
    # previous result set. Use this value to start a new operation, excluding
    # this value in the new request.

    # If `LastEvaluatedShardId` is empty, then the "last page" of results has
    # been processed and there is currently no more data to be retrieved.

    # If `LastEvaluatedShardId` is not empty, it does not necessarily mean that
    # there is more data in the result set. The only way to know when you have
    # reached the end of the result set is when `LastEvaluatedShardId` is empty.
    last_evaluated_shard_id: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class StreamRecord(ShapeBase):
    """
    A description of a single data modification that was performed on an item in a
    DynamoDB table.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "approximate_creation_date_time",
                "ApproximateCreationDateTime",
                TypeInfo(datetime.datetime),
            ),
            (
                "keys",
                "Keys",
                TypeInfo(typing.Dict[str, AttributeValue]),
            ),
            (
                "new_image",
                "NewImage",
                TypeInfo(typing.Dict[str, AttributeValue]),
            ),
            (
                "old_image",
                "OldImage",
                TypeInfo(typing.Dict[str, AttributeValue]),
            ),
            (
                "sequence_number",
                "SequenceNumber",
                TypeInfo(str),
            ),
            (
                "size_bytes",
                "SizeBytes",
                TypeInfo(int),
            ),
            (
                "stream_view_type",
                "StreamViewType",
                TypeInfo(typing.Union[str, StreamViewType]),
            ),
        ]

    # The approximate date and time when the stream record was created, in [UNIX
    # epoch time](http://www.epochconverter.com/) format.
    approximate_creation_date_time: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The primary key attribute(s) for the DynamoDB item that was modified.
    keys: typing.Dict[str, "AttributeValue"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The item in the DynamoDB table as it appeared after it was modified.
    new_image: typing.Dict[str, "AttributeValue"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The item in the DynamoDB table as it appeared before it was modified.
    old_image: typing.Dict[str, "AttributeValue"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The sequence number of the stream record.
    sequence_number: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The size of the stream record, in bytes.
    size_bytes: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The type of data from the modified DynamoDB item that was captured in this
    # stream record:

    #   * `KEYS_ONLY` \- only the key attributes of the modified item.

    #   * `NEW_IMAGE` \- the entire item, as it appeared after it was modified.

    #   * `OLD_IMAGE` \- the entire item, as it appeared before it was modified.

    #   * `NEW_AND_OLD_IMAGES` \- both the new and the old item images of the item.
    stream_view_type: typing.Union[str, "StreamViewType"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


class StreamStatus(str):
    ENABLING = "ENABLING"
    ENABLED = "ENABLED"
    DISABLING = "DISABLING"
    DISABLED = "DISABLED"


class StreamViewType(str):
    NEW_IMAGE = "NEW_IMAGE"
    OLD_IMAGE = "OLD_IMAGE"
    NEW_AND_OLD_IMAGES = "NEW_AND_OLD_IMAGES"
    KEYS_ONLY = "KEYS_ONLY"


@dataclasses.dataclass
class TrimmedDataAccessException(ShapeBase):
    """
    The operation attempted to read past the oldest stream record in a shard.

    In DynamoDB Streams, there is a 24 hour limit on data retention. Stream records
    whose age exceeds this limit are subject to removal (trimming) from the stream.
    You might receive a TrimmedDataAccessException if:

      * You request a shard iterator with a sequence number older than the trim point (24 hours).

      * You obtain a shard iterator, but before you use the iterator in a `GetRecords` request, a stream record in the shard exceeds the 24 hour period and is trimmed. This causes the iterator to access a record that no longer exists.
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

    # "The data you are trying to access has been trimmed.
    message: str = dataclasses.field(default=ShapeBase.NOT_SET, )
