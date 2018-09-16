import datetime
import typing
from autoboto import ShapeBase, OutputShapeBase, TypeInfo
import dataclasses


@dataclasses.dataclass
class DetectedLanguageLowConfidenceException(ShapeBase):
    """
    The confidence that Amazon Comprehend accurately detected the source language is
    low. If a low confidence level is acceptable for your application, you can use
    the language in the exception to call Amazon Translate again. For more
    information, see the
    [DetectDominantLanguage](https://docs.aws.amazon.com/comprehend/latest/dg/API_DetectDominantLanguage.html)
    operation in the _Amazon Comprehend Developer Guide_.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "message",
                "Message",
                TypeInfo(str),
            ),
            (
                "detected_language_code",
                "DetectedLanguageCode",
                TypeInfo(str),
            ),
        ]

    message: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Auto detected language code from Comprehend.
    detected_language_code: str = dataclasses.field(default=ShapeBase.NOT_SET, )


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
class ServiceUnavailableException(ShapeBase):
    """
    Amazon Translate is unavailable. Retry your request later.
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
class TextSizeLimitExceededException(ShapeBase):
    """
    The size of the input text exceeds the length constraint for the `Text` field.
    Try again with a shorter text.
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
class TranslateTextRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "text",
                "Text",
                TypeInfo(str),
            ),
            (
                "source_language_code",
                "SourceLanguageCode",
                TypeInfo(str),
            ),
            (
                "target_language_code",
                "TargetLanguageCode",
                TypeInfo(str),
            ),
        ]

    # The text to translate.
    text: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # One of the supported language codes for the source text. If the
    # `TargetLanguageCode` is not "en", the `SourceLanguageCode` must be "en".

    # To have Amazon Translate determine the source language of your text, you
    # can specify `auto` in the `SourceLanguageCode` field. If you specify
    # `auto`, Amazon Translate will call Amazon Comprehend to determine the
    # source language.
    source_language_code: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # One of the supported language codes for the target text. If the
    # `SourceLanguageCode` is not "en", the `TargetLanguageCode` must be "en".
    target_language_code: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class TranslateTextResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "translated_text",
                "TranslatedText",
                TypeInfo(str),
            ),
            (
                "source_language_code",
                "SourceLanguageCode",
                TypeInfo(str),
            ),
            (
                "target_language_code",
                "TargetLanguageCode",
                TypeInfo(str),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The text translated into the target language.
    translated_text: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The language code for the language of the input text.
    source_language_code: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The language code for the language of the translated text.
    target_language_code: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class UnsupportedLanguagePairException(ShapeBase):
    """
    Amazon Translate cannot translate input text in the source language into this
    target language. For more information, see how-to-error-msg.
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
