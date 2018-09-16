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


class DiscontinuityMode(str):
    ALWAYS = "ALWAYS"
    NEVER = "NEVER"


@dataclasses.dataclass
class Fragment(ShapeBase):
    """
    Represents a segment of video or other time-delimited data.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "fragment_number",
                "FragmentNumber",
                TypeInfo(str),
            ),
            (
                "fragment_size_in_bytes",
                "FragmentSizeInBytes",
                TypeInfo(int),
            ),
            (
                "producer_timestamp",
                "ProducerTimestamp",
                TypeInfo(datetime.datetime),
            ),
            (
                "server_timestamp",
                "ServerTimestamp",
                TypeInfo(datetime.datetime),
            ),
            (
                "fragment_length_in_milliseconds",
                "FragmentLengthInMilliseconds",
                TypeInfo(int),
            ),
        ]

    # The index value of the fragment.
    fragment_number: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The total fragment size, including information about the fragment and
    # contained media data.
    fragment_size_in_bytes: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The time stamp from the producer corresponding to the fragment.
    producer_timestamp: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The time stamp from the AWS server corresponding to the fragment.
    server_timestamp: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The playback duration or other time value associated with the fragment.
    fragment_length_in_milliseconds: int = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class FragmentSelector(ShapeBase):
    """
    Describes the time stamp range and time stamp origin of a range of fragments.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "fragment_selector_type",
                "FragmentSelectorType",
                TypeInfo(typing.Union[str, FragmentSelectorType]),
            ),
            (
                "timestamp_range",
                "TimestampRange",
                TypeInfo(TimestampRange),
            ),
        ]

    # The origin of the time stamps to use (Server or Producer).
    fragment_selector_type: typing.Union[str, "FragmentSelectorType"
                                        ] = dataclasses.field(
                                            default=ShapeBase.NOT_SET,
                                        )

    # The range of time stamps to return.
    timestamp_range: "TimestampRange" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


class FragmentSelectorType(str):
    PRODUCER_TIMESTAMP = "PRODUCER_TIMESTAMP"
    SERVER_TIMESTAMP = "SERVER_TIMESTAMP"


