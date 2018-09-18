import datetime
import typing
from autoboto import ShapeBase, OutputShapeBase, TypeInfo
import botocore.response
import dataclasses


class AlgorithmSpec(str):
    RSAES_PKCS1_V1_5 = "RSAES_PKCS1_V1_5"
    RSAES_OAEP_SHA_1 = "RSAES_OAEP_SHA_1"
    RSAES_OAEP_SHA_256 = "RSAES_OAEP_SHA_256"


@dataclasses.dataclass
class AliasListEntry(ShapeBase):
    """
    Contains information about an alias.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "alias_name",
                "AliasName",
                TypeInfo(str),
            ),
            (
                "alias_arn",
                "AliasArn",
                TypeInfo(str),
            ),
            (
                "target_key_id",
                "TargetKeyId",
                TypeInfo(str),
            ),
        ]

    # String that contains the alias.
    alias_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # String that contains the key ARN.
    alias_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # String that contains the key identifier referred to by the alias.
    target_key_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class AlreadyExistsException(ShapeBase):
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
class CancelKeyDeletionRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "key_id",
                "KeyId",
                TypeInfo(str),
            ),
        ]

    # The unique identifier for the customer master key (CMK) for which to cancel
    # deletion.

    # Specify the key ID or the Amazon Resource Name (ARN) of the CMK.

    # For example:

    #   * Key ID: `1234abcd-12ab-34cd-56ef-1234567890ab`

    #   * Key ARN: `arn:aws:kms:us-east-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab`

    # To get the key ID and key ARN for a CMK, use ListKeys or DescribeKey.
    key_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class CancelKeyDeletionResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "key_id",
                "KeyId",
                TypeInfo(str),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The unique identifier of the master key for which deletion is canceled.
    key_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )


class CiphertextType(botocore.response.StreamingBody):
    pass


@dataclasses.dataclass
class CreateAliasRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "alias_name",
                "AliasName",
                TypeInfo(str),
            ),
            (
                "target_key_id",
                "TargetKeyId",
                TypeInfo(str),
            ),
        ]

    # Specifies the alias name. This value must begin with `alias/` followed by
    # the alias name, such as `alias/ExampleAlias`. The alias name cannot begin
    # with `aws/`. The `alias/aws/` prefix is reserved for AWS managed CMKs.
    alias_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Identifies the CMK for which you are creating the alias. This value cannot
    # be an alias.

    # Specify the key ID or the Amazon Resource Name (ARN) of the CMK.

    # For example:

    #   * Key ID: `1234abcd-12ab-34cd-56ef-1234567890ab`

    #   * Key ARN: `arn:aws:kms:us-east-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab`

    # To get the key ID and key ARN for a CMK, use ListKeys or DescribeKey.
    target_key_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class CreateGrantRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "key_id",
                "KeyId",
                TypeInfo(str),
            ),
            (
                "grantee_principal",
                "GranteePrincipal",
                TypeInfo(str),
            ),
            (
                "operations",
                "Operations",
                TypeInfo(typing.List[typing.Union[str, GrantOperation]]),
            ),
            (
                "retiring_principal",
                "RetiringPrincipal",
                TypeInfo(str),
            ),
            (
                "constraints",
                "Constraints",
                TypeInfo(GrantConstraints),
            ),
            (
                "grant_tokens",
                "GrantTokens",
                TypeInfo(typing.List[str]),
            ),
            (
                "name",
                "Name",
                TypeInfo(str),
            ),
        ]

    # The unique identifier for the customer master key (CMK) that the grant
    # applies to.

    # Specify the key ID or the Amazon Resource Name (ARN) of the CMK. To specify
    # a CMK in a different AWS account, you must use the key ARN.

    # For example:

    #   * Key ID: `1234abcd-12ab-34cd-56ef-1234567890ab`

    #   * Key ARN: `arn:aws:kms:us-east-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab`

    # To get the key ID and key ARN for a CMK, use ListKeys or DescribeKey.
    key_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The principal that is given permission to perform the operations that the
    # grant permits.

    # To specify the principal, use the [Amazon Resource Name
    # (ARN)](http://docs.aws.amazon.com/general/latest/gr/aws-arns-and-
    # namespaces.html) of an AWS principal. Valid AWS principals include AWS
    # accounts (root), IAM users, IAM roles, federated users, and assumed role
    # users. For examples of the ARN syntax to use for specifying a principal,
    # see [AWS Identity and Access Management
    # (IAM)](http://docs.aws.amazon.com/general/latest/gr/aws-arns-and-
    # namespaces.html#arn-syntax-iam) in the Example ARNs section of the _AWS
    # General Reference_.
    grantee_principal: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A list of operations that the grant permits.
    operations: typing.List[typing.Union[str, "GrantOperation"]
                           ] = dataclasses.field(
                               default=ShapeBase.NOT_SET,
                           )

    # The principal that is given permission to retire the grant by using
    # RetireGrant operation.

    # To specify the principal, use the [Amazon Resource Name
    # (ARN)](http://docs.aws.amazon.com/general/latest/gr/aws-arns-and-
    # namespaces.html) of an AWS principal. Valid AWS principals include AWS
    # accounts (root), IAM users, federated users, and assumed role users. For
    # examples of the ARN syntax to use for specifying a principal, see [AWS
    # Identity and Access Management
    # (IAM)](http://docs.aws.amazon.com/general/latest/gr/aws-arns-and-
    # namespaces.html#arn-syntax-iam) in the Example ARNs section of the _AWS
    # General Reference_.
    retiring_principal: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A structure that you can use to allow certain operations in the grant only
    # when the desired encryption context is present. For more information about
    # encryption context, see [Encryption
    # Context](http://docs.aws.amazon.com/kms/latest/developerguide/encryption-
    # context.html) in the _AWS Key Management Service Developer Guide_.
    constraints: "GrantConstraints" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A list of grant tokens.

    # For more information, see [Grant
    # Tokens](http://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#grant_token)
    # in the _AWS Key Management Service Developer Guide_.
    grant_tokens: typing.List[str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A friendly name for identifying the grant. Use this value to prevent the
    # unintended creation of duplicate grants when retrying this request.

    # When this value is absent, all `CreateGrant` requests result in a new grant
    # with a unique `GrantId` even if all the supplied parameters are identical.
    # This can result in unintended duplicates when you retry the `CreateGrant`
    # request.

    # When this value is present, you can retry a `CreateGrant` request with
    # identical parameters; if the grant already exists, the original `GrantId`
    # is returned without creating a new grant. Note that the returned grant
    # token is unique with every `CreateGrant` request, even when a duplicate
    # `GrantId` is returned. All grant tokens obtained in this way can be used
    # interchangeably.
    name: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class CreateGrantResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "grant_token",
                "GrantToken",
                TypeInfo(str),
            ),
            (
                "grant_id",
                "GrantId",
                TypeInfo(str),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The grant token.

    # For more information, see [Grant
    # Tokens](http://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#grant_token)
    # in the _AWS Key Management Service Developer Guide_.
    grant_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The unique identifier for the grant.

    # You can use the `GrantId` in a subsequent RetireGrant or RevokeGrant
    # operation.
    grant_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class CreateKeyRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "policy",
                "Policy",
                TypeInfo(str),
            ),
            (
                "description",
                "Description",
                TypeInfo(str),
            ),
            (
                "key_usage",
                "KeyUsage",
                TypeInfo(typing.Union[str, KeyUsageType]),
            ),
            (
                "origin",
                "Origin",
                TypeInfo(typing.Union[str, OriginType]),
            ),
            (
                "bypass_policy_lockout_safety_check",
                "BypassPolicyLockoutSafetyCheck",
                TypeInfo(bool),
            ),
            (
                "tags",
                "Tags",
                TypeInfo(typing.List[Tag]),
            ),
        ]

    # The key policy to attach to the CMK.

    # If you provide a key policy, it must meet the following criteria:

    #   * If you don't set `BypassPolicyLockoutSafetyCheck` to true, the key policy must allow the principal that is making the `CreateKey` request to make a subsequent PutKeyPolicy request on the CMK. This reduces the risk that the CMK becomes unmanageable. For more information, refer to the scenario in the [Default Key Policy](http://docs.aws.amazon.com/kms/latest/developerguide/key-policies.html#key-policy-default-allow-root-enable-iam) section of the _AWS Key Management Service Developer Guide_.

    #   * Each statement in the key policy must contain one or more principals. The principals in the key policy must exist and be visible to AWS KMS. When you create a new AWS principal (for example, an IAM user or role), you might need to enforce a delay before including the new principal in a key policy. The reason for this is that the new principal might not be immediately visible to AWS KMS. For more information, see [Changes that I make are not always immediately visible](http://docs.aws.amazon.com/IAM/latest/UserGuide/troubleshoot_general.html#troubleshoot_general_eventual-consistency) in the _AWS Identity and Access Management User Guide_.

    # If you do not provide a key policy, AWS KMS attaches a default key policy
    # to the CMK. For more information, see [Default Key
    # Policy](http://docs.aws.amazon.com/kms/latest/developerguide/key-
    # policies.html#key-policy-default) in the _AWS Key Management Service
    # Developer Guide_.

    # The key policy size limit is 32 kilobytes (32768 bytes).
    policy: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A description of the CMK.

    # Use a description that helps you decide whether the CMK is appropriate for
    # a task.
    description: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The intended use of the CMK.

    # You can use CMKs only for symmetric encryption and decryption.
    key_usage: typing.Union[str, "KeyUsageType"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The source of the CMK's key material.

    # The default is `AWS_KMS`, which means AWS KMS creates the key material.
    # When this parameter is set to `EXTERNAL`, the request creates a CMK without
    # key material so that you can import key material from your existing key
    # management infrastructure. For more information about importing key
    # material into AWS KMS, see [Importing Key
    # Material](http://docs.aws.amazon.com/kms/latest/developerguide/importing-
    # keys.html) in the _AWS Key Management Service Developer Guide_.

    # The CMK's `Origin` is immutable and is set when the CMK is created.
    origin: typing.Union[str, "OriginType"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A flag to indicate whether to bypass the key policy lockout safety check.

    # Setting this value to true increases the risk that the CMK becomes
    # unmanageable. Do not set this value to true indiscriminately.

    # For more information, refer to the scenario in the [Default Key
    # Policy](http://docs.aws.amazon.com/kms/latest/developerguide/key-
    # policies.html#key-policy-default-allow-root-enable-iam) section in the _AWS
    # Key Management Service Developer Guide_.

    # Use this parameter only when you include a policy in the request and you
    # intend to prevent the principal that is making the request from making a
    # subsequent PutKeyPolicy request on the CMK.

    # The default value is false.
    bypass_policy_lockout_safety_check: bool = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # One or more tags. Each tag consists of a tag key and a tag value. Tag keys
    # and tag values are both required, but tag values can be empty (null)
    # strings.

    # Use this parameter to tag the CMK when it is created. Alternately, you can
    # omit this parameter and instead tag the CMK after it is created using
    # TagResource.
    tags: typing.List["Tag"] = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class CreateKeyResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "key_metadata",
                "KeyMetadata",
                TypeInfo(KeyMetadata),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Metadata associated with the CMK.
    key_metadata: "KeyMetadata" = dataclasses.field(default=ShapeBase.NOT_SET, )


class DataKeySpec(str):
    AES_256 = "AES_256"
    AES_128 = "AES_128"


@dataclasses.dataclass
class DecryptRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "ciphertext_blob",
                "CiphertextBlob",
                TypeInfo(typing.Any),
            ),
            (
                "encryption_context",
                "EncryptionContext",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "grant_tokens",
                "GrantTokens",
                TypeInfo(typing.List[str]),
            ),
        ]

    # Ciphertext to be decrypted. The blob includes metadata.
    ciphertext_blob: typing.Any = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The encryption context. If this was specified in the Encrypt function, it
    # must be specified here or the decryption operation will fail. For more
    # information, see [Encryption
    # Context](http://docs.aws.amazon.com/kms/latest/developerguide/encryption-
    # context.html).
    encryption_context: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A list of grant tokens.

    # For more information, see [Grant
    # Tokens](http://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#grant_token)
    # in the _AWS Key Management Service Developer Guide_.
    grant_tokens: typing.List[str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class DecryptResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "key_id",
                "KeyId",
                TypeInfo(str),
            ),
            (
                "plaintext",
                "Plaintext",
                TypeInfo(typing.Any),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # ARN of the key used to perform the decryption. This value is returned if no
    # errors are encountered during the operation.
    key_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Decrypted plaintext data. When you use the HTTP API or the AWS CLI, the
    # value is Base64-encoded. Otherwise, it is not encoded.
    plaintext: typing.Any = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DeleteAliasRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "alias_name",
                "AliasName",
                TypeInfo(str),
            ),
        ]

    # The alias to be deleted. The name must start with the word "alias" followed
    # by a forward slash (alias/). Aliases that begin with "alias/aws" are
    # reserved.
    alias_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DeleteImportedKeyMaterialRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "key_id",
                "KeyId",
                TypeInfo(str),
            ),
        ]

    # The identifier of the CMK whose key material to delete. The CMK's `Origin`
    # must be `EXTERNAL`.

    # Specify the key ID or the Amazon Resource Name (ARN) of the CMK.

    # For example:

    #   * Key ID: `1234abcd-12ab-34cd-56ef-1234567890ab`

    #   * Key ARN: `arn:aws:kms:us-east-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab`

    # To get the key ID and key ARN for a CMK, use ListKeys or DescribeKey.
    key_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DependencyTimeoutException(ShapeBase):
    """
    The system timed out while trying to fulfill the request. The request can be
    retried.
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
class DescribeKeyRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "key_id",
                "KeyId",
                TypeInfo(str),
            ),
            (
                "grant_tokens",
                "GrantTokens",
                TypeInfo(typing.List[str]),
            ),
        ]

    # Describes the specified customer master key (CMK).

    # If you specify a predefined AWS alias (an AWS alias with no key ID), KMS
    # associates the alias with an [AWS managed
    # CMK](http://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#master_keys)
    # and returns its `KeyId` and `Arn` in the response.

    # To specify a CMK, use its key ID, Amazon Resource Name (ARN), alias name,
    # or alias ARN. When using an alias name, prefix it with `"alias/"`. To
    # specify a CMK in a different AWS account, you must use the key ARN or alias
    # ARN.

    # For example:

    #   * Key ID: `1234abcd-12ab-34cd-56ef-1234567890ab`

    #   * Key ARN: `arn:aws:kms:us-east-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab`

    #   * Alias name: `alias/ExampleAlias`

    #   * Alias ARN: `arn:aws:kms:us-east-2:111122223333:alias/ExampleAlias`

    # To get the key ID and key ARN for a CMK, use ListKeys or DescribeKey. To
    # get the alias name and alias ARN, use ListAliases.
    key_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A list of grant tokens.

    # For more information, see [Grant
    # Tokens](http://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#grant_token)
    # in the _AWS Key Management Service Developer Guide_.
    grant_tokens: typing.List[str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class DescribeKeyResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "key_metadata",
                "KeyMetadata",
                TypeInfo(KeyMetadata),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Metadata associated with the key.
    key_metadata: "KeyMetadata" = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DisableKeyRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "key_id",
                "KeyId",
                TypeInfo(str),
            ),
        ]

    # A unique identifier for the customer master key (CMK).

    # Specify the key ID or the Amazon Resource Name (ARN) of the CMK.

    # For example:

    #   * Key ID: `1234abcd-12ab-34cd-56ef-1234567890ab`

    #   * Key ARN: `arn:aws:kms:us-east-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab`

    # To get the key ID and key ARN for a CMK, use ListKeys or DescribeKey.
    key_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DisableKeyRotationRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "key_id",
                "KeyId",
                TypeInfo(str),
            ),
        ]

    # A unique identifier for the customer master key (CMK).

    # Specify the key ID or the Amazon Resource Name (ARN) of the CMK.

    # For example:

    #   * Key ID: `1234abcd-12ab-34cd-56ef-1234567890ab`

    #   * Key ARN: `arn:aws:kms:us-east-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab`

    # To get the key ID and key ARN for a CMK, use ListKeys or DescribeKey.
    key_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DisabledException(ShapeBase):
    """
    The request was rejected because the specified CMK is not enabled.
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
class EnableKeyRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "key_id",
                "KeyId",
                TypeInfo(str),
            ),
        ]

    # A unique identifier for the customer master key (CMK).

    # Specify the key ID or the Amazon Resource Name (ARN) of the CMK.

    # For example:

    #   * Key ID: `1234abcd-12ab-34cd-56ef-1234567890ab`

    #   * Key ARN: `arn:aws:kms:us-east-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab`

    # To get the key ID and key ARN for a CMK, use ListKeys or DescribeKey.
    key_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class EnableKeyRotationRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "key_id",
                "KeyId",
                TypeInfo(str),
            ),
        ]

    # A unique identifier for the customer master key (CMK).

    # Specify the key ID or the Amazon Resource Name (ARN) of the CMK.

    # For example:

    #   * Key ID: `1234abcd-12ab-34cd-56ef-1234567890ab`

    #   * Key ARN: `arn:aws:kms:us-east-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab`

    # To get the key ID and key ARN for a CMK, use ListKeys or DescribeKey.
    key_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class EncryptRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "key_id",
                "KeyId",
                TypeInfo(str),
            ),
            (
                "plaintext",
                "Plaintext",
                TypeInfo(typing.Any),
            ),
            (
                "encryption_context",
                "EncryptionContext",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "grant_tokens",
                "GrantTokens",
                TypeInfo(typing.List[str]),
            ),
        ]

    # A unique identifier for the customer master key (CMK).

    # To specify a CMK, use its key ID, Amazon Resource Name (ARN), alias name,
    # or alias ARN. When using an alias name, prefix it with `"alias/"`. To
    # specify a CMK in a different AWS account, you must use the key ARN or alias
    # ARN.

    # For example:

    #   * Key ID: `1234abcd-12ab-34cd-56ef-1234567890ab`

    #   * Key ARN: `arn:aws:kms:us-east-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab`

    #   * Alias name: `alias/ExampleAlias`

    #   * Alias ARN: `arn:aws:kms:us-east-2:111122223333:alias/ExampleAlias`

    # To get the key ID and key ARN for a CMK, use ListKeys or DescribeKey. To
    # get the alias name and alias ARN, use ListAliases.
    key_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Data to be encrypted.
    plaintext: typing.Any = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Name-value pair that specifies the encryption context to be used for
    # authenticated encryption. If used here, the same value must be supplied to
    # the `Decrypt` API or decryption will fail. For more information, see
    # [Encryption
    # Context](http://docs.aws.amazon.com/kms/latest/developerguide/encryption-
    # context.html).
    encryption_context: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A list of grant tokens.

    # For more information, see [Grant
    # Tokens](http://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#grant_token)
    # in the _AWS Key Management Service Developer Guide_.
    grant_tokens: typing.List[str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class EncryptResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "ciphertext_blob",
                "CiphertextBlob",
                TypeInfo(typing.Any),
            ),
            (
                "key_id",
                "KeyId",
                TypeInfo(str),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The encrypted plaintext. When you use the HTTP API or the AWS CLI, the
    # value is Base64-encoded. Otherwise, it is not encoded.
    ciphertext_blob: typing.Any = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The ID of the key used during encryption.
    key_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )


class ExpirationModelType(str):
    KEY_MATERIAL_EXPIRES = "KEY_MATERIAL_EXPIRES"
    KEY_MATERIAL_DOES_NOT_EXPIRE = "KEY_MATERIAL_DOES_NOT_EXPIRE"


@dataclasses.dataclass
class ExpiredImportTokenException(ShapeBase):
    """
    The request was rejected because the provided import token is expired. Use
    GetParametersForImport to get a new import token and public key, use the new
    public key to encrypt the key material, and then try the request again.
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
class GenerateDataKeyRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "key_id",
                "KeyId",
                TypeInfo(str),
            ),
            (
                "encryption_context",
                "EncryptionContext",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "number_of_bytes",
                "NumberOfBytes",
                TypeInfo(int),
            ),
            (
                "key_spec",
                "KeySpec",
                TypeInfo(typing.Union[str, DataKeySpec]),
            ),
            (
                "grant_tokens",
                "GrantTokens",
                TypeInfo(typing.List[str]),
            ),
        ]

    # The identifier of the CMK under which to generate and encrypt the data
    # encryption key.

    # To specify a CMK, use its key ID, Amazon Resource Name (ARN), alias name,
    # or alias ARN. When using an alias name, prefix it with `"alias/"`. To
    # specify a CMK in a different AWS account, you must use the key ARN or alias
    # ARN.

    # For example:

    #   * Key ID: `1234abcd-12ab-34cd-56ef-1234567890ab`

    #   * Key ARN: `arn:aws:kms:us-east-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab`

    #   * Alias name: `alias/ExampleAlias`

    #   * Alias ARN: `arn:aws:kms:us-east-2:111122223333:alias/ExampleAlias`

    # To get the key ID and key ARN for a CMK, use ListKeys or DescribeKey. To
    # get the alias name and alias ARN, use ListAliases.
    key_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A set of key-value pairs that represents additional authenticated data.

    # For more information, see [Encryption
    # Context](http://docs.aws.amazon.com/kms/latest/developerguide/encryption-
    # context.html) in the _AWS Key Management Service Developer Guide_.
    encryption_context: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The length of the data encryption key in bytes. For example, use the value
    # 64 to generate a 512-bit data key (64 bytes is 512 bits). For common key
    # lengths (128-bit and 256-bit symmetric keys), we recommend that you use the
    # `KeySpec` field instead of this one.
    number_of_bytes: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The length of the data encryption key. Use `AES_128` to generate a 128-bit
    # symmetric key, or `AES_256` to generate a 256-bit symmetric key.
    key_spec: typing.Union[str, "DataKeySpec"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A list of grant tokens.

    # For more information, see [Grant
    # Tokens](http://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#grant_token)
    # in the _AWS Key Management Service Developer Guide_.
    grant_tokens: typing.List[str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class GenerateDataKeyResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "ciphertext_blob",
                "CiphertextBlob",
                TypeInfo(typing.Any),
            ),
            (
                "plaintext",
                "Plaintext",
                TypeInfo(typing.Any),
            ),
            (
                "key_id",
                "KeyId",
                TypeInfo(str),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The encrypted data encryption key. When you use the HTTP API or the AWS
    # CLI, the value is Base64-encoded. Otherwise, it is not encoded.
    ciphertext_blob: typing.Any = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The data encryption key. When you use the HTTP API or the AWS CLI, the
    # value is Base64-encoded. Otherwise, it is not encoded. Use this data key
    # for local encryption and decryption, then remove it from memory as soon as
    # possible.
    plaintext: typing.Any = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The identifier of the CMK under which the data encryption key was generated
    # and encrypted.
    key_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class GenerateDataKeyWithoutPlaintextRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "key_id",
                "KeyId",
                TypeInfo(str),
            ),
            (
                "encryption_context",
                "EncryptionContext",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "key_spec",
                "KeySpec",
                TypeInfo(typing.Union[str, DataKeySpec]),
            ),
            (
                "number_of_bytes",
                "NumberOfBytes",
                TypeInfo(int),
            ),
            (
                "grant_tokens",
                "GrantTokens",
                TypeInfo(typing.List[str]),
            ),
        ]

    # The identifier of the customer master key (CMK) under which to generate and
    # encrypt the data encryption key.

    # To specify a CMK, use its key ID, Amazon Resource Name (ARN), alias name,
    # or alias ARN. When using an alias name, prefix it with `"alias/"`. To
    # specify a CMK in a different AWS account, you must use the key ARN or alias
    # ARN.

    # For example:

    #   * Key ID: `1234abcd-12ab-34cd-56ef-1234567890ab`

    #   * Key ARN: `arn:aws:kms:us-east-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab`

    #   * Alias name: `alias/ExampleAlias`

    #   * Alias ARN: `arn:aws:kms:us-east-2:111122223333:alias/ExampleAlias`

    # To get the key ID and key ARN for a CMK, use ListKeys or DescribeKey. To
    # get the alias name and alias ARN, use ListAliases.
    key_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A set of key-value pairs that represents additional authenticated data.

    # For more information, see [Encryption
    # Context](http://docs.aws.amazon.com/kms/latest/developerguide/encryption-
    # context.html) in the _AWS Key Management Service Developer Guide_.
    encryption_context: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The length of the data encryption key. Use `AES_128` to generate a 128-bit
    # symmetric key, or `AES_256` to generate a 256-bit symmetric key.
    key_spec: typing.Union[str, "DataKeySpec"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The length of the data encryption key in bytes. For example, use the value
    # 64 to generate a 512-bit data key (64 bytes is 512 bits). For common key
    # lengths (128-bit and 256-bit symmetric keys), we recommend that you use the
    # `KeySpec` field instead of this one.
    number_of_bytes: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A list of grant tokens.

    # For more information, see [Grant
    # Tokens](http://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#grant_token)
    # in the _AWS Key Management Service Developer Guide_.
    grant_tokens: typing.List[str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class GenerateDataKeyWithoutPlaintextResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "ciphertext_blob",
                "CiphertextBlob",
                TypeInfo(typing.Any),
            ),
            (
                "key_id",
                "KeyId",
                TypeInfo(str),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The encrypted data encryption key. When you use the HTTP API or the AWS
    # CLI, the value is Base64-encoded. Otherwise, it is not encoded.
    ciphertext_blob: typing.Any = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The identifier of the CMK under which the data encryption key was generated
    # and encrypted.
    key_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class GenerateRandomRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "number_of_bytes",
                "NumberOfBytes",
                TypeInfo(int),
            ),
        ]

    # The length of the byte string.
    number_of_bytes: int = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class GenerateRandomResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "plaintext",
                "Plaintext",
                TypeInfo(typing.Any),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The random byte string. When you use the HTTP API or the AWS CLI, the value
    # is Base64-encoded. Otherwise, it is not encoded.
    plaintext: typing.Any = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class GetKeyPolicyRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "key_id",
                "KeyId",
                TypeInfo(str),
            ),
            (
                "policy_name",
                "PolicyName",
                TypeInfo(str),
            ),
        ]

    # A unique identifier for the customer master key (CMK).

    # Specify the key ID or the Amazon Resource Name (ARN) of the CMK.

    # For example:

    #   * Key ID: `1234abcd-12ab-34cd-56ef-1234567890ab`

    #   * Key ARN: `arn:aws:kms:us-east-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab`

    # To get the key ID and key ARN for a CMK, use ListKeys or DescribeKey.
    key_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Specifies the name of the key policy. The only valid name is `default`. To
    # get the names of key policies, use ListKeyPolicies.
    policy_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class GetKeyPolicyResponse(OutputShapeBase):
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
                TypeInfo(str),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A key policy document in JSON format.
    policy: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class GetKeyRotationStatusRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "key_id",
                "KeyId",
                TypeInfo(str),
            ),
        ]

    # A unique identifier for the customer master key (CMK).

    # Specify the key ID or the Amazon Resource Name (ARN) of the CMK. To specify
    # a CMK in a different AWS account, you must use the key ARN.

    # For example:

    #   * Key ID: `1234abcd-12ab-34cd-56ef-1234567890ab`

    #   * Key ARN: `arn:aws:kms:us-east-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab`

    # To get the key ID and key ARN for a CMK, use ListKeys or DescribeKey.
    key_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class GetKeyRotationStatusResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "key_rotation_enabled",
                "KeyRotationEnabled",
                TypeInfo(bool),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A Boolean value that specifies whether key rotation is enabled.
    key_rotation_enabled: bool = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class GetParametersForImportRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "key_id",
                "KeyId",
                TypeInfo(str),
            ),
            (
                "wrapping_algorithm",
                "WrappingAlgorithm",
                TypeInfo(typing.Union[str, AlgorithmSpec]),
            ),
            (
                "wrapping_key_spec",
                "WrappingKeySpec",
                TypeInfo(typing.Union[str, WrappingKeySpec]),
            ),
        ]

    # The identifier of the CMK into which you will import key material. The
    # CMK's `Origin` must be `EXTERNAL`.

    # Specify the key ID or the Amazon Resource Name (ARN) of the CMK.

    # For example:

    #   * Key ID: `1234abcd-12ab-34cd-56ef-1234567890ab`

    #   * Key ARN: `arn:aws:kms:us-east-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab`

    # To get the key ID and key ARN for a CMK, use ListKeys or DescribeKey.
    key_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The algorithm you use to encrypt the key material before importing it with
    # ImportKeyMaterial. For more information, see [Encrypt the Key
    # Material](http://docs.aws.amazon.com/kms/latest/developerguide/importing-
    # keys-encrypt-key-material.html) in the _AWS Key Management Service
    # Developer Guide_.
    wrapping_algorithm: typing.Union[str, "AlgorithmSpec"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The type of wrapping key (public key) to return in the response. Only
    # 2048-bit RSA public keys are supported.
    wrapping_key_spec: typing.Union[str, "WrappingKeySpec"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class GetParametersForImportResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "key_id",
                "KeyId",
                TypeInfo(str),
            ),
            (
                "import_token",
                "ImportToken",
                TypeInfo(typing.Any),
            ),
            (
                "public_key",
                "PublicKey",
                TypeInfo(typing.Any),
            ),
            (
                "parameters_valid_to",
                "ParametersValidTo",
                TypeInfo(datetime.datetime),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The identifier of the CMK to use in a subsequent ImportKeyMaterial request.
    # This is the same CMK specified in the `GetParametersForImport` request.
    key_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The import token to send in a subsequent ImportKeyMaterial request.
    import_token: typing.Any = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The public key to use to encrypt the key material before importing it with
    # ImportKeyMaterial.
    public_key: typing.Any = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The time at which the import token and public key are no longer valid.
    # After this time, you cannot use them to make an ImportKeyMaterial request
    # and you must send another `GetParametersForImport` request to get new ones.
    parameters_valid_to: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class GrantConstraints(ShapeBase):
    """
    A structure that you can use to allow certain operations in the grant only when
    the preferred encryption context is present. For more information about
    encryption context, see [Encryption
    Context](http://docs.aws.amazon.com/kms/latest/developerguide/encryption-
    context.html) in the _AWS Key Management Service Developer Guide_.

    Grant constraints apply only to operations that accept encryption context as
    input. For example, the ` DescribeKey ` operation does not accept encryption
    context as input. A grant that allows the `DescribeKey` operation does so
    regardless of the grant constraints. In contrast, the ` Encrypt ` operation
    accepts encryption context as input. A grant that allows the `Encrypt` operation
    does so only when the encryption context of the `Encrypt` operation satisfies
    the grant constraints.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "encryption_context_subset",
                "EncryptionContextSubset",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "encryption_context_equals",
                "EncryptionContextEquals",
                TypeInfo(typing.Dict[str, str]),
            ),
        ]

    # A list of key-value pairs, all of which must be present in the encryption
    # context of certain subsequent operations that the grant allows. When
    # certain subsequent operations allowed by the grant include encryption
    # context that matches this list or is a superset of this list, the grant
    # allows the operation. Otherwise, the grant does not allow the operation.
    encryption_context_subset: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A list of key-value pairs that must be present in the encryption context of
    # certain subsequent operations that the grant allows. When certain
    # subsequent operations allowed by the grant include encryption context that
    # matches this list, the grant allows the operation. Otherwise, the grant
    # does not allow the operation.
    encryption_context_equals: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class GrantListEntry(ShapeBase):
    """
    Contains information about an entry in a list of grants.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "key_id",
                "KeyId",
                TypeInfo(str),
            ),
            (
                "grant_id",
                "GrantId",
                TypeInfo(str),
            ),
            (
                "name",
                "Name",
                TypeInfo(str),
            ),
            (
                "creation_date",
                "CreationDate",
                TypeInfo(datetime.datetime),
            ),
            (
                "grantee_principal",
                "GranteePrincipal",
                TypeInfo(str),
            ),
            (
                "retiring_principal",
                "RetiringPrincipal",
                TypeInfo(str),
            ),
            (
                "issuing_account",
                "IssuingAccount",
                TypeInfo(str),
            ),
            (
                "operations",
                "Operations",
                TypeInfo(typing.List[typing.Union[str, GrantOperation]]),
            ),
            (
                "constraints",
                "Constraints",
                TypeInfo(GrantConstraints),
            ),
        ]

    # The unique identifier for the customer master key (CMK) to which the grant
    # applies.
    key_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The unique identifier for the grant.
    grant_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The friendly name that identifies the grant. If a name was provided in the
    # CreateGrant request, that name is returned. Otherwise this value is null.
    name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The date and time when the grant was created.
    creation_date: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The principal that receives the grant's permissions.
    grantee_principal: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The principal that can retire the grant.
    retiring_principal: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The AWS account under which the grant was issued.
    issuing_account: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The list of operations permitted by the grant.
    operations: typing.List[typing.Union[str, "GrantOperation"]
                           ] = dataclasses.field(
                               default=ShapeBase.NOT_SET,
                           )

    # A list of key-value pairs that must be present in the encryption context of
    # certain subsequent operations that the grant allows.
    constraints: "GrantConstraints" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


