import datetime
import typing
from autoboto import ShapeBase, OutputShapeBase, TypeInfo
import dataclasses


class APIName(str):
    PUT_MEDIA = "PUT_MEDIA"
    GET_MEDIA = "GET_MEDIA"
    LIST_FRAGMENTS = "LIST_FRAGMENTS"
    GET_MEDIA_FOR_FRAGMENT_LIST = "GET_MEDIA_FOR_FRAGMENT_LIST"
    GET_HLS_STREAMING_SESSION_URL = "GET_HLS_STREAMING_SESSION_URL"


@dataclasses.dataclass
class AccountStreamLimitExceededException(ShapeBase):
    """
    The number of streams created for the account is too high.
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
class ClientLimitExceededException(ShapeBase):
    """
    Kinesis Video Streams has throttled the request because you have exceeded the
    limit of allowed client calls. Try making the call later.
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


class ComparisonOperator(str):
    BEGINS_WITH = "BEGINS_WITH"


@dataclasses.dataclass
class CreateStreamInput(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "stream_name",
                "StreamName",
                TypeInfo(str),
            ),
            (
                "device_name",
                "DeviceName",
                TypeInfo(str),
            ),
            (
                "media_type",
                "MediaType",
                TypeInfo(str),
            ),
            (
                "kms_key_id",
                "KmsKeyId",
                TypeInfo(str),
            ),
            (
                "data_retention_in_hours",
                "DataRetentionInHours",
                TypeInfo(int),
            ),
        ]

    # A name for the stream that you are creating.

    # The stream name is an identifier for the stream, and must be unique for
    # each account and region.
    stream_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The name of the device that is writing to the stream.

    # In the current implementation, Kinesis Video Streams does not use this
    # name.
    device_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The media type of the stream. Consumers of the stream can use this
    # information when processing the stream. For more information about media
    # types, see [Media Types](http://www.iana.org/assignments/media-types/media-
    # types.xhtml). If you choose to specify the `MediaType`, see [Naming
    # Requirements](https://tools.ietf.org/html/rfc6838#section-4.2) for
    # guidelines.

    # To play video on the console, the media must be H.264 encoded, and you need
    # to specify this video type in this parameter as `video/h264`.

    # This parameter is optional; the default value is `null` (or empty in JSON).
    media_type: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The ID of the AWS Key Management Service (AWS KMS) key that you want
    # Kinesis Video Streams to use to encrypt stream data.

    # If no key ID is specified, the default, Kinesis Video-managed key
    # (`aws/kinesisvideo`) is used.

    # For more information, see
    # [DescribeKey](http://docs.aws.amazon.com/kms/latest/APIReference/API_DescribeKey.html#API_DescribeKey_RequestParameters).
    kms_key_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The number of hours that you want to retain the data in the stream. Kinesis
    # Video Streams retains the data in a data store that is associated with the
    # stream.

    # The default value is 0, indicating that the stream does not persist data.

    # When the `DataRetentionInHours` value is 0, consumers can still consume the
    # fragments that remain in the service host buffer, which has a retention
    # time limit of 5 minutes and a retention memory limit of 200 MB. Fragments
    # are removed from the buffer when either limit is reached.
    data_retention_in_hours: int = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class CreateStreamOutput(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "stream_arn",
                "StreamARN",
                TypeInfo(str),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The Amazon Resource Name (ARN) of the stream.
    stream_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DeleteStreamInput(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "stream_arn",
                "StreamARN",
                TypeInfo(str),
            ),
            (
                "current_version",
                "CurrentVersion",
                TypeInfo(str),
            ),
        ]

    # The Amazon Resource Name (ARN) of the stream that you want to delete.
    stream_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Optional: The version of the stream that you want to delete.

    # Specify the version as a safeguard to ensure that your are deleting the
    # correct stream. To get the stream version, use the `DescribeStream` API.

    # If not specified, only the `CreationTime` is checked before deleting the
    # stream.
    current_version: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DeleteStreamOutput(OutputShapeBase):
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
class DescribeStreamInput(ShapeBase):
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
        ]

    # The name of the stream.
    stream_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The Amazon Resource Name (ARN) of the stream.
    stream_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DescribeStreamOutput(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "stream_info",
                "StreamInfo",
                TypeInfo(StreamInfo),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # An object that describes the stream.
    stream_info: "StreamInfo" = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DeviceStreamLimitExceededException(ShapeBase):
    """
    Not implemented.
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
class GetDataEndpointInput(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "api_name",
                "APIName",
                TypeInfo(typing.Union[str, APIName]),
            ),
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
        ]

    # The name of the API action for which to get an endpoint.
    api_name: typing.Union[str, "APIName"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The name of the stream that you want to get the endpoint for. You must
    # specify either this parameter or a `StreamARN` in the request.
    stream_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The Amazon Resource Name (ARN) of the stream that you want to get the
    # endpoint for. You must specify either this parameter or a `StreamName` in
    # the request.
    stream_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class GetDataEndpointOutput(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "data_endpoint",
                "DataEndpoint",
                TypeInfo(str),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The endpoint value. To read data from the stream or to write data to it,
    # specify this endpoint in your application.
    data_endpoint: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class InvalidArgumentException(ShapeBase):
    """
    The value for this input parameter is invalid.
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
class InvalidDeviceException(ShapeBase):
    """
    Not implemented.
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
class InvalidResourceFormatException(ShapeBase):
    """
    The format of the `StreamARN` is invalid.
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
class ListStreamsInput(ShapeBase):
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
            (
                "stream_name_condition",
                "StreamNameCondition",
                TypeInfo(StreamNameCondition),
            ),
        ]

    # The maximum number of streams to return in the response. The default is
    # 10,000.
    max_results: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # If you specify this parameter, when the result of a `ListStreams` operation
    # is truncated, the call returns the `NextToken` in the response. To get
    # another batch of streams, provide this token in your next request.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Optional: Returns only streams that satisfy a specific condition.
    # Currently, you can specify only the prefix of a stream name as a condition.
    stream_name_condition: "StreamNameCondition" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class ListStreamsOutput(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "stream_info_list",
                "StreamInfoList",
                TypeInfo(typing.List[StreamInfo]),
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

    # An array of `StreamInfo` objects.
    stream_info_list: typing.List["StreamInfo"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # If the response is truncated, the call returns this element with a token.
    # To get the next batch of streams, use this token in your next request.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ListTagsForStreamInput(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "next_token",
                "NextToken",
                TypeInfo(str),
            ),
            (
                "stream_arn",
                "StreamARN",
                TypeInfo(str),
            ),
            (
                "stream_name",
                "StreamName",
                TypeInfo(str),
            ),
        ]

    # If you specify this parameter and the result of a `ListTagsForStream` call
    # is truncated, the response includes a token that you can use in the next
    # request to fetch the next batch of tags.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The Amazon Resource Name (ARN) of the stream that you want to list tags
    # for.
    stream_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The name of the stream that you want to list tags for.
    stream_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ListTagsForStreamOutput(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "next_token",
                "NextToken",
                TypeInfo(str),
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

    # If you specify this parameter and the result of a `ListTags` call is
    # truncated, the response includes a token that you can use in the next
    # request to fetch the next set of tags.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A map of tag keys and values associated with the specified stream.
    tags: typing.Dict[str, str] = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class NotAuthorizedException(ShapeBase):
    """
    The caller is not authorized to perform this operation.
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
class ResourceInUseException(ShapeBase):
    """
    The stream is currently not available for this operation.
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
class ResourceNotFoundException(ShapeBase):
    """
    Amazon Kinesis Video Streams can't find the stream that you specified.
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


class Status(str):
    CREATING = "CREATING"
    ACTIVE = "ACTIVE"
    UPDATING = "UPDATING"
    DELETING = "DELETING"


@dataclasses.dataclass
class StreamInfo(ShapeBase):
    """
    An object describing a Kinesis video stream.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "device_name",
                "DeviceName",
                TypeInfo(str),
            ),
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
                "media_type",
                "MediaType",
                TypeInfo(str),
            ),
            (
                "kms_key_id",
                "KmsKeyId",
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
                TypeInfo(typing.Union[str, Status]),
            ),
            (
                "creation_time",
                "CreationTime",
                TypeInfo(datetime.datetime),
            ),
            (
                "data_retention_in_hours",
                "DataRetentionInHours",
                TypeInfo(int),
            ),
        ]

    # The name of the device that is associated with the stream.
    device_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The name of the stream.
    stream_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The Amazon Resource Name (ARN) of the stream.
    stream_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The `MediaType` of the stream.
    media_type: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The ID of the AWS Key Management Service (AWS KMS) key that Kinesis Video
    # Streams uses to encrypt data on the stream.
    kms_key_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The version of the stream.
    version: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The status of the stream.
    status: typing.Union[str, "Status"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A time stamp that indicates when the stream was created.
    creation_time: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # How long the stream retains data, in hours.
    data_retention_in_hours: int = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class StreamNameCondition(ShapeBase):
    """
    Specifies the condition that streams must satisfy to be returned when you list
    streams (see the `ListStreams` API). A condition has a comparison operation and
    a value. Currently, you can specify only the `BEGINS_WITH` operator, which finds
    streams whose names start with a given prefix.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "comparison_operator",
                "ComparisonOperator",
                TypeInfo(typing.Union[str, ComparisonOperator]),
            ),
            (
                "comparison_value",
                "ComparisonValue",
                TypeInfo(str),
            ),
        ]

    # A comparison operator. Currently, you can specify only the `BEGINS_WITH`
    # operator, which finds streams whose names start with a given prefix.
    comparison_operator: typing.Union[str, "ComparisonOperator"
                                     ] = dataclasses.field(
                                         default=ShapeBase.NOT_SET,
                                     )

    # A value to compare.
    comparison_value: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class TagStreamInput(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "tags",
                "Tags",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "stream_arn",
                "StreamARN",
                TypeInfo(str),
            ),
            (
                "stream_name",
                "StreamName",
                TypeInfo(str),
            ),
        ]

    # A list of tags to associate with the specified stream. Each tag is a key-
    # value pair (the value is optional).
    tags: typing.Dict[str, str] = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The Amazon Resource Name (ARN) of the resource that you want to add the tag
    # or tags to.
    stream_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The name of the stream that you want to add the tag or tags to.
    stream_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class TagStreamOutput(OutputShapeBase):
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
class TagsPerResourceExceededLimitException(ShapeBase):
    """
    You have exceeded the limit of tags that you can associate with the resource.
    Kinesis video streams support up to 50 tags.
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
class UntagStreamInput(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "tag_key_list",
                "TagKeyList",
                TypeInfo(typing.List[str]),
            ),
            (
                "stream_arn",
                "StreamARN",
                TypeInfo(str),
            ),
            (
                "stream_name",
                "StreamName",
                TypeInfo(str),
            ),
        ]

    # A list of the keys of the tags that you want to remove.
    tag_key_list: typing.List[str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The Amazon Resource Name (ARN) of the stream that you want to remove tags
    # from.
    stream_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The name of the stream that you want to remove tags from.
    stream_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class UntagStreamOutput(OutputShapeBase):
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
class UpdateDataRetentionInput(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "current_version",
                "CurrentVersion",
                TypeInfo(str),
            ),
            (
                "operation",
                "Operation",
                TypeInfo(typing.Union[str, UpdateDataRetentionOperation]),
            ),
            (
                "data_retention_change_in_hours",
                "DataRetentionChangeInHours",
                TypeInfo(int),
            ),
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
        ]

    # The version of the stream whose retention period you want to change. To get
    # the version, call either the `DescribeStream` or the `ListStreams` API.
    current_version: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Indicates whether you want to increase or decrease the retention period.
    operation: typing.Union[str, "UpdateDataRetentionOperation"
                           ] = dataclasses.field(
                               default=ShapeBase.NOT_SET,
                           )

    # The retention period, in hours. The value you specify replaces the current
    # value.
    data_retention_change_in_hours: int = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The name of the stream whose retention period you want to change.
    stream_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The Amazon Resource Name (ARN) of the stream whose retention period you
    # want to change.
    stream_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )


