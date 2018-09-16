import datetime
import typing
from autoboto import ShapeBase, OutputShapeBase, TypeInfo
import botocore.response
import dataclasses


@dataclasses.dataclass
class CancelRotateSecretRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "secret_id",
                "SecretId",
                TypeInfo(str),
            ),
        ]

    # Specifies the secret for which you want to cancel a rotation request. You
    # can specify either the Amazon Resource Name (ARN) or the friendly name of
    # the secret.
    secret_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class CancelRotateSecretResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "arn",
                "ARN",
                TypeInfo(str),
            ),
            (
                "name",
                "Name",
                TypeInfo(str),
            ),
            (
                "version_id",
                "VersionId",
                TypeInfo(str),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The ARN of the secret for which rotation was canceled.
    arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The friendly name of the secret for which rotation was canceled.
    name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The unique identifier of the version of the secret that was created during
    # the rotation. This version might not be complete, and should be evaluated
    # for possible deletion. At the very least, you should remove the
    # `VersionStage` value `AWSPENDING` to enable this version to be deleted.
    # Failing to clean up a cancelled rotation can block you from successfully
    # starting future rotations.
    version_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class CreateSecretRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "name",
                "Name",
                TypeInfo(str),
            ),
            (
                "client_request_token",
                "ClientRequestToken",
                TypeInfo(str),
            ),
            (
                "description",
                "Description",
                TypeInfo(str),
            ),
            (
                "kms_key_id",
                "KmsKeyId",
                TypeInfo(str),
            ),
            (
                "secret_binary",
                "SecretBinary",
                TypeInfo(typing.Any),
            ),
            (
                "secret_string",
                "SecretString",
                TypeInfo(str),
            ),
            (
                "tags",
                "Tags",
                TypeInfo(typing.List[Tag]),
            ),
        ]

    # Specifies the friendly name of the new secret.

    # The secret name must be ASCII letters, digits, or the following characters
    # : /_+=.@-
    name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # (Optional) If you include `SecretString` or `SecretBinary`, then an initial
    # version is created as part of the secret, and this parameter specifies a
    # unique identifier for the new version.

    # If you use the AWS CLI or one of the AWS SDK to call this operation, then
    # you can leave this parameter empty. The CLI or SDK generates a random UUID
    # for you and includes it as the value for this parameter in the request. If
    # you don't use the SDK and instead generate a raw HTTP request to the
    # Secrets Manager service endpoint, then you must generate a
    # `ClientRequestToken` yourself for the new version and include that value in
    # the request.

    # This value helps ensure idempotency. Secrets Manager uses this value to
    # prevent the accidental creation of duplicate versions if there are failures
    # and retries during a rotation. We recommend that you generate a [UUID-
    # type](https://wikipedia.org/wiki/Universally_unique_identifier) value to
    # ensure uniqueness of your versions within the specified secret.

    #   * If the `ClientRequestToken` value isn't already associated with a version of the secret then a new version of the secret is created.

    #   * If a version with this value already exists and that version's `SecretString` and `SecretBinary` values are the same as those in the request, then the request is ignored (the operation is idempotent).

    #   * If a version with this value already exists and that version's `SecretString` and `SecretBinary` values are different from those in the request then the request fails because you cannot modify an existing version. Instead, use PutSecretValue to create a new version.

    # This value becomes the `VersionId` of the new version.
    client_request_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # (Optional) Specifies a user-provided description of the secret.
    description: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # (Optional) Specifies the ARN, Key ID, or alias of the AWS KMS customer
    # master key (CMK) to be used to encrypt the `SecretString` or `SecretBinary`
    # values in the versions stored in this secret.

    # You can specify any of the supported ways to identify a AWS KMS key ID. If
    # you need to reference a CMK in a different account, you can use only the
    # key ARN or the alias ARN.

    # If you don't specify this value, then Secrets Manager defaults to using the
    # AWS account's default CMK (the one named `aws/secretsmanager`). If a AWS
    # KMS CMK with that name doesn't yet exist, then Secrets Manager creates it
    # for you automatically the first time it needs to encrypt a version's
    # `SecretString` or `SecretBinary` fields.

    # You can use the account's default CMK to encrypt and decrypt only if you
    # call this operation using credentials from the same account that owns the
    # secret. If the secret is in a different account, then you must create a
    # custom CMK and specify the ARN in this field.
    kms_key_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # (Optional) Specifies binary data that you want to encrypt and store in the
    # new version of the secret. To use this parameter in the command-line tools,
    # we recommend that you store your binary data in a file and then use the
    # appropriate technique for your tool to pass the contents of the file as a
    # parameter.

    # Either `SecretString` or `SecretBinary` must have a value, but not both.
    # They cannot both be empty.

    # This parameter is not available using the Secrets Manager console. It can
    # be accessed only by using the AWS CLI or one of the AWS SDKs.
    secret_binary: typing.Any = dataclasses.field(default=ShapeBase.NOT_SET, )

    # (Optional) Specifies text data that you want to encrypt and store in this
    # new version of the secret.

    # Either `SecretString` or `SecretBinary` must have a value, but not both.
    # They cannot both be empty.

    # If you create a secret by using the Secrets Manager console then Secrets
    # Manager puts the protected secret text in only the `SecretString`
    # parameter. The Secrets Manager console stores the information as a JSON
    # structure of key/value pairs that the Lambda rotation function knows how to
    # parse.

    # For storing multiple values, we recommend that you use a JSON text string
    # argument and specify key/value pairs. For information on how to format a
    # JSON parameter for the various command line tool environments, see [Using
    # JSON for Parameters](http://docs.aws.amazon.com/cli/latest/userguide/cli-
    # using-param.html#cli-using-param-json) in the _AWS CLI User Guide_. For
    # example:

    # `[{"username":"bob"},{"password":"abc123xyz456"}]`

    # If your command-line tool or SDK requires quotation marks around the
    # parameter, you should use single quotes to avoid confusion with the double
    # quotes required in the JSON text.
    secret_string: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # (Optional) Specifies a list of user-defined tags that are attached to the
    # secret. Each tag is a "Key" and "Value" pair of strings. This operation
    # only appends tags to the existing list of tags. To remove tags, you must
    # use UntagResource.

    #   * Secrets Manager tag key names are case sensitive. A tag with the key "ABC" is a different tag from one with key "abc".

    #   * If you check tags in IAM policy `Condition` elements as part of your security strategy, then adding or removing a tag can change permissions. If the successful completion of this operation would result in you losing your permissions for this secret, then this operation is blocked and returns an `Access Denied` error.

    # This parameter requires a JSON text string argument. For information on how
    # to format a JSON parameter for the various command line tool environments,
    # see [Using JSON for
    # Parameters](http://docs.aws.amazon.com/cli/latest/userguide/cli-using-
    # param.html#cli-using-param-json) in the _AWS CLI User Guide_. For example:

    # `[{"Key":"CostCenter","Value":"12345"},{"Key":"environment","Value":"production"}]`

    # If your command-line tool or SDK requires quotation marks around the
    # parameter, you should use single quotes to avoid confusion with the double
    # quotes required in the JSON text.

    # The following basic restrictions apply to tags:

    #   * Maximum number of tags per secret—50

    #   * Maximum key length—127 Unicode characters in UTF-8

    #   * Maximum value length—255 Unicode characters in UTF-8

    #   * Tag keys and values are case sensitive.

    #   * Do not use the `aws:` prefix in your tag names or values because it is reserved for AWS use. You can't edit or delete tag names or values with this prefix. Tags with this prefix do not count against your tags per secret limit.

    #   * If your tagging schema will be used across multiple services and resources, remember that other services might have restrictions on allowed characters. Generally allowed characters are: letters, spaces, and numbers representable in UTF-8, plus the following special characters: + - = . _ : / @.
    tags: typing.List["Tag"] = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class CreateSecretResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "arn",
                "ARN",
                TypeInfo(str),
            ),
            (
                "name",
                "Name",
                TypeInfo(str),
            ),
            (
                "version_id",
                "VersionId",
                TypeInfo(str),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The Amazon Resource Name (ARN) of the secret that you just created.

    # Secrets Manager automatically adds several random characters to the name at
    # the end of the ARN when you initially create a secret. This affects only
    # the ARN and not the actual friendly name. This ensures that if you create a
    # new secret with the same name as an old secret that you previously deleted,
    # then users with access to the old secret _don't_ automatically get access
    # to the new secret because the ARNs are different.
    arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The friendly name of the secret that you just created.
    name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The unique identifier that's associated with the version of the secret you
    # just created.
    version_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DecryptionFailure(ShapeBase):
    """
    Secrets Manager can't decrypt the protected secret text using the provided KMS
    key.
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
class DeleteResourcePolicyRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "secret_id",
                "SecretId",
                TypeInfo(str),
            ),
        ]

    # Specifies the secret that you want to delete the attached resource-based
    # policy for. You can specify either the Amazon Resource Name (ARN) or the
    # friendly name of the secret.
    secret_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DeleteResourcePolicyResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "arn",
                "ARN",
                TypeInfo(str),
            ),
            (
                "name",
                "Name",
                TypeInfo(str),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The ARN of the secret that the resource-based policy was deleted for.
    arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The friendly name of the secret that the resource-based policy was deleted
    # for.
    name: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DeleteSecretRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "secret_id",
                "SecretId",
                TypeInfo(str),
            ),
            (
                "recovery_window_in_days",
                "RecoveryWindowInDays",
                TypeInfo(int),
            ),
            (
                "force_delete_without_recovery",
                "ForceDeleteWithoutRecovery",
                TypeInfo(bool),
            ),
        ]

    # Specifies the secret that you want to delete. You can specify either the
    # Amazon Resource Name (ARN) or the friendly name of the secret.
    secret_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # (Optional) Specifies the number of days that Secrets Manager waits before
    # it can delete the secret. You can't use both this parameter and the
    # `ForceDeleteWithoutRecovery` parameter in the same API call.

    # This value can range from 7 to 30 days. The default value is 30.
    recovery_window_in_days: int = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # (Optional) Specifies that the secret is to be deleted without any recovery
    # window. You can't use both this parameter and the `RecoveryWindowInDays`
    # parameter in the same API call.

    # An asynchronous background process performs the actual deletion, so there
    # can be a short delay before the operation completes. If you write code to
    # delete and then immediately recreate a secret with the same name, ensure
    # that your code includes appropriate back off and retry logic.

    # Use this parameter with caution. This parameter causes the operation to
    # skip the normal waiting period before the permanent deletion that AWS would
    # normally impose with the `RecoveryWindowInDays` parameter. If you delete a
    # secret with the `ForceDeleteWithouRecovery` parameter, then you have no
    # opportunity to recover the secret. It is permanently lost.
    force_delete_without_recovery: bool = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class DeleteSecretResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "arn",
                "ARN",
                TypeInfo(str),
            ),
            (
                "name",
                "Name",
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

    # The ARN of the secret that is now scheduled for deletion.
    arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The friendly name of the secret that is now scheduled for deletion.
    name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The date and time after which this secret can be deleted by Secrets Manager
    # and can no longer be restored. This value is the date and time of the
    # delete request plus the number of days specified in `RecoveryWindowInDays`.
    deletion_date: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class DescribeSecretRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "secret_id",
                "SecretId",
                TypeInfo(str),
            ),
        ]

    # The identifier of the secret whose details you want to retrieve. You can
    # specify either the Amazon Resource Name (ARN) or the friendly name of the
    # secret.
    secret_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DescribeSecretResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "arn",
                "ARN",
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
                "kms_key_id",
                "KmsKeyId",
                TypeInfo(str),
            ),
            (
                "rotation_enabled",
                "RotationEnabled",
                TypeInfo(bool),
            ),
            (
                "rotation_lambda_arn",
                "RotationLambdaARN",
                TypeInfo(str),
            ),
            (
                "rotation_rules",
                "RotationRules",
                TypeInfo(RotationRulesType),
            ),
            (
                "last_rotated_date",
                "LastRotatedDate",
                TypeInfo(datetime.datetime),
            ),
            (
                "last_changed_date",
                "LastChangedDate",
                TypeInfo(datetime.datetime),
            ),
            (
                "last_accessed_date",
                "LastAccessedDate",
                TypeInfo(datetime.datetime),
            ),
            (
                "deleted_date",
                "DeletedDate",
                TypeInfo(datetime.datetime),
            ),
            (
                "tags",
                "Tags",
                TypeInfo(typing.List[Tag]),
            ),
            (
                "version_ids_to_stages",
                "VersionIdsToStages",
                TypeInfo(typing.Dict[str, typing.List[str]]),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The ARN of the secret.
    arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The user-provided friendly name of the secret.
    name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The user-provided description of the secret.
    description: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The ARN or alias of the AWS KMS customer master key (CMK) that's used to
    # encrypt the `SecretString` or `SecretBinary` fields in each version of the
    # secret. If you don't provide a key, then Secrets Manager defaults to
    # encrypting the secret fields with the default AWS KMS CMK (the one named
    # `awssecretsmanager`) for this account.
    kms_key_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Specifies whether automatic rotation is enabled for this secret.

    # To enable rotation, use RotateSecret with `AutomaticallyRotateAfterDays`
    # set to a value greater than 0. To disable rotation, use CancelRotateSecret.
    rotation_enabled: bool = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The ARN of a Lambda function that's invoked by Secrets Manager to rotate
    # the secret either automatically per the schedule or manually by a call to
    # `RotateSecret`.
    rotation_lambda_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A structure that contains the rotation configuration for this secret.
    rotation_rules: "RotationRulesType" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The most recent date and time that the Secrets Manager rotation process was
    # successfully completed. This value is null if the secret has never rotated.
    last_rotated_date: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The last date and time that this secret was modified in any way.
    last_changed_date: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The last date that this secret was accessed. This value is truncated to
    # midnight of the date and therefore shows only the date, not the time.
    last_accessed_date: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # This value exists if the secret is scheduled for deletion. Some time after
    # the specified date and time, Secrets Manager deletes the secret and all of
    # its versions.

    # If a secret is scheduled for deletion, then its details, including the
    # encrypted secret information, is not accessible. To cancel a scheduled
    # deletion and restore access, use RestoreSecret.
    deleted_date: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The list of user-defined tags that are associated with the secret. To add
    # tags to a secret, use TagResource. To remove tags, use UntagResource.
    tags: typing.List["Tag"] = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A list of all of the currently assigned `VersionStage` staging labels and
    # the `VersionId` that each is attached to. Staging labels are used to keep
    # track of the different versions during the rotation process.

    # A version that does not have any staging labels attached is considered
    # deprecated and subject to deletion. Such versions are not included in this
    # list.
    version_ids_to_stages: typing.Dict[str, typing.
                                       List[str]] = dataclasses.field(
                                           default=ShapeBase.NOT_SET,
                                       )


@dataclasses.dataclass
class EncryptionFailure(ShapeBase):
    """
    Secrets Manager can't encrypt the protected secret text using the provided KMS
    key. Check that the customer master key (CMK) is available, enabled, and not in
    an invalid state. For more information, see [How Key State Affects Use of a
    Customer Master Key](http://docs.aws.amazon.com/kms/latest/developerguide/key-
    state.html).
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
class GetRandomPasswordRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "password_length",
                "PasswordLength",
                TypeInfo(int),
            ),
            (
                "exclude_characters",
                "ExcludeCharacters",
                TypeInfo(str),
            ),
            (
                "exclude_numbers",
                "ExcludeNumbers",
                TypeInfo(bool),
            ),
            (
                "exclude_punctuation",
                "ExcludePunctuation",
                TypeInfo(bool),
            ),
            (
                "exclude_uppercase",
                "ExcludeUppercase",
                TypeInfo(bool),
            ),
            (
                "exclude_lowercase",
                "ExcludeLowercase",
                TypeInfo(bool),
            ),
            (
                "include_space",
                "IncludeSpace",
                TypeInfo(bool),
            ),
            (
                "require_each_included_type",
                "RequireEachIncludedType",
                TypeInfo(bool),
            ),
        ]

    # The desired length of the generated password. The default value if you do
    # not include this parameter is 32 characters.
    password_length: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A string that includes characters that should not be included in the
    # generated password. The default is that all characters from the included
    # sets can be used.
    exclude_characters: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Specifies that the generated password should not include digits. The
    # default if you do not include this switch parameter is that digits can be
    # included.
    exclude_numbers: bool = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Specifies that the generated password should not include punctuation
    # characters. The default if you do not include this switch parameter is that
    # punctuation characters can be included.

    # The following are the punctuation characters that _can_ be included in the
    # generated password if you don't explicitly exclude them with
    # `ExcludeCharacters` or `ExcludePunctuation`:

    # `! " # $ % & ' ( ) * + , - . / : ; < = > ? @ [ \ ] ^ _ ` { | } ~`
    exclude_punctuation: bool = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Specifies that the generated password should not include uppercase letters.
    # The default if you do not include this switch parameter is that uppercase
    # letters can be included.
    exclude_uppercase: bool = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Specifies that the generated password should not include lowercase letters.
    # The default if you do not include this switch parameter is that lowercase
    # letters can be included.
    exclude_lowercase: bool = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Specifies that the generated password can include the space character. The
    # default if you do not include this switch parameter is that the space
    # character is not included.
    include_space: bool = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A boolean value that specifies whether the generated password must include
    # at least one of every allowed character type. The default value is `True`
    # and the operation requires at least one of every character type.
    require_each_included_type: bool = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class GetRandomPasswordResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "random_password",
                "RandomPassword",
                TypeInfo(str),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A string with the generated password.
    random_password: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class GetResourcePolicyRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "secret_id",
                "SecretId",
                TypeInfo(str),
            ),
        ]

    # Specifies the secret that you want to retrieve the attached resource-based
    # policy for. You can specify either the Amazon Resource Name (ARN) or the
    # friendly name of the secret.
    secret_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class GetResourcePolicyResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "arn",
                "ARN",
                TypeInfo(str),
            ),
            (
                "name",
                "Name",
                TypeInfo(str),
            ),
            (
                "resource_policy",
                "ResourcePolicy",
                TypeInfo(str),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The ARN of the secret that the resource-based policy was retrieved for.
    arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The friendly name of the secret that the resource-based policy was
    # retrieved for.
    name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A JSON-formatted string that describes the permissions that are associated
    # with the attached secret. These permissions are combined with any
    # permissions that are associated with the user or role that attempts to
    # access this secret. The combined permissions specify who can access the
    # secret and what actions they can perform. For more information, see
    # [Authentication and Access Control for AWS Secrets
    # Manager](http://docs.aws.amazon.com/secretsmanager/latest/userguide/auth-
    # and-access.html) in the _AWS Secrets Manager User Guide_.
    resource_policy: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class GetSecretValueRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "secret_id",
                "SecretId",
                TypeInfo(str),
            ),
            (
                "version_id",
                "VersionId",
                TypeInfo(str),
            ),
            (
                "version_stage",
                "VersionStage",
                TypeInfo(str),
            ),
        ]

    # Specifies the secret containing the version that you want to retrieve. You
    # can specify either the Amazon Resource Name (ARN) or the friendly name of
    # the secret.
    secret_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Specifies the unique identifier of the version of the secret that you want
    # to retrieve. If you specify this parameter then don't specify
    # `VersionStage`. If you don't specify either a `VersionStage` or `VersionId`
    # then the default is to perform the operation on the version with the
    # `VersionStage` value of `AWSCURRENT`.

    # This value is typically a [UUID-
    # type](https://wikipedia.org/wiki/Universally_unique_identifier) value with
    # 32 hexadecimal digits.
    version_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Specifies the secret version that you want to retrieve by the staging label
    # attached to the version.

    # Staging labels are used to keep track of different versions during the
    # rotation process. If you use this parameter then don't specify `VersionId`.
    # If you don't specify either a `VersionStage` or `VersionId`, then the
    # default is to perform the operation on the version with the `VersionStage`
    # value of `AWSCURRENT`.
    version_stage: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class GetSecretValueResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "arn",
                "ARN",
                TypeInfo(str),
            ),
            (
                "name",
                "Name",
                TypeInfo(str),
            ),
            (
                "version_id",
                "VersionId",
                TypeInfo(str),
            ),
            (
                "secret_binary",
                "SecretBinary",
                TypeInfo(typing.Any),
            ),
            (
                "secret_string",
                "SecretString",
                TypeInfo(str),
            ),
            (
                "version_stages",
                "VersionStages",
                TypeInfo(typing.List[str]),
            ),
            (
                "created_date",
                "CreatedDate",
                TypeInfo(datetime.datetime),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The ARN of the secret.
    arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The friendly name of the secret.
    name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The unique identifier of this version of the secret.
    version_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The decrypted part of the protected secret information that was originally
    # provided as binary data in the form of a byte array. The response parameter
    # represents the binary data as a
    # [base64-encoded](https://tools.ietf.org/html/rfc4648#section-4) string.

    # This parameter is not used if the secret is created by the Secrets Manager
    # console.

    # If you store custom information in this field of the secret, then you must
    # code your Lambda rotation function to parse and interpret whatever you
    # store in the `SecretString` or `SecretBinary` fields.
    secret_binary: typing.Any = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The decrypted part of the protected secret information that was originally
    # provided as a string.

    # If you create this secret by using the Secrets Manager console then only
    # the `SecretString` parameter contains data. Secrets Manager stores the
    # information as a JSON structure of key/value pairs that the Lambda rotation
    # function knows how to parse.

    # If you store custom information in the secret by using the CreateSecret,
    # UpdateSecret, or PutSecretValue API operations instead of the Secrets
    # Manager console, or by using the **Other secret type** in the console, then
    # you must code your Lambda rotation function to parse and interpret those
    # values.
    secret_string: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A list of all of the staging labels currently attached to this version of
    # the secret.
    version_stages: typing.List[str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The date and time that this version of the secret was created.
    created_date: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class InternalServiceError(ShapeBase):
    """
    An error occurred on the server side.
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
class InvalidNextTokenException(ShapeBase):
    """
    You provided an invalid `NextToken` value.
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
class InvalidParameterException(ShapeBase):
    """
    You provided an invalid value for a parameter.
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
class InvalidRequestException(ShapeBase):
    """
    You provided a parameter value that is not valid for the current state of the
    resource.

    Possible causes:

      * You tried to perform the operation on a secret that's currently marked deleted.

      * You tried to enable rotation on a secret that doesn't already have a Lambda function ARN configured and you didn't include such an ARN as a parameter in this call.
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
    The request failed because it would exceed one of the Secrets Manager internal
    limits.
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
class ListSecretVersionIdsRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "secret_id",
                "SecretId",
                TypeInfo(str),
            ),
            (
                "max_results",
                "MaxResults",
                TypeInfo(int),
            ),
            (
                "next_token",
                "NextToken",
                TypeInfo(str),
            ),
            (
                "include_deprecated",
                "IncludeDeprecated",
                TypeInfo(bool),
            ),
        ]

    # The identifier for the secret containing the versions you want to list. You
    # can specify either the Amazon Resource Name (ARN) or the friendly name of
    # the secret.
    secret_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # (Optional) Limits the number of results that you want to include in the
    # response. If you don't include this parameter, it defaults to a value
    # that's specific to the operation. If additional items exist beyond the
    # maximum you specify, the `NextToken` response element is present and has a
    # value (isn't null). Include that value as the `NextToken` request parameter
    # in the next call to the operation to get the next part of the results. Note
    # that Secrets Manager might return fewer results than the maximum even when
    # there are more results available. You should check `NextToken` after every
    # operation to ensure that you receive all of the results.
    max_results: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # (Optional) Use this parameter in a request if you receive a `NextToken`
    # response in a previous request that indicates that there's more output
    # available. In a subsequent call, set it to the value of the previous call's
    # `NextToken` response to indicate where the output should continue from.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # (Optional) Specifies that you want the results to include versions that do
    # not have any staging labels attached to them. Such versions are considered
    # deprecated and are subject to deletion by Secrets Manager as needed.
    include_deprecated: bool = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ListSecretVersionIdsResponse(OutputShapeBase):
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
                TypeInfo(typing.List[SecretVersionsListEntry]),
            ),
            (
                "next_token",
                "NextToken",
                TypeInfo(str),
            ),
            (
                "arn",
                "ARN",
                TypeInfo(str),
            ),
            (
                "name",
                "Name",
                TypeInfo(str),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The list of the currently available versions of the specified secret.
    versions: typing.List["SecretVersionsListEntry"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # If present in the response, this value indicates that there's more output
    # available than what's included in the current response. This can occur even
    # when the response includes no values at all, such as when you ask for a
    # filtered view of a very long list. Use this value in the `NextToken`
    # request parameter in a subsequent call to the operation to continue
    # processing and get the next part of the output. You should repeat this
    # until the `NextToken` response element comes back empty (as `null`).
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The Amazon Resource Name (ARN) for the secret.

    # Secrets Manager automatically adds several random characters to the name at
    # the end of the ARN when you initially create a secret. This affects only
    # the ARN and not the actual friendly name. This ensures that if you create a
    # new secret with the same name as an old secret that you previously deleted,
    # then users with access to the old secret _don't_ automatically get access
    # to the new secret because the ARNs are different.
    arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The friendly name of the secret.
    name: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ListSecretsRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "max_results",
                "MaxResults",
                TypeInfo(int),
            ),
            (
                "next_token",
                "NextToken",
                TypeInfo(str),
            ),
        ]

    # (Optional) Limits the number of results that you want to include in the
    # response. If you don't include this parameter, it defaults to a value
    # that's specific to the operation. If additional items exist beyond the
    # maximum you specify, the `NextToken` response element is present and has a
    # value (isn't null). Include that value as the `NextToken` request parameter
    # in the next call to the operation to get the next part of the results. Note
    # that Secrets Manager might return fewer results than the maximum even when
    # there are more results available. You should check `NextToken` after every
    # operation to ensure that you receive all of the results.
    max_results: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # (Optional) Use this parameter in a request if you receive a `NextToken`
    # response in a previous request that indicates that there's more output
    # available. In a subsequent call, set it to the value of the previous call's
    # `NextToken` response to indicate where the output should continue from.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ListSecretsResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "secret_list",
                "SecretList",
                TypeInfo(typing.List[SecretListEntry]),
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

    # A list of the secrets in the account.
    secret_list: typing.List["SecretListEntry"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # If present in the response, this value indicates that there's more output
    # available than what's included in the current response. This can occur even
    # when the response includes no values at all, such as when you ask for a
    # filtered view of a very long list. Use this value in the `NextToken`
    # request parameter in a subsequent call to the operation to continue
    # processing and get the next part of the output. You should repeat this
    # until the `NextToken` response element comes back empty (as `null`).
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class MalformedPolicyDocumentException(ShapeBase):
    """
    The policy document that you provided isn't valid.
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
class PreconditionNotMetException(ShapeBase):
    """
    The request failed because you did not complete all the prerequisite steps.
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
class PutResourcePolicyRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "secret_id",
                "SecretId",
                TypeInfo(str),
            ),
            (
                "resource_policy",
                "ResourcePolicy",
                TypeInfo(str),
            ),
        ]

    # Specifies the secret that you want to attach the resource-based policy to.
    # You can specify either the ARN or the friendly name of the secret.
    secret_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A JSON-formatted string that's constructed according to the grammar and
    # syntax for an AWS resource-based policy. The policy in the string
    # identifies who can access or manage this secret and its versions. For
    # information on how to format a JSON parameter for the various command line
    # tool environments, see [Using JSON for
    # Parameters](http://docs.aws.amazon.com/cli/latest/userguide/cli-using-
    # param.html#cli-using-param-json) in the _AWS CLI User Guide_.
    resource_policy: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class PutResourcePolicyResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "arn",
                "ARN",
                TypeInfo(str),
            ),
            (
                "name",
                "Name",
                TypeInfo(str),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The ARN of the secret that the resource-based policy was retrieved for.
    arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The friendly name of the secret that the resource-based policy was
    # retrieved for.
    name: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class PutSecretValueRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "secret_id",
                "SecretId",
                TypeInfo(str),
            ),
            (
                "client_request_token",
                "ClientRequestToken",
                TypeInfo(str),
            ),
            (
                "secret_binary",
                "SecretBinary",
                TypeInfo(typing.Any),
            ),
            (
                "secret_string",
                "SecretString",
                TypeInfo(str),
            ),
            (
                "version_stages",
                "VersionStages",
                TypeInfo(typing.List[str]),
            ),
        ]

    # Specifies the secret to which you want to add a new version. You can
    # specify either the Amazon Resource Name (ARN) or the friendly name of the
    # secret. The secret must already exist.
    secret_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # (Optional) Specifies a unique identifier for the new version of the secret.

    # If you use the AWS CLI or one of the AWS SDK to call this operation, then
    # you can leave this parameter empty. The CLI or SDK generates a random UUID
    # for you and includes that in the request. If you don't use the SDK and
    # instead generate a raw HTTP request to the Secrets Manager service
    # endpoint, then you must generate a `ClientRequestToken` yourself for new
    # versions and include that value in the request.

    # This value helps ensure idempotency. Secrets Manager uses this value to
    # prevent the accidental creation of duplicate versions if there are failures
    # and retries during the Lambda rotation function's processing. We recommend
    # that you generate a [UUID-
    # type](https://wikipedia.org/wiki/Universally_unique_identifier) value to
    # ensure uniqueness within the specified secret.

    #   * If the `ClientRequestToken` value isn't already associated with a version of the secret then a new version of the secret is created.

    #   * If a version with this value already exists and that version's `SecretString` or `SecretBinary` values are the same as those in the request then the request is ignored (the operation is idempotent).

    #   * If a version with this value already exists and that version's `SecretString` and `SecretBinary` values are different from those in the request then the request fails because you cannot modify an existing secret version. You can only create new versions to store new secret values.

    # This value becomes the `VersionId` of the new version.
    client_request_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # (Optional) Specifies binary data that you want to encrypt and store in the
    # new version of the secret. To use this parameter in the command-line tools,
    # we recommend that you store your binary data in a file and then use the
    # appropriate technique for your tool to pass the contents of the file as a
    # parameter. Either `SecretBinary` or `SecretString` must have a value, but
    # not both. They cannot both be empty.

    # This parameter is not accessible if the secret using the Secrets Manager
    # console.
    secret_binary: typing.Any = dataclasses.field(default=ShapeBase.NOT_SET, )

    # (Optional) Specifies text data that you want to encrypt and store in this
    # new version of the secret. Either `SecretString` or `SecretBinary` must
    # have a value, but not both. They cannot both be empty.

    # If you create this secret by using the Secrets Manager console then Secrets
    # Manager puts the protected secret text in only the `SecretString`
    # parameter. The Secrets Manager console stores the information as a JSON
    # structure of key/value pairs that the default Lambda rotation function
    # knows how to parse.

    # For storing multiple values, we recommend that you use a JSON text string
    # argument and specify key/value pairs. For information on how to format a
    # JSON parameter for the various command line tool environments, see [Using
    # JSON for Parameters](http://docs.aws.amazon.com/cli/latest/userguide/cli-
    # using-param.html#cli-using-param-json) in the _AWS CLI User Guide_.

    # For example:

    # `[{"username":"bob"},{"password":"abc123xyz456"}]`

    # If your command-line tool or SDK requires quotation marks around the
    # parameter, you should use single quotes to avoid confusion with the double
    # quotes required in the JSON text.
    secret_string: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # (Optional) Specifies a list of staging labels that are attached to this
    # version of the secret. These staging labels are used to track the versions
    # through the rotation process by the Lambda rotation function.

    # A staging label must be unique to a single version of the secret. If you
    # specify a staging label that's already associated with a different version
    # of the same secret then that staging label is automatically removed from
    # the other version and attached to this version.

    # If you do not specify a value for `VersionStages` then Secrets Manager
    # automatically moves the staging label `AWSCURRENT` to this new version.
    version_stages: typing.List[str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class PutSecretValueResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "arn",
                "ARN",
                TypeInfo(str),
            ),
            (
                "name",
                "Name",
                TypeInfo(str),
            ),
            (
                "version_id",
                "VersionId",
                TypeInfo(str),
            ),
            (
                "version_stages",
                "VersionStages",
                TypeInfo(typing.List[str]),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The Amazon Resource Name (ARN) for the secret for which you just created a
    # version.
    arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The friendly name of the secret for which you just created or updated a
    # version.
    name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The unique identifier of the version of the secret you just created or
    # updated.
    version_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The list of staging labels that are currently attached to this version of
    # the secret. Staging labels are used to track a version as it progresses
    # through the secret rotation process.
    version_stages: typing.List[str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class ResourceExistsException(ShapeBase):
    """
    A resource with the ID you requested already exists.
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
class ResourceNotFoundException(ShapeBase):
    """
    We can't find the resource that you asked for.
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
class RestoreSecretRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "secret_id",
                "SecretId",
                TypeInfo(str),
            ),
        ]

    # Specifies the secret that you want to restore from a previously scheduled
    # deletion. You can specify either the Amazon Resource Name (ARN) or the
    # friendly name of the secret.
    secret_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class RestoreSecretResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "arn",
                "ARN",
                TypeInfo(str),
            ),
            (
                "name",
                "Name",
                TypeInfo(str),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The ARN of the secret that was restored.
    arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The friendly name of the secret that was restored.
    name: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class RotateSecretRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "secret_id",
                "SecretId",
                TypeInfo(str),
            ),
            (
                "client_request_token",
                "ClientRequestToken",
                TypeInfo(str),
            ),
            (
                "rotation_lambda_arn",
                "RotationLambdaARN",
                TypeInfo(str),
            ),
            (
                "rotation_rules",
                "RotationRules",
                TypeInfo(RotationRulesType),
            ),
        ]

    # Specifies the secret that you want to rotate. You can specify either the
    # Amazon Resource Name (ARN) or the friendly name of the secret.
    secret_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # (Optional) Specifies a unique identifier for the new version of the secret
    # that helps ensure idempotency.

    # If you use the AWS CLI or one of the AWS SDK to call this operation, then
    # you can leave this parameter empty. The CLI or SDK generates a random UUID
    # for you and includes that in the request for this parameter. If you don't
    # use the SDK and instead generate a raw HTTP request to the Secrets Manager
    # service endpoint, then you must generate a `ClientRequestToken` yourself
    # for new versions and include that value in the request.

    # You only need to specify your own value if you are implementing your own
    # retry logic and want to ensure that a given secret is not created twice. We
    # recommend that you generate a [UUID-
    # type](https://wikipedia.org/wiki/Universally_unique_identifier) value to
    # ensure uniqueness within the specified secret.

    # Secrets Manager uses this value to prevent the accidental creation of
    # duplicate versions if there are failures and retries during the function's
    # processing. This value becomes the `VersionId` of the new version.
    client_request_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # (Optional) Specifies the ARN of the Lambda function that can rotate the
    # secret.
    rotation_lambda_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A structure that defines the rotation configuration for this secret.
    rotation_rules: "RotationRulesType" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class RotateSecretResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "arn",
                "ARN",
                TypeInfo(str),
            ),
            (
                "name",
                "Name",
                TypeInfo(str),
            ),
            (
                "version_id",
                "VersionId",
                TypeInfo(str),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The ARN of the secret.
    arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The friendly name of the secret.
    name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The ID of the new version of the secret created by the rotation started by
    # this request.
    version_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class RotationRulesType(ShapeBase):
    """
    A structure that defines the rotation configuration for the secret.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "automatically_after_days",
                "AutomaticallyAfterDays",
                TypeInfo(int),
            ),
        ]

    # Specifies the number of days between automatic scheduled rotations of the
    # secret.

    # Secrets Manager schedules the next rotation when the previous one is
    # complete. Secrets Manager schedules the date by adding the rotation
    # interval (number of days) to the actual date of the last rotation. The
    # service chooses the hour within that 24-hour date window randomly. The
    # minute is also chosen somewhat randomly, but weighted towards the top of
    # the hour and influenced by a variety of factors that help distribute load.
    automatically_after_days: int = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


class SecretBinaryType(botocore.response.StreamingBody):
    pass


@dataclasses.dataclass
class SecretListEntry(ShapeBase):
    """
    A structure that contains the details about a secret. It does not include the
    encrypted `SecretString` and `SecretBinary` values. To get those values, use the
    GetSecretValue operation.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "arn",
                "ARN",
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
                "kms_key_id",
                "KmsKeyId",
                TypeInfo(str),
            ),
            (
                "rotation_enabled",
                "RotationEnabled",
                TypeInfo(bool),
            ),
            (
                "rotation_lambda_arn",
                "RotationLambdaARN",
                TypeInfo(str),
            ),
            (
                "rotation_rules",
                "RotationRules",
                TypeInfo(RotationRulesType),
            ),
            (
                "last_rotated_date",
                "LastRotatedDate",
                TypeInfo(datetime.datetime),
            ),
            (
                "last_changed_date",
                "LastChangedDate",
                TypeInfo(datetime.datetime),
            ),
            (
                "last_accessed_date",
                "LastAccessedDate",
                TypeInfo(datetime.datetime),
            ),
            (
                "deleted_date",
                "DeletedDate",
                TypeInfo(datetime.datetime),
            ),
            (
                "tags",
                "Tags",
                TypeInfo(typing.List[Tag]),
            ),
            (
                "secret_versions_to_stages",
                "SecretVersionsToStages",
                TypeInfo(typing.Dict[str, typing.List[str]]),
            ),
        ]

    # The Amazon Resource Name (ARN) of the secret.

    # For more information about ARNs in Secrets Manager, see [Policy
    # Resources](http://docs.aws.amazon.com/secretsmanager/latest/userguide/reference_iam-
    # permissions.html#iam-resources) in the _AWS Secrets Manager User Guide_.
    arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The friendly name of the secret. You can use forward slashes in the name to
    # represent a path hierarchy. For example, `/prod/databases/dbserver1` could
    # represent the secret for a server named `dbserver1` in the folder
    # `databases` in the folder `prod`.
    name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The user-provided description of the secret.
    description: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The ARN or alias of the AWS KMS customer master key (CMK) that's used to
    # encrypt the `SecretString` and `SecretBinary` fields in each version of the
    # secret. If you don't provide a key, then Secrets Manager defaults to
    # encrypting the secret fields with the default KMS CMK (the one named
    # `awssecretsmanager`) for this account.
    kms_key_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Indicated whether automatic, scheduled rotation is enabled for this secret.
    rotation_enabled: bool = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The ARN of an AWS Lambda function that's invoked by Secrets Manager to
    # rotate and expire the secret either automatically per the schedule or
    # manually by a call to RotateSecret.
    rotation_lambda_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A structure that defines the rotation configuration for the secret.
    rotation_rules: "RotationRulesType" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The last date and time that the rotation process for this secret was
    # invoked.
    last_rotated_date: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The last date and time that this secret was modified in any way.
    last_changed_date: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The last date that this secret was accessed. This value is truncated to
    # midnight of the date and therefore shows only the date, not the time.
    last_accessed_date: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The date and time on which this secret was deleted. Not present on active
    # secrets. The secret can be recovered until the number of days in the
    # recovery window has passed, as specified in the `RecoveryWindowInDays`
    # parameter of the DeleteSecret operation.
    deleted_date: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The list of user-defined tags that are associated with the secret. To add
    # tags to a secret, use TagResource. To remove tags, use UntagResource.
    tags: typing.List["Tag"] = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A list of all of the currently assigned `SecretVersionStage` staging labels
    # and the `SecretVersionId` that each is attached to. Staging labels are used
    # to keep track of the different versions during the rotation process.

    # A version that does not have any `SecretVersionStage` is considered
    # deprecated and subject to deletion. Such versions are not included in this
    # list.
    secret_versions_to_stages: typing.Dict[str, typing.
                                           List[str]] = dataclasses.field(
                                               default=ShapeBase.NOT_SET,
                                           )


