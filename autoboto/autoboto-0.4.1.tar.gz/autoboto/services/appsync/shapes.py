import datetime
import typing
from autoboto import ShapeBase, OutputShapeBase, TypeInfo
import botocore.response
import dataclasses


@dataclasses.dataclass
class ApiKey(ShapeBase):
    """
    Describes an API key.

    Customers invoke AWS AppSync GraphQL APIs with API keys as an identity
    mechanism. There are two key versions:

    **da1** : This version was introduced at launch in November 2017. These keys
    always expire after 7 days. Key expiration is managed by DynamoDB TTL. The keys
    will cease to be valid after Feb 21, 2018 and should not be used after that
    date.

      * `ListApiKeys` returns the expiration time in milliseconds.

      * `CreateApiKey` returns the expiration time in milliseconds.

      * `UpdateApiKey` is not available for this key version.

      * `DeleteApiKey` deletes the item from the table.

      * Expiration is stored in DynamoDB as milliseconds. This results in a bug where keys are not automatically deleted because DynamoDB expects the TTL to be stored in seconds. As a one-time action, we will delete these keys from the table after Feb 21, 2018.

    **da2** : This version was introduced in February 2018 when AppSync added
    support to extend key expiration.

      * `ListApiKeys` returns the expiration time in seconds.

      * `CreateApiKey` returns the expiration time in seconds and accepts a user-provided expiration time in seconds.

      * `UpdateApiKey` returns the expiration time in seconds and accepts a user-provided expiration time in seconds. Key expiration can only be updated while the key has not expired.

      * `DeleteApiKey` deletes the item from the table.

      * Expiration is stored in DynamoDB as seconds.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "id",
                "id",
                TypeInfo(str),
            ),
            (
                "description",
                "description",
                TypeInfo(str),
            ),
            (
                "expires",
                "expires",
                TypeInfo(int),
            ),
        ]

    # The API key ID.
    id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A description of the purpose of the API key.
    description: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The time after which the API key expires. The date is represented as
    # seconds since the epoch, rounded down to the nearest hour.
    expires: int = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ApiKeyLimitExceededException(ShapeBase):
    """
    The API key exceeded a limit. Try your request again.
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
class ApiKeyValidityOutOfBoundsException(ShapeBase):
    """
    The API key expiration must be set to a value between 1 and 365 days from
    creation (for `CreateApiKey`) or from update (for `UpdateApiKey`).
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
class ApiLimitExceededException(ShapeBase):
    """
    The GraphQL API exceeded a limit. Try your request again.
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


class AuthenticationType(str):
    API_KEY = "API_KEY"
    AWS_IAM = "AWS_IAM"
    AMAZON_COGNITO_USER_POOLS = "AMAZON_COGNITO_USER_POOLS"
    OPENID_CONNECT = "OPENID_CONNECT"