class GrantOperation(str):
    Decrypt = "Decrypt"
    Encrypt = "Encrypt"
    GenerateDataKey = "GenerateDataKey"
    GenerateDataKeyWithoutPlaintext = "GenerateDataKeyWithoutPlaintext"
    ReEncryptFrom = "ReEncryptFrom"
    ReEncryptTo = "ReEncryptTo"
    CreateGrant = "CreateGrant"
    RetireGrant = "RetireGrant"
    DescribeKey = "DescribeKey"


@dataclasses.dataclass
class ImportKeyMaterialRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "key_id",
                "KeyId",
                TypeInfo(str),
            ),
            (
                "import_token",
                "ImportToken",
                TypeInfo(typing.Any),
            ),
            (
                "encrypted_key_material",
                "EncryptedKeyMaterial",
                TypeInfo(typing.Any),
            ),
            (
                "valid_to",
                "ValidTo",
                TypeInfo(datetime.datetime),
            ),
            (
                "expiration_model",
                "ExpirationModel",
                TypeInfo(typing.Union[str, ExpirationModelType]),
            ),
        ]

    # The identifier of the CMK to import the key material into. The CMK's
    # `Origin` must be `EXTERNAL`.

    # Specify the key ID or the Amazon Resource Name (ARN) of the CMK.

    # For example:

    #   * Key ID: `1234abcd-12ab-34cd-56ef-1234567890ab`

    #   * Key ARN: `arn:aws:kms:us-east-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab`

    # To get the key ID and key ARN for a CMK, use ListKeys or DescribeKey.
    key_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The import token that you received in the response to a previous
    # GetParametersForImport request. It must be from the same response that
    # contained the public key that you used to encrypt the key material.
    import_token: typing.Any = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The encrypted key material to import. It must be encrypted with the public
    # key that you received in the response to a previous GetParametersForImport
    # request, using the wrapping algorithm that you specified in that request.
    encrypted_key_material: typing.Any = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The time at which the imported key material expires. When the key material
    # expires, AWS KMS deletes the key material and the CMK becomes unusable. You
    # must omit this parameter when the `ExpirationModel` parameter is set to
    # `KEY_MATERIAL_DOES_NOT_EXPIRE`. Otherwise it is required.
    valid_to: datetime.datetime = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Specifies whether the key material expires. The default is
    # `KEY_MATERIAL_EXPIRES`, in which case you must include the `ValidTo`
    # parameter. When this parameter is set to `KEY_MATERIAL_DOES_NOT_EXPIRE`,
    # you must omit the `ValidTo` parameter.
    expiration_model: typing.Union[str, "ExpirationModelType"
                                  ] = dataclasses.field(
                                      default=ShapeBase.NOT_SET,
                                  )


