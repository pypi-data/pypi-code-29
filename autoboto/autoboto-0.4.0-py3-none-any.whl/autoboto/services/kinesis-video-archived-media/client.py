import datetime
import typing
import boto3
from autoboto import ClientBase, ShapeBase, OutputShapeBase
from . import shapes


class Client(ClientBase):
    def __init__(self, *args, **kwargs):
        super().__init__("kinesis-video-archived-media", *args, **kwargs)

    def get_hls_streaming_session_url(
        self,
        _request: shapes.GetHLSStreamingSessionURLInput = None,
        *,
        stream_name: str = ShapeBase.NOT_SET,
        stream_arn: str = ShapeBase.NOT_SET,
        playback_mode: typing.Union[str, shapes.PlaybackMode] = ShapeBase.
        NOT_SET,
        hls_fragment_selector: shapes.HLSFragmentSelector = ShapeBase.NOT_SET,
        discontinuity_mode: typing.Union[str, shapes.
                                         DiscontinuityMode] = ShapeBase.NOT_SET,
        expires: int = ShapeBase.NOT_SET,
        max_media_playlist_fragment_results: int = ShapeBase.NOT_SET,
    ) -> shapes.GetHLSStreamingSessionURLOutput:
        """
        Retrieves an HTTP Live Streaming (HLS) URL for the stream. You can then open the
        URL in a browser or media player to view the stream contents.

        You must specify either the `StreamName` or the `StreamARN`.

        An Amazon Kinesis video stream has the following requirements for providing data
        through HLS:

          * The media type must be `video/h264`.

          * Data retention must be greater than 0.

          * The fragments must contain codec private data in the AVC (Advanced Video Coding) for H.264 format ([MPEG-4 specification ISO/IEC 14496-15](https://www.iso.org/standard/55980.html)). For information about adapting stream data to a given format, see [NAL Adaptation Flags](http://docs.aws.amazon.com/kinesisvideostreams/latest/dg/latest/dg/producer-reference-nal.html).

        Kinesis Video Streams HLS sessions contain fragments in the fragmented MPEG-4
        form (also called fMP4 or CMAF), rather than the MPEG-2 form (also called TS
        chunks, which the HLS specification also supports). For more information about
        HLS fragment types, see the [HLS
        specification](https://tools.ietf.org/html/draft-pantos-http-live-streaming-23).

        The following procedure shows how to use HLS with Kinesis Video Streams:

          1. Get an endpoint using [GetDataEndpoint](http://docs.aws.amazon.com/kinesisvideostreams/latest/dg/API_GetDataEndpoint.html), specifying `GET_HLS_STREAMING_SESSION_URL` for the `APIName` parameter.

          2. Retrieve the HLS URL using `GetHLSStreamingSessionURL`. Kinesis Video Streams creates an HLS streaming session to be used for accessing content in a stream using the HLS protocol. `GetHLSStreamingSessionURL` returns an authenticated URL (that includes an encrypted session token) for the session's HLS _master playlist_ (the root resource needed for streaming with HLS).

        Don't share or store this token where an unauthorized entity could access it.
        The token provides access to the content of the stream. Safeguard the token with
        the same measures that you would use with your AWS credentials.

        The media that is made available through the playlist consists only of the
        requested stream, time range, and format. No other media data (such as frames
        outside the requested window or alternate bit rates) is made available.

          3. Provide the URL (containing the encrypted session token) for the HLS master playlist to a media player that supports the HLS protocol. Kinesis Video Streams makes the HLS media playlist, initialization fragment, and media fragments available through the master playlist URL. The initialization fragment contains the codec private data for the stream, and other data needed to set up the video decoder and renderer. The media fragments contain H.264-encoded video frames and time stamps.

          4. The media player receives the authenticated URL and requests stream metadata and media data normally. When the media player requests data, it calls the following actions:

            * **GetHLSMasterPlaylist:** Retrieves an HLS master playlist, which contains a URL for the `GetHLSMediaPlaylist` action, and additional metadata for the media player, including estimated bit rate and resolution.

            * **GetHLSMediaPlaylist:** Retrieves an HLS media playlist, which contains a URL to access the MP4 initialization fragment with the `GetMP4InitFragment` action, and URLs to access the MP4 media fragments with the `GetMP4MediaFragment` actions. The HLS media playlist also contains metadata about the stream that the player needs to play it, such as whether the `PlaybackMode` is `LIVE` or `ON_DEMAND`. The HLS media playlist is typically static for sessions with a `PlaybackType` of `ON_DEMAND`. The HLS media playlist is continually updated with new fragments for sessions with a `PlaybackType` of `LIVE`.

            * **GetMP4InitFragment:** Retrieves the MP4 initialization fragment. The media player typically loads the initialization fragment before loading any media fragments. This fragment contains the "`fytp`" and "`moov`" MP4 atoms, and the child atoms that are needed to initialize the media player decoder.

        The initialization fragment does not correspond to a fragment in a Kinesis video
        stream. It contains only the codec private data for the stream, which the media
        player needs to decode video frames.

            * **GetMP4MediaFragment:** Retrieves MP4 media fragments. These fragments contain the "`moof`" and "`mdat`" MP4 atoms and their child atoms, containing the encoded fragment's video frames and their time stamps. 

        After the first media fragment is made available in a streaming session, any
        fragments that don't contain the same codec private data are excluded in the HLS
        media playlist. Therefore, the codec private data does not change between
        fragments in a session.

        Data retrieved with this action is billable. See
        [Pricing](aws.amazon.comkinesis/video-streams/pricing/) for details.

        The following restrictions apply to HLS sessions:

          * A streaming session URL should not be shared between players. The service might throttle a session if multiple media players are sharing it. For connection limits, see [Kinesis Video Streams Limits](http://docs.aws.amazon.com/kinesisvideostreams/latest/dg/limits.html).

          * A Kinesis video stream can have a maximum of five active HLS streaming sessions. If a new session is created when the maximum number of sessions is already active, the oldest (earliest created) session is closed. The number of active `GetMedia` connections on a Kinesis video stream does not count against this limit, and the number of active HLS sessions does not count against the active `GetMedia` connection limit.

        You can monitor the amount of data that the media player consumes by monitoring
        the `GetMP4MediaFragment.OutgoingBytes` Amazon CloudWatch metric. For
        information about using CloudWatch to monitor Kinesis Video Streams, see
        [Monitoring Kinesis Video
        Streams](http://docs.aws.amazon.com/kinesisvideostreams/latest/dg/monitoring.html).
        For pricing information, see [Amazon Kinesis Video Streams
        Pricing](https://aws.amazon.com/kinesis/video-streams/pricing/) and [AWS
        Pricing](https://aws.amazon.com/pricing/). Charges for both HLS sessions and
        outgoing AWS data apply.

        For more information about HLS, see [HTTP Live
        Streaming](https://developer.apple.com/streaming/) on the [Apple Developer
        site](https://developer.apple.com).
        """
        if _request is None:
            _params = {}
            if stream_name is not ShapeBase.NOT_SET:
                _params['stream_name'] = stream_name
            if stream_arn is not ShapeBase.NOT_SET:
                _params['stream_arn'] = stream_arn
            if playback_mode is not ShapeBase.NOT_SET:
                _params['playback_mode'] = playback_mode
            if hls_fragment_selector is not ShapeBase.NOT_SET:
                _params['hls_fragment_selector'] = hls_fragment_selector
            if discontinuity_mode is not ShapeBase.NOT_SET:
                _params['discontinuity_mode'] = discontinuity_mode
            if expires is not ShapeBase.NOT_SET:
                _params['expires'] = expires
            if max_media_playlist_fragment_results is not ShapeBase.NOT_SET:
                _params['max_media_playlist_fragment_results'
                       ] = max_media_playlist_fragment_results
            _request = shapes.GetHLSStreamingSessionURLInput(**_params)
        response = self._boto_client.get_hls_streaming_session_url(
            **_request.to_boto()
        )

        return shapes.GetHLSStreamingSessionURLOutput.from_boto(response)

    def get_media_for_fragment_list(
        self,
        _request: shapes.GetMediaForFragmentListInput = None,
        *,
        stream_name: str,
        fragments: typing.List[str],
    ) -> shapes.GetMediaForFragmentListOutput:
        """
        Gets media for a list of fragments (specified by fragment number) from the
        archived data in an Amazon Kinesis video stream.

        The following limits apply when using the `GetMediaForFragmentList` API:

          * A client can call `GetMediaForFragmentList` up to five times per second per stream. 

          * Kinesis Video Streams sends media data at a rate of up to 25 megabytes per second (or 200 megabits per second) during a `GetMediaForFragmentList` session.
        """
        if _request is None:
            _params = {}
            if stream_name is not ShapeBase.NOT_SET:
                _params['stream_name'] = stream_name
            if fragments is not ShapeBase.NOT_SET:
                _params['fragments'] = fragments
            _request = shapes.GetMediaForFragmentListInput(**_params)
        response = self._boto_client.get_media_for_fragment_list(
            **_request.to_boto()
        )

        return shapes.GetMediaForFragmentListOutput.from_boto(response)

    def list_fragments(
        self,
        _request: shapes.ListFragmentsInput = None,
        *,
        stream_name: str,
        max_results: int = ShapeBase.NOT_SET,
        next_token: str = ShapeBase.NOT_SET,
        fragment_selector: shapes.FragmentSelector = ShapeBase.NOT_SET,
    ) -> shapes.ListFragmentsOutput:
        """
        Returns a list of Fragment objects from the specified stream and start location
        within the archived data.
        """
        if _request is None:
            _params = {}
            if stream_name is not ShapeBase.NOT_SET:
                _params['stream_name'] = stream_name
            if max_results is not ShapeBase.NOT_SET:
                _params['max_results'] = max_results
            if next_token is not ShapeBase.NOT_SET:
                _params['next_token'] = next_token
            if fragment_selector is not ShapeBase.NOT_SET:
                _params['fragment_selector'] = fragment_selector
            _request = shapes.ListFragmentsInput(**_params)
        response = self._boto_client.list_fragments(**_request.to_boto())

        return shapes.ListFragmentsOutput.from_boto(response)
