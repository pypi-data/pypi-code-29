import datetime
import typing
import boto3
from autoboto import ClientBase, ShapeBase, OutputShapeBase
from . import shapes


class Client(ClientBase):
    def __init__(self, *args, **kwargs):
        super().__init__("kms", *args, **kwargs)

    def cancel_key_deletion(
        self,
        _request: shapes.CancelKeyDeletionRequest = None,
        *,
        key_id: str,
    ) -> shapes.CancelKeyDeletionResponse:
        """
        Cancels the deletion of a customer master key (CMK). When this operation is
        successful, the CMK is set to the `Disabled` state. To enable a CMK, use
        EnableKey. You cannot perform this operation on a CMK in a different AWS
        account.

        For more information about scheduling and canceling deletion of a CMK, see
        [Deleting Customer Master
        Keys](http://docs.aws.amazon.com/kms/latest/developerguide/deleting-keys.html)
        in the _AWS Key Management Service Developer Guide_.

        The result of this operation varies with the key state of the CMK. For details,
        see [How Key State Affects Use of a Customer Master
        Key](http://docs.aws.amazon.com/kms/latest/developerguide/key-state.html) in the
        _AWS Key Management Service Developer Guide_.
        """
        if _request is None:
            _params = {}
            if key_id is not ShapeBase.NOT_SET:
                _params['key_id'] = key_id
            _request = shapes.CancelKeyDeletionRequest(**_params)
        response = self._boto_client.cancel_key_deletion(**_request.to_boto())

        return shapes.CancelKeyDeletionResponse.from_boto(response)

    def create_alias(
        self,
        _request: shapes.CreateAliasRequest = None,
        *,
        alias_name: str,
        target_key_id: str,
    ) -> None:
        """
        Creates a display name for a customer-managed customer master key (CMK). You can
        use an alias to identify a CMK in selected operations, such as Encrypt and
        GenerateDataKey.

        Each CMK can have multiple aliases, but each alias points to only one CMK. The
        alias name must be unique in the AWS account and region. To simplify code that
        runs in multiple regions, use the same alias name, but point it to a different
        CMK in each region.

        Because an alias is not a property of a CMK, you can delete and change the
        aliases of a CMK without affecting the CMK. Also, aliases do not appear in the
        response from the DescribeKey operation. To get the aliases of all CMKs, use the
        ListAliases operation.

        The alias name can contain only alphanumeric characters, forward slashes (/),
        underscores (_), and dashes (-). Alias names cannot begin with **aws/**. That
        alias name prefix is reserved for AWS managed CMKs.

        The alias and the CMK it is mapped to must be in the same AWS account and the
        same region. You cannot perform this operation on an alias in a different AWS
        account.

        To map an existing alias to a different CMK, call UpdateAlias.

        The result of this operation varies with the key state of the CMK. For details,
        see [How Key State Affects Use of a Customer Master
        Key](http://docs.aws.amazon.com/kms/latest/developerguide/key-state.html) in the
        _AWS Key Management Service Developer Guide_.
        """
        if _request is None:
            _params = {}
            if alias_name is not ShapeBase.NOT_SET:
                _params['alias_name'] = alias_name
            if target_key_id is not ShapeBase.NOT_SET:
                _params['target_key_id'] = target_key_id
            _request = shapes.CreateAliasRequest(**_params)
        response = self._boto_client.create_alias(**_request.to_boto())

    def create_grant(
        self,
        _request: shapes.CreateGrantRequest = None,
        *,
        key_id: str,
        grantee_principal: str,
        operations: typing.List[typing.Union[str, shapes.GrantOperation]],
        retiring_principal: str = ShapeBase.NOT_SET,
        constraints: shapes.GrantConstraints = ShapeBase.NOT_SET,
        grant_tokens: typing.List[str] = ShapeBase.NOT_SET,
        name: str = ShapeBase.NOT_SET,
    ) -> shapes.CreateGrantResponse:
        """
        Adds a grant to a customer master key (CMK). The grant specifies who can use the
        CMK and under what conditions. When setting permissions, grants are an
        alternative to key policies.

        To perform this operation on a CMK in a different AWS account, specify the key
        ARN in the value of the `KeyId` parameter. For more information about grants,
        see [Grants](http://docs.aws.amazon.com/kms/latest/developerguide/grants.html)
        in the _AWS Key Management Service Developer Guide_.

        The result of this operation varies with the key state of the CMK. For details,
        see [How Key State Affects Use of a Customer Master
        Key](http://docs.aws.amazon.com/kms/latest/developerguide/key-state.html) in the
        _AWS Key Management Service Developer Guide_.
        """
        if _request is None:
            _params = {}
            if key_id is not ShapeBase.NOT_SET:
                _params['key_id'] = key_id
            if grantee_principal is not ShapeBase.NOT_SET:
                _params['grantee_principal'] = grantee_principal
            if operations is not ShapeBase.NOT_SET:
                _params['operations'] = operations
            if retiring_principal is not ShapeBase.NOT_SET:
                _params['retiring_principal'] = retiring_principal
            if constraints is not ShapeBase.NOT_SET:
                _params['constraints'] = constraints
            if grant_tokens is not ShapeBase.NOT_SET:
                _params['grant_tokens'] = grant_tokens
            if name is not ShapeBase.NOT_SET:
                _params['name'] = name
            _request = shapes.CreateGrantRequest(**_params)
        response = self._boto_client.create_grant(**_request.to_boto())

        return shapes.CreateGrantResponse.from_boto(response)

    def create_key(
        self,
        _request: shapes.CreateKeyRequest = None,
        *,
        policy: str = ShapeBase.NOT_SET,
        description: str = ShapeBase.NOT_SET,
        key_usage: typing.Union[str, shapes.KeyUsageType] = ShapeBase.NOT_SET,
        origin: typing.Union[str, shapes.OriginType] = ShapeBase.NOT_SET,
        bypass_policy_lockout_safety_check: bool = ShapeBase.NOT_SET,
        tags: typing.List[shapes.Tag] = ShapeBase.NOT_SET,
    ) -> shapes.CreateKeyResponse:
        """
        Creates a customer master key (CMK) in the caller's AWS account.

        You can use a CMK to encrypt small amounts of data (4 KiB or less) directly. But
        CMKs are more commonly used to encrypt data encryption keys (DEKs), which are
        used to encrypt raw data. For more information about DEKs and the difference
        between CMKs and DEKs, see the following:

          * The GenerateDataKey operation

          * [AWS Key Management Service Concepts](http://docs.aws.amazon.com/kms/latest/developerguide/concepts.html) in the _AWS Key Management Service Developer Guide_

        You cannot use this operation to create a CMK in a different AWS account.
        """
        if _request is None:
            _params = {}
            if policy is not ShapeBase.NOT_SET:
                _params['policy'] = policy
            if description is not ShapeBase.NOT_SET:
                _params['description'] = description
            if key_usage is not ShapeBase.NOT_SET:
                _params['key_usage'] = key_usage
            if origin is not ShapeBase.NOT_SET:
                _params['origin'] = origin
            if bypass_policy_lockout_safety_check is not ShapeBase.NOT_SET:
                _params['bypass_policy_lockout_safety_check'
                       ] = bypass_policy_lockout_safety_check
            if tags is not ShapeBase.NOT_SET:
                _params['tags'] = tags
            _request = shapes.CreateKeyRequest(**_params)
        response = self._boto_client.create_key(**_request.to_boto())

        return shapes.CreateKeyResponse.from_boto(response)

    def decrypt(
        self,
        _request: shapes.DecryptRequest = None,
        *,
        ciphertext_blob: typing.Any,
        encryption_context: typing.Dict[str, str] = ShapeBase.NOT_SET,
        grant_tokens: typing.List[str] = ShapeBase.NOT_SET,
    ) -> shapes.DecryptResponse:
        """
        Decrypts ciphertext. Ciphertext is plaintext that has been previously encrypted
        by using any of the following operations:

          * GenerateDataKey

          * GenerateDataKeyWithoutPlaintext

          * Encrypt

        Whenever possible, use key policies to give users permission to call the Decrypt
        operation on the CMK, instead of IAM policies. Otherwise, you might create an
        IAM user policy that gives the user Decrypt permission on all CMKs. This user
        could decrypt ciphertext that was encrypted by CMKs in other accounts if the key
        policy for the cross-account CMK permits it. If you must use an IAM policy for
        `Decrypt` permissions, limit the user to particular CMKs or particular trusted
        accounts.

        The result of this operation varies with the key state of the CMK. For details,
        see [How Key State Affects Use of a Customer Master
        Key](http://docs.aws.amazon.com/kms/latest/developerguide/key-state.html) in the
        _AWS Key Management Service Developer Guide_.
        """
        if _request is None:
            _params = {}
            if ciphertext_blob is not ShapeBase.NOT_SET:
                _params['ciphertext_blob'] = ciphertext_blob
            if encryption_context is not ShapeBase.NOT_SET:
                _params['encryption_context'] = encryption_context
            if grant_tokens is not ShapeBase.NOT_SET:
                _params['grant_tokens'] = grant_tokens
            _request = shapes.DecryptRequest(**_params)
        response = self._boto_client.decrypt(**_request.to_boto())

        return shapes.DecryptResponse.from_boto(response)

    def delete_alias(
        self,
        _request: shapes.DeleteAliasRequest = None,
        *,
        alias_name: str,
    ) -> None:
        """
        Deletes the specified alias. You cannot perform this operation on an alias in a
        different AWS account.

        Because an alias is not a property of a CMK, you can delete and change the
        aliases of a CMK without affecting the CMK. Also, aliases do not appear in the
        response from the DescribeKey operation. To get the aliases of all CMKs, use the
        ListAliases operation.

        Each CMK can have multiple aliases. To change the alias of a CMK, use
        DeleteAlias to delete the current alias and CreateAlias to create a new alias.
        To associate an existing alias with a different customer master key (CMK), call
        UpdateAlias.
        """
        if _request is None:
            _params = {}
            if alias_name is not ShapeBase.NOT_SET:
                _params['alias_name'] = alias_name
            _request = shapes.DeleteAliasRequest(**_params)
        response = self._boto_client.delete_alias(**_request.to_boto())

    def delete_imported_key_material(
        self,
        _request: shapes.DeleteImportedKeyMaterialRequest = None,
        *,
        key_id: str,
    ) -> None:
        """
        Deletes key material that you previously imported. This operation makes the
        specified customer master key (CMK) unusable. For more information about
        importing key material into AWS KMS, see [Importing Key
        Material](http://docs.aws.amazon.com/kms/latest/developerguide/importing-
        keys.html) in the _AWS Key Management Service Developer Guide_. You cannot
        perform this operation on a CMK in a different AWS account.

        When the specified CMK is in the `PendingDeletion` state, this operation does
        not change the CMK's state. Otherwise, it changes the CMK's state to
        `PendingImport`.

        After you delete key material, you can use ImportKeyMaterial to reimport the
        same key material into the CMK.

        The result of this operation varies with the key state of the CMK. For details,
        see [How Key State Affects Use of a Customer Master
        Key](http://docs.aws.amazon.com/kms/latest/developerguide/key-state.html) in the
        _AWS Key Management Service Developer Guide_.
        """
        if _request is None:
            _params = {}
            if key_id is not ShapeBase.NOT_SET:
                _params['key_id'] = key_id
            _request = shapes.DeleteImportedKeyMaterialRequest(**_params)
        response = self._boto_client.delete_imported_key_material(
            **_request.to_boto()
        )

    def describe_key(
        self,
        _request: shapes.DescribeKeyRequest = None,
        *,
        key_id: str,
        grant_tokens: typing.List[str] = ShapeBase.NOT_SET,
    ) -> shapes.DescribeKeyResponse:
        """
        Provides detailed information about the specified customer master key (CMK).

        You can use `DescribeKey` on a predefined AWS alias, that is, an AWS alias with
        no key ID. When you do, AWS KMS associates the alias with an [AWS managed
        CMK](http://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#master_keys)
        and returns its `KeyId` and `Arn` in the response.

        To perform this operation on a CMK in a different AWS account, specify the key
        ARN or alias ARN in the value of the KeyId parameter.
        """
        if _request is None:
            _params = {}
            if key_id is not ShapeBase.NOT_SET:
                _params['key_id'] = key_id
            if grant_tokens is not ShapeBase.NOT_SET:
                _params['grant_tokens'] = grant_tokens
            _request = shapes.DescribeKeyRequest(**_params)
        response = self._boto_client.describe_key(**_request.to_boto())

        return shapes.DescribeKeyResponse.from_boto(response)

    def disable_key(
        self,
        _request: shapes.DisableKeyRequest = None,
        *,
        key_id: str,
    ) -> None:
        """
        Sets the state of a customer master key (CMK) to disabled, thereby preventing
        its use for cryptographic operations. You cannot perform this operation on a CMK
        in a different AWS account.

        For more information about how key state affects the use of a CMK, see [How Key
        State Affects the Use of a Customer Master
        Key](http://docs.aws.amazon.com/kms/latest/developerguide/key-state.html) in the
        _AWS Key Management Service Developer Guide_.

        The result of this operation varies with the key state of the CMK. For details,
        see [How Key State Affects Use of a Customer Master
        Key](http://docs.aws.amazon.com/kms/latest/developerguide/key-state.html) in the
        _AWS Key Management Service Developer Guide_.
        """
        if _request is None:
            _params = {}
            if key_id is not ShapeBase.NOT_SET:
                _params['key_id'] = key_id
            _request = shapes.DisableKeyRequest(**_params)
        response = self._boto_client.disable_key(**_request.to_boto())

    def disable_key_rotation(
        self,
        _request: shapes.DisableKeyRotationRequest = None,
        *,
        key_id: str,
    ) -> None:
        """
        Disables [automatic rotation of the key
        material](http://docs.aws.amazon.com/kms/latest/developerguide/rotate-keys.html)
        for the specified customer master key (CMK). You cannot perform this operation
        on a CMK in a different AWS account.

        The result of this operation varies with the key state of the CMK. For details,
        see [How Key State Affects Use of a Customer Master
        Key](http://docs.aws.amazon.com/kms/latest/developerguide/key-state.html) in the
        _AWS Key Management Service Developer Guide_.
        """
        if _request is None:
            _params = {}
            if key_id is not ShapeBase.NOT_SET:
                _params['key_id'] = key_id
            _request = shapes.DisableKeyRotationRequest(**_params)
        response = self._boto_client.disable_key_rotation(**_request.to_boto())

    def enable_key(
        self,
        _request: shapes.EnableKeyRequest = None,
        *,
        key_id: str,
    ) -> None:
        """
        Sets the state of a customer master key (CMK) to enabled, thereby permitting its
        use for cryptographic operations. You cannot perform this operation on a CMK in
        a different AWS account.

        The result of this operation varies with the key state of the CMK. For details,
        see [How Key State Affects Use of a Customer Master
        Key](http://docs.aws.amazon.com/kms/latest/developerguide/key-state.html) in the
        _AWS Key Management Service Developer Guide_.
        """
        if _request is None:
            _params = {}
            if key_id is not ShapeBase.NOT_SET:
                _params['key_id'] = key_id
            _request = shapes.EnableKeyRequest(**_params)
        response = self._boto_client.enable_key(**_request.to_boto())

    def enable_key_rotation(
        self,
        _request: shapes.EnableKeyRotationRequest = None,
        *,
        key_id: str,
    ) -> None:
        """
        Enables [automatic rotation of the key
        material](http://docs.aws.amazon.com/kms/latest/developerguide/rotate-keys.html)
        for the specified customer master key (CMK). You cannot perform this operation
        on a CMK in a different AWS account.

        The result of this operation varies with the key state of the CMK. For details,
        see [How Key State Affects Use of a Customer Master
        Key](http://docs.aws.amazon.com/kms/latest/developerguide/key-state.html) in the
        _AWS Key Management Service Developer Guide_.
        """
        if _request is None:
            _params = {}
            if key_id is not ShapeBase.NOT_SET:
                _params['key_id'] = key_id
            _request = shapes.EnableKeyRotationRequest(**_params)
        response = self._boto_client.enable_key_rotation(**_request.to_boto())

    def encrypt(
        self,
        _request: shapes.EncryptRequest = None,
        *,
        key_id: str,
        plaintext: typing.Any,
        encryption_context: typing.Dict[str, str] = ShapeBase.NOT_SET,
        grant_tokens: typing.List[str] = ShapeBase.NOT_SET,
    ) -> shapes.EncryptResponse:
        """
        Encrypts plaintext into ciphertext by using a customer master key (CMK). The
        `Encrypt` operation has two primary use cases:

          * You can encrypt up to 4 kilobytes (4096 bytes) of arbitrary data such as an RSA key, a database password, or other sensitive information.

          * You can use the `Encrypt` operation to move encrypted data from one AWS region to another. In the first region, generate a data key and use the plaintext key to encrypt the data. Then, in the new region, call the `Encrypt` method on same plaintext data key. Now, you can safely move the encrypted data and encrypted data key to the new region, and decrypt in the new region when necessary.

        You don't need use this operation to encrypt a data key within a region. The
        GenerateDataKey and GenerateDataKeyWithoutPlaintext operations return an
        encrypted data key.

        Also, you don't need to use this operation to encrypt data in your application.
        You can use the plaintext and encrypted data keys that the `GenerateDataKey`
        operation returns.

        The result of this operation varies with the key state of the CMK. For details,
        see [How Key State Affects Use of a Customer Master
        Key](http://docs.aws.amazon.com/kms/latest/developerguide/key-state.html) in the
        _AWS Key Management Service Developer Guide_.

        To perform this operation on a CMK in a different AWS account, specify the key
        ARN or alias ARN in the value of the KeyId parameter.
        """
        if _request is None:
            _params = {}
            if key_id is not ShapeBase.NOT_SET:
                _params['key_id'] = key_id
            if plaintext is not ShapeBase.NOT_SET:
                _params['plaintext'] = plaintext
            if encryption_context is not ShapeBase.NOT_SET:
                _params['encryption_context'] = encryption_context
            if grant_tokens is not ShapeBase.NOT_SET:
                _params['grant_tokens'] = grant_tokens
            _request = shapes.EncryptRequest(**_params)
        response = self._boto_client.encrypt(**_request.to_boto())

        return shapes.EncryptResponse.from_boto(response)

    def generate_data_key(
        self,
        _request: shapes.GenerateDataKeyRequest = None,
        *,
        key_id: str,
        encryption_context: typing.Dict[str, str] = ShapeBase.NOT_SET,
        number_of_bytes: int = ShapeBase.NOT_SET,
        key_spec: typing.Union[str, shapes.DataKeySpec] = ShapeBase.NOT_SET,
        grant_tokens: typing.List[str] = ShapeBase.NOT_SET,
    ) -> shapes.GenerateDataKeyResponse:
        """
        Returns a data encryption key that you can use in your application to encrypt
        data locally.

        You must specify the customer master key (CMK) under which to generate the data
        key. You must also specify the length of the data key using either the `KeySpec`
        or `NumberOfBytes` field. You must specify one field or the other, but not both.
        For common key lengths (128-bit and 256-bit symmetric keys), we recommend that
        you use `KeySpec`. To perform this operation on a CMK in a different AWS
        account, specify the key ARN or alias ARN in the value of the KeyId parameter.

        This operation returns a plaintext copy of the data key in the `Plaintext` field
        of the response, and an encrypted copy of the data key in the `CiphertextBlob`
        field. The data key is encrypted under the CMK specified in the `KeyId` field of
        the request.

        We recommend that you use the following pattern to encrypt data locally in your
        application:

          1. Use this operation (`GenerateDataKey`) to get a data encryption key.

          2. Use the plaintext data encryption key (returned in the `Plaintext` field of the response) to encrypt data locally, then erase the plaintext data key from memory.

          3. Store the encrypted data key (returned in the `CiphertextBlob` field of the response) alongside the locally encrypted data.

        To decrypt data locally:

          1. Use the Decrypt operation to decrypt the encrypted data key into a plaintext copy of the data key.

          2. Use the plaintext data key to decrypt data locally, then erase the plaintext data key from memory.

        To return only an encrypted copy of the data key, use
        GenerateDataKeyWithoutPlaintext. To return a random byte string that is
        cryptographically secure, use GenerateRandom.

        If you use the optional `EncryptionContext` field, you must store at least
        enough information to be able to reconstruct the full encryption context when
        you later send the ciphertext to the Decrypt operation. It is a good practice to
        choose an encryption context that you can reconstruct on the fly to better
        secure the ciphertext. For more information, see [Encryption
        Context](http://docs.aws.amazon.com/kms/latest/developerguide/encryption-
        context.html) in the _AWS Key Management Service Developer Guide_.

        The result of this operation varies with the key state of the CMK. For details,
        see [How Key State Affects Use of a Customer Master
        Key](http://docs.aws.amazon.com/kms/latest/developerguide/key-state.html) in the
        _AWS Key Management Service Developer Guide_.
        """
        if _request is None:
            _params = {}
            if key_id is not ShapeBase.NOT_SET:
                _params['key_id'] = key_id
            if encryption_context is not ShapeBase.NOT_SET:
                _params['encryption_context'] = encryption_context
            if number_of_bytes is not ShapeBase.NOT_SET:
                _params['number_of_bytes'] = number_of_bytes
            if key_spec is not ShapeBase.NOT_SET:
                _params['key_spec'] = key_spec
            if grant_tokens is not ShapeBase.NOT_SET:
                _params['grant_tokens'] = grant_tokens
            _request = shapes.GenerateDataKeyRequest(**_params)
        response = self._boto_client.generate_data_key(**_request.to_boto())

        return shapes.GenerateDataKeyResponse.from_boto(response)

    def generate_data_key_without_plaintext(
        self,
        _request: shapes.GenerateDataKeyWithoutPlaintextRequest = None,
        *,
        key_id: str,
        encryption_context: typing.Dict[str, str] = ShapeBase.NOT_SET,
        key_spec: typing.Union[str, shapes.DataKeySpec] = ShapeBase.NOT_SET,
        number_of_bytes: int = ShapeBase.NOT_SET,
        grant_tokens: typing.List[str] = ShapeBase.NOT_SET,
    ) -> shapes.GenerateDataKeyWithoutPlaintextResponse:
        """
        Returns a data encryption key encrypted under a customer master key (CMK). This
        operation is identical to GenerateDataKey but returns only the encrypted copy of
        the data key.

        To perform this operation on a CMK in a different AWS account, specify the key
        ARN or alias ARN in the value of the KeyId parameter.

        This operation is useful in a system that has multiple components with different
        degrees of trust. For example, consider a system that stores encrypted data in
        containers. Each container stores the encrypted data and an encrypted copy of
        the data key. One component of the system, called the _control plane_ , creates
        new containers. When it creates a new container, it uses this operation
        (`GenerateDataKeyWithoutPlaintext`) to get an encrypted data key and then stores
        it in the container. Later, a different component of the system, called the
        _data plane_ , puts encrypted data into the containers. To do this, it passes
        the encrypted data key to the Decrypt operation. It then uses the returned
        plaintext data key to encrypt data and finally stores the encrypted data in the
        container. In this system, the control plane never sees the plaintext data key.

        The result of this operation varies with the key state of the CMK. For details,
        see [How Key State Affects Use of a Customer Master
        Key](http://docs.aws.amazon.com/kms/latest/developerguide/key-state.html) in the
        _AWS Key Management Service Developer Guide_.
        """
        if _request is None:
            _params = {}
            if key_id is not ShapeBase.NOT_SET:
                _params['key_id'] = key_id
            if encryption_context is not ShapeBase.NOT_SET:
                _params['encryption_context'] = encryption_context
            if key_spec is not ShapeBase.NOT_SET:
                _params['key_spec'] = key_spec
            if number_of_bytes is not ShapeBase.NOT_SET:
                _params['number_of_bytes'] = number_of_bytes
            if grant_tokens is not ShapeBase.NOT_SET:
                _params['grant_tokens'] = grant_tokens
            _request = shapes.GenerateDataKeyWithoutPlaintextRequest(**_params)
        response = self._boto_client.generate_data_key_without_plaintext(
            **_request.to_boto()
        )

        return shapes.GenerateDataKeyWithoutPlaintextResponse.from_boto(
            response
        )

    def generate_random(
        self,
        _request: shapes.GenerateRandomRequest = None,
        *,
        number_of_bytes: int = ShapeBase.NOT_SET,
    ) -> shapes.GenerateRandomResponse:
        """
        Returns a random byte string that is cryptographically secure.

        For more information about entropy and random number generation, see the [AWS
        Key Management Service Cryptographic
        Details](https://d0.awsstatic.com/whitepapers/KMS-Cryptographic-Details.pdf)
        whitepaper.
        """
        if _request is None:
            _params = {}
            if number_of_bytes is not ShapeBase.NOT_SET:
                _params['number_of_bytes'] = number_of_bytes
            _request = shapes.GenerateRandomRequest(**_params)
        response = self._boto_client.generate_random(**_request.to_boto())

        return shapes.GenerateRandomResponse.from_boto(response)

    def get_key_policy(
        self,
        _request: shapes.GetKeyPolicyRequest = None,
        *,
        key_id: str,
        policy_name: str,
    ) -> shapes.GetKeyPolicyResponse:
        """
        Gets a key policy attached to the specified customer master key (CMK). You
        cannot perform this operation on a CMK in a different AWS account.
        """
        if _request is None:
            _params = {}
            if key_id is not ShapeBase.NOT_SET:
                _params['key_id'] = key_id
            if policy_name is not ShapeBase.NOT_SET:
                _params['policy_name'] = policy_name
            _request = shapes.GetKeyPolicyRequest(**_params)
        response = self._boto_client.get_key_policy(**_request.to_boto())

        return shapes.GetKeyPolicyResponse.from_boto(response)

    def get_key_rotation_status(
        self,
        _request: shapes.GetKeyRotationStatusRequest = None,
        *,
        key_id: str,
    ) -> shapes.GetKeyRotationStatusResponse:
        """
        Gets a Boolean value that indicates whether [automatic rotation of the key
        material](http://docs.aws.amazon.com/kms/latest/developerguide/rotate-keys.html)
        is enabled for the specified customer master key (CMK).

        The result of this operation varies with the key state of the CMK. For details,
        see [How Key State Affects Use of a Customer Master
        Key](http://docs.aws.amazon.com/kms/latest/developerguide/key-state.html) in the
        _AWS Key Management Service Developer Guide_.

          * Disabled: The key rotation status does not change when you disable a CMK. However, while the CMK is disabled, AWS KMS does not rotate the backing key.

          * Pending deletion: While a CMK is pending deletion, its key rotation status is `false` and AWS KMS does not rotate the backing key. If you cancel the deletion, the original key rotation status is restored.

        To perform this operation on a CMK in a different AWS account, specify the key
        ARN in the value of the `KeyId` parameter.
        """
        if _request is None:
            _params = {}
            if key_id is not ShapeBase.NOT_SET:
                _params['key_id'] = key_id
            _request = shapes.GetKeyRotationStatusRequest(**_params)
        response = self._boto_client.get_key_rotation_status(
            **_request.to_boto()
        )

        return shapes.GetKeyRotationStatusResponse.from_boto(response)

    def get_parameters_for_import(
        self,
        _request: shapes.GetParametersForImportRequest = None,
        *,
        key_id: str,
        wrapping_algorithm: typing.Union[str, shapes.AlgorithmSpec],
        wrapping_key_spec: typing.Union[str, shapes.WrappingKeySpec],
    ) -> shapes.GetParametersForImportResponse:
        """
        Returns the items you need in order to import key material into AWS KMS from
        your existing key management infrastructure. For more information about
        importing key material into AWS KMS, see [Importing Key
        Material](http://docs.aws.amazon.com/kms/latest/developerguide/importing-
        keys.html) in the _AWS Key Management Service Developer Guide_.

        You must specify the key ID of the customer master key (CMK) into which you will
        import key material. This CMK's `Origin` must be `EXTERNAL`. You must also
        specify the wrapping algorithm and type of wrapping key (public key) that you
        will use to encrypt the key material. You cannot perform this operation on a CMK
        in a different AWS account.

        This operation returns a public key and an import token. Use the public key to
        encrypt the key material. Store the import token to send with a subsequent
        ImportKeyMaterial request. The public key and import token from the same
        response must be used together. These items are valid for 24 hours. When they
        expire, they cannot be used for a subsequent ImportKeyMaterial request. To get
        new ones, send another `GetParametersForImport` request.

        The result of this operation varies with the key state of the CMK. For details,
        see [How Key State Affects Use of a Customer Master
        Key](http://docs.aws.amazon.com/kms/latest/developerguide/key-state.html) in the
        _AWS Key Management Service Developer Guide_.
        """
        if _request is None:
            _params = {}
            if key_id is not ShapeBase.NOT_SET:
                _params['key_id'] = key_id
            if wrapping_algorithm is not ShapeBase.NOT_SET:
                _params['wrapping_algorithm'] = wrapping_algorithm
            if wrapping_key_spec is not ShapeBase.NOT_SET:
                _params['wrapping_key_spec'] = wrapping_key_spec
            _request = shapes.GetParametersForImportRequest(**_params)
        response = self._boto_client.get_parameters_for_import(
            **_request.to_boto()
        )

        return shapes.GetParametersForImportResponse.from_boto(response)

    def import_key_material(
        self,
        _request: shapes.ImportKeyMaterialRequest = None,
        *,
        key_id: str,
        import_token: typing.Any,
        encrypted_key_material: typing.Any,
        valid_to: datetime.datetime = ShapeBase.NOT_SET,
        expiration_model: typing.Union[str, shapes.
                                       ExpirationModelType] = ShapeBase.NOT_SET,
    ) -> shapes.ImportKeyMaterialResponse:
        """
        Imports key material into an existing AWS KMS customer master key (CMK) that was
        created without key material. You cannot perform this operation on a CMK in a
        different AWS account. For more information about creating CMKs with no key
        material and then importing key material, see [Importing Key
        Material](http://docs.aws.amazon.com/kms/latest/developerguide/importing-
        keys.html) in the _AWS Key Management Service Developer Guide_.

        Before using this operation, call GetParametersForImport. Its response includes
        a public key and an import token. Use the public key to encrypt the key
        material. Then, submit the import token from the same `GetParametersForImport`
        response.

        When calling this operation, you must specify the following values:

          * The key ID or key ARN of a CMK with no key material. Its `Origin` must be `EXTERNAL`.

        To create a CMK with no key material, call CreateKey and set the value of its
        `Origin` parameter to `EXTERNAL`. To get the `Origin` of a CMK, call
        DescribeKey.)

          * The encrypted key material. To get the public key to encrypt the key material, call GetParametersForImport.

          * The import token that GetParametersForImport returned. This token and the public key used to encrypt the key material must have come from the same response.

          * Whether the key material expires and if so, when. If you set an expiration date, you can change it only by reimporting the same key material and specifying a new expiration date. If the key material expires, AWS KMS deletes the key material and the CMK becomes unusable. To use the CMK again, you must reimport the same key material.

        When this operation is successful, the CMK's key state changes from
        `PendingImport` to `Enabled`, and you can use the CMK. After you successfully
        import key material into a CMK, you can reimport the same key material into that
        CMK, but you cannot import different key material.

        The result of this operation varies with the key state of the CMK. For details,
        see [How Key State Affects Use of a Customer Master
        Key](http://docs.aws.amazon.com/kms/latest/developerguide/key-state.html) in the
        _AWS Key Management Service Developer Guide_.
        """
        if _request is None:
            _params = {}
            if key_id is not ShapeBase.NOT_SET:
                _params['key_id'] = key_id
            if import_token is not ShapeBase.NOT_SET:
                _params['import_token'] = import_token
            if encrypted_key_material is not ShapeBase.NOT_SET:
                _params['encrypted_key_material'] = encrypted_key_material
            if valid_to is not ShapeBase.NOT_SET:
                _params['valid_to'] = valid_to
            if expiration_model is not ShapeBase.NOT_SET:
                _params['expiration_model'] = expiration_model
            _request = shapes.ImportKeyMaterialRequest(**_params)
        response = self._boto_client.import_key_material(**_request.to_boto())

        return shapes.ImportKeyMaterialResponse.from_boto(response)

    def list_aliases(
        self,
        _request: shapes.ListAliasesRequest = None,
        *,
        key_id: str = ShapeBase.NOT_SET,
        limit: int = ShapeBase.NOT_SET,
        marker: str = ShapeBase.NOT_SET,
    ) -> shapes.ListAliasesResponse:
        """
        Gets a list of aliases in the caller's AWS account and region. You cannot list
        aliases in other accounts. For more information about aliases, see CreateAlias.

        By default, the ListAliases command returns all aliases in the account and
        region. To get only the aliases that point to a particular customer master key
        (CMK), use the `KeyId` parameter.

        The `ListAliases` response can include aliases that you created and associated
        with your customer managed CMKs, and aliases that AWS created and associated
        with AWS managed CMKs in your account. You can recognize AWS aliases because
        their names have the format `aws/<service-name>`, such as `aws/dynamodb`.

        The response might also include aliases that have no `TargetKeyId` field. These
        are predefined aliases that AWS has created but has not yet associated with a
        CMK. Aliases that AWS creates in your account, including predefined aliases, do
        not count against your [AWS KMS aliases
        limit](http://docs.aws.amazon.com/kms/latest/developerguide/limits.html#aliases-
        limit).
        """
        if _request is None:
            _params = {}
            if key_id is not ShapeBase.NOT_SET:
                _params['key_id'] = key_id
            if limit is not ShapeBase.NOT_SET:
                _params['limit'] = limit
            if marker is not ShapeBase.NOT_SET:
                _params['marker'] = marker
            _request = shapes.ListAliasesRequest(**_params)
        paginator = self.get_paginator("list_aliases").paginate(
            **_request.to_boto()
        )
        page_generator = (page for page in paginator)
        first_page = next(page_generator)
        result = shapes.ListAliasesResponse.from_boto(first_page)
        result._page_iterator = page_generator
        return result

        return shapes.ListAliasesResponse.from_boto(response)

    def list_grants(
        self,
        _request: shapes.ListGrantsRequest = None,
        *,
        key_id: str,
        limit: int = ShapeBase.NOT_SET,
        marker: str = ShapeBase.NOT_SET,
    ) -> shapes.ListGrantsResponse:
        """
        Gets a list of all grants for the specified customer master key (CMK).

        To perform this operation on a CMK in a different AWS account, specify the key
        ARN in the value of the `KeyId` parameter.
        """
        if _request is None:
            _params = {}
            if key_id is not ShapeBase.NOT_SET:
                _params['key_id'] = key_id
            if limit is not ShapeBase.NOT_SET:
                _params['limit'] = limit
            if marker is not ShapeBase.NOT_SET:
                _params['marker'] = marker
            _request = shapes.ListGrantsRequest(**_params)
        paginator = self.get_paginator("list_grants").paginate(
            **_request.to_boto()
        )
        page_generator = (page for page in paginator)
        first_page = next(page_generator)
        result = shapes.ListGrantsResponse.from_boto(first_page)
        result._page_iterator = page_generator
        return result

        return shapes.ListGrantsResponse.from_boto(response)

    def list_key_policies(
        self,
        _request: shapes.ListKeyPoliciesRequest = None,
        *,
        key_id: str,
        limit: int = ShapeBase.NOT_SET,
        marker: str = ShapeBase.NOT_SET,
    ) -> shapes.ListKeyPoliciesResponse:
        """
        Gets the names of the key policies that are attached to a customer master key
        (CMK). This operation is designed to get policy names that you can use in a
        GetKeyPolicy operation. However, the only valid policy name is `default`. You
        cannot perform this operation on a CMK in a different AWS account.
        """
        if _request is None:
            _params = {}
            if key_id is not ShapeBase.NOT_SET:
                _params['key_id'] = key_id
            if limit is not ShapeBase.NOT_SET:
                _params['limit'] = limit
            if marker is not ShapeBase.NOT_SET:
                _params['marker'] = marker
            _request = shapes.ListKeyPoliciesRequest(**_params)
        paginator = self.get_paginator("list_key_policies").paginate(
            **_request.to_boto()
        )
        page_generator = (page for page in paginator)
        first_page = next(page_generator)
        result = shapes.ListKeyPoliciesResponse.from_boto(first_page)
        result._page_iterator = page_generator
        return result

        return shapes.ListKeyPoliciesResponse.from_boto(response)

    def list_keys(
        self,
        _request: shapes.ListKeysRequest = None,
        *,
        limit: int = ShapeBase.NOT_SET,
        marker: str = ShapeBase.NOT_SET,
    ) -> shapes.ListKeysResponse:
        """
        Gets a list of all customer master keys (CMKs) in the caller's AWS account and
        region.
        """
        if _request is None:
            _params = {}
            if limit is not ShapeBase.NOT_SET:
                _params['limit'] = limit
            if marker is not ShapeBase.NOT_SET:
                _params['marker'] = marker
            _request = shapes.ListKeysRequest(**_params)
        paginator = self.get_paginator("list_keys").paginate(
            **_request.to_boto()
        )
        page_generator = (page for page in paginator)
        first_page = next(page_generator)
        result = shapes.ListKeysResponse.from_boto(first_page)
        result._page_iterator = page_generator
        return result

        return shapes.ListKeysResponse.from_boto(response)

    def list_resource_tags(
        self,
        _request: shapes.ListResourceTagsRequest = None,
        *,
        key_id: str,
        limit: int = ShapeBase.NOT_SET,
        marker: str = ShapeBase.NOT_SET,
    ) -> shapes.ListResourceTagsResponse:
        """
        Returns a list of all tags for the specified customer master key (CMK).

        You cannot perform this operation on a CMK in a different AWS account.
        """
        if _request is None:
            _params = {}
            if key_id is not ShapeBase.NOT_SET:
                _params['key_id'] = key_id
            if limit is not ShapeBase.NOT_SET:
                _params['limit'] = limit
            if marker is not ShapeBase.NOT_SET:
                _params['marker'] = marker
            _request = shapes.ListResourceTagsRequest(**_params)
        response = self._boto_client.list_resource_tags(**_request.to_boto())

        return shapes.ListResourceTagsResponse.from_boto(response)

    def list_retirable_grants(
        self,
        _request: shapes.ListRetirableGrantsRequest = None,
        *,
        retiring_principal: str,
        limit: int = ShapeBase.NOT_SET,
        marker: str = ShapeBase.NOT_SET,
    ) -> shapes.ListGrantsResponse:
        """
        Returns a list of all grants for which the grant's `RetiringPrincipal` matches
        the one specified.

        A typical use is to list all grants that you are able to retire. To retire a
        grant, use RetireGrant.
        """
        if _request is None:
            _params = {}
            if retiring_principal is not ShapeBase.NOT_SET:
                _params['retiring_principal'] = retiring_principal
            if limit is not ShapeBase.NOT_SET:
                _params['limit'] = limit
            if marker is not ShapeBase.NOT_SET:
                _params['marker'] = marker
            _request = shapes.ListRetirableGrantsRequest(**_params)
        response = self._boto_client.list_retirable_grants(**_request.to_boto())

        return shapes.ListGrantsResponse.from_boto(response)

    def put_key_policy(
        self,
        _request: shapes.PutKeyPolicyRequest = None,
        *,
        key_id: str,
        policy_name: str,
        policy: str,
        bypass_policy_lockout_safety_check: bool = ShapeBase.NOT_SET,
    ) -> None:
        """
        Attaches a key policy to the specified customer master key (CMK). You cannot
        perform this operation on a CMK in a different AWS account.

        For more information about key policies, see [Key
        Policies](http://docs.aws.amazon.com/kms/latest/developerguide/key-
        policies.html) in the _AWS Key Management Service Developer Guide_.
        """
        if _request is None:
            _params = {}
            if key_id is not ShapeBase.NOT_SET:
                _params['key_id'] = key_id
            if policy_name is not ShapeBase.NOT_SET:
                _params['policy_name'] = policy_name
            if policy is not ShapeBase.NOT_SET:
                _params['policy'] = policy
            if bypass_policy_lockout_safety_check is not ShapeBase.NOT_SET:
                _params['bypass_policy_lockout_safety_check'
                       ] = bypass_policy_lockout_safety_check
            _request = shapes.PutKeyPolicyRequest(**_params)
        response = self._boto_client.put_key_policy(**_request.to_boto())

    def re_encrypt(
        self,
        _request: shapes.ReEncryptRequest = None,
        *,
        ciphertext_blob: typing.Any,
        destination_key_id: str,
        source_encryption_context: typing.Dict[str, str] = ShapeBase.NOT_SET,
        destination_encryption_context: typing.Dict[str, str] = ShapeBase.
        NOT_SET,
        grant_tokens: typing.List[str] = ShapeBase.NOT_SET,
    ) -> shapes.ReEncryptResponse:
        """
        Encrypts data on the server side with a new customer master key (CMK) without
        exposing the plaintext of the data on the client side. The data is first
        decrypted and then reencrypted. You can also use this operation to change the
        encryption context of a ciphertext.

        You can reencrypt data using CMKs in different AWS accounts.

        Unlike other operations, `ReEncrypt` is authorized twice, once as
        `ReEncryptFrom` on the source CMK and once as `ReEncryptTo` on the destination
        CMK. We recommend that you include the `"kms:ReEncrypt*"` permission in your
        [key policies](http://docs.aws.amazon.com/kms/latest/developerguide/key-
        policies.html) to permit reencryption from or to the CMK. This permission is
        automatically included in the key policy when you create a CMK through the
        console. But you must include it manually when you create a CMK programmatically
        or when you set a key policy with the PutKeyPolicy operation.

        The result of this operation varies with the key state of the CMK. For details,
        see [How Key State Affects Use of a Customer Master
        Key](http://docs.aws.amazon.com/kms/latest/developerguide/key-state.html) in the
        _AWS Key Management Service Developer Guide_.
        """
        if _request is None:
            _params = {}
            if ciphertext_blob is not ShapeBase.NOT_SET:
                _params['ciphertext_blob'] = ciphertext_blob
            if destination_key_id is not ShapeBase.NOT_SET:
                _params['destination_key_id'] = destination_key_id
            if source_encryption_context is not ShapeBase.NOT_SET:
                _params['source_encryption_context'] = source_encryption_context
            if destination_encryption_context is not ShapeBase.NOT_SET:
                _params['destination_encryption_context'
                       ] = destination_encryption_context
            if grant_tokens is not ShapeBase.NOT_SET:
                _params['grant_tokens'] = grant_tokens
            _request = shapes.ReEncryptRequest(**_params)
        response = self._boto_client.re_encrypt(**_request.to_boto())

        return shapes.ReEncryptResponse.from_boto(response)

    def retire_grant(
        self,
        _request: shapes.RetireGrantRequest = None,
        *,
        grant_token: str = ShapeBase.NOT_SET,
        key_id: str = ShapeBase.NOT_SET,
        grant_id: str = ShapeBase.NOT_SET,
    ) -> None:
        """
        Retires a grant. To clean up, you can retire a grant when you're done using it.
        You should revoke a grant when you intend to actively deny operations that
        depend on it. The following are permitted to call this API:

          * The AWS account (root user) under which the grant was created

          * The `RetiringPrincipal`, if present in the grant

          * The `GranteePrincipal`, if `RetireGrant` is an operation specified in the grant

        You must identify the grant to retire by its grant token or by a combination of
        the grant ID and the Amazon Resource Name (ARN) of the customer master key
        (CMK). A grant token is a unique variable-length base64-encoded string. A grant
        ID is a 64 character unique identifier of a grant. The CreateGrant operation
        returns both.
        """
        if _request is None:
            _params = {}
            if grant_token is not ShapeBase.NOT_SET:
                _params['grant_token'] = grant_token
            if key_id is not ShapeBase.NOT_SET:
                _params['key_id'] = key_id
            if grant_id is not ShapeBase.NOT_SET:
                _params['grant_id'] = grant_id
            _request = shapes.RetireGrantRequest(**_params)
        response = self._boto_client.retire_grant(**_request.to_boto())

    def revoke_grant(
        self,
        _request: shapes.RevokeGrantRequest = None,
        *,
        key_id: str,
        grant_id: str,
    ) -> None:
        """
        Revokes the specified grant for the specified customer master key (CMK). You can
        revoke a grant to actively deny operations that depend on it.

        To perform this operation on a CMK in a different AWS account, specify the key
        ARN in the value of the `KeyId` parameter.
        """
        if _request is None:
            _params = {}
            if key_id is not ShapeBase.NOT_SET:
                _params['key_id'] = key_id
            if grant_id is not ShapeBase.NOT_SET:
                _params['grant_id'] = grant_id
            _request = shapes.RevokeGrantRequest(**_params)
        response = self._boto_client.revoke_grant(**_request.to_boto())

    def schedule_key_deletion(
        self,
        _request: shapes.ScheduleKeyDeletionRequest = None,
        *,
        key_id: str,
        pending_window_in_days: int = ShapeBase.NOT_SET,
    ) -> shapes.ScheduleKeyDeletionResponse:
        """
        Schedules the deletion of a customer master key (CMK). You may provide a waiting
        period, specified in days, before deletion occurs. If you do not provide a
        waiting period, the default period of 30 days is used. When this operation is
        successful, the state of the CMK changes to `PendingDeletion`. Before the
        waiting period ends, you can use CancelKeyDeletion to cancel the deletion of the
        CMK. After the waiting period ends, AWS KMS deletes the CMK and all AWS KMS data
        associated with it, including all aliases that refer to it.

        You cannot perform this operation on a CMK in a different AWS account.

        Deleting a CMK is a destructive and potentially dangerous operation. When a CMK
        is deleted, all data that was encrypted under the CMK is rendered unrecoverable.
        To restrict the use of a CMK without deleting it, use DisableKey.

        For more information about scheduling a CMK for deletion, see [Deleting Customer
        Master Keys](http://docs.aws.amazon.com/kms/latest/developerguide/deleting-
        keys.html) in the _AWS Key Management Service Developer Guide_.

        The result of this operation varies with the key state of the CMK. For details,
        see [How Key State Affects Use of a Customer Master
        Key](http://docs.aws.amazon.com/kms/latest/developerguide/key-state.html) in the
        _AWS Key Management Service Developer Guide_.
        """
        if _request is None:
            _params = {}
            if key_id is not ShapeBase.NOT_SET:
                _params['key_id'] = key_id
            if pending_window_in_days is not ShapeBase.NOT_SET:
                _params['pending_window_in_days'] = pending_window_in_days
            _request = shapes.ScheduleKeyDeletionRequest(**_params)
        response = self._boto_client.schedule_key_deletion(**_request.to_boto())

        return shapes.ScheduleKeyDeletionResponse.from_boto(response)

    def tag_resource(
        self,
        _request: shapes.TagResourceRequest = None,
        *,
        key_id: str,
        tags: typing.List[shapes.Tag],
    ) -> None:
        """
        Adds or edits tags for a customer master key (CMK). You cannot perform this
        operation on a CMK in a different AWS account.

        Each tag consists of a tag key and a tag value. Tag keys and tag values are both
        required, but tag values can be empty (null) strings.

        You can only use a tag key once for each CMK. If you use the tag key again, AWS
        KMS replaces the current tag value with the specified value.

        For information about the rules that apply to tag keys and tag values, see
        [User-Defined Tag
        Restrictions](http://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/allocation-
        tag-restrictions.html) in the _AWS Billing and Cost Management User Guide_.

        The result of this operation varies with the key state of the CMK. For details,
        see [How Key State Affects Use of a Customer Master
        Key](http://docs.aws.amazon.com/kms/latest/developerguide/key-state.html) in the
        _AWS Key Management Service Developer Guide_.
        """
        if _request is None:
            _params = {}
            if key_id is not ShapeBase.NOT_SET:
                _params['key_id'] = key_id
            if tags is not ShapeBase.NOT_SET:
                _params['tags'] = tags
            _request = shapes.TagResourceRequest(**_params)
        response = self._boto_client.tag_resource(**_request.to_boto())

    def untag_resource(
        self,
        _request: shapes.UntagResourceRequest = None,
        *,
        key_id: str,
        tag_keys: typing.List[str],
    ) -> None:
        """
        Removes the specified tags from the specified customer master key (CMK). You
        cannot perform this operation on a CMK in a different AWS account.

        To remove a tag, specify the tag key. To change the tag value of an existing tag
        key, use TagResource.

        The result of this operation varies with the key state of the CMK. For details,
        see [How Key State Affects Use of a Customer Master
        Key](http://docs.aws.amazon.com/kms/latest/developerguide/key-state.html) in the
        _AWS Key Management Service Developer Guide_.
        """
        if _request is None:
            _params = {}
            if key_id is not ShapeBase.NOT_SET:
                _params['key_id'] = key_id
            if tag_keys is not ShapeBase.NOT_SET:
                _params['tag_keys'] = tag_keys
            _request = shapes.UntagResourceRequest(**_params)
        response = self._boto_client.untag_resource(**_request.to_boto())

    def update_alias(
        self,
        _request: shapes.UpdateAliasRequest = None,
        *,
        alias_name: str,
        target_key_id: str,
    ) -> None:
        """
        Associates an existing alias with a different customer master key (CMK). Each
        CMK can have multiple aliases, but the aliases must be unique within the account
        and region. You cannot perform this operation on an alias in a different AWS
        account.

        This operation works only on existing aliases. To change the alias of a CMK to a
        new value, use CreateAlias to create a new alias and DeleteAlias to delete the
        old alias.

        Because an alias is not a property of a CMK, you can create, update, and delete
        the aliases of a CMK without affecting the CMK. Also, aliases do not appear in
        the response from the DescribeKey operation. To get the aliases of all CMKs in
        the account, use the ListAliases operation.

        An alias name can contain only alphanumeric characters, forward slashes (/),
        underscores (_), and dashes (-). An alias must start with the word `alias`
        followed by a forward slash (`alias/`). The alias name can contain only
        alphanumeric characters, forward slashes (/), underscores (_), and dashes (-).
        Alias names cannot begin with `aws`; that alias name prefix is reserved by
        Amazon Web Services (AWS).

        The result of this operation varies with the key state of the CMK. For details,
        see [How Key State Affects Use of a Customer Master
        Key](http://docs.aws.amazon.com/kms/latest/developerguide/key-state.html) in the
        _AWS Key Management Service Developer Guide_.
        """
        if _request is None:
            _params = {}
            if alias_name is not ShapeBase.NOT_SET:
                _params['alias_name'] = alias_name
            if target_key_id is not ShapeBase.NOT_SET:
                _params['target_key_id'] = target_key_id
            _request = shapes.UpdateAliasRequest(**_params)
        response = self._boto_client.update_alias(**_request.to_boto())

    def update_key_description(
        self,
        _request: shapes.UpdateKeyDescriptionRequest = None,
        *,
        key_id: str,
        description: str,
    ) -> None:
        """
        Updates the description of a customer master key (CMK). To see the description
        of a CMK, use DescribeKey.

        You cannot perform this operation on a CMK in a different AWS account.

        The result of this operation varies with the key state of the CMK. For details,
        see [How Key State Affects Use of a Customer Master
        Key](http://docs.aws.amazon.com/kms/latest/developerguide/key-state.html) in the
        _AWS Key Management Service Developer Guide_.
        """
        if _request is None:
            _params = {}
            if key_id is not ShapeBase.NOT_SET:
                _params['key_id'] = key_id
            if description is not ShapeBase.NOT_SET:
                _params['description'] = description
            _request = shapes.UpdateKeyDescriptionRequest(**_params)
        response = self._boto_client.update_key_description(
            **_request.to_boto()
        )
