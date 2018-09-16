import datetime
import typing
from autoboto import ShapeBase, OutputShapeBase, TypeInfo
import dataclasses


@dataclasses.dataclass
class Attributes(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class ClaimDevicesByClaimCodeRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "claim_code",
                "ClaimCode",
                TypeInfo(str),
            ),
        ]

    # The claim code, starting with "C-", as provided by the device manufacturer.
    claim_code: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ClaimDevicesByClaimCodeResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "claim_code",
                "ClaimCode",
                TypeInfo(str),
            ),
            (
                "total",
                "Total",
                TypeInfo(int),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The claim code provided by the device manufacturer.
    claim_code: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The total number of devices associated with the claim code that has been
    # processed in the claim request.
    total: int = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DescribeDeviceRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "device_id",
                "DeviceId",
                TypeInfo(str),
            ),
        ]

    # The unique identifier of the device.
    device_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DescribeDeviceResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "device_description",
                "DeviceDescription",
                TypeInfo(DeviceDescription),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Device details.
    device_description: "DeviceDescription" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class Device(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "attributes",
                "Attributes",
                TypeInfo(Attributes),
            ),
            (
                "device_id",
                "DeviceId",
                TypeInfo(str),
            ),
            (
                "type",
                "Type",
                TypeInfo(str),
            ),
        ]

    # The user specified attributes associated with the device for an event.
    attributes: "Attributes" = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The unique identifier of the device.
    device_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The device type, such as "button".
    type: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DeviceClaimResponse(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "state",
                "State",
                TypeInfo(str),
            ),
        ]

    # The device's final claim state.
    state: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DeviceDescription(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "attributes",
                "Attributes",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "device_id",
                "DeviceId",
                TypeInfo(str),
            ),
            (
                "enabled",
                "Enabled",
                TypeInfo(bool),
            ),
            (
                "remaining_life",
                "RemainingLife",
                TypeInfo(float),
            ),
            (
                "type",
                "Type",
                TypeInfo(str),
            ),
        ]

    # An array of zero or more elements of DeviceAttribute objects providing user
    # specified device attributes.
    attributes: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The unique identifier of the device.
    device_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A Boolean value indicating whether or not the device is enabled.
    enabled: bool = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A value between 0 and 1 inclusive, representing the fraction of life
    # remaining for the device.
    remaining_life: float = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The type of the device, such as "button".
    type: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DeviceEvent(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "device",
                "Device",
                TypeInfo(Device),
            ),
            (
                "std_event",
                "StdEvent",
                TypeInfo(str),
            ),
        ]

    # An object representing the device associated with the event.
    device: "Device" = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A serialized JSON object representing the device-type specific event.
    std_event: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DeviceEventsResponse(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "events",
                "Events",
                TypeInfo(typing.List[DeviceEvent]),
            ),
            (
                "next_token",
                "NextToken",
                TypeInfo(str),
            ),
        ]

    # An array of zero or more elements describing the event(s) associated with
    # the device.
    events: typing.List["DeviceEvent"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The token to retrieve the next set of results.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DeviceMethod(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "device_type",
                "DeviceType",
                TypeInfo(str),
            ),
            (
                "method_name",
                "MethodName",
                TypeInfo(str),
            ),
        ]

    # The type of the device, such as "button".
    device_type: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The name of the method applicable to the deviceType.
    method_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class Empty(ShapeBase):
    """
    On success, an empty object is returned.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class FinalizeDeviceClaimRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "device_id",
                "DeviceId",
                TypeInfo(str),
            ),
        ]

    # The unique identifier of the device.
    device_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class FinalizeDeviceClaimResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "state",
                "State",
                TypeInfo(str),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The device's final claim state.
    state: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ForbiddenException(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "code",
                "Code",
                TypeInfo(str),
            ),
            (
                "message",
                "Message",
                TypeInfo(str),
            ),
        ]

    # 403
    code: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The 403 error message returned by the web server.
    message: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class GetDeviceMethodsRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "device_id",
                "DeviceId",
                TypeInfo(str),
            ),
        ]

    # The unique identifier of the device.
    device_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class GetDeviceMethodsResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "device_methods",
                "DeviceMethods",
                TypeInfo(typing.List[DeviceMethod]),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # List of available device APIs.
    device_methods: typing.List["DeviceMethod"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class InitiateDeviceClaimRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "device_id",
                "DeviceId",
                TypeInfo(str),
            ),
        ]

    # The unique identifier of the device.
    device_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class InitiateDeviceClaimResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "state",
                "State",
                TypeInfo(str),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The device's final claim state.
    state: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class InternalFailureException(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "code",
                "Code",
                TypeInfo(str),
            ),
            (
                "message",
                "Message",
                TypeInfo(str),
            ),
        ]

    # 500
    code: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The 500 error message returned by the web server.
    message: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class InvalidRequestException(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "code",
                "Code",
                TypeInfo(str),
            ),
            (
                "message",
                "Message",
                TypeInfo(str),
            ),
        ]

    # 400
    code: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The 400 error message returned by the web server.
    message: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class InvokeDeviceMethodRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "device_id",
                "DeviceId",
                TypeInfo(str),
            ),
            (
                "device_method",
                "DeviceMethod",
                TypeInfo(DeviceMethod),
            ),
            (
                "device_method_parameters",
                "DeviceMethodParameters",
                TypeInfo(str),
            ),
        ]

    # The unique identifier of the device.
    device_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The device method to invoke.
    device_method: "DeviceMethod" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A JSON encoded string containing the device method request parameters.
    device_method_parameters: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class InvokeDeviceMethodResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "device_method_response",
                "DeviceMethodResponse",
                TypeInfo(str),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A JSON encoded string containing the device method response.
    device_method_response: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ListDeviceEventsRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "device_id",
                "DeviceId",
                TypeInfo(str),
            ),
            (
                "from_time_stamp",
                "FromTimeStamp",
                TypeInfo(datetime.datetime),
            ),
            (
                "to_time_stamp",
                "ToTimeStamp",
                TypeInfo(datetime.datetime),
            ),
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
        ]

    # The unique identifier of the device.
    device_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The start date for the device event query, in ISO8061 format. For example,
    # 2018-03-28T15:45:12.880Z
    from_time_stamp: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The end date for the device event query, in ISO8061 format. For example,
    # 2018-03-28T15:45:12.880Z
    to_time_stamp: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The maximum number of results to return per request. If not set, a default
    # value of 100 is used.
    max_results: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The token to retrieve the next set of results.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ListDeviceEventsResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "events",
                "Events",
                TypeInfo(typing.List[DeviceEvent]),
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

    # An array of zero or more elements describing the event(s) associated with
    # the device.
    events: typing.List["DeviceEvent"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The token to retrieve the next set of results.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ListDevicesRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "device_type",
                "DeviceType",
                TypeInfo(str),
            ),
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
        ]

    # The type of the device, such as "button".
    device_type: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The maximum number of results to return per request. If not set, a default
    # value of 100 is used.
    max_results: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The token to retrieve the next set of results.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ListDevicesResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "devices",
                "Devices",
                TypeInfo(typing.List[DeviceDescription]),
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

    # A list of devices.
    devices: typing.List["DeviceDescription"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The token to retrieve the next set of results.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class PreconditionFailedException(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "code",
                "Code",
                TypeInfo(str),
            ),
            (
                "message",
                "Message",
                TypeInfo(str),
            ),
        ]

    # 412
    code: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # An error message explaining the error or its remedy.
    message: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class RangeNotSatisfiableException(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "code",
                "Code",
                TypeInfo(str),
            ),
            (
                "message",
                "Message",
                TypeInfo(str),
            ),
        ]

    # 416
    code: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The requested number of results specified by nextToken cannot be satisfied.
    message: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ResourceConflictException(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "code",
                "Code",
                TypeInfo(str),
            ),
            (
                "message",
                "Message",
                TypeInfo(str),
            ),
        ]

    # 409
    code: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # An error message explaining the error or its remedy.
    message: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ResourceNotFoundException(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "code",
                "Code",
                TypeInfo(str),
            ),
            (
                "message",
                "Message",
                TypeInfo(str),
            ),
        ]

    # 404
    code: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The requested device could not be found.
    message: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class UnclaimDeviceRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "device_id",
                "DeviceId",
                TypeInfo(str),
            ),
        ]

    # The unique identifier of the device.
    device_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class UnclaimDeviceResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "state",
                "State",
                TypeInfo(str),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The device's final claim state.
    state: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class UpdateDeviceStateRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "device_id",
                "DeviceId",
                TypeInfo(str),
            ),
            (
                "enabled",
                "Enabled",
                TypeInfo(bool),
            ),
        ]

    # The unique identifier of the device.
    device_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # If true, the device is enabled. If false, the device is disabled.
    enabled: bool = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class UpdateDeviceStateResponse(OutputShapeBase):
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
