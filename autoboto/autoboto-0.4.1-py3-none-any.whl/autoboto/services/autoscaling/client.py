import datetime
import typing
import boto3
from autoboto import ClientBase, ShapeBase, OutputShapeBase
from . import shapes


class Client(ClientBase):
    def __init__(self, *args, **kwargs):
        super().__init__("autoscaling", *args, **kwargs)

    def attach_instances(
        self,
        _request: shapes.AttachInstancesQuery = None,
        *,
        auto_scaling_group_name: str,
        instance_ids: typing.List[str] = ShapeBase.NOT_SET,
    ) -> None:
        """
        Attaches one or more EC2 instances to the specified Auto Scaling group.

        When you attach instances, Amazon EC2 Auto Scaling increases the desired
        capacity of the group by the number of instances being attached. If the number
        of instances being attached plus the desired capacity of the group exceeds the
        maximum size of the group, the operation fails.

        If there is a Classic Load Balancer attached to your Auto Scaling group, the
        instances are also registered with the load balancer. If there are target groups
        attached to your Auto Scaling group, the instances are also registered with the
        target groups.

        For more information, see [Attach EC2 Instances to Your Auto Scaling
        Group](http://docs.aws.amazon.com/autoscaling/ec2/userguide/attach-instance-
        asg.html) in the _Amazon EC2 Auto Scaling User Guide_.
        """
        if _request is None:
            _params = {}
            if auto_scaling_group_name is not ShapeBase.NOT_SET:
                _params['auto_scaling_group_name'] = auto_scaling_group_name
            if instance_ids is not ShapeBase.NOT_SET:
                _params['instance_ids'] = instance_ids
            _request = shapes.AttachInstancesQuery(**_params)
        response = self._boto_client.attach_instances(**_request.to_boto())

    def attach_load_balancer_target_groups(
        self,
        _request: shapes.AttachLoadBalancerTargetGroupsType = None,
        *,
        auto_scaling_group_name: str,
        target_group_arns: typing.List[str],
    ) -> shapes.AttachLoadBalancerTargetGroupsResultType:
        """
        Attaches one or more target groups to the specified Auto Scaling group.

        To describe the target groups for an Auto Scaling group, use
        DescribeLoadBalancerTargetGroups. To detach the target group from the Auto
        Scaling group, use DetachLoadBalancerTargetGroups.

        For more information, see [Attach a Load Balancer to Your Auto Scaling
        Group](http://docs.aws.amazon.com/autoscaling/ec2/userguide/attach-load-
        balancer-asg.html) in the _Amazon EC2 Auto Scaling User Guide_.
        """
        if _request is None:
            _params = {}
            if auto_scaling_group_name is not ShapeBase.NOT_SET:
                _params['auto_scaling_group_name'] = auto_scaling_group_name
            if target_group_arns is not ShapeBase.NOT_SET:
                _params['target_group_arns'] = target_group_arns
            _request = shapes.AttachLoadBalancerTargetGroupsType(**_params)
        response = self._boto_client.attach_load_balancer_target_groups(
            **_request.to_boto()
        )

        return shapes.AttachLoadBalancerTargetGroupsResultType.from_boto(
            response
        )

    def attach_load_balancers(
        self,
        _request: shapes.AttachLoadBalancersType = None,
        *,
        auto_scaling_group_name: str,
        load_balancer_names: typing.List[str],
    ) -> shapes.AttachLoadBalancersResultType:
        """
        Attaches one or more Classic Load Balancers to the specified Auto Scaling group.

        To attach an Application Load Balancer instead, see
        AttachLoadBalancerTargetGroups.

        To describe the load balancers for an Auto Scaling group, use
        DescribeLoadBalancers. To detach the load balancer from the Auto Scaling group,
        use DetachLoadBalancers.

        For more information, see [Attach a Load Balancer to Your Auto Scaling
        Group](http://docs.aws.amazon.com/autoscaling/ec2/userguide/attach-load-
        balancer-asg.html) in the _Amazon EC2 Auto Scaling User Guide_.
        """
        if _request is None:
            _params = {}
            if auto_scaling_group_name is not ShapeBase.NOT_SET:
                _params['auto_scaling_group_name'] = auto_scaling_group_name
            if load_balancer_names is not ShapeBase.NOT_SET:
                _params['load_balancer_names'] = load_balancer_names
            _request = shapes.AttachLoadBalancersType(**_params)
        response = self._boto_client.attach_load_balancers(**_request.to_boto())

        return shapes.AttachLoadBalancersResultType.from_boto(response)

    def batch_delete_scheduled_action(
        self,
        _request: shapes.BatchDeleteScheduledActionType = None,
        *,
        auto_scaling_group_name: str,
        scheduled_action_names: typing.List[str],
    ) -> shapes.BatchDeleteScheduledActionAnswer:
        """
        Deletes one or more scheduled actions for the specified Auto Scaling group.
        """
        if _request is None:
            _params = {}
            if auto_scaling_group_name is not ShapeBase.NOT_SET:
                _params['auto_scaling_group_name'] = auto_scaling_group_name
            if scheduled_action_names is not ShapeBase.NOT_SET:
                _params['scheduled_action_names'] = scheduled_action_names
            _request = shapes.BatchDeleteScheduledActionType(**_params)
        response = self._boto_client.batch_delete_scheduled_action(
            **_request.to_boto()
        )

        return shapes.BatchDeleteScheduledActionAnswer.from_boto(response)

    def batch_put_scheduled_update_group_action(
        self,
        _request: shapes.BatchPutScheduledUpdateGroupActionType = None,
        *,
        auto_scaling_group_name: str,
        scheduled_update_group_actions: typing.List[
            shapes.ScheduledUpdateGroupActionRequest],
    ) -> shapes.BatchPutScheduledUpdateGroupActionAnswer:
        """
        Creates or updates one or more scheduled scaling actions for an Auto Scaling
        group. When updating a scheduled scaling action, if you leave a parameter
        unspecified, the corresponding value remains unchanged.
        """
        if _request is None:
            _params = {}
            if auto_scaling_group_name is not ShapeBase.NOT_SET:
                _params['auto_scaling_group_name'] = auto_scaling_group_name
            if scheduled_update_group_actions is not ShapeBase.NOT_SET:
                _params['scheduled_update_group_actions'
                       ] = scheduled_update_group_actions
            _request = shapes.BatchPutScheduledUpdateGroupActionType(**_params)
        response = self._boto_client.batch_put_scheduled_update_group_action(
            **_request.to_boto()
        )

        return shapes.BatchPutScheduledUpdateGroupActionAnswer.from_boto(
            response
        )

    def complete_lifecycle_action(
        self,
        _request: shapes.CompleteLifecycleActionType = None,
        *,
        lifecycle_hook_name: str,
        auto_scaling_group_name: str,
        lifecycle_action_result: str,
        lifecycle_action_token: str = ShapeBase.NOT_SET,
        instance_id: str = ShapeBase.NOT_SET,
    ) -> shapes.CompleteLifecycleActionAnswer:
        """
        Completes the lifecycle action for the specified token or instance with the
        specified result.

        This step is a part of the procedure for adding a lifecycle hook to an Auto
        Scaling group:

          1. (Optional) Create a Lambda function and a rule that allows CloudWatch Events to invoke your Lambda function when Amazon EC2 Auto Scaling launches or terminates instances.

          2. (Optional) Create a notification target and an IAM role. The target can be either an Amazon SQS queue or an Amazon SNS topic. The role allows Amazon EC2 Auto Scaling to publish lifecycle notifications to the target.

          3. Create the lifecycle hook. Specify whether the hook is used when the instances launch or terminate.

          4. If you need more time, record the lifecycle action heartbeat to keep the instance in a pending state.

          5. **If you finish before the timeout period ends, complete the lifecycle action.**

        For more information, see [Auto Scaling
        Lifecycle](http://docs.aws.amazon.com/autoscaling/ec2/userguide/AutoScalingGroupLifecycle.html)
        in the _Amazon EC2 Auto Scaling User Guide_.
        """
        if _request is None:
            _params = {}
            if lifecycle_hook_name is not ShapeBase.NOT_SET:
                _params['lifecycle_hook_name'] = lifecycle_hook_name
            if auto_scaling_group_name is not ShapeBase.NOT_SET:
                _params['auto_scaling_group_name'] = auto_scaling_group_name
            if lifecycle_action_result is not ShapeBase.NOT_SET:
                _params['lifecycle_action_result'] = lifecycle_action_result
            if lifecycle_action_token is not ShapeBase.NOT_SET:
                _params['lifecycle_action_token'] = lifecycle_action_token
            if instance_id is not ShapeBase.NOT_SET:
                _params['instance_id'] = instance_id
            _request = shapes.CompleteLifecycleActionType(**_params)
        response = self._boto_client.complete_lifecycle_action(
            **_request.to_boto()
        )

        return shapes.CompleteLifecycleActionAnswer.from_boto(response)

    def create_auto_scaling_group(
        self,
        _request: shapes.CreateAutoScalingGroupType = None,
        *,
        auto_scaling_group_name: str,
        min_size: int,
        max_size: int,
        launch_configuration_name: str = ShapeBase.NOT_SET,
        launch_template: shapes.LaunchTemplateSpecification = ShapeBase.NOT_SET,
        instance_id: str = ShapeBase.NOT_SET,
        desired_capacity: int = ShapeBase.NOT_SET,
        default_cooldown: int = ShapeBase.NOT_SET,
        availability_zones: typing.List[str] = ShapeBase.NOT_SET,
        load_balancer_names: typing.List[str] = ShapeBase.NOT_SET,
        target_group_arns: typing.List[str] = ShapeBase.NOT_SET,
        health_check_type: str = ShapeBase.NOT_SET,
        health_check_grace_period: int = ShapeBase.NOT_SET,
        placement_group: str = ShapeBase.NOT_SET,
        vpc_zone_identifier: str = ShapeBase.NOT_SET,
        termination_policies: typing.List[str] = ShapeBase.NOT_SET,
        new_instances_protected_from_scale_in: bool = ShapeBase.NOT_SET,
        lifecycle_hook_specification_list: typing.List[
            shapes.LifecycleHookSpecification] = ShapeBase.NOT_SET,
        tags: typing.List[shapes.Tag] = ShapeBase.NOT_SET,
        service_linked_role_arn: str = ShapeBase.NOT_SET,
    ) -> None:
        """
        Creates an Auto Scaling group with the specified name and attributes.

        If you exceed your maximum limit of Auto Scaling groups, the call fails. For
        information about viewing this limit, see DescribeAccountLimits. For information
        about updating this limit, see [Auto Scaling
        Limits](http://docs.aws.amazon.com/autoscaling/ec2/userguide/as-account-
        limits.html) in the _Amazon EC2 Auto Scaling User Guide_.

        For more information, see [Auto Scaling
        Groups](http://docs.aws.amazon.com/autoscaling/ec2/userguide/AutoScalingGroup.html)
        in the _Amazon EC2 Auto Scaling User Guide_.
        """
        if _request is None:
            _params = {}
            if auto_scaling_group_name is not ShapeBase.NOT_SET:
                _params['auto_scaling_group_name'] = auto_scaling_group_name
            if min_size is not ShapeBase.NOT_SET:
                _params['min_size'] = min_size
            if max_size is not ShapeBase.NOT_SET:
                _params['max_size'] = max_size
            if launch_configuration_name is not ShapeBase.NOT_SET:
                _params['launch_configuration_name'] = launch_configuration_name
            if launch_template is not ShapeBase.NOT_SET:
                _params['launch_template'] = launch_template
            if instance_id is not ShapeBase.NOT_SET:
                _params['instance_id'] = instance_id
            if desired_capacity is not ShapeBase.NOT_SET:
                _params['desired_capacity'] = desired_capacity
            if default_cooldown is not ShapeBase.NOT_SET:
                _params['default_cooldown'] = default_cooldown
            if availability_zones is not ShapeBase.NOT_SET:
                _params['availability_zones'] = availability_zones
            if load_balancer_names is not ShapeBase.NOT_SET:
                _params['load_balancer_names'] = load_balancer_names
            if target_group_arns is not ShapeBase.NOT_SET:
                _params['target_group_arns'] = target_group_arns
            if health_check_type is not ShapeBase.NOT_SET:
                _params['health_check_type'] = health_check_type
            if health_check_grace_period is not ShapeBase.NOT_SET:
                _params['health_check_grace_period'] = health_check_grace_period
            if placement_group is not ShapeBase.NOT_SET:
                _params['placement_group'] = placement_group
            if vpc_zone_identifier is not ShapeBase.NOT_SET:
                _params['vpc_zone_identifier'] = vpc_zone_identifier
            if termination_policies is not ShapeBase.NOT_SET:
                _params['termination_policies'] = termination_policies
            if new_instances_protected_from_scale_in is not ShapeBase.NOT_SET:
                _params['new_instances_protected_from_scale_in'
                       ] = new_instances_protected_from_scale_in
            if lifecycle_hook_specification_list is not ShapeBase.NOT_SET:
                _params['lifecycle_hook_specification_list'
                       ] = lifecycle_hook_specification_list
            if tags is not ShapeBase.NOT_SET:
                _params['tags'] = tags
            if service_linked_role_arn is not ShapeBase.NOT_SET:
                _params['service_linked_role_arn'] = service_linked_role_arn
            _request = shapes.CreateAutoScalingGroupType(**_params)
        response = self._boto_client.create_auto_scaling_group(
            **_request.to_boto()
        )

    def create_launch_configuration(
        self,
        _request: shapes.CreateLaunchConfigurationType = None,
        *,
        launch_configuration_name: str,
        image_id: str = ShapeBase.NOT_SET,
        key_name: str = ShapeBase.NOT_SET,
        security_groups: typing.List[str] = ShapeBase.NOT_SET,
        classic_link_vpc_id: str = ShapeBase.NOT_SET,
        classic_link_vpc_security_groups: typing.List[str] = ShapeBase.NOT_SET,
        user_data: str = ShapeBase.NOT_SET,
        instance_id: str = ShapeBase.NOT_SET,
        instance_type: str = ShapeBase.NOT_SET,
        kernel_id: str = ShapeBase.NOT_SET,
        ramdisk_id: str = ShapeBase.NOT_SET,
        block_device_mappings: typing.List[shapes.BlockDeviceMapping
                                          ] = ShapeBase.NOT_SET,
        instance_monitoring: shapes.InstanceMonitoring = ShapeBase.NOT_SET,
        spot_price: str = ShapeBase.NOT_SET,
        iam_instance_profile: str = ShapeBase.NOT_SET,
        ebs_optimized: bool = ShapeBase.NOT_SET,
        associate_public_ip_address: bool = ShapeBase.NOT_SET,
        placement_tenancy: str = ShapeBase.NOT_SET,
    ) -> None:
        """
        Creates a launch configuration.

        If you exceed your maximum limit of launch configurations, the call fails. For
        information about viewing this limit, see DescribeAccountLimits. For information
        about updating this limit, see [Auto Scaling
        Limits](http://docs.aws.amazon.com/autoscaling/ec2/userguide/as-account-
        limits.html) in the _Amazon EC2 Auto Scaling User Guide_.

        For more information, see [Launch
        Configurations](http://docs.aws.amazon.com/autoscaling/ec2/userguide/LaunchConfiguration.html)
        in the _Amazon EC2 Auto Scaling User Guide_.
        """
        if _request is None:
            _params = {}
            if launch_configuration_name is not ShapeBase.NOT_SET:
                _params['launch_configuration_name'] = launch_configuration_name
            if image_id is not ShapeBase.NOT_SET:
                _params['image_id'] = image_id
            if key_name is not ShapeBase.NOT_SET:
                _params['key_name'] = key_name
            if security_groups is not ShapeBase.NOT_SET:
                _params['security_groups'] = security_groups
            if classic_link_vpc_id is not ShapeBase.NOT_SET:
                _params['classic_link_vpc_id'] = classic_link_vpc_id
            if classic_link_vpc_security_groups is not ShapeBase.NOT_SET:
                _params['classic_link_vpc_security_groups'
                       ] = classic_link_vpc_security_groups
            if user_data is not ShapeBase.NOT_SET:
                _params['user_data'] = user_data
            if instance_id is not ShapeBase.NOT_SET:
                _params['instance_id'] = instance_id
            if instance_type is not ShapeBase.NOT_SET:
                _params['instance_type'] = instance_type
            if kernel_id is not ShapeBase.NOT_SET:
                _params['kernel_id'] = kernel_id
            if ramdisk_id is not ShapeBase.NOT_SET:
                _params['ramdisk_id'] = ramdisk_id
            if block_device_mappings is not ShapeBase.NOT_SET:
                _params['block_device_mappings'] = block_device_mappings
            if instance_monitoring is not ShapeBase.NOT_SET:
                _params['instance_monitoring'] = instance_monitoring
            if spot_price is not ShapeBase.NOT_SET:
                _params['spot_price'] = spot_price
            if iam_instance_profile is not ShapeBase.NOT_SET:
                _params['iam_instance_profile'] = iam_instance_profile
            if ebs_optimized is not ShapeBase.NOT_SET:
                _params['ebs_optimized'] = ebs_optimized
            if associate_public_ip_address is not ShapeBase.NOT_SET:
                _params['associate_public_ip_address'
                       ] = associate_public_ip_address
            if placement_tenancy is not ShapeBase.NOT_SET:
                _params['placement_tenancy'] = placement_tenancy
            _request = shapes.CreateLaunchConfigurationType(**_params)
        response = self._boto_client.create_launch_configuration(
            **_request.to_boto()
        )

    def create_or_update_tags(
        self,
        _request: shapes.CreateOrUpdateTagsType = None,
        *,
        tags: typing.List[shapes.Tag],
    ) -> None:
        """
        Creates or updates tags for the specified Auto Scaling group.

        When you specify a tag with a key that already exists, the operation overwrites
        the previous tag definition, and you do not get an error message.

        For more information, see [Tagging Auto Scaling Groups and
        Instances](http://docs.aws.amazon.com/autoscaling/ec2/userguide/autoscaling-
        tagging.html) in the _Amazon EC2 Auto Scaling User Guide_.
        """
        if _request is None:
            _params = {}
            if tags is not ShapeBase.NOT_SET:
                _params['tags'] = tags
            _request = shapes.CreateOrUpdateTagsType(**_params)
        response = self._boto_client.create_or_update_tags(**_request.to_boto())

    def delete_auto_scaling_group(
        self,
        _request: shapes.DeleteAutoScalingGroupType = None,
        *,
        auto_scaling_group_name: str,
        force_delete: bool = ShapeBase.NOT_SET,
    ) -> None:
        """
        Deletes the specified Auto Scaling group.

        If the group has instances or scaling activities in progress, you must specify
        the option to force the deletion in order for it to succeed.

        If the group has policies, deleting the group deletes the policies, the
        underlying alarm actions, and any alarm that no longer has an associated action.

        To remove instances from the Auto Scaling group before deleting it, call
        DetachInstances with the list of instances and the option to decrement the
        desired capacity so that Amazon EC2 Auto Scaling does not launch replacement
        instances.

        To terminate all instances before deleting the Auto Scaling group, call
        UpdateAutoScalingGroup and set the minimum size and desired capacity of the Auto
        Scaling group to zero.
        """
        if _request is None:
            _params = {}
            if auto_scaling_group_name is not ShapeBase.NOT_SET:
                _params['auto_scaling_group_name'] = auto_scaling_group_name
            if force_delete is not ShapeBase.NOT_SET:
                _params['force_delete'] = force_delete
            _request = shapes.DeleteAutoScalingGroupType(**_params)
        response = self._boto_client.delete_auto_scaling_group(
            **_request.to_boto()
        )

    def delete_launch_configuration(
        self,
        _request: shapes.LaunchConfigurationNameType = None,
        *,
        launch_configuration_name: str,
    ) -> None:
        """
        Deletes the specified launch configuration.

        The launch configuration must not be attached to an Auto Scaling group. When
        this call completes, the launch configuration is no longer available for use.
        """
        if _request is None:
            _params = {}
            if launch_configuration_name is not ShapeBase.NOT_SET:
                _params['launch_configuration_name'] = launch_configuration_name
            _request = shapes.LaunchConfigurationNameType(**_params)
        response = self._boto_client.delete_launch_configuration(
            **_request.to_boto()
        )

    def delete_lifecycle_hook(
        self,
        _request: shapes.DeleteLifecycleHookType = None,
        *,
        lifecycle_hook_name: str,
        auto_scaling_group_name: str,
    ) -> shapes.DeleteLifecycleHookAnswer:
        """
        Deletes the specified lifecycle hook.

        If there are any outstanding lifecycle actions, they are completed first
        (`ABANDON` for launching instances, `CONTINUE` for terminating instances).
        """
        if _request is None:
            _params = {}
            if lifecycle_hook_name is not ShapeBase.NOT_SET:
                _params['lifecycle_hook_name'] = lifecycle_hook_name
            if auto_scaling_group_name is not ShapeBase.NOT_SET:
                _params['auto_scaling_group_name'] = auto_scaling_group_name
            _request = shapes.DeleteLifecycleHookType(**_params)
        response = self._boto_client.delete_lifecycle_hook(**_request.to_boto())

        return shapes.DeleteLifecycleHookAnswer.from_boto(response)

    def delete_notification_configuration(
        self,
        _request: shapes.DeleteNotificationConfigurationType = None,
        *,
        auto_scaling_group_name: str,
        topic_arn: str,
    ) -> None:
        """
        Deletes the specified notification.
        """
        if _request is None:
            _params = {}
            if auto_scaling_group_name is not ShapeBase.NOT_SET:
                _params['auto_scaling_group_name'] = auto_scaling_group_name
            if topic_arn is not ShapeBase.NOT_SET:
                _params['topic_arn'] = topic_arn
            _request = shapes.DeleteNotificationConfigurationType(**_params)
        response = self._boto_client.delete_notification_configuration(
            **_request.to_boto()
        )

    def delete_policy(
        self,
        _request: shapes.DeletePolicyType = None,
        *,
        policy_name: str,
        auto_scaling_group_name: str = ShapeBase.NOT_SET,
    ) -> None:
        """
        Deletes the specified Auto Scaling policy.

        Deleting a policy deletes the underlying alarm action, but does not delete the
        alarm, even if it no longer has an associated action.
        """
        if _request is None:
            _params = {}
            if policy_name is not ShapeBase.NOT_SET:
                _params['policy_name'] = policy_name
            if auto_scaling_group_name is not ShapeBase.NOT_SET:
                _params['auto_scaling_group_name'] = auto_scaling_group_name
            _request = shapes.DeletePolicyType(**_params)
        response = self._boto_client.delete_policy(**_request.to_boto())

    def delete_scheduled_action(
        self,
        _request: shapes.DeleteScheduledActionType = None,
        *,
        auto_scaling_group_name: str,
        scheduled_action_name: str,
    ) -> None:
        """
        Deletes the specified scheduled action.
        """
        if _request is None:
            _params = {}
            if auto_scaling_group_name is not ShapeBase.NOT_SET:
                _params['auto_scaling_group_name'] = auto_scaling_group_name
            if scheduled_action_name is not ShapeBase.NOT_SET:
                _params['scheduled_action_name'] = scheduled_action_name
            _request = shapes.DeleteScheduledActionType(**_params)
        response = self._boto_client.delete_scheduled_action(
            **_request.to_boto()
        )

    def delete_tags(
        self,
        _request: shapes.DeleteTagsType = None,
        *,
        tags: typing.List[shapes.Tag],
    ) -> None:
        """
        Deletes the specified tags.
        """
        if _request is None:
            _params = {}
            if tags is not ShapeBase.NOT_SET:
                _params['tags'] = tags
            _request = shapes.DeleteTagsType(**_params)
        response = self._boto_client.delete_tags(**_request.to_boto())

    def describe_account_limits(self, ) -> shapes.DescribeAccountLimitsAnswer:
        """
        Describes the current Auto Scaling resource limits for your AWS account.

        For information about requesting an increase in these limits, see [Auto Scaling
        Limits](http://docs.aws.amazon.com/autoscaling/ec2/userguide/as-account-
        limits.html) in the _Amazon EC2 Auto Scaling User Guide_.
        """
        response = self._boto_client.describe_account_limits()

        return shapes.DescribeAccountLimitsAnswer.from_boto(response)

    def describe_adjustment_types(
        self,
    ) -> shapes.DescribeAdjustmentTypesAnswer:
        """
        Describes the policy adjustment types for use with PutScalingPolicy.
        """
        response = self._boto_client.describe_adjustment_types()

        return shapes.DescribeAdjustmentTypesAnswer.from_boto(response)

    def describe_auto_scaling_groups(
        self,
        _request: shapes.AutoScalingGroupNamesType = None,
        *,
        auto_scaling_group_names: typing.List[str] = ShapeBase.NOT_SET,
        next_token: str = ShapeBase.NOT_SET,
        max_records: int = ShapeBase.NOT_SET,
    ) -> shapes.AutoScalingGroupsType:
        """
        Describes one or more Auto Scaling groups.
        """
        if _request is None:
            _params = {}
            if auto_scaling_group_names is not ShapeBase.NOT_SET:
                _params['auto_scaling_group_names'] = auto_scaling_group_names
            if next_token is not ShapeBase.NOT_SET:
                _params['next_token'] = next_token
            if max_records is not ShapeBase.NOT_SET:
                _params['max_records'] = max_records
            _request = shapes.AutoScalingGroupNamesType(**_params)
        paginator = self.get_paginator("describe_auto_scaling_groups").paginate(
            **_request.to_boto()
        )
        page_generator = (page for page in paginator)
        first_page = next(page_generator)
        result = shapes.AutoScalingGroupsType.from_boto(first_page)
        result._page_iterator = page_generator
        return result

        return shapes.AutoScalingGroupsType.from_boto(response)

    def describe_auto_scaling_instances(
        self,
        _request: shapes.DescribeAutoScalingInstancesType = None,
        *,
        instance_ids: typing.List[str] = ShapeBase.NOT_SET,
        max_records: int = ShapeBase.NOT_SET,
        next_token: str = ShapeBase.NOT_SET,
    ) -> shapes.AutoScalingInstancesType:
        """
        Describes one or more Auto Scaling instances.
        """
        if _request is None:
            _params = {}
            if instance_ids is not ShapeBase.NOT_SET:
                _params['instance_ids'] = instance_ids
            if max_records is not ShapeBase.NOT_SET:
                _params['max_records'] = max_records
            if next_token is not ShapeBase.NOT_SET:
                _params['next_token'] = next_token
            _request = shapes.DescribeAutoScalingInstancesType(**_params)
        paginator = self.get_paginator("describe_auto_scaling_instances"
                                      ).paginate(**_request.to_boto())
        page_generator = (page for page in paginator)
        first_page = next(page_generator)
        result = shapes.AutoScalingInstancesType.from_boto(first_page)
        result._page_iterator = page_generator
        return result

        return shapes.AutoScalingInstancesType.from_boto(response)

    def describe_auto_scaling_notification_types(
        self,
    ) -> shapes.DescribeAutoScalingNotificationTypesAnswer:
        """
        Describes the notification types that are supported by Amazon EC2 Auto Scaling.
        """
        response = self._boto_client.describe_auto_scaling_notification_types()

        return shapes.DescribeAutoScalingNotificationTypesAnswer.from_boto(
            response
        )

    def describe_launch_configurations(
        self,
        _request: shapes.LaunchConfigurationNamesType = None,
        *,
        launch_configuration_names: typing.List[str] = ShapeBase.NOT_SET,
        next_token: str = ShapeBase.NOT_SET,
        max_records: int = ShapeBase.NOT_SET,
    ) -> shapes.LaunchConfigurationsType:
        """
        Describes one or more launch configurations.
        """
        if _request is None:
            _params = {}
            if launch_configuration_names is not ShapeBase.NOT_SET:
                _params['launch_configuration_names'
                       ] = launch_configuration_names
            if next_token is not ShapeBase.NOT_SET:
                _params['next_token'] = next_token
            if max_records is not ShapeBase.NOT_SET:
                _params['max_records'] = max_records
            _request = shapes.LaunchConfigurationNamesType(**_params)
        paginator = self.get_paginator("describe_launch_configurations"
                                      ).paginate(**_request.to_boto())
        page_generator = (page for page in paginator)
        first_page = next(page_generator)
        result = shapes.LaunchConfigurationsType.from_boto(first_page)
        result._page_iterator = page_generator
        return result

        return shapes.LaunchConfigurationsType.from_boto(response)

    def describe_lifecycle_hook_types(
        self,
    ) -> shapes.DescribeLifecycleHookTypesAnswer:
        """
        Describes the available types of lifecycle hooks.

        The following hook types are supported:

          * autoscaling:EC2_INSTANCE_LAUNCHING

          * autoscaling:EC2_INSTANCE_TERMINATING
        """
        response = self._boto_client.describe_lifecycle_hook_types()

        return shapes.DescribeLifecycleHookTypesAnswer.from_boto(response)

    def describe_lifecycle_hooks(
        self,
        _request: shapes.DescribeLifecycleHooksType = None,
        *,
        auto_scaling_group_name: str,
        lifecycle_hook_names: typing.List[str] = ShapeBase.NOT_SET,
    ) -> shapes.DescribeLifecycleHooksAnswer:
        """
        Describes the lifecycle hooks for the specified Auto Scaling group.
        """
        if _request is None:
            _params = {}
            if auto_scaling_group_name is not ShapeBase.NOT_SET:
                _params['auto_scaling_group_name'] = auto_scaling_group_name
            if lifecycle_hook_names is not ShapeBase.NOT_SET:
                _params['lifecycle_hook_names'] = lifecycle_hook_names
            _request = shapes.DescribeLifecycleHooksType(**_params)
        response = self._boto_client.describe_lifecycle_hooks(
            **_request.to_boto()
        )

        return shapes.DescribeLifecycleHooksAnswer.from_boto(response)

    def describe_load_balancer_target_groups(
        self,
        _request: shapes.DescribeLoadBalancerTargetGroupsRequest = None,
        *,
        auto_scaling_group_name: str,
        next_token: str = ShapeBase.NOT_SET,
        max_records: int = ShapeBase.NOT_SET,
    ) -> shapes.DescribeLoadBalancerTargetGroupsResponse:
        """
        Describes the target groups for the specified Auto Scaling group.
        """
        if _request is None:
            _params = {}
            if auto_scaling_group_name is not ShapeBase.NOT_SET:
                _params['auto_scaling_group_name'] = auto_scaling_group_name
            if next_token is not ShapeBase.NOT_SET:
                _params['next_token'] = next_token
            if max_records is not ShapeBase.NOT_SET:
                _params['max_records'] = max_records
            _request = shapes.DescribeLoadBalancerTargetGroupsRequest(**_params)
        response = self._boto_client.describe_load_balancer_target_groups(
            **_request.to_boto()
        )

        return shapes.DescribeLoadBalancerTargetGroupsResponse.from_boto(
            response
        )

    def describe_load_balancers(
        self,
        _request: shapes.DescribeLoadBalancersRequest = None,
        *,
        auto_scaling_group_name: str,
        next_token: str = ShapeBase.NOT_SET,
        max_records: int = ShapeBase.NOT_SET,
    ) -> shapes.DescribeLoadBalancersResponse:
        """
        Describes the load balancers for the specified Auto Scaling group.

        Note that this operation describes only Classic Load Balancers. If you have
        Application Load Balancers, use DescribeLoadBalancerTargetGroups instead.
        """
        if _request is None:
            _params = {}
            if auto_scaling_group_name is not ShapeBase.NOT_SET:
                _params['auto_scaling_group_name'] = auto_scaling_group_name
            if next_token is not ShapeBase.NOT_SET:
                _params['next_token'] = next_token
            if max_records is not ShapeBase.NOT_SET:
                _params['max_records'] = max_records
            _request = shapes.DescribeLoadBalancersRequest(**_params)
        response = self._boto_client.describe_load_balancers(
            **_request.to_boto()
        )

        return shapes.DescribeLoadBalancersResponse.from_boto(response)

    def describe_metric_collection_types(
        self,
    ) -> shapes.DescribeMetricCollectionTypesAnswer:
        """
        Describes the available CloudWatch metrics for Amazon EC2 Auto Scaling.

        Note that the `GroupStandbyInstances` metric is not returned by default. You
        must explicitly request this metric when calling EnableMetricsCollection.
        """
        response = self._boto_client.describe_metric_collection_types()

        return shapes.DescribeMetricCollectionTypesAnswer.from_boto(response)

    def describe_notification_configurations(
        self,
        _request: shapes.DescribeNotificationConfigurationsType = None,
        *,
        auto_scaling_group_names: typing.List[str] = ShapeBase.NOT_SET,
        next_token: str = ShapeBase.NOT_SET,
        max_records: int = ShapeBase.NOT_SET,
    ) -> shapes.DescribeNotificationConfigurationsAnswer:
        """
        Describes the notification actions associated with the specified Auto Scaling
        group.
        """
        if _request is None:
            _params = {}
            if auto_scaling_group_names is not ShapeBase.NOT_SET:
                _params['auto_scaling_group_names'] = auto_scaling_group_names
            if next_token is not ShapeBase.NOT_SET:
                _params['next_token'] = next_token
            if max_records is not ShapeBase.NOT_SET:
                _params['max_records'] = max_records
            _request = shapes.DescribeNotificationConfigurationsType(**_params)
        paginator = self.get_paginator("describe_notification_configurations"
                                      ).paginate(**_request.to_boto())
        page_generator = (page for page in paginator)
        first_page = next(page_generator)
        result = shapes.DescribeNotificationConfigurationsAnswer.from_boto(
            first_page
        )
        result._page_iterator = page_generator
        return result

        return shapes.DescribeNotificationConfigurationsAnswer.from_boto(
            response
        )

    def describe_policies(
        self,
        _request: shapes.DescribePoliciesType = None,
        *,
        auto_scaling_group_name: str = ShapeBase.NOT_SET,
        policy_names: typing.List[str] = ShapeBase.NOT_SET,
        policy_types: typing.List[str] = ShapeBase.NOT_SET,
        next_token: str = ShapeBase.NOT_SET,
        max_records: int = ShapeBase.NOT_SET,
    ) -> shapes.PoliciesType:
        """
        Describes the policies for the specified Auto Scaling group.
        """
        if _request is None:
            _params = {}
            if auto_scaling_group_name is not ShapeBase.NOT_SET:
                _params['auto_scaling_group_name'] = auto_scaling_group_name
            if policy_names is not ShapeBase.NOT_SET:
                _params['policy_names'] = policy_names
            if policy_types is not ShapeBase.NOT_SET:
                _params['policy_types'] = policy_types
            if next_token is not ShapeBase.NOT_SET:
                _params['next_token'] = next_token
            if max_records is not ShapeBase.NOT_SET:
                _params['max_records'] = max_records
            _request = shapes.DescribePoliciesType(**_params)
        paginator = self.get_paginator("describe_policies").paginate(
            **_request.to_boto()
        )
        page_generator = (page for page in paginator)
        first_page = next(page_generator)
        result = shapes.PoliciesType.from_boto(first_page)
        result._page_iterator = page_generator
        return result

        return shapes.PoliciesType.from_boto(response)

    def describe_scaling_activities(
        self,
        _request: shapes.DescribeScalingActivitiesType = None,
        *,
        activity_ids: typing.List[str] = ShapeBase.NOT_SET,
        auto_scaling_group_name: str = ShapeBase.NOT_SET,
        max_records: int = ShapeBase.NOT_SET,
        next_token: str = ShapeBase.NOT_SET,
    ) -> shapes.ActivitiesType:
        """
        Describes one or more scaling activities for the specified Auto Scaling group.
        """
        if _request is None:
            _params = {}
            if activity_ids is not ShapeBase.NOT_SET:
                _params['activity_ids'] = activity_ids
            if auto_scaling_group_name is not ShapeBase.NOT_SET:
                _params['auto_scaling_group_name'] = auto_scaling_group_name
            if max_records is not ShapeBase.NOT_SET:
                _params['max_records'] = max_records
            if next_token is not ShapeBase.NOT_SET:
                _params['next_token'] = next_token
            _request = shapes.DescribeScalingActivitiesType(**_params)
        paginator = self.get_paginator("describe_scaling_activities").paginate(
            **_request.to_boto()
        )
        page_generator = (page for page in paginator)
        first_page = next(page_generator)
        result = shapes.ActivitiesType.from_boto(first_page)
        result._page_iterator = page_generator
        return result

        return shapes.ActivitiesType.from_boto(response)

    def describe_scaling_process_types(self) -> shapes.ProcessesType:
        """
        Describes the scaling process types for use with ResumeProcesses and
        SuspendProcesses.
        """
        response = self._boto_client.describe_scaling_process_types()

        return shapes.ProcessesType.from_boto(response)

    def describe_scheduled_actions(
        self,
        _request: shapes.DescribeScheduledActionsType = None,
        *,
        auto_scaling_group_name: str = ShapeBase.NOT_SET,
        scheduled_action_names: typing.List[str] = ShapeBase.NOT_SET,
        start_time: datetime.datetime = ShapeBase.NOT_SET,
        end_time: datetime.datetime = ShapeBase.NOT_SET,
        next_token: str = ShapeBase.NOT_SET,
        max_records: int = ShapeBase.NOT_SET,
    ) -> shapes.ScheduledActionsType:
        """
        Describes the actions scheduled for your Auto Scaling group that haven't run. To
        describe the actions that have already run, use DescribeScalingActivities.
        """
        if _request is None:
            _params = {}
            if auto_scaling_group_name is not ShapeBase.NOT_SET:
                _params['auto_scaling_group_name'] = auto_scaling_group_name
            if scheduled_action_names is not ShapeBase.NOT_SET:
                _params['scheduled_action_names'] = scheduled_action_names
            if start_time is not ShapeBase.NOT_SET:
                _params['start_time'] = start_time
            if end_time is not ShapeBase.NOT_SET:
                _params['end_time'] = end_time
            if next_token is not ShapeBase.NOT_SET:
                _params['next_token'] = next_token
            if max_records is not ShapeBase.NOT_SET:
                _params['max_records'] = max_records
            _request = shapes.DescribeScheduledActionsType(**_params)
        paginator = self.get_paginator("describe_scheduled_actions").paginate(
            **_request.to_boto()
        )
        page_generator = (page for page in paginator)
        first_page = next(page_generator)
        result = shapes.ScheduledActionsType.from_boto(first_page)
        result._page_iterator = page_generator
        return result

        return shapes.ScheduledActionsType.from_boto(response)

    def describe_tags(
        self,
        _request: shapes.DescribeTagsType = None,
        *,
        filters: typing.List[shapes.Filter] = ShapeBase.NOT_SET,
        next_token: str = ShapeBase.NOT_SET,
        max_records: int = ShapeBase.NOT_SET,
    ) -> shapes.TagsType:
        """
        Describes the specified tags.

        You can use filters to limit the results. For example, you can query for the
        tags for a specific Auto Scaling group. You can specify multiple values for a
        filter. A tag must match at least one of the specified values for it to be
        included in the results.

        You can also specify multiple filters. The result includes information for a
        particular tag only if it matches all the filters. If there's no match, no
        special message is returned.
        """
        if _request is None:
            _params = {}
            if filters is not ShapeBase.NOT_SET:
                _params['filters'] = filters
            if next_token is not ShapeBase.NOT_SET:
                _params['next_token'] = next_token
            if max_records is not ShapeBase.NOT_SET:
                _params['max_records'] = max_records
            _request = shapes.DescribeTagsType(**_params)
        paginator = self.get_paginator("describe_tags").paginate(
            **_request.to_boto()
        )
        page_generator = (page for page in paginator)
        first_page = next(page_generator)
        result = shapes.TagsType.from_boto(first_page)
        result._page_iterator = page_generator
        return result

        return shapes.TagsType.from_boto(response)

    def describe_termination_policy_types(
        self,
    ) -> shapes.DescribeTerminationPolicyTypesAnswer:
        """
        Describes the termination policies supported by Amazon EC2 Auto Scaling.
        """
        response = self._boto_client.describe_termination_policy_types()

        return shapes.DescribeTerminationPolicyTypesAnswer.from_boto(response)

    def detach_instances(
        self,
        _request: shapes.DetachInstancesQuery = None,
        *,
        auto_scaling_group_name: str,
        should_decrement_desired_capacity: bool,
        instance_ids: typing.List[str] = ShapeBase.NOT_SET,
    ) -> shapes.DetachInstancesAnswer:
        """
        Removes one or more instances from the specified Auto Scaling group.

        After the instances are detached, you can manage them independent of the Auto
        Scaling group.

        If you do not specify the option to decrement the desired capacity, Amazon EC2
        Auto Scaling launches instances to replace the ones that are detached.

        If there is a Classic Load Balancer attached to the Auto Scaling group, the
        instances are deregistered from the load balancer. If there are target groups
        attached to the Auto Scaling group, the instances are deregistered from the
        target groups.

        For more information, see [Detach EC2 Instances from Your Auto Scaling
        Group](http://docs.aws.amazon.com/autoscaling/ec2/userguide/detach-instance-
        asg.html) in the _Amazon EC2 Auto Scaling User Guide_.
        """
        if _request is None:
            _params = {}
            if auto_scaling_group_name is not ShapeBase.NOT_SET:
                _params['auto_scaling_group_name'] = auto_scaling_group_name
            if should_decrement_desired_capacity is not ShapeBase.NOT_SET:
                _params['should_decrement_desired_capacity'
                       ] = should_decrement_desired_capacity
            if instance_ids is not ShapeBase.NOT_SET:
                _params['instance_ids'] = instance_ids
            _request = shapes.DetachInstancesQuery(**_params)
        response = self._boto_client.detach_instances(**_request.to_boto())

        return shapes.DetachInstancesAnswer.from_boto(response)

    def detach_load_balancer_target_groups(
        self,
        _request: shapes.DetachLoadBalancerTargetGroupsType = None,
        *,
        auto_scaling_group_name: str,
        target_group_arns: typing.List[str],
    ) -> shapes.DetachLoadBalancerTargetGroupsResultType:
        """
        Detaches one or more target groups from the specified Auto Scaling group.
        """
        if _request is None:
            _params = {}
            if auto_scaling_group_name is not ShapeBase.NOT_SET:
                _params['auto_scaling_group_name'] = auto_scaling_group_name
            if target_group_arns is not ShapeBase.NOT_SET:
                _params['target_group_arns'] = target_group_arns
            _request = shapes.DetachLoadBalancerTargetGroupsType(**_params)
        response = self._boto_client.detach_load_balancer_target_groups(
            **_request.to_boto()
        )

        return shapes.DetachLoadBalancerTargetGroupsResultType.from_boto(
            response
        )

    def detach_load_balancers(
        self,
        _request: shapes.DetachLoadBalancersType = None,
        *,
        auto_scaling_group_name: str,
        load_balancer_names: typing.List[str],
    ) -> shapes.DetachLoadBalancersResultType:
        """
        Detaches one or more Classic Load Balancers from the specified Auto Scaling
        group.

        Note that this operation detaches only Classic Load Balancers. If you have
        Application Load Balancers, use DetachLoadBalancerTargetGroups instead.

        When you detach a load balancer, it enters the `Removing` state while
        deregistering the instances in the group. When all instances are deregistered,
        then you can no longer describe the load balancer using DescribeLoadBalancers.
        Note that the instances remain running.
        """
        if _request is None:
            _params = {}
            if auto_scaling_group_name is not ShapeBase.NOT_SET:
                _params['auto_scaling_group_name'] = auto_scaling_group_name
            if load_balancer_names is not ShapeBase.NOT_SET:
                _params['load_balancer_names'] = load_balancer_names
            _request = shapes.DetachLoadBalancersType(**_params)
        response = self._boto_client.detach_load_balancers(**_request.to_boto())

        return shapes.DetachLoadBalancersResultType.from_boto(response)

    def disable_metrics_collection(
        self,
        _request: shapes.DisableMetricsCollectionQuery = None,
        *,
        auto_scaling_group_name: str,
        metrics: typing.List[str] = ShapeBase.NOT_SET,
    ) -> None:
        """
        Disables group metrics for the specified Auto Scaling group.
        """
        if _request is None:
            _params = {}
            if auto_scaling_group_name is not ShapeBase.NOT_SET:
                _params['auto_scaling_group_name'] = auto_scaling_group_name
            if metrics is not ShapeBase.NOT_SET:
                _params['metrics'] = metrics
            _request = shapes.DisableMetricsCollectionQuery(**_params)
        response = self._boto_client.disable_metrics_collection(
            **_request.to_boto()
        )

    def enable_metrics_collection(
        self,
        _request: shapes.EnableMetricsCollectionQuery = None,
        *,
        auto_scaling_group_name: str,
        granularity: str,
        metrics: typing.List[str] = ShapeBase.NOT_SET,
    ) -> None:
        """
        Enables group metrics for the specified Auto Scaling group. For more
        information, see [Monitoring Your Auto Scaling Groups and
        Instances](http://docs.aws.amazon.com/autoscaling/ec2/userguide/as-instance-
        monitoring.html) in the _Amazon EC2 Auto Scaling User Guide_.
        """
        if _request is None:
            _params = {}
            if auto_scaling_group_name is not ShapeBase.NOT_SET:
                _params['auto_scaling_group_name'] = auto_scaling_group_name
            if granularity is not ShapeBase.NOT_SET:
                _params['granularity'] = granularity
            if metrics is not ShapeBase.NOT_SET:
                _params['metrics'] = metrics
            _request = shapes.EnableMetricsCollectionQuery(**_params)
        response = self._boto_client.enable_metrics_collection(
            **_request.to_boto()
        )

    def enter_standby(
        self,
        _request: shapes.EnterStandbyQuery = None,
        *,
        auto_scaling_group_name: str,
        should_decrement_desired_capacity: bool,
        instance_ids: typing.List[str] = ShapeBase.NOT_SET,
    ) -> shapes.EnterStandbyAnswer:
        """
        Moves the specified instances into the standby state.

        For more information, see [Temporarily Removing Instances from Your Auto Scaling
        Group](http://docs.aws.amazon.com/autoscaling/ec2/userguide/as-enter-exit-
        standby.html) in the _Amazon EC2 Auto Scaling User Guide_.
        """
        if _request is None:
            _params = {}
            if auto_scaling_group_name is not ShapeBase.NOT_SET:
                _params['auto_scaling_group_name'] = auto_scaling_group_name
            if should_decrement_desired_capacity is not ShapeBase.NOT_SET:
                _params['should_decrement_desired_capacity'
                       ] = should_decrement_desired_capacity
            if instance_ids is not ShapeBase.NOT_SET:
                _params['instance_ids'] = instance_ids
            _request = shapes.EnterStandbyQuery(**_params)
        response = self._boto_client.enter_standby(**_request.to_boto())

        return shapes.EnterStandbyAnswer.from_boto(response)

    def execute_policy(
        self,
        _request: shapes.ExecutePolicyType = None,
        *,
        policy_name: str,
        auto_scaling_group_name: str = ShapeBase.NOT_SET,
        honor_cooldown: bool = ShapeBase.NOT_SET,
        metric_value: float = ShapeBase.NOT_SET,
        breach_threshold: float = ShapeBase.NOT_SET,
    ) -> None:
        """
        Executes the specified policy.
        """
        if _request is None:
            _params = {}
            if policy_name is not ShapeBase.NOT_SET:
                _params['policy_name'] = policy_name
            if auto_scaling_group_name is not ShapeBase.NOT_SET:
                _params['auto_scaling_group_name'] = auto_scaling_group_name
            if honor_cooldown is not ShapeBase.NOT_SET:
                _params['honor_cooldown'] = honor_cooldown
            if metric_value is not ShapeBase.NOT_SET:
                _params['metric_value'] = metric_value
            if breach_threshold is not ShapeBase.NOT_SET:
                _params['breach_threshold'] = breach_threshold
            _request = shapes.ExecutePolicyType(**_params)
        response = self._boto_client.execute_policy(**_request.to_boto())

    def exit_standby(
        self,
        _request: shapes.ExitStandbyQuery = None,
        *,
        auto_scaling_group_name: str,
        instance_ids: typing.List[str] = ShapeBase.NOT_SET,
    ) -> shapes.ExitStandbyAnswer:
        """
        Moves the specified instances out of the standby state.

        For more information, see [Temporarily Removing Instances from Your Auto Scaling
        Group](http://docs.aws.amazon.com/autoscaling/ec2/userguide/as-enter-exit-
        standby.html) in the _Amazon EC2 Auto Scaling User Guide_.
        """
        if _request is None:
            _params = {}
            if auto_scaling_group_name is not ShapeBase.NOT_SET:
                _params['auto_scaling_group_name'] = auto_scaling_group_name
            if instance_ids is not ShapeBase.NOT_SET:
                _params['instance_ids'] = instance_ids
            _request = shapes.ExitStandbyQuery(**_params)
        response = self._boto_client.exit_standby(**_request.to_boto())

        return shapes.ExitStandbyAnswer.from_boto(response)

    def put_lifecycle_hook(
        self,
        _request: shapes.PutLifecycleHookType = None,
        *,
        lifecycle_hook_name: str,
        auto_scaling_group_name: str,
        lifecycle_transition: str = ShapeBase.NOT_SET,
        role_arn: str = ShapeBase.NOT_SET,
        notification_target_arn: str = ShapeBase.NOT_SET,
        notification_metadata: str = ShapeBase.NOT_SET,
        heartbeat_timeout: int = ShapeBase.NOT_SET,
        default_result: str = ShapeBase.NOT_SET,
    ) -> shapes.PutLifecycleHookAnswer:
        """
        Creates or updates a lifecycle hook for the specified Auto Scaling Group.

        A lifecycle hook tells Amazon EC2 Auto Scaling that you want to perform an
        action on an instance that is not actively in service; for example, either when
        the instance launches or before the instance terminates.

        This step is a part of the procedure for adding a lifecycle hook to an Auto
        Scaling group:

          1. (Optional) Create a Lambda function and a rule that allows CloudWatch Events to invoke your Lambda function when Amazon EC2 Auto Scaling launches or terminates instances.

          2. (Optional) Create a notification target and an IAM role. The target can be either an Amazon SQS queue or an Amazon SNS topic. The role allows Amazon EC2 Auto Scaling to publish lifecycle notifications to the target.

          3. **Create the lifecycle hook. Specify whether the hook is used when the instances launch or terminate.**

          4. If you need more time, record the lifecycle action heartbeat to keep the instance in a pending state.

          5. If you finish before the timeout period ends, complete the lifecycle action.

        For more information, see [Auto Scaling Lifecycle
        Hooks](http://docs.aws.amazon.com/autoscaling/ec2/userguide/lifecycle-
        hooks.html) in the _Amazon EC2 Auto Scaling User Guide_.

        If you exceed your maximum limit of lifecycle hooks, which by default is 50 per
        Auto Scaling group, the call fails. For information about updating this limit,
        see [AWS Service
        Limits](http://docs.aws.amazon.com/general/latest/gr/aws_service_limits.html) in
        the _Amazon Web Services General Reference_.
        """
        if _request is None:
            _params = {}
            if lifecycle_hook_name is not ShapeBase.NOT_SET:
                _params['lifecycle_hook_name'] = lifecycle_hook_name
            if auto_scaling_group_name is not ShapeBase.NOT_SET:
                _params['auto_scaling_group_name'] = auto_scaling_group_name
            if lifecycle_transition is not ShapeBase.NOT_SET:
                _params['lifecycle_transition'] = lifecycle_transition
            if role_arn is not ShapeBase.NOT_SET:
                _params['role_arn'] = role_arn
            if notification_target_arn is not ShapeBase.NOT_SET:
                _params['notification_target_arn'] = notification_target_arn
            if notification_metadata is not ShapeBase.NOT_SET:
                _params['notification_metadata'] = notification_metadata
            if heartbeat_timeout is not ShapeBase.NOT_SET:
                _params['heartbeat_timeout'] = heartbeat_timeout
            if default_result is not ShapeBase.NOT_SET:
                _params['default_result'] = default_result
            _request = shapes.PutLifecycleHookType(**_params)
        response = self._boto_client.put_lifecycle_hook(**_request.to_boto())

        return shapes.PutLifecycleHookAnswer.from_boto(response)

    def put_notification_configuration(
        self,
        _request: shapes.PutNotificationConfigurationType = None,
        *,
        auto_scaling_group_name: str,
        topic_arn: str,
        notification_types: typing.List[str],
    ) -> None:
        """
        Configures an Auto Scaling group to send notifications when specified events
        take place. Subscribers to the specified topic can have messages delivered to an
        endpoint such as a web server or an email address.

        This configuration overwrites any existing configuration.

        For more information see [Getting SNS Notifications When Your Auto Scaling Group
        Scales](http://docs.aws.amazon.com/autoscaling/ec2/userguide/ASGettingNotifications.html)
        in the _Auto Scaling User Guide_.
        """
        if _request is None:
            _params = {}
            if auto_scaling_group_name is not ShapeBase.NOT_SET:
                _params['auto_scaling_group_name'] = auto_scaling_group_name
            if topic_arn is not ShapeBase.NOT_SET:
                _params['topic_arn'] = topic_arn
            if notification_types is not ShapeBase.NOT_SET:
                _params['notification_types'] = notification_types
            _request = shapes.PutNotificationConfigurationType(**_params)
        response = self._boto_client.put_notification_configuration(
            **_request.to_boto()
        )

    def put_scaling_policy(
        self,
        _request: shapes.PutScalingPolicyType = None,
        *,
        auto_scaling_group_name: str,
        policy_name: str,
        policy_type: str = ShapeBase.NOT_SET,
        adjustment_type: str = ShapeBase.NOT_SET,
        min_adjustment_step: int = ShapeBase.NOT_SET,
        min_adjustment_magnitude: int = ShapeBase.NOT_SET,
        scaling_adjustment: int = ShapeBase.NOT_SET,
        cooldown: int = ShapeBase.NOT_SET,
        metric_aggregation_type: str = ShapeBase.NOT_SET,
        step_adjustments: typing.List[shapes.StepAdjustment
                                     ] = ShapeBase.NOT_SET,
        estimated_instance_warmup: int = ShapeBase.NOT_SET,
        target_tracking_configuration: shapes.
        TargetTrackingConfiguration = ShapeBase.NOT_SET,
    ) -> shapes.PolicyARNType:
        """
        Creates or updates a policy for an Auto Scaling group. To update an existing
        policy, use the existing policy name and set the parameters you want to change.
        Any existing parameter not changed in an update to an existing policy is not
        changed in this update request.

        If you exceed your maximum limit of step adjustments, which by default is 20 per
        region, the call fails. For information about updating this limit, see [AWS
        Service
        Limits](http://docs.aws.amazon.com/general/latest/gr/aws_service_limits.html) in
        the _Amazon Web Services General Reference_.
        """
        if _request is None:
            _params = {}
            if auto_scaling_group_name is not ShapeBase.NOT_SET:
                _params['auto_scaling_group_name'] = auto_scaling_group_name
            if policy_name is not ShapeBase.NOT_SET:
                _params['policy_name'] = policy_name
            if policy_type is not ShapeBase.NOT_SET:
                _params['policy_type'] = policy_type
            if adjustment_type is not ShapeBase.NOT_SET:
                _params['adjustment_type'] = adjustment_type
            if min_adjustment_step is not ShapeBase.NOT_SET:
                _params['min_adjustment_step'] = min_adjustment_step
            if min_adjustment_magnitude is not ShapeBase.NOT_SET:
                _params['min_adjustment_magnitude'] = min_adjustment_magnitude
            if scaling_adjustment is not ShapeBase.NOT_SET:
                _params['scaling_adjustment'] = scaling_adjustment
            if cooldown is not ShapeBase.NOT_SET:
                _params['cooldown'] = cooldown
            if metric_aggregation_type is not ShapeBase.NOT_SET:
                _params['metric_aggregation_type'] = metric_aggregation_type
            if step_adjustments is not ShapeBase.NOT_SET:
                _params['step_adjustments'] = step_adjustments
            if estimated_instance_warmup is not ShapeBase.NOT_SET:
                _params['estimated_instance_warmup'] = estimated_instance_warmup
            if target_tracking_configuration is not ShapeBase.NOT_SET:
                _params['target_tracking_configuration'
                       ] = target_tracking_configuration
            _request = shapes.PutScalingPolicyType(**_params)
        response = self._boto_client.put_scaling_policy(**_request.to_boto())

        return shapes.PolicyARNType.from_boto(response)

    def put_scheduled_update_group_action(
        self,
        _request: shapes.PutScheduledUpdateGroupActionType = None,
        *,
        auto_scaling_group_name: str,
        scheduled_action_name: str,
        time: datetime.datetime = ShapeBase.NOT_SET,
        start_time: datetime.datetime = ShapeBase.NOT_SET,
        end_time: datetime.datetime = ShapeBase.NOT_SET,
        recurrence: str = ShapeBase.NOT_SET,
        min_size: int = ShapeBase.NOT_SET,
        max_size: int = ShapeBase.NOT_SET,
        desired_capacity: int = ShapeBase.NOT_SET,
    ) -> None:
        """
        Creates or updates a scheduled scaling action for an Auto Scaling group. When
        updating a scheduled scaling action, if you leave a parameter unspecified, the
        corresponding value remains unchanged.

        For more information, see [Scheduled
        Scaling](http://docs.aws.amazon.com/autoscaling/ec2/userguide/schedule_time.html)
        in the _Amazon EC2 Auto Scaling User Guide_.
        """
        if _request is None:
            _params = {}
            if auto_scaling_group_name is not ShapeBase.NOT_SET:
                _params['auto_scaling_group_name'] = auto_scaling_group_name
            if scheduled_action_name is not ShapeBase.NOT_SET:
                _params['scheduled_action_name'] = scheduled_action_name
            if time is not ShapeBase.NOT_SET:
                _params['time'] = time
            if start_time is not ShapeBase.NOT_SET:
                _params['start_time'] = start_time
            if end_time is not ShapeBase.NOT_SET:
                _params['end_time'] = end_time
            if recurrence is not ShapeBase.NOT_SET:
                _params['recurrence'] = recurrence
            if min_size is not ShapeBase.NOT_SET:
                _params['min_size'] = min_size
            if max_size is not ShapeBase.NOT_SET:
                _params['max_size'] = max_size
            if desired_capacity is not ShapeBase.NOT_SET:
                _params['desired_capacity'] = desired_capacity
            _request = shapes.PutScheduledUpdateGroupActionType(**_params)
        response = self._boto_client.put_scheduled_update_group_action(
            **_request.to_boto()
        )

    def record_lifecycle_action_heartbeat(
        self,
        _request: shapes.RecordLifecycleActionHeartbeatType = None,
        *,
        lifecycle_hook_name: str,
        auto_scaling_group_name: str,
        lifecycle_action_token: str = ShapeBase.NOT_SET,
        instance_id: str = ShapeBase.NOT_SET,
    ) -> shapes.RecordLifecycleActionHeartbeatAnswer:
        """
        Records a heartbeat for the lifecycle action associated with the specified token
        or instance. This extends the timeout by the length of time defined using
        PutLifecycleHook.

        This step is a part of the procedure for adding a lifecycle hook to an Auto
        Scaling group:

          1. (Optional) Create a Lambda function and a rule that allows CloudWatch Events to invoke your Lambda function when Amazon EC2 Auto Scaling launches or terminates instances.

          2. (Optional) Create a notification target and an IAM role. The target can be either an Amazon SQS queue or an Amazon SNS topic. The role allows Amazon EC2 Auto Scaling to publish lifecycle notifications to the target.

          3. Create the lifecycle hook. Specify whether the hook is used when the instances launch or terminate.

          4. **If you need more time, record the lifecycle action heartbeat to keep the instance in a pending state.**

          5. If you finish before the timeout period ends, complete the lifecycle action.

        For more information, see [Auto Scaling
        Lifecycle](http://docs.aws.amazon.com/autoscaling/ec2/userguide/AutoScalingGroupLifecycle.html)
        in the _Amazon EC2 Auto Scaling User Guide_.
        """
        if _request is None:
            _params = {}
            if lifecycle_hook_name is not ShapeBase.NOT_SET:
                _params['lifecycle_hook_name'] = lifecycle_hook_name
            if auto_scaling_group_name is not ShapeBase.NOT_SET:
                _params['auto_scaling_group_name'] = auto_scaling_group_name
            if lifecycle_action_token is not ShapeBase.NOT_SET:
                _params['lifecycle_action_token'] = lifecycle_action_token
            if instance_id is not ShapeBase.NOT_SET:
                _params['instance_id'] = instance_id
            _request = shapes.RecordLifecycleActionHeartbeatType(**_params)
        response = self._boto_client.record_lifecycle_action_heartbeat(
            **_request.to_boto()
        )

        return shapes.RecordLifecycleActionHeartbeatAnswer.from_boto(response)

    def resume_processes(
        self,
        _request: shapes.ScalingProcessQuery = None,
        *,
        auto_scaling_group_name: str,
        scaling_processes: typing.List[str] = ShapeBase.NOT_SET,
    ) -> None:
        """
        Resumes the specified suspended automatic scaling processes, or all suspended
        process, for the specified Auto Scaling group.

        For more information, see [Suspending and Resuming Scaling
        Processes](http://docs.aws.amazon.com/autoscaling/ec2/userguide/as-suspend-
        resume-processes.html) in the _Amazon EC2 Auto Scaling User Guide_.
        """
        if _request is None:
            _params = {}
            if auto_scaling_group_name is not ShapeBase.NOT_SET:
                _params['auto_scaling_group_name'] = auto_scaling_group_name
            if scaling_processes is not ShapeBase.NOT_SET:
                _params['scaling_processes'] = scaling_processes
            _request = shapes.ScalingProcessQuery(**_params)
        response = self._boto_client.resume_processes(**_request.to_boto())

    def set_desired_capacity(
        self,
        _request: shapes.SetDesiredCapacityType = None,
        *,
        auto_scaling_group_name: str,
        desired_capacity: int,
        honor_cooldown: bool = ShapeBase.NOT_SET,
    ) -> None:
        """
        Sets the size of the specified Auto Scaling group.

        For more information about desired capacity, see [What Is Amazon EC2 Auto
        Scaling?](http://docs.aws.amazon.com/autoscaling/ec2/userguide/WhatIsAutoScaling.html)
        in the _Amazon EC2 Auto Scaling User Guide_.
        """
        if _request is None:
            _params = {}
            if auto_scaling_group_name is not ShapeBase.NOT_SET:
                _params['auto_scaling_group_name'] = auto_scaling_group_name
            if desired_capacity is not ShapeBase.NOT_SET:
                _params['desired_capacity'] = desired_capacity
            if honor_cooldown is not ShapeBase.NOT_SET:
                _params['honor_cooldown'] = honor_cooldown
            _request = shapes.SetDesiredCapacityType(**_params)
        response = self._boto_client.set_desired_capacity(**_request.to_boto())

    def set_instance_health(
        self,
        _request: shapes.SetInstanceHealthQuery = None,
        *,
        instance_id: str,
        health_status: str,
        should_respect_grace_period: bool = ShapeBase.NOT_SET,
    ) -> None:
        """
        Sets the health status of the specified instance.

        For more information, see [Health
        Checks](http://docs.aws.amazon.com/autoscaling/ec2/userguide/healthcheck.html)
        in the _Amazon EC2 Auto Scaling User Guide_.
        """
        if _request is None:
            _params = {}
            if instance_id is not ShapeBase.NOT_SET:
                _params['instance_id'] = instance_id
            if health_status is not ShapeBase.NOT_SET:
                _params['health_status'] = health_status
            if should_respect_grace_period is not ShapeBase.NOT_SET:
                _params['should_respect_grace_period'
                       ] = should_respect_grace_period
            _request = shapes.SetInstanceHealthQuery(**_params)
        response = self._boto_client.set_instance_health(**_request.to_boto())

    def set_instance_protection(
        self,
        _request: shapes.SetInstanceProtectionQuery = None,
        *,
        instance_ids: typing.List[str],
        auto_scaling_group_name: str,
        protected_from_scale_in: bool,
    ) -> shapes.SetInstanceProtectionAnswer:
        """
        Updates the instance protection settings of the specified instances.

        For more information, see [Instance
        Protection](http://docs.aws.amazon.com/autoscaling/ec2/userguide/as-instance-
        termination.html#instance-protection) in the _Amazon EC2 Auto Scaling User
        Guide_.
        """
        if _request is None:
            _params = {}
            if instance_ids is not ShapeBase.NOT_SET:
                _params['instance_ids'] = instance_ids
            if auto_scaling_group_name is not ShapeBase.NOT_SET:
                _params['auto_scaling_group_name'] = auto_scaling_group_name
            if protected_from_scale_in is not ShapeBase.NOT_SET:
                _params['protected_from_scale_in'] = protected_from_scale_in
            _request = shapes.SetInstanceProtectionQuery(**_params)
        response = self._boto_client.set_instance_protection(
            **_request.to_boto()
        )

        return shapes.SetInstanceProtectionAnswer.from_boto(response)

    def suspend_processes(
        self,
        _request: shapes.ScalingProcessQuery = None,
        *,
        auto_scaling_group_name: str,
        scaling_processes: typing.List[str] = ShapeBase.NOT_SET,
    ) -> None:
        """
        Suspends the specified automatic scaling processes, or all processes, for the
        specified Auto Scaling group.

        Note that if you suspend either the `Launch` or `Terminate` process types, it
        can prevent other process types from functioning properly.

        To resume processes that have been suspended, use ResumeProcesses.

        For more information, see [Suspending and Resuming Scaling
        Processes](http://docs.aws.amazon.com/autoscaling/ec2/userguide/as-suspend-
        resume-processes.html) in the _Amazon EC2 Auto Scaling User Guide_.
        """
        if _request is None:
            _params = {}
            if auto_scaling_group_name is not ShapeBase.NOT_SET:
                _params['auto_scaling_group_name'] = auto_scaling_group_name
            if scaling_processes is not ShapeBase.NOT_SET:
                _params['scaling_processes'] = scaling_processes
            _request = shapes.ScalingProcessQuery(**_params)
        response = self._boto_client.suspend_processes(**_request.to_boto())

    def terminate_instance_in_auto_scaling_group(
        self,
        _request: shapes.TerminateInstanceInAutoScalingGroupType = None,
        *,
        instance_id: str,
        should_decrement_desired_capacity: bool,
    ) -> shapes.ActivityType:
        """
        Terminates the specified instance and optionally adjusts the desired group size.

        This call simply makes a termination request. The instance is not terminated
        immediately.
        """
        if _request is None:
            _params = {}
            if instance_id is not ShapeBase.NOT_SET:
                _params['instance_id'] = instance_id
            if should_decrement_desired_capacity is not ShapeBase.NOT_SET:
                _params['should_decrement_desired_capacity'
                       ] = should_decrement_desired_capacity
            _request = shapes.TerminateInstanceInAutoScalingGroupType(**_params)
        response = self._boto_client.terminate_instance_in_auto_scaling_group(
            **_request.to_boto()
        )

        return shapes.ActivityType.from_boto(response)

    def update_auto_scaling_group(
        self,
        _request: shapes.UpdateAutoScalingGroupType = None,
        *,
        auto_scaling_group_name: str,
        launch_configuration_name: str = ShapeBase.NOT_SET,
        launch_template: shapes.LaunchTemplateSpecification = ShapeBase.NOT_SET,
        min_size: int = ShapeBase.NOT_SET,
        max_size: int = ShapeBase.NOT_SET,
        desired_capacity: int = ShapeBase.NOT_SET,
        default_cooldown: int = ShapeBase.NOT_SET,
        availability_zones: typing.List[str] = ShapeBase.NOT_SET,
        health_check_type: str = ShapeBase.NOT_SET,
        health_check_grace_period: int = ShapeBase.NOT_SET,
        placement_group: str = ShapeBase.NOT_SET,
        vpc_zone_identifier: str = ShapeBase.NOT_SET,
        termination_policies: typing.List[str] = ShapeBase.NOT_SET,
        new_instances_protected_from_scale_in: bool = ShapeBase.NOT_SET,
        service_linked_role_arn: str = ShapeBase.NOT_SET,
    ) -> None:
        """
        Updates the configuration for the specified Auto Scaling group.

        The new settings take effect on any scaling activities after this call returns.
        Scaling activities that are currently in progress aren't affected.

        To update an Auto Scaling group with a launch configuration with
        `InstanceMonitoring` set to `false`, you must first disable the collection of
        group metrics. Otherwise, you will get an error. If you have previously enabled
        the collection of group metrics, you can disable it using
        DisableMetricsCollection.

        Note the following:

          * If you specify a new value for `MinSize` without specifying a value for `DesiredCapacity`, and the new `MinSize` is larger than the current size of the group, we implicitly call SetDesiredCapacity to set the size of the group to the new value of `MinSize`.

          * If you specify a new value for `MaxSize` without specifying a value for `DesiredCapacity`, and the new `MaxSize` is smaller than the current size of the group, we implicitly call SetDesiredCapacity to set the size of the group to the new value of `MaxSize`.

          * All other optional parameters are left unchanged if not specified.
        """
        if _request is None:
            _params = {}
            if auto_scaling_group_name is not ShapeBase.NOT_SET:
                _params['auto_scaling_group_name'] = auto_scaling_group_name
            if launch_configuration_name is not ShapeBase.NOT_SET:
                _params['launch_configuration_name'] = launch_configuration_name
            if launch_template is not ShapeBase.NOT_SET:
                _params['launch_template'] = launch_template
            if min_size is not ShapeBase.NOT_SET:
                _params['min_size'] = min_size
            if max_size is not ShapeBase.NOT_SET:
                _params['max_size'] = max_size
            if desired_capacity is not ShapeBase.NOT_SET:
                _params['desired_capacity'] = desired_capacity
            if default_cooldown is not ShapeBase.NOT_SET:
                _params['default_cooldown'] = default_cooldown
            if availability_zones is not ShapeBase.NOT_SET:
                _params['availability_zones'] = availability_zones
            if health_check_type is not ShapeBase.NOT_SET:
                _params['health_check_type'] = health_check_type
            if health_check_grace_period is not ShapeBase.NOT_SET:
                _params['health_check_grace_period'] = health_check_grace_period
            if placement_group is not ShapeBase.NOT_SET:
                _params['placement_group'] = placement_group
            if vpc_zone_identifier is not ShapeBase.NOT_SET:
                _params['vpc_zone_identifier'] = vpc_zone_identifier
            if termination_policies is not ShapeBase.NOT_SET:
                _params['termination_policies'] = termination_policies
            if new_instances_protected_from_scale_in is not ShapeBase.NOT_SET:
                _params['new_instances_protected_from_scale_in'
                       ] = new_instances_protected_from_scale_in
            if service_linked_role_arn is not ShapeBase.NOT_SET:
                _params['service_linked_role_arn'] = service_linked_role_arn
            _request = shapes.UpdateAutoScalingGroupType(**_params)
        response = self._boto_client.update_auto_scaling_group(
            **_request.to_boto()
        )
