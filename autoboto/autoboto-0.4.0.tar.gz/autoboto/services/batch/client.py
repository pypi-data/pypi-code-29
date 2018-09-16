import datetime
import typing
import boto3
from autoboto import ClientBase, ShapeBase, OutputShapeBase
from . import shapes


class Client(ClientBase):
    def __init__(self, *args, **kwargs):
        super().__init__("batch", *args, **kwargs)

    def cancel_job(
        self,
        _request: shapes.CancelJobRequest = None,
        *,
        job_id: str,
        reason: str,
    ) -> shapes.CancelJobResponse:
        """
        Cancels a job in an AWS Batch job queue. Jobs that are in the `SUBMITTED`,
        `PENDING`, or `RUNNABLE` state are cancelled. Jobs that have progressed to
        `STARTING` or `RUNNING` are not cancelled (but the API operation still succeeds,
        even if no job is cancelled); these jobs must be terminated with the
        TerminateJob operation.
        """
        if _request is None:
            _params = {}
            if job_id is not ShapeBase.NOT_SET:
                _params['job_id'] = job_id
            if reason is not ShapeBase.NOT_SET:
                _params['reason'] = reason
            _request = shapes.CancelJobRequest(**_params)
        response = self._boto_client.cancel_job(**_request.to_boto())

        return shapes.CancelJobResponse.from_boto(response)

    def create_compute_environment(
        self,
        _request: shapes.CreateComputeEnvironmentRequest = None,
        *,
        compute_environment_name: str,
        type: typing.Union[str, shapes.CEType],
        service_role: str,
        state: typing.Union[str, shapes.CEState] = ShapeBase.NOT_SET,
        compute_resources: shapes.ComputeResource = ShapeBase.NOT_SET,
    ) -> shapes.CreateComputeEnvironmentResponse:
        """
        Creates an AWS Batch compute environment. You can create `MANAGED` or
        `UNMANAGED` compute environments.

        In a managed compute environment, AWS Batch manages the compute resources within
        the environment, based on the compute resources that you specify. Instances
        launched into a managed compute environment use a recent, approved version of
        the Amazon ECS-optimized AMI. You can choose to use Amazon EC2 On-Demand
        Instances in your managed compute environment, or you can use Amazon EC2 Spot
        Instances that only launch when the Spot bid price is below a specified
        percentage of the On-Demand price.

        In an unmanaged compute environment, you can manage your own compute resources.
        This provides more compute resource configuration options, such as using a
        custom AMI, but you must ensure that your AMI meets the Amazon ECS container
        instance AMI specification. For more information, see [Container Instance
        AMIs](http://docs.aws.amazon.com/AmazonECS/latest/developerguide/container_instance_AMIs.html)
        in the _Amazon Elastic Container Service Developer Guide_. After you have
        created your unmanaged compute environment, you can use the
        DescribeComputeEnvironments operation to find the Amazon ECS cluster that is
        associated with it and then manually launch your container instances into that
        Amazon ECS cluster. For more information, see [Launching an Amazon ECS Container
        Instance](http://docs.aws.amazon.com/AmazonECS/latest/developerguide/launch_container_instance.html)
        in the _Amazon Elastic Container Service Developer Guide_.
        """
        if _request is None:
            _params = {}
            if compute_environment_name is not ShapeBase.NOT_SET:
                _params['compute_environment_name'] = compute_environment_name
            if type is not ShapeBase.NOT_SET:
                _params['type'] = type
            if service_role is not ShapeBase.NOT_SET:
                _params['service_role'] = service_role
            if state is not ShapeBase.NOT_SET:
                _params['state'] = state
            if compute_resources is not ShapeBase.NOT_SET:
                _params['compute_resources'] = compute_resources
            _request = shapes.CreateComputeEnvironmentRequest(**_params)
        response = self._boto_client.create_compute_environment(
            **_request.to_boto()
        )

        return shapes.CreateComputeEnvironmentResponse.from_boto(response)

    def create_job_queue(
        self,
        _request: shapes.CreateJobQueueRequest = None,
        *,
        job_queue_name: str,
        priority: int,
        compute_environment_order: typing.List[shapes.ComputeEnvironmentOrder],
        state: typing.Union[str, shapes.JQState] = ShapeBase.NOT_SET,
    ) -> shapes.CreateJobQueueResponse:
        """
        Creates an AWS Batch job queue. When you create a job queue, you associate one
        or more compute environments to the queue and assign an order of preference for
        the compute environments.

        You also set a priority to the job queue that determines the order in which the
        AWS Batch scheduler places jobs onto its associated compute environments. For
        example, if a compute environment is associated with more than one job queue,
        the job queue with a higher priority is given preference for scheduling jobs to
        that compute environment.
        """
        if _request is None:
            _params = {}
            if job_queue_name is not ShapeBase.NOT_SET:
                _params['job_queue_name'] = job_queue_name
            if priority is not ShapeBase.NOT_SET:
                _params['priority'] = priority
            if compute_environment_order is not ShapeBase.NOT_SET:
                _params['compute_environment_order'] = compute_environment_order
            if state is not ShapeBase.NOT_SET:
                _params['state'] = state
            _request = shapes.CreateJobQueueRequest(**_params)
        response = self._boto_client.create_job_queue(**_request.to_boto())

        return shapes.CreateJobQueueResponse.from_boto(response)

    def delete_compute_environment(
        self,
        _request: shapes.DeleteComputeEnvironmentRequest = None,
        *,
        compute_environment: str,
    ) -> shapes.DeleteComputeEnvironmentResponse:
        """
        Deletes an AWS Batch compute environment.

        Before you can delete a compute environment, you must set its state to
        `DISABLED` with the UpdateComputeEnvironment API operation and disassociate it
        from any job queues with the UpdateJobQueue API operation.
        """
        if _request is None:
            _params = {}
            if compute_environment is not ShapeBase.NOT_SET:
                _params['compute_environment'] = compute_environment
            _request = shapes.DeleteComputeEnvironmentRequest(**_params)
        response = self._boto_client.delete_compute_environment(
            **_request.to_boto()
        )

        return shapes.DeleteComputeEnvironmentResponse.from_boto(response)

    def delete_job_queue(
        self,
        _request: shapes.DeleteJobQueueRequest = None,
        *,
        job_queue: str,
    ) -> shapes.DeleteJobQueueResponse:
        """
        Deletes the specified job queue. You must first disable submissions for a queue
        with the UpdateJobQueue operation. All jobs in the queue are terminated when you
        delete a job queue.

        It is not necessary to disassociate compute environments from a queue before
        submitting a `DeleteJobQueue` request.
        """
        if _request is None:
            _params = {}
            if job_queue is not ShapeBase.NOT_SET:
                _params['job_queue'] = job_queue
            _request = shapes.DeleteJobQueueRequest(**_params)
        response = self._boto_client.delete_job_queue(**_request.to_boto())

        return shapes.DeleteJobQueueResponse.from_boto(response)

    def deregister_job_definition(
        self,
        _request: shapes.DeregisterJobDefinitionRequest = None,
        *,
        job_definition: str,
    ) -> shapes.DeregisterJobDefinitionResponse:
        """
        Deregisters an AWS Batch job definition.
        """
        if _request is None:
            _params = {}
            if job_definition is not ShapeBase.NOT_SET:
                _params['job_definition'] = job_definition
            _request = shapes.DeregisterJobDefinitionRequest(**_params)
        response = self._boto_client.deregister_job_definition(
            **_request.to_boto()
        )

        return shapes.DeregisterJobDefinitionResponse.from_boto(response)

    def describe_compute_environments(
        self,
        _request: shapes.DescribeComputeEnvironmentsRequest = None,
        *,
        compute_environments: typing.List[str] = ShapeBase.NOT_SET,
        max_results: int = ShapeBase.NOT_SET,
        next_token: str = ShapeBase.NOT_SET,
    ) -> shapes.DescribeComputeEnvironmentsResponse:
        """
        Describes one or more of your compute environments.

        If you are using an unmanaged compute environment, you can use the
        `DescribeComputeEnvironment` operation to determine the `ecsClusterArn` that you
        should launch your Amazon ECS container instances into.
        """
        if _request is None:
            _params = {}
            if compute_environments is not ShapeBase.NOT_SET:
                _params['compute_environments'] = compute_environments
            if max_results is not ShapeBase.NOT_SET:
                _params['max_results'] = max_results
            if next_token is not ShapeBase.NOT_SET:
                _params['next_token'] = next_token
            _request = shapes.DescribeComputeEnvironmentsRequest(**_params)
        response = self._boto_client.describe_compute_environments(
            **_request.to_boto()
        )

        return shapes.DescribeComputeEnvironmentsResponse.from_boto(response)

    def describe_job_definitions(
        self,
        _request: shapes.DescribeJobDefinitionsRequest = None,
        *,
        job_definitions: typing.List[str] = ShapeBase.NOT_SET,
        max_results: int = ShapeBase.NOT_SET,
        job_definition_name: str = ShapeBase.NOT_SET,
        status: str = ShapeBase.NOT_SET,
        next_token: str = ShapeBase.NOT_SET,
    ) -> shapes.DescribeJobDefinitionsResponse:
        """
        Describes a list of job definitions. You can specify a `status` (such as
        `ACTIVE`) to only return job definitions that match that status.
        """
        if _request is None:
            _params = {}
            if job_definitions is not ShapeBase.NOT_SET:
                _params['job_definitions'] = job_definitions
            if max_results is not ShapeBase.NOT_SET:
                _params['max_results'] = max_results
            if job_definition_name is not ShapeBase.NOT_SET:
                _params['job_definition_name'] = job_definition_name
            if status is not ShapeBase.NOT_SET:
                _params['status'] = status
            if next_token is not ShapeBase.NOT_SET:
                _params['next_token'] = next_token
            _request = shapes.DescribeJobDefinitionsRequest(**_params)
        response = self._boto_client.describe_job_definitions(
            **_request.to_boto()
        )

        return shapes.DescribeJobDefinitionsResponse.from_boto(response)

    def describe_job_queues(
        self,
        _request: shapes.DescribeJobQueuesRequest = None,
        *,
        job_queues: typing.List[str] = ShapeBase.NOT_SET,
        max_results: int = ShapeBase.NOT_SET,
        next_token: str = ShapeBase.NOT_SET,
    ) -> shapes.DescribeJobQueuesResponse:
        """
        Describes one or more of your job queues.
        """
        if _request is None:
            _params = {}
            if job_queues is not ShapeBase.NOT_SET:
                _params['job_queues'] = job_queues
            if max_results is not ShapeBase.NOT_SET:
                _params['max_results'] = max_results
            if next_token is not ShapeBase.NOT_SET:
                _params['next_token'] = next_token
            _request = shapes.DescribeJobQueuesRequest(**_params)
        response = self._boto_client.describe_job_queues(**_request.to_boto())

        return shapes.DescribeJobQueuesResponse.from_boto(response)

    def describe_jobs(
        self,
        _request: shapes.DescribeJobsRequest = None,
        *,
        jobs: typing.List[str],
    ) -> shapes.DescribeJobsResponse:
        """
        Describes a list of AWS Batch jobs.
        """
        if _request is None:
            _params = {}
            if jobs is not ShapeBase.NOT_SET:
                _params['jobs'] = jobs
            _request = shapes.DescribeJobsRequest(**_params)
        response = self._boto_client.describe_jobs(**_request.to_boto())

        return shapes.DescribeJobsResponse.from_boto(response)

    def list_jobs(
        self,
        _request: shapes.ListJobsRequest = None,
        *,
        job_queue: str = ShapeBase.NOT_SET,
        array_job_id: str = ShapeBase.NOT_SET,
        job_status: typing.Union[str, shapes.JobStatus] = ShapeBase.NOT_SET,
        max_results: int = ShapeBase.NOT_SET,
        next_token: str = ShapeBase.NOT_SET,
    ) -> shapes.ListJobsResponse:
        """
        Returns a list of task jobs for a specified job queue. You can filter the
        results by job status with the `jobStatus` parameter. If you do not specify a
        status, only `RUNNING` jobs are returned.
        """
        if _request is None:
            _params = {}
            if job_queue is not ShapeBase.NOT_SET:
                _params['job_queue'] = job_queue
            if array_job_id is not ShapeBase.NOT_SET:
                _params['array_job_id'] = array_job_id
            if job_status is not ShapeBase.NOT_SET:
                _params['job_status'] = job_status
            if max_results is not ShapeBase.NOT_SET:
                _params['max_results'] = max_results
            if next_token is not ShapeBase.NOT_SET:
                _params['next_token'] = next_token
            _request = shapes.ListJobsRequest(**_params)
        response = self._boto_client.list_jobs(**_request.to_boto())

        return shapes.ListJobsResponse.from_boto(response)

    def register_job_definition(
        self,
        _request: shapes.RegisterJobDefinitionRequest = None,
        *,
        job_definition_name: str,
        type: typing.Union[str, shapes.JobDefinitionType],
        parameters: typing.Dict[str, str] = ShapeBase.NOT_SET,
        container_properties: shapes.ContainerProperties = ShapeBase.NOT_SET,
        retry_strategy: shapes.RetryStrategy = ShapeBase.NOT_SET,
        timeout: shapes.JobTimeout = ShapeBase.NOT_SET,
    ) -> shapes.RegisterJobDefinitionResponse:
        """
        Registers an AWS Batch job definition.
        """
        if _request is None:
            _params = {}
            if job_definition_name is not ShapeBase.NOT_SET:
                _params['job_definition_name'] = job_definition_name
            if type is not ShapeBase.NOT_SET:
                _params['type'] = type
            if parameters is not ShapeBase.NOT_SET:
                _params['parameters'] = parameters
            if container_properties is not ShapeBase.NOT_SET:
                _params['container_properties'] = container_properties
            if retry_strategy is not ShapeBase.NOT_SET:
                _params['retry_strategy'] = retry_strategy
            if timeout is not ShapeBase.NOT_SET:
                _params['timeout'] = timeout
            _request = shapes.RegisterJobDefinitionRequest(**_params)
        response = self._boto_client.register_job_definition(
            **_request.to_boto()
        )

        return shapes.RegisterJobDefinitionResponse.from_boto(response)

    def submit_job(
        self,
        _request: shapes.SubmitJobRequest = None,
        *,
        job_name: str,
        job_queue: str,
        job_definition: str,
        array_properties: shapes.ArrayProperties = ShapeBase.NOT_SET,
        depends_on: typing.List[shapes.JobDependency] = ShapeBase.NOT_SET,
        parameters: typing.Dict[str, str] = ShapeBase.NOT_SET,
        container_overrides: shapes.ContainerOverrides = ShapeBase.NOT_SET,
        retry_strategy: shapes.RetryStrategy = ShapeBase.NOT_SET,
        timeout: shapes.JobTimeout = ShapeBase.NOT_SET,
    ) -> shapes.SubmitJobResponse:
        """
        Submits an AWS Batch job from a job definition. Parameters specified during
        SubmitJob override parameters defined in the job definition.
        """
        if _request is None:
            _params = {}
            if job_name is not ShapeBase.NOT_SET:
                _params['job_name'] = job_name
            if job_queue is not ShapeBase.NOT_SET:
                _params['job_queue'] = job_queue
            if job_definition is not ShapeBase.NOT_SET:
                _params['job_definition'] = job_definition
            if array_properties is not ShapeBase.NOT_SET:
                _params['array_properties'] = array_properties
            if depends_on is not ShapeBase.NOT_SET:
                _params['depends_on'] = depends_on
            if parameters is not ShapeBase.NOT_SET:
                _params['parameters'] = parameters
            if container_overrides is not ShapeBase.NOT_SET:
                _params['container_overrides'] = container_overrides
            if retry_strategy is not ShapeBase.NOT_SET:
                _params['retry_strategy'] = retry_strategy
            if timeout is not ShapeBase.NOT_SET:
                _params['timeout'] = timeout
            _request = shapes.SubmitJobRequest(**_params)
        response = self._boto_client.submit_job(**_request.to_boto())

        return shapes.SubmitJobResponse.from_boto(response)

    def terminate_job(
        self,
        _request: shapes.TerminateJobRequest = None,
        *,
        job_id: str,
        reason: str,
    ) -> shapes.TerminateJobResponse:
        """
        Terminates a job in a job queue. Jobs that are in the `STARTING` or `RUNNING`
        state are terminated, which causes them to transition to `FAILED`. Jobs that
        have not progressed to the `STARTING` state are cancelled.
        """
        if _request is None:
            _params = {}
            if job_id is not ShapeBase.NOT_SET:
                _params['job_id'] = job_id
            if reason is not ShapeBase.NOT_SET:
                _params['reason'] = reason
            _request = shapes.TerminateJobRequest(**_params)
        response = self._boto_client.terminate_job(**_request.to_boto())

        return shapes.TerminateJobResponse.from_boto(response)

    def update_compute_environment(
        self,
        _request: shapes.UpdateComputeEnvironmentRequest = None,
        *,
        compute_environment: str,
        state: typing.Union[str, shapes.CEState] = ShapeBase.NOT_SET,
        compute_resources: shapes.ComputeResourceUpdate = ShapeBase.NOT_SET,
        service_role: str = ShapeBase.NOT_SET,
    ) -> shapes.UpdateComputeEnvironmentResponse:
        """
        Updates an AWS Batch compute environment.
        """
        if _request is None:
            _params = {}
            if compute_environment is not ShapeBase.NOT_SET:
                _params['compute_environment'] = compute_environment
            if state is not ShapeBase.NOT_SET:
                _params['state'] = state
            if compute_resources is not ShapeBase.NOT_SET:
                _params['compute_resources'] = compute_resources
            if service_role is not ShapeBase.NOT_SET:
                _params['service_role'] = service_role
            _request = shapes.UpdateComputeEnvironmentRequest(**_params)
        response = self._boto_client.update_compute_environment(
            **_request.to_boto()
        )

        return shapes.UpdateComputeEnvironmentResponse.from_boto(response)

    def update_job_queue(
        self,
        _request: shapes.UpdateJobQueueRequest = None,
        *,
        job_queue: str,
        state: typing.Union[str, shapes.JQState] = ShapeBase.NOT_SET,
        priority: int = ShapeBase.NOT_SET,
        compute_environment_order: typing.List[shapes.ComputeEnvironmentOrder
                                              ] = ShapeBase.NOT_SET,
    ) -> shapes.UpdateJobQueueResponse:
        """
        Updates a job queue.
        """
        if _request is None:
            _params = {}
            if job_queue is not ShapeBase.NOT_SET:
                _params['job_queue'] = job_queue
            if state is not ShapeBase.NOT_SET:
                _params['state'] = state
            if priority is not ShapeBase.NOT_SET:
                _params['priority'] = priority
            if compute_environment_order is not ShapeBase.NOT_SET:
                _params['compute_environment_order'] = compute_environment_order
            _request = shapes.UpdateJobQueueRequest(**_params)
        response = self._boto_client.update_job_queue(**_request.to_boto())

        return shapes.UpdateJobQueueResponse.from_boto(response)
