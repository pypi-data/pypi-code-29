import datetime
import typing
import boto3
from autoboto import ClientBase, ShapeBase, OutputShapeBase
from . import shapes


class Client(ClientBase):
    def __init__(self, *args, **kwargs):
        super().__init__("comprehend", *args, **kwargs)

    def batch_detect_dominant_language(
        self,
        _request: shapes.BatchDetectDominantLanguageRequest = None,
        *,
        text_list: typing.List[str],
    ) -> shapes.BatchDetectDominantLanguageResponse:
        """
        Determines the dominant language of the input text for a batch of documents. For
        a list of languages that Amazon Comprehend can detect, see [Amazon Comprehend
        Supported Languages](http://docs.aws.amazon.com/comprehend/latest/dg/how-
        languages.html).
        """
        if _request is None:
            _params = {}
            if text_list is not ShapeBase.NOT_SET:
                _params['text_list'] = text_list
            _request = shapes.BatchDetectDominantLanguageRequest(**_params)
        response = self._boto_client.batch_detect_dominant_language(
            **_request.to_boto()
        )

        return shapes.BatchDetectDominantLanguageResponse.from_boto(response)

    def batch_detect_entities(
        self,
        _request: shapes.BatchDetectEntitiesRequest = None,
        *,
        text_list: typing.List[str],
        language_code: typing.Union[str, shapes.LanguageCode],
    ) -> shapes.BatchDetectEntitiesResponse:
        """
        Inspects the text of a batch of documents for named entities and returns
        information about them. For more information about named entities, see how-
        entities
        """
        if _request is None:
            _params = {}
            if text_list is not ShapeBase.NOT_SET:
                _params['text_list'] = text_list
            if language_code is not ShapeBase.NOT_SET:
                _params['language_code'] = language_code
            _request = shapes.BatchDetectEntitiesRequest(**_params)
        response = self._boto_client.batch_detect_entities(**_request.to_boto())

        return shapes.BatchDetectEntitiesResponse.from_boto(response)

    def batch_detect_key_phrases(
        self,
        _request: shapes.BatchDetectKeyPhrasesRequest = None,
        *,
        text_list: typing.List[str],
        language_code: typing.Union[str, shapes.LanguageCode],
    ) -> shapes.BatchDetectKeyPhrasesResponse:
        """
        Detects the key noun phrases found in a batch of documents.
        """
        if _request is None:
            _params = {}
            if text_list is not ShapeBase.NOT_SET:
                _params['text_list'] = text_list
            if language_code is not ShapeBase.NOT_SET:
                _params['language_code'] = language_code
            _request = shapes.BatchDetectKeyPhrasesRequest(**_params)
        response = self._boto_client.batch_detect_key_phrases(
            **_request.to_boto()
        )

        return shapes.BatchDetectKeyPhrasesResponse.from_boto(response)

    def batch_detect_sentiment(
        self,
        _request: shapes.BatchDetectSentimentRequest = None,
        *,
        text_list: typing.List[str],
        language_code: typing.Union[str, shapes.LanguageCode],
    ) -> shapes.BatchDetectSentimentResponse:
        """
        Inspects a batch of documents and returns an inference of the prevailing
        sentiment, `POSITIVE`, `NEUTRAL`, `MIXED`, or `NEGATIVE`, in each one.
        """
        if _request is None:
            _params = {}
            if text_list is not ShapeBase.NOT_SET:
                _params['text_list'] = text_list
            if language_code is not ShapeBase.NOT_SET:
                _params['language_code'] = language_code
            _request = shapes.BatchDetectSentimentRequest(**_params)
        response = self._boto_client.batch_detect_sentiment(
            **_request.to_boto()
        )

        return shapes.BatchDetectSentimentResponse.from_boto(response)

    def batch_detect_syntax(
        self,
        _request: shapes.BatchDetectSyntaxRequest = None,
        *,
        text_list: typing.List[str],
        language_code: typing.Union[str, shapes.SyntaxLanguageCode],
    ) -> shapes.BatchDetectSyntaxResponse:
        """
        Inspects the text of a batch of documents for the syntax and part of speech of
        the words in the document and returns information about them. For more
        information, see how-syntax.
        """
        if _request is None:
            _params = {}
            if text_list is not ShapeBase.NOT_SET:
                _params['text_list'] = text_list
            if language_code is not ShapeBase.NOT_SET:
                _params['language_code'] = language_code
            _request = shapes.BatchDetectSyntaxRequest(**_params)
        response = self._boto_client.batch_detect_syntax(**_request.to_boto())

        return shapes.BatchDetectSyntaxResponse.from_boto(response)

    def describe_dominant_language_detection_job(
        self,
        _request: shapes.DescribeDominantLanguageDetectionJobRequest = None,
        *,
        job_id: str,
    ) -> shapes.DescribeDominantLanguageDetectionJobResponse:
        """
        Gets the properties associated with a dominant language detection job. Use this
        operation to get the status of a detection job.
        """
        if _request is None:
            _params = {}
            if job_id is not ShapeBase.NOT_SET:
                _params['job_id'] = job_id
            _request = shapes.DescribeDominantLanguageDetectionJobRequest(
                **_params
            )
        response = self._boto_client.describe_dominant_language_detection_job(
            **_request.to_boto()
        )

        return shapes.DescribeDominantLanguageDetectionJobResponse.from_boto(
            response
        )

    def describe_entities_detection_job(
        self,
        _request: shapes.DescribeEntitiesDetectionJobRequest = None,
        *,
        job_id: str,
    ) -> shapes.DescribeEntitiesDetectionJobResponse:
        """
        Gets the properties associated with an entities detection job. Use this
        operation to get the status of a detection job.
        """
        if _request is None:
            _params = {}
            if job_id is not ShapeBase.NOT_SET:
                _params['job_id'] = job_id
            _request = shapes.DescribeEntitiesDetectionJobRequest(**_params)
        response = self._boto_client.describe_entities_detection_job(
            **_request.to_boto()
        )

        return shapes.DescribeEntitiesDetectionJobResponse.from_boto(response)

    def describe_key_phrases_detection_job(
        self,
        _request: shapes.DescribeKeyPhrasesDetectionJobRequest = None,
        *,
        job_id: str,
    ) -> shapes.DescribeKeyPhrasesDetectionJobResponse:
        """
        Gets the properties associated with a key phrases detection job. Use this
        operation to get the status of a detection job.
        """
        if _request is None:
            _params = {}
            if job_id is not ShapeBase.NOT_SET:
                _params['job_id'] = job_id
            _request = shapes.DescribeKeyPhrasesDetectionJobRequest(**_params)
        response = self._boto_client.describe_key_phrases_detection_job(
            **_request.to_boto()
        )

        return shapes.DescribeKeyPhrasesDetectionJobResponse.from_boto(response)

    def describe_sentiment_detection_job(
        self,
        _request: shapes.DescribeSentimentDetectionJobRequest = None,
        *,
        job_id: str,
    ) -> shapes.DescribeSentimentDetectionJobResponse:
        """
        Gets the properties associated with a sentiment detection job. Use this
        operation to get the status of a detection job.
        """
        if _request is None:
            _params = {}
            if job_id is not ShapeBase.NOT_SET:
                _params['job_id'] = job_id
            _request = shapes.DescribeSentimentDetectionJobRequest(**_params)
        response = self._boto_client.describe_sentiment_detection_job(
            **_request.to_boto()
        )

        return shapes.DescribeSentimentDetectionJobResponse.from_boto(response)

    def describe_topics_detection_job(
        self,
        _request: shapes.DescribeTopicsDetectionJobRequest = None,
        *,
        job_id: str,
    ) -> shapes.DescribeTopicsDetectionJobResponse:
        """
        Gets the properties associated with a topic detection job. Use this operation to
        get the status of a detection job.
        """
        if _request is None:
            _params = {}
            if job_id is not ShapeBase.NOT_SET:
                _params['job_id'] = job_id
            _request = shapes.DescribeTopicsDetectionJobRequest(**_params)
        response = self._boto_client.describe_topics_detection_job(
            **_request.to_boto()
        )

        return shapes.DescribeTopicsDetectionJobResponse.from_boto(response)

    def detect_dominant_language(
        self,
        _request: shapes.DetectDominantLanguageRequest = None,
        *,
        text: str,
    ) -> shapes.DetectDominantLanguageResponse:
        """
        Determines the dominant language of the input text. For a list of languages that
        Amazon Comprehend can detect, see [Amazon Comprehend Supported
        Languages](http://docs.aws.amazon.com/comprehend/latest/dg/how-languages.html).
        """
        if _request is None:
            _params = {}
            if text is not ShapeBase.NOT_SET:
                _params['text'] = text
            _request = shapes.DetectDominantLanguageRequest(**_params)
        response = self._boto_client.detect_dominant_language(
            **_request.to_boto()
        )

        return shapes.DetectDominantLanguageResponse.from_boto(response)

    def detect_entities(
        self,
        _request: shapes.DetectEntitiesRequest = None,
        *,
        text: str,
        language_code: typing.Union[str, shapes.LanguageCode],
    ) -> shapes.DetectEntitiesResponse:
        """
        Inspects text for named entities, and returns information about them. For more
        information, about named entities, see how-entities.
        """
        if _request is None:
            _params = {}
            if text is not ShapeBase.NOT_SET:
                _params['text'] = text
            if language_code is not ShapeBase.NOT_SET:
                _params['language_code'] = language_code
            _request = shapes.DetectEntitiesRequest(**_params)
        response = self._boto_client.detect_entities(**_request.to_boto())

        return shapes.DetectEntitiesResponse.from_boto(response)

    def detect_key_phrases(
        self,
        _request: shapes.DetectKeyPhrasesRequest = None,
        *,
        text: str,
        language_code: typing.Union[str, shapes.LanguageCode],
    ) -> shapes.DetectKeyPhrasesResponse:
        """
        Detects the key noun phrases found in the text.
        """
        if _request is None:
            _params = {}
            if text is not ShapeBase.NOT_SET:
                _params['text'] = text
            if language_code is not ShapeBase.NOT_SET:
                _params['language_code'] = language_code
            _request = shapes.DetectKeyPhrasesRequest(**_params)
        response = self._boto_client.detect_key_phrases(**_request.to_boto())

        return shapes.DetectKeyPhrasesResponse.from_boto(response)

    def detect_sentiment(
        self,
        _request: shapes.DetectSentimentRequest = None,
        *,
        text: str,
        language_code: typing.Union[str, shapes.LanguageCode],
    ) -> shapes.DetectSentimentResponse:
        """
        Inspects text and returns an inference of the prevailing sentiment (`POSITIVE`,
        `NEUTRAL`, `MIXED`, or `NEGATIVE`).
        """
        if _request is None:
            _params = {}
            if text is not ShapeBase.NOT_SET:
                _params['text'] = text
            if language_code is not ShapeBase.NOT_SET:
                _params['language_code'] = language_code
            _request = shapes.DetectSentimentRequest(**_params)
        response = self._boto_client.detect_sentiment(**_request.to_boto())

        return shapes.DetectSentimentResponse.from_boto(response)

    def detect_syntax(
        self,
        _request: shapes.DetectSyntaxRequest = None,
        *,
        text: str,
        language_code: typing.Union[str, shapes.SyntaxLanguageCode],
    ) -> shapes.DetectSyntaxResponse:
        """
        Inspects text for syntax and the part of speech of words in the document. For
        more information, how-syntax.
        """
        if _request is None:
            _params = {}
            if text is not ShapeBase.NOT_SET:
                _params['text'] = text
            if language_code is not ShapeBase.NOT_SET:
                _params['language_code'] = language_code
            _request = shapes.DetectSyntaxRequest(**_params)
        response = self._boto_client.detect_syntax(**_request.to_boto())

        return shapes.DetectSyntaxResponse.from_boto(response)

    def list_dominant_language_detection_jobs(
        self,
        _request: shapes.ListDominantLanguageDetectionJobsRequest = None,
        *,
        filter: shapes.DominantLanguageDetectionJobFilter = ShapeBase.NOT_SET,
        next_token: str = ShapeBase.NOT_SET,
        max_results: int = ShapeBase.NOT_SET,
    ) -> shapes.ListDominantLanguageDetectionJobsResponse:
        """
        Gets a list of the dominant language detection jobs that you have submitted.
        """
        if _request is None:
            _params = {}
            if filter is not ShapeBase.NOT_SET:
                _params['filter'] = filter
            if next_token is not ShapeBase.NOT_SET:
                _params['next_token'] = next_token
            if max_results is not ShapeBase.NOT_SET:
                _params['max_results'] = max_results
            _request = shapes.ListDominantLanguageDetectionJobsRequest(
                **_params
            )
        response = self._boto_client.list_dominant_language_detection_jobs(
            **_request.to_boto()
        )

        return shapes.ListDominantLanguageDetectionJobsResponse.from_boto(
            response
        )

    def list_entities_detection_jobs(
        self,
        _request: shapes.ListEntitiesDetectionJobsRequest = None,
        *,
        filter: shapes.EntitiesDetectionJobFilter = ShapeBase.NOT_SET,
        next_token: str = ShapeBase.NOT_SET,
        max_results: int = ShapeBase.NOT_SET,
    ) -> shapes.ListEntitiesDetectionJobsResponse:
        """
        Gets a list of the entity detection jobs that you have submitted.
        """
        if _request is None:
            _params = {}
            if filter is not ShapeBase.NOT_SET:
                _params['filter'] = filter
            if next_token is not ShapeBase.NOT_SET:
                _params['next_token'] = next_token
            if max_results is not ShapeBase.NOT_SET:
                _params['max_results'] = max_results
            _request = shapes.ListEntitiesDetectionJobsRequest(**_params)
        response = self._boto_client.list_entities_detection_jobs(
            **_request.to_boto()
        )

        return shapes.ListEntitiesDetectionJobsResponse.from_boto(response)

    def list_key_phrases_detection_jobs(
        self,
        _request: shapes.ListKeyPhrasesDetectionJobsRequest = None,
        *,
        filter: shapes.KeyPhrasesDetectionJobFilter = ShapeBase.NOT_SET,
        next_token: str = ShapeBase.NOT_SET,
        max_results: int = ShapeBase.NOT_SET,
    ) -> shapes.ListKeyPhrasesDetectionJobsResponse:
        """
        Get a list of key phrase detection jobs that you have submitted.
        """
        if _request is None:
            _params = {}
            if filter is not ShapeBase.NOT_SET:
                _params['filter'] = filter
            if next_token is not ShapeBase.NOT_SET:
                _params['next_token'] = next_token
            if max_results is not ShapeBase.NOT_SET:
                _params['max_results'] = max_results
            _request = shapes.ListKeyPhrasesDetectionJobsRequest(**_params)
        response = self._boto_client.list_key_phrases_detection_jobs(
            **_request.to_boto()
        )

        return shapes.ListKeyPhrasesDetectionJobsResponse.from_boto(response)

    def list_sentiment_detection_jobs(
        self,
        _request: shapes.ListSentimentDetectionJobsRequest = None,
        *,
        filter: shapes.SentimentDetectionJobFilter = ShapeBase.NOT_SET,
        next_token: str = ShapeBase.NOT_SET,
        max_results: int = ShapeBase.NOT_SET,
    ) -> shapes.ListSentimentDetectionJobsResponse:
        """
        Gets a list of sentiment detection jobs that you have submitted.
        """
        if _request is None:
            _params = {}
            if filter is not ShapeBase.NOT_SET:
                _params['filter'] = filter
            if next_token is not ShapeBase.NOT_SET:
                _params['next_token'] = next_token
            if max_results is not ShapeBase.NOT_SET:
                _params['max_results'] = max_results
            _request = shapes.ListSentimentDetectionJobsRequest(**_params)
        response = self._boto_client.list_sentiment_detection_jobs(
            **_request.to_boto()
        )

        return shapes.ListSentimentDetectionJobsResponse.from_boto(response)

    def list_topics_detection_jobs(
        self,
        _request: shapes.ListTopicsDetectionJobsRequest = None,
        *,
        filter: shapes.TopicsDetectionJobFilter = ShapeBase.NOT_SET,
        next_token: str = ShapeBase.NOT_SET,
        max_results: int = ShapeBase.NOT_SET,
    ) -> shapes.ListTopicsDetectionJobsResponse:
        """
        Gets a list of the topic detection jobs that you have submitted.
        """
        if _request is None:
            _params = {}
            if filter is not ShapeBase.NOT_SET:
                _params['filter'] = filter
            if next_token is not ShapeBase.NOT_SET:
                _params['next_token'] = next_token
            if max_results is not ShapeBase.NOT_SET:
                _params['max_results'] = max_results
            _request = shapes.ListTopicsDetectionJobsRequest(**_params)
        paginator = self.get_paginator("list_topics_detection_jobs").paginate(
            **_request.to_boto()
        )
        page_generator = (page for page in paginator)
        first_page = next(page_generator)
        result = shapes.ListTopicsDetectionJobsResponse.from_boto(first_page)
        result._page_iterator = page_generator
        return result

        return shapes.ListTopicsDetectionJobsResponse.from_boto(response)

    def start_dominant_language_detection_job(
        self,
        _request: shapes.StartDominantLanguageDetectionJobRequest = None,
        *,
        input_data_config: shapes.InputDataConfig,
        output_data_config: shapes.OutputDataConfig,
        data_access_role_arn: str,
        job_name: str = ShapeBase.NOT_SET,
        client_request_token: str = ShapeBase.NOT_SET,
    ) -> shapes.StartDominantLanguageDetectionJobResponse:
        """
        Starts an asynchronous dominant language detection job for a collection of
        documents. Use the operation to track the status of a job.
        """
        if _request is None:
            _params = {}
            if input_data_config is not ShapeBase.NOT_SET:
                _params['input_data_config'] = input_data_config
            if output_data_config is not ShapeBase.NOT_SET:
                _params['output_data_config'] = output_data_config
            if data_access_role_arn is not ShapeBase.NOT_SET:
                _params['data_access_role_arn'] = data_access_role_arn
            if job_name is not ShapeBase.NOT_SET:
                _params['job_name'] = job_name
            if client_request_token is not ShapeBase.NOT_SET:
                _params['client_request_token'] = client_request_token
            _request = shapes.StartDominantLanguageDetectionJobRequest(
                **_params
            )
        response = self._boto_client.start_dominant_language_detection_job(
            **_request.to_boto()
        )

        return shapes.StartDominantLanguageDetectionJobResponse.from_boto(
            response
        )

    def start_entities_detection_job(
        self,
        _request: shapes.StartEntitiesDetectionJobRequest = None,
        *,
        input_data_config: shapes.InputDataConfig,
        output_data_config: shapes.OutputDataConfig,
        data_access_role_arn: str,
        language_code: typing.Union[str, shapes.LanguageCode],
        job_name: str = ShapeBase.NOT_SET,
        client_request_token: str = ShapeBase.NOT_SET,
    ) -> shapes.StartEntitiesDetectionJobResponse:
        """
        Starts an asynchronous entity detection job for a collection of documents. Use
        the operation to track the status of a job.
        """
        if _request is None:
            _params = {}
            if input_data_config is not ShapeBase.NOT_SET:
                _params['input_data_config'] = input_data_config
            if output_data_config is not ShapeBase.NOT_SET:
                _params['output_data_config'] = output_data_config
            if data_access_role_arn is not ShapeBase.NOT_SET:
                _params['data_access_role_arn'] = data_access_role_arn
            if language_code is not ShapeBase.NOT_SET:
                _params['language_code'] = language_code
            if job_name is not ShapeBase.NOT_SET:
                _params['job_name'] = job_name
            if client_request_token is not ShapeBase.NOT_SET:
                _params['client_request_token'] = client_request_token
            _request = shapes.StartEntitiesDetectionJobRequest(**_params)
        response = self._boto_client.start_entities_detection_job(
            **_request.to_boto()
        )

        return shapes.StartEntitiesDetectionJobResponse.from_boto(response)

    def start_key_phrases_detection_job(
        self,
        _request: shapes.StartKeyPhrasesDetectionJobRequest = None,
        *,
        input_data_config: shapes.InputDataConfig,
        output_data_config: shapes.OutputDataConfig,
        data_access_role_arn: str,
        language_code: typing.Union[str, shapes.LanguageCode],
        job_name: str = ShapeBase.NOT_SET,
        client_request_token: str = ShapeBase.NOT_SET,
    ) -> shapes.StartKeyPhrasesDetectionJobResponse:
        """
        Starts an asynchronous key phrase detection job for a collection of documents.
        Use the operation to track the status of a job.
        """
        if _request is None:
            _params = {}
            if input_data_config is not ShapeBase.NOT_SET:
                _params['input_data_config'] = input_data_config
            if output_data_config is not ShapeBase.NOT_SET:
                _params['output_data_config'] = output_data_config
            if data_access_role_arn is not ShapeBase.NOT_SET:
                _params['data_access_role_arn'] = data_access_role_arn
            if language_code is not ShapeBase.NOT_SET:
                _params['language_code'] = language_code
            if job_name is not ShapeBase.NOT_SET:
                _params['job_name'] = job_name
            if client_request_token is not ShapeBase.NOT_SET:
                _params['client_request_token'] = client_request_token
            _request = shapes.StartKeyPhrasesDetectionJobRequest(**_params)
        response = self._boto_client.start_key_phrases_detection_job(
            **_request.to_boto()
        )

        return shapes.StartKeyPhrasesDetectionJobResponse.from_boto(response)

    def start_sentiment_detection_job(
        self,
        _request: shapes.StartSentimentDetectionJobRequest = None,
        *,
        input_data_config: shapes.InputDataConfig,
        output_data_config: shapes.OutputDataConfig,
        data_access_role_arn: str,
        language_code: typing.Union[str, shapes.LanguageCode],
        job_name: str = ShapeBase.NOT_SET,
        client_request_token: str = ShapeBase.NOT_SET,
    ) -> shapes.StartSentimentDetectionJobResponse:
        """
        Starts an asynchronous sentiment detection job for a collection of documents.
        use the operation to track the status of a job.
        """
        if _request is None:
            _params = {}
            if input_data_config is not ShapeBase.NOT_SET:
                _params['input_data_config'] = input_data_config
            if output_data_config is not ShapeBase.NOT_SET:
                _params['output_data_config'] = output_data_config
            if data_access_role_arn is not ShapeBase.NOT_SET:
                _params['data_access_role_arn'] = data_access_role_arn
            if language_code is not ShapeBase.NOT_SET:
                _params['language_code'] = language_code
            if job_name is not ShapeBase.NOT_SET:
                _params['job_name'] = job_name
            if client_request_token is not ShapeBase.NOT_SET:
                _params['client_request_token'] = client_request_token
            _request = shapes.StartSentimentDetectionJobRequest(**_params)
        response = self._boto_client.start_sentiment_detection_job(
            **_request.to_boto()
        )

        return shapes.StartSentimentDetectionJobResponse.from_boto(response)

    def start_topics_detection_job(
        self,
        _request: shapes.StartTopicsDetectionJobRequest = None,
        *,
        input_data_config: shapes.InputDataConfig,
        output_data_config: shapes.OutputDataConfig,
        data_access_role_arn: str,
        job_name: str = ShapeBase.NOT_SET,
        number_of_topics: int = ShapeBase.NOT_SET,
        client_request_token: str = ShapeBase.NOT_SET,
    ) -> shapes.StartTopicsDetectionJobResponse:
        """
        Starts an asynchronous topic detection job. Use the `DescribeTopicDetectionJob`
        operation to track the status of a job.
        """
        if _request is None:
            _params = {}
            if input_data_config is not ShapeBase.NOT_SET:
                _params['input_data_config'] = input_data_config
            if output_data_config is not ShapeBase.NOT_SET:
                _params['output_data_config'] = output_data_config
            if data_access_role_arn is not ShapeBase.NOT_SET:
                _params['data_access_role_arn'] = data_access_role_arn
            if job_name is not ShapeBase.NOT_SET:
                _params['job_name'] = job_name
            if number_of_topics is not ShapeBase.NOT_SET:
                _params['number_of_topics'] = number_of_topics
            if client_request_token is not ShapeBase.NOT_SET:
                _params['client_request_token'] = client_request_token
            _request = shapes.StartTopicsDetectionJobRequest(**_params)
        response = self._boto_client.start_topics_detection_job(
            **_request.to_boto()
        )

        return shapes.StartTopicsDetectionJobResponse.from_boto(response)

    def stop_dominant_language_detection_job(
        self,
        _request: shapes.StopDominantLanguageDetectionJobRequest = None,
        *,
        job_id: str,
    ) -> shapes.StopDominantLanguageDetectionJobResponse:
        """
        Stops a dominant language detection job in progress.

        If the job state is `IN_PROGRESS` the job is marked for termination and put into
        the `STOP_REQUESTED` state. If the job completes before it can be stopped, it is
        put into the `COMPLETED` state; otherwise the job is stopped and put into the
        `STOPPED` state.

        If the job is in the `COMPLETED` or `FAILED` state when you call the
        `StopDominantLanguageDetectionJob` operation, the operation returns a 400
        Internal Request Exception.

        When a job is stopped, any documents already processed are written to the output
        location.
        """
        if _request is None:
            _params = {}
            if job_id is not ShapeBase.NOT_SET:
                _params['job_id'] = job_id
            _request = shapes.StopDominantLanguageDetectionJobRequest(**_params)
        response = self._boto_client.stop_dominant_language_detection_job(
            **_request.to_boto()
        )

        return shapes.StopDominantLanguageDetectionJobResponse.from_boto(
            response
        )

    def stop_entities_detection_job(
        self,
        _request: shapes.StopEntitiesDetectionJobRequest = None,
        *,
        job_id: str,
    ) -> shapes.StopEntitiesDetectionJobResponse:
        """
        Stops an entities detection job in progress.

        If the job state is `IN_PROGRESS` the job is marked for termination and put into
        the `STOP_REQUESTED` state. If the job completes before it can be stopped, it is
        put into the `COMPLETED` state; otherwise the job is stopped and put into the
        `STOPPED` state.

        If the job is in the `COMPLETED` or `FAILED` state when you call the
        `StopDominantLanguageDetectionJob` operation, the operation returns a 400
        Internal Request Exception.

        When a job is stopped, any documents already processed are written to the output
        location.
        """
        if _request is None:
            _params = {}
            if job_id is not ShapeBase.NOT_SET:
                _params['job_id'] = job_id
            _request = shapes.StopEntitiesDetectionJobRequest(**_params)
        response = self._boto_client.stop_entities_detection_job(
            **_request.to_boto()
        )

        return shapes.StopEntitiesDetectionJobResponse.from_boto(response)

    def stop_key_phrases_detection_job(
        self,
        _request: shapes.StopKeyPhrasesDetectionJobRequest = None,
        *,
        job_id: str,
    ) -> shapes.StopKeyPhrasesDetectionJobResponse:
        """
        Stops a key phrases detection job in progress.

        If the job state is `IN_PROGRESS` the job is marked for termination and put into
        the `STOP_REQUESTED` state. If the job completes before it can be stopped, it is
        put into the `COMPLETED` state; otherwise the job is stopped and put into the
        `STOPPED` state.

        If the job is in the `COMPLETED` or `FAILED` state when you call the
        `StopDominantLanguageDetectionJob` operation, the operation returns a 400
        Internal Request Exception.

        When a job is stopped, any documents already processed are written to the output
        location.
        """
        if _request is None:
            _params = {}
            if job_id is not ShapeBase.NOT_SET:
                _params['job_id'] = job_id
            _request = shapes.StopKeyPhrasesDetectionJobRequest(**_params)
        response = self._boto_client.stop_key_phrases_detection_job(
            **_request.to_boto()
        )

        return shapes.StopKeyPhrasesDetectionJobResponse.from_boto(response)

    def stop_sentiment_detection_job(
        self,
        _request: shapes.StopSentimentDetectionJobRequest = None,
        *,
        job_id: str,
    ) -> shapes.StopSentimentDetectionJobResponse:
        """
        Stops a sentiment detection job in progress.

        If the job state is `IN_PROGRESS` the job is marked for termination and put into
        the `STOP_REQUESTED` state. If the job completes before it can be stopped, it is
        put into the `COMPLETED` state; otherwise the job is be stopped and put into the
        `STOPPED` state.

        If the job is in the `COMPLETED` or `FAILED` state when you call the
        `StopDominantLanguageDetectionJob` operation, the operation returns a 400
        Internal Request Exception.

        When a job is stopped, any documents already processed are written to the output
        location.
        """
        if _request is None:
            _params = {}
            if job_id is not ShapeBase.NOT_SET:
                _params['job_id'] = job_id
            _request = shapes.StopSentimentDetectionJobRequest(**_params)
        response = self._boto_client.stop_sentiment_detection_job(
            **_request.to_boto()
        )

        return shapes.StopSentimentDetectionJobResponse.from_boto(response)
