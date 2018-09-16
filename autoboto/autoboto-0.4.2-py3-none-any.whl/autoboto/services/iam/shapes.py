import datetime
import typing
from autoboto import ShapeBase, OutputShapeBase, TypeInfo
import botocore.response
import dataclasses


@dataclasses.dataclass
class AccessKey(ShapeBase):
    """
    Contains information about an AWS access key.

    This data type is used as a response element in the CreateAccessKey and
    ListAccessKeys operations.

    The `SecretAccessKey` value is returned only in response to CreateAccessKey. You
    can get a secret access key only when you first create an access key; you cannot
    recover the secret access key later. If you lose a secret access key, you must
    create a new access key.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "user_name",
                "UserName",
                TypeInfo(str),
            ),
            (
                "access_key_id",
                "AccessKeyId",
                TypeInfo(str),
            ),
            (
                "status",
                "Status",
                TypeInfo(typing.Union[str, statusType]),
            ),
            (
                "secret_access_key",
                "SecretAccessKey",
                TypeInfo(str),
            ),
            (
                "create_date",
                "CreateDate",
                TypeInfo(datetime.datetime),
            ),
        ]

    # The name of the IAM user that the access key is associated with.
    user_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The ID for this access key.
    access_key_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The status of the access key. `Active` means that the key is valid for API
    # calls, while `Inactive` means it is not.
    status: typing.Union[str, "statusType"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The secret key used to sign requests.
    secret_access_key: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The date when the access key was created.
    create_date: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class AccessKeyLastUsed(ShapeBase):
    """
    Contains information about the last time an AWS access key was used.

    This data type is used as a response element in the GetAccessKeyLastUsed
    operation.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "last_used_date",
                "LastUsedDate",
                TypeInfo(datetime.datetime),
            ),
            (
                "service_name",
                "ServiceName",
                TypeInfo(str),
            ),
            (
                "region",
                "Region",
                TypeInfo(str),
            ),
        ]

    # The date and time, in [ISO 8601 date-time
    # format](http://www.iso.org/iso/iso8601), when the access key was most
    # recently used. This field is null in the following situations:

    #   * The user does not have an access key.

    #   * An access key exists but has never been used, at least not since IAM started tracking this information on April 22nd, 2015.

    #   * There is no sign-in data associated with the user
    last_used_date: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The name of the AWS service with which this access key was most recently
    # used. This field displays "N/A" in the following situations:

    #   * The user does not have an access key.

    #   * An access key exists but has never been used, at least not since IAM started tracking this information on April 22nd, 2015.

    #   * There is no sign-in data associated with the user
    service_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The AWS region where this access key was most recently used. This field is
    # displays "N/A" in the following situations:

    #   * The user does not have an access key.

    #   * An access key exists but has never been used, at least not since IAM started tracking this information on April 22nd, 2015.

    #   * There is no sign-in data associated with the user

    # For more information about AWS regions, see [Regions and
    # Endpoints](http://docs.aws.amazon.com/general/latest/gr/rande.html) in the
    # Amazon Web Services General Reference.
    region: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class AccessKeyMetadata(ShapeBase):
    """
    Contains information about an AWS access key, without its secret key.

    This data type is used as a response element in the ListAccessKeys operation.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "user_name",
                "UserName",
                TypeInfo(str),
            ),
            (
                "access_key_id",
                "AccessKeyId",
                TypeInfo(str),
            ),
            (
                "status",
                "Status",
                TypeInfo(typing.Union[str, statusType]),
            ),
            (
                "create_date",
                "CreateDate",
                TypeInfo(datetime.datetime),
            ),
        ]

    # The name of the IAM user that the key is associated with.
    user_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The ID for this access key.
    access_key_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The status of the access key. `Active` means the key is valid for API
    # calls; `Inactive` means it is not.
    status: typing.Union[str, "statusType"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The date when the access key was created.
    create_date: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class AddClientIDToOpenIDConnectProviderRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "open_id_connect_provider_arn",
                "OpenIDConnectProviderArn",
                TypeInfo(str),
            ),
            (
                "client_id",
                "ClientID",
                TypeInfo(str),
            ),
        ]

    # The Amazon Resource Name (ARN) of the IAM OpenID Connect (OIDC) provider
    # resource to add the client ID to. You can get a list of OIDC provider ARNs
    # by using the ListOpenIDConnectProviders operation.
    open_id_connect_provider_arn: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The client ID (also known as audience) to add to the IAM OpenID Connect
    # provider resource.
    client_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class AddRoleToInstanceProfileRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "instance_profile_name",
                "InstanceProfileName",
                TypeInfo(str),
            ),
            (
                "role_name",
                "RoleName",
                TypeInfo(str),
            ),
        ]

    # The name of the instance profile to update.

    # This parameter allows (per its [regex
    # pattern](http://wikipedia.org/wiki/regex)) a string of characters
    # consisting of upper and lowercase alphanumeric characters with no spaces.
    # You can also include any of the following characters: _+=,.@-
    instance_profile_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The name of the role to add.

    # This parameter allows (per its [regex
    # pattern](http://wikipedia.org/wiki/regex)) a string of characters
    # consisting of upper and lowercase alphanumeric characters with no spaces.
    # You can also include any of the following characters: _+=,.@-
    role_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class AddUserToGroupRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "group_name",
                "GroupName",
                TypeInfo(str),
            ),
            (
                "user_name",
                "UserName",
                TypeInfo(str),
            ),
        ]

    # The name of the group to update.

    # This parameter allows (per its [regex
    # pattern](http://wikipedia.org/wiki/regex)) a string of characters
    # consisting of upper and lowercase alphanumeric characters with no spaces.
    # You can also include any of the following characters: _+=,.@-
    group_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The name of the user to add.

    # This parameter allows (per its [regex
    # pattern](http://wikipedia.org/wiki/regex)) a string of characters
    # consisting of upper and lowercase alphanumeric characters with no spaces.
    # You can also include any of the following characters: _+=,.@-
    user_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class AttachGroupPolicyRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "group_name",
                "GroupName",
                TypeInfo(str),
            ),
            (
                "policy_arn",
                "PolicyArn",
                TypeInfo(str),
            ),
        ]

    # The name (friendly name, not ARN) of the group to attach the policy to.

    # This parameter allows (per its [regex
    # pattern](http://wikipedia.org/wiki/regex)) a string of characters
    # consisting of upper and lowercase alphanumeric characters with no spaces.
    # You can also include any of the following characters: _+=,.@-
    group_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The Amazon Resource Name (ARN) of the IAM policy you want to attach.

    # For more information about ARNs, see [Amazon Resource Names (ARNs) and AWS
    # Service Namespaces](http://docs.aws.amazon.com/general/latest/gr/aws-arns-
    # and-namespaces.html) in the _AWS General Reference_.
    policy_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class AttachRolePolicyRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "role_name",
                "RoleName",
                TypeInfo(str),
            ),
            (
                "policy_arn",
                "PolicyArn",
                TypeInfo(str),
            ),
        ]

    # The name (friendly name, not ARN) of the role to attach the policy to.

    # This parameter allows (per its [regex
    # pattern](http://wikipedia.org/wiki/regex)) a string of characters
    # consisting of upper and lowercase alphanumeric characters with no spaces.
    # You can also include any of the following characters: _+=,.@-
    role_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The Amazon Resource Name (ARN) of the IAM policy you want to attach.

    # For more information about ARNs, see [Amazon Resource Names (ARNs) and AWS
    # Service Namespaces](http://docs.aws.amazon.com/general/latest/gr/aws-arns-
    # and-namespaces.html) in the _AWS General Reference_.
    policy_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class AttachUserPolicyRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "user_name",
                "UserName",
                TypeInfo(str),
            ),
            (
                "policy_arn",
                "PolicyArn",
                TypeInfo(str),
            ),
        ]

    # The name (friendly name, not ARN) of the IAM user to attach the policy to.

    # This parameter allows (per its [regex
    # pattern](http://wikipedia.org/wiki/regex)) a string of characters
    # consisting of upper and lowercase alphanumeric characters with no spaces.
    # You can also include any of the following characters: _+=,.@-
    user_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The Amazon Resource Name (ARN) of the IAM policy you want to attach.

    # For more information about ARNs, see [Amazon Resource Names (ARNs) and AWS
    # Service Namespaces](http://docs.aws.amazon.com/general/latest/gr/aws-arns-
    # and-namespaces.html) in the _AWS General Reference_.
    policy_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class AttachedPermissionsBoundary(ShapeBase):
    """
    Contains information about an attached permissions boundary.

    An attached permissions boundary is a managed policy that has been attached to a
    user or role to set the permissions boundary.

    For more information about permissions boundaries, see [Permissions Boundaries
    for IAM Identities
    ](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_boundaries.html)
    in the _IAM User Guide_.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "permissions_boundary_type",
                "PermissionsBoundaryType",
                TypeInfo(typing.Union[str, PermissionsBoundaryAttachmentType]),
            ),
            (
                "permissions_boundary_arn",
                "PermissionsBoundaryArn",
                TypeInfo(str),
            ),
        ]

    # The permissions boundary usage type that indicates what type of IAM
    # resource is used as the permissions boundary for an entity. This data type
    # can only have a value of `Policy`.
    permissions_boundary_type: typing.Union[
        str, "PermissionsBoundaryAttachmentType"] = dataclasses.field(
            default=ShapeBase.NOT_SET,
        )

    # The ARN of the policy used to set the permissions boundary for the user or
    # role.
    permissions_boundary_arn: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class AttachedPolicy(ShapeBase):
    """
    Contains information about an attached policy.

    An attached policy is a managed policy that has been attached to a user, group,
    or role. This data type is used as a response element in the
    ListAttachedGroupPolicies, ListAttachedRolePolicies, ListAttachedUserPolicies,
    and GetAccountAuthorizationDetails operations.

    For more information about managed policies, refer to [Managed Policies and
    Inline Policies](http://docs.aws.amazon.com/IAM/latest/UserGuide/policies-
    managed-vs-inline.html) in the _Using IAM_ guide.
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
                "policy_arn",
                "PolicyArn",
                TypeInfo(str),
            ),
        ]

    # The friendly name of the attached policy.
    policy_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The Amazon Resource Name (ARN). ARNs are unique identifiers for AWS
    # resources.

    # For more information about ARNs, go to [Amazon Resource Names (ARNs) and
    # AWS Service Namespaces](http://docs.aws.amazon.com/general/latest/gr/aws-
    # arns-and-namespaces.html) in the _AWS General Reference_.
    policy_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )


class BootstrapDatum(botocore.response.StreamingBody):
    pass


@dataclasses.dataclass
class ChangePasswordRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "old_password",
                "OldPassword",
                TypeInfo(str),
            ),
            (
                "new_password",
                "NewPassword",
                TypeInfo(str),
            ),
        ]

    # The IAM user's current password.
    old_password: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The new password. The new password must conform to the AWS account's
    # password policy, if one exists.

    # The [regex pattern](http://wikipedia.org/wiki/regex) that is used to
    # validate this parameter is a string of characters. That string can include
    # almost any printable ASCII character from the space (\u0020) through the
    # end of the ASCII character range (\u00FF). You can also include the tab
    # (\u0009), line feed (\u000A), and carriage return (\u000D) characters. Any
    # of these characters are valid in a password. However, many tools, such as
    # the AWS Management Console, might restrict the ability to type certain
    # characters because they have special meaning within that tool.
    new_password: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ContextEntry(ShapeBase):
    """
    Contains information about a condition context key. It includes the name of the
    key and specifies the value (or values, if the context key supports multiple
    values) to use in the simulation. This information is used when evaluating the
    `Condition` elements of the input policies.

    This data type is used as an input parameter to ` SimulateCustomPolicy ` and `
    SimulateCustomPolicy `.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "context_key_name",
                "ContextKeyName",
                TypeInfo(str),
            ),
            (
                "context_key_values",
                "ContextKeyValues",
                TypeInfo(typing.List[str]),
            ),
            (
                "context_key_type",
                "ContextKeyType",
                TypeInfo(typing.Union[str, ContextKeyTypeEnum]),
            ),
        ]

    # The full name of a condition context key, including the service prefix. For
    # example, `aws:SourceIp` or `s3:VersionId`.
    context_key_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The value (or values, if the condition context key supports multiple
    # values) to provide to the simulation when the key is referenced by a
    # `Condition` element in an input policy.
    context_key_values: typing.List[str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The data type of the value (or values) specified in the `ContextKeyValues`
    # parameter.
    context_key_type: typing.Union[str, "ContextKeyTypeEnum"
                                  ] = dataclasses.field(
                                      default=ShapeBase.NOT_SET,
                                  )


class ContextKeyTypeEnum(str):
    string = "string"
    stringList = "stringList"
    numeric = "numeric"
    numericList = "numericList"
    boolean = "boolean"
    booleanList = "booleanList"
    ip = "ip"
    ipList = "ipList"
    binary = "binary"
    binaryList = "binaryList"
    date = "date"
    dateList = "dateList"


@dataclasses.dataclass
class CreateAccessKeyRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "user_name",
                "UserName",
                TypeInfo(str),
            ),
        ]

    # The name of the IAM user that the new key will belong to.

    # This parameter allows (per its [regex
    # pattern](http://wikipedia.org/wiki/regex)) a string of characters
    # consisting of upper and lowercase alphanumeric characters with no spaces.
    # You can also include any of the following characters: _+=,.@-
    user_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class CreateAccessKeyResponse(OutputShapeBase):
    """
    Contains the response to a successful CreateAccessKey request.
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
                "access_key",
                "AccessKey",
                TypeInfo(AccessKey),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A structure with details about the access key.
    access_key: "AccessKey" = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class CreateAccountAliasRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "account_alias",
                "AccountAlias",
                TypeInfo(str),
            ),
        ]

    # The account alias to create.

    # This parameter allows (per its [regex
    # pattern](http://wikipedia.org/wiki/regex)) a string of characters
    # consisting of lowercase letters, digits, and dashes. You cannot start or
    # finish with a dash, nor can you have two dashes in a row.
    account_alias: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class CreateGroupRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "group_name",
                "GroupName",
                TypeInfo(str),
            ),
            (
                "path",
                "Path",
                TypeInfo(str),
            ),
        ]

    # The name of the group to create. Do not include the path in this value.

    # This parameter allows (per its [regex
    # pattern](http://wikipedia.org/wiki/regex)) a string of characters
    # consisting of upper and lowercase alphanumeric characters with no spaces.
    # You can also include any of the following characters: _+=,.@-. The group
    # name must be unique within the account. Group names are not distinguished
    # by case. For example, you cannot create groups named both "ADMINS" and
    # "admins".
    group_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The path to the group. For more information about paths, see [IAM
    # Identifiers](http://docs.aws.amazon.com/IAM/latest/UserGuide/Using_Identifiers.html)
    # in the _IAM User Guide_.

    # This parameter is optional. If it is not included, it defaults to a slash
    # (/).

    # This parameter allows (per its [regex
    # pattern](http://wikipedia.org/wiki/regex)) a string of characters
    # consisting of either a forward slash (/) by itself or a string that must
    # begin and end with forward slashes. In addition, it can contain any ASCII
    # character from the ! (\u0021) through the DEL character (\u007F), including
    # most punctuation characters, digits, and upper and lowercased letters.
    path: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class CreateGroupResponse(OutputShapeBase):
    """
    Contains the response to a successful CreateGroup request.
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
                "group",
                "Group",
                TypeInfo(Group),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A structure containing details about the new group.
    group: "Group" = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class CreateInstanceProfileRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "instance_profile_name",
                "InstanceProfileName",
                TypeInfo(str),
            ),
            (
                "path",
                "Path",
                TypeInfo(str),
            ),
        ]

    # The name of the instance profile to create.

    # This parameter allows (per its [regex
    # pattern](http://wikipedia.org/wiki/regex)) a string of characters
    # consisting of upper and lowercase alphanumeric characters with no spaces.
    # You can also include any of the following characters: _+=,.@-
    instance_profile_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The path to the instance profile. For more information about paths, see
    # [IAM
    # Identifiers](http://docs.aws.amazon.com/IAM/latest/UserGuide/Using_Identifiers.html)
    # in the _IAM User Guide_.

    # This parameter is optional. If it is not included, it defaults to a slash
    # (/).

    # This parameter allows (per its [regex
    # pattern](http://wikipedia.org/wiki/regex)) a string of characters
    # consisting of either a forward slash (/) by itself or a string that must
    # begin and end with forward slashes. In addition, it can contain any ASCII
    # character from the ! (\u0021) through the DEL character (\u007F), including
    # most punctuation characters, digits, and upper and lowercased letters.
    path: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class CreateInstanceProfileResponse(OutputShapeBase):
    """
    Contains the response to a successful CreateInstanceProfile request.
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
                "instance_profile",
                "InstanceProfile",
                TypeInfo(InstanceProfile),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A structure containing details about the new instance profile.
    instance_profile: "InstanceProfile" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class CreateLoginProfileRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "user_name",
                "UserName",
                TypeInfo(str),
            ),
            (
                "password",
                "Password",
                TypeInfo(str),
            ),
            (
                "password_reset_required",
                "PasswordResetRequired",
                TypeInfo(bool),
            ),
        ]

    # The name of the IAM user to create a password for. The user must already
    # exist.

    # This parameter allows (per its [regex
    # pattern](http://wikipedia.org/wiki/regex)) a string of characters
    # consisting of upper and lowercase alphanumeric characters with no spaces.
    # You can also include any of the following characters: _+=,.@-
    user_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The new password for the user.

    # The [regex pattern](http://wikipedia.org/wiki/regex) that is used to
    # validate this parameter is a string of characters. That string can include
    # almost any printable ASCII character from the space (\u0020) through the
    # end of the ASCII character range (\u00FF). You can also include the tab
    # (\u0009), line feed (\u000A), and carriage return (\u000D) characters. Any
    # of these characters are valid in a password. However, many tools, such as
    # the AWS Management Console, might restrict the ability to type certain
    # characters because they have special meaning within that tool.
    password: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Specifies whether the user is required to set a new password on next sign-
    # in.
    password_reset_required: bool = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class CreateLoginProfileResponse(OutputShapeBase):
    """
    Contains the response to a successful CreateLoginProfile request.
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
                "login_profile",
                "LoginProfile",
                TypeInfo(LoginProfile),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A structure containing the user name and password create date.
    login_profile: "LoginProfile" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class CreateOpenIDConnectProviderRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "url",
                "Url",
                TypeInfo(str),
            ),
            (
                "thumbprint_list",
                "ThumbprintList",
                TypeInfo(typing.List[str]),
            ),
            (
                "client_id_list",
                "ClientIDList",
                TypeInfo(typing.List[str]),
            ),
        ]

    # The URL of the identity provider. The URL must begin with `https://` and
    # should correspond to the `iss` claim in the provider's OpenID Connect ID
    # tokens. Per the OIDC standard, path components are allowed but query
    # parameters are not. Typically the URL consists of only a hostname, like
    # `https://server.example.org` or `https://example.com`.

    # You cannot register the same provider multiple times in a single AWS
    # account. If you try to submit a URL that has already been used for an
    # OpenID Connect provider in the AWS account, you will get an error.
    url: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A list of server certificate thumbprints for the OpenID Connect (OIDC)
    # identity provider's server certificates. Typically this list includes only
    # one entry. However, IAM lets you have up to five thumbprints for an OIDC
    # provider. This lets you maintain multiple thumbprints if the identity
    # provider is rotating certificates.

    # The server certificate thumbprint is the hex-encoded SHA-1 hash value of
    # the X.509 certificate used by the domain where the OpenID Connect provider
    # makes its keys available. It is always a 40-character string.

    # You must provide at least one thumbprint when creating an IAM OIDC
    # provider. For example, assume that the OIDC provider is
    # `server.example.com` and the provider stores its keys at
    # https://keys.server.example.com/openid-connect. In that case, the
    # thumbprint string would be the hex-encoded SHA-1 hash value of the
    # certificate used by https://keys.server.example.com.

    # For more information about obtaining the OIDC provider's thumbprint, see
    # [Obtaining the Thumbprint for an OpenID Connect
    # Provider](http://docs.aws.amazon.com/IAM/latest/UserGuide/identity-
    # providers-oidc-obtain-thumbprint.html) in the _IAM User Guide_.
    thumbprint_list: typing.List[str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A list of client IDs (also known as audiences). When a mobile or web app
    # registers with an OpenID Connect provider, they establish a value that
    # identifies the application. (This is the value that's sent as the
    # `client_id` parameter on OAuth requests.)

    # You can register multiple client IDs with the same provider. For example,
    # you might have multiple applications that use the same OIDC provider. You
    # cannot register more than 100 client IDs with a single IAM OIDC provider.

    # There is no defined format for a client ID. The
    # `CreateOpenIDConnectProviderRequest` operation accepts client IDs up to 255
    # characters long.
    client_id_list: typing.List[str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class CreateOpenIDConnectProviderResponse(OutputShapeBase):
    """
    Contains the response to a successful CreateOpenIDConnectProvider request.
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
                "open_id_connect_provider_arn",
                "OpenIDConnectProviderArn",
                TypeInfo(str),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The Amazon Resource Name (ARN) of the new IAM OpenID Connect provider that
    # is created. For more information, see OpenIDConnectProviderListEntry.
    open_id_connect_provider_arn: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class CreatePolicyRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "policy_name",
                "PolicyName",
                TypeInfo(str),
            ),
            (
                "policy_document",
                "PolicyDocument",
                TypeInfo(str),
            ),
            (
                "path",
                "Path",
                TypeInfo(str),
            ),
            (
                "description",
                "Description",
                TypeInfo(str),
            ),
        ]

    # The friendly name of the policy.

    # This parameter allows (per its [regex
    # pattern](http://wikipedia.org/wiki/regex)) a string of characters
    # consisting of upper and lowercase alphanumeric characters with no spaces.
    # You can also include any of the following characters: _+=,.@-
    policy_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The JSON policy document that you want to use as the content for the new
    # policy.

    # The [regex pattern](http://wikipedia.org/wiki/regex) used to validate this
    # parameter is a string of characters consisting of the following:

    #   * Any printable ASCII character ranging from the space character (\u0020) through the end of the ASCII character range

    #   * The printable characters in the Basic Latin and Latin-1 Supplement character set (through \u00FF)

    #   * The special characters tab (\u0009), line feed (\u000A), and carriage return (\u000D)
    policy_document: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The path for the policy.

    # For more information about paths, see [IAM
    # Identifiers](http://docs.aws.amazon.com/IAM/latest/UserGuide/Using_Identifiers.html)
    # in the _IAM User Guide_.

    # This parameter is optional. If it is not included, it defaults to a slash
    # (/).

    # This parameter allows (per its [regex
    # pattern](http://wikipedia.org/wiki/regex)) a string of characters
    # consisting of either a forward slash (/) by itself or a string that must
    # begin and end with forward slashes. In addition, it can contain any ASCII
    # character from the ! (\u0021) through the DEL character (\u007F), including
    # most punctuation characters, digits, and upper and lowercased letters.
    path: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A friendly description of the policy.

    # Typically used to store information about the permissions defined in the
    # policy. For example, "Grants access to production DynamoDB tables."

    # The policy description is immutable. After a value is assigned, it cannot
    # be changed.
    description: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class CreatePolicyResponse(OutputShapeBase):
    """
    Contains the response to a successful CreatePolicy request.
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
                "policy",
                "Policy",
                TypeInfo(Policy),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A structure containing details about the new policy.
    policy: "Policy" = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class CreatePolicyVersionRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "policy_arn",
                "PolicyArn",
                TypeInfo(str),
            ),
            (
                "policy_document",
                "PolicyDocument",
                TypeInfo(str),
            ),
            (
                "set_as_default",
                "SetAsDefault",
                TypeInfo(bool),
            ),
        ]

    # The Amazon Resource Name (ARN) of the IAM policy to which you want to add a
    # new version.

    # For more information about ARNs, see [Amazon Resource Names (ARNs) and AWS
    # Service Namespaces](http://docs.aws.amazon.com/general/latest/gr/aws-arns-
    # and-namespaces.html) in the _AWS General Reference_.
    policy_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The JSON policy document that you want to use as the content for this new
    # version of the policy.

    # The [regex pattern](http://wikipedia.org/wiki/regex) used to validate this
    # parameter is a string of characters consisting of the following:

    #   * Any printable ASCII character ranging from the space character (\u0020) through the end of the ASCII character range

    #   * The printable characters in the Basic Latin and Latin-1 Supplement character set (through \u00FF)

    #   * The special characters tab (\u0009), line feed (\u000A), and carriage return (\u000D)
    policy_document: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Specifies whether to set this version as the policy's default version.

    # When this parameter is `true`, the new policy version becomes the operative
    # version. That is, it becomes the version that is in effect for the IAM
    # users, groups, and roles that the policy is attached to.

    # For more information about managed policy versions, see [Versioning for
    # Managed Policies](http://docs.aws.amazon.com/IAM/latest/UserGuide/policies-
    # managed-versions.html) in the _IAM User Guide_.
    set_as_default: bool = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class CreatePolicyVersionResponse(OutputShapeBase):
    """
    Contains the response to a successful CreatePolicyVersion request.
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
                "policy_version",
                "PolicyVersion",
                TypeInfo(PolicyVersion),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A structure containing details about the new policy version.
    policy_version: "PolicyVersion" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class CreateRoleRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "role_name",
                "RoleName",
                TypeInfo(str),
            ),
            (
                "assume_role_policy_document",
                "AssumeRolePolicyDocument",
                TypeInfo(str),
            ),
            (
                "path",
                "Path",
                TypeInfo(str),
            ),
            (
                "description",
                "Description",
                TypeInfo(str),
            ),
            (
                "max_session_duration",
                "MaxSessionDuration",
                TypeInfo(int),
            ),
            (
                "permissions_boundary",
                "PermissionsBoundary",
                TypeInfo(str),
            ),
        ]

    # The name of the role to create.

    # This parameter allows (per its [regex
    # pattern](http://wikipedia.org/wiki/regex)) a string of characters
    # consisting of upper and lowercase alphanumeric characters with no spaces.
    # You can also include any of the following characters: _+=,.@-

    # Role names are not distinguished by case. For example, you cannot create
    # roles named both "PRODROLE" and "prodrole".
    role_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The trust relationship policy document that grants an entity permission to
    # assume the role.

    # The [regex pattern](http://wikipedia.org/wiki/regex) used to validate this
    # parameter is a string of characters consisting of the following:

    #   * Any printable ASCII character ranging from the space character (\u0020) through the end of the ASCII character range

    #   * The printable characters in the Basic Latin and Latin-1 Supplement character set (through \u00FF)

    #   * The special characters tab (\u0009), line feed (\u000A), and carriage return (\u000D)
    assume_role_policy_document: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The path to the role. For more information about paths, see [IAM
    # Identifiers](http://docs.aws.amazon.com/IAM/latest/UserGuide/Using_Identifiers.html)
    # in the _IAM User Guide_.

    # This parameter is optional. If it is not included, it defaults to a slash
    # (/).

    # This parameter allows (per its [regex
    # pattern](http://wikipedia.org/wiki/regex)) a string of characters
    # consisting of either a forward slash (/) by itself or a string that must
    # begin and end with forward slashes. In addition, it can contain any ASCII
    # character from the ! (\u0021) through the DEL character (\u007F), including
    # most punctuation characters, digits, and upper and lowercased letters.
    path: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A description of the role.
    description: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The maximum session duration (in seconds) that you want to set for the
    # specified role. If you do not specify a value for this setting, the default
    # maximum of one hour is applied. This setting can have a value from 1 hour
    # to 12 hours.

    # Anyone who assumes the role from the AWS CLI or API can use the
    # `DurationSeconds` API parameter or the `duration-seconds` CLI parameter to
    # request a longer session. The `MaxSessionDuration` setting determines the
    # maximum duration that can be requested using the `DurationSeconds`
    # parameter. If users don't specify a value for the `DurationSeconds`
    # parameter, their security credentials are valid for one hour by default.
    # This applies when you use the `AssumeRole*` API operations or the `assume-
    # role*` CLI operations but does not apply when you use those operations to
    # create a console URL. For more information, see [Using IAM
    # Roles](http://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use.html)
    # in the _IAM User Guide_.
    max_session_duration: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The ARN of the policy that is used to set the permissions boundary for the
    # role.
    permissions_boundary: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class CreateRoleResponse(OutputShapeBase):
    """
    Contains the response to a successful CreateRole request.
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
                "role",
                "Role",
                TypeInfo(Role),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A structure containing details about the new role.
    role: "Role" = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class CreateSAMLProviderRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "saml_metadata_document",
                "SAMLMetadataDocument",
                TypeInfo(str),
            ),
            (
                "name",
                "Name",
                TypeInfo(str),
            ),
        ]

    # An XML document generated by an identity provider (IdP) that supports SAML
    # 2.0. The document includes the issuer's name, expiration information, and
    # keys that can be used to validate the SAML authentication response
    # (assertions) that are received from the IdP. You must generate the metadata
    # document using the identity management software that is used as your
    # organization's IdP.

    # For more information, see [About SAML 2.0-based
    # Federation](http://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_providers_saml.html)
    # in the _IAM User Guide_
    saml_metadata_document: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The name of the provider to create.

    # This parameter allows (per its [regex
    # pattern](http://wikipedia.org/wiki/regex)) a string of characters
    # consisting of upper and lowercase alphanumeric characters with no spaces.
    # You can also include any of the following characters: _+=,.@-
    name: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class CreateSAMLProviderResponse(OutputShapeBase):
    """
    Contains the response to a successful CreateSAMLProvider request.
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
                "saml_provider_arn",
                "SAMLProviderArn",
                TypeInfo(str),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The Amazon Resource Name (ARN) of the new SAML provider resource in IAM.
    saml_provider_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class CreateServiceLinkedRoleRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "aws_service_name",
                "AWSServiceName",
                TypeInfo(str),
            ),
            (
                "description",
                "Description",
                TypeInfo(str),
            ),
            (
                "custom_suffix",
                "CustomSuffix",
                TypeInfo(str),
            ),
        ]

    # The AWS service to which this role is attached. You use a string similar to
    # a URL but without the http:// in front. For example:
    # `elasticbeanstalk.amazonaws.com`
    aws_service_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The description of the role.
    description: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A string that you provide, which is combined with the service name to form
    # the complete role name. If you make multiple requests for the same service,
    # then you must supply a different `CustomSuffix` for each request. Otherwise
    # the request fails with a duplicate role name error. For example, you could
    # add `-1` or `-debug` to the suffix.
    custom_suffix: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class CreateServiceLinkedRoleResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "role",
                "Role",
                TypeInfo(Role),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A Role object that contains details about the newly created role.
    role: "Role" = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class CreateServiceSpecificCredentialRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "user_name",
                "UserName",
                TypeInfo(str),
            ),
            (
                "service_name",
                "ServiceName",
                TypeInfo(str),
            ),
        ]

    # The name of the IAM user that is to be associated with the credentials. The
    # new service-specific credentials have the same permissions as the
    # associated user except that they can be used only to access the specified
    # service.

    # This parameter allows (per its [regex
    # pattern](http://wikipedia.org/wiki/regex)) a string of characters
    # consisting of upper and lowercase alphanumeric characters with no spaces.
    # You can also include any of the following characters: _+=,.@-
    user_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The name of the AWS service that is to be associated with the credentials.
    # The service you specify here is the only service that can be accessed using
    # these credentials.
    service_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class CreateServiceSpecificCredentialResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "service_specific_credential",
                "ServiceSpecificCredential",
                TypeInfo(ServiceSpecificCredential),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A structure that contains information about the newly created service-
    # specific credential.

    # This is the only time that the password for this credential set is
    # available. It cannot be recovered later. Instead, you will have to reset
    # the password with ResetServiceSpecificCredential.
    service_specific_credential: "ServiceSpecificCredential" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class CreateUserRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "user_name",
                "UserName",
                TypeInfo(str),
            ),
            (
                "path",
                "Path",
                TypeInfo(str),
            ),
            (
                "permissions_boundary",
                "PermissionsBoundary",
                TypeInfo(str),
            ),
        ]

    # The name of the user to create.

    # This parameter allows (per its [regex
    # pattern](http://wikipedia.org/wiki/regex)) a string of characters
    # consisting of upper and lowercase alphanumeric characters with no spaces.
    # You can also include any of the following characters: _+=,.@-. User names
    # are not distinguished by case. For example, you cannot create users named
    # both "TESTUSER" and "testuser".
    user_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The path for the user name. For more information about paths, see [IAM
    # Identifiers](http://docs.aws.amazon.com/IAM/latest/UserGuide/Using_Identifiers.html)
    # in the _IAM User Guide_.

    # This parameter is optional. If it is not included, it defaults to a slash
    # (/).

    # This parameter allows (per its [regex
    # pattern](http://wikipedia.org/wiki/regex)) a string of characters
    # consisting of either a forward slash (/) by itself or a string that must
    # begin and end with forward slashes. In addition, it can contain any ASCII
    # character from the ! (\u0021) through the DEL character (\u007F), including
    # most punctuation characters, digits, and upper and lowercased letters.
    path: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The ARN of the policy that is used to set the permissions boundary for the
    # user.
    permissions_boundary: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class CreateUserResponse(OutputShapeBase):
    """
    Contains the response to a successful CreateUser request.
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
                "user",
                "User",
                TypeInfo(User),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A structure with details about the new IAM user.
    user: "User" = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class CreateVirtualMFADeviceRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "virtual_mfa_device_name",
                "VirtualMFADeviceName",
                TypeInfo(str),
            ),
            (
                "path",
                "Path",
                TypeInfo(str),
            ),
        ]

    # The name of the virtual MFA device. Use with path to uniquely identify a
    # virtual MFA device.

    # This parameter allows (per its [regex
    # pattern](http://wikipedia.org/wiki/regex)) a string of characters
    # consisting of upper and lowercase alphanumeric characters with no spaces.
    # You can also include any of the following characters: _+=,.@-
    virtual_mfa_device_name: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The path for the virtual MFA device. For more information about paths, see
    # [IAM
    # Identifiers](http://docs.aws.amazon.com/IAM/latest/UserGuide/Using_Identifiers.html)
    # in the _IAM User Guide_.

    # This parameter is optional. If it is not included, it defaults to a slash
    # (/).

    # This parameter allows (per its [regex
    # pattern](http://wikipedia.org/wiki/regex)) a string of characters
    # consisting of either a forward slash (/) by itself or a string that must
    # begin and end with forward slashes. In addition, it can contain any ASCII
    # character from the ! (\u0021) through the DEL character (\u007F), including
    # most punctuation characters, digits, and upper and lowercased letters.
    path: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class CreateVirtualMFADeviceResponse(OutputShapeBase):
    """
    Contains the response to a successful CreateVirtualMFADevice request.
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
                "virtual_mfa_device",
                "VirtualMFADevice",
                TypeInfo(VirtualMFADevice),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A structure containing details about the new virtual MFA device.
    virtual_mfa_device: "VirtualMFADevice" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class CredentialReportExpiredException(ShapeBase):
    """
    The request was rejected because the most recent credential report has expired.
    To generate a new credential report, use GenerateCredentialReport. For more
    information about credential report expiration, see [Getting Credential
    Reports](http://docs.aws.amazon.com/IAM/latest/UserGuide/credential-
    reports.html) in the _IAM User Guide_.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "message",
                "message",
                TypeInfo(str),
            ),
        ]

    message: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class CredentialReportNotPresentException(ShapeBase):
    """
    The request was rejected because the credential report does not exist. To
    generate a credential report, use GenerateCredentialReport.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "message",
                "message",
                TypeInfo(str),
            ),
        ]

    message: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class CredentialReportNotReadyException(ShapeBase):
    """
    The request was rejected because the credential report is still being generated.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "message",
                "message",
                TypeInfo(str),
            ),
        ]

    message: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DeactivateMFADeviceRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "user_name",
                "UserName",
                TypeInfo(str),
            ),
            (
                "serial_number",
                "SerialNumber",
                TypeInfo(str),
            ),
        ]

    # The name of the user whose MFA device you want to deactivate.

    # This parameter allows (per its [regex
    # pattern](http://wikipedia.org/wiki/regex)) a string of characters
    # consisting of upper and lowercase alphanumeric characters with no spaces.
    # You can also include any of the following characters: _+=,.@-
    user_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The serial number that uniquely identifies the MFA device. For virtual MFA
    # devices, the serial number is the device ARN.

    # This parameter allows (per its [regex
    # pattern](http://wikipedia.org/wiki/regex)) a string of characters
    # consisting of upper and lowercase alphanumeric characters with no spaces.
    # You can also include any of the following characters: =,.@:/-
    serial_number: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DeleteAccessKeyRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "access_key_id",
                "AccessKeyId",
                TypeInfo(str),
            ),
            (
                "user_name",
                "UserName",
                TypeInfo(str),
            ),
        ]

    # The access key ID for the access key ID and secret access key you want to
    # delete.

    # This parameter allows (per its [regex
    # pattern](http://wikipedia.org/wiki/regex)) a string of characters that can
    # consist of any upper or lowercased letter or digit.
    access_key_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The name of the user whose access key pair you want to delete.

    # This parameter allows (per its [regex
    # pattern](http://wikipedia.org/wiki/regex)) a string of characters
    # consisting of upper and lowercase alphanumeric characters with no spaces.
    # You can also include any of the following characters: _+=,.@-
    user_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DeleteAccountAliasRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "account_alias",
                "AccountAlias",
                TypeInfo(str),
            ),
        ]

    # The name of the account alias to delete.

    # This parameter allows (per its [regex
    # pattern](http://wikipedia.org/wiki/regex)) a string of characters
    # consisting of lowercase letters, digits, and dashes. You cannot start or
    # finish with a dash, nor can you have two dashes in a row.
    account_alias: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DeleteConflictException(ShapeBase):
    """
    The request was rejected because it attempted to delete a resource that has
    attached subordinate entities. The error message describes these entities.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "message",
                "message",
                TypeInfo(str),
            ),
        ]

    message: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DeleteGroupPolicyRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "group_name",
                "GroupName",
                TypeInfo(str),
            ),
            (
                "policy_name",
                "PolicyName",
                TypeInfo(str),
            ),
        ]

    # The name (friendly name, not ARN) identifying the group that the policy is
    # embedded in.

    # This parameter allows (per its [regex
    # pattern](http://wikipedia.org/wiki/regex)) a string of characters
    # consisting of upper and lowercase alphanumeric characters with no spaces.
    # You can also include any of the following characters: _+=,.@-
    group_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The name identifying the policy document to delete.

    # This parameter allows (per its [regex
    # pattern](http://wikipedia.org/wiki/regex)) a string of characters
    # consisting of upper and lowercase alphanumeric characters with no spaces.
    # You can also include any of the following characters: _+=,.@-
    policy_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DeleteGroupRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "group_name",
                "GroupName",
                TypeInfo(str),
            ),
        ]

    # The name of the IAM group to delete.

    # This parameter allows (per its [regex
    # pattern](http://wikipedia.org/wiki/regex)) a string of characters
    # consisting of upper and lowercase alphanumeric characters with no spaces.
    # You can also include any of the following characters: _+=,.@-
    group_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DeleteInstanceProfileRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "instance_profile_name",
                "InstanceProfileName",
                TypeInfo(str),
            ),
        ]

    # The name of the instance profile to delete.

    # This parameter allows (per its [regex
    # pattern](http://wikipedia.org/wiki/regex)) a string of characters
    # consisting of upper and lowercase alphanumeric characters with no spaces.
    # You can also include any of the following characters: _+=,.@-
    instance_profile_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DeleteLoginProfileRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "user_name",
                "UserName",
                TypeInfo(str),
            ),
        ]

    # The name of the user whose password you want to delete.

    # This parameter allows (per its [regex
    # pattern](http://wikipedia.org/wiki/regex)) a string of characters
    # consisting of upper and lowercase alphanumeric characters with no spaces.
    # You can also include any of the following characters: _+=,.@-
    user_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DeleteOpenIDConnectProviderRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "open_id_connect_provider_arn",
                "OpenIDConnectProviderArn",
                TypeInfo(str),
            ),
        ]

    # The Amazon Resource Name (ARN) of the IAM OpenID Connect provider resource
    # object to delete. You can get a list of OpenID Connect provider resource
    # ARNs by using the ListOpenIDConnectProviders operation.
    open_id_connect_provider_arn: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class DeletePolicyRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "policy_arn",
                "PolicyArn",
                TypeInfo(str),
            ),
        ]

    # The Amazon Resource Name (ARN) of the IAM policy you want to delete.

    # For more information about ARNs, see [Amazon Resource Names (ARNs) and AWS
    # Service Namespaces](http://docs.aws.amazon.com/general/latest/gr/aws-arns-
    # and-namespaces.html) in the _AWS General Reference_.
    policy_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DeletePolicyVersionRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "policy_arn",
                "PolicyArn",
                TypeInfo(str),
            ),
            (
                "version_id",
                "VersionId",
                TypeInfo(str),
            ),
        ]

    # The Amazon Resource Name (ARN) of the IAM policy from which you want to
    # delete a version.

    # For more information about ARNs, see [Amazon Resource Names (ARNs) and AWS
    # Service Namespaces](http://docs.aws.amazon.com/general/latest/gr/aws-arns-
    # and-namespaces.html) in the _AWS General Reference_.
    policy_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The policy version to delete.

    # This parameter allows (per its [regex
    # pattern](http://wikipedia.org/wiki/regex)) a string of characters that
    # consists of the lowercase letter 'v' followed by one or two digits, and
    # optionally followed by a period '.' and a string of letters and digits.

    # For more information about managed policy versions, see [Versioning for
    # Managed Policies](http://docs.aws.amazon.com/IAM/latest/UserGuide/policies-
    # managed-versions.html) in the _IAM User Guide_.
    version_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DeleteRolePermissionsBoundaryRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "role_name",
                "RoleName",
                TypeInfo(str),
            ),
        ]

    # The name (friendly name, not ARN) of the IAM role from which you want to
    # remove the permissions boundary.
    role_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DeleteRolePolicyRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "role_name",
                "RoleName",
                TypeInfo(str),
            ),
            (
                "policy_name",
                "PolicyName",
                TypeInfo(str),
            ),
        ]

    # The name (friendly name, not ARN) identifying the role that the policy is
    # embedded in.

    # This parameter allows (per its [regex
    # pattern](http://wikipedia.org/wiki/regex)) a string of characters
    # consisting of upper and lowercase alphanumeric characters with no spaces.
    # You can also include any of the following characters: _+=,.@-
    role_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The name of the inline policy to delete from the specified IAM role.

    # This parameter allows (per its [regex
    # pattern](http://wikipedia.org/wiki/regex)) a string of characters
    # consisting of upper and lowercase alphanumeric characters with no spaces.
    # You can also include any of the following characters: _+=,.@-
    policy_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DeleteRoleRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "role_name",
                "RoleName",
                TypeInfo(str),
            ),
        ]

    # The name of the role to delete.

    # This parameter allows (per its [regex
    # pattern](http://wikipedia.org/wiki/regex)) a string of characters
    # consisting of upper and lowercase alphanumeric characters with no spaces.
    # You can also include any of the following characters: _+=,.@-
    role_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DeleteSAMLProviderRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "saml_provider_arn",
                "SAMLProviderArn",
                TypeInfo(str),
            ),
        ]

    # The Amazon Resource Name (ARN) of the SAML provider to delete.
    saml_provider_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DeleteSSHPublicKeyRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "user_name",
                "UserName",
                TypeInfo(str),
            ),
            (
                "ssh_public_key_id",
                "SSHPublicKeyId",
                TypeInfo(str),
            ),
        ]

    # The name of the IAM user associated with the SSH public key.

    # This parameter allows (per its [regex
    # pattern](http://wikipedia.org/wiki/regex)) a string of characters
    # consisting of upper and lowercase alphanumeric characters with no spaces.
    # You can also include any of the following characters: _+=,.@-
    user_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The unique identifier for the SSH public key.

    # This parameter allows (per its [regex
    # pattern](http://wikipedia.org/wiki/regex)) a string of characters that can
    # consist of any upper or lowercased letter or digit.
    ssh_public_key_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DeleteServerCertificateRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "server_certificate_name",
                "ServerCertificateName",
                TypeInfo(str),
            ),
        ]

    # The name of the server certificate you want to delete.

    # This parameter allows (per its [regex
    # pattern](http://wikipedia.org/wiki/regex)) a string of characters
    # consisting of upper and lowercase alphanumeric characters with no spaces.
    # You can also include any of the following characters: _+=,.@-
    server_certificate_name: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class DeleteServiceLinkedRoleRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "role_name",
                "RoleName",
                TypeInfo(str),
            ),
        ]

    # The name of the service-linked role to be deleted.
    role_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DeleteServiceLinkedRoleResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "deletion_task_id",
                "DeletionTaskId",
                TypeInfo(str),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The deletion task identifier that you can use to check the status of the
    # deletion. This identifier is returned in the format `task/aws-service-
    # role/<service-principal-name>/<role-name>/<task-uuid>`.
    deletion_task_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DeleteServiceSpecificCredentialRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "service_specific_credential_id",
                "ServiceSpecificCredentialId",
                TypeInfo(str),
            ),
            (
                "user_name",
                "UserName",
                TypeInfo(str),
            ),
        ]

    # The unique identifier of the service-specific credential. You can get this
    # value by calling ListServiceSpecificCredentials.

    # This parameter allows (per its [regex
    # pattern](http://wikipedia.org/wiki/regex)) a string of characters that can
    # consist of any upper or lowercased letter or digit.
    service_specific_credential_id: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The name of the IAM user associated with the service-specific credential.
    # If this value is not specified, then the operation assumes the user whose
    # credentials are used to call the operation.

    # This parameter allows (per its [regex
    # pattern](http://wikipedia.org/wiki/regex)) a string of characters
    # consisting of upper and lowercase alphanumeric characters with no spaces.
    # You can also include any of the following characters: _+=,.@-
    user_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DeleteSigningCertificateRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "certificate_id",
                "CertificateId",
                TypeInfo(str),
            ),
            (
                "user_name",
                "UserName",
                TypeInfo(str),
            ),
        ]

    # The ID of the signing certificate to delete.

    # The format of this parameter, as described by its
    # [regex](http://wikipedia.org/wiki/regex) pattern, is a string of characters
    # that can be upper- or lower-cased letters or digits.
    certificate_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The name of the user the signing certificate belongs to.

    # This parameter allows (per its [regex
    # pattern](http://wikipedia.org/wiki/regex)) a string of characters
    # consisting of upper and lowercase alphanumeric characters with no spaces.
    # You can also include any of the following characters: _+=,.@-
    user_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DeleteUserPermissionsBoundaryRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "user_name",
                "UserName",
                TypeInfo(str),
            ),
        ]

    # The name (friendly name, not ARN) of the IAM user from which you want to
    # remove the permissions boundary.
    user_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DeleteUserPolicyRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "user_name",
                "UserName",
                TypeInfo(str),
            ),
            (
                "policy_name",
                "PolicyName",
                TypeInfo(str),
            ),
        ]

    # The name (friendly name, not ARN) identifying the user that the policy is
    # embedded in.

    # This parameter allows (per its [regex
    # pattern](http://wikipedia.org/wiki/regex)) a string of characters
    # consisting of upper and lowercase alphanumeric characters with no spaces.
    # You can also include any of the following characters: _+=,.@-
    user_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The name identifying the policy document to delete.

    # This parameter allows (per its [regex
    # pattern](http://wikipedia.org/wiki/regex)) a string of characters
    # consisting of upper and lowercase alphanumeric characters with no spaces.
    # You can also include any of the following characters: _+=,.@-
    policy_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DeleteUserRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "user_name",
                "UserName",
                TypeInfo(str),
            ),
        ]

    # The name of the user to delete.

    # This parameter allows (per its [regex
    # pattern](http://wikipedia.org/wiki/regex)) a string of characters
    # consisting of upper and lowercase alphanumeric characters with no spaces.
    # You can also include any of the following characters: _+=,.@-
    user_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DeleteVirtualMFADeviceRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "serial_number",
                "SerialNumber",
                TypeInfo(str),
            ),
        ]

    # The serial number that uniquely identifies the MFA device. For virtual MFA
    # devices, the serial number is the same as the ARN.

    # This parameter allows (per its [regex
    # pattern](http://wikipedia.org/wiki/regex)) a string of characters
    # consisting of upper and lowercase alphanumeric characters with no spaces.
    # You can also include any of the following characters: =,.@:/-
    serial_number: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DeletionTaskFailureReasonType(ShapeBase):
    """
    The reason that the service-linked role deletion failed.

    This data type is used as a response element in the
    GetServiceLinkedRoleDeletionStatus operation.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "reason",
                "Reason",
                TypeInfo(str),
            ),
            (
                "role_usage_list",
                "RoleUsageList",
                TypeInfo(typing.List[RoleUsageType]),
            ),
        ]

    # A short description of the reason that the service-linked role deletion
    # failed.
    reason: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A list of objects that contains details about the service-linked role
    # deletion failure, if that information is returned by the service. If the
    # service-linked role has active sessions or if any resources that were used
    # by the role have not been deleted from the linked service, the role can't
    # be deleted. This parameter includes a list of the resources that are
    # associated with the role and the region in which the resources are being
    # used.
    role_usage_list: typing.List["RoleUsageType"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


class DeletionTaskStatusType(str):
    SUCCEEDED = "SUCCEEDED"
    IN_PROGRESS = "IN_PROGRESS"
    FAILED = "FAILED"
    NOT_STARTED = "NOT_STARTED"


@dataclasses.dataclass
class DetachGroupPolicyRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "group_name",
                "GroupName",
                TypeInfo(str),
            ),
            (
                "policy_arn",
                "PolicyArn",
                TypeInfo(str),
            ),
        ]

    # The name (friendly name, not ARN) of the IAM group to detach the policy
    # from.

    # This parameter allows (per its [regex
    # pattern](http://wikipedia.org/wiki/regex)) a string of characters
    # consisting of upper and lowercase alphanumeric characters with no spaces.
    # You can also include any of the following characters: _+=,.@-
    group_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The Amazon Resource Name (ARN) of the IAM policy you want to detach.

    # For more information about ARNs, see [Amazon Resource Names (ARNs) and AWS
    # Service Namespaces](http://docs.aws.amazon.com/general/latest/gr/aws-arns-
    # and-namespaces.html) in the _AWS General Reference_.
    policy_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DetachRolePolicyRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "role_name",
                "RoleName",
                TypeInfo(str),
            ),
            (
                "policy_arn",
                "PolicyArn",
                TypeInfo(str),
            ),
        ]

    # The name (friendly name, not ARN) of the IAM role to detach the policy
    # from.

    # This parameter allows (per its [regex
    # pattern](http://wikipedia.org/wiki/regex)) a string of characters
    # consisting of upper and lowercase alphanumeric characters with no spaces.
    # You can also include any of the following characters: _+=,.@-
    role_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The Amazon Resource Name (ARN) of the IAM policy you want to detach.

    # For more information about ARNs, see [Amazon Resource Names (ARNs) and AWS
    # Service Namespaces](http://docs.aws.amazon.com/general/latest/gr/aws-arns-
    # and-namespaces.html) in the _AWS General Reference_.
    policy_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DetachUserPolicyRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "user_name",
                "UserName",
                TypeInfo(str),
            ),
            (
                "policy_arn",
                "PolicyArn",
                TypeInfo(str),
            ),
        ]

    # The name (friendly name, not ARN) of the IAM user to detach the policy
    # from.

    # This parameter allows (per its [regex
    # pattern](http://wikipedia.org/wiki/regex)) a string of characters
    # consisting of upper and lowercase alphanumeric characters with no spaces.
    # You can also include any of the following characters: _+=,.@-
    user_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The Amazon Resource Name (ARN) of the IAM policy you want to detach.

    # For more information about ARNs, see [Amazon Resource Names (ARNs) and AWS
    # Service Namespaces](http://docs.aws.amazon.com/general/latest/gr/aws-arns-
    # and-namespaces.html) in the _AWS General Reference_.
    policy_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DuplicateCertificateException(ShapeBase):
    """
    The request was rejected because the same certificate is associated with an IAM
    user in the account.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "message",
                "message",
                TypeInfo(str),
            ),
        ]

    message: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DuplicateSSHPublicKeyException(ShapeBase):
    """
    The request was rejected because the SSH public key is already associated with
    the specified IAM user.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "message",
                "message",
                TypeInfo(str),
            ),
        ]

    message: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class EnableMFADeviceRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "user_name",
                "UserName",
                TypeInfo(str),
            ),
            (
                "serial_number",
                "SerialNumber",
                TypeInfo(str),
            ),
            (
                "authentication_code1",
                "AuthenticationCode1",
                TypeInfo(str),
            ),
            (
                "authentication_code2",
                "AuthenticationCode2",
                TypeInfo(str),
            ),
        ]

    # The name of the IAM user for whom you want to enable the MFA device.

    # This parameter allows (per its [regex
    # pattern](http://wikipedia.org/wiki/regex)) a string of characters
    # consisting of upper and lowercase alphanumeric characters with no spaces.
    # You can also include any of the following characters: _+=,.@-
    user_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The serial number that uniquely identifies the MFA device. For virtual MFA
    # devices, the serial number is the device ARN.

    # This parameter allows (per its [regex
    # pattern](http://wikipedia.org/wiki/regex)) a string of characters
    # consisting of upper and lowercase alphanumeric characters with no spaces.
    # You can also include any of the following characters: =,.@:/-
    serial_number: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # An authentication code emitted by the device.

    # The format for this parameter is a string of six digits.

    # Submit your request immediately after generating the authentication codes.
    # If you generate the codes and then wait too long to submit the request, the
    # MFA device successfully associates with the user but the MFA device becomes
    # out of sync. This happens because time-based one-time passwords (TOTP)
    # expire after a short period of time. If this happens, you can [resync the
    # device](http://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_mfa_sync.html).
    authentication_code1: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A subsequent authentication code emitted by the device.

    # The format for this parameter is a string of six digits.

    # Submit your request immediately after generating the authentication codes.
    # If you generate the codes and then wait too long to submit the request, the
    # MFA device successfully associates with the user but the MFA device becomes
    # out of sync. This happens because time-based one-time passwords (TOTP)
    # expire after a short period of time. If this happens, you can [resync the
    # device](http://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_mfa_sync.html).
    authentication_code2: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class EntityAlreadyExistsException(ShapeBase):
    """
    The request was rejected because it attempted to create a resource that already
    exists.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "message",
                "message",
                TypeInfo(str),
            ),
        ]

    message: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class EntityTemporarilyUnmodifiableException(ShapeBase):
    """
    The request was rejected because it referenced an entity that is temporarily
    unmodifiable, such as a user name that was deleted and then recreated. The error
    indicates that the request is likely to succeed if you try again after waiting
    several minutes. The error message describes the entity.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "message",
                "message",
                TypeInfo(str),
            ),
        ]

    message: str = dataclasses.field(default=ShapeBase.NOT_SET, )


