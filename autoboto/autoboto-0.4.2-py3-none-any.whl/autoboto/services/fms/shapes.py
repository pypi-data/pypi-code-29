import datetime
import typing
from autoboto import ShapeBase, OutputShapeBase, TypeInfo
import dataclasses


class AccountRoleStatus(str):
    READY = "READY"
    CREATING = "CREATING"
    PENDING_DELETION = "PENDING_DELETION"
    DELETING = "DELETING"
    DELETED = "DELETED"


@dataclasses.dataclass
class AssociateAdminAccountRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "admin_account",
                "AdminAccount",
                TypeInfo(str),
            ),
        ]

    # The AWS account ID to associate with AWS Firewall Manager as the AWS
    # Firewall Manager administrator account. This can be an AWS Organizations
    # master account or a member account. For more information about AWS
    # Organizations and master accounts, see [Managing the AWS Accounts in Your
    # Organization](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_accounts.html).
    admin_account: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ComplianceViolator(ShapeBase):
    """
    Details of the resource that is not protected by the policy.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "resource_id",
                "ResourceId",
                TypeInfo(str),
            ),
            (
                "violation_reason",
                "ViolationReason",
                TypeInfo(typing.Union[str, ViolationReason]),
            ),
            (
                "resource_type",
                "ResourceType",
                TypeInfo(str),
            ),
        ]

    # The resource ID.
    resource_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The reason that the resource is not protected by the policy.
    violation_reason: typing.Union[str, "ViolationReason"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The resource type. This is in the format shown in [AWS Resource Types
    # Reference](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-
    # template-resource-type-ref.html). Valid values are
    # `AWS::ElasticLoadBalancingV2::LoadBalancer` or
    # `AWS::CloudFront::Distribution`.
    resource_type: str = dataclasses.field(default=ShapeBase.NOT_SET, )


class CustomerPolicyScopeIdType(str):
    ACCOUNT = "ACCOUNT"


@dataclasses.dataclass
class DeleteNotificationChannelRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return []


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

    # The ID of the policy that you want to delete. `PolicyId` is returned by
    # `PutPolicy` and by `ListPolicies`.
    policy_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )


class DependentServiceName(str):
    AWSCONFIG = "AWSCONFIG"
    AWSWAF = "AWSWAF"


@dataclasses.dataclass
class DisassociateAdminAccountRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class EvaluationResult(ShapeBase):
    """
    Describes the compliance status for the account. An account is considered non-
    compliant if it includes resources that are not protected by the specified
    policy.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "compliance_status",
                "ComplianceStatus",
                TypeInfo(typing.Union[str, PolicyComplianceStatusType]),
            ),
            (
                "violator_count",
                "ViolatorCount",
                TypeInfo(int),
            ),
            (
                "evaluation_limit_exceeded",
                "EvaluationLimitExceeded",
                TypeInfo(bool),
            ),
        ]

    # Describes an AWS account's compliance with the AWS Firewall Manager policy.
    compliance_status: typing.Union[str, "PolicyComplianceStatusType"
                                   ] = dataclasses.field(
                                       default=ShapeBase.NOT_SET,
                                   )

    # Number of resources that are non-compliant with the specified policy. A
    # resource is considered non-compliant if it is not associated with the
    # specified policy.
    violator_count: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Indicates that over 100 resources are non-compliant with the AWS Firewall
    # Manager policy.
    evaluation_limit_exceeded: bool = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class GetAdminAccountRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class GetAdminAccountResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "admin_account",
                "AdminAccount",
                TypeInfo(str),
            ),
            (
                "role_status",
                "RoleStatus",
                TypeInfo(typing.Union[str, AccountRoleStatus]),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The AWS account that is set as the AWS Firewall Manager administrator.
    admin_account: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The status of the AWS account that you set as the AWS Firewall Manager
    # administrator.
    role_status: typing.Union[str, "AccountRoleStatus"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class GetComplianceDetailRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "policy_id",
                "PolicyId",
                TypeInfo(str),
            ),
            (
                "member_account",
                "MemberAccount",
                TypeInfo(str),
            ),
        ]

    # The ID of the policy that you want to get the details for. `PolicyId` is
    # returned by `PutPolicy` and by `ListPolicies`.
    policy_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The AWS account that owns the resources that you want to get the details
    # for.
    member_account: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class GetComplianceDetailResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "policy_compliance_detail",
                "PolicyComplianceDetail",
                TypeInfo(PolicyComplianceDetail),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Information about the resources and the policy that you specified in the
    # `GetComplianceDetail` request.
    policy_compliance_detail: "PolicyComplianceDetail" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class GetNotificationChannelRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class GetNotificationChannelResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "sns_topic_arn",
                "SnsTopicArn",
                TypeInfo(str),
            ),
            (
                "sns_role_name",
                "SnsRoleName",
                TypeInfo(str),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The SNS topic that records AWS Firewall Manager activity.
    sns_topic_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The IAM role that is used by AWS Firewall Manager to record activity to
    # SNS.
    sns_role_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class GetPolicyRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "policy_id",
                "PolicyId",
                TypeInfo(str),
            ),
        ]

    # The ID of the AWS Firewall Manager policy that you want the details for.
    policy_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class GetPolicyResponse(OutputShapeBase):
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
            (
                "policy_arn",
                "PolicyArn",
                TypeInfo(str),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Information about the specified AWS Firewall Manager policy.
    policy: "Policy" = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The Amazon Resource Name (ARN) of the specified policy.
    policy_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class InternalErrorException(ShapeBase):
    """
    The operation failed because of a system problem, even though the request was
    valid. Retry your request.
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
    The parameters of the request were invalid.
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
class InvalidOperationException(ShapeBase):
    """
    The operation failed because there was nothing to do. For example, you might
    have submitted an `AssociateAdminAccount` request, but the account ID that you
    submitted was already set as the AWS Firewall Manager administrator.
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
class InvalidTypeException(ShapeBase):
    """
    The value of the `Type` parameter is invalid.
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
    The operation exceeds a resource limit, for example, the maximum number of
    `policy` objects that you can create for an AWS account. For more information,
    see [Firewall Manager
    Limits](http://docs.aws.amazon.com/waf/latest/developerguide/fms-limits.html) in
    the _AWS WAF Developer Guide_.
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
class ListComplianceStatusRequest(ShapeBase):
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

    # The ID of the AWS Firewall Manager policy that you want the details for.
    policy_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # If you specify a value for `MaxResults` and you have more
    # `PolicyComplianceStatus` objects than the number that you specify for
    # `MaxResults`, AWS Firewall Manager returns a `NextToken` value in the
    # response that allows you to list another group of `PolicyComplianceStatus`
    # objects. For the second and subsequent `ListComplianceStatus` requests,
    # specify the value of `NextToken` from the previous response to get
    # information about another batch of `PolicyComplianceStatus` objects.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Specifies the number of `PolicyComplianceStatus` objects that you want AWS
    # Firewall Manager to return for this request. If you have more
    # `PolicyComplianceStatus` objects than the number that you specify for
    # `MaxResults`, the response includes a `NextToken` value that you can use to
    # get another batch of `PolicyComplianceStatus` objects.
    max_results: int = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ListComplianceStatusResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "policy_compliance_status_list",
                "PolicyComplianceStatusList",
                TypeInfo(typing.List[PolicyComplianceStatus]),
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

    # An array of `PolicyComplianceStatus` objects.
    policy_compliance_status_list: typing.List["PolicyComplianceStatus"
                                              ] = dataclasses.field(
                                                  default=ShapeBase.NOT_SET,
                                              )

    # If you have more `PolicyComplianceStatus` objects than the number that you
    # specified for `MaxResults` in the request, the response includes a
    # `NextToken` value. To list more `PolicyComplianceStatus` objects, submit
    # another `ListComplianceStatus` request, and specify the `NextToken` value
    # from the response in the `NextToken` value in the next request.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ListMemberAccountsRequest(ShapeBase):
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

    # If you specify a value for `MaxResults` and you have more account IDs than
    # the number that you specify for `MaxResults`, AWS Firewall Manager returns
    # a `NextToken` value in the response that allows you to list another group
    # of IDs. For the second and subsequent `ListMemberAccountsRequest` requests,
    # specify the value of `NextToken` from the previous response to get
    # information about another batch of member account IDs.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Specifies the number of member account IDs that you want AWS Firewall
    # Manager to return for this request. If you have more IDs than the number
    # that you specify for `MaxResults`, the response includes a `NextToken`
    # value that you can use to get another batch of member account IDs. The
    # maximum value for `MaxResults` is 100.
    max_results: int = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ListMemberAccountsResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "member_accounts",
                "MemberAccounts",
                TypeInfo(typing.List[str]),
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

    # An array of account IDs.
    member_accounts: typing.List[str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # If you have more member account IDs than the number that you specified for
    # `MaxResults` in the request, the response includes a `NextToken` value. To
    # list more IDs, submit another `ListMemberAccounts` request, and specify the
    # `NextToken` value from the response in the `NextToken` value in the next
    # request.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ListPoliciesRequest(ShapeBase):
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

    # If you specify a value for `MaxResults` and you have more `PolicySummary`
    # objects than the number that you specify for `MaxResults`, AWS Firewall
    # Manager returns a `NextToken` value in the response that allows you to list
    # another group of `PolicySummary` objects. For the second and subsequent
    # `ListPolicies` requests, specify the value of `NextToken` from the previous
    # response to get information about another batch of `PolicySummary` objects.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Specifies the number of `PolicySummary` objects that you want AWS Firewall
    # Manager to return for this request. If you have more `PolicySummary`
    # objects than the number that you specify for `MaxResults`, the response
    # includes a `NextToken` value that you can use to get another batch of
    # `PolicySummary` objects.
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
                "policy_list",
                "PolicyList",
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

    # An array of `PolicySummary` objects.
    policy_list: typing.List["PolicySummary"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # If you have more `PolicySummary` objects than the number that you specified
    # for `MaxResults` in the request, the response includes a `NextToken` value.
    # To list more `PolicySummary` objects, submit another `ListPolicies`
    # request, and specify the `NextToken` value from the response in the
    # `NextToken` value in the next request.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class Policy(ShapeBase):
    """
    An AWS Firewall Manager policy.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "policy_name",
                "PolicyName",
                TypeInfo(str),
            ),
            (
                "security_service_policy_data",
                "SecurityServicePolicyData",
                TypeInfo(SecurityServicePolicyData),
            ),
            (
                "resource_type",
                "ResourceType",
                TypeInfo(str),
            ),
            (
                "exclude_resource_tags",
                "ExcludeResourceTags",
                TypeInfo(bool),
            ),
            (
                "remediation_enabled",
                "RemediationEnabled",
                TypeInfo(bool),
            ),
            (
                "policy_id",
                "PolicyId",
                TypeInfo(str),
            ),
            (
                "policy_update_token",
                "PolicyUpdateToken",
                TypeInfo(str),
            ),
            (
                "resource_tags",
                "ResourceTags",
                TypeInfo(typing.List[ResourceTag]),
            ),
            (
                "include_map",
                "IncludeMap",
                TypeInfo(
                    typing.Dict[typing.Union[str, CustomerPolicyScopeIdType],
                                typing.List[str]]
                ),
            ),
            (
                "exclude_map",
                "ExcludeMap",
                TypeInfo(
                    typing.Dict[typing.Union[str, CustomerPolicyScopeIdType],
                                typing.List[str]]
                ),
            ),
        ]

    # The friendly name of the AWS Firewall Manager policy.
    policy_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Details about the security service that is being used to protect the
    # resources.
    security_service_policy_data: "SecurityServicePolicyData" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The type of resource to protect with the policy, either an Application Load
    # Balancer or a CloudFront distribution. This is in the format shown in [AWS
    # Resource Types
    # Reference](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-
    # template-resource-type-ref.html). Valid values are
    # `AWS::ElasticLoadBalancingV2::LoadBalancer` or
    # `AWS::CloudFront::Distribution`.
    resource_type: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # If set to `True`, resources with the tags that are specified in the
    # `ResourceTag` array are not protected by the policy. If set to `False`, and
    # the `ResourceTag` array is not null, only resources with the specified tags
    # are associated with the policy.
    exclude_resource_tags: bool = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Indicates if the policy should be automatically applied to new resources.
    remediation_enabled: bool = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The ID of the AWS Firewall Manager policy.
    policy_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A unique identifier for each update to the policy. When issuing a
    # `PutPolicy` request, the `PolicyUpdateToken` in the request must match the
    # `PolicyUpdateToken` of the current policy version. To get the
    # `PolicyUpdateToken` of the current policy version, use a `GetPolicy`
    # request.
    policy_update_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # An array of `ResourceTag` objects.
    resource_tags: typing.List["ResourceTag"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Specifies the AWS account IDs to include in the policy. If `IncludeMap` is
    # null, all accounts in the AWS Organization are included in the policy. If
    # `IncludeMap` is not null, only values listed in `IncludeMap` will be
    # included in the policy.

    # The key to the map is `ACCOUNT`. For example, a valid `IncludeMap` would be
    # `{“ACCOUNT” : [“accountID1”, “accountID2”]}`.
    include_map: typing.Dict[typing.Union[str, "CustomerPolicyScopeIdType"],
                             typing.List[str]] = dataclasses.field(
                                 default=ShapeBase.NOT_SET,
                             )

    # Specifies the AWS account IDs to exclude from the policy. The `IncludeMap`
    # values are evaluated first, with all of the appropriate account IDs added
    # to the policy. Then the accounts listed in `ExcludeMap` are removed,
    # resulting in the final list of accounts to add to the policy.

    # The key to the map is `ACCOUNT`. For example, a valid `ExcludeMap` would be
    # `{“ACCOUNT” : [“accountID1”, “accountID2”]}`.
    exclude_map: typing.Dict[typing.Union[str, "CustomerPolicyScopeIdType"],
                             typing.List[str]] = dataclasses.field(
                                 default=ShapeBase.NOT_SET,
                             )


@dataclasses.dataclass
class PolicyComplianceDetail(ShapeBase):
    """
    Describes the non-compliant resources in a member account for a specific AWS
    Firewall Manager policy. A maximum of 100 entries are displayed. If more than
    100 resources are non-compliant, `EvaluationLimitExceeded` is set to `True`.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "policy_owner",
                "PolicyOwner",
                TypeInfo(str),
            ),
            (
                "policy_id",
                "PolicyId",
                TypeInfo(str),
            ),
            (
                "member_account",
                "MemberAccount",
                TypeInfo(str),
            ),
            (
                "violators",
                "Violators",
                TypeInfo(typing.List[ComplianceViolator]),
            ),
            (
                "evaluation_limit_exceeded",
                "EvaluationLimitExceeded",
                TypeInfo(bool),
            ),
            (
                "expired_at",
                "ExpiredAt",
                TypeInfo(datetime.datetime),
            ),
            (
                "issue_info_map",
                "IssueInfoMap",
                TypeInfo(
                    typing.Dict[typing.Union[str, DependentServiceName], str]
                ),
            ),
        ]

    # The AWS account that created the AWS Firewall Manager policy.
    policy_owner: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The ID of the AWS Firewall Manager policy.
    policy_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The AWS account ID.
    member_account: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # An array of resources that are not protected by the policy.
    violators: typing.List["ComplianceViolator"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Indicates if over 100 resources are non-compliant with the AWS Firewall
    # Manager policy.
    evaluation_limit_exceeded: bool = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A time stamp that indicates when the returned information should be
    # considered out-of-date.
    expired_at: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Details about problems with dependent services, such as AWS WAF or AWS
    # Config, that are causing a resource to be non-compliant. The details
    # include the name of the dependent service and the error message recieved
    # indicating the problem with the service.
    issue_info_map: typing.Dict[typing.Union[str, "DependentServiceName"], str
                               ] = dataclasses.field(
                                   default=ShapeBase.NOT_SET,
                               )


@dataclasses.dataclass
class PolicyComplianceStatus(ShapeBase):
    """
    Indicates whether the account is compliant with the specified policy. An account
    is considered non-compliant if it includes resources that are not protected by
    the policy.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "policy_owner",
                "PolicyOwner",
                TypeInfo(str),
            ),
            (
                "policy_id",
                "PolicyId",
                TypeInfo(str),
            ),
            (
                "policy_name",
                "PolicyName",
                TypeInfo(str),
            ),
            (
                "member_account",
                "MemberAccount",
                TypeInfo(str),
            ),
            (
                "evaluation_results",
                "EvaluationResults",
                TypeInfo(typing.List[EvaluationResult]),
            ),
            (
                "last_updated",
                "LastUpdated",
                TypeInfo(datetime.datetime),
            ),
            (
                "issue_info_map",
                "IssueInfoMap",
                TypeInfo(
                    typing.Dict[typing.Union[str, DependentServiceName], str]
                ),
            ),
        ]

    # The AWS account that created the AWS Firewall Manager policy.
    policy_owner: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The ID of the AWS Firewall Manager policy.
    policy_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The friendly name of the AWS Firewall Manager policy.
    policy_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The member account ID.
    member_account: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # An array of `EvaluationResult` objects.
    evaluation_results: typing.List["EvaluationResult"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Time stamp of the last update to the `EvaluationResult` objects.
    last_updated: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Details about problems with dependent services, such as AWS WAF or AWS
    # Config, that are causing a resource to be non-compliant. The details
    # include the name of the dependent service and the error message recieved
    # indicating the problem with the service.
    issue_info_map: typing.Dict[typing.Union[str, "DependentServiceName"], str
                               ] = dataclasses.field(
                                   default=ShapeBase.NOT_SET,
                               )


class PolicyComplianceStatusType(str):
    COMPLIANT = "COMPLIANT"
    NON_COMPLIANT = "NON_COMPLIANT"


@dataclasses.dataclass
class PolicySummary(ShapeBase):
    """
    Details of the AWS Firewall Manager policy.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "policy_arn",
                "PolicyArn",
                TypeInfo(str),
            ),
            (
                "policy_id",
                "PolicyId",
                TypeInfo(str),
            ),
            (
                "policy_name",
                "PolicyName",
                TypeInfo(str),
            ),
            (
                "resource_type",
                "ResourceType",
                TypeInfo(str),
            ),
            (
                "security_service_type",
                "SecurityServiceType",
                TypeInfo(typing.Union[str, SecurityServiceType]),
            ),
            (
                "remediation_enabled",
                "RemediationEnabled",
                TypeInfo(bool),
            ),
        ]

    # The Amazon Resource Name (ARN) of the specified policy.
    policy_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The ID of the specified policy.
    policy_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The friendly name of the specified policy.
    policy_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The type of resource to protect with the policy, either an Application Load
    # Balancer or a CloudFront distribution. This is in the format shown in [AWS
    # Resource Types
    # Reference](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-
    # template-resource-type-ref.html). Valid values are
    # `AWS::ElasticLoadBalancingV2::LoadBalancer` or
    # `AWS::CloudFront::Distribution`.
    resource_type: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The service that the policy is using to protect the resources. This value
    # is `WAF`.
    security_service_type: typing.Union[str, "SecurityServiceType"
                                       ] = dataclasses.field(
                                           default=ShapeBase.NOT_SET,
                                       )

    # Indicates if the policy should be automatically applied to new resources.
    remediation_enabled: bool = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class PutNotificationChannelRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "sns_topic_arn",
                "SnsTopicArn",
                TypeInfo(str),
            ),
            (
                "sns_role_name",
                "SnsRoleName",
                TypeInfo(str),
            ),
        ]

    # The Amazon Resource Name (ARN) of the SNS topic that collects notifications
    # from AWS Firewall Manager.
    sns_topic_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The Amazon Resource Name (ARN) of the IAM role that allows Amazon SNS to
    # record AWS Firewall Manager activity.
    sns_role_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class PutPolicyRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "policy",
                "Policy",
                TypeInfo(Policy),
            ),
        ]

    # The details of the AWS Firewall Manager policy to be created.
    policy: "Policy" = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class PutPolicyResponse(OutputShapeBase):
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
            (
                "policy_arn",
                "PolicyArn",
                TypeInfo(str),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The details of the AWS Firewall Manager policy that was created.
    policy: "Policy" = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The Amazon Resource Name (ARN) of the policy that was created.
    policy_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ResourceNotFoundException(ShapeBase):
    """
    The specified resource was not found.
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
class ResourceTag(ShapeBase):
    """
    The resource tags that AWS Firewall Manager uses to determine if a particular
    resource should be included or excluded from protection by the AWS Firewall
    Manager policy. Tags enable you to categorize your AWS resources in different
    ways, for example, by purpose, owner, or environment. Each tag consists of a key
    and an optional value, both of which you define. Tags are combined with an "OR."
    That is, if you add more than one tag, if any of the tags matches, the resource
    is considered a match for the include or exclude. [Working with Tag
    Editor](https://docs.aws.amazon.com/awsconsolehelpdocs/latest/gsg/tag-
    editor.html).
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

    # The resource tag key.
    key: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The resource tag value.
    value: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class SecurityServicePolicyData(ShapeBase):
    """
    Details about the security service that is being used to protect the resources.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "type",
                "Type",
                TypeInfo(typing.Union[str, SecurityServiceType]),
            ),
            (
                "managed_service_data",
                "ManagedServiceData",
                TypeInfo(str),
            ),
        ]

    # The service that the policy is using to protect the resources. This value
    # is `WAF`.
    type: typing.Union[str, "SecurityServiceType"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Details about the service. This contains `WAF` data in JSON format, as
    # shown in the following example:

    # `ManagedServiceData": "{\"type\": \"WAF\", \"ruleGroups\": [{\"id\":
    # \"12345678-1bcd-9012-efga-0987654321ab\", \"overrideAction\" : {\"type\":
    # \"COUNT\"}}], \"defaultAction\": {\"type\": \"BLOCK\"}}`
    managed_service_data: str = dataclasses.field(default=ShapeBase.NOT_SET, )


class SecurityServiceType(str):
    WAF = "WAF"


class ViolationReason(str):
    WEB_ACL_MISSING_RULE_GROUP = "WEB_ACL_MISSING_RULE_GROUP"
    RESOURCE_MISSING_WEB_ACL = "RESOURCE_MISSING_WEB_ACL"
    RESOURCE_INCORRECT_WEB_ACL = "RESOURCE_INCORRECT_WEB_ACL"
