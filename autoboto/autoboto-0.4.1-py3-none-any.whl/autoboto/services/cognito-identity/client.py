import datetime
import typing
import boto3
from autoboto import ClientBase, ShapeBase, OutputShapeBase
from . import shapes


class Client(ClientBase):
    def __init__(self, *args, **kwargs):
        super().__init__("cognito-identity", *args, **kwargs)

    def create_identity_pool(
        self,
        _request: shapes.CreateIdentityPoolInput = None,
        *,
        identity_pool_name: str,
        allow_unauthenticated_identities: bool,
        supported_login_providers: typing.Dict[str, str] = ShapeBase.NOT_SET,
        developer_provider_name: str = ShapeBase.NOT_SET,
        open_id_connect_provider_arns: typing.List[str] = ShapeBase.NOT_SET,
        cognito_identity_providers: typing.List[shapes.CognitoIdentityProvider
                                               ] = ShapeBase.NOT_SET,
        saml_provider_arns: typing.List[str] = ShapeBase.NOT_SET,
    ) -> shapes.IdentityPool:
        """
        Creates a new identity pool. The identity pool is a store of user identity
        information that is specific to your AWS account. The limit on identity pools is
        60 per account. The keys for `SupportedLoginProviders` are as follows:

          * Facebook: `graph.facebook.com`

          * Google: `accounts.google.com`

          * Amazon: `www.amazon.com`

          * Twitter: `api.twitter.com`

          * Digits: `www.digits.com`

        You must use AWS Developer credentials to call this API.
        """
        if _request is None:
            _params = {}
            if identity_pool_name is not ShapeBase.NOT_SET:
                _params['identity_pool_name'] = identity_pool_name
            if allow_unauthenticated_identities is not ShapeBase.NOT_SET:
                _params['allow_unauthenticated_identities'
                       ] = allow_unauthenticated_identities
            if supported_login_providers is not ShapeBase.NOT_SET:
                _params['supported_login_providers'] = supported_login_providers
            if developer_provider_name is not ShapeBase.NOT_SET:
                _params['developer_provider_name'] = developer_provider_name
            if open_id_connect_provider_arns is not ShapeBase.NOT_SET:
                _params['open_id_connect_provider_arns'
                       ] = open_id_connect_provider_arns
            if cognito_identity_providers is not ShapeBase.NOT_SET:
                _params['cognito_identity_providers'
                       ] = cognito_identity_providers
            if saml_provider_arns is not ShapeBase.NOT_SET:
                _params['saml_provider_arns'] = saml_provider_arns
            _request = shapes.CreateIdentityPoolInput(**_params)
        response = self._boto_client.create_identity_pool(**_request.to_boto())

        return shapes.IdentityPool.from_boto(response)

    def delete_identities(
        self,
        _request: shapes.DeleteIdentitiesInput = None,
        *,
        identity_ids_to_delete: typing.List[str],
    ) -> shapes.DeleteIdentitiesResponse:
        """
        Deletes identities from an identity pool. You can specify a list of 1-60
        identities that you want to delete.

        You must use AWS Developer credentials to call this API.
        """
        if _request is None:
            _params = {}
            if identity_ids_to_delete is not ShapeBase.NOT_SET:
                _params['identity_ids_to_delete'] = identity_ids_to_delete
            _request = shapes.DeleteIdentitiesInput(**_params)
        response = self._boto_client.delete_identities(**_request.to_boto())

        return shapes.DeleteIdentitiesResponse.from_boto(response)

    def delete_identity_pool(
        self,
        _request: shapes.DeleteIdentityPoolInput = None,
        *,
        identity_pool_id: str,
    ) -> None:
        """
        Deletes a user pool. Once a pool is deleted, users will not be able to
        authenticate with the pool.

        You must use AWS Developer credentials to call this API.
        """
        if _request is None:
            _params = {}
            if identity_pool_id is not ShapeBase.NOT_SET:
                _params['identity_pool_id'] = identity_pool_id
            _request = shapes.DeleteIdentityPoolInput(**_params)
        response = self._boto_client.delete_identity_pool(**_request.to_boto())

    def describe_identity(
        self,
        _request: shapes.DescribeIdentityInput = None,
        *,
        identity_id: str,
    ) -> shapes.IdentityDescription:
        """
        Returns metadata related to the given identity, including when the identity was
        created and any associated linked logins.

        You must use AWS Developer credentials to call this API.
        """
        if _request is None:
            _params = {}
            if identity_id is not ShapeBase.NOT_SET:
                _params['identity_id'] = identity_id
            _request = shapes.DescribeIdentityInput(**_params)
        response = self._boto_client.describe_identity(**_request.to_boto())

        return shapes.IdentityDescription.from_boto(response)

    def describe_identity_pool(
        self,
        _request: shapes.DescribeIdentityPoolInput = None,
        *,
        identity_pool_id: str,
    ) -> shapes.IdentityPool:
        """
        Gets details about a particular identity pool, including the pool name, ID
        description, creation date, and current number of users.

        You must use AWS Developer credentials to call this API.
        """
        if _request is None:
            _params = {}
            if identity_pool_id is not ShapeBase.NOT_SET:
                _params['identity_pool_id'] = identity_pool_id
            _request = shapes.DescribeIdentityPoolInput(**_params)
        response = self._boto_client.describe_identity_pool(
            **_request.to_boto()
        )

        return shapes.IdentityPool.from_boto(response)

    def get_credentials_for_identity(
        self,
        _request: shapes.GetCredentialsForIdentityInput = None,
        *,
        identity_id: str,
        logins: typing.Dict[str, str] = ShapeBase.NOT_SET,
        custom_role_arn: str = ShapeBase.NOT_SET,
    ) -> shapes.GetCredentialsForIdentityResponse:
        """
        Returns credentials for the provided identity ID. Any provided logins will be
        validated against supported login providers. If the token is for cognito-
        identity.amazonaws.com, it will be passed through to AWS Security Token Service
        with the appropriate role for the token.

        This is a public API. You do not need any credentials to call this API.
        """
        if _request is None:
            _params = {}
            if identity_id is not ShapeBase.NOT_SET:
                _params['identity_id'] = identity_id
            if logins is not ShapeBase.NOT_SET:
                _params['logins'] = logins
            if custom_role_arn is not ShapeBase.NOT_SET:
                _params['custom_role_arn'] = custom_role_arn
            _request = shapes.GetCredentialsForIdentityInput(**_params)
        response = self._boto_client.get_credentials_for_identity(
            **_request.to_boto()
        )

        return shapes.GetCredentialsForIdentityResponse.from_boto(response)

    def get_id(
        self,
        _request: shapes.GetIdInput = None,
        *,
        identity_pool_id: str,
        account_id: str = ShapeBase.NOT_SET,
        logins: typing.Dict[str, str] = ShapeBase.NOT_SET,
    ) -> shapes.GetIdResponse:
        """
        Generates (or retrieves) a Cognito ID. Supplying multiple logins will create an
        implicit linked account.

        This is a public API. You do not need any credentials to call this API.
        """
        if _request is None:
            _params = {}
            if identity_pool_id is not ShapeBase.NOT_SET:
                _params['identity_pool_id'] = identity_pool_id
            if account_id is not ShapeBase.NOT_SET:
                _params['account_id'] = account_id
            if logins is not ShapeBase.NOT_SET:
                _params['logins'] = logins
            _request = shapes.GetIdInput(**_params)
        response = self._boto_client.get_id(**_request.to_boto())

        return shapes.GetIdResponse.from_boto(response)

    def get_identity_pool_roles(
        self,
        _request: shapes.GetIdentityPoolRolesInput = None,
        *,
        identity_pool_id: str,
    ) -> shapes.GetIdentityPoolRolesResponse:
        """
        Gets the roles for an identity pool.

        You must use AWS Developer credentials to call this API.
        """
        if _request is None:
            _params = {}
            if identity_pool_id is not ShapeBase.NOT_SET:
                _params['identity_pool_id'] = identity_pool_id
            _request = shapes.GetIdentityPoolRolesInput(**_params)
        response = self._boto_client.get_identity_pool_roles(
            **_request.to_boto()
        )

        return shapes.GetIdentityPoolRolesResponse.from_boto(response)

    def get_open_id_token(
        self,
        _request: shapes.GetOpenIdTokenInput = None,
        *,
        identity_id: str,
        logins: typing.Dict[str, str] = ShapeBase.NOT_SET,
    ) -> shapes.GetOpenIdTokenResponse:
        """
        Gets an OpenID token, using a known Cognito ID. This known Cognito ID is
        returned by GetId. You can optionally add additional logins for the identity.
        Supplying multiple logins creates an implicit link.

        The OpenId token is valid for 15 minutes.

        This is a public API. You do not need any credentials to call this API.
        """
        if _request is None:
            _params = {}
            if identity_id is not ShapeBase.NOT_SET:
                _params['identity_id'] = identity_id
            if logins is not ShapeBase.NOT_SET:
                _params['logins'] = logins
            _request = shapes.GetOpenIdTokenInput(**_params)
        response = self._boto_client.get_open_id_token(**_request.to_boto())

        return shapes.GetOpenIdTokenResponse.from_boto(response)

    def get_open_id_token_for_developer_identity(
        self,
        _request: shapes.GetOpenIdTokenForDeveloperIdentityInput = None,
        *,
        identity_pool_id: str,
        logins: typing.Dict[str, str],
        identity_id: str = ShapeBase.NOT_SET,
        token_duration: int = ShapeBase.NOT_SET,
    ) -> shapes.GetOpenIdTokenForDeveloperIdentityResponse:
        """
        Registers (or retrieves) a Cognito `IdentityId` and an OpenID Connect token for
        a user authenticated by your backend authentication process. Supplying multiple
        logins will create an implicit linked account. You can only specify one
        developer provider as part of the `Logins` map, which is linked to the identity
        pool. The developer provider is the "domain" by which Cognito will refer to your
        users.

        You can use `GetOpenIdTokenForDeveloperIdentity` to create a new identity and to
        link new logins (that is, user credentials issued by a public provider or
        developer provider) to an existing identity. When you want to create a new
        identity, the `IdentityId` should be null. When you want to associate a new
        login with an existing authenticated/unauthenticated identity, you can do so by
        providing the existing `IdentityId`. This API will create the identity in the
        specified `IdentityPoolId`.

        You must use AWS Developer credentials to call this API.
        """
        if _request is None:
            _params = {}
            if identity_pool_id is not ShapeBase.NOT_SET:
                _params['identity_pool_id'] = identity_pool_id
            if logins is not ShapeBase.NOT_SET:
                _params['logins'] = logins
            if identity_id is not ShapeBase.NOT_SET:
                _params['identity_id'] = identity_id
            if token_duration is not ShapeBase.NOT_SET:
                _params['token_duration'] = token_duration
            _request = shapes.GetOpenIdTokenForDeveloperIdentityInput(**_params)
        response = self._boto_client.get_open_id_token_for_developer_identity(
            **_request.to_boto()
        )

        return shapes.GetOpenIdTokenForDeveloperIdentityResponse.from_boto(
            response
        )

    def list_identities(
        self,
        _request: shapes.ListIdentitiesInput = None,
        *,
        identity_pool_id: str,
        max_results: int,
        next_token: str = ShapeBase.NOT_SET,
        hide_disabled: bool = ShapeBase.NOT_SET,
    ) -> shapes.ListIdentitiesResponse:
        """
        Lists the identities in a pool.

        You must use AWS Developer credentials to call this API.
        """
        if _request is None:
            _params = {}
            if identity_pool_id is not ShapeBase.NOT_SET:
                _params['identity_pool_id'] = identity_pool_id
            if max_results is not ShapeBase.NOT_SET:
                _params['max_results'] = max_results
            if next_token is not ShapeBase.NOT_SET:
                _params['next_token'] = next_token
            if hide_disabled is not ShapeBase.NOT_SET:
                _params['hide_disabled'] = hide_disabled
            _request = shapes.ListIdentitiesInput(**_params)
        response = self._boto_client.list_identities(**_request.to_boto())

        return shapes.ListIdentitiesResponse.from_boto(response)

    def list_identity_pools(
        self,
        _request: shapes.ListIdentityPoolsInput = None,
        *,
        max_results: int,
        next_token: str = ShapeBase.NOT_SET,
    ) -> shapes.ListIdentityPoolsResponse:
        """
        Lists all of the Cognito identity pools registered for your account.

        You must use AWS Developer credentials to call this API.
        """
        if _request is None:
            _params = {}
            if max_results is not ShapeBase.NOT_SET:
                _params['max_results'] = max_results
            if next_token is not ShapeBase.NOT_SET:
                _params['next_token'] = next_token
            _request = shapes.ListIdentityPoolsInput(**_params)
        response = self._boto_client.list_identity_pools(**_request.to_boto())

        return shapes.ListIdentityPoolsResponse.from_boto(response)

    def lookup_developer_identity(
        self,
        _request: shapes.LookupDeveloperIdentityInput = None,
        *,
        identity_pool_id: str,
        identity_id: str = ShapeBase.NOT_SET,
        developer_user_identifier: str = ShapeBase.NOT_SET,
        max_results: int = ShapeBase.NOT_SET,
        next_token: str = ShapeBase.NOT_SET,
    ) -> shapes.LookupDeveloperIdentityResponse:
        """
        Retrieves the `IdentityID` associated with a `DeveloperUserIdentifier` or the
        list of `DeveloperUserIdentifier`s associated with an `IdentityId` for an
        existing identity. Either `IdentityID` or `DeveloperUserIdentifier` must not be
        null. If you supply only one of these values, the other value will be searched
        in the database and returned as a part of the response. If you supply both,
        `DeveloperUserIdentifier` will be matched against `IdentityID`. If the values
        are verified against the database, the response returns both values and is the
        same as the request. Otherwise a `ResourceConflictException` is thrown.

        You must use AWS Developer credentials to call this API.
        """
        if _request is None:
            _params = {}
            if identity_pool_id is not ShapeBase.NOT_SET:
                _params['identity_pool_id'] = identity_pool_id
            if identity_id is not ShapeBase.NOT_SET:
                _params['identity_id'] = identity_id
            if developer_user_identifier is not ShapeBase.NOT_SET:
                _params['developer_user_identifier'] = developer_user_identifier
            if max_results is not ShapeBase.NOT_SET:
                _params['max_results'] = max_results
            if next_token is not ShapeBase.NOT_SET:
                _params['next_token'] = next_token
            _request = shapes.LookupDeveloperIdentityInput(**_params)
        response = self._boto_client.lookup_developer_identity(
            **_request.to_boto()
        )

        return shapes.LookupDeveloperIdentityResponse.from_boto(response)

    def merge_developer_identities(
        self,
        _request: shapes.MergeDeveloperIdentitiesInput = None,
        *,
        source_user_identifier: str,
        destination_user_identifier: str,
        developer_provider_name: str,
        identity_pool_id: str,
    ) -> shapes.MergeDeveloperIdentitiesResponse:
        """
        Merges two users having different `IdentityId`s, existing in the same identity
        pool, and identified by the same developer provider. You can use this action to
        request that discrete users be merged and identified as a single user in the
        Cognito environment. Cognito associates the given source user
        (`SourceUserIdentifier`) with the `IdentityId` of the
        `DestinationUserIdentifier`. Only developer-authenticated users can be merged.
        If the users to be merged are associated with the same public provider, but as
        two different users, an exception will be thrown.

        You must use AWS Developer credentials to call this API.
        """
        if _request is None:
            _params = {}
            if source_user_identifier is not ShapeBase.NOT_SET:
                _params['source_user_identifier'] = source_user_identifier
            if destination_user_identifier is not ShapeBase.NOT_SET:
                _params['destination_user_identifier'
                       ] = destination_user_identifier
            if developer_provider_name is not ShapeBase.NOT_SET:
                _params['developer_provider_name'] = developer_provider_name
            if identity_pool_id is not ShapeBase.NOT_SET:
                _params['identity_pool_id'] = identity_pool_id
            _request = shapes.MergeDeveloperIdentitiesInput(**_params)
        response = self._boto_client.merge_developer_identities(
            **_request.to_boto()
        )

        return shapes.MergeDeveloperIdentitiesResponse.from_boto(response)

    def set_identity_pool_roles(
        self,
        _request: shapes.SetIdentityPoolRolesInput = None,
        *,
        identity_pool_id: str,
        roles: typing.Dict[str, str],
        role_mappings: typing.Dict[str, shapes.RoleMapping] = ShapeBase.NOT_SET,
    ) -> None:
        """
        Sets the roles for an identity pool. These roles are used when making calls to
        GetCredentialsForIdentity action.

        You must use AWS Developer credentials to call this API.
        """
        if _request is None:
            _params = {}
            if identity_pool_id is not ShapeBase.NOT_SET:
                _params['identity_pool_id'] = identity_pool_id
            if roles is not ShapeBase.NOT_SET:
                _params['roles'] = roles
            if role_mappings is not ShapeBase.NOT_SET:
                _params['role_mappings'] = role_mappings
            _request = shapes.SetIdentityPoolRolesInput(**_params)
        response = self._boto_client.set_identity_pool_roles(
            **_request.to_boto()
        )

    def unlink_developer_identity(
        self,
        _request: shapes.UnlinkDeveloperIdentityInput = None,
        *,
        identity_id: str,
        identity_pool_id: str,
        developer_provider_name: str,
        developer_user_identifier: str,
    ) -> None:
        """
        Unlinks a `DeveloperUserIdentifier` from an existing identity. Unlinked
        developer users will be considered new identities next time they are seen. If,
        for a given Cognito identity, you remove all federated identities as well as the
        developer user identifier, the Cognito identity becomes inaccessible.

        You must use AWS Developer credentials to call this API.
        """
        if _request is None:
            _params = {}
            if identity_id is not ShapeBase.NOT_SET:
                _params['identity_id'] = identity_id
            if identity_pool_id is not ShapeBase.NOT_SET:
                _params['identity_pool_id'] = identity_pool_id
            if developer_provider_name is not ShapeBase.NOT_SET:
                _params['developer_provider_name'] = developer_provider_name
            if developer_user_identifier is not ShapeBase.NOT_SET:
                _params['developer_user_identifier'] = developer_user_identifier
            _request = shapes.UnlinkDeveloperIdentityInput(**_params)
        response = self._boto_client.unlink_developer_identity(
            **_request.to_boto()
        )

    def unlink_identity(
        self,
        _request: shapes.UnlinkIdentityInput = None,
        *,
        identity_id: str,
        logins: typing.Dict[str, str],
        logins_to_remove: typing.List[str],
    ) -> None:
        """
        Unlinks a federated identity from an existing account. Unlinked logins will be
        considered new identities next time they are seen. Removing the last linked
        login will make this identity inaccessible.

        This is a public API. You do not need any credentials to call this API.
        """
        if _request is None:
            _params = {}
            if identity_id is not ShapeBase.NOT_SET:
                _params['identity_id'] = identity_id
            if logins is not ShapeBase.NOT_SET:
                _params['logins'] = logins
            if logins_to_remove is not ShapeBase.NOT_SET:
                _params['logins_to_remove'] = logins_to_remove
            _request = shapes.UnlinkIdentityInput(**_params)
        response = self._boto_client.unlink_identity(**_request.to_boto())

    def update_identity_pool(
        self,
        _request: shapes.IdentityPool = None,
        *,
        response_metadata: typing.Dict[str, str],
        identity_pool_id: str,
        identity_pool_name: str,
        allow_unauthenticated_identities: bool,
        supported_login_providers: typing.Dict[str, str] = ShapeBase.NOT_SET,
        developer_provider_name: str = ShapeBase.NOT_SET,
        open_id_connect_provider_arns: typing.List[str] = ShapeBase.NOT_SET,
        cognito_identity_providers: typing.List[shapes.CognitoIdentityProvider
                                               ] = ShapeBase.NOT_SET,
        saml_provider_arns: typing.List[str] = ShapeBase.NOT_SET,
    ) -> shapes.IdentityPool:
        """
        Updates a user pool.

        You must use AWS Developer credentials to call this API.
        """
        if _request is None:
            _params = {}
            if response_metadata is not ShapeBase.NOT_SET:
                _params['response_metadata'] = response_metadata
            if identity_pool_id is not ShapeBase.NOT_SET:
                _params['identity_pool_id'] = identity_pool_id
            if identity_pool_name is not ShapeBase.NOT_SET:
                _params['identity_pool_name'] = identity_pool_name
            if allow_unauthenticated_identities is not ShapeBase.NOT_SET:
                _params['allow_unauthenticated_identities'
                       ] = allow_unauthenticated_identities
            if supported_login_providers is not ShapeBase.NOT_SET:
                _params['supported_login_providers'] = supported_login_providers
            if developer_provider_name is not ShapeBase.NOT_SET:
                _params['developer_provider_name'] = developer_provider_name
            if open_id_connect_provider_arns is not ShapeBase.NOT_SET:
                _params['open_id_connect_provider_arns'
                       ] = open_id_connect_provider_arns
            if cognito_identity_providers is not ShapeBase.NOT_SET:
                _params['cognito_identity_providers'
                       ] = cognito_identity_providers
            if saml_provider_arns is not ShapeBase.NOT_SET:
                _params['saml_provider_arns'] = saml_provider_arns
            _request = shapes.IdentityPool(**_params)
        response = self._boto_client.update_identity_pool(**_request.to_boto())

        return shapes.IdentityPool.from_boto(response)
