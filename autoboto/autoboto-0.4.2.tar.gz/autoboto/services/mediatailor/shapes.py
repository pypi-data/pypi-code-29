import datetime
import typing
from autoboto import ShapeBase, OutputShapeBase, TypeInfo
import dataclasses


@dataclasses.dataclass
class CdnConfiguration(ShapeBase):
    """
    The configuration for using a content delivery network (CDN), like Amazon
    CloudFront, for content and ad segment management.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "ad_segment_url_prefix",
                "AdSegmentUrlPrefix",
                TypeInfo(str),
            ),
            (
                "content_segment_url_prefix",
                "ContentSegmentUrlPrefix",
                TypeInfo(str),
            ),
        ]

    # A non-default content delivery network (CDN) to serve ad segments. By
    # default, AWS Elemental MediaTailor uses Amazon CloudFront with default
    # cache settings as its CDN for ad segments. To set up an alternate CDN,
    # create a rule in your CDN for the following origin:
    # ads.mediatailor.<region>.amazonaws.com. Then specify the rule's name in
    # this AdSegmentUrlPrefix. When AWS Elemental MediaTailor serves a manifest,
    # it reports your CDN as the source for ad segments.
    ad_segment_url_prefix: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A content delivery network (CDN) to cache content segments, so that content
    # requests don’t always have to go to the origin server. First, create a rule
    # in your CDN for the content segment origin server. Then specify the rule's
    # name in this ContentSegmentUrlPrefix. When AWS Elemental MediaTailor serves
    # a manifest, it reports your CDN as the source for content segments.
    content_segment_url_prefix: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class HlsConfiguration(ShapeBase):
    """
    The configuration for HLS content.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "manifest_endpoint_prefix",
                "ManifestEndpointPrefix",
                TypeInfo(str),
            ),
        ]

    # The URL that is used to initiate a playback session for devices that
    # support Apple HLS. The session uses server-side reporting.
    manifest_endpoint_prefix: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class DeletePlaybackConfigurationRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "name",
                "Name",
                TypeInfo(str),
            ),
        ]

    # The identifier for the configuration.
    name: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DeletePlaybackConfigurationResponse(OutputShapeBase):
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
class Empty(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class GetPlaybackConfigurationRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "name",
                "Name",
                TypeInfo(str),
            ),
        ]

    # The identifier for the configuration.
    name: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class GetPlaybackConfigurationResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "ad_decision_server_url",
                "AdDecisionServerUrl",
                TypeInfo(str),
            ),
            (
                "cdn_configuration",
                "CdnConfiguration",
                TypeInfo(CdnConfiguration),
            ),
            (
                "hls_configuration",
                "HlsConfiguration",
                TypeInfo(HlsConfiguration),
            ),
            (
                "name",
                "Name",
                TypeInfo(str),
            ),
            (
                "playback_endpoint_prefix",
                "PlaybackEndpointPrefix",
                TypeInfo(str),
            ),
            (
                "session_initialization_endpoint_prefix",
                "SessionInitializationEndpointPrefix",
                TypeInfo(str),
            ),
            (
                "slate_ad_url",
                "SlateAdUrl",
                TypeInfo(str),
            ),
            (
                "video_content_source_url",
                "VideoContentSourceUrl",
                TypeInfo(str),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The URL for the ad decision server (ADS). This includes the specification
    # of static parameters and placeholders for dynamic parameters. AWS Elemental
    # MediaTailor substitutes player-specific and session-specific parameters as
    # needed when calling the ADS. Alternately, for testing, you can provide a
    # static VAST URL. The maximum length is 25000 characters.
    ad_decision_server_url: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The configuration for using a content delivery network (CDN), like Amazon
    # CloudFront, for content and ad segment management.
    cdn_configuration: "CdnConfiguration" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The configuration for HLS content.
    hls_configuration: "HlsConfiguration" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The identifier for the configuration.
    name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The URL that the player accesses to get a manifest from AWS Elemental
    # MediaTailor. This session will use server-side reporting.
    playback_endpoint_prefix: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The URL that the player uses to initialize a session that uses client-side
    # reporting.
    session_initialization_endpoint_prefix: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # URL for a high-quality video asset to transcode and use to fill in time
    # that's not used by ads. AWS Elemental MediaTailor shows the slate to fill
    # in gaps in media content. Configuring the slate is optional for non-VPAID
    # configurations. For VPAID, the slate is required because AWS Elemental
    # MediaTailor provides it in the slots designated for dynamic ad content. The
    # slate must be a high-quality asset that contains both audio and video.
    slate_ad_url: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The URL prefix for the master playlist for the stream, minus the asset ID.
    # The maximum length is 512 characters.
    video_content_source_url: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class PlaybackConfiguration(ShapeBase):
    """
    The AWSMediaTailor configuration.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "ad_decision_server_url",
                "AdDecisionServerUrl",
                TypeInfo(str),
            ),
            (
                "cdn_configuration",
                "CdnConfiguration",
                TypeInfo(CdnConfiguration),
            ),
            (
                "name",
                "Name",
                TypeInfo(str),
            ),
            (
                "slate_ad_url",
                "SlateAdUrl",
                TypeInfo(str),
            ),
            (
                "video_content_source_url",
                "VideoContentSourceUrl",
                TypeInfo(str),
            ),
        ]

    # The URL for the ad decision server (ADS). This includes the specification
    # of static parameters and placeholders for dynamic parameters. AWS Elemental
    # MediaTailor substitutes player-specific and session-specific parameters as
    # needed when calling the ADS. Alternately, for testing, you can provide a
    # static VAST URL. The maximum length is 25000 characters.
    ad_decision_server_url: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The configuration for using a content delivery network (CDN), like Amazon
    # CloudFront, for content and ad segment management.
    cdn_configuration: "CdnConfiguration" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The identifier for the configuration.
    name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # URL for a high-quality video asset to transcode and use to fill in time
    # that's not used by ads. AWS Elemental MediaTailor shows the slate to fill
    # in gaps in media content. Configuring the slate is optional for non-VPAID
    # configurations. For VPAID, the slate is required because AWS Elemental
    # MediaTailor provides it in the slots designated for dynamic ad content. The
    # slate must be a high-quality asset that contains both audio and video.
    slate_ad_url: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The URL prefix for the master playlist for the stream, minus the asset ID.
    # The maximum length is 512 characters.
    video_content_source_url: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class ListPlaybackConfigurationsRequest(ShapeBase):
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

    # Maximum number of records to return.
    max_results: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Pagination token returned by the GET list request when results overrun the
    # meximum allowed. Use the token to fetch the next page of results.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ListPlaybackConfigurationsResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "items",
                "Items",
                TypeInfo(typing.List[PlaybackConfiguration]),
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

    # Array of playback configurations. This may be all of the available
    # configurations or a subset, depending on the settings you provide and on
    # the total number of configurations stored.
    items: typing.List["PlaybackConfiguration"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Pagination token returned by the GET list request when results overrun the
    # meximum allowed. Use the token to fetch the next page of results.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class PutPlaybackConfigurationRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "ad_decision_server_url",
                "AdDecisionServerUrl",
                TypeInfo(str),
            ),
            (
                "cdn_configuration",
                "CdnConfiguration",
                TypeInfo(CdnConfiguration),
            ),
            (
                "name",
                "Name",
                TypeInfo(str),
            ),
            (
                "slate_ad_url",
                "SlateAdUrl",
                TypeInfo(str),
            ),
            (
                "video_content_source_url",
                "VideoContentSourceUrl",
                TypeInfo(str),
            ),
        ]

    # The URL for the ad decision server (ADS). This includes the specification
    # of static parameters and placeholders for dynamic parameters. AWS Elemental
    # MediaTailor substitutes player-specific and session-specific parameters as
    # needed when calling the ADS. Alternately, for testing you can provide a
    # static VAST URL. The maximum length is 25000 characters.
    ad_decision_server_url: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The configuration for using a content delivery network (CDN), like Amazon
    # CloudFront, for content and ad segment management.
    cdn_configuration: "CdnConfiguration" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The identifier for the configuration.
    name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The URL for a high-quality video asset to transcode and use to fill in time
    # that's not used by ads. AWS Elemental MediaTailor shows the slate to fill
    # in gaps in media content. Configuring the slate is optional for non-VPAID
    # configurations. For VPAID, the slate is required because AWS Elemental
    # MediaTailor provides it in the slots that are designated for dynamic ad
    # content. The slate must be a high-quality asset that contains both audio
    # and video.
    slate_ad_url: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The URL prefix for the master playlist for the stream, minus the asset ID.
    # The maximum length is 512 characters.
    video_content_source_url: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class PutPlaybackConfigurationResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "ad_decision_server_url",
                "AdDecisionServerUrl",
                TypeInfo(str),
            ),
            (
                "cdn_configuration",
                "CdnConfiguration",
                TypeInfo(CdnConfiguration),
            ),
            (
                "hls_configuration",
                "HlsConfiguration",
                TypeInfo(HlsConfiguration),
            ),
            (
                "name",
                "Name",
                TypeInfo(str),
            ),
            (
                "playback_endpoint_prefix",
                "PlaybackEndpointPrefix",
                TypeInfo(str),
            ),
            (
                "session_initialization_endpoint_prefix",
                "SessionInitializationEndpointPrefix",
                TypeInfo(str),
            ),
            (
                "slate_ad_url",
                "SlateAdUrl",
                TypeInfo(str),
            ),
            (
                "video_content_source_url",
                "VideoContentSourceUrl",
                TypeInfo(str),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The URL for the ad decision server (ADS). This includes the specification
    # of static parameters and placeholders for dynamic parameters. AWS Elemental
    # MediaTailor substitutes player-specific and session-specific parameters as
    # needed when calling the ADS. Alternately, for testing, you can provide a
    # static VAST URL. The maximum length is 25000 characters.
    ad_decision_server_url: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The configuration for using a content delivery network (CDN), like Amazon
    # CloudFront, for content and ad segment management.
    cdn_configuration: "CdnConfiguration" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The configuration for HLS content.
    hls_configuration: "HlsConfiguration" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The identifier for the configuration.
    name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The URL that the player accesses to get a manifest from AWS Elemental
    # MediaTailor. This session will use server-side reporting.
    playback_endpoint_prefix: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The URL that the player uses to initialize a session that uses client-side
    # reporting.
    session_initialization_endpoint_prefix: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # URL for a high-quality video asset to transcode and use to fill in time
    # that's not used by ads. AWS Elemental MediaTailor shows the slate to fill
    # in gaps in media content. Configuring the slate is optional for non-VPAID
    # configurations. For VPAID, the slate is required because AWS Elemental
    # MediaTailor provides it in the slots designated for dynamic ad content. The
    # slate must be a high-quality asset that contains both audio and video.
    slate_ad_url: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The URL prefix for the master playlist for the stream, minus the asset ID.
    # The maximum length is 512 characters.
    video_content_source_url: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )
