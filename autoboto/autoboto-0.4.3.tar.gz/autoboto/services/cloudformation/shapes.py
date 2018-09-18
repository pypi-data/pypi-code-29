import datetime
import typing
from autoboto import ShapeBase, OutputShapeBase, TypeInfo
import dataclasses


@dataclasses.dataclass
class AccountGateResult(ShapeBase):
    """
    Structure that contains the results of the account gate function which AWS
    CloudFormation invokes, if present, before proceeding with a stack set operation
    in an account and region.

    For each account and region, AWS CloudFormation lets you specify a Lamdba
    function that encapsulates any requirements that must be met before
    CloudFormation can proceed with a stack set operation in that account and
    region. CloudFormation invokes the function each time a stack set operation is
    requested for that account and region; if the function returns `FAILED`,
    CloudFormation cancels the operation in that account and region, and sets the
    stack set operation result status for that account and region to `FAILED`.

    For more information, see [Configuring a target account
    gate](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/stacksets-
    account-gating.html).
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "status",
                "Status",
                TypeInfo(typing.Union[str, AccountGateStatus]),
            ),
            (
                "status_reason",
                "StatusReason",
                TypeInfo(str),
            ),
        ]

    # The status of the account gate function.

    #   * `SUCCEEDED`: The account gate function has determined that the account and region passes any requirements for a stack set operation to occur. AWS CloudFormation proceeds with the stack operation in that account and region.

    #   * `FAILED`: The account gate function has determined that the account and region does not meet the requirements for a stack set operation to occur. AWS CloudFormation cancels the stack set operation in that account and region, and sets the stack set operation result status for that account and region to `FAILED`.

    #   * `SKIPPED`: AWS CloudFormation has skipped calling the account gate function for this account and region, for one of the following reasons:

    #     * An account gate function has not been specified for the account and region. AWS CloudFormation proceeds with the stack set operation in this account and region.

    #     * The `AWSCloudFormationStackSetExecutionRole` of the stack set adminstration account lacks permissions to invoke the function. AWS CloudFormation proceeds with the stack set operation in this account and region.

    #     * Either no action is necessary, or no action is possible, on the stack. AWS CloudFormation skips the stack set operation in this account and region.
    status: typing.Union[str, "AccountGateStatus"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The reason for the account gate status assigned to this account and region
    # for the stack set operation.
    status_reason: str = dataclasses.field(default=ShapeBase.NOT_SET, )


class AccountGateStatus(str):
    SUCCEEDED = "SUCCEEDED"
    FAILED = "FAILED"
    SKIPPED = "SKIPPED"


@dataclasses.dataclass
class AccountLimit(ShapeBase):
    """
    The AccountLimit data type.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "name",
                "Name",
                TypeInfo(str),
            ),
            (
                "value",
                "Value",
                TypeInfo(int),
            ),
        ]

    # The name of the account limit. Currently, the only account limit is
    # `StackLimit`.
    name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The value that is associated with the account limit name.
    value: int = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class AlreadyExistsException(ShapeBase):
    """
    The resource with the name requested already exists.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class CancelUpdateStackInput(ShapeBase):
    """
    The input for the CancelUpdateStack action.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "stack_name",
                "StackName",
                TypeInfo(str),
            ),
            (
                "client_request_token",
                "ClientRequestToken",
                TypeInfo(str),
            ),
        ]

    # The name or the unique stack ID that is associated with the stack.
    stack_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A unique identifier for this `CancelUpdateStack` request. Specify this
    # token if you plan to retry requests so that AWS CloudFormation knows that
    # you're not attempting to cancel an update on a stack with the same name.
    # You might retry `CancelUpdateStack` requests to ensure that AWS
    # CloudFormation successfully received them.
    client_request_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )


class Capability(str):
    CAPABILITY_IAM = "CAPABILITY_IAM"
    CAPABILITY_NAMED_IAM = "CAPABILITY_NAMED_IAM"


@dataclasses.dataclass
class Change(ShapeBase):
    """
    The `Change` structure describes the changes AWS CloudFormation will perform if
    you execute the change set.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "type",
                "Type",
                TypeInfo(typing.Union[str, ChangeType]),
            ),
            (
                "resource_change",
                "ResourceChange",
                TypeInfo(ResourceChange),
            ),
        ]

    # The type of entity that AWS CloudFormation changes. Currently, the only
    # entity type is `Resource`.
    type: typing.Union[str, "ChangeType"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A `ResourceChange` structure that describes the resource and action that
    # AWS CloudFormation will perform.
    resource_change: "ResourceChange" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


class ChangeAction(str):
    Add = "Add"
    Modify = "Modify"
    Remove = "Remove"


@dataclasses.dataclass
class ChangeSetNotFoundException(ShapeBase):
    """
    The specified change set name or ID doesn't exit. To view valid change sets for
    a stack, use the `ListChangeSets` action.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


class ChangeSetStatus(str):
    CREATE_PENDING = "CREATE_PENDING"
    CREATE_IN_PROGRESS = "CREATE_IN_PROGRESS"
    CREATE_COMPLETE = "CREATE_COMPLETE"
    DELETE_COMPLETE = "DELETE_COMPLETE"
    FAILED = "FAILED"


