import datetime
import typing
import boto3
from autoboto import ClientBase, ShapeBase, OutputShapeBase
from . import shapes


class Client(ClientBase):
    def __init__(self, *args, **kwargs):
        super().__init__("secretsmanager", *args, **kwargs)

    def cancel_rotate_secret(
        self,
        _request: shapes.CancelRotateSecretRequest = None,
        *,
        secret_id: str,
    ) -> shapes.CancelRotateSecretResponse:
        """
        Disables automatic scheduled rotation and cancels the rotation of a secret if
        one is currently in progress.

        To re-enable scheduled rotation, call RotateSecret with
        `AutomaticallyRotateAfterDays` set to a value greater than 0. This will
        immediately rotate your secret and then enable the automatic schedule.

        If you cancel a rotation that is in progress, it can leave the `VersionStage`
        labels in an unexpected state. Depending on what step of the rotation was in
        progress, you might need to remove the staging label `AWSPENDING` from the
        partially created version, specified by the `VersionId` response value. You
        should also evaluate the partially rotated new version to see if it should be
        deleted, which you can do by removing all staging labels from the new version's
        `VersionStage` field.

        To successfully start a rotation, the staging label `AWSPENDING` must be in one
        of the following states:

          * Not be attached to any version at all

          * Attached to the same version as the staging label `AWSCURRENT`

        If the staging label `AWSPENDING` is attached to a different version than the
        version with `AWSCURRENT` then the attempt to rotate fails.

        **Minimum permissions**

        To run this command, you must have the following permissions:

          * secretsmanager:CancelRotateSecret

        **Related operations**

          * To configure rotation for a secret or to manually trigger a rotation, use RotateSecret.

          * To get the rotation configuration details for a secret, use DescribeSecret.

          * To list all of the currently available secrets, use ListSecrets.

          * To list all of the versions currently associated with a secret, use ListSecretVersionIds.
        """
        if _request is None:
            _params = {}
            if secret_id is not ShapeBase.NOT_SET:
                _params['secret_id'] = secret_id
            _request = shapes.CancelRotateSecretRequest(**_params)
        response = self._boto_client.cancel_rotate_secret(**_request.to_boto())

        return shapes.CancelRotateSecretResponse.from_boto(response)

    def create_secret(
        self,
        _request: shapes.CreateSecretRequest = None,
        *,
        name: str,
        client_request_token: str = ShapeBase.NOT_SET,
        description: str = ShapeBase.NOT_SET,
        kms_key_id: str = ShapeBase.NOT_SET,
        secret_binary: typing.Any = ShapeBase.NOT_SET,
        secret_string: str = ShapeBase.NOT_SET,
        tags: typing.List[shapes.Tag] = ShapeBase.NOT_SET,
    ) -> shapes.CreateSecretResponse:
        """
        Creates a new secret. A secret in Secrets Manager consists of both the protected
        secret data and the important information needed to manage the secret.

        Secrets Manager stores the encrypted secret data in one of a collection of
        "versions" associated with the secret. Each version contains a copy of the
        encrypted secret data. Each version is associated with one or more "staging
        labels" that identify where the version is in the rotation cycle. The
        `SecretVersionsToStages` field of the secret contains the mapping of staging
        labels to the active versions of the secret. Versions without a staging label
        are considered deprecated and are not included in the list.

        You provide the secret data to be encrypted by putting text in either the
        `SecretString` parameter or binary data in the `SecretBinary` parameter, but not
        both. If you include `SecretString` or `SecretBinary` then Secrets Manager also
        creates an initial secret version and automatically attaches the staging label
        `AWSCURRENT` to the new version.

          * If you call an operation that needs to encrypt or decrypt the `SecretString` or `SecretBinary` for a secret in the same account as the calling user and that secret doesn't specify a AWS KMS encryption key, Secrets Manager uses the account's default AWS managed customer master key (CMK) with the alias `aws/secretsmanager`. If this key doesn't already exist in your account then Secrets Manager creates it for you automatically. All users in the same AWS account automatically have access to use the default CMK. Note that if an Secrets Manager API call results in AWS having to create the account's AWS-managed CMK, it can result in a one-time significant delay in returning the result.

          * If the secret is in a different AWS account from the credentials calling an API that requires encryption or decryption of the secret value then you must create and use a custom AWS KMS CMK because you can't access the default CMK for the account using credentials from a different AWS account. Store the ARN of the CMK in the secret when you create the secret or when you update it by including it in the `KMSKeyId`. If you call an API that must encrypt or decrypt `SecretString` or `SecretBinary` using credentials from a different account then the AWS KMS key policy must grant cross-account access to that other account's user or role for both the kms:GenerateDataKey and kms:Decrypt operations.

        **Minimum permissions**

        To run this command, you must have the following permissions:

          * secretsmanager:CreateSecret

          * kms:GenerateDataKey - needed only if you use a customer-managed AWS KMS key to encrypt the secret. You do not need this permission to use the account's default AWS managed CMK for Secrets Manager.

          * kms:Decrypt - needed only if you use a customer-managed AWS KMS key to encrypt the secret. You do not need this permission to use the account's default AWS managed CMK for Secrets Manager.

        **Related operations**

          * To delete a secret, use DeleteSecret.

          * To modify an existing secret, use UpdateSecret.

          * To create a new version of a secret, use PutSecretValue.

          * To retrieve the encrypted secure string and secure binary values, use GetSecretValue.

          * To retrieve all other details for a secret, use DescribeSecret. This does not include the encrypted secure string and secure binary values.

          * To retrieve the list of secret versions associated with the current secret, use DescribeSecret and examine the `SecretVersionsToStages` response value.
        """
        if _request is None:
            _params = {}
            if name is not ShapeBase.NOT_SET:
                _params['name'] = name
            if client_request_token is not ShapeBase.NOT_SET:
                _params['client_request_token'] = client_request_token
            if description is not ShapeBase.NOT_SET:
                _params['description'] = description
            if kms_key_id is not ShapeBase.NOT_SET:
                _params['kms_key_id'] = kms_key_id
            if secret_binary is not ShapeBase.NOT_SET:
                _params['secret_binary'] = secret_binary
            if secret_string is not ShapeBase.NOT_SET:
                _params['secret_string'] = secret_string
            if tags is not ShapeBase.NOT_SET:
                _params['tags'] = tags
            _request = shapes.CreateSecretRequest(**_params)
        response = self._boto_client.create_secret(**_request.to_boto())

        return shapes.CreateSecretResponse.from_boto(response)

    def delete_resource_policy(
        self,
        _request: shapes.DeleteResourcePolicyRequest = None,
        *,
        secret_id: str,
    ) -> shapes.DeleteResourcePolicyResponse:
        """
        Deletes the resource-based permission policy that's attached to the secret.

        **Minimum permissions**

        To run this command, you must have the following permissions:

          * secretsmanager:DeleteResourcePolicy

        **Related operations**

          * To attach a resource policy to a secret, use PutResourcePolicy.

          * To retrieve the current resource-based policy that's attached to a secret, use GetResourcePolicy.

          * To list all of the currently available secrets, use ListSecrets.
        """
        if _request is None:
            _params = {}
            if secret_id is not ShapeBase.NOT_SET:
                _params['secret_id'] = secret_id
            _request = shapes.DeleteResourcePolicyRequest(**_params)
        response = self._boto_client.delete_resource_policy(
            **_request.to_boto()
        )

        return shapes.DeleteResourcePolicyResponse.from_boto(response)

    def delete_secret(
        self,
        _request: shapes.DeleteSecretRequest = None,
        *,
        secret_id: str,
        recovery_window_in_days: int = ShapeBase.NOT_SET,
        force_delete_without_recovery: bool = ShapeBase.NOT_SET,
    ) -> shapes.DeleteSecretResponse:
        """
        Deletes an entire secret and all of its versions. You can optionally include a
        recovery window during which you can restore the secret. If you don't specify a
        recovery window value, the operation defaults to 30 days. Secrets Manager
        attaches a `DeletionDate` stamp to the secret that specifies the end of the
        recovery window. At the end of the recovery window, Secrets Manager deletes the
        secret permanently.

        At any time before recovery window ends, you can use RestoreSecret to remove the
        `DeletionDate` and cancel the deletion of the secret.

        You cannot access the encrypted secret information in any secret that is
        scheduled for deletion. If you need to access that information, you must cancel
        the deletion with RestoreSecret and then retrieve the information.

          * There is no explicit operation to delete a version of a secret. Instead, remove all staging labels from the `VersionStage` field of a version. That marks the version as deprecated and allows Secrets Manager to delete it as needed. Versions that do not have any staging labels do not show up in ListSecretVersionIds unless you specify `IncludeDeprecated`.

          * The permanent secret deletion at the end of the waiting period is performed as a background task with low priority. There is no guarantee of a specific time after the recovery window for the actual delete operation to occur.

        **Minimum permissions**

        To run this command, you must have the following permissions:

          * secretsmanager:DeleteSecret

        **Related operations**

          * To create a secret, use CreateSecret.

          * To cancel deletion of a version of a secret before the recovery window has expired, use RestoreSecret.
        """
        if _request is None:
            _params = {}
            if secret_id is not ShapeBase.NOT_SET:
                _params['secret_id'] = secret_id
            if recovery_window_in_days is not ShapeBase.NOT_SET:
                _params['recovery_window_in_days'] = recovery_window_in_days
            if force_delete_without_recovery is not ShapeBase.NOT_SET:
                _params['force_delete_without_recovery'
                       ] = force_delete_without_recovery
            _request = shapes.DeleteSecretRequest(**_params)
        response = self._boto_client.delete_secret(**_request.to_boto())

        return shapes.DeleteSecretResponse.from_boto(response)

    def describe_secret(
        self,
        _request: shapes.DescribeSecretRequest = None,
        *,
        secret_id: str,
    ) -> shapes.DescribeSecretResponse:
        """
        Retrieves the details of a secret. It does not include the encrypted fields.
        Only those fields that are populated with a value are returned in the response.

        **Minimum permissions**

        To run this command, you must have the following permissions:

          * secretsmanager:DescribeSecret

        **Related operations**

          * To create a secret, use CreateSecret.

          * To modify a secret, use UpdateSecret.

          * To retrieve the encrypted secret information in a version of the secret, use GetSecretValue.

          * To list all of the secrets in the AWS account, use ListSecrets.
        """
        if _request is None:
            _params = {}
            if secret_id is not ShapeBase.NOT_SET:
                _params['secret_id'] = secret_id
            _request = shapes.DescribeSecretRequest(**_params)
        response = self._boto_client.describe_secret(**_request.to_boto())

        return shapes.DescribeSecretResponse.from_boto(response)

    def get_random_password(
        self,
        _request: shapes.GetRandomPasswordRequest = None,
        *,
        password_length: int = ShapeBase.NOT_SET,
        exclude_characters: str = ShapeBase.NOT_SET,
        exclude_numbers: bool = ShapeBase.NOT_SET,
        exclude_punctuation: bool = ShapeBase.NOT_SET,
        exclude_uppercase: bool = ShapeBase.NOT_SET,
        exclude_lowercase: bool = ShapeBase.NOT_SET,
        include_space: bool = ShapeBase.NOT_SET,
        require_each_included_type: bool = ShapeBase.NOT_SET,
    ) -> shapes.GetRandomPasswordResponse:
        """
        Generates a random password of the specified complexity. This operation is
        intended for use in the Lambda rotation function. Per best practice, we
        recommend that you specify the maximum length and include every character type
        that the system you are generating a password for can support.

        **Minimum permissions**

        To run this command, you must have the following permissions:

          * secretsmanager:GetRandomPassword
        """
        if _request is None:
            _params = {}
            if password_length is not ShapeBase.NOT_SET:
                _params['password_length'] = password_length
            if exclude_characters is not ShapeBase.NOT_SET:
                _params['exclude_characters'] = exclude_characters
            if exclude_numbers is not ShapeBase.NOT_SET:
                _params['exclude_numbers'] = exclude_numbers
            if exclude_punctuation is not ShapeBase.NOT_SET:
                _params['exclude_punctuation'] = exclude_punctuation
            if exclude_uppercase is not ShapeBase.NOT_SET:
                _params['exclude_uppercase'] = exclude_uppercase
            if exclude_lowercase is not ShapeBase.NOT_SET:
                _params['exclude_lowercase'] = exclude_lowercase
            if include_space is not ShapeBase.NOT_SET:
                _params['include_space'] = include_space
            if require_each_included_type is not ShapeBase.NOT_SET:
                _params['require_each_included_type'
                       ] = require_each_included_type
            _request = shapes.GetRandomPasswordRequest(**_params)
        response = self._boto_client.get_random_password(**_request.to_boto())

        return shapes.GetRandomPasswordResponse.from_boto(response)

    def get_resource_policy(
        self,
        _request: shapes.GetResourcePolicyRequest = None,
        *,
        secret_id: str,
    ) -> shapes.GetResourcePolicyResponse:
        """
        Retrieves the JSON text of the resource-based policy document that's attached to
        the specified secret. The JSON request string input and response output are
        shown formatted with white space and line breaks for better readability. Submit
        your input as a single line JSON string.

        **Minimum permissions**

        To run this command, you must have the following permissions:

          * secretsmanager:GetResourcePolicy

        **Related operations**

          * To attach a resource policy to a secret, use PutResourcePolicy.

          * To delete the resource-based policy that's attached to a secret, use DeleteResourcePolicy.

          * To list all of the currently available secrets, use ListSecrets.
        """
        if _request is None:
            _params = {}
            if secret_id is not ShapeBase.NOT_SET:
                _params['secret_id'] = secret_id
            _request = shapes.GetResourcePolicyRequest(**_params)
        response = self._boto_client.get_resource_policy(**_request.to_boto())

        return shapes.GetResourcePolicyResponse.from_boto(response)

    def get_secret_value(
        self,
        _request: shapes.GetSecretValueRequest = None,
        *,
        secret_id: str,
        version_id: str = ShapeBase.NOT_SET,
        version_stage: str = ShapeBase.NOT_SET,
    ) -> shapes.GetSecretValueResponse:
        """
        Retrieves the contents of the encrypted fields `SecretString` or `SecretBinary`
        from the specified version of a secret, whichever contains content.

        **Minimum permissions**

        To run this command, you must have the following permissions:

          * secretsmanager:GetSecretValue

          * kms:Decrypt - required only if you use a customer-managed AWS KMS key to encrypt the secret. You do not need this permission to use the account's default AWS managed CMK for Secrets Manager.

        **Related operations**

          * To create a new version of the secret with different encrypted information, use PutSecretValue.

          * To retrieve the non-encrypted details for the secret, use DescribeSecret.
        """
        if _request is None:
            _params = {}
            if secret_id is not ShapeBase.NOT_SET:
                _params['secret_id'] = secret_id
            if version_id is not ShapeBase.NOT_SET:
                _params['version_id'] = version_id
            if version_stage is not ShapeBase.NOT_SET:
                _params['version_stage'] = version_stage
            _request = shapes.GetSecretValueRequest(**_params)
        response = self._boto_client.get_secret_value(**_request.to_boto())

        return shapes.GetSecretValueResponse.from_boto(response)

    def list_secret_version_ids(
        self,
        _request: shapes.ListSecretVersionIdsRequest = None,
        *,
        secret_id: str,
        max_results: int = ShapeBase.NOT_SET,
        next_token: str = ShapeBase.NOT_SET,
        include_deprecated: bool = ShapeBase.NOT_SET,
    ) -> shapes.ListSecretVersionIdsResponse:
        """
        Lists all of the versions attached to the specified secret. The output does not
        include the `SecretString` or `SecretBinary` fields. By default, the list
        includes only versions that have at least one staging label in `VersionStage`
        attached.

        Always check the `NextToken` response parameter when calling any of the `List*`
        operations. These operations can occasionally return an empty or shorter than
        expected list of results even when there are more results available. When this
        happens, the `NextToken` response parameter contains a value to pass to the next
        call to the same API to request the next part of the list.

        **Minimum permissions**

        To run this command, you must have the following permissions:

          * secretsmanager:ListSecretVersionIds

        **Related operations**

          * To list the secrets in an account, use ListSecrets.
        """
        if _request is None:
            _params = {}
            if secret_id is not ShapeBase.NOT_SET:
                _params['secret_id'] = secret_id
            if max_results is not ShapeBase.NOT_SET:
                _params['max_results'] = max_results
            if next_token is not ShapeBase.NOT_SET:
                _params['next_token'] = next_token
            if include_deprecated is not ShapeBase.NOT_SET:
                _params['include_deprecated'] = include_deprecated
            _request = shapes.ListSecretVersionIdsRequest(**_params)
        response = self._boto_client.list_secret_version_ids(
            **_request.to_boto()
        )

        return shapes.ListSecretVersionIdsResponse.from_boto(response)

    def list_secrets(
        self,
        _request: shapes.ListSecretsRequest = None,
        *,
        max_results: int = ShapeBase.NOT_SET,
        next_token: str = ShapeBase.NOT_SET,
    ) -> shapes.ListSecretsResponse:
        """
        Lists all of the secrets that are stored by Secrets Manager in the AWS account.
        To list the versions currently stored for a specific secret, use
        ListSecretVersionIds. The encrypted fields `SecretString` and `SecretBinary` are
        not included in the output. To get that information, call the GetSecretValue
        operation.

        Always check the `NextToken` response parameter when calling any of the `List*`
        operations. These operations can occasionally return an empty or shorter than
        expected list of results even when there are more results available. When this
        happens, the `NextToken` response parameter contains a value to pass to the next
        call to the same API to request the next part of the list.

        **Minimum permissions**

        To run this command, you must have the following permissions:

          * secretsmanager:ListSecrets

        **Related operations**

          * To list the versions attached to a secret, use ListSecretVersionIds.
        """
        if _request is None:
            _params = {}
            if max_results is not ShapeBase.NOT_SET:
                _params['max_results'] = max_results
            if next_token is not ShapeBase.NOT_SET:
                _params['next_token'] = next_token
            _request = shapes.ListSecretsRequest(**_params)
        response = self._boto_client.list_secrets(**_request.to_boto())

        return shapes.ListSecretsResponse.from_boto(response)

    def put_resource_policy(
        self,
        _request: shapes.PutResourcePolicyRequest = None,
        *,
        secret_id: str,
        resource_policy: str,
    ) -> shapes.PutResourcePolicyResponse:
        """
        Attaches the contents of the specified resource-based permission policy to a
        secret. A resource-based policy is optional. Alternatively, you can use IAM
        identity-based policies that specify the secret's Amazon Resource Name (ARN) in
        the policy statement's `Resources` element. You can also use a combination of
        both identity-based and resource-based policies. The affected users and roles
        receive the permissions that are permitted by all of the relevant policies. For
        more information, see [Using Resource-Based Policies for AWS Secrets
        Manager](http://docs.aws.amazon.com/secretsmanager/latest/userguide/auth-and-
        access_resource-based-policies.html). For the complete description of the AWS
        policy syntax and grammar, see [IAM JSON Policy
        Reference](http://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies.html)
        in the _IAM User Guide_.

        **Minimum permissions**

        To run this command, you must have the following permissions:

          * secretsmanager:PutResourcePolicy

        **Related operations**

          * To retrieve the resource policy that's attached to a secret, use GetResourcePolicy.

          * To delete the resource-based policy that's attached to a secret, use DeleteResourcePolicy.

          * To list all of the currently available secrets, use ListSecrets.
        """
        if _request is None:
            _params = {}
            if secret_id is not ShapeBase.NOT_SET:
                _params['secret_id'] = secret_id
            if resource_policy is not ShapeBase.NOT_SET:
                _params['resource_policy'] = resource_policy
            _request = shapes.PutResourcePolicyRequest(**_params)
        response = self._boto_client.put_resource_policy(**_request.to_boto())

        return shapes.PutResourcePolicyResponse.from_boto(response)

    def put_secret_value(
        self,
        _request: shapes.PutSecretValueRequest = None,
        *,
        secret_id: str,
        client_request_token: str = ShapeBase.NOT_SET,
        secret_binary: typing.Any = ShapeBase.NOT_SET,
        secret_string: str = ShapeBase.NOT_SET,
        version_stages: typing.List[str] = ShapeBase.NOT_SET,
    ) -> shapes.PutSecretValueResponse:
        """
        Stores a new encrypted secret value in the specified secret. To do this, the
        operation creates a new version and attaches it to the secret. The version can
        contain a new `SecretString` value or a new `SecretBinary` value. You can also
        specify the staging labels that are initially attached to the new version.

        The Secrets Manager console uses only the `SecretString` field. To add binary
        data to a secret with the `SecretBinary` field you must use the AWS CLI or one
        of the AWS SDKs.

          * If this operation creates the first version for the secret then Secrets Manager automatically attaches the staging label `AWSCURRENT` to the new version.

          * If another version of this secret already exists, then this operation does not automatically move any staging labels other than those that you explicitly specify in the `VersionStages` parameter.

          * If this operation moves the staging label `AWSCURRENT` from another version to this version (because you included it in the `StagingLabels` parameter) then Secrets Manager also automatically moves the staging label `AWSPREVIOUS` to the version that `AWSCURRENT` was removed from.

          * This operation is idempotent. If a version with a `VersionId` with the same value as the `ClientRequestToken` parameter already exists and you specify the same secret data, the operation succeeds but does nothing. However, if the secret data is different, then the operation fails because you cannot modify an existing version; you can only create new ones.

          * If you call an operation that needs to encrypt or decrypt the `SecretString` or `SecretBinary` for a secret in the same account as the calling user and that secret doesn't specify a AWS KMS encryption key, Secrets Manager uses the account's default AWS managed customer master key (CMK) with the alias `aws/secretsmanager`. If this key doesn't already exist in your account then Secrets Manager creates it for you automatically. All users in the same AWS account automatically have access to use the default CMK. Note that if an Secrets Manager API call results in AWS having to create the account's AWS-managed CMK, it can result in a one-time significant delay in returning the result.

          * If the secret is in a different AWS account from the credentials calling an API that requires encryption or decryption of the secret value then you must create and use a custom AWS KMS CMK because you can't access the default CMK for the account using credentials from a different AWS account. Store the ARN of the CMK in the secret when you create the secret or when you update it by including it in the `KMSKeyId`. If you call an API that must encrypt or decrypt `SecretString` or `SecretBinary` using credentials from a different account then the AWS KMS key policy must grant cross-account access to that other account's user or role for both the kms:GenerateDataKey and kms:Decrypt operations.

        **Minimum permissions**

        To run this command, you must have the following permissions:

          * secretsmanager:PutSecretValue

          * kms:GenerateDataKey - needed only if you use a customer-managed AWS KMS key to encrypt the secret. You do not need this permission to use the account's default AWS managed CMK for Secrets Manager.

        **Related operations**

          * To retrieve the encrypted value you store in the version of a secret, use GetSecretValue.

          * To create a secret, use CreateSecret.

          * To get the details for a secret, use DescribeSecret.

          * To list the versions attached to a secret, use ListSecretVersionIds.
        """
        if _request is None:
            _params = {}
            if secret_id is not ShapeBase.NOT_SET:
                _params['secret_id'] = secret_id
            if client_request_token is not ShapeBase.NOT_SET:
                _params['client_request_token'] = client_request_token
            if secret_binary is not ShapeBase.NOT_SET:
                _params['secret_binary'] = secret_binary
            if secret_string is not ShapeBase.NOT_SET:
                _params['secret_string'] = secret_string
            if version_stages is not ShapeBase.NOT_SET:
                _params['version_stages'] = version_stages
            _request = shapes.PutSecretValueRequest(**_params)
        response = self._boto_client.put_secret_value(**_request.to_boto())

        return shapes.PutSecretValueResponse.from_boto(response)

    def restore_secret(
        self,
        _request: shapes.RestoreSecretRequest = None,
        *,
        secret_id: str,
    ) -> shapes.RestoreSecretResponse:
        """
        Cancels the scheduled deletion of a secret by removing the `DeletedDate` time
        stamp. This makes the secret accessible to query once again.

        **Minimum permissions**

        To run this command, you must have the following permissions:

          * secretsmanager:RestoreSecret

        **Related operations**

          * To delete a secret, use DeleteSecret.
        """
        if _request is None:
            _params = {}
            if secret_id is not ShapeBase.NOT_SET:
                _params['secret_id'] = secret_id
            _request = shapes.RestoreSecretRequest(**_params)
        response = self._boto_client.restore_secret(**_request.to_boto())

        return shapes.RestoreSecretResponse.from_boto(response)

    def rotate_secret(
        self,
        _request: shapes.RotateSecretRequest = None,
        *,
        secret_id: str,
        client_request_token: str = ShapeBase.NOT_SET,
        rotation_lambda_arn: str = ShapeBase.NOT_SET,
        rotation_rules: shapes.RotationRulesType = ShapeBase.NOT_SET,
    ) -> shapes.RotateSecretResponse:
        """
        Configures and starts the asynchronous process of rotating this secret. If you
        include the configuration parameters, the operation sets those values for the
        secret and then immediately starts a rotation. If you do not include the
        configuration parameters, the operation starts a rotation with the values
        already stored in the secret. After the rotation completes, the protected
        service and its clients all use the new version of the secret.

        This required configuration information includes the ARN of an AWS Lambda
        function and the time between scheduled rotations. The Lambda rotation function
        creates a new version of the secret and creates or updates the credentials on
        the protected service to match. After testing the new credentials, the function
        marks the new secret with the staging label `AWSCURRENT` so that your clients
        all immediately begin to use the new version. For more information about
        rotating secrets and how to configure a Lambda function to rotate the secrets
        for your protected service, see [Rotating Secrets in AWS Secrets
        Manager](http://docs.aws.amazon.com/secretsmanager/latest/userguide/rotating-
        secrets.html) in the _AWS Secrets Manager User Guide_.

        Secrets Manager schedules the next rotation when the previous one is complete.
        Secrets Manager schedules the date by adding the rotation interval (number of
        days) to the actual date of the last rotation. The service chooses the hour
        within that 24-hour date window randomly. The minute is also chosen somewhat
        randomly, but weighted towards the top of the hour and influenced by a variety
        of factors that help distribute load.

        The rotation function must end with the versions of the secret in one of two
        states:

          * The `AWSPENDING` and `AWSCURRENT` staging labels are attached to the same version of the secret, or

          * The `AWSPENDING` staging label is not attached to any version of the secret.

        If instead the `AWSPENDING` staging label is present but is not attached to the
        same version as `AWSCURRENT` then any later invocation of `RotateSecret` assumes
        that a previous rotation request is still in progress and returns an error.

        **Minimum permissions**

        To run this command, you must have the following permissions:

          * secretsmanager:RotateSecret

          * lambda:InvokeFunction (on the function specified in the secret's metadata)

        **Related operations**

          * To list the secrets in your account, use ListSecrets.

          * To get the details for a version of a secret, use DescribeSecret.

          * To create a new version of a secret, use CreateSecret.

          * To attach staging labels to or remove staging labels from a version of a secret, use UpdateSecretVersionStage.
        """
        if _request is None:
            _params = {}
            if secret_id is not ShapeBase.NOT_SET:
                _params['secret_id'] = secret_id
            if client_request_token is not ShapeBase.NOT_SET:
                _params['client_request_token'] = client_request_token
            if rotation_lambda_arn is not ShapeBase.NOT_SET:
                _params['rotation_lambda_arn'] = rotation_lambda_arn
            if rotation_rules is not ShapeBase.NOT_SET:
                _params['rotation_rules'] = rotation_rules
            _request = shapes.RotateSecretRequest(**_params)
        response = self._boto_client.rotate_secret(**_request.to_boto())

        return shapes.RotateSecretResponse.from_boto(response)

    def tag_resource(
        self,
        _request: shapes.TagResourceRequest = None,
        *,
        secret_id: str,
        tags: typing.List[shapes.Tag],
    ) -> None:
        """
        Attaches one or more tags, each consisting of a key name and a value, to the
        specified secret. Tags are part of the secret's overall metadata, and are not
        associated with any specific version of the secret. This operation only appends
        tags to the existing list of tags. To remove tags, you must use UntagResource.

        The following basic restrictions apply to tags:

          * Maximum number of tags per secret—50

          * Maximum key length—127 Unicode characters in UTF-8

          * Maximum value length—255 Unicode characters in UTF-8

          * Tag keys and values are case sensitive.

          * Do not use the `aws:` prefix in your tag names or values because it is reserved for AWS use. You can't edit or delete tag names or values with this prefix. Tags with this prefix do not count against your tags per secret limit.

          * If your tagging schema will be used across multiple services and resources, remember that other services might have restrictions on allowed characters. Generally allowed characters are: letters, spaces, and numbers representable in UTF-8, plus the following special characters: + - = . _ : / @.

        If you use tags as part of your security strategy, then adding or removing a tag
        can change permissions. If successfully completing this operation would result
        in you losing your permissions for this secret, then the operation is blocked
        and returns an Access Denied error.

        **Minimum permissions**

        To run this command, you must have the following permissions:

          * secretsmanager:TagResource

        **Related operations**

          * To remove one or more tags from the collection attached to a secret, use UntagResource.

          * To view the list of tags attached to a secret, use DescribeSecret.
        """
        if _request is None:
            _params = {}
            if secret_id is not ShapeBase.NOT_SET:
                _params['secret_id'] = secret_id
            if tags is not ShapeBase.NOT_SET:
                _params['tags'] = tags
            _request = shapes.TagResourceRequest(**_params)
        response = self._boto_client.tag_resource(**_request.to_boto())

    def untag_resource(
        self,
        _request: shapes.UntagResourceRequest = None,
        *,
        secret_id: str,
        tag_keys: typing.List[str],
    ) -> None:
        """
        Removes one or more tags from the specified secret.

        This operation is idempotent. If a requested tag is not attached to the secret,
        no error is returned and the secret metadata is unchanged.

        If you use tags as part of your security strategy, then removing a tag can
        change permissions. If successfully completing this operation would result in
        you losing your permissions for this secret, then the operation is blocked and
        returns an Access Denied error.

        **Minimum permissions**

        To run this command, you must have the following permissions:

          * secretsmanager:UntagResource

        **Related operations**

          * To add one or more tags to the collection attached to a secret, use TagResource.

          * To view the list of tags attached to a secret, use DescribeSecret.
        """
        if _request is None:
            _params = {}
            if secret_id is not ShapeBase.NOT_SET:
                _params['secret_id'] = secret_id
            if tag_keys is not ShapeBase.NOT_SET:
                _params['tag_keys'] = tag_keys
            _request = shapes.UntagResourceRequest(**_params)
        response = self._boto_client.untag_resource(**_request.to_boto())

    def update_secret(
        self,
        _request: shapes.UpdateSecretRequest = None,
        *,
        secret_id: str,
        client_request_token: str = ShapeBase.NOT_SET,
        description: str = ShapeBase.NOT_SET,
        kms_key_id: str = ShapeBase.NOT_SET,
        secret_binary: typing.Any = ShapeBase.NOT_SET,
        secret_string: str = ShapeBase.NOT_SET,
    ) -> shapes.UpdateSecretResponse:
        """
        Modifies many of the details of the specified secret. If you include a
        `ClientRequestToken` and _either_ `SecretString` or `SecretBinary` then it also
        creates a new version attached to the secret.

        To modify the rotation configuration of a secret, use RotateSecret instead.

        The Secrets Manager console uses only the `SecretString` parameter and therefore
        limits you to encrypting and storing only a text string. To encrypt and store
        binary data as part of the version of a secret, you must use either the AWS CLI
        or one of the AWS SDKs.

          * If a version with a `VersionId` with the same value as the `ClientRequestToken` parameter already exists, the operation results in an error. You cannot modify an existing version, you can only create a new version.

          * If you include `SecretString` or `SecretBinary` to create a new secret version, Secrets Manager automatically attaches the staging label `AWSCURRENT` to the new version. 

          * If you call an operation that needs to encrypt or decrypt the `SecretString` or `SecretBinary` for a secret in the same account as the calling user and that secret doesn't specify a AWS KMS encryption key, Secrets Manager uses the account's default AWS managed customer master key (CMK) with the alias `aws/secretsmanager`. If this key doesn't already exist in your account then Secrets Manager creates it for you automatically. All users in the same AWS account automatically have access to use the default CMK. Note that if an Secrets Manager API call results in AWS having to create the account's AWS-managed CMK, it can result in a one-time significant delay in returning the result.

          * If the secret is in a different AWS account from the credentials calling an API that requires encryption or decryption of the secret value then you must create and use a custom AWS KMS CMK because you can't access the default CMK for the account using credentials from a different AWS account. Store the ARN of the CMK in the secret when you create the secret or when you update it by including it in the `KMSKeyId`. If you call an API that must encrypt or decrypt `SecretString` or `SecretBinary` using credentials from a different account then the AWS KMS key policy must grant cross-account access to that other account's user or role for both the kms:GenerateDataKey and kms:Decrypt operations.

        **Minimum permissions**

        To run this command, you must have the following permissions:

          * secretsmanager:UpdateSecret

          * kms:GenerateDataKey - needed only if you use a custom AWS KMS key to encrypt the secret. You do not need this permission to use the account's AWS managed CMK for Secrets Manager.

          * kms:Decrypt - needed only if you use a custom AWS KMS key to encrypt the secret. You do not need this permission to use the account's AWS managed CMK for Secrets Manager.

        **Related operations**

          * To create a new secret, use CreateSecret.

          * To add only a new version to an existing secret, use PutSecretValue.

          * To get the details for a secret, use DescribeSecret.

          * To list the versions contained in a secret, use ListSecretVersionIds.
        """
        if _request is None:
            _params = {}
            if secret_id is not ShapeBase.NOT_SET:
                _params['secret_id'] = secret_id
            if client_request_token is not ShapeBase.NOT_SET:
                _params['client_request_token'] = client_request_token
            if description is not ShapeBase.NOT_SET:
                _params['description'] = description
            if kms_key_id is not ShapeBase.NOT_SET:
                _params['kms_key_id'] = kms_key_id
            if secret_binary is not ShapeBase.NOT_SET:
                _params['secret_binary'] = secret_binary
            if secret_string is not ShapeBase.NOT_SET:
                _params['secret_string'] = secret_string
            _request = shapes.UpdateSecretRequest(**_params)
        response = self._boto_client.update_secret(**_request.to_boto())

        return shapes.UpdateSecretResponse.from_boto(response)

    def update_secret_version_stage(
        self,
        _request: shapes.UpdateSecretVersionStageRequest = None,
        *,
        secret_id: str,
        version_stage: str,
        remove_from_version_id: str = ShapeBase.NOT_SET,
        move_to_version_id: str = ShapeBase.NOT_SET,
    ) -> shapes.UpdateSecretVersionStageResponse:
        """
        Modifies the staging labels attached to a version of a secret. Staging labels
        are used to track a version as it progresses through the secret rotation
        process. You can attach a staging label to only one version of a secret at a
        time. If a staging label to be added is already attached to another version,
        then it is moved--removed from the other version first and then attached to this
        one. For more information about staging labels, see [Staging
        Labels](http://docs.aws.amazon.com/secretsmanager/latest/userguide/terms-
        concepts.html#term_staging-label) in the _AWS Secrets Manager User Guide_.

        The staging labels that you specify in the `VersionStage` parameter are added to
        the existing list of staging labels--they don't replace it.

        You can move the `AWSCURRENT` staging label to this version by including it in
        this call.

        Whenever you move `AWSCURRENT`, Secrets Manager automatically moves the label
        `AWSPREVIOUS` to the version that `AWSCURRENT` was removed from.

        If this action results in the last label being removed from a version, then the
        version is considered to be 'deprecated' and can be deleted by Secrets Manager.

        **Minimum permissions**

        To run this command, you must have the following permissions:

          * secretsmanager:UpdateSecretVersionStage

        **Related operations**

          * To get the list of staging labels that are currently associated with a version of a secret, use ` DescribeSecret ` and examine the `SecretVersionsToStages` response value.
        """
        if _request is None:
            _params = {}
            if secret_id is not ShapeBase.NOT_SET:
                _params['secret_id'] = secret_id
            if version_stage is not ShapeBase.NOT_SET:
                _params['version_stage'] = version_stage
            if remove_from_version_id is not ShapeBase.NOT_SET:
                _params['remove_from_version_id'] = remove_from_version_id
            if move_to_version_id is not ShapeBase.NOT_SET:
                _params['move_to_version_id'] = move_to_version_id
            _request = shapes.UpdateSecretVersionStageRequest(**_params)
        response = self._boto_client.update_secret_version_stage(
            **_request.to_boto()
        )

        return shapes.UpdateSecretVersionStageResponse.from_boto(response)
