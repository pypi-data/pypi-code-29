import datetime
import typing
import boto3
from autoboto import ClientBase, ShapeBase, OutputShapeBase
from . import shapes


class Client(ClientBase):
    def __init__(self, *args, **kwargs):
        super().__init__("elastictranscoder", *args, **kwargs)

    def cancel_job(
        self,
        _request: shapes.CancelJobRequest = None,
        *,
        id: str,
    ) -> shapes.CancelJobResponse:
        """
        The CancelJob operation cancels an unfinished job.

        You can only cancel a job that has a status of `Submitted`. To prevent a
        pipeline from starting to process a job while you're getting the job identifier,
        use UpdatePipelineStatus to temporarily pause the pipeline.
        """
        if _request is None:
            _params = {}
            if id is not ShapeBase.NOT_SET:
                _params['id'] = id
            _request = shapes.CancelJobRequest(**_params)
        response = self._boto_client.cancel_job(**_request.to_boto())

        return shapes.CancelJobResponse.from_boto(response)

    def create_job(
        self,
        _request: shapes.CreateJobRequest = None,
        *,
        pipeline_id: str,
        input: shapes.JobInput = ShapeBase.NOT_SET,
        inputs: typing.List[shapes.JobInput] = ShapeBase.NOT_SET,
        output: shapes.CreateJobOutput = ShapeBase.NOT_SET,
        outputs: typing.List[shapes.CreateJobOutput] = ShapeBase.NOT_SET,
        output_key_prefix: str = ShapeBase.NOT_SET,
        playlists: typing.List[shapes.CreateJobPlaylist] = ShapeBase.NOT_SET,
        user_metadata: typing.Dict[str, str] = ShapeBase.NOT_SET,
    ) -> shapes.CreateJobResponse:
        """
        When you create a job, Elastic Transcoder returns JSON data that includes the
        values that you specified plus information about the job that is created.

        If you have specified more than one output for your jobs (for example, one
        output for the Kindle Fire and another output for the Apple iPhone 4s), you
        currently must use the Elastic Transcoder API to list the jobs (as opposed to
        the AWS Console).
        """
        if _request is None:
            _params = {}
            if pipeline_id is not ShapeBase.NOT_SET:
                _params['pipeline_id'] = pipeline_id
            if input is not ShapeBase.NOT_SET:
                _params['input'] = input
            if inputs is not ShapeBase.NOT_SET:
                _params['inputs'] = inputs
            if output is not ShapeBase.NOT_SET:
                _params['output'] = output
            if outputs is not ShapeBase.NOT_SET:
                _params['outputs'] = outputs
            if output_key_prefix is not ShapeBase.NOT_SET:
                _params['output_key_prefix'] = output_key_prefix
            if playlists is not ShapeBase.NOT_SET:
                _params['playlists'] = playlists
            if user_metadata is not ShapeBase.NOT_SET:
                _params['user_metadata'] = user_metadata
            _request = shapes.CreateJobRequest(**_params)
        response = self._boto_client.create_job(**_request.to_boto())

        return shapes.CreateJobResponse.from_boto(response)

    def create_pipeline(
        self,
        _request: shapes.CreatePipelineRequest = None,
        *,
        name: str,
        input_bucket: str,
        role: str,
        output_bucket: str = ShapeBase.NOT_SET,
        aws_kms_key_arn: str = ShapeBase.NOT_SET,
        notifications: shapes.Notifications = ShapeBase.NOT_SET,
        content_config: shapes.PipelineOutputConfig = ShapeBase.NOT_SET,
        thumbnail_config: shapes.PipelineOutputConfig = ShapeBase.NOT_SET,
    ) -> shapes.CreatePipelineResponse:
        """
        The CreatePipeline operation creates a pipeline with settings that you specify.
        """
        if _request is None:
            _params = {}
            if name is not ShapeBase.NOT_SET:
                _params['name'] = name
            if input_bucket is not ShapeBase.NOT_SET:
                _params['input_bucket'] = input_bucket
            if role is not ShapeBase.NOT_SET:
                _params['role'] = role
            if output_bucket is not ShapeBase.NOT_SET:
                _params['output_bucket'] = output_bucket
            if aws_kms_key_arn is not ShapeBase.NOT_SET:
                _params['aws_kms_key_arn'] = aws_kms_key_arn
            if notifications is not ShapeBase.NOT_SET:
                _params['notifications'] = notifications
            if content_config is not ShapeBase.NOT_SET:
                _params['content_config'] = content_config
            if thumbnail_config is not ShapeBase.NOT_SET:
                _params['thumbnail_config'] = thumbnail_config
            _request = shapes.CreatePipelineRequest(**_params)
        response = self._boto_client.create_pipeline(**_request.to_boto())

        return shapes.CreatePipelineResponse.from_boto(response)

    def create_preset(
        self,
        _request: shapes.CreatePresetRequest = None,
        *,
        name: str,
        container: str,
        description: str = ShapeBase.NOT_SET,
        video: shapes.VideoParameters = ShapeBase.NOT_SET,
        audio: shapes.AudioParameters = ShapeBase.NOT_SET,
        thumbnails: shapes.Thumbnails = ShapeBase.NOT_SET,
    ) -> shapes.CreatePresetResponse:
        """
        The CreatePreset operation creates a preset with settings that you specify.

        Elastic Transcoder checks the CreatePreset settings to ensure that they meet
        Elastic Transcoder requirements and to determine whether they comply with H.264
        standards. If your settings are not valid for Elastic Transcoder, Elastic
        Transcoder returns an HTTP 400 response (`ValidationException`) and does not
        create the preset. If the settings are valid for Elastic Transcoder but aren't
        strictly compliant with the H.264 standard, Elastic Transcoder creates the
        preset and returns a warning message in the response. This helps you determine
        whether your settings comply with the H.264 standard while giving you greater
        flexibility with respect to the video that Elastic Transcoder produces.

        Elastic Transcoder uses the H.264 video-compression format. For more
        information, see the International Telecommunication Union publication
        _Recommendation ITU-T H.264: Advanced video coding for generic audiovisual
        services_.
        """
        if _request is None:
            _params = {}
            if name is not ShapeBase.NOT_SET:
                _params['name'] = name
            if container is not ShapeBase.NOT_SET:
                _params['container'] = container
            if description is not ShapeBase.NOT_SET:
                _params['description'] = description
            if video is not ShapeBase.NOT_SET:
                _params['video'] = video
            if audio is not ShapeBase.NOT_SET:
                _params['audio'] = audio
            if thumbnails is not ShapeBase.NOT_SET:
                _params['thumbnails'] = thumbnails
            _request = shapes.CreatePresetRequest(**_params)
        response = self._boto_client.create_preset(**_request.to_boto())

        return shapes.CreatePresetResponse.from_boto(response)

    def delete_pipeline(
        self,
        _request: shapes.DeletePipelineRequest = None,
        *,
        id: str,
    ) -> shapes.DeletePipelineResponse:
        """
        The DeletePipeline operation removes a pipeline.

        You can only delete a pipeline that has never been used or that is not currently
        in use (doesn't contain any active jobs). If the pipeline is currently in use,
        `DeletePipeline` returns an error.
        """
        if _request is None:
            _params = {}
            if id is not ShapeBase.NOT_SET:
                _params['id'] = id
            _request = shapes.DeletePipelineRequest(**_params)
        response = self._boto_client.delete_pipeline(**_request.to_boto())

        return shapes.DeletePipelineResponse.from_boto(response)

    def delete_preset(
        self,
        _request: shapes.DeletePresetRequest = None,
        *,
        id: str,
    ) -> shapes.DeletePresetResponse:
        """
        The DeletePreset operation removes a preset that you've added in an AWS region.

        You can't delete the default presets that are included with Elastic Transcoder.
        """
        if _request is None:
            _params = {}
            if id is not ShapeBase.NOT_SET:
                _params['id'] = id
            _request = shapes.DeletePresetRequest(**_params)
        response = self._boto_client.delete_preset(**_request.to_boto())

        return shapes.DeletePresetResponse.from_boto(response)

    def list_jobs_by_pipeline(
        self,
        _request: shapes.ListJobsByPipelineRequest = None,
        *,
        pipeline_id: str,
        ascending: str = ShapeBase.NOT_SET,
        page_token: str = ShapeBase.NOT_SET,
    ) -> shapes.ListJobsByPipelineResponse:
        """
        The ListJobsByPipeline operation gets a list of the jobs currently in a
        pipeline.

        Elastic Transcoder returns all of the jobs currently in the specified pipeline.
        The response body contains one element for each job that satisfies the search
        criteria.
        """
        if _request is None:
            _params = {}
            if pipeline_id is not ShapeBase.NOT_SET:
                _params['pipeline_id'] = pipeline_id
            if ascending is not ShapeBase.NOT_SET:
                _params['ascending'] = ascending
            if page_token is not ShapeBase.NOT_SET:
                _params['page_token'] = page_token
            _request = shapes.ListJobsByPipelineRequest(**_params)
        paginator = self.get_paginator("list_jobs_by_pipeline").paginate(
            **_request.to_boto()
        )
        page_generator = (page for page in paginator)
        first_page = next(page_generator)
        result = shapes.ListJobsByPipelineResponse.from_boto(first_page)
        result._page_iterator = page_generator
        return result

        return shapes.ListJobsByPipelineResponse.from_boto(response)

    def list_jobs_by_status(
        self,
        _request: shapes.ListJobsByStatusRequest = None,
        *,
        status: str,
        ascending: str = ShapeBase.NOT_SET,
        page_token: str = ShapeBase.NOT_SET,
    ) -> shapes.ListJobsByStatusResponse:
        """
        The ListJobsByStatus operation gets a list of jobs that have a specified status.
        The response body contains one element for each job that satisfies the search
        criteria.
        """
        if _request is None:
            _params = {}
            if status is not ShapeBase.NOT_SET:
                _params['status'] = status
            if ascending is not ShapeBase.NOT_SET:
                _params['ascending'] = ascending
            if page_token is not ShapeBase.NOT_SET:
                _params['page_token'] = page_token
            _request = shapes.ListJobsByStatusRequest(**_params)
        paginator = self.get_paginator("list_jobs_by_status").paginate(
            **_request.to_boto()
        )
        page_generator = (page for page in paginator)
        first_page = next(page_generator)
        result = shapes.ListJobsByStatusResponse.from_boto(first_page)
        result._page_iterator = page_generator
        return result

        return shapes.ListJobsByStatusResponse.from_boto(response)

    def list_pipelines(
        self,
        _request: shapes.ListPipelinesRequest = None,
        *,
        ascending: str = ShapeBase.NOT_SET,
        page_token: str = ShapeBase.NOT_SET,
    ) -> shapes.ListPipelinesResponse:
        """
        The ListPipelines operation gets a list of the pipelines associated with the
        current AWS account.
        """
        if _request is None:
            _params = {}
            if ascending is not ShapeBase.NOT_SET:
                _params['ascending'] = ascending
            if page_token is not ShapeBase.NOT_SET:
                _params['page_token'] = page_token
            _request = shapes.ListPipelinesRequest(**_params)
        paginator = self.get_paginator("list_pipelines").paginate(
            **_request.to_boto()
        )
        page_generator = (page for page in paginator)
        first_page = next(page_generator)
        result = shapes.ListPipelinesResponse.from_boto(first_page)
        result._page_iterator = page_generator
        return result

        return shapes.ListPipelinesResponse.from_boto(response)

    def list_presets(
        self,
        _request: shapes.ListPresetsRequest = None,
        *,
        ascending: str = ShapeBase.NOT_SET,
        page_token: str = ShapeBase.NOT_SET,
    ) -> shapes.ListPresetsResponse:
        """
        The ListPresets operation gets a list of the default presets included with
        Elastic Transcoder and the presets that you've added in an AWS region.
        """
        if _request is None:
            _params = {}
            if ascending is not ShapeBase.NOT_SET:
                _params['ascending'] = ascending
            if page_token is not ShapeBase.NOT_SET:
                _params['page_token'] = page_token
            _request = shapes.ListPresetsRequest(**_params)
        paginator = self.get_paginator("list_presets").paginate(
            **_request.to_boto()
        )
        page_generator = (page for page in paginator)
        first_page = next(page_generator)
        result = shapes.ListPresetsResponse.from_boto(first_page)
        result._page_iterator = page_generator
        return result

        return shapes.ListPresetsResponse.from_boto(response)

    def read_job(
        self,
        _request: shapes.ReadJobRequest = None,
        *,
        id: str,
    ) -> shapes.ReadJobResponse:
        """
        The ReadJob operation returns detailed information about a job.
        """
        if _request is None:
            _params = {}
            if id is not ShapeBase.NOT_SET:
                _params['id'] = id
            _request = shapes.ReadJobRequest(**_params)
        response = self._boto_client.read_job(**_request.to_boto())

        return shapes.ReadJobResponse.from_boto(response)

    def read_pipeline(
        self,
        _request: shapes.ReadPipelineRequest = None,
        *,
        id: str,
    ) -> shapes.ReadPipelineResponse:
        """
        The ReadPipeline operation gets detailed information about a pipeline.
        """
        if _request is None:
            _params = {}
            if id is not ShapeBase.NOT_SET:
                _params['id'] = id
            _request = shapes.ReadPipelineRequest(**_params)
        response = self._boto_client.read_pipeline(**_request.to_boto())

        return shapes.ReadPipelineResponse.from_boto(response)

    def read_preset(
        self,
        _request: shapes.ReadPresetRequest = None,
        *,
        id: str,
    ) -> shapes.ReadPresetResponse:
        """
        The ReadPreset operation gets detailed information about a preset.
        """
        if _request is None:
            _params = {}
            if id is not ShapeBase.NOT_SET:
                _params['id'] = id
            _request = shapes.ReadPresetRequest(**_params)
        response = self._boto_client.read_preset(**_request.to_boto())

        return shapes.ReadPresetResponse.from_boto(response)

    def test_role(
        self,
        _request: shapes.TestRoleRequest = None,
        *,
        role: str,
        input_bucket: str,
        output_bucket: str,
        topics: typing.List[str],
    ) -> shapes.TestRoleResponse:
        """
        The TestRole operation tests the IAM role used to create the pipeline.

        The `TestRole` action lets you determine whether the IAM role you are using has
        sufficient permissions to let Elastic Transcoder perform tasks associated with
        the transcoding process. The action attempts to assume the specified IAM role,
        checks read access to the input and output buckets, and tries to send a test
        notification to Amazon SNS topics that you specify.
        """
        if _request is None:
            _params = {}
            if role is not ShapeBase.NOT_SET:
                _params['role'] = role
            if input_bucket is not ShapeBase.NOT_SET:
                _params['input_bucket'] = input_bucket
            if output_bucket is not ShapeBase.NOT_SET:
                _params['output_bucket'] = output_bucket
            if topics is not ShapeBase.NOT_SET:
                _params['topics'] = topics
            _request = shapes.TestRoleRequest(**_params)
        response = self._boto_client.test_role(**_request.to_boto())

        return shapes.TestRoleResponse.from_boto(response)

    def update_pipeline(
        self,
        _request: shapes.UpdatePipelineRequest = None,
        *,
        id: str,
        name: str = ShapeBase.NOT_SET,
        input_bucket: str = ShapeBase.NOT_SET,
        role: str = ShapeBase.NOT_SET,
        aws_kms_key_arn: str = ShapeBase.NOT_SET,
        notifications: shapes.Notifications = ShapeBase.NOT_SET,
        content_config: shapes.PipelineOutputConfig = ShapeBase.NOT_SET,
        thumbnail_config: shapes.PipelineOutputConfig = ShapeBase.NOT_SET,
    ) -> shapes.UpdatePipelineResponse:
        """
        Use the `UpdatePipeline` operation to update settings for a pipeline.

        When you change pipeline settings, your changes take effect immediately. Jobs
        that you have already submitted and that Elastic Transcoder has not started to
        process are affected in addition to jobs that you submit after you change
        settings.
        """
        if _request is None:
            _params = {}
            if id is not ShapeBase.NOT_SET:
                _params['id'] = id
            if name is not ShapeBase.NOT_SET:
                _params['name'] = name
            if input_bucket is not ShapeBase.NOT_SET:
                _params['input_bucket'] = input_bucket
            if role is not ShapeBase.NOT_SET:
                _params['role'] = role
            if aws_kms_key_arn is not ShapeBase.NOT_SET:
                _params['aws_kms_key_arn'] = aws_kms_key_arn
            if notifications is not ShapeBase.NOT_SET:
                _params['notifications'] = notifications
            if content_config is not ShapeBase.NOT_SET:
                _params['content_config'] = content_config
            if thumbnail_config is not ShapeBase.NOT_SET:
                _params['thumbnail_config'] = thumbnail_config
            _request = shapes.UpdatePipelineRequest(**_params)
        response = self._boto_client.update_pipeline(**_request.to_boto())

        return shapes.UpdatePipelineResponse.from_boto(response)

    def update_pipeline_notifications(
        self,
        _request: shapes.UpdatePipelineNotificationsRequest = None,
        *,
        id: str,
        notifications: shapes.Notifications,
    ) -> shapes.UpdatePipelineNotificationsResponse:
        """
        With the UpdatePipelineNotifications operation, you can update Amazon Simple
        Notification Service (Amazon SNS) notifications for a pipeline.

        When you update notifications for a pipeline, Elastic Transcoder returns the
        values that you specified in the request.
        """
        if _request is None:
            _params = {}
            if id is not ShapeBase.NOT_SET:
                _params['id'] = id
            if notifications is not ShapeBase.NOT_SET:
                _params['notifications'] = notifications
            _request = shapes.UpdatePipelineNotificationsRequest(**_params)
        response = self._boto_client.update_pipeline_notifications(
            **_request.to_boto()
        )

        return shapes.UpdatePipelineNotificationsResponse.from_boto(response)

    def update_pipeline_status(
        self,
        _request: shapes.UpdatePipelineStatusRequest = None,
        *,
        id: str,
        status: str,
    ) -> shapes.UpdatePipelineStatusResponse:
        """
        The UpdatePipelineStatus operation pauses or reactivates a pipeline, so that the
        pipeline stops or restarts the processing of jobs.

        Changing the pipeline status is useful if you want to cancel one or more jobs.
        You can't cancel jobs after Elastic Transcoder has started processing them; if
        you pause the pipeline to which you submitted the jobs, you have more time to
        get the job IDs for the jobs that you want to cancel, and to send a CancelJob
        request.
        """
        if _request is None:
            _params = {}
            if id is not ShapeBase.NOT_SET:
                _params['id'] = id
            if status is not ShapeBase.NOT_SET:
                _params['status'] = status
            _request = shapes.UpdatePipelineStatusRequest(**_params)
        response = self._boto_client.update_pipeline_status(
            **_request.to_boto()
        )

        return shapes.UpdatePipelineStatusResponse.from_boto(response)