@dataclasses.dataclass
class ChangeSetSummary(ShapeBase):
    """
    The `ChangeSetSummary` structure describes a change set, its status, and the
    stack with which it's associated.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "stack_id",
                "StackId",
                TypeInfo(str),
            ),
            (
                "stack_name",
                "StackName",
                TypeInfo(str),
            ),
            (
                "change_set_id",
                "ChangeSetId",
                TypeInfo(str),
            ),
            (
                "change_set_name",
                "ChangeSetName",
                TypeInfo(str),
            ),
            (
                "execution_status",
                "ExecutionStatus",
                TypeInfo(typing.Union[str, ExecutionStatus]),
            ),
            (
                "status",
                "Status",
                TypeInfo(typing.Union[str, ChangeSetStatus]),
            ),
            (
                "status_reason",
                "StatusReason",
                TypeInfo(str),
            ),
            (
                "creation_time",
                "CreationTime",
                TypeInfo(datetime.datetime),
            ),
            (
                "description",
                "Description",
                TypeInfo(str),
            ),
        ]

    # The ID of the stack with which the change set is associated.
    stack_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The name of the stack with which the change set is associated.
    stack_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The ID of the change set.
    change_set_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The name of the change set.
    change_set_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # If the change set execution status is `AVAILABLE`, you can execute the
    # change set. If you can’t execute the change set, the status indicates why.
    # For example, a change set might be in an `UNAVAILABLE` state because AWS
    # CloudFormation is still creating it or in an `OBSOLETE` state because the
    # stack was already updated.
    execution_status: typing.Union[str, "ExecutionStatus"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The state of the change set, such as `CREATE_IN_PROGRESS`,
    # `CREATE_COMPLETE`, or `FAILED`.
    status: typing.Union[str, "ChangeSetStatus"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A description of the change set's status. For example, if your change set
    # is in the `FAILED` state, AWS CloudFormation shows the error message.
    status_reason: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The start time when the change set was created, in UTC.
    creation_time: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Descriptive information about the change set.
    description: str = dataclasses.field(default=ShapeBase.NOT_SET, )


class ChangeSetType(str):
    CREATE = "CREATE"
    UPDATE = "UPDATE"


class ChangeSource(str):
    ResourceReference = "ResourceReference"
    ParameterReference = "ParameterReference"
    ResourceAttribute = "ResourceAttribute"
    DirectModification = "DirectModification"
    Automatic = "Automatic"


class ChangeType(str):
    Resource = "Resource"


@dataclasses.dataclass
class ContinueUpdateRollbackInput(ShapeBase):
    """
    The input for the ContinueUpdateRollback action.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "stack_name",
                "StackName",
                TypeInfo(str),
            ),
            (
                "role_arn",
                "RoleARN",
                TypeInfo(str),
            ),
            (
                "resources_to_skip",
                "ResourcesToSkip",
                TypeInfo(typing.List[str]),
            ),
            (
                "client_request_token",
                "ClientRequestToken",
                TypeInfo(str),
            ),
        ]

    # The name or the unique ID of the stack that you want to continue rolling
    # back.

    # Don't specify the name of a nested stack (a stack that was created by using
    # the `AWS::CloudFormation::Stack` resource). Instead, use this operation on
    # the parent stack (the stack that contains the `AWS::CloudFormation::Stack`
    # resource).
    stack_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The Amazon Resource Name (ARN) of an AWS Identity and Access Management
    # (IAM) role that AWS CloudFormation assumes to roll back the stack. AWS
    # CloudFormation uses the role's credentials to make calls on your behalf.
    # AWS CloudFormation always uses this role for all future operations on the
    # stack. As long as users have permission to operate on the stack, AWS
    # CloudFormation uses this role even if the users don't have permission to
    # pass it. Ensure that the role grants least privilege.

    # If you don't specify a value, AWS CloudFormation uses the role that was
    # previously associated with the stack. If no role is available, AWS
    # CloudFormation uses a temporary session that is generated from your user
    # credentials.
    role_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A list of the logical IDs of the resources that AWS CloudFormation skips
    # during the continue update rollback operation. You can specify only
    # resources that are in the `UPDATE_FAILED` state because a rollback failed.
    # You can't specify resources that are in the `UPDATE_FAILED` state for other
    # reasons, for example, because an update was cancelled. To check why a
    # resource update failed, use the DescribeStackResources action, and view the
    # resource status reason.

    # Specify this property to skip rolling back resources that AWS
    # CloudFormation can't successfully roll back. We recommend that you [
    # troubleshoot](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/troubleshooting.html#troubleshooting-
    # errors-update-rollback-failed) resources before skipping them. AWS
    # CloudFormation sets the status of the specified resources to
    # `UPDATE_COMPLETE` and continues to roll back the stack. After the rollback
    # is complete, the state of the skipped resources will be inconsistent with
    # the state of the resources in the stack template. Before performing another
    # stack update, you must update the stack or resources to be consistent with
    # each other. If you don't, subsequent stack updates might fail, and the
    # stack will become unrecoverable.

    # Specify the minimum number of resources required to successfully roll back
    # your stack. For example, a failed resource update might cause dependent
    # resources to fail. In this case, it might not be necessary to skip the
    # dependent resources.

    # To skip resources that are part of nested stacks, use the following format:
    # `NestedStackName.ResourceLogicalID`. If you want to specify the logical ID
    # of a stack resource (`Type: AWS::CloudFormation::Stack`) in the
    # `ResourcesToSkip` list, then its corresponding embedded stack must be in
    # one of the following states: `DELETE_IN_PROGRESS`, `DELETE_COMPLETE`, or
    # `DELETE_FAILED`.

    # Don't confuse a child stack's name with its corresponding logical ID
    # defined in the parent stack. For an example of a continue update rollback
    # operation with nested stacks, see [Using ResourcesToSkip to recover a
    # nested stacks
    # hierarchy](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-
    # cfn-updating-stacks-continueupdaterollback.html#nested-stacks).
    resources_to_skip: typing.List[str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A unique identifier for this `ContinueUpdateRollback` request. Specify this
    # token if you plan to retry requests so that AWS CloudFormation knows that
    # you're not attempting to continue the rollback to a stack with the same
    # name. You might retry `ContinueUpdateRollback` requests to ensure that AWS
    # CloudFormation successfully received them.
    client_request_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ContinueUpdateRollbackOutput(OutputShapeBase):
    """
    The output for a ContinueUpdateRollback action.
    """

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
class CreateChangeSetInput(ShapeBase):
    """
    The input for the CreateChangeSet action.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "stack_name",
                "StackName",
                TypeInfo(str),
            ),
            (
                "change_set_name",
                "ChangeSetName",
                TypeInfo(str),
            ),
            (
                "template_body",
                "TemplateBody",
                TypeInfo(str),
            ),
            (
                "template_url",
                "TemplateURL",
                TypeInfo(str),
            ),
            (
                "use_previous_template",
                "UsePreviousTemplate",
                TypeInfo(bool),
            ),
            (
                "parameters",
                "Parameters",
                TypeInfo(typing.List[Parameter]),
            ),
            (
                "capabilities",
                "Capabilities",
                TypeInfo(typing.List[typing.Union[str, Capability]]),
            ),
            (
                "resource_types",
                "ResourceTypes",
                TypeInfo(typing.List[str]),
            ),
            (
                "role_arn",
                "RoleARN",
                TypeInfo(str),
            ),
            (
                "rollback_configuration",
                "RollbackConfiguration",
                TypeInfo(RollbackConfiguration),
            ),
            (
                "notification_arns",
                "NotificationARNs",
                TypeInfo(typing.List[str]),
            ),
            (
                "tags",
                "Tags",
                TypeInfo(typing.List[Tag]),
            ),
            (
                "client_token",
                "ClientToken",
                TypeInfo(str),
            ),
            (
                "description",
                "Description",
                TypeInfo(str),
            ),
            (
                "change_set_type",
                "ChangeSetType",
                TypeInfo(typing.Union[str, ChangeSetType]),
            ),
        ]

    # The name or the unique ID of the stack for which you are creating a change
    # set. AWS CloudFormation generates the change set by comparing this stack's
    # information with the information that you submit, such as a modified
    # template or different parameter input values.
    stack_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The name of the change set. The name must be unique among all change sets
    # that are associated with the specified stack.

    # A change set name can contain only alphanumeric, case sensitive characters
    # and hyphens. It must start with an alphabetic character and cannot exceed
    # 128 characters.
    change_set_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A structure that contains the body of the revised template, with a minimum
    # length of 1 byte and a maximum length of 51,200 bytes. AWS CloudFormation
    # generates the change set by comparing this template with the template of
    # the stack that you specified.

    # Conditional: You must specify only `TemplateBody` or `TemplateURL`.
    template_body: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The location of the file that contains the revised template. The URL must
    # point to a template (max size: 460,800 bytes) that is located in an S3
    # bucket. AWS CloudFormation generates the change set by comparing this
    # template with the stack that you specified.

    # Conditional: You must specify only `TemplateBody` or `TemplateURL`.
    template_url: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Whether to reuse the template that is associated with the stack to create
    # the change set.
    use_previous_template: bool = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A list of `Parameter` structures that specify input parameters for the
    # change set. For more information, see the
    # [Parameter](http://docs.aws.amazon.com/AWSCloudFormation/latest/APIReference/API_Parameter.html)
    # data type.
    parameters: typing.List["Parameter"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A list of values that you must specify before AWS CloudFormation can update
    # certain stacks. Some stack templates might include resources that can
    # affect permissions in your AWS account, for example, by creating new AWS
    # Identity and Access Management (IAM) users. For those stacks, you must
    # explicitly acknowledge their capabilities by specifying this parameter.

    # The only valid values are `CAPABILITY_IAM` and `CAPABILITY_NAMED_IAM`. The
    # following resources require you to specify this parameter: [
    # AWS::IAM::AccessKey](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-
    # properties-iam-accesskey.html), [
    # AWS::IAM::Group](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-
    # properties-iam-group.html), [
    # AWS::IAM::InstanceProfile](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-
    # resource-iam-instanceprofile.html), [
    # AWS::IAM::Policy](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-
    # properties-iam-policy.html), [
    # AWS::IAM::Role](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-
    # resource-iam-role.html), [
    # AWS::IAM::User](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-
    # properties-iam-user.html), and [
    # AWS::IAM::UserToGroupAddition](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-
    # properties-iam-addusertogroup.html). If your stack template contains these
    # resources, we recommend that you review all permissions associated with
    # them and edit their permissions if necessary.

    # If you have IAM resources, you can specify either capability. If you have
    # IAM resources with custom names, you must specify `CAPABILITY_NAMED_IAM`.
    # If you don't specify this parameter, this action returns an
    # `InsufficientCapabilities` error.

    # For more information, see [Acknowledging IAM Resources in AWS
    # CloudFormation
    # Templates](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-
    # iam-template.html#capabilities).
    capabilities: typing.List[typing.Union[str, "Capability"]
                             ] = dataclasses.field(
                                 default=ShapeBase.NOT_SET,
                             )

    # The template resource types that you have permissions to work with if you
    # execute this change set, such as `AWS::EC2::Instance`, `AWS::EC2::*`, or
    # `Custom::MyCustomInstance`.

    # If the list of resource types doesn't include a resource type that you're
    # updating, the stack update fails. By default, AWS CloudFormation grants
    # permissions to all resource types. AWS Identity and Access Management (IAM)
    # uses this parameter for condition keys in IAM policies for AWS
    # CloudFormation. For more information, see [Controlling Access with AWS
    # Identity and Access
    # Management](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-
    # iam-template.html) in the AWS CloudFormation User Guide.
    resource_types: typing.List[str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The Amazon Resource Name (ARN) of an AWS Identity and Access Management
    # (IAM) role that AWS CloudFormation assumes when executing the change set.
    # AWS CloudFormation uses the role's credentials to make calls on your
    # behalf. AWS CloudFormation uses this role for all future operations on the
    # stack. As long as users have permission to operate on the stack, AWS
    # CloudFormation uses this role even if the users don't have permission to
    # pass it. Ensure that the role grants least privilege.

    # If you don't specify a value, AWS CloudFormation uses the role that was
    # previously associated with the stack. If no role is available, AWS
    # CloudFormation uses a temporary session that is generated from your user
    # credentials.
    role_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The rollback triggers for AWS CloudFormation to monitor during stack
    # creation and updating operations, and for the specified monitoring period
    # afterwards.
    rollback_configuration: "RollbackConfiguration" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The Amazon Resource Names (ARNs) of Amazon Simple Notification Service
    # (Amazon SNS) topics that AWS CloudFormation associates with the stack. To
    # remove all associated notification topics, specify an empty list.
    notification_arns: typing.List[str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Key-value pairs to associate with this stack. AWS CloudFormation also
    # propagates these tags to resources in the stack. You can specify a maximum
    # of 50 tags.
    tags: typing.List["Tag"] = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A unique identifier for this `CreateChangeSet` request. Specify this token
    # if you plan to retry requests so that AWS CloudFormation knows that you're
    # not attempting to create another change set with the same name. You might
    # retry `CreateChangeSet` requests to ensure that AWS CloudFormation
    # successfully received them.
    client_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A description to help you identify this change set.
    description: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The type of change set operation. To create a change set for a new stack,
    # specify `CREATE`. To create a change set for an existing stack, specify
    # `UPDATE`.

    # If you create a change set for a new stack, AWS Cloudformation creates a
    # stack with a unique stack ID, but no template or resources. The stack will
    # be in the [ `REVIEW_IN_PROGRESS`
    # ](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-
    # describing-stacks.html#d0e11995) state until you execute the change set.

    # By default, AWS CloudFormation specifies `UPDATE`. You can't use the
    # `UPDATE` type to create a change set for a new stack or the `CREATE` type
    # to create a change set for an existing stack.
    change_set_type: typing.Union[str, "ChangeSetType"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class CreateChangeSetOutput(OutputShapeBase):
    """
    The output for the CreateChangeSet action.
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
                "id",
                "Id",
                TypeInfo(str),
            ),
            (
                "stack_id",
                "StackId",
                TypeInfo(str),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The Amazon Resource Name (ARN) of the change set.
    id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The unique ID of the stack.
    stack_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class CreateStackInput(ShapeBase):
    """
    The input for CreateStack action.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "stack_name",
                "StackName",
                TypeInfo(str),
            ),
            (
                "template_body",
                "TemplateBody",
                TypeInfo(str),
            ),
            (
                "template_url",
                "TemplateURL",
                TypeInfo(str),
            ),
            (
                "parameters",
                "Parameters",
                TypeInfo(typing.List[Parameter]),
            ),
            (
                "disable_rollback",
                "DisableRollback",
                TypeInfo(bool),
            ),
            (
                "rollback_configuration",
                "RollbackConfiguration",
                TypeInfo(RollbackConfiguration),
            ),
            (
                "timeout_in_minutes",
                "TimeoutInMinutes",
                TypeInfo(int),
            ),
            (
                "notification_arns",
                "NotificationARNs",
                TypeInfo(typing.List[str]),
            ),
            (
                "capabilities",
                "Capabilities",
                TypeInfo(typing.List[typing.Union[str, Capability]]),
            ),
            (
                "resource_types",
                "ResourceTypes",
                TypeInfo(typing.List[str]),
            ),
            (
                "role_arn",
                "RoleARN",
                TypeInfo(str),
            ),
            (
                "on_failure",
                "OnFailure",
                TypeInfo(typing.Union[str, OnFailure]),
            ),
            (
                "stack_policy_body",
                "StackPolicyBody",
                TypeInfo(str),
            ),
            (
                "stack_policy_url",
                "StackPolicyURL",
                TypeInfo(str),
            ),
            (
                "tags",
                "Tags",
                TypeInfo(typing.List[Tag]),
            ),
            (
                "client_request_token",
                "ClientRequestToken",
                TypeInfo(str),
            ),
            (
                "enable_termination_protection",
                "EnableTerminationProtection",
                TypeInfo(bool),
            ),
        ]

    # The name that is associated with the stack. The name must be unique in the
    # region in which you are creating the stack.

    # A stack name can contain only alphanumeric characters (case sensitive) and
    # hyphens. It must start with an alphabetic character and cannot be longer
    # than 128 characters.
    stack_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Structure containing the template body with a minimum length of 1 byte and
    # a maximum length of 51,200 bytes. For more information, go to [Template
    # Anatomy](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/template-
    # anatomy.html) in the AWS CloudFormation User Guide.

    # Conditional: You must specify either the `TemplateBody` or the
    # `TemplateURL` parameter, but not both.
    template_body: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Location of file containing the template body. The URL must point to a
    # template (max size: 460,800 bytes) that is located in an Amazon S3 bucket.
    # For more information, go to the [Template
    # Anatomy](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/template-
    # anatomy.html) in the AWS CloudFormation User Guide.

    # Conditional: You must specify either the `TemplateBody` or the
    # `TemplateURL` parameter, but not both.
    template_url: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A list of `Parameter` structures that specify input parameters for the
    # stack. For more information, see the
    # [Parameter](http://docs.aws.amazon.com/AWSCloudFormation/latest/APIReference/API_Parameter.html)
    # data type.
    parameters: typing.List["Parameter"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Set to `true` to disable rollback of the stack if stack creation failed.
    # You can specify either `DisableRollback` or `OnFailure`, but not both.

    # Default: `false`
    disable_rollback: bool = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The rollback triggers for AWS CloudFormation to monitor during stack
    # creation and updating operations, and for the specified monitoring period
    # afterwards.
    rollback_configuration: "RollbackConfiguration" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The amount of time that can pass before the stack status becomes
    # CREATE_FAILED; if `DisableRollback` is not set or is set to `false`, the
    # stack will be rolled back.
    timeout_in_minutes: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The Simple Notification Service (SNS) topic ARNs to publish stack related
    # events. You can find your SNS topic ARNs using the SNS console or your
    # Command Line Interface (CLI).
    notification_arns: typing.List[str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A list of values that you must specify before AWS CloudFormation can create
    # certain stacks. Some stack templates might include resources that can
    # affect permissions in your AWS account, for example, by creating new AWS
    # Identity and Access Management (IAM) users. For those stacks, you must
    # explicitly acknowledge their capabilities by specifying this parameter.

    # The only valid values are `CAPABILITY_IAM` and `CAPABILITY_NAMED_IAM`. The
    # following resources require you to specify this parameter: [
    # AWS::IAM::AccessKey](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-
    # properties-iam-accesskey.html), [
    # AWS::IAM::Group](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-
    # properties-iam-group.html), [
    # AWS::IAM::InstanceProfile](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-
    # resource-iam-instanceprofile.html), [
    # AWS::IAM::Policy](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-
    # properties-iam-policy.html), [
    # AWS::IAM::Role](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-
    # resource-iam-role.html), [
    # AWS::IAM::User](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-
    # properties-iam-user.html), and [
    # AWS::IAM::UserToGroupAddition](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-
    # properties-iam-addusertogroup.html). If your stack template contains these
    # resources, we recommend that you review all permissions associated with
    # them and edit their permissions if necessary.

    # If you have IAM resources, you can specify either capability. If you have
    # IAM resources with custom names, you must specify `CAPABILITY_NAMED_IAM`.
    # If you don't specify this parameter, this action returns an
    # `InsufficientCapabilities` error.

    # For more information, see [Acknowledging IAM Resources in AWS
    # CloudFormation
    # Templates](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-
    # iam-template.html#capabilities).
    capabilities: typing.List[typing.Union[str, "Capability"]
                             ] = dataclasses.field(
                                 default=ShapeBase.NOT_SET,
                             )

    # The template resource types that you have permissions to work with for this
    # create stack action, such as `AWS::EC2::Instance`, `AWS::EC2::*`, or
    # `Custom::MyCustomInstance`. Use the following syntax to describe template
    # resource types: `AWS::*` (for all AWS resource), `Custom::*` (for all
    # custom resources), `Custom:: _logical_ID_ ` (for a specific custom
    # resource), `AWS:: _service_name_ ::*` (for all resources of a particular
    # AWS service), and `AWS:: _service_name_ :: _resource_logical_ID_ ` (for a
    # specific AWS resource).

    # If the list of resource types doesn't include a resource that you're
    # creating, the stack creation fails. By default, AWS CloudFormation grants
    # permissions to all resource types. AWS Identity and Access Management (IAM)
    # uses this parameter for AWS CloudFormation-specific condition keys in IAM
    # policies. For more information, see [Controlling Access with AWS Identity
    # and Access
    # Management](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-
    # iam-template.html).
    resource_types: typing.List[str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The Amazon Resource Name (ARN) of an AWS Identity and Access Management
    # (IAM) role that AWS CloudFormation assumes to create the stack. AWS
    # CloudFormation uses the role's credentials to make calls on your behalf.
    # AWS CloudFormation always uses this role for all future operations on the
    # stack. As long as users have permission to operate on the stack, AWS
    # CloudFormation uses this role even if the users don't have permission to
    # pass it. Ensure that the role grants least privilege.

    # If you don't specify a value, AWS CloudFormation uses the role that was
    # previously associated with the stack. If no role is available, AWS
    # CloudFormation uses a temporary session that is generated from your user
    # credentials.
    role_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Determines what action will be taken if stack creation fails. This must be
    # one of: DO_NOTHING, ROLLBACK, or DELETE. You can specify either `OnFailure`
    # or `DisableRollback`, but not both.

    # Default: `ROLLBACK`
    on_failure: typing.Union[str, "OnFailure"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Structure containing the stack policy body. For more information, go to [
    # Prevent Updates to Stack
    # Resources](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/protect-
    # stack-resources.html) in the _AWS CloudFormation User Guide_. You can
    # specify either the `StackPolicyBody` or the `StackPolicyURL` parameter, but
    # not both.
    stack_policy_body: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Location of a file containing the stack policy. The URL must point to a
    # policy (maximum size: 16 KB) located in an S3 bucket in the same region as
    # the stack. You can specify either the `StackPolicyBody` or the
    # `StackPolicyURL` parameter, but not both.
    stack_policy_url: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Key-value pairs to associate with this stack. AWS CloudFormation also
    # propagates these tags to the resources created in the stack. A maximum
    # number of 50 tags can be specified.
    tags: typing.List["Tag"] = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A unique identifier for this `CreateStack` request. Specify this token if
    # you plan to retry requests so that AWS CloudFormation knows that you're not
    # attempting to create a stack with the same name. You might retry
    # `CreateStack` requests to ensure that AWS CloudFormation successfully
    # received them.

    # All events triggered by a given stack operation are assigned the same
    # client request token, which you can use to track operations. For example,
    # if you execute a `CreateStack` operation with the token `token1`, then all
    # the `StackEvents` generated by that operation will have
    # `ClientRequestToken` set as `token1`.

    # In the console, stack operations display the client request token on the
    # Events tab. Stack operations that are initiated from the console use the
    # token format _Console-StackOperation-ID_ , which helps you easily identify
    # the stack operation . For example, if you create a stack using the console,
    # each stack event would be assigned the same token in the following format:
    # `Console-CreateStack-7f59c3cf-00d2-40c7-b2ff-e75db0987002`.
    client_request_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Whether to enable termination protection on the specified stack. If a user
    # attempts to delete a stack with termination protection enabled, the
    # operation fails and the stack remains unchanged. For more information, see
    # [Protecting a Stack From Being
    # Deleted](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-
    # cfn-protect-stacks.html) in the _AWS CloudFormation User Guide_.
    # Termination protection is disabled on stacks by default.

    # For [nested
    # stacks](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-
    # cfn-nested-stacks.html), termination protection is set on the root stack
    # and cannot be changed directly on the nested stack.
    enable_termination_protection: bool = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class CreateStackInstancesInput(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "stack_set_name",
                "StackSetName",
                TypeInfo(str),
            ),
            (
                "accounts",
                "Accounts",
                TypeInfo(typing.List[str]),
            ),
            (
                "regions",
                "Regions",
                TypeInfo(typing.List[str]),
            ),
            (
                "parameter_overrides",
                "ParameterOverrides",
                TypeInfo(typing.List[Parameter]),
            ),
            (
                "operation_preferences",
                "OperationPreferences",
                TypeInfo(StackSetOperationPreferences),
            ),
            (
                "operation_id",
                "OperationId",
                TypeInfo(str),
            ),
        ]

    # The name or unique ID of the stack set that you want to create stack
    # instances from.
    stack_set_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The names of one or more AWS accounts that you want to create stack
    # instances in the specified region(s) for.
    accounts: typing.List[str] = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The names of one or more regions where you want to create stack instances
    # using the specified AWS account(s).
    regions: typing.List[str] = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A list of stack set parameters whose values you want to override in the
    # selected stack instances.

    # Any overridden parameter values will be applied to all stack instances in
    # the specified accounts and regions. When specifying parameters and their
    # values, be aware of how AWS CloudFormation sets parameter values during
    # stack instance operations:

    #   * To override the current value for a parameter, include the parameter and specify its value.

    #   * To leave a parameter set to its present value, you can do one of the following:

    #     * Do not include the parameter in the list.

    #     * Include the parameter and specify `UsePreviousValue` as `true`. (You cannot specify both a value and set `UsePreviousValue` to `true`.)

    #   * To set all overridden parameter back to the values specified in the stack set, specify a parameter list but do not include any parameters.

    #   * To leave all parameters set to their present values, do not specify this property at all.

    # During stack set updates, any parameter values overridden for a stack
    # instance are not updated, but retain their overridden value.

    # You can only override the parameter _values_ that are specified in the
    # stack set; to add or delete a parameter itself, use
    # [UpdateStackSet](http://docs.aws.amazon.com/AWSCloudFormation/latest/APIReference/API_UpdateStackSet.html)
    # to update the stack set template.
    parameter_overrides: typing.List["Parameter"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Preferences for how AWS CloudFormation performs this stack set operation.
    operation_preferences: "StackSetOperationPreferences" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The unique identifier for this stack set operation.

    # The operation ID also functions as an idempotency token, to ensure that AWS
    # CloudFormation performs the stack set operation only once, even if you
    # retry the request multiple times. You might retry stack set operation
    # requests to ensure that AWS CloudFormation successfully received them.

    # If you don't specify an operation ID, the SDK generates one automatically.

    # Repeating this stack set operation with a new operation ID retries all
    # stack instances whose status is `OUTDATED`.
    operation_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class CreateStackInstancesOutput(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "operation_id",
                "OperationId",
                TypeInfo(str),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The unique identifier for this stack set operation.
    operation_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class CreateStackOutput(OutputShapeBase):
    """
    The output for a CreateStack action.
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
                "stack_id",
                "StackId",
                TypeInfo(str),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Unique identifier of the stack.
    stack_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class CreateStackSetInput(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "stack_set_name",
                "StackSetName",
                TypeInfo(str),
            ),
            (
                "description",
                "Description",
                TypeInfo(str),
            ),
            (
                "template_body",
                "TemplateBody",
                TypeInfo(str),
            ),
            (
                "template_url",
                "TemplateURL",
                TypeInfo(str),
            ),
            (
                "parameters",
                "Parameters",
                TypeInfo(typing.List[Parameter]),
            ),
            (
                "capabilities",
                "Capabilities",
                TypeInfo(typing.List[typing.Union[str, Capability]]),
            ),
            (
                "tags",
                "Tags",
                TypeInfo(typing.List[Tag]),
            ),
            (
                "administration_role_arn",
                "AdministrationRoleARN",
                TypeInfo(str),
            ),
            (
                "execution_role_name",
                "ExecutionRoleName",
                TypeInfo(str),
            ),
            (
                "client_request_token",
                "ClientRequestToken",
                TypeInfo(str),
            ),
        ]

    # The name to associate with the stack set. The name must be unique in the
    # region where you create your stack set.

    # A stack name can contain only alphanumeric characters (case-sensitive) and
    # hyphens. It must start with an alphabetic character and can't be longer
    # than 128 characters.
    stack_set_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A description of the stack set. You can use the description to identify the
    # stack set's purpose or other important information.
    description: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The structure that contains the template body, with a minimum length of 1
    # byte and a maximum length of 51,200 bytes. For more information, see
    # [Template
    # Anatomy](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/template-
    # anatomy.html) in the AWS CloudFormation User Guide.

    # Conditional: You must specify either the TemplateBody or the TemplateURL
    # parameter, but not both.
    template_body: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The location of the file that contains the template body. The URL must
    # point to a template (maximum size: 460,800 bytes) that's located in an
    # Amazon S3 bucket. For more information, see [Template
    # Anatomy](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/template-
    # anatomy.html) in the AWS CloudFormation User Guide.

    # Conditional: You must specify either the TemplateBody or the TemplateURL
    # parameter, but not both.
    template_url: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The input parameters for the stack set template.
    parameters: typing.List["Parameter"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A list of values that you must specify before AWS CloudFormation can create
    # certain stack sets. Some stack set templates might include resources that
    # can affect permissions in your AWS account—for example, by creating new AWS
    # Identity and Access Management (IAM) users. For those stack sets, you must
    # explicitly acknowledge their capabilities by specifying this parameter.

    # The only valid values are CAPABILITY_IAM and CAPABILITY_NAMED_IAM. The
    # following resources require you to specify this parameter:

    #   * AWS::IAM::AccessKey

    #   * AWS::IAM::Group

    #   * AWS::IAM::InstanceProfile

    #   * AWS::IAM::Policy

    #   * AWS::IAM::Role

    #   * AWS::IAM::User

    #   * AWS::IAM::UserToGroupAddition

    # If your stack template contains these resources, we recommend that you
    # review all permissions that are associated with them and edit their
    # permissions if necessary.

    # If you have IAM resources, you can specify either capability. If you have
    # IAM resources with custom names, you must specify CAPABILITY_NAMED_IAM. If
    # you don't specify this parameter, this action returns an
    # `InsufficientCapabilities` error.

    # For more information, see [Acknowledging IAM Resources in AWS
    # CloudFormation
    # Templates.](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-
    # iam-template.html#capabilities)
    capabilities: typing.List[typing.Union[str, "Capability"]
                             ] = dataclasses.field(
                                 default=ShapeBase.NOT_SET,
                             )

    # The key-value pairs to associate with this stack set and the stacks created
    # from it. AWS CloudFormation also propagates these tags to supported
    # resources that are created in the stacks. A maximum number of 50 tags can
    # be specified.

    # If you specify tags as part of a `CreateStackSet` action, AWS
    # CloudFormation checks to see if you have the required IAM permission to tag
    # resources. If you don't, the entire `CreateStackSet` action fails with an
    # `access denied` error, and the stack set is not created.
    tags: typing.List["Tag"] = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The Amazon Resource Number (ARN) of the IAM role to use to create this
    # stack set.

    # Specify an IAM role only if you are using customized administrator roles to
    # control which users or groups can manage specific stack sets within the
    # same administrator account. For more information, see [Prerequisites:
    # Granting Permissions for Stack Set
    # Operations](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/stacksets-
    # prereqs.html) in the _AWS CloudFormation User Guide_.
    administration_role_arn: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The name of the IAM execution role to use to create the stack set. If you
    # do not specify an execution role, AWS CloudFormation uses the
    # `AWSCloudFormationStackSetExecutionRole` role for the stack set operation.

    # Specify an IAM role only if you are using customized execution roles to
    # control which stack resources users and groups can include in their stack
    # sets.
    execution_role_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A unique identifier for this `CreateStackSet` request. Specify this token
    # if you plan to retry requests so that AWS CloudFormation knows that you're
    # not attempting to create another stack set with the same name. You might
    # retry `CreateStackSet` requests to ensure that AWS CloudFormation
    # successfully received them.

    # If you don't specify an operation ID, the SDK generates one automatically.
    client_request_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class CreateStackSetOutput(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "stack_set_id",
                "StackSetId",
                TypeInfo(str),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The ID of the stack set that you're creating.
    stack_set_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class CreatedButModifiedException(ShapeBase):
    """
    The specified resource exists, but has been changed.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class DeleteChangeSetInput(ShapeBase):
    """
    The input for the DeleteChangeSet action.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "change_set_name",
                "ChangeSetName",
                TypeInfo(str),
            ),
            (
                "stack_name",
                "StackName",
                TypeInfo(str),
            ),
        ]

    # The name or Amazon Resource Name (ARN) of the change set that you want to
    # delete.
    change_set_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # If you specified the name of a change set to delete, specify the stack name
    # or ID (ARN) that is associated with it.
    stack_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DeleteChangeSetOutput(OutputShapeBase):
    """
    The output for the DeleteChangeSet action.
    """

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
class DeleteStackInput(ShapeBase):
    """
    The input for DeleteStack action.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "stack_name",
                "StackName",
                TypeInfo(str),
            ),
            (
                "retain_resources",
                "RetainResources",
                TypeInfo(typing.List[str]),
            ),
            (
                "role_arn",
                "RoleARN",
                TypeInfo(str),
            ),
            (
                "client_request_token",
                "ClientRequestToken",
                TypeInfo(str),
            ),
        ]

    # The name or the unique stack ID that is associated with the stack.
    stack_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # For stacks in the `DELETE_FAILED` state, a list of resource logical IDs
    # that are associated with the resources you want to retain. During deletion,
    # AWS CloudFormation deletes the stack but does not delete the retained
    # resources.

    # Retaining resources is useful when you cannot delete a resource, such as a
    # non-empty S3 bucket, but you want to delete the stack.
    retain_resources: typing.List[str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The Amazon Resource Name (ARN) of an AWS Identity and Access Management
    # (IAM) role that AWS CloudFormation assumes to delete the stack. AWS
    # CloudFormation uses the role's credentials to make calls on your behalf.

    # If you don't specify a value, AWS CloudFormation uses the role that was
    # previously associated with the stack. If no role is available, AWS
    # CloudFormation uses a temporary session that is generated from your user
    # credentials.
    role_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A unique identifier for this `DeleteStack` request. Specify this token if
    # you plan to retry requests so that AWS CloudFormation knows that you're not
    # attempting to delete a stack with the same name. You might retry
    # `DeleteStack` requests to ensure that AWS CloudFormation successfully
    # received them.

    # All events triggered by a given stack operation are assigned the same
    # client request token, which you can use to track operations. For example,
    # if you execute a `CreateStack` operation with the token `token1`, then all
    # the `StackEvents` generated by that operation will have
    # `ClientRequestToken` set as `token1`.

    # In the console, stack operations display the client request token on the
    # Events tab. Stack operations that are initiated from the console use the
    # token format _Console-StackOperation-ID_ , which helps you easily identify
    # the stack operation . For example, if you create a stack using the console,
    # each stack event would be assigned the same token in the following format:
    # `Console-CreateStack-7f59c3cf-00d2-40c7-b2ff-e75db0987002`.
    client_request_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DeleteStackInstancesInput(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "stack_set_name",
                "StackSetName",
                TypeInfo(str),
            ),
            (
                "accounts",
                "Accounts",
                TypeInfo(typing.List[str]),
            ),
            (
                "regions",
                "Regions",
                TypeInfo(typing.List[str]),
            ),
            (
                "retain_stacks",
                "RetainStacks",
                TypeInfo(bool),
            ),
            (
                "operation_preferences",
                "OperationPreferences",
                TypeInfo(StackSetOperationPreferences),
            ),
            (
                "operation_id",
                "OperationId",
                TypeInfo(str),
            ),
        ]

    # The name or unique ID of the stack set that you want to delete stack
    # instances for.
    stack_set_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The names of the AWS accounts that you want to delete stack instances for.
    accounts: typing.List[str] = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The regions where you want to delete stack set instances.
    regions: typing.List[str] = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Removes the stack instances from the specified stack set, but doesn't
    # delete the stacks. You can't reassociate a retained stack or add an
    # existing, saved stack to a new stack set.

    # For more information, see [Stack set operation
    # options](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/stacksets-
    # concepts.html#stackset-ops-options).
    retain_stacks: bool = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Preferences for how AWS CloudFormation performs this stack set operation.
    operation_preferences: "StackSetOperationPreferences" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The unique identifier for this stack set operation.

    # If you don't specify an operation ID, the SDK generates one automatically.

    # The operation ID also functions as an idempotency token, to ensure that AWS
    # CloudFormation performs the stack set operation only once, even if you
    # retry the request multiple times. You can retry stack set operation
    # requests to ensure that AWS CloudFormation successfully received them.

    # Repeating this stack set operation with a new operation ID retries all
    # stack instances whose status is `OUTDATED`.
    operation_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DeleteStackInstancesOutput(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "operation_id",
                "OperationId",
                TypeInfo(str),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The unique identifier for this stack set operation.
    operation_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DeleteStackSetInput(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "stack_set_name",
                "StackSetName",
                TypeInfo(str),
            ),
        ]

    # The name or unique ID of the stack set that you're deleting. You can obtain
    # this value by running ListStackSets.
    stack_set_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DeleteStackSetOutput(OutputShapeBase):
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
class DescribeAccountLimitsInput(ShapeBase):
    """
    The input for the DescribeAccountLimits action.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "next_token",
                "NextToken",
                TypeInfo(str),
            ),
        ]

    # A string that identifies the next page of limits that you want to retrieve.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DescribeAccountLimitsOutput(OutputShapeBase):
    """
    The output for the DescribeAccountLimits action.
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
                "account_limits",
                "AccountLimits",
                TypeInfo(typing.List[AccountLimit]),
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

    # An account limit structure that contain a list of AWS CloudFormation
    # account limits and their values.
    account_limits: typing.List["AccountLimit"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # If the output exceeds 1 MB in size, a string that identifies the next page
    # of limits. If no additional page exists, this value is null.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DescribeChangeSetInput(ShapeBase):
    """
    The input for the DescribeChangeSet action.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "change_set_name",
                "ChangeSetName",
                TypeInfo(str),
            ),
            (
                "stack_name",
                "StackName",
                TypeInfo(str),
            ),
            (
                "next_token",
                "NextToken",
                TypeInfo(str),
            ),
        ]

    # The name or Amazon Resource Name (ARN) of the change set that you want to
    # describe.
    change_set_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # If you specified the name of a change set, specify the stack name or ID
    # (ARN) of the change set you want to describe.
    stack_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A string (provided by the DescribeChangeSet response output) that
    # identifies the next page of information that you want to retrieve.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DescribeChangeSetOutput(OutputShapeBase):
    """
    The output for the DescribeChangeSet action.
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
                "change_set_name",
                "ChangeSetName",
                TypeInfo(str),
            ),
            (
                "change_set_id",
                "ChangeSetId",
                TypeInfo(str),
            ),
            (
                "stack_id",
                "StackId",
                TypeInfo(str),
            ),
            (
                "stack_name",
                "StackName",
                TypeInfo(str),
            ),
            (
                "description",
                "Description",
                TypeInfo(str),
            ),
            (
                "parameters",
                "Parameters",
                TypeInfo(typing.List[Parameter]),
            ),
            (
                "creation_time",
                "CreationTime",
                TypeInfo(datetime.datetime),
            ),
            (
                "execution_status",
                "ExecutionStatus",
                TypeInfo(typing.Union[str, ExecutionStatus]),
            ),
            (
                "status",
                "Status",
                TypeInfo(typing.Union[str, ChangeSetStatus]),
            ),
            (
                "status_reason",
                "StatusReason",
                TypeInfo(str),
            ),
            (
                "notification_arns",
                "NotificationARNs",
                TypeInfo(typing.List[str]),
            ),
            (
                "rollback_configuration",
                "RollbackConfiguration",
                TypeInfo(RollbackConfiguration),
            ),
            (
                "capabilities",
                "Capabilities",
                TypeInfo(typing.List[typing.Union[str, Capability]]),
            ),
            (
                "tags",
                "Tags",
                TypeInfo(typing.List[Tag]),
            ),
            (
                "changes",
                "Changes",
                TypeInfo(typing.List[Change]),
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

    # The name of the change set.
    change_set_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The ARN of the change set.
    change_set_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The ARN of the stack that is associated with the change set.
    stack_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The name of the stack that is associated with the change set.
    stack_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Information about the change set.
    description: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A list of `Parameter` structures that describes the input parameters and
    # their values used to create the change set. For more information, see the
    # [Parameter](http://docs.aws.amazon.com/AWSCloudFormation/latest/APIReference/API_Parameter.html)
    # data type.
    parameters: typing.List["Parameter"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The start time when the change set was created, in UTC.
    creation_time: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # If the change set execution status is `AVAILABLE`, you can execute the
    # change set. If you can’t execute the change set, the status indicates why.
    # For example, a change set might be in an `UNAVAILABLE` state because AWS
    # CloudFormation is still creating it or in an `OBSOLETE` state because the
    # stack was already updated.
    execution_status: typing.Union[str, "ExecutionStatus"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The current status of the change set, such as `CREATE_IN_PROGRESS`,
    # `CREATE_COMPLETE`, or `FAILED`.
    status: typing.Union[str, "ChangeSetStatus"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A description of the change set's status. For example, if your attempt to
    # create a change set failed, AWS CloudFormation shows the error message.
    status_reason: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The ARNs of the Amazon Simple Notification Service (Amazon SNS) topics that
    # will be associated with the stack if you execute the change set.
    notification_arns: typing.List[str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The rollback triggers for AWS CloudFormation to monitor during stack
    # creation and updating operations, and for the specified monitoring period
    # afterwards.
    rollback_configuration: "RollbackConfiguration" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # If you execute the change set, the list of capabilities that were
    # explicitly acknowledged when the change set was created.
    capabilities: typing.List[typing.Union[str, "Capability"]
                             ] = dataclasses.field(
                                 default=ShapeBase.NOT_SET,
                             )

    # If you execute the change set, the tags that will be associated with the
    # stack.
    tags: typing.List["Tag"] = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A list of `Change` structures that describes the resources AWS
    # CloudFormation changes if you execute the change set.
    changes: typing.List["Change"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # If the output exceeds 1 MB, a string that identifies the next page of
    # changes. If there is no additional page, this value is null.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DescribeStackEventsInput(ShapeBase):
    """
    The input for DescribeStackEvents action.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "stack_name",
                "StackName",
                TypeInfo(str),
            ),
            (
                "next_token",
                "NextToken",
                TypeInfo(str),
            ),
        ]

    # The name or the unique stack ID that is associated with the stack, which
    # are not always interchangeable:

    #   * Running stacks: You can specify either the stack's name or its unique stack ID.

    #   * Deleted stacks: You must specify the unique stack ID.

    # Default: There is no default value.
    stack_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A string that identifies the next page of events that you want to retrieve.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DescribeStackEventsOutput(OutputShapeBase):
    """
    The output for a DescribeStackEvents action.
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
                "stack_events",
                "StackEvents",
                TypeInfo(typing.List[StackEvent]),
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

    # A list of `StackEvents` structures.
    stack_events: typing.List["StackEvent"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # If the output exceeds 1 MB in size, a string that identifies the next page
    # of events. If no additional page exists, this value is null.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    def paginate(self,
                ) -> typing.Generator["DescribeStackEventsOutput", None, None]:
        yield from super()._paginate()


@dataclasses.dataclass
class DescribeStackInstanceInput(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "stack_set_name",
                "StackSetName",
                TypeInfo(str),
            ),
            (
                "stack_instance_account",
                "StackInstanceAccount",
                TypeInfo(str),
            ),
            (
                "stack_instance_region",
                "StackInstanceRegion",
                TypeInfo(str),
            ),
        ]

    # The name or the unique stack ID of the stack set that you want to get stack
    # instance information for.
    stack_set_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The ID of an AWS account that's associated with this stack instance.
    stack_instance_account: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The name of a region that's associated with this stack instance.
    stack_instance_region: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DescribeStackInstanceOutput(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "stack_instance",
                "StackInstance",
                TypeInfo(StackInstance),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The stack instance that matches the specified request parameters.
    stack_instance: "StackInstance" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class DescribeStackResourceInput(ShapeBase):
    """
    The input for DescribeStackResource action.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "stack_name",
                "StackName",
                TypeInfo(str),
            ),
            (
                "logical_resource_id",
                "LogicalResourceId",
                TypeInfo(str),
            ),
        ]

    # The name or the unique stack ID that is associated with the stack, which
    # are not always interchangeable:

    #   * Running stacks: You can specify either the stack's name or its unique stack ID.

    #   * Deleted stacks: You must specify the unique stack ID.

    # Default: There is no default value.
    stack_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The logical name of the resource as specified in the template.

    # Default: There is no default value.
    logical_resource_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DescribeStackResourceOutput(OutputShapeBase):
    """
    The output for a DescribeStackResource action.
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
                "stack_resource_detail",
                "StackResourceDetail",
                TypeInfo(StackResourceDetail),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A `StackResourceDetail` structure containing the description of the
    # specified resource in the specified stack.
    stack_resource_detail: "StackResourceDetail" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class DescribeStackResourcesInput(ShapeBase):
    """
    The input for DescribeStackResources action.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "stack_name",
                "StackName",
                TypeInfo(str),
            ),
            (
                "logical_resource_id",
                "LogicalResourceId",
                TypeInfo(str),
            ),
            (
                "physical_resource_id",
                "PhysicalResourceId",
                TypeInfo(str),
            ),
        ]

    # The name or the unique stack ID that is associated with the stack, which
    # are not always interchangeable:

    #   * Running stacks: You can specify either the stack's name or its unique stack ID.

    #   * Deleted stacks: You must specify the unique stack ID.

    # Default: There is no default value.

    # Required: Conditional. If you do not specify `StackName`, you must specify
    # `PhysicalResourceId`.
    stack_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The logical name of the resource as specified in the template.

    # Default: There is no default value.
    logical_resource_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The name or unique identifier that corresponds to a physical instance ID of
    # a resource supported by AWS CloudFormation.

    # For example, for an Amazon Elastic Compute Cloud (EC2) instance,
    # `PhysicalResourceId` corresponds to the `InstanceId`. You can pass the EC2
    # `InstanceId` to `DescribeStackResources` to find which stack the instance
    # belongs to and what other resources are part of the stack.

    # Required: Conditional. If you do not specify `PhysicalResourceId`, you must
    # specify `StackName`.

    # Default: There is no default value.
    physical_resource_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DescribeStackResourcesOutput(OutputShapeBase):
    """
    The output for a DescribeStackResources action.
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
                "stack_resources",
                "StackResources",
                TypeInfo(typing.List[StackResource]),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A list of `StackResource` structures.
    stack_resources: typing.List["StackResource"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class DescribeStackSetInput(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "stack_set_name",
                "StackSetName",
                TypeInfo(str),
            ),
        ]

    # The name or unique ID of the stack set whose description you want.
    stack_set_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DescribeStackSetOperationInput(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "stack_set_name",
                "StackSetName",
                TypeInfo(str),
            ),
            (
                "operation_id",
                "OperationId",
                TypeInfo(str),
            ),
        ]

    # The name or the unique stack ID of the stack set for the stack operation.
    stack_set_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The unique ID of the stack set operation.
    operation_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DescribeStackSetOperationOutput(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "stack_set_operation",
                "StackSetOperation",
                TypeInfo(StackSetOperation),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The specified stack set operation.
    stack_set_operation: "StackSetOperation" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class DescribeStackSetOutput(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "stack_set",
                "StackSet",
                TypeInfo(StackSet),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The specified stack set.
    stack_set: "StackSet" = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DescribeStacksInput(ShapeBase):
    """
    The input for DescribeStacks action.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "stack_name",
                "StackName",
                TypeInfo(str),
            ),
            (
                "next_token",
                "NextToken",
                TypeInfo(str),
            ),
        ]

    # The name or the unique stack ID that is associated with the stack, which
    # are not always interchangeable:

    #   * Running stacks: You can specify either the stack's name or its unique stack ID.

    #   * Deleted stacks: You must specify the unique stack ID.

    # Default: There is no default value.
    stack_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A string that identifies the next page of stacks that you want to retrieve.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DescribeStacksOutput(OutputShapeBase):
    """
    The output for a DescribeStacks action.
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
                "stacks",
                "Stacks",
                TypeInfo(typing.List[Stack]),
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

    # A list of stack structures.
    stacks: typing.List["Stack"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # If the output exceeds 1 MB in size, a string that identifies the next page
    # of stacks. If no additional page exists, this value is null.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    def paginate(self,
                ) -> typing.Generator["DescribeStacksOutput", None, None]:
        yield from super()._paginate()


@dataclasses.dataclass
class EstimateTemplateCostInput(ShapeBase):
    """
    The input for an EstimateTemplateCost action.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "template_body",
                "TemplateBody",
                TypeInfo(str),
            ),
            (
                "template_url",
                "TemplateURL",
                TypeInfo(str),
            ),
            (
                "parameters",
                "Parameters",
                TypeInfo(typing.List[Parameter]),
            ),
        ]

    # Structure containing the template body with a minimum length of 1 byte and
    # a maximum length of 51,200 bytes. (For more information, go to [Template
    # Anatomy](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/template-
    # anatomy.html) in the AWS CloudFormation User Guide.)

    # Conditional: You must pass `TemplateBody` or `TemplateURL`. If both are
    # passed, only `TemplateBody` is used.
    template_body: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Location of file containing the template body. The URL must point to a
    # template that is located in an Amazon S3 bucket. For more information, go
    # to [Template
    # Anatomy](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/template-
    # anatomy.html) in the AWS CloudFormation User Guide.

    # Conditional: You must pass `TemplateURL` or `TemplateBody`. If both are
    # passed, only `TemplateBody` is used.
    template_url: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A list of `Parameter` structures that specify input parameters.
    parameters: typing.List["Parameter"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class EstimateTemplateCostOutput(OutputShapeBase):
    """
    The output for a EstimateTemplateCost action.
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
                "url",
                "Url",
                TypeInfo(str),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # An AWS Simple Monthly Calculator URL with a query string that describes the
    # resources required to run the template.
    url: str = dataclasses.field(default=ShapeBase.NOT_SET, )


class EvaluationType(str):
    Static = "Static"
    Dynamic = "Dynamic"


@dataclasses.dataclass
class ExecuteChangeSetInput(ShapeBase):
    """
    The input for the ExecuteChangeSet action.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "change_set_name",
                "ChangeSetName",
                TypeInfo(str),
            ),
            (
                "stack_name",
                "StackName",
                TypeInfo(str),
            ),
            (
                "client_request_token",
                "ClientRequestToken",
                TypeInfo(str),
            ),
        ]

    # The name or ARN of the change set that you want use to update the specified
    # stack.
    change_set_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # If you specified the name of a change set, specify the stack name or ID
    # (ARN) that is associated with the change set you want to execute.
    stack_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A unique identifier for this `ExecuteChangeSet` request. Specify this token
    # if you plan to retry requests so that AWS CloudFormation knows that you're
    # not attempting to execute a change set to update a stack with the same
    # name. You might retry `ExecuteChangeSet` requests to ensure that AWS
    # CloudFormation successfully received them.
    client_request_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ExecuteChangeSetOutput(OutputShapeBase):
    """
    The output for the ExecuteChangeSet action.
    """

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