@dataclasses.dataclass
class BadRequestException(ShapeBase):
    """
    The request is not well formed. For example, a value is invalid or a required
    field is missing. Check the field values, and try again.
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


class Blob(botocore.response.StreamingBody):
    pass


@dataclasses.dataclass
class ConcurrentModificationException(ShapeBase):
    """
    Another modification is being made. That modification must complete before you
    can make your change.
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
class CreateApiKeyRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "api_id",
                "apiId",
                TypeInfo(str),
            ),
            (
                "description",
                "description",
                TypeInfo(str),
            ),
            (
                "expires",
                "expires",
                TypeInfo(int),
            ),
        ]

    # The ID for your GraphQL API.
    api_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A description of the purpose of the API key.
    description: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The time from creation time after which the API key expires. The date is
    # represented as seconds since the epoch, rounded down to the nearest hour.
    # The default value for this parameter is 7 days from creation time. For more
    # information, see .
    expires: int = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class CreateApiKeyResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "api_key",
                "apiKey",
                TypeInfo(ApiKey),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The API key.
    api_key: "ApiKey" = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class CreateDataSourceRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "api_id",
                "apiId",
                TypeInfo(str),
            ),
            (
                "name",
                "name",
                TypeInfo(str),
            ),
            (
                "type",
                "type",
                TypeInfo(typing.Union[str, DataSourceType]),
            ),
            (
                "description",
                "description",
                TypeInfo(str),
            ),
            (
                "service_role_arn",
                "serviceRoleArn",
                TypeInfo(str),
            ),
            (
                "dynamodb_config",
                "dynamodbConfig",
                TypeInfo(DynamodbDataSourceConfig),
            ),
            (
                "lambda_config",
                "lambdaConfig",
                TypeInfo(LambdaDataSourceConfig),
            ),
            (
                "elasticsearch_config",
                "elasticsearchConfig",
                TypeInfo(ElasticsearchDataSourceConfig),
            ),
            (
                "http_config",
                "httpConfig",
                TypeInfo(HttpDataSourceConfig),
            ),
        ]

    # The API ID for the GraphQL API for the `DataSource`.
    api_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A user-supplied name for the `DataSource`.
    name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The type of the `DataSource`.
    type: typing.Union[str, "DataSourceType"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A description of the `DataSource`.
    description: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The IAM service role ARN for the data source. The system assumes this role
    # when accessing the data source.
    service_role_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # DynamoDB settings.
    dynamodb_config: "DynamodbDataSourceConfig" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # AWS Lambda settings.
    lambda_config: "LambdaDataSourceConfig" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Amazon Elasticsearch settings.
    elasticsearch_config: "ElasticsearchDataSourceConfig" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Http endpoint settings.
    http_config: "HttpDataSourceConfig" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class CreateDataSourceResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "data_source",
                "dataSource",
                TypeInfo(DataSource),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The `DataSource` object.
    data_source: "DataSource" = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class CreateGraphqlApiRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "name",
                "name",
                TypeInfo(str),
            ),
            (
                "authentication_type",
                "authenticationType",
                TypeInfo(typing.Union[str, AuthenticationType]),
            ),
            (
                "log_config",
                "logConfig",
                TypeInfo(LogConfig),
            ),
            (
                "user_pool_config",
                "userPoolConfig",
                TypeInfo(UserPoolConfig),
            ),
            (
                "open_id_connect_config",
                "openIDConnectConfig",
                TypeInfo(OpenIDConnectConfig),
            ),
        ]

    # A user-supplied name for the `GraphqlApi`.
    name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The authentication type: API key, IAM, or Amazon Cognito User Pools.
    authentication_type: typing.Union[str, "AuthenticationType"
                                     ] = dataclasses.field(
                                         default=ShapeBase.NOT_SET,
                                     )

    # The Amazon CloudWatch logs configuration.
    log_config: "LogConfig" = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The Amazon Cognito User Pool configuration.
    user_pool_config: "UserPoolConfig" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The Open Id Connect configuration configuration.
    open_id_connect_config: "OpenIDConnectConfig" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class CreateGraphqlApiResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "graphql_api",
                "graphqlApi",
                TypeInfo(GraphqlApi),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The `GraphqlApi`.
    graphql_api: "GraphqlApi" = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class CreateResolverRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "api_id",
                "apiId",
                TypeInfo(str),
            ),
            (
                "type_name",
                "typeName",
                TypeInfo(str),
            ),
            (
                "field_name",
                "fieldName",
                TypeInfo(str),
            ),
            (
                "data_source_name",
                "dataSourceName",
                TypeInfo(str),
            ),
            (
                "request_mapping_template",
                "requestMappingTemplate",
                TypeInfo(str),
            ),
            (
                "response_mapping_template",
                "responseMappingTemplate",
                TypeInfo(str),
            ),
        ]

    # The ID for the GraphQL API for which the resolver is being created.
    api_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The name of the `Type`.
    type_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The name of the field to attach the resolver to.
    field_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The name of the data source for which the resolver is being created.
    data_source_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The mapping template to be used for requests.

    # A resolver uses a request mapping template to convert a GraphQL expression
    # into a format that a data source can understand. Mapping templates are
    # written in Apache Velocity Template Language (VTL).
    request_mapping_template: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The mapping template to be used for responses from the data source.
    response_mapping_template: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class CreateResolverResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "resolver",
                "resolver",
                TypeInfo(Resolver),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The `Resolver` object.
    resolver: "Resolver" = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class CreateTypeRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "api_id",
                "apiId",
                TypeInfo(str),
            ),
            (
                "definition",
                "definition",
                TypeInfo(str),
            ),
            (
                "format",
                "format",
                TypeInfo(typing.Union[str, TypeDefinitionFormat]),
            ),
        ]

    # The API ID.
    api_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The type definition, in GraphQL Schema Definition Language (SDL) format.

    # For more information, see the [GraphQL SDL
    # documentation](http://graphql.org/learn/schema/).
    definition: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The type format: SDL or JSON.
    format: typing.Union[str, "TypeDefinitionFormat"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class CreateTypeResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "type",
                "type",
                TypeInfo(Type),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The `Type` object.
    type: "Type" = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DataSource(ShapeBase):
    """
    Describes a data source.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "data_source_arn",
                "dataSourceArn",
                TypeInfo(str),
            ),
            (
                "name",
                "name",
                TypeInfo(str),
            ),
            (
                "description",
                "description",
                TypeInfo(str),
            ),
            (
                "type",
                "type",
                TypeInfo(typing.Union[str, DataSourceType]),
            ),
            (
                "service_role_arn",
                "serviceRoleArn",
                TypeInfo(str),
            ),
            (
                "dynamodb_config",
                "dynamodbConfig",
                TypeInfo(DynamodbDataSourceConfig),
            ),
            (
                "lambda_config",
                "lambdaConfig",
                TypeInfo(LambdaDataSourceConfig),
            ),
            (
                "elasticsearch_config",
                "elasticsearchConfig",
                TypeInfo(ElasticsearchDataSourceConfig),
            ),
            (
                "http_config",
                "httpConfig",
                TypeInfo(HttpDataSourceConfig),
            ),
        ]

    # The data source ARN.
    data_source_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The name of the data source.
    name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The description of the data source.
    description: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The type of the data source.

    #   * **AMAZON_DYNAMODB** : The data source is an Amazon DynamoDB table.

    #   * **AMAZON_ELASTICSEARCH** : The data source is an Amazon Elasticsearch Service domain.

    #   * **AWS_LAMBDA** : The data source is an AWS Lambda function.

    #   * **NONE** : There is no data source. This type is used when when you wish to invoke a GraphQL operation without connecting to a data source, such as performing data transformation with resolvers or triggering a subscription to be invoked from a mutation.

    #   * **HTTP** : The data source is an HTTP endpoint.
    type: typing.Union[str, "DataSourceType"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The IAM service role ARN for the data source. The system assumes this role
    # when accessing the data source.
    service_role_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # DynamoDB settings.
    dynamodb_config: "DynamodbDataSourceConfig" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Lambda settings.
    lambda_config: "LambdaDataSourceConfig" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Amazon Elasticsearch settings.
    elasticsearch_config: "ElasticsearchDataSourceConfig" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Http endpoint settings.
    http_config: "HttpDataSourceConfig" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


class DataSourceType(str):
    AWS_LAMBDA = "AWS_LAMBDA"
    AMAZON_DYNAMODB = "AMAZON_DYNAMODB"
    AMAZON_ELASTICSEARCH = "AMAZON_ELASTICSEARCH"
    NONE = "NONE"
    HTTP = "HTTP"


class DefaultAction(str):
    ALLOW = "ALLOW"
    DENY = "DENY"


@dataclasses.dataclass
class DeleteApiKeyRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "api_id",
                "apiId",
                TypeInfo(str),
            ),
            (
                "id",
                "id",
                TypeInfo(str),
            ),
        ]

    # The API ID.
    api_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The ID for the API key.
    id: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DeleteApiKeyResponse(OutputShapeBase):
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
class DeleteDataSourceRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "api_id",
                "apiId",
                TypeInfo(str),
            ),
            (
                "name",
                "name",
                TypeInfo(str),
            ),
        ]

    # The API ID.
    api_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The name of the data source.
    name: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DeleteDataSourceResponse(OutputShapeBase):
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
class DeleteGraphqlApiRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "api_id",
                "apiId",
                TypeInfo(str),
            ),
        ]

    # The API ID.
    api_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DeleteGraphqlApiResponse(OutputShapeBase):
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
class DeleteResolverRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "api_id",
                "apiId",
                TypeInfo(str),
            ),
            (
                "type_name",
                "typeName",
                TypeInfo(str),
            ),
            (
                "field_name",
                "fieldName",
                TypeInfo(str),
            ),
        ]

    # The API ID.
    api_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The name of the resolver type.
    type_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The resolver field name.
    field_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DeleteResolverResponse(OutputShapeBase):
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
class DeleteTypeRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "api_id",
                "apiId",
                TypeInfo(str),
            ),
            (
                "type_name",
                "typeName",
                TypeInfo(str),
            ),
        ]

    # The API ID.
    api_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The type name.
    type_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DeleteTypeResponse(OutputShapeBase):
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
class DynamodbDataSourceConfig(ShapeBase):
    """
    Describes a DynamoDB data source configuration.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "table_name",
                "tableName",
                TypeInfo(str),
            ),
            (
                "aws_region",
                "awsRegion",
                TypeInfo(str),
            ),
            (
                "use_caller_credentials",
                "useCallerCredentials",
                TypeInfo(bool),
            ),
        ]

    # The table name.
    table_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The AWS region.
    aws_region: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Set to TRUE to use Amazon Cognito credentials with this data source.
    use_caller_credentials: bool = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class ElasticsearchDataSourceConfig(ShapeBase):
    """
    Describes an Elasticsearch data source configuration.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "endpoint",
                "endpoint",
                TypeInfo(str),
            ),
            (
                "aws_region",
                "awsRegion",
                TypeInfo(str),
            ),
        ]

    # The endpoint.
    endpoint: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The AWS region.
    aws_region: str = dataclasses.field(default=ShapeBase.NOT_SET, )


class FieldLogLevel(str):
    NONE = "NONE"
    ERROR = "ERROR"
    ALL = "ALL"


@dataclasses.dataclass
class GetDataSourceRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "api_id",
                "apiId",
                TypeInfo(str),
            ),
            (
                "name",
                "name",
                TypeInfo(str),
            ),
        ]

    # The API ID.
    api_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The name of the data source.
    name: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class GetDataSourceResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "data_source",
                "dataSource",
                TypeInfo(DataSource),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The `DataSource` object.
    data_source: "DataSource" = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class GetGraphqlApiRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "api_id",
                "apiId",
                TypeInfo(str),
            ),
        ]

    # The API ID for the GraphQL API.
    api_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class GetGraphqlApiResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "graphql_api",
                "graphqlApi",
                TypeInfo(GraphqlApi),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The `GraphqlApi` object.
    graphql_api: "GraphqlApi" = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class GetIntrospectionSchemaRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "api_id",
                "apiId",
                TypeInfo(str),
            ),
            (
                "format",
                "format",
                TypeInfo(typing.Union[str, OutputType]),
            ),
        ]

    # The API ID.
    api_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The schema format: SDL or JSON.
    format: typing.Union[str, "OutputType"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class GetIntrospectionSchemaResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "schema",
                "schema",
                TypeInfo(typing.Any),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The schema, in GraphQL Schema Definition Language (SDL) format.

    # For more information, see the [GraphQL SDL
    # documentation](http://graphql.org/learn/schema/).
    schema: typing.Any = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class GetResolverRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "api_id",
                "apiId",
                TypeInfo(str),
            ),
            (
                "type_name",
                "typeName",
                TypeInfo(str),
            ),
            (
                "field_name",
                "fieldName",
                TypeInfo(str),
            ),
        ]

    # The API ID.
    api_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The resolver type name.
    type_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The resolver field name.
    field_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class GetResolverResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "resolver",
                "resolver",
                TypeInfo(Resolver),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The `Resolver` object.
    resolver: "Resolver" = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class GetSchemaCreationStatusRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "api_id",
                "apiId",
                TypeInfo(str),
            ),
        ]

    # The API ID.
    api_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class GetSchemaCreationStatusResponse(OutputShapeBase):
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
                "status",
                TypeInfo(typing.Union[str, SchemaStatus]),
            ),
            (
                "details",
                "details",
                TypeInfo(str),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The current state of the schema (PROCESSING, ACTIVE, or DELETING). Once the
    # schema is in the ACTIVE state, you can add data.
    status: typing.Union[str, "SchemaStatus"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Detailed information about the status of the schema creation operation.
    details: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class GetTypeRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "api_id",
                "apiId",
                TypeInfo(str),
            ),
            (
                "type_name",
                "typeName",
                TypeInfo(str),
            ),
            (
                "format",
                "format",
                TypeInfo(typing.Union[str, TypeDefinitionFormat]),
            ),
        ]

    # The API ID.
    api_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The type name.
    type_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The type format: SDL or JSON.
    format: typing.Union[str, "TypeDefinitionFormat"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class GetTypeResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "type",
                "type",
                TypeInfo(Type),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The `Type` object.
    type: "Type" = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class GraphQLSchemaException(ShapeBase):
    """
    The GraphQL schema is not valid.
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
class GraphqlApi(ShapeBase):
    """
    Describes a GraphQL API.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "name",
                "name",
                TypeInfo(str),
            ),
            (
                "api_id",
                "apiId",
                TypeInfo(str),
            ),
            (
                "authentication_type",
                "authenticationType",
                TypeInfo(typing.Union[str, AuthenticationType]),
            ),
            (
                "log_config",
                "logConfig",
                TypeInfo(LogConfig),
            ),
            (
                "user_pool_config",
                "userPoolConfig",
                TypeInfo(UserPoolConfig),
            ),
            (
                "open_id_connect_config",
                "openIDConnectConfig",
                TypeInfo(OpenIDConnectConfig),
            ),
            (
                "arn",
                "arn",
                TypeInfo(str),
            ),
            (
                "uris",
                "uris",
                TypeInfo(typing.Dict[str, str]),
            ),
        ]

    # The API name.
    name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The API ID.
    api_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The authentication type.
    authentication_type: typing.Union[str, "AuthenticationType"
                                     ] = dataclasses.field(
                                         default=ShapeBase.NOT_SET,
                                     )

    # The Amazon CloudWatch Logs configuration.
    log_config: "LogConfig" = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The Amazon Cognito User Pool configuration.
    user_pool_config: "UserPoolConfig" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The Open Id Connect configuration.
    open_id_connect_config: "OpenIDConnectConfig" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The ARN.
    arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The URIs.
    uris: typing.Dict[str, str] = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class HttpDataSourceConfig(ShapeBase):
    """
    Describes a Http data source configuration.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "endpoint",
                "endpoint",
                TypeInfo(str),
            ),
        ]

    # The Http url endpoint. You can either specify the domain name or ip and
    # port combination and the url scheme must be http(s). If the port is not
    # specified, AWS AppSync will use the default port 80 for http endpoint and
    # port 443 for https endpoints.
    endpoint: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class InternalFailureException(ShapeBase):
    """
    An internal AWS AppSync error occurred. Try your request again.
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
class LambdaDataSourceConfig(ShapeBase):
    """
    Describes a Lambda data source configuration.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "lambda_function_arn",
                "lambdaFunctionArn",
                TypeInfo(str),
            ),
        ]

    # The ARN for the Lambda function.
    lambda_function_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class LimitExceededException(ShapeBase):
    """
    The request exceeded a limit. Try your request again.
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
class ListApiKeysRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "api_id",
                "apiId",
                TypeInfo(str),
            ),
            (
                "next_token",
                "nextToken",
                TypeInfo(str),
            ),
            (
                "max_results",
                "maxResults",
                TypeInfo(int),
            ),
        ]

    # The API ID.
    api_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # An identifier that was returned from the previous call to this operation,
    # which can be used to return the next set of items in the list.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The maximum number of results you want the request to return.
    max_results: int = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ListApiKeysResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "api_keys",
                "apiKeys",
                TypeInfo(typing.List[ApiKey]),
            ),
            (
                "next_token",
                "nextToken",
                TypeInfo(str),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The `ApiKey` objects.
    api_keys: typing.List["ApiKey"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # An identifier to be passed in the next request to this operation to return
    # the next set of items in the list.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ListDataSourcesRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "api_id",
                "apiId",
                TypeInfo(str),
            ),
            (
                "next_token",
                "nextToken",
                TypeInfo(str),
            ),
            (
                "max_results",
                "maxResults",
                TypeInfo(int),
            ),
        ]

    # The API ID.
    api_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # An identifier that was returned from the previous call to this operation,
    # which can be used to return the next set of items in the list.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The maximum number of results you want the request to return.
    max_results: int = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ListDataSourcesResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "data_sources",
                "dataSources",
                TypeInfo(typing.List[DataSource]),
            ),
            (
                "next_token",
                "nextToken",
                TypeInfo(str),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The `DataSource` objects.
    data_sources: typing.List["DataSource"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # An identifier to be passed in the next request to this operation to return
    # the next set of items in the list.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ListGraphqlApisRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "next_token",
                "nextToken",
                TypeInfo(str),
            ),
            (
                "max_results",
                "maxResults",
                TypeInfo(int),
            ),
        ]

    # An identifier that was returned from the previous call to this operation,
    # which can be used to return the next set of items in the list.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The maximum number of results you want the request to return.
    max_results: int = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ListGraphqlApisResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "graphql_apis",
                "graphqlApis",
                TypeInfo(typing.List[GraphqlApi]),
            ),
            (
                "next_token",
                "nextToken",
                TypeInfo(str),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The `GraphqlApi` objects.
    graphql_apis: typing.List["GraphqlApi"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # An identifier to be passed in the next request to this operation to return
    # the next set of items in the list.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ListResolversRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "api_id",
                "apiId",
                TypeInfo(str),
            ),
            (
                "type_name",
                "typeName",
                TypeInfo(str),
            ),
            (
                "next_token",
                "nextToken",
                TypeInfo(str),
            ),
            (
                "max_results",
                "maxResults",
                TypeInfo(int),
            ),
        ]

    # The API ID.
    api_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The type name.
    type_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # An identifier that was returned from the previous call to this operation,
    # which can be used to return the next set of items in the list.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The maximum number of results you want the request to return.
    max_results: int = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ListResolversResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "resolvers",
                "resolvers",
                TypeInfo(typing.List[Resolver]),
            ),
            (
                "next_token",
                "nextToken",
                TypeInfo(str),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The `Resolver` objects.
    resolvers: typing.List["Resolver"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # An identifier to be passed in the next request to this operation to return
    # the next set of items in the list.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ListTypesRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "api_id",
                "apiId",
                TypeInfo(str),
            ),
            (
                "format",
                "format",
                TypeInfo(typing.Union[str, TypeDefinitionFormat]),
            ),
            (
                "next_token",
                "nextToken",
                TypeInfo(str),
            ),
            (
                "max_results",
                "maxResults",
                TypeInfo(int),
            ),
        ]

    # The API ID.
    api_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The type format: SDL or JSON.
    format: typing.Union[str, "TypeDefinitionFormat"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # An identifier that was returned from the previous call to this operation,
    # which can be used to return the next set of items in the list.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The maximum number of results you want the request to return.
    max_results: int = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ListTypesResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "types",
                "types",
                TypeInfo(typing.List[Type]),
            ),
            (
                "next_token",
                "nextToken",
                TypeInfo(str),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The `Type` objects.
    types: typing.List["Type"] = dataclasses.field(default=ShapeBase.NOT_SET, )

    # An identifier to be passed in the next request to this operation to return
    # the next set of items in the list.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class LogConfig(ShapeBase):
    """
    The CloudWatch Logs configuration.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "field_log_level",
                "fieldLogLevel",
                TypeInfo(typing.Union[str, FieldLogLevel]),
            ),
            (
                "cloud_watch_logs_role_arn",
                "cloudWatchLogsRoleArn",
                TypeInfo(str),
            ),
        ]

    # The field logging level. Values can be NONE, ERROR, ALL.

    #   * **NONE** : No field-level logs are captured.

    #   * **ERROR** : Logs the following information only for the fields that are in error:

    #     * The error section in the server response.

    #     * Field-level errors.

    #     * The generated request/response functions that got resolved for error fields.

    #   * **ALL** : The following information is logged for all fields in the query:

    #     * Field-level tracing information.

    #     * The generated request/response functions that got resolved for each field.
    field_log_level: typing.Union[str, "FieldLogLevel"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The service role that AWS AppSync will assume to publish to Amazon
    # CloudWatch logs in your account.
    cloud_watch_logs_role_arn: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class NotFoundException(ShapeBase):
    """
    The resource specified in the request was not found. Check the resource and try
    again.
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
class OpenIDConnectConfig(ShapeBase):
    """
    Describes an Open Id Connect configuration.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "issuer",
                "issuer",
                TypeInfo(str),
            ),
            (
                "client_id",
                "clientId",
                TypeInfo(str),
            ),
            (
                "iat_ttl",
                "iatTTL",
                TypeInfo(int),
            ),
            (
                "auth_ttl",
                "authTTL",
                TypeInfo(int),
            ),
        ]

    # The issuer for the open id connect configuration. The issuer returned by
    # discovery MUST exactly match the value of iss in the ID Token.
    issuer: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The client identifier of the Relying party at the OpenID Provider. This
    # identifier is typically obtained when the Relying party is registered with
    # the OpenID Provider. You can specify a regular expression so the AWS
    # AppSync can validate against multiple client identifiers at a time
    client_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The number of milliseconds a token is valid after being issued to a user.
    iat_ttl: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The number of milliseconds a token is valid after being authenticated.
    auth_ttl: int = dataclasses.field(default=ShapeBase.NOT_SET, )