@dataclasses.dataclass
class ImportKeyMaterialResponse(OutputShapeBase):
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
class IncorrectKeyMaterialException(ShapeBase):
    """
    The request was rejected because the provided key material is invalid or is not
    the same key material that was previously imported into this customer master key
    (CMK).
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
class InvalidAliasNameException(ShapeBase):
    """
    The request was rejected because the specified alias name is not valid.
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
class InvalidArnException(ShapeBase):
    """
    The request was rejected because a specified ARN was not valid.
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
class InvalidCiphertextException(ShapeBase):
    """
    The request was rejected because the specified ciphertext, or additional
    authenticated data incorporated into the ciphertext, such as the encryption
    context, is corrupted, missing, or otherwise invalid.
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
class InvalidGrantIdException(ShapeBase):
    """
    The request was rejected because the specified `GrantId` is not valid.
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
class InvalidGrantTokenException(ShapeBase):
    """
    The request was rejected because the specified grant token is not valid.
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
class InvalidImportTokenException(ShapeBase):
    """
    The request was rejected because the provided import token is invalid or is
    associated with a different customer master key (CMK).
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
class InvalidKeyUsageException(ShapeBase):
    """
    The request was rejected because the specified `KeySpec` value is not valid.
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
class InvalidMarkerException(ShapeBase):
    """
    The request was rejected because the marker that specifies where pagination
    should next begin is not valid.
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
class KMSInternalException(ShapeBase):
    """
    The request was rejected because an internal exception occurred. The request can
    be retried.
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
class KMSInvalidStateException(ShapeBase):
    """
    The request was rejected because the state of the specified resource is not
    valid for this request.

    For more information about how key state affects the use of a CMK, see [How Key
    State Affects Use of a Customer Master
    Key](http://docs.aws.amazon.com/kms/latest/developerguide/key-state.html) in the
    _AWS Key Management Service Developer Guide_.
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
class KeyListEntry(ShapeBase):
    """
    Contains information about each entry in the key list.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "key_id",
                "KeyId",
                TypeInfo(str),
            ),
            (
                "key_arn",
                "KeyArn",
                TypeInfo(str),
            ),
        ]

    # Unique identifier of the key.
    key_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # ARN of the key.
    key_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )


class KeyManagerType(str):
    AWS = "AWS"
    CUSTOMER = "CUSTOMER"


@dataclasses.dataclass
class KeyMetadata(ShapeBase):
    """
    Contains metadata about a customer master key (CMK).

    This data type is used as a response element for the CreateKey and DescribeKey
    operations.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "key_id",
                "KeyId",
                TypeInfo(str),
            ),
            (
                "aws_account_id",
                "AWSAccountId",
                TypeInfo(str),
            ),
            (
                "arn",
                "Arn",
                TypeInfo(str),
            ),
            (
                "creation_date",
                "CreationDate",
                TypeInfo(datetime.datetime),
            ),
            (
                "enabled",
                "Enabled",
                TypeInfo(bool),
            ),
            (
                "description",
                "Description",
                TypeInfo(str),
            ),
            (
                "key_usage",
                "KeyUsage",
                TypeInfo(typing.Union[str, KeyUsageType]),
            ),
            (
                "key_state",
                "KeyState",
                TypeInfo(typing.Union[str, KeyState]),
            ),
            (
                "deletion_date",
                "DeletionDate",
                TypeInfo(datetime.datetime),
            ),
            (
                "valid_to",
                "ValidTo",
                TypeInfo(datetime.datetime),
            ),
            (
                "origin",
                "Origin",
                TypeInfo(typing.Union[str, OriginType]),
            ),
            (
                "expiration_model",
                "ExpirationModel",
                TypeInfo(typing.Union[str, ExpirationModelType]),
            ),
            (
                "key_manager",
                "KeyManager",
                TypeInfo(typing.Union[str, KeyManagerType]),
            ),
        ]

    # The globally unique identifier for the CMK.
    key_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The twelve-digit account ID of the AWS account that owns the CMK.
    aws_account_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The Amazon Resource Name (ARN) of the CMK. For examples, see [AWS Key
    # Management Service (AWS
    # KMS)](http://docs.aws.amazon.com/general/latest/gr/aws-arns-and-
    # namespaces.html#arn-syntax-kms) in the Example ARNs section of the _AWS
    # General Reference_.
    arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The date and time when the CMK was created.
    creation_date: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Specifies whether the CMK is enabled. When `KeyState` is `Enabled` this
    # value is true, otherwise it is false.
    enabled: bool = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The description of the CMK.
    description: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The cryptographic operations for which you can use the CMK. Currently the
    # only allowed value is `ENCRYPT_DECRYPT`, which means you can use the CMK
    # for the Encrypt and Decrypt operations.
    key_usage: typing.Union[str, "KeyUsageType"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The state of the CMK.

    # For more information about how key state affects the use of a CMK, see [How
    # Key State Affects the Use of a Customer Master
    # Key](http://docs.aws.amazon.com/kms/latest/developerguide/key-state.html)
    # in the _AWS Key Management Service Developer Guide_.
    key_state: typing.Union[str, "KeyState"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The date and time after which AWS KMS deletes the CMK. This value is
    # present only when `KeyState` is `PendingDeletion`, otherwise this value is
    # omitted.
    deletion_date: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The time at which the imported key material expires. When the key material
    # expires, AWS KMS deletes the key material and the CMK becomes unusable.
    # This value is present only for CMKs whose `Origin` is `EXTERNAL` and whose
    # `ExpirationModel` is `KEY_MATERIAL_EXPIRES`, otherwise this value is
    # omitted.
    valid_to: datetime.datetime = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The source of the CMK's key material. When this value is `AWS_KMS`, AWS KMS
    # created the key material. When this value is `EXTERNAL`, the key material
    # was imported from your existing key management infrastructure or the CMK
    # lacks key material.
    origin: typing.Union[str, "OriginType"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Specifies whether the CMK's key material expires. This value is present
    # only when `Origin` is `EXTERNAL`, otherwise this value is omitted.
    expiration_model: typing.Union[str, "ExpirationModelType"
                                  ] = dataclasses.field(
                                      default=ShapeBase.NOT_SET,
                                  )

    # The CMK's manager. CMKs are either customer managed or AWS managed. For
    # more information about the difference, see [Customer Master
    # Keys](http://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#master_keys)
    # in the _AWS Key Management Service Developer Guide_.
    key_manager: typing.Union[str, "KeyManagerType"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


class KeyState(str):
    Enabled = "Enabled"
    Disabled = "Disabled"
    PendingDeletion = "PendingDeletion"
    PendingImport = "PendingImport"


@dataclasses.dataclass
class KeyUnavailableException(ShapeBase):
    """
    The request was rejected because the specified CMK was not available. The
    request can be retried.
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


