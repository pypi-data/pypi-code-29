import datetime
import typing
import boto3
from autoboto import ClientBase, ShapeBase, OutputShapeBase
from . import shapes


class Client(ClientBase):
    def __init__(self, *args, **kwargs):
        super().__init__("codepipeline", *args, **kwargs)

    def acknowledge_job(
        self,
        _request: shapes.AcknowledgeJobInput = None,
        *,
        job_id: str,
        nonce: str,
    ) -> shapes.AcknowledgeJobOutput:
        """
        Returns information about a specified job and whether that job has been received
        by the job worker. Only used for custom actions.
        """
        if _request is None:
            _params = {}
            if job_id is not ShapeBase.NOT_SET:
                _params['job_id'] = job_id
            if nonce is not ShapeBase.NOT_SET:
                _params['nonce'] = nonce
            _request = shapes.AcknowledgeJobInput(**_params)
        response = self._boto_client.acknowledge_job(**_request.to_boto())

        return shapes.AcknowledgeJobOutput.from_boto(response)

    def acknowledge_third_party_job(
        self,
        _request: shapes.AcknowledgeThirdPartyJobInput = None,
        *,
        job_id: str,
        nonce: str,
        client_token: str,
    ) -> shapes.AcknowledgeThirdPartyJobOutput:
        """
        Confirms a job worker has received the specified job. Only used for partner
        actions.
        """
        if _request is None:
            _params = {}
            if job_id is not ShapeBase.NOT_SET:
                _params['job_id'] = job_id
            if nonce is not ShapeBase.NOT_SET:
                _params['nonce'] = nonce
            if client_token is not ShapeBase.NOT_SET:
                _params['client_token'] = client_token
            _request = shapes.AcknowledgeThirdPartyJobInput(**_params)
        response = self._boto_client.acknowledge_third_party_job(
            **_request.to_boto()
        )

        return shapes.AcknowledgeThirdPartyJobOutput.from_boto(response)

    def create_custom_action_type(
        self,
        _request: shapes.CreateCustomActionTypeInput = None,
        *,
        category: typing.Union[str, shapes.ActionCategory],
        provider: str,
        version: str,
        input_artifact_details: shapes.ArtifactDetails,
        output_artifact_details: shapes.ArtifactDetails,
        settings: shapes.ActionTypeSettings = ShapeBase.NOT_SET,
        configuration_properties: typing.List[shapes.ActionConfigurationProperty
                                             ] = ShapeBase.NOT_SET,
    ) -> shapes.CreateCustomActionTypeOutput:
        """
        Creates a new custom action that can be used in all pipelines associated with
        the AWS account. Only used for custom actions.
        """
        if _request is None:
            _params = {}
            if category is not ShapeBase.NOT_SET:
                _params['category'] = category
            if provider is not ShapeBase.NOT_SET:
                _params['provider'] = provider
            if version is not ShapeBase.NOT_SET:
                _params['version'] = version
            if input_artifact_details is not ShapeBase.NOT_SET:
                _params['input_artifact_details'] = input_artifact_details
            if output_artifact_details is not ShapeBase.NOT_SET:
                _params['output_artifact_details'] = output_artifact_details
            if settings is not ShapeBase.NOT_SET:
                _params['settings'] = settings
            if configuration_properties is not ShapeBase.NOT_SET:
                _params['configuration_properties'] = configuration_properties
            _request = shapes.CreateCustomActionTypeInput(**_params)
        response = self._boto_client.create_custom_action_type(
            **_request.to_boto()
        )

        return shapes.CreateCustomActionTypeOutput.from_boto(response)

    def create_pipeline(
        self,
        _request: shapes.CreatePipelineInput = None,
        *,
        pipeline: shapes.PipelineDeclaration,
    ) -> shapes.CreatePipelineOutput:
        """
        Creates a pipeline.
        """
        if _request is None:
            _params = {}
            if pipeline is not ShapeBase.NOT_SET:
                _params['pipeline'] = pipeline
            _request = shapes.CreatePipelineInput(**_params)
        response = self._boto_client.create_pipeline(**_request.to_boto())

        return shapes.CreatePipelineOutput.from_boto(response)

    def delete_custom_action_type(
        self,
        _request: shapes.DeleteCustomActionTypeInput = None,
        *,
        category: typing.Union[str, shapes.ActionCategory],
        provider: str,
        version: str,
    ) -> None:
        """
        Marks a custom action as deleted. PollForJobs for the custom action will fail
        after the action is marked for deletion. Only used for custom actions.

        To re-create a custom action after it has been deleted you must use a string in
        the version field that has never been used before. This string can be an
        incremented version number, for example. To restore a deleted custom action, use
        a JSON file that is identical to the deleted action, including the original
        string in the version field.
        """
        if _request is None:
            _params = {}
            if category is not ShapeBase.NOT_SET:
                _params['category'] = category
            if provider is not ShapeBase.NOT_SET:
                _params['provider'] = provider
            if version is not ShapeBase.NOT_SET:
                _params['version'] = version
            _request = shapes.DeleteCustomActionTypeInput(**_params)
        response = self._boto_client.delete_custom_action_type(
            **_request.to_boto()
        )

    def delete_pipeline(
        self,
        _request: shapes.DeletePipelineInput = None,
        *,
        name: str,
    ) -> None:
        """
        Deletes the specified pipeline.
        """
        if _request is None:
            _params = {}
            if name is not ShapeBase.NOT_SET:
                _params['name'] = name
            _request = shapes.DeletePipelineInput(**_params)
        response = self._boto_client.delete_pipeline(**_request.to_boto())

    def delete_webhook(
        self,
        _request: shapes.DeleteWebhookInput = None,
        *,
        name: str,
    ) -> shapes.DeleteWebhookOutput:
        """
        Deletes a previously created webhook by name. Deleting the webhook stops AWS
        CodePipeline from starting a pipeline every time an external event occurs. The
        API will return successfully when trying to delete a webhook that is already
        deleted. If a deleted webhook is re-created by calling PutWebhook with the same
        name, it will have a different URL.
        """
        if _request is None:
            _params = {}
            if name is not ShapeBase.NOT_SET:
                _params['name'] = name
            _request = shapes.DeleteWebhookInput(**_params)
        response = self._boto_client.delete_webhook(**_request.to_boto())

        return shapes.DeleteWebhookOutput.from_boto(response)

    def deregister_webhook_with_third_party(
        self,
        _request: shapes.DeregisterWebhookWithThirdPartyInput = None,
        *,
        webhook_name: str = ShapeBase.NOT_SET,
    ) -> shapes.DeregisterWebhookWithThirdPartyOutput:
        """
        Removes the connection between the webhook that was created by CodePipeline and
        the external tool with events to be detected. Currently only supported for
        webhooks that target an action type of GitHub.
        """
        if _request is None:
            _params = {}
            if webhook_name is not ShapeBase.NOT_SET:
                _params['webhook_name'] = webhook_name
            _request = shapes.DeregisterWebhookWithThirdPartyInput(**_params)
        response = self._boto_client.deregister_webhook_with_third_party(
            **_request.to_boto()
        )

        return shapes.DeregisterWebhookWithThirdPartyOutput.from_boto(response)

    def disable_stage_transition(
        self,
        _request: shapes.DisableStageTransitionInput = None,
        *,
        pipeline_name: str,
        stage_name: str,
        transition_type: typing.Union[str, shapes.StageTransitionType],
        reason: str,
    ) -> None:
        """
        Prevents artifacts in a pipeline from transitioning to the next stage in the
        pipeline.
        """
        if _request is None:
            _params = {}
            if pipeline_name is not ShapeBase.NOT_SET:
                _params['pipeline_name'] = pipeline_name
            if stage_name is not ShapeBase.NOT_SET:
                _params['stage_name'] = stage_name
            if transition_type is not ShapeBase.NOT_SET:
                _params['transition_type'] = transition_type
            if reason is not ShapeBase.NOT_SET:
                _params['reason'] = reason
            _request = shapes.DisableStageTransitionInput(**_params)
        response = self._boto_client.disable_stage_transition(
            **_request.to_boto()
        )

    def enable_stage_transition(
        self,
        _request: shapes.EnableStageTransitionInput = None,
        *,
        pipeline_name: str,
        stage_name: str,
        transition_type: typing.Union[str, shapes.StageTransitionType],
    ) -> None:
        """
        Enables artifacts in a pipeline to transition to a stage in a pipeline.
        """
        if _request is None:
            _params = {}
            if pipeline_name is not ShapeBase.NOT_SET:
                _params['pipeline_name'] = pipeline_name
            if stage_name is not ShapeBase.NOT_SET:
                _params['stage_name'] = stage_name
            if transition_type is not ShapeBase.NOT_SET:
                _params['transition_type'] = transition_type
            _request = shapes.EnableStageTransitionInput(**_params)
        response = self._boto_client.enable_stage_transition(
            **_request.to_boto()
        )

    def get_job_details(
        self,
        _request: shapes.GetJobDetailsInput = None,
        *,
        job_id: str,
    ) -> shapes.GetJobDetailsOutput:
        """
        Returns information about a job. Only used for custom actions.

        When this API is called, AWS CodePipeline returns temporary credentials for the
        Amazon S3 bucket used to store artifacts for the pipeline, if the action
        requires access to that Amazon S3 bucket for input or output artifacts.
        Additionally, this API returns any secret values defined for the action.
        """
        if _request is None:
            _params = {}
            if job_id is not ShapeBase.NOT_SET:
                _params['job_id'] = job_id
            _request = shapes.GetJobDetailsInput(**_params)
        response = self._boto_client.get_job_details(**_request.to_boto())

        return shapes.GetJobDetailsOutput.from_boto(response)

    def get_pipeline(
        self,
        _request: shapes.GetPipelineInput = None,
        *,
        name: str,
        version: int = ShapeBase.NOT_SET,
    ) -> shapes.GetPipelineOutput:
        """
        Returns the metadata, structure, stages, and actions of a pipeline. Can be used
        to return the entire structure of a pipeline in JSON format, which can then be
        modified and used to update the pipeline structure with UpdatePipeline.
        """
        if _request is None:
            _params = {}
            if name is not ShapeBase.NOT_SET:
                _params['name'] = name
            if version is not ShapeBase.NOT_SET:
                _params['version'] = version
            _request = shapes.GetPipelineInput(**_params)
        response = self._boto_client.get_pipeline(**_request.to_boto())

        return shapes.GetPipelineOutput.from_boto(response)

    def get_pipeline_execution(
        self,
        _request: shapes.GetPipelineExecutionInput = None,
        *,
        pipeline_name: str,
        pipeline_execution_id: str,
    ) -> shapes.GetPipelineExecutionOutput:
        """
        Returns information about an execution of a pipeline, including details about
        artifacts, the pipeline execution ID, and the name, version, and status of the
        pipeline.
        """
        if _request is None:
            _params = {}
            if pipeline_name is not ShapeBase.NOT_SET:
                _params['pipeline_name'] = pipeline_name
            if pipeline_execution_id is not ShapeBase.NOT_SET:
                _params['pipeline_execution_id'] = pipeline_execution_id
            _request = shapes.GetPipelineExecutionInput(**_params)
        response = self._boto_client.get_pipeline_execution(
            **_request.to_boto()
        )

        return shapes.GetPipelineExecutionOutput.from_boto(response)

    def get_pipeline_state(
        self,
        _request: shapes.GetPipelineStateInput = None,
        *,
        name: str,
    ) -> shapes.GetPipelineStateOutput:
        """
        Returns information about the state of a pipeline, including the stages and
        actions.
        """
        if _request is None:
            _params = {}
            if name is not ShapeBase.NOT_SET:
                _params['name'] = name
            _request = shapes.GetPipelineStateInput(**_params)
        response = self._boto_client.get_pipeline_state(**_request.to_boto())

        return shapes.GetPipelineStateOutput.from_boto(response)

    def get_third_party_job_details(
        self,
        _request: shapes.GetThirdPartyJobDetailsInput = None,
        *,
        job_id: str,
        client_token: str,
    ) -> shapes.GetThirdPartyJobDetailsOutput:
        """
        Requests the details of a job for a third party action. Only used for partner
        actions.

        When this API is called, AWS CodePipeline returns temporary credentials for the
        Amazon S3 bucket used to store artifacts for the pipeline, if the action
        requires access to that Amazon S3 bucket for input or output artifacts.
        Additionally, this API returns any secret values defined for the action.
        """
        if _request is None:
            _params = {}
            if job_id is not ShapeBase.NOT_SET:
                _params['job_id'] = job_id
            if client_token is not ShapeBase.NOT_SET:
                _params['client_token'] = client_token
            _request = shapes.GetThirdPartyJobDetailsInput(**_params)
        response = self._boto_client.get_third_party_job_details(
            **_request.to_boto()
        )

        return shapes.GetThirdPartyJobDetailsOutput.from_boto(response)

    def list_action_types(
        self,
        _request: shapes.ListActionTypesInput = None,
        *,
        action_owner_filter: typing.Union[str, shapes.ActionOwner] = ShapeBase.
        NOT_SET,
        next_token: str = ShapeBase.NOT_SET,
    ) -> shapes.ListActionTypesOutput:
        """
        Gets a summary of all AWS CodePipeline action types associated with your
        account.
        """
        if _request is None:
            _params = {}
            if action_owner_filter is not ShapeBase.NOT_SET:
                _params['action_owner_filter'] = action_owner_filter
            if next_token is not ShapeBase.NOT_SET:
                _params['next_token'] = next_token
            _request = shapes.ListActionTypesInput(**_params)
        response = self._boto_client.list_action_types(**_request.to_boto())

        return shapes.ListActionTypesOutput.from_boto(response)

    def list_pipeline_executions(
        self,
        _request: shapes.ListPipelineExecutionsInput = None,
        *,
        pipeline_name: str,
        max_results: int = ShapeBase.NOT_SET,
        next_token: str = ShapeBase.NOT_SET,
    ) -> shapes.ListPipelineExecutionsOutput:
        """
        Gets a summary of the most recent executions for a pipeline.
        """
        if _request is None:
            _params = {}
            if pipeline_name is not ShapeBase.NOT_SET:
                _params['pipeline_name'] = pipeline_name
            if max_results is not ShapeBase.NOT_SET:
                _params['max_results'] = max_results
            if next_token is not ShapeBase.NOT_SET:
                _params['next_token'] = next_token
            _request = shapes.ListPipelineExecutionsInput(**_params)
        response = self._boto_client.list_pipeline_executions(
            **_request.to_boto()
        )

        return shapes.ListPipelineExecutionsOutput.from_boto(response)

    def list_pipelines(
        self,
        _request: shapes.ListPipelinesInput = None,
        *,
        next_token: str = ShapeBase.NOT_SET,
    ) -> shapes.ListPipelinesOutput:
        """
        Gets a summary of all of the pipelines associated with your account.
        """
        if _request is None:
            _params = {}
            if next_token is not ShapeBase.NOT_SET:
                _params['next_token'] = next_token
            _request = shapes.ListPipelinesInput(**_params)
        response = self._boto_client.list_pipelines(**_request.to_boto())

        return shapes.ListPipelinesOutput.from_boto(response)

    def list_webhooks(
        self,
        _request: shapes.ListWebhooksInput = None,
        *,
        next_token: str = ShapeBase.NOT_SET,
        max_results: int = ShapeBase.NOT_SET,
    ) -> shapes.ListWebhooksOutput:
        """
        Gets a listing of all the webhooks in this region for this account. The output
        lists all webhooks and includes the webhook URL and ARN, as well the
        configuration for each webhook.
        """
        if _request is None:
            _params = {}
            if next_token is not ShapeBase.NOT_SET:
                _params['next_token'] = next_token
            if max_results is not ShapeBase.NOT_SET:
                _params['max_results'] = max_results
            _request = shapes.ListWebhooksInput(**_params)
        response = self._boto_client.list_webhooks(**_request.to_boto())

        return shapes.ListWebhooksOutput.from_boto(response)

    def poll_for_jobs(
        self,
        _request: shapes.PollForJobsInput = None,
        *,
        action_type_id: shapes.ActionTypeId,
        max_batch_size: int = ShapeBase.NOT_SET,
        query_param: typing.Dict[str, str] = ShapeBase.NOT_SET,
    ) -> shapes.PollForJobsOutput:
        """
        Returns information about any jobs for AWS CodePipeline to act upon. PollForJobs
        is only valid for action types with "Custom" in the owner field. If the action
        type contains "AWS" or "ThirdParty" in the owner field, the PollForJobs action
        returns an error.

        When this API is called, AWS CodePipeline returns temporary credentials for the
        Amazon S3 bucket used to store artifacts for the pipeline, if the action
        requires access to that Amazon S3 bucket for input or output artifacts.
        Additionally, this API returns any secret values defined for the action.
        """
        if _request is None:
            _params = {}
            if action_type_id is not ShapeBase.NOT_SET:
                _params['action_type_id'] = action_type_id
            if max_batch_size is not ShapeBase.NOT_SET:
                _params['max_batch_size'] = max_batch_size
            if query_param is not ShapeBase.NOT_SET:
                _params['query_param'] = query_param
            _request = shapes.PollForJobsInput(**_params)
        response = self._boto_client.poll_for_jobs(**_request.to_boto())

        return shapes.PollForJobsOutput.from_boto(response)

    def poll_for_third_party_jobs(
        self,
        _request: shapes.PollForThirdPartyJobsInput = None,
        *,
        action_type_id: shapes.ActionTypeId,
        max_batch_size: int = ShapeBase.NOT_SET,
    ) -> shapes.PollForThirdPartyJobsOutput:
        """
        Determines whether there are any third party jobs for a job worker to act on.
        Only used for partner actions.

        When this API is called, AWS CodePipeline returns temporary credentials for the
        Amazon S3 bucket used to store artifacts for the pipeline, if the action
        requires access to that Amazon S3 bucket for input or output artifacts.
        """
        if _request is None:
            _params = {}
            if action_type_id is not ShapeBase.NOT_SET:
                _params['action_type_id'] = action_type_id
            if max_batch_size is not ShapeBase.NOT_SET:
                _params['max_batch_size'] = max_batch_size
            _request = shapes.PollForThirdPartyJobsInput(**_params)
        response = self._boto_client.poll_for_third_party_jobs(
            **_request.to_boto()
        )

        return shapes.PollForThirdPartyJobsOutput.from_boto(response)

    def put_action_revision(
        self,
        _request: shapes.PutActionRevisionInput = None,
        *,
        pipeline_name: str,
        stage_name: str,
        action_name: str,
        action_revision: shapes.ActionRevision,
    ) -> shapes.PutActionRevisionOutput:
        """
        Provides information to AWS CodePipeline about new revisions to a source.
        """
        if _request is None:
            _params = {}
            if pipeline_name is not ShapeBase.NOT_SET:
                _params['pipeline_name'] = pipeline_name
            if stage_name is not ShapeBase.NOT_SET:
                _params['stage_name'] = stage_name
            if action_name is not ShapeBase.NOT_SET:
                _params['action_name'] = action_name
            if action_revision is not ShapeBase.NOT_SET:
                _params['action_revision'] = action_revision
            _request = shapes.PutActionRevisionInput(**_params)
        response = self._boto_client.put_action_revision(**_request.to_boto())

        return shapes.PutActionRevisionOutput.from_boto(response)

    def put_approval_result(
        self,
        _request: shapes.PutApprovalResultInput = None,
        *,
        pipeline_name: str,
        stage_name: str,
        action_name: str,
        result: shapes.ApprovalResult,
        token: str,
    ) -> shapes.PutApprovalResultOutput:
        """
        Provides the response to a manual approval request to AWS CodePipeline. Valid
        responses include Approved and Rejected.
        """
        if _request is None:
            _params = {}
            if pipeline_name is not ShapeBase.NOT_SET:
                _params['pipeline_name'] = pipeline_name
            if stage_name is not ShapeBase.NOT_SET:
                _params['stage_name'] = stage_name
            if action_name is not ShapeBase.NOT_SET:
                _params['action_name'] = action_name
            if result is not ShapeBase.NOT_SET:
                _params['result'] = result
            if token is not ShapeBase.NOT_SET:
                _params['token'] = token
            _request = shapes.PutApprovalResultInput(**_params)
        response = self._boto_client.put_approval_result(**_request.to_boto())

        return shapes.PutApprovalResultOutput.from_boto(response)

    def put_job_failure_result(
        self,
        _request: shapes.PutJobFailureResultInput = None,
        *,
        job_id: str,
        failure_details: shapes.FailureDetails,
    ) -> None:
        """
        Represents the failure of a job as returned to the pipeline by a job worker.
        Only used for custom actions.
        """
        if _request is None:
            _params = {}
            if job_id is not ShapeBase.NOT_SET:
                _params['job_id'] = job_id
            if failure_details is not ShapeBase.NOT_SET:
                _params['failure_details'] = failure_details
            _request = shapes.PutJobFailureResultInput(**_params)
        response = self._boto_client.put_job_failure_result(
            **_request.to_boto()
        )

    def put_job_success_result(
        self,
        _request: shapes.PutJobSuccessResultInput = None,
        *,
        job_id: str,
        current_revision: shapes.CurrentRevision = ShapeBase.NOT_SET,
        continuation_token: str = ShapeBase.NOT_SET,
        execution_details: shapes.ExecutionDetails = ShapeBase.NOT_SET,
    ) -> None:
        """
        Represents the success of a job as returned to the pipeline by a job worker.
        Only used for custom actions.
        """
        if _request is None:
            _params = {}
            if job_id is not ShapeBase.NOT_SET:
                _params['job_id'] = job_id
            if current_revision is not ShapeBase.NOT_SET:
                _params['current_revision'] = current_revision
            if continuation_token is not ShapeBase.NOT_SET:
                _params['continuation_token'] = continuation_token
            if execution_details is not ShapeBase.NOT_SET:
                _params['execution_details'] = execution_details
            _request = shapes.PutJobSuccessResultInput(**_params)
        response = self._boto_client.put_job_success_result(
            **_request.to_boto()
        )

    def put_third_party_job_failure_result(
        self,
        _request: shapes.PutThirdPartyJobFailureResultInput = None,
        *,
        job_id: str,
        client_token: str,
        failure_details: shapes.FailureDetails,
    ) -> None:
        """
        Represents the failure of a third party job as returned to the pipeline by a job
        worker. Only used for partner actions.
        """
        if _request is None:
            _params = {}
            if job_id is not ShapeBase.NOT_SET:
                _params['job_id'] = job_id
            if client_token is not ShapeBase.NOT_SET:
                _params['client_token'] = client_token
            if failure_details is not ShapeBase.NOT_SET:
                _params['failure_details'] = failure_details
            _request = shapes.PutThirdPartyJobFailureResultInput(**_params)
        response = self._boto_client.put_third_party_job_failure_result(
            **_request.to_boto()
        )

    def put_third_party_job_success_result(
        self,
        _request: shapes.PutThirdPartyJobSuccessResultInput = None,
        *,
        job_id: str,
        client_token: str,
        current_revision: shapes.CurrentRevision = ShapeBase.NOT_SET,
        continuation_token: str = ShapeBase.NOT_SET,
        execution_details: shapes.ExecutionDetails = ShapeBase.NOT_SET,
    ) -> None:
        """
        Represents the success of a third party job as returned to the pipeline by a job
        worker. Only used for partner actions.
        """
        if _request is None:
            _params = {}
            if job_id is not ShapeBase.NOT_SET:
                _params['job_id'] = job_id
            if client_token is not ShapeBase.NOT_SET:
                _params['client_token'] = client_token
            if current_revision is not ShapeBase.NOT_SET:
                _params['current_revision'] = current_revision
            if continuation_token is not ShapeBase.NOT_SET:
                _params['continuation_token'] = continuation_token
            if execution_details is not ShapeBase.NOT_SET:
                _params['execution_details'] = execution_details
            _request = shapes.PutThirdPartyJobSuccessResultInput(**_params)
        response = self._boto_client.put_third_party_job_success_result(
            **_request.to_boto()
        )

    def put_webhook(
        self,
        _request: shapes.PutWebhookInput = None,
        *,
        webhook: shapes.WebhookDefinition,
    ) -> shapes.PutWebhookOutput:
        """
        Defines a webhook and returns a unique webhook URL generated by CodePipeline.
        This URL can be supplied to third party source hosting providers to call every
        time there's a code change. When CodePipeline receives a POST request on this
        URL, the pipeline defined in the webhook is started as long as the POST request
        satisfied the authentication and filtering requirements supplied when defining
        the webhook. RegisterWebhookWithThirdParty and DeregisterWebhookWithThirdParty
        APIs can be used to automatically configure supported third parties to call the
        generated webhook URL.
        """
        if _request is None:
            _params = {}
            if webhook is not ShapeBase.NOT_SET:
                _params['webhook'] = webhook
            _request = shapes.PutWebhookInput(**_params)
        response = self._boto_client.put_webhook(**_request.to_boto())

        return shapes.PutWebhookOutput.from_boto(response)

    def register_webhook_with_third_party(
        self,
        _request: shapes.RegisterWebhookWithThirdPartyInput = None,
        *,
        webhook_name: str = ShapeBase.NOT_SET,
    ) -> shapes.RegisterWebhookWithThirdPartyOutput:
        """
        Configures a connection between the webhook that was created and the external
        tool with events to be detected.
        """
        if _request is None:
            _params = {}
            if webhook_name is not ShapeBase.NOT_SET:
                _params['webhook_name'] = webhook_name
            _request = shapes.RegisterWebhookWithThirdPartyInput(**_params)
        response = self._boto_client.register_webhook_with_third_party(
            **_request.to_boto()
        )

        return shapes.RegisterWebhookWithThirdPartyOutput.from_boto(response)

    def retry_stage_execution(
        self,
        _request: shapes.RetryStageExecutionInput = None,
        *,
        pipeline_name: str,
        stage_name: str,
        pipeline_execution_id: str,
        retry_mode: typing.Union[str, shapes.StageRetryMode],
    ) -> shapes.RetryStageExecutionOutput:
        """
        Resumes the pipeline execution by retrying the last failed actions in a stage.
        """
        if _request is None:
            _params = {}
            if pipeline_name is not ShapeBase.NOT_SET:
                _params['pipeline_name'] = pipeline_name
            if stage_name is not ShapeBase.NOT_SET:
                _params['stage_name'] = stage_name
            if pipeline_execution_id is not ShapeBase.NOT_SET:
                _params['pipeline_execution_id'] = pipeline_execution_id
            if retry_mode is not ShapeBase.NOT_SET:
                _params['retry_mode'] = retry_mode
            _request = shapes.RetryStageExecutionInput(**_params)
        response = self._boto_client.retry_stage_execution(**_request.to_boto())

        return shapes.RetryStageExecutionOutput.from_boto(response)

    def start_pipeline_execution(
        self,
        _request: shapes.StartPipelineExecutionInput = None,
        *,
        name: str,
    ) -> shapes.StartPipelineExecutionOutput:
        """
        Starts the specified pipeline. Specifically, it begins processing the latest
        commit to the source location specified as part of the pipeline.
        """
        if _request is None:
            _params = {}
            if name is not ShapeBase.NOT_SET:
                _params['name'] = name
            _request = shapes.StartPipelineExecutionInput(**_params)
        response = self._boto_client.start_pipeline_execution(
            **_request.to_boto()
        )

        return shapes.StartPipelineExecutionOutput.from_boto(response)

    def update_pipeline(
        self,
        _request: shapes.UpdatePipelineInput = None,
        *,
        pipeline: shapes.PipelineDeclaration,
    ) -> shapes.UpdatePipelineOutput:
        """
        Updates a specified pipeline with edits or changes to its structure. Use a JSON
        file with the pipeline structure in conjunction with UpdatePipeline to provide
        the full structure of the pipeline. Updating the pipeline increases the version
        number of the pipeline by 1.
        """
        if _request is None:
            _params = {}
            if pipeline is not ShapeBase.NOT_SET:
                _params['pipeline'] = pipeline
            _request = shapes.UpdatePipelineInput(**_params)
        response = self._boto_client.update_pipeline(**_request.to_boto())

        return shapes.UpdatePipelineOutput.from_boto(response)
