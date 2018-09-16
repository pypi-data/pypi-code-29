import datetime
import typing
import boto3
from autoboto import ClientBase, ShapeBase, OutputShapeBase
from . import shapes


class Client(ClientBase):
    def __init__(self, *args, **kwargs):
        super().__init__("cloudformation", *args, **kwargs)

    def cancel_update_stack(
        self,
        _request: shapes.CancelUpdateStackInput = None,
        *,
        stack_name: str,
        client_request_token: str = ShapeBase.NOT_SET,
    ) -> None:
        """
        Cancels an update on the specified stack. If the call completes successfully,
        the stack rolls back the update and reverts to the previous stack configuration.

        You can cancel only stacks that are in the UPDATE_IN_PROGRESS state.
        """
        if _request is None:
            _params = {}
            if stack_name is not ShapeBase.NOT_SET:
                _params['stack_name'] = stack_name
            if client_request_token is not ShapeBase.NOT_SET:
                _params['client_request_token'] = client_request_token
            _request = shapes.CancelUpdateStackInput(**_params)
        response = self._boto_client.cancel_update_stack(**_request.to_boto())

    def continue_update_rollback(
        self,
        _request: shapes.ContinueUpdateRollbackInput = None,
        *,
        stack_name: str,
        role_arn: str = ShapeBase.NOT_SET,
        resources_to_skip: typing.List[str] = ShapeBase.NOT_SET,
        client_request_token: str = ShapeBase.NOT_SET,
    ) -> shapes.ContinueUpdateRollbackOutput:
        """
        For a specified stack that is in the `UPDATE_ROLLBACK_FAILED` state, continues
        rolling it back to the `UPDATE_ROLLBACK_COMPLETE` state. Depending on the cause
        of the failure, you can manually [ fix the
        error](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/troubleshooting.html#troubleshooting-
        errors-update-rollback-failed) and continue the rollback. By continuing the
        rollback, you can return your stack to a working state (the
        `UPDATE_ROLLBACK_COMPLETE` state), and then try to update the stack again.

        A stack goes into the `UPDATE_ROLLBACK_FAILED` state when AWS CloudFormation
        cannot roll back all changes after a failed stack update. For example, you might
        have a stack that is rolling back to an old database instance that was deleted
        outside of AWS CloudFormation. Because AWS CloudFormation doesn't know the
        database was deleted, it assumes that the database instance still exists and
        attempts to roll back to it, causing the update rollback to fail.
        """
        if _request is None:
            _params = {}
            if stack_name is not ShapeBase.NOT_SET:
                _params['stack_name'] = stack_name
            if role_arn is not ShapeBase.NOT_SET:
                _params['role_arn'] = role_arn
            if resources_to_skip is not ShapeBase.NOT_SET:
                _params['resources_to_skip'] = resources_to_skip
            if client_request_token is not ShapeBase.NOT_SET:
                _params['client_request_token'] = client_request_token
            _request = shapes.ContinueUpdateRollbackInput(**_params)
        response = self._boto_client.continue_update_rollback(
            **_request.to_boto()
        )

        return shapes.ContinueUpdateRollbackOutput.from_boto(response)

    def create_change_set(
        self,
        _request: shapes.CreateChangeSetInput = None,
        *,
        stack_name: str,
        change_set_name: str,
        template_body: str = ShapeBase.NOT_SET,
        template_url: str = ShapeBase.NOT_SET,
        use_previous_template: bool = ShapeBase.NOT_SET,
        parameters: typing.List[shapes.Parameter] = ShapeBase.NOT_SET,
        capabilities: typing.List[typing.Union[str, shapes.Capability]
                                 ] = ShapeBase.NOT_SET,
        resource_types: typing.List[str] = ShapeBase.NOT_SET,
        role_arn: str = ShapeBase.NOT_SET,
        rollback_configuration: shapes.RollbackConfiguration = ShapeBase.
        NOT_SET,
        notification_arns: typing.List[str] = ShapeBase.NOT_SET,
        tags: typing.List[shapes.Tag] = ShapeBase.NOT_SET,
        client_token: str = ShapeBase.NOT_SET,
        description: str = ShapeBase.NOT_SET,
        change_set_type: typing.Union[str, shapes.
                                      ChangeSetType] = ShapeBase.NOT_SET,
    ) -> shapes.CreateChangeSetOutput:
        """
        Creates a list of changes that will be applied to a stack so that you can review
        the changes before executing them. You can create a change set for a stack that
        doesn't exist or an existing stack. If you create a change set for a stack that
        doesn't exist, the change set shows all of the resources that AWS CloudFormation
        will create. If you create a change set for an existing stack, AWS
        CloudFormation compares the stack's information with the information that you
        submit in the change set and lists the differences. Use change sets to
        understand which resources AWS CloudFormation will create or change, and how it
        will change resources in an existing stack, before you create or update a stack.

        To create a change set for a stack that doesn't exist, for the `ChangeSetType`
        parameter, specify `CREATE`. To create a change set for an existing stack,
        specify `UPDATE` for the `ChangeSetType` parameter. After the `CreateChangeSet`
        call successfully completes, AWS CloudFormation starts creating the change set.
        To check the status of the change set or to review it, use the DescribeChangeSet
        action.

        When you are satisfied with the changes the change set will make, execute the
        change set by using the ExecuteChangeSet action. AWS CloudFormation doesn't make
        changes until you execute the change set.
        """
        if _request is None:
            _params = {}
            if stack_name is not ShapeBase.NOT_SET:
                _params['stack_name'] = stack_name
            if change_set_name is not ShapeBase.NOT_SET:
                _params['change_set_name'] = change_set_name
            if template_body is not ShapeBase.NOT_SET:
                _params['template_body'] = template_body
            if template_url is not ShapeBase.NOT_SET:
                _params['template_url'] = template_url
            if use_previous_template is not ShapeBase.NOT_SET:
                _params['use_previous_template'] = use_previous_template
            if parameters is not ShapeBase.NOT_SET:
                _params['parameters'] = parameters
            if capabilities is not ShapeBase.NOT_SET:
                _params['capabilities'] = capabilities
            if resource_types is not ShapeBase.NOT_SET:
                _params['resource_types'] = resource_types
            if role_arn is not ShapeBase.NOT_SET:
                _params['role_arn'] = role_arn
            if rollback_configuration is not ShapeBase.NOT_SET:
                _params['rollback_configuration'] = rollback_configuration
            if notification_arns is not ShapeBase.NOT_SET:
                _params['notification_arns'] = notification_arns
            if tags is not ShapeBase.NOT_SET:
                _params['tags'] = tags
            if client_token is not ShapeBase.NOT_SET:
                _params['client_token'] = client_token
            if description is not ShapeBase.NOT_SET:
                _params['description'] = description
            if change_set_type is not ShapeBase.NOT_SET:
                _params['change_set_type'] = change_set_type
            _request = shapes.CreateChangeSetInput(**_params)
        response = self._boto_client.create_change_set(**_request.to_boto())

        return shapes.CreateChangeSetOutput.from_boto(response)

    def create_stack(
        self,
        _request: shapes.CreateStackInput = None,
        *,
        stack_name: str,
        template_body: str = ShapeBase.NOT_SET,
        template_url: str = ShapeBase.NOT_SET,
        parameters: typing.List[shapes.Parameter] = ShapeBase.NOT_SET,
        disable_rollback: bool = ShapeBase.NOT_SET,
        rollback_configuration: shapes.RollbackConfiguration = ShapeBase.
        NOT_SET,
        timeout_in_minutes: int = ShapeBase.NOT_SET,
        notification_arns: typing.List[str] = ShapeBase.NOT_SET,
        capabilities: typing.List[typing.Union[str, shapes.Capability]
                                 ] = ShapeBase.NOT_SET,
        resource_types: typing.List[str] = ShapeBase.NOT_SET,
        role_arn: str = ShapeBase.NOT_SET,
        on_failure: typing.Union[str, shapes.OnFailure] = ShapeBase.NOT_SET,
        stack_policy_body: str = ShapeBase.NOT_SET,
        stack_policy_url: str = ShapeBase.NOT_SET,
        tags: typing.List[shapes.Tag] = ShapeBase.NOT_SET,
        client_request_token: str = ShapeBase.NOT_SET,
        enable_termination_protection: bool = ShapeBase.NOT_SET,
    ) -> shapes.CreateStackOutput:
        """
        Creates a stack as specified in the template. After the call completes
        successfully, the stack creation starts. You can check the status of the stack
        via the DescribeStacks API.
        """
        if _request is None:
            _params = {}
            if stack_name is not ShapeBase.NOT_SET:
                _params['stack_name'] = stack_name
            if template_body is not ShapeBase.NOT_SET:
                _params['template_body'] = template_body
            if template_url is not ShapeBase.NOT_SET:
                _params['template_url'] = template_url
            if parameters is not ShapeBase.NOT_SET:
                _params['parameters'] = parameters
            if disable_rollback is not ShapeBase.NOT_SET:
                _params['disable_rollback'] = disable_rollback
            if rollback_configuration is not ShapeBase.NOT_SET:
                _params['rollback_configuration'] = rollback_configuration
            if timeout_in_minutes is not ShapeBase.NOT_SET:
                _params['timeout_in_minutes'] = timeout_in_minutes
            if notification_arns is not ShapeBase.NOT_SET:
                _params['notification_arns'] = notification_arns
            if capabilities is not ShapeBase.NOT_SET:
                _params['capabilities'] = capabilities
            if resource_types is not ShapeBase.NOT_SET:
                _params['resource_types'] = resource_types
            if role_arn is not ShapeBase.NOT_SET:
                _params['role_arn'] = role_arn
            if on_failure is not ShapeBase.NOT_SET:
                _params['on_failure'] = on_failure
            if stack_policy_body is not ShapeBase.NOT_SET:
                _params['stack_policy_body'] = stack_policy_body
            if stack_policy_url is not ShapeBase.NOT_SET:
                _params['stack_policy_url'] = stack_policy_url
            if tags is not ShapeBase.NOT_SET:
                _params['tags'] = tags
            if client_request_token is not ShapeBase.NOT_SET:
                _params['client_request_token'] = client_request_token
            if enable_termination_protection is not ShapeBase.NOT_SET:
                _params['enable_termination_protection'
                       ] = enable_termination_protection
            _request = shapes.CreateStackInput(**_params)
        response = self._boto_client.create_stack(**_request.to_boto())

        return shapes.CreateStackOutput.from_boto(response)

    def create_stack_instances(
        self,
        _request: shapes.CreateStackInstancesInput = None,
        *,
        stack_set_name: str,
        accounts: typing.List[str],
        regions: typing.List[str],
        parameter_overrides: typing.List[shapes.Parameter] = ShapeBase.NOT_SET,
        operation_preferences: shapes.StackSetOperationPreferences = ShapeBase.
        NOT_SET,
        operation_id: str = ShapeBase.NOT_SET,
    ) -> shapes.CreateStackInstancesOutput:
        """
        Creates stack instances for the specified accounts, within the specified
        regions. A stack instance refers to a stack in a specific account and region.
        `Accounts` and `Regions` are required parameters—you must specify at least one
        account and one region.
        """
        if _request is None:
            _params = {}
            if stack_set_name is not ShapeBase.NOT_SET:
                _params['stack_set_name'] = stack_set_name
            if accounts is not ShapeBase.NOT_SET:
                _params['accounts'] = accounts
            if regions is not ShapeBase.NOT_SET:
                _params['regions'] = regions
            if parameter_overrides is not ShapeBase.NOT_SET:
                _params['parameter_overrides'] = parameter_overrides
            if operation_preferences is not ShapeBase.NOT_SET:
                _params['operation_preferences'] = operation_preferences
            if operation_id is not ShapeBase.NOT_SET:
                _params['operation_id'] = operation_id
            _request = shapes.CreateStackInstancesInput(**_params)
        response = self._boto_client.create_stack_instances(
            **_request.to_boto()
        )

        return shapes.CreateStackInstancesOutput.from_boto(response)

    def create_stack_set(
        self,
        _request: shapes.CreateStackSetInput = None,
        *,
        stack_set_name: str,
        description: str = ShapeBase.NOT_SET,
        template_body: str = ShapeBase.NOT_SET,
        template_url: str = ShapeBase.NOT_SET,
        parameters: typing.List[shapes.Parameter] = ShapeBase.NOT_SET,
        capabilities: typing.List[typing.Union[str, shapes.Capability]
                                 ] = ShapeBase.NOT_SET,
        tags: typing.List[shapes.Tag] = ShapeBase.NOT_SET,
        administration_role_arn: str = ShapeBase.NOT_SET,
        execution_role_name: str = ShapeBase.NOT_SET,
        client_request_token: str = ShapeBase.NOT_SET,
    ) -> shapes.CreateStackSetOutput:
        """
        Creates a stack set.
        """
        if _request is None:
            _params = {}
            if stack_set_name is not ShapeBase.NOT_SET:
                _params['stack_set_name'] = stack_set_name
            if description is not ShapeBase.NOT_SET:
                _params['description'] = description
            if template_body is not ShapeBase.NOT_SET:
                _params['template_body'] = template_body
            if template_url is not ShapeBase.NOT_SET:
                _params['template_url'] = template_url
            if parameters is not ShapeBase.NOT_SET:
                _params['parameters'] = parameters
            if capabilities is not ShapeBase.NOT_SET:
                _params['capabilities'] = capabilities
            if tags is not ShapeBase.NOT_SET:
                _params['tags'] = tags
            if administration_role_arn is not ShapeBase.NOT_SET:
                _params['administration_role_arn'] = administration_role_arn
            if execution_role_name is not ShapeBase.NOT_SET:
                _params['execution_role_name'] = execution_role_name
            if client_request_token is not ShapeBase.NOT_SET:
                _params['client_request_token'] = client_request_token
            _request = shapes.CreateStackSetInput(**_params)
        response = self._boto_client.create_stack_set(**_request.to_boto())

        return shapes.CreateStackSetOutput.from_boto(response)

    def delete_change_set(
        self,
        _request: shapes.DeleteChangeSetInput = None,
        *,
        change_set_name: str,
        stack_name: str = ShapeBase.NOT_SET,
    ) -> shapes.DeleteChangeSetOutput:
        """
        Deletes the specified change set. Deleting change sets ensures that no one
        executes the wrong change set.

        If the call successfully completes, AWS CloudFormation successfully deleted the
        change set.
        """
        if _request is None:
            _params = {}
            if change_set_name is not ShapeBase.NOT_SET:
                _params['change_set_name'] = change_set_name
            if stack_name is not ShapeBase.NOT_SET:
                _params['stack_name'] = stack_name
            _request = shapes.DeleteChangeSetInput(**_params)
        response = self._boto_client.delete_change_set(**_request.to_boto())

        return shapes.DeleteChangeSetOutput.from_boto(response)

    def delete_stack(
        self,
        _request: shapes.DeleteStackInput = None,
        *,
        stack_name: str,
        retain_resources: typing.List[str] = ShapeBase.NOT_SET,
        role_arn: str = ShapeBase.NOT_SET,
        client_request_token: str = ShapeBase.NOT_SET,
    ) -> None:
        """
        Deletes a specified stack. Once the call completes successfully, stack deletion
        starts. Deleted stacks do not show up in the DescribeStacks API if the deletion
        has been completed successfully.
        """
        if _request is None:
            _params = {}
            if stack_name is not ShapeBase.NOT_SET:
                _params['stack_name'] = stack_name
            if retain_resources is not ShapeBase.NOT_SET:
                _params['retain_resources'] = retain_resources
            if role_arn is not ShapeBase.NOT_SET:
                _params['role_arn'] = role_arn
            if client_request_token is not ShapeBase.NOT_SET:
                _params['client_request_token'] = client_request_token
            _request = shapes.DeleteStackInput(**_params)
        response = self._boto_client.delete_stack(**_request.to_boto())

    def delete_stack_instances(
        self,
        _request: shapes.DeleteStackInstancesInput = None,
        *,
        stack_set_name: str,
        accounts: typing.List[str],
        regions: typing.List[str],
        retain_stacks: bool,
        operation_preferences: shapes.StackSetOperationPreferences = ShapeBase.
        NOT_SET,
        operation_id: str = ShapeBase.NOT_SET,
    ) -> shapes.DeleteStackInstancesOutput:
        """
        Deletes stack instances for the specified accounts, in the specified regions.
        """
        if _request is None:
            _params = {}
            if stack_set_name is not ShapeBase.NOT_SET:
                _params['stack_set_name'] = stack_set_name
            if accounts is not ShapeBase.NOT_SET:
                _params['accounts'] = accounts
            if regions is not ShapeBase.NOT_SET:
                _params['regions'] = regions
            if retain_stacks is not ShapeBase.NOT_SET:
                _params['retain_stacks'] = retain_stacks
            if operation_preferences is not ShapeBase.NOT_SET:
                _params['operation_preferences'] = operation_preferences
            if operation_id is not ShapeBase.NOT_SET:
                _params['operation_id'] = operation_id
            _request = shapes.DeleteStackInstancesInput(**_params)
        response = self._boto_client.delete_stack_instances(
            **_request.to_boto()
        )

        return shapes.DeleteStackInstancesOutput.from_boto(response)

    def delete_stack_set(
        self,
        _request: shapes.DeleteStackSetInput = None,
        *,
        stack_set_name: str,
    ) -> shapes.DeleteStackSetOutput:
        """
        Deletes a stack set. Before you can delete a stack set, all of its member stack
        instances must be deleted. For more information about how to do this, see
        DeleteStackInstances.
        """
        if _request is None:
            _params = {}
            if stack_set_name is not ShapeBase.NOT_SET:
                _params['stack_set_name'] = stack_set_name
            _request = shapes.DeleteStackSetInput(**_params)
        response = self._boto_client.delete_stack_set(**_request.to_boto())

        return shapes.DeleteStackSetOutput.from_boto(response)

    def describe_account_limits(
        self,
        _request: shapes.DescribeAccountLimitsInput = None,
        *,
        next_token: str = ShapeBase.NOT_SET,
    ) -> shapes.DescribeAccountLimitsOutput:
        """
        Retrieves your account's AWS CloudFormation limits, such as the maximum number
        of stacks that you can create in your account.
        """
        if _request is None:
            _params = {}
            if next_token is not ShapeBase.NOT_SET:
                _params['next_token'] = next_token
            _request = shapes.DescribeAccountLimitsInput(**_params)
        response = self._boto_client.describe_account_limits(
            **_request.to_boto()
        )

        return shapes.DescribeAccountLimitsOutput.from_boto(response)

    def describe_change_set(
        self,
        _request: shapes.DescribeChangeSetInput = None,
        *,
        change_set_name: str,
        stack_name: str = ShapeBase.NOT_SET,
        next_token: str = ShapeBase.NOT_SET,
    ) -> shapes.DescribeChangeSetOutput:
        """
        Returns the inputs for the change set and a list of changes that AWS
        CloudFormation will make if you execute the change set. For more information,
        see [Updating Stacks Using Change
        Sets](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-
        updating-stacks-changesets.html) in the AWS CloudFormation User Guide.
        """
        if _request is None:
            _params = {}
            if change_set_name is not ShapeBase.NOT_SET:
                _params['change_set_name'] = change_set_name
            if stack_name is not ShapeBase.NOT_SET:
                _params['stack_name'] = stack_name
            if next_token is not ShapeBase.NOT_SET:
                _params['next_token'] = next_token
            _request = shapes.DescribeChangeSetInput(**_params)
        response = self._boto_client.describe_change_set(**_request.to_boto())

        return shapes.DescribeChangeSetOutput.from_boto(response)

    def describe_stack_events(
        self,
        _request: shapes.DescribeStackEventsInput = None,
        *,
        stack_name: str = ShapeBase.NOT_SET,
        next_token: str = ShapeBase.NOT_SET,
    ) -> shapes.DescribeStackEventsOutput:
        """
        Returns all stack related events for a specified stack in reverse chronological
        order. For more information about a stack's event history, go to
        [Stacks](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/concept-
        stack.html) in the AWS CloudFormation User Guide.

        You can list events for stacks that have failed to create or have been deleted
        by specifying the unique stack identifier (stack ID).
        """
        if _request is None:
            _params = {}
            if stack_name is not ShapeBase.NOT_SET:
                _params['stack_name'] = stack_name
            if next_token is not ShapeBase.NOT_SET:
                _params['next_token'] = next_token
            _request = shapes.DescribeStackEventsInput(**_params)
        paginator = self.get_paginator("describe_stack_events").paginate(
            **_request.to_boto()
        )
        page_generator = (page for page in paginator)
        first_page = next(page_generator)
        result = shapes.DescribeStackEventsOutput.from_boto(first_page)
        result._page_iterator = page_generator
        return result

        return shapes.DescribeStackEventsOutput.from_boto(response)

    def describe_stack_instance(
        self,
        _request: shapes.DescribeStackInstanceInput = None,
        *,
        stack_set_name: str,
        stack_instance_account: str,
        stack_instance_region: str,
    ) -> shapes.DescribeStackInstanceOutput:
        """
        Returns the stack instance that's associated with the specified stack set, AWS
        account, and region.

        For a list of stack instances that are associated with a specific stack set, use
        ListStackInstances.
        """
        if _request is None:
            _params = {}
            if stack_set_name is not ShapeBase.NOT_SET:
                _params['stack_set_name'] = stack_set_name
            if stack_instance_account is not ShapeBase.NOT_SET:
                _params['stack_instance_account'] = stack_instance_account
            if stack_instance_region is not ShapeBase.NOT_SET:
                _params['stack_instance_region'] = stack_instance_region
            _request = shapes.DescribeStackInstanceInput(**_params)
        response = self._boto_client.describe_stack_instance(
            **_request.to_boto()
        )

        return shapes.DescribeStackInstanceOutput.from_boto(response)

    def describe_stack_resource(
        self,
        _request: shapes.DescribeStackResourceInput = None,
        *,
        stack_name: str,
        logical_resource_id: str,
    ) -> shapes.DescribeStackResourceOutput:
        """
        Returns a description of the specified resource in the specified stack.

        For deleted stacks, DescribeStackResource returns resource information for up to
        90 days after the stack has been deleted.
        """
        if _request is None:
            _params = {}
            if stack_name is not ShapeBase.NOT_SET:
                _params['stack_name'] = stack_name
            if logical_resource_id is not ShapeBase.NOT_SET:
                _params['logical_resource_id'] = logical_resource_id
            _request = shapes.DescribeStackResourceInput(**_params)
        response = self._boto_client.describe_stack_resource(
            **_request.to_boto()
        )

        return shapes.DescribeStackResourceOutput.from_boto(response)

    def describe_stack_resources(
        self,
        _request: shapes.DescribeStackResourcesInput = None,
        *,
        stack_name: str = ShapeBase.NOT_SET,
        logical_resource_id: str = ShapeBase.NOT_SET,
        physical_resource_id: str = ShapeBase.NOT_SET,
    ) -> shapes.DescribeStackResourcesOutput:
        """
        Returns AWS resource descriptions for running and deleted stacks. If `StackName`
        is specified, all the associated resources that are part of the stack are
        returned. If `PhysicalResourceId` is specified, the associated resources of the
        stack that the resource belongs to are returned.

        Only the first 100 resources will be returned. If your stack has more resources
        than this, you should use `ListStackResources` instead.

        For deleted stacks, `DescribeStackResources` returns resource information for up
        to 90 days after the stack has been deleted.

        You must specify either `StackName` or `PhysicalResourceId`, but not both. In
        addition, you can specify `LogicalResourceId` to filter the returned result. For
        more information about resources, the `LogicalResourceId` and
        `PhysicalResourceId`, go to the [AWS CloudFormation User
        Guide](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/).

        A `ValidationError` is returned if you specify both `StackName` and
        `PhysicalResourceId` in the same request.
        """
        if _request is None:
            _params = {}
            if stack_name is not ShapeBase.NOT_SET:
                _params['stack_name'] = stack_name
            if logical_resource_id is not ShapeBase.NOT_SET:
                _params['logical_resource_id'] = logical_resource_id
            if physical_resource_id is not ShapeBase.NOT_SET:
                _params['physical_resource_id'] = physical_resource_id
            _request = shapes.DescribeStackResourcesInput(**_params)
        response = self._boto_client.describe_stack_resources(
            **_request.to_boto()
        )

        return shapes.DescribeStackResourcesOutput.from_boto(response)

    def describe_stack_set(
        self,
        _request: shapes.DescribeStackSetInput = None,
        *,
        stack_set_name: str,
    ) -> shapes.DescribeStackSetOutput:
        """
        Returns the description of the specified stack set.
        """
        if _request is None:
            _params = {}
            if stack_set_name is not ShapeBase.NOT_SET:
                _params['stack_set_name'] = stack_set_name
            _request = shapes.DescribeStackSetInput(**_params)
        response = self._boto_client.describe_stack_set(**_request.to_boto())

        return shapes.DescribeStackSetOutput.from_boto(response)

    def describe_stack_set_operation(
        self,
        _request: shapes.DescribeStackSetOperationInput = None,
        *,
        stack_set_name: str,
        operation_id: str,
    ) -> shapes.DescribeStackSetOperationOutput:
        """
        Returns the description of the specified stack set operation.
        """
        if _request is None:
            _params = {}
            if stack_set_name is not ShapeBase.NOT_SET:
                _params['stack_set_name'] = stack_set_name
            if operation_id is not ShapeBase.NOT_SET:
                _params['operation_id'] = operation_id
            _request = shapes.DescribeStackSetOperationInput(**_params)
        response = self._boto_client.describe_stack_set_operation(
            **_request.to_boto()
        )

        return shapes.DescribeStackSetOperationOutput.from_boto(response)

    def describe_stacks(
        self,
        _request: shapes.DescribeStacksInput = None,
        *,
        stack_name: str = ShapeBase.NOT_SET,
        next_token: str = ShapeBase.NOT_SET,
    ) -> shapes.DescribeStacksOutput:
        """
        Returns the description for the specified stack; if no stack name was specified,
        then it returns the description for all the stacks created.

        If the stack does not exist, an `AmazonCloudFormationException` is returned.
        """
        if _request is None:
            _params = {}
            if stack_name is not ShapeBase.NOT_SET:
                _params['stack_name'] = stack_name
            if next_token is not ShapeBase.NOT_SET:
                _params['next_token'] = next_token
            _request = shapes.DescribeStacksInput(**_params)
        paginator = self.get_paginator("describe_stacks").paginate(
            **_request.to_boto()
        )
        page_generator = (page for page in paginator)
        first_page = next(page_generator)
        result = shapes.DescribeStacksOutput.from_boto(first_page)
        result._page_iterator = page_generator
        return result

        return shapes.DescribeStacksOutput.from_boto(response)

    def estimate_template_cost(
        self,
        _request: shapes.EstimateTemplateCostInput = None,
        *,
        template_body: str = ShapeBase.NOT_SET,
        template_url: str = ShapeBase.NOT_SET,
        parameters: typing.List[shapes.Parameter] = ShapeBase.NOT_SET,
    ) -> shapes.EstimateTemplateCostOutput:
        """
        Returns the estimated monthly cost of a template. The return value is an AWS
        Simple Monthly Calculator URL with a query string that describes the resources
        required to run the template.
        """
        if _request is None:
            _params = {}
            if template_body is not ShapeBase.NOT_SET:
                _params['template_body'] = template_body
            if template_url is not ShapeBase.NOT_SET:
                _params['template_url'] = template_url
            if parameters is not ShapeBase.NOT_SET:
                _params['parameters'] = parameters
            _request = shapes.EstimateTemplateCostInput(**_params)
        response = self._boto_client.estimate_template_cost(
            **_request.to_boto()
        )

        return shapes.EstimateTemplateCostOutput.from_boto(response)

    def execute_change_set(
        self,
        _request: shapes.ExecuteChangeSetInput = None,
        *,
        change_set_name: str,
        stack_name: str = ShapeBase.NOT_SET,
        client_request_token: str = ShapeBase.NOT_SET,
    ) -> shapes.ExecuteChangeSetOutput:
        """
        Updates a stack using the input information that was provided when the specified
        change set was created. After the call successfully completes, AWS
        CloudFormation starts updating the stack. Use the DescribeStacks action to view
        the status of the update.

        When you execute a change set, AWS CloudFormation deletes all other change sets
        associated with the stack because they aren't valid for the updated stack.

        If a stack policy is associated with the stack, AWS CloudFormation enforces the
        policy during the update. You can't specify a temporary stack policy that
        overrides the current policy.
        """
        if _request is None:
            _params = {}
            if change_set_name is not ShapeBase.NOT_SET:
                _params['change_set_name'] = change_set_name
            if stack_name is not ShapeBase.NOT_SET:
                _params['stack_name'] = stack_name
            if client_request_token is not ShapeBase.NOT_SET:
                _params['client_request_token'] = client_request_token
            _request = shapes.ExecuteChangeSetInput(**_params)
        response = self._boto_client.execute_change_set(**_request.to_boto())

        return shapes.ExecuteChangeSetOutput.from_boto(response)

    def get_stack_policy(
        self,
        _request: shapes.GetStackPolicyInput = None,
        *,
        stack_name: str,
    ) -> shapes.GetStackPolicyOutput:
        """
        Returns the stack policy for a specified stack. If a stack doesn't have a
        policy, a null value is returned.
        """
        if _request is None:
            _params = {}
            if stack_name is not ShapeBase.NOT_SET:
                _params['stack_name'] = stack_name
            _request = shapes.GetStackPolicyInput(**_params)
        response = self._boto_client.get_stack_policy(**_request.to_boto())

        return shapes.GetStackPolicyOutput.from_boto(response)

    def get_template(
        self,
        _request: shapes.GetTemplateInput = None,
        *,
        stack_name: str = ShapeBase.NOT_SET,
        change_set_name: str = ShapeBase.NOT_SET,
        template_stage: typing.Union[str, shapes.TemplateStage] = ShapeBase.
        NOT_SET,
    ) -> shapes.GetTemplateOutput:
        """
        Returns the template body for a specified stack. You can get the template for
        running or deleted stacks.

        For deleted stacks, GetTemplate returns the template for up to 90 days after the
        stack has been deleted.

        If the template does not exist, a `ValidationError` is returned.
        """
        if _request is None:
            _params = {}
            if stack_name is not ShapeBase.NOT_SET:
                _params['stack_name'] = stack_name
            if change_set_name is not ShapeBase.NOT_SET:
                _params['change_set_name'] = change_set_name
            if template_stage is not ShapeBase.NOT_SET:
                _params['template_stage'] = template_stage
            _request = shapes.GetTemplateInput(**_params)
        response = self._boto_client.get_template(**_request.to_boto())

        return shapes.GetTemplateOutput.from_boto(response)

    def get_template_summary(
        self,
        _request: shapes.GetTemplateSummaryInput = None,
        *,
        template_body: str = ShapeBase.NOT_SET,
        template_url: str = ShapeBase.NOT_SET,
        stack_name: str = ShapeBase.NOT_SET,
        stack_set_name: str = ShapeBase.NOT_SET,
    ) -> shapes.GetTemplateSummaryOutput:
        """
        Returns information about a new or existing template. The `GetTemplateSummary`
        action is useful for viewing parameter information, such as default parameter
        values and parameter types, before you create or update a stack or stack set.

        You can use the `GetTemplateSummary` action when you submit a template, or you
        can get template information for a stack set, or a running or deleted stack.

        For deleted stacks, `GetTemplateSummary` returns the template information for up
        to 90 days after the stack has been deleted. If the template does not exist, a
        `ValidationError` is returned.
        """
        if _request is None:
            _params = {}
            if template_body is not ShapeBase.NOT_SET:
                _params['template_body'] = template_body
            if template_url is not ShapeBase.NOT_SET:
                _params['template_url'] = template_url
            if stack_name is not ShapeBase.NOT_SET:
                _params['stack_name'] = stack_name
            if stack_set_name is not ShapeBase.NOT_SET:
                _params['stack_set_name'] = stack_set_name
            _request = shapes.GetTemplateSummaryInput(**_params)
        response = self._boto_client.get_template_summary(**_request.to_boto())

        return shapes.GetTemplateSummaryOutput.from_boto(response)

    def list_change_sets(
        self,
        _request: shapes.ListChangeSetsInput = None,
        *,
        stack_name: str,
        next_token: str = ShapeBase.NOT_SET,
    ) -> shapes.ListChangeSetsOutput:
        """
        Returns the ID and status of each active change set for a stack. For example,
        AWS CloudFormation lists change sets that are in the `CREATE_IN_PROGRESS` or
        `CREATE_PENDING` state.
        """
        if _request is None:
            _params = {}
            if stack_name is not ShapeBase.NOT_SET:
                _params['stack_name'] = stack_name
            if next_token is not ShapeBase.NOT_SET:
                _params['next_token'] = next_token
            _request = shapes.ListChangeSetsInput(**_params)
        response = self._boto_client.list_change_sets(**_request.to_boto())

        return shapes.ListChangeSetsOutput.from_boto(response)

    def list_exports(
        self,
        _request: shapes.ListExportsInput = None,
        *,
        next_token: str = ShapeBase.NOT_SET,
    ) -> shapes.ListExportsOutput:
        """
        Lists all exported output values in the account and region in which you call
        this action. Use this action to see the exported output values that you can
        import into other stacks. To import values, use the [ `Fn::ImportValue`
        ](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-
        function-reference-importvalue.html) function.

        For more information, see [ AWS CloudFormation Export Stack Output
        Values](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-
        stack-exports.html).
        """
        if _request is None:
            _params = {}
            if next_token is not ShapeBase.NOT_SET:
                _params['next_token'] = next_token
            _request = shapes.ListExportsInput(**_params)
        paginator = self.get_paginator("list_exports").paginate(
            **_request.to_boto()
        )
        page_generator = (page for page in paginator)
        first_page = next(page_generator)
        result = shapes.ListExportsOutput.from_boto(first_page)
        result._page_iterator = page_generator
        return result

        return shapes.ListExportsOutput.from_boto(response)

    def list_imports(
        self,
        _request: shapes.ListImportsInput = None,
        *,
        export_name: str,
        next_token: str = ShapeBase.NOT_SET,
    ) -> shapes.ListImportsOutput:
        """
        Lists all stacks that are importing an exported output value. To modify or
        remove an exported output value, first use this action to see which stacks are
        using it. To see the exported output values in your account, see ListExports.

        For more information about importing an exported output value, see the [
        `Fn::ImportValue`
        ](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-
        function-reference-importvalue.html) function.
        """
        if _request is None:
            _params = {}
            if export_name is not ShapeBase.NOT_SET:
                _params['export_name'] = export_name
            if next_token is not ShapeBase.NOT_SET:
                _params['next_token'] = next_token
            _request = shapes.ListImportsInput(**_params)
        paginator = self.get_paginator("list_imports").paginate(
            **_request.to_boto()
        )
        page_generator = (page for page in paginator)
        first_page = next(page_generator)
        result = shapes.ListImportsOutput.from_boto(first_page)
        result._page_iterator = page_generator
        return result

        return shapes.ListImportsOutput.from_boto(response)

    def list_stack_instances(
        self,
        _request: shapes.ListStackInstancesInput = None,
        *,
        stack_set_name: str,
        next_token: str = ShapeBase.NOT_SET,
        max_results: int = ShapeBase.NOT_SET,
        stack_instance_account: str = ShapeBase.NOT_SET,
        stack_instance_region: str = ShapeBase.NOT_SET,
    ) -> shapes.ListStackInstancesOutput:
        """
        Returns summary information about stack instances that are associated with the
        specified stack set. You can filter for stack instances that are associated with
        a specific AWS account name or region.
        """
        if _request is None:
            _params = {}
            if stack_set_name is not ShapeBase.NOT_SET:
                _params['stack_set_name'] = stack_set_name
            if next_token is not ShapeBase.NOT_SET:
                _params['next_token'] = next_token
            if max_results is not ShapeBase.NOT_SET:
                _params['max_results'] = max_results
            if stack_instance_account is not ShapeBase.NOT_SET:
                _params['stack_instance_account'] = stack_instance_account
            if stack_instance_region is not ShapeBase.NOT_SET:
                _params['stack_instance_region'] = stack_instance_region
            _request = shapes.ListStackInstancesInput(**_params)
        response = self._boto_client.list_stack_instances(**_request.to_boto())

        return shapes.ListStackInstancesOutput.from_boto(response)

    def list_stack_resources(
        self,
        _request: shapes.ListStackResourcesInput = None,
        *,
        stack_name: str,
        next_token: str = ShapeBase.NOT_SET,
    ) -> shapes.ListStackResourcesOutput:
        """
        Returns descriptions of all resources of the specified stack.

        For deleted stacks, ListStackResources returns resource information for up to 90
        days after the stack has been deleted.
        """
        if _request is None:
            _params = {}
            if stack_name is not ShapeBase.NOT_SET:
                _params['stack_name'] = stack_name
            if next_token is not ShapeBase.NOT_SET:
                _params['next_token'] = next_token
            _request = shapes.ListStackResourcesInput(**_params)
        paginator = self.get_paginator("list_stack_resources").paginate(
            **_request.to_boto()
        )
        page_generator = (page for page in paginator)
        first_page = next(page_generator)
        result = shapes.ListStackResourcesOutput.from_boto(first_page)
        result._page_iterator = page_generator
        return result

        return shapes.ListStackResourcesOutput.from_boto(response)

    def list_stack_set_operation_results(
        self,
        _request: shapes.ListStackSetOperationResultsInput = None,
        *,
        stack_set_name: str,
        operation_id: str,
        next_token: str = ShapeBase.NOT_SET,
        max_results: int = ShapeBase.NOT_SET,
    ) -> shapes.ListStackSetOperationResultsOutput:
        """
        Returns summary information about the results of a stack set operation.
        """
        if _request is None:
            _params = {}
            if stack_set_name is not ShapeBase.NOT_SET:
                _params['stack_set_name'] = stack_set_name
            if operation_id is not ShapeBase.NOT_SET:
                _params['operation_id'] = operation_id
            if next_token is not ShapeBase.NOT_SET:
                _params['next_token'] = next_token
            if max_results is not ShapeBase.NOT_SET:
                _params['max_results'] = max_results
            _request = shapes.ListStackSetOperationResultsInput(**_params)
        response = self._boto_client.list_stack_set_operation_results(
            **_request.to_boto()
        )

        return shapes.ListStackSetOperationResultsOutput.from_boto(response)

    def list_stack_set_operations(
        self,
        _request: shapes.ListStackSetOperationsInput = None,
        *,
        stack_set_name: str,
        next_token: str = ShapeBase.NOT_SET,
        max_results: int = ShapeBase.NOT_SET,
    ) -> shapes.ListStackSetOperationsOutput:
        """
        Returns summary information about operations performed on a stack set.
        """
        if _request is None:
            _params = {}
            if stack_set_name is not ShapeBase.NOT_SET:
                _params['stack_set_name'] = stack_set_name
            if next_token is not ShapeBase.NOT_SET:
                _params['next_token'] = next_token
            if max_results is not ShapeBase.NOT_SET:
                _params['max_results'] = max_results
            _request = shapes.ListStackSetOperationsInput(**_params)
        response = self._boto_client.list_stack_set_operations(
            **_request.to_boto()
        )

        return shapes.ListStackSetOperationsOutput.from_boto(response)

    def list_stack_sets(
        self,
        _request: shapes.ListStackSetsInput = None,
        *,
        next_token: str = ShapeBase.NOT_SET,
        max_results: int = ShapeBase.NOT_SET,
        status: typing.Union[str, shapes.StackSetStatus] = ShapeBase.NOT_SET,
    ) -> shapes.ListStackSetsOutput:
        """
        Returns summary information about stack sets that are associated with the user.
        """
        if _request is None:
            _params = {}
            if next_token is not ShapeBase.NOT_SET:
                _params['next_token'] = next_token
            if max_results is not ShapeBase.NOT_SET:
                _params['max_results'] = max_results
            if status is not ShapeBase.NOT_SET:
                _params['status'] = status
            _request = shapes.ListStackSetsInput(**_params)
        response = self._boto_client.list_stack_sets(**_request.to_boto())

        return shapes.ListStackSetsOutput.from_boto(response)

    def list_stacks(
        self,
        _request: shapes.ListStacksInput = None,
        *,
        next_token: str = ShapeBase.NOT_SET,
        stack_status_filter: typing.List[typing.Union[str, shapes.StackStatus]
                                        ] = ShapeBase.NOT_SET,
    ) -> shapes.ListStacksOutput:
        """
        Returns the summary information for stacks whose status matches the specified
        StackStatusFilter. Summary information for stacks that have been deleted is kept
        for 90 days after the stack is deleted. If no StackStatusFilter is specified,
        summary information for all stacks is returned (including existing stacks and
        stacks that have been deleted).
        """
        if _request is None:
            _params = {}
            if next_token is not ShapeBase.NOT_SET:
                _params['next_token'] = next_token
            if stack_status_filter is not ShapeBase.NOT_SET:
                _params['stack_status_filter'] = stack_status_filter
            _request = shapes.ListStacksInput(**_params)
        paginator = self.get_paginator("list_stacks").paginate(
            **_request.to_boto()
        )
        page_generator = (page for page in paginator)
        first_page = next(page_generator)
        result = shapes.ListStacksOutput.from_boto(first_page)
        result._page_iterator = page_generator
        return result

        return shapes.ListStacksOutput.from_boto(response)

    def set_stack_policy(
        self,
        _request: shapes.SetStackPolicyInput = None,
        *,
        stack_name: str,
        stack_policy_body: str = ShapeBase.NOT_SET,
        stack_policy_url: str = ShapeBase.NOT_SET,
    ) -> None:
        """
        Sets a stack policy for a specified stack.
        """
        if _request is None:
            _params = {}
            if stack_name is not ShapeBase.NOT_SET:
                _params['stack_name'] = stack_name
            if stack_policy_body is not ShapeBase.NOT_SET:
                _params['stack_policy_body'] = stack_policy_body
            if stack_policy_url is not ShapeBase.NOT_SET:
                _params['stack_policy_url'] = stack_policy_url
            _request = shapes.SetStackPolicyInput(**_params)
        response = self._boto_client.set_stack_policy(**_request.to_boto())

    def signal_resource(
        self,
        _request: shapes.SignalResourceInput = None,
        *,
        stack_name: str,
        logical_resource_id: str,
        unique_id: str,
        status: typing.Union[str, shapes.ResourceSignalStatus],
    ) -> None:
        """
        Sends a signal to the specified resource with a success or failure status. You
        can use the SignalResource API in conjunction with a creation policy or update
        policy. AWS CloudFormation doesn't proceed with a stack creation or update until
        resources receive the required number of signals or the timeout period is
        exceeded. The SignalResource API is useful in cases where you want to send
        signals from anywhere other than an Amazon EC2 instance.
        """
        if _request is None:
            _params = {}
            if stack_name is not ShapeBase.NOT_SET:
                _params['stack_name'] = stack_name
            if logical_resource_id is not ShapeBase.NOT_SET:
                _params['logical_resource_id'] = logical_resource_id
            if unique_id is not ShapeBase.NOT_SET:
                _params['unique_id'] = unique_id
            if status is not ShapeBase.NOT_SET:
                _params['status'] = status
            _request = shapes.SignalResourceInput(**_params)
        response = self._boto_client.signal_resource(**_request.to_boto())

    def stop_stack_set_operation(
        self,
        _request: shapes.StopStackSetOperationInput = None,
        *,
        stack_set_name: str,
        operation_id: str,
    ) -> shapes.StopStackSetOperationOutput:
        """
        Stops an in-progress operation on a stack set and its associated stack
        instances.
        """
        if _request is None:
            _params = {}
            if stack_set_name is not ShapeBase.NOT_SET:
                _params['stack_set_name'] = stack_set_name
            if operation_id is not ShapeBase.NOT_SET:
                _params['operation_id'] = operation_id
            _request = shapes.StopStackSetOperationInput(**_params)
        response = self._boto_client.stop_stack_set_operation(
            **_request.to_boto()
        )

        return shapes.StopStackSetOperationOutput.from_boto(response)

    def update_stack(
        self,
        _request: shapes.UpdateStackInput = None,
        *,
        stack_name: str,
        template_body: str = ShapeBase.NOT_SET,
        template_url: str = ShapeBase.NOT_SET,
        use_previous_template: bool = ShapeBase.NOT_SET,
        stack_policy_during_update_body: str = ShapeBase.NOT_SET,
        stack_policy_during_update_url: str = ShapeBase.NOT_SET,
        parameters: typing.List[shapes.Parameter] = ShapeBase.NOT_SET,
        capabilities: typing.List[typing.Union[str, shapes.Capability]
                                 ] = ShapeBase.NOT_SET,
        resource_types: typing.List[str] = ShapeBase.NOT_SET,
        role_arn: str = ShapeBase.NOT_SET,
        rollback_configuration: shapes.RollbackConfiguration = ShapeBase.
        NOT_SET,
        stack_policy_body: str = ShapeBase.NOT_SET,
        stack_policy_url: str = ShapeBase.NOT_SET,
        notification_arns: typing.List[str] = ShapeBase.NOT_SET,
        tags: typing.List[shapes.Tag] = ShapeBase.NOT_SET,
        client_request_token: str = ShapeBase.NOT_SET,
    ) -> shapes.UpdateStackOutput:
        """
        Updates a stack as specified in the template. After the call completes
        successfully, the stack update starts. You can check the status of the stack via
        the DescribeStacks action.

        To get a copy of the template for an existing stack, you can use the GetTemplate
        action.

        For more information about creating an update template, updating a stack, and
        monitoring the progress of the update, see [Updating a
        Stack](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-
        updating-stacks.html).
        """
        if _request is None:
            _params = {}
            if stack_name is not ShapeBase.NOT_SET:
                _params['stack_name'] = stack_name
            if template_body is not ShapeBase.NOT_SET:
                _params['template_body'] = template_body
            if template_url is not ShapeBase.NOT_SET:
                _params['template_url'] = template_url
            if use_previous_template is not ShapeBase.NOT_SET:
                _params['use_previous_template'] = use_previous_template
            if stack_policy_during_update_body is not ShapeBase.NOT_SET:
                _params['stack_policy_during_update_body'
                       ] = stack_policy_during_update_body
            if stack_policy_during_update_url is not ShapeBase.NOT_SET:
                _params['stack_policy_during_update_url'
                       ] = stack_policy_during_update_url
            if parameters is not ShapeBase.NOT_SET:
                _params['parameters'] = parameters
            if capabilities is not ShapeBase.NOT_SET:
                _params['capabilities'] = capabilities
            if resource_types is not ShapeBase.NOT_SET:
                _params['resource_types'] = resource_types
            if role_arn is not ShapeBase.NOT_SET:
                _params['role_arn'] = role_arn
            if rollback_configuration is not ShapeBase.NOT_SET:
                _params['rollback_configuration'] = rollback_configuration
            if stack_policy_body is not ShapeBase.NOT_SET:
                _params['stack_policy_body'] = stack_policy_body
            if stack_policy_url is not ShapeBase.NOT_SET:
                _params['stack_policy_url'] = stack_policy_url
            if notification_arns is not ShapeBase.NOT_SET:
                _params['notification_arns'] = notification_arns
            if tags is not ShapeBase.NOT_SET:
                _params['tags'] = tags
            if client_request_token is not ShapeBase.NOT_SET:
                _params['client_request_token'] = client_request_token
            _request = shapes.UpdateStackInput(**_params)
        response = self._boto_client.update_stack(**_request.to_boto())

        return shapes.UpdateStackOutput.from_boto(response)

    def update_stack_instances(
        self,
        _request: shapes.UpdateStackInstancesInput = None,
        *,
        stack_set_name: str,
        accounts: typing.List[str],
        regions: typing.List[str],
        parameter_overrides: typing.List[shapes.Parameter] = ShapeBase.NOT_SET,
        operation_preferences: shapes.StackSetOperationPreferences = ShapeBase.
        NOT_SET,
        operation_id: str = ShapeBase.NOT_SET,
    ) -> shapes.UpdateStackInstancesOutput:
        """
        Updates the parameter values for stack instances for the specified accounts,
        within the specified regions. A stack instance refers to a stack in a specific
        account and region.

        You can only update stack instances in regions and accounts where they already
        exist; to create additional stack instances, use
        [CreateStackInstances](http://docs.aws.amazon.com/AWSCloudFormation/latest/APIReference/API_CreateStackInstances.html).

        During stack set updates, any parameters overridden for a stack instance are not
        updated, but retain their overridden value.

        You can only update the parameter _values_ that are specified in the stack set;
        to add or delete a parameter itself, use
        [UpdateStackSet](http://docs.aws.amazon.com/AWSCloudFormation/latest/APIReference/API_UpdateStackSet.html)
        to update the stack set template. If you add a parameter to a template, before
        you can override the parameter value specified in the stack set you must first
        use
        [UpdateStackSet](http://docs.aws.amazon.com/AWSCloudFormation/latest/APIReference/API_UpdateStackSet.html)
        to update all stack instances with the updated template and parameter value
        specified in the stack set. Once a stack instance has been updated with the new
        parameter, you can then override the parameter value using
        `UpdateStackInstances`.
        """
        if _request is None:
            _params = {}
            if stack_set_name is not ShapeBase.NOT_SET:
                _params['stack_set_name'] = stack_set_name
            if accounts is not ShapeBase.NOT_SET:
                _params['accounts'] = accounts
            if regions is not ShapeBase.NOT_SET:
                _params['regions'] = regions
            if parameter_overrides is not ShapeBase.NOT_SET:
                _params['parameter_overrides'] = parameter_overrides
            if operation_preferences is not ShapeBase.NOT_SET:
                _params['operation_preferences'] = operation_preferences
            if operation_id is not ShapeBase.NOT_SET:
                _params['operation_id'] = operation_id
            _request = shapes.UpdateStackInstancesInput(**_params)
        response = self._boto_client.update_stack_instances(
            **_request.to_boto()
        )

        return shapes.UpdateStackInstancesOutput.from_boto(response)

    def update_stack_set(
        self,
        _request: shapes.UpdateStackSetInput = None,
        *,
        stack_set_name: str,
        description: str = ShapeBase.NOT_SET,
        template_body: str = ShapeBase.NOT_SET,
        template_url: str = ShapeBase.NOT_SET,
        use_previous_template: bool = ShapeBase.NOT_SET,
        parameters: typing.List[shapes.Parameter] = ShapeBase.NOT_SET,
        capabilities: typing.List[typing.Union[str, shapes.Capability]
                                 ] = ShapeBase.NOT_SET,
        tags: typing.List[shapes.Tag] = ShapeBase.NOT_SET,
        operation_preferences: shapes.StackSetOperationPreferences = ShapeBase.
        NOT_SET,
        administration_role_arn: str = ShapeBase.NOT_SET,
        execution_role_name: str = ShapeBase.NOT_SET,
        operation_id: str = ShapeBase.NOT_SET,
        accounts: typing.List[str] = ShapeBase.NOT_SET,
        regions: typing.List[str] = ShapeBase.NOT_SET,
    ) -> shapes.UpdateStackSetOutput:
        """
        Updates the stack set, and associated stack instances in the specified accounts
        and regions.

        Even if the stack set operation created by updating the stack set fails
        (completely or partially, below or above a specified failure tolerance), the
        stack set is updated with your changes. Subsequent CreateStackInstances calls on
        the specified stack set use the updated stack set.
        """
        if _request is None:
            _params = {}
            if stack_set_name is not ShapeBase.NOT_SET:
                _params['stack_set_name'] = stack_set_name
            if description is not ShapeBase.NOT_SET:
                _params['description'] = description
            if template_body is not ShapeBase.NOT_SET:
                _params['template_body'] = template_body
            if template_url is not ShapeBase.NOT_SET:
                _params['template_url'] = template_url
            if use_previous_template is not ShapeBase.NOT_SET:
                _params['use_previous_template'] = use_previous_template
            if parameters is not ShapeBase.NOT_SET:
                _params['parameters'] = parameters
            if capabilities is not ShapeBase.NOT_SET:
                _params['capabilities'] = capabilities
            if tags is not ShapeBase.NOT_SET:
                _params['tags'] = tags
            if operation_preferences is not ShapeBase.NOT_SET:
                _params['operation_preferences'] = operation_preferences
            if administration_role_arn is not ShapeBase.NOT_SET:
                _params['administration_role_arn'] = administration_role_arn
            if execution_role_name is not ShapeBase.NOT_SET:
                _params['execution_role_name'] = execution_role_name
            if operation_id is not ShapeBase.NOT_SET:
                _params['operation_id'] = operation_id
            if accounts is not ShapeBase.NOT_SET:
                _params['accounts'] = accounts
            if regions is not ShapeBase.NOT_SET:
                _params['regions'] = regions
            _request = shapes.UpdateStackSetInput(**_params)
        response = self._boto_client.update_stack_set(**_request.to_boto())

        return shapes.UpdateStackSetOutput.from_boto(response)

    def update_termination_protection(
        self,
        _request: shapes.UpdateTerminationProtectionInput = None,
        *,
        enable_termination_protection: bool,
        stack_name: str,
    ) -> shapes.UpdateTerminationProtectionOutput:
        """
        Updates termination protection for the specified stack. If a user attempts to
        delete a stack with termination protection enabled, the operation fails and the
        stack remains unchanged. For more information, see [Protecting a Stack From
        Being
        Deleted](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-
        cfn-protect-stacks.html) in the _AWS CloudFormation User Guide_.

        For [nested
        stacks](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-
        nested-stacks.html), termination protection is set on the root stack and cannot
        be changed directly on the nested stack.
        """
        if _request is None:
            _params = {}
            if enable_termination_protection is not ShapeBase.NOT_SET:
                _params['enable_termination_protection'
                       ] = enable_termination_protection
            if stack_name is not ShapeBase.NOT_SET:
                _params['stack_name'] = stack_name
            _request = shapes.UpdateTerminationProtectionInput(**_params)
        response = self._boto_client.update_termination_protection(
            **_request.to_boto()
        )

        return shapes.UpdateTerminationProtectionOutput.from_boto(response)

    def validate_template(
        self,
        _request: shapes.ValidateTemplateInput = None,
        *,
        template_body: str = ShapeBase.NOT_SET,
        template_url: str = ShapeBase.NOT_SET,
    ) -> shapes.ValidateTemplateOutput:
        """
        Validates a specified template. AWS CloudFormation first checks if the template
        is valid JSON. If it isn't, AWS CloudFormation checks if the template is valid
        YAML. If both these checks fail, AWS CloudFormation returns a template
        validation error.
        """
        if _request is None:
            _params = {}
            if template_body is not ShapeBase.NOT_SET:
                _params['template_body'] = template_body
            if template_url is not ShapeBase.NOT_SET:
                _params['template_url'] = template_url
            _request = shapes.ValidateTemplateInput(**_params)
        response = self._boto_client.validate_template(**_request.to_boto())

        return shapes.ValidateTemplateOutput.from_boto(response)
