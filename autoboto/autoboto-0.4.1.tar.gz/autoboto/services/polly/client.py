import datetime
import typing
import boto3
from autoboto import ClientBase, ShapeBase, OutputShapeBase
from . import shapes


class Client(ClientBase):
    def __init__(self, *args, **kwargs):
        super().__init__("polly", *args, **kwargs)

    def delete_lexicon(
        self,
        _request: shapes.DeleteLexiconInput = None,
        *,
        name: str,
    ) -> shapes.DeleteLexiconOutput:
        """
        Deletes the specified pronunciation lexicon stored in an AWS Region. A lexicon
        which has been deleted is not available for speech synthesis, nor is it possible
        to retrieve it using either the `GetLexicon` or `ListLexicon` APIs.

        For more information, see [Managing
        Lexicons](http://docs.aws.amazon.com/polly/latest/dg/managing-lexicons.html).
        """
        if _request is None:
            _params = {}
            if name is not ShapeBase.NOT_SET:
                _params['name'] = name
            _request = shapes.DeleteLexiconInput(**_params)
        response = self._boto_client.delete_lexicon(**_request.to_boto())

        return shapes.DeleteLexiconOutput.from_boto(response)

    def describe_voices(
        self,
        _request: shapes.DescribeVoicesInput = None,
        *,
        language_code: typing.Union[str, shapes.LanguageCode] = ShapeBase.
        NOT_SET,
        include_additional_language_codes: bool = ShapeBase.NOT_SET,
        next_token: str = ShapeBase.NOT_SET,
    ) -> shapes.DescribeVoicesOutput:
        """
        Returns the list of voices that are available for use when requesting speech
        synthesis. Each voice speaks a specified language, is either male or female, and
        is identified by an ID, which is the ASCII version of the voice name.

        When synthesizing speech ( `SynthesizeSpeech` ), you provide the voice ID for
        the voice you want from the list of voices returned by `DescribeVoices`.

        For example, you want your news reader application to read news in a specific
        language, but giving a user the option to choose the voice. Using the
        `DescribeVoices` operation you can provide the user with a list of available
        voices to select from.

        You can optionally specify a language code to filter the available voices. For
        example, if you specify `en-US`, the operation returns a list of all available
        US English voices.

        This operation requires permissions to perform the `polly:DescribeVoices`
        action.
        """
        if _request is None:
            _params = {}
            if language_code is not ShapeBase.NOT_SET:
                _params['language_code'] = language_code
            if include_additional_language_codes is not ShapeBase.NOT_SET:
                _params['include_additional_language_codes'
                       ] = include_additional_language_codes
            if next_token is not ShapeBase.NOT_SET:
                _params['next_token'] = next_token
            _request = shapes.DescribeVoicesInput(**_params)
        paginator = self.get_paginator("describe_voices").paginate(
            **_request.to_boto()
        )
        page_generator = (page for page in paginator)
        first_page = next(page_generator)
        result = shapes.DescribeVoicesOutput.from_boto(first_page)
        result._page_iterator = page_generator
        return result

        return shapes.DescribeVoicesOutput.from_boto(response)

    def get_lexicon(
        self,
        _request: shapes.GetLexiconInput = None,
        *,
        name: str,
    ) -> shapes.GetLexiconOutput:
        """
        Returns the content of the specified pronunciation lexicon stored in an AWS
        Region. For more information, see [Managing
        Lexicons](http://docs.aws.amazon.com/polly/latest/dg/managing-lexicons.html).
        """
        if _request is None:
            _params = {}
            if name is not ShapeBase.NOT_SET:
                _params['name'] = name
            _request = shapes.GetLexiconInput(**_params)
        response = self._boto_client.get_lexicon(**_request.to_boto())

        return shapes.GetLexiconOutput.from_boto(response)

    def get_speech_synthesis_task(
        self,
        _request: shapes.GetSpeechSynthesisTaskInput = None,
        *,
        task_id: str,
    ) -> shapes.GetSpeechSynthesisTaskOutput:
        """
        Retrieves a specific SpeechSynthesisTask object based on its TaskID. This object
        contains information about the given speech synthesis task, including the status
        of the task, and a link to the S3 bucket containing the output of the task.
        """
        if _request is None:
            _params = {}
            if task_id is not ShapeBase.NOT_SET:
                _params['task_id'] = task_id
            _request = shapes.GetSpeechSynthesisTaskInput(**_params)
        response = self._boto_client.get_speech_synthesis_task(
            **_request.to_boto()
        )

        return shapes.GetSpeechSynthesisTaskOutput.from_boto(response)

    def list_lexicons(
        self,
        _request: shapes.ListLexiconsInput = None,
        *,
        next_token: str = ShapeBase.NOT_SET,
    ) -> shapes.ListLexiconsOutput:
        """
        Returns a list of pronunciation lexicons stored in an AWS Region. For more
        information, see [Managing
        Lexicons](http://docs.aws.amazon.com/polly/latest/dg/managing-lexicons.html).
        """
        if _request is None:
            _params = {}
            if next_token is not ShapeBase.NOT_SET:
                _params['next_token'] = next_token
            _request = shapes.ListLexiconsInput(**_params)
        response = self._boto_client.list_lexicons(**_request.to_boto())

        return shapes.ListLexiconsOutput.from_boto(response)

    def list_speech_synthesis_tasks(
        self,
        _request: shapes.ListSpeechSynthesisTasksInput = None,
        *,
        max_results: int = ShapeBase.NOT_SET,
        next_token: str = ShapeBase.NOT_SET,
        status: typing.Union[str, shapes.TaskStatus] = ShapeBase.NOT_SET,
    ) -> shapes.ListSpeechSynthesisTasksOutput:
        """
        Returns a list of SpeechSynthesisTask objects ordered by their creation date.
        This operation can filter the tasks by their status, for example, allowing users
        to list only tasks that are completed.
        """
        if _request is None:
            _params = {}
            if max_results is not ShapeBase.NOT_SET:
                _params['max_results'] = max_results
            if next_token is not ShapeBase.NOT_SET:
                _params['next_token'] = next_token
            if status is not ShapeBase.NOT_SET:
                _params['status'] = status
            _request = shapes.ListSpeechSynthesisTasksInput(**_params)
        response = self._boto_client.list_speech_synthesis_tasks(
            **_request.to_boto()
        )

        return shapes.ListSpeechSynthesisTasksOutput.from_boto(response)

    def put_lexicon(
        self,
        _request: shapes.PutLexiconInput = None,
        *,
        name: str,
        content: str,
    ) -> shapes.PutLexiconOutput:
        """
        Stores a pronunciation lexicon in an AWS Region. If a lexicon with the same name
        already exists in the region, it is overwritten by the new lexicon. Lexicon
        operations have eventual consistency, therefore, it might take some time before
        the lexicon is available to the SynthesizeSpeech operation.

        For more information, see [Managing
        Lexicons](http://docs.aws.amazon.com/polly/latest/dg/managing-lexicons.html).
        """
        if _request is None:
            _params = {}
            if name is not ShapeBase.NOT_SET:
                _params['name'] = name
            if content is not ShapeBase.NOT_SET:
                _params['content'] = content
            _request = shapes.PutLexiconInput(**_params)
        response = self._boto_client.put_lexicon(**_request.to_boto())

        return shapes.PutLexiconOutput.from_boto(response)

    def start_speech_synthesis_task(
        self,
        _request: shapes.StartSpeechSynthesisTaskInput = None,
        *,
        output_format: typing.Union[str, shapes.OutputFormat],
        output_s3_bucket_name: str,
        text: str,
        voice_id: typing.Union[str, shapes.VoiceId],
        lexicon_names: typing.List[str] = ShapeBase.NOT_SET,
        output_s3_key_prefix: str = ShapeBase.NOT_SET,
        sample_rate: str = ShapeBase.NOT_SET,
        sns_topic_arn: str = ShapeBase.NOT_SET,
        speech_mark_types: typing.List[typing.Union[str, shapes.SpeechMarkType]
                                      ] = ShapeBase.NOT_SET,
        text_type: typing.Union[str, shapes.TextType] = ShapeBase.NOT_SET,
        language_code: typing.Union[str, shapes.LanguageCode] = ShapeBase.
        NOT_SET,
    ) -> shapes.StartSpeechSynthesisTaskOutput:
        """
        Allows the creation of an asynchronous synthesis task, by starting a new
        `SpeechSynthesisTask`. This operation requires all the standard information
        needed for speech synthesis, plus the name of an Amazon S3 bucket for the
        service to store the output of the synthesis task and two optional parameters
        (OutputS3KeyPrefix and SnsTopicArn). Once the synthesis task is created, this
        operation will return a SpeechSynthesisTask object, which will include an
        identifier of this task as well as the current status.
        """
        if _request is None:
            _params = {}
            if output_format is not ShapeBase.NOT_SET:
                _params['output_format'] = output_format
            if output_s3_bucket_name is not ShapeBase.NOT_SET:
                _params['output_s3_bucket_name'] = output_s3_bucket_name
            if text is not ShapeBase.NOT_SET:
                _params['text'] = text
            if voice_id is not ShapeBase.NOT_SET:
                _params['voice_id'] = voice_id
            if lexicon_names is not ShapeBase.NOT_SET:
                _params['lexicon_names'] = lexicon_names
            if output_s3_key_prefix is not ShapeBase.NOT_SET:
                _params['output_s3_key_prefix'] = output_s3_key_prefix
            if sample_rate is not ShapeBase.NOT_SET:
                _params['sample_rate'] = sample_rate
            if sns_topic_arn is not ShapeBase.NOT_SET:
                _params['sns_topic_arn'] = sns_topic_arn
            if speech_mark_types is not ShapeBase.NOT_SET:
                _params['speech_mark_types'] = speech_mark_types
            if text_type is not ShapeBase.NOT_SET:
                _params['text_type'] = text_type
            if language_code is not ShapeBase.NOT_SET:
                _params['language_code'] = language_code
            _request = shapes.StartSpeechSynthesisTaskInput(**_params)
        response = self._boto_client.start_speech_synthesis_task(
            **_request.to_boto()
        )

        return shapes.StartSpeechSynthesisTaskOutput.from_boto(response)

    def synthesize_speech(
        self,
        _request: shapes.SynthesizeSpeechInput = None,
        *,
        output_format: typing.Union[str, shapes.OutputFormat],
        text: str,
        voice_id: typing.Union[str, shapes.VoiceId],
        lexicon_names: typing.List[str] = ShapeBase.NOT_SET,
        sample_rate: str = ShapeBase.NOT_SET,
        speech_mark_types: typing.List[typing.Union[str, shapes.SpeechMarkType]
                                      ] = ShapeBase.NOT_SET,
        text_type: typing.Union[str, shapes.TextType] = ShapeBase.NOT_SET,
        language_code: typing.Union[str, shapes.LanguageCode] = ShapeBase.
        NOT_SET,
    ) -> shapes.SynthesizeSpeechOutput:
        """
        Synthesizes UTF-8 input, plain text or SSML, to a stream of bytes. SSML input
        must be valid, well-formed SSML. Some alphabets might not be available with all
        the voices (for example, Cyrillic might not be read at all by English voices)
        unless phoneme mapping is used. For more information, see [How it
        Works](http://docs.aws.amazon.com/polly/latest/dg/how-text-to-speech-
        works.html).
        """
        if _request is None:
            _params = {}
            if output_format is not ShapeBase.NOT_SET:
                _params['output_format'] = output_format
            if text is not ShapeBase.NOT_SET:
                _params['text'] = text
            if voice_id is not ShapeBase.NOT_SET:
                _params['voice_id'] = voice_id
            if lexicon_names is not ShapeBase.NOT_SET:
                _params['lexicon_names'] = lexicon_names
            if sample_rate is not ShapeBase.NOT_SET:
                _params['sample_rate'] = sample_rate
            if speech_mark_types is not ShapeBase.NOT_SET:
                _params['speech_mark_types'] = speech_mark_types
            if text_type is not ShapeBase.NOT_SET:
                _params['text_type'] = text_type
            if language_code is not ShapeBase.NOT_SET:
                _params['language_code'] = language_code
            _request = shapes.SynthesizeSpeechInput(**_params)
        response = self._boto_client.synthesize_speech(**_request.to_boto())

        return shapes.SynthesizeSpeechOutput.from_boto(response)
