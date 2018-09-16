import datetime
import typing
from autoboto import ShapeBase, OutputShapeBase, TypeInfo
import dataclasses


class AmbiguousRoleResolutionType(str):
    AuthenticatedRole = "AuthenticatedRole"
    Deny = "Deny"


@dataclasses.dataclass
class CognitoIdentityProvider(ShapeBase):
    """
    A provider representing an Amazon Cognito Identity User Pool and its client ID.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "provider_name",
                "ProviderName",
                TypeInfo(str),
            ),
            (
                "client_id",
                "ClientId",
                TypeInfo(str),
            ),
            (
                "server_side_token_check",
                "ServerSideTokenCheck",
                TypeInfo(bool),
            ),
        ]

    # The provider name for an Amazon Cognito Identity User Pool. For example,
    # `cognito-idp.us-east-1.amazonaws.com/us-east-1_123456789`.
    provider_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The client ID for the Amazon Cognito Identity User Pool.
    client_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # TRUE if server-side token validation is enabled for the identity provider’s
    # token.
    server_side_token_check: bool = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class ConcurrentModificationException(ShapeBase):
    """
    Thrown if there are parallel requests to modify a resource.
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

    # The message returned by a ConcurrentModificationException.
    message: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class CreateIdentityPoolInput(ShapeBase):
    """
    Input to the CreateIdentityPool action.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "identity_pool_name",
                "IdentityPoolName",
                TypeInfo(str),
            ),
            (
                "allow_unauthenticated_identities",
                "AllowUnauthenticatedIdentities",
                TypeInfo(bool),
            ),
            (
                "supported_login_providers",
                "SupportedLoginProviders",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "developer_provider_name",
                "DeveloperProviderName",
                TypeInfo(str),
            ),
            (
                "open_id_connect_provider_arns",
                "OpenIdConnectProviderARNs",
                TypeInfo(typing.List[str]),
            ),
            (
                "cognito_identity_providers",
                "CognitoIdentityProviders",
                TypeInfo(typing.List[CognitoIdentityProvider]),
            ),
            (
                "saml_provider_arns",
                "SamlProviderARNs",
                TypeInfo(typing.List[str]),
            ),
        ]

    # A string that you provide.
    identity_pool_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # TRUE if the identity pool supports unauthenticated logins.
    allow_unauthenticated_identities: bool = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Optional key:value pairs mapping provider names to provider app IDs.
    supported_login_providers: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The "domain" by which Cognito will refer to your users. This name acts as a
    # placeholder that allows your backend and the Cognito service to communicate
    # about the developer provider. For the `DeveloperProviderName`, you can use
    # letters as well as period (`.`), underscore (`_`), and dash (`-`).

    # Once you have set a developer provider name, you cannot change it. Please
    # take care in setting this parameter.
    developer_provider_name: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A list of OpendID Connect provider ARNs.
    open_id_connect_provider_arns: typing.List[str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # An array of Amazon Cognito Identity user pools and their client IDs.
    cognito_identity_providers: typing.List["CognitoIdentityProvider"
                                           ] = dataclasses.field(
                                               default=ShapeBase.NOT_SET,
                                           )

    # An array of Amazon Resource Names (ARNs) of the SAML provider for your
    # identity pool.
    saml_provider_arns: typing.List[str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class Credentials(ShapeBase):
    """
    Credentials for the provided identity ID.
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
                "secret_key",
                "SecretKey",
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

    # The Access Key portion of the credentials.
    access_key_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The Secret Access Key portion of the credentials
    secret_key: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The Session Token portion of the credentials
    session_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The date at which these credentials will expire.
    expiration: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class DeleteIdentitiesInput(ShapeBase):
    """
    Input to the `DeleteIdentities` action.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "identity_ids_to_delete",
                "IdentityIdsToDelete",
                TypeInfo(typing.List[str]),
            ),
        ]

    # A list of 1-60 identities that you want to delete.
    identity_ids_to_delete: typing.List[str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class DeleteIdentitiesResponse(OutputShapeBase):
    """
    Returned in response to a successful `DeleteIdentities` operation.
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
                "unprocessed_identity_ids",
                "UnprocessedIdentityIds",
                TypeInfo(typing.List[UnprocessedIdentityId]),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # An array of UnprocessedIdentityId objects, each of which contains an
    # ErrorCode and IdentityId.
    unprocessed_identity_ids: typing.List["UnprocessedIdentityId"
                                         ] = dataclasses.field(
                                             default=ShapeBase.NOT_SET,
                                         )


