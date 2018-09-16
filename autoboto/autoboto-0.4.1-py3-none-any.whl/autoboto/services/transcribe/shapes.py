import datetime
import typing
from autoboto import ShapeBase, OutputShapeBase, TypeInfo
import dataclasses


@dataclasses.dataclass
class BadRequestException(ShapeBase):
    """
    Your request didn't pass one or more validation tests. For example, a name
    already exists when creating a resource or a name may not exist when getting a
    transcription job or custom vocabulary. See the exception `Message` field for
    more information.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "message",
                "Message",
                TypeInfo(str),
            ),
        ]

    message: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ConflictException(ShapeBase):
    """
    When you are using the `StartTranscriptionJob` operation, the `JobName` field is
    a duplicate of a previously entered job name. Resend your request with a
    different name.

    When you are using the `UpdateVocabulary` operation, there are two jobs running
    at the same time. Resend the second request later.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "message",
                "Message",
                TypeInfo(str),
            ),
        ]

    message: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class CreateVocabularyRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "vocabulary_name",
                "VocabularyName",
                TypeInfo(str),
            ),
            (
                "language_code",
                "LanguageCode",
                TypeInfo(typing.Union[str, LanguageCode]),
            ),
            (
                "phrases",
                "Phrases",
                TypeInfo(typing.List[str]),
            ),
        ]

    # The name of the vocabulary. The name must be unique within an AWS account.
    # The name is case-sensitive.
    vocabulary_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The language code of the vocabulary entries.
    language_code: typing.Union[str, "LanguageCode"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # An array of strings that contains the vocabulary entries.
    phrases: typing.List[str] = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class CreateVocabularyResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "vocabulary_name",
                "VocabularyName",
                TypeInfo(str),
            ),
            (
                "language_code",
                "LanguageCode",
                TypeInfo(typing.Union[str, LanguageCode]),
            ),
            (
                "vocabulary_state",
                "VocabularyState",
                TypeInfo(typing.Union[str, VocabularyState]),
            ),
            (
                "last_modified_time",
                "LastModifiedTime",
                TypeInfo(datetime.datetime),
            ),
            (
                "failure_reason",
                "FailureReason",
                TypeInfo(str),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The name of the vocabulary.
    vocabulary_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The language code of the vocabulary entries.
    language_code: typing.Union[str, "LanguageCode"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The processing state of the vocabulary. When the `VocabularyState` field
    # contains `READY` the vocabulary is ready to be used in a
    # `StartTranscriptionJob` request.
    vocabulary_state: typing.Union[str, "VocabularyState"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The date and time that the vocabulary was created.
    last_modified_time: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # If the `VocabularyState` field is `FAILED`, this field contains information
    # about why the job failed.
    failure_reason: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DeleteVocabularyRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "vocabulary_name",
                "VocabularyName",
                TypeInfo(str),
            ),
        ]

    # The name of the vocabulary to delete.
    vocabulary_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class GetTranscriptionJobRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "transcription_job_name",
                "TranscriptionJobName",
                TypeInfo(str),
            ),
        ]

    # The name of the job.
    transcription_job_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class GetTranscriptionJobResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "transcription_job",
                "TranscriptionJob",
                TypeInfo(TranscriptionJob),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # An object that contains the results of the transcription job.
    transcription_job: "TranscriptionJob" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class GetVocabularyRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "vocabulary_name",
                "VocabularyName",
                TypeInfo(str),
            ),
        ]

    # The name of the vocabulary to return information about. The name is case-
    # sensitive.
    vocabulary_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class GetVocabularyResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "vocabulary_name",
                "VocabularyName",
                TypeInfo(str),
            ),
            (
                "language_code",
                "LanguageCode",
                TypeInfo(typing.Union[str, LanguageCode]),
            ),
            (
                "vocabulary_state",
                "VocabularyState",
                TypeInfo(typing.Union[str, VocabularyState]),
            ),
            (
                "last_modified_time",
                "LastModifiedTime",
                TypeInfo(datetime.datetime),
            ),
            (
                "failure_reason",
                "FailureReason",
                TypeInfo(str),
            ),
            (
                "download_uri",
                "DownloadUri",
                TypeInfo(str),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The name of the vocabulary to return.
    vocabulary_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The language code of the vocabulary entries.
    language_code: typing.Union[str, "LanguageCode"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The processing state of the vocabulary.
    vocabulary_state: typing.Union[str, "VocabularyState"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The date and time that the vocabulary was last modified.
    last_modified_time: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # If the `VocabularyState` field is `FAILED`, this field contains information
    # about why the job failed.
    failure_reason: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The S3 location where the vocabulary is stored. Use this URI to get the
    # contents of the vocabulary. The URI is available for a limited time.
    download_uri: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class InternalFailureException(ShapeBase):
    """
    There was an internal error. Check the error message and try your request again.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "message",
                "Message",
                TypeInfo(str),
            ),
        ]

    message: str = dataclasses.field(default=ShapeBase.NOT_SET, )


class LanguageCode(str):
    en_US = "en-US"
    es_US = "es-US"


@dataclasses.dataclass
class LimitExceededException(ShapeBase):
    """
    Either you have sent too many requests or your input file is too long. Wait
    before you resend your request, or use a smaller file and resend the request.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "message",
                "Message",
                TypeInfo(str),
            ),
        ]

    message: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ListTranscriptionJobsRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "status",
                "Status",
                TypeInfo(typing.Union[str, TranscriptionJobStatus]),
            ),
            (
                "job_name_contains",
                "JobNameContains",
                TypeInfo(str),
            ),
            (
                "next_token",
                "NextToken",
                TypeInfo(str),
            ),
            (
                "max_results",
                "MaxResults",
                TypeInfo(int),
            ),
        ]

    # When specified, returns only transcription jobs with the specified status.
    status: typing.Union[str, "TranscriptionJobStatus"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # When specified, the jobs returned in the list are limited to jobs whose
    # name contains the specified string.
    job_name_contains: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # If the result of the previous request to `ListTranscriptionJobs` was
    # truncated, include the `NextToken` to fetch the next set of jobs.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The maximum number of jobs to return in the response. If there are fewer
    # results in the list, this response contains only the actual results.
    max_results: int = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ListTranscriptionJobsResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "status",
                "Status",
                TypeInfo(typing.Union[str, TranscriptionJobStatus]),
            ),
            (
                "next_token",
                "NextToken",
                TypeInfo(str),
            ),
            (
                "transcription_job_summaries",
                "TranscriptionJobSummaries",
                TypeInfo(typing.List[TranscriptionJobSummary]),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The requested status of the jobs returned.
    status: typing.Union[str, "TranscriptionJobStatus"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The `ListTranscriptionJobs` operation returns a page of jobs at a time. The
    # maximum size of the page is set by the `MaxResults` parameter. If there are
    # more jobs in the list than the page size, Amazon Transcribe returns the
    # `NextPage` token. Include the token in the next request to the
    # `ListTranscriptionJobs` operation to return in the next page of jobs.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A list of objects containing summary information for a transcription job.
    transcription_job_summaries: typing.List["TranscriptionJobSummary"
                                            ] = dataclasses.field(
                                                default=ShapeBase.NOT_SET,
                                            )


@dataclasses.dataclass
class ListVocabulariesRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "next_token",
                "NextToken",
                TypeInfo(str),
            ),
            (
                "max_results",
                "MaxResults",
                TypeInfo(int),
            ),
            (
                "state_equals",
                "StateEquals",
                TypeInfo(typing.Union[str, VocabularyState]),
            ),
            (
                "name_contains",
                "NameContains",
                TypeInfo(str),
            ),
        ]

    # If the result of the previous request to `ListVocabularies` was truncated,
    # include the `NextToken` to fetch the next set of jobs.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The maximum number of vocabularies to return in the response. If there are
    # fewer results in the list, this response contains only the actual results.
    max_results: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # When specified, only returns vocabularies with the `VocabularyState` field
    # equal to the specified state.
    state_equals: typing.Union[str, "VocabularyState"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # When specified, the vocabularies returned in the list are limited to
    # vocabularies whose name contains the specified string. The search is case-
    # insensitive, `ListVocabularies` will return both "vocabularyname" and
    # "VocabularyName" in the response list.
    name_contains: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ListVocabulariesResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "status",
                "Status",
                TypeInfo(typing.Union[str, TranscriptionJobStatus]),
            ),
            (
                "next_token",
                "NextToken",
                TypeInfo(str),
            ),
            (
                "vocabularies",
                "Vocabularies",
                TypeInfo(typing.List[VocabularyInfo]),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The requested vocabulary state.
    status: typing.Union[str, "TranscriptionJobStatus"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The `ListVocabularies` operation returns a page of vocabularies at a time.
    # The maximum size of the page is set by the `MaxResults` parameter. If there
    # are more jobs in the list than the page size, Amazon Transcribe returns the
    # `NextPage` token. Include the token in the next request to the
    # `ListVocabularies` operation to return in the next page of jobs.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A list of objects that describe the vocabularies that match the search
    # criteria in the request.
    vocabularies: typing.List["VocabularyInfo"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class Media(ShapeBase):
    """
    Describes the input media file in a transcription request.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "media_file_uri",
                "MediaFileUri",
                TypeInfo(str),
            ),
        ]

    # The S3 location of the input media file. The URI must be in the same region
    # as the API endpoint that you are calling. The general form is:

    # ` https://<aws-region>.amazonaws.com/<bucket-name>/<keyprefix>/<objectkey>
    # `

    # For example:

    # `https://s3-us-east-1.amazonaws.com/examplebucket/example.mp4`

    # `https://s3-us-east-1.amazonaws.com/examplebucket/mediadocs/example.mp4`

    # For more information about S3 object names, see [Object
    # Keys](http://docs.aws.amazon.com/AmazonS3/latest/dev/UsingMetadata.html#object-
    # keys) in the _Amazon S3 Developer Guide_.
    media_file_uri: str = dataclasses.field(default=ShapeBase.NOT_SET, )


class MediaFormat(str):
    mp3 = "mp3"
    mp4 = "mp4"
    wav = "wav"
    flac = "flac"


@dataclasses.dataclass
class NotFoundException(ShapeBase):
    """
    We can't find the requested resource. Check the name and try your request again.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "message",
                "Message",
                TypeInfo(str),
            ),
        ]

    message: str = dataclasses.field(default=ShapeBase.NOT_SET, )


class OutputLocationType(str):
    CUSTOMER_BUCKET = "CUSTOMER_BUCKET"
    SERVICE_BUCKET = "SERVICE_BUCKET"


@dataclasses.dataclass
class Settings(ShapeBase):
    """
    Provides optional settings for the `StartTranscriptionJob` operation.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "vocabulary_name",
                "VocabularyName",
                TypeInfo(str),
            ),
            (
                "show_speaker_labels",
                "ShowSpeakerLabels",
                TypeInfo(bool),
            ),
            (
                "max_speaker_labels",
                "MaxSpeakerLabels",
                TypeInfo(int),
            ),
            (
                "channel_identification",
                "ChannelIdentification",
                TypeInfo(bool),
            ),
        ]

    # The name of a vocabulary to use when processing the transcription job.
    vocabulary_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Determines whether the transcription job uses speaker recognition to
    # identify different speakers in the input audio. Speaker recognition labels
    # individual speakers in the audio file. If you set the `ShowSpeakerLabels`
    # field to true, you must also set the maximum number of speaker labels
    # `MaxSpeakerLabels` field.

    # You can't set both `ShowSpeakerLabels` and `ChannelIdentification` in the
    # same request. If you set both, your request returns a
    # `BadRequestException`.
    show_speaker_labels: bool = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The maximum number of speakers to identify in the input audio. If there are
    # more speakers in the audio than this number, multiple speakers will be
    # identified as a single speaker. If you specify the `MaxSpeakerLabels`
    # field, you must set the `ShowSpeakerLabels` field to true.
    max_speaker_labels: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Instructs Amazon Transcribe to process each audio channel separately and
    # then merge the transcription output of each channel into a single
    # transcription.

    # Amazon Transcribe also produces a transcription of each item detected on an
    # audio channel, including the start time and end time of the item and
    # alternative transcriptions of the item including the confidence that Amazon
    # Transcribe has in the transcription.

    # You can't set both `ShowSpeakerLabels` and `ChannelIdentification` in the
    # same request. If you set both, your request returns a
    # `BadRequestException`.
    channel_identification: bool = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class StartTranscriptionJobRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "transcription_job_name",
                "TranscriptionJobName",
                TypeInfo(str),
            ),
            (
                "language_code",
                "LanguageCode",
                TypeInfo(typing.Union[str, LanguageCode]),
            ),
            (
                "media_format",
                "MediaFormat",
                TypeInfo(typing.Union[str, MediaFormat]),
            ),
            (
                "media",
                "Media",
                TypeInfo(Media),
            ),
            (
                "media_sample_rate_hertz",
                "MediaSampleRateHertz",
                TypeInfo(int),
            ),
            (
                "output_bucket_name",
                "OutputBucketName",
                TypeInfo(str),
            ),
            (
                "settings",
                "Settings",
                TypeInfo(Settings),
            ),
        ]

    # The name of the job. You can't use the strings "." or ".." in the job name.
    # The name must be unique within an AWS account.
    transcription_job_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The language code for the language used in the input media file.
    language_code: typing.Union[str, "LanguageCode"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The format of the input media file.
    media_format: typing.Union[str, "MediaFormat"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # An object that describes the input media for a transcription job.
    media: "Media" = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The sample rate, in Hertz, of the audio track in the input media file.
    media_sample_rate_hertz: int = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The location where the transcription is stored.

    # If you set the `OutputBucketName`, Amazon Transcribe puts the transcription
    # in the specified S3 bucket. When you call the GetTranscriptionJob
    # operation, the operation returns this location in the `TranscriptFileUri`
    # field. The S3 bucket must have permissions that allow Amazon Transcribe to
    # put files in the bucket. For more information, see [Permissions Required
    # for IAM User
    # Roles](https://docs.aws.amazon.com/transcribe/latest/dg/access-control-
    # managing-permissions.html#auth-role-iam-user).

    # If you don't set the `OutputBucketName`, Amazon Transcribe generates a pre-
    # signed URL, a shareable URL that provides secure access to your
    # transcription, and returns it in the `TranscriptFileUri` field. Use this
    # URL to download the transcription.
    output_bucket_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A `Settings` object that provides optional settings for a transcription
    # job.
    settings: "Settings" = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class StartTranscriptionJobResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "transcription_job",
                "TranscriptionJob",
                TypeInfo(TranscriptionJob),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # An object containing details of the asynchronous transcription job.
    transcription_job: "TranscriptionJob" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class Transcript(ShapeBase):
    """
    Identifies the location of a transcription.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "transcript_file_uri",
                "TranscriptFileUri",
                TypeInfo(str),
            ),
        ]

    # The location where the transcription is stored.

    # Use this URI to access the transcription. If you specified an S3 bucket in
    # the `OutputBucketName` field when you created the job, this is the URI of
    # that bucket. If you chose to store the transcription in Amazon Transcribe,
    # this is a shareable URL that provides secure access to that location.
    transcript_file_uri: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class TranscriptionJob(ShapeBase):
    """
    Describes an asynchronous transcription job that was created with the
    `StartTranscriptionJob` operation.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "transcription_job_name",
                "TranscriptionJobName",
                TypeInfo(str),
            ),
            (
                "transcription_job_status",
                "TranscriptionJobStatus",
                TypeInfo(typing.Union[str, TranscriptionJobStatus]),
            ),
            (
                "language_code",
                "LanguageCode",
                TypeInfo(typing.Union[str, LanguageCode]),
            ),
            (
                "media_sample_rate_hertz",
                "MediaSampleRateHertz",
                TypeInfo(int),
            ),
            (
                "media_format",
                "MediaFormat",
                TypeInfo(typing.Union[str, MediaFormat]),
            ),
            (
                "media",
                "Media",
                TypeInfo(Media),
            ),
            (
                "transcript",
                "Transcript",
                TypeInfo(Transcript),
            ),
            (
                "creation_time",
                "CreationTime",
                TypeInfo(datetime.datetime),
            ),
            (
                "completion_time",
                "CompletionTime",
                TypeInfo(datetime.datetime),
            ),
            (
                "failure_reason",
                "FailureReason",
                TypeInfo(str),
            ),
            (
                "settings",
                "Settings",
                TypeInfo(Settings),
            ),
        ]

    # The name of the transcription job.
    transcription_job_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The status of the transcription job.
    transcription_job_status: typing.Union[str, "TranscriptionJobStatus"
                                          ] = dataclasses.field(
                                              default=ShapeBase.NOT_SET,
                                          )

    # The language code for the input speech.
    language_code: typing.Union[str, "LanguageCode"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The sample rate, in Hertz, of the audio track in the input media file.
    media_sample_rate_hertz: int = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The format of the input media file.
    media_format: typing.Union[str, "MediaFormat"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # An object that describes the input media for the transcription job.
    media: "Media" = dataclasses.field(default=ShapeBase.NOT_SET, )

    # An object that describes the output of the transcription job.
    transcript: "Transcript" = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A timestamp that shows when the job was created.
    creation_time: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A timestamp that shows when the job was completed.
    completion_time: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # If the `TranscriptionJobStatus` field is `FAILED`, this field contains
    # information about why the job failed.
    failure_reason: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Optional settings for the transcription job. Use these settings to turn on
    # speaker recognition, to set the maximum number of speakers that should be
    # identified and to specify a custom vocabulary to use when processing the
    # transcription job.
    settings: "Settings" = dataclasses.field(default=ShapeBase.NOT_SET, )


class TranscriptionJobStatus(str):
    IN_PROGRESS = "IN_PROGRESS"
    FAILED = "FAILED"
    COMPLETED = "COMPLETED"


@dataclasses.dataclass
class TranscriptionJobSummary(ShapeBase):
    """
    Provides a summary of information about a transcription job.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "transcription_job_name",
                "TranscriptionJobName",
                TypeInfo(str),
            ),
            (
                "creation_time",
                "CreationTime",
                TypeInfo(datetime.datetime),
            ),
            (
                "completion_time",
                "CompletionTime",
                TypeInfo(datetime.datetime),
            ),
            (
                "language_code",
                "LanguageCode",
                TypeInfo(typing.Union[str, LanguageCode]),
            ),
            (
                "transcription_job_status",
                "TranscriptionJobStatus",
                TypeInfo(typing.Union[str, TranscriptionJobStatus]),
            ),
            (
                "failure_reason",
                "FailureReason",
                TypeInfo(str),
            ),
            (
                "output_location_type",
                "OutputLocationType",
                TypeInfo(typing.Union[str, OutputLocationType]),
            ),
        ]

    # The name of the transcription job.
    transcription_job_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A timestamp that shows when the job was created.
    creation_time: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A timestamp that shows when the job was completed.
    completion_time: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The language code for the input speech.
    language_code: typing.Union[str, "LanguageCode"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The status of the transcription job. When the status is `COMPLETED`, use
    # the `GetTranscriptionJob` operation to get the results of the
    # transcription.
    transcription_job_status: typing.Union[str, "TranscriptionJobStatus"
                                          ] = dataclasses.field(
                                              default=ShapeBase.NOT_SET,
                                          )

    # If the `TranscriptionJobStatus` field is `FAILED`, a description of the
    # error.
    failure_reason: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Indicates the location of the output of the transcription job.

    # If the value is `CUSTOMER_BUCKET` then the location is the S3 bucket
    # specified in the `outputBucketName` field when the transcription job was
    # started with the `StartTranscriptionJob` operation.

    # If the value is `SERVICE_BUCKET` then the output is stored by Amazon
    # Transcribe and can be retrieved using the URI in the `GetTranscriptionJob`
    # response's `TranscriptFileUri` field.
    output_location_type: typing.Union[str, "OutputLocationType"
                                      ] = dataclasses.field(
                                          default=ShapeBase.NOT_SET,
                                      )


@dataclasses.dataclass
class UpdateVocabularyRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "vocabulary_name",
                "VocabularyName",
                TypeInfo(str),
            ),
            (
                "language_code",
                "LanguageCode",
                TypeInfo(typing.Union[str, LanguageCode]),
            ),
            (
                "phrases",
                "Phrases",
                TypeInfo(typing.List[str]),
            ),
        ]

    # The name of the vocabulary to update. The name is case-sensitive.
    vocabulary_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The language code of the vocabulary entries.
    language_code: typing.Union[str, "LanguageCode"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # An array of strings containing the vocabulary entries.
    phrases: typing.List[str] = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class UpdateVocabularyResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "vocabulary_name",
                "VocabularyName",
                TypeInfo(str),
            ),
            (
                "language_code",
                "LanguageCode",
                TypeInfo(typing.Union[str, LanguageCode]),
            ),
            (
                "last_modified_time",
                "LastModifiedTime",
                TypeInfo(datetime.datetime),
            ),
            (
                "vocabulary_state",
                "VocabularyState",
                TypeInfo(typing.Union[str, VocabularyState]),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The name of the vocabulary that was updated.
    vocabulary_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The language code of the vocabulary entries.
    language_code: typing.Union[str, "LanguageCode"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The date and time that the vocabulary was updated.
    last_modified_time: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The processing state of the vocabulary. When the `VocabularyState` field
    # contains `READY` the vocabulary is ready to be used in a
    # `StartTranscriptionJob` request.
    vocabulary_state: typing.Union[str, "VocabularyState"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class VocabularyInfo(ShapeBase):
    """
    Provides information about a custom vocabulary.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "vocabulary_name",
                "VocabularyName",
                TypeInfo(str),
            ),
            (
                "language_code",
                "LanguageCode",
                TypeInfo(typing.Union[str, LanguageCode]),
            ),
            (
                "last_modified_time",
                "LastModifiedTime",
                TypeInfo(datetime.datetime),
            ),
            (
                "vocabulary_state",
                "VocabularyState",
                TypeInfo(typing.Union[str, VocabularyState]),
            ),
        ]

    # The name of the vocabulary.
    vocabulary_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The language code of the vocabulary entries.
    language_code: typing.Union[str, "LanguageCode"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The date and time that the vocabulary was last modified.
    last_modified_time: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The processing state of the vocabulary. If the state is `READY` you can use
    # the vocabulary in a `StartTranscriptionJob` request.
    vocabulary_state: typing.Union[str, "VocabularyState"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


class VocabularyState(str):
    PENDING = "PENDING"
    READY = "READY"
    FAILED = "FAILED"