class EntityType(str):
    User = "User"
    Role = "Role"
    Group = "Group"
    LocalManagedPolicy = "LocalManagedPolicy"
    AWSManagedPolicy = "AWSManagedPolicy"


@dataclasses.dataclass
class EvaluationResult(ShapeBase):
    """
    Contains the results of a simulation.

    This data type is used by the return parameter of ` SimulateCustomPolicy ` and `
    SimulatePrincipalPolicy `.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "eval_action_name",
                "EvalActionName",
                TypeInfo(str),
            ),
            (
                "eval_decision",
                "EvalDecision",
                TypeInfo(typing.Union[str, PolicyEvaluationDecisionType]),
            ),
            (
                "eval_resource_name",
                "EvalResourceName",
                TypeInfo(str),
            ),
            (
                "matched_statements",
                "MatchedStatements",
                TypeInfo(typing.List[Statement]),
            ),
            (
                "missing_context_values",
                "MissingContextValues",
                TypeInfo(typing.List[str]),
            ),
            (
                "organizations_decision_detail",
                "OrganizationsDecisionDetail",
                TypeInfo(OrganizationsDecisionDetail),
            ),
            (
                "eval_decision_details",
                "EvalDecisionDetails",
                TypeInfo(
                    typing.Dict[str, typing.
                                Union[str, PolicyEvaluationDecisionType]]
                ),
            ),
            (
                "resource_specific_results",
                "ResourceSpecificResults",
                TypeInfo(typing.List[ResourceSpecificResult]),
            ),
        ]

    # The name of the API operation tested on the indicated resource.
    eval_action_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The result of the simulation.
    eval_decision: typing.Union[str, "PolicyEvaluationDecisionType"
                               ] = dataclasses.field(
                                   default=ShapeBase.NOT_SET,
                               )

    # The ARN of the resource that the indicated API operation was tested on.
    eval_resource_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A list of the statements in the input policies that determine the result
    # for this scenario. Remember that even if multiple statements allow the
    # operation on the resource, if only one statement denies that operation,
    # then the explicit deny overrides any allow, and the deny statement is the
    # only entry included in the result.
    matched_statements: typing.List["Statement"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A list of context keys that are required by the included input policies but
    # that were not provided by one of the input parameters. This list is used
    # when the resource in a simulation is "*", either explicitly, or when the
    # `ResourceArns` parameter blank. If you include a list of resources, then
    # any missing context values are instead included under the
    # `ResourceSpecificResults` section. To discover the context keys used by a
    # set of policies, you can call GetContextKeysForCustomPolicy or
    # GetContextKeysForPrincipalPolicy.
    missing_context_values: typing.List[str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A structure that details how AWS Organizations and its service control
    # policies affect the results of the simulation. Only applies if the
    # simulated user's account is part of an organization.
    organizations_decision_detail: "OrganizationsDecisionDetail" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Additional details about the results of the evaluation decision. When there
    # are both IAM policies and resource policies, this parameter explains how
    # each set of policies contributes to the final evaluation decision. When
    # simulating cross-account access to a resource, both the resource-based
    # policy and the caller's IAM policy must grant access. See [How IAM Roles
    # Differ from Resource-based
    # Policies](http://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_compare-
    # resource-policies.html)
    eval_decision_details: typing.Dict[
        str, typing.
        Union[str, "PolicyEvaluationDecisionType"]] = dataclasses.field(
            default=ShapeBase.NOT_SET,
        )

    # The individual results of the simulation of the API operation specified in
    # EvalActionName on each resource.
    resource_specific_results: typing.List["ResourceSpecificResult"
                                          ] = dataclasses.field(
                                              default=ShapeBase.NOT_SET,
                                          )


@dataclasses.dataclass
class GenerateCredentialReportResponse(OutputShapeBase):
    """
    Contains the response to a successful GenerateCredentialReport request.
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
                "state",
                "State",
                TypeInfo(typing.Union[str, ReportStateType]),
            ),
            (
                "description",
                "Description",
                TypeInfo(str),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Information about the state of the credential report.
    state: typing.Union[str, "ReportStateType"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Information about the credential report.
    description: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class GetAccessKeyLastUsedRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "access_key_id",
                "AccessKeyId",
                TypeInfo(str),
            ),
        ]

    # The identifier of an access key.

    # This parameter allows (per its [regex
    # pattern](http://wikipedia.org/wiki/regex)) a string of characters that can
    # consist of any upper or lowercased letter or digit.
    access_key_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class GetAccessKeyLastUsedResponse(OutputShapeBase):
    """
    Contains the response to a successful GetAccessKeyLastUsed request. It is also
    returned as a member of the AccessKeyMetaData structure returned by the
    ListAccessKeys action.
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
                "user_name",
                "UserName",
                TypeInfo(str),
            ),
            (
                "access_key_last_used",
                "AccessKeyLastUsed",
                TypeInfo(AccessKeyLastUsed),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The name of the AWS IAM user that owns this access key.
    user_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Contains information about the last time the access key was used.
    access_key_last_used: "AccessKeyLastUsed" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class GetAccountAuthorizationDetailsRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "filter",
                "Filter",
                TypeInfo(typing.List[typing.Union[str, EntityType]]),
            ),
            (
                "max_items",
                "MaxItems",
                TypeInfo(int),
            ),
            (
                "marker",
                "Marker",
                TypeInfo(str),
            ),
        ]

    # A list of entity types used to filter the results. Only the entities that
    # match the types you specify are included in the output. Use the value
    # `LocalManagedPolicy` to include customer managed policies.

    # The format for this parameter is a comma-separated (if more than one) list
    # of strings. Each string value in the list must be one of the valid values
    # listed below.
    filter: typing.List[typing.Union[str, "EntityType"]] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # (Optional) Use this only when paginating results to indicate the maximum
    # number of items you want in the response. If additional items exist beyond
    # the maximum you specify, the `IsTruncated` response element is `true`.

    # If you do not include this parameter, it defaults to 100. Note that IAM
    # might return fewer results, even when there are more results available. In
    # that case, the `IsTruncated` response element returns `true` and `Marker`
    # contains a value to include in the subsequent call that tells the service
    # where to continue from.
    max_items: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Use this parameter only when paginating results and only after you receive
    # a response indicating that the results are truncated. Set it to the value
    # of the `Marker` element in the response that you received to indicate where
    # the next call should start.
    marker: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class GetAccountAuthorizationDetailsResponse(OutputShapeBase):
    """
    Contains the response to a successful GetAccountAuthorizationDetails request.
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
                "user_detail_list",
                "UserDetailList",
                TypeInfo(typing.List[UserDetail]),
            ),
            (
                "group_detail_list",
                "GroupDetailList",
                TypeInfo(typing.List[GroupDetail]),
            ),
            (
                "role_detail_list",
                "RoleDetailList",
                TypeInfo(typing.List[RoleDetail]),
            ),
            (
                "policies",
                "Policies",
                TypeInfo(typing.List[ManagedPolicyDetail]),
            ),
            (
                "is_truncated",
                "IsTruncated",
                TypeInfo(bool),
            ),
            (
                "marker",
                "Marker",
                TypeInfo(str),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A list containing information about IAM users.
    user_detail_list: typing.List["UserDetail"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A list containing information about IAM groups.
    group_detail_list: typing.List["GroupDetail"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A list containing information about IAM roles.
    role_detail_list: typing.List["RoleDetail"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A list containing information about managed policies.
    policies: typing.List["ManagedPolicyDetail"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A flag that indicates whether there are more items to return. If your
    # results were truncated, you can make a subsequent pagination request using
    # the `Marker` request parameter to retrieve more items. Note that IAM might
    # return fewer than the `MaxItems` number of results even when there are more
    # results available. We recommend that you check `IsTruncated` after every
    # call to ensure that you receive all of your results.
    is_truncated: bool = dataclasses.field(default=ShapeBase.NOT_SET, )

    # When `IsTruncated` is `true`, this element is present and contains the
    # value to use for the `Marker` parameter in a subsequent pagination request.
    marker: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    def paginate(
        self,
    ) -> typing.Generator["GetAccountAuthorizationDetailsResponse", None, None]:
        yield from super()._paginate()


@dataclasses.dataclass
class GetAccountPasswordPolicyResponse(OutputShapeBase):
    """
    Contains the response to a successful GetAccountPasswordPolicy request.
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
                "password_policy",
                "PasswordPolicy",
                TypeInfo(PasswordPolicy),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A structure that contains details about the account's password policy.
    password_policy: "PasswordPolicy" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class GetAccountSummaryResponse(OutputShapeBase):
    """
    Contains the response to a successful GetAccountSummary request.
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
                "summary_map",
                "SummaryMap",
                TypeInfo(typing.Dict[typing.Union[str, summaryKeyType], int]),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A set of key value pairs containing information about IAM entity usage and
    # IAM quotas.
    summary_map: typing.Dict[typing.Union[str, "summaryKeyType"], int
                            ] = dataclasses.field(
                                default=ShapeBase.NOT_SET,
                            )


@dataclasses.dataclass
class GetContextKeysForCustomPolicyRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "policy_input_list",
                "PolicyInputList",
                TypeInfo(typing.List[str]),
            ),
        ]

    # A list of policies for which you want the list of context keys referenced
    # in those policies. Each document is specified as a string containing the
    # complete, valid JSON text of an IAM policy.

    # The [regex pattern](http://wikipedia.org/wiki/regex) used to validate this
    # parameter is a string of characters consisting of the following:

    #   * Any printable ASCII character ranging from the space character (\u0020) through the end of the ASCII character range

    #   * The printable characters in the Basic Latin and Latin-1 Supplement character set (through \u00FF)

    #   * The special characters tab (\u0009), line feed (\u000A), and carriage return (\u000D)
    policy_input_list: typing.List[str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class GetContextKeysForPolicyResponse(OutputShapeBase):
    """
    Contains the response to a successful GetContextKeysForPrincipalPolicy or
    GetContextKeysForCustomPolicy request.
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
                "context_key_names",
                "ContextKeyNames",
                TypeInfo(typing.List[str]),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The list of context keys that are referenced in the input policies.
    context_key_names: typing.List[str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class GetContextKeysForPrincipalPolicyRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "policy_source_arn",
                "PolicySourceArn",
                TypeInfo(str),
            ),
            (
                "policy_input_list",
                "PolicyInputList",
                TypeInfo(typing.List[str]),
            ),
        ]

    # The ARN of a user, group, or role whose policies contain the context keys
    # that you want listed. If you specify a user, the list includes context keys
    # that are found in all policies that are attached to the user. The list also
    # includes all groups that the user is a member of. If you pick a group or a
    # role, then it includes only those context keys that are found in policies
    # attached to that entity. Note that all parameters are shown in unencoded
    # form here for clarity, but must be URL encoded to be included as a part of
    # a real HTML request.

    # For more information about ARNs, see [Amazon Resource Names (ARNs) and AWS
    # Service Namespaces](http://docs.aws.amazon.com/general/latest/gr/aws-arns-
    # and-namespaces.html) in the _AWS General Reference_.
    policy_source_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # An optional list of additional policies for which you want the list of
    # context keys that are referenced.

    # The [regex pattern](http://wikipedia.org/wiki/regex) used to validate this
    # parameter is a string of characters consisting of the following:

    #   * Any printable ASCII character ranging from the space character (\u0020) through the end of the ASCII character range

    #   * The printable characters in the Basic Latin and Latin-1 Supplement character set (through \u00FF)

    #   * The special characters tab (\u0009), line feed (\u000A), and carriage return (\u000D)
    policy_input_list: typing.List[str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class GetCredentialReportResponse(OutputShapeBase):
    """
    Contains the response to a successful GetCredentialReport request.
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
                "content",
                "Content",
                TypeInfo(typing.Any),
            ),
            (
                "report_format",
                "ReportFormat",
                TypeInfo(typing.Union[str, ReportFormatType]),
            ),
            (
                "generated_time",
                "GeneratedTime",
                TypeInfo(datetime.datetime),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Contains the credential report. The report is Base64-encoded.
    content: typing.Any = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The format (MIME type) of the credential report.
    report_format: typing.Union[str, "ReportFormatType"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The date and time when the credential report was created, in [ISO 8601
    # date-time format](http://www.iso.org/iso/iso8601).
    generated_time: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class GetGroupPolicyRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "group_name",
                "GroupName",
                TypeInfo(str),
            ),
            (
                "policy_name",
                "PolicyName",
                TypeInfo(str),
            ),
        ]

    # The name of the group the policy is associated with.

    # This parameter allows (per its [regex
    # pattern](http://wikipedia.org/wiki/regex)) a string of characters
    # consisting of upper and lowercase alphanumeric characters with no spaces.
    # You can also include any of the following characters: _+=,.@-
    group_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The name of the policy document to get.

    # This parameter allows (per its [regex
    # pattern](http://wikipedia.org/wiki/regex)) a string of characters
    # consisting of upper and lowercase alphanumeric characters with no spaces.
    # You can also include any of the following characters: _+=,.@-
    policy_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class GetGroupPolicyResponse(OutputShapeBase):
    """
    Contains the response to a successful GetGroupPolicy request.
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
                "group_name",
                "GroupName",
                TypeInfo(str),
            ),
            (
                "policy_name",
                "PolicyName",
                TypeInfo(str),
            ),
            (
                "policy_document",
                "PolicyDocument",
                TypeInfo(str),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The group the policy is associated with.
    group_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The name of the policy.
    policy_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The policy document.
    policy_document: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class GetGroupRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "group_name",
                "GroupName",
                TypeInfo(str),
            ),
            (
                "marker",
                "Marker",
                TypeInfo(str),
            ),
            (
                "max_items",
                "MaxItems",
                TypeInfo(int),
            ),
        ]

    # The name of the group.

    # This parameter allows (per its [regex
    # pattern](http://wikipedia.org/wiki/regex)) a string of characters
    # consisting of upper and lowercase alphanumeric characters with no spaces.
    # You can also include any of the following characters: _+=,.@-
    group_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Use this parameter only when paginating results and only after you receive
    # a response indicating that the results are truncated. Set it to the value
    # of the `Marker` element in the response that you received to indicate where
    # the next call should start.
    marker: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # (Optional) Use this only when paginating results to indicate the maximum
    # number of items you want in the response. If additional items exist beyond
    # the maximum you specify, the `IsTruncated` response element is `true`.

    # If you do not include this parameter, it defaults to 100. Note that IAM
    # might return fewer results, even when there are more results available. In
    # that case, the `IsTruncated` response element returns `true` and `Marker`
    # contains a value to include in the subsequent call that tells the service
    # where to continue from.
    max_items: int = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class GetGroupResponse(OutputShapeBase):
    """
    Contains the response to a successful GetGroup request.
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
                "group",
                "Group",
                TypeInfo(Group),
            ),
            (
                "users",
                "Users",
                TypeInfo(typing.List[User]),
            ),
            (
                "is_truncated",
                "IsTruncated",
                TypeInfo(bool),
            ),
            (
                "marker",
                "Marker",
                TypeInfo(str),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A structure that contains details about the group.
    group: "Group" = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A list of users in the group.
    users: typing.List["User"] = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A flag that indicates whether there are more items to return. If your
    # results were truncated, you can make a subsequent pagination request using
    # the `Marker` request parameter to retrieve more items. Note that IAM might
    # return fewer than the `MaxItems` number of results even when there are more
    # results available. We recommend that you check `IsTruncated` after every
    # call to ensure that you receive all of your results.
    is_truncated: bool = dataclasses.field(default=ShapeBase.NOT_SET, )

    # When `IsTruncated` is `true`, this element is present and contains the
    # value to use for the `Marker` parameter in a subsequent pagination request.
    marker: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    def paginate(self, ) -> typing.Generator["GetGroupResponse", None, None]:
        yield from super()._paginate()


@dataclasses.dataclass
class GetInstanceProfileRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "instance_profile_name",
                "InstanceProfileName",
                TypeInfo(str),
            ),
        ]

    # The name of the instance profile to get information about.

    # This parameter allows (per its [regex
    # pattern](http://wikipedia.org/wiki/regex)) a string of characters
    # consisting of upper and lowercase alphanumeric characters with no spaces.
    # You can also include any of the following characters: _+=,.@-
    instance_profile_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class GetInstanceProfileResponse(OutputShapeBase):
    """
    Contains the response to a successful GetInstanceProfile request.
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
                "instance_profile",
                "InstanceProfile",
                TypeInfo(InstanceProfile),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A structure containing details about the instance profile.
    instance_profile: "InstanceProfile" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class GetLoginProfileRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "user_name",
                "UserName",
                TypeInfo(str),
            ),
        ]

    # The name of the user whose login profile you want to retrieve.

    # This parameter allows (per its [regex
    # pattern](http://wikipedia.org/wiki/regex)) a string of characters
    # consisting of upper and lowercase alphanumeric characters with no spaces.
    # You can also include any of the following characters: _+=,.@-
    user_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class GetLoginProfileResponse(OutputShapeBase):
    """
    Contains the response to a successful GetLoginProfile request.
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
                "login_profile",
                "LoginProfile",
                TypeInfo(LoginProfile),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A structure containing the user name and password create date for the user.
    login_profile: "LoginProfile" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class GetOpenIDConnectProviderRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "open_id_connect_provider_arn",
                "OpenIDConnectProviderArn",
                TypeInfo(str),
            ),
        ]

    # The Amazon Resource Name (ARN) of the OIDC provider resource object in IAM
    # to get information for. You can get a list of OIDC provider resource ARNs
    # by using the ListOpenIDConnectProviders operation.

    # For more information about ARNs, see [Amazon Resource Names (ARNs) and AWS
    # Service Namespaces](http://docs.aws.amazon.com/general/latest/gr/aws-arns-
    # and-namespaces.html) in the _AWS General Reference_.
    open_id_connect_provider_arn: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class GetOpenIDConnectProviderResponse(OutputShapeBase):
    """
    Contains the response to a successful GetOpenIDConnectProvider request.
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
            (
                "client_id_list",
                "ClientIDList",
                TypeInfo(typing.List[str]),
            ),
            (
                "thumbprint_list",
                "ThumbprintList",
                TypeInfo(typing.List[str]),
            ),
            (
                "create_date",
                "CreateDate",
                TypeInfo(datetime.datetime),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The URL that the IAM OIDC provider resource object is associated with. For
    # more information, see CreateOpenIDConnectProvider.
    url: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A list of client IDs (also known as audiences) that are associated with the
    # specified IAM OIDC provider resource object. For more information, see
    # CreateOpenIDConnectProvider.
    client_id_list: typing.List[str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A list of certificate thumbprints that are associated with the specified
    # IAM OIDC provider resource object. For more information, see
    # CreateOpenIDConnectProvider.
    thumbprint_list: typing.List[str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The date and time when the IAM OIDC provider resource object was created in
    # the AWS account.
    create_date: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class GetPolicyRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "policy_arn",
                "PolicyArn",
                TypeInfo(str),
            ),
        ]

    # The Amazon Resource Name (ARN) of the managed policy that you want
    # information about.

    # For more information about ARNs, see [Amazon Resource Names (ARNs) and AWS
    # Service Namespaces](http://docs.aws.amazon.com/general/latest/gr/aws-arns-
    # and-namespaces.html) in the _AWS General Reference_.
    policy_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class GetPolicyResponse(OutputShapeBase):
    """
    Contains the response to a successful GetPolicy request.
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
                "policy",
                "Policy",
                TypeInfo(Policy),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A structure containing details about the policy.
    policy: "Policy" = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class GetPolicyVersionRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "policy_arn",
                "PolicyArn",
                TypeInfo(str),
            ),
            (
                "version_id",
                "VersionId",
                TypeInfo(str),
            ),
        ]

    # The Amazon Resource Name (ARN) of the managed policy that you want
    # information about.

    # For more information about ARNs, see [Amazon Resource Names (ARNs) and AWS
    # Service Namespaces](http://docs.aws.amazon.com/general/latest/gr/aws-arns-
    # and-namespaces.html) in the _AWS General Reference_.
    policy_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Identifies the policy version to retrieve.

    # This parameter allows (per its [regex
    # pattern](http://wikipedia.org/wiki/regex)) a string of characters that
    # consists of the lowercase letter 'v' followed by one or two digits, and
    # optionally followed by a period '.' and a string of letters and digits.
    version_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class GetPolicyVersionResponse(OutputShapeBase):
    """
    Contains the response to a successful GetPolicyVersion request.
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
                "policy_version",
                "PolicyVersion",
                TypeInfo(PolicyVersion),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A structure containing details about the policy version.
    policy_version: "PolicyVersion" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class GetRolePolicyRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "role_name",
                "RoleName",
                TypeInfo(str),
            ),
            (
                "policy_name",
                "PolicyName",
                TypeInfo(str),
            ),
        ]

    # The name of the role associated with the policy.

    # This parameter allows (per its [regex
    # pattern](http://wikipedia.org/wiki/regex)) a string of characters
    # consisting of upper and lowercase alphanumeric characters with no spaces.
    # You can also include any of the following characters: _+=,.@-
    role_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The name of the policy document to get.

    # This parameter allows (per its [regex
    # pattern](http://wikipedia.org/wiki/regex)) a string of characters
    # consisting of upper and lowercase alphanumeric characters with no spaces.
    # You can also include any of the following characters: _+=,.@-
    policy_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class GetRolePolicyResponse(OutputShapeBase):
    """
    Contains the response to a successful GetRolePolicy request.
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
                "role_name",
                "RoleName",
                TypeInfo(str),
            ),
            (
                "policy_name",
                "PolicyName",
                TypeInfo(str),
            ),
            (
                "policy_document",
                "PolicyDocument",
                TypeInfo(str),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The role the policy is associated with.
    role_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The name of the policy.
    policy_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The policy document.
    policy_document: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class GetRoleRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "role_name",
                "RoleName",
                TypeInfo(str),
            ),
        ]

    # The name of the IAM role to get information about.

    # This parameter allows (per its [regex
    # pattern](http://wikipedia.org/wiki/regex)) a string of characters
    # consisting of upper and lowercase alphanumeric characters with no spaces.
    # You can also include any of the following characters: _+=,.@-
    role_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class GetRoleResponse(OutputShapeBase):
    """
    Contains the response to a successful GetRole request.
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
                "role",
                "Role",
                TypeInfo(Role),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A structure containing details about the IAM role.
    role: "Role" = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class GetSAMLProviderRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "saml_provider_arn",
                "SAMLProviderArn",
                TypeInfo(str),
            ),
        ]

    # The Amazon Resource Name (ARN) of the SAML provider resource object in IAM
    # to get information about.

    # For more information about ARNs, see [Amazon Resource Names (ARNs) and AWS
    # Service Namespaces](http://docs.aws.amazon.com/general/latest/gr/aws-arns-
    # and-namespaces.html) in the _AWS General Reference_.
    saml_provider_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class GetSAMLProviderResponse(OutputShapeBase):
    """
    Contains the response to a successful GetSAMLProvider request.
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
                "saml_metadata_document",
                "SAMLMetadataDocument",
                TypeInfo(str),
            ),
            (
                "create_date",
                "CreateDate",
                TypeInfo(datetime.datetime),
            ),
            (
                "valid_until",
                "ValidUntil",
                TypeInfo(datetime.datetime),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The XML metadata document that includes information about an identity
    # provider.
    saml_metadata_document: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The date and time when the SAML provider was created.
    create_date: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The expiration date and time for the SAML provider.
    valid_until: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class GetSSHPublicKeyRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "user_name",
                "UserName",
                TypeInfo(str),
            ),
            (
                "ssh_public_key_id",
                "SSHPublicKeyId",
                TypeInfo(str),
            ),
            (
                "encoding",
                "Encoding",
                TypeInfo(typing.Union[str, encodingType]),
            ),
        ]

    # The name of the IAM user associated with the SSH public key.

    # This parameter allows (per its [regex
    # pattern](http://wikipedia.org/wiki/regex)) a string of characters
    # consisting of upper and lowercase alphanumeric characters with no spaces.
    # You can also include any of the following characters: _+=,.@-
    user_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The unique identifier for the SSH public key.

    # This parameter allows (per its [regex
    # pattern](http://wikipedia.org/wiki/regex)) a string of characters that can
    # consist of any upper or lowercased letter or digit.
    ssh_public_key_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Specifies the public key encoding format to use in the response. To
    # retrieve the public key in ssh-rsa format, use `SSH`. To retrieve the
    # public key in PEM format, use `PEM`.
    encoding: typing.Union[str, "encodingType"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class GetSSHPublicKeyResponse(OutputShapeBase):
    """
    Contains the response to a successful GetSSHPublicKey request.
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
                "ssh_public_key",
                "SSHPublicKey",
                TypeInfo(SSHPublicKey),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A structure containing details about the SSH public key.
    ssh_public_key: "SSHPublicKey" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class GetServerCertificateRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "server_certificate_name",
                "ServerCertificateName",
                TypeInfo(str),
            ),
        ]

    # The name of the server certificate you want to retrieve information about.

    # This parameter allows (per its [regex
    # pattern](http://wikipedia.org/wiki/regex)) a string of characters
    # consisting of upper and lowercase alphanumeric characters with no spaces.
    # You can also include any of the following characters: _+=,.@-
    server_certificate_name: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class GetServerCertificateResponse(OutputShapeBase):
    """
    Contains the response to a successful GetServerCertificate request.
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
                "server_certificate",
                "ServerCertificate",
                TypeInfo(ServerCertificate),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A structure containing details about the server certificate.
    server_certificate: "ServerCertificate" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class GetServiceLinkedRoleDeletionStatusRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "deletion_task_id",
                "DeletionTaskId",
                TypeInfo(str),
            ),
        ]

    # The deletion task identifier. This identifier is returned by the
    # DeleteServiceLinkedRole operation in the format `task/aws-service-
    # role/<service-principal-name>/<role-name>/<task-uuid>`.
    deletion_task_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class GetServiceLinkedRoleDeletionStatusResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "status",
                "Status",
                TypeInfo(typing.Union[str, DeletionTaskStatusType]),
            ),
            (
                "reason",
                "Reason",
                TypeInfo(DeletionTaskFailureReasonType),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The status of the deletion.
    status: typing.Union[str, "DeletionTaskStatusType"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # An object that contains details about the reason the deletion failed.
    reason: "DeletionTaskFailureReasonType" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class GetUserPolicyRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "user_name",
                "UserName",
                TypeInfo(str),
            ),
            (
                "policy_name",
                "PolicyName",
                TypeInfo(str),
            ),
        ]

    # The name of the user who the policy is associated with.

    # This parameter allows (per its [regex
    # pattern](http://wikipedia.org/wiki/regex)) a string of characters
    # consisting of upper and lowercase alphanumeric characters with no spaces.
    # You can also include any of the following characters: _+=,.@-
    user_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The name of the policy document to get.

    # This parameter allows (per its [regex
    # pattern](http://wikipedia.org/wiki/regex)) a string of characters
    # consisting of upper and lowercase alphanumeric characters with no spaces.
    # You can also include any of the following characters: _+=,.@-
    policy_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class GetUserPolicyResponse(OutputShapeBase):
    """
    Contains the response to a successful GetUserPolicy request.
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
                "user_name",
                "UserName",
                TypeInfo(str),
            ),
            (
                "policy_name",
                "PolicyName",
                TypeInfo(str),
            ),
            (
                "policy_document",
                "PolicyDocument",
                TypeInfo(str),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The user the policy is associated with.
    user_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The name of the policy.
    policy_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The policy document.
    policy_document: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class GetUserRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "user_name",
                "UserName",
                TypeInfo(str),
            ),
        ]

    # The name of the user to get information about.

    # This parameter is optional. If it is not included, it defaults to the user
    # making the request. This parameter allows (per its [regex
    # pattern](http://wikipedia.org/wiki/regex)) a string of characters
    # consisting of upper and lowercase alphanumeric characters with no spaces.
    # You can also include any of the following characters: _+=,.@-
    user_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class GetUserResponse(OutputShapeBase):
    """
    Contains the response to a successful GetUser request.
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
                "user",
                "User",
                TypeInfo(User),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A structure containing details about the IAM user.

    # Due to a service issue, password last used data does not include password
    # use from May 3rd 2018 22:50 PDT to May 23rd 2018 14:08 PDT. This affects
    # [last sign-
    # in](http://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_finding-
    # unused.html) dates shown in the IAM console and password last used dates in
    # the [IAM credential
    # report](http://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_getting-
    # report.html), and returned by this GetUser API. If users signed in during
    # the affected time, the password last used date that is returned is the date
    # the user last signed in before May 3rd 2018. For users that signed in after
    # May 23rd 2018 14:08 PDT, the returned password last used date is accurate.

    # If you use password last used information to identify unused credentials
    # for deletion, such as deleting users who did not sign in to AWS in the last
    # 90 days, we recommend that you adjust your evaluation window to include
    # dates after May 23rd 2018. Alternatively, if your users use access keys to
    # access AWS programmatically you can refer to access key last used
    # information because it is accurate for all dates.
    user: "User" = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class Group(ShapeBase):
    """
    Contains information about an IAM group entity.

    This data type is used as a response element in the following operations:

      * CreateGroup

      * GetGroup

      * ListGroups
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "path",
                "Path",
                TypeInfo(str),
            ),
            (
                "group_name",
                "GroupName",
                TypeInfo(str),
            ),
            (
                "group_id",
                "GroupId",
                TypeInfo(str),
            ),
            (
                "arn",
                "Arn",
                TypeInfo(str),
            ),
            (
                "create_date",
                "CreateDate",
                TypeInfo(datetime.datetime),
            ),
        ]

    # The path to the group. For more information about paths, see [IAM
    # Identifiers](http://docs.aws.amazon.com/IAM/latest/UserGuide/Using_Identifiers.html)
    # in the _Using IAM_ guide.
    path: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The friendly name that identifies the group.
    group_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The stable and unique string identifying the group. For more information
    # about IDs, see [IAM
    # Identifiers](http://docs.aws.amazon.com/IAM/latest/UserGuide/Using_Identifiers.html)
    # in the _Using IAM_ guide.
    group_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The Amazon Resource Name (ARN) specifying the group. For more information
    # about ARNs and how to use them in policies, see [IAM
    # Identifiers](http://docs.aws.amazon.com/IAM/latest/UserGuide/Using_Identifiers.html)
    # in the _Using IAM_ guide.
    arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The date and time, in [ISO 8601 date-time
    # format](http://www.iso.org/iso/iso8601), when the group was created.
    create_date: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class GroupDetail(ShapeBase):
    """
    Contains information about an IAM group, including all of the group's policies.

    This data type is used as a response element in the
    GetAccountAuthorizationDetails operation.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "path",
                "Path",
                TypeInfo(str),
            ),
            (
                "group_name",
                "GroupName",
                TypeInfo(str),
            ),
            (
                "group_id",
                "GroupId",
                TypeInfo(str),
            ),
            (
                "arn",
                "Arn",
                TypeInfo(str),
            ),
            (
                "create_date",
                "CreateDate",
                TypeInfo(datetime.datetime),
            ),
            (
                "group_policy_list",
                "GroupPolicyList",
                TypeInfo(typing.List[PolicyDetail]),
            ),
            (
                "attached_managed_policies",
                "AttachedManagedPolicies",
                TypeInfo(typing.List[AttachedPolicy]),
            ),
        ]

    # The path to the group. For more information about paths, see [IAM
    # Identifiers](http://docs.aws.amazon.com/IAM/latest/UserGuide/Using_Identifiers.html)
    # in the _Using IAM_ guide.
    path: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The friendly name that identifies the group.
    group_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The stable and unique string identifying the group. For more information
    # about IDs, see [IAM
    # Identifiers](http://docs.aws.amazon.com/IAM/latest/UserGuide/Using_Identifiers.html)
    # in the _Using IAM_ guide.
    group_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The Amazon Resource Name (ARN). ARNs are unique identifiers for AWS
    # resources.

    # For more information about ARNs, go to [Amazon Resource Names (ARNs) and
    # AWS Service Namespaces](http://docs.aws.amazon.com/general/latest/gr/aws-
    # arns-and-namespaces.html) in the _AWS General Reference_.
    arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The date and time, in [ISO 8601 date-time
    # format](http://www.iso.org/iso/iso8601), when the group was created.
    create_date: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A list of the inline policies embedded in the group.
    group_policy_list: typing.List["PolicyDetail"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A list of the managed policies attached to the group.
    attached_managed_policies: typing.List["AttachedPolicy"
                                          ] = dataclasses.field(
                                              default=ShapeBase.NOT_SET,
                                          )


@dataclasses.dataclass
class InstanceProfile(ShapeBase):
    """
    Contains information about an instance profile.

    This data type is used as a response element in the following operations:

      * CreateInstanceProfile

      * GetInstanceProfile

      * ListInstanceProfiles

      * ListInstanceProfilesForRole
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "path",
                "Path",
                TypeInfo(str),
            ),
            (
                "instance_profile_name",
                "InstanceProfileName",
                TypeInfo(str),
            ),
            (
                "instance_profile_id",
                "InstanceProfileId",
                TypeInfo(str),
            ),
            (
                "arn",
                "Arn",
                TypeInfo(str),
            ),
            (
                "create_date",
                "CreateDate",
                TypeInfo(datetime.datetime),
            ),
            (
                "roles",
                "Roles",
                TypeInfo(typing.List[Role]),
            ),
        ]

    # The path to the instance profile. For more information about paths, see
    # [IAM
    # Identifiers](http://docs.aws.amazon.com/IAM/latest/UserGuide/Using_Identifiers.html)
    # in the _Using IAM_ guide.
    path: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The name identifying the instance profile.
    instance_profile_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The stable and unique string identifying the instance profile. For more
    # information about IDs, see [IAM
    # Identifiers](http://docs.aws.amazon.com/IAM/latest/UserGuide/Using_Identifiers.html)
    # in the _Using IAM_ guide.
    instance_profile_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The Amazon Resource Name (ARN) specifying the instance profile. For more
    # information about ARNs and how to use them in policies, see [IAM
    # Identifiers](http://docs.aws.amazon.com/IAM/latest/UserGuide/Using_Identifiers.html)
    # in the _Using IAM_ guide.
    arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The date when the instance profile was created.
    create_date: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The role associated with the instance profile.
    roles: typing.List["Role"] = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class InvalidAuthenticationCodeException(ShapeBase):
    """
    The request was rejected because the authentication code was not recognized. The
    error message describes the specific error.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "message",
                "message",
                TypeInfo(str),
            ),
        ]

    message: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class InvalidCertificateException(ShapeBase):
    """
    The request was rejected because the certificate is invalid.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "message",
                "message",
                TypeInfo(str),
            ),
        ]

    message: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class InvalidInputException(ShapeBase):
    """
    The request was rejected because an invalid or out-of-range value was supplied
    for an input parameter.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "message",
                "message",
                TypeInfo(str),
            ),
        ]

    message: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class InvalidPublicKeyException(ShapeBase):
    """
    The request was rejected because the public key is malformed or otherwise
    invalid.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "message",
                "message",
                TypeInfo(str),
            ),
        ]

    message: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class InvalidUserTypeException(ShapeBase):
    """
    The request was rejected because the type of user for the transaction was
    incorrect.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "message",
                "message",
                TypeInfo(str),
            ),
        ]

    message: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class KeyPairMismatchException(ShapeBase):
    """
    The request was rejected because the public key certificate and the private key
    do not match.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "message",
                "message",
                TypeInfo(str),
            ),
        ]

    message: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class LimitExceededException(ShapeBase):
    """
    The request was rejected because it attempted to create resources beyond the
    current AWS account limits. The error message describes the limit exceeded.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "message",
                "message",
                TypeInfo(str),
            ),
        ]

    message: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ListAccessKeysRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "user_name",
                "UserName",
                TypeInfo(str),
            ),
            (
                "marker",
                "Marker",
                TypeInfo(str),
            ),
            (
                "max_items",
                "MaxItems",
                TypeInfo(int),
            ),
        ]

    # The name of the user.

    # This parameter allows (per its [regex
    # pattern](http://wikipedia.org/wiki/regex)) a string of characters
    # consisting of upper and lowercase alphanumeric characters with no spaces.
    # You can also include any of the following characters: _+=,.@-
    user_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Use this parameter only when paginating results and only after you receive
    # a response indicating that the results are truncated. Set it to the value
    # of the `Marker` element in the response that you received to indicate where
    # the next call should start.
    marker: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # (Optional) Use this only when paginating results to indicate the maximum
    # number of items you want in the response. If additional items exist beyond
    # the maximum you specify, the `IsTruncated` response element is `true`.

    # If you do not include this parameter, it defaults to 100. Note that IAM
    # might return fewer results, even when there are more results available. In
    # that case, the `IsTruncated` response element returns `true` and `Marker`
    # contains a value to include in the subsequent call that tells the service
    # where to continue from.
    max_items: int = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ListAccessKeysResponse(OutputShapeBase):
    """
    Contains the response to a successful ListAccessKeys request.
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
                "access_key_metadata",
                "AccessKeyMetadata",
                TypeInfo(typing.List[AccessKeyMetadata]),
            ),
            (
                "is_truncated",
                "IsTruncated",
                TypeInfo(bool),
            ),
            (
                "marker",
                "Marker",
                TypeInfo(str),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A list of objects containing metadata about the access keys.
    access_key_metadata: typing.List["AccessKeyMetadata"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A flag that indicates whether there are more items to return. If your
    # results were truncated, you can make a subsequent pagination request using
    # the `Marker` request parameter to retrieve more items. Note that IAM might
    # return fewer than the `MaxItems` number of results even when there are more
    # results available. We recommend that you check `IsTruncated` after every
    # call to ensure that you receive all of your results.
    is_truncated: bool = dataclasses.field(default=ShapeBase.NOT_SET, )

    # When `IsTruncated` is `true`, this element is present and contains the
    # value to use for the `Marker` parameter in a subsequent pagination request.
    marker: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    def paginate(self,
                ) -> typing.Generator["ListAccessKeysResponse", None, None]:
        yield from super()._paginate()


@dataclasses.dataclass
class ListAccountAliasesRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "marker",
                "Marker",
                TypeInfo(str),
            ),
            (
                "max_items",
                "MaxItems",
                TypeInfo(int),
            ),
        ]

    # Use this parameter only when paginating results and only after you receive
    # a response indicating that the results are truncated. Set it to the value
    # of the `Marker` element in the response that you received to indicate where
    # the next call should start.
    marker: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # (Optional) Use this only when paginating results to indicate the maximum
    # number of items you want in the response. If additional items exist beyond
    # the maximum you specify, the `IsTruncated` response element is `true`.

    # If you do not include this parameter, it defaults to 100. Note that IAM
    # might return fewer results, even when there are more results available. In
    # that case, the `IsTruncated` response element returns `true` and `Marker`
    # contains a value to include in the subsequent call that tells the service
    # where to continue from.
    max_items: int = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ListAccountAliasesResponse(OutputShapeBase):
    """
    Contains the response to a successful ListAccountAliases request.
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
                "account_aliases",
                "AccountAliases",
                TypeInfo(typing.List[str]),
            ),
            (
                "is_truncated",
                "IsTruncated",
                TypeInfo(bool),
            ),
            (
                "marker",
                "Marker",
                TypeInfo(str),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A list of aliases associated with the account. AWS supports only one alias
    # per account.
    account_aliases: typing.List[str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A flag that indicates whether there are more items to return. If your
    # results were truncated, you can make a subsequent pagination request using
    # the `Marker` request parameter to retrieve more items. Note that IAM might
    # return fewer than the `MaxItems` number of results even when there are more
    # results available. We recommend that you check `IsTruncated` after every
    # call to ensure that you receive all of your results.
    is_truncated: bool = dataclasses.field(default=ShapeBase.NOT_SET, )

    # When `IsTruncated` is `true`, this element is present and contains the
    # value to use for the `Marker` parameter in a subsequent pagination request.
    marker: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    def paginate(self,
                ) -> typing.Generator["ListAccountAliasesResponse", None, None]:
        yield from super()._paginate()


@dataclasses.dataclass
class ListAttachedGroupPoliciesRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "group_name",
                "GroupName",
                TypeInfo(str),
            ),
            (
                "path_prefix",
                "PathPrefix",
                TypeInfo(str),
            ),
            (
                "marker",
                "Marker",
                TypeInfo(str),
            ),
            (
                "max_items",
                "MaxItems",
                TypeInfo(int),
            ),
        ]

    # The name (friendly name, not ARN) of the group to list attached policies
    # for.

    # This parameter allows (per its [regex
    # pattern](http://wikipedia.org/wiki/regex)) a string of characters
    # consisting of upper and lowercase alphanumeric characters with no spaces.
    # You can also include any of the following characters: _+=,.@-
    group_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The path prefix for filtering the results. This parameter is optional. If
    # it is not included, it defaults to a slash (/), listing all policies.

    # This parameter allows (per its [regex
    # pattern](http://wikipedia.org/wiki/regex)) a string of characters
    # consisting of either a forward slash (/) by itself or a string that must
    # begin and end with forward slashes. In addition, it can contain any ASCII
    # character from the ! (\u0021) through the DEL character (\u007F), including
    # most punctuation characters, digits, and upper and lowercased letters.
    path_prefix: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Use this parameter only when paginating results and only after you receive
    # a response indicating that the results are truncated. Set it to the value
    # of the `Marker` element in the response that you received to indicate where
    # the next call should start.
    marker: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # (Optional) Use this only when paginating results to indicate the maximum
    # number of items you want in the response. If additional items exist beyond
    # the maximum you specify, the `IsTruncated` response element is `true`.

    # If you do not include this parameter, it defaults to 100. Note that IAM
    # might return fewer results, even when there are more results available. In
    # that case, the `IsTruncated` response element returns `true` and `Marker`
    # contains a value to include in the subsequent call that tells the service
    # where to continue from.
    max_items: int = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ListAttachedGroupPoliciesResponse(OutputShapeBase):
    """
    Contains the response to a successful ListAttachedGroupPolicies request.
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
                "attached_policies",
                "AttachedPolicies",
                TypeInfo(typing.List[AttachedPolicy]),
            ),
            (
                "is_truncated",
                "IsTruncated",
                TypeInfo(bool),
            ),
            (
                "marker",
                "Marker",
                TypeInfo(str),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A list of the attached policies.
    attached_policies: typing.List["AttachedPolicy"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A flag that indicates whether there are more items to return. If your
    # results were truncated, you can make a subsequent pagination request using
    # the `Marker` request parameter to retrieve more items. Note that IAM might
    # return fewer than the `MaxItems` number of results even when there are more
    # results available. We recommend that you check `IsTruncated` after every
    # call to ensure that you receive all of your results.
    is_truncated: bool = dataclasses.field(default=ShapeBase.NOT_SET, )

    # When `IsTruncated` is `true`, this element is present and contains the
    # value to use for the `Marker` parameter in a subsequent pagination request.
    marker: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    def paginate(
        self,
    ) -> typing.Generator["ListAttachedGroupPoliciesResponse", None, None]:
        yield from super()._paginate()


@dataclasses.dataclass
class ListAttachedRolePoliciesRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "role_name",
                "RoleName",
                TypeInfo(str),
            ),
            (
                "path_prefix",
                "PathPrefix",
                TypeInfo(str),
            ),
            (
                "marker",
                "Marker",
                TypeInfo(str),
            ),
            (
                "max_items",
                "MaxItems",
                TypeInfo(int),
            ),
        ]

    # The name (friendly name, not ARN) of the role to list attached policies
    # for.

    # This parameter allows (per its [regex
    # pattern](http://wikipedia.org/wiki/regex)) a string of characters
    # consisting of upper and lowercase alphanumeric characters with no spaces.
    # You can also include any of the following characters: _+=,.@-
    role_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The path prefix for filtering the results. This parameter is optional. If
    # it is not included, it defaults to a slash (/), listing all policies.

    # This parameter allows (per its [regex
    # pattern](http://wikipedia.org/wiki/regex)) a string of characters
    # consisting of either a forward slash (/) by itself or a string that must
    # begin and end with forward slashes. In addition, it can contain any ASCII
    # character from the ! (\u0021) through the DEL character (\u007F), including
    # most punctuation characters, digits, and upper and lowercased letters.
    path_prefix: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Use this parameter only when paginating results and only after you receive
    # a response indicating that the results are truncated. Set it to the value
    # of the `Marker` element in the response that you received to indicate where
    # the next call should start.
    marker: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # (Optional) Use this only when paginating results to indicate the maximum
    # number of items you want in the response. If additional items exist beyond
    # the maximum you specify, the `IsTruncated` response element is `true`.

    # If you do not include this parameter, it defaults to 100. Note that IAM
    # might return fewer results, even when there are more results available. In
    # that case, the `IsTruncated` response element returns `true` and `Marker`
    # contains a value to include in the subsequent call that tells the service
    # where to continue from.
    max_items: int = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ListAttachedRolePoliciesResponse(OutputShapeBase):
    """
    Contains the response to a successful ListAttachedRolePolicies request.
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
                "attached_policies",
                "AttachedPolicies",
                TypeInfo(typing.List[AttachedPolicy]),
            ),
            (
                "is_truncated",
                "IsTruncated",
                TypeInfo(bool),
            ),
            (
                "marker",
                "Marker",
                TypeInfo(str),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A list of the attached policies.
    attached_policies: typing.List["AttachedPolicy"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A flag that indicates whether there are more items to return. If your
    # results were truncated, you can make a subsequent pagination request using
    # the `Marker` request parameter to retrieve more items. Note that IAM might
    # return fewer than the `MaxItems` number of results even when there are more
    # results available. We recommend that you check `IsTruncated` after every
    # call to ensure that you receive all of your results.
    is_truncated: bool = dataclasses.field(default=ShapeBase.NOT_SET, )

    # When `IsTruncated` is `true`, this element is present and contains the
    # value to use for the `Marker` parameter in a subsequent pagination request.
    marker: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    def paginate(
        self,
    ) -> typing.Generator["ListAttachedRolePoliciesResponse", None, None]:
        yield from super()._paginate()


@dataclasses.dataclass
class ListAttachedUserPoliciesRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "user_name",
                "UserName",
                TypeInfo(str),
            ),
            (
                "path_prefix",
                "PathPrefix",
                TypeInfo(str),
            ),
            (
                "marker",
                "Marker",
                TypeInfo(str),
            ),
            (
                "max_items",
                "MaxItems",
                TypeInfo(int),
            ),
        ]

    # The name (friendly name, not ARN) of the user to list attached policies
    # for.

    # This parameter allows (per its [regex
    # pattern](http://wikipedia.org/wiki/regex)) a string of characters
    # consisting of upper and lowercase alphanumeric characters with no spaces.
    # You can also include any of the following characters: _+=,.@-
    user_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The path prefix for filtering the results. This parameter is optional. If
    # it is not included, it defaults to a slash (/), listing all policies.

    # This parameter allows (per its [regex
    # pattern](http://wikipedia.org/wiki/regex)) a string of characters
    # consisting of either a forward slash (/) by itself or a string that must
    # begin and end with forward slashes. In addition, it can contain any ASCII
    # character from the ! (\u0021) through the DEL character (\u007F), including
    # most punctuation characters, digits, and upper and lowercased letters.
    path_prefix: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Use this parameter only when paginating results and only after you receive
    # a response indicating that the results are truncated. Set it to the value
    # of the `Marker` element in the response that you received to indicate where
    # the next call should start.
    marker: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # (Optional) Use this only when paginating results to indicate the maximum
    # number of items you want in the response. If additional items exist beyond
    # the maximum you specify, the `IsTruncated` response element is `true`.

    # If you do not include this parameter, it defaults to 100. Note that IAM
    # might return fewer results, even when there are more results available. In
    # that case, the `IsTruncated` response element returns `true` and `Marker`
    # contains a value to include in the subsequent call that tells the service
    # where to continue from.
    max_items: int = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ListAttachedUserPoliciesResponse(OutputShapeBase):
    """
    Contains the response to a successful ListAttachedUserPolicies request.
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
                "attached_policies",
                "AttachedPolicies",
                TypeInfo(typing.List[AttachedPolicy]),
            ),
            (
                "is_truncated",
                "IsTruncated",
                TypeInfo(bool),
            ),
            (
                "marker",
                "Marker",
                TypeInfo(str),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A list of the attached policies.
    attached_policies: typing.List["AttachedPolicy"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A flag that indicates whether there are more items to return. If your
    # results were truncated, you can make a subsequent pagination request using
    # the `Marker` request parameter to retrieve more items. Note that IAM might
    # return fewer than the `MaxItems` number of results even when there are more
    # results available. We recommend that you check `IsTruncated` after every
    # call to ensure that you receive all of your results.
    is_truncated: bool = dataclasses.field(default=ShapeBase.NOT_SET, )

    # When `IsTruncated` is `true`, this element is present and contains the
    # value to use for the `Marker` parameter in a subsequent pagination request.
    marker: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    def paginate(
        self,
    ) -> typing.Generator["ListAttachedUserPoliciesResponse", None, None]:
        yield from super()._paginate()


@dataclasses.dataclass
class ListEntitiesForPolicyRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "policy_arn",
                "PolicyArn",
                TypeInfo(str),
            ),
            (
                "entity_filter",
                "EntityFilter",
                TypeInfo(typing.Union[str, EntityType]),
            ),
            (
                "path_prefix",
                "PathPrefix",
                TypeInfo(str),
            ),
            (
                "policy_usage_filter",
                "PolicyUsageFilter",
                TypeInfo(typing.Union[str, PolicyUsageType]),
            ),
            (
                "marker",
                "Marker",
                TypeInfo(str),
            ),
            (
                "max_items",
                "MaxItems",
                TypeInfo(int),
            ),
        ]

    # The Amazon Resource Name (ARN) of the IAM policy for which you want the
    # versions.

    # For more information about ARNs, see [Amazon Resource Names (ARNs) and AWS
    # Service Namespaces](http://docs.aws.amazon.com/general/latest/gr/aws-arns-
    # and-namespaces.html) in the _AWS General Reference_.
    policy_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The entity type to use for filtering the results.

    # For example, when `EntityFilter` is `Role`, only the roles that are
    # attached to the specified policy are returned. This parameter is optional.
    # If it is not included, all attached entities (users, groups, and roles) are
    # returned. The argument for this parameter must be one of the valid values
    # listed below.
    entity_filter: typing.Union[str, "EntityType"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The path prefix for filtering the results. This parameter is optional. If
    # it is not included, it defaults to a slash (/), listing all entities.

    # This parameter allows (per its [regex
    # pattern](http://wikipedia.org/wiki/regex)) a string of characters
    # consisting of either a forward slash (/) by itself or a string that must
    # begin and end with forward slashes. In addition, it can contain any ASCII
    # character from the ! (\u0021) through the DEL character (\u007F), including
    # most punctuation characters, digits, and upper and lowercased letters.
    path_prefix: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The policy usage method to use for filtering the results.

    # To list only permissions policies, set `PolicyUsageFilter` to
    # `PermissionsPolicy`. To list only the policies used to set permissions
    # boundaries, set the value to `PermissionsBoundary`.

    # This parameter is optional. If it is not included, all policies are
    # returned.
    policy_usage_filter: typing.Union[str, "PolicyUsageType"
                                     ] = dataclasses.field(
                                         default=ShapeBase.NOT_SET,
                                     )

    # Use this parameter only when paginating results and only after you receive
    # a response indicating that the results are truncated. Set it to the value
    # of the `Marker` element in the response that you received to indicate where
    # the next call should start.
    marker: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # (Optional) Use this only when paginating results to indicate the maximum
    # number of items you want in the response. If additional items exist beyond
    # the maximum you specify, the `IsTruncated` response element is `true`.

    # If you do not include this parameter, it defaults to 100. Note that IAM
    # might return fewer results, even when there are more results available. In
    # that case, the `IsTruncated` response element returns `true` and `Marker`
    # contains a value to include in the subsequent call that tells the service
    # where to continue from.
    max_items: int = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ListEntitiesForPolicyResponse(OutputShapeBase):
    """
    Contains the response to a successful ListEntitiesForPolicy request.
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
                "policy_groups",
                "PolicyGroups",
                TypeInfo(typing.List[PolicyGroup]),
            ),
            (
                "policy_users",
                "PolicyUsers",
                TypeInfo(typing.List[PolicyUser]),
            ),
            (
                "policy_roles",
                "PolicyRoles",
                TypeInfo(typing.List[PolicyRole]),
            ),
            (
                "is_truncated",
                "IsTruncated",
                TypeInfo(bool),
            ),
            (
                "marker",
                "Marker",
                TypeInfo(str),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A list of IAM groups that the policy is attached to.
    policy_groups: typing.List["PolicyGroup"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A list of IAM users that the policy is attached to.
    policy_users: typing.List["PolicyUser"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A list of IAM roles that the policy is attached to.
    policy_roles: typing.List["PolicyRole"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A flag that indicates whether there are more items to return. If your
    # results were truncated, you can make a subsequent pagination request using
    # the `Marker` request parameter to retrieve more items. Note that IAM might
    # return fewer than the `MaxItems` number of results even when there are more
    # results available. We recommend that you check `IsTruncated` after every
    # call to ensure that you receive all of your results.
    is_truncated: bool = dataclasses.field(default=ShapeBase.NOT_SET, )

    # When `IsTruncated` is `true`, this element is present and contains the
    # value to use for the `Marker` parameter in a subsequent pagination request.
    marker: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    def paginate(
        self,
    ) -> typing.Generator["ListEntitiesForPolicyResponse", None, None]:
        yield from super()._paginate()


@dataclasses.dataclass
class ListGroupPoliciesRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "group_name",
                "GroupName",
                TypeInfo(str),
            ),
            (
                "marker",
                "Marker",
                TypeInfo(str),
            ),
            (
                "max_items",
                "MaxItems",
                TypeInfo(int),
            ),
        ]

    # The name of the group to list policies for.

    # This parameter allows (per its [regex
    # pattern](http://wikipedia.org/wiki/regex)) a string of characters
    # consisting of upper and lowercase alphanumeric characters with no spaces.
    # You can also include any of the following characters: _+=,.@-
    group_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Use this parameter only when paginating results and only after you receive
    # a response indicating that the results are truncated. Set it to the value
    # of the `Marker` element in the response that you received to indicate where
    # the next call should start.
    marker: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # (Optional) Use this only when paginating results to indicate the maximum
    # number of items you want in the response. If additional items exist beyond
    # the maximum you specify, the `IsTruncated` response element is `true`.

    # If you do not include this parameter, it defaults to 100. Note that IAM
    # might return fewer results, even when there are more results available. In
    # that case, the `IsTruncated` response element returns `true` and `Marker`
    # contains a value to include in the subsequent call that tells the service
    # where to continue from.
    max_items: int = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ListGroupPoliciesResponse(OutputShapeBase):
    """
    Contains the response to a successful ListGroupPolicies request.
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
                "policy_names",
                "PolicyNames",
                TypeInfo(typing.List[str]),
            ),
            (
                "is_truncated",
                "IsTruncated",
                TypeInfo(bool),
            ),
            (
                "marker",
                "Marker",
                TypeInfo(str),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A list of policy names.

    # This parameter allows (per its [regex
    # pattern](http://wikipedia.org/wiki/regex)) a string of characters
    # consisting of upper and lowercase alphanumeric characters with no spaces.
    # You can also include any of the following characters: _+=,.@-
    policy_names: typing.List[str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A flag that indicates whether there are more items to return. If your
    # results were truncated, you can make a subsequent pagination request using
    # the `Marker` request parameter to retrieve more items. Note that IAM might
    # return fewer than the `MaxItems` number of results even when there are more
    # results available. We recommend that you check `IsTruncated` after every
    # call to ensure that you receive all of your results.
    is_truncated: bool = dataclasses.field(default=ShapeBase.NOT_SET, )

    # When `IsTruncated` is `true`, this element is present and contains the
    # value to use for the `Marker` parameter in a subsequent pagination request.
    marker: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    def paginate(self,
                ) -> typing.Generator["ListGroupPoliciesResponse", None, None]:
        yield from super()._paginate()


@dataclasses.dataclass
class ListGroupsForUserRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "user_name",
                "UserName",
                TypeInfo(str),
            ),
            (
                "marker",
                "Marker",
                TypeInfo(str),
            ),
            (
                "max_items",
                "MaxItems",
                TypeInfo(int),
            ),
        ]

    # The name of the user to list groups for.

    # This parameter allows (per its [regex
    # pattern](http://wikipedia.org/wiki/regex)) a string of characters
    # consisting of upper and lowercase alphanumeric characters with no spaces.
    # You can also include any of the following characters: _+=,.@-
    user_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Use this parameter only when paginating results and only after you receive
    # a response indicating that the results are truncated. Set it to the value
    # of the `Marker` element in the response that you received to indicate where
    # the next call should start.
    marker: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # (Optional) Use this only when paginating results to indicate the maximum
    # number of items you want in the response. If additional items exist beyond
    # the maximum you specify, the `IsTruncated` response element is `true`.

    # If you do not include this parameter, it defaults to 100. Note that IAM
    # might return fewer results, even when there are more results available. In
    # that case, the `IsTruncated` response element returns `true` and `Marker`
    # contains a value to include in the subsequent call that tells the service
    # where to continue from.
    max_items: int = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ListGroupsForUserResponse(OutputShapeBase):
    """
    Contains the response to a successful ListGroupsForUser request.
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
                "groups",
                "Groups",
                TypeInfo(typing.List[Group]),
            ),
            (
                "is_truncated",
                "IsTruncated",
                TypeInfo(bool),
            ),
            (
                "marker",
                "Marker",
                TypeInfo(str),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A list of groups.
    groups: typing.List["Group"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A flag that indicates whether there are more items to return. If your
    # results were truncated, you can make a subsequent pagination request using
    # the `Marker` request parameter to retrieve more items. Note that IAM might
    # return fewer than the `MaxItems` number of results even when there are more
    # results available. We recommend that you check `IsTruncated` after every
    # call to ensure that you receive all of your results.
    is_truncated: bool = dataclasses.field(default=ShapeBase.NOT_SET, )

    # When `IsTruncated` is `true`, this element is present and contains the
    # value to use for the `Marker` parameter in a subsequent pagination request.
    marker: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    def paginate(self,
                ) -> typing.Generator["ListGroupsForUserResponse", None, None]:
        yield from super()._paginate()


@dataclasses.dataclass
class ListGroupsRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "path_prefix",
                "PathPrefix",
                TypeInfo(str),
            ),
            (
                "marker",
                "Marker",
                TypeInfo(str),
            ),
            (
                "max_items",
                "MaxItems",
                TypeInfo(int),
            ),
        ]

    # The path prefix for filtering the results. For example, the prefix
    # `/division_abc/subdivision_xyz/` gets all groups whose path starts with
    # `/division_abc/subdivision_xyz/`.

    # This parameter is optional. If it is not included, it defaults to a slash
    # (/), listing all groups. This parameter allows (per its [regex
    # pattern](http://wikipedia.org/wiki/regex)) a string of characters
    # consisting of either a forward slash (/) by itself or a string that must
    # begin and end with forward slashes. In addition, it can contain any ASCII
    # character from the ! (\u0021) through the DEL character (\u007F), including
    # most punctuation characters, digits, and upper and lowercased letters.
    path_prefix: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Use this parameter only when paginating results and only after you receive
    # a response indicating that the results are truncated. Set it to the value
    # of the `Marker` element in the response that you received to indicate where
    # the next call should start.
    marker: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # (Optional) Use this only when paginating results to indicate the maximum
    # number of items you want in the response. If additional items exist beyond
    # the maximum you specify, the `IsTruncated` response element is `true`.

    # If you do not include this parameter, it defaults to 100. Note that IAM
    # might return fewer results, even when there are more results available. In
    # that case, the `IsTruncated` response element returns `true` and `Marker`
    # contains a value to include in the subsequent call that tells the service
    # where to continue from.
    max_items: int = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ListGroupsResponse(OutputShapeBase):
    """
    Contains the response to a successful ListGroups request.
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
                "groups",
                "Groups",
                TypeInfo(typing.List[Group]),
            ),
            (
                "is_truncated",
                "IsTruncated",
                TypeInfo(bool),
            ),
            (
                "marker",
                "Marker",
                TypeInfo(str),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A list of groups.
    groups: typing.List["Group"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A flag that indicates whether there are more items to return. If your
    # results were truncated, you can make a subsequent pagination request using
    # the `Marker` request parameter to retrieve more items. Note that IAM might
    # return fewer than the `MaxItems` number of results even when there are more
    # results available. We recommend that you check `IsTruncated` after every
    # call to ensure that you receive all of your results.
    is_truncated: bool = dataclasses.field(default=ShapeBase.NOT_SET, )

    # When `IsTruncated` is `true`, this element is present and contains the
    # value to use for the `Marker` parameter in a subsequent pagination request.
    marker: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    def paginate(self, ) -> typing.Generator["ListGroupsResponse", None, None]:
        yield from super()._paginate()


@dataclasses.dataclass
class ListInstanceProfilesForRoleRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "role_name",
                "RoleName",
                TypeInfo(str),
            ),
            (
                "marker",
                "Marker",
                TypeInfo(str),
            ),
            (
                "max_items",
                "MaxItems",
                TypeInfo(int),
            ),
        ]

    # The name of the role to list instance profiles for.

    # This parameter allows (per its [regex
    # pattern](http://wikipedia.org/wiki/regex)) a string of characters
    # consisting of upper and lowercase alphanumeric characters with no spaces.
    # You can also include any of the following characters: _+=,.@-
    role_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Use this parameter only when paginating results and only after you receive
    # a response indicating that the results are truncated. Set it to the value
    # of the `Marker` element in the response that you received to indicate where
    # the next call should start.
    marker: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # (Optional) Use this only when paginating results to indicate the maximum
    # number of items you want in the response. If additional items exist beyond
    # the maximum you specify, the `IsTruncated` response element is `true`.

    # If you do not include this parameter, it defaults to 100. Note that IAM
    # might return fewer results, even when there are more results available. In
    # that case, the `IsTruncated` response element returns `true` and `Marker`
    # contains a value to include in the subsequent call that tells the service
    # where to continue from.
    max_items: int = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ListInstanceProfilesForRoleResponse(OutputShapeBase):
    """
    Contains the response to a successful ListInstanceProfilesForRole request.
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
                "instance_profiles",
                "InstanceProfiles",
                TypeInfo(typing.List[InstanceProfile]),
            ),
            (
                "is_truncated",
                "IsTruncated",
                TypeInfo(bool),
            ),
            (
                "marker",
                "Marker",
                TypeInfo(str),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A list of instance profiles.
    instance_profiles: typing.List["InstanceProfile"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A flag that indicates whether there are more items to return. If your
    # results were truncated, you can make a subsequent pagination request using
    # the `Marker` request parameter to retrieve more items. Note that IAM might
    # return fewer than the `MaxItems` number of results even when there are more
    # results available. We recommend that you check `IsTruncated` after every
    # call to ensure that you receive all of your results.
    is_truncated: bool = dataclasses.field(default=ShapeBase.NOT_SET, )

    # When `IsTruncated` is `true`, this element is present and contains the
    # value to use for the `Marker` parameter in a subsequent pagination request.
    marker: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    def paginate(
        self,
    ) -> typing.Generator["ListInstanceProfilesForRoleResponse", None, None]:
        yield from super()._paginate()


@dataclasses.dataclass
class ListInstanceProfilesRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "path_prefix",
                "PathPrefix",
                TypeInfo(str),
            ),
            (
                "marker",
                "Marker",
                TypeInfo(str),
            ),
            (
                "max_items",
                "MaxItems",
                TypeInfo(int),
            ),
        ]

    # The path prefix for filtering the results. For example, the prefix
    # `/application_abc/component_xyz/` gets all instance profiles whose path
    # starts with `/application_abc/component_xyz/`.

    # This parameter is optional. If it is not included, it defaults to a slash
    # (/), listing all instance profiles. This parameter allows (per its [regex
    # pattern](http://wikipedia.org/wiki/regex)) a string of characters
    # consisting of either a forward slash (/) by itself or a string that must
    # begin and end with forward slashes. In addition, it can contain any ASCII
    # character from the ! (\u0021) through the DEL character (\u007F), including
    # most punctuation characters, digits, and upper and lowercased letters.
    path_prefix: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Use this parameter only when paginating results and only after you receive
    # a response indicating that the results are truncated. Set it to the value
    # of the `Marker` element in the response that you received to indicate where
    # the next call should start.
    marker: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # (Optional) Use this only when paginating results to indicate the maximum
    # number of items you want in the response. If additional items exist beyond
    # the maximum you specify, the `IsTruncated` response element is `true`.

    # If you do not include this parameter, it defaults to 100. Note that IAM
    # might return fewer results, even when there are more results available. In
    # that case, the `IsTruncated` response element returns `true` and `Marker`
    # contains a value to include in the subsequent call that tells the service
    # where to continue from.
    max_items: int = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ListInstanceProfilesResponse(OutputShapeBase):
    """
    Contains the response to a successful ListInstanceProfiles request.
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
                "instance_profiles",
                "InstanceProfiles",
                TypeInfo(typing.List[InstanceProfile]),
            ),
            (
                "is_truncated",
                "IsTruncated",
                TypeInfo(bool),
            ),
            (
                "marker",
                "Marker",
                TypeInfo(str),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A list of instance profiles.
    instance_profiles: typing.List["InstanceProfile"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A flag that indicates whether there are more items to return. If your
    # results were truncated, you can make a subsequent pagination request using
    # the `Marker` request parameter to retrieve more items. Note that IAM might
    # return fewer than the `MaxItems` number of results even when there are more
    # results available. We recommend that you check `IsTruncated` after every
    # call to ensure that you receive all of your results.
    is_truncated: bool = dataclasses.field(default=ShapeBase.NOT_SET, )

    # When `IsTruncated` is `true`, this element is present and contains the
    # value to use for the `Marker` parameter in a subsequent pagination request.
    marker: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    def paginate(
        self,
    ) -> typing.Generator["ListInstanceProfilesResponse", None, None]:
        yield from super()._paginate()


@dataclasses.dataclass
class ListMFADevicesRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "user_name",
                "UserName",
                TypeInfo(str),
            ),
            (
                "marker",
                "Marker",
                TypeInfo(str),
            ),
            (
                "max_items",
                "MaxItems",
                TypeInfo(int),
            ),
        ]

    # The name of the user whose MFA devices you want to list.

    # This parameter allows (per its [regex
    # pattern](http://wikipedia.org/wiki/regex)) a string of characters
    # consisting of upper and lowercase alphanumeric characters with no spaces.
    # You can also include any of the following characters: _+=,.@-
    user_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Use this parameter only when paginating results and only after you receive
    # a response indicating that the results are truncated. Set it to the value
    # of the `Marker` element in the response that you received to indicate where
    # the next call should start.
    marker: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # (Optional) Use this only when paginating results to indicate the maximum
    # number of items you want in the response. If additional items exist beyond
    # the maximum you specify, the `IsTruncated` response element is `true`.

    # If you do not include this parameter, it defaults to 100. Note that IAM
    # might return fewer results, even when there are more results available. In
    # that case, the `IsTruncated` response element returns `true` and `Marker`
    # contains a value to include in the subsequent call that tells the service
    # where to continue from.
    max_items: int = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ListMFADevicesResponse(OutputShapeBase):
    """
    Contains the response to a successful ListMFADevices request.
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
                "mfa_devices",
                "MFADevices",
                TypeInfo(typing.List[MFADevice]),
            ),
            (
                "is_truncated",
                "IsTruncated",
                TypeInfo(bool),
            ),
            (
                "marker",
                "Marker",
                TypeInfo(str),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A list of MFA devices.
    mfa_devices: typing.List["MFADevice"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A flag that indicates whether there are more items to return. If your
    # results were truncated, you can make a subsequent pagination request using
    # the `Marker` request parameter to retrieve more items. Note that IAM might
    # return fewer than the `MaxItems` number of results even when there are more
    # results available. We recommend that you check `IsTruncated` after every
    # call to ensure that you receive all of your results.
    is_truncated: bool = dataclasses.field(default=ShapeBase.NOT_SET, )

    # When `IsTruncated` is `true`, this element is present and contains the
    # value to use for the `Marker` parameter in a subsequent pagination request.
    marker: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    def paginate(self,
                ) -> typing.Generator["ListMFADevicesResponse", None, None]:
        yield from super()._paginate()


@dataclasses.dataclass
class ListOpenIDConnectProvidersRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class ListOpenIDConnectProvidersResponse(OutputShapeBase):
    """
    Contains the response to a successful ListOpenIDConnectProviders request.
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
                "open_id_connect_provider_list",
                "OpenIDConnectProviderList",
                TypeInfo(typing.List[OpenIDConnectProviderListEntry]),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The list of IAM OIDC provider resource objects defined in the AWS account.
    open_id_connect_provider_list: typing.List["OpenIDConnectProviderListEntry"
                                              ] = dataclasses.field(
                                                  default=ShapeBase.NOT_SET,
                                              )


@dataclasses.dataclass
class ListPoliciesRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "scope",
                "Scope",
                TypeInfo(typing.Union[str, policyScopeType]),
            ),
            (
                "only_attached",
                "OnlyAttached",
                TypeInfo(bool),
            ),
            (
                "path_prefix",
                "PathPrefix",
                TypeInfo(str),
            ),
            (
                "policy_usage_filter",
                "PolicyUsageFilter",
                TypeInfo(typing.Union[str, PolicyUsageType]),
            ),
            (
                "marker",
                "Marker",
                TypeInfo(str),
            ),
            (
                "max_items",
                "MaxItems",
                TypeInfo(int),
            ),
        ]

    # The scope to use for filtering the results.

    # To list only AWS managed policies, set `Scope` to `AWS`. To list only the
    # customer managed policies in your AWS account, set `Scope` to `Local`.

    # This parameter is optional. If it is not included, or if it is set to
    # `All`, all policies are returned.
    scope: typing.Union[str, "policyScopeType"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A flag to filter the results to only the attached policies.

    # When `OnlyAttached` is `true`, the returned list contains only the policies
    # that are attached to an IAM user, group, or role. When `OnlyAttached` is
    # `false`, or when the parameter is not included, all policies are returned.
    only_attached: bool = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The path prefix for filtering the results. This parameter is optional. If
    # it is not included, it defaults to a slash (/), listing all policies. This
    # parameter allows (per its [regex pattern](http://wikipedia.org/wiki/regex))
    # a string of characters consisting of either a forward slash (/) by itself
    # or a string that must begin and end with forward slashes. In addition, it
    # can contain any ASCII character from the ! (\u0021) through the DEL
    # character (\u007F), including most punctuation characters, digits, and
    # upper and lowercased letters.
    path_prefix: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The policy usage method to use for filtering the results.

    # To list only permissions policies, set `PolicyUsageFilter` to
    # `PermissionsPolicy`. To list only the policies used to set permissions
    # boundaries, set the value to `PermissionsBoundary`.

    # This parameter is optional. If it is not included, all policies are
    # returned.
    policy_usage_filter: typing.Union[str, "PolicyUsageType"
                                     ] = dataclasses.field(
                                         default=ShapeBase.NOT_SET,
                                     )

    # Use this parameter only when paginating results and only after you receive
    # a response indicating that the results are truncated. Set it to the value
    # of the `Marker` element in the response that you received to indicate where
    # the next call should start.
    marker: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # (Optional) Use this only when paginating results to indicate the maximum
    # number of items you want in the response. If additional items exist beyond
    # the maximum you specify, the `IsTruncated` response element is `true`.

    # If you do not include this parameter, it defaults to 100. Note that IAM
    # might return fewer results, even when there are more results available. In
    # that case, the `IsTruncated` response element returns `true` and `Marker`
    # contains a value to include in the subsequent call that tells the service
    # where to continue from.
    max_items: int = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ListPoliciesResponse(OutputShapeBase):
    """
    Contains the response to a successful ListPolicies request.
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
                "policies",
                "Policies",
                TypeInfo(typing.List[Policy]),
            ),
            (
                "is_truncated",
                "IsTruncated",
                TypeInfo(bool),
            ),
            (
                "marker",
                "Marker",
                TypeInfo(str),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A list of policies.
    policies: typing.List["Policy"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A flag that indicates whether there are more items to return. If your
    # results were truncated, you can make a subsequent pagination request using
    # the `Marker` request parameter to retrieve more items. Note that IAM might
    # return fewer than the `MaxItems` number of results even when there are more
    # results available. We recommend that you check `IsTruncated` after every
    # call to ensure that you receive all of your results.
    is_truncated: bool = dataclasses.field(default=ShapeBase.NOT_SET, )

    # When `IsTruncated` is `true`, this element is present and contains the
    # value to use for the `Marker` parameter in a subsequent pagination request.
    marker: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    def paginate(self,
                ) -> typing.Generator["ListPoliciesResponse", None, None]:
        yield from super()._paginate()


@dataclasses.dataclass
class ListPolicyVersionsRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "policy_arn",
                "PolicyArn",
                TypeInfo(str),
            ),
            (
                "marker",
                "Marker",
                TypeInfo(str),
            ),
            (
                "max_items",
                "MaxItems",
                TypeInfo(int),
            ),
        ]

    # The Amazon Resource Name (ARN) of the IAM policy for which you want the
    # versions.

    # For more information about ARNs, see [Amazon Resource Names (ARNs) and AWS
    # Service Namespaces](http://docs.aws.amazon.com/general/latest/gr/aws-arns-
    # and-namespaces.html) in the _AWS General Reference_.
    policy_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Use this parameter only when paginating results and only after you receive
    # a response indicating that the results are truncated. Set it to the value
    # of the `Marker` element in the response that you received to indicate where
    # the next call should start.
    marker: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # (Optional) Use this only when paginating results to indicate the maximum
    # number of items you want in the response. If additional items exist beyond
    # the maximum you specify, the `IsTruncated` response element is `true`.

    # If you do not include this parameter, it defaults to 100. Note that IAM
    # might return fewer results, even when there are more results available. In
    # that case, the `IsTruncated` response element returns `true` and `Marker`
    # contains a value to include in the subsequent call that tells the service
    # where to continue from.
    max_items: int = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ListPolicyVersionsResponse(OutputShapeBase):
    """
    Contains the response to a successful ListPolicyVersions request.
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
                "versions",
                "Versions",
                TypeInfo(typing.List[PolicyVersion]),
            ),
            (
                "is_truncated",
                "IsTruncated",
                TypeInfo(bool),
            ),
            (
                "marker",
                "Marker",
                TypeInfo(str),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A list of policy versions.

    # For more information about managed policy versions, see [Versioning for
    # Managed Policies](http://docs.aws.amazon.com/IAM/latest/UserGuide/policies-
    # managed-versions.html) in the _IAM User Guide_.
    versions: typing.List["PolicyVersion"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A flag that indicates whether there are more items to return. If your
    # results were truncated, you can make a subsequent pagination request using
    # the `Marker` request parameter to retrieve more items. Note that IAM might
    # return fewer than the `MaxItems` number of results even when there are more
    # results available. We recommend that you check `IsTruncated` after every
    # call to ensure that you receive all of your results.
    is_truncated: bool = dataclasses.field(default=ShapeBase.NOT_SET, )

    # When `IsTruncated` is `true`, this element is present and contains the
    # value to use for the `Marker` parameter in a subsequent pagination request.
    marker: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    def paginate(self,
                ) -> typing.Generator["ListPolicyVersionsResponse", None, None]:
        yield from super()._paginate()


@dataclasses.dataclass
class ListRolePoliciesRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "role_name",
                "RoleName",
                TypeInfo(str),
            ),
            (
                "marker",
                "Marker",
                TypeInfo(str),
            ),
            (
                "max_items",
                "MaxItems",
                TypeInfo(int),
            ),
        ]

    # The name of the role to list policies for.

    # This parameter allows (per its [regex
    # pattern](http://wikipedia.org/wiki/regex)) a string of characters
    # consisting of upper and lowercase alphanumeric characters with no spaces.
    # You can also include any of the following characters: _+=,.@-
    role_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Use this parameter only when paginating results and only after you receive
    # a response indicating that the results are truncated. Set it to the value
    # of the `Marker` element in the response that you received to indicate where
    # the next call should start.
    marker: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # (Optional) Use this only when paginating results to indicate the maximum
    # number of items you want in the response. If additional items exist beyond
    # the maximum you specify, the `IsTruncated` response element is `true`.

    # If you do not include this parameter, it defaults to 100. Note that IAM
    # might return fewer results, even when there are more results available. In
    # that case, the `IsTruncated` response element returns `true` and `Marker`
    # contains a value to include in the subsequent call that tells the service
    # where to continue from.
    max_items: int = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ListRolePoliciesResponse(OutputShapeBase):
    """
    Contains the response to a successful ListRolePolicies request.
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
                "policy_names",
                "PolicyNames",
                TypeInfo(typing.List[str]),
            ),
            (
                "is_truncated",
                "IsTruncated",
                TypeInfo(bool),
            ),
            (
                "marker",
                "Marker",
                TypeInfo(str),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A list of policy names.
    policy_names: typing.List[str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A flag that indicates whether there are more items to return. If your
    # results were truncated, you can make a subsequent pagination request using
    # the `Marker` request parameter to retrieve more items. Note that IAM might
    # return fewer than the `MaxItems` number of results even when there are more
    # results available. We recommend that you check `IsTruncated` after every
    # call to ensure that you receive all of your results.
    is_truncated: bool = dataclasses.field(default=ShapeBase.NOT_SET, )

    # When `IsTruncated` is `true`, this element is present and contains the
    # value to use for the `Marker` parameter in a subsequent pagination request.
    marker: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    def paginate(self,
                ) -> typing.Generator["ListRolePoliciesResponse", None, None]:
        yield from super()._paginate()


@dataclasses.dataclass
class ListRolesRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "path_prefix",
                "PathPrefix",
                TypeInfo(str),
            ),
            (
                "marker",
                "Marker",
                TypeInfo(str),
            ),
            (
                "max_items",
                "MaxItems",
                TypeInfo(int),
            ),
        ]

    # The path prefix for filtering the results. For example, the prefix
    # `/application_abc/component_xyz/` gets all roles whose path starts with
    # `/application_abc/component_xyz/`.

    # This parameter is optional. If it is not included, it defaults to a slash
    # (/), listing all roles. This parameter allows (per its [regex
    # pattern](http://wikipedia.org/wiki/regex)) a string of characters
    # consisting of either a forward slash (/) by itself or a string that must
    # begin and end with forward slashes. In addition, it can contain any ASCII
    # character from the ! (\u0021) through the DEL character (\u007F), including
    # most punctuation characters, digits, and upper and lowercased letters.
    path_prefix: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Use this parameter only when paginating results and only after you receive
    # a response indicating that the results are truncated. Set it to the value
    # of the `Marker` element in the response that you received to indicate where
    # the next call should start.
    marker: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # (Optional) Use this only when paginating results to indicate the maximum
    # number of items you want in the response. If additional items exist beyond
    # the maximum you specify, the `IsTruncated` response element is `true`.

    # If you do not include this parameter, it defaults to 100. Note that IAM
    # might return fewer results, even when there are more results available. In
    # that case, the `IsTruncated` response element returns `true` and `Marker`
    # contains a value to include in the subsequent call that tells the service
    # where to continue from.
    max_items: int = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ListRolesResponse(OutputShapeBase):
    """
    Contains the response to a successful ListRoles request.
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
                "roles",
                "Roles",
                TypeInfo(typing.List[Role]),
            ),
            (
                "is_truncated",
                "IsTruncated",
                TypeInfo(bool),
            ),
            (
                "marker",
                "Marker",
                TypeInfo(str),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A list of roles.
    roles: typing.List["Role"] = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A flag that indicates whether there are more items to return. If your
    # results were truncated, you can make a subsequent pagination request using
    # the `Marker` request parameter to retrieve more items. Note that IAM might
    # return fewer than the `MaxItems` number of results even when there are more
    # results available. We recommend that you check `IsTruncated` after every
    # call to ensure that you receive all of your results.
    is_truncated: bool = dataclasses.field(default=ShapeBase.NOT_SET, )

    # When `IsTruncated` is `true`, this element is present and contains the
    # value to use for the `Marker` parameter in a subsequent pagination request.
    marker: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    def paginate(self, ) -> typing.Generator["ListRolesResponse", None, None]:
        yield from super()._paginate()


@dataclasses.dataclass
class ListSAMLProvidersRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class ListSAMLProvidersResponse(OutputShapeBase):
    """
    Contains the response to a successful ListSAMLProviders request.
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
                "saml_provider_list",
                "SAMLProviderList",
                TypeInfo(typing.List[SAMLProviderListEntry]),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The list of SAML provider resource objects defined in IAM for this AWS
    # account.
    saml_provider_list: typing.List["SAMLProviderListEntry"
                                   ] = dataclasses.field(
                                       default=ShapeBase.NOT_SET,
                                   )


