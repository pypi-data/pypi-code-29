import datetime
import typing
from autoboto import ShapeBase, OutputShapeBase, TypeInfo
import dataclasses


@dataclasses.dataclass
class AWSOrganizationsNotInUseException(ShapeBase):
    """
    Your account is not a member of an organization. To make this request, you must
    use the credentials of an account that belongs to an organization.
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
class AcceptHandshakeRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "handshake_id",
                "HandshakeId",
                TypeInfo(str),
            ),
        ]

    # The unique identifier (ID) of the handshake that you want to accept.

    # The [regex pattern](http://wikipedia.org/wiki/regex) for handshake ID
    # string requires "h-" followed by from 8 to 32 lower-case letters or digits.
    handshake_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class AcceptHandshakeResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "handshake",
                "Handshake",
                TypeInfo(Handshake),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A structure that contains details about the accepted handshake.
    handshake: "Handshake" = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class AccessDeniedException(ShapeBase):
    """
    You don't have permissions to perform the requested operation. The user or role
    that is making the request must have at least one IAM permissions policy
    attached that grants the required permissions. For more information, see [Access
    Management](http://docs.aws.amazon.com/IAM/latest/UserGuide/access.html) in the
    _IAM User Guide_.
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
class AccessDeniedForDependencyException(ShapeBase):
    """
    The operation you attempted requires you to have the
    `iam:CreateServiceLinkedRole` so that Organizations can create the required
    service-linked role. You do not have that permission.
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
                "reason",
                "Reason",
                TypeInfo(
                    typing.Union[str, AccessDeniedForDependencyExceptionReason]
                ),
            ),
        ]

    message: str = dataclasses.field(default=ShapeBase.NOT_SET, )
    reason: typing.Union[str, "AccessDeniedForDependencyExceptionReason"
                        ] = dataclasses.field(
                            default=ShapeBase.NOT_SET,
                        )


class AccessDeniedForDependencyExceptionReason(str):
    ACCESS_DENIED_DURING_CREATE_SERVICE_LINKED_ROLE = "ACCESS_DENIED_DURING_CREATE_SERVICE_LINKED_ROLE"


@dataclasses.dataclass
class Account(ShapeBase):
    """
    Contains information about an AWS account that is a member of an organization.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "id",
                "Id",
                TypeInfo(str),
            ),
            (
                "arn",
                "Arn",
                TypeInfo(str),
            ),
            (
                "email",
                "Email",
                TypeInfo(str),
            ),
            (
                "name",
                "Name",
                TypeInfo(str),
            ),
            (
                "status",
                "Status",
                TypeInfo(typing.Union[str, AccountStatus]),
            ),
            (
                "joined_method",
                "JoinedMethod",
                TypeInfo(typing.Union[str, AccountJoinedMethod]),
            ),
            (
                "joined_timestamp",
                "JoinedTimestamp",
                TypeInfo(datetime.datetime),
            ),
        ]

    # The unique identifier (ID) of the account.

    # The [regex pattern](http://wikipedia.org/wiki/regex) for an account ID
    # string requires exactly 12 digits.
    id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The Amazon Resource Name (ARN) of the account.

    # For more information about ARNs in Organizations, see [ARN Formats
    # Supported by
    # Organizations](http://docs.aws.amazon.com/organizations/latest/userguide/orgs_permissions.html#orgs-
    # permissions-arns) in the _AWS Organizations User Guide_.
    arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The email address associated with the AWS account.

    # The [regex pattern](http://wikipedia.org/wiki/regex) for this parameter is
    # a string of characters that represents a standard Internet email address.
    email: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The friendly name of the account.

    # The [regex pattern](http://wikipedia.org/wiki/regex) that is used to
    # validate this parameter is a string of any of the characters in the ASCII
    # character range.
    name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The status of the account in the organization.
    status: typing.Union[str, "AccountStatus"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The method by which the account joined the organization.
    joined_method: typing.Union[str, "AccountJoinedMethod"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The date the account became a part of the organization.
    joined_timestamp: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


class AccountJoinedMethod(str):
    INVITED = "INVITED"
    CREATED = "CREATED"


@dataclasses.dataclass
class AccountNotFoundException(ShapeBase):
    """
    We can't find an AWS account with the AccountId that you specified, or the
    account whose credentials you used to make this request is not a member of an
    organization.
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


class AccountStatus(str):
    ACTIVE = "ACTIVE"
    SUSPENDED = "SUSPENDED"


class ActionType(str):
    INVITE = "INVITE"
    ENABLE_ALL_FEATURES = "ENABLE_ALL_FEATURES"
    APPROVE_ALL_FEATURES = "APPROVE_ALL_FEATURES"
    ADD_ORGANIZATIONS_SERVICE_LINKED_ROLE = "ADD_ORGANIZATIONS_SERVICE_LINKED_ROLE"


@dataclasses.dataclass
class AlreadyInOrganizationException(ShapeBase):
    """
    This account is already a member of an organization. An account can belong to
    only one organization at a time.
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
class AttachPolicyRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "policy_id",
                "PolicyId",
                TypeInfo(str),
            ),
            (
                "target_id",
                "TargetId",
                TypeInfo(str),
            ),
        ]

    # The unique identifier (ID) of the policy that you want to attach to the
    # target. You can get the ID for the policy by calling the ListPolicies
    # operation.

    # The [regex pattern](http://wikipedia.org/wiki/regex) for a policy ID string
    # requires "p-" followed by from 8 to 128 lower-case letters or digits.
    policy_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The unique identifier (ID) of the root, OU, or account that you want to
    # attach the policy to. You can get the ID by calling the ListRoots,
    # ListOrganizationalUnitsForParent, or ListAccounts operations.

    # The [regex pattern](http://wikipedia.org/wiki/regex) for a target ID string
    # requires one of the following:

    #   * Root: a string that begins with "r-" followed by from 4 to 32 lower-case letters or digits.

    #   * Account: a string that consists of exactly 12 digits.

    #   * Organizational unit (OU): a string that begins with "ou-" followed by from 4 to 32 lower-case letters or digits (the ID of the root that the OU is in) followed by a second "-" dash and from 8 to 32 additional lower-case letters or digits.
    target_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class CancelHandshakeRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "handshake_id",
                "HandshakeId",
                TypeInfo(str),
            ),
        ]

    # The unique identifier (ID) of the handshake that you want to cancel. You
    # can get the ID from the ListHandshakesForOrganization operation.

    # The [regex pattern](http://wikipedia.org/wiki/regex) for handshake ID
    # string requires "h-" followed by from 8 to 32 lower-case letters or digits.
    handshake_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class CancelHandshakeResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "handshake",
                "Handshake",
                TypeInfo(Handshake),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A structure that contains details about the handshake that you canceled.
    handshake: "Handshake" = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class Child(ShapeBase):
    """
    Contains a list of child entities, either OUs or accounts.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "id",
                "Id",
                TypeInfo(str),
            ),
            (
                "type",
                "Type",
                TypeInfo(typing.Union[str, ChildType]),
            ),
        ]

    # The unique identifier (ID) of this child entity.

    # The [regex pattern](http://wikipedia.org/wiki/regex) for a child ID string
    # requires one of the following:

    #   * Account: a string that consists of exactly 12 digits.

    #   * Organizational unit (OU): a string that begins with "ou-" followed by from 4 to 32 lower-case letters or digits (the ID of the root that contains the OU) followed by a second "-" dash and from 8 to 32 additional lower-case letters or digits.
    id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The type of this child entity.
    type: typing.Union[str, "ChildType"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class ChildNotFoundException(ShapeBase):
    """
    We can't find an organizational unit (OU) or AWS account with the ChildId that
    you specified.
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


class ChildType(str):
    ACCOUNT = "ACCOUNT"
    ORGANIZATIONAL_UNIT = "ORGANIZATIONAL_UNIT"


