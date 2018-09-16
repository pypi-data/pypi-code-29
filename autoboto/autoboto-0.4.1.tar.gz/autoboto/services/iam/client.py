import datetime
import typing
import boto3
from autoboto import ClientBase, ShapeBase, OutputShapeBase
from . import shapes


class Client(ClientBase):
    def __init__(self, *args, **kwargs):
        super().__init__("iam", *args, **kwargs)

    def add_client_id_to_open_id_connect_provider(
        self,
        _request: shapes.AddClientIDToOpenIDConnectProviderRequest = None,
        *,
        open_id_connect_provider_arn: str,
        client_id: str,
    ) -> None:
        """
        Adds a new client ID (also known as audience) to the list of client IDs already
        registered for the specified IAM OpenID Connect (OIDC) provider resource.

        This operation is idempotent; it does not fail or return an error if you add an
        existing client ID to the provider.
        """
        if _request is None:
            _params = {}
            if open_id_connect_provider_arn is not ShapeBase.NOT_SET:
                _params['open_id_connect_provider_arn'
                       ] = open_id_connect_provider_arn
            if client_id is not ShapeBase.NOT_SET:
                _params['client_id'] = client_id
            _request = shapes.AddClientIDToOpenIDConnectProviderRequest(
                **_params
            )
        response = self._boto_client.add_client_id_to_open_id_connect_provider(
            **_request.to_boto()
        )

    def add_role_to_instance_profile(
        self,
        _request: shapes.AddRoleToInstanceProfileRequest = None,
        *,
        instance_profile_name: str,
        role_name: str,
    ) -> None:
        """
        Adds the specified IAM role to the specified instance profile. An instance
        profile can contain only one role, and this limit cannot be increased. You can
        remove the existing role and then add a different role to an instance profile.
        You must then wait for the change to appear across all of AWS because of
        [eventual consistency](https://en.wikipedia.org/wiki/Eventual_consistency). To
        force the change, you must [disassociate the instance
        profile](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DisassociateIamInstanceProfile.html)
        and then [associate the instance
        profile](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_AssociateIamInstanceProfile.html),
        or you can stop your instance and then restart it.

        The caller of this API must be granted the `PassRole` permission on the IAM role
        by a permission policy.

        For more information about roles, go to [Working with
        Roles](http://docs.aws.amazon.com/IAM/latest/UserGuide/WorkingWithRoles.html).
        For more information about instance profiles, go to [About Instance
        Profiles](http://docs.aws.amazon.com/IAM/latest/UserGuide/AboutInstanceProfiles.html).
        """
        if _request is None:
            _params = {}
            if instance_profile_name is not ShapeBase.NOT_SET:
                _params['instance_profile_name'] = instance_profile_name
            if role_name is not ShapeBase.NOT_SET:
                _params['role_name'] = role_name
            _request = shapes.AddRoleToInstanceProfileRequest(**_params)
        response = self._boto_client.add_role_to_instance_profile(
            **_request.to_boto()
        )

    def add_user_to_group(
        self,
        _request: shapes.AddUserToGroupRequest = None,
        *,
        group_name: str,
        user_name: str,
    ) -> None:
        """
        Adds the specified user to the specified group.
        """
        if _request is None:
            _params = {}
            if group_name is not ShapeBase.NOT_SET:
                _params['group_name'] = group_name
            if user_name is not ShapeBase.NOT_SET:
                _params['user_name'] = user_name
            _request = shapes.AddUserToGroupRequest(**_params)
        response = self._boto_client.add_user_to_group(**_request.to_boto())

    def attach_group_policy(
        self,
        _request: shapes.AttachGroupPolicyRequest = None,
        *,
        group_name: str,
        policy_arn: str,
    ) -> None:
        """
        Attaches the specified managed policy to the specified IAM group.

        You use this API to attach a managed policy to a group. To embed an inline
        policy in a group, use PutGroupPolicy.

        For more information about policies, see [Managed Policies and Inline
        Policies](http://docs.aws.amazon.com/IAM/latest/UserGuide/policies-managed-vs-
        inline.html) in the _IAM User Guide_.
        """
        if _request is None:
            _params = {}
            if group_name is not ShapeBase.NOT_SET:
                _params['group_name'] = group_name
            if policy_arn is not ShapeBase.NOT_SET:
                _params['policy_arn'] = policy_arn
            _request = shapes.AttachGroupPolicyRequest(**_params)
        response = self._boto_client.attach_group_policy(**_request.to_boto())

    def attach_role_policy(
        self,
        _request: shapes.AttachRolePolicyRequest = None,
        *,
        role_name: str,
        policy_arn: str,
    ) -> None:
        """
        Attaches the specified managed policy to the specified IAM role. When you attach
        a managed policy to a role, the managed policy becomes part of the role's
        permission (access) policy.

        You cannot use a managed policy as the role's trust policy. The role's trust
        policy is created at the same time as the role, using CreateRole. You can update
        a role's trust policy using UpdateAssumeRolePolicy.

        Use this API to attach a _managed_ policy to a role. To embed an inline policy
        in a role, use PutRolePolicy. For more information about policies, see [Managed
        Policies and Inline
        Policies](http://docs.aws.amazon.com/IAM/latest/UserGuide/policies-managed-vs-
        inline.html) in the _IAM User Guide_.
        """
        if _request is None:
            _params = {}
            if role_name is not ShapeBase.NOT_SET:
                _params['role_name'] = role_name
            if policy_arn is not ShapeBase.NOT_SET:
                _params['policy_arn'] = policy_arn
            _request = shapes.AttachRolePolicyRequest(**_params)
        response = self._boto_client.attach_role_policy(**_request.to_boto())

    def attach_user_policy(
        self,
        _request: shapes.AttachUserPolicyRequest = None,
        *,
        user_name: str,
        policy_arn: str,
    ) -> None:
        """
        Attaches the specified managed policy to the specified user.

        You use this API to attach a _managed_ policy to a user. To embed an inline
        policy in a user, use PutUserPolicy.

        For more information about policies, see [Managed Policies and Inline
        Policies](http://docs.aws.amazon.com/IAM/latest/UserGuide/policies-managed-vs-
        inline.html) in the _IAM User Guide_.
        """
        if _request is None:
            _params = {}
            if user_name is not ShapeBase.NOT_SET:
                _params['user_name'] = user_name
            if policy_arn is not ShapeBase.NOT_SET:
                _params['policy_arn'] = policy_arn
            _request = shapes.AttachUserPolicyRequest(**_params)
        response = self._boto_client.attach_user_policy(**_request.to_boto())

    def change_password(
        self,
        _request: shapes.ChangePasswordRequest = None,
        *,
        old_password: str,
        new_password: str,
    ) -> None:
        """
        Changes the password of the IAM user who is calling this operation. The AWS
        account root user password is not affected by this operation.

        To change the password for a different user, see UpdateLoginProfile. For more
        information about modifying passwords, see [Managing
        Passwords](http://docs.aws.amazon.com/IAM/latest/UserGuide/Using_ManagingLogins.html)
        in the _IAM User Guide_.
        """
        if _request is None:
            _params = {}
            if old_password is not ShapeBase.NOT_SET:
                _params['old_password'] = old_password
            if new_password is not ShapeBase.NOT_SET:
                _params['new_password'] = new_password
            _request = shapes.ChangePasswordRequest(**_params)
        response = self._boto_client.change_password(**_request.to_boto())

    def create_access_key(
        self,
        _request: shapes.CreateAccessKeyRequest = None,
        *,
        user_name: str = ShapeBase.NOT_SET,
    ) -> shapes.CreateAccessKeyResponse:
        """
        Creates a new AWS secret access key and corresponding AWS access key ID for the
        specified user. The default status for new keys is `Active`.

        If you do not specify a user name, IAM determines the user name implicitly based
        on the AWS access key ID signing the request. Because this operation works for
        access keys under the AWS account, you can use this operation to manage AWS
        account root user credentials. This is true even if the AWS account has no
        associated users.

        For information about limits on the number of keys you can create, see
        [Limitations on IAM
        Entities](http://docs.aws.amazon.com/IAM/latest/UserGuide/LimitationsOnEntities.html)
        in the _IAM User Guide_.

        To ensure the security of your AWS account, the secret access key is accessible
        only during key and user creation. You must save the key (for example, in a text
        file) if you want to be able to access it again. If a secret key is lost, you
        can delete the access keys for the associated user and then create new keys.
        """
        if _request is None:
            _params = {}
            if user_name is not ShapeBase.NOT_SET:
                _params['user_name'] = user_name
            _request = shapes.CreateAccessKeyRequest(**_params)
        response = self._boto_client.create_access_key(**_request.to_boto())

        return shapes.CreateAccessKeyResponse.from_boto(response)

    def create_account_alias(
        self,
        _request: shapes.CreateAccountAliasRequest = None,
        *,
        account_alias: str,
    ) -> None:
        """
        Creates an alias for your AWS account. For information about using an AWS
        account alias, see [Using an Alias for Your AWS Account
        ID](http://docs.aws.amazon.com/IAM/latest/UserGuide/AccountAlias.html) in the
        _IAM User Guide_.
        """
        if _request is None:
            _params = {}
            if account_alias is not ShapeBase.NOT_SET:
                _params['account_alias'] = account_alias
            _request = shapes.CreateAccountAliasRequest(**_params)
        response = self._boto_client.create_account_alias(**_request.to_boto())

    def create_group(
        self,
        _request: shapes.CreateGroupRequest = None,
        *,
        group_name: str,
        path: str = ShapeBase.NOT_SET,
    ) -> shapes.CreateGroupResponse:
        """
        Creates a new group.

        For information about the number of groups you can create, see [Limitations on
        IAM
        Entities](http://docs.aws.amazon.com/IAM/latest/UserGuide/LimitationsOnEntities.html)
        in the _IAM User Guide_.
        """
        if _request is None:
            _params = {}
            if group_name is not ShapeBase.NOT_SET:
                _params['group_name'] = group_name
            if path is not ShapeBase.NOT_SET:
                _params['path'] = path
            _request = shapes.CreateGroupRequest(**_params)
        response = self._boto_client.create_group(**_request.to_boto())

        return shapes.CreateGroupResponse.from_boto(response)

    def create_instance_profile(
        self,
        _request: shapes.CreateInstanceProfileRequest = None,
        *,
        instance_profile_name: str,
        path: str = ShapeBase.NOT_SET,
    ) -> shapes.CreateInstanceProfileResponse:
        """
        Creates a new instance profile. For information about instance profiles, go to
        [About Instance
        Profiles](http://docs.aws.amazon.com/IAM/latest/UserGuide/AboutInstanceProfiles.html).

        For information about the number of instance profiles you can create, see
        [Limitations on IAM
        Entities](http://docs.aws.amazon.com/IAM/latest/UserGuide/LimitationsOnEntities.html)
        in the _IAM User Guide_.
        """
        if _request is None:
            _params = {}
            if instance_profile_name is not ShapeBase.NOT_SET:
                _params['instance_profile_name'] = instance_profile_name
            if path is not ShapeBase.NOT_SET:
                _params['path'] = path
            _request = shapes.CreateInstanceProfileRequest(**_params)
        response = self._boto_client.create_instance_profile(
            **_request.to_boto()
        )

        return shapes.CreateInstanceProfileResponse.from_boto(response)

    def create_login_profile(
        self,
        _request: shapes.CreateLoginProfileRequest = None,
        *,
        user_name: str,
        password: str,
        password_reset_required: bool = ShapeBase.NOT_SET,
    ) -> shapes.CreateLoginProfileResponse:
        """
        Creates a password for the specified user, giving the user the ability to access
        AWS services through the AWS Management Console. For more information about
        managing passwords, see [Managing
        Passwords](http://docs.aws.amazon.com/IAM/latest/UserGuide/Using_ManagingLogins.html)
        in the _IAM User Guide_.
        """
        if _request is None:
            _params = {}
            if user_name is not ShapeBase.NOT_SET:
                _params['user_name'] = user_name
            if password is not ShapeBase.NOT_SET:
                _params['password'] = password
            if password_reset_required is not ShapeBase.NOT_SET:
                _params['password_reset_required'] = password_reset_required
            _request = shapes.CreateLoginProfileRequest(**_params)
        response = self._boto_client.create_login_profile(**_request.to_boto())

        return shapes.CreateLoginProfileResponse.from_boto(response)

    def create_open_id_connect_provider(
        self,
        _request: shapes.CreateOpenIDConnectProviderRequest = None,
        *,
        url: str,
        thumbprint_list: typing.List[str],
        client_id_list: typing.List[str] = ShapeBase.NOT_SET,
    ) -> shapes.CreateOpenIDConnectProviderResponse:
        """
        Creates an IAM entity to describe an identity provider (IdP) that supports
        [OpenID Connect (OIDC)](http://openid.net/connect/).

        The OIDC provider that you create with this operation can be used as a principal
        in a role's trust policy. Such a policy establishes a trust relationship between
        AWS and the OIDC provider.

        When you create the IAM OIDC provider, you specify the following:

          * The URL of the OIDC identity provider (IdP) to trust

          * A list of client IDs (also known as audiences) that identify the application or applications that are allowed to authenticate using the OIDC provider

          * A list of thumbprints of the server certificate(s) that the IdP uses.

        You get all of this information from the OIDC IdP that you want to use to access
        AWS.

        Because trust for the OIDC provider is derived from the IAM provider that this
        operation creates, it is best to limit access to the CreateOpenIDConnectProvider
        operation to highly privileged users.
        """
        if _request is None:
            _params = {}
            if url is not ShapeBase.NOT_SET:
                _params['url'] = url
            if thumbprint_list is not ShapeBase.NOT_SET:
                _params['thumbprint_list'] = thumbprint_list
            if client_id_list is not ShapeBase.NOT_SET:
                _params['client_id_list'] = client_id_list
            _request = shapes.CreateOpenIDConnectProviderRequest(**_params)
        response = self._boto_client.create_open_id_connect_provider(
            **_request.to_boto()
        )

        return shapes.CreateOpenIDConnectProviderResponse.from_boto(response)

    def create_policy(
        self,
        _request: shapes.CreatePolicyRequest = None,
        *,
        policy_name: str,
        policy_document: str,
        path: str = ShapeBase.NOT_SET,
        description: str = ShapeBase.NOT_SET,
    ) -> shapes.CreatePolicyResponse:
        """
        Creates a new managed policy for your AWS account.

        This operation creates a policy version with a version identifier of `v1` and
        sets v1 as the policy's default version. For more information about policy
        versions, see [Versioning for Managed
        Policies](http://docs.aws.amazon.com/IAM/latest/UserGuide/policies-managed-
        versions.html) in the _IAM User Guide_.

        For more information about managed policies in general, see [Managed Policies
        and Inline Policies](http://docs.aws.amazon.com/IAM/latest/UserGuide/policies-
        managed-vs-inline.html) in the _IAM User Guide_.
        """
        if _request is None:
            _params = {}
            if policy_name is not ShapeBase.NOT_SET:
                _params['policy_name'] = policy_name
            if policy_document is not ShapeBase.NOT_SET:
                _params['policy_document'] = policy_document
            if path is not ShapeBase.NOT_SET:
                _params['path'] = path
            if description is not ShapeBase.NOT_SET:
                _params['description'] = description
            _request = shapes.CreatePolicyRequest(**_params)
        response = self._boto_client.create_policy(**_request.to_boto())

        return shapes.CreatePolicyResponse.from_boto(response)

    def create_policy_version(
        self,
        _request: shapes.CreatePolicyVersionRequest = None,
        *,
        policy_arn: str,
        policy_document: str,
        set_as_default: bool = ShapeBase.NOT_SET,
    ) -> shapes.CreatePolicyVersionResponse:
        """
        Creates a new version of the specified managed policy. To update a managed
        policy, you create a new policy version. A managed policy can have up to five
        versions. If the policy has five versions, you must delete an existing version
        using DeletePolicyVersion before you create a new version.

        Optionally, you can set the new version as the policy's default version. The
        default version is the version that is in effect for the IAM users, groups, and
        roles to which the policy is attached.

        For more information about managed policy versions, see [Versioning for Managed
        Policies](http://docs.aws.amazon.com/IAM/latest/UserGuide/policies-managed-
        versions.html) in the _IAM User Guide_.
        """
        if _request is None:
            _params = {}
            if policy_arn is not ShapeBase.NOT_SET:
                _params['policy_arn'] = policy_arn
            if policy_document is not ShapeBase.NOT_SET:
                _params['policy_document'] = policy_document
            if set_as_default is not ShapeBase.NOT_SET:
                _params['set_as_default'] = set_as_default
            _request = shapes.CreatePolicyVersionRequest(**_params)
        response = self._boto_client.create_policy_version(**_request.to_boto())

        return shapes.CreatePolicyVersionResponse.from_boto(response)

    def create_role(
        self,
        _request: shapes.CreateRoleRequest = None,
        *,
        role_name: str,
        assume_role_policy_document: str,
        path: str = ShapeBase.NOT_SET,
        description: str = ShapeBase.NOT_SET,
        max_session_duration: int = ShapeBase.NOT_SET,
        permissions_boundary: str = ShapeBase.NOT_SET,
    ) -> shapes.CreateRoleResponse:
        """
        Creates a new role for your AWS account. For more information about roles, go to
        [IAM
        Roles](http://docs.aws.amazon.com/IAM/latest/UserGuide/WorkingWithRoles.html).
        For information about limitations on role names and the number of roles you can
        create, go to [Limitations on IAM
        Entities](http://docs.aws.amazon.com/IAM/latest/UserGuide/LimitationsOnEntities.html)
        in the _IAM User Guide_.
        """
        if _request is None:
            _params = {}
            if role_name is not ShapeBase.NOT_SET:
                _params['role_name'] = role_name
            if assume_role_policy_document is not ShapeBase.NOT_SET:
                _params['assume_role_policy_document'
                       ] = assume_role_policy_document
            if path is not ShapeBase.NOT_SET:
                _params['path'] = path
            if description is not ShapeBase.NOT_SET:
                _params['description'] = description
            if max_session_duration is not ShapeBase.NOT_SET:
                _params['max_session_duration'] = max_session_duration
            if permissions_boundary is not ShapeBase.NOT_SET:
                _params['permissions_boundary'] = permissions_boundary
            _request = shapes.CreateRoleRequest(**_params)
        response = self._boto_client.create_role(**_request.to_boto())

        return shapes.CreateRoleResponse.from_boto(response)

    def create_saml_provider(
        self,
        _request: shapes.CreateSAMLProviderRequest = None,
        *,
        saml_metadata_document: str,
        name: str,
    ) -> shapes.CreateSAMLProviderResponse:
        """
        Creates an IAM resource that describes an identity provider (IdP) that supports
        SAML 2.0.

        The SAML provider resource that you create with this operation can be used as a
        principal in an IAM role's trust policy. Such a policy can enable federated
        users who sign-in using the SAML IdP to assume the role. You can create an IAM
        role that supports Web-based single sign-on (SSO) to the AWS Management Console
        or one that supports API access to AWS.

        When you create the SAML provider resource, you upload a SAML metadata document
        that you get from your IdP. That document includes the issuer's name, expiration
        information, and keys that can be used to validate the SAML authentication
        response (assertions) that the IdP sends. You must generate the metadata
        document using the identity management software that is used as your
        organization's IdP.

        This operation requires [Signature Version
        4](http://docs.aws.amazon.com/general/latest/gr/signature-version-4.html).

        For more information, see [Enabling SAML 2.0 Federated Users to Access the AWS
        Management
        Console](http://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_providers_enable-
        console-saml.html) and [About SAML 2.0-based
        Federation](http://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_providers_saml.html)
        in the _IAM User Guide_.
        """
        if _request is None:
            _params = {}
            if saml_metadata_document is not ShapeBase.NOT_SET:
                _params['saml_metadata_document'] = saml_metadata_document
            if name is not ShapeBase.NOT_SET:
                _params['name'] = name
            _request = shapes.CreateSAMLProviderRequest(**_params)
        response = self._boto_client.create_saml_provider(**_request.to_boto())

        return shapes.CreateSAMLProviderResponse.from_boto(response)

    def create_service_linked_role(
        self,
        _request: shapes.CreateServiceLinkedRoleRequest = None,
        *,
        aws_service_name: str,
        description: str = ShapeBase.NOT_SET,
        custom_suffix: str = ShapeBase.NOT_SET,
    ) -> shapes.CreateServiceLinkedRoleResponse:
        """
        Creates an IAM role that is linked to a specific AWS service. The service
        controls the attached policies and when the role can be deleted. This helps
        ensure that the service is not broken by an unexpectedly changed or deleted
        role, which could put your AWS resources into an unknown state. Allowing the
        service to control the role helps improve service stability and proper cleanup
        when a service and its role are no longer needed.

        The name of the role is generated by combining the string that you specify for
        the `AWSServiceName` parameter with the string that you specify for the
        `CustomSuffix` parameter. The resulting name must be unique in your account or
        the request fails.

        To attach a policy to this service-linked role, you must make the request using
        the AWS service that depends on this role.
        """
        if _request is None:
            _params = {}
            if aws_service_name is not ShapeBase.NOT_SET:
                _params['aws_service_name'] = aws_service_name
            if description is not ShapeBase.NOT_SET:
                _params['description'] = description
            if custom_suffix is not ShapeBase.NOT_SET:
                _params['custom_suffix'] = custom_suffix
            _request = shapes.CreateServiceLinkedRoleRequest(**_params)
        response = self._boto_client.create_service_linked_role(
            **_request.to_boto()
        )

        return shapes.CreateServiceLinkedRoleResponse.from_boto(response)

    def create_service_specific_credential(
        self,
        _request: shapes.CreateServiceSpecificCredentialRequest = None,
        *,
        user_name: str,
        service_name: str,
    ) -> shapes.CreateServiceSpecificCredentialResponse:
        """
        Generates a set of credentials consisting of a user name and password that can
        be used to access the service specified in the request. These credentials are
        generated by IAM, and can be used only for the specified service.

        You can have a maximum of two sets of service-specific credentials for each
        supported service per user.

        The only supported service at this time is AWS CodeCommit.

        You can reset the password to a new service-generated value by calling
        ResetServiceSpecificCredential.

        For more information about service-specific credentials, see [Using IAM with AWS
        CodeCommit: Git Credentials, SSH Keys, and AWS Access
        Keys](http://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_ssh-
        keys.html) in the _IAM User Guide_.
        """
        if _request is None:
            _params = {}
            if user_name is not ShapeBase.NOT_SET:
                _params['user_name'] = user_name
            if service_name is not ShapeBase.NOT_SET:
                _params['service_name'] = service_name
            _request = shapes.CreateServiceSpecificCredentialRequest(**_params)
        response = self._boto_client.create_service_specific_credential(
            **_request.to_boto()
        )

        return shapes.CreateServiceSpecificCredentialResponse.from_boto(
            response
        )

    def create_user(
        self,
        _request: shapes.CreateUserRequest = None,
        *,
        user_name: str,
        path: str = ShapeBase.NOT_SET,
        permissions_boundary: str = ShapeBase.NOT_SET,
    ) -> shapes.CreateUserResponse:
        """
        Creates a new IAM user for your AWS account.

        For information about limitations on the number of IAM users you can create, see
        [Limitations on IAM
        Entities](http://docs.aws.amazon.com/IAM/latest/UserGuide/LimitationsOnEntities.html)
        in the _IAM User Guide_.
        """
        if _request is None:
            _params = {}
            if user_name is not ShapeBase.NOT_SET:
                _params['user_name'] = user_name
            if path is not ShapeBase.NOT_SET:
                _params['path'] = path
            if permissions_boundary is not ShapeBase.NOT_SET:
                _params['permissions_boundary'] = permissions_boundary
            _request = shapes.CreateUserRequest(**_params)
        response = self._boto_client.create_user(**_request.to_boto())

        return shapes.CreateUserResponse.from_boto(response)

    def create_virtual_mfa_device(
        self,
        _request: shapes.CreateVirtualMFADeviceRequest = None,
        *,
        virtual_mfa_device_name: str,
        path: str = ShapeBase.NOT_SET,
    ) -> shapes.CreateVirtualMFADeviceResponse:
        """
        Creates a new virtual MFA device for the AWS account. After creating the virtual
        MFA, use EnableMFADevice to attach the MFA device to an IAM user. For more
        information about creating and working with virtual MFA devices, go to [Using a
        Virtual MFA
        Device](http://docs.aws.amazon.com/IAM/latest/UserGuide/Using_VirtualMFA.html)
        in the _IAM User Guide_.

        For information about limits on the number of MFA devices you can create, see
        [Limitations on
        Entities](http://docs.aws.amazon.com/IAM/latest/UserGuide/LimitationsOnEntities.html)
        in the _IAM User Guide_.

        The seed information contained in the QR code and the Base32 string should be
        treated like any other secret access information, such as your AWS access keys
        or your passwords. After you provision your virtual device, you should ensure
        that the information is destroyed following secure procedures.
        """
        if _request is None:
            _params = {}
            if virtual_mfa_device_name is not ShapeBase.NOT_SET:
                _params['virtual_mfa_device_name'] = virtual_mfa_device_name
            if path is not ShapeBase.NOT_SET:
                _params['path'] = path
            _request = shapes.CreateVirtualMFADeviceRequest(**_params)
        response = self._boto_client.create_virtual_mfa_device(
            **_request.to_boto()
        )

        return shapes.CreateVirtualMFADeviceResponse.from_boto(response)

    def deactivate_mfa_device(
        self,
        _request: shapes.DeactivateMFADeviceRequest = None,
        *,
        user_name: str,
        serial_number: str,
    ) -> None:
        """
        Deactivates the specified MFA device and removes it from association with the
        user name for which it was originally enabled.

        For more information about creating and working with virtual MFA devices, go to
        [Using a Virtual MFA
        Device](http://docs.aws.amazon.com/IAM/latest/UserGuide/Using_VirtualMFA.html)
        in the _IAM User Guide_.
        """
        if _request is None:
            _params = {}
            if user_name is not ShapeBase.NOT_SET:
                _params['user_name'] = user_name
            if serial_number is not ShapeBase.NOT_SET:
                _params['serial_number'] = serial_number
            _request = shapes.DeactivateMFADeviceRequest(**_params)
        response = self._boto_client.deactivate_mfa_device(**_request.to_boto())

    def delete_access_key(
        self,
        _request: shapes.DeleteAccessKeyRequest = None,
        *,
        access_key_id: str,
        user_name: str = ShapeBase.NOT_SET,
    ) -> None:
        """
        Deletes the access key pair associated with the specified IAM user.

        If you do not specify a user name, IAM determines the user name implicitly based
        on the AWS access key ID signing the request. Because this operation works for
        access keys under the AWS account, you can use this operation to manage AWS
        account root user credentials even if the AWS account has no associated users.
        """
        if _request is None:
            _params = {}
            if access_key_id is not ShapeBase.NOT_SET:
                _params['access_key_id'] = access_key_id
            if user_name is not ShapeBase.NOT_SET:
                _params['user_name'] = user_name
            _request = shapes.DeleteAccessKeyRequest(**_params)
        response = self._boto_client.delete_access_key(**_request.to_boto())

    def delete_account_alias(
        self,
        _request: shapes.DeleteAccountAliasRequest = None,
        *,
        account_alias: str,
    ) -> None:
        """
        Deletes the specified AWS account alias. For information about using an AWS
        account alias, see [Using an Alias for Your AWS Account
        ID](http://docs.aws.amazon.com/IAM/latest/UserGuide/AccountAlias.html) in the
        _IAM User Guide_.
        """
        if _request is None:
            _params = {}
            if account_alias is not ShapeBase.NOT_SET:
                _params['account_alias'] = account_alias
            _request = shapes.DeleteAccountAliasRequest(**_params)
        response = self._boto_client.delete_account_alias(**_request.to_boto())

    def delete_account_password_policy(self) -> None:
        """
        Deletes the password policy for the AWS account. There are no parameters.
        """
        response = self._boto_client.delete_account_password_policy()

    def delete_group(
        self,
        _request: shapes.DeleteGroupRequest = None,
        *,
        group_name: str,
    ) -> None:
        """
        Deletes the specified IAM group. The group must not contain any users or have
        any attached policies.
        """
        if _request is None:
            _params = {}
            if group_name is not ShapeBase.NOT_SET:
                _params['group_name'] = group_name
            _request = shapes.DeleteGroupRequest(**_params)
        response = self._boto_client.delete_group(**_request.to_boto())

    def delete_group_policy(
        self,
        _request: shapes.DeleteGroupPolicyRequest = None,
        *,
        group_name: str,
        policy_name: str,
    ) -> None:
        """
        Deletes the specified inline policy that is embedded in the specified IAM group.

        A group can also have managed policies attached to it. To detach a managed
        policy from a group, use DetachGroupPolicy. For more information about policies,
        refer to [Managed Policies and Inline
        Policies](http://docs.aws.amazon.com/IAM/latest/UserGuide/policies-managed-vs-
        inline.html) in the _IAM User Guide_.
        """
        if _request is None:
            _params = {}
            if group_name is not ShapeBase.NOT_SET:
                _params['group_name'] = group_name
            if policy_name is not ShapeBase.NOT_SET:
                _params['policy_name'] = policy_name
            _request = shapes.DeleteGroupPolicyRequest(**_params)
        response = self._boto_client.delete_group_policy(**_request.to_boto())

    def delete_instance_profile(
        self,
        _request: shapes.DeleteInstanceProfileRequest = None,
        *,
        instance_profile_name: str,
    ) -> None:
        """
        Deletes the specified instance profile. The instance profile must not have an
        associated role.

        Make sure that you do not have any Amazon EC2 instances running with the
        instance profile you are about to delete. Deleting a role or instance profile
        that is associated with a running instance will break any applications running
        on the instance.

        For more information about instance profiles, go to [About Instance
        Profiles](http://docs.aws.amazon.com/IAM/latest/UserGuide/AboutInstanceProfiles.html).
        """
        if _request is None:
            _params = {}
            if instance_profile_name is not ShapeBase.NOT_SET:
                _params['instance_profile_name'] = instance_profile_name
            _request = shapes.DeleteInstanceProfileRequest(**_params)
        response = self._boto_client.delete_instance_profile(
            **_request.to_boto()
        )

    def delete_login_profile(
        self,
        _request: shapes.DeleteLoginProfileRequest = None,
        *,
        user_name: str,
    ) -> None:
        """
        Deletes the password for the specified IAM user, which terminates the user's
        ability to access AWS services through the AWS Management Console.

        Deleting a user's password does not prevent a user from accessing AWS through
        the command line interface or the API. To prevent all user access you must also
        either make any access keys inactive or delete them. For more information about
        making keys inactive or deleting them, see UpdateAccessKey and DeleteAccessKey.
        """
        if _request is None:
            _params = {}
            if user_name is not ShapeBase.NOT_SET:
                _params['user_name'] = user_name
            _request = shapes.DeleteLoginProfileRequest(**_params)
        response = self._boto_client.delete_login_profile(**_request.to_boto())

    def delete_open_id_connect_provider(
        self,
        _request: shapes.DeleteOpenIDConnectProviderRequest = None,
        *,
        open_id_connect_provider_arn: str,
    ) -> None:
        """
        Deletes an OpenID Connect identity provider (IdP) resource object in IAM.

        Deleting an IAM OIDC provider resource does not update any roles that reference
        the provider as a principal in their trust policies. Any attempt to assume a
        role that references a deleted provider fails.

        This operation is idempotent; it does not fail or return an error if you call
        the operation for a provider that does not exist.
        """
        if _request is None:
            _params = {}
            if open_id_connect_provider_arn is not ShapeBase.NOT_SET:
                _params['open_id_connect_provider_arn'
                       ] = open_id_connect_provider_arn
            _request = shapes.DeleteOpenIDConnectProviderRequest(**_params)
        response = self._boto_client.delete_open_id_connect_provider(
            **_request.to_boto()
        )

    def delete_policy(
        self,
        _request: shapes.DeletePolicyRequest = None,
        *,
        policy_arn: str,
    ) -> None:
        """
        Deletes the specified managed policy.

        Before you can delete a managed policy, you must first detach the policy from
        all users, groups, and roles that it is attached to. In addition you must delete
        all the policy's versions. The following steps describe the process for deleting
        a managed policy:

          * Detach the policy from all users, groups, and roles that the policy is attached to, using the DetachUserPolicy, DetachGroupPolicy, or DetachRolePolicy API operations. To list all the users, groups, and roles that a policy is attached to, use ListEntitiesForPolicy.

          * Delete all versions of the policy using DeletePolicyVersion. To list the policy's versions, use ListPolicyVersions. You cannot use DeletePolicyVersion to delete the version that is marked as the default version. You delete the policy's default version in the next step of the process.

          * Delete the policy (this automatically deletes the policy's default version) using this API.

        For information about managed policies, see [Managed Policies and Inline
        Policies](http://docs.aws.amazon.com/IAM/latest/UserGuide/policies-managed-vs-
        inline.html) in the _IAM User Guide_.
        """
        if _request is None:
            _params = {}
            if policy_arn is not ShapeBase.NOT_SET:
                _params['policy_arn'] = policy_arn
            _request = shapes.DeletePolicyRequest(**_params)
        response = self._boto_client.delete_policy(**_request.to_boto())

    def delete_policy_version(
        self,
        _request: shapes.DeletePolicyVersionRequest = None,
        *,
        policy_arn: str,
        version_id: str,
    ) -> None:
        """
        Deletes the specified version from the specified managed policy.

        You cannot delete the default version from a policy using this API. To delete
        the default version from a policy, use DeletePolicy. To find out which version
        of a policy is marked as the default version, use ListPolicyVersions.

        For information about versions for managed policies, see [Versioning for Managed
        Policies](http://docs.aws.amazon.com/IAM/latest/UserGuide/policies-managed-
        versions.html) in the _IAM User Guide_.
        """
        if _request is None:
            _params = {}
            if policy_arn is not ShapeBase.NOT_SET:
                _params['policy_arn'] = policy_arn
            if version_id is not ShapeBase.NOT_SET:
                _params['version_id'] = version_id
            _request = shapes.DeletePolicyVersionRequest(**_params)
        response = self._boto_client.delete_policy_version(**_request.to_boto())

    def delete_role(
        self,
        _request: shapes.DeleteRoleRequest = None,
        *,
        role_name: str,
    ) -> None:
        """
        Deletes the specified role. The role must not have any policies attached. For
        more information about roles, go to [Working with
        Roles](http://docs.aws.amazon.com/IAM/latest/UserGuide/WorkingWithRoles.html).

        Make sure that you do not have any Amazon EC2 instances running with the role
        you are about to delete. Deleting a role or instance profile that is associated
        with a running instance will break any applications running on the instance.
        """
        if _request is None:
            _params = {}
            if role_name is not ShapeBase.NOT_SET:
                _params['role_name'] = role_name
            _request = shapes.DeleteRoleRequest(**_params)
        response = self._boto_client.delete_role(**_request.to_boto())

    def delete_role_permissions_boundary(
        self,
        _request: shapes.DeleteRolePermissionsBoundaryRequest = None,
        *,
        role_name: str,
    ) -> None:
        """
        Deletes the permissions boundary for the specified IAM role.

        Deleting the permissions boundary for a role might increase its permissions by
        allowing anyone who assumes the role to perform all the actions granted in its
        permissions policies.
        """
        if _request is None:
            _params = {}
            if role_name is not ShapeBase.NOT_SET:
                _params['role_name'] = role_name
            _request = shapes.DeleteRolePermissionsBoundaryRequest(**_params)
        response = self._boto_client.delete_role_permissions_boundary(
            **_request.to_boto()
        )

    def delete_role_policy(
        self,
        _request: shapes.DeleteRolePolicyRequest = None,
        *,
        role_name: str,
        policy_name: str,
    ) -> None:
        """
        Deletes the specified inline policy that is embedded in the specified IAM role.

        A role can also have managed policies attached to it. To detach a managed policy
        from a role, use DetachRolePolicy. For more information about policies, refer to
        [Managed Policies and Inline
        Policies](http://docs.aws.amazon.com/IAM/latest/UserGuide/policies-managed-vs-
        inline.html) in the _IAM User Guide_.
        """
        if _request is None:
            _params = {}
            if role_name is not ShapeBase.NOT_SET:
                _params['role_name'] = role_name
            if policy_name is not ShapeBase.NOT_SET:
                _params['policy_name'] = policy_name
            _request = shapes.DeleteRolePolicyRequest(**_params)
        response = self._boto_client.delete_role_policy(**_request.to_boto())

    def delete_saml_provider(
        self,
        _request: shapes.DeleteSAMLProviderRequest = None,
        *,
        saml_provider_arn: str,
    ) -> None:
        """
        Deletes a SAML provider resource in IAM.

        Deleting the provider resource from IAM does not update any roles that reference
        the SAML provider resource's ARN as a principal in their trust policies. Any
        attempt to assume a role that references a non-existent provider resource ARN
        fails.

        This operation requires [Signature Version
        4](http://docs.aws.amazon.com/general/latest/gr/signature-version-4.html).
        """
        if _request is None:
            _params = {}
            if saml_provider_arn is not ShapeBase.NOT_SET:
                _params['saml_provider_arn'] = saml_provider_arn
            _request = shapes.DeleteSAMLProviderRequest(**_params)
        response = self._boto_client.delete_saml_provider(**_request.to_boto())

    def delete_ssh_public_key(
        self,
        _request: shapes.DeleteSSHPublicKeyRequest = None,
        *,
        user_name: str,
        ssh_public_key_id: str,
    ) -> None:
        """
        Deletes the specified SSH public key.

        The SSH public key deleted by this operation is used only for authenticating the
        associated IAM user to an AWS CodeCommit repository. For more information about
        using SSH keys to authenticate to an AWS CodeCommit repository, see [Set up AWS
        CodeCommit for SSH
        Connections](http://docs.aws.amazon.com/codecommit/latest/userguide/setting-up-
        credentials-ssh.html) in the _AWS CodeCommit User Guide_.
        """
        if _request is None:
            _params = {}
            if user_name is not ShapeBase.NOT_SET:
                _params['user_name'] = user_name
            if ssh_public_key_id is not ShapeBase.NOT_SET:
                _params['ssh_public_key_id'] = ssh_public_key_id
            _request = shapes.DeleteSSHPublicKeyRequest(**_params)
        response = self._boto_client.delete_ssh_public_key(**_request.to_boto())

    def delete_server_certificate(
        self,
        _request: shapes.DeleteServerCertificateRequest = None,
        *,
        server_certificate_name: str,
    ) -> None:
        """
        Deletes the specified server certificate.

        For more information about working with server certificates, see [Working with
        Server
        Certificates](http://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_server-
        certs.html) in the _IAM User Guide_. This topic also includes a list of AWS
        services that can use the server certificates that you manage with IAM.

        If you are using a server certificate with Elastic Load Balancing, deleting the
        certificate could have implications for your application. If Elastic Load
        Balancing doesn't detect the deletion of bound certificates, it may continue to
        use the certificates. This could cause Elastic Load Balancing to stop accepting
        traffic. We recommend that you remove the reference to the certificate from
        Elastic Load Balancing before using this command to delete the certificate. For
        more information, go to
        [DeleteLoadBalancerListeners](http://docs.aws.amazon.com/ElasticLoadBalancing/latest/APIReference/API_DeleteLoadBalancerListeners.html)
        in the _Elastic Load Balancing API Reference_.
        """
        if _request is None:
            _params = {}
            if server_certificate_name is not ShapeBase.NOT_SET:
                _params['server_certificate_name'] = server_certificate_name
            _request = shapes.DeleteServerCertificateRequest(**_params)
        response = self._boto_client.delete_server_certificate(
            **_request.to_boto()
        )

    def delete_service_linked_role(
        self,
        _request: shapes.DeleteServiceLinkedRoleRequest = None,
        *,
        role_name: str,
    ) -> shapes.DeleteServiceLinkedRoleResponse:
        """
        Submits a service-linked role deletion request and returns a `DeletionTaskId`,
        which you can use to check the status of the deletion. Before you call this
        operation, confirm that the role has no active sessions and that any resources
        used by the role in the linked service are deleted. If you call this operation
        more than once for the same service-linked role and an earlier deletion task is
        not complete, then the `DeletionTaskId` of the earlier request is returned.

        If you submit a deletion request for a service-linked role whose linked service
        is still accessing a resource, then the deletion task fails. If it fails, the
        GetServiceLinkedRoleDeletionStatus API operation returns the reason for the
        failure, usually including the resources that must be deleted. To delete the
        service-linked role, you must first remove those resources from the linked
        service and then submit the deletion request again. Resources are specific to
        the service that is linked to the role. For more information about removing
        resources from a service, see the [AWS
        documentation](http://docs.aws.amazon.com/) for your service.

        For more information about service-linked roles, see [Roles Terms and Concepts:
        AWS Service-Linked
        Role](http://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_terms-and-
        concepts.html#iam-term-service-linked-role) in the _IAM User Guide_.
        """
        if _request is None:
            _params = {}
            if role_name is not ShapeBase.NOT_SET:
                _params['role_name'] = role_name
            _request = shapes.DeleteServiceLinkedRoleRequest(**_params)
        response = self._boto_client.delete_service_linked_role(
            **_request.to_boto()
        )

        return shapes.DeleteServiceLinkedRoleResponse.from_boto(response)

    def delete_service_specific_credential(
        self,
        _request: shapes.DeleteServiceSpecificCredentialRequest = None,
        *,
        service_specific_credential_id: str,
        user_name: str = ShapeBase.NOT_SET,
    ) -> None:
        """
        Deletes the specified service-specific credential.
        """
        if _request is None:
            _params = {}
            if service_specific_credential_id is not ShapeBase.NOT_SET:
                _params['service_specific_credential_id'
                       ] = service_specific_credential_id
            if user_name is not ShapeBase.NOT_SET:
                _params['user_name'] = user_name
            _request = shapes.DeleteServiceSpecificCredentialRequest(**_params)
        response = self._boto_client.delete_service_specific_credential(
            **_request.to_boto()
        )

    def delete_signing_certificate(
        self,
        _request: shapes.DeleteSigningCertificateRequest = None,
        *,
        certificate_id: str,
        user_name: str = ShapeBase.NOT_SET,
    ) -> None:
        """
        Deletes a signing certificate associated with the specified IAM user.

        If you do not specify a user name, IAM determines the user name implicitly based
        on the AWS access key ID signing the request. Because this operation works for
        access keys under the AWS account, you can use this operation to manage AWS
        account root user credentials even if the AWS account has no associated IAM
        users.
        """
        if _request is None:
            _params = {}
            if certificate_id is not ShapeBase.NOT_SET:
                _params['certificate_id'] = certificate_id
            if user_name is not ShapeBase.NOT_SET:
                _params['user_name'] = user_name
            _request = shapes.DeleteSigningCertificateRequest(**_params)
        response = self._boto_client.delete_signing_certificate(
            **_request.to_boto()
        )

    def delete_user(
        self,
        _request: shapes.DeleteUserRequest = None,
        *,
        user_name: str,
    ) -> None:
        """
        Deletes the specified IAM user. The user must not belong to any groups or have
        any access keys, signing certificates, or attached policies.
        """
        if _request is None:
            _params = {}
            if user_name is not ShapeBase.NOT_SET:
                _params['user_name'] = user_name
            _request = shapes.DeleteUserRequest(**_params)
        response = self._boto_client.delete_user(**_request.to_boto())

    def delete_user_permissions_boundary(
        self,
        _request: shapes.DeleteUserPermissionsBoundaryRequest = None,
        *,
        user_name: str,
    ) -> None:
        """
        Deletes the permissions boundary for the specified IAM user.

        Deleting the permissions boundary for a user might increase its permissions by
        allowing the user to perform all the actions granted in its permissions
        policies.
        """
        if _request is None:
            _params = {}
            if user_name is not ShapeBase.NOT_SET:
                _params['user_name'] = user_name
            _request = shapes.DeleteUserPermissionsBoundaryRequest(**_params)
        response = self._boto_client.delete_user_permissions_boundary(
            **_request.to_boto()
        )

    def delete_user_policy(
        self,
        _request: shapes.DeleteUserPolicyRequest = None,
        *,
        user_name: str,
        policy_name: str,
    ) -> None:
        """
        Deletes the specified inline policy that is embedded in the specified IAM user.

        A user can also have managed policies attached to it. To detach a managed policy
        from a user, use DetachUserPolicy. For more information about policies, refer to
        [Managed Policies and Inline
        Policies](http://docs.aws.amazon.com/IAM/latest/UserGuide/policies-managed-vs-
        inline.html) in the _IAM User Guide_.
        """
        if _request is None:
            _params = {}
            if user_name is not ShapeBase.NOT_SET:
                _params['user_name'] = user_name
            if policy_name is not ShapeBase.NOT_SET:
                _params['policy_name'] = policy_name
            _request = shapes.DeleteUserPolicyRequest(**_params)
        response = self._boto_client.delete_user_policy(**_request.to_boto())

    def delete_virtual_mfa_device(
        self,
        _request: shapes.DeleteVirtualMFADeviceRequest = None,
        *,
        serial_number: str,
    ) -> None:
        """
        Deletes a virtual MFA device.

        You must deactivate a user's virtual MFA device before you can delete it. For
        information about deactivating MFA devices, see DeactivateMFADevice.
        """
        if _request is None:
            _params = {}
            if serial_number is not ShapeBase.NOT_SET:
                _params['serial_number'] = serial_number
            _request = shapes.DeleteVirtualMFADeviceRequest(**_params)
        response = self._boto_client.delete_virtual_mfa_device(
            **_request.to_boto()
        )

    def detach_group_policy(
        self,
        _request: shapes.DetachGroupPolicyRequest = None,
        *,
        group_name: str,
        policy_arn: str,
    ) -> None:
        """
        Removes the specified managed policy from the specified IAM group.

        A group can also have inline policies embedded with it. To delete an inline
        policy, use the DeleteGroupPolicy API. For information about policies, see
        [Managed Policies and Inline
        Policies](http://docs.aws.amazon.com/IAM/latest/UserGuide/policies-managed-vs-
        inline.html) in the _IAM User Guide_.
        """
        if _request is None:
            _params = {}
            if group_name is not ShapeBase.NOT_SET:
                _params['group_name'] = group_name
            if policy_arn is not ShapeBase.NOT_SET:
                _params['policy_arn'] = policy_arn
            _request = shapes.DetachGroupPolicyRequest(**_params)
        response = self._boto_client.detach_group_policy(**_request.to_boto())

    def detach_role_policy(
        self,
        _request: shapes.DetachRolePolicyRequest = None,
        *,
        role_name: str,
        policy_arn: str,
    ) -> None:
        """
        Removes the specified managed policy from the specified role.

        A role can also have inline policies embedded with it. To delete an inline
        policy, use the DeleteRolePolicy API. For information about policies, see
        [Managed Policies and Inline
        Policies](http://docs.aws.amazon.com/IAM/latest/UserGuide/policies-managed-vs-
        inline.html) in the _IAM User Guide_.
        """
        if _request is None:
            _params = {}
            if role_name is not ShapeBase.NOT_SET:
                _params['role_name'] = role_name
            if policy_arn is not ShapeBase.NOT_SET:
                _params['policy_arn'] = policy_arn
            _request = shapes.DetachRolePolicyRequest(**_params)
        response = self._boto_client.detach_role_policy(**_request.to_boto())

    def detach_user_policy(
        self,
        _request: shapes.DetachUserPolicyRequest = None,
        *,
        user_name: str,
        policy_arn: str,
    ) -> None:
        """
        Removes the specified managed policy from the specified user.

        A user can also have inline policies embedded with it. To delete an inline
        policy, use the DeleteUserPolicy API. For information about policies, see
        [Managed Policies and Inline
        Policies](http://docs.aws.amazon.com/IAM/latest/UserGuide/policies-managed-vs-
        inline.html) in the _IAM User Guide_.
        """
        if _request is None:
            _params = {}
            if user_name is not ShapeBase.NOT_SET:
                _params['user_name'] = user_name
            if policy_arn is not ShapeBase.NOT_SET:
                _params['policy_arn'] = policy_arn
            _request = shapes.DetachUserPolicyRequest(**_params)
        response = self._boto_client.detach_user_policy(**_request.to_boto())

    def enable_mfa_device(
        self,
        _request: shapes.EnableMFADeviceRequest = None,
        *,
        user_name: str,
        serial_number: str,
        authentication_code1: str,
        authentication_code2: str,
    ) -> None:
        """
        Enables the specified MFA device and associates it with the specified IAM user.
        When enabled, the MFA device is required for every subsequent login by the IAM
        user associated with the device.
        """
        if _request is None:
            _params = {}
            if user_name is not ShapeBase.NOT_SET:
                _params['user_name'] = user_name
            if serial_number is not ShapeBase.NOT_SET:
                _params['serial_number'] = serial_number
            if authentication_code1 is not ShapeBase.NOT_SET:
                _params['authentication_code1'] = authentication_code1
            if authentication_code2 is not ShapeBase.NOT_SET:
                _params['authentication_code2'] = authentication_code2
            _request = shapes.EnableMFADeviceRequest(**_params)
        response = self._boto_client.enable_mfa_device(**_request.to_boto())

    def generate_credential_report(
        self,
    ) -> shapes.GenerateCredentialReportResponse:
        """
        Generates a credential report for the AWS account. For more information about
        the credential report, see [Getting Credential
        Reports](http://docs.aws.amazon.com/IAM/latest/UserGuide/credential-
        reports.html) in the _IAM User Guide_.
        """
        response = self._boto_client.generate_credential_report()

        return shapes.GenerateCredentialReportResponse.from_boto(response)

    def get_access_key_last_used(
        self,
        _request: shapes.GetAccessKeyLastUsedRequest = None,
        *,
        access_key_id: str,
    ) -> shapes.GetAccessKeyLastUsedResponse:
        """
        Retrieves information about when the specified access key was last used. The
        information includes the date and time of last use, along with the AWS service
        and region that were specified in the last request made with that key.
        """
        if _request is None:
            _params = {}
            if access_key_id is not ShapeBase.NOT_SET:
                _params['access_key_id'] = access_key_id
            _request = shapes.GetAccessKeyLastUsedRequest(**_params)
        response = self._boto_client.get_access_key_last_used(
            **_request.to_boto()
        )

        return shapes.GetAccessKeyLastUsedResponse.from_boto(response)

    def get_account_authorization_details(
        self,
        _request: shapes.GetAccountAuthorizationDetailsRequest = None,
        *,
        filter: typing.List[typing.Union[str, shapes.EntityType]
                           ] = ShapeBase.NOT_SET,
        max_items: int = ShapeBase.NOT_SET,
        marker: str = ShapeBase.NOT_SET,
    ) -> shapes.GetAccountAuthorizationDetailsResponse:
        """
        Retrieves information about all IAM users, groups, roles, and policies in your
        AWS account, including their relationships to one another. Use this API to
        obtain a snapshot of the configuration of IAM permissions (users, groups, roles,
        and policies) in your account.

        Policies returned by this API are URL-encoded compliant with [RFC
        3986](https://tools.ietf.org/html/rfc3986). You can use a URL decoding method to
        convert the policy back to plain JSON text. For example, if you use Java, you
        can use the `decode` method of the `java.net.URLDecoder` utility class in the
        Java SDK. Other languages and SDKs provide similar functionality.

        You can optionally filter the results using the `Filter` parameter. You can
        paginate the results using the `MaxItems` and `Marker` parameters.
        """
        if _request is None:
            _params = {}
            if filter is not ShapeBase.NOT_SET:
                _params['filter'] = filter
            if max_items is not ShapeBase.NOT_SET:
                _params['max_items'] = max_items
            if marker is not ShapeBase.NOT_SET:
                _params['marker'] = marker
            _request = shapes.GetAccountAuthorizationDetailsRequest(**_params)
        paginator = self.get_paginator("get_account_authorization_details"
                                      ).paginate(**_request.to_boto())
        page_generator = (page for page in paginator)
        first_page = next(page_generator)
        result = shapes.GetAccountAuthorizationDetailsResponse.from_boto(
            first_page
        )
        result._page_iterator = page_generator
        return result

        return shapes.GetAccountAuthorizationDetailsResponse.from_boto(response)

    def get_account_password_policy(
        self,
    ) -> shapes.GetAccountPasswordPolicyResponse:
        """
        Retrieves the password policy for the AWS account. For more information about
        using a password policy, go to [Managing an IAM Password
        Policy](http://docs.aws.amazon.com/IAM/latest/UserGuide/Using_ManagingPasswordPolicies.html).
        """
        response = self._boto_client.get_account_password_policy()

        return shapes.GetAccountPasswordPolicyResponse.from_boto(response)

    def get_account_summary(self, ) -> shapes.GetAccountSummaryResponse:
        """
        Retrieves information about IAM entity usage and IAM quotas in the AWS account.

        For information about limitations on IAM entities, see [Limitations on IAM
        Entities](http://docs.aws.amazon.com/IAM/latest/UserGuide/LimitationsOnEntities.html)
        in the _IAM User Guide_.
        """
        response = self._boto_client.get_account_summary()

        return shapes.GetAccountSummaryResponse.from_boto(response)

    def get_context_keys_for_custom_policy(
        self,
        _request: shapes.GetContextKeysForCustomPolicyRequest = None,
        *,
        policy_input_list: typing.List[str],
    ) -> shapes.GetContextKeysForPolicyResponse:
        """
        Gets a list of all of the context keys referenced in the input policies. The
        policies are supplied as a list of one or more strings. To get the context keys
        from policies associated with an IAM user, group, or role, use
        GetContextKeysForPrincipalPolicy.

        Context keys are variables maintained by AWS and its services that provide
        details about the context of an API query request. Context keys can be evaluated
        by testing against a value specified in an IAM policy. Use
        `GetContextKeysForCustomPolicy` to understand what key names and values you must
        supply when you call SimulateCustomPolicy. Note that all parameters are shown in
        unencoded form here for clarity but must be URL encoded to be included as a part
        of a real HTML request.
        """
        if _request is None:
            _params = {}
            if policy_input_list is not ShapeBase.NOT_SET:
                _params['policy_input_list'] = policy_input_list
            _request = shapes.GetContextKeysForCustomPolicyRequest(**_params)
        response = self._boto_client.get_context_keys_for_custom_policy(
            **_request.to_boto()
        )

        return shapes.GetContextKeysForPolicyResponse.from_boto(response)

    def get_context_keys_for_principal_policy(
        self,
        _request: shapes.GetContextKeysForPrincipalPolicyRequest = None,
        *,
        policy_source_arn: str,
        policy_input_list: typing.List[str] = ShapeBase.NOT_SET,
    ) -> shapes.GetContextKeysForPolicyResponse:
        """
        Gets a list of all of the context keys referenced in all the IAM policies that
        are attached to the specified IAM entity. The entity can be an IAM user, group,
        or role. If you specify a user, then the request also includes all of the
        policies attached to groups that the user is a member of.

        You can optionally include a list of one or more additional policies, specified
        as strings. If you want to include _only_ a list of policies by string, use
        GetContextKeysForCustomPolicy instead.

        **Note:** This API discloses information about the permissions granted to other
        users. If you do not want users to see other user's permissions, then consider
        allowing them to use GetContextKeysForCustomPolicy instead.

        Context keys are variables maintained by AWS and its services that provide
        details about the context of an API query request. Context keys can be evaluated
        by testing against a value in an IAM policy. Use
        GetContextKeysForPrincipalPolicy to understand what key names and values you
        must supply when you call SimulatePrincipalPolicy.
        """
        if _request is None:
            _params = {}
            if policy_source_arn is not ShapeBase.NOT_SET:
                _params['policy_source_arn'] = policy_source_arn
            if policy_input_list is not ShapeBase.NOT_SET:
                _params['policy_input_list'] = policy_input_list
            _request = shapes.GetContextKeysForPrincipalPolicyRequest(**_params)
        response = self._boto_client.get_context_keys_for_principal_policy(
            **_request.to_boto()
        )

        return shapes.GetContextKeysForPolicyResponse.from_boto(response)

    def get_credential_report(self, ) -> shapes.GetCredentialReportResponse:
        """
        Retrieves a credential report for the AWS account. For more information about
        the credential report, see [Getting Credential
        Reports](http://docs.aws.amazon.com/IAM/latest/UserGuide/credential-
        reports.html) in the _IAM User Guide_.
        """
        response = self._boto_client.get_credential_report()

        return shapes.GetCredentialReportResponse.from_boto(response)

    def get_group(
        self,
        _request: shapes.GetGroupRequest = None,
        *,
        group_name: str,
        marker: str = ShapeBase.NOT_SET,
        max_items: int = ShapeBase.NOT_SET,
    ) -> shapes.GetGroupResponse:
        """
        Returns a list of IAM users that are in the specified IAM group. You can
        paginate the results using the `MaxItems` and `Marker` parameters.
        """
        if _request is None:
            _params = {}
            if group_name is not ShapeBase.NOT_SET:
                _params['group_name'] = group_name
            if marker is not ShapeBase.NOT_SET:
                _params['marker'] = marker
            if max_items is not ShapeBase.NOT_SET:
                _params['max_items'] = max_items
            _request = shapes.GetGroupRequest(**_params)
        paginator = self.get_paginator("get_group").paginate(
            **_request.to_boto()
        )
        page_generator = (page for page in paginator)
        first_page = next(page_generator)
        result = shapes.GetGroupResponse.from_boto(first_page)
        result._page_iterator = page_generator
        return result

        return shapes.GetGroupResponse.from_boto(response)

    def get_group_policy(
        self,
        _request: shapes.GetGroupPolicyRequest = None,
        *,
        group_name: str,
        policy_name: str,
    ) -> shapes.GetGroupPolicyResponse:
        """
        Retrieves the specified inline policy document that is embedded in the specified
        IAM group.

        Policies returned by this API are URL-encoded compliant with [RFC
        3986](https://tools.ietf.org/html/rfc3986). You can use a URL decoding method to
        convert the policy back to plain JSON text. For example, if you use Java, you
        can use the `decode` method of the `java.net.URLDecoder` utility class in the
        Java SDK. Other languages and SDKs provide similar functionality.

        An IAM group can also have managed policies attached to it. To retrieve a
        managed policy document that is attached to a group, use GetPolicy to determine
        the policy's default version, then use GetPolicyVersion to retrieve the policy
        document.

        For more information about policies, see [Managed Policies and Inline
        Policies](http://docs.aws.amazon.com/IAM/latest/UserGuide/policies-managed-vs-
        inline.html) in the _IAM User Guide_.
        """
        if _request is None:
            _params = {}
            if group_name is not ShapeBase.NOT_SET:
                _params['group_name'] = group_name
            if policy_name is not ShapeBase.NOT_SET:
                _params['policy_name'] = policy_name
            _request = shapes.GetGroupPolicyRequest(**_params)
        response = self._boto_client.get_group_policy(**_request.to_boto())

        return shapes.GetGroupPolicyResponse.from_boto(response)

    def get_instance_profile(
        self,
        _request: shapes.GetInstanceProfileRequest = None,
        *,
        instance_profile_name: str,
    ) -> shapes.GetInstanceProfileResponse:
        """
        Retrieves information about the specified instance profile, including the
        instance profile's path, GUID, ARN, and role. For more information about
        instance profiles, see [About Instance
        Profiles](http://docs.aws.amazon.com/IAM/latest/UserGuide/AboutInstanceProfiles.html)
        in the _IAM User Guide_.
        """
        if _request is None:
            _params = {}
            if instance_profile_name is not ShapeBase.NOT_SET:
                _params['instance_profile_name'] = instance_profile_name
            _request = shapes.GetInstanceProfileRequest(**_params)
        response = self._boto_client.get_instance_profile(**_request.to_boto())

        return shapes.GetInstanceProfileResponse.from_boto(response)

    def get_login_profile(
        self,
        _request: shapes.GetLoginProfileRequest = None,
        *,
        user_name: str,
    ) -> shapes.GetLoginProfileResponse:
        """
        Retrieves the user name and password-creation date for the specified IAM user.
        If the user has not been assigned a password, the operation returns a 404
        (`NoSuchEntity`) error.
        """
        if _request is None:
            _params = {}
            if user_name is not ShapeBase.NOT_SET:
                _params['user_name'] = user_name
            _request = shapes.GetLoginProfileRequest(**_params)
        response = self._boto_client.get_login_profile(**_request.to_boto())

        return shapes.GetLoginProfileResponse.from_boto(response)

    def get_open_id_connect_provider(
        self,
        _request: shapes.GetOpenIDConnectProviderRequest = None,
        *,
        open_id_connect_provider_arn: str,
    ) -> shapes.GetOpenIDConnectProviderResponse:
        """
        Returns information about the specified OpenID Connect (OIDC) provider resource
        object in IAM.
        """
        if _request is None:
            _params = {}
            if open_id_connect_provider_arn is not ShapeBase.NOT_SET:
                _params['open_id_connect_provider_arn'
                       ] = open_id_connect_provider_arn
            _request = shapes.GetOpenIDConnectProviderRequest(**_params)
        response = self._boto_client.get_open_id_connect_provider(
            **_request.to_boto()
        )

        return shapes.GetOpenIDConnectProviderResponse.from_boto(response)

    def get_policy(
        self,
        _request: shapes.GetPolicyRequest = None,
        *,
        policy_arn: str,
    ) -> shapes.GetPolicyResponse:
        """
        Retrieves information about the specified managed policy, including the policy's
        default version and the total number of IAM users, groups, and roles to which
        the policy is attached. To retrieve the list of the specific users, groups, and
        roles that the policy is attached to, use the ListEntitiesForPolicy API. This
        API returns metadata about the policy. To retrieve the actual policy document
        for a specific version of the policy, use GetPolicyVersion.

        This API retrieves information about managed policies. To retrieve information
        about an inline policy that is embedded with an IAM user, group, or role, use
        the GetUserPolicy, GetGroupPolicy, or GetRolePolicy API.

        For more information about policies, see [Managed Policies and Inline
        Policies](http://docs.aws.amazon.com/IAM/latest/UserGuide/policies-managed-vs-
        inline.html) in the _IAM User Guide_.
        """
        if _request is None:
            _params = {}
            if policy_arn is not ShapeBase.NOT_SET:
                _params['policy_arn'] = policy_arn
            _request = shapes.GetPolicyRequest(**_params)
        response = self._boto_client.get_policy(**_request.to_boto())

        return shapes.GetPolicyResponse.from_boto(response)

    def get_policy_version(
        self,
        _request: shapes.GetPolicyVersionRequest = None,
        *,
        policy_arn: str,
        version_id: str,
    ) -> shapes.GetPolicyVersionResponse:
        """
        Retrieves information about the specified version of the specified managed
        policy, including the policy document.

        Policies returned by this API are URL-encoded compliant with [RFC
        3986](https://tools.ietf.org/html/rfc3986). You can use a URL decoding method to
        convert the policy back to plain JSON text. For example, if you use Java, you
        can use the `decode` method of the `java.net.URLDecoder` utility class in the
        Java SDK. Other languages and SDKs provide similar functionality.

        To list the available versions for a policy, use ListPolicyVersions.

        This API retrieves information about managed policies. To retrieve information
        about an inline policy that is embedded in a user, group, or role, use the
        GetUserPolicy, GetGroupPolicy, or GetRolePolicy API.

        For more information about the types of policies, see [Managed Policies and
        Inline Policies](http://docs.aws.amazon.com/IAM/latest/UserGuide/policies-
        managed-vs-inline.html) in the _IAM User Guide_.

        For more information about managed policy versions, see [Versioning for Managed
        Policies](http://docs.aws.amazon.com/IAM/latest/UserGuide/policies-managed-
        versions.html) in the _IAM User Guide_.
        """
        if _request is None:
            _params = {}
            if policy_arn is not ShapeBase.NOT_SET:
                _params['policy_arn'] = policy_arn
            if version_id is not ShapeBase.NOT_SET:
                _params['version_id'] = version_id
            _request = shapes.GetPolicyVersionRequest(**_params)
        response = self._boto_client.get_policy_version(**_request.to_boto())

        return shapes.GetPolicyVersionResponse.from_boto(response)

    def get_role(
        self,
        _request: shapes.GetRoleRequest = None,
        *,
        role_name: str,
    ) -> shapes.GetRoleResponse:
        """
        Retrieves information about the specified role, including the role's path, GUID,
        ARN, and the role's trust policy that grants permission to assume the role. For
        more information about roles, see [Working with
        Roles](http://docs.aws.amazon.com/IAM/latest/UserGuide/WorkingWithRoles.html).

        Policies returned by this API are URL-encoded compliant with [RFC
        3986](https://tools.ietf.org/html/rfc3986). You can use a URL decoding method to
        convert the policy back to plain JSON text. For example, if you use Java, you
        can use the `decode` method of the `java.net.URLDecoder` utility class in the
        Java SDK. Other languages and SDKs provide similar functionality.
        """
        if _request is None:
            _params = {}
            if role_name is not ShapeBase.NOT_SET:
                _params['role_name'] = role_name
            _request = shapes.GetRoleRequest(**_params)
        response = self._boto_client.get_role(**_request.to_boto())

        return shapes.GetRoleResponse.from_boto(response)

    def get_role_policy(
        self,
        _request: shapes.GetRolePolicyRequest = None,
        *,
        role_name: str,
        policy_name: str,
    ) -> shapes.GetRolePolicyResponse:
        """
        Retrieves the specified inline policy document that is embedded with the
        specified IAM role.

        Policies returned by this API are URL-encoded compliant with [RFC
        3986](https://tools.ietf.org/html/rfc3986). You can use a URL decoding method to
        convert the policy back to plain JSON text. For example, if you use Java, you
        can use the `decode` method of the `java.net.URLDecoder` utility class in the
        Java SDK. Other languages and SDKs provide similar functionality.

        An IAM role can also have managed policies attached to it. To retrieve a managed
        policy document that is attached to a role, use GetPolicy to determine the
        policy's default version, then use GetPolicyVersion to retrieve the policy
        document.

        For more information about policies, see [Managed Policies and Inline
        Policies](http://docs.aws.amazon.com/IAM/latest/UserGuide/policies-managed-vs-
        inline.html) in the _IAM User Guide_.

        For more information about roles, see [Using Roles to Delegate Permissions and
        Federate Identities](http://docs.aws.amazon.com/IAM/latest/UserGuide/roles-
        toplevel.html).
        """
        if _request is None:
            _params = {}
            if role_name is not ShapeBase.NOT_SET:
                _params['role_name'] = role_name
            if policy_name is not ShapeBase.NOT_SET:
                _params['policy_name'] = policy_name
            _request = shapes.GetRolePolicyRequest(**_params)
        response = self._boto_client.get_role_policy(**_request.to_boto())

        return shapes.GetRolePolicyResponse.from_boto(response)

    def get_saml_provider(
        self,
        _request: shapes.GetSAMLProviderRequest = None,
        *,
        saml_provider_arn: str,
    ) -> shapes.GetSAMLProviderResponse:
        """
        Returns the SAML provider metadocument that was uploaded when the IAM SAML
        provider resource object was created or updated.

        This operation requires [Signature Version
        4](http://docs.aws.amazon.com/general/latest/gr/signature-version-4.html).
        """
        if _request is None:
            _params = {}
            if saml_provider_arn is not ShapeBase.NOT_SET:
                _params['saml_provider_arn'] = saml_provider_arn
            _request = shapes.GetSAMLProviderRequest(**_params)
        response = self._boto_client.get_saml_provider(**_request.to_boto())

        return shapes.GetSAMLProviderResponse.from_boto(response)

    def get_ssh_public_key(
        self,
        _request: shapes.GetSSHPublicKeyRequest = None,
        *,
        user_name: str,
        ssh_public_key_id: str,
        encoding: typing.Union[str, shapes.encodingType],
    ) -> shapes.GetSSHPublicKeyResponse:
        """
        Retrieves the specified SSH public key, including metadata about the key.

        The SSH public key retrieved by this operation is used only for authenticating
        the associated IAM user to an AWS CodeCommit repository. For more information
        about using SSH keys to authenticate to an AWS CodeCommit repository, see [Set
        up AWS CodeCommit for SSH
        Connections](http://docs.aws.amazon.com/codecommit/latest/userguide/setting-up-
        credentials-ssh.html) in the _AWS CodeCommit User Guide_.
        """
        if _request is None:
            _params = {}
            if user_name is not ShapeBase.NOT_SET:
                _params['user_name'] = user_name
            if ssh_public_key_id is not ShapeBase.NOT_SET:
                _params['ssh_public_key_id'] = ssh_public_key_id
            if encoding is not ShapeBase.NOT_SET:
                _params['encoding'] = encoding
            _request = shapes.GetSSHPublicKeyRequest(**_params)
        response = self._boto_client.get_ssh_public_key(**_request.to_boto())

        return shapes.GetSSHPublicKeyResponse.from_boto(response)

    def get_server_certificate(
        self,
        _request: shapes.GetServerCertificateRequest = None,
        *,
        server_certificate_name: str,
    ) -> shapes.GetServerCertificateResponse:
        """
        Retrieves information about the specified server certificate stored in IAM.

        For more information about working with server certificates, see [Working with
        Server
        Certificates](http://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_server-
        certs.html) in the _IAM User Guide_. This topic includes a list of AWS services
        that can use the server certificates that you manage with IAM.
        """
        if _request is None:
            _params = {}
            if server_certificate_name is not ShapeBase.NOT_SET:
                _params['server_certificate_name'] = server_certificate_name
            _request = shapes.GetServerCertificateRequest(**_params)
        response = self._boto_client.get_server_certificate(
            **_request.to_boto()
        )

        return shapes.GetServerCertificateResponse.from_boto(response)

    def get_service_linked_role_deletion_status(
        self,
        _request: shapes.GetServiceLinkedRoleDeletionStatusRequest = None,
        *,
        deletion_task_id: str,
    ) -> shapes.GetServiceLinkedRoleDeletionStatusResponse:
        """
        Retrieves the status of your service-linked role deletion. After you use the
        DeleteServiceLinkedRole API operation to submit a service-linked role for
        deletion, you can use the `DeletionTaskId` parameter in
        `GetServiceLinkedRoleDeletionStatus` to check the status of the deletion. If the
        deletion fails, this operation returns the reason that it failed, if that
        information is returned by the service.
        """
        if _request is None:
            _params = {}
            if deletion_task_id is not ShapeBase.NOT_SET:
                _params['deletion_task_id'] = deletion_task_id
            _request = shapes.GetServiceLinkedRoleDeletionStatusRequest(
                **_params
            )
        response = self._boto_client.get_service_linked_role_deletion_status(
            **_request.to_boto()
        )

        return shapes.GetServiceLinkedRoleDeletionStatusResponse.from_boto(
            response
        )

    def get_user(
        self,
        _request: shapes.GetUserRequest = None,
        *,
        user_name: str = ShapeBase.NOT_SET,
    ) -> shapes.GetUserResponse:
        """
        Retrieves information about the specified IAM user, including the user's
        creation date, path, unique ID, and ARN.

        If you do not specify a user name, IAM determines the user name implicitly based
        on the AWS access key ID used to sign the request to this API.
        """
        if _request is None:
            _params = {}
            if user_name is not ShapeBase.NOT_SET:
                _params['user_name'] = user_name
            _request = shapes.GetUserRequest(**_params)
        response = self._boto_client.get_user(**_request.to_boto())

        return shapes.GetUserResponse.from_boto(response)

    def get_user_policy(
        self,
        _request: shapes.GetUserPolicyRequest = None,
        *,
        user_name: str,
        policy_name: str,
    ) -> shapes.GetUserPolicyResponse:
        """
        Retrieves the specified inline policy document that is embedded in the specified
        IAM user.

        Policies returned by this API are URL-encoded compliant with [RFC
        3986](https://tools.ietf.org/html/rfc3986). You can use a URL decoding method to
        convert the policy back to plain JSON text. For example, if you use Java, you
        can use the `decode` method of the `java.net.URLDecoder` utility class in the
        Java SDK. Other languages and SDKs provide similar functionality.

        An IAM user can also have managed policies attached to it. To retrieve a managed
        policy document that is attached to a user, use GetPolicy to determine the
        policy's default version, then use GetPolicyVersion to retrieve the policy
        document.

        For more information about policies, see [Managed Policies and Inline
        Policies](http://docs.aws.amazon.com/IAM/latest/UserGuide/policies-managed-vs-
        inline.html) in the _IAM User Guide_.
        """
        if _request is None:
            _params = {}
            if user_name is not ShapeBase.NOT_SET:
                _params['user_name'] = user_name
            if policy_name is not ShapeBase.NOT_SET:
                _params['policy_name'] = policy_name
            _request = shapes.GetUserPolicyRequest(**_params)
        response = self._boto_client.get_user_policy(**_request.to_boto())

        return shapes.GetUserPolicyResponse.from_boto(response)

    def list_access_keys(
        self,
        _request: shapes.ListAccessKeysRequest = None,
        *,
        user_name: str = ShapeBase.NOT_SET,
        marker: str = ShapeBase.NOT_SET,
        max_items: int = ShapeBase.NOT_SET,
    ) -> shapes.ListAccessKeysResponse:
        """
        Returns information about the access key IDs associated with the specified IAM
        user. If there are none, the operation returns an empty list.

        Although each user is limited to a small number of keys, you can still paginate
        the results using the `MaxItems` and `Marker` parameters.

        If the `UserName` field is not specified, the user name is determined implicitly
        based on the AWS access key ID used to sign the request. Because this operation
        works for access keys under the AWS account, you can use this operation to
        manage AWS account root user credentials even if the AWS account has no
        associated users.

        To ensure the security of your AWS account, the secret access key is accessible
        only during key and user creation.
        """
        if _request is None:
            _params = {}
            if user_name is not ShapeBase.NOT_SET:
                _params['user_name'] = user_name
            if marker is not ShapeBase.NOT_SET:
                _params['marker'] = marker
            if max_items is not ShapeBase.NOT_SET:
                _params['max_items'] = max_items
            _request = shapes.ListAccessKeysRequest(**_params)
        paginator = self.get_paginator("list_access_keys").paginate(
            **_request.to_boto()
        )
        page_generator = (page for page in paginator)
        first_page = next(page_generator)
        result = shapes.ListAccessKeysResponse.from_boto(first_page)
        result._page_iterator = page_generator
        return result

        return shapes.ListAccessKeysResponse.from_boto(response)

    def list_account_aliases(
        self,
        _request: shapes.ListAccountAliasesRequest = None,
        *,
        marker: str = ShapeBase.NOT_SET,
        max_items: int = ShapeBase.NOT_SET,
    ) -> shapes.ListAccountAliasesResponse:
        """
        Lists the account alias associated with the AWS account (Note: you can have only
        one). For information about using an AWS account alias, see [Using an Alias for
        Your AWS Account
        ID](http://docs.aws.amazon.com/IAM/latest/UserGuide/AccountAlias.html) in the
        _IAM User Guide_.
        """
        if _request is None:
            _params = {}
            if marker is not ShapeBase.NOT_SET:
                _params['marker'] = marker
            if max_items is not ShapeBase.NOT_SET:
                _params['max_items'] = max_items
            _request = shapes.ListAccountAliasesRequest(**_params)
        paginator = self.get_paginator("list_account_aliases").paginate(
            **_request.to_boto()
        )
        page_generator = (page for page in paginator)
        first_page = next(page_generator)
        result = shapes.ListAccountAliasesResponse.from_boto(first_page)
        result._page_iterator = page_generator
        return result

        return shapes.ListAccountAliasesResponse.from_boto(response)

    def list_attached_group_policies(
        self,
        _request: shapes.ListAttachedGroupPoliciesRequest = None,
        *,
        group_name: str,
        path_prefix: str = ShapeBase.NOT_SET,
        marker: str = ShapeBase.NOT_SET,
        max_items: int = ShapeBase.NOT_SET,
    ) -> shapes.ListAttachedGroupPoliciesResponse:
        """
        Lists all managed policies that are attached to the specified IAM group.

        An IAM group can also have inline policies embedded with it. To list the inline
        policies for a group, use the ListGroupPolicies API. For information about
        policies, see [Managed Policies and Inline
        Policies](http://docs.aws.amazon.com/IAM/latest/UserGuide/policies-managed-vs-
        inline.html) in the _IAM User Guide_.

        You can paginate the results using the `MaxItems` and `Marker` parameters. You
        can use the `PathPrefix` parameter to limit the list of policies to only those
        matching the specified path prefix. If there are no policies attached to the
        specified group (or none that match the specified path prefix), the operation
        returns an empty list.
        """
        if _request is None:
            _params = {}
            if group_name is not ShapeBase.NOT_SET:
                _params['group_name'] = group_name
            if path_prefix is not ShapeBase.NOT_SET:
                _params['path_prefix'] = path_prefix
            if marker is not ShapeBase.NOT_SET:
                _params['marker'] = marker
            if max_items is not ShapeBase.NOT_SET:
                _params['max_items'] = max_items
            _request = shapes.ListAttachedGroupPoliciesRequest(**_params)
        paginator = self.get_paginator("list_attached_group_policies").paginate(
            **_request.to_boto()
        )
        page_generator = (page for page in paginator)
        first_page = next(page_generator)
        result = shapes.ListAttachedGroupPoliciesResponse.from_boto(first_page)
        result._page_iterator = page_generator
        return result

        return shapes.ListAttachedGroupPoliciesResponse.from_boto(response)

    def list_attached_role_policies(
        self,
        _request: shapes.ListAttachedRolePoliciesRequest = None,
        *,
        role_name: str,
        path_prefix: str = ShapeBase.NOT_SET,
        marker: str = ShapeBase.NOT_SET,
        max_items: int = ShapeBase.NOT_SET,
    ) -> shapes.ListAttachedRolePoliciesResponse:
        """
        Lists all managed policies that are attached to the specified IAM role.

        An IAM role can also have inline policies embedded with it. To list the inline
        policies for a role, use the ListRolePolicies API. For information about
        policies, see [Managed Policies and Inline
        Policies](http://docs.aws.amazon.com/IAM/latest/UserGuide/policies-managed-vs-
        inline.html) in the _IAM User Guide_.

        You can paginate the results using the `MaxItems` and `Marker` parameters. You
        can use the `PathPrefix` parameter to limit the list of policies to only those
        matching the specified path prefix. If there are no policies attached to the
        specified role (or none that match the specified path prefix), the operation
        returns an empty list.
        """
        if _request is None:
            _params = {}
            if role_name is not ShapeBase.NOT_SET:
                _params['role_name'] = role_name
            if path_prefix is not ShapeBase.NOT_SET:
                _params['path_prefix'] = path_prefix
            if marker is not ShapeBase.NOT_SET:
                _params['marker'] = marker
            if max_items is not ShapeBase.NOT_SET:
                _params['max_items'] = max_items
            _request = shapes.ListAttachedRolePoliciesRequest(**_params)
        paginator = self.get_paginator("list_attached_role_policies").paginate(
            **_request.to_boto()
        )
        page_generator = (page for page in paginator)
        first_page = next(page_generator)
        result = shapes.ListAttachedRolePoliciesResponse.from_boto(first_page)
        result._page_iterator = page_generator
        return result

        return shapes.ListAttachedRolePoliciesResponse.from_boto(response)

    def list_attached_user_policies(
        self,
        _request: shapes.ListAttachedUserPoliciesRequest = None,
        *,
        user_name: str,
        path_prefix: str = ShapeBase.NOT_SET,
        marker: str = ShapeBase.NOT_SET,
        max_items: int = ShapeBase.NOT_SET,
    ) -> shapes.ListAttachedUserPoliciesResponse:
        """
        Lists all managed policies that are attached to the specified IAM user.

        An IAM user can also have inline policies embedded with it. To list the inline
        policies for a user, use the ListUserPolicies API. For information about
        policies, see [Managed Policies and Inline
        Policies](http://docs.aws.amazon.com/IAM/latest/UserGuide/policies-managed-vs-
        inline.html) in the _IAM User Guide_.

        You can paginate the results using the `MaxItems` and `Marker` parameters. You
        can use the `PathPrefix` parameter to limit the list of policies to only those
        matching the specified path prefix. If there are no policies attached to the
        specified group (or none that match the specified path prefix), the operation
        returns an empty list.
        """
        if _request is None:
            _params = {}
            if user_name is not ShapeBase.NOT_SET:
                _params['user_name'] = user_name
            if path_prefix is not ShapeBase.NOT_SET:
                _params['path_prefix'] = path_prefix
            if marker is not ShapeBase.NOT_SET:
                _params['marker'] = marker
            if max_items is not ShapeBase.NOT_SET:
                _params['max_items'] = max_items
            _request = shapes.ListAttachedUserPoliciesRequest(**_params)
        paginator = self.get_paginator("list_attached_user_policies").paginate(
            **_request.to_boto()
        )
        page_generator = (page for page in paginator)
        first_page = next(page_generator)
        result = shapes.ListAttachedUserPoliciesResponse.from_boto(first_page)
        result._page_iterator = page_generator
        return result

        return shapes.ListAttachedUserPoliciesResponse.from_boto(response)

    def list_entities_for_policy(
        self,
        _request: shapes.ListEntitiesForPolicyRequest = None,
        *,
        policy_arn: str,
        entity_filter: typing.Union[str, shapes.EntityType] = ShapeBase.NOT_SET,
        path_prefix: str = ShapeBase.NOT_SET,
        policy_usage_filter: typing.Union[str, shapes.
                                          PolicyUsageType] = ShapeBase.NOT_SET,
        marker: str = ShapeBase.NOT_SET,
        max_items: int = ShapeBase.NOT_SET,
    ) -> shapes.ListEntitiesForPolicyResponse:
        """
        Lists all IAM users, groups, and roles that the specified managed policy is
        attached to.

        You can use the optional `EntityFilter` parameter to limit the results to a
        particular type of entity (users, groups, or roles). For example, to list only
        the roles that are attached to the specified policy, set `EntityFilter` to
        `Role`.

        You can paginate the results using the `MaxItems` and `Marker` parameters.
        """
        if _request is None:
            _params = {}
            if policy_arn is not ShapeBase.NOT_SET:
                _params['policy_arn'] = policy_arn
            if entity_filter is not ShapeBase.NOT_SET:
                _params['entity_filter'] = entity_filter
            if path_prefix is not ShapeBase.NOT_SET:
                _params['path_prefix'] = path_prefix
            if policy_usage_filter is not ShapeBase.NOT_SET:
                _params['policy_usage_filter'] = policy_usage_filter
            if marker is not ShapeBase.NOT_SET:
                _params['marker'] = marker
            if max_items is not ShapeBase.NOT_SET:
                _params['max_items'] = max_items
            _request = shapes.ListEntitiesForPolicyRequest(**_params)
        paginator = self.get_paginator("list_entities_for_policy").paginate(
            **_request.to_boto()
        )
        page_generator = (page for page in paginator)
        first_page = next(page_generator)
        result = shapes.ListEntitiesForPolicyResponse.from_boto(first_page)
        result._page_iterator = page_generator
        return result

        return shapes.ListEntitiesForPolicyResponse.from_boto(response)

    def list_group_policies(
        self,
        _request: shapes.ListGroupPoliciesRequest = None,
        *,
        group_name: str,
        marker: str = ShapeBase.NOT_SET,
        max_items: int = ShapeBase.NOT_SET,
    ) -> shapes.ListGroupPoliciesResponse:
        """
        Lists the names of the inline policies that are embedded in the specified IAM
        group.

        An IAM group can also have managed policies attached to it. To list the managed
        policies that are attached to a group, use ListAttachedGroupPolicies. For more
        information about policies, see [Managed Policies and Inline
        Policies](http://docs.aws.amazon.com/IAM/latest/UserGuide/policies-managed-vs-
        inline.html) in the _IAM User Guide_.

        You can paginate the results using the `MaxItems` and `Marker` parameters. If
        there are no inline policies embedded with the specified group, the operation
        returns an empty list.
        """
        if _request is None:
            _params = {}
            if group_name is not ShapeBase.NOT_SET:
                _params['group_name'] = group_name
            if marker is not ShapeBase.NOT_SET:
                _params['marker'] = marker
            if max_items is not ShapeBase.NOT_SET:
                _params['max_items'] = max_items
            _request = shapes.ListGroupPoliciesRequest(**_params)
        paginator = self.get_paginator("list_group_policies").paginate(
            **_request.to_boto()
        )
        page_generator = (page for page in paginator)
        first_page = next(page_generator)
        result = shapes.ListGroupPoliciesResponse.from_boto(first_page)
        result._page_iterator = page_generator
        return result

        return shapes.ListGroupPoliciesResponse.from_boto(response)

    def list_groups(
        self,
        _request: shapes.ListGroupsRequest = None,
        *,
        path_prefix: str = ShapeBase.NOT_SET,
        marker: str = ShapeBase.NOT_SET,
        max_items: int = ShapeBase.NOT_SET,
    ) -> shapes.ListGroupsResponse:
        """
        Lists the IAM groups that have the specified path prefix.

        You can paginate the results using the `MaxItems` and `Marker` parameters.
        """
        if _request is None:
            _params = {}
            if path_prefix is not ShapeBase.NOT_SET:
                _params['path_prefix'] = path_prefix
            if marker is not ShapeBase.NOT_SET:
                _params['marker'] = marker
            if max_items is not ShapeBase.NOT_SET:
                _params['max_items'] = max_items
            _request = shapes.ListGroupsRequest(**_params)
        paginator = self.get_paginator("list_groups").paginate(
            **_request.to_boto()
        )
        page_generator = (page for page in paginator)
        first_page = next(page_generator)
        result = shapes.ListGroupsResponse.from_boto(first_page)
        result._page_iterator = page_generator
        return result

        return shapes.ListGroupsResponse.from_boto(response)

    def list_groups_for_user(
        self,
        _request: shapes.ListGroupsForUserRequest = None,
        *,
        user_name: str,
        marker: str = ShapeBase.NOT_SET,
        max_items: int = ShapeBase.NOT_SET,
    ) -> shapes.ListGroupsForUserResponse:
        """
        Lists the IAM groups that the specified IAM user belongs to.

        You can paginate the results using the `MaxItems` and `Marker` parameters.
        """
        if _request is None:
            _params = {}
            if user_name is not ShapeBase.NOT_SET:
                _params['user_name'] = user_name
            if marker is not ShapeBase.NOT_SET:
                _params['marker'] = marker
            if max_items is not ShapeBase.NOT_SET:
                _params['max_items'] = max_items
            _request = shapes.ListGroupsForUserRequest(**_params)
        paginator = self.get_paginator("list_groups_for_user").paginate(
            **_request.to_boto()
        )
        page_generator = (page for page in paginator)
        first_page = next(page_generator)
        result = shapes.ListGroupsForUserResponse.from_boto(first_page)
        result._page_iterator = page_generator
        return result

        return shapes.ListGroupsForUserResponse.from_boto(response)

    def list_instance_profiles(
        self,
        _request: shapes.ListInstanceProfilesRequest = None,
        *,
        path_prefix: str = ShapeBase.NOT_SET,
        marker: str = ShapeBase.NOT_SET,
        max_items: int = ShapeBase.NOT_SET,
    ) -> shapes.ListInstanceProfilesResponse:
        """
        Lists the instance profiles that have the specified path prefix. If there are
        none, the operation returns an empty list. For more information about instance
        profiles, go to [About Instance
        Profiles](http://docs.aws.amazon.com/IAM/latest/UserGuide/AboutInstanceProfiles.html).

        You can paginate the results using the `MaxItems` and `Marker` parameters.
        """
        if _request is None:
            _params = {}
            if path_prefix is not ShapeBase.NOT_SET:
                _params['path_prefix'] = path_prefix
            if marker is not ShapeBase.NOT_SET:
                _params['marker'] = marker
            if max_items is not ShapeBase.NOT_SET:
                _params['max_items'] = max_items
            _request = shapes.ListInstanceProfilesRequest(**_params)
        paginator = self.get_paginator("list_instance_profiles").paginate(
            **_request.to_boto()
        )
        page_generator = (page for page in paginator)
        first_page = next(page_generator)
        result = shapes.ListInstanceProfilesResponse.from_boto(first_page)
        result._page_iterator = page_generator
        return result

        return shapes.ListInstanceProfilesResponse.from_boto(response)

    def list_instance_profiles_for_role(
        self,
        _request: shapes.ListInstanceProfilesForRoleRequest = None,
        *,
        role_name: str,
        marker: str = ShapeBase.NOT_SET,
        max_items: int = ShapeBase.NOT_SET,
    ) -> shapes.ListInstanceProfilesForRoleResponse:
        """
        Lists the instance profiles that have the specified associated IAM role. If
        there are none, the operation returns an empty list. For more information about
        instance profiles, go to [About Instance
        Profiles](http://docs.aws.amazon.com/IAM/latest/UserGuide/AboutInstanceProfiles.html).

        You can paginate the results using the `MaxItems` and `Marker` parameters.
        """
        if _request is None:
            _params = {}
            if role_name is not ShapeBase.NOT_SET:
                _params['role_name'] = role_name
            if marker is not ShapeBase.NOT_SET:
                _params['marker'] = marker
            if max_items is not ShapeBase.NOT_SET:
                _params['max_items'] = max_items
            _request = shapes.ListInstanceProfilesForRoleRequest(**_params)
        paginator = self.get_paginator("list_instance_profiles_for_role"
                                      ).paginate(**_request.to_boto())
        page_generator = (page for page in paginator)
        first_page = next(page_generator)
        result = shapes.ListInstanceProfilesForRoleResponse.from_boto(
            first_page
        )
        result._page_iterator = page_generator
        return result

        return shapes.ListInstanceProfilesForRoleResponse.from_boto(response)

    def list_mfa_devices(
        self,
        _request: shapes.ListMFADevicesRequest = None,
        *,
        user_name: str = ShapeBase.NOT_SET,
        marker: str = ShapeBase.NOT_SET,
        max_items: int = ShapeBase.NOT_SET,
    ) -> shapes.ListMFADevicesResponse:
        """
        Lists the MFA devices for an IAM user. If the request includes a IAM user name,
        then this operation lists all the MFA devices associated with the specified
        user. If you do not specify a user name, IAM determines the user name implicitly
        based on the AWS access key ID signing the request for this API.

        You can paginate the results using the `MaxItems` and `Marker` parameters.
        """
        if _request is None:
            _params = {}
            if user_name is not ShapeBase.NOT_SET:
                _params['user_name'] = user_name
            if marker is not ShapeBase.NOT_SET:
                _params['marker'] = marker
            if max_items is not ShapeBase.NOT_SET:
                _params['max_items'] = max_items
            _request = shapes.ListMFADevicesRequest(**_params)
        paginator = self.get_paginator("list_mfa_devices").paginate(
            **_request.to_boto()
        )
        page_generator = (page for page in paginator)
        first_page = next(page_generator)
        result = shapes.ListMFADevicesResponse.from_boto(first_page)
        result._page_iterator = page_generator
        return result

        return shapes.ListMFADevicesResponse.from_boto(response)

    def list_open_id_connect_providers(
        self,
        _request: shapes.ListOpenIDConnectProvidersRequest = None,
    ) -> shapes.ListOpenIDConnectProvidersResponse:
        """
        Lists information about the IAM OpenID Connect (OIDC) provider resource objects
        defined in the AWS account.
        """
        if _request is None:
            _params = {}
            _request = shapes.ListOpenIDConnectProvidersRequest(**_params)
        response = self._boto_client.list_open_id_connect_providers(
            **_request.to_boto()
        )

        return shapes.ListOpenIDConnectProvidersResponse.from_boto(response)

    def list_policies(
        self,
        _request: shapes.ListPoliciesRequest = None,
        *,
        scope: typing.Union[str, shapes.policyScopeType] = ShapeBase.NOT_SET,
        only_attached: bool = ShapeBase.NOT_SET,
        path_prefix: str = ShapeBase.NOT_SET,
        policy_usage_filter: typing.Union[str, shapes.
                                          PolicyUsageType] = ShapeBase.NOT_SET,
        marker: str = ShapeBase.NOT_SET,
        max_items: int = ShapeBase.NOT_SET,
    ) -> shapes.ListPoliciesResponse:
        """
        Lists all the managed policies that are available in your AWS account, including
        your own customer-defined managed policies and all AWS managed policies.

        You can filter the list of policies that is returned using the optional
        `OnlyAttached`, `Scope`, and `PathPrefix` parameters. For example, to list only
        the customer managed policies in your AWS account, set `Scope` to `Local`. To
        list only AWS managed policies, set `Scope` to `AWS`.

        You can paginate the results using the `MaxItems` and `Marker` parameters.

        For more information about managed policies, see [Managed Policies and Inline
        Policies](http://docs.aws.amazon.com/IAM/latest/UserGuide/policies-managed-vs-
        inline.html) in the _IAM User Guide_.
        """
        if _request is None:
            _params = {}
            if scope is not ShapeBase.NOT_SET:
                _params['scope'] = scope
            if only_attached is not ShapeBase.NOT_SET:
                _params['only_attached'] = only_attached
            if path_prefix is not ShapeBase.NOT_SET:
                _params['path_prefix'] = path_prefix
            if policy_usage_filter is not ShapeBase.NOT_SET:
                _params['policy_usage_filter'] = policy_usage_filter
            if marker is not ShapeBase.NOT_SET:
                _params['marker'] = marker
            if max_items is not ShapeBase.NOT_SET:
                _params['max_items'] = max_items
            _request = shapes.ListPoliciesRequest(**_params)
        paginator = self.get_paginator("list_policies").paginate(
            **_request.to_boto()
        )
        page_generator = (page for page in paginator)
        first_page = next(page_generator)
        result = shapes.ListPoliciesResponse.from_boto(first_page)
        result._page_iterator = page_generator
        return result

        return shapes.ListPoliciesResponse.from_boto(response)

    def list_policy_versions(
        self,
        _request: shapes.ListPolicyVersionsRequest = None,
        *,
        policy_arn: str,
        marker: str = ShapeBase.NOT_SET,
        max_items: int = ShapeBase.NOT_SET,
    ) -> shapes.ListPolicyVersionsResponse:
        """
        Lists information about the versions of the specified managed policy, including
        the version that is currently set as the policy's default version.

        For more information about managed policies, see [Managed Policies and Inline
        Policies](http://docs.aws.amazon.com/IAM/latest/UserGuide/policies-managed-vs-
        inline.html) in the _IAM User Guide_.
        """
        if _request is None:
            _params = {}
            if policy_arn is not ShapeBase.NOT_SET:
                _params['policy_arn'] = policy_arn
            if marker is not ShapeBase.NOT_SET:
                _params['marker'] = marker
            if max_items is not ShapeBase.NOT_SET:
                _params['max_items'] = max_items
            _request = shapes.ListPolicyVersionsRequest(**_params)
        paginator = self.get_paginator("list_policy_versions").paginate(
            **_request.to_boto()
        )
        page_generator = (page for page in paginator)
        first_page = next(page_generator)
        result = shapes.ListPolicyVersionsResponse.from_boto(first_page)
        result._page_iterator = page_generator
        return result

        return shapes.ListPolicyVersionsResponse.from_boto(response)

    def list_role_policies(
        self,
        _request: shapes.ListRolePoliciesRequest = None,
        *,
        role_name: str,
        marker: str = ShapeBase.NOT_SET,
        max_items: int = ShapeBase.NOT_SET,
    ) -> shapes.ListRolePoliciesResponse:
        """
        Lists the names of the inline policies that are embedded in the specified IAM
        role.

        An IAM role can also have managed policies attached to it. To list the managed
        policies that are attached to a role, use ListAttachedRolePolicies. For more
        information about policies, see [Managed Policies and Inline
        Policies](http://docs.aws.amazon.com/IAM/latest/UserGuide/policies-managed-vs-
        inline.html) in the _IAM User Guide_.

        You can paginate the results using the `MaxItems` and `Marker` parameters. If
        there are no inline policies embedded with the specified role, the operation
        returns an empty list.
        """
        if _request is None:
            _params = {}
            if role_name is not ShapeBase.NOT_SET:
                _params['role_name'] = role_name
            if marker is not ShapeBase.NOT_SET:
                _params['marker'] = marker
            if max_items is not ShapeBase.NOT_SET:
                _params['max_items'] = max_items
            _request = shapes.ListRolePoliciesRequest(**_params)
        paginator = self.get_paginator("list_role_policies").paginate(
            **_request.to_boto()
        )
        page_generator = (page for page in paginator)
        first_page = next(page_generator)
        result = shapes.ListRolePoliciesResponse.from_boto(first_page)
        result._page_iterator = page_generator
        return result

        return shapes.ListRolePoliciesResponse.from_boto(response)

    def list_roles(
        self,
        _request: shapes.ListRolesRequest = None,
        *,
        path_prefix: str = ShapeBase.NOT_SET,
        marker: str = ShapeBase.NOT_SET,
        max_items: int = ShapeBase.NOT_SET,
    ) -> shapes.ListRolesResponse:
        """
        Lists the IAM roles that have the specified path prefix. If there are none, the
        operation returns an empty list. For more information about roles, go to
        [Working with
        Roles](http://docs.aws.amazon.com/IAM/latest/UserGuide/WorkingWithRoles.html).

        You can paginate the results using the `MaxItems` and `Marker` parameters.
        """
        if _request is None:
            _params = {}
            if path_prefix is not ShapeBase.NOT_SET:
                _params['path_prefix'] = path_prefix
            if marker is not ShapeBase.NOT_SET:
                _params['marker'] = marker
            if max_items is not ShapeBase.NOT_SET:
                _params['max_items'] = max_items
            _request = shapes.ListRolesRequest(**_params)
        paginator = self.get_paginator("list_roles").paginate(
            **_request.to_boto()
        )
        page_generator = (page for page in paginator)
        first_page = next(page_generator)
        result = shapes.ListRolesResponse.from_boto(first_page)
        result._page_iterator = page_generator
        return result

        return shapes.ListRolesResponse.from_boto(response)

    def list_saml_providers(
        self,
        _request: shapes.ListSAMLProvidersRequest = None,
    ) -> shapes.ListSAMLProvidersResponse:
        """
        Lists the SAML provider resource objects defined in IAM in the account.

        This operation requires [Signature Version
        4](http://docs.aws.amazon.com/general/latest/gr/signature-version-4.html).
        """
        if _request is None:
            _params = {}
            _request = shapes.ListSAMLProvidersRequest(**_params)
        response = self._boto_client.list_saml_providers(**_request.to_boto())

        return shapes.ListSAMLProvidersResponse.from_boto(response)

    def list_ssh_public_keys(
        self,
        _request: shapes.ListSSHPublicKeysRequest = None,
        *,
        user_name: str = ShapeBase.NOT_SET,
        marker: str = ShapeBase.NOT_SET,
        max_items: int = ShapeBase.NOT_SET,
    ) -> shapes.ListSSHPublicKeysResponse:
        """
        Returns information about the SSH public keys associated with the specified IAM
        user. If there are none, the operation returns an empty list.

        The SSH public keys returned by this operation are used only for authenticating
        the IAM user to an AWS CodeCommit repository. For more information about using
        SSH keys to authenticate to an AWS CodeCommit repository, see [Set up AWS
        CodeCommit for SSH
        Connections](http://docs.aws.amazon.com/codecommit/latest/userguide/setting-up-
        credentials-ssh.html) in the _AWS CodeCommit User Guide_.

        Although each user is limited to a small number of keys, you can still paginate
        the results using the `MaxItems` and `Marker` parameters.
        """
        if _request is None:
            _params = {}
            if user_name is not ShapeBase.NOT_SET:
                _params['user_name'] = user_name
            if marker is not ShapeBase.NOT_SET:
                _params['marker'] = marker
            if max_items is not ShapeBase.NOT_SET:
                _params['max_items'] = max_items
            _request = shapes.ListSSHPublicKeysRequest(**_params)
        paginator = self.get_paginator("list_ssh_public_keys").paginate(
            **_request.to_boto()
        )
        page_generator = (page for page in paginator)
        first_page = next(page_generator)
        result = shapes.ListSSHPublicKeysResponse.from_boto(first_page)
        result._page_iterator = page_generator
        return result

        return shapes.ListSSHPublicKeysResponse.from_boto(response)

    def list_server_certificates(
        self,
        _request: shapes.ListServerCertificatesRequest = None,
        *,
        path_prefix: str = ShapeBase.NOT_SET,
        marker: str = ShapeBase.NOT_SET,
        max_items: int = ShapeBase.NOT_SET,
    ) -> shapes.ListServerCertificatesResponse:
        """
        Lists the server certificates stored in IAM that have the specified path prefix.
        If none exist, the operation returns an empty list.

        You can paginate the results using the `MaxItems` and `Marker` parameters.

        For more information about working with server certificates, see [Working with
        Server
        Certificates](http://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_server-
        certs.html) in the _IAM User Guide_. This topic also includes a list of AWS
        services that can use the server certificates that you manage with IAM.
        """
        if _request is None:
            _params = {}
            if path_prefix is not ShapeBase.NOT_SET:
                _params['path_prefix'] = path_prefix
            if marker is not ShapeBase.NOT_SET:
                _params['marker'] = marker
            if max_items is not ShapeBase.NOT_SET:
                _params['max_items'] = max_items
            _request = shapes.ListServerCertificatesRequest(**_params)
        paginator = self.get_paginator("list_server_certificates").paginate(
            **_request.to_boto()
        )
        page_generator = (page for page in paginator)
        first_page = next(page_generator)
        result = shapes.ListServerCertificatesResponse.from_boto(first_page)
        result._page_iterator = page_generator
        return result

        return shapes.ListServerCertificatesResponse.from_boto(response)

    def list_service_specific_credentials(
        self,
        _request: shapes.ListServiceSpecificCredentialsRequest = None,
        *,
        user_name: str = ShapeBase.NOT_SET,
        service_name: str = ShapeBase.NOT_SET,
    ) -> shapes.ListServiceSpecificCredentialsResponse:
        """
        Returns information about the service-specific credentials associated with the
        specified IAM user. If there are none, the operation returns an empty list. The
        service-specific credentials returned by this operation are used only for
        authenticating the IAM user to a specific service. For more information about
        using service-specific credentials to authenticate to an AWS service, see [Set
        Up service-specific
        credentials](http://docs.aws.amazon.com/codecommit/latest/userguide/setting-up-
        gc.html) in the AWS CodeCommit User Guide.
        """
        if _request is None:
            _params = {}
            if user_name is not ShapeBase.NOT_SET:
                _params['user_name'] = user_name
            if service_name is not ShapeBase.NOT_SET:
                _params['service_name'] = service_name
            _request = shapes.ListServiceSpecificCredentialsRequest(**_params)
        response = self._boto_client.list_service_specific_credentials(
            **_request.to_boto()
        )

        return shapes.ListServiceSpecificCredentialsResponse.from_boto(response)

    def list_signing_certificates(
        self,
        _request: shapes.ListSigningCertificatesRequest = None,
        *,
        user_name: str = ShapeBase.NOT_SET,
        marker: str = ShapeBase.NOT_SET,
        max_items: int = ShapeBase.NOT_SET,
    ) -> shapes.ListSigningCertificatesResponse:
        """
        Returns information about the signing certificates associated with the specified
        IAM user. If there are none, the operation returns an empty list.

        Although each user is limited to a small number of signing certificates, you can
        still paginate the results using the `MaxItems` and `Marker` parameters.

        If the `UserName` field is not specified, the user name is determined implicitly
        based on the AWS access key ID used to sign the request for this API. Because
        this operation works for access keys under the AWS account, you can use this
        operation to manage AWS account root user credentials even if the AWS account
        has no associated users.
        """
        if _request is None:
            _params = {}
            if user_name is not ShapeBase.NOT_SET:
                _params['user_name'] = user_name
            if marker is not ShapeBase.NOT_SET:
                _params['marker'] = marker
            if max_items is not ShapeBase.NOT_SET:
                _params['max_items'] = max_items
            _request = shapes.ListSigningCertificatesRequest(**_params)
        paginator = self.get_paginator("list_signing_certificates").paginate(
            **_request.to_boto()
        )
        page_generator = (page for page in paginator)
        first_page = next(page_generator)
        result = shapes.ListSigningCertificatesResponse.from_boto(first_page)
        result._page_iterator = page_generator
        return result

        return shapes.ListSigningCertificatesResponse.from_boto(response)

    def list_user_policies(
        self,
        _request: shapes.ListUserPoliciesRequest = None,
        *,
        user_name: str,
        marker: str = ShapeBase.NOT_SET,
        max_items: int = ShapeBase.NOT_SET,
    ) -> shapes.ListUserPoliciesResponse:
        """
        Lists the names of the inline policies embedded in the specified IAM user.

        An IAM user can also have managed policies attached to it. To list the managed
        policies that are attached to a user, use ListAttachedUserPolicies. For more
        information about policies, see [Managed Policies and Inline
        Policies](http://docs.aws.amazon.com/IAM/latest/UserGuide/policies-managed-vs-
        inline.html) in the _IAM User Guide_.

        You can paginate the results using the `MaxItems` and `Marker` parameters. If
        there are no inline policies embedded with the specified user, the operation
        returns an empty list.
        """
        if _request is None:
            _params = {}
            if user_name is not ShapeBase.NOT_SET:
                _params['user_name'] = user_name
            if marker is not ShapeBase.NOT_SET:
                _params['marker'] = marker
            if max_items is not ShapeBase.NOT_SET:
                _params['max_items'] = max_items
            _request = shapes.ListUserPoliciesRequest(**_params)
        paginator = self.get_paginator("list_user_policies").paginate(
            **_request.to_boto()
        )
        page_generator = (page for page in paginator)
        first_page = next(page_generator)
        result = shapes.ListUserPoliciesResponse.from_boto(first_page)
        result._page_iterator = page_generator
        return result

        return shapes.ListUserPoliciesResponse.from_boto(response)

    def list_users(
        self,
        _request: shapes.ListUsersRequest = None,
        *,
        path_prefix: str = ShapeBase.NOT_SET,
        marker: str = ShapeBase.NOT_SET,
        max_items: int = ShapeBase.NOT_SET,
    ) -> shapes.ListUsersResponse:
        """
        Lists the IAM users that have the specified path prefix. If no path prefix is
        specified, the operation returns all users in the AWS account. If there are
        none, the operation returns an empty list.

        You can paginate the results using the `MaxItems` and `Marker` parameters.
        """
        if _request is None:
            _params = {}
            if path_prefix is not ShapeBase.NOT_SET:
                _params['path_prefix'] = path_prefix
            if marker is not ShapeBase.NOT_SET:
                _params['marker'] = marker
            if max_items is not ShapeBase.NOT_SET:
                _params['max_items'] = max_items
            _request = shapes.ListUsersRequest(**_params)
        paginator = self.get_paginator("list_users").paginate(
            **_request.to_boto()
        )
        page_generator = (page for page in paginator)
        first_page = next(page_generator)
        result = shapes.ListUsersResponse.from_boto(first_page)
        result._page_iterator = page_generator
        return result

        return shapes.ListUsersResponse.from_boto(response)

    def list_virtual_mfa_devices(
        self,
        _request: shapes.ListVirtualMFADevicesRequest = None,
        *,
        assignment_status: typing.
        Union[str, shapes.assignmentStatusType] = ShapeBase.NOT_SET,
        marker: str = ShapeBase.NOT_SET,
        max_items: int = ShapeBase.NOT_SET,
    ) -> shapes.ListVirtualMFADevicesResponse:
        """
        Lists the virtual MFA devices defined in the AWS account by assignment status.
        If you do not specify an assignment status, the operation returns a list of all
        virtual MFA devices. Assignment status can be `Assigned`, `Unassigned`, or
        `Any`.

        You can paginate the results using the `MaxItems` and `Marker` parameters.
        """
        if _request is None:
            _params = {}
            if assignment_status is not ShapeBase.NOT_SET:
                _params['assignment_status'] = assignment_status
            if marker is not ShapeBase.NOT_SET:
                _params['marker'] = marker
            if max_items is not ShapeBase.NOT_SET:
                _params['max_items'] = max_items
            _request = shapes.ListVirtualMFADevicesRequest(**_params)
        paginator = self.get_paginator("list_virtual_mfa_devices").paginate(
            **_request.to_boto()
        )
        page_generator = (page for page in paginator)
        first_page = next(page_generator)
        result = shapes.ListVirtualMFADevicesResponse.from_boto(first_page)
        result._page_iterator = page_generator
        return result

        return shapes.ListVirtualMFADevicesResponse.from_boto(response)

    def put_group_policy(
        self,
        _request: shapes.PutGroupPolicyRequest = None,
        *,
        group_name: str,
        policy_name: str,
        policy_document: str,
    ) -> None:
        """
        Adds or updates an inline policy document that is embedded in the specified IAM
        group.

        A user can also have managed policies attached to it. To attach a managed policy
        to a group, use AttachGroupPolicy. To create a new managed policy, use
        CreatePolicy. For information about policies, see [Managed Policies and Inline
        Policies](http://docs.aws.amazon.com/IAM/latest/UserGuide/policies-managed-vs-
        inline.html) in the _IAM User Guide_.

        For information about limits on the number of inline policies that you can embed
        in a group, see [Limitations on IAM
        Entities](http://docs.aws.amazon.com/IAM/latest/UserGuide/LimitationsOnEntities.html)
        in the _IAM User Guide_.

        Because policy documents can be large, you should use POST rather than GET when
        calling `PutGroupPolicy`. For general information about using the Query API with
        IAM, go to [Making Query
        Requests](http://docs.aws.amazon.com/IAM/latest/UserGuide/IAM_UsingQueryAPI.html)
        in the _IAM User Guide_.
        """
        if _request is None:
            _params = {}
            if group_name is not ShapeBase.NOT_SET:
                _params['group_name'] = group_name
            if policy_name is not ShapeBase.NOT_SET:
                _params['policy_name'] = policy_name
            if policy_document is not ShapeBase.NOT_SET:
                _params['policy_document'] = policy_document
            _request = shapes.PutGroupPolicyRequest(**_params)
        response = self._boto_client.put_group_policy(**_request.to_boto())

    def put_role_permissions_boundary(
        self,
        _request: shapes.PutRolePermissionsBoundaryRequest = None,
        *,
        role_name: str,
        permissions_boundary: str,
    ) -> None:
        """
        Adds or updates the policy that is specified as the IAM role's permissions
        boundary. You can use an AWS managed policy or a customer managed policy to set
        the boundary for a role. Use the boundary to control the maximum permissions
        that the role can have. Setting a permissions boundary is an advanced feature
        that can affect the permissions for the role.

        You cannot set the boundary for a service-linked role.

        Policies used as permissions boundaries do not provide permissions. You must
        also attach a permissions policy to the role. To learn how the effective
        permissions for a role are evaluated, see [IAM JSON Policy Evaluation
        Logic](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_evaluation-
        logic.html) in the IAM User Guide.
        """
        if _request is None:
            _params = {}
            if role_name is not ShapeBase.NOT_SET:
                _params['role_name'] = role_name
            if permissions_boundary is not ShapeBase.NOT_SET:
                _params['permissions_boundary'] = permissions_boundary
            _request = shapes.PutRolePermissionsBoundaryRequest(**_params)
        response = self._boto_client.put_role_permissions_boundary(
            **_request.to_boto()
        )

    def put_role_policy(
        self,
        _request: shapes.PutRolePolicyRequest = None,
        *,
        role_name: str,
        policy_name: str,
        policy_document: str,
    ) -> None:
        """
        Adds or updates an inline policy document that is embedded in the specified IAM
        role.

        When you embed an inline policy in a role, the inline policy is used as part of
        the role's access (permissions) policy. The role's trust policy is created at
        the same time as the role, using CreateRole. You can update a role's trust
        policy using UpdateAssumeRolePolicy. For more information about IAM roles, go to
        [Using Roles to Delegate Permissions and Federate
        Identities](http://docs.aws.amazon.com/IAM/latest/UserGuide/roles-
        toplevel.html).

        A role can also have a managed policy attached to it. To attach a managed policy
        to a role, use AttachRolePolicy. To create a new managed policy, use
        CreatePolicy. For information about policies, see [Managed Policies and Inline
        Policies](http://docs.aws.amazon.com/IAM/latest/UserGuide/policies-managed-vs-
        inline.html) in the _IAM User Guide_.

        For information about limits on the number of inline policies that you can embed
        with a role, see [Limitations on IAM
        Entities](http://docs.aws.amazon.com/IAM/latest/UserGuide/LimitationsOnEntities.html)
        in the _IAM User Guide_.

        Because policy documents can be large, you should use POST rather than GET when
        calling `PutRolePolicy`. For general information about using the Query API with
        IAM, go to [Making Query
        Requests](http://docs.aws.amazon.com/IAM/latest/UserGuide/IAM_UsingQueryAPI.html)
        in the _IAM User Guide_.
        """
        if _request is None:
            _params = {}
            if role_name is not ShapeBase.NOT_SET:
                _params['role_name'] = role_name
            if policy_name is not ShapeBase.NOT_SET:
                _params['policy_name'] = policy_name
            if policy_document is not ShapeBase.NOT_SET:
                _params['policy_document'] = policy_document
            _request = shapes.PutRolePolicyRequest(**_params)
        response = self._boto_client.put_role_policy(**_request.to_boto())

    def put_user_permissions_boundary(
        self,
        _request: shapes.PutUserPermissionsBoundaryRequest = None,
        *,
        user_name: str,
        permissions_boundary: str,
    ) -> None:
        """
        Adds or updates the policy that is specified as the IAM user's permissions
        boundary. You can use an AWS managed policy or a customer managed policy to set
        the boundary for a user. Use the boundary to control the maximum permissions
        that the user can have. Setting a permissions boundary is an advanced feature
        that can affect the permissions for the user.

        Policies that are used as permissions boundaries do not provide permissions. You
        must also attach a permissions policy to the user. To learn how the effective
        permissions for a user are evaluated, see [IAM JSON Policy Evaluation
        Logic](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_evaluation-
        logic.html) in the IAM User Guide.
        """
        if _request is None:
            _params = {}
            if user_name is not ShapeBase.NOT_SET:
                _params['user_name'] = user_name
            if permissions_boundary is not ShapeBase.NOT_SET:
                _params['permissions_boundary'] = permissions_boundary
            _request = shapes.PutUserPermissionsBoundaryRequest(**_params)
        response = self._boto_client.put_user_permissions_boundary(
            **_request.to_boto()
        )

    def put_user_policy(
        self,
        _request: shapes.PutUserPolicyRequest = None,
        *,
        user_name: str,
        policy_name: str,
        policy_document: str,
    ) -> None:
        """
        Adds or updates an inline policy document that is embedded in the specified IAM
        user.

        An IAM user can also have a managed policy attached to it. To attach a managed
        policy to a user, use AttachUserPolicy. To create a new managed policy, use
        CreatePolicy. For information about policies, see [Managed Policies and Inline
        Policies](http://docs.aws.amazon.com/IAM/latest/UserGuide/policies-managed-vs-
        inline.html) in the _IAM User Guide_.

        For information about limits on the number of inline policies that you can embed
        in a user, see [Limitations on IAM
        Entities](http://docs.aws.amazon.com/IAM/latest/UserGuide/LimitationsOnEntities.html)
        in the _IAM User Guide_.

        Because policy documents can be large, you should use POST rather than GET when
        calling `PutUserPolicy`. For general information about using the Query API with
        IAM, go to [Making Query
        Requests](http://docs.aws.amazon.com/IAM/latest/UserGuide/IAM_UsingQueryAPI.html)
        in the _IAM User Guide_.
        """
        if _request is None:
            _params = {}
            if user_name is not ShapeBase.NOT_SET:
                _params['user_name'] = user_name
            if policy_name is not ShapeBase.NOT_SET:
                _params['policy_name'] = policy_name
            if policy_document is not ShapeBase.NOT_SET:
                _params['policy_document'] = policy_document
            _request = shapes.PutUserPolicyRequest(**_params)
        response = self._boto_client.put_user_policy(**_request.to_boto())

    def remove_client_id_from_open_id_connect_provider(
        self,
        _request: shapes.RemoveClientIDFromOpenIDConnectProviderRequest = None,
        *,
        open_id_connect_provider_arn: str,
        client_id: str,
    ) -> None:
        """
        Removes the specified client ID (also known as audience) from the list of client
        IDs registered for the specified IAM OpenID Connect (OIDC) provider resource
        object.

        This operation is idempotent; it does not fail or return an error if you try to
        remove a client ID that does not exist.
        """
        if _request is None:
            _params = {}
            if open_id_connect_provider_arn is not ShapeBase.NOT_SET:
                _params['open_id_connect_provider_arn'
                       ] = open_id_connect_provider_arn
            if client_id is not ShapeBase.NOT_SET:
                _params['client_id'] = client_id
            _request = shapes.RemoveClientIDFromOpenIDConnectProviderRequest(
                **_params
            )
        response = self._boto_client.remove_client_id_from_open_id_connect_provider(
            **_request.to_boto()
        )

    def remove_role_from_instance_profile(
        self,
        _request: shapes.RemoveRoleFromInstanceProfileRequest = None,
        *,
        instance_profile_name: str,
        role_name: str,
    ) -> None:
        """
        Removes the specified IAM role from the specified EC2 instance profile.

        Make sure that you do not have any Amazon EC2 instances running with the role
        you are about to remove from the instance profile. Removing a role from an
        instance profile that is associated with a running instance might break any
        applications running on the instance.

        For more information about IAM roles, go to [Working with
        Roles](http://docs.aws.amazon.com/IAM/latest/UserGuide/WorkingWithRoles.html).
        For more information about instance profiles, go to [About Instance
        Profiles](http://docs.aws.amazon.com/IAM/latest/UserGuide/AboutInstanceProfiles.html).
        """
        if _request is None:
            _params = {}
            if instance_profile_name is not ShapeBase.NOT_SET:
                _params['instance_profile_name'] = instance_profile_name
            if role_name is not ShapeBase.NOT_SET:
                _params['role_name'] = role_name
            _request = shapes.RemoveRoleFromInstanceProfileRequest(**_params)
        response = self._boto_client.remove_role_from_instance_profile(
            **_request.to_boto()
        )

    def remove_user_from_group(
        self,
        _request: shapes.RemoveUserFromGroupRequest = None,
        *,
        group_name: str,
        user_name: str,
    ) -> None:
        """
        Removes the specified user from the specified group.
        """
        if _request is None:
            _params = {}
            if group_name is not ShapeBase.NOT_SET:
                _params['group_name'] = group_name
            if user_name is not ShapeBase.NOT_SET:
                _params['user_name'] = user_name
            _request = shapes.RemoveUserFromGroupRequest(**_params)
        response = self._boto_client.remove_user_from_group(
            **_request.to_boto()
        )

    def reset_service_specific_credential(
        self,
        _request: shapes.ResetServiceSpecificCredentialRequest = None,
        *,
        service_specific_credential_id: str,
        user_name: str = ShapeBase.NOT_SET,
    ) -> shapes.ResetServiceSpecificCredentialResponse:
        """
        Resets the password for a service-specific credential. The new password is AWS
        generated and cryptographically strong. It cannot be configured by the user.
        Resetting the password immediately invalidates the previous password associated
        with this user.
        """
        if _request is None:
            _params = {}
            if service_specific_credential_id is not ShapeBase.NOT_SET:
                _params['service_specific_credential_id'
                       ] = service_specific_credential_id
            if user_name is not ShapeBase.NOT_SET:
                _params['user_name'] = user_name
            _request = shapes.ResetServiceSpecificCredentialRequest(**_params)
        response = self._boto_client.reset_service_specific_credential(
            **_request.to_boto()
        )

        return shapes.ResetServiceSpecificCredentialResponse.from_boto(response)

    def resync_mfa_device(
        self,
        _request: shapes.ResyncMFADeviceRequest = None,
        *,
        user_name: str,
        serial_number: str,
        authentication_code1: str,
        authentication_code2: str,
    ) -> None:
        """
        Synchronizes the specified MFA device with its IAM resource object on the AWS
        servers.

        For more information about creating and working with virtual MFA devices, go to
        [Using a Virtual MFA
        Device](http://docs.aws.amazon.com/IAM/latest/UserGuide/Using_VirtualMFA.html)
        in the _IAM User Guide_.
        """
        if _request is None:
            _params = {}
            if user_name is not ShapeBase.NOT_SET:
                _params['user_name'] = user_name
            if serial_number is not ShapeBase.NOT_SET:
                _params['serial_number'] = serial_number
            if authentication_code1 is not ShapeBase.NOT_SET:
                _params['authentication_code1'] = authentication_code1
            if authentication_code2 is not ShapeBase.NOT_SET:
                _params['authentication_code2'] = authentication_code2
            _request = shapes.ResyncMFADeviceRequest(**_params)
        response = self._boto_client.resync_mfa_device(**_request.to_boto())

    def set_default_policy_version(
        self,
        _request: shapes.SetDefaultPolicyVersionRequest = None,
        *,
        policy_arn: str,
        version_id: str,
    ) -> None:
        """
        Sets the specified version of the specified policy as the policy's default
        (operative) version.

        This operation affects all users, groups, and roles that the policy is attached
        to. To list the users, groups, and roles that the policy is attached to, use the
        ListEntitiesForPolicy API.

        For information about managed policies, see [Managed Policies and Inline
        Policies](http://docs.aws.amazon.com/IAM/latest/UserGuide/policies-managed-vs-
        inline.html) in the _IAM User Guide_.
        """
        if _request is None:
            _params = {}
            if policy_arn is not ShapeBase.NOT_SET:
                _params['policy_arn'] = policy_arn
            if version_id is not ShapeBase.NOT_SET:
                _params['version_id'] = version_id
            _request = shapes.SetDefaultPolicyVersionRequest(**_params)
        response = self._boto_client.set_default_policy_version(
            **_request.to_boto()
        )

    def simulate_custom_policy(
        self,
        _request: shapes.SimulateCustomPolicyRequest = None,
        *,
        policy_input_list: typing.List[str],
        action_names: typing.List[str],
        resource_arns: typing.List[str] = ShapeBase.NOT_SET,
        resource_policy: str = ShapeBase.NOT_SET,
        resource_owner: str = ShapeBase.NOT_SET,
        caller_arn: str = ShapeBase.NOT_SET,
        context_entries: typing.List[shapes.ContextEntry] = ShapeBase.NOT_SET,
        resource_handling_option: str = ShapeBase.NOT_SET,
        max_items: int = ShapeBase.NOT_SET,
        marker: str = ShapeBase.NOT_SET,
    ) -> shapes.SimulatePolicyResponse:
        """
        Simulate how a set of IAM policies and optionally a resource-based policy works
        with a list of API operations and AWS resources to determine the policies'
        effective permissions. The policies are provided as strings.

        The simulation does not perform the API operations; it only checks the
        authorization to determine if the simulated policies allow or deny the
        operations.

        If you want to simulate existing policies attached to an IAM user, group, or
        role, use SimulatePrincipalPolicy instead.

        Context keys are variables maintained by AWS and its services that provide
        details about the context of an API query request. You can use the `Condition`
        element of an IAM policy to evaluate context keys. To get the list of context
        keys that the policies require for correct simulation, use
        GetContextKeysForCustomPolicy.

        If the output is long, you can use `MaxItems` and `Marker` parameters to
        paginate the results.
        """
        if _request is None:
            _params = {}
            if policy_input_list is not ShapeBase.NOT_SET:
                _params['policy_input_list'] = policy_input_list
            if action_names is not ShapeBase.NOT_SET:
                _params['action_names'] = action_names
            if resource_arns is not ShapeBase.NOT_SET:
                _params['resource_arns'] = resource_arns
            if resource_policy is not ShapeBase.NOT_SET:
                _params['resource_policy'] = resource_policy
            if resource_owner is not ShapeBase.NOT_SET:
                _params['resource_owner'] = resource_owner
            if caller_arn is not ShapeBase.NOT_SET:
                _params['caller_arn'] = caller_arn
            if context_entries is not ShapeBase.NOT_SET:
                _params['context_entries'] = context_entries
            if resource_handling_option is not ShapeBase.NOT_SET:
                _params['resource_handling_option'] = resource_handling_option
            if max_items is not ShapeBase.NOT_SET:
                _params['max_items'] = max_items
            if marker is not ShapeBase.NOT_SET:
                _params['marker'] = marker
            _request = shapes.SimulateCustomPolicyRequest(**_params)
        paginator = self.get_paginator("simulate_custom_policy").paginate(
            **_request.to_boto()
        )
        page_generator = (page for page in paginator)
        first_page = next(page_generator)
        result = shapes.SimulatePolicyResponse.from_boto(first_page)
        result._page_iterator = page_generator
        return result

        return shapes.SimulatePolicyResponse.from_boto(response)

    def simulate_principal_policy(
        self,
        _request: shapes.SimulatePrincipalPolicyRequest = None,
        *,
        policy_source_arn: str,
        action_names: typing.List[str],
        policy_input_list: typing.List[str] = ShapeBase.NOT_SET,
        resource_arns: typing.List[str] = ShapeBase.NOT_SET,
        resource_policy: str = ShapeBase.NOT_SET,
        resource_owner: str = ShapeBase.NOT_SET,
        caller_arn: str = ShapeBase.NOT_SET,
        context_entries: typing.List[shapes.ContextEntry] = ShapeBase.NOT_SET,
        resource_handling_option: str = ShapeBase.NOT_SET,
        max_items: int = ShapeBase.NOT_SET,
        marker: str = ShapeBase.NOT_SET,
    ) -> shapes.SimulatePolicyResponse:
        """
        Simulate how a set of IAM policies attached to an IAM entity works with a list
        of API operations and AWS resources to determine the policies' effective
        permissions. The entity can be an IAM user, group, or role. If you specify a
        user, then the simulation also includes all of the policies that are attached to
        groups that the user belongs to.

        You can optionally include a list of one or more additional policies specified
        as strings to include in the simulation. If you want to simulate only policies
        specified as strings, use SimulateCustomPolicy instead.

        You can also optionally include one resource-based policy to be evaluated with
        each of the resources included in the simulation.

        The simulation does not perform the API operations, it only checks the
        authorization to determine if the simulated policies allow or deny the
        operations.

        **Note:** This API discloses information about the permissions granted to other
        users. If you do not want users to see other user's permissions, then consider
        allowing them to use SimulateCustomPolicy instead.

        Context keys are variables maintained by AWS and its services that provide
        details about the context of an API query request. You can use the `Condition`
        element of an IAM policy to evaluate context keys. To get the list of context
        keys that the policies require for correct simulation, use
        GetContextKeysForPrincipalPolicy.

        If the output is long, you can use the `MaxItems` and `Marker` parameters to
        paginate the results.
        """
        if _request is None:
            _params = {}
            if policy_source_arn is not ShapeBase.NOT_SET:
                _params['policy_source_arn'] = policy_source_arn
            if action_names is not ShapeBase.NOT_SET:
                _params['action_names'] = action_names
            if policy_input_list is not ShapeBase.NOT_SET:
                _params['policy_input_list'] = policy_input_list
            if resource_arns is not ShapeBase.NOT_SET:
                _params['resource_arns'] = resource_arns
            if resource_policy is not ShapeBase.NOT_SET:
                _params['resource_policy'] = resource_policy
            if resource_owner is not ShapeBase.NOT_SET:
                _params['resource_owner'] = resource_owner
            if caller_arn is not ShapeBase.NOT_SET:
                _params['caller_arn'] = caller_arn
            if context_entries is not ShapeBase.NOT_SET:
                _params['context_entries'] = context_entries
            if resource_handling_option is not ShapeBase.NOT_SET:
                _params['resource_handling_option'] = resource_handling_option
            if max_items is not ShapeBase.NOT_SET:
                _params['max_items'] = max_items
            if marker is not ShapeBase.NOT_SET:
                _params['marker'] = marker
            _request = shapes.SimulatePrincipalPolicyRequest(**_params)
        paginator = self.get_paginator("simulate_principal_policy").paginate(
            **_request.to_boto()
        )
        page_generator = (page for page in paginator)
        first_page = next(page_generator)
        result = shapes.SimulatePolicyResponse.from_boto(first_page)
        result._page_iterator = page_generator
        return result

        return shapes.SimulatePolicyResponse.from_boto(response)

    def update_access_key(
        self,
        _request: shapes.UpdateAccessKeyRequest = None,
        *,
        access_key_id: str,
        status: typing.Union[str, shapes.statusType],
        user_name: str = ShapeBase.NOT_SET,
    ) -> None:
        """
        Changes the status of the specified access key from Active to Inactive, or vice
        versa. This operation can be used to disable a user's key as part of a key
        rotation workflow.

        If the `UserName` field is not specified, the user name is determined implicitly
        based on the AWS access key ID used to sign the request. Because this operation
        works for access keys under the AWS account, you can use this operation to
        manage AWS account root user credentials even if the AWS account has no
        associated users.

        For information about rotating keys, see [Managing Keys and
        Certificates](http://docs.aws.amazon.com/IAM/latest/UserGuide/ManagingCredentials.html)
        in the _IAM User Guide_.
        """
        if _request is None:
            _params = {}
            if access_key_id is not ShapeBase.NOT_SET:
                _params['access_key_id'] = access_key_id
            if status is not ShapeBase.NOT_SET:
                _params['status'] = status
            if user_name is not ShapeBase.NOT_SET:
                _params['user_name'] = user_name
            _request = shapes.UpdateAccessKeyRequest(**_params)
        response = self._boto_client.update_access_key(**_request.to_boto())

    def update_account_password_policy(
        self,
        _request: shapes.UpdateAccountPasswordPolicyRequest = None,
        *,
        minimum_password_length: int = ShapeBase.NOT_SET,
        require_symbols: bool = ShapeBase.NOT_SET,
        require_numbers: bool = ShapeBase.NOT_SET,
        require_uppercase_characters: bool = ShapeBase.NOT_SET,
        require_lowercase_characters: bool = ShapeBase.NOT_SET,
        allow_users_to_change_password: bool = ShapeBase.NOT_SET,
        max_password_age: int = ShapeBase.NOT_SET,
        password_reuse_prevention: int = ShapeBase.NOT_SET,
        hard_expiry: bool = ShapeBase.NOT_SET,
    ) -> None:
        """
        Updates the password policy settings for the AWS account.

          * This operation does not support partial updates. No parameters are required, but if you do not specify a parameter, that parameter's value reverts to its default value. See the **Request Parameters** section for each parameter's default value. Also note that some parameters do not allow the default parameter to be explicitly set. Instead, to invoke the default value, do not include that parameter when you invoke the operation.

        For more information about using a password policy, see [Managing an IAM
        Password
        Policy](http://docs.aws.amazon.com/IAM/latest/UserGuide/Using_ManagingPasswordPolicies.html)
        in the _IAM User Guide_.
        """
        if _request is None:
            _params = {}
            if minimum_password_length is not ShapeBase.NOT_SET:
                _params['minimum_password_length'] = minimum_password_length
            if require_symbols is not ShapeBase.NOT_SET:
                _params['require_symbols'] = require_symbols
            if require_numbers is not ShapeBase.NOT_SET:
                _params['require_numbers'] = require_numbers
            if require_uppercase_characters is not ShapeBase.NOT_SET:
                _params['require_uppercase_characters'
                       ] = require_uppercase_characters
            if require_lowercase_characters is not ShapeBase.NOT_SET:
                _params['require_lowercase_characters'
                       ] = require_lowercase_characters
            if allow_users_to_change_password is not ShapeBase.NOT_SET:
                _params['allow_users_to_change_password'
                       ] = allow_users_to_change_password
            if max_password_age is not ShapeBase.NOT_SET:
                _params['max_password_age'] = max_password_age
            if password_reuse_prevention is not ShapeBase.NOT_SET:
                _params['password_reuse_prevention'] = password_reuse_prevention
            if hard_expiry is not ShapeBase.NOT_SET:
                _params['hard_expiry'] = hard_expiry
            _request = shapes.UpdateAccountPasswordPolicyRequest(**_params)
        response = self._boto_client.update_account_password_policy(
            **_request.to_boto()
        )

    def update_assume_role_policy(
        self,
        _request: shapes.UpdateAssumeRolePolicyRequest = None,
        *,
        role_name: str,
        policy_document: str,
    ) -> None:
        """
        Updates the policy that grants an IAM entity permission to assume a role. This
        is typically referred to as the "role trust policy". For more information about
        roles, go to [Using Roles to Delegate Permissions and Federate
        Identities](http://docs.aws.amazon.com/IAM/latest/UserGuide/roles-
        toplevel.html).
        """
        if _request is None:
            _params = {}
            if role_name is not ShapeBase.NOT_SET:
                _params['role_name'] = role_name
            if policy_document is not ShapeBase.NOT_SET:
                _params['policy_document'] = policy_document
            _request = shapes.UpdateAssumeRolePolicyRequest(**_params)
        response = self._boto_client.update_assume_role_policy(
            **_request.to_boto()
        )

    def update_group(
        self,
        _request: shapes.UpdateGroupRequest = None,
        *,
        group_name: str,
        new_path: str = ShapeBase.NOT_SET,
        new_group_name: str = ShapeBase.NOT_SET,
    ) -> None:
        """
        Updates the name and/or the path of the specified IAM group.

        You should understand the implications of changing a group's path or name. For
        more information, see [Renaming Users and
        Groups](http://docs.aws.amazon.com/IAM/latest/UserGuide/Using_WorkingWithGroupsAndUsers.html)
        in the _IAM User Guide_.

        The person making the request (the principal), must have permission to change
        the role group with the old name and the new name. For example, to change the
        group named `Managers` to `MGRs`, the principal must have a policy that allows
        them to update both groups. If the principal has permission to update the
        `Managers` group, but not the `MGRs` group, then the update fails. For more
        information about permissions, see [Access
        Management](http://docs.aws.amazon.com/IAM/latest/UserGuide/access.html).
        """
        if _request is None:
            _params = {}
            if group_name is not ShapeBase.NOT_SET:
                _params['group_name'] = group_name
            if new_path is not ShapeBase.NOT_SET:
                _params['new_path'] = new_path
            if new_group_name is not ShapeBase.NOT_SET:
                _params['new_group_name'] = new_group_name
            _request = shapes.UpdateGroupRequest(**_params)
        response = self._boto_client.update_group(**_request.to_boto())

    def update_login_profile(
        self,
        _request: shapes.UpdateLoginProfileRequest = None,
        *,
        user_name: str,
        password: str = ShapeBase.NOT_SET,
        password_reset_required: bool = ShapeBase.NOT_SET,
    ) -> None:
        """
        Changes the password for the specified IAM user.

        IAM users can change their own passwords by calling ChangePassword. For more
        information about modifying passwords, see [Managing
        Passwords](http://docs.aws.amazon.com/IAM/latest/UserGuide/Using_ManagingLogins.html)
        in the _IAM User Guide_.
        """
        if _request is None:
            _params = {}
            if user_name is not ShapeBase.NOT_SET:
                _params['user_name'] = user_name
            if password is not ShapeBase.NOT_SET:
                _params['password'] = password
            if password_reset_required is not ShapeBase.NOT_SET:
                _params['password_reset_required'] = password_reset_required
            _request = shapes.UpdateLoginProfileRequest(**_params)
        response = self._boto_client.update_login_profile(**_request.to_boto())

    def update_open_id_connect_provider_thumbprint(
        self,
        _request: shapes.UpdateOpenIDConnectProviderThumbprintRequest = None,
        *,
        open_id_connect_provider_arn: str,
        thumbprint_list: typing.List[str],
    ) -> None:
        """
        Replaces the existing list of server certificate thumbprints associated with an
        OpenID Connect (OIDC) provider resource object with a new list of thumbprints.

        The list that you pass with this operation completely replaces the existing list
        of thumbprints. (The lists are not merged.)

        Typically, you need to update a thumbprint only when the identity provider's
        certificate changes, which occurs rarely. However, if the provider's certificate
        _does_ change, any attempt to assume an IAM role that specifies the OIDC
        provider as a principal fails until the certificate thumbprint is updated.

        Because trust for the OIDC provider is derived from the provider's certificate
        and is validated by the thumbprint, it is best to limit access to the
        `UpdateOpenIDConnectProviderThumbprint` operation to highly privileged users.
        """
        if _request is None:
            _params = {}
            if open_id_connect_provider_arn is not ShapeBase.NOT_SET:
                _params['open_id_connect_provider_arn'
                       ] = open_id_connect_provider_arn
            if thumbprint_list is not ShapeBase.NOT_SET:
                _params['thumbprint_list'] = thumbprint_list
            _request = shapes.UpdateOpenIDConnectProviderThumbprintRequest(
                **_params
            )
        response = self._boto_client.update_open_id_connect_provider_thumbprint(
            **_request.to_boto()
        )

    def update_role(
        self,
        _request: shapes.UpdateRoleRequest = None,
        *,
        role_name: str,
        description: str = ShapeBase.NOT_SET,
        max_session_duration: int = ShapeBase.NOT_SET,
    ) -> shapes.UpdateRoleResponse:
        """
        Updates the description or maximum session duration setting of a role.
        """
        if _request is None:
            _params = {}
            if role_name is not ShapeBase.NOT_SET:
                _params['role_name'] = role_name
            if description is not ShapeBase.NOT_SET:
                _params['description'] = description
            if max_session_duration is not ShapeBase.NOT_SET:
                _params['max_session_duration'] = max_session_duration
            _request = shapes.UpdateRoleRequest(**_params)
        response = self._boto_client.update_role(**_request.to_boto())

        return shapes.UpdateRoleResponse.from_boto(response)

    def update_role_description(
        self,
        _request: shapes.UpdateRoleDescriptionRequest = None,
        *,
        role_name: str,
        description: str,
    ) -> shapes.UpdateRoleDescriptionResponse:
        """
        Use instead.

        Modifies only the description of a role. This operation performs the same
        function as the `Description` parameter in the `UpdateRole` operation.
        """
        if _request is None:
            _params = {}
            if role_name is not ShapeBase.NOT_SET:
                _params['role_name'] = role_name
            if description is not ShapeBase.NOT_SET:
                _params['description'] = description
            _request = shapes.UpdateRoleDescriptionRequest(**_params)
        response = self._boto_client.update_role_description(
            **_request.to_boto()
        )

        return shapes.UpdateRoleDescriptionResponse.from_boto(response)

    def update_saml_provider(
        self,
        _request: shapes.UpdateSAMLProviderRequest = None,
        *,
        saml_metadata_document: str,
        saml_provider_arn: str,
    ) -> shapes.UpdateSAMLProviderResponse:
        """
        Updates the metadata document for an existing SAML provider resource object.

        This operation requires [Signature Version
        4](http://docs.aws.amazon.com/general/latest/gr/signature-version-4.html).
        """
        if _request is None:
            _params = {}
            if saml_metadata_document is not ShapeBase.NOT_SET:
                _params['saml_metadata_document'] = saml_metadata_document
            if saml_provider_arn is not ShapeBase.NOT_SET:
                _params['saml_provider_arn'] = saml_provider_arn
            _request = shapes.UpdateSAMLProviderRequest(**_params)
        response = self._boto_client.update_saml_provider(**_request.to_boto())

        return shapes.UpdateSAMLProviderResponse.from_boto(response)

    def update_ssh_public_key(
        self,
        _request: shapes.UpdateSSHPublicKeyRequest = None,
        *,
        user_name: str,
        ssh_public_key_id: str,
        status: typing.Union[str, shapes.statusType],
    ) -> None:
        """
        Sets the status of an IAM user's SSH public key to active or inactive. SSH
        public keys that are inactive cannot be used for authentication. This operation
        can be used to disable a user's SSH public key as part of a key rotation work
        flow.

        The SSH public key affected by this operation is used only for authenticating
        the associated IAM user to an AWS CodeCommit repository. For more information
        about using SSH keys to authenticate to an AWS CodeCommit repository, see [Set
        up AWS CodeCommit for SSH
        Connections](http://docs.aws.amazon.com/codecommit/latest/userguide/setting-up-
        credentials-ssh.html) in the _AWS CodeCommit User Guide_.
        """
        if _request is None:
            _params = {}
            if user_name is not ShapeBase.NOT_SET:
                _params['user_name'] = user_name
            if ssh_public_key_id is not ShapeBase.NOT_SET:
                _params['ssh_public_key_id'] = ssh_public_key_id
            if status is not ShapeBase.NOT_SET:
                _params['status'] = status
            _request = shapes.UpdateSSHPublicKeyRequest(**_params)
        response = self._boto_client.update_ssh_public_key(**_request.to_boto())

    def update_server_certificate(
        self,
        _request: shapes.UpdateServerCertificateRequest = None,
        *,
        server_certificate_name: str,
        new_path: str = ShapeBase.NOT_SET,
        new_server_certificate_name: str = ShapeBase.NOT_SET,
    ) -> None:
        """
        Updates the name and/or the path of the specified server certificate stored in
        IAM.

        For more information about working with server certificates, see [Working with
        Server
        Certificates](http://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_server-
        certs.html) in the _IAM User Guide_. This topic also includes a list of AWS
        services that can use the server certificates that you manage with IAM.

        You should understand the implications of changing a server certificate's path
        or name. For more information, see [Renaming a Server
        Certificate](http://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_server-
        certs_manage.html#RenamingServerCerts) in the _IAM User Guide_.

        The person making the request (the principal), must have permission to change
        the server certificate with the old name and the new name. For example, to
        change the certificate named `ProductionCert` to `ProdCert`, the principal must
        have a policy that allows them to update both certificates. If the principal has
        permission to update the `ProductionCert` group, but not the `ProdCert`
        certificate, then the update fails. For more information about permissions, see
        [Access Management](http://docs.aws.amazon.com/IAM/latest/UserGuide/access.html)
        in the _IAM User Guide_.
        """
        if _request is None:
            _params = {}
            if server_certificate_name is not ShapeBase.NOT_SET:
                _params['server_certificate_name'] = server_certificate_name
            if new_path is not ShapeBase.NOT_SET:
                _params['new_path'] = new_path
            if new_server_certificate_name is not ShapeBase.NOT_SET:
                _params['new_server_certificate_name'
                       ] = new_server_certificate_name
            _request = shapes.UpdateServerCertificateRequest(**_params)
        response = self._boto_client.update_server_certificate(
            **_request.to_boto()
        )

    def update_service_specific_credential(
        self,
        _request: shapes.UpdateServiceSpecificCredentialRequest = None,
        *,
        service_specific_credential_id: str,
        status: typing.Union[str, shapes.statusType],
        user_name: str = ShapeBase.NOT_SET,
    ) -> None:
        """
        Sets the status of a service-specific credential to `Active` or `Inactive`.
        Service-specific credentials that are inactive cannot be used for authentication
        to the service. This operation can be used to disable a user's service-specific
        credential as part of a credential rotation work flow.
        """
        if _request is None:
            _params = {}
            if service_specific_credential_id is not ShapeBase.NOT_SET:
                _params['service_specific_credential_id'
                       ] = service_specific_credential_id
            if status is not ShapeBase.NOT_SET:
                _params['status'] = status
            if user_name is not ShapeBase.NOT_SET:
                _params['user_name'] = user_name
            _request = shapes.UpdateServiceSpecificCredentialRequest(**_params)
        response = self._boto_client.update_service_specific_credential(
            **_request.to_boto()
        )

    def update_signing_certificate(
        self,
        _request: shapes.UpdateSigningCertificateRequest = None,
        *,
        certificate_id: str,
        status: typing.Union[str, shapes.statusType],
        user_name: str = ShapeBase.NOT_SET,
    ) -> None:
        """
        Changes the status of the specified user signing certificate from active to
        disabled, or vice versa. This operation can be used to disable an IAM user's
        signing certificate as part of a certificate rotation work flow.

        If the `UserName` field is not specified, the user name is determined implicitly
        based on the AWS access key ID used to sign the request. Because this operation
        works for access keys under the AWS account, you can use this operation to
        manage AWS account root user credentials even if the AWS account has no
        associated users.
        """
        if _request is None:
            _params = {}
            if certificate_id is not ShapeBase.NOT_SET:
                _params['certificate_id'] = certificate_id
            if status is not ShapeBase.NOT_SET:
                _params['status'] = status
            if user_name is not ShapeBase.NOT_SET:
                _params['user_name'] = user_name
            _request = shapes.UpdateSigningCertificateRequest(**_params)
        response = self._boto_client.update_signing_certificate(
            **_request.to_boto()
        )

    def update_user(
        self,
        _request: shapes.UpdateUserRequest = None,
        *,
        user_name: str,
        new_path: str = ShapeBase.NOT_SET,
        new_user_name: str = ShapeBase.NOT_SET,
    ) -> None:
        """
        Updates the name and/or the path of the specified IAM user.

        You should understand the implications of changing an IAM user's path or name.
        For more information, see [Renaming an IAM
        User](http://docs.aws.amazon.com/IAM/latest/UserGuide/id_users_manage.html#id_users_renaming)
        and [Renaming an IAM
        Group](http://docs.aws.amazon.com/IAM/latest/UserGuide/id_groups_manage_rename.html)
        in the _IAM User Guide_.

        To change a user name, the requester must have appropriate permissions on both
        the source object and the target object. For example, to change Bob to Robert,
        the entity making the request must have permission on Bob and Robert, or must
        have permission on all (*). For more information about permissions, see
        [Permissions and
        Policies](http://docs.aws.amazon.com/IAM/latest/UserGuide/PermissionsAndPolicies.html).
        """
        if _request is None:
            _params = {}
            if user_name is not ShapeBase.NOT_SET:
                _params['user_name'] = user_name
            if new_path is not ShapeBase.NOT_SET:
                _params['new_path'] = new_path
            if new_user_name is not ShapeBase.NOT_SET:
                _params['new_user_name'] = new_user_name
            _request = shapes.UpdateUserRequest(**_params)
        response = self._boto_client.update_user(**_request.to_boto())

    def upload_ssh_public_key(
        self,
        _request: shapes.UploadSSHPublicKeyRequest = None,
        *,
        user_name: str,
        ssh_public_key_body: str,
    ) -> shapes.UploadSSHPublicKeyResponse:
        """
        Uploads an SSH public key and associates it with the specified IAM user.

        The SSH public key uploaded by this operation can be used only for
        authenticating the associated IAM user to an AWS CodeCommit repository. For more
        information about using SSH keys to authenticate to an AWS CodeCommit
        repository, see [Set up AWS CodeCommit for SSH
        Connections](http://docs.aws.amazon.com/codecommit/latest/userguide/setting-up-
        credentials-ssh.html) in the _AWS CodeCommit User Guide_.
        """
        if _request is None:
            _params = {}
            if user_name is not ShapeBase.NOT_SET:
                _params['user_name'] = user_name
            if ssh_public_key_body is not ShapeBase.NOT_SET:
                _params['ssh_public_key_body'] = ssh_public_key_body
            _request = shapes.UploadSSHPublicKeyRequest(**_params)
        response = self._boto_client.upload_ssh_public_key(**_request.to_boto())

        return shapes.UploadSSHPublicKeyResponse.from_boto(response)

    def upload_server_certificate(
        self,
        _request: shapes.UploadServerCertificateRequest = None,
        *,
        server_certificate_name: str,
        certificate_body: str,
        private_key: str,
        path: str = ShapeBase.NOT_SET,
        certificate_chain: str = ShapeBase.NOT_SET,
    ) -> shapes.UploadServerCertificateResponse:
        """
        Uploads a server certificate entity for the AWS account. The server certificate
        entity includes a public key certificate, a private key, and an optional
        certificate chain, which should all be PEM-encoded.

        We recommend that you use [AWS Certificate
        Manager](https://aws.amazon.com/certificate-manager/) to provision, manage, and
        deploy your server certificates. With ACM you can request a certificate, deploy
        it to AWS resources, and let ACM handle certificate renewals for you.
        Certificates provided by ACM are free. For more information about using ACM, see
        the [AWS Certificate Manager User
        Guide](http://docs.aws.amazon.com/acm/latest/userguide/).

        For more information about working with server certificates, see [Working with
        Server
        Certificates](http://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_server-
        certs.html) in the _IAM User Guide_. This topic includes a list of AWS services
        that can use the server certificates that you manage with IAM.

        For information about the number of server certificates you can upload, see
        [Limitations on IAM Entities and
        Objects](http://docs.aws.amazon.com/IAM/latest/UserGuide/reference_iam-
        limits.html) in the _IAM User Guide_.

        Because the body of the public key certificate, private key, and the certificate
        chain can be large, you should use POST rather than GET when calling
        `UploadServerCertificate`. For information about setting up signatures and
        authorization through the API, go to [Signing AWS API
        Requests](http://docs.aws.amazon.com/general/latest/gr/signing_aws_api_requests.html)
        in the _AWS General Reference_. For general information about using the Query
        API with IAM, go to [Calling the API by Making HTTP Query
        Requests](http://docs.aws.amazon.com/IAM/latest/UserGuide/programming.html) in
        the _IAM User Guide_.
        """
        if _request is None:
            _params = {}
            if server_certificate_name is not ShapeBase.NOT_SET:
                _params['server_certificate_name'] = server_certificate_name
            if certificate_body is not ShapeBase.NOT_SET:
                _params['certificate_body'] = certificate_body
            if private_key is not ShapeBase.NOT_SET:
                _params['private_key'] = private_key
            if path is not ShapeBase.NOT_SET:
                _params['path'] = path
            if certificate_chain is not ShapeBase.NOT_SET:
                _params['certificate_chain'] = certificate_chain
            _request = shapes.UploadServerCertificateRequest(**_params)
        response = self._boto_client.upload_server_certificate(
            **_request.to_boto()
        )

        return shapes.UploadServerCertificateResponse.from_boto(response)

    def upload_signing_certificate(
        self,
        _request: shapes.UploadSigningCertificateRequest = None,
        *,
        certificate_body: str,
        user_name: str = ShapeBase.NOT_SET,
    ) -> shapes.UploadSigningCertificateResponse:
        """
        Uploads an X.509 signing certificate and associates it with the specified IAM
        user. Some AWS services use X.509 signing certificates to validate requests that
        are signed with a corresponding private key. When you upload the certificate,
        its default status is `Active`.

        If the `UserName` field is not specified, the IAM user name is determined
        implicitly based on the AWS access key ID used to sign the request. Because this
        operation works for access keys under the AWS account, you can use this
        operation to manage AWS account root user credentials even if the AWS account
        has no associated users.

        Because the body of an X.509 certificate can be large, you should use POST
        rather than GET when calling `UploadSigningCertificate`. For information about
        setting up signatures and authorization through the API, go to [Signing AWS API
        Requests](http://docs.aws.amazon.com/general/latest/gr/signing_aws_api_requests.html)
        in the _AWS General Reference_. For general information about using the Query
        API with IAM, go to [Making Query
        Requests](http://docs.aws.amazon.com/IAM/latest/UserGuide/IAM_UsingQueryAPI.html)
        in the _IAM User Guide_.
        """
        if _request is None:
            _params = {}
            if certificate_body is not ShapeBase.NOT_SET:
                _params['certificate_body'] = certificate_body
            if user_name is not ShapeBase.NOT_SET:
                _params['user_name'] = user_name
            _request = shapes.UploadSigningCertificateRequest(**_params)
        response = self._boto_client.upload_signing_certificate(
            **_request.to_boto()
        )

        return shapes.UploadSigningCertificateResponse.from_boto(response)
