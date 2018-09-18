import datetime
import typing
import boto3
from autoboto import ClientBase, ShapeBase, OutputShapeBase
from . import shapes


class Client(ClientBase):
    def __init__(self, *args, **kwargs):
        super().__init__("alexaforbusiness", *args, **kwargs)

    def associate_contact_with_address_book(
        self,
        _request: shapes.AssociateContactWithAddressBookRequest = None,
        *,
        contact_arn: str,
        address_book_arn: str,
    ) -> shapes.AssociateContactWithAddressBookResponse:
        """
        Associates a contact with a given address book.
        """
        if _request is None:
            _params = {}
            if contact_arn is not ShapeBase.NOT_SET:
                _params['contact_arn'] = contact_arn
            if address_book_arn is not ShapeBase.NOT_SET:
                _params['address_book_arn'] = address_book_arn
            _request = shapes.AssociateContactWithAddressBookRequest(**_params)
        response = self._boto_client.associate_contact_with_address_book(
            **_request.to_boto()
        )

        return shapes.AssociateContactWithAddressBookResponse.from_boto(
            response
        )

    def associate_device_with_room(
        self,
        _request: shapes.AssociateDeviceWithRoomRequest = None,
        *,
        device_arn: str = ShapeBase.NOT_SET,
        room_arn: str = ShapeBase.NOT_SET,
    ) -> shapes.AssociateDeviceWithRoomResponse:
        """
        Associates a device with a given room. This applies all the settings from the
        room profile to the device, and all the skills in any skill groups added to that
        room. This operation requires the device to be online, or else a manual sync is
        required.
        """
        if _request is None:
            _params = {}
            if device_arn is not ShapeBase.NOT_SET:
                _params['device_arn'] = device_arn
            if room_arn is not ShapeBase.NOT_SET:
                _params['room_arn'] = room_arn
            _request = shapes.AssociateDeviceWithRoomRequest(**_params)
        response = self._boto_client.associate_device_with_room(
            **_request.to_boto()
        )

        return shapes.AssociateDeviceWithRoomResponse.from_boto(response)

    def associate_skill_group_with_room(
        self,
        _request: shapes.AssociateSkillGroupWithRoomRequest = None,
        *,
        skill_group_arn: str = ShapeBase.NOT_SET,
        room_arn: str = ShapeBase.NOT_SET,
    ) -> shapes.AssociateSkillGroupWithRoomResponse:
        """
        Associates a skill group with a given room. This enables all skills in the
        associated skill group on all devices in the room.
        """
        if _request is None:
            _params = {}
            if skill_group_arn is not ShapeBase.NOT_SET:
                _params['skill_group_arn'] = skill_group_arn
            if room_arn is not ShapeBase.NOT_SET:
                _params['room_arn'] = room_arn
            _request = shapes.AssociateSkillGroupWithRoomRequest(**_params)
        response = self._boto_client.associate_skill_group_with_room(
            **_request.to_boto()
        )

        return shapes.AssociateSkillGroupWithRoomResponse.from_boto(response)

    def create_address_book(
        self,
        _request: shapes.CreateAddressBookRequest = None,
        *,
        name: str,
        description: str = ShapeBase.NOT_SET,
        client_request_token: str = ShapeBase.NOT_SET,
    ) -> shapes.CreateAddressBookResponse:
        """
        Creates an address book with the specified details.
        """
        if _request is None:
            _params = {}
            if name is not ShapeBase.NOT_SET:
                _params['name'] = name
            if description is not ShapeBase.NOT_SET:
                _params['description'] = description
            if client_request_token is not ShapeBase.NOT_SET:
                _params['client_request_token'] = client_request_token
            _request = shapes.CreateAddressBookRequest(**_params)
        response = self._boto_client.create_address_book(**_request.to_boto())

        return shapes.CreateAddressBookResponse.from_boto(response)

    def create_contact(
        self,
        _request: shapes.CreateContactRequest = None,
        *,
        first_name: str,
        phone_number: str,
        display_name: str = ShapeBase.NOT_SET,
        last_name: str = ShapeBase.NOT_SET,
        client_request_token: str = ShapeBase.NOT_SET,
    ) -> shapes.CreateContactResponse:
        """
        Creates a contact with the specified details.
        """
        if _request is None:
            _params = {}
            if first_name is not ShapeBase.NOT_SET:
                _params['first_name'] = first_name
            if phone_number is not ShapeBase.NOT_SET:
                _params['phone_number'] = phone_number
            if display_name is not ShapeBase.NOT_SET:
                _params['display_name'] = display_name
            if last_name is not ShapeBase.NOT_SET:
                _params['last_name'] = last_name
            if client_request_token is not ShapeBase.NOT_SET:
                _params['client_request_token'] = client_request_token
            _request = shapes.CreateContactRequest(**_params)
        response = self._boto_client.create_contact(**_request.to_boto())

        return shapes.CreateContactResponse.from_boto(response)

    def create_profile(
        self,
        _request: shapes.CreateProfileRequest = None,
        *,
        profile_name: str,
        timezone: str,
        address: str,
        distance_unit: typing.Union[str, shapes.DistanceUnit],
        temperature_unit: typing.Union[str, shapes.TemperatureUnit],
        wake_word: typing.Union[str, shapes.WakeWord],
        client_request_token: str = ShapeBase.NOT_SET,
        setup_mode_disabled: bool = ShapeBase.NOT_SET,
        max_volume_limit: int = ShapeBase.NOT_SET,
        pstn_enabled: bool = ShapeBase.NOT_SET,
    ) -> shapes.CreateProfileResponse:
        """
        Creates a new room profile with the specified details.
        """
        if _request is None:
            _params = {}
            if profile_name is not ShapeBase.NOT_SET:
                _params['profile_name'] = profile_name
            if timezone is not ShapeBase.NOT_SET:
                _params['timezone'] = timezone
            if address is not ShapeBase.NOT_SET:
                _params['address'] = address
            if distance_unit is not ShapeBase.NOT_SET:
                _params['distance_unit'] = distance_unit
            if temperature_unit is not ShapeBase.NOT_SET:
                _params['temperature_unit'] = temperature_unit
            if wake_word is not ShapeBase.NOT_SET:
                _params['wake_word'] = wake_word
            if client_request_token is not ShapeBase.NOT_SET:
                _params['client_request_token'] = client_request_token
            if setup_mode_disabled is not ShapeBase.NOT_SET:
                _params['setup_mode_disabled'] = setup_mode_disabled
            if max_volume_limit is not ShapeBase.NOT_SET:
                _params['max_volume_limit'] = max_volume_limit
            if pstn_enabled is not ShapeBase.NOT_SET:
                _params['pstn_enabled'] = pstn_enabled
            _request = shapes.CreateProfileRequest(**_params)
        response = self._boto_client.create_profile(**_request.to_boto())

        return shapes.CreateProfileResponse.from_boto(response)

    def create_room(
        self,
        _request: shapes.CreateRoomRequest = None,
        *,
        room_name: str,
        description: str = ShapeBase.NOT_SET,
        profile_arn: str = ShapeBase.NOT_SET,
        provider_calendar_id: str = ShapeBase.NOT_SET,
        client_request_token: str = ShapeBase.NOT_SET,
        tags: typing.List[shapes.Tag] = ShapeBase.NOT_SET,
    ) -> shapes.CreateRoomResponse:
        """
        Creates a room with the specified details.
        """
        if _request is None:
            _params = {}
            if room_name is not ShapeBase.NOT_SET:
                _params['room_name'] = room_name
            if description is not ShapeBase.NOT_SET:
                _params['description'] = description
            if profile_arn is not ShapeBase.NOT_SET:
                _params['profile_arn'] = profile_arn
            if provider_calendar_id is not ShapeBase.NOT_SET:
                _params['provider_calendar_id'] = provider_calendar_id
            if client_request_token is not ShapeBase.NOT_SET:
                _params['client_request_token'] = client_request_token
            if tags is not ShapeBase.NOT_SET:
                _params['tags'] = tags
            _request = shapes.CreateRoomRequest(**_params)
        response = self._boto_client.create_room(**_request.to_boto())

        return shapes.CreateRoomResponse.from_boto(response)

    def create_skill_group(
        self,
        _request: shapes.CreateSkillGroupRequest = None,
        *,
        skill_group_name: str,
        description: str = ShapeBase.NOT_SET,
        client_request_token: str = ShapeBase.NOT_SET,
    ) -> shapes.CreateSkillGroupResponse:
        """
        Creates a skill group with a specified name and description.
        """
        if _request is None:
            _params = {}
            if skill_group_name is not ShapeBase.NOT_SET:
                _params['skill_group_name'] = skill_group_name
            if description is not ShapeBase.NOT_SET:
                _params['description'] = description
            if client_request_token is not ShapeBase.NOT_SET:
                _params['client_request_token'] = client_request_token
            _request = shapes.CreateSkillGroupRequest(**_params)
        response = self._boto_client.create_skill_group(**_request.to_boto())

        return shapes.CreateSkillGroupResponse.from_boto(response)

    def create_user(
        self,
        _request: shapes.CreateUserRequest = None,
        *,
        user_id: str,
        first_name: str = ShapeBase.NOT_SET,
        last_name: str = ShapeBase.NOT_SET,
        email: str = ShapeBase.NOT_SET,
        client_request_token: str = ShapeBase.NOT_SET,
        tags: typing.List[shapes.Tag] = ShapeBase.NOT_SET,
    ) -> shapes.CreateUserResponse:
        """
        Creates a user.
        """
        if _request is None:
            _params = {}
            if user_id is not ShapeBase.NOT_SET:
                _params['user_id'] = user_id
            if first_name is not ShapeBase.NOT_SET:
                _params['first_name'] = first_name
            if last_name is not ShapeBase.NOT_SET:
                _params['last_name'] = last_name
            if email is not ShapeBase.NOT_SET:
                _params['email'] = email
            if client_request_token is not ShapeBase.NOT_SET:
                _params['client_request_token'] = client_request_token
            if tags is not ShapeBase.NOT_SET:
                _params['tags'] = tags
            _request = shapes.CreateUserRequest(**_params)
        response = self._boto_client.create_user(**_request.to_boto())

        return shapes.CreateUserResponse.from_boto(response)

    def delete_address_book(
        self,
        _request: shapes.DeleteAddressBookRequest = None,
        *,
        address_book_arn: str,
    ) -> shapes.DeleteAddressBookResponse:
        """
        Deletes an address book by the address book ARN.
        """
        if _request is None:
            _params = {}
            if address_book_arn is not ShapeBase.NOT_SET:
                _params['address_book_arn'] = address_book_arn
            _request = shapes.DeleteAddressBookRequest(**_params)
        response = self._boto_client.delete_address_book(**_request.to_boto())

        return shapes.DeleteAddressBookResponse.from_boto(response)

    def delete_contact(
        self,
        _request: shapes.DeleteContactRequest = None,
        *,
        contact_arn: str,
    ) -> shapes.DeleteContactResponse:
        """
        Deletes a contact by the contact ARN.
        """
        if _request is None:
            _params = {}
            if contact_arn is not ShapeBase.NOT_SET:
                _params['contact_arn'] = contact_arn
            _request = shapes.DeleteContactRequest(**_params)
        response = self._boto_client.delete_contact(**_request.to_boto())

        return shapes.DeleteContactResponse.from_boto(response)

    def delete_profile(
        self,
        _request: shapes.DeleteProfileRequest = None,
        *,
        profile_arn: str = ShapeBase.NOT_SET,
    ) -> shapes.DeleteProfileResponse:
        """
        Deletes a room profile by the profile ARN.
        """
        if _request is None:
            _params = {}
            if profile_arn is not ShapeBase.NOT_SET:
                _params['profile_arn'] = profile_arn
            _request = shapes.DeleteProfileRequest(**_params)
        response = self._boto_client.delete_profile(**_request.to_boto())

        return shapes.DeleteProfileResponse.from_boto(response)

    def delete_room(
        self,
        _request: shapes.DeleteRoomRequest = None,
        *,
        room_arn: str = ShapeBase.NOT_SET,
    ) -> shapes.DeleteRoomResponse:
        """
        Deletes a room by the room ARN.
        """
        if _request is None:
            _params = {}
            if room_arn is not ShapeBase.NOT_SET:
                _params['room_arn'] = room_arn
            _request = shapes.DeleteRoomRequest(**_params)
        response = self._boto_client.delete_room(**_request.to_boto())

        return shapes.DeleteRoomResponse.from_boto(response)

    def delete_room_skill_parameter(
        self,
        _request: shapes.DeleteRoomSkillParameterRequest = None,
        *,
        skill_id: str,
        parameter_key: str,
        room_arn: str = ShapeBase.NOT_SET,
    ) -> shapes.DeleteRoomSkillParameterResponse:
        """
        Deletes room skill parameter details by room, skill, and parameter key ID.
        """
        if _request is None:
            _params = {}
            if skill_id is not ShapeBase.NOT_SET:
                _params['skill_id'] = skill_id
            if parameter_key is not ShapeBase.NOT_SET:
                _params['parameter_key'] = parameter_key
            if room_arn is not ShapeBase.NOT_SET:
                _params['room_arn'] = room_arn
            _request = shapes.DeleteRoomSkillParameterRequest(**_params)
        response = self._boto_client.delete_room_skill_parameter(
            **_request.to_boto()
        )

        return shapes.DeleteRoomSkillParameterResponse.from_boto(response)

    def delete_skill_group(
        self,
        _request: shapes.DeleteSkillGroupRequest = None,
        *,
        skill_group_arn: str = ShapeBase.NOT_SET,
    ) -> shapes.DeleteSkillGroupResponse:
        """
        Deletes a skill group by skill group ARN.
        """
        if _request is None:
            _params = {}
            if skill_group_arn is not ShapeBase.NOT_SET:
                _params['skill_group_arn'] = skill_group_arn
            _request = shapes.DeleteSkillGroupRequest(**_params)
        response = self._boto_client.delete_skill_group(**_request.to_boto())

        return shapes.DeleteSkillGroupResponse.from_boto(response)

    def delete_user(
        self,
        _request: shapes.DeleteUserRequest = None,
        *,
        enrollment_id: str,
        user_arn: str = ShapeBase.NOT_SET,
    ) -> shapes.DeleteUserResponse:
        """
        Deletes a specified user by user ARN and enrollment ARN.
        """
        if _request is None:
            _params = {}
            if enrollment_id is not ShapeBase.NOT_SET:
                _params['enrollment_id'] = enrollment_id
            if user_arn is not ShapeBase.NOT_SET:
                _params['user_arn'] = user_arn
            _request = shapes.DeleteUserRequest(**_params)
        response = self._boto_client.delete_user(**_request.to_boto())

        return shapes.DeleteUserResponse.from_boto(response)

    def disassociate_contact_from_address_book(
        self,
        _request: shapes.DisassociateContactFromAddressBookRequest = None,
        *,
        contact_arn: str,
        address_book_arn: str,
    ) -> shapes.DisassociateContactFromAddressBookResponse:
        """
        Disassociates a contact from a given address book.
        """
        if _request is None:
            _params = {}
            if contact_arn is not ShapeBase.NOT_SET:
                _params['contact_arn'] = contact_arn
            if address_book_arn is not ShapeBase.NOT_SET:
                _params['address_book_arn'] = address_book_arn
            _request = shapes.DisassociateContactFromAddressBookRequest(
                **_params
            )
        response = self._boto_client.disassociate_contact_from_address_book(
            **_request.to_boto()
        )

        return shapes.DisassociateContactFromAddressBookResponse.from_boto(
            response
        )

    def disassociate_device_from_room(
        self,
        _request: shapes.DisassociateDeviceFromRoomRequest = None,
        *,
        device_arn: str = ShapeBase.NOT_SET,
    ) -> shapes.DisassociateDeviceFromRoomResponse:
        """
        Disassociates a device from its current room. The device continues to be
        connected to the Wi-Fi network and is still registered to the account. The
        device settings and skills are removed from the room.
        """
        if _request is None:
            _params = {}
            if device_arn is not ShapeBase.NOT_SET:
                _params['device_arn'] = device_arn
            _request = shapes.DisassociateDeviceFromRoomRequest(**_params)
        response = self._boto_client.disassociate_device_from_room(
            **_request.to_boto()
        )

        return shapes.DisassociateDeviceFromRoomResponse.from_boto(response)

    def disassociate_skill_group_from_room(
        self,
        _request: shapes.DisassociateSkillGroupFromRoomRequest = None,
        *,
        skill_group_arn: str = ShapeBase.NOT_SET,
        room_arn: str = ShapeBase.NOT_SET,
    ) -> shapes.DisassociateSkillGroupFromRoomResponse:
        """
        Disassociates a skill group from a specified room. This disables all skills in
        the skill group on all devices in the room.
        """
        if _request is None:
            _params = {}
            if skill_group_arn is not ShapeBase.NOT_SET:
                _params['skill_group_arn'] = skill_group_arn
            if room_arn is not ShapeBase.NOT_SET:
                _params['room_arn'] = room_arn
            _request = shapes.DisassociateSkillGroupFromRoomRequest(**_params)
        response = self._boto_client.disassociate_skill_group_from_room(
            **_request.to_boto()
        )

        return shapes.DisassociateSkillGroupFromRoomResponse.from_boto(response)

    def get_address_book(
        self,
        _request: shapes.GetAddressBookRequest = None,
        *,
        address_book_arn: str,
    ) -> shapes.GetAddressBookResponse:
        """
        Gets address the book details by the address book ARN.
        """
        if _request is None:
            _params = {}
            if address_book_arn is not ShapeBase.NOT_SET:
                _params['address_book_arn'] = address_book_arn
            _request = shapes.GetAddressBookRequest(**_params)
        response = self._boto_client.get_address_book(**_request.to_boto())

        return shapes.GetAddressBookResponse.from_boto(response)

    def get_contact(
        self,
        _request: shapes.GetContactRequest = None,
        *,
        contact_arn: str,
    ) -> shapes.GetContactResponse:
        """
        Gets the contact details by the contact ARN.
        """
        if _request is None:
            _params = {}
            if contact_arn is not ShapeBase.NOT_SET:
                _params['contact_arn'] = contact_arn
            _request = shapes.GetContactRequest(**_params)
        response = self._boto_client.get_contact(**_request.to_boto())

        return shapes.GetContactResponse.from_boto(response)

    def get_device(
        self,
        _request: shapes.GetDeviceRequest = None,
        *,
        device_arn: str = ShapeBase.NOT_SET,
    ) -> shapes.GetDeviceResponse:
        """
        Gets the details of a device by device ARN.
        """
        if _request is None:
            _params = {}
            if device_arn is not ShapeBase.NOT_SET:
                _params['device_arn'] = device_arn
            _request = shapes.GetDeviceRequest(**_params)
        response = self._boto_client.get_device(**_request.to_boto())

        return shapes.GetDeviceResponse.from_boto(response)

    def get_profile(
        self,
        _request: shapes.GetProfileRequest = None,
        *,
        profile_arn: str = ShapeBase.NOT_SET,
    ) -> shapes.GetProfileResponse:
        """
        Gets the details of a room profile by profile ARN.
        """
        if _request is None:
            _params = {}
            if profile_arn is not ShapeBase.NOT_SET:
                _params['profile_arn'] = profile_arn
            _request = shapes.GetProfileRequest(**_params)
        response = self._boto_client.get_profile(**_request.to_boto())

        return shapes.GetProfileResponse.from_boto(response)

    def get_room(
        self,
        _request: shapes.GetRoomRequest = None,
        *,
        room_arn: str = ShapeBase.NOT_SET,
    ) -> shapes.GetRoomResponse:
        """
        Gets room details by room ARN.
        """
        if _request is None:
            _params = {}
            if room_arn is not ShapeBase.NOT_SET:
                _params['room_arn'] = room_arn
            _request = shapes.GetRoomRequest(**_params)
        response = self._boto_client.get_room(**_request.to_boto())

        return shapes.GetRoomResponse.from_boto(response)

    def get_room_skill_parameter(
        self,
        _request: shapes.GetRoomSkillParameterRequest = None,
        *,
        skill_id: str,
        parameter_key: str,
        room_arn: str = ShapeBase.NOT_SET,
    ) -> shapes.GetRoomSkillParameterResponse:
        """
        Gets room skill parameter details by room, skill, and parameter key ARN.
        """
        if _request is None:
            _params = {}
            if skill_id is not ShapeBase.NOT_SET:
                _params['skill_id'] = skill_id
            if parameter_key is not ShapeBase.NOT_SET:
                _params['parameter_key'] = parameter_key
            if room_arn is not ShapeBase.NOT_SET:
                _params['room_arn'] = room_arn
            _request = shapes.GetRoomSkillParameterRequest(**_params)
        response = self._boto_client.get_room_skill_parameter(
            **_request.to_boto()
        )

        return shapes.GetRoomSkillParameterResponse.from_boto(response)

    def get_skill_group(
        self,
        _request: shapes.GetSkillGroupRequest = None,
        *,
        skill_group_arn: str = ShapeBase.NOT_SET,
    ) -> shapes.GetSkillGroupResponse:
        """
        Gets skill group details by skill group ARN.
        """
        if _request is None:
            _params = {}
            if skill_group_arn is not ShapeBase.NOT_SET:
                _params['skill_group_arn'] = skill_group_arn
            _request = shapes.GetSkillGroupRequest(**_params)
        response = self._boto_client.get_skill_group(**_request.to_boto())

        return shapes.GetSkillGroupResponse.from_boto(response)

    def list_device_events(
        self,
        _request: shapes.ListDeviceEventsRequest = None,
        *,
        device_arn: str,
        event_type: typing.Union[str, shapes.DeviceEventType] = ShapeBase.
        NOT_SET,
        next_token: str = ShapeBase.NOT_SET,
        max_results: int = ShapeBase.NOT_SET,
    ) -> shapes.ListDeviceEventsResponse:
        """
        Lists the device event history, including device connection status, for up to 30
        days.
        """
        if _request is None:
            _params = {}
            if device_arn is not ShapeBase.NOT_SET:
                _params['device_arn'] = device_arn
            if event_type is not ShapeBase.NOT_SET:
                _params['event_type'] = event_type
            if next_token is not ShapeBase.NOT_SET:
                _params['next_token'] = next_token
            if max_results is not ShapeBase.NOT_SET:
                _params['max_results'] = max_results
            _request = shapes.ListDeviceEventsRequest(**_params)
        response = self._boto_client.list_device_events(**_request.to_boto())

        return shapes.ListDeviceEventsResponse.from_boto(response)

    def list_skills(
        self,
        _request: shapes.ListSkillsRequest = None,
        *,
        skill_group_arn: str = ShapeBase.NOT_SET,
        next_token: str = ShapeBase.NOT_SET,
        max_results: int = ShapeBase.NOT_SET,
    ) -> shapes.ListSkillsResponse:
        """
        Lists all enabled skills in a specific skill group.
        """
        if _request is None:
            _params = {}
            if skill_group_arn is not ShapeBase.NOT_SET:
                _params['skill_group_arn'] = skill_group_arn
            if next_token is not ShapeBase.NOT_SET:
                _params['next_token'] = next_token
            if max_results is not ShapeBase.NOT_SET:
                _params['max_results'] = max_results
            _request = shapes.ListSkillsRequest(**_params)
        paginator = self.get_paginator("list_skills").paginate(
            **_request.to_boto()
        )
        page_generator = (page for page in paginator)
        first_page = next(page_generator)
        result = shapes.ListSkillsResponse.from_boto(first_page)
        result._page_iterator = page_generator
        return result

        return shapes.ListSkillsResponse.from_boto(response)

    def list_tags(
        self,
        _request: shapes.ListTagsRequest = None,
        *,
        arn: str,
        next_token: str = ShapeBase.NOT_SET,
        max_results: int = ShapeBase.NOT_SET,
    ) -> shapes.ListTagsResponse:
        """
        Lists all tags for the specified resource.
        """
        if _request is None:
            _params = {}
            if arn is not ShapeBase.NOT_SET:
                _params['arn'] = arn
            if next_token is not ShapeBase.NOT_SET:
                _params['next_token'] = next_token
            if max_results is not ShapeBase.NOT_SET:
                _params['max_results'] = max_results
            _request = shapes.ListTagsRequest(**_params)
        paginator = self.get_paginator("list_tags").paginate(
            **_request.to_boto()
        )
        page_generator = (page for page in paginator)
        first_page = next(page_generator)
        result = shapes.ListTagsResponse.from_boto(first_page)
        result._page_iterator = page_generator
        return result

        return shapes.ListTagsResponse.from_boto(response)

    def put_room_skill_parameter(
        self,
        _request: shapes.PutRoomSkillParameterRequest = None,
        *,
        skill_id: str,
        room_skill_parameter: shapes.RoomSkillParameter,
        room_arn: str = ShapeBase.NOT_SET,
    ) -> shapes.PutRoomSkillParameterResponse:
        """
        Updates room skill parameter details by room, skill, and parameter key ID. Not
        all skills have a room skill parameter.
        """
        if _request is None:
            _params = {}
            if skill_id is not ShapeBase.NOT_SET:
                _params['skill_id'] = skill_id
            if room_skill_parameter is not ShapeBase.NOT_SET:
                _params['room_skill_parameter'] = room_skill_parameter
            if room_arn is not ShapeBase.NOT_SET:
                _params['room_arn'] = room_arn
            _request = shapes.PutRoomSkillParameterRequest(**_params)
        response = self._boto_client.put_room_skill_parameter(
            **_request.to_boto()
        )

        return shapes.PutRoomSkillParameterResponse.from_boto(response)

    def resolve_room(
        self,
        _request: shapes.ResolveRoomRequest = None,
        *,
        user_id: str,
        skill_id: str,
    ) -> shapes.ResolveRoomResponse:
        """
        Determines the details for the room from which a skill request was invoked. This
        operation is used by skill developers.
        """
        if _request is None:
            _params = {}
            if user_id is not ShapeBase.NOT_SET:
                _params['user_id'] = user_id
            if skill_id is not ShapeBase.NOT_SET:
                _params['skill_id'] = skill_id
            _request = shapes.ResolveRoomRequest(**_params)
        response = self._boto_client.resolve_room(**_request.to_boto())

        return shapes.ResolveRoomResponse.from_boto(response)

    def revoke_invitation(
        self,
        _request: shapes.RevokeInvitationRequest = None,
        *,
        user_arn: str = ShapeBase.NOT_SET,
        enrollment_id: str = ShapeBase.NOT_SET,
    ) -> shapes.RevokeInvitationResponse:
        """
        Revokes an invitation and invalidates the enrollment URL.
        """
        if _request is None:
            _params = {}
            if user_arn is not ShapeBase.NOT_SET:
                _params['user_arn'] = user_arn
            if enrollment_id is not ShapeBase.NOT_SET:
                _params['enrollment_id'] = enrollment_id
            _request = shapes.RevokeInvitationRequest(**_params)
        response = self._boto_client.revoke_invitation(**_request.to_boto())

        return shapes.RevokeInvitationResponse.from_boto(response)

    def search_address_books(
        self,
        _request: shapes.SearchAddressBooksRequest = None,
        *,
        filters: typing.List[shapes.Filter] = ShapeBase.NOT_SET,
        sort_criteria: typing.List[shapes.Sort] = ShapeBase.NOT_SET,
        next_token: str = ShapeBase.NOT_SET,
        max_results: int = ShapeBase.NOT_SET,
    ) -> shapes.SearchAddressBooksResponse:
        """
        Searches address books and lists the ones that meet a set of filter and sort
        criteria.
        """
        if _request is None:
            _params = {}
            if filters is not ShapeBase.NOT_SET:
                _params['filters'] = filters
            if sort_criteria is not ShapeBase.NOT_SET:
                _params['sort_criteria'] = sort_criteria
            if next_token is not ShapeBase.NOT_SET:
                _params['next_token'] = next_token
            if max_results is not ShapeBase.NOT_SET:
                _params['max_results'] = max_results
            _request = shapes.SearchAddressBooksRequest(**_params)
        response = self._boto_client.search_address_books(**_request.to_boto())

        return shapes.SearchAddressBooksResponse.from_boto(response)

    def search_contacts(
        self,
        _request: shapes.SearchContactsRequest = None,
        *,
        filters: typing.List[shapes.Filter] = ShapeBase.NOT_SET,
        sort_criteria: typing.List[shapes.Sort] = ShapeBase.NOT_SET,
        next_token: str = ShapeBase.NOT_SET,
        max_results: int = ShapeBase.NOT_SET,
    ) -> shapes.SearchContactsResponse:
        """
        Searches contacts and lists the ones that meet a set of filter and sort
        criteria.
        """
        if _request is None:
            _params = {}
            if filters is not ShapeBase.NOT_SET:
                _params['filters'] = filters
            if sort_criteria is not ShapeBase.NOT_SET:
                _params['sort_criteria'] = sort_criteria
            if next_token is not ShapeBase.NOT_SET:
                _params['next_token'] = next_token
            if max_results is not ShapeBase.NOT_SET:
                _params['max_results'] = max_results
            _request = shapes.SearchContactsRequest(**_params)
        response = self._boto_client.search_contacts(**_request.to_boto())

        return shapes.SearchContactsResponse.from_boto(response)

    def search_devices(
        self,
        _request: shapes.SearchDevicesRequest = None,
        *,
        next_token: str = ShapeBase.NOT_SET,
        max_results: int = ShapeBase.NOT_SET,
        filters: typing.List[shapes.Filter] = ShapeBase.NOT_SET,
        sort_criteria: typing.List[shapes.Sort] = ShapeBase.NOT_SET,
    ) -> shapes.SearchDevicesResponse:
        """
        Searches devices and lists the ones that meet a set of filter criteria.
        """
        if _request is None:
            _params = {}
            if next_token is not ShapeBase.NOT_SET:
                _params['next_token'] = next_token
            if max_results is not ShapeBase.NOT_SET:
                _params['max_results'] = max_results
            if filters is not ShapeBase.NOT_SET:
                _params['filters'] = filters
            if sort_criteria is not ShapeBase.NOT_SET:
                _params['sort_criteria'] = sort_criteria
            _request = shapes.SearchDevicesRequest(**_params)
        paginator = self.get_paginator("search_devices").paginate(
            **_request.to_boto()
        )
        page_generator = (page for page in paginator)
        first_page = next(page_generator)
        result = shapes.SearchDevicesResponse.from_boto(first_page)
        result._page_iterator = page_generator
        return result

        return shapes.SearchDevicesResponse.from_boto(response)

    def search_profiles(
        self,
        _request: shapes.SearchProfilesRequest = None,
        *,
        next_token: str = ShapeBase.NOT_SET,
        max_results: int = ShapeBase.NOT_SET,
        filters: typing.List[shapes.Filter] = ShapeBase.NOT_SET,
        sort_criteria: typing.List[shapes.Sort] = ShapeBase.NOT_SET,
    ) -> shapes.SearchProfilesResponse:
        """
        Searches room profiles and lists the ones that meet a set of filter criteria.
        """
        if _request is None:
            _params = {}
            if next_token is not ShapeBase.NOT_SET:
                _params['next_token'] = next_token
            if max_results is not ShapeBase.NOT_SET:
                _params['max_results'] = max_results
            if filters is not ShapeBase.NOT_SET:
                _params['filters'] = filters
            if sort_criteria is not ShapeBase.NOT_SET:
                _params['sort_criteria'] = sort_criteria
            _request = shapes.SearchProfilesRequest(**_params)
        paginator = self.get_paginator("search_profiles").paginate(
            **_request.to_boto()
        )
        page_generator = (page for page in paginator)
        first_page = next(page_generator)
        result = shapes.SearchProfilesResponse.from_boto(first_page)
        result._page_iterator = page_generator
        return result

        return shapes.SearchProfilesResponse.from_boto(response)

    def search_rooms(
        self,
        _request: shapes.SearchRoomsRequest = None,
        *,
        next_token: str = ShapeBase.NOT_SET,
        max_results: int = ShapeBase.NOT_SET,
        filters: typing.List[shapes.Filter] = ShapeBase.NOT_SET,
        sort_criteria: typing.List[shapes.Sort] = ShapeBase.NOT_SET,
    ) -> shapes.SearchRoomsResponse:
        """
        Searches rooms and lists the ones that meet a set of filter and sort criteria.
        """
        if _request is None:
            _params = {}
            if next_token is not ShapeBase.NOT_SET:
                _params['next_token'] = next_token
            if max_results is not ShapeBase.NOT_SET:
                _params['max_results'] = max_results
            if filters is not ShapeBase.NOT_SET:
                _params['filters'] = filters
            if sort_criteria is not ShapeBase.NOT_SET:
                _params['sort_criteria'] = sort_criteria
            _request = shapes.SearchRoomsRequest(**_params)
        paginator = self.get_paginator("search_rooms").paginate(
            **_request.to_boto()
        )
        page_generator = (page for page in paginator)
        first_page = next(page_generator)
        result = shapes.SearchRoomsResponse.from_boto(first_page)
        result._page_iterator = page_generator
        return result

        return shapes.SearchRoomsResponse.from_boto(response)

    def search_skill_groups(
        self,
        _request: shapes.SearchSkillGroupsRequest = None,
        *,
        next_token: str = ShapeBase.NOT_SET,
        max_results: int = ShapeBase.NOT_SET,
        filters: typing.List[shapes.Filter] = ShapeBase.NOT_SET,
        sort_criteria: typing.List[shapes.Sort] = ShapeBase.NOT_SET,
    ) -> shapes.SearchSkillGroupsResponse:
        """
        Searches skill groups and lists the ones that meet a set of filter and sort
        criteria.
        """
        if _request is None:
            _params = {}
            if next_token is not ShapeBase.NOT_SET:
                _params['next_token'] = next_token
            if max_results is not ShapeBase.NOT_SET:
                _params['max_results'] = max_results
            if filters is not ShapeBase.NOT_SET:
                _params['filters'] = filters
            if sort_criteria is not ShapeBase.NOT_SET:
                _params['sort_criteria'] = sort_criteria
            _request = shapes.SearchSkillGroupsRequest(**_params)
        paginator = self.get_paginator("search_skill_groups").paginate(
            **_request.to_boto()
        )
        page_generator = (page for page in paginator)
        first_page = next(page_generator)
        result = shapes.SearchSkillGroupsResponse.from_boto(first_page)
        result._page_iterator = page_generator
        return result

        return shapes.SearchSkillGroupsResponse.from_boto(response)

    def search_users(
        self,
        _request: shapes.SearchUsersRequest = None,
        *,
        next_token: str = ShapeBase.NOT_SET,
        max_results: int = ShapeBase.NOT_SET,
        filters: typing.List[shapes.Filter] = ShapeBase.NOT_SET,
        sort_criteria: typing.List[shapes.Sort] = ShapeBase.NOT_SET,
    ) -> shapes.SearchUsersResponse:
        """
        Searches users and lists the ones that meet a set of filter and sort criteria.
        """
        if _request is None:
            _params = {}
            if next_token is not ShapeBase.NOT_SET:
                _params['next_token'] = next_token
            if max_results is not ShapeBase.NOT_SET:
                _params['max_results'] = max_results
            if filters is not ShapeBase.NOT_SET:
                _params['filters'] = filters
            if sort_criteria is not ShapeBase.NOT_SET:
                _params['sort_criteria'] = sort_criteria
            _request = shapes.SearchUsersRequest(**_params)
        paginator = self.get_paginator("search_users").paginate(
            **_request.to_boto()
        )
        page_generator = (page for page in paginator)
        first_page = next(page_generator)
        result = shapes.SearchUsersResponse.from_boto(first_page)
        result._page_iterator = page_generator
        return result

        return shapes.SearchUsersResponse.from_boto(response)

    def send_invitation(
        self,
        _request: shapes.SendInvitationRequest = None,
        *,
        user_arn: str = ShapeBase.NOT_SET,
    ) -> shapes.SendInvitationResponse:
        """
        Sends an enrollment invitation email with a URL to a user. The URL is valid for
        72 hours or until you call this operation again, whichever comes first.
        """
        if _request is None:
            _params = {}
            if user_arn is not ShapeBase.NOT_SET:
                _params['user_arn'] = user_arn
            _request = shapes.SendInvitationRequest(**_params)
        response = self._boto_client.send_invitation(**_request.to_boto())

        return shapes.SendInvitationResponse.from_boto(response)

    def start_device_sync(
        self,
        _request: shapes.StartDeviceSyncRequest = None,
        *,
        features: typing.List[typing.Union[str, shapes.Feature]],
        room_arn: str = ShapeBase.NOT_SET,
        device_arn: str = ShapeBase.NOT_SET,
    ) -> shapes.StartDeviceSyncResponse:
        """
        Resets a device and its account to the known default settings, by clearing all
        information and settings set by previous users.
        """
        if _request is None:
            _params = {}
            if features is not ShapeBase.NOT_SET:
                _params['features'] = features
            if room_arn is not ShapeBase.NOT_SET:
                _params['room_arn'] = room_arn
            if device_arn is not ShapeBase.NOT_SET:
                _params['device_arn'] = device_arn
            _request = shapes.StartDeviceSyncRequest(**_params)
        response = self._boto_client.start_device_sync(**_request.to_boto())

        return shapes.StartDeviceSyncResponse.from_boto(response)

    def tag_resource(
        self,
        _request: shapes.TagResourceRequest = None,
        *,
        arn: str,
        tags: typing.List[shapes.Tag],
    ) -> shapes.TagResourceResponse:
        """
        Adds metadata tags to a specified resource.
        """
        if _request is None:
            _params = {}
            if arn is not ShapeBase.NOT_SET:
                _params['arn'] = arn
            if tags is not ShapeBase.NOT_SET:
                _params['tags'] = tags
            _request = shapes.TagResourceRequest(**_params)
        response = self._boto_client.tag_resource(**_request.to_boto())

        return shapes.TagResourceResponse.from_boto(response)

    def untag_resource(
        self,
        _request: shapes.UntagResourceRequest = None,
        *,
        arn: str,
        tag_keys: typing.List[str],
    ) -> shapes.UntagResourceResponse:
        """
        Removes metadata tags from a specified resource.
        """
        if _request is None:
            _params = {}
            if arn is not ShapeBase.NOT_SET:
                _params['arn'] = arn
            if tag_keys is not ShapeBase.NOT_SET:
                _params['tag_keys'] = tag_keys
            _request = shapes.UntagResourceRequest(**_params)
        response = self._boto_client.untag_resource(**_request.to_boto())

        return shapes.UntagResourceResponse.from_boto(response)

    def update_address_book(
        self,
        _request: shapes.UpdateAddressBookRequest = None,
        *,
        address_book_arn: str,
        name: str = ShapeBase.NOT_SET,
        description: str = ShapeBase.NOT_SET,
    ) -> shapes.UpdateAddressBookResponse:
        """
        Updates address book details by the address book ARN.
        """
        if _request is None:
            _params = {}
            if address_book_arn is not ShapeBase.NOT_SET:
                _params['address_book_arn'] = address_book_arn
            if name is not ShapeBase.NOT_SET:
                _params['name'] = name
            if description is not ShapeBase.NOT_SET:
                _params['description'] = description
            _request = shapes.UpdateAddressBookRequest(**_params)
        response = self._boto_client.update_address_book(**_request.to_boto())

        return shapes.UpdateAddressBookResponse.from_boto(response)

    def update_contact(
        self,
        _request: shapes.UpdateContactRequest = None,
        *,
        contact_arn: str,
        display_name: str = ShapeBase.NOT_SET,
        first_name: str = ShapeBase.NOT_SET,
        last_name: str = ShapeBase.NOT_SET,
        phone_number: str = ShapeBase.NOT_SET,
    ) -> shapes.UpdateContactResponse:
        """
        Updates the contact details by the contact ARN.
        """
        if _request is None:
            _params = {}
            if contact_arn is not ShapeBase.NOT_SET:
                _params['contact_arn'] = contact_arn
            if display_name is not ShapeBase.NOT_SET:
                _params['display_name'] = display_name
            if first_name is not ShapeBase.NOT_SET:
                _params['first_name'] = first_name
            if last_name is not ShapeBase.NOT_SET:
                _params['last_name'] = last_name
            if phone_number is not ShapeBase.NOT_SET:
                _params['phone_number'] = phone_number
            _request = shapes.UpdateContactRequest(**_params)
        response = self._boto_client.update_contact(**_request.to_boto())

        return shapes.UpdateContactResponse.from_boto(response)

    def update_device(
        self,
        _request: shapes.UpdateDeviceRequest = None,
        *,
        device_arn: str = ShapeBase.NOT_SET,
        device_name: str = ShapeBase.NOT_SET,
    ) -> shapes.UpdateDeviceResponse:
        """
        Updates the device name by device ARN.
        """
        if _request is None:
            _params = {}
            if device_arn is not ShapeBase.NOT_SET:
                _params['device_arn'] = device_arn
            if device_name is not ShapeBase.NOT_SET:
                _params['device_name'] = device_name
            _request = shapes.UpdateDeviceRequest(**_params)
        response = self._boto_client.update_device(**_request.to_boto())

        return shapes.UpdateDeviceResponse.from_boto(response)

    def update_profile(
        self,
        _request: shapes.UpdateProfileRequest = None,
        *,
        profile_arn: str = ShapeBase.NOT_SET,
        profile_name: str = ShapeBase.NOT_SET,
        timezone: str = ShapeBase.NOT_SET,
        address: str = ShapeBase.NOT_SET,
        distance_unit: typing.Union[str, shapes.
                                    DistanceUnit] = ShapeBase.NOT_SET,
        temperature_unit: typing.Union[str, shapes.TemperatureUnit] = ShapeBase.
        NOT_SET,
        wake_word: typing.Union[str, shapes.WakeWord] = ShapeBase.NOT_SET,
        setup_mode_disabled: bool = ShapeBase.NOT_SET,
        max_volume_limit: int = ShapeBase.NOT_SET,
        pstn_enabled: bool = ShapeBase.NOT_SET,
    ) -> shapes.UpdateProfileResponse:
        """
        Updates an existing room profile by room profile ARN.
        """
        if _request is None:
            _params = {}
            if profile_arn is not ShapeBase.NOT_SET:
                _params['profile_arn'] = profile_arn
            if profile_name is not ShapeBase.NOT_SET:
                _params['profile_name'] = profile_name
            if timezone is not ShapeBase.NOT_SET:
                _params['timezone'] = timezone
            if address is not ShapeBase.NOT_SET:
                _params['address'] = address
            if distance_unit is not ShapeBase.NOT_SET:
                _params['distance_unit'] = distance_unit
            if temperature_unit is not ShapeBase.NOT_SET:
                _params['temperature_unit'] = temperature_unit
            if wake_word is not ShapeBase.NOT_SET:
                _params['wake_word'] = wake_word
            if setup_mode_disabled is not ShapeBase.NOT_SET:
                _params['setup_mode_disabled'] = setup_mode_disabled
            if max_volume_limit is not ShapeBase.NOT_SET:
                _params['max_volume_limit'] = max_volume_limit
            if pstn_enabled is not ShapeBase.NOT_SET:
                _params['pstn_enabled'] = pstn_enabled
            _request = shapes.UpdateProfileRequest(**_params)
        response = self._boto_client.update_profile(**_request.to_boto())

        return shapes.UpdateProfileResponse.from_boto(response)

    def update_room(
        self,
        _request: shapes.UpdateRoomRequest = None,
        *,
        room_arn: str = ShapeBase.NOT_SET,
        room_name: str = ShapeBase.NOT_SET,
        description: str = ShapeBase.NOT_SET,
        provider_calendar_id: str = ShapeBase.NOT_SET,
        profile_arn: str = ShapeBase.NOT_SET,
    ) -> shapes.UpdateRoomResponse:
        """
        Updates room details by room ARN.
        """
        if _request is None:
            _params = {}
            if room_arn is not ShapeBase.NOT_SET:
                _params['room_arn'] = room_arn
            if room_name is not ShapeBase.NOT_SET:
                _params['room_name'] = room_name
            if description is not ShapeBase.NOT_SET:
                _params['description'] = description
            if provider_calendar_id is not ShapeBase.NOT_SET:
                _params['provider_calendar_id'] = provider_calendar_id
            if profile_arn is not ShapeBase.NOT_SET:
                _params['profile_arn'] = profile_arn
            _request = shapes.UpdateRoomRequest(**_params)
        response = self._boto_client.update_room(**_request.to_boto())

        return shapes.UpdateRoomResponse.from_boto(response)

    def update_skill_group(
        self,
        _request: shapes.UpdateSkillGroupRequest = None,
        *,
        skill_group_arn: str = ShapeBase.NOT_SET,
        skill_group_name: str = ShapeBase.NOT_SET,
        description: str = ShapeBase.NOT_SET,
    ) -> shapes.UpdateSkillGroupResponse:
        """
        Updates skill group details by skill group ARN.
        """
        if _request is None:
            _params = {}
            if skill_group_arn is not ShapeBase.NOT_SET:
                _params['skill_group_arn'] = skill_group_arn
            if skill_group_name is not ShapeBase.NOT_SET:
                _params['skill_group_name'] = skill_group_name
            if description is not ShapeBase.NOT_SET:
                _params['description'] = description
            _request = shapes.UpdateSkillGroupRequest(**_params)
        response = self._boto_client.update_skill_group(**_request.to_boto())

        return shapes.UpdateSkillGroupResponse.from_boto(response)
