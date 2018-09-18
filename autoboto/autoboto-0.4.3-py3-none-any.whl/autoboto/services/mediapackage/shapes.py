import datetime
import typing
from autoboto import ShapeBase, OutputShapeBase, TypeInfo
import dataclasses


class AdMarkers(str):
    NONE = "NONE"
    SCTE35_ENHANCED = "SCTE35_ENHANCED"
    PASSTHROUGH = "PASSTHROUGH"


@dataclasses.dataclass
class Channel(ShapeBase):
    """
    A Channel resource configuration.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "arn",
                "Arn",
                TypeInfo(str),
            ),
            (
                "description",
                "Description",
                TypeInfo(str),
            ),
            (
                "hls_ingest",
                "HlsIngest",
                TypeInfo(HlsIngest),
            ),
            (
                "id",
                "Id",
                TypeInfo(str),
            ),
        ]

    # The Amazon Resource Name (ARN) assigned to the Channel.
    arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A short text description of the Channel.
    description: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # An HTTP Live Streaming (HLS) ingest resource configuration.
    hls_ingest: "HlsIngest" = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The ID of the Channel.
    id: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ChannelCreateParameters(ShapeBase):
    """
    Configuration parameters for a new Channel.
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
                "description",
                "Description",
                TypeInfo(str),
            ),
        ]

    # The ID of the Channel. The ID must be unique within the region and it
    # cannot be changed after a Channel is created.
    id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A short text description of the Channel.
    description: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ChannelList(ShapeBase):
    """
    A collection of Channel records.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "channels",
                "Channels",
                TypeInfo(typing.List[Channel]),
            ),
            (
                "next_token",
                "NextToken",
                TypeInfo(str),
            ),
        ]

    # A list of Channel records.
    channels: typing.List["Channel"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A token that can be used to resume pagination from the end of the
    # collection.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ChannelUpdateParameters(ShapeBase):
    """
    Configuration parameters for updating an existing Channel.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "description",
                "Description",
                TypeInfo(str),
            ),
        ]

    # A short text description of the Channel.
    description: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class CmafEncryption(ShapeBase):
    """
    A Common Media Application Format (CMAF) encryption configuration.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "speke_key_provider",
                "SpekeKeyProvider",
                TypeInfo(SpekeKeyProvider),
            ),
            (
                "key_rotation_interval_seconds",
                "KeyRotationIntervalSeconds",
                TypeInfo(int),
            ),
        ]

    # A configuration for accessing an external Secure Packager and Encoder Key
    # Exchange (SPEKE) service that will provide encryption keys.
    speke_key_provider: "SpekeKeyProvider" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Time (in seconds) between each encryption key rotation.
    key_rotation_interval_seconds: int = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class CmafPackage(ShapeBase):
    """
    A Common Media Application Format (CMAF) packaging configuration.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "encryption",
                "Encryption",
                TypeInfo(CmafEncryption),
            ),
            (
                "hls_manifests",
                "HlsManifests",
                TypeInfo(typing.List[HlsManifest]),
            ),
            (
                "segment_duration_seconds",
                "SegmentDurationSeconds",
                TypeInfo(int),
            ),
            (
                "segment_prefix",
                "SegmentPrefix",
                TypeInfo(str),
            ),
            (
                "stream_selection",
                "StreamSelection",
                TypeInfo(StreamSelection),
            ),
        ]

    # A Common Media Application Format (CMAF) encryption configuration.
    encryption: "CmafEncryption" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A list of HLS manifest configurations
    hls_manifests: typing.List["HlsManifest"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Duration (in seconds) of each segment. Actual segments will be rounded to
    # the nearest multiple of the source segment duration.
    segment_duration_seconds: int = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # An optional custom string that is prepended to the name of each segment. If
    # not specified, it defaults to the ChannelId.
    segment_prefix: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A StreamSelection configuration.
    stream_selection: "StreamSelection" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class CmafPackageCreateOrUpdateParameters(ShapeBase):
    """
    A Common Media Application Format (CMAF) packaging configuration.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "encryption",
                "Encryption",
                TypeInfo(CmafEncryption),
            ),
            (
                "hls_manifests",
                "HlsManifests",
                TypeInfo(typing.List[HlsManifestCreateOrUpdateParameters]),
            ),
            (
                "segment_duration_seconds",
                "SegmentDurationSeconds",
                TypeInfo(int),
            ),
            (
                "segment_prefix",
                "SegmentPrefix",
                TypeInfo(str),
            ),
            (
                "stream_selection",
                "StreamSelection",
                TypeInfo(StreamSelection),
            ),
        ]

    # A Common Media Application Format (CMAF) encryption configuration.
    encryption: "CmafEncryption" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A list of HLS manifest configurations
    hls_manifests: typing.List["HlsManifestCreateOrUpdateParameters"
                              ] = dataclasses.field(
                                  default=ShapeBase.NOT_SET,
                              )

    # Duration (in seconds) of each segment. Actual segments will be rounded to
    # the nearest multiple of the source segment duration.
    segment_duration_seconds: int = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # An optional custom string that is prepended to the name of each segment. If
    # not specified, it defaults to the ChannelId.
    segment_prefix: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A StreamSelection configuration.
    stream_selection: "StreamSelection" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class CreateChannelRequest(ShapeBase):
    """
    A new Channel configuration.
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
                "description",
                "Description",
                TypeInfo(str),
            ),
        ]

    # The ID of the Channel. The ID must be unique within the region and it
    # cannot be changed after a Channel is created.
    id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A short text description of the Channel.
    description: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class CreateChannelResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "arn",
                "Arn",
                TypeInfo(str),
            ),
            (
                "description",
                "Description",
                TypeInfo(str),
            ),
            (
                "hls_ingest",
                "HlsIngest",
                TypeInfo(HlsIngest),
            ),
            (
                "id",
                "Id",
                TypeInfo(str),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The Amazon Resource Name (ARN) assigned to the Channel.
    arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A short text description of the Channel.
    description: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # An HTTP Live Streaming (HLS) ingest resource configuration.
    hls_ingest: "HlsIngest" = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The ID of the Channel.
    id: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class CreateOriginEndpointRequest(ShapeBase):
    """
    Configuration parameters used to create a new OriginEndpoint.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "channel_id",
                "ChannelId",
                TypeInfo(str),
            ),
            (
                "id",
                "Id",
                TypeInfo(str),
            ),
            (
                "cmaf_package",
                "CmafPackage",
                TypeInfo(CmafPackageCreateOrUpdateParameters),
            ),
            (
                "dash_package",
                "DashPackage",
                TypeInfo(DashPackage),
            ),
            (
                "description",
                "Description",
                TypeInfo(str),
            ),
            (
                "hls_package",
                "HlsPackage",
                TypeInfo(HlsPackage),
            ),
            (
                "manifest_name",
                "ManifestName",
                TypeInfo(str),
            ),
            (
                "mss_package",
                "MssPackage",
                TypeInfo(MssPackage),
            ),
            (
                "startover_window_seconds",
                "StartoverWindowSeconds",
                TypeInfo(int),
            ),
            (
                "time_delay_seconds",
                "TimeDelaySeconds",
                TypeInfo(int),
            ),
            (
                "whitelist",
                "Whitelist",
                TypeInfo(typing.List[str]),
            ),
        ]

    # The ID of the Channel that the OriginEndpoint will be associated with. This
    # cannot be changed after the OriginEndpoint is created.
    channel_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The ID of the OriginEndpoint. The ID must be unique within the region and
    # it cannot be changed after the OriginEndpoint is created.
    id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A Common Media Application Format (CMAF) packaging configuration.
    cmaf_package: "CmafPackageCreateOrUpdateParameters" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A Dynamic Adaptive Streaming over HTTP (DASH) packaging configuration.
    dash_package: "DashPackage" = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A short text description of the OriginEndpoint.
    description: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # An HTTP Live Streaming (HLS) packaging configuration.
    hls_package: "HlsPackage" = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A short string that will be used as the filename of the OriginEndpoint URL
    # (defaults to "index").
    manifest_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A Microsoft Smooth Streaming (MSS) packaging configuration.
    mss_package: "MssPackage" = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Maximum duration (seconds) of content to retain for startover playback. If
    # not specified, startover playback will be disabled for the OriginEndpoint.
    startover_window_seconds: int = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Amount of delay (seconds) to enforce on the playback of live content. If
    # not specified, there will be no time delay in effect for the
    # OriginEndpoint.
    time_delay_seconds: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A list of source IP CIDR blocks that will be allowed to access the
    # OriginEndpoint.
    whitelist: typing.List[str] = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class CreateOriginEndpointResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "arn",
                "Arn",
                TypeInfo(str),
            ),
            (
                "channel_id",
                "ChannelId",
                TypeInfo(str),
            ),
            (
                "cmaf_package",
                "CmafPackage",
                TypeInfo(CmafPackage),
            ),
            (
                "dash_package",
                "DashPackage",
                TypeInfo(DashPackage),
            ),
            (
                "description",
                "Description",
                TypeInfo(str),
            ),
            (
                "hls_package",
                "HlsPackage",
                TypeInfo(HlsPackage),
            ),
            (
                "id",
                "Id",
                TypeInfo(str),
            ),
            (
                "manifest_name",
                "ManifestName",
                TypeInfo(str),
            ),
            (
                "mss_package",
                "MssPackage",
                TypeInfo(MssPackage),
            ),
            (
                "startover_window_seconds",
                "StartoverWindowSeconds",
                TypeInfo(int),
            ),
            (
                "time_delay_seconds",
                "TimeDelaySeconds",
                TypeInfo(int),
            ),
            (
                "url",
                "Url",
                TypeInfo(str),
            ),
            (
                "whitelist",
                "Whitelist",
                TypeInfo(typing.List[str]),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The Amazon Resource Name (ARN) assigned to the OriginEndpoint.
    arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The ID of the Channel the OriginEndpoint is associated with.
    channel_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A Common Media Application Format (CMAF) packaging configuration.
    cmaf_package: "CmafPackage" = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A Dynamic Adaptive Streaming over HTTP (DASH) packaging configuration.
    dash_package: "DashPackage" = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A short text description of the OriginEndpoint.
    description: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # An HTTP Live Streaming (HLS) packaging configuration.
    hls_package: "HlsPackage" = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The ID of the OriginEndpoint.
    id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A short string appended to the end of the OriginEndpoint URL.
    manifest_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A Microsoft Smooth Streaming (MSS) packaging configuration.
    mss_package: "MssPackage" = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Maximum duration (seconds) of content to retain for startover playback. If
    # not specified, startover playback will be disabled for the OriginEndpoint.
    startover_window_seconds: int = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Amount of delay (seconds) to enforce on the playback of live content. If
    # not specified, there will be no time delay in effect for the
    # OriginEndpoint.
    time_delay_seconds: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The URL of the packaged OriginEndpoint for consumption.
    url: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A list of source IP CIDR blocks that will be allowed to access the
    # OriginEndpoint.
    whitelist: typing.List[str] = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DashEncryption(ShapeBase):
    """
    A Dynamic Adaptive Streaming over HTTP (DASH) encryption configuration.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "speke_key_provider",
                "SpekeKeyProvider",
                TypeInfo(SpekeKeyProvider),
            ),
            (
                "key_rotation_interval_seconds",
                "KeyRotationIntervalSeconds",
                TypeInfo(int),
            ),
        ]

    # A configuration for accessing an external Secure Packager and Encoder Key
    # Exchange (SPEKE) service that will provide encryption keys.
    speke_key_provider: "SpekeKeyProvider" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Time (in seconds) between each encryption key rotation.
    key_rotation_interval_seconds: int = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class DashPackage(ShapeBase):
    """
    A Dynamic Adaptive Streaming over HTTP (DASH) packaging configuration.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "encryption",
                "Encryption",
                TypeInfo(DashEncryption),
            ),
            (
                "manifest_window_seconds",
                "ManifestWindowSeconds",
                TypeInfo(int),
            ),
            (
                "min_buffer_time_seconds",
                "MinBufferTimeSeconds",
                TypeInfo(int),
            ),
            (
                "min_update_period_seconds",
                "MinUpdatePeriodSeconds",
                TypeInfo(int),
            ),
            (
                "period_triggers",
                "PeriodTriggers",
                TypeInfo(
                    typing.List[typing.Union[str, __PeriodTriggersElement]]
                ),
            ),
            (
                "profile",
                "Profile",
                TypeInfo(typing.Union[str, Profile]),
            ),
            (
                "segment_duration_seconds",
                "SegmentDurationSeconds",
                TypeInfo(int),
            ),
            (
                "stream_selection",
                "StreamSelection",
                TypeInfo(StreamSelection),
            ),
            (
                "suggested_presentation_delay_seconds",
                "SuggestedPresentationDelaySeconds",
                TypeInfo(int),
            ),
        ]

    # A Dynamic Adaptive Streaming over HTTP (DASH) encryption configuration.
    encryption: "DashEncryption" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Time window (in seconds) contained in each manifest.
    manifest_window_seconds: int = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Minimum duration (in seconds) that a player will buffer media before
    # starting the presentation.
    min_buffer_time_seconds: int = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Minimum duration (in seconds) between potential changes to the Dynamic
    # Adaptive Streaming over HTTP (DASH) Media Presentation Description (MPD).
    min_update_period_seconds: int = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A list of triggers that controls when the outgoing Dynamic Adaptive
    # Streaming over HTTP (DASH) Media Presentation Description (MPD) will be
    # partitioned into multiple periods. If empty, the content will not be
    # partitioned into more than one period. If the list contains "ADS", new
    # periods will be created where the Channel source contains SCTE-35 ad
    # markers.
    period_triggers: typing.List[typing.Union[str, "__PeriodTriggersElement"]
                                ] = dataclasses.field(
                                    default=ShapeBase.NOT_SET,
                                )

    # The Dynamic Adaptive Streaming over HTTP (DASH) profile type. When set to
    # "HBBTV_1_5", HbbTV 1.5 compliant output is enabled.
    profile: typing.Union[str, "Profile"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Duration (in seconds) of each segment. Actual segments will be rounded to
    # the nearest multiple of the source segment duration.
    segment_duration_seconds: int = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A StreamSelection configuration.
    stream_selection: "StreamSelection" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Duration (in seconds) to delay live content before presentation.
    suggested_presentation_delay_seconds: int = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class DeleteChannelRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "id",
                "Id",
                TypeInfo(str),
            ),
        ]

    # The ID of the Channel to delete.
    id: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DeleteChannelResponse(OutputShapeBase):
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
class DeleteOriginEndpointRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "id",
                "Id",
                TypeInfo(str),
            ),
        ]

    # The ID of the OriginEndpoint to delete.
    id: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DeleteOriginEndpointResponse(OutputShapeBase):
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
class DescribeChannelRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "id",
                "Id",
                TypeInfo(str),
            ),
        ]

    # The ID of a Channel.
    id: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DescribeChannelResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "arn",
                "Arn",
                TypeInfo(str),
            ),
            (
                "description",
                "Description",
                TypeInfo(str),
            ),
            (
                "hls_ingest",
                "HlsIngest",
                TypeInfo(HlsIngest),
            ),
            (
                "id",
                "Id",
                TypeInfo(str),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The Amazon Resource Name (ARN) assigned to the Channel.
    arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A short text description of the Channel.
    description: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # An HTTP Live Streaming (HLS) ingest resource configuration.
    hls_ingest: "HlsIngest" = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The ID of the Channel.
    id: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DescribeOriginEndpointRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "id",
                "Id",
                TypeInfo(str),
            ),
        ]

    # The ID of the OriginEndpoint.
    id: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DescribeOriginEndpointResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "arn",
                "Arn",
                TypeInfo(str),
            ),
            (
                "channel_id",
                "ChannelId",
                TypeInfo(str),
            ),
            (
                "cmaf_package",
                "CmafPackage",
                TypeInfo(CmafPackage),
            ),
            (
                "dash_package",
                "DashPackage",
                TypeInfo(DashPackage),
            ),
            (
                "description",
                "Description",
                TypeInfo(str),
            ),
            (
                "hls_package",
                "HlsPackage",
                TypeInfo(HlsPackage),
            ),
            (
                "id",
                "Id",
                TypeInfo(str),
            ),
            (
                "manifest_name",
                "ManifestName",
                TypeInfo(str),
            ),
            (
                "mss_package",
                "MssPackage",
                TypeInfo(MssPackage),
            ),
            (
                "startover_window_seconds",
                "StartoverWindowSeconds",
                TypeInfo(int),
            ),
            (
                "time_delay_seconds",
                "TimeDelaySeconds",
                TypeInfo(int),
            ),
            (
                "url",
                "Url",
                TypeInfo(str),
            ),
            (
                "whitelist",
                "Whitelist",
                TypeInfo(typing.List[str]),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The Amazon Resource Name (ARN) assigned to the OriginEndpoint.
    arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The ID of the Channel the OriginEndpoint is associated with.
    channel_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A Common Media Application Format (CMAF) packaging configuration.
    cmaf_package: "CmafPackage" = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A Dynamic Adaptive Streaming over HTTP (DASH) packaging configuration.
    dash_package: "DashPackage" = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A short text description of the OriginEndpoint.
    description: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # An HTTP Live Streaming (HLS) packaging configuration.
    hls_package: "HlsPackage" = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The ID of the OriginEndpoint.
    id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A short string appended to the end of the OriginEndpoint URL.
    manifest_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A Microsoft Smooth Streaming (MSS) packaging configuration.
    mss_package: "MssPackage" = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Maximum duration (seconds) of content to retain for startover playback. If
    # not specified, startover playback will be disabled for the OriginEndpoint.
    startover_window_seconds: int = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Amount of delay (seconds) to enforce on the playback of live content. If
    # not specified, there will be no time delay in effect for the
    # OriginEndpoint.
    time_delay_seconds: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The URL of the packaged OriginEndpoint for consumption.
    url: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A list of source IP CIDR blocks that will be allowed to access the
    # OriginEndpoint.
    whitelist: typing.List[str] = dataclasses.field(default=ShapeBase.NOT_SET, )


class EncryptionMethod(str):
    AES_128 = "AES_128"
    SAMPLE_AES = "SAMPLE_AES"


@dataclasses.dataclass
class ForbiddenException(ShapeBase):
    """
    The client is not authorized to access the requested resource.
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
class HlsEncryption(ShapeBase):
    """
    An HTTP Live Streaming (HLS) encryption configuration.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "speke_key_provider",
                "SpekeKeyProvider",
                TypeInfo(SpekeKeyProvider),
            ),
            (
                "constant_initialization_vector",
                "ConstantInitializationVector",
                TypeInfo(str),
            ),
            (
                "encryption_method",
                "EncryptionMethod",
                TypeInfo(typing.Union[str, EncryptionMethod]),
            ),
            (
                "key_rotation_interval_seconds",
                "KeyRotationIntervalSeconds",
                TypeInfo(int),
            ),
            (
                "repeat_ext_x_key",
                "RepeatExtXKey",
                TypeInfo(bool),
            ),
        ]

    # A configuration for accessing an external Secure Packager and Encoder Key
    # Exchange (SPEKE) service that will provide encryption keys.
    speke_key_provider: "SpekeKeyProvider" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A constant initialization vector for encryption (optional). When not
    # specified the initialization vector will be periodically rotated.
    constant_initialization_vector: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The encryption method to use.
    encryption_method: typing.Union[str, "EncryptionMethod"
                                   ] = dataclasses.field(
                                       default=ShapeBase.NOT_SET,
                                   )

    # Interval (in seconds) between each encryption key rotation.
    key_rotation_interval_seconds: int = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # When enabled, the EXT-X-KEY tag will be repeated in output manifests.
    repeat_ext_x_key: bool = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class HlsIngest(ShapeBase):
    """
    An HTTP Live Streaming (HLS) ingest resource configuration.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "ingest_endpoints",
                "IngestEndpoints",
                TypeInfo(typing.List[IngestEndpoint]),
            ),
        ]

    # A list of endpoints to which the source stream should be sent.
    ingest_endpoints: typing.List["IngestEndpoint"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class HlsManifest(ShapeBase):
    """
    A HTTP Live Streaming (HLS) manifest configuration.
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
                "ad_markers",
                "AdMarkers",
                TypeInfo(typing.Union[str, AdMarkers]),
            ),
            (
                "include_iframe_only_stream",
                "IncludeIframeOnlyStream",
                TypeInfo(bool),
            ),
            (
                "manifest_name",
                "ManifestName",
                TypeInfo(str),
            ),
            (
                "playlist_type",
                "PlaylistType",
                TypeInfo(typing.Union[str, PlaylistType]),
            ),
            (
                "playlist_window_seconds",
                "PlaylistWindowSeconds",
                TypeInfo(int),
            ),
            (
                "program_date_time_interval_seconds",
                "ProgramDateTimeIntervalSeconds",
                TypeInfo(int),
            ),
            (
                "url",
                "Url",
                TypeInfo(str),
            ),
        ]

    # The ID of the manifest. The ID must be unique within the OriginEndpoint and
    # it cannot be changed after it is created.
    id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # This setting controls how ad markers are included in the packaged
    # OriginEndpoint. "NONE" will omit all SCTE-35 ad markers from the output.
    # "PASSTHROUGH" causes the manifest to contain a copy of the SCTE-35 ad
    # markers (comments) taken directly from the input HTTP Live Streaming (HLS)
    # manifest. "SCTE35_ENHANCED" generates ad markers and blackout tags based on
    # SCTE-35 messages in the input source.
    ad_markers: typing.Union[str, "AdMarkers"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # When enabled, an I-Frame only stream will be included in the output.
    include_iframe_only_stream: bool = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # An optional short string appended to the end of the OriginEndpoint URL. If
    # not specified, defaults to the manifestName for the OriginEndpoint.
    manifest_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The HTTP Live Streaming (HLS) playlist type. When either "EVENT" or "VOD"
    # is specified, a corresponding EXT-X-PLAYLIST-TYPE entry will be included in
    # the media playlist.
    playlist_type: typing.Union[str, "PlaylistType"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Time window (in seconds) contained in each parent manifest.
    playlist_window_seconds: int = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The interval (in seconds) between each EXT-X-PROGRAM-DATE-TIME tag inserted
    # into manifests. Additionally, when an interval is specified ID3Timed
    # Metadata messages will be generated every 5 seconds using the ingest time
    # of the content. If the interval is not specified, or set to 0, then no EXT-
    # X-PROGRAM-DATE-TIME tags will be inserted into manifests and no ID3Timed
    # Metadata messages will be generated. Note that irrespective of this
    # parameter, if any ID3 Timed Metadata is found in HTTP Live Streaming (HLS)
    # input, it will be passed through to HLS output.
    program_date_time_interval_seconds: int = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The URL of the packaged OriginEndpoint for consumption.
    url: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class HlsManifestCreateOrUpdateParameters(ShapeBase):
    """
    A HTTP Live Streaming (HLS) manifest configuration.
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
                "ad_markers",
                "AdMarkers",
                TypeInfo(typing.Union[str, AdMarkers]),
            ),
            (
                "include_iframe_only_stream",
                "IncludeIframeOnlyStream",
                TypeInfo(bool),
            ),
            (
                "manifest_name",
                "ManifestName",
                TypeInfo(str),
            ),
            (
                "playlist_type",
                "PlaylistType",
                TypeInfo(typing.Union[str, PlaylistType]),
            ),
            (
                "playlist_window_seconds",
                "PlaylistWindowSeconds",
                TypeInfo(int),
            ),
            (
                "program_date_time_interval_seconds",
                "ProgramDateTimeIntervalSeconds",
                TypeInfo(int),
            ),
        ]

    # The ID of the manifest. The ID must be unique within the OriginEndpoint and
    # it cannot be changed after it is created.
    id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # This setting controls how ad markers are included in the packaged
    # OriginEndpoint. "NONE" will omit all SCTE-35 ad markers from the output.
    # "PASSTHROUGH" causes the manifest to contain a copy of the SCTE-35 ad
    # markers (comments) taken directly from the input HTTP Live Streaming (HLS)
    # manifest. "SCTE35_ENHANCED" generates ad markers and blackout tags based on
    # SCTE-35 messages in the input source.
    ad_markers: typing.Union[str, "AdMarkers"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # When enabled, an I-Frame only stream will be included in the output.
    include_iframe_only_stream: bool = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # An optional short string appended to the end of the OriginEndpoint URL. If
    # not specified, defaults to the manifestName for the OriginEndpoint.
    manifest_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The HTTP Live Streaming (HLS) playlist type. When either "EVENT" or "VOD"
    # is specified, a corresponding EXT-X-PLAYLIST-TYPE entry will be included in
    # the media playlist.
    playlist_type: typing.Union[str, "PlaylistType"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Time window (in seconds) contained in each parent manifest.
    playlist_window_seconds: int = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The interval (in seconds) between each EXT-X-PROGRAM-DATE-TIME tag inserted
    # into manifests. Additionally, when an interval is specified ID3Timed
    # Metadata messages will be generated every 5 seconds using the ingest time
    # of the content. If the interval is not specified, or set to 0, then no EXT-
    # X-PROGRAM-DATE-TIME tags will be inserted into manifests and no ID3Timed
    # Metadata messages will be generated. Note that irrespective of this
    # parameter, if any ID3 Timed Metadata is found in HTTP Live Streaming (HLS)
    # input, it will be passed through to HLS output.
    program_date_time_interval_seconds: int = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class HlsPackage(ShapeBase):
    """
    An HTTP Live Streaming (HLS) packaging configuration.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "ad_markers",
                "AdMarkers",
                TypeInfo(typing.Union[str, AdMarkers]),
            ),
            (
                "encryption",
                "Encryption",
                TypeInfo(HlsEncryption),
            ),
            (
                "include_iframe_only_stream",
                "IncludeIframeOnlyStream",
                TypeInfo(bool),
            ),
            (
                "playlist_type",
                "PlaylistType",
                TypeInfo(typing.Union[str, PlaylistType]),
            ),
            (
                "playlist_window_seconds",
                "PlaylistWindowSeconds",
                TypeInfo(int),
            ),
            (
                "program_date_time_interval_seconds",
                "ProgramDateTimeIntervalSeconds",
                TypeInfo(int),
            ),
            (
                "segment_duration_seconds",
                "SegmentDurationSeconds",
                TypeInfo(int),
            ),
            (
                "stream_selection",
                "StreamSelection",
                TypeInfo(StreamSelection),
            ),
            (
                "use_audio_rendition_group",
                "UseAudioRenditionGroup",
                TypeInfo(bool),
            ),
        ]

    # This setting controls how ad markers are included in the packaged
    # OriginEndpoint. "NONE" will omit all SCTE-35 ad markers from the output.
    # "PASSTHROUGH" causes the manifest to contain a copy of the SCTE-35 ad
    # markers (comments) taken directly from the input HTTP Live Streaming (HLS)
    # manifest. "SCTE35_ENHANCED" generates ad markers and blackout tags based on
    # SCTE-35 messages in the input source.
    ad_markers: typing.Union[str, "AdMarkers"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # An HTTP Live Streaming (HLS) encryption configuration.
    encryption: "HlsEncryption" = dataclasses.field(default=ShapeBase.NOT_SET, )

    # When enabled, an I-Frame only stream will be included in the output.
    include_iframe_only_stream: bool = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The HTTP Live Streaming (HLS) playlist type. When either "EVENT" or "VOD"
    # is specified, a corresponding EXT-X-PLAYLIST-TYPE entry will be included in
    # the media playlist.
    playlist_type: typing.Union[str, "PlaylistType"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Time window (in seconds) contained in each parent manifest.
    playlist_window_seconds: int = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The interval (in seconds) between each EXT-X-PROGRAM-DATE-TIME tag inserted
    # into manifests. Additionally, when an interval is specified ID3Timed
    # Metadata messages will be generated every 5 seconds using the ingest time
    # of the content. If the interval is not specified, or set to 0, then no EXT-
    # X-PROGRAM-DATE-TIME tags will be inserted into manifests and no ID3Timed
    # Metadata messages will be generated. Note that irrespective of this
    # parameter, if any ID3 Timed Metadata is found in HTTP Live Streaming (HLS)
    # input, it will be passed through to HLS output.
    program_date_time_interval_seconds: int = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Duration (in seconds) of each fragment. Actual fragments will be rounded to
    # the nearest multiple of the source fragment duration.
    segment_duration_seconds: int = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A StreamSelection configuration.
    stream_selection: "StreamSelection" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # When enabled, audio streams will be placed in rendition groups in the
    # output.
    use_audio_rendition_group: bool = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class IngestEndpoint(ShapeBase):
    """
    An endpoint for ingesting source content for a Channel.
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
                "password",
                "Password",
                TypeInfo(str),
            ),
            (
                "url",
                "Url",
                TypeInfo(str),
            ),
            (
                "username",
                "Username",
                TypeInfo(str),
            ),
        ]

    # The system generated unique identifier for the IngestEndpoint
    id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The system generated password for ingest authentication.
    password: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The ingest URL to which the source stream should be sent.
    url: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The system generated username for ingest authentication.
    username: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class InternalServerErrorException(ShapeBase):
    """
    An unexpected error occurred.
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
class ListChannelsRequest(ShapeBase):
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

    # Upper bound on number of records to return.
    max_results: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A token used to resume pagination from the end of a previous request.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ListChannelsResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "channels",
                "Channels",
                TypeInfo(typing.List[Channel]),
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

    # A list of Channel records.
    channels: typing.List["Channel"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A token that can be used to resume pagination from the end of the
    # collection.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    def paginate(self,
                ) -> typing.Generator["ListChannelsResponse", None, None]:
        yield from super()._paginate()


@dataclasses.dataclass
class ListOriginEndpointsRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "channel_id",
                "ChannelId",
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
        ]

    # When specified, the request will return only OriginEndpoints associated
    # with the given Channel ID.
    channel_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The upper bound on the number of records to return.
    max_results: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A token used to resume pagination from the end of a previous request.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ListOriginEndpointsResponse(OutputShapeBase):
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
                "origin_endpoints",
                "OriginEndpoints",
                TypeInfo(typing.List[OriginEndpoint]),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A token that can be used to resume pagination from the end of the
    # collection.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A list of OriginEndpoint records.
    origin_endpoints: typing.List["OriginEndpoint"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    def paginate(
        self,
    ) -> typing.Generator["ListOriginEndpointsResponse", None, None]:
        yield from super()._paginate()


@dataclasses.dataclass
class MssEncryption(ShapeBase):
    """
    A Microsoft Smooth Streaming (MSS) encryption configuration.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "speke_key_provider",
                "SpekeKeyProvider",
                TypeInfo(SpekeKeyProvider),
            ),
        ]

    # A configuration for accessing an external Secure Packager and Encoder Key
    # Exchange (SPEKE) service that will provide encryption keys.
    speke_key_provider: "SpekeKeyProvider" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class MssPackage(ShapeBase):
    """
    A Microsoft Smooth Streaming (MSS) packaging configuration.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "encryption",
                "Encryption",
                TypeInfo(MssEncryption),
            ),
            (
                "manifest_window_seconds",
                "ManifestWindowSeconds",
                TypeInfo(int),
            ),
            (
                "segment_duration_seconds",
                "SegmentDurationSeconds",
                TypeInfo(int),
            ),
            (
                "stream_selection",
                "StreamSelection",
                TypeInfo(StreamSelection),
            ),
        ]

    # A Microsoft Smooth Streaming (MSS) encryption configuration.
    encryption: "MssEncryption" = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The time window (in seconds) contained in each manifest.
    manifest_window_seconds: int = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The duration (in seconds) of each segment.
    segment_duration_seconds: int = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A StreamSelection configuration.
    stream_selection: "StreamSelection" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class NotFoundException(ShapeBase):
    """
    The requested resource does not exist.
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
class OriginEndpoint(ShapeBase):
    """
    An OriginEndpoint resource configuration.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "arn",
                "Arn",
                TypeInfo(str),
            ),
            (
                "channel_id",
                "ChannelId",
                TypeInfo(str),
            ),
            (
                "cmaf_package",
                "CmafPackage",
                TypeInfo(CmafPackage),
            ),
            (
                "dash_package",
                "DashPackage",
                TypeInfo(DashPackage),
            ),
            (
                "description",
                "Description",
                TypeInfo(str),
            ),
            (
                "hls_package",
                "HlsPackage",
                TypeInfo(HlsPackage),
            ),
            (
                "id",
                "Id",
                TypeInfo(str),
            ),
            (
                "manifest_name",
                "ManifestName",
                TypeInfo(str),
            ),
            (
                "mss_package",
                "MssPackage",
                TypeInfo(MssPackage),
            ),
            (
                "startover_window_seconds",
                "StartoverWindowSeconds",
                TypeInfo(int),
            ),
            (
                "time_delay_seconds",
                "TimeDelaySeconds",
                TypeInfo(int),
            ),
            (
                "url",
                "Url",
                TypeInfo(str),
            ),
            (
                "whitelist",
                "Whitelist",
                TypeInfo(typing.List[str]),
            ),
        ]

    # The Amazon Resource Name (ARN) assigned to the OriginEndpoint.
    arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The ID of the Channel the OriginEndpoint is associated with.
    channel_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A Common Media Application Format (CMAF) packaging configuration.
    cmaf_package: "CmafPackage" = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A Dynamic Adaptive Streaming over HTTP (DASH) packaging configuration.
    dash_package: "DashPackage" = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A short text description of the OriginEndpoint.
    description: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # An HTTP Live Streaming (HLS) packaging configuration.
    hls_package: "HlsPackage" = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The ID of the OriginEndpoint.
    id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A short string appended to the end of the OriginEndpoint URL.
    manifest_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A Microsoft Smooth Streaming (MSS) packaging configuration.
    mss_package: "MssPackage" = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Maximum duration (seconds) of content to retain for startover playback. If
    # not specified, startover playback will be disabled for the OriginEndpoint.
    startover_window_seconds: int = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Amount of delay (seconds) to enforce on the playback of live content. If
    # not specified, there will be no time delay in effect for the
    # OriginEndpoint.
    time_delay_seconds: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The URL of the packaged OriginEndpoint for consumption.
    url: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A list of source IP CIDR blocks that will be allowed to access the
    # OriginEndpoint.
    whitelist: typing.List[str] = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class OriginEndpointCreateParameters(ShapeBase):
    """
    Configuration parameters for a new OriginEndpoint.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "channel_id",
                "ChannelId",
                TypeInfo(str),
            ),
            (
                "id",
                "Id",
                TypeInfo(str),
            ),
            (
                "cmaf_package",
                "CmafPackage",
                TypeInfo(CmafPackageCreateOrUpdateParameters),
            ),
            (
                "dash_package",
                "DashPackage",
                TypeInfo(DashPackage),
            ),
            (
                "description",
                "Description",
                TypeInfo(str),
            ),
            (
                "hls_package",
                "HlsPackage",
                TypeInfo(HlsPackage),
            ),
            (
                "manifest_name",
                "ManifestName",
                TypeInfo(str),
            ),
            (
                "mss_package",
                "MssPackage",
                TypeInfo(MssPackage),
            ),
            (
                "startover_window_seconds",
                "StartoverWindowSeconds",
                TypeInfo(int),
            ),
            (
                "time_delay_seconds",
                "TimeDelaySeconds",
                TypeInfo(int),
            ),
            (
                "whitelist",
                "Whitelist",
                TypeInfo(typing.List[str]),
            ),
        ]

    # The ID of the Channel that the OriginEndpoint will be associated with. This
    # cannot be changed after the OriginEndpoint is created.
    channel_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The ID of the OriginEndpoint. The ID must be unique within the region and
    # it cannot be changed after the OriginEndpoint is created.
    id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A Common Media Application Format (CMAF) packaging configuration.
    cmaf_package: "CmafPackageCreateOrUpdateParameters" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A Dynamic Adaptive Streaming over HTTP (DASH) packaging configuration.
    dash_package: "DashPackage" = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A short text description of the OriginEndpoint.
    description: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # An HTTP Live Streaming (HLS) packaging configuration.
    hls_package: "HlsPackage" = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A short string that will be used as the filename of the OriginEndpoint URL
    # (defaults to "index").
    manifest_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A Microsoft Smooth Streaming (MSS) packaging configuration.
    mss_package: "MssPackage" = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Maximum duration (seconds) of content to retain for startover playback. If
    # not specified, startover playback will be disabled for the OriginEndpoint.
    startover_window_seconds: int = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Amount of delay (seconds) to enforce on the playback of live content. If
    # not specified, there will be no time delay in effect for the
    # OriginEndpoint.
    time_delay_seconds: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A list of source IP CIDR blocks that will be allowed to access the
    # OriginEndpoint.
    whitelist: typing.List[str] = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class OriginEndpointList(ShapeBase):
    """
    A collection of OriginEndpoint records.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "next_token",
                "NextToken",
                TypeInfo(str),
            ),
            (
                "origin_endpoints",
                "OriginEndpoints",
                TypeInfo(typing.List[OriginEndpoint]),
            ),
        ]

    # A token that can be used to resume pagination from the end of the
    # collection.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A list of OriginEndpoint records.
    origin_endpoints: typing.List["OriginEndpoint"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class OriginEndpointUpdateParameters(ShapeBase):
    """
    Configuration parameters for updating an existing OriginEndpoint.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "cmaf_package",
                "CmafPackage",
                TypeInfo(CmafPackageCreateOrUpdateParameters),
            ),
            (
                "dash_package",
                "DashPackage",
                TypeInfo(DashPackage),
            ),
            (
                "description",
                "Description",
                TypeInfo(str),
            ),
            (
                "hls_package",
                "HlsPackage",
                TypeInfo(HlsPackage),
            ),
            (
                "manifest_name",
                "ManifestName",
                TypeInfo(str),
            ),
            (
                "mss_package",
                "MssPackage",
                TypeInfo(MssPackage),
            ),
            (
                "startover_window_seconds",
                "StartoverWindowSeconds",
                TypeInfo(int),
            ),
            (
                "time_delay_seconds",
                "TimeDelaySeconds",
                TypeInfo(int),
            ),
            (
                "whitelist",
                "Whitelist",
                TypeInfo(typing.List[str]),
            ),
        ]

    # A Common Media Application Format (CMAF) packaging configuration.
    cmaf_package: "CmafPackageCreateOrUpdateParameters" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A Dynamic Adaptive Streaming over HTTP (DASH) packaging configuration.
    dash_package: "DashPackage" = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A short text description of the OriginEndpoint.
    description: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # An HTTP Live Streaming (HLS) packaging configuration.
    hls_package: "HlsPackage" = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A short string that will be appended to the end of the Endpoint URL.
    manifest_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A Microsoft Smooth Streaming (MSS) packaging configuration.
    mss_package: "MssPackage" = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Maximum duration (in seconds) of content to retain for startover playback.
    # If not specified, startover playback will be disabled for the
    # OriginEndpoint.
    startover_window_seconds: int = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Amount of delay (in seconds) to enforce on the playback of live content. If
    # not specified, there will be no time delay in effect for the
    # OriginEndpoint.
    time_delay_seconds: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A list of source IP CIDR blocks that will be allowed to access the
    # OriginEndpoint.
    whitelist: typing.List[str] = dataclasses.field(default=ShapeBase.NOT_SET, )


