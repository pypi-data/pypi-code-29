import datetime
import typing
from autoboto import ShapeBase, OutputShapeBase, TypeInfo
import botocore.response
import dataclasses


@dataclasses.dataclass
class AccessLogSettings(ShapeBase):
    """
    Access log settings, including the access log format and access log destination
    ARN.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "format",
                "format",
                TypeInfo(str),
            ),
            (
                "destination_arn",
                "destinationArn",
                TypeInfo(str),
            ),
        ]

    # A single line format of the access logs of data, as specified by selected
    # [$context
    # variables](http://docs.aws.amazon.com/apigateway/latest/developerguide/api-
    # gateway-mapping-template-reference.html#context-variable-reference). The
    # format must include at least `$context.requestId`.
    format: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The ARN of the CloudWatch Logs log group to receive access logs.
    destination_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class Account(OutputShapeBase):
    """
    Represents an AWS account that is associated with API Gateway.

    To view the account info, call `GET` on this resource.

    #### Error Codes

    The following exception may be thrown when the request fails.

      * UnauthorizedException
      * NotFoundException
      * TooManyRequestsException

    For detailed error code information, including the corresponding HTTP Status
    Codes, see [API Gateway Error Codes](http://docs.aws.amazon.com/apigateway/api-
    reference/handling-errors/#api-error-codes)

    #### Example: Get the information about an account.

    ##### Request



        GET /account HTTP/1.1 Content-Type: application/json Host: apigateway.us-east-1.amazonaws.com X-Amz-Date: 20160531T184618Z Authorization: AWS4-HMAC-SHA256 Credential={access_key_ID}/us-east-1/apigateway/aws4_request, SignedHeaders=content-type;host;x-amz-date, Signature={sig4_hash} 

    ##### Response

    The successful response returns a `200 OK` status code and a payload similar to
    the following:



        { "_links": { "curies": { "href": "http://docs.aws.amazon.com/apigateway/latest/developerguide/account-apigateway-{rel}.html", "name": "account", "templated": true }, "self": { "href": "/account" }, "account:update": { "href": "/account" } }, "cloudwatchRoleArn": "arn:aws:iam::123456789012:role/apigAwsProxyRole", "throttleSettings": { "rateLimit": 500, "burstLimit": 1000 } } 

    In addition to making the REST API call directly, you can use the AWS CLI and an
    AWS SDK to access this resource.

    [API Gateway
    Limits](http://docs.aws.amazon.com/apigateway/latest/developerguide/api-gateway-
    limits.html) [Developer
    Guide](http://docs.aws.amazon.com/apigateway/latest/developerguide/welcome.html),
    [AWS CLI](http://docs.aws.amazon.com/cli/latest/reference/apigateway/get-
    account.html)
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
                "cloudwatch_role_arn",
                "cloudwatchRoleArn",
                TypeInfo(str),
            ),
            (
                "throttle_settings",
                "throttleSettings",
                TypeInfo(ThrottleSettings),
            ),
            (
                "features",
                "features",
                TypeInfo(typing.List[str]),
            ),
            (
                "api_key_version",
                "apiKeyVersion",
                TypeInfo(str),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The ARN of an Amazon CloudWatch role for the current Account.
    cloudwatch_role_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Specifies the API request limits configured for the current Account.
    throttle_settings: "ThrottleSettings" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A list of features supported for the account. When usage plans are enabled,
    # the features list will include an entry of `"UsagePlans"`.
    features: typing.List[str] = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The version of the API keys used for the account.
    api_key_version: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ApiKey(OutputShapeBase):
    """
    A resource that can be distributed to callers for executing Method resources
    that require an API key. API keys can be mapped to any Stage on any RestApi,
    which indicates that the callers with the API key can make requests to that
    stage.

    [Use API Keys](http://docs.aws.amazon.com/apigateway/latest/developerguide/how-
    to-api-keys.html)
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
                "id",
                "id",
                TypeInfo(str),
            ),
            (
                "value",
                "value",
                TypeInfo(str),
            ),
            (
                "name",
                "name",
                TypeInfo(str),
            ),
            (
                "customer_id",
                "customerId",
                TypeInfo(str),
            ),
            (
                "description",
                "description",
                TypeInfo(str),
            ),
            (
                "enabled",
                "enabled",
                TypeInfo(bool),
            ),
            (
                "created_date",
                "createdDate",
                TypeInfo(datetime.datetime),
            ),
            (
                "last_updated_date",
                "lastUpdatedDate",
                TypeInfo(datetime.datetime),
            ),
            (
                "stage_keys",
                "stageKeys",
                TypeInfo(typing.List[str]),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The identifier of the API Key.
    id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The value of the API Key.
    value: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The name of the API Key.
    name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # An AWS Marketplace customer identifier , when integrating with the AWS SaaS
    # Marketplace.
    customer_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The description of the API Key.
    description: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Specifies whether the API Key can be used by callers.
    enabled: bool = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The timestamp when the API Key was created.
    created_date: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The timestamp when the API Key was last updated.
    last_updated_date: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A list of Stage resources that are associated with the ApiKey resource.
    stage_keys: typing.List[str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class ApiKeyIds(OutputShapeBase):
    """
    The identifier of an ApiKey used in a UsagePlan.
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
                "ids",
                "ids",
                TypeInfo(typing.List[str]),
            ),
            (
                "warnings",
                "warnings",
                TypeInfo(typing.List[str]),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A list of all the ApiKey identifiers.
    ids: typing.List[str] = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A list of warning messages.
    warnings: typing.List[str] = dataclasses.field(default=ShapeBase.NOT_SET, )


class ApiKeySourceType(str):
    HEADER = "HEADER"
    AUTHORIZER = "AUTHORIZER"


@dataclasses.dataclass
class ApiKeys(OutputShapeBase):
    """
    Represents a collection of API keys as represented by an ApiKeys resource.

    [Use API Keys](http://docs.aws.amazon.com/apigateway/latest/developerguide/how-
    to-api-keys.html)
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
                "warnings",
                "warnings",
                TypeInfo(typing.List[str]),
            ),
            (
                "position",
                "position",
                TypeInfo(str),
            ),
            (
                "items",
                "items",
                TypeInfo(typing.List[ApiKey]),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A list of warning messages logged during the import of API keys when the
    # `failOnWarnings` option is set to true.
    warnings: typing.List[str] = dataclasses.field(default=ShapeBase.NOT_SET, )
    position: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The current page of elements from this collection.
    items: typing.List["ApiKey"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    def paginate(self, ) -> typing.Generator["ApiKeys", None, None]:
        yield from super()._paginate()


class ApiKeysFormat(str):
    csv = "csv"


@dataclasses.dataclass
class ApiStage(ShapeBase):
    """
    API stage name of the associated API stage in a usage plan.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "api_id",
                "apiId",
                TypeInfo(str),
            ),
            (
                "stage",
                "stage",
                TypeInfo(str),
            ),
            (
                "throttle",
                "throttle",
                TypeInfo(typing.Dict[str, ThrottleSettings]),
            ),
        ]

    # API Id of the associated API stage in a usage plan.
    api_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # API stage name of the associated API stage in a usage plan.
    stage: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Map containing method level throttling information for API stage in a usage
    # plan.
    throttle: typing.Dict[str, "ThrottleSettings"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class Authorizer(OutputShapeBase):
    """
    Represents an authorization layer for methods. If enabled on a method, API
    Gateway will activate the authorizer when a client calls the method.

    [Enable custom
    authorization](http://docs.aws.amazon.com/apigateway/latest/developerguide/use-
    custom-authorizer.html)
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
                "id",
                "id",
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
                TypeInfo(typing.Union[str, AuthorizerType]),
            ),
            (
                "provider_arns",
                "providerARNs",
                TypeInfo(typing.List[str]),
            ),
            (
                "auth_type",
                "authType",
                TypeInfo(str),
            ),
            (
                "authorizer_uri",
                "authorizerUri",
                TypeInfo(str),
            ),
            (
                "authorizer_credentials",
                "authorizerCredentials",
                TypeInfo(str),
            ),
            (
                "identity_source",
                "identitySource",
                TypeInfo(str),
            ),
            (
                "identity_validation_expression",
                "identityValidationExpression",
                TypeInfo(str),
            ),
            (
                "authorizer_result_ttl_in_seconds",
                "authorizerResultTtlInSeconds",
                TypeInfo(int),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The identifier for the authorizer resource.
    id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # [Required] The name of the authorizer.
    name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The authorizer type. Valid values are `TOKEN` for a Lambda function using a
    # single authorization token submitted in a custom header, `REQUEST` for a
    # Lambda function using incoming request parameters, and `COGNITO_USER_POOLS`
    # for using an Amazon Cognito user pool.
    type: typing.Union[str, "AuthorizerType"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A list of the Amazon Cognito user pool ARNs for the `COGNITO_USER_POOLS`
    # authorizer. Each element is of this format: `arn:aws:cognito-
    # idp:{region}:{account_id}:userpool/{user_pool_id}`. For a `TOKEN` or
    # `REQUEST` authorizer, this is not defined.
    provider_arns: typing.List[str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Optional customer-defined field, used in Swagger imports and exports
    # without functional impact.
    auth_type: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Specifies the authorizer's Uniform Resource Identifier (URI). For `TOKEN`
    # or `REQUEST` authorizers, this must be a well-formed Lambda function URI,
    # for example, `arn:aws:apigateway:us-
    # west-2:lambda:path/2015-03-31/functions/arn:aws:lambda:us-
    # west-2:{account_id}:function:{lambda_function_name}/invocations`. In
    # general, the URI has this form
    # `arn:aws:apigateway:{region}:lambda:path/{service_api}`, where `{region}`
    # is the same as the region hosting the Lambda function, `path` indicates
    # that the remaining substring in the URI should be treated as the path to
    # the resource, including the initial `/`. For Lambda functions, this is
    # usually of the form `/2015-03-31/functions/[FunctionARN]/invocations`.
    authorizer_uri: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Specifies the required credentials as an IAM role for API Gateway to invoke
    # the authorizer. To specify an IAM role for API Gateway to assume, use the
    # role's Amazon Resource Name (ARN). To use resource-based permissions on the
    # Lambda function, specify null.
    authorizer_credentials: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The identity source for which authorization is requested.

    #   * For a `TOKEN` or `COGNITO_USER_POOLS` authorizer, this is required and specifies the request header mapping expression for the custom header holding the authorization token submitted by the client. For example, if the token header name is `Auth`, the header mapping expression is `method.request.header.Auth`.
    #   * For the `REQUEST` authorizer, this is required when authorization caching is enabled. The value is a comma-separated string of one or more mapping expressions of the specified request parameters. For example, if an `Auth` header, a `Name` query string parameter are defined as identity sources, this value is `method.request.header.Auth, method.request.querystring.Name`. These parameters will be used to derive the authorization caching key and to perform runtime validation of the `REQUEST` authorizer by verifying all of the identity-related request parameters are present, not null and non-empty. Only when this is true does the authorizer invoke the authorizer Lambda function, otherwise, it returns a 401 Unauthorized response without calling the Lambda function. The valid value is a string of comma-separated mapping expressions of the specified request parameters. When the authorization caching is not enabled, this property is optional.
    identity_source: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A validation expression for the incoming identity token. For `TOKEN`
    # authorizers, this value is a regular expression. API Gateway will match the
    # `aud` field of the incoming token from the client against the specified
    # regular expression. It will invoke the authorizer's Lambda function when
    # there is a match. Otherwise, it will return a 401 Unauthorized response
    # without calling the Lambda function. The validation expression does not
    # apply to the `REQUEST` authorizer.
    identity_validation_expression: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The TTL in seconds of cached authorizer results. If it equals 0,
    # authorization caching is disabled. If it is greater than 0, API Gateway
    # will cache authorizer responses. If this field is not set, the default
    # value is 300. The maximum value is 3600, or 1 hour.
    authorizer_result_ttl_in_seconds: int = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


class AuthorizerType(str):
    """
    The authorizer type. Valid values are `TOKEN` for a Lambda function using a
    single authorization token submitted in a custom header, `REQUEST` for a Lambda
    function using incoming request parameters, and `COGNITO_USER_POOLS` for using
    an Amazon Cognito user pool.
    """
    TOKEN = "TOKEN"
    REQUEST = "REQUEST"
    COGNITO_USER_POOLS = "COGNITO_USER_POOLS"


@dataclasses.dataclass
class Authorizers(OutputShapeBase):
    """
    Represents a collection of Authorizer resources.

    [Enable custom
    authorization](http://docs.aws.amazon.com/apigateway/latest/developerguide/use-
    custom-authorizer.html)
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
                "position",
                "position",
                TypeInfo(str),
            ),
            (
                "items",
                "items",
                TypeInfo(typing.List[Authorizer]),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )
    position: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The current page of elements from this collection.
    items: typing.List["Authorizer"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class BadRequestException(ShapeBase):
    """
    The submitted request is not valid, for example, the input is incomplete or
    incorrect. See the accompanying error message for details.
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
class BasePathMapping(OutputShapeBase):
    """
    Represents the base path that callers of the API must provide as part of the URL
    after the domain name.

    A custom domain name plus a `BasePathMapping` specification identifies a
    deployed RestApi in a given stage of the owner Account.

    [Use Custom Domain
    Names](http://docs.aws.amazon.com/apigateway/latest/developerguide/how-to-
    custom-domains.html)
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
                "base_path",
                "basePath",
                TypeInfo(str),
            ),
            (
                "rest_api_id",
                "restApiId",
                TypeInfo(str),
            ),
            (
                "stage",
                "stage",
                TypeInfo(str),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The base path name that callers of the API must provide as part of the URL
    # after the domain name.
    base_path: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The string identifier of the associated RestApi.
    rest_api_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The name of the associated stage.
    stage: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class BasePathMappings(OutputShapeBase):
    """
    Represents a collection of BasePathMapping resources.

    [Use Custom Domain
    Names](http://docs.aws.amazon.com/apigateway/latest/developerguide/how-to-
    custom-domains.html)
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
                "position",
                "position",
                TypeInfo(str),
            ),
            (
                "items",
                "items",
                TypeInfo(typing.List[BasePathMapping]),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )
    position: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The current page of elements from this collection.
    items: typing.List["BasePathMapping"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    def paginate(self, ) -> typing.Generator["BasePathMappings", None, None]:
        yield from super()._paginate()


class Blob(botocore.response.StreamingBody):
    pass


class CacheClusterSize(str):
    """
    Returns the size of the **CacheCluster**.
    """
    VALUE_OF_0_5 = "0.5"
    VALUE_OF_1_6 = "1.6"
    VALUE_OF_6_1 = "6.1"
    VALUE_OF_13_5 = "13.5"
    VALUE_OF_28_4 = "28.4"
    VALUE_OF_58_2 = "58.2"
    VALUE_OF_118 = "118"
    VALUE_OF_237 = "237"


class CacheClusterStatus(str):
    """
    Returns the status of the **CacheCluster**.
    """
    CREATE_IN_PROGRESS = "CREATE_IN_PROGRESS"
    AVAILABLE = "AVAILABLE"
    DELETE_IN_PROGRESS = "DELETE_IN_PROGRESS"
    NOT_AVAILABLE = "NOT_AVAILABLE"
    FLUSH_IN_PROGRESS = "FLUSH_IN_PROGRESS"


@dataclasses.dataclass
class CanarySettings(ShapeBase):
    """
    Configuration settings of a canary deployment.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "percent_traffic",
                "percentTraffic",
                TypeInfo(float),
            ),
            (
                "deployment_id",
                "deploymentId",
                TypeInfo(str),
            ),
            (
                "stage_variable_overrides",
                "stageVariableOverrides",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "use_stage_cache",
                "useStageCache",
                TypeInfo(bool),
            ),
        ]

    # The percent (0-100) of traffic diverted to a canary deployment.
    percent_traffic: float = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The ID of the canary deployment.
    deployment_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Stage variables overridden for a canary release deployment, including new
    # stage variables introduced in the canary. These stage variables are
    # represented as a string-to-string map between stage variable names and
    # their values.
    stage_variable_overrides: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A Boolean flag to indicate whether the canary deployment uses the stage
    # cache or not.
    use_stage_cache: bool = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ClientCertificate(OutputShapeBase):
    """
    Represents a client certificate used to configure client-side SSL authentication
    while sending requests to the integration endpoint.

    Client certificates are used to authenticate an API by the backend server. To
    authenticate an API client (or user), use IAM roles and policies, a custom
    Authorizer or an Amazon Cognito user pool.

    [Use Client-Side
    Certificate](http://docs.aws.amazon.com/apigateway/latest/developerguide/getting-
    started-client-side-ssl-authentication.html)
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
                "client_certificate_id",
                "clientCertificateId",
                TypeInfo(str),
            ),
            (
                "description",
                "description",
                TypeInfo(str),
            ),
            (
                "pem_encoded_certificate",
                "pemEncodedCertificate",
                TypeInfo(str),
            ),
            (
                "created_date",
                "createdDate",
                TypeInfo(datetime.datetime),
            ),
            (
                "expiration_date",
                "expirationDate",
                TypeInfo(datetime.datetime),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The identifier of the client certificate.
    client_certificate_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The description of the client certificate.
    description: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The PEM-encoded public key of the client certificate, which can be used to
    # configure certificate authentication in the integration endpoint .
    pem_encoded_certificate: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The timestamp when the client certificate was created.
    created_date: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The timestamp when the client certificate will expire.
    expiration_date: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class ClientCertificates(OutputShapeBase):
    """
    Represents a collection of ClientCertificate resources.

    [Use Client-Side
    Certificate](http://docs.aws.amazon.com/apigateway/latest/developerguide/getting-
    started-client-side-ssl-authentication.html)
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
                "position",
                "position",
                TypeInfo(str),
            ),
            (
                "items",
                "items",
                TypeInfo(typing.List[ClientCertificate]),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )
    position: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The current page of elements from this collection.
    items: typing.List["ClientCertificate"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    def paginate(self, ) -> typing.Generator["ClientCertificates", None, None]:
        yield from super()._paginate()


@dataclasses.dataclass
class ConflictException(ShapeBase):
    """
    The request configuration has conflicts. For details, see the accompanying error
    message.
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


class ConnectionType(str):
    INTERNET = "INTERNET"
    VPC_LINK = "VPC_LINK"


class ContentHandlingStrategy(str):
    CONVERT_TO_BINARY = "CONVERT_TO_BINARY"
    CONVERT_TO_TEXT = "CONVERT_TO_TEXT"


@dataclasses.dataclass
class CreateApiKeyRequest(ShapeBase):
    """
    Request to create an ApiKey resource.
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
                "enabled",
                "enabled",
                TypeInfo(bool),
            ),
            (
                "generate_distinct_id",
                "generateDistinctId",
                TypeInfo(bool),
            ),
            (
                "value",
                "value",
                TypeInfo(str),
            ),
            (
                "stage_keys",
                "stageKeys",
                TypeInfo(typing.List[StageKey]),
            ),
            (
                "customer_id",
                "customerId",
                TypeInfo(str),
            ),
        ]

    # The name of the ApiKey.
    name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The description of the ApiKey.
    description: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Specifies whether the ApiKey can be used by callers.
    enabled: bool = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Specifies whether (`true`) or not (`false`) the key identifier is distinct
    # from the created API key value.
    generate_distinct_id: bool = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Specifies a value of the API key.
    value: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # DEPRECATED FOR USAGE PLANS - Specifies stages associated with the API key.
    stage_keys: typing.List["StageKey"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # An AWS Marketplace customer identifier , when integrating with the AWS SaaS
    # Marketplace.
    customer_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class CreateAuthorizerRequest(ShapeBase):
    """
    Request to add a new Authorizer to an existing RestApi resource.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "rest_api_id",
                "restApiId",
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
                TypeInfo(typing.Union[str, AuthorizerType]),
            ),
            (
                "provider_arns",
                "providerARNs",
                TypeInfo(typing.List[str]),
            ),
            (
                "auth_type",
                "authType",
                TypeInfo(str),
            ),
            (
                "authorizer_uri",
                "authorizerUri",
                TypeInfo(str),
            ),
            (
                "authorizer_credentials",
                "authorizerCredentials",
                TypeInfo(str),
            ),
            (
                "identity_source",
                "identitySource",
                TypeInfo(str),
            ),
            (
                "identity_validation_expression",
                "identityValidationExpression",
                TypeInfo(str),
            ),
            (
                "authorizer_result_ttl_in_seconds",
                "authorizerResultTtlInSeconds",
                TypeInfo(int),
            ),
        ]

    # [Required] The string identifier of the associated RestApi.
    rest_api_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # [Required] The name of the authorizer.
    name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # [Required] The authorizer type. Valid values are `TOKEN` for a Lambda
    # function using a single authorization token submitted in a custom header,
    # `REQUEST` for a Lambda function using incoming request parameters, and
    # `COGNITO_USER_POOLS` for using an Amazon Cognito user pool.
    type: typing.Union[str, "AuthorizerType"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A list of the Amazon Cognito user pool ARNs for the `COGNITO_USER_POOLS`
    # authorizer. Each element is of this format: `arn:aws:cognito-
    # idp:{region}:{account_id}:userpool/{user_pool_id}`. For a `TOKEN` or
    # `REQUEST` authorizer, this is not defined.
    provider_arns: typing.List[str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Optional customer-defined field, used in Swagger imports and exports
    # without functional impact.
    auth_type: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Specifies the authorizer's Uniform Resource Identifier (URI). For `TOKEN`
    # or `REQUEST` authorizers, this must be a well-formed Lambda function URI,
    # for example, `arn:aws:apigateway:us-
    # west-2:lambda:path/2015-03-31/functions/arn:aws:lambda:us-
    # west-2:{account_id}:function:{lambda_function_name}/invocations`. In
    # general, the URI has this form
    # `arn:aws:apigateway:{region}:lambda:path/{service_api}`, where `{region}`
    # is the same as the region hosting the Lambda function, `path` indicates
    # that the remaining substring in the URI should be treated as the path to
    # the resource, including the initial `/`. For Lambda functions, this is
    # usually of the form `/2015-03-31/functions/[FunctionARN]/invocations`.
    authorizer_uri: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Specifies the required credentials as an IAM role for API Gateway to invoke
    # the authorizer. To specify an IAM role for API Gateway to assume, use the
    # role's Amazon Resource Name (ARN). To use resource-based permissions on the
    # Lambda function, specify null.
    authorizer_credentials: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The identity source for which authorization is requested.

    #   * For a `TOKEN` or `COGNITO_USER_POOLS` authorizer, this is required and specifies the request header mapping expression for the custom header holding the authorization token submitted by the client. For example, if the token header name is `Auth`, the header mapping expression is `method.request.header.Auth`.
    #   * For the `REQUEST` authorizer, this is required when authorization caching is enabled. The value is a comma-separated string of one or more mapping expressions of the specified request parameters. For example, if an `Auth` header, a `Name` query string parameter are defined as identity sources, this value is `method.request.header.Auth, method.request.querystring.Name`. These parameters will be used to derive the authorization caching key and to perform runtime validation of the `REQUEST` authorizer by verifying all of the identity-related request parameters are present, not null and non-empty. Only when this is true does the authorizer invoke the authorizer Lambda function, otherwise, it returns a 401 Unauthorized response without calling the Lambda function. The valid value is a string of comma-separated mapping expressions of the specified request parameters. When the authorization caching is not enabled, this property is optional.
    identity_source: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A validation expression for the incoming identity token. For `TOKEN`
    # authorizers, this value is a regular expression. API Gateway will match the
    # `aud` field of the incoming token from the client against the specified
    # regular expression. It will invoke the authorizer's Lambda function when
    # there is a match. Otherwise, it will return a 401 Unauthorized response
    # without calling the Lambda function. The validation expression does not
    # apply to the `REQUEST` authorizer.
    identity_validation_expression: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The TTL in seconds of cached authorizer results. If it equals 0,
    # authorization caching is disabled. If it is greater than 0, API Gateway
    # will cache authorizer responses. If this field is not set, the default
    # value is 300. The maximum value is 3600, or 1 hour.
    authorizer_result_ttl_in_seconds: int = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class CreateBasePathMappingRequest(ShapeBase):
    """
    Requests API Gateway to create a new BasePathMapping resource.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "domain_name",
                "domainName",
                TypeInfo(str),
            ),
            (
                "rest_api_id",
                "restApiId",
                TypeInfo(str),
            ),
            (
                "base_path",
                "basePath",
                TypeInfo(str),
            ),
            (
                "stage",
                "stage",
                TypeInfo(str),
            ),
        ]

    # [Required] The domain name of the BasePathMapping resource to create.
    domain_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # [Required] The string identifier of the associated RestApi.
    rest_api_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The base path name that callers of the API must provide as part of the URL
    # after the domain name. This value must be unique for all of the mappings
    # across a single API. Leave this blank if you do not want callers to specify
    # a base path name after the domain name.
    base_path: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The name of the API's stage that you want to use for this mapping. Leave
    # this blank if you do not want callers to explicitly specify the stage name
    # after any base path name.
    stage: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class CreateDeploymentRequest(ShapeBase):
    """
    Requests API Gateway to create a Deployment resource.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "rest_api_id",
                "restApiId",
                TypeInfo(str),
            ),
            (
                "stage_name",
                "stageName",
                TypeInfo(str),
            ),
            (
                "stage_description",
                "stageDescription",
                TypeInfo(str),
            ),
            (
                "description",
                "description",
                TypeInfo(str),
            ),
            (
                "cache_cluster_enabled",
                "cacheClusterEnabled",
                TypeInfo(bool),
            ),
            (
                "cache_cluster_size",
                "cacheClusterSize",
                TypeInfo(typing.Union[str, CacheClusterSize]),
            ),
            (
                "variables",
                "variables",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "canary_settings",
                "canarySettings",
                TypeInfo(DeploymentCanarySettings),
            ),
            (
                "tracing_enabled",
                "tracingEnabled",
                TypeInfo(bool),
            ),
        ]

    # [Required] The string identifier of the associated RestApi.
    rest_api_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The name of the Stage resource for the Deployment resource to create.
    stage_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The description of the Stage resource for the Deployment resource to
    # create.
    stage_description: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The description for the Deployment resource to create.
    description: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Enables a cache cluster for the Stage resource specified in the input.
    cache_cluster_enabled: bool = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Specifies the cache cluster size for the Stage resource specified in the
    # input, if a cache cluster is enabled.
    cache_cluster_size: typing.Union[str, "CacheClusterSize"
                                    ] = dataclasses.field(
                                        default=ShapeBase.NOT_SET,
                                    )

    # A map that defines the stage variables for the Stage resource that is
    # associated with the new deployment. Variable names can have alphanumeric
    # and underscore characters, and the values must match
    # `[A-Za-z0-9-._~:/?#&=,]+`.
    variables: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The input configuration for the canary deployment when the deployment is a
    # canary release deployment.
    canary_settings: "DeploymentCanarySettings" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Specifies whether active tracing with X-ray is enabled for the Stage.
    tracing_enabled: bool = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class CreateDocumentationPartRequest(ShapeBase):
    """
    Creates a new documentation part of a given API.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "rest_api_id",
                "restApiId",
                TypeInfo(str),
            ),
            (
                "location",
                "location",
                TypeInfo(DocumentationPartLocation),
            ),
            (
                "properties",
                "properties",
                TypeInfo(str),
            ),
        ]

    # [Required] The string identifier of the associated RestApi.
    rest_api_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # [Required] The location of the targeted API entity of the to-be-created
    # documentation part.
    location: "DocumentationPartLocation" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # [Required] The new documentation content map of the targeted API entity.
    # Enclosed key-value pairs are API-specific, but only Swagger-compliant key-
    # value pairs can be exported and, hence, published.
    properties: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class CreateDocumentationVersionRequest(ShapeBase):
    """
    Creates a new documentation version of a given API.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "rest_api_id",
                "restApiId",
                TypeInfo(str),
            ),
            (
                "documentation_version",
                "documentationVersion",
                TypeInfo(str),
            ),
            (
                "stage_name",
                "stageName",
                TypeInfo(str),
            ),
            (
                "description",
                "description",
                TypeInfo(str),
            ),
        ]

    # [Required] The string identifier of the associated RestApi.
    rest_api_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # [Required] The version identifier of the new snapshot.
    documentation_version: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The stage name to be associated with the new documentation snapshot.
    stage_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A description about the new documentation snapshot.
    description: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class CreateDomainNameRequest(ShapeBase):
    """
    A request to create a new domain name.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "domain_name",
                "domainName",
                TypeInfo(str),
            ),
            (
                "certificate_name",
                "certificateName",
                TypeInfo(str),
            ),
            (
                "certificate_body",
                "certificateBody",
                TypeInfo(str),
            ),
            (
                "certificate_private_key",
                "certificatePrivateKey",
                TypeInfo(str),
            ),
            (
                "certificate_chain",
                "certificateChain",
                TypeInfo(str),
            ),
            (
                "certificate_arn",
                "certificateArn",
                TypeInfo(str),
            ),
            (
                "regional_certificate_name",
                "regionalCertificateName",
                TypeInfo(str),
            ),
            (
                "regional_certificate_arn",
                "regionalCertificateArn",
                TypeInfo(str),
            ),
            (
                "endpoint_configuration",
                "endpointConfiguration",
                TypeInfo(EndpointConfiguration),
            ),
        ]

    # [Required] The name of the DomainName resource.
    domain_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The user-friendly name of the certificate that will be used by edge-
    # optimized endpoint for this domain name.
    certificate_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # [Deprecated] The body of the server certificate that will be used by edge-
    # optimized endpoint for this domain name provided by your certificate
    # authority.
    certificate_body: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # [Deprecated] Your edge-optimized endpoint's domain name certificate's
    # private key.
    certificate_private_key: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # [Deprecated] The intermediate certificates and optionally the root
    # certificate, one after the other without any blank lines, used by an edge-
    # optimized endpoint for this domain name. If you include the root
    # certificate, your certificate chain must start with intermediate
    # certificates and end with the root certificate. Use the intermediate
    # certificates that were provided by your certificate authority. Do not
    # include any intermediaries that are not in the chain of trust path.
    certificate_chain: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The reference to an AWS-managed certificate that will be used by edge-
    # optimized endpoint for this domain name. AWS Certificate Manager is the
    # only supported source.
    certificate_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The user-friendly name of the certificate that will be used by regional
    # endpoint for this domain name.
    regional_certificate_name: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The reference to an AWS-managed certificate that will be used by regional
    # endpoint for this domain name. AWS Certificate Manager is the only
    # supported source.
    regional_certificate_arn: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The endpoint configuration of this DomainName showing the endpoint types of
    # the domain name.
    endpoint_configuration: "EndpointConfiguration" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class CreateModelRequest(ShapeBase):
    """
    Request to add a new Model to an existing RestApi resource.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "rest_api_id",
                "restApiId",
                TypeInfo(str),
            ),
            (
                "name",
                "name",
                TypeInfo(str),
            ),
            (
                "content_type",
                "contentType",
                TypeInfo(str),
            ),
            (
                "description",
                "description",
                TypeInfo(str),
            ),
            (
                "schema",
                "schema",
                TypeInfo(str),
            ),
        ]

    # [Required] The RestApi identifier under which the Model will be created.
    rest_api_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # [Required] The name of the model. Must be alphanumeric.
    name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # [Required] The content-type for the model.
    content_type: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The description of the model.
    description: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The schema for the model. For `application/json` models, this should be
    # [JSON schema draft 4](https://tools.ietf.org/html/draft-zyp-json-schema-04)
    # model.
    schema: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class CreateRequestValidatorRequest(ShapeBase):
    """
    Creates a RequestValidator of a given RestApi.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "rest_api_id",
                "restApiId",
                TypeInfo(str),
            ),
            (
                "name",
                "name",
                TypeInfo(str),
            ),
            (
                "validate_request_body",
                "validateRequestBody",
                TypeInfo(bool),
            ),
            (
                "validate_request_parameters",
                "validateRequestParameters",
                TypeInfo(bool),
            ),
        ]

    # [Required] The string identifier of the associated RestApi.
    rest_api_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The name of the to-be-created RequestValidator.
    name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A Boolean flag to indicate whether to validate request body according to
    # the configured model schema for the method (`true`) or not (`false`).
    validate_request_body: bool = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A Boolean flag to indicate whether to validate request parameters, `true`,
    # or not `false`.
    validate_request_parameters: bool = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class CreateResourceRequest(ShapeBase):
    """
    Requests API Gateway to create a Resource resource.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "rest_api_id",
                "restApiId",
                TypeInfo(str),
            ),
            (
                "parent_id",
                "parentId",
                TypeInfo(str),
            ),
            (
                "path_part",
                "pathPart",
                TypeInfo(str),
            ),
        ]

    # [Required] The string identifier of the associated RestApi.
    rest_api_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # [Required] The parent resource's identifier.
    parent_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The last path segment for this resource.
    path_part: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class CreateRestApiRequest(ShapeBase):
    """
    The POST Request to add a new RestApi resource to your collection.
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
                "version",
                "version",
                TypeInfo(str),
            ),
            (
                "clone_from",
                "cloneFrom",
                TypeInfo(str),
            ),
            (
                "binary_media_types",
                "binaryMediaTypes",
                TypeInfo(typing.List[str]),
            ),
            (
                "minimum_compression_size",
                "minimumCompressionSize",
                TypeInfo(int),
            ),
            (
                "api_key_source",
                "apiKeySource",
                TypeInfo(typing.Union[str, ApiKeySourceType]),
            ),
            (
                "endpoint_configuration",
                "endpointConfiguration",
                TypeInfo(EndpointConfiguration),
            ),
            (
                "policy",
                "policy",
                TypeInfo(str),
            ),
        ]

    # [Required] The name of the RestApi.
    name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The description of the RestApi.
    description: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A version identifier for the API.
    version: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The ID of the RestApi that you want to clone from.
    clone_from: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The list of binary media types supported by the RestApi. By default, the
    # RestApi supports only UTF-8-encoded text payloads.
    binary_media_types: typing.List[str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A nullable integer that is used to enable compression (with non-negative
    # between 0 and 10485760 (10M) bytes, inclusive) or disable compression (with
    # a null value) on an API. When compression is enabled, compression or
    # decompression is not applied on the payload if the payload size is smaller
    # than this value. Setting it to zero allows compression for any payload
    # size.
    minimum_compression_size: int = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The source of the API key for metering requests according to a usage plan.
    # Valid values are:

    #   * `HEADER` to read the API key from the `X-API-Key` header of a request.
    #   * `AUTHORIZER` to read the API key from the `UsageIdentifierKey` from a custom authorizer.
    api_key_source: typing.Union[str, "ApiKeySourceType"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The endpoint configuration of this RestApi showing the endpoint types of
    # the API.
    endpoint_configuration: "EndpointConfiguration" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A stringified JSON policy document that applies to this RestApi regardless
    # of the caller and Method configuration.
    policy: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class CreateStageRequest(ShapeBase):
    """
    Requests API Gateway to create a Stage resource.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "rest_api_id",
                "restApiId",
                TypeInfo(str),
            ),
            (
                "stage_name",
                "stageName",
                TypeInfo(str),
            ),
            (
                "deployment_id",
                "deploymentId",
                TypeInfo(str),
            ),
            (
                "description",
                "description",
                TypeInfo(str),
            ),
            (
                "cache_cluster_enabled",
                "cacheClusterEnabled",
                TypeInfo(bool),
            ),
            (
                "cache_cluster_size",
                "cacheClusterSize",
                TypeInfo(typing.Union[str, CacheClusterSize]),
            ),
            (
                "variables",
                "variables",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "documentation_version",
                "documentationVersion",
                TypeInfo(str),
            ),
            (
                "canary_settings",
                "canarySettings",
                TypeInfo(CanarySettings),
            ),
            (
                "tracing_enabled",
                "tracingEnabled",
                TypeInfo(bool),
            ),
            (
                "tags",
                "tags",
                TypeInfo(typing.Dict[str, str]),
            ),
        ]

    # [Required] The string identifier of the associated RestApi.
    rest_api_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # [Required] The name for the Stage resource.
    stage_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # [Required] The identifier of the Deployment resource for the Stage
    # resource.
    deployment_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The description of the Stage resource.
    description: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Whether cache clustering is enabled for the stage.
    cache_cluster_enabled: bool = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The stage's cache cluster size.
    cache_cluster_size: typing.Union[str, "CacheClusterSize"
                                    ] = dataclasses.field(
                                        default=ShapeBase.NOT_SET,
                                    )

    # A map that defines the stage variables for the new Stage resource. Variable
    # names can have alphanumeric and underscore characters, and the values must
    # match `[A-Za-z0-9-._~:/?#&=,]+`.
    variables: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The version of the associated API documentation.
    documentation_version: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The canary deployment settings of this stage.
    canary_settings: "CanarySettings" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Specifies whether active tracing with X-ray is enabled for the Stage.
    tracing_enabled: bool = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The key-value map of strings. The valid character set is [a-zA-Z+-=._:/].
    # The tag key can be up to 128 characters and must not start with `aws:`. The
    # tag value can be up to 256 characters.
    tags: typing.Dict[str, str] = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class CreateUsagePlanKeyRequest(ShapeBase):
    """
    The POST request to create a usage plan key for adding an existing API key to a
    usage plan.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "usage_plan_id",
                "usagePlanId",
                TypeInfo(str),
            ),
            (
                "key_id",
                "keyId",
                TypeInfo(str),
            ),
            (
                "key_type",
                "keyType",
                TypeInfo(str),
            ),
        ]

    # [Required] The Id of the UsagePlan resource representing the usage plan
    # containing the to-be-created UsagePlanKey resource representing a plan
    # customer.
    usage_plan_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # [Required] The identifier of a UsagePlanKey resource for a plan customer.
    key_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # [Required] The type of a UsagePlanKey resource for a plan customer.
    key_type: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class CreateUsagePlanRequest(ShapeBase):
    """
    The POST request to create a usage plan with the name, description, throttle
    limits and quota limits, as well as the associated API stages, specified in the
    payload.
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
                "api_stages",
                "apiStages",
                TypeInfo(typing.List[ApiStage]),
            ),
            (
                "throttle",
                "throttle",
                TypeInfo(ThrottleSettings),
            ),
            (
                "quota",
                "quota",
                TypeInfo(QuotaSettings),
            ),
        ]

    # [Required] The name of the usage plan.
    name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The description of the usage plan.
    description: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The associated API stages of the usage plan.
    api_stages: typing.List["ApiStage"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The throttling limits of the usage plan.
    throttle: "ThrottleSettings" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The quota of the usage plan.
    quota: "QuotaSettings" = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class CreateVpcLinkRequest(ShapeBase):
    """
    Creates a VPC link, under the caller's account in a selected region, in an
    asynchronous operation that typically takes 2-4 minutes to complete and become
    operational. The caller must have permissions to create and update VPC Endpoint
    services.
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
                "target_arns",
                "targetArns",
                TypeInfo(typing.List[str]),
            ),
            (
                "description",
                "description",
                TypeInfo(str),
            ),
        ]

    # [Required] The name used to label and identify the VPC link.
    name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # [Required] The ARNs of network load balancers of the VPC targeted by the
    # VPC link. The network load balancers must be owned by the same AWS account
    # of the API owner.
    target_arns: typing.List[str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The description of the VPC link.
    description: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DeleteApiKeyRequest(ShapeBase):
    """
    A request to delete the ApiKey resource.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "api_key",
                "apiKey",
                TypeInfo(str),
            ),
        ]

    # [Required] The identifier of the ApiKey resource to be deleted.
    api_key: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DeleteAuthorizerRequest(ShapeBase):
    """
    Request to delete an existing Authorizer resource.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "rest_api_id",
                "restApiId",
                TypeInfo(str),
            ),
            (
                "authorizer_id",
                "authorizerId",
                TypeInfo(str),
            ),
        ]

    # [Required] The string identifier of the associated RestApi.
    rest_api_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # [Required] The identifier of the Authorizer resource.
    authorizer_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DeleteBasePathMappingRequest(ShapeBase):
    """
    A request to delete the BasePathMapping resource.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "domain_name",
                "domainName",
                TypeInfo(str),
            ),
            (
                "base_path",
                "basePath",
                TypeInfo(str),
            ),
        ]

    # [Required] The domain name of the BasePathMapping resource to delete.
    domain_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # [Required] The base path name of the BasePathMapping resource to delete.
    base_path: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DeleteClientCertificateRequest(ShapeBase):
    """
    A request to delete the ClientCertificate resource.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "client_certificate_id",
                "clientCertificateId",
                TypeInfo(str),
            ),
        ]

    # [Required] The identifier of the ClientCertificate resource to be deleted.
    client_certificate_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DeleteDeploymentRequest(ShapeBase):
    """
    Requests API Gateway to delete a Deployment resource.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "rest_api_id",
                "restApiId",
                TypeInfo(str),
            ),
            (
                "deployment_id",
                "deploymentId",
                TypeInfo(str),
            ),
        ]

    # [Required] The string identifier of the associated RestApi.
    rest_api_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # [Required] The identifier of the Deployment resource to delete.
    deployment_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DeleteDocumentationPartRequest(ShapeBase):
    """
    Deletes an existing documentation part of an API.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "rest_api_id",
                "restApiId",
                TypeInfo(str),
            ),
            (
                "documentation_part_id",
                "documentationPartId",
                TypeInfo(str),
            ),
        ]

    # [Required] The string identifier of the associated RestApi.
    rest_api_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # [Required] The identifier of the to-be-deleted documentation part.
    documentation_part_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DeleteDocumentationVersionRequest(ShapeBase):
    """
    Deletes an existing documentation version of an API.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "rest_api_id",
                "restApiId",
                TypeInfo(str),
            ),
            (
                "documentation_version",
                "documentationVersion",
                TypeInfo(str),
            ),
        ]

    # [Required] The string identifier of the associated RestApi.
    rest_api_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # [Required] The version identifier of a to-be-deleted documentation
    # snapshot.
    documentation_version: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DeleteDomainNameRequest(ShapeBase):
    """
    A request to delete the DomainName resource.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "domain_name",
                "domainName",
                TypeInfo(str),
            ),
        ]

    # [Required] The name of the DomainName resource to be deleted.
    domain_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DeleteGatewayResponseRequest(ShapeBase):
    """
    Clears any customization of a GatewayResponse of a specified response type on
    the given RestApi and resets it with the default settings.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "rest_api_id",
                "restApiId",
                TypeInfo(str),
            ),
            (
                "response_type",
                "responseType",
                TypeInfo(typing.Union[str, GatewayResponseType]),
            ),
        ]

    # [Required] The string identifier of the associated RestApi.
    rest_api_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # [Required]

    # The response type of the associated GatewayResponse. Valid values are

    #   * ACCESS_DENIED
    #   * API_CONFIGURATION_ERROR
    #   * AUTHORIZER_FAILURE
    #   * AUTHORIZER_CONFIGURATION_ERROR
    #   * BAD_REQUEST_PARAMETERS
    #   * BAD_REQUEST_BODY
    #   * DEFAULT_4XX
    #   * DEFAULT_5XX
    #   * EXPIRED_TOKEN
    #   * INVALID_SIGNATURE
    #   * INTEGRATION_FAILURE
    #   * INTEGRATION_TIMEOUT
    #   * INVALID_API_KEY
    #   * MISSING_AUTHENTICATION_TOKEN
    #   * QUOTA_EXCEEDED
    #   * REQUEST_TOO_LARGE
    #   * RESOURCE_NOT_FOUND
    #   * THROTTLED
    #   * UNAUTHORIZED
    #   * UNSUPPORTED_MEDIA_TYPE
    response_type: typing.Union[str, "GatewayResponseType"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class DeleteIntegrationRequest(ShapeBase):
    """
    Represents a delete integration request.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "rest_api_id",
                "restApiId",
                TypeInfo(str),
            ),
            (
                "resource_id",
                "resourceId",
                TypeInfo(str),
            ),
            (
                "http_method",
                "httpMethod",
                TypeInfo(str),
            ),
        ]

    # [Required] The string identifier of the associated RestApi.
    rest_api_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # [Required] Specifies a delete integration request's resource identifier.
    resource_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # [Required] Specifies a delete integration request's HTTP method.
    http_method: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DeleteIntegrationResponseRequest(ShapeBase):
    """
    Represents a delete integration response request.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "rest_api_id",
                "restApiId",
                TypeInfo(str),
            ),
            (
                "resource_id",
                "resourceId",
                TypeInfo(str),
            ),
            (
                "http_method",
                "httpMethod",
                TypeInfo(str),
            ),
            (
                "status_code",
                "statusCode",
                TypeInfo(str),
            ),
        ]

    # [Required] The string identifier of the associated RestApi.
    rest_api_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # [Required] Specifies a delete integration response request's resource
    # identifier.
    resource_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # [Required] Specifies a delete integration response request's HTTP method.
    http_method: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # [Required] Specifies a delete integration response request's status code.
    status_code: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DeleteMethodRequest(ShapeBase):
    """
    Request to delete an existing Method resource.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "rest_api_id",
                "restApiId",
                TypeInfo(str),
            ),
            (
                "resource_id",
                "resourceId",
                TypeInfo(str),
            ),
            (
                "http_method",
                "httpMethod",
                TypeInfo(str),
            ),
        ]

    # [Required] The string identifier of the associated RestApi.
    rest_api_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # [Required] The Resource identifier for the Method resource.
    resource_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # [Required] The HTTP verb of the Method resource.
    http_method: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DeleteMethodResponseRequest(ShapeBase):
    """
    A request to delete an existing MethodResponse resource.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "rest_api_id",
                "restApiId",
                TypeInfo(str),
            ),
            (
                "resource_id",
                "resourceId",
                TypeInfo(str),
            ),
            (
                "http_method",
                "httpMethod",
                TypeInfo(str),
            ),
            (
                "status_code",
                "statusCode",
                TypeInfo(str),
            ),
        ]

    # [Required] The string identifier of the associated RestApi.
    rest_api_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # [Required] The Resource identifier for the MethodResponse resource.
    resource_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # [Required] The HTTP verb of the Method resource.
    http_method: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # [Required] The status code identifier for the MethodResponse resource.
    status_code: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DeleteModelRequest(ShapeBase):
    """
    Request to delete an existing model in an existing RestApi resource.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "rest_api_id",
                "restApiId",
                TypeInfo(str),
            ),
            (
                "model_name",
                "modelName",
                TypeInfo(str),
            ),
        ]

    # [Required] The string identifier of the associated RestApi.
    rest_api_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # [Required] The name of the model to delete.
    model_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DeleteRequestValidatorRequest(ShapeBase):
    """
    Deletes a specified RequestValidator of a given RestApi.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "rest_api_id",
                "restApiId",
                TypeInfo(str),
            ),
            (
                "request_validator_id",
                "requestValidatorId",
                TypeInfo(str),
            ),
        ]

    # [Required] The string identifier of the associated RestApi.
    rest_api_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # [Required] The identifier of the RequestValidator to be deleted.
    request_validator_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DeleteResourceRequest(ShapeBase):
    """
    Request to delete a Resource.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "rest_api_id",
                "restApiId",
                TypeInfo(str),
            ),
            (
                "resource_id",
                "resourceId",
                TypeInfo(str),
            ),
        ]

    # [Required] The string identifier of the associated RestApi.
    rest_api_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # [Required] The identifier of the Resource resource.
    resource_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DeleteRestApiRequest(ShapeBase):
    """
    Request to delete the specified API from your collection.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "rest_api_id",
                "restApiId",
                TypeInfo(str),
            ),
        ]

    # [Required] The string identifier of the associated RestApi.
    rest_api_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DeleteStageRequest(ShapeBase):
    """
    Requests API Gateway to delete a Stage resource.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "rest_api_id",
                "restApiId",
                TypeInfo(str),
            ),
            (
                "stage_name",
                "stageName",
                TypeInfo(str),
            ),
        ]

    # [Required] The string identifier of the associated RestApi.
    rest_api_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # [Required] The name of the Stage resource to delete.
    stage_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DeleteUsagePlanKeyRequest(ShapeBase):
    """
    The DELETE request to delete a usage plan key and remove the underlying API key
    from the associated usage plan.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "usage_plan_id",
                "usagePlanId",
                TypeInfo(str),
            ),
            (
                "key_id",
                "keyId",
                TypeInfo(str),
            ),
        ]

    # [Required] The Id of the UsagePlan resource representing the usage plan
    # containing the to-be-deleted UsagePlanKey resource representing a plan
    # customer.
    usage_plan_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # [Required] The Id of the UsagePlanKey resource to be deleted.
    key_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DeleteUsagePlanRequest(ShapeBase):
    """
    The DELETE request to delete a usage plan of a given plan Id.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "usage_plan_id",
                "usagePlanId",
                TypeInfo(str),
            ),
        ]

    # [Required] The Id of the to-be-deleted usage plan.
    usage_plan_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DeleteVpcLinkRequest(ShapeBase):
    """
    Deletes an existing VpcLink of a specified identifier.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "vpc_link_id",
                "vpcLinkId",
                TypeInfo(str),
            ),
        ]

    # [Required] The identifier of the VpcLink. It is used in an Integration to
    # reference this VpcLink.
    vpc_link_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class Deployment(OutputShapeBase):
    """
    An immutable representation of a RestApi resource that can be called by users
    using Stages. A deployment must be associated with a Stage for it to be callable
    over the Internet.

    To create a deployment, call `POST` on the Deployments resource of a RestApi. To
    view, update, or delete a deployment, call `GET`, `PATCH`, or `DELETE` on the
    specified deployment resource
    (`/restapis/{restapi_id}/deployments/{deployment_id}`).

    RestApi, Deployments, Stage, [AWS
    CLI](http://docs.aws.amazon.com/cli/latest/reference/apigateway/get-
    deployment.html), [AWS SDKs](https://aws.amazon.com/tools/)
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
                "created_date",
                "createdDate",
                TypeInfo(datetime.datetime),
            ),
            (
                "api_summary",
                "apiSummary",
                TypeInfo(typing.Dict[str, typing.Dict[str, MethodSnapshot]]),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The identifier for the deployment resource.
    id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The description for the deployment resource.
    description: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The date and time that the deployment resource was created.
    created_date: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A summary of the RestApi at the date and time that the deployment resource
    # was created.
    api_summary: typing.Dict[str, typing.
                             Dict[str, "MethodSnapshot"]] = dataclasses.field(
                                 default=ShapeBase.NOT_SET,
                             )


@dataclasses.dataclass
class DeploymentCanarySettings(ShapeBase):
    """
    The input configuration for a canary deployment.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "percent_traffic",
                "percentTraffic",
                TypeInfo(float),
            ),
            (
                "stage_variable_overrides",
                "stageVariableOverrides",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "use_stage_cache",
                "useStageCache",
                TypeInfo(bool),
            ),
        ]

    # The percentage (0.0-100.0) of traffic routed to the canary deployment.
    percent_traffic: float = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A stage variable overrides used for the canary release deployment. They can
    # override existing stage variables or add new stage variables for the canary
    # release deployment. These stage variables are represented as a string-to-
    # string map between stage variable names and their values.
    stage_variable_overrides: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A Boolean flag to indicate whether the canary release deployment uses the
    # stage cache or not.
    use_stage_cache: bool = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class Deployments(OutputShapeBase):
    """
    Represents a collection resource that contains zero or more references to your
    existing deployments, and links that guide you on how to interact with your
    collection. The collection offers a paginated view of the contained deployments.

    To create a new deployment of a RestApi, make a `POST` request against this
    resource. To view, update, or delete an existing deployment, make a `GET`,
    `PATCH`, or `DELETE` request, respectively, on a specified Deployment resource.

    [Deploying an
    API](http://docs.aws.amazon.com/apigateway/latest/developerguide/how-to-deploy-
    api.html), [AWS
    CLI](http://docs.aws.amazon.com/cli/latest/reference/apigateway/get-
    deployment.html), [AWS SDKs](https://aws.amazon.com/tools/)
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
                "position",
                "position",
                TypeInfo(str),
            ),
            (
                "items",
                "items",
                TypeInfo(typing.List[Deployment]),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )
    position: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The current page of elements from this collection.
    items: typing.List["Deployment"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    def paginate(self, ) -> typing.Generator["Deployments", None, None]:
        yield from super()._paginate()


@dataclasses.dataclass
class DocumentationPart(OutputShapeBase):
    """
    A documentation part for a targeted API entity.

    A documentation part consists of a content map (`properties`) and a target
    (`location`). The target specifies an API entity to which the documentation
    content applies. The supported API entity types are `API`, `AUTHORIZER`,
    `MODEL`, `RESOURCE`, `METHOD`, `PATH_PARAMETER`, `QUERY_PARAMETER`,
    `REQUEST_HEADER`, `REQUEST_BODY`, `RESPONSE`, `RESPONSE_HEADER`, and
    `RESPONSE_BODY`. Valid `location` fields depend on the API entity type. All
    valid fields are not required.

    The content map is a JSON string of API-specific key-value pairs. Although an
    API can use any shape for the content map, only the Swagger-compliant
    documentation fields will be injected into the associated API entity definition
    in the exported Swagger definition file.

    [Documenting an
    API](http://docs.aws.amazon.com/apigateway/latest/developerguide/api-gateway-
    documenting-api.html), DocumentationParts
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
                "id",
                "id",
                TypeInfo(str),
            ),
            (
                "location",
                "location",
                TypeInfo(DocumentationPartLocation),
            ),
            (
                "properties",
                "properties",
                TypeInfo(str),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The DocumentationPart identifier, generated by API Gateway when the
    # `DocumentationPart` is created.
    id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The location of the API entity to which the documentation applies. Valid
    # fields depend on the targeted API entity type. All the valid location
    # fields are not required. If not explicitly specified, a valid location
    # field is treated as a wildcard and associated documentation content may be
    # inherited by matching entities, unless overridden.
    location: "DocumentationPartLocation" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A content map of API-specific key-value pairs describing the targeted API
    # entity. The map must be encoded as a JSON string, e.g., `"{
    # \"description\": \"The API does ...\" }"`. Only Swagger-compliant
    # documentation-related fields from the properties map are exported and,
    # hence, published as part of the API entity definitions, while the original
    # documentation parts are exported in a Swagger extension of `x-amazon-
    # apigateway-documentation`.
    properties: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DocumentationPartIds(OutputShapeBase):
    """
    A collection of the imported DocumentationPart identifiers.

    This is used to return the result when documentation parts in an external (e.g.,
    Swagger) file are imported into API Gateway

    [Documenting an
    API](http://docs.aws.amazon.com/apigateway/latest/developerguide/api-gateway-
    documenting-api.html),
    [documentationpart:import](http://docs.aws.amazon.com/apigateway/api-
    reference/link-relation/documentationpart-import/), DocumentationPart
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
                "ids",
                "ids",
                TypeInfo(typing.List[str]),
            ),
            (
                "warnings",
                "warnings",
                TypeInfo(typing.List[str]),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A list of the returned documentation part identifiers.
    ids: typing.List[str] = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A list of warning messages reported during import of documentation parts.
    warnings: typing.List[str] = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DocumentationPartLocation(ShapeBase):
    """
    Specifies the target API entity to which the documentation applies.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "type",
                "type",
                TypeInfo(typing.Union[str, DocumentationPartType]),
            ),
            (
                "path",
                "path",
                TypeInfo(str),
            ),
            (
                "method",
                "method",
                TypeInfo(str),
            ),
            (
                "status_code",
                "statusCode",
                TypeInfo(str),
            ),
            (
                "name",
                "name",
                TypeInfo(str),
            ),
        ]

    # [Required] The type of API entity to which the documentation content
    # applies. Valid values are `API`, `AUTHORIZER`, `MODEL`, `RESOURCE`,
    # `METHOD`, `PATH_PARAMETER`, `QUERY_PARAMETER`, `REQUEST_HEADER`,
    # `REQUEST_BODY`, `RESPONSE`, `RESPONSE_HEADER`, and `RESPONSE_BODY`. Content
    # inheritance does not apply to any entity of the `API`, `AUTHORIZER`,
    # `METHOD`, `MODEL`, `REQUEST_BODY`, or `RESOURCE` type.
    type: typing.Union[str, "DocumentationPartType"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The URL path of the target. It is a valid field for the API entity types of
    # `RESOURCE`, `METHOD`, `PATH_PARAMETER`, `QUERY_PARAMETER`,
    # `REQUEST_HEADER`, `REQUEST_BODY`, `RESPONSE`, `RESPONSE_HEADER`, and
    # `RESPONSE_BODY`. The default value is `/` for the root resource. When an
    # applicable child entity inherits the content of another entity of the same
    # type with more general specifications of the other `location` attributes,
    # the child entity's `path` attribute must match that of the parent entity as
    # a prefix.
    path: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The HTTP verb of a method. It is a valid field for the API entity types of
    # `METHOD`, `PATH_PARAMETER`, `QUERY_PARAMETER`, `REQUEST_HEADER`,
    # `REQUEST_BODY`, `RESPONSE`, `RESPONSE_HEADER`, and `RESPONSE_BODY`. The
    # default value is `*` for any method. When an applicable child entity
    # inherits the content of an entity of the same type with more general
    # specifications of the other `location` attributes, the child entity's
    # `method` attribute must match that of the parent entity exactly.
    method: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The HTTP status code of a response. It is a valid field for the API entity
    # types of `RESPONSE`, `RESPONSE_HEADER`, and `RESPONSE_BODY`. The default
    # value is `*` for any status code. When an applicable child entity inherits
    # the content of an entity of the same type with more general specifications
    # of the other `location` attributes, the child entity's `statusCode`
    # attribute must match that of the parent entity exactly.
    status_code: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The name of the targeted API entity. It is a valid and required field for
    # the API entity types of `AUTHORIZER`, `MODEL`, `PATH_PARAMETER`,
    # `QUERY_PARAMETER`, `REQUEST_HEADER`, `REQUEST_BODY` and `RESPONSE_HEADER`.
    # It is an invalid field for any other entity type.
    name: str = dataclasses.field(default=ShapeBase.NOT_SET, )


class DocumentationPartType(str):
    API = "API"
    AUTHORIZER = "AUTHORIZER"
    MODEL = "MODEL"
    RESOURCE = "RESOURCE"
    METHOD = "METHOD"
    PATH_PARAMETER = "PATH_PARAMETER"
    QUERY_PARAMETER = "QUERY_PARAMETER"
    REQUEST_HEADER = "REQUEST_HEADER"
    REQUEST_BODY = "REQUEST_BODY"
    RESPONSE = "RESPONSE"
    RESPONSE_HEADER = "RESPONSE_HEADER"
    RESPONSE_BODY = "RESPONSE_BODY"


@dataclasses.dataclass
class DocumentationParts(OutputShapeBase):
    """
    The collection of documentation parts of an API.

    [Documenting an
    API](http://docs.aws.amazon.com/apigateway/latest/developerguide/api-gateway-
    documenting-api.html), DocumentationPart
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
                "position",
                "position",
                TypeInfo(str),
            ),
            (
                "items",
                "items",
                TypeInfo(typing.List[DocumentationPart]),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )
    position: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The current page of elements from this collection.
    items: typing.List["DocumentationPart"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class DocumentationVersion(OutputShapeBase):
    """
    A snapshot of the documentation of an API.

    Publishing API documentation involves creating a documentation version
    associated with an API stage and exporting the versioned documentation to an
    external (e.g., Swagger) file.

    [Documenting an
    API](http://docs.aws.amazon.com/apigateway/latest/developerguide/api-gateway-
    documenting-api.html), DocumentationPart, DocumentationVersions
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
                "version",
                "version",
                TypeInfo(str),
            ),
            (
                "created_date",
                "createdDate",
                TypeInfo(datetime.datetime),
            ),
            (
                "description",
                "description",
                TypeInfo(str),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The version identifier of the API documentation snapshot.
    version: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The date when the API documentation snapshot is created.
    created_date: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The description of the API documentation snapshot.
    description: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DocumentationVersions(OutputShapeBase):
    """
    The collection of documentation snapshots of an API.

    Use the DocumentationVersions to manage documentation snapshots associated with
    various API stages.

    [Documenting an
    API](http://docs.aws.amazon.com/apigateway/latest/developerguide/api-gateway-
    documenting-api.html), DocumentationPart, DocumentationVersion
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
                "position",
                "position",
                TypeInfo(str),
            ),
            (
                "items",
                "items",
                TypeInfo(typing.List[DocumentationVersion]),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )
    position: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The current page of elements from this collection.
    items: typing.List["DocumentationVersion"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class DomainName(OutputShapeBase):
    """
    Represents a custom domain name as a user-friendly host name of an API
    (RestApi).

    When you deploy an API, API Gateway creates a default host name for the API.
    This default API host name is of the `{restapi-id}.execute-
    api.{region}.amazonaws.com` format. With the default host name, you can access
    the API's root resource with the URL of `https://{restapi-id}.execute-
    api.{region}.amazonaws.com/{stage}/`. When you set up a custom domain name of
    `apis.example.com` for this API, you can then access the same resource using the
    URL of the `https://apis.examples.com/myApi`, where `myApi` is the base path
    mapping (BasePathMapping) of your API under the custom domain name.

    [Set a Custom Host Name for an
    API](http://docs.aws.amazon.com/apigateway/latest/developerguide/how-to-custom-
    domains.html)
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
                "domain_name",
                "domainName",
                TypeInfo(str),
            ),
            (
                "certificate_name",
                "certificateName",
                TypeInfo(str),
            ),
            (
                "certificate_arn",
                "certificateArn",
                TypeInfo(str),
            ),
            (
                "certificate_upload_date",
                "certificateUploadDate",
                TypeInfo(datetime.datetime),
            ),
            (
                "regional_domain_name",
                "regionalDomainName",
                TypeInfo(str),
            ),
            (
                "regional_hosted_zone_id",
                "regionalHostedZoneId",
                TypeInfo(str),
            ),
            (
                "regional_certificate_name",
                "regionalCertificateName",
                TypeInfo(str),
            ),
            (
                "regional_certificate_arn",
                "regionalCertificateArn",
                TypeInfo(str),
            ),
            (
                "distribution_domain_name",
                "distributionDomainName",
                TypeInfo(str),
            ),
            (
                "distribution_hosted_zone_id",
                "distributionHostedZoneId",
                TypeInfo(str),
            ),
            (
                "endpoint_configuration",
                "endpointConfiguration",
                TypeInfo(EndpointConfiguration),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The custom domain name as an API host name, for example, `my-
    # api.example.com`.
    domain_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The name of the certificate that will be used by edge-optimized endpoint
    # for this domain name.
    certificate_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The reference to an AWS-managed certificate that will be used by edge-
    # optimized endpoint for this domain name. AWS Certificate Manager is the
    # only supported source.
    certificate_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The timestamp when the certificate that was used by edge-optimized endpoint
    # for this domain name was uploaded.
    certificate_upload_date: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The domain name associated with the regional endpoint for this custom
    # domain name. You set up this association by adding a DNS record that points
    # the custom domain name to this regional domain name. The regional domain
    # name is returned by API Gateway when you create a regional endpoint.
    regional_domain_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The region-specific Amazon Route 53 Hosted Zone ID of the regional
    # endpoint. For more information, see [Set up a Regional Custom Domain
    # Name](https://docs.aws.amazon.com/apigateway/latest/developerguide/apigateway-
    # regional-api-custom-domain-create.html) and [AWS Regions and Endpoints for
    # API
    # Gateway](http://docs.aws.amazon.com/general/latest/gr/rande.html#apigateway_region).
    regional_hosted_zone_id: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The name of the certificate that will be used for validating the regional
    # domain name.
    regional_certificate_name: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The reference to an AWS-managed certificate that will be used for
    # validating the regional domain name. AWS Certificate Manager is the only
    # supported source.
    regional_certificate_arn: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The domain name of the Amazon CloudFront distribution associated with this
    # custom domain name for an edge-optimized endpoint. You set up this
    # association when adding a DNS record pointing the custom domain name to
    # this distribution name. For more information about CloudFront
    # distributions, see the [Amazon CloudFront
    # documentation](http://aws.amazon.com/documentation/cloudfront/).
    distribution_domain_name: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The region-agnostic Amazon Route 53 Hosted Zone ID of the edge-optimized
    # endpoint. The valid value is `Z2FDTNDATAQYW2` for all the regions. For more
    # information, see [Set up a Regional Custom Domain
    # Name](https://docs.aws.amazon.com/apigateway/latest/developerguide/apigateway-
    # regional-api-custom-domain-create.html) and [AWS Regions and Endpoints for
    # API
    # Gateway](http://docs.aws.amazon.com/general/latest/gr/rande.html#apigateway_region).
    distribution_hosted_zone_id: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The endpoint configuration of this DomainName showing the endpoint types of
    # the domain name.
    endpoint_configuration: "EndpointConfiguration" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class DomainNames(OutputShapeBase):
    """
    Represents a collection of DomainName resources.

    [Use Client-Side
    Certificate](http://docs.aws.amazon.com/apigateway/latest/developerguide/how-to-
    custom-domains.html)
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
                "position",
                "position",
                TypeInfo(str),
            ),
            (
                "items",
                "items",
                TypeInfo(typing.List[DomainName]),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )
    position: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The current page of elements from this collection.
    items: typing.List["DomainName"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    def paginate(self, ) -> typing.Generator["DomainNames", None, None]:
        yield from super()._paginate()


@dataclasses.dataclass
class EndpointConfiguration(ShapeBase):
    """
    The endpoint configuration to indicate the types of endpoints an API (RestApi)
    or its custom domain name (DomainName) has.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "types",
                "types",
                TypeInfo(typing.List[typing.Union[str, EndpointType]]),
            ),
        ]

    # A list of endpoint types of an API (RestApi) or its custom domain name
    # (DomainName). For an edge-optimized API and its custom domain name, the
    # endpoint type is `"EDGE"`. For a regional API and its custom domain name,
    # the endpoint type is `REGIONAL`. For a private API, the endpoint type is
    # `PRIVATE`.
    types: typing.List[typing.Union[str, "EndpointType"]] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


class EndpointType(str):
    """
    The endpoint type. The valid values are `EDGE` for edge-optimized API setup,
    most suitable for mobile applications; `REGIONAL` for regional API endpoint
    setup, most suitable for calling from AWS Region; and `PRIVATE` for private
    APIs.
    """
    REGIONAL = "REGIONAL"
    EDGE = "EDGE"
    PRIVATE = "PRIVATE"


@dataclasses.dataclass
class ExportResponse(OutputShapeBase):
    """
    The binary blob response to GetExport, which contains the generated SDK.
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
                "content_type",
                "contentType",
                TypeInfo(str),
            ),
            (
                "content_disposition",
                "contentDisposition",
                TypeInfo(str),
            ),
            (
                "body",
                "body",
                TypeInfo(typing.Any),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The content-type header value in the HTTP response. This will correspond to
    # a valid 'accept' type in the request.
    content_type: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The content-disposition header value in the HTTP response.
    content_disposition: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The binary blob response to GetExport, which contains the export.
    body: typing.Any = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class FlushStageAuthorizersCacheRequest(ShapeBase):
    """
    Request to flush authorizer cache entries on a specified stage.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "rest_api_id",
                "restApiId",
                TypeInfo(str),
            ),
            (
                "stage_name",
                "stageName",
                TypeInfo(str),
            ),
        ]

    # The string identifier of the associated RestApi.
    rest_api_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The name of the stage to flush.
    stage_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class FlushStageCacheRequest(ShapeBase):
    """
    Requests API Gateway to flush a stage's cache.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "rest_api_id",
                "restApiId",
                TypeInfo(str),
            ),
            (
                "stage_name",
                "stageName",
                TypeInfo(str),
            ),
        ]

    # [Required] The string identifier of the associated RestApi.
    rest_api_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # [Required] The name of the stage to flush its cache.
    stage_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class GatewayResponse(OutputShapeBase):
    """
    A gateway response of a given response type and status code, with optional
    response parameters and mapping templates.

    For more information about valid gateway response types, see [Gateway Response
    Types Supported by API
    Gateway](http://docs.aws.amazon.com/apigateway/latest/developerguide/supported-
    gateway-response-types.html)

    #### Example: Get a Gateway Response of a given response type

    ##### Request

    This example shows how to get a gateway response of the
    `MISSING_AUTHENTICATION_TOKEN` type.



        GET /restapis/o81lxisefl/gatewayresponses/MISSING_AUTHENTICATION_TOKEN HTTP/1.1 Host: beta-apigateway.us-east-1.amazonaws.com Content-Type: application/json X-Amz-Date: 20170503T202516Z Authorization: AWS4-HMAC-SHA256 Credential={access-key-id}/20170503/us-east-1/apigateway/aws4_request, SignedHeaders=content-type;host;x-amz-date, Signature=1b52460e3159c1a26cff29093855d50ea141c1c5b937528fecaf60f51129697a Cache-Control: no-cache Postman-Token: 3b2a1ce9-c848-2e26-2e2f-9c2caefbed45 

    The response type is specified as a URL path.

    ##### Response

    The successful operation returns the `200 OK` status code and a payload similar
    to the following:



        { "_links": { "curies": { "href": "http://docs.aws.amazon.com/apigateway/latest/developerguide/restapi-gatewayresponse-{rel}.html", "name": "gatewayresponse", "templated": true }, "self": { "href": "/restapis/o81lxisefl/gatewayresponses/MISSING_AUTHENTICATION_TOKEN" }, "gatewayresponse:delete": { "href": "/restapis/o81lxisefl/gatewayresponses/MISSING_AUTHENTICATION_TOKEN" }, "gatewayresponse:put": { "href": "/restapis/o81lxisefl/gatewayresponses/{response_type}", "templated": true }, "gatewayresponse:update": { "href": "/restapis/o81lxisefl/gatewayresponses/MISSING_AUTHENTICATION_TOKEN" } }, "defaultResponse": false, "responseParameters": { "gatewayresponse.header.x-request-path": "method.request.path.petId", "gatewayresponse.header.Access-Control-Allow-Origin": "'a.b.c'", "gatewayresponse.header.x-request-query": "method.request.querystring.q", "gatewayresponse.header.x-request-header": "method.request.header.Accept" }, "responseTemplates": { "application/json": "{\n \"message\": $context.error.messageString,\n \"type\": \"$context.error.responseType\",\n \"stage\": \"$context.stage\",\n \"resourcePath\": \"$context.resourcePath\",\n \"stageVariables.a\": \"$stageVariables.a\",\n \"statusCode\": \"'404'\"\n}" }, "responseType": "MISSING_AUTHENTICATION_TOKEN", "statusCode": "404" }

    [Customize Gateway
    Responses](http://docs.aws.amazon.com/apigateway/latest/developerguide/customize-
    gateway-responses.html)
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
                "response_type",
                "responseType",
                TypeInfo(typing.Union[str, GatewayResponseType]),
            ),
            (
                "status_code",
                "statusCode",
                TypeInfo(str),
            ),
            (
                "response_parameters",
                "responseParameters",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "response_templates",
                "responseTemplates",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "default_response",
                "defaultResponse",
                TypeInfo(bool),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The response type of the associated GatewayResponse. Valid values are

    #   * ACCESS_DENIED
    #   * API_CONFIGURATION_ERROR
    #   * AUTHORIZER_FAILURE
    #   * AUTHORIZER_CONFIGURATION_ERROR
    #   * BAD_REQUEST_PARAMETERS
    #   * BAD_REQUEST_BODY
    #   * DEFAULT_4XX
    #   * DEFAULT_5XX
    #   * EXPIRED_TOKEN
    #   * INVALID_SIGNATURE
    #   * INTEGRATION_FAILURE
    #   * INTEGRATION_TIMEOUT
    #   * INVALID_API_KEY
    #   * MISSING_AUTHENTICATION_TOKEN
    #   * QUOTA_EXCEEDED
    #   * REQUEST_TOO_LARGE
    #   * RESOURCE_NOT_FOUND
    #   * THROTTLED
    #   * UNAUTHORIZED
    #   * UNSUPPORTED_MEDIA_TYPE
    response_type: typing.Union[str, "GatewayResponseType"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The HTTP status code for this GatewayResponse.
    status_code: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Response parameters (paths, query strings and headers) of the
    # GatewayResponse as a string-to-string map of key-value pairs.
    response_parameters: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Response templates of the GatewayResponse as a string-to-string map of key-
    # value pairs.
    response_templates: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A Boolean flag to indicate whether this GatewayResponse is the default
    # gateway response (`true`) or not (`false`). A default gateway response is
    # one generated by API Gateway without any customization by an API developer.
    default_response: bool = dataclasses.field(default=ShapeBase.NOT_SET, )


class GatewayResponseType(str):
    DEFAULT_4XX = "DEFAULT_4XX"
    DEFAULT_5XX = "DEFAULT_5XX"
    RESOURCE_NOT_FOUND = "RESOURCE_NOT_FOUND"
    UNAUTHORIZED = "UNAUTHORIZED"
    INVALID_API_KEY = "INVALID_API_KEY"
    ACCESS_DENIED = "ACCESS_DENIED"
    AUTHORIZER_FAILURE = "AUTHORIZER_FAILURE"
    AUTHORIZER_CONFIGURATION_ERROR = "AUTHORIZER_CONFIGURATION_ERROR"
    INVALID_SIGNATURE = "INVALID_SIGNATURE"
    EXPIRED_TOKEN = "EXPIRED_TOKEN"
    MISSING_AUTHENTICATION_TOKEN = "MISSING_AUTHENTICATION_TOKEN"
    INTEGRATION_FAILURE = "INTEGRATION_FAILURE"
    INTEGRATION_TIMEOUT = "INTEGRATION_TIMEOUT"
    API_CONFIGURATION_ERROR = "API_CONFIGURATION_ERROR"
    UNSUPPORTED_MEDIA_TYPE = "UNSUPPORTED_MEDIA_TYPE"
    BAD_REQUEST_PARAMETERS = "BAD_REQUEST_PARAMETERS"
    BAD_REQUEST_BODY = "BAD_REQUEST_BODY"
    REQUEST_TOO_LARGE = "REQUEST_TOO_LARGE"
    THROTTLED = "THROTTLED"
    QUOTA_EXCEEDED = "QUOTA_EXCEEDED"


@dataclasses.dataclass
class GatewayResponses(OutputShapeBase):
    """
    The collection of the GatewayResponse instances of a RestApi as a
    `responseType`-to-GatewayResponse object map of key-value pairs. As such,
    pagination is not supported for querying this collection.

    For more information about valid gateway response types, see [Gateway Response
    Types Supported by API
    Gateway](http://docs.aws.amazon.com/apigateway/latest/developerguide/supported-
    gateway-response-types.html)

    #### Example: Get the collection of gateway responses of an API

    ##### Request

    This example request shows how to retrieve the GatewayResponses collection from
    an API.



        GET /restapis/o81lxisefl/gatewayresponses HTTP/1.1 Host: beta-apigateway.us-east-1.amazonaws.com Content-Type: application/json X-Amz-Date: 20170503T220604Z Authorization: AWS4-HMAC-SHA256 Credential={access-key-id}/20170503/us-east-1/apigateway/aws4_request, SignedHeaders=content-type;host;x-amz-date, Signature=59b42fe54a76a5de8adf2c67baa6d39206f8e9ad49a1d77ccc6a5da3103a398a Cache-Control: no-cache Postman-Token: 5637af27-dc29-fc5c-9dfe-0645d52cb515 

    ##### Response

    The successful operation returns the `200 OK` status code and a payload similar
    to the following:



        { "_links": { "curies": { "href": "http://docs.aws.amazon.com/apigateway/latest/developerguide/restapi-gatewayresponse-{rel}.html", "name": "gatewayresponse", "templated": true }, "self": { "href": "/restapis/o81lxisefl/gatewayresponses" }, "first": { "href": "/restapis/o81lxisefl/gatewayresponses" }, "gatewayresponse:by-type": { "href": "/restapis/o81lxisefl/gatewayresponses/{response_type}", "templated": true }, "item": [ { "href": "/restapis/o81lxisefl/gatewayresponses/INTEGRATION_FAILURE" }, { "href": "/restapis/o81lxisefl/gatewayresponses/RESOURCE_NOT_FOUND" }, { "href": "/restapis/o81lxisefl/gatewayresponses/REQUEST_TOO_LARGE" }, { "href": "/restapis/o81lxisefl/gatewayresponses/THROTTLED" }, { "href": "/restapis/o81lxisefl/gatewayresponses/UNSUPPORTED_MEDIA_TYPE" }, { "href": "/restapis/o81lxisefl/gatewayresponses/AUTHORIZER_CONFIGURATION_ERROR" }, { "href": "/restapis/o81lxisefl/gatewayresponses/DEFAULT_5XX" }, { "href": "/restapis/o81lxisefl/gatewayresponses/DEFAULT_4XX" }, { "href": "/restapis/o81lxisefl/gatewayresponses/BAD_REQUEST_PARAMETERS" }, { "href": "/restapis/o81lxisefl/gatewayresponses/BAD_REQUEST_BODY" }, { "href": "/restapis/o81lxisefl/gatewayresponses/EXPIRED_TOKEN" }, { "href": "/restapis/o81lxisefl/gatewayresponses/ACCESS_DENIED" }, { "href": "/restapis/o81lxisefl/gatewayresponses/INVALID_API_KEY" }, { "href": "/restapis/o81lxisefl/gatewayresponses/UNAUTHORIZED" }, { "href": "/restapis/o81lxisefl/gatewayresponses/API_CONFIGURATION_ERROR" }, { "href": "/restapis/o81lxisefl/gatewayresponses/QUOTA_EXCEEDED" }, { "href": "/restapis/o81lxisefl/gatewayresponses/INTEGRATION_TIMEOUT" }, { "href": "/restapis/o81lxisefl/gatewayresponses/MISSING_AUTHENTICATION_TOKEN" }, { "href": "/restapis/o81lxisefl/gatewayresponses/INVALID_SIGNATURE" }, { "href": "/restapis/o81lxisefl/gatewayresponses/AUTHORIZER_FAILURE" } ] }, "_embedded": { "item": [ { "_links": { "self": { "href": "/restapis/o81lxisefl/gatewayresponses/INTEGRATION_FAILURE" }, "gatewayresponse:put": { "href": "/restapis/o81lxisefl/gatewayresponses/{response_type}", "templated": true }, "gatewayresponse:update": { "href": "/restapis/o81lxisefl/gatewayresponses/INTEGRATION_FAILURE" } }, "defaultResponse": true, "responseParameters": {}, "responseTemplates": { "application/json": "{\"message\":$context.error.messageString}" }, "responseType": "INTEGRATION_FAILURE", "statusCode": "504" }, { "_links": { "self": { "href": "/restapis/o81lxisefl/gatewayresponses/RESOURCE_NOT_FOUND" }, "gatewayresponse:put": { "href": "/restapis/o81lxisefl/gatewayresponses/{response_type}", "templated": true }, "gatewayresponse:update": { "href": "/restapis/o81lxisefl/gatewayresponses/RESOURCE_NOT_FOUND" } }, "defaultResponse": true, "responseParameters": {}, "responseTemplates": { "application/json": "{\"message\":$context.error.messageString}" }, "responseType": "RESOURCE_NOT_FOUND", "statusCode": "404" }, { "_links": { "self": { "href": "/restapis/o81lxisefl/gatewayresponses/REQUEST_TOO_LARGE" }, "gatewayresponse:put": { "href": "/restapis/o81lxisefl/gatewayresponses/{response_type}", "templated": true }, "gatewayresponse:update": { "href": "/restapis/o81lxisefl/gatewayresponses/REQUEST_TOO_LARGE" } }, "defaultResponse": true, "responseParameters": {}, "responseTemplates": { "application/json": "{\"message\":$context.error.messageString}" }, "responseType": "REQUEST_TOO_LARGE", "statusCode": "413" }, { "_links": { "self": { "href": "/restapis/o81lxisefl/gatewayresponses/THROTTLED" }, "gatewayresponse:put": { "href": "/restapis/o81lxisefl/gatewayresponses/{response_type}", "templated": true }, "gatewayresponse:update": { "href": "/restapis/o81lxisefl/gatewayresponses/THROTTLED" } }, "defaultResponse": true, "responseParameters": {}, "responseTemplates": { "application/json": "{\"message\":$context.error.messageString}" }, "responseType": "THROTTLED", "statusCode": "429" }, { "_links": { "self": { "href": "/restapis/o81lxisefl/gatewayresponses/UNSUPPORTED_MEDIA_TYPE" }, "gatewayresponse:put": { "href": "/restapis/o81lxisefl/gatewayresponses/{response_type}", "templated": true }, "gatewayresponse:update": { "href": "/restapis/o81lxisefl/gatewayresponses/UNSUPPORTED_MEDIA_TYPE" } }, "defaultResponse": true, "responseParameters": {}, "responseTemplates": { "application/json": "{\"message\":$context.error.messageString}" }, "responseType": "UNSUPPORTED_MEDIA_TYPE", "statusCode": "415" }, { "_links": { "self": { "href": "/restapis/o81lxisefl/gatewayresponses/AUTHORIZER_CONFIGURATION_ERROR" }, "gatewayresponse:put": { "href": "/restapis/o81lxisefl/gatewayresponses/{response_type}", "templated": true }, "gatewayresponse:update": { "href": "/restapis/o81lxisefl/gatewayresponses/AUTHORIZER_CONFIGURATION_ERROR" } }, "defaultResponse": true, "responseParameters": {}, "responseTemplates": { "application/json": "{\"message\":$context.error.messageString}" }, "responseType": "AUTHORIZER_CONFIGURATION_ERROR", "statusCode": "500" }, { "_links": { "self": { "href": "/restapis/o81lxisefl/gatewayresponses/DEFAULT_5XX" }, "gatewayresponse:put": { "href": "/restapis/o81lxisefl/gatewayresponses/{response_type}", "templated": true }, "gatewayresponse:update": { "href": "/restapis/o81lxisefl/gatewayresponses/DEFAULT_5XX" } }, "defaultResponse": true, "responseParameters": {}, "responseTemplates": { "application/json": "{\"message\":$context.error.messageString}" }, "responseType": "DEFAULT_5XX" }, { "_links": { "self": { "href": "/restapis/o81lxisefl/gatewayresponses/DEFAULT_4XX" }, "gatewayresponse:put": { "href": "/restapis/o81lxisefl/gatewayresponses/{response_type}", "templated": true }, "gatewayresponse:update": { "href": "/restapis/o81lxisefl/gatewayresponses/DEFAULT_4XX" } }, "defaultResponse": true, "responseParameters": {}, "responseTemplates": { "application/json": "{\"message\":$context.error.messageString}" }, "responseType": "DEFAULT_4XX" }, { "_links": { "self": { "href": "/restapis/o81lxisefl/gatewayresponses/BAD_REQUEST_PARAMETERS" }, "gatewayresponse:put": { "href": "/restapis/o81lxisefl/gatewayresponses/{response_type}", "templated": true }, "gatewayresponse:update": { "href": "/restapis/o81lxisefl/gatewayresponses/BAD_REQUEST_PARAMETERS" } }, "defaultResponse": true, "responseParameters": {}, "responseTemplates": { "application/json": "{\"message\":$context.error.messageString}" }, "responseType": "BAD_REQUEST_PARAMETERS", "statusCode": "400" }, { "_links": { "self": { "href": "/restapis/o81lxisefl/gatewayresponses/BAD_REQUEST_BODY" }, "gatewayresponse:put": { "href": "/restapis/o81lxisefl/gatewayresponses/{response_type}", "templated": true }, "gatewayresponse:update": { "href": "/restapis/o81lxisefl/gatewayresponses/BAD_REQUEST_BODY" } }, "defaultResponse": true, "responseParameters": {}, "responseTemplates": { "application/json": "{\"message\":$context.error.messageString}" }, "responseType": "BAD_REQUEST_BODY", "statusCode": "400" }, { "_links": { "self": { "href": "/restapis/o81lxisefl/gatewayresponses/EXPIRED_TOKEN" }, "gatewayresponse:put": { "href": "/restapis/o81lxisefl/gatewayresponses/{response_type}", "templated": true }, "gatewayresponse:update": { "href": "/restapis/o81lxisefl/gatewayresponses/EXPIRED_TOKEN" } }, "defaultResponse": true, "responseParameters": {}, "responseTemplates": { "application/json": "{\"message\":$context.error.messageString}" }, "responseType": "EXPIRED_TOKEN", "statusCode": "403" }, { "_links": { "self": { "href": "/restapis/o81lxisefl/gatewayresponses/ACCESS_DENIED" }, "gatewayresponse:put": { "href": "/restapis/o81lxisefl/gatewayresponses/{response_type}", "templated": true }, "gatewayresponse:update": { "href": "/restapis/o81lxisefl/gatewayresponses/ACCESS_DENIED" } }, "defaultResponse": true, "responseParameters": {}, "responseTemplates": { "application/json": "{\"message\":$context.error.messageString}" }, "responseType": "ACCESS_DENIED", "statusCode": "403" }, { "_links": { "self": { "href": "/restapis/o81lxisefl/gatewayresponses/INVALID_API_KEY" }, "gatewayresponse:put": { "href": "/restapis/o81lxisefl/gatewayresponses/{response_type}", "templated": true }, "gatewayresponse:update": { "href": "/restapis/o81lxisefl/gatewayresponses/INVALID_API_KEY" } }, "defaultResponse": true, "responseParameters": {}, "responseTemplates": { "application/json": "{\"message\":$context.error.messageString}" }, "responseType": "INVALID_API_KEY", "statusCode": "403" }, { "_links": { "self": { "href": "/restapis/o81lxisefl/gatewayresponses/UNAUTHORIZED" }, "gatewayresponse:put": { "href": "/restapis/o81lxisefl/gatewayresponses/{response_type}", "templated": true }, "gatewayresponse:update": { "href": "/restapis/o81lxisefl/gatewayresponses/UNAUTHORIZED" } }, "defaultResponse": true, "responseParameters": {}, "responseTemplates": { "application/json": "{\"message\":$context.error.messageString}" }, "responseType": "UNAUTHORIZED", "statusCode": "401" }, { "_links": { "self": { "href": "/restapis/o81lxisefl/gatewayresponses/API_CONFIGURATION_ERROR" }, "gatewayresponse:put": { "href": "/restapis/o81lxisefl/gatewayresponses/{response_type}", "templated": true }, "gatewayresponse:update": { "href": "/restapis/o81lxisefl/gatewayresponses/API_CONFIGURATION_ERROR" } }, "defaultResponse": true, "responseParameters": {}, "responseTemplates": { "application/json": "{\"message\":$context.error.messageString}" }, "responseType": "API_CONFIGURATION_ERROR", "statusCode": "500" }, { "_links": { "self": { "href": "/restapis/o81lxisefl/gatewayresponses/QUOTA_EXCEEDED" }, "gatewayresponse:put": { "href": "/restapis/o81lxisefl/gatewayresponses/{response_type}", "templated": true }, "gatewayresponse:update": { "href": "/restapis/o81lxisefl/gatewayresponses/QUOTA_EXCEEDED" } }, "defaultResponse": true, "responseParameters": {}, "responseTemplates": { "application/json": "{\"message\":$context.error.messageString}" }, "responseType": "QUOTA_EXCEEDED", "statusCode": "429" }, { "_links": { "self": { "href": "/restapis/o81lxisefl/gatewayresponses/INTEGRATION_TIMEOUT" }, "gatewayresponse:put": { "href": "/restapis/o81lxisefl/gatewayresponses/{response_type}", "templated": true }, "gatewayresponse:update": { "href": "/restapis/o81lxisefl/gatewayresponses/INTEGRATION_TIMEOUT" } }, "defaultResponse": true, "responseParameters": {}, "responseTemplates": { "application/json": "{\"message\":$context.error.messageString}" }, "responseType": "INTEGRATION_TIMEOUT", "statusCode": "504" }, { "_links": { "self": { "href": "/restapis/o81lxisefl/gatewayresponses/MISSING_AUTHENTICATION_TOKEN" }, "gatewayresponse:put": { "href": "/restapis/o81lxisefl/gatewayresponses/{response_type}", "templated": true }, "gatewayresponse:update": { "href": "/restapis/o81lxisefl/gatewayresponses/MISSING_AUTHENTICATION_TOKEN" } }, "defaultResponse": true, "responseParameters": {}, "responseTemplates": { "application/json": "{\"message\":$context.error.messageString}" }, "responseType": "MISSING_AUTHENTICATION_TOKEN", "statusCode": "403" }, { "_links": { "self": { "href": "/restapis/o81lxisefl/gatewayresponses/INVALID_SIGNATURE" }, "gatewayresponse:put": { "href": "/restapis/o81lxisefl/gatewayresponses/{response_type}", "templated": true }, "gatewayresponse:update": { "href": "/restapis/o81lxisefl/gatewayresponses/INVALID_SIGNATURE" } }, "defaultResponse": true, "responseParameters": {}, "responseTemplates": { "application/json": "{\"message\":$context.error.messageString}" }, "responseType": "INVALID_SIGNATURE", "statusCode": "403" }, { "_links": { "self": { "href": "/restapis/o81lxisefl/gatewayresponses/AUTHORIZER_FAILURE" }, "gatewayresponse:put": { "href": "/restapis/o81lxisefl/gatewayresponses/{response_type}", "templated": true }, "gatewayresponse:update": { "href": "/restapis/o81lxisefl/gatewayresponses/AUTHORIZER_FAILURE" } }, "defaultResponse": true, "responseParameters": {}, "responseTemplates": { "application/json": "{\"message\":$context.error.messageString}" }, "responseType": "AUTHORIZER_FAILURE", "statusCode": "500" } ] } }

    [Customize Gateway
    Responses](http://docs.aws.amazon.com/apigateway/latest/developerguide/customize-
    gateway-responses.html)
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
                "position",
                "position",
                TypeInfo(str),
            ),
            (
                "items",
                "items",
                TypeInfo(typing.List[GatewayResponse]),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )
    position: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Returns the entire collection, because of no pagination support.
    items: typing.List["GatewayResponse"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class GenerateClientCertificateRequest(ShapeBase):
    """
    A request to generate a ClientCertificate resource.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "description",
                "description",
                TypeInfo(str),
            ),
        ]

    # The description of the ClientCertificate.
    description: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class GetAccountRequest(ShapeBase):
    """
    Requests API Gateway to get information about the current Account resource.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class GetApiKeyRequest(ShapeBase):
    """
    A request to get information about the current ApiKey resource.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "api_key",
                "apiKey",
                TypeInfo(str),
            ),
            (
                "include_value",
                "includeValue",
                TypeInfo(bool),
            ),
        ]

    # [Required] The identifier of the ApiKey resource.
    api_key: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A boolean flag to specify whether (`true`) or not (`false`) the result
    # contains the key value.
    include_value: bool = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class GetApiKeysRequest(ShapeBase):
    """
    A request to get information about the current ApiKeys resource.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "position",
                "position",
                TypeInfo(str),
            ),
            (
                "limit",
                "limit",
                TypeInfo(int),
            ),
            (
                "name_query",
                "nameQuery",
                TypeInfo(str),
            ),
            (
                "customer_id",
                "customerId",
                TypeInfo(str),
            ),
            (
                "include_values",
                "includeValues",
                TypeInfo(bool),
            ),
        ]

    # The current pagination position in the paged result set.
    position: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The maximum number of returned results per page. The default value is 25
    # and the maximum value is 500.
    limit: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The name of queried API keys.
    name_query: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The identifier of a customer in AWS Marketplace or an external system, such
    # as a developer portal.
    customer_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A boolean flag to specify whether (`true`) or not (`false`) the result
    # contains key values.
    include_values: bool = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class GetAuthorizerRequest(ShapeBase):
    """
    Request to describe an existing Authorizer resource.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "rest_api_id",
                "restApiId",
                TypeInfo(str),
            ),
            (
                "authorizer_id",
                "authorizerId",
                TypeInfo(str),
            ),
        ]

    # [Required] The string identifier of the associated RestApi.
    rest_api_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # [Required] The identifier of the Authorizer resource.
    authorizer_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class GetAuthorizersRequest(ShapeBase):
    """
    Request to describe an existing Authorizers resource.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "rest_api_id",
                "restApiId",
                TypeInfo(str),
            ),
            (
                "position",
                "position",
                TypeInfo(str),
            ),
            (
                "limit",
                "limit",
                TypeInfo(int),
            ),
        ]

    # [Required] The string identifier of the associated RestApi.
    rest_api_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The current pagination position in the paged result set.
    position: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The maximum number of returned results per page. The default value is 25
    # and the maximum value is 500.
    limit: int = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class GetBasePathMappingRequest(ShapeBase):
    """
    Request to describe a BasePathMapping resource.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "domain_name",
                "domainName",
                TypeInfo(str),
            ),
            (
                "base_path",
                "basePath",
                TypeInfo(str),
            ),
        ]

    # [Required] The domain name of the BasePathMapping resource to be described.
    domain_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # [Required] The base path name that callers of the API must provide as part
    # of the URL after the domain name. This value must be unique for all of the
    # mappings across a single API. Leave this blank if you do not want callers
    # to specify any base path name after the domain name.
    base_path: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class GetBasePathMappingsRequest(ShapeBase):
    """
    A request to get information about a collection of BasePathMapping resources.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "domain_name",
                "domainName",
                TypeInfo(str),
            ),
            (
                "position",
                "position",
                TypeInfo(str),
            ),
            (
                "limit",
                "limit",
                TypeInfo(int),
            ),
        ]

    # [Required] The domain name of a BasePathMapping resource.
    domain_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The current pagination position in the paged result set.
    position: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The maximum number of returned results per page. The default value is 25
    # and the maximum value is 500.
    limit: int = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class GetClientCertificateRequest(ShapeBase):
    """
    A request to get information about the current ClientCertificate resource.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "client_certificate_id",
                "clientCertificateId",
                TypeInfo(str),
            ),
        ]

    # [Required] The identifier of the ClientCertificate resource to be
    # described.
    client_certificate_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class GetClientCertificatesRequest(ShapeBase):
    """
    A request to get information about a collection of ClientCertificate resources.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "position",
                "position",
                TypeInfo(str),
            ),
            (
                "limit",
                "limit",
                TypeInfo(int),
            ),
        ]

    # The current pagination position in the paged result set.
    position: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The maximum number of returned results per page. The default value is 25
    # and the maximum value is 500.
    limit: int = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class GetDeploymentRequest(ShapeBase):
    """
    Requests API Gateway to get information about a Deployment resource.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "rest_api_id",
                "restApiId",
                TypeInfo(str),
            ),
            (
                "deployment_id",
                "deploymentId",
                TypeInfo(str),
            ),
            (
                "embed",
                "embed",
                TypeInfo(typing.List[str]),
            ),
        ]

    # [Required] The string identifier of the associated RestApi.
    rest_api_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # [Required] The identifier of the Deployment resource to get information
    # about.
    deployment_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A query parameter to retrieve the specified embedded resources of the
    # returned Deployment resource in the response. In a REST API call, this
    # `embed` parameter value is a list of comma-separated strings, as in `GET
    # /restapis/{restapi_id}/deployments/{deployment_id}?embed=var1,var2`. The
    # SDK and other platform-dependent libraries might use a different format for
    # the list. Currently, this request supports only retrieval of the embedded
    # API summary this way. Hence, the parameter value must be a single-valued
    # list containing only the `"apisummary"` string. For example, `GET
    # /restapis/{restapi_id}/deployments/{deployment_id}?embed=apisummary`.
    embed: typing.List[str] = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class GetDeploymentsRequest(ShapeBase):
    """
    Requests API Gateway to get information about a Deployments collection.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "rest_api_id",
                "restApiId",
                TypeInfo(str),
            ),
            (
                "position",
                "position",
                TypeInfo(str),
            ),
            (
                "limit",
                "limit",
                TypeInfo(int),
            ),
        ]

    # [Required] The string identifier of the associated RestApi.
    rest_api_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The current pagination position in the paged result set.
    position: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The maximum number of returned results per page. The default value is 25
    # and the maximum value is 500.
    limit: int = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class GetDocumentationPartRequest(ShapeBase):
    """
    Gets a specified documentation part of a given API.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "rest_api_id",
                "restApiId",
                TypeInfo(str),
            ),
            (
                "documentation_part_id",
                "documentationPartId",
                TypeInfo(str),
            ),
        ]

    # [Required] The string identifier of the associated RestApi.
    rest_api_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # [Required] The string identifier of the associated RestApi.
    documentation_part_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class GetDocumentationPartsRequest(ShapeBase):
    """
    Gets the documentation parts of an API. The result may be filtered by the type,
    name, or path of API entities (targets).
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "rest_api_id",
                "restApiId",
                TypeInfo(str),
            ),
            (
                "type",
                "type",
                TypeInfo(typing.Union[str, DocumentationPartType]),
            ),
            (
                "name_query",
                "nameQuery",
                TypeInfo(str),
            ),
            (
                "path",
                "path",
                TypeInfo(str),
            ),
            (
                "position",
                "position",
                TypeInfo(str),
            ),
            (
                "limit",
                "limit",
                TypeInfo(int),
            ),
            (
                "location_status",
                "locationStatus",
                TypeInfo(typing.Union[str, LocationStatusType]),
            ),
        ]

    # [Required] The string identifier of the associated RestApi.
    rest_api_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The type of API entities of the to-be-retrieved documentation parts.
    type: typing.Union[str, "DocumentationPartType"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The name of API entities of the to-be-retrieved documentation parts.
    name_query: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The path of API entities of the to-be-retrieved documentation parts.
    path: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The current pagination position in the paged result set.
    position: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The maximum number of returned results per page. The default value is 25
    # and the maximum value is 500.
    limit: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The status of the API documentation parts to retrieve. Valid values are
    # `DOCUMENTED` for retrieving DocumentationPart resources with content and
    # `UNDOCUMENTED` for DocumentationPart resources without content.
    location_status: typing.Union[str, "LocationStatusType"
                                 ] = dataclasses.field(
                                     default=ShapeBase.NOT_SET,
                                 )


@dataclasses.dataclass
class GetDocumentationVersionRequest(ShapeBase):
    """
    Gets a documentation snapshot of an API.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "rest_api_id",
                "restApiId",
                TypeInfo(str),
            ),
            (
                "documentation_version",
                "documentationVersion",
                TypeInfo(str),
            ),
        ]

    # [Required] The string identifier of the associated RestApi.
    rest_api_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # [Required] The version identifier of the to-be-retrieved documentation
    # snapshot.
    documentation_version: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class GetDocumentationVersionsRequest(ShapeBase):
    """
    Gets the documentation versions of an API.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "rest_api_id",
                "restApiId",
                TypeInfo(str),
            ),
            (
                "position",
                "position",
                TypeInfo(str),
            ),
            (
                "limit",
                "limit",
                TypeInfo(int),
            ),
        ]

    # [Required] The string identifier of the associated RestApi.
    rest_api_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The current pagination position in the paged result set.
    position: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The maximum number of returned results per page. The default value is 25
    # and the maximum value is 500.
    limit: int = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class GetDomainNameRequest(ShapeBase):
    """
    Request to get the name of a DomainName resource.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "domain_name",
                "domainName",
                TypeInfo(str),
            ),
        ]

    # [Required] The name of the DomainName resource.
    domain_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class GetDomainNamesRequest(ShapeBase):
    """
    Request to describe a collection of DomainName resources.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "position",
                "position",
                TypeInfo(str),
            ),
            (
                "limit",
                "limit",
                TypeInfo(int),
            ),
        ]

    # The current pagination position in the paged result set.
    position: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The maximum number of returned results per page. The default value is 25
    # and the maximum value is 500.
    limit: int = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class GetExportRequest(ShapeBase):
    """
    Request a new export of a RestApi for a particular Stage.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "rest_api_id",
                "restApiId",
                TypeInfo(str),
            ),
            (
                "stage_name",
                "stageName",
                TypeInfo(str),
            ),
            (
                "export_type",
                "exportType",
                TypeInfo(str),
            ),
            (
                "parameters",
                "parameters",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "accepts",
                "accepts",
                TypeInfo(str),
            ),
        ]

    # [Required] The string identifier of the associated RestApi.
    rest_api_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # [Required] The name of the Stage that will be exported.
    stage_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # [Required] The type of export. Currently only 'swagger' is supported.
    export_type: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A key-value map of query string parameters that specify properties of the
    # export, depending on the requested `exportType`. For `exportType`
    # `swagger`, any combination of the following parameters are supported:
    # `extensions='integrations'` or `extensions='apigateway'` will export the
    # API with x-amazon-apigateway-integration extensions.
    # `extensions='authorizers'` will export the API with x-amazon-apigateway-
    # authorizer extensions. `postman` will export the API with Postman
    # extensions, allowing for import to the Postman tool
    parameters: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The content-type of the export, for example `application/json`. Currently
    # `application/json` and `application/yaml` are supported for `exportType` of
    # `swagger`. This should be specified in the `Accept` header for direct API
    # requests.
    accepts: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class GetGatewayResponseRequest(ShapeBase):
    """
    Gets a GatewayResponse of a specified response type on the given RestApi.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "rest_api_id",
                "restApiId",
                TypeInfo(str),
            ),
            (
                "response_type",
                "responseType",
                TypeInfo(typing.Union[str, GatewayResponseType]),
            ),
        ]

    # [Required] The string identifier of the associated RestApi.
    rest_api_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # [Required]

    # The response type of the associated GatewayResponse. Valid values are

    #   * ACCESS_DENIED
    #   * API_CONFIGURATION_ERROR
    #   * AUTHORIZER_FAILURE
    #   * AUTHORIZER_CONFIGURATION_ERROR
    #   * BAD_REQUEST_PARAMETERS
    #   * BAD_REQUEST_BODY
    #   * DEFAULT_4XX
    #   * DEFAULT_5XX
    #   * EXPIRED_TOKEN
    #   * INVALID_SIGNATURE
    #   * INTEGRATION_FAILURE
    #   * INTEGRATION_TIMEOUT
    #   * INVALID_API_KEY
    #   * MISSING_AUTHENTICATION_TOKEN
    #   * QUOTA_EXCEEDED
    #   * REQUEST_TOO_LARGE
    #   * RESOURCE_NOT_FOUND
    #   * THROTTLED
    #   * UNAUTHORIZED
    #   * UNSUPPORTED_MEDIA_TYPE
    response_type: typing.Union[str, "GatewayResponseType"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class GetGatewayResponsesRequest(ShapeBase):
    """
    Gets the GatewayResponses collection on the given RestApi. If an API developer
    has not added any definitions for gateway responses, the result will be the API
    Gateway-generated default GatewayResponses collection for the supported response
    types.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "rest_api_id",
                "restApiId",
                TypeInfo(str),
            ),
            (
                "position",
                "position",
                TypeInfo(str),
            ),
            (
                "limit",
                "limit",
                TypeInfo(int),
            ),
        ]

    # [Required] The string identifier of the associated RestApi.
    rest_api_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The current pagination position in the paged result set. The
    # GatewayResponse collection does not support pagination and the position
    # does not apply here.
    position: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The maximum number of returned results per page. The default value is 25
    # and the maximum value is 500. The GatewayResponses collection does not
    # support pagination and the limit does not apply here.
    limit: int = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class GetIntegrationRequest(ShapeBase):
    """
    Represents a request to get the integration configuration.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "rest_api_id",
                "restApiId",
                TypeInfo(str),
            ),
            (
                "resource_id",
                "resourceId",
                TypeInfo(str),
            ),
            (
                "http_method",
                "httpMethod",
                TypeInfo(str),
            ),
        ]

    # [Required] The string identifier of the associated RestApi.
    rest_api_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # [Required] Specifies a get integration request's resource identifier
    resource_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # [Required] Specifies a get integration request's HTTP method.
    http_method: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class GetIntegrationResponseRequest(ShapeBase):
    """
    Represents a get integration response request.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "rest_api_id",
                "restApiId",
                TypeInfo(str),
            ),
            (
                "resource_id",
                "resourceId",
                TypeInfo(str),
            ),
            (
                "http_method",
                "httpMethod",
                TypeInfo(str),
            ),
            (
                "status_code",
                "statusCode",
                TypeInfo(str),
            ),
        ]

    # [Required] The string identifier of the associated RestApi.
    rest_api_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # [Required] Specifies a get integration response request's resource
    # identifier.
    resource_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # [Required] Specifies a get integration response request's HTTP method.
    http_method: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # [Required] Specifies a get integration response request's status code.
    status_code: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class GetMethodRequest(ShapeBase):
    """
    Request to describe an existing Method resource.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "rest_api_id",
                "restApiId",
                TypeInfo(str),
            ),
            (
                "resource_id",
                "resourceId",
                TypeInfo(str),
            ),
            (
                "http_method",
                "httpMethod",
                TypeInfo(str),
            ),
        ]

    # [Required] The string identifier of the associated RestApi.
    rest_api_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # [Required] The Resource identifier for the Method resource.
    resource_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # [Required] Specifies the method request's HTTP method type.
    http_method: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class GetMethodResponseRequest(ShapeBase):
    """
    Request to describe a MethodResponse resource.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "rest_api_id",
                "restApiId",
                TypeInfo(str),
            ),
            (
                "resource_id",
                "resourceId",
                TypeInfo(str),
            ),
            (
                "http_method",
                "httpMethod",
                TypeInfo(str),
            ),
            (
                "status_code",
                "statusCode",
                TypeInfo(str),
            ),
        ]

    # [Required] The string identifier of the associated RestApi.
    rest_api_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # [Required] The Resource identifier for the MethodResponse resource.
    resource_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # [Required] The HTTP verb of the Method resource.
    http_method: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # [Required] The status code for the MethodResponse resource.
    status_code: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class GetModelRequest(ShapeBase):
    """
    Request to list information about a model in an existing RestApi resource.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "rest_api_id",
                "restApiId",
                TypeInfo(str),
            ),
            (
                "model_name",
                "modelName",
                TypeInfo(str),
            ),
            (
                "flatten",
                "flatten",
                TypeInfo(bool),
            ),
        ]

    # [Required] The RestApi identifier under which the Model exists.
    rest_api_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # [Required] The name of the model as an identifier.
    model_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A query parameter of a Boolean value to resolve (`true`) all external model
    # references and returns a flattened model schema or not (`false`) The
    # default is `false`.
    flatten: bool = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class GetModelTemplateRequest(ShapeBase):
    """
    Request to generate a sample mapping template used to transform the payload.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "rest_api_id",
                "restApiId",
                TypeInfo(str),
            ),
            (
                "model_name",
                "modelName",
                TypeInfo(str),
            ),
        ]

    # [Required] The string identifier of the associated RestApi.
    rest_api_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # [Required] The name of the model for which to generate a template.
    model_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class GetModelsRequest(ShapeBase):
    """
    Request to list existing Models defined for a RestApi resource.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "rest_api_id",
                "restApiId",
                TypeInfo(str),
            ),
            (
                "position",
                "position",
                TypeInfo(str),
            ),
            (
                "limit",
                "limit",
                TypeInfo(int),
            ),
        ]

    # [Required] The string identifier of the associated RestApi.
    rest_api_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The current pagination position in the paged result set.
    position: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The maximum number of returned results per page. The default value is 25
    # and the maximum value is 500.
    limit: int = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class GetRequestValidatorRequest(ShapeBase):
    """
    Gets a RequestValidator of a given RestApi.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "rest_api_id",
                "restApiId",
                TypeInfo(str),
            ),
            (
                "request_validator_id",
                "requestValidatorId",
                TypeInfo(str),
            ),
        ]

    # [Required] The string identifier of the associated RestApi.
    rest_api_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # [Required] The identifier of the RequestValidator to be retrieved.
    request_validator_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class GetRequestValidatorsRequest(ShapeBase):
    """
    Gets the RequestValidators collection of a given RestApi.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "rest_api_id",
                "restApiId",
                TypeInfo(str),
            ),
            (
                "position",
                "position",
                TypeInfo(str),
            ),
            (
                "limit",
                "limit",
                TypeInfo(int),
            ),
        ]

    # [Required] The string identifier of the associated RestApi.
    rest_api_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The current pagination position in the paged result set.
    position: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The maximum number of returned results per page. The default value is 25
    # and the maximum value is 500.
    limit: int = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class GetResourceRequest(ShapeBase):
    """
    Request to list information about a resource.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "rest_api_id",
                "restApiId",
                TypeInfo(str),
            ),
            (
                "resource_id",
                "resourceId",
                TypeInfo(str),
            ),
            (
                "embed",
                "embed",
                TypeInfo(typing.List[str]),
            ),
        ]

    # [Required] The string identifier of the associated RestApi.
    rest_api_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # [Required] The identifier for the Resource resource.
    resource_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A query parameter to retrieve the specified resources embedded in the
    # returned Resource representation in the response. This `embed` parameter
    # value is a list of comma-separated strings. Currently, the request supports
    # only retrieval of the embedded Method resources this way. The query
    # parameter value must be a single-valued list and contain the `"methods"`
    # string. For example, `GET
    # /restapis/{restapi_id}/resources/{resource_id}?embed=methods`.
    embed: typing.List[str] = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class GetResourcesRequest(ShapeBase):
    """
    Request to list information about a collection of resources.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "rest_api_id",
                "restApiId",
                TypeInfo(str),
            ),
            (
                "position",
                "position",
                TypeInfo(str),
            ),
            (
                "limit",
                "limit",
                TypeInfo(int),
            ),
            (
                "embed",
                "embed",
                TypeInfo(typing.List[str]),
            ),
        ]

    # [Required] The string identifier of the associated RestApi.
    rest_api_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The current pagination position in the paged result set.
    position: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The maximum number of returned results per page. The default value is 25
    # and the maximum value is 500.
    limit: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A query parameter used to retrieve the specified resources embedded in the
    # returned Resources resource in the response. This `embed` parameter value
    # is a list of comma-separated strings. Currently, the request supports only
    # retrieval of the embedded Method resources this way. The query parameter
    # value must be a single-valued list and contain the `"methods"` string. For
    # example, `GET /restapis/{restapi_id}/resources?embed=methods`.
    embed: typing.List[str] = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class GetRestApiRequest(ShapeBase):
    """
    The GET request to list an existing RestApi defined for your collection.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "rest_api_id",
                "restApiId",
                TypeInfo(str),
            ),
        ]

    # [Required] The string identifier of the associated RestApi.
    rest_api_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class GetRestApisRequest(ShapeBase):
    """
    The GET request to list existing RestApis defined for your collection.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "position",
                "position",
                TypeInfo(str),
            ),
            (
                "limit",
                "limit",
                TypeInfo(int),
            ),
        ]

    # The current pagination position in the paged result set.
    position: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The maximum number of returned results per page. The default value is 25
    # and the maximum value is 500.
    limit: int = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class GetSdkRequest(ShapeBase):
    """
    Request a new generated client SDK for a RestApi and Stage.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "rest_api_id",
                "restApiId",
                TypeInfo(str),
            ),
            (
                "stage_name",
                "stageName",
                TypeInfo(str),
            ),
            (
                "sdk_type",
                "sdkType",
                TypeInfo(str),
            ),
            (
                "parameters",
                "parameters",
                TypeInfo(typing.Dict[str, str]),
            ),
        ]

    # [Required] The string identifier of the associated RestApi.
    rest_api_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # [Required] The name of the Stage that the SDK will use.
    stage_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # [Required] The language for the generated SDK. Currently `java`,
    # `javascript`, `android`, `objectivec` (for iOS), `swift` (for iOS), and
    # `ruby` are supported.
    sdk_type: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A string-to-string key-value map of query parameters `sdkType`-dependent
    # properties of the SDK. For `sdkType` of `objectivec` or `swift`, a
    # parameter named `classPrefix` is required. For `sdkType` of `android`,
    # parameters named `groupId`, `artifactId`, `artifactVersion`, and
    # `invokerPackage` are required. For `sdkType` of `java`, parameters named
    # `serviceName` and `javaPackageName` are required.
    parameters: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class GetSdkTypeRequest(ShapeBase):
    """
    Get an SdkType instance.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "id",
                "id",
                TypeInfo(str),
            ),
        ]

    # [Required] The identifier of the queried SdkType instance.
    id: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class GetSdkTypesRequest(ShapeBase):
    """
    Get the SdkTypes collection.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "position",
                "position",
                TypeInfo(str),
            ),
            (
                "limit",
                "limit",
                TypeInfo(int),
            ),
        ]

    # The current pagination position in the paged result set.
    position: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The maximum number of returned results per page. The default value is 25
    # and the maximum value is 500.
    limit: int = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class GetStageRequest(ShapeBase):
    """
    Requests API Gateway to get information about a Stage resource.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "rest_api_id",
                "restApiId",
                TypeInfo(str),
            ),
            (
                "stage_name",
                "stageName",
                TypeInfo(str),
            ),
        ]

    # [Required] The string identifier of the associated RestApi.
    rest_api_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # [Required] The name of the Stage resource to get information about.
    stage_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class GetStagesRequest(ShapeBase):
    """
    Requests API Gateway to get information about one or more Stage resources.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "rest_api_id",
                "restApiId",
                TypeInfo(str),
            ),
            (
                "deployment_id",
                "deploymentId",
                TypeInfo(str),
            ),
        ]

    # [Required] The string identifier of the associated RestApi.
    rest_api_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The stages' deployment identifiers.
    deployment_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class GetTagsRequest(ShapeBase):
    """
    Gets the Tags collection for a given resource.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "resource_arn",
                "resourceArn",
                TypeInfo(str),
            ),
            (
                "position",
                "position",
                TypeInfo(str),
            ),
            (
                "limit",
                "limit",
                TypeInfo(int),
            ),
        ]

    # [Required] The ARN of a resource that can be tagged. The resource ARN must
    # be URL-encoded. At present, Stage is the only taggable resource.
    resource_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # (Not currently supported) The current pagination position in the paged
    # result set.
    position: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # (Not currently supported) The maximum number of returned results per page.
    # The default value is 25 and the maximum value is 500.
    limit: int = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class GetUsagePlanKeyRequest(ShapeBase):
    """
    The GET request to get a usage plan key of a given key identifier.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "usage_plan_id",
                "usagePlanId",
                TypeInfo(str),
            ),
            (
                "key_id",
                "keyId",
                TypeInfo(str),
            ),
        ]

    # [Required] The Id of the UsagePlan resource representing the usage plan
    # containing the to-be-retrieved UsagePlanKey resource representing a plan
    # customer.
    usage_plan_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # [Required] The key Id of the to-be-retrieved UsagePlanKey resource
    # representing a plan customer.
    key_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class GetUsagePlanKeysRequest(ShapeBase):
    """
    The GET request to get all the usage plan keys representing the API keys added
    to a specified usage plan.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "usage_plan_id",
                "usagePlanId",
                TypeInfo(str),
            ),
            (
                "position",
                "position",
                TypeInfo(str),
            ),
            (
                "limit",
                "limit",
                TypeInfo(int),
            ),
            (
                "name_query",
                "nameQuery",
                TypeInfo(str),
            ),
        ]

    # [Required] The Id of the UsagePlan resource representing the usage plan
    # containing the to-be-retrieved UsagePlanKey resource representing a plan
    # customer.
    usage_plan_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The current pagination position in the paged result set.
    position: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The maximum number of returned results per page. The default value is 25
    # and the maximum value is 500.
    limit: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A query parameter specifying the name of the to-be-returned usage plan
    # keys.
    name_query: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class GetUsagePlanRequest(ShapeBase):
    """
    The GET request to get a usage plan of a given plan identifier.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "usage_plan_id",
                "usagePlanId",
                TypeInfo(str),
            ),
        ]

    # [Required] The identifier of the UsagePlan resource to be retrieved.
    usage_plan_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class GetUsagePlansRequest(ShapeBase):
    """
    The GET request to get all the usage plans of the caller's account.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "position",
                "position",
                TypeInfo(str),
            ),
            (
                "key_id",
                "keyId",
                TypeInfo(str),
            ),
            (
                "limit",
                "limit",
                TypeInfo(int),
            ),
        ]

    # The current pagination position in the paged result set.
    position: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The identifier of the API key associated with the usage plans.
    key_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The maximum number of returned results per page. The default value is 25
    # and the maximum value is 500.
    limit: int = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class GetUsageRequest(ShapeBase):
    """
    The GET request to get the usage data of a usage plan in a specified time
    interval.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "usage_plan_id",
                "usagePlanId",
                TypeInfo(str),
            ),
            (
                "start_date",
                "startDate",
                TypeInfo(str),
            ),
            (
                "end_date",
                "endDate",
                TypeInfo(str),
            ),
            (
                "key_id",
                "keyId",
                TypeInfo(str),
            ),
            (
                "position",
                "position",
                TypeInfo(str),
            ),
            (
                "limit",
                "limit",
                TypeInfo(int),
            ),
        ]

    # [Required] The Id of the usage plan associated with the usage data.
    usage_plan_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # [Required] The starting date (e.g., 2016-01-01) of the usage data.
    start_date: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # [Required] The ending date (e.g., 2016-12-31) of the usage data.
    end_date: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The Id of the API key associated with the resultant usage data.
    key_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The current pagination position in the paged result set.
    position: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The maximum number of returned results per page. The default value is 25
    # and the maximum value is 500.
    limit: int = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class GetVpcLinkRequest(ShapeBase):
    """
    Gets a specified VPC link under the caller's account in a region.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "vpc_link_id",
                "vpcLinkId",
                TypeInfo(str),
            ),
        ]

    # [Required] The identifier of the VpcLink. It is used in an Integration to
    # reference this VpcLink.
    vpc_link_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class GetVpcLinksRequest(ShapeBase):
    """
    Gets the VpcLinks collection under the caller's account in a selected region.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "position",
                "position",
                TypeInfo(str),
            ),
            (
                "limit",
                "limit",
                TypeInfo(int),
            ),
        ]

    # The current pagination position in the paged result set.
    position: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The maximum number of returned results per page. The default value is 25
    # and the maximum value is 500.
    limit: int = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ImportApiKeysRequest(ShapeBase):
    """
    The POST request to import API keys from an external source, such as a CSV-
    formatted file.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "body",
                "body",
                TypeInfo(typing.Any),
            ),
            (
                "format",
                "format",
                TypeInfo(typing.Union[str, ApiKeysFormat]),
            ),
            (
                "fail_on_warnings",
                "failOnWarnings",
                TypeInfo(bool),
            ),
        ]

    # The payload of the POST request to import API keys. For the payload format,
    # see [API Key File
    # Format](http://docs.aws.amazon.com/apigateway/latest/developerguide/api-
    # key-file-format.html).
    body: typing.Any = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A query parameter to specify the input format to imported API keys.
    # Currently, only the `csv` format is supported.
    format: typing.Union[str, "ApiKeysFormat"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A query parameter to indicate whether to rollback ApiKey importation
    # (`true`) or not (`false`) when error is encountered.
    fail_on_warnings: bool = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ImportDocumentationPartsRequest(ShapeBase):
    """
    Import documentation parts from an external (e.g., Swagger) definition file.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "rest_api_id",
                "restApiId",
                TypeInfo(str),
            ),
            (
                "body",
                "body",
                TypeInfo(typing.Any),
            ),
            (
                "mode",
                "mode",
                TypeInfo(typing.Union[str, PutMode]),
            ),
            (
                "fail_on_warnings",
                "failOnWarnings",
                TypeInfo(bool),
            ),
        ]

    # [Required] The string identifier of the associated RestApi.
    rest_api_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # [Required] Raw byte array representing the to-be-imported documentation
    # parts. To import from a Swagger file, this is a JSON object.
    body: typing.Any = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A query parameter to indicate whether to overwrite (`OVERWRITE`) any
    # existing DocumentationParts definition or to merge (`MERGE`) the new
    # definition into the existing one. The default value is `MERGE`.
    mode: typing.Union[str, "PutMode"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A query parameter to specify whether to rollback the documentation
    # importation (`true`) or not (`false`) when a warning is encountered. The
    # default value is `false`.
    fail_on_warnings: bool = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ImportRestApiRequest(ShapeBase):
    """
    A POST request to import an API to API Gateway using an input of an API
    definition file.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "body",
                "body",
                TypeInfo(typing.Any),
            ),
            (
                "fail_on_warnings",
                "failOnWarnings",
                TypeInfo(bool),
            ),
            (
                "parameters",
                "parameters",
                TypeInfo(typing.Dict[str, str]),
            ),
        ]

    # [Required] The POST request body containing external API definitions.
    # Currently, only Swagger definition JSON files are supported. The maximum
    # size of the API definition file is 2MB.
    body: typing.Any = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A query parameter to indicate whether to rollback the API creation (`true`)
    # or not (`false`) when a warning is encountered. The default value is
    # `false`.
    fail_on_warnings: bool = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A key-value map of context-specific query string parameters specifying the
    # behavior of different API importing operations. The following shows
    # operation-specific parameters and their supported values.

    # To exclude DocumentationParts from the import, set `parameters` as
    # `ignore=documentation`.

    # To configure the endpoint type, set `parameters` as
    # `endpointConfigurationTypes=EDGE`, `endpointConfigurationTypes=REGIONAL`,
    # or `endpointConfigurationTypes=PRIVATE`. The default endpoint type is
    # `EDGE`.

    # To handle imported `basePath`, set `parameters` as `basePath=ignore`,
    # `basePath=prepend` or `basePath=split`.

    # For example, the AWS CLI command to exclude documentation from the imported
    # API is:

    #     aws apigateway import-rest-api --parameters ignore=documentation --body 'file:///path/to/imported-api-body.json'

    # The AWS CLI command to set the regional endpoint on the imported API is:

    #     aws apigateway import-rest-api --parameters endpointConfigurationTypes=REGIONAL --body 'file:///path/to/imported-api-body.json'
    parameters: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class Integration(OutputShapeBase):
    """
    Represents an HTTP, HTTP_PROXY, AWS, AWS_PROXY, or Mock integration.

    In the API Gateway console, the built-in Lambda integration is an AWS
    integration.

    [Creating an
    API](http://docs.aws.amazon.com/apigateway/latest/developerguide/how-to-create-
    api.html)
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
                "type",
                "type",
                TypeInfo(typing.Union[str, IntegrationType]),
            ),
            (
                "http_method",
                "httpMethod",
                TypeInfo(str),
            ),
            (
                "uri",
                "uri",
                TypeInfo(str),
            ),
            (
                "connection_type",
                "connectionType",
                TypeInfo(typing.Union[str, ConnectionType]),
            ),
            (
                "connection_id",
                "connectionId",
                TypeInfo(str),
            ),
            (
                "credentials",
                "credentials",
                TypeInfo(str),
            ),
            (
                "request_parameters",
                "requestParameters",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "request_templates",
                "requestTemplates",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "passthrough_behavior",
                "passthroughBehavior",
                TypeInfo(str),
            ),
            (
                "content_handling",
                "contentHandling",
                TypeInfo(typing.Union[str, ContentHandlingStrategy]),
            ),
            (
                "timeout_in_millis",
                "timeoutInMillis",
                TypeInfo(int),
            ),
            (
                "cache_namespace",
                "cacheNamespace",
                TypeInfo(str),
            ),
            (
                "cache_key_parameters",
                "cacheKeyParameters",
                TypeInfo(typing.List[str]),
            ),
            (
                "integration_responses",
                "integrationResponses",
                TypeInfo(typing.Dict[str, IntegrationResponse]),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Specifies an API method integration type. The valid value is one of the
    # following:

    #   * `AWS`: for integrating the API method request with an AWS service action, including the Lambda function-invoking action. With the Lambda function-invoking action, this is referred to as the Lambda custom integration. With any other AWS service action, this is known as AWS integration.
    #   * `AWS_PROXY`: for integrating the API method request with the Lambda function-invoking action with the client request passed through as-is. This integration is also referred to as the Lambda proxy integration.
    #   * `HTTP`: for integrating the API method request with an HTTP endpoint, including a private HTTP endpoint within a VPC. This integration is also referred to as the HTTP custom integration.
    #   * `HTTP_PROXY`: for integrating the API method request with an HTTP endpoint, including a private HTTP endpoint within a VPC, with the client request passed through as-is. This is also referred to as the HTTP proxy integration.
    #   * `MOCK`: for integrating the API method request with API Gateway as a "loop-back" endpoint without invoking any backend.

    # For the HTTP and HTTP proxy integrations, each integration can specify a
    # protocol (`http/https`), port and path. Standard 80 and 443 ports are
    # supported as well as custom ports above 1024. An HTTP or HTTP proxy
    # integration with a `connectionType` of `VPC_LINK` is referred to as a
    # private integration and uses a VpcLink to connect API Gateway to a network
    # load balancer of a VPC.
    type: typing.Union[str, "IntegrationType"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Specifies the integration's HTTP method type.
    http_method: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Specifies Uniform Resource Identifier (URI) of the integration endpoint.

    #   * For `HTTP` or `HTTP_PROXY` integrations, the URI must be a fully formed, encoded HTTP(S) URL according to the [RFC-3986 specification](https://en.wikipedia.org/wiki/Uniform_Resource_Identifier), for either standard integration, where `connectionType` is not `VPC_LINK`, or private integration, where `connectionType` is `VPC_LINK`. For a private HTTP integration, the URI is not used for routing.

    #   * For `AWS` or `AWS_PROXY` integrations, the URI is of the form `arn:aws:apigateway:{region}:{subdomain.service|service}:path|action/{service_api}`. Here, `{Region}` is the API Gateway region (e.g., `us-east-1`); `{service}` is the name of the integrated AWS service (e.g., `s3`); and `{subdomain}` is a designated subdomain supported by certain AWS service for fast host-name lookup. `action` can be used for an AWS service action-based API, using an `Action={name}&{p1}={v1}&p2={v2}...` query string. The ensuing `{service_api}` refers to a supported action `{name}` plus any required input parameters. Alternatively, `path` can be used for an AWS service path-based API. The ensuing `service_api` refers to the path to an AWS service resource, including the region of the integrated AWS service, if applicable. For example, for integration with the S3 API of `[GetObject](http://docs.aws.amazon.com/AmazonS3/latest/API/RESTObjectGET.html)`, the `uri` can be either `arn:aws:apigateway:us-west-2:s3:action/GetObject&Bucket={bucket}&Key={key}` or `arn:aws:apigateway:us-west-2:s3:path/{bucket}/{key}`
    uri: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The type of the network connection to the integration endpoint. The valid
    # value is `INTERNET` for connections through the public routable internet or
    # `VPC_LINK` for private connections between API Gateway and a network load
    # balancer in a VPC. The default value is `INTERNET`.
    connection_type: typing.Union[str, "ConnectionType"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The ([`id`](http://docs.aws.amazon.com/apigateway/api-
    # reference/resource/vpc-link/#id)) of the VpcLink used for the integration
    # when `connectionType=VPC_LINK` and undefined, otherwise.
    connection_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Specifies the credentials required for the integration, if any. For AWS
    # integrations, three options are available. To specify an IAM Role for API
    # Gateway to assume, use the role's Amazon Resource Name (ARN). To require
    # that the caller's identity be passed through from the request, specify the
    # string `arn:aws:iam::\*:user/\*`. To use resource-based permissions on
    # supported AWS services, specify null.
    credentials: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A key-value map specifying request parameters that are passed from the
    # method request to the back end. The key is an integration request parameter
    # name and the associated value is a method request parameter value or static
    # value that must be enclosed within single quotes and pre-encoded as
    # required by the back end. The method request parameter value must match the
    # pattern of `method.request.{location}.{name}`, where `location` is
    # `querystring`, `path`, or `header` and `name` must be a valid and unique
    # method request parameter name.
    request_parameters: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Represents a map of Velocity templates that are applied on the request
    # payload based on the value of the Content-Type header sent by the client.
    # The content type value is the key in this map, and the template (as a
    # String) is the value.
    request_templates: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Specifies how the method request body of an unmapped content type will be
    # passed through the integration request to the back end without
    # transformation. A content type is unmapped if no mapping template is
    # defined in the integration or the content type does not match any of the
    # mapped content types, as specified in `requestTemplates`. The valid value
    # is one of the following:

    #   * `WHEN_NO_MATCH`: passes the method request body through the integration request to the back end without transformation when the method request content type does not match any content type associated with the mapping templates defined in the integration request.
    #   * `WHEN_NO_TEMPLATES`: passes the method request body through the integration request to the back end without transformation when no mapping template is defined in the integration request. If a template is defined when this option is selected, the method request of an unmapped content-type will be rejected with an HTTP `415 Unsupported Media Type` response.
    #   * `NEVER`: rejects the method request with an HTTP `415 Unsupported Media Type` response when either the method request content type does not match any content type associated with the mapping templates defined in the integration request or no mapping template is defined in the integration request.
    passthrough_behavior: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Specifies how to handle request payload content type conversions. Supported
    # values are `CONVERT_TO_BINARY` and `CONVERT_TO_TEXT`, with the following
    # behaviors:

    #   * `CONVERT_TO_BINARY`: Converts a request payload from a Base64-encoded string to the corresponding binary blob.

    #   * `CONVERT_TO_TEXT`: Converts a request payload from a binary blob to a Base64-encoded string.

    # If this property is not defined, the request payload will be passed through
    # from the method request to integration request without modification,
    # provided that the `passthroughBehaviors` is configured to support payload
    # pass-through.
    content_handling: typing.Union[str, "ContentHandlingStrategy"
                                  ] = dataclasses.field(
                                      default=ShapeBase.NOT_SET,
                                  )

    # Custom timeout between 50 and 29,000 milliseconds. The default value is
    # 29,000 milliseconds or 29 seconds.
    timeout_in_millis: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Specifies the integration's cache namespace.
    cache_namespace: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Specifies the integration's cache key parameters.
    cache_key_parameters: typing.List[str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Specifies the integration's responses.

    # #### Example: Get integration responses of a method

    # ##### Request

    #     GET /restapis/fugvjdxtri/resources/3kzxbg5sa2/methods/GET/integration/responses/200 HTTP/1.1 Content-Type: application/json Host: apigateway.us-east-1.amazonaws.com X-Amz-Date: 20160607T191449Z Authorization: AWS4-HMAC-SHA256 Credential={access_key_ID}/20160607/us-east-1/apigateway/aws4_request, SignedHeaders=content-type;host;x-amz-date, Signature={sig4_hash}

    # ##### Response

    # The successful response returns `200 OK` status and a payload as follows:

    #     { "_links": { "curies": { "href": "http://docs.aws.amazon.com/apigateway/latest/developerguide/restapi-integration-response-{rel}.html", "name": "integrationresponse", "templated": true }, "self": { "href": "/restapis/fugvjdxtri/resources/3kzxbg5sa2/methods/GET/integration/responses/200", "title": "200" }, "integrationresponse:delete": { "href": "/restapis/fugvjdxtri/resources/3kzxbg5sa2/methods/GET/integration/responses/200" }, "integrationresponse:update": { "href": "/restapis/fugvjdxtri/resources/3kzxbg5sa2/methods/GET/integration/responses/200" } }, "responseParameters": { "method.response.header.Content-Type": "'application/xml'" }, "responseTemplates": { "application/json": "$util.urlDecode(\"%3CkinesisStreams%3E#foreach($stream in $input.path('$.StreamNames'))%3Cstream%3E%3Cname%3E$stream%3C/name%3E%3C/stream%3E#end%3C/kinesisStreams%3E\")\n" }, "statusCode": "200" }

    # [Creating an
    # API](http://docs.aws.amazon.com/apigateway/latest/developerguide/how-to-
    # create-api.html)
    integration_responses: typing.Dict[str, "IntegrationResponse"
                                      ] = dataclasses.field(
                                          default=ShapeBase.NOT_SET,
                                      )


@dataclasses.dataclass
class IntegrationResponse(OutputShapeBase):
    """
    Represents an integration response. The status code must map to an existing
    MethodResponse, and parameters and templates can be used to transform the back-
    end response.

    [Creating an
    API](http://docs.aws.amazon.com/apigateway/latest/developerguide/how-to-create-
    api.html)
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
                "status_code",
                "statusCode",
                TypeInfo(str),
            ),
            (
                "selection_pattern",
                "selectionPattern",
                TypeInfo(str),
            ),
            (
                "response_parameters",
                "responseParameters",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "response_templates",
                "responseTemplates",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "content_handling",
                "contentHandling",
                TypeInfo(typing.Union[str, ContentHandlingStrategy]),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Specifies the status code that is used to map the integration response to
    # an existing MethodResponse.
    status_code: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Specifies the regular expression (regex) pattern used to choose an
    # integration response based on the response from the back end. For example,
    # if the success response returns nothing and the error response returns some
    # string, you could use the `.+` regex to match error response. However, make
    # sure that the error response does not contain any newline (`\n`) character
    # in such cases. If the back end is an AWS Lambda function, the AWS Lambda
    # function error header is matched. For all other HTTP and AWS back ends, the
    # HTTP status code is matched.
    selection_pattern: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A key-value map specifying response parameters that are passed to the
    # method response from the back end. The key is a method response header
    # parameter name and the mapped value is an integration response header
    # value, a static value enclosed within a pair of single quotes, or a JSON
    # expression from the integration response body. The mapping key must match
    # the pattern of `method.response.header.{name}`, where `name` is a valid and
    # unique header name. The mapped non-static value must match the pattern of
    # `integration.response.header.{name}` or `integration.response.body.{JSON-
    # expression}`, where `name` is a valid and unique response header name and
    # `JSON-expression` is a valid JSON expression without the `$` prefix.
    response_parameters: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Specifies the templates used to transform the integration response body.
    # Response templates are represented as a key/value map, with a content-type
    # as the key and a template as the value.
    response_templates: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Specifies how to handle response payload content type conversions.
    # Supported values are `CONVERT_TO_BINARY` and `CONVERT_TO_TEXT`, with the
    # following behaviors:

    #   * `CONVERT_TO_BINARY`: Converts a response payload from a Base64-encoded string to the corresponding binary blob.

    #   * `CONVERT_TO_TEXT`: Converts a response payload from a binary blob to a Base64-encoded string.

    # If this property is not defined, the response payload will be passed
    # through from the integration response to the method response without
    # modification.
    content_handling: typing.Union[str, "ContentHandlingStrategy"
                                  ] = dataclasses.field(
                                      default=ShapeBase.NOT_SET,
                                  )


class IntegrationType(str):
    """
    The integration type. The valid value is `HTTP` for integrating an API method
    with an HTTP backend; `AWS` with any AWS service endpoints; `MOCK` for testing
    without actually invoking the backend; `HTTP_PROXY` for integrating with the
    HTTP proxy integration; `AWS_PROXY` for integrating with the Lambda proxy
    integration.
    """
    HTTP = "HTTP"
    AWS = "AWS"
    MOCK = "MOCK"
    HTTP_PROXY = "HTTP_PROXY"
    AWS_PROXY = "AWS_PROXY"


@dataclasses.dataclass
class LimitExceededException(ShapeBase):
    """
    The request exceeded the rate limit. Retry after the specified time period.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "retry_after_seconds",
                "retryAfterSeconds",
                TypeInfo(str),
            ),
            (
                "message",
                "message",
                TypeInfo(str),
            ),
        ]

    retry_after_seconds: str = dataclasses.field(default=ShapeBase.NOT_SET, )
    message: str = dataclasses.field(default=ShapeBase.NOT_SET, )


class LocationStatusType(str):
    DOCUMENTED = "DOCUMENTED"
    UNDOCUMENTED = "UNDOCUMENTED"


@dataclasses.dataclass
class Method(OutputShapeBase):
    """
    Represents a client-facing interface by which the client calls the API to access
    back-end resources. A **Method** resource is integrated with an Integration
    resource. Both consist of a request and one or more responses. The method
    request takes the client input that is passed to the back end through the
    integration request. A method response returns the output from the back end to
    the client through an integration response. A method request is embodied in a
    **Method** resource, whereas an integration request is embodied in an
    Integration resource. On the other hand, a method response is represented by a
    MethodResponse resource, whereas an integration response is represented by an
    IntegrationResponse resource.

    #### Example: Retrive the GET method on a specified resource

    ##### Request

    The following example request retrieves the information about the GET method on
    an API resource (`3kzxbg5sa2`) of an API (`fugvjdxtri`).



        GET /restapis/fugvjdxtri/resources/3kzxbg5sa2/methods/GET HTTP/1.1 Content-Type: application/json Host: apigateway.us-east-1.amazonaws.com X-Amz-Date: 20160603T210259Z Authorization: AWS4-HMAC-SHA256 Credential={access_key_ID}/20160603/us-east-1/apigateway/aws4_request, SignedHeaders=content-type;host;x-amz-date, Signature={sig4_hash}

    ##### Response

    The successful response returns a `200 OK` status code and a payload similar to
    the following:



        { "_links": { "curies": [ { "href": "http://docs.aws.amazon.com/apigateway/latest/developerguide/restapi-integration-{rel}.html", "name": "integration", "templated": true }, { "href": "http://docs.aws.amazon.com/apigateway/latest/developerguide/restapi-integration-response-{rel}.html", "name": "integrationresponse", "templated": true }, { "href": "http://docs.aws.amazon.com/apigateway/latest/developerguide/restapi-method-{rel}.html", "name": "method", "templated": true }, { "href": "http://docs.aws.amazon.com/apigateway/latest/developerguide/restapi-method-response-{rel}.html", "name": "methodresponse", "templated": true } ], "self": { "href": "/restapis/fugvjdxtri/resources/3kzxbg5sa2/methods/GET", "name": "GET", "title": "GET" }, "integration:put": { "href": "/restapis/fugvjdxtri/resources/3kzxbg5sa2/methods/GET/integration" }, "method:delete": { "href": "/restapis/fugvjdxtri/resources/3kzxbg5sa2/methods/GET" }, "method:integration": { "href": "/restapis/fugvjdxtri/resources/3kzxbg5sa2/methods/GET/integration" }, "method:responses": { "href": "/restapis/fugvjdxtri/resources/3kzxbg5sa2/methods/GET/responses/200", "name": "200", "title": "200" }, "method:update": { "href": "/restapis/fugvjdxtri/resources/3kzxbg5sa2/methods/GET" }, "methodresponse:put": { "href": "/restapis/fugvjdxtri/resources/3kzxbg5sa2/methods/GET/responses/{status_code}", "templated": true } }, "apiKeyRequired": true, "authorizationType": "NONE", "httpMethod": "GET", "_embedded": { "method:integration": { "_links": { "self": { "href": "/restapis/fugvjdxtri/resources/3kzxbg5sa2/methods/GET/integration" }, "integration:delete": { "href": "/restapis/fugvjdxtri/resources/3kzxbg5sa2/methods/GET/integration" }, "integration:responses": { "href": "/restapis/fugvjdxtri/resources/3kzxbg5sa2/methods/GET/integration/responses/200", "name": "200", "title": "200" }, "integration:update": { "href": "/restapis/fugvjdxtri/resources/3kzxbg5sa2/methods/GET/integration" }, "integrationresponse:put": { "href": "/restapis/fugvjdxtri/resources/3kzxbg5sa2/methods/GET/integration/responses/{status_code}", "templated": true } }, "cacheKeyParameters": [], "cacheNamespace": "3kzxbg5sa2", "credentials": "arn:aws:iam::123456789012:role/apigAwsProxyRole", "httpMethod": "POST", "passthroughBehavior": "WHEN_NO_MATCH", "requestParameters": { "integration.request.header.Content-Type": "'application/x-amz-json-1.1'" }, "requestTemplates": { "application/json": "{\n}" }, "type": "AWS", "uri": "arn:aws:apigateway:us-east-1:kinesis:action/ListStreams", "_embedded": { "integration:responses": { "_links": { "self": { "href": "/restapis/fugvjdxtri/resources/3kzxbg5sa2/methods/GET/integration/responses/200", "name": "200", "title": "200" }, "integrationresponse:delete": { "href": "/restapis/fugvjdxtri/resources/3kzxbg5sa2/methods/GET/integration/responses/200" }, "integrationresponse:update": { "href": "/restapis/fugvjdxtri/resources/3kzxbg5sa2/methods/GET/integration/responses/200" } }, "responseParameters": { "method.response.header.Content-Type": "'application/xml'" }, "responseTemplates": { "application/json": "$util.urlDecode(\"%3CkinesisStreams%3E%23foreach(%24stream%20in%20%24input.path(%27%24.StreamNames%27))%3Cstream%3E%3Cname%3E%24stream%3C%2Fname%3E%3C%2Fstream%3E%23end%3C%2FkinesisStreams%3E\")" }, "statusCode": "200" } } }, "method:responses": { "_links": { "self": { "href": "/restapis/fugvjdxtri/resources/3kzxbg5sa2/methods/GET/responses/200", "name": "200", "title": "200" }, "methodresponse:delete": { "href": "/restapis/fugvjdxtri/resources/3kzxbg5sa2/methods/GET/responses/200" }, "methodresponse:update": { "href": "/restapis/fugvjdxtri/resources/3kzxbg5sa2/methods/GET/responses/200" } }, "responseModels": { "application/json": "Empty" }, "responseParameters": { "method.response.header.Content-Type": false }, "statusCode": "200" } } }

    In the example above, the response template for the `200 OK` response maps the
    JSON output from the `ListStreams` action in the back end to an XML output. The
    mapping template is URL-encoded as
    `%3CkinesisStreams%3E%23foreach(%24stream%20in%20%24input.path(%27%24.StreamNames%27))%3Cstream%3E%3Cname%3E%24stream%3C%2Fname%3E%3C%2Fstream%3E%23end%3C%2FkinesisStreams%3E`
    and the output is decoded using the
    [$util.urlDecode()](http://docs.aws.amazon.com/apigateway/latest/developerguide/api-
    gateway-mapping-template-reference.html#util-templat-reference) helper function.

    MethodResponse, Integration, IntegrationResponse, Resource, [Set up an API's
    method](http://docs.aws.amazon.com/apigateway/latest/developerguide/how-to-
    method-settings.html)
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
                "http_method",
                "httpMethod",
                TypeInfo(str),
            ),
            (
                "authorization_type",
                "authorizationType",
                TypeInfo(str),
            ),
            (
                "authorizer_id",
                "authorizerId",
                TypeInfo(str),
            ),
            (
                "api_key_required",
                "apiKeyRequired",
                TypeInfo(bool),
            ),
            (
                "request_validator_id",
                "requestValidatorId",
                TypeInfo(str),
            ),
            (
                "operation_name",
                "operationName",
                TypeInfo(str),
            ),
            (
                "request_parameters",
                "requestParameters",
                TypeInfo(typing.Dict[str, bool]),
            ),
            (
                "request_models",
                "requestModels",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "method_responses",
                "methodResponses",
                TypeInfo(typing.Dict[str, MethodResponse]),
            ),
            (
                "method_integration",
                "methodIntegration",
                TypeInfo(Integration),
            ),
            (
                "authorization_scopes",
                "authorizationScopes",
                TypeInfo(typing.List[str]),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The method's HTTP verb.
    http_method: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The method's authorization type. Valid values are `NONE` for open access,
    # `AWS_IAM` for using AWS IAM permissions, `CUSTOM` for using a custom
    # authorizer, or `COGNITO_USER_POOLS` for using a Cognito user pool.
    authorization_type: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The identifier of an Authorizer to use on this method. The
    # `authorizationType` must be `CUSTOM`.
    authorizer_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A boolean flag specifying whether a valid ApiKey is required to invoke this
    # method.
    api_key_required: bool = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The identifier of a RequestValidator for request validation.
    request_validator_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A human-friendly operation identifier for the method. For example, you can
    # assign the `operationName` of `ListPets` for the `GET /pets` method in
    # [PetStore](http://petstore-demo-endpoint.execute-api.com/petstore/pets)
    # example.
    operation_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A key-value map defining required or optional method request parameters
    # that can be accepted by API Gateway. A key is a method request parameter
    # name matching the pattern of `method.request.{location}.{name}`, where
    # `location` is `querystring`, `path`, or `header` and `name` is a valid and
    # unique parameter name. The value associated with the key is a Boolean flag
    # indicating whether the parameter is required (`true`) or optional
    # (`false`). The method request parameter names defined here are available in
    # Integration to be mapped to integration request parameters or templates.
    request_parameters: typing.Dict[str, bool] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A key-value map specifying data schemas, represented by Model resources,
    # (as the mapped value) of the request payloads of given content types (as
    # the mapping key).
    request_models: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Gets a method response associated with a given HTTP status code.

    # The collection of method responses are encapsulated in a key-value map,
    # where the key is a response's HTTP status code and the value is a
    # MethodResponse resource that specifies the response returned to the caller
    # from the back end through the integration response.

    # #### Example: Get a 200 OK response of a GET method

    # ##### Request

    #     GET /restapis/uojnr9hd57/resources/0cjtch/methods/GET/responses/200 HTTP/1.1 Content-Type: application/json Host: apigateway.us-east-1.amazonaws.com Content-Length: 117 X-Amz-Date: 20160613T215008Z Authorization: AWS4-HMAC-SHA256 Credential={access_key_ID}/20160613/us-east-1/apigateway/aws4_request, SignedHeaders=content-type;host;x-amz-date, Signature={sig4_hash}

    # ##### Response

    # The successful response returns a `200 OK` status code and a payload
    # similar to the following:

    #     { "_links": { "curies": { "href": "http://docs.aws.amazon.com/apigateway/latest/developerguide/restapi-method-response-{rel}.html", "name": "methodresponse", "templated": true }, "self": { "href": "/restapis/uojnr9hd57/resources/0cjtch/methods/GET/responses/200", "title": "200" }, "methodresponse:delete": { "href": "/restapis/uojnr9hd57/resources/0cjtch/methods/GET/responses/200" }, "methodresponse:update": { "href": "/restapis/uojnr9hd57/resources/0cjtch/methods/GET/responses/200" } }, "responseModels": { "application/json": "Empty" }, "responseParameters": { "method.response.header.operator": false, "method.response.header.operand_2": false, "method.response.header.operand_1": false }, "statusCode": "200" }

    # [AWS CLI](http://docs.aws.amazon.com/cli/latest/reference/apigateway/get-
    # method-response.html)
    method_responses: typing.Dict[str, "MethodResponse"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Gets the method's integration responsible for passing the client-submitted
    # request to the back end and performing necessary transformations to make
    # the request compliant with the back end.

    # #### Example:

    # ##### Request

    #     GET /restapis/uojnr9hd57/resources/0cjtch/methods/GET/integration HTTP/1.1 Content-Type: application/json Host: apigateway.us-east-1.amazonaws.com Content-Length: 117 X-Amz-Date: 20160613T213210Z Authorization: AWS4-HMAC-SHA256 Credential={access_key_ID}/20160613/us-east-1/apigateway/aws4_request, SignedHeaders=content-type;host;x-amz-date, Signature={sig4_hash}

    # ##### Response

    # The successful response returns a `200 OK` status code and a payload
    # similar to the following:

    #     { "_links": { "curies": [ { "href": "http://docs.aws.amazon.com/apigateway/latest/developerguide/restapi-integration-{rel}.html", "name": "integration", "templated": true }, { "href": "http://docs.aws.amazon.com/apigateway/latest/developerguide/restapi-integration-response-{rel}.html", "name": "integrationresponse", "templated": true } ], "self": { "href": "/restapis/uojnr9hd57/resources/0cjtch/methods/GET/integration" }, "integration:delete": { "href": "/restapis/uojnr9hd57/resources/0cjtch/methods/GET/integration" }, "integration:responses": { "href": "/restapis/uojnr9hd57/resources/0cjtch/methods/GET/integration/responses/200", "name": "200", "title": "200" }, "integration:update": { "href": "/restapis/uojnr9hd57/resources/0cjtch/methods/GET/integration" }, "integrationresponse:put": { "href": "/restapis/uojnr9hd57/resources/0cjtch/methods/GET/integration/responses/{status_code}", "templated": true } }, "cacheKeyParameters": [], "cacheNamespace": "0cjtch", "credentials": "arn:aws:iam::123456789012:role/apigAwsProxyRole", "httpMethod": "POST", "passthroughBehavior": "WHEN_NO_MATCH", "requestTemplates": { "application/json": "{\n \"a\": \"$input.params('operand1')\",\n \"b\": \"$input.params('operand2')\", \n \"op\": \"$input.params('operator')\" \n}" }, "type": "AWS", "uri": "arn:aws:apigateway:us-west-2:lambda:path//2015-03-31/functions/arn:aws:lambda:us-west-2:123456789012:function:Calc/invocations", "_embedded": { "integration:responses": { "_links": { "self": { "href": "/restapis/uojnr9hd57/resources/0cjtch/methods/GET/integration/responses/200", "name": "200", "title": "200" }, "integrationresponse:delete": { "href": "/restapis/uojnr9hd57/resources/0cjtch/methods/GET/integration/responses/200" }, "integrationresponse:update": { "href": "/restapis/uojnr9hd57/resources/0cjtch/methods/GET/integration/responses/200" } }, "responseParameters": { "method.response.header.operator": "integration.response.body.op", "method.response.header.operand_2": "integration.response.body.b", "method.response.header.operand_1": "integration.response.body.a" }, "responseTemplates": { "application/json": "#set($res = $input.path('$'))\n{\n \"result\": \"$res.a, $res.b, $res.op => $res.c\",\n \"a\" : \"$res.a\",\n \"b\" : \"$res.b\",\n \"op\" : \"$res.op\",\n \"c\" : \"$res.c\"\n}" }, "selectionPattern": "", "statusCode": "200" } } }

    # [AWS CLI](http://docs.aws.amazon.com/cli/latest/reference/apigateway/get-
    # integration.html)
    method_integration: "Integration" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A list of authorization scopes configured on the method. The scopes are
    # used with a `COGNITO_USER_POOLS` authorizer to authorize the method
    # invocation. The authorization works by matching the method scopes against
    # the scopes parsed from the access token in the incoming request. The method
    # invocation is authorized if any method scopes matches a claimed scope in
    # the access token. Otherwise, the invocation is not authorized. When the
    # method scope is configured, the client must provide an access token instead
    # of an identity token for authorization purposes.
    authorization_scopes: typing.List[str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class MethodResponse(OutputShapeBase):
    """
    Represents a method response of a given HTTP status code returned to the client.
    The method response is passed from the back end through the associated
    integration response that can be transformed using a mapping template.

    #### Example: A **MethodResponse** instance of an API

    ##### Request

    The example request retrieves a **MethodResponse** of the 200 status code.



        GET /restapis/fugvjdxtri/resources/3kzxbg5sa2/methods/GET/responses/200 HTTP/1.1 Content-Type: application/json Host: apigateway.us-east-1.amazonaws.com X-Amz-Date: 20160603T222952Z Authorization: AWS4-HMAC-SHA256 Credential={access_key_ID}/20160603/us-east-1/apigateway/aws4_request, SignedHeaders=content-type;host;x-amz-date, Signature={sig4_hash}

    ##### Response

    The successful response returns `200 OK` status and a payload as follows:



        { "_links": { "curies": { "href": "http://docs.aws.amazon.com/apigateway/latest/developerguide/restapi-method-response-{rel}.html", "name": "methodresponse", "templated": true }, "self": { "href": "/restapis/fugvjdxtri/resources/3kzxbg5sa2/methods/GET/responses/200", "title": "200" }, "methodresponse:delete": { "href": "/restapis/fugvjdxtri/resources/3kzxbg5sa2/methods/GET/responses/200" }, "methodresponse:update": { "href": "/restapis/fugvjdxtri/resources/3kzxbg5sa2/methods/GET/responses/200" } }, "responseModels": { "application/json": "Empty" }, "responseParameters": { "method.response.header.Content-Type": false }, "statusCode": "200" }

    Method, IntegrationResponse, Integration [Creating an
    API](http://docs.aws.amazon.com/apigateway/latest/developerguide/how-to-create-
    api.html)
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
                "status_code",
                "statusCode",
                TypeInfo(str),
            ),
            (
                "response_parameters",
                "responseParameters",
                TypeInfo(typing.Dict[str, bool]),
            ),
            (
                "response_models",
                "responseModels",
                TypeInfo(typing.Dict[str, str]),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The method response's status code.
    status_code: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A key-value map specifying required or optional response parameters that
    # API Gateway can send back to the caller. A key defines a method response
    # header and the value specifies whether the associated method response
    # header is required or not. The expression of the key must match the pattern
    # `method.response.header.{name}`, where `name` is a valid and unique header
    # name. API Gateway passes certain integration response data to the method
    # response headers specified here according to the mapping you prescribe in
    # the API's IntegrationResponse. The integration response data that can be
    # mapped include an integration response header expressed in
    # `integration.response.header.{name}`, a static value enclosed within a pair
    # of single quotes (e.g., `'application/json'`), or a JSON expression from
    # the back-end response payload in the form of
    # `integration.response.body.{JSON-expression}`, where `JSON-expression` is a
    # valid JSON expression without the `$` prefix.)
    response_parameters: typing.Dict[str, bool] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Specifies the Model resources used for the response's content-type.
    # Response models are represented as a key/value map, with a content-type as
    # the key and a Model name as the value.
    response_models: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class MethodSetting(ShapeBase):
    """
    Specifies the method setting properties.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "metrics_enabled",
                "metricsEnabled",
                TypeInfo(bool),
            ),
            (
                "logging_level",
                "loggingLevel",
                TypeInfo(str),
            ),
            (
                "data_trace_enabled",
                "dataTraceEnabled",
                TypeInfo(bool),
            ),
            (
                "throttling_burst_limit",
                "throttlingBurstLimit",
                TypeInfo(int),
            ),
            (
                "throttling_rate_limit",
                "throttlingRateLimit",
                TypeInfo(float),
            ),
            (
                "caching_enabled",
                "cachingEnabled",
                TypeInfo(bool),
            ),
            (
                "cache_ttl_in_seconds",
                "cacheTtlInSeconds",
                TypeInfo(int),
            ),
            (
                "cache_data_encrypted",
                "cacheDataEncrypted",
                TypeInfo(bool),
            ),
            (
                "require_authorization_for_cache_control",
                "requireAuthorizationForCacheControl",
                TypeInfo(bool),
            ),
            (
                "unauthorized_cache_control_header_strategy",
                "unauthorizedCacheControlHeaderStrategy",
                TypeInfo(
                    typing.Union[str, UnauthorizedCacheControlHeaderStrategy]
                ),
            ),
        ]

    # Specifies whether Amazon CloudWatch metrics are enabled for this method.
    # The PATCH path for this setting is `/{method_setting_key}/metrics/enabled`,
    # and the value is a Boolean.
    metrics_enabled: bool = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Specifies the logging level for this method, which affects the log entries
    # pushed to Amazon CloudWatch Logs. The PATCH path for this setting is
    # `/{method_setting_key}/logging/loglevel`, and the available levels are
    # `OFF`, `ERROR`, and `INFO`.
    logging_level: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Specifies whether data trace logging is enabled for this method, which
    # affects the log entries pushed to Amazon CloudWatch Logs. The PATCH path
    # for this setting is `/{method_setting_key}/logging/dataTrace`, and the
    # value is a Boolean.
    data_trace_enabled: bool = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Specifies the throttling burst limit. The PATCH path for this setting is
    # `/{method_setting_key}/throttling/burstLimit`, and the value is an integer.
    throttling_burst_limit: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Specifies the throttling rate limit. The PATCH path for this setting is
    # `/{method_setting_key}/throttling/rateLimit`, and the value is a double.
    throttling_rate_limit: float = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Specifies whether responses should be cached and returned for requests. A
    # cache cluster must be enabled on the stage for responses to be cached. The
    # PATCH path for this setting is `/{method_setting_key}/caching/enabled`, and
    # the value is a Boolean.
    caching_enabled: bool = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Specifies the time to live (TTL), in seconds, for cached responses. The
    # higher the TTL, the longer the response will be cached. The PATCH path for
    # this setting is `/{method_setting_key}/caching/ttlInSeconds`, and the value
    # is an integer.
    cache_ttl_in_seconds: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Specifies whether the cached responses are encrypted. The PATCH path for
    # this setting is `/{method_setting_key}/caching/dataEncrypted`, and the
    # value is a Boolean.
    cache_data_encrypted: bool = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Specifies whether authorization is required for a cache invalidation
    # request. The PATCH path for this setting is
    # `/{method_setting_key}/caching/requireAuthorizationForCacheControl`, and
    # the value is a Boolean.
    require_authorization_for_cache_control: bool = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Specifies how to handle unauthorized requests for cache invalidation. The
    # PATCH path for this setting is
    # `/{method_setting_key}/caching/unauthorizedCacheControlHeaderStrategy`, and
    # the available values are `FAIL_WITH_403`, `SUCCEED_WITH_RESPONSE_HEADER`,
    # `SUCCEED_WITHOUT_RESPONSE_HEADER`.
    unauthorized_cache_control_header_strategy: typing.Union[
        str, "UnauthorizedCacheControlHeaderStrategy"] = dataclasses.field(
            default=ShapeBase.NOT_SET,
        )


@dataclasses.dataclass
class MethodSnapshot(ShapeBase):
    """
    Represents a summary of a Method resource, given a particular date and time.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "authorization_type",
                "authorizationType",
                TypeInfo(str),
            ),
            (
                "api_key_required",
                "apiKeyRequired",
                TypeInfo(bool),
            ),
        ]

    # The method's authorization type. Valid values are `NONE` for open access,
    # `AWS_IAM` for using AWS IAM permissions, `CUSTOM` for using a custom
    # authorizer, or `COGNITO_USER_POOLS` for using a Cognito user pool.
    authorization_type: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Specifies whether the method requires a valid ApiKey.
    api_key_required: bool = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class Model(OutputShapeBase):
    """
    Represents the data structure of a method's request or response payload.

    A request model defines the data structure of the client-supplied request
    payload. A response model defines the data structure of the response payload
    returned by the back end. Although not required, models are useful for mapping
    payloads between the front end and back end.

    A model is used for generating an API's SDK, validating the input request body,
    and creating a skeletal mapping template.

    Method, MethodResponse, [Models and
    Mappings](http://docs.aws.amazon.com/apigateway/latest/developerguide/models-
    mappings.html)
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
                "id",
                "id",
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
                "schema",
                "schema",
                TypeInfo(str),
            ),
            (
                "content_type",
                "contentType",
                TypeInfo(str),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The identifier for the model resource.
    id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The name of the model. Must be an alphanumeric string.
    name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The description of the model.
    description: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The schema for the model. For `application/json` models, this should be
    # [JSON schema draft 4](https://tools.ietf.org/html/draft-zyp-json-schema-04)
    # model. Do not include "\\*/" characters in the description of any
    # properties because such "\\*/" characters may be interpreted as the closing
    # marker for comments in some languages, such as Java or JavaScript, causing
    # the installation of your API's SDK generated by API Gateway to fail.
    schema: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The content-type for the model.
    content_type: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class Models(OutputShapeBase):
    """
    Represents a collection of Model resources.

    Method, MethodResponse, [Models and
    Mappings](http://docs.aws.amazon.com/apigateway/latest/developerguide/models-
    mappings.html)
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
                "position",
                "position",
                TypeInfo(str),
            ),
            (
                "items",
                "items",
                TypeInfo(typing.List[Model]),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )
    position: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The current page of elements from this collection.
    items: typing.List["Model"] = dataclasses.field(default=ShapeBase.NOT_SET, )

    def paginate(self, ) -> typing.Generator["Models", None, None]:
        yield from super()._paginate()


@dataclasses.dataclass
class NotFoundException(ShapeBase):
    """
    The requested resource is not found. Make sure that the request URI is correct.
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


class Op(str):
    add = "add"
    remove = "remove"
    replace = "replace"
    move = "move"
    copy = "copy"
    test = "test"


@dataclasses.dataclass
class PatchOperation(ShapeBase):
    """
    A single patch operation to apply to the specified resource. Please refer to
    http://tools.ietf.org/html/rfc6902#section-4 for an explanation of how each
    operation is used.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "op",
                "op",
                TypeInfo(typing.Union[str, Op]),
            ),
            (
                "path",
                "path",
                TypeInfo(str),
            ),
            (
                "value",
                "value",
                TypeInfo(str),
            ),
            (
                "from_",
                "from",
                TypeInfo(str),
            ),
        ]

    # An update operation to be performed with this PATCH request. The valid
    # value can be `add`, `remove`, `replace` or `copy`. Not all valid operations
    # are supported for a given resource. Support of the operations depends on
    # specific operational contexts. Attempts to apply an unsupported operation
    # on a resource will return an error message.
    op: typing.Union[str, "Op"] = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The `op` operation's target, as identified by a [JSON
    # Pointer](https://tools.ietf.org/html/draft-ietf-appsawg-json-pointer-08)
    # value that references a location within the targeted resource. For example,
    # if the target resource has an updateable property of `{"name":"value"}`,
    # the path for this property is `/name`. If the `name` property value is a
    # JSON object (e.g., `{"name": {"child/name": "child-value"}}`), the path for
    # the `child/name` property will be `/name/child~1name`. Any slash ("/")
    # character appearing in path names must be escaped with "~1", as shown in
    # the example above. Each `op` operation can have only one `path` associated
    # with it.
    path: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The new target value of the update operation. It is applicable for the
    # `add` or `replace` operation. When using AWS CLI to update a property of a
    # JSON value, enclose the JSON object with a pair of single quotes in a Linux
    # shell, e.g., '{"a": ...}'. In a Windows shell, see [Using JSON for
    # Parameters](http://docs.aws.amazon.com/cli/latest/userguide/cli-using-
    # param.html#cli-using-param-json).
    value: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The `copy` update operation's source as identified by a `JSON-Pointer`
    # value referencing the location within the targeted resource to copy the
    # value from. For example, to promote a canary deployment, you copy the
    # canary deployment ID to the affiliated deployment ID by calling a PATCH
    # request on a Stage resource with `"op":"copy"`,
    # `"from":"/canarySettings/deploymentId"` and `"path":"/deploymentId"`.
    from_: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class PutGatewayResponseRequest(ShapeBase):
    """
    Creates a customization of a GatewayResponse of a specified response type and
    status code on the given RestApi.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "rest_api_id",
                "restApiId",
                TypeInfo(str),
            ),
            (
                "response_type",
                "responseType",
                TypeInfo(typing.Union[str, GatewayResponseType]),
            ),
            (
                "status_code",
                "statusCode",
                TypeInfo(str),
            ),
            (
                "response_parameters",
                "responseParameters",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "response_templates",
                "responseTemplates",
                TypeInfo(typing.Dict[str, str]),
            ),
        ]

    # [Required] The string identifier of the associated RestApi.
    rest_api_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # [Required]

    # The response type of the associated GatewayResponse. Valid values are

    #   * ACCESS_DENIED
    #   * API_CONFIGURATION_ERROR
    #   * AUTHORIZER_FAILURE
    #   * AUTHORIZER_CONFIGURATION_ERROR
    #   * BAD_REQUEST_PARAMETERS
    #   * BAD_REQUEST_BODY
    #   * DEFAULT_4XX
    #   * DEFAULT_5XX
    #   * EXPIRED_TOKEN
    #   * INVALID_SIGNATURE
    #   * INTEGRATION_FAILURE
    #   * INTEGRATION_TIMEOUT
    #   * INVALID_API_KEY
    #   * MISSING_AUTHENTICATION_TOKEN
    #   * QUOTA_EXCEEDED
    #   * REQUEST_TOO_LARGE
    #   * RESOURCE_NOT_FOUND
    #   * THROTTLED
    #   * UNAUTHORIZED
    #   * UNSUPPORTED_MEDIA_TYPE
    response_type: typing.Union[str, "GatewayResponseType"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The HTTP status code of the GatewayResponse.
    status_code: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Response parameters (paths, query strings and headers) of the
    # GatewayResponse as a string-to-string map of key-value pairs.
    response_parameters: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Response templates of the GatewayResponse as a string-to-string map of key-
    # value pairs.
    response_templates: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class PutIntegrationRequest(ShapeBase):
    """
    Sets up a method's integration.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "rest_api_id",
                "restApiId",
                TypeInfo(str),
            ),
            (
                "resource_id",
                "resourceId",
                TypeInfo(str),
            ),
            (
                "http_method",
                "httpMethod",
                TypeInfo(str),
            ),
            (
                "type",
                "type",
                TypeInfo(typing.Union[str, IntegrationType]),
            ),
            (
                "integration_http_method",
                "integrationHttpMethod",
                TypeInfo(str),
            ),
            (
                "uri",
                "uri",
                TypeInfo(str),
            ),
            (
                "connection_type",
                "connectionType",
                TypeInfo(typing.Union[str, ConnectionType]),
            ),
            (
                "connection_id",
                "connectionId",
                TypeInfo(str),
            ),
            (
                "credentials",
                "credentials",
                TypeInfo(str),
            ),
            (
                "request_parameters",
                "requestParameters",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "request_templates",
                "requestTemplates",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "passthrough_behavior",
                "passthroughBehavior",
                TypeInfo(str),
            ),
            (
                "cache_namespace",
                "cacheNamespace",
                TypeInfo(str),
            ),
            (
                "cache_key_parameters",
                "cacheKeyParameters",
                TypeInfo(typing.List[str]),
            ),
            (
                "content_handling",
                "contentHandling",
                TypeInfo(typing.Union[str, ContentHandlingStrategy]),
            ),
            (
                "timeout_in_millis",
                "timeoutInMillis",
                TypeInfo(int),
            ),
        ]

    # [Required] The string identifier of the associated RestApi.
    rest_api_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # [Required] Specifies a put integration request's resource ID.
    resource_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # [Required] Specifies a put integration request's HTTP method.
    http_method: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # [Required] Specifies a put integration input's type.
    type: typing.Union[str, "IntegrationType"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Specifies a put integration HTTP method. When the integration type is HTTP
    # or AWS, this field is required.
    integration_http_method: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Specifies Uniform Resource Identifier (URI) of the integration endpoint.

    #   * For `HTTP` or `HTTP_PROXY` integrations, the URI must be a fully formed, encoded HTTP(S) URL according to the [RFC-3986 specification](https://en.wikipedia.org/wiki/Uniform_Resource_Identifier), for either standard integration, where `connectionType` is not `VPC_LINK`, or private integration, where `connectionType` is `VPC_LINK`. For a private HTTP integration, the URI is not used for routing.

    #   * For `AWS` or `AWS_PROXY` integrations, the URI is of the form `arn:aws:apigateway:{region}:{subdomain.service|service}:path|action/{service_api}`. Here, `{Region}` is the API Gateway region (e.g., `us-east-1`); `{service}` is the name of the integrated AWS service (e.g., `s3`); and `{subdomain}` is a designated subdomain supported by certain AWS service for fast host-name lookup. `action` can be used for an AWS service action-based API, using an `Action={name}&{p1}={v1}&p2={v2}...` query string. The ensuing `{service_api}` refers to a supported action `{name}` plus any required input parameters. Alternatively, `path` can be used for an AWS service path-based API. The ensuing `service_api` refers to the path to an AWS service resource, including the region of the integrated AWS service, if applicable. For example, for integration with the S3 API of `[GetObject](http://docs.aws.amazon.com/AmazonS3/latest/API/RESTObjectGET.html)`, the `uri` can be either `arn:aws:apigateway:us-west-2:s3:action/GetObject&Bucket={bucket}&Key={key}` or `arn:aws:apigateway:us-west-2:s3:path/{bucket}/{key}`
    uri: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The type of the network connection to the integration endpoint. The valid
    # value is `INTERNET` for connections through the public routable internet or
    # `VPC_LINK` for private connections between API Gateway and a network load
    # balancer in a VPC. The default value is `INTERNET`.
    connection_type: typing.Union[str, "ConnectionType"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The ([`id`](http://docs.aws.amazon.com/apigateway/api-
    # reference/resource/vpc-link/#id)) of the VpcLink used for the integration
    # when `connectionType=VPC_LINK` and undefined, otherwise.
    connection_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Specifies whether credentials are required for a put integration.
    credentials: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A key-value map specifying request parameters that are passed from the
    # method request to the back end. The key is an integration request parameter
    # name and the associated value is a method request parameter value or static
    # value that must be enclosed within single quotes and pre-encoded as
    # required by the back end. The method request parameter value must match the
    # pattern of `method.request.{location}.{name}`, where `location` is
    # `querystring`, `path`, or `header` and `name` must be a valid and unique
    # method request parameter name.
    request_parameters: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Represents a map of Velocity templates that are applied on the request
    # payload based on the value of the Content-Type header sent by the client.
    # The content type value is the key in this map, and the template (as a
    # String) is the value.
    request_templates: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Specifies the pass-through behavior for incoming requests based on the
    # Content-Type header in the request, and the available mapping templates
    # specified as the `requestTemplates` property on the Integration resource.
    # There are three valid values: `WHEN_NO_MATCH`, `WHEN_NO_TEMPLATES`, and
    # `NEVER`.

    #   * `WHEN_NO_MATCH` passes the request body for unmapped content types through to the integration back end without transformation.

    #   * `NEVER` rejects unmapped content types with an HTTP 415 'Unsupported Media Type' response.

    #   * `WHEN_NO_TEMPLATES` allows pass-through when the integration has NO content types mapped to templates. However if there is at least one content type defined, unmapped content types will be rejected with the same 415 response.
    passthrough_behavior: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Specifies a put integration input's cache namespace.
    cache_namespace: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Specifies a put integration input's cache key parameters.
    cache_key_parameters: typing.List[str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Specifies how to handle request payload content type conversions. Supported
    # values are `CONVERT_TO_BINARY` and `CONVERT_TO_TEXT`, with the following
    # behaviors:

    #   * `CONVERT_TO_BINARY`: Converts a request payload from a Base64-encoded string to the corresponding binary blob.

    #   * `CONVERT_TO_TEXT`: Converts a request payload from a binary blob to a Base64-encoded string.

    # If this property is not defined, the request payload will be passed through
    # from the method request to integration request without modification,
    # provided that the `passthroughBehaviors` is configured to support payload
    # pass-through.
    content_handling: typing.Union[str, "ContentHandlingStrategy"
                                  ] = dataclasses.field(
                                      default=ShapeBase.NOT_SET,
                                  )

    # Custom timeout between 50 and 29,000 milliseconds. The default value is
    # 29,000 milliseconds or 29 seconds.
    timeout_in_millis: int = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class PutIntegrationResponseRequest(ShapeBase):
    """
    Represents a put integration response request.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "rest_api_id",
                "restApiId",
                TypeInfo(str),
            ),
            (
                "resource_id",
                "resourceId",
                TypeInfo(str),
            ),
            (
                "http_method",
                "httpMethod",
                TypeInfo(str),
            ),
            (
                "status_code",
                "statusCode",
                TypeInfo(str),
            ),
            (
                "selection_pattern",
                "selectionPattern",
                TypeInfo(str),
            ),
            (
                "response_parameters",
                "responseParameters",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "response_templates",
                "responseTemplates",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "content_handling",
                "contentHandling",
                TypeInfo(typing.Union[str, ContentHandlingStrategy]),
            ),
        ]

    # [Required] The string identifier of the associated RestApi.
    rest_api_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # [Required] Specifies a put integration response request's resource
    # identifier.
    resource_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # [Required] Specifies a put integration response request's HTTP method.
    http_method: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # [Required] Specifies the status code that is used to map the integration
    # response to an existing MethodResponse.
    status_code: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Specifies the selection pattern of a put integration response.
    selection_pattern: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A key-value map specifying response parameters that are passed to the
    # method response from the back end. The key is a method response header
    # parameter name and the mapped value is an integration response header
    # value, a static value enclosed within a pair of single quotes, or a JSON
    # expression from the integration response body. The mapping key must match
    # the pattern of `method.response.header.{name}`, where `name` is a valid and
    # unique header name. The mapped non-static value must match the pattern of
    # `integration.response.header.{name}` or `integration.response.body.{JSON-
    # expression}`, where `name` must be a valid and unique response header name
    # and `JSON-expression` a valid JSON expression without the `$` prefix.
    response_parameters: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Specifies a put integration response's templates.
    response_templates: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Specifies how to handle response payload content type conversions.
    # Supported values are `CONVERT_TO_BINARY` and `CONVERT_TO_TEXT`, with the
    # following behaviors:

    #   * `CONVERT_TO_BINARY`: Converts a response payload from a Base64-encoded string to the corresponding binary blob.

    #   * `CONVERT_TO_TEXT`: Converts a response payload from a binary blob to a Base64-encoded string.

    # If this property is not defined, the response payload will be passed
    # through from the integration response to the method response without
    # modification.
    content_handling: typing.Union[str, "ContentHandlingStrategy"
                                  ] = dataclasses.field(
                                      default=ShapeBase.NOT_SET,
                                  )