@dataclasses.dataclass
class ConcurrentModificationException(ShapeBase):
    """
    The target of the operation is currently being modified by a different request.
    Try again later.
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
class ConstraintViolationException(ShapeBase):
    """
    Performing this operation violates a minimum or maximum value limit. For
    example, attempting to removing the last SCP from an OU or root, inviting or
    creating too many accounts to the organization, or attaching too many policies
    to an account, OU, or root. This exception includes a reason that contains
    additional information about the violated limit:

    Some of the reasons in the following list might not be applicable to this
    specific API or operation:

      * ACCOUNT_NUMBER_LIMIT_EXCEEDED: You attempted to exceed the limit on the number of accounts in an organization. If you need more accounts, contact AWS Support to request an increase in your limit. 

    Or, The number of invitations that you tried to send would cause you to exceed
    the limit of accounts in your organization. Send fewer invitations, or contact
    AWS Support to request an increase in the number of accounts.

    **Note** : deleted and closed accounts still count toward your limit.

    If you get receive this exception when running a command immediately after
    creating the organization, wait one hour and try again. If after an hour it
    continues to fail with this error, contact [AWS Customer
    Support](https://console.aws.amazon.com/support/home#/).

      * HANDSHAKE_RATE_LIMIT_EXCEEDED: You attempted to exceed the number of handshakes you can send in one day.

      * OU_NUMBER_LIMIT_EXCEEDED: You attempted to exceed the number of organizational units you can have in an organization.

      * OU_DEPTH_LIMIT_EXCEEDED: You attempted to create an organizational unit tree that is too many levels deep.

      * ORGANIZATION_NOT_IN_ALL_FEATURES_MODE: You attempted to perform an operation that requires the organization to be configured to support all features. An organization that supports consolidated billing features only cannot perform this operation.

      * POLICY_NUMBER_LIMIT_EXCEEDED. You attempted to exceed the number of policies that you can have in an organization.

      * MAX_POLICY_TYPE_ATTACHMENT_LIMIT_EXCEEDED: You attempted to exceed the number of policies of a certain type that can be attached to an entity at one time.

      * MIN_POLICY_TYPE_ATTACHMENT_LIMIT_EXCEEDED: You attempted to detach a policy from an entity that would cause the entity to have fewer than the minimum number of policies of a certain type required.

      * ACCOUNT_CANNOT_LEAVE_WITHOUT_EULA: You attempted to remove an account from the organization that does not yet have enough information to exist as a stand-alone account. This account requires you to first agree to the AWS Customer Agreement. Follow the steps at [To leave an organization when all required account information has not yet been provided](http://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_accounts_remove.html#leave-without-all-info) in the _AWS Organizations User Guide_.

      * ACCOUNT_CANNOT_LEAVE_WITHOUT_PHONE_VERIFICATION: You attempted to remove an account from the organization that does not yet have enough information to exist as a stand-alone account. This account requires you to first complete phone verification. Follow the steps at [To leave an organization when all required account information has not yet been provided](http://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_accounts_remove.html#leave-without-all-info) in the _AWS Organizations User Guide_.

      * MASTER_ACCOUNT_PAYMENT_INSTRUMENT_REQUIRED: To create an organization with this account, you first must associate a payment instrument, such as a credit card, with the account. Follow the steps at [To leave an organization when all required account information has not yet been provided](http://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_accounts_remove.html#leave-without-all-info) in the _AWS Organizations User Guide_.

      * MEMBER_ACCOUNT_PAYMENT_INSTRUMENT_REQUIRED: To complete this operation with this member account, you first must associate a payment instrument, such as a credit card, with the account. Follow the steps at [To leave an organization when all required account information has not yet been provided](http://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_accounts_remove.html#leave-without-all-info) in the _AWS Organizations User Guide_.

      * ACCOUNT_CREATION_RATE_LIMIT_EXCEEDED: You attempted to exceed the number of accounts that you can create in one day.

      * MASTER_ACCOUNT_ADDRESS_DOES_NOT_MATCH_MARKETPLACE: To create an account in this organization, you first must migrate the organization's master account to the marketplace that corresponds to the master account's address. For example, accounts with India addresses must be associated with the AISPL marketplace. All accounts in an organization must be associated with the same marketplace.

      * MASTER_ACCOUNT_MISSING_CONTACT_INFO: To complete this operation, you must first provide contact a valid address and phone number for the master account. Then try the operation again.
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
                "reason",
                "Reason",
                TypeInfo(typing.Union[str, ConstraintViolationExceptionReason]),
            ),
        ]

    message: str = dataclasses.field(default=ShapeBase.NOT_SET, )
    reason: typing.Union[str, "ConstraintViolationExceptionReason"
                        ] = dataclasses.field(
                            default=ShapeBase.NOT_SET,
                        )


class ConstraintViolationExceptionReason(str):
    ACCOUNT_NUMBER_LIMIT_EXCEEDED = "ACCOUNT_NUMBER_LIMIT_EXCEEDED"
    HANDSHAKE_RATE_LIMIT_EXCEEDED = "HANDSHAKE_RATE_LIMIT_EXCEEDED"
    OU_NUMBER_LIMIT_EXCEEDED = "OU_NUMBER_LIMIT_EXCEEDED"
    OU_DEPTH_LIMIT_EXCEEDED = "OU_DEPTH_LIMIT_EXCEEDED"
    POLICY_NUMBER_LIMIT_EXCEEDED = "POLICY_NUMBER_LIMIT_EXCEEDED"
    MAX_POLICY_TYPE_ATTACHMENT_LIMIT_EXCEEDED = "MAX_POLICY_TYPE_ATTACHMENT_LIMIT_EXCEEDED"
    MIN_POLICY_TYPE_ATTACHMENT_LIMIT_EXCEEDED = "MIN_POLICY_TYPE_ATTACHMENT_LIMIT_EXCEEDED"
    ACCOUNT_CANNOT_LEAVE_ORGANIZATION = "ACCOUNT_CANNOT_LEAVE_ORGANIZATION"
    ACCOUNT_CANNOT_LEAVE_WITHOUT_EULA = "ACCOUNT_CANNOT_LEAVE_WITHOUT_EULA"
    ACCOUNT_CANNOT_LEAVE_WITHOUT_PHONE_VERIFICATION = "ACCOUNT_CANNOT_LEAVE_WITHOUT_PHONE_VERIFICATION"
    MASTER_ACCOUNT_PAYMENT_INSTRUMENT_REQUIRED = "MASTER_ACCOUNT_PAYMENT_INSTRUMENT_REQUIRED"
    MEMBER_ACCOUNT_PAYMENT_INSTRUMENT_REQUIRED = "MEMBER_ACCOUNT_PAYMENT_INSTRUMENT_REQUIRED"
    ACCOUNT_CREATION_RATE_LIMIT_EXCEEDED = "ACCOUNT_CREATION_RATE_LIMIT_EXCEEDED"
    MASTER_ACCOUNT_ADDRESS_DOES_NOT_MATCH_MARKETPLACE = "MASTER_ACCOUNT_ADDRESS_DOES_NOT_MATCH_MARKETPLACE"
    MASTER_ACCOUNT_MISSING_CONTACT_INFO = "MASTER_ACCOUNT_MISSING_CONTACT_INFO"
    ORGANIZATION_NOT_IN_ALL_FEATURES_MODE = "ORGANIZATION_NOT_IN_ALL_FEATURES_MODE"


class CreateAccountFailureReason(str):
    ACCOUNT_LIMIT_EXCEEDED = "ACCOUNT_LIMIT_EXCEEDED"
    EMAIL_ALREADY_EXISTS = "EMAIL_ALREADY_EXISTS"
    INVALID_ADDRESS = "INVALID_ADDRESS"
    INVALID_EMAIL = "INVALID_EMAIL"
    CONCURRENT_ACCOUNT_MODIFICATION = "CONCURRENT_ACCOUNT_MODIFICATION"
    INTERNAL_FAILURE = "INTERNAL_FAILURE"


@dataclasses.dataclass
class CreateAccountRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "email",
                "Email",
                TypeInfo(str),
            ),
            (
                "account_name",
                "AccountName",
                TypeInfo(str),
            ),
            (
                "role_name",
                "RoleName",
                TypeInfo(str),
            ),
            (
                "iam_user_access_to_billing",
                "IamUserAccessToBilling",
                TypeInfo(typing.Union[str, IAMUserAccessToBilling]),
            ),
        ]

    # The email address of the owner to assign to the new member account. This
    # email address must not already be associated with another AWS account. You
    # must use a valid email address to complete account creation. You cannot
    # access the root user of the account or remove an account that was created
    # with an invalid email address.
    email: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The friendly name of the member account.
    account_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # (Optional)

    # The name of an IAM role that Organizations automatically preconfigures in
    # the new member account. This role trusts the master account, allowing users
    # in the master account to assume the role, as permitted by the master
    # account administrator. The role has administrator permissions in the new
    # member account.

    # If you do not specify this parameter, the role name defaults to
    # `OrganizationAccountAccessRole`.

    # For more information about how to use this role to access the member
    # account, see [Accessing and Administering the Member Accounts in Your
    # Organization](http://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_accounts_access.html#orgs_manage_accounts_create-
    # cross-account-role) in the _AWS Organizations User Guide_ , and steps 2 and
    # 3 in [Tutorial: Delegate Access Across AWS Accounts Using IAM
    # Roles](http://docs.aws.amazon.com/IAM/latest/UserGuide/tutorial_cross-
    # account-with-roles.html) in the _IAM User Guide_.

    # The [regex pattern](http://wikipedia.org/wiki/regex) that is used to
    # validate this parameter is a string of characters that can consist of
    # uppercase letters, lowercase letters, digits with no spaces, and any of the
    # following characters: =,.@-
    role_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # If set to `ALLOW`, the new account enables IAM users to access account
    # billing information _if_ they have the required permissions. If set to
    # `DENY`, then only the root user of the new account can access account
    # billing information. For more information, see [Activating Access to the
    # Billing and Cost Management
    # Console](http://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/grantaccess.html#ControllingAccessWebsite-
    # Activate) in the _AWS Billing and Cost Management User Guide_.

    # If you do not specify this parameter, the value defaults to ALLOW, and IAM
    # users and roles with the required permissions can access billing
    # information for the new account.
    iam_user_access_to_billing: typing.Union[str, "IAMUserAccessToBilling"
                                            ] = dataclasses.field(
                                                default=ShapeBase.NOT_SET,
                                            )


@dataclasses.dataclass
class CreateAccountResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "create_account_status",
                "CreateAccountStatus",
                TypeInfo(CreateAccountStatus),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A structure that contains details about the request to create an account.
    # This response structure might not be fully populated when you first receive
    # it because account creation is an asynchronous process. You can pass the
    # returned CreateAccountStatus ID as a parameter to `
    # DescribeCreateAccountStatus ` to get status about the progress of the
    # request at later times.
    create_account_status: "CreateAccountStatus" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


class CreateAccountState(str):
    IN_PROGRESS = "IN_PROGRESS"
    SUCCEEDED = "SUCCEEDED"
    FAILED = "FAILED"


@dataclasses.dataclass
class CreateAccountStatus(ShapeBase):
    """
    Contains the status about a CreateAccount request to create an AWS account in an
    organization.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "id",
                "Id",
                TypeInfo(str),
            ),
            (
                "account_name",
                "AccountName",
                TypeInfo(str),
            ),
            (
                "state",
                "State",
                TypeInfo(typing.Union[str, CreateAccountState]),
            ),
            (
                "requested_timestamp",
                "RequestedTimestamp",
                TypeInfo(datetime.datetime),
            ),
            (
                "completed_timestamp",
                "CompletedTimestamp",
                TypeInfo(datetime.datetime),
            ),
            (
                "account_id",
                "AccountId",
                TypeInfo(str),
            ),
            (
                "failure_reason",
                "FailureReason",
                TypeInfo(typing.Union[str, CreateAccountFailureReason]),
            ),
        ]

    # The unique identifier (ID) that references this request. You get this value
    # from the response of the initial CreateAccount request to create the
    # account.

    # The [regex pattern](http://wikipedia.org/wiki/regex) for an create account
    # request ID string requires "car-" followed by from 8 to 32 lower-case
    # letters or digits.
    id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The account name given to the account when it was created.
    account_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The status of the request.
    state: typing.Union[str, "CreateAccountState"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The date and time that the request was made for the account creation.
    requested_timestamp: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The date and time that the account was created and the request completed.
    completed_timestamp: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # If the account was created successfully, the unique identifier (ID) of the
    # new account.

    # The [regex pattern](http://wikipedia.org/wiki/regex) for an account ID
    # string requires exactly 12 digits.
    account_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # If the request failed, a description of the reason for the failure.

    #   * ACCOUNT_LIMIT_EXCEEDED: The account could not be created because you have reached the limit on the number of accounts in your organization.

    #   * EMAIL_ALREADY_EXISTS: The account could not be created because another AWS account with that email address already exists.

    #   * INVALID_ADDRESS: The account could not be created because the address you provided is not valid.

    #   * INVALID_EMAIL: The account could not be created because the email address you provided is not valid.

    #   * INTERNAL_FAILURE: The account could not be created because of an internal failure. Try again later. If the problem persists, contact Customer Support.
    failure_reason: typing.Union[str, "CreateAccountFailureReason"
                                ] = dataclasses.field(
                                    default=ShapeBase.NOT_SET,
                                )


@dataclasses.dataclass
class CreateAccountStatusNotFoundException(ShapeBase):
    """
    We can't find an create account request with the CreateAccountRequestId that you
    specified.
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
class CreateOrganizationRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "feature_set",
                "FeatureSet",
                TypeInfo(typing.Union[str, OrganizationFeatureSet]),
            ),
        ]

    # Specifies the feature set supported by the new organization. Each feature
    # set supports different levels of functionality.

    #   * _CONSOLIDATED_BILLING_ : All member accounts have their bills consolidated to and paid by the master account. For more information, see [Consolidated Billing](http://docs.aws.amazon.com/organizations/latest/userguide/orgs_getting-started_concepts.html#feature-set-cb-only) in the _AWS Organizations User Guide_.

    #   * _ALL_ : In addition to all the features supported by the consolidated billing feature set, the master account can also apply any type of policy to any member account in the organization. For more information, see [All features](http://docs.aws.amazon.com/organizations/latest/userguide/orgs_getting-started_concepts.html#feature-set-all) in the _AWS Organizations User Guide_.
    feature_set: typing.Union[str, "OrganizationFeatureSet"
                             ] = dataclasses.field(
                                 default=ShapeBase.NOT_SET,
                             )


