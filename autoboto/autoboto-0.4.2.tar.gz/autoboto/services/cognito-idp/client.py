import datetime
import typing
import boto3
from autoboto import ClientBase, ShapeBase, OutputShapeBase
from . import shapes


class Client(ClientBase):
    def __init__(self, *args, **kwargs):
        super().__init__("cognito-idp", *args, **kwargs)

    def add_custom_attributes(
        self,
        _request: shapes.AddCustomAttributesRequest = None,
        *,
        user_pool_id: str,
        custom_attributes: typing.List[shapes.SchemaAttributeType],
    ) -> shapes.AddCustomAttributesResponse:
        """
        Adds additional user attributes to the user pool schema.
        """
        if _request is None:
            _params = {}
            if user_pool_id is not ShapeBase.NOT_SET:
                _params['user_pool_id'] = user_pool_id
            if custom_attributes is not ShapeBase.NOT_SET:
                _params['custom_attributes'] = custom_attributes
            _request = shapes.AddCustomAttributesRequest(**_params)
        response = self._boto_client.add_custom_attributes(**_request.to_boto())

        return shapes.AddCustomAttributesResponse.from_boto(response)

    def admin_add_user_to_group(
        self,
        _request: shapes.AdminAddUserToGroupRequest = None,
        *,
        user_pool_id: str,
        username: str,
        group_name: str,
    ) -> None:
        """
        Adds the specified user to the specified group.

        Requires developer credentials.
        """
        if _request is None:
            _params = {}
            if user_pool_id is not ShapeBase.NOT_SET:
                _params['user_pool_id'] = user_pool_id
            if username is not ShapeBase.NOT_SET:
                _params['username'] = username
            if group_name is not ShapeBase.NOT_SET:
                _params['group_name'] = group_name
            _request = shapes.AdminAddUserToGroupRequest(**_params)
        response = self._boto_client.admin_add_user_to_group(
            **_request.to_boto()
        )

    def admin_confirm_sign_up(
        self,
        _request: shapes.AdminConfirmSignUpRequest = None,
        *,
        user_pool_id: str,
        username: str,
    ) -> shapes.AdminConfirmSignUpResponse:
        """
        Confirms user registration as an admin without using a confirmation code. Works
        on any user.

        Requires developer credentials.
        """
        if _request is None:
            _params = {}
            if user_pool_id is not ShapeBase.NOT_SET:
                _params['user_pool_id'] = user_pool_id
            if username is not ShapeBase.NOT_SET:
                _params['username'] = username
            _request = shapes.AdminConfirmSignUpRequest(**_params)
        response = self._boto_client.admin_confirm_sign_up(**_request.to_boto())

        return shapes.AdminConfirmSignUpResponse.from_boto(response)

    def admin_create_user(
        self,
        _request: shapes.AdminCreateUserRequest = None,
        *,
        user_pool_id: str,
        username: str,
        user_attributes: typing.List[shapes.AttributeType] = ShapeBase.NOT_SET,
        validation_data: typing.List[shapes.AttributeType] = ShapeBase.NOT_SET,
        temporary_password: str = ShapeBase.NOT_SET,
        force_alias_creation: bool = ShapeBase.NOT_SET,
        message_action: typing.Union[str, shapes.MessageActionType] = ShapeBase.
        NOT_SET,
        desired_delivery_mediums: typing.List[
            typing.Union[str, shapes.DeliveryMediumType]] = ShapeBase.NOT_SET,
    ) -> shapes.AdminCreateUserResponse:
        """
        Creates a new user in the specified user pool.

        If `MessageAction` is not set, the default is to send a welcome message via
        email or phone (SMS).

        This message is based on a template that you configured in your call to or .
        This template includes your custom sign-up instructions and placeholders for
        user name and temporary password.

        Alternatively, you can call AdminCreateUser with “SUPPRESS” for the
        `MessageAction` parameter, and Amazon Cognito will not send any email.

        In either case, the user will be in the `FORCE_CHANGE_PASSWORD` state until they
        sign in and change their password.

        AdminCreateUser requires developer credentials.
        """
        if _request is None:
            _params = {}
            if user_pool_id is not ShapeBase.NOT_SET:
                _params['user_pool_id'] = user_pool_id
            if username is not ShapeBase.NOT_SET:
                _params['username'] = username
            if user_attributes is not ShapeBase.NOT_SET:
                _params['user_attributes'] = user_attributes
            if validation_data is not ShapeBase.NOT_SET:
                _params['validation_data'] = validation_data
            if temporary_password is not ShapeBase.NOT_SET:
                _params['temporary_password'] = temporary_password
            if force_alias_creation is not ShapeBase.NOT_SET:
                _params['force_alias_creation'] = force_alias_creation
            if message_action is not ShapeBase.NOT_SET:
                _params['message_action'] = message_action
            if desired_delivery_mediums is not ShapeBase.NOT_SET:
                _params['desired_delivery_mediums'] = desired_delivery_mediums
            _request = shapes.AdminCreateUserRequest(**_params)
        response = self._boto_client.admin_create_user(**_request.to_boto())

        return shapes.AdminCreateUserResponse.from_boto(response)

    def admin_delete_user(
        self,
        _request: shapes.AdminDeleteUserRequest = None,
        *,
        user_pool_id: str,
        username: str,
    ) -> None:
        """
        Deletes a user as an administrator. Works on any user.

        Requires developer credentials.
        """
        if _request is None:
            _params = {}
            if user_pool_id is not ShapeBase.NOT_SET:
                _params['user_pool_id'] = user_pool_id
            if username is not ShapeBase.NOT_SET:
                _params['username'] = username
            _request = shapes.AdminDeleteUserRequest(**_params)
        response = self._boto_client.admin_delete_user(**_request.to_boto())

    def admin_delete_user_attributes(
        self,
        _request: shapes.AdminDeleteUserAttributesRequest = None,
        *,
        user_pool_id: str,
        username: str,
        user_attribute_names: typing.List[str],
    ) -> shapes.AdminDeleteUserAttributesResponse:
        """
        Deletes the user attributes in a user pool as an administrator. Works on any
        user.

        Requires developer credentials.
        """
        if _request is None:
            _params = {}
            if user_pool_id is not ShapeBase.NOT_SET:
                _params['user_pool_id'] = user_pool_id
            if username is not ShapeBase.NOT_SET:
                _params['username'] = username
            if user_attribute_names is not ShapeBase.NOT_SET:
                _params['user_attribute_names'] = user_attribute_names
            _request = shapes.AdminDeleteUserAttributesRequest(**_params)
        response = self._boto_client.admin_delete_user_attributes(
            **_request.to_boto()
        )

        return shapes.AdminDeleteUserAttributesResponse.from_boto(response)

    def admin_disable_provider_for_user(
        self,
        _request: shapes.AdminDisableProviderForUserRequest = None,
        *,
        user_pool_id: str,
        user: shapes.ProviderUserIdentifierType,
    ) -> shapes.AdminDisableProviderForUserResponse:
        """
        Disables the user from signing in with the specified external (SAML or social)
        identity provider. If the user to disable is a Cognito User Pools native
        username + password user, they are not permitted to use their password to sign-
        in. If the user to disable is a linked external IdP user, any link between that
        user and an existing user is removed. The next time the external user (no longer
        attached to the previously linked `DestinationUser`) signs in, they must create
        a new user account. See .

        This action is enabled only for admin access and requires developer credentials.

        The `ProviderName` must match the value specified when creating an IdP for the
        pool.

        To disable a native username + password user, the `ProviderName` value must be
        `Cognito` and the `ProviderAttributeName` must be `Cognito_Subject`, with the
        `ProviderAttributeValue` being the name that is used in the user pool for the
        user.

        The `ProviderAttributeName` must always be `Cognito_Subject` for social identity
        providers. The `ProviderAttributeValue` must always be the exact subject that
        was used when the user was originally linked as a source user.

        For de-linking a SAML identity, there are two scenarios. If the linked identity
        has not yet been used to sign-in, the `ProviderAttributeName` and
        `ProviderAttributeValue` must be the same values that were used for the
        `SourceUser` when the identities were originally linked in the call. (If the
        linking was done with `ProviderAttributeName` set to `Cognito_Subject`, the same
        applies here). However, if the user has already signed in, the
        `ProviderAttributeName` must be `Cognito_Subject` and `ProviderAttributeValue`
        must be the subject of the SAML assertion.
        """
        if _request is None:
            _params = {}
            if user_pool_id is not ShapeBase.NOT_SET:
                _params['user_pool_id'] = user_pool_id
            if user is not ShapeBase.NOT_SET:
                _params['user'] = user
            _request = shapes.AdminDisableProviderForUserRequest(**_params)
        response = self._boto_client.admin_disable_provider_for_user(
            **_request.to_boto()
        )

        return shapes.AdminDisableProviderForUserResponse.from_boto(response)

    def admin_disable_user(
        self,
        _request: shapes.AdminDisableUserRequest = None,
        *,
        user_pool_id: str,
        username: str,
    ) -> shapes.AdminDisableUserResponse:
        """
        Disables the specified user as an administrator. Works on any user.

        Requires developer credentials.
        """
        if _request is None:
            _params = {}
            if user_pool_id is not ShapeBase.NOT_SET:
                _params['user_pool_id'] = user_pool_id
            if username is not ShapeBase.NOT_SET:
                _params['username'] = username
            _request = shapes.AdminDisableUserRequest(**_params)
        response = self._boto_client.admin_disable_user(**_request.to_boto())

        return shapes.AdminDisableUserResponse.from_boto(response)

    def admin_enable_user(
        self,
        _request: shapes.AdminEnableUserRequest = None,
        *,
        user_pool_id: str,
        username: str,
    ) -> shapes.AdminEnableUserResponse:
        """
        Enables the specified user as an administrator. Works on any user.

        Requires developer credentials.
        """
        if _request is None:
            _params = {}
            if user_pool_id is not ShapeBase.NOT_SET:
                _params['user_pool_id'] = user_pool_id
            if username is not ShapeBase.NOT_SET:
                _params['username'] = username
            _request = shapes.AdminEnableUserRequest(**_params)
        response = self._boto_client.admin_enable_user(**_request.to_boto())

        return shapes.AdminEnableUserResponse.from_boto(response)

    def admin_forget_device(
        self,
        _request: shapes.AdminForgetDeviceRequest = None,
        *,
        user_pool_id: str,
        username: str,
        device_key: str,
    ) -> None:
        """
        Forgets the device, as an administrator.

        Requires developer credentials.
        """
        if _request is None:
            _params = {}
            if user_pool_id is not ShapeBase.NOT_SET:
                _params['user_pool_id'] = user_pool_id
            if username is not ShapeBase.NOT_SET:
                _params['username'] = username
            if device_key is not ShapeBase.NOT_SET:
                _params['device_key'] = device_key
            _request = shapes.AdminForgetDeviceRequest(**_params)
        response = self._boto_client.admin_forget_device(**_request.to_boto())

    def admin_get_device(
        self,
        _request: shapes.AdminGetDeviceRequest = None,
        *,
        device_key: str,
        user_pool_id: str,
        username: str,
    ) -> shapes.AdminGetDeviceResponse:
        """
        Gets the device, as an administrator.

        Requires developer credentials.
        """
        if _request is None:
            _params = {}
            if device_key is not ShapeBase.NOT_SET:
                _params['device_key'] = device_key
            if user_pool_id is not ShapeBase.NOT_SET:
                _params['user_pool_id'] = user_pool_id
            if username is not ShapeBase.NOT_SET:
                _params['username'] = username
            _request = shapes.AdminGetDeviceRequest(**_params)
        response = self._boto_client.admin_get_device(**_request.to_boto())

        return shapes.AdminGetDeviceResponse.from_boto(response)

    def admin_get_user(
        self,
        _request: shapes.AdminGetUserRequest = None,
        *,
        user_pool_id: str,
        username: str,
    ) -> shapes.AdminGetUserResponse:
        """
        Gets the specified user by user name in a user pool as an administrator. Works
        on any user.

        Requires developer credentials.
        """
        if _request is None:
            _params = {}
            if user_pool_id is not ShapeBase.NOT_SET:
                _params['user_pool_id'] = user_pool_id
            if username is not ShapeBase.NOT_SET:
                _params['username'] = username
            _request = shapes.AdminGetUserRequest(**_params)
        response = self._boto_client.admin_get_user(**_request.to_boto())

        return shapes.AdminGetUserResponse.from_boto(response)

    def admin_initiate_auth(
        self,
        _request: shapes.AdminInitiateAuthRequest = None,
        *,
        user_pool_id: str,
        client_id: str,
        auth_flow: typing.Union[str, shapes.AuthFlowType],
        auth_parameters: typing.Dict[str, str] = ShapeBase.NOT_SET,
        client_metadata: typing.Dict[str, str] = ShapeBase.NOT_SET,
        analytics_metadata: shapes.AnalyticsMetadataType = ShapeBase.NOT_SET,
        context_data: shapes.ContextDataType = ShapeBase.NOT_SET,
    ) -> shapes.AdminInitiateAuthResponse:
        """
        Initiates the authentication flow, as an administrator.

        Requires developer credentials.
        """
        if _request is None:
            _params = {}
            if user_pool_id is not ShapeBase.NOT_SET:
                _params['user_pool_id'] = user_pool_id
            if client_id is not ShapeBase.NOT_SET:
                _params['client_id'] = client_id
            if auth_flow is not ShapeBase.NOT_SET:
                _params['auth_flow'] = auth_flow
            if auth_parameters is not ShapeBase.NOT_SET:
                _params['auth_parameters'] = auth_parameters
            if client_metadata is not ShapeBase.NOT_SET:
                _params['client_metadata'] = client_metadata
            if analytics_metadata is not ShapeBase.NOT_SET:
                _params['analytics_metadata'] = analytics_metadata
            if context_data is not ShapeBase.NOT_SET:
                _params['context_data'] = context_data
            _request = shapes.AdminInitiateAuthRequest(**_params)
        response = self._boto_client.admin_initiate_auth(**_request.to_boto())

        return shapes.AdminInitiateAuthResponse.from_boto(response)

    def admin_link_provider_for_user(
        self,
        _request: shapes.AdminLinkProviderForUserRequest = None,
        *,
        user_pool_id: str,
        destination_user: shapes.ProviderUserIdentifierType,
        source_user: shapes.ProviderUserIdentifierType,
    ) -> shapes.AdminLinkProviderForUserResponse:
        """
        Links an existing user account in a user pool (`DestinationUser`) to an identity
        from an external identity provider (`SourceUser`) based on a specified attribute
        name and value from the external identity provider. This allows you to create a
        link from the existing user account to an external federated user identity that
        has not yet been used to sign in, so that the federated user identity can be
        used to sign in as the existing user account.

        For example, if there is an existing user with a username and password, this API
        links that user to a federated user identity, so that when the federated user
        identity is used, the user signs in as the existing user account.

        Because this API allows a user with an external federated identity to sign in as
        an existing user in the user pool, it is critical that it only be used with
        external identity providers and provider attributes that have been trusted by
        the application owner.

        See also .

        This action is enabled only for admin access and requires developer credentials.
        """
        if _request is None:
            _params = {}
            if user_pool_id is not ShapeBase.NOT_SET:
                _params['user_pool_id'] = user_pool_id
            if destination_user is not ShapeBase.NOT_SET:
                _params['destination_user'] = destination_user
            if source_user is not ShapeBase.NOT_SET:
                _params['source_user'] = source_user
            _request = shapes.AdminLinkProviderForUserRequest(**_params)
        response = self._boto_client.admin_link_provider_for_user(
            **_request.to_boto()
        )

        return shapes.AdminLinkProviderForUserResponse.from_boto(response)

    def admin_list_devices(
        self,
        _request: shapes.AdminListDevicesRequest = None,
        *,
        user_pool_id: str,
        username: str,
        limit: int = ShapeBase.NOT_SET,
        pagination_token: str = ShapeBase.NOT_SET,
    ) -> shapes.AdminListDevicesResponse:
        """
        Lists devices, as an administrator.

        Requires developer credentials.
        """
        if _request is None:
            _params = {}
            if user_pool_id is not ShapeBase.NOT_SET:
                _params['user_pool_id'] = user_pool_id
            if username is not ShapeBase.NOT_SET:
                _params['username'] = username
            if limit is not ShapeBase.NOT_SET:
                _params['limit'] = limit
            if pagination_token is not ShapeBase.NOT_SET:
                _params['pagination_token'] = pagination_token
            _request = shapes.AdminListDevicesRequest(**_params)
        response = self._boto_client.admin_list_devices(**_request.to_boto())

        return shapes.AdminListDevicesResponse.from_boto(response)

    def admin_list_groups_for_user(
        self,
        _request: shapes.AdminListGroupsForUserRequest = None,
        *,
        username: str,
        user_pool_id: str,
        limit: int = ShapeBase.NOT_SET,
        next_token: str = ShapeBase.NOT_SET,
    ) -> shapes.AdminListGroupsForUserResponse:
        """
        Lists the groups that the user belongs to.

        Requires developer credentials.
        """
        if _request is None:
            _params = {}
            if username is not ShapeBase.NOT_SET:
                _params['username'] = username
            if user_pool_id is not ShapeBase.NOT_SET:
                _params['user_pool_id'] = user_pool_id
            if limit is not ShapeBase.NOT_SET:
                _params['limit'] = limit
            if next_token is not ShapeBase.NOT_SET:
                _params['next_token'] = next_token
            _request = shapes.AdminListGroupsForUserRequest(**_params)
        response = self._boto_client.admin_list_groups_for_user(
            **_request.to_boto()
        )

        return shapes.AdminListGroupsForUserResponse.from_boto(response)

    def admin_list_user_auth_events(
        self,
        _request: shapes.AdminListUserAuthEventsRequest = None,
        *,
        user_pool_id: str,
        username: str,
        max_results: int = ShapeBase.NOT_SET,
        next_token: str = ShapeBase.NOT_SET,
    ) -> shapes.AdminListUserAuthEventsResponse:
        """
        Lists a history of user activity and any risks detected as part of Amazon
        Cognito advanced security.
        """
        if _request is None:
            _params = {}
            if user_pool_id is not ShapeBase.NOT_SET:
                _params['user_pool_id'] = user_pool_id
            if username is not ShapeBase.NOT_SET:
                _params['username'] = username
            if max_results is not ShapeBase.NOT_SET:
                _params['max_results'] = max_results
            if next_token is not ShapeBase.NOT_SET:
                _params['next_token'] = next_token
            _request = shapes.AdminListUserAuthEventsRequest(**_params)
        response = self._boto_client.admin_list_user_auth_events(
            **_request.to_boto()
        )

        return shapes.AdminListUserAuthEventsResponse.from_boto(response)

    def admin_remove_user_from_group(
        self,
        _request: shapes.AdminRemoveUserFromGroupRequest = None,
        *,
        user_pool_id: str,
        username: str,
        group_name: str,
    ) -> None:
        """
        Removes the specified user from the specified group.

        Requires developer credentials.
        """
        if _request is None:
            _params = {}
            if user_pool_id is not ShapeBase.NOT_SET:
                _params['user_pool_id'] = user_pool_id
            if username is not ShapeBase.NOT_SET:
                _params['username'] = username
            if group_name is not ShapeBase.NOT_SET:
                _params['group_name'] = group_name
            _request = shapes.AdminRemoveUserFromGroupRequest(**_params)
        response = self._boto_client.admin_remove_user_from_group(
            **_request.to_boto()
        )

    def admin_reset_user_password(
        self,
        _request: shapes.AdminResetUserPasswordRequest = None,
        *,
        user_pool_id: str,
        username: str,
    ) -> shapes.AdminResetUserPasswordResponse:
        """
        Resets the specified user's password in a user pool as an administrator. Works
        on any user.

        When a developer calls this API, the current password is invalidated, so it must
        be changed. If a user tries to sign in after the API is called, the app will get
        a PasswordResetRequiredException exception back and should direct the user down
        the flow to reset the password, which is the same as the forgot password flow.
        In addition, if the user pool has phone verification selected and a verified
        phone number exists for the user, or if email verification is selected and a
        verified email exists for the user, calling this API will also result in sending
        a message to the end user with the code to change their password.

        Requires developer credentials.
        """
        if _request is None:
            _params = {}
            if user_pool_id is not ShapeBase.NOT_SET:
                _params['user_pool_id'] = user_pool_id
            if username is not ShapeBase.NOT_SET:
                _params['username'] = username
            _request = shapes.AdminResetUserPasswordRequest(**_params)
        response = self._boto_client.admin_reset_user_password(
            **_request.to_boto()
        )

        return shapes.AdminResetUserPasswordResponse.from_boto(response)

    def admin_respond_to_auth_challenge(
        self,
        _request: shapes.AdminRespondToAuthChallengeRequest = None,
        *,
        user_pool_id: str,
        client_id: str,
        challenge_name: typing.Union[str, shapes.ChallengeNameType],
        challenge_responses: typing.Dict[str, str] = ShapeBase.NOT_SET,
        session: str = ShapeBase.NOT_SET,
        analytics_metadata: shapes.AnalyticsMetadataType = ShapeBase.NOT_SET,
        context_data: shapes.ContextDataType = ShapeBase.NOT_SET,
    ) -> shapes.AdminRespondToAuthChallengeResponse:
        """
        Responds to an authentication challenge, as an administrator.

        Requires developer credentials.
        """
        if _request is None:
            _params = {}
            if user_pool_id is not ShapeBase.NOT_SET:
                _params['user_pool_id'] = user_pool_id
            if client_id is not ShapeBase.NOT_SET:
                _params['client_id'] = client_id
            if challenge_name is not ShapeBase.NOT_SET:
                _params['challenge_name'] = challenge_name
            if challenge_responses is not ShapeBase.NOT_SET:
                _params['challenge_responses'] = challenge_responses
            if session is not ShapeBase.NOT_SET:
                _params['session'] = session
            if analytics_metadata is not ShapeBase.NOT_SET:
                _params['analytics_metadata'] = analytics_metadata
            if context_data is not ShapeBase.NOT_SET:
                _params['context_data'] = context_data
            _request = shapes.AdminRespondToAuthChallengeRequest(**_params)
        response = self._boto_client.admin_respond_to_auth_challenge(
            **_request.to_boto()
        )

        return shapes.AdminRespondToAuthChallengeResponse.from_boto(response)

    def admin_set_user_mfa_preference(
        self,
        _request: shapes.AdminSetUserMFAPreferenceRequest = None,
        *,
        username: str,
        user_pool_id: str,
        sms_mfa_settings: shapes.SMSMfaSettingsType = ShapeBase.NOT_SET,
        software_token_mfa_settings: shapes.
        SoftwareTokenMfaSettingsType = ShapeBase.NOT_SET,
    ) -> shapes.AdminSetUserMFAPreferenceResponse:
        """
        Sets the user's multi-factor authentication (MFA) preference.
        """
        if _request is None:
            _params = {}
            if username is not ShapeBase.NOT_SET:
                _params['username'] = username
            if user_pool_id is not ShapeBase.NOT_SET:
                _params['user_pool_id'] = user_pool_id
            if sms_mfa_settings is not ShapeBase.NOT_SET:
                _params['sms_mfa_settings'] = sms_mfa_settings
            if software_token_mfa_settings is not ShapeBase.NOT_SET:
                _params['software_token_mfa_settings'
                       ] = software_token_mfa_settings
            _request = shapes.AdminSetUserMFAPreferenceRequest(**_params)
        response = self._boto_client.admin_set_user_mfa_preference(
            **_request.to_boto()
        )

        return shapes.AdminSetUserMFAPreferenceResponse.from_boto(response)

    def admin_set_user_settings(
        self,
        _request: shapes.AdminSetUserSettingsRequest = None,
        *,
        user_pool_id: str,
        username: str,
        mfa_options: typing.List[shapes.MFAOptionType],
    ) -> shapes.AdminSetUserSettingsResponse:
        """
        Sets all the user settings for a specified user name. Works on any user.

        Requires developer credentials.
        """
        if _request is None:
            _params = {}
            if user_pool_id is not ShapeBase.NOT_SET:
                _params['user_pool_id'] = user_pool_id
            if username is not ShapeBase.NOT_SET:
                _params['username'] = username
            if mfa_options is not ShapeBase.NOT_SET:
                _params['mfa_options'] = mfa_options
            _request = shapes.AdminSetUserSettingsRequest(**_params)
        response = self._boto_client.admin_set_user_settings(
            **_request.to_boto()
        )

        return shapes.AdminSetUserSettingsResponse.from_boto(response)

    def admin_update_auth_event_feedback(
        self,
        _request: shapes.AdminUpdateAuthEventFeedbackRequest = None,
        *,
        user_pool_id: str,
        username: str,
        event_id: str,
        feedback_value: typing.Union[str, shapes.FeedbackValueType],
    ) -> shapes.AdminUpdateAuthEventFeedbackResponse:
        """
        Provides feedback for an authentication event as to whether it was from a valid
        user. This feedback is used for improving the risk evaluation decision for the
        user pool as part of Amazon Cognito advanced security.
        """
        if _request is None:
            _params = {}
            if user_pool_id is not ShapeBase.NOT_SET:
                _params['user_pool_id'] = user_pool_id
            if username is not ShapeBase.NOT_SET:
                _params['username'] = username
            if event_id is not ShapeBase.NOT_SET:
                _params['event_id'] = event_id
            if feedback_value is not ShapeBase.NOT_SET:
                _params['feedback_value'] = feedback_value
            _request = shapes.AdminUpdateAuthEventFeedbackRequest(**_params)
        response = self._boto_client.admin_update_auth_event_feedback(
            **_request.to_boto()
        )

        return shapes.AdminUpdateAuthEventFeedbackResponse.from_boto(response)

    def admin_update_device_status(
        self,
        _request: shapes.AdminUpdateDeviceStatusRequest = None,
        *,
        user_pool_id: str,
        username: str,
        device_key: str,
        device_remembered_status: typing.
        Union[str, shapes.DeviceRememberedStatusType] = ShapeBase.NOT_SET,
    ) -> shapes.AdminUpdateDeviceStatusResponse:
        """
        Updates the device status as an administrator.

        Requires developer credentials.
        """
        if _request is None:
            _params = {}
            if user_pool_id is not ShapeBase.NOT_SET:
                _params['user_pool_id'] = user_pool_id
            if username is not ShapeBase.NOT_SET:
                _params['username'] = username
            if device_key is not ShapeBase.NOT_SET:
                _params['device_key'] = device_key
            if device_remembered_status is not ShapeBase.NOT_SET:
                _params['device_remembered_status'] = device_remembered_status
            _request = shapes.AdminUpdateDeviceStatusRequest(**_params)
        response = self._boto_client.admin_update_device_status(
            **_request.to_boto()
        )

        return shapes.AdminUpdateDeviceStatusResponse.from_boto(response)

    def admin_update_user_attributes(
        self,
        _request: shapes.AdminUpdateUserAttributesRequest = None,
        *,
        user_pool_id: str,
        username: str,
        user_attributes: typing.List[shapes.AttributeType],
    ) -> shapes.AdminUpdateUserAttributesResponse:
        """
        Updates the specified user's attributes, including developer attributes, as an
        administrator. Works on any user.

        For custom attributes, you must prepend the `custom:` prefix to the attribute
        name.

        In addition to updating user attributes, this API can also be used to mark phone
        and email as verified.

        Requires developer credentials.
        """
        if _request is None:
            _params = {}
            if user_pool_id is not ShapeBase.NOT_SET:
                _params['user_pool_id'] = user_pool_id
            if username is not ShapeBase.NOT_SET:
                _params['username'] = username
            if user_attributes is not ShapeBase.NOT_SET:
                _params['user_attributes'] = user_attributes
            _request = shapes.AdminUpdateUserAttributesRequest(**_params)
        response = self._boto_client.admin_update_user_attributes(
            **_request.to_boto()
        )

        return shapes.AdminUpdateUserAttributesResponse.from_boto(response)

    def admin_user_global_sign_out(
        self,
        _request: shapes.AdminUserGlobalSignOutRequest = None,
        *,
        user_pool_id: str,
        username: str,
    ) -> shapes.AdminUserGlobalSignOutResponse:
        """
        Signs out users from all devices, as an administrator.

        Requires developer credentials.
        """
        if _request is None:
            _params = {}
            if user_pool_id is not ShapeBase.NOT_SET:
                _params['user_pool_id'] = user_pool_id
            if username is not ShapeBase.NOT_SET:
                _params['username'] = username
            _request = shapes.AdminUserGlobalSignOutRequest(**_params)
        response = self._boto_client.admin_user_global_sign_out(
            **_request.to_boto()
        )

        return shapes.AdminUserGlobalSignOutResponse.from_boto(response)

    def associate_software_token(
        self,
        _request: shapes.AssociateSoftwareTokenRequest = None,
        *,
        access_token: str = ShapeBase.NOT_SET,
        session: str = ShapeBase.NOT_SET,
    ) -> shapes.AssociateSoftwareTokenResponse:
        """
        Returns a unique generated shared secret key code for the user account. The
        request takes an access token or a session string, but not both.
        """
        if _request is None:
            _params = {}
            if access_token is not ShapeBase.NOT_SET:
                _params['access_token'] = access_token
            if session is not ShapeBase.NOT_SET:
                _params['session'] = session
            _request = shapes.AssociateSoftwareTokenRequest(**_params)
        response = self._boto_client.associate_software_token(
            **_request.to_boto()
        )

        return shapes.AssociateSoftwareTokenResponse.from_boto(response)

    def change_password(
        self,
        _request: shapes.ChangePasswordRequest = None,
        *,
        previous_password: str,
        proposed_password: str,
        access_token: str,
    ) -> shapes.ChangePasswordResponse:
        """
        Changes the password for a specified user in a user pool.
        """
        if _request is None:
            _params = {}
            if previous_password is not ShapeBase.NOT_SET:
                _params['previous_password'] = previous_password
            if proposed_password is not ShapeBase.NOT_SET:
                _params['proposed_password'] = proposed_password
            if access_token is not ShapeBase.NOT_SET:
                _params['access_token'] = access_token
            _request = shapes.ChangePasswordRequest(**_params)
        response = self._boto_client.change_password(**_request.to_boto())

        return shapes.ChangePasswordResponse.from_boto(response)

    def confirm_device(
        self,
        _request: shapes.ConfirmDeviceRequest = None,
        *,
        access_token: str,
        device_key: str,
        device_secret_verifier_config: shapes.
        DeviceSecretVerifierConfigType = ShapeBase.NOT_SET,
        device_name: str = ShapeBase.NOT_SET,
    ) -> shapes.ConfirmDeviceResponse:
        """
        Confirms tracking of the device. This API call is the call that begins device
        tracking.
        """
        if _request is None:
            _params = {}
            if access_token is not ShapeBase.NOT_SET:
                _params['access_token'] = access_token
            if device_key is not ShapeBase.NOT_SET:
                _params['device_key'] = device_key
            if device_secret_verifier_config is not ShapeBase.NOT_SET:
                _params['device_secret_verifier_config'
                       ] = device_secret_verifier_config
            if device_name is not ShapeBase.NOT_SET:
                _params['device_name'] = device_name
            _request = shapes.ConfirmDeviceRequest(**_params)
        response = self._boto_client.confirm_device(**_request.to_boto())

        return shapes.ConfirmDeviceResponse.from_boto(response)

    def confirm_forgot_password(
        self,
        _request: shapes.ConfirmForgotPasswordRequest = None,
        *,
        client_id: str,
        username: str,
        confirmation_code: str,
        password: str,
        secret_hash: str = ShapeBase.NOT_SET,
        analytics_metadata: shapes.AnalyticsMetadataType = ShapeBase.NOT_SET,
        user_context_data: shapes.UserContextDataType = ShapeBase.NOT_SET,
    ) -> shapes.ConfirmForgotPasswordResponse:
        """
        Allows a user to enter a confirmation code to reset a forgotten password.
        """
        if _request is None:
            _params = {}
            if client_id is not ShapeBase.NOT_SET:
                _params['client_id'] = client_id
            if username is not ShapeBase.NOT_SET:
                _params['username'] = username
            if confirmation_code is not ShapeBase.NOT_SET:
                _params['confirmation_code'] = confirmation_code
            if password is not ShapeBase.NOT_SET:
                _params['password'] = password
            if secret_hash is not ShapeBase.NOT_SET:
                _params['secret_hash'] = secret_hash
            if analytics_metadata is not ShapeBase.NOT_SET:
                _params['analytics_metadata'] = analytics_metadata
            if user_context_data is not ShapeBase.NOT_SET:
                _params['user_context_data'] = user_context_data
            _request = shapes.ConfirmForgotPasswordRequest(**_params)
        response = self._boto_client.confirm_forgot_password(
            **_request.to_boto()
        )

        return shapes.ConfirmForgotPasswordResponse.from_boto(response)

    def confirm_sign_up(
        self,
        _request: shapes.ConfirmSignUpRequest = None,
        *,
        client_id: str,
        username: str,
        confirmation_code: str,
        secret_hash: str = ShapeBase.NOT_SET,
        force_alias_creation: bool = ShapeBase.NOT_SET,
        analytics_metadata: shapes.AnalyticsMetadataType = ShapeBase.NOT_SET,
        user_context_data: shapes.UserContextDataType = ShapeBase.NOT_SET,
    ) -> shapes.ConfirmSignUpResponse:
        """
        Confirms registration of a user and handles the existing alias from a previous
        user.
        """
        if _request is None:
            _params = {}
            if client_id is not ShapeBase.NOT_SET:
                _params['client_id'] = client_id
            if username is not ShapeBase.NOT_SET:
                _params['username'] = username
            if confirmation_code is not ShapeBase.NOT_SET:
                _params['confirmation_code'] = confirmation_code
            if secret_hash is not ShapeBase.NOT_SET:
                _params['secret_hash'] = secret_hash
            if force_alias_creation is not ShapeBase.NOT_SET:
                _params['force_alias_creation'] = force_alias_creation
            if analytics_metadata is not ShapeBase.NOT_SET:
                _params['analytics_metadata'] = analytics_metadata
            if user_context_data is not ShapeBase.NOT_SET:
                _params['user_context_data'] = user_context_data
            _request = shapes.ConfirmSignUpRequest(**_params)
        response = self._boto_client.confirm_sign_up(**_request.to_boto())

        return shapes.ConfirmSignUpResponse.from_boto(response)

    def create_group(
        self,
        _request: shapes.CreateGroupRequest = None,
        *,
        group_name: str,
        user_pool_id: str,
        description: str = ShapeBase.NOT_SET,
        role_arn: str = ShapeBase.NOT_SET,
        precedence: int = ShapeBase.NOT_SET,
    ) -> shapes.CreateGroupResponse:
        """
        Creates a new group in the specified user pool.

        Requires developer credentials.
        """
        if _request is None:
            _params = {}
            if group_name is not ShapeBase.NOT_SET:
                _params['group_name'] = group_name
            if user_pool_id is not ShapeBase.NOT_SET:
                _params['user_pool_id'] = user_pool_id
            if description is not ShapeBase.NOT_SET:
                _params['description'] = description
            if role_arn is not ShapeBase.NOT_SET:
                _params['role_arn'] = role_arn
            if precedence is not ShapeBase.NOT_SET:
                _params['precedence'] = precedence
            _request = shapes.CreateGroupRequest(**_params)
        response = self._boto_client.create_group(**_request.to_boto())

        return shapes.CreateGroupResponse.from_boto(response)

    def create_identity_provider(
        self,
        _request: shapes.CreateIdentityProviderRequest = None,
        *,
        user_pool_id: str,
        provider_name: str,
        provider_type: typing.Union[str, shapes.IdentityProviderTypeType],
        provider_details: typing.Dict[str, str],
        attribute_mapping: typing.Dict[str, str] = ShapeBase.NOT_SET,
        idp_identifiers: typing.List[str] = ShapeBase.NOT_SET,
    ) -> shapes.CreateIdentityProviderResponse:
        """
        Creates an identity provider for a user pool.
        """
        if _request is None:
            _params = {}
            if user_pool_id is not ShapeBase.NOT_SET:
                _params['user_pool_id'] = user_pool_id
            if provider_name is not ShapeBase.NOT_SET:
                _params['provider_name'] = provider_name
            if provider_type is not ShapeBase.NOT_SET:
                _params['provider_type'] = provider_type
            if provider_details is not ShapeBase.NOT_SET:
                _params['provider_details'] = provider_details
            if attribute_mapping is not ShapeBase.NOT_SET:
                _params['attribute_mapping'] = attribute_mapping
            if idp_identifiers is not ShapeBase.NOT_SET:
                _params['idp_identifiers'] = idp_identifiers
            _request = shapes.CreateIdentityProviderRequest(**_params)
        response = self._boto_client.create_identity_provider(
            **_request.to_boto()
        )

        return shapes.CreateIdentityProviderResponse.from_boto(response)

    def create_resource_server(
        self,
        _request: shapes.CreateResourceServerRequest = None,
        *,
        user_pool_id: str,
        identifier: str,
        name: str,
        scopes: typing.List[shapes.ResourceServerScopeType] = ShapeBase.NOT_SET,
    ) -> shapes.CreateResourceServerResponse:
        """
        Creates a new OAuth2.0 resource server and defines custom scopes in it.
        """
        if _request is None:
            _params = {}
            if user_pool_id is not ShapeBase.NOT_SET:
                _params['user_pool_id'] = user_pool_id
            if identifier is not ShapeBase.NOT_SET:
                _params['identifier'] = identifier
            if name is not ShapeBase.NOT_SET:
                _params['name'] = name
            if scopes is not ShapeBase.NOT_SET:
                _params['scopes'] = scopes
            _request = shapes.CreateResourceServerRequest(**_params)
        response = self._boto_client.create_resource_server(
            **_request.to_boto()
        )

        return shapes.CreateResourceServerResponse.from_boto(response)

    def create_user_import_job(
        self,
        _request: shapes.CreateUserImportJobRequest = None,
        *,
        job_name: str,
        user_pool_id: str,
        cloud_watch_logs_role_arn: str,
    ) -> shapes.CreateUserImportJobResponse:
        """
        Creates the user import job.
        """
        if _request is None:
            _params = {}
            if job_name is not ShapeBase.NOT_SET:
                _params['job_name'] = job_name
            if user_pool_id is not ShapeBase.NOT_SET:
                _params['user_pool_id'] = user_pool_id
            if cloud_watch_logs_role_arn is not ShapeBase.NOT_SET:
                _params['cloud_watch_logs_role_arn'] = cloud_watch_logs_role_arn
            _request = shapes.CreateUserImportJobRequest(**_params)
        response = self._boto_client.create_user_import_job(
            **_request.to_boto()
        )

        return shapes.CreateUserImportJobResponse.from_boto(response)

    def create_user_pool(
        self,
        _request: shapes.CreateUserPoolRequest = None,
        *,
        pool_name: str,
        policies: shapes.UserPoolPolicyType = ShapeBase.NOT_SET,
        lambda_config: shapes.LambdaConfigType = ShapeBase.NOT_SET,
        auto_verified_attributes: typing.List[
            typing.Union[str, shapes.VerifiedAttributeType]
        ] = ShapeBase.NOT_SET,
        alias_attributes: typing.List[
            typing.Union[str, shapes.AliasAttributeType]] = ShapeBase.NOT_SET,
        username_attributes: typing.List[typing.Union[str, shapes.
                                                      UsernameAttributeType]
                                        ] = ShapeBase.NOT_SET,
        sms_verification_message: str = ShapeBase.NOT_SET,
        email_verification_message: str = ShapeBase.NOT_SET,
        email_verification_subject: str = ShapeBase.NOT_SET,
        verification_message_template: shapes.
        VerificationMessageTemplateType = ShapeBase.NOT_SET,
        sms_authentication_message: str = ShapeBase.NOT_SET,
        mfa_configuration: typing.Union[str, shapes.
                                        UserPoolMfaType] = ShapeBase.NOT_SET,
        device_configuration: shapes.DeviceConfigurationType = ShapeBase.
        NOT_SET,
        email_configuration: shapes.EmailConfigurationType = ShapeBase.NOT_SET,
        sms_configuration: shapes.SmsConfigurationType = ShapeBase.NOT_SET,
        user_pool_tags: typing.Dict[str, str] = ShapeBase.NOT_SET,
        admin_create_user_config: shapes.AdminCreateUserConfigType = ShapeBase.
        NOT_SET,
        schema: typing.List[shapes.SchemaAttributeType] = ShapeBase.NOT_SET,
        user_pool_add_ons: shapes.UserPoolAddOnsType = ShapeBase.NOT_SET,
    ) -> shapes.CreateUserPoolResponse:
        """
        Creates a new Amazon Cognito user pool and sets the password policy for the
        pool.
        """
        if _request is None:
            _params = {}
            if pool_name is not ShapeBase.NOT_SET:
                _params['pool_name'] = pool_name
            if policies is not ShapeBase.NOT_SET:
                _params['policies'] = policies
            if lambda_config is not ShapeBase.NOT_SET:
                _params['lambda_config'] = lambda_config
            if auto_verified_attributes is not ShapeBase.NOT_SET:
                _params['auto_verified_attributes'] = auto_verified_attributes
            if alias_attributes is not ShapeBase.NOT_SET:
                _params['alias_attributes'] = alias_attributes
            if username_attributes is not ShapeBase.NOT_SET:
                _params['username_attributes'] = username_attributes
            if sms_verification_message is not ShapeBase.NOT_SET:
                _params['sms_verification_message'] = sms_verification_message
            if email_verification_message is not ShapeBase.NOT_SET:
                _params['email_verification_message'
                       ] = email_verification_message
            if email_verification_subject is not ShapeBase.NOT_SET:
                _params['email_verification_subject'
                       ] = email_verification_subject
            if verification_message_template is not ShapeBase.NOT_SET:
                _params['verification_message_template'
                       ] = verification_message_template
            if sms_authentication_message is not ShapeBase.NOT_SET:
                _params['sms_authentication_message'
                       ] = sms_authentication_message
            if mfa_configuration is not ShapeBase.NOT_SET:
                _params['mfa_configuration'] = mfa_configuration
            if device_configuration is not ShapeBase.NOT_SET:
                _params['device_configuration'] = device_configuration
            if email_configuration is not ShapeBase.NOT_SET:
                _params['email_configuration'] = email_configuration
            if sms_configuration is not ShapeBase.NOT_SET:
                _params['sms_configuration'] = sms_configuration
            if user_pool_tags is not ShapeBase.NOT_SET:
                _params['user_pool_tags'] = user_pool_tags
            if admin_create_user_config is not ShapeBase.NOT_SET:
                _params['admin_create_user_config'] = admin_create_user_config
            if schema is not ShapeBase.NOT_SET:
                _params['schema'] = schema
            if user_pool_add_ons is not ShapeBase.NOT_SET:
                _params['user_pool_add_ons'] = user_pool_add_ons
            _request = shapes.CreateUserPoolRequest(**_params)
        response = self._boto_client.create_user_pool(**_request.to_boto())

        return shapes.CreateUserPoolResponse.from_boto(response)

    def create_user_pool_client(
        self,
        _request: shapes.CreateUserPoolClientRequest = None,
        *,
        user_pool_id: str,
        client_name: str,
        generate_secret: bool = ShapeBase.NOT_SET,
        refresh_token_validity: int = ShapeBase.NOT_SET,
        read_attributes: typing.List[str] = ShapeBase.NOT_SET,
        write_attributes: typing.List[str] = ShapeBase.NOT_SET,
        explicit_auth_flows: typing.List[typing.Union[str, shapes.
                                                      ExplicitAuthFlowsType]
                                        ] = ShapeBase.NOT_SET,
        supported_identity_providers: typing.List[str] = ShapeBase.NOT_SET,
        callback_urls: typing.List[str] = ShapeBase.NOT_SET,
        logout_urls: typing.List[str] = ShapeBase.NOT_SET,
        default_redirect_uri: str = ShapeBase.NOT_SET,
        allowed_o_auth_flows: typing.List[
            typing.Union[str, shapes.OAuthFlowType]] = ShapeBase.NOT_SET,
        allowed_o_auth_scopes: typing.List[str] = ShapeBase.NOT_SET,
        allowed_o_auth_flows_user_pool_client: bool = ShapeBase.NOT_SET,
        analytics_configuration: shapes.AnalyticsConfigurationType = ShapeBase.
        NOT_SET,
    ) -> shapes.CreateUserPoolClientResponse:
        """
        Creates the user pool client.
        """
        if _request is None:
            _params = {}
            if user_pool_id is not ShapeBase.NOT_SET:
                _params['user_pool_id'] = user_pool_id
            if client_name is not ShapeBase.NOT_SET:
                _params['client_name'] = client_name
            if generate_secret is not ShapeBase.NOT_SET:
                _params['generate_secret'] = generate_secret
            if refresh_token_validity is not ShapeBase.NOT_SET:
                _params['refresh_token_validity'] = refresh_token_validity
            if read_attributes is not ShapeBase.NOT_SET:
                _params['read_attributes'] = read_attributes
            if write_attributes is not ShapeBase.NOT_SET:
                _params['write_attributes'] = write_attributes
            if explicit_auth_flows is not ShapeBase.NOT_SET:
                _params['explicit_auth_flows'] = explicit_auth_flows
            if supported_identity_providers is not ShapeBase.NOT_SET:
                _params['supported_identity_providers'
                       ] = supported_identity_providers
            if callback_urls is not ShapeBase.NOT_SET:
                _params['callback_urls'] = callback_urls
            if logout_urls is not ShapeBase.NOT_SET:
                _params['logout_urls'] = logout_urls
            if default_redirect_uri is not ShapeBase.NOT_SET:
                _params['default_redirect_uri'] = default_redirect_uri
            if allowed_o_auth_flows is not ShapeBase.NOT_SET:
                _params['allowed_o_auth_flows'] = allowed_o_auth_flows
            if allowed_o_auth_scopes is not ShapeBase.NOT_SET:
                _params['allowed_o_auth_scopes'] = allowed_o_auth_scopes
            if allowed_o_auth_flows_user_pool_client is not ShapeBase.NOT_SET:
                _params['allowed_o_auth_flows_user_pool_client'
                       ] = allowed_o_auth_flows_user_pool_client
            if analytics_configuration is not ShapeBase.NOT_SET:
                _params['analytics_configuration'] = analytics_configuration
            _request = shapes.CreateUserPoolClientRequest(**_params)
        response = self._boto_client.create_user_pool_client(
            **_request.to_boto()
        )

        return shapes.CreateUserPoolClientResponse.from_boto(response)

    def create_user_pool_domain(
        self,
        _request: shapes.CreateUserPoolDomainRequest = None,
        *,
        domain: str,
        user_pool_id: str,
        custom_domain_config: shapes.CustomDomainConfigType = ShapeBase.NOT_SET,
    ) -> shapes.CreateUserPoolDomainResponse:
        """
        Creates a new domain for a user pool.
        """
        if _request is None:
            _params = {}
            if domain is not ShapeBase.NOT_SET:
                _params['domain'] = domain
            if user_pool_id is not ShapeBase.NOT_SET:
                _params['user_pool_id'] = user_pool_id
            if custom_domain_config is not ShapeBase.NOT_SET:
                _params['custom_domain_config'] = custom_domain_config
            _request = shapes.CreateUserPoolDomainRequest(**_params)
        response = self._boto_client.create_user_pool_domain(
            **_request.to_boto()
        )

        return shapes.CreateUserPoolDomainResponse.from_boto(response)

    def delete_group(
        self,
        _request: shapes.DeleteGroupRequest = None,
        *,
        group_name: str,
        user_pool_id: str,
    ) -> None:
        """
        Deletes a group. Currently only groups with no members can be deleted.

        Requires developer credentials.
        """
        if _request is None:
            _params = {}
            if group_name is not ShapeBase.NOT_SET:
                _params['group_name'] = group_name
            if user_pool_id is not ShapeBase.NOT_SET:
                _params['user_pool_id'] = user_pool_id
            _request = shapes.DeleteGroupRequest(**_params)
        response = self._boto_client.delete_group(**_request.to_boto())

    def delete_identity_provider(
        self,
        _request: shapes.DeleteIdentityProviderRequest = None,
        *,
        user_pool_id: str,
        provider_name: str,
    ) -> None:
        """
        Deletes an identity provider for a user pool.
        """
        if _request is None:
            _params = {}
            if user_pool_id is not ShapeBase.NOT_SET:
                _params['user_pool_id'] = user_pool_id
            if provider_name is not ShapeBase.NOT_SET:
                _params['provider_name'] = provider_name
            _request = shapes.DeleteIdentityProviderRequest(**_params)
        response = self._boto_client.delete_identity_provider(
            **_request.to_boto()
        )

    def delete_resource_server(
        self,
        _request: shapes.DeleteResourceServerRequest = None,
        *,
        user_pool_id: str,
        identifier: str,
    ) -> None:
        """
        Deletes a resource server.
        """
        if _request is None:
            _params = {}
            if user_pool_id is not ShapeBase.NOT_SET:
                _params['user_pool_id'] = user_pool_id
            if identifier is not ShapeBase.NOT_SET:
                _params['identifier'] = identifier
            _request = shapes.DeleteResourceServerRequest(**_params)
        response = self._boto_client.delete_resource_server(
            **_request.to_boto()
        )

    def delete_user(
        self,
        _request: shapes.DeleteUserRequest = None,
        *,
        access_token: str,
    ) -> None:
        """
        Allows a user to delete himself or herself.
        """
        if _request is None:
            _params = {}
            if access_token is not ShapeBase.NOT_SET:
                _params['access_token'] = access_token
            _request = shapes.DeleteUserRequest(**_params)
        response = self._boto_client.delete_user(**_request.to_boto())

    def delete_user_attributes(
        self,
        _request: shapes.DeleteUserAttributesRequest = None,
        *,
        user_attribute_names: typing.List[str],
        access_token: str,
    ) -> shapes.DeleteUserAttributesResponse:
        """
        Deletes the attributes for a user.
        """
        if _request is None:
            _params = {}
            if user_attribute_names is not ShapeBase.NOT_SET:
                _params['user_attribute_names'] = user_attribute_names
            if access_token is not ShapeBase.NOT_SET:
                _params['access_token'] = access_token
            _request = shapes.DeleteUserAttributesRequest(**_params)
        response = self._boto_client.delete_user_attributes(
            **_request.to_boto()
        )

        return shapes.DeleteUserAttributesResponse.from_boto(response)

    def delete_user_pool(
        self,
        _request: shapes.DeleteUserPoolRequest = None,
        *,
        user_pool_id: str,
    ) -> None:
        """
        Deletes the specified Amazon Cognito user pool.
        """
        if _request is None:
            _params = {}
            if user_pool_id is not ShapeBase.NOT_SET:
                _params['user_pool_id'] = user_pool_id
            _request = shapes.DeleteUserPoolRequest(**_params)
        response = self._boto_client.delete_user_pool(**_request.to_boto())

    def delete_user_pool_client(
        self,
        _request: shapes.DeleteUserPoolClientRequest = None,
        *,
        user_pool_id: str,
        client_id: str,
    ) -> None:
        """
        Allows the developer to delete the user pool client.
        """
        if _request is None:
            _params = {}
            if user_pool_id is not ShapeBase.NOT_SET:
                _params['user_pool_id'] = user_pool_id
            if client_id is not ShapeBase.NOT_SET:
                _params['client_id'] = client_id
            _request = shapes.DeleteUserPoolClientRequest(**_params)
        response = self._boto_client.delete_user_pool_client(
            **_request.to_boto()
        )

    def delete_user_pool_domain(
        self,
        _request: shapes.DeleteUserPoolDomainRequest = None,
        *,
        domain: str,
        user_pool_id: str,
    ) -> shapes.DeleteUserPoolDomainResponse:
        """
        Deletes a domain for a user pool.
        """
        if _request is None:
            _params = {}
            if domain is not ShapeBase.NOT_SET:
                _params['domain'] = domain
            if user_pool_id is not ShapeBase.NOT_SET:
                _params['user_pool_id'] = user_pool_id
            _request = shapes.DeleteUserPoolDomainRequest(**_params)
        response = self._boto_client.delete_user_pool_domain(
            **_request.to_boto()
        )

        return shapes.DeleteUserPoolDomainResponse.from_boto(response)

    def describe_identity_provider(
        self,
        _request: shapes.DescribeIdentityProviderRequest = None,
        *,
        user_pool_id: str,
        provider_name: str,
    ) -> shapes.DescribeIdentityProviderResponse:
        """
        Gets information about a specific identity provider.
        """
        if _request is None:
            _params = {}
            if user_pool_id is not ShapeBase.NOT_SET:
                _params['user_pool_id'] = user_pool_id
            if provider_name is not ShapeBase.NOT_SET:
                _params['provider_name'] = provider_name
            _request = shapes.DescribeIdentityProviderRequest(**_params)
        response = self._boto_client.describe_identity_provider(
            **_request.to_boto()
        )

        return shapes.DescribeIdentityProviderResponse.from_boto(response)

    def describe_resource_server(
        self,
        _request: shapes.DescribeResourceServerRequest = None,
        *,
        user_pool_id: str,
        identifier: str,
    ) -> shapes.DescribeResourceServerResponse:
        """
        Describes a resource server.
        """
        if _request is None:
            _params = {}
            if user_pool_id is not ShapeBase.NOT_SET:
                _params['user_pool_id'] = user_pool_id
            if identifier is not ShapeBase.NOT_SET:
                _params['identifier'] = identifier
            _request = shapes.DescribeResourceServerRequest(**_params)
        response = self._boto_client.describe_resource_server(
            **_request.to_boto()
        )

        return shapes.DescribeResourceServerResponse.from_boto(response)

    def describe_risk_configuration(
        self,
        _request: shapes.DescribeRiskConfigurationRequest = None,
        *,
        user_pool_id: str,
        client_id: str = ShapeBase.NOT_SET,
    ) -> shapes.DescribeRiskConfigurationResponse:
        """
        Describes the risk configuration.
        """
        if _request is None:
            _params = {}
            if user_pool_id is not ShapeBase.NOT_SET:
                _params['user_pool_id'] = user_pool_id
            if client_id is not ShapeBase.NOT_SET:
                _params['client_id'] = client_id
            _request = shapes.DescribeRiskConfigurationRequest(**_params)
        response = self._boto_client.describe_risk_configuration(
            **_request.to_boto()
        )

        return shapes.DescribeRiskConfigurationResponse.from_boto(response)

    def describe_user_import_job(
        self,
        _request: shapes.DescribeUserImportJobRequest = None,
        *,
        user_pool_id: str,
        job_id: str,
    ) -> shapes.DescribeUserImportJobResponse:
        """
        Describes the user import job.
        """
        if _request is None:
            _params = {}
            if user_pool_id is not ShapeBase.NOT_SET:
                _params['user_pool_id'] = user_pool_id
            if job_id is not ShapeBase.NOT_SET:
                _params['job_id'] = job_id
            _request = shapes.DescribeUserImportJobRequest(**_params)
        response = self._boto_client.describe_user_import_job(
            **_request.to_boto()
        )

        return shapes.DescribeUserImportJobResponse.from_boto(response)

    def describe_user_pool(
        self,
        _request: shapes.DescribeUserPoolRequest = None,
        *,
        user_pool_id: str,
    ) -> shapes.DescribeUserPoolResponse:
        """
        Returns the configuration information and metadata of the specified user pool.
        """
        if _request is None:
            _params = {}
            if user_pool_id is not ShapeBase.NOT_SET:
                _params['user_pool_id'] = user_pool_id
            _request = shapes.DescribeUserPoolRequest(**_params)
        response = self._boto_client.describe_user_pool(**_request.to_boto())

        return shapes.DescribeUserPoolResponse.from_boto(response)

    def describe_user_pool_client(
        self,
        _request: shapes.DescribeUserPoolClientRequest = None,
        *,
        user_pool_id: str,
        client_id: str,
    ) -> shapes.DescribeUserPoolClientResponse:
        """
        Client method for returning the configuration information and metadata of the
        specified user pool app client.
        """
        if _request is None:
            _params = {}
            if user_pool_id is not ShapeBase.NOT_SET:
                _params['user_pool_id'] = user_pool_id
            if client_id is not ShapeBase.NOT_SET:
                _params['client_id'] = client_id
            _request = shapes.DescribeUserPoolClientRequest(**_params)
        response = self._boto_client.describe_user_pool_client(
            **_request.to_boto()
        )

        return shapes.DescribeUserPoolClientResponse.from_boto(response)

    def describe_user_pool_domain(
        self,
        _request: shapes.DescribeUserPoolDomainRequest = None,
        *,
        domain: str,
    ) -> shapes.DescribeUserPoolDomainResponse:
        """
        Gets information about a domain.
        """
        if _request is None:
            _params = {}
            if domain is not ShapeBase.NOT_SET:
                _params['domain'] = domain
            _request = shapes.DescribeUserPoolDomainRequest(**_params)
        response = self._boto_client.describe_user_pool_domain(
            **_request.to_boto()
        )

        return shapes.DescribeUserPoolDomainResponse.from_boto(response)

    def forget_device(
        self,
        _request: shapes.ForgetDeviceRequest = None,
        *,
        device_key: str,
        access_token: str = ShapeBase.NOT_SET,
    ) -> None:
        """
        Forgets the specified device.
        """
        if _request is None:
            _params = {}
            if device_key is not ShapeBase.NOT_SET:
                _params['device_key'] = device_key
            if access_token is not ShapeBase.NOT_SET:
                _params['access_token'] = access_token
            _request = shapes.ForgetDeviceRequest(**_params)
        response = self._boto_client.forget_device(**_request.to_boto())

    def forgot_password(
        self,
        _request: shapes.ForgotPasswordRequest = None,
        *,
        client_id: str,
        username: str,
        secret_hash: str = ShapeBase.NOT_SET,
        user_context_data: shapes.UserContextDataType = ShapeBase.NOT_SET,
        analytics_metadata: shapes.AnalyticsMetadataType = ShapeBase.NOT_SET,
    ) -> shapes.ForgotPasswordResponse:
        """
        Calling this API causes a message to be sent to the end user with a confirmation
        code that is required to change the user's password. For the `Username`
        parameter, you can use the username or user alias. If a verified phone number
        exists for the user, the confirmation code is sent to the phone number.
        Otherwise, if a verified email exists, the confirmation code is sent to the
        email. If neither a verified phone number nor a verified email exists,
        `InvalidParameterException` is thrown. To use the confirmation code for
        resetting the password, call .
        """
        if _request is None:
            _params = {}
            if client_id is not ShapeBase.NOT_SET:
                _params['client_id'] = client_id
            if username is not ShapeBase.NOT_SET:
                _params['username'] = username
            if secret_hash is not ShapeBase.NOT_SET:
                _params['secret_hash'] = secret_hash
            if user_context_data is not ShapeBase.NOT_SET:
                _params['user_context_data'] = user_context_data
            if analytics_metadata is not ShapeBase.NOT_SET:
                _params['analytics_metadata'] = analytics_metadata
            _request = shapes.ForgotPasswordRequest(**_params)
        response = self._boto_client.forgot_password(**_request.to_boto())

        return shapes.ForgotPasswordResponse.from_boto(response)

    def get_csv_header(
        self,
        _request: shapes.GetCSVHeaderRequest = None,
        *,
        user_pool_id: str,
    ) -> shapes.GetCSVHeaderResponse:
        """
        Gets the header information for the .csv file to be used as input for the user
        import job.
        """
        if _request is None:
            _params = {}
            if user_pool_id is not ShapeBase.NOT_SET:
                _params['user_pool_id'] = user_pool_id
            _request = shapes.GetCSVHeaderRequest(**_params)
        response = self._boto_client.get_csv_header(**_request.to_boto())

        return shapes.GetCSVHeaderResponse.from_boto(response)

    def get_device(
        self,
        _request: shapes.GetDeviceRequest = None,
        *,
        device_key: str,
        access_token: str = ShapeBase.NOT_SET,
    ) -> shapes.GetDeviceResponse:
        """
        Gets the device.
        """
        if _request is None:
            _params = {}
            if device_key is not ShapeBase.NOT_SET:
                _params['device_key'] = device_key
            if access_token is not ShapeBase.NOT_SET:
                _params['access_token'] = access_token
            _request = shapes.GetDeviceRequest(**_params)
        response = self._boto_client.get_device(**_request.to_boto())

        return shapes.GetDeviceResponse.from_boto(response)

    def get_group(
        self,
        _request: shapes.GetGroupRequest = None,
        *,
        group_name: str,
        user_pool_id: str,
    ) -> shapes.GetGroupResponse:
        """
        Gets a group.

        Requires developer credentials.
        """
        if _request is None:
            _params = {}
            if group_name is not ShapeBase.NOT_SET:
                _params['group_name'] = group_name
            if user_pool_id is not ShapeBase.NOT_SET:
                _params['user_pool_id'] = user_pool_id
            _request = shapes.GetGroupRequest(**_params)
        response = self._boto_client.get_group(**_request.to_boto())

        return shapes.GetGroupResponse.from_boto(response)

    def get_identity_provider_by_identifier(
        self,
        _request: shapes.GetIdentityProviderByIdentifierRequest = None,
        *,
        user_pool_id: str,
        idp_identifier: str,
    ) -> shapes.GetIdentityProviderByIdentifierResponse:
        """
        Gets the specified identity provider.
        """
        if _request is None:
            _params = {}
            if user_pool_id is not ShapeBase.NOT_SET:
                _params['user_pool_id'] = user_pool_id
            if idp_identifier is not ShapeBase.NOT_SET:
                _params['idp_identifier'] = idp_identifier
            _request = shapes.GetIdentityProviderByIdentifierRequest(**_params)
        response = self._boto_client.get_identity_provider_by_identifier(
            **_request.to_boto()
        )

        return shapes.GetIdentityProviderByIdentifierResponse.from_boto(
            response
        )

    def get_signing_certificate(
        self,
        _request: shapes.GetSigningCertificateRequest = None,
        *,
        user_pool_id: str,
    ) -> shapes.GetSigningCertificateResponse:
        """
        This method takes a user pool ID, and returns the signing certificate.
        """
        if _request is None:
            _params = {}
            if user_pool_id is not ShapeBase.NOT_SET:
                _params['user_pool_id'] = user_pool_id
            _request = shapes.GetSigningCertificateRequest(**_params)
        response = self._boto_client.get_signing_certificate(
            **_request.to_boto()
        )

        return shapes.GetSigningCertificateResponse.from_boto(response)

    def get_ui_customization(
        self,
        _request: shapes.GetUICustomizationRequest = None,
        *,
        user_pool_id: str,
        client_id: str = ShapeBase.NOT_SET,
    ) -> shapes.GetUICustomizationResponse:
        """
        Gets the UI Customization information for a particular app client's app UI, if
        there is something set. If nothing is set for the particular client, but there
        is an existing pool level customization (app `clientId` will be `ALL`), then
        that is returned. If nothing is present, then an empty shape is returned.
        """
        if _request is None:
            _params = {}
            if user_pool_id is not ShapeBase.NOT_SET:
                _params['user_pool_id'] = user_pool_id
            if client_id is not ShapeBase.NOT_SET:
                _params['client_id'] = client_id
            _request = shapes.GetUICustomizationRequest(**_params)
        response = self._boto_client.get_ui_customization(**_request.to_boto())

        return shapes.GetUICustomizationResponse.from_boto(response)

    def get_user(
        self,
        _request: shapes.GetUserRequest = None,
        *,
        access_token: str,
    ) -> shapes.GetUserResponse:
        """
        Gets the user attributes and metadata for a user.
        """
        if _request is None:
            _params = {}
            if access_token is not ShapeBase.NOT_SET:
                _params['access_token'] = access_token
            _request = shapes.GetUserRequest(**_params)
        response = self._boto_client.get_user(**_request.to_boto())

        return shapes.GetUserResponse.from_boto(response)

    def get_user_attribute_verification_code(
        self,
        _request: shapes.GetUserAttributeVerificationCodeRequest = None,
        *,
        access_token: str,
        attribute_name: str,
    ) -> shapes.GetUserAttributeVerificationCodeResponse:
        """
        Gets the user attribute verification code for the specified attribute name.
        """
        if _request is None:
            _params = {}
            if access_token is not ShapeBase.NOT_SET:
                _params['access_token'] = access_token
            if attribute_name is not ShapeBase.NOT_SET:
                _params['attribute_name'] = attribute_name
            _request = shapes.GetUserAttributeVerificationCodeRequest(**_params)
        response = self._boto_client.get_user_attribute_verification_code(
            **_request.to_boto()
        )

        return shapes.GetUserAttributeVerificationCodeResponse.from_boto(
            response
        )

    def get_user_pool_mfa_config(
        self,
        _request: shapes.GetUserPoolMfaConfigRequest = None,
        *,
        user_pool_id: str,
    ) -> shapes.GetUserPoolMfaConfigResponse:
        """
        Gets the user pool multi-factor authentication (MFA) configuration.
        """
        if _request is None:
            _params = {}
            if user_pool_id is not ShapeBase.NOT_SET:
                _params['user_pool_id'] = user_pool_id
            _request = shapes.GetUserPoolMfaConfigRequest(**_params)
        response = self._boto_client.get_user_pool_mfa_config(
            **_request.to_boto()
        )

        return shapes.GetUserPoolMfaConfigResponse.from_boto(response)

    def global_sign_out(
        self,
        _request: shapes.GlobalSignOutRequest = None,
        *,
        access_token: str,
    ) -> shapes.GlobalSignOutResponse:
        """
        Signs out users from all devices.
        """
        if _request is None:
            _params = {}
            if access_token is not ShapeBase.NOT_SET:
                _params['access_token'] = access_token
            _request = shapes.GlobalSignOutRequest(**_params)
        response = self._boto_client.global_sign_out(**_request.to_boto())

        return shapes.GlobalSignOutResponse.from_boto(response)

    def initiate_auth(
        self,
        _request: shapes.InitiateAuthRequest = None,
        *,
        auth_flow: typing.Union[str, shapes.AuthFlowType],
        client_id: str,
        auth_parameters: typing.Dict[str, str] = ShapeBase.NOT_SET,
        client_metadata: typing.Dict[str, str] = ShapeBase.NOT_SET,
        analytics_metadata: shapes.AnalyticsMetadataType = ShapeBase.NOT_SET,
        user_context_data: shapes.UserContextDataType = ShapeBase.NOT_SET,
    ) -> shapes.InitiateAuthResponse:
        """
        Initiates the authentication flow.
        """
        if _request is None:
            _params = {}
            if auth_flow is not ShapeBase.NOT_SET:
                _params['auth_flow'] = auth_flow
            if client_id is not ShapeBase.NOT_SET:
                _params['client_id'] = client_id
            if auth_parameters is not ShapeBase.NOT_SET:
                _params['auth_parameters'] = auth_parameters
            if client_metadata is not ShapeBase.NOT_SET:
                _params['client_metadata'] = client_metadata
            if analytics_metadata is not ShapeBase.NOT_SET:
                _params['analytics_metadata'] = analytics_metadata
            if user_context_data is not ShapeBase.NOT_SET:
                _params['user_context_data'] = user_context_data
            _request = shapes.InitiateAuthRequest(**_params)
        response = self._boto_client.initiate_auth(**_request.to_boto())

        return shapes.InitiateAuthResponse.from_boto(response)

    def list_devices(
        self,
        _request: shapes.ListDevicesRequest = None,
        *,
        access_token: str,
        limit: int = ShapeBase.NOT_SET,
        pagination_token: str = ShapeBase.NOT_SET,
    ) -> shapes.ListDevicesResponse:
        """
        Lists the devices.
        """
        if _request is None:
            _params = {}
            if access_token is not ShapeBase.NOT_SET:
                _params['access_token'] = access_token
            if limit is not ShapeBase.NOT_SET:
                _params['limit'] = limit
            if pagination_token is not ShapeBase.NOT_SET:
                _params['pagination_token'] = pagination_token
            _request = shapes.ListDevicesRequest(**_params)
        response = self._boto_client.list_devices(**_request.to_boto())

        return shapes.ListDevicesResponse.from_boto(response)

    def list_groups(
        self,
        _request: shapes.ListGroupsRequest = None,
        *,
        user_pool_id: str,
        limit: int = ShapeBase.NOT_SET,
        next_token: str = ShapeBase.NOT_SET,
    ) -> shapes.ListGroupsResponse:
        """
        Lists the groups associated with a user pool.

        Requires developer credentials.
        """
        if _request is None:
            _params = {}
            if user_pool_id is not ShapeBase.NOT_SET:
                _params['user_pool_id'] = user_pool_id
            if limit is not ShapeBase.NOT_SET:
                _params['limit'] = limit
            if next_token is not ShapeBase.NOT_SET:
                _params['next_token'] = next_token
            _request = shapes.ListGroupsRequest(**_params)
        response = self._boto_client.list_groups(**_request.to_boto())

        return shapes.ListGroupsResponse.from_boto(response)

    def list_identity_providers(
        self,
        _request: shapes.ListIdentityProvidersRequest = None,
        *,
        user_pool_id: str,
        max_results: int = ShapeBase.NOT_SET,
        next_token: str = ShapeBase.NOT_SET,
    ) -> shapes.ListIdentityProvidersResponse:
        """
        Lists information about all identity providers for a user pool.
        """
        if _request is None:
            _params = {}
            if user_pool_id is not ShapeBase.NOT_SET:
                _params['user_pool_id'] = user_pool_id
            if max_results is not ShapeBase.NOT_SET:
                _params['max_results'] = max_results
            if next_token is not ShapeBase.NOT_SET:
                _params['next_token'] = next_token
            _request = shapes.ListIdentityProvidersRequest(**_params)
        response = self._boto_client.list_identity_providers(
            **_request.to_boto()
        )

        return shapes.ListIdentityProvidersResponse.from_boto(response)

    def list_resource_servers(
        self,
        _request: shapes.ListResourceServersRequest = None,
        *,
        user_pool_id: str,
        max_results: int = ShapeBase.NOT_SET,
        next_token: str = ShapeBase.NOT_SET,
    ) -> shapes.ListResourceServersResponse:
        """
        Lists the resource servers for a user pool.
        """
        if _request is None:
            _params = {}
            if user_pool_id is not ShapeBase.NOT_SET:
                _params['user_pool_id'] = user_pool_id
            if max_results is not ShapeBase.NOT_SET:
                _params['max_results'] = max_results
            if next_token is not ShapeBase.NOT_SET:
                _params['next_token'] = next_token
            _request = shapes.ListResourceServersRequest(**_params)
        response = self._boto_client.list_resource_servers(**_request.to_boto())

        return shapes.ListResourceServersResponse.from_boto(response)

    def list_user_import_jobs(
        self,
        _request: shapes.ListUserImportJobsRequest = None,
        *,
        user_pool_id: str,
        max_results: int,
        pagination_token: str = ShapeBase.NOT_SET,
    ) -> shapes.ListUserImportJobsResponse:
        """
        Lists the user import jobs.
        """
        if _request is None:
            _params = {}
            if user_pool_id is not ShapeBase.NOT_SET:
                _params['user_pool_id'] = user_pool_id
            if max_results is not ShapeBase.NOT_SET:
                _params['max_results'] = max_results
            if pagination_token is not ShapeBase.NOT_SET:
                _params['pagination_token'] = pagination_token
            _request = shapes.ListUserImportJobsRequest(**_params)
        response = self._boto_client.list_user_import_jobs(**_request.to_boto())

        return shapes.ListUserImportJobsResponse.from_boto(response)

    def list_user_pool_clients(
        self,
        _request: shapes.ListUserPoolClientsRequest = None,
        *,
        user_pool_id: str,
        max_results: int = ShapeBase.NOT_SET,
        next_token: str = ShapeBase.NOT_SET,
    ) -> shapes.ListUserPoolClientsResponse:
        """
        Lists the clients that have been created for the specified user pool.
        """
        if _request is None:
            _params = {}
            if user_pool_id is not ShapeBase.NOT_SET:
                _params['user_pool_id'] = user_pool_id
            if max_results is not ShapeBase.NOT_SET:
                _params['max_results'] = max_results
            if next_token is not ShapeBase.NOT_SET:
                _params['next_token'] = next_token
            _request = shapes.ListUserPoolClientsRequest(**_params)
        response = self._boto_client.list_user_pool_clients(
            **_request.to_boto()
        )

        return shapes.ListUserPoolClientsResponse.from_boto(response)

    def list_user_pools(
        self,
        _request: shapes.ListUserPoolsRequest = None,
        *,
        max_results: int,
        next_token: str = ShapeBase.NOT_SET,
    ) -> shapes.ListUserPoolsResponse:
        """
        Lists the user pools associated with an AWS account.
        """
        if _request is None:
            _params = {}
            if max_results is not ShapeBase.NOT_SET:
                _params['max_results'] = max_results
            if next_token is not ShapeBase.NOT_SET:
                _params['next_token'] = next_token
            _request = shapes.ListUserPoolsRequest(**_params)
        response = self._boto_client.list_user_pools(**_request.to_boto())

        return shapes.ListUserPoolsResponse.from_boto(response)

    def list_users(
        self,
        _request: shapes.ListUsersRequest = None,
        *,
        user_pool_id: str,
        attributes_to_get: typing.List[str] = ShapeBase.NOT_SET,
        limit: int = ShapeBase.NOT_SET,
        pagination_token: str = ShapeBase.NOT_SET,
        filter: str = ShapeBase.NOT_SET,
    ) -> shapes.ListUsersResponse:
        """
        Lists the users in the Amazon Cognito user pool.
        """
        if _request is None:
            _params = {}
            if user_pool_id is not ShapeBase.NOT_SET:
                _params['user_pool_id'] = user_pool_id
            if attributes_to_get is not ShapeBase.NOT_SET:
                _params['attributes_to_get'] = attributes_to_get
            if limit is not ShapeBase.NOT_SET:
                _params['limit'] = limit
            if pagination_token is not ShapeBase.NOT_SET:
                _params['pagination_token'] = pagination_token
            if filter is not ShapeBase.NOT_SET:
                _params['filter'] = filter
            _request = shapes.ListUsersRequest(**_params)
        response = self._boto_client.list_users(**_request.to_boto())

        return shapes.ListUsersResponse.from_boto(response)

    def list_users_in_group(
        self,
        _request: shapes.ListUsersInGroupRequest = None,
        *,
        user_pool_id: str,
        group_name: str,
        limit: int = ShapeBase.NOT_SET,
        next_token: str = ShapeBase.NOT_SET,
    ) -> shapes.ListUsersInGroupResponse:
        """
        Lists the users in the specified group.

        Requires developer credentials.
        """
        if _request is None:
            _params = {}
            if user_pool_id is not ShapeBase.NOT_SET:
                _params['user_pool_id'] = user_pool_id
            if group_name is not ShapeBase.NOT_SET:
                _params['group_name'] = group_name
            if limit is not ShapeBase.NOT_SET:
                _params['limit'] = limit
            if next_token is not ShapeBase.NOT_SET:
                _params['next_token'] = next_token
            _request = shapes.ListUsersInGroupRequest(**_params)
        response = self._boto_client.list_users_in_group(**_request.to_boto())

        return shapes.ListUsersInGroupResponse.from_boto(response)

    def resend_confirmation_code(
        self,
        _request: shapes.ResendConfirmationCodeRequest = None,
        *,
        client_id: str,
        username: str,
        secret_hash: str = ShapeBase.NOT_SET,
        user_context_data: shapes.UserContextDataType = ShapeBase.NOT_SET,
        analytics_metadata: shapes.AnalyticsMetadataType = ShapeBase.NOT_SET,
    ) -> shapes.ResendConfirmationCodeResponse:
        """
        Resends the confirmation (for confirmation of registration) to a specific user
        in the user pool.
        """
        if _request is None:
            _params = {}
            if client_id is not ShapeBase.NOT_SET:
                _params['client_id'] = client_id
            if username is not ShapeBase.NOT_SET:
                _params['username'] = username
            if secret_hash is not ShapeBase.NOT_SET:
                _params['secret_hash'] = secret_hash
            if user_context_data is not ShapeBase.NOT_SET:
                _params['user_context_data'] = user_context_data
            if analytics_metadata is not ShapeBase.NOT_SET:
                _params['analytics_metadata'] = analytics_metadata
            _request = shapes.ResendConfirmationCodeRequest(**_params)
        response = self._boto_client.resend_confirmation_code(
            **_request.to_boto()
        )

        return shapes.ResendConfirmationCodeResponse.from_boto(response)

    def respond_to_auth_challenge(
        self,
        _request: shapes.RespondToAuthChallengeRequest = None,
        *,
        client_id: str,
        challenge_name: typing.Union[str, shapes.ChallengeNameType],
        session: str = ShapeBase.NOT_SET,
        challenge_responses: typing.Dict[str, str] = ShapeBase.NOT_SET,
        analytics_metadata: shapes.AnalyticsMetadataType = ShapeBase.NOT_SET,
        user_context_data: shapes.UserContextDataType = ShapeBase.NOT_SET,
    ) -> shapes.RespondToAuthChallengeResponse:
        """
        Responds to the authentication challenge.
        """
        if _request is None:
            _params = {}
            if client_id is not ShapeBase.NOT_SET:
                _params['client_id'] = client_id
            if challenge_name is not ShapeBase.NOT_SET:
                _params['challenge_name'] = challenge_name
            if session is not ShapeBase.NOT_SET:
                _params['session'] = session
            if challenge_responses is not ShapeBase.NOT_SET:
                _params['challenge_responses'] = challenge_responses
            if analytics_metadata is not ShapeBase.NOT_SET:
                _params['analytics_metadata'] = analytics_metadata
            if user_context_data is not ShapeBase.NOT_SET:
                _params['user_context_data'] = user_context_data
            _request = shapes.RespondToAuthChallengeRequest(**_params)
        response = self._boto_client.respond_to_auth_challenge(
            **_request.to_boto()
        )

        return shapes.RespondToAuthChallengeResponse.from_boto(response)

    def set_risk_configuration(
        self,
        _request: shapes.SetRiskConfigurationRequest = None,
        *,
        user_pool_id: str,
        client_id: str = ShapeBase.NOT_SET,
        compromised_credentials_risk_configuration: shapes.
        CompromisedCredentialsRiskConfigurationType = ShapeBase.NOT_SET,
        account_takeover_risk_configuration: shapes.
        AccountTakeoverRiskConfigurationType = ShapeBase.NOT_SET,
        risk_exception_configuration: shapes.
        RiskExceptionConfigurationType = ShapeBase.NOT_SET,
    ) -> shapes.SetRiskConfigurationResponse:
        """
        Configures actions on detected risks. To delete the risk configuration for
        `UserPoolId` or `ClientId`, pass null values for all four configuration types.

        To enable Amazon Cognito advanced security features, update the user pool to
        include the `UserPoolAddOns` key`AdvancedSecurityMode`.

        See .
        """
        if _request is None:
            _params = {}
            if user_pool_id is not ShapeBase.NOT_SET:
                _params['user_pool_id'] = user_pool_id
            if client_id is not ShapeBase.NOT_SET:
                _params['client_id'] = client_id
            if compromised_credentials_risk_configuration is not ShapeBase.NOT_SET:
                _params['compromised_credentials_risk_configuration'
                       ] = compromised_credentials_risk_configuration
            if account_takeover_risk_configuration is not ShapeBase.NOT_SET:
                _params['account_takeover_risk_configuration'
                       ] = account_takeover_risk_configuration
            if risk_exception_configuration is not ShapeBase.NOT_SET:
                _params['risk_exception_configuration'
                       ] = risk_exception_configuration
            _request = shapes.SetRiskConfigurationRequest(**_params)
        response = self._boto_client.set_risk_configuration(
            **_request.to_boto()
        )

        return shapes.SetRiskConfigurationResponse.from_boto(response)

    def set_ui_customization(
        self,
        _request: shapes.SetUICustomizationRequest = None,
        *,
        user_pool_id: str,
        client_id: str = ShapeBase.NOT_SET,
        css: str = ShapeBase.NOT_SET,
        image_file: typing.Any = ShapeBase.NOT_SET,
    ) -> shapes.SetUICustomizationResponse:
        """
        Sets the UI customization information for a user pool's built-in app UI.

        You can specify app UI customization settings for a single client (with a
        specific `clientId`) or for all clients (by setting the `clientId` to `ALL`). If
        you specify `ALL`, the default configuration will be used for every client that
        has no UI customization set previously. If you specify UI customization settings
        for a particular client, it will no longer fall back to the `ALL` configuration.

        To use this API, your user pool must have a domain associated with it.
        Otherwise, there is no place to host the app's pages, and the service will throw
        an error.
        """
        if _request is None:
            _params = {}
            if user_pool_id is not ShapeBase.NOT_SET:
                _params['user_pool_id'] = user_pool_id
            if client_id is not ShapeBase.NOT_SET:
                _params['client_id'] = client_id
            if css is not ShapeBase.NOT_SET:
                _params['css'] = css
            if image_file is not ShapeBase.NOT_SET:
                _params['image_file'] = image_file
            _request = shapes.SetUICustomizationRequest(**_params)
        response = self._boto_client.set_ui_customization(**_request.to_boto())

        return shapes.SetUICustomizationResponse.from_boto(response)

    def set_user_mfa_preference(
        self,
        _request: shapes.SetUserMFAPreferenceRequest = None,
        *,
        access_token: str,
        sms_mfa_settings: shapes.SMSMfaSettingsType = ShapeBase.NOT_SET,
        software_token_mfa_settings: shapes.
        SoftwareTokenMfaSettingsType = ShapeBase.NOT_SET,
    ) -> shapes.SetUserMFAPreferenceResponse:
        """
        Set the user's multi-factor authentication (MFA) method preference.
        """
        if _request is None:
            _params = {}
            if access_token is not ShapeBase.NOT_SET:
                _params['access_token'] = access_token
            if sms_mfa_settings is not ShapeBase.NOT_SET:
                _params['sms_mfa_settings'] = sms_mfa_settings
            if software_token_mfa_settings is not ShapeBase.NOT_SET:
                _params['software_token_mfa_settings'
                       ] = software_token_mfa_settings
            _request = shapes.SetUserMFAPreferenceRequest(**_params)
        response = self._boto_client.set_user_mfa_preference(
            **_request.to_boto()
        )

        return shapes.SetUserMFAPreferenceResponse.from_boto(response)

    def set_user_pool_mfa_config(
        self,
        _request: shapes.SetUserPoolMfaConfigRequest = None,
        *,
        user_pool_id: str,
        sms_mfa_configuration: shapes.SmsMfaConfigType = ShapeBase.NOT_SET,
        software_token_mfa_configuration: shapes.
        SoftwareTokenMfaConfigType = ShapeBase.NOT_SET,
        mfa_configuration: typing.Union[str, shapes.
                                        UserPoolMfaType] = ShapeBase.NOT_SET,
    ) -> shapes.SetUserPoolMfaConfigResponse:
        """
        Set the user pool MFA configuration.
        """
        if _request is None:
            _params = {}
            if user_pool_id is not ShapeBase.NOT_SET:
                _params['user_pool_id'] = user_pool_id
            if sms_mfa_configuration is not ShapeBase.NOT_SET:
                _params['sms_mfa_configuration'] = sms_mfa_configuration
            if software_token_mfa_configuration is not ShapeBase.NOT_SET:
                _params['software_token_mfa_configuration'
                       ] = software_token_mfa_configuration
            if mfa_configuration is not ShapeBase.NOT_SET:
                _params['mfa_configuration'] = mfa_configuration
            _request = shapes.SetUserPoolMfaConfigRequest(**_params)
        response = self._boto_client.set_user_pool_mfa_config(
            **_request.to_boto()
        )

        return shapes.SetUserPoolMfaConfigResponse.from_boto(response)

    def set_user_settings(
        self,
        _request: shapes.SetUserSettingsRequest = None,
        *,
        access_token: str,
        mfa_options: typing.List[shapes.MFAOptionType],
    ) -> shapes.SetUserSettingsResponse:
        """
        Sets the user settings like multi-factor authentication (MFA). If MFA is to be
        removed for a particular attribute pass the attribute with code delivery as
        null. If null list is passed, all MFA options are removed.
        """
        if _request is None:
            _params = {}
            if access_token is not ShapeBase.NOT_SET:
                _params['access_token'] = access_token
            if mfa_options is not ShapeBase.NOT_SET:
                _params['mfa_options'] = mfa_options
            _request = shapes.SetUserSettingsRequest(**_params)
        response = self._boto_client.set_user_settings(**_request.to_boto())

        return shapes.SetUserSettingsResponse.from_boto(response)

    def sign_up(
        self,
        _request: shapes.SignUpRequest = None,
        *,
        client_id: str,
        username: str,
        password: str,
        secret_hash: str = ShapeBase.NOT_SET,
        user_attributes: typing.List[shapes.AttributeType] = ShapeBase.NOT_SET,
        validation_data: typing.List[shapes.AttributeType] = ShapeBase.NOT_SET,
        analytics_metadata: shapes.AnalyticsMetadataType = ShapeBase.NOT_SET,
        user_context_data: shapes.UserContextDataType = ShapeBase.NOT_SET,
    ) -> shapes.SignUpResponse:
        """
        Registers the user in the specified user pool and creates a user name, password,
        and user attributes.
        """
        if _request is None:
            _params = {}
            if client_id is not ShapeBase.NOT_SET:
                _params['client_id'] = client_id
            if username is not ShapeBase.NOT_SET:
                _params['username'] = username
            if password is not ShapeBase.NOT_SET:
                _params['password'] = password
            if secret_hash is not ShapeBase.NOT_SET:
                _params['secret_hash'] = secret_hash
            if user_attributes is not ShapeBase.NOT_SET:
                _params['user_attributes'] = user_attributes
            if validation_data is not ShapeBase.NOT_SET:
                _params['validation_data'] = validation_data
            if analytics_metadata is not ShapeBase.NOT_SET:
                _params['analytics_metadata'] = analytics_metadata
            if user_context_data is not ShapeBase.NOT_SET:
                _params['user_context_data'] = user_context_data
            _request = shapes.SignUpRequest(**_params)
        response = self._boto_client.sign_up(**_request.to_boto())

        return shapes.SignUpResponse.from_boto(response)

    def start_user_import_job(
        self,
        _request: shapes.StartUserImportJobRequest = None,
        *,
        user_pool_id: str,
        job_id: str,
    ) -> shapes.StartUserImportJobResponse:
        """
        Starts the user import.
        """
        if _request is None:
            _params = {}
            if user_pool_id is not ShapeBase.NOT_SET:
                _params['user_pool_id'] = user_pool_id
            if job_id is not ShapeBase.NOT_SET:
                _params['job_id'] = job_id
            _request = shapes.StartUserImportJobRequest(**_params)
        response = self._boto_client.start_user_import_job(**_request.to_boto())

        return shapes.StartUserImportJobResponse.from_boto(response)

    def stop_user_import_job(
        self,
        _request: shapes.StopUserImportJobRequest = None,
        *,
        user_pool_id: str,
        job_id: str,
    ) -> shapes.StopUserImportJobResponse:
        """
        Stops the user import job.
        """
        if _request is None:
            _params = {}
            if user_pool_id is not ShapeBase.NOT_SET:
                _params['user_pool_id'] = user_pool_id
            if job_id is not ShapeBase.NOT_SET:
                _params['job_id'] = job_id
            _request = shapes.StopUserImportJobRequest(**_params)
        response = self._boto_client.stop_user_import_job(**_request.to_boto())

        return shapes.StopUserImportJobResponse.from_boto(response)

    def update_auth_event_feedback(
        self,
        _request: shapes.UpdateAuthEventFeedbackRequest = None,
        *,
        user_pool_id: str,
        username: str,
        event_id: str,
        feedback_token: str,
        feedback_value: typing.Union[str, shapes.FeedbackValueType],
    ) -> shapes.UpdateAuthEventFeedbackResponse:
        """
        Provides the feedback for an authentication event whether it was from a valid
        user or not. This feedback is used for improving the risk evaluation decision
        for the user pool as part of Amazon Cognito advanced security.
        """
        if _request is None:
            _params = {}
            if user_pool_id is not ShapeBase.NOT_SET:
                _params['user_pool_id'] = user_pool_id
            if username is not ShapeBase.NOT_SET:
                _params['username'] = username
            if event_id is not ShapeBase.NOT_SET:
                _params['event_id'] = event_id
            if feedback_token is not ShapeBase.NOT_SET:
                _params['feedback_token'] = feedback_token
            if feedback_value is not ShapeBase.NOT_SET:
                _params['feedback_value'] = feedback_value
            _request = shapes.UpdateAuthEventFeedbackRequest(**_params)
        response = self._boto_client.update_auth_event_feedback(
            **_request.to_boto()
        )

        return shapes.UpdateAuthEventFeedbackResponse.from_boto(response)

    def update_device_status(
        self,
        _request: shapes.UpdateDeviceStatusRequest = None,
        *,
        access_token: str,
        device_key: str,
        device_remembered_status: typing.
        Union[str, shapes.DeviceRememberedStatusType] = ShapeBase.NOT_SET,
    ) -> shapes.UpdateDeviceStatusResponse:
        """
        Updates the device status.
        """
        if _request is None:
            _params = {}
            if access_token is not ShapeBase.NOT_SET:
                _params['access_token'] = access_token
            if device_key is not ShapeBase.NOT_SET:
                _params['device_key'] = device_key
            if device_remembered_status is not ShapeBase.NOT_SET:
                _params['device_remembered_status'] = device_remembered_status
            _request = shapes.UpdateDeviceStatusRequest(**_params)
        response = self._boto_client.update_device_status(**_request.to_boto())

        return shapes.UpdateDeviceStatusResponse.from_boto(response)

    def update_group(
        self,
        _request: shapes.UpdateGroupRequest = None,
        *,
        group_name: str,
        user_pool_id: str,
        description: str = ShapeBase.NOT_SET,
        role_arn: str = ShapeBase.NOT_SET,
        precedence: int = ShapeBase.NOT_SET,
    ) -> shapes.UpdateGroupResponse:
        """
        Updates the specified group with the specified attributes.

        Requires developer credentials.
        """
        if _request is None:
            _params = {}
            if group_name is not ShapeBase.NOT_SET:
                _params['group_name'] = group_name
            if user_pool_id is not ShapeBase.NOT_SET:
                _params['user_pool_id'] = user_pool_id
            if description is not ShapeBase.NOT_SET:
                _params['description'] = description
            if role_arn is not ShapeBase.NOT_SET:
                _params['role_arn'] = role_arn
            if precedence is not ShapeBase.NOT_SET:
                _params['precedence'] = precedence
            _request = shapes.UpdateGroupRequest(**_params)
        response = self._boto_client.update_group(**_request.to_boto())

        return shapes.UpdateGroupResponse.from_boto(response)

    def update_identity_provider(
        self,
        _request: shapes.UpdateIdentityProviderRequest = None,
        *,
        user_pool_id: str,
        provider_name: str,
        provider_details: typing.Dict[str, str] = ShapeBase.NOT_SET,
        attribute_mapping: typing.Dict[str, str] = ShapeBase.NOT_SET,
        idp_identifiers: typing.List[str] = ShapeBase.NOT_SET,
    ) -> shapes.UpdateIdentityProviderResponse:
        """
        Updates identity provider information for a user pool.
        """
        if _request is None:
            _params = {}
            if user_pool_id is not ShapeBase.NOT_SET:
                _params['user_pool_id'] = user_pool_id
            if provider_name is not ShapeBase.NOT_SET:
                _params['provider_name'] = provider_name
            if provider_details is not ShapeBase.NOT_SET:
                _params['provider_details'] = provider_details
            if attribute_mapping is not ShapeBase.NOT_SET:
                _params['attribute_mapping'] = attribute_mapping
            if idp_identifiers is not ShapeBase.NOT_SET:
                _params['idp_identifiers'] = idp_identifiers
            _request = shapes.UpdateIdentityProviderRequest(**_params)
        response = self._boto_client.update_identity_provider(
            **_request.to_boto()
        )

        return shapes.UpdateIdentityProviderResponse.from_boto(response)

    def update_resource_server(
        self,
        _request: shapes.UpdateResourceServerRequest = None,
        *,
        user_pool_id: str,
        identifier: str,
        name: str,
        scopes: typing.List[shapes.ResourceServerScopeType] = ShapeBase.NOT_SET,
    ) -> shapes.UpdateResourceServerResponse:
        """
        Updates the name and scopes of resource server. All other fields are read-only.
        """
        if _request is None:
            _params = {}
            if user_pool_id is not ShapeBase.NOT_SET:
                _params['user_pool_id'] = user_pool_id
            if identifier is not ShapeBase.NOT_SET:
                _params['identifier'] = identifier
            if name is not ShapeBase.NOT_SET:
                _params['name'] = name
            if scopes is not ShapeBase.NOT_SET:
                _params['scopes'] = scopes
            _request = shapes.UpdateResourceServerRequest(**_params)
        response = self._boto_client.update_resource_server(
            **_request.to_boto()
        )

        return shapes.UpdateResourceServerResponse.from_boto(response)

    def update_user_attributes(
        self,
        _request: shapes.UpdateUserAttributesRequest = None,
        *,
        user_attributes: typing.List[shapes.AttributeType],
        access_token: str,
    ) -> shapes.UpdateUserAttributesResponse:
        """
        Allows a user to update a specific attribute (one at a time).
        """
        if _request is None:
            _params = {}
            if user_attributes is not ShapeBase.NOT_SET:
                _params['user_attributes'] = user_attributes
            if access_token is not ShapeBase.NOT_SET:
                _params['access_token'] = access_token
            _request = shapes.UpdateUserAttributesRequest(**_params)
        response = self._boto_client.update_user_attributes(
            **_request.to_boto()
        )

        return shapes.UpdateUserAttributesResponse.from_boto(response)

    def update_user_pool(
        self,
        _request: shapes.UpdateUserPoolRequest = None,
        *,
        user_pool_id: str,
        policies: shapes.UserPoolPolicyType = ShapeBase.NOT_SET,
        lambda_config: shapes.LambdaConfigType = ShapeBase.NOT_SET,
        auto_verified_attributes: typing.List[
            typing.Union[str, shapes.VerifiedAttributeType]
        ] = ShapeBase.NOT_SET,
        sms_verification_message: str = ShapeBase.NOT_SET,
        email_verification_message: str = ShapeBase.NOT_SET,
        email_verification_subject: str = ShapeBase.NOT_SET,
        verification_message_template: shapes.
        VerificationMessageTemplateType = ShapeBase.NOT_SET,
        sms_authentication_message: str = ShapeBase.NOT_SET,
        mfa_configuration: typing.Union[str, shapes.
                                        UserPoolMfaType] = ShapeBase.NOT_SET,
        device_configuration: shapes.DeviceConfigurationType = ShapeBase.
        NOT_SET,
        email_configuration: shapes.EmailConfigurationType = ShapeBase.NOT_SET,
        sms_configuration: shapes.SmsConfigurationType = ShapeBase.NOT_SET,
        user_pool_tags: typing.Dict[str, str] = ShapeBase.NOT_SET,
        admin_create_user_config: shapes.AdminCreateUserConfigType = ShapeBase.
        NOT_SET,
        user_pool_add_ons: shapes.UserPoolAddOnsType = ShapeBase.NOT_SET,
    ) -> shapes.UpdateUserPoolResponse:
        """
        Updates the specified user pool with the specified attributes. If you don't
        provide a value for an attribute, it will be set to the default value. You can
        get a list of the current user pool settings with .
        """
        if _request is None:
            _params = {}
            if user_pool_id is not ShapeBase.NOT_SET:
                _params['user_pool_id'] = user_pool_id
            if policies is not ShapeBase.NOT_SET:
                _params['policies'] = policies
            if lambda_config is not ShapeBase.NOT_SET:
                _params['lambda_config'] = lambda_config
            if auto_verified_attributes is not ShapeBase.NOT_SET:
                _params['auto_verified_attributes'] = auto_verified_attributes
            if sms_verification_message is not ShapeBase.NOT_SET:
                _params['sms_verification_message'] = sms_verification_message
            if email_verification_message is not ShapeBase.NOT_SET:
                _params['email_verification_message'
                       ] = email_verification_message
            if email_verification_subject is not ShapeBase.NOT_SET:
                _params['email_verification_subject'
                       ] = email_verification_subject
            if verification_message_template is not ShapeBase.NOT_SET:
                _params['verification_message_template'
                       ] = verification_message_template
            if sms_authentication_message is not ShapeBase.NOT_SET:
                _params['sms_authentication_message'
                       ] = sms_authentication_message
            if mfa_configuration is not ShapeBase.NOT_SET:
                _params['mfa_configuration'] = mfa_configuration
            if device_configuration is not ShapeBase.NOT_SET:
                _params['device_configuration'] = device_configuration
            if email_configuration is not ShapeBase.NOT_SET:
                _params['email_configuration'] = email_configuration
            if sms_configuration is not ShapeBase.NOT_SET:
                _params['sms_configuration'] = sms_configuration
            if user_pool_tags is not ShapeBase.NOT_SET:
                _params['user_pool_tags'] = user_pool_tags
            if admin_create_user_config is not ShapeBase.NOT_SET:
                _params['admin_create_user_config'] = admin_create_user_config
            if user_pool_add_ons is not ShapeBase.NOT_SET:
                _params['user_pool_add_ons'] = user_pool_add_ons
            _request = shapes.UpdateUserPoolRequest(**_params)
        response = self._boto_client.update_user_pool(**_request.to_boto())

        return shapes.UpdateUserPoolResponse.from_boto(response)

    def update_user_pool_client(
        self,
        _request: shapes.UpdateUserPoolClientRequest = None,
        *,
        user_pool_id: str,
        client_id: str,
        client_name: str = ShapeBase.NOT_SET,
        refresh_token_validity: int = ShapeBase.NOT_SET,
        read_attributes: typing.List[str] = ShapeBase.NOT_SET,
        write_attributes: typing.List[str] = ShapeBase.NOT_SET,
        explicit_auth_flows: typing.List[typing.Union[str, shapes.
                                                      ExplicitAuthFlowsType]
                                        ] = ShapeBase.NOT_SET,
        supported_identity_providers: typing.List[str] = ShapeBase.NOT_SET,
        callback_urls: typing.List[str] = ShapeBase.NOT_SET,
        logout_urls: typing.List[str] = ShapeBase.NOT_SET,
        default_redirect_uri: str = ShapeBase.NOT_SET,
        allowed_o_auth_flows: typing.List[
            typing.Union[str, shapes.OAuthFlowType]] = ShapeBase.NOT_SET,
        allowed_o_auth_scopes: typing.List[str] = ShapeBase.NOT_SET,
        allowed_o_auth_flows_user_pool_client: bool = ShapeBase.NOT_SET,
        analytics_configuration: shapes.AnalyticsConfigurationType = ShapeBase.
        NOT_SET,
    ) -> shapes.UpdateUserPoolClientResponse:
        """
        Updates the specified user pool app client with the specified attributes. If you
        don't provide a value for an attribute, it will be set to the default value. You
        can get a list of the current user pool app client settings with .
        """
        if _request is None:
            _params = {}
            if user_pool_id is not ShapeBase.NOT_SET:
                _params['user_pool_id'] = user_pool_id
            if client_id is not ShapeBase.NOT_SET:
                _params['client_id'] = client_id
            if client_name is not ShapeBase.NOT_SET:
                _params['client_name'] = client_name
            if refresh_token_validity is not ShapeBase.NOT_SET:
                _params['refresh_token_validity'] = refresh_token_validity
            if read_attributes is not ShapeBase.NOT_SET:
                _params['read_attributes'] = read_attributes
            if write_attributes is not ShapeBase.NOT_SET:
                _params['write_attributes'] = write_attributes
            if explicit_auth_flows is not ShapeBase.NOT_SET:
                _params['explicit_auth_flows'] = explicit_auth_flows
            if supported_identity_providers is not ShapeBase.NOT_SET:
                _params['supported_identity_providers'
                       ] = supported_identity_providers
            if callback_urls is not ShapeBase.NOT_SET:
                _params['callback_urls'] = callback_urls
            if logout_urls is not ShapeBase.NOT_SET:
                _params['logout_urls'] = logout_urls
            if default_redirect_uri is not ShapeBase.NOT_SET:
                _params['default_redirect_uri'] = default_redirect_uri
            if allowed_o_auth_flows is not ShapeBase.NOT_SET:
                _params['allowed_o_auth_flows'] = allowed_o_auth_flows
            if allowed_o_auth_scopes is not ShapeBase.NOT_SET:
                _params['allowed_o_auth_scopes'] = allowed_o_auth_scopes
            if allowed_o_auth_flows_user_pool_client is not ShapeBase.NOT_SET:
                _params['allowed_o_auth_flows_user_pool_client'
                       ] = allowed_o_auth_flows_user_pool_client
            if analytics_configuration is not ShapeBase.NOT_SET:
                _params['analytics_configuration'] = analytics_configuration
            _request = shapes.UpdateUserPoolClientRequest(**_params)
        response = self._boto_client.update_user_pool_client(
            **_request.to_boto()
        )

        return shapes.UpdateUserPoolClientResponse.from_boto(response)

    def verify_software_token(
        self,
        _request: shapes.VerifySoftwareTokenRequest = None,
        *,
        user_code: str,
        access_token: str = ShapeBase.NOT_SET,
        session: str = ShapeBase.NOT_SET,
        friendly_device_name: str = ShapeBase.NOT_SET,
    ) -> shapes.VerifySoftwareTokenResponse:
        """
        Use this API to register a user's entered TOTP code and mark the user's software
        token MFA status as "verified" if successful. The request takes an access token
        or a session string, but not both.
        """
        if _request is None:
            _params = {}
            if user_code is not ShapeBase.NOT_SET:
                _params['user_code'] = user_code
            if access_token is not ShapeBase.NOT_SET:
                _params['access_token'] = access_token
            if session is not ShapeBase.NOT_SET:
                _params['session'] = session
            if friendly_device_name is not ShapeBase.NOT_SET:
                _params['friendly_device_name'] = friendly_device_name
            _request = shapes.VerifySoftwareTokenRequest(**_params)
        response = self._boto_client.verify_software_token(**_request.to_boto())

        return shapes.VerifySoftwareTokenResponse.from_boto(response)

    def verify_user_attribute(
        self,
        _request: shapes.VerifyUserAttributeRequest = None,
        *,
        access_token: str,
        attribute_name: str,
        code: str,
    ) -> shapes.VerifyUserAttributeResponse:
        """
        Verifies the specified user attributes in the user pool.
        """
        if _request is None:
            _params = {}
            if access_token is not ShapeBase.NOT_SET:
                _params['access_token'] = access_token
            if attribute_name is not ShapeBase.NOT_SET:
                _params['attribute_name'] = attribute_name
            if code is not ShapeBase.NOT_SET:
                _params['code'] = code
            _request = shapes.VerifyUserAttributeRequest(**_params)
        response = self._boto_client.verify_user_attribute(**_request.to_boto())

        return shapes.VerifyUserAttributeResponse.from_boto(response)
