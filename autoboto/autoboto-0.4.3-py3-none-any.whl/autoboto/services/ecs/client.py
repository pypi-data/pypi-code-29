import datetime
import typing
import boto3
from autoboto import ClientBase, ShapeBase, OutputShapeBase
from . import shapes


class Client(ClientBase):
    def __init__(self, *args, **kwargs):
        super().__init__("ecs", *args, **kwargs)

    def create_cluster(
        self,
        _request: shapes.CreateClusterRequest = None,
        *,
        cluster_name: str = ShapeBase.NOT_SET,
    ) -> shapes.CreateClusterResponse:
        """
        Creates a new Amazon ECS cluster. By default, your account receives a `default`
        cluster when you launch your first container instance. However, you can create
        your own cluster with a unique name with the `CreateCluster` action.

        When you call the CreateCluster API operation, Amazon ECS attempts to create the
        service-linked role for your account so that required resources in other AWS
        services can be managed on your behalf. However, if the IAM user that makes the
        call does not have permissions to create the service-linked role, it is not
        created. For more information, see [Using Service-Linked Roles for Amazon
        ECS](http://docs.aws.amazon.com/AmazonECS/latest/developerguide/using-service-
        linked-roles.html) in the _Amazon Elastic Container Service Developer Guide_.
        """
        if _request is None:
            _params = {}
            if cluster_name is not ShapeBase.NOT_SET:
                _params['cluster_name'] = cluster_name
            _request = shapes.CreateClusterRequest(**_params)
        response = self._boto_client.create_cluster(**_request.to_boto())

        return shapes.CreateClusterResponse.from_boto(response)

    def create_service(
        self,
        _request: shapes.CreateServiceRequest = None,
        *,
        service_name: str,
        task_definition: str,
        cluster: str = ShapeBase.NOT_SET,
        load_balancers: typing.List[shapes.LoadBalancer] = ShapeBase.NOT_SET,
        service_registries: typing.List[shapes.ServiceRegistry
                                       ] = ShapeBase.NOT_SET,
        desired_count: int = ShapeBase.NOT_SET,
        client_token: str = ShapeBase.NOT_SET,
        launch_type: typing.Union[str, shapes.LaunchType] = ShapeBase.NOT_SET,
        platform_version: str = ShapeBase.NOT_SET,
        role: str = ShapeBase.NOT_SET,
        deployment_configuration: shapes.DeploymentConfiguration = ShapeBase.
        NOT_SET,
        placement_constraints: typing.List[shapes.PlacementConstraint
                                          ] = ShapeBase.NOT_SET,
        placement_strategy: typing.List[shapes.PlacementStrategy
                                       ] = ShapeBase.NOT_SET,
        network_configuration: shapes.NetworkConfiguration = ShapeBase.NOT_SET,
        health_check_grace_period_seconds: int = ShapeBase.NOT_SET,
        scheduling_strategy: typing.
        Union[str, shapes.SchedulingStrategy] = ShapeBase.NOT_SET,
    ) -> shapes.CreateServiceResponse:
        """
        Runs and maintains a desired number of tasks from a specified task definition.
        If the number of tasks running in a service drops below `desiredCount`, Amazon
        ECS spawns another copy of the task in the specified cluster. To update an
        existing service, see UpdateService.

        In addition to maintaining the desired count of tasks in your service, you can
        optionally run your service behind a load balancer. The load balancer
        distributes traffic across the tasks that are associated with the service. For
        more information, see [Service Load
        Balancing](http://docs.aws.amazon.com/AmazonECS/latest/developerguide/service-
        load-balancing.html) in the _Amazon Elastic Container Service Developer Guide_.

        You can optionally specify a deployment configuration for your service. During a
        deployment, the service scheduler uses the `minimumHealthyPercent` and
        `maximumPercent` parameters to determine the deployment strategy. The deployment
        is triggered by changing the task definition or the desired count of a service
        with an UpdateService operation.

        The `minimumHealthyPercent` represents a lower limit on the number of your
        service's tasks that must remain in the `RUNNING` state during a deployment, as
        a percentage of the `desiredCount` (rounded up to the nearest integer). This
        parameter enables you to deploy without using additional cluster capacity. For
        example, if your service has a `desiredCount` of four tasks and a
        `minimumHealthyPercent` of 50%, the scheduler can stop two existing tasks to
        free up cluster capacity before starting two new tasks. Tasks for services that
        _do not_ use a load balancer are considered healthy if they are in the `RUNNING`
        state. Tasks for services that _do_ use a load balancer are considered healthy
        if they are in the `RUNNING` state and the container instance they are hosted on
        is reported as healthy by the load balancer. The default value for a replica
        service for `minimumHealthyPercent` is 50% in the console and 100% for the AWS
        CLI, the AWS SDKs, and the APIs. The default value for a daemon service for
        `minimumHealthyPercent` is 0% for the AWS CLI, the AWS SDKs, and the APIs and
        50% for the console.

        The `maximumPercent` parameter represents an upper limit on the number of your
        service's tasks that are allowed in the `RUNNING` or `PENDING` state during a
        deployment, as a percentage of the `desiredCount` (rounded down to the nearest
        integer). This parameter enables you to define the deployment batch size. For
        example, if your replica service has a `desiredCount` of four tasks and a
        `maximumPercent` value of 200%, the scheduler can start four new tasks before
        stopping the four older tasks (provided that the cluster resources required to
        do this are available). The default value for a replica service for
        `maximumPercent` is 200%. If you are using a daemon service type, the
        `maximumPercent` should remain at 100%, which is the default value.

        When the service scheduler launches new tasks, it determines task placement in
        your cluster using the following logic:

          * Determine which of the container instances in your cluster can support your service's task definition (for example, they have the required CPU, memory, ports, and container instance attributes).

          * By default, the service scheduler attempts to balance tasks across Availability Zones in this manner (although you can choose a different placement strategy) with the `placementStrategy` parameter):

            * Sort the valid container instances, giving priority to instances that have the fewest number of running tasks for this service in their respective Availability Zone. For example, if zone A has one running service task and zones B and C each have zero, valid container instances in either zone B or C are considered optimal for placement.

            * Place the new service task on a valid container instance in an optimal Availability Zone (based on the previous steps), favoring container instances with the fewest number of running tasks for this service.
        """
        if _request is None:
            _params = {}
            if service_name is not ShapeBase.NOT_SET:
                _params['service_name'] = service_name
            if task_definition is not ShapeBase.NOT_SET:
                _params['task_definition'] = task_definition
            if cluster is not ShapeBase.NOT_SET:
                _params['cluster'] = cluster
            if load_balancers is not ShapeBase.NOT_SET:
                _params['load_balancers'] = load_balancers
            if service_registries is not ShapeBase.NOT_SET:
                _params['service_registries'] = service_registries
            if desired_count is not ShapeBase.NOT_SET:
                _params['desired_count'] = desired_count
            if client_token is not ShapeBase.NOT_SET:
                _params['client_token'] = client_token
            if launch_type is not ShapeBase.NOT_SET:
                _params['launch_type'] = launch_type
            if platform_version is not ShapeBase.NOT_SET:
                _params['platform_version'] = platform_version
            if role is not ShapeBase.NOT_SET:
                _params['role'] = role
            if deployment_configuration is not ShapeBase.NOT_SET:
                _params['deployment_configuration'] = deployment_configuration
            if placement_constraints is not ShapeBase.NOT_SET:
                _params['placement_constraints'] = placement_constraints
            if placement_strategy is not ShapeBase.NOT_SET:
                _params['placement_strategy'] = placement_strategy
            if network_configuration is not ShapeBase.NOT_SET:
                _params['network_configuration'] = network_configuration
            if health_check_grace_period_seconds is not ShapeBase.NOT_SET:
                _params['health_check_grace_period_seconds'
                       ] = health_check_grace_period_seconds
            if scheduling_strategy is not ShapeBase.NOT_SET:
                _params['scheduling_strategy'] = scheduling_strategy
            _request = shapes.CreateServiceRequest(**_params)
        response = self._boto_client.create_service(**_request.to_boto())

        return shapes.CreateServiceResponse.from_boto(response)

    def delete_attributes(
        self,
        _request: shapes.DeleteAttributesRequest = None,
        *,
        attributes: typing.List[shapes.Attribute],
        cluster: str = ShapeBase.NOT_SET,
    ) -> shapes.DeleteAttributesResponse:
        """
        Deletes one or more custom attributes from an Amazon ECS resource.
        """
        if _request is None:
            _params = {}
            if attributes is not ShapeBase.NOT_SET:
                _params['attributes'] = attributes
            if cluster is not ShapeBase.NOT_SET:
                _params['cluster'] = cluster
            _request = shapes.DeleteAttributesRequest(**_params)
        response = self._boto_client.delete_attributes(**_request.to_boto())

        return shapes.DeleteAttributesResponse.from_boto(response)

    def delete_cluster(
        self,
        _request: shapes.DeleteClusterRequest = None,
        *,
        cluster: str,
    ) -> shapes.DeleteClusterResponse:
        """
        Deletes the specified cluster. You must deregister all container instances from
        this cluster before you may delete it. You can list the container instances in a
        cluster with ListContainerInstances and deregister them with
        DeregisterContainerInstance.
        """
        if _request is None:
            _params = {}
            if cluster is not ShapeBase.NOT_SET:
                _params['cluster'] = cluster
            _request = shapes.DeleteClusterRequest(**_params)
        response = self._boto_client.delete_cluster(**_request.to_boto())

        return shapes.DeleteClusterResponse.from_boto(response)

    def delete_service(
        self,
        _request: shapes.DeleteServiceRequest = None,
        *,
        service: str,
        cluster: str = ShapeBase.NOT_SET,
        force: bool = ShapeBase.NOT_SET,
    ) -> shapes.DeleteServiceResponse:
        """
        Deletes a specified service within a cluster. You can delete a service if you
        have no running tasks in it and the desired task count is zero. If the service
        is actively maintaining tasks, you cannot delete it, and you must update the
        service to a desired task count of zero. For more information, see
        UpdateService.

        When you delete a service, if there are still running tasks that require
        cleanup, the service status moves from `ACTIVE` to `DRAINING`, and the service
        is no longer visible in the console or in ListServices API operations. After the
        tasks have stopped, then the service status moves from `DRAINING` to `INACTIVE`.
        Services in the `DRAINING` or `INACTIVE` status can still be viewed with
        DescribeServices API operations. However, in the future, `INACTIVE` services may
        be cleaned up and purged from Amazon ECS record keeping, and DescribeServices
        API operations on those services return a `ServiceNotFoundException` error.

        If you attempt to create a new service with the same name as an existing service
        in either `ACTIVE` or `DRAINING` status, you will receive an error.
        """
        if _request is None:
            _params = {}
            if service is not ShapeBase.NOT_SET:
                _params['service'] = service
            if cluster is not ShapeBase.NOT_SET:
                _params['cluster'] = cluster
            if force is not ShapeBase.NOT_SET:
                _params['force'] = force
            _request = shapes.DeleteServiceRequest(**_params)
        response = self._boto_client.delete_service(**_request.to_boto())

        return shapes.DeleteServiceResponse.from_boto(response)

    def deregister_container_instance(
        self,
        _request: shapes.DeregisterContainerInstanceRequest = None,
        *,
        container_instance: str,
        cluster: str = ShapeBase.NOT_SET,
        force: bool = ShapeBase.NOT_SET,
    ) -> shapes.DeregisterContainerInstanceResponse:
        """
        Deregisters an Amazon ECS container instance from the specified cluster. This
        instance is no longer available to run tasks.

        If you intend to use the container instance for some other purpose after
        deregistration, you should stop all of the tasks running on the container
        instance before deregistration. That prevents any orphaned tasks from consuming
        resources.

        Deregistering a container instance removes the instance from a cluster, but it
        does not terminate the EC2 instance; if you are finished using the instance, be
        sure to terminate it in the Amazon EC2 console to stop billing.

        If you terminate a running container instance, Amazon ECS automatically
        deregisters the instance from your cluster (stopped container instances or
        instances with disconnected agents are not automatically deregistered when
        terminated).
        """
        if _request is None:
            _params = {}
            if container_instance is not ShapeBase.NOT_SET:
                _params['container_instance'] = container_instance
            if cluster is not ShapeBase.NOT_SET:
                _params['cluster'] = cluster
            if force is not ShapeBase.NOT_SET:
                _params['force'] = force
            _request = shapes.DeregisterContainerInstanceRequest(**_params)
        response = self._boto_client.deregister_container_instance(
            **_request.to_boto()
        )

        return shapes.DeregisterContainerInstanceResponse.from_boto(response)

    def deregister_task_definition(
        self,
        _request: shapes.DeregisterTaskDefinitionRequest = None,
        *,
        task_definition: str,
    ) -> shapes.DeregisterTaskDefinitionResponse:
        """
        Deregisters the specified task definition by family and revision. Upon
        deregistration, the task definition is marked as `INACTIVE`. Existing tasks and
        services that reference an `INACTIVE` task definition continue to run without
        disruption. Existing services that reference an `INACTIVE` task definition can
        still scale up or down by modifying the service's desired count.

        You cannot use an `INACTIVE` task definition to run new tasks or create new
        services, and you cannot update an existing service to reference an `INACTIVE`
        task definition (although there may be up to a 10-minute window following
        deregistration where these restrictions have not yet taken effect).

        At this time, `INACTIVE` task definitions remain discoverable in your account
        indefinitely; however, this behavior is subject to change in the future, so you
        should not rely on `INACTIVE` task definitions persisting beyond the lifecycle
        of any associated tasks and services.
        """
        if _request is None:
            _params = {}
            if task_definition is not ShapeBase.NOT_SET:
                _params['task_definition'] = task_definition
            _request = shapes.DeregisterTaskDefinitionRequest(**_params)
        response = self._boto_client.deregister_task_definition(
            **_request.to_boto()
        )

        return shapes.DeregisterTaskDefinitionResponse.from_boto(response)

    def describe_clusters(
        self,
        _request: shapes.DescribeClustersRequest = None,
        *,
        clusters: typing.List[str] = ShapeBase.NOT_SET,
        include: typing.List[typing.Union[str, shapes.ClusterField]
                            ] = ShapeBase.NOT_SET,
    ) -> shapes.DescribeClustersResponse:
        """
        Describes one or more of your clusters.
        """
        if _request is None:
            _params = {}
            if clusters is not ShapeBase.NOT_SET:
                _params['clusters'] = clusters
            if include is not ShapeBase.NOT_SET:
                _params['include'] = include
            _request = shapes.DescribeClustersRequest(**_params)
        response = self._boto_client.describe_clusters(**_request.to_boto())

        return shapes.DescribeClustersResponse.from_boto(response)

    def describe_container_instances(
        self,
        _request: shapes.DescribeContainerInstancesRequest = None,
        *,
        container_instances: typing.List[str],
        cluster: str = ShapeBase.NOT_SET,
    ) -> shapes.DescribeContainerInstancesResponse:
        """
        Describes Amazon Elastic Container Service container instances. Returns metadata
        about registered and remaining resources on each container instance requested.
        """
        if _request is None:
            _params = {}
            if container_instances is not ShapeBase.NOT_SET:
                _params['container_instances'] = container_instances
            if cluster is not ShapeBase.NOT_SET:
                _params['cluster'] = cluster
            _request = shapes.DescribeContainerInstancesRequest(**_params)
        response = self._boto_client.describe_container_instances(
            **_request.to_boto()
        )

        return shapes.DescribeContainerInstancesResponse.from_boto(response)

    def describe_services(
        self,
        _request: shapes.DescribeServicesRequest = None,
        *,
        services: typing.List[str],
        cluster: str = ShapeBase.NOT_SET,
    ) -> shapes.DescribeServicesResponse:
        """
        Describes the specified services running in your cluster.
        """
        if _request is None:
            _params = {}
            if services is not ShapeBase.NOT_SET:
                _params['services'] = services
            if cluster is not ShapeBase.NOT_SET:
                _params['cluster'] = cluster
            _request = shapes.DescribeServicesRequest(**_params)
        response = self._boto_client.describe_services(**_request.to_boto())

        return shapes.DescribeServicesResponse.from_boto(response)

    def describe_task_definition(
        self,
        _request: shapes.DescribeTaskDefinitionRequest = None,
        *,
        task_definition: str,
    ) -> shapes.DescribeTaskDefinitionResponse:
        """
        Describes a task definition. You can specify a `family` and `revision` to find
        information about a specific task definition, or you can simply specify the
        family to find the latest `ACTIVE` revision in that family.

        You can only describe `INACTIVE` task definitions while an active task or
        service references them.
        """
        if _request is None:
            _params = {}
            if task_definition is not ShapeBase.NOT_SET:
                _params['task_definition'] = task_definition
            _request = shapes.DescribeTaskDefinitionRequest(**_params)
        response = self._boto_client.describe_task_definition(
            **_request.to_boto()
        )

        return shapes.DescribeTaskDefinitionResponse.from_boto(response)

    def describe_tasks(
        self,
        _request: shapes.DescribeTasksRequest = None,
        *,
        tasks: typing.List[str],
        cluster: str = ShapeBase.NOT_SET,
    ) -> shapes.DescribeTasksResponse:
        """
        Describes a specified task or tasks.
        """
        if _request is None:
            _params = {}
            if tasks is not ShapeBase.NOT_SET:
                _params['tasks'] = tasks
            if cluster is not ShapeBase.NOT_SET:
                _params['cluster'] = cluster
            _request = shapes.DescribeTasksRequest(**_params)
        response = self._boto_client.describe_tasks(**_request.to_boto())

        return shapes.DescribeTasksResponse.from_boto(response)

    def discover_poll_endpoint(
        self,
        _request: shapes.DiscoverPollEndpointRequest = None,
        *,
        container_instance: str = ShapeBase.NOT_SET,
        cluster: str = ShapeBase.NOT_SET,
    ) -> shapes.DiscoverPollEndpointResponse:
        """
        This action is only used by the Amazon ECS agent, and it is not intended for use
        outside of the agent.

        Returns an endpoint for the Amazon ECS agent to poll for updates.
        """
        if _request is None:
            _params = {}
            if container_instance is not ShapeBase.NOT_SET:
                _params['container_instance'] = container_instance
            if cluster is not ShapeBase.NOT_SET:
                _params['cluster'] = cluster
            _request = shapes.DiscoverPollEndpointRequest(**_params)
        response = self._boto_client.discover_poll_endpoint(
            **_request.to_boto()
        )

        return shapes.DiscoverPollEndpointResponse.from_boto(response)

    def list_attributes(
        self,
        _request: shapes.ListAttributesRequest = None,
        *,
        target_type: typing.Union[str, shapes.TargetType],
        cluster: str = ShapeBase.NOT_SET,
        attribute_name: str = ShapeBase.NOT_SET,
        attribute_value: str = ShapeBase.NOT_SET,
        next_token: str = ShapeBase.NOT_SET,
        max_results: int = ShapeBase.NOT_SET,
    ) -> shapes.ListAttributesResponse:
        """
        Lists the attributes for Amazon ECS resources within a specified target type and
        cluster. When you specify a target type and cluster, `ListAttributes` returns a
        list of attribute objects, one for each attribute on each resource. You can
        filter the list of results to a single attribute name to only return results
        that have that name. You can also filter the results by attribute name and
        value, for example, to see which container instances in a cluster are running a
        Linux AMI (`ecs.os-type=linux`).
        """
        if _request is None:
            _params = {}
            if target_type is not ShapeBase.NOT_SET:
                _params['target_type'] = target_type
            if cluster is not ShapeBase.NOT_SET:
                _params['cluster'] = cluster
            if attribute_name is not ShapeBase.NOT_SET:
                _params['attribute_name'] = attribute_name
            if attribute_value is not ShapeBase.NOT_SET:
                _params['attribute_value'] = attribute_value
            if next_token is not ShapeBase.NOT_SET:
                _params['next_token'] = next_token
            if max_results is not ShapeBase.NOT_SET:
                _params['max_results'] = max_results
            _request = shapes.ListAttributesRequest(**_params)
        response = self._boto_client.list_attributes(**_request.to_boto())

        return shapes.ListAttributesResponse.from_boto(response)

    def list_clusters(
        self,
        _request: shapes.ListClustersRequest = None,
        *,
        next_token: str = ShapeBase.NOT_SET,
        max_results: int = ShapeBase.NOT_SET,
    ) -> shapes.ListClustersResponse:
        """
        Returns a list of existing clusters.
        """
        if _request is None:
            _params = {}
            if next_token is not ShapeBase.NOT_SET:
                _params['next_token'] = next_token
            if max_results is not ShapeBase.NOT_SET:
                _params['max_results'] = max_results
            _request = shapes.ListClustersRequest(**_params)
        paginator = self.get_paginator("list_clusters").paginate(
            **_request.to_boto()
        )
        page_generator = (page for page in paginator)
        first_page = next(page_generator)
        result = shapes.ListClustersResponse.from_boto(first_page)
        result._page_iterator = page_generator
        return result

        return shapes.ListClustersResponse.from_boto(response)

    def list_container_instances(
        self,
        _request: shapes.ListContainerInstancesRequest = None,
        *,
        cluster: str = ShapeBase.NOT_SET,
        filter: str = ShapeBase.NOT_SET,
        next_token: str = ShapeBase.NOT_SET,
        max_results: int = ShapeBase.NOT_SET,
        status: typing.Union[str, shapes.ContainerInstanceStatus] = ShapeBase.
        NOT_SET,
    ) -> shapes.ListContainerInstancesResponse:
        """
        Returns a list of container instances in a specified cluster. You can filter the
        results of a `ListContainerInstances` operation with cluster query language
        statements inside the `filter` parameter. For more information, see [Cluster
        Query
        Language](http://docs.aws.amazon.com/AmazonECS/latest/developerguide/cluster-
        query-language.html) in the _Amazon Elastic Container Service Developer Guide_.
        """
        if _request is None:
            _params = {}
            if cluster is not ShapeBase.NOT_SET:
                _params['cluster'] = cluster
            if filter is not ShapeBase.NOT_SET:
                _params['filter'] = filter
            if next_token is not ShapeBase.NOT_SET:
                _params['next_token'] = next_token
            if max_results is not ShapeBase.NOT_SET:
                _params['max_results'] = max_results
            if status is not ShapeBase.NOT_SET:
                _params['status'] = status
            _request = shapes.ListContainerInstancesRequest(**_params)
        paginator = self.get_paginator("list_container_instances").paginate(
            **_request.to_boto()
        )
        page_generator = (page for page in paginator)
        first_page = next(page_generator)
        result = shapes.ListContainerInstancesResponse.from_boto(first_page)
        result._page_iterator = page_generator
        return result

        return shapes.ListContainerInstancesResponse.from_boto(response)

    def list_services(
        self,
        _request: shapes.ListServicesRequest = None,
        *,
        cluster: str = ShapeBase.NOT_SET,
        next_token: str = ShapeBase.NOT_SET,
        max_results: int = ShapeBase.NOT_SET,
        launch_type: typing.Union[str, shapes.LaunchType] = ShapeBase.NOT_SET,
        scheduling_strategy: typing.
        Union[str, shapes.SchedulingStrategy] = ShapeBase.NOT_SET,
    ) -> shapes.ListServicesResponse:
        """
        Lists the services that are running in a specified cluster.
        """
        if _request is None:
            _params = {}
            if cluster is not ShapeBase.NOT_SET:
                _params['cluster'] = cluster
            if next_token is not ShapeBase.NOT_SET:
                _params['next_token'] = next_token
            if max_results is not ShapeBase.NOT_SET:
                _params['max_results'] = max_results
            if launch_type is not ShapeBase.NOT_SET:
                _params['launch_type'] = launch_type
            if scheduling_strategy is not ShapeBase.NOT_SET:
                _params['scheduling_strategy'] = scheduling_strategy
            _request = shapes.ListServicesRequest(**_params)
        paginator = self.get_paginator("list_services").paginate(
            **_request.to_boto()
        )
        page_generator = (page for page in paginator)
        first_page = next(page_generator)
        result = shapes.ListServicesResponse.from_boto(first_page)
        result._page_iterator = page_generator
        return result

        return shapes.ListServicesResponse.from_boto(response)

    def list_task_definition_families(
        self,
        _request: shapes.ListTaskDefinitionFamiliesRequest = None,
        *,
        family_prefix: str = ShapeBase.NOT_SET,
        status: typing.Union[str, shapes.
                             TaskDefinitionFamilyStatus] = ShapeBase.NOT_SET,
        next_token: str = ShapeBase.NOT_SET,
        max_results: int = ShapeBase.NOT_SET,
    ) -> shapes.ListTaskDefinitionFamiliesResponse:
        """
        Returns a list of task definition families that are registered to your account
        (which may include task definition families that no longer have any `ACTIVE`
        task definition revisions).

        You can filter out task definition families that do not contain any `ACTIVE`
        task definition revisions by setting the `status` parameter to `ACTIVE`. You can
        also filter the results with the `familyPrefix` parameter.
        """
        if _request is None:
            _params = {}
            if family_prefix is not ShapeBase.NOT_SET:
                _params['family_prefix'] = family_prefix
            if status is not ShapeBase.NOT_SET:
                _params['status'] = status
            if next_token is not ShapeBase.NOT_SET:
                _params['next_token'] = next_token
            if max_results is not ShapeBase.NOT_SET:
                _params['max_results'] = max_results
            _request = shapes.ListTaskDefinitionFamiliesRequest(**_params)
        paginator = self.get_paginator("list_task_definition_families"
                                      ).paginate(**_request.to_boto())
        page_generator = (page for page in paginator)
        first_page = next(page_generator)
        result = shapes.ListTaskDefinitionFamiliesResponse.from_boto(first_page)
        result._page_iterator = page_generator
        return result

        return shapes.ListTaskDefinitionFamiliesResponse.from_boto(response)

    def list_task_definitions(
        self,
        _request: shapes.ListTaskDefinitionsRequest = None,
        *,
        family_prefix: str = ShapeBase.NOT_SET,
        status: typing.Union[str, shapes.TaskDefinitionStatus] = ShapeBase.
        NOT_SET,
        sort: typing.Union[str, shapes.SortOrder] = ShapeBase.NOT_SET,
        next_token: str = ShapeBase.NOT_SET,
        max_results: int = ShapeBase.NOT_SET,
    ) -> shapes.ListTaskDefinitionsResponse:
        """
        Returns a list of task definitions that are registered to your account. You can
        filter the results by family name with the `familyPrefix` parameter or by status
        with the `status` parameter.
        """
        if _request is None:
            _params = {}
            if family_prefix is not ShapeBase.NOT_SET:
                _params['family_prefix'] = family_prefix
            if status is not ShapeBase.NOT_SET:
                _params['status'] = status
            if sort is not ShapeBase.NOT_SET:
                _params['sort'] = sort
            if next_token is not ShapeBase.NOT_SET:
                _params['next_token'] = next_token
            if max_results is not ShapeBase.NOT_SET:
                _params['max_results'] = max_results
            _request = shapes.ListTaskDefinitionsRequest(**_params)
        paginator = self.get_paginator("list_task_definitions").paginate(
            **_request.to_boto()
        )
        page_generator = (page for page in paginator)
        first_page = next(page_generator)
        result = shapes.ListTaskDefinitionsResponse.from_boto(first_page)
        result._page_iterator = page_generator
        return result

        return shapes.ListTaskDefinitionsResponse.from_boto(response)

    def list_tasks(
        self,
        _request: shapes.ListTasksRequest = None,
        *,
        cluster: str = ShapeBase.NOT_SET,
        container_instance: str = ShapeBase.NOT_SET,
        family: str = ShapeBase.NOT_SET,
        next_token: str = ShapeBase.NOT_SET,
        max_results: int = ShapeBase.NOT_SET,
        started_by: str = ShapeBase.NOT_SET,
        service_name: str = ShapeBase.NOT_SET,
        desired_status: typing.Union[str, shapes.DesiredStatus] = ShapeBase.
        NOT_SET,
        launch_type: typing.Union[str, shapes.LaunchType] = ShapeBase.NOT_SET,
    ) -> shapes.ListTasksResponse:
        """
        Returns a list of tasks for a specified cluster. You can filter the results by
        family name, by a particular container instance, or by the desired status of the
        task with the `family`, `containerInstance`, and `desiredStatus` parameters.

        Recently stopped tasks might appear in the returned results. Currently, stopped
        tasks appear in the returned results for at least one hour.
        """
        if _request is None:
            _params = {}
            if cluster is not ShapeBase.NOT_SET:
                _params['cluster'] = cluster
            if container_instance is not ShapeBase.NOT_SET:
                _params['container_instance'] = container_instance
            if family is not ShapeBase.NOT_SET:
                _params['family'] = family
            if next_token is not ShapeBase.NOT_SET:
                _params['next_token'] = next_token
            if max_results is not ShapeBase.NOT_SET:
                _params['max_results'] = max_results
            if started_by is not ShapeBase.NOT_SET:
                _params['started_by'] = started_by
            if service_name is not ShapeBase.NOT_SET:
                _params['service_name'] = service_name
            if desired_status is not ShapeBase.NOT_SET:
                _params['desired_status'] = desired_status
            if launch_type is not ShapeBase.NOT_SET:
                _params['launch_type'] = launch_type
            _request = shapes.ListTasksRequest(**_params)
        paginator = self.get_paginator("list_tasks").paginate(
            **_request.to_boto()
        )
        page_generator = (page for page in paginator)
        first_page = next(page_generator)
        result = shapes.ListTasksResponse.from_boto(first_page)
        result._page_iterator = page_generator
        return result

        return shapes.ListTasksResponse.from_boto(response)

    def put_attributes(
        self,
        _request: shapes.PutAttributesRequest = None,
        *,
        attributes: typing.List[shapes.Attribute],
        cluster: str = ShapeBase.NOT_SET,
    ) -> shapes.PutAttributesResponse:
        """
        Create or update an attribute on an Amazon ECS resource. If the attribute does
        not exist, it is created. If the attribute exists, its value is replaced with
        the specified value. To delete an attribute, use DeleteAttributes. For more
        information, see
        [Attributes](http://docs.aws.amazon.com/AmazonECS/latest/developerguide/task-
        placement-constraints.html#attributes) in the _Amazon Elastic Container Service
        Developer Guide_.
        """
        if _request is None:
            _params = {}
            if attributes is not ShapeBase.NOT_SET:
                _params['attributes'] = attributes
            if cluster is not ShapeBase.NOT_SET:
                _params['cluster'] = cluster
            _request = shapes.PutAttributesRequest(**_params)
        response = self._boto_client.put_attributes(**_request.to_boto())

        return shapes.PutAttributesResponse.from_boto(response)

    def register_container_instance(
        self,
        _request: shapes.RegisterContainerInstanceRequest = None,
        *,
        cluster: str = ShapeBase.NOT_SET,
        instance_identity_document: str = ShapeBase.NOT_SET,
        instance_identity_document_signature: str = ShapeBase.NOT_SET,
        total_resources: typing.List[shapes.Resource] = ShapeBase.NOT_SET,
        version_info: shapes.VersionInfo = ShapeBase.NOT_SET,
        container_instance_arn: str = ShapeBase.NOT_SET,
        attributes: typing.List[shapes.Attribute] = ShapeBase.NOT_SET,
    ) -> shapes.RegisterContainerInstanceResponse:
        """
        This action is only used by the Amazon ECS agent, and it is not intended for use
        outside of the agent.

        Registers an EC2 instance into the specified cluster. This instance becomes
        available to place containers on.
        """
        if _request is None:
            _params = {}
            if cluster is not ShapeBase.NOT_SET:
                _params['cluster'] = cluster
            if instance_identity_document is not ShapeBase.NOT_SET:
                _params['instance_identity_document'
                       ] = instance_identity_document
            if instance_identity_document_signature is not ShapeBase.NOT_SET:
                _params['instance_identity_document_signature'
                       ] = instance_identity_document_signature
            if total_resources is not ShapeBase.NOT_SET:
                _params['total_resources'] = total_resources
            if version_info is not ShapeBase.NOT_SET:
                _params['version_info'] = version_info
            if container_instance_arn is not ShapeBase.NOT_SET:
                _params['container_instance_arn'] = container_instance_arn
            if attributes is not ShapeBase.NOT_SET:
                _params['attributes'] = attributes
            _request = shapes.RegisterContainerInstanceRequest(**_params)
        response = self._boto_client.register_container_instance(
            **_request.to_boto()
        )

        return shapes.RegisterContainerInstanceResponse.from_boto(response)

    def register_task_definition(
        self,
        _request: shapes.RegisterTaskDefinitionRequest = None,
        *,
        family: str,
        container_definitions: typing.List[shapes.ContainerDefinition],
        task_role_arn: str = ShapeBase.NOT_SET,
        execution_role_arn: str = ShapeBase.NOT_SET,
        network_mode: typing.Union[str, shapes.NetworkMode] = ShapeBase.NOT_SET,
        volumes: typing.List[shapes.Volume] = ShapeBase.NOT_SET,
        placement_constraints: typing.List[
            shapes.TaskDefinitionPlacementConstraint] = ShapeBase.NOT_SET,
        requires_compatibilities: typing.List[
            typing.Union[str, shapes.Compatibility]] = ShapeBase.NOT_SET,
        cpu: str = ShapeBase.NOT_SET,
        memory: str = ShapeBase.NOT_SET,
    ) -> shapes.RegisterTaskDefinitionResponse:
        """
        Registers a new task definition from the supplied `family` and
        `containerDefinitions`. Optionally, you can add data volumes to your containers
        with the `volumes` parameter. For more information about task definition
        parameters and defaults, see [Amazon ECS Task
        Definitions](http://docs.aws.amazon.com/AmazonECS/latest/developerguide/task_defintions.html)
        in the _Amazon Elastic Container Service Developer Guide_.

        You can specify an IAM role for your task with the `taskRoleArn` parameter. When
        you specify an IAM role for a task, its containers can then use the latest
        versions of the AWS CLI or SDKs to make API requests to the AWS services that
        are specified in the IAM policy associated with the role. For more information,
        see [IAM Roles for
        Tasks](http://docs.aws.amazon.com/AmazonECS/latest/developerguide/task-iam-
        roles.html) in the _Amazon Elastic Container Service Developer Guide_.

        You can specify a Docker networking mode for the containers in your task
        definition with the `networkMode` parameter. The available network modes
        correspond to those described in [Network
        settings](https://docs.docker.com/engine/reference/run/#/network-settings) in
        the Docker run reference. If you specify the `awsvpc` network mode, the task is
        allocated an elastic network interface, and you must specify a
        NetworkConfiguration when you create a service or run a task with the task
        definition. For more information, see [Task
        Networking](http://docs.aws.amazon.com/AmazonECS/latest/developerguide/task-
        networking.html) in the _Amazon Elastic Container Service Developer Guide_.
        """
        if _request is None:
            _params = {}
            if family is not ShapeBase.NOT_SET:
                _params['family'] = family
            if container_definitions is not ShapeBase.NOT_SET:
                _params['container_definitions'] = container_definitions
            if task_role_arn is not ShapeBase.NOT_SET:
                _params['task_role_arn'] = task_role_arn
            if execution_role_arn is not ShapeBase.NOT_SET:
                _params['execution_role_arn'] = execution_role_arn
            if network_mode is not ShapeBase.NOT_SET:
                _params['network_mode'] = network_mode
            if volumes is not ShapeBase.NOT_SET:
                _params['volumes'] = volumes
            if placement_constraints is not ShapeBase.NOT_SET:
                _params['placement_constraints'] = placement_constraints
            if requires_compatibilities is not ShapeBase.NOT_SET:
                _params['requires_compatibilities'] = requires_compatibilities
            if cpu is not ShapeBase.NOT_SET:
                _params['cpu'] = cpu
            if memory is not ShapeBase.NOT_SET:
                _params['memory'] = memory
            _request = shapes.RegisterTaskDefinitionRequest(**_params)
        response = self._boto_client.register_task_definition(
            **_request.to_boto()
        )

        return shapes.RegisterTaskDefinitionResponse.from_boto(response)

    def run_task(
        self,
        _request: shapes.RunTaskRequest = None,
        *,
        task_definition: str,
        cluster: str = ShapeBase.NOT_SET,
        overrides: shapes.TaskOverride = ShapeBase.NOT_SET,
        count: int = ShapeBase.NOT_SET,
        started_by: str = ShapeBase.NOT_SET,
        group: str = ShapeBase.NOT_SET,
        placement_constraints: typing.List[shapes.PlacementConstraint
                                          ] = ShapeBase.NOT_SET,
        placement_strategy: typing.List[shapes.PlacementStrategy
                                       ] = ShapeBase.NOT_SET,
        launch_type: typing.Union[str, shapes.LaunchType] = ShapeBase.NOT_SET,
        platform_version: str = ShapeBase.NOT_SET,
        network_configuration: shapes.NetworkConfiguration = ShapeBase.NOT_SET,
    ) -> shapes.RunTaskResponse:
        """
        Starts a new task using the specified task definition.

        You can allow Amazon ECS to place tasks for you, or you can customize how Amazon
        ECS places tasks using placement constraints and placement strategies. For more
        information, see [Scheduling
        Tasks](http://docs.aws.amazon.com/AmazonECS/latest/developerguide/scheduling_tasks.html)
        in the _Amazon Elastic Container Service Developer Guide_.

        Alternatively, you can use StartTask to use your own scheduler or place tasks
        manually on specific container instances.

        The Amazon ECS API follows an eventual consistency model, due to the distributed
        nature of the system supporting the API. This means that the result of an API
        command you run that affects your Amazon ECS resources might not be immediately
        visible to all subsequent commands you run. You should keep this in mind when
        you carry out an API command that immediately follows a previous API command.

        To manage eventual consistency, you can do the following:

          * Confirm the state of the resource before you run a command to modify it. Run the DescribeTasks command using an exponential backoff algorithm to ensure that you allow enough time for the previous command to propagate through the system. To do this, run the DescribeTasks command repeatedly, starting with a couple of seconds of wait time and increasing gradually up to five minutes of wait time.

          * Add wait time between subsequent commands, even if the DescribeTasks command returns an accurate response. Apply an exponential backoff algorithm starting with a couple of seconds of wait time, and increase gradually up to about five minutes of wait time.
        """
        if _request is None:
            _params = {}
            if task_definition is not ShapeBase.NOT_SET:
                _params['task_definition'] = task_definition
            if cluster is not ShapeBase.NOT_SET:
                _params['cluster'] = cluster
            if overrides is not ShapeBase.NOT_SET:
                _params['overrides'] = overrides
            if count is not ShapeBase.NOT_SET:
                _params['count'] = count
            if started_by is not ShapeBase.NOT_SET:
                _params['started_by'] = started_by
            if group is not ShapeBase.NOT_SET:
                _params['group'] = group
            if placement_constraints is not ShapeBase.NOT_SET:
                _params['placement_constraints'] = placement_constraints
            if placement_strategy is not ShapeBase.NOT_SET:
                _params['placement_strategy'] = placement_strategy
            if launch_type is not ShapeBase.NOT_SET:
                _params['launch_type'] = launch_type
            if platform_version is not ShapeBase.NOT_SET:
                _params['platform_version'] = platform_version
            if network_configuration is not ShapeBase.NOT_SET:
                _params['network_configuration'] = network_configuration
            _request = shapes.RunTaskRequest(**_params)
        response = self._boto_client.run_task(**_request.to_boto())

        return shapes.RunTaskResponse.from_boto(response)

    def start_task(
        self,
        _request: shapes.StartTaskRequest = None,
        *,
        task_definition: str,
        container_instances: typing.List[str],
        cluster: str = ShapeBase.NOT_SET,
        overrides: shapes.TaskOverride = ShapeBase.NOT_SET,
        started_by: str = ShapeBase.NOT_SET,
        group: str = ShapeBase.NOT_SET,
        network_configuration: shapes.NetworkConfiguration = ShapeBase.NOT_SET,
    ) -> shapes.StartTaskResponse:
        """
        Starts a new task from the specified task definition on the specified container
        instance or instances.

        Alternatively, you can use RunTask to place tasks for you. For more information,
        see [Scheduling
        Tasks](http://docs.aws.amazon.com/AmazonECS/latest/developerguide/scheduling_tasks.html)
        in the _Amazon Elastic Container Service Developer Guide_.
        """
        if _request is None:
            _params = {}
            if task_definition is not ShapeBase.NOT_SET:
                _params['task_definition'] = task_definition
            if container_instances is not ShapeBase.NOT_SET:
                _params['container_instances'] = container_instances
            if cluster is not ShapeBase.NOT_SET:
                _params['cluster'] = cluster
            if overrides is not ShapeBase.NOT_SET:
                _params['overrides'] = overrides
            if started_by is not ShapeBase.NOT_SET:
                _params['started_by'] = started_by
            if group is not ShapeBase.NOT_SET:
                _params['group'] = group
            if network_configuration is not ShapeBase.NOT_SET:
                _params['network_configuration'] = network_configuration
            _request = shapes.StartTaskRequest(**_params)
        response = self._boto_client.start_task(**_request.to_boto())

        return shapes.StartTaskResponse.from_boto(response)

    def stop_task(
        self,
        _request: shapes.StopTaskRequest = None,
        *,
        task: str,
        cluster: str = ShapeBase.NOT_SET,
        reason: str = ShapeBase.NOT_SET,
    ) -> shapes.StopTaskResponse:
        """
        Stops a running task.

        When StopTask is called on a task, the equivalent of `docker stop` is issued to
        the containers running in the task. This results in a `SIGTERM` and a default
        30-second timeout, after which `SIGKILL` is sent and the containers are forcibly
        stopped. If the container handles the `SIGTERM` gracefully and exits within 30
        seconds from receiving it, no `SIGKILL` is sent.

        The default 30-second timeout can be configured on the Amazon ECS container
        agent with the `ECS_CONTAINER_STOP_TIMEOUT` variable. For more information, see
        [Amazon ECS Container Agent
        Configuration](http://docs.aws.amazon.com/AmazonECS/latest/developerguide/ecs-
        agent-config.html) in the _Amazon Elastic Container Service Developer Guide_.
        """
        if _request is None:
            _params = {}
            if task is not ShapeBase.NOT_SET:
                _params['task'] = task
            if cluster is not ShapeBase.NOT_SET:
                _params['cluster'] = cluster
            if reason is not ShapeBase.NOT_SET:
                _params['reason'] = reason
            _request = shapes.StopTaskRequest(**_params)
        response = self._boto_client.stop_task(**_request.to_boto())

        return shapes.StopTaskResponse.from_boto(response)

    def submit_container_state_change(
        self,
        _request: shapes.SubmitContainerStateChangeRequest = None,
        *,
        cluster: str = ShapeBase.NOT_SET,
        task: str = ShapeBase.NOT_SET,
        container_name: str = ShapeBase.NOT_SET,
        status: str = ShapeBase.NOT_SET,
        exit_code: int = ShapeBase.NOT_SET,
        reason: str = ShapeBase.NOT_SET,
        network_bindings: typing.List[shapes.NetworkBinding
                                     ] = ShapeBase.NOT_SET,
    ) -> shapes.SubmitContainerStateChangeResponse:
        """
        This action is only used by the Amazon ECS agent, and it is not intended for use
        outside of the agent.

        Sent to acknowledge that a container changed states.
        """
        if _request is None:
            _params = {}
            if cluster is not ShapeBase.NOT_SET:
                _params['cluster'] = cluster
            if task is not ShapeBase.NOT_SET:
                _params['task'] = task
            if container_name is not ShapeBase.NOT_SET:
                _params['container_name'] = container_name
            if status is not ShapeBase.NOT_SET:
                _params['status'] = status
            if exit_code is not ShapeBase.NOT_SET:
                _params['exit_code'] = exit_code
            if reason is not ShapeBase.NOT_SET:
                _params['reason'] = reason
            if network_bindings is not ShapeBase.NOT_SET:
                _params['network_bindings'] = network_bindings
            _request = shapes.SubmitContainerStateChangeRequest(**_params)
        response = self._boto_client.submit_container_state_change(
            **_request.to_boto()
        )

        return shapes.SubmitContainerStateChangeResponse.from_boto(response)

    def submit_task_state_change(
        self,
        _request: shapes.SubmitTaskStateChangeRequest = None,
        *,
        cluster: str = ShapeBase.NOT_SET,
        task: str = ShapeBase.NOT_SET,
        status: str = ShapeBase.NOT_SET,
        reason: str = ShapeBase.NOT_SET,
        containers: typing.List[shapes.ContainerStateChange
                               ] = ShapeBase.NOT_SET,
        attachments: typing.List[shapes.AttachmentStateChange
                                ] = ShapeBase.NOT_SET,
        pull_started_at: datetime.datetime = ShapeBase.NOT_SET,
        pull_stopped_at: datetime.datetime = ShapeBase.NOT_SET,
        execution_stopped_at: datetime.datetime = ShapeBase.NOT_SET,
    ) -> shapes.SubmitTaskStateChangeResponse:
        """
        This action is only used by the Amazon ECS agent, and it is not intended for use
        outside of the agent.

        Sent to acknowledge that a task changed states.
        """
        if _request is None:
            _params = {}
            if cluster is not ShapeBase.NOT_SET:
                _params['cluster'] = cluster
            if task is not ShapeBase.NOT_SET:
                _params['task'] = task
            if status is not ShapeBase.NOT_SET:
                _params['status'] = status
            if reason is not ShapeBase.NOT_SET:
                _params['reason'] = reason
            if containers is not ShapeBase.NOT_SET:
                _params['containers'] = containers
            if attachments is not ShapeBase.NOT_SET:
                _params['attachments'] = attachments
            if pull_started_at is not ShapeBase.NOT_SET:
                _params['pull_started_at'] = pull_started_at
            if pull_stopped_at is not ShapeBase.NOT_SET:
                _params['pull_stopped_at'] = pull_stopped_at
            if execution_stopped_at is not ShapeBase.NOT_SET:
                _params['execution_stopped_at'] = execution_stopped_at
            _request = shapes.SubmitTaskStateChangeRequest(**_params)
        response = self._boto_client.submit_task_state_change(
            **_request.to_boto()
        )

        return shapes.SubmitTaskStateChangeResponse.from_boto(response)

    def update_container_agent(
        self,
        _request: shapes.UpdateContainerAgentRequest = None,
        *,
        container_instance: str,
        cluster: str = ShapeBase.NOT_SET,
    ) -> shapes.UpdateContainerAgentResponse:
        """
        Updates the Amazon ECS container agent on a specified container instance.
        Updating the Amazon ECS container agent does not interrupt running tasks or
        services on the container instance. The process for updating the agent differs
        depending on whether your container instance was launched with the Amazon ECS-
        optimized AMI or another operating system.

        `UpdateContainerAgent` requires the Amazon ECS-optimized AMI or Amazon Linux
        with the `ecs-init` service installed and running. For help updating the Amazon
        ECS container agent on other operating systems, see [Manually Updating the
        Amazon ECS Container
        Agent](http://docs.aws.amazon.com/AmazonECS/latest/developerguide/ecs-agent-
        update.html#manually_update_agent) in the _Amazon Elastic Container Service
        Developer Guide_.
        """
        if _request is None:
            _params = {}
            if container_instance is not ShapeBase.NOT_SET:
                _params['container_instance'] = container_instance
            if cluster is not ShapeBase.NOT_SET:
                _params['cluster'] = cluster
            _request = shapes.UpdateContainerAgentRequest(**_params)
        response = self._boto_client.update_container_agent(
            **_request.to_boto()
        )

        return shapes.UpdateContainerAgentResponse.from_boto(response)

    def update_container_instances_state(
        self,
        _request: shapes.UpdateContainerInstancesStateRequest = None,
        *,
        container_instances: typing.List[str],
        status: typing.Union[str, shapes.ContainerInstanceStatus],
        cluster: str = ShapeBase.NOT_SET,
    ) -> shapes.UpdateContainerInstancesStateResponse:
        """
        Modifies the status of an Amazon ECS container instance.

        You can change the status of a container instance to `DRAINING` to manually
        remove an instance from a cluster, for example to perform system updates, update
        the Docker daemon, or scale down the cluster size.

        When you set a container instance to `DRAINING`, Amazon ECS prevents new tasks
        from being scheduled for placement on the container instance and replacement
        service tasks are started on other container instances in the cluster if the
        resources are available. Service tasks on the container instance that are in the
        `PENDING` state are stopped immediately.

        Service tasks on the container instance that are in the `RUNNING` state are
        stopped and replaced according to the service's deployment configuration
        parameters, `minimumHealthyPercent` and `maximumPercent`. You can change the
        deployment configuration of your service using UpdateService.

          * If `minimumHealthyPercent` is below 100%, the scheduler can ignore `desiredCount` temporarily during task replacement. For example, `desiredCount` is four tasks, a minimum of 50% allows the scheduler to stop two existing tasks before starting two new tasks. If the minimum is 100%, the service scheduler can't remove existing tasks until the replacement tasks are considered healthy. Tasks for services that do not use a load balancer are considered healthy if they are in the `RUNNING` state. Tasks for services that use a load balancer are considered healthy if they are in the `RUNNING` state and the container instance they are hosted on is reported as healthy by the load balancer.

          * The `maximumPercent` parameter represents an upper limit on the number of running tasks during task replacement, which enables you to define the replacement batch size. For example, if `desiredCount` of four tasks, a maximum of 200% starts four new tasks before stopping the four tasks to be drained (provided that the cluster resources required to do this are available). If the maximum is 100%, then replacement tasks can't start until the draining tasks have stopped.

        Any `PENDING` or `RUNNING` tasks that do not belong to a service are not
        affected; you must wait for them to finish or stop them manually.

        A container instance has completed draining when it has no more `RUNNING` tasks.
        You can verify this using ListTasks.

        When you set a container instance to `ACTIVE`, the Amazon ECS scheduler can
        begin scheduling tasks on the instance again.
        """
        if _request is None:
            _params = {}
            if container_instances is not ShapeBase.NOT_SET:
                _params['container_instances'] = container_instances
            if status is not ShapeBase.NOT_SET:
                _params['status'] = status
            if cluster is not ShapeBase.NOT_SET:
                _params['cluster'] = cluster
            _request = shapes.UpdateContainerInstancesStateRequest(**_params)
        response = self._boto_client.update_container_instances_state(
            **_request.to_boto()
        )

        return shapes.UpdateContainerInstancesStateResponse.from_boto(response)

    def update_service(
        self,
        _request: shapes.UpdateServiceRequest = None,
        *,
        service: str,
        cluster: str = ShapeBase.NOT_SET,
        desired_count: int = ShapeBase.NOT_SET,
        task_definition: str = ShapeBase.NOT_SET,
        deployment_configuration: shapes.DeploymentConfiguration = ShapeBase.
        NOT_SET,
        network_configuration: shapes.NetworkConfiguration = ShapeBase.NOT_SET,
        platform_version: str = ShapeBase.NOT_SET,
        force_new_deployment: bool = ShapeBase.NOT_SET,
        health_check_grace_period_seconds: int = ShapeBase.NOT_SET,
    ) -> shapes.UpdateServiceResponse:
        """
        Modifies the desired count, deployment configuration, network configuration, or
        task definition used in a service.

        You can add to or subtract from the number of instantiations of a task
        definition in a service by specifying the cluster that the service is running in
        and a new `desiredCount` parameter.

        If you have updated the Docker image of your application, you can create a new
        task definition with that image and deploy it to your service. The service
        scheduler uses the minimum healthy percent and maximum percent parameters (in
        the service's deployment configuration) to determine the deployment strategy.

        If your updated Docker image uses the same tag as what is in the existing task
        definition for your service (for example, `my_image:latest`), you do not need to
        create a new revision of your task definition. You can update the service using
        the `forceNewDeployment` option. The new tasks launched by the deployment pull
        the current image/tag combination from your repository when they start.

        You can also update the deployment configuration of a service. When a deployment
        is triggered by updating the task definition of a service, the service scheduler
        uses the deployment configuration parameters, `minimumHealthyPercent` and
        `maximumPercent`, to determine the deployment strategy.

          * If `minimumHealthyPercent` is below 100%, the scheduler can ignore `desiredCount` temporarily during a deployment. For example, if `desiredCount` is four tasks, a minimum of 50% allows the scheduler to stop two existing tasks before starting two new tasks. Tasks for services that do not use a load balancer are considered healthy if they are in the `RUNNING` state. Tasks for services that use a load balancer are considered healthy if they are in the `RUNNING` state and the container instance they are hosted on is reported as healthy by the load balancer.

          * The `maximumPercent` parameter represents an upper limit on the number of running tasks during a deployment, which enables you to define the deployment batch size. For example, if `desiredCount` is four tasks, a maximum of 200% starts four new tasks before stopping the four older tasks (provided that the cluster resources required to do this are available).

        When UpdateService stops a task during a deployment, the equivalent of `docker
        stop` is issued to the containers running in the task. This results in a
        `SIGTERM` and a 30-second timeout, after which `SIGKILL` is sent and the
        containers are forcibly stopped. If the container handles the `SIGTERM`
        gracefully and exits within 30 seconds from receiving it, no `SIGKILL` is sent.

        When the service scheduler launches new tasks, it determines task placement in
        your cluster with the following logic:

          * Determine which of the container instances in your cluster can support your service's task definition (for example, they have the required CPU, memory, ports, and container instance attributes).

          * By default, the service scheduler attempts to balance tasks across Availability Zones in this manner (although you can choose a different placement strategy):

            * Sort the valid container instances by the fewest number of running tasks for this service in the same Availability Zone as the instance. For example, if zone A has one running service task and zones B and C each have zero, valid container instances in either zone B or C are considered optimal for placement.

            * Place the new service task on a valid container instance in an optimal Availability Zone (based on the previous steps), favoring container instances with the fewest number of running tasks for this service.

        When the service scheduler stops running tasks, it attempts to maintain balance
        across the Availability Zones in your cluster using the following logic:

          * Sort the container instances by the largest number of running tasks for this service in the same Availability Zone as the instance. For example, if zone A has one running service task and zones B and C each have two, container instances in either zone B or C are considered optimal for termination.

          * Stop the task on a container instance in an optimal Availability Zone (based on the previous steps), favoring container instances with the largest number of running tasks for this service.
        """
        if _request is None:
            _params = {}
            if service is not ShapeBase.NOT_SET:
                _params['service'] = service
            if cluster is not ShapeBase.NOT_SET:
                _params['cluster'] = cluster
            if desired_count is not ShapeBase.NOT_SET:
                _params['desired_count'] = desired_count
            if task_definition is not ShapeBase.NOT_SET:
                _params['task_definition'] = task_definition
            if deployment_configuration is not ShapeBase.NOT_SET:
                _params['deployment_configuration'] = deployment_configuration
            if network_configuration is not ShapeBase.NOT_SET:
                _params['network_configuration'] = network_configuration
            if platform_version is not ShapeBase.NOT_SET:
                _params['platform_version'] = platform_version
            if force_new_deployment is not ShapeBase.NOT_SET:
                _params['force_new_deployment'] = force_new_deployment
            if health_check_grace_period_seconds is not ShapeBase.NOT_SET:
                _params['health_check_grace_period_seconds'
                       ] = health_check_grace_period_seconds
            _request = shapes.UpdateServiceRequest(**_params)
        response = self._boto_client.update_service(**_request.to_boto())

        return shapes.UpdateServiceResponse.from_boto(response)