@dataclasses.dataclass
class ListSSHPublicKeysRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "user_name",
                "UserName",
                TypeInfo(str),
            ),
            (
                "marker",
                "Marker",
                TypeInfo(str),
            ),
            (
                "max_items",
                "MaxItems",
                TypeInfo(int),
            ),
        ]

    # The name of the IAM user to list SSH public keys for. If none is specified,
    # the `UserName` field is determined implicitly based on the AWS access key
    # used to sign the request.

    # This parameter allows (per its [regex
    # pattern](http://wikipedia.org/wiki/regex)) a string of characters
    # consisting of upper and lowercase alphanumeric characters with no spaces.
    # You can also include any of the following characters: _+=,.@-
    user_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Use this parameter only when paginating results and only after you receive
    # a response indicating that the results are truncated. Set it to the value
    # of the `Marker` element in the response that you received to indicate where
    # the next call should start.
    marker: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # (Optional) Use this only when paginating results to indicate the maximum
    # number of items you want in the response. If additional items exist beyond
    # the maximum you specify, the `IsTruncated` response element is `true`.

    # If you do not include this parameter, it defaults to 100. Note that IAM
    # might return fewer results, even when there are more results available. In
    # that case, the `IsTruncated` response element returns `true` and `Marker`
    # contains a value to include in the subsequent call that tells the service
    # where to continue from.
    max_items: int = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ListSSHPublicKeysResponse(OutputShapeBase):
    """
    Contains the response to a successful ListSSHPublicKeys request.
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
                "ssh_public_keys",
                "SSHPublicKeys",
                TypeInfo(typing.List[SSHPublicKeyMetadata]),
            ),
            (
                "is_truncated",
                "IsTruncated",
                TypeInfo(bool),
            ),
            (
                "marker",
                "Marker",
                TypeInfo(str),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A list of the SSH public keys assigned to IAM user.
    ssh_public_keys: typing.List["SSHPublicKeyMetadata"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A flag that indicates whether there are more items to return. If your
    # results were truncated, you can make a subsequent pagination request using
    # the `Marker` request parameter to retrieve more items. Note that IAM might
    # return fewer than the `MaxItems` number of results even when there are more
    # results available. We recommend that you check `IsTruncated` after every
    # call to ensure that you receive all of your results.
    is_truncated: bool = dataclasses.field(default=ShapeBase.NOT_SET, )

    # When `IsTruncated` is `true`, this element is present and contains the
    # value to use for the `Marker` parameter in a subsequent pagination request.
    marker: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    def paginate(self,
                ) -> typing.Generator["ListSSHPublicKeysResponse", None, None]:
        yield from super()._paginate()


@dataclasses.dataclass
class ListServerCertificatesRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "path_prefix",
                "PathPrefix",
                TypeInfo(str),
            ),
            (
                "marker",
                "Marker",
                TypeInfo(str),
            ),
            (
                "max_items",
                "MaxItems",
                TypeInfo(int),
            ),
        ]

    # The path prefix for filtering the results. For example:
    # `/company/servercerts` would get all server certificates for which the path
    # starts with `/company/servercerts`.

    # This parameter is optional. If it is not included, it defaults to a slash
    # (/), listing all server certificates. This parameter allows (per its [regex
    # pattern](http://wikipedia.org/wiki/regex)) a string of characters
    # consisting of either a forward slash (/) by itself or a string that must
    # begin and end with forward slashes. In addition, it can contain any ASCII
    # character from the ! (\u0021) through the DEL character (\u007F), including
    # most punctuation characters, digits, and upper and lowercased letters.
    path_prefix: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Use this parameter only when paginating results and only after you receive
    # a response indicating that the results are truncated. Set it to the value
    # of the `Marker` element in the response that you received to indicate where
    # the next call should start.
    marker: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # (Optional) Use this only when paginating results to indicate the maximum
    # number of items you want in the response. If additional items exist beyond
    # the maximum you specify, the `IsTruncated` response element is `true`.

    # If you do not include this parameter, it defaults to 100. Note that IAM
    # might return fewer results, even when there are more results available. In
    # that case, the `IsTruncated` response element returns `true` and `Marker`
    # contains a value to include in the subsequent call that tells the service
    # where to continue from.
    max_items: int = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ListServerCertificatesResponse(OutputShapeBase):
    """
    Contains the response to a successful ListServerCertificates request.
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
                "server_certificate_metadata_list",
                "ServerCertificateMetadataList",
                TypeInfo(typing.List[ServerCertificateMetadata]),
            ),
            (
                "is_truncated",
                "IsTruncated",
                TypeInfo(bool),
            ),
            (
                "marker",
                "Marker",
                TypeInfo(str),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A list of server certificates.
    server_certificate_metadata_list: typing.List["ServerCertificateMetadata"
                                                 ] = dataclasses.field(
                                                     default=ShapeBase.NOT_SET,
                                                 )

    # A flag that indicates whether there are more items to return. If your
    # results were truncated, you can make a subsequent pagination request using
    # the `Marker` request parameter to retrieve more items. Note that IAM might
    # return fewer than the `MaxItems` number of results even when there are more
    # results available. We recommend that you check `IsTruncated` after every
    # call to ensure that you receive all of your results.
    is_truncated: bool = dataclasses.field(default=ShapeBase.NOT_SET, )

    # When `IsTruncated` is `true`, this element is present and contains the
    # value to use for the `Marker` parameter in a subsequent pagination request.
    marker: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    def paginate(
        self,
    ) -> typing.Generator["ListServerCertificatesResponse", None, None]:
        yield from super()._paginate()


@dataclasses.dataclass
class ListServiceSpecificCredentialsRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "user_name",
                "UserName",
                TypeInfo(str),
            ),
            (
                "service_name",
                "ServiceName",
                TypeInfo(str),
            ),
        ]

    # The name of the user whose service-specific credentials you want
    # information about. If this value is not specified, then the operation
    # assumes the user whose credentials are used to call the operation.

    # This parameter allows (per its [regex
    # pattern](http://wikipedia.org/wiki/regex)) a string of characters
    # consisting of upper and lowercase alphanumeric characters with no spaces.
    # You can also include any of the following characters: _+=,.@-
    user_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Filters the returned results to only those for the specified AWS service.
    # If not specified, then AWS returns service-specific credentials for all
    # services.
    service_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ListServiceSpecificCredentialsResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "service_specific_credentials",
                "ServiceSpecificCredentials",
                TypeInfo(typing.List[ServiceSpecificCredentialMetadata]),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A list of structures that each contain details about a service-specific
    # credential.
    service_specific_credentials: typing.List[
        "ServiceSpecificCredentialMetadata"] = dataclasses.field(
            default=ShapeBase.NOT_SET,
        )