class ExecutionStatus(str):
    UNAVAILABLE = "UNAVAILABLE"
    AVAILABLE = "AVAILABLE"
    EXECUTE_IN_PROGRESS = "EXECUTE_IN_PROGRESS"
    EXECUTE_COMPLETE = "EXECUTE_COMPLETE"
    EXECUTE_FAILED = "EXECUTE_FAILED"
    OBSOLETE = "OBSOLETE"


@dataclasses.dataclass
class Export(ShapeBase):
    """
    The `Export` structure describes the exported output values for a stack.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "exporting_stack_id",
                "ExportingStackId",
                TypeInfo(str),
            ),
            (
                "name",
                "Name",
                TypeInfo(str),
            ),
            (
                "value",
                "Value",
                TypeInfo(str),
            ),
        ]

    # The stack that contains the exported output name and value.
    exporting_stack_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The name of exported output value. Use this name and the `Fn::ImportValue`
    # function to import the associated value into other stacks. The name is
    # defined in the `Export` field in the associated stack's `Outputs` section.
    name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The value of the exported output, such as a resource physical ID. This
    # value is defined in the `Export` field in the associated stack's `Outputs`
    # section.
    value: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class GetStackPolicyInput(ShapeBase):
    """
    The input for the GetStackPolicy action.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "stack_name",
                "StackName",
                TypeInfo(str),
            ),
        ]

    # The name or unique stack ID that is associated with the stack whose policy
    # you want to get.
    stack_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class GetStackPolicyOutput(OutputShapeBase):
    """
    The output for the GetStackPolicy action.
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
                "stack_policy_body",
                "StackPolicyBody",
                TypeInfo(str),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Structure containing the stack policy body. (For more information, go to [
    # Prevent Updates to Stack
    # Resources](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/protect-
    # stack-resources.html) in the AWS CloudFormation User Guide.)
    stack_policy_body: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class GetTemplateInput(ShapeBase):
    """
    The input for a GetTemplate action.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "stack_name",
                "StackName",
                TypeInfo(str),
            ),
            (
                "change_set_name",
                "ChangeSetName",
                TypeInfo(str),
            ),
            (
                "template_stage",
                "TemplateStage",
                TypeInfo(typing.Union[str, TemplateStage]),
            ),
        ]

    # The name or the unique stack ID that is associated with the stack, which
    # are not always interchangeable:

    #   * Running stacks: You can specify either the stack's name or its unique stack ID.

    #   * Deleted stacks: You must specify the unique stack ID.

    # Default: There is no default value.
    stack_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The name or Amazon Resource Name (ARN) of a change set for which AWS
    # CloudFormation returns the associated template. If you specify a name, you
    # must also specify the `StackName`.
    change_set_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # For templates that include transforms, the stage of the template that AWS
    # CloudFormation returns. To get the user-submitted template, specify
    # `Original`. To get the template after AWS CloudFormation has processed all
    # transforms, specify `Processed`.

    # If the template doesn't include transforms, `Original` and `Processed`
    # return the same template. By default, AWS CloudFormation specifies
    # `Original`.
    template_stage: typing.Union[str, "TemplateStage"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class GetTemplateOutput(OutputShapeBase):
    """
    The output for GetTemplate action.
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
                "template_body",
                "TemplateBody",
                TypeInfo(str),
            ),
            (
                "stages_available",
                "StagesAvailable",
                TypeInfo(typing.List[typing.Union[str, TemplateStage]]),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Structure containing the template body. (For more information, go to
    # [Template
    # Anatomy](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/template-
    # anatomy.html) in the AWS CloudFormation User Guide.)

    # AWS CloudFormation returns the same template that was used when the stack
    # was created.
    template_body: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The stage of the template that you can retrieve. For stacks, the `Original`
    # and `Processed` templates are always available. For change sets, the
    # `Original` template is always available. After AWS CloudFormation finishes
    # creating the change set, the `Processed` template becomes available.
    stages_available: typing.List[typing.Union[str, "TemplateStage"]
                                 ] = dataclasses.field(
                                     default=ShapeBase.NOT_SET,
                                 )


@dataclasses.dataclass
class GetTemplateSummaryInput(ShapeBase):
    """
    The input for the GetTemplateSummary action.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "template_body",
                "TemplateBody",
                TypeInfo(str),
            ),
            (
                "template_url",
                "TemplateURL",
                TypeInfo(str),
            ),
            (
                "stack_name",
                "StackName",
                TypeInfo(str),
            ),
            (
                "stack_set_name",
                "StackSetName",
                TypeInfo(str),
            ),
        ]

    # Structure containing the template body with a minimum length of 1 byte and
    # a maximum length of 51,200 bytes. For more information about templates, see
    # [Template
    # Anatomy](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/template-
    # anatomy.html) in the AWS CloudFormation User Guide.

    # Conditional: You must specify only one of the following parameters:
    # `StackName`, `StackSetName`, `TemplateBody`, or `TemplateURL`.
    template_body: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Location of file containing the template body. The URL must point to a
    # template (max size: 460,800 bytes) that is located in an Amazon S3 bucket.
    # For more information about templates, see [Template
    # Anatomy](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/template-
    # anatomy.html) in the AWS CloudFormation User Guide.

    # Conditional: You must specify only one of the following parameters:
    # `StackName`, `StackSetName`, `TemplateBody`, or `TemplateURL`.
    template_url: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The name or the stack ID that is associated with the stack, which are not
    # always interchangeable. For running stacks, you can specify either the
    # stack's name or its unique stack ID. For deleted stack, you must specify
    # the unique stack ID.

    # Conditional: You must specify only one of the following parameters:
    # `StackName`, `StackSetName`, `TemplateBody`, or `TemplateURL`.
    stack_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The name or unique ID of the stack set from which the stack was created.

    # Conditional: You must specify only one of the following parameters:
    # `StackName`, `StackSetName`, `TemplateBody`, or `TemplateURL`.
    stack_set_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class GetTemplateSummaryOutput(OutputShapeBase):
    """
    The output for the GetTemplateSummary action.
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
                "parameters",
                "Parameters",
                TypeInfo(typing.List[ParameterDeclaration]),
            ),
            (
                "description",
                "Description",
                TypeInfo(str),
            ),
            (
                "capabilities",
                "Capabilities",
                TypeInfo(typing.List[typing.Union[str, Capability]]),
            ),
            (
                "capabilities_reason",
                "CapabilitiesReason",
                TypeInfo(str),
            ),
            (
                "resource_types",
                "ResourceTypes",
                TypeInfo(typing.List[str]),
            ),
            (
                "version",
                "Version",
                TypeInfo(str),
            ),
            (
                "metadata",
                "Metadata",
                TypeInfo(str),
            ),
            (
                "declared_transforms",
                "DeclaredTransforms",
                TypeInfo(typing.List[str]),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A list of parameter declarations that describe various properties for each
    # parameter.
    parameters: typing.List["ParameterDeclaration"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The value that is defined in the `Description` property of the template.
    description: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The capabilities found within the template. If your template contains IAM
    # resources, you must specify the CAPABILITY_IAM or CAPABILITY_NAMED_IAM
    # value for this parameter when you use the CreateStack or UpdateStack
    # actions with your template; otherwise, those actions return an
    # InsufficientCapabilities error.

    # For more information, see [Acknowledging IAM Resources in AWS
    # CloudFormation
    # Templates](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-
    # iam-template.html#capabilities).
    capabilities: typing.List[typing.Union[str, "Capability"]
                             ] = dataclasses.field(
                                 default=ShapeBase.NOT_SET,
                             )

    # The list of resources that generated the values in the `Capabilities`
    # response element.
    capabilities_reason: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A list of all the template resource types that are defined in the template,
    # such as `AWS::EC2::Instance`, `AWS::Dynamo::Table`, and
    # `Custom::MyCustomInstance`.
    resource_types: typing.List[str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The AWS template format version, which identifies the capabilities of the
    # template.
    version: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The value that is defined for the `Metadata` property of the template.
    metadata: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A list of the transforms that are declared in the template.
    declared_transforms: typing.List[str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class InsufficientCapabilitiesException(ShapeBase):
    """
    The template contains resources with capabilities that weren't specified in the
    Capabilities parameter.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class InvalidChangeSetStatusException(ShapeBase):
    """
    The specified change set can't be used to update the stack. For example, the
    change set status might be `CREATE_IN_PROGRESS`, or the stack status might be
    `UPDATE_IN_PROGRESS`.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class InvalidOperationException(ShapeBase):
    """
    The specified operation isn't valid.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class LimitExceededException(ShapeBase):
    """
    The quota for the resource has already been reached.

    For information on stack set limitations, see [Limitations of
    StackSets](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/stacksets-
    limitations.html).
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class ListChangeSetsInput(ShapeBase):
    """
    The input for the ListChangeSets action.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "stack_name",
                "StackName",
                TypeInfo(str),
            ),
            (
                "next_token",
                "NextToken",
                TypeInfo(str),
            ),
        ]

    # The name or the Amazon Resource Name (ARN) of the stack for which you want
    # to list change sets.
    stack_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A string (provided by the ListChangeSets response output) that identifies
    # the next page of change sets that you want to retrieve.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ListChangeSetsOutput(OutputShapeBase):
    """
    The output for the ListChangeSets action.
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
                "summaries",
                "Summaries",
                TypeInfo(typing.List[ChangeSetSummary]),
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

    # A list of `ChangeSetSummary` structures that provides the ID and status of
    # each change set for the specified stack.
    summaries: typing.List["ChangeSetSummary"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # If the output exceeds 1 MB, a string that identifies the next page of
    # change sets. If there is no additional page, this value is null.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ListExportsInput(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "next_token",
                "NextToken",
                TypeInfo(str),
            ),
        ]

    # A string (provided by the ListExports response output) that identifies the
    # next page of exported output values that you asked to retrieve.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ListExportsOutput(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "exports",
                "Exports",
                TypeInfo(typing.List[Export]),
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

    # The output for the ListExports action.
    exports: typing.List["Export"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # If the output exceeds 100 exported output values, a string that identifies
    # the next page of exports. If there is no additional page, this value is
    # null.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    def paginate(self, ) -> typing.Generator["ListExportsOutput", None, None]:
        yield from super()._paginate()


@dataclasses.dataclass
class ListImportsInput(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "export_name",
                "ExportName",
                TypeInfo(str),
            ),
            (
                "next_token",
                "NextToken",
                TypeInfo(str),
            ),
        ]

    # The name of the exported output value. AWS CloudFormation returns the stack
    # names that are importing this value.
    export_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A string (provided by the ListImports response output) that identifies the
    # next page of stacks that are importing the specified exported output value.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ListImportsOutput(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "imports",
                "Imports",
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

    # A list of stack names that are importing the specified exported output
    # value.
    imports: typing.List[str] = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A string that identifies the next page of exports. If there is no
    # additional page, this value is null.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    def paginate(self, ) -> typing.Generator["ListImportsOutput", None, None]:
        yield from super()._paginate()


@dataclasses.dataclass
class ListStackInstancesInput(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "stack_set_name",
                "StackSetName",
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
            (
                "stack_instance_account",
                "StackInstanceAccount",
                TypeInfo(str),
            ),
            (
                "stack_instance_region",
                "StackInstanceRegion",
                TypeInfo(str),
            ),
        ]

    # The name or unique ID of the stack set that you want to list stack
    # instances for.
    stack_set_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # If the previous request didn't return all of the remaining results, the
    # response's `NextToken` parameter value is set to a token. To retrieve the
    # next set of results, call `ListStackInstances` again and assign that token
    # to the request object's `NextToken` parameter. If there are no remaining
    # results, the previous response object's `NextToken` parameter is set to
    # `null`.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The maximum number of results to be returned with a single call. If the
    # number of available results exceeds this maximum, the response includes a
    # `NextToken` value that you can assign to the `NextToken` request parameter
    # to get the next set of results.
    max_results: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The name of the AWS account that you want to list stack instances for.
    stack_instance_account: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The name of the region where you want to list stack instances.
    stack_instance_region: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ListStackInstancesOutput(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "summaries",
                "Summaries",
                TypeInfo(typing.List[StackInstanceSummary]),
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

    # A list of `StackInstanceSummary` structures that contain information about
    # the specified stack instances.
    summaries: typing.List["StackInstanceSummary"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # If the request doesn't return all of the remaining results, `NextToken` is
    # set to a token. To retrieve the next set of results, call
    # `ListStackInstances` again and assign that token to the request object's
    # `NextToken` parameter. If the request returns all results, `NextToken` is
    # set to `null`.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ListStackResourcesInput(ShapeBase):
    """
    The input for the ListStackResource action.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "stack_name",
                "StackName",
                TypeInfo(str),
            ),
            (
                "next_token",
                "NextToken",
                TypeInfo(str),
            ),
        ]

    # The name or the unique stack ID that is associated with the stack, which
    # are not always interchangeable:

    #   * Running stacks: You can specify either the stack's name or its unique stack ID.

    #   * Deleted stacks: You must specify the unique stack ID.

    # Default: There is no default value.
    stack_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A string that identifies the next page of stack resources that you want to
    # retrieve.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ListStackResourcesOutput(OutputShapeBase):
    """
    The output for a ListStackResources action.
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
                "stack_resource_summaries",
                "StackResourceSummaries",
                TypeInfo(typing.List[StackResourceSummary]),
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

    # A list of `StackResourceSummary` structures.
    stack_resource_summaries: typing.List["StackResourceSummary"
                                         ] = dataclasses.field(
                                             default=ShapeBase.NOT_SET,
                                         )

    # If the output exceeds 1 MB, a string that identifies the next page of stack
    # resources. If no additional page exists, this value is null.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    def paginate(self,
                ) -> typing.Generator["ListStackResourcesOutput", None, None]:
        yield from super()._paginate()


@dataclasses.dataclass
class ListStackSetOperationResultsInput(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "stack_set_name",
                "StackSetName",
                TypeInfo(str),
            ),
            (
                "operation_id",
                "OperationId",
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

    # The name or unique ID of the stack set that you want to get operation
    # results for.
    stack_set_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The ID of the stack set operation.
    operation_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # If the previous request didn't return all of the remaining results, the
    # response object's `NextToken` parameter value is set to a token. To
    # retrieve the next set of results, call `ListStackSetOperationResults` again
    # and assign that token to the request object's `NextToken` parameter. If
    # there are no remaining results, the previous response object's `NextToken`
    # parameter is set to `null`.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The maximum number of results to be returned with a single call. If the
    # number of available results exceeds this maximum, the response includes a
    # `NextToken` value that you can assign to the `NextToken` request parameter
    # to get the next set of results.
    max_results: int = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ListStackSetOperationResultsOutput(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "summaries",
                "Summaries",
                TypeInfo(typing.List[StackSetOperationResultSummary]),
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

    # A list of `StackSetOperationResultSummary` structures that contain
    # information about the specified operation results, for accounts and regions
    # that are included in the operation.
    summaries: typing.List["StackSetOperationResultSummary"
                          ] = dataclasses.field(
                              default=ShapeBase.NOT_SET,
                          )

    # If the request doesn't return all results, `NextToken` is set to a token.
    # To retrieve the next set of results, call `ListOperationResults` again and
    # assign that token to the request object's `NextToken` parameter. If there
    # are no remaining results, `NextToken` is set to `null`.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ListStackSetOperationsInput(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "stack_set_name",
                "StackSetName",
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

    # The name or unique ID of the stack set that you want to get operation
    # summaries for.
    stack_set_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # If the previous paginated request didn't return all of the remaining
    # results, the response object's `NextToken` parameter value is set to a
    # token. To retrieve the next set of results, call `ListStackSetOperations`
    # again and assign that token to the request object's `NextToken` parameter.
    # If there are no remaining results, the previous response object's
    # `NextToken` parameter is set to `null`.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The maximum number of results to be returned with a single call. If the
    # number of available results exceeds this maximum, the response includes a
    # `NextToken` value that you can assign to the `NextToken` request parameter
    # to get the next set of results.
    max_results: int = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ListStackSetOperationsOutput(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "summaries",
                "Summaries",
                TypeInfo(typing.List[StackSetOperationSummary]),
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

    # A list of `StackSetOperationSummary` structures that contain summary
    # information about operations for the specified stack set.
    summaries: typing.List["StackSetOperationSummary"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # If the request doesn't return all results, `NextToken` is set to a token.
    # To retrieve the next set of results, call `ListOperationResults` again and
    # assign that token to the request object's `NextToken` parameter. If there
    # are no remaining results, `NextToken` is set to `null`.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ListStackSetsInput(ShapeBase):
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
                "status",
                "Status",
                TypeInfo(typing.Union[str, StackSetStatus]),
            ),
        ]

    # If the previous paginated request didn't return all of the remaining
    # results, the response object's `NextToken` parameter value is set to a
    # token. To retrieve the next set of results, call `ListStackSets` again and
    # assign that token to the request object's `NextToken` parameter. If there
    # are no remaining results, the previous response object's `NextToken`
    # parameter is set to `null`.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The maximum number of results to be returned with a single call. If the
    # number of available results exceeds this maximum, the response includes a
    # `NextToken` value that you can assign to the `NextToken` request parameter
    # to get the next set of results.
    max_results: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The status of the stack sets that you want to get summary information
    # about.
    status: typing.Union[str, "StackSetStatus"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class ListStackSetsOutput(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "summaries",
                "Summaries",
                TypeInfo(typing.List[StackSetSummary]),
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

    # A list of `StackSetSummary` structures that contain information about the
    # user's stack sets.
    summaries: typing.List["StackSetSummary"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # If the request doesn't return all of the remaining results, `NextToken` is
    # set to a token. To retrieve the next set of results, call
    # `ListStackInstances` again and assign that token to the request object's
    # `NextToken` parameter. If the request returns all results, `NextToken` is
    # set to `null`.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ListStacksInput(ShapeBase):
    """
    The input for ListStacks action.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "next_token",
                "NextToken",
                TypeInfo(str),
            ),
            (
                "stack_status_filter",
                "StackStatusFilter",
                TypeInfo(typing.List[typing.Union[str, StackStatus]]),
            ),
        ]

    # A string that identifies the next page of stacks that you want to retrieve.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Stack status to use as a filter. Specify one or more stack status codes to
    # list only stacks with the specified status codes. For a complete list of
    # stack status codes, see the `StackStatus` parameter of the Stack data type.
    stack_status_filter: typing.List[typing.Union[str, "StackStatus"]
                                    ] = dataclasses.field(
                                        default=ShapeBase.NOT_SET,
                                    )


