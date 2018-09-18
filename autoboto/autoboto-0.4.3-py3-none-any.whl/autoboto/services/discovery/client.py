import datetime
import typing
import boto3
from autoboto import ClientBase, ShapeBase, OutputShapeBase
from . import shapes


class Client(ClientBase):
    def __init__(self, *args, **kwargs):
        super().__init__("discovery", *args, **kwargs)

    def associate_configuration_items_to_application(
        self,
        _request: shapes.AssociateConfigurationItemsToApplicationRequest = None,
        *,
        application_configuration_id: str,
        configuration_ids: typing.List[str],
    ) -> shapes.AssociateConfigurationItemsToApplicationResponse:
        """
        Associates one or more configuration items with an application.
        """
        if _request is None:
            _params = {}
            if application_configuration_id is not ShapeBase.NOT_SET:
                _params['application_configuration_id'
                       ] = application_configuration_id
            if configuration_ids is not ShapeBase.NOT_SET:
                _params['configuration_ids'] = configuration_ids
            _request = shapes.AssociateConfigurationItemsToApplicationRequest(
                **_params
            )
        response = self._boto_client.associate_configuration_items_to_application(
            **_request.to_boto()
        )

        return shapes.AssociateConfigurationItemsToApplicationResponse.from_boto(
            response
        )

    def create_application(
        self,
        _request: shapes.CreateApplicationRequest = None,
        *,
        name: str,
        description: str = ShapeBase.NOT_SET,
    ) -> shapes.CreateApplicationResponse:
        """
        Creates an application with the given name and description.
        """
        if _request is None:
            _params = {}
            if name is not ShapeBase.NOT_SET:
                _params['name'] = name
            if description is not ShapeBase.NOT_SET:
                _params['description'] = description
            _request = shapes.CreateApplicationRequest(**_params)
        response = self._boto_client.create_application(**_request.to_boto())

        return shapes.CreateApplicationResponse.from_boto(response)

    def create_tags(
        self,
        _request: shapes.CreateTagsRequest = None,
        *,
        configuration_ids: typing.List[str],
        tags: typing.List[shapes.Tag],
    ) -> shapes.CreateTagsResponse:
        """
        Creates one or more tags for configuration items. Tags are metadata that help
        you categorize IT assets. This API accepts a list of multiple configuration
        items.
        """
        if _request is None:
            _params = {}
            if configuration_ids is not ShapeBase.NOT_SET:
                _params['configuration_ids'] = configuration_ids
            if tags is not ShapeBase.NOT_SET:
                _params['tags'] = tags
            _request = shapes.CreateTagsRequest(**_params)
        response = self._boto_client.create_tags(**_request.to_boto())

        return shapes.CreateTagsResponse.from_boto(response)

    def delete_applications(
        self,
        _request: shapes.DeleteApplicationsRequest = None,
        *,
        configuration_ids: typing.List[str],
    ) -> shapes.DeleteApplicationsResponse:
        """
        Deletes a list of applications and their associations with configuration items.
        """
        if _request is None:
            _params = {}
            if configuration_ids is not ShapeBase.NOT_SET:
                _params['configuration_ids'] = configuration_ids
            _request = shapes.DeleteApplicationsRequest(**_params)
        response = self._boto_client.delete_applications(**_request.to_boto())

        return shapes.DeleteApplicationsResponse.from_boto(response)

    def delete_tags(
        self,
        _request: shapes.DeleteTagsRequest = None,
        *,
        configuration_ids: typing.List[str],
        tags: typing.List[shapes.Tag] = ShapeBase.NOT_SET,
    ) -> shapes.DeleteTagsResponse:
        """
        Deletes the association between configuration items and one or more tags. This
        API accepts a list of multiple configuration items.
        """
        if _request is None:
            _params = {}
            if configuration_ids is not ShapeBase.NOT_SET:
                _params['configuration_ids'] = configuration_ids
            if tags is not ShapeBase.NOT_SET:
                _params['tags'] = tags
            _request = shapes.DeleteTagsRequest(**_params)
        response = self._boto_client.delete_tags(**_request.to_boto())

        return shapes.DeleteTagsResponse.from_boto(response)

    def describe_agents(
        self,
        _request: shapes.DescribeAgentsRequest = None,
        *,
        agent_ids: typing.List[str] = ShapeBase.NOT_SET,
        filters: typing.List[shapes.Filter] = ShapeBase.NOT_SET,
        max_results: int = ShapeBase.NOT_SET,
        next_token: str = ShapeBase.NOT_SET,
    ) -> shapes.DescribeAgentsResponse:
        """
        Lists agents or connectors as specified by ID or other filters. All
        agents/connectors associated with your user account can be listed if you call
        `DescribeAgents` as is without passing any parameters.
        """
        if _request is None:
            _params = {}
            if agent_ids is not ShapeBase.NOT_SET:
                _params['agent_ids'] = agent_ids
            if filters is not ShapeBase.NOT_SET:
                _params['filters'] = filters
            if max_results is not ShapeBase.NOT_SET:
                _params['max_results'] = max_results
            if next_token is not ShapeBase.NOT_SET:
                _params['next_token'] = next_token
            _request = shapes.DescribeAgentsRequest(**_params)
        response = self._boto_client.describe_agents(**_request.to_boto())

        return shapes.DescribeAgentsResponse.from_boto(response)

    def describe_configurations(
        self,
        _request: shapes.DescribeConfigurationsRequest = None,
        *,
        configuration_ids: typing.List[str],
    ) -> shapes.DescribeConfigurationsResponse:
        """
        Retrieves attributes for a list of configuration item IDs.

        All of the supplied IDs must be for the same asset type from one of the
        follwoing:

          * server

          * application

          * process

          * connection

        Output fields are specific to the asset type specified. For example, the output
        for a _server_ configuration item includes a list of attributes about the
        server, such as host name, operating system, number of network cards, etc.

        For a complete list of outputs for each asset type, see [Using the
        DescribeConfigurations Action](http://docs.aws.amazon.com/application-
        discovery/latest/APIReference/discovery-api-
        queries.html#DescribeConfigurations).
        """
        if _request is None:
            _params = {}
            if configuration_ids is not ShapeBase.NOT_SET:
                _params['configuration_ids'] = configuration_ids
            _request = shapes.DescribeConfigurationsRequest(**_params)
        response = self._boto_client.describe_configurations(
            **_request.to_boto()
        )

        return shapes.DescribeConfigurationsResponse.from_boto(response)

    def describe_continuous_exports(
        self,
        _request: shapes.DescribeContinuousExportsRequest = None,
        *,
        export_ids: typing.List[str] = ShapeBase.NOT_SET,
        max_results: int = ShapeBase.NOT_SET,
        next_token: str = ShapeBase.NOT_SET,
    ) -> shapes.DescribeContinuousExportsResponse:
        """
        Lists exports as specified by ID. All continuous exports associated with your
        user account can be listed if you call `DescribeContinuousExports` as is without
        passing any parameters.
        """
        if _request is None:
            _params = {}
            if export_ids is not ShapeBase.NOT_SET:
                _params['export_ids'] = export_ids
            if max_results is not ShapeBase.NOT_SET:
                _params['max_results'] = max_results
            if next_token is not ShapeBase.NOT_SET:
                _params['next_token'] = next_token
            _request = shapes.DescribeContinuousExportsRequest(**_params)
        response = self._boto_client.describe_continuous_exports(
            **_request.to_boto()
        )

        return shapes.DescribeContinuousExportsResponse.from_boto(response)

    def describe_export_configurations(
        self,
        _request: shapes.DescribeExportConfigurationsRequest = None,
        *,
        export_ids: typing.List[str] = ShapeBase.NOT_SET,
        max_results: int = ShapeBase.NOT_SET,
        next_token: str = ShapeBase.NOT_SET,
    ) -> shapes.DescribeExportConfigurationsResponse:
        """
        `DescribeExportConfigurations` is deprecated.

        Use instead [ `DescribeExportTasks` ](http://docs.aws.amazon.com/application-
        discovery/latest/APIReference/API_DescribeExportTasks.html).
        """
        if _request is None:
            _params = {}
            if export_ids is not ShapeBase.NOT_SET:
                _params['export_ids'] = export_ids
            if max_results is not ShapeBase.NOT_SET:
                _params['max_results'] = max_results
            if next_token is not ShapeBase.NOT_SET:
                _params['next_token'] = next_token
            _request = shapes.DescribeExportConfigurationsRequest(**_params)
        response = self._boto_client.describe_export_configurations(
            **_request.to_boto()
        )

        return shapes.DescribeExportConfigurationsResponse.from_boto(response)

    def describe_export_tasks(
        self,
        _request: shapes.DescribeExportTasksRequest = None,
        *,
        export_ids: typing.List[str] = ShapeBase.NOT_SET,
        filters: typing.List[shapes.ExportFilter] = ShapeBase.NOT_SET,
        max_results: int = ShapeBase.NOT_SET,
        next_token: str = ShapeBase.NOT_SET,
    ) -> shapes.DescribeExportTasksResponse:
        """
        Retrieve status of one or more export tasks. You can retrieve the status of up
        to 100 export tasks.
        """
        if _request is None:
            _params = {}
            if export_ids is not ShapeBase.NOT_SET:
                _params['export_ids'] = export_ids
            if filters is not ShapeBase.NOT_SET:
                _params['filters'] = filters
            if max_results is not ShapeBase.NOT_SET:
                _params['max_results'] = max_results
            if next_token is not ShapeBase.NOT_SET:
                _params['next_token'] = next_token
            _request = shapes.DescribeExportTasksRequest(**_params)
        response = self._boto_client.describe_export_tasks(**_request.to_boto())

        return shapes.DescribeExportTasksResponse.from_boto(response)

    def describe_tags(
        self,
        _request: shapes.DescribeTagsRequest = None,
        *,
        filters: typing.List[shapes.TagFilter] = ShapeBase.NOT_SET,
        max_results: int = ShapeBase.NOT_SET,
        next_token: str = ShapeBase.NOT_SET,
    ) -> shapes.DescribeTagsResponse:
        """
        Retrieves a list of configuration items that have tags as specified by the key-
        value pairs, name and value, passed to the optional parameter `filters`.

        There are three valid tag filter names:

          * tagKey

          * tagValue

          * configurationId

        Also, all configuration items associated with your user account that have tags
        can be listed if you call `DescribeTags` as is without passing any parameters.
        """
        if _request is None:
            _params = {}
            if filters is not ShapeBase.NOT_SET:
                _params['filters'] = filters
            if max_results is not ShapeBase.NOT_SET:
                _params['max_results'] = max_results
            if next_token is not ShapeBase.NOT_SET:
                _params['next_token'] = next_token
            _request = shapes.DescribeTagsRequest(**_params)
        response = self._boto_client.describe_tags(**_request.to_boto())

        return shapes.DescribeTagsResponse.from_boto(response)

    def disassociate_configuration_items_from_application(
        self,
        _request: shapes.
        DisassociateConfigurationItemsFromApplicationRequest = None,
        *,
        application_configuration_id: str,
        configuration_ids: typing.List[str],
    ) -> shapes.DisassociateConfigurationItemsFromApplicationResponse:
        """
        Disassociates one or more configuration items from an application.
        """
        if _request is None:
            _params = {}
            if application_configuration_id is not ShapeBase.NOT_SET:
                _params['application_configuration_id'
                       ] = application_configuration_id
            if configuration_ids is not ShapeBase.NOT_SET:
                _params['configuration_ids'] = configuration_ids
            _request = shapes.DisassociateConfigurationItemsFromApplicationRequest(
                **_params
            )
        response = self._boto_client.disassociate_configuration_items_from_application(
            **_request.to_boto()
        )

        return shapes.DisassociateConfigurationItemsFromApplicationResponse.from_boto(
            response
        )

    def export_configurations(self, ) -> shapes.ExportConfigurationsResponse:
        """
        Deprecated. Use `StartExportTask` instead.

        Exports all discovered configuration data to an Amazon S3 bucket or an
        application that enables you to view and evaluate the data. Data includes tags
        and tag associations, processes, connections, servers, and system performance.
        This API returns an export ID that you can query using the
        _DescribeExportConfigurations_ API. The system imposes a limit of two
        configuration exports in six hours.
        """
        response = self._boto_client.export_configurations()

        return shapes.ExportConfigurationsResponse.from_boto(response)

    def get_discovery_summary(
        self,
        _request: shapes.GetDiscoverySummaryRequest = None,
    ) -> shapes.GetDiscoverySummaryResponse:
        """
        Retrieves a short summary of discovered assets.

        This API operation takes no request parameters and is called as is at the
        command prompt as shown in the example.
        """
        if _request is None:
            _params = {}
            _request = shapes.GetDiscoverySummaryRequest(**_params)
        response = self._boto_client.get_discovery_summary(**_request.to_boto())

        return shapes.GetDiscoverySummaryResponse.from_boto(response)

    def list_configurations(
        self,
        _request: shapes.ListConfigurationsRequest = None,
        *,
        configuration_type: typing.Union[str, shapes.ConfigurationItemType],
        filters: typing.List[shapes.Filter] = ShapeBase.NOT_SET,
        max_results: int = ShapeBase.NOT_SET,
        next_token: str = ShapeBase.NOT_SET,
        order_by: typing.List[shapes.OrderByElement] = ShapeBase.NOT_SET,
    ) -> shapes.ListConfigurationsResponse:
        """
        Retrieves a list of configuration items as specified by the value passed to the
        required paramater `configurationType`. Optional filtering may be applied to
        refine search results.
        """
        if _request is None:
            _params = {}
            if configuration_type is not ShapeBase.NOT_SET:
                _params['configuration_type'] = configuration_type
            if filters is not ShapeBase.NOT_SET:
                _params['filters'] = filters
            if max_results is not ShapeBase.NOT_SET:
                _params['max_results'] = max_results
            if next_token is not ShapeBase.NOT_SET:
                _params['next_token'] = next_token
            if order_by is not ShapeBase.NOT_SET:
                _params['order_by'] = order_by
            _request = shapes.ListConfigurationsRequest(**_params)
        response = self._boto_client.list_configurations(**_request.to_boto())

        return shapes.ListConfigurationsResponse.from_boto(response)

    def list_server_neighbors(
        self,
        _request: shapes.ListServerNeighborsRequest = None,
        *,
        configuration_id: str,
        port_information_needed: bool = ShapeBase.NOT_SET,
        neighbor_configuration_ids: typing.List[str] = ShapeBase.NOT_SET,
        max_results: int = ShapeBase.NOT_SET,
        next_token: str = ShapeBase.NOT_SET,
    ) -> shapes.ListServerNeighborsResponse:
        """
        Retrieves a list of servers that are one network hop away from a specified
        server.
        """
        if _request is None:
            _params = {}
            if configuration_id is not ShapeBase.NOT_SET:
                _params['configuration_id'] = configuration_id
            if port_information_needed is not ShapeBase.NOT_SET:
                _params['port_information_needed'] = port_information_needed
            if neighbor_configuration_ids is not ShapeBase.NOT_SET:
                _params['neighbor_configuration_ids'
                       ] = neighbor_configuration_ids
            if max_results is not ShapeBase.NOT_SET:
                _params['max_results'] = max_results
            if next_token is not ShapeBase.NOT_SET:
                _params['next_token'] = next_token
            _request = shapes.ListServerNeighborsRequest(**_params)
        response = self._boto_client.list_server_neighbors(**_request.to_boto())

        return shapes.ListServerNeighborsResponse.from_boto(response)

    def start_continuous_export(
        self,
        _request: shapes.StartContinuousExportRequest = None,
    ) -> shapes.StartContinuousExportResponse:
        """
        Start the continuous flow of agent's discovered data into Amazon Athena.
        """
        if _request is None:
            _params = {}
            _request = shapes.StartContinuousExportRequest(**_params)
        response = self._boto_client.start_continuous_export(
            **_request.to_boto()
        )

        return shapes.StartContinuousExportResponse.from_boto(response)

    def start_data_collection_by_agent_ids(
        self,
        _request: shapes.StartDataCollectionByAgentIdsRequest = None,
        *,
        agent_ids: typing.List[str],
    ) -> shapes.StartDataCollectionByAgentIdsResponse:
        """
        Instructs the specified agents or connectors to start collecting data.
        """
        if _request is None:
            _params = {}
            if agent_ids is not ShapeBase.NOT_SET:
                _params['agent_ids'] = agent_ids
            _request = shapes.StartDataCollectionByAgentIdsRequest(**_params)
        response = self._boto_client.start_data_collection_by_agent_ids(
            **_request.to_boto()
        )

        return shapes.StartDataCollectionByAgentIdsResponse.from_boto(response)

    def start_export_task(
        self,
        _request: shapes.StartExportTaskRequest = None,
        *,
        export_data_format: typing.List[
            typing.Union[str, shapes.ExportDataFormat]] = ShapeBase.NOT_SET,
        filters: typing.List[shapes.ExportFilter] = ShapeBase.NOT_SET,
        start_time: datetime.datetime = ShapeBase.NOT_SET,
        end_time: datetime.datetime = ShapeBase.NOT_SET,
    ) -> shapes.StartExportTaskResponse:
        """
        Begins the export of discovered data to an S3 bucket.

        If you specify `agentIds` in a filter, the task exports up to 72 hours of
        detailed data collected by the identified Application Discovery Agent, including
        network, process, and performance details. A time range for exported agent data
        may be set by using `startTime` and `endTime`. Export of detailed agent data is
        limited to five concurrently running exports.

        If you do not include an `agentIds` filter, summary data is exported that
        includes both AWS Agentless Discovery Connector data and summary data from AWS
        Discovery Agents. Export of summary data is limited to two exports per day.
        """
        if _request is None:
            _params = {}
            if export_data_format is not ShapeBase.NOT_SET:
                _params['export_data_format'] = export_data_format
            if filters is not ShapeBase.NOT_SET:
                _params['filters'] = filters
            if start_time is not ShapeBase.NOT_SET:
                _params['start_time'] = start_time
            if end_time is not ShapeBase.NOT_SET:
                _params['end_time'] = end_time
            _request = shapes.StartExportTaskRequest(**_params)
        response = self._boto_client.start_export_task(**_request.to_boto())

        return shapes.StartExportTaskResponse.from_boto(response)

    def stop_continuous_export(
        self,
        _request: shapes.StopContinuousExportRequest = None,
        *,
        export_id: str,
    ) -> shapes.StopContinuousExportResponse:
        """
        Stop the continuous flow of agent's discovered data into Amazon Athena.
        """
        if _request is None:
            _params = {}
            if export_id is not ShapeBase.NOT_SET:
                _params['export_id'] = export_id
            _request = shapes.StopContinuousExportRequest(**_params)
        response = self._boto_client.stop_continuous_export(
            **_request.to_boto()
        )

        return shapes.StopContinuousExportResponse.from_boto(response)

    def stop_data_collection_by_agent_ids(
        self,
        _request: shapes.StopDataCollectionByAgentIdsRequest = None,
        *,
        agent_ids: typing.List[str],
    ) -> shapes.StopDataCollectionByAgentIdsResponse:
        """
        Instructs the specified agents or connectors to stop collecting data.
        """
        if _request is None:
            _params = {}
            if agent_ids is not ShapeBase.NOT_SET:
                _params['agent_ids'] = agent_ids
            _request = shapes.StopDataCollectionByAgentIdsRequest(**_params)
        response = self._boto_client.stop_data_collection_by_agent_ids(
            **_request.to_boto()
        )

        return shapes.StopDataCollectionByAgentIdsResponse.from_boto(response)

    def update_application(
        self,
        _request: shapes.UpdateApplicationRequest = None,
        *,
        configuration_id: str,
        name: str = ShapeBase.NOT_SET,
        description: str = ShapeBase.NOT_SET,
    ) -> shapes.UpdateApplicationResponse:
        """
        Updates metadata about an application.
        """
        if _request is None:
            _params = {}
            if configuration_id is not ShapeBase.NOT_SET:
                _params['configuration_id'] = configuration_id
            if name is not ShapeBase.NOT_SET:
                _params['name'] = name
            if description is not ShapeBase.NOT_SET:
                _params['description'] = description
            _request = shapes.UpdateApplicationRequest(**_params)
        response = self._boto_client.update_application(**_request.to_boto())

        return shapes.UpdateApplicationResponse.from_boto(response)
