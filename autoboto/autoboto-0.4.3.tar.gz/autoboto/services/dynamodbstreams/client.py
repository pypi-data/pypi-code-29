import datetime
import typing
import boto3
from autoboto import ClientBase, ShapeBase, OutputShapeBase
from . import shapes


class Client(ClientBase):
    def __init__(self, *args, **kwargs):
        super().__init__("dynamodbstreams", *args, **kwargs)

    def describe_stream(
        self,
        _request: shapes.DescribeStreamInput = None,
        *,
        stream_arn: str,
        limit: int = ShapeBase.NOT_SET,
        exclusive_start_shard_id: str = ShapeBase.NOT_SET,
    ) -> shapes.DescribeStreamOutput:
        """
        Returns information about a stream, including the current status of the stream,
        its Amazon Resource Name (ARN), the composition of its shards, and its
        corresponding DynamoDB table.

        You can call `DescribeStream` at a maximum rate of 10 times per second.

        Each shard in the stream has a `SequenceNumberRange` associated with it. If the
        `SequenceNumberRange` has a `StartingSequenceNumber` but no
        `EndingSequenceNumber`, then the shard is still open (able to receive more
        stream records). If both `StartingSequenceNumber` and `EndingSequenceNumber` are
        present, then that shard is closed and can no longer receive more data.
        """
        if _request is None:
            _params = {}
            if stream_arn is not ShapeBase.NOT_SET:
                _params['stream_arn'] = stream_arn
            if limit is not ShapeBase.NOT_SET:
                _params['limit'] = limit
            if exclusive_start_shard_id is not ShapeBase.NOT_SET:
                _params['exclusive_start_shard_id'] = exclusive_start_shard_id
            _request = shapes.DescribeStreamInput(**_params)
        response = self._boto_client.describe_stream(**_request.to_boto())

        return shapes.DescribeStreamOutput.from_boto(response)

    def get_records(
        self,
        _request: shapes.GetRecordsInput = None,
        *,
        shard_iterator: str,
        limit: int = ShapeBase.NOT_SET,
    ) -> shapes.GetRecordsOutput:
        """
        Retrieves the stream records from a given shard.

        Specify a shard iterator using the `ShardIterator` parameter. The shard iterator
        specifies the position in the shard from which you want to start reading stream
        records sequentially. If there are no stream records available in the portion of
        the shard that the iterator points to, `GetRecords` returns an empty list. Note
        that it might take multiple calls to get to a portion of the shard that contains
        stream records.

        `GetRecords` can retrieve a maximum of 1 MB of data or 1000 stream records,
        whichever comes first.
        """
        if _request is None:
            _params = {}
            if shard_iterator is not ShapeBase.NOT_SET:
                _params['shard_iterator'] = shard_iterator
            if limit is not ShapeBase.NOT_SET:
                _params['limit'] = limit
            _request = shapes.GetRecordsInput(**_params)
        response = self._boto_client.get_records(**_request.to_boto())

        return shapes.GetRecordsOutput.from_boto(response)

    def get_shard_iterator(
        self,
        _request: shapes.GetShardIteratorInput = None,
        *,
        stream_arn: str,
        shard_id: str,
        shard_iterator_type: typing.Union[str, shapes.ShardIteratorType],
        sequence_number: str = ShapeBase.NOT_SET,
    ) -> shapes.GetShardIteratorOutput:
        """
        Returns a shard iterator. A shard iterator provides information about how to
        retrieve the stream records from within a shard. Use the shard iterator in a
        subsequent `GetRecords` request to read the stream records from the shard.

        A shard iterator expires 15 minutes after it is returned to the requester.
        """
        if _request is None:
            _params = {}
            if stream_arn is not ShapeBase.NOT_SET:
                _params['stream_arn'] = stream_arn
            if shard_id is not ShapeBase.NOT_SET:
                _params['shard_id'] = shard_id
            if shard_iterator_type is not ShapeBase.NOT_SET:
                _params['shard_iterator_type'] = shard_iterator_type
            if sequence_number is not ShapeBase.NOT_SET:
                _params['sequence_number'] = sequence_number
            _request = shapes.GetShardIteratorInput(**_params)
        response = self._boto_client.get_shard_iterator(**_request.to_boto())

        return shapes.GetShardIteratorOutput.from_boto(response)

    def list_streams(
        self,
        _request: shapes.ListStreamsInput = None,
        *,
        table_name: str = ShapeBase.NOT_SET,
        limit: int = ShapeBase.NOT_SET,
        exclusive_start_stream_arn: str = ShapeBase.NOT_SET,
    ) -> shapes.ListStreamsOutput:
        """
        Returns an array of stream ARNs associated with the current account and
        endpoint. If the `TableName` parameter is present, then `ListStreams` will
        return only the streams ARNs for that table.

        You can call `ListStreams` at a maximum rate of 5 times per second.
        """
        if _request is None:
            _params = {}
            if table_name is not ShapeBase.NOT_SET:
                _params['table_name'] = table_name
            if limit is not ShapeBase.NOT_SET:
                _params['limit'] = limit
            if exclusive_start_stream_arn is not ShapeBase.NOT_SET:
                _params['exclusive_start_stream_arn'
                       ] = exclusive_start_stream_arn
            _request = shapes.ListStreamsInput(**_params)
        response = self._boto_client.list_streams(**_request.to_boto())

        return shapes.ListStreamsOutput.from_boto(response)
