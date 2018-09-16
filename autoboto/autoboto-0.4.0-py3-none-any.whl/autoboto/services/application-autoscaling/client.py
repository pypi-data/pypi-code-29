import datetime
import typing
import boto3
from autoboto import ClientBase, ShapeBase, OutputShapeBase
from . import shapes


class Client(ClientBase):
    def __init__(self, *args, **kwargs):
        super().__init__("application-autoscaling", *args, **kwargs)

    def delete_scaling_policy(
        self,
        _request: shapes.DeleteScalingPolicyRequest = None,
        *,
        policy_name: str,
        service_namespace: typing.Union[str, shapes.ServiceNamespace],
        resource_id: str,
        scalable_dimension: typing.Union[str, shapes.ScalableDimension],
    ) -> shapes.DeleteScalingPolicyResponse:
        """
        Deletes the specified Application Auto Scaling scaling policy.

        Deleting a policy deletes the underlying alarm action, but does not delete the
        CloudWatch alarm associated with the scaling policy, even if it no longer has an
        associated action.

        To create a scaling policy or update an existing one, see PutScalingPolicy.
        """
        if _request is None:
            _params = {}
            if policy_name is not ShapeBase.NOT_SET:
                _params['policy_name'] = policy_name
            if service_namespace is not ShapeBase.NOT_SET:
                _params['service_namespace'] = service_namespace
            if resource_id is not ShapeBase.NOT_SET:
                _params['resource_id'] = resource_id
            if scalable_dimension is not ShapeBase.NOT_SET:
                _params['scalable_dimension'] = scalable_dimension
            _request = shapes.DeleteScalingPolicyRequest(**_params)
        response = self._boto_client.delete_scaling_policy(**_request.to_boto())

        return shapes.DeleteScalingPolicyResponse.from_boto(response)

    def delete_scheduled_action(
        self,
        _request: shapes.DeleteScheduledActionRequest = None,
        *,
        service_namespace: typing.Union[str, shapes.ServiceNamespace],
        scheduled_action_name: str,
        resource_id: str,
        scalable_dimension: typing.Union[str, shapes.
                                         ScalableDimension] = ShapeBase.NOT_SET,
    ) -> shapes.DeleteScheduledActionResponse:
        """
        Deletes the specified Application Auto Scaling scheduled action.
        """
        if _request is None:
            _params = {}
            if service_namespace is not ShapeBase.NOT_SET:
                _params['service_namespace'] = service_namespace
            if scheduled_action_name is not ShapeBase.NOT_SET:
                _params['scheduled_action_name'] = scheduled_action_name
            if resource_id is not ShapeBase.NOT_SET:
                _params['resource_id'] = resource_id
            if scalable_dimension is not ShapeBase.NOT_SET:
                _params['scalable_dimension'] = scalable_dimension
            _request = shapes.DeleteScheduledActionRequest(**_params)
        response = self._boto_client.delete_scheduled_action(
            **_request.to_boto()
        )

        return shapes.DeleteScheduledActionResponse.from_boto(response)

    def deregister_scalable_target(
        self,
        _request: shapes.DeregisterScalableTargetRequest = None,
        *,
        service_namespace: typing.Union[str, shapes.ServiceNamespace],
        resource_id: str,
        scalable_dimension: typing.Union[str, shapes.ScalableDimension],
    ) -> shapes.DeregisterScalableTargetResponse:
        """
        Deregisters a scalable target.

        Deregistering a scalable target deletes the scaling policies that are associated
        with it.

        To create a scalable target or update an existing one, see
        RegisterScalableTarget.
        """
        if _request is None:
            _params = {}
            if service_namespace is not ShapeBase.NOT_SET:
                _params['service_namespace'] = service_namespace
            if resource_id is not ShapeBase.NOT_SET:
                _params['resource_id'] = resource_id
            if scalable_dimension is not ShapeBase.NOT_SET:
                _params['scalable_dimension'] = scalable_dimension
            _request = shapes.DeregisterScalableTargetRequest(**_params)
        response = self._boto_client.deregister_scalable_target(
            **_request.to_boto()
        )

        return shapes.DeregisterScalableTargetResponse.from_boto(response)

    def describe_scalable_targets(
        self,
        _request: shapes.DescribeScalableTargetsRequest = None,
        *,
        service_namespace: typing.Union[str, shapes.ServiceNamespace],
        resource_ids: typing.List[str] = ShapeBase.NOT_SET,
        scalable_dimension: typing.Union[str, shapes.
                                         ScalableDimension] = ShapeBase.NOT_SET,
        max_results: int = ShapeBase.NOT_SET,
        next_token: str = ShapeBase.NOT_SET,
    ) -> shapes.DescribeScalableTargetsResponse:
        """
        Gets information about the scalable targets in the specified namespace.

        You can filter the results using the `ResourceIds` and `ScalableDimension`
        parameters.

        To create a scalable target or update an existing one, see
        RegisterScalableTarget. If you are no longer using a scalable target, you can
        deregister it using DeregisterScalableTarget.
        """
        if _request is None:
            _params = {}
            if service_namespace is not ShapeBase.NOT_SET:
                _params['service_namespace'] = service_namespace
            if resource_ids is not ShapeBase.NOT_SET:
                _params['resource_ids'] = resource_ids
            if scalable_dimension is not ShapeBase.NOT_SET:
                _params['scalable_dimension'] = scalable_dimension
            if max_results is not ShapeBase.NOT_SET:
                _params['max_results'] = max_results
            if next_token is not ShapeBase.NOT_SET:
                _params['next_token'] = next_token
            _request = shapes.DescribeScalableTargetsRequest(**_params)
        paginator = self.get_paginator("describe_scalable_targets").paginate(
            **_request.to_boto()
        )
        page_generator = (page for page in paginator)
        first_page = next(page_generator)
        result = shapes.DescribeScalableTargetsResponse.from_boto(first_page)
        result._page_iterator = page_generator
        return result

        return shapes.DescribeScalableTargetsResponse.from_boto(response)

    def describe_scaling_activities(
        self,
        _request: shapes.DescribeScalingActivitiesRequest = None,
        *,
        service_namespace: typing.Union[str, shapes.ServiceNamespace],
        resource_id: str = ShapeBase.NOT_SET,
        scalable_dimension: typing.Union[str, shapes.
                                         ScalableDimension] = ShapeBase.NOT_SET,
        max_results: int = ShapeBase.NOT_SET,
        next_token: str = ShapeBase.NOT_SET,
    ) -> shapes.DescribeScalingActivitiesResponse:
        """
        Provides descriptive information about the scaling activities in the specified
        namespace from the previous six weeks.

        You can filter the results using the `ResourceId` and `ScalableDimension`
        parameters.

        Scaling activities are triggered by CloudWatch alarms that are associated with
        scaling policies. To view the scaling policies for a service namespace, see
        DescribeScalingPolicies. To create a scaling policy or update an existing one,
        see PutScalingPolicy.
        """
        if _request is None:
            _params = {}
            if service_namespace is not ShapeBase.NOT_SET:
                _params['service_namespace'] = service_namespace
            if resource_id is not ShapeBase.NOT_SET:
                _params['resource_id'] = resource_id
            if scalable_dimension is not ShapeBase.NOT_SET:
                _params['scalable_dimension'] = scalable_dimension
            if max_results is not ShapeBase.NOT_SET:
                _params['max_results'] = max_results
            if next_token is not ShapeBase.NOT_SET:
                _params['next_token'] = next_token
            _request = shapes.DescribeScalingActivitiesRequest(**_params)
        paginator = self.get_paginator("describe_scaling_activities").paginate(
            **_request.to_boto()
        )
        page_generator = (page for page in paginator)
        first_page = next(page_generator)
        result = shapes.DescribeScalingActivitiesResponse.from_boto(first_page)
        result._page_iterator = page_generator
        return result

        return shapes.DescribeScalingActivitiesResponse.from_boto(response)

    def describe_scaling_policies(
        self,
        _request: shapes.DescribeScalingPoliciesRequest = None,
        *,
        service_namespace: typing.Union[str, shapes.ServiceNamespace],
        policy_names: typing.List[str] = ShapeBase.NOT_SET,
        resource_id: str = ShapeBase.NOT_SET,
        scalable_dimension: typing.Union[str, shapes.
                                         ScalableDimension] = ShapeBase.NOT_SET,
        max_results: int = ShapeBase.NOT_SET,
        next_token: str = ShapeBase.NOT_SET,
    ) -> shapes.DescribeScalingPoliciesResponse:
        """
        Describes the scaling policies for the specified service namespace.

        You can filter the results using the `ResourceId`, `ScalableDimension`, and
        `PolicyNames` parameters.

        To create a scaling policy or update an existing one, see PutScalingPolicy. If
        you are no longer using a scaling policy, you can delete it using
        DeleteScalingPolicy.
        """
        if _request is None:
            _params = {}
            if service_namespace is not ShapeBase.NOT_SET:
                _params['service_namespace'] = service_namespace
            if policy_names is not ShapeBase.NOT_SET:
                _params['policy_names'] = policy_names
            if resource_id is not ShapeBase.NOT_SET:
                _params['resource_id'] = resource_id
            if scalable_dimension is not ShapeBase.NOT_SET:
                _params['scalable_dimension'] = scalable_dimension
            if max_results is not ShapeBase.NOT_SET:
                _params['max_results'] = max_results
            if next_token is not ShapeBase.NOT_SET:
                _params['next_token'] = next_token
            _request = shapes.DescribeScalingPoliciesRequest(**_params)
        paginator = self.get_paginator("describe_scaling_policies").paginate(
            **_request.to_boto()
        )
        page_generator = (page for page in paginator)
        first_page = next(page_generator)
        result = shapes.DescribeScalingPoliciesResponse.from_boto(first_page)
        result._page_iterator = page_generator
        return result

        return shapes.DescribeScalingPoliciesResponse.from_boto(response)

    def describe_scheduled_actions(
        self,
        _request: shapes.DescribeScheduledActionsRequest = None,
        *,
        service_namespace: typing.Union[str, shapes.ServiceNamespace],
        scheduled_action_names: typing.List[str] = ShapeBase.NOT_SET,
        resource_id: str = ShapeBase.NOT_SET,
        scalable_dimension: typing.Union[str, shapes.
                                         ScalableDimension] = ShapeBase.NOT_SET,
        max_results: int = ShapeBase.NOT_SET,
        next_token: str = ShapeBase.NOT_SET,
    ) -> shapes.DescribeScheduledActionsResponse:
        """
        Describes the scheduled actions for the specified service namespace.

        You can filter the results using the `ResourceId`, `ScalableDimension`, and
        `ScheduledActionNames` parameters.

        To create a scheduled action or update an existing one, see PutScheduledAction.
        If you are no longer using a scheduled action, you can delete it using
        DeleteScheduledAction.
        """
        if _request is None:
            _params = {}
            if service_namespace is not ShapeBase.NOT_SET:
                _params['service_namespace'] = service_namespace
            if scheduled_action_names is not ShapeBase.NOT_SET:
                _params['scheduled_action_names'] = scheduled_action_names
            if resource_id is not ShapeBase.NOT_SET:
                _params['resource_id'] = resource_id
            if scalable_dimension is not ShapeBase.NOT_SET:
                _params['scalable_dimension'] = scalable_dimension
            if max_results is not ShapeBase.NOT_SET:
                _params['max_results'] = max_results
            if next_token is not ShapeBase.NOT_SET:
                _params['next_token'] = next_token
            _request = shapes.DescribeScheduledActionsRequest(**_params)
        response = self._boto_client.describe_scheduled_actions(
            **_request.to_boto()
        )

        return shapes.DescribeScheduledActionsResponse.from_boto(response)

    def put_scaling_policy(
        self,
        _request: shapes.PutScalingPolicyRequest = None,
        *,
        policy_name: str,
        service_namespace: typing.Union[str, shapes.ServiceNamespace],
        resource_id: str,
        scalable_dimension: typing.Union[str, shapes.ScalableDimension],
        policy_type: typing.Union[str, shapes.PolicyType] = ShapeBase.NOT_SET,
        step_scaling_policy_configuration: shapes.
        StepScalingPolicyConfiguration = ShapeBase.NOT_SET,
        target_tracking_scaling_policy_configuration: shapes.
        TargetTrackingScalingPolicyConfiguration = ShapeBase.NOT_SET,
    ) -> shapes.PutScalingPolicyResponse:
        """
        Creates or updates a policy for an Application Auto Scaling scalable target.

        Each scalable target is identified by a service namespace, resource ID, and
        scalable dimension. A scaling policy applies to the scalable target identified
        by those three attributes. You cannot create a scaling policy until you register
        the scalable target using RegisterScalableTarget.

        To update a policy, specify its policy name and the parameters that you want to
        change. Any parameters that you don't specify are not changed by this update
        request.

        You can view the scaling policies for a service namespace using
        DescribeScalingPolicies. If you are no longer using a scaling policy, you can
        delete it using DeleteScalingPolicy.
        """
        if _request is None:
            _params = {}
            if policy_name is not ShapeBase.NOT_SET:
                _params['policy_name'] = policy_name
            if service_namespace is not ShapeBase.NOT_SET:
                _params['service_namespace'] = service_namespace
            if resource_id is not ShapeBase.NOT_SET:
                _params['resource_id'] = resource_id
            if scalable_dimension is not ShapeBase.NOT_SET:
                _params['scalable_dimension'] = scalable_dimension
            if policy_type is not ShapeBase.NOT_SET:
                _params['policy_type'] = policy_type
            if step_scaling_policy_configuration is not ShapeBase.NOT_SET:
                _params['step_scaling_policy_configuration'
                       ] = step_scaling_policy_configuration
            if target_tracking_scaling_policy_configuration is not ShapeBase.NOT_SET:
                _params['target_tracking_scaling_policy_configuration'
                       ] = target_tracking_scaling_policy_configuration
            _request = shapes.PutScalingPolicyRequest(**_params)
        response = self._boto_client.put_scaling_policy(**_request.to_boto())

        return shapes.PutScalingPolicyResponse.from_boto(response)

    def put_scheduled_action(
        self,
        _request: shapes.PutScheduledActionRequest = None,
        *,
        service_namespace: typing.Union[str, shapes.ServiceNamespace],
        scheduled_action_name: str,
        resource_id: str,
        schedule: str = ShapeBase.NOT_SET,
        scalable_dimension: typing.Union[str, shapes.
                                         ScalableDimension] = ShapeBase.NOT_SET,
        start_time: datetime.datetime = ShapeBase.NOT_SET,
        end_time: datetime.datetime = ShapeBase.NOT_SET,
        scalable_target_action: shapes.ScalableTargetAction = ShapeBase.NOT_SET,
    ) -> shapes.PutScheduledActionResponse:
        """
        Creates or updates a scheduled action for an Application Auto Scaling scalable
        target.

        Each scalable target is identified by a service namespace, resource ID, and
        scalable dimension. A scheduled action applies to the scalable target identified
        by those three attributes. You cannot create a scheduled action until you
        register the scalable target using RegisterScalableTarget.

        To update an action, specify its name and the parameters that you want to
        change. If you don't specify start and end times, the old values are deleted.
        Any other parameters that you don't specify are not changed by this update
        request.

        You can view the scheduled actions using DescribeScheduledActions. If you are no
        longer using a scheduled action, you can delete it using DeleteScheduledAction.
        """
        if _request is None:
            _params = {}
            if service_namespace is not ShapeBase.NOT_SET:
                _params['service_namespace'] = service_namespace
            if scheduled_action_name is not ShapeBase.NOT_SET:
                _params['scheduled_action_name'] = scheduled_action_name
            if resource_id is not ShapeBase.NOT_SET:
                _params['resource_id'] = resource_id
            if schedule is not ShapeBase.NOT_SET:
                _params['schedule'] = schedule
            if scalable_dimension is not ShapeBase.NOT_SET:
                _params['scalable_dimension'] = scalable_dimension
            if start_time is not ShapeBase.NOT_SET:
                _params['start_time'] = start_time
            if end_time is not ShapeBase.NOT_SET:
                _params['end_time'] = end_time
            if scalable_target_action is not ShapeBase.NOT_SET:
                _params['scalable_target_action'] = scalable_target_action
            _request = shapes.PutScheduledActionRequest(**_params)
        response = self._boto_client.put_scheduled_action(**_request.to_boto())

        return shapes.PutScheduledActionResponse.from_boto(response)

    def register_scalable_target(
        self,
        _request: shapes.RegisterScalableTargetRequest = None,
        *,
        service_namespace: typing.Union[str, shapes.ServiceNamespace],
        resource_id: str,
        scalable_dimension: typing.Union[str, shapes.ScalableDimension],
        min_capacity: int = ShapeBase.NOT_SET,
        max_capacity: int = ShapeBase.NOT_SET,
        role_arn: str = ShapeBase.NOT_SET,
    ) -> shapes.RegisterScalableTargetResponse:
        """
        Registers or updates a scalable target. A scalable target is a resource that
        Application Auto Scaling can scale out or scale in. After you have registered a
        scalable target, you can use this operation to update the minimum and maximum
        values for its scalable dimension.

        After you register a scalable target, you can create and apply scaling policies
        using PutScalingPolicy. You can view the scaling policies for a service
        namespace using DescribeScalableTargets. If you no longer need a scalable
        target, you can deregister it using DeregisterScalableTarget.
        """
        if _request is None:
            _params = {}
            if service_namespace is not ShapeBase.NOT_SET:
                _params['service_namespace'] = service_namespace
            if resource_id is not ShapeBase.NOT_SET:
                _params['resource_id'] = resource_id
            if scalable_dimension is not ShapeBase.NOT_SET:
                _params['scalable_dimension'] = scalable_dimension
            if min_capacity is not ShapeBase.NOT_SET:
                _params['min_capacity'] = min_capacity
            if max_capacity is not ShapeBase.NOT_SET:
                _params['max_capacity'] = max_capacity
            if role_arn is not ShapeBase.NOT_SET:
                _params['role_arn'] = role_arn
            _request = shapes.RegisterScalableTargetRequest(**_params)
        response = self._boto_client.register_scalable_target(
            **_request.to_boto()
        )

        return shapes.RegisterScalableTargetResponse.from_boto(response)