class KeyUsageType(str):
    ENCRYPT_DECRYPT = "ENCRYPT_DECRYPT"


@dataclasses.dataclass
class LimitExceededException(ShapeBase):
    """
    The request was rejected because a limit was exceeded. For more information, see
    [Limits](http://docs.aws.amazon.com/kms/latest/developerguide/limits.html) in
    the _AWS Key Management Service Developer Guide_.
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
class ListAliasesRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "key_id",
                "KeyId",
                TypeInfo(str),
            ),
            (
                "limit",
                "Limit",
                TypeInfo(int),
            ),
            (
                "marker",
                "Marker",
                TypeInfo(str),
            ),
        ]

    # Lists only aliases that refer to the specified CMK. The value of this
    # parameter can be the ID or Amazon Resource Name (ARN) of a CMK in the
    # caller's account and region. You cannot use an alias name or alias ARN in
    # this value.

    # This parameter is optional. If you omit it, `ListAliases` returns all
    # aliases in the account and region.
    key_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Use this parameter to specify the maximum number of items to return. When
    # this value is present, AWS KMS does not return more than the specified
    # number of items, but it might return fewer.

    # This value is optional. If you include a value, it must be between 1 and
    # 100, inclusive. If you do not include a value, it defaults to 50.
    limit: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Use this parameter in a subsequent request after you receive a response
    # with truncated results. Set it to the value of `NextMarker` from the
    # truncated response you just received.
    marker: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ListAliasesResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "aliases",
                "Aliases",
                TypeInfo(typing.List[AliasListEntry]),
            ),
            (
                "next_marker",
                "NextMarker",
                TypeInfo(str),
            ),
            (
                "truncated",
                "Truncated",
                TypeInfo(bool),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A list of aliases.
    aliases: typing.List["AliasListEntry"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # When `Truncated` is true, this element is present and contains the value to
    # use for the `Marker` parameter in a subsequent request.
    next_marker: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A flag that indicates whether there are more items in the list. When this
    # value is true, the list in this response is truncated. To get more items,
    # pass the value of the `NextMarker` element in this response to the `Marker`
    # parameter in a subsequent request.
    truncated: bool = dataclasses.field(default=ShapeBase.NOT_SET, )

    def paginate(self, ) -> typing.Generator["ListAliasesResponse", None, None]:
        yield from super()._paginate()


@dataclasses.dataclass
class ListGrantsRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "key_id",
                "KeyId",
                TypeInfo(str),
            ),
            (
                "limit",
                "Limit",
                TypeInfo(int),
            ),
            (
                "marker",
                "Marker",
                TypeInfo(str),
            ),
        ]

    # A unique identifier for the customer master key (CMK).

    # Specify the key ID or the Amazon Resource Name (ARN) of the CMK. To specify
    # a CMK in a different AWS account, you must use the key ARN.

    # For example:

    #   * Key ID: `1234abcd-12ab-34cd-56ef-1234567890ab`

    #   * Key ARN: `arn:aws:kms:us-east-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab`

    # To get the key ID and key ARN for a CMK, use ListKeys or DescribeKey.
    key_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Use this parameter to specify the maximum number of items to return. When
    # this value is present, AWS KMS does not return more than the specified
    # number of items, but it might return fewer.

    # This value is optional. If you include a value, it must be between 1 and
    # 100, inclusive. If you do not include a value, it defaults to 50.
    limit: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Use this parameter in a subsequent request after you receive a response
    # with truncated results. Set it to the value of `NextMarker` from the
    # truncated response you just received.
    marker: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ListGrantsResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "grants",
                "Grants",
                TypeInfo(typing.List[GrantListEntry]),
            ),
            (
                "next_marker",
                "NextMarker",
                TypeInfo(str),
            ),
            (
                "truncated",
                "Truncated",
                TypeInfo(bool),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A list of grants.
    grants: typing.List["GrantListEntry"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # When `Truncated` is true, this element is present and contains the value to
    # use for the `Marker` parameter in a subsequent request.
    next_marker: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A flag that indicates whether there are more items in the list. When this
    # value is true, the list in this response is truncated. To get more items,
    # pass the value of the `NextMarker` element in this response to the `Marker`
    # parameter in a subsequent request.
    truncated: bool = dataclasses.field(default=ShapeBase.NOT_SET, )

    def paginate(self, ) -> typing.Generator["ListGrantsResponse", None, None]:
        yield from super()._paginate()


@dataclasses.dataclass
class ListKeyPoliciesRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "key_id",
                "KeyId",
                TypeInfo(str),
            ),
            (
                "limit",
                "Limit",
                TypeInfo(int),
            ),
            (
                "marker",
                "Marker",
                TypeInfo(str),
            ),
        ]

    # A unique identifier for the customer master key (CMK).

    # Specify the key ID or the Amazon Resource Name (ARN) of the CMK.

    # For example:

    #   * Key ID: `1234abcd-12ab-34cd-56ef-1234567890ab`

    #   * Key ARN: `arn:aws:kms:us-east-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab`

    # To get the key ID and key ARN for a CMK, use ListKeys or DescribeKey.
    key_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Use this parameter to specify the maximum number of items to return. When
    # this value is present, AWS KMS does not return more than the specified
    # number of items, but it might return fewer.

    # This value is optional. If you include a value, it must be between 1 and
    # 1000, inclusive. If you do not include a value, it defaults to 100.

    # Currently only 1 policy can be attached to a key.
    limit: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Use this parameter in a subsequent request after you receive a response
    # with truncated results. Set it to the value of `NextMarker` from the
    # truncated response you just received.
    marker: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ListKeyPoliciesResponse(OutputShapeBase):
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
                "next_marker",
                "NextMarker",
                TypeInfo(str),
            ),
            (
                "truncated",
                "Truncated",
                TypeInfo(bool),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A list of key policy names. Currently, there is only one key policy per CMK
    # and it is always named `default`.
    policy_names: typing.List[str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # When `Truncated` is true, this element is present and contains the value to
    # use for the `Marker` parameter in a subsequent request.
    next_marker: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A flag that indicates whether there are more items in the list. When this
    # value is true, the list in this response is truncated. To get more items,
    # pass the value of the `NextMarker` element in this response to the `Marker`
    # parameter in a subsequent request.
    truncated: bool = dataclasses.field(default=ShapeBase.NOT_SET, )

    def paginate(self,
                ) -> typing.Generator["ListKeyPoliciesResponse", None, None]:
        yield from super()._paginate()


@dataclasses.dataclass
class ListKeysRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "limit",
                "Limit",
                TypeInfo(int),
            ),
            (
                "marker",
                "Marker",
                TypeInfo(str),
            ),
        ]

    # Use this parameter to specify the maximum number of items to return. When
    # this value is present, AWS KMS does not return more than the specified
    # number of items, but it might return fewer.

    # This value is optional. If you include a value, it must be between 1 and
    # 1000, inclusive. If you do not include a value, it defaults to 100.
    limit: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Use this parameter in a subsequent request after you receive a response
    # with truncated results. Set it to the value of `NextMarker` from the
    # truncated response you just received.
    marker: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ListKeysResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "keys",
                "Keys",
                TypeInfo(typing.List[KeyListEntry]),
            ),
            (
                "next_marker",
                "NextMarker",
                TypeInfo(str),
            ),
            (
                "truncated",
                "Truncated",
                TypeInfo(bool),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A list of customer master keys (CMKs).
    keys: typing.List["KeyListEntry"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # When `Truncated` is true, this element is present and contains the value to
    # use for the `Marker` parameter in a subsequent request.
    next_marker: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A flag that indicates whether there are more items in the list. When this
    # value is true, the list in this response is truncated. To get more items,
    # pass the value of the `NextMarker` element in this response to the `Marker`
    # parameter in a subsequent request.
    truncated: bool = dataclasses.field(default=ShapeBase.NOT_SET, )

    def paginate(self, ) -> typing.Generator["ListKeysResponse", None, None]:
        yield from super()._paginate()


@dataclasses.dataclass
class ListResourceTagsRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "key_id",
                "KeyId",
                TypeInfo(str),
            ),
            (
                "limit",
                "Limit",
                TypeInfo(int),
            ),
            (
                "marker",
                "Marker",
                TypeInfo(str),
            ),
        ]

    # A unique identifier for the customer master key (CMK).

    # Specify the key ID or the Amazon Resource Name (ARN) of the CMK.

    # For example:

    #   * Key ID: `1234abcd-12ab-34cd-56ef-1234567890ab`

    #   * Key ARN: `arn:aws:kms:us-east-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab`

    # To get the key ID and key ARN for a CMK, use ListKeys or DescribeKey.
    key_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Use this parameter to specify the maximum number of items to return. When
    # this value is present, AWS KMS does not return more than the specified
    # number of items, but it might return fewer.

    # This value is optional. If you include a value, it must be between 1 and
    # 50, inclusive. If you do not include a value, it defaults to 50.
    limit: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Use this parameter in a subsequent request after you receive a response
    # with truncated results. Set it to the value of `NextMarker` from the
    # truncated response you just received.

    # Do not attempt to construct this value. Use only the value of `NextMarker`
    # from the truncated response you just received.
    marker: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ListResourceTagsResponse(OutputShapeBase):
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
                "next_marker",
                "NextMarker",
                TypeInfo(str),
            ),
            (
                "truncated",
                "Truncated",
                TypeInfo(bool),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A list of tags. Each tag consists of a tag key and a tag value.
    tags: typing.List["Tag"] = dataclasses.field(default=ShapeBase.NOT_SET, )

    # When `Truncated` is true, this element is present and contains the value to
    # use for the `Marker` parameter in a subsequent request.

    # Do not assume or infer any information from this value.
    next_marker: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A flag that indicates whether there are more items in the list. When this
    # value is true, the list in this response is truncated. To get more items,
    # pass the value of the `NextMarker` element in this response to the `Marker`
    # parameter in a subsequent request.
    truncated: bool = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ListRetirableGrantsRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "retiring_principal",
                "RetiringPrincipal",
                TypeInfo(str),
            ),
            (
                "limit",
                "Limit",
                TypeInfo(int),
            ),
            (
                "marker",
                "Marker",
                TypeInfo(str),
            ),
        ]

    # The retiring principal for which to list grants.

    # To specify the retiring principal, use the [Amazon Resource Name
    # (ARN)](http://docs.aws.amazon.com/general/latest/gr/aws-arns-and-
    # namespaces.html) of an AWS principal. Valid AWS principals include AWS
    # accounts (root), IAM users, federated users, and assumed role users. For
    # examples of the ARN syntax for specifying a principal, see [AWS Identity
    # and Access Management
    # (IAM)](http://docs.aws.amazon.com/general/latest/gr/aws-arns-and-
    # namespaces.html#arn-syntax-iam) in the Example ARNs section of the _Amazon
    # Web Services General Reference_.
    retiring_principal: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Use this parameter to specify the maximum number of items to return. When
    # this value is present, AWS KMS does not return more than the specified
    # number of items, but it might return fewer.

    # This value is optional. If you include a value, it must be between 1 and
    # 100, inclusive. If you do not include a value, it defaults to 50.
    limit: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Use this parameter in a subsequent request after you receive a response
    # with truncated results. Set it to the value of `NextMarker` from the
    # truncated response you just received.
    marker: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class MalformedPolicyDocumentException(ShapeBase):
    """
    The request was rejected because the specified policy is not syntactically or
    semantically correct.
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
class NotFoundException(ShapeBase):
    """
    The request was rejected because the specified entity or resource could not be
    found.
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


class OriginType(str):
    AWS_KMS = "AWS_KMS"
    EXTERNAL = "EXTERNAL"


class PlaintextType(botocore.response.StreamingBody):
    pass


@dataclasses.dataclass
class PutKeyPolicyRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "key_id",
                "KeyId",
                TypeInfo(str),
            ),
            (
                "policy_name",
                "PolicyName",
                TypeInfo(str),
            ),
            (
                "policy",
                "Policy",
                TypeInfo(str),
            ),
            (
                "bypass_policy_lockout_safety_check",
                "BypassPolicyLockoutSafetyCheck",
                TypeInfo(bool),
            ),
        ]

    # A unique identifier for the customer master key (CMK).

    # Specify the key ID or the Amazon Resource Name (ARN) of the CMK.

    # For example:

    #   * Key ID: `1234abcd-12ab-34cd-56ef-1234567890ab`

    #   * Key ARN: `arn:aws:kms:us-east-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab`

    # To get the key ID and key ARN for a CMK, use ListKeys or DescribeKey.
    key_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The name of the key policy. The only valid value is `default`.
    policy_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The key policy to attach to the CMK.

    # The key policy must meet the following criteria:

    #   * If you don't set `BypassPolicyLockoutSafetyCheck` to true, the key policy must allow the principal that is making the `PutKeyPolicy` request to make a subsequent `PutKeyPolicy` request on the CMK. This reduces the risk that the CMK becomes unmanageable. For more information, refer to the scenario in the [Default Key Policy](http://docs.aws.amazon.com/kms/latest/developerguide/key-policies.html#key-policy-default-allow-root-enable-iam) section of the _AWS Key Management Service Developer Guide_.

    #   * Each statement in the key policy must contain one or more principals. The principals in the key policy must exist and be visible to AWS KMS. When you create a new AWS principal (for example, an IAM user or role), you might need to enforce a delay before including the new principal in a key policy. The reason for this is that the new principal might not be immediately visible to AWS KMS. For more information, see [Changes that I make are not always immediately visible](http://docs.aws.amazon.com/IAM/latest/UserGuide/troubleshoot_general.html#troubleshoot_general_eventual-consistency) in the _AWS Identity and Access Management User Guide_.

    # The key policy size limit is 32 kilobytes (32768 bytes).
    policy: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A flag to indicate whether to bypass the key policy lockout safety check.

    # Setting this value to true increases the risk that the CMK becomes
    # unmanageable. Do not set this value to true indiscriminately.

    # For more information, refer to the scenario in the [Default Key
    # Policy](http://docs.aws.amazon.com/kms/latest/developerguide/key-
    # policies.html#key-policy-default-allow-root-enable-iam) section in the _AWS
    # Key Management Service Developer Guide_.

    # Use this parameter only when you intend to prevent the principal that is
    # making the request from making a subsequent `PutKeyPolicy` request on the
    # CMK.

    # The default value is false.
    bypass_policy_lockout_safety_check: bool = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class ReEncryptRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "ciphertext_blob",
                "CiphertextBlob",
                TypeInfo(typing.Any),
            ),
            (
                "destination_key_id",
                "DestinationKeyId",
                TypeInfo(str),
            ),
            (
                "source_encryption_context",
                "SourceEncryptionContext",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "destination_encryption_context",
                "DestinationEncryptionContext",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "grant_tokens",
                "GrantTokens",
                TypeInfo(typing.List[str]),
            ),
        ]

    # Ciphertext of the data to reencrypt.
    ciphertext_blob: typing.Any = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A unique identifier for the CMK that is used to reencrypt the data.

    # To specify a CMK, use its key ID, Amazon Resource Name (ARN), alias name,
    # or alias ARN. When using an alias name, prefix it with `"alias/"`. To
    # specify a CMK in a different AWS account, you must use the key ARN or alias
    # ARN.

    # For example:

    #   * Key ID: `1234abcd-12ab-34cd-56ef-1234567890ab`

    #   * Key ARN: `arn:aws:kms:us-east-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab`

    #   * Alias name: `alias/ExampleAlias`

    #   * Alias ARN: `arn:aws:kms:us-east-2:111122223333:alias/ExampleAlias`

    # To get the key ID and key ARN for a CMK, use ListKeys or DescribeKey. To
    # get the alias name and alias ARN, use ListAliases.
    destination_key_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Encryption context used to encrypt and decrypt the data specified in the
    # `CiphertextBlob` parameter.
    source_encryption_context: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Encryption context to use when the data is reencrypted.
    destination_encryption_context: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A list of grant tokens.

    # For more information, see [Grant
    # Tokens](http://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#grant_token)
    # in the _AWS Key Management Service Developer Guide_.
    grant_tokens: typing.List[str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class ReEncryptResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "ciphertext_blob",
                "CiphertextBlob",
                TypeInfo(typing.Any),
            ),
            (
                "source_key_id",
                "SourceKeyId",
                TypeInfo(str),
            ),
            (
                "key_id",
                "KeyId",
                TypeInfo(str),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The reencrypted data. When you use the HTTP API or the AWS CLI, the value
    # is Base64-encoded. Otherwise, it is not encoded.
    ciphertext_blob: typing.Any = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Unique identifier of the CMK used to originally encrypt the data.
    source_key_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Unique identifier of the CMK used to reencrypt the data.
    key_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class RetireGrantRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "grant_token",
                "GrantToken",
                TypeInfo(str),
            ),
            (
                "key_id",
                "KeyId",
                TypeInfo(str),
            ),
            (
                "grant_id",
                "GrantId",
                TypeInfo(str),
            ),
        ]

    # Token that identifies the grant to be retired.
    grant_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The Amazon Resource Name (ARN) of the CMK associated with the grant.

    # For example: `arn:aws:kms:us-
    # east-2:444455556666:key/1234abcd-12ab-34cd-56ef-1234567890ab`
    key_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Unique identifier of the grant to retire. The grant ID is returned in the
    # response to a `CreateGrant` operation.

    #   * Grant ID Example - 0123456789012345678901234567890123456789012345678901234567890123
    grant_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class RevokeGrantRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "key_id",
                "KeyId",
                TypeInfo(str),
            ),
            (
                "grant_id",
                "GrantId",
                TypeInfo(str),
            ),
        ]

    # A unique identifier for the customer master key associated with the grant.

    # Specify the key ID or the Amazon Resource Name (ARN) of the CMK. To specify
    # a CMK in a different AWS account, you must use the key ARN.

    # For example:

    #   * Key ID: `1234abcd-12ab-34cd-56ef-1234567890ab`

    #   * Key ARN: `arn:aws:kms:us-east-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab`

    # To get the key ID and key ARN for a CMK, use ListKeys or DescribeKey.
    key_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Identifier of the grant to be revoked.
    grant_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ScheduleKeyDeletionRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "key_id",
                "KeyId",
                TypeInfo(str),
            ),
            (
                "pending_window_in_days",
                "PendingWindowInDays",
                TypeInfo(int),
            ),
        ]

    # The unique identifier of the customer master key (CMK) to delete.

    # Specify the key ID or the Amazon Resource Name (ARN) of the CMK.

    # For example:

    #   * Key ID: `1234abcd-12ab-34cd-56ef-1234567890ab`

    #   * Key ARN: `arn:aws:kms:us-east-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab`

    # To get the key ID and key ARN for a CMK, use ListKeys or DescribeKey.
    key_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The waiting period, specified in number of days. After the waiting period
    # ends, AWS KMS deletes the customer master key (CMK).

    # This value is optional. If you include a value, it must be between 7 and
    # 30, inclusive. If you do not include a value, it defaults to 30.
    pending_window_in_days: int = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ScheduleKeyDeletionResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "key_id",
                "KeyId",
                TypeInfo(str),
            ),
            (
                "deletion_date",
                "DeletionDate",
                TypeInfo(datetime.datetime),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The unique identifier of the customer master key (CMK) for which deletion
    # is scheduled.
    key_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The date and time after which AWS KMS deletes the customer master key
    # (CMK).
    deletion_date: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class Tag(ShapeBase):
    """
    A key-value pair. A tag consists of a tag key and a tag value. Tag keys and tag
    values are both required, but tag values can be empty (null) strings.

    For information about the rules that apply to tag keys and tag values, see
    [User-Defined Tag
    Restrictions](http://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/allocation-
    tag-restrictions.html) in the _AWS Billing and Cost Management User Guide_.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "tag_key",
                "TagKey",
                TypeInfo(str),
            ),
            (
                "tag_value",
                "TagValue",
                TypeInfo(str),
            ),
        ]

    # The key of the tag.
    tag_key: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The value of the tag.
    tag_value: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class TagException(ShapeBase):
    """
    The request was rejected because one or more tags are not valid.
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
class TagResourceRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "key_id",
                "KeyId",
                TypeInfo(str),
            ),
            (
                "tags",
                "Tags",
                TypeInfo(typing.List[Tag]),
            ),
        ]

    # A unique identifier for the CMK you are tagging.

    # Specify the key ID or the Amazon Resource Name (ARN) of the CMK.

    # For example:

    #   * Key ID: `1234abcd-12ab-34cd-56ef-1234567890ab`

    #   * Key ARN: `arn:aws:kms:us-east-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab`

    # To get the key ID and key ARN for a CMK, use ListKeys or DescribeKey.
    key_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # One or more tags. Each tag consists of a tag key and a tag value.
    tags: typing.List["Tag"] = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class UnsupportedOperationException(ShapeBase):
    """
    The request was rejected because a specified parameter is not supported or a
    specified resource is not valid for this operation.
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
class UntagResourceRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "key_id",
                "KeyId",
                TypeInfo(str),
            ),
            (
                "tag_keys",
                "TagKeys",
                TypeInfo(typing.List[str]),
            ),
        ]

    # A unique identifier for the CMK from which you are removing tags.

    # Specify the key ID or the Amazon Resource Name (ARN) of the CMK.

    # For example:

    #   * Key ID: `1234abcd-12ab-34cd-56ef-1234567890ab`

    #   * Key ARN: `arn:aws:kms:us-east-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab`

    # To get the key ID and key ARN for a CMK, use ListKeys or DescribeKey.
    key_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # One or more tag keys. Specify only the tag keys, not the tag values.
    tag_keys: typing.List[str] = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class UpdateAliasRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "alias_name",
                "AliasName",
                TypeInfo(str),
            ),
            (
                "target_key_id",
                "TargetKeyId",
                TypeInfo(str),
            ),
        ]

    # String that contains the name of the alias to be modified. The name must
    # start with the word "alias" followed by a forward slash (alias/). Aliases
    # that begin with "alias/aws" are reserved.
    alias_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Unique identifier of the customer master key to be mapped to the alias.

    # Specify the key ID or the Amazon Resource Name (ARN) of the CMK.

    # For example:

    #   * Key ID: `1234abcd-12ab-34cd-56ef-1234567890ab`

    #   * Key ARN: `arn:aws:kms:us-east-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab`

    # To get the key ID and key ARN for a CMK, use ListKeys or DescribeKey.

    # To verify that the alias is mapped to the correct CMK, use ListAliases.
    target_key_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class UpdateKeyDescriptionRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "key_id",
                "KeyId",
                TypeInfo(str),
            ),
            (
                "description",
                "Description",
                TypeInfo(str),
            ),
        ]

    # A unique identifier for the customer master key (CMK).

    # Specify the key ID or the Amazon Resource Name (ARN) of the CMK.

    # For example:

    #   * Key ID: `1234abcd-12ab-34cd-56ef-1234567890ab`

    #   * Key ARN: `arn:aws:kms:us-east-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab`

    # To get the key ID and key ARN for a CMK, use ListKeys or DescribeKey.
    key_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # New description for the CMK.
    description: str = dataclasses.field(default=ShapeBase.NOT_SET, )


class WrappingKeySpec(str):
    RSA_2048 = "RSA_2048"