@dataclasses.dataclass
class ListSigningCertificatesRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "user_name",
                "UserName",
                TypeInfo(str),
            ),
            (
                "marker",
                "Marker",
                TypeInfo(str),
            ),
            (
                "max_items",
                "MaxItems",
                TypeInfo(int),
            ),
        ]

    # The name of the IAM user whose signing certificates you want to examine.

    # This parameter allows (per its [regex
    # pattern](http://wikipedia.org/wiki/regex)) a string of characters
    # consisting of upper and lowercase alphanumeric characters with no spaces.
    # You can also include any of the following characters: _+=,.@-
    user_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Use this parameter only when paginating results and only after you receive
    # a response indicating that the results are truncated. Set it to the value
    # of the `Marker` element in the response that you received to indicate where
    # the next call should start.
    marker: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # (Optional) Use this only when paginating results to indicate the maximum
    # number of items you want in the response. If additional items exist beyond
    # the maximum you specify, the `IsTruncated` response element is `true`.

    # If you do not include this parameter, it defaults to 100. Note that IAM
    # might return fewer results, even when there are more results available. In
    # that case, the `IsTruncated` response element returns `true` and `Marker`
    # contains a value to include in the subsequent call that tells the service
    # where to continue from.
    max_items: int = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ListSigningCertificatesResponse(OutputShapeBase):
    """
    Contains the response to a successful ListSigningCertificates request.
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
                "certificates",
                "Certificates",
                TypeInfo(typing.List[SigningCertificate]),
            ),
            (
                "is_truncated",
                "IsTruncated",
                TypeInfo(bool),
            ),
            (
                "marker",
                "Marker",
                TypeInfo(str),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A list of the user's signing certificate information.
    certificates: typing.List["SigningCertificate"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A flag that indicates whether there are more items to return. If your
    # results were truncated, you can make a subsequent pagination request using
    # the `Marker` request parameter to retrieve more items. Note that IAM might
    # return fewer than the `MaxItems` number of results even when there are more
    # results available. We recommend that you check `IsTruncated` after every
    # call to ensure that you receive all of your results.
    is_truncated: bool = dataclasses.field(default=ShapeBase.NOT_SET, )

    # When `IsTruncated` is `true`, this element is present and contains the
    # value to use for the `Marker` parameter in a subsequent pagination request.
    marker: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    def paginate(
        self,
    ) -> typing.Generator["ListSigningCertificatesResponse", None, None]:
        yield from super()._paginate()


@dataclasses.dataclass
class ListUserPoliciesRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "user_name",
                "UserName",
                TypeInfo(str),
            ),
            (
                "marker",
                "Marker",
                TypeInfo(str),
            ),
            (
                "max_items",
                "MaxItems",
                TypeInfo(int),
            ),
        ]

    # The name of the user to list policies for.

    # This parameter allows (per its [regex
    # pattern](http://wikipedia.org/wiki/regex)) a string of characters
    # consisting of upper and lowercase alphanumeric characters with no spaces.
    # You can also include any of the following characters: _+=,.@-
    user_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Use this parameter only when paginating results and only after you receive
    # a response indicating that the results are truncated. Set it to the value
    # of the `Marker` element in the response that you received to indicate where
    # the next call should start.
    marker: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # (Optional) Use this only when paginating results to indicate the maximum
    # number of items you want in the response. If additional items exist beyond
    # the maximum you specify, the `IsTruncated` response element is `true`.

    # If you do not include this parameter, it defaults to 100. Note that IAM
    # might return fewer results, even when there are more results available. In
    # that case, the `IsTruncated` response element returns `true` and `Marker`
    # contains a value to include in the subsequent call that tells the service
    # where to continue from.
    max_items: int = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ListUserPoliciesResponse(OutputShapeBase):
    """
    Contains the response to a successful ListUserPolicies request.
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
                "policy_names",
                "PolicyNames",
                TypeInfo(typing.List[str]),
            ),
            (
                "is_truncated",
                "IsTruncated",
                TypeInfo(bool),
            ),
            (
                "marker",
                "Marker",
                TypeInfo(str),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A list of policy names.
    policy_names: typing.List[str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A flag that indicates whether there are more items to return. If your
    # results were truncated, you can make a subsequent pagination request using
    # the `Marker` request parameter to retrieve more items. Note that IAM might
    # return fewer than the `MaxItems` number of results even when there are more
    # results available. We recommend that you check `IsTruncated` after every
    # call to ensure that you receive all of your results.
    is_truncated: bool = dataclasses.field(default=ShapeBase.NOT_SET, )

    # When `IsTruncated` is `true`, this element is present and contains the
    # value to use for the `Marker` parameter in a subsequent pagination request.
    marker: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    def paginate(self,
                ) -> typing.Generator["ListUserPoliciesResponse", None, None]:
        yield from super()._paginate()


@dataclasses.dataclass
class ListUsersRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "path_prefix",
                "PathPrefix",
                TypeInfo(str),
            ),
            (
                "marker",
                "Marker",
                TypeInfo(str),
            ),
            (
                "max_items",
                "MaxItems",
                TypeInfo(int),
            ),
        ]

    # The path prefix for filtering the results. For example:
    # `/division_abc/subdivision_xyz/`, which would get all user names whose path
    # starts with `/division_abc/subdivision_xyz/`.

    # This parameter is optional. If it is not included, it defaults to a slash
    # (/), listing all user names. This parameter allows (per its [regex
    # pattern](http://wikipedia.org/wiki/regex)) a string of characters
    # consisting of either a forward slash (/) by itself or a string that must
    # begin and end with forward slashes. In addition, it can contain any ASCII
    # character from the ! (\u0021) through the DEL character (\u007F), including
    # most punctuation characters, digits, and upper and lowercased letters.
    path_prefix: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Use this parameter only when paginating results and only after you receive
    # a response indicating that the results are truncated. Set it to the value
    # of the `Marker` element in the response that you received to indicate where
    # the next call should start.
    marker: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # (Optional) Use this only when paginating results to indicate the maximum
    # number of items you want in the response. If additional items exist beyond
    # the maximum you specify, the `IsTruncated` response element is `true`.

    # If you do not include this parameter, it defaults to 100. Note that IAM
    # might return fewer results, even when there are more results available. In
    # that case, the `IsTruncated` response element returns `true` and `Marker`
    # contains a value to include in the subsequent call that tells the service
    # where to continue from.
    max_items: int = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ListUsersResponse(OutputShapeBase):
    """
    Contains the response to a successful ListUsers request.
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
                "users",
                "Users",
                TypeInfo(typing.List[User]),
            ),
            (
                "is_truncated",
                "IsTruncated",
                TypeInfo(bool),
            ),
            (
                "marker",
                "Marker",
                TypeInfo(str),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A list of users.
    users: typing.List["User"] = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A flag that indicates whether there are more items to return. If your
    # results were truncated, you can make a subsequent pagination request using
    # the `Marker` request parameter to retrieve more items. Note that IAM might
    # return fewer than the `MaxItems` number of results even when there are more
    # results available. We recommend that you check `IsTruncated` after every
    # call to ensure that you receive all of your results.
    is_truncated: bool = dataclasses.field(default=ShapeBase.NOT_SET, )

    # When `IsTruncated` is `true`, this element is present and contains the
    # value to use for the `Marker` parameter in a subsequent pagination request.
    marker: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    def paginate(self, ) -> typing.Generator["ListUsersResponse", None, None]:
        yield from super()._paginate()


@dataclasses.dataclass
class ListVirtualMFADevicesRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "assignment_status",
                "AssignmentStatus",
                TypeInfo(typing.Union[str, assignmentStatusType]),
            ),
            (
                "marker",
                "Marker",
                TypeInfo(str),
            ),
            (
                "max_items",
                "MaxItems",
                TypeInfo(int),
            ),
        ]

    # The status (`Unassigned` or `Assigned`) of the devices to list. If you do
    # not specify an `AssignmentStatus`, the operation defaults to `Any` which
    # lists both assigned and unassigned virtual MFA devices.
    assignment_status: typing.Union[str, "assignmentStatusType"
                                   ] = dataclasses.field(
                                       default=ShapeBase.NOT_SET,
                                   )

    # Use this parameter only when paginating results and only after you receive
    # a response indicating that the results are truncated. Set it to the value
    # of the `Marker` element in the response that you received to indicate where
    # the next call should start.
    marker: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # (Optional) Use this only when paginating results to indicate the maximum
    # number of items you want in the response. If additional items exist beyond
    # the maximum you specify, the `IsTruncated` response element is `true`.

    # If you do not include this parameter, it defaults to 100. Note that IAM
    # might return fewer results, even when there are more results available. In
    # that case, the `IsTruncated` response element returns `true` and `Marker`
    # contains a value to include in the subsequent call that tells the service
    # where to continue from.
    max_items: int = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ListVirtualMFADevicesResponse(OutputShapeBase):
    """
    Contains the response to a successful ListVirtualMFADevices request.
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
                "virtual_mfa_devices",
                "VirtualMFADevices",
                TypeInfo(typing.List[VirtualMFADevice]),
            ),
            (
                "is_truncated",
                "IsTruncated",
                TypeInfo(bool),
            ),
            (
                "marker",
                "Marker",
                TypeInfo(str),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The list of virtual MFA devices in the current account that match the
    # `AssignmentStatus` value that was passed in the request.
    virtual_mfa_devices: typing.List["VirtualMFADevice"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A flag that indicates whether there are more items to return. If your
    # results were truncated, you can make a subsequent pagination request using
    # the `Marker` request parameter to retrieve more items. Note that IAM might
    # return fewer than the `MaxItems` number of results even when there are more
    # results available. We recommend that you check `IsTruncated` after every
    # call to ensure that you receive all of your results.
    is_truncated: bool = dataclasses.field(default=ShapeBase.NOT_SET, )

    # When `IsTruncated` is `true`, this element is present and contains the
    # value to use for the `Marker` parameter in a subsequent pagination request.
    marker: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    def paginate(
        self,
    ) -> typing.Generator["ListVirtualMFADevicesResponse", None, None]:
        yield from super()._paginate()


@dataclasses.dataclass
class LoginProfile(ShapeBase):
    """
    Contains the user name and password create date for a user.

    This data type is used as a response element in the CreateLoginProfile and
    GetLoginProfile operations.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "user_name",
                "UserName",
                TypeInfo(str),
            ),
            (
                "create_date",
                "CreateDate",
                TypeInfo(datetime.datetime),
            ),
            (
                "password_reset_required",
                "PasswordResetRequired",
                TypeInfo(bool),
            ),
        ]

    # The name of the user, which can be used for signing in to the AWS
    # Management Console.
    user_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The date when the password for the user was created.
    create_date: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Specifies whether the user is required to set a new password on next sign-
    # in.
    password_reset_required: bool = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class MFADevice(ShapeBase):
    """
    Contains information about an MFA device.

    This data type is used as a response element in the ListMFADevices operation.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "user_name",
                "UserName",
                TypeInfo(str),
            ),
            (
                "serial_number",
                "SerialNumber",
                TypeInfo(str),
            ),
            (
                "enable_date",
                "EnableDate",
                TypeInfo(datetime.datetime),
            ),
        ]

    # The user with whom the MFA device is associated.
    user_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The serial number that uniquely identifies the MFA device. For virtual MFA
    # devices, the serial number is the device ARN.
    serial_number: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The date when the MFA device was enabled for the user.
    enable_date: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class MalformedCertificateException(ShapeBase):
    """
    The request was rejected because the certificate was malformed or expired. The
    error message describes the specific error.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "message",
                "message",
                TypeInfo(str),
            ),
        ]

    message: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class MalformedPolicyDocumentException(ShapeBase):
    """
    The request was rejected because the policy document was malformed. The error
    message describes the specific error.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "message",
                "message",
                TypeInfo(str),
            ),
        ]

    message: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ManagedPolicyDetail(ShapeBase):
    """
    Contains information about a managed policy, including the policy's ARN,
    versions, and the number of principal entities (users, groups, and roles) that
    the policy is attached to.

    This data type is used as a response element in the
    GetAccountAuthorizationDetails operation.

    For more information about managed policies, see [Managed Policies and Inline
    Policies](http://docs.aws.amazon.com/IAM/latest/UserGuide/policies-managed-vs-
    inline.html) in the _Using IAM_ guide.
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
                "policy_id",
                "PolicyId",
                TypeInfo(str),
            ),
            (
                "arn",
                "Arn",
                TypeInfo(str),
            ),
            (
                "path",
                "Path",
                TypeInfo(str),
            ),
            (
                "default_version_id",
                "DefaultVersionId",
                TypeInfo(str),
            ),
            (
                "attachment_count",
                "AttachmentCount",
                TypeInfo(int),
            ),
            (
                "permissions_boundary_usage_count",
                "PermissionsBoundaryUsageCount",
                TypeInfo(int),
            ),
            (
                "is_attachable",
                "IsAttachable",
                TypeInfo(bool),
            ),
            (
                "description",
                "Description",
                TypeInfo(str),
            ),
            (
                "create_date",
                "CreateDate",
                TypeInfo(datetime.datetime),
            ),
            (
                "update_date",
                "UpdateDate",
                TypeInfo(datetime.datetime),
            ),
            (
                "policy_version_list",
                "PolicyVersionList",
                TypeInfo(typing.List[PolicyVersion]),
            ),
        ]

    # The friendly name (not ARN) identifying the policy.
    policy_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The stable and unique string identifying the policy.

    # For more information about IDs, see [IAM
    # Identifiers](http://docs.aws.amazon.com/IAM/latest/UserGuide/Using_Identifiers.html)
    # in the _Using IAM_ guide.
    policy_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The Amazon Resource Name (ARN). ARNs are unique identifiers for AWS
    # resources.

    # For more information about ARNs, go to [Amazon Resource Names (ARNs) and
    # AWS Service Namespaces](http://docs.aws.amazon.com/general/latest/gr/aws-
    # arns-and-namespaces.html) in the _AWS General Reference_.
    arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The path to the policy.

    # For more information about paths, see [IAM
    # Identifiers](http://docs.aws.amazon.com/IAM/latest/UserGuide/Using_Identifiers.html)
    # in the _Using IAM_ guide.
    path: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The identifier for the version of the policy that is set as the default
    # (operative) version.

    # For more information about policy versions, see [Versioning for Managed
    # Policies](http://docs.aws.amazon.com/IAM/latest/UserGuide/policies-managed-
    # versions.html) in the _Using IAM_ guide.
    default_version_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The number of principal entities (users, groups, and roles) that the policy
    # is attached to.
    attachment_count: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The number of entities (users and roles) for which the policy is used as
    # the permissions boundary.

    # For more information about permissions boundaries, see [Permissions
    # Boundaries for IAM Identities
    # ](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_boundaries.html)
    # in the _IAM User Guide_.
    permissions_boundary_usage_count: int = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Specifies whether the policy can be attached to an IAM user, group, or
    # role.
    is_attachable: bool = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A friendly description of the policy.
    description: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The date and time, in [ISO 8601 date-time
    # format](http://www.iso.org/iso/iso8601), when the policy was created.
    create_date: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The date and time, in [ISO 8601 date-time
    # format](http://www.iso.org/iso/iso8601), when the policy was last updated.

    # When a policy has only one version, this field contains the date and time
    # when the policy was created. When a policy has more than one version, this
    # field contains the date and time when the most recent policy version was
    # created.
    update_date: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A list containing information about the versions of the policy.
    policy_version_list: typing.List["PolicyVersion"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class NoSuchEntityException(ShapeBase):
    """
    The request was rejected because it referenced an entity that does not exist.
    The error message describes the entity.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "message",
                "message",
                TypeInfo(str),
            ),
        ]

    message: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class OpenIDConnectProviderListEntry(ShapeBase):
    """
    Contains the Amazon Resource Name (ARN) for an IAM OpenID Connect provider.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "arn",
                "Arn",
                TypeInfo(str),
            ),
        ]

    # The Amazon Resource Name (ARN). ARNs are unique identifiers for AWS
    # resources.

    # For more information about ARNs, go to [Amazon Resource Names (ARNs) and
    # AWS Service Namespaces](http://docs.aws.amazon.com/general/latest/gr/aws-
    # arns-and-namespaces.html) in the _AWS General Reference_.
    arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class OrganizationsDecisionDetail(ShapeBase):
    """
    Contains information about AWS Organizations's effect on a policy simulation.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "allowed_by_organizations",
                "AllowedByOrganizations",
                TypeInfo(bool),
            ),
        ]

    # Specifies whether the simulated operation is allowed by the AWS
    # Organizations service control policies that impact the simulated user's
    # account.
    allowed_by_organizations: bool = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class PasswordPolicy(ShapeBase):
    """
    Contains information about the account password policy.

    This data type is used as a response element in the GetAccountPasswordPolicy
    operation.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "minimum_password_length",
                "MinimumPasswordLength",
                TypeInfo(int),
            ),
            (
                "require_symbols",
                "RequireSymbols",
                TypeInfo(bool),
            ),
            (
                "require_numbers",
                "RequireNumbers",
                TypeInfo(bool),
            ),
            (
                "require_uppercase_characters",
                "RequireUppercaseCharacters",
                TypeInfo(bool),
            ),
            (
                "require_lowercase_characters",
                "RequireLowercaseCharacters",
                TypeInfo(bool),
            ),
            (
                "allow_users_to_change_password",
                "AllowUsersToChangePassword",
                TypeInfo(bool),
            ),
            (
                "expire_passwords",
                "ExpirePasswords",
                TypeInfo(bool),
            ),
            (
                "max_password_age",
                "MaxPasswordAge",
                TypeInfo(int),
            ),
            (
                "password_reuse_prevention",
                "PasswordReusePrevention",
                TypeInfo(int),
            ),
            (
                "hard_expiry",
                "HardExpiry",
                TypeInfo(bool),
            ),
        ]

    # Minimum length to require for IAM user passwords.
    minimum_password_length: int = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Specifies whether to require symbols for IAM user passwords.
    require_symbols: bool = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Specifies whether to require numbers for IAM user passwords.
    require_numbers: bool = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Specifies whether to require uppercase characters for IAM user passwords.
    require_uppercase_characters: bool = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Specifies whether to require lowercase characters for IAM user passwords.
    require_lowercase_characters: bool = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Specifies whether IAM users are allowed to change their own password.
    allow_users_to_change_password: bool = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Indicates whether passwords in the account expire. Returns true if
    # `MaxPasswordAge` contains a value greater than 0. Returns false if
    # MaxPasswordAge is 0 or not present.
    expire_passwords: bool = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The number of days that an IAM user password is valid.
    max_password_age: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Specifies the number of previous passwords that IAM users are prevented
    # from reusing.
    password_reuse_prevention: int = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Specifies whether IAM users are prevented from setting a new password after
    # their password has expired.
    hard_expiry: bool = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class PasswordPolicyViolationException(ShapeBase):
    """
    The request was rejected because the provided password did not meet the
    requirements imposed by the account password policy.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "message",
                "message",
                TypeInfo(str),
            ),
        ]

    message: str = dataclasses.field(default=ShapeBase.NOT_SET, )


