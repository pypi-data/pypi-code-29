import datetime
import typing
import boto3
from autoboto import ClientBase, ShapeBase, OutputShapeBase
from . import shapes


class Client(ClientBase):
    def __init__(self, *args, **kwargs):
        super().__init__("connect", *args, **kwargs)

    def create_user(
        self,
        _request: shapes.CreateUserRequest = None,
        *,
        username: str,
        phone_config: shapes.UserPhoneConfig,
        security_profile_ids: typing.List[str],
        routing_profile_id: str,
        instance_id: str,
        password: str = ShapeBase.NOT_SET,
        identity_info: shapes.UserIdentityInfo = ShapeBase.NOT_SET,
        directory_user_id: str = ShapeBase.NOT_SET,
        hierarchy_group_id: str = ShapeBase.NOT_SET,
    ) -> shapes.CreateUserResponse:
        """
        Creates a new user account in your Amazon Connect instance.
        """
        if _request is None:
            _params = {}
            if username is not ShapeBase.NOT_SET:
                _params['username'] = username
            if phone_config is not ShapeBase.NOT_SET:
                _params['phone_config'] = phone_config
            if security_profile_ids is not ShapeBase.NOT_SET:
                _params['security_profile_ids'] = security_profile_ids
            if routing_profile_id is not ShapeBase.NOT_SET:
                _params['routing_profile_id'] = routing_profile_id
            if instance_id is not ShapeBase.NOT_SET:
                _params['instance_id'] = instance_id
            if password is not ShapeBase.NOT_SET:
                _params['password'] = password
            if identity_info is not ShapeBase.NOT_SET:
                _params['identity_info'] = identity_info
            if directory_user_id is not ShapeBase.NOT_SET:
                _params['directory_user_id'] = directory_user_id
            if hierarchy_group_id is not ShapeBase.NOT_SET:
                _params['hierarchy_group_id'] = hierarchy_group_id
            _request = shapes.CreateUserRequest(**_params)
        response = self._boto_client.create_user(**_request.to_boto())

        return shapes.CreateUserResponse.from_boto(response)

    def delete_user(
        self,
        _request: shapes.DeleteUserRequest = None,
        *,
        instance_id: str,
        user_id: str,
    ) -> None:
        """
        Deletes a user account from Amazon Connect.
        """
        if _request is None:
            _params = {}
            if instance_id is not ShapeBase.NOT_SET:
                _params['instance_id'] = instance_id
            if user_id is not ShapeBase.NOT_SET:
                _params['user_id'] = user_id
            _request = shapes.DeleteUserRequest(**_params)
        response = self._boto_client.delete_user(**_request.to_boto())

    def describe_user(
        self,
        _request: shapes.DescribeUserRequest = None,
        *,
        user_id: str,
        instance_id: str,
    ) -> shapes.DescribeUserResponse:
        """
        Returns a `User` object that contains information about the user account
        specified by the `UserId`.
        """
        if _request is None:
            _params = {}
            if user_id is not ShapeBase.NOT_SET:
                _params['user_id'] = user_id
            if instance_id is not ShapeBase.NOT_SET:
                _params['instance_id'] = instance_id
            _request = shapes.DescribeUserRequest(**_params)
        response = self._boto_client.describe_user(**_request.to_boto())

        return shapes.DescribeUserResponse.from_boto(response)

    def describe_user_hierarchy_group(
        self,
        _request: shapes.DescribeUserHierarchyGroupRequest = None,
        *,
        hierarchy_group_id: str,
        instance_id: str,
    ) -> shapes.DescribeUserHierarchyGroupResponse:
        """
        Returns a `HierarchyGroup` object that includes information about a hierarchy
        group in your instance.
        """
        if _request is None:
            _params = {}
            if hierarchy_group_id is not ShapeBase.NOT_SET:
                _params['hierarchy_group_id'] = hierarchy_group_id
            if instance_id is not ShapeBase.NOT_SET:
                _params['instance_id'] = instance_id
            _request = shapes.DescribeUserHierarchyGroupRequest(**_params)
        response = self._boto_client.describe_user_hierarchy_group(
            **_request.to_boto()
        )

        return shapes.DescribeUserHierarchyGroupResponse.from_boto(response)

    def describe_user_hierarchy_structure(
        self,
        _request: shapes.DescribeUserHierarchyStructureRequest = None,
        *,
        instance_id: str,
    ) -> shapes.DescribeUserHierarchyStructureResponse:
        """
        Returns a `HiearchyGroupStructure` object, which contains data about the levels
        in the agent hierarchy.
        """
        if _request is None:
            _params = {}
            if instance_id is not ShapeBase.NOT_SET:
                _params['instance_id'] = instance_id
            _request = shapes.DescribeUserHierarchyStructureRequest(**_params)
        response = self._boto_client.describe_user_hierarchy_structure(
            **_request.to_boto()
        )

        return shapes.DescribeUserHierarchyStructureResponse.from_boto(response)

    def get_federation_token(
        self,
        _request: shapes.GetFederationTokenRequest = None,
        *,
        instance_id: str,
    ) -> shapes.GetFederationTokenResponse:
        """
        Retrieves a token for federation.
        """
        if _request is None:
            _params = {}
            if instance_id is not ShapeBase.NOT_SET:
                _params['instance_id'] = instance_id
            _request = shapes.GetFederationTokenRequest(**_params)
        response = self._boto_client.get_federation_token(**_request.to_boto())

        return shapes.GetFederationTokenResponse.from_boto(response)

    def list_routing_profiles(
        self,
        _request: shapes.ListRoutingProfilesRequest = None,
        *,
        instance_id: str,
        next_token: str = ShapeBase.NOT_SET,
        max_results: int = ShapeBase.NOT_SET,
    ) -> shapes.ListRoutingProfilesResponse:
        """
        Returns an array of `RoutingProfileSummary` objects that includes information
        about the routing profiles in your instance.
        """
        if _request is None:
            _params = {}
            if instance_id is not ShapeBase.NOT_SET:
                _params['instance_id'] = instance_id
            if next_token is not ShapeBase.NOT_SET:
                _params['next_token'] = next_token
            if max_results is not ShapeBase.NOT_SET:
                _params['max_results'] = max_results
            _request = shapes.ListRoutingProfilesRequest(**_params)
        response = self._boto_client.list_routing_profiles(**_request.to_boto())

        return shapes.ListRoutingProfilesResponse.from_boto(response)

    def list_security_profiles(
        self,
        _request: shapes.ListSecurityProfilesRequest = None,
        *,
        instance_id: str,
        next_token: str = ShapeBase.NOT_SET,
        max_results: int = ShapeBase.NOT_SET,
    ) -> shapes.ListSecurityProfilesResponse:
        """
        Returns an array of SecurityProfileSummary objects that contain information
        about the security profiles in your instance, including the ARN, Id, and Name of
        the security profile.
        """
        if _request is None:
            _params = {}
            if instance_id is not ShapeBase.NOT_SET:
                _params['instance_id'] = instance_id
            if next_token is not ShapeBase.NOT_SET:
                _params['next_token'] = next_token
            if max_results is not ShapeBase.NOT_SET:
                _params['max_results'] = max_results
            _request = shapes.ListSecurityProfilesRequest(**_params)
        response = self._boto_client.list_security_profiles(
            **_request.to_boto()
        )

        return shapes.ListSecurityProfilesResponse.from_boto(response)

    def list_user_hierarchy_groups(
        self,
        _request: shapes.ListUserHierarchyGroupsRequest = None,
        *,
        instance_id: str,
        next_token: str = ShapeBase.NOT_SET,
        max_results: int = ShapeBase.NOT_SET,
    ) -> shapes.ListUserHierarchyGroupsResponse:
        """
        Returns a `UserHierarchyGroupSummaryList`, which is an array of
        `HierarchyGroupSummary` objects that contain information about the hierarchy
        groups in your instance.
        """
        if _request is None:
            _params = {}
            if instance_id is not ShapeBase.NOT_SET:
                _params['instance_id'] = instance_id
            if next_token is not ShapeBase.NOT_SET:
                _params['next_token'] = next_token
            if max_results is not ShapeBase.NOT_SET:
                _params['max_results'] = max_results
            _request = shapes.ListUserHierarchyGroupsRequest(**_params)
        response = self._boto_client.list_user_hierarchy_groups(
            **_request.to_boto()
        )

        return shapes.ListUserHierarchyGroupsResponse.from_boto(response)

    def list_users(
        self,
        _request: shapes.ListUsersRequest = None,
        *,
        instance_id: str,
        next_token: str = ShapeBase.NOT_SET,
        max_results: int = ShapeBase.NOT_SET,
    ) -> shapes.ListUsersResponse:
        """
        Returns a `UserSummaryList`, which is an array of `UserSummary` objects.
        """
        if _request is None:
            _params = {}
            if instance_id is not ShapeBase.NOT_SET:
                _params['instance_id'] = instance_id
            if next_token is not ShapeBase.NOT_SET:
                _params['next_token'] = next_token
            if max_results is not ShapeBase.NOT_SET:
                _params['max_results'] = max_results
            _request = shapes.ListUsersRequest(**_params)
        response = self._boto_client.list_users(**_request.to_boto())

        return shapes.ListUsersResponse.from_boto(response)

    def start_outbound_voice_contact(
        self,
        _request: shapes.StartOutboundVoiceContactRequest = None,
        *,
        destination_phone_number: str,
        contact_flow_id: str,
        instance_id: str,
        client_token: str = ShapeBase.NOT_SET,
        source_phone_number: str = ShapeBase.NOT_SET,
        queue_id: str = ShapeBase.NOT_SET,
        attributes: typing.Dict[str, str] = ShapeBase.NOT_SET,
    ) -> shapes.StartOutboundVoiceContactResponse:
        """
        The `StartOutboundVoiceContact` operation initiates a contact flow to place an
        outbound call to a customer.

        There is a throttling limit placed on usage of the API that includes a RateLimit
        of 2 per second, and a BurstLimit of 5 per second.

        If you are using an IAM account, it must have permission to the
        `connect:StartOutboundVoiceContact` action.
        """
        if _request is None:
            _params = {}
            if destination_phone_number is not ShapeBase.NOT_SET:
                _params['destination_phone_number'] = destination_phone_number
            if contact_flow_id is not ShapeBase.NOT_SET:
                _params['contact_flow_id'] = contact_flow_id
            if instance_id is not ShapeBase.NOT_SET:
                _params['instance_id'] = instance_id
            if client_token is not ShapeBase.NOT_SET:
                _params['client_token'] = client_token
            if source_phone_number is not ShapeBase.NOT_SET:
                _params['source_phone_number'] = source_phone_number
            if queue_id is not ShapeBase.NOT_SET:
                _params['queue_id'] = queue_id
            if attributes is not ShapeBase.NOT_SET:
                _params['attributes'] = attributes
            _request = shapes.StartOutboundVoiceContactRequest(**_params)
        response = self._boto_client.start_outbound_voice_contact(
            **_request.to_boto()
        )

        return shapes.StartOutboundVoiceContactResponse.from_boto(response)

    def stop_contact(
        self,
        _request: shapes.StopContactRequest = None,
        *,
        contact_id: str,
        instance_id: str,
    ) -> shapes.StopContactResponse:
        """
        Ends the contact initiated by the `StartOutboundVoiceContact` operation.

        If you are using an IAM account, it must have permission to the
        `connect:StopContact` action.
        """
        if _request is None:
            _params = {}
            if contact_id is not ShapeBase.NOT_SET:
                _params['contact_id'] = contact_id
            if instance_id is not ShapeBase.NOT_SET:
                _params['instance_id'] = instance_id
            _request = shapes.StopContactRequest(**_params)
        response = self._boto_client.stop_contact(**_request.to_boto())

        return shapes.StopContactResponse.from_boto(response)

    def update_contact_attributes(
        self,
        _request: shapes.UpdateContactAttributesRequest = None,
        *,
        initial_contact_id: str,
        instance_id: str,
        attributes: typing.Dict[str, str],
    ) -> shapes.UpdateContactAttributesResponse:
        """
        The `UpdateContactAttributes` operation lets you programmatically create new or
        update existing contact attributes associated with a contact. You can use the
        operation to add or update attributes for both ongoing and completed contacts.
        For example, you can update the customer's name or the reason the customer
        called while the call is active, or add notes about steps that the agent took
        during the call that are displayed to the next agent that takes the call. You
        can also use the `UpdateContactAttributes` operation to update attributes for a
        contact using data from your CRM application and save the data with the contact
        in Amazon Connect. You could also flag calls for additional analysis, or flag
        abusive callers.

        Contact attributes are available in Amazon Connect for 24 months, and are then
        deleted.
        """
        if _request is None:
            _params = {}
            if initial_contact_id is not ShapeBase.NOT_SET:
                _params['initial_contact_id'] = initial_contact_id
            if instance_id is not ShapeBase.NOT_SET:
                _params['instance_id'] = instance_id
            if attributes is not ShapeBase.NOT_SET:
                _params['attributes'] = attributes
            _request = shapes.UpdateContactAttributesRequest(**_params)
        response = self._boto_client.update_contact_attributes(
            **_request.to_boto()
        )

        return shapes.UpdateContactAttributesResponse.from_boto(response)

    def update_user_hierarchy(
        self,
        _request: shapes.UpdateUserHierarchyRequest = None,
        *,
        user_id: str,
        instance_id: str,
        hierarchy_group_id: str = ShapeBase.NOT_SET,
    ) -> None:
        """
        Assigns the specified hierarchy group to the user.
        """
        if _request is None:
            _params = {}
            if user_id is not ShapeBase.NOT_SET:
                _params['user_id'] = user_id
            if instance_id is not ShapeBase.NOT_SET:
                _params['instance_id'] = instance_id
            if hierarchy_group_id is not ShapeBase.NOT_SET:
                _params['hierarchy_group_id'] = hierarchy_group_id
            _request = shapes.UpdateUserHierarchyRequest(**_params)
        response = self._boto_client.update_user_hierarchy(**_request.to_boto())

    def update_user_identity_info(
        self,
        _request: shapes.UpdateUserIdentityInfoRequest = None,
        *,
        identity_info: shapes.UserIdentityInfo,
        user_id: str,
        instance_id: str,
    ) -> None:
        """
        Updates the identity information for the specified user in a `UserIdentityInfo`
        object, including email, first name, and last name.
        """
        if _request is None:
            _params = {}
            if identity_info is not ShapeBase.NOT_SET:
                _params['identity_info'] = identity_info
            if user_id is not ShapeBase.NOT_SET:
                _params['user_id'] = user_id
            if instance_id is not ShapeBase.NOT_SET:
                _params['instance_id'] = instance_id
            _request = shapes.UpdateUserIdentityInfoRequest(**_params)
        response = self._boto_client.update_user_identity_info(
            **_request.to_boto()
        )

    def update_user_phone_config(
        self,
        _request: shapes.UpdateUserPhoneConfigRequest = None,
        *,
        phone_config: shapes.UserPhoneConfig,
        user_id: str,
        instance_id: str,
    ) -> None:
        """
        Updates the phone configuration settings in the `UserPhoneConfig` object for the
        specified user.
        """
        if _request is None:
            _params = {}
            if phone_config is not ShapeBase.NOT_SET:
                _params['phone_config'] = phone_config
            if user_id is not ShapeBase.NOT_SET:
                _params['user_id'] = user_id
            if instance_id is not ShapeBase.NOT_SET:
                _params['instance_id'] = instance_id
            _request = shapes.UpdateUserPhoneConfigRequest(**_params)
        response = self._boto_client.update_user_phone_config(
            **_request.to_boto()
        )

    def update_user_routing_profile(
        self,
        _request: shapes.UpdateUserRoutingProfileRequest = None,
        *,
        routing_profile_id: str,
        user_id: str,
        instance_id: str,
    ) -> None:
        """
        Assigns the specified routing profile to a user.
        """
        if _request is None:
            _params = {}
            if routing_profile_id is not ShapeBase.NOT_SET:
                _params['routing_profile_id'] = routing_profile_id
            if user_id is not ShapeBase.NOT_SET:
                _params['user_id'] = user_id
            if instance_id is not ShapeBase.NOT_SET:
                _params['instance_id'] = instance_id
            _request = shapes.UpdateUserRoutingProfileRequest(**_params)
        response = self._boto_client.update_user_routing_profile(
            **_request.to_boto()
        )

    def update_user_security_profiles(
        self,
        _request: shapes.UpdateUserSecurityProfilesRequest = None,
        *,
        security_profile_ids: typing.List[str],
        user_id: str,
        instance_id: str,
    ) -> None:
        """
        Update the security profiles assigned to the user.
        """
        if _request is None:
            _params = {}
            if security_profile_ids is not ShapeBase.NOT_SET:
                _params['security_profile_ids'] = security_profile_ids
            if user_id is not ShapeBase.NOT_SET:
                _params['user_id'] = user_id
            if instance_id is not ShapeBase.NOT_SET:
                _params['instance_id'] = instance_id
            _request = shapes.UpdateUserSecurityProfilesRequest(**_params)
        response = self._boto_client.update_user_security_profiles(
            **_request.to_boto()
        )