@dataclasses.dataclass
class SecretVersionsListEntry(ShapeBase):
    """
    A structure that contains information about one version of a secret.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "version_id",
                "VersionId",
                TypeInfo(str),
            ),
            (
                "version_stages",
                "VersionStages",
                TypeInfo(typing.List[str]),
            ),
            (
                "last_accessed_date",
                "LastAccessedDate",
                TypeInfo(datetime.datetime),
            ),
            (
                "created_date",
                "CreatedDate",
                TypeInfo(datetime.datetime),
            ),
        ]

    # The unique version identifier of this version of the secret.
    version_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # An array of staging labels that are currently associated with this version
    # of the secret.
    version_stages: typing.List[str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The date that this version of the secret was last accessed. Note that the
    # resolution of this field is at the date level and does not include the
    # time.
    last_accessed_date: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The date and time this version of the secret was created.
    created_date: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class Tag(ShapeBase):
    """
    A structure that contains information about a tag.
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

    # The key identifier, or name, of the tag.
    key: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The string value that's associated with the key of the tag.
    value: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class TagResourceRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "secret_id",
                "SecretId",
                TypeInfo(str),
            ),
            (
                "tags",
                "Tags",
                TypeInfo(typing.List[Tag]),
            ),
        ]

    # The identifier for the secret that you want to attach tags to. You can
    # specify either the Amazon Resource Name (ARN) or the friendly name of the
    # secret.
    secret_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The tags to attach to the secret. Each element in the list consists of a
    # `Key` and a `Value`.

    # This parameter to the API requires a JSON text string argument. For
    # information on how to format a JSON parameter for the various command line
    # tool environments, see [Using JSON for
    # Parameters](http://docs.aws.amazon.com/cli/latest/userguide/cli-using-
    # param.html#cli-using-param-json) in the _AWS CLI User Guide_. For the AWS
    # CLI, you can also use the syntax: `--Tags
    # Key="Key1",Value="Value1",Key="Key2",Value="Value2"[,…]`
    tags: typing.List["Tag"] = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class UntagResourceRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "secret_id",
                "SecretId",
                TypeInfo(str),
            ),
            (
                "tag_keys",
                "TagKeys",
                TypeInfo(typing.List[str]),
            ),
        ]

    # The identifier for the secret that you want to remove tags from. You can
    # specify either the Amazon Resource Name (ARN) or the friendly name of the
    # secret.
    secret_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A list of tag key names to remove from the secret. You don't specify the
    # value. Both the key and its associated value are removed.

    # This parameter to the API requires a JSON text string argument. For
    # information on how to format a JSON parameter for the various command line
    # tool environments, see [Using JSON for
    # Parameters](http://docs.aws.amazon.com/cli/latest/userguide/cli-using-
    # param.html#cli-using-param-json) in the _AWS CLI User Guide_.
    tag_keys: typing.List[str] = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class UpdateSecretRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "secret_id",
                "SecretId",
                TypeInfo(str),
            ),
            (
                "client_request_token",
                "ClientRequestToken",
                TypeInfo(str),
            ),
            (
                "description",
                "Description",
                TypeInfo(str),
            ),
            (
                "kms_key_id",
                "KmsKeyId",
                TypeInfo(str),
            ),
            (
                "secret_binary",
                "SecretBinary",
                TypeInfo(typing.Any),
            ),
            (
                "secret_string",
                "SecretString",
                TypeInfo(str),
            ),
        ]

    # Specifies the secret that you want to modify or to which you want to add a
    # new version. You can specify either the Amazon Resource Name (ARN) or the
    # friendly name of the secret.
    secret_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # (Optional) If you want to add a new version to the secret, this parameter
    # specifies a unique identifier for the new version that helps ensure
    # idempotency.

    # If you use the AWS CLI or one of the AWS SDK to call this operation, then
    # you can leave this parameter empty. The CLI or SDK generates a random UUID
    # for you and includes that in the request. If you don't use the SDK and
    # instead generate a raw HTTP request to the Secrets Manager service
    # endpoint, then you must generate a `ClientRequestToken` yourself for new
    # versions and include that value in the request.

    # You typically only need to interact with this value if you implement your
    # own retry logic and want to ensure that a given secret is not created
    # twice. We recommend that you generate a [UUID-
    # type](https://wikipedia.org/wiki/Universally_unique_identifier) value to
    # ensure uniqueness within the specified secret.

    # Secrets Manager uses this value to prevent the accidental creation of
    # duplicate versions if there are failures and retries during the Lambda
    # rotation function's processing.

    #   * If the `ClientRequestToken` value isn't already associated with a version of the secret then a new version of the secret is created.

    #   * If a version with this value already exists and that version's `SecretString` and `SecretBinary` values are the same as those in the request then the request is ignored (the operation is idempotent).

    #   * If a version with this value already exists and that version's `SecretString` and `SecretBinary` values are different from the request then an error occurs because you cannot modify an existing secret value.

    # This value becomes the `VersionId` of the new version.
    client_request_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # (Optional) Specifies an updated user-provided description of the secret.
    description: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # (Optional) Specifies an updated ARN or alias of the AWS KMS customer master
    # key (CMK) to be used to encrypt the protected text in new versions of this
    # secret.

    # You can only use the account's default CMK to encrypt and decrypt if you
    # call this operation using credentials from the same account that owns the
    # secret. If the secret is in a different account, then you must create a
    # custom CMK and provide the ARN of that CMK in this field. The user making
    # the call must have permissions to both the secret and the CMK in their
    # respective accounts.
    kms_key_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # (Optional) Specifies updated binary data that you want to encrypt and store
    # in the new version of the secret. To use this parameter in the command-line
    # tools, we recommend that you store your binary data in a file and then use
    # the appropriate technique for your tool to pass the contents of the file as
    # a parameter. Either `SecretBinary` or `SecretString` must have a value, but
    # not both. They cannot both be empty.

    # This parameter is not accessible using the Secrets Manager console.
    secret_binary: typing.Any = dataclasses.field(default=ShapeBase.NOT_SET, )

    # (Optional) Specifies updated text data that you want to encrypt and store
    # in this new version of the secret. Either `SecretBinary` or `SecretString`
    # must have a value, but not both. They cannot both be empty.

    # If you create this secret by using the Secrets Manager console then Secrets
    # Manager puts the protected secret text in only the `SecretString`
    # parameter. The Secrets Manager console stores the information as a JSON
    # structure of key/value pairs that the default Lambda rotation function
    # knows how to parse.

    # For storing multiple values, we recommend that you use a JSON text string
    # argument and specify key/value pairs. For information on how to format a
    # JSON parameter for the various command line tool environments, see [Using
    # JSON for Parameters](http://docs.aws.amazon.com/cli/latest/userguide/cli-
    # using-param.html#cli-using-param-json) in the _AWS CLI User Guide_. For
    # example:

    # `[{"username":"bob"},{"password":"abc123xyz456"}]`

    # If your command-line tool or SDK requires quotation marks around the
    # parameter, you should use single quotes to avoid confusion with the double
    # quotes required in the JSON text. You can also 'escape' the double quote
    # character in the embedded JSON text by prefacing each with a backslash. For
    # example, the following string is surrounded by double-quotes. All of the
    # embedded double quotes are escaped:

    # `"[{\"username\":\"bob\"},{\"password\":\"abc123xyz456\"}]"`
    secret_string: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class UpdateSecretResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "arn",
                "ARN",
                TypeInfo(str),
            ),
            (
                "name",
                "Name",
                TypeInfo(str),
            ),
            (
                "version_id",
                "VersionId",
                TypeInfo(str),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The ARN of the secret that was updated.

    # Secrets Manager automatically adds several random characters to the name at
    # the end of the ARN when you initially create a secret. This affects only
    # the ARN and not the actual friendly name. This ensures that if you create a
    # new secret with the same name as an old secret that you previously deleted,
    # then users with access to the old secret _don't_ automatically get access
    # to the new secret because the ARNs are different.
    arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The friendly name of the secret that was updated.
    name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # If a new version of the secret was created by this operation, then
    # `VersionId` contains the unique identifier of the new version.
    version_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class UpdateSecretVersionStageRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "secret_id",
                "SecretId",
                TypeInfo(str),
            ),
            (
                "version_stage",
                "VersionStage",
                TypeInfo(str),
            ),
            (
                "remove_from_version_id",
                "RemoveFromVersionId",
                TypeInfo(str),
            ),
            (
                "move_to_version_id",
                "MoveToVersionId",
                TypeInfo(str),
            ),
        ]

    # Specifies the secret with the version whose list of staging labels you want
    # to modify. You can specify either the Amazon Resource Name (ARN) or the
    # friendly name of the secret.
    secret_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The list of staging labels to add to this version.
    version_stage: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # (Optional) Specifies the secret version ID of the version that the staging
    # labels are to be removed from.

    # If you want to move a label to a new version, you do not have to explicitly
    # remove it with this parameter. Adding a label using the `MoveToVersionId`
    # parameter automatically removes it from the old version. However, if you do
    # include both the "MoveTo" and "RemoveFrom" parameters, then the move is
    # successful only if the staging labels are actually present on the
    # "RemoveFrom" version. If a staging label was on a different version than
    # "RemoveFrom", then the request fails.
    remove_from_version_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # (Optional) The secret version ID that you want to add the staging labels
    # to.

    # If any of the staging labels are already attached to a different version of
    # the secret, then they are automatically removed from that version before
    # adding them to this version.
    move_to_version_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class UpdateSecretVersionStageResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "arn",
                "ARN",
                TypeInfo(str),
            ),
            (
                "name",
                "Name",
                TypeInfo(str),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The ARN of the secret with the staging labels that were modified.
    arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The friendly name of the secret with the staging labels that were modified.
    name: str = dataclasses.field(default=ShapeBase.NOT_SET, )
