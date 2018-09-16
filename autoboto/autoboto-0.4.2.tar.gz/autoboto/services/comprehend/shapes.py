import datetime
import typing
from autoboto import ShapeBase, OutputShapeBase, TypeInfo
import dataclasses


@dataclasses.dataclass
class BatchDetectDominantLanguageItemResult(ShapeBase):
    """
    The result of calling the operation. The operation returns one object for each
    document that is successfully processed by the operation.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "index",
                "Index",
                TypeInfo(int),
            ),
            (
                "languages",
                "Languages",
                TypeInfo(typing.List[DominantLanguage]),
            ),
        ]

    # The zero-based index of the document in the input list.
    index: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # One or more DominantLanguage objects describing the dominant languages in
    # the document.
    languages: typing.List["DominantLanguage"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class BatchDetectDominantLanguageRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "text_list",
                "TextList",
                TypeInfo(typing.List[str]),
            ),
        ]

    # A list containing the text of the input documents. The list can contain a
    # maximum of 25 documents. Each document should contain at least 20
    # characters and must contain fewer than 5,000 bytes of UTF-8 encoded
    # characters.
    text_list: typing.List[str] = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class BatchDetectDominantLanguageResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "result_list",
                "ResultList",
                TypeInfo(typing.List[BatchDetectDominantLanguageItemResult]),
            ),
            (
                "error_list",
                "ErrorList",
                TypeInfo(typing.List[BatchItemError]),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A list of objects containing the results of the operation. The results are
    # sorted in ascending order by the `Index` field and match the order of the
    # documents in the input list. If all of the documents contain an error, the
    # `ResultList` is empty.
    result_list: typing.List["BatchDetectDominantLanguageItemResult"
                            ] = dataclasses.field(
                                default=ShapeBase.NOT_SET,
                            )

    # A list containing one object for each document that contained an error. The
    # results are sorted in ascending order by the `Index` field and match the
    # order of the documents in the input list. If there are no errors in the
    # batch, the `ErrorList` is empty.
    error_list: typing.List["BatchItemError"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class BatchDetectEntitiesItemResult(ShapeBase):
    """
    The result of calling the operation. The operation returns one object for each
    document that is successfully processed by the operation.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "index",
                "Index",
                TypeInfo(int),
            ),
            (
                "entities",
                "Entities",
                TypeInfo(typing.List[Entity]),
            ),
        ]

    # The zero-based index of the document in the input list.
    index: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # One or more Entity objects, one for each entity detected in the document.
    entities: typing.List["Entity"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class BatchDetectEntitiesRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "text_list",
                "TextList",
                TypeInfo(typing.List[str]),
            ),
            (
                "language_code",
                "LanguageCode",
                TypeInfo(typing.Union[str, LanguageCode]),
            ),
        ]

    # A list containing the text of the input documents. The list can contain a
    # maximum of 25 documents. Each document must contain fewer than 5,000 bytes
    # of UTF-8 encoded characters.
    text_list: typing.List[str] = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The language of the input documents. You can specify English ("en") or
    # Spanish ("es"). All documents must be in the same language.
    language_code: typing.Union[str, "LanguageCode"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class BatchDetectEntitiesResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "result_list",
                "ResultList",
                TypeInfo(typing.List[BatchDetectEntitiesItemResult]),
            ),
            (
                "error_list",
                "ErrorList",
                TypeInfo(typing.List[BatchItemError]),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A list of objects containing the results of the operation. The results are
    # sorted in ascending order by the `Index` field and match the order of the
    # documents in the input list. If all of the documents contain an error, the
    # `ResultList` is empty.
    result_list: typing.List["BatchDetectEntitiesItemResult"
                            ] = dataclasses.field(
                                default=ShapeBase.NOT_SET,
                            )

    # A list containing one object for each document that contained an error. The
    # results are sorted in ascending order by the `Index` field and match the
    # order of the documents in the input list. If there are no errors in the
    # batch, the `ErrorList` is empty.
    error_list: typing.List["BatchItemError"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class BatchDetectKeyPhrasesItemResult(ShapeBase):
    """
    The result of calling the operation. The operation returns one object for each
    document that is successfully processed by the operation.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "index",
                "Index",
                TypeInfo(int),
            ),
            (
                "key_phrases",
                "KeyPhrases",
                TypeInfo(typing.List[KeyPhrase]),
            ),
        ]

    # The zero-based index of the document in the input list.
    index: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # One or more KeyPhrase objects, one for each key phrase detected in the
    # document.
    key_phrases: typing.List["KeyPhrase"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class BatchDetectKeyPhrasesRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "text_list",
                "TextList",
                TypeInfo(typing.List[str]),
            ),
            (
                "language_code",
                "LanguageCode",
                TypeInfo(typing.Union[str, LanguageCode]),
            ),
        ]

    # A list containing the text of the input documents. The list can contain a
    # maximum of 25 documents. Each document must contain fewer that 5,000 bytes
    # of UTF-8 encoded characters.
    text_list: typing.List[str] = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The language of the input documents. You can specify English ("en") or
    # Spanish ("es"). All documents must be in the same language.
    language_code: typing.Union[str, "LanguageCode"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class BatchDetectKeyPhrasesResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "result_list",
                "ResultList",
                TypeInfo(typing.List[BatchDetectKeyPhrasesItemResult]),
            ),
            (
                "error_list",
                "ErrorList",
                TypeInfo(typing.List[BatchItemError]),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A list of objects containing the results of the operation. The results are
    # sorted in ascending order by the `Index` field and match the order of the
    # documents in the input list. If all of the documents contain an error, the
    # `ResultList` is empty.
    result_list: typing.List["BatchDetectKeyPhrasesItemResult"
                            ] = dataclasses.field(
                                default=ShapeBase.NOT_SET,
                            )

    # A list containing one object for each document that contained an error. The
    # results are sorted in ascending order by the `Index` field and match the
    # order of the documents in the input list. If there are no errors in the
    # batch, the `ErrorList` is empty.
    error_list: typing.List["BatchItemError"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class BatchDetectSentimentItemResult(ShapeBase):
    """
    The result of calling the operation. The operation returns one object for each
    document that is successfully processed by the operation.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "index",
                "Index",
                TypeInfo(int),
            ),
            (
                "sentiment",
                "Sentiment",
                TypeInfo(typing.Union[str, SentimentType]),
            ),
            (
                "sentiment_score",
                "SentimentScore",
                TypeInfo(SentimentScore),
            ),
        ]

    # The zero-based index of the document in the input list.
    index: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The sentiment detected in the document.
    sentiment: typing.Union[str, "SentimentType"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The level of confidence that Amazon Comprehend has in the accuracy of its
    # sentiment detection.
    sentiment_score: "SentimentScore" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class BatchDetectSentimentRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "text_list",
                "TextList",
                TypeInfo(typing.List[str]),
            ),
            (
                "language_code",
                "LanguageCode",
                TypeInfo(typing.Union[str, LanguageCode]),
            ),
        ]

    # A list containing the text of the input documents. The list can contain a
    # maximum of 25 documents. Each document must contain fewer that 5,000 bytes
    # of UTF-8 encoded characters.
    text_list: typing.List[str] = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The language of the input documents. You can specify English ("en") or
    # Spanish ("es"). All documents must be in the same language.
    language_code: typing.Union[str, "LanguageCode"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class BatchDetectSentimentResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "result_list",
                "ResultList",
                TypeInfo(typing.List[BatchDetectSentimentItemResult]),
            ),
            (
                "error_list",
                "ErrorList",
                TypeInfo(typing.List[BatchItemError]),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A list of objects containing the results of the operation. The results are
    # sorted in ascending order by the `Index` field and match the order of the
    # documents in the input list. If all of the documents contain an error, the
    # `ResultList` is empty.
    result_list: typing.List["BatchDetectSentimentItemResult"
                            ] = dataclasses.field(
                                default=ShapeBase.NOT_SET,
                            )

    # A list containing one object for each document that contained an error. The
    # results are sorted in ascending order by the `Index` field and match the
    # order of the documents in the input list. If there are no errors in the
    # batch, the `ErrorList` is empty.
    error_list: typing.List["BatchItemError"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class BatchDetectSyntaxItemResult(ShapeBase):
    """
    The result of calling the operation. The operation returns one object that is
    successfully processed by the operation.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "index",
                "Index",
                TypeInfo(int),
            ),
            (
                "syntax_tokens",
                "SyntaxTokens",
                TypeInfo(typing.List[SyntaxToken]),
            ),
        ]

    # The zero-based index of the document in the input list.
    index: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The syntax tokens for the words in the document, one token for each word.
    syntax_tokens: typing.List["SyntaxToken"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class BatchDetectSyntaxRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "text_list",
                "TextList",
                TypeInfo(typing.List[str]),
            ),
            (
                "language_code",
                "LanguageCode",
                TypeInfo(typing.Union[str, SyntaxLanguageCode]),
            ),
        ]

    # A list containing the text of the input documents. The list can contain a
    # maximum of 25 documents. Each document must contain fewer that 5,000 bytes
    # of UTF-8 encoded characters.
    text_list: typing.List[str] = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The language of the input documents. You can specify English ("en") or
    # Spanish ("es"). All documents must be in the same language.
    language_code: typing.Union[str, "SyntaxLanguageCode"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class BatchDetectSyntaxResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "result_list",
                "ResultList",
                TypeInfo(typing.List[BatchDetectSyntaxItemResult]),
            ),
            (
                "error_list",
                "ErrorList",
                TypeInfo(typing.List[BatchItemError]),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A list of objects containing the results of the operation. The results are
    # sorted in ascending order by the `Index` field and match the order of the
    # documents in the input list. If all of the documents contain an error, the
    # `ResultList` is empty.
    result_list: typing.List["BatchDetectSyntaxItemResult"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A list containing one object for each document that contained an error. The
    # results are sorted in ascending order by the `Index` field and match the
    # order of the documents in the input list. If there are no errors in the
    # batch, the `ErrorList` is empty.
    error_list: typing.List["BatchItemError"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class BatchItemError(ShapeBase):
    """
    Describes an error that occurred while processing a document in a batch. The
    operation returns on `BatchItemError` object for each document that contained an
    error.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "index",
                "Index",
                TypeInfo(int),
            ),
            (
                "error_code",
                "ErrorCode",
                TypeInfo(str),
            ),
            (
                "error_message",
                "ErrorMessage",
                TypeInfo(str),
            ),
        ]

    # The zero-based index of the document in the input list.
    index: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The numeric error code of the error.
    error_code: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A text description of the error.
    error_message: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class BatchSizeLimitExceededException(ShapeBase):
    """
    The number of documents in the request exceeds the limit of 25. Try your request
    again with fewer documents.
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
class DescribeDominantLanguageDetectionJobRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "job_id",
                "JobId",
                TypeInfo(str),
            ),
        ]

    # The identifier that Amazon Comprehend generated for the job. The operation
    # returns this identifier in its response.
    job_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DescribeDominantLanguageDetectionJobResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "dominant_language_detection_job_properties",
                "DominantLanguageDetectionJobProperties",
                TypeInfo(DominantLanguageDetectionJobProperties),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # An object that contains the properties associated with a dominant language
    # detection job.
    dominant_language_detection_job_properties: "DominantLanguageDetectionJobProperties" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class DescribeEntitiesDetectionJobRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "job_id",
                "JobId",
                TypeInfo(str),
            ),
        ]

    # The identifier that Amazon Comprehend generated for the job. The operation
    # returns this identifier in its response.
    job_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DescribeEntitiesDetectionJobResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "entities_detection_job_properties",
                "EntitiesDetectionJobProperties",
                TypeInfo(EntitiesDetectionJobProperties),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # An object that contains the properties associated with an entities
    # detection job.
    entities_detection_job_properties: "EntitiesDetectionJobProperties" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class DescribeKeyPhrasesDetectionJobRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "job_id",
                "JobId",
                TypeInfo(str),
            ),
        ]

    # The identifier that Amazon Comprehend generated for the job. The operation
    # returns this identifier in its response.
    job_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DescribeKeyPhrasesDetectionJobResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "key_phrases_detection_job_properties",
                "KeyPhrasesDetectionJobProperties",
                TypeInfo(KeyPhrasesDetectionJobProperties),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # An object that contains the properties associated with a key phrases
    # detection job.
    key_phrases_detection_job_properties: "KeyPhrasesDetectionJobProperties" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class DescribeSentimentDetectionJobRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "job_id",
                "JobId",
                TypeInfo(str),
            ),
        ]

    # The identifier that Amazon Comprehend generated for the job. The operation
    # returns this identifier in its response.
    job_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DescribeSentimentDetectionJobResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "sentiment_detection_job_properties",
                "SentimentDetectionJobProperties",
                TypeInfo(SentimentDetectionJobProperties),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # An object that contains the properties associated with a sentiment
    # detection job.
    sentiment_detection_job_properties: "SentimentDetectionJobProperties" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class DescribeTopicsDetectionJobRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "job_id",
                "JobId",
                TypeInfo(str),
            ),
        ]

    # The identifier assigned by the user to the detection job.
    job_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DescribeTopicsDetectionJobResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "topics_detection_job_properties",
                "TopicsDetectionJobProperties",
                TypeInfo(TopicsDetectionJobProperties),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The list of properties for the requested job.
    topics_detection_job_properties: "TopicsDetectionJobProperties" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class DetectDominantLanguageRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "text",
                "Text",
                TypeInfo(str),
            ),
        ]

    # A UTF-8 text string. Each string should contain at least 20 characters and
    # must contain fewer that 5,000 bytes of UTF-8 encoded characters.
    text: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DetectDominantLanguageResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "languages",
                "Languages",
                TypeInfo(typing.List[DominantLanguage]),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The languages that Amazon Comprehend detected in the input text. For each
    # language, the response returns the RFC 5646 language code and the level of
    # confidence that Amazon Comprehend has in the accuracy of its inference. For
    # more information about RFC 5646, see [Tags for Identifying
    # Languages](https://tools.ietf.org/html/rfc5646) on the _IETF Tools_ web
    # site.
    languages: typing.List["DominantLanguage"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class DetectEntitiesRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "text",
                "Text",
                TypeInfo(str),
            ),
            (
                "language_code",
                "LanguageCode",
                TypeInfo(typing.Union[str, LanguageCode]),
            ),
        ]

    # A UTF-8 text string. Each string must contain fewer that 5,000 bytes of
    # UTF-8 encoded characters.
    text: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The language of the input documents. You can specify English ("en") or
    # Spanish ("es"). All documents must be in the same language.
    language_code: typing.Union[str, "LanguageCode"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class DetectEntitiesResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "entities",
                "Entities",
                TypeInfo(typing.List[Entity]),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A collection of entities identified in the input text. For each entity, the
    # response provides the entity text, entity type, where the entity text
    # begins and ends, and the level of confidence that Amazon Comprehend has in
    # the detection. For a list of entity types, see how-entities.
    entities: typing.List["Entity"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class DetectKeyPhrasesRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "text",
                "Text",
                TypeInfo(str),
            ),
            (
                "language_code",
                "LanguageCode",
                TypeInfo(typing.Union[str, LanguageCode]),
            ),
        ]

    # A UTF-8 text string. Each string must contain fewer that 5,000 bytes of
    # UTF-8 encoded characters.
    text: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The language of the input documents. You can specify English ("en") or
    # Spanish ("es"). All documents must be in the same language.
    language_code: typing.Union[str, "LanguageCode"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class DetectKeyPhrasesResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "key_phrases",
                "KeyPhrases",
                TypeInfo(typing.List[KeyPhrase]),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A collection of key phrases that Amazon Comprehend identified in the input
    # text. For each key phrase, the response provides the text of the key
    # phrase, where the key phrase begins and ends, and the level of confidence
    # that Amazon Comprehend has in the accuracy of the detection.
    key_phrases: typing.List["KeyPhrase"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class DetectSentimentRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "text",
                "Text",
                TypeInfo(str),
            ),
            (
                "language_code",
                "LanguageCode",
                TypeInfo(typing.Union[str, LanguageCode]),
            ),
        ]

    # A UTF-8 text string. Each string must contain fewer that 5,000 bytes of
    # UTF-8 encoded characters.
    text: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The language of the input documents. You can specify English ("en") or
    # Spanish ("es"). All documents must be in the same language.
    language_code: typing.Union[str, "LanguageCode"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class DetectSentimentResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "sentiment",
                "Sentiment",
                TypeInfo(typing.Union[str, SentimentType]),
            ),
            (
                "sentiment_score",
                "SentimentScore",
                TypeInfo(SentimentScore),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The inferred sentiment that Amazon Comprehend has the highest level of
    # confidence in.
    sentiment: typing.Union[str, "SentimentType"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # An object that lists the sentiments, and their corresponding confidence
    # levels.
    sentiment_score: "SentimentScore" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class DetectSyntaxRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "text",
                "Text",
                TypeInfo(str),
            ),
            (
                "language_code",
                "LanguageCode",
                TypeInfo(typing.Union[str, SyntaxLanguageCode]),
            ),
        ]

    # A UTF-8 string. Each string must contain fewer that 5,000 bytes of UTF
    # encoded characters.
    text: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The language code of the input documents. You can specify English ("en") or
    # Spanish ("es").
    language_code: typing.Union[str, "SyntaxLanguageCode"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class DetectSyntaxResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "syntax_tokens",
                "SyntaxTokens",
                TypeInfo(typing.List[SyntaxToken]),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A collection of syntax tokens describing the text. For each token, the
    # response provides the text, the token type, where the text begins and ends,
    # and the level of confidence that Amazon Comprehend has that the token is
    # correct. For a list of token types, see how-syntax.
    syntax_tokens: typing.List["SyntaxToken"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class DominantLanguage(ShapeBase):
    """
    Returns the code for the dominant language in the input text and the level of
    confidence that Amazon Comprehend has in the accuracy of the detection.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "language_code",
                "LanguageCode",
                TypeInfo(str),
            ),
            (
                "score",
                "Score",
                TypeInfo(float),
            ),
        ]

    # The RFC 5646 language code for the dominant language. For more information
    # about RFC 5646, see [Tags for Identifying
    # Languages](https://tools.ietf.org/html/rfc5646) on the _IETF Tools_ web
    # site.
    language_code: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The level of confidence that Amazon Comprehend has in the accuracy of the
    # detection.
    score: float = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DominantLanguageDetectionJobFilter(ShapeBase):
    """
    Provides information for filtering a list of dominant language detection jobs.
    For more information, see the operation.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "job_name",
                "JobName",
                TypeInfo(str),
            ),
            (
                "job_status",
                "JobStatus",
                TypeInfo(typing.Union[str, JobStatus]),
            ),
            (
                "submit_time_before",
                "SubmitTimeBefore",
                TypeInfo(datetime.datetime),
            ),
            (
                "submit_time_after",
                "SubmitTimeAfter",
                TypeInfo(datetime.datetime),
            ),
        ]

    # Filters on the name of the job.
    job_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Filters the list of jobs based on job status. Returns only jobs with the
    # specified status.
    job_status: typing.Union[str, "JobStatus"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Filters the list of jobs based on the time that the job was submitted for
    # processing. Returns only jobs submitted before the specified time. Jobs are
    # returned in ascending order, oldest to newest.
    submit_time_before: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Filters the list of jobs based on the time that the job was submitted for
    # processing. Returns only jobs submitted after the specified time. Jobs are
    # returned in descending order, newest to oldest.
    submit_time_after: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class DominantLanguageDetectionJobProperties(ShapeBase):
    """
    Provides information about a dominant language detection job.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "job_id",
                "JobId",
                TypeInfo(str),
            ),
            (
                "job_name",
                "JobName",
                TypeInfo(str),
            ),
            (
                "job_status",
                "JobStatus",
                TypeInfo(typing.Union[str, JobStatus]),
            ),
            (
                "message",
                "Message",
                TypeInfo(str),
            ),
            (
                "submit_time",
                "SubmitTime",
                TypeInfo(datetime.datetime),
            ),
            (
                "end_time",
                "EndTime",
                TypeInfo(datetime.datetime),
            ),
            (
                "input_data_config",
                "InputDataConfig",
                TypeInfo(InputDataConfig),
            ),
            (
                "output_data_config",
                "OutputDataConfig",
                TypeInfo(OutputDataConfig),
            ),
            (
                "data_access_role_arn",
                "DataAccessRoleArn",
                TypeInfo(str),
            ),
        ]

    # The identifier assigned to the dominant language detection job.
    job_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The name that you assigned to the dominant language detection job.
    job_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The current status of the dominant language detection job. If the status is
    # `FAILED`, the `Message` field shows the reason for the failure.
    job_status: typing.Union[str, "JobStatus"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A description for the status of a job.
    message: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The time that the dominant language detection job was submitted for
    # processing.
    submit_time: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The time that the dominant language detection job completed.
    end_time: datetime.datetime = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The input data configuration that you supplied when you created the
    # dominant language detection job.
    input_data_config: "InputDataConfig" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The output data configuration that you supplied when you created the
    # dominant language detection job.
    output_data_config: "OutputDataConfig" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The Amazon Resource Name (ARN) that gives Amazon Comprehend read access to
    # your input data.
    data_access_role_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class EntitiesDetectionJobFilter(ShapeBase):
    """
    Provides information for filtering a list of dominant language detection jobs.
    For more information, see the operation.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "job_name",
                "JobName",
                TypeInfo(str),
            ),
            (
                "job_status",
                "JobStatus",
                TypeInfo(typing.Union[str, JobStatus]),
            ),
            (
                "submit_time_before",
                "SubmitTimeBefore",
                TypeInfo(datetime.datetime),
            ),
            (
                "submit_time_after",
                "SubmitTimeAfter",
                TypeInfo(datetime.datetime),
            ),
        ]

    # Filters on the name of the job.
    job_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Filters the list of jobs based on job status. Returns only jobs with the
    # specified status.
    job_status: typing.Union[str, "JobStatus"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Filters the list of jobs based on the time that the job was submitted for
    # processing. Returns only jobs submitted before the specified time. Jobs are
    # returned in ascending order, oldest to newest.
    submit_time_before: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Filters the list of jobs based on the time that the job was submitted for
    # processing. Returns only jobs submitted after the specified time. Jobs are
    # returned in descending order, newest to oldest.
    submit_time_after: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class EntitiesDetectionJobProperties(ShapeBase):
    """
    Provides information about an entities detection job.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "job_id",
                "JobId",
                TypeInfo(str),
            ),
            (
                "job_name",
                "JobName",
                TypeInfo(str),
            ),
            (
                "job_status",
                "JobStatus",
                TypeInfo(typing.Union[str, JobStatus]),
            ),
            (
                "message",
                "Message",
                TypeInfo(str),
            ),
            (
                "submit_time",
                "SubmitTime",
                TypeInfo(datetime.datetime),
            ),
            (
                "end_time",
                "EndTime",
                TypeInfo(datetime.datetime),
            ),
            (
                "input_data_config",
                "InputDataConfig",
                TypeInfo(InputDataConfig),
            ),
            (
                "output_data_config",
                "OutputDataConfig",
                TypeInfo(OutputDataConfig),
            ),
            (
                "language_code",
                "LanguageCode",
                TypeInfo(typing.Union[str, LanguageCode]),
            ),
            (
                "data_access_role_arn",
                "DataAccessRoleArn",
                TypeInfo(str),
            ),
        ]

    # The identifier assigned to the entities detection job.
    job_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The name that you assigned the entities detection job.
    job_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The current status of the entities detection job. If the status is
    # `FAILED`, the `Message` field shows the reason for the failure.
    job_status: typing.Union[str, "JobStatus"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A description of the status of a job.
    message: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The time that the entities detection job was submitted for processing.
    submit_time: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The time that the entities detection job completed
    end_time: datetime.datetime = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The input data configuration that you supplied when you created the
    # entities detection job.
    input_data_config: "InputDataConfig" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The output data configuration that you supplied when you created the
    # entities detection job.
    output_data_config: "OutputDataConfig" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The language code of the input documents.
    language_code: typing.Union[str, "LanguageCode"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The Amazon Resource Name (ARN) that gives Amazon Comprehend read access to
    # your input data.
    data_access_role_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class Entity(ShapeBase):
    """
    Provides information about an entity.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "score",
                "Score",
                TypeInfo(float),
            ),
            (
                "type",
                "Type",
                TypeInfo(typing.Union[str, EntityType]),
            ),
            (
                "text",
                "Text",
                TypeInfo(str),
            ),
            (
                "begin_offset",
                "BeginOffset",
                TypeInfo(int),
            ),
            (
                "end_offset",
                "EndOffset",
                TypeInfo(int),
            ),
        ]

    # The level of confidence that Amazon Comprehend has in the accuracy of the
    # detection.
    score: float = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The entity's type.
    type: typing.Union[str, "EntityType"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The text of the entity.
    text: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A character offset in the input text that shows where the entity begins
    # (the first character is at position 0). The offset returns the position of
    # each UTF-8 code point in the string. A _code point_ is the abstract
    # character from a particular graphical representation. For example, a multi-
    # byte UTF-8 character maps to a single code point.
    begin_offset: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A character offset in the input text that shows where the entity ends. The
    # offset returns the position of each UTF-8 code point in the string. A _code
    # point_ is the abstract character from a particular graphical
    # representation. For example, a multi-byte UTF-8 character maps to a single
    # code point.
    end_offset: int = dataclasses.field(default=ShapeBase.NOT_SET, )


class EntityType(str):
    PERSON = "PERSON"
    LOCATION = "LOCATION"
    ORGANIZATION = "ORGANIZATION"
    COMMERCIAL_ITEM = "COMMERCIAL_ITEM"
    EVENT = "EVENT"
    DATE = "DATE"
    QUANTITY = "QUANTITY"
    TITLE = "TITLE"
    OTHER = "OTHER"


@dataclasses.dataclass
class InputDataConfig(ShapeBase):
    """
    The input properties for a topic detection job.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "s3_uri",
                "S3Uri",
                TypeInfo(str),
            ),
            (
                "input_format",
                "InputFormat",
                TypeInfo(typing.Union[str, InputFormat]),
            ),
        ]

    # The Amazon S3 URI for the input data. The URI must be in same region as the
    # API endpoint that you are calling. The URI can point to a single input file
    # or it can provide the prefix for a collection of data files.

    # For example, if you use the URI `S3://bucketName/prefix`, if the prefix is
    # a single file, Amazon Comprehend uses that file as input. If more than one
    # file begins with the prefix, Amazon Comprehend uses all of them as input.
    s3_uri: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Specifies how the text in an input file should be processed:

    #   * `ONE_DOC_PER_FILE` \- Each file is considered a separate document. Use this option when you are processing large documents, such as newspaper articles or scientific papers.

    #   * `ONE_DOC_PER_LINE` \- Each line in a file is considered a separate document. Use this option when you are processing many short documents, such as text messages.
    input_format: typing.Union[str, "InputFormat"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


class InputFormat(str):
    ONE_DOC_PER_FILE = "ONE_DOC_PER_FILE"
    ONE_DOC_PER_LINE = "ONE_DOC_PER_LINE"


@dataclasses.dataclass
class InternalServerException(ShapeBase):
    """
    An internal server error occurred. Retry your request.
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
class InvalidFilterException(ShapeBase):
    """
    The filter specified for the `ListTopicDetectionJobs` operation is invalid.
    Specify a different filter.
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
class InvalidRequestException(ShapeBase):
    """
    The request is invalid.
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
class JobNotFoundException(ShapeBase):
    """
    The specified job was not found. Check the job ID and try again.
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


class JobStatus(str):
    SUBMITTED = "SUBMITTED"
    IN_PROGRESS = "IN_PROGRESS"
    COMPLETED = "COMPLETED"
    FAILED = "FAILED"
    STOP_REQUESTED = "STOP_REQUESTED"
    STOPPED = "STOPPED"


@dataclasses.dataclass
class KeyPhrase(ShapeBase):
    """
    Describes a key noun phrase.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "score",
                "Score",
                TypeInfo(float),
            ),
            (
                "text",
                "Text",
                TypeInfo(str),
            ),
            (
                "begin_offset",
                "BeginOffset",
                TypeInfo(int),
            ),
            (
                "end_offset",
                "EndOffset",
                TypeInfo(int),
            ),
        ]

    # The level of confidence that Amazon Comprehend has in the accuracy of the
    # detection.
    score: float = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The text of a key noun phrase.
    text: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A character offset in the input text that shows where the key phrase begins
    # (the first character is at position 0). The offset returns the position of
    # each UTF-8 code point in the string. A _code point_ is the abstract
    # character from a particular graphical representation. For example, a multi-
    # byte UTF-8 character maps to a single code point.
    begin_offset: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A character offset in the input text where the key phrase ends. The offset
    # returns the position of each UTF-8 code point in the string. A `code point`
    # is the abstract character from a particular graphical representation. For
    # example, a multi-byte UTF-8 character maps to a single code point.
    end_offset: int = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class KeyPhrasesDetectionJobFilter(ShapeBase):
    """
    Provides information for filtering a list of dominant language detection jobs.
    For more information, see the operation.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "job_name",
                "JobName",
                TypeInfo(str),
            ),
            (
                "job_status",
                "JobStatus",
                TypeInfo(typing.Union[str, JobStatus]),
            ),
            (
                "submit_time_before",
                "SubmitTimeBefore",
                TypeInfo(datetime.datetime),
            ),
            (
                "submit_time_after",
                "SubmitTimeAfter",
                TypeInfo(datetime.datetime),
            ),
        ]

    # Filters on the name of the job.
    job_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Filters the list of jobs based on job status. Returns only jobs with the
    # specified status.
    job_status: typing.Union[str, "JobStatus"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Filters the list of jobs based on the time that the job was submitted for
    # processing. Returns only jobs submitted before the specified time. Jobs are
    # returned in ascending order, oldest to newest.
    submit_time_before: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Filters the list of jobs based on the time that the job was submitted for
    # processing. Returns only jobs submitted after the specified time. Jobs are
    # returned in descending order, newest to oldest.
    submit_time_after: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class KeyPhrasesDetectionJobProperties(ShapeBase):
    """
    Provides information about a key phrases detection job.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "job_id",
                "JobId",
                TypeInfo(str),
            ),
            (
                "job_name",
                "JobName",
                TypeInfo(str),
            ),
            (
                "job_status",
                "JobStatus",
                TypeInfo(typing.Union[str, JobStatus]),
            ),
            (
                "message",
                "Message",
                TypeInfo(str),
            ),
            (
                "submit_time",
                "SubmitTime",
                TypeInfo(datetime.datetime),
            ),
            (
                "end_time",
                "EndTime",
                TypeInfo(datetime.datetime),
            ),
            (
                "input_data_config",
                "InputDataConfig",
                TypeInfo(InputDataConfig),
            ),
            (
                "output_data_config",
                "OutputDataConfig",
                TypeInfo(OutputDataConfig),
            ),
            (
                "language_code",
                "LanguageCode",
                TypeInfo(typing.Union[str, LanguageCode]),
            ),
            (
                "data_access_role_arn",
                "DataAccessRoleArn",
                TypeInfo(str),
            ),
        ]

    # The identifier assigned to the key phrases detection job.
    job_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The name that you assigned the key phrases detection job.
    job_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The current status of the key phrases detection job. If the status is
    # `FAILED`, the `Message` field shows the reason for the failure.
    job_status: typing.Union[str, "JobStatus"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A description of the status of a job.
    message: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The time that the key phrases detection job was submitted for processing.
    submit_time: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The time that the key phrases detection job completed.
    end_time: datetime.datetime = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The input data configuration that you supplied when you created the key
    # phrases detection job.
    input_data_config: "InputDataConfig" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The output data configuration that you supplied when you created the key
    # phrases detection job.
    output_data_config: "OutputDataConfig" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The language code of the input documents.
    language_code: typing.Union[str, "LanguageCode"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The Amazon Resource Name (ARN) that gives Amazon Comprehend read access to
    # your input data.
    data_access_role_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )


class LanguageCode(str):
    en = "en"
    es = "es"


@dataclasses.dataclass
class ListDominantLanguageDetectionJobsRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "filter",
                "Filter",
                TypeInfo(DominantLanguageDetectionJobFilter),
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

    # Filters that jobs that are returned. You can filter jobs on their name,
    # status, or the date and time that they were submitted. You can only set one
    # filter at a time.
    filter: "DominantLanguageDetectionJobFilter" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Identifies the next page of results to return.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The maximum number of results to return in each page. The default is 100.
    max_results: int = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ListDominantLanguageDetectionJobsResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "dominant_language_detection_job_properties_list",
                "DominantLanguageDetectionJobPropertiesList",
                TypeInfo(typing.List[DominantLanguageDetectionJobProperties]),
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

    # A list containing the properties of each job that is returned.
    dominant_language_detection_job_properties_list: typing.List[
        "DominantLanguageDetectionJobProperties"] = dataclasses.field(
            default=ShapeBase.NOT_SET,
        )

    # Identifies the next page of results to return.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ListEntitiesDetectionJobsRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "filter",
                "Filter",
                TypeInfo(EntitiesDetectionJobFilter),
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

    # Filters the jobs that are returned. You can filter jobs on their name,
    # status, or the date and time that they were submitted. You can only set one
    # filter at a time.
    filter: "EntitiesDetectionJobFilter" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Identifies the next page of results to return.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The maximum number of results to return in each page. The default is 100.
    max_results: int = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ListEntitiesDetectionJobsResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "entities_detection_job_properties_list",
                "EntitiesDetectionJobPropertiesList",
                TypeInfo(typing.List[EntitiesDetectionJobProperties]),
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

    # A list containing the properties of each job that is returned.
    entities_detection_job_properties_list: typing.List[
        "EntitiesDetectionJobProperties"] = dataclasses.field(
            default=ShapeBase.NOT_SET,
        )

    # Identifies the next page of results to return.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ListKeyPhrasesDetectionJobsRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "filter",
                "Filter",
                TypeInfo(KeyPhrasesDetectionJobFilter),
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

    # Filters the jobs that are returned. You can filter jobs on their name,
    # status, or the date and time that they were submitted. You can only set one
    # filter at a time.
    filter: "KeyPhrasesDetectionJobFilter" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Identifies the next page of results to return.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The maximum number of results to return in each page. The default is 100.
    max_results: int = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ListKeyPhrasesDetectionJobsResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "key_phrases_detection_job_properties_list",
                "KeyPhrasesDetectionJobPropertiesList",
                TypeInfo(typing.List[KeyPhrasesDetectionJobProperties]),
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

    # A list containing the properties of each job that is returned.
    key_phrases_detection_job_properties_list: typing.List[
        "KeyPhrasesDetectionJobProperties"] = dataclasses.field(
            default=ShapeBase.NOT_SET,
        )

    # Identifies the next page of results to return.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ListSentimentDetectionJobsRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "filter",
                "Filter",
                TypeInfo(SentimentDetectionJobFilter),
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

    # Filters the jobs that are returned. You can filter jobs on their name,
    # status, or the date and time that they were submitted. You can only set one
    # filter at a time.
    filter: "SentimentDetectionJobFilter" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Identifies the next page of results to return.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The maximum number of results to return in each page. The default is 100.
    max_results: int = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ListSentimentDetectionJobsResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "sentiment_detection_job_properties_list",
                "SentimentDetectionJobPropertiesList",
                TypeInfo(typing.List[SentimentDetectionJobProperties]),
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

    # A list containing the properties of each job that is returned.
    sentiment_detection_job_properties_list: typing.List[
        "SentimentDetectionJobProperties"] = dataclasses.field(
            default=ShapeBase.NOT_SET,
        )

    # Identifies the next page of results to return.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ListTopicsDetectionJobsRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "filter",
                "Filter",
                TypeInfo(TopicsDetectionJobFilter),
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

    # Filters the jobs that are returned. Jobs can be filtered on their name,
    # status, or the date and time that they were submitted. You can set only one
    # filter at a time.
    filter: "TopicsDetectionJobFilter" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Identifies the next page of results to return.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The maximum number of results to return in each page. The default is 100.
    max_results: int = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ListTopicsDetectionJobsResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "topics_detection_job_properties_list",
                "TopicsDetectionJobPropertiesList",
                TypeInfo(typing.List[TopicsDetectionJobProperties]),
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

    # A list containing the properties of each job that is returned.
    topics_detection_job_properties_list: typing.List[
        "TopicsDetectionJobProperties"] = dataclasses.field(
            default=ShapeBase.NOT_SET,
        )

    # Identifies the next page of results to return.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    def paginate(
        self,
    ) -> typing.Generator["ListTopicsDetectionJobsResponse", None, None]:
        yield from super()._paginate()


@dataclasses.dataclass
class OutputDataConfig(ShapeBase):
    """
    Provides configuration parameters for the output of topic detection jobs.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "s3_uri",
                "S3Uri",
                TypeInfo(str),
            ),
        ]

    # When you use the `OutputDataConfig` object with asynchronous operations,
    # you specify the Amazon S3 location where you want to write the output data.
    # The URI must be in the same region as the API endpoint that you are
    # calling. The location is used as the prefix for the actual location of the
    # output file.

    # When the topic detection job is finished, the service creates an output
    # file in a directory specific to the job. The `S3Uri` field contains the
    # location of the output file, called `output.tar.gz`. It is a compressed
    # archive that contains the ouput of the operation.
    s3_uri: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class PartOfSpeechTag(ShapeBase):
    """
    Identifies the part of speech represented by the token and gives the confidence
    that Amazon Comprehend has that the part of speech was correctly identified. For
    more information about the parts of speech that Amazon Comprehend can identify,
    see how-syntax.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "tag",
                "Tag",
                TypeInfo(typing.Union[str, PartOfSpeechTagType]),
            ),
            (
                "score",
                "Score",
                TypeInfo(float),
            ),
        ]

    # Identifies the part of speech that the token represents.
    tag: typing.Union[str, "PartOfSpeechTagType"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The confidence that Amazon Comprehend has that the part of speech was
    # correctly identified.
    score: float = dataclasses.field(default=ShapeBase.NOT_SET, )


class PartOfSpeechTagType(str):
    ADJ = "ADJ"
    ADP = "ADP"
    ADV = "ADV"
    AUX = "AUX"
    CONJ = "CONJ"
    DET = "DET"
    INTJ = "INTJ"
    NOUN = "NOUN"
    NUM = "NUM"
    O = "O"
    PART = "PART"
    PRON = "PRON"
    PROPN = "PROPN"
    PUNCT = "PUNCT"
    SCONJ = "SCONJ"
    SYM = "SYM"
    VERB = "VERB"


@dataclasses.dataclass
class SentimentDetectionJobFilter(ShapeBase):
    """
    Provides information for filtering a list of dominant language detection jobs.
    For more information, see the operation.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "job_name",
                "JobName",
                TypeInfo(str),
            ),
            (
                "job_status",
                "JobStatus",
                TypeInfo(typing.Union[str, JobStatus]),
            ),
            (
                "submit_time_before",
                "SubmitTimeBefore",
                TypeInfo(datetime.datetime),
            ),
            (
                "submit_time_after",
                "SubmitTimeAfter",
                TypeInfo(datetime.datetime),
            ),
        ]

    # Filters on the name of the job.
    job_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Filters the list of jobs based on job status. Returns only jobs with the
    # specified status.
    job_status: typing.Union[str, "JobStatus"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Filters the list of jobs based on the time that the job was submitted for
    # processing. Returns only jobs submitted before the specified time. Jobs are
    # returned in ascending order, oldest to newest.
    submit_time_before: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Filters the list of jobs based on the time that the job was submitted for
    # processing. Returns only jobs submitted after the specified time. Jobs are
    # returned in descending order, newest to oldest.
    submit_time_after: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class SentimentDetectionJobProperties(ShapeBase):
    """
    Provides information about a sentiment detection job.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "job_id",
                "JobId",
                TypeInfo(str),
            ),
            (
                "job_name",
                "JobName",
                TypeInfo(str),
            ),
            (
                "job_status",
                "JobStatus",
                TypeInfo(typing.Union[str, JobStatus]),
            ),
            (
                "message",
                "Message",
                TypeInfo(str),
            ),
            (
                "submit_time",
                "SubmitTime",
                TypeInfo(datetime.datetime),
            ),
            (
                "end_time",
                "EndTime",
                TypeInfo(datetime.datetime),
            ),
            (
                "input_data_config",
                "InputDataConfig",
                TypeInfo(InputDataConfig),
            ),
            (
                "output_data_config",
                "OutputDataConfig",
                TypeInfo(OutputDataConfig),
            ),
            (
                "language_code",
                "LanguageCode",
                TypeInfo(typing.Union[str, LanguageCode]),
            ),
            (
                "data_access_role_arn",
                "DataAccessRoleArn",
                TypeInfo(str),
            ),
        ]

    # The identifier assigned to the sentiment detection job.
    job_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The name that you assigned to the sentiment detection job
    job_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The current status of the sentiment detection job. If the status is
    # `FAILED`, the `Messages` field shows the reason for the failure.
    job_status: typing.Union[str, "JobStatus"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A description of the status of a job.
    message: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The time that the sentiment detection job was submitted for processing.
    submit_time: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The time that the sentiment detection job ended.
    end_time: datetime.datetime = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The input data configuration that you supplied when you created the
    # sentiment detection job.
    input_data_config: "InputDataConfig" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The output data configuration that you supplied when you created the
    # sentiment detection job.
    output_data_config: "OutputDataConfig" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The language code of the input documents.
    language_code: typing.Union[str, "LanguageCode"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The Amazon Resource Name (ARN) that gives Amazon Comprehend read access to
    # your input data.
    data_access_role_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class SentimentScore(ShapeBase):
    """
    Describes the level of confidence that Amazon Comprehend has in the accuracy of
    its detection of sentiments.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "positive",
                "Positive",
                TypeInfo(float),
            ),
            (
                "negative",
                "Negative",
                TypeInfo(float),
            ),
            (
                "neutral",
                "Neutral",
                TypeInfo(float),
            ),
            (
                "mixed",
                "Mixed",
                TypeInfo(float),
            ),
        ]

    # The level of confidence that Amazon Comprehend has in the accuracy of its
    # detection of the `POSITIVE` sentiment.
    positive: float = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The level of confidence that Amazon Comprehend has in the accuracy of its
    # detection of the `NEGATIVE` sentiment.
    negative: float = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The level of confidence that Amazon Comprehend has in the accuracy of its
    # detection of the `NEUTRAL` sentiment.
    neutral: float = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The level of confidence that Amazon Comprehend has in the accuracy of its
    # detection of the `MIXED` sentiment.
    mixed: float = dataclasses.field(default=ShapeBase.NOT_SET, )