@dataclasses.dataclass
class CreateOrganizationResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "organization",
                "Organization",
                TypeInfo(Organization),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A structure that contains details about the newly created organization.
    organization: "Organization" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class CreateOrganizationalUnitRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "parent_id",
                "ParentId",
                TypeInfo(str),
            ),
            (
                "name",
                "Name",
                TypeInfo(str),
            ),
        ]

    # The unique identifier (ID) of the parent root or OU in which you want to
    # create the new OU.

    # The [regex pattern](http://wikipedia.org/wiki/regex) for a parent ID string
    # requires one of the following:

    #   * Root: a string that begins with "r-" followed by from 4 to 32 lower-case letters or digits.

    #   * Organizational unit (OU): a string that begins with "ou-" followed by from 4 to 32 lower-case letters or digits (the ID of the root that the OU is in) followed by a second "-" dash and from 8 to 32 additional lower-case letters or digits.
    parent_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The friendly name to assign to the new OU.
    name: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class CreateOrganizationalUnitResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "organizational_unit",
                "OrganizationalUnit",
                TypeInfo(OrganizationalUnit),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A structure that contains details about the newly created OU.
    organizational_unit: "OrganizationalUnit" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class CreatePolicyRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "content",
                "Content",
                TypeInfo(str),
            ),
            (
                "description",
                "Description",
                TypeInfo(str),
            ),
            (
                "name",
                "Name",
                TypeInfo(str),
            ),
            (
                "type",
                "Type",
                TypeInfo(typing.Union[str, PolicyType]),
            ),
        ]

    # The policy content to add to the new policy. For example, if you create a
    # [service control
    # policy](http://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_scp.html)
    # (SCP), this string must be JSON text that specifies the permissions that
    # admins in attached accounts can delegate to their users, groups, and roles.
    # For more information about the SCP syntax, see [Service Control Policy
    # Syntax](http://docs.aws.amazon.com/organizations/latest/userguide/orgs_reference_scp-
    # syntax.html) in the _AWS Organizations User Guide_.
    content: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # An optional description to assign to the policy.
    description: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The friendly name to assign to the policy.

    # The [regex pattern](http://wikipedia.org/wiki/regex) that is used to
    # validate this parameter is a string of any of the characters in the ASCII
    # character range.
    name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The type of policy to create.

    # In the current release, the only type of policy that you can create is a
    # service control policy (SCP).
    type: typing.Union[str, "PolicyType"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class CreatePolicyResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "policy",
                "Policy",
                TypeInfo(Policy),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A structure that contains details about the newly created policy.
    policy: "Policy" = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DeclineHandshakeRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "handshake_id",
                "HandshakeId",
                TypeInfo(str),
            ),
        ]

    # The unique identifier (ID) of the handshake that you want to decline. You
    # can get the ID from the ListHandshakesForAccount operation.

    # The [regex pattern](http://wikipedia.org/wiki/regex) for handshake ID
    # string requires "h-" followed by from 8 to 32 lower-case letters or digits.
    handshake_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DeclineHandshakeResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "handshake",
                "Handshake",
                TypeInfo(Handshake),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A structure that contains details about the declined handshake. The state
    # is updated to show the value `DECLINED`.
    handshake: "Handshake" = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DeleteOrganizationalUnitRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "organizational_unit_id",
                "OrganizationalUnitId",
                TypeInfo(str),
            ),
        ]

    # The unique identifier (ID) of the organizational unit that you want to
    # delete. You can get the ID from the ListOrganizationalUnitsForParent
    # operation.

    # The [regex pattern](http://wikipedia.org/wiki/regex) for an organizational
    # unit ID string requires "ou-" followed by from 4 to 32 lower-case letters
    # or digits (the ID of the root that contains the OU) followed by a second
    # "-" dash and from 8 to 32 additional lower-case letters or digits.
    organizational_unit_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DeletePolicyRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "policy_id",
                "PolicyId",
                TypeInfo(str),
            ),
        ]

    # The unique identifier (ID) of the policy that you want to delete. You can
    # get the ID from the ListPolicies or ListPoliciesForTarget operations.

    # The [regex pattern](http://wikipedia.org/wiki/regex) for a policy ID string
    # requires "p-" followed by from 8 to 128 lower-case letters or digits.
    policy_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DescribeAccountRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "account_id",
                "AccountId",
                TypeInfo(str),
            ),
        ]

    # The unique identifier (ID) of the AWS account that you want information
    # about. You can get the ID from the ListAccounts or ListAccountsForParent
    # operations.

    # The [regex pattern](http://wikipedia.org/wiki/regex) for an account ID
    # string requires exactly 12 digits.
    account_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DescribeAccountResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "account",
                "Account",
                TypeInfo(Account),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A structure that contains information about the requested account.
    account: "Account" = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DescribeCreateAccountStatusRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "create_account_request_id",
                "CreateAccountRequestId",
                TypeInfo(str),
            ),
        ]

    # Specifies the `operationId` that uniquely identifies the request. You can
    # get the ID from the response to an earlier CreateAccount request, or from
    # the ListCreateAccountStatus operation.

    # The [regex pattern](http://wikipedia.org/wiki/regex) for an create account
    # request ID string requires "car-" followed by from 8 to 32 lower-case
    # letters or digits.
    create_account_request_id: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class DescribeCreateAccountStatusResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "create_account_status",
                "CreateAccountStatus",
                TypeInfo(CreateAccountStatus),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A structure that contains the current status of an account creation
    # request.
    create_account_status: "CreateAccountStatus" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class DescribeHandshakeRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "handshake_id",
                "HandshakeId",
                TypeInfo(str),
            ),
        ]

    # The unique identifier (ID) of the handshake that you want information
    # about. You can get the ID from the original call to
    # InviteAccountToOrganization, or from a call to ListHandshakesForAccount or
    # ListHandshakesForOrganization.

    # The [regex pattern](http://wikipedia.org/wiki/regex) for handshake ID
    # string requires "h-" followed by from 8 to 32 lower-case letters or digits.
    handshake_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DescribeHandshakeResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "handshake",
                "Handshake",
                TypeInfo(Handshake),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A structure that contains information about the specified handshake.
    handshake: "Handshake" = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DescribeOrganizationResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "organization",
                "Organization",
                TypeInfo(Organization),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A structure that contains information about the organization.
    organization: "Organization" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class DescribeOrganizationalUnitRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "organizational_unit_id",
                "OrganizationalUnitId",
                TypeInfo(str),
            ),
        ]

    # The unique identifier (ID) of the organizational unit that you want details
    # about. You can get the ID from the ListOrganizationalUnitsForParent
    # operation.

    # The [regex pattern](http://wikipedia.org/wiki/regex) for an organizational
    # unit ID string requires "ou-" followed by from 4 to 32 lower-case letters
    # or digits (the ID of the root that contains the OU) followed by a second
    # "-" dash and from 8 to 32 additional lower-case letters or digits.
    organizational_unit_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DescribeOrganizationalUnitResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "organizational_unit",
                "OrganizationalUnit",
                TypeInfo(OrganizationalUnit),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A structure that contains details about the specified OU.
    organizational_unit: "OrganizationalUnit" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class DescribePolicyRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "policy_id",
                "PolicyId",
                TypeInfo(str),
            ),
        ]

    # The unique identifier (ID) of the policy that you want details about. You
    # can get the ID from the ListPolicies or ListPoliciesForTarget operations.

    # The [regex pattern](http://wikipedia.org/wiki/regex) for a policy ID string
    # requires "p-" followed by from 8 to 128 lower-case letters or digits.
    policy_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DescribePolicyResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "policy",
                "Policy",
                TypeInfo(Policy),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A structure that contains details about the specified policy.
    policy: "Policy" = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DestinationParentNotFoundException(ShapeBase):
    """
    We can't find the destination container (a root or OU) with the ParentId that
    you specified.
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
class DetachPolicyRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "policy_id",
                "PolicyId",
                TypeInfo(str),
            ),
            (
                "target_id",
                "TargetId",
                TypeInfo(str),
            ),
        ]

    # The unique identifier (ID) of the policy you want to detach. You can get
    # the ID from the ListPolicies or ListPoliciesForTarget operations.

    # The [regex pattern](http://wikipedia.org/wiki/regex) for a policy ID string
    # requires "p-" followed by from 8 to 128 lower-case letters or digits.
    policy_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The unique identifier (ID) of the root, OU, or account from which you want
    # to detach the policy. You can get the ID from the ListRoots,
    # ListOrganizationalUnitsForParent, or ListAccounts operations.

    # The [regex pattern](http://wikipedia.org/wiki/regex) for a target ID string
    # requires one of the following:

    #   * Root: a string that begins with "r-" followed by from 4 to 32 lower-case letters or digits.

    #   * Account: a string that consists of exactly 12 digits.

    #   * Organizational unit (OU): a string that begins with "ou-" followed by from 4 to 32 lower-case letters or digits (the ID of the root that the OU is in) followed by a second "-" dash and from 8 to 32 additional lower-case letters or digits.
    target_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DisableAWSServiceAccessRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "service_principal",
                "ServicePrincipal",
                TypeInfo(str),
            ),
        ]

    # The service principal name of the AWS service for which you want to disable
    # integration with your organization. This is typically in the form of a URL,
    # such as ` _service-abbreviation_.amazonaws.com`.
    service_principal: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DisablePolicyTypeRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "root_id",
                "RootId",
                TypeInfo(str),
            ),
            (
                "policy_type",
                "PolicyType",
                TypeInfo(typing.Union[str, PolicyType]),
            ),
        ]

    # The unique identifier (ID) of the root in which you want to disable a
    # policy type. You can get the ID from the ListRoots operation.

    # The [regex pattern](http://wikipedia.org/wiki/regex) for a root ID string
    # requires "r-" followed by from 4 to 32 lower-case letters or digits.
    root_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The policy type that you want to disable in this root.
    policy_type: typing.Union[str, "PolicyType"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class DisablePolicyTypeResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "root",
                "Root",
                TypeInfo(Root),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A structure that shows the root with the updated list of enabled policy
    # types.
    root: "Root" = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DuplicateAccountException(ShapeBase):
    """
    That account is already present in the specified destination.
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
class DuplicateHandshakeException(ShapeBase):
    """
    A handshake with the same action and target already exists. For example, if you
    invited an account to join your organization, the invited account might already
    have a pending invitation from this organization. If you intend to resend an
    invitation to an account, ensure that existing handshakes that might be
    considered duplicates are canceled or declined.
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
class DuplicateOrganizationalUnitException(ShapeBase):
    """
    An organizational unit (OU) with the same name already exists.
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
class DuplicatePolicyAttachmentException(ShapeBase):
    """
    The selected policy is already attached to the specified target.
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
class DuplicatePolicyException(ShapeBase):
    """
    A policy with the same name already exists.
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
class EnableAWSServiceAccessRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "service_principal",
                "ServicePrincipal",
                TypeInfo(str),
            ),
        ]

    # The service principal name of the AWS service for which you want to enable
    # integration with your organization. This is typically in the form of a URL,
    # such as ` _service-abbreviation_.amazonaws.com`.
    service_principal: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class EnableAllFeaturesRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class EnableAllFeaturesResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "handshake",
                "Handshake",
                TypeInfo(Handshake),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A structure that contains details about the handshake created to support
    # this request to enable all features in the organization.
    handshake: "Handshake" = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class EnablePolicyTypeRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "root_id",
                "RootId",
                TypeInfo(str),
            ),
            (
                "policy_type",
                "PolicyType",
                TypeInfo(typing.Union[str, PolicyType]),
            ),
        ]

    # The unique identifier (ID) of the root in which you want to enable a policy
    # type. You can get the ID from the ListRoots operation.

    # The [regex pattern](http://wikipedia.org/wiki/regex) for a root ID string
    # requires "r-" followed by from 4 to 32 lower-case letters or digits.
    root_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The policy type that you want to enable.
    policy_type: typing.Union[str, "PolicyType"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class EnablePolicyTypeResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "root",
                "Root",
                TypeInfo(Root),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A structure that shows the root with the updated list of enabled policy
    # types.
    root: "Root" = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class EnabledServicePrincipal(ShapeBase):
    """
    A structure that contains details of a service principal that is enabled to
    integrate with AWS Organizations.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "service_principal",
                "ServicePrincipal",
                TypeInfo(str),
            ),
            (
                "date_enabled",
                "DateEnabled",
                TypeInfo(datetime.datetime),
            ),
        ]

    # The name of the service principal. This is typically in the form of a URL,
    # such as: ` _servicename_.amazonaws.com`.
    service_principal: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The date that the service principal was enabled for integration with AWS
    # Organizations.
    date_enabled: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class FinalizingOrganizationException(ShapeBase):
    """
    AWS Organizations could not perform the operation because your organization has
    not finished initializing. This can take up to an hour. Try again later. If
    after one hour you continue to receive this error, contact [ AWS Customer
    Support](https://console.aws.amazon.com/support/home#/).
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
class Handshake(ShapeBase):
    """
    Contains information that must be exchanged to securely establish a relationship
    between two accounts (an _originator_ and a _recipient_ ). For example, when a
    master account (the originator) invites another account (the recipient) to join
    its organization, the two accounts exchange information as a series of handshake
    requests and responses.

    **Note:** Handshakes that are CANCELED, ACCEPTED, or DECLINED show up in lists
    for only 30 days after entering that state After that they are deleted.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "id",
                "Id",
                TypeInfo(str),
            ),
            (
                "arn",
                "Arn",
                TypeInfo(str),
            ),
            (
                "parties",
                "Parties",
                TypeInfo(typing.List[HandshakeParty]),
            ),
            (
                "state",
                "State",
                TypeInfo(typing.Union[str, HandshakeState]),
            ),
            (
                "requested_timestamp",
                "RequestedTimestamp",
                TypeInfo(datetime.datetime),
            ),
            (
                "expiration_timestamp",
                "ExpirationTimestamp",
                TypeInfo(datetime.datetime),
            ),
            (
                "action",
                "Action",
                TypeInfo(typing.Union[str, ActionType]),
            ),
            (
                "resources",
                "Resources",
                TypeInfo(typing.List[HandshakeResource]),
            ),
        ]

    # The unique identifier (ID) of a handshake. The originating account creates
    # the ID when it initiates the handshake.

    # The [regex pattern](http://wikipedia.org/wiki/regex) for handshake ID
    # string requires "h-" followed by from 8 to 32 lower-case letters or digits.
    id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The Amazon Resource Name (ARN) of a handshake.

    # For more information about ARNs in Organizations, see [ARN Formats
    # Supported by
    # Organizations](http://docs.aws.amazon.com/organizations/latest/userguide/orgs_permissions.html#orgs-
    # permissions-arns) in the _AWS Organizations User Guide_.
    arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Information about the two accounts that are participating in the handshake.
    parties: typing.List["HandshakeParty"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The current state of the handshake. Use the state to trace the flow of the
    # handshake through the process from its creation to its acceptance. The
    # meaning of each of the valid values is as follows:

    #   * **REQUESTED** : This handshake was sent to multiple recipients (applicable to only some handshake types) and not all recipients have responded yet. The request stays in this state until all recipients respond.

    #   * **OPEN** : This handshake was sent to multiple recipients (applicable to only some policy types) and all recipients have responded, allowing the originator to complete the handshake action.

    #   * **CANCELED** : This handshake is no longer active because it was canceled by the originating account.

    #   * **ACCEPTED** : This handshake is complete because it has been accepted by the recipient.

    #   * **DECLINED** : This handshake is no longer active because it was declined by the recipient account.

    #   * **EXPIRED** : This handshake is no longer active because the originator did not receive a response of any kind from the recipient before the expiration time (15 days).
    state: typing.Union[str, "HandshakeState"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The date and time that the handshake request was made.
    requested_timestamp: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The date and time that the handshake expires. If the recipient of the
    # handshake request fails to respond before the specified date and time, the
    # handshake becomes inactive and is no longer valid.
    expiration_timestamp: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The type of handshake, indicating what action occurs when the recipient
    # accepts the handshake. The following handshake types are supported:

    #   * **INVITE** : This type of handshake represents a request to join an organization. It is always sent from the master account to only non-member accounts.

    #   * **ENABLE_ALL_FEATURES** : This type of handshake represents a request to enable all features in an organization. It is always sent from the master account to only _invited_ member accounts. Created accounts do not receive this because those accounts were created by the organization's master account and approval is inferred.

    #   * **APPROVE_ALL_FEATURES** : This type of handshake is sent from the Organizations service when all member accounts have approved the `ENABLE_ALL_FEATURES` invitation. It is sent only to the master account and signals the master that it can finalize the process to enable all features.
    action: typing.Union[str, "ActionType"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Additional information that is needed to process the handshake.
    resources: typing.List["HandshakeResource"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class HandshakeAlreadyInStateException(ShapeBase):
    """
    The specified handshake is already in the requested state. For example, you
    can't accept a handshake that was already accepted.
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
class HandshakeConstraintViolationException(ShapeBase):
    """
    The requested operation would violate the constraint identified in the reason
    code.

    Some of the reasons in the following list might not be applicable to this
    specific API or operation:

      * ACCOUNT_NUMBER_LIMIT_EXCEEDED: You attempted to exceed the limit on the number of accounts in an organization. **Note** : deleted and closed accounts still count toward your limit.

    If you get this exception immediately after creating the organization, wait one
    hour and try again. If after an hour it continues to fail with this error,
    contact [AWS Customer Support](https://console.aws.amazon.com/support/home#/).

      * HANDSHAKE_RATE_LIMIT_EXCEEDED: You attempted to exceed the number of handshakes you can send in one day.

      * ALREADY_IN_AN_ORGANIZATION: The handshake request is invalid because the invited account is already a member of an organization.

      * ORGANIZATION_ALREADY_HAS_ALL_FEATURES: The handshake request is invalid because the organization has already enabled all features.

      * INVITE_DISABLED_DURING_ENABLE_ALL_FEATURES: You cannot issue new invitations to join an organization while it is in the process of enabling all features. You can resume inviting accounts after you finalize the process when all accounts have agreed to the change.

      * PAYMENT_INSTRUMENT_REQUIRED: You cannot complete the operation with an account that does not have a payment instrument, such as a credit card, associated with it.

      * ORGANIZATION_FROM_DIFFERENT_SELLER_OF_RECORD: The request failed because the account is from a different marketplace than the accounts in the organization. For example, accounts with India addresses must be associated with the AISPL marketplace. All accounts in an organization must be from the same marketplace.

      * ORGANIZATION_MEMBERSHIP_CHANGE_RATE_LIMIT_EXCEEDED: You attempted to change the membership of an account too quickly after its previous change.
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
                "reason",
                "Reason",
                TypeInfo(
                    typing.
                    Union[str, HandshakeConstraintViolationExceptionReason]
                ),
            ),
        ]

    message: str = dataclasses.field(default=ShapeBase.NOT_SET, )
    reason: typing.Union[str, "HandshakeConstraintViolationExceptionReason"
                        ] = dataclasses.field(
                            default=ShapeBase.NOT_SET,
                        )


class HandshakeConstraintViolationExceptionReason(str):
    ACCOUNT_NUMBER_LIMIT_EXCEEDED = "ACCOUNT_NUMBER_LIMIT_EXCEEDED"
    HANDSHAKE_RATE_LIMIT_EXCEEDED = "HANDSHAKE_RATE_LIMIT_EXCEEDED"
    ALREADY_IN_AN_ORGANIZATION = "ALREADY_IN_AN_ORGANIZATION"
    ORGANIZATION_ALREADY_HAS_ALL_FEATURES = "ORGANIZATION_ALREADY_HAS_ALL_FEATURES"
    INVITE_DISABLED_DURING_ENABLE_ALL_FEATURES = "INVITE_DISABLED_DURING_ENABLE_ALL_FEATURES"
    PAYMENT_INSTRUMENT_REQUIRED = "PAYMENT_INSTRUMENT_REQUIRED"
    ORGANIZATION_FROM_DIFFERENT_SELLER_OF_RECORD = "ORGANIZATION_FROM_DIFFERENT_SELLER_OF_RECORD"
    ORGANIZATION_MEMBERSHIP_CHANGE_RATE_LIMIT_EXCEEDED = "ORGANIZATION_MEMBERSHIP_CHANGE_RATE_LIMIT_EXCEEDED"


@dataclasses.dataclass
class HandshakeFilter(ShapeBase):
    """
    Specifies the criteria that are used to select the handshakes for the operation.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "action_type",
                "ActionType",
                TypeInfo(typing.Union[str, ActionType]),
            ),
            (
                "parent_handshake_id",
                "ParentHandshakeId",
                TypeInfo(str),
            ),
        ]

    # Specifies the type of handshake action.

    # If you specify `ActionType`, you cannot also specify `ParentHandshakeId`.
    action_type: typing.Union[str, "ActionType"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Specifies the parent handshake. Only used for handshake types that are a
    # child of another type.

    # If you specify `ParentHandshakeId`, you cannot also specify `ActionType`.

    # The [regex pattern](http://wikipedia.org/wiki/regex) for handshake ID
    # string requires "h-" followed by from 8 to 32 lower-case letters or digits.
    parent_handshake_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class HandshakeNotFoundException(ShapeBase):
    """
    We can't find a handshake with the HandshakeId that you specified.
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
class HandshakeParty(ShapeBase):
    """
    Identifies a participant in a handshake.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "id",
                "Id",
                TypeInfo(str),
            ),
            (
                "type",
                "Type",
                TypeInfo(typing.Union[str, HandshakePartyType]),
            ),
        ]

    # The unique identifier (ID) for the party.

    # The [regex pattern](http://wikipedia.org/wiki/regex) for handshake ID
    # string requires "h-" followed by from 8 to 32 lower-case letters or digits.
    id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The type of party.
    type: typing.Union[str, "HandshakePartyType"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


class HandshakePartyType(str):
    ACCOUNT = "ACCOUNT"
    ORGANIZATION = "ORGANIZATION"
    EMAIL = "EMAIL"


@dataclasses.dataclass
class HandshakeResource(ShapeBase):
    """
    Contains additional data that is needed to process a handshake.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "value",
                "Value",
                TypeInfo(str),
            ),
            (
                "type",
                "Type",
                TypeInfo(typing.Union[str, HandshakeResourceType]),
            ),
            (
                "resources",
                "Resources",
                TypeInfo(typing.List[HandshakeResource]),
            ),
        ]

    # The information that is passed to the other party in the handshake. The
    # format of the value string must match the requirements of the specified
    # type.
    value: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The type of information being passed, specifying how the value is to be
    # interpreted by the other party:

    #   * `ACCOUNT` \- Specifies an AWS account ID number.

    #   * `ORGANIZATION` \- Specifies an organization ID number.

    #   * `EMAIL` \- Specifies the email address that is associated with the account that receives the handshake.

    #   * `OWNER_EMAIL` \- Specifies the email address associated with the master account. Included as information about an organization.

    #   * `OWNER_NAME` \- Specifies the name associated with the master account. Included as information about an organization.

    #   * `NOTES` \- Additional text provided by the handshake initiator and intended for the recipient to read.
    type: typing.Union[str, "HandshakeResourceType"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # When needed, contains an additional array of `HandshakeResource` objects.
    resources: typing.List["HandshakeResource"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


class HandshakeResourceType(str):
    ACCOUNT = "ACCOUNT"
    ORGANIZATION = "ORGANIZATION"
    ORGANIZATION_FEATURE_SET = "ORGANIZATION_FEATURE_SET"
    EMAIL = "EMAIL"
    MASTER_EMAIL = "MASTER_EMAIL"
    MASTER_NAME = "MASTER_NAME"
    NOTES = "NOTES"
    PARENT_HANDSHAKE = "PARENT_HANDSHAKE"


class HandshakeState(str):
    REQUESTED = "REQUESTED"
    OPEN = "OPEN"
    CANCELED = "CANCELED"
    ACCEPTED = "ACCEPTED"
    DECLINED = "DECLINED"
    EXPIRED = "EXPIRED"


class IAMUserAccessToBilling(str):
    ALLOW = "ALLOW"
    DENY = "DENY"


@dataclasses.dataclass
class InvalidHandshakeTransitionException(ShapeBase):
    """
    You can't perform the operation on the handshake in its current state. For
    example, you can't cancel a handshake that was already accepted, or accept a
    handshake that was already declined.
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
class InvalidInputException(ShapeBase):
    """
    The requested operation failed because you provided invalid values for one or
    more of the request parameters. This exception includes a reason that contains
    additional information about the violated limit:

    Some of the reasons in the following list might not be applicable to this
    specific API or operation:

      * IMMUTABLE_POLICY: You specified a policy that is managed by AWS and cannot be modified.

      * INPUT_REQUIRED: You must include a value for all required parameters.

      * INVALID_ENUM: You specified a value that is not valid for that parameter.

      * INVALID_FULL_NAME_TARGET: You specified a full name that contains invalid characters.

      * INVALID_LIST_MEMBER: You provided a list to a parameter that contains at least one invalid value.

      * INVALID_PARTY_TYPE_TARGET: You specified the wrong type of entity (account, organization, or email) as a party.

      * INVALID_PAGINATION_TOKEN: Get the value for the NextToken parameter from the response to a previous call of the operation.

      * INVALID_PATTERN: You provided a value that doesn't match the required pattern.

      * INVALID_PATTERN_TARGET_ID: You specified a policy target ID that doesn't match the required pattern.

      * INVALID_ROLE_NAME: You provided a role name that is not valid. A role name can’t begin with the reserved prefix 'AWSServiceRoleFor'.

      * INVALID_SYNTAX_ORGANIZATION_ARN: You specified an invalid ARN for the organization.

      * INVALID_SYNTAX_POLICY_ID: You specified an invalid policy ID. 

      * MAX_FILTER_LIMIT_EXCEEDED: You can specify only one filter parameter for the operation.

      * MAX_LENGTH_EXCEEDED: You provided a string parameter that is longer than allowed.

      * MAX_VALUE_EXCEEDED: You provided a numeric parameter that has a larger value than allowed.

      * MIN_LENGTH_EXCEEDED: You provided a string parameter that is shorter than allowed.

      * MIN_VALUE_EXCEEDED: You provided a numeric parameter that has a smaller value than allowed.

      * MOVING_ACCOUNT_BETWEEN_DIFFERENT_ROOTS: You can move an account only between entities in the same root.
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
                "reason",
                "Reason",
                TypeInfo(typing.Union[str, InvalidInputExceptionReason]),
            ),
        ]

    message: str = dataclasses.field(default=ShapeBase.NOT_SET, )
    reason: typing.Union[str, "InvalidInputExceptionReason"
                        ] = dataclasses.field(
                            default=ShapeBase.NOT_SET,
                        )


class InvalidInputExceptionReason(str):
    INVALID_PARTY_TYPE_TARGET = "INVALID_PARTY_TYPE_TARGET"
    INVALID_SYNTAX_ORGANIZATION_ARN = "INVALID_SYNTAX_ORGANIZATION_ARN"
    INVALID_SYNTAX_POLICY_ID = "INVALID_SYNTAX_POLICY_ID"
    INVALID_ENUM = "INVALID_ENUM"
    INVALID_LIST_MEMBER = "INVALID_LIST_MEMBER"
    MAX_LENGTH_EXCEEDED = "MAX_LENGTH_EXCEEDED"
    MAX_VALUE_EXCEEDED = "MAX_VALUE_EXCEEDED"
    MIN_LENGTH_EXCEEDED = "MIN_LENGTH_EXCEEDED"
    MIN_VALUE_EXCEEDED = "MIN_VALUE_EXCEEDED"
    IMMUTABLE_POLICY = "IMMUTABLE_POLICY"
    INVALID_PATTERN = "INVALID_PATTERN"
    INVALID_PATTERN_TARGET_ID = "INVALID_PATTERN_TARGET_ID"
    INPUT_REQUIRED = "INPUT_REQUIRED"
    INVALID_NEXT_TOKEN = "INVALID_NEXT_TOKEN"
    MAX_LIMIT_EXCEEDED_FILTER = "MAX_LIMIT_EXCEEDED_FILTER"
    MOVING_ACCOUNT_BETWEEN_DIFFERENT_ROOTS = "MOVING_ACCOUNT_BETWEEN_DIFFERENT_ROOTS"
    INVALID_FULL_NAME_TARGET = "INVALID_FULL_NAME_TARGET"
    UNRECOGNIZED_SERVICE_PRINCIPAL = "UNRECOGNIZED_SERVICE_PRINCIPAL"
    INVALID_ROLE_NAME = "INVALID_ROLE_NAME"


@dataclasses.dataclass
class InviteAccountToOrganizationRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "target",
                "Target",
                TypeInfo(HandshakeParty),
            ),
            (
                "notes",
                "Notes",
                TypeInfo(str),
            ),
        ]

    # The identifier (ID) of the AWS account that you want to invite to join your
    # organization. This is a JSON object that contains the following elements:

    # `{ "Type": "ACCOUNT", "Id": "< _**account id number** _ >" }`

    # If you use the AWS CLI, you can submit this as a single string, similar to
    # the following example:

    # `--target Id=123456789012,Type=ACCOUNT`

    # If you specify `"Type": "ACCOUNT"`, then you must provide the AWS account
    # ID number as the `Id`. If you specify `"Type": "EMAIL"`, then you must
    # specify the email address that is associated with the account.

    # `--target Id=bill@example.com,Type=EMAIL`
    target: "HandshakeParty" = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Additional information that you want to include in the generated email to
    # the recipient account owner.
    notes: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class InviteAccountToOrganizationResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "handshake",
                "Handshake",
                TypeInfo(Handshake),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A structure that contains details about the handshake that is created to
    # support this invitation request.
    handshake: "Handshake" = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ListAWSServiceAccessForOrganizationRequest(ShapeBase):
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
        ]

    # Use this parameter if you receive a `NextToken` response in a previous
    # request that indicates that there is more output available. Set it to the
    # value of the previous call's `NextToken` response to indicate where the
    # output should continue from.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # (Optional) Use this to limit the number of results you want included in the
    # response. If you do not include this parameter, it defaults to a value that
    # is specific to the operation. If additional items exist beyond the maximum
    # you specify, the `NextToken` response element is present and has a value
    # (is not null). Include that value as the `NextToken` request parameter in
    # the next call to the operation to get the next part of the results. Note
    # that Organizations might return fewer results than the maximum even when
    # there are more results available. You should check `NextToken` after every
    # operation to ensure that you receive all of the results.
    max_results: int = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ListAWSServiceAccessForOrganizationResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "enabled_service_principals",
                "EnabledServicePrincipals",
                TypeInfo(typing.List[EnabledServicePrincipal]),
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

    # A list of the service principals for the services that are enabled to
    # integrate with your organization. Each principal is a structure that
    # includes the name and the date that it was enabled for integration with AWS
    # Organizations.
    enabled_service_principals: typing.List["EnabledServicePrincipal"
                                           ] = dataclasses.field(
                                               default=ShapeBase.NOT_SET,
                                           )

    # If present, this value indicates that there is more output available than
    # is included in the current response. Use this value in the `NextToken`
    # request parameter in a subsequent call to the operation to get the next
    # part of the output. You should repeat this until the `NextToken` response
    # element comes back as `null`.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    def paginate(self, ) -> typing.Generator[
        "ListAWSServiceAccessForOrganizationResponse", None, None]:
        yield from super()._paginate()


@dataclasses.dataclass
class ListAccountsForParentRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "parent_id",
                "ParentId",
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

    # The unique identifier (ID) for the parent root or organization unit (OU)
    # whose accounts you want to list.
    parent_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Use this parameter if you receive a `NextToken` response in a previous
    # request that indicates that there is more output available. Set it to the
    # value of the previous call's `NextToken` response to indicate where the
    # output should continue from.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # (Optional) Use this to limit the number of results you want included in the
    # response. If you do not include this parameter, it defaults to a value that
    # is specific to the operation. If additional items exist beyond the maximum
    # you specify, the `NextToken` response element is present and has a value
    # (is not null). Include that value as the `NextToken` request parameter in
    # the next call to the operation to get the next part of the results. Note
    # that Organizations might return fewer results than the maximum even when
    # there are more results available. You should check `NextToken` after every
    # operation to ensure that you receive all of the results.
    max_results: int = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ListAccountsForParentResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "accounts",
                "Accounts",
                TypeInfo(typing.List[Account]),
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

    # A list of the accounts in the specified root or OU.
    accounts: typing.List["Account"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # If present, this value indicates that there is more output available than
    # is included in the current response. Use this value in the `NextToken`
    # request parameter in a subsequent call to the operation to get the next
    # part of the output. You should repeat this until the `NextToken` response
    # element comes back as `null`.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    def paginate(
        self,
    ) -> typing.Generator["ListAccountsForParentResponse", None, None]:
        yield from super()._paginate()


@dataclasses.dataclass
class ListAccountsRequest(ShapeBase):
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
        ]

    # Use this parameter if you receive a `NextToken` response in a previous
    # request that indicates that there is more output available. Set it to the
    # value of the previous call's `NextToken` response to indicate where the
    # output should continue from.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # (Optional) Use this to limit the number of results you want included in the
    # response. If you do not include this parameter, it defaults to a value that
    # is specific to the operation. If additional items exist beyond the maximum
    # you specify, the `NextToken` response element is present and has a value
    # (is not null). Include that value as the `NextToken` request parameter in
    # the next call to the operation to get the next part of the results. Note
    # that Organizations might return fewer results than the maximum even when
    # there are more results available. You should check `NextToken` after every
    # operation to ensure that you receive all of the results.
    max_results: int = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ListAccountsResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "accounts",
                "Accounts",
                TypeInfo(typing.List[Account]),
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

    # A list of objects in the organization.
    accounts: typing.List["Account"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # If present, this value indicates that there is more output available than
    # is included in the current response. Use this value in the `NextToken`
    # request parameter in a subsequent call to the operation to get the next
    # part of the output. You should repeat this until the `NextToken` response
    # element comes back as `null`.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    def paginate(self,
                ) -> typing.Generator["ListAccountsResponse", None, None]:
        yield from super()._paginate()


@dataclasses.dataclass
class ListChildrenRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "parent_id",
                "ParentId",
                TypeInfo(str),
            ),
            (
                "child_type",
                "ChildType",
                TypeInfo(typing.Union[str, ChildType]),
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

    # The unique identifier (ID) for the parent root or OU whose children you
    # want to list.

    # The [regex pattern](http://wikipedia.org/wiki/regex) for a parent ID string
    # requires one of the following:

    #   * Root: a string that begins with "r-" followed by from 4 to 32 lower-case letters or digits.

    #   * Organizational unit (OU): a string that begins with "ou-" followed by from 4 to 32 lower-case letters or digits (the ID of the root that the OU is in) followed by a second "-" dash and from 8 to 32 additional lower-case letters or digits.
    parent_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Filters the output to include only the specified child type.
    child_type: typing.Union[str, "ChildType"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Use this parameter if you receive a `NextToken` response in a previous
    # request that indicates that there is more output available. Set it to the
    # value of the previous call's `NextToken` response to indicate where the
    # output should continue from.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # (Optional) Use this to limit the number of results you want included in the
    # response. If you do not include this parameter, it defaults to a value that
    # is specific to the operation. If additional items exist beyond the maximum
    # you specify, the `NextToken` response element is present and has a value
    # (is not null). Include that value as the `NextToken` request parameter in
    # the next call to the operation to get the next part of the results. Note
    # that Organizations might return fewer results than the maximum even when
    # there are more results available. You should check `NextToken` after every
    # operation to ensure that you receive all of the results.
    max_results: int = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ListChildrenResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "children",
                "Children",
                TypeInfo(typing.List[Child]),
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

    # The list of children of the specified parent container.
    children: typing.List["Child"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # If present, this value indicates that there is more output available than
    # is included in the current response. Use this value in the `NextToken`
    # request parameter in a subsequent call to the operation to get the next
    # part of the output. You should repeat this until the `NextToken` response
    # element comes back as `null`.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    def paginate(self,
                ) -> typing.Generator["ListChildrenResponse", None, None]:
        yield from super()._paginate()


@dataclasses.dataclass
class ListCreateAccountStatusRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "states",
                "States",
                TypeInfo(typing.List[typing.Union[str, CreateAccountState]]),
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

    # A list of one or more states that you want included in the response. If
    # this parameter is not present, then all requests are included in the
    # response.
    states: typing.List[typing.Union[str, "CreateAccountState"]
                       ] = dataclasses.field(
                           default=ShapeBase.NOT_SET,
                       )

    # Use this parameter if you receive a `NextToken` response in a previous
    # request that indicates that there is more output available. Set it to the
    # value of the previous call's `NextToken` response to indicate where the
    # output should continue from.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # (Optional) Use this to limit the number of results you want included in the
    # response. If you do not include this parameter, it defaults to a value that
    # is specific to the operation. If additional items exist beyond the maximum
    # you specify, the `NextToken` response element is present and has a value
    # (is not null). Include that value as the `NextToken` request parameter in
    # the next call to the operation to get the next part of the results. Note
    # that Organizations might return fewer results than the maximum even when
    # there are more results available. You should check `NextToken` after every
    # operation to ensure that you receive all of the results.
    max_results: int = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ListCreateAccountStatusResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "create_account_statuses",
                "CreateAccountStatuses",
                TypeInfo(typing.List[CreateAccountStatus]),
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

    # A list of objects with details about the requests. Certain elements, such
    # as the accountId number, are present in the output only after the account
    # has been successfully created.
    create_account_statuses: typing.List["CreateAccountStatus"
                                        ] = dataclasses.field(
                                            default=ShapeBase.NOT_SET,
                                        )

    # If present, this value indicates that there is more output available than
    # is included in the current response. Use this value in the `NextToken`
    # request parameter in a subsequent call to the operation to get the next
    # part of the output. You should repeat this until the `NextToken` response
    # element comes back as `null`.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    def paginate(
        self,
    ) -> typing.Generator["ListCreateAccountStatusResponse", None, None]:
        yield from super()._paginate()


@dataclasses.dataclass
class ListHandshakesForAccountRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "filter",
                "Filter",
                TypeInfo(HandshakeFilter),
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

    # Filters the handshakes that you want included in the response. The default
    # is all types. Use the `ActionType` element to limit the output to only a
    # specified type, such as `INVITE`, `ENABLE-FULL-CONTROL`, or `APPROVE-FULL-
    # CONTROL`. Alternatively, for the `ENABLE-FULL-CONTROL` handshake that
    # generates a separate child handshake for each member account, you can
    # specify `ParentHandshakeId` to see only the handshakes that were generated
    # by that parent request.
    filter: "HandshakeFilter" = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Use this parameter if you receive a `NextToken` response in a previous
    # request that indicates that there is more output available. Set it to the
    # value of the previous call's `NextToken` response to indicate where the
    # output should continue from.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # (Optional) Use this to limit the number of results you want included in the
    # response. If you do not include this parameter, it defaults to a value that
    # is specific to the operation. If additional items exist beyond the maximum
    # you specify, the `NextToken` response element is present and has a value
    # (is not null). Include that value as the `NextToken` request parameter in
    # the next call to the operation to get the next part of the results. Note
    # that Organizations might return fewer results than the maximum even when
    # there are more results available. You should check `NextToken` after every
    # operation to ensure that you receive all of the results.
    max_results: int = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ListHandshakesForAccountResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "handshakes",
                "Handshakes",
                TypeInfo(typing.List[Handshake]),
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

    # A list of Handshake objects with details about each of the handshakes that
    # is associated with the specified account.
    handshakes: typing.List["Handshake"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # If present, this value indicates that there is more output available than
    # is included in the current response. Use this value in the `NextToken`
    # request parameter in a subsequent call to the operation to get the next
    # part of the output. You should repeat this until the `NextToken` response
    # element comes back as `null`.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    def paginate(
        self,
    ) -> typing.Generator["ListHandshakesForAccountResponse", None, None]:
        yield from super()._paginate()


@dataclasses.dataclass
class ListHandshakesForOrganizationRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "filter",
                "Filter",
                TypeInfo(HandshakeFilter),
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

    # A filter of the handshakes that you want included in the response. The
    # default is all types. Use the `ActionType` element to limit the output to
    # only a specified type, such as `INVITE`, `ENABLE-ALL-FEATURES`, or
    # `APPROVE-ALL-FEATURES`. Alternatively, for the `ENABLE-ALL-FEATURES`
    # handshake that generates a separate child handshake for each member
    # account, you can specify the `ParentHandshakeId` to see only the handshakes
    # that were generated by that parent request.
    filter: "HandshakeFilter" = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Use this parameter if you receive a `NextToken` response in a previous
    # request that indicates that there is more output available. Set it to the
    # value of the previous call's `NextToken` response to indicate where the
    # output should continue from.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # (Optional) Use this to limit the number of results you want included in the
    # response. If you do not include this parameter, it defaults to a value that
    # is specific to the operation. If additional items exist beyond the maximum
    # you specify, the `NextToken` response element is present and has a value
    # (is not null). Include that value as the `NextToken` request parameter in
    # the next call to the operation to get the next part of the results. Note
    # that Organizations might return fewer results than the maximum even when
    # there are more results available. You should check `NextToken` after every
    # operation to ensure that you receive all of the results.
    max_results: int = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ListHandshakesForOrganizationResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "handshakes",
                "Handshakes",
                TypeInfo(typing.List[Handshake]),
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

    # A list of Handshake objects with details about each of the handshakes that
    # are associated with an organization.
    handshakes: typing.List["Handshake"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # If present, this value indicates that there is more output available than
    # is included in the current response. Use this value in the `NextToken`
    # request parameter in a subsequent call to the operation to get the next
    # part of the output. You should repeat this until the `NextToken` response
    # element comes back as `null`.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    def paginate(
        self,
    ) -> typing.Generator["ListHandshakesForOrganizationResponse", None, None]:
        yield from super()._paginate()


@dataclasses.dataclass
class ListOrganizationalUnitsForParentRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "parent_id",
                "ParentId",
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

    # The unique identifier (ID) of the root or OU whose child OUs you want to
    # list.

    # The [regex pattern](http://wikipedia.org/wiki/regex) for a parent ID string
    # requires one of the following:

    #   * Root: a string that begins with "r-" followed by from 4 to 32 lower-case letters or digits.

    #   * Organizational unit (OU): a string that begins with "ou-" followed by from 4 to 32 lower-case letters or digits (the ID of the root that the OU is in) followed by a second "-" dash and from 8 to 32 additional lower-case letters or digits.
    parent_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Use this parameter if you receive a `NextToken` response in a previous
    # request that indicates that there is more output available. Set it to the
    # value of the previous call's `NextToken` response to indicate where the
    # output should continue from.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # (Optional) Use this to limit the number of results you want included in the
    # response. If you do not include this parameter, it defaults to a value that
    # is specific to the operation. If additional items exist beyond the maximum
    # you specify, the `NextToken` response element is present and has a value
    # (is not null). Include that value as the `NextToken` request parameter in
    # the next call to the operation to get the next part of the results. Note
    # that Organizations might return fewer results than the maximum even when
    # there are more results available. You should check `NextToken` after every
    # operation to ensure that you receive all of the results.
    max_results: int = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ListOrganizationalUnitsForParentResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "organizational_units",
                "OrganizationalUnits",
                TypeInfo(typing.List[OrganizationalUnit]),
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

    # A list of the OUs in the specified root or parent OU.
    organizational_units: typing.List["OrganizationalUnit"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # If present, this value indicates that there is more output available than
    # is included in the current response. Use this value in the `NextToken`
    # request parameter in a subsequent call to the operation to get the next
    # part of the output. You should repeat this until the `NextToken` response
    # element comes back as `null`.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    def paginate(self, ) -> typing.Generator[
        "ListOrganizationalUnitsForParentResponse", None, None]:
        yield from super()._paginate()


@dataclasses.dataclass
class ListParentsRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "child_id",
                "ChildId",
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

    # The unique identifier (ID) of the OU or account whose parent containers you
    # want to list. Do not specify a root.

    # The [regex pattern](http://wikipedia.org/wiki/regex) for a child ID string
    # requires one of the following:

    #   * Account: a string that consists of exactly 12 digits.

    #   * Organizational unit (OU): a string that begins with "ou-" followed by from 4 to 32 lower-case letters or digits (the ID of the root that contains the OU) followed by a second "-" dash and from 8 to 32 additional lower-case letters or digits.
    child_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Use this parameter if you receive a `NextToken` response in a previous
    # request that indicates that there is more output available. Set it to the
    # value of the previous call's `NextToken` response to indicate where the
    # output should continue from.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # (Optional) Use this to limit the number of results you want included in the
    # response. If you do not include this parameter, it defaults to a value that
    # is specific to the operation. If additional items exist beyond the maximum
    # you specify, the `NextToken` response element is present and has a value
    # (is not null). Include that value as the `NextToken` request parameter in
    # the next call to the operation to get the next part of the results. Note
    # that Organizations might return fewer results than the maximum even when
    # there are more results available. You should check `NextToken` after every
    # operation to ensure that you receive all of the results.
    max_results: int = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ListParentsResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "parents",
                "Parents",
                TypeInfo(typing.List[Parent]),
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

    # A list of parents for the specified child account or OU.
    parents: typing.List["Parent"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # If present, this value indicates that there is more output available than
    # is included in the current response. Use this value in the `NextToken`
    # request parameter in a subsequent call to the operation to get the next
    # part of the output. You should repeat this until the `NextToken` response
    # element comes back as `null`.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    def paginate(self, ) -> typing.Generator["ListParentsResponse", None, None]:
        yield from super()._paginate()


@dataclasses.dataclass
class ListPoliciesForTargetRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "target_id",
                "TargetId",
                TypeInfo(str),
            ),
            (
                "filter",
                "Filter",
                TypeInfo(typing.Union[str, PolicyType]),
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

    # The unique identifier (ID) of the root, organizational unit, or account
    # whose policies you want to list.

    # The [regex pattern](http://wikipedia.org/wiki/regex) for a target ID string
    # requires one of the following:

    #   * Root: a string that begins with "r-" followed by from 4 to 32 lower-case letters or digits.

    #   * Account: a string that consists of exactly 12 digits.

    #   * Organizational unit (OU): a string that begins with "ou-" followed by from 4 to 32 lower-case letters or digits (the ID of the root that the OU is in) followed by a second "-" dash and from 8 to 32 additional lower-case letters or digits.
    target_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The type of policy that you want to include in the returned list.
    filter: typing.Union[str, "PolicyType"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Use this parameter if you receive a `NextToken` response in a previous
    # request that indicates that there is more output available. Set it to the
    # value of the previous call's `NextToken` response to indicate where the
    # output should continue from.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # (Optional) Use this to limit the number of results you want included in the
    # response. If you do not include this parameter, it defaults to a value that
    # is specific to the operation. If additional items exist beyond the maximum
    # you specify, the `NextToken` response element is present and has a value
    # (is not null). Include that value as the `NextToken` request parameter in
    # the next call to the operation to get the next part of the results. Note
    # that Organizations might return fewer results than the maximum even when
    # there are more results available. You should check `NextToken` after every
    # operation to ensure that you receive all of the results.
    max_results: int = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ListPoliciesForTargetResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "policies",
                "Policies",
                TypeInfo(typing.List[PolicySummary]),
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

    # The list of policies that match the criteria in the request.
    policies: typing.List["PolicySummary"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # If present, this value indicates that there is more output available than
    # is included in the current response. Use this value in the `NextToken`
    # request parameter in a subsequent call to the operation to get the next
    # part of the output. You should repeat this until the `NextToken` response
    # element comes back as `null`.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    def paginate(
        self,
    ) -> typing.Generator["ListPoliciesForTargetResponse", None, None]:
        yield from super()._paginate()


@dataclasses.dataclass
class ListPoliciesRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "filter",
                "Filter",
                TypeInfo(typing.Union[str, PolicyType]),
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

    # Specifies the type of policy that you want to include in the response.
    filter: typing.Union[str, "PolicyType"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Use this parameter if you receive a `NextToken` response in a previous
    # request that indicates that there is more output available. Set it to the
    # value of the previous call's `NextToken` response to indicate where the
    # output should continue from.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # (Optional) Use this to limit the number of results you want included in the
    # response. If you do not include this parameter, it defaults to a value that
    # is specific to the operation. If additional items exist beyond the maximum
    # you specify, the `NextToken` response element is present and has a value
    # (is not null). Include that value as the `NextToken` request parameter in
    # the next call to the operation to get the next part of the results. Note
    # that Organizations might return fewer results than the maximum even when
    # there are more results available. You should check `NextToken` after every
    # operation to ensure that you receive all of the results.
    max_results: int = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ListPoliciesResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "policies",
                "Policies",
                TypeInfo(typing.List[PolicySummary]),
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

    # A list of policies that match the filter criteria in the request. The
    # output list does not include the policy contents. To see the content for a
    # policy, see DescribePolicy.
    policies: typing.List["PolicySummary"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # If present, this value indicates that there is more output available than
    # is included in the current response. Use this value in the `NextToken`
    # request parameter in a subsequent call to the operation to get the next
    # part of the output. You should repeat this until the `NextToken` response
    # element comes back as `null`.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    def paginate(self,
                ) -> typing.Generator["ListPoliciesResponse", None, None]:
        yield from super()._paginate()


@dataclasses.dataclass
class ListRootsRequest(ShapeBase):
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
        ]

    # Use this parameter if you receive a `NextToken` response in a previous
    # request that indicates that there is more output available. Set it to the
    # value of the previous call's `NextToken` response to indicate where the
    # output should continue from.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # (Optional) Use this to limit the number of results you want included in the
    # response. If you do not include this parameter, it defaults to a value that
    # is specific to the operation. If additional items exist beyond the maximum
    # you specify, the `NextToken` response element is present and has a value
    # (is not null). Include that value as the `NextToken` request parameter in
    # the next call to the operation to get the next part of the results. Note
    # that Organizations might return fewer results than the maximum even when
    # there are more results available. You should check `NextToken` after every
    # operation to ensure that you receive all of the results.
    max_results: int = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ListRootsResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "roots",
                "Roots",
                TypeInfo(typing.List[Root]),
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

    # A list of roots that are defined in an organization.
    roots: typing.List["Root"] = dataclasses.field(default=ShapeBase.NOT_SET, )

    # If present, this value indicates that there is more output available than
    # is included in the current response. Use this value in the `NextToken`
    # request parameter in a subsequent call to the operation to get the next
    # part of the output. You should repeat this until the `NextToken` response
    # element comes back as `null`.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    def paginate(self, ) -> typing.Generator["ListRootsResponse", None, None]:
        yield from super()._paginate()


@dataclasses.dataclass
class ListTargetsForPolicyRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "policy_id",
                "PolicyId",
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

    # The unique identifier (ID) of the policy for which you want to know its
    # attachments.

    # The [regex pattern](http://wikipedia.org/wiki/regex) for a policy ID string
    # requires "p-" followed by from 8 to 128 lower-case letters or digits.
    policy_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Use this parameter if you receive a `NextToken` response in a previous
    # request that indicates that there is more output available. Set it to the
    # value of the previous call's `NextToken` response to indicate where the
    # output should continue from.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # (Optional) Use this to limit the number of results you want included in the
    # response. If you do not include this parameter, it defaults to a value that
    # is specific to the operation. If additional items exist beyond the maximum
    # you specify, the `NextToken` response element is present and has a value
    # (is not null). Include that value as the `NextToken` request parameter in
    # the next call to the operation to get the next part of the results. Note
    # that Organizations might return fewer results than the maximum even when
    # there are more results available. You should check `NextToken` after every
    # operation to ensure that you receive all of the results.
    max_results: int = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ListTargetsForPolicyResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "targets",
                "Targets",
                TypeInfo(typing.List[PolicyTargetSummary]),
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

    # A list of structures, each of which contains details about one of the
    # entities to which the specified policy is attached.
    targets: typing.List["PolicyTargetSummary"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # If present, this value indicates that there is more output available than
    # is included in the current response. Use this value in the `NextToken`
    # request parameter in a subsequent call to the operation to get the next
    # part of the output. You should repeat this until the `NextToken` response
    # element comes back as `null`.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    def paginate(
        self,
    ) -> typing.Generator["ListTargetsForPolicyResponse", None, None]:
        yield from super()._paginate()


@dataclasses.dataclass
class MalformedPolicyDocumentException(ShapeBase):
    """
    The provided policy document does not meet the requirements of the specified
    policy type. For example, the syntax might be incorrect. For details about
    service control policy syntax, see [Service Control Policy
    Syntax](http://docs.aws.amazon.com/organizations/latest/userguide/orgs_reference_scp-
    syntax.html) in the _AWS Organizations User Guide_.
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
class MasterCannotLeaveOrganizationException(ShapeBase):
    """
    You can't remove a master account from an organization. If you want the master
    account to become a member account in another organization, you must first
    delete the current organization of the master account.
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
class MoveAccountRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "account_id",
                "AccountId",
                TypeInfo(str),
            ),
            (
                "source_parent_id",
                "SourceParentId",
                TypeInfo(str),
            ),
            (
                "destination_parent_id",
                "DestinationParentId",
                TypeInfo(str),
            ),
        ]

    # The unique identifier (ID) of the account that you want to move.

    # The [regex pattern](http://wikipedia.org/wiki/regex) for an account ID
    # string requires exactly 12 digits.
    account_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The unique identifier (ID) of the root or organizational unit that you want
    # to move the account from.

    # The [regex pattern](http://wikipedia.org/wiki/regex) for a parent ID string
    # requires one of the following:

    #   * Root: a string that begins with "r-" followed by from 4 to 32 lower-case letters or digits.

    #   * Organizational unit (OU): a string that begins with "ou-" followed by from 4 to 32 lower-case letters or digits (the ID of the root that the OU is in) followed by a second "-" dash and from 8 to 32 additional lower-case letters or digits.
    source_parent_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The unique identifier (ID) of the root or organizational unit that you want
    # to move the account to.

    # The [regex pattern](http://wikipedia.org/wiki/regex) for a parent ID string
    # requires one of the following:

    #   * Root: a string that begins with "r-" followed by from 4 to 32 lower-case letters or digits.

    #   * Organizational unit (OU): a string that begins with "ou-" followed by from 4 to 32 lower-case letters or digits (the ID of the root that the OU is in) followed by a second "-" dash and from 8 to 32 additional lower-case letters or digits.
    destination_parent_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class Organization(ShapeBase):
    """
    Contains details about an organization. An organization is a collection of
    accounts that are centrally managed together using consolidated billing,
    organized hierarchically with organizational units (OUs), and controlled with
    policies .
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "id",
                "Id",
                TypeInfo(str),
            ),
            (
                "arn",
                "Arn",
                TypeInfo(str),
            ),
            (
                "feature_set",
                "FeatureSet",
                TypeInfo(typing.Union[str, OrganizationFeatureSet]),
            ),
            (
                "master_account_arn",
                "MasterAccountArn",
                TypeInfo(str),
            ),
            (
                "master_account_id",
                "MasterAccountId",
                TypeInfo(str),
            ),
            (
                "master_account_email",
                "MasterAccountEmail",
                TypeInfo(str),
            ),
            (
                "available_policy_types",
                "AvailablePolicyTypes",
                TypeInfo(typing.List[PolicyTypeSummary]),
            ),
        ]

    # The unique identifier (ID) of an organization.

    # The [regex pattern](http://wikipedia.org/wiki/regex) for an organization ID
    # string requires "o-" followed by from 10 to 32 lower-case letters or
    # digits.
    id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The Amazon Resource Name (ARN) of an organization.

    # For more information about ARNs in Organizations, see [ARN Formats
    # Supported by
    # Organizations](http://docs.aws.amazon.com/organizations/latest/userguide/orgs_permissions.html#orgs-
    # permissions-arns) in the _AWS Organizations User Guide_.
    arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Specifies the functionality that currently is available to the
    # organization. If set to "ALL", then all features are enabled and policies
    # can be applied to accounts in the organization. If set to
    # "CONSOLIDATED_BILLING", then only consolidated billing functionality is
    # available. For more information, see [Enabling All Features in Your
    # Organization](http://docs.aws.amazon.com/IAM/latest/UserGuide/orgs_manage_org_support-
    # all-features.html) in the _AWS Organizations User Guide_.
    feature_set: typing.Union[str, "OrganizationFeatureSet"
                             ] = dataclasses.field(
                                 default=ShapeBase.NOT_SET,
                             )

    # The Amazon Resource Name (ARN) of the account that is designated as the
    # master account for the organization.

    # For more information about ARNs in Organizations, see [ARN Formats
    # Supported by
    # Organizations](http://docs.aws.amazon.com/organizations/latest/userguide/orgs_permissions.html#orgs-
    # permissions-arns) in the _AWS Organizations User Guide_.
    master_account_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The unique identifier (ID) of the master account of an organization.

    # The [regex pattern](http://wikipedia.org/wiki/regex) for an account ID
    # string requires exactly 12 digits.
    master_account_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The email address that is associated with the AWS account that is
    # designated as the master account for the organization.
    master_account_email: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A list of policy types that are enabled for this organization. For example,
    # if your organization has all features enabled, then service control
    # policies (SCPs) are included in the list.

    # Even if a policy type is shown as available in the organization, you can
    # separately enable and disable them at the root level by using
    # EnablePolicyType and DisablePolicyType. Use ListRoots to see the status of
    # a policy type in that root.
    available_policy_types: typing.List["PolicyTypeSummary"
                                       ] = dataclasses.field(
                                           default=ShapeBase.NOT_SET,
                                       )


class OrganizationFeatureSet(str):
    ALL = "ALL"
    CONSOLIDATED_BILLING = "CONSOLIDATED_BILLING"


@dataclasses.dataclass
class OrganizationNotEmptyException(ShapeBase):
    """
    The organization isn't empty. To delete an organization, you must first remove
    all accounts except the master account, delete all organizational units (OUs),
    and delete all policies.
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
class OrganizationalUnit(ShapeBase):
    """
    Contains details about an organizational unit (OU). An OU is a container of AWS
    accounts within a root of an organization. Policies that are attached to an OU
    apply to all accounts contained in that OU and in any child OUs.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "id",
                "Id",
                TypeInfo(str),
            ),
            (
                "arn",
                "Arn",
                TypeInfo(str),
            ),
            (
                "name",
                "Name",
                TypeInfo(str),
            ),
        ]

    # The unique identifier (ID) associated with this OU.

    # The [regex pattern](http://wikipedia.org/wiki/regex) for an organizational
    # unit ID string requires "ou-" followed by from 4 to 32 lower-case letters
    # or digits (the ID of the root that contains the OU) followed by a second
    # "-" dash and from 8 to 32 additional lower-case letters or digits.
    id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The Amazon Resource Name (ARN) of this OU.

    # For more information about ARNs in Organizations, see [ARN Formats
    # Supported by
    # Organizations](http://docs.aws.amazon.com/organizations/latest/userguide/orgs_permissions.html#orgs-
    # permissions-arns) in the _AWS Organizations User Guide_.
    arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The friendly name of this OU.

    # The [regex pattern](http://wikipedia.org/wiki/regex) that is used to
    # validate this parameter is a string of any of the characters in the ASCII
    # character range.
    name: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class OrganizationalUnitNotEmptyException(ShapeBase):
    """
    The specified organizational unit (OU) is not empty. Move all accounts to
    another root or to other OUs, remove all child OUs, and then try the operation
    again.
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
class OrganizationalUnitNotFoundException(ShapeBase):
    """
    We can't find an organizational unit (OU) with the OrganizationalUnitId that you
    specified.
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
class Parent(ShapeBase):
    """
    Contains information about either a root or an organizational unit (OU) that can
    contain OUs or accounts in an organization.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "id",
                "Id",
                TypeInfo(str),
            ),
            (
                "type",
                "Type",
                TypeInfo(typing.Union[str, ParentType]),
            ),
        ]

    # The unique identifier (ID) of the parent entity.

    # The [regex pattern](http://wikipedia.org/wiki/regex) for a parent ID string
    # requires one of the following:

    #   * Root: a string that begins with "r-" followed by from 4 to 32 lower-case letters or digits.

    #   * Organizational unit (OU): a string that begins with "ou-" followed by from 4 to 32 lower-case letters or digits (the ID of the root that the OU is in) followed by a second "-" dash and from 8 to 32 additional lower-case letters or digits.
    id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The type of the parent entity.
    type: typing.Union[str, "ParentType"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class ParentNotFoundException(ShapeBase):
    """
    We can't find a root or organizational unit (OU) with the ParentId that you
    specified.
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


