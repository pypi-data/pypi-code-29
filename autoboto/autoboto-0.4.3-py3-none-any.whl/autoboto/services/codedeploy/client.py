import datetime
import typing
import boto3
from autoboto import ClientBase, ShapeBase, OutputShapeBase
from . import shapes


class Client(ClientBase):
    def __init__(self, *args, **kwargs):
        super().__init__("codedeploy", *args, **kwargs)

    def add_tags_to_on_premises_instances(
        self,
        _request: shapes.AddTagsToOnPremisesInstancesInput = None,
        *,
        tags: typing.List[shapes.Tag],
        instance_names: typing.List[str],
    ) -> None:
        """
        Adds tags to on-premises instances.
        """
        if _request is None:
            _params = {}
            if tags is not ShapeBase.NOT_SET:
                _params['tags'] = tags
            if instance_names is not ShapeBase.NOT_SET:
                _params['instance_names'] = instance_names
            _request = shapes.AddTagsToOnPremisesInstancesInput(**_params)
        response = self._boto_client.add_tags_to_on_premises_instances(
            **_request.to_boto()
        )

    def batch_get_application_revisions(
        self,
        _request: shapes.BatchGetApplicationRevisionsInput = None,
        *,
        application_name: str,
        revisions: typing.List[shapes.RevisionLocation],
    ) -> shapes.BatchGetApplicationRevisionsOutput:
        """
        Gets information about one or more application revisions.
        """
        if _request is None:
            _params = {}
            if application_name is not ShapeBase.NOT_SET:
                _params['application_name'] = application_name
            if revisions is not ShapeBase.NOT_SET:
                _params['revisions'] = revisions
            _request = shapes.BatchGetApplicationRevisionsInput(**_params)
        response = self._boto_client.batch_get_application_revisions(
            **_request.to_boto()
        )

        return shapes.BatchGetApplicationRevisionsOutput.from_boto(response)

    def batch_get_applications(
        self,
        _request: shapes.BatchGetApplicationsInput = None,
        *,
        application_names: typing.List[str],
    ) -> shapes.BatchGetApplicationsOutput:
        """
        Gets information about one or more applications.
        """
        if _request is None:
            _params = {}
            if application_names is not ShapeBase.NOT_SET:
                _params['application_names'] = application_names
            _request = shapes.BatchGetApplicationsInput(**_params)
        response = self._boto_client.batch_get_applications(
            **_request.to_boto()
        )

        return shapes.BatchGetApplicationsOutput.from_boto(response)

    def batch_get_deployment_groups(
        self,
        _request: shapes.BatchGetDeploymentGroupsInput = None,
        *,
        application_name: str,
        deployment_group_names: typing.List[str],
    ) -> shapes.BatchGetDeploymentGroupsOutput:
        """
        Gets information about one or more deployment groups.
        """
        if _request is None:
            _params = {}
            if application_name is not ShapeBase.NOT_SET:
                _params['application_name'] = application_name
            if deployment_group_names is not ShapeBase.NOT_SET:
                _params['deployment_group_names'] = deployment_group_names
            _request = shapes.BatchGetDeploymentGroupsInput(**_params)
        response = self._boto_client.batch_get_deployment_groups(
            **_request.to_boto()
        )

        return shapes.BatchGetDeploymentGroupsOutput.from_boto(response)

    def batch_get_deployment_instances(
        self,
        _request: shapes.BatchGetDeploymentInstancesInput = None,
        *,
        deployment_id: str,
        instance_ids: typing.List[str],
    ) -> shapes.BatchGetDeploymentInstancesOutput:
        """
        Gets information about one or more instance that are part of a deployment group.
        """
        if _request is None:
            _params = {}
            if deployment_id is not ShapeBase.NOT_SET:
                _params['deployment_id'] = deployment_id
            if instance_ids is not ShapeBase.NOT_SET:
                _params['instance_ids'] = instance_ids
            _request = shapes.BatchGetDeploymentInstancesInput(**_params)
        response = self._boto_client.batch_get_deployment_instances(
            **_request.to_boto()
        )

        return shapes.BatchGetDeploymentInstancesOutput.from_boto(response)

    def batch_get_deployments(
        self,
        _request: shapes.BatchGetDeploymentsInput = None,
        *,
        deployment_ids: typing.List[str],
    ) -> shapes.BatchGetDeploymentsOutput:
        """
        Gets information about one or more deployments.
        """
        if _request is None:
            _params = {}
            if deployment_ids is not ShapeBase.NOT_SET:
                _params['deployment_ids'] = deployment_ids
            _request = shapes.BatchGetDeploymentsInput(**_params)
        response = self._boto_client.batch_get_deployments(**_request.to_boto())

        return shapes.BatchGetDeploymentsOutput.from_boto(response)

    def batch_get_on_premises_instances(
        self,
        _request: shapes.BatchGetOnPremisesInstancesInput = None,
        *,
        instance_names: typing.List[str],
    ) -> shapes.BatchGetOnPremisesInstancesOutput:
        """
        Gets information about one or more on-premises instances.
        """
        if _request is None:
            _params = {}
            if instance_names is not ShapeBase.NOT_SET:
                _params['instance_names'] = instance_names
            _request = shapes.BatchGetOnPremisesInstancesInput(**_params)
        response = self._boto_client.batch_get_on_premises_instances(
            **_request.to_boto()
        )

        return shapes.BatchGetOnPremisesInstancesOutput.from_boto(response)

    def continue_deployment(
        self,
        _request: shapes.ContinueDeploymentInput = None,
        *,
        deployment_id: str = ShapeBase.NOT_SET,
    ) -> None:
        """
        For a blue/green deployment, starts the process of rerouting traffic from
        instances in the original environment to instances in the replacement
        environment without waiting for a specified wait time to elapse. (Traffic
        rerouting, which is achieved by registering instances in the replacement
        environment with the load balancer, can start as soon as all instances have a
        status of Ready.)
        """
        if _request is None:
            _params = {}
            if deployment_id is not ShapeBase.NOT_SET:
                _params['deployment_id'] = deployment_id
            _request = shapes.ContinueDeploymentInput(**_params)
        response = self._boto_client.continue_deployment(**_request.to_boto())

    def create_application(
        self,
        _request: shapes.CreateApplicationInput = None,
        *,
        application_name: str,
        compute_platform: typing.Union[str, shapes.ComputePlatform] = ShapeBase.
        NOT_SET,
    ) -> shapes.CreateApplicationOutput:
        """
        Creates an application.
        """
        if _request is None:
            _params = {}
            if application_name is not ShapeBase.NOT_SET:
                _params['application_name'] = application_name
            if compute_platform is not ShapeBase.NOT_SET:
                _params['compute_platform'] = compute_platform
            _request = shapes.CreateApplicationInput(**_params)
        response = self._boto_client.create_application(**_request.to_boto())

        return shapes.CreateApplicationOutput.from_boto(response)

    def create_deployment(
        self,
        _request: shapes.CreateDeploymentInput = None,
        *,
        application_name: str,
        deployment_group_name: str = ShapeBase.NOT_SET,
        revision: shapes.RevisionLocation = ShapeBase.NOT_SET,
        deployment_config_name: str = ShapeBase.NOT_SET,
        description: str = ShapeBase.NOT_SET,
        ignore_application_stop_failures: bool = ShapeBase.NOT_SET,
        target_instances: shapes.TargetInstances = ShapeBase.NOT_SET,
        auto_rollback_configuration: shapes.
        AutoRollbackConfiguration = ShapeBase.NOT_SET,
        update_outdated_instances_only: bool = ShapeBase.NOT_SET,
        file_exists_behavior: typing.
        Union[str, shapes.FileExistsBehavior] = ShapeBase.NOT_SET,
    ) -> shapes.CreateDeploymentOutput:
        """
        Deploys an application revision through the specified deployment group.
        """
        if _request is None:
            _params = {}
            if application_name is not ShapeBase.NOT_SET:
                _params['application_name'] = application_name
            if deployment_group_name is not ShapeBase.NOT_SET:
                _params['deployment_group_name'] = deployment_group_name
            if revision is not ShapeBase.NOT_SET:
                _params['revision'] = revision
            if deployment_config_name is not ShapeBase.NOT_SET:
                _params['deployment_config_name'] = deployment_config_name
            if description is not ShapeBase.NOT_SET:
                _params['description'] = description
            if ignore_application_stop_failures is not ShapeBase.NOT_SET:
                _params['ignore_application_stop_failures'
                       ] = ignore_application_stop_failures
            if target_instances is not ShapeBase.NOT_SET:
                _params['target_instances'] = target_instances
            if auto_rollback_configuration is not ShapeBase.NOT_SET:
                _params['auto_rollback_configuration'
                       ] = auto_rollback_configuration
            if update_outdated_instances_only is not ShapeBase.NOT_SET:
                _params['update_outdated_instances_only'
                       ] = update_outdated_instances_only
            if file_exists_behavior is not ShapeBase.NOT_SET:
                _params['file_exists_behavior'] = file_exists_behavior
            _request = shapes.CreateDeploymentInput(**_params)
        response = self._boto_client.create_deployment(**_request.to_boto())

        return shapes.CreateDeploymentOutput.from_boto(response)

    def create_deployment_config(
        self,
        _request: shapes.CreateDeploymentConfigInput = None,
        *,
        deployment_config_name: str,
        minimum_healthy_hosts: shapes.MinimumHealthyHosts = ShapeBase.NOT_SET,
        traffic_routing_config: shapes.TrafficRoutingConfig = ShapeBase.NOT_SET,
        compute_platform: typing.Union[str, shapes.ComputePlatform] = ShapeBase.
        NOT_SET,
    ) -> shapes.CreateDeploymentConfigOutput:
        """
        Creates a deployment configuration.
        """
        if _request is None:
            _params = {}
            if deployment_config_name is not ShapeBase.NOT_SET:
                _params['deployment_config_name'] = deployment_config_name
            if minimum_healthy_hosts is not ShapeBase.NOT_SET:
                _params['minimum_healthy_hosts'] = minimum_healthy_hosts
            if traffic_routing_config is not ShapeBase.NOT_SET:
                _params['traffic_routing_config'] = traffic_routing_config
            if compute_platform is not ShapeBase.NOT_SET:
                _params['compute_platform'] = compute_platform
            _request = shapes.CreateDeploymentConfigInput(**_params)
        response = self._boto_client.create_deployment_config(
            **_request.to_boto()
        )

        return shapes.CreateDeploymentConfigOutput.from_boto(response)

    def create_deployment_group(
        self,
        _request: shapes.CreateDeploymentGroupInput = None,
        *,
        application_name: str,
        deployment_group_name: str,
        service_role_arn: str,
        deployment_config_name: str = ShapeBase.NOT_SET,
        ec2_tag_filters: typing.List[shapes.EC2TagFilter] = ShapeBase.NOT_SET,
        on_premises_instance_tag_filters: typing.List[shapes.TagFilter
                                                     ] = ShapeBase.NOT_SET,
        auto_scaling_groups: typing.List[str] = ShapeBase.NOT_SET,
        trigger_configurations: typing.List[shapes.TriggerConfig
                                           ] = ShapeBase.NOT_SET,
        alarm_configuration: shapes.AlarmConfiguration = ShapeBase.NOT_SET,
        auto_rollback_configuration: shapes.
        AutoRollbackConfiguration = ShapeBase.NOT_SET,
        deployment_style: shapes.DeploymentStyle = ShapeBase.NOT_SET,
        blue_green_deployment_configuration: shapes.
        BlueGreenDeploymentConfiguration = ShapeBase.NOT_SET,
        load_balancer_info: shapes.LoadBalancerInfo = ShapeBase.NOT_SET,
        ec2_tag_set: shapes.EC2TagSet = ShapeBase.NOT_SET,
        on_premises_tag_set: shapes.OnPremisesTagSet = ShapeBase.NOT_SET,
    ) -> shapes.CreateDeploymentGroupOutput:
        """
        Creates a deployment group to which application revisions will be deployed.
        """
        if _request is None:
            _params = {}
            if application_name is not ShapeBase.NOT_SET:
                _params['application_name'] = application_name
            if deployment_group_name is not ShapeBase.NOT_SET:
                _params['deployment_group_name'] = deployment_group_name
            if service_role_arn is not ShapeBase.NOT_SET:
                _params['service_role_arn'] = service_role_arn
            if deployment_config_name is not ShapeBase.NOT_SET:
                _params['deployment_config_name'] = deployment_config_name
            if ec2_tag_filters is not ShapeBase.NOT_SET:
                _params['ec2_tag_filters'] = ec2_tag_filters
            if on_premises_instance_tag_filters is not ShapeBase.NOT_SET:
                _params['on_premises_instance_tag_filters'
                       ] = on_premises_instance_tag_filters
            if auto_scaling_groups is not ShapeBase.NOT_SET:
                _params['auto_scaling_groups'] = auto_scaling_groups
            if trigger_configurations is not ShapeBase.NOT_SET:
                _params['trigger_configurations'] = trigger_configurations
            if alarm_configuration is not ShapeBase.NOT_SET:
                _params['alarm_configuration'] = alarm_configuration
            if auto_rollback_configuration is not ShapeBase.NOT_SET:
                _params['auto_rollback_configuration'
                       ] = auto_rollback_configuration
            if deployment_style is not ShapeBase.NOT_SET:
                _params['deployment_style'] = deployment_style
            if blue_green_deployment_configuration is not ShapeBase.NOT_SET:
                _params['blue_green_deployment_configuration'
                       ] = blue_green_deployment_configuration
            if load_balancer_info is not ShapeBase.NOT_SET:
                _params['load_balancer_info'] = load_balancer_info
            if ec2_tag_set is not ShapeBase.NOT_SET:
                _params['ec2_tag_set'] = ec2_tag_set
            if on_premises_tag_set is not ShapeBase.NOT_SET:
                _params['on_premises_tag_set'] = on_premises_tag_set
            _request = shapes.CreateDeploymentGroupInput(**_params)
        response = self._boto_client.create_deployment_group(
            **_request.to_boto()
        )

        return shapes.CreateDeploymentGroupOutput.from_boto(response)

    def delete_application(
        self,
        _request: shapes.DeleteApplicationInput = None,
        *,
        application_name: str,
    ) -> None:
        """
        Deletes an application.
        """
        if _request is None:
            _params = {}
            if application_name is not ShapeBase.NOT_SET:
                _params['application_name'] = application_name
            _request = shapes.DeleteApplicationInput(**_params)
        response = self._boto_client.delete_application(**_request.to_boto())

    def delete_deployment_config(
        self,
        _request: shapes.DeleteDeploymentConfigInput = None,
        *,
        deployment_config_name: str,
    ) -> None:
        """
        Deletes a deployment configuration.

        A deployment configuration cannot be deleted if it is currently in use.
        Predefined configurations cannot be deleted.
        """
        if _request is None:
            _params = {}
            if deployment_config_name is not ShapeBase.NOT_SET:
                _params['deployment_config_name'] = deployment_config_name
            _request = shapes.DeleteDeploymentConfigInput(**_params)
        response = self._boto_client.delete_deployment_config(
            **_request.to_boto()
        )

    def delete_deployment_group(
        self,
        _request: shapes.DeleteDeploymentGroupInput = None,
        *,
        application_name: str,
        deployment_group_name: str,
    ) -> shapes.DeleteDeploymentGroupOutput:
        """
        Deletes a deployment group.
        """
        if _request is None:
            _params = {}
            if application_name is not ShapeBase.NOT_SET:
                _params['application_name'] = application_name
            if deployment_group_name is not ShapeBase.NOT_SET:
                _params['deployment_group_name'] = deployment_group_name
            _request = shapes.DeleteDeploymentGroupInput(**_params)
        response = self._boto_client.delete_deployment_group(
            **_request.to_boto()
        )

        return shapes.DeleteDeploymentGroupOutput.from_boto(response)

    def delete_git_hub_account_token(
        self,
        _request: shapes.DeleteGitHubAccountTokenInput = None,
        *,
        token_name: str = ShapeBase.NOT_SET,
    ) -> shapes.DeleteGitHubAccountTokenOutput:
        """
        Deletes a GitHub account connection.
        """
        if _request is None:
            _params = {}
            if token_name is not ShapeBase.NOT_SET:
                _params['token_name'] = token_name
            _request = shapes.DeleteGitHubAccountTokenInput(**_params)
        response = self._boto_client.delete_git_hub_account_token(
            **_request.to_boto()
        )

        return shapes.DeleteGitHubAccountTokenOutput.from_boto(response)

    def deregister_on_premises_instance(
        self,
        _request: shapes.DeregisterOnPremisesInstanceInput = None,
        *,
        instance_name: str,
    ) -> None:
        """
        Deregisters an on-premises instance.
        """
        if _request is None:
            _params = {}
            if instance_name is not ShapeBase.NOT_SET:
                _params['instance_name'] = instance_name
            _request = shapes.DeregisterOnPremisesInstanceInput(**_params)
        response = self._boto_client.deregister_on_premises_instance(
            **_request.to_boto()
        )

    def get_application(
        self,
        _request: shapes.GetApplicationInput = None,
        *,
        application_name: str,
    ) -> shapes.GetApplicationOutput:
        """
        Gets information about an application.
        """
        if _request is None:
            _params = {}
            if application_name is not ShapeBase.NOT_SET:
                _params['application_name'] = application_name
            _request = shapes.GetApplicationInput(**_params)
        response = self._boto_client.get_application(**_request.to_boto())

        return shapes.GetApplicationOutput.from_boto(response)

    def get_application_revision(
        self,
        _request: shapes.GetApplicationRevisionInput = None,
        *,
        application_name: str,
        revision: shapes.RevisionLocation,
    ) -> shapes.GetApplicationRevisionOutput:
        """
        Gets information about an application revision.
        """
        if _request is None:
            _params = {}
            if application_name is not ShapeBase.NOT_SET:
                _params['application_name'] = application_name
            if revision is not ShapeBase.NOT_SET:
                _params['revision'] = revision
            _request = shapes.GetApplicationRevisionInput(**_params)
        response = self._boto_client.get_application_revision(
            **_request.to_boto()
        )

        return shapes.GetApplicationRevisionOutput.from_boto(response)

    def get_deployment(
        self,
        _request: shapes.GetDeploymentInput = None,
        *,
        deployment_id: str,
    ) -> shapes.GetDeploymentOutput:
        """
        Gets information about a deployment.
        """
        if _request is None:
            _params = {}
            if deployment_id is not ShapeBase.NOT_SET:
                _params['deployment_id'] = deployment_id
            _request = shapes.GetDeploymentInput(**_params)
        response = self._boto_client.get_deployment(**_request.to_boto())

        return shapes.GetDeploymentOutput.from_boto(response)

    def get_deployment_config(
        self,
        _request: shapes.GetDeploymentConfigInput = None,
        *,
        deployment_config_name: str,
    ) -> shapes.GetDeploymentConfigOutput:
        """
        Gets information about a deployment configuration.
        """
        if _request is None:
            _params = {}
            if deployment_config_name is not ShapeBase.NOT_SET:
                _params['deployment_config_name'] = deployment_config_name
            _request = shapes.GetDeploymentConfigInput(**_params)
        response = self._boto_client.get_deployment_config(**_request.to_boto())

        return shapes.GetDeploymentConfigOutput.from_boto(response)

    def get_deployment_group(
        self,
        _request: shapes.GetDeploymentGroupInput = None,
        *,
        application_name: str,
        deployment_group_name: str,
    ) -> shapes.GetDeploymentGroupOutput:
        """
        Gets information about a deployment group.
        """
        if _request is None:
            _params = {}
            if application_name is not ShapeBase.NOT_SET:
                _params['application_name'] = application_name
            if deployment_group_name is not ShapeBase.NOT_SET:
                _params['deployment_group_name'] = deployment_group_name
            _request = shapes.GetDeploymentGroupInput(**_params)
        response = self._boto_client.get_deployment_group(**_request.to_boto())

        return shapes.GetDeploymentGroupOutput.from_boto(response)

    def get_deployment_instance(
        self,
        _request: shapes.GetDeploymentInstanceInput = None,
        *,
        deployment_id: str,
        instance_id: str,
    ) -> shapes.GetDeploymentInstanceOutput:
        """
        Gets information about an instance as part of a deployment.
        """
        if _request is None:
            _params = {}
            if deployment_id is not ShapeBase.NOT_SET:
                _params['deployment_id'] = deployment_id
            if instance_id is not ShapeBase.NOT_SET:
                _params['instance_id'] = instance_id
            _request = shapes.GetDeploymentInstanceInput(**_params)
        response = self._boto_client.get_deployment_instance(
            **_request.to_boto()
        )

        return shapes.GetDeploymentInstanceOutput.from_boto(response)

    def get_on_premises_instance(
        self,
        _request: shapes.GetOnPremisesInstanceInput = None,
        *,
        instance_name: str,
    ) -> shapes.GetOnPremisesInstanceOutput:
        """
        Gets information about an on-premises instance.
        """
        if _request is None:
            _params = {}
            if instance_name is not ShapeBase.NOT_SET:
                _params['instance_name'] = instance_name
            _request = shapes.GetOnPremisesInstanceInput(**_params)
        response = self._boto_client.get_on_premises_instance(
            **_request.to_boto()
        )

        return shapes.GetOnPremisesInstanceOutput.from_boto(response)

    def list_application_revisions(
        self,
        _request: shapes.ListApplicationRevisionsInput = None,
        *,
        application_name: str,
        sort_by: typing.Union[str, shapes.
                              ApplicationRevisionSortBy] = ShapeBase.NOT_SET,
        sort_order: typing.Union[str, shapes.SortOrder] = ShapeBase.NOT_SET,
        s3_bucket: str = ShapeBase.NOT_SET,
        s3_key_prefix: str = ShapeBase.NOT_SET,
        deployed: typing.Union[str, shapes.ListStateFilterAction] = ShapeBase.
        NOT_SET,
        next_token: str = ShapeBase.NOT_SET,
    ) -> shapes.ListApplicationRevisionsOutput:
        """
        Lists information about revisions for an application.
        """
        if _request is None:
            _params = {}
            if application_name is not ShapeBase.NOT_SET:
                _params['application_name'] = application_name
            if sort_by is not ShapeBase.NOT_SET:
                _params['sort_by'] = sort_by
            if sort_order is not ShapeBase.NOT_SET:
                _params['sort_order'] = sort_order
            if s3_bucket is not ShapeBase.NOT_SET:
                _params['s3_bucket'] = s3_bucket
            if s3_key_prefix is not ShapeBase.NOT_SET:
                _params['s3_key_prefix'] = s3_key_prefix
            if deployed is not ShapeBase.NOT_SET:
                _params['deployed'] = deployed
            if next_token is not ShapeBase.NOT_SET:
                _params['next_token'] = next_token
            _request = shapes.ListApplicationRevisionsInput(**_params)
        paginator = self.get_paginator("list_application_revisions").paginate(
            **_request.to_boto()
        )
        page_generator = (page for page in paginator)
        first_page = next(page_generator)
        result = shapes.ListApplicationRevisionsOutput.from_boto(first_page)
        result._page_iterator = page_generator
        return result

        return shapes.ListApplicationRevisionsOutput.from_boto(response)

    def list_applications(
        self,
        _request: shapes.ListApplicationsInput = None,
        *,
        next_token: str = ShapeBase.NOT_SET,
    ) -> shapes.ListApplicationsOutput:
        """
        Lists the applications registered with the applicable IAM user or AWS account.
        """
        if _request is None:
            _params = {}
            if next_token is not ShapeBase.NOT_SET:
                _params['next_token'] = next_token
            _request = shapes.ListApplicationsInput(**_params)
        paginator = self.get_paginator("list_applications").paginate(
            **_request.to_boto()
        )
        page_generator = (page for page in paginator)
        first_page = next(page_generator)
        result = shapes.ListApplicationsOutput.from_boto(first_page)
        result._page_iterator = page_generator
        return result

        return shapes.ListApplicationsOutput.from_boto(response)

    def list_deployment_configs(
        self,
        _request: shapes.ListDeploymentConfigsInput = None,
        *,
        next_token: str = ShapeBase.NOT_SET,
    ) -> shapes.ListDeploymentConfigsOutput:
        """
        Lists the deployment configurations with the applicable IAM user or AWS account.
        """
        if _request is None:
            _params = {}
            if next_token is not ShapeBase.NOT_SET:
                _params['next_token'] = next_token
            _request = shapes.ListDeploymentConfigsInput(**_params)
        paginator = self.get_paginator("list_deployment_configs").paginate(
            **_request.to_boto()
        )
        page_generator = (page for page in paginator)
        first_page = next(page_generator)
        result = shapes.ListDeploymentConfigsOutput.from_boto(first_page)
        result._page_iterator = page_generator
        return result

        return shapes.ListDeploymentConfigsOutput.from_boto(response)

    def list_deployment_groups(
        self,
        _request: shapes.ListDeploymentGroupsInput = None,
        *,
        application_name: str,
        next_token: str = ShapeBase.NOT_SET,
    ) -> shapes.ListDeploymentGroupsOutput:
        """
        Lists the deployment groups for an application registered with the applicable
        IAM user or AWS account.
        """
        if _request is None:
            _params = {}
            if application_name is not ShapeBase.NOT_SET:
                _params['application_name'] = application_name
            if next_token is not ShapeBase.NOT_SET:
                _params['next_token'] = next_token
            _request = shapes.ListDeploymentGroupsInput(**_params)
        paginator = self.get_paginator("list_deployment_groups").paginate(
            **_request.to_boto()
        )
        page_generator = (page for page in paginator)
        first_page = next(page_generator)
        result = shapes.ListDeploymentGroupsOutput.from_boto(first_page)
        result._page_iterator = page_generator
        return result

        return shapes.ListDeploymentGroupsOutput.from_boto(response)

    def list_deployment_instances(
        self,
        _request: shapes.ListDeploymentInstancesInput = None,
        *,
        deployment_id: str,
        next_token: str = ShapeBase.NOT_SET,
        instance_status_filter: typing.List[
            typing.Union[str, shapes.InstanceStatus]] = ShapeBase.NOT_SET,
        instance_type_filter: typing.List[typing.Union[str, shapes.InstanceType]
                                         ] = ShapeBase.NOT_SET,
    ) -> shapes.ListDeploymentInstancesOutput:
        """
        Lists the instance for a deployment associated with the applicable IAM user or
        AWS account.
        """
        if _request is None:
            _params = {}
            if deployment_id is not ShapeBase.NOT_SET:
                _params['deployment_id'] = deployment_id
            if next_token is not ShapeBase.NOT_SET:
                _params['next_token'] = next_token
            if instance_status_filter is not ShapeBase.NOT_SET:
                _params['instance_status_filter'] = instance_status_filter
            if instance_type_filter is not ShapeBase.NOT_SET:
                _params['instance_type_filter'] = instance_type_filter
            _request = shapes.ListDeploymentInstancesInput(**_params)
        paginator = self.get_paginator("list_deployment_instances").paginate(
            **_request.to_boto()
        )
        page_generator = (page for page in paginator)
        first_page = next(page_generator)
        result = shapes.ListDeploymentInstancesOutput.from_boto(first_page)
        result._page_iterator = page_generator
        return result

        return shapes.ListDeploymentInstancesOutput.from_boto(response)

    def list_deployments(
        self,
        _request: shapes.ListDeploymentsInput = None,
        *,
        application_name: str = ShapeBase.NOT_SET,
        deployment_group_name: str = ShapeBase.NOT_SET,
        include_only_statuses: typing.List[
            typing.Union[str, shapes.DeploymentStatus]] = ShapeBase.NOT_SET,
        create_time_range: shapes.TimeRange = ShapeBase.NOT_SET,
        next_token: str = ShapeBase.NOT_SET,
    ) -> shapes.ListDeploymentsOutput:
        """
        Lists the deployments in a deployment group for an application registered with
        the applicable IAM user or AWS account.
        """
        if _request is None:
            _params = {}
            if application_name is not ShapeBase.NOT_SET:
                _params['application_name'] = application_name
            if deployment_group_name is not ShapeBase.NOT_SET:
                _params['deployment_group_name'] = deployment_group_name
            if include_only_statuses is not ShapeBase.NOT_SET:
                _params['include_only_statuses'] = include_only_statuses
            if create_time_range is not ShapeBase.NOT_SET:
                _params['create_time_range'] = create_time_range
            if next_token is not ShapeBase.NOT_SET:
                _params['next_token'] = next_token
            _request = shapes.ListDeploymentsInput(**_params)
        paginator = self.get_paginator("list_deployments").paginate(
            **_request.to_boto()
        )
        page_generator = (page for page in paginator)
        first_page = next(page_generator)
        result = shapes.ListDeploymentsOutput.from_boto(first_page)
        result._page_iterator = page_generator
        return result

        return shapes.ListDeploymentsOutput.from_boto(response)

    def list_git_hub_account_token_names(
        self,
        _request: shapes.ListGitHubAccountTokenNamesInput = None,
        *,
        next_token: str = ShapeBase.NOT_SET,
    ) -> shapes.ListGitHubAccountTokenNamesOutput:
        """
        Lists the names of stored connections to GitHub accounts.
        """
        if _request is None:
            _params = {}
            if next_token is not ShapeBase.NOT_SET:
                _params['next_token'] = next_token
            _request = shapes.ListGitHubAccountTokenNamesInput(**_params)
        response = self._boto_client.list_git_hub_account_token_names(
            **_request.to_boto()
        )

        return shapes.ListGitHubAccountTokenNamesOutput.from_boto(response)

    def list_on_premises_instances(
        self,
        _request: shapes.ListOnPremisesInstancesInput = None,
        *,
        registration_status: typing.
        Union[str, shapes.RegistrationStatus] = ShapeBase.NOT_SET,
        tag_filters: typing.List[shapes.TagFilter] = ShapeBase.NOT_SET,
        next_token: str = ShapeBase.NOT_SET,
    ) -> shapes.ListOnPremisesInstancesOutput:
        """
        Gets a list of names for one or more on-premises instances.

        Unless otherwise specified, both registered and deregistered on-premises
        instance names will be listed. To list only registered or deregistered on-
        premises instance names, use the registration status parameter.
        """
        if _request is None:
            _params = {}
            if registration_status is not ShapeBase.NOT_SET:
                _params['registration_status'] = registration_status
            if tag_filters is not ShapeBase.NOT_SET:
                _params['tag_filters'] = tag_filters
            if next_token is not ShapeBase.NOT_SET:
                _params['next_token'] = next_token
            _request = shapes.ListOnPremisesInstancesInput(**_params)
        response = self._boto_client.list_on_premises_instances(
            **_request.to_boto()
        )

        return shapes.ListOnPremisesInstancesOutput.from_boto(response)

    def put_lifecycle_event_hook_execution_status(
        self,
        _request: shapes.PutLifecycleEventHookExecutionStatusInput = None,
        *,
        deployment_id: str = ShapeBase.NOT_SET,
        lifecycle_event_hook_execution_id: str = ShapeBase.NOT_SET,
        status: typing.Union[str, shapes.LifecycleEventStatus] = ShapeBase.
        NOT_SET,
    ) -> shapes.PutLifecycleEventHookExecutionStatusOutput:
        """
        Sets the result of a Lambda validation function. The function validates one or
        both lifecycle events (`BeforeAllowTraffic` and `AfterAllowTraffic`) and returns
        `Succeeded` or `Failed`.
        """
        if _request is None:
            _params = {}
            if deployment_id is not ShapeBase.NOT_SET:
                _params['deployment_id'] = deployment_id
            if lifecycle_event_hook_execution_id is not ShapeBase.NOT_SET:
                _params['lifecycle_event_hook_execution_id'
                       ] = lifecycle_event_hook_execution_id
            if status is not ShapeBase.NOT_SET:
                _params['status'] = status
            _request = shapes.PutLifecycleEventHookExecutionStatusInput(
                **_params
            )
        response = self._boto_client.put_lifecycle_event_hook_execution_status(
            **_request.to_boto()
        )

        return shapes.PutLifecycleEventHookExecutionStatusOutput.from_boto(
            response
        )

    def register_application_revision(
        self,
        _request: shapes.RegisterApplicationRevisionInput = None,
        *,
        application_name: str,
        revision: shapes.RevisionLocation,
        description: str = ShapeBase.NOT_SET,
    ) -> None:
        """
        Registers with AWS CodeDeploy a revision for the specified application.
        """
        if _request is None:
            _params = {}
            if application_name is not ShapeBase.NOT_SET:
                _params['application_name'] = application_name
            if revision is not ShapeBase.NOT_SET:
                _params['revision'] = revision
            if description is not ShapeBase.NOT_SET:
                _params['description'] = description
            _request = shapes.RegisterApplicationRevisionInput(**_params)
        response = self._boto_client.register_application_revision(
            **_request.to_boto()
        )

    def register_on_premises_instance(
        self,
        _request: shapes.RegisterOnPremisesInstanceInput = None,
        *,
        instance_name: str,
        iam_session_arn: str = ShapeBase.NOT_SET,
        iam_user_arn: str = ShapeBase.NOT_SET,
    ) -> None:
        """
        Registers an on-premises instance.

        Only one IAM ARN (an IAM session ARN or IAM user ARN) is supported in the
        request. You cannot use both.
        """
        if _request is None:
            _params = {}
            if instance_name is not ShapeBase.NOT_SET:
                _params['instance_name'] = instance_name
            if iam_session_arn is not ShapeBase.NOT_SET:
                _params['iam_session_arn'] = iam_session_arn
            if iam_user_arn is not ShapeBase.NOT_SET:
                _params['iam_user_arn'] = iam_user_arn
            _request = shapes.RegisterOnPremisesInstanceInput(**_params)
        response = self._boto_client.register_on_premises_instance(
            **_request.to_boto()
        )

    def remove_tags_from_on_premises_instances(
        self,
        _request: shapes.RemoveTagsFromOnPremisesInstancesInput = None,
        *,
        tags: typing.List[shapes.Tag],
        instance_names: typing.List[str],
    ) -> None:
        """
        Removes one or more tags from one or more on-premises instances.
        """
        if _request is None:
            _params = {}
            if tags is not ShapeBase.NOT_SET:
                _params['tags'] = tags
            if instance_names is not ShapeBase.NOT_SET:
                _params['instance_names'] = instance_names
            _request = shapes.RemoveTagsFromOnPremisesInstancesInput(**_params)
        response = self._boto_client.remove_tags_from_on_premises_instances(
            **_request.to_boto()
        )

    def skip_wait_time_for_instance_termination(
        self,
        _request: shapes.SkipWaitTimeForInstanceTerminationInput = None,
        *,
        deployment_id: str = ShapeBase.NOT_SET,
    ) -> None:
        """
        In a blue/green deployment, overrides any specified wait time and starts
        terminating instances immediately after the traffic routing is completed.
        """
        if _request is None:
            _params = {}
            if deployment_id is not ShapeBase.NOT_SET:
                _params['deployment_id'] = deployment_id
            _request = shapes.SkipWaitTimeForInstanceTerminationInput(**_params)
        response = self._boto_client.skip_wait_time_for_instance_termination(
            **_request.to_boto()
        )

    def stop_deployment(
        self,
        _request: shapes.StopDeploymentInput = None,
        *,
        deployment_id: str,
        auto_rollback_enabled: bool = ShapeBase.NOT_SET,
    ) -> shapes.StopDeploymentOutput:
        """
        Attempts to stop an ongoing deployment.
        """
        if _request is None:
            _params = {}
            if deployment_id is not ShapeBase.NOT_SET:
                _params['deployment_id'] = deployment_id
            if auto_rollback_enabled is not ShapeBase.NOT_SET:
                _params['auto_rollback_enabled'] = auto_rollback_enabled
            _request = shapes.StopDeploymentInput(**_params)
        response = self._boto_client.stop_deployment(**_request.to_boto())

        return shapes.StopDeploymentOutput.from_boto(response)

    def update_application(
        self,
        _request: shapes.UpdateApplicationInput = None,
        *,
        application_name: str = ShapeBase.NOT_SET,
        new_application_name: str = ShapeBase.NOT_SET,
    ) -> None:
        """
        Changes the name of an application.
        """
        if _request is None:
            _params = {}
            if application_name is not ShapeBase.NOT_SET:
                _params['application_name'] = application_name
            if new_application_name is not ShapeBase.NOT_SET:
                _params['new_application_name'] = new_application_name
            _request = shapes.UpdateApplicationInput(**_params)
        response = self._boto_client.update_application(**_request.to_boto())

    def update_deployment_group(
        self,
        _request: shapes.UpdateDeploymentGroupInput = None,
        *,
        application_name: str,
        current_deployment_group_name: str,
        new_deployment_group_name: str = ShapeBase.NOT_SET,
        deployment_config_name: str = ShapeBase.NOT_SET,
        ec2_tag_filters: typing.List[shapes.EC2TagFilter] = ShapeBase.NOT_SET,
        on_premises_instance_tag_filters: typing.List[shapes.TagFilter
                                                     ] = ShapeBase.NOT_SET,
        auto_scaling_groups: typing.List[str] = ShapeBase.NOT_SET,
        service_role_arn: str = ShapeBase.NOT_SET,
        trigger_configurations: typing.List[shapes.TriggerConfig
                                           ] = ShapeBase.NOT_SET,
        alarm_configuration: shapes.AlarmConfiguration = ShapeBase.NOT_SET,
        auto_rollback_configuration: shapes.
        AutoRollbackConfiguration = ShapeBase.NOT_SET,
        deployment_style: shapes.DeploymentStyle = ShapeBase.NOT_SET,
        blue_green_deployment_configuration: shapes.
        BlueGreenDeploymentConfiguration = ShapeBase.NOT_SET,
        load_balancer_info: shapes.LoadBalancerInfo = ShapeBase.NOT_SET,
        ec2_tag_set: shapes.EC2TagSet = ShapeBase.NOT_SET,
        on_premises_tag_set: shapes.OnPremisesTagSet = ShapeBase.NOT_SET,
    ) -> shapes.UpdateDeploymentGroupOutput:
        """
        Changes information about a deployment group.
        """
        if _request is None:
            _params = {}
            if application_name is not ShapeBase.NOT_SET:
                _params['application_name'] = application_name
            if current_deployment_group_name is not ShapeBase.NOT_SET:
                _params['current_deployment_group_name'
                       ] = current_deployment_group_name
            if new_deployment_group_name is not ShapeBase.NOT_SET:
                _params['new_deployment_group_name'] = new_deployment_group_name
            if deployment_config_name is not ShapeBase.NOT_SET:
                _params['deployment_config_name'] = deployment_config_name
            if ec2_tag_filters is not ShapeBase.NOT_SET:
                _params['ec2_tag_filters'] = ec2_tag_filters
            if on_premises_instance_tag_filters is not ShapeBase.NOT_SET:
                _params['on_premises_instance_tag_filters'
                       ] = on_premises_instance_tag_filters
            if auto_scaling_groups is not ShapeBase.NOT_SET:
                _params['auto_scaling_groups'] = auto_scaling_groups
            if service_role_arn is not ShapeBase.NOT_SET:
                _params['service_role_arn'] = service_role_arn
            if trigger_configurations is not ShapeBase.NOT_SET:
                _params['trigger_configurations'] = trigger_configurations
            if alarm_configuration is not ShapeBase.NOT_SET:
                _params['alarm_configuration'] = alarm_configuration
            if auto_rollback_configuration is not ShapeBase.NOT_SET:
                _params['auto_rollback_configuration'
                       ] = auto_rollback_configuration
            if deployment_style is not ShapeBase.NOT_SET:
                _params['deployment_style'] = deployment_style
            if blue_green_deployment_configuration is not ShapeBase.NOT_SET:
                _params['blue_green_deployment_configuration'
                       ] = blue_green_deployment_configuration
            if load_balancer_info is not ShapeBase.NOT_SET:
                _params['load_balancer_info'] = load_balancer_info
            if ec2_tag_set is not ShapeBase.NOT_SET:
                _params['ec2_tag_set'] = ec2_tag_set
            if on_premises_tag_set is not ShapeBase.NOT_SET:
                _params['on_premises_tag_set'] = on_premises_tag_set
            _request = shapes.UpdateDeploymentGroupInput(**_params)
        response = self._boto_client.update_deployment_group(
            **_request.to_boto()
        )

        return shapes.UpdateDeploymentGroupOutput.from_boto(response)
