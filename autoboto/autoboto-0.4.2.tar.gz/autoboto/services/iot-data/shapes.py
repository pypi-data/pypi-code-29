import datetime
import typing
from autoboto import ShapeBase, OutputShapeBase, TypeInfo
import botocore.response
import dataclasses


@dataclasses.dataclass
class ConflictException(ShapeBase):
    """
    The specified version does not match the version of the document.
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

    # The message for the exception.
    message: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DeleteThingShadowRequest(ShapeBase):
    """
    The input for the DeleteThingShadow operation.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "thing_name",
                "thingName",
                TypeInfo(str),
            ),
        ]

    # The name of the thing.
    thing_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DeleteThingShadowResponse(OutputShapeBase):
    """
    The output from the DeleteThingShadow operation.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "payload",
                "payload",
                TypeInfo(typing.Any),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The state information, in JSON format.
    payload: typing.Any = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class GetThingShadowRequest(ShapeBase):
    """
    The input for the GetThingShadow operation.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "thing_name",
                "thingName",
                TypeInfo(str),
            ),
        ]

    # The name of the thing.
    thing_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class GetThingShadowResponse(OutputShapeBase):
    """
    The output from the GetThingShadow operation.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "payload",
                "payload",
                TypeInfo(typing.Any),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The state information, in JSON format.
    payload: typing.Any = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class InternalFailureException(ShapeBase):
    """
    An unexpected error has occurred.
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

    # The message for the exception.
    message: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class InvalidRequestException(ShapeBase):
    """
    The request is not valid.
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

    # The message for the exception.
    message: str = dataclasses.field(default=ShapeBase.NOT_SET, )


class JsonDocument(botocore.response.StreamingBody):
    pass


@dataclasses.dataclass
class MethodNotAllowedException(ShapeBase):
    """
    The specified combination of HTTP verb and URI is not supported.
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

    # The message for the exception.
    message: str = dataclasses.field(default=ShapeBase.NOT_SET, )


class Payload(botocore.response.StreamingBody):
    pass


@dataclasses.dataclass
class PublishRequest(ShapeBase):
    """
    The input for the Publish operation.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "topic",
                "topic",
                TypeInfo(str),
            ),
            (
                "qos",
                "qos",
                TypeInfo(int),
            ),
            (
                "payload",
                "payload",
                TypeInfo(typing.Any),
            ),
        ]

    # The name of the MQTT topic.
    topic: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The Quality of Service (QoS) level.
    qos: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The state information, in JSON format.
    payload: typing.Any = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class RequestEntityTooLargeException(ShapeBase):
    """
    The payload exceeds the maximum size allowed.
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

    # The message for the exception.
    message: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ResourceNotFoundException(ShapeBase):
    """
    The specified resource does not exist.
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

    # The message for the exception.
    message: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ServiceUnavailableException(ShapeBase):
    """
    The service is temporarily unavailable.
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

    # The message for the exception.
    message: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ThrottlingException(ShapeBase):
    """
    The rate exceeds the limit.
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

    # The message for the exception.
    message: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class UnauthorizedException(ShapeBase):
    """
    You are not authorized to perform this operation.
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

    # The message for the exception.
    message: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class UnsupportedDocumentEncodingException(ShapeBase):
    """
    The document encoding is not supported.
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

    # The message for the exception.
    message: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class UpdateThingShadowRequest(ShapeBase):
    """
    The input for the UpdateThingShadow operation.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "thing_name",
                "thingName",
                TypeInfo(str),
            ),
            (
                "payload",
                "payload",
                TypeInfo(typing.Any),
            ),
        ]

    # The name of the thing.
    thing_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The state information, in JSON format.
    payload: typing.Any = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class UpdateThingShadowResponse(OutputShapeBase):
    """
    The output from the UpdateThingShadow operation.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "payload",
                "payload",
                TypeInfo(typing.Any),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The state information, in JSON format.
    payload: typing.Any = dataclasses.field(default=ShapeBase.NOT_SET, )
