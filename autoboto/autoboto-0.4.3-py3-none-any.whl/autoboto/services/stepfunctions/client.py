import datetime
import typing
import boto3
from autoboto import ClientBase, ShapeBase, OutputShapeBase
from . import shapes


class Client(ClientBase):
    def __init__(self, *args, **kwargs):
        super().__init__("stepfunctions", *args, **kwargs)

    def create_activity(
        self,
        _request: shapes.CreateActivityInput = None,
        *,
        name: str,
    ) -> shapes.CreateActivityOutput:
        """
        Creates an activity. An activity is a task which you write in any programming
        language and host on any machine which has access to AWS Step Functions.
        Activities must poll Step Functions using the `GetActivityTask` API action and
        respond using `SendTask*` API actions. This function lets Step Functions know
        the existence of your activity and returns an identifier for use in a state
        machine and when polling from the activity.
        """
        if _request is None:
            _params = {}
            if name is not ShapeBase.NOT_SET:
                _params['name'] = name
            _request = shapes.CreateActivityInput(**_params)
        response = self._boto_client.create_activity(**_request.to_boto())

        return shapes.CreateActivityOutput.from_boto(response)

    def create_state_machine(
        self,
        _request: shapes.CreateStateMachineInput = None,
        *,
        name: str,
        definition: str,
        role_arn: str,
    ) -> shapes.CreateStateMachineOutput:
        """
        Creates a state machine. A state machine consists of a collection of states that
        can do work (`Task` states), determine to which states to transition next
        (`Choice` states), stop an execution with an error (`Fail` states), and so on.
        State machines are specified using a JSON-based, structured language.
        """
        if _request is None:
            _params = {}
            if name is not ShapeBase.NOT_SET:
                _params['name'] = name
            if definition is not ShapeBase.NOT_SET:
                _params['definition'] = definition
            if role_arn is not ShapeBase.NOT_SET:
                _params['role_arn'] = role_arn
            _request = shapes.CreateStateMachineInput(**_params)
        response = self._boto_client.create_state_machine(**_request.to_boto())

        return shapes.CreateStateMachineOutput.from_boto(response)

    def delete_activity(
        self,
        _request: shapes.DeleteActivityInput = None,
        *,
        activity_arn: str,
    ) -> shapes.DeleteActivityOutput:
        """
        Deletes an activity.
        """
        if _request is None:
            _params = {}
            if activity_arn is not ShapeBase.NOT_SET:
                _params['activity_arn'] = activity_arn
            _request = shapes.DeleteActivityInput(**_params)
        response = self._boto_client.delete_activity(**_request.to_boto())

        return shapes.DeleteActivityOutput.from_boto(response)

    def delete_state_machine(
        self,
        _request: shapes.DeleteStateMachineInput = None,
        *,
        state_machine_arn: str,
    ) -> shapes.DeleteStateMachineOutput:
        """
        Deletes a state machine. This is an asynchronous operation: It sets the state
        machine's status to `DELETING` and begins the deletion process. Each state
        machine execution is deleted the next time it makes a state transition.

        The state machine itself is deleted after all executions are completed or
        deleted.
        """
        if _request is None:
            _params = {}
            if state_machine_arn is not ShapeBase.NOT_SET:
                _params['state_machine_arn'] = state_machine_arn
            _request = shapes.DeleteStateMachineInput(**_params)
        response = self._boto_client.delete_state_machine(**_request.to_boto())

        return shapes.DeleteStateMachineOutput.from_boto(response)

    def describe_activity(
        self,
        _request: shapes.DescribeActivityInput = None,
        *,
        activity_arn: str,
    ) -> shapes.DescribeActivityOutput:
        """
        Describes an activity.
        """
        if _request is None:
            _params = {}
            if activity_arn is not ShapeBase.NOT_SET:
                _params['activity_arn'] = activity_arn
            _request = shapes.DescribeActivityInput(**_params)
        response = self._boto_client.describe_activity(**_request.to_boto())

        return shapes.DescribeActivityOutput.from_boto(response)

    def describe_execution(
        self,
        _request: shapes.DescribeExecutionInput = None,
        *,
        execution_arn: str,
    ) -> shapes.DescribeExecutionOutput:
        """
        Describes an execution.
        """
        if _request is None:
            _params = {}
            if execution_arn is not ShapeBase.NOT_SET:
                _params['execution_arn'] = execution_arn
            _request = shapes.DescribeExecutionInput(**_params)
        response = self._boto_client.describe_execution(**_request.to_boto())

        return shapes.DescribeExecutionOutput.from_boto(response)

    def describe_state_machine(
        self,
        _request: shapes.DescribeStateMachineInput = None,
        *,
        state_machine_arn: str,
    ) -> shapes.DescribeStateMachineOutput:
        """
        Describes a state machine.
        """
        if _request is None:
            _params = {}
            if state_machine_arn is not ShapeBase.NOT_SET:
                _params['state_machine_arn'] = state_machine_arn
            _request = shapes.DescribeStateMachineInput(**_params)
        response = self._boto_client.describe_state_machine(
            **_request.to_boto()
        )

        return shapes.DescribeStateMachineOutput.from_boto(response)

    def describe_state_machine_for_execution(
        self,
        _request: shapes.DescribeStateMachineForExecutionInput = None,
        *,
        execution_arn: str,
    ) -> shapes.DescribeStateMachineForExecutionOutput:
        """
        Describes the state machine associated with a specific execution.
        """
        if _request is None:
            _params = {}
            if execution_arn is not ShapeBase.NOT_SET:
                _params['execution_arn'] = execution_arn
            _request = shapes.DescribeStateMachineForExecutionInput(**_params)
        response = self._boto_client.describe_state_machine_for_execution(
            **_request.to_boto()
        )

        return shapes.DescribeStateMachineForExecutionOutput.from_boto(response)

    def get_activity_task(
        self,
        _request: shapes.GetActivityTaskInput = None,
        *,
        activity_arn: str,
        worker_name: str = ShapeBase.NOT_SET,
    ) -> shapes.GetActivityTaskOutput:
        """
        Used by workers to retrieve a task (with the specified activity ARN) which has
        been scheduled for execution by a running state machine. This initiates a long
        poll, where the service holds the HTTP connection open and responds as soon as a
        task becomes available (i.e. an execution of a task of this type is needed.) The
        maximum time the service holds on to the request before responding is 60
        seconds. If no task is available within 60 seconds, the poll returns a
        `taskToken` with a null string.

        Workers should set their client side socket timeout to at least 65 seconds (5
        seconds higher than the maximum time the service may hold the poll request).
        """
        if _request is None:
            _params = {}
            if activity_arn is not ShapeBase.NOT_SET:
                _params['activity_arn'] = activity_arn
            if worker_name is not ShapeBase.NOT_SET:
                _params['worker_name'] = worker_name
            _request = shapes.GetActivityTaskInput(**_params)
        response = self._boto_client.get_activity_task(**_request.to_boto())

        return shapes.GetActivityTaskOutput.from_boto(response)

    def get_execution_history(
        self,
        _request: shapes.GetExecutionHistoryInput = None,
        *,
        execution_arn: str,
        max_results: int = ShapeBase.NOT_SET,
        reverse_order: bool = ShapeBase.NOT_SET,
        next_token: str = ShapeBase.NOT_SET,
    ) -> shapes.GetExecutionHistoryOutput:
        """
        Returns the history of the specified execution as a list of events. By default,
        the results are returned in ascending order of the `timeStamp` of the events.
        Use the `reverseOrder` parameter to get the latest events first.

        If a `nextToken` is returned by a previous call, there are more results
        available. To retrieve the next page of results, make the call again using the
        returned token in `nextToken`. Keep all other arguments unchanged.
        """
        if _request is None:
            _params = {}
            if execution_arn is not ShapeBase.NOT_SET:
                _params['execution_arn'] = execution_arn
            if max_results is not ShapeBase.NOT_SET:
                _params['max_results'] = max_results
            if reverse_order is not ShapeBase.NOT_SET:
                _params['reverse_order'] = reverse_order
            if next_token is not ShapeBase.NOT_SET:
                _params['next_token'] = next_token
            _request = shapes.GetExecutionHistoryInput(**_params)
        paginator = self.get_paginator("get_execution_history").paginate(
            **_request.to_boto()
        )
        page_generator = (page for page in paginator)
        first_page = next(page_generator)
        result = shapes.GetExecutionHistoryOutput.from_boto(first_page)
        result._page_iterator = page_generator
        return result

        return shapes.GetExecutionHistoryOutput.from_boto(response)

    def list_activities(
        self,
        _request: shapes.ListActivitiesInput = None,
        *,
        max_results: int = ShapeBase.NOT_SET,
        next_token: str = ShapeBase.NOT_SET,
    ) -> shapes.ListActivitiesOutput:
        """
        Lists the existing activities.

        If a `nextToken` is returned by a previous call, there are more results
        available. To retrieve the next page of results, make the call again using the
        returned token in `nextToken`. Keep all other arguments unchanged.
        """
        if _request is None:
            _params = {}
            if max_results is not ShapeBase.NOT_SET:
                _params['max_results'] = max_results
            if next_token is not ShapeBase.NOT_SET:
                _params['next_token'] = next_token
            _request = shapes.ListActivitiesInput(**_params)
        paginator = self.get_paginator("list_activities").paginate(
            **_request.to_boto()
        )
        page_generator = (page for page in paginator)
        first_page = next(page_generator)
        result = shapes.ListActivitiesOutput.from_boto(first_page)
        result._page_iterator = page_generator
        return result

        return shapes.ListActivitiesOutput.from_boto(response)

    def list_executions(
        self,
        _request: shapes.ListExecutionsInput = None,
        *,
        state_machine_arn: str,
        status_filter: typing.Union[str, shapes.ExecutionStatus] = ShapeBase.
        NOT_SET,
        max_results: int = ShapeBase.NOT_SET,
        next_token: str = ShapeBase.NOT_SET,
    ) -> shapes.ListExecutionsOutput:
        """
        Lists the executions of a state machine that meet the filtering criteria.

        If a `nextToken` is returned by a previous call, there are more results
        available. To retrieve the next page of results, make the call again using the
        returned token in `nextToken`. Keep all other arguments unchanged.
        """
        if _request is None:
            _params = {}
            if state_machine_arn is not ShapeBase.NOT_SET:
                _params['state_machine_arn'] = state_machine_arn
            if status_filter is not ShapeBase.NOT_SET:
                _params['status_filter'] = status_filter
            if max_results is not ShapeBase.NOT_SET:
                _params['max_results'] = max_results
            if next_token is not ShapeBase.NOT_SET:
                _params['next_token'] = next_token
            _request = shapes.ListExecutionsInput(**_params)
        paginator = self.get_paginator("list_executions").paginate(
            **_request.to_boto()
        )
        page_generator = (page for page in paginator)
        first_page = next(page_generator)
        result = shapes.ListExecutionsOutput.from_boto(first_page)
        result._page_iterator = page_generator
        return result

        return shapes.ListExecutionsOutput.from_boto(response)

    def list_state_machines(
        self,
        _request: shapes.ListStateMachinesInput = None,
        *,
        max_results: int = ShapeBase.NOT_SET,
        next_token: str = ShapeBase.NOT_SET,
    ) -> shapes.ListStateMachinesOutput:
        """
        Lists the existing state machines.

        If a `nextToken` is returned by a previous call, there are more results
        available. To retrieve the next page of results, make the call again using the
        returned token in `nextToken`. Keep all other arguments unchanged.
        """
        if _request is None:
            _params = {}
            if max_results is not ShapeBase.NOT_SET:
                _params['max_results'] = max_results
            if next_token is not ShapeBase.NOT_SET:
                _params['next_token'] = next_token
            _request = shapes.ListStateMachinesInput(**_params)
        paginator = self.get_paginator("list_state_machines").paginate(
            **_request.to_boto()
        )
        page_generator = (page for page in paginator)
        first_page = next(page_generator)
        result = shapes.ListStateMachinesOutput.from_boto(first_page)
        result._page_iterator = page_generator
        return result

        return shapes.ListStateMachinesOutput.from_boto(response)

    def send_task_failure(
        self,
        _request: shapes.SendTaskFailureInput = None,
        *,
        task_token: str,
        error: str = ShapeBase.NOT_SET,
        cause: str = ShapeBase.NOT_SET,
    ) -> shapes.SendTaskFailureOutput:
        """
        Used by workers to report that the task identified by the `taskToken` failed.
        """
        if _request is None:
            _params = {}
            if task_token is not ShapeBase.NOT_SET:
                _params['task_token'] = task_token
            if error is not ShapeBase.NOT_SET:
                _params['error'] = error
            if cause is not ShapeBase.NOT_SET:
                _params['cause'] = cause
            _request = shapes.SendTaskFailureInput(**_params)
        response = self._boto_client.send_task_failure(**_request.to_boto())

        return shapes.SendTaskFailureOutput.from_boto(response)

    def send_task_heartbeat(
        self,
        _request: shapes.SendTaskHeartbeatInput = None,
        *,
        task_token: str,
    ) -> shapes.SendTaskHeartbeatOutput:
        """
        Used by workers to report to the service that the task represented by the
        specified `taskToken` is still making progress. This action resets the
        `Heartbeat` clock. The `Heartbeat` threshold is specified in the state machine's
        Amazon States Language definition. This action does not in itself create an
        event in the execution history. However, if the task times out, the execution
        history contains an `ActivityTimedOut` event.

        The `Timeout` of a task, defined in the state machine's Amazon States Language
        definition, is its maximum allowed duration, regardless of the number of
        SendTaskHeartbeat requests received.

        This operation is only useful for long-lived tasks to report the liveliness of
        the task.
        """
        if _request is None:
            _params = {}
            if task_token is not ShapeBase.NOT_SET:
                _params['task_token'] = task_token
            _request = shapes.SendTaskHeartbeatInput(**_params)
        response = self._boto_client.send_task_heartbeat(**_request.to_boto())

        return shapes.SendTaskHeartbeatOutput.from_boto(response)

    def send_task_success(
        self,
        _request: shapes.SendTaskSuccessInput = None,
        *,
        task_token: str,
        output: str,
    ) -> shapes.SendTaskSuccessOutput:
        """
        Used by workers to report that the task identified by the `taskToken` completed
        successfully.
        """
        if _request is None:
            _params = {}
            if task_token is not ShapeBase.NOT_SET:
                _params['task_token'] = task_token
            if output is not ShapeBase.NOT_SET:
                _params['output'] = output
            _request = shapes.SendTaskSuccessInput(**_params)
        response = self._boto_client.send_task_success(**_request.to_boto())

        return shapes.SendTaskSuccessOutput.from_boto(response)

    def start_execution(
        self,
        _request: shapes.StartExecutionInput = None,
        *,
        state_machine_arn: str,
        name: str = ShapeBase.NOT_SET,
        input: str = ShapeBase.NOT_SET,
    ) -> shapes.StartExecutionOutput:
        """
        Starts a state machine execution.
        """
        if _request is None:
            _params = {}
            if state_machine_arn is not ShapeBase.NOT_SET:
                _params['state_machine_arn'] = state_machine_arn
            if name is not ShapeBase.NOT_SET:
                _params['name'] = name
            if input is not ShapeBase.NOT_SET:
                _params['input'] = input
            _request = shapes.StartExecutionInput(**_params)
        response = self._boto_client.start_execution(**_request.to_boto())

        return shapes.StartExecutionOutput.from_boto(response)

    def stop_execution(
        self,
        _request: shapes.StopExecutionInput = None,
        *,
        execution_arn: str,
        error: str = ShapeBase.NOT_SET,
        cause: str = ShapeBase.NOT_SET,
    ) -> shapes.StopExecutionOutput:
        """
        Stops an execution.
        """
        if _request is None:
            _params = {}
            if execution_arn is not ShapeBase.NOT_SET:
                _params['execution_arn'] = execution_arn
            if error is not ShapeBase.NOT_SET:
                _params['error'] = error
            if cause is not ShapeBase.NOT_SET:
                _params['cause'] = cause
            _request = shapes.StopExecutionInput(**_params)
        response = self._boto_client.stop_execution(**_request.to_boto())

        return shapes.StopExecutionOutput.from_boto(response)

    def update_state_machine(
        self,
        _request: shapes.UpdateStateMachineInput = None,
        *,
        state_machine_arn: str,
        definition: str = ShapeBase.NOT_SET,
        role_arn: str = ShapeBase.NOT_SET,
    ) -> shapes.UpdateStateMachineOutput:
        """
        Updates an existing state machine by modifying its `definition` and/or
        `roleArn`. Running executions will continue to use the previous `definition` and
        `roleArn`.

        All `StartExecution` calls within a few seconds will use the updated
        `definition` and `roleArn`. Executions started immediately after calling
        `UpdateStateMachine` may use the previous state machine `definition` and
        `roleArn`. You must include at least one of `definition` or `roleArn` or you
        will receive a `MissingRequiredParameter` error.
        """
        if _request is None:
            _params = {}
            if state_machine_arn is not ShapeBase.NOT_SET:
                _params['state_machine_arn'] = state_machine_arn
            if definition is not ShapeBase.NOT_SET:
                _params['definition'] = definition
            if role_arn is not ShapeBase.NOT_SET:
                _params['role_arn'] = role_arn
            _request = shapes.UpdateStateMachineInput(**_params)
        response = self._boto_client.update_state_machine(**_request.to_boto())

        return shapes.UpdateStateMachineOutput.from_boto(response)
