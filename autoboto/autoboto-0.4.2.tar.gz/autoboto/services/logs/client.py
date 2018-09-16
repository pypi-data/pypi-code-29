import datetime
import typing
import boto3
from autoboto import ClientBase, ShapeBase, OutputShapeBase
from . import shapes


class Client(ClientBase):
    def __init__(self, *args, **kwargs):
        super().__init__("logs", *args, **kwargs)

    def associate_kms_key(
        self,
        _request: shapes.AssociateKmsKeyRequest = None,
        *,
        log_group_name: str,
        kms_key_id: str,
    ) -> None:
        """
        Associates the specified AWS Key Management Service (AWS KMS) customer master
        key (CMK) with the specified log group.

        Associating an AWS KMS CMK with a log group overrides any existing associations
        between the log group and a CMK. After a CMK is associated with a log group, all
        newly ingested data for the log group is encrypted using the CMK. This
        association is stored as long as the data encrypted with the CMK is still within
        Amazon CloudWatch Logs. This enables Amazon CloudWatch Logs to decrypt this data
        whenever it is requested.

        Note that it can take up to 5 minutes for this operation to take effect.

        If you attempt to associate a CMK with a log group but the CMK does not exist or
        the CMK is disabled, you will receive an `InvalidParameterException` error.
        """
        if _request is None:
            _params = {}
            if log_group_name is not ShapeBase.NOT_SET:
                _params['log_group_name'] = log_group_name
            if kms_key_id is not ShapeBase.NOT_SET:
                _params['kms_key_id'] = kms_key_id
            _request = shapes.AssociateKmsKeyRequest(**_params)
        response = self._boto_client.associate_kms_key(**_request.to_boto())

    def cancel_export_task(
        self,
        _request: shapes.CancelExportTaskRequest = None,
        *,
        task_id: str,
    ) -> None:
        """
        Cancels the specified export task.

        The task must be in the `PENDING` or `RUNNING` state.
        """
        if _request is None:
            _params = {}
            if task_id is not ShapeBase.NOT_SET:
                _params['task_id'] = task_id
            _request = shapes.CancelExportTaskRequest(**_params)
        response = self._boto_client.cancel_export_task(**_request.to_boto())

    def create_export_task(
        self,
        _request: shapes.CreateExportTaskRequest = None,
        *,
        log_group_name: str,
        from_: int,
        to: int,
        destination: str,
        task_name: str = ShapeBase.NOT_SET,
        log_stream_name_prefix: str = ShapeBase.NOT_SET,
        destination_prefix: str = ShapeBase.NOT_SET,
    ) -> shapes.CreateExportTaskResponse:
        """
        Creates an export task, which allows you to efficiently export data from a log
        group to an Amazon S3 bucket.

        This is an asynchronous call. If all the required information is provided, this
        operation initiates an export task and responds with the ID of the task. After
        the task has started, you can use DescribeExportTasks to get the status of the
        export task. Each account can only have one active (`RUNNING` or `PENDING`)
        export task at a time. To cancel an export task, use CancelExportTask.

        You can export logs from multiple log groups or multiple time ranges to the same
        S3 bucket. To separate out log data for each export task, you can specify a
        prefix to be used as the Amazon S3 key prefix for all exported objects.
        """
        if _request is None:
            _params = {}
            if log_group_name is not ShapeBase.NOT_SET:
                _params['log_group_name'] = log_group_name
            if from_ is not ShapeBase.NOT_SET:
                _params['from_'] = from_
            if to is not ShapeBase.NOT_SET:
                _params['to'] = to
            if destination is not ShapeBase.NOT_SET:
                _params['destination'] = destination
            if task_name is not ShapeBase.NOT_SET:
                _params['task_name'] = task_name
            if log_stream_name_prefix is not ShapeBase.NOT_SET:
                _params['log_stream_name_prefix'] = log_stream_name_prefix
            if destination_prefix is not ShapeBase.NOT_SET:
                _params['destination_prefix'] = destination_prefix
            _request = shapes.CreateExportTaskRequest(**_params)
        response = self._boto_client.create_export_task(**_request.to_boto())

        return shapes.CreateExportTaskResponse.from_boto(response)

    def create_log_group(
        self,
        _request: shapes.CreateLogGroupRequest = None,
        *,
        log_group_name: str,
        kms_key_id: str = ShapeBase.NOT_SET,
        tags: typing.Dict[str, str] = ShapeBase.NOT_SET,
    ) -> None:
        """
        Creates a log group with the specified name.

        You can create up to 5000 log groups per account.

        You must use the following guidelines when naming a log group:

          * Log group names must be unique within a region for an AWS account.

          * Log group names can be between 1 and 512 characters long.

          * Log group names consist of the following characters: a-z, A-Z, 0-9, '_' (underscore), '-' (hyphen), '/' (forward slash), and '.' (period).

        If you associate a AWS Key Management Service (AWS KMS) customer master key
        (CMK) with the log group, ingested data is encrypted using the CMK. This
        association is stored as long as the data encrypted with the CMK is still within
        Amazon CloudWatch Logs. This enables Amazon CloudWatch Logs to decrypt this data
        whenever it is requested.

        If you attempt to associate a CMK with the log group but the CMK does not exist
        or the CMK is disabled, you will receive an `InvalidParameterException` error.
        """
        if _request is None:
            _params = {}
            if log_group_name is not ShapeBase.NOT_SET:
                _params['log_group_name'] = log_group_name
            if kms_key_id is not ShapeBase.NOT_SET:
                _params['kms_key_id'] = kms_key_id
            if tags is not ShapeBase.NOT_SET:
                _params['tags'] = tags
            _request = shapes.CreateLogGroupRequest(**_params)
        response = self._boto_client.create_log_group(**_request.to_boto())

    def create_log_stream(
        self,
        _request: shapes.CreateLogStreamRequest = None,
        *,
        log_group_name: str,
        log_stream_name: str,
    ) -> None:
        """
        Creates a log stream for the specified log group.

        There is no limit on the number of log streams that you can create for a log
        group.

        You must use the following guidelines when naming a log stream:

          * Log stream names must be unique within the log group.

          * Log stream names can be between 1 and 512 characters long.

          * The ':' (colon) and '*' (asterisk) characters are not allowed.
        """
        if _request is None:
            _params = {}
            if log_group_name is not ShapeBase.NOT_SET:
                _params['log_group_name'] = log_group_name
            if log_stream_name is not ShapeBase.NOT_SET:
                _params['log_stream_name'] = log_stream_name
            _request = shapes.CreateLogStreamRequest(**_params)
        response = self._boto_client.create_log_stream(**_request.to_boto())

    def delete_destination(
        self,
        _request: shapes.DeleteDestinationRequest = None,
        *,
        destination_name: str,
    ) -> None:
        """
        Deletes the specified destination, and eventually disables all the subscription
        filters that publish to it. This operation does not delete the physical resource
        encapsulated by the destination.
        """
        if _request is None:
            _params = {}
            if destination_name is not ShapeBase.NOT_SET:
                _params['destination_name'] = destination_name
            _request = shapes.DeleteDestinationRequest(**_params)
        response = self._boto_client.delete_destination(**_request.to_boto())

    def delete_log_group(
        self,
        _request: shapes.DeleteLogGroupRequest = None,
        *,
        log_group_name: str,
    ) -> None:
        """
        Deletes the specified log group and permanently deletes all the archived log
        events associated with the log group.
        """
        if _request is None:
            _params = {}
            if log_group_name is not ShapeBase.NOT_SET:
                _params['log_group_name'] = log_group_name
            _request = shapes.DeleteLogGroupRequest(**_params)
        response = self._boto_client.delete_log_group(**_request.to_boto())

    def delete_log_stream(
        self,
        _request: shapes.DeleteLogStreamRequest = None,
        *,
        log_group_name: str,
        log_stream_name: str,
    ) -> None:
        """
        Deletes the specified log stream and permanently deletes all the archived log
        events associated with the log stream.
        """
        if _request is None:
            _params = {}
            if log_group_name is not ShapeBase.NOT_SET:
                _params['log_group_name'] = log_group_name
            if log_stream_name is not ShapeBase.NOT_SET:
                _params['log_stream_name'] = log_stream_name
            _request = shapes.DeleteLogStreamRequest(**_params)
        response = self._boto_client.delete_log_stream(**_request.to_boto())

    def delete_metric_filter(
        self,
        _request: shapes.DeleteMetricFilterRequest = None,
        *,
        log_group_name: str,
        filter_name: str,
    ) -> None:
        """
        Deletes the specified metric filter.
        """
        if _request is None:
            _params = {}
            if log_group_name is not ShapeBase.NOT_SET:
                _params['log_group_name'] = log_group_name
            if filter_name is not ShapeBase.NOT_SET:
                _params['filter_name'] = filter_name
            _request = shapes.DeleteMetricFilterRequest(**_params)
        response = self._boto_client.delete_metric_filter(**_request.to_boto())

    def delete_resource_policy(
        self,
        _request: shapes.DeleteResourcePolicyRequest = None,
        *,
        policy_name: str = ShapeBase.NOT_SET,
    ) -> None:
        """
        Deletes a resource policy from this account. This revokes the access of the
        identities in that policy to put log events to this account.
        """
        if _request is None:
            _params = {}
            if policy_name is not ShapeBase.NOT_SET:
                _params['policy_name'] = policy_name
            _request = shapes.DeleteResourcePolicyRequest(**_params)
        response = self._boto_client.delete_resource_policy(
            **_request.to_boto()
        )

    def delete_retention_policy(
        self,
        _request: shapes.DeleteRetentionPolicyRequest = None,
        *,
        log_group_name: str,
    ) -> None:
        """
        Deletes the specified retention policy.

        Log events do not expire if they belong to log groups without a retention
        policy.
        """
        if _request is None:
            _params = {}
            if log_group_name is not ShapeBase.NOT_SET:
                _params['log_group_name'] = log_group_name
            _request = shapes.DeleteRetentionPolicyRequest(**_params)
        response = self._boto_client.delete_retention_policy(
            **_request.to_boto()
        )

    def delete_subscription_filter(
        self,
        _request: shapes.DeleteSubscriptionFilterRequest = None,
        *,
        log_group_name: str,
        filter_name: str,
    ) -> None:
        """
        Deletes the specified subscription filter.
        """
        if _request is None:
            _params = {}
            if log_group_name is not ShapeBase.NOT_SET:
                _params['log_group_name'] = log_group_name
            if filter_name is not ShapeBase.NOT_SET:
                _params['filter_name'] = filter_name
            _request = shapes.DeleteSubscriptionFilterRequest(**_params)
        response = self._boto_client.delete_subscription_filter(
            **_request.to_boto()
        )

    def describe_destinations(
        self,
        _request: shapes.DescribeDestinationsRequest = None,
        *,
        destination_name_prefix: str = ShapeBase.NOT_SET,
        next_token: str = ShapeBase.NOT_SET,
        limit: int = ShapeBase.NOT_SET,
    ) -> shapes.DescribeDestinationsResponse:
        """
        Lists all your destinations. The results are ASCII-sorted by destination name.
        """
        if _request is None:
            _params = {}
            if destination_name_prefix is not ShapeBase.NOT_SET:
                _params['destination_name_prefix'] = destination_name_prefix
            if next_token is not ShapeBase.NOT_SET:
                _params['next_token'] = next_token
            if limit is not ShapeBase.NOT_SET:
                _params['limit'] = limit
            _request = shapes.DescribeDestinationsRequest(**_params)
        paginator = self.get_paginator("describe_destinations").paginate(
            **_request.to_boto()
        )
        page_generator = (page for page in paginator)
        first_page = next(page_generator)
        result = shapes.DescribeDestinationsResponse.from_boto(first_page)
        result._page_iterator = page_generator
        return result

        return shapes.DescribeDestinationsResponse.from_boto(response)

    def describe_export_tasks(
        self,
        _request: shapes.DescribeExportTasksRequest = None,
        *,
        task_id: str = ShapeBase.NOT_SET,
        status_code: typing.Union[str, shapes.ExportTaskStatusCode] = ShapeBase.
        NOT_SET,
        next_token: str = ShapeBase.NOT_SET,
        limit: int = ShapeBase.NOT_SET,
    ) -> shapes.DescribeExportTasksResponse:
        """
        Lists the specified export tasks. You can list all your export tasks or filter
        the results based on task ID or task status.
        """
        if _request is None:
            _params = {}
            if task_id is not ShapeBase.NOT_SET:
                _params['task_id'] = task_id
            if status_code is not ShapeBase.NOT_SET:
                _params['status_code'] = status_code
            if next_token is not ShapeBase.NOT_SET:
                _params['next_token'] = next_token
            if limit is not ShapeBase.NOT_SET:
                _params['limit'] = limit
            _request = shapes.DescribeExportTasksRequest(**_params)
        response = self._boto_client.describe_export_tasks(**_request.to_boto())

        return shapes.DescribeExportTasksResponse.from_boto(response)

    def describe_log_groups(
        self,
        _request: shapes.DescribeLogGroupsRequest = None,
        *,
        log_group_name_prefix: str = ShapeBase.NOT_SET,
        next_token: str = ShapeBase.NOT_SET,
        limit: int = ShapeBase.NOT_SET,
    ) -> shapes.DescribeLogGroupsResponse:
        """
        Lists the specified log groups. You can list all your log groups or filter the
        results by prefix. The results are ASCII-sorted by log group name.
        """
        if _request is None:
            _params = {}
            if log_group_name_prefix is not ShapeBase.NOT_SET:
                _params['log_group_name_prefix'] = log_group_name_prefix
            if next_token is not ShapeBase.NOT_SET:
                _params['next_token'] = next_token
            if limit is not ShapeBase.NOT_SET:
                _params['limit'] = limit
            _request = shapes.DescribeLogGroupsRequest(**_params)
        paginator = self.get_paginator("describe_log_groups").paginate(
            **_request.to_boto()
        )
        page_generator = (page for page in paginator)
        first_page = next(page_generator)
        result = shapes.DescribeLogGroupsResponse.from_boto(first_page)
        result._page_iterator = page_generator
        return result

        return shapes.DescribeLogGroupsResponse.from_boto(response)

    def describe_log_streams(
        self,
        _request: shapes.DescribeLogStreamsRequest = None,
        *,
        log_group_name: str,
        log_stream_name_prefix: str = ShapeBase.NOT_SET,
        order_by: typing.Union[str, shapes.OrderBy] = ShapeBase.NOT_SET,
        descending: bool = ShapeBase.NOT_SET,
        next_token: str = ShapeBase.NOT_SET,
        limit: int = ShapeBase.NOT_SET,
    ) -> shapes.DescribeLogStreamsResponse:
        """
        Lists the log streams for the specified log group. You can list all the log
        streams or filter the results by prefix. You can also control how the results
        are ordered.

        This operation has a limit of five transactions per second, after which
        transactions are throttled.
        """
        if _request is None:
            _params = {}
            if log_group_name is not ShapeBase.NOT_SET:
                _params['log_group_name'] = log_group_name
            if log_stream_name_prefix is not ShapeBase.NOT_SET:
                _params['log_stream_name_prefix'] = log_stream_name_prefix
            if order_by is not ShapeBase.NOT_SET:
                _params['order_by'] = order_by
            if descending is not ShapeBase.NOT_SET:
                _params['descending'] = descending
            if next_token is not ShapeBase.NOT_SET:
                _params['next_token'] = next_token
            if limit is not ShapeBase.NOT_SET:
                _params['limit'] = limit
            _request = shapes.DescribeLogStreamsRequest(**_params)
        paginator = self.get_paginator("describe_log_streams").paginate(
            **_request.to_boto()
        )
        page_generator = (page for page in paginator)
        first_page = next(page_generator)
        result = shapes.DescribeLogStreamsResponse.from_boto(first_page)
        result._page_iterator = page_generator
        return result

        return shapes.DescribeLogStreamsResponse.from_boto(response)

    def describe_metric_filters(
        self,
        _request: shapes.DescribeMetricFiltersRequest = None,
        *,
        log_group_name: str = ShapeBase.NOT_SET,
        filter_name_prefix: str = ShapeBase.NOT_SET,
        next_token: str = ShapeBase.NOT_SET,
        limit: int = ShapeBase.NOT_SET,
        metric_name: str = ShapeBase.NOT_SET,
        metric_namespace: str = ShapeBase.NOT_SET,
    ) -> shapes.DescribeMetricFiltersResponse:
        """
        Lists the specified metric filters. You can list all the metric filters or
        filter the results by log name, prefix, metric name, or metric namespace. The
        results are ASCII-sorted by filter name.
        """
        if _request is None:
            _params = {}
            if log_group_name is not ShapeBase.NOT_SET:
                _params['log_group_name'] = log_group_name
            if filter_name_prefix is not ShapeBase.NOT_SET:
                _params['filter_name_prefix'] = filter_name_prefix
            if next_token is not ShapeBase.NOT_SET:
                _params['next_token'] = next_token
            if limit is not ShapeBase.NOT_SET:
                _params['limit'] = limit
            if metric_name is not ShapeBase.NOT_SET:
                _params['metric_name'] = metric_name
            if metric_namespace is not ShapeBase.NOT_SET:
                _params['metric_namespace'] = metric_namespace
            _request = shapes.DescribeMetricFiltersRequest(**_params)
        paginator = self.get_paginator("describe_metric_filters").paginate(
            **_request.to_boto()
        )
        page_generator = (page for page in paginator)
        first_page = next(page_generator)
        result = shapes.DescribeMetricFiltersResponse.from_boto(first_page)
        result._page_iterator = page_generator
        return result

        return shapes.DescribeMetricFiltersResponse.from_boto(response)

    def describe_resource_policies(
        self,
        _request: shapes.DescribeResourcePoliciesRequest = None,
        *,
        next_token: str = ShapeBase.NOT_SET,
        limit: int = ShapeBase.NOT_SET,
    ) -> shapes.DescribeResourcePoliciesResponse:
        """
        Lists the resource policies in this account.
        """
        if _request is None:
            _params = {}
            if next_token is not ShapeBase.NOT_SET:
                _params['next_token'] = next_token
            if limit is not ShapeBase.NOT_SET:
                _params['limit'] = limit
            _request = shapes.DescribeResourcePoliciesRequest(**_params)
        response = self._boto_client.describe_resource_policies(
            **_request.to_boto()
        )

        return shapes.DescribeResourcePoliciesResponse.from_boto(response)

    def describe_subscription_filters(
        self,
        _request: shapes.DescribeSubscriptionFiltersRequest = None,
        *,
        log_group_name: str,
        filter_name_prefix: str = ShapeBase.NOT_SET,
        next_token: str = ShapeBase.NOT_SET,
        limit: int = ShapeBase.NOT_SET,
    ) -> shapes.DescribeSubscriptionFiltersResponse:
        """
        Lists the subscription filters for the specified log group. You can list all the
        subscription filters or filter the results by prefix. The results are ASCII-
        sorted by filter name.
        """
        if _request is None:
            _params = {}
            if log_group_name is not ShapeBase.NOT_SET:
                _params['log_group_name'] = log_group_name
            if filter_name_prefix is not ShapeBase.NOT_SET:
                _params['filter_name_prefix'] = filter_name_prefix
            if next_token is not ShapeBase.NOT_SET:
                _params['next_token'] = next_token
            if limit is not ShapeBase.NOT_SET:
                _params['limit'] = limit
            _request = shapes.DescribeSubscriptionFiltersRequest(**_params)
        paginator = self.get_paginator("describe_subscription_filters"
                                      ).paginate(**_request.to_boto())
        page_generator = (page for page in paginator)
        first_page = next(page_generator)
        result = shapes.DescribeSubscriptionFiltersResponse.from_boto(
            first_page
        )
        result._page_iterator = page_generator
        return result

        return shapes.DescribeSubscriptionFiltersResponse.from_boto(response)

    def disassociate_kms_key(
        self,
        _request: shapes.DisassociateKmsKeyRequest = None,
        *,
        log_group_name: str,
    ) -> None:
        """
        Disassociates the associated AWS Key Management Service (AWS KMS) customer
        master key (CMK) from the specified log group.

        After the AWS KMS CMK is disassociated from the log group, AWS CloudWatch Logs
        stops encrypting newly ingested data for the log group. All previously ingested
        data remains encrypted, and AWS CloudWatch Logs requires permissions for the CMK
        whenever the encrypted data is requested.

        Note that it can take up to 5 minutes for this operation to take effect.
        """
        if _request is None:
            _params = {}
            if log_group_name is not ShapeBase.NOT_SET:
                _params['log_group_name'] = log_group_name
            _request = shapes.DisassociateKmsKeyRequest(**_params)
        response = self._boto_client.disassociate_kms_key(**_request.to_boto())

    def filter_log_events(
        self,
        _request: shapes.FilterLogEventsRequest = None,
        *,
        log_group_name: str,
        log_stream_names: typing.List[str] = ShapeBase.NOT_SET,
        log_stream_name_prefix: str = ShapeBase.NOT_SET,
        start_time: int = ShapeBase.NOT_SET,
        end_time: int = ShapeBase.NOT_SET,
        filter_pattern: str = ShapeBase.NOT_SET,
        next_token: str = ShapeBase.NOT_SET,
        limit: int = ShapeBase.NOT_SET,
        interleaved: bool = ShapeBase.NOT_SET,
    ) -> shapes.FilterLogEventsResponse:
        """
        Lists log events from the specified log group. You can list all the log events
        or filter the results using a filter pattern, a time range, and the name of the
        log stream.

        By default, this operation returns as many log events as can fit in 1 MB (up to
        10,000 log events), or all the events found within the time range that you
        specify. If the results include a token, then there are more log events
        available, and you can get additional results by specifying the token in a
        subsequent call.
        """
        if _request is None:
            _params = {}
            if log_group_name is not ShapeBase.NOT_SET:
                _params['log_group_name'] = log_group_name
            if log_stream_names is not ShapeBase.NOT_SET:
                _params['log_stream_names'] = log_stream_names
            if log_stream_name_prefix is not ShapeBase.NOT_SET:
                _params['log_stream_name_prefix'] = log_stream_name_prefix
            if start_time is not ShapeBase.NOT_SET:
                _params['start_time'] = start_time
            if end_time is not ShapeBase.NOT_SET:
                _params['end_time'] = end_time
            if filter_pattern is not ShapeBase.NOT_SET:
                _params['filter_pattern'] = filter_pattern
            if next_token is not ShapeBase.NOT_SET:
                _params['next_token'] = next_token
            if limit is not ShapeBase.NOT_SET:
                _params['limit'] = limit
            if interleaved is not ShapeBase.NOT_SET:
                _params['interleaved'] = interleaved
            _request = shapes.FilterLogEventsRequest(**_params)
        paginator = self.get_paginator("filter_log_events").paginate(
            **_request.to_boto()
        )
        page_generator = (page for page in paginator)
        first_page = next(page_generator)
        result = shapes.FilterLogEventsResponse.from_boto(first_page)
        result._page_iterator = page_generator
        return result

        return shapes.FilterLogEventsResponse.from_boto(response)

    def get_log_events(
        self,
        _request: shapes.GetLogEventsRequest = None,
        *,
        log_group_name: str,
        log_stream_name: str,
        start_time: int = ShapeBase.NOT_SET,
        end_time: int = ShapeBase.NOT_SET,
        next_token: str = ShapeBase.NOT_SET,
        limit: int = ShapeBase.NOT_SET,
        start_from_head: bool = ShapeBase.NOT_SET,
    ) -> shapes.GetLogEventsResponse:
        """
        Lists log events from the specified log stream. You can list all the log events
        or filter using a time range.

        By default, this operation returns as many log events as can fit in a response
        size of 1MB (up to 10,000 log events). You can get additional log events by
        specifying one of the tokens in a subsequent call.
        """
        if _request is None:
            _params = {}
            if log_group_name is not ShapeBase.NOT_SET:
                _params['log_group_name'] = log_group_name
            if log_stream_name is not ShapeBase.NOT_SET:
                _params['log_stream_name'] = log_stream_name
            if start_time is not ShapeBase.NOT_SET:
                _params['start_time'] = start_time
            if end_time is not ShapeBase.NOT_SET:
                _params['end_time'] = end_time
            if next_token is not ShapeBase.NOT_SET:
                _params['next_token'] = next_token
            if limit is not ShapeBase.NOT_SET:
                _params['limit'] = limit
            if start_from_head is not ShapeBase.NOT_SET:
                _params['start_from_head'] = start_from_head
            _request = shapes.GetLogEventsRequest(**_params)
        response = self._boto_client.get_log_events(**_request.to_boto())

        return shapes.GetLogEventsResponse.from_boto(response)

    def list_tags_log_group(
        self,
        _request: shapes.ListTagsLogGroupRequest = None,
        *,
        log_group_name: str,
    ) -> shapes.ListTagsLogGroupResponse:
        """
        Lists the tags for the specified log group.
        """
        if _request is None:
            _params = {}
            if log_group_name is not ShapeBase.NOT_SET:
                _params['log_group_name'] = log_group_name
            _request = shapes.ListTagsLogGroupRequest(**_params)
        response = self._boto_client.list_tags_log_group(**_request.to_boto())

        return shapes.ListTagsLogGroupResponse.from_boto(response)

    def put_destination(
        self,
        _request: shapes.PutDestinationRequest = None,
        *,
        destination_name: str,
        target_arn: str,
        role_arn: str,
    ) -> shapes.PutDestinationResponse:
        """
        Creates or updates a destination. A destination encapsulates a physical resource
        (such as an Amazon Kinesis stream) and enables you to subscribe to a real-time
        stream of log events for a different account, ingested using PutLogEvents.
        Currently, the only supported physical resource is a Kinesis stream belonging to
        the same account as the destination.

        Through an access policy, a destination controls what is written to its Kinesis
        stream. By default, `PutDestination` does not set any access policy with the
        destination, which means a cross-account user cannot call PutSubscriptionFilter
        against this destination. To enable this, the destination owner must call
        PutDestinationPolicy after `PutDestination`.
        """
        if _request is None:
            _params = {}
            if destination_name is not ShapeBase.NOT_SET:
                _params['destination_name'] = destination_name
            if target_arn is not ShapeBase.NOT_SET:
                _params['target_arn'] = target_arn
            if role_arn is not ShapeBase.NOT_SET:
                _params['role_arn'] = role_arn
            _request = shapes.PutDestinationRequest(**_params)
        response = self._boto_client.put_destination(**_request.to_boto())

        return shapes.PutDestinationResponse.from_boto(response)

    def put_destination_policy(
        self,
        _request: shapes.PutDestinationPolicyRequest = None,
        *,
        destination_name: str,
        access_policy: str,
    ) -> None:
        """
        Creates or updates an access policy associated with an existing destination. An
        access policy is an [IAM policy
        document](http://docs.aws.amazon.com/IAM/latest/UserGuide/policies_overview.html)
        that is used to authorize claims to register a subscription filter against a
        given destination.
        """
        if _request is None:
            _params = {}
            if destination_name is not ShapeBase.NOT_SET:
                _params['destination_name'] = destination_name
            if access_policy is not ShapeBase.NOT_SET:
                _params['access_policy'] = access_policy
            _request = shapes.PutDestinationPolicyRequest(**_params)
        response = self._boto_client.put_destination_policy(
            **_request.to_boto()
        )

    def put_log_events(
        self,
        _request: shapes.PutLogEventsRequest = None,
        *,
        log_group_name: str,
        log_stream_name: str,
        log_events: typing.List[shapes.InputLogEvent],
        sequence_token: str = ShapeBase.NOT_SET,
    ) -> shapes.PutLogEventsResponse:
        """
        Uploads a batch of log events to the specified log stream.

        You must include the sequence token obtained from the response of the previous
        call. An upload in a newly created log stream does not require a sequence token.
        You can also get the sequence token using DescribeLogStreams. If you call
        `PutLogEvents` twice within a narrow time period using the same value for
        `sequenceToken`, both calls may be successful, or one may be rejected.

        The batch of events must satisfy the following constraints:

          * The maximum batch size is 1,048,576 bytes, and this size is calculated as the sum of all event messages in UTF-8, plus 26 bytes for each log event.

          * None of the log events in the batch can be more than 2 hours in the future.

          * None of the log events in the batch can be older than 14 days or the retention period of the log group.

          * The log events in the batch must be in chronological ordered by their time stamp. The time stamp is the time the event occurred, expressed as the number of milliseconds after Jan 1, 1970 00:00:00 UTC. (In AWS Tools for PowerShell and the AWS SDK for .NET, the timestamp is specified in .NET format: yyyy-mm-ddThh:mm:ss. For example, 2017-09-15T13:45:30.) 

          * The maximum number of log events in a batch is 10,000.

          * A batch of log events in a single request cannot span more than 24 hours. Otherwise, the operation fails.

        If a call to PutLogEvents returns "UnrecognizedClientException" the most likely
        cause is an invalid AWS access key ID or secret key.
        """
        if _request is None:
            _params = {}
            if log_group_name is not ShapeBase.NOT_SET:
                _params['log_group_name'] = log_group_name
            if log_stream_name is not ShapeBase.NOT_SET:
                _params['log_stream_name'] = log_stream_name
            if log_events is not ShapeBase.NOT_SET:
                _params['log_events'] = log_events
            if sequence_token is not ShapeBase.NOT_SET:
                _params['sequence_token'] = sequence_token
            _request = shapes.PutLogEventsRequest(**_params)
        response = self._boto_client.put_log_events(**_request.to_boto())

        return shapes.PutLogEventsResponse.from_boto(response)

    def put_metric_filter(
        self,
        _request: shapes.PutMetricFilterRequest = None,
        *,
        log_group_name: str,
        filter_name: str,
        filter_pattern: str,
        metric_transformations: typing.List[shapes.MetricTransformation],
    ) -> None:
        """
        Creates or updates a metric filter and associates it with the specified log
        group. Metric filters allow you to configure rules to extract metric data from
        log events ingested through PutLogEvents.

        The maximum number of metric filters that can be associated with a log group is
        100.
        """
        if _request is None:
            _params = {}
            if log_group_name is not ShapeBase.NOT_SET:
                _params['log_group_name'] = log_group_name
            if filter_name is not ShapeBase.NOT_SET:
                _params['filter_name'] = filter_name
            if filter_pattern is not ShapeBase.NOT_SET:
                _params['filter_pattern'] = filter_pattern
            if metric_transformations is not ShapeBase.NOT_SET:
                _params['metric_transformations'] = metric_transformations
            _request = shapes.PutMetricFilterRequest(**_params)
        response = self._boto_client.put_metric_filter(**_request.to_boto())

    def put_resource_policy(
        self,
        _request: shapes.PutResourcePolicyRequest = None,
        *,
        policy_name: str = ShapeBase.NOT_SET,
        policy_document: str = ShapeBase.NOT_SET,
    ) -> shapes.PutResourcePolicyResponse:
        """
        Creates or updates a resource policy allowing other AWS services to put log
        events to this account, such as Amazon Route 53. An account can have up to 10
        resource policies per region.
        """
        if _request is None:
            _params = {}
            if policy_name is not ShapeBase.NOT_SET:
                _params['policy_name'] = policy_name
            if policy_document is not ShapeBase.NOT_SET:
                _params['policy_document'] = policy_document
            _request = shapes.PutResourcePolicyRequest(**_params)
        response = self._boto_client.put_resource_policy(**_request.to_boto())

        return shapes.PutResourcePolicyResponse.from_boto(response)

    def put_retention_policy(
        self,
        _request: shapes.PutRetentionPolicyRequest = None,
        *,
        log_group_name: str,
        retention_in_days: int,
    ) -> None:
        """
        Sets the retention of the specified log group. A retention policy allows you to
        configure the number of days for which to retain log events in the specified log
        group.
        """
        if _request is None:
            _params = {}
            if log_group_name is not ShapeBase.NOT_SET:
                _params['log_group_name'] = log_group_name
            if retention_in_days is not ShapeBase.NOT_SET:
                _params['retention_in_days'] = retention_in_days
            _request = shapes.PutRetentionPolicyRequest(**_params)
        response = self._boto_client.put_retention_policy(**_request.to_boto())

    def put_subscription_filter(
        self,
        _request: shapes.PutSubscriptionFilterRequest = None,
        *,
        log_group_name: str,
        filter_name: str,
        filter_pattern: str,
        destination_arn: str,
        role_arn: str = ShapeBase.NOT_SET,
        distribution: typing.Union[str, shapes.Distribution] = ShapeBase.
        NOT_SET,
    ) -> None:
        """
        Creates or updates a subscription filter and associates it with the specified
        log group. Subscription filters allow you to subscribe to a real-time stream of
        log events ingested through PutLogEvents and have them delivered to a specific
        destination. Currently, the supported destinations are:

          * An Amazon Kinesis stream belonging to the same account as the subscription filter, for same-account delivery.

          * A logical destination that belongs to a different account, for cross-account delivery.

          * An Amazon Kinesis Firehose delivery stream that belongs to the same account as the subscription filter, for same-account delivery.

          * An AWS Lambda function that belongs to the same account as the subscription filter, for same-account delivery.

        There can only be one subscription filter associated with a log group. If you
        are updating an existing filter, you must specify the correct name in
        `filterName`. Otherwise, the call fails because you cannot associate a second
        filter with a log group.
        """
        if _request is None:
            _params = {}
            if log_group_name is not ShapeBase.NOT_SET:
                _params['log_group_name'] = log_group_name
            if filter_name is not ShapeBase.NOT_SET:
                _params['filter_name'] = filter_name
            if filter_pattern is not ShapeBase.NOT_SET:
                _params['filter_pattern'] = filter_pattern
            if destination_arn is not ShapeBase.NOT_SET:
                _params['destination_arn'] = destination_arn
            if role_arn is not ShapeBase.NOT_SET:
                _params['role_arn'] = role_arn
            if distribution is not ShapeBase.NOT_SET:
                _params['distribution'] = distribution
            _request = shapes.PutSubscriptionFilterRequest(**_params)
        response = self._boto_client.put_subscription_filter(
            **_request.to_boto()
        )

    def tag_log_group(
        self,
        _request: shapes.TagLogGroupRequest = None,
        *,
        log_group_name: str,
        tags: typing.Dict[str, str],
    ) -> None:
        """
        Adds or updates the specified tags for the specified log group.

        To list the tags for a log group, use ListTagsLogGroup. To remove tags, use
        UntagLogGroup.

        For more information about tags, see [Tag Log Groups in Amazon CloudWatch
        Logs](http://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/log-group-
        tagging.html) in the _Amazon CloudWatch Logs User Guide_.
        """
        if _request is None:
            _params = {}
            if log_group_name is not ShapeBase.NOT_SET:
                _params['log_group_name'] = log_group_name
            if tags is not ShapeBase.NOT_SET:
                _params['tags'] = tags
            _request = shapes.TagLogGroupRequest(**_params)
        response = self._boto_client.tag_log_group(**_request.to_boto())

    def test_metric_filter(
        self,
        _request: shapes.TestMetricFilterRequest = None,
        *,
        filter_pattern: str,
        log_event_messages: typing.List[str],
    ) -> shapes.TestMetricFilterResponse:
        """
        Tests the filter pattern of a metric filter against a sample of log event
        messages. You can use this operation to validate the correctness of a metric
        filter pattern.
        """
        if _request is None:
            _params = {}
            if filter_pattern is not ShapeBase.NOT_SET:
                _params['filter_pattern'] = filter_pattern
            if log_event_messages is not ShapeBase.NOT_SET:
                _params['log_event_messages'] = log_event_messages
            _request = shapes.TestMetricFilterRequest(**_params)
        response = self._boto_client.test_metric_filter(**_request.to_boto())

        return shapes.TestMetricFilterResponse.from_boto(response)

    def untag_log_group(
        self,
        _request: shapes.UntagLogGroupRequest = None,
        *,
        log_group_name: str,
        tags: typing.List[str],
    ) -> None:
        """
        Removes the specified tags from the specified log group.

        To list the tags for a log group, use ListTagsLogGroup. To add tags, use
        UntagLogGroup.
        """
        if _request is None:
            _params = {}
            if log_group_name is not ShapeBase.NOT_SET:
                _params['log_group_name'] = log_group_name
            if tags is not ShapeBase.NOT_SET:
                _params['tags'] = tags
            _request = shapes.UntagLogGroupRequest(**_params)
        response = self._boto_client.untag_log_group(**_request.to_boto())
