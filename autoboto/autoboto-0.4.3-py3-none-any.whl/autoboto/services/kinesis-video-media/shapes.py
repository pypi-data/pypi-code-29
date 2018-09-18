import datetime
import typing
from autoboto import ShapeBase, OutputShapeBase, TypeInfo
import botocore.response
import dataclasses


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


@dataclasses.dataclass
class ConnectionLimitExceededException(ShapeBase):
    """
    Kinesis Video Streams has throttled the request because you have exceeded the
    limit of allowed client connections.
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
class GetMediaInput(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "start_selector",
                "StartSelector",
                TypeInfo(StartSelector),
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

    # Identifies the starting chunk to get from the specified stream.
    start_selector: "StartSelector" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The Kinesis video stream name from where you want to get the media content.
    # If you don't specify the `streamName`, you must specify the `streamARN`.
    stream_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The ARN of the stream from where you want to get the media content. If you
    # don't specify the `streamARN`, you must specify the `streamName`.
    stream_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class GetMediaOutput(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "content_type",
                "ContentType",
                TypeInfo(str),
            ),
            (
                "payload",
                "Payload",
                TypeInfo(typing.Any),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The content type of the requested media.
    content_type: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The payload Kinesis Video Streams returns is a sequence of chunks from the
    # specified stream. For information about the chunks, see . The chunks that
    # Kinesis Video Streams returns in the `GetMedia` call also include the
    # following additional Matroska (MKV) tags:

    #   * AWS_KINESISVIDEO_CONTINUATION_TOKEN (UTF-8 string) - In the event your `GetMedia` call terminates, you can use this continuation token in your next request to get the next chunk where the last request terminated.

    #   * AWS_KINESISVIDEO_MILLIS_BEHIND_NOW (UTF-8 string) - Client applications can use this tag value to determine how far behind the chunk returned in the response is from the latest chunk on the stream.

    #   * AWS_KINESISVIDEO_FRAGMENT_NUMBER - Fragment number returned in the chunk.

    #   * AWS_KINESISVIDEO_SERVER_TIMESTAMP - Server time stamp of the fragment.

    #   * AWS_KINESISVIDEO_PRODUCER_TIMESTAMP - Producer time stamp of the fragment.

    # The following tags will be present if an error occurs:

    #   * AWS_KINESISVIDEO_ERROR_CODE - String description of an error that caused GetMedia to stop.

    #   * AWS_KINESISVIDEO_ERROR_ID: Integer code of the error.

    # The error codes are as follows:

    #   * 3002 - Error writing to the stream

    #   * 4000 - Requested fragment is not found

    #   * 4500 - Access denied for the stream's KMS key

    #   * 4501 - Stream's KMS key is disabled

    #   * 4502 - Validation error on the Stream's KMS key

    #   * 4503 - KMS key specified in the stream is unavailable

    #   * 4504 - Invalid usage of the KMS key specified in the stream

    #   * 4505 - Invalid state of the KMS key specified in the stream

    #   * 4506 - Unable to find the KMS key specified in the stream

    #   * 5000 - Internal error
    payload: typing.Any = dataclasses.field(default=ShapeBase.NOT_SET, )


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
class InvalidEndpointException(ShapeBase):
    """
    Status Code: 400, Caller used wrong endpoint to write data to a stream. On
    receiving such an exception, the user must call `GetDataEndpoint` with
    `AccessMode` set to "READ" and use the endpoint Kinesis Video returns in the
    next `GetMedia` call.
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
class NotAuthorizedException(ShapeBase):
    """
    Status Code: 403, The caller is not authorized to perform an operation on the
    given stream, or the token has expired.
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


class Payload(botocore.response.StreamingBody):
    pass


@dataclasses.dataclass
class ResourceNotFoundException(ShapeBase):
    """
    Status Code: 404, The stream with the given name does not exist.
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
class StartSelector(ShapeBase):
    """
    Identifies the chunk on the Kinesis video stream where you want the `GetMedia`
    API to start returning media data. You have the following options to identify
    the starting chunk:

      * Choose the latest (or oldest) chunk.

      * Identify a specific chunk. You can identify a specific chunk either by providing a fragment number or time stamp (server or producer). 

      * Each chunk's metadata includes a continuation token as a Matroska (MKV) tag (`AWS_KINESISVIDEO_CONTINUATION_TOKEN`). If your previous `GetMedia` request terminated, you can use this tag value in your next `GetMedia` request. The API then starts returning chunks starting where the last API ended.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "start_selector_type",
                "StartSelectorType",
                TypeInfo(typing.Union[str, StartSelectorType]),
            ),
            (
                "after_fragment_number",
                "AfterFragmentNumber",
                TypeInfo(str),
            ),
            (
                "start_timestamp",
                "StartTimestamp",
                TypeInfo(datetime.datetime),
            ),
            (
                "continuation_token",
                "ContinuationToken",
                TypeInfo(str),
            ),
        ]

    # Identifies the fragment on the Kinesis video stream where you want to start
    # getting the data from.

    #   * NOW - Start with the latest chunk on the stream.

    #   * EARLIEST - Start with earliest available chunk on the stream.

    #   * FRAGMENT_NUMBER - Start with the chunk containing the specific fragment. You must also specify the `StartFragmentNumber`.

    #   * PRODUCER_TIMESTAMP or SERVER_TIMESTAMP - Start with the chunk containing a fragment with the specified producer or server time stamp. You specify the time stamp by adding `StartTimestamp`.

    #   * CONTINUATION_TOKEN - Read using the specified continuation token.

    # If you choose the NOW, EARLIEST, or CONTINUATION_TOKEN as the
    # `startSelectorType`, you don't provide any additional information in the
    # `startSelector`.
    start_selector_type: typing.Union[str, "StartSelectorType"
                                     ] = dataclasses.field(
                                         default=ShapeBase.NOT_SET,
                                     )

    # Specifies the fragment number from where you want the `GetMedia` API to
    # start returning the fragments.
    after_fragment_number: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A time stamp value. This value is required if you choose the
    # PRODUCER_TIMESTAMP or the SERVER_TIMESTAMP as the `startSelectorType`. The
    # `GetMedia` API then starts with the chunk containing the fragment that has
    # the specified time stamp.
    start_timestamp: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Continuation token that Kinesis Video Streams returned in the previous
    # `GetMedia` response. The `GetMedia` API then starts with the chunk
    # identified by the continuation token.
    continuation_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )


class StartSelectorType(str):
    FRAGMENT_NUMBER = "FRAGMENT_NUMBER"
    SERVER_TIMESTAMP = "SERVER_TIMESTAMP"
    PRODUCER_TIMESTAMP = "PRODUCER_TIMESTAMP"
    NOW = "NOW"
    EARLIEST = "EARLIEST"
    CONTINUATION_TOKEN = "CONTINUATION_TOKEN"
