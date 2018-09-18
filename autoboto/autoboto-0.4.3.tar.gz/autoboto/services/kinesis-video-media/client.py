import datetime
import typing
import boto3
from autoboto import ClientBase, ShapeBase, OutputShapeBase
from . import shapes


class Client(ClientBase):
    def __init__(self, *args, **kwargs):
        super().__init__("kinesis-video-media", *args, **kwargs)

    def get_media(
        self,
        _request: shapes.GetMediaInput = None,
        *,
        start_selector: shapes.StartSelector,
        stream_name: str = ShapeBase.NOT_SET,
        stream_arn: str = ShapeBase.NOT_SET,
    ) -> shapes.GetMediaOutput:
        """
        Use this API to retrieve media content from a Kinesis video stream. In the
        request, you identify stream name or stream Amazon Resource Name (ARN), and the
        starting chunk. Kinesis Video Streams then returns a stream of chunks in order
        by fragment number.

        You must first call the `GetDataEndpoint` API to get an endpoint to which you
        can then send the `GetMedia` requests.

        When you put media data (fragments) on a stream, Kinesis Video Streams stores
        each incoming fragment and related metadata in what is called a "chunk." For
        more information, see . The `GetMedia` API returns a stream of these chunks
        starting from the chunk that you specify in the request.

        The following limits apply when using the `GetMedia` API:

          * A client can call `GetMedia` up to five times per second per stream. 

          * Kinesis Video Streams sends media data at a rate of up to 25 megabytes per second (or 200 megabits per second) during a `GetMedia` session.
        """
        if _request is None:
            _params = {}
            if start_selector is not ShapeBase.NOT_SET:
                _params['start_selector'] = start_selector
            if stream_name is not ShapeBase.NOT_SET:
                _params['stream_name'] = stream_name
            if stream_arn is not ShapeBase.NOT_SET:
                _params['stream_arn'] = stream_arn
            _request = shapes.GetMediaInput(**_params)
        response = self._boto_client.get_media(**_request.to_boto())

        return shapes.GetMediaOutput.from_boto(response)
