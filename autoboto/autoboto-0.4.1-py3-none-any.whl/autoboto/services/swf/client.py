import datetime
import typing
import boto3
from autoboto import ClientBase, ShapeBase, OutputShapeBase
from . import shapes


class Client(ClientBase):
    def __init__(self, *args, **kwargs):
        super().__init__("swf", *args, **kwargs)

    def count_closed_workflow_executions(
        self,
        _request: shapes.CountClosedWorkflowExecutionsInput = None,
        *,
        domain: str,
        start_time_filter: shapes.ExecutionTimeFilter = ShapeBase.NOT_SET,
        close_time_filter: shapes.ExecutionTimeFilter = ShapeBase.NOT_SET,
        execution_filter: shapes.WorkflowExecutionFilter = ShapeBase.NOT_SET,
        type_filter: shapes.WorkflowTypeFilter = ShapeBase.NOT_SET,
        tag_filter: shapes.TagFilter = ShapeBase.NOT_SET,
        close_status_filter: shapes.CloseStatusFilter = ShapeBase.NOT_SET,
    ) -> shapes.WorkflowExecutionCount:
        """
        Returns the number of closed workflow executions within the given domain that
        meet the specified filtering criteria.

        This operation is eventually consistent. The results are best effort and may not
        exactly reflect recent updates and changes.

        **Access Control**

        You can use IAM policies to control this action's access to Amazon SWF resources
        as follows:

          * Use a `Resource` element with the domain name to limit the action to only specified domains.

          * Use an `Action` element to allow or deny permission to call this action.

          * Constrain the following parameters by using a `Condition` element with the appropriate keys.

            * `tagFilter.tag`: String constraint. The key is `swf:tagFilter.tag`.

            * `typeFilter.name`: String constraint. The key is `swf:typeFilter.name`.

            * `typeFilter.version`: String constraint. The key is `swf:typeFilter.version`.

        If the caller doesn't have sufficient permissions to invoke the action, or the
        parameter values fall outside the specified constraints, the action fails. The
        associated event attribute's `cause` parameter is set to
        `OPERATION_NOT_PERMITTED`. For details and example IAM policies, see [Using IAM
        to Manage Access to Amazon SWF
        Workflows](http://docs.aws.amazon.com/amazonswf/latest/developerguide/swf-dev-
        iam.html) in the _Amazon SWF Developer Guide_.
        """
        if _request is None:
            _params = {}
            if domain is not ShapeBase.NOT_SET:
                _params['domain'] = domain
            if start_time_filter is not ShapeBase.NOT_SET:
                _params['start_time_filter'] = start_time_filter
            if close_time_filter is not ShapeBase.NOT_SET:
                _params['close_time_filter'] = close_time_filter
            if execution_filter is not ShapeBase.NOT_SET:
                _params['execution_filter'] = execution_filter
            if type_filter is not ShapeBase.NOT_SET:
                _params['type_filter'] = type_filter
            if tag_filter is not ShapeBase.NOT_SET:
                _params['tag_filter'] = tag_filter
            if close_status_filter is not ShapeBase.NOT_SET:
                _params['close_status_filter'] = close_status_filter
            _request = shapes.CountClosedWorkflowExecutionsInput(**_params)
        response = self._boto_client.count_closed_workflow_executions(
            **_request.to_boto()
        )

        return shapes.WorkflowExecutionCount.from_boto(response)

    def count_open_workflow_executions(
        self,
        _request: shapes.CountOpenWorkflowExecutionsInput = None,
        *,
        domain: str,
        start_time_filter: shapes.ExecutionTimeFilter,
        type_filter: shapes.WorkflowTypeFilter = ShapeBase.NOT_SET,
        tag_filter: shapes.TagFilter = ShapeBase.NOT_SET,
        execution_filter: shapes.WorkflowExecutionFilter = ShapeBase.NOT_SET,
    ) -> shapes.WorkflowExecutionCount:
        """
        Returns the number of open workflow executions within the given domain that meet
        the specified filtering criteria.

        This operation is eventually consistent. The results are best effort and may not
        exactly reflect recent updates and changes.

        **Access Control**

        You can use IAM policies to control this action's access to Amazon SWF resources
        as follows:

          * Use a `Resource` element with the domain name to limit the action to only specified domains.

          * Use an `Action` element to allow or deny permission to call this action.

          * Constrain the following parameters by using a `Condition` element with the appropriate keys.

            * `tagFilter.tag`: String constraint. The key is `swf:tagFilter.tag`.

            * `typeFilter.name`: String constraint. The key is `swf:typeFilter.name`.

            * `typeFilter.version`: String constraint. The key is `swf:typeFilter.version`.

        If the caller doesn't have sufficient permissions to invoke the action, or the
        parameter values fall outside the specified constraints, the action fails. The
        associated event attribute's `cause` parameter is set to
        `OPERATION_NOT_PERMITTED`. For details and example IAM policies, see [Using IAM
        to Manage Access to Amazon SWF
        Workflows](http://docs.aws.amazon.com/amazonswf/latest/developerguide/swf-dev-
        iam.html) in the _Amazon SWF Developer Guide_.
        """
        if _request is None:
            _params = {}
            if domain is not ShapeBase.NOT_SET:
                _params['domain'] = domain
            if start_time_filter is not ShapeBase.NOT_SET:
                _params['start_time_filter'] = start_time_filter
            if type_filter is not ShapeBase.NOT_SET:
                _params['type_filter'] = type_filter
            if tag_filter is not ShapeBase.NOT_SET:
                _params['tag_filter'] = tag_filter
            if execution_filter is not ShapeBase.NOT_SET:
                _params['execution_filter'] = execution_filter
            _request = shapes.CountOpenWorkflowExecutionsInput(**_params)
        response = self._boto_client.count_open_workflow_executions(
            **_request.to_boto()
        )

        return shapes.WorkflowExecutionCount.from_boto(response)

    def count_pending_activity_tasks(
        self,
        _request: shapes.CountPendingActivityTasksInput = None,
        *,
        domain: str,
        task_list: shapes.TaskList,
    ) -> shapes.PendingTaskCount:
        """
        Returns the estimated number of activity tasks in the specified task list. The
        count returned is an approximation and isn't guaranteed to be exact. If you
        specify a task list that no activity task was ever scheduled in then `0` is
        returned.

        **Access Control**

        You can use IAM policies to control this action's access to Amazon SWF resources
        as follows:

          * Use a `Resource` element with the domain name to limit the action to only specified domains.

          * Use an `Action` element to allow or deny permission to call this action.

          * Constrain the `taskList.name` parameter by using a `Condition` element with the `swf:taskList.name` key to allow the action to access only certain task lists.

        If the caller doesn't have sufficient permissions to invoke the action, or the
        parameter values fall outside the specified constraints, the action fails. The
        associated event attribute's `cause` parameter is set to
        `OPERATION_NOT_PERMITTED`. For details and example IAM policies, see [Using IAM
        to Manage Access to Amazon SWF
        Workflows](http://docs.aws.amazon.com/amazonswf/latest/developerguide/swf-dev-
        iam.html) in the _Amazon SWF Developer Guide_.
        """
        if _request is None:
            _params = {}
            if domain is not ShapeBase.NOT_SET:
                _params['domain'] = domain
            if task_list is not ShapeBase.NOT_SET:
                _params['task_list'] = task_list
            _request = shapes.CountPendingActivityTasksInput(**_params)
        response = self._boto_client.count_pending_activity_tasks(
            **_request.to_boto()
        )

        return shapes.PendingTaskCount.from_boto(response)

    def count_pending_decision_tasks(
        self,
        _request: shapes.CountPendingDecisionTasksInput = None,
        *,
        domain: str,
        task_list: shapes.TaskList,
    ) -> shapes.PendingTaskCount:
        """
        Returns the estimated number of decision tasks in the specified task list. The
        count returned is an approximation and isn't guaranteed to be exact. If you
        specify a task list that no decision task was ever scheduled in then `0` is
        returned.

        **Access Control**

        You can use IAM policies to control this action's access to Amazon SWF resources
        as follows:

          * Use a `Resource` element with the domain name to limit the action to only specified domains.

          * Use an `Action` element to allow or deny permission to call this action.

          * Constrain the `taskList.name` parameter by using a `Condition` element with the `swf:taskList.name` key to allow the action to access only certain task lists.

        If the caller doesn't have sufficient permissions to invoke the action, or the
        parameter values fall outside the specified constraints, the action fails. The
        associated event attribute's `cause` parameter is set to
        `OPERATION_NOT_PERMITTED`. For details and example IAM policies, see [Using IAM
        to Manage Access to Amazon SWF
        Workflows](http://docs.aws.amazon.com/amazonswf/latest/developerguide/swf-dev-
        iam.html) in the _Amazon SWF Developer Guide_.
        """
        if _request is None:
            _params = {}
            if domain is not ShapeBase.NOT_SET:
                _params['domain'] = domain
            if task_list is not ShapeBase.NOT_SET:
                _params['task_list'] = task_list
            _request = shapes.CountPendingDecisionTasksInput(**_params)
        response = self._boto_client.count_pending_decision_tasks(
            **_request.to_boto()
        )

        return shapes.PendingTaskCount.from_boto(response)

    def deprecate_activity_type(
        self,
        _request: shapes.DeprecateActivityTypeInput = None,
        *,
        domain: str,
        activity_type: shapes.ActivityType,
    ) -> None:
        """
        Deprecates the specified _activity type_. After an activity type has been
        deprecated, you cannot create new tasks of that activity type. Tasks of this
        type that were scheduled before the type was deprecated continue to run.

        This operation is eventually consistent. The results are best effort and may not
        exactly reflect recent updates and changes.

        **Access Control**

        You can use IAM policies to control this action's access to Amazon SWF resources
        as follows:

          * Use a `Resource` element with the domain name to limit the action to only specified domains.

          * Use an `Action` element to allow or deny permission to call this action.

          * Constrain the following parameters by using a `Condition` element with the appropriate keys.

            * `activityType.name`: String constraint. The key is `swf:activityType.name`.

            * `activityType.version`: String constraint. The key is `swf:activityType.version`.

        If the caller doesn't have sufficient permissions to invoke the action, or the
        parameter values fall outside the specified constraints, the action fails. The
        associated event attribute's `cause` parameter is set to
        `OPERATION_NOT_PERMITTED`. For details and example IAM policies, see [Using IAM
        to Manage Access to Amazon SWF
        Workflows](http://docs.aws.amazon.com/amazonswf/latest/developerguide/swf-dev-
        iam.html) in the _Amazon SWF Developer Guide_.
        """
        if _request is None:
            _params = {}
            if domain is not ShapeBase.NOT_SET:
                _params['domain'] = domain
            if activity_type is not ShapeBase.NOT_SET:
                _params['activity_type'] = activity_type
            _request = shapes.DeprecateActivityTypeInput(**_params)
        response = self._boto_client.deprecate_activity_type(
            **_request.to_boto()
        )

    def deprecate_domain(
        self,
        _request: shapes.DeprecateDomainInput = None,
        *,
        name: str,
    ) -> None:
        """
        Deprecates the specified domain. After a domain has been deprecated it cannot be
        used to create new workflow executions or register new types. However, you can
        still use visibility actions on this domain. Deprecating a domain also
        deprecates all activity and workflow types registered in the domain. Executions
        that were started before the domain was deprecated continues to run.

        This operation is eventually consistent. The results are best effort and may not
        exactly reflect recent updates and changes.

        **Access Control**

        You can use IAM policies to control this action's access to Amazon SWF resources
        as follows:

          * Use a `Resource` element with the domain name to limit the action to only specified domains.

          * Use an `Action` element to allow or deny permission to call this action.

          * You cannot use an IAM policy to constrain this action's parameters.

        If the caller doesn't have sufficient permissions to invoke the action, or the
        parameter values fall outside the specified constraints, the action fails. The
        associated event attribute's `cause` parameter is set to
        `OPERATION_NOT_PERMITTED`. For details and example IAM policies, see [Using IAM
        to Manage Access to Amazon SWF
        Workflows](http://docs.aws.amazon.com/amazonswf/latest/developerguide/swf-dev-
        iam.html) in the _Amazon SWF Developer Guide_.
        """
        if _request is None:
            _params = {}
            if name is not ShapeBase.NOT_SET:
                _params['name'] = name
            _request = shapes.DeprecateDomainInput(**_params)
        response = self._boto_client.deprecate_domain(**_request.to_boto())

    def deprecate_workflow_type(
        self,
        _request: shapes.DeprecateWorkflowTypeInput = None,
        *,
        domain: str,
        workflow_type: shapes.WorkflowType,
    ) -> None:
        """
        Deprecates the specified _workflow type_. After a workflow type has been
        deprecated, you cannot create new executions of that type. Executions that were
        started before the type was deprecated continues to run. A deprecated workflow
        type may still be used when calling visibility actions.

        This operation is eventually consistent. The results are best effort and may not
        exactly reflect recent updates and changes.

        **Access Control**

        You can use IAM policies to control this action's access to Amazon SWF resources
        as follows:

          * Use a `Resource` element with the domain name to limit the action to only specified domains.

          * Use an `Action` element to allow or deny permission to call this action.

          * Constrain the following parameters by using a `Condition` element with the appropriate keys.

            * `workflowType.name`: String constraint. The key is `swf:workflowType.name`.

            * `workflowType.version`: String constraint. The key is `swf:workflowType.version`.

        If the caller doesn't have sufficient permissions to invoke the action, or the
        parameter values fall outside the specified constraints, the action fails. The
        associated event attribute's `cause` parameter is set to
        `OPERATION_NOT_PERMITTED`. For details and example IAM policies, see [Using IAM
        to Manage Access to Amazon SWF
        Workflows](http://docs.aws.amazon.com/amazonswf/latest/developerguide/swf-dev-
        iam.html) in the _Amazon SWF Developer Guide_.
        """
        if _request is None:
            _params = {}
            if domain is not ShapeBase.NOT_SET:
                _params['domain'] = domain
            if workflow_type is not ShapeBase.NOT_SET:
                _params['workflow_type'] = workflow_type
            _request = shapes.DeprecateWorkflowTypeInput(**_params)
        response = self._boto_client.deprecate_workflow_type(
            **_request.to_boto()
        )

    def describe_activity_type(
        self,
        _request: shapes.DescribeActivityTypeInput = None,
        *,
        domain: str,
        activity_type: shapes.ActivityType,
    ) -> shapes.ActivityTypeDetail:
        """
        Returns information about the specified activity type. This includes
        configuration settings provided when the type was registered and other general
        information about the type.

        **Access Control**

        You can use IAM policies to control this action's access to Amazon SWF resources
        as follows:

          * Use a `Resource` element with the domain name to limit the action to only specified domains.

          * Use an `Action` element to allow or deny permission to call this action.

          * Constrain the following parameters by using a `Condition` element with the appropriate keys.

            * `activityType.name`: String constraint. The key is `swf:activityType.name`.

            * `activityType.version`: String constraint. The key is `swf:activityType.version`.

        If the caller doesn't have sufficient permissions to invoke the action, or the
        parameter values fall outside the specified constraints, the action fails. The
        associated event attribute's `cause` parameter is set to
        `OPERATION_NOT_PERMITTED`. For details and example IAM policies, see [Using IAM
        to Manage Access to Amazon SWF
        Workflows](http://docs.aws.amazon.com/amazonswf/latest/developerguide/swf-dev-
        iam.html) in the _Amazon SWF Developer Guide_.
        """
        if _request is None:
            _params = {}
            if domain is not ShapeBase.NOT_SET:
                _params['domain'] = domain
            if activity_type is not ShapeBase.NOT_SET:
                _params['activity_type'] = activity_type
            _request = shapes.DescribeActivityTypeInput(**_params)
        response = self._boto_client.describe_activity_type(
            **_request.to_boto()
        )

        return shapes.ActivityTypeDetail.from_boto(response)

    def describe_domain(
        self,
        _request: shapes.DescribeDomainInput = None,
        *,
        name: str,
    ) -> shapes.DomainDetail:
        """
        Returns information about the specified domain, including description and
        status.

        **Access Control**

        You can use IAM policies to control this action's access to Amazon SWF resources
        as follows:

          * Use a `Resource` element with the domain name to limit the action to only specified domains.

          * Use an `Action` element to allow or deny permission to call this action.

          * You cannot use an IAM policy to constrain this action's parameters.

        If the caller doesn't have sufficient permissions to invoke the action, or the
        parameter values fall outside the specified constraints, the action fails. The
        associated event attribute's `cause` parameter is set to
        `OPERATION_NOT_PERMITTED`. For details and example IAM policies, see [Using IAM
        to Manage Access to Amazon SWF
        Workflows](http://docs.aws.amazon.com/amazonswf/latest/developerguide/swf-dev-
        iam.html) in the _Amazon SWF Developer Guide_.
        """
        if _request is None:
            _params = {}
            if name is not ShapeBase.NOT_SET:
                _params['name'] = name
            _request = shapes.DescribeDomainInput(**_params)
        response = self._boto_client.describe_domain(**_request.to_boto())

        return shapes.DomainDetail.from_boto(response)

    def describe_workflow_execution(
        self,
        _request: shapes.DescribeWorkflowExecutionInput = None,
        *,
        domain: str,
        execution: shapes.WorkflowExecution,
    ) -> shapes.WorkflowExecutionDetail:
        """
        Returns information about the specified workflow execution including its type
        and some statistics.

        This operation is eventually consistent. The results are best effort and may not
        exactly reflect recent updates and changes.

        **Access Control**

        You can use IAM policies to control this action's access to Amazon SWF resources
        as follows:

          * Use a `Resource` element with the domain name to limit the action to only specified domains.

          * Use an `Action` element to allow or deny permission to call this action.

          * You cannot use an IAM policy to constrain this action's parameters.

        If the caller doesn't have sufficient permissions to invoke the action, or the
        parameter values fall outside the specified constraints, the action fails. The
        associated event attribute's `cause` parameter is set to
        `OPERATION_NOT_PERMITTED`. For details and example IAM policies, see [Using IAM
        to Manage Access to Amazon SWF
        Workflows](http://docs.aws.amazon.com/amazonswf/latest/developerguide/swf-dev-
        iam.html) in the _Amazon SWF Developer Guide_.
        """
        if _request is None:
            _params = {}
            if domain is not ShapeBase.NOT_SET:
                _params['domain'] = domain
            if execution is not ShapeBase.NOT_SET:
                _params['execution'] = execution
            _request = shapes.DescribeWorkflowExecutionInput(**_params)
        response = self._boto_client.describe_workflow_execution(
            **_request.to_boto()
        )

        return shapes.WorkflowExecutionDetail.from_boto(response)

    def describe_workflow_type(
        self,
        _request: shapes.DescribeWorkflowTypeInput = None,
        *,
        domain: str,
        workflow_type: shapes.WorkflowType,
    ) -> shapes.WorkflowTypeDetail:
        """
        Returns information about the specified _workflow type_. This includes
        configuration settings specified when the type was registered and other
        information such as creation date, current status, etc.

        **Access Control**

        You can use IAM policies to control this action's access to Amazon SWF resources
        as follows:

          * Use a `Resource` element with the domain name to limit the action to only specified domains.

          * Use an `Action` element to allow or deny permission to call this action.

          * Constrain the following parameters by using a `Condition` element with the appropriate keys.

            * `workflowType.name`: String constraint. The key is `swf:workflowType.name`.

            * `workflowType.version`: String constraint. The key is `swf:workflowType.version`.

        If the caller doesn't have sufficient permissions to invoke the action, or the
        parameter values fall outside the specified constraints, the action fails. The
        associated event attribute's `cause` parameter is set to
        `OPERATION_NOT_PERMITTED`. For details and example IAM policies, see [Using IAM
        to Manage Access to Amazon SWF
        Workflows](http://docs.aws.amazon.com/amazonswf/latest/developerguide/swf-dev-
        iam.html) in the _Amazon SWF Developer Guide_.
        """
        if _request is None:
            _params = {}
            if domain is not ShapeBase.NOT_SET:
                _params['domain'] = domain
            if workflow_type is not ShapeBase.NOT_SET:
                _params['workflow_type'] = workflow_type
            _request = shapes.DescribeWorkflowTypeInput(**_params)
        response = self._boto_client.describe_workflow_type(
            **_request.to_boto()
        )

        return shapes.WorkflowTypeDetail.from_boto(response)

    def get_workflow_execution_history(
        self,
        _request: shapes.GetWorkflowExecutionHistoryInput = None,
        *,
        domain: str,
        execution: shapes.WorkflowExecution,
        next_page_token: str = ShapeBase.NOT_SET,
        maximum_page_size: int = ShapeBase.NOT_SET,
        reverse_order: bool = ShapeBase.NOT_SET,
    ) -> shapes.History:
        """
        Returns the history of the specified workflow execution. The results may be
        split into multiple pages. To retrieve subsequent pages, make the call again
        using the `nextPageToken` returned by the initial call.

        This operation is eventually consistent. The results are best effort and may not
        exactly reflect recent updates and changes.

        **Access Control**

        You can use IAM policies to control this action's access to Amazon SWF resources
        as follows:

          * Use a `Resource` element with the domain name to limit the action to only specified domains.

          * Use an `Action` element to allow or deny permission to call this action.

          * You cannot use an IAM policy to constrain this action's parameters.

        If the caller doesn't have sufficient permissions to invoke the action, or the
        parameter values fall outside the specified constraints, the action fails. The
        associated event attribute's `cause` parameter is set to
        `OPERATION_NOT_PERMITTED`. For details and example IAM policies, see [Using IAM
        to Manage Access to Amazon SWF
        Workflows](http://docs.aws.amazon.com/amazonswf/latest/developerguide/swf-dev-
        iam.html) in the _Amazon SWF Developer Guide_.
        """
        if _request is None:
            _params = {}
            if domain is not ShapeBase.NOT_SET:
                _params['domain'] = domain
            if execution is not ShapeBase.NOT_SET:
                _params['execution'] = execution
            if next_page_token is not ShapeBase.NOT_SET:
                _params['next_page_token'] = next_page_token
            if maximum_page_size is not ShapeBase.NOT_SET:
                _params['maximum_page_size'] = maximum_page_size
            if reverse_order is not ShapeBase.NOT_SET:
                _params['reverse_order'] = reverse_order
            _request = shapes.GetWorkflowExecutionHistoryInput(**_params)
        paginator = self.get_paginator("get_workflow_execution_history"
                                      ).paginate(**_request.to_boto())
        page_generator = (page for page in paginator)
        first_page = next(page_generator)
        result = shapes.History.from_boto(first_page)
        result._page_iterator = page_generator
        return result

        return shapes.History.from_boto(response)

    def list_activity_types(
        self,
        _request: shapes.ListActivityTypesInput = None,
        *,
        domain: str,
        registration_status: typing.Union[str, shapes.RegistrationStatus],
        name: str = ShapeBase.NOT_SET,
        next_page_token: str = ShapeBase.NOT_SET,
        maximum_page_size: int = ShapeBase.NOT_SET,
        reverse_order: bool = ShapeBase.NOT_SET,
    ) -> shapes.ActivityTypeInfos:
        """
        Returns information about all activities registered in the specified domain that
        match the specified name and registration status. The result includes
        information like creation date, current status of the activity, etc. The results
        may be split into multiple pages. To retrieve subsequent pages, make the call
        again using the `nextPageToken` returned by the initial call.

        **Access Control**

        You can use IAM policies to control this action's access to Amazon SWF resources
        as follows:

          * Use a `Resource` element with the domain name to limit the action to only specified domains.

          * Use an `Action` element to allow or deny permission to call this action.

          * You cannot use an IAM policy to constrain this action's parameters.

        If the caller doesn't have sufficient permissions to invoke the action, or the
        parameter values fall outside the specified constraints, the action fails. The
        associated event attribute's `cause` parameter is set to
        `OPERATION_NOT_PERMITTED`. For details and example IAM policies, see [Using IAM
        to Manage Access to Amazon SWF
        Workflows](http://docs.aws.amazon.com/amazonswf/latest/developerguide/swf-dev-
        iam.html) in the _Amazon SWF Developer Guide_.
        """
        if _request is None:
            _params = {}
            if domain is not ShapeBase.NOT_SET:
                _params['domain'] = domain
            if registration_status is not ShapeBase.NOT_SET:
                _params['registration_status'] = registration_status
            if name is not ShapeBase.NOT_SET:
                _params['name'] = name
            if next_page_token is not ShapeBase.NOT_SET:
                _params['next_page_token'] = next_page_token
            if maximum_page_size is not ShapeBase.NOT_SET:
                _params['maximum_page_size'] = maximum_page_size
            if reverse_order is not ShapeBase.NOT_SET:
                _params['reverse_order'] = reverse_order
            _request = shapes.ListActivityTypesInput(**_params)
        paginator = self.get_paginator("list_activity_types").paginate(
            **_request.to_boto()
        )
        page_generator = (page for page in paginator)
        first_page = next(page_generator)
        result = shapes.ActivityTypeInfos.from_boto(first_page)
        result._page_iterator = page_generator
        return result

        return shapes.ActivityTypeInfos.from_boto(response)

    def list_closed_workflow_executions(
        self,
        _request: shapes.ListClosedWorkflowExecutionsInput = None,
        *,
        domain: str,
        start_time_filter: shapes.ExecutionTimeFilter = ShapeBase.NOT_SET,
        close_time_filter: shapes.ExecutionTimeFilter = ShapeBase.NOT_SET,
        execution_filter: shapes.WorkflowExecutionFilter = ShapeBase.NOT_SET,
        close_status_filter: shapes.CloseStatusFilter = ShapeBase.NOT_SET,
        type_filter: shapes.WorkflowTypeFilter = ShapeBase.NOT_SET,
        tag_filter: shapes.TagFilter = ShapeBase.NOT_SET,
        next_page_token: str = ShapeBase.NOT_SET,
        maximum_page_size: int = ShapeBase.NOT_SET,
        reverse_order: bool = ShapeBase.NOT_SET,
    ) -> shapes.WorkflowExecutionInfos:
        """
        Returns a list of closed workflow executions in the specified domain that meet
        the filtering criteria. The results may be split into multiple pages. To
        retrieve subsequent pages, make the call again using the nextPageToken returned
        by the initial call.

        This operation is eventually consistent. The results are best effort and may not
        exactly reflect recent updates and changes.

        **Access Control**

        You can use IAM policies to control this action's access to Amazon SWF resources
        as follows:

          * Use a `Resource` element with the domain name to limit the action to only specified domains.

          * Use an `Action` element to allow or deny permission to call this action.

          * Constrain the following parameters by using a `Condition` element with the appropriate keys.

            * `tagFilter.tag`: String constraint. The key is `swf:tagFilter.tag`.

            * `typeFilter.name`: String constraint. The key is `swf:typeFilter.name`.

            * `typeFilter.version`: String constraint. The key is `swf:typeFilter.version`.

        If the caller doesn't have sufficient permissions to invoke the action, or the
        parameter values fall outside the specified constraints, the action fails. The
        associated event attribute's `cause` parameter is set to
        `OPERATION_NOT_PERMITTED`. For details and example IAM policies, see [Using IAM
        to Manage Access to Amazon SWF
        Workflows](http://docs.aws.amazon.com/amazonswf/latest/developerguide/swf-dev-
        iam.html) in the _Amazon SWF Developer Guide_.
        """
        if _request is None:
            _params = {}
            if domain is not ShapeBase.NOT_SET:
                _params['domain'] = domain
            if start_time_filter is not ShapeBase.NOT_SET:
                _params['start_time_filter'] = start_time_filter
            if close_time_filter is not ShapeBase.NOT_SET:
                _params['close_time_filter'] = close_time_filter
            if execution_filter is not ShapeBase.NOT_SET:
                _params['execution_filter'] = execution_filter
            if close_status_filter is not ShapeBase.NOT_SET:
                _params['close_status_filter'] = close_status_filter
            if type_filter is not ShapeBase.NOT_SET:
                _params['type_filter'] = type_filter
            if tag_filter is not ShapeBase.NOT_SET:
                _params['tag_filter'] = tag_filter
            if next_page_token is not ShapeBase.NOT_SET:
                _params['next_page_token'] = next_page_token
            if maximum_page_size is not ShapeBase.NOT_SET:
                _params['maximum_page_size'] = maximum_page_size
            if reverse_order is not ShapeBase.NOT_SET:
                _params['reverse_order'] = reverse_order
            _request = shapes.ListClosedWorkflowExecutionsInput(**_params)
        paginator = self.get_paginator("list_closed_workflow_executions"
                                      ).paginate(**_request.to_boto())
        page_generator = (page for page in paginator)
        first_page = next(page_generator)
        result = shapes.WorkflowExecutionInfos.from_boto(first_page)
        result._page_iterator = page_generator
        return result

        return shapes.WorkflowExecutionInfos.from_boto(response)

    def list_domains(
        self,
        _request: shapes.ListDomainsInput = None,
        *,
        registration_status: typing.Union[str, shapes.RegistrationStatus],
        next_page_token: str = ShapeBase.NOT_SET,
        maximum_page_size: int = ShapeBase.NOT_SET,
        reverse_order: bool = ShapeBase.NOT_SET,
    ) -> shapes.DomainInfos:
        """
        Returns the list of domains registered in the account. The results may be split
        into multiple pages. To retrieve subsequent pages, make the call again using the
        nextPageToken returned by the initial call.

        This operation is eventually consistent. The results are best effort and may not
        exactly reflect recent updates and changes.

        **Access Control**

        You can use IAM policies to control this action's access to Amazon SWF resources
        as follows:

          * Use a `Resource` element with the domain name to limit the action to only specified domains. The element must be set to `arn:aws:swf::AccountID:domain/*`, where _AccountID_ is the account ID, with no dashes.

          * Use an `Action` element to allow or deny permission to call this action.

          * You cannot use an IAM policy to constrain this action's parameters.

        If the caller doesn't have sufficient permissions to invoke the action, or the
        parameter values fall outside the specified constraints, the action fails. The
        associated event attribute's `cause` parameter is set to
        `OPERATION_NOT_PERMITTED`. For details and example IAM policies, see [Using IAM
        to Manage Access to Amazon SWF
        Workflows](http://docs.aws.amazon.com/amazonswf/latest/developerguide/swf-dev-
        iam.html) in the _Amazon SWF Developer Guide_.
        """
        if _request is None:
            _params = {}
            if registration_status is not ShapeBase.NOT_SET:
                _params['registration_status'] = registration_status
            if next_page_token is not ShapeBase.NOT_SET:
                _params['next_page_token'] = next_page_token
            if maximum_page_size is not ShapeBase.NOT_SET:
                _params['maximum_page_size'] = maximum_page_size
            if reverse_order is not ShapeBase.NOT_SET:
                _params['reverse_order'] = reverse_order
            _request = shapes.ListDomainsInput(**_params)
        paginator = self.get_paginator("list_domains").paginate(
            **_request.to_boto()
        )
        page_generator = (page for page in paginator)
        first_page = next(page_generator)
        result = shapes.DomainInfos.from_boto(first_page)
        result._page_iterator = page_generator
        return result

        return shapes.DomainInfos.from_boto(response)

    def list_open_workflow_executions(
        self,
        _request: shapes.ListOpenWorkflowExecutionsInput = None,
        *,
        domain: str,
        start_time_filter: shapes.ExecutionTimeFilter,
        type_filter: shapes.WorkflowTypeFilter = ShapeBase.NOT_SET,
        tag_filter: shapes.TagFilter = ShapeBase.NOT_SET,
        next_page_token: str = ShapeBase.NOT_SET,
        maximum_page_size: int = ShapeBase.NOT_SET,
        reverse_order: bool = ShapeBase.NOT_SET,
        execution_filter: shapes.WorkflowExecutionFilter = ShapeBase.NOT_SET,
    ) -> shapes.WorkflowExecutionInfos:
        """
        Returns a list of open workflow executions in the specified domain that meet the
        filtering criteria. The results may be split into multiple pages. To retrieve
        subsequent pages, make the call again using the nextPageToken returned by the
        initial call.

        This operation is eventually consistent. The results are best effort and may not
        exactly reflect recent updates and changes.

        **Access Control**

        You can use IAM policies to control this action's access to Amazon SWF resources
        as follows:

          * Use a `Resource` element with the domain name to limit the action to only specified domains.

          * Use an `Action` element to allow or deny permission to call this action.

          * Constrain the following parameters by using a `Condition` element with the appropriate keys.

            * `tagFilter.tag`: String constraint. The key is `swf:tagFilter.tag`.

            * `typeFilter.name`: String constraint. The key is `swf:typeFilter.name`.

            * `typeFilter.version`: String constraint. The key is `swf:typeFilter.version`.

        If the caller doesn't have sufficient permissions to invoke the action, or the
        parameter values fall outside the specified constraints, the action fails. The
        associated event attribute's `cause` parameter is set to
        `OPERATION_NOT_PERMITTED`. For details and example IAM policies, see [Using IAM
        to Manage Access to Amazon SWF
        Workflows](http://docs.aws.amazon.com/amazonswf/latest/developerguide/swf-dev-
        iam.html) in the _Amazon SWF Developer Guide_.
        """
        if _request is None:
            _params = {}
            if domain is not ShapeBase.NOT_SET:
                _params['domain'] = domain
            if start_time_filter is not ShapeBase.NOT_SET:
                _params['start_time_filter'] = start_time_filter
            if type_filter is not ShapeBase.NOT_SET:
                _params['type_filter'] = type_filter
            if tag_filter is not ShapeBase.NOT_SET:
                _params['tag_filter'] = tag_filter
            if next_page_token is not ShapeBase.NOT_SET:
                _params['next_page_token'] = next_page_token
            if maximum_page_size is not ShapeBase.NOT_SET:
                _params['maximum_page_size'] = maximum_page_size
            if reverse_order is not ShapeBase.NOT_SET:
                _params['reverse_order'] = reverse_order
            if execution_filter is not ShapeBase.NOT_SET:
                _params['execution_filter'] = execution_filter
            _request = shapes.ListOpenWorkflowExecutionsInput(**_params)
        paginator = self.get_paginator("list_open_workflow_executions"
                                      ).paginate(**_request.to_boto())
        page_generator = (page for page in paginator)
        first_page = next(page_generator)
        result = shapes.WorkflowExecutionInfos.from_boto(first_page)
        result._page_iterator = page_generator
        return result

        return shapes.WorkflowExecutionInfos.from_boto(response)

    def list_workflow_types(
        self,
        _request: shapes.ListWorkflowTypesInput = None,
        *,
        domain: str,
        registration_status: typing.Union[str, shapes.RegistrationStatus],
        name: str = ShapeBase.NOT_SET,
        next_page_token: str = ShapeBase.NOT_SET,
        maximum_page_size: int = ShapeBase.NOT_SET,
        reverse_order: bool = ShapeBase.NOT_SET,
    ) -> shapes.WorkflowTypeInfos:
        """
        Returns information about workflow types in the specified domain. The results
        may be split into multiple pages that can be retrieved by making the call
        repeatedly.

        **Access Control**

        You can use IAM policies to control this action's access to Amazon SWF resources
        as follows:

          * Use a `Resource` element with the domain name to limit the action to only specified domains.

          * Use an `Action` element to allow or deny permission to call this action.

          * You cannot use an IAM policy to constrain this action's parameters.

        If the caller doesn't have sufficient permissions to invoke the action, or the
        parameter values fall outside the specified constraints, the action fails. The
        associated event attribute's `cause` parameter is set to
        `OPERATION_NOT_PERMITTED`. For details and example IAM policies, see [Using IAM
        to Manage Access to Amazon SWF
        Workflows](http://docs.aws.amazon.com/amazonswf/latest/developerguide/swf-dev-
        iam.html) in the _Amazon SWF Developer Guide_.
        """
        if _request is None:
            _params = {}
            if domain is not ShapeBase.NOT_SET:
                _params['domain'] = domain
            if registration_status is not ShapeBase.NOT_SET:
                _params['registration_status'] = registration_status
            if name is not ShapeBase.NOT_SET:
                _params['name'] = name
            if next_page_token is not ShapeBase.NOT_SET:
                _params['next_page_token'] = next_page_token
            if maximum_page_size is not ShapeBase.NOT_SET:
                _params['maximum_page_size'] = maximum_page_size
            if reverse_order is not ShapeBase.NOT_SET:
                _params['reverse_order'] = reverse_order
            _request = shapes.ListWorkflowTypesInput(**_params)
        paginator = self.get_paginator("list_workflow_types").paginate(
            **_request.to_boto()
        )
        page_generator = (page for page in paginator)
        first_page = next(page_generator)
        result = shapes.WorkflowTypeInfos.from_boto(first_page)
        result._page_iterator = page_generator
        return result

        return shapes.WorkflowTypeInfos.from_boto(response)

    def poll_for_activity_task(
        self,
        _request: shapes.PollForActivityTaskInput = None,
        *,
        domain: str,
        task_list: shapes.TaskList,
        identity: str = ShapeBase.NOT_SET,
    ) -> shapes.ActivityTask:
        """
        Used by workers to get an ActivityTask from the specified activity `taskList`.
        This initiates a long poll, where the service holds the HTTP connection open and
        responds as soon as a task becomes available. The maximum time the service holds
        on to the request before responding is 60 seconds. If no task is available
        within 60 seconds, the poll returns an empty result. An empty result, in this
        context, means that an ActivityTask is returned, but that the value of taskToken
        is an empty string. If a task is returned, the worker should use its type to
        identify and process it correctly.

        Workers should set their client side socket timeout to at least 70 seconds (10
        seconds higher than the maximum time service may hold the poll request).

        **Access Control**

        You can use IAM policies to control this action's access to Amazon SWF resources
        as follows:

          * Use a `Resource` element with the domain name to limit the action to only specified domains.

          * Use an `Action` element to allow or deny permission to call this action.

          * Constrain the `taskList.name` parameter by using a `Condition` element with the `swf:taskList.name` key to allow the action to access only certain task lists.

        If the caller doesn't have sufficient permissions to invoke the action, or the
        parameter values fall outside the specified constraints, the action fails. The
        associated event attribute's `cause` parameter is set to
        `OPERATION_NOT_PERMITTED`. For details and example IAM policies, see [Using IAM
        to Manage Access to Amazon SWF
        Workflows](http://docs.aws.amazon.com/amazonswf/latest/developerguide/swf-dev-
        iam.html) in the _Amazon SWF Developer Guide_.
        """
        if _request is None:
            _params = {}
            if domain is not ShapeBase.NOT_SET:
                _params['domain'] = domain
            if task_list is not ShapeBase.NOT_SET:
                _params['task_list'] = task_list
            if identity is not ShapeBase.NOT_SET:
                _params['identity'] = identity
            _request = shapes.PollForActivityTaskInput(**_params)
        response = self._boto_client.poll_for_activity_task(
            **_request.to_boto()
        )

        return shapes.ActivityTask.from_boto(response)

    def poll_for_decision_task(
        self,
        _request: shapes.PollForDecisionTaskInput = None,
        *,
        domain: str,
        task_list: shapes.TaskList,
        identity: str = ShapeBase.NOT_SET,
        next_page_token: str = ShapeBase.NOT_SET,
        maximum_page_size: int = ShapeBase.NOT_SET,
        reverse_order: bool = ShapeBase.NOT_SET,
    ) -> shapes.DecisionTask:
        """
        Used by deciders to get a DecisionTask from the specified decision `taskList`. A
        decision task may be returned for any open workflow execution that is using the
        specified task list. The task includes a paginated view of the history of the
        workflow execution. The decider should use the workflow type and the history to
        determine how to properly handle the task.

        This action initiates a long poll, where the service holds the HTTP connection
        open and responds as soon a task becomes available. If no decision task is
        available in the specified task list before the timeout of 60 seconds expires,
        an empty result is returned. An empty result, in this context, means that a
        DecisionTask is returned, but that the value of taskToken is an empty string.

        Deciders should set their client side socket timeout to at least 70 seconds (10
        seconds higher than the timeout).

        Because the number of workflow history events for a single workflow execution
        might be very large, the result returned might be split up across a number of
        pages. To retrieve subsequent pages, make additional calls to
        `PollForDecisionTask` using the `nextPageToken` returned by the initial call.
        Note that you do _not_ call `GetWorkflowExecutionHistory` with this
        `nextPageToken`. Instead, call `PollForDecisionTask` again.

        **Access Control**

        You can use IAM policies to control this action's access to Amazon SWF resources
        as follows:

          * Use a `Resource` element with the domain name to limit the action to only specified domains.

          * Use an `Action` element to allow or deny permission to call this action.

          * Constrain the `taskList.name` parameter by using a `Condition` element with the `swf:taskList.name` key to allow the action to access only certain task lists.

        If the caller doesn't have sufficient permissions to invoke the action, or the
        parameter values fall outside the specified constraints, the action fails. The
        associated event attribute's `cause` parameter is set to
        `OPERATION_NOT_PERMITTED`. For details and example IAM policies, see [Using IAM
        to Manage Access to Amazon SWF
        Workflows](http://docs.aws.amazon.com/amazonswf/latest/developerguide/swf-dev-
        iam.html) in the _Amazon SWF Developer Guide_.
        """
        if _request is None:
            _params = {}
            if domain is not ShapeBase.NOT_SET:
                _params['domain'] = domain
            if task_list is not ShapeBase.NOT_SET:
                _params['task_list'] = task_list
            if identity is not ShapeBase.NOT_SET:
                _params['identity'] = identity
            if next_page_token is not ShapeBase.NOT_SET:
                _params['next_page_token'] = next_page_token
            if maximum_page_size is not ShapeBase.NOT_SET:
                _params['maximum_page_size'] = maximum_page_size
            if reverse_order is not ShapeBase.NOT_SET:
                _params['reverse_order'] = reverse_order
            _request = shapes.PollForDecisionTaskInput(**_params)
        paginator = self.get_paginator("poll_for_decision_task").paginate(
            **_request.to_boto()
        )
        page_generator = (page for page in paginator)
        first_page = next(page_generator)
        result = shapes.DecisionTask.from_boto(first_page)
        result._page_iterator = page_generator
        return result

        return shapes.DecisionTask.from_boto(response)

    def record_activity_task_heartbeat(
        self,
        _request: shapes.RecordActivityTaskHeartbeatInput = None,
        *,
        task_token: str,
        details: str = ShapeBase.NOT_SET,
    ) -> shapes.ActivityTaskStatus:
        """
        Used by activity workers to report to the service that the ActivityTask
        represented by the specified `taskToken` is still making progress. The worker
        can also specify details of the progress, for example percent complete, using
        the `details` parameter. This action can also be used by the worker as a
        mechanism to check if cancellation is being requested for the activity task. If
        a cancellation is being attempted for the specified task, then the boolean
        `cancelRequested` flag returned by the service is set to `true`.

        This action resets the `taskHeartbeatTimeout` clock. The `taskHeartbeatTimeout`
        is specified in RegisterActivityType.

        This action doesn't in itself create an event in the workflow execution history.
        However, if the task times out, the workflow execution history contains a
        `ActivityTaskTimedOut` event that contains the information from the last
        heartbeat generated by the activity worker.

        The `taskStartToCloseTimeout` of an activity type is the maximum duration of an
        activity task, regardless of the number of RecordActivityTaskHeartbeat requests
        received. The `taskStartToCloseTimeout` is also specified in
        RegisterActivityType.

        This operation is only useful for long-lived activities to report liveliness of
        the task and to determine if a cancellation is being attempted.

        If the `cancelRequested` flag returns `true`, a cancellation is being attempted.
        If the worker can cancel the activity, it should respond with
        RespondActivityTaskCanceled. Otherwise, it should ignore the cancellation
        request.

        **Access Control**

        You can use IAM policies to control this action's access to Amazon SWF resources
        as follows:

          * Use a `Resource` element with the domain name to limit the action to only specified domains.

          * Use an `Action` element to allow or deny permission to call this action.

          * You cannot use an IAM policy to constrain this action's parameters.

        If the caller doesn't have sufficient permissions to invoke the action, or the
        parameter values fall outside the specified constraints, the action fails. The
        associated event attribute's `cause` parameter is set to
        `OPERATION_NOT_PERMITTED`. For details and example IAM policies, see [Using IAM
        to Manage Access to Amazon SWF
        Workflows](http://docs.aws.amazon.com/amazonswf/latest/developerguide/swf-dev-
        iam.html) in the _Amazon SWF Developer Guide_.
        """
        if _request is None:
            _params = {}
            if task_token is not ShapeBase.NOT_SET:
                _params['task_token'] = task_token
            if details is not ShapeBase.NOT_SET:
                _params['details'] = details
            _request = shapes.RecordActivityTaskHeartbeatInput(**_params)
        response = self._boto_client.record_activity_task_heartbeat(
            **_request.to_boto()
        )

        return shapes.ActivityTaskStatus.from_boto(response)

    def register_activity_type(
        self,
        _request: shapes.RegisterActivityTypeInput = None,
        *,
        domain: str,
        name: str,
        version: str,
        description: str = ShapeBase.NOT_SET,
        default_task_start_to_close_timeout: str = ShapeBase.NOT_SET,
        default_task_heartbeat_timeout: str = ShapeBase.NOT_SET,
        default_task_list: shapes.TaskList = ShapeBase.NOT_SET,
        default_task_priority: str = ShapeBase.NOT_SET,
        default_task_schedule_to_start_timeout: str = ShapeBase.NOT_SET,
        default_task_schedule_to_close_timeout: str = ShapeBase.NOT_SET,
    ) -> None:
        """
        Registers a new _activity type_ along with its configuration settings in the
        specified domain.

        A `TypeAlreadyExists` fault is returned if the type already exists in the
        domain. You cannot change any configuration settings of the type after its
        registration, and it must be registered as a new version.

        **Access Control**

        You can use IAM policies to control this action's access to Amazon SWF resources
        as follows:

          * Use a `Resource` element with the domain name to limit the action to only specified domains.

          * Use an `Action` element to allow or deny permission to call this action.

          * Constrain the following parameters by using a `Condition` element with the appropriate keys.

            * `defaultTaskList.name`: String constraint. The key is `swf:defaultTaskList.name`.

            * `name`: String constraint. The key is `swf:name`.

            * `version`: String constraint. The key is `swf:version`.

        If the caller doesn't have sufficient permissions to invoke the action, or the
        parameter values fall outside the specified constraints, the action fails. The
        associated event attribute's `cause` parameter is set to
        `OPERATION_NOT_PERMITTED`. For details and example IAM policies, see [Using IAM
        to Manage Access to Amazon SWF
        Workflows](http://docs.aws.amazon.com/amazonswf/latest/developerguide/swf-dev-
        iam.html) in the _Amazon SWF Developer Guide_.
        """
        if _request is None:
            _params = {}
            if domain is not ShapeBase.NOT_SET:
                _params['domain'] = domain
            if name is not ShapeBase.NOT_SET:
                _params['name'] = name
            if version is not ShapeBase.NOT_SET:
                _params['version'] = version
            if description is not ShapeBase.NOT_SET:
                _params['description'] = description
            if default_task_start_to_close_timeout is not ShapeBase.NOT_SET:
                _params['default_task_start_to_close_timeout'
                       ] = default_task_start_to_close_timeout
            if default_task_heartbeat_timeout is not ShapeBase.NOT_SET:
                _params['default_task_heartbeat_timeout'
                       ] = default_task_heartbeat_timeout
            if default_task_list is not ShapeBase.NOT_SET:
                _params['default_task_list'] = default_task_list
            if default_task_priority is not ShapeBase.NOT_SET:
                _params['default_task_priority'] = default_task_priority
            if default_task_schedule_to_start_timeout is not ShapeBase.NOT_SET:
                _params['default_task_schedule_to_start_timeout'
                       ] = default_task_schedule_to_start_timeout
            if default_task_schedule_to_close_timeout is not ShapeBase.NOT_SET:
                _params['default_task_schedule_to_close_timeout'
                       ] = default_task_schedule_to_close_timeout
            _request = shapes.RegisterActivityTypeInput(**_params)
        response = self._boto_client.register_activity_type(
            **_request.to_boto()
        )

    def register_domain(
        self,
        _request: shapes.RegisterDomainInput = None,
        *,
        name: str,
        workflow_execution_retention_period_in_days: str,
        description: str = ShapeBase.NOT_SET,
    ) -> None:
        """
        Registers a new domain.

        **Access Control**

        You can use IAM policies to control this action's access to Amazon SWF resources
        as follows:

          * You cannot use an IAM policy to control domain access for this action. The name of the domain being registered is available as the resource of this action.

          * Use an `Action` element to allow or deny permission to call this action.

          * You cannot use an IAM policy to constrain this action's parameters.

        If the caller doesn't have sufficient permissions to invoke the action, or the
        parameter values fall outside the specified constraints, the action fails. The
        associated event attribute's `cause` parameter is set to
        `OPERATION_NOT_PERMITTED`. For details and example IAM policies, see [Using IAM
        to Manage Access to Amazon SWF
        Workflows](http://docs.aws.amazon.com/amazonswf/latest/developerguide/swf-dev-
        iam.html) in the _Amazon SWF Developer Guide_.
        """
        if _request is None:
            _params = {}
            if name is not ShapeBase.NOT_SET:
                _params['name'] = name
            if workflow_execution_retention_period_in_days is not ShapeBase.NOT_SET:
                _params['workflow_execution_retention_period_in_days'
                       ] = workflow_execution_retention_period_in_days
            if description is not ShapeBase.NOT_SET:
                _params['description'] = description
            _request = shapes.RegisterDomainInput(**_params)
        response = self._boto_client.register_domain(**_request.to_boto())

    def register_workflow_type(
        self,
        _request: shapes.RegisterWorkflowTypeInput = None,
        *,
        domain: str,
        name: str,
        version: str,
        description: str = ShapeBase.NOT_SET,
        default_task_start_to_close_timeout: str = ShapeBase.NOT_SET,
        default_execution_start_to_close_timeout: str = ShapeBase.NOT_SET,
        default_task_list: shapes.TaskList = ShapeBase.NOT_SET,
        default_task_priority: str = ShapeBase.NOT_SET,
        default_child_policy: typing.Union[str, shapes.ChildPolicy] = ShapeBase.
        NOT_SET,
        default_lambda_role: str = ShapeBase.NOT_SET,
    ) -> None:
        """
        Registers a new _workflow type_ and its configuration settings in the specified
        domain.

        The retention period for the workflow history is set by the RegisterDomain
        action.

        If the type already exists, then a `TypeAlreadyExists` fault is returned. You
        cannot change the configuration settings of a workflow type once it is
        registered and it must be registered as a new version.

        **Access Control**

        You can use IAM policies to control this action's access to Amazon SWF resources
        as follows:

          * Use a `Resource` element with the domain name to limit the action to only specified domains.

          * Use an `Action` element to allow or deny permission to call this action.

          * Constrain the following parameters by using a `Condition` element with the appropriate keys.

            * `defaultTaskList.name`: String constraint. The key is `swf:defaultTaskList.name`.

            * `name`: String constraint. The key is `swf:name`.

            * `version`: String constraint. The key is `swf:version`.

        If the caller doesn't have sufficient permissions to invoke the action, or the
        parameter values fall outside the specified constraints, the action fails. The
        associated event attribute's `cause` parameter is set to
        `OPERATION_NOT_PERMITTED`. For details and example IAM policies, see [Using IAM
        to Manage Access to Amazon SWF
        Workflows](http://docs.aws.amazon.com/amazonswf/latest/developerguide/swf-dev-
        iam.html) in the _Amazon SWF Developer Guide_.
        """
        if _request is None:
            _params = {}
            if domain is not ShapeBase.NOT_SET:
                _params['domain'] = domain
            if name is not ShapeBase.NOT_SET:
                _params['name'] = name
            if version is not ShapeBase.NOT_SET:
                _params['version'] = version
            if description is not ShapeBase.NOT_SET:
                _params['description'] = description
            if default_task_start_to_close_timeout is not ShapeBase.NOT_SET:
                _params['default_task_start_to_close_timeout'
                       ] = default_task_start_to_close_timeout
            if default_execution_start_to_close_timeout is not ShapeBase.NOT_SET:
                _params['default_execution_start_to_close_timeout'
                       ] = default_execution_start_to_close_timeout
            if default_task_list is not ShapeBase.NOT_SET:
                _params['default_task_list'] = default_task_list
            if default_task_priority is not ShapeBase.NOT_SET:
                _params['default_task_priority'] = default_task_priority
            if default_child_policy is not ShapeBase.NOT_SET:
                _params['default_child_policy'] = default_child_policy
            if default_lambda_role is not ShapeBase.NOT_SET:
                _params['default_lambda_role'] = default_lambda_role
            _request = shapes.RegisterWorkflowTypeInput(**_params)
        response = self._boto_client.register_workflow_type(
            **_request.to_boto()
        )

    def request_cancel_workflow_execution(
        self,
        _request: shapes.RequestCancelWorkflowExecutionInput = None,
        *,
        domain: str,
        workflow_id: str,
        run_id: str = ShapeBase.NOT_SET,
    ) -> None:
        """
        Records a `WorkflowExecutionCancelRequested` event in the currently running
        workflow execution identified by the given domain, workflowId, and runId. This
        logically requests the cancellation of the workflow execution as a whole. It is
        up to the decider to take appropriate actions when it receives an execution
        history with this event.

        If the runId isn't specified, the `WorkflowExecutionCancelRequested` event is
        recorded in the history of the current open workflow execution with the
        specified workflowId in the domain.

        Because this action allows the workflow to properly clean up and gracefully
        close, it should be used instead of TerminateWorkflowExecution when possible.

        **Access Control**

        You can use IAM policies to control this action's access to Amazon SWF resources
        as follows:

          * Use a `Resource` element with the domain name to limit the action to only specified domains.

          * Use an `Action` element to allow or deny permission to call this action.

          * You cannot use an IAM policy to constrain this action's parameters.

        If the caller doesn't have sufficient permissions to invoke the action, or the
        parameter values fall outside the specified constraints, the action fails. The
        associated event attribute's `cause` parameter is set to
        `OPERATION_NOT_PERMITTED`. For details and example IAM policies, see [Using IAM
        to Manage Access to Amazon SWF
        Workflows](http://docs.aws.amazon.com/amazonswf/latest/developerguide/swf-dev-
        iam.html) in the _Amazon SWF Developer Guide_.
        """
        if _request is None:
            _params = {}
            if domain is not ShapeBase.NOT_SET:
                _params['domain'] = domain
            if workflow_id is not ShapeBase.NOT_SET:
                _params['workflow_id'] = workflow_id
            if run_id is not ShapeBase.NOT_SET:
                _params['run_id'] = run_id
            _request = shapes.RequestCancelWorkflowExecutionInput(**_params)
        response = self._boto_client.request_cancel_workflow_execution(
            **_request.to_boto()
        )

    def respond_activity_task_canceled(
        self,
        _request: shapes.RespondActivityTaskCanceledInput = None,
        *,
        task_token: str,
        details: str = ShapeBase.NOT_SET,
    ) -> None:
        """
        Used by workers to tell the service that the ActivityTask identified by the
        `taskToken` was successfully canceled. Additional `details` can be provided
        using the `details` argument.

        These `details` (if provided) appear in the `ActivityTaskCanceled` event added
        to the workflow history.

        Only use this operation if the `canceled` flag of a RecordActivityTaskHeartbeat
        request returns `true` and if the activity can be safely undone or abandoned.

        A task is considered open from the time that it is scheduled until it is closed.
        Therefore a task is reported as open while a worker is processing it. A task is
        closed after it has been specified in a call to RespondActivityTaskCompleted,
        RespondActivityTaskCanceled, RespondActivityTaskFailed, or the task has [timed
        out](http://docs.aws.amazon.com/amazonswf/latest/developerguide/swf-dg-
        basic.html#swf-dev-timeout-types).

        **Access Control**

        You can use IAM policies to control this action's access to Amazon SWF resources
        as follows:

          * Use a `Resource` element with the domain name to limit the action to only specified domains.

          * Use an `Action` element to allow or deny permission to call this action.

          * You cannot use an IAM policy to constrain this action's parameters.

        If the caller doesn't have sufficient permissions to invoke the action, or the
        parameter values fall outside the specified constraints, the action fails. The
        associated event attribute's `cause` parameter is set to
        `OPERATION_NOT_PERMITTED`. For details and example IAM policies, see [Using IAM
        to Manage Access to Amazon SWF
        Workflows](http://docs.aws.amazon.com/amazonswf/latest/developerguide/swf-dev-
        iam.html) in the _Amazon SWF Developer Guide_.
        """
        if _request is None:
            _params = {}
            if task_token is not ShapeBase.NOT_SET:
                _params['task_token'] = task_token
            if details is not ShapeBase.NOT_SET:
                _params['details'] = details
            _request = shapes.RespondActivityTaskCanceledInput(**_params)
        response = self._boto_client.respond_activity_task_canceled(
            **_request.to_boto()
        )

    def respond_activity_task_completed(
        self,
        _request: shapes.RespondActivityTaskCompletedInput = None,
        *,
        task_token: str,
        result: str = ShapeBase.NOT_SET,
    ) -> None:
        """
        Used by workers to tell the service that the ActivityTask identified by the
        `taskToken` completed successfully with a `result` (if provided). The `result`
        appears in the `ActivityTaskCompleted` event in the workflow history.

        If the requested task doesn't complete successfully, use
        RespondActivityTaskFailed instead. If the worker finds that the task is canceled
        through the `canceled` flag returned by RecordActivityTaskHeartbeat, it should
        cancel the task, clean up and then call RespondActivityTaskCanceled.

        A task is considered open from the time that it is scheduled until it is closed.
        Therefore a task is reported as open while a worker is processing it. A task is
        closed after it has been specified in a call to RespondActivityTaskCompleted,
        RespondActivityTaskCanceled, RespondActivityTaskFailed, or the task has [timed
        out](http://docs.aws.amazon.com/amazonswf/latest/developerguide/swf-dg-
        basic.html#swf-dev-timeout-types).

        **Access Control**

        You can use IAM policies to control this action's access to Amazon SWF resources
        as follows:

          * Use a `Resource` element with the domain name to limit the action to only specified domains.

          * Use an `Action` element to allow or deny permission to call this action.

          * You cannot use an IAM policy to constrain this action's parameters.

        If the caller doesn't have sufficient permissions to invoke the action, or the
        parameter values fall outside the specified constraints, the action fails. The
        associated event attribute's `cause` parameter is set to
        `OPERATION_NOT_PERMITTED`. For details and example IAM policies, see [Using IAM
        to Manage Access to Amazon SWF
        Workflows](http://docs.aws.amazon.com/amazonswf/latest/developerguide/swf-dev-
        iam.html) in the _Amazon SWF Developer Guide_.
        """
        if _request is None:
            _params = {}
            if task_token is not ShapeBase.NOT_SET:
                _params['task_token'] = task_token
            if result is not ShapeBase.NOT_SET:
                _params['result'] = result
            _request = shapes.RespondActivityTaskCompletedInput(**_params)
        response = self._boto_client.respond_activity_task_completed(
            **_request.to_boto()
        )

    def respond_activity_task_failed(
        self,
        _request: shapes.RespondActivityTaskFailedInput = None,
        *,
        task_token: str,
        reason: str = ShapeBase.NOT_SET,
        details: str = ShapeBase.NOT_SET,
    ) -> None:
        """
        Used by workers to tell the service that the ActivityTask identified by the
        `taskToken` has failed with `reason` (if specified). The `reason` and `details`
        appear in the `ActivityTaskFailed` event added to the workflow history.

        A task is considered open from the time that it is scheduled until it is closed.
        Therefore a task is reported as open while a worker is processing it. A task is
        closed after it has been specified in a call to RespondActivityTaskCompleted,
        RespondActivityTaskCanceled, RespondActivityTaskFailed, or the task has [timed
        out](http://docs.aws.amazon.com/amazonswf/latest/developerguide/swf-dg-
        basic.html#swf-dev-timeout-types).

        **Access Control**

        You can use IAM policies to control this action's access to Amazon SWF resources
        as follows:

          * Use a `Resource` element with the domain name to limit the action to only specified domains.

          * Use an `Action` element to allow or deny permission to call this action.

          * You cannot use an IAM policy to constrain this action's parameters.

        If the caller doesn't have sufficient permissions to invoke the action, or the
        parameter values fall outside the specified constraints, the action fails. The
        associated event attribute's `cause` parameter is set to
        `OPERATION_NOT_PERMITTED`. For details and example IAM policies, see [Using IAM
        to Manage Access to Amazon SWF
        Workflows](http://docs.aws.amazon.com/amazonswf/latest/developerguide/swf-dev-
        iam.html) in the _Amazon SWF Developer Guide_.
        """
        if _request is None:
            _params = {}
            if task_token is not ShapeBase.NOT_SET:
                _params['task_token'] = task_token
            if reason is not ShapeBase.NOT_SET:
                _params['reason'] = reason
            if details is not ShapeBase.NOT_SET:
                _params['details'] = details
            _request = shapes.RespondActivityTaskFailedInput(**_params)
        response = self._boto_client.respond_activity_task_failed(
            **_request.to_boto()
        )

    def respond_decision_task_completed(
        self,
        _request: shapes.RespondDecisionTaskCompletedInput = None,
        *,
        task_token: str,
        decisions: typing.List[shapes.Decision] = ShapeBase.NOT_SET,
        execution_context: str = ShapeBase.NOT_SET,
    ) -> None:
        """
        Used by deciders to tell the service that the DecisionTask identified by the
        `taskToken` has successfully completed. The `decisions` argument specifies the
        list of decisions made while processing the task.

        A `DecisionTaskCompleted` event is added to the workflow history. The
        `executionContext` specified is attached to the event in the workflow execution
        history.

        **Access Control**

        If an IAM policy grants permission to use `RespondDecisionTaskCompleted`, it can
        express permissions for the list of decisions in the `decisions` parameter. Each
        of the decisions has one or more parameters, much like a regular API call. To
        allow for policies to be as readable as possible, you can express permissions on
        decisions as if they were actual API calls, including applying conditions to
        some parameters. For more information, see [Using IAM to Manage Access to Amazon
        SWF Workflows](http://docs.aws.amazon.com/amazonswf/latest/developerguide/swf-
        dev-iam.html) in the _Amazon SWF Developer Guide_.
        """
        if _request is None:
            _params = {}
            if task_token is not ShapeBase.NOT_SET:
                _params['task_token'] = task_token
            if decisions is not ShapeBase.NOT_SET:
                _params['decisions'] = decisions
            if execution_context is not ShapeBase.NOT_SET:
                _params['execution_context'] = execution_context
            _request = shapes.RespondDecisionTaskCompletedInput(**_params)
        response = self._boto_client.respond_decision_task_completed(
            **_request.to_boto()
        )

    def signal_workflow_execution(
        self,
        _request: shapes.SignalWorkflowExecutionInput = None,
        *,
        domain: str,
        workflow_id: str,
        signal_name: str,
        run_id: str = ShapeBase.NOT_SET,
        input: str = ShapeBase.NOT_SET,
    ) -> None:
        """
        Records a `WorkflowExecutionSignaled` event in the workflow execution history
        and creates a decision task for the workflow execution identified by the given
        domain, workflowId and runId. The event is recorded with the specified user
        defined signalName and input (if provided).

        If a runId isn't specified, then the `WorkflowExecutionSignaled` event is
        recorded in the history of the current open workflow with the matching
        workflowId in the domain.

        If the specified workflow execution isn't open, this method fails with
        `UnknownResource`.

        **Access Control**

        You can use IAM policies to control this action's access to Amazon SWF resources
        as follows:

          * Use a `Resource` element with the domain name to limit the action to only specified domains.

          * Use an `Action` element to allow or deny permission to call this action.

          * You cannot use an IAM policy to constrain this action's parameters.

        If the caller doesn't have sufficient permissions to invoke the action, or the
        parameter values fall outside the specified constraints, the action fails. The
        associated event attribute's `cause` parameter is set to
        `OPERATION_NOT_PERMITTED`. For details and example IAM policies, see [Using IAM
        to Manage Access to Amazon SWF
        Workflows](http://docs.aws.amazon.com/amazonswf/latest/developerguide/swf-dev-
        iam.html) in the _Amazon SWF Developer Guide_.
        """
        if _request is None:
            _params = {}
            if domain is not ShapeBase.NOT_SET:
                _params['domain'] = domain
            if workflow_id is not ShapeBase.NOT_SET:
                _params['workflow_id'] = workflow_id
            if signal_name is not ShapeBase.NOT_SET:
                _params['signal_name'] = signal_name
            if run_id is not ShapeBase.NOT_SET:
                _params['run_id'] = run_id
            if input is not ShapeBase.NOT_SET:
                _params['input'] = input
            _request = shapes.SignalWorkflowExecutionInput(**_params)
        response = self._boto_client.signal_workflow_execution(
            **_request.to_boto()
        )

    def start_workflow_execution(
        self,
        _request: shapes.StartWorkflowExecutionInput = None,
        *,
        domain: str,
        workflow_id: str,
        workflow_type: shapes.WorkflowType,
        task_list: shapes.TaskList = ShapeBase.NOT_SET,
        task_priority: str = ShapeBase.NOT_SET,
        input: str = ShapeBase.NOT_SET,
        execution_start_to_close_timeout: str = ShapeBase.NOT_SET,
        tag_list: typing.List[str] = ShapeBase.NOT_SET,
        task_start_to_close_timeout: str = ShapeBase.NOT_SET,
        child_policy: typing.Union[str, shapes.ChildPolicy] = ShapeBase.NOT_SET,
        lambda_role: str = ShapeBase.NOT_SET,
    ) -> shapes.Run:
        """
        Starts an execution of the workflow type in the specified domain using the
        provided `workflowId` and input data.

        This action returns the newly started workflow execution.

        **Access Control**

        You can use IAM policies to control this action's access to Amazon SWF resources
        as follows:

          * Use a `Resource` element with the domain name to limit the action to only specified domains.

          * Use an `Action` element to allow or deny permission to call this action.

          * Constrain the following parameters by using a `Condition` element with the appropriate keys.

            * `tagList.member.0`: The key is `swf:tagList.member.0`.

            * `tagList.member.1`: The key is `swf:tagList.member.1`.

            * `tagList.member.2`: The key is `swf:tagList.member.2`.

            * `tagList.member.3`: The key is `swf:tagList.member.3`.

            * `tagList.member.4`: The key is `swf:tagList.member.4`.

            * `taskList`: String constraint. The key is `swf:taskList.name`.

            * `workflowType.name`: String constraint. The key is `swf:workflowType.name`.

            * `workflowType.version`: String constraint. The key is `swf:workflowType.version`.

        If the caller doesn't have sufficient permissions to invoke the action, or the
        parameter values fall outside the specified constraints, the action fails. The
        associated event attribute's `cause` parameter is set to
        `OPERATION_NOT_PERMITTED`. For details and example IAM policies, see [Using IAM
        to Manage Access to Amazon SWF
        Workflows](http://docs.aws.amazon.com/amazonswf/latest/developerguide/swf-dev-
        iam.html) in the _Amazon SWF Developer Guide_.
        """
        if _request is None:
            _params = {}
            if domain is not ShapeBase.NOT_SET:
                _params['domain'] = domain
            if workflow_id is not ShapeBase.NOT_SET:
                _params['workflow_id'] = workflow_id
            if workflow_type is not ShapeBase.NOT_SET:
                _params['workflow_type'] = workflow_type
            if task_list is not ShapeBase.NOT_SET:
                _params['task_list'] = task_list
            if task_priority is not ShapeBase.NOT_SET:
                _params['task_priority'] = task_priority
            if input is not ShapeBase.NOT_SET:
                _params['input'] = input
            if execution_start_to_close_timeout is not ShapeBase.NOT_SET:
                _params['execution_start_to_close_timeout'
                       ] = execution_start_to_close_timeout
            if tag_list is not ShapeBase.NOT_SET:
                _params['tag_list'] = tag_list
            if task_start_to_close_timeout is not ShapeBase.NOT_SET:
                _params['task_start_to_close_timeout'
                       ] = task_start_to_close_timeout
            if child_policy is not ShapeBase.NOT_SET:
                _params['child_policy'] = child_policy
            if lambda_role is not ShapeBase.NOT_SET:
                _params['lambda_role'] = lambda_role
            _request = shapes.StartWorkflowExecutionInput(**_params)
        response = self._boto_client.start_workflow_execution(
            **_request.to_boto()
        )

        return shapes.Run.from_boto(response)

    def terminate_workflow_execution(
        self,
        _request: shapes.TerminateWorkflowExecutionInput = None,
        *,
        domain: str,
        workflow_id: str,
        run_id: str = ShapeBase.NOT_SET,
        reason: str = ShapeBase.NOT_SET,
        details: str = ShapeBase.NOT_SET,
        child_policy: typing.Union[str, shapes.ChildPolicy] = ShapeBase.NOT_SET,
    ) -> None:
        """
        Records a `WorkflowExecutionTerminated` event and forces closure of the workflow
        execution identified by the given domain, runId, and workflowId. The child
        policy, registered with the workflow type or specified when starting this
        execution, is applied to any open child workflow executions of this workflow
        execution.

        If the identified workflow execution was in progress, it is terminated
        immediately.

        If a runId isn't specified, then the `WorkflowExecutionTerminated` event is
        recorded in the history of the current open workflow with the matching
        workflowId in the domain.

        You should consider using RequestCancelWorkflowExecution action instead because
        it allows the workflow to gracefully close while TerminateWorkflowExecution
        doesn't.

        **Access Control**

        You can use IAM policies to control this action's access to Amazon SWF resources
        as follows:

          * Use a `Resource` element with the domain name to limit the action to only specified domains.

          * Use an `Action` element to allow or deny permission to call this action.

          * You cannot use an IAM policy to constrain this action's parameters.

        If the caller doesn't have sufficient permissions to invoke the action, or the
        parameter values fall outside the specified constraints, the action fails. The
        associated event attribute's `cause` parameter is set to
        `OPERATION_NOT_PERMITTED`. For details and example IAM policies, see [Using IAM
        to Manage Access to Amazon SWF
        Workflows](http://docs.aws.amazon.com/amazonswf/latest/developerguide/swf-dev-
        iam.html) in the _Amazon SWF Developer Guide_.
        """
        if _request is None:
            _params = {}
            if domain is not ShapeBase.NOT_SET:
                _params['domain'] = domain
            if workflow_id is not ShapeBase.NOT_SET:
                _params['workflow_id'] = workflow_id
            if run_id is not ShapeBase.NOT_SET:
                _params['run_id'] = run_id
            if reason is not ShapeBase.NOT_SET:
                _params['reason'] = reason
            if details is not ShapeBase.NOT_SET:
                _params['details'] = details
            if child_policy is not ShapeBase.NOT_SET:
                _params['child_policy'] = child_policy
            _request = shapes.TerminateWorkflowExecutionInput(**_params)
        response = self._boto_client.terminate_workflow_execution(
            **_request.to_boto()
        )
