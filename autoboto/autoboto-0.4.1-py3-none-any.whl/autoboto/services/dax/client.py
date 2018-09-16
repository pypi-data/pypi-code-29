import datetime
import typing
import boto3
from autoboto import ClientBase, ShapeBase, OutputShapeBase
from . import shapes


class Client(ClientBase):
    def __init__(self, *args, **kwargs):
        super().__init__("dax", *args, **kwargs)

    def create_cluster(
        self,
        _request: shapes.CreateClusterRequest = None,
        *,
        cluster_name: str,
        node_type: str,
        replication_factor: int,
        iam_role_arn: str,
        description: str = ShapeBase.NOT_SET,
        availability_zones: typing.List[str] = ShapeBase.NOT_SET,
        subnet_group_name: str = ShapeBase.NOT_SET,
        security_group_ids: typing.List[str] = ShapeBase.NOT_SET,
        preferred_maintenance_window: str = ShapeBase.NOT_SET,
        notification_topic_arn: str = ShapeBase.NOT_SET,
        parameter_group_name: str = ShapeBase.NOT_SET,
        tags: typing.List[shapes.Tag] = ShapeBase.NOT_SET,
        sse_specification: shapes.SSESpecification = ShapeBase.NOT_SET,
    ) -> shapes.CreateClusterResponse:
        """
        Creates a DAX cluster. All nodes in the cluster run the same DAX caching
        software.
        """
        if _request is None:
            _params = {}
            if cluster_name is not ShapeBase.NOT_SET:
                _params['cluster_name'] = cluster_name
            if node_type is not ShapeBase.NOT_SET:
                _params['node_type'] = node_type
            if replication_factor is not ShapeBase.NOT_SET:
                _params['replication_factor'] = replication_factor
            if iam_role_arn is not ShapeBase.NOT_SET:
                _params['iam_role_arn'] = iam_role_arn
            if description is not ShapeBase.NOT_SET:
                _params['description'] = description
            if availability_zones is not ShapeBase.NOT_SET:
                _params['availability_zones'] = availability_zones
            if subnet_group_name is not ShapeBase.NOT_SET:
                _params['subnet_group_name'] = subnet_group_name
            if security_group_ids is not ShapeBase.NOT_SET:
                _params['security_group_ids'] = security_group_ids
            if preferred_maintenance_window is not ShapeBase.NOT_SET:
                _params['preferred_maintenance_window'
                       ] = preferred_maintenance_window
            if notification_topic_arn is not ShapeBase.NOT_SET:
                _params['notification_topic_arn'] = notification_topic_arn
            if parameter_group_name is not ShapeBase.NOT_SET:
                _params['parameter_group_name'] = parameter_group_name
            if tags is not ShapeBase.NOT_SET:
                _params['tags'] = tags
            if sse_specification is not ShapeBase.NOT_SET:
                _params['sse_specification'] = sse_specification
            _request = shapes.CreateClusterRequest(**_params)
        response = self._boto_client.create_cluster(**_request.to_boto())

        return shapes.CreateClusterResponse.from_boto(response)

    def create_parameter_group(
        self,
        _request: shapes.CreateParameterGroupRequest = None,
        *,
        parameter_group_name: str,
        description: str = ShapeBase.NOT_SET,
    ) -> shapes.CreateParameterGroupResponse:
        """
        Creates a new parameter group. A parameter group is a collection of parameters
        that you apply to all of the nodes in a DAX cluster.
        """
        if _request is None:
            _params = {}
            if parameter_group_name is not ShapeBase.NOT_SET:
                _params['parameter_group_name'] = parameter_group_name
            if description is not ShapeBase.NOT_SET:
                _params['description'] = description
            _request = shapes.CreateParameterGroupRequest(**_params)
        response = self._boto_client.create_parameter_group(
            **_request.to_boto()
        )

        return shapes.CreateParameterGroupResponse.from_boto(response)

    def create_subnet_group(
        self,
        _request: shapes.CreateSubnetGroupRequest = None,
        *,
        subnet_group_name: str,
        subnet_ids: typing.List[str],
        description: str = ShapeBase.NOT_SET,
    ) -> shapes.CreateSubnetGroupResponse:
        """
        Creates a new subnet group.
        """
        if _request is None:
            _params = {}
            if subnet_group_name is not ShapeBase.NOT_SET:
                _params['subnet_group_name'] = subnet_group_name
            if subnet_ids is not ShapeBase.NOT_SET:
                _params['subnet_ids'] = subnet_ids
            if description is not ShapeBase.NOT_SET:
                _params['description'] = description
            _request = shapes.CreateSubnetGroupRequest(**_params)
        response = self._boto_client.create_subnet_group(**_request.to_boto())

        return shapes.CreateSubnetGroupResponse.from_boto(response)

    def decrease_replication_factor(
        self,
        _request: shapes.DecreaseReplicationFactorRequest = None,
        *,
        cluster_name: str,
        new_replication_factor: int,
        availability_zones: typing.List[str] = ShapeBase.NOT_SET,
        node_ids_to_remove: typing.List[str] = ShapeBase.NOT_SET,
    ) -> shapes.DecreaseReplicationFactorResponse:
        """
        Removes one or more nodes from a DAX cluster.

        You cannot use `DecreaseReplicationFactor` to remove the last node in a DAX
        cluster. If you need to do this, use `DeleteCluster` instead.
        """
        if _request is None:
            _params = {}
            if cluster_name is not ShapeBase.NOT_SET:
                _params['cluster_name'] = cluster_name
            if new_replication_factor is not ShapeBase.NOT_SET:
                _params['new_replication_factor'] = new_replication_factor
            if availability_zones is not ShapeBase.NOT_SET:
                _params['availability_zones'] = availability_zones
            if node_ids_to_remove is not ShapeBase.NOT_SET:
                _params['node_ids_to_remove'] = node_ids_to_remove
            _request = shapes.DecreaseReplicationFactorRequest(**_params)
        response = self._boto_client.decrease_replication_factor(
            **_request.to_boto()
        )

        return shapes.DecreaseReplicationFactorResponse.from_boto(response)

    def delete_cluster(
        self,
        _request: shapes.DeleteClusterRequest = None,
        *,
        cluster_name: str,
    ) -> shapes.DeleteClusterResponse:
        """
        Deletes a previously provisioned DAX cluster. _DeleteCluster_ deletes all
        associated nodes, node endpoints and the DAX cluster itself. When you receive a
        successful response from this action, DAX immediately begins deleting the
        cluster; you cannot cancel or revert this action.
        """
        if _request is None:
            _params = {}
            if cluster_name is not ShapeBase.NOT_SET:
                _params['cluster_name'] = cluster_name
            _request = shapes.DeleteClusterRequest(**_params)
        response = self._boto_client.delete_cluster(**_request.to_boto())

        return shapes.DeleteClusterResponse.from_boto(response)

    def delete_parameter_group(
        self,
        _request: shapes.DeleteParameterGroupRequest = None,
        *,
        parameter_group_name: str,
    ) -> shapes.DeleteParameterGroupResponse:
        """
        Deletes the specified parameter group. You cannot delete a parameter group if it
        is associated with any DAX clusters.
        """
        if _request is None:
            _params = {}
            if parameter_group_name is not ShapeBase.NOT_SET:
                _params['parameter_group_name'] = parameter_group_name
            _request = shapes.DeleteParameterGroupRequest(**_params)
        response = self._boto_client.delete_parameter_group(
            **_request.to_boto()
        )

        return shapes.DeleteParameterGroupResponse.from_boto(response)

    def delete_subnet_group(
        self,
        _request: shapes.DeleteSubnetGroupRequest = None,
        *,
        subnet_group_name: str,
    ) -> shapes.DeleteSubnetGroupResponse:
        """
        Deletes a subnet group.

        You cannot delete a subnet group if it is associated with any DAX clusters.
        """
        if _request is None:
            _params = {}
            if subnet_group_name is not ShapeBase.NOT_SET:
                _params['subnet_group_name'] = subnet_group_name
            _request = shapes.DeleteSubnetGroupRequest(**_params)
        response = self._boto_client.delete_subnet_group(**_request.to_boto())

        return shapes.DeleteSubnetGroupResponse.from_boto(response)

    def describe_clusters(
        self,
        _request: shapes.DescribeClustersRequest = None,
        *,
        cluster_names: typing.List[str] = ShapeBase.NOT_SET,
        max_results: int = ShapeBase.NOT_SET,
        next_token: str = ShapeBase.NOT_SET,
    ) -> shapes.DescribeClustersResponse:
        """
        Returns information about all provisioned DAX clusters if no cluster identifier
        is specified, or about a specific DAX cluster if a cluster identifier is
        supplied.

        If the cluster is in the CREATING state, only cluster level information will be
        displayed until all of the nodes are successfully provisioned.

        If the cluster is in the DELETING state, only cluster level information will be
        displayed.

        If nodes are currently being added to the DAX cluster, node endpoint information
        and creation time for the additional nodes will not be displayed until they are
        completely provisioned. When the DAX cluster state is _available_ , the cluster
        is ready for use.

        If nodes are currently being removed from the DAX cluster, no endpoint
        information for the removed nodes is displayed.
        """
        if _request is None:
            _params = {}
            if cluster_names is not ShapeBase.NOT_SET:
                _params['cluster_names'] = cluster_names
            if max_results is not ShapeBase.NOT_SET:
                _params['max_results'] = max_results
            if next_token is not ShapeBase.NOT_SET:
                _params['next_token'] = next_token
            _request = shapes.DescribeClustersRequest(**_params)
        response = self._boto_client.describe_clusters(**_request.to_boto())

        return shapes.DescribeClustersResponse.from_boto(response)

    def describe_default_parameters(
        self,
        _request: shapes.DescribeDefaultParametersRequest = None,
        *,
        max_results: int = ShapeBase.NOT_SET,
        next_token: str = ShapeBase.NOT_SET,
    ) -> shapes.DescribeDefaultParametersResponse:
        """
        Returns the default system parameter information for the DAX caching software.
        """
        if _request is None:
            _params = {}
            if max_results is not ShapeBase.NOT_SET:
                _params['max_results'] = max_results
            if next_token is not ShapeBase.NOT_SET:
                _params['next_token'] = next_token
            _request = shapes.DescribeDefaultParametersRequest(**_params)
        response = self._boto_client.describe_default_parameters(
            **_request.to_boto()
        )

        return shapes.DescribeDefaultParametersResponse.from_boto(response)

    def describe_events(
        self,
        _request: shapes.DescribeEventsRequest = None,
        *,
        source_name: str = ShapeBase.NOT_SET,
        source_type: typing.Union[str, shapes.SourceType] = ShapeBase.NOT_SET,
        start_time: datetime.datetime = ShapeBase.NOT_SET,
        end_time: datetime.datetime = ShapeBase.NOT_SET,
        duration: int = ShapeBase.NOT_SET,
        max_results: int = ShapeBase.NOT_SET,
        next_token: str = ShapeBase.NOT_SET,
    ) -> shapes.DescribeEventsResponse:
        """
        Returns events related to DAX clusters and parameter groups. You can obtain
        events specific to a particular DAX cluster or parameter group by providing the
        name as a parameter.

        By default, only the events occurring within the last hour are returned;
        however, you can retrieve up to 14 days' worth of events if necessary.
        """
        if _request is None:
            _params = {}
            if source_name is not ShapeBase.NOT_SET:
                _params['source_name'] = source_name
            if source_type is not ShapeBase.NOT_SET:
                _params['source_type'] = source_type
            if start_time is not ShapeBase.NOT_SET:
                _params['start_time'] = start_time
            if end_time is not ShapeBase.NOT_SET:
                _params['end_time'] = end_time
            if duration is not ShapeBase.NOT_SET:
                _params['duration'] = duration
            if max_results is not ShapeBase.NOT_SET:
                _params['max_results'] = max_results
            if next_token is not ShapeBase.NOT_SET:
                _params['next_token'] = next_token
            _request = shapes.DescribeEventsRequest(**_params)
        response = self._boto_client.describe_events(**_request.to_boto())

        return shapes.DescribeEventsResponse.from_boto(response)

    def describe_parameter_groups(
        self,
        _request: shapes.DescribeParameterGroupsRequest = None,
        *,
        parameter_group_names: typing.List[str] = ShapeBase.NOT_SET,
        max_results: int = ShapeBase.NOT_SET,
        next_token: str = ShapeBase.NOT_SET,
    ) -> shapes.DescribeParameterGroupsResponse:
        """
        Returns a list of parameter group descriptions. If a parameter group name is
        specified, the list will contain only the descriptions for that group.
        """
        if _request is None:
            _params = {}
            if parameter_group_names is not ShapeBase.NOT_SET:
                _params['parameter_group_names'] = parameter_group_names
            if max_results is not ShapeBase.NOT_SET:
                _params['max_results'] = max_results
            if next_token is not ShapeBase.NOT_SET:
                _params['next_token'] = next_token
            _request = shapes.DescribeParameterGroupsRequest(**_params)
        response = self._boto_client.describe_parameter_groups(
            **_request.to_boto()
        )

        return shapes.DescribeParameterGroupsResponse.from_boto(response)

    def describe_parameters(
        self,
        _request: shapes.DescribeParametersRequest = None,
        *,
        parameter_group_name: str,
        source: str = ShapeBase.NOT_SET,
        max_results: int = ShapeBase.NOT_SET,
        next_token: str = ShapeBase.NOT_SET,
    ) -> shapes.DescribeParametersResponse:
        """
        Returns the detailed parameter list for a particular parameter group.
        """
        if _request is None:
            _params = {}
            if parameter_group_name is not ShapeBase.NOT_SET:
                _params['parameter_group_name'] = parameter_group_name
            if source is not ShapeBase.NOT_SET:
                _params['source'] = source
            if max_results is not ShapeBase.NOT_SET:
                _params['max_results'] = max_results
            if next_token is not ShapeBase.NOT_SET:
                _params['next_token'] = next_token
            _request = shapes.DescribeParametersRequest(**_params)
        response = self._boto_client.describe_parameters(**_request.to_boto())

        return shapes.DescribeParametersResponse.from_boto(response)

    def describe_subnet_groups(
        self,
        _request: shapes.DescribeSubnetGroupsRequest = None,
        *,
        subnet_group_names: typing.List[str] = ShapeBase.NOT_SET,
        max_results: int = ShapeBase.NOT_SET,
        next_token: str = ShapeBase.NOT_SET,
    ) -> shapes.DescribeSubnetGroupsResponse:
        """
        Returns a list of subnet group descriptions. If a subnet group name is
        specified, the list will contain only the description of that group.
        """
        if _request is None:
            _params = {}
            if subnet_group_names is not ShapeBase.NOT_SET:
                _params['subnet_group_names'] = subnet_group_names
            if max_results is not ShapeBase.NOT_SET:
                _params['max_results'] = max_results
            if next_token is not ShapeBase.NOT_SET:
                _params['next_token'] = next_token
            _request = shapes.DescribeSubnetGroupsRequest(**_params)
        response = self._boto_client.describe_subnet_groups(
            **_request.to_boto()
        )

        return shapes.DescribeSubnetGroupsResponse.from_boto(response)

    def increase_replication_factor(
        self,
        _request: shapes.IncreaseReplicationFactorRequest = None,
        *,
        cluster_name: str,
        new_replication_factor: int,
        availability_zones: typing.List[str] = ShapeBase.NOT_SET,
    ) -> shapes.IncreaseReplicationFactorResponse:
        """
        Adds one or more nodes to a DAX cluster.
        """
        if _request is None:
            _params = {}
            if cluster_name is not ShapeBase.NOT_SET:
                _params['cluster_name'] = cluster_name
            if new_replication_factor is not ShapeBase.NOT_SET:
                _params['new_replication_factor'] = new_replication_factor
            if availability_zones is not ShapeBase.NOT_SET:
                _params['availability_zones'] = availability_zones
            _request = shapes.IncreaseReplicationFactorRequest(**_params)
        response = self._boto_client.increase_replication_factor(
            **_request.to_boto()
        )

        return shapes.IncreaseReplicationFactorResponse.from_boto(response)

    def list_tags(
        self,
        _request: shapes.ListTagsRequest = None,
        *,
        resource_name: str,
        next_token: str = ShapeBase.NOT_SET,
    ) -> shapes.ListTagsResponse:
        """
        List all of the tags for a DAX cluster. You can call `ListTags` up to 10 times
        per second, per account.
        """
        if _request is None:
            _params = {}
            if resource_name is not ShapeBase.NOT_SET:
                _params['resource_name'] = resource_name
            if next_token is not ShapeBase.NOT_SET:
                _params['next_token'] = next_token
            _request = shapes.ListTagsRequest(**_params)
        response = self._boto_client.list_tags(**_request.to_boto())

        return shapes.ListTagsResponse.from_boto(response)

    def reboot_node(
        self,
        _request: shapes.RebootNodeRequest = None,
        *,
        cluster_name: str,
        node_id: str,
    ) -> shapes.RebootNodeResponse:
        """
        Reboots a single node of a DAX cluster. The reboot action takes place as soon as
        possible. During the reboot, the node status is set to REBOOTING.
        """
        if _request is None:
            _params = {}
            if cluster_name is not ShapeBase.NOT_SET:
                _params['cluster_name'] = cluster_name
            if node_id is not ShapeBase.NOT_SET:
                _params['node_id'] = node_id
            _request = shapes.RebootNodeRequest(**_params)
        response = self._boto_client.reboot_node(**_request.to_boto())

        return shapes.RebootNodeResponse.from_boto(response)

    def tag_resource(
        self,
        _request: shapes.TagResourceRequest = None,
        *,
        resource_name: str,
        tags: typing.List[shapes.Tag],
    ) -> shapes.TagResourceResponse:
        """
        Associates a set of tags with a DAX resource. You can call `TagResource` up to 5
        times per second, per account.
        """
        if _request is None:
            _params = {}
            if resource_name is not ShapeBase.NOT_SET:
                _params['resource_name'] = resource_name
            if tags is not ShapeBase.NOT_SET:
                _params['tags'] = tags
            _request = shapes.TagResourceRequest(**_params)
        response = self._boto_client.tag_resource(**_request.to_boto())

        return shapes.TagResourceResponse.from_boto(response)

    def untag_resource(
        self,
        _request: shapes.UntagResourceRequest = None,
        *,
        resource_name: str,
        tag_keys: typing.List[str],
    ) -> shapes.UntagResourceResponse:
        """
        Removes the association of tags from a DAX resource. You can call
        `UntagResource` up to 5 times per second, per account.
        """
        if _request is None:
            _params = {}
            if resource_name is not ShapeBase.NOT_SET:
                _params['resource_name'] = resource_name
            if tag_keys is not ShapeBase.NOT_SET:
                _params['tag_keys'] = tag_keys
            _request = shapes.UntagResourceRequest(**_params)
        response = self._boto_client.untag_resource(**_request.to_boto())

        return shapes.UntagResourceResponse.from_boto(response)

    def update_cluster(
        self,
        _request: shapes.UpdateClusterRequest = None,
        *,
        cluster_name: str,
        description: str = ShapeBase.NOT_SET,
        preferred_maintenance_window: str = ShapeBase.NOT_SET,
        notification_topic_arn: str = ShapeBase.NOT_SET,
        notification_topic_status: str = ShapeBase.NOT_SET,
        parameter_group_name: str = ShapeBase.NOT_SET,
        security_group_ids: typing.List[str] = ShapeBase.NOT_SET,
    ) -> shapes.UpdateClusterResponse:
        """
        Modifies the settings for a DAX cluster. You can use this action to change one
        or more cluster configuration parameters by specifying the parameters and the
        new values.
        """
        if _request is None:
            _params = {}
            if cluster_name is not ShapeBase.NOT_SET:
                _params['cluster_name'] = cluster_name
            if description is not ShapeBase.NOT_SET:
                _params['description'] = description
            if preferred_maintenance_window is not ShapeBase.NOT_SET:
                _params['preferred_maintenance_window'
                       ] = preferred_maintenance_window
            if notification_topic_arn is not ShapeBase.NOT_SET:
                _params['notification_topic_arn'] = notification_topic_arn
            if notification_topic_status is not ShapeBase.NOT_SET:
                _params['notification_topic_status'] = notification_topic_status
            if parameter_group_name is not ShapeBase.NOT_SET:
                _params['parameter_group_name'] = parameter_group_name
            if security_group_ids is not ShapeBase.NOT_SET:
                _params['security_group_ids'] = security_group_ids
            _request = shapes.UpdateClusterRequest(**_params)
        response = self._boto_client.update_cluster(**_request.to_boto())

        return shapes.UpdateClusterResponse.from_boto(response)

    def update_parameter_group(
        self,
        _request: shapes.UpdateParameterGroupRequest = None,
        *,
        parameter_group_name: str,
        parameter_name_values: typing.List[shapes.ParameterNameValue],
    ) -> shapes.UpdateParameterGroupResponse:
        """
        Modifies the parameters of a parameter group. You can modify up to 20 parameters
        in a single request by submitting a list parameter name and value pairs.
        """
        if _request is None:
            _params = {}
            if parameter_group_name is not ShapeBase.NOT_SET:
                _params['parameter_group_name'] = parameter_group_name
            if parameter_name_values is not ShapeBase.NOT_SET:
                _params['parameter_name_values'] = parameter_name_values
            _request = shapes.UpdateParameterGroupRequest(**_params)
        response = self._boto_client.update_parameter_group(
            **_request.to_boto()
        )

        return shapes.UpdateParameterGroupResponse.from_boto(response)

    def update_subnet_group(
        self,
        _request: shapes.UpdateSubnetGroupRequest = None,
        *,
        subnet_group_name: str,
        description: str = ShapeBase.NOT_SET,
        subnet_ids: typing.List[str] = ShapeBase.NOT_SET,
    ) -> shapes.UpdateSubnetGroupResponse:
        """
        Modifies an existing subnet group.
        """
        if _request is None:
            _params = {}
            if subnet_group_name is not ShapeBase.NOT_SET:
                _params['subnet_group_name'] = subnet_group_name
            if description is not ShapeBase.NOT_SET:
                _params['description'] = description
            if subnet_ids is not ShapeBase.NOT_SET:
                _params['subnet_ids'] = subnet_ids
            _request = shapes.UpdateSubnetGroupRequest(**_params)
        response = self._boto_client.update_subnet_group(**_request.to_boto())

        return shapes.UpdateSubnetGroupResponse.from_boto(response)