class PlaylistType(str):
    NONE = "NONE"
    EVENT = "EVENT"
    VOD = "VOD"


class Profile(str):
    NONE = "NONE"
    HBBTV_1_5 = "HBBTV_1_5"


@dataclasses.dataclass
class RotateChannelCredentialsRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "id",
                "Id",
                TypeInfo(str),
            ),
        ]

    # The ID of the channel to update.
    id: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class RotateChannelCredentialsResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "arn",
                "Arn",
                TypeInfo(str),
            ),
            (
                "description",
                "Description",
                TypeInfo(str),
            ),
            (
                "hls_ingest",
                "HlsIngest",
                TypeInfo(HlsIngest),
            ),
            (
                "id",
                "Id",
                TypeInfo(str),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The Amazon Resource Name (ARN) assigned to the Channel.
    arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A short text description of the Channel.
    description: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # An HTTP Live Streaming (HLS) ingest resource configuration.
    hls_ingest: "HlsIngest" = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The ID of the Channel.
    id: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class RotateIngestEndpointCredentialsRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "id",
                "Id",
                TypeInfo(str),
            ),
            (
                "ingest_endpoint_id",
                "IngestEndpointId",
                TypeInfo(str),
            ),
        ]

    # The ID of the channel the IngestEndpoint is on.
    id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The id of the IngestEndpoint whose credentials should be rotated
    ingest_endpoint_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class RotateIngestEndpointCredentialsResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "arn",
                "Arn",
                TypeInfo(str),
            ),
            (
                "description",
                "Description",
                TypeInfo(str),
            ),
            (
                "hls_ingest",
                "HlsIngest",
                TypeInfo(HlsIngest),
            ),
            (
                "id",
                "Id",
                TypeInfo(str),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The Amazon Resource Name (ARN) assigned to the Channel.
    arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A short text description of the Channel.
    description: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # An HTTP Live Streaming (HLS) ingest resource configuration.
    hls_ingest: "HlsIngest" = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The ID of the Channel.
    id: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ServiceUnavailableException(ShapeBase):
    """
    An unexpected error occurred.
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
class SpekeKeyProvider(ShapeBase):
    """
    A configuration for accessing an external Secure Packager and Encoder Key
    Exchange (SPEKE) service that will provide encryption keys.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "resource_id",
                "ResourceId",
                TypeInfo(str),
            ),
            (
                "role_arn",
                "RoleArn",
                TypeInfo(str),
            ),
            (
                "system_ids",
                "SystemIds",
                TypeInfo(typing.List[str]),
            ),
            (
                "url",
                "Url",
                TypeInfo(str),
            ),
        ]

    # The resource ID to include in key requests.
    resource_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # An Amazon Resource Name (ARN) of an IAM role that AWS Elemental
    # MediaPackage will assume when accessing the key provider service.
    role_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The system IDs to include in key requests.
    system_ids: typing.List[str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The URL of the external key provider service.
    url: str = dataclasses.field(default=ShapeBase.NOT_SET, )


class StreamOrder(str):
    ORIGINAL = "ORIGINAL"
    VIDEO_BITRATE_ASCENDING = "VIDEO_BITRATE_ASCENDING"
    VIDEO_BITRATE_DESCENDING = "VIDEO_BITRATE_DESCENDING"


@dataclasses.dataclass
class StreamSelection(ShapeBase):
    """
    A StreamSelection configuration.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "max_video_bits_per_second",
                "MaxVideoBitsPerSecond",
                TypeInfo(int),
            ),
            (
                "min_video_bits_per_second",
                "MinVideoBitsPerSecond",
                TypeInfo(int),
            ),
            (
                "stream_order",
                "StreamOrder",
                TypeInfo(typing.Union[str, StreamOrder]),
            ),
        ]

    # The maximum video bitrate (bps) to include in output.
    max_video_bits_per_second: int = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The minimum video bitrate (bps) to include in output.
    min_video_bits_per_second: int = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A directive that determines the order of streams in the output.
    stream_order: typing.Union[str, "StreamOrder"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class TooManyRequestsException(ShapeBase):
    """
    The client has exceeded their resource or throttling limits.
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
class UnprocessableEntityException(ShapeBase):
    """
    The parameters sent in the request are not valid.
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
class UpdateChannelRequest(ShapeBase):
    """
    Configuration parameters used to update the Channel.
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
                "description",
                "Description",
                TypeInfo(str),
            ),
        ]

    # The ID of the Channel to update.
    id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A short text description of the Channel.
    description: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class UpdateChannelResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "arn",
                "Arn",
                TypeInfo(str),
            ),
            (
                "description",
                "Description",
                TypeInfo(str),
            ),
            (
                "hls_ingest",
                "HlsIngest",
                TypeInfo(HlsIngest),
            ),
            (
                "id",
                "Id",
                TypeInfo(str),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The Amazon Resource Name (ARN) assigned to the Channel.
    arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A short text description of the Channel.
    description: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # An HTTP Live Streaming (HLS) ingest resource configuration.
    hls_ingest: "HlsIngest" = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The ID of the Channel.
    id: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class UpdateOriginEndpointRequest(ShapeBase):
    """
    Configuration parameters used to update an existing OriginEndpoint.
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
                "cmaf_package",
                "CmafPackage",
                TypeInfo(CmafPackageCreateOrUpdateParameters),
            ),
            (
                "dash_package",
                "DashPackage",
                TypeInfo(DashPackage),
            ),
            (
                "description",
                "Description",
                TypeInfo(str),
            ),
            (
                "hls_package",
                "HlsPackage",
                TypeInfo(HlsPackage),
            ),
            (
                "manifest_name",
                "ManifestName",
                TypeInfo(str),
            ),
            (
                "mss_package",
                "MssPackage",
                TypeInfo(MssPackage),
            ),
            (
                "startover_window_seconds",
                "StartoverWindowSeconds",
                TypeInfo(int),
            ),
            (
                "time_delay_seconds",
                "TimeDelaySeconds",
                TypeInfo(int),
            ),
            (
                "whitelist",
                "Whitelist",
                TypeInfo(typing.List[str]),
            ),
        ]

    # The ID of the OriginEndpoint to update.
    id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A Common Media Application Format (CMAF) packaging configuration.
    cmaf_package: "CmafPackageCreateOrUpdateParameters" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A Dynamic Adaptive Streaming over HTTP (DASH) packaging configuration.
    dash_package: "DashPackage" = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A short text description of the OriginEndpoint.
    description: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # An HTTP Live Streaming (HLS) packaging configuration.
    hls_package: "HlsPackage" = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A short string that will be appended to the end of the Endpoint URL.
    manifest_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A Microsoft Smooth Streaming (MSS) packaging configuration.
    mss_package: "MssPackage" = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Maximum duration (in seconds) of content to retain for startover playback.
    # If not specified, startover playback will be disabled for the
    # OriginEndpoint.
    startover_window_seconds: int = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Amount of delay (in seconds) to enforce on the playback of live content. If
    # not specified, there will be no time delay in effect for the
    # OriginEndpoint.
    time_delay_seconds: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A list of source IP CIDR blocks that will be allowed to access the
    # OriginEndpoint.
    whitelist: typing.List[str] = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class UpdateOriginEndpointResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "arn",
                "Arn",
                TypeInfo(str),
            ),
            (
                "channel_id",
                "ChannelId",
                TypeInfo(str),
            ),
            (
                "cmaf_package",
                "CmafPackage",
                TypeInfo(CmafPackage),
            ),
            (
                "dash_package",
                "DashPackage",
                TypeInfo(DashPackage),
            ),
            (
                "description",
                "Description",
                TypeInfo(str),
            ),
            (
                "hls_package",
                "HlsPackage",
                TypeInfo(HlsPackage),
            ),
            (
                "id",
                "Id",
                TypeInfo(str),
            ),
            (
                "manifest_name",
                "ManifestName",
                TypeInfo(str),
            ),
            (
                "mss_package",
                "MssPackage",
                TypeInfo(MssPackage),
            ),
            (
                "startover_window_seconds",
                "StartoverWindowSeconds",
                TypeInfo(int),
            ),
            (
                "time_delay_seconds",
                "TimeDelaySeconds",
                TypeInfo(int),
            ),
            (
                "url",
                "Url",
                TypeInfo(str),
            ),
            (
                "whitelist",
                "Whitelist",
                TypeInfo(typing.List[str]),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The Amazon Resource Name (ARN) assigned to the OriginEndpoint.
    arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The ID of the Channel the OriginEndpoint is associated with.
    channel_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A Common Media Application Format (CMAF) packaging configuration.
    cmaf_package: "CmafPackage" = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A Dynamic Adaptive Streaming over HTTP (DASH) packaging configuration.
    dash_package: "DashPackage" = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A short text description of the OriginEndpoint.
    description: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # An HTTP Live Streaming (HLS) packaging configuration.
    hls_package: "HlsPackage" = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The ID of the OriginEndpoint.
    id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A short string appended to the end of the OriginEndpoint URL.
    manifest_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A Microsoft Smooth Streaming (MSS) packaging configuration.
    mss_package: "MssPackage" = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Maximum duration (seconds) of content to retain for startover playback. If
    # not specified, startover playback will be disabled for the OriginEndpoint.
    startover_window_seconds: int = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Amount of delay (seconds) to enforce on the playback of live content. If
    # not specified, there will be no time delay in effect for the
    # OriginEndpoint.
    time_delay_seconds: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The URL of the packaged OriginEndpoint for consumption.
    url: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A list of source IP CIDR blocks that will be allowed to access the
    # OriginEndpoint.
    whitelist: typing.List[str] = dataclasses.field(default=ShapeBase.NOT_SET, )


class __PeriodTriggersElement(str):
    ADS = "ADS"