@dataclasses.dataclass
class GetHLSStreamingSessionURLInput(ShapeBase):
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
                "playback_mode",
                "PlaybackMode",
                TypeInfo(typing.Union[str, PlaybackMode]),
            ),
            (
                "hls_fragment_selector",
                "HLSFragmentSelector",
                TypeInfo(HLSFragmentSelector),
            ),
            (
                "discontinuity_mode",
                "DiscontinuityMode",
                TypeInfo(typing.Union[str, DiscontinuityMode]),
            ),
            (
                "expires",
                "Expires",
                TypeInfo(int),
            ),
            (
                "max_media_playlist_fragment_results",
                "MaxMediaPlaylistFragmentResults",
                TypeInfo(int),
            ),
        ]

    # The name of the stream for which to retrieve the HLS master playlist URL.

    # You must specify either the `StreamName` or the `StreamARN`.
    stream_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The Amazon Resource Name (ARN) of the stream for which to retrieve the HLS
    # master playlist URL.

    # You must specify either the `StreamName` or the `StreamARN`.
    stream_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Whether to retrieve live or archived, on-demand data.

    # Features of the two types of session include the following:

    #   * **`LIVE` ** : For sessions of this type, the HLS media playlist is continually updated with the latest fragments as they become available. We recommend that the media player retrieve a new playlist on a one-second interval. When this type of session is played in a media player, the user interface typically displays a "live" notification, with no scrubber control for choosing the position in the playback window to display.

    # In `LIVE` mode, the newest available fragments are included in an HLS media
    # playlist, even if there is a gap between fragments (that is, if a fragment
    # is missing). A gap like this might cause a media player to halt or cause a
    # jump in playback. In this mode, fragments are not added to the HLS media
    # playlist if they are older than the newest fragment in the playlist. If the
    # missing fragment becomes available after a subsequent fragment is added to
    # the playlist, the older fragment is not added, and the gap is not filled.

    #   * **`ON_DEMAND` ** : For sessions of this type, the HLS media playlist contains all the fragments for the session, up to the number that is specified in `MaxMediaPlaylistFragmentResults`. The playlist must be retrieved only once for each session. When this type of session is played in a media player, the user interface typically displays a scrubber control for choosing the position in the playback window to display.

    # In both playback modes, if `FragmentSelectorType` is `PRODUCER_TIMESTAMP`,
    # and if there are multiple fragments with the same start time stamp, the
    # fragment that has the larger fragment number (that is, the newer fragment)
    # is included in the HLS media playlist. The other fragments are not
    # included. Fragments that have different time stamps but have overlapping
    # durations are still included in the HLS media playlist. This can lead to
    # unexpected behavior in the media player.

    # The default is `LIVE`.
    playback_mode: typing.Union[str, "PlaybackMode"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The time range of the requested fragment, and the source of the time
    # stamps.

    # This parameter is required if `PlaybackMode` is `ON_DEMAND`. This parameter
    # is optional if `PlaybackMode` is `LIVE`. If `PlaybackMode` is `LIVE`, the
    # `FragmentSelectorType` can be set, but the `TimestampRange` should not be
    # set. If `PlaybackMode` is `ON_DEMAND`, both `FragmentSelectorType` and
    # `TimestampRange` must be set.
    hls_fragment_selector: "HLSFragmentSelector" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Specifies when flags marking discontinuities between fragments will be
    # added to the media playlists. The default is `ALWAYS` when
    # HLSFragmentSelector is `SERVER_TIMESTAMP`, and `NEVER` when it is
    # `PRODUCER_TIMESTAMP`.

    # Media players typically build a timeline of media content to play, based on
    # the time stamps of each fragment. This means that if there is any overlap
    # between fragments (as is typical if HLSFragmentSelector is
    # `SERVER_TIMESTAMP`), the media player timeline has small gaps between
    # fragments in some places, and overwrites frames in other places. When there
    # are discontinuity flags between fragments, the media player is expected to
    # reset the timeline, resulting in the fragment being played immediately
    # after the previous fragment. We recommend that you always have
    # discontinuity flags between fragments if the fragment time stamps are not
    # accurate or if fragments might be missing. You should not place
    # discontinuity flags between fragments for the player timeline to accurately
    # map to the producer time stamps.
    discontinuity_mode: typing.Union[str, "DiscontinuityMode"
                                    ] = dataclasses.field(
                                        default=ShapeBase.NOT_SET,
                                    )

    # The time in seconds until the requested session expires. This value can be
    # between 300 (5 minutes) and 43200 (12 hours).

    # When a session expires, no new calls to `GetHLSMasterPlaylist`,
    # `GetHLSMediaPlaylist`, `GetMP4InitFragment`, or `GetMP4MediaFragment` can
    # be made for that session.

    # The default is 300 (5 minutes).
    expires: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The maximum number of fragments that are returned in the HLS media
    # playlists.

    # When the `PlaybackMode` is `LIVE`, the most recent fragments are returned
    # up to this value. When the `PlaybackMode` is `ON_DEMAND`, the oldest
    # fragments are returned, up to this maximum number.

    # When there are a higher number of fragments available in a live HLS media
    # playlist, video players often buffer content before starting playback.
    # Increasing the buffer size increases the playback latency, but it decreases
    # the likelihood that rebuffering will occur during playback. We recommend
    # that a live HLS media playlist have a minimum of 3 fragments and a maximum
    # of 10 fragments.

    # The default is 5 fragments if `PlaybackMode` is `LIVE`, and 1,000 if
    # `PlaybackMode` is `ON_DEMAND`.

    # The maximum value of 1,000 fragments corresponds to more than 16 minutes of
    # video on streams with 1-second fragments, and more than 2 1/2 hours of
    # video on streams with 10-second fragments.
    max_media_playlist_fragment_results: int = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class GetHLSStreamingSessionURLOutput(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "hls_streaming_session_url",
                "HLSStreamingSessionURL",
                TypeInfo(str),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The URL (containing the session token) that a media player can use to
    # retrieve the HLS master playlist.
    hls_streaming_session_url: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class GetMediaForFragmentListInput(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "stream_name",
                "StreamName",
                TypeInfo(str),
            ),
            (
                "fragments",
                "Fragments",
                TypeInfo(typing.List[str]),
            ),
        ]

    # The name of the stream from which to retrieve fragment media.
    stream_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A list of the numbers of fragments for which to retrieve media. You
    # retrieve these values with ListFragments.
    fragments: typing.List[str] = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class GetMediaForFragmentListOutput(OutputShapeBase):
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

    # The payload that Kinesis Video Streams returns is a sequence of chunks from
    # the specified stream. For information about the chunks, see
    # [PutMedia](http://docs.aws.amazon.com/kinesisvideostreams/latest/dg/API_dataplane_PutMedia.html).
    # The chunks that Kinesis Video Streams returns in the
    # `GetMediaForFragmentList` call also include the following additional
    # Matroska (MKV) tags:

    #   * AWS_KINESISVIDEO_FRAGMENT_NUMBER - Fragment number returned in the chunk.

    #   * AWS_KINESISVIDEO_SERVER_SIDE_TIMESTAMP - Server-side time stamp of the fragment.

    #   * AWS_KINESISVIDEO_PRODUCER_SIDE_TIMESTAMP - Producer-side time stamp of the fragment.

    # The following tags will be included if an exception occurs:

    #   * AWS_KINESISVIDEO_FRAGMENT_NUMBER - The number of the fragment that threw the exception

    #   * AWS_KINESISVIDEO_EXCEPTION_ERROR_CODE - The integer code of the exception

    #   * AWS_KINESISVIDEO_EXCEPTION_MESSAGE - A text description of the exception
    payload: typing.Any = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class HLSFragmentSelector(ShapeBase):
    """
    Contains the range of time stamps for the requested media, and the source of the
    time stamps.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "fragment_selector_type",
                "FragmentSelectorType",
                TypeInfo(typing.Union[str, HLSFragmentSelectorType]),
            ),
            (
                "timestamp_range",
                "TimestampRange",
                TypeInfo(HLSTimestampRange),
            ),
        ]

    # The source of the time stamps for the requested media.

    # When `FragmentSelectorType` is set to `PRODUCER_TIMESTAMP` and
    # GetHLSStreamingSessionURLInput$PlaybackMode is `ON_DEMAND`, the first
    # fragment ingested with a producer time stamp within the specified
    # FragmentSelector$TimestampRange is included in the media playlist. In
    # addition, the fragments with producer time stamps within the
    # `TimestampRange` ingested immediately following the first fragment (up to
    # the GetHLSStreamingSessionURLInput$MaxMediaPlaylistFragmentResults value)
    # are included.

    # Fragments that have duplicate producer time stamps are deduplicated. This
    # means that if producers are producing a stream of fragments with producer
    # time stamps that are approximately equal to the true clock time, the HLS
    # media playlists will contain all of the fragments within the requested time
    # stamp range. If some fragments are ingested within the same time range and
    # very different points in time, only the oldest ingested collection of
    # fragments are returned.

    # When `FragmentSelectorType` is set to `PRODUCER_TIMESTAMP` and
    # GetHLSStreamingSessionURLInput$PlaybackMode is `LIVE`, the producer time
    # stamps are used in the MP4 fragments and for deduplication. But the most
    # recently ingested fragments based on server time stamps are included in the
    # HLS media playlist. This means that even if fragments ingested in the past
    # have producer time stamps with values now, they are not included in the HLS
    # media playlist.

    # The default is `SERVER_TIMESTAMP`.
    fragment_selector_type: typing.Union[str, "HLSFragmentSelectorType"
                                        ] = dataclasses.field(
                                            default=ShapeBase.NOT_SET,
                                        )

    # The start and end of the time stamp range for the requested media.

    # This value should not be present if `PlaybackType` is `LIVE`.
    timestamp_range: "HLSTimestampRange" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


class HLSFragmentSelectorType(str):
    PRODUCER_TIMESTAMP = "PRODUCER_TIMESTAMP"
    SERVER_TIMESTAMP = "SERVER_TIMESTAMP"


@dataclasses.dataclass
class HLSTimestampRange(ShapeBase):
    """
    The start and end of the time stamp range for the requested media.

    This value should not be present if `PlaybackType` is `LIVE`.

    The values in the `HLSTimestampRange` are inclusive. Fragments that begin before
    the start time but continue past it, or fragments that begin before the end time
    but continue past it, are included in the session.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "start_timestamp",
                "StartTimestamp",
                TypeInfo(datetime.datetime),
            ),
            (
                "end_timestamp",
                "EndTimestamp",
                TypeInfo(datetime.datetime),
            ),
        ]

    # The start of the time stamp range for the requested media.

    # If the `HLSTimestampRange` value is specified, the `StartTimestamp` value
    # is required.

    # This value is inclusive. Fragments that start before the `StartTimestamp`
    # and continue past it are included in the session. If `FragmentSelectorType`
    # is `SERVER_TIMESTAMP`, the `StartTimestamp` must be later than the stream
    # head.
    start_timestamp: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The end of the time stamp range for the requested media. This value must be
    # within 3 hours of the specified `StartTimestamp`, and it must be later than
    # the `StartTimestamp` value.

    # If `FragmentSelectorType` for the request is `SERVER_TIMESTAMP`, this value
    # must be in the past.

    # If the `HLSTimestampRange` value is specified, the `EndTimestamp` value is
    # required.

    # This value is inclusive. The `EndTimestamp` is compared to the (starting)
    # time stamp of the fragment. Fragments that start before the `EndTimestamp`
    # value and continue past it are included in the session.
    end_timestamp: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class InvalidArgumentException(ShapeBase):
    """
    A specified parameter exceeds its restrictions, is not supported, or can't be
    used.
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
class InvalidCodecPrivateDataException(ShapeBase):
    """
    The Codec Private Data in the video stream is not valid for this operation.
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
class ListFragmentsInput(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "stream_name",
                "StreamName",
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
                "fragment_selector",
                "FragmentSelector",
                TypeInfo(FragmentSelector),
            ),
        ]

    # The name of the stream from which to retrieve a fragment list.
    stream_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The total number of fragments to return. If the total number of fragments
    # available is more than the value specified in `max-results`, then a
    # ListFragmentsOutput$NextToken is provided in the output that you can use to
    # resume pagination.
    max_results: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A token to specify where to start paginating. This is the
    # ListFragmentsOutput$NextToken from a previously truncated response.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Describes the time stamp range and time stamp origin for the range of
    # fragments to return.
    fragment_selector: "FragmentSelector" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class ListFragmentsOutput(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "fragments",
                "Fragments",
                TypeInfo(typing.List[Fragment]),
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

    # A list of fragment numbers that correspond to the time stamp range
    # provided.
    fragments: typing.List["Fragment"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # If the returned list is truncated, the operation returns this token to use
    # to retrieve the next page of results. This value is `null` when there are
    # no more results to return.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class MissingCodecPrivateDataException(ShapeBase):
    """
    No Codec Private Data was found in the video stream.
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
class NoDataRetentionException(ShapeBase):
    """
    A `PlaybackMode` of `ON_DEMAND` was requested for a stream that does not retain
    data (that is, has a `DataRetentionInHours` of 0).
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


class PlaybackMode(str):
    LIVE = "LIVE"
    ON_DEMAND = "ON_DEMAND"


@dataclasses.dataclass
class ResourceNotFoundException(ShapeBase):
    """
    `GetMedia` throws this error when Kinesis Video Streams can't find the stream
    that you specified.

    `GetHLSStreamingSessionURL` throws this error if a session with a `PlaybackMode`
    of `ON_DEMAND` is requested for a stream that has no fragments within the
    requested time range, or if a session with a `PlaybackMode` of `LIVE` is
    requested for a stream that has no fragments within the last 30 seconds.
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
class TimestampRange(ShapeBase):
    """
    The range of time stamps for which to return fragments.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "start_timestamp",
                "StartTimestamp",
                TypeInfo(datetime.datetime),
            ),
            (
                "end_timestamp",
                "EndTimestamp",
                TypeInfo(datetime.datetime),
            ),
        ]

    # The starting time stamp in the range of time stamps for which to return
    # fragments.
    start_timestamp: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The ending time stamp in the range of time stamps for which to return
    # fragments.
    end_timestamp: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class UnsupportedStreamMediaTypeException(ShapeBase):
    """
    An HLS streaming session was requested for a stream with a media type that is
    not `video/h264`.
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
