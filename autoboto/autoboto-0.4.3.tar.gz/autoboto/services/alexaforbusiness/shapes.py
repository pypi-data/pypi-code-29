import datetime
import typing
from autoboto import ShapeBase, OutputShapeBase, TypeInfo
import dataclasses


@dataclasses.dataclass
class AddressBook(ShapeBase):
    """
    An address book with attributes.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "address_book_arn",
                "AddressBookArn",
                TypeInfo(str),
            ),
            (
                "name",
                "Name",
                TypeInfo(str),
            ),
            (
                "description",
                "Description",
                TypeInfo(str),
            ),
        ]

    # The ARN of the address book.
    address_book_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The name of the address book.
    name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The description of the address book.
    description: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class AddressBookData(ShapeBase):
    """
    Information related to an address book.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "address_book_arn",
                "AddressBookArn",
                TypeInfo(str),
            ),
            (
                "name",
                "Name",
                TypeInfo(str),
            ),
            (
                "description",
                "Description",
                TypeInfo(str),
            ),
        ]

    # The ARN of the address book.
    address_book_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The name of the address book.
    name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The description of the address book.
    description: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class AlreadyExistsException(ShapeBase):
    """
    The resource being created already exists. HTTP Status Code: 400
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
class AssociateContactWithAddressBookRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "contact_arn",
                "ContactArn",
                TypeInfo(str),
            ),
            (
                "address_book_arn",
                "AddressBookArn",
                TypeInfo(str),
            ),
        ]

    # The ARN of the contact to associate with an address book.
    contact_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The ARN of the address book with which to associate the contact.
    address_book_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class AssociateContactWithAddressBookResponse(OutputShapeBase):
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
class AssociateDeviceWithRoomRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "device_arn",
                "DeviceArn",
                TypeInfo(str),
            ),
            (
                "room_arn",
                "RoomArn",
                TypeInfo(str),
            ),
        ]

    # The ARN of the device to associate to a room. Required.
    device_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The ARN of the room with which to associate the device. Required.
    room_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class AssociateDeviceWithRoomResponse(OutputShapeBase):
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
class AssociateSkillGroupWithRoomRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "skill_group_arn",
                "SkillGroupArn",
                TypeInfo(str),
            ),
            (
                "room_arn",
                "RoomArn",
                TypeInfo(str),
            ),
        ]

    # The ARN of the skill group to associate with a room. Required.
    skill_group_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The ARN of the room with which to associate the skill group. Required.
    room_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class AssociateSkillGroupWithRoomResponse(OutputShapeBase):
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


class ConnectionStatus(str):
    ONLINE = "ONLINE"
    OFFLINE = "OFFLINE"


@dataclasses.dataclass
class Contact(ShapeBase):
    """
    A contact with attributes.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "contact_arn",
                "ContactArn",
                TypeInfo(str),
            ),
            (
                "display_name",
                "DisplayName",
                TypeInfo(str),
            ),
            (
                "first_name",
                "FirstName",
                TypeInfo(str),
            ),
            (
                "last_name",
                "LastName",
                TypeInfo(str),
            ),
            (
                "phone_number",
                "PhoneNumber",
                TypeInfo(str),
            ),
        ]

    # The ARN of the contact.
    contact_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The name of the contact to display on the console.
    display_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The first name of the contact, used to call the contact on the device.
    first_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The last name of the contact, used to call the contact on the device.
    last_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The phone number of the contact.
    phone_number: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ContactData(ShapeBase):
    """
    Information related to a contact.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "contact_arn",
                "ContactArn",
                TypeInfo(str),
            ),
            (
                "display_name",
                "DisplayName",
                TypeInfo(str),
            ),
            (
                "first_name",
                "FirstName",
                TypeInfo(str),
            ),
            (
                "last_name",
                "LastName",
                TypeInfo(str),
            ),
            (
                "phone_number",
                "PhoneNumber",
                TypeInfo(str),
            ),
        ]

    # The ARN of the contact.
    contact_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The name of the contact to display on the console.
    display_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The first name of the contact, used to call the contact on the device.
    first_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The last name of the contact, used to call the contact on the device.
    last_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The phone number of the contact.
    phone_number: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class CreateAddressBookRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "name",
                "Name",
                TypeInfo(str),
            ),
            (
                "description",
                "Description",
                TypeInfo(str),
            ),
            (
                "client_request_token",
                "ClientRequestToken",
                TypeInfo(str),
            ),
        ]

    # The name of the address book.
    name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The description of the address book.
    description: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A unique, user-specified identifier for the request that ensures
    # idempotency.
    client_request_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class CreateAddressBookResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "address_book_arn",
                "AddressBookArn",
                TypeInfo(str),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The ARN of the newly created address book.
    address_book_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class CreateContactRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "first_name",
                "FirstName",
                TypeInfo(str),
            ),
            (
                "phone_number",
                "PhoneNumber",
                TypeInfo(str),
            ),
            (
                "display_name",
                "DisplayName",
                TypeInfo(str),
            ),
            (
                "last_name",
                "LastName",
                TypeInfo(str),
            ),
            (
                "client_request_token",
                "ClientRequestToken",
                TypeInfo(str),
            ),
        ]

    # The first name of the contact that is used to call the contact on the
    # device.
    first_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The phone number of the contact in E.164 format.
    phone_number: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The name of the contact to display on the console.
    display_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The last name of the contact that is used to call the contact on the
    # device.
    last_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A unique, user-specified identifier for this request that ensures
    # idempotency.
    client_request_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class CreateContactResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "contact_arn",
                "ContactArn",
                TypeInfo(str),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The ARN of the newly created address book.
    contact_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class CreateProfileRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "profile_name",
                "ProfileName",
                TypeInfo(str),
            ),
            (
                "timezone",
                "Timezone",
                TypeInfo(str),
            ),
            (
                "address",
                "Address",
                TypeInfo(str),
            ),
            (
                "distance_unit",
                "DistanceUnit",
                TypeInfo(typing.Union[str, DistanceUnit]),
            ),
            (
                "temperature_unit",
                "TemperatureUnit",
                TypeInfo(typing.Union[str, TemperatureUnit]),
            ),
            (
                "wake_word",
                "WakeWord",
                TypeInfo(typing.Union[str, WakeWord]),
            ),
            (
                "client_request_token",
                "ClientRequestToken",
                TypeInfo(str),
            ),
            (
                "setup_mode_disabled",
                "SetupModeDisabled",
                TypeInfo(bool),
            ),
            (
                "max_volume_limit",
                "MaxVolumeLimit",
                TypeInfo(int),
            ),
            (
                "pstn_enabled",
                "PSTNEnabled",
                TypeInfo(bool),
            ),
        ]

    # The name of a room profile.
    profile_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The time zone used by a room profile.
    timezone: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The valid address for the room.
    address: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The distance unit to be used by devices in the profile.
    distance_unit: typing.Union[str, "DistanceUnit"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The temperature unit to be used by devices in the profile.
    temperature_unit: typing.Union[str, "TemperatureUnit"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A wake word for Alexa, Echo, Amazon, or a computer.
    wake_word: typing.Union[str, "WakeWord"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The user-specified token that is used during the creation of a profile.
    client_request_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Whether room profile setup is enabled.
    setup_mode_disabled: bool = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The maximum volume limit for a room profile.
    max_volume_limit: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Whether PSTN calling is enabled.
    pstn_enabled: bool = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class CreateProfileResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "profile_arn",
                "ProfileArn",
                TypeInfo(str),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The ARN of the newly created room profile in the response.
    profile_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class CreateRoomRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "room_name",
                "RoomName",
                TypeInfo(str),
            ),
            (
                "description",
                "Description",
                TypeInfo(str),
            ),
            (
                "profile_arn",
                "ProfileArn",
                TypeInfo(str),
            ),
            (
                "provider_calendar_id",
                "ProviderCalendarId",
                TypeInfo(str),
            ),
            (
                "client_request_token",
                "ClientRequestToken",
                TypeInfo(str),
            ),
            (
                "tags",
                "Tags",
                TypeInfo(typing.List[Tag]),
            ),
        ]

    # The name for the room.
    room_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The description for the room.
    description: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The profile ARN for the room.
    profile_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The calendar ARN for the room.
    provider_calendar_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A unique, user-specified identifier for this request that ensures
    # idempotency.
    client_request_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The tags for the room.
    tags: typing.List["Tag"] = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class CreateRoomResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "room_arn",
                "RoomArn",
                TypeInfo(str),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The ARN of the newly created room in the response.
    room_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class CreateSkillGroupRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "skill_group_name",
                "SkillGroupName",
                TypeInfo(str),
            ),
            (
                "description",
                "Description",
                TypeInfo(str),
            ),
            (
                "client_request_token",
                "ClientRequestToken",
                TypeInfo(str),
            ),
        ]

    # The name for the skill group.
    skill_group_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The description for the skill group.
    description: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A unique, user-specified identifier for this request that ensures
    # idempotency.
    client_request_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class CreateSkillGroupResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "skill_group_arn",
                "SkillGroupArn",
                TypeInfo(str),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The ARN of the newly created skill group in the response.
    skill_group_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class CreateUserRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "user_id",
                "UserId",
                TypeInfo(str),
            ),
            (
                "first_name",
                "FirstName",
                TypeInfo(str),
            ),
            (
                "last_name",
                "LastName",
                TypeInfo(str),
            ),
            (
                "email",
                "Email",
                TypeInfo(str),
            ),
            (
                "client_request_token",
                "ClientRequestToken",
                TypeInfo(str),
            ),
            (
                "tags",
                "Tags",
                TypeInfo(typing.List[Tag]),
            ),
        ]

    # The ARN for the user.
    user_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The first name for the user.
    first_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The last name for the user.
    last_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The email address for the user.
    email: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A unique, user-specified identifier for this request that ensures
    # idempotency.
    client_request_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The tags for the user.
    tags: typing.List["Tag"] = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class CreateUserResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "user_arn",
                "UserArn",
                TypeInfo(str),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The ARN of the newly created user in the response.
    user_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DeleteAddressBookRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "address_book_arn",
                "AddressBookArn",
                TypeInfo(str),
            ),
        ]

    # The ARN of the address book to delete.
    address_book_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DeleteAddressBookResponse(OutputShapeBase):
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
class DeleteContactRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "contact_arn",
                "ContactArn",
                TypeInfo(str),
            ),
        ]

    # The ARN of the contact to delete.
    contact_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DeleteContactResponse(OutputShapeBase):
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
class DeleteProfileRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "profile_arn",
                "ProfileArn",
                TypeInfo(str),
            ),
        ]

    # The ARN of the room profile to delete. Required.
    profile_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DeleteProfileResponse(OutputShapeBase):
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
class DeleteRoomRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "room_arn",
                "RoomArn",
                TypeInfo(str),
            ),
        ]

    # The ARN of the room to delete. Required.
    room_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DeleteRoomResponse(OutputShapeBase):
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
class DeleteRoomSkillParameterRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "skill_id",
                "SkillId",
                TypeInfo(str),
            ),
            (
                "parameter_key",
                "ParameterKey",
                TypeInfo(str),
            ),
            (
                "room_arn",
                "RoomArn",
                TypeInfo(str),
            ),
        ]

    # The ID of the skill from which to remove the room skill parameter details.
    skill_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The room skill parameter key for which to remove details.
    parameter_key: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The ARN of the room from which to remove the room skill parameter details.
    room_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DeleteRoomSkillParameterResponse(OutputShapeBase):
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
class DeleteSkillGroupRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "skill_group_arn",
                "SkillGroupArn",
                TypeInfo(str),
            ),
        ]

    # The ARN of the skill group to delete. Required.
    skill_group_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DeleteSkillGroupResponse(OutputShapeBase):
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
class DeleteUserRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "enrollment_id",
                "EnrollmentId",
                TypeInfo(str),
            ),
            (
                "user_arn",
                "UserArn",
                TypeInfo(str),
            ),
        ]

    # The ARN of the user's enrollment in the organization. Required.
    enrollment_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The ARN of the user to delete in the organization. Required.
    user_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DeleteUserResponse(OutputShapeBase):
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
class Device(ShapeBase):
    """
    A device with attributes.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "device_arn",
                "DeviceArn",
                TypeInfo(str),
            ),
            (
                "device_serial_number",
                "DeviceSerialNumber",
                TypeInfo(str),
            ),
            (
                "device_type",
                "DeviceType",
                TypeInfo(str),
            ),
            (
                "device_name",
                "DeviceName",
                TypeInfo(str),
            ),
            (
                "software_version",
                "SoftwareVersion",
                TypeInfo(str),
            ),
            (
                "mac_address",
                "MacAddress",
                TypeInfo(str),
            ),
            (
                "room_arn",
                "RoomArn",
                TypeInfo(str),
            ),
            (
                "device_status",
                "DeviceStatus",
                TypeInfo(typing.Union[str, DeviceStatus]),
            ),
            (
                "device_status_info",
                "DeviceStatusInfo",
                TypeInfo(DeviceStatusInfo),
            ),
        ]

    # The ARN of a device.
    device_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The serial number of a device.
    device_serial_number: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The type of a device.
    device_type: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The name of a device.
    device_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The software version of a device.
    software_version: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The MAC address of a device.
    mac_address: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The room ARN of a device.
    room_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The status of a device. If the status is not READY, check the
    # DeviceStatusInfo value for details.
    device_status: typing.Union[str, "DeviceStatus"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Detailed information about a device's status.
    device_status_info: "DeviceStatusInfo" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class DeviceData(ShapeBase):
    """
    Device attributes.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "device_arn",
                "DeviceArn",
                TypeInfo(str),
            ),
            (
                "device_serial_number",
                "DeviceSerialNumber",
                TypeInfo(str),
            ),
            (
                "device_type",
                "DeviceType",
                TypeInfo(str),
            ),
            (
                "device_name",
                "DeviceName",
                TypeInfo(str),
            ),
            (
                "software_version",
                "SoftwareVersion",
                TypeInfo(str),
            ),
            (
                "mac_address",
                "MacAddress",
                TypeInfo(str),
            ),
            (
                "device_status",
                "DeviceStatus",
                TypeInfo(typing.Union[str, DeviceStatus]),
            ),
            (
                "room_arn",
                "RoomArn",
                TypeInfo(str),
            ),
            (
                "room_name",
                "RoomName",
                TypeInfo(str),
            ),
            (
                "device_status_info",
                "DeviceStatusInfo",
                TypeInfo(DeviceStatusInfo),
            ),
        ]

    # The ARN of a device.
    device_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The serial number of a device.
    device_serial_number: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The type of a device.
    device_type: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The name of a device.
    device_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The software version of a device.
    software_version: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The MAC address of a device.
    mac_address: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The status of a device.
    device_status: typing.Union[str, "DeviceStatus"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The room ARN associated with a device.
    room_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The name of the room associated with a device.
    room_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Detailed information about a device's status.
    device_status_info: "DeviceStatusInfo" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class DeviceEvent(ShapeBase):
    """
    The list of device events.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "type",
                "Type",
                TypeInfo(typing.Union[str, DeviceEventType]),
            ),
            (
                "value",
                "Value",
                TypeInfo(str),
            ),
            (
                "timestamp",
                "Timestamp",
                TypeInfo(datetime.datetime),
            ),
        ]

    # The type of device event.
    type: typing.Union[str, "DeviceEventType"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The value of the event.
    value: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The time (in epoch) when the event occurred.
    timestamp: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


class DeviceEventType(str):
    CONNECTION_STATUS = "CONNECTION_STATUS"
    DEVICE_STATUS = "DEVICE_STATUS"


@dataclasses.dataclass
class DeviceNotRegisteredException(ShapeBase):
    """
    The request failed because this device is no longer registered and therefore no
    longer managed by this account.
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


class DeviceStatus(str):
    READY = "READY"
    PENDING = "PENDING"
    WAS_OFFLINE = "WAS_OFFLINE"
    DEREGISTERED = "DEREGISTERED"


@dataclasses.dataclass
class DeviceStatusDetail(ShapeBase):
    """
    Details of a device’s status.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "code",
                "Code",
                TypeInfo(typing.Union[str, DeviceStatusDetailCode]),
            ),
        ]

    # The device status detail code.
    code: typing.Union[str, "DeviceStatusDetailCode"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


class DeviceStatusDetailCode(str):
    DEVICE_SOFTWARE_UPDATE_NEEDED = "DEVICE_SOFTWARE_UPDATE_NEEDED"
    DEVICE_WAS_OFFLINE = "DEVICE_WAS_OFFLINE"


@dataclasses.dataclass
class DeviceStatusInfo(ShapeBase):
    """
    Detailed information about a device's status.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "device_status_details",
                "DeviceStatusDetails",
                TypeInfo(typing.List[DeviceStatusDetail]),
            ),
            (
                "connection_status",
                "ConnectionStatus",
                TypeInfo(typing.Union[str, ConnectionStatus]),
            ),
        ]

    # One or more device status detail descriptions.
    device_status_details: typing.List["DeviceStatusDetail"
                                      ] = dataclasses.field(
                                          default=ShapeBase.NOT_SET,
                                      )

    # The latest available information about the connection status of a device.
    connection_status: typing.Union[str, "ConnectionStatus"
                                   ] = dataclasses.field(
                                       default=ShapeBase.NOT_SET,
                                   )


@dataclasses.dataclass
class DisassociateContactFromAddressBookRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "contact_arn",
                "ContactArn",
                TypeInfo(str),
            ),
            (
                "address_book_arn",
                "AddressBookArn",
                TypeInfo(str),
            ),
        ]

    # The ARN of the contact to disassociate from an address book.
    contact_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The ARN of the address from which to disassociate the contact.
    address_book_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DisassociateContactFromAddressBookResponse(OutputShapeBase):
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
class DisassociateDeviceFromRoomRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "device_arn",
                "DeviceArn",
                TypeInfo(str),
            ),
        ]

    # The ARN of the device to disassociate from a room. Required.
    device_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DisassociateDeviceFromRoomResponse(OutputShapeBase):
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
class DisassociateSkillGroupFromRoomRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "skill_group_arn",
                "SkillGroupArn",
                TypeInfo(str),
            ),
            (
                "room_arn",
                "RoomArn",
                TypeInfo(str),
            ),
        ]

    # The ARN of the skill group to disassociate from a room. Required.
    skill_group_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The ARN of the room from which the skill group is to be disassociated.
    # Required.
    room_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DisassociateSkillGroupFromRoomResponse(OutputShapeBase):
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


class DistanceUnit(str):
    METRIC = "METRIC"
    IMPERIAL = "IMPERIAL"


class EnrollmentStatus(str):
    INITIALIZED = "INITIALIZED"
    PENDING = "PENDING"
    REGISTERED = "REGISTERED"
    DISASSOCIATING = "DISASSOCIATING"
    DEREGISTERING = "DEREGISTERING"


class Feature(str):
    BLUETOOTH = "BLUETOOTH"
    VOLUME = "VOLUME"
    NOTIFICATIONS = "NOTIFICATIONS"
    LISTS = "LISTS"
    SKILLS = "SKILLS"
    ALL = "ALL"


@dataclasses.dataclass
class Filter(ShapeBase):
    """
    A filter name and value pair that is used to return a more specific list of
    results. Filters can be used to match a set of resources by various criteria.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "key",
                "Key",
                TypeInfo(str),
            ),
            (
                "values",
                "Values",
                TypeInfo(typing.List[str]),
            ),
        ]

    # The key of a filter.
    key: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The values of a filter.
    values: typing.List[str] = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class GetAddressBookRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "address_book_arn",
                "AddressBookArn",
                TypeInfo(str),
            ),
        ]

    # The ARN of the address book for which to request details.
    address_book_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class GetAddressBookResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "address_book",
                "AddressBook",
                TypeInfo(AddressBook),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The details of the requested address book.
    address_book: "AddressBook" = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class GetContactRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "contact_arn",
                "ContactArn",
                TypeInfo(str),
            ),
        ]

    # The ARN of the contact for which to request details.
    contact_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class GetContactResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "contact",
                "Contact",
                TypeInfo(Contact),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The details of the requested contact.
    contact: "Contact" = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class GetDeviceRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "device_arn",
                "DeviceArn",
                TypeInfo(str),
            ),
        ]

    # The ARN of the device for which to request details. Required.
    device_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class GetDeviceResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "device",
                "Device",
                TypeInfo(Device),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The details of the device requested. Required.
    device: "Device" = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class GetProfileRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "profile_arn",
                "ProfileArn",
                TypeInfo(str),
            ),
        ]

    # The ARN of the room profile for which to request details. Required.
    profile_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class GetProfileResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "profile",
                "Profile",
                TypeInfo(Profile),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The details of the room profile requested. Required.
    profile: "Profile" = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class GetRoomRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "room_arn",
                "RoomArn",
                TypeInfo(str),
            ),
        ]

    # The ARN of the room for which to request details. Required.
    room_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class GetRoomResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "room",
                "Room",
                TypeInfo(Room),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The details of the room requested.
    room: "Room" = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class GetRoomSkillParameterRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "skill_id",
                "SkillId",
                TypeInfo(str),
            ),
            (
                "parameter_key",
                "ParameterKey",
                TypeInfo(str),
            ),
            (
                "room_arn",
                "RoomArn",
                TypeInfo(str),
            ),
        ]

    # The ARN of the skill from which to get the room skill parameter details.
    # Required.
    skill_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The room skill parameter key for which to get details. Required.
    parameter_key: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The ARN of the room from which to get the room skill parameter details.
    room_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class GetRoomSkillParameterResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "room_skill_parameter",
                "RoomSkillParameter",
                TypeInfo(RoomSkillParameter),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The details of the room skill parameter requested. Required.
    room_skill_parameter: "RoomSkillParameter" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class GetSkillGroupRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "skill_group_arn",
                "SkillGroupArn",
                TypeInfo(str),
            ),
        ]

    # The ARN of the skill group for which to get details. Required.
    skill_group_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class GetSkillGroupResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "skill_group",
                "SkillGroup",
                TypeInfo(SkillGroup),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The details of the skill group requested. Required.
    skill_group: "SkillGroup" = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class InvalidUserStatusException(ShapeBase):
    """
    The attempt to update a user is invalid due to the user's current status. HTTP
    Status Code: 400
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
class LimitExceededException(ShapeBase):
    """
    You are performing an action that would put you beyond your account's limits.
    HTTP Status Code: 400
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
class ListDeviceEventsRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "device_arn",
                "DeviceArn",
                TypeInfo(str),
            ),
            (
                "event_type",
                "EventType",
                TypeInfo(typing.Union[str, DeviceEventType]),
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

    # The ARN of a device.
    device_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The event type to filter device events. If EventType isn't specified, this
    # returns a list of all device events in reverse chronological order. If
    # EventType is specified, this returns a list of device events for that
    # EventType in reverse chronological order.
    event_type: typing.Union[str, "DeviceEventType"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # An optional token returned from a prior request. Use this token for
    # pagination of results from this action. If this parameter is specified, the
    # response only includes results beyond the token, up to the value specified
    # by MaxResults. When the end of results is reached, the response has a value
    # of null.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The maximum number of results to include in the response. The default value
    # is 50. If more results exist than the specified MaxResults value, a token
    # is included in the response so that the remaining results can be retrieved.
    max_results: int = dataclasses.field(default=ShapeBase.NOT_SET, )


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
                "device_events",
                "DeviceEvents",
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

    # The device events requested for the device ARN.
    device_events: typing.List["DeviceEvent"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The token returned to indicate that there is more data available.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ListSkillsRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "skill_group_arn",
                "SkillGroupArn",
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

    # The ARN of the skill group for which to list enabled skills. Required.
    skill_group_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # An optional token returned from a prior request. Use this token for
    # pagination of results from this action. If this parameter is specified, the
    # response includes only results beyond the token, up to the value specified
    # by `MaxResults`. Required.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The maximum number of results to include in the response. If more results
    # exist than the specified `MaxResults` value, a token is included in the
    # response so that the remaining results can be retrieved. Required.
    max_results: int = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ListSkillsResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "skill_summaries",
                "SkillSummaries",
                TypeInfo(typing.List[SkillSummary]),
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

    # The list of enabled skills requested. Required.
    skill_summaries: typing.List["SkillSummary"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The token returned to indicate that there is more data available.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    def paginate(self, ) -> typing.Generator["ListSkillsResponse", None, None]:
        yield from super()._paginate()


@dataclasses.dataclass
class ListTagsRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "arn",
                "Arn",
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

    # The ARN of the specified resource for which to list tags.
    arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # An optional token returned from a prior request. Use this token for
    # pagination of results from this action. If this parameter is specified, the
    # response includes only results beyond the token, up to the value specified
    # by `MaxResults`.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The maximum number of results to include in the response. If more results
    # exist than the specified `MaxResults` value, a token is included in the
    # response so that the remaining results can be retrieved.
    max_results: int = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ListTagsResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "tags",
                "Tags",
                TypeInfo(typing.List[Tag]),
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

    # The tags requested for the specified resource.
    tags: typing.List["Tag"] = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The token returned to indicate that there is more data available.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    def paginate(self, ) -> typing.Generator["ListTagsResponse", None, None]:
        yield from super()._paginate()


@dataclasses.dataclass
class NameInUseException(ShapeBase):
    """
    The name sent in the request is already in use. HTTP Status Code: 400
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
class NotFoundException(ShapeBase):
    """
    The resource is not found. HTTP Status Code: 400
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
class Profile(ShapeBase):
    """
    A room profile with attributes.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "profile_arn",
                "ProfileArn",
                TypeInfo(str),
            ),
            (
                "profile_name",
                "ProfileName",
                TypeInfo(str),
            ),
            (
                "address",
                "Address",
                TypeInfo(str),
            ),
            (
                "timezone",
                "Timezone",
                TypeInfo(str),
            ),
            (
                "distance_unit",
                "DistanceUnit",
                TypeInfo(typing.Union[str, DistanceUnit]),
            ),
            (
                "temperature_unit",
                "TemperatureUnit",
                TypeInfo(typing.Union[str, TemperatureUnit]),
            ),
            (
                "wake_word",
                "WakeWord",
                TypeInfo(typing.Union[str, WakeWord]),
            ),
            (
                "setup_mode_disabled",
                "SetupModeDisabled",
                TypeInfo(bool),
            ),
            (
                "max_volume_limit",
                "MaxVolumeLimit",
                TypeInfo(int),
            ),
            (
                "pstn_enabled",
                "PSTNEnabled",
                TypeInfo(bool),
            ),
        ]

    # The ARN of a room profile.
    profile_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The name of a room profile.
    profile_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The address of a room profile.
    address: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The time zone of a room profile.
    timezone: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The distance unit of a room profile.
    distance_unit: typing.Union[str, "DistanceUnit"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The temperature unit of a room profile.
    temperature_unit: typing.Union[str, "TemperatureUnit"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The wake word of a room profile.
    wake_word: typing.Union[str, "WakeWord"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The setup mode of a room profile.
    setup_mode_disabled: bool = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The max volume limit of a room profile.
    max_volume_limit: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The PSTN setting of a room profile.
    pstn_enabled: bool = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ProfileData(ShapeBase):
    """
    The data of a room profile.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "profile_arn",
                "ProfileArn",
                TypeInfo(str),
            ),
            (
                "profile_name",
                "ProfileName",
                TypeInfo(str),
            ),
            (
                "address",
                "Address",
                TypeInfo(str),
            ),
            (
                "timezone",
                "Timezone",
                TypeInfo(str),
            ),
            (
                "distance_unit",
                "DistanceUnit",
                TypeInfo(typing.Union[str, DistanceUnit]),
            ),
            (
                "temperature_unit",
                "TemperatureUnit",
                TypeInfo(typing.Union[str, TemperatureUnit]),
            ),
            (
                "wake_word",
                "WakeWord",
                TypeInfo(typing.Union[str, WakeWord]),
            ),
        ]

    # The ARN of a room profile.
    profile_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The name of a room profile.
    profile_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The address of a room profile.
    address: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The timezone of a room profile.
    timezone: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The distance unit of a room profile.
    distance_unit: typing.Union[str, "DistanceUnit"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The temperature unit of a room profile.
    temperature_unit: typing.Union[str, "TemperatureUnit"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The wake word of a room profile.
    wake_word: typing.Union[str, "WakeWord"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class PutRoomSkillParameterRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "skill_id",
                "SkillId",
                TypeInfo(str),
            ),
            (
                "room_skill_parameter",
                "RoomSkillParameter",
                TypeInfo(RoomSkillParameter),
            ),
            (
                "room_arn",
                "RoomArn",
                TypeInfo(str),
            ),
        ]

    # The ARN of the skill associated with the room skill parameter. Required.
    skill_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The updated room skill parameter. Required.
    room_skill_parameter: "RoomSkillParameter" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The ARN of the room associated with the room skill parameter. Required.
    room_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class PutRoomSkillParameterResponse(OutputShapeBase):
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
class ResolveRoomRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "user_id",
                "UserId",
                TypeInfo(str),
            ),
            (
                "skill_id",
                "SkillId",
                TypeInfo(str),
            ),
        ]

    # The ARN of the user. Required.
    user_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The ARN of the skill that was requested. Required.
    skill_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ResolveRoomResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "room_arn",
                "RoomArn",
                TypeInfo(str),
            ),
            (
                "room_name",
                "RoomName",
                TypeInfo(str),
            ),
            (
                "room_skill_parameters",
                "RoomSkillParameters",
                TypeInfo(typing.List[RoomSkillParameter]),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The ARN of the room from which the skill request was invoked.
    room_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The name of the room from which the skill request was invoked.
    room_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Response to get the room profile request. Required.
    room_skill_parameters: typing.List["RoomSkillParameter"
                                      ] = dataclasses.field(
                                          default=ShapeBase.NOT_SET,
                                      )


@dataclasses.dataclass
class ResourceInUseException(ShapeBase):
    """
    The resource in the request is already in use. HTTP Status Code: 400
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
                "client_request_token",
                "ClientRequestToken",
                TypeInfo(str),
            ),
        ]

    message: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # User specified token that is used to support idempotency during Create
    # Resource
    client_request_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class RevokeInvitationRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "user_arn",
                "UserArn",
                TypeInfo(str),
            ),
            (
                "enrollment_id",
                "EnrollmentId",
                TypeInfo(str),
            ),
        ]

    # The ARN of the user for whom to revoke an enrollment invitation. Required.
    user_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The ARN of the enrollment invitation to revoke. Required.
    enrollment_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class RevokeInvitationResponse(OutputShapeBase):
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
class Room(ShapeBase):
    """
    A room with attributes.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "room_arn",
                "RoomArn",
                TypeInfo(str),
            ),
            (
                "room_name",
                "RoomName",
                TypeInfo(str),
            ),
            (
                "description",
                "Description",
                TypeInfo(str),
            ),
            (
                "provider_calendar_id",
                "ProviderCalendarId",
                TypeInfo(str),
            ),
            (
                "profile_arn",
                "ProfileArn",
                TypeInfo(str),
            ),
        ]

    # The ARN of a room.
    room_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The name of a room.
    room_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The description of a room.
    description: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The provider calendar ARN of a room.
    provider_calendar_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The profile ARN of a room.
    profile_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class RoomData(ShapeBase):
    """
    The data of a room.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "room_arn",
                "RoomArn",
                TypeInfo(str),
            ),
            (
                "room_name",
                "RoomName",
                TypeInfo(str),
            ),
            (
                "description",
                "Description",
                TypeInfo(str),
            ),
            (
                "provider_calendar_id",
                "ProviderCalendarId",
                TypeInfo(str),
            ),
            (
                "profile_arn",
                "ProfileArn",
                TypeInfo(str),
            ),
            (
                "profile_name",
                "ProfileName",
                TypeInfo(str),
            ),
        ]

    # The ARN of a room.
    room_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The name of a room.
    room_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The description of a room.
    description: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The provider calendar ARN of a room.
    provider_calendar_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The profile ARN of a room.
    profile_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The profile name of a room.
    profile_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class RoomSkillParameter(ShapeBase):
    """
    A skill parameter associated with a room.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "parameter_key",
                "ParameterKey",
                TypeInfo(str),
            ),
            (
                "parameter_value",
                "ParameterValue",
                TypeInfo(str),
            ),
        ]

    # The parameter key of a room skill parameter. ParameterKey is an enumerated
    # type that only takes “DEFAULT” or “SCOPE” as valid values.
    parameter_key: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The parameter value of a room skill parameter.
    parameter_value: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class SearchAddressBooksRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "filters",
                "Filters",
                TypeInfo(typing.List[Filter]),
            ),
            (
                "sort_criteria",
                "SortCriteria",
                TypeInfo(typing.List[Sort]),
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

    # The filters to use to list a specified set of address books. The supported
    # filter key is AddressBookName.
    filters: typing.List["Filter"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The sort order to use in listing the specified set of address books. The
    # supported sort key is AddressBookName.
    sort_criteria: typing.List["Sort"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # An optional token returned from a prior request. Use this token for
    # pagination of results from this action. If this parameter is specified, the
    # response only includes results beyond the token, up to the value specified
    # by MaxResults.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The maximum number of results to include in the response. If more results
    # exist than the specified MaxResults value, a token is included in the
    # response so that the remaining results can be retrieved.
    max_results: int = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class SearchAddressBooksResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "address_books",
                "AddressBooks",
                TypeInfo(typing.List[AddressBookData]),
            ),
            (
                "next_token",
                "NextToken",
                TypeInfo(str),
            ),
            (
                "total_count",
                "TotalCount",
                TypeInfo(int),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The address books that meet the specified set of filter criteria, in sort
    # order.
    address_books: typing.List["AddressBookData"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The token returned to indicate that there is more data available.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The total number of address books returned.
    total_count: int = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class SearchContactsRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "filters",
                "Filters",
                TypeInfo(typing.List[Filter]),
            ),
            (
                "sort_criteria",
                "SortCriteria",
                TypeInfo(typing.List[Sort]),
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

    # The filters to use to list a specified set of address books. The supported
    # filter keys are DisplayName, FirstName, LastName, and AddressBookArns.
    filters: typing.List["Filter"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The sort order to use in listing the specified set of contacts. The
    # supported sort keys are DisplayName, FirstName, and LastName.
    sort_criteria: typing.List["Sort"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # An optional token returned from a prior request. Use this token for
    # pagination of results from this action. If this parameter is specified, the
    # response only includes results beyond the token, up to the value specified
    # by MaxResults.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The maximum number of results to include in the response. If more results
    # exist than the specified MaxResults value, a token is included in the
    # response so that the remaining results can be retrieved.
    max_results: int = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class SearchContactsResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "contacts",
                "Contacts",
                TypeInfo(typing.List[ContactData]),
            ),
            (
                "next_token",
                "NextToken",
                TypeInfo(str),
            ),
            (
                "total_count",
                "TotalCount",
                TypeInfo(int),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The contacts that meet the specified set of filter criteria, in sort order.
    contacts: typing.List["ContactData"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The token returned to indicate that there is more data available.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The total number of contacts returned.
    total_count: int = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class SearchDevicesRequest(ShapeBase):
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
                "filters",
                "Filters",
                TypeInfo(typing.List[Filter]),
            ),
            (
                "sort_criteria",
                "SortCriteria",
                TypeInfo(typing.List[Sort]),
            ),
        ]

    # An optional token returned from a prior request. Use this token for
    # pagination of results from this action. If this parameter is specified, the
    # response includes only results beyond the token, up to the value specified
    # by `MaxResults`.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The maximum number of results to include in the response. If more results
    # exist than the specified `MaxResults` value, a token is included in the
    # response so that the remaining results can be retrieved.
    max_results: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The filters to use to list a specified set of devices. Supported filter
    # keys are DeviceName, DeviceStatus, DeviceStatusDetailCode, RoomName,
    # DeviceType, DeviceSerialNumber, UnassociatedOnly, and ConnectionStatus
    # (ONLINE and OFFLINE).
    filters: typing.List["Filter"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The sort order to use in listing the specified set of devices. Supported
    # sort keys are DeviceName, DeviceStatus, RoomName, DeviceType,
    # DeviceSerialNumber, and ConnectionStatus.
    sort_criteria: typing.List["Sort"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class SearchDevicesResponse(OutputShapeBase):
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
                TypeInfo(typing.List[DeviceData]),
            ),
            (
                "next_token",
                "NextToken",
                TypeInfo(str),
            ),
            (
                "total_count",
                "TotalCount",
                TypeInfo(int),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The devices that meet the specified set of filter criteria, in sort order.
    devices: typing.List["DeviceData"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The token returned to indicate that there is more data available.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The total number of devices returned.
    total_count: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    def paginate(self,
                ) -> typing.Generator["SearchDevicesResponse", None, None]:
        yield from super()._paginate()


@dataclasses.dataclass
class SearchProfilesRequest(ShapeBase):
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
                "filters",
                "Filters",
                TypeInfo(typing.List[Filter]),
            ),
            (
                "sort_criteria",
                "SortCriteria",
                TypeInfo(typing.List[Sort]),
            ),
        ]

    # An optional token returned from a prior request. Use this token for
    # pagination of results from this action. If this parameter is specified, the
    # response includes only results beyond the token, up to the value specified
    # by `MaxResults`.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The maximum number of results to include in the response. If more results
    # exist than the specified `MaxResults` value, a token is included in the
    # response so that the remaining results can be retrieved.
    max_results: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The filters to use to list a specified set of room profiles. Supported
    # filter keys are ProfileName and Address. Required.
    filters: typing.List["Filter"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The sort order to use in listing the specified set of room profiles.
    # Supported sort keys are ProfileName and Address.
    sort_criteria: typing.List["Sort"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class SearchProfilesResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "profiles",
                "Profiles",
                TypeInfo(typing.List[ProfileData]),
            ),
            (
                "next_token",
                "NextToken",
                TypeInfo(str),
            ),
            (
                "total_count",
                "TotalCount",
                TypeInfo(int),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The profiles that meet the specified set of filter criteria, in sort order.
    profiles: typing.List["ProfileData"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The token returned to indicate that there is more data available.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The total number of room profiles returned.
    total_count: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    def paginate(self,
                ) -> typing.Generator["SearchProfilesResponse", None, None]:
        yield from super()._paginate()


@dataclasses.dataclass
class SearchRoomsRequest(ShapeBase):
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
                "filters",
                "Filters",
                TypeInfo(typing.List[Filter]),
            ),
            (
                "sort_criteria",
                "SortCriteria",
                TypeInfo(typing.List[Sort]),
            ),
        ]

    # An optional token returned from a prior request. Use this token for
    # pagination of results from this action. If this parameter is specified, the
    # response includes only results beyond the token, up to the value specified
    # by `MaxResults`.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The maximum number of results to include in the response. If more results
    # exist than the specified `MaxResults` value, a token is included in the
    # response so that the remaining results can be retrieved.
    max_results: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The filters to use to list a specified set of rooms. The supported filter
    # keys are RoomName and ProfileName.
    filters: typing.List["Filter"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The sort order to use in listing the specified set of rooms. The supported
    # sort keys are RoomName and ProfileName.
    sort_criteria: typing.List["Sort"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class SearchRoomsResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "rooms",
                "Rooms",
                TypeInfo(typing.List[RoomData]),
            ),
            (
                "next_token",
                "NextToken",
                TypeInfo(str),
            ),
            (
                "total_count",
                "TotalCount",
                TypeInfo(int),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The rooms that meet the specified set of filter criteria, in sort order.
    rooms: typing.List["RoomData"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The token returned to indicate that there is more data available.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The total number of rooms returned.
    total_count: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    def paginate(self, ) -> typing.Generator["SearchRoomsResponse", None, None]:
        yield from super()._paginate()


@dataclasses.dataclass
class SearchSkillGroupsRequest(ShapeBase):
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
                "filters",
                "Filters",
                TypeInfo(typing.List[Filter]),
            ),
            (
                "sort_criteria",
                "SortCriteria",
                TypeInfo(typing.List[Sort]),
            ),
        ]

    # An optional token returned from a prior request. Use this token for
    # pagination of results from this action. If this parameter is specified, the
    # response includes only results beyond the token, up to the value specified
    # by `MaxResults`. Required.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The maximum number of results to include in the response. If more results
    # exist than the specified `MaxResults` value, a token is included in the
    # response so that the remaining results can be retrieved.
    max_results: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The filters to use to list a specified set of skill groups. The supported
    # filter key is SkillGroupName.
    filters: typing.List["Filter"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The sort order to use in listing the specified set of skill groups. The
    # supported sort key is SkillGroupName.
    sort_criteria: typing.List["Sort"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class SearchSkillGroupsResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "skill_groups",
                "SkillGroups",
                TypeInfo(typing.List[SkillGroupData]),
            ),
            (
                "next_token",
                "NextToken",
                TypeInfo(str),
            ),
            (
                "total_count",
                "TotalCount",
                TypeInfo(int),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The skill groups that meet the filter criteria, in sort order.
    skill_groups: typing.List["SkillGroupData"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The token returned to indicate that there is more data available.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The total number of skill groups returned.
    total_count: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    def paginate(self,
                ) -> typing.Generator["SearchSkillGroupsResponse", None, None]:
        yield from super()._paginate()


@dataclasses.dataclass
class SearchUsersRequest(ShapeBase):
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
                "filters",
                "Filters",
                TypeInfo(typing.List[Filter]),
            ),
            (
                "sort_criteria",
                "SortCriteria",
                TypeInfo(typing.List[Sort]),
            ),
        ]

    # An optional token returned from a prior request. Use this token for
    # pagination of results from this action. If this parameter is specified, the
    # response includes only results beyond the token, up to the value specified
    # by `MaxResults`. Required.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The maximum number of results to include in the response. If more results
    # exist than the specified `MaxResults` value, a token is included in the
    # response so that the remaining results can be retrieved. Required.
    max_results: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The filters to use for listing a specific set of users. Required. Supported
    # filter keys are UserId, FirstName, LastName, Email, and EnrollmentStatus.
    filters: typing.List["Filter"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The sort order to use in listing the filtered set of users. Required.
    # Supported sort keys are UserId, FirstName, LastName, Email, and
    # EnrollmentStatus.
    sort_criteria: typing.List["Sort"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class SearchUsersResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "users",
                "Users",
                TypeInfo(typing.List[UserData]),
            ),
            (
                "next_token",
                "NextToken",
                TypeInfo(str),
            ),
            (
                "total_count",
                "TotalCount",
                TypeInfo(int),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The users that meet the specified set of filter criteria, in sort order.
    users: typing.List["UserData"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The token returned to indicate that there is more data available.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The total number of users returned.
    total_count: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    def paginate(self, ) -> typing.Generator["SearchUsersResponse", None, None]:
        yield from super()._paginate()


@dataclasses.dataclass
class SendInvitationRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "user_arn",
                "UserArn",
                TypeInfo(str),
            ),
        ]

    # The ARN of the user to whom to send an invitation. Required.
    user_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class SendInvitationResponse(OutputShapeBase):
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
class SkillGroup(ShapeBase):
    """
    A skill group with attributes.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "skill_group_arn",
                "SkillGroupArn",
                TypeInfo(str),
            ),
            (
                "skill_group_name",
                "SkillGroupName",
                TypeInfo(str),
            ),
            (
                "description",
                "Description",
                TypeInfo(str),
            ),
        ]

    # The ARN of a skill group.
    skill_group_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The name of a skill group.
    skill_group_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The description of a skill group.
    description: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class SkillGroupData(ShapeBase):
    """
    The attributes of a skill group.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "skill_group_arn",
                "SkillGroupArn",
                TypeInfo(str),
            ),
            (
                "skill_group_name",
                "SkillGroupName",
                TypeInfo(str),
            ),
            (
                "description",
                "Description",
                TypeInfo(str),
            ),
        ]

    # The skill group ARN of a skill group.
    skill_group_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The skill group name of a skill group.
    skill_group_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The description of a skill group.
    description: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class SkillSummary(ShapeBase):
    """
    The summary of skills.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "skill_id",
                "SkillId",
                TypeInfo(str),
            ),
            (
                "skill_name",
                "SkillName",
                TypeInfo(str),
            ),
            (
                "supports_linking",
                "SupportsLinking",
                TypeInfo(bool),
            ),
        ]

    # The ARN of the skill summary.
    skill_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The name of the skill.
    skill_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Linking support for a skill.
    supports_linking: bool = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class Sort(ShapeBase):
    """
    An object representing a sort criteria.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "key",
                "Key",
                TypeInfo(str),
            ),
            (
                "value",
                "Value",
                TypeInfo(typing.Union[str, SortValue]),
            ),
        ]

    # The sort key of a sort object.
    key: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The sort value of a sort object.
    value: typing.Union[str, "SortValue"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


class SortValue(str):
    ASC = "ASC"
    DESC = "DESC"


@dataclasses.dataclass
class StartDeviceSyncRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "features",
                "Features",
                TypeInfo(typing.List[typing.Union[str, Feature]]),
            ),
            (
                "room_arn",
                "RoomArn",
                TypeInfo(str),
            ),
            (
                "device_arn",
                "DeviceArn",
                TypeInfo(str),
            ),
        ]

    # Request structure to start the device sync. Required.
    features: typing.List[typing.Union[str, "Feature"]] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The ARN of the room with which the device to sync is associated. Required.
    room_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The ARN of the device to sync. Required.
    device_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class StartDeviceSyncResponse(OutputShapeBase):
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
class Tag(ShapeBase):
    """
    A key-value pair that can be associated with a resource.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "key",
                "Key",
                TypeInfo(str),
            ),
            (
                "value",
                "Value",
                TypeInfo(str),
            ),
        ]

    # The key of a tag. Tag keys are case-sensitive.
    key: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The value of a tag. Tag values are case-sensitive and can be null.
    value: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class TagResourceRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "arn",
                "Arn",
                TypeInfo(str),
            ),
            (
                "tags",
                "Tags",
                TypeInfo(typing.List[Tag]),
            ),
        ]

    # The ARN of the resource to which to add metadata tags. Required.
    arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The tags to be added to the specified resource. Do not provide system tags.
    # Required.
    tags: typing.List["Tag"] = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class TagResourceResponse(OutputShapeBase):
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


class TemperatureUnit(str):
    FAHRENHEIT = "FAHRENHEIT"
    CELSIUS = "CELSIUS"


@dataclasses.dataclass
class UntagResourceRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "arn",
                "Arn",
                TypeInfo(str),
            ),
            (
                "tag_keys",
                "TagKeys",
                TypeInfo(typing.List[str]),
            ),
        ]

    # The ARN of the resource from which to remove metadata tags. Required.
    arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The tags to be removed from the specified resource. Do not provide system
    # tags. Required.
    tag_keys: typing.List[str] = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class UntagResourceResponse(OutputShapeBase):
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
class UpdateAddressBookRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "address_book_arn",
                "AddressBookArn",
                TypeInfo(str),
            ),
            (
                "name",
                "Name",
                TypeInfo(str),
            ),
            (
                "description",
                "Description",
                TypeInfo(str),
            ),
        ]

    # The ARN of the room to update.
    address_book_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The updated name of the room.
    name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The updated description of the room.
    description: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class UpdateAddressBookResponse(OutputShapeBase):
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
class UpdateContactRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "contact_arn",
                "ContactArn",
                TypeInfo(str),
            ),
            (
                "display_name",
                "DisplayName",
                TypeInfo(str),
            ),
            (
                "first_name",
                "FirstName",
                TypeInfo(str),
            ),
            (
                "last_name",
                "LastName",
                TypeInfo(str),
            ),
            (
                "phone_number",
                "PhoneNumber",
                TypeInfo(str),
            ),
        ]

    # The ARN of the contact to update.
    contact_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The updated display name of the contact.
    display_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The updated first name of the contact.
    first_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The updated last name of the contact.
    last_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The updated phone number of the contact.
    phone_number: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class UpdateContactResponse(OutputShapeBase):
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
class UpdateDeviceRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "device_arn",
                "DeviceArn",
                TypeInfo(str),
            ),
            (
                "device_name",
                "DeviceName",
                TypeInfo(str),
            ),
        ]

    # The ARN of the device to update. Required.
    device_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The updated device name. Required.
    device_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class UpdateDeviceResponse(OutputShapeBase):
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
class UpdateProfileRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "profile_arn",
                "ProfileArn",
                TypeInfo(str),
            ),
            (
                "profile_name",
                "ProfileName",
                TypeInfo(str),
            ),
            (
                "timezone",
                "Timezone",
                TypeInfo(str),
            ),
            (
                "address",
                "Address",
                TypeInfo(str),
            ),
            (
                "distance_unit",
                "DistanceUnit",
                TypeInfo(typing.Union[str, DistanceUnit]),
            ),
            (
                "temperature_unit",
                "TemperatureUnit",
                TypeInfo(typing.Union[str, TemperatureUnit]),
            ),
            (
                "wake_word",
                "WakeWord",
                TypeInfo(typing.Union[str, WakeWord]),
            ),
            (
                "setup_mode_disabled",
                "SetupModeDisabled",
                TypeInfo(bool),
            ),
            (
                "max_volume_limit",
                "MaxVolumeLimit",
                TypeInfo(int),
            ),
            (
                "pstn_enabled",
                "PSTNEnabled",
                TypeInfo(bool),
            ),
        ]

    # The ARN of the room profile to update. Required.
    profile_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The updated name for the room profile.
    profile_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The updated timezone for the room profile.
    timezone: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The updated address for the room profile.
    address: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The updated distance unit for the room profile.
    distance_unit: typing.Union[str, "DistanceUnit"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The updated temperature unit for the room profile.
    temperature_unit: typing.Union[str, "TemperatureUnit"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The updated wake word for the room profile.
    wake_word: typing.Union[str, "WakeWord"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Whether the setup mode of the profile is enabled.
    setup_mode_disabled: bool = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The updated maximum volume limit for the room profile.
    max_volume_limit: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Whether the PSTN setting of the room profile is enabled.
    pstn_enabled: bool = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class UpdateProfileResponse(OutputShapeBase):
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
class UpdateRoomRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "room_arn",
                "RoomArn",
                TypeInfo(str),
            ),
            (
                "room_name",
                "RoomName",
                TypeInfo(str),
            ),
            (
                "description",
                "Description",
                TypeInfo(str),
            ),
            (
                "provider_calendar_id",
                "ProviderCalendarId",
                TypeInfo(str),
            ),
            (
                "profile_arn",
                "ProfileArn",
                TypeInfo(str),
            ),
        ]

    # The ARN of the room to update.
    room_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The updated name for the room.
    room_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The updated description for the room.
    description: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The updated provider calendar ARN for the room.
    provider_calendar_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The updated profile ARN for the room.
    profile_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class UpdateRoomResponse(OutputShapeBase):
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
class UpdateSkillGroupRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "skill_group_arn",
                "SkillGroupArn",
                TypeInfo(str),
            ),
            (
                "skill_group_name",
                "SkillGroupName",
                TypeInfo(str),
            ),
            (
                "description",
                "Description",
                TypeInfo(str),
            ),
        ]

    # The ARN of the skill group to update.
    skill_group_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The updated name for the skill group.
    skill_group_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The updated description for the skill group.
    description: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class UpdateSkillGroupResponse(OutputShapeBase):
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
class UserData(ShapeBase):
    """
    Information related to a user.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "user_arn",
                "UserArn",
                TypeInfo(str),
            ),
            (
                "first_name",
                "FirstName",
                TypeInfo(str),
            ),
            (
                "last_name",
                "LastName",
                TypeInfo(str),
            ),
            (
                "email",
                "Email",
                TypeInfo(str),
            ),
            (
                "enrollment_status",
                "EnrollmentStatus",
                TypeInfo(typing.Union[str, EnrollmentStatus]),
            ),
            (
                "enrollment_id",
                "EnrollmentId",
                TypeInfo(str),
            ),
        ]

    # The ARN of a user.
    user_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The first name of a user.
    first_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The last name of a user.
    last_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The email of a user.
    email: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The enrollment status of a user.
    enrollment_status: typing.Union[str, "EnrollmentStatus"
                                   ] = dataclasses.field(
                                       default=ShapeBase.NOT_SET,
                                   )

    # The enrollment ARN of a user.
    enrollment_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )


class WakeWord(str):
    ALEXA = "ALEXA"
    AMAZON = "AMAZON"
    ECHO = "ECHO"
    COMPUTER = "COMPUTER"