class SentimentType(str):
    POSITIVE = "POSITIVE"
    NEGATIVE = "NEGATIVE"
    NEUTRAL = "NEUTRAL"
    MIXED = "MIXED"


@dataclasses.dataclass
class StartDominantLanguageDetectionJobRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "input_data_config",
                "InputDataConfig",
                TypeInfo(InputDataConfig),
            ),
            (
                "output_data_config",
                "OutputDataConfig",
                TypeInfo(OutputDataConfig),
            ),
            (
                "data_access_role_arn",
                "DataAccessRoleArn",
                TypeInfo(str),
            ),
            (
                "job_name",
                "JobName",
                TypeInfo(str),
            ),
            (
                "client_request_token",
                "ClientRequestToken",
                TypeInfo(str),
            ),
        ]

    # Specifies the format and location of the input data for the job.
    input_data_config: "InputDataConfig" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Specifies where to send the output files.
    output_data_config: "OutputDataConfig" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The Amazon Resource Name (ARN) of the AWS Identity and Access Management
    # (IAM) role that grants Amazon Comprehend read access to your input data.
    # For more information, see
    # <https://docs.aws.amazon.com/comprehend/latest/dg/access-control-managing-
    # permissions.html#auth-role-permissions>.
    data_access_role_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # An identifier for the job.
    job_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A unique identifier for the request. If you do not set the client request
    # token, Amazon Comprehend generates one.
    client_request_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class StartDominantLanguageDetectionJobResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "job_id",
                "JobId",
                TypeInfo(str),
            ),
            (
                "job_status",
                "JobStatus",
                TypeInfo(typing.Union[str, JobStatus]),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The identifier generated for the job. To get the status of a job, use this
    # identifier with the operation.
    job_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The status of the job.

    #   * SUBMITTED - The job has been received and is queued for processing.

    #   * IN_PROGRESS - Amazon Comprehend is processing the job.

    #   * COMPLETED - The job was successfully completed and the output is available.

    #   * FAILED - The job did not complete. To get details, use the operation.
    job_status: typing.Union[str, "JobStatus"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class StartEntitiesDetectionJobRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "input_data_config",
                "InputDataConfig",
                TypeInfo(InputDataConfig),
            ),
            (
                "output_data_config",
                "OutputDataConfig",
                TypeInfo(OutputDataConfig),
            ),
            (
                "data_access_role_arn",
                "DataAccessRoleArn",
                TypeInfo(str),
            ),
            (
                "language_code",
                "LanguageCode",
                TypeInfo(typing.Union[str, LanguageCode]),
            ),
            (
                "job_name",
                "JobName",
                TypeInfo(str),
            ),
            (
                "client_request_token",
                "ClientRequestToken",
                TypeInfo(str),
            ),
        ]

    # Specifies the format and location of the input data for the job.
    input_data_config: "InputDataConfig" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Specifies where to send the output files.
    output_data_config: "OutputDataConfig" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The Amazon Resource Name (ARN) of the AWS Identity and Access Management
    # (IAM) role that grants Amazon Comprehend read access to your input data.
    # For more information, see
    # <https://docs.aws.amazon.com/comprehend/latest/dg/access-control-managing-
    # permissions.html#auth-role-permissions>.
    data_access_role_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The language of the input documents. You can specify English ("en") or
    # Spanish ("es"). All documents must be in the same language.
    language_code: typing.Union[str, "LanguageCode"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The identifier of the job.
    job_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A unique identifier for the request. If you don't set the client request
    # token, Amazon Comprehend generates one.
    client_request_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class StartEntitiesDetectionJobResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "job_id",
                "JobId",
                TypeInfo(str),
            ),
            (
                "job_status",
                "JobStatus",
                TypeInfo(typing.Union[str, JobStatus]),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The identifier generated for the job. To get the status of job, use this
    # identifier with the operation.
    job_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The status of the job.

    #   * SUBMITTED - The job has been received and is queued for processing.

    #   * IN_PROGRESS - Amazon Comprehend is processing the job.

    #   * COMPLETED - The job was successfully completed and the output is available.

    #   * FAILED - The job did not complete. To get details, use the operation.
    job_status: typing.Union[str, "JobStatus"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class StartKeyPhrasesDetectionJobRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "input_data_config",
                "InputDataConfig",
                TypeInfo(InputDataConfig),
            ),
            (
                "output_data_config",
                "OutputDataConfig",
                TypeInfo(OutputDataConfig),
            ),
            (
                "data_access_role_arn",
                "DataAccessRoleArn",
                TypeInfo(str),
            ),
            (
                "language_code",
                "LanguageCode",
                TypeInfo(typing.Union[str, LanguageCode]),
            ),
            (
                "job_name",
                "JobName",
                TypeInfo(str),
            ),
            (
                "client_request_token",
                "ClientRequestToken",
                TypeInfo(str),
            ),
        ]

    # Specifies the format and location of the input data for the job.
    input_data_config: "InputDataConfig" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Specifies where to send the output files.
    output_data_config: "OutputDataConfig" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The Amazon Resource Name (ARN) of the AWS Identity and Access Management
    # (IAM) role that grants Amazon Comprehend read access to your input data.
    # For more information, see
    # <https://docs.aws.amazon.com/comprehend/latest/dg/access-control-managing-
    # permissions.html#auth-role-permissions>.
    data_access_role_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The language of the input documents. You can specify English ("en") or
    # Spanish ("es"). All documents must be in the same language.
    language_code: typing.Union[str, "LanguageCode"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The identifier of the job.
    job_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A unique identifier for the request. If you don't set the client request
    # token, Amazon Comprehend generates one.
    client_request_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class StartKeyPhrasesDetectionJobResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "job_id",
                "JobId",
                TypeInfo(str),
            ),
            (
                "job_status",
                "JobStatus",
                TypeInfo(typing.Union[str, JobStatus]),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The identifier generated for the job. To get the status of a job, use this
    # identifier with the operation.
    job_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The status of the job.

    #   * SUBMITTED - The job has been received and is queued for processing.

    #   * IN_PROGRESS - Amazon Comprehend is processing the job.

    #   * COMPLETED - The job was successfully completed and the output is available.

    #   * FAILED - The job did not complete. To get details, use the operation.
    job_status: typing.Union[str, "JobStatus"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class StartSentimentDetectionJobRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "input_data_config",
                "InputDataConfig",
                TypeInfo(InputDataConfig),
            ),
            (
                "output_data_config",
                "OutputDataConfig",
                TypeInfo(OutputDataConfig),
            ),
            (
                "data_access_role_arn",
                "DataAccessRoleArn",
                TypeInfo(str),
            ),
            (
                "language_code",
                "LanguageCode",
                TypeInfo(typing.Union[str, LanguageCode]),
            ),
            (
                "job_name",
                "JobName",
                TypeInfo(str),
            ),
            (
                "client_request_token",
                "ClientRequestToken",
                TypeInfo(str),
            ),
        ]

    # Specifies the format and location of the input data for the job.
    input_data_config: "InputDataConfig" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Specifies where to send the output files.
    output_data_config: "OutputDataConfig" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The Amazon Resource Name (ARN) of the AWS Identity and Access Management
    # (IAM) role that grants Amazon Comprehend read access to your input data.
    # For more information, see
    # <https://docs.aws.amazon.com/comprehend/latest/dg/access-control-managing-
    # permissions.html#auth-role-permissions>.
    data_access_role_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The language of the input documents. You can specify English ("en") or
    # Spanish ("es"). All documents must be in the same language.
    language_code: typing.Union[str, "LanguageCode"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The identifier of the job.
    job_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A unique identifier for the request. If you don't set the client request
    # token, Amazon Comprehend generates one.
    client_request_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class StartSentimentDetectionJobResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "job_id",
                "JobId",
                TypeInfo(str),
            ),
            (
                "job_status",
                "JobStatus",
                TypeInfo(typing.Union[str, JobStatus]),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The identifier generated for the job. To get the status of a job, use this
    # identifier with the operation.
    job_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The status of the job.

    #   * SUBMITTED - The job has been received and is queued for processing.

    #   * IN_PROGRESS - Amazon Comprehend is processing the job.

    #   * COMPLETED - The job was successfully completed and the output is available.

    #   * FAILED - The job did not complete. To get details, use the operation.
    job_status: typing.Union[str, "JobStatus"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class StartTopicsDetectionJobRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "input_data_config",
                "InputDataConfig",
                TypeInfo(InputDataConfig),
            ),
            (
                "output_data_config",
                "OutputDataConfig",
                TypeInfo(OutputDataConfig),
            ),
            (
                "data_access_role_arn",
                "DataAccessRoleArn",
                TypeInfo(str),
            ),
            (
                "job_name",
                "JobName",
                TypeInfo(str),
            ),
            (
                "number_of_topics",
                "NumberOfTopics",
                TypeInfo(int),
            ),
            (
                "client_request_token",
                "ClientRequestToken",
                TypeInfo(str),
            ),
        ]

    # Specifies the format and location of the input data for the job.
    input_data_config: "InputDataConfig" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Specifies where to send the output files. The output is a compressed
    # archive with two files, `topic-terms.csv` that lists the terms associated
    # with each topic, and `doc-topics.csv` that lists the documents associated
    # with each topic
    output_data_config: "OutputDataConfig" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The Amazon Resource Name (ARN) of the AWS Identity and Access Management
    # (IAM) role that grants Amazon Comprehend read access to your input data.
    # For more information, see
    # <https://docs.aws.amazon.com/comprehend/latest/dg/access-control-managing-
    # permissions.html#auth-role-permissions>.
    data_access_role_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The identifier of the job.
    job_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The number of topics to detect.
    number_of_topics: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A unique identifier for the request. If you do not set the client request
    # token, Amazon Comprehend generates one.
    client_request_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class StartTopicsDetectionJobResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "job_id",
                "JobId",
                TypeInfo(str),
            ),
            (
                "job_status",
                "JobStatus",
                TypeInfo(typing.Union[str, JobStatus]),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The identifier generated for the job. To get the status of the job, use
    # this identifier with the `DescribeTopicDetectionJob` operation.
    job_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The status of the job:

    #   * SUBMITTED - The job has been received and is queued for processing.

    #   * IN_PROGRESS - Amazon Comprehend is processing the job.

    #   * COMPLETED - The job was successfully completed and the output is available.

    #   * FAILED - The job did not complete. To get details, use the `DescribeTopicDetectionJob` operation.
    job_status: typing.Union[str, "JobStatus"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class StopDominantLanguageDetectionJobRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "job_id",
                "JobId",
                TypeInfo(str),
            ),
        ]

    # The identifier of the dominant language detection job to stop.
    job_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class StopDominantLanguageDetectionJobResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "job_id",
                "JobId",
                TypeInfo(str),
            ),
            (
                "job_status",
                "JobStatus",
                TypeInfo(typing.Union[str, JobStatus]),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The identifier of the dominant language detection job to stop.
    job_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Either `STOP_REQUESTED` if the job is currently running, or `STOPPED` if
    # the job was previously stopped with the `StopDominantLanguageDetectionJob`
    # operation.
    job_status: typing.Union[str, "JobStatus"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class StopEntitiesDetectionJobRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "job_id",
                "JobId",
                TypeInfo(str),
            ),
        ]

    # The identifier of the entities detection job to stop.
    job_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class StopEntitiesDetectionJobResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "job_id",
                "JobId",
                TypeInfo(str),
            ),
            (
                "job_status",
                "JobStatus",
                TypeInfo(typing.Union[str, JobStatus]),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The identifier of the entities detection job to stop.
    job_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Either `STOP_REQUESTED` if the job is currently running, or `STOPPED` if
    # the job was previously stopped with the `StopEntitiesDetectionJob`
    # operation.
    job_status: typing.Union[str, "JobStatus"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class StopKeyPhrasesDetectionJobRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "job_id",
                "JobId",
                TypeInfo(str),
            ),
        ]

    # The identifier of the key phrases detection job to stop.
    job_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class StopKeyPhrasesDetectionJobResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "job_id",
                "JobId",
                TypeInfo(str),
            ),
            (
                "job_status",
                "JobStatus",
                TypeInfo(typing.Union[str, JobStatus]),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The identifier of the key phrases detection job to stop.
    job_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Either `STOP_REQUESTED` if the job is currently running, or `STOPPED` if
    # the job was previously stopped with the `StopKeyPhrasesDetectionJob`
    # operation.
    job_status: typing.Union[str, "JobStatus"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class StopSentimentDetectionJobRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "job_id",
                "JobId",
                TypeInfo(str),
            ),
        ]

    # The identifier of the sentiment detection job to stop.
    job_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class StopSentimentDetectionJobResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "job_id",
                "JobId",
                TypeInfo(str),
            ),
            (
                "job_status",
                "JobStatus",
                TypeInfo(typing.Union[str, JobStatus]),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The identifier of the sentiment detection job to stop.
    job_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Either `STOP_REQUESTED` if the job is currently running, or `STOPPED` if
    # the job was previously stopped with the `StopSentimentDetectionJob`
    # operation.
    job_status: typing.Union[str, "JobStatus"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


class SyntaxLanguageCode(str):
    en = "en"


@dataclasses.dataclass
class SyntaxToken(ShapeBase):
    """
    Represents a work in the input text that was recognized and assigned a part of
    speech. There is one syntax token record for each word in the source text.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "token_id",
                "TokenId",
                TypeInfo(int),
            ),
            (
                "text",
                "Text",
                TypeInfo(str),
            ),
            (
                "begin_offset",
                "BeginOffset",
                TypeInfo(int),
            ),
            (
                "end_offset",
                "EndOffset",
                TypeInfo(int),
            ),
            (
                "part_of_speech",
                "PartOfSpeech",
                TypeInfo(PartOfSpeechTag),
            ),
        ]

    # A unique identifier for a token.
    token_id: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The word that was recognized in the source text.
    text: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The zero-based offset from the beginning of the source text to the first
    # character in the word.
    begin_offset: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The zero-based offset from the beginning of the source text to the last
    # character in the word.
    end_offset: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Provides the part of speech label and the confidence level that Amazon
    # Comprehend has that the part of speech was correctly identified. For more
    # information, see how-syntax.
    part_of_speech: "PartOfSpeechTag" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class TextSizeLimitExceededException(ShapeBase):
    """
    The size of the input text exceeds the limit. Use a smaller document.
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
class TooManyRequestsException(ShapeBase):
    """
    The number of requests exceeds the limit. Resubmit your request later.
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
class TopicsDetectionJobFilter(ShapeBase):
    """
    Provides information for filtering topic detection jobs. For more information,
    see .
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "job_name",
                "JobName",
                TypeInfo(str),
            ),
            (
                "job_status",
                "JobStatus",
                TypeInfo(typing.Union[str, JobStatus]),
            ),
            (
                "submit_time_before",
                "SubmitTimeBefore",
                TypeInfo(datetime.datetime),
            ),
            (
                "submit_time_after",
                "SubmitTimeAfter",
                TypeInfo(datetime.datetime),
            ),
        ]

    job_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Filters the list of topic detection jobs based on job status. Returns only
    # jobs with the specified status.
    job_status: typing.Union[str, "JobStatus"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Filters the list of jobs based on the time that the job was submitted for
    # processing. Only returns jobs submitted before the specified time. Jobs are
    # returned in descending order, newest to oldest.
    submit_time_before: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Filters the list of jobs based on the time that the job was submitted for
    # processing. Only returns jobs submitted after the specified time. Jobs are
    # returned in ascending order, oldest to newest.
    submit_time_after: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class TopicsDetectionJobProperties(ShapeBase):
    """
    Provides information about a topic detection job.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "job_id",
                "JobId",
                TypeInfo(str),
            ),
            (
                "job_name",
                "JobName",
                TypeInfo(str),
            ),
            (
                "job_status",
                "JobStatus",
                TypeInfo(typing.Union[str, JobStatus]),
            ),
            (
                "message",
                "Message",
                TypeInfo(str),
            ),
            (
                "submit_time",
                "SubmitTime",
                TypeInfo(datetime.datetime),
            ),
            (
                "end_time",
                "EndTime",
                TypeInfo(datetime.datetime),
            ),
            (
                "input_data_config",
                "InputDataConfig",
                TypeInfo(InputDataConfig),
            ),
            (
                "output_data_config",
                "OutputDataConfig",
                TypeInfo(OutputDataConfig),
            ),
            (
                "number_of_topics",
                "NumberOfTopics",
                TypeInfo(int),
            ),
        ]

    # The identifier assigned to the topic detection job.
    job_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The name of the topic detection job.
    job_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The current status of the topic detection job. If the status is `Failed`,
    # the reason for the failure is shown in the `Message` field.
    job_status: typing.Union[str, "JobStatus"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A description for the status of a job.
    message: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The time that the topic detection job was submitted for processing.
    submit_time: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The time that the topic detection job was completed.
    end_time: datetime.datetime = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The input data configuration supplied when you created the topic detection
    # job.
    input_data_config: "InputDataConfig" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The output data configuration supplied when you created the topic detection
    # job.
    output_data_config: "OutputDataConfig" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The number of topics to detect supplied when you created the topic
    # detection job. The default is 10.
    number_of_topics: int = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class UnsupportedLanguageException(ShapeBase):
    """
    Amazon Comprehend can't process the language of the input text. For all APIs
    except `DetectDominantLanguage`, Amazon Comprehend accepts only English or
    Spanish text. For the `DetectDominantLanguage` API, Amazon Comprehend detects
    100 languages. For a list of languages, see how-languages
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