@dataclasses.dataclass
class DeleteIdentityPoolInput(ShapeBase):
    """
    Input to the DeleteIdentityPool action.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "identity_pool_id",
                "IdentityPoolId",
                TypeInfo(str),
            ),
        ]

    # An identity pool ID in the format REGION:GUID.
    identity_pool_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DescribeIdentityInput(ShapeBase):
    """
    Input to the `DescribeIdentity` action.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "identity_id",
                "IdentityId",
                TypeInfo(str),
            ),
        ]

    # A unique identifier in the format REGION:GUID.
    identity_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DescribeIdentityPoolInput(ShapeBase):
    """
    Input to the DescribeIdentityPool action.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "identity_pool_id",
                "IdentityPoolId",
                TypeInfo(str),
            ),
        ]

    # An identity pool ID in the format REGION:GUID.
    identity_pool_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DeveloperUserAlreadyRegisteredException(ShapeBase):
    """
    The provided developer user identifier is already registered with Cognito under
    a different identity ID.
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

    # This developer user identifier is already registered with Cognito.
    message: str = dataclasses.field(default=ShapeBase.NOT_SET, )


class ErrorCode(str):
    AccessDenied = "AccessDenied"
    InternalServerError = "InternalServerError"


@dataclasses.dataclass
class ExternalServiceException(ShapeBase):
    """
    An exception thrown when a dependent service such as Facebook or Twitter is not
    responding
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

    # The message returned by an ExternalServiceException
    message: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class GetCredentialsForIdentityInput(ShapeBase):
    """
    Input to the `GetCredentialsForIdentity` action.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "identity_id",
                "IdentityId",
                TypeInfo(str),
            ),
            (
                "logins",
                "Logins",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "custom_role_arn",
                "CustomRoleArn",
                TypeInfo(str),
            ),
        ]

    # A unique identifier in the format REGION:GUID.
    identity_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A set of optional name-value pairs that map provider names to provider
    # tokens.
    logins: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The Amazon Resource Name (ARN) of the role to be assumed when multiple
    # roles were received in the token from the identity provider. For example, a
    # SAML-based identity provider. This parameter is optional for identity
    # providers that do not support role customization.
    custom_role_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class GetCredentialsForIdentityResponse(OutputShapeBase):
    """
    Returned in response to a successful `GetCredentialsForIdentity` operation.
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
                "identity_id",
                "IdentityId",
                TypeInfo(str),
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

    # A unique identifier in the format REGION:GUID.
    identity_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Credentials for the provided identity ID.
    credentials: "Credentials" = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class GetIdInput(ShapeBase):
    """
    Input to the GetId action.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "identity_pool_id",
                "IdentityPoolId",
                TypeInfo(str),
            ),
            (
                "account_id",
                "AccountId",
                TypeInfo(str),
            ),
            (
                "logins",
                "Logins",
                TypeInfo(typing.Dict[str, str]),
            ),
        ]

    # An identity pool ID in the format REGION:GUID.
    identity_pool_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A standard AWS account ID (9+ digits).
    account_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A set of optional name-value pairs that map provider names to provider
    # tokens. The available provider names for `Logins` are as follows:

    #   * Facebook: `graph.facebook.com`

    #   * Amazon Cognito Identity Provider: `cognito-idp.us-east-1.amazonaws.com/us-east-1_123456789`

    #   * Google: `accounts.google.com`

    #   * Amazon: `www.amazon.com`

    #   * Twitter: `api.twitter.com`

    #   * Digits: `www.digits.com`
    logins: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class GetIdResponse(OutputShapeBase):
    """
    Returned in response to a GetId request.
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
                "identity_id",
                "IdentityId",
                TypeInfo(str),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A unique identifier in the format REGION:GUID.
    identity_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class GetIdentityPoolRolesInput(ShapeBase):
    """
    Input to the `GetIdentityPoolRoles` action.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "identity_pool_id",
                "IdentityPoolId",
                TypeInfo(str),
            ),
        ]

    # An identity pool ID in the format REGION:GUID.
    identity_pool_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class GetIdentityPoolRolesResponse(OutputShapeBase):
    """
    Returned in response to a successful `GetIdentityPoolRoles` operation.
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
                "identity_pool_id",
                "IdentityPoolId",
                TypeInfo(str),
            ),
            (
                "roles",
                "Roles",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "role_mappings",
                "RoleMappings",
                TypeInfo(typing.Dict[str, RoleMapping]),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # An identity pool ID in the format REGION:GUID.
    identity_pool_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The map of roles associated with this pool. Currently only authenticated
    # and unauthenticated roles are supported.
    roles: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # How users for a specific identity provider are to mapped to roles. This is
    # a String-to-RoleMapping object map. The string identifies the identity
    # provider, for example, "graph.facebook.com" or "cognito-idp-
    # east-1.amazonaws.com/us-east-1_abcdefghi:app_client_id".
    role_mappings: typing.Dict[str, "RoleMapping"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class GetOpenIdTokenForDeveloperIdentityInput(ShapeBase):
    """
    Input to the `GetOpenIdTokenForDeveloperIdentity` action.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "identity_pool_id",
                "IdentityPoolId",
                TypeInfo(str),
            ),
            (
                "logins",
                "Logins",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "identity_id",
                "IdentityId",
                TypeInfo(str),
            ),
            (
                "token_duration",
                "TokenDuration",
                TypeInfo(int),
            ),
        ]

    # An identity pool ID in the format REGION:GUID.
    identity_pool_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A set of optional name-value pairs that map provider names to provider
    # tokens. Each name-value pair represents a user from a public provider or
    # developer provider. If the user is from a developer provider, the name-
    # value pair will follow the syntax `"developer_provider_name":
    # "developer_user_identifier"`. The developer provider is the "domain" by
    # which Cognito will refer to your users; you provided this domain while
    # creating/updating the identity pool. The developer user identifier is an
    # identifier from your backend that uniquely identifies a user. When you
    # create an identity pool, you can specify the supported logins.
    logins: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A unique identifier in the format REGION:GUID.
    identity_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The expiration time of the token, in seconds. You can specify a custom
    # expiration time for the token so that you can cache it. If you don't
    # provide an expiration time, the token is valid for 15 minutes. You can
    # exchange the token with Amazon STS for temporary AWS credentials, which are
    # valid for a maximum of one hour. The maximum token duration you can set is
    # 24 hours. You should take care in setting the expiration time for a token,
    # as there are significant security implications: an attacker could use a
    # leaked token to access your AWS resources for the token's duration.
    token_duration: int = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class GetOpenIdTokenForDeveloperIdentityResponse(OutputShapeBase):
    """
    Returned in response to a successful `GetOpenIdTokenForDeveloperIdentity`
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
                "identity_id",
                "IdentityId",
                TypeInfo(str),
            ),
            (
                "token",
                "Token",
                TypeInfo(str),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A unique identifier in the format REGION:GUID.
    identity_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # An OpenID token.
    token: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class GetOpenIdTokenInput(ShapeBase):
    """
    Input to the GetOpenIdToken action.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "identity_id",
                "IdentityId",
                TypeInfo(str),
            ),
            (
                "logins",
                "Logins",
                TypeInfo(typing.Dict[str, str]),
            ),
        ]

    # A unique identifier in the format REGION:GUID.
    identity_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A set of optional name-value pairs that map provider names to provider
    # tokens. When using graph.facebook.com and www.amazon.com, supply the
    # access_token returned from the provider's authflow. For
    # accounts.google.com, an Amazon Cognito Identity Provider, or any other
    # OpenId Connect provider, always include the `id_token`.
    logins: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class GetOpenIdTokenResponse(OutputShapeBase):
    """
    Returned in response to a successful GetOpenIdToken request.
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
                "identity_id",
                "IdentityId",
                TypeInfo(str),
            ),
            (
                "token",
                "Token",
                TypeInfo(str),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A unique identifier in the format REGION:GUID. Note that the IdentityId
    # returned may not match the one passed on input.
    identity_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # An OpenID token, valid for 15 minutes.
    token: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class IdentityDescription(OutputShapeBase):
    """
    A description of the identity.
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
                "identity_id",
                "IdentityId",
                TypeInfo(str),
            ),
            (
                "logins",
                "Logins",
                TypeInfo(typing.List[str]),
            ),
            (
                "creation_date",
                "CreationDate",
                TypeInfo(datetime.datetime),
            ),
            (
                "last_modified_date",
                "LastModifiedDate",
                TypeInfo(datetime.datetime),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A unique identifier in the format REGION:GUID.
    identity_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A set of optional name-value pairs that map provider names to provider
    # tokens.
    logins: typing.List[str] = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Date on which the identity was created.
    creation_date: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Date on which the identity was last modified.
    last_modified_date: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class IdentityPool(OutputShapeBase):
    """
    An object representing an Amazon Cognito identity pool.
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
                "identity_pool_id",
                "IdentityPoolId",
                TypeInfo(str),
            ),
            (
                "identity_pool_name",
                "IdentityPoolName",
                TypeInfo(str),
            ),
            (
                "allow_unauthenticated_identities",
                "AllowUnauthenticatedIdentities",
                TypeInfo(bool),
            ),
            (
                "supported_login_providers",
                "SupportedLoginProviders",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "developer_provider_name",
                "DeveloperProviderName",
                TypeInfo(str),
            ),
            (
                "open_id_connect_provider_arns",
                "OpenIdConnectProviderARNs",
                TypeInfo(typing.List[str]),
            ),
            (
                "cognito_identity_providers",
                "CognitoIdentityProviders",
                TypeInfo(typing.List[CognitoIdentityProvider]),
            ),
            (
                "saml_provider_arns",
                "SamlProviderARNs",
                TypeInfo(typing.List[str]),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # An identity pool ID in the format REGION:GUID.
    identity_pool_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A string that you provide.
    identity_pool_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # TRUE if the identity pool supports unauthenticated logins.
    allow_unauthenticated_identities: bool = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Optional key:value pairs mapping provider names to provider app IDs.
    supported_login_providers: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The "domain" by which Cognito will refer to your users.
    developer_provider_name: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A list of OpendID Connect provider ARNs.
    open_id_connect_provider_arns: typing.List[str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A list representing an Amazon Cognito Identity User Pool and its client ID.
    cognito_identity_providers: typing.List["CognitoIdentityProvider"
                                           ] = dataclasses.field(
                                               default=ShapeBase.NOT_SET,
                                           )

    # An array of Amazon Resource Names (ARNs) of the SAML provider for your
    # identity pool.
    saml_provider_arns: typing.List[str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class IdentityPoolShortDescription(ShapeBase):
    """
    A description of the identity pool.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "identity_pool_id",
                "IdentityPoolId",
                TypeInfo(str),
            ),
            (
                "identity_pool_name",
                "IdentityPoolName",
                TypeInfo(str),
            ),
        ]

    # An identity pool ID in the format REGION:GUID.
    identity_pool_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A string that you provide.
    identity_pool_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class InternalErrorException(ShapeBase):
    """
    Thrown when the service encounters an error during processing the request.
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

    # The message returned by an InternalErrorException.
    message: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class InvalidIdentityPoolConfigurationException(ShapeBase):
    """
    Thrown if the identity pool has no role associated for the given auth type
    (auth/unauth) or if the AssumeRole fails.
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

    # The message returned for an `InvalidIdentityPoolConfigurationException`
    message: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class InvalidParameterException(ShapeBase):
    """
    Thrown for missing or bad input parameter(s).
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

    # The message returned by an InvalidParameterException.
    message: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class LimitExceededException(ShapeBase):
    """
    Thrown when the total number of user pools has exceeded a preset limit.
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

    # The message returned by a LimitExceededException.
    message: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ListIdentitiesInput(ShapeBase):
    """
    Input to the ListIdentities action.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "identity_pool_id",
                "IdentityPoolId",
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
                "hide_disabled",
                "HideDisabled",
                TypeInfo(bool),
            ),
        ]

    # An identity pool ID in the format REGION:GUID.
    identity_pool_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The maximum number of identities to return.
    max_results: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A pagination token.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # An optional boolean parameter that allows you to hide disabled identities.
    # If omitted, the ListIdentities API will include disabled identities in the
    # response.
    hide_disabled: bool = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ListIdentitiesResponse(OutputShapeBase):
    """
    The response to a ListIdentities request.
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
                "identity_pool_id",
                "IdentityPoolId",
                TypeInfo(str),
            ),
            (
                "identities",
                "Identities",
                TypeInfo(typing.List[IdentityDescription]),
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

    # An identity pool ID in the format REGION:GUID.
    identity_pool_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # An object containing a set of identities and associated mappings.
    identities: typing.List["IdentityDescription"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A pagination token.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ListIdentityPoolsInput(ShapeBase):
    """
    Input to the ListIdentityPools action.
    """

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

    # The maximum number of identities to return.
    max_results: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A pagination token.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ListIdentityPoolsResponse(OutputShapeBase):
    """
    The result of a successful ListIdentityPools action.
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
                "identity_pools",
                "IdentityPools",
                TypeInfo(typing.List[IdentityPoolShortDescription]),
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

    # The identity pools returned by the ListIdentityPools action.
    identity_pools: typing.List["IdentityPoolShortDescription"
                               ] = dataclasses.field(
                                   default=ShapeBase.NOT_SET,
                               )

    # A pagination token.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class LookupDeveloperIdentityInput(ShapeBase):
    """
    Input to the `LookupDeveloperIdentityInput` action.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "identity_pool_id",
                "IdentityPoolId",
                TypeInfo(str),
            ),
            (
                "identity_id",
                "IdentityId",
                TypeInfo(str),
            ),
            (
                "developer_user_identifier",
                "DeveloperUserIdentifier",
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
        ]

    # An identity pool ID in the format REGION:GUID.
    identity_pool_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A unique identifier in the format REGION:GUID.
    identity_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A unique ID used by your backend authentication process to identify a user.
    # Typically, a developer identity provider would issue many developer user
    # identifiers, in keeping with the number of users.
    developer_user_identifier: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The maximum number of identities to return.
    max_results: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A pagination token. The first call you make will have `NextToken` set to
    # null. After that the service will return `NextToken` values as needed. For
    # example, let's say you make a request with `MaxResults` set to 10, and
    # there are 20 matches in the database. The service will return a pagination
    # token as a part of the response. This token can be used to call the API
    # again and get results starting from the 11th match.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class LookupDeveloperIdentityResponse(OutputShapeBase):
    """
    Returned in response to a successful `LookupDeveloperIdentity` action.
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
                "identity_id",
                "IdentityId",
                TypeInfo(str),
            ),
            (
                "developer_user_identifier_list",
                "DeveloperUserIdentifierList",
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

    # A unique identifier in the format REGION:GUID.
    identity_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # This is the list of developer user identifiers associated with an identity
    # ID. Cognito supports the association of multiple developer user identifiers
    # with an identity ID.
    developer_user_identifier_list: typing.List[str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A pagination token. The first call you make will have `NextToken` set to
    # null. After that the service will return `NextToken` values as needed. For
    # example, let's say you make a request with `MaxResults` set to 10, and
    # there are 20 matches in the database. The service will return a pagination
    # token as a part of the response. This token can be used to call the API
    # again and get results starting from the 11th match.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class MappingRule(ShapeBase):
    """
    A rule that maps a claim name, a claim value, and a match type to a role ARN.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "claim",
                "Claim",
                TypeInfo(str),
            ),
            (
                "match_type",
                "MatchType",
                TypeInfo(typing.Union[str, MappingRuleMatchType]),
            ),
            (
                "value",
                "Value",
                TypeInfo(str),
            ),
            (
                "role_arn",
                "RoleARN",
                TypeInfo(str),
            ),
        ]

    # The claim name that must be present in the token, for example, "isAdmin" or
    # "paid".
    claim: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The match condition that specifies how closely the claim value in the IdP
    # token must match `Value`.
    match_type: typing.Union[str, "MappingRuleMatchType"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A brief string that the claim must match, for example, "paid" or "yes".
    value: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The role ARN.
    role_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )


class MappingRuleMatchType(str):
    Equals = "Equals"
    Contains = "Contains"
    StartsWith = "StartsWith"
    NotEqual = "NotEqual"


@dataclasses.dataclass
class MergeDeveloperIdentitiesInput(ShapeBase):
    """
    Input to the `MergeDeveloperIdentities` action.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "source_user_identifier",
                "SourceUserIdentifier",
                TypeInfo(str),
            ),
            (
                "destination_user_identifier",
                "DestinationUserIdentifier",
                TypeInfo(str),
            ),
            (
                "developer_provider_name",
                "DeveloperProviderName",
                TypeInfo(str),
            ),
            (
                "identity_pool_id",
                "IdentityPoolId",
                TypeInfo(str),
            ),
        ]

    # User identifier for the source user. The value should be a
    # `DeveloperUserIdentifier`.
    source_user_identifier: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # User identifier for the destination user. The value should be a
    # `DeveloperUserIdentifier`.
    destination_user_identifier: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The "domain" by which Cognito will refer to your users. This is a (pseudo)
    # domain name that you provide while creating an identity pool. This name
    # acts as a placeholder that allows your backend and the Cognito service to
    # communicate about the developer provider. For the `DeveloperProviderName`,
    # you can use letters as well as period (.), underscore (_), and dash (-).
    developer_provider_name: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # An identity pool ID in the format REGION:GUID.
    identity_pool_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class MergeDeveloperIdentitiesResponse(OutputShapeBase):
    """
    Returned in response to a successful `MergeDeveloperIdentities` action.
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
                "identity_id",
                "IdentityId",
                TypeInfo(str),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A unique identifier in the format REGION:GUID.
    identity_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class NotAuthorizedException(ShapeBase):
    """
    Thrown when a user is not authorized to access the requested resource.
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

    # The message returned by a NotAuthorizedException
    message: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ResourceConflictException(ShapeBase):
    """
    Thrown when a user tries to use a login which is already linked to another
    account.
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

    # The message returned by a ResourceConflictException.
    message: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ResourceNotFoundException(ShapeBase):
    """
    Thrown when the requested resource (for example, a dataset or record) does not
    exist.
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

    # The message returned by a ResourceNotFoundException.
    message: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class RoleMapping(ShapeBase):
    """
    A role mapping.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "type",
                "Type",
                TypeInfo(typing.Union[str, RoleMappingType]),
            ),
            (
                "ambiguous_role_resolution",
                "AmbiguousRoleResolution",
                TypeInfo(typing.Union[str, AmbiguousRoleResolutionType]),
            ),
            (
                "rules_configuration",
                "RulesConfiguration",
                TypeInfo(RulesConfigurationType),
            ),
        ]

    # The role mapping type. Token will use `cognito:roles` and
    # `cognito:preferred_role` claims from the Cognito identity provider token to
    # map groups to roles. Rules will attempt to match claims from the token to
    # map to a role.
    type: typing.Union[str, "RoleMappingType"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # If you specify Token or Rules as the `Type`, `AmbiguousRoleResolution` is
    # required.

    # Specifies the action to be taken if either no rules match the claim value
    # for the `Rules` type, or there is no `cognito:preferred_role` claim and
    # there are multiple `cognito:roles` matches for the `Token` type.
    ambiguous_role_resolution: typing.Union[str, "AmbiguousRoleResolutionType"
                                           ] = dataclasses.field(
                                               default=ShapeBase.NOT_SET,
                                           )

    # The rules to be used for mapping users to roles.

    # If you specify Rules as the role mapping type, `RulesConfiguration` is
    # required.
    rules_configuration: "RulesConfigurationType" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


class RoleMappingType(str):
    Token = "Token"
    Rules = "Rules"


@dataclasses.dataclass
class RulesConfigurationType(ShapeBase):
    """
    A container for rules.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "rules",
                "Rules",
                TypeInfo(typing.List[MappingRule]),
            ),
        ]

    # An array of rules. You can specify up to 25 rules per identity provider.

    # Rules are evaluated in order. The first one to match specifies the role.
    rules: typing.List["MappingRule"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class SetIdentityPoolRolesInput(ShapeBase):
    """
    Input to the `SetIdentityPoolRoles` action.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "identity_pool_id",
                "IdentityPoolId",
                TypeInfo(str),
            ),
            (
                "roles",
                "Roles",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "role_mappings",
                "RoleMappings",
                TypeInfo(typing.Dict[str, RoleMapping]),
            ),
        ]

    # An identity pool ID in the format REGION:GUID.
    identity_pool_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The map of roles associated with this pool. For a given role, the key will
    # be either "authenticated" or "unauthenticated" and the value will be the
    # Role ARN.
    roles: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # How users for a specific identity provider are to mapped to roles. This is
    # a string to RoleMapping object map. The string identifies the identity
    # provider, for example, "graph.facebook.com" or "cognito-idp-
    # east-1.amazonaws.com/us-east-1_abcdefghi:app_client_id".

    # Up to 25 rules can be specified per identity provider.
    role_mappings: typing.Dict[str, "RoleMapping"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class TooManyRequestsException(ShapeBase):
    """
    Thrown when a request is throttled.
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

    # Message returned by a TooManyRequestsException
    message: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class UnlinkDeveloperIdentityInput(ShapeBase):
    """
    Input to the `UnlinkDeveloperIdentity` action.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "identity_id",
                "IdentityId",
                TypeInfo(str),
            ),
            (
                "identity_pool_id",
                "IdentityPoolId",
                TypeInfo(str),
            ),
            (
                "developer_provider_name",
                "DeveloperProviderName",
                TypeInfo(str),
            ),
            (
                "developer_user_identifier",
                "DeveloperUserIdentifier",
                TypeInfo(str),
            ),
        ]

    # A unique identifier in the format REGION:GUID.
    identity_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # An identity pool ID in the format REGION:GUID.
    identity_pool_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The "domain" by which Cognito will refer to your users.
    developer_provider_name: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A unique ID used by your backend authentication process to identify a user.
    developer_user_identifier: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class UnlinkIdentityInput(ShapeBase):
    """
    Input to the UnlinkIdentity action.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "identity_id",
                "IdentityId",
                TypeInfo(str),
            ),
            (
                "logins",
                "Logins",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "logins_to_remove",
                "LoginsToRemove",
                TypeInfo(typing.List[str]),
            ),
        ]

    # A unique identifier in the format REGION:GUID.
    identity_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A set of optional name-value pairs that map provider names to provider
    # tokens.
    logins: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Provider names to unlink from this identity.
    logins_to_remove: typing.List[str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class UnprocessedIdentityId(ShapeBase):
    """
    An array of UnprocessedIdentityId objects, each of which contains an ErrorCode
    and IdentityId.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "identity_id",
                "IdentityId",
                TypeInfo(str),
            ),
            (
                "error_code",
                "ErrorCode",
                TypeInfo(typing.Union[str, ErrorCode]),
            ),
        ]

    # A unique identifier in the format REGION:GUID.
    identity_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The error code indicating the type of error that occurred.
    error_code: typing.Union[str, "ErrorCode"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )
