import datetime
import typing
from autoboto import ShapeBase, OutputShapeBase, TypeInfo
import botocore.response
import dataclasses


class AudioStream(botocore.response.StreamingBody):
    pass


@dataclasses.dataclass
class DeleteLexiconInput(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "name",
                "Name",
                TypeInfo(str),
            ),
        ]

    # The name of the lexicon to delete. Must be an existing lexicon in the
    # region.
    name: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DeleteLexiconOutput(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class DescribeVoicesInput(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "language_code",
                "LanguageCode",
                TypeInfo(typing.Union[str, LanguageCode]),
            ),
            (
                "include_additional_language_codes",
                "IncludeAdditionalLanguageCodes",
                TypeInfo(bool),
            ),
            (
                "next_token",
                "NextToken",
                TypeInfo(str),
            ),
        ]

    # The language identification tag (ISO 639 code for the language name-ISO
    # 3166 country code) for filtering the list of voices returned. If you don't
    # specify this optional parameter, all available voices are returned.
    language_code: typing.Union[str, "LanguageCode"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Boolean value indicating whether to return any bilingual voices that use
    # the specified language as an additional language. For instance, if you
    # request all languages that use US English (es-US), and there is an Italian
    # voice that speaks both Italian (it-IT) and US English, that voice will be
    # included if you specify `yes` but not if you specify `no`.
    include_additional_language_codes: bool = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # An opaque pagination token returned from the previous `DescribeVoices`
    # operation. If present, this indicates where to continue the listing.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DescribeVoicesOutput(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "voices",
                "Voices",
                TypeInfo(typing.List[Voice]),
            ),
            (
                "next_token",
                "NextToken",
                TypeInfo(str),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A list of voices with their properties.
    voices: typing.List["Voice"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The pagination token to use in the next request to continue the listing of
    # voices. `NextToken` is returned only if the response is truncated.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    def paginate(self,
                ) -> typing.Generator["DescribeVoicesOutput", None, None]:
        yield from super()._paginate()


class Gender(str):
    Female = "Female"
    Male = "Male"


@dataclasses.dataclass
class GetLexiconInput(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "name",
                "Name",
                TypeInfo(str),
            ),
        ]

    # Name of the lexicon.
    name: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class GetLexiconOutput(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "lexicon",
                "Lexicon",
                TypeInfo(Lexicon),
            ),
            (
                "lexicon_attributes",
                "LexiconAttributes",
                TypeInfo(LexiconAttributes),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Lexicon object that provides name and the string content of the lexicon.
    lexicon: "Lexicon" = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Metadata of the lexicon, including phonetic alphabetic used, language code,
    # lexicon ARN, number of lexemes defined in the lexicon, and size of lexicon
    # in bytes.
    lexicon_attributes: "LexiconAttributes" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class GetSpeechSynthesisTaskInput(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "task_id",
                "TaskId",
                TypeInfo(str),
            ),
        ]

    # The Amazon Polly generated identifier for a speech synthesis task.
    task_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class GetSpeechSynthesisTaskOutput(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "synthesis_task",
                "SynthesisTask",
                TypeInfo(SynthesisTask),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # SynthesisTask object that provides information from the requested task,
    # including output format, creation time, task status, and so on.
    synthesis_task: "SynthesisTask" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class InvalidLexiconException(ShapeBase):
    """
    Amazon Polly can't find the specified lexicon. Verify that the lexicon's name is
    spelled correctly, and then try again.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "message",
                "message",
                TypeInfo(str),
            ),
        ]

    message: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class InvalidNextTokenException(ShapeBase):
    """
    The NextToken is invalid. Verify that it's spelled correctly, and then try
    again.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "message",
                "message",
                TypeInfo(str),
            ),
        ]

    message: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class InvalidS3BucketException(ShapeBase):
    """
    The provided Amazon S3 bucket name is invalid. Please check your input with S3
    bucket naming requirements and try again.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "message",
                "message",
                TypeInfo(str),
            ),
        ]

    message: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class InvalidS3KeyException(ShapeBase):
    """
    The provided Amazon S3 key prefix is invalid. Please provide a valid S3 object
    key name.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "message",
                "message",
                TypeInfo(str),
            ),
        ]

    message: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class InvalidSampleRateException(ShapeBase):
    """
    The specified sample rate is not valid.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "message",
                "message",
                TypeInfo(str),
            ),
        ]

    message: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class InvalidSnsTopicArnException(ShapeBase):
    """
    The provided SNS topic ARN is invalid. Please provide a valid SNS topic ARN and
    try again.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "message",
                "message",
                TypeInfo(str),
            ),
        ]

    message: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class InvalidSsmlException(ShapeBase):
    """
    The SSML you provided is invalid. Verify the SSML syntax, spelling of tags and
    values, and then try again.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "message",
                "message",
                TypeInfo(str),
            ),
        ]

    message: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class InvalidTaskIdException(ShapeBase):
    """
    The provided Task ID is not valid. Please provide a valid Task ID and try again.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "message",
                "message",
                TypeInfo(str),
            ),
        ]

    message: str = dataclasses.field(default=ShapeBase.NOT_SET, )