class PermissionsBoundaryAttachmentType(str):
    PermissionsBoundaryPolicy = "PermissionsBoundaryPolicy"


@dataclasses.dataclass
class Policy(ShapeBase):
    """
    Contains information about a managed policy.

    This data type is used as a response element in the CreatePolicy, GetPolicy, and
    ListPolicies operations.

    For more information about managed policies, refer to [Managed Policies and
    Inline Policies](http://docs.aws.amazon.com/IAM/latest/UserGuide/policies-
    managed-vs-inline.html) in the _Using IAM_ guide.
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
                "policy_id",
                "PolicyId",
                TypeInfo(str),
            ),
            (
                "arn",
                "Arn",
                TypeInfo(str),
            ),
            (
                "path",
                "Path",
                TypeInfo(str),
            ),
            (
                "default_version_id",
                "DefaultVersionId",
                TypeInfo(str),
            ),
            (
                "attachment_count",
                "AttachmentCount",
                TypeInfo(int),
            ),
            (
                "permissions_boundary_usage_count",
                "PermissionsBoundaryUsageCount",
                TypeInfo(int),
            ),
            (
                "is_attachable",
                "IsAttachable",
                TypeInfo(bool),
            ),
            (
                "description",
                "Description",
                TypeInfo(str),
            ),
            (
                "create_date",
                "CreateDate",
                TypeInfo(datetime.datetime),
            ),
            (
                "update_date",
                "UpdateDate",
                TypeInfo(datetime.datetime),
            ),
        ]

    # The friendly name (not ARN) identifying the policy.
    policy_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The stable and unique string identifying the policy.

    # For more information about IDs, see [IAM
    # Identifiers](http://docs.aws.amazon.com/IAM/latest/UserGuide/Using_Identifiers.html)
    # in the _Using IAM_ guide.
    policy_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The Amazon Resource Name (ARN). ARNs are unique identifiers for AWS
    # resources.

    # For more information about ARNs, go to [Amazon Resource Names (ARNs) and
    # AWS Service Namespaces](http://docs.aws.amazon.com/general/latest/gr/aws-
    # arns-and-namespaces.html) in the _AWS General Reference_.
    arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The path to the policy.

    # For more information about paths, see [IAM
    # Identifiers](http://docs.aws.amazon.com/IAM/latest/UserGuide/Using_Identifiers.html)
    # in the _Using IAM_ guide.
    path: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The identifier for the version of the policy that is set as the default
    # version.
    default_version_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The number of entities (users, groups, and roles) that the policy is
    # attached to.
    attachment_count: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The number of entities (users and roles) for which the policy is used to
    # set the permissions boundary.

    # For more information about permissions boundaries, see [Permissions
    # Boundaries for IAM Identities
    # ](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_boundaries.html)
    # in the _IAM User Guide_.
    permissions_boundary_usage_count: int = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Specifies whether the policy can be attached to an IAM user, group, or
    # role.
    is_attachable: bool = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A friendly description of the policy.

    # This element is included in the response to the GetPolicy operation. It is
    # not included in the response to the ListPolicies operation.
    description: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The date and time, in [ISO 8601 date-time
    # format](http://www.iso.org/iso/iso8601), when the policy was created.
    create_date: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The date and time, in [ISO 8601 date-time
    # format](http://www.iso.org/iso/iso8601), when the policy was last updated.

    # When a policy has only one version, this field contains the date and time
    # when the policy was created. When a policy has more than one version, this
    # field contains the date and time when the most recent policy version was
    # created.
    update_date: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class PolicyDetail(ShapeBase):
    """
    Contains information about an IAM policy, including the policy document.

    This data type is used as a response element in the
    GetAccountAuthorizationDetails operation.
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
                "policy_document",
                "PolicyDocument",
                TypeInfo(str),
            ),
        ]

    # The name of the policy.
    policy_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The policy document.
    policy_document: str = dataclasses.field(default=ShapeBase.NOT_SET, )


class PolicyEvaluationDecisionType(str):
    allowed = "allowed"
    explicitDeny = "explicitDeny"
    implicitDeny = "implicitDeny"


@dataclasses.dataclass
class PolicyEvaluationException(ShapeBase):
    """
    The request failed because a provided policy could not be successfully
    evaluated. An additional detailed message indicates the source of the failure.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "message",
                "message",
                TypeInfo(str),
            ),
        ]

    message: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class PolicyGroup(ShapeBase):
    """
    Contains information about a group that a managed policy is attached to.

    This data type is used as a response element in the ListEntitiesForPolicy
    operation.

    For more information about managed policies, refer to [Managed Policies and
    Inline Policies](http://docs.aws.amazon.com/IAM/latest/UserGuide/policies-
    managed-vs-inline.html) in the _Using IAM_ guide.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "group_name",
                "GroupName",
                TypeInfo(str),
            ),
            (
                "group_id",
                "GroupId",
                TypeInfo(str),
            ),
        ]

    # The name (friendly name, not ARN) identifying the group.
    group_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The stable and unique string identifying the group. For more information
    # about IDs, see [IAM
    # Identifiers](http://docs.aws.amazon.com/IAM/latest/UserGuide/reference_identifiers.html)
    # in the _IAM User Guide_.
    group_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class PolicyNotAttachableException(ShapeBase):
    """
    The request failed because AWS service role policies can only be attached to the
    service-linked role for that service.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "message",
                "message",
                TypeInfo(str),
            ),
        ]

    message: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class PolicyRole(ShapeBase):
    """
    Contains information about a role that a managed policy is attached to.

    This data type is used as a response element in the ListEntitiesForPolicy
    operation.

    For more information about managed policies, refer to [Managed Policies and
    Inline Policies](http://docs.aws.amazon.com/IAM/latest/UserGuide/policies-
    managed-vs-inline.html) in the _Using IAM_ guide.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "role_name",
                "RoleName",
                TypeInfo(str),
            ),
            (
                "role_id",
                "RoleId",
                TypeInfo(str),
            ),
        ]

    # The name (friendly name, not ARN) identifying the role.
    role_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The stable and unique string identifying the role. For more information
    # about IDs, see [IAM
    # Identifiers](http://docs.aws.amazon.com/IAM/latest/UserGuide/reference_identifiers.html)
    # in the _IAM User Guide_.
    role_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )


class PolicySourceType(str):
    user = "user"
    group = "group"
    role = "role"
    aws_managed = "aws-managed"
    user_managed = "user-managed"
    resource = "resource"
    none = "none"


class PolicyUsageType(str):
    """
    The policy usage type that indicates whether the policy is used as a permissions
    policy or as the permissions boundary for an entity.

    For more information about permissions boundaries, see [Permissions Boundaries
    for IAM Identities
    ](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_boundaries.html)
    in the _IAM User Guide_.
    """
    PermissionsPolicy = "PermissionsPolicy"
    PermissionsBoundary = "PermissionsBoundary"


@dataclasses.dataclass
class PolicyUser(ShapeBase):
    """
    Contains information about a user that a managed policy is attached to.

    This data type is used as a response element in the ListEntitiesForPolicy
    operation.

    For more information about managed policies, refer to [Managed Policies and
    Inline Policies](http://docs.aws.amazon.com/IAM/latest/UserGuide/policies-
    managed-vs-inline.html) in the _Using IAM_ guide.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "user_name",
                "UserName",
                TypeInfo(str),
            ),
            (
                "user_id",
                "UserId",
                TypeInfo(str),
            ),
        ]

    # The name (friendly name, not ARN) identifying the user.
    user_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The stable and unique string identifying the user. For more information
    # about IDs, see [IAM
    # Identifiers](http://docs.aws.amazon.com/IAM/latest/UserGuide/reference_identifiers.html)
    # in the _IAM User Guide_.
    user_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class PolicyVersion(ShapeBase):
    """
    Contains information about a version of a managed policy.

    This data type is used as a response element in the CreatePolicyVersion,
    GetPolicyVersion, ListPolicyVersions, and GetAccountAuthorizationDetails
    operations.

    For more information about managed policies, refer to [Managed Policies and
    Inline Policies](http://docs.aws.amazon.com/IAM/latest/UserGuide/policies-
    managed-vs-inline.html) in the _Using IAM_ guide.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "document",
                "Document",
                TypeInfo(str),
            ),
            (
                "version_id",
                "VersionId",
                TypeInfo(str),
            ),
            (
                "is_default_version",
                "IsDefaultVersion",
                TypeInfo(bool),
            ),
            (
                "create_date",
                "CreateDate",
                TypeInfo(datetime.datetime),
            ),
        ]

    # The policy document.

    # The policy document is returned in the response to the GetPolicyVersion and
    # GetAccountAuthorizationDetails operations. It is not returned in the
    # response to the CreatePolicyVersion or ListPolicyVersions operations.

    # The policy document returned in this structure is URL-encoded compliant
    # with [RFC 3986](https://tools.ietf.org/html/rfc3986). You can use a URL
    # decoding method to convert the policy back to plain JSON text. For example,
    # if you use Java, you can use the `decode` method of the
    # `java.net.URLDecoder` utility class in the Java SDK. Other languages and
    # SDKs provide similar functionality.
    document: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The identifier for the policy version.

    # Policy version identifiers always begin with `v` (always lowercase). When a
    # policy is created, the first policy version is `v1`.
    version_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Specifies whether the policy version is set as the policy's default
    # version.
    is_default_version: bool = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The date and time, in [ISO 8601 date-time
    # format](http://www.iso.org/iso/iso8601), when the policy version was
    # created.
    create_date: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class Position(ShapeBase):
    """
    Contains the row and column of a location of a `Statement` element in a policy
    document.

    This data type is used as a member of the ` Statement ` type.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "line",
                "Line",
                TypeInfo(int),
            ),
            (
                "column",
                "Column",
                TypeInfo(int),
            ),
        ]

    # The line containing the specified position in the document.
    line: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The column in the line containing the specified position in the document.
    column: int = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class PutGroupPolicyRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "group_name",
                "GroupName",
                TypeInfo(str),
            ),
            (
                "policy_name",
                "PolicyName",
                TypeInfo(str),
            ),
            (
                "policy_document",
                "PolicyDocument",
                TypeInfo(str),
            ),
        ]

    # The name of the group to associate the policy with.

    # This parameter allows (per its [regex
    # pattern](http://wikipedia.org/wiki/regex)) a string of characters
    # consisting of upper and lowercase alphanumeric characters with no spaces.
    # You can also include any of the following characters: _+=,.@-
    group_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The name of the policy document.

    # This parameter allows (per its [regex
    # pattern](http://wikipedia.org/wiki/regex)) a string of characters
    # consisting of upper and lowercase alphanumeric characters with no spaces.
    # You can also include any of the following characters: _+=,.@-
    policy_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The policy document.

    # The [regex pattern](http://wikipedia.org/wiki/regex) used to validate this
    # parameter is a string of characters consisting of the following:

    #   * Any printable ASCII character ranging from the space character (\u0020) through the end of the ASCII character range

    #   * The printable characters in the Basic Latin and Latin-1 Supplement character set (through \u00FF)

    #   * The special characters tab (\u0009), line feed (\u000A), and carriage return (\u000D)
    policy_document: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class PutRolePermissionsBoundaryRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "role_name",
                "RoleName",
                TypeInfo(str),
            ),
            (
                "permissions_boundary",
                "PermissionsBoundary",
                TypeInfo(str),
            ),
        ]

    # The name (friendly name, not ARN) of the IAM role for which you want to set
    # the permissions boundary.
    role_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The ARN of the policy that is used to set the permissions boundary for the
    # role.
    permissions_boundary: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class PutRolePolicyRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "role_name",
                "RoleName",
                TypeInfo(str),
            ),
            (
                "policy_name",
                "PolicyName",
                TypeInfo(str),
            ),
            (
                "policy_document",
                "PolicyDocument",
                TypeInfo(str),
            ),
        ]

    # The name of the role to associate the policy with.

    # This parameter allows (per its [regex
    # pattern](http://wikipedia.org/wiki/regex)) a string of characters
    # consisting of upper and lowercase alphanumeric characters with no spaces.
    # You can also include any of the following characters: _+=,.@-
    role_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The name of the policy document.

    # This parameter allows (per its [regex
    # pattern](http://wikipedia.org/wiki/regex)) a string of characters
    # consisting of upper and lowercase alphanumeric characters with no spaces.
    # You can also include any of the following characters: _+=,.@-
    policy_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The policy document.

    # The [regex pattern](http://wikipedia.org/wiki/regex) used to validate this
    # parameter is a string of characters consisting of the following:

    #   * Any printable ASCII character ranging from the space character (\u0020) through the end of the ASCII character range

    #   * The printable characters in the Basic Latin and Latin-1 Supplement character set (through \u00FF)

    #   * The special characters tab (\u0009), line feed (\u000A), and carriage return (\u000D)
    policy_document: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class PutUserPermissionsBoundaryRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "user_name",
                "UserName",
                TypeInfo(str),
            ),
            (
                "permissions_boundary",
                "PermissionsBoundary",
                TypeInfo(str),
            ),
        ]

    # The name (friendly name, not ARN) of the IAM user for which you want to set
    # the permissions boundary.
    user_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The ARN of the policy that is used to set the permissions boundary for the
    # user.
    permissions_boundary: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class PutUserPolicyRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "user_name",
                "UserName",
                TypeInfo(str),
            ),
            (
                "policy_name",
                "PolicyName",
                TypeInfo(str),
            ),
            (
                "policy_document",
                "PolicyDocument",
                TypeInfo(str),
            ),
        ]

    # The name of the user to associate the policy with.

    # This parameter allows (per its [regex
    # pattern](http://wikipedia.org/wiki/regex)) a string of characters
    # consisting of upper and lowercase alphanumeric characters with no spaces.
    # You can also include any of the following characters: _+=,.@-
    user_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The name of the policy document.

    # This parameter allows (per its [regex
    # pattern](http://wikipedia.org/wiki/regex)) a string of characters
    # consisting of upper and lowercase alphanumeric characters with no spaces.
    # You can also include any of the following characters: _+=,.@-
    policy_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The policy document.

    # The [regex pattern](http://wikipedia.org/wiki/regex) used to validate this
    # parameter is a string of characters consisting of the following:

    #   * Any printable ASCII character ranging from the space character (\u0020) through the end of the ASCII character range

    #   * The printable characters in the Basic Latin and Latin-1 Supplement character set (through \u00FF)

    #   * The special characters tab (\u0009), line feed (\u000A), and carriage return (\u000D)
    policy_document: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class RemoveClientIDFromOpenIDConnectProviderRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "open_id_connect_provider_arn",
                "OpenIDConnectProviderArn",
                TypeInfo(str),
            ),
            (
                "client_id",
                "ClientID",
                TypeInfo(str),
            ),
        ]

    # The Amazon Resource Name (ARN) of the IAM OIDC provider resource to remove
    # the client ID from. You can get a list of OIDC provider ARNs by using the
    # ListOpenIDConnectProviders operation.

    # For more information about ARNs, see [Amazon Resource Names (ARNs) and AWS
    # Service Namespaces](http://docs.aws.amazon.com/general/latest/gr/aws-arns-
    # and-namespaces.html) in the _AWS General Reference_.
    open_id_connect_provider_arn: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The client ID (also known as audience) to remove from the IAM OIDC provider
    # resource. For more information about client IDs, see
    # CreateOpenIDConnectProvider.
    client_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class RemoveRoleFromInstanceProfileRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "instance_profile_name",
                "InstanceProfileName",
                TypeInfo(str),
            ),
            (
                "role_name",
                "RoleName",
                TypeInfo(str),
            ),
        ]

    # The name of the instance profile to update.

    # This parameter allows (per its [regex
    # pattern](http://wikipedia.org/wiki/regex)) a string of characters
    # consisting of upper and lowercase alphanumeric characters with no spaces.
    # You can also include any of the following characters: _+=,.@-
    instance_profile_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The name of the role to remove.

    # This parameter allows (per its [regex
    # pattern](http://wikipedia.org/wiki/regex)) a string of characters
    # consisting of upper and lowercase alphanumeric characters with no spaces.
    # You can also include any of the following characters: _+=,.@-
    role_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class RemoveUserFromGroupRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "group_name",
                "GroupName",
                TypeInfo(str),
            ),
            (
                "user_name",
                "UserName",
                TypeInfo(str),
            ),
        ]

    # The name of the group to update.

    # This parameter allows (per its [regex
    # pattern](http://wikipedia.org/wiki/regex)) a string of characters
    # consisting of upper and lowercase alphanumeric characters with no spaces.
    # You can also include any of the following characters: _+=,.@-
    group_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The name of the user to remove.

    # This parameter allows (per its [regex
    # pattern](http://wikipedia.org/wiki/regex)) a string of characters
    # consisting of upper and lowercase alphanumeric characters with no spaces.
    # You can also include any of the following characters: _+=,.@-
    user_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )


class ReportContentType(botocore.response.StreamingBody):
    pass


class ReportFormatType(str):
    text_csv = "text/csv"


class ReportStateType(str):
    STARTED = "STARTED"
    INPROGRESS = "INPROGRESS"
    COMPLETE = "COMPLETE"


@dataclasses.dataclass
class ResetServiceSpecificCredentialRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "service_specific_credential_id",
                "ServiceSpecificCredentialId",
                TypeInfo(str),
            ),
            (
                "user_name",
                "UserName",
                TypeInfo(str),
            ),
        ]

    # The unique identifier of the service-specific credential.

    # This parameter allows (per its [regex
    # pattern](http://wikipedia.org/wiki/regex)) a string of characters that can
    # consist of any upper or lowercased letter or digit.
    service_specific_credential_id: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The name of the IAM user associated with the service-specific credential.
    # If this value is not specified, then the operation assumes the user whose
    # credentials are used to call the operation.

    # This parameter allows (per its [regex
    # pattern](http://wikipedia.org/wiki/regex)) a string of characters
    # consisting of upper and lowercase alphanumeric characters with no spaces.
    # You can also include any of the following characters: _+=,.@-
    user_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ResetServiceSpecificCredentialResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "service_specific_credential",
                "ServiceSpecificCredential",
                TypeInfo(ServiceSpecificCredential),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A structure with details about the updated service-specific credential,
    # including the new password.

    # This is the **only** time that you can access the password. You cannot
    # recover the password later, but you can reset it again.
    service_specific_credential: "ServiceSpecificCredential" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class ResourceSpecificResult(ShapeBase):
    """
    Contains the result of the simulation of a single API operation call on a single
    resource.

    This data type is used by a member of the EvaluationResult data type.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "eval_resource_name",
                "EvalResourceName",
                TypeInfo(str),
            ),
            (
                "eval_resource_decision",
                "EvalResourceDecision",
                TypeInfo(typing.Union[str, PolicyEvaluationDecisionType]),
            ),
            (
                "matched_statements",
                "MatchedStatements",
                TypeInfo(typing.List[Statement]),
            ),
            (
                "missing_context_values",
                "MissingContextValues",
                TypeInfo(typing.List[str]),
            ),
            (
                "eval_decision_details",
                "EvalDecisionDetails",
                TypeInfo(
                    typing.Dict[str, typing.
                                Union[str, PolicyEvaluationDecisionType]]
                ),
            ),
        ]

    # The name of the simulated resource, in Amazon Resource Name (ARN) format.
    eval_resource_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The result of the simulation of the simulated API operation on the resource
    # specified in `EvalResourceName`.
    eval_resource_decision: typing.Union[str, "PolicyEvaluationDecisionType"
                                        ] = dataclasses.field(
                                            default=ShapeBase.NOT_SET,
                                        )

    # A list of the statements in the input policies that determine the result
    # for this part of the simulation. Remember that even if multiple statements
    # allow the operation on the resource, if _any_ statement denies that
    # operation, then the explicit deny overrides any allow, and the deny
    # statement is the only entry included in the result.
    matched_statements: typing.List["Statement"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A list of context keys that are required by the included input policies but
    # that were not provided by one of the input parameters. This list is used
    # when a list of ARNs is included in the `ResourceArns` parameter instead of
    # "*". If you do not specify individual resources, by setting `ResourceArns`
    # to "*" or by not including the `ResourceArns` parameter, then any missing
    # context values are instead included under the `EvaluationResults` section.
    # To discover the context keys used by a set of policies, you can call
    # GetContextKeysForCustomPolicy or GetContextKeysForPrincipalPolicy.
    missing_context_values: typing.List[str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Additional details about the results of the evaluation decision. When there
    # are both IAM policies and resource policies, this parameter explains how
    # each set of policies contributes to the final evaluation decision. When
    # simulating cross-account access to a resource, both the resource-based
    # policy and the caller's IAM policy must grant access.
    eval_decision_details: typing.Dict[
        str, typing.
        Union[str, "PolicyEvaluationDecisionType"]] = dataclasses.field(
            default=ShapeBase.NOT_SET,
        )


@dataclasses.dataclass
class ResyncMFADeviceRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "user_name",
                "UserName",
                TypeInfo(str),
            ),
            (
                "serial_number",
                "SerialNumber",
                TypeInfo(str),
            ),
            (
                "authentication_code1",
                "AuthenticationCode1",
                TypeInfo(str),
            ),
            (
                "authentication_code2",
                "AuthenticationCode2",
                TypeInfo(str),
            ),
        ]

    # The name of the user whose MFA device you want to resynchronize.

    # This parameter allows (per its [regex
    # pattern](http://wikipedia.org/wiki/regex)) a string of characters
    # consisting of upper and lowercase alphanumeric characters with no spaces.
    # You can also include any of the following characters: _+=,.@-
    user_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Serial number that uniquely identifies the MFA device.

    # This parameter allows (per its [regex
    # pattern](http://wikipedia.org/wiki/regex)) a string of characters
    # consisting of upper and lowercase alphanumeric characters with no spaces.
    # You can also include any of the following characters: _+=,.@-
    serial_number: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # An authentication code emitted by the device.

    # The format for this parameter is a sequence of six digits.
    authentication_code1: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A subsequent authentication code emitted by the device.

    # The format for this parameter is a sequence of six digits.
    authentication_code2: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class Role(ShapeBase):
    """
    Contains information about an IAM role. This structure is returned as a response
    element in several API operations that interact with roles.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "path",
                "Path",
                TypeInfo(str),
            ),
            (
                "role_name",
                "RoleName",
                TypeInfo(str),
            ),
            (
                "role_id",
                "RoleId",
                TypeInfo(str),
            ),
            (
                "arn",
                "Arn",
                TypeInfo(str),
            ),
            (
                "create_date",
                "CreateDate",
                TypeInfo(datetime.datetime),
            ),
            (
                "assume_role_policy_document",
                "AssumeRolePolicyDocument",
                TypeInfo(str),
            ),
            (
                "description",
                "Description",
                TypeInfo(str),
            ),
            (
                "max_session_duration",
                "MaxSessionDuration",
                TypeInfo(int),
            ),
            (
                "permissions_boundary",
                "PermissionsBoundary",
                TypeInfo(AttachedPermissionsBoundary),
            ),
        ]

    # The path to the role. For more information about paths, see [IAM
    # Identifiers](http://docs.aws.amazon.com/IAM/latest/UserGuide/Using_Identifiers.html)
    # in the _Using IAM_ guide.
    path: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The friendly name that identifies the role.
    role_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The stable and unique string identifying the role. For more information
    # about IDs, see [IAM
    # Identifiers](http://docs.aws.amazon.com/IAM/latest/UserGuide/Using_Identifiers.html)
    # in the _Using IAM_ guide.
    role_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The Amazon Resource Name (ARN) specifying the role. For more information
    # about ARNs and how to use them in policies, see [IAM
    # Identifiers](http://docs.aws.amazon.com/IAM/latest/UserGuide/Using_Identifiers.html)
    # in the _IAM User Guide_ guide.
    arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The date and time, in [ISO 8601 date-time
    # format](http://www.iso.org/iso/iso8601), when the role was created.
    create_date: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The policy that grants an entity permission to assume the role.
    assume_role_policy_document: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A description of the role that you provide.
    description: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The maximum session duration (in seconds) for the specified role. Anyone
    # who uses the AWS CLI or API to assume the role can specify the duration
    # using the optional `DurationSeconds` API parameter or `duration-seconds`
    # CLI parameter.
    max_session_duration: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The ARN of the policy used to set the permissions boundary for the role.

    # For more information about permissions boundaries, see [Permissions
    # Boundaries for IAM Identities
    # ](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_boundaries.html)
    # in the _IAM User Guide_.
    permissions_boundary: "AttachedPermissionsBoundary" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class RoleDetail(ShapeBase):
    """
    Contains information about an IAM role, including all of the role's policies.

    This data type is used as a response element in the
    GetAccountAuthorizationDetails operation.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "path",
                "Path",
                TypeInfo(str),
            ),
            (
                "role_name",
                "RoleName",
                TypeInfo(str),
            ),
            (
                "role_id",
                "RoleId",
                TypeInfo(str),
            ),
            (
                "arn",
                "Arn",
                TypeInfo(str),
            ),
            (
                "create_date",
                "CreateDate",
                TypeInfo(datetime.datetime),
            ),
            (
                "assume_role_policy_document",
                "AssumeRolePolicyDocument",
                TypeInfo(str),
            ),
            (
                "instance_profile_list",
                "InstanceProfileList",
                TypeInfo(typing.List[InstanceProfile]),
            ),
            (
                "role_policy_list",
                "RolePolicyList",
                TypeInfo(typing.List[PolicyDetail]),
            ),
            (
                "attached_managed_policies",
                "AttachedManagedPolicies",
                TypeInfo(typing.List[AttachedPolicy]),
            ),
            (
                "permissions_boundary",
                "PermissionsBoundary",
                TypeInfo(AttachedPermissionsBoundary),
            ),
        ]

    # The path to the role. For more information about paths, see [IAM
    # Identifiers](http://docs.aws.amazon.com/IAM/latest/UserGuide/Using_Identifiers.html)
    # in the _Using IAM_ guide.
    path: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The friendly name that identifies the role.
    role_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The stable and unique string identifying the role. For more information
    # about IDs, see [IAM
    # Identifiers](http://docs.aws.amazon.com/IAM/latest/UserGuide/Using_Identifiers.html)
    # in the _Using IAM_ guide.
    role_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The Amazon Resource Name (ARN). ARNs are unique identifiers for AWS
    # resources.

    # For more information about ARNs, go to [Amazon Resource Names (ARNs) and
    # AWS Service Namespaces](http://docs.aws.amazon.com/general/latest/gr/aws-
    # arns-and-namespaces.html) in the _AWS General Reference_.
    arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The date and time, in [ISO 8601 date-time
    # format](http://www.iso.org/iso/iso8601), when the role was created.
    create_date: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The trust policy that grants permission to assume the role.
    assume_role_policy_document: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A list of instance profiles that contain this role.
    instance_profile_list: typing.List["InstanceProfile"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A list of inline policies embedded in the role. These policies are the
    # role's access (permissions) policies.
    role_policy_list: typing.List["PolicyDetail"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A list of managed policies attached to the role. These policies are the
    # role's access (permissions) policies.
    attached_managed_policies: typing.List["AttachedPolicy"
                                          ] = dataclasses.field(
                                              default=ShapeBase.NOT_SET,
                                          )

    # The ARN of the policy used to set the permissions boundary for the role.

    # For more information about permissions boundaries, see [Permissions
    # Boundaries for IAM Identities
    # ](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_boundaries.html)
    # in the _IAM User Guide_.
    permissions_boundary: "AttachedPermissionsBoundary" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class RoleUsageType(ShapeBase):
    """
    An object that contains details about how a service-linked role is used, if that
    information is returned by the service.

    This data type is used as a response element in the
    GetServiceLinkedRoleDeletionStatus operation.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "region",
                "Region",
                TypeInfo(str),
            ),
            (
                "resources",
                "Resources",
                TypeInfo(typing.List[str]),
            ),
        ]

    # The name of the region where the service-linked role is being used.
    region: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The name of the resource that is using the service-linked role.
    resources: typing.List[str] = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class SAMLProviderListEntry(ShapeBase):
    """
    Contains the list of SAML providers for this account.
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
                "valid_until",
                "ValidUntil",
                TypeInfo(datetime.datetime),
            ),
            (
                "create_date",
                "CreateDate",
                TypeInfo(datetime.datetime),
            ),
        ]

    # The Amazon Resource Name (ARN) of the SAML provider.
    arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The expiration date and time for the SAML provider.
    valid_until: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The date and time when the SAML provider was created.
    create_date: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class SSHPublicKey(ShapeBase):
    """
    Contains information about an SSH public key.

    This data type is used as a response element in the GetSSHPublicKey and
    UploadSSHPublicKey operations.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "user_name",
                "UserName",
                TypeInfo(str),
            ),
            (
                "ssh_public_key_id",
                "SSHPublicKeyId",
                TypeInfo(str),
            ),
            (
                "fingerprint",
                "Fingerprint",
                TypeInfo(str),
            ),
            (
                "ssh_public_key_body",
                "SSHPublicKeyBody",
                TypeInfo(str),
            ),
            (
                "status",
                "Status",
                TypeInfo(typing.Union[str, statusType]),
            ),
            (
                "upload_date",
                "UploadDate",
                TypeInfo(datetime.datetime),
            ),
        ]

    # The name of the IAM user associated with the SSH public key.
    user_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The unique identifier for the SSH public key.
    ssh_public_key_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The MD5 message digest of the SSH public key.
    fingerprint: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The SSH public key.
    ssh_public_key_body: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The status of the SSH public key. `Active` means that the key can be used
    # for authentication with an AWS CodeCommit repository. `Inactive` means that
    # the key cannot be used.
    status: typing.Union[str, "statusType"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The date and time, in [ISO 8601 date-time
    # format](http://www.iso.org/iso/iso8601), when the SSH public key was
    # uploaded.
    upload_date: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class SSHPublicKeyMetadata(ShapeBase):
    """
    Contains information about an SSH public key, without the key's body or
    fingerprint.

    This data type is used as a response element in the ListSSHPublicKeys operation.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "user_name",
                "UserName",
                TypeInfo(str),
            ),
            (
                "ssh_public_key_id",
                "SSHPublicKeyId",
                TypeInfo(str),
            ),
            (
                "status",
                "Status",
                TypeInfo(typing.Union[str, statusType]),
            ),
            (
                "upload_date",
                "UploadDate",
                TypeInfo(datetime.datetime),
            ),
        ]

    # The name of the IAM user associated with the SSH public key.
    user_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The unique identifier for the SSH public key.
    ssh_public_key_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The status of the SSH public key. `Active` means that the key can be used
    # for authentication with an AWS CodeCommit repository. `Inactive` means that
    # the key cannot be used.
    status: typing.Union[str, "statusType"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The date and time, in [ISO 8601 date-time
    # format](http://www.iso.org/iso/iso8601), when the SSH public key was
    # uploaded.
    upload_date: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class ServerCertificate(ShapeBase):
    """
    Contains information about a server certificate.

    This data type is used as a response element in the GetServerCertificate
    operation.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "server_certificate_metadata",
                "ServerCertificateMetadata",
                TypeInfo(ServerCertificateMetadata),
            ),
            (
                "certificate_body",
                "CertificateBody",
                TypeInfo(str),
            ),
            (
                "certificate_chain",
                "CertificateChain",
                TypeInfo(str),
            ),
        ]

    # The meta information of the server certificate, such as its name, path, ID,
    # and ARN.
    server_certificate_metadata: "ServerCertificateMetadata" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The contents of the public key certificate.
    certificate_body: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The contents of the public key certificate chain.
    certificate_chain: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ServerCertificateMetadata(ShapeBase):
    """
    Contains information about a server certificate without its certificate body,
    certificate chain, and private key.

    This data type is used as a response element in the UploadServerCertificate and
    ListServerCertificates operations.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "path",
                "Path",
                TypeInfo(str),
            ),
            (
                "server_certificate_name",
                "ServerCertificateName",
                TypeInfo(str),
            ),
            (
                "server_certificate_id",
                "ServerCertificateId",
                TypeInfo(str),
            ),
            (
                "arn",
                "Arn",
                TypeInfo(str),
            ),
            (
                "upload_date",
                "UploadDate",
                TypeInfo(datetime.datetime),
            ),
            (
                "expiration",
                "Expiration",
                TypeInfo(datetime.datetime),
            ),
        ]

    # The path to the server certificate. For more information about paths, see
    # [IAM
    # Identifiers](http://docs.aws.amazon.com/IAM/latest/UserGuide/Using_Identifiers.html)
    # in the _Using IAM_ guide.
    path: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The name that identifies the server certificate.
    server_certificate_name: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The stable and unique string identifying the server certificate. For more
    # information about IDs, see [IAM
    # Identifiers](http://docs.aws.amazon.com/IAM/latest/UserGuide/Using_Identifiers.html)
    # in the _Using IAM_ guide.
    server_certificate_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The Amazon Resource Name (ARN) specifying the server certificate. For more
    # information about ARNs and how to use them in policies, see [IAM
    # Identifiers](http://docs.aws.amazon.com/IAM/latest/UserGuide/Using_Identifiers.html)
    # in the _Using IAM_ guide.
    arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The date when the server certificate was uploaded.
    upload_date: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The date on which the certificate is set to expire.
    expiration: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class ServiceFailureException(ShapeBase):
    """
    The request processing has failed because of an unknown error, exception or
    failure.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "message",
                "message",
                TypeInfo(str),
            ),
        ]

    message: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ServiceNotSupportedException(ShapeBase):
    """
    The specified service does not support service-specific credentials.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "message",
                "message",
                TypeInfo(str),
            ),
        ]

    message: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ServiceSpecificCredential(ShapeBase):
    """
    Contains the details of a service-specific credential.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "create_date",
                "CreateDate",
                TypeInfo(datetime.datetime),
            ),
            (
                "service_name",
                "ServiceName",
                TypeInfo(str),
            ),
            (
                "service_user_name",
                "ServiceUserName",
                TypeInfo(str),
            ),
            (
                "service_password",
                "ServicePassword",
                TypeInfo(str),
            ),
            (
                "service_specific_credential_id",
                "ServiceSpecificCredentialId",
                TypeInfo(str),
            ),
            (
                "user_name",
                "UserName",
                TypeInfo(str),
            ),
            (
                "status",
                "Status",
                TypeInfo(typing.Union[str, statusType]),
            ),
        ]

    # The date and time, in [ISO 8601 date-time
    # format](http://www.iso.org/iso/iso8601), when the service-specific
    # credential were created.
    create_date: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The name of the service associated with the service-specific credential.
    service_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The generated user name for the service-specific credential. This value is
    # generated by combining the IAM user's name combined with the ID number of
    # the AWS account, as in `jane-at-123456789012`, for example. This value
    # cannot be configured by the user.
    service_user_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The generated password for the service-specific credential.
    service_password: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The unique identifier for the service-specific credential.
    service_specific_credential_id: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The name of the IAM user associated with the service-specific credential.
    user_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The status of the service-specific credential. `Active` means that the key
    # is valid for API calls, while `Inactive` means it is not.
    status: typing.Union[str, "statusType"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class ServiceSpecificCredentialMetadata(ShapeBase):
    """
    Contains additional details about a service-specific credential.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "user_name",
                "UserName",
                TypeInfo(str),
            ),
            (
                "status",
                "Status",
                TypeInfo(typing.Union[str, statusType]),
            ),
            (
                "service_user_name",
                "ServiceUserName",
                TypeInfo(str),
            ),
            (
                "create_date",
                "CreateDate",
                TypeInfo(datetime.datetime),
            ),
            (
                "service_specific_credential_id",
                "ServiceSpecificCredentialId",
                TypeInfo(str),
            ),
            (
                "service_name",
                "ServiceName",
                TypeInfo(str),
            ),
        ]

    # The name of the IAM user associated with the service-specific credential.
    user_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The status of the service-specific credential. `Active` means that the key
    # is valid for API calls, while `Inactive` means it is not.
    status: typing.Union[str, "statusType"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The generated user name for the service-specific credential.
    service_user_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The date and time, in [ISO 8601 date-time
    # format](http://www.iso.org/iso/iso8601), when the service-specific
    # credential were created.
    create_date: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The unique identifier for the service-specific credential.
    service_specific_credential_id: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The name of the service associated with the service-specific credential.
    service_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class SetDefaultPolicyVersionRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "policy_arn",
                "PolicyArn",
                TypeInfo(str),
            ),
            (
                "version_id",
                "VersionId",
                TypeInfo(str),
            ),
        ]

    # The Amazon Resource Name (ARN) of the IAM policy whose default version you
    # want to set.

    # For more information about ARNs, see [Amazon Resource Names (ARNs) and AWS
    # Service Namespaces](http://docs.aws.amazon.com/general/latest/gr/aws-arns-
    # and-namespaces.html) in the _AWS General Reference_.
    policy_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The version of the policy to set as the default (operative) version.

    # For more information about managed policy versions, see [Versioning for
    # Managed Policies](http://docs.aws.amazon.com/IAM/latest/UserGuide/policies-
    # managed-versions.html) in the _IAM User Guide_.
    version_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class SigningCertificate(ShapeBase):
    """
    Contains information about an X.509 signing certificate.

    This data type is used as a response element in the UploadSigningCertificate and
    ListSigningCertificates operations.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "user_name",
                "UserName",
                TypeInfo(str),
            ),
            (
                "certificate_id",
                "CertificateId",
                TypeInfo(str),
            ),
            (
                "certificate_body",
                "CertificateBody",
                TypeInfo(str),
            ),
            (
                "status",
                "Status",
                TypeInfo(typing.Union[str, statusType]),
            ),
            (
                "upload_date",
                "UploadDate",
                TypeInfo(datetime.datetime),
            ),
        ]

    # The name of the user the signing certificate is associated with.
    user_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The ID for the signing certificate.
    certificate_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The contents of the signing certificate.
    certificate_body: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The status of the signing certificate. `Active` means that the key is valid
    # for API calls, while `Inactive` means it is not.
    status: typing.Union[str, "statusType"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The date when the signing certificate was uploaded.
    upload_date: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class SimulateCustomPolicyRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "policy_input_list",
                "PolicyInputList",
                TypeInfo(typing.List[str]),
            ),
            (
                "action_names",
                "ActionNames",
                TypeInfo(typing.List[str]),
            ),
            (
                "resource_arns",
                "ResourceArns",
                TypeInfo(typing.List[str]),
            ),
            (
                "resource_policy",
                "ResourcePolicy",
                TypeInfo(str),
            ),
            (
                "resource_owner",
                "ResourceOwner",
                TypeInfo(str),
            ),
            (
                "caller_arn",
                "CallerArn",
                TypeInfo(str),
            ),
            (
                "context_entries",
                "ContextEntries",
                TypeInfo(typing.List[ContextEntry]),
            ),
            (
                "resource_handling_option",
                "ResourceHandlingOption",
                TypeInfo(str),
            ),
            (
                "max_items",
                "MaxItems",
                TypeInfo(int),
            ),
            (
                "marker",
                "Marker",
                TypeInfo(str),
            ),
        ]

    # A list of policy documents to include in the simulation. Each document is
    # specified as a string containing the complete, valid JSON text of an IAM
    # policy. Do not include any resource-based policies in this parameter. Any
    # resource-based policy must be submitted with the `ResourcePolicy`
    # parameter. The policies cannot be "scope-down" policies, such as you could
    # include in a call to
    # [GetFederationToken](http://docs.aws.amazon.com/IAM/latest/APIReference/API_GetFederationToken.html)
    # or one of the
    # [AssumeRole](http://docs.aws.amazon.com/IAM/latest/APIReference/API_AssumeRole.html)
    # API operations. In other words, do not use policies designed to restrict
    # what a user can do while using the temporary credentials.

    # The [regex pattern](http://wikipedia.org/wiki/regex) used to validate this
    # parameter is a string of characters consisting of the following:

    #   * Any printable ASCII character ranging from the space character (\u0020) through the end of the ASCII character range

    #   * The printable characters in the Basic Latin and Latin-1 Supplement character set (through \u00FF)

    #   * The special characters tab (\u0009), line feed (\u000A), and carriage return (\u000D)
    policy_input_list: typing.List[str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A list of names of API operations to evaluate in the simulation. Each
    # operation is evaluated against each resource. Each operation must include
    # the service identifier, such as `iam:CreateUser`.
    action_names: typing.List[str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A list of ARNs of AWS resources to include in the simulation. If this
    # parameter is not provided then the value defaults to `*` (all resources).
    # Each API in the `ActionNames` parameter is evaluated for each resource in
    # this list. The simulation determines the access result (allowed or denied)
    # of each combination and reports it in the response.

    # The simulation does not automatically retrieve policies for the specified
    # resources. If you want to include a resource policy in the simulation, then
    # you must include the policy as a string in the `ResourcePolicy` parameter.

    # If you include a `ResourcePolicy`, then it must be applicable to all of the
    # resources included in the simulation or you receive an invalid input error.

    # For more information about ARNs, see [Amazon Resource Names (ARNs) and AWS
    # Service Namespaces](http://docs.aws.amazon.com/general/latest/gr/aws-arns-
    # and-namespaces.html) in the _AWS General Reference_.
    resource_arns: typing.List[str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A resource-based policy to include in the simulation provided as a string.
    # Each resource in the simulation is treated as if it had this policy
    # attached. You can include only one resource-based policy in a simulation.

    # The [regex pattern](http://wikipedia.org/wiki/regex) used to validate this
    # parameter is a string of characters consisting of the following:

    #   * Any printable ASCII character ranging from the space character (\u0020) through the end of the ASCII character range

    #   * The printable characters in the Basic Latin and Latin-1 Supplement character set (through \u00FF)

    #   * The special characters tab (\u0009), line feed (\u000A), and carriage return (\u000D)
    resource_policy: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # An ARN representing the AWS account ID that specifies the owner of any
    # simulated resource that does not identify its owner in the resource ARN,
    # such as an S3 bucket or object. If `ResourceOwner` is specified, it is also
    # used as the account owner of any `ResourcePolicy` included in the
    # simulation. If the `ResourceOwner` parameter is not specified, then the
    # owner of the resources and the resource policy defaults to the account of
    # the identity provided in `CallerArn`. This parameter is required only if
    # you specify a resource-based policy and account that owns the resource is
    # different from the account that owns the simulated calling user
    # `CallerArn`.

    # The ARN for an account uses the following syntax: `arn:aws:iam:: _AWS-
    # account-ID_ :root`. For example, to represent the account with the
    # 112233445566 ID, use the following ARN:
    # `arn:aws:iam::112233445566-ID:root`.
    resource_owner: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The ARN of the IAM user that you want to use as the simulated caller of the
    # API operations. `CallerArn` is required if you include a `ResourcePolicy`
    # so that the policy's `Principal` element has a value to use in evaluating
    # the policy.

    # You can specify only the ARN of an IAM user. You cannot specify the ARN of
    # an assumed role, federated user, or a service principal.
    caller_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A list of context keys and corresponding values for the simulation to use.
    # Whenever a context key is evaluated in one of the simulated IAM permission
    # policies, the corresponding value is supplied.
    context_entries: typing.List["ContextEntry"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Specifies the type of simulation to run. Different API operations that
    # support resource-based policies require different combinations of
    # resources. By specifying the type of simulation to run, you enable the
    # policy simulator to enforce the presence of the required resources to
    # ensure reliable simulation results. If your simulation does not match one
    # of the following scenarios, then you can omit this parameter. The following
    # list shows each of the supported scenario values and the resources that you
    # must define to run the simulation.

    # Each of the EC2 scenarios requires that you specify instance, image, and
    # security-group resources. If your scenario includes an EBS volume, then you
    # must specify that volume as a resource. If the EC2 scenario includes VPC,
    # then you must supply the network-interface resource. If it includes an IP
    # subnet, then you must specify the subnet resource. For more information on
    # the EC2 scenario options, see [Supported
    # Platforms](http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-supported-
    # platforms.html) in the _Amazon EC2 User Guide_.

    #   * **EC2-Classic-InstanceStore**

    # instance, image, security-group

    #   * **EC2-Classic-EBS**

    # instance, image, security-group, volume

    #   * **EC2-VPC-InstanceStore**

    # instance, image, security-group, network-interface

    #   * **EC2-VPC-InstanceStore-Subnet**

    # instance, image, security-group, network-interface, subnet

    #   * **EC2-VPC-EBS**

    # instance, image, security-group, network-interface, volume

    #   * **EC2-VPC-EBS-Subnet**

    # instance, image, security-group, network-interface, subnet, volume
    resource_handling_option: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # (Optional) Use this only when paginating results to indicate the maximum
    # number of items you want in the response. If additional items exist beyond
    # the maximum you specify, the `IsTruncated` response element is `true`.

    # If you do not include this parameter, it defaults to 100. Note that IAM
    # might return fewer results, even when there are more results available. In
    # that case, the `IsTruncated` response element returns `true` and `Marker`
    # contains a value to include in the subsequent call that tells the service
    # where to continue from.
    max_items: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Use this parameter only when paginating results and only after you receive
    # a response indicating that the results are truncated. Set it to the value
    # of the `Marker` element in the response that you received to indicate where
    # the next call should start.
    marker: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class SimulatePolicyResponse(OutputShapeBase):
    """
    Contains the response to a successful SimulatePrincipalPolicy or
    SimulateCustomPolicy request.
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
                "evaluation_results",
                "EvaluationResults",
                TypeInfo(typing.List[EvaluationResult]),
            ),
            (
                "is_truncated",
                "IsTruncated",
                TypeInfo(bool),
            ),
            (
                "marker",
                "Marker",
                TypeInfo(str),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The results of the simulation.
    evaluation_results: typing.List["EvaluationResult"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A flag that indicates whether there are more items to return. If your
    # results were truncated, you can make a subsequent pagination request using
    # the `Marker` request parameter to retrieve more items. Note that IAM might
    # return fewer than the `MaxItems` number of results even when there are more
    # results available. We recommend that you check `IsTruncated` after every
    # call to ensure that you receive all of your results.
    is_truncated: bool = dataclasses.field(default=ShapeBase.NOT_SET, )

    # When `IsTruncated` is `true`, this element is present and contains the
    # value to use for the `Marker` parameter in a subsequent pagination request.
    marker: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    def paginate(self,
                ) -> typing.Generator["SimulatePolicyResponse", None, None]:
        yield from super()._paginate()


@dataclasses.dataclass
class SimulatePrincipalPolicyRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "policy_source_arn",
                "PolicySourceArn",
                TypeInfo(str),
            ),
            (
                "action_names",
                "ActionNames",
                TypeInfo(typing.List[str]),
            ),
            (
                "policy_input_list",
                "PolicyInputList",
                TypeInfo(typing.List[str]),
            ),
            (
                "resource_arns",
                "ResourceArns",
                TypeInfo(typing.List[str]),
            ),
            (
                "resource_policy",
                "ResourcePolicy",
                TypeInfo(str),
            ),
            (
                "resource_owner",
                "ResourceOwner",
                TypeInfo(str),
            ),
            (
                "caller_arn",
                "CallerArn",
                TypeInfo(str),
            ),
            (
                "context_entries",
                "ContextEntries",
                TypeInfo(typing.List[ContextEntry]),
            ),
            (
                "resource_handling_option",
                "ResourceHandlingOption",
                TypeInfo(str),
            ),
            (
                "max_items",
                "MaxItems",
                TypeInfo(int),
            ),
            (
                "marker",
                "Marker",
                TypeInfo(str),
            ),
        ]

    # The Amazon Resource Name (ARN) of a user, group, or role whose policies you
    # want to include in the simulation. If you specify a user, group, or role,
    # the simulation includes all policies that are associated with that entity.
    # If you specify a user, the simulation also includes all policies that are
    # attached to any groups the user belongs to.

    # For more information about ARNs, see [Amazon Resource Names (ARNs) and AWS
    # Service Namespaces](http://docs.aws.amazon.com/general/latest/gr/aws-arns-
    # and-namespaces.html) in the _AWS General Reference_.
    policy_source_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A list of names of API operations to evaluate in the simulation. Each
    # operation is evaluated for each resource. Each operation must include the
    # service identifier, such as `iam:CreateUser`.
    action_names: typing.List[str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # An optional list of additional policy documents to include in the
    # simulation. Each document is specified as a string containing the complete,
    # valid JSON text of an IAM policy.

    # The [regex pattern](http://wikipedia.org/wiki/regex) used to validate this
    # parameter is a string of characters consisting of the following:

    #   * Any printable ASCII character ranging from the space character (\u0020) through the end of the ASCII character range

    #   * The printable characters in the Basic Latin and Latin-1 Supplement character set (through \u00FF)

    #   * The special characters tab (\u0009), line feed (\u000A), and carriage return (\u000D)
    policy_input_list: typing.List[str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A list of ARNs of AWS resources to include in the simulation. If this
    # parameter is not provided, then the value defaults to `*` (all resources).
    # Each API in the `ActionNames` parameter is evaluated for each resource in
    # this list. The simulation determines the access result (allowed or denied)
    # of each combination and reports it in the response.

    # The simulation does not automatically retrieve policies for the specified
    # resources. If you want to include a resource policy in the simulation, then
    # you must include the policy as a string in the `ResourcePolicy` parameter.

    # For more information about ARNs, see [Amazon Resource Names (ARNs) and AWS
    # Service Namespaces](http://docs.aws.amazon.com/general/latest/gr/aws-arns-
    # and-namespaces.html) in the _AWS General Reference_.
    resource_arns: typing.List[str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A resource-based policy to include in the simulation provided as a string.
    # Each resource in the simulation is treated as if it had this policy
    # attached. You can include only one resource-based policy in a simulation.

    # The [regex pattern](http://wikipedia.org/wiki/regex) used to validate this
    # parameter is a string of characters consisting of the following:

    #   * Any printable ASCII character ranging from the space character (\u0020) through the end of the ASCII character range

    #   * The printable characters in the Basic Latin and Latin-1 Supplement character set (through \u00FF)

    #   * The special characters tab (\u0009), line feed (\u000A), and carriage return (\u000D)
    resource_policy: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # An AWS account ID that specifies the owner of any simulated resource that
    # does not identify its owner in the resource ARN, such as an S3 bucket or
    # object. If `ResourceOwner` is specified, it is also used as the account
    # owner of any `ResourcePolicy` included in the simulation. If the
    # `ResourceOwner` parameter is not specified, then the owner of the resources
    # and the resource policy defaults to the account of the identity provided in
    # `CallerArn`. This parameter is required only if you specify a resource-
    # based policy and account that owns the resource is different from the
    # account that owns the simulated calling user `CallerArn`.
    resource_owner: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The ARN of the IAM user that you want to specify as the simulated caller of
    # the API operations. If you do not specify a `CallerArn`, it defaults to the
    # ARN of the user that you specify in `PolicySourceArn`, if you specified a
    # user. If you include both a `PolicySourceArn` (for example,
    # `arn:aws:iam::123456789012:user/David`) and a `CallerArn` (for example,
    # `arn:aws:iam::123456789012:user/Bob`), the result is that you simulate
    # calling the API operations as Bob, as if Bob had David's policies.

    # You can specify only the ARN of an IAM user. You cannot specify the ARN of
    # an assumed role, federated user, or a service principal.

    # `CallerArn` is required if you include a `ResourcePolicy` and the
    # `PolicySourceArn` is not the ARN for an IAM user. This is required so that
    # the resource-based policy's `Principal` element has a value to use in
    # evaluating the policy.

    # For more information about ARNs, see [Amazon Resource Names (ARNs) and AWS
    # Service Namespaces](http://docs.aws.amazon.com/general/latest/gr/aws-arns-
    # and-namespaces.html) in the _AWS General Reference_.
    caller_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A list of context keys and corresponding values for the simulation to use.
    # Whenever a context key is evaluated in one of the simulated IAM permission
    # policies, the corresponding value is supplied.
    context_entries: typing.List["ContextEntry"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Specifies the type of simulation to run. Different API operations that
    # support resource-based policies require different combinations of
    # resources. By specifying the type of simulation to run, you enable the
    # policy simulator to enforce the presence of the required resources to
    # ensure reliable simulation results. If your simulation does not match one
    # of the following scenarios, then you can omit this parameter. The following
    # list shows each of the supported scenario values and the resources that you
    # must define to run the simulation.

    # Each of the EC2 scenarios requires that you specify instance, image, and
    # security-group resources. If your scenario includes an EBS volume, then you
    # must specify that volume as a resource. If the EC2 scenario includes VPC,
    # then you must supply the network-interface resource. If it includes an IP
    # subnet, then you must specify the subnet resource. For more information on
    # the EC2 scenario options, see [Supported
    # Platforms](http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-supported-
    # platforms.html) in the _Amazon EC2 User Guide_.

    #   * **EC2-Classic-InstanceStore**

    # instance, image, security-group

    #   * **EC2-Classic-EBS**

    # instance, image, security-group, volume

    #   * **EC2-VPC-InstanceStore**

    # instance, image, security-group, network-interface

    #   * **EC2-VPC-InstanceStore-Subnet**

    # instance, image, security-group, network-interface, subnet

    #   * **EC2-VPC-EBS**

    # instance, image, security-group, network-interface, volume

    #   * **EC2-VPC-EBS-Subnet**

    # instance, image, security-group, network-interface, subnet, volume
    resource_handling_option: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # (Optional) Use this only when paginating results to indicate the maximum
    # number of items you want in the response. If additional items exist beyond
    # the maximum you specify, the `IsTruncated` response element is `true`.

    # If you do not include this parameter, it defaults to 100. Note that IAM
    # might return fewer results, even when there are more results available. In
    # that case, the `IsTruncated` response element returns `true` and `Marker`
    # contains a value to include in the subsequent call that tells the service
    # where to continue from.
    max_items: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Use this parameter only when paginating results and only after you receive
    # a response indicating that the results are truncated. Set it to the value
    # of the `Marker` element in the response that you received to indicate where
    # the next call should start.
    marker: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class Statement(ShapeBase):
    """
    Contains a reference to a `Statement` element in a policy document that
    determines the result of the simulation.

    This data type is used by the `MatchedStatements` member of the `
    EvaluationResult ` type.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "source_policy_id",
                "SourcePolicyId",
                TypeInfo(str),
            ),
            (
                "source_policy_type",
                "SourcePolicyType",
                TypeInfo(typing.Union[str, PolicySourceType]),
            ),
            (
                "start_position",
                "StartPosition",
                TypeInfo(Position),
            ),
            (
                "end_position",
                "EndPosition",
                TypeInfo(Position),
            ),
        ]

    # The identifier of the policy that was provided as an input.
    source_policy_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The type of the policy.
    source_policy_type: typing.Union[str, "PolicySourceType"
                                    ] = dataclasses.field(
                                        default=ShapeBase.NOT_SET,
                                    )

    # The row and column of the beginning of the `Statement` in an IAM policy.
    start_position: "Position" = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The row and column of the end of a `Statement` in an IAM policy.
    end_position: "Position" = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class UnmodifiableEntityException(ShapeBase):
    """
    The request was rejected because only the service that depends on the service-
    linked role can modify or delete the role on your behalf. The error message
    includes the name of the service that depends on this service-linked role. You
    must request the change through that service.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "message",
                "message",
                TypeInfo(str),
            ),
        ]

    message: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class UnrecognizedPublicKeyEncodingException(ShapeBase):
    """
    The request was rejected because the public key encoding format is unsupported
    or unrecognized.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "message",
                "message",
                TypeInfo(str),
            ),
        ]

    message: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class UpdateAccessKeyRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "access_key_id",
                "AccessKeyId",
                TypeInfo(str),
            ),
            (
                "status",
                "Status",
                TypeInfo(typing.Union[str, statusType]),
            ),
            (
                "user_name",
                "UserName",
                TypeInfo(str),
            ),
        ]

    # The access key ID of the secret access key you want to update.

    # This parameter allows (per its [regex
    # pattern](http://wikipedia.org/wiki/regex)) a string of characters that can
    # consist of any upper or lowercased letter or digit.
    access_key_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The status you want to assign to the secret access key. `Active` means that
    # the key can be used for API calls to AWS, while `Inactive` means that the
    # key cannot be used.
    status: typing.Union[str, "statusType"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The name of the user whose key you want to update.

    # This parameter allows (per its [regex
    # pattern](http://wikipedia.org/wiki/regex)) a string of characters
    # consisting of upper and lowercase alphanumeric characters with no spaces.
    # You can also include any of the following characters: _+=,.@-
    user_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class UpdateAccountPasswordPolicyRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "minimum_password_length",
                "MinimumPasswordLength",
                TypeInfo(int),
            ),
            (
                "require_symbols",
                "RequireSymbols",
                TypeInfo(bool),
            ),
            (
                "require_numbers",
                "RequireNumbers",
                TypeInfo(bool),
            ),
            (
                "require_uppercase_characters",
                "RequireUppercaseCharacters",
                TypeInfo(bool),
            ),
            (
                "require_lowercase_characters",
                "RequireLowercaseCharacters",
                TypeInfo(bool),
            ),
            (
                "allow_users_to_change_password",
                "AllowUsersToChangePassword",
                TypeInfo(bool),
            ),
            (
                "max_password_age",
                "MaxPasswordAge",
                TypeInfo(int),
            ),
            (
                "password_reuse_prevention",
                "PasswordReusePrevention",
                TypeInfo(int),
            ),
            (
                "hard_expiry",
                "HardExpiry",
                TypeInfo(bool),
            ),
        ]

    # The minimum number of characters allowed in an IAM user password.

    # If you do not specify a value for this parameter, then the operation uses
    # the default value of `6`.
    minimum_password_length: int = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Specifies whether IAM user passwords must contain at least one of the
    # following non-alphanumeric characters:

    # ! @ # $ % ^ & * ( ) _ + - = [ ] { } | '

    # If you do not specify a value for this parameter, then the operation uses
    # the default value of `false`. The result is that passwords do not require
    # at least one symbol character.
    require_symbols: bool = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Specifies whether IAM user passwords must contain at least one numeric
    # character (0 to 9).

    # If you do not specify a value for this parameter, then the operation uses
    # the default value of `false`. The result is that passwords do not require
    # at least one numeric character.
    require_numbers: bool = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Specifies whether IAM user passwords must contain at least one uppercase
    # character from the ISO basic Latin alphabet (A to Z).

    # If you do not specify a value for this parameter, then the operation uses
    # the default value of `false`. The result is that passwords do not require
    # at least one uppercase character.
    require_uppercase_characters: bool = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Specifies whether IAM user passwords must contain at least one lowercase
    # character from the ISO basic Latin alphabet (a to z).

    # If you do not specify a value for this parameter, then the operation uses
    # the default value of `false`. The result is that passwords do not require
    # at least one lowercase character.
    require_lowercase_characters: bool = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Allows all IAM users in your account to use the AWS Management Console to
    # change their own passwords. For more information, see [Letting IAM Users
    # Change Their Own
    # Passwords](http://docs.aws.amazon.com/IAM/latest/UserGuide/HowToPwdIAMUser.html)
    # in the _IAM User Guide_.

    # If you do not specify a value for this parameter, then the operation uses
    # the default value of `false`. The result is that IAM users in the account
    # do not automatically have permissions to change their own password.
    allow_users_to_change_password: bool = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The number of days that an IAM user password is valid.

    # If you do not specify a value for this parameter, then the operation uses
    # the default value of `0`. The result is that IAM user passwords never
    # expire.
    max_password_age: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Specifies the number of previous passwords that IAM users are prevented
    # from reusing.

    # If you do not specify a value for this parameter, then the operation uses
    # the default value of `0`. The result is that IAM users are not prevented
    # from reusing previous passwords.
    password_reuse_prevention: int = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Prevents IAM users from setting a new password after their password has
    # expired. The IAM user cannot be accessed until an administrator resets the
    # password.

    # If you do not specify a value for this parameter, then the operation uses
    # the default value of `false`. The result is that IAM users can change their
    # passwords after they expire and continue to sign in as the user.
    hard_expiry: bool = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class UpdateAssumeRolePolicyRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "role_name",
                "RoleName",
                TypeInfo(str),
            ),
            (
                "policy_document",
                "PolicyDocument",
                TypeInfo(str),
            ),
        ]

    # The name of the role to update with the new policy.

    # This parameter allows (per its [regex
    # pattern](http://wikipedia.org/wiki/regex)) a string of characters
    # consisting of upper and lowercase alphanumeric characters with no spaces.
    # You can also include any of the following characters: _+=,.@-
    role_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The policy that grants an entity permission to assume the role.

    # The [regex pattern](http://wikipedia.org/wiki/regex) used to validate this
    # parameter is a string of characters consisting of the following:

    #   * Any printable ASCII character ranging from the space character (\u0020) through the end of the ASCII character range

    #   * The printable characters in the Basic Latin and Latin-1 Supplement character set (through \u00FF)

    #   * The special characters tab (\u0009), line feed (\u000A), and carriage return (\u000D)
    policy_document: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class UpdateGroupRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "group_name",
                "GroupName",
                TypeInfo(str),
            ),
            (
                "new_path",
                "NewPath",
                TypeInfo(str),
            ),
            (
                "new_group_name",
                "NewGroupName",
                TypeInfo(str),
            ),
        ]

    # Name of the IAM group to update. If you're changing the name of the group,
    # this is the original name.

    # This parameter allows (per its [regex
    # pattern](http://wikipedia.org/wiki/regex)) a string of characters
    # consisting of upper and lowercase alphanumeric characters with no spaces.
    # You can also include any of the following characters: _+=,.@-
    group_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # New path for the IAM group. Only include this if changing the group's path.

    # This parameter allows (per its [regex
    # pattern](http://wikipedia.org/wiki/regex)) a string of characters
    # consisting of either a forward slash (/) by itself or a string that must
    # begin and end with forward slashes. In addition, it can contain any ASCII
    # character from the ! (\u0021) through the DEL character (\u007F), including
    # most punctuation characters, digits, and upper and lowercased letters.
    new_path: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # New name for the IAM group. Only include this if changing the group's name.

    # This parameter allows (per its [regex
    # pattern](http://wikipedia.org/wiki/regex)) a string of characters
    # consisting of upper and lowercase alphanumeric characters with no spaces.
    # You can also include any of the following characters: _+=,.@-
    new_group_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class UpdateLoginProfileRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "user_name",
                "UserName",
                TypeInfo(str),
            ),
            (
                "password",
                "Password",
                TypeInfo(str),
            ),
            (
                "password_reset_required",
                "PasswordResetRequired",
                TypeInfo(bool),
            ),
        ]

    # The name of the user whose password you want to update.

    # This parameter allows (per its [regex
    # pattern](http://wikipedia.org/wiki/regex)) a string of characters
    # consisting of upper and lowercase alphanumeric characters with no spaces.
    # You can also include any of the following characters: _+=,.@-
    user_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The new password for the specified IAM user.

    # The [regex pattern](http://wikipedia.org/wiki/regex) used to validate this
    # parameter is a string of characters consisting of the following:

    #   * Any printable ASCII character ranging from the space character (\u0020) through the end of the ASCII character range

    #   * The printable characters in the Basic Latin and Latin-1 Supplement character set (through \u00FF)

    #   * The special characters tab (\u0009), line feed (\u000A), and carriage return (\u000D)

    # However, the format can be further restricted by the account administrator
    # by setting a password policy on the AWS account. For more information, see
    # UpdateAccountPasswordPolicy.
    password: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Allows this new password to be used only once by requiring the specified
    # IAM user to set a new password on next sign-in.
    password_reset_required: bool = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class UpdateOpenIDConnectProviderThumbprintRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "open_id_connect_provider_arn",
                "OpenIDConnectProviderArn",
                TypeInfo(str),
            ),
            (
                "thumbprint_list",
                "ThumbprintList",
                TypeInfo(typing.List[str]),
            ),
        ]

    # The Amazon Resource Name (ARN) of the IAM OIDC provider resource object for
    # which you want to update the thumbprint. You can get a list of OIDC
    # provider ARNs by using the ListOpenIDConnectProviders operation.

    # For more information about ARNs, see [Amazon Resource Names (ARNs) and AWS
    # Service Namespaces](http://docs.aws.amazon.com/general/latest/gr/aws-arns-
    # and-namespaces.html) in the _AWS General Reference_.
    open_id_connect_provider_arn: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A list of certificate thumbprints that are associated with the specified
    # IAM OpenID Connect provider. For more information, see
    # CreateOpenIDConnectProvider.
    thumbprint_list: typing.List[str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class UpdateRoleDescriptionRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "role_name",
                "RoleName",
                TypeInfo(str),
            ),
            (
                "description",
                "Description",
                TypeInfo(str),
            ),
        ]

    # The name of the role that you want to modify.
    role_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The new description that you want to apply to the specified role.
    description: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class UpdateRoleDescriptionResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "role",
                "Role",
                TypeInfo(Role),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A structure that contains details about the modified role.
    role: "Role" = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class UpdateRoleRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "role_name",
                "RoleName",
                TypeInfo(str),
            ),
            (
                "description",
                "Description",
                TypeInfo(str),
            ),
            (
                "max_session_duration",
                "MaxSessionDuration",
                TypeInfo(int),
            ),
        ]

    # The name of the role that you want to modify.
    role_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The new description that you want to apply to the specified role.
    description: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The maximum session duration (in seconds) that you want to set for the
    # specified role. If you do not specify a value for this setting, the default
    # maximum of one hour is applied. This setting can have a value from 1 hour
    # to 12 hours.

    # Anyone who assumes the role from the AWS CLI or API can use the
    # `DurationSeconds` API parameter or the `duration-seconds` CLI parameter to
    # request a longer session. The `MaxSessionDuration` setting determines the
    # maximum duration that can be requested using the `DurationSeconds`
    # parameter. If users don't specify a value for the `DurationSeconds`
    # parameter, their security credentials are valid for one hour by default.
    # This applies when you use the `AssumeRole*` API operations or the `assume-
    # role*` CLI operations but does not apply when you use those operations to
    # create a console URL. For more information, see [Using IAM
    # Roles](http://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use.html)
    # in the _IAM User Guide_.
    max_session_duration: int = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class UpdateRoleResponse(OutputShapeBase):
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
class UpdateSAMLProviderRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "saml_metadata_document",
                "SAMLMetadataDocument",
                TypeInfo(str),
            ),
            (
                "saml_provider_arn",
                "SAMLProviderArn",
                TypeInfo(str),
            ),
        ]

    # An XML document generated by an identity provider (IdP) that supports SAML
    # 2.0. The document includes the issuer's name, expiration information, and
    # keys that can be used to validate the SAML authentication response
    # (assertions) that are received from the IdP. You must generate the metadata
    # document using the identity management software that is used as your
    # organization's IdP.
    saml_metadata_document: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The Amazon Resource Name (ARN) of the SAML provider to update.

    # For more information about ARNs, see [Amazon Resource Names (ARNs) and AWS
    # Service Namespaces](http://docs.aws.amazon.com/general/latest/gr/aws-arns-
    # and-namespaces.html) in the _AWS General Reference_.
    saml_provider_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class UpdateSAMLProviderResponse(OutputShapeBase):
    """
    Contains the response to a successful UpdateSAMLProvider request.
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
                "saml_provider_arn",
                "SAMLProviderArn",
                TypeInfo(str),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The Amazon Resource Name (ARN) of the SAML provider that was updated.
    saml_provider_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class UpdateSSHPublicKeyRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "user_name",
                "UserName",
                TypeInfo(str),
            ),
            (
                "ssh_public_key_id",
                "SSHPublicKeyId",
                TypeInfo(str),
            ),
            (
                "status",
                "Status",
                TypeInfo(typing.Union[str, statusType]),
            ),
        ]

    # The name of the IAM user associated with the SSH public key.

    # This parameter allows (per its [regex
    # pattern](http://wikipedia.org/wiki/regex)) a string of characters
    # consisting of upper and lowercase alphanumeric characters with no spaces.
    # You can also include any of the following characters: _+=,.@-
    user_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The unique identifier for the SSH public key.

    # This parameter allows (per its [regex
    # pattern](http://wikipedia.org/wiki/regex)) a string of characters that can
    # consist of any upper or lowercased letter or digit.
    ssh_public_key_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The status to assign to the SSH public key. `Active` means that the key can
    # be used for authentication with an AWS CodeCommit repository. `Inactive`
    # means that the key cannot be used.
    status: typing.Union[str, "statusType"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class UpdateServerCertificateRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "server_certificate_name",
                "ServerCertificateName",
                TypeInfo(str),
            ),
            (
                "new_path",
                "NewPath",
                TypeInfo(str),
            ),
            (
                "new_server_certificate_name",
                "NewServerCertificateName",
                TypeInfo(str),
            ),
        ]

    # The name of the server certificate that you want to update.

    # This parameter allows (per its [regex
    # pattern](http://wikipedia.org/wiki/regex)) a string of characters
    # consisting of upper and lowercase alphanumeric characters with no spaces.
    # You can also include any of the following characters: _+=,.@-
    server_certificate_name: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The new path for the server certificate. Include this only if you are
    # updating the server certificate's path.

    # This parameter allows (per its [regex
    # pattern](http://wikipedia.org/wiki/regex)) a string of characters
    # consisting of either a forward slash (/) by itself or a string that must
    # begin and end with forward slashes. In addition, it can contain any ASCII
    # character from the ! (\u0021) through the DEL character (\u007F), including
    # most punctuation characters, digits, and upper and lowercased letters.
    new_path: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The new name for the server certificate. Include this only if you are
    # updating the server certificate's name. The name of the certificate cannot
    # contain any spaces.

    # This parameter allows (per its [regex
    # pattern](http://wikipedia.org/wiki/regex)) a string of characters
    # consisting of upper and lowercase alphanumeric characters with no spaces.
    # You can also include any of the following characters: _+=,.@-
    new_server_certificate_name: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class UpdateServiceSpecificCredentialRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "service_specific_credential_id",
                "ServiceSpecificCredentialId",
                TypeInfo(str),
            ),
            (
                "status",
                "Status",
                TypeInfo(typing.Union[str, statusType]),
            ),
            (
                "user_name",
                "UserName",
                TypeInfo(str),
            ),
        ]

    # The unique identifier of the service-specific credential.

    # This parameter allows (per its [regex
    # pattern](http://wikipedia.org/wiki/regex)) a string of characters that can
    # consist of any upper or lowercased letter or digit.
    service_specific_credential_id: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The status to be assigned to the service-specific credential.
    status: typing.Union[str, "statusType"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The name of the IAM user associated with the service-specific credential.
    # If you do not specify this value, then the operation assumes the user whose
    # credentials are used to call the operation.

    # This parameter allows (per its [regex
    # pattern](http://wikipedia.org/wiki/regex)) a string of characters
    # consisting of upper and lowercase alphanumeric characters with no spaces.
    # You can also include any of the following characters: _+=,.@-
    user_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class UpdateSigningCertificateRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "certificate_id",
                "CertificateId",
                TypeInfo(str),
            ),
            (
                "status",
                "Status",
                TypeInfo(typing.Union[str, statusType]),
            ),
            (
                "user_name",
                "UserName",
                TypeInfo(str),
            ),
        ]

    # The ID of the signing certificate you want to update.

    # This parameter allows (per its [regex
    # pattern](http://wikipedia.org/wiki/regex)) a string of characters that can
    # consist of any upper or lowercased letter or digit.
    certificate_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The status you want to assign to the certificate. `Active` means that the
    # certificate can be used for API calls to AWS `Inactive` means that the
    # certificate cannot be used.
    status: typing.Union[str, "statusType"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The name of the IAM user the signing certificate belongs to.

    # This parameter allows (per its [regex
    # pattern](http://wikipedia.org/wiki/regex)) a string of characters
    # consisting of upper and lowercase alphanumeric characters with no spaces.
    # You can also include any of the following characters: _+=,.@-
    user_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class UpdateUserRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "user_name",
                "UserName",
                TypeInfo(str),
            ),
            (
                "new_path",
                "NewPath",
                TypeInfo(str),
            ),
            (
                "new_user_name",
                "NewUserName",
                TypeInfo(str),
            ),
        ]

    # Name of the user to update. If you're changing the name of the user, this
    # is the original user name.

    # This parameter allows (per its [regex
    # pattern](http://wikipedia.org/wiki/regex)) a string of characters
    # consisting of upper and lowercase alphanumeric characters with no spaces.
    # You can also include any of the following characters: _+=,.@-
    user_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # New path for the IAM user. Include this parameter only if you're changing
    # the user's path.

    # This parameter allows (per its [regex
    # pattern](http://wikipedia.org/wiki/regex)) a string of characters
    # consisting of either a forward slash (/) by itself or a string that must
    # begin and end with forward slashes. In addition, it can contain any ASCII
    # character from the ! (\u0021) through the DEL character (\u007F), including
    # most punctuation characters, digits, and upper and lowercased letters.
    new_path: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # New name for the user. Include this parameter only if you're changing the
    # user's name.

    # This parameter allows (per its [regex
    # pattern](http://wikipedia.org/wiki/regex)) a string of characters
    # consisting of upper and lowercase alphanumeric characters with no spaces.
    # You can also include any of the following characters: _+=,.@-
    new_user_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class UploadSSHPublicKeyRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "user_name",
                "UserName",
                TypeInfo(str),
            ),
            (
                "ssh_public_key_body",
                "SSHPublicKeyBody",
                TypeInfo(str),
            ),
        ]

    # The name of the IAM user to associate the SSH public key with.

    # This parameter allows (per its [regex
    # pattern](http://wikipedia.org/wiki/regex)) a string of characters
    # consisting of upper and lowercase alphanumeric characters with no spaces.
    # You can also include any of the following characters: _+=,.@-
    user_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The SSH public key. The public key must be encoded in ssh-rsa format or PEM
    # format. The miminum bit-length of the public key is 2048 bits. For example,
    # you can generate a 2048-bit key, and the resulting PEM file is 1679 bytes
    # long.

    # The [regex pattern](http://wikipedia.org/wiki/regex) used to validate this
    # parameter is a string of characters consisting of the following:

    #   * Any printable ASCII character ranging from the space character (\u0020) through the end of the ASCII character range

    #   * The printable characters in the Basic Latin and Latin-1 Supplement character set (through \u00FF)

    #   * The special characters tab (\u0009), line feed (\u000A), and carriage return (\u000D)
    ssh_public_key_body: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class UploadSSHPublicKeyResponse(OutputShapeBase):
    """
    Contains the response to a successful UploadSSHPublicKey request.
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
                "ssh_public_key",
                "SSHPublicKey",
                TypeInfo(SSHPublicKey),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Contains information about the SSH public key.
    ssh_public_key: "SSHPublicKey" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class UploadServerCertificateRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "server_certificate_name",
                "ServerCertificateName",
                TypeInfo(str),
            ),
            (
                "certificate_body",
                "CertificateBody",
                TypeInfo(str),
            ),
            (
                "private_key",
                "PrivateKey",
                TypeInfo(str),
            ),
            (
                "path",
                "Path",
                TypeInfo(str),
            ),
            (
                "certificate_chain",
                "CertificateChain",
                TypeInfo(str),
            ),
        ]

    # The name for the server certificate. Do not include the path in this value.
    # The name of the certificate cannot contain any spaces.

    # This parameter allows (per its [regex
    # pattern](http://wikipedia.org/wiki/regex)) a string of characters
    # consisting of upper and lowercase alphanumeric characters with no spaces.
    # You can also include any of the following characters: _+=,.@-
    server_certificate_name: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The contents of the public key certificate in PEM-encoded format.

    # The [regex pattern](http://wikipedia.org/wiki/regex) used to validate this
    # parameter is a string of characters consisting of the following:

    #   * Any printable ASCII character ranging from the space character (\u0020) through the end of the ASCII character range

    #   * The printable characters in the Basic Latin and Latin-1 Supplement character set (through \u00FF)

    #   * The special characters tab (\u0009), line feed (\u000A), and carriage return (\u000D)
    certificate_body: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The contents of the private key in PEM-encoded format.

    # The [regex pattern](http://wikipedia.org/wiki/regex) used to validate this
    # parameter is a string of characters consisting of the following:

    #   * Any printable ASCII character ranging from the space character (\u0020) through the end of the ASCII character range

    #   * The printable characters in the Basic Latin and Latin-1 Supplement character set (through \u00FF)

    #   * The special characters tab (\u0009), line feed (\u000A), and carriage return (\u000D)
    private_key: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The path for the server certificate. For more information about paths, see
    # [IAM
    # Identifiers](http://docs.aws.amazon.com/IAM/latest/UserGuide/Using_Identifiers.html)
    # in the _IAM User Guide_.

    # This parameter is optional. If it is not included, it defaults to a slash
    # (/). This parameter allows (per its [regex
    # pattern](http://wikipedia.org/wiki/regex)) a string of characters
    # consisting of either a forward slash (/) by itself or a string that must
    # begin and end with forward slashes. In addition, it can contain any ASCII
    # character from the ! (\u0021) through the DEL character (\u007F), including
    # most punctuation characters, digits, and upper and lowercased letters.

    # If you are uploading a server certificate specifically for use with Amazon
    # CloudFront distributions, you must specify a path using the `path`
    # parameter. The path must begin with `/cloudfront` and must include a
    # trailing slash (for example, `/cloudfront/test/`).
    path: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The contents of the certificate chain. This is typically a concatenation of
    # the PEM-encoded public key certificates of the chain.

    # The [regex pattern](http://wikipedia.org/wiki/regex) used to validate this
    # parameter is a string of characters consisting of the following:

    #   * Any printable ASCII character ranging from the space character (\u0020) through the end of the ASCII character range

    #   * The printable characters in the Basic Latin and Latin-1 Supplement character set (through \u00FF)

    #   * The special characters tab (\u0009), line feed (\u000A), and carriage return (\u000D)
    certificate_chain: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class UploadServerCertificateResponse(OutputShapeBase):
    """
    Contains the response to a successful UploadServerCertificate request.
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
                "server_certificate_metadata",
                "ServerCertificateMetadata",
                TypeInfo(ServerCertificateMetadata),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The meta information of the uploaded server certificate without its
    # certificate body, certificate chain, and private key.
    server_certificate_metadata: "ServerCertificateMetadata" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class UploadSigningCertificateRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "certificate_body",
                "CertificateBody",
                TypeInfo(str),
            ),
            (
                "user_name",
                "UserName",
                TypeInfo(str),
            ),
        ]

    # The contents of the signing certificate.

    # The [regex pattern](http://wikipedia.org/wiki/regex) used to validate this
    # parameter is a string of characters consisting of the following:

    #   * Any printable ASCII character ranging from the space character (\u0020) through the end of the ASCII character range

    #   * The printable characters in the Basic Latin and Latin-1 Supplement character set (through \u00FF)

    #   * The special characters tab (\u0009), line feed (\u000A), and carriage return (\u000D)
    certificate_body: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The name of the user the signing certificate is for.

    # This parameter allows (per its [regex
    # pattern](http://wikipedia.org/wiki/regex)) a string of characters
    # consisting of upper and lowercase alphanumeric characters with no spaces.
    # You can also include any of the following characters: _+=,.@-
    user_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class UploadSigningCertificateResponse(OutputShapeBase):
    """
    Contains the response to a successful UploadSigningCertificate request.
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
                "certificate",
                "Certificate",
                TypeInfo(SigningCertificate),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Information about the certificate.
    certificate: "SigningCertificate" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class User(ShapeBase):
    """
    Contains information about an IAM user entity.

    This data type is used as a response element in the following operations:

      * CreateUser

      * GetUser

      * ListUsers
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "path",
                "Path",
                TypeInfo(str),
            ),
            (
                "user_name",
                "UserName",
                TypeInfo(str),
            ),
            (
                "user_id",
                "UserId",
                TypeInfo(str),
            ),
            (
                "arn",
                "Arn",
                TypeInfo(str),
            ),
            (
                "create_date",
                "CreateDate",
                TypeInfo(datetime.datetime),
            ),
            (
                "password_last_used",
                "PasswordLastUsed",
                TypeInfo(datetime.datetime),
            ),
            (
                "permissions_boundary",
                "PermissionsBoundary",
                TypeInfo(AttachedPermissionsBoundary),
            ),
        ]

    # The path to the user. For more information about paths, see [IAM
    # Identifiers](http://docs.aws.amazon.com/IAM/latest/UserGuide/Using_Identifiers.html)
    # in the _Using IAM_ guide.
    path: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The friendly name identifying the user.
    user_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The stable and unique string identifying the user. For more information
    # about IDs, see [IAM
    # Identifiers](http://docs.aws.amazon.com/IAM/latest/UserGuide/Using_Identifiers.html)
    # in the _Using IAM_ guide.
    user_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The Amazon Resource Name (ARN) that identifies the user. For more
    # information about ARNs and how to use ARNs in policies, see [IAM
    # Identifiers](http://docs.aws.amazon.com/IAM/latest/UserGuide/Using_Identifiers.html)
    # in the _Using IAM_ guide.
    arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The date and time, in [ISO 8601 date-time
    # format](http://www.iso.org/iso/iso8601), when the user was created.
    create_date: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The date and time, in [ISO 8601 date-time
    # format](http://www.iso.org/iso/iso8601), when the user's password was last
    # used to sign in to an AWS website. For a list of AWS websites that capture
    # a user's last sign-in time, see the [Credential
    # Reports](http://docs.aws.amazon.com/IAM/latest/UserGuide/credential-
    # reports.html) topic in the _Using IAM_ guide. If a password is used more
    # than once in a five-minute span, only the first use is returned in this
    # field. If the field is null (no value) then it indicates that they never
    # signed in with a password. This can be because:

    #   * The user never had a password.

    #   * A password exists but has not been used since IAM started tracking this information on October 20th, 2014.

    # A null does not mean that the user _never_ had a password. Also, if the
    # user does not currently have a password, but had one in the past, then this
    # field contains the date and time the most recent password was used.

    # This value is returned only in the GetUser and ListUsers operations.
    password_last_used: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The ARN of the policy used to set the permissions boundary for the user.

    # For more information about permissions boundaries, see [Permissions
    # Boundaries for IAM Identities
    # ](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_boundaries.html)
    # in the _IAM User Guide_.
    permissions_boundary: "AttachedPermissionsBoundary" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class UserDetail(ShapeBase):
    """
    Contains information about an IAM user, including all the user's policies and
    all the IAM groups the user is in.

    This data type is used as a response element in the
    GetAccountAuthorizationDetails operation.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "path",
                "Path",
                TypeInfo(str),
            ),
            (
                "user_name",
                "UserName",
                TypeInfo(str),
            ),
            (
                "user_id",
                "UserId",
                TypeInfo(str),
            ),
            (
                "arn",
                "Arn",
                TypeInfo(str),
            ),
            (
                "create_date",
                "CreateDate",
                TypeInfo(datetime.datetime),
            ),
            (
                "user_policy_list",
                "UserPolicyList",
                TypeInfo(typing.List[PolicyDetail]),
            ),
            (
                "group_list",
                "GroupList",
                TypeInfo(typing.List[str]),
            ),
            (
                "attached_managed_policies",
                "AttachedManagedPolicies",
                TypeInfo(typing.List[AttachedPolicy]),
            ),
            (
                "permissions_boundary",
                "PermissionsBoundary",
                TypeInfo(AttachedPermissionsBoundary),
            ),
        ]

    # The path to the user. For more information about paths, see [IAM
    # Identifiers](http://docs.aws.amazon.com/IAM/latest/UserGuide/Using_Identifiers.html)
    # in the _Using IAM_ guide.
    path: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The friendly name identifying the user.
    user_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The stable and unique string identifying the user. For more information
    # about IDs, see [IAM
    # Identifiers](http://docs.aws.amazon.com/IAM/latest/UserGuide/Using_Identifiers.html)
    # in the _Using IAM_ guide.
    user_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The Amazon Resource Name (ARN). ARNs are unique identifiers for AWS
    # resources.

    # For more information about ARNs, go to [Amazon Resource Names (ARNs) and
    # AWS Service Namespaces](http://docs.aws.amazon.com/general/latest/gr/aws-
    # arns-and-namespaces.html) in the _AWS General Reference_.
    arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The date and time, in [ISO 8601 date-time
    # format](http://www.iso.org/iso/iso8601), when the user was created.
    create_date: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A list of the inline policies embedded in the user.
    user_policy_list: typing.List["PolicyDetail"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A list of IAM groups that the user is in.
    group_list: typing.List[str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A list of the managed policies attached to the user.
    attached_managed_policies: typing.List["AttachedPolicy"
                                          ] = dataclasses.field(
                                              default=ShapeBase.NOT_SET,
                                          )

    # The ARN of the policy used to set the permissions boundary for the user.

    # For more information about permissions boundaries, see [Permissions
    # Boundaries for IAM Identities
    # ](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_boundaries.html)
    # in the _IAM User Guide_.
    permissions_boundary: "AttachedPermissionsBoundary" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class VirtualMFADevice(ShapeBase):
    """
    Contains information about a virtual MFA device.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "serial_number",
                "SerialNumber",
                TypeInfo(str),
            ),
            (
                "base32_string_seed",
                "Base32StringSeed",
                TypeInfo(typing.Any),
            ),
            (
                "qr_code_png",
                "QRCodePNG",
                TypeInfo(typing.Any),
            ),
            (
                "user",
                "User",
                TypeInfo(User),
            ),
            (
                "enable_date",
                "EnableDate",
                TypeInfo(datetime.datetime),
            ),
        ]

    # The serial number associated with `VirtualMFADevice`.
    serial_number: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The Base32 seed defined as specified in
    # [RFC3548](https://tools.ietf.org/html/rfc3548.txt). The `Base32StringSeed`
    # is Base64-encoded.
    base32_string_seed: typing.Any = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A QR code PNG image that encodes
    # `otpauth://totp/$virtualMFADeviceName@$AccountName?secret=$Base32String`
    # where `$virtualMFADeviceName` is one of the create call arguments,
    # `AccountName` is the user name if set (otherwise, the account ID
    # otherwise), and `Base32String` is the seed in Base32 format. The
    # `Base32String` value is Base64-encoded.
    qr_code_png: typing.Any = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The IAM user associated with this virtual MFA device.
    user: "User" = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The date and time on which the virtual MFA device was enabled.
    enable_date: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


class assignmentStatusType(str):
    Assigned = "Assigned"
    Unassigned = "Unassigned"
    Any = "Any"


class encodingType(str):
    SSH = "SSH"
    PEM = "PEM"


class policyScopeType(str):
    All = "All"
    AWS = "AWS"
    Local = "Local"


class statusType(str):
    Active = "Active"
    Inactive = "Inactive"


class summaryKeyType(str):
    Users = "Users"
    UsersQuota = "UsersQuota"
    Groups = "Groups"
    GroupsQuota = "GroupsQuota"
    ServerCertificates = "ServerCertificates"
    ServerCertificatesQuota = "ServerCertificatesQuota"
    UserPolicySizeQuota = "UserPolicySizeQuota"
    GroupPolicySizeQuota = "GroupPolicySizeQuota"
    GroupsPerUserQuota = "GroupsPerUserQuota"
    SigningCertificatesPerUserQuota = "SigningCertificatesPerUserQuota"
    AccessKeysPerUserQuota = "AccessKeysPerUserQuota"
    MFADevices = "MFADevices"
    MFADevicesInUse = "MFADevicesInUse"
    AccountMFAEnabled = "AccountMFAEnabled"
    AccountAccessKeysPresent = "AccountAccessKeysPresent"
    AccountSigningCertificatesPresent = "AccountSigningCertificatesPresent"
    AttachedPoliciesPerGroupQuota = "AttachedPoliciesPerGroupQuota"
    AttachedPoliciesPerRoleQuota = "AttachedPoliciesPerRoleQuota"
    AttachedPoliciesPerUserQuota = "AttachedPoliciesPerUserQuota"
    Policies = "Policies"
    PoliciesQuota = "PoliciesQuota"
    PolicySizeQuota = "PolicySizeQuota"
    PolicyVersionsInUse = "PolicyVersionsInUse"
    PolicyVersionsInUseQuota = "PolicyVersionsInUseQuota"
    VersionsPerPolicyQuota = "VersionsPerPolicyQuota"
