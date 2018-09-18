import datetime
import typing
import boto3
from autoboto import ClientBase, ShapeBase, OutputShapeBase
from . import shapes


class Client(ClientBase):
    def __init__(self, *args, **kwargs):
        super().__init__("dms", *args, **kwargs)

    def add_tags_to_resource(
        self,
        _request: shapes.AddTagsToResourceMessage = None,
        *,
        resource_arn: str,
        tags: typing.List[shapes.Tag],
    ) -> shapes.AddTagsToResourceResponse:
        """
        Adds metadata tags to an AWS DMS resource, including replication instance,
        endpoint, security group, and migration task. These tags can also be used with
        cost allocation reporting to track cost associated with DMS resources, or used
        in a Condition statement in an IAM policy for DMS.
        """
        if _request is None:
            _params = {}
            if resource_arn is not ShapeBase.NOT_SET:
                _params['resource_arn'] = resource_arn
            if tags is not ShapeBase.NOT_SET:
                _params['tags'] = tags
            _request = shapes.AddTagsToResourceMessage(**_params)
        response = self._boto_client.add_tags_to_resource(**_request.to_boto())

        return shapes.AddTagsToResourceResponse.from_boto(response)

    def create_endpoint(
        self,
        _request: shapes.CreateEndpointMessage = None,
        *,
        endpoint_identifier: str,
        endpoint_type: typing.Union[str, shapes.ReplicationEndpointTypeValue],
        engine_name: str,
        username: str = ShapeBase.NOT_SET,
        password: str = ShapeBase.NOT_SET,
        server_name: str = ShapeBase.NOT_SET,
        port: int = ShapeBase.NOT_SET,
        database_name: str = ShapeBase.NOT_SET,
        extra_connection_attributes: str = ShapeBase.NOT_SET,
        kms_key_id: str = ShapeBase.NOT_SET,
        tags: typing.List[shapes.Tag] = ShapeBase.NOT_SET,
        certificate_arn: str = ShapeBase.NOT_SET,
        ssl_mode: typing.Union[str, shapes.DmsSslModeValue] = ShapeBase.NOT_SET,
        service_access_role_arn: str = ShapeBase.NOT_SET,
        external_table_definition: str = ShapeBase.NOT_SET,
        dynamo_db_settings: shapes.DynamoDbSettings = ShapeBase.NOT_SET,
        s3_settings: shapes.S3Settings = ShapeBase.NOT_SET,
        dms_transfer_settings: shapes.DmsTransferSettings = ShapeBase.NOT_SET,
        mongo_db_settings: shapes.MongoDbSettings = ShapeBase.NOT_SET,
    ) -> shapes.CreateEndpointResponse:
        """
        Creates an endpoint using the provided settings.
        """
        if _request is None:
            _params = {}
            if endpoint_identifier is not ShapeBase.NOT_SET:
                _params['endpoint_identifier'] = endpoint_identifier
            if endpoint_type is not ShapeBase.NOT_SET:
                _params['endpoint_type'] = endpoint_type
            if engine_name is not ShapeBase.NOT_SET:
                _params['engine_name'] = engine_name
            if username is not ShapeBase.NOT_SET:
                _params['username'] = username
            if password is not ShapeBase.NOT_SET:
                _params['password'] = password
            if server_name is not ShapeBase.NOT_SET:
                _params['server_name'] = server_name
            if port is not ShapeBase.NOT_SET:
                _params['port'] = port
            if database_name is not ShapeBase.NOT_SET:
                _params['database_name'] = database_name
            if extra_connection_attributes is not ShapeBase.NOT_SET:
                _params['extra_connection_attributes'
                       ] = extra_connection_attributes
            if kms_key_id is not ShapeBase.NOT_SET:
                _params['kms_key_id'] = kms_key_id
            if tags is not ShapeBase.NOT_SET:
                _params['tags'] = tags
            if certificate_arn is not ShapeBase.NOT_SET:
                _params['certificate_arn'] = certificate_arn
            if ssl_mode is not ShapeBase.NOT_SET:
                _params['ssl_mode'] = ssl_mode
            if service_access_role_arn is not ShapeBase.NOT_SET:
                _params['service_access_role_arn'] = service_access_role_arn
            if external_table_definition is not ShapeBase.NOT_SET:
                _params['external_table_definition'] = external_table_definition
            if dynamo_db_settings is not ShapeBase.NOT_SET:
                _params['dynamo_db_settings'] = dynamo_db_settings
            if s3_settings is not ShapeBase.NOT_SET:
                _params['s3_settings'] = s3_settings
            if dms_transfer_settings is not ShapeBase.NOT_SET:
                _params['dms_transfer_settings'] = dms_transfer_settings
            if mongo_db_settings is not ShapeBase.NOT_SET:
                _params['mongo_db_settings'] = mongo_db_settings
            _request = shapes.CreateEndpointMessage(**_params)
        response = self._boto_client.create_endpoint(**_request.to_boto())

        return shapes.CreateEndpointResponse.from_boto(response)

    def create_event_subscription(
        self,
        _request: shapes.CreateEventSubscriptionMessage = None,
        *,
        subscription_name: str,
        sns_topic_arn: str,
        source_type: str = ShapeBase.NOT_SET,
        event_categories: typing.List[str] = ShapeBase.NOT_SET,
        source_ids: typing.List[str] = ShapeBase.NOT_SET,
        enabled: bool = ShapeBase.NOT_SET,
        tags: typing.List[shapes.Tag] = ShapeBase.NOT_SET,
    ) -> shapes.CreateEventSubscriptionResponse:
        """
        Creates an AWS DMS event notification subscription.

        You can specify the type of source (`SourceType`) you want to be notified of,
        provide a list of AWS DMS source IDs (`SourceIds`) that triggers the events, and
        provide a list of event categories (`EventCategories`) for events you want to be
        notified of. If you specify both the `SourceType` and `SourceIds`, such as
        `SourceType = replication-instance` and `SourceIdentifier = my-replinstance`,
        you will be notified of all the replication instance events for the specified
        source. If you specify a `SourceType` but don't specify a `SourceIdentifier`,
        you receive notice of the events for that source type for all your AWS DMS
        sources. If you don't specify either `SourceType` nor `SourceIdentifier`, you
        will be notified of events generated from all AWS DMS sources belonging to your
        customer account.

        For more information about AWS DMS events, see [ Working with Events and
        Notifications
        ](http://docs.aws.amazon.com/dms/latest/userguide/CHAP_Events.html) in the AWS
        Database MIgration Service User Guide.
        """
        if _request is None:
            _params = {}
            if subscription_name is not ShapeBase.NOT_SET:
                _params['subscription_name'] = subscription_name
            if sns_topic_arn is not ShapeBase.NOT_SET:
                _params['sns_topic_arn'] = sns_topic_arn
            if source_type is not ShapeBase.NOT_SET:
                _params['source_type'] = source_type
            if event_categories is not ShapeBase.NOT_SET:
                _params['event_categories'] = event_categories
            if source_ids is not ShapeBase.NOT_SET:
                _params['source_ids'] = source_ids
            if enabled is not ShapeBase.NOT_SET:
                _params['enabled'] = enabled
            if tags is not ShapeBase.NOT_SET:
                _params['tags'] = tags
            _request = shapes.CreateEventSubscriptionMessage(**_params)
        response = self._boto_client.create_event_subscription(
            **_request.to_boto()
        )

        return shapes.CreateEventSubscriptionResponse.from_boto(response)

    def create_replication_instance(
        self,
        _request: shapes.CreateReplicationInstanceMessage = None,
        *,
        replication_instance_identifier: str,
        replication_instance_class: str,
        allocated_storage: int = ShapeBase.NOT_SET,
        vpc_security_group_ids: typing.List[str] = ShapeBase.NOT_SET,
        availability_zone: str = ShapeBase.NOT_SET,
        replication_subnet_group_identifier: str = ShapeBase.NOT_SET,
        preferred_maintenance_window: str = ShapeBase.NOT_SET,
        multi_az: bool = ShapeBase.NOT_SET,
        engine_version: str = ShapeBase.NOT_SET,
        auto_minor_version_upgrade: bool = ShapeBase.NOT_SET,
        tags: typing.List[shapes.Tag] = ShapeBase.NOT_SET,
        kms_key_id: str = ShapeBase.NOT_SET,
        publicly_accessible: bool = ShapeBase.NOT_SET,
    ) -> shapes.CreateReplicationInstanceResponse:
        """
        Creates the replication instance using the specified parameters.
        """
        if _request is None:
            _params = {}
            if replication_instance_identifier is not ShapeBase.NOT_SET:
                _params['replication_instance_identifier'
                       ] = replication_instance_identifier
            if replication_instance_class is not ShapeBase.NOT_SET:
                _params['replication_instance_class'
                       ] = replication_instance_class
            if allocated_storage is not ShapeBase.NOT_SET:
                _params['allocated_storage'] = allocated_storage
            if vpc_security_group_ids is not ShapeBase.NOT_SET:
                _params['vpc_security_group_ids'] = vpc_security_group_ids
            if availability_zone is not ShapeBase.NOT_SET:
                _params['availability_zone'] = availability_zone
            if replication_subnet_group_identifier is not ShapeBase.NOT_SET:
                _params['replication_subnet_group_identifier'
                       ] = replication_subnet_group_identifier
            if preferred_maintenance_window is not ShapeBase.NOT_SET:
                _params['preferred_maintenance_window'
                       ] = preferred_maintenance_window
            if multi_az is not ShapeBase.NOT_SET:
                _params['multi_az'] = multi_az
            if engine_version is not ShapeBase.NOT_SET:
                _params['engine_version'] = engine_version
            if auto_minor_version_upgrade is not ShapeBase.NOT_SET:
                _params['auto_minor_version_upgrade'
                       ] = auto_minor_version_upgrade
            if tags is not ShapeBase.NOT_SET:
                _params['tags'] = tags
            if kms_key_id is not ShapeBase.NOT_SET:
                _params['kms_key_id'] = kms_key_id
            if publicly_accessible is not ShapeBase.NOT_SET:
                _params['publicly_accessible'] = publicly_accessible
            _request = shapes.CreateReplicationInstanceMessage(**_params)
        response = self._boto_client.create_replication_instance(
            **_request.to_boto()
        )

        return shapes.CreateReplicationInstanceResponse.from_boto(response)

    def create_replication_subnet_group(
        self,
        _request: shapes.CreateReplicationSubnetGroupMessage = None,
        *,
        replication_subnet_group_identifier: str,
        replication_subnet_group_description: str,
        subnet_ids: typing.List[str],
        tags: typing.List[shapes.Tag] = ShapeBase.NOT_SET,
    ) -> shapes.CreateReplicationSubnetGroupResponse:
        """
        Creates a replication subnet group given a list of the subnet IDs in a VPC.
        """
        if _request is None:
            _params = {}
            if replication_subnet_group_identifier is not ShapeBase.NOT_SET:
                _params['replication_subnet_group_identifier'
                       ] = replication_subnet_group_identifier
            if replication_subnet_group_description is not ShapeBase.NOT_SET:
                _params['replication_subnet_group_description'
                       ] = replication_subnet_group_description
            if subnet_ids is not ShapeBase.NOT_SET:
                _params['subnet_ids'] = subnet_ids
            if tags is not ShapeBase.NOT_SET:
                _params['tags'] = tags
            _request = shapes.CreateReplicationSubnetGroupMessage(**_params)
        response = self._boto_client.create_replication_subnet_group(
            **_request.to_boto()
        )

        return shapes.CreateReplicationSubnetGroupResponse.from_boto(response)

    def create_replication_task(
        self,
        _request: shapes.CreateReplicationTaskMessage = None,
        *,
        replication_task_identifier: str,
        source_endpoint_arn: str,
        target_endpoint_arn: str,
        replication_instance_arn: str,
        migration_type: typing.Union[str, shapes.MigrationTypeValue],
        table_mappings: str,
        replication_task_settings: str = ShapeBase.NOT_SET,
        cdc_start_time: datetime.datetime = ShapeBase.NOT_SET,
        cdc_start_position: str = ShapeBase.NOT_SET,
        cdc_stop_position: str = ShapeBase.NOT_SET,
        tags: typing.List[shapes.Tag] = ShapeBase.NOT_SET,
    ) -> shapes.CreateReplicationTaskResponse:
        """
        Creates a replication task using the specified parameters.
        """
        if _request is None:
            _params = {}
            if replication_task_identifier is not ShapeBase.NOT_SET:
                _params['replication_task_identifier'
                       ] = replication_task_identifier
            if source_endpoint_arn is not ShapeBase.NOT_SET:
                _params['source_endpoint_arn'] = source_endpoint_arn
            if target_endpoint_arn is not ShapeBase.NOT_SET:
                _params['target_endpoint_arn'] = target_endpoint_arn
            if replication_instance_arn is not ShapeBase.NOT_SET:
                _params['replication_instance_arn'] = replication_instance_arn
            if migration_type is not ShapeBase.NOT_SET:
                _params['migration_type'] = migration_type
            if table_mappings is not ShapeBase.NOT_SET:
                _params['table_mappings'] = table_mappings
            if replication_task_settings is not ShapeBase.NOT_SET:
                _params['replication_task_settings'] = replication_task_settings
            if cdc_start_time is not ShapeBase.NOT_SET:
                _params['cdc_start_time'] = cdc_start_time
            if cdc_start_position is not ShapeBase.NOT_SET:
                _params['cdc_start_position'] = cdc_start_position
            if cdc_stop_position is not ShapeBase.NOT_SET:
                _params['cdc_stop_position'] = cdc_stop_position
            if tags is not ShapeBase.NOT_SET:
                _params['tags'] = tags
            _request = shapes.CreateReplicationTaskMessage(**_params)
        response = self._boto_client.create_replication_task(
            **_request.to_boto()
        )

        return shapes.CreateReplicationTaskResponse.from_boto(response)

    def delete_certificate(
        self,
        _request: shapes.DeleteCertificateMessage = None,
        *,
        certificate_arn: str,
    ) -> shapes.DeleteCertificateResponse:
        """
        Deletes the specified certificate.
        """
        if _request is None:
            _params = {}
            if certificate_arn is not ShapeBase.NOT_SET:
                _params['certificate_arn'] = certificate_arn
            _request = shapes.DeleteCertificateMessage(**_params)
        response = self._boto_client.delete_certificate(**_request.to_boto())

        return shapes.DeleteCertificateResponse.from_boto(response)

    def delete_endpoint(
        self,
        _request: shapes.DeleteEndpointMessage = None,
        *,
        endpoint_arn: str,
    ) -> shapes.DeleteEndpointResponse:
        """
        Deletes the specified endpoint.

        All tasks associated with the endpoint must be deleted before you can delete the
        endpoint.
        """
        if _request is None:
            _params = {}
            if endpoint_arn is not ShapeBase.NOT_SET:
                _params['endpoint_arn'] = endpoint_arn
            _request = shapes.DeleteEndpointMessage(**_params)
        response = self._boto_client.delete_endpoint(**_request.to_boto())

        return shapes.DeleteEndpointResponse.from_boto(response)

    def delete_event_subscription(
        self,
        _request: shapes.DeleteEventSubscriptionMessage = None,
        *,
        subscription_name: str,
    ) -> shapes.DeleteEventSubscriptionResponse:
        """
        Deletes an AWS DMS event subscription.
        """
        if _request is None:
            _params = {}
            if subscription_name is not ShapeBase.NOT_SET:
                _params['subscription_name'] = subscription_name
            _request = shapes.DeleteEventSubscriptionMessage(**_params)
        response = self._boto_client.delete_event_subscription(
            **_request.to_boto()
        )

        return shapes.DeleteEventSubscriptionResponse.from_boto(response)

    def delete_replication_instance(
        self,
        _request: shapes.DeleteReplicationInstanceMessage = None,
        *,
        replication_instance_arn: str,
    ) -> shapes.DeleteReplicationInstanceResponse:
        """
        Deletes the specified replication instance.

        You must delete any migration tasks that are associated with the replication
        instance before you can delete it.
        """
        if _request is None:
            _params = {}
            if replication_instance_arn is not ShapeBase.NOT_SET:
                _params['replication_instance_arn'] = replication_instance_arn
            _request = shapes.DeleteReplicationInstanceMessage(**_params)
        response = self._boto_client.delete_replication_instance(
            **_request.to_boto()
        )

        return shapes.DeleteReplicationInstanceResponse.from_boto(response)

    def delete_replication_subnet_group(
        self,
        _request: shapes.DeleteReplicationSubnetGroupMessage = None,
        *,
        replication_subnet_group_identifier: str,
    ) -> shapes.DeleteReplicationSubnetGroupResponse:
        """
        Deletes a subnet group.
        """
        if _request is None:
            _params = {}
            if replication_subnet_group_identifier is not ShapeBase.NOT_SET:
                _params['replication_subnet_group_identifier'
                       ] = replication_subnet_group_identifier
            _request = shapes.DeleteReplicationSubnetGroupMessage(**_params)
        response = self._boto_client.delete_replication_subnet_group(
            **_request.to_boto()
        )

        return shapes.DeleteReplicationSubnetGroupResponse.from_boto(response)

    def delete_replication_task(
        self,
        _request: shapes.DeleteReplicationTaskMessage = None,
        *,
        replication_task_arn: str,
    ) -> shapes.DeleteReplicationTaskResponse:
        """
        Deletes the specified replication task.
        """
        if _request is None:
            _params = {}
            if replication_task_arn is not ShapeBase.NOT_SET:
                _params['replication_task_arn'] = replication_task_arn
            _request = shapes.DeleteReplicationTaskMessage(**_params)
        response = self._boto_client.delete_replication_task(
            **_request.to_boto()
        )

        return shapes.DeleteReplicationTaskResponse.from_boto(response)

    def describe_account_attributes(
        self,
        _request: shapes.DescribeAccountAttributesMessage = None,
    ) -> shapes.DescribeAccountAttributesResponse:
        """
        Lists all of the AWS DMS attributes for a customer account. The attributes
        include AWS DMS quotas for the account, such as the number of replication
        instances allowed. The description for a quota includes the quota name, current
        usage toward that quota, and the quota's maximum value.

        This command does not take any parameters.
        """
        if _request is None:
            _params = {}
            _request = shapes.DescribeAccountAttributesMessage(**_params)
        response = self._boto_client.describe_account_attributes(
            **_request.to_boto()
        )

        return shapes.DescribeAccountAttributesResponse.from_boto(response)

    def describe_certificates(
        self,
        _request: shapes.DescribeCertificatesMessage = None,
        *,
        filters: typing.List[shapes.Filter] = ShapeBase.NOT_SET,
        max_records: int = ShapeBase.NOT_SET,
        marker: str = ShapeBase.NOT_SET,
    ) -> shapes.DescribeCertificatesResponse:
        """
        Provides a description of the certificate.
        """
        if _request is None:
            _params = {}
            if filters is not ShapeBase.NOT_SET:
                _params['filters'] = filters
            if max_records is not ShapeBase.NOT_SET:
                _params['max_records'] = max_records
            if marker is not ShapeBase.NOT_SET:
                _params['marker'] = marker
            _request = shapes.DescribeCertificatesMessage(**_params)
        paginator = self.get_paginator("describe_certificates").paginate(
            **_request.to_boto()
        )
        page_generator = (page for page in paginator)
        first_page = next(page_generator)
        result = shapes.DescribeCertificatesResponse.from_boto(first_page)
        result._page_iterator = page_generator
        return result

        return shapes.DescribeCertificatesResponse.from_boto(response)

    def describe_connections(
        self,
        _request: shapes.DescribeConnectionsMessage = None,
        *,
        filters: typing.List[shapes.Filter] = ShapeBase.NOT_SET,
        max_records: int = ShapeBase.NOT_SET,
        marker: str = ShapeBase.NOT_SET,
    ) -> shapes.DescribeConnectionsResponse:
        """
        Describes the status of the connections that have been made between the
        replication instance and an endpoint. Connections are created when you test an
        endpoint.
        """
        if _request is None:
            _params = {}
            if filters is not ShapeBase.NOT_SET:
                _params['filters'] = filters
            if max_records is not ShapeBase.NOT_SET:
                _params['max_records'] = max_records
            if marker is not ShapeBase.NOT_SET:
                _params['marker'] = marker
            _request = shapes.DescribeConnectionsMessage(**_params)
        paginator = self.get_paginator("describe_connections").paginate(
            **_request.to_boto()
        )
        page_generator = (page for page in paginator)
        first_page = next(page_generator)
        result = shapes.DescribeConnectionsResponse.from_boto(first_page)
        result._page_iterator = page_generator
        return result

        return shapes.DescribeConnectionsResponse.from_boto(response)

    def describe_endpoint_types(
        self,
        _request: shapes.DescribeEndpointTypesMessage = None,
        *,
        filters: typing.List[shapes.Filter] = ShapeBase.NOT_SET,
        max_records: int = ShapeBase.NOT_SET,
        marker: str = ShapeBase.NOT_SET,
    ) -> shapes.DescribeEndpointTypesResponse:
        """
        Returns information about the type of endpoints available.
        """
        if _request is None:
            _params = {}
            if filters is not ShapeBase.NOT_SET:
                _params['filters'] = filters
            if max_records is not ShapeBase.NOT_SET:
                _params['max_records'] = max_records
            if marker is not ShapeBase.NOT_SET:
                _params['marker'] = marker
            _request = shapes.DescribeEndpointTypesMessage(**_params)
        paginator = self.get_paginator("describe_endpoint_types").paginate(
            **_request.to_boto()
        )
        page_generator = (page for page in paginator)
        first_page = next(page_generator)
        result = shapes.DescribeEndpointTypesResponse.from_boto(first_page)
        result._page_iterator = page_generator
        return result

        return shapes.DescribeEndpointTypesResponse.from_boto(response)

    def describe_endpoints(
        self,
        _request: shapes.DescribeEndpointsMessage = None,
        *,
        filters: typing.List[shapes.Filter] = ShapeBase.NOT_SET,
        max_records: int = ShapeBase.NOT_SET,
        marker: str = ShapeBase.NOT_SET,
    ) -> shapes.DescribeEndpointsResponse:
        """
        Returns information about the endpoints for your account in the current region.
        """
        if _request is None:
            _params = {}
            if filters is not ShapeBase.NOT_SET:
                _params['filters'] = filters
            if max_records is not ShapeBase.NOT_SET:
                _params['max_records'] = max_records
            if marker is not ShapeBase.NOT_SET:
                _params['marker'] = marker
            _request = shapes.DescribeEndpointsMessage(**_params)
        paginator = self.get_paginator("describe_endpoints").paginate(
            **_request.to_boto()
        )
        page_generator = (page for page in paginator)
        first_page = next(page_generator)
        result = shapes.DescribeEndpointsResponse.from_boto(first_page)
        result._page_iterator = page_generator
        return result

        return shapes.DescribeEndpointsResponse.from_boto(response)

    def describe_event_categories(
        self,
        _request: shapes.DescribeEventCategoriesMessage = None,
        *,
        source_type: str = ShapeBase.NOT_SET,
        filters: typing.List[shapes.Filter] = ShapeBase.NOT_SET,
    ) -> shapes.DescribeEventCategoriesResponse:
        """
        Lists categories for all event source types, or, if specified, for a specified
        source type. You can see a list of the event categories and source types in [
        Working with Events and Notifications
        ](http://docs.aws.amazon.com/dms/latest/userguide/CHAP_Events.html) in the AWS
        Database Migration Service User Guide.
        """
        if _request is None:
            _params = {}
            if source_type is not ShapeBase.NOT_SET:
                _params['source_type'] = source_type
            if filters is not ShapeBase.NOT_SET:
                _params['filters'] = filters
            _request = shapes.DescribeEventCategoriesMessage(**_params)
        response = self._boto_client.describe_event_categories(
            **_request.to_boto()
        )

        return shapes.DescribeEventCategoriesResponse.from_boto(response)

    def describe_event_subscriptions(
        self,
        _request: shapes.DescribeEventSubscriptionsMessage = None,
        *,
        subscription_name: str = ShapeBase.NOT_SET,
        filters: typing.List[shapes.Filter] = ShapeBase.NOT_SET,
        max_records: int = ShapeBase.NOT_SET,
        marker: str = ShapeBase.NOT_SET,
    ) -> shapes.DescribeEventSubscriptionsResponse:
        """
        Lists all the event subscriptions for a customer account. The description of a
        subscription includes `SubscriptionName`, `SNSTopicARN`, `CustomerID`,
        `SourceType`, `SourceID`, `CreationTime`, and `Status`.

        If you specify `SubscriptionName`, this action lists the description for that
        subscription.
        """
        if _request is None:
            _params = {}
            if subscription_name is not ShapeBase.NOT_SET:
                _params['subscription_name'] = subscription_name
            if filters is not ShapeBase.NOT_SET:
                _params['filters'] = filters
            if max_records is not ShapeBase.NOT_SET:
                _params['max_records'] = max_records
            if marker is not ShapeBase.NOT_SET:
                _params['marker'] = marker
            _request = shapes.DescribeEventSubscriptionsMessage(**_params)
        paginator = self.get_paginator("describe_event_subscriptions").paginate(
            **_request.to_boto()
        )
        page_generator = (page for page in paginator)
        first_page = next(page_generator)
        result = shapes.DescribeEventSubscriptionsResponse.from_boto(first_page)
        result._page_iterator = page_generator
        return result

        return shapes.DescribeEventSubscriptionsResponse.from_boto(response)

    def describe_events(
        self,
        _request: shapes.DescribeEventsMessage = None,
        *,
        source_identifier: str = ShapeBase.NOT_SET,
        source_type: typing.Union[str, shapes.SourceType] = ShapeBase.NOT_SET,
        start_time: datetime.datetime = ShapeBase.NOT_SET,
        end_time: datetime.datetime = ShapeBase.NOT_SET,
        duration: int = ShapeBase.NOT_SET,
        event_categories: typing.List[str] = ShapeBase.NOT_SET,
        filters: typing.List[shapes.Filter] = ShapeBase.NOT_SET,
        max_records: int = ShapeBase.NOT_SET,
        marker: str = ShapeBase.NOT_SET,
    ) -> shapes.DescribeEventsResponse:
        """
        Lists events for a given source identifier and source type. You can also specify
        a start and end time. For more information on AWS DMS events, see [ Working with
        Events and Notifications
        ](http://docs.aws.amazon.com/dms/latest/userguide/CHAP_Events.html).
        """
        if _request is None:
            _params = {}
            if source_identifier is not ShapeBase.NOT_SET:
                _params['source_identifier'] = source_identifier
            if source_type is not ShapeBase.NOT_SET:
                _params['source_type'] = source_type
            if start_time is not ShapeBase.NOT_SET:
                _params['start_time'] = start_time
            if end_time is not ShapeBase.NOT_SET:
                _params['end_time'] = end_time
            if duration is not ShapeBase.NOT_SET:
                _params['duration'] = duration
            if event_categories is not ShapeBase.NOT_SET:
                _params['event_categories'] = event_categories
            if filters is not ShapeBase.NOT_SET:
                _params['filters'] = filters
            if max_records is not ShapeBase.NOT_SET:
                _params['max_records'] = max_records
            if marker is not ShapeBase.NOT_SET:
                _params['marker'] = marker
            _request = shapes.DescribeEventsMessage(**_params)
        paginator = self.get_paginator("describe_events").paginate(
            **_request.to_boto()
        )
        page_generator = (page for page in paginator)
        first_page = next(page_generator)
        result = shapes.DescribeEventsResponse.from_boto(first_page)
        result._page_iterator = page_generator
        return result

        return shapes.DescribeEventsResponse.from_boto(response)

    def describe_orderable_replication_instances(
        self,
        _request: shapes.DescribeOrderableReplicationInstancesMessage = None,
        *,
        max_records: int = ShapeBase.NOT_SET,
        marker: str = ShapeBase.NOT_SET,
    ) -> shapes.DescribeOrderableReplicationInstancesResponse:
        """
        Returns information about the replication instance types that can be created in
        the specified region.
        """
        if _request is None:
            _params = {}
            if max_records is not ShapeBase.NOT_SET:
                _params['max_records'] = max_records
            if marker is not ShapeBase.NOT_SET:
                _params['marker'] = marker
            _request = shapes.DescribeOrderableReplicationInstancesMessage(
                **_params
            )
        paginator = self.get_paginator(
            "describe_orderable_replication_instances"
        ).paginate(**_request.to_boto())
        page_generator = (page for page in paginator)
        first_page = next(page_generator)
        result = shapes.DescribeOrderableReplicationInstancesResponse.from_boto(
            first_page
        )
        result._page_iterator = page_generator
        return result

        return shapes.DescribeOrderableReplicationInstancesResponse.from_boto(
            response
        )

    def describe_refresh_schemas_status(
        self,
        _request: shapes.DescribeRefreshSchemasStatusMessage = None,
        *,
        endpoint_arn: str,
    ) -> shapes.DescribeRefreshSchemasStatusResponse:
        """
        Returns the status of the RefreshSchemas operation.
        """
        if _request is None:
            _params = {}
            if endpoint_arn is not ShapeBase.NOT_SET:
                _params['endpoint_arn'] = endpoint_arn
            _request = shapes.DescribeRefreshSchemasStatusMessage(**_params)
        response = self._boto_client.describe_refresh_schemas_status(
            **_request.to_boto()
        )

        return shapes.DescribeRefreshSchemasStatusResponse.from_boto(response)

    def describe_replication_instance_task_logs(
        self,
        _request: shapes.DescribeReplicationInstanceTaskLogsMessage = None,
        *,
        replication_instance_arn: str,
        max_records: int = ShapeBase.NOT_SET,
        marker: str = ShapeBase.NOT_SET,
    ) -> shapes.DescribeReplicationInstanceTaskLogsResponse:
        """
        Returns information about the task logs for the specified task.
        """
        if _request is None:
            _params = {}
            if replication_instance_arn is not ShapeBase.NOT_SET:
                _params['replication_instance_arn'] = replication_instance_arn
            if max_records is not ShapeBase.NOT_SET:
                _params['max_records'] = max_records
            if marker is not ShapeBase.NOT_SET:
                _params['marker'] = marker
            _request = shapes.DescribeReplicationInstanceTaskLogsMessage(
                **_params
            )
        response = self._boto_client.describe_replication_instance_task_logs(
            **_request.to_boto()
        )

        return shapes.DescribeReplicationInstanceTaskLogsResponse.from_boto(
            response
        )

    def describe_replication_instances(
        self,
        _request: shapes.DescribeReplicationInstancesMessage = None,
        *,
        filters: typing.List[shapes.Filter] = ShapeBase.NOT_SET,
        max_records: int = ShapeBase.NOT_SET,
        marker: str = ShapeBase.NOT_SET,
    ) -> shapes.DescribeReplicationInstancesResponse:
        """
        Returns information about replication instances for your account in the current
        region.
        """
        if _request is None:
            _params = {}
            if filters is not ShapeBase.NOT_SET:
                _params['filters'] = filters
            if max_records is not ShapeBase.NOT_SET:
                _params['max_records'] = max_records
            if marker is not ShapeBase.NOT_SET:
                _params['marker'] = marker
            _request = shapes.DescribeReplicationInstancesMessage(**_params)
        paginator = self.get_paginator("describe_replication_instances"
                                      ).paginate(**_request.to_boto())
        page_generator = (page for page in paginator)
        first_page = next(page_generator)
        result = shapes.DescribeReplicationInstancesResponse.from_boto(
            first_page
        )
        result._page_iterator = page_generator
        return result

        return shapes.DescribeReplicationInstancesResponse.from_boto(response)

    def describe_replication_subnet_groups(
        self,
        _request: shapes.DescribeReplicationSubnetGroupsMessage = None,
        *,
        filters: typing.List[shapes.Filter] = ShapeBase.NOT_SET,
        max_records: int = ShapeBase.NOT_SET,
        marker: str = ShapeBase.NOT_SET,
    ) -> shapes.DescribeReplicationSubnetGroupsResponse:
        """
        Returns information about the replication subnet groups.
        """
        if _request is None:
            _params = {}
            if filters is not ShapeBase.NOT_SET:
                _params['filters'] = filters
            if max_records is not ShapeBase.NOT_SET:
                _params['max_records'] = max_records
            if marker is not ShapeBase.NOT_SET:
                _params['marker'] = marker
            _request = shapes.DescribeReplicationSubnetGroupsMessage(**_params)
        paginator = self.get_paginator("describe_replication_subnet_groups"
                                      ).paginate(**_request.to_boto())
        page_generator = (page for page in paginator)
        first_page = next(page_generator)
        result = shapes.DescribeReplicationSubnetGroupsResponse.from_boto(
            first_page
        )
        result._page_iterator = page_generator
        return result

        return shapes.DescribeReplicationSubnetGroupsResponse.from_boto(
            response
        )

    def describe_replication_task_assessment_results(
        self,
        _request: shapes.DescribeReplicationTaskAssessmentResultsMessage = None,
        *,
        replication_task_arn: str = ShapeBase.NOT_SET,
        max_records: int = ShapeBase.NOT_SET,
        marker: str = ShapeBase.NOT_SET,
    ) -> shapes.DescribeReplicationTaskAssessmentResultsResponse:
        """
        Returns the task assessment results from Amazon S3. This action always returns
        the latest results.
        """
        if _request is None:
            _params = {}
            if replication_task_arn is not ShapeBase.NOT_SET:
                _params['replication_task_arn'] = replication_task_arn
            if max_records is not ShapeBase.NOT_SET:
                _params['max_records'] = max_records
            if marker is not ShapeBase.NOT_SET:
                _params['marker'] = marker
            _request = shapes.DescribeReplicationTaskAssessmentResultsMessage(
                **_params
            )
        paginator = self.get_paginator(
            "describe_replication_task_assessment_results"
        ).paginate(**_request.to_boto())
        page_generator = (page for page in paginator)
        first_page = next(page_generator)
        result = shapes.DescribeReplicationTaskAssessmentResultsResponse.from_boto(
            first_page
        )
        result._page_iterator = page_generator
        return result

        return shapes.DescribeReplicationTaskAssessmentResultsResponse.from_boto(
            response
        )

    def describe_replication_tasks(
        self,
        _request: shapes.DescribeReplicationTasksMessage = None,
        *,
        filters: typing.List[shapes.Filter] = ShapeBase.NOT_SET,
        max_records: int = ShapeBase.NOT_SET,
        marker: str = ShapeBase.NOT_SET,
    ) -> shapes.DescribeReplicationTasksResponse:
        """
        Returns information about replication tasks for your account in the current
        region.
        """
        if _request is None:
            _params = {}
            if filters is not ShapeBase.NOT_SET:
                _params['filters'] = filters
            if max_records is not ShapeBase.NOT_SET:
                _params['max_records'] = max_records
            if marker is not ShapeBase.NOT_SET:
                _params['marker'] = marker
            _request = shapes.DescribeReplicationTasksMessage(**_params)
        paginator = self.get_paginator("describe_replication_tasks").paginate(
            **_request.to_boto()
        )
        page_generator = (page for page in paginator)
        first_page = next(page_generator)
        result = shapes.DescribeReplicationTasksResponse.from_boto(first_page)
        result._page_iterator = page_generator
        return result

        return shapes.DescribeReplicationTasksResponse.from_boto(response)

    def describe_schemas(
        self,
        _request: shapes.DescribeSchemasMessage = None,
        *,
        endpoint_arn: str,
        max_records: int = ShapeBase.NOT_SET,
        marker: str = ShapeBase.NOT_SET,
    ) -> shapes.DescribeSchemasResponse:
        """
        Returns information about the schema for the specified endpoint.
        """
        if _request is None:
            _params = {}
            if endpoint_arn is not ShapeBase.NOT_SET:
                _params['endpoint_arn'] = endpoint_arn
            if max_records is not ShapeBase.NOT_SET:
                _params['max_records'] = max_records
            if marker is not ShapeBase.NOT_SET:
                _params['marker'] = marker
            _request = shapes.DescribeSchemasMessage(**_params)
        paginator = self.get_paginator("describe_schemas").paginate(
            **_request.to_boto()
        )
        page_generator = (page for page in paginator)
        first_page = next(page_generator)
        result = shapes.DescribeSchemasResponse.from_boto(first_page)
        result._page_iterator = page_generator
        return result

        return shapes.DescribeSchemasResponse.from_boto(response)

    def describe_table_statistics(
        self,
        _request: shapes.DescribeTableStatisticsMessage = None,
        *,
        replication_task_arn: str,
        max_records: int = ShapeBase.NOT_SET,
        marker: str = ShapeBase.NOT_SET,
        filters: typing.List[shapes.Filter] = ShapeBase.NOT_SET,
    ) -> shapes.DescribeTableStatisticsResponse:
        """
        Returns table statistics on the database migration task, including table name,
        rows inserted, rows updated, and rows deleted.

        Note that the "last updated" column the DMS console only indicates the time that
        AWS DMS last updated the table statistics record for a table. It does not
        indicate the time of the last update to the table.
        """
        if _request is None:
            _params = {}
            if replication_task_arn is not ShapeBase.NOT_SET:
                _params['replication_task_arn'] = replication_task_arn
            if max_records is not ShapeBase.NOT_SET:
                _params['max_records'] = max_records
            if marker is not ShapeBase.NOT_SET:
                _params['marker'] = marker
            if filters is not ShapeBase.NOT_SET:
                _params['filters'] = filters
            _request = shapes.DescribeTableStatisticsMessage(**_params)
        paginator = self.get_paginator("describe_table_statistics").paginate(
            **_request.to_boto()
        )
        page_generator = (page for page in paginator)
        first_page = next(page_generator)
        result = shapes.DescribeTableStatisticsResponse.from_boto(first_page)
        result._page_iterator = page_generator
        return result

        return shapes.DescribeTableStatisticsResponse.from_boto(response)

    def import_certificate(
        self,
        _request: shapes.ImportCertificateMessage = None,
        *,
        certificate_identifier: str,
        certificate_pem: str = ShapeBase.NOT_SET,
        certificate_wallet: typing.Any = ShapeBase.NOT_SET,
        tags: typing.List[shapes.Tag] = ShapeBase.NOT_SET,
    ) -> shapes.ImportCertificateResponse:
        """
        Uploads the specified certificate.
        """
        if _request is None:
            _params = {}
            if certificate_identifier is not ShapeBase.NOT_SET:
                _params['certificate_identifier'] = certificate_identifier
            if certificate_pem is not ShapeBase.NOT_SET:
                _params['certificate_pem'] = certificate_pem
            if certificate_wallet is not ShapeBase.NOT_SET:
                _params['certificate_wallet'] = certificate_wallet
            if tags is not ShapeBase.NOT_SET:
                _params['tags'] = tags
            _request = shapes.ImportCertificateMessage(**_params)
        response = self._boto_client.import_certificate(**_request.to_boto())

        return shapes.ImportCertificateResponse.from_boto(response)

    def list_tags_for_resource(
        self,
        _request: shapes.ListTagsForResourceMessage = None,
        *,
        resource_arn: str,
    ) -> shapes.ListTagsForResourceResponse:
        """
        Lists all tags for an AWS DMS resource.
        """
        if _request is None:
            _params = {}
            if resource_arn is not ShapeBase.NOT_SET:
                _params['resource_arn'] = resource_arn
            _request = shapes.ListTagsForResourceMessage(**_params)
        response = self._boto_client.list_tags_for_resource(
            **_request.to_boto()
        )

        return shapes.ListTagsForResourceResponse.from_boto(response)

    def modify_endpoint(
        self,
        _request: shapes.ModifyEndpointMessage = None,
        *,
        endpoint_arn: str,
        endpoint_identifier: str = ShapeBase.NOT_SET,
        endpoint_type: typing.
        Union[str, shapes.ReplicationEndpointTypeValue] = ShapeBase.NOT_SET,
        engine_name: str = ShapeBase.NOT_SET,
        username: str = ShapeBase.NOT_SET,
        password: str = ShapeBase.NOT_SET,
        server_name: str = ShapeBase.NOT_SET,
        port: int = ShapeBase.NOT_SET,
        database_name: str = ShapeBase.NOT_SET,
        extra_connection_attributes: str = ShapeBase.NOT_SET,
        certificate_arn: str = ShapeBase.NOT_SET,
        ssl_mode: typing.Union[str, shapes.DmsSslModeValue] = ShapeBase.NOT_SET,
        service_access_role_arn: str = ShapeBase.NOT_SET,
        external_table_definition: str = ShapeBase.NOT_SET,
        dynamo_db_settings: shapes.DynamoDbSettings = ShapeBase.NOT_SET,
        s3_settings: shapes.S3Settings = ShapeBase.NOT_SET,
        dms_transfer_settings: shapes.DmsTransferSettings = ShapeBase.NOT_SET,
        mongo_db_settings: shapes.MongoDbSettings = ShapeBase.NOT_SET,
    ) -> shapes.ModifyEndpointResponse:
        """
        Modifies the specified endpoint.
        """
        if _request is None:
            _params = {}
            if endpoint_arn is not ShapeBase.NOT_SET:
                _params['endpoint_arn'] = endpoint_arn
            if endpoint_identifier is not ShapeBase.NOT_SET:
                _params['endpoint_identifier'] = endpoint_identifier
            if endpoint_type is not ShapeBase.NOT_SET:
                _params['endpoint_type'] = endpoint_type
            if engine_name is not ShapeBase.NOT_SET:
                _params['engine_name'] = engine_name
            if username is not ShapeBase.NOT_SET:
                _params['username'] = username
            if password is not ShapeBase.NOT_SET:
                _params['password'] = password
            if server_name is not ShapeBase.NOT_SET:
                _params['server_name'] = server_name
            if port is not ShapeBase.NOT_SET:
                _params['port'] = port
            if database_name is not ShapeBase.NOT_SET:
                _params['database_name'] = database_name
            if extra_connection_attributes is not ShapeBase.NOT_SET:
                _params['extra_connection_attributes'
                       ] = extra_connection_attributes
            if certificate_arn is not ShapeBase.NOT_SET:
                _params['certificate_arn'] = certificate_arn
            if ssl_mode is not ShapeBase.NOT_SET:
                _params['ssl_mode'] = ssl_mode
            if service_access_role_arn is not ShapeBase.NOT_SET:
                _params['service_access_role_arn'] = service_access_role_arn
            if external_table_definition is not ShapeBase.NOT_SET:
                _params['external_table_definition'] = external_table_definition
            if dynamo_db_settings is not ShapeBase.NOT_SET:
                _params['dynamo_db_settings'] = dynamo_db_settings
            if s3_settings is not ShapeBase.NOT_SET:
                _params['s3_settings'] = s3_settings
            if dms_transfer_settings is not ShapeBase.NOT_SET:
                _params['dms_transfer_settings'] = dms_transfer_settings
            if mongo_db_settings is not ShapeBase.NOT_SET:
                _params['mongo_db_settings'] = mongo_db_settings
            _request = shapes.ModifyEndpointMessage(**_params)
        response = self._boto_client.modify_endpoint(**_request.to_boto())

        return shapes.ModifyEndpointResponse.from_boto(response)

    def modify_event_subscription(
        self,
        _request: shapes.ModifyEventSubscriptionMessage = None,
        *,
        subscription_name: str,
        sns_topic_arn: str = ShapeBase.NOT_SET,
        source_type: str = ShapeBase.NOT_SET,
        event_categories: typing.List[str] = ShapeBase.NOT_SET,
        enabled: bool = ShapeBase.NOT_SET,
    ) -> shapes.ModifyEventSubscriptionResponse:
        """
        Modifies an existing AWS DMS event notification subscription.
        """
        if _request is None:
            _params = {}
            if subscription_name is not ShapeBase.NOT_SET:
                _params['subscription_name'] = subscription_name
            if sns_topic_arn is not ShapeBase.NOT_SET:
                _params['sns_topic_arn'] = sns_topic_arn
            if source_type is not ShapeBase.NOT_SET:
                _params['source_type'] = source_type
            if event_categories is not ShapeBase.NOT_SET:
                _params['event_categories'] = event_categories
            if enabled is not ShapeBase.NOT_SET:
                _params['enabled'] = enabled
            _request = shapes.ModifyEventSubscriptionMessage(**_params)
        response = self._boto_client.modify_event_subscription(
            **_request.to_boto()
        )

        return shapes.ModifyEventSubscriptionResponse.from_boto(response)

    def modify_replication_instance(
        self,
        _request: shapes.ModifyReplicationInstanceMessage = None,
        *,
        replication_instance_arn: str,
        allocated_storage: int = ShapeBase.NOT_SET,
        apply_immediately: bool = ShapeBase.NOT_SET,
        replication_instance_class: str = ShapeBase.NOT_SET,
        vpc_security_group_ids: typing.List[str] = ShapeBase.NOT_SET,
        preferred_maintenance_window: str = ShapeBase.NOT_SET,
        multi_az: bool = ShapeBase.NOT_SET,
        engine_version: str = ShapeBase.NOT_SET,
        allow_major_version_upgrade: bool = ShapeBase.NOT_SET,
        auto_minor_version_upgrade: bool = ShapeBase.NOT_SET,
        replication_instance_identifier: str = ShapeBase.NOT_SET,
    ) -> shapes.ModifyReplicationInstanceResponse:
        """
        Modifies the replication instance to apply new settings. You can change one or
        more parameters by specifying these parameters and the new values in the
        request.

        Some settings are applied during the maintenance window.
        """
        if _request is None:
            _params = {}
            if replication_instance_arn is not ShapeBase.NOT_SET:
                _params['replication_instance_arn'] = replication_instance_arn
            if allocated_storage is not ShapeBase.NOT_SET:
                _params['allocated_storage'] = allocated_storage
            if apply_immediately is not ShapeBase.NOT_SET:
                _params['apply_immediately'] = apply_immediately
            if replication_instance_class is not ShapeBase.NOT_SET:
                _params['replication_instance_class'
                       ] = replication_instance_class
            if vpc_security_group_ids is not ShapeBase.NOT_SET:
                _params['vpc_security_group_ids'] = vpc_security_group_ids
            if preferred_maintenance_window is not ShapeBase.NOT_SET:
                _params['preferred_maintenance_window'
                       ] = preferred_maintenance_window
            if multi_az is not ShapeBase.NOT_SET:
                _params['multi_az'] = multi_az
            if engine_version is not ShapeBase.NOT_SET:
                _params['engine_version'] = engine_version
            if allow_major_version_upgrade is not ShapeBase.NOT_SET:
                _params['allow_major_version_upgrade'
                       ] = allow_major_version_upgrade
            if auto_minor_version_upgrade is not ShapeBase.NOT_SET:
                _params['auto_minor_version_upgrade'
                       ] = auto_minor_version_upgrade
            if replication_instance_identifier is not ShapeBase.NOT_SET:
                _params['replication_instance_identifier'
                       ] = replication_instance_identifier
            _request = shapes.ModifyReplicationInstanceMessage(**_params)
        response = self._boto_client.modify_replication_instance(
            **_request.to_boto()
        )

        return shapes.ModifyReplicationInstanceResponse.from_boto(response)

    def modify_replication_subnet_group(
        self,
        _request: shapes.ModifyReplicationSubnetGroupMessage = None,
        *,
        replication_subnet_group_identifier: str,
        subnet_ids: typing.List[str],
        replication_subnet_group_description: str = ShapeBase.NOT_SET,
    ) -> shapes.ModifyReplicationSubnetGroupResponse:
        """
        Modifies the settings for the specified replication subnet group.
        """
        if _request is None:
            _params = {}
            if replication_subnet_group_identifier is not ShapeBase.NOT_SET:
                _params['replication_subnet_group_identifier'
                       ] = replication_subnet_group_identifier
            if subnet_ids is not ShapeBase.NOT_SET:
                _params['subnet_ids'] = subnet_ids
            if replication_subnet_group_description is not ShapeBase.NOT_SET:
                _params['replication_subnet_group_description'
                       ] = replication_subnet_group_description
            _request = shapes.ModifyReplicationSubnetGroupMessage(**_params)
        response = self._boto_client.modify_replication_subnet_group(
            **_request.to_boto()
        )

        return shapes.ModifyReplicationSubnetGroupResponse.from_boto(response)

    def modify_replication_task(
        self,
        _request: shapes.ModifyReplicationTaskMessage = None,
        *,
        replication_task_arn: str,
        replication_task_identifier: str = ShapeBase.NOT_SET,
        migration_type: typing.Union[str, shapes.
                                     MigrationTypeValue] = ShapeBase.NOT_SET,
        table_mappings: str = ShapeBase.NOT_SET,
        replication_task_settings: str = ShapeBase.NOT_SET,
        cdc_start_time: datetime.datetime = ShapeBase.NOT_SET,
        cdc_start_position: str = ShapeBase.NOT_SET,
        cdc_stop_position: str = ShapeBase.NOT_SET,
    ) -> shapes.ModifyReplicationTaskResponse:
        """
        Modifies the specified replication task.

        You can't modify the task endpoints. The task must be stopped before you can
        modify it.

        For more information about AWS DMS tasks, see the AWS DMS user guide at [
        Working with Migration Tasks
        ](http://docs.aws.amazon.com/dms/latest/userguide/CHAP_Tasks.html)
        """
        if _request is None:
            _params = {}
            if replication_task_arn is not ShapeBase.NOT_SET:
                _params['replication_task_arn'] = replication_task_arn
            if replication_task_identifier is not ShapeBase.NOT_SET:
                _params['replication_task_identifier'
                       ] = replication_task_identifier
            if migration_type is not ShapeBase.NOT_SET:
                _params['migration_type'] = migration_type
            if table_mappings is not ShapeBase.NOT_SET:
                _params['table_mappings'] = table_mappings
            if replication_task_settings is not ShapeBase.NOT_SET:
                _params['replication_task_settings'] = replication_task_settings
            if cdc_start_time is not ShapeBase.NOT_SET:
                _params['cdc_start_time'] = cdc_start_time
            if cdc_start_position is not ShapeBase.NOT_SET:
                _params['cdc_start_position'] = cdc_start_position
            if cdc_stop_position is not ShapeBase.NOT_SET:
                _params['cdc_stop_position'] = cdc_stop_position
            _request = shapes.ModifyReplicationTaskMessage(**_params)
        response = self._boto_client.modify_replication_task(
            **_request.to_boto()
        )

        return shapes.ModifyReplicationTaskResponse.from_boto(response)

    def reboot_replication_instance(
        self,
        _request: shapes.RebootReplicationInstanceMessage = None,
        *,
        replication_instance_arn: str,
        force_failover: bool = ShapeBase.NOT_SET,
    ) -> shapes.RebootReplicationInstanceResponse:
        """
        Reboots a replication instance. Rebooting results in a momentary outage, until
        the replication instance becomes available again.
        """
        if _request is None:
            _params = {}
            if replication_instance_arn is not ShapeBase.NOT_SET:
                _params['replication_instance_arn'] = replication_instance_arn
            if force_failover is not ShapeBase.NOT_SET:
                _params['force_failover'] = force_failover
            _request = shapes.RebootReplicationInstanceMessage(**_params)
        response = self._boto_client.reboot_replication_instance(
            **_request.to_boto()
        )

        return shapes.RebootReplicationInstanceResponse.from_boto(response)

    def refresh_schemas(
        self,
        _request: shapes.RefreshSchemasMessage = None,
        *,
        endpoint_arn: str,
        replication_instance_arn: str,
    ) -> shapes.RefreshSchemasResponse:
        """
        Populates the schema for the specified endpoint. This is an asynchronous
        operation and can take several minutes. You can check the status of this
        operation by calling the DescribeRefreshSchemasStatus operation.
        """
        if _request is None:
            _params = {}
            if endpoint_arn is not ShapeBase.NOT_SET:
                _params['endpoint_arn'] = endpoint_arn
            if replication_instance_arn is not ShapeBase.NOT_SET:
                _params['replication_instance_arn'] = replication_instance_arn
            _request = shapes.RefreshSchemasMessage(**_params)
        response = self._boto_client.refresh_schemas(**_request.to_boto())

        return shapes.RefreshSchemasResponse.from_boto(response)

    def reload_tables(
        self,
        _request: shapes.ReloadTablesMessage = None,
        *,
        replication_task_arn: str,
        tables_to_reload: typing.List[shapes.TableToReload],
        reload_option: typing.Union[str, shapes.ReloadOptionValue] = ShapeBase.
        NOT_SET,
    ) -> shapes.ReloadTablesResponse:
        """
        Reloads the target database table with the source data.
        """
        if _request is None:
            _params = {}
            if replication_task_arn is not ShapeBase.NOT_SET:
                _params['replication_task_arn'] = replication_task_arn
            if tables_to_reload is not ShapeBase.NOT_SET:
                _params['tables_to_reload'] = tables_to_reload
            if reload_option is not ShapeBase.NOT_SET:
                _params['reload_option'] = reload_option
            _request = shapes.ReloadTablesMessage(**_params)
        response = self._boto_client.reload_tables(**_request.to_boto())

        return shapes.ReloadTablesResponse.from_boto(response)

    def remove_tags_from_resource(
        self,
        _request: shapes.RemoveTagsFromResourceMessage = None,
        *,
        resource_arn: str,
        tag_keys: typing.List[str],
    ) -> shapes.RemoveTagsFromResourceResponse:
        """
        Removes metadata tags from a DMS resource.
        """
        if _request is None:
            _params = {}
            if resource_arn is not ShapeBase.NOT_SET:
                _params['resource_arn'] = resource_arn
            if tag_keys is not ShapeBase.NOT_SET:
                _params['tag_keys'] = tag_keys
            _request = shapes.RemoveTagsFromResourceMessage(**_params)
        response = self._boto_client.remove_tags_from_resource(
            **_request.to_boto()
        )

        return shapes.RemoveTagsFromResourceResponse.from_boto(response)

    def start_replication_task(
        self,
        _request: shapes.StartReplicationTaskMessage = None,
        *,
        replication_task_arn: str,
        start_replication_task_type: typing.
        Union[str, shapes.StartReplicationTaskTypeValue],
        cdc_start_time: datetime.datetime = ShapeBase.NOT_SET,
        cdc_start_position: str = ShapeBase.NOT_SET,
        cdc_stop_position: str = ShapeBase.NOT_SET,
    ) -> shapes.StartReplicationTaskResponse:
        """
        Starts the replication task.

        For more information about AWS DMS tasks, see the AWS DMS user guide at [
        Working with Migration Tasks
        ](http://docs.aws.amazon.com/dms/latest/userguide/CHAP_Tasks.html)
        """
        if _request is None:
            _params = {}
            if replication_task_arn is not ShapeBase.NOT_SET:
                _params['replication_task_arn'] = replication_task_arn
            if start_replication_task_type is not ShapeBase.NOT_SET:
                _params['start_replication_task_type'
                       ] = start_replication_task_type
            if cdc_start_time is not ShapeBase.NOT_SET:
                _params['cdc_start_time'] = cdc_start_time
            if cdc_start_position is not ShapeBase.NOT_SET:
                _params['cdc_start_position'] = cdc_start_position
            if cdc_stop_position is not ShapeBase.NOT_SET:
                _params['cdc_stop_position'] = cdc_stop_position
            _request = shapes.StartReplicationTaskMessage(**_params)
        response = self._boto_client.start_replication_task(
            **_request.to_boto()
        )

        return shapes.StartReplicationTaskResponse.from_boto(response)

    def start_replication_task_assessment(
        self,
        _request: shapes.StartReplicationTaskAssessmentMessage = None,
        *,
        replication_task_arn: str,
    ) -> shapes.StartReplicationTaskAssessmentResponse:
        """
        Starts the replication task assessment for unsupported data types in the source
        database.
        """
        if _request is None:
            _params = {}
            if replication_task_arn is not ShapeBase.NOT_SET:
                _params['replication_task_arn'] = replication_task_arn
            _request = shapes.StartReplicationTaskAssessmentMessage(**_params)
        response = self._boto_client.start_replication_task_assessment(
            **_request.to_boto()
        )

        return shapes.StartReplicationTaskAssessmentResponse.from_boto(response)

    def stop_replication_task(
        self,
        _request: shapes.StopReplicationTaskMessage = None,
        *,
        replication_task_arn: str,
    ) -> shapes.StopReplicationTaskResponse:
        """
        Stops the replication task.
        """
        if _request is None:
            _params = {}
            if replication_task_arn is not ShapeBase.NOT_SET:
                _params['replication_task_arn'] = replication_task_arn
            _request = shapes.StopReplicationTaskMessage(**_params)
        response = self._boto_client.stop_replication_task(**_request.to_boto())

        return shapes.StopReplicationTaskResponse.from_boto(response)

    def test_connection(
        self,
        _request: shapes.TestConnectionMessage = None,
        *,
        replication_instance_arn: str,
        endpoint_arn: str,
    ) -> shapes.TestConnectionResponse:
        """
        Tests the connection between the replication instance and the endpoint.
        """
        if _request is None:
            _params = {}
            if replication_instance_arn is not ShapeBase.NOT_SET:
                _params['replication_instance_arn'] = replication_instance_arn
            if endpoint_arn is not ShapeBase.NOT_SET:
                _params['endpoint_arn'] = endpoint_arn
            _request = shapes.TestConnectionMessage(**_params)
        response = self._boto_client.test_connection(**_request.to_boto())

        return shapes.TestConnectionResponse.from_boto(response)