class LanguageCode(str):
    cmn_CN = "cmn-CN"
    cy_GB = "cy-GB"
    da_DK = "da-DK"
    de_DE = "de-DE"
    en_AU = "en-AU"
    en_GB = "en-GB"
    en_GB_WLS = "en-GB-WLS"
    en_IN = "en-IN"
    en_US = "en-US"
    es_ES = "es-ES"
    es_US = "es-US"
    fr_CA = "fr-CA"
    fr_FR = "fr-FR"
    is_IS = "is-IS"
    it_IT = "it-IT"
    ja_JP = "ja-JP"
    hi_IN = "hi-IN"
    ko_KR = "ko-KR"
    nb_NO = "nb-NO"
    nl_NL = "nl-NL"
    pl_PL = "pl-PL"
    pt_BR = "pt-BR"
    pt_PT = "pt-PT"
    ro_RO = "ro-RO"
    ru_RU = "ru-RU"
    sv_SE = "sv-SE"
    tr_TR = "tr-TR"


@dataclasses.dataclass
class LanguageNotSupportedException(ShapeBase):
    """
    The language specified is not currently supported by Amazon Polly in this
    capacity.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "message",
                "message",
                TypeInfo(str),
            ),
        ]

    message: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class Lexicon(ShapeBase):
    """
    Provides lexicon name and lexicon content in string format. For more
    information, see [Pronunciation Lexicon Specification (PLS) Version
    1.0](https://www.w3.org/TR/pronunciation-lexicon/).
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "content",
                "Content",
                TypeInfo(str),
            ),
            (
                "name",
                "Name",
                TypeInfo(str),
            ),
        ]

    # Lexicon content in string format. The content of a lexicon must be in PLS
    # format.
    content: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Name of the lexicon.
    name: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class LexiconAttributes(ShapeBase):
    """
    Contains metadata describing the lexicon such as the number of lexemes, language
    code, and so on. For more information, see [Managing
    Lexicons](http://docs.aws.amazon.com/polly/latest/dg/managing-lexicons.html).
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "alphabet",
                "Alphabet",
                TypeInfo(str),
            ),
            (
                "language_code",
                "LanguageCode",
                TypeInfo(typing.Union[str, LanguageCode]),
            ),
            (
                "last_modified",
                "LastModified",
                TypeInfo(datetime.datetime),
            ),
            (
                "lexicon_arn",
                "LexiconArn",
                TypeInfo(str),
            ),
            (
                "lexemes_count",
                "LexemesCount",
                TypeInfo(int),
            ),
            (
                "size",
                "Size",
                TypeInfo(int),
            ),
        ]

    # Phonetic alphabet used in the lexicon. Valid values are `ipa` and
    # `x-sampa`.
    alphabet: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Language code that the lexicon applies to. A lexicon with a language code
    # such as "en" would be applied to all English languages (en-GB, en-US, en-
    # AUS, en-WLS, and so on.
    language_code: typing.Union[str, "LanguageCode"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Date lexicon was last modified (a timestamp value).
    last_modified: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Amazon Resource Name (ARN) of the lexicon.
    lexicon_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Number of lexemes in the lexicon.
    lexemes_count: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Total size of the lexicon, in characters.
    size: int = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class LexiconDescription(ShapeBase):
    """
    Describes the content of the lexicon.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "name",
                "Name",
                TypeInfo(str),
            ),
            (
                "attributes",
                "Attributes",
                TypeInfo(LexiconAttributes),
            ),
        ]

    # Name of the lexicon.
    name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Provides lexicon metadata.
    attributes: "LexiconAttributes" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class LexiconNotFoundException(ShapeBase):
    """
    Amazon Polly can't find the specified lexicon. This could be caused by a lexicon
    that is missing, its name is misspelled or specifying a lexicon that is in a
    different region.

    Verify that the lexicon exists, is in the region (see ListLexicons) and that you
    spelled its name is spelled correctly. Then try again.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "message",
                "message",
                TypeInfo(str),
            ),
        ]

    message: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class LexiconSizeExceededException(ShapeBase):
    """
    The maximum size of the specified lexicon would be exceeded by this operation.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "message",
                "message",
                TypeInfo(str),
            ),
        ]

    message: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ListLexiconsInput(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "next_token",
                "NextToken",
                TypeInfo(str),
            ),
        ]

    # An opaque pagination token returned from previous `ListLexicons` operation.
    # If present, indicates where to continue the list of lexicons.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ListLexiconsOutput(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "lexicons",
                "Lexicons",
                TypeInfo(typing.List[LexiconDescription]),
            ),
            (
                "next_token",
                "NextToken",
                TypeInfo(str),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A list of lexicon names and attributes.
    lexicons: typing.List["LexiconDescription"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The pagination token to use in the next request to continue the listing of
    # lexicons. `NextToken` is returned only if the response is truncated.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ListSpeechSynthesisTasksInput(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "max_results",
                "MaxResults",
                TypeInfo(int),
            ),
            (
                "next_token",
                "NextToken",
                TypeInfo(str),
            ),
            (
                "status",
                "Status",
                TypeInfo(typing.Union[str, TaskStatus]),
            ),
        ]

    # Maximum number of speech synthesis tasks returned in a List operation.
    max_results: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The pagination token to use in the next request to continue the listing of
    # speech synthesis tasks.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Status of the speech synthesis tasks returned in a List operation
    status: typing.Union[str, "TaskStatus"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class ListSpeechSynthesisTasksOutput(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "next_token",
                "NextToken",
                TypeInfo(str),
            ),
            (
                "synthesis_tasks",
                "SynthesisTasks",
                TypeInfo(typing.List[SynthesisTask]),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # An opaque pagination token returned from the previous List operation in
    # this request. If present, this indicates where to continue the listing.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # List of SynthesisTask objects that provides information from the specified
    # task in the list request, including output format, creation time, task
    # status, and so on.
    synthesis_tasks: typing.List["SynthesisTask"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class MarksNotSupportedForFormatException(ShapeBase):
    """
    Speech marks are not supported for the `OutputFormat` selected. Speech marks are
    only available for content in `json` format.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "message",
                "message",
                TypeInfo(str),
            ),
        ]

    message: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class MaxLexemeLengthExceededException(ShapeBase):
    """
    The maximum size of the lexeme would be exceeded by this operation.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "message",
                "message",
                TypeInfo(str),
            ),
        ]

    message: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class MaxLexiconsNumberExceededException(ShapeBase):
    """
    The maximum number of lexicons would be exceeded by this operation.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "message",
                "message",
                TypeInfo(str),
            ),
        ]

    message: str = dataclasses.field(default=ShapeBase.NOT_SET, )


class OutputFormat(str):
    json = "json"
    mp3 = "mp3"
    ogg_vorbis = "ogg_vorbis"
    pcm = "pcm"


@dataclasses.dataclass
class PutLexiconInput(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "name",
                "Name",
                TypeInfo(str),
            ),
            (
                "content",
                "Content",
                TypeInfo(str),
            ),
        ]

    # Name of the lexicon. The name must follow the regular express format
    # [0-9A-Za-z]{1,20}. That is, the name is a case-sensitive alphanumeric
    # string up to 20 characters long.
    name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Content of the PLS lexicon as string data.
    content: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class PutLexiconOutput(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class ServiceFailureException(ShapeBase):
    """
    An unknown condition has caused a service failure.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "message",
                "message",
                TypeInfo(str),
            ),
        ]

    message: str = dataclasses.field(default=ShapeBase.NOT_SET, )


