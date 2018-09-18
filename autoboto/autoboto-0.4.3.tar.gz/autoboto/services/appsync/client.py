import datetime
import typing
import boto3
from autoboto import ClientBase, ShapeBase, OutputShapeBase
from . import shapes


class Client(ClientBase):
    def __init__(self, *args, **kwargs):
        super().__init__("appsync", *args, **kwargs)

    def create_api_key(
        self,
        _request: shapes.CreateApiKeyRequest = None,
        *,
        api_id: str,
        description: str = ShapeBase.NOT_SET,
        expires: int = ShapeBase.NOT_SET,
    ) -> shapes.CreateApiKeyResponse:
        """
        Creates a unique key that you can distribute to clients who are executing your
        API.
        """
        if _request is None:
            _params = {}
            if api_id is not ShapeBase.NOT_SET:
                _params['api_id'] = api_id
            if description is not ShapeBase.NOT_SET:
                _params['description'] = description
            if expires is not ShapeBase.NOT_SET:
                _params['expires'] = expires
            _request = shapes.CreateApiKeyRequest(**_params)
        response = self._boto_client.create_api_key(**_request.to_boto())

        return shapes.CreateApiKeyResponse.from_boto(response)

    def create_data_source(
        self,
        _request: shapes.CreateDataSourceRequest = None,
        *,
        api_id: str,
        name: str,
        type: typing.Union[str, shapes.DataSourceType],
        description: str = ShapeBase.NOT_SET,
        service_role_arn: str = ShapeBase.NOT_SET,
        dynamodb_config: shapes.DynamodbDataSourceConfig = ShapeBase.NOT_SET,
        lambda_config: shapes.LambdaDataSourceConfig = ShapeBase.NOT_SET,
        elasticsearch_config: shapes.ElasticsearchDataSourceConfig = ShapeBase.
        NOT_SET,
        http_config: shapes.HttpDataSourceConfig = ShapeBase.NOT_SET,
    ) -> shapes.CreateDataSourceResponse:
        """
        Creates a `DataSource` object.
        """
        if _request is None:
            _params = {}
            if api_id is not ShapeBase.NOT_SET:
                _params['api_id'] = api_id
            if name is not ShapeBase.NOT_SET:
                _params['name'] = name
            if type is not ShapeBase.NOT_SET:
                _params['type'] = type
            if description is not ShapeBase.NOT_SET:
                _params['description'] = description
            if service_role_arn is not ShapeBase.NOT_SET:
                _params['service_role_arn'] = service_role_arn
            if dynamodb_config is not ShapeBase.NOT_SET:
                _params['dynamodb_config'] = dynamodb_config
            if lambda_config is not ShapeBase.NOT_SET:
                _params['lambda_config'] = lambda_config
            if elasticsearch_config is not ShapeBase.NOT_SET:
                _params['elasticsearch_config'] = elasticsearch_config
            if http_config is not ShapeBase.NOT_SET:
                _params['http_config'] = http_config
            _request = shapes.CreateDataSourceRequest(**_params)
        response = self._boto_client.create_data_source(**_request.to_boto())

        return shapes.CreateDataSourceResponse.from_boto(response)

    def create_graphql_api(
        self,
        _request: shapes.CreateGraphqlApiRequest = None,
        *,
        name: str,
        authentication_type: typing.Union[str, shapes.AuthenticationType],
        log_config: shapes.LogConfig = ShapeBase.NOT_SET,
        user_pool_config: shapes.UserPoolConfig = ShapeBase.NOT_SET,
        open_id_connect_config: shapes.OpenIDConnectConfig = ShapeBase.NOT_SET,
    ) -> shapes.CreateGraphqlApiResponse:
        """
        Creates a `GraphqlApi` object.
        """
        if _request is None:
            _params = {}
            if name is not ShapeBase.NOT_SET:
                _params['name'] = name
            if authentication_type is not ShapeBase.NOT_SET:
                _params['authentication_type'] = authentication_type
            if log_config is not ShapeBase.NOT_SET:
                _params['log_config'] = log_config
            if user_pool_config is not ShapeBase.NOT_SET:
                _params['user_pool_config'] = user_pool_config
            if open_id_connect_config is not ShapeBase.NOT_SET:
                _params['open_id_connect_config'] = open_id_connect_config
            _request = shapes.CreateGraphqlApiRequest(**_params)
        response = self._boto_client.create_graphql_api(**_request.to_boto())

        return shapes.CreateGraphqlApiResponse.from_boto(response)

    def create_resolver(
        self,
        _request: shapes.CreateResolverRequest = None,
        *,
        api_id: str,
        type_name: str,
        field_name: str,
        data_source_name: str,
        request_mapping_template: str,
        response_mapping_template: str = ShapeBase.NOT_SET,
    ) -> shapes.CreateResolverResponse:
        """
        Creates a `Resolver` object.

        A resolver converts incoming requests into a format that a data source can
        understand and converts the data source's responses into GraphQL.
        """
        if _request is None:
            _params = {}
            if api_id is not ShapeBase.NOT_SET:
                _params['api_id'] = api_id
            if type_name is not ShapeBase.NOT_SET:
                _params['type_name'] = type_name
            if field_name is not ShapeBase.NOT_SET:
                _params['field_name'] = field_name
            if data_source_name is not ShapeBase.NOT_SET:
                _params['data_source_name'] = data_source_name
            if request_mapping_template is not ShapeBase.NOT_SET:
                _params['request_mapping_template'] = request_mapping_template
            if response_mapping_template is not ShapeBase.NOT_SET:
                _params['response_mapping_template'] = response_mapping_template
            _request = shapes.CreateResolverRequest(**_params)
        response = self._boto_client.create_resolver(**_request.to_boto())

        return shapes.CreateResolverResponse.from_boto(response)

    def create_type(
        self,
        _request: shapes.CreateTypeRequest = None,
        *,
        api_id: str,
        definition: str,
        format: typing.Union[str, shapes.TypeDefinitionFormat],
    ) -> shapes.CreateTypeResponse:
        """
        Creates a `Type` object.
        """
        if _request is None:
            _params = {}
            if api_id is not ShapeBase.NOT_SET:
                _params['api_id'] = api_id
            if definition is not ShapeBase.NOT_SET:
                _params['definition'] = definition
            if format is not ShapeBase.NOT_SET:
                _params['format'] = format
            _request = shapes.CreateTypeRequest(**_params)
        response = self._boto_client.create_type(**_request.to_boto())

        return shapes.CreateTypeResponse.from_boto(response)

    def delete_api_key(
        self,
        _request: shapes.DeleteApiKeyRequest = None,
        *,
        api_id: str,
        id: str,
    ) -> shapes.DeleteApiKeyResponse:
        """
        Deletes an API key.
        """
        if _request is None:
            _params = {}
            if api_id is not ShapeBase.NOT_SET:
                _params['api_id'] = api_id
            if id is not ShapeBase.NOT_SET:
                _params['id'] = id
            _request = shapes.DeleteApiKeyRequest(**_params)
        response = self._boto_client.delete_api_key(**_request.to_boto())

        return shapes.DeleteApiKeyResponse.from_boto(response)

    def delete_data_source(
        self,
        _request: shapes.DeleteDataSourceRequest = None,
        *,
        api_id: str,
        name: str,
    ) -> shapes.DeleteDataSourceResponse:
        """
        Deletes a `DataSource` object.
        """
        if _request is None:
            _params = {}
            if api_id is not ShapeBase.NOT_SET:
                _params['api_id'] = api_id
            if name is not ShapeBase.NOT_SET:
                _params['name'] = name
            _request = shapes.DeleteDataSourceRequest(**_params)
        response = self._boto_client.delete_data_source(**_request.to_boto())

        return shapes.DeleteDataSourceResponse.from_boto(response)

    def delete_graphql_api(
        self,
        _request: shapes.DeleteGraphqlApiRequest = None,
        *,
        api_id: str,
    ) -> shapes.DeleteGraphqlApiResponse:
        """
        Deletes a `GraphqlApi` object.
        """
        if _request is None:
            _params = {}
            if api_id is not ShapeBase.NOT_SET:
                _params['api_id'] = api_id
            _request = shapes.DeleteGraphqlApiRequest(**_params)
        response = self._boto_client.delete_graphql_api(**_request.to_boto())

        return shapes.DeleteGraphqlApiResponse.from_boto(response)

    def delete_resolver(
        self,
        _request: shapes.DeleteResolverRequest = None,
        *,
        api_id: str,
        type_name: str,
        field_name: str,
    ) -> shapes.DeleteResolverResponse:
        """
        Deletes a `Resolver` object.
        """
        if _request is None:
            _params = {}
            if api_id is not ShapeBase.NOT_SET:
                _params['api_id'] = api_id
            if type_name is not ShapeBase.NOT_SET:
                _params['type_name'] = type_name
            if field_name is not ShapeBase.NOT_SET:
                _params['field_name'] = field_name
            _request = shapes.DeleteResolverRequest(**_params)
        response = self._boto_client.delete_resolver(**_request.to_boto())

        return shapes.DeleteResolverResponse.from_boto(response)

    def delete_type(
        self,
        _request: shapes.DeleteTypeRequest = None,
        *,
        api_id: str,
        type_name: str,
    ) -> shapes.DeleteTypeResponse:
        """
        Deletes a `Type` object.
        """
        if _request is None:
            _params = {}
            if api_id is not ShapeBase.NOT_SET:
                _params['api_id'] = api_id
            if type_name is not ShapeBase.NOT_SET:
                _params['type_name'] = type_name
            _request = shapes.DeleteTypeRequest(**_params)
        response = self._boto_client.delete_type(**_request.to_boto())

        return shapes.DeleteTypeResponse.from_boto(response)

    def get_data_source(
        self,
        _request: shapes.GetDataSourceRequest = None,
        *,
        api_id: str,
        name: str,
    ) -> shapes.GetDataSourceResponse:
        """
        Retrieves a `DataSource` object.
        """
        if _request is None:
            _params = {}
            if api_id is not ShapeBase.NOT_SET:
                _params['api_id'] = api_id
            if name is not ShapeBase.NOT_SET:
                _params['name'] = name
            _request = shapes.GetDataSourceRequest(**_params)
        response = self._boto_client.get_data_source(**_request.to_boto())

        return shapes.GetDataSourceResponse.from_boto(response)

    def get_graphql_api(
        self,
        _request: shapes.GetGraphqlApiRequest = None,
        *,
        api_id: str,
    ) -> shapes.GetGraphqlApiResponse:
        """
        Retrieves a `GraphqlApi` object.
        """
        if _request is None:
            _params = {}
            if api_id is not ShapeBase.NOT_SET:
                _params['api_id'] = api_id
            _request = shapes.GetGraphqlApiRequest(**_params)
        response = self._boto_client.get_graphql_api(**_request.to_boto())

        return shapes.GetGraphqlApiResponse.from_boto(response)

    def get_introspection_schema(
        self,
        _request: shapes.GetIntrospectionSchemaRequest = None,
        *,
        api_id: str,
        format: typing.Union[str, shapes.OutputType],
    ) -> shapes.GetIntrospectionSchemaResponse:
        """
        Retrieves the introspection schema for a GraphQL API.
        """
        if _request is None:
            _params = {}
            if api_id is not ShapeBase.NOT_SET:
                _params['api_id'] = api_id
            if format is not ShapeBase.NOT_SET:
                _params['format'] = format
            _request = shapes.GetIntrospectionSchemaRequest(**_params)
        response = self._boto_client.get_introspection_schema(
            **_request.to_boto()
        )

        return shapes.GetIntrospectionSchemaResponse.from_boto(response)

    def get_resolver(
        self,
        _request: shapes.GetResolverRequest = None,
        *,
        api_id: str,
        type_name: str,
        field_name: str,
    ) -> shapes.GetResolverResponse:
        """
        Retrieves a `Resolver` object.
        """
        if _request is None:
            _params = {}
            if api_id is not ShapeBase.NOT_SET:
                _params['api_id'] = api_id
            if type_name is not ShapeBase.NOT_SET:
                _params['type_name'] = type_name
            if field_name is not ShapeBase.NOT_SET:
                _params['field_name'] = field_name
            _request = shapes.GetResolverRequest(**_params)
        response = self._boto_client.get_resolver(**_request.to_boto())

        return shapes.GetResolverResponse.from_boto(response)

    def get_schema_creation_status(
        self,
        _request: shapes.GetSchemaCreationStatusRequest = None,
        *,
        api_id: str,
    ) -> shapes.GetSchemaCreationStatusResponse:
        """
        Retrieves the current status of a schema creation operation.
        """
        if _request is None:
            _params = {}
            if api_id is not ShapeBase.NOT_SET:
                _params['api_id'] = api_id
            _request = shapes.GetSchemaCreationStatusRequest(**_params)
        response = self._boto_client.get_schema_creation_status(
            **_request.to_boto()
        )

        return shapes.GetSchemaCreationStatusResponse.from_boto(response)

    def get_type(
        self,
        _request: shapes.GetTypeRequest = None,
        *,
        api_id: str,
        type_name: str,
        format: typing.Union[str, shapes.TypeDefinitionFormat],
    ) -> shapes.GetTypeResponse:
        """
        Retrieves a `Type` object.
        """
        if _request is None:
            _params = {}
            if api_id is not ShapeBase.NOT_SET:
                _params['api_id'] = api_id
            if type_name is not ShapeBase.NOT_SET:
                _params['type_name'] = type_name
            if format is not ShapeBase.NOT_SET:
                _params['format'] = format
            _request = shapes.GetTypeRequest(**_params)
        response = self._boto_client.get_type(**_request.to_boto())

        return shapes.GetTypeResponse.from_boto(response)

    def list_api_keys(
        self,
        _request: shapes.ListApiKeysRequest = None,
        *,
        api_id: str,
        next_token: str = ShapeBase.NOT_SET,
        max_results: int = ShapeBase.NOT_SET,
    ) -> shapes.ListApiKeysResponse:
        """
        Lists the API keys for a given API.

        API keys are deleted automatically sometime after they expire. However, they may
        still be included in the response until they have actually been deleted. You can
        safely call `DeleteApiKey` to manually delete a key before it's automatically
        deleted.
        """
        if _request is None:
            _params = {}
            if api_id is not ShapeBase.NOT_SET:
                _params['api_id'] = api_id
            if next_token is not ShapeBase.NOT_SET:
                _params['next_token'] = next_token
            if max_results is not ShapeBase.NOT_SET:
                _params['max_results'] = max_results
            _request = shapes.ListApiKeysRequest(**_params)
        response = self._boto_client.list_api_keys(**_request.to_boto())

        return shapes.ListApiKeysResponse.from_boto(response)

    def list_data_sources(
        self,
        _request: shapes.ListDataSourcesRequest = None,
        *,
        api_id: str,
        next_token: str = ShapeBase.NOT_SET,
        max_results: int = ShapeBase.NOT_SET,
    ) -> shapes.ListDataSourcesResponse:
        """
        Lists the data sources for a given API.
        """
        if _request is None:
            _params = {}
            if api_id is not ShapeBase.NOT_SET:
                _params['api_id'] = api_id
            if next_token is not ShapeBase.NOT_SET:
                _params['next_token'] = next_token
            if max_results is not ShapeBase.NOT_SET:
                _params['max_results'] = max_results
            _request = shapes.ListDataSourcesRequest(**_params)
        response = self._boto_client.list_data_sources(**_request.to_boto())

        return shapes.ListDataSourcesResponse.from_boto(response)

    def list_graphql_apis(
        self,
        _request: shapes.ListGraphqlApisRequest = None,
        *,
        next_token: str = ShapeBase.NOT_SET,
        max_results: int = ShapeBase.NOT_SET,
    ) -> shapes.ListGraphqlApisResponse:
        """
        Lists your GraphQL APIs.
        """
        if _request is None:
            _params = {}
            if next_token is not ShapeBase.NOT_SET:
                _params['next_token'] = next_token
            if max_results is not ShapeBase.NOT_SET:
                _params['max_results'] = max_results
            _request = shapes.ListGraphqlApisRequest(**_params)
        response = self._boto_client.list_graphql_apis(**_request.to_boto())

        return shapes.ListGraphqlApisResponse.from_boto(response)

    def list_resolvers(
        self,
        _request: shapes.ListResolversRequest = None,
        *,
        api_id: str,
        type_name: str,
        next_token: str = ShapeBase.NOT_SET,
        max_results: int = ShapeBase.NOT_SET,
    ) -> shapes.ListResolversResponse:
        """
        Lists the resolvers for a given API and type.
        """
        if _request is None:
            _params = {}
            if api_id is not ShapeBase.NOT_SET:
                _params['api_id'] = api_id
            if type_name is not ShapeBase.NOT_SET:
                _params['type_name'] = type_name
            if next_token is not ShapeBase.NOT_SET:
                _params['next_token'] = next_token
            if max_results is not ShapeBase.NOT_SET:
                _params['max_results'] = max_results
            _request = shapes.ListResolversRequest(**_params)
        response = self._boto_client.list_resolvers(**_request.to_boto())

        return shapes.ListResolversResponse.from_boto(response)

    def list_types(
        self,
        _request: shapes.ListTypesRequest = None,
        *,
        api_id: str,
        format: typing.Union[str, shapes.TypeDefinitionFormat],
        next_token: str = ShapeBase.NOT_SET,
        max_results: int = ShapeBase.NOT_SET,
    ) -> shapes.ListTypesResponse:
        """
        Lists the types for a given API.
        """
        if _request is None:
            _params = {}
            if api_id is not ShapeBase.NOT_SET:
                _params['api_id'] = api_id
            if format is not ShapeBase.NOT_SET:
                _params['format'] = format
            if next_token is not ShapeBase.NOT_SET:
                _params['next_token'] = next_token
            if max_results is not ShapeBase.NOT_SET:
                _params['max_results'] = max_results
            _request = shapes.ListTypesRequest(**_params)
        response = self._boto_client.list_types(**_request.to_boto())

        return shapes.ListTypesResponse.from_boto(response)

    def start_schema_creation(
        self,
        _request: shapes.StartSchemaCreationRequest = None,
        *,
        api_id: str,
        definition: typing.Any,
    ) -> shapes.StartSchemaCreationResponse:
        """
        Adds a new schema to your GraphQL API.

        This operation is asynchronous. Use to determine when it has completed.
        """
        if _request is None:
            _params = {}
            if api_id is not ShapeBase.NOT_SET:
                _params['api_id'] = api_id
            if definition is not ShapeBase.NOT_SET:
                _params['definition'] = definition
            _request = shapes.StartSchemaCreationRequest(**_params)
        response = self._boto_client.start_schema_creation(**_request.to_boto())

        return shapes.StartSchemaCreationResponse.from_boto(response)

    def update_api_key(
        self,
        _request: shapes.UpdateApiKeyRequest = None,
        *,
        api_id: str,
        id: str,
        description: str = ShapeBase.NOT_SET,
        expires: int = ShapeBase.NOT_SET,
    ) -> shapes.UpdateApiKeyResponse:
        """
        Updates an API key.
        """
        if _request is None:
            _params = {}
            if api_id is not ShapeBase.NOT_SET:
                _params['api_id'] = api_id
            if id is not ShapeBase.NOT_SET:
                _params['id'] = id
            if description is not ShapeBase.NOT_SET:
                _params['description'] = description
            if expires is not ShapeBase.NOT_SET:
                _params['expires'] = expires
            _request = shapes.UpdateApiKeyRequest(**_params)
        response = self._boto_client.update_api_key(**_request.to_boto())

        return shapes.UpdateApiKeyResponse.from_boto(response)

    def update_data_source(
        self,
        _request: shapes.UpdateDataSourceRequest = None,
        *,
        api_id: str,
        name: str,
        type: typing.Union[str, shapes.DataSourceType],
        description: str = ShapeBase.NOT_SET,
        service_role_arn: str = ShapeBase.NOT_SET,
        dynamodb_config: shapes.DynamodbDataSourceConfig = ShapeBase.NOT_SET,
        lambda_config: shapes.LambdaDataSourceConfig = ShapeBase.NOT_SET,
        elasticsearch_config: shapes.ElasticsearchDataSourceConfig = ShapeBase.
        NOT_SET,
        http_config: shapes.HttpDataSourceConfig = ShapeBase.NOT_SET,
    ) -> shapes.UpdateDataSourceResponse:
        """
        Updates a `DataSource` object.
        """
        if _request is None:
            _params = {}
            if api_id is not ShapeBase.NOT_SET:
                _params['api_id'] = api_id
            if name is not ShapeBase.NOT_SET:
                _params['name'] = name
            if type is not ShapeBase.NOT_SET:
                _params['type'] = type
            if description is not ShapeBase.NOT_SET:
                _params['description'] = description
            if service_role_arn is not ShapeBase.NOT_SET:
                _params['service_role_arn'] = service_role_arn
            if dynamodb_config is not ShapeBase.NOT_SET:
                _params['dynamodb_config'] = dynamodb_config
            if lambda_config is not ShapeBase.NOT_SET:
                _params['lambda_config'] = lambda_config
            if elasticsearch_config is not ShapeBase.NOT_SET:
                _params['elasticsearch_config'] = elasticsearch_config
            if http_config is not ShapeBase.NOT_SET:
                _params['http_config'] = http_config
            _request = shapes.UpdateDataSourceRequest(**_params)
        response = self._boto_client.update_data_source(**_request.to_boto())

        return shapes.UpdateDataSourceResponse.from_boto(response)

    def update_graphql_api(
        self,
        _request: shapes.UpdateGraphqlApiRequest = None,
        *,
        api_id: str,
        name: str,
        log_config: shapes.LogConfig = ShapeBase.NOT_SET,
        authentication_type: typing.
        Union[str, shapes.AuthenticationType] = ShapeBase.NOT_SET,
        user_pool_config: shapes.UserPoolConfig = ShapeBase.NOT_SET,
        open_id_connect_config: shapes.OpenIDConnectConfig = ShapeBase.NOT_SET,
    ) -> shapes.UpdateGraphqlApiResponse:
        """
        Updates a `GraphqlApi` object.
        """
        if _request is None:
            _params = {}
            if api_id is not ShapeBase.NOT_SET:
                _params['api_id'] = api_id
            if name is not ShapeBase.NOT_SET:
                _params['name'] = name
            if log_config is not ShapeBase.NOT_SET:
                _params['log_config'] = log_config
            if authentication_type is not ShapeBase.NOT_SET:
                _params['authentication_type'] = authentication_type
            if user_pool_config is not ShapeBase.NOT_SET:
                _params['user_pool_config'] = user_pool_config
            if open_id_connect_config is not ShapeBase.NOT_SET:
                _params['open_id_connect_config'] = open_id_connect_config
            _request = shapes.UpdateGraphqlApiRequest(**_params)
        response = self._boto_client.update_graphql_api(**_request.to_boto())

        return shapes.UpdateGraphqlApiResponse.from_boto(response)

    def update_resolver(
        self,
        _request: shapes.UpdateResolverRequest = None,
        *,
        api_id: str,
        type_name: str,
        field_name: str,
        data_source_name: str,
        request_mapping_template: str,
        response_mapping_template: str = ShapeBase.NOT_SET,
    ) -> shapes.UpdateResolverResponse:
        """
        Updates a `Resolver` object.
        """
        if _request is None:
            _params = {}
            if api_id is not ShapeBase.NOT_SET:
                _params['api_id'] = api_id
            if type_name is not ShapeBase.NOT_SET:
                _params['type_name'] = type_name
            if field_name is not ShapeBase.NOT_SET:
                _params['field_name'] = field_name
            if data_source_name is not ShapeBase.NOT_SET:
                _params['data_source_name'] = data_source_name
            if request_mapping_template is not ShapeBase.NOT_SET:
                _params['request_mapping_template'] = request_mapping_template
            if response_mapping_template is not ShapeBase.NOT_SET:
                _params['response_mapping_template'] = response_mapping_template
            _request = shapes.UpdateResolverRequest(**_params)
        response = self._boto_client.update_resolver(**_request.to_boto())

        return shapes.UpdateResolverResponse.from_boto(response)

    def update_type(
        self,
        _request: shapes.UpdateTypeRequest = None,
        *,
        api_id: str,
        type_name: str,
        format: typing.Union[str, shapes.TypeDefinitionFormat],
        definition: str = ShapeBase.NOT_SET,
    ) -> shapes.UpdateTypeResponse:
        """
        Updates a `Type` object.
        """
        if _request is None:
            _params = {}
            if api_id is not ShapeBase.NOT_SET:
                _params['api_id'] = api_id
            if type_name is not ShapeBase.NOT_SET:
                _params['type_name'] = type_name
            if format is not ShapeBase.NOT_SET:
                _params['format'] = format
            if definition is not ShapeBase.NOT_SET:
                _params['definition'] = definition
            _request = shapes.UpdateTypeRequest(**_params)
        response = self._boto_client.update_type(**_request.to_boto())

        return shapes.UpdateTypeResponse.from_boto(response)
