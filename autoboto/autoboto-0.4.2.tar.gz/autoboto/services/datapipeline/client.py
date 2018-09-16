import datetime
import typing
import boto3
from autoboto import ClientBase, ShapeBase, OutputShapeBase
from . import shapes


class Client(ClientBase):
    def __init__(self, *args, **kwargs):
        super().__init__("datapipeline", *args, **kwargs)

    def activate_pipeline(
        self,
        _request: shapes.ActivatePipelineInput = None,
        *,
        pipeline_id: str,
        parameter_values: typing.List[shapes.ParameterValue
                                     ] = ShapeBase.NOT_SET,
        start_timestamp: datetime.datetime = ShapeBase.NOT_SET,
    ) -> shapes.ActivatePipelineOutput:
        """
        Validates the specified pipeline and starts processing pipeline tasks. If the
        pipeline does not pass validation, activation fails.

        If you need to pause the pipeline to investigate an issue with a component, such
        as a data source or script, call DeactivatePipeline.

        To activate a finished pipeline, modify the end date for the pipeline and then
        activate it.
        """
        if _request is None:
            _params = {}
            if pipeline_id is not ShapeBase.NOT_SET:
                _params['pipeline_id'] = pipeline_id
            if parameter_values is not ShapeBase.NOT_SET:
                _params['parameter_values'] = parameter_values
            if start_timestamp is not ShapeBase.NOT_SET:
                _params['start_timestamp'] = start_timestamp
            _request = shapes.ActivatePipelineInput(**_params)
        response = self._boto_client.activate_pipeline(**_request.to_boto())

        return shapes.ActivatePipelineOutput.from_boto(response)

    def add_tags(
        self,
        _request: shapes.AddTagsInput = None,
        *,
        pipeline_id: str,
        tags: typing.List[shapes.Tag],
    ) -> shapes.AddTagsOutput:
        """
        Adds or modifies tags for the specified pipeline.
        """
        if _request is None:
            _params = {}
            if pipeline_id is not ShapeBase.NOT_SET:
                _params['pipeline_id'] = pipeline_id
            if tags is not ShapeBase.NOT_SET:
                _params['tags'] = tags
            _request = shapes.AddTagsInput(**_params)
        response = self._boto_client.add_tags(**_request.to_boto())

        return shapes.AddTagsOutput.from_boto(response)

    def create_pipeline(
        self,
        _request: shapes.CreatePipelineInput = None,
        *,
        name: str,
        unique_id: str,
        description: str = ShapeBase.NOT_SET,
        tags: typing.List[shapes.Tag] = ShapeBase.NOT_SET,
    ) -> shapes.CreatePipelineOutput:
        """
        Creates a new, empty pipeline. Use PutPipelineDefinition to populate the
        pipeline.
        """
        if _request is None:
            _params = {}
            if name is not ShapeBase.NOT_SET:
                _params['name'] = name
            if unique_id is not ShapeBase.NOT_SET:
                _params['unique_id'] = unique_id
            if description is not ShapeBase.NOT_SET:
                _params['description'] = description
            if tags is not ShapeBase.NOT_SET:
                _params['tags'] = tags
            _request = shapes.CreatePipelineInput(**_params)
        response = self._boto_client.create_pipeline(**_request.to_boto())

        return shapes.CreatePipelineOutput.from_boto(response)

    def deactivate_pipeline(
        self,
        _request: shapes.DeactivatePipelineInput = None,
        *,
        pipeline_id: str,
        cancel_active: bool = ShapeBase.NOT_SET,
    ) -> shapes.DeactivatePipelineOutput:
        """
        Deactivates the specified running pipeline. The pipeline is set to the
        `DEACTIVATING` state until the deactivation process completes.

        To resume a deactivated pipeline, use ActivatePipeline. By default, the pipeline
        resumes from the last completed execution. Optionally, you can specify the date
        and time to resume the pipeline.
        """
        if _request is None:
            _params = {}
            if pipeline_id is not ShapeBase.NOT_SET:
                _params['pipeline_id'] = pipeline_id
            if cancel_active is not ShapeBase.NOT_SET:
                _params['cancel_active'] = cancel_active
            _request = shapes.DeactivatePipelineInput(**_params)
        response = self._boto_client.deactivate_pipeline(**_request.to_boto())

        return shapes.DeactivatePipelineOutput.from_boto(response)

    def delete_pipeline(
        self,
        _request: shapes.DeletePipelineInput = None,
        *,
        pipeline_id: str,
    ) -> None:
        """
        Deletes a pipeline, its pipeline definition, and its run history. AWS Data
        Pipeline attempts to cancel instances associated with the pipeline that are
        currently being processed by task runners.

        Deleting a pipeline cannot be undone. You cannot query or restore a deleted
        pipeline. To temporarily pause a pipeline instead of deleting it, call SetStatus
        with the status set to `PAUSE` on individual components. Components that are
        paused by SetStatus can be resumed.
        """
        if _request is None:
            _params = {}
            if pipeline_id is not ShapeBase.NOT_SET:
                _params['pipeline_id'] = pipeline_id
            _request = shapes.DeletePipelineInput(**_params)
        response = self._boto_client.delete_pipeline(**_request.to_boto())

    def describe_objects(
        self,
        _request: shapes.DescribeObjectsInput = None,
        *,
        pipeline_id: str,
        object_ids: typing.List[str],
        evaluate_expressions: bool = ShapeBase.NOT_SET,
        marker: str = ShapeBase.NOT_SET,
    ) -> shapes.DescribeObjectsOutput:
        """
        Gets the object definitions for a set of objects associated with the pipeline.
        Object definitions are composed of a set of fields that define the properties of
        the object.
        """
        if _request is None:
            _params = {}
            if pipeline_id is not ShapeBase.NOT_SET:
                _params['pipeline_id'] = pipeline_id
            if object_ids is not ShapeBase.NOT_SET:
                _params['object_ids'] = object_ids
            if evaluate_expressions is not ShapeBase.NOT_SET:
                _params['evaluate_expressions'] = evaluate_expressions
            if marker is not ShapeBase.NOT_SET:
                _params['marker'] = marker
            _request = shapes.DescribeObjectsInput(**_params)
        paginator = self.get_paginator("describe_objects").paginate(
            **_request.to_boto()
        )
        page_generator = (page for page in paginator)
        first_page = next(page_generator)
        result = shapes.DescribeObjectsOutput.from_boto(first_page)
        result._page_iterator = page_generator
        return result

        return shapes.DescribeObjectsOutput.from_boto(response)

    def describe_pipelines(
        self,
        _request: shapes.DescribePipelinesInput = None,
        *,
        pipeline_ids: typing.List[str],
    ) -> shapes.DescribePipelinesOutput:
        """
        Retrieves metadata about one or more pipelines. The information retrieved
        includes the name of the pipeline, the pipeline identifier, its current state,
        and the user account that owns the pipeline. Using account credentials, you can
        retrieve metadata about pipelines that you or your IAM users have created. If
        you are using an IAM user account, you can retrieve metadata about only those
        pipelines for which you have read permissions.

        To retrieve the full pipeline definition instead of metadata about the pipeline,
        call GetPipelineDefinition.
        """
        if _request is None:
            _params = {}
            if pipeline_ids is not ShapeBase.NOT_SET:
                _params['pipeline_ids'] = pipeline_ids
            _request = shapes.DescribePipelinesInput(**_params)
        response = self._boto_client.describe_pipelines(**_request.to_boto())

        return shapes.DescribePipelinesOutput.from_boto(response)

    def evaluate_expression(
        self,
        _request: shapes.EvaluateExpressionInput = None,
        *,
        pipeline_id: str,
        object_id: str,
        expression: str,
    ) -> shapes.EvaluateExpressionOutput:
        """
        Task runners call `EvaluateExpression` to evaluate a string in the context of
        the specified object. For example, a task runner can evaluate SQL queries stored
        in Amazon S3.
        """
        if _request is None:
            _params = {}
            if pipeline_id is not ShapeBase.NOT_SET:
                _params['pipeline_id'] = pipeline_id
            if object_id is not ShapeBase.NOT_SET:
                _params['object_id'] = object_id
            if expression is not ShapeBase.NOT_SET:
                _params['expression'] = expression
            _request = shapes.EvaluateExpressionInput(**_params)
        response = self._boto_client.evaluate_expression(**_request.to_boto())

        return shapes.EvaluateExpressionOutput.from_boto(response)

    def get_pipeline_definition(
        self,
        _request: shapes.GetPipelineDefinitionInput = None,
        *,
        pipeline_id: str,
        version: str = ShapeBase.NOT_SET,
    ) -> shapes.GetPipelineDefinitionOutput:
        """
        Gets the definition of the specified pipeline. You can call
        `GetPipelineDefinition` to retrieve the pipeline definition that you provided
        using PutPipelineDefinition.
        """
        if _request is None:
            _params = {}
            if pipeline_id is not ShapeBase.NOT_SET:
                _params['pipeline_id'] = pipeline_id
            if version is not ShapeBase.NOT_SET:
                _params['version'] = version
            _request = shapes.GetPipelineDefinitionInput(**_params)
        response = self._boto_client.get_pipeline_definition(
            **_request.to_boto()
        )

        return shapes.GetPipelineDefinitionOutput.from_boto(response)

    def list_pipelines(
        self,
        _request: shapes.ListPipelinesInput = None,
        *,
        marker: str = ShapeBase.NOT_SET,
    ) -> shapes.ListPipelinesOutput:
        """
        Lists the pipeline identifiers for all active pipelines that you have permission
        to access.
        """
        if _request is None:
            _params = {}
            if marker is not ShapeBase.NOT_SET:
                _params['marker'] = marker
            _request = shapes.ListPipelinesInput(**_params)
        paginator = self.get_paginator("list_pipelines").paginate(
            **_request.to_boto()
        )
        page_generator = (page for page in paginator)
        first_page = next(page_generator)
        result = shapes.ListPipelinesOutput.from_boto(first_page)
        result._page_iterator = page_generator
        return result

        return shapes.ListPipelinesOutput.from_boto(response)

    def poll_for_task(
        self,
        _request: shapes.PollForTaskInput = None,
        *,
        worker_group: str,
        hostname: str = ShapeBase.NOT_SET,
        instance_identity: shapes.InstanceIdentity = ShapeBase.NOT_SET,
    ) -> shapes.PollForTaskOutput:
        """
        Task runners call `PollForTask` to receive a task to perform from AWS Data
        Pipeline. The task runner specifies which tasks it can perform by setting a
        value for the `workerGroup` parameter. The task returned can come from any of
        the pipelines that match the `workerGroup` value passed in by the task runner
        and that was launched using the IAM user credentials specified by the task
        runner.

        If tasks are ready in the work queue, `PollForTask` returns a response
        immediately. If no tasks are available in the queue, `PollForTask` uses long-
        polling and holds on to a poll connection for up to a 90 seconds, during which
        time the first newly scheduled task is handed to the task runner. To accomodate
        this, set the socket timeout in your task runner to 90 seconds. The task runner
        should not call `PollForTask` again on the same `workerGroup` until it receives
        a response, and this can take up to 90 seconds.
        """
        if _request is None:
            _params = {}
            if worker_group is not ShapeBase.NOT_SET:
                _params['worker_group'] = worker_group
            if hostname is not ShapeBase.NOT_SET:
                _params['hostname'] = hostname
            if instance_identity is not ShapeBase.NOT_SET:
                _params['instance_identity'] = instance_identity
            _request = shapes.PollForTaskInput(**_params)
        response = self._boto_client.poll_for_task(**_request.to_boto())

        return shapes.PollForTaskOutput.from_boto(response)

    def put_pipeline_definition(
        self,
        _request: shapes.PutPipelineDefinitionInput = None,
        *,
        pipeline_id: str,
        pipeline_objects: typing.List[shapes.PipelineObject],
        parameter_objects: typing.List[shapes.ParameterObject
                                      ] = ShapeBase.NOT_SET,
        parameter_values: typing.List[shapes.ParameterValue
                                     ] = ShapeBase.NOT_SET,
    ) -> shapes.PutPipelineDefinitionOutput:
        """
        Adds tasks, schedules, and preconditions to the specified pipeline. You can use
        `PutPipelineDefinition` to populate a new pipeline.

        `PutPipelineDefinition` also validates the configuration as it adds it to the
        pipeline. Changes to the pipeline are saved unless one of the following three
        validation errors exists in the pipeline.

          1. An object is missing a name or identifier field.
          2. A string or reference field is empty.
          3. The number of objects in the pipeline exceeds the maximum allowed objects.
          4. The pipeline is in a FINISHED state.

        Pipeline object definitions are passed to the `PutPipelineDefinition` action and
        returned by the GetPipelineDefinition action.
        """
        if _request is None:
            _params = {}
            if pipeline_id is not ShapeBase.NOT_SET:
                _params['pipeline_id'] = pipeline_id
            if pipeline_objects is not ShapeBase.NOT_SET:
                _params['pipeline_objects'] = pipeline_objects
            if parameter_objects is not ShapeBase.NOT_SET:
                _params['parameter_objects'] = parameter_objects
            if parameter_values is not ShapeBase.NOT_SET:
                _params['parameter_values'] = parameter_values
            _request = shapes.PutPipelineDefinitionInput(**_params)
        response = self._boto_client.put_pipeline_definition(
            **_request.to_boto()
        )

        return shapes.PutPipelineDefinitionOutput.from_boto(response)

    def query_objects(
        self,
        _request: shapes.QueryObjectsInput = None,
        *,
        pipeline_id: str,
        sphere: str,
        query: shapes.Query = ShapeBase.NOT_SET,
        marker: str = ShapeBase.NOT_SET,
        limit: int = ShapeBase.NOT_SET,
    ) -> shapes.QueryObjectsOutput:
        """
        Queries the specified pipeline for the names of objects that match the specified
        set of conditions.
        """
        if _request is None:
            _params = {}
            if pipeline_id is not ShapeBase.NOT_SET:
                _params['pipeline_id'] = pipeline_id
            if sphere is not ShapeBase.NOT_SET:
                _params['sphere'] = sphere
            if query is not ShapeBase.NOT_SET:
                _params['query'] = query
            if marker is not ShapeBase.NOT_SET:
                _params['marker'] = marker
            if limit is not ShapeBase.NOT_SET:
                _params['limit'] = limit
            _request = shapes.QueryObjectsInput(**_params)
        paginator = self.get_paginator("query_objects").paginate(
            **_request.to_boto()
        )
        page_generator = (page for page in paginator)
        first_page = next(page_generator)
        result = shapes.QueryObjectsOutput.from_boto(first_page)
        result._page_iterator = page_generator
        return result

        return shapes.QueryObjectsOutput.from_boto(response)

    def remove_tags(
        self,
        _request: shapes.RemoveTagsInput = None,
        *,
        pipeline_id: str,
        tag_keys: typing.List[str],
    ) -> shapes.RemoveTagsOutput:
        """
        Removes existing tags from the specified pipeline.
        """
        if _request is None:
            _params = {}
            if pipeline_id is not ShapeBase.NOT_SET:
                _params['pipeline_id'] = pipeline_id
            if tag_keys is not ShapeBase.NOT_SET:
                _params['tag_keys'] = tag_keys
            _request = shapes.RemoveTagsInput(**_params)
        response = self._boto_client.remove_tags(**_request.to_boto())

        return shapes.RemoveTagsOutput.from_boto(response)

    def report_task_progress(
        self,
        _request: shapes.ReportTaskProgressInput = None,
        *,
        task_id: str,
        fields: typing.List[shapes.Field] = ShapeBase.NOT_SET,
    ) -> shapes.ReportTaskProgressOutput:
        """
        Task runners call `ReportTaskProgress` when assigned a task to acknowledge that
        it has the task. If the web service does not receive this acknowledgement within
        2 minutes, it assigns the task in a subsequent PollForTask call. After this
        initial acknowledgement, the task runner only needs to report progress every 15
        minutes to maintain its ownership of the task. You can change this reporting
        time from 15 minutes by specifying a `reportProgressTimeout` field in your
        pipeline.

        If a task runner does not report its status after 5 minutes, AWS Data Pipeline
        assumes that the task runner is unable to process the task and reassigns the
        task in a subsequent response to PollForTask. Task runners should call
        `ReportTaskProgress` every 60 seconds.
        """
        if _request is None:
            _params = {}
            if task_id is not ShapeBase.NOT_SET:
                _params['task_id'] = task_id
            if fields is not ShapeBase.NOT_SET:
                _params['fields'] = fields
            _request = shapes.ReportTaskProgressInput(**_params)
        response = self._boto_client.report_task_progress(**_request.to_boto())

        return shapes.ReportTaskProgressOutput.from_boto(response)

    def report_task_runner_heartbeat(
        self,
        _request: shapes.ReportTaskRunnerHeartbeatInput = None,
        *,
        taskrunner_id: str,
        worker_group: str = ShapeBase.NOT_SET,
        hostname: str = ShapeBase.NOT_SET,
    ) -> shapes.ReportTaskRunnerHeartbeatOutput:
        """
        Task runners call `ReportTaskRunnerHeartbeat` every 15 minutes to indicate that
        they are operational. If the AWS Data Pipeline Task Runner is launched on a
        resource managed by AWS Data Pipeline, the web service can use this call to
        detect when the task runner application has failed and restart a new instance.
        """
        if _request is None:
            _params = {}
            if taskrunner_id is not ShapeBase.NOT_SET:
                _params['taskrunner_id'] = taskrunner_id
            if worker_group is not ShapeBase.NOT_SET:
                _params['worker_group'] = worker_group
            if hostname is not ShapeBase.NOT_SET:
                _params['hostname'] = hostname
            _request = shapes.ReportTaskRunnerHeartbeatInput(**_params)
        response = self._boto_client.report_task_runner_heartbeat(
            **_request.to_boto()
        )

        return shapes.ReportTaskRunnerHeartbeatOutput.from_boto(response)

    def set_status(
        self,
        _request: shapes.SetStatusInput = None,
        *,
        pipeline_id: str,
        object_ids: typing.List[str],
        status: str,
    ) -> None:
        """
        Requests that the status of the specified physical or logical pipeline objects
        be updated in the specified pipeline. This update might not occur immediately,
        but is eventually consistent. The status that can be set depends on the type of
        object (for example, DataNode or Activity). You cannot perform this operation on
        `FINISHED` pipelines and attempting to do so returns `InvalidRequestException`.
        """
        if _request is None:
            _params = {}
            if pipeline_id is not ShapeBase.NOT_SET:
                _params['pipeline_id'] = pipeline_id
            if object_ids is not ShapeBase.NOT_SET:
                _params['object_ids'] = object_ids
            if status is not ShapeBase.NOT_SET:
                _params['status'] = status
            _request = shapes.SetStatusInput(**_params)
        response = self._boto_client.set_status(**_request.to_boto())

    def set_task_status(
        self,
        _request: shapes.SetTaskStatusInput = None,
        *,
        task_id: str,
        task_status: typing.Union[str, shapes.TaskStatus],
        error_id: str = ShapeBase.NOT_SET,
        error_message: str = ShapeBase.NOT_SET,
        error_stack_trace: str = ShapeBase.NOT_SET,
    ) -> shapes.SetTaskStatusOutput:
        """
        Task runners call `SetTaskStatus` to notify AWS Data Pipeline that a task is
        completed and provide information about the final status. A task runner makes
        this call regardless of whether the task was sucessful. A task runner does not
        need to call `SetTaskStatus` for tasks that are canceled by the web service
        during a call to ReportTaskProgress.
        """
        if _request is None:
            _params = {}
            if task_id is not ShapeBase.NOT_SET:
                _params['task_id'] = task_id
            if task_status is not ShapeBase.NOT_SET:
                _params['task_status'] = task_status
            if error_id is not ShapeBase.NOT_SET:
                _params['error_id'] = error_id
            if error_message is not ShapeBase.NOT_SET:
                _params['error_message'] = error_message
            if error_stack_trace is not ShapeBase.NOT_SET:
                _params['error_stack_trace'] = error_stack_trace
            _request = shapes.SetTaskStatusInput(**_params)
        response = self._boto_client.set_task_status(**_request.to_boto())

        return shapes.SetTaskStatusOutput.from_boto(response)

    def validate_pipeline_definition(
        self,
        _request: shapes.ValidatePipelineDefinitionInput = None,
        *,
        pipeline_id: str,
        pipeline_objects: typing.List[shapes.PipelineObject],
        parameter_objects: typing.List[shapes.ParameterObject
                                      ] = ShapeBase.NOT_SET,
        parameter_values: typing.List[shapes.ParameterValue
                                     ] = ShapeBase.NOT_SET,
    ) -> shapes.ValidatePipelineDefinitionOutput:
        """
        Validates the specified pipeline definition to ensure that it is well formed and
        can be run without error.
        """
        if _request is None:
            _params = {}
            if pipeline_id is not ShapeBase.NOT_SET:
                _params['pipeline_id'] = pipeline_id
            if pipeline_objects is not ShapeBase.NOT_SET:
                _params['pipeline_objects'] = pipeline_objects
            if parameter_objects is not ShapeBase.NOT_SET:
                _params['parameter_objects'] = parameter_objects
            if parameter_values is not ShapeBase.NOT_SET:
                _params['parameter_values'] = parameter_values
            _request = shapes.ValidatePipelineDefinitionInput(**_params)
        response = self._boto_client.validate_pipeline_definition(
            **_request.to_boto()
        )

        return shapes.ValidatePipelineDefinitionOutput.from_boto(response)