class UpdateDataRetentionOperation(str):
    INCREASE_DATA_RETENTION = "INCREASE_DATA_RETENTION"
    DECREASE_DATA_RETENTION = "DECREASE_DATA_RETENTION"


@dataclasses.dataclass
class UpdateDataRetentionOutput(OutputShapeBase):
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
class UpdateStreamInput(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "current_version",
                "CurrentVersion",
                TypeInfo(str),
            ),
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
                "device_name",
                "DeviceName",
                TypeInfo(str),
            ),
            (
                "media_type",
                "MediaType",
                TypeInfo(str),
            ),
        ]

    # The version of the stream whose metadata you want to update.
    current_version: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The name of the stream whose metadata you want to update.

    # The stream name is an identifier for the stream, and must be unique for
    # each account and region.
    stream_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The ARN of the stream whose metadata you want to update.
    stream_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The name of the device that is writing to the stream.

    # In the current implementation, Kinesis Video Streams does not use this
    # name.
    device_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The stream's media type. Use `MediaType` to specify the type of content
    # that the stream contains to the consumers of the stream. For more
    # information about media types, see [Media
    # Types](http://www.iana.org/assignments/media-types/media-types.xhtml). If
    # you choose to specify the `MediaType`, see [Naming
    # Requirements](https://tools.ietf.org/html/rfc6838#section-4.2).

    # To play video on the console, you must specify the correct video type. For
    # example, if the video in the stream is H.264, specify `video/h264` as the
    # `MediaType`.
    media_type: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class UpdateStreamOutput(OutputShapeBase):
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
class VersionMismatchException(ShapeBase):
    """
    The stream version that you specified is not the latest version. To get the
    latest version, use the
    [DescribeStream](http://docs.aws.amazon.com/kinesisvideostreams/latest/dg/API_DescribeStream.html)
    API.
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