class SpeechMarkType(str):
    sentence = "sentence"
    ssml = "ssml"
    viseme = "viseme"
    word = "word"


@dataclasses.dataclass
class SsmlMarksNotSupportedForTextTypeException(ShapeBase):
    """
    SSML speech marks are not supported for plain text-type input.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "message",
                "message",
                TypeInfo(str),
            ),
        ]

    message: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class StartSpeechSynthesisTaskInput(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "output_format",
                "OutputFormat",
                TypeInfo(typing.Union[str, OutputFormat]),
            ),
            (
                "output_s3_bucket_name",
                "OutputS3BucketName",
                TypeInfo(str),
            ),
            (
                "text",
                "Text",
                TypeInfo(str),
            ),
            (
                "voice_id",
                "VoiceId",
                TypeInfo(typing.Union[str, VoiceId]),
            ),
            (
                "lexicon_names",
                "LexiconNames",
                TypeInfo(typing.List[str]),
            ),
            (
                "output_s3_key_prefix",
                "OutputS3KeyPrefix",
                TypeInfo(str),
            ),
            (
                "sample_rate",
                "SampleRate",
                TypeInfo(str),
            ),
            (
                "sns_topic_arn",
                "SnsTopicArn",
                TypeInfo(str),
            ),
            (
                "speech_mark_types",
                "SpeechMarkTypes",
                TypeInfo(typing.List[typing.Union[str, SpeechMarkType]]),
            ),
            (
                "text_type",
                "TextType",
                TypeInfo(typing.Union[str, TextType]),
            ),
            (
                "language_code",
                "LanguageCode",
                TypeInfo(typing.Union[str, LanguageCode]),
            ),
        ]

    # The format in which the returned output will be encoded. For audio stream,
    # this will be mp3, ogg_vorbis, or pcm. For speech marks, this will be json.
    output_format: typing.Union[str, "OutputFormat"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Amazon S3 bucket name to which the output file will be saved.
    output_s3_bucket_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The input text to synthesize. If you specify ssml as the TextType, follow
    # the SSML format for the input text.
    text: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Voice ID to use for the synthesis.
    voice_id: typing.Union[str, "VoiceId"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # List of one or more pronunciation lexicon names you want the service to
    # apply during synthesis. Lexicons are applied only if the language of the
    # lexicon is the same as the language of the voice.
    lexicon_names: typing.List[str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The Amazon S3 key prefix for the output speech file.
    output_s3_key_prefix: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The audio frequency specified in Hz.

    # The valid values for mp3 and ogg_vorbis are "8000", "16000", and "22050".
    # The default value is "22050".

    # Valid values for pcm are "8000" and "16000" The default value is "16000".
    sample_rate: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # ARN for the SNS topic optionally used for providing status notification for
    # a speech synthesis task.
    sns_topic_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The type of speech marks returned for the input text.
    speech_mark_types: typing.List[typing.Union[str, "SpeechMarkType"]
                                  ] = dataclasses.field(
                                      default=ShapeBase.NOT_SET,
                                  )

    # Specifies whether the input text is plain text or SSML. The default value
    # is plain text.
    text_type: typing.Union[str, "TextType"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Optional language code for the Speech Synthesis request. This is only
    # necessary if using a bilingual voice, such as Aditi, which can be used for
    # either Indian English (en-IN) or Hindi (hi-IN).

    # If a bilingual voice is used and no language code is specified, Amazon
    # Polly will use the default language of the bilingual voice. The default
    # language for any voice is the one returned by the
    # [DescribeVoices](https://docs.aws.amazon.com/polly/latest/dg/API_DescribeVoices.html)
    # operation for the `LanguageCode` parameter. For example, if no language
    # code is specified, Aditi will use Indian English rather than Hindi.
    language_code: typing.Union[str, "LanguageCode"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class StartSpeechSynthesisTaskOutput(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "synthesis_task",
                "SynthesisTask",
                TypeInfo(SynthesisTask),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # SynthesisTask object that provides information and attributes about a newly
    # submitted speech synthesis task.
    synthesis_task: "SynthesisTask" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class SynthesisTask(ShapeBase):
    """
    SynthesisTask object that provides information about a speech synthesis task.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "task_id",
                "TaskId",
                TypeInfo(str),
            ),
            (
                "task_status",
                "TaskStatus",
                TypeInfo(typing.Union[str, TaskStatus]),
            ),
            (
                "task_status_reason",
                "TaskStatusReason",
                TypeInfo(str),
            ),
            (
                "output_uri",
                "OutputUri",
                TypeInfo(str),
            ),
            (
                "creation_time",
                "CreationTime",
                TypeInfo(datetime.datetime),
            ),
            (
                "request_characters",
                "RequestCharacters",
                TypeInfo(int),
            ),
            (
                "sns_topic_arn",
                "SnsTopicArn",
                TypeInfo(str),
            ),
            (
                "lexicon_names",
                "LexiconNames",
                TypeInfo(typing.List[str]),
            ),
            (
                "output_format",
                "OutputFormat",
                TypeInfo(typing.Union[str, OutputFormat]),
            ),
            (
                "sample_rate",
                "SampleRate",
                TypeInfo(str),
            ),
            (
                "speech_mark_types",
                "SpeechMarkTypes",
                TypeInfo(typing.List[typing.Union[str, SpeechMarkType]]),
            ),
            (
                "text_type",
                "TextType",
                TypeInfo(typing.Union[str, TextType]),
            ),
            (
                "voice_id",
                "VoiceId",
                TypeInfo(typing.Union[str, VoiceId]),
            ),
            (
                "language_code",
                "LanguageCode",
                TypeInfo(typing.Union[str, LanguageCode]),
            ),
        ]

    # The Amazon Polly generated identifier for a speech synthesis task.
    task_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Current status of the individual speech synthesis task.
    task_status: typing.Union[str, "TaskStatus"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Reason for the current status of a specific speech synthesis task,
    # including errors if the task has failed.
    task_status_reason: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Pathway for the output speech file.
    output_uri: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Timestamp for the time the synthesis task was started.
    creation_time: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Number of billable characters synthesized.
    request_characters: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # ARN for the SNS topic optionally used for providing status notification for
    # a speech synthesis task.
    sns_topic_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # List of one or more pronunciation lexicon names you want the service to
    # apply during synthesis. Lexicons are applied only if the language of the
    # lexicon is the same as the language of the voice.
    lexicon_names: typing.List[str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The format in which the returned output will be encoded. For audio stream,
    # this will be mp3, ogg_vorbis, or pcm. For speech marks, this will be json.
    output_format: typing.Union[str, "OutputFormat"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The audio frequency specified in Hz.

    # The valid values for mp3 and ogg_vorbis are "8000", "16000", and "22050".
    # The default value is "22050".

    # Valid values for pcm are "8000" and "16000" The default value is "16000".
    sample_rate: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The type of speech marks returned for the input text.
    speech_mark_types: typing.List[typing.Union[str, "SpeechMarkType"]
                                  ] = dataclasses.field(
                                      default=ShapeBase.NOT_SET,
                                  )

    # Specifies whether the input text is plain text or SSML. The default value
    # is plain text.
    text_type: typing.Union[str, "TextType"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Voice ID to use for the synthesis.
    voice_id: typing.Union[str, "VoiceId"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Optional language code for a synthesis task. This is only necessary if
    # using a bilingual voice, such as Aditi, which can be used for either Indian
    # English (en-IN) or Hindi (hi-IN).

    # If a bilingual voice is used and no language code is specified, Amazon
    # Polly will use the default language of the bilingual voice. The default
    # language for any voice is the one returned by the
    # [DescribeVoices](https://docs.aws.amazon.com/polly/latest/dg/API_DescribeVoices.html)
    # operation for the `LanguageCode` parameter. For example, if no language
    # code is specified, Aditi will use Indian English rather than Hindi.
    language_code: typing.Union[str, "LanguageCode"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class SynthesisTaskNotFoundException(ShapeBase):
    """
    The Speech Synthesis task with requested Task ID cannot be found.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "message",
                "message",
                TypeInfo(str),
            ),
        ]

    message: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class SynthesizeSpeechInput(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "output_format",
                "OutputFormat",
                TypeInfo(typing.Union[str, OutputFormat]),
            ),
            (
                "text",
                "Text",
                TypeInfo(str),
            ),
            (
                "voice_id",
                "VoiceId",
                TypeInfo(typing.Union[str, VoiceId]),
            ),
            (
                "lexicon_names",
                "LexiconNames",
                TypeInfo(typing.List[str]),
            ),
            (
                "sample_rate",
                "SampleRate",
                TypeInfo(str),
            ),
            (
                "speech_mark_types",
                "SpeechMarkTypes",
                TypeInfo(typing.List[typing.Union[str, SpeechMarkType]]),
            ),
            (
                "text_type",
                "TextType",
                TypeInfo(typing.Union[str, TextType]),
            ),
            (
                "language_code",
                "LanguageCode",
                TypeInfo(typing.Union[str, LanguageCode]),
            ),
        ]

    # The format in which the returned output will be encoded. For audio stream,
    # this will be mp3, ogg_vorbis, or pcm. For speech marks, this will be json.

    # When pcm is used, the content returned is audio/pcm in a signed 16-bit, 1
    # channel (mono), little-endian format.
    output_format: typing.Union[str, "OutputFormat"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Input text to synthesize. If you specify `ssml` as the `TextType`, follow
    # the SSML format for the input text.
    text: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Voice ID to use for the synthesis. You can get a list of available voice
    # IDs by calling the
    # [DescribeVoices](http://docs.aws.amazon.com/polly/latest/dg/API_DescribeVoices.html)
    # operation.
    voice_id: typing.Union[str, "VoiceId"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # List of one or more pronunciation lexicon names you want the service to
    # apply during synthesis. Lexicons are applied only if the language of the
    # lexicon is the same as the language of the voice. For information about
    # storing lexicons, see
    # [PutLexicon](http://docs.aws.amazon.com/polly/latest/dg/API_PutLexicon.html).
    lexicon_names: typing.List[str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The audio frequency specified in Hz.

    # The valid values for `mp3` and `ogg_vorbis` are "8000", "16000", and
    # "22050". The default value is "22050".

    # Valid values for `pcm` are "8000" and "16000" The default value is "16000".
    sample_rate: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The type of speech marks returned for the input text.
    speech_mark_types: typing.List[typing.Union[str, "SpeechMarkType"]
                                  ] = dataclasses.field(
                                      default=ShapeBase.NOT_SET,
                                  )

    # Specifies whether the input text is plain text or SSML. The default value
    # is plain text. For more information, see [Using
    # SSML](http://docs.aws.amazon.com/polly/latest/dg/ssml.html).
    text_type: typing.Union[str, "TextType"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Optional language code for the Synthesize Speech request. This is only
    # necessary if using a bilingual voice, such as Aditi, which can be used for
    # either Indian English (en-IN) or Hindi (hi-IN).

    # If a bilingual voice is used and no language code is specified, Amazon
    # Polly will use the default language of the bilingual voice. The default
    # language for any voice is the one returned by the
    # [DescribeVoices](https://docs.aws.amazon.com/polly/latest/dg/API_DescribeVoices.html)
    # operation for the `LanguageCode` parameter. For example, if no language
    # code is specified, Aditi will use Indian English rather than Hindi.
    language_code: typing.Union[str, "LanguageCode"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class SynthesizeSpeechOutput(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "audio_stream",
                "AudioStream",
                TypeInfo(typing.Any),
            ),
            (
                "content_type",
                "ContentType",
                TypeInfo(str),
            ),
            (
                "request_characters",
                "RequestCharacters",
                TypeInfo(int),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Stream containing the synthesized speech.
    audio_stream: typing.Any = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Specifies the type audio stream. This should reflect the `OutputFormat`
    # parameter in your request.

    #   * If you request `mp3` as the `OutputFormat`, the `ContentType` returned is audio/mpeg.

    #   * If you request `ogg_vorbis` as the `OutputFormat`, the `ContentType` returned is audio/ogg.

    #   * If you request `pcm` as the `OutputFormat`, the `ContentType` returned is audio/pcm in a signed 16-bit, 1 channel (mono), little-endian format.

    #   * If you request `json` as the `OutputFormat`, the `ContentType` returned is audio/json.
    content_type: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Number of characters synthesized.
    request_characters: int = dataclasses.field(default=ShapeBase.NOT_SET, )


class TaskStatus(str):
    scheduled = "scheduled"
    inProgress = "inProgress"
    completed = "completed"
    failed = "failed"


@dataclasses.dataclass
class TextLengthExceededException(ShapeBase):
    """
    The value of the "Text" parameter is longer than the accepted limits. For the
    `SynthesizeSpeech` API, the limit for input text is a maximum of 6000 characters
    total, of which no more than 3000 can be billed characters. For the
    `StartSpeechSynthesisTask` API, the maximum is 200,000 characters, of which no
    more than 100,000 can be billed characters. SSML tags are not counted as billed
    characters.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "message",
                "message",
                TypeInfo(str),
            ),
        ]

    message: str = dataclasses.field(default=ShapeBase.NOT_SET, )


class TextType(str):
    ssml = "ssml"
    text = "text"


@dataclasses.dataclass
class UnsupportedPlsAlphabetException(ShapeBase):
    """
    The alphabet specified by the lexicon is not a supported alphabet. Valid values
    are `x-sampa` and `ipa`.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "message",
                "message",
                TypeInfo(str),
            ),
        ]

    message: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class UnsupportedPlsLanguageException(ShapeBase):
    """
    The language specified in the lexicon is unsupported. For a list of supported
    languages, see [Lexicon
    Attributes](http://docs.aws.amazon.com/polly/latest/dg/API_LexiconAttributes.html).
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "message",
                "message",
                TypeInfo(str),
            ),
        ]

    message: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class Voice(ShapeBase):
    """
    Description of the voice.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "gender",
                "Gender",
                TypeInfo(typing.Union[str, Gender]),
            ),
            (
                "id",
                "Id",
                TypeInfo(typing.Union[str, VoiceId]),
            ),
            (
                "language_code",
                "LanguageCode",
                TypeInfo(typing.Union[str, LanguageCode]),
            ),
            (
                "language_name",
                "LanguageName",
                TypeInfo(str),
            ),
            (
                "name",
                "Name",
                TypeInfo(str),
            ),
            (
                "additional_language_codes",
                "AdditionalLanguageCodes",
                TypeInfo(typing.List[typing.Union[str, LanguageCode]]),
            ),
        ]

    # Gender of the voice.
    gender: typing.Union[str, "Gender"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Amazon Polly assigned voice ID. This is the ID that you specify when
    # calling the `SynthesizeSpeech` operation.
    id: typing.Union[str, "VoiceId"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Language code of the voice.
    language_code: typing.Union[str, "LanguageCode"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Human readable name of the language in English.
    language_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Name of the voice (for example, Salli, Kendra, etc.). This provides a human
    # readable voice name that you might display in your application.
    name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Additional codes for languages available for the specified voice in
    # addition to its default language.

    # For example, the default language for Aditi is Indian English (en-IN)
    # because it was first used for that language. Since Aditi is bilingual and
    # fluent in both Indian English and Hindi, this parameter would show the code
    # `hi-IN`.
    additional_language_codes: typing.List[typing.Union[str, "LanguageCode"]
                                          ] = dataclasses.field(
                                              default=ShapeBase.NOT_SET,
                                          )


class VoiceId(str):
    Geraint = "Geraint"
    Gwyneth = "Gwyneth"
    Mads = "Mads"
    Naja = "Naja"
    Hans = "Hans"
    Marlene = "Marlene"
    Nicole = "Nicole"
    Russell = "Russell"
    Amy = "Amy"
    Brian = "Brian"
    Emma = "Emma"
    Raveena = "Raveena"
    Ivy = "Ivy"
    Joanna = "Joanna"
    Joey = "Joey"
    Justin = "Justin"
    Kendra = "Kendra"
    Kimberly = "Kimberly"
    Matthew = "Matthew"
    Salli = "Salli"
    Conchita = "Conchita"
    Enrique = "Enrique"
    Miguel = "Miguel"
    Penelope = "Penelope"
    Chantal = "Chantal"
    Celine = "Celine"
    Lea = "Lea"
    Mathieu = "Mathieu"
    Dora = "Dora"
    Karl = "Karl"
    Carla = "Carla"
    Giorgio = "Giorgio"
    Mizuki = "Mizuki"
    Liv = "Liv"
    Lotte = "Lotte"
    Ruben = "Ruben"
    Ewa = "Ewa"
    Jacek = "Jacek"
    Jan = "Jan"
    Maja = "Maja"
    Ricardo = "Ricardo"
    Vitoria = "Vitoria"
    Cristiano = "Cristiano"
    Ines = "Ines"
    Carmen = "Carmen"
    Maxim = "Maxim"
    Tatyana = "Tatyana"
    Astrid = "Astrid"
    Filiz = "Filiz"
    Vicki = "Vicki"
    Takumi = "Takumi"
    Seoyeon = "Seoyeon"
    Aditi = "Aditi"
    Zhiyu = "Zhiyu"