@dataclasses.dataclass
class PutMethodRequest(ShapeBase):
    """
    Request to add a method to an existing Resource resource.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "rest_api_id",
                "restApiId",
                TypeInfo(str),
            ),
            (
                "resource_id",
                "resourceId",
                TypeInfo(str),
            ),
            (
                "http_method",
                "httpMethod",
                TypeInfo(str),
            ),
            (
                "authorization_type",
                "authorizationType",
                TypeInfo(str),
            ),
            (
                "authorizer_id",
                "authorizerId",
                TypeInfo(str),
            ),
            (
                "api_key_required",
                "apiKeyRequired",
                TypeInfo(bool),
            ),
            (
                "operation_name",
                "operationName",
                TypeInfo(str),
            ),
            (
                "request_parameters",
                "requestParameters",
                TypeInfo(typing.Dict[str, bool]),
            ),
            (
                "request_models",
                "requestModels",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "request_validator_id",
                "requestValidatorId",
                TypeInfo(str),
            ),
            (
                "authorization_scopes",
                "authorizationScopes",
                TypeInfo(typing.List[str]),
            ),
        ]

    # [Required] The string identifier of the associated RestApi.
    rest_api_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # [Required] The Resource identifier for the new Method resource.
    resource_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # [Required] Specifies the method request's HTTP method type.
    http_method: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # [Required] The method's authorization type. Valid values are `NONE` for
    # open access, `AWS_IAM` for using AWS IAM permissions, `CUSTOM` for using a
    # custom authorizer, or `COGNITO_USER_POOLS` for using a Cognito user pool.
    authorization_type: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Specifies the identifier of an Authorizer to use on this Method, if the
    # type is CUSTOM or COGNITO_USER_POOLS. The authorizer identifier is
    # generated by API Gateway when you created the authorizer.
    authorizer_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Specifies whether the method required a valid ApiKey.
    api_key_required: bool = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A human-friendly operation identifier for the method. For example, you can
    # assign the `operationName` of `ListPets` for the `GET /pets` method in
    # [PetStore](http://petstore-demo-endpoint.execute-api.com/petstore/pets)
    # example.
    operation_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A key-value map defining required or optional method request parameters
    # that can be accepted by API Gateway. A key defines a method request
    # parameter name matching the pattern of `method.request.{location}.{name}`,
    # where `location` is `querystring`, `path`, or `header` and `name` is a
    # valid and unique parameter name. The value associated with the key is a
    # Boolean flag indicating whether the parameter is required (`true`) or
    # optional (`false`). The method request parameter names defined here are
    # available in Integration to be mapped to integration request parameters or
    # body-mapping templates.
    request_parameters: typing.Dict[str, bool] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Specifies the Model resources used for the request's content type. Request
    # models are represented as a key/value map, with a content type as the key
    # and a Model name as the value.
    request_models: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The identifier of a RequestValidator for validating the method request.
    request_validator_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A list of authorization scopes configured on the method. The scopes are
    # used with a `COGNITO_USER_POOLS` authorizer to authorize the method
    # invocation. The authorization works by matching the method scopes against
    # the scopes parsed from the access token in the incoming request. The method
    # invocation is authorized if any method scopes matches a claimed scope in
    # the access token. Otherwise, the invocation is not authorized. When the
    # method scope is configured, the client must provide an access token instead
    # of an identity token for authorization purposes.
    authorization_scopes: typing.List[str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class PutMethodResponseRequest(ShapeBase):
    """
    Request to add a MethodResponse to an existing Method resource.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "rest_api_id",
                "restApiId",
                TypeInfo(str),
            ),
            (
                "resource_id",
                "resourceId",
                TypeInfo(str),
            ),
            (
                "http_method",
                "httpMethod",
                TypeInfo(str),
            ),
            (
                "status_code",
                "statusCode",
                TypeInfo(str),
            ),
            (
                "response_parameters",
                "responseParameters",
                TypeInfo(typing.Dict[str, bool]),
            ),
            (
                "response_models",
                "responseModels",
                TypeInfo(typing.Dict[str, str]),
            ),
        ]

    # [Required] The string identifier of the associated RestApi.
    rest_api_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # [Required] The Resource identifier for the Method resource.
    resource_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # [Required] The HTTP verb of the Method resource.
    http_method: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # [Required] The method response's status code.
    status_code: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A key-value map specifying required or optional response parameters that
    # API Gateway can send back to the caller. A key defines a method response
    # header name and the associated value is a Boolean flag indicating whether
    # the method response parameter is required or not. The method response
    # header names must match the pattern of `method.response.header.{name}`,
    # where `name` is a valid and unique header name. The response parameter
    # names defined here are available in the integration response to be mapped
    # from an integration response header expressed in
    # `integration.response.header.{name}`, a static value enclosed within a pair
    # of single quotes (e.g., `'application/json'`), or a JSON expression from
    # the back-end response payload in the form of
    # `integration.response.body.{JSON-expression}`, where `JSON-expression` is a
    # valid JSON expression without the `$` prefix.)
    response_parameters: typing.Dict[str, bool] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Specifies the Model resources used for the response's content type.
    # Response models are represented as a key/value map, with a content type as
    # the key and a Model name as the value.
    response_models: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


