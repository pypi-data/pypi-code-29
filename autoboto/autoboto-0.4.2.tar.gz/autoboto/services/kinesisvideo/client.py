import datetime
import typing
import boto3
from autoboto import ClientBase, ShapeBase, OutputShapeBase
from . import shapes


class Client(ClientBase):
    def __init__(self, *args, **kwargs):
        super().__init__("kinesisvideo", *args, **kwargs)

    def create_stream(
        self,
        _request: shapes.CreateStreamInput = None,
        *,
        stream_name: str,
        device_name: str = ShapeBase.NOT_SET,
        media_type: str = ShapeBase.NOT_SET,
        kms_key_id: str = ShapeBase.NOT_SET,
        data_retention_in_hours: int = ShapeBase.NOT_SET,
    ) -> shapes.CreateStreamOutput:
        """
        Creates a new Kinesis video stream.

        When you create a new stream, Kinesis Video Streams assigns it a version number.
        When you change the stream's metadata, Kinesis Video Streams updates the
        version.

        `CreateStream` is an asynchronous operation.

        For information about how the service works, see [How it
        Works](http://docs.aws.amazon.com/kinesisvideostreams/latest/dg/how-it-
        works.html).

        You must have permissions for the `KinesisVideo:CreateStream` action.
        """
        if _request is None:
            _params = {}
            if stream_name is not ShapeBase.NOT_SET:
                _params['stream_name'] = stream_name
            if device_name is not ShapeBase.NOT_SET:
                _params['device_name'] = device_name
            if media_type is not ShapeBase.NOT_SET:
                _params['media_type'] = media_type
            if kms_key_id is not ShapeBase.NOT_SET:
                _params['kms_key_id'] = kms_key_id
            if data_retention_in_hours is not ShapeBase.NOT_SET:
                _params['data_retention_in_hours'] = data_retention_in_hours
            _request = shapes.CreateStreamInput(**_params)
        response = self._boto_client.create_stream(**_request.to_boto())

        return shapes.CreateStreamOutput.from_boto(response)

    def delete_stream(
        self,
        _request: shapes.DeleteStreamInput = None,
        *,
        stream_arn: str,
        current_version: str = ShapeBase.NOT_SET,
    ) -> shapes.DeleteStreamOutput:
        """
        Deletes a Kinesis video stream and the data contained in the stream.

        This method marks the stream for deletion, and makes the data in the stream
        inaccessible immediately.

        To ensure that you have the latest version of the stream before deleting it, you
        can specify the stream version. Kinesis Video Streams assigns a version to each
        stream. When you update a stream, Kinesis Video Streams assigns a new version
        number. To get the latest stream version, use the `DescribeStream` API.

        This operation requires permission for the `KinesisVideo:DeleteStream` action.
        """
        if _request is None:
            _params = {}
            if stream_arn is not ShapeBase.NOT_SET:
                _params['stream_arn'] = stream_arn
            if current_version is not ShapeBase.NOT_SET:
                _params['current_version'] = current_version
            _request = shapes.DeleteStreamInput(**_params)
        response = self._boto_client.delete_stream(**_request.to_boto())

        return shapes.DeleteStreamOutput.from_boto(response)

    def describe_stream(
        self,
        _request: shapes.DescribeStreamInput = None,
        *,
        stream_name: str = ShapeBase.NOT_SET,
        stream_arn: str = ShapeBase.NOT_SET,
    ) -> shapes.DescribeStreamOutput:
        """
        Returns the most current information about the specified stream. You must
        specify either the `StreamName` or the `StreamARN`.
        """
        if _request is None:
            _params = {}
            if stream_name is not ShapeBase.NOT_SET:
                _params['stream_name'] = stream_name
            if stream_arn is not ShapeBase.NOT_SET:
                _params['stream_arn'] = stream_arn
            _request = shapes.DescribeStreamInput(**_params)
        response = self._boto_client.describe_stream(**_request.to_boto())

        return shapes.DescribeStreamOutput.from_boto(response)

    def get_data_endpoint(
        self,
        _request: shapes.GetDataEndpointInput = None,
        *,
        api_name: typing.Union[str, shapes.APIName],
        stream_name: str = ShapeBase.NOT_SET,
        stream_arn: str = ShapeBase.NOT_SET,
    ) -> shapes.GetDataEndpointOutput:
        """
        Gets an endpoint for a specified stream for either reading or writing. Use this
        endpoint in your application to read from the specified stream (using the
        `GetMedia` or `GetMediaForFragmentList` operations) or write to it (using the
        `PutMedia` operation).

        The returned endpoint does not have the API name appended. The client needs to
        add the API name to the returned endpoint.

        In the request, specify the stream either by `StreamName` or `StreamARN`.
        """
        if _request is None:
            _params = {}
            if api_name is not ShapeBase.NOT_SET:
                _params['api_name'] = api_name
            if stream_name is not ShapeBase.NOT_SET:
                _params['stream_name'] = stream_name
            if stream_arn is not ShapeBase.NOT_SET:
                _params['stream_arn'] = stream_arn
            _request = shapes.GetDataEndpointInput(**_params)
        response = self._boto_client.get_data_endpoint(**_request.to_boto())

        return shapes.GetDataEndpointOutput.from_boto(response)

    def list_streams(
        self,
        _request: shapes.ListStreamsInput = None,
        *,
        max_results: int = ShapeBase.NOT_SET,
        next_token: str = ShapeBase.NOT_SET,
        stream_name_condition: shapes.StreamNameCondition = ShapeBase.NOT_SET,
    ) -> shapes.ListStreamsOutput:
        """
        Returns an array of `StreamInfo` objects. Each object describes a stream. To
        retrieve only streams that satisfy a specific condition, you can specify a
        `StreamNameCondition`.
        """
        if _request is None:
            _params = {}
            if max_results is not ShapeBase.NOT_SET:
                _params['max_results'] = max_results
            if next_token is not ShapeBase.NOT_SET:
                _params['next_token'] = next_token
            if stream_name_condition is not ShapeBase.NOT_SET:
                _params['stream_name_condition'] = stream_name_condition
            _request = shapes.ListStreamsInput(**_params)
        response = self._boto_client.list_streams(**_request.to_boto())

        return shapes.ListStreamsOutput.from_boto(response)

    def list_tags_for_stream(
        self,
        _request: shapes.ListTagsForStreamInput = None,
        *,
        next_token: str = ShapeBase.NOT_SET,
        stream_arn: str = ShapeBase.NOT_SET,
        stream_name: str = ShapeBase.NOT_SET,
    ) -> shapes.ListTagsForStreamOutput:
        """
        Returns a list of tags associated with the specified stream.

        In the request, you must specify either the `StreamName` or the `StreamARN`.
        """
        if _request is None:
            _params = {}
            if next_token is not ShapeBase.NOT_SET:
                _params['next_token'] = next_token
            if stream_arn is not ShapeBase.NOT_SET:
                _params['stream_arn'] = stream_arn
            if stream_name is not ShapeBase.NOT_SET:
                _params['stream_name'] = stream_name
            _request = shapes.ListTagsForStreamInput(**_params)
        response = self._boto_client.list_tags_for_stream(**_request.to_boto())

        return shapes.ListTagsForStreamOutput.from_boto(response)

    def tag_stream(
        self,
        _request: shapes.TagStreamInput = None,
        *,
        tags: typing.Dict[str, str],
        stream_arn: str = ShapeBase.NOT_SET,
        stream_name: str = ShapeBase.NOT_SET,
    ) -> shapes.TagStreamOutput:
        """
        Adds one or more tags to a stream. A _tag_ is a key-value pair (the value is
        optional) that you can define and assign to AWS resources. If you specify a tag
        that already exists, the tag value is replaced with the value that you specify
        in the request. For more information, see [Using Cost Allocation
        Tags](http://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/cost-alloc-
        tags.html) in the _AWS Billing and Cost Management User Guide_.

        You must provide either the `StreamName` or the `StreamARN`.

        This operation requires permission for the `KinesisVideo:TagStream` action.

        Kinesis video streams support up to 50 tags.
        """
        if _request is None:
            _params = {}
            if tags is not ShapeBase.NOT_SET:
                _params['tags'] = tags
            if stream_arn is not ShapeBase.NOT_SET:
                _params['stream_arn'] = stream_arn
            if stream_name is not ShapeBase.NOT_SET:
                _params['stream_name'] = stream_name
            _request = shapes.TagStreamInput(**_params)
        response = self._boto_client.tag_stream(**_request.to_boto())

        return shapes.TagStreamOutput.from_boto(response)

    def untag_stream(
        self,
        _request: shapes.UntagStreamInput = None,
        *,
        tag_key_list: typing.List[str],
        stream_arn: str = ShapeBase.NOT_SET,
        stream_name: str = ShapeBase.NOT_SET,
    ) -> shapes.UntagStreamOutput:
        """
        Removes one or more tags from a stream. In the request, specify only a tag key
        or keys; don't specify the value. If you specify a tag key that does not exist,
        it's ignored.

        In the request, you must provide the `StreamName` or `StreamARN`.
        """
        if _request is None:
            _params = {}
            if tag_key_list is not ShapeBase.NOT_SET:
                _params['tag_key_list'] = tag_key_list
            if stream_arn is not ShapeBase.NOT_SET:
                _params['stream_arn'] = stream_arn
            if stream_name is not ShapeBase.NOT_SET:
                _params['stream_name'] = stream_name
            _request = shapes.UntagStreamInput(**_params)
        response = self._boto_client.untag_stream(**_request.to_boto())

        return shapes.UntagStreamOutput.from_boto(response)

    def update_data_retention(
        self,
        _request: shapes.UpdateDataRetentionInput = None,
        *,
        current_version: str,
        operation: typing.Union[str, shapes.UpdateDataRetentionOperation],
        data_retention_change_in_hours: int,
        stream_name: str = ShapeBase.NOT_SET,
        stream_arn: str = ShapeBase.NOT_SET,
    ) -> shapes.UpdateDataRetentionOutput:
        """
        Increases or decreases the stream's data retention period by the value that you
        specify. To indicate whether you want to increase or decrease the data retention
        period, specify the `Operation` parameter in the request body. In the request,
        you must specify either the `StreamName` or the `StreamARN`.

        The retention period that you specify replaces the current value.

        This operation requires permission for the `KinesisVideo:UpdateDataRetention`
        action.

        Changing the data retention period affects the data in the stream as follows:

          * If the data retention period is increased, existing data is retained for the new retention period. For example, if the data retention period is increased from one hour to seven hours, all existing data is retained for seven hours.

          * If the data retention period is decreased, existing data is retained for the new retention period. For example, if the data retention period is decreased from seven hours to one hour, all existing data is retained for one hour, and any data older than one hour is deleted immediately.
        """
        if _request is None:
            _params = {}
            if current_version is not ShapeBase.NOT_SET:
                _params['current_version'] = current_version
            if operation is not ShapeBase.NOT_SET:
                _params['operation'] = operation
            if data_retention_change_in_hours is not ShapeBase.NOT_SET:
                _params['data_retention_change_in_hours'
                       ] = data_retention_change_in_hours
            if stream_name is not ShapeBase.NOT_SET:
                _params['stream_name'] = stream_name
            if stream_arn is not ShapeBase.NOT_SET:
                _params['stream_arn'] = stream_arn
            _request = shapes.UpdateDataRetentionInput(**_params)
        response = self._boto_client.update_data_retention(**_request.to_boto())

        return shapes.UpdateDataRetentionOutput.from_boto(response)

    def update_stream(
        self,
        _request: shapes.UpdateStreamInput = None,
        *,
        current_version: str,
        stream_name: str = ShapeBase.NOT_SET,
        stream_arn: str = ShapeBase.NOT_SET,
        device_name: str = ShapeBase.NOT_SET,
        media_type: str = ShapeBase.NOT_SET,
    ) -> shapes.UpdateStreamOutput:
        """
        Updates stream metadata, such as the device name and media type.

        You must provide the stream name or the Amazon Resource Name (ARN) of the
        stream.

        To make sure that you have the latest version of the stream before updating it,
        you can specify the stream version. Kinesis Video Streams assigns a version to
        each stream. When you update a stream, Kinesis Video Streams assigns a new
        version number. To get the latest stream version, use the `DescribeStream` API.

        `UpdateStream` is an asynchronous operation, and takes time to complete.
        """
        if _request is None:
            _params = {}
            if current_version is not ShapeBase.NOT_SET:
                _params['current_version'] = current_version
            if stream_name is not ShapeBase.NOT_SET:
                _params['stream_name'] = stream_name
            if stream_arn is not ShapeBase.NOT_SET:
                _params['stream_arn'] = stream_arn
            if device_name is not ShapeBase.NOT_SET:
                _params['device_name'] = device_name
            if media_type is not ShapeBase.NOT_SET:
                _params['media_type'] = media_type
            _request = shapes.UpdateStreamInput(**_params)
        response = self._boto_client.update_stream(**_request.to_boto())

        return shapes.UpdateStreamOutput.from_boto(response)
