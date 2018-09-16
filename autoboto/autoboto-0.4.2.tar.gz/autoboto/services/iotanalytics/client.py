import datetime
import typing
import boto3
from autoboto import ClientBase, ShapeBase, OutputShapeBase
from . import shapes


class Client(ClientBase):
    def __init__(self, *args, **kwargs):
        super().__init__("iotanalytics", *args, **kwargs)

    def batch_put_message(
        self,
        _request: shapes.BatchPutMessageRequest = None,
        *,
        channel_name: str,
        messages: typing.List[shapes.Message],
    ) -> shapes.BatchPutMessageResponse:
        """
        Sends messages to a channel.
        """
        if _request is None:
            _params = {}
            if channel_name is not ShapeBase.NOT_SET:
                _params['channel_name'] = channel_name
            if messages is not ShapeBase.NOT_SET:
                _params['messages'] = messages
            _request = shapes.BatchPutMessageRequest(**_params)
        response = self._boto_client.batch_put_message(**_request.to_boto())

        return shapes.BatchPutMessageResponse.from_boto(response)

    def cancel_pipeline_reprocessing(
        self,
        _request: shapes.CancelPipelineReprocessingRequest = None,
        *,
        pipeline_name: str,
        reprocessing_id: str,
    ) -> shapes.CancelPipelineReprocessingResponse:
        """
        Cancels the reprocessing of data through the pipeline.
        """
        if _request is None:
            _params = {}
            if pipeline_name is not ShapeBase.NOT_SET:
                _params['pipeline_name'] = pipeline_name
            if reprocessing_id is not ShapeBase.NOT_SET:
                _params['reprocessing_id'] = reprocessing_id
            _request = shapes.CancelPipelineReprocessingRequest(**_params)
        response = self._boto_client.cancel_pipeline_reprocessing(
            **_request.to_boto()
        )

        return shapes.CancelPipelineReprocessingResponse.from_boto(response)

    def create_channel(
        self,
        _request: shapes.CreateChannelRequest = None,
        *,
        channel_name: str,
        retention_period: shapes.RetentionPeriod = ShapeBase.NOT_SET,
        tags: typing.List[shapes.Tag] = ShapeBase.NOT_SET,
    ) -> shapes.CreateChannelResponse:
        """
        Creates a channel. A channel collects data from an MQTT topic and archives the
        raw, unprocessed messages before publishing the data to a pipeline.
        """
        if _request is None:
            _params = {}
            if channel_name is not ShapeBase.NOT_SET:
                _params['channel_name'] = channel_name
            if retention_period is not ShapeBase.NOT_SET:
                _params['retention_period'] = retention_period
            if tags is not ShapeBase.NOT_SET:
                _params['tags'] = tags
            _request = shapes.CreateChannelRequest(**_params)
        response = self._boto_client.create_channel(**_request.to_boto())

        return shapes.CreateChannelResponse.from_boto(response)

    def create_dataset(
        self,
        _request: shapes.CreateDatasetRequest = None,
        *,
        dataset_name: str,
        actions: typing.List[shapes.DatasetAction],
        triggers: typing.List[shapes.DatasetTrigger] = ShapeBase.NOT_SET,
        retention_period: shapes.RetentionPeriod = ShapeBase.NOT_SET,
        tags: typing.List[shapes.Tag] = ShapeBase.NOT_SET,
    ) -> shapes.CreateDatasetResponse:
        """
        Creates a data set. A data set stores data retrieved from a data store by
        applying a "queryAction" (a SQL query) or a "containerAction" (executing a
        containerized application). This operation creates the skeleton of a data set.
        The data set can be populated manually by calling "CreateDatasetContent" or
        automatically according to a "trigger" you specify.
        """
        if _request is None:
            _params = {}
            if dataset_name is not ShapeBase.NOT_SET:
                _params['dataset_name'] = dataset_name
            if actions is not ShapeBase.NOT_SET:
                _params['actions'] = actions
            if triggers is not ShapeBase.NOT_SET:
                _params['triggers'] = triggers
            if retention_period is not ShapeBase.NOT_SET:
                _params['retention_period'] = retention_period
            if tags is not ShapeBase.NOT_SET:
                _params['tags'] = tags
            _request = shapes.CreateDatasetRequest(**_params)
        response = self._boto_client.create_dataset(**_request.to_boto())

        return shapes.CreateDatasetResponse.from_boto(response)

    def create_dataset_content(
        self,
        _request: shapes.CreateDatasetContentRequest = None,
        *,
        dataset_name: str,
    ) -> shapes.CreateDatasetContentResponse:
        """
        Creates the content of a data set by applying a SQL action.
        """
        if _request is None:
            _params = {}
            if dataset_name is not ShapeBase.NOT_SET:
                _params['dataset_name'] = dataset_name
            _request = shapes.CreateDatasetContentRequest(**_params)
        response = self._boto_client.create_dataset_content(
            **_request.to_boto()
        )

        return shapes.CreateDatasetContentResponse.from_boto(response)

    def create_datastore(
        self,
        _request: shapes.CreateDatastoreRequest = None,
        *,
        datastore_name: str,
        retention_period: shapes.RetentionPeriod = ShapeBase.NOT_SET,
        tags: typing.List[shapes.Tag] = ShapeBase.NOT_SET,
    ) -> shapes.CreateDatastoreResponse:
        """
        Creates a data store, which is a repository for messages.
        """
        if _request is None:
            _params = {}
            if datastore_name is not ShapeBase.NOT_SET:
                _params['datastore_name'] = datastore_name
            if retention_period is not ShapeBase.NOT_SET:
                _params['retention_period'] = retention_period
            if tags is not ShapeBase.NOT_SET:
                _params['tags'] = tags
            _request = shapes.CreateDatastoreRequest(**_params)
        response = self._boto_client.create_datastore(**_request.to_boto())

        return shapes.CreateDatastoreResponse.from_boto(response)

    def create_pipeline(
        self,
        _request: shapes.CreatePipelineRequest = None,
        *,
        pipeline_name: str,
        pipeline_activities: typing.List[shapes.PipelineActivity],
        tags: typing.List[shapes.Tag] = ShapeBase.NOT_SET,
    ) -> shapes.CreatePipelineResponse:
        """
        Creates a pipeline. A pipeline consumes messages from one or more channels and
        allows you to process the messages before storing them in a data store.
        """
        if _request is None:
            _params = {}
            if pipeline_name is not ShapeBase.NOT_SET:
                _params['pipeline_name'] = pipeline_name
            if pipeline_activities is not ShapeBase.NOT_SET:
                _params['pipeline_activities'] = pipeline_activities
            if tags is not ShapeBase.NOT_SET:
                _params['tags'] = tags
            _request = shapes.CreatePipelineRequest(**_params)
        response = self._boto_client.create_pipeline(**_request.to_boto())

        return shapes.CreatePipelineResponse.from_boto(response)

    def delete_channel(
        self,
        _request: shapes.DeleteChannelRequest = None,
        *,
        channel_name: str,
    ) -> None:
        """
        Deletes the specified channel.
        """
        if _request is None:
            _params = {}
            if channel_name is not ShapeBase.NOT_SET:
                _params['channel_name'] = channel_name
            _request = shapes.DeleteChannelRequest(**_params)
        response = self._boto_client.delete_channel(**_request.to_boto())

    def delete_dataset(
        self,
        _request: shapes.DeleteDatasetRequest = None,
        *,
        dataset_name: str,
    ) -> None:
        """
        Deletes the specified data set.

        You do not have to delete the content of the data set before you perform this
        operation.
        """
        if _request is None:
            _params = {}
            if dataset_name is not ShapeBase.NOT_SET:
                _params['dataset_name'] = dataset_name
            _request = shapes.DeleteDatasetRequest(**_params)
        response = self._boto_client.delete_dataset(**_request.to_boto())

    def delete_dataset_content(
        self,
        _request: shapes.DeleteDatasetContentRequest = None,
        *,
        dataset_name: str,
        version_id: str = ShapeBase.NOT_SET,
    ) -> None:
        """
        Deletes the content of the specified data set.
        """
        if _request is None:
            _params = {}
            if dataset_name is not ShapeBase.NOT_SET:
                _params['dataset_name'] = dataset_name
            if version_id is not ShapeBase.NOT_SET:
                _params['version_id'] = version_id
            _request = shapes.DeleteDatasetContentRequest(**_params)
        response = self._boto_client.delete_dataset_content(
            **_request.to_boto()
        )

    def delete_datastore(
        self,
        _request: shapes.DeleteDatastoreRequest = None,
        *,
        datastore_name: str,
    ) -> None:
        """
        Deletes the specified data store.
        """
        if _request is None:
            _params = {}
            if datastore_name is not ShapeBase.NOT_SET:
                _params['datastore_name'] = datastore_name
            _request = shapes.DeleteDatastoreRequest(**_params)
        response = self._boto_client.delete_datastore(**_request.to_boto())

    def delete_pipeline(
        self,
        _request: shapes.DeletePipelineRequest = None,
        *,
        pipeline_name: str,
    ) -> None:
        """
        Deletes the specified pipeline.
        """
        if _request is None:
            _params = {}
            if pipeline_name is not ShapeBase.NOT_SET:
                _params['pipeline_name'] = pipeline_name
            _request = shapes.DeletePipelineRequest(**_params)
        response = self._boto_client.delete_pipeline(**_request.to_boto())

    def describe_channel(
        self,
        _request: shapes.DescribeChannelRequest = None,
        *,
        channel_name: str,
        include_statistics: bool = ShapeBase.NOT_SET,
    ) -> shapes.DescribeChannelResponse:
        """
        Retrieves information about a channel.
        """
        if _request is None:
            _params = {}
            if channel_name is not ShapeBase.NOT_SET:
                _params['channel_name'] = channel_name
            if include_statistics is not ShapeBase.NOT_SET:
                _params['include_statistics'] = include_statistics
            _request = shapes.DescribeChannelRequest(**_params)
        response = self._boto_client.describe_channel(**_request.to_boto())

        return shapes.DescribeChannelResponse.from_boto(response)

    def describe_dataset(
        self,
        _request: shapes.DescribeDatasetRequest = None,
        *,
        dataset_name: str,
    ) -> shapes.DescribeDatasetResponse:
        """
        Retrieves information about a data set.
        """
        if _request is None:
            _params = {}
            if dataset_name is not ShapeBase.NOT_SET:
                _params['dataset_name'] = dataset_name
            _request = shapes.DescribeDatasetRequest(**_params)
        response = self._boto_client.describe_dataset(**_request.to_boto())

        return shapes.DescribeDatasetResponse.from_boto(response)

    def describe_datastore(
        self,
        _request: shapes.DescribeDatastoreRequest = None,
        *,
        datastore_name: str,
        include_statistics: bool = ShapeBase.NOT_SET,
    ) -> shapes.DescribeDatastoreResponse:
        """
        Retrieves information about a data store.
        """
        if _request is None:
            _params = {}
            if datastore_name is not ShapeBase.NOT_SET:
                _params['datastore_name'] = datastore_name
            if include_statistics is not ShapeBase.NOT_SET:
                _params['include_statistics'] = include_statistics
            _request = shapes.DescribeDatastoreRequest(**_params)
        response = self._boto_client.describe_datastore(**_request.to_boto())

        return shapes.DescribeDatastoreResponse.from_boto(response)

    def describe_logging_options(
        self,
        _request: shapes.DescribeLoggingOptionsRequest = None,
    ) -> shapes.DescribeLoggingOptionsResponse:
        """
        Retrieves the current settings of the AWS IoT Analytics logging options.
        """
        if _request is None:
            _params = {}
            _request = shapes.DescribeLoggingOptionsRequest(**_params)
        response = self._boto_client.describe_logging_options(
            **_request.to_boto()
        )

        return shapes.DescribeLoggingOptionsResponse.from_boto(response)

    def describe_pipeline(
        self,
        _request: shapes.DescribePipelineRequest = None,
        *,
        pipeline_name: str,
    ) -> shapes.DescribePipelineResponse:
        """
        Retrieves information about a pipeline.
        """
        if _request is None:
            _params = {}
            if pipeline_name is not ShapeBase.NOT_SET:
                _params['pipeline_name'] = pipeline_name
            _request = shapes.DescribePipelineRequest(**_params)
        response = self._boto_client.describe_pipeline(**_request.to_boto())

        return shapes.DescribePipelineResponse.from_boto(response)

    def get_dataset_content(
        self,
        _request: shapes.GetDatasetContentRequest = None,
        *,
        dataset_name: str,
        version_id: str = ShapeBase.NOT_SET,
    ) -> shapes.GetDatasetContentResponse:
        """
        Retrieves the contents of a data set as pre-signed URIs.
        """
        if _request is None:
            _params = {}
            if dataset_name is not ShapeBase.NOT_SET:
                _params['dataset_name'] = dataset_name
            if version_id is not ShapeBase.NOT_SET:
                _params['version_id'] = version_id
            _request = shapes.GetDatasetContentRequest(**_params)
        response = self._boto_client.get_dataset_content(**_request.to_boto())

        return shapes.GetDatasetContentResponse.from_boto(response)

    def list_channels(
        self,
        _request: shapes.ListChannelsRequest = None,
        *,
        next_token: str = ShapeBase.NOT_SET,
        max_results: int = ShapeBase.NOT_SET,
    ) -> shapes.ListChannelsResponse:
        """
        Retrieves a list of channels.
        """
        if _request is None:
            _params = {}
            if next_token is not ShapeBase.NOT_SET:
                _params['next_token'] = next_token
            if max_results is not ShapeBase.NOT_SET:
                _params['max_results'] = max_results
            _request = shapes.ListChannelsRequest(**_params)
        response = self._boto_client.list_channels(**_request.to_boto())

        return shapes.ListChannelsResponse.from_boto(response)

    def list_dataset_contents(
        self,
        _request: shapes.ListDatasetContentsRequest = None,
        *,
        dataset_name: str,
        next_token: str = ShapeBase.NOT_SET,
        max_results: int = ShapeBase.NOT_SET,
    ) -> shapes.ListDatasetContentsResponse:
        """
        Lists information about data set contents that have been created.
        """
        if _request is None:
            _params = {}
            if dataset_name is not ShapeBase.NOT_SET:
                _params['dataset_name'] = dataset_name
            if next_token is not ShapeBase.NOT_SET:
                _params['next_token'] = next_token
            if max_results is not ShapeBase.NOT_SET:
                _params['max_results'] = max_results
            _request = shapes.ListDatasetContentsRequest(**_params)
        response = self._boto_client.list_dataset_contents(**_request.to_boto())

        return shapes.ListDatasetContentsResponse.from_boto(response)

    def list_datasets(
        self,
        _request: shapes.ListDatasetsRequest = None,
        *,
        next_token: str = ShapeBase.NOT_SET,
        max_results: int = ShapeBase.NOT_SET,
    ) -> shapes.ListDatasetsResponse:
        """
        Retrieves information about data sets.
        """
        if _request is None:
            _params = {}
            if next_token is not ShapeBase.NOT_SET:
                _params['next_token'] = next_token
            if max_results is not ShapeBase.NOT_SET:
                _params['max_results'] = max_results
            _request = shapes.ListDatasetsRequest(**_params)
        response = self._boto_client.list_datasets(**_request.to_boto())

        return shapes.ListDatasetsResponse.from_boto(response)

    def list_datastores(
        self,
        _request: shapes.ListDatastoresRequest = None,
        *,
        next_token: str = ShapeBase.NOT_SET,
        max_results: int = ShapeBase.NOT_SET,
    ) -> shapes.ListDatastoresResponse:
        """
        Retrieves a list of data stores.
        """
        if _request is None:
            _params = {}
            if next_token is not ShapeBase.NOT_SET:
                _params['next_token'] = next_token
            if max_results is not ShapeBase.NOT_SET:
                _params['max_results'] = max_results
            _request = shapes.ListDatastoresRequest(**_params)
        response = self._boto_client.list_datastores(**_request.to_boto())

        return shapes.ListDatastoresResponse.from_boto(response)

    def list_pipelines(
        self,
        _request: shapes.ListPipelinesRequest = None,
        *,
        next_token: str = ShapeBase.NOT_SET,
        max_results: int = ShapeBase.NOT_SET,
    ) -> shapes.ListPipelinesResponse:
        """
        Retrieves a list of pipelines.
        """
        if _request is None:
            _params = {}
            if next_token is not ShapeBase.NOT_SET:
                _params['next_token'] = next_token
            if max_results is not ShapeBase.NOT_SET:
                _params['max_results'] = max_results
            _request = shapes.ListPipelinesRequest(**_params)
        response = self._boto_client.list_pipelines(**_request.to_boto())

        return shapes.ListPipelinesResponse.from_boto(response)

    def list_tags_for_resource(
        self,
        _request: shapes.ListTagsForResourceRequest = None,
        *,
        resource_arn: str,
    ) -> shapes.ListTagsForResourceResponse:
        """
        Lists the tags (metadata) which you have assigned to the resource.
        """
        if _request is None:
            _params = {}
            if resource_arn is not ShapeBase.NOT_SET:
                _params['resource_arn'] = resource_arn
            _request = shapes.ListTagsForResourceRequest(**_params)
        response = self._boto_client.list_tags_for_resource(
            **_request.to_boto()
        )

        return shapes.ListTagsForResourceResponse.from_boto(response)

    def put_logging_options(
        self,
        _request: shapes.PutLoggingOptionsRequest = None,
        *,
        logging_options: shapes.LoggingOptions,
    ) -> None:
        """
        Sets or updates the AWS IoT Analytics logging options.

        Note that if you update the value of any `loggingOptions` field, it takes up to
        one minute for the change to take effect. Also, if you change the policy
        attached to the role you specified in the roleArn field (for example, to correct
        an invalid policy) it takes up to 5 minutes for that change to take effect.
        """
        if _request is None:
            _params = {}
            if logging_options is not ShapeBase.NOT_SET:
                _params['logging_options'] = logging_options
            _request = shapes.PutLoggingOptionsRequest(**_params)
        response = self._boto_client.put_logging_options(**_request.to_boto())

    def run_pipeline_activity(
        self,
        _request: shapes.RunPipelineActivityRequest = None,
        *,
        pipeline_activity: shapes.PipelineActivity,
        payloads: typing.List[typing.Any],
    ) -> shapes.RunPipelineActivityResponse:
        """
        Simulates the results of running a pipeline activity on a message payload.
        """
        if _request is None:
            _params = {}
            if pipeline_activity is not ShapeBase.NOT_SET:
                _params['pipeline_activity'] = pipeline_activity
            if payloads is not ShapeBase.NOT_SET:
                _params['payloads'] = payloads
            _request = shapes.RunPipelineActivityRequest(**_params)
        response = self._boto_client.run_pipeline_activity(**_request.to_boto())

        return shapes.RunPipelineActivityResponse.from_boto(response)

    def sample_channel_data(
        self,
        _request: shapes.SampleChannelDataRequest = None,
        *,
        channel_name: str,
        max_messages: int = ShapeBase.NOT_SET,
        start_time: datetime.datetime = ShapeBase.NOT_SET,
        end_time: datetime.datetime = ShapeBase.NOT_SET,
    ) -> shapes.SampleChannelDataResponse:
        """
        Retrieves a sample of messages from the specified channel ingested during the
        specified timeframe. Up to 10 messages can be retrieved.
        """
        if _request is None:
            _params = {}
            if channel_name is not ShapeBase.NOT_SET:
                _params['channel_name'] = channel_name
            if max_messages is not ShapeBase.NOT_SET:
                _params['max_messages'] = max_messages
            if start_time is not ShapeBase.NOT_SET:
                _params['start_time'] = start_time
            if end_time is not ShapeBase.NOT_SET:
                _params['end_time'] = end_time
            _request = shapes.SampleChannelDataRequest(**_params)
        response = self._boto_client.sample_channel_data(**_request.to_boto())

        return shapes.SampleChannelDataResponse.from_boto(response)

    def start_pipeline_reprocessing(
        self,
        _request: shapes.StartPipelineReprocessingRequest = None,
        *,
        pipeline_name: str,
        start_time: datetime.datetime = ShapeBase.NOT_SET,
        end_time: datetime.datetime = ShapeBase.NOT_SET,
    ) -> shapes.StartPipelineReprocessingResponse:
        """
        Starts the reprocessing of raw message data through the pipeline.
        """
        if _request is None:
            _params = {}
            if pipeline_name is not ShapeBase.NOT_SET:
                _params['pipeline_name'] = pipeline_name
            if start_time is not ShapeBase.NOT_SET:
                _params['start_time'] = start_time
            if end_time is not ShapeBase.NOT_SET:
                _params['end_time'] = end_time
            _request = shapes.StartPipelineReprocessingRequest(**_params)
        response = self._boto_client.start_pipeline_reprocessing(
            **_request.to_boto()
        )

        return shapes.StartPipelineReprocessingResponse.from_boto(response)

    def tag_resource(
        self,
        _request: shapes.TagResourceRequest = None,
        *,
        resource_arn: str,
        tags: typing.List[shapes.Tag],
    ) -> shapes.TagResourceResponse:
        """
        Adds to or modifies the tags of the given resource. Tags are metadata which can
        be used to manage a resource.
        """
        if _request is None:
            _params = {}
            if resource_arn is not ShapeBase.NOT_SET:
                _params['resource_arn'] = resource_arn
            if tags is not ShapeBase.NOT_SET:
                _params['tags'] = tags
            _request = shapes.TagResourceRequest(**_params)
        response = self._boto_client.tag_resource(**_request.to_boto())

        return shapes.TagResourceResponse.from_boto(response)

    def untag_resource(
        self,
        _request: shapes.UntagResourceRequest = None,
        *,
        resource_arn: str,
        tag_keys: typing.List[str],
    ) -> shapes.UntagResourceResponse:
        """
        Removes the given tags (metadata) from the resource.
        """
        if _request is None:
            _params = {}
            if resource_arn is not ShapeBase.NOT_SET:
                _params['resource_arn'] = resource_arn
            if tag_keys is not ShapeBase.NOT_SET:
                _params['tag_keys'] = tag_keys
            _request = shapes.UntagResourceRequest(**_params)
        response = self._boto_client.untag_resource(**_request.to_boto())

        return shapes.UntagResourceResponse.from_boto(response)

    def update_channel(
        self,
        _request: shapes.UpdateChannelRequest = None,
        *,
        channel_name: str,
        retention_period: shapes.RetentionPeriod = ShapeBase.NOT_SET,
    ) -> None:
        """
        Updates the settings of a channel.
        """
        if _request is None:
            _params = {}
            if channel_name is not ShapeBase.NOT_SET:
                _params['channel_name'] = channel_name
            if retention_period is not ShapeBase.NOT_SET:
                _params['retention_period'] = retention_period
            _request = shapes.UpdateChannelRequest(**_params)
        response = self._boto_client.update_channel(**_request.to_boto())

    def update_dataset(
        self,
        _request: shapes.UpdateDatasetRequest = None,
        *,
        dataset_name: str,
        actions: typing.List[shapes.DatasetAction],
        triggers: typing.List[shapes.DatasetTrigger] = ShapeBase.NOT_SET,
        retention_period: shapes.RetentionPeriod = ShapeBase.NOT_SET,
    ) -> None:
        """
        Updates the settings of a data set.
        """
        if _request is None:
            _params = {}
            if dataset_name is not ShapeBase.NOT_SET:
                _params['dataset_name'] = dataset_name
            if actions is not ShapeBase.NOT_SET:
                _params['actions'] = actions
            if triggers is not ShapeBase.NOT_SET:
                _params['triggers'] = triggers
            if retention_period is not ShapeBase.NOT_SET:
                _params['retention_period'] = retention_period
            _request = shapes.UpdateDatasetRequest(**_params)
        response = self._boto_client.update_dataset(**_request.to_boto())

    def update_datastore(
        self,
        _request: shapes.UpdateDatastoreRequest = None,
        *,
        datastore_name: str,
        retention_period: shapes.RetentionPeriod = ShapeBase.NOT_SET,
    ) -> None:
        """
        Updates the settings of a data store.
        """
        if _request is None:
            _params = {}
            if datastore_name is not ShapeBase.NOT_SET:
                _params['datastore_name'] = datastore_name
            if retention_period is not ShapeBase.NOT_SET:
                _params['retention_period'] = retention_period
            _request = shapes.UpdateDatastoreRequest(**_params)
        response = self._boto_client.update_datastore(**_request.to_boto())

    def update_pipeline(
        self,
        _request: shapes.UpdatePipelineRequest = None,
        *,
        pipeline_name: str,
        pipeline_activities: typing.List[shapes.PipelineActivity],
    ) -> None:
        """
        Updates the settings of a pipeline.
        """
        if _request is None:
            _params = {}
            if pipeline_name is not ShapeBase.NOT_SET:
                _params['pipeline_name'] = pipeline_name
            if pipeline_activities is not ShapeBase.NOT_SET:
                _params['pipeline_activities'] = pipeline_activities
            _request = shapes.UpdatePipelineRequest(**_params)
        response = self._boto_client.update_pipeline(**_request.to_boto())
