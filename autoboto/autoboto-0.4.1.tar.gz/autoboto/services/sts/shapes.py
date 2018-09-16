import datetime
import typing
from autoboto import ShapeBase, OutputShapeBase, TypeInfo
import dataclasses


@dataclasses.dataclass
class AssumeRoleRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "role_arn",
                "RoleArn",
                TypeInfo(str),
            ),
            (
                "role_session_name",
                "RoleSessionName",
                TypeInfo(str),
            ),
            (
                "policy",
                "Policy",
                TypeInfo(str),
            ),
            (
                "duration_seconds",
                "DurationSeconds",
                TypeInfo(int),
            ),
            (
                "external_id",
                "ExternalId",
                TypeInfo(str),
            ),
            (
                "serial_number",
                "SerialNumber",
                TypeInfo(str),
            ),
            (
                "token_code",
                "TokenCode",
                TypeInfo(str),
            ),
        ]

    # The Amazon Resource Name (ARN) of the role to assume.
    role_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # An identifier for the assumed role session.

    # Use the role session name to uniquely identify a session when the same role
    # is assumed by different principals or for different reasons. In cross-
    # account scenarios, the role session name is visible to, and can be logged
    # by the account that owns the role. The role session name is also used in
    # the ARN of the assumed role principal. This means that subsequent cross-
    # account API requests using the temporary security credentials will expose
    # the role session name to the external account in their CloudTrail logs.

    # The regex used to validate this parameter is a string of characters
    # consisting of upper- and lower-case alphanumeric characters with no spaces.
    # You can also include underscores or any of the following characters: =,.@-
    role_session_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # An IAM policy in JSON format.

    # This parameter is optional. If you pass a policy, the temporary security
    # credentials that are returned by the operation have the permissions that
    # are allowed by both (the intersection of) the access policy of the role
    # that is being assumed, _and_ the policy that you pass. This gives you a way
    # to further restrict the permissions for the resulting temporary security
    # credentials. You cannot use the passed policy to grant permissions that are
    # in excess of those allowed by the access policy of the role that is being
    # assumed. For more information, see [Permissions for AssumeRole,
    # AssumeRoleWithSAML, and
    # AssumeRoleWithWebIdentity](http://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_temp_control-
    # access_assumerole.html) in the _IAM User Guide_.

    # The format for this parameter, as described by its regex pattern, is a
    # string of characters up to 2048 characters in length. The characters can be
    # any ASCII character from the space character to the end of the valid
    # character list (\u0020-\u00FF). It can also include the tab (\u0009),
    # linefeed (\u000A), and carriage return (\u000D) characters.

    # The policy plain text must be 2048 bytes or shorter. However, an internal
    # conversion compresses it into a packed binary format with a separate limit.
    # The PackedPolicySize response element indicates by percentage how close to
    # the upper size limit the policy is, with 100% equaling the maximum allowed
    # size.
    policy: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The duration, in seconds, of the role session. The value can range from 900
    # seconds (15 minutes) up to the maximum session duration setting for the
    # role. This setting can have a value from 1 hour to 12 hours. If you specify
    # a value higher than this setting, the operation fails. For example, if you
    # specify a session duration of 12 hours, but your administrator set the
    # maximum session duration to 6 hours, your operation fails. To learn how to
    # view the maximum value for your role, see [View the Maximum Session
    # Duration Setting for a
    # Role](http://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use.html#id_roles_use_view-
    # role-max-session) in the _IAM User Guide_.

    # By default, the value is set to 3600 seconds.

    # The `DurationSeconds` parameter is separate from the duration of a console
    # session that you might request using the returned credentials. The request
    # to the federation endpoint for a console sign-in token takes a
    # `SessionDuration` parameter that specifies the maximum length of the
    # console session. For more information, see [Creating a URL that Enables
    # Federated Users to Access the AWS Management
    # Console](http://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_providers_enable-
    # console-custom-url.html) in the _IAM User Guide_.
    duration_seconds: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A unique identifier that is used by third parties when assuming roles in
    # their customers' accounts. For each role that the third party can assume,
    # they should instruct their customers to ensure the role's trust policy
    # checks for the external ID that the third party generated. Each time the
    # third party assumes the role, they should pass the customer's external ID.
    # The external ID is useful in order to help third parties bind a role to the
    # customer who created it. For more information about the external ID, see
    # [How to Use an External ID When Granting Access to Your AWS Resources to a
    # Third
    # Party](http://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_create_for-
    # user_externalid.html) in the _IAM User Guide_.

    # The regex used to validated this parameter is a string of characters
    # consisting of upper- and lower-case alphanumeric characters with no spaces.
    # You can also include underscores or any of the following characters:
    # =,.@:/-
    external_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The identification number of the MFA device that is associated with the
    # user who is making the `AssumeRole` call. Specify this value if the trust
    # policy of the role being assumed includes a condition that requires MFA
    # authentication. The value is either the serial number for a hardware device
    # (such as `GAHT12345678`) or an Amazon Resource Name (ARN) for a virtual
    # device (such as `arn:aws:iam::123456789012:mfa/user`).

    # The regex used to validate this parameter is a string of characters
    # consisting of upper- and lower-case alphanumeric characters with no spaces.
    # You can also include underscores or any of the following characters: =,.@-
    serial_number: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The value provided by the MFA device, if the trust policy of the role being
    # assumed requires MFA (that is, if the policy includes a condition that
    # tests for MFA). If the role being assumed requires MFA and if the
    # `TokenCode` value is missing or expired, the `AssumeRole` call returns an
    # "access denied" error.

    # The format for this parameter, as described by its regex pattern, is a
    # sequence of six numeric digits.
    token_code: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class AssumeRoleResponse(OutputShapeBase):
    """
    Contains the response to a successful AssumeRole request, including temporary
    AWS credentials that can be used to make AWS requests.
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
                "credentials",
                "Credentials",
                TypeInfo(Credentials),
            ),
            (
                "assumed_role_user",
                "AssumedRoleUser",
                TypeInfo(AssumedRoleUser),
            ),
            (
                "packed_policy_size",
                "PackedPolicySize",
                TypeInfo(int),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The temporary security credentials, which include an access key ID, a
    # secret access key, and a security (or session) token.

    # **Note:** The size of the security token that STS APIs return is not fixed.
    # We strongly recommend that you make no assumptions about the maximum size.
    # As of this writing, the typical size is less than 4096 bytes, but that can
    # vary. Also, future updates to AWS might require larger sizes.
    credentials: "Credentials" = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The Amazon Resource Name (ARN) and the assumed role ID, which are
    # identifiers that you can use to refer to the resulting temporary security
    # credentials. For example, you can reference these credentials as a
    # principal in a resource-based policy by using the ARN or assumed role ID.
    # The ARN and ID include the `RoleSessionName` that you specified when you
    # called `AssumeRole`.
    assumed_role_user: "AssumedRoleUser" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A percentage value that indicates the size of the policy in packed form.
    # The service rejects any policy with a packed size greater than 100 percent,
    # which means the policy exceeded the allowed space.
    packed_policy_size: int = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class AssumeRoleWithSAMLRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "role_arn",
                "RoleArn",
                TypeInfo(str),
            ),
            (
                "principal_arn",
                "PrincipalArn",
                TypeInfo(str),
            ),
            (
                "saml_assertion",
                "SAMLAssertion",
                TypeInfo(str),
            ),
            (
                "policy",
                "Policy",
                TypeInfo(str),
            ),
            (
                "duration_seconds",
                "DurationSeconds",
                TypeInfo(int),
            ),
        ]

    # The Amazon Resource Name (ARN) of the role that the caller is assuming.
    role_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The Amazon Resource Name (ARN) of the SAML provider in IAM that describes
    # the IdP.
    principal_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The base-64 encoded SAML authentication response provided by the IdP.

    # For more information, see [Configuring a Relying Party and Adding
    # Claims](http://docs.aws.amazon.com/IAM/latest/UserGuide/create-role-saml-
    # IdP-tasks.html) in the _Using IAM_ guide.
    saml_assertion: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # An IAM policy in JSON format.

    # The policy parameter is optional. If you pass a policy, the temporary
    # security credentials that are returned by the operation have the
    # permissions that are allowed by both the access policy of the role that is
    # being assumed, _**and** _ the policy that you pass. This gives you a way to
    # further restrict the permissions for the resulting temporary security
    # credentials. You cannot use the passed policy to grant permissions that are
    # in excess of those allowed by the access policy of the role that is being
    # assumed. For more information, [Permissions for AssumeRole,
    # AssumeRoleWithSAML, and
    # AssumeRoleWithWebIdentity](http://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_temp_control-
    # access_assumerole.html) in the _IAM User Guide_.

    # The format for this parameter, as described by its regex pattern, is a
    # string of characters up to 2048 characters in length. The characters can be
    # any ASCII character from the space character to the end of the valid
    # character list (\u0020-\u00FF). It can also include the tab (\u0009),
    # linefeed (\u000A), and carriage return (\u000D) characters.

    # The policy plain text must be 2048 bytes or shorter. However, an internal
    # conversion compresses it into a packed binary format with a separate limit.
    # The PackedPolicySize response element indicates by percentage how close to
    # the upper size limit the policy is, with 100% equaling the maximum allowed
    # size.
    policy: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The duration, in seconds, of the role session. Your role session lasts for
    # the duration that you specify for the `DurationSeconds` parameter, or until
    # the time specified in the SAML authentication response's
    # `SessionNotOnOrAfter` value, whichever is shorter. You can provide a
    # `DurationSeconds` value from 900 seconds (15 minutes) up to the maximum
    # session duration setting for the role. This setting can have a value from 1
    # hour to 12 hours. If you specify a value higher than this setting, the
    # operation fails. For example, if you specify a session duration of 12
    # hours, but your administrator set the maximum session duration to 6 hours,
    # your operation fails. To learn how to view the maximum value for your role,
    # see [View the Maximum Session Duration Setting for a
    # Role](http://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use.html#id_roles_use_view-
    # role-max-session) in the _IAM User Guide_.

    # By default, the value is set to 3600 seconds.

    # The `DurationSeconds` parameter is separate from the duration of a console
    # session that you might request using the returned credentials. The request
    # to the federation endpoint for a console sign-in token takes a
    # `SessionDuration` parameter that specifies the maximum length of the
    # console session. For more information, see [Creating a URL that Enables
    # Federated Users to Access the AWS Management
    # Console](http://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_providers_enable-
    # console-custom-url.html) in the _IAM User Guide_.
    duration_seconds: int = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class AssumeRoleWithSAMLResponse(OutputShapeBase):
    """
    Contains the response to a successful AssumeRoleWithSAML request, including
    temporary AWS credentials that can be used to make AWS requests.
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
                "credentials",
                "Credentials",
                TypeInfo(Credentials),
            ),
            (
                "assumed_role_user",
                "AssumedRoleUser",
                TypeInfo(AssumedRoleUser),
            ),
            (
                "packed_policy_size",
                "PackedPolicySize",
                TypeInfo(int),
            ),
            (
                "subject",
                "Subject",
                TypeInfo(str),
            ),
            (
                "subject_type",
                "SubjectType",
                TypeInfo(str),
            ),
            (
                "issuer",
                "Issuer",
                TypeInfo(str),
            ),
            (
                "audience",
                "Audience",
                TypeInfo(str),
            ),
            (
                "name_qualifier",
                "NameQualifier",
                TypeInfo(str),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The temporary security credentials, which include an access key ID, a
    # secret access key, and a security (or session) token.

    # **Note:** The size of the security token that STS APIs return is not fixed.
    # We strongly recommend that you make no assumptions about the maximum size.
    # As of this writing, the typical size is less than 4096 bytes, but that can
    # vary. Also, future updates to AWS might require larger sizes.
    credentials: "Credentials" = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The identifiers for the temporary security credentials that the operation
    # returns.
    assumed_role_user: "AssumedRoleUser" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A percentage value that indicates the size of the policy in packed form.
    # The service rejects any policy with a packed size greater than 100 percent,
    # which means the policy exceeded the allowed space.
    packed_policy_size: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The value of the `NameID` element in the `Subject` element of the SAML
    # assertion.
    subject: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The format of the name ID, as defined by the `Format` attribute in the
    # `NameID` element of the SAML assertion. Typical examples of the format are
    # `transient` or `persistent`.

    # If the format includes the prefix `urn:oasis:names:tc:SAML:2.0:nameid-
    # format`, that prefix is removed. For example,
    # `urn:oasis:names:tc:SAML:2.0:nameid-format:transient` is returned as
    # `transient`. If the format includes any other prefix, the format is
    # returned with no modifications.
    subject_type: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The value of the `Issuer` element of the SAML assertion.
    issuer: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The value of the `Recipient` attribute of the `SubjectConfirmationData`
    # element of the SAML assertion.
    audience: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A hash value based on the concatenation of the `Issuer` response value, the
    # AWS account ID, and the friendly name (the last part of the ARN) of the
    # SAML provider in IAM. The combination of `NameQualifier` and `Subject` can
    # be used to uniquely identify a federated user.

    # The following pseudocode shows how the hash value is calculated:

    # `BASE64 ( SHA1 ( "https://example.com/saml" + "123456789012" + "/MySAMLIdP"
    # ) )`
    name_qualifier: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class AssumeRoleWithWebIdentityRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "role_arn",
                "RoleArn",
                TypeInfo(str),
            ),
            (
                "role_session_name",
                "RoleSessionName",
                TypeInfo(str),
            ),
            (
                "web_identity_token",
                "WebIdentityToken",
                TypeInfo(str),
            ),
            (
                "provider_id",
                "ProviderId",
                TypeInfo(str),
            ),
            (
                "policy",
                "Policy",
                TypeInfo(str),
            ),
            (
                "duration_seconds",
                "DurationSeconds",
                TypeInfo(int),
            ),
        ]

    # The Amazon Resource Name (ARN) of the role that the caller is assuming.
    role_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # An identifier for the assumed role session. Typically, you pass the name or
    # identifier that is associated with the user who is using your application.
    # That way, the temporary security credentials that your application will use
    # are associated with that user. This session name is included as part of the
    # ARN and assumed role ID in the `AssumedRoleUser` response element.

    # The regex used to validate this parameter is a string of characters
    # consisting of upper- and lower-case alphanumeric characters with no spaces.
    # You can also include underscores or any of the following characters: =,.@-
    role_session_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The OAuth 2.0 access token or OpenID Connect ID token that is provided by
    # the identity provider. Your application must get this token by
    # authenticating the user who is using your application with a web identity
    # provider before the application makes an `AssumeRoleWithWebIdentity` call.
    web_identity_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The fully qualified host component of the domain name of the identity
    # provider.

    # Specify this value only for OAuth 2.0 access tokens. Currently
    # `www.amazon.com` and `graph.facebook.com` are the only supported identity
    # providers for OAuth 2.0 access tokens. Do not include URL schemes and port
    # numbers.

    # Do not specify this value for OpenID Connect ID tokens.
    provider_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # An IAM policy in JSON format.

    # The policy parameter is optional. If you pass a policy, the temporary
    # security credentials that are returned by the operation have the
    # permissions that are allowed by both the access policy of the role that is
    # being assumed, _**and** _ the policy that you pass. This gives you a way to
    # further restrict the permissions for the resulting temporary security
    # credentials. You cannot use the passed policy to grant permissions that are
    # in excess of those allowed by the access policy of the role that is being
    # assumed. For more information, see [Permissions for
    # AssumeRoleWithWebIdentity](http://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_temp_control-
    # access_assumerole.html) in the _IAM User Guide_.

    # The format for this parameter, as described by its regex pattern, is a
    # string of characters up to 2048 characters in length. The characters can be
    # any ASCII character from the space character to the end of the valid
    # character list (\u0020-\u00FF). It can also include the tab (\u0009),
    # linefeed (\u000A), and carriage return (\u000D) characters.

    # The policy plain text must be 2048 bytes or shorter. However, an internal
    # conversion compresses it into a packed binary format with a separate limit.
    # The PackedPolicySize response element indicates by percentage how close to
    # the upper size limit the policy is, with 100% equaling the maximum allowed
    # size.
    policy: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The duration, in seconds, of the role session. The value can range from 900
    # seconds (15 minutes) up to the maximum session duration setting for the
    # role. This setting can have a value from 1 hour to 12 hours. If you specify
    # a value higher than this setting, the operation fails. For example, if you
    # specify a session duration of 12 hours, but your administrator set the
    # maximum session duration to 6 hours, your operation fails. To learn how to
    # view the maximum value for your role, see [View the Maximum Session
    # Duration Setting for a
    # Role](http://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use.html#id_roles_use_view-
    # role-max-session) in the _IAM User Guide_.

    # By default, the value is set to 3600 seconds.

    # The `DurationSeconds` parameter is separate from the duration of a console
    # session that you might request using the returned credentials. The request
    # to the federation endpoint for a console sign-in token takes a
    # `SessionDuration` parameter that specifies the maximum length of the
    # console session. For more information, see [Creating a URL that Enables
    # Federated Users to Access the AWS Management
    # Console](http://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_providers_enable-
    # console-custom-url.html) in the _IAM User Guide_.
    duration_seconds: int = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class AssumeRoleWithWebIdentityResponse(OutputShapeBase):
    """
    Contains the response to a successful AssumeRoleWithWebIdentity request,
    including temporary AWS credentials that can be used to make AWS requests.
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
                "credentials",
                "Credentials",
                TypeInfo(Credentials),
            ),
            (
                "subject_from_web_identity_token",
                "SubjectFromWebIdentityToken",
                TypeInfo(str),
            ),
            (
                "assumed_role_user",
                "AssumedRoleUser",
                TypeInfo(AssumedRoleUser),
            ),
            (
                "packed_policy_size",
                "PackedPolicySize",
                TypeInfo(int),
            ),
            (
                "provider",
                "Provider",
                TypeInfo(str),
            ),
            (
                "audience",
                "Audience",
                TypeInfo(str),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The temporary security credentials, which include an access key ID, a
    # secret access key, and a security token.

    # **Note:** The size of the security token that STS APIs return is not fixed.
    # We strongly recommend that you make no assumptions about the maximum size.
    # As of this writing, the typical size is less than 4096 bytes, but that can
    # vary. Also, future updates to AWS might require larger sizes.
    credentials: "Credentials" = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The unique user identifier that is returned by the identity provider. This
    # identifier is associated with the `WebIdentityToken` that was submitted
    # with the `AssumeRoleWithWebIdentity` call. The identifier is typically
    # unique to the user and the application that acquired the `WebIdentityToken`
    # (pairwise identifier). For OpenID Connect ID tokens, this field contains
    # the value returned by the identity provider as the token's `sub` (Subject)
    # claim.
    subject_from_web_identity_token: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The Amazon Resource Name (ARN) and the assumed role ID, which are
    # identifiers that you can use to refer to the resulting temporary security
    # credentials. For example, you can reference these credentials as a
    # principal in a resource-based policy by using the ARN or assumed role ID.
    # The ARN and ID include the `RoleSessionName` that you specified when you
    # called `AssumeRole`.
    assumed_role_user: "AssumedRoleUser" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A percentage value that indicates the size of the policy in packed form.
    # The service rejects any policy with a packed size greater than 100 percent,
    # which means the policy exceeded the allowed space.
    packed_policy_size: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The issuing authority of the web identity token presented. For OpenID
    # Connect ID Tokens this contains the value of the `iss` field. For OAuth 2.0
    # access tokens, this contains the value of the `ProviderId` parameter that
    # was passed in the `AssumeRoleWithWebIdentity` request.
    provider: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The intended audience (also known as client ID) of the web identity token.
    # This is traditionally the client identifier issued to the application that
    # requested the web identity token.
    audience: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class AssumedRoleUser(ShapeBase):
    """
    The identifiers for the temporary security credentials that the operation
    returns.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "assumed_role_id",
                "AssumedRoleId",
                TypeInfo(str),
            ),
            (
                "arn",
                "Arn",
                TypeInfo(str),
            ),
        ]

    # A unique identifier that contains the role ID and the role session name of
    # the role that is being assumed. The role ID is generated by AWS when the
    # role is created.
    assumed_role_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The ARN of the temporary security credentials that are returned from the
    # AssumeRole action. For more information about ARNs and how to use them in
    # policies, see [IAM
    # Identifiers](http://docs.aws.amazon.com/IAM/latest/UserGuide/reference_identifiers.html)
    # in _Using IAM_.
    arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class Credentials(ShapeBase):
    """
    AWS credentials for API authentication.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "access_key_id",
                "AccessKeyId",
                TypeInfo(str),
            ),
            (
                "secret_access_key",
                "SecretAccessKey",
                TypeInfo(str),
            ),
            (
                "session_token",
                "SessionToken",
                TypeInfo(str),
            ),
            (
                "expiration",
                "Expiration",
                TypeInfo(datetime.datetime),
            ),
        ]

    # The access key ID that identifies the temporary security credentials.
    access_key_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The secret access key that can be used to sign requests.
    secret_access_key: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The token that users must pass to the service API to use the temporary
    # credentials.
    session_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The date on which the current credentials expire.
    expiration: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class DecodeAuthorizationMessageRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "encoded_message",
                "EncodedMessage",
                TypeInfo(str),
            ),
        ]

    # The encoded message that was returned with the response.
    encoded_message: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DecodeAuthorizationMessageResponse(OutputShapeBase):
    """
    A document that contains additional information about the authorization status
    of a request from an encoded message that is returned in response to an AWS
    request.
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
                "decoded_message",
                "DecodedMessage",
                TypeInfo(str),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # An XML document that contains the decoded message.
    decoded_message: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ExpiredTokenException(ShapeBase):
    """
    The web identity token that was passed is expired or is not valid. Get a new
    identity token from the identity provider and then retry the request.
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
class FederatedUser(ShapeBase):
    """
    Identifiers for the federated user that is associated with the credentials.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "federated_user_id",
                "FederatedUserId",
                TypeInfo(str),
            ),
            (
                "arn",
                "Arn",
                TypeInfo(str),
            ),
        ]

    # The string that identifies the federated user associated with the
    # credentials, similar to the unique ID of an IAM user.
    federated_user_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The ARN that specifies the federated user that is associated with the
    # credentials. For more information about ARNs and how to use them in
    # policies, see [IAM
    # Identifiers](http://docs.aws.amazon.com/IAM/latest/UserGuide/reference_identifiers.html)
    # in _Using IAM_.
    arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class GetCallerIdentityRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class GetCallerIdentityResponse(OutputShapeBase):
    """
    Contains the response to a successful GetCallerIdentity request, including
    information about the entity making the request.
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
                "user_id",
                "UserId",
                TypeInfo(str),
            ),
            (
                "account",
                "Account",
                TypeInfo(str),
            ),
            (
                "arn",
                "Arn",
                TypeInfo(str),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The unique identifier of the calling entity. The exact value depends on the
    # type of entity making the call. The values returned are those listed in the
    # **aws:userid** column in the [Principal
    # table](http://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_variables.html#principaltable)
    # found on the **Policy Variables** reference page in the _IAM User Guide_.
    user_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The AWS account ID number of the account that owns or contains the calling
    # entity.
    account: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The AWS ARN associated with the calling entity.
    arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class GetFederationTokenRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "name",
                "Name",
                TypeInfo(str),
            ),
            (
                "policy",
                "Policy",
                TypeInfo(str),
            ),
            (
                "duration_seconds",
                "DurationSeconds",
                TypeInfo(int),
            ),
        ]

    # The name of the federated user. The name is used as an identifier for the
    # temporary security credentials (such as `Bob`). For example, you can
    # reference the federated user name in a resource-based policy, such as in an
    # Amazon S3 bucket policy.

    # The regex used to validate this parameter is a string of characters
    # consisting of upper- and lower-case alphanumeric characters with no spaces.
    # You can also include underscores or any of the following characters: =,.@-
    name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # An IAM policy in JSON format that is passed with the `GetFederationToken`
    # call and evaluated along with the policy or policies that are attached to
    # the IAM user whose credentials are used to call `GetFederationToken`. The
    # passed policy is used to scope down the permissions that are available to
    # the IAM user, by allowing only a subset of the permissions that are granted
    # to the IAM user. The passed policy cannot grant more permissions than those
    # granted to the IAM user. The final permissions for the federated user are
    # the most restrictive set based on the intersection of the passed policy and
    # the IAM user policy.

    # If you do not pass a policy, the resulting temporary security credentials
    # have no effective permissions. The only exception is when the temporary
    # security credentials are used to access a resource that has a resource-
    # based policy that specifically allows the federated user to access the
    # resource.

    # The format for this parameter, as described by its regex pattern, is a
    # string of characters up to 2048 characters in length. The characters can be
    # any ASCII character from the space character to the end of the valid
    # character list (\u0020-\u00FF). It can also include the tab (\u0009),
    # linefeed (\u000A), and carriage return (\u000D) characters.

    # The policy plain text must be 2048 bytes or shorter. However, an internal
    # conversion compresses it into a packed binary format with a separate limit.
    # The PackedPolicySize response element indicates by percentage how close to
    # the upper size limit the policy is, with 100% equaling the maximum allowed
    # size.

    # For more information about how permissions work, see [Permissions for
    # GetFederationToken](http://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_temp_control-
    # access_getfederationtoken.html).
    policy: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The duration, in seconds, that the session should last. Acceptable
    # durations for federation sessions range from 900 seconds (15 minutes) to
    # 129600 seconds (36 hours), with 43200 seconds (12 hours) as the default.
    # Sessions obtained using AWS account (root) credentials are restricted to a
    # maximum of 3600 seconds (one hour). If the specified duration is longer
    # than one hour, the session obtained by using AWS account (root) credentials
    # defaults to one hour.
    duration_seconds: int = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class GetFederationTokenResponse(OutputShapeBase):
    """
    Contains the response to a successful GetFederationToken request, including
    temporary AWS credentials that can be used to make AWS requests.
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
                "credentials",
                "Credentials",
                TypeInfo(Credentials),
            ),
            (
                "federated_user",
                "FederatedUser",
                TypeInfo(FederatedUser),
            ),
            (
                "packed_policy_size",
                "PackedPolicySize",
                TypeInfo(int),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The temporary security credentials, which include an access key ID, a
    # secret access key, and a security (or session) token.

    # **Note:** The size of the security token that STS APIs return is not fixed.
    # We strongly recommend that you make no assumptions about the maximum size.
    # As of this writing, the typical size is less than 4096 bytes, but that can
    # vary. Also, future updates to AWS might require larger sizes.
    credentials: "Credentials" = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Identifiers for the federated user associated with the credentials (such as
    # `arn:aws:sts::123456789012:federated-user/Bob` or `123456789012:Bob`). You
    # can use the federated user's ARN in your resource-based policies, such as
    # an Amazon S3 bucket policy.
    federated_user: "FederatedUser" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A percentage value indicating the size of the policy in packed form. The
    # service rejects policies for which the packed size is greater than 100
    # percent of the allowed value.
    packed_policy_size: int = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class GetSessionTokenRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "duration_seconds",
                "DurationSeconds",
                TypeInfo(int),
            ),
            (
                "serial_number",
                "SerialNumber",
                TypeInfo(str),
            ),
            (
                "token_code",
                "TokenCode",
                TypeInfo(str),
            ),
        ]

    # The duration, in seconds, that the credentials should remain valid.
    # Acceptable durations for IAM user sessions range from 900 seconds (15
    # minutes) to 129600 seconds (36 hours), with 43200 seconds (12 hours) as the
    # default. Sessions for AWS account owners are restricted to a maximum of
    # 3600 seconds (one hour). If the duration is longer than one hour, the
    # session for AWS account owners defaults to one hour.
    duration_seconds: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The identification number of the MFA device that is associated with the IAM
    # user who is making the `GetSessionToken` call. Specify this value if the
    # IAM user has a policy that requires MFA authentication. The value is either
    # the serial number for a hardware device (such as `GAHT12345678`) or an
    # Amazon Resource Name (ARN) for a virtual device (such as
    # `arn:aws:iam::123456789012:mfa/user`). You can find the device for an IAM
    # user by going to the AWS Management Console and viewing the user's security
    # credentials.

    # The regex used to validated this parameter is a string of characters
    # consisting of upper- and lower-case alphanumeric characters with no spaces.
    # You can also include underscores or any of the following characters:
    # =,.@:/-
    serial_number: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The value provided by the MFA device, if MFA is required. If any policy
    # requires the IAM user to submit an MFA code, specify this value. If MFA
    # authentication is required, and the user does not provide a code when
    # requesting a set of temporary security credentials, the user will receive
    # an "access denied" response when requesting resources that require MFA
    # authentication.

    # The format for this parameter, as described by its regex pattern, is a
    # sequence of six numeric digits.
    token_code: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class GetSessionTokenResponse(OutputShapeBase):
    """
    Contains the response to a successful GetSessionToken request, including
    temporary AWS credentials that can be used to make AWS requests.
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
                "credentials",
                "Credentials",
                TypeInfo(Credentials),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The temporary security credentials, which include an access key ID, a
    # secret access key, and a security (or session) token.

    # **Note:** The size of the security token that STS APIs return is not fixed.
    # We strongly recommend that you make no assumptions about the maximum size.
    # As of this writing, the typical size is less than 4096 bytes, but that can
    # vary. Also, future updates to AWS might require larger sizes.
    credentials: "Credentials" = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class IDPCommunicationErrorException(ShapeBase):
    """
    The request could not be fulfilled because the non-AWS identity provider (IDP)
    that was asked to verify the incoming identity token could not be reached. This
    is often a transient error caused by network conditions. Retry the request a
    limited number of times so that you don't exceed the request rate. If the error
    persists, the non-AWS identity provider might be down or not responding.
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
class IDPRejectedClaimException(ShapeBase):
    """
    The identity provider (IdP) reported that authentication failed. This might be
    because the claim is invalid.

    If this error is returned for the `AssumeRoleWithWebIdentity` operation, it can
    also mean that the claim has expired or has been explicitly revoked.
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
class InvalidAuthorizationMessageException(ShapeBase):
    """
    The error returned if the message passed to `DecodeAuthorizationMessage` was
    invalid. This can happen if the token contains invalid characters, such as
    linebreaks.
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
class InvalidIdentityTokenException(ShapeBase):
    """
    The web identity token that was passed could not be validated by AWS. Get a new
    identity token from the identity provider and then retry the request.
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
class PackedPolicyTooLargeException(ShapeBase):
    """
    The request was rejected because the policy document was too large. The error
    message describes how big the policy document is, in packed form, as a
    percentage of what the API allows.
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
class RegionDisabledException(ShapeBase):
    """
    STS is not activated in the requested region for the account that is being asked
    to generate credentials. The account administrator must use the IAM console to
    activate STS in that region. For more information, see [Activating and
    Deactivating AWS STS in an AWS
    Region](http://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_temp_enable-
    regions.html) in the _IAM User Guide_.
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