class OutputType(str):
    SDL = "SDL"
    JSON = "JSON"


@dataclasses.dataclass
class Resolver(ShapeBase):
    """
    Describes a resolver.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "type_name",
                "typeName",
                TypeInfo(str),
            ),
            (
                "field_name",
                "fieldName",
                TypeInfo(str),
            ),
            (
                "data_source_name",
                "dataSourceName",
                TypeInfo(str),
            ),
            (
                "resolver_arn",
                "resolverArn",
                TypeInfo(str),
            ),
            (
                "request_mapping_template",
                "requestMappingTemplate",
                TypeInfo(str),
            ),
            (
                "response_mapping_template",
                "responseMappingTemplate",
                TypeInfo(str),
            ),
        ]

    # The resolver type name.
    type_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The resolver field name.
    field_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The resolver data source name.
    data_source_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The resolver ARN.
    resolver_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The request mapping template.
    request_mapping_template: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The response mapping template.
    response_mapping_template: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


class SchemaStatus(str):
    PROCESSING = "PROCESSING"
    ACTIVE = "ACTIVE"
    DELETING = "DELETING"


@dataclasses.dataclass
class StartSchemaCreationRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "api_id",
                "apiId",
                TypeInfo(str),
            ),
            (
                "definition",
                "definition",
                TypeInfo(typing.Any),
            ),
        ]

    # The API ID.
    api_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The schema definition, in GraphQL schema language format.
    definition: typing.Any = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class StartSchemaCreationResponse(OutputShapeBase):
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
                "status",
                TypeInfo(typing.Union[str, SchemaStatus]),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The current state of the schema (PROCESSING, ACTIVE, or DELETING). Once the
    # schema is in the ACTIVE state, you can add data.
    status: typing.Union[str, "SchemaStatus"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class Type(ShapeBase):
    """
    Describes a type.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "name",
                "name",
                TypeInfo(str),
            ),
            (
                "description",
                "description",
                TypeInfo(str),
            ),
            (
                "arn",
                "arn",
                TypeInfo(str),
            ),
            (
                "definition",
                "definition",
                TypeInfo(str),
            ),
            (
                "format",
                "format",
                TypeInfo(typing.Union[str, TypeDefinitionFormat]),
            ),
        ]

    # The type name.
    name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The type description.
    description: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The type ARN.
    arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The type definition.
    definition: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The type format: SDL or JSON.
    format: typing.Union[str, "TypeDefinitionFormat"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


class TypeDefinitionFormat(str):
    SDL = "SDL"
    JSON = "JSON"


@dataclasses.dataclass
class UnauthorizedException(ShapeBase):
    """
    You are not authorized to perform this operation.
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
class UpdateApiKeyRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "api_id",
                "apiId",
                TypeInfo(str),
            ),
            (
                "id",
                "id",
                TypeInfo(str),
            ),
            (
                "description",
                "description",
                TypeInfo(str),
            ),
            (
                "expires",
                "expires",
                TypeInfo(int),
            ),
        ]

    # The ID for the GraphQL API
    api_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The API key ID.
    id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A description of the purpose of the API key.
    description: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The time from update time after which the API key expires. The date is
    # represented as seconds since the epoch. For more information, see .
    expires: int = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class UpdateApiKeyResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "api_key",
                "apiKey",
                TypeInfo(ApiKey),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The API key.
    api_key: "ApiKey" = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class UpdateDataSourceRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "api_id",
                "apiId",
                TypeInfo(str),
            ),
            (
                "name",
                "name",
                TypeInfo(str),
            ),
            (
                "type",
                "type",
                TypeInfo(typing.Union[str, DataSourceType]),
            ),
            (
                "description",
                "description",
                TypeInfo(str),
            ),
            (
                "service_role_arn",
                "serviceRoleArn",
                TypeInfo(str),
            ),
            (
                "dynamodb_config",
                "dynamodbConfig",
                TypeInfo(DynamodbDataSourceConfig),
            ),
            (
                "lambda_config",
                "lambdaConfig",
                TypeInfo(LambdaDataSourceConfig),
            ),
            (
                "elasticsearch_config",
                "elasticsearchConfig",
                TypeInfo(ElasticsearchDataSourceConfig),
            ),
            (
                "http_config",
                "httpConfig",
                TypeInfo(HttpDataSourceConfig),
            ),
        ]

    # The API ID.
    api_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The new name for the data source.
    name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The new data source type.
    type: typing.Union[str, "DataSourceType"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The new description for the data source.
    description: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The new service role ARN for the data source.
    service_role_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The new DynamoDB configuration.
    dynamodb_config: "DynamodbDataSourceConfig" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The new Lambda configuration.
    lambda_config: "LambdaDataSourceConfig" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The new Elasticsearch configuration.
    elasticsearch_config: "ElasticsearchDataSourceConfig" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The new http endpoint configuration
    http_config: "HttpDataSourceConfig" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class UpdateDataSourceResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "data_source",
                "dataSource",
                TypeInfo(DataSource),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The updated `DataSource` object.
    data_source: "DataSource" = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class UpdateGraphqlApiRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "api_id",
                "apiId",
                TypeInfo(str),
            ),
            (
                "name",
                "name",
                TypeInfo(str),
            ),
            (
                "log_config",
                "logConfig",
                TypeInfo(LogConfig),
            ),
            (
                "authentication_type",
                "authenticationType",
                TypeInfo(typing.Union[str, AuthenticationType]),
            ),
            (
                "user_pool_config",
                "userPoolConfig",
                TypeInfo(UserPoolConfig),
            ),
            (
                "open_id_connect_config",
                "openIDConnectConfig",
                TypeInfo(OpenIDConnectConfig),
            ),
        ]

    # The API ID.
    api_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The new name for the `GraphqlApi` object.
    name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The Amazon CloudWatch logs configuration for the `GraphqlApi` object.
    log_config: "LogConfig" = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The new authentication type for the `GraphqlApi` object.
    authentication_type: typing.Union[str, "AuthenticationType"
                                     ] = dataclasses.field(
                                         default=ShapeBase.NOT_SET,
                                     )

    # The new Amazon Cognito User Pool configuration for the `GraphqlApi` object.
    user_pool_config: "UserPoolConfig" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The Open Id Connect configuration configuration for the `GraphqlApi`
    # object.
    open_id_connect_config: "OpenIDConnectConfig" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class UpdateGraphqlApiResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "graphql_api",
                "graphqlApi",
                TypeInfo(GraphqlApi),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The updated `GraphqlApi` object.
    graphql_api: "GraphqlApi" = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class UpdateResolverRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "api_id",
                "apiId",
                TypeInfo(str),
            ),
            (
                "type_name",
                "typeName",
                TypeInfo(str),
            ),
            (
                "field_name",
                "fieldName",
                TypeInfo(str),
            ),
            (
                "data_source_name",
                "dataSourceName",
                TypeInfo(str),
            ),
            (
                "request_mapping_template",
                "requestMappingTemplate",
                TypeInfo(str),
            ),
            (
                "response_mapping_template",
                "responseMappingTemplate",
                TypeInfo(str),
            ),
        ]

    # The API ID.
    api_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The new type name.
    type_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The new field name.
    field_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The new data source name.
    data_source_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The new request mapping template.
    request_mapping_template: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The new response mapping template.
    response_mapping_template: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class UpdateResolverResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "resolver",
                "resolver",
                TypeInfo(Resolver),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The updated `Resolver` object.
    resolver: "Resolver" = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class UpdateTypeRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "api_id",
                "apiId",
                TypeInfo(str),
            ),
            (
                "type_name",
                "typeName",
                TypeInfo(str),
            ),
            (
                "format",
                "format",
                TypeInfo(typing.Union[str, TypeDefinitionFormat]),
            ),
            (
                "definition",
                "definition",
                TypeInfo(str),
            ),
        ]

    # The API ID.
    api_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The new type name.
    type_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The new type format: SDL or JSON.
    format: typing.Union[str, "TypeDefinitionFormat"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The new definition.
    definition: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class UpdateTypeResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "type",
                "type",
                TypeInfo(Type),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The updated `Type` object.
    type: "Type" = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class UserPoolConfig(ShapeBase):
    """
    Describes an Amazon Cognito User Pool configuration.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "user_pool_id",
                "userPoolId",
                TypeInfo(str),
            ),
            (
                "aws_region",
                "awsRegion",
                TypeInfo(str),
            ),
            (
                "default_action",
                "defaultAction",
                TypeInfo(typing.Union[str, DefaultAction]),
            ),
            (
                "app_id_client_regex",
                "appIdClientRegex",
                TypeInfo(str),
            ),
        ]

    # The user pool ID.
    user_pool_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The AWS region in which the user pool was created.
    aws_region: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The action that you want your GraphQL API to take when a request that uses
    # Amazon Cognito User Pool authentication doesn't match the Amazon Cognito
    # User Pool configuration.
    default_action: typing.Union[str, "DefaultAction"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A regular expression for validating the incoming Amazon Cognito User Pool
    # app client ID.
    app_id_client_regex: str = dataclasses.field(default=ShapeBase.NOT_SET, )
