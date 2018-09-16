import datetime
import typing
import boto3
from autoboto import ClientBase, ShapeBase, OutputShapeBase
from . import shapes


class Client(ClientBase):
    def __init__(self, *args, **kwargs):
        super().__init__("transcribe", *args, **kwargs)

    def create_vocabulary(
        self,
        _request: shapes.CreateVocabularyRequest = None,
        *,
        vocabulary_name: str,
        language_code: typing.Union[str, shapes.LanguageCode],
        phrases: typing.List[str],
    ) -> shapes.CreateVocabularyResponse:
        """
        Creates a new custom vocabulary that you can use to change the way Amazon
        Transcribe handles transcription of an audio file.
        """
        if _request is None:
            _params = {}
            if vocabulary_name is not ShapeBase.NOT_SET:
                _params['vocabulary_name'] = vocabulary_name
            if language_code is not ShapeBase.NOT_SET:
                _params['language_code'] = language_code
            if phrases is not ShapeBase.NOT_SET:
                _params['phrases'] = phrases
            _request = shapes.CreateVocabularyRequest(**_params)
        response = self._boto_client.create_vocabulary(**_request.to_boto())

        return shapes.CreateVocabularyResponse.from_boto(response)

    def delete_vocabulary(
        self,
        _request: shapes.DeleteVocabularyRequest = None,
        *,
        vocabulary_name: str,
    ) -> None:
        """
        Deletes a vocabulary from Amazon Transcribe.
        """
        if _request is None:
            _params = {}
            if vocabulary_name is not ShapeBase.NOT_SET:
                _params['vocabulary_name'] = vocabulary_name
            _request = shapes.DeleteVocabularyRequest(**_params)
        response = self._boto_client.delete_vocabulary(**_request.to_boto())

    def get_transcription_job(
        self,
        _request: shapes.GetTranscriptionJobRequest = None,
        *,
        transcription_job_name: str,
    ) -> shapes.GetTranscriptionJobResponse:
        """
        Returns information about a transcription job. To see the status of the job,
        check the `TranscriptionJobStatus` field. If the status is `COMPLETED`, the job
        is finished and you can find the results at the location specified in the
        `TranscriptionFileUri` field.
        """
        if _request is None:
            _params = {}
            if transcription_job_name is not ShapeBase.NOT_SET:
                _params['transcription_job_name'] = transcription_job_name
            _request = shapes.GetTranscriptionJobRequest(**_params)
        response = self._boto_client.get_transcription_job(**_request.to_boto())

        return shapes.GetTranscriptionJobResponse.from_boto(response)

    def get_vocabulary(
        self,
        _request: shapes.GetVocabularyRequest = None,
        *,
        vocabulary_name: str,
    ) -> shapes.GetVocabularyResponse:
        """
        Gets information about a vocabulary.
        """
        if _request is None:
            _params = {}
            if vocabulary_name is not ShapeBase.NOT_SET:
                _params['vocabulary_name'] = vocabulary_name
            _request = shapes.GetVocabularyRequest(**_params)
        response = self._boto_client.get_vocabulary(**_request.to_boto())

        return shapes.GetVocabularyResponse.from_boto(response)

    def list_transcription_jobs(
        self,
        _request: shapes.ListTranscriptionJobsRequest = None,
        *,
        status: typing.Union[str, shapes.TranscriptionJobStatus] = ShapeBase.
        NOT_SET,
        job_name_contains: str = ShapeBase.NOT_SET,
        next_token: str = ShapeBase.NOT_SET,
        max_results: int = ShapeBase.NOT_SET,
    ) -> shapes.ListTranscriptionJobsResponse:
        """
        Lists transcription jobs with the specified status.
        """
        if _request is None:
            _params = {}
            if status is not ShapeBase.NOT_SET:
                _params['status'] = status
            if job_name_contains is not ShapeBase.NOT_SET:
                _params['job_name_contains'] = job_name_contains
            if next_token is not ShapeBase.NOT_SET:
                _params['next_token'] = next_token
            if max_results is not ShapeBase.NOT_SET:
                _params['max_results'] = max_results
            _request = shapes.ListTranscriptionJobsRequest(**_params)
        response = self._boto_client.list_transcription_jobs(
            **_request.to_boto()
        )

        return shapes.ListTranscriptionJobsResponse.from_boto(response)

    def list_vocabularies(
        self,
        _request: shapes.ListVocabulariesRequest = None,
        *,
        next_token: str = ShapeBase.NOT_SET,
        max_results: int = ShapeBase.NOT_SET,
        state_equals: typing.Union[str, shapes.VocabularyState] = ShapeBase.
        NOT_SET,
        name_contains: str = ShapeBase.NOT_SET,
    ) -> shapes.ListVocabulariesResponse:
        """
        Returns a list of vocabularies that match the specified criteria. If no criteria
        are specified, returns the entire list of vocabularies.
        """
        if _request is None:
            _params = {}
            if next_token is not ShapeBase.NOT_SET:
                _params['next_token'] = next_token
            if max_results is not ShapeBase.NOT_SET:
                _params['max_results'] = max_results
            if state_equals is not ShapeBase.NOT_SET:
                _params['state_equals'] = state_equals
            if name_contains is not ShapeBase.NOT_SET:
                _params['name_contains'] = name_contains
            _request = shapes.ListVocabulariesRequest(**_params)
        response = self._boto_client.list_vocabularies(**_request.to_boto())

        return shapes.ListVocabulariesResponse.from_boto(response)

    def start_transcription_job(
        self,
        _request: shapes.StartTranscriptionJobRequest = None,
        *,
        transcription_job_name: str,
        language_code: typing.Union[str, shapes.LanguageCode],
        media_format: typing.Union[str, shapes.MediaFormat],
        media: shapes.Media,
        media_sample_rate_hertz: int = ShapeBase.NOT_SET,
        output_bucket_name: str = ShapeBase.NOT_SET,
        settings: shapes.Settings = ShapeBase.NOT_SET,
    ) -> shapes.StartTranscriptionJobResponse:
        """
        Starts an asynchronous job to transcribe speech to text.
        """
        if _request is None:
            _params = {}
            if transcription_job_name is not ShapeBase.NOT_SET:
                _params['transcription_job_name'] = transcription_job_name
            if language_code is not ShapeBase.NOT_SET:
                _params['language_code'] = language_code
            if media_format is not ShapeBase.NOT_SET:
                _params['media_format'] = media_format
            if media is not ShapeBase.NOT_SET:
                _params['media'] = media
            if media_sample_rate_hertz is not ShapeBase.NOT_SET:
                _params['media_sample_rate_hertz'] = media_sample_rate_hertz
            if output_bucket_name is not ShapeBase.NOT_SET:
                _params['output_bucket_name'] = output_bucket_name
            if settings is not ShapeBase.NOT_SET:
                _params['settings'] = settings
            _request = shapes.StartTranscriptionJobRequest(**_params)
        response = self._boto_client.start_transcription_job(
            **_request.to_boto()
        )

        return shapes.StartTranscriptionJobResponse.from_boto(response)

    def update_vocabulary(
        self,
        _request: shapes.UpdateVocabularyRequest = None,
        *,
        vocabulary_name: str,
        language_code: typing.Union[str, shapes.LanguageCode],
        phrases: typing.List[str],
    ) -> shapes.UpdateVocabularyResponse:
        """
        Updates an existing vocabulary with new values. The `UpdateVocabulary` operation
        overwrites all of the existing information with the values that you provide in
        the request.
        """
        if _request is None:
            _params = {}
            if vocabulary_name is not ShapeBase.NOT_SET:
                _params['vocabulary_name'] = vocabulary_name
            if language_code is not ShapeBase.NOT_SET:
                _params['language_code'] = language_code
            if phrases is not ShapeBase.NOT_SET:
                _params['phrases'] = phrases
            _request = shapes.UpdateVocabularyRequest(**_params)
        response = self._boto_client.update_vocabulary(**_request.to_boto())

        return shapes.UpdateVocabularyResponse.from_boto(response)
