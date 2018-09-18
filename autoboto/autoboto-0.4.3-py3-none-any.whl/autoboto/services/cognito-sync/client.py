import datetime
import typing
import boto3
from autoboto import ClientBase, ShapeBase, OutputShapeBase
from . import shapes


class Client(ClientBase):
    def __init__(self, *args, **kwargs):
        super().__init__("cognito-sync", *args, **kwargs)

    def bulk_publish(
        self,
        _request: shapes.BulkPublishRequest = None,
        *,
        identity_pool_id: str,
    ) -> shapes.BulkPublishResponse:
        """
        Initiates a bulk publish of all existing datasets for an Identity Pool to the
        configured stream. Customers are limited to one successful bulk publish per 24
        hours. Bulk publish is an asynchronous request, customers can see the status of
        the request via the GetBulkPublishDetails operation.

        This API can only be called with developer credentials. You cannot call this API
        with the temporary user credentials provided by Cognito Identity.
        """
        if _request is None:
            _params = {}
            if identity_pool_id is not ShapeBase.NOT_SET:
                _params['identity_pool_id'] = identity_pool_id
            _request = shapes.BulkPublishRequest(**_params)
        response = self._boto_client.bulk_publish(**_request.to_boto())

        return shapes.BulkPublishResponse.from_boto(response)

    def delete_dataset(
        self,
        _request: shapes.DeleteDatasetRequest = None,
        *,
        identity_pool_id: str,
        identity_id: str,
        dataset_name: str,
    ) -> shapes.DeleteDatasetResponse:
        """
        Deletes the specific dataset. The dataset will be deleted permanently, and the
        action can't be undone. Datasets that this dataset was merged with will no
        longer report the merge. Any subsequent operation on this dataset will result in
        a ResourceNotFoundException.

        This API can be called with temporary user credentials provided by Cognito
        Identity or with developer credentials.
        """
        if _request is None:
            _params = {}
            if identity_pool_id is not ShapeBase.NOT_SET:
                _params['identity_pool_id'] = identity_pool_id
            if identity_id is not ShapeBase.NOT_SET:
                _params['identity_id'] = identity_id
            if dataset_name is not ShapeBase.NOT_SET:
                _params['dataset_name'] = dataset_name
            _request = shapes.DeleteDatasetRequest(**_params)
        response = self._boto_client.delete_dataset(**_request.to_boto())

        return shapes.DeleteDatasetResponse.from_boto(response)

    def describe_dataset(
        self,
        _request: shapes.DescribeDatasetRequest = None,
        *,
        identity_pool_id: str,
        identity_id: str,
        dataset_name: str,
    ) -> shapes.DescribeDatasetResponse:
        """
        Gets meta data about a dataset by identity and dataset name. With Amazon Cognito
        Sync, each identity has access only to its own data. Thus, the credentials used
        to make this API call need to have access to the identity data.

        This API can be called with temporary user credentials provided by Cognito
        Identity or with developer credentials. You should use Cognito Identity
        credentials to make this API call.
        """
        if _request is None:
            _params = {}
            if identity_pool_id is not ShapeBase.NOT_SET:
                _params['identity_pool_id'] = identity_pool_id
            if identity_id is not ShapeBase.NOT_SET:
                _params['identity_id'] = identity_id
            if dataset_name is not ShapeBase.NOT_SET:
                _params['dataset_name'] = dataset_name
            _request = shapes.DescribeDatasetRequest(**_params)
        response = self._boto_client.describe_dataset(**_request.to_boto())

        return shapes.DescribeDatasetResponse.from_boto(response)

    def describe_identity_pool_usage(
        self,
        _request: shapes.DescribeIdentityPoolUsageRequest = None,
        *,
        identity_pool_id: str,
    ) -> shapes.DescribeIdentityPoolUsageResponse:
        """
        Gets usage details (for example, data storage) about a particular identity pool.

        This API can only be called with developer credentials. You cannot call this API
        with the temporary user credentials provided by Cognito Identity.
        """
        if _request is None:
            _params = {}
            if identity_pool_id is not ShapeBase.NOT_SET:
                _params['identity_pool_id'] = identity_pool_id
            _request = shapes.DescribeIdentityPoolUsageRequest(**_params)
        response = self._boto_client.describe_identity_pool_usage(
            **_request.to_boto()
        )

        return shapes.DescribeIdentityPoolUsageResponse.from_boto(response)

    def describe_identity_usage(
        self,
        _request: shapes.DescribeIdentityUsageRequest = None,
        *,
        identity_pool_id: str,
        identity_id: str,
    ) -> shapes.DescribeIdentityUsageResponse:
        """
        Gets usage information for an identity, including number of datasets and data
        usage.

        This API can be called with temporary user credentials provided by Cognito
        Identity or with developer credentials.
        """
        if _request is None:
            _params = {}
            if identity_pool_id is not ShapeBase.NOT_SET:
                _params['identity_pool_id'] = identity_pool_id
            if identity_id is not ShapeBase.NOT_SET:
                _params['identity_id'] = identity_id
            _request = shapes.DescribeIdentityUsageRequest(**_params)
        response = self._boto_client.describe_identity_usage(
            **_request.to_boto()
        )

        return shapes.DescribeIdentityUsageResponse.from_boto(response)

    def get_bulk_publish_details(
        self,
        _request: shapes.GetBulkPublishDetailsRequest = None,
        *,
        identity_pool_id: str,
    ) -> shapes.GetBulkPublishDetailsResponse:
        """
        Get the status of the last BulkPublish operation for an identity pool.

        This API can only be called with developer credentials. You cannot call this API
        with the temporary user credentials provided by Cognito Identity.
        """
        if _request is None:
            _params = {}
            if identity_pool_id is not ShapeBase.NOT_SET:
                _params['identity_pool_id'] = identity_pool_id
            _request = shapes.GetBulkPublishDetailsRequest(**_params)
        response = self._boto_client.get_bulk_publish_details(
            **_request.to_boto()
        )

        return shapes.GetBulkPublishDetailsResponse.from_boto(response)

    def get_cognito_events(
        self,
        _request: shapes.GetCognitoEventsRequest = None,
        *,
        identity_pool_id: str,
    ) -> shapes.GetCognitoEventsResponse:
        """
        Gets the events and the corresponding Lambda functions associated with an
        identity pool.

        This API can only be called with developer credentials. You cannot call this API
        with the temporary user credentials provided by Cognito Identity.
        """
        if _request is None:
            _params = {}
            if identity_pool_id is not ShapeBase.NOT_SET:
                _params['identity_pool_id'] = identity_pool_id
            _request = shapes.GetCognitoEventsRequest(**_params)
        response = self._boto_client.get_cognito_events(**_request.to_boto())

        return shapes.GetCognitoEventsResponse.from_boto(response)

    def get_identity_pool_configuration(
        self,
        _request: shapes.GetIdentityPoolConfigurationRequest = None,
        *,
        identity_pool_id: str,
    ) -> shapes.GetIdentityPoolConfigurationResponse:
        """
        Gets the configuration settings of an identity pool.

        This API can only be called with developer credentials. You cannot call this API
        with the temporary user credentials provided by Cognito Identity.
        """
        if _request is None:
            _params = {}
            if identity_pool_id is not ShapeBase.NOT_SET:
                _params['identity_pool_id'] = identity_pool_id
            _request = shapes.GetIdentityPoolConfigurationRequest(**_params)
        response = self._boto_client.get_identity_pool_configuration(
            **_request.to_boto()
        )

        return shapes.GetIdentityPoolConfigurationResponse.from_boto(response)

    def list_datasets(
        self,
        _request: shapes.ListDatasetsRequest = None,
        *,
        identity_pool_id: str,
        identity_id: str,
        next_token: str = ShapeBase.NOT_SET,
        max_results: int = ShapeBase.NOT_SET,
    ) -> shapes.ListDatasetsResponse:
        """
        Lists datasets for an identity. With Amazon Cognito Sync, each identity has
        access only to its own data. Thus, the credentials used to make this API call
        need to have access to the identity data.

        ListDatasets can be called with temporary user credentials provided by Cognito
        Identity or with developer credentials. You should use the Cognito Identity
        credentials to make this API call.
        """
        if _request is None:
            _params = {}
            if identity_pool_id is not ShapeBase.NOT_SET:
                _params['identity_pool_id'] = identity_pool_id
            if identity_id is not ShapeBase.NOT_SET:
                _params['identity_id'] = identity_id
            if next_token is not ShapeBase.NOT_SET:
                _params['next_token'] = next_token
            if max_results is not ShapeBase.NOT_SET:
                _params['max_results'] = max_results
            _request = shapes.ListDatasetsRequest(**_params)
        response = self._boto_client.list_datasets(**_request.to_boto())

        return shapes.ListDatasetsResponse.from_boto(response)

    def list_identity_pool_usage(
        self,
        _request: shapes.ListIdentityPoolUsageRequest = None,
        *,
        next_token: str = ShapeBase.NOT_SET,
        max_results: int = ShapeBase.NOT_SET,
    ) -> shapes.ListIdentityPoolUsageResponse:
        """
        Gets a list of identity pools registered with Cognito.

        ListIdentityPoolUsage can only be called with developer credentials. You cannot
        make this API call with the temporary user credentials provided by Cognito
        Identity.
        """
        if _request is None:
            _params = {}
            if next_token is not ShapeBase.NOT_SET:
                _params['next_token'] = next_token
            if max_results is not ShapeBase.NOT_SET:
                _params['max_results'] = max_results
            _request = shapes.ListIdentityPoolUsageRequest(**_params)
        response = self._boto_client.list_identity_pool_usage(
            **_request.to_boto()
        )

        return shapes.ListIdentityPoolUsageResponse.from_boto(response)

    def list_records(
        self,
        _request: shapes.ListRecordsRequest = None,
        *,
        identity_pool_id: str,
        identity_id: str,
        dataset_name: str,
        last_sync_count: int = ShapeBase.NOT_SET,
        next_token: str = ShapeBase.NOT_SET,
        max_results: int = ShapeBase.NOT_SET,
        sync_session_token: str = ShapeBase.NOT_SET,
    ) -> shapes.ListRecordsResponse:
        """
        Gets paginated records, optionally changed after a particular sync count for a
        dataset and identity. With Amazon Cognito Sync, each identity has access only to
        its own data. Thus, the credentials used to make this API call need to have
        access to the identity data.

        ListRecords can be called with temporary user credentials provided by Cognito
        Identity or with developer credentials. You should use Cognito Identity
        credentials to make this API call.
        """
        if _request is None:
            _params = {}
            if identity_pool_id is not ShapeBase.NOT_SET:
                _params['identity_pool_id'] = identity_pool_id
            if identity_id is not ShapeBase.NOT_SET:
                _params['identity_id'] = identity_id
            if dataset_name is not ShapeBase.NOT_SET:
                _params['dataset_name'] = dataset_name
            if last_sync_count is not ShapeBase.NOT_SET:
                _params['last_sync_count'] = last_sync_count
            if next_token is not ShapeBase.NOT_SET:
                _params['next_token'] = next_token
            if max_results is not ShapeBase.NOT_SET:
                _params['max_results'] = max_results
            if sync_session_token is not ShapeBase.NOT_SET:
                _params['sync_session_token'] = sync_session_token
            _request = shapes.ListRecordsRequest(**_params)
        response = self._boto_client.list_records(**_request.to_boto())

        return shapes.ListRecordsResponse.from_boto(response)

    def register_device(
        self,
        _request: shapes.RegisterDeviceRequest = None,
        *,
        identity_pool_id: str,
        identity_id: str,
        platform: typing.Union[str, shapes.Platform],
        token: str,
    ) -> shapes.RegisterDeviceResponse:
        """
        Registers a device to receive push sync notifications.

        This API can only be called with temporary credentials provided by Cognito
        Identity. You cannot call this API with developer credentials.
        """
        if _request is None:
            _params = {}
            if identity_pool_id is not ShapeBase.NOT_SET:
                _params['identity_pool_id'] = identity_pool_id
            if identity_id is not ShapeBase.NOT_SET:
                _params['identity_id'] = identity_id
            if platform is not ShapeBase.NOT_SET:
                _params['platform'] = platform
            if token is not ShapeBase.NOT_SET:
                _params['token'] = token
            _request = shapes.RegisterDeviceRequest(**_params)
        response = self._boto_client.register_device(**_request.to_boto())

        return shapes.RegisterDeviceResponse.from_boto(response)

    def set_cognito_events(
        self,
        _request: shapes.SetCognitoEventsRequest = None,
        *,
        identity_pool_id: str,
        events: typing.Dict[str, str],
    ) -> None:
        """
        Sets the AWS Lambda function for a given event type for an identity pool. This
        request only updates the key/value pair specified. Other key/values pairs are
        not updated. To remove a key value pair, pass a empty value for the particular
        key.

        This API can only be called with developer credentials. You cannot call this API
        with the temporary user credentials provided by Cognito Identity.
        """
        if _request is None:
            _params = {}
            if identity_pool_id is not ShapeBase.NOT_SET:
                _params['identity_pool_id'] = identity_pool_id
            if events is not ShapeBase.NOT_SET:
                _params['events'] = events
            _request = shapes.SetCognitoEventsRequest(**_params)
        response = self._boto_client.set_cognito_events(**_request.to_boto())

    def set_identity_pool_configuration(
        self,
        _request: shapes.SetIdentityPoolConfigurationRequest = None,
        *,
        identity_pool_id: str,
        push_sync: shapes.PushSync = ShapeBase.NOT_SET,
        cognito_streams: shapes.CognitoStreams = ShapeBase.NOT_SET,
    ) -> shapes.SetIdentityPoolConfigurationResponse:
        """
        Sets the necessary configuration for push sync.

        This API can only be called with developer credentials. You cannot call this API
        with the temporary user credentials provided by Cognito Identity.
        """
        if _request is None:
            _params = {}
            if identity_pool_id is not ShapeBase.NOT_SET:
                _params['identity_pool_id'] = identity_pool_id
            if push_sync is not ShapeBase.NOT_SET:
                _params['push_sync'] = push_sync
            if cognito_streams is not ShapeBase.NOT_SET:
                _params['cognito_streams'] = cognito_streams
            _request = shapes.SetIdentityPoolConfigurationRequest(**_params)
        response = self._boto_client.set_identity_pool_configuration(
            **_request.to_boto()
        )

        return shapes.SetIdentityPoolConfigurationResponse.from_boto(response)

    def subscribe_to_dataset(
        self,
        _request: shapes.SubscribeToDatasetRequest = None,
        *,
        identity_pool_id: str,
        identity_id: str,
        dataset_name: str,
        device_id: str,
    ) -> shapes.SubscribeToDatasetResponse:
        """
        Subscribes to receive notifications when a dataset is modified by another
        device.

        This API can only be called with temporary credentials provided by Cognito
        Identity. You cannot call this API with developer credentials.
        """
        if _request is None:
            _params = {}
            if identity_pool_id is not ShapeBase.NOT_SET:
                _params['identity_pool_id'] = identity_pool_id
            if identity_id is not ShapeBase.NOT_SET:
                _params['identity_id'] = identity_id
            if dataset_name is not ShapeBase.NOT_SET:
                _params['dataset_name'] = dataset_name
            if device_id is not ShapeBase.NOT_SET:
                _params['device_id'] = device_id
            _request = shapes.SubscribeToDatasetRequest(**_params)
        response = self._boto_client.subscribe_to_dataset(**_request.to_boto())

        return shapes.SubscribeToDatasetResponse.from_boto(response)

    def unsubscribe_from_dataset(
        self,
        _request: shapes.UnsubscribeFromDatasetRequest = None,
        *,
        identity_pool_id: str,
        identity_id: str,
        dataset_name: str,
        device_id: str,
    ) -> shapes.UnsubscribeFromDatasetResponse:
        """
        Unsubscribes from receiving notifications when a dataset is modified by another
        device.

        This API can only be called with temporary credentials provided by Cognito
        Identity. You cannot call this API with developer credentials.
        """
        if _request is None:
            _params = {}
            if identity_pool_id is not ShapeBase.NOT_SET:
                _params['identity_pool_id'] = identity_pool_id
            if identity_id is not ShapeBase.NOT_SET:
                _params['identity_id'] = identity_id
            if dataset_name is not ShapeBase.NOT_SET:
                _params['dataset_name'] = dataset_name
            if device_id is not ShapeBase.NOT_SET:
                _params['device_id'] = device_id
            _request = shapes.UnsubscribeFromDatasetRequest(**_params)
        response = self._boto_client.unsubscribe_from_dataset(
            **_request.to_boto()
        )

        return shapes.UnsubscribeFromDatasetResponse.from_boto(response)

    def update_records(
        self,
        _request: shapes.UpdateRecordsRequest = None,
        *,
        identity_pool_id: str,
        identity_id: str,
        dataset_name: str,
        sync_session_token: str,
        device_id: str = ShapeBase.NOT_SET,
        record_patches: typing.List[shapes.RecordPatch] = ShapeBase.NOT_SET,
        client_context: str = ShapeBase.NOT_SET,
    ) -> shapes.UpdateRecordsResponse:
        """
        Posts updates to records and adds and deletes records for a dataset and user.

        The sync count in the record patch is your last known sync count for that
        record. The server will reject an UpdateRecords request with a
        ResourceConflictException if you try to patch a record with a new value but a
        stale sync count.

        For example, if the sync count on the server is 5 for a key called highScore and
        you try and submit a new highScore with sync count of 4, the request will be
        rejected. To obtain the current sync count for a record, call ListRecords. On a
        successful update of the record, the response returns the new sync count for
        that record. You should present that sync count the next time you try to update
        that same record. When the record does not exist, specify the sync count as 0.

        This API can be called with temporary user credentials provided by Cognito
        Identity or with developer credentials.
        """
        if _request is None:
            _params = {}
            if identity_pool_id is not ShapeBase.NOT_SET:
                _params['identity_pool_id'] = identity_pool_id
            if identity_id is not ShapeBase.NOT_SET:
                _params['identity_id'] = identity_id
            if dataset_name is not ShapeBase.NOT_SET:
                _params['dataset_name'] = dataset_name
            if sync_session_token is not ShapeBase.NOT_SET:
                _params['sync_session_token'] = sync_session_token
            if device_id is not ShapeBase.NOT_SET:
                _params['device_id'] = device_id
            if record_patches is not ShapeBase.NOT_SET:
                _params['record_patches'] = record_patches
            if client_context is not ShapeBase.NOT_SET:
                _params['client_context'] = client_context
            _request = shapes.UpdateRecordsRequest(**_params)
        response = self._boto_client.update_records(**_request.to_boto())

        return shapes.UpdateRecordsResponse.from_boto(response)