class PutMode(str):
    merge = "merge"
    overwrite = "overwrite"


@dataclasses.dataclass
class PutRestApiRequest(ShapeBase):
    """
    A PUT request to update an existing API, with external API definitions specified
    as the request body.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "rest_api_id",
                "restApiId",
                TypeInfo(str),
            ),
            (
                "body",
                "body",
                TypeInfo(typing.Any),
            ),
            (
                "mode",
                "mode",
                TypeInfo(typing.Union[str, PutMode]),
            ),
            (
                "fail_on_warnings",
                "failOnWarnings",
                TypeInfo(bool),
            ),
            (
                "parameters",
                "parameters",
                TypeInfo(typing.Dict[str, str]),
            ),
        ]

    # [Required] The string identifier of the associated RestApi.
    rest_api_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # [Required] The PUT request body containing external API definitions.
    # Currently, only Swagger definition JSON files are supported. The maximum
    # size of the API definition file is 2MB.
    body: typing.Any = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The `mode` query parameter to specify the update mode. Valid values are
    # "merge" and "overwrite". By default, the update mode is "merge".
    mode: typing.Union[str, "PutMode"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A query parameter to indicate whether to rollback the API update (`true`)
    # or not (`false`) when a warning is encountered. The default value is
    # `false`.
    fail_on_warnings: bool = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Custom header parameters as part of the request. For example, to exclude
    # DocumentationParts from an imported API, set `ignore=documentation` as a
    # `parameters` value, as in the AWS CLI command of `aws apigateway import-
    # rest-api --parameters ignore=documentation --body
    # 'file:///path/to/imported-api-body.json'`.
    parameters: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


class QuotaPeriodType(str):
    DAY = "DAY"
    WEEK = "WEEK"
    MONTH = "MONTH"


@dataclasses.dataclass
class QuotaSettings(ShapeBase):
    """
    Quotas configured for a usage plan.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "limit",
                "limit",
                TypeInfo(int),
            ),
            (
                "offset",
                "offset",
                TypeInfo(int),
            ),
            (
                "period",
                "period",
                TypeInfo(typing.Union[str, QuotaPeriodType]),
            ),
        ]

    # The maximum number of requests that can be made in a given time period.
    limit: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The number of requests subtracted from the given limit in the initial time
    # period.
    offset: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The time period in which the limit applies. Valid values are "DAY", "WEEK"
    # or "MONTH".
    period: typing.Union[str, "QuotaPeriodType"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class RequestValidator(OutputShapeBase):
    """
    A set of validation rules for incoming Method requests.

    In Swagger, a RequestValidator of an API is defined by the [x-amazon-apigateway-
    request-
    validators.requestValidator](http://docs.aws.amazon.com/apigateway/latest/developerguide/api-
    gateway-swagger-extensions.html#api-gateway-swagger-extensions-request-
    validators.requestValidator.html) object. It the referenced using the [x-amazon-
    apigateway-request-
    validator](http://docs.aws.amazon.com/apigateway/latest/developerguide/api-
    gateway-swagger-extensions.html#api-gateway-swagger-extensions-request-
    validator) property.

    [Enable Basic Request Validation in API
    Gateway](http://docs.aws.amazon.com/apigateway/latest/developerguide/api-
    gateway-method-request-validation.html)
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
                "id",
                "id",
                TypeInfo(str),
            ),
            (
                "name",
                "name",
                TypeInfo(str),
            ),
            (
                "validate_request_body",
                "validateRequestBody",
                TypeInfo(bool),
            ),
            (
                "validate_request_parameters",
                "validateRequestParameters",
                TypeInfo(bool),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The identifier of this RequestValidator.
    id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The name of this RequestValidator
    name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A Boolean flag to indicate whether to validate a request body according to
    # the configured Model schema.
    validate_request_body: bool = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A Boolean flag to indicate whether to validate request parameters (`true`)
    # or not (`false`).
    validate_request_parameters: bool = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class RequestValidators(OutputShapeBase):
    """
    A collection of RequestValidator resources of a given RestApi.

    In Swagger, the RequestValidators of an API is defined by the [x-amazon-
    apigateway-request-
    validators](http://docs.aws.amazon.com/apigateway/latest/developerguide/api-
    gateway-swagger-extensions.html#api-gateway-swagger-extensions-request-
    validators.html) extension.

    [Enable Basic Request Validation in API
    Gateway](http://docs.aws.amazon.com/apigateway/latest/developerguide/api-
    gateway-method-request-validation.html)
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
                "position",
                "position",
                TypeInfo(str),
            ),
            (
                "items",
                "items",
                TypeInfo(typing.List[RequestValidator]),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )
    position: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The current page of elements from this collection.
    items: typing.List["RequestValidator"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class Resource(OutputShapeBase):
    """
    Represents an API resource.

    [Create an API](http://docs.aws.amazon.com/apigateway/latest/developerguide/how-
    to-create-api.html)
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
                "id",
                "id",
                TypeInfo(str),
            ),
            (
                "parent_id",
                "parentId",
                TypeInfo(str),
            ),
            (
                "path_part",
                "pathPart",
                TypeInfo(str),
            ),
            (
                "path",
                "path",
                TypeInfo(str),
            ),
            (
                "resource_methods",
                "resourceMethods",
                TypeInfo(typing.Dict[str, Method]),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The resource's identifier.
    id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The parent resource's identifier.
    parent_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The last path segment for this resource.
    path_part: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The full path for this resource.
    path: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Gets an API resource's method of a given HTTP verb.

    # The resource methods are a map of methods indexed by methods' HTTP verbs
    # enabled on the resource. This method map is included in the `200 OK`
    # response of the `GET /restapis/{restapi_id}/resources/{resource_id}` or
    # `GET /restapis/{restapi_id}/resources/{resource_id}?embed=methods` request.

    # #### Example: Get the GET method of an API resource

    # ##### Request

    #     GET /restapis/fugvjdxtri/resources/3kzxbg5sa2/methods/GET HTTP/1.1 Content-Type: application/json Host: apigateway.us-east-1.amazonaws.com X-Amz-Date: 20170223T031827Z Authorization: AWS4-HMAC-SHA256 Credential={access_key_ID}/20170223/us-east-1/apigateway/aws4_request, SignedHeaders=content-type;host;x-amz-date, Signature={sig4_hash}

    # ##### Response

    #     { "_links": { "curies": [ { "href": "http://docs.aws.amazon.com/apigateway/latest/developerguide/restapi-integration-{rel}.html", "name": "integration", "templated": true }, { "href": "http://docs.aws.amazon.com/apigateway/latest/developerguide/restapi-integration-response-{rel}.html", "name": "integrationresponse", "templated": true }, { "href": "http://docs.aws.amazon.com/apigateway/latest/developerguide/restapi-method-{rel}.html", "name": "method", "templated": true }, { "href": "http://docs.aws.amazon.com/apigateway/latest/developerguide/restapi-method-response-{rel}.html", "name": "methodresponse", "templated": true } ], "self": { "href": "/restapis/fugvjdxtri/resources/3kzxbg5sa2/methods/GET", "name": "GET", "title": "GET" }, "integration:put": { "href": "/restapis/fugvjdxtri/resources/3kzxbg5sa2/methods/GET/integration" }, "method:delete": { "href": "/restapis/fugvjdxtri/resources/3kzxbg5sa2/methods/GET" }, "method:integration": { "href": "/restapis/fugvjdxtri/resources/3kzxbg5sa2/methods/GET/integration" }, "method:responses": { "href": "/restapis/fugvjdxtri/resources/3kzxbg5sa2/methods/GET/responses/200", "name": "200", "title": "200" }, "method:update": { "href": "/restapis/fugvjdxtri/resources/3kzxbg5sa2/methods/GET" }, "methodresponse:put": { "href": "/restapis/fugvjdxtri/resources/3kzxbg5sa2/methods/GET/responses/{status_code}", "templated": true } }, "apiKeyRequired": false, "authorizationType": "NONE", "httpMethod": "GET", "_embedded": { "method:integration": { "_links": { "self": { "href": "/restapis/fugvjdxtri/resources/3kzxbg5sa2/methods/GET/integration" }, "integration:delete": { "href": "/restapis/fugvjdxtri/resources/3kzxbg5sa2/methods/GET/integration" }, "integration:responses": { "href": "/restapis/fugvjdxtri/resources/3kzxbg5sa2/methods/GET/integration/responses/200", "name": "200", "title": "200" }, "integration:update": { "href": "/restapis/fugvjdxtri/resources/3kzxbg5sa2/methods/GET/integration" }, "integrationresponse:put": { "href": "/restapis/fugvjdxtri/resources/3kzxbg5sa2/methods/GET/integration/responses/{status_code}", "templated": true } }, "cacheKeyParameters": [], "cacheNamespace": "3kzxbg5sa2", "credentials": "arn:aws:iam::123456789012:role/apigAwsProxyRole", "httpMethod": "POST", "passthroughBehavior": "WHEN_NO_MATCH", "requestParameters": { "integration.request.header.Content-Type": "'application/x-amz-json-1.1'" }, "requestTemplates": { "application/json": "{\n}" }, "type": "AWS", "uri": "arn:aws:apigateway:us-east-1:kinesis:action/ListStreams", "_embedded": { "integration:responses": { "_links": { "self": { "href": "/restapis/fugvjdxtri/resources/3kzxbg5sa2/methods/GET/integration/responses/200", "name": "200", "title": "200" }, "integrationresponse:delete": { "href": "/restapis/fugvjdxtri/resources/3kzxbg5sa2/methods/GET/integration/responses/200" }, "integrationresponse:update": { "href": "/restapis/fugvjdxtri/resources/3kzxbg5sa2/methods/GET/integration/responses/200" } }, "responseParameters": { "method.response.header.Content-Type": "'application/xml'" }, "responseTemplates": { "application/json": "$util.urlDecode(\"%3CkinesisStreams%3E#foreach($stream in $input.path('$.StreamNames'))%3Cstream%3E%3Cname%3E$stream%3C/name%3E%3C/stream%3E#end%3C/kinesisStreams%3E\")\n" }, "statusCode": "200" } } }, "method:responses": { "_links": { "self": { "href": "/restapis/fugvjdxtri/resources/3kzxbg5sa2/methods/GET/responses/200", "name": "200", "title": "200" }, "methodresponse:delete": { "href": "/restapis/fugvjdxtri/resources/3kzxbg5sa2/methods/GET/responses/200" }, "methodresponse:update": { "href": "/restapis/fugvjdxtri/resources/3kzxbg5sa2/methods/GET/responses/200" } }, "responseModels": { "application/json": "Empty" }, "responseParameters": { "method.response.header.Content-Type": false }, "statusCode": "200" } } }

    # If the `OPTIONS` is enabled on the resource, you can follow the example
    # here to get that method. Just replace the `GET` of the last path segment in
    # the request URL with `OPTIONS`.
    resource_methods: typing.Dict[str, "Method"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class Resources(OutputShapeBase):
    """
    Represents a collection of Resource resources.

    [Create an API](http://docs.aws.amazon.com/apigateway/latest/developerguide/how-
    to-create-api.html)
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
                "position",
                "position",
                TypeInfo(str),
            ),
            (
                "items",
                "items",
                TypeInfo(typing.List[Resource]),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )
    position: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The current page of elements from this collection.
    items: typing.List["Resource"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    def paginate(self, ) -> typing.Generator["Resources", None, None]:
        yield from super()._paginate()


@dataclasses.dataclass
class RestApi(OutputShapeBase):
    """
    Represents a REST API.

    [Create an API](http://docs.aws.amazon.com/apigateway/latest/developerguide/how-
    to-create-api.html)
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
                "id",
                "id",
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
                "created_date",
                "createdDate",
                TypeInfo(datetime.datetime),
            ),
            (
                "version",
                "version",
                TypeInfo(str),
            ),
            (
                "warnings",
                "warnings",
                TypeInfo(typing.List[str]),
            ),
            (
                "binary_media_types",
                "binaryMediaTypes",
                TypeInfo(typing.List[str]),
            ),
            (
                "minimum_compression_size",
                "minimumCompressionSize",
                TypeInfo(int),
            ),
            (
                "api_key_source",
                "apiKeySource",
                TypeInfo(typing.Union[str, ApiKeySourceType]),
            ),
            (
                "endpoint_configuration",
                "endpointConfiguration",
                TypeInfo(EndpointConfiguration),
            ),
            (
                "policy",
                "policy",
                TypeInfo(str),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The API's identifier. This identifier is unique across all of your APIs in
    # API Gateway.
    id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The API's name.
    name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The API's description.
    description: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The timestamp when the API was created.
    created_date: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A version identifier for the API.
    version: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The warning messages reported when `failonwarnings` is turned on during API
    # import.
    warnings: typing.List[str] = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The list of binary media types supported by the RestApi. By default, the
    # RestApi supports only UTF-8-encoded text payloads.
    binary_media_types: typing.List[str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A nullable integer that is used to enable compression (with non-negative
    # between 0 and 10485760 (10M) bytes, inclusive) or disable compression (with
    # a null value) on an API. When compression is enabled, compression or
    # decompression is not applied on the payload if the payload size is smaller
    # than this value. Setting it to zero allows compression for any payload
    # size.
    minimum_compression_size: int = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The source of the API key for metering requests according to a usage plan.
    # Valid values are:

    #   * `HEADER` to read the API key from the `X-API-Key` header of a request.
    #   * `AUTHORIZER` to read the API key from the `UsageIdentifierKey` from a custom authorizer.
    api_key_source: typing.Union[str, "ApiKeySourceType"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The endpoint configuration of this RestApi showing the endpoint types of
    # the API.
    endpoint_configuration: "EndpointConfiguration" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A stringified JSON policy document that applies to this RestApi regardless
    # of the caller and Method configuration.
    policy: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class RestApis(OutputShapeBase):
    """
    Contains references to your APIs and links that guide you in how to interact
    with your collection. A collection offers a paginated view of your APIs.

    [Create an API](http://docs.aws.amazon.com/apigateway/latest/developerguide/how-
    to-create-api.html)
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
                "position",
                "position",
                TypeInfo(str),
            ),
            (
                "items",
                "items",
                TypeInfo(typing.List[RestApi]),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )
    position: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The current page of elements from this collection.
    items: typing.List["RestApi"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    def paginate(self, ) -> typing.Generator["RestApis", None, None]:
        yield from super()._paginate()


@dataclasses.dataclass
class SdkConfigurationProperty(ShapeBase):
    """
    A configuration property of an SDK type.
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
                "friendly_name",
                "friendlyName",
                TypeInfo(str),
            ),
            (
                "description",
                "description",
                TypeInfo(str),
            ),
            (
                "required",
                "required",
                TypeInfo(bool),
            ),
            (
                "default_value",
                "defaultValue",
                TypeInfo(str),
            ),
        ]

    # The name of a an SdkType configuration property.
    name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The user-friendly name of an SdkType configuration property.
    friendly_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The description of an SdkType configuration property.
    description: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A boolean flag of an SdkType configuration property to indicate if the
    # associated SDK configuration property is required (`true`) or not
    # (`false`).
    required: bool = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The default value of an SdkType configuration property.
    default_value: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class SdkResponse(OutputShapeBase):
    """
    The binary blob response to GetSdk, which contains the generated SDK.
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
                "content_type",
                "contentType",
                TypeInfo(str),
            ),
            (
                "content_disposition",
                "contentDisposition",
                TypeInfo(str),
            ),
            (
                "body",
                "body",
                TypeInfo(typing.Any),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The content-type header value in the HTTP response.
    content_type: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The content-disposition header value in the HTTP response.
    content_disposition: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The binary blob response to GetSdk, which contains the generated SDK.
    body: typing.Any = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class SdkType(OutputShapeBase):
    """
    A type of SDK that API Gateway can generate.
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
                "id",
                "id",
                TypeInfo(str),
            ),
            (
                "friendly_name",
                "friendlyName",
                TypeInfo(str),
            ),
            (
                "description",
                "description",
                TypeInfo(str),
            ),
            (
                "configuration_properties",
                "configurationProperties",
                TypeInfo(typing.List[SdkConfigurationProperty]),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The identifier of an SdkType instance.
    id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The user-friendly name of an SdkType instance.
    friendly_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The description of an SdkType.
    description: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A list of configuration properties of an SdkType.
    configuration_properties: typing.List["SdkConfigurationProperty"
                                         ] = dataclasses.field(
                                             default=ShapeBase.NOT_SET,
                                         )


@dataclasses.dataclass
class SdkTypes(OutputShapeBase):
    """
    The collection of SdkType instances.
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
                "position",
                "position",
                TypeInfo(str),
            ),
            (
                "items",
                "items",
                TypeInfo(typing.List[SdkType]),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )
    position: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The current page of elements from this collection.
    items: typing.List["SdkType"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class ServiceUnavailableException(ShapeBase):
    """
    The requested service is not available. For details see the accompanying error
    message. Retry after the specified time period.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "retry_after_seconds",
                "retryAfterSeconds",
                TypeInfo(str),
            ),
            (
                "message",
                "message",
                TypeInfo(str),
            ),
        ]

    retry_after_seconds: str = dataclasses.field(default=ShapeBase.NOT_SET, )
    message: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class Stage(OutputShapeBase):
    """
    Represents a unique identifier for a version of a deployed RestApi that is
    callable by users.

    [Deploy an API](http://docs.aws.amazon.com/apigateway/latest/developerguide/how-
    to-deploy-api.html)
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
                "deployment_id",
                "deploymentId",
                TypeInfo(str),
            ),
            (
                "client_certificate_id",
                "clientCertificateId",
                TypeInfo(str),
            ),
            (
                "stage_name",
                "stageName",
                TypeInfo(str),
            ),
            (
                "description",
                "description",
                TypeInfo(str),
            ),
            (
                "cache_cluster_enabled",
                "cacheClusterEnabled",
                TypeInfo(bool),
            ),
            (
                "cache_cluster_size",
                "cacheClusterSize",
                TypeInfo(typing.Union[str, CacheClusterSize]),
            ),
            (
                "cache_cluster_status",
                "cacheClusterStatus",
                TypeInfo(typing.Union[str, CacheClusterStatus]),
            ),
            (
                "method_settings",
                "methodSettings",
                TypeInfo(typing.Dict[str, MethodSetting]),
            ),
            (
                "variables",
                "variables",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "documentation_version",
                "documentationVersion",
                TypeInfo(str),
            ),
            (
                "access_log_settings",
                "accessLogSettings",
                TypeInfo(AccessLogSettings),
            ),
            (
                "canary_settings",
                "canarySettings",
                TypeInfo(CanarySettings),
            ),
            (
                "tracing_enabled",
                "tracingEnabled",
                TypeInfo(bool),
            ),
            (
                "tags",
                "tags",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "created_date",
                "createdDate",
                TypeInfo(datetime.datetime),
            ),
            (
                "last_updated_date",
                "lastUpdatedDate",
                TypeInfo(datetime.datetime),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The identifier of the Deployment that the stage points to.
    deployment_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The identifier of a client certificate for an API stage.
    client_certificate_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The name of the stage is the first path segment in the Uniform Resource
    # Identifier (URI) of a call to API Gateway.
    stage_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The stage's description.
    description: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Specifies whether a cache cluster is enabled for the stage.
    cache_cluster_enabled: bool = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The size of the cache cluster for the stage, if enabled.
    cache_cluster_size: typing.Union[str, "CacheClusterSize"
                                    ] = dataclasses.field(
                                        default=ShapeBase.NOT_SET,
                                    )

    # The status of the cache cluster for the stage, if enabled.
    cache_cluster_status: typing.Union[str, "CacheClusterStatus"
                                      ] = dataclasses.field(
                                          default=ShapeBase.NOT_SET,
                                      )

    # A map that defines the method settings for a Stage resource. Keys
    # (designated as `/{method_setting_key` below) are method paths defined as
    # `{resource_path}/{http_method}` for an individual method override, or
    # `/\*/\*` for overriding all methods in the stage.
    method_settings: typing.Dict[str, "MethodSetting"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A map that defines the stage variables for a Stage resource. Variable names
    # can have alphanumeric and underscore characters, and the values must match
    # `[A-Za-z0-9-._~:/?#&=,]+`.
    variables: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The version of the associated API documentation.
    documentation_version: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Settings for logging access in this stage.
    access_log_settings: "AccessLogSettings" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Settings for the canary deployment in this stage.
    canary_settings: "CanarySettings" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Specifies whether active tracing with X-ray is enabled for the Stage.
    tracing_enabled: bool = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The collection of tags. Each tag element is associated with a given
    # resource.
    tags: typing.Dict[str, str] = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The timestamp when the stage was created.
    created_date: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The timestamp when the stage last updated.
    last_updated_date: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class StageKey(ShapeBase):
    """
    A reference to a unique stage identified in the format `{restApiId}/{stage}`.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "rest_api_id",
                "restApiId",
                TypeInfo(str),
            ),
            (
                "stage_name",
                "stageName",
                TypeInfo(str),
            ),
        ]

    # The string identifier of the associated RestApi.
    rest_api_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The stage name associated with the stage key.
    stage_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class Stages(OutputShapeBase):
    """
    A list of Stage resources that are associated with the ApiKey resource.

    [Deploying API in
    Stages](http://docs.aws.amazon.com/apigateway/latest/developerguide/stages.html)
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
                "item",
                "item",
                TypeInfo(typing.List[Stage]),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The current page of elements from this collection.
    item: typing.List["Stage"] = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class TagResourceRequest(ShapeBase):
    """
    Adds or updates a tag on a given resource.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "resource_arn",
                "resourceArn",
                TypeInfo(str),
            ),
            (
                "tags",
                "tags",
                TypeInfo(typing.Dict[str, str]),
            ),
        ]

    # [Required] The ARN of a resource that can be tagged. The resource ARN must
    # be URL-encoded. At present, Stage is the only taggable resource.
    resource_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # [Required] The key-value map of strings. The valid character set is
    # [a-zA-Z+-=._:/]. The tag key can be up to 128 characters and must not start
    # with `aws:`. The tag value can be up to 256 characters.
    tags: typing.Dict[str, str] = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class Tags(OutputShapeBase):
    """
    The collection of tags. Each tag element is associated with a given resource.
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
                "tags",
                "tags",
                TypeInfo(typing.Dict[str, str]),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The collection of tags. Each tag element is associated with a given
    # resource.
    tags: typing.Dict[str, str] = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class Template(OutputShapeBase):
    """
    Represents a mapping template used to transform a payload.

    [Mapping
    Templates](http://docs.aws.amazon.com/apigateway/latest/developerguide/models-
    mappings.html#models-mappings-mappings)
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
                "value",
                "value",
                TypeInfo(str),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The Apache [Velocity Template Language
    # (VTL)](http://velocity.apache.org/engine/devel/vtl-reference-guide.html)
    # template content used for the template resource.
    value: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class TestInvokeAuthorizerRequest(ShapeBase):
    """
    Make a request to simulate the execution of an Authorizer.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "rest_api_id",
                "restApiId",
                TypeInfo(str),
            ),
            (
                "authorizer_id",
                "authorizerId",
                TypeInfo(str),
            ),
            (
                "headers",
                "headers",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "path_with_query_string",
                "pathWithQueryString",
                TypeInfo(str),
            ),
            (
                "body",
                "body",
                TypeInfo(str),
            ),
            (
                "stage_variables",
                "stageVariables",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "additional_context",
                "additionalContext",
                TypeInfo(typing.Dict[str, str]),
            ),
        ]

    # [Required] The string identifier of the associated RestApi.
    rest_api_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # [Required] Specifies a test invoke authorizer request's Authorizer ID.
    authorizer_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # [Required] A key-value map of headers to simulate an incoming invocation
    # request. This is where the incoming authorization token, or identity
    # source, should be specified.
    headers: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # [Optional] The URI path, including query string, of the simulated
    # invocation request. Use this to specify path parameters and query string
    # parameters.
    path_with_query_string: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # [Optional] The simulated request body of an incoming invocation request.
    body: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A key-value map of stage variables to simulate an invocation on a deployed
    # Stage.
    stage_variables: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # [Optional] A key-value map of additional context variables.
    additional_context: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class TestInvokeAuthorizerResponse(OutputShapeBase):
    """
    Represents the response of the test invoke request for a custom Authorizer
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
                "client_status",
                "clientStatus",
                TypeInfo(int),
            ),
            (
                "log",
                "log",
                TypeInfo(str),
            ),
            (
                "latency",
                "latency",
                TypeInfo(int),
            ),
            (
                "principal_id",
                "principalId",
                TypeInfo(str),
            ),
            (
                "policy",
                "policy",
                TypeInfo(str),
            ),
            (
                "authorization",
                "authorization",
                TypeInfo(typing.Dict[str, typing.List[str]]),
            ),
            (
                "claims",
                "claims",
                TypeInfo(typing.Dict[str, str]),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The HTTP status code that the client would have received. Value is 0 if the
    # authorizer succeeded.
    client_status: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The API Gateway execution log for the test authorizer request.
    log: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The execution latency of the test authorizer request.
    latency: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The principal identity returned by the Authorizer
    principal_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The JSON policy document returned by the Authorizer
    policy: str = dataclasses.field(default=ShapeBase.NOT_SET, )
    authorization: typing.Dict[str, typing.List[str]] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The [open identity claims](http://openid.net/specs/openid-connect-
    # core-1_0.html#StandardClaims), with any supported custom attributes,
    # returned from the Cognito Your User Pool configured for the API.
    claims: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class TestInvokeMethodRequest(ShapeBase):
    """
    Make a request to simulate the execution of a Method.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "rest_api_id",
                "restApiId",
                TypeInfo(str),
            ),
            (
                "resource_id",
                "resourceId",
                TypeInfo(str),
            ),
            (
                "http_method",
                "httpMethod",
                TypeInfo(str),
            ),
            (
                "path_with_query_string",
                "pathWithQueryString",
                TypeInfo(str),
            ),
            (
                "body",
                "body",
                TypeInfo(str),
            ),
            (
                "headers",
                "headers",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "client_certificate_id",
                "clientCertificateId",
                TypeInfo(str),
            ),
            (
                "stage_variables",
                "stageVariables",
                TypeInfo(typing.Dict[str, str]),
            ),
        ]

    # [Required] The string identifier of the associated RestApi.
    rest_api_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # [Required] Specifies a test invoke method request's resource ID.
    resource_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # [Required] Specifies a test invoke method request's HTTP method.
    http_method: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The URI path, including query string, of the simulated invocation request.
    # Use this to specify path parameters and query string parameters.
    path_with_query_string: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The simulated request body of an incoming invocation request.
    body: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A key-value map of headers to simulate an incoming invocation request.
    headers: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A ClientCertificate identifier to use in the test invocation. API Gateway
    # will use the certificate when making the HTTPS request to the defined back-
    # end endpoint.
    client_certificate_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A key-value map of stage variables to simulate an invocation on a deployed
    # Stage.
    stage_variables: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class TestInvokeMethodResponse(OutputShapeBase):
    """
    Represents the response of the test invoke request in the HTTP method.

    [Test API using the API Gateway
    console](http://docs.aws.amazon.com/apigateway/latest/developerguide/how-to-
    test-method.html#how-to-test-method-console)
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
                "status",
                "status",
                TypeInfo(int),
            ),
            (
                "body",
                "body",
                TypeInfo(str),
            ),
            (
                "headers",
                "headers",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "log",
                "log",
                TypeInfo(str),
            ),
            (
                "latency",
                "latency",
                TypeInfo(int),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The HTTP status code.
    status: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The body of the HTTP response.
    body: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The headers of the HTTP response.
    headers: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The API Gateway execution log for the test invoke request.
    log: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The execution latency of the test invoke request.
    latency: int = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ThrottleSettings(ShapeBase):
    """
    The API request rate limits.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "burst_limit",
                "burstLimit",
                TypeInfo(int),
            ),
            (
                "rate_limit",
                "rateLimit",
                TypeInfo(float),
            ),
        ]

    # The API request burst limit, the maximum rate limit over a time ranging
    # from one to a few seconds, depending upon whether the underlying token
    # bucket is at its full capacity.
    burst_limit: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The API request steady-state rate limit.
    rate_limit: float = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class TooManyRequestsException(ShapeBase):
    """
    The request has reached its throttling limit. Retry after the specified time
    period.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "retry_after_seconds",
                "retryAfterSeconds",
                TypeInfo(str),
            ),
            (
                "message",
                "message",
                TypeInfo(str),
            ),
        ]

    retry_after_seconds: str = dataclasses.field(default=ShapeBase.NOT_SET, )
    message: str = dataclasses.field(default=ShapeBase.NOT_SET, )


class UnauthorizedCacheControlHeaderStrategy(str):
    FAIL_WITH_403 = "FAIL_WITH_403"
    SUCCEED_WITH_RESPONSE_HEADER = "SUCCEED_WITH_RESPONSE_HEADER"
    SUCCEED_WITHOUT_RESPONSE_HEADER = "SUCCEED_WITHOUT_RESPONSE_HEADER"


@dataclasses.dataclass
class UnauthorizedException(ShapeBase):
    """
    The request is denied because the caller has insufficient permissions.
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
    """
    Removes a tag from a given resource.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "resource_arn",
                "resourceArn",
                TypeInfo(str),
            ),
            (
                "tag_keys",
                "tagKeys",
                TypeInfo(typing.List[str]),
            ),
        ]

    # [Required] The ARN of a resource that can be tagged. The resource ARN must
    # be URL-encoded. At present, Stage is the only taggable resource.
    resource_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # [Required] The Tag keys to delete.
    tag_keys: typing.List[str] = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class UpdateAccountRequest(ShapeBase):
    """
    Requests API Gateway to change information about the current Account resource.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "patch_operations",
                "patchOperations",
                TypeInfo(typing.List[PatchOperation]),
            ),
        ]

    # A list of update operations to be applied to the specified resource and in
    # the order specified in this list.
    patch_operations: typing.List["PatchOperation"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class UpdateApiKeyRequest(ShapeBase):
    """
    A request to change information about an ApiKey resource.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "api_key",
                "apiKey",
                TypeInfo(str),
            ),
            (
                "patch_operations",
                "patchOperations",
                TypeInfo(typing.List[PatchOperation]),
            ),
        ]

    # [Required] The identifier of the ApiKey resource to be updated.
    api_key: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A list of update operations to be applied to the specified resource and in
    # the order specified in this list.
    patch_operations: typing.List["PatchOperation"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class UpdateAuthorizerRequest(ShapeBase):
    """
    Request to update an existing Authorizer resource.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "rest_api_id",
                "restApiId",
                TypeInfo(str),
            ),
            (
                "authorizer_id",
                "authorizerId",
                TypeInfo(str),
            ),
            (
                "patch_operations",
                "patchOperations",
                TypeInfo(typing.List[PatchOperation]),
            ),
        ]

    # [Required] The string identifier of the associated RestApi.
    rest_api_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # [Required] The identifier of the Authorizer resource.
    authorizer_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A list of update operations to be applied to the specified resource and in
    # the order specified in this list.
    patch_operations: typing.List["PatchOperation"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class UpdateBasePathMappingRequest(ShapeBase):
    """
    A request to change information about the BasePathMapping resource.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "domain_name",
                "domainName",
                TypeInfo(str),
            ),
            (
                "base_path",
                "basePath",
                TypeInfo(str),
            ),
            (
                "patch_operations",
                "patchOperations",
                TypeInfo(typing.List[PatchOperation]),
            ),
        ]

    # [Required] The domain name of the BasePathMapping resource to change.
    domain_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # [Required] The base path of the BasePathMapping resource to change.
    base_path: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A list of update operations to be applied to the specified resource and in
    # the order specified in this list.
    patch_operations: typing.List["PatchOperation"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class UpdateClientCertificateRequest(ShapeBase):
    """
    A request to change information about an ClientCertificate resource.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "client_certificate_id",
                "clientCertificateId",
                TypeInfo(str),
            ),
            (
                "patch_operations",
                "patchOperations",
                TypeInfo(typing.List[PatchOperation]),
            ),
        ]

    # [Required] The identifier of the ClientCertificate resource to be updated.
    client_certificate_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A list of update operations to be applied to the specified resource and in
    # the order specified in this list.
    patch_operations: typing.List["PatchOperation"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class UpdateDeploymentRequest(ShapeBase):
    """
    Requests API Gateway to change information about a Deployment resource.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "rest_api_id",
                "restApiId",
                TypeInfo(str),
            ),
            (
                "deployment_id",
                "deploymentId",
                TypeInfo(str),
            ),
            (
                "patch_operations",
                "patchOperations",
                TypeInfo(typing.List[PatchOperation]),
            ),
        ]

    # [Required] The string identifier of the associated RestApi.
    rest_api_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The replacement identifier for the Deployment resource to change
    # information about.
    deployment_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A list of update operations to be applied to the specified resource and in
    # the order specified in this list.
    patch_operations: typing.List["PatchOperation"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class UpdateDocumentationPartRequest(ShapeBase):
    """
    Updates an existing documentation part of a given API.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "rest_api_id",
                "restApiId",
                TypeInfo(str),
            ),
            (
                "documentation_part_id",
                "documentationPartId",
                TypeInfo(str),
            ),
            (
                "patch_operations",
                "patchOperations",
                TypeInfo(typing.List[PatchOperation]),
            ),
        ]

    # [Required] The string identifier of the associated RestApi.
    rest_api_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # [Required] The identifier of the to-be-updated documentation part.
    documentation_part_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A list of update operations to be applied to the specified resource and in
    # the order specified in this list.
    patch_operations: typing.List["PatchOperation"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class UpdateDocumentationVersionRequest(ShapeBase):
    """
    Updates an existing documentation version of an API.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "rest_api_id",
                "restApiId",
                TypeInfo(str),
            ),
            (
                "documentation_version",
                "documentationVersion",
                TypeInfo(str),
            ),
            (
                "patch_operations",
                "patchOperations",
                TypeInfo(typing.List[PatchOperation]),
            ),
        ]

    # [Required] The string identifier of the associated RestApi..
    rest_api_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # [Required] The version identifier of the to-be-updated documentation
    # version.
    documentation_version: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A list of update operations to be applied to the specified resource and in
    # the order specified in this list.
    patch_operations: typing.List["PatchOperation"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class UpdateDomainNameRequest(ShapeBase):
    """
    A request to change information about the DomainName resource.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "domain_name",
                "domainName",
                TypeInfo(str),
            ),
            (
                "patch_operations",
                "patchOperations",
                TypeInfo(typing.List[PatchOperation]),
            ),
        ]

    # [Required] The name of the DomainName resource to be changed.
    domain_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A list of update operations to be applied to the specified resource and in
    # the order specified in this list.
    patch_operations: typing.List["PatchOperation"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class UpdateGatewayResponseRequest(ShapeBase):
    """
    Updates a GatewayResponse of a specified response type on the given RestApi.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "rest_api_id",
                "restApiId",
                TypeInfo(str),
            ),
            (
                "response_type",
                "responseType",
                TypeInfo(typing.Union[str, GatewayResponseType]),
            ),
            (
                "patch_operations",
                "patchOperations",
                TypeInfo(typing.List[PatchOperation]),
            ),
        ]

    # [Required] The string identifier of the associated RestApi.
    rest_api_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # [Required]

    # The response type of the associated GatewayResponse. Valid values are

    #   * ACCESS_DENIED
    #   * API_CONFIGURATION_ERROR
    #   * AUTHORIZER_FAILURE
    #   * AUTHORIZER_CONFIGURATION_ERROR
    #   * BAD_REQUEST_PARAMETERS
    #   * BAD_REQUEST_BODY
    #   * DEFAULT_4XX
    #   * DEFAULT_5XX
    #   * EXPIRED_TOKEN
    #   * INVALID_SIGNATURE
    #   * INTEGRATION_FAILURE
    #   * INTEGRATION_TIMEOUT
    #   * INVALID_API_KEY
    #   * MISSING_AUTHENTICATION_TOKEN
    #   * QUOTA_EXCEEDED
    #   * REQUEST_TOO_LARGE
    #   * RESOURCE_NOT_FOUND
    #   * THROTTLED
    #   * UNAUTHORIZED
    #   * UNSUPPORTED_MEDIA_TYPE
    response_type: typing.Union[str, "GatewayResponseType"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A list of update operations to be applied to the specified resource and in
    # the order specified in this list.
    patch_operations: typing.List["PatchOperation"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class UpdateIntegrationRequest(ShapeBase):
    """
    Represents an update integration request.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "rest_api_id",
                "restApiId",
                TypeInfo(str),
            ),
            (
                "resource_id",
                "resourceId",
                TypeInfo(str),
            ),
            (
                "http_method",
                "httpMethod",
                TypeInfo(str),
            ),
            (
                "patch_operations",
                "patchOperations",
                TypeInfo(typing.List[PatchOperation]),
            ),
        ]

    # [Required] The string identifier of the associated RestApi.
    rest_api_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # [Required] Represents an update integration request's resource identifier.
    resource_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # [Required] Represents an update integration request's HTTP method.
    http_method: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A list of update operations to be applied to the specified resource and in
    # the order specified in this list.
    patch_operations: typing.List["PatchOperation"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class UpdateIntegrationResponseRequest(ShapeBase):
    """
    Represents an update integration response request.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "rest_api_id",
                "restApiId",
                TypeInfo(str),
            ),
            (
                "resource_id",
                "resourceId",
                TypeInfo(str),
            ),
            (
                "http_method",
                "httpMethod",
                TypeInfo(str),
            ),
            (
                "status_code",
                "statusCode",
                TypeInfo(str),
            ),
            (
                "patch_operations",
                "patchOperations",
                TypeInfo(typing.List[PatchOperation]),
            ),
        ]

    # [Required] The string identifier of the associated RestApi.
    rest_api_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # [Required] Specifies an update integration response request's resource
    # identifier.
    resource_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # [Required] Specifies an update integration response request's HTTP method.
    http_method: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # [Required] Specifies an update integration response request's status code.
    status_code: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A list of update operations to be applied to the specified resource and in
    # the order specified in this list.
    patch_operations: typing.List["PatchOperation"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class UpdateMethodRequest(ShapeBase):
    """
    Request to update an existing Method resource.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "rest_api_id",
                "restApiId",
                TypeInfo(str),
            ),
            (
                "resource_id",
                "resourceId",
                TypeInfo(str),
            ),
            (
                "http_method",
                "httpMethod",
                TypeInfo(str),
            ),
            (
                "patch_operations",
                "patchOperations",
                TypeInfo(typing.List[PatchOperation]),
            ),
        ]

    # [Required] The string identifier of the associated RestApi.
    rest_api_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # [Required] The Resource identifier for the Method resource.
    resource_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # [Required] The HTTP verb of the Method resource.
    http_method: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A list of update operations to be applied to the specified resource and in
    # the order specified in this list.
    patch_operations: typing.List["PatchOperation"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class UpdateMethodResponseRequest(ShapeBase):
    """
    A request to update an existing MethodResponse resource.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "rest_api_id",
                "restApiId",
                TypeInfo(str),
            ),
            (
                "resource_id",
                "resourceId",
                TypeInfo(str),
            ),
            (
                "http_method",
                "httpMethod",
                TypeInfo(str),
            ),
            (
                "status_code",
                "statusCode",
                TypeInfo(str),
            ),
            (
                "patch_operations",
                "patchOperations",
                TypeInfo(typing.List[PatchOperation]),
            ),
        ]

    # [Required] The string identifier of the associated RestApi.
    rest_api_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # [Required] The Resource identifier for the MethodResponse resource.
    resource_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # [Required] The HTTP verb of the Method resource.
    http_method: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # [Required] The status code for the MethodResponse resource.
    status_code: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A list of update operations to be applied to the specified resource and in
    # the order specified in this list.
    patch_operations: typing.List["PatchOperation"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class UpdateModelRequest(ShapeBase):
    """
    Request to update an existing model in an existing RestApi resource.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "rest_api_id",
                "restApiId",
                TypeInfo(str),
            ),
            (
                "model_name",
                "modelName",
                TypeInfo(str),
            ),
            (
                "patch_operations",
                "patchOperations",
                TypeInfo(typing.List[PatchOperation]),
            ),
        ]

    # [Required] The string identifier of the associated RestApi.
    rest_api_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # [Required] The name of the model to update.
    model_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A list of update operations to be applied to the specified resource and in
    # the order specified in this list.
    patch_operations: typing.List["PatchOperation"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class UpdateRequestValidatorRequest(ShapeBase):
    """
    Updates a RequestValidator of a given RestApi.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "rest_api_id",
                "restApiId",
                TypeInfo(str),
            ),
            (
                "request_validator_id",
                "requestValidatorId",
                TypeInfo(str),
            ),
            (
                "patch_operations",
                "patchOperations",
                TypeInfo(typing.List[PatchOperation]),
            ),
        ]

    # [Required] The string identifier of the associated RestApi.
    rest_api_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # [Required] The identifier of RequestValidator to be updated.
    request_validator_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A list of update operations to be applied to the specified resource and in
    # the order specified in this list.
    patch_operations: typing.List["PatchOperation"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class UpdateResourceRequest(ShapeBase):
    """
    Request to change information about a Resource resource.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "rest_api_id",
                "restApiId",
                TypeInfo(str),
            ),
            (
                "resource_id",
                "resourceId",
                TypeInfo(str),
            ),
            (
                "patch_operations",
                "patchOperations",
                TypeInfo(typing.List[PatchOperation]),
            ),
        ]

    # [Required] The string identifier of the associated RestApi.
    rest_api_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # [Required] The identifier of the Resource resource.
    resource_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A list of update operations to be applied to the specified resource and in
    # the order specified in this list.
    patch_operations: typing.List["PatchOperation"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class UpdateRestApiRequest(ShapeBase):
    """
    Request to update an existing RestApi resource in your collection.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "rest_api_id",
                "restApiId",
                TypeInfo(str),
            ),
            (
                "patch_operations",
                "patchOperations",
                TypeInfo(typing.List[PatchOperation]),
            ),
        ]

    # [Required] The string identifier of the associated RestApi.
    rest_api_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A list of update operations to be applied to the specified resource and in
    # the order specified in this list.
    patch_operations: typing.List["PatchOperation"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class UpdateStageRequest(ShapeBase):
    """
    Requests API Gateway to change information about a Stage resource.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "rest_api_id",
                "restApiId",
                TypeInfo(str),
            ),
            (
                "stage_name",
                "stageName",
                TypeInfo(str),
            ),
            (
                "patch_operations",
                "patchOperations",
                TypeInfo(typing.List[PatchOperation]),
            ),
        ]

    # [Required] The string identifier of the associated RestApi.
    rest_api_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # [Required] The name of the Stage resource to change information about.
    stage_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A list of update operations to be applied to the specified resource and in
    # the order specified in this list.
    patch_operations: typing.List["PatchOperation"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class UpdateUsagePlanRequest(ShapeBase):
    """
    The PATCH request to update a usage plan of a given plan Id.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "usage_plan_id",
                "usagePlanId",
                TypeInfo(str),
            ),
            (
                "patch_operations",
                "patchOperations",
                TypeInfo(typing.List[PatchOperation]),
            ),
        ]

    # [Required] The Id of the to-be-updated usage plan.
    usage_plan_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A list of update operations to be applied to the specified resource and in
    # the order specified in this list.
    patch_operations: typing.List["PatchOperation"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class UpdateUsageRequest(ShapeBase):
    """
    The PATCH request to grant a temporary extension to the remaining quota of a
    usage plan associated with a specified API key.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "usage_plan_id",
                "usagePlanId",
                TypeInfo(str),
            ),
            (
                "key_id",
                "keyId",
                TypeInfo(str),
            ),
            (
                "patch_operations",
                "patchOperations",
                TypeInfo(typing.List[PatchOperation]),
            ),
        ]

    # [Required] The Id of the usage plan associated with the usage data.
    usage_plan_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # [Required] The identifier of the API key associated with the usage plan in
    # which a temporary extension is granted to the remaining quota.
    key_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A list of update operations to be applied to the specified resource and in
    # the order specified in this list.
    patch_operations: typing.List["PatchOperation"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class UpdateVpcLinkRequest(ShapeBase):
    """
    Updates an existing VpcLink of a specified identifier.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "vpc_link_id",
                "vpcLinkId",
                TypeInfo(str),
            ),
            (
                "patch_operations",
                "patchOperations",
                TypeInfo(typing.List[PatchOperation]),
            ),
        ]

    # [Required] The identifier of the VpcLink. It is used in an Integration to
    # reference this VpcLink.
    vpc_link_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A list of update operations to be applied to the specified resource and in
    # the order specified in this list.
    patch_operations: typing.List["PatchOperation"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class Usage(OutputShapeBase):
    """
    Represents the usage data of a usage plan.

    [Create and Use Usage
    Plans](http://docs.aws.amazon.com/apigateway/latest/developerguide/api-gateway-
    api-usage-plans.html), [Manage Usage in a Usage
    Plan](http://docs.aws.amazon.com/apigateway/latest/developerguide/api-gateway-
    create-usage-plans-with-console.html#api-gateway-usage-plan-manage-usage)
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
                "usage_plan_id",
                "usagePlanId",
                TypeInfo(str),
            ),
            (
                "start_date",
                "startDate",
                TypeInfo(str),
            ),
            (
                "end_date",
                "endDate",
                TypeInfo(str),
            ),
            (
                "position",
                "position",
                TypeInfo(str),
            ),
            (
                "items",
                "items",
                TypeInfo(typing.Dict[str, typing.List[typing.List[int]]]),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The plan Id associated with this usage data.
    usage_plan_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The starting date of the usage data.
    start_date: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The ending date of the usage data.
    end_date: str = dataclasses.field(default=ShapeBase.NOT_SET, )
    position: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The usage data, as daily logs of used and remaining quotas, over the
    # specified time interval indexed over the API keys in a usage plan. For
    # example, `{..., "values" : { "{api_key}" : [ [0, 100], [10, 90], [100,
    # 10]]}`, where `{api_key}` stands for an API key value and the daily log
    # entry is of the format `[used quota, remaining quota]`.
    items: typing.Dict[str, typing.List[typing.List[int]]] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    def paginate(self, ) -> typing.Generator["Usage", None, None]:
        yield from super()._paginate()


@dataclasses.dataclass
class UsagePlan(OutputShapeBase):
    """
    Represents a usage plan than can specify who can assess associated API stages
    with specified request limits and quotas.

    In a usage plan, you associate an API by specifying the API's Id and a stage
    name of the specified API. You add plan customers by adding API keys to the
    plan.

    [Create and Use Usage
    Plans](http://docs.aws.amazon.com/apigateway/latest/developerguide/api-gateway-
    api-usage-plans.html)
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
                "id",
                "id",
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
                "api_stages",
                "apiStages",
                TypeInfo(typing.List[ApiStage]),
            ),
            (
                "throttle",
                "throttle",
                TypeInfo(ThrottleSettings),
            ),
            (
                "quota",
                "quota",
                TypeInfo(QuotaSettings),
            ),
            (
                "product_code",
                "productCode",
                TypeInfo(str),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The identifier of a UsagePlan resource.
    id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The name of a usage plan.
    name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The description of a usage plan.
    description: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The associated API stages of a usage plan.
    api_stages: typing.List["ApiStage"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The request throttle limits of a usage plan.
    throttle: "ThrottleSettings" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The maximum number of permitted requests per a given unit time interval.
    quota: "QuotaSettings" = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The AWS Markeplace product identifier to associate with the usage plan as a
    # SaaS product on AWS Marketplace.
    product_code: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class UsagePlanKey(OutputShapeBase):
    """
    Represents a usage plan key to identify a plan customer.

    To associate an API stage with a selected API key in a usage plan, you must
    create a UsagePlanKey resource to represent the selected ApiKey.

    "

    [Create and Use Usage
    Plans](http://docs.aws.amazon.com/apigateway/latest/developerguide/api-gateway-
    api-usage-plans.html)
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
                "id",
                "id",
                TypeInfo(str),
            ),
            (
                "type",
                "type",
                TypeInfo(str),
            ),
            (
                "value",
                "value",
                TypeInfo(str),
            ),
            (
                "name",
                "name",
                TypeInfo(str),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The Id of a usage plan key.
    id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The type of a usage plan key. Currently, the valid key type is `API_KEY`.
    type: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The value of a usage plan key.
    value: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The name of a usage plan key.
    name: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class UsagePlanKeys(OutputShapeBase):
    """
    Represents the collection of usage plan keys added to usage plans for the
    associated API keys and, possibly, other types of keys.

    [Create and Use Usage
    Plans](http://docs.aws.amazon.com/apigateway/latest/developerguide/api-gateway-
    api-usage-plans.html)
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
                "position",
                "position",
                TypeInfo(str),
            ),
            (
                "items",
                "items",
                TypeInfo(typing.List[UsagePlanKey]),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )
    position: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The current page of elements from this collection.
    items: typing.List["UsagePlanKey"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    def paginate(self, ) -> typing.Generator["UsagePlanKeys", None, None]:
        yield from super()._paginate()


@dataclasses.dataclass
class UsagePlans(OutputShapeBase):
    """
    Represents a collection of usage plans for an AWS account.

    [Create and Use Usage
    Plans](http://docs.aws.amazon.com/apigateway/latest/developerguide/api-gateway-
    api-usage-plans.html)
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
                "position",
                "position",
                TypeInfo(str),
            ),
            (
                "items",
                "items",
                TypeInfo(typing.List[UsagePlan]),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )
    position: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The current page of elements from this collection.
    items: typing.List["UsagePlan"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    def paginate(self, ) -> typing.Generator["UsagePlans", None, None]:
        yield from super()._paginate()


@dataclasses.dataclass
class VpcLink(OutputShapeBase):
    """
    A API Gateway VPC link for a RestApi to access resources in an Amazon Virtual
    Private Cloud (VPC).

    To enable access to a resource in an Amazon Virtual Private Cloud through Amazon
    API Gateway, you, as an API developer, create a VpcLink resource targeted for
    one or more network load balancers of the VPC and then integrate an API method
    with a private integration that uses the VpcLink. The private integration has an
    integration type of `HTTP` or `HTTP_PROXY` and has a connection type of
    `VPC_LINK`. The integration uses the `connectionId` property to identify the
    VpcLink used.
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
                "id",
                "id",
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
                "target_arns",
                "targetArns",
                TypeInfo(typing.List[str]),
            ),
            (
                "status",
                "status",
                TypeInfo(typing.Union[str, VpcLinkStatus]),
            ),
            (
                "status_message",
                "statusMessage",
                TypeInfo(str),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The identifier of the VpcLink. It is used in an Integration to reference
    # this VpcLink.
    id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The name used to label and identify the VPC link.
    name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The description of the VPC link.
    description: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The ARNs of network load balancers of the VPC targeted by the VPC link. The
    # network load balancers must be owned by the same AWS account of the API
    # owner.
    target_arns: typing.List[str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The status of the VPC link. The valid values are `AVAILABLE`, `PENDING`,
    # `DELETING`, or `FAILED`. Deploying an API will wait if the status is
    # `PENDING` and will fail if the status is `DELETING`.
    status: typing.Union[str, "VpcLinkStatus"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A description about the VPC link status.
    status_message: str = dataclasses.field(default=ShapeBase.NOT_SET, )


class VpcLinkStatus(str):
    AVAILABLE = "AVAILABLE"
    PENDING = "PENDING"
    DELETING = "DELETING"
    FAILED = "FAILED"


@dataclasses.dataclass
class VpcLinks(OutputShapeBase):
    """
    The collection of VPC links under the caller's account in a region.

    [Getting Started with Private
    Integrations](http://docs.aws.amazon.com/apigateway/latest/developerguide/getting-
    started-with-private-integration.html), [Set up Private
    Integrations](http://docs.aws.amazon.com/apigateway/latest/developerguide/set-
    up-private-integration.html)
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
                "position",
                "position",
                TypeInfo(str),
            ),
            (
                "items",
                "items",
                TypeInfo(typing.List[VpcLink]),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )
    position: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The current page of elements from this collection.
    items: typing.List["VpcLink"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    def paginate(self, ) -> typing.Generator["VpcLinks", None, None]:
        yield from super()._paginate()