@dataclasses.dataclass
class ListStacksOutput(OutputShapeBase):
    """
    The output for ListStacks action.
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
                "stack_summaries",
                "StackSummaries",
                TypeInfo(typing.List[StackSummary]),
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

    # A list of `StackSummary` structures containing information about the
    # specified stacks.
    stack_summaries: typing.List["StackSummary"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # If the output exceeds 1 MB in size, a string that identifies the next page
    # of stacks. If no additional page exists, this value is null.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    def paginate(self, ) -> typing.Generator["ListStacksOutput", None, None]:
        yield from super()._paginate()


@dataclasses.dataclass
class NameAlreadyExistsException(ShapeBase):
    """
    The specified name is already in use.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


class OnFailure(str):
    DO_NOTHING = "DO_NOTHING"
    ROLLBACK = "ROLLBACK"
    DELETE = "DELETE"


@dataclasses.dataclass
class OperationIdAlreadyExistsException(ShapeBase):
    """
    The specified operation ID already exists.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class OperationInProgressException(ShapeBase):
    """
    Another operation is currently in progress for this stack set. Only one
    operation can be performed for a stack set at a given time.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class OperationNotFoundException(ShapeBase):
    """
    The specified ID refers to an operation that doesn't exist.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class Output(ShapeBase):
    """
    The Output data type.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "output_key",
                "OutputKey",
                TypeInfo(str),
            ),
            (
                "output_value",
                "OutputValue",
                TypeInfo(str),
            ),
            (
                "description",
                "Description",
                TypeInfo(str),
            ),
            (
                "export_name",
                "ExportName",
                TypeInfo(str),
            ),
        ]

    # The key associated with the output.
    output_key: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The value associated with the output.
    output_value: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # User defined description associated with the output.
    description: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The name of the export associated with the output.
    export_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class Parameter(ShapeBase):
    """
    The Parameter data type.
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
            (
                "use_previous_value",
                "UsePreviousValue",
                TypeInfo(bool),
            ),
            (
                "resolved_value",
                "ResolvedValue",
                TypeInfo(str),
            ),
        ]

    # The key associated with the parameter. If you don't specify a key and value
    # for a particular parameter, AWS CloudFormation uses the default value that
    # is specified in your template.
    parameter_key: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The input value associated with the parameter.
    parameter_value: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # During a stack update, use the existing parameter value that the stack is
    # using for a given parameter key. If you specify `true`, do not specify a
    # parameter value.
    use_previous_value: bool = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Read-only. The value that corresponds to a Systems Manager parameter key.
    # This field is returned only for [ `SSM` parameter
    # types](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/parameters-
    # section-structure.html#aws-ssm-parameter-types) in the template.
    resolved_value: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ParameterConstraints(ShapeBase):
    """
    A set of criteria that AWS CloudFormation uses to validate parameter values.
    Although other constraints might be defined in the stack template, AWS
    CloudFormation returns only the `AllowedValues` property.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "allowed_values",
                "AllowedValues",
                TypeInfo(typing.List[str]),
            ),
        ]

    # A list of values that are permitted for a parameter.
    allowed_values: typing.List[str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class ParameterDeclaration(ShapeBase):
    """
    The ParameterDeclaration data type.
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
                "default_value",
                "DefaultValue",
                TypeInfo(str),
            ),
            (
                "parameter_type",
                "ParameterType",
                TypeInfo(str),
            ),
            (
                "no_echo",
                "NoEcho",
                TypeInfo(bool),
            ),
            (
                "description",
                "Description",
                TypeInfo(str),
            ),
            (
                "parameter_constraints",
                "ParameterConstraints",
                TypeInfo(ParameterConstraints),
            ),
        ]

    # The name that is associated with the parameter.
    parameter_key: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The default value of the parameter.
    default_value: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The type of parameter.
    parameter_type: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Flag that indicates whether the parameter value is shown as plain text in
    # logs and in the AWS Management Console.
    no_echo: bool = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The description that is associate with the parameter.
    description: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The criteria that AWS CloudFormation uses to validate parameter values.
    parameter_constraints: "ParameterConstraints" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


class Replacement(str):
    TRUE = "True"
    FALSE = "False"
    CONDITIONAL = "Conditional"


class RequiresRecreation(str):
    Never = "Never"
    Conditionally = "Conditionally"
    Always = "Always"


class ResourceAttribute(str):
    Properties = "Properties"
    Metadata = "Metadata"
    CreationPolicy = "CreationPolicy"
    UpdatePolicy = "UpdatePolicy"
    DeletionPolicy = "DeletionPolicy"
    Tags = "Tags"


@dataclasses.dataclass
class ResourceChange(ShapeBase):
    """
    The `ResourceChange` structure describes the resource and the action that AWS
    CloudFormation will perform on it if you execute this change set.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "action",
                "Action",
                TypeInfo(typing.Union[str, ChangeAction]),
            ),
            (
                "logical_resource_id",
                "LogicalResourceId",
                TypeInfo(str),
            ),
            (
                "physical_resource_id",
                "PhysicalResourceId",
                TypeInfo(str),
            ),
            (
                "resource_type",
                "ResourceType",
                TypeInfo(str),
            ),
            (
                "replacement",
                "Replacement",
                TypeInfo(typing.Union[str, Replacement]),
            ),
            (
                "scope",
                "Scope",
                TypeInfo(typing.List[typing.Union[str, ResourceAttribute]]),
            ),
            (
                "details",
                "Details",
                TypeInfo(typing.List[ResourceChangeDetail]),
            ),
        ]

    # The action that AWS CloudFormation takes on the resource, such as `Add`
    # (adds a new resource), `Modify` (changes a resource), or `Remove` (deletes
    # a resource).
    action: typing.Union[str, "ChangeAction"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The resource's logical ID, which is defined in the stack's template.
    logical_resource_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The resource's physical ID (resource name). Resources that you are adding
    # don't have physical IDs because they haven't been created.
    physical_resource_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The type of AWS CloudFormation resource, such as `AWS::S3::Bucket`.
    resource_type: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # For the `Modify` action, indicates whether AWS CloudFormation will replace
    # the resource by creating a new one and deleting the old one. This value
    # depends on the value of the `RequiresRecreation` property in the
    # `ResourceTargetDefinition` structure. For example, if the
    # `RequiresRecreation` field is `Always` and the `Evaluation` field is
    # `Static`, `Replacement` is `True`. If the `RequiresRecreation` field is
    # `Always` and the `Evaluation` field is `Dynamic`, `Replacement` is
    # `Conditionally`.

    # If you have multiple changes with different `RequiresRecreation` values,
    # the `Replacement` value depends on the change with the most impact. A
    # `RequiresRecreation` value of `Always` has the most impact, followed by
    # `Conditionally`, and then `Never`.
    replacement: typing.Union[str, "Replacement"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # For the `Modify` action, indicates which resource attribute is triggering
    # this update, such as a change in the resource attribute's `Metadata`,
    # `Properties`, or `Tags`.
    scope: typing.List[typing.Union[str, "ResourceAttribute"]
                      ] = dataclasses.field(
                          default=ShapeBase.NOT_SET,
                      )

    # For the `Modify` action, a list of `ResourceChangeDetail` structures that
    # describes the changes that AWS CloudFormation will make to the resource.
    details: typing.List["ResourceChangeDetail"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class ResourceChangeDetail(ShapeBase):
    """
    For a resource with `Modify` as the action, the `ResourceChange` structure
    describes the changes AWS CloudFormation will make to that resource.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "target",
                "Target",
                TypeInfo(ResourceTargetDefinition),
            ),
            (
                "evaluation",
                "Evaluation",
                TypeInfo(typing.Union[str, EvaluationType]),
            ),
            (
                "change_source",
                "ChangeSource",
                TypeInfo(typing.Union[str, ChangeSource]),
            ),
            (
                "causing_entity",
                "CausingEntity",
                TypeInfo(str),
            ),
        ]

    # A `ResourceTargetDefinition` structure that describes the field that AWS
    # CloudFormation will change and whether the resource will be recreated.
    target: "ResourceTargetDefinition" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Indicates whether AWS CloudFormation can determine the target value, and
    # whether the target value will change before you execute a change set.

    # For `Static` evaluations, AWS CloudFormation can determine that the target
    # value will change, and its value. For example, if you directly modify the
    # `InstanceType` property of an EC2 instance, AWS CloudFormation knows that
    # this property value will change, and its value, so this is a `Static`
    # evaluation.

    # For `Dynamic` evaluations, cannot determine the target value because it
    # depends on the result of an intrinsic function, such as a `Ref` or
    # `Fn::GetAtt` intrinsic function, when the stack is updated. For example, if
    # your template includes a reference to a resource that is conditionally
    # recreated, the value of the reference (the physical ID of the resource)
    # might change, depending on if the resource is recreated. If the resource is
    # recreated, it will have a new physical ID, so all references to that
    # resource will also be updated.
    evaluation: typing.Union[str, "EvaluationType"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The group to which the `CausingEntity` value belongs. There are five entity
    # groups:

    #   * `ResourceReference` entities are `Ref` intrinsic functions that refer to resources in the template, such as `{ "Ref" : "MyEC2InstanceResource" }`.

    #   * `ParameterReference` entities are `Ref` intrinsic functions that get template parameter values, such as `{ "Ref" : "MyPasswordParameter" }`.

    #   * `ResourceAttribute` entities are `Fn::GetAtt` intrinsic functions that get resource attribute values, such as `{ "Fn::GetAtt" : [ "MyEC2InstanceResource", "PublicDnsName" ] }`.

    #   * `DirectModification` entities are changes that are made directly to the template.

    #   * `Automatic` entities are `AWS::CloudFormation::Stack` resource types, which are also known as nested stacks. If you made no changes to the `AWS::CloudFormation::Stack` resource, AWS CloudFormation sets the `ChangeSource` to `Automatic` because the nested stack's template might have changed. Changes to a nested stack's template aren't visible to AWS CloudFormation until you run an update on the parent stack.
    change_source: typing.Union[str, "ChangeSource"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The identity of the entity that triggered this change. This entity is a
    # member of the group that is specified by the `ChangeSource` field. For
    # example, if you modified the value of the `KeyPairName` parameter, the
    # `CausingEntity` is the name of the parameter (`KeyPairName`).

    # If the `ChangeSource` value is `DirectModification`, no value is given for
    # `CausingEntity`.
    causing_entity: str = dataclasses.field(default=ShapeBase.NOT_SET, )


class ResourceSignalStatus(str):
    SUCCESS = "SUCCESS"
    FAILURE = "FAILURE"


class ResourceStatus(str):
    CREATE_IN_PROGRESS = "CREATE_IN_PROGRESS"
    CREATE_FAILED = "CREATE_FAILED"
    CREATE_COMPLETE = "CREATE_COMPLETE"
    DELETE_IN_PROGRESS = "DELETE_IN_PROGRESS"
    DELETE_FAILED = "DELETE_FAILED"
    DELETE_COMPLETE = "DELETE_COMPLETE"
    DELETE_SKIPPED = "DELETE_SKIPPED"
    UPDATE_IN_PROGRESS = "UPDATE_IN_PROGRESS"
    UPDATE_FAILED = "UPDATE_FAILED"
    UPDATE_COMPLETE = "UPDATE_COMPLETE"


@dataclasses.dataclass
class ResourceTargetDefinition(ShapeBase):
    """
    The field that AWS CloudFormation will change, such as the name of a resource's
    property, and whether the resource will be recreated.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "attribute",
                "Attribute",
                TypeInfo(typing.Union[str, ResourceAttribute]),
            ),
            (
                "name",
                "Name",
                TypeInfo(str),
            ),
            (
                "requires_recreation",
                "RequiresRecreation",
                TypeInfo(typing.Union[str, RequiresRecreation]),
            ),
        ]

    # Indicates which resource attribute is triggering this update, such as a
    # change in the resource attribute's `Metadata`, `Properties`, or `Tags`.
    attribute: typing.Union[str, "ResourceAttribute"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # If the `Attribute` value is `Properties`, the name of the property. For all
    # other attributes, the value is null.
    name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # If the `Attribute` value is `Properties`, indicates whether a change to
    # this property causes the resource to be recreated. The value can be
    # `Never`, `Always`, or `Conditionally`. To determine the conditions for a
    # `Conditionally` recreation, see the update behavior for that
    # [property](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-
    # template-resource-type-ref.html) in the AWS CloudFormation User Guide.
    requires_recreation: typing.Union[str, "RequiresRecreation"
                                     ] = dataclasses.field(
                                         default=ShapeBase.NOT_SET,
                                     )


@dataclasses.dataclass
class RollbackConfiguration(ShapeBase):
    """
    Structure containing the rollback triggers for AWS CloudFormation to monitor
    during stack creation and updating operations, and for the specified monitoring
    period afterwards.

    Rollback triggers enable you to have AWS CloudFormation monitor the state of
    your application during stack creation and updating, and to roll back that
    operation if the application breaches the threshold of any of the alarms you've
    specified. For more information, see [Monitor and Roll Back Stack
    Operations](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-
    cfn-rollback-triggers.html).
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "rollback_triggers",
                "RollbackTriggers",
                TypeInfo(typing.List[RollbackTrigger]),
            ),
            (
                "monitoring_time_in_minutes",
                "MonitoringTimeInMinutes",
                TypeInfo(int),
            ),
        ]

    # The triggers to monitor during stack creation or update actions.

    # By default, AWS CloudFormation saves the rollback triggers specified for a
    # stack and applies them to any subsequent update operations for the stack,
    # unless you specify otherwise. If you do specify rollback triggers for this
    # parameter, those triggers replace any list of triggers previously specified
    # for the stack. This means:

    #   * To use the rollback triggers previously specified for this stack, if any, don't specify this parameter.

    #   * To specify new or updated rollback triggers, you must specify _all_ the triggers that you want used for this stack, even triggers you've specifed before (for example, when creating the stack or during a previous stack update). Any triggers that you don't include in the updated list of triggers are no longer applied to the stack.

    #   * To remove all currently specified triggers, specify an empty list for this parameter.

    # If a specified trigger is missing, the entire stack operation fails and is
    # rolled back.
    rollback_triggers: typing.List["RollbackTrigger"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The amount of time, in minutes, during which CloudFormation should monitor
    # all the rollback triggers after the stack creation or update operation
    # deploys all necessary resources.

    # The default is 0 minutes.

    # If you specify a monitoring period but do not specify any rollback
    # triggers, CloudFormation still waits the specified period of time before
    # cleaning up old resources after update operations. You can use this
    # monitoring period to perform any manual stack validation desired, and
    # manually cancel the stack creation or update (using
    # [CancelUpdateStack](http://docs.aws.amazon.com/AWSCloudFormation/latest/APIReference/API_CancelUpdateStack.html),
    # for example) as necessary.

    # If you specify 0 for this parameter, CloudFormation still monitors the
    # specified rollback triggers during stack creation and update operations.
    # Then, for update operations, it begins disposing of old resources
    # immediately once the operation completes.
    monitoring_time_in_minutes: int = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class RollbackTrigger(ShapeBase):
    """
    A rollback trigger AWS CloudFormation monitors during creation and updating of
    stacks. If any of the alarms you specify goes to ALARM state during the stack
    operation or within the specified monitoring period afterwards, CloudFormation
    rolls back the entire stack operation.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "arn",
                "Arn",
                TypeInfo(str),
            ),
            (
                "type",
                "Type",
                TypeInfo(str),
            ),
        ]

    # The Amazon Resource Name (ARN) of the rollback trigger.

    # If a specified trigger is missing, the entire stack operation fails and is
    # rolled back.
    arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The resource type of the rollback trigger. Currently,
    # [AWS::CloudWatch::Alarm](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-
    # properties-cw-alarm.html) is the only supported resource type.
    type: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class SetStackPolicyInput(ShapeBase):
    """
    The input for the SetStackPolicy action.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "stack_name",
                "StackName",
                TypeInfo(str),
            ),
            (
                "stack_policy_body",
                "StackPolicyBody",
                TypeInfo(str),
            ),
            (
                "stack_policy_url",
                "StackPolicyURL",
                TypeInfo(str),
            ),
        ]

    # The name or unique stack ID that you want to associate a policy with.
    stack_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Structure containing the stack policy body. For more information, go to [
    # Prevent Updates to Stack
    # Resources](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/protect-
    # stack-resources.html) in the AWS CloudFormation User Guide. You can specify
    # either the `StackPolicyBody` or the `StackPolicyURL` parameter, but not
    # both.
    stack_policy_body: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Location of a file containing the stack policy. The URL must point to a
    # policy (maximum size: 16 KB) located in an S3 bucket in the same region as
    # the stack. You can specify either the `StackPolicyBody` or the
    # `StackPolicyURL` parameter, but not both.
    stack_policy_url: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class SignalResourceInput(ShapeBase):
    """
    The input for the SignalResource action.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "stack_name",
                "StackName",
                TypeInfo(str),
            ),
            (
                "logical_resource_id",
                "LogicalResourceId",
                TypeInfo(str),
            ),
            (
                "unique_id",
                "UniqueId",
                TypeInfo(str),
            ),
            (
                "status",
                "Status",
                TypeInfo(typing.Union[str, ResourceSignalStatus]),
            ),
        ]

    # The stack name or unique stack ID that includes the resource that you want
    # to signal.
    stack_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The logical ID of the resource that you want to signal. The logical ID is
    # the name of the resource that given in the template.
    logical_resource_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A unique ID of the signal. When you signal Amazon EC2 instances or Auto
    # Scaling groups, specify the instance ID that you are signaling as the
    # unique ID. If you send multiple signals to a single resource (such as
    # signaling a wait condition), each signal requires a different unique ID.
    unique_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The status of the signal, which is either success or failure. A failure
    # signal causes AWS CloudFormation to immediately fail the stack creation or
    # update.
    status: typing.Union[str, "ResourceSignalStatus"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class Stack(ShapeBase):
    """
    The Stack data type.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "stack_name",
                "StackName",
                TypeInfo(str),
            ),
            (
                "creation_time",
                "CreationTime",
                TypeInfo(datetime.datetime),
            ),
            (
                "stack_status",
                "StackStatus",
                TypeInfo(typing.Union[str, StackStatus]),
            ),
            (
                "stack_id",
                "StackId",
                TypeInfo(str),
            ),
            (
                "change_set_id",
                "ChangeSetId",
                TypeInfo(str),
            ),
            (
                "description",
                "Description",
                TypeInfo(str),
            ),
            (
                "parameters",
                "Parameters",
                TypeInfo(typing.List[Parameter]),
            ),
            (
                "deletion_time",
                "DeletionTime",
                TypeInfo(datetime.datetime),
            ),
            (
                "last_updated_time",
                "LastUpdatedTime",
                TypeInfo(datetime.datetime),
            ),
            (
                "rollback_configuration",
                "RollbackConfiguration",
                TypeInfo(RollbackConfiguration),
            ),
            (
                "stack_status_reason",
                "StackStatusReason",
                TypeInfo(str),
            ),
            (
                "disable_rollback",
                "DisableRollback",
                TypeInfo(bool),
            ),
            (
                "notification_arns",
                "NotificationARNs",
                TypeInfo(typing.List[str]),
            ),
            (
                "timeout_in_minutes",
                "TimeoutInMinutes",
                TypeInfo(int),
            ),
            (
                "capabilities",
                "Capabilities",
                TypeInfo(typing.List[typing.Union[str, Capability]]),
            ),
            (
                "outputs",
                "Outputs",
                TypeInfo(typing.List[Output]),
            ),
            (
                "role_arn",
                "RoleARN",
                TypeInfo(str),
            ),
            (
                "tags",
                "Tags",
                TypeInfo(typing.List[Tag]),
            ),
            (
                "enable_termination_protection",
                "EnableTerminationProtection",
                TypeInfo(bool),
            ),
            (
                "parent_id",
                "ParentId",
                TypeInfo(str),
            ),
            (
                "root_id",
                "RootId",
                TypeInfo(str),
            ),
        ]

    # The name associated with the stack.
    stack_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The time at which the stack was created.
    creation_time: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Current status of the stack.
    stack_status: typing.Union[str, "StackStatus"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Unique identifier of the stack.
    stack_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The unique ID of the change set.
    change_set_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A user-defined description associated with the stack.
    description: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A list of `Parameter` structures.
    parameters: typing.List["Parameter"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The time the stack was deleted.
    deletion_time: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The time the stack was last updated. This field will only be returned if
    # the stack has been updated at least once.
    last_updated_time: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The rollback triggers for AWS CloudFormation to monitor during stack
    # creation and updating operations, and for the specified monitoring period
    # afterwards.
    rollback_configuration: "RollbackConfiguration" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Success/failure message associated with the stack status.
    stack_status_reason: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Boolean to enable or disable rollback on stack creation failures:

    #   * `true`: disable rollback

    #   * `false`: enable rollback
    disable_rollback: bool = dataclasses.field(default=ShapeBase.NOT_SET, )

    # SNS topic ARNs to which stack related events are published.
    notification_arns: typing.List[str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The amount of time within which stack creation should complete.
    timeout_in_minutes: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The capabilities allowed in the stack.
    capabilities: typing.List[typing.Union[str, "Capability"]
                             ] = dataclasses.field(
                                 default=ShapeBase.NOT_SET,
                             )

    # A list of output structures.
    outputs: typing.List["Output"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The Amazon Resource Name (ARN) of an AWS Identity and Access Management
    # (IAM) role that is associated with the stack. During a stack operation, AWS
    # CloudFormation uses this role's credentials to make calls on your behalf.
    role_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A list of `Tag`s that specify information about the stack.
    tags: typing.List["Tag"] = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Whether termination protection is enabled for the stack.

    # For [nested
    # stacks](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-
    # cfn-nested-stacks.html), termination protection is set on the root stack
    # and cannot be changed directly on the nested stack. For more information,
    # see [Protecting a Stack From Being
    # Deleted](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-
    # cfn-protect-stacks.html) in the _AWS CloudFormation User Guide_.
    enable_termination_protection: bool = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # For nested stacks--stacks created as resources for another stack--the stack
    # ID of the direct parent of this stack. For the first level of nested
    # stacks, the root stack is also the parent stack.

    # For more information, see [Working with Nested
    # Stacks](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-
    # cfn-nested-stacks.html) in the _AWS CloudFormation User Guide_.
    parent_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # For nested stacks--stacks created as resources for another stack--the stack
    # ID of the the top-level stack to which the nested stack ultimately belongs.

    # For more information, see [Working with Nested
    # Stacks](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-
    # cfn-nested-stacks.html) in the _AWS CloudFormation User Guide_.
    root_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class StackEvent(ShapeBase):
    """
    The StackEvent data type.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "stack_id",
                "StackId",
                TypeInfo(str),
            ),
            (
                "event_id",
                "EventId",
                TypeInfo(str),
            ),
            (
                "stack_name",
                "StackName",
                TypeInfo(str),
            ),
            (
                "timestamp",
                "Timestamp",
                TypeInfo(datetime.datetime),
            ),
            (
                "logical_resource_id",
                "LogicalResourceId",
                TypeInfo(str),
            ),
            (
                "physical_resource_id",
                "PhysicalResourceId",
                TypeInfo(str),
            ),
            (
                "resource_type",
                "ResourceType",
                TypeInfo(str),
            ),
            (
                "resource_status",
                "ResourceStatus",
                TypeInfo(typing.Union[str, ResourceStatus]),
            ),
            (
                "resource_status_reason",
                "ResourceStatusReason",
                TypeInfo(str),
            ),
            (
                "resource_properties",
                "ResourceProperties",
                TypeInfo(str),
            ),
            (
                "client_request_token",
                "ClientRequestToken",
                TypeInfo(str),
            ),
        ]

    # The unique ID name of the instance of the stack.
    stack_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The unique ID of this event.
    event_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The name associated with a stack.
    stack_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Time the status was updated.
    timestamp: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The logical name of the resource specified in the template.
    logical_resource_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The name or unique identifier associated with the physical instance of the
    # resource.
    physical_resource_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Type of resource. (For more information, go to [ AWS Resource Types
    # Reference](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-
    # template-resource-type-ref.html) in the AWS CloudFormation User Guide.)
    resource_type: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Current status of the resource.
    resource_status: typing.Union[str, "ResourceStatus"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Success/failure message associated with the resource.
    resource_status_reason: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # BLOB of the properties used to create the resource.
    resource_properties: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The token passed to the operation that generated this event.

    # All events triggered by a given stack operation are assigned the same
    # client request token, which you can use to track operations. For example,
    # if you execute a `CreateStack` operation with the token `token1`, then all
    # the `StackEvents` generated by that operation will have
    # `ClientRequestToken` set as `token1`.

    # In the console, stack operations display the client request token on the
    # Events tab. Stack operations that are initiated from the console use the
    # token format _Console-StackOperation-ID_ , which helps you easily identify
    # the stack operation . For example, if you create a stack using the console,
    # each stack event would be assigned the same token in the following format:
    # `Console-CreateStack-7f59c3cf-00d2-40c7-b2ff-e75db0987002`.
    client_request_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class StackInstance(ShapeBase):
    """
    An AWS CloudFormation stack, in a specific account and region, that's part of a
    stack set operation. A stack instance is a reference to an attempted or actual
    stack in a given account within a given region. A stack instance can exist
    without a stack—for example, if the stack couldn't be created for some reason. A
    stack instance is associated with only one stack set. Each stack instance
    contains the ID of its associated stack set, as well as the ID of the actual
    stack and the stack status.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "stack_set_id",
                "StackSetId",
                TypeInfo(str),
            ),
            (
                "region",
                "Region",
                TypeInfo(str),
            ),
            (
                "account",
                "Account",
                TypeInfo(str),
            ),
            (
                "stack_id",
                "StackId",
                TypeInfo(str),
            ),
            (
                "parameter_overrides",
                "ParameterOverrides",
                TypeInfo(typing.List[Parameter]),
            ),
            (
                "status",
                "Status",
                TypeInfo(typing.Union[str, StackInstanceStatus]),
            ),
            (
                "status_reason",
                "StatusReason",
                TypeInfo(str),
            ),
        ]

    # The name or unique ID of the stack set that the stack instance is
    # associated with.
    stack_set_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The name of the AWS region that the stack instance is associated with.
    region: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The name of the AWS account that the stack instance is associated with.
    account: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The ID of the stack instance.
    stack_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A list of parameters from the stack set template whose values have been
    # overridden in this stack instance.
    parameter_overrides: typing.List["Parameter"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The status of the stack instance, in terms of its synchronization with its
    # associated stack set.

    #   * `INOPERABLE`: A `DeleteStackInstances` operation has failed and left the stack in an unstable state. Stacks in this state are excluded from further `UpdateStackSet` operations. You might need to perform a `DeleteStackInstances` operation, with `RetainStacks` set to `true`, to delete the stack instance, and then delete the stack manually.

    #   * `OUTDATED`: The stack isn't currently up to date with the stack set because:

    #     * The associated stack failed during a `CreateStackSet` or `UpdateStackSet` operation.

    #     * The stack was part of a `CreateStackSet` or `UpdateStackSet` operation that failed or was stopped before the stack was created or updated.

    #   * `CURRENT`: The stack is currently up to date with the stack set.
    status: typing.Union[str, "StackInstanceStatus"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The explanation for the specific status code that is assigned to this stack
    # instance.
    status_reason: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class StackInstanceNotFoundException(ShapeBase):
    """
    The specified stack instance doesn't exist.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


class StackInstanceStatus(str):
    CURRENT = "CURRENT"
    OUTDATED = "OUTDATED"
    INOPERABLE = "INOPERABLE"


@dataclasses.dataclass
class StackInstanceSummary(ShapeBase):
    """
    The structure that contains summary information about a stack instance.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "stack_set_id",
                "StackSetId",
                TypeInfo(str),
            ),
            (
                "region",
                "Region",
                TypeInfo(str),
            ),
            (
                "account",
                "Account",
                TypeInfo(str),
            ),
            (
                "stack_id",
                "StackId",
                TypeInfo(str),
            ),
            (
                "status",
                "Status",
                TypeInfo(typing.Union[str, StackInstanceStatus]),
            ),
            (
                "status_reason",
                "StatusReason",
                TypeInfo(str),
            ),
        ]

    # The name or unique ID of the stack set that the stack instance is
    # associated with.
    stack_set_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The name of the AWS region that the stack instance is associated with.
    region: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The name of the AWS account that the stack instance is associated with.
    account: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The ID of the stack instance.
    stack_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The status of the stack instance, in terms of its synchronization with its
    # associated stack set.

    #   * `INOPERABLE`: A `DeleteStackInstances` operation has failed and left the stack in an unstable state. Stacks in this state are excluded from further `UpdateStackSet` operations. You might need to perform a `DeleteStackInstances` operation, with `RetainStacks` set to `true`, to delete the stack instance, and then delete the stack manually.

    #   * `OUTDATED`: The stack isn't currently up to date with the stack set because:

    #     * The associated stack failed during a `CreateStackSet` or `UpdateStackSet` operation.

    #     * The stack was part of a `CreateStackSet` or `UpdateStackSet` operation that failed or was stopped before the stack was created or updated.

    #   * `CURRENT`: The stack is currently up to date with the stack set.
    status: typing.Union[str, "StackInstanceStatus"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The explanation for the specific status code assigned to this stack
    # instance.
    status_reason: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class StackResource(ShapeBase):
    """
    The StackResource data type.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "logical_resource_id",
                "LogicalResourceId",
                TypeInfo(str),
            ),
            (
                "resource_type",
                "ResourceType",
                TypeInfo(str),
            ),
            (
                "timestamp",
                "Timestamp",
                TypeInfo(datetime.datetime),
            ),
            (
                "resource_status",
                "ResourceStatus",
                TypeInfo(typing.Union[str, ResourceStatus]),
            ),
            (
                "stack_name",
                "StackName",
                TypeInfo(str),
            ),
            (
                "stack_id",
                "StackId",
                TypeInfo(str),
            ),
            (
                "physical_resource_id",
                "PhysicalResourceId",
                TypeInfo(str),
            ),
            (
                "resource_status_reason",
                "ResourceStatusReason",
                TypeInfo(str),
            ),
            (
                "description",
                "Description",
                TypeInfo(str),
            ),
        ]

    # The logical name of the resource specified in the template.
    logical_resource_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Type of resource. (For more information, go to [ AWS Resource Types
    # Reference](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-
    # template-resource-type-ref.html) in the AWS CloudFormation User Guide.)
    resource_type: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Time the status was updated.
    timestamp: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Current status of the resource.
    resource_status: typing.Union[str, "ResourceStatus"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The name associated with the stack.
    stack_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Unique identifier of the stack.
    stack_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The name or unique identifier that corresponds to a physical instance ID of
    # a resource supported by AWS CloudFormation.
    physical_resource_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Success/failure message associated with the resource.
    resource_status_reason: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # User defined description associated with the resource.
    description: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class StackResourceDetail(ShapeBase):
    """
    Contains detailed information about the specified stack resource.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "logical_resource_id",
                "LogicalResourceId",
                TypeInfo(str),
            ),
            (
                "resource_type",
                "ResourceType",
                TypeInfo(str),
            ),
            (
                "last_updated_timestamp",
                "LastUpdatedTimestamp",
                TypeInfo(datetime.datetime),
            ),
            (
                "resource_status",
                "ResourceStatus",
                TypeInfo(typing.Union[str, ResourceStatus]),
            ),
            (
                "stack_name",
                "StackName",
                TypeInfo(str),
            ),
            (
                "stack_id",
                "StackId",
                TypeInfo(str),
            ),
            (
                "physical_resource_id",
                "PhysicalResourceId",
                TypeInfo(str),
            ),
            (
                "resource_status_reason",
                "ResourceStatusReason",
                TypeInfo(str),
            ),
            (
                "description",
                "Description",
                TypeInfo(str),
            ),
            (
                "metadata",
                "Metadata",
                TypeInfo(str),
            ),
        ]

    # The logical name of the resource specified in the template.
    logical_resource_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Type of resource. ((For more information, go to [ AWS Resource Types
    # Reference](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-
    # template-resource-type-ref.html) in the AWS CloudFormation User Guide.)
    resource_type: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Time the status was updated.
    last_updated_timestamp: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Current status of the resource.
    resource_status: typing.Union[str, "ResourceStatus"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The name associated with the stack.
    stack_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Unique identifier of the stack.
    stack_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The name or unique identifier that corresponds to a physical instance ID of
    # a resource supported by AWS CloudFormation.
    physical_resource_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Success/failure message associated with the resource.
    resource_status_reason: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # User defined description associated with the resource.
    description: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The content of the `Metadata` attribute declared for the resource. For more
    # information, see [Metadata
    # Attribute](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-
    # attribute-metadata.html) in the AWS CloudFormation User Guide.
    metadata: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class StackResourceSummary(ShapeBase):
    """
    Contains high-level information about the specified stack resource.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "logical_resource_id",
                "LogicalResourceId",
                TypeInfo(str),
            ),
            (
                "resource_type",
                "ResourceType",
                TypeInfo(str),
            ),
            (
                "last_updated_timestamp",
                "LastUpdatedTimestamp",
                TypeInfo(datetime.datetime),
            ),
            (
                "resource_status",
                "ResourceStatus",
                TypeInfo(typing.Union[str, ResourceStatus]),
            ),
            (
                "physical_resource_id",
                "PhysicalResourceId",
                TypeInfo(str),
            ),
            (
                "resource_status_reason",
                "ResourceStatusReason",
                TypeInfo(str),
            ),
        ]

    # The logical name of the resource specified in the template.
    logical_resource_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Type of resource. (For more information, go to [ AWS Resource Types
    # Reference](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-
    # template-resource-type-ref.html) in the AWS CloudFormation User Guide.)
    resource_type: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Time the status was updated.
    last_updated_timestamp: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Current status of the resource.
    resource_status: typing.Union[str, "ResourceStatus"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The name or unique identifier that corresponds to a physical instance ID of
    # the resource.
    physical_resource_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Success/failure message associated with the resource.
    resource_status_reason: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class StackSet(ShapeBase):
    """
    A structure that contains information about a stack set. A stack set enables you
    to provision stacks into AWS accounts and across regions by using a single
    CloudFormation template. In the stack set, you specify the template to use, as
    well as any parameters and capabilities that the template requires.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "stack_set_name",
                "StackSetName",
                TypeInfo(str),
            ),
            (
                "stack_set_id",
                "StackSetId",
                TypeInfo(str),
            ),
            (
                "description",
                "Description",
                TypeInfo(str),
            ),
            (
                "status",
                "Status",
                TypeInfo(typing.Union[str, StackSetStatus]),
            ),
            (
                "template_body",
                "TemplateBody",
                TypeInfo(str),
            ),
            (
                "parameters",
                "Parameters",
                TypeInfo(typing.List[Parameter]),
            ),
            (
                "capabilities",
                "Capabilities",
                TypeInfo(typing.List[typing.Union[str, Capability]]),
            ),
            (
                "tags",
                "Tags",
                TypeInfo(typing.List[Tag]),
            ),
            (
                "stack_set_arn",
                "StackSetARN",
                TypeInfo(str),
            ),
            (
                "administration_role_arn",
                "AdministrationRoleARN",
                TypeInfo(str),
            ),
            (
                "execution_role_name",
                "ExecutionRoleName",
                TypeInfo(str),
            ),
        ]

    # The name that's associated with the stack set.
    stack_set_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The ID of the stack set.
    stack_set_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A description of the stack set that you specify when the stack set is
    # created or updated.
    description: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The status of the stack set.
    status: typing.Union[str, "StackSetStatus"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The structure that contains the body of the template that was used to
    # create or update the stack set.
    template_body: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A list of input parameters for a stack set.
    parameters: typing.List["Parameter"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The capabilities that are allowed in the stack set. Some stack set
    # templates might include resources that can affect permissions in your AWS
    # account—for example, by creating new AWS Identity and Access Management
    # (IAM) users. For more information, see [Acknowledging IAM Resources in AWS
    # CloudFormation
    # Templates.](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-
    # iam-template.html#capabilities)
    capabilities: typing.List[typing.Union[str, "Capability"]
                             ] = dataclasses.field(
                                 default=ShapeBase.NOT_SET,
                             )

    # A list of tags that specify information about the stack set. A maximum
    # number of 50 tags can be specified.
    tags: typing.List["Tag"] = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The Amazon Resource Number (ARN) of the stack set.
    stack_set_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The Amazon Resource Number (ARN) of the IAM role used to create or update
    # the stack set.

    # Use customized administrator roles to control which users or groups can
    # manage specific stack sets within the same administrator account. For more
    # information, see [Prerequisites: Granting Permissions for Stack Set
    # Operations](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/stacksets-
    # prereqs.html) in the _AWS CloudFormation User Guide_.
    administration_role_arn: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The name of the IAM execution role used to create or update the stack set.

    # Use customized execution roles to control which stack resources users and
    # groups can include in their stack sets.
    execution_role_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class StackSetNotEmptyException(ShapeBase):
    """
    You can't yet delete this stack set, because it still contains one or more stack
    instances. Delete all stack instances from the stack set before deleting the
    stack set.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class StackSetNotFoundException(ShapeBase):
    """
    The specified stack set doesn't exist.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class StackSetOperation(ShapeBase):
    """
    The structure that contains information about a stack set operation.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "operation_id",
                "OperationId",
                TypeInfo(str),
            ),
            (
                "stack_set_id",
                "StackSetId",
                TypeInfo(str),
            ),
            (
                "action",
                "Action",
                TypeInfo(typing.Union[str, StackSetOperationAction]),
            ),
            (
                "status",
                "Status",
                TypeInfo(typing.Union[str, StackSetOperationStatus]),
            ),
            (
                "operation_preferences",
                "OperationPreferences",
                TypeInfo(StackSetOperationPreferences),
            ),
            (
                "retain_stacks",
                "RetainStacks",
                TypeInfo(bool),
            ),
            (
                "administration_role_arn",
                "AdministrationRoleARN",
                TypeInfo(str),
            ),
            (
                "execution_role_name",
                "ExecutionRoleName",
                TypeInfo(str),
            ),
            (
                "creation_timestamp",
                "CreationTimestamp",
                TypeInfo(datetime.datetime),
            ),
            (
                "end_timestamp",
                "EndTimestamp",
                TypeInfo(datetime.datetime),
            ),
        ]

    # The unique ID of a stack set operation.
    operation_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The ID of the stack set.
    stack_set_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The type of stack set operation: `CREATE`, `UPDATE`, or `DELETE`. Create
    # and delete operations affect only the specified stack set instances that
    # are associated with the specified stack set. Update operations affect both
    # the stack set itself, as well as _all_ associated stack set instances.
    action: typing.Union[str, "StackSetOperationAction"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The status of the operation.

    #   * `FAILED`: The operation exceeded the specified failure tolerance. The failure tolerance value that you've set for an operation is applied for each region during stack create and update operations. If the number of failed stacks within a region exceeds the failure tolerance, the status of the operation in the region is set to `FAILED`. This in turn sets the status of the operation as a whole to `FAILED`, and AWS CloudFormation cancels the operation in any remaining regions.

    #   * `RUNNING`: The operation is currently being performed.

    #   * `STOPPED`: The user has cancelled the operation.

    #   * `STOPPING`: The operation is in the process of stopping, at user request.

    #   * `SUCCEEDED`: The operation completed creating or updating all the specified stacks without exceeding the failure tolerance for the operation.
    status: typing.Union[str, "StackSetOperationStatus"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The preferences for how AWS CloudFormation performs this stack set
    # operation.
    operation_preferences: "StackSetOperationPreferences" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # For stack set operations of action type `DELETE`, specifies whether to
    # remove the stack instances from the specified stack set, but doesn't delete
    # the stacks. You can't reassociate a retained stack, or add an existing,
    # saved stack to a new stack set.
    retain_stacks: bool = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The Amazon Resource Number (ARN) of the IAM role used to perform this stack
    # set operation.

    # Use customized administrator roles to control which users or groups can
    # manage specific stack sets within the same administrator account. For more
    # information, see [Define Permissions for Multiple
    # Administrators](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/stacksets-
    # prereqs.html) in the _AWS CloudFormation User Guide_.
    administration_role_arn: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The name of the IAM execution role used to create or update the stack set.

    # Use customized execution roles to control which stack resources users and
    # groups can include in their stack sets.
    execution_role_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The time at which the operation was initiated. Note that the creation times
    # for the stack set operation might differ from the creation time of the
    # individual stacks themselves. This is because AWS CloudFormation needs to
    # perform preparatory work for the operation, such as dispatching the work to
    # the requested regions, before actually creating the first stacks.
    creation_timestamp: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The time at which the stack set operation ended, across all accounts and
    # regions specified. Note that this doesn't necessarily mean that the stack
    # set operation was successful, or even attempted, in each account or region.
    end_timestamp: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


class StackSetOperationAction(str):
    CREATE = "CREATE"
    UPDATE = "UPDATE"
    DELETE = "DELETE"


@dataclasses.dataclass
class StackSetOperationPreferences(ShapeBase):
    """
    The user-specified preferences for how AWS CloudFormation performs a stack set
    operation.

    For more information on maximum concurrent accounts and failure tolerance, see
    [Stack set operation
    options](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/stacksets-
    concepts.html#stackset-ops-options).
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "region_order",
                "RegionOrder",
                TypeInfo(typing.List[str]),
            ),
            (
                "failure_tolerance_count",
                "FailureToleranceCount",
                TypeInfo(int),
            ),
            (
                "failure_tolerance_percentage",
                "FailureTolerancePercentage",
                TypeInfo(int),
            ),
            (
                "max_concurrent_count",
                "MaxConcurrentCount",
                TypeInfo(int),
            ),
            (
                "max_concurrent_percentage",
                "MaxConcurrentPercentage",
                TypeInfo(int),
            ),
        ]

    # The order of the regions in where you want to perform the stack operation.
    region_order: typing.List[str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The number of accounts, per region, for which this operation can fail
    # before AWS CloudFormation stops the operation in that region. If the
    # operation is stopped in a region, AWS CloudFormation doesn't attempt the
    # operation in any subsequent regions.

    # Conditional: You must specify either `FailureToleranceCount` or
    # `FailureTolerancePercentage` (but not both).
    failure_tolerance_count: int = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The percentage of accounts, per region, for which this stack operation can
    # fail before AWS CloudFormation stops the operation in that region. If the
    # operation is stopped in a region, AWS CloudFormation doesn't attempt the
    # operation in any subsequent regions.

    # When calculating the number of accounts based on the specified percentage,
    # AWS CloudFormation rounds _down_ to the next whole number.

    # Conditional: You must specify either `FailureToleranceCount` or
    # `FailureTolerancePercentage`, but not both.
    failure_tolerance_percentage: int = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The maximum number of accounts in which to perform this operation at one
    # time. This is dependent on the value of
    # `FailureToleranceCount`—`MaxConcurrentCount` is at most one more than the
    # `FailureToleranceCount` .

    # Note that this setting lets you specify the _maximum_ for operations. For
    # large deployments, under certain circumstances the actual number of
    # accounts acted upon concurrently may be lower due to service throttling.

    # Conditional: You must specify either `MaxConcurrentCount` or
    # `MaxConcurrentPercentage`, but not both.
    max_concurrent_count: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The maximum percentage of accounts in which to perform this operation at
    # one time.

    # When calculating the number of accounts based on the specified percentage,
    # AWS CloudFormation rounds down to the next whole number. This is true
    # except in cases where rounding down would result is zero. In this case,
    # CloudFormation sets the number as one instead.

    # Note that this setting lets you specify the _maximum_ for operations. For
    # large deployments, under certain circumstances the actual number of
    # accounts acted upon concurrently may be lower due to service throttling.

    # Conditional: You must specify either `MaxConcurrentCount` or
    # `MaxConcurrentPercentage`, but not both.
    max_concurrent_percentage: int = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


class StackSetOperationResultStatus(str):
    PENDING = "PENDING"
    RUNNING = "RUNNING"
    SUCCEEDED = "SUCCEEDED"
    FAILED = "FAILED"
    CANCELLED = "CANCELLED"


@dataclasses.dataclass
class StackSetOperationResultSummary(ShapeBase):
    """
    The structure that contains information about a specified operation's results
    for a given account in a given region.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "account",
                "Account",
                TypeInfo(str),
            ),
            (
                "region",
                "Region",
                TypeInfo(str),
            ),
            (
                "status",
                "Status",
                TypeInfo(typing.Union[str, StackSetOperationResultStatus]),
            ),
            (
                "status_reason",
                "StatusReason",
                TypeInfo(str),
            ),
            (
                "account_gate_result",
                "AccountGateResult",
                TypeInfo(AccountGateResult),
            ),
        ]

    # The name of the AWS account for this operation result.
    account: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The name of the AWS region for this operation result.
    region: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The result status of the stack set operation for the given account in the
    # given region.

    #   * `CANCELLED`: The operation in the specified account and region has been cancelled. This is either because a user has stopped the stack set operation, or because the failure tolerance of the stack set operation has been exceeded.

    #   * `FAILED`: The operation in the specified account and region failed.

    # If the stack set operation fails in enough accounts within a region, the
    # failure tolerance for the stack set operation as a whole might be exceeded.

    #   * `RUNNING`: The operation in the specified account and region is currently in progress.

    #   * `PENDING`: The operation in the specified account and region has yet to start.

    #   * `SUCCEEDED`: The operation in the specified account and region completed successfully.
    status: typing.Union[str, "StackSetOperationResultStatus"
                        ] = dataclasses.field(
                            default=ShapeBase.NOT_SET,
                        )

    # The reason for the assigned result status.
    status_reason: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The results of the account gate function AWS CloudFormation invokes, if
    # present, before proceeding with stack set operations in an account
    account_gate_result: "AccountGateResult" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


class StackSetOperationStatus(str):
    RUNNING = "RUNNING"
    SUCCEEDED = "SUCCEEDED"
    FAILED = "FAILED"
    STOPPING = "STOPPING"
    STOPPED = "STOPPED"


@dataclasses.dataclass
class StackSetOperationSummary(ShapeBase):
    """
    The structures that contain summary information about the specified operation.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "operation_id",
                "OperationId",
                TypeInfo(str),
            ),
            (
                "action",
                "Action",
                TypeInfo(typing.Union[str, StackSetOperationAction]),
            ),
            (
                "status",
                "Status",
                TypeInfo(typing.Union[str, StackSetOperationStatus]),
            ),
            (
                "creation_timestamp",
                "CreationTimestamp",
                TypeInfo(datetime.datetime),
            ),
            (
                "end_timestamp",
                "EndTimestamp",
                TypeInfo(datetime.datetime),
            ),
        ]

    # The unique ID of the stack set operation.
    operation_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The type of operation: `CREATE`, `UPDATE`, or `DELETE`. Create and delete
    # operations affect only the specified stack instances that are associated
    # with the specified stack set. Update operations affect both the stack set
    # itself as well as _all_ associated stack set instances.
    action: typing.Union[str, "StackSetOperationAction"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The overall status of the operation.

    #   * `FAILED`: The operation exceeded the specified failure tolerance. The failure tolerance value that you've set for an operation is applied for each region during stack create and update operations. If the number of failed stacks within a region exceeds the failure tolerance, the status of the operation in the region is set to `FAILED`. This in turn sets the status of the operation as a whole to `FAILED`, and AWS CloudFormation cancels the operation in any remaining regions.

    #   * `RUNNING`: The operation is currently being performed.

    #   * `STOPPED`: The user has cancelled the operation.

    #   * `STOPPING`: The operation is in the process of stopping, at user request.

    #   * `SUCCEEDED`: The operation completed creating or updating all the specified stacks without exceeding the failure tolerance for the operation.
    status: typing.Union[str, "StackSetOperationStatus"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The time at which the operation was initiated. Note that the creation times
    # for the stack set operation might differ from the creation time of the
    # individual stacks themselves. This is because AWS CloudFormation needs to
    # perform preparatory work for the operation, such as dispatching the work to
    # the requested regions, before actually creating the first stacks.
    creation_timestamp: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The time at which the stack set operation ended, across all accounts and
    # regions specified. Note that this doesn't necessarily mean that the stack
    # set operation was successful, or even attempted, in each account or region.
    end_timestamp: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


class StackSetStatus(str):
    ACTIVE = "ACTIVE"
    DELETED = "DELETED"


@dataclasses.dataclass
class StackSetSummary(ShapeBase):
    """
    The structures that contain summary information about the specified stack set.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "stack_set_name",
                "StackSetName",
                TypeInfo(str),
            ),
            (
                "stack_set_id",
                "StackSetId",
                TypeInfo(str),
            ),
            (
                "description",
                "Description",
                TypeInfo(str),
            ),
            (
                "status",
                "Status",
                TypeInfo(typing.Union[str, StackSetStatus]),
            ),
        ]

    # The name of the stack set.
    stack_set_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The ID of the stack set.
    stack_set_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A description of the stack set that you specify when the stack set is
    # created or updated.
    description: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The status of the stack set.
    status: typing.Union[str, "StackSetStatus"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


class StackStatus(str):
    CREATE_IN_PROGRESS = "CREATE_IN_PROGRESS"
    CREATE_FAILED = "CREATE_FAILED"
    CREATE_COMPLETE = "CREATE_COMPLETE"
    ROLLBACK_IN_PROGRESS = "ROLLBACK_IN_PROGRESS"
    ROLLBACK_FAILED = "ROLLBACK_FAILED"
    ROLLBACK_COMPLETE = "ROLLBACK_COMPLETE"
    DELETE_IN_PROGRESS = "DELETE_IN_PROGRESS"
    DELETE_FAILED = "DELETE_FAILED"
    DELETE_COMPLETE = "DELETE_COMPLETE"
    UPDATE_IN_PROGRESS = "UPDATE_IN_PROGRESS"
    UPDATE_COMPLETE_CLEANUP_IN_PROGRESS = "UPDATE_COMPLETE_CLEANUP_IN_PROGRESS"
    UPDATE_COMPLETE = "UPDATE_COMPLETE"
    UPDATE_ROLLBACK_IN_PROGRESS = "UPDATE_ROLLBACK_IN_PROGRESS"
    UPDATE_ROLLBACK_FAILED = "UPDATE_ROLLBACK_FAILED"
    UPDATE_ROLLBACK_COMPLETE_CLEANUP_IN_PROGRESS = "UPDATE_ROLLBACK_COMPLETE_CLEANUP_IN_PROGRESS"
    UPDATE_ROLLBACK_COMPLETE = "UPDATE_ROLLBACK_COMPLETE"
    REVIEW_IN_PROGRESS = "REVIEW_IN_PROGRESS"


@dataclasses.dataclass
class StackSummary(ShapeBase):
    """
    The StackSummary Data Type
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "stack_name",
                "StackName",
                TypeInfo(str),
            ),
            (
                "creation_time",
                "CreationTime",
                TypeInfo(datetime.datetime),
            ),
            (
                "stack_status",
                "StackStatus",
                TypeInfo(typing.Union[str, StackStatus]),
            ),
            (
                "stack_id",
                "StackId",
                TypeInfo(str),
            ),
            (
                "template_description",
                "TemplateDescription",
                TypeInfo(str),
            ),
            (
                "last_updated_time",
                "LastUpdatedTime",
                TypeInfo(datetime.datetime),
            ),
            (
                "deletion_time",
                "DeletionTime",
                TypeInfo(datetime.datetime),
            ),
            (
                "stack_status_reason",
                "StackStatusReason",
                TypeInfo(str),
            ),
            (
                "parent_id",
                "ParentId",
                TypeInfo(str),
            ),
            (
                "root_id",
                "RootId",
                TypeInfo(str),
            ),
        ]

    # The name associated with the stack.
    stack_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The time the stack was created.
    creation_time: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The current status of the stack.
    stack_status: typing.Union[str, "StackStatus"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Unique stack identifier.
    stack_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The template description of the template used to create the stack.
    template_description: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The time the stack was last updated. This field will only be returned if
    # the stack has been updated at least once.
    last_updated_time: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The time the stack was deleted.
    deletion_time: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Success/Failure message associated with the stack status.
    stack_status_reason: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # For nested stacks--stacks created as resources for another stack--the stack
    # ID of the direct parent of this stack. For the first level of nested
    # stacks, the root stack is also the parent stack.

    # For more information, see [Working with Nested
    # Stacks](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-
    # cfn-nested-stacks.html) in the _AWS CloudFormation User Guide_.
    parent_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # For nested stacks--stacks created as resources for another stack--the stack
    # ID of the the top-level stack to which the nested stack ultimately belongs.

    # For more information, see [Working with Nested
    # Stacks](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-
    # cfn-nested-stacks.html) in the _AWS CloudFormation User Guide_.
    root_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class StaleRequestException(ShapeBase):
    """
    Another operation has been performed on this stack set since the specified
    operation was performed.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class StopStackSetOperationInput(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "stack_set_name",
                "StackSetName",
                TypeInfo(str),
            ),
            (
                "operation_id",
                "OperationId",
                TypeInfo(str),
            ),
        ]

    # The name or unique ID of the stack set that you want to stop the operation
    # for.
    stack_set_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The ID of the stack operation.
    operation_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class StopStackSetOperationOutput(OutputShapeBase):
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
    The Tag type enables you to specify a key-value pair that can be used to store
    information about an AWS CloudFormation stack.
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

    # _Required_. A string used to identify this tag. You can specify a maximum
    # of 128 characters for a tag key. Tags owned by Amazon Web Services (AWS)
    # have the reserved prefix: `aws:`.
    key: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # _Required_. A string containing the value for this tag. You can specify a
    # maximum of 256 characters for a tag value.
    value: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class TemplateParameter(ShapeBase):
    """
    The TemplateParameter data type.
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
                "default_value",
                "DefaultValue",
                TypeInfo(str),
            ),
            (
                "no_echo",
                "NoEcho",
                TypeInfo(bool),
            ),
            (
                "description",
                "Description",
                TypeInfo(str),
            ),
        ]

    # The name associated with the parameter.
    parameter_key: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The default value associated with the parameter.
    default_value: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Flag indicating whether the parameter should be displayed as plain text in
    # logs and UIs.
    no_echo: bool = dataclasses.field(default=ShapeBase.NOT_SET, )

    # User defined description associated with the parameter.
    description: str = dataclasses.field(default=ShapeBase.NOT_SET, )


class TemplateStage(str):
    Original = "Original"
    Processed = "Processed"


@dataclasses.dataclass
class TokenAlreadyExistsException(ShapeBase):
    """
    A client request token already exists.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class UpdateStackInput(ShapeBase):
    """
    The input for an UpdateStack action.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "stack_name",
                "StackName",
                TypeInfo(str),
            ),
            (
                "template_body",
                "TemplateBody",
                TypeInfo(str),
            ),
            (
                "template_url",
                "TemplateURL",
                TypeInfo(str),
            ),
            (
                "use_previous_template",
                "UsePreviousTemplate",
                TypeInfo(bool),
            ),
            (
                "stack_policy_during_update_body",
                "StackPolicyDuringUpdateBody",
                TypeInfo(str),
            ),
            (
                "stack_policy_during_update_url",
                "StackPolicyDuringUpdateURL",
                TypeInfo(str),
            ),
            (
                "parameters",
                "Parameters",
                TypeInfo(typing.List[Parameter]),
            ),
            (
                "capabilities",
                "Capabilities",
                TypeInfo(typing.List[typing.Union[str, Capability]]),
            ),
            (
                "resource_types",
                "ResourceTypes",
                TypeInfo(typing.List[str]),
            ),
            (
                "role_arn",
                "RoleARN",
                TypeInfo(str),
            ),
            (
                "rollback_configuration",
                "RollbackConfiguration",
                TypeInfo(RollbackConfiguration),
            ),
            (
                "stack_policy_body",
                "StackPolicyBody",
                TypeInfo(str),
            ),
            (
                "stack_policy_url",
                "StackPolicyURL",
                TypeInfo(str),
            ),
            (
                "notification_arns",
                "NotificationARNs",
                TypeInfo(typing.List[str]),
            ),
            (
                "tags",
                "Tags",
                TypeInfo(typing.List[Tag]),
            ),
            (
                "client_request_token",
                "ClientRequestToken",
                TypeInfo(str),
            ),
        ]

    # The name or unique stack ID of the stack to update.
    stack_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Structure containing the template body with a minimum length of 1 byte and
    # a maximum length of 51,200 bytes. (For more information, go to [Template
    # Anatomy](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/template-
    # anatomy.html) in the AWS CloudFormation User Guide.)

    # Conditional: You must specify only one of the following parameters:
    # `TemplateBody`, `TemplateURL`, or set the `UsePreviousTemplate` to `true`.
    template_body: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Location of file containing the template body. The URL must point to a
    # template that is located in an Amazon S3 bucket. For more information, go
    # to [Template
    # Anatomy](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/template-
    # anatomy.html) in the AWS CloudFormation User Guide.

    # Conditional: You must specify only one of the following parameters:
    # `TemplateBody`, `TemplateURL`, or set the `UsePreviousTemplate` to `true`.
    template_url: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Reuse the existing template that is associated with the stack that you are
    # updating.

    # Conditional: You must specify only one of the following parameters:
    # `TemplateBody`, `TemplateURL`, or set the `UsePreviousTemplate` to `true`.
    use_previous_template: bool = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Structure containing the temporary overriding stack policy body. You can
    # specify either the `StackPolicyDuringUpdateBody` or the
    # `StackPolicyDuringUpdateURL` parameter, but not both.

    # If you want to update protected resources, specify a temporary overriding
    # stack policy during this update. If you do not specify a stack policy, the
    # current policy that is associated with the stack will be used.
    stack_policy_during_update_body: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Location of a file containing the temporary overriding stack policy. The
    # URL must point to a policy (max size: 16KB) located in an S3 bucket in the
    # same region as the stack. You can specify either the
    # `StackPolicyDuringUpdateBody` or the `StackPolicyDuringUpdateURL`
    # parameter, but not both.

    # If you want to update protected resources, specify a temporary overriding
    # stack policy during this update. If you do not specify a stack policy, the
    # current policy that is associated with the stack will be used.
    stack_policy_during_update_url: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A list of `Parameter` structures that specify input parameters for the
    # stack. For more information, see the
    # [Parameter](http://docs.aws.amazon.com/AWSCloudFormation/latest/APIReference/API_Parameter.html)
    # data type.
    parameters: typing.List["Parameter"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A list of values that you must specify before AWS CloudFormation can update
    # certain stacks. Some stack templates might include resources that can
    # affect permissions in your AWS account, for example, by creating new AWS
    # Identity and Access Management (IAM) users. For those stacks, you must
    # explicitly acknowledge their capabilities by specifying this parameter.

    # The only valid values are `CAPABILITY_IAM` and `CAPABILITY_NAMED_IAM`. The
    # following resources require you to specify this parameter: [
    # AWS::IAM::AccessKey](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-
    # properties-iam-accesskey.html), [
    # AWS::IAM::Group](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-
    # properties-iam-group.html), [
    # AWS::IAM::InstanceProfile](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-
    # resource-iam-instanceprofile.html), [
    # AWS::IAM::Policy](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-
    # properties-iam-policy.html), [
    # AWS::IAM::Role](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-
    # resource-iam-role.html), [
    # AWS::IAM::User](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-
    # properties-iam-user.html), and [
    # AWS::IAM::UserToGroupAddition](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-
    # properties-iam-addusertogroup.html). If your stack template contains these
    # resources, we recommend that you review all permissions associated with
    # them and edit their permissions if necessary.

    # If you have IAM resources, you can specify either capability. If you have
    # IAM resources with custom names, you must specify `CAPABILITY_NAMED_IAM`.
    # If you don't specify this parameter, this action returns an
    # `InsufficientCapabilities` error.

    # For more information, see [Acknowledging IAM Resources in AWS
    # CloudFormation
    # Templates](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-
    # iam-template.html#capabilities).
    capabilities: typing.List[typing.Union[str, "Capability"]
                             ] = dataclasses.field(
                                 default=ShapeBase.NOT_SET,
                             )

    # The template resource types that you have permissions to work with for this
    # update stack action, such as `AWS::EC2::Instance`, `AWS::EC2::*`, or
    # `Custom::MyCustomInstance`.

    # If the list of resource types doesn't include a resource that you're
    # updating, the stack update fails. By default, AWS CloudFormation grants
    # permissions to all resource types. AWS Identity and Access Management (IAM)
    # uses this parameter for AWS CloudFormation-specific condition keys in IAM
    # policies. For more information, see [Controlling Access with AWS Identity
    # and Access
    # Management](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-
    # iam-template.html).
    resource_types: typing.List[str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The Amazon Resource Name (ARN) of an AWS Identity and Access Management
    # (IAM) role that AWS CloudFormation assumes to update the stack. AWS
    # CloudFormation uses the role's credentials to make calls on your behalf.
    # AWS CloudFormation always uses this role for all future operations on the
    # stack. As long as users have permission to operate on the stack, AWS
    # CloudFormation uses this role even if the users don't have permission to
    # pass it. Ensure that the role grants least privilege.

    # If you don't specify a value, AWS CloudFormation uses the role that was
    # previously associated with the stack. If no role is available, AWS
    # CloudFormation uses a temporary session that is generated from your user
    # credentials.
    role_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The rollback triggers for AWS CloudFormation to monitor during stack
    # creation and updating operations, and for the specified monitoring period
    # afterwards.
    rollback_configuration: "RollbackConfiguration" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Structure containing a new stack policy body. You can specify either the
    # `StackPolicyBody` or the `StackPolicyURL` parameter, but not both.

    # You might update the stack policy, for example, in order to protect a new
    # resource that you created during a stack update. If you do not specify a
    # stack policy, the current policy that is associated with the stack is
    # unchanged.
    stack_policy_body: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Location of a file containing the updated stack policy. The URL must point
    # to a policy (max size: 16KB) located in an S3 bucket in the same region as
    # the stack. You can specify either the `StackPolicyBody` or the
    # `StackPolicyURL` parameter, but not both.

    # You might update the stack policy, for example, in order to protect a new
    # resource that you created during a stack update. If you do not specify a
    # stack policy, the current policy that is associated with the stack is
    # unchanged.
    stack_policy_url: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Amazon Simple Notification Service topic Amazon Resource Names (ARNs) that
    # AWS CloudFormation associates with the stack. Specify an empty list to
    # remove all notification topics.
    notification_arns: typing.List[str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Key-value pairs to associate with this stack. AWS CloudFormation also
    # propagates these tags to supported resources in the stack. You can specify
    # a maximum number of 50 tags.

    # If you don't specify this parameter, AWS CloudFormation doesn't modify the
    # stack's tags. If you specify an empty value, AWS CloudFormation removes all
    # associated tags.
    tags: typing.List["Tag"] = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A unique identifier for this `UpdateStack` request. Specify this token if
    # you plan to retry requests so that AWS CloudFormation knows that you're not
    # attempting to update a stack with the same name. You might retry
    # `UpdateStack` requests to ensure that AWS CloudFormation successfully
    # received them.

    # All events triggered by a given stack operation are assigned the same
    # client request token, which you can use to track operations. For example,
    # if you execute a `CreateStack` operation with the token `token1`, then all
    # the `StackEvents` generated by that operation will have
    # `ClientRequestToken` set as `token1`.

    # In the console, stack operations display the client request token on the
    # Events tab. Stack operations that are initiated from the console use the
    # token format _Console-StackOperation-ID_ , which helps you easily identify
    # the stack operation . For example, if you create a stack using the console,
    # each stack event would be assigned the same token in the following format:
    # `Console-CreateStack-7f59c3cf-00d2-40c7-b2ff-e75db0987002`.
    client_request_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class UpdateStackInstancesInput(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "stack_set_name",
                "StackSetName",
                TypeInfo(str),
            ),
            (
                "accounts",
                "Accounts",
                TypeInfo(typing.List[str]),
            ),
            (
                "regions",
                "Regions",
                TypeInfo(typing.List[str]),
            ),
            (
                "parameter_overrides",
                "ParameterOverrides",
                TypeInfo(typing.List[Parameter]),
            ),
            (
                "operation_preferences",
                "OperationPreferences",
                TypeInfo(StackSetOperationPreferences),
            ),
            (
                "operation_id",
                "OperationId",
                TypeInfo(str),
            ),
        ]

    # The name or unique ID of the stack set associated with the stack instances.
    stack_set_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The names of one or more AWS accounts for which you want to update
    # parameter values for stack instances. The overridden parameter values will
    # be applied to all stack instances in the specified accounts and regions.
    accounts: typing.List[str] = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The names of one or more regions in which you want to update parameter
    # values for stack instances. The overridden parameter values will be applied
    # to all stack instances in the specified accounts and regions.
    regions: typing.List[str] = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A list of input parameters whose values you want to update for the
    # specified stack instances.

    # Any overridden parameter values will be applied to all stack instances in
    # the specified accounts and regions. When specifying parameters and their
    # values, be aware of how AWS CloudFormation sets parameter values during
    # stack instance update operations:

    #   * To override the current value for a parameter, include the parameter and specify its value.

    #   * To leave a parameter set to its present value, you can do one of the following:

    #     * Do not include the parameter in the list.

    #     * Include the parameter and specify `UsePreviousValue` as `true`. (You cannot specify both a value and set `UsePreviousValue` to `true`.)

    #   * To set all overridden parameter back to the values specified in the stack set, specify a parameter list but do not include any parameters.

    #   * To leave all parameters set to their present values, do not specify this property at all.

    # During stack set updates, any parameter values overridden for a stack
    # instance are not updated, but retain their overridden value.

    # You can only override the parameter _values_ that are specified in the
    # stack set; to add or delete a parameter itself, use `UpdateStackSet` to
    # update the stack set template. If you add a parameter to a template, before
    # you can override the parameter value specified in the stack set you must
    # first use
    # [UpdateStackSet](http://docs.aws.amazon.com/AWSCloudFormation/latest/APIReference/API_UpdateStackSet.html)
    # to update all stack instances with the updated template and parameter value
    # specified in the stack set. Once a stack instance has been updated with the
    # new parameter, you can then override the parameter value using
    # `UpdateStackInstances`.
    parameter_overrides: typing.List["Parameter"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Preferences for how AWS CloudFormation performs this stack set operation.
    operation_preferences: "StackSetOperationPreferences" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The unique identifier for this stack set operation.

    # The operation ID also functions as an idempotency token, to ensure that AWS
    # CloudFormation performs the stack set operation only once, even if you
    # retry the request multiple times. You might retry stack set operation
    # requests to ensure that AWS CloudFormation successfully received them.

    # If you don't specify an operation ID, the SDK generates one automatically.
    operation_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class UpdateStackInstancesOutput(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "operation_id",
                "OperationId",
                TypeInfo(str),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The unique identifier for this stack set operation.
    operation_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class UpdateStackOutput(OutputShapeBase):
    """
    The output for an UpdateStack action.
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
                "stack_id",
                "StackId",
                TypeInfo(str),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Unique identifier of the stack.
    stack_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class UpdateStackSetInput(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "stack_set_name",
                "StackSetName",
                TypeInfo(str),
            ),
            (
                "description",
                "Description",
                TypeInfo(str),
            ),
            (
                "template_body",
                "TemplateBody",
                TypeInfo(str),
            ),
            (
                "template_url",
                "TemplateURL",
                TypeInfo(str),
            ),
            (
                "use_previous_template",
                "UsePreviousTemplate",
                TypeInfo(bool),
            ),
            (
                "parameters",
                "Parameters",
                TypeInfo(typing.List[Parameter]),
            ),
            (
                "capabilities",
                "Capabilities",
                TypeInfo(typing.List[typing.Union[str, Capability]]),
            ),
            (
                "tags",
                "Tags",
                TypeInfo(typing.List[Tag]),
            ),
            (
                "operation_preferences",
                "OperationPreferences",
                TypeInfo(StackSetOperationPreferences),
            ),
            (
                "administration_role_arn",
                "AdministrationRoleARN",
                TypeInfo(str),
            ),
            (
                "execution_role_name",
                "ExecutionRoleName",
                TypeInfo(str),
            ),
            (
                "operation_id",
                "OperationId",
                TypeInfo(str),
            ),
            (
                "accounts",
                "Accounts",
                TypeInfo(typing.List[str]),
            ),
            (
                "regions",
                "Regions",
                TypeInfo(typing.List[str]),
            ),
        ]

    # The name or unique ID of the stack set that you want to update.
    stack_set_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A brief description of updates that you are making.
    description: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The structure that contains the template body, with a minimum length of 1
    # byte and a maximum length of 51,200 bytes. For more information, see
    # [Template
    # Anatomy](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/template-
    # anatomy.html) in the AWS CloudFormation User Guide.

    # Conditional: You must specify only one of the following parameters:
    # `TemplateBody` or `TemplateURL`—or set `UsePreviousTemplate` to true.
    template_body: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The location of the file that contains the template body. The URL must
    # point to a template (maximum size: 460,800 bytes) that is located in an
    # Amazon S3 bucket. For more information, see [Template
    # Anatomy](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/template-
    # anatomy.html) in the AWS CloudFormation User Guide.

    # Conditional: You must specify only one of the following parameters:
    # `TemplateBody` or `TemplateURL`—or set `UsePreviousTemplate` to true.
    template_url: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Use the existing template that's associated with the stack set that you're
    # updating.

    # Conditional: You must specify only one of the following parameters:
    # `TemplateBody` or `TemplateURL`—or set `UsePreviousTemplate` to true.
    use_previous_template: bool = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A list of input parameters for the stack set template.
    parameters: typing.List["Parameter"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A list of values that you must specify before AWS CloudFormation can create
    # certain stack sets. Some stack set templates might include resources that
    # can affect permissions in your AWS account—for example, by creating new AWS
    # Identity and Access Management (IAM) users. For those stack sets, you must
    # explicitly acknowledge their capabilities by specifying this parameter.

    # The only valid values are CAPABILITY_IAM and CAPABILITY_NAMED_IAM. The
    # following resources require you to specify this parameter:

    #   * AWS::IAM::AccessKey

    #   * AWS::IAM::Group

    #   * AWS::IAM::InstanceProfile

    #   * AWS::IAM::Policy

    #   * AWS::IAM::Role

    #   * AWS::IAM::User

    #   * AWS::IAM::UserToGroupAddition

    # If your stack template contains these resources, we recommend that you
    # review all permissions that are associated with them and edit their
    # permissions if necessary.

    # If you have IAM resources, you can specify either capability. If you have
    # IAM resources with custom names, you must specify CAPABILITY_NAMED_IAM. If
    # you don't specify this parameter, this action returns an
    # `InsufficientCapabilities` error.

    # For more information, see [Acknowledging IAM Resources in AWS
    # CloudFormation
    # Templates.](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-
    # iam-template.html#capabilities)
    capabilities: typing.List[typing.Union[str, "Capability"]
                             ] = dataclasses.field(
                                 default=ShapeBase.NOT_SET,
                             )

    # The key-value pairs to associate with this stack set and the stacks created
    # from it. AWS CloudFormation also propagates these tags to supported
    # resources that are created in the stacks. You can specify a maximum number
    # of 50 tags.

    # If you specify tags for this parameter, those tags replace any list of tags
    # that are currently associated with this stack set. This means:

    #   * If you don't specify this parameter, AWS CloudFormation doesn't modify the stack's tags.

    #   * If you specify _any_ tags using this parameter, you must specify _all_ the tags that you want associated with this stack set, even tags you've specifed before (for example, when creating the stack set or during a previous update of the stack set.). Any tags that you don't include in the updated list of tags are removed from the stack set, and therefore from the stacks and resources as well.

    #   * If you specify an empty value, AWS CloudFormation removes all currently associated tags.

    # If you specify new tags as part of an `UpdateStackSet` action, AWS
    # CloudFormation checks to see if you have the required IAM permission to tag
    # resources. If you omit tags that are currently associated with the stack
    # set from the list of tags you specify, AWS CloudFormation assumes that you
    # want to remove those tags from the stack set, and checks to see if you have
    # permission to untag resources. If you don't have the necessary
    # permission(s), the entire `UpdateStackSet` action fails with an `access
    # denied` error, and the stack set is not updated.
    tags: typing.List["Tag"] = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Preferences for how AWS CloudFormation performs this stack set operation.
    operation_preferences: "StackSetOperationPreferences" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The Amazon Resource Number (ARN) of the IAM role to use to update this
    # stack set.

    # Specify an IAM role only if you are using customized administrator roles to
    # control which users or groups can manage specific stack sets within the
    # same administrator account. For more information, see [Define Permissions
    # for Multiple
    # Administrators](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/stacksets-
    # prereqs.html) in the _AWS CloudFormation User Guide_.

    # If you specify a customized administrator role, AWS CloudFormation uses
    # that role to update the stack. If you do not specify a customized
    # administrator role, AWS CloudFormation performs the update using the role
    # previously associated with the stack set, so long as you have permissions
    # to perform operations on the stack set.
    administration_role_arn: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The name of the IAM execution role to use to update the stack set. If you
    # do not specify an execution role, AWS CloudFormation uses the
    # `AWSCloudFormationStackSetExecutionRole` role for the stack set operation.

    # Specify an IAM role only if you are using customized execution roles to
    # control which stack resources users and groups can include in their stack
    # sets.

    # If you specify a customized execution role, AWS CloudFormation uses that
    # role to update the stack. If you do not specify a customized execution
    # role, AWS CloudFormation performs the update using the role previously
    # associated with the stack set, so long as you have permissions to perform
    # operations on the stack set.
    execution_role_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The unique ID for this stack set operation.

    # The operation ID also functions as an idempotency token, to ensure that AWS
    # CloudFormation performs the stack set operation only once, even if you
    # retry the request multiple times. You might retry stack set operation
    # requests to ensure that AWS CloudFormation successfully received them.

    # If you don't specify an operation ID, AWS CloudFormation generates one
    # automatically.

    # Repeating this stack set operation with a new operation ID retries all
    # stack instances whose status is `OUTDATED`.
    operation_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The accounts in which to update associated stack instances. If you specify
    # accounts, you must also specify the regions in which to update stack set
    # instances.

    # To update _all_ the stack instances associated with this stack set, do not
    # specify the `Accounts` or `Regions` properties.

    # If the stack set update includes changes to the template (that is, if the
    # `TemplateBody` or `TemplateURL` properties are specified), or the
    # `Parameters` property, AWS CloudFormation marks all stack instances with a
    # status of `OUTDATED` prior to updating the stack instances in the specified
    # accounts and regions. If the stack set update does not include changes to
    # the template or parameters, AWS CloudFormation updates the stack instances
    # in the specified accounts and regions, while leaving all other stack
    # instances with their existing stack instance status.
    accounts: typing.List[str] = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The regions in which to update associated stack instances. If you specify
    # regions, you must also specify accounts in which to update stack set
    # instances.

    # To update _all_ the stack instances associated with this stack set, do not
    # specify the `Accounts` or `Regions` properties.

    # If the stack set update includes changes to the template (that is, if the
    # `TemplateBody` or `TemplateURL` properties are specified), or the
    # `Parameters` property, AWS CloudFormation marks all stack instances with a
    # status of `OUTDATED` prior to updating the stack instances in the specified
    # accounts and regions. If the stack set update does not include changes to
    # the template or parameters, AWS CloudFormation updates the stack instances
    # in the specified accounts and regions, while leaving all other stack
    # instances with their existing stack instance status.
    regions: typing.List[str] = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class UpdateStackSetOutput(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "operation_id",
                "OperationId",
                TypeInfo(str),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The unique ID for this stack set operation.
    operation_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class UpdateTerminationProtectionInput(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "enable_termination_protection",
                "EnableTerminationProtection",
                TypeInfo(bool),
            ),
            (
                "stack_name",
                "StackName",
                TypeInfo(str),
            ),
        ]

    # Whether to enable termination protection on the specified stack.
    enable_termination_protection: bool = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The name or unique ID of the stack for which you want to set termination
    # protection.
    stack_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class UpdateTerminationProtectionOutput(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "stack_id",
                "StackId",
                TypeInfo(str),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The unique ID of the stack.
    stack_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ValidateTemplateInput(ShapeBase):
    """
    The input for ValidateTemplate action.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "template_body",
                "TemplateBody",
                TypeInfo(str),
            ),
            (
                "template_url",
                "TemplateURL",
                TypeInfo(str),
            ),
        ]

    # Structure containing the template body with a minimum length of 1 byte and
    # a maximum length of 51,200 bytes. For more information, go to [Template
    # Anatomy](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/template-
    # anatomy.html) in the AWS CloudFormation User Guide.

    # Conditional: You must pass `TemplateURL` or `TemplateBody`. If both are
    # passed, only `TemplateBody` is used.
    template_body: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Location of file containing the template body. The URL must point to a
    # template (max size: 460,800 bytes) that is located in an Amazon S3 bucket.
    # For more information, go to [Template
    # Anatomy](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/template-
    # anatomy.html) in the AWS CloudFormation User Guide.

    # Conditional: You must pass `TemplateURL` or `TemplateBody`. If both are
    # passed, only `TemplateBody` is used.
    template_url: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ValidateTemplateOutput(OutputShapeBase):
    """
    The output for ValidateTemplate action.
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
                "parameters",
                "Parameters",
                TypeInfo(typing.List[TemplateParameter]),
            ),
            (
                "description",
                "Description",
                TypeInfo(str),
            ),
            (
                "capabilities",
                "Capabilities",
                TypeInfo(typing.List[typing.Union[str, Capability]]),
            ),
            (
                "capabilities_reason",
                "CapabilitiesReason",
                TypeInfo(str),
            ),
            (
                "declared_transforms",
                "DeclaredTransforms",
                TypeInfo(typing.List[str]),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A list of `TemplateParameter` structures.
    parameters: typing.List["TemplateParameter"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The description found within the template.
    description: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The capabilities found within the template. If your template contains IAM
    # resources, you must specify the CAPABILITY_IAM or CAPABILITY_NAMED_IAM
    # value for this parameter when you use the CreateStack or UpdateStack
    # actions with your template; otherwise, those actions return an
    # InsufficientCapabilities error.

    # For more information, see [Acknowledging IAM Resources in AWS
    # CloudFormation
    # Templates](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-
    # iam-template.html#capabilities).
    capabilities: typing.List[typing.Union[str, "Capability"]
                             ] = dataclasses.field(
                                 default=ShapeBase.NOT_SET,
                             )

    # The list of resources that generated the values in the `Capabilities`
    # response element.
    capabilities_reason: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A list of the transforms that are declared in the template.
    declared_transforms: typing.List[str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )
