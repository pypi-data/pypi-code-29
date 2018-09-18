import datetime
import typing
import boto3
from autoboto import ClientBase, ShapeBase, OutputShapeBase
from . import shapes


class Client(ClientBase):
    def __init__(self, *args, **kwargs):
        super().__init__("cloudtrail", *args, **kwargs)

    def add_tags(
        self,
        _request: shapes.AddTagsRequest = None,
        *,
        resource_id: str,
        tags_list: typing.List[shapes.Tag] = ShapeBase.NOT_SET,
    ) -> shapes.AddTagsResponse:
        """
        Adds one or more tags to a trail, up to a limit of 50. Tags must be unique per
        trail. Overwrites an existing tag's value when a new value is specified for an
        existing tag key. If you specify a key without a value, the tag will be created
        with the specified key and a value of null. You can tag a trail that applies to
        all regions only from the region in which the trail was created (that is, from
        its home region).
        """
        if _request is None:
            _params = {}
            if resource_id is not ShapeBase.NOT_SET:
                _params['resource_id'] = resource_id
            if tags_list is not ShapeBase.NOT_SET:
                _params['tags_list'] = tags_list
            _request = shapes.AddTagsRequest(**_params)
        response = self._boto_client.add_tags(**_request.to_boto())

        return shapes.AddTagsResponse.from_boto(response)

    def create_trail(
        self,
        _request: shapes.CreateTrailRequest = None,
        *,
        name: str,
        s3_bucket_name: str,
        s3_key_prefix: str = ShapeBase.NOT_SET,
        sns_topic_name: str = ShapeBase.NOT_SET,
        include_global_service_events: bool = ShapeBase.NOT_SET,
        is_multi_region_trail: bool = ShapeBase.NOT_SET,
        enable_log_file_validation: bool = ShapeBase.NOT_SET,
        cloud_watch_logs_log_group_arn: str = ShapeBase.NOT_SET,
        cloud_watch_logs_role_arn: str = ShapeBase.NOT_SET,
        kms_key_id: str = ShapeBase.NOT_SET,
    ) -> shapes.CreateTrailResponse:
        """
        Creates a trail that specifies the settings for delivery of log data to an
        Amazon S3 bucket. A maximum of five trails can exist in a region, irrespective
        of the region in which they were created.
        """
        if _request is None:
            _params = {}
            if name is not ShapeBase.NOT_SET:
                _params['name'] = name
            if s3_bucket_name is not ShapeBase.NOT_SET:
                _params['s3_bucket_name'] = s3_bucket_name
            if s3_key_prefix is not ShapeBase.NOT_SET:
                _params['s3_key_prefix'] = s3_key_prefix
            if sns_topic_name is not ShapeBase.NOT_SET:
                _params['sns_topic_name'] = sns_topic_name
            if include_global_service_events is not ShapeBase.NOT_SET:
                _params['include_global_service_events'
                       ] = include_global_service_events
            if is_multi_region_trail is not ShapeBase.NOT_SET:
                _params['is_multi_region_trail'] = is_multi_region_trail
            if enable_log_file_validation is not ShapeBase.NOT_SET:
                _params['enable_log_file_validation'
                       ] = enable_log_file_validation
            if cloud_watch_logs_log_group_arn is not ShapeBase.NOT_SET:
                _params['cloud_watch_logs_log_group_arn'
                       ] = cloud_watch_logs_log_group_arn
            if cloud_watch_logs_role_arn is not ShapeBase.NOT_SET:
                _params['cloud_watch_logs_role_arn'] = cloud_watch_logs_role_arn
            if kms_key_id is not ShapeBase.NOT_SET:
                _params['kms_key_id'] = kms_key_id
            _request = shapes.CreateTrailRequest(**_params)
        response = self._boto_client.create_trail(**_request.to_boto())

        return shapes.CreateTrailResponse.from_boto(response)

    def delete_trail(
        self,
        _request: shapes.DeleteTrailRequest = None,
        *,
        name: str,
    ) -> shapes.DeleteTrailResponse:
        """
        Deletes a trail. This operation must be called from the region in which the
        trail was created. `DeleteTrail` cannot be called on the shadow trails
        (replicated trails in other regions) of a trail that is enabled in all regions.
        """
        if _request is None:
            _params = {}
            if name is not ShapeBase.NOT_SET:
                _params['name'] = name
            _request = shapes.DeleteTrailRequest(**_params)
        response = self._boto_client.delete_trail(**_request.to_boto())

        return shapes.DeleteTrailResponse.from_boto(response)

    def describe_trails(
        self,
        _request: shapes.DescribeTrailsRequest = None,
        *,
        trail_name_list: typing.List[str] = ShapeBase.NOT_SET,
        include_shadow_trails: bool = ShapeBase.NOT_SET,
    ) -> shapes.DescribeTrailsResponse:
        """
        Retrieves settings for the trail associated with the current region for your
        account.
        """
        if _request is None:
            _params = {}
            if trail_name_list is not ShapeBase.NOT_SET:
                _params['trail_name_list'] = trail_name_list
            if include_shadow_trails is not ShapeBase.NOT_SET:
                _params['include_shadow_trails'] = include_shadow_trails
            _request = shapes.DescribeTrailsRequest(**_params)
        response = self._boto_client.describe_trails(**_request.to_boto())

        return shapes.DescribeTrailsResponse.from_boto(response)

    def get_event_selectors(
        self,
        _request: shapes.GetEventSelectorsRequest = None,
        *,
        trail_name: str,
    ) -> shapes.GetEventSelectorsResponse:
        """
        Describes the settings for the event selectors that you configured for your
        trail. The information returned for your event selectors includes the following:

          * The S3 objects that you are logging for data events.

          * If your event selector includes management events.

          * If your event selector includes read-only events, write-only events, or all. 

        For more information, see [Logging Data and Management Events for Trails
        ](http://docs.aws.amazon.com/awscloudtrail/latest/userguide/logging-management-
        and-data-events-with-cloudtrail.html) in the _AWS CloudTrail User Guide_.
        """
        if _request is None:
            _params = {}
            if trail_name is not ShapeBase.NOT_SET:
                _params['trail_name'] = trail_name
            _request = shapes.GetEventSelectorsRequest(**_params)
        response = self._boto_client.get_event_selectors(**_request.to_boto())

        return shapes.GetEventSelectorsResponse.from_boto(response)

    def get_trail_status(
        self,
        _request: shapes.GetTrailStatusRequest = None,
        *,
        name: str,
    ) -> shapes.GetTrailStatusResponse:
        """
        Returns a JSON-formatted list of information about the specified trail. Fields
        include information on delivery errors, Amazon SNS and Amazon S3 errors, and
        start and stop logging times for each trail. This operation returns trail status
        from a single region. To return trail status from all regions, you must call the
        operation on each region.
        """
        if _request is None:
            _params = {}
            if name is not ShapeBase.NOT_SET:
                _params['name'] = name
            _request = shapes.GetTrailStatusRequest(**_params)
        response = self._boto_client.get_trail_status(**_request.to_boto())

        return shapes.GetTrailStatusResponse.from_boto(response)

    def list_public_keys(
        self,
        _request: shapes.ListPublicKeysRequest = None,
        *,
        start_time: datetime.datetime = ShapeBase.NOT_SET,
        end_time: datetime.datetime = ShapeBase.NOT_SET,
        next_token: str = ShapeBase.NOT_SET,
    ) -> shapes.ListPublicKeysResponse:
        """
        Returns all public keys whose private keys were used to sign the digest files
        within the specified time range. The public key is needed to validate digest
        files that were signed with its corresponding private key.

        CloudTrail uses different private/public key pairs per region. Each digest file
        is signed with a private key unique to its region. Therefore, when you validate
        a digest file from a particular region, you must look in the same region for its
        corresponding public key.
        """
        if _request is None:
            _params = {}
            if start_time is not ShapeBase.NOT_SET:
                _params['start_time'] = start_time
            if end_time is not ShapeBase.NOT_SET:
                _params['end_time'] = end_time
            if next_token is not ShapeBase.NOT_SET:
                _params['next_token'] = next_token
            _request = shapes.ListPublicKeysRequest(**_params)
        response = self._boto_client.list_public_keys(**_request.to_boto())

        return shapes.ListPublicKeysResponse.from_boto(response)

    def list_tags(
        self,
        _request: shapes.ListTagsRequest = None,
        *,
        resource_id_list: typing.List[str],
        next_token: str = ShapeBase.NOT_SET,
    ) -> shapes.ListTagsResponse:
        """
        Lists the tags for the trail in the current region.
        """
        if _request is None:
            _params = {}
            if resource_id_list is not ShapeBase.NOT_SET:
                _params['resource_id_list'] = resource_id_list
            if next_token is not ShapeBase.NOT_SET:
                _params['next_token'] = next_token
            _request = shapes.ListTagsRequest(**_params)
        response = self._boto_client.list_tags(**_request.to_boto())

        return shapes.ListTagsResponse.from_boto(response)

    def lookup_events(
        self,
        _request: shapes.LookupEventsRequest = None,
        *,
        lookup_attributes: typing.List[shapes.LookupAttribute
                                      ] = ShapeBase.NOT_SET,
        start_time: datetime.datetime = ShapeBase.NOT_SET,
        end_time: datetime.datetime = ShapeBase.NOT_SET,
        max_results: int = ShapeBase.NOT_SET,
        next_token: str = ShapeBase.NOT_SET,
    ) -> shapes.LookupEventsResponse:
        """
        Looks up API activity events captured by CloudTrail that create, update, or
        delete resources in your account. Events for a region can be looked up for the
        times in which you had CloudTrail turned on in that region during the last seven
        days. Lookup supports the following attributes:

          * Event ID

          * Event name

          * Event source

          * Resource name

          * Resource type

          * User name

        All attributes are optional. The default number of results returned is 10, with
        a maximum of 50 possible. The response includes a token that you can use to get
        the next page of results.

        The rate of lookup requests is limited to one per second per account. If this
        limit is exceeded, a throttling error occurs.

        Events that occurred during the selected time range will not be available for
        lookup if CloudTrail logging was not enabled when the events occurred.
        """
        if _request is None:
            _params = {}
            if lookup_attributes is not ShapeBase.NOT_SET:
                _params['lookup_attributes'] = lookup_attributes
            if start_time is not ShapeBase.NOT_SET:
                _params['start_time'] = start_time
            if end_time is not ShapeBase.NOT_SET:
                _params['end_time'] = end_time
            if max_results is not ShapeBase.NOT_SET:
                _params['max_results'] = max_results
            if next_token is not ShapeBase.NOT_SET:
                _params['next_token'] = next_token
            _request = shapes.LookupEventsRequest(**_params)
        paginator = self.get_paginator("lookup_events").paginate(
            **_request.to_boto()
        )
        page_generator = (page for page in paginator)
        first_page = next(page_generator)
        result = shapes.LookupEventsResponse.from_boto(first_page)
        result._page_iterator = page_generator
        return result

        return shapes.LookupEventsResponse.from_boto(response)

    def put_event_selectors(
        self,
        _request: shapes.PutEventSelectorsRequest = None,
        *,
        trail_name: str,
        event_selectors: typing.List[shapes.EventSelector],
    ) -> shapes.PutEventSelectorsResponse:
        """
        Configures an event selector for your trail. Use event selectors to specify
        whether you want your trail to log management and/or data events. When an event
        occurs in your account, CloudTrail evaluates the event selectors in all trails.
        For each trail, if the event matches any event selector, the trail processes and
        logs the event. If the event doesn't match any event selector, the trail doesn't
        log the event.

        Example

          1. You create an event selector for a trail and specify that you want write-only events.

          2. The EC2 `GetConsoleOutput` and `RunInstances` API operations occur in your account.

          3. CloudTrail evaluates whether the events match your event selectors.

          4. The `RunInstances` is a write-only event and it matches your event selector. The trail logs the event.

          5. The `GetConsoleOutput` is a read-only event but it doesn't match your event selector. The trail doesn't log the event. 

        The `PutEventSelectors` operation must be called from the region in which the
        trail was created; otherwise, an `InvalidHomeRegionException` is thrown.

        You can configure up to five event selectors for each trail. For more
        information, see [Logging Data and Management Events for Trails
        ](http://docs.aws.amazon.com/awscloudtrail/latest/userguide/logging-management-
        and-data-events-with-cloudtrail.html) in the _AWS CloudTrail User Guide_.
        """
        if _request is None:
            _params = {}
            if trail_name is not ShapeBase.NOT_SET:
                _params['trail_name'] = trail_name
            if event_selectors is not ShapeBase.NOT_SET:
                _params['event_selectors'] = event_selectors
            _request = shapes.PutEventSelectorsRequest(**_params)
        response = self._boto_client.put_event_selectors(**_request.to_boto())

        return shapes.PutEventSelectorsResponse.from_boto(response)

    def remove_tags(
        self,
        _request: shapes.RemoveTagsRequest = None,
        *,
        resource_id: str,
        tags_list: typing.List[shapes.Tag] = ShapeBase.NOT_SET,
    ) -> shapes.RemoveTagsResponse:
        """
        Removes the specified tags from a trail.
        """
        if _request is None:
            _params = {}
            if resource_id is not ShapeBase.NOT_SET:
                _params['resource_id'] = resource_id
            if tags_list is not ShapeBase.NOT_SET:
                _params['tags_list'] = tags_list
            _request = shapes.RemoveTagsRequest(**_params)
        response = self._boto_client.remove_tags(**_request.to_boto())

        return shapes.RemoveTagsResponse.from_boto(response)

    def start_logging(
        self,
        _request: shapes.StartLoggingRequest = None,
        *,
        name: str,
    ) -> shapes.StartLoggingResponse:
        """
        Starts the recording of AWS API calls and log file delivery for a trail. For a
        trail that is enabled in all regions, this operation must be called from the
        region in which the trail was created. This operation cannot be called on the
        shadow trails (replicated trails in other regions) of a trail that is enabled in
        all regions.
        """
        if _request is None:
            _params = {}
            if name is not ShapeBase.NOT_SET:
                _params['name'] = name
            _request = shapes.StartLoggingRequest(**_params)
        response = self._boto_client.start_logging(**_request.to_boto())

        return shapes.StartLoggingResponse.from_boto(response)

    def stop_logging(
        self,
        _request: shapes.StopLoggingRequest = None,
        *,
        name: str,
    ) -> shapes.StopLoggingResponse:
        """
        Suspends the recording of AWS API calls and log file delivery for the specified
        trail. Under most circumstances, there is no need to use this action. You can
        update a trail without stopping it first. This action is the only way to stop
        recording. For a trail enabled in all regions, this operation must be called
        from the region in which the trail was created, or an
        `InvalidHomeRegionException` will occur. This operation cannot be called on the
        shadow trails (replicated trails in other regions) of a trail enabled in all
        regions.
        """
        if _request is None:
            _params = {}
            if name is not ShapeBase.NOT_SET:
                _params['name'] = name
            _request = shapes.StopLoggingRequest(**_params)
        response = self._boto_client.stop_logging(**_request.to_boto())

        return shapes.StopLoggingResponse.from_boto(response)

    def update_trail(
        self,
        _request: shapes.UpdateTrailRequest = None,
        *,
        name: str,
        s3_bucket_name: str = ShapeBase.NOT_SET,
        s3_key_prefix: str = ShapeBase.NOT_SET,
        sns_topic_name: str = ShapeBase.NOT_SET,
        include_global_service_events: bool = ShapeBase.NOT_SET,
        is_multi_region_trail: bool = ShapeBase.NOT_SET,
        enable_log_file_validation: bool = ShapeBase.NOT_SET,
        cloud_watch_logs_log_group_arn: str = ShapeBase.NOT_SET,
        cloud_watch_logs_role_arn: str = ShapeBase.NOT_SET,
        kms_key_id: str = ShapeBase.NOT_SET,
    ) -> shapes.UpdateTrailResponse:
        """
        Updates the settings that specify delivery of log files. Changes to a trail do
        not require stopping the CloudTrail service. Use this action to designate an
        existing bucket for log delivery. If the existing bucket has previously been a
        target for CloudTrail log files, an IAM policy exists for the bucket.
        `UpdateTrail` must be called from the region in which the trail was created;
        otherwise, an `InvalidHomeRegionException` is thrown.
        """
        if _request is None:
            _params = {}
            if name is not ShapeBase.NOT_SET:
                _params['name'] = name
            if s3_bucket_name is not ShapeBase.NOT_SET:
                _params['s3_bucket_name'] = s3_bucket_name
            if s3_key_prefix is not ShapeBase.NOT_SET:
                _params['s3_key_prefix'] = s3_key_prefix
            if sns_topic_name is not ShapeBase.NOT_SET:
                _params['sns_topic_name'] = sns_topic_name
            if include_global_service_events is not ShapeBase.NOT_SET:
                _params['include_global_service_events'
                       ] = include_global_service_events
            if is_multi_region_trail is not ShapeBase.NOT_SET:
                _params['is_multi_region_trail'] = is_multi_region_trail
            if enable_log_file_validation is not ShapeBase.NOT_SET:
                _params['enable_log_file_validation'
                       ] = enable_log_file_validation
            if cloud_watch_logs_log_group_arn is not ShapeBase.NOT_SET:
                _params['cloud_watch_logs_log_group_arn'
                       ] = cloud_watch_logs_log_group_arn
            if cloud_watch_logs_role_arn is not ShapeBase.NOT_SET:
                _params['cloud_watch_logs_role_arn'] = cloud_watch_logs_role_arn
            if kms_key_id is not ShapeBase.NOT_SET:
                _params['kms_key_id'] = kms_key_id
            _request = shapes.UpdateTrailRequest(**_params)
        response = self._boto_client.update_trail(**_request.to_boto())

        return shapes.UpdateTrailResponse.from_boto(response)