class ParentType(str):
    ROOT = "ROOT"
    ORGANIZATIONAL_UNIT = "ORGANIZATIONAL_UNIT"


@dataclasses.dataclass
class Policy(ShapeBase):
    """
    Contains rules to be applied to the affected accounts. Policies can be attached
    directly to accounts, or to roots and OUs to affect all accounts in those
    hierarchies.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "policy_summary",
                "PolicySummary",
                TypeInfo(PolicySummary),
            ),
            (
                "content",
                "Content",
                TypeInfo(str),
            ),
        ]

    # A structure that contains additional details about the policy.
    policy_summary: "PolicySummary" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The text content of the policy.
    content: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class PolicyInUseException(ShapeBase):
    """
    The policy is attached to one or more entities. You must detach it from all
    roots, organizational units (OUs), and accounts before performing this
    operation.
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
class PolicyNotAttachedException(ShapeBase):
    """
    The policy isn't attached to the specified target in the specified root.
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
class PolicyNotFoundException(ShapeBase):
    """
    We can't find a policy with the PolicyId that you specified.
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
class PolicySummary(ShapeBase):
    """
    Contains information about a policy, but does not include the content. To see
    the content of a policy, see DescribePolicy.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "id",
                "Id",
                TypeInfo(str),
            ),
            (
                "arn",
                "Arn",
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
            (
                "type",
                "Type",
                TypeInfo(typing.Union[str, PolicyType]),
            ),
            (
                "aws_managed",
                "AwsManaged",
                TypeInfo(bool),
            ),
        ]

    # The unique identifier (ID) of the policy.

    # The [regex pattern](http://wikipedia.org/wiki/regex) for a policy ID string
    # requires "p-" followed by from 8 to 128 lower-case letters or digits.
    id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The Amazon Resource Name (ARN) of the policy.

    # For more information about ARNs in Organizations, see [ARN Formats
    # Supported by
    # Organizations](http://docs.aws.amazon.com/organizations/latest/userguide/orgs_permissions.html#orgs-
    # permissions-arns) in the _AWS Organizations User Guide_.
    arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The friendly name of the policy.

    # The [regex pattern](http://wikipedia.org/wiki/regex) that is used to
    # validate this parameter is a string of any of the characters in the ASCII
    # character range.
    name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The description of the policy.
    description: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The type of policy.
    type: typing.Union[str, "PolicyType"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A boolean value that indicates whether the specified policy is an AWS
    # managed policy. If true, then you can attach the policy to roots, OUs, or
    # accounts, but you cannot edit it.
    aws_managed: bool = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class PolicyTargetSummary(ShapeBase):
    """
    Contains information about a root, OU, or account that a policy is attached to.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "target_id",
                "TargetId",
                TypeInfo(str),
            ),
            (
                "arn",
                "Arn",
                TypeInfo(str),
            ),
            (
                "name",
                "Name",
                TypeInfo(str),
            ),
            (
                "type",
                "Type",
                TypeInfo(typing.Union[str, TargetType]),
            ),
        ]

    # The unique identifier (ID) of the policy target.

    # The [regex pattern](http://wikipedia.org/wiki/regex) for a target ID string
    # requires one of the following:

    #   * Root: a string that begins with "r-" followed by from 4 to 32 lower-case letters or digits.

    #   * Account: a string that consists of exactly 12 digits.

    #   * Organizational unit (OU): a string that begins with "ou-" followed by from 4 to 32 lower-case letters or digits (the ID of the root that the OU is in) followed by a second "-" dash and from 8 to 32 additional lower-case letters or digits.
    target_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The Amazon Resource Name (ARN) of the policy target.

    # For more information about ARNs in Organizations, see [ARN Formats
    # Supported by
    # Organizations](http://docs.aws.amazon.com/organizations/latest/userguide/orgs_permissions.html#orgs-
    # permissions-arns) in the _AWS Organizations User Guide_.
    arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The friendly name of the policy target.

    # The [regex pattern](http://wikipedia.org/wiki/regex) that is used to
    # validate this parameter is a string of any of the characters in the ASCII
    # character range.
    name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The type of the policy target.
    type: typing.Union[str, "TargetType"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


class PolicyType(str):
    SERVICE_CONTROL_POLICY = "SERVICE_CONTROL_POLICY"


@dataclasses.dataclass
class PolicyTypeAlreadyEnabledException(ShapeBase):
    """
    The specified policy type is already enabled in the specified root.
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
class PolicyTypeNotAvailableForOrganizationException(ShapeBase):
    """
    You can't use the specified policy type with the feature set currently enabled
    for this organization. For example, you can enable service control policies
    (SCPs) only after you enable all features in the organization. For more
    information, see [Enabling and Disabling a Policy Type on a
    Root](http://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies.html#enable_policies_on_root)
    in the _AWS Organizations User Guide_.
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
class PolicyTypeNotEnabledException(ShapeBase):
    """
    The specified policy type is not currently enabled in this root. You cannot
    attach policies of the specified type to entities in a root until you enable
    that type in the root. For more information, see [Enabling All Features in Your
    Organization](http://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_org_support-
    all-features.html) in the _AWS Organizations User Guide_.
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


class PolicyTypeStatus(str):
    ENABLED = "ENABLED"
    PENDING_ENABLE = "PENDING_ENABLE"
    PENDING_DISABLE = "PENDING_DISABLE"


@dataclasses.dataclass
class PolicyTypeSummary(ShapeBase):
    """
    Contains information about a policy type and its status in the associated root.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "type",
                "Type",
                TypeInfo(typing.Union[str, PolicyType]),
            ),
            (
                "status",
                "Status",
                TypeInfo(typing.Union[str, PolicyTypeStatus]),
            ),
        ]

    # The name of the policy type.
    type: typing.Union[str, "PolicyType"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The status of the policy type as it relates to the associated root. To
    # attach a policy of the specified type to a root or to an OU or account in
    # that root, it must be available in the organization and enabled for that
    # root.
    status: typing.Union[str, "PolicyTypeStatus"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class RemoveAccountFromOrganizationRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "account_id",
                "AccountId",
                TypeInfo(str),
            ),
        ]

    # The unique identifier (ID) of the member account that you want to remove
    # from the organization.

    # The [regex pattern](http://wikipedia.org/wiki/regex) for an account ID
    # string requires exactly 12 digits.
    account_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class Root(ShapeBase):
    """
    Contains details about a root. A root is a top-level parent node in the
    hierarchy of an organization that can contain organizational units (OUs) and
    accounts. Every root contains every AWS account in the organization. Each root
    enables the accounts to be organized in a different way and to have different
    policy types enabled for use in that root.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "id",
                "Id",
                TypeInfo(str),
            ),
            (
                "arn",
                "Arn",
                TypeInfo(str),
            ),
            (
                "name",
                "Name",
                TypeInfo(str),
            ),
            (
                "policy_types",
                "PolicyTypes",
                TypeInfo(typing.List[PolicyTypeSummary]),
            ),
        ]

    # The unique identifier (ID) for the root.

    # The [regex pattern](http://wikipedia.org/wiki/regex) for a root ID string
    # requires "r-" followed by from 4 to 32 lower-case letters or digits.
    id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The Amazon Resource Name (ARN) of the root.

    # For more information about ARNs in Organizations, see [ARN Formats
    # Supported by
    # Organizations](http://docs.aws.amazon.com/organizations/latest/userguide/orgs_permissions.html#orgs-
    # permissions-arns) in the _AWS Organizations User Guide_.
    arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The friendly name of the root.

    # The [regex pattern](http://wikipedia.org/wiki/regex) that is used to
    # validate this parameter is a string of any of the characters in the ASCII
    # character range.
    name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The types of policies that are currently enabled for the root and therefore
    # can be attached to the root or to its OUs or accounts.

    # Even if a policy type is shown as available in the organization, you can
    # separately enable and disable them at the root level by using
    # EnablePolicyType and DisablePolicyType. Use DescribeOrganization to see the
    # availability of the policy types in that organization.
    policy_types: typing.List["PolicyTypeSummary"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class RootNotFoundException(ShapeBase):
    """
    We can't find a root with the RootId that you specified.
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
class ServiceException(ShapeBase):
    """
    AWS Organizations can't complete your request because of an internal service
    error. Try again later.
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
class SourceParentNotFoundException(ShapeBase):
    """
    We can't find a source root or OU with the ParentId that you specified.
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
class TargetNotFoundException(ShapeBase):
    """
    We can't find a root, OU, or account with the TargetId that you specified.
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


class TargetType(str):
    ACCOUNT = "ACCOUNT"
    ORGANIZATIONAL_UNIT = "ORGANIZATIONAL_UNIT"
    ROOT = "ROOT"


@dataclasses.dataclass
class TooManyRequestsException(ShapeBase):
    """
    You've sent too many requests in too short a period of time. The limit helps
    protect against denial-of-service attacks. Try again later.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "type",
                "Type",
                TypeInfo(str),
            ),
            (
                "message",
                "Message",
                TypeInfo(str),
            ),
        ]

    type: str = dataclasses.field(default=ShapeBase.NOT_SET, )
    message: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class UpdateOrganizationalUnitRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "organizational_unit_id",
                "OrganizationalUnitId",
                TypeInfo(str),
            ),
            (
                "name",
                "Name",
                TypeInfo(str),
            ),
        ]

    # The unique identifier (ID) of the OU that you want to rename. You can get
    # the ID from the ListOrganizationalUnitsForParent operation.

    # The [regex pattern](http://wikipedia.org/wiki/regex) for an organizational
    # unit ID string requires "ou-" followed by from 4 to 32 lower-case letters
    # or digits (the ID of the root that contains the OU) followed by a second
    # "-" dash and from 8 to 32 additional lower-case letters or digits.
    organizational_unit_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The new name that you want to assign to the OU.

    # The [regex pattern](http://wikipedia.org/wiki/regex) that is used to
    # validate this parameter is a string of any of the characters in the ASCII
    # character range.
    name: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class UpdateOrganizationalUnitResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "organizational_unit",
                "OrganizationalUnit",
                TypeInfo(OrganizationalUnit),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A structure that contains the details about the specified OU, including its
    # new name.
    organizational_unit: "OrganizationalUnit" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class UpdatePolicyRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "policy_id",
                "PolicyId",
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
            (
                "content",
                "Content",
                TypeInfo(str),
            ),
        ]

    # The unique identifier (ID) of the policy that you want to update.

    # The [regex pattern](http://wikipedia.org/wiki/regex) for a policy ID string
    # requires "p-" followed by from 8 to 128 lower-case letters or digits.
    policy_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # If provided, the new name for the policy.

    # The [regex pattern](http://wikipedia.org/wiki/regex) that is used to
    # validate this parameter is a string of any of the characters in the ASCII
    # character range.
    name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # If provided, the new description for the policy.
    description: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # If provided, the new content for the policy. The text must be correctly
    # formatted JSON that complies with the syntax for the policy's type. For
    # more information, see [Service Control Policy
    # Syntax](http://docs.aws.amazon.com/organizations/latest/userguide/orgs_reference_scp-
    # syntax.html) in the _AWS Organizations User Guide_.
    content: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class UpdatePolicyResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "policy",
                "Policy",
                TypeInfo(Policy),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A structure that contains details about the updated policy, showing the
    # requested changes.
    policy: "Policy" = dataclasses.field(default=ShapeBase.NOT_SET, )
