import datetime
import typing
import boto3
from autoboto import ClientBase, ShapeBase, OutputShapeBase
from . import shapes


class Client(ClientBase):
    def __init__(self, *args, **kwargs):
        super().__init__("iot-jobs-data", *args, **kwargs)

    def describe_job_execution(
        self,
        _request: shapes.DescribeJobExecutionRequest = None,
        *,
        job_id: str,
        thing_name: str,
        include_job_document: bool = ShapeBase.NOT_SET,
        execution_number: int = ShapeBase.NOT_SET,
    ) -> shapes.DescribeJobExecutionResponse:
        """
        Gets details of a job execution.
        """
        if _request is None:
            _params = {}
            if job_id is not ShapeBase.NOT_SET:
                _params['job_id'] = job_id
            if thing_name is not ShapeBase.NOT_SET:
                _params['thing_name'] = thing_name
            if include_job_document is not ShapeBase.NOT_SET:
                _params['include_job_document'] = include_job_document
            if execution_number is not ShapeBase.NOT_SET:
                _params['execution_number'] = execution_number
            _request = shapes.DescribeJobExecutionRequest(**_params)
        response = self._boto_client.describe_job_execution(
            **_request.to_boto()
        )

        return shapes.DescribeJobExecutionResponse.from_boto(response)

    def get_pending_job_executions(
        self,
        _request: shapes.GetPendingJobExecutionsRequest = None,
        *,
        thing_name: str,
    ) -> shapes.GetPendingJobExecutionsResponse:
        """
        Gets the list of all jobs for a thing that are not in a terminal status.
        """
        if _request is None:
            _params = {}
            if thing_name is not ShapeBase.NOT_SET:
                _params['thing_name'] = thing_name
            _request = shapes.GetPendingJobExecutionsRequest(**_params)
        response = self._boto_client.get_pending_job_executions(
            **_request.to_boto()
        )

        return shapes.GetPendingJobExecutionsResponse.from_boto(response)

    def start_next_pending_job_execution(
        self,
        _request: shapes.StartNextPendingJobExecutionRequest = None,
        *,
        thing_name: str,
        status_details: typing.Dict[str, str] = ShapeBase.NOT_SET,
    ) -> shapes.StartNextPendingJobExecutionResponse:
        """
        Gets and starts the next pending (status IN_PROGRESS or QUEUED) job execution
        for a thing.
        """
        if _request is None:
            _params = {}
            if thing_name is not ShapeBase.NOT_SET:
                _params['thing_name'] = thing_name
            if status_details is not ShapeBase.NOT_SET:
                _params['status_details'] = status_details
            _request = shapes.StartNextPendingJobExecutionRequest(**_params)
        response = self._boto_client.start_next_pending_job_execution(
            **_request.to_boto()
        )

        return shapes.StartNextPendingJobExecutionResponse.from_boto(response)

    def update_job_execution(
        self,
        _request: shapes.UpdateJobExecutionRequest = None,
        *,
        job_id: str,
        thing_name: str,
        status: typing.Union[str, shapes.JobExecutionStatus],
        status_details: typing.Dict[str, str] = ShapeBase.NOT_SET,
        expected_version: int = ShapeBase.NOT_SET,
        include_job_execution_state: bool = ShapeBase.NOT_SET,
        include_job_document: bool = ShapeBase.NOT_SET,
        execution_number: int = ShapeBase.NOT_SET,
    ) -> shapes.UpdateJobExecutionResponse:
        """
        Updates the status of a job execution.
        """
        if _request is None:
            _params = {}
            if job_id is not ShapeBase.NOT_SET:
                _params['job_id'] = job_id
            if thing_name is not ShapeBase.NOT_SET:
                _params['thing_name'] = thing_name
            if status is not ShapeBase.NOT_SET:
                _params['status'] = status
            if status_details is not ShapeBase.NOT_SET:
                _params['status_details'] = status_details
            if expected_version is not ShapeBase.NOT_SET:
                _params['expected_version'] = expected_version
            if include_job_execution_state is not ShapeBase.NOT_SET:
                _params['include_job_execution_state'
                       ] = include_job_execution_state
            if include_job_document is not ShapeBase.NOT_SET:
                _params['include_job_document'] = include_job_document
            if execution_number is not ShapeBase.NOT_SET:
                _params['execution_number'] = execution_number
            _request = shapes.UpdateJobExecutionRequest(**_params)
        response = self._boto_client.update_job_execution(**_request.to_boto())

        return shapes.UpdateJobExecutionResponse.from_boto(response)
