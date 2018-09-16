import datetime
import typing
import boto3
from autoboto import ClientBase, ShapeBase, OutputShapeBase
from . import shapes


class Client(ClientBase):
    def __init__(self, *args, **kwargs):
        super().__init__("organizations", *args, **kwargs)

    def accept_handshake(
        self,
        _request: shapes.AcceptHandshakeRequest = None,
        *,
        handshake_id: str,
    ) -> shapes.AcceptHandshakeResponse:
        """
        Sends a response to the originator of a handshake agreeing to the action
        proposed by the handshake request.

        This operation can be called only by the following principals when they also
        have the relevant IAM permissions:

          * **Invitation to join** or **Approve all features request** handshakes: only a principal from the member account. 

        The user who calls the API for an invitation to join must have the
        `organizations:AcceptHandshake` permission. If you enabled all features in the
        organization, then the user must also have the `iam:CreateServiceLinkedRole`
        permission so that Organizations can create the required service-linked role
        named _OrgsServiceLinkedRoleName_. For more information, see [AWS Organizations
        and Service-Linked
        Roles](http://docs.aws.amazon.com/organizations/latest/userguide/orgs_integration_services.html#orgs_integration_service-
        linked-roles) in the _AWS Organizations User Guide_.

          * **Enable all features final confirmation** handshake: only a principal from the master account.

        For more information about invitations, see [Inviting an AWS Account to Join
        Your
        Organization](http://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_accounts_invites.html)
        in the _AWS Organizations User Guide_. For more information about requests to
        enable all features in the organization, see [Enabling All Features in Your
        Organization](http://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_org_support-
        all-features.html) in the _AWS Organizations User Guide_.

        After you accept a handshake, it continues to appear in the results of relevant
        APIs for only 30 days. After that it is deleted.
        """
        if _request is None:
            _params = {}
            if handshake_id is not ShapeBase.NOT_SET:
                _params['handshake_id'] = handshake_id
            _request = shapes.AcceptHandshakeRequest(**_params)
        response = self._boto_client.accept_handshake(**_request.to_boto())

        return shapes.AcceptHandshakeResponse.from_boto(response)

    def attach_policy(
        self,
        _request: shapes.AttachPolicyRequest = None,
        *,
        policy_id: str,
        target_id: str,
    ) -> None:
        """
        Attaches a policy to a root, an organizational unit (OU), or an individual
        account. How the policy affects accounts depends on the type of policy:

          * **Service control policy (SCP)** \- An SCP specifies what permissions can be delegated to users in affected member accounts. The scope of influence for a policy depends on what you attach the policy to:

            * If you attach an SCP to a root, it affects all accounts in the organization.

            * If you attach an SCP to an OU, it affects all accounts in that OU and in any child OUs.

            * If you attach the policy directly to an account, then it affects only that account.

        SCPs essentially are permission "filters". When you attach one SCP to a higher
        level root or OU, and you also attach a different SCP to a child OU or to an
        account, the child policy can further restrict only the permissions that pass
        through the parent filter and are available to the child. An SCP that is
        attached to a child cannot grant a permission that is not already granted by the
        parent. For example, imagine that the parent SCP allows permissions A, B, C, D,
        and E. The child SCP allows C, D, E, F, and G. The result is that the accounts
        affected by the child SCP are allowed to use only C, D, and E. They cannot use A
        or B because they were filtered out by the child OU. They also cannot use F and
        G because they were filtered out by the parent OU. They cannot be granted back
        by the child SCP; child SCPs can only filter the permissions they receive from
        the parent SCP.

        AWS Organizations attaches a default SCP named `"FullAWSAccess` to every root,
        OU, and account. This default SCP allows all services and actions, enabling any
        new child OU or account to inherit the permissions of the parent root or OU. If
        you detach the default policy, you must replace it with a policy that specifies
        the permissions that you want to allow in that OU or account.

        For more information about how Organizations policies permissions work, see
        [Using Service Control
        Policies](http://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_scp.html)
        in the _AWS Organizations User Guide_.

        This operation can be called only from the organization's master account.
        """
        if _request is None:
            _params = {}
            if policy_id is not ShapeBase.NOT_SET:
                _params['policy_id'] = policy_id
            if target_id is not ShapeBase.NOT_SET:
                _params['target_id'] = target_id
            _request = shapes.AttachPolicyRequest(**_params)
        response = self._boto_client.attach_policy(**_request.to_boto())

    def cancel_handshake(
        self,
        _request: shapes.CancelHandshakeRequest = None,
        *,
        handshake_id: str,
    ) -> shapes.CancelHandshakeResponse:
        """
        Cancels a handshake. Canceling a handshake sets the handshake state to
        `CANCELED`.

        This operation can be called only from the account that originated the
        handshake. The recipient of the handshake can't cancel it, but can use
        DeclineHandshake instead. After a handshake is canceled, the recipient can no
        longer respond to that handshake.

        After you cancel a handshake, it continues to appear in the results of relevant
        APIs for only 30 days. After that it is deleted.
        """
        if _request is None:
            _params = {}
            if handshake_id is not ShapeBase.NOT_SET:
                _params['handshake_id'] = handshake_id
            _request = shapes.CancelHandshakeRequest(**_params)
        response = self._boto_client.cancel_handshake(**_request.to_boto())

        return shapes.CancelHandshakeResponse.from_boto(response)

    def create_account(
        self,
        _request: shapes.CreateAccountRequest = None,
        *,
        email: str,
        account_name: str,
        role_name: str = ShapeBase.NOT_SET,
        iam_user_access_to_billing: typing.
        Union[str, shapes.IAMUserAccessToBilling] = ShapeBase.NOT_SET,
    ) -> shapes.CreateAccountResponse:
        """
        Creates an AWS account that is automatically a member of the organization whose
        credentials made the request. This is an asynchronous request that AWS performs
        in the background. If you want to check the status of the request later, you
        need the `OperationId` response element from this operation to provide as a
        parameter to the DescribeCreateAccountStatus operation.

        The user who calls the API for an invitation to join must have the
        `organizations:CreateAccount` permission. If you enabled all features in the
        organization, then the user must also have the `iam:CreateServiceLinkedRole`
        permission so that Organizations can create the required service-linked role
        named _OrgsServiceLinkedRoleName_. For more information, see [AWS Organizations
        and Service-Linked
        Roles](http://docs.aws.amazon.com/organizations/latest/userguide/orgs_integration_services.html#orgs_integration_service-
        linked-roles) in the _AWS Organizations User Guide_.

        The user in the master account who calls this API must also have the
        `iam:CreateRole` permission because AWS Organizations preconfigures the new
        member account with a role (named `OrganizationAccountAccessRole` by default)
        that grants users in the master account administrator permissions in the new
        member account. Principals in the master account can assume the role. AWS
        Organizations clones the company name and address information for the new
        account from the organization's master account.

        This operation can be called only from the organization's master account.

        For more information about creating accounts, see [Creating an AWS Account in
        Your
        Organization](http://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_accounts_create.html)
        in the _AWS Organizations User Guide_.

          * When you create an account in an organization using the AWS Organizations console, API, or CLI commands, the information required for the account to operate as a standalone account, such as a payment method and signing the End User Licence Agreement (EULA) is _not_ automatically collected. If you must remove an account from your organization later, you can do so only after you provide the missing information. Follow the steps at [ To leave an organization when all required account information has not yet been provided](http://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_accounts_remove.html#leave-without-all-info) in the _AWS Organizations User Guide_.

          * If you get an exception that indicates that you exceeded your account limits for the organization or that the operation failed because your organization is still initializing, wait one hour and then try again. If the error persists after an hour, then contact [AWS Customer Support](https://console.aws.amazon.com/support/home#/).

          * Because `CreateAccount` operates asynchronously, it can return a successful completion message even though account initialization might still be in progress. You might need to wait a few minutes before you can successfully access the account. 

        When you create a member account with this operation, you can choose whether to
        create the account with the **IAM User and Role Access to Billing Information**
        switch enabled. If you enable it, IAM users and roles that have appropriate
        permissions can view billing information for the account. If you disable this,
        then only the account root user can access billing information. For information
        about how to disable this for an account, see [Granting Access to Your Billing
        Information and
        Tools](http://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/grantaccess.html).
        """
        if _request is None:
            _params = {}
            if email is not ShapeBase.NOT_SET:
                _params['email'] = email
            if account_name is not ShapeBase.NOT_SET:
                _params['account_name'] = account_name
            if role_name is not ShapeBase.NOT_SET:
                _params['role_name'] = role_name
            if iam_user_access_to_billing is not ShapeBase.NOT_SET:
                _params['iam_user_access_to_billing'
                       ] = iam_user_access_to_billing
            _request = shapes.CreateAccountRequest(**_params)
        response = self._boto_client.create_account(**_request.to_boto())

        return shapes.CreateAccountResponse.from_boto(response)

    def create_organization(
        self,
        _request: shapes.CreateOrganizationRequest = None,
        *,
        feature_set: typing.Union[str, shapes.
                                  OrganizationFeatureSet] = ShapeBase.NOT_SET,
    ) -> shapes.CreateOrganizationResponse:
        """
        Creates an AWS organization. The account whose user is calling the
        CreateOrganization operation automatically becomes the [master
        account](http://docs.aws.amazon.com/IAM/latest/UserGuide/orgs_getting-
        started_concepts.html#account) of the new organization.

        This operation must be called using credentials from the account that is to
        become the new organization's master account. The principal must also have the
        relevant IAM permissions.

        By default (or if you set the `FeatureSet` parameter to `ALL`), the new
        organization is created with all features enabled and service control policies
        automatically enabled in the root. If you instead choose to create the
        organization supporting only the consolidated billing features by setting the
        `FeatureSet` parameter to `CONSOLIDATED_BILLING"`, then no policy types are
        enabled by default and you cannot use organization policies.
        """
        if _request is None:
            _params = {}
            if feature_set is not ShapeBase.NOT_SET:
                _params['feature_set'] = feature_set
            _request = shapes.CreateOrganizationRequest(**_params)
        response = self._boto_client.create_organization(**_request.to_boto())

        return shapes.CreateOrganizationResponse.from_boto(response)

    def create_organizational_unit(
        self,
        _request: shapes.CreateOrganizationalUnitRequest = None,
        *,
        parent_id: str,
        name: str,
    ) -> shapes.CreateOrganizationalUnitResponse:
        """
        Creates an organizational unit (OU) within a root or parent OU. An OU is a
        container for accounts that enables you to organize your accounts to apply
        policies according to your business requirements. The number of levels deep that
        you can nest OUs is dependent upon the policy types enabled for that root. For
        service control policies, the limit is five.

        For more information about OUs, see [Managing Organizational
        Units](http://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_ous.html)
        in the _AWS Organizations User Guide_.

        This operation can be called only from the organization's master account.
        """
        if _request is None:
            _params = {}
            if parent_id is not ShapeBase.NOT_SET:
                _params['parent_id'] = parent_id
            if name is not ShapeBase.NOT_SET:
                _params['name'] = name
            _request = shapes.CreateOrganizationalUnitRequest(**_params)
        response = self._boto_client.create_organizational_unit(
            **_request.to_boto()
        )

        return shapes.CreateOrganizationalUnitResponse.from_boto(response)

    def create_policy(
        self,
        _request: shapes.CreatePolicyRequest = None,
        *,
        content: str,
        description: str,
        name: str,
        type: typing.Union[str, shapes.PolicyType],
    ) -> shapes.CreatePolicyResponse:
        """
        Creates a policy of a specified type that you can attach to a root, an
        organizational unit (OU), or an individual AWS account.

        For more information about policies and their use, see [Managing Organization
        Policies](http://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies.html).

        This operation can be called only from the organization's master account.
        """
        if _request is None:
            _params = {}
            if content is not ShapeBase.NOT_SET:
                _params['content'] = content
            if description is not ShapeBase.NOT_SET:
                _params['description'] = description
            if name is not ShapeBase.NOT_SET:
                _params['name'] = name
            if type is not ShapeBase.NOT_SET:
                _params['type'] = type
            _request = shapes.CreatePolicyRequest(**_params)
        response = self._boto_client.create_policy(**_request.to_boto())

        return shapes.CreatePolicyResponse.from_boto(response)

    def decline_handshake(
        self,
        _request: shapes.DeclineHandshakeRequest = None,
        *,
        handshake_id: str,
    ) -> shapes.DeclineHandshakeResponse:
        """
        Declines a handshake request. This sets the handshake state to `DECLINED` and
        effectively deactivates the request.

        This operation can be called only from the account that received the handshake.
        The originator of the handshake can use CancelHandshake instead. The originator
        can't reactivate a declined request, but can re-initiate the process with a new
        handshake request.

        After you decline a handshake, it continues to appear in the results of relevant
        APIs for only 30 days. After that it is deleted.
        """
        if _request is None:
            _params = {}
            if handshake_id is not ShapeBase.NOT_SET:
                _params['handshake_id'] = handshake_id
            _request = shapes.DeclineHandshakeRequest(**_params)
        response = self._boto_client.decline_handshake(**_request.to_boto())

        return shapes.DeclineHandshakeResponse.from_boto(response)

    def delete_organization(self) -> None:
        """
        Deletes the organization. You can delete an organization only by using
        credentials from the master account. The organization must be empty of member
        accounts, organizational units (OUs), and policies.
        """
        response = self._boto_client.delete_organization()

    def delete_organizational_unit(
        self,
        _request: shapes.DeleteOrganizationalUnitRequest = None,
        *,
        organizational_unit_id: str,
    ) -> None:
        """
        Deletes an organizational unit (OU) from a root or another OU. You must first
        remove all accounts and child OUs from the OU that you want to delete.

        This operation can be called only from the organization's master account.
        """
        if _request is None:
            _params = {}
            if organizational_unit_id is not ShapeBase.NOT_SET:
                _params['organizational_unit_id'] = organizational_unit_id
            _request = shapes.DeleteOrganizationalUnitRequest(**_params)
        response = self._boto_client.delete_organizational_unit(
            **_request.to_boto()
        )

    def delete_policy(
        self,
        _request: shapes.DeletePolicyRequest = None,
        *,
        policy_id: str,
    ) -> None:
        """
        Deletes the specified policy from your organization. Before you perform this
        operation, you must first detach the policy from all organizational units (OUs),
        roots, and accounts.

        This operation can be called only from the organization's master account.
        """
        if _request is None:
            _params = {}
            if policy_id is not ShapeBase.NOT_SET:
                _params['policy_id'] = policy_id
            _request = shapes.DeletePolicyRequest(**_params)
        response = self._boto_client.delete_policy(**_request.to_boto())

    def describe_account(
        self,
        _request: shapes.DescribeAccountRequest = None,
        *,
        account_id: str,
    ) -> shapes.DescribeAccountResponse:
        """
        Retrieves Organizations-related information about the specified account.

        This operation can be called only from the organization's master account.
        """
        if _request is None:
            _params = {}
            if account_id is not ShapeBase.NOT_SET:
                _params['account_id'] = account_id
            _request = shapes.DescribeAccountRequest(**_params)
        response = self._boto_client.describe_account(**_request.to_boto())

        return shapes.DescribeAccountResponse.from_boto(response)

    def describe_create_account_status(
        self,
        _request: shapes.DescribeCreateAccountStatusRequest = None,
        *,
        create_account_request_id: str,
    ) -> shapes.DescribeCreateAccountStatusResponse:
        """
        Retrieves the current status of an asynchronous request to create an account.

        This operation can be called only from the organization's master account.
        """
        if _request is None:
            _params = {}
            if create_account_request_id is not ShapeBase.NOT_SET:
                _params['create_account_request_id'] = create_account_request_id
            _request = shapes.DescribeCreateAccountStatusRequest(**_params)
        response = self._boto_client.describe_create_account_status(
            **_request.to_boto()
        )

        return shapes.DescribeCreateAccountStatusResponse.from_boto(response)

    def describe_handshake(
        self,
        _request: shapes.DescribeHandshakeRequest = None,
        *,
        handshake_id: str,
    ) -> shapes.DescribeHandshakeResponse:
        """
        Retrieves information about a previously requested handshake. The handshake ID
        comes from the response to the original InviteAccountToOrganization operation
        that generated the handshake.

        You can access handshakes that are ACCEPTED, DECLINED, or CANCELED for only 30
        days after they change to that state. They are then deleted and no longer
        accessible.

        This operation can be called from any account in the organization.
        """
        if _request is None:
            _params = {}
            if handshake_id is not ShapeBase.NOT_SET:
                _params['handshake_id'] = handshake_id
            _request = shapes.DescribeHandshakeRequest(**_params)
        response = self._boto_client.describe_handshake(**_request.to_boto())

        return shapes.DescribeHandshakeResponse.from_boto(response)

    def describe_organization(self, ) -> shapes.DescribeOrganizationResponse:
        """
        Retrieves information about the organization that the user's account belongs to.

        This operation can be called from any account in the organization.

        Even if a policy type is shown as available in the organization, it can be
        disabled separately at the root level with DisablePolicyType. Use ListRoots to
        see the status of policy types for a specified root.
        """
        response = self._boto_client.describe_organization()

        return shapes.DescribeOrganizationResponse.from_boto(response)

    def describe_organizational_unit(
        self,
        _request: shapes.DescribeOrganizationalUnitRequest = None,
        *,
        organizational_unit_id: str,
    ) -> shapes.DescribeOrganizationalUnitResponse:
        """
        Retrieves information about an organizational unit (OU).

        This operation can be called only from the organization's master account.
        """
        if _request is None:
            _params = {}
            if organizational_unit_id is not ShapeBase.NOT_SET:
                _params['organizational_unit_id'] = organizational_unit_id
            _request = shapes.DescribeOrganizationalUnitRequest(**_params)
        response = self._boto_client.describe_organizational_unit(
            **_request.to_boto()
        )

        return shapes.DescribeOrganizationalUnitResponse.from_boto(response)

    def describe_policy(
        self,
        _request: shapes.DescribePolicyRequest = None,
        *,
        policy_id: str,
    ) -> shapes.DescribePolicyResponse:
        """
        Retrieves information about a policy.

        This operation can be called only from the organization's master account.
        """
        if _request is None:
            _params = {}
            if policy_id is not ShapeBase.NOT_SET:
                _params['policy_id'] = policy_id
            _request = shapes.DescribePolicyRequest(**_params)
        response = self._boto_client.describe_policy(**_request.to_boto())

        return shapes.DescribePolicyResponse.from_boto(response)

    def detach_policy(
        self,
        _request: shapes.DetachPolicyRequest = None,
        *,
        policy_id: str,
        target_id: str,
    ) -> None:
        """
        Detaches a policy from a target root, organizational unit (OU), or account. If
        the policy being detached is a service control policy (SCP), the changes to
        permissions for IAM users and roles in affected accounts are immediate.

        **Note:** Every root, OU, and account must have at least one SCP attached. If
        you want to replace the default `FullAWSAccess` policy with one that limits the
        permissions that can be delegated, then you must attach the replacement policy
        before you can remove the default one. This is the authorization strategy of
        [whitelisting](http://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_about-
        scps.html#orgs_policies_whitelist). If you instead attach a second SCP and leave
        the `FullAWSAccess` SCP still attached, and specify `"Effect": "Deny"` in the
        second SCP to override the `"Effect": "Allow"` in the `FullAWSAccess` policy (or
        any other attached SCP), then you are using the authorization strategy of
        [blacklisting](http://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_about-
        scps.html#orgs_policies_blacklist).

        This operation can be called only from the organization's master account.
        """
        if _request is None:
            _params = {}
            if policy_id is not ShapeBase.NOT_SET:
                _params['policy_id'] = policy_id
            if target_id is not ShapeBase.NOT_SET:
                _params['target_id'] = target_id
            _request = shapes.DetachPolicyRequest(**_params)
        response = self._boto_client.detach_policy(**_request.to_boto())

    def disable_aws_service_access(
        self,
        _request: shapes.DisableAWSServiceAccessRequest = None,
        *,
        service_principal: str,
    ) -> None:
        """
        Disables the integration of an AWS service (the service that is specified by
        `ServicePrincipal`) with AWS Organizations. When you disable integration, the
        specified service no longer can create a [service-linked
        role](http://docs.aws.amazon.com/IAM/latest/UserGuide/using-service-linked-
        roles.html) in _new_ accounts in your organization. This means the service can't
        perform operations on your behalf on any new accounts in your organization. The
        service can still perform operations in older accounts until the service
        completes its clean-up from AWS Organizations.

        We recommend that you disable integration between AWS Organizations and the
        specified AWS service by using the console or commands that are provided by the
        specified service. Doing so ensures that the other service is aware that it can
        clean up any resources that are required only for the integration. How the
        service cleans up its resources in the organization's accounts depends on that
        service. For more information, see the documentation for the other AWS service.

        After you perform the `DisableAWSServiceAccess` operation, the specified service
        can no longer perform operations in your organization's accounts unless the
        operations are explicitly permitted by the IAM policies that are attached to
        your roles.

        For more information about integrating other services with AWS Organizations,
        including the list of services that work with Organizations, see [Integrating
        AWS Organizations with Other AWS
        Services](http://docs.aws.amazon.com/organizations/latest/userguide/orgs_integrate_services.html)
        in the _AWS Organizations User Guide_.

        This operation can be called only from the organization's master account.
        """
        if _request is None:
            _params = {}
            if service_principal is not ShapeBase.NOT_SET:
                _params['service_principal'] = service_principal
            _request = shapes.DisableAWSServiceAccessRequest(**_params)
        response = self._boto_client.disable_aws_service_access(
            **_request.to_boto()
        )

    def disable_policy_type(
        self,
        _request: shapes.DisablePolicyTypeRequest = None,
        *,
        root_id: str,
        policy_type: typing.Union[str, shapes.PolicyType],
    ) -> shapes.DisablePolicyTypeResponse:
        """
        Disables an organizational control policy type in a root. A policy of a certain
        type can be attached to entities in a root only if that type is enabled in the
        root. After you perform this operation, you no longer can attach policies of the
        specified type to that root or to any organizational unit (OU) or account in
        that root. You can undo this by using the EnablePolicyType operation.

        This operation can be called only from the organization's master account.

        If you disable a policy type for a root, it still shows as enabled for the
        organization if all features are enabled in that organization. Use ListRoots to
        see the status of policy types for a specified root. Use DescribeOrganization to
        see the status of policy types in the organization.
        """
        if _request is None:
            _params = {}
            if root_id is not ShapeBase.NOT_SET:
                _params['root_id'] = root_id
            if policy_type is not ShapeBase.NOT_SET:
                _params['policy_type'] = policy_type
            _request = shapes.DisablePolicyTypeRequest(**_params)
        response = self._boto_client.disable_policy_type(**_request.to_boto())

        return shapes.DisablePolicyTypeResponse.from_boto(response)

    def enable_aws_service_access(
        self,
        _request: shapes.EnableAWSServiceAccessRequest = None,
        *,
        service_principal: str,
    ) -> None:
        """
        Enables the integration of an AWS service (the service that is specified by
        `ServicePrincipal`) with AWS Organizations. When you enable integration, you
        allow the specified service to create a [service-linked
        role](http://docs.aws.amazon.com/IAM/latest/UserGuide/using-service-linked-
        roles.html) in all the accounts in your organization. This allows the service to
        perform operations on your behalf in your organization and its accounts.

        We recommend that you enable integration between AWS Organizations and the
        specified AWS service by using the console or commands that are provided by the
        specified service. Doing so ensures that the service is aware that it can create
        the resources that are required for the integration. How the service creates
        those resources in the organization's accounts depends on that service. For more
        information, see the documentation for the other AWS service.

        For more information about enabling services to integrate with AWS
        Organizations, see [Integrating AWS Organizations with Other AWS
        Services](http://docs.aws.amazon.com/organizations/latest/userguide/orgs_integrate_services.html)
        in the _AWS Organizations User Guide_.

        This operation can be called only from the organization's master account and
        only if the organization has [enabled all
        features](http://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_org_support-
        all-features.html).
        """
        if _request is None:
            _params = {}
            if service_principal is not ShapeBase.NOT_SET:
                _params['service_principal'] = service_principal
            _request = shapes.EnableAWSServiceAccessRequest(**_params)
        response = self._boto_client.enable_aws_service_access(
            **_request.to_boto()
        )

    def enable_all_features(
        self,
        _request: shapes.EnableAllFeaturesRequest = None,
    ) -> shapes.EnableAllFeaturesResponse:
        """
        Enables all features in an organization. This enables the use of organization
        policies that can restrict the services and actions that can be called in each
        account. Until you enable all features, you have access only to consolidated
        billing, and you can't use any of the advanced account administration features
        that AWS Organizations supports. For more information, see [Enabling All
        Features in Your
        Organization](http://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_org_support-
        all-features.html) in the _AWS Organizations User Guide_.

        This operation is required only for organizations that were created explicitly
        with only the consolidated billing features enabled. Calling this operation
        sends a handshake to every invited account in the organization. The feature set
        change can be finalized and the additional features enabled only after all
        administrators in the invited accounts approve the change by accepting the
        handshake.

        After you enable all features, you can separately enable or disable individual
        policy types in a root using EnablePolicyType and DisablePolicyType. To see the
        status of policy types in a root, use ListRoots.

        After all invited member accounts accept the handshake, you finalize the feature
        set change by accepting the handshake that contains `"Action":
        "ENABLE_ALL_FEATURES"`. This completes the change.

        After you enable all features in your organization, the master account in the
        organization can apply policies on all member accounts. These policies can
        restrict what users and even administrators in those accounts can do. The master
        account can apply policies that prevent accounts from leaving the organization.
        Ensure that your account administrators are aware of this.

        This operation can be called only from the organization's master account.
        """
        if _request is None:
            _params = {}
            _request = shapes.EnableAllFeaturesRequest(**_params)
        response = self._boto_client.enable_all_features(**_request.to_boto())

        return shapes.EnableAllFeaturesResponse.from_boto(response)

    def enable_policy_type(
        self,
        _request: shapes.EnablePolicyTypeRequest = None,
        *,
        root_id: str,
        policy_type: typing.Union[str, shapes.PolicyType],
    ) -> shapes.EnablePolicyTypeResponse:
        """
        Enables a policy type in a root. After you enable a policy type in a root, you
        can attach policies of that type to the root, any organizational unit (OU), or
        account in that root. You can undo this by using the DisablePolicyType
        operation.

        This operation can be called only from the organization's master account.

        You can enable a policy type in a root only if that policy type is available in
        the organization. Use DescribeOrganization to view the status of available
        policy types in the organization.

        To view the status of policy type in a root, use ListRoots.
        """
        if _request is None:
            _params = {}
            if root_id is not ShapeBase.NOT_SET:
                _params['root_id'] = root_id
            if policy_type is not ShapeBase.NOT_SET:
                _params['policy_type'] = policy_type
            _request = shapes.EnablePolicyTypeRequest(**_params)
        response = self._boto_client.enable_policy_type(**_request.to_boto())

        return shapes.EnablePolicyTypeResponse.from_boto(response)

    def invite_account_to_organization(
        self,
        _request: shapes.InviteAccountToOrganizationRequest = None,
        *,
        target: shapes.HandshakeParty,
        notes: str = ShapeBase.NOT_SET,
    ) -> shapes.InviteAccountToOrganizationResponse:
        """
        Sends an invitation to another account to join your organization as a member
        account. Organizations sends email on your behalf to the email address that is
        associated with the other account's owner. The invitation is implemented as a
        Handshake whose details are in the response.

          * You can invite AWS accounts only from the same seller as the master account. For example, if your organization's master account was created by Amazon Internet Services Pvt. Ltd (AISPL), an AWS seller in India, then you can only invite other AISPL accounts to your organization. You can't combine accounts from AISPL and AWS, or any other AWS seller. For more information, see [Consolidated Billing in India](http://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/useconsolidatedbilliing-India.html).

          * If you receive an exception that indicates that you exceeded your account limits for the organization or that the operation failed because your organization is still initializing, wait one hour and then try again. If the error persists after an hour, then contact [AWS Customer Support](https://console.aws.amazon.com/support/home#/).

        This operation can be called only from the organization's master account.
        """
        if _request is None:
            _params = {}
            if target is not ShapeBase.NOT_SET:
                _params['target'] = target
            if notes is not ShapeBase.NOT_SET:
                _params['notes'] = notes
            _request = shapes.InviteAccountToOrganizationRequest(**_params)
        response = self._boto_client.invite_account_to_organization(
            **_request.to_boto()
        )

        return shapes.InviteAccountToOrganizationResponse.from_boto(response)

    def leave_organization(self) -> None:
        """
        Removes a member account from its parent organization. This version of the
        operation is performed by the account that wants to leave. To remove a member
        account as a user in the master account, use RemoveAccountFromOrganization
        instead.

        This operation can be called only from a member account in the organization.

          * The master account in an organization with all features enabled can set service control policies (SCPs) that can restrict what administrators of member accounts can do, including preventing them from successfully calling `LeaveOrganization` and leaving the organization. 

          * You can leave an organization as a member account only if the account is configured with the information required to operate as a standalone account. When you create an account in an organization using the AWS Organizations console, API, or CLI commands, the information required of standalone accounts is _not_ automatically collected. For each account that you want to make standalone, you must accept the End User License Agreement (EULA), choose a support plan, provide and verify the required contact information, and provide a current payment method. AWS uses the payment method to charge for any billable (not free tier) AWS activity that occurs while the account is not attached to an organization. Follow the steps at [ To leave an organization when all required account information has not yet been provided](http://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_accounts_remove.html#leave-without-all-info) in the _AWS Organizations User Guide_.

          * You can leave an organization only after you enable IAM user access to billing in your account. For more information, see [Activating Access to the Billing and Cost Management Console](http://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/grantaccess.html#ControllingAccessWebsite-Activate) in the _AWS Billing and Cost Management User Guide_.
        """
        response = self._boto_client.leave_organization()

    def list_aws_service_access_for_organization(
        self,
        _request: shapes.ListAWSServiceAccessForOrganizationRequest = None,
        *,
        next_token: str = ShapeBase.NOT_SET,
        max_results: int = ShapeBase.NOT_SET,
    ) -> shapes.ListAWSServiceAccessForOrganizationResponse:
        """
        Returns a list of the AWS services that you enabled to integrate with your
        organization. After a service on this list creates the resources that it
        requires for the integration, it can perform operations on your organization and
        its accounts.

        For more information about integrating other services with AWS Organizations,
        including the list of services that currently work with Organizations, see
        [Integrating AWS Organizations with Other AWS
        Services](http://docs.aws.amazon.com/organizations/latest/userguide/orgs_integrate_services.html)
        in the _AWS Organizations User Guide_.

        This operation can be called only from the organization's master account.
        """
        if _request is None:
            _params = {}
            if next_token is not ShapeBase.NOT_SET:
                _params['next_token'] = next_token
            if max_results is not ShapeBase.NOT_SET:
                _params['max_results'] = max_results
            _request = shapes.ListAWSServiceAccessForOrganizationRequest(
                **_params
            )
        paginator = self.get_paginator(
            "list_aws_service_access_for_organization"
        ).paginate(**_request.to_boto())
        page_generator = (page for page in paginator)
        first_page = next(page_generator)
        result = shapes.ListAWSServiceAccessForOrganizationResponse.from_boto(
            first_page
        )
        result._page_iterator = page_generator
        return result

        return shapes.ListAWSServiceAccessForOrganizationResponse.from_boto(
            response
        )

    def list_accounts(
        self,
        _request: shapes.ListAccountsRequest = None,
        *,
        next_token: str = ShapeBase.NOT_SET,
        max_results: int = ShapeBase.NOT_SET,
    ) -> shapes.ListAccountsResponse:
        """
        Lists all the accounts in the organization. To request only the accounts in a
        specified root or organizational unit (OU), use the ListAccountsForParent
        operation instead.

        Always check the `NextToken` response parameter for a `null` value when calling
        a `List*` operation. These operations can occasionally return an empty set of
        results even when there are more results available. The `NextToken` response
        parameter value is `null` _only_ when there are no more results to display.

        This operation can be called only from the organization's master account.
        """
        if _request is None:
            _params = {}
            if next_token is not ShapeBase.NOT_SET:
                _params['next_token'] = next_token
            if max_results is not ShapeBase.NOT_SET:
                _params['max_results'] = max_results
            _request = shapes.ListAccountsRequest(**_params)
        paginator = self.get_paginator("list_accounts").paginate(
            **_request.to_boto()
        )
        page_generator = (page for page in paginator)
        first_page = next(page_generator)
        result = shapes.ListAccountsResponse.from_boto(first_page)
        result._page_iterator = page_generator
        return result

        return shapes.ListAccountsResponse.from_boto(response)

    def list_accounts_for_parent(
        self,
        _request: shapes.ListAccountsForParentRequest = None,
        *,
        parent_id: str,
        next_token: str = ShapeBase.NOT_SET,
        max_results: int = ShapeBase.NOT_SET,
    ) -> shapes.ListAccountsForParentResponse:
        """
        Lists the accounts in an organization that are contained by the specified target
        root or organizational unit (OU). If you specify the root, you get a list of all
        the accounts that are not in any OU. If you specify an OU, you get a list of all
        the accounts in only that OU, and not in any child OUs. To get a list of all
        accounts in the organization, use the ListAccounts operation.

        Always check the `NextToken` response parameter for a `null` value when calling
        a `List*` operation. These operations can occasionally return an empty set of
        results even when there are more results available. The `NextToken` response
        parameter value is `null` _only_ when there are no more results to display.

        This operation can be called only from the organization's master account.
        """
        if _request is None:
            _params = {}
            if parent_id is not ShapeBase.NOT_SET:
                _params['parent_id'] = parent_id
            if next_token is not ShapeBase.NOT_SET:
                _params['next_token'] = next_token
            if max_results is not ShapeBase.NOT_SET:
                _params['max_results'] = max_results
            _request = shapes.ListAccountsForParentRequest(**_params)
        paginator = self.get_paginator("list_accounts_for_parent").paginate(
            **_request.to_boto()
        )
        page_generator = (page for page in paginator)
        first_page = next(page_generator)
        result = shapes.ListAccountsForParentResponse.from_boto(first_page)
        result._page_iterator = page_generator
        return result

        return shapes.ListAccountsForParentResponse.from_boto(response)

    def list_children(
        self,
        _request: shapes.ListChildrenRequest = None,
        *,
        parent_id: str,
        child_type: typing.Union[str, shapes.ChildType],
        next_token: str = ShapeBase.NOT_SET,
        max_results: int = ShapeBase.NOT_SET,
    ) -> shapes.ListChildrenResponse:
        """
        Lists all of the organizational units (OUs) or accounts that are contained in
        the specified parent OU or root. This operation, along with ListParents enables
        you to traverse the tree structure that makes up this root.

        Always check the `NextToken` response parameter for a `null` value when calling
        a `List*` operation. These operations can occasionally return an empty set of
        results even when there are more results available. The `NextToken` response
        parameter value is `null` _only_ when there are no more results to display.

        This operation can be called only from the organization's master account.
        """
        if _request is None:
            _params = {}
            if parent_id is not ShapeBase.NOT_SET:
                _params['parent_id'] = parent_id
            if child_type is not ShapeBase.NOT_SET:
                _params['child_type'] = child_type
            if next_token is not ShapeBase.NOT_SET:
                _params['next_token'] = next_token
            if max_results is not ShapeBase.NOT_SET:
                _params['max_results'] = max_results
            _request = shapes.ListChildrenRequest(**_params)
        paginator = self.get_paginator("list_children").paginate(
            **_request.to_boto()
        )
        page_generator = (page for page in paginator)
        first_page = next(page_generator)
        result = shapes.ListChildrenResponse.from_boto(first_page)
        result._page_iterator = page_generator
        return result

        return shapes.ListChildrenResponse.from_boto(response)

    def list_create_account_status(
        self,
        _request: shapes.ListCreateAccountStatusRequest = None,
        *,
        states: typing.List[typing.Union[str, shapes.CreateAccountState]
                           ] = ShapeBase.NOT_SET,
        next_token: str = ShapeBase.NOT_SET,
        max_results: int = ShapeBase.NOT_SET,
    ) -> shapes.ListCreateAccountStatusResponse:
        """
        Lists the account creation requests that match the specified status that is
        currently being tracked for the organization.

        Always check the `NextToken` response parameter for a `null` value when calling
        a `List*` operation. These operations can occasionally return an empty set of
        results even when there are more results available. The `NextToken` response
        parameter value is `null` _only_ when there are no more results to display.

        This operation can be called only from the organization's master account.
        """
        if _request is None:
            _params = {}
            if states is not ShapeBase.NOT_SET:
                _params['states'] = states
            if next_token is not ShapeBase.NOT_SET:
                _params['next_token'] = next_token
            if max_results is not ShapeBase.NOT_SET:
                _params['max_results'] = max_results
            _request = shapes.ListCreateAccountStatusRequest(**_params)
        paginator = self.get_paginator("list_create_account_status").paginate(
            **_request.to_boto()
        )
        page_generator = (page for page in paginator)
        first_page = next(page_generator)
        result = shapes.ListCreateAccountStatusResponse.from_boto(first_page)
        result._page_iterator = page_generator
        return result

        return shapes.ListCreateAccountStatusResponse.from_boto(response)

    def list_handshakes_for_account(
        self,
        _request: shapes.ListHandshakesForAccountRequest = None,
        *,
        filter: shapes.HandshakeFilter = ShapeBase.NOT_SET,
        next_token: str = ShapeBase.NOT_SET,
        max_results: int = ShapeBase.NOT_SET,
    ) -> shapes.ListHandshakesForAccountResponse:
        """
        Lists the current handshakes that are associated with the account of the
        requesting user.

        Handshakes that are ACCEPTED, DECLINED, or CANCELED appear in the results of
        this API for only 30 days after changing to that state. After that they are
        deleted and no longer accessible.

        Always check the `NextToken` response parameter for a `null` value when calling
        a `List*` operation. These operations can occasionally return an empty set of
        results even when there are more results available. The `NextToken` response
        parameter value is `null` _only_ when there are no more results to display.

        This operation can be called from any account in the organization.
        """
        if _request is None:
            _params = {}
            if filter is not ShapeBase.NOT_SET:
                _params['filter'] = filter
            if next_token is not ShapeBase.NOT_SET:
                _params['next_token'] = next_token
            if max_results is not ShapeBase.NOT_SET:
                _params['max_results'] = max_results
            _request = shapes.ListHandshakesForAccountRequest(**_params)
        paginator = self.get_paginator("list_handshakes_for_account").paginate(
            **_request.to_boto()
        )
        page_generator = (page for page in paginator)
        first_page = next(page_generator)
        result = shapes.ListHandshakesForAccountResponse.from_boto(first_page)
        result._page_iterator = page_generator
        return result

        return shapes.ListHandshakesForAccountResponse.from_boto(response)

    def list_handshakes_for_organization(
        self,
        _request: shapes.ListHandshakesForOrganizationRequest = None,
        *,
        filter: shapes.HandshakeFilter = ShapeBase.NOT_SET,
        next_token: str = ShapeBase.NOT_SET,
        max_results: int = ShapeBase.NOT_SET,
    ) -> shapes.ListHandshakesForOrganizationResponse:
        """
        Lists the handshakes that are associated with the organization that the
        requesting user is part of. The `ListHandshakesForOrganization` operation
        returns a list of handshake structures. Each structure contains details and
        status about a handshake.

        Handshakes that are ACCEPTED, DECLINED, or CANCELED appear in the results of
        this API for only 30 days after changing to that state. After that they are
        deleted and no longer accessible.

        Always check the `NextToken` response parameter for a `null` value when calling
        a `List*` operation. These operations can occasionally return an empty set of
        results even when there are more results available. The `NextToken` response
        parameter value is `null` _only_ when there are no more results to display.

        This operation can be called only from the organization's master account.
        """
        if _request is None:
            _params = {}
            if filter is not ShapeBase.NOT_SET:
                _params['filter'] = filter
            if next_token is not ShapeBase.NOT_SET:
                _params['next_token'] = next_token
            if max_results is not ShapeBase.NOT_SET:
                _params['max_results'] = max_results
            _request = shapes.ListHandshakesForOrganizationRequest(**_params)
        paginator = self.get_paginator("list_handshakes_for_organization"
                                      ).paginate(**_request.to_boto())
        page_generator = (page for page in paginator)
        first_page = next(page_generator)
        result = shapes.ListHandshakesForOrganizationResponse.from_boto(
            first_page
        )
        result._page_iterator = page_generator
        return result

        return shapes.ListHandshakesForOrganizationResponse.from_boto(response)

    def list_organizational_units_for_parent(
        self,
        _request: shapes.ListOrganizationalUnitsForParentRequest = None,
        *,
        parent_id: str,
        next_token: str = ShapeBase.NOT_SET,
        max_results: int = ShapeBase.NOT_SET,
    ) -> shapes.ListOrganizationalUnitsForParentResponse:
        """
        Lists the organizational units (OUs) in a parent organizational unit or root.

        Always check the `NextToken` response parameter for a `null` value when calling
        a `List*` operation. These operations can occasionally return an empty set of
        results even when there are more results available. The `NextToken` response
        parameter value is `null` _only_ when there are no more results to display.

        This operation can be called only from the organization's master account.
        """
        if _request is None:
            _params = {}
            if parent_id is not ShapeBase.NOT_SET:
                _params['parent_id'] = parent_id
            if next_token is not ShapeBase.NOT_SET:
                _params['next_token'] = next_token
            if max_results is not ShapeBase.NOT_SET:
                _params['max_results'] = max_results
            _request = shapes.ListOrganizationalUnitsForParentRequest(**_params)
        paginator = self.get_paginator("list_organizational_units_for_parent"
                                      ).paginate(**_request.to_boto())
        page_generator = (page for page in paginator)
        first_page = next(page_generator)
        result = shapes.ListOrganizationalUnitsForParentResponse.from_boto(
            first_page
        )
        result._page_iterator = page_generator
        return result

        return shapes.ListOrganizationalUnitsForParentResponse.from_boto(
            response
        )

    def list_parents(
        self,
        _request: shapes.ListParentsRequest = None,
        *,
        child_id: str,
        next_token: str = ShapeBase.NOT_SET,
        max_results: int = ShapeBase.NOT_SET,
    ) -> shapes.ListParentsResponse:
        """
        Lists the root or organizational units (OUs) that serve as the immediate parent
        of the specified child OU or account. This operation, along with ListChildren
        enables you to traverse the tree structure that makes up this root.

        Always check the `NextToken` response parameter for a `null` value when calling
        a `List*` operation. These operations can occasionally return an empty set of
        results even when there are more results available. The `NextToken` response
        parameter value is `null` _only_ when there are no more results to display.

        This operation can be called only from the organization's master account.

        In the current release, a child can have only a single parent.
        """
        if _request is None:
            _params = {}
            if child_id is not ShapeBase.NOT_SET:
                _params['child_id'] = child_id
            if next_token is not ShapeBase.NOT_SET:
                _params['next_token'] = next_token
            if max_results is not ShapeBase.NOT_SET:
                _params['max_results'] = max_results
            _request = shapes.ListParentsRequest(**_params)
        paginator = self.get_paginator("list_parents").paginate(
            **_request.to_boto()
        )
        page_generator = (page for page in paginator)
        first_page = next(page_generator)
        result = shapes.ListParentsResponse.from_boto(first_page)
        result._page_iterator = page_generator
        return result

        return shapes.ListParentsResponse.from_boto(response)

    def list_policies(
        self,
        _request: shapes.ListPoliciesRequest = None,
        *,
        filter: typing.Union[str, shapes.PolicyType],
        next_token: str = ShapeBase.NOT_SET,
        max_results: int = ShapeBase.NOT_SET,
    ) -> shapes.ListPoliciesResponse:
        """
        Retrieves the list of all policies in an organization of a specified type.

        Always check the `NextToken` response parameter for a `null` value when calling
        a `List*` operation. These operations can occasionally return an empty set of
        results even when there are more results available. The `NextToken` response
        parameter value is `null` _only_ when there are no more results to display.

        This operation can be called only from the organization's master account.
        """
        if _request is None:
            _params = {}
            if filter is not ShapeBase.NOT_SET:
                _params['filter'] = filter
            if next_token is not ShapeBase.NOT_SET:
                _params['next_token'] = next_token
            if max_results is not ShapeBase.NOT_SET:
                _params['max_results'] = max_results
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

    def list_policies_for_target(
        self,
        _request: shapes.ListPoliciesForTargetRequest = None,
        *,
        target_id: str,
        filter: typing.Union[str, shapes.PolicyType],
        next_token: str = ShapeBase.NOT_SET,
        max_results: int = ShapeBase.NOT_SET,
    ) -> shapes.ListPoliciesForTargetResponse:
        """
        Lists the policies that are directly attached to the specified target root,
        organizational unit (OU), or account. You must specify the policy type that you
        want included in the returned list.

        Always check the `NextToken` response parameter for a `null` value when calling
        a `List*` operation. These operations can occasionally return an empty set of
        results even when there are more results available. The `NextToken` response
        parameter value is `null` _only_ when there are no more results to display.

        This operation can be called only from the organization's master account.
        """
        if _request is None:
            _params = {}
            if target_id is not ShapeBase.NOT_SET:
                _params['target_id'] = target_id
            if filter is not ShapeBase.NOT_SET:
                _params['filter'] = filter
            if next_token is not ShapeBase.NOT_SET:
                _params['next_token'] = next_token
            if max_results is not ShapeBase.NOT_SET:
                _params['max_results'] = max_results
            _request = shapes.ListPoliciesForTargetRequest(**_params)
        paginator = self.get_paginator("list_policies_for_target").paginate(
            **_request.to_boto()
        )
        page_generator = (page for page in paginator)
        first_page = next(page_generator)
        result = shapes.ListPoliciesForTargetResponse.from_boto(first_page)
        result._page_iterator = page_generator
        return result

        return shapes.ListPoliciesForTargetResponse.from_boto(response)

    def list_roots(
        self,
        _request: shapes.ListRootsRequest = None,
        *,
        next_token: str = ShapeBase.NOT_SET,
        max_results: int = ShapeBase.NOT_SET,
    ) -> shapes.ListRootsResponse:
        """
        Lists the roots that are defined in the current organization.

        Always check the `NextToken` response parameter for a `null` value when calling
        a `List*` operation. These operations can occasionally return an empty set of
        results even when there are more results available. The `NextToken` response
        parameter value is `null` _only_ when there are no more results to display.

        This operation can be called only from the organization's master account.

        Policy types can be enabled and disabled in roots. This is distinct from whether
        they are available in the organization. When you enable all features, you make
        policy types available for use in that organization. Individual policy types can
        then be enabled and disabled in a root. To see the availability of a policy type
        in an organization, use DescribeOrganization.
        """
        if _request is None:
            _params = {}
            if next_token is not ShapeBase.NOT_SET:
                _params['next_token'] = next_token
            if max_results is not ShapeBase.NOT_SET:
                _params['max_results'] = max_results
            _request = shapes.ListRootsRequest(**_params)
        paginator = self.get_paginator("list_roots").paginate(
            **_request.to_boto()
        )
        page_generator = (page for page in paginator)
        first_page = next(page_generator)
        result = shapes.ListRootsResponse.from_boto(first_page)
        result._page_iterator = page_generator
        return result

        return shapes.ListRootsResponse.from_boto(response)

    def list_targets_for_policy(
        self,
        _request: shapes.ListTargetsForPolicyRequest = None,
        *,
        policy_id: str,
        next_token: str = ShapeBase.NOT_SET,
        max_results: int = ShapeBase.NOT_SET,
    ) -> shapes.ListTargetsForPolicyResponse:
        """
        Lists all the roots, organizaitonal units (OUs), and accounts to which the
        specified policy is attached.

        Always check the `NextToken` response parameter for a `null` value when calling
        a `List*` operation. These operations can occasionally return an empty set of
        results even when there are more results available. The `NextToken` response
        parameter value is `null` _only_ when there are no more results to display.

        This operation can be called only from the organization's master account.
        """
        if _request is None:
            _params = {}
            if policy_id is not ShapeBase.NOT_SET:
                _params['policy_id'] = policy_id
            if next_token is not ShapeBase.NOT_SET:
                _params['next_token'] = next_token
            if max_results is not ShapeBase.NOT_SET:
                _params['max_results'] = max_results
            _request = shapes.ListTargetsForPolicyRequest(**_params)
        paginator = self.get_paginator("list_targets_for_policy").paginate(
            **_request.to_boto()
        )
        page_generator = (page for page in paginator)
        first_page = next(page_generator)
        result = shapes.ListTargetsForPolicyResponse.from_boto(first_page)
        result._page_iterator = page_generator
        return result

        return shapes.ListTargetsForPolicyResponse.from_boto(response)

    def move_account(
        self,
        _request: shapes.MoveAccountRequest = None,
        *,
        account_id: str,
        source_parent_id: str,
        destination_parent_id: str,
    ) -> None:
        """
        Moves an account from its current source parent root or organizational unit (OU)
        to the specified destination parent root or OU.

        This operation can be called only from the organization's master account.
        """
        if _request is None:
            _params = {}
            if account_id is not ShapeBase.NOT_SET:
                _params['account_id'] = account_id
            if source_parent_id is not ShapeBase.NOT_SET:
                _params['source_parent_id'] = source_parent_id
            if destination_parent_id is not ShapeBase.NOT_SET:
                _params['destination_parent_id'] = destination_parent_id
            _request = shapes.MoveAccountRequest(**_params)
        response = self._boto_client.move_account(**_request.to_boto())

    def remove_account_from_organization(
        self,
        _request: shapes.RemoveAccountFromOrganizationRequest = None,
        *,
        account_id: str,
    ) -> None:
        """
        Removes the specified account from the organization.

        The removed account becomes a stand-alone account that is not a member of any
        organization. It is no longer subject to any policies and is responsible for its
        own bill payments. The organization's master account is no longer charged for
        any expenses accrued by the member account after it is removed from the
        organization.

        This operation can be called only from the organization's master account. Member
        accounts can remove themselves with LeaveOrganization instead.

        You can remove an account from your organization only if the account is
        configured with the information required to operate as a standalone account.
        When you create an account in an organization using the AWS Organizations
        console, API, or CLI commands, the information required of standalone accounts
        is _not_ automatically collected. For an account that you want to make
        standalone, you must accept the End User License Agreement (EULA), choose a
        support plan, provide and verify the required contact information, and provide a
        current payment method. AWS uses the payment method to charge for any billable
        (not free tier) AWS activity that occurs while the account is not attached to an
        organization. To remove an account that does not yet have this information, you
        must sign in as the member account and follow the steps at [ To leave an
        organization when all required account information has not yet been
        provided](http://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_accounts_remove.html#leave-
        without-all-info) in the _AWS Organizations User Guide_.
        """
        if _request is None:
            _params = {}
            if account_id is not ShapeBase.NOT_SET:
                _params['account_id'] = account_id
            _request = shapes.RemoveAccountFromOrganizationRequest(**_params)
        response = self._boto_client.remove_account_from_organization(
            **_request.to_boto()
        )

    def update_organizational_unit(
        self,
        _request: shapes.UpdateOrganizationalUnitRequest = None,
        *,
        organizational_unit_id: str,
        name: str = ShapeBase.NOT_SET,
    ) -> shapes.UpdateOrganizationalUnitResponse:
        """
        Renames the specified organizational unit (OU). The ID and ARN do not change.
        The child OUs and accounts remain in place, and any attached policies of the OU
        remain attached.

        This operation can be called only from the organization's master account.
        """
        if _request is None:
            _params = {}
            if organizational_unit_id is not ShapeBase.NOT_SET:
                _params['organizational_unit_id'] = organizational_unit_id
            if name is not ShapeBase.NOT_SET:
                _params['name'] = name
            _request = shapes.UpdateOrganizationalUnitRequest(**_params)
        response = self._boto_client.update_organizational_unit(
            **_request.to_boto()
        )

        return shapes.UpdateOrganizationalUnitResponse.from_boto(response)

    def update_policy(
        self,
        _request: shapes.UpdatePolicyRequest = None,
        *,
        policy_id: str,
        name: str = ShapeBase.NOT_SET,
        description: str = ShapeBase.NOT_SET,
        content: str = ShapeBase.NOT_SET,
    ) -> shapes.UpdatePolicyResponse:
        """
        Updates an existing policy with a new name, description, or content. If any
        parameter is not supplied, that value remains unchanged. Note that you cannot
        change a policy's type.

        This operation can be called only from the organization's master account.
        """
        if _request is None:
            _params = {}
            if policy_id is not ShapeBase.NOT_SET:
                _params['policy_id'] = policy_id
            if name is not ShapeBase.NOT_SET:
                _params['name'] = name
            if description is not ShapeBase.NOT_SET:
                _params['description'] = description
            if content is not ShapeBase.NOT_SET:
                _params['content'] = content
            _request = shapes.UpdatePolicyRequest(**_params)
        response = self._boto_client.update_policy(**_request.to_boto())

        return shapes.UpdatePolicyResponse.from_boto(response)
