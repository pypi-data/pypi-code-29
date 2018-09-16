import datetime
import typing
import boto3
from autoboto import ClientBase, ShapeBase, OutputShapeBase
from . import shapes


class Client(ClientBase):
    def __init__(self, *args, **kwargs):
        super().__init__("emr", *args, **kwargs)

    def add_instance_fleet(
        self,
        _request: shapes.AddInstanceFleetInput = None,
        *,
        cluster_id: str,
        instance_fleet: shapes.InstanceFleetConfig,
    ) -> shapes.AddInstanceFleetOutput:
        """
        Adds an instance fleet to a running cluster.

        The instance fleet configuration is available only in Amazon EMR versions 4.8.0
        and later, excluding 5.0.x.
        """
        if _request is None:
            _params = {}
            if cluster_id is not ShapeBase.NOT_SET:
                _params['cluster_id'] = cluster_id
            if instance_fleet is not ShapeBase.NOT_SET:
                _params['instance_fleet'] = instance_fleet
            _request = shapes.AddInstanceFleetInput(**_params)
        response = self._boto_client.add_instance_fleet(**_request.to_boto())

        return shapes.AddInstanceFleetOutput.from_boto(response)

    def add_instance_groups(
        self,
        _request: shapes.AddInstanceGroupsInput = None,
        *,
        instance_groups: typing.List[shapes.InstanceGroupConfig],
        job_flow_id: str,
    ) -> shapes.AddInstanceGroupsOutput:
        """
        Adds one or more instance groups to a running cluster.
        """
        if _request is None:
            _params = {}
            if instance_groups is not ShapeBase.NOT_SET:
                _params['instance_groups'] = instance_groups
            if job_flow_id is not ShapeBase.NOT_SET:
                _params['job_flow_id'] = job_flow_id
            _request = shapes.AddInstanceGroupsInput(**_params)
        response = self._boto_client.add_instance_groups(**_request.to_boto())

        return shapes.AddInstanceGroupsOutput.from_boto(response)

    def add_job_flow_steps(
        self,
        _request: shapes.AddJobFlowStepsInput = None,
        *,
        job_flow_id: str,
        steps: typing.List[shapes.StepConfig],
    ) -> shapes.AddJobFlowStepsOutput:
        """
        AddJobFlowSteps adds new steps to a running cluster. A maximum of 256 steps are
        allowed in each job flow.

        If your cluster is long-running (such as a Hive data warehouse) or complex, you
        may require more than 256 steps to process your data. You can bypass the
        256-step limitation in various ways, including using SSH to connect to the
        master node and submitting queries directly to the software running on the
        master node, such as Hive and Hadoop. For more information on how to do this,
        see [Add More than 256 Steps to a
        Cluster](http://docs.aws.amazon.com/emr/latest/ManagementGuide/AddMoreThan256Steps.html)
        in the _Amazon EMR Management Guide_.

        A step specifies the location of a JAR file stored either on the master node of
        the cluster or in Amazon S3. Each step is performed by the main function of the
        main class of the JAR file. The main class can be specified either in the
        manifest of the JAR or by using the MainFunction parameter of the step.

        Amazon EMR executes each step in the order listed. For a step to be considered
        complete, the main function must exit with a zero exit code and all Hadoop jobs
        started while the step was running must have completed and run successfully.

        You can only add steps to a cluster that is in one of the following states:
        STARTING, BOOTSTRAPPING, RUNNING, or WAITING.
        """
        if _request is None:
            _params = {}
            if job_flow_id is not ShapeBase.NOT_SET:
                _params['job_flow_id'] = job_flow_id
            if steps is not ShapeBase.NOT_SET:
                _params['steps'] = steps
            _request = shapes.AddJobFlowStepsInput(**_params)
        response = self._boto_client.add_job_flow_steps(**_request.to_boto())

        return shapes.AddJobFlowStepsOutput.from_boto(response)

    def add_tags(
        self,
        _request: shapes.AddTagsInput = None,
        *,
        resource_id: str,
        tags: typing.List[shapes.Tag],
    ) -> shapes.AddTagsOutput:
        """
        Adds tags to an Amazon EMR resource. Tags make it easier to associate clusters
        in various ways, such as grouping clusters to track your Amazon EMR resource
        allocation costs. For more information, see [Tag
        Clusters](http://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-plan-
        tags.html).
        """
        if _request is None:
            _params = {}
            if resource_id is not ShapeBase.NOT_SET:
                _params['resource_id'] = resource_id
            if tags is not ShapeBase.NOT_SET:
                _params['tags'] = tags
            _request = shapes.AddTagsInput(**_params)
        response = self._boto_client.add_tags(**_request.to_boto())

        return shapes.AddTagsOutput.from_boto(response)

    def cancel_steps(
        self,
        _request: shapes.CancelStepsInput = None,
        *,
        cluster_id: str = ShapeBase.NOT_SET,
        step_ids: typing.List[str] = ShapeBase.NOT_SET,
    ) -> shapes.CancelStepsOutput:
        """
        Cancels a pending step or steps in a running cluster. Available only in Amazon
        EMR versions 4.8.0 and later, excluding version 5.0.0. A maximum of 256 steps
        are allowed in each CancelSteps request. CancelSteps is idempotent but
        asynchronous; it does not guarantee a step will be canceled, even if the request
        is successfully submitted. You can only cancel steps that are in a `PENDING`
        state.
        """
        if _request is None:
            _params = {}
            if cluster_id is not ShapeBase.NOT_SET:
                _params['cluster_id'] = cluster_id
            if step_ids is not ShapeBase.NOT_SET:
                _params['step_ids'] = step_ids
            _request = shapes.CancelStepsInput(**_params)
        response = self._boto_client.cancel_steps(**_request.to_boto())

        return shapes.CancelStepsOutput.from_boto(response)

    def create_security_configuration(
        self,
        _request: shapes.CreateSecurityConfigurationInput = None,
        *,
        name: str,
        security_configuration: str,
    ) -> shapes.CreateSecurityConfigurationOutput:
        """
        Creates a security configuration, which is stored in the service and can be
        specified when a cluster is created.
        """
        if _request is None:
            _params = {}
            if name is not ShapeBase.NOT_SET:
                _params['name'] = name
            if security_configuration is not ShapeBase.NOT_SET:
                _params['security_configuration'] = security_configuration
            _request = shapes.CreateSecurityConfigurationInput(**_params)
        response = self._boto_client.create_security_configuration(
            **_request.to_boto()
        )

        return shapes.CreateSecurityConfigurationOutput.from_boto(response)

    def delete_security_configuration(
        self,
        _request: shapes.DeleteSecurityConfigurationInput = None,
        *,
        name: str,
    ) -> shapes.DeleteSecurityConfigurationOutput:
        """
        Deletes a security configuration.
        """
        if _request is None:
            _params = {}
            if name is not ShapeBase.NOT_SET:
                _params['name'] = name
            _request = shapes.DeleteSecurityConfigurationInput(**_params)
        response = self._boto_client.delete_security_configuration(
            **_request.to_boto()
        )

        return shapes.DeleteSecurityConfigurationOutput.from_boto(response)

    def describe_cluster(
        self,
        _request: shapes.DescribeClusterInput = None,
        *,
        cluster_id: str,
    ) -> shapes.DescribeClusterOutput:
        """
        Provides cluster-level details including status, hardware and software
        configuration, VPC settings, and so on.
        """
        if _request is None:
            _params = {}
            if cluster_id is not ShapeBase.NOT_SET:
                _params['cluster_id'] = cluster_id
            _request = shapes.DescribeClusterInput(**_params)
        response = self._boto_client.describe_cluster(**_request.to_boto())

        return shapes.DescribeClusterOutput.from_boto(response)

    def describe_job_flows(
        self,
        _request: shapes.DescribeJobFlowsInput = None,
        *,
        created_after: datetime.datetime = ShapeBase.NOT_SET,
        created_before: datetime.datetime = ShapeBase.NOT_SET,
        job_flow_ids: typing.List[str] = ShapeBase.NOT_SET,
        job_flow_states: typing.List[typing.Union[str, shapes.
                                                  JobFlowExecutionState]
                                    ] = ShapeBase.NOT_SET,
    ) -> shapes.DescribeJobFlowsOutput:
        """
        This API is deprecated and will eventually be removed. We recommend you use
        ListClusters, DescribeCluster, ListSteps, ListInstanceGroups and
        ListBootstrapActions instead.

        DescribeJobFlows returns a list of job flows that match all of the supplied
        parameters. The parameters can include a list of job flow IDs, job flow states,
        and restrictions on job flow creation date and time.

        Regardless of supplied parameters, only job flows created within the last two
        months are returned.

        If no parameters are supplied, then job flows matching either of the following
        criteria are returned:

          * Job flows created and completed in the last two weeks

          * Job flows created within the last two months that are in one of the following states: `RUNNING`, `WAITING`, `SHUTTING_DOWN`, `STARTING`

        Amazon EMR can return a maximum of 512 job flow descriptions.
        """
        if _request is None:
            _params = {}
            if created_after is not ShapeBase.NOT_SET:
                _params['created_after'] = created_after
            if created_before is not ShapeBase.NOT_SET:
                _params['created_before'] = created_before
            if job_flow_ids is not ShapeBase.NOT_SET:
                _params['job_flow_ids'] = job_flow_ids
            if job_flow_states is not ShapeBase.NOT_SET:
                _params['job_flow_states'] = job_flow_states
            _request = shapes.DescribeJobFlowsInput(**_params)
        response = self._boto_client.describe_job_flows(**_request.to_boto())

        return shapes.DescribeJobFlowsOutput.from_boto(response)

    def describe_security_configuration(
        self,
        _request: shapes.DescribeSecurityConfigurationInput = None,
        *,
        name: str,
    ) -> shapes.DescribeSecurityConfigurationOutput:
        """
        Provides the details of a security configuration by returning the configuration
        JSON.
        """
        if _request is None:
            _params = {}
            if name is not ShapeBase.NOT_SET:
                _params['name'] = name
            _request = shapes.DescribeSecurityConfigurationInput(**_params)
        response = self._boto_client.describe_security_configuration(
            **_request.to_boto()
        )

        return shapes.DescribeSecurityConfigurationOutput.from_boto(response)

    def describe_step(
        self,
        _request: shapes.DescribeStepInput = None,
        *,
        cluster_id: str,
        step_id: str,
    ) -> shapes.DescribeStepOutput:
        """
        Provides more detail about the cluster step.
        """
        if _request is None:
            _params = {}
            if cluster_id is not ShapeBase.NOT_SET:
                _params['cluster_id'] = cluster_id
            if step_id is not ShapeBase.NOT_SET:
                _params['step_id'] = step_id
            _request = shapes.DescribeStepInput(**_params)
        response = self._boto_client.describe_step(**_request.to_boto())

        return shapes.DescribeStepOutput.from_boto(response)

    def list_bootstrap_actions(
        self,
        _request: shapes.ListBootstrapActionsInput = None,
        *,
        cluster_id: str,
        marker: str = ShapeBase.NOT_SET,
    ) -> shapes.ListBootstrapActionsOutput:
        """
        Provides information about the bootstrap actions associated with a cluster.
        """
        if _request is None:
            _params = {}
            if cluster_id is not ShapeBase.NOT_SET:
                _params['cluster_id'] = cluster_id
            if marker is not ShapeBase.NOT_SET:
                _params['marker'] = marker
            _request = shapes.ListBootstrapActionsInput(**_params)
        paginator = self.get_paginator("list_bootstrap_actions").paginate(
            **_request.to_boto()
        )
        page_generator = (page for page in paginator)
        first_page = next(page_generator)
        result = shapes.ListBootstrapActionsOutput.from_boto(first_page)
        result._page_iterator = page_generator
        return result

        return shapes.ListBootstrapActionsOutput.from_boto(response)

    def list_clusters(
        self,
        _request: shapes.ListClustersInput = None,
        *,
        created_after: datetime.datetime = ShapeBase.NOT_SET,
        created_before: datetime.datetime = ShapeBase.NOT_SET,
        cluster_states: typing.List[typing.Union[str, shapes.ClusterState]
                                   ] = ShapeBase.NOT_SET,
        marker: str = ShapeBase.NOT_SET,
    ) -> shapes.ListClustersOutput:
        """
        Provides the status of all clusters visible to this AWS account. Allows you to
        filter the list of clusters based on certain criteria; for example, filtering by
        cluster creation date and time or by status. This call returns a maximum of 50
        clusters per call, but returns a marker to track the paging of the cluster list
        across multiple ListClusters calls.
        """
        if _request is None:
            _params = {}
            if created_after is not ShapeBase.NOT_SET:
                _params['created_after'] = created_after
            if created_before is not ShapeBase.NOT_SET:
                _params['created_before'] = created_before
            if cluster_states is not ShapeBase.NOT_SET:
                _params['cluster_states'] = cluster_states
            if marker is not ShapeBase.NOT_SET:
                _params['marker'] = marker
            _request = shapes.ListClustersInput(**_params)
        paginator = self.get_paginator("list_clusters").paginate(
            **_request.to_boto()
        )
        page_generator = (page for page in paginator)
        first_page = next(page_generator)
        result = shapes.ListClustersOutput.from_boto(first_page)
        result._page_iterator = page_generator
        return result

        return shapes.ListClustersOutput.from_boto(response)

    def list_instance_fleets(
        self,
        _request: shapes.ListInstanceFleetsInput = None,
        *,
        cluster_id: str,
        marker: str = ShapeBase.NOT_SET,
    ) -> shapes.ListInstanceFleetsOutput:
        """
        Lists all available details about the instance fleets in a cluster.

        The instance fleet configuration is available only in Amazon EMR versions 4.8.0
        and later, excluding 5.0.x versions.
        """
        if _request is None:
            _params = {}
            if cluster_id is not ShapeBase.NOT_SET:
                _params['cluster_id'] = cluster_id
            if marker is not ShapeBase.NOT_SET:
                _params['marker'] = marker
            _request = shapes.ListInstanceFleetsInput(**_params)
        paginator = self.get_paginator("list_instance_fleets").paginate(
            **_request.to_boto()
        )
        page_generator = (page for page in paginator)
        first_page = next(page_generator)
        result = shapes.ListInstanceFleetsOutput.from_boto(first_page)
        result._page_iterator = page_generator
        return result

        return shapes.ListInstanceFleetsOutput.from_boto(response)

    def list_instance_groups(
        self,
        _request: shapes.ListInstanceGroupsInput = None,
        *,
        cluster_id: str,
        marker: str = ShapeBase.NOT_SET,
    ) -> shapes.ListInstanceGroupsOutput:
        """
        Provides all available details about the instance groups in a cluster.
        """
        if _request is None:
            _params = {}
            if cluster_id is not ShapeBase.NOT_SET:
                _params['cluster_id'] = cluster_id
            if marker is not ShapeBase.NOT_SET:
                _params['marker'] = marker
            _request = shapes.ListInstanceGroupsInput(**_params)
        paginator = self.get_paginator("list_instance_groups").paginate(
            **_request.to_boto()
        )
        page_generator = (page for page in paginator)
        first_page = next(page_generator)
        result = shapes.ListInstanceGroupsOutput.from_boto(first_page)
        result._page_iterator = page_generator
        return result

        return shapes.ListInstanceGroupsOutput.from_boto(response)

    def list_instances(
        self,
        _request: shapes.ListInstancesInput = None,
        *,
        cluster_id: str,
        instance_group_id: str = ShapeBase.NOT_SET,
        instance_group_types: typing.List[
            typing.Union[str, shapes.InstanceGroupType]] = ShapeBase.NOT_SET,
        instance_fleet_id: str = ShapeBase.NOT_SET,
        instance_fleet_type: typing.
        Union[str, shapes.InstanceFleetType] = ShapeBase.NOT_SET,
        instance_states: typing.List[typing.Union[str, shapes.InstanceState]
                                    ] = ShapeBase.NOT_SET,
        marker: str = ShapeBase.NOT_SET,
    ) -> shapes.ListInstancesOutput:
        """
        Provides information for all active EC2 instances and EC2 instances terminated
        in the last 30 days, up to a maximum of 2,000. EC2 instances in any of the
        following states are considered active: AWAITING_FULFILLMENT, PROVISIONING,
        BOOTSTRAPPING, RUNNING.
        """
        if _request is None:
            _params = {}
            if cluster_id is not ShapeBase.NOT_SET:
                _params['cluster_id'] = cluster_id
            if instance_group_id is not ShapeBase.NOT_SET:
                _params['instance_group_id'] = instance_group_id
            if instance_group_types is not ShapeBase.NOT_SET:
                _params['instance_group_types'] = instance_group_types
            if instance_fleet_id is not ShapeBase.NOT_SET:
                _params['instance_fleet_id'] = instance_fleet_id
            if instance_fleet_type is not ShapeBase.NOT_SET:
                _params['instance_fleet_type'] = instance_fleet_type
            if instance_states is not ShapeBase.NOT_SET:
                _params['instance_states'] = instance_states
            if marker is not ShapeBase.NOT_SET:
                _params['marker'] = marker
            _request = shapes.ListInstancesInput(**_params)
        paginator = self.get_paginator("list_instances").paginate(
            **_request.to_boto()
        )
        page_generator = (page for page in paginator)
        first_page = next(page_generator)
        result = shapes.ListInstancesOutput.from_boto(first_page)
        result._page_iterator = page_generator
        return result

        return shapes.ListInstancesOutput.from_boto(response)

    def list_security_configurations(
        self,
        _request: shapes.ListSecurityConfigurationsInput = None,
        *,
        marker: str = ShapeBase.NOT_SET,
    ) -> shapes.ListSecurityConfigurationsOutput:
        """
        Lists all the security configurations visible to this account, providing their
        creation dates and times, and their names. This call returns a maximum of 50
        clusters per call, but returns a marker to track the paging of the cluster list
        across multiple ListSecurityConfigurations calls.
        """
        if _request is None:
            _params = {}
            if marker is not ShapeBase.NOT_SET:
                _params['marker'] = marker
            _request = shapes.ListSecurityConfigurationsInput(**_params)
        response = self._boto_client.list_security_configurations(
            **_request.to_boto()
        )

        return shapes.ListSecurityConfigurationsOutput.from_boto(response)

    def list_steps(
        self,
        _request: shapes.ListStepsInput = None,
        *,
        cluster_id: str,
        step_states: typing.List[typing.Union[str, shapes.StepState]
                                ] = ShapeBase.NOT_SET,
        step_ids: typing.List[str] = ShapeBase.NOT_SET,
        marker: str = ShapeBase.NOT_SET,
    ) -> shapes.ListStepsOutput:
        """
        Provides a list of steps for the cluster in reverse order unless you specify
        stepIds with the request.
        """
        if _request is None:
            _params = {}
            if cluster_id is not ShapeBase.NOT_SET:
                _params['cluster_id'] = cluster_id
            if step_states is not ShapeBase.NOT_SET:
                _params['step_states'] = step_states
            if step_ids is not ShapeBase.NOT_SET:
                _params['step_ids'] = step_ids
            if marker is not ShapeBase.NOT_SET:
                _params['marker'] = marker
            _request = shapes.ListStepsInput(**_params)
        paginator = self.get_paginator("list_steps").paginate(
            **_request.to_boto()
        )
        page_generator = (page for page in paginator)
        first_page = next(page_generator)
        result = shapes.ListStepsOutput.from_boto(first_page)
        result._page_iterator = page_generator
        return result

        return shapes.ListStepsOutput.from_boto(response)

    def modify_instance_fleet(
        self,
        _request: shapes.ModifyInstanceFleetInput = None,
        *,
        cluster_id: str,
        instance_fleet: shapes.InstanceFleetModifyConfig,
    ) -> None:
        """
        Modifies the target On-Demand and target Spot capacities for the instance fleet
        with the specified InstanceFleetID within the cluster specified using ClusterID.
        The call either succeeds or fails atomically.

        The instance fleet configuration is available only in Amazon EMR versions 4.8.0
        and later, excluding 5.0.x versions.
        """
        if _request is None:
            _params = {}
            if cluster_id is not ShapeBase.NOT_SET:
                _params['cluster_id'] = cluster_id
            if instance_fleet is not ShapeBase.NOT_SET:
                _params['instance_fleet'] = instance_fleet
            _request = shapes.ModifyInstanceFleetInput(**_params)
        response = self._boto_client.modify_instance_fleet(**_request.to_boto())

    def modify_instance_groups(
        self,
        _request: shapes.ModifyInstanceGroupsInput = None,
        *,
        cluster_id: str = ShapeBase.NOT_SET,
        instance_groups: typing.List[shapes.InstanceGroupModifyConfig
                                    ] = ShapeBase.NOT_SET,
    ) -> None:
        """
        ModifyInstanceGroups modifies the number of nodes and configuration settings of
        an instance group. The input parameters include the new target instance count
        for the group and the instance group ID. The call will either succeed or fail
        atomically.
        """
        if _request is None:
            _params = {}
            if cluster_id is not ShapeBase.NOT_SET:
                _params['cluster_id'] = cluster_id
            if instance_groups is not ShapeBase.NOT_SET:
                _params['instance_groups'] = instance_groups
            _request = shapes.ModifyInstanceGroupsInput(**_params)
        response = self._boto_client.modify_instance_groups(
            **_request.to_boto()
        )

    def put_auto_scaling_policy(
        self,
        _request: shapes.PutAutoScalingPolicyInput = None,
        *,
        cluster_id: str,
        instance_group_id: str,
        auto_scaling_policy: shapes.AutoScalingPolicy,
    ) -> shapes.PutAutoScalingPolicyOutput:
        """
        Creates or updates an automatic scaling policy for a core instance group or task
        instance group in an Amazon EMR cluster. The automatic scaling policy defines
        how an instance group dynamically adds and terminates EC2 instances in response
        to the value of a CloudWatch metric.
        """
        if _request is None:
            _params = {}
            if cluster_id is not ShapeBase.NOT_SET:
                _params['cluster_id'] = cluster_id
            if instance_group_id is not ShapeBase.NOT_SET:
                _params['instance_group_id'] = instance_group_id
            if auto_scaling_policy is not ShapeBase.NOT_SET:
                _params['auto_scaling_policy'] = auto_scaling_policy
            _request = shapes.PutAutoScalingPolicyInput(**_params)
        response = self._boto_client.put_auto_scaling_policy(
            **_request.to_boto()
        )

        return shapes.PutAutoScalingPolicyOutput.from_boto(response)

    def remove_auto_scaling_policy(
        self,
        _request: shapes.RemoveAutoScalingPolicyInput = None,
        *,
        cluster_id: str,
        instance_group_id: str,
    ) -> shapes.RemoveAutoScalingPolicyOutput:
        """
        Removes an automatic scaling policy from a specified instance group within an
        EMR cluster.
        """
        if _request is None:
            _params = {}
            if cluster_id is not ShapeBase.NOT_SET:
                _params['cluster_id'] = cluster_id
            if instance_group_id is not ShapeBase.NOT_SET:
                _params['instance_group_id'] = instance_group_id
            _request = shapes.RemoveAutoScalingPolicyInput(**_params)
        response = self._boto_client.remove_auto_scaling_policy(
            **_request.to_boto()
        )

        return shapes.RemoveAutoScalingPolicyOutput.from_boto(response)

    def remove_tags(
        self,
        _request: shapes.RemoveTagsInput = None,
        *,
        resource_id: str,
        tag_keys: typing.List[str],
    ) -> shapes.RemoveTagsOutput:
        """
        Removes tags from an Amazon EMR resource. Tags make it easier to associate
        clusters in various ways, such as grouping clusters to track your Amazon EMR
        resource allocation costs. For more information, see [Tag
        Clusters](http://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-plan-
        tags.html).

        The following example removes the stack tag with value Prod from a cluster:
        """
        if _request is None:
            _params = {}
            if resource_id is not ShapeBase.NOT_SET:
                _params['resource_id'] = resource_id
            if tag_keys is not ShapeBase.NOT_SET:
                _params['tag_keys'] = tag_keys
            _request = shapes.RemoveTagsInput(**_params)
        response = self._boto_client.remove_tags(**_request.to_boto())

        return shapes.RemoveTagsOutput.from_boto(response)

    def run_job_flow(
        self,
        _request: shapes.RunJobFlowInput = None,
        *,
        name: str,
        instances: shapes.JobFlowInstancesConfig,
        log_uri: str = ShapeBase.NOT_SET,
        additional_info: str = ShapeBase.NOT_SET,
        ami_version: str = ShapeBase.NOT_SET,
        release_label: str = ShapeBase.NOT_SET,
        steps: typing.List[shapes.StepConfig] = ShapeBase.NOT_SET,
        bootstrap_actions: typing.List[shapes.BootstrapActionConfig
                                      ] = ShapeBase.NOT_SET,
        supported_products: typing.List[str] = ShapeBase.NOT_SET,
        new_supported_products: typing.List[shapes.SupportedProductConfig
                                           ] = ShapeBase.NOT_SET,
        applications: typing.List[shapes.Application] = ShapeBase.NOT_SET,
        configurations: typing.List[shapes.Configuration] = ShapeBase.NOT_SET,
        visible_to_all_users: bool = ShapeBase.NOT_SET,
        job_flow_role: str = ShapeBase.NOT_SET,
        service_role: str = ShapeBase.NOT_SET,
        tags: typing.List[shapes.Tag] = ShapeBase.NOT_SET,
        security_configuration: str = ShapeBase.NOT_SET,
        auto_scaling_role: str = ShapeBase.NOT_SET,
        scale_down_behavior: typing.
        Union[str, shapes.ScaleDownBehavior] = ShapeBase.NOT_SET,
        custom_ami_id: str = ShapeBase.NOT_SET,
        ebs_root_volume_size: int = ShapeBase.NOT_SET,
        repo_upgrade_on_boot: typing.
        Union[str, shapes.RepoUpgradeOnBoot] = ShapeBase.NOT_SET,
        kerberos_attributes: shapes.KerberosAttributes = ShapeBase.NOT_SET,
    ) -> shapes.RunJobFlowOutput:
        """
        RunJobFlow creates and starts running a new cluster (job flow). The cluster runs
        the steps specified. After the steps complete, the cluster stops and the HDFS
        partition is lost. To prevent loss of data, configure the last step of the job
        flow to store results in Amazon S3. If the JobFlowInstancesConfig
        `KeepJobFlowAliveWhenNoSteps` parameter is set to `TRUE`, the cluster
        transitions to the WAITING state rather than shutting down after the steps have
        completed.

        For additional protection, you can set the JobFlowInstancesConfig
        `TerminationProtected` parameter to `TRUE` to lock the cluster and prevent it
        from being terminated by API call, user intervention, or in the event of a job
        flow error.

        A maximum of 256 steps are allowed in each job flow.

        If your cluster is long-running (such as a Hive data warehouse) or complex, you
        may require more than 256 steps to process your data. You can bypass the
        256-step limitation in various ways, including using the SSH shell to connect to
        the master node and submitting queries directly to the software running on the
        master node, such as Hive and Hadoop. For more information on how to do this,
        see [Add More than 256 Steps to a
        Cluster](http://docs.aws.amazon.com/emr/latest/ManagementGuide/AddMoreThan256Steps.html)
        in the _Amazon EMR Management Guide_.

        For long running clusters, we recommend that you periodically store your
        results.

        The instance fleets configuration is available only in Amazon EMR versions 4.8.0
        and later, excluding 5.0.x versions. The RunJobFlow request can contain
        InstanceFleets parameters or InstanceGroups parameters, but not both.
        """
        if _request is None:
            _params = {}
            if name is not ShapeBase.NOT_SET:
                _params['name'] = name
            if instances is not ShapeBase.NOT_SET:
                _params['instances'] = instances
            if log_uri is not ShapeBase.NOT_SET:
                _params['log_uri'] = log_uri
            if additional_info is not ShapeBase.NOT_SET:
                _params['additional_info'] = additional_info
            if ami_version is not ShapeBase.NOT_SET:
                _params['ami_version'] = ami_version
            if release_label is not ShapeBase.NOT_SET:
                _params['release_label'] = release_label
            if steps is not ShapeBase.NOT_SET:
                _params['steps'] = steps
            if bootstrap_actions is not ShapeBase.NOT_SET:
                _params['bootstrap_actions'] = bootstrap_actions
            if supported_products is not ShapeBase.NOT_SET:
                _params['supported_products'] = supported_products
            if new_supported_products is not ShapeBase.NOT_SET:
                _params['new_supported_products'] = new_supported_products
            if applications is not ShapeBase.NOT_SET:
                _params['applications'] = applications
            if configurations is not ShapeBase.NOT_SET:
                _params['configurations'] = configurations
            if visible_to_all_users is not ShapeBase.NOT_SET:
                _params['visible_to_all_users'] = visible_to_all_users
            if job_flow_role is not ShapeBase.NOT_SET:
                _params['job_flow_role'] = job_flow_role
            if service_role is not ShapeBase.NOT_SET:
                _params['service_role'] = service_role
            if tags is not ShapeBase.NOT_SET:
                _params['tags'] = tags
            if security_configuration is not ShapeBase.NOT_SET:
                _params['security_configuration'] = security_configuration
            if auto_scaling_role is not ShapeBase.NOT_SET:
                _params['auto_scaling_role'] = auto_scaling_role
            if scale_down_behavior is not ShapeBase.NOT_SET:
                _params['scale_down_behavior'] = scale_down_behavior
            if custom_ami_id is not ShapeBase.NOT_SET:
                _params['custom_ami_id'] = custom_ami_id
            if ebs_root_volume_size is not ShapeBase.NOT_SET:
                _params['ebs_root_volume_size'] = ebs_root_volume_size
            if repo_upgrade_on_boot is not ShapeBase.NOT_SET:
                _params['repo_upgrade_on_boot'] = repo_upgrade_on_boot
            if kerberos_attributes is not ShapeBase.NOT_SET:
                _params['kerberos_attributes'] = kerberos_attributes
            _request = shapes.RunJobFlowInput(**_params)
        response = self._boto_client.run_job_flow(**_request.to_boto())

        return shapes.RunJobFlowOutput.from_boto(response)

    def set_termination_protection(
        self,
        _request: shapes.SetTerminationProtectionInput = None,
        *,
        job_flow_ids: typing.List[str],
        termination_protected: bool,
    ) -> None:
        """
        SetTerminationProtection locks a cluster (job flow) so the EC2 instances in the
        cluster cannot be terminated by user intervention, an API call, or in the event
        of a job-flow error. The cluster still terminates upon successful completion of
        the job flow. Calling `SetTerminationProtection` on a cluster is similar to
        calling the Amazon EC2 `DisableAPITermination` API on all EC2 instances in a
        cluster.

        `SetTerminationProtection` is used to prevent accidental termination of a
        cluster and to ensure that in the event of an error, the instances persist so
        that you can recover any data stored in their ephemeral instance storage.

        To terminate a cluster that has been locked by setting
        `SetTerminationProtection` to `true`, you must first unlock the job flow by a
        subsequent call to `SetTerminationProtection` in which you set the value to
        `false`.

        For more information, see[Managing Cluster
        Termination](http://docs.aws.amazon.com/emr/latest/ManagementGuide/UsingEMR_TerminationProtection.html)
        in the _Amazon EMR Management Guide_.
        """
        if _request is None:
            _params = {}
            if job_flow_ids is not ShapeBase.NOT_SET:
                _params['job_flow_ids'] = job_flow_ids
            if termination_protected is not ShapeBase.NOT_SET:
                _params['termination_protected'] = termination_protected
            _request = shapes.SetTerminationProtectionInput(**_params)
        response = self._boto_client.set_termination_protection(
            **_request.to_boto()
        )

    def set_visible_to_all_users(
        self,
        _request: shapes.SetVisibleToAllUsersInput = None,
        *,
        job_flow_ids: typing.List[str],
        visible_to_all_users: bool,
    ) -> None:
        """
        Sets whether all AWS Identity and Access Management (IAM) users under your
        account can access the specified clusters (job flows). This action works on
        running clusters. You can also set the visibility of a cluster when you launch
        it using the `VisibleToAllUsers` parameter of RunJobFlow. The
        SetVisibleToAllUsers action can be called only by an IAM user who created the
        cluster or the AWS account that owns the cluster.
        """
        if _request is None:
            _params = {}
            if job_flow_ids is not ShapeBase.NOT_SET:
                _params['job_flow_ids'] = job_flow_ids
            if visible_to_all_users is not ShapeBase.NOT_SET:
                _params['visible_to_all_users'] = visible_to_all_users
            _request = shapes.SetVisibleToAllUsersInput(**_params)
        response = self._boto_client.set_visible_to_all_users(
            **_request.to_boto()
        )

    def terminate_job_flows(
        self,
        _request: shapes.TerminateJobFlowsInput = None,
        *,
        job_flow_ids: typing.List[str],
    ) -> None:
        """
        TerminateJobFlows shuts a list of clusters (job flows) down. When a job flow is
        shut down, any step not yet completed is canceled and the EC2 instances on which
        the cluster is running are stopped. Any log files not already saved are uploaded
        to Amazon S3 if a LogUri was specified when the cluster was created.

        The maximum number of clusters allowed is 10. The call to `TerminateJobFlows` is
        asynchronous. Depending on the configuration of the cluster, it may take up to
        1-5 minutes for the cluster to completely terminate and release allocated
        resources, such as Amazon EC2 instances.
        """
        if _request is None:
            _params = {}
            if job_flow_ids is not ShapeBase.NOT_SET:
                _params['job_flow_ids'] = job_flow_ids
            _request = shapes.TerminateJobFlowsInput(**_params)
        response = self._boto_client.terminate_job_flows(**_request.to_boto())
