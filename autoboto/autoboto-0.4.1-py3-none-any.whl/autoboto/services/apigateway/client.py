import datetime
import typing
import boto3
from autoboto import ClientBase, ShapeBase, OutputShapeBase
from . import shapes


class Client(ClientBase):
    def __init__(self, *args, **kwargs):
        super().__init__("apigateway", *args, **kwargs)

    def create_api_key(
        self,
        _request: shapes.CreateApiKeyRequest = None,
        *,
        name: str = ShapeBase.NOT_SET,
        description: str = ShapeBase.NOT_SET,
        enabled: bool = ShapeBase.NOT_SET,
        generate_distinct_id: bool = ShapeBase.NOT_SET,
        value: str = ShapeBase.NOT_SET,
        stage_keys: typing.List[shapes.StageKey] = ShapeBase.NOT_SET,
        customer_id: str = ShapeBase.NOT_SET,
    ) -> shapes.ApiKey:
        """
        Create an ApiKey resource.

        [AWS CLI](http://docs.aws.amazon.com/cli/latest/reference/apigateway/create-api-
        key.html)
        """
        if _request is None:
            _params = {}
            if name is not ShapeBase.NOT_SET:
                _params['name'] = name
            if description is not ShapeBase.NOT_SET:
                _params['description'] = description
            if enabled is not ShapeBase.NOT_SET:
                _params['enabled'] = enabled
            if generate_distinct_id is not ShapeBase.NOT_SET:
                _params['generate_distinct_id'] = generate_distinct_id
            if value is not ShapeBase.NOT_SET:
                _params['value'] = value
            if stage_keys is not ShapeBase.NOT_SET:
                _params['stage_keys'] = stage_keys
            if customer_id is not ShapeBase.NOT_SET:
                _params['customer_id'] = customer_id
            _request = shapes.CreateApiKeyRequest(**_params)
        response = self._boto_client.create_api_key(**_request.to_boto())

        return shapes.ApiKey.from_boto(response)

    def create_authorizer(
        self,
        _request: shapes.CreateAuthorizerRequest = None,
        *,
        rest_api_id: str,
        name: str,
        type: typing.Union[str, shapes.AuthorizerType],
        provider_arns: typing.List[str] = ShapeBase.NOT_SET,
        auth_type: str = ShapeBase.NOT_SET,
        authorizer_uri: str = ShapeBase.NOT_SET,
        authorizer_credentials: str = ShapeBase.NOT_SET,
        identity_source: str = ShapeBase.NOT_SET,
        identity_validation_expression: str = ShapeBase.NOT_SET,
        authorizer_result_ttl_in_seconds: int = ShapeBase.NOT_SET,
    ) -> shapes.Authorizer:
        """
        Adds a new Authorizer resource to an existing RestApi resource.

        [AWS CLI](http://docs.aws.amazon.com/cli/latest/reference/apigateway/create-
        authorizer.html)
        """
        if _request is None:
            _params = {}
            if rest_api_id is not ShapeBase.NOT_SET:
                _params['rest_api_id'] = rest_api_id
            if name is not ShapeBase.NOT_SET:
                _params['name'] = name
            if type is not ShapeBase.NOT_SET:
                _params['type'] = type
            if provider_arns is not ShapeBase.NOT_SET:
                _params['provider_arns'] = provider_arns
            if auth_type is not ShapeBase.NOT_SET:
                _params['auth_type'] = auth_type
            if authorizer_uri is not ShapeBase.NOT_SET:
                _params['authorizer_uri'] = authorizer_uri
            if authorizer_credentials is not ShapeBase.NOT_SET:
                _params['authorizer_credentials'] = authorizer_credentials
            if identity_source is not ShapeBase.NOT_SET:
                _params['identity_source'] = identity_source
            if identity_validation_expression is not ShapeBase.NOT_SET:
                _params['identity_validation_expression'
                       ] = identity_validation_expression
            if authorizer_result_ttl_in_seconds is not ShapeBase.NOT_SET:
                _params['authorizer_result_ttl_in_seconds'
                       ] = authorizer_result_ttl_in_seconds
            _request = shapes.CreateAuthorizerRequest(**_params)
        response = self._boto_client.create_authorizer(**_request.to_boto())

        return shapes.Authorizer.from_boto(response)

    def create_base_path_mapping(
        self,
        _request: shapes.CreateBasePathMappingRequest = None,
        *,
        domain_name: str,
        rest_api_id: str,
        base_path: str = ShapeBase.NOT_SET,
        stage: str = ShapeBase.NOT_SET,
    ) -> shapes.BasePathMapping:
        """
        Creates a new BasePathMapping resource.
        """
        if _request is None:
            _params = {}
            if domain_name is not ShapeBase.NOT_SET:
                _params['domain_name'] = domain_name
            if rest_api_id is not ShapeBase.NOT_SET:
                _params['rest_api_id'] = rest_api_id
            if base_path is not ShapeBase.NOT_SET:
                _params['base_path'] = base_path
            if stage is not ShapeBase.NOT_SET:
                _params['stage'] = stage
            _request = shapes.CreateBasePathMappingRequest(**_params)
        response = self._boto_client.create_base_path_mapping(
            **_request.to_boto()
        )

        return shapes.BasePathMapping.from_boto(response)

    def create_deployment(
        self,
        _request: shapes.CreateDeploymentRequest = None,
        *,
        rest_api_id: str,
        stage_name: str = ShapeBase.NOT_SET,
        stage_description: str = ShapeBase.NOT_SET,
        description: str = ShapeBase.NOT_SET,
        cache_cluster_enabled: bool = ShapeBase.NOT_SET,
        cache_cluster_size: typing.Union[str, shapes.
                                         CacheClusterSize] = ShapeBase.NOT_SET,
        variables: typing.Dict[str, str] = ShapeBase.NOT_SET,
        canary_settings: shapes.DeploymentCanarySettings = ShapeBase.NOT_SET,
        tracing_enabled: bool = ShapeBase.NOT_SET,
    ) -> shapes.Deployment:
        """
        Creates a Deployment resource, which makes a specified RestApi callable over the
        internet.
        """
        if _request is None:
            _params = {}
            if rest_api_id is not ShapeBase.NOT_SET:
                _params['rest_api_id'] = rest_api_id
            if stage_name is not ShapeBase.NOT_SET:
                _params['stage_name'] = stage_name
            if stage_description is not ShapeBase.NOT_SET:
                _params['stage_description'] = stage_description
            if description is not ShapeBase.NOT_SET:
                _params['description'] = description
            if cache_cluster_enabled is not ShapeBase.NOT_SET:
                _params['cache_cluster_enabled'] = cache_cluster_enabled
            if cache_cluster_size is not ShapeBase.NOT_SET:
                _params['cache_cluster_size'] = cache_cluster_size
            if variables is not ShapeBase.NOT_SET:
                _params['variables'] = variables
            if canary_settings is not ShapeBase.NOT_SET:
                _params['canary_settings'] = canary_settings
            if tracing_enabled is not ShapeBase.NOT_SET:
                _params['tracing_enabled'] = tracing_enabled
            _request = shapes.CreateDeploymentRequest(**_params)
        response = self._boto_client.create_deployment(**_request.to_boto())

        return shapes.Deployment.from_boto(response)

    def create_documentation_part(
        self,
        _request: shapes.CreateDocumentationPartRequest = None,
        *,
        rest_api_id: str,
        location: shapes.DocumentationPartLocation,
        properties: str,
    ) -> shapes.DocumentationPart:
        if _request is None:
            _params = {}
            if rest_api_id is not ShapeBase.NOT_SET:
                _params['rest_api_id'] = rest_api_id
            if location is not ShapeBase.NOT_SET:
                _params['location'] = location
            if properties is not ShapeBase.NOT_SET:
                _params['properties'] = properties
            _request = shapes.CreateDocumentationPartRequest(**_params)
        response = self._boto_client.create_documentation_part(
            **_request.to_boto()
        )

        return shapes.DocumentationPart.from_boto(response)

    def create_documentation_version(
        self,
        _request: shapes.CreateDocumentationVersionRequest = None,
        *,
        rest_api_id: str,
        documentation_version: str,
        stage_name: str = ShapeBase.NOT_SET,
        description: str = ShapeBase.NOT_SET,
    ) -> shapes.DocumentationVersion:
        if _request is None:
            _params = {}
            if rest_api_id is not ShapeBase.NOT_SET:
                _params['rest_api_id'] = rest_api_id
            if documentation_version is not ShapeBase.NOT_SET:
                _params['documentation_version'] = documentation_version
            if stage_name is not ShapeBase.NOT_SET:
                _params['stage_name'] = stage_name
            if description is not ShapeBase.NOT_SET:
                _params['description'] = description
            _request = shapes.CreateDocumentationVersionRequest(**_params)
        response = self._boto_client.create_documentation_version(
            **_request.to_boto()
        )

        return shapes.DocumentationVersion.from_boto(response)

    def create_domain_name(
        self,
        _request: shapes.CreateDomainNameRequest = None,
        *,
        domain_name: str,
        certificate_name: str = ShapeBase.NOT_SET,
        certificate_body: str = ShapeBase.NOT_SET,
        certificate_private_key: str = ShapeBase.NOT_SET,
        certificate_chain: str = ShapeBase.NOT_SET,
        certificate_arn: str = ShapeBase.NOT_SET,
        regional_certificate_name: str = ShapeBase.NOT_SET,
        regional_certificate_arn: str = ShapeBase.NOT_SET,
        endpoint_configuration: shapes.EndpointConfiguration = ShapeBase.
        NOT_SET,
    ) -> shapes.DomainName:
        """
        Creates a new domain name.
        """
        if _request is None:
            _params = {}
            if domain_name is not ShapeBase.NOT_SET:
                _params['domain_name'] = domain_name
            if certificate_name is not ShapeBase.NOT_SET:
                _params['certificate_name'] = certificate_name
            if certificate_body is not ShapeBase.NOT_SET:
                _params['certificate_body'] = certificate_body
            if certificate_private_key is not ShapeBase.NOT_SET:
                _params['certificate_private_key'] = certificate_private_key
            if certificate_chain is not ShapeBase.NOT_SET:
                _params['certificate_chain'] = certificate_chain
            if certificate_arn is not ShapeBase.NOT_SET:
                _params['certificate_arn'] = certificate_arn
            if regional_certificate_name is not ShapeBase.NOT_SET:
                _params['regional_certificate_name'] = regional_certificate_name
            if regional_certificate_arn is not ShapeBase.NOT_SET:
                _params['regional_certificate_arn'] = regional_certificate_arn
            if endpoint_configuration is not ShapeBase.NOT_SET:
                _params['endpoint_configuration'] = endpoint_configuration
            _request = shapes.CreateDomainNameRequest(**_params)
        response = self._boto_client.create_domain_name(**_request.to_boto())

        return shapes.DomainName.from_boto(response)

    def create_model(
        self,
        _request: shapes.CreateModelRequest = None,
        *,
        rest_api_id: str,
        name: str,
        content_type: str,
        description: str = ShapeBase.NOT_SET,
        schema: str = ShapeBase.NOT_SET,
    ) -> shapes.Model:
        """
        Adds a new Model resource to an existing RestApi resource.
        """
        if _request is None:
            _params = {}
            if rest_api_id is not ShapeBase.NOT_SET:
                _params['rest_api_id'] = rest_api_id
            if name is not ShapeBase.NOT_SET:
                _params['name'] = name
            if content_type is not ShapeBase.NOT_SET:
                _params['content_type'] = content_type
            if description is not ShapeBase.NOT_SET:
                _params['description'] = description
            if schema is not ShapeBase.NOT_SET:
                _params['schema'] = schema
            _request = shapes.CreateModelRequest(**_params)
        response = self._boto_client.create_model(**_request.to_boto())

        return shapes.Model.from_boto(response)

    def create_request_validator(
        self,
        _request: shapes.CreateRequestValidatorRequest = None,
        *,
        rest_api_id: str,
        name: str = ShapeBase.NOT_SET,
        validate_request_body: bool = ShapeBase.NOT_SET,
        validate_request_parameters: bool = ShapeBase.NOT_SET,
    ) -> shapes.RequestValidator:
        """
        Creates a ReqeustValidator of a given RestApi.
        """
        if _request is None:
            _params = {}
            if rest_api_id is not ShapeBase.NOT_SET:
                _params['rest_api_id'] = rest_api_id
            if name is not ShapeBase.NOT_SET:
                _params['name'] = name
            if validate_request_body is not ShapeBase.NOT_SET:
                _params['validate_request_body'] = validate_request_body
            if validate_request_parameters is not ShapeBase.NOT_SET:
                _params['validate_request_parameters'
                       ] = validate_request_parameters
            _request = shapes.CreateRequestValidatorRequest(**_params)
        response = self._boto_client.create_request_validator(
            **_request.to_boto()
        )

        return shapes.RequestValidator.from_boto(response)

    def create_resource(
        self,
        _request: shapes.CreateResourceRequest = None,
        *,
        rest_api_id: str,
        parent_id: str,
        path_part: str,
    ) -> shapes.Resource:
        """
        Creates a Resource resource.
        """
        if _request is None:
            _params = {}
            if rest_api_id is not ShapeBase.NOT_SET:
                _params['rest_api_id'] = rest_api_id
            if parent_id is not ShapeBase.NOT_SET:
                _params['parent_id'] = parent_id
            if path_part is not ShapeBase.NOT_SET:
                _params['path_part'] = path_part
            _request = shapes.CreateResourceRequest(**_params)
        response = self._boto_client.create_resource(**_request.to_boto())

        return shapes.Resource.from_boto(response)

    def create_rest_api(
        self,
        _request: shapes.CreateRestApiRequest = None,
        *,
        name: str,
        description: str = ShapeBase.NOT_SET,
        version: str = ShapeBase.NOT_SET,
        clone_from: str = ShapeBase.NOT_SET,
        binary_media_types: typing.List[str] = ShapeBase.NOT_SET,
        minimum_compression_size: int = ShapeBase.NOT_SET,
        api_key_source: typing.Union[str, shapes.
                                     ApiKeySourceType] = ShapeBase.NOT_SET,
        endpoint_configuration: shapes.EndpointConfiguration = ShapeBase.
        NOT_SET,
        policy: str = ShapeBase.NOT_SET,
    ) -> shapes.RestApi:
        """
        Creates a new RestApi resource.
        """
        if _request is None:
            _params = {}
            if name is not ShapeBase.NOT_SET:
                _params['name'] = name
            if description is not ShapeBase.NOT_SET:
                _params['description'] = description
            if version is not ShapeBase.NOT_SET:
                _params['version'] = version
            if clone_from is not ShapeBase.NOT_SET:
                _params['clone_from'] = clone_from
            if binary_media_types is not ShapeBase.NOT_SET:
                _params['binary_media_types'] = binary_media_types
            if minimum_compression_size is not ShapeBase.NOT_SET:
                _params['minimum_compression_size'] = minimum_compression_size
            if api_key_source is not ShapeBase.NOT_SET:
                _params['api_key_source'] = api_key_source
            if endpoint_configuration is not ShapeBase.NOT_SET:
                _params['endpoint_configuration'] = endpoint_configuration
            if policy is not ShapeBase.NOT_SET:
                _params['policy'] = policy
            _request = shapes.CreateRestApiRequest(**_params)
        response = self._boto_client.create_rest_api(**_request.to_boto())

        return shapes.RestApi.from_boto(response)

    def create_stage(
        self,
        _request: shapes.CreateStageRequest = None,
        *,
        rest_api_id: str,
        stage_name: str,
        deployment_id: str,
        description: str = ShapeBase.NOT_SET,
        cache_cluster_enabled: bool = ShapeBase.NOT_SET,
        cache_cluster_size: typing.Union[str, shapes.
                                         CacheClusterSize] = ShapeBase.NOT_SET,
        variables: typing.Dict[str, str] = ShapeBase.NOT_SET,
        documentation_version: str = ShapeBase.NOT_SET,
        canary_settings: shapes.CanarySettings = ShapeBase.NOT_SET,
        tracing_enabled: bool = ShapeBase.NOT_SET,
        tags: typing.Dict[str, str] = ShapeBase.NOT_SET,
    ) -> shapes.Stage:
        """
        Creates a new Stage resource that references a pre-existing Deployment for the
        API.
        """
        if _request is None:
            _params = {}
            if rest_api_id is not ShapeBase.NOT_SET:
                _params['rest_api_id'] = rest_api_id
            if stage_name is not ShapeBase.NOT_SET:
                _params['stage_name'] = stage_name
            if deployment_id is not ShapeBase.NOT_SET:
                _params['deployment_id'] = deployment_id
            if description is not ShapeBase.NOT_SET:
                _params['description'] = description
            if cache_cluster_enabled is not ShapeBase.NOT_SET:
                _params['cache_cluster_enabled'] = cache_cluster_enabled
            if cache_cluster_size is not ShapeBase.NOT_SET:
                _params['cache_cluster_size'] = cache_cluster_size
            if variables is not ShapeBase.NOT_SET:
                _params['variables'] = variables
            if documentation_version is not ShapeBase.NOT_SET:
                _params['documentation_version'] = documentation_version
            if canary_settings is not ShapeBase.NOT_SET:
                _params['canary_settings'] = canary_settings
            if tracing_enabled is not ShapeBase.NOT_SET:
                _params['tracing_enabled'] = tracing_enabled
            if tags is not ShapeBase.NOT_SET:
                _params['tags'] = tags
            _request = shapes.CreateStageRequest(**_params)
        response = self._boto_client.create_stage(**_request.to_boto())

        return shapes.Stage.from_boto(response)

    def create_usage_plan(
        self,
        _request: shapes.CreateUsagePlanRequest = None,
        *,
        name: str,
        description: str = ShapeBase.NOT_SET,
        api_stages: typing.List[shapes.ApiStage] = ShapeBase.NOT_SET,
        throttle: shapes.ThrottleSettings = ShapeBase.NOT_SET,
        quota: shapes.QuotaSettings = ShapeBase.NOT_SET,
    ) -> shapes.UsagePlan:
        """
        Creates a usage plan with the throttle and quota limits, as well as the
        associated API stages, specified in the payload.
        """
        if _request is None:
            _params = {}
            if name is not ShapeBase.NOT_SET:
                _params['name'] = name
            if description is not ShapeBase.NOT_SET:
                _params['description'] = description
            if api_stages is not ShapeBase.NOT_SET:
                _params['api_stages'] = api_stages
            if throttle is not ShapeBase.NOT_SET:
                _params['throttle'] = throttle
            if quota is not ShapeBase.NOT_SET:
                _params['quota'] = quota
            _request = shapes.CreateUsagePlanRequest(**_params)
        response = self._boto_client.create_usage_plan(**_request.to_boto())

        return shapes.UsagePlan.from_boto(response)

    def create_usage_plan_key(
        self,
        _request: shapes.CreateUsagePlanKeyRequest = None,
        *,
        usage_plan_id: str,
        key_id: str,
        key_type: str,
    ) -> shapes.UsagePlanKey:
        """
        Creates a usage plan key for adding an existing API key to a usage plan.
        """
        if _request is None:
            _params = {}
            if usage_plan_id is not ShapeBase.NOT_SET:
                _params['usage_plan_id'] = usage_plan_id
            if key_id is not ShapeBase.NOT_SET:
                _params['key_id'] = key_id
            if key_type is not ShapeBase.NOT_SET:
                _params['key_type'] = key_type
            _request = shapes.CreateUsagePlanKeyRequest(**_params)
        response = self._boto_client.create_usage_plan_key(**_request.to_boto())

        return shapes.UsagePlanKey.from_boto(response)

    def create_vpc_link(
        self,
        _request: shapes.CreateVpcLinkRequest = None,
        *,
        name: str,
        target_arns: typing.List[str],
        description: str = ShapeBase.NOT_SET,
    ) -> shapes.VpcLink:
        """
        Creates a VPC link, under the caller's account in a selected region, in an
        asynchronous operation that typically takes 2-4 minutes to complete and become
        operational. The caller must have permissions to create and update VPC Endpoint
        services.
        """
        if _request is None:
            _params = {}
            if name is not ShapeBase.NOT_SET:
                _params['name'] = name
            if target_arns is not ShapeBase.NOT_SET:
                _params['target_arns'] = target_arns
            if description is not ShapeBase.NOT_SET:
                _params['description'] = description
            _request = shapes.CreateVpcLinkRequest(**_params)
        response = self._boto_client.create_vpc_link(**_request.to_boto())

        return shapes.VpcLink.from_boto(response)

    def delete_api_key(
        self,
        _request: shapes.DeleteApiKeyRequest = None,
        *,
        api_key: str,
    ) -> None:
        """
        Deletes the ApiKey resource.
        """
        if _request is None:
            _params = {}
            if api_key is not ShapeBase.NOT_SET:
                _params['api_key'] = api_key
            _request = shapes.DeleteApiKeyRequest(**_params)
        response = self._boto_client.delete_api_key(**_request.to_boto())

    def delete_authorizer(
        self,
        _request: shapes.DeleteAuthorizerRequest = None,
        *,
        rest_api_id: str,
        authorizer_id: str,
    ) -> None:
        """
        Deletes an existing Authorizer resource.

        [AWS CLI](http://docs.aws.amazon.com/cli/latest/reference/apigateway/delete-
        authorizer.html)
        """
        if _request is None:
            _params = {}
            if rest_api_id is not ShapeBase.NOT_SET:
                _params['rest_api_id'] = rest_api_id
            if authorizer_id is not ShapeBase.NOT_SET:
                _params['authorizer_id'] = authorizer_id
            _request = shapes.DeleteAuthorizerRequest(**_params)
        response = self._boto_client.delete_authorizer(**_request.to_boto())

    def delete_base_path_mapping(
        self,
        _request: shapes.DeleteBasePathMappingRequest = None,
        *,
        domain_name: str,
        base_path: str,
    ) -> None:
        """
        Deletes the BasePathMapping resource.
        """
        if _request is None:
            _params = {}
            if domain_name is not ShapeBase.NOT_SET:
                _params['domain_name'] = domain_name
            if base_path is not ShapeBase.NOT_SET:
                _params['base_path'] = base_path
            _request = shapes.DeleteBasePathMappingRequest(**_params)
        response = self._boto_client.delete_base_path_mapping(
            **_request.to_boto()
        )

    def delete_client_certificate(
        self,
        _request: shapes.DeleteClientCertificateRequest = None,
        *,
        client_certificate_id: str,
    ) -> None:
        """
        Deletes the ClientCertificate resource.
        """
        if _request is None:
            _params = {}
            if client_certificate_id is not ShapeBase.NOT_SET:
                _params['client_certificate_id'] = client_certificate_id
            _request = shapes.DeleteClientCertificateRequest(**_params)
        response = self._boto_client.delete_client_certificate(
            **_request.to_boto()
        )

    def delete_deployment(
        self,
        _request: shapes.DeleteDeploymentRequest = None,
        *,
        rest_api_id: str,
        deployment_id: str,
    ) -> None:
        """
        Deletes a Deployment resource. Deleting a deployment will only succeed if there
        are no Stage resources associated with it.
        """
        if _request is None:
            _params = {}
            if rest_api_id is not ShapeBase.NOT_SET:
                _params['rest_api_id'] = rest_api_id
            if deployment_id is not ShapeBase.NOT_SET:
                _params['deployment_id'] = deployment_id
            _request = shapes.DeleteDeploymentRequest(**_params)
        response = self._boto_client.delete_deployment(**_request.to_boto())

    def delete_documentation_part(
        self,
        _request: shapes.DeleteDocumentationPartRequest = None,
        *,
        rest_api_id: str,
        documentation_part_id: str,
    ) -> None:
        if _request is None:
            _params = {}
            if rest_api_id is not ShapeBase.NOT_SET:
                _params['rest_api_id'] = rest_api_id
            if documentation_part_id is not ShapeBase.NOT_SET:
                _params['documentation_part_id'] = documentation_part_id
            _request = shapes.DeleteDocumentationPartRequest(**_params)
        response = self._boto_client.delete_documentation_part(
            **_request.to_boto()
        )

    def delete_documentation_version(
        self,
        _request: shapes.DeleteDocumentationVersionRequest = None,
        *,
        rest_api_id: str,
        documentation_version: str,
    ) -> None:
        if _request is None:
            _params = {}
            if rest_api_id is not ShapeBase.NOT_SET:
                _params['rest_api_id'] = rest_api_id
            if documentation_version is not ShapeBase.NOT_SET:
                _params['documentation_version'] = documentation_version
            _request = shapes.DeleteDocumentationVersionRequest(**_params)
        response = self._boto_client.delete_documentation_version(
            **_request.to_boto()
        )

    def delete_domain_name(
        self,
        _request: shapes.DeleteDomainNameRequest = None,
        *,
        domain_name: str,
    ) -> None:
        """
        Deletes the DomainName resource.
        """
        if _request is None:
            _params = {}
            if domain_name is not ShapeBase.NOT_SET:
                _params['domain_name'] = domain_name
            _request = shapes.DeleteDomainNameRequest(**_params)
        response = self._boto_client.delete_domain_name(**_request.to_boto())

    def delete_gateway_response(
        self,
        _request: shapes.DeleteGatewayResponseRequest = None,
        *,
        rest_api_id: str,
        response_type: typing.Union[str, shapes.GatewayResponseType],
    ) -> None:
        """
        Clears any customization of a GatewayResponse of a specified response type on
        the given RestApi and resets it with the default settings.
        """
        if _request is None:
            _params = {}
            if rest_api_id is not ShapeBase.NOT_SET:
                _params['rest_api_id'] = rest_api_id
            if response_type is not ShapeBase.NOT_SET:
                _params['response_type'] = response_type
            _request = shapes.DeleteGatewayResponseRequest(**_params)
        response = self._boto_client.delete_gateway_response(
            **_request.to_boto()
        )

    def delete_integration(
        self,
        _request: shapes.DeleteIntegrationRequest = None,
        *,
        rest_api_id: str,
        resource_id: str,
        http_method: str,
    ) -> None:
        """
        Represents a delete integration.
        """
        if _request is None:
            _params = {}
            if rest_api_id is not ShapeBase.NOT_SET:
                _params['rest_api_id'] = rest_api_id
            if resource_id is not ShapeBase.NOT_SET:
                _params['resource_id'] = resource_id
            if http_method is not ShapeBase.NOT_SET:
                _params['http_method'] = http_method
            _request = shapes.DeleteIntegrationRequest(**_params)
        response = self._boto_client.delete_integration(**_request.to_boto())

    def delete_integration_response(
        self,
        _request: shapes.DeleteIntegrationResponseRequest = None,
        *,
        rest_api_id: str,
        resource_id: str,
        http_method: str,
        status_code: str,
    ) -> None:
        """
        Represents a delete integration response.
        """
        if _request is None:
            _params = {}
            if rest_api_id is not ShapeBase.NOT_SET:
                _params['rest_api_id'] = rest_api_id
            if resource_id is not ShapeBase.NOT_SET:
                _params['resource_id'] = resource_id
            if http_method is not ShapeBase.NOT_SET:
                _params['http_method'] = http_method
            if status_code is not ShapeBase.NOT_SET:
                _params['status_code'] = status_code
            _request = shapes.DeleteIntegrationResponseRequest(**_params)
        response = self._boto_client.delete_integration_response(
            **_request.to_boto()
        )

    def delete_method(
        self,
        _request: shapes.DeleteMethodRequest = None,
        *,
        rest_api_id: str,
        resource_id: str,
        http_method: str,
    ) -> None:
        """
        Deletes an existing Method resource.
        """
        if _request is None:
            _params = {}
            if rest_api_id is not ShapeBase.NOT_SET:
                _params['rest_api_id'] = rest_api_id
            if resource_id is not ShapeBase.NOT_SET:
                _params['resource_id'] = resource_id
            if http_method is not ShapeBase.NOT_SET:
                _params['http_method'] = http_method
            _request = shapes.DeleteMethodRequest(**_params)
        response = self._boto_client.delete_method(**_request.to_boto())

    def delete_method_response(
        self,
        _request: shapes.DeleteMethodResponseRequest = None,
        *,
        rest_api_id: str,
        resource_id: str,
        http_method: str,
        status_code: str,
    ) -> None:
        """
        Deletes an existing MethodResponse resource.
        """
        if _request is None:
            _params = {}
            if rest_api_id is not ShapeBase.NOT_SET:
                _params['rest_api_id'] = rest_api_id
            if resource_id is not ShapeBase.NOT_SET:
                _params['resource_id'] = resource_id
            if http_method is not ShapeBase.NOT_SET:
                _params['http_method'] = http_method
            if status_code is not ShapeBase.NOT_SET:
                _params['status_code'] = status_code
            _request = shapes.DeleteMethodResponseRequest(**_params)
        response = self._boto_client.delete_method_response(
            **_request.to_boto()
        )

    def delete_model(
        self,
        _request: shapes.DeleteModelRequest = None,
        *,
        rest_api_id: str,
        model_name: str,
    ) -> None:
        """
        Deletes a model.
        """
        if _request is None:
            _params = {}
            if rest_api_id is not ShapeBase.NOT_SET:
                _params['rest_api_id'] = rest_api_id
            if model_name is not ShapeBase.NOT_SET:
                _params['model_name'] = model_name
            _request = shapes.DeleteModelRequest(**_params)
        response = self._boto_client.delete_model(**_request.to_boto())

    def delete_request_validator(
        self,
        _request: shapes.DeleteRequestValidatorRequest = None,
        *,
        rest_api_id: str,
        request_validator_id: str,
    ) -> None:
        """
        Deletes a RequestValidator of a given RestApi.
        """
        if _request is None:
            _params = {}
            if rest_api_id is not ShapeBase.NOT_SET:
                _params['rest_api_id'] = rest_api_id
            if request_validator_id is not ShapeBase.NOT_SET:
                _params['request_validator_id'] = request_validator_id
            _request = shapes.DeleteRequestValidatorRequest(**_params)
        response = self._boto_client.delete_request_validator(
            **_request.to_boto()
        )

    def delete_resource(
        self,
        _request: shapes.DeleteResourceRequest = None,
        *,
        rest_api_id: str,
        resource_id: str,
    ) -> None:
        """
        Deletes a Resource resource.
        """
        if _request is None:
            _params = {}
            if rest_api_id is not ShapeBase.NOT_SET:
                _params['rest_api_id'] = rest_api_id
            if resource_id is not ShapeBase.NOT_SET:
                _params['resource_id'] = resource_id
            _request = shapes.DeleteResourceRequest(**_params)
        response = self._boto_client.delete_resource(**_request.to_boto())

    def delete_rest_api(
        self,
        _request: shapes.DeleteRestApiRequest = None,
        *,
        rest_api_id: str,
    ) -> None:
        """
        Deletes the specified API.
        """
        if _request is None:
            _params = {}
            if rest_api_id is not ShapeBase.NOT_SET:
                _params['rest_api_id'] = rest_api_id
            _request = shapes.DeleteRestApiRequest(**_params)
        response = self._boto_client.delete_rest_api(**_request.to_boto())

    def delete_stage(
        self,
        _request: shapes.DeleteStageRequest = None,
        *,
        rest_api_id: str,
        stage_name: str,
    ) -> None:
        """
        Deletes a Stage resource.
        """
        if _request is None:
            _params = {}
            if rest_api_id is not ShapeBase.NOT_SET:
                _params['rest_api_id'] = rest_api_id
            if stage_name is not ShapeBase.NOT_SET:
                _params['stage_name'] = stage_name
            _request = shapes.DeleteStageRequest(**_params)
        response = self._boto_client.delete_stage(**_request.to_boto())

    def delete_usage_plan(
        self,
        _request: shapes.DeleteUsagePlanRequest = None,
        *,
        usage_plan_id: str,
    ) -> None:
        """
        Deletes a usage plan of a given plan Id.
        """
        if _request is None:
            _params = {}
            if usage_plan_id is not ShapeBase.NOT_SET:
                _params['usage_plan_id'] = usage_plan_id
            _request = shapes.DeleteUsagePlanRequest(**_params)
        response = self._boto_client.delete_usage_plan(**_request.to_boto())

    def delete_usage_plan_key(
        self,
        _request: shapes.DeleteUsagePlanKeyRequest = None,
        *,
        usage_plan_id: str,
        key_id: str,
    ) -> None:
        """
        Deletes a usage plan key and remove the underlying API key from the associated
        usage plan.
        """
        if _request is None:
            _params = {}
            if usage_plan_id is not ShapeBase.NOT_SET:
                _params['usage_plan_id'] = usage_plan_id
            if key_id is not ShapeBase.NOT_SET:
                _params['key_id'] = key_id
            _request = shapes.DeleteUsagePlanKeyRequest(**_params)
        response = self._boto_client.delete_usage_plan_key(**_request.to_boto())

    def delete_vpc_link(
        self,
        _request: shapes.DeleteVpcLinkRequest = None,
        *,
        vpc_link_id: str,
    ) -> None:
        """
        Deletes an existing VpcLink of a specified identifier.
        """
        if _request is None:
            _params = {}
            if vpc_link_id is not ShapeBase.NOT_SET:
                _params['vpc_link_id'] = vpc_link_id
            _request = shapes.DeleteVpcLinkRequest(**_params)
        response = self._boto_client.delete_vpc_link(**_request.to_boto())

    def flush_stage_authorizers_cache(
        self,
        _request: shapes.FlushStageAuthorizersCacheRequest = None,
        *,
        rest_api_id: str,
        stage_name: str,
    ) -> None:
        """
        Flushes all authorizer cache entries on a stage.
        """
        if _request is None:
            _params = {}
            if rest_api_id is not ShapeBase.NOT_SET:
                _params['rest_api_id'] = rest_api_id
            if stage_name is not ShapeBase.NOT_SET:
                _params['stage_name'] = stage_name
            _request = shapes.FlushStageAuthorizersCacheRequest(**_params)
        response = self._boto_client.flush_stage_authorizers_cache(
            **_request.to_boto()
        )

    def flush_stage_cache(
        self,
        _request: shapes.FlushStageCacheRequest = None,
        *,
        rest_api_id: str,
        stage_name: str,
    ) -> None:
        """
        Flushes a stage's cache.
        """
        if _request is None:
            _params = {}
            if rest_api_id is not ShapeBase.NOT_SET:
                _params['rest_api_id'] = rest_api_id
            if stage_name is not ShapeBase.NOT_SET:
                _params['stage_name'] = stage_name
            _request = shapes.FlushStageCacheRequest(**_params)
        response = self._boto_client.flush_stage_cache(**_request.to_boto())

    def generate_client_certificate(
        self,
        _request: shapes.GenerateClientCertificateRequest = None,
        *,
        description: str = ShapeBase.NOT_SET,
    ) -> shapes.ClientCertificate:
        """
        Generates a ClientCertificate resource.
        """
        if _request is None:
            _params = {}
            if description is not ShapeBase.NOT_SET:
                _params['description'] = description
            _request = shapes.GenerateClientCertificateRequest(**_params)
        response = self._boto_client.generate_client_certificate(
            **_request.to_boto()
        )

        return shapes.ClientCertificate.from_boto(response)

    def get_account(
        self,
        _request: shapes.GetAccountRequest = None,
    ) -> shapes.Account:
        """
        Gets information about the current Account resource.
        """
        if _request is None:
            _params = {}
            _request = shapes.GetAccountRequest(**_params)
        response = self._boto_client.get_account(**_request.to_boto())

        return shapes.Account.from_boto(response)

    def get_api_key(
        self,
        _request: shapes.GetApiKeyRequest = None,
        *,
        api_key: str,
        include_value: bool = ShapeBase.NOT_SET,
    ) -> shapes.ApiKey:
        """
        Gets information about the current ApiKey resource.
        """
        if _request is None:
            _params = {}
            if api_key is not ShapeBase.NOT_SET:
                _params['api_key'] = api_key
            if include_value is not ShapeBase.NOT_SET:
                _params['include_value'] = include_value
            _request = shapes.GetApiKeyRequest(**_params)
        response = self._boto_client.get_api_key(**_request.to_boto())

        return shapes.ApiKey.from_boto(response)

    def get_api_keys(
        self,
        _request: shapes.GetApiKeysRequest = None,
        *,
        position: str = ShapeBase.NOT_SET,
        limit: int = ShapeBase.NOT_SET,
        name_query: str = ShapeBase.NOT_SET,
        customer_id: str = ShapeBase.NOT_SET,
        include_values: bool = ShapeBase.NOT_SET,
    ) -> shapes.ApiKeys:
        """
        Gets information about the current ApiKeys resource.
        """
        if _request is None:
            _params = {}
            if position is not ShapeBase.NOT_SET:
                _params['position'] = position
            if limit is not ShapeBase.NOT_SET:
                _params['limit'] = limit
            if name_query is not ShapeBase.NOT_SET:
                _params['name_query'] = name_query
            if customer_id is not ShapeBase.NOT_SET:
                _params['customer_id'] = customer_id
            if include_values is not ShapeBase.NOT_SET:
                _params['include_values'] = include_values
            _request = shapes.GetApiKeysRequest(**_params)
        paginator = self.get_paginator("get_api_keys").paginate(
            **_request.to_boto()
        )
        page_generator = (page for page in paginator)
        first_page = next(page_generator)
        result = shapes.ApiKeys.from_boto(first_page)
        result._page_iterator = page_generator
        return result

        return shapes.ApiKeys.from_boto(response)

    def get_authorizer(
        self,
        _request: shapes.GetAuthorizerRequest = None,
        *,
        rest_api_id: str,
        authorizer_id: str,
    ) -> shapes.Authorizer:
        """
        Describe an existing Authorizer resource.

        [AWS CLI](http://docs.aws.amazon.com/cli/latest/reference/apigateway/get-
        authorizer.html)
        """
        if _request is None:
            _params = {}
            if rest_api_id is not ShapeBase.NOT_SET:
                _params['rest_api_id'] = rest_api_id
            if authorizer_id is not ShapeBase.NOT_SET:
                _params['authorizer_id'] = authorizer_id
            _request = shapes.GetAuthorizerRequest(**_params)
        response = self._boto_client.get_authorizer(**_request.to_boto())

        return shapes.Authorizer.from_boto(response)

    def get_authorizers(
        self,
        _request: shapes.GetAuthorizersRequest = None,
        *,
        rest_api_id: str,
        position: str = ShapeBase.NOT_SET,
        limit: int = ShapeBase.NOT_SET,
    ) -> shapes.Authorizers:
        """
        Describe an existing Authorizers resource.

        [AWS CLI](http://docs.aws.amazon.com/cli/latest/reference/apigateway/get-
        authorizers.html)
        """
        if _request is None:
            _params = {}
            if rest_api_id is not ShapeBase.NOT_SET:
                _params['rest_api_id'] = rest_api_id
            if position is not ShapeBase.NOT_SET:
                _params['position'] = position
            if limit is not ShapeBase.NOT_SET:
                _params['limit'] = limit
            _request = shapes.GetAuthorizersRequest(**_params)
        response = self._boto_client.get_authorizers(**_request.to_boto())

        return shapes.Authorizers.from_boto(response)

    def get_base_path_mapping(
        self,
        _request: shapes.GetBasePathMappingRequest = None,
        *,
        domain_name: str,
        base_path: str,
    ) -> shapes.BasePathMapping:
        """
        Describe a BasePathMapping resource.
        """
        if _request is None:
            _params = {}
            if domain_name is not ShapeBase.NOT_SET:
                _params['domain_name'] = domain_name
            if base_path is not ShapeBase.NOT_SET:
                _params['base_path'] = base_path
            _request = shapes.GetBasePathMappingRequest(**_params)
        response = self._boto_client.get_base_path_mapping(**_request.to_boto())

        return shapes.BasePathMapping.from_boto(response)

    def get_base_path_mappings(
        self,
        _request: shapes.GetBasePathMappingsRequest = None,
        *,
        domain_name: str,
        position: str = ShapeBase.NOT_SET,
        limit: int = ShapeBase.NOT_SET,
    ) -> shapes.BasePathMappings:
        """
        Represents a collection of BasePathMapping resources.
        """
        if _request is None:
            _params = {}
            if domain_name is not ShapeBase.NOT_SET:
                _params['domain_name'] = domain_name
            if position is not ShapeBase.NOT_SET:
                _params['position'] = position
            if limit is not ShapeBase.NOT_SET:
                _params['limit'] = limit
            _request = shapes.GetBasePathMappingsRequest(**_params)
        paginator = self.get_paginator("get_base_path_mappings").paginate(
            **_request.to_boto()
        )
        page_generator = (page for page in paginator)
        first_page = next(page_generator)
        result = shapes.BasePathMappings.from_boto(first_page)
        result._page_iterator = page_generator
        return result

        return shapes.BasePathMappings.from_boto(response)

    def get_client_certificate(
        self,
        _request: shapes.GetClientCertificateRequest = None,
        *,
        client_certificate_id: str,
    ) -> shapes.ClientCertificate:
        """
        Gets information about the current ClientCertificate resource.
        """
        if _request is None:
            _params = {}
            if client_certificate_id is not ShapeBase.NOT_SET:
                _params['client_certificate_id'] = client_certificate_id
            _request = shapes.GetClientCertificateRequest(**_params)
        response = self._boto_client.get_client_certificate(
            **_request.to_boto()
        )

        return shapes.ClientCertificate.from_boto(response)

    def get_client_certificates(
        self,
        _request: shapes.GetClientCertificatesRequest = None,
        *,
        position: str = ShapeBase.NOT_SET,
        limit: int = ShapeBase.NOT_SET,
    ) -> shapes.ClientCertificates:
        """
        Gets a collection of ClientCertificate resources.
        """
        if _request is None:
            _params = {}
            if position is not ShapeBase.NOT_SET:
                _params['position'] = position
            if limit is not ShapeBase.NOT_SET:
                _params['limit'] = limit
            _request = shapes.GetClientCertificatesRequest(**_params)
        paginator = self.get_paginator("get_client_certificates").paginate(
            **_request.to_boto()
        )
        page_generator = (page for page in paginator)
        first_page = next(page_generator)
        result = shapes.ClientCertificates.from_boto(first_page)
        result._page_iterator = page_generator
        return result

        return shapes.ClientCertificates.from_boto(response)

    def get_deployment(
        self,
        _request: shapes.GetDeploymentRequest = None,
        *,
        rest_api_id: str,
        deployment_id: str,
        embed: typing.List[str] = ShapeBase.NOT_SET,
    ) -> shapes.Deployment:
        """
        Gets information about a Deployment resource.
        """
        if _request is None:
            _params = {}
            if rest_api_id is not ShapeBase.NOT_SET:
                _params['rest_api_id'] = rest_api_id
            if deployment_id is not ShapeBase.NOT_SET:
                _params['deployment_id'] = deployment_id
            if embed is not ShapeBase.NOT_SET:
                _params['embed'] = embed
            _request = shapes.GetDeploymentRequest(**_params)
        response = self._boto_client.get_deployment(**_request.to_boto())

        return shapes.Deployment.from_boto(response)

    def get_deployments(
        self,
        _request: shapes.GetDeploymentsRequest = None,
        *,
        rest_api_id: str,
        position: str = ShapeBase.NOT_SET,
        limit: int = ShapeBase.NOT_SET,
    ) -> shapes.Deployments:
        """
        Gets information about a Deployments collection.
        """
        if _request is None:
            _params = {}
            if rest_api_id is not ShapeBase.NOT_SET:
                _params['rest_api_id'] = rest_api_id
            if position is not ShapeBase.NOT_SET:
                _params['position'] = position
            if limit is not ShapeBase.NOT_SET:
                _params['limit'] = limit
            _request = shapes.GetDeploymentsRequest(**_params)
        paginator = self.get_paginator("get_deployments").paginate(
            **_request.to_boto()
        )
        page_generator = (page for page in paginator)
        first_page = next(page_generator)
        result = shapes.Deployments.from_boto(first_page)
        result._page_iterator = page_generator
        return result

        return shapes.Deployments.from_boto(response)

    def get_documentation_part(
        self,
        _request: shapes.GetDocumentationPartRequest = None,
        *,
        rest_api_id: str,
        documentation_part_id: str,
    ) -> shapes.DocumentationPart:
        if _request is None:
            _params = {}
            if rest_api_id is not ShapeBase.NOT_SET:
                _params['rest_api_id'] = rest_api_id
            if documentation_part_id is not ShapeBase.NOT_SET:
                _params['documentation_part_id'] = documentation_part_id
            _request = shapes.GetDocumentationPartRequest(**_params)
        response = self._boto_client.get_documentation_part(
            **_request.to_boto()
        )

        return shapes.DocumentationPart.from_boto(response)

    def get_documentation_parts(
        self,
        _request: shapes.GetDocumentationPartsRequest = None,
        *,
        rest_api_id: str,
        type: typing.Union[str, shapes.DocumentationPartType] = ShapeBase.
        NOT_SET,
        name_query: str = ShapeBase.NOT_SET,
        path: str = ShapeBase.NOT_SET,
        position: str = ShapeBase.NOT_SET,
        limit: int = ShapeBase.NOT_SET,
        location_status: typing.Union[str, shapes.
                                      LocationStatusType] = ShapeBase.NOT_SET,
    ) -> shapes.DocumentationParts:
        if _request is None:
            _params = {}
            if rest_api_id is not ShapeBase.NOT_SET:
                _params['rest_api_id'] = rest_api_id
            if type is not ShapeBase.NOT_SET:
                _params['type'] = type
            if name_query is not ShapeBase.NOT_SET:
                _params['name_query'] = name_query
            if path is not ShapeBase.NOT_SET:
                _params['path'] = path
            if position is not ShapeBase.NOT_SET:
                _params['position'] = position
            if limit is not ShapeBase.NOT_SET:
                _params['limit'] = limit
            if location_status is not ShapeBase.NOT_SET:
                _params['location_status'] = location_status
            _request = shapes.GetDocumentationPartsRequest(**_params)
        response = self._boto_client.get_documentation_parts(
            **_request.to_boto()
        )

        return shapes.DocumentationParts.from_boto(response)

    def get_documentation_version(
        self,
        _request: shapes.GetDocumentationVersionRequest = None,
        *,
        rest_api_id: str,
        documentation_version: str,
    ) -> shapes.DocumentationVersion:
        if _request is None:
            _params = {}
            if rest_api_id is not ShapeBase.NOT_SET:
                _params['rest_api_id'] = rest_api_id
            if documentation_version is not ShapeBase.NOT_SET:
                _params['documentation_version'] = documentation_version
            _request = shapes.GetDocumentationVersionRequest(**_params)
        response = self._boto_client.get_documentation_version(
            **_request.to_boto()
        )

        return shapes.DocumentationVersion.from_boto(response)

    def get_documentation_versions(
        self,
        _request: shapes.GetDocumentationVersionsRequest = None,
        *,
        rest_api_id: str,
        position: str = ShapeBase.NOT_SET,
        limit: int = ShapeBase.NOT_SET,
    ) -> shapes.DocumentationVersions:
        if _request is None:
            _params = {}
            if rest_api_id is not ShapeBase.NOT_SET:
                _params['rest_api_id'] = rest_api_id
            if position is not ShapeBase.NOT_SET:
                _params['position'] = position
            if limit is not ShapeBase.NOT_SET:
                _params['limit'] = limit
            _request = shapes.GetDocumentationVersionsRequest(**_params)
        response = self._boto_client.get_documentation_versions(
            **_request.to_boto()
        )

        return shapes.DocumentationVersions.from_boto(response)

    def get_domain_name(
        self,
        _request: shapes.GetDomainNameRequest = None,
        *,
        domain_name: str,
    ) -> shapes.DomainName:
        """
        Represents a domain name that is contained in a simpler, more intuitive URL that
        can be called.
        """
        if _request is None:
            _params = {}
            if domain_name is not ShapeBase.NOT_SET:
                _params['domain_name'] = domain_name
            _request = shapes.GetDomainNameRequest(**_params)
        response = self._boto_client.get_domain_name(**_request.to_boto())

        return shapes.DomainName.from_boto(response)

    def get_domain_names(
        self,
        _request: shapes.GetDomainNamesRequest = None,
        *,
        position: str = ShapeBase.NOT_SET,
        limit: int = ShapeBase.NOT_SET,
    ) -> shapes.DomainNames:
        """
        Represents a collection of DomainName resources.
        """
        if _request is None:
            _params = {}
            if position is not ShapeBase.NOT_SET:
                _params['position'] = position
            if limit is not ShapeBase.NOT_SET:
                _params['limit'] = limit
            _request = shapes.GetDomainNamesRequest(**_params)
        paginator = self.get_paginator("get_domain_names").paginate(
            **_request.to_boto()
        )
        page_generator = (page for page in paginator)
        first_page = next(page_generator)
        result = shapes.DomainNames.from_boto(first_page)
        result._page_iterator = page_generator
        return result

        return shapes.DomainNames.from_boto(response)

    def get_export(
        self,
        _request: shapes.GetExportRequest = None,
        *,
        rest_api_id: str,
        stage_name: str,
        export_type: str,
        parameters: typing.Dict[str, str] = ShapeBase.NOT_SET,
        accepts: str = ShapeBase.NOT_SET,
    ) -> shapes.ExportResponse:
        """
        Exports a deployed version of a RestApi in a specified format.
        """
        if _request is None:
            _params = {}
            if rest_api_id is not ShapeBase.NOT_SET:
                _params['rest_api_id'] = rest_api_id
            if stage_name is not ShapeBase.NOT_SET:
                _params['stage_name'] = stage_name
            if export_type is not ShapeBase.NOT_SET:
                _params['export_type'] = export_type
            if parameters is not ShapeBase.NOT_SET:
                _params['parameters'] = parameters
            if accepts is not ShapeBase.NOT_SET:
                _params['accepts'] = accepts
            _request = shapes.GetExportRequest(**_params)
        response = self._boto_client.get_export(**_request.to_boto())

        return shapes.ExportResponse.from_boto(response)

    def get_gateway_response(
        self,
        _request: shapes.GetGatewayResponseRequest = None,
        *,
        rest_api_id: str,
        response_type: typing.Union[str, shapes.GatewayResponseType],
    ) -> shapes.GatewayResponse:
        """
        Gets a GatewayResponse of a specified response type on the given RestApi.
        """
        if _request is None:
            _params = {}
            if rest_api_id is not ShapeBase.NOT_SET:
                _params['rest_api_id'] = rest_api_id
            if response_type is not ShapeBase.NOT_SET:
                _params['response_type'] = response_type
            _request = shapes.GetGatewayResponseRequest(**_params)
        response = self._boto_client.get_gateway_response(**_request.to_boto())

        return shapes.GatewayResponse.from_boto(response)

    def get_gateway_responses(
        self,
        _request: shapes.GetGatewayResponsesRequest = None,
        *,
        rest_api_id: str,
        position: str = ShapeBase.NOT_SET,
        limit: int = ShapeBase.NOT_SET,
    ) -> shapes.GatewayResponses:
        """
        Gets the GatewayResponses collection on the given RestApi. If an API developer
        has not added any definitions for gateway responses, the result will be the API
        Gateway-generated default GatewayResponses collection for the supported response
        types.
        """
        if _request is None:
            _params = {}
            if rest_api_id is not ShapeBase.NOT_SET:
                _params['rest_api_id'] = rest_api_id
            if position is not ShapeBase.NOT_SET:
                _params['position'] = position
            if limit is not ShapeBase.NOT_SET:
                _params['limit'] = limit
            _request = shapes.GetGatewayResponsesRequest(**_params)
        response = self._boto_client.get_gateway_responses(**_request.to_boto())

        return shapes.GatewayResponses.from_boto(response)

    def get_integration(
        self,
        _request: shapes.GetIntegrationRequest = None,
        *,
        rest_api_id: str,
        resource_id: str,
        http_method: str,
    ) -> shapes.Integration:
        """
        Get the integration settings.
        """
        if _request is None:
            _params = {}
            if rest_api_id is not ShapeBase.NOT_SET:
                _params['rest_api_id'] = rest_api_id
            if resource_id is not ShapeBase.NOT_SET:
                _params['resource_id'] = resource_id
            if http_method is not ShapeBase.NOT_SET:
                _params['http_method'] = http_method
            _request = shapes.GetIntegrationRequest(**_params)
        response = self._boto_client.get_integration(**_request.to_boto())

        return shapes.Integration.from_boto(response)

    def get_integration_response(
        self,
        _request: shapes.GetIntegrationResponseRequest = None,
        *,
        rest_api_id: str,
        resource_id: str,
        http_method: str,
        status_code: str,
    ) -> shapes.IntegrationResponse:
        """
        Represents a get integration response.
        """
        if _request is None:
            _params = {}
            if rest_api_id is not ShapeBase.NOT_SET:
                _params['rest_api_id'] = rest_api_id
            if resource_id is not ShapeBase.NOT_SET:
                _params['resource_id'] = resource_id
            if http_method is not ShapeBase.NOT_SET:
                _params['http_method'] = http_method
            if status_code is not ShapeBase.NOT_SET:
                _params['status_code'] = status_code
            _request = shapes.GetIntegrationResponseRequest(**_params)
        response = self._boto_client.get_integration_response(
            **_request.to_boto()
        )

        return shapes.IntegrationResponse.from_boto(response)

    def get_method(
        self,
        _request: shapes.GetMethodRequest = None,
        *,
        rest_api_id: str,
        resource_id: str,
        http_method: str,
    ) -> shapes.Method:
        """
        Describe an existing Method resource.
        """
        if _request is None:
            _params = {}
            if rest_api_id is not ShapeBase.NOT_SET:
                _params['rest_api_id'] = rest_api_id
            if resource_id is not ShapeBase.NOT_SET:
                _params['resource_id'] = resource_id
            if http_method is not ShapeBase.NOT_SET:
                _params['http_method'] = http_method
            _request = shapes.GetMethodRequest(**_params)
        response = self._boto_client.get_method(**_request.to_boto())

        return shapes.Method.from_boto(response)

    def get_method_response(
        self,
        _request: shapes.GetMethodResponseRequest = None,
        *,
        rest_api_id: str,
        resource_id: str,
        http_method: str,
        status_code: str,
    ) -> shapes.MethodResponse:
        """
        Describes a MethodResponse resource.
        """
        if _request is None:
            _params = {}
            if rest_api_id is not ShapeBase.NOT_SET:
                _params['rest_api_id'] = rest_api_id
            if resource_id is not ShapeBase.NOT_SET:
                _params['resource_id'] = resource_id
            if http_method is not ShapeBase.NOT_SET:
                _params['http_method'] = http_method
            if status_code is not ShapeBase.NOT_SET:
                _params['status_code'] = status_code
            _request = shapes.GetMethodResponseRequest(**_params)
        response = self._boto_client.get_method_response(**_request.to_boto())

        return shapes.MethodResponse.from_boto(response)

    def get_model(
        self,
        _request: shapes.GetModelRequest = None,
        *,
        rest_api_id: str,
        model_name: str,
        flatten: bool = ShapeBase.NOT_SET,
    ) -> shapes.Model:
        """
        Describes an existing model defined for a RestApi resource.
        """
        if _request is None:
            _params = {}
            if rest_api_id is not ShapeBase.NOT_SET:
                _params['rest_api_id'] = rest_api_id
            if model_name is not ShapeBase.NOT_SET:
                _params['model_name'] = model_name
            if flatten is not ShapeBase.NOT_SET:
                _params['flatten'] = flatten
            _request = shapes.GetModelRequest(**_params)
        response = self._boto_client.get_model(**_request.to_boto())

        return shapes.Model.from_boto(response)

    def get_model_template(
        self,
        _request: shapes.GetModelTemplateRequest = None,
        *,
        rest_api_id: str,
        model_name: str,
    ) -> shapes.Template:
        """
        Generates a sample mapping template that can be used to transform a payload into
        the structure of a model.
        """
        if _request is None:
            _params = {}
            if rest_api_id is not ShapeBase.NOT_SET:
                _params['rest_api_id'] = rest_api_id
            if model_name is not ShapeBase.NOT_SET:
                _params['model_name'] = model_name
            _request = shapes.GetModelTemplateRequest(**_params)
        response = self._boto_client.get_model_template(**_request.to_boto())

        return shapes.Template.from_boto(response)

    def get_models(
        self,
        _request: shapes.GetModelsRequest = None,
        *,
        rest_api_id: str,
        position: str = ShapeBase.NOT_SET,
        limit: int = ShapeBase.NOT_SET,
    ) -> shapes.Models:
        """
        Describes existing Models defined for a RestApi resource.
        """
        if _request is None:
            _params = {}
            if rest_api_id is not ShapeBase.NOT_SET:
                _params['rest_api_id'] = rest_api_id
            if position is not ShapeBase.NOT_SET:
                _params['position'] = position
            if limit is not ShapeBase.NOT_SET:
                _params['limit'] = limit
            _request = shapes.GetModelsRequest(**_params)
        paginator = self.get_paginator("get_models").paginate(
            **_request.to_boto()
        )
        page_generator = (page for page in paginator)
        first_page = next(page_generator)
        result = shapes.Models.from_boto(first_page)
        result._page_iterator = page_generator
        return result

        return shapes.Models.from_boto(response)

    def get_request_validator(
        self,
        _request: shapes.GetRequestValidatorRequest = None,
        *,
        rest_api_id: str,
        request_validator_id: str,
    ) -> shapes.RequestValidator:
        """
        Gets a RequestValidator of a given RestApi.
        """
        if _request is None:
            _params = {}
            if rest_api_id is not ShapeBase.NOT_SET:
                _params['rest_api_id'] = rest_api_id
            if request_validator_id is not ShapeBase.NOT_SET:
                _params['request_validator_id'] = request_validator_id
            _request = shapes.GetRequestValidatorRequest(**_params)
        response = self._boto_client.get_request_validator(**_request.to_boto())

        return shapes.RequestValidator.from_boto(response)

    def get_request_validators(
        self,
        _request: shapes.GetRequestValidatorsRequest = None,
        *,
        rest_api_id: str,
        position: str = ShapeBase.NOT_SET,
        limit: int = ShapeBase.NOT_SET,
    ) -> shapes.RequestValidators:
        """
        Gets the RequestValidators collection of a given RestApi.
        """
        if _request is None:
            _params = {}
            if rest_api_id is not ShapeBase.NOT_SET:
                _params['rest_api_id'] = rest_api_id
            if position is not ShapeBase.NOT_SET:
                _params['position'] = position
            if limit is not ShapeBase.NOT_SET:
                _params['limit'] = limit
            _request = shapes.GetRequestValidatorsRequest(**_params)
        response = self._boto_client.get_request_validators(
            **_request.to_boto()
        )

        return shapes.RequestValidators.from_boto(response)

    def get_resource(
        self,
        _request: shapes.GetResourceRequest = None,
        *,
        rest_api_id: str,
        resource_id: str,
        embed: typing.List[str] = ShapeBase.NOT_SET,
    ) -> shapes.Resource:
        """
        Lists information about a resource.
        """
        if _request is None:
            _params = {}
            if rest_api_id is not ShapeBase.NOT_SET:
                _params['rest_api_id'] = rest_api_id
            if resource_id is not ShapeBase.NOT_SET:
                _params['resource_id'] = resource_id
            if embed is not ShapeBase.NOT_SET:
                _params['embed'] = embed
            _request = shapes.GetResourceRequest(**_params)
        response = self._boto_client.get_resource(**_request.to_boto())

        return shapes.Resource.from_boto(response)

    def get_resources(
        self,
        _request: shapes.GetResourcesRequest = None,
        *,
        rest_api_id: str,
        position: str = ShapeBase.NOT_SET,
        limit: int = ShapeBase.NOT_SET,
        embed: typing.List[str] = ShapeBase.NOT_SET,
    ) -> shapes.Resources:
        """
        Lists information about a collection of Resource resources.
        """
        if _request is None:
            _params = {}
            if rest_api_id is not ShapeBase.NOT_SET:
                _params['rest_api_id'] = rest_api_id
            if position is not ShapeBase.NOT_SET:
                _params['position'] = position
            if limit is not ShapeBase.NOT_SET:
                _params['limit'] = limit
            if embed is not ShapeBase.NOT_SET:
                _params['embed'] = embed
            _request = shapes.GetResourcesRequest(**_params)
        paginator = self.get_paginator("get_resources").paginate(
            **_request.to_boto()
        )
        page_generator = (page for page in paginator)
        first_page = next(page_generator)
        result = shapes.Resources.from_boto(first_page)
        result._page_iterator = page_generator
        return result

        return shapes.Resources.from_boto(response)

    def get_rest_api(
        self,
        _request: shapes.GetRestApiRequest = None,
        *,
        rest_api_id: str,
    ) -> shapes.RestApi:
        """
        Lists the RestApi resource in the collection.
        """
        if _request is None:
            _params = {}
            if rest_api_id is not ShapeBase.NOT_SET:
                _params['rest_api_id'] = rest_api_id
            _request = shapes.GetRestApiRequest(**_params)
        response = self._boto_client.get_rest_api(**_request.to_boto())

        return shapes.RestApi.from_boto(response)

    def get_rest_apis(
        self,
        _request: shapes.GetRestApisRequest = None,
        *,
        position: str = ShapeBase.NOT_SET,
        limit: int = ShapeBase.NOT_SET,
    ) -> shapes.RestApis:
        """
        Lists the RestApis resources for your collection.
        """
        if _request is None:
            _params = {}
            if position is not ShapeBase.NOT_SET:
                _params['position'] = position
            if limit is not ShapeBase.NOT_SET:
                _params['limit'] = limit
            _request = shapes.GetRestApisRequest(**_params)
        paginator = self.get_paginator("get_rest_apis").paginate(
            **_request.to_boto()
        )
        page_generator = (page for page in paginator)
        first_page = next(page_generator)
        result = shapes.RestApis.from_boto(first_page)
        result._page_iterator = page_generator
        return result

        return shapes.RestApis.from_boto(response)

    def get_sdk(
        self,
        _request: shapes.GetSdkRequest = None,
        *,
        rest_api_id: str,
        stage_name: str,
        sdk_type: str,
        parameters: typing.Dict[str, str] = ShapeBase.NOT_SET,
    ) -> shapes.SdkResponse:
        """
        Generates a client SDK for a RestApi and Stage.
        """
        if _request is None:
            _params = {}
            if rest_api_id is not ShapeBase.NOT_SET:
                _params['rest_api_id'] = rest_api_id
            if stage_name is not ShapeBase.NOT_SET:
                _params['stage_name'] = stage_name
            if sdk_type is not ShapeBase.NOT_SET:
                _params['sdk_type'] = sdk_type
            if parameters is not ShapeBase.NOT_SET:
                _params['parameters'] = parameters
            _request = shapes.GetSdkRequest(**_params)
        response = self._boto_client.get_sdk(**_request.to_boto())

        return shapes.SdkResponse.from_boto(response)

    def get_sdk_type(
        self,
        _request: shapes.GetSdkTypeRequest = None,
        *,
        id: str,
    ) -> shapes.SdkType:
        if _request is None:
            _params = {}
            if id is not ShapeBase.NOT_SET:
                _params['id'] = id
            _request = shapes.GetSdkTypeRequest(**_params)
        response = self._boto_client.get_sdk_type(**_request.to_boto())

        return shapes.SdkType.from_boto(response)

    def get_sdk_types(
        self,
        _request: shapes.GetSdkTypesRequest = None,
        *,
        position: str = ShapeBase.NOT_SET,
        limit: int = ShapeBase.NOT_SET,
    ) -> shapes.SdkTypes:
        if _request is None:
            _params = {}
            if position is not ShapeBase.NOT_SET:
                _params['position'] = position
            if limit is not ShapeBase.NOT_SET:
                _params['limit'] = limit
            _request = shapes.GetSdkTypesRequest(**_params)
        response = self._boto_client.get_sdk_types(**_request.to_boto())

        return shapes.SdkTypes.from_boto(response)

    def get_stage(
        self,
        _request: shapes.GetStageRequest = None,
        *,
        rest_api_id: str,
        stage_name: str,
    ) -> shapes.Stage:
        """
        Gets information about a Stage resource.
        """
        if _request is None:
            _params = {}
            if rest_api_id is not ShapeBase.NOT_SET:
                _params['rest_api_id'] = rest_api_id
            if stage_name is not ShapeBase.NOT_SET:
                _params['stage_name'] = stage_name
            _request = shapes.GetStageRequest(**_params)
        response = self._boto_client.get_stage(**_request.to_boto())

        return shapes.Stage.from_boto(response)

    def get_stages(
        self,
        _request: shapes.GetStagesRequest = None,
        *,
        rest_api_id: str,
        deployment_id: str = ShapeBase.NOT_SET,
    ) -> shapes.Stages:
        """
        Gets information about one or more Stage resources.
        """
        if _request is None:
            _params = {}
            if rest_api_id is not ShapeBase.NOT_SET:
                _params['rest_api_id'] = rest_api_id
            if deployment_id is not ShapeBase.NOT_SET:
                _params['deployment_id'] = deployment_id
            _request = shapes.GetStagesRequest(**_params)
        response = self._boto_client.get_stages(**_request.to_boto())

        return shapes.Stages.from_boto(response)

    def get_tags(
        self,
        _request: shapes.GetTagsRequest = None,
        *,
        resource_arn: str,
        position: str = ShapeBase.NOT_SET,
        limit: int = ShapeBase.NOT_SET,
    ) -> shapes.Tags:
        """
        Gets the Tags collection for a given resource.
        """
        if _request is None:
            _params = {}
            if resource_arn is not ShapeBase.NOT_SET:
                _params['resource_arn'] = resource_arn
            if position is not ShapeBase.NOT_SET:
                _params['position'] = position
            if limit is not ShapeBase.NOT_SET:
                _params['limit'] = limit
            _request = shapes.GetTagsRequest(**_params)
        response = self._boto_client.get_tags(**_request.to_boto())

        return shapes.Tags.from_boto(response)

    def get_usage(
        self,
        _request: shapes.GetUsageRequest = None,
        *,
        usage_plan_id: str,
        start_date: str,
        end_date: str,
        key_id: str = ShapeBase.NOT_SET,
        position: str = ShapeBase.NOT_SET,
        limit: int = ShapeBase.NOT_SET,
    ) -> shapes.Usage:
        """
        Gets the usage data of a usage plan in a specified time interval.
        """
        if _request is None:
            _params = {}
            if usage_plan_id is not ShapeBase.NOT_SET:
                _params['usage_plan_id'] = usage_plan_id
            if start_date is not ShapeBase.NOT_SET:
                _params['start_date'] = start_date
            if end_date is not ShapeBase.NOT_SET:
                _params['end_date'] = end_date
            if key_id is not ShapeBase.NOT_SET:
                _params['key_id'] = key_id
            if position is not ShapeBase.NOT_SET:
                _params['position'] = position
            if limit is not ShapeBase.NOT_SET:
                _params['limit'] = limit
            _request = shapes.GetUsageRequest(**_params)
        paginator = self.get_paginator("get_usage").paginate(
            **_request.to_boto()
        )
        page_generator = (page for page in paginator)
        first_page = next(page_generator)
        result = shapes.Usage.from_boto(first_page)
        result._page_iterator = page_generator
        return result

        return shapes.Usage.from_boto(response)

    def get_usage_plan(
        self,
        _request: shapes.GetUsagePlanRequest = None,
        *,
        usage_plan_id: str,
    ) -> shapes.UsagePlan:
        """
        Gets a usage plan of a given plan identifier.
        """
        if _request is None:
            _params = {}
            if usage_plan_id is not ShapeBase.NOT_SET:
                _params['usage_plan_id'] = usage_plan_id
            _request = shapes.GetUsagePlanRequest(**_params)
        response = self._boto_client.get_usage_plan(**_request.to_boto())

        return shapes.UsagePlan.from_boto(response)

    def get_usage_plan_key(
        self,
        _request: shapes.GetUsagePlanKeyRequest = None,
        *,
        usage_plan_id: str,
        key_id: str,
    ) -> shapes.UsagePlanKey:
        """
        Gets a usage plan key of a given key identifier.
        """
        if _request is None:
            _params = {}
            if usage_plan_id is not ShapeBase.NOT_SET:
                _params['usage_plan_id'] = usage_plan_id
            if key_id is not ShapeBase.NOT_SET:
                _params['key_id'] = key_id
            _request = shapes.GetUsagePlanKeyRequest(**_params)
        response = self._boto_client.get_usage_plan_key(**_request.to_boto())

        return shapes.UsagePlanKey.from_boto(response)

    def get_usage_plan_keys(
        self,
        _request: shapes.GetUsagePlanKeysRequest = None,
        *,
        usage_plan_id: str,
        position: str = ShapeBase.NOT_SET,
        limit: int = ShapeBase.NOT_SET,
        name_query: str = ShapeBase.NOT_SET,
    ) -> shapes.UsagePlanKeys:
        """
        Gets all the usage plan keys representing the API keys added to a specified
        usage plan.
        """
        if _request is None:
            _params = {}
            if usage_plan_id is not ShapeBase.NOT_SET:
                _params['usage_plan_id'] = usage_plan_id
            if position is not ShapeBase.NOT_SET:
                _params['position'] = position
            if limit is not ShapeBase.NOT_SET:
                _params['limit'] = limit
            if name_query is not ShapeBase.NOT_SET:
                _params['name_query'] = name_query
            _request = shapes.GetUsagePlanKeysRequest(**_params)
        paginator = self.get_paginator("get_usage_plan_keys").paginate(
            **_request.to_boto()
        )
        page_generator = (page for page in paginator)
        first_page = next(page_generator)
        result = shapes.UsagePlanKeys.from_boto(first_page)
        result._page_iterator = page_generator
        return result

        return shapes.UsagePlanKeys.from_boto(response)

    def get_usage_plans(
        self,
        _request: shapes.GetUsagePlansRequest = None,
        *,
        position: str = ShapeBase.NOT_SET,
        key_id: str = ShapeBase.NOT_SET,
        limit: int = ShapeBase.NOT_SET,
    ) -> shapes.UsagePlans:
        """
        Gets all the usage plans of the caller's account.
        """
        if _request is None:
            _params = {}
            if position is not ShapeBase.NOT_SET:
                _params['position'] = position
            if key_id is not ShapeBase.NOT_SET:
                _params['key_id'] = key_id
            if limit is not ShapeBase.NOT_SET:
                _params['limit'] = limit
            _request = shapes.GetUsagePlansRequest(**_params)
        paginator = self.get_paginator("get_usage_plans").paginate(
            **_request.to_boto()
        )
        page_generator = (page for page in paginator)
        first_page = next(page_generator)
        result = shapes.UsagePlans.from_boto(first_page)
        result._page_iterator = page_generator
        return result

        return shapes.UsagePlans.from_boto(response)

    def get_vpc_link(
        self,
        _request: shapes.GetVpcLinkRequest = None,
        *,
        vpc_link_id: str,
    ) -> shapes.VpcLink:
        """
        Gets a specified VPC link under the caller's account in a region.
        """
        if _request is None:
            _params = {}
            if vpc_link_id is not ShapeBase.NOT_SET:
                _params['vpc_link_id'] = vpc_link_id
            _request = shapes.GetVpcLinkRequest(**_params)
        response = self._boto_client.get_vpc_link(**_request.to_boto())

        return shapes.VpcLink.from_boto(response)

    def get_vpc_links(
        self,
        _request: shapes.GetVpcLinksRequest = None,
        *,
        position: str = ShapeBase.NOT_SET,
        limit: int = ShapeBase.NOT_SET,
    ) -> shapes.VpcLinks:
        """
        Gets the VpcLinks collection under the caller's account in a selected region.
        """
        if _request is None:
            _params = {}
            if position is not ShapeBase.NOT_SET:
                _params['position'] = position
            if limit is not ShapeBase.NOT_SET:
                _params['limit'] = limit
            _request = shapes.GetVpcLinksRequest(**_params)
        paginator = self.get_paginator("get_vpc_links").paginate(
            **_request.to_boto()
        )
        page_generator = (page for page in paginator)
        first_page = next(page_generator)
        result = shapes.VpcLinks.from_boto(first_page)
        result._page_iterator = page_generator
        return result

        return shapes.VpcLinks.from_boto(response)

    def import_api_keys(
        self,
        _request: shapes.ImportApiKeysRequest = None,
        *,
        body: typing.Any,
        format: typing.Union[str, shapes.ApiKeysFormat],
        fail_on_warnings: bool = ShapeBase.NOT_SET,
    ) -> shapes.ApiKeyIds:
        """
        Import API keys from an external source, such as a CSV-formatted file.
        """
        if _request is None:
            _params = {}
            if body is not ShapeBase.NOT_SET:
                _params['body'] = body
            if format is not ShapeBase.NOT_SET:
                _params['format'] = format
            if fail_on_warnings is not ShapeBase.NOT_SET:
                _params['fail_on_warnings'] = fail_on_warnings
            _request = shapes.ImportApiKeysRequest(**_params)
        response = self._boto_client.import_api_keys(**_request.to_boto())

        return shapes.ApiKeyIds.from_boto(response)

    def import_documentation_parts(
        self,
        _request: shapes.ImportDocumentationPartsRequest = None,
        *,
        rest_api_id: str,
        body: typing.Any,
        mode: typing.Union[str, shapes.PutMode] = ShapeBase.NOT_SET,
        fail_on_warnings: bool = ShapeBase.NOT_SET,
    ) -> shapes.DocumentationPartIds:
        if _request is None:
            _params = {}
            if rest_api_id is not ShapeBase.NOT_SET:
                _params['rest_api_id'] = rest_api_id
            if body is not ShapeBase.NOT_SET:
                _params['body'] = body
            if mode is not ShapeBase.NOT_SET:
                _params['mode'] = mode
            if fail_on_warnings is not ShapeBase.NOT_SET:
                _params['fail_on_warnings'] = fail_on_warnings
            _request = shapes.ImportDocumentationPartsRequest(**_params)
        response = self._boto_client.import_documentation_parts(
            **_request.to_boto()
        )

        return shapes.DocumentationPartIds.from_boto(response)

    def import_rest_api(
        self,
        _request: shapes.ImportRestApiRequest = None,
        *,
        body: typing.Any,
        fail_on_warnings: bool = ShapeBase.NOT_SET,
        parameters: typing.Dict[str, str] = ShapeBase.NOT_SET,
    ) -> shapes.RestApi:
        """
        A feature of the API Gateway control service for creating a new API from an
        external API definition file.
        """
        if _request is None:
            _params = {}
            if body is not ShapeBase.NOT_SET:
                _params['body'] = body
            if fail_on_warnings is not ShapeBase.NOT_SET:
                _params['fail_on_warnings'] = fail_on_warnings
            if parameters is not ShapeBase.NOT_SET:
                _params['parameters'] = parameters
            _request = shapes.ImportRestApiRequest(**_params)
        response = self._boto_client.import_rest_api(**_request.to_boto())

        return shapes.RestApi.from_boto(response)

    def put_gateway_response(
        self,
        _request: shapes.PutGatewayResponseRequest = None,
        *,
        rest_api_id: str,
        response_type: typing.Union[str, shapes.GatewayResponseType],
        status_code: str = ShapeBase.NOT_SET,
        response_parameters: typing.Dict[str, str] = ShapeBase.NOT_SET,
        response_templates: typing.Dict[str, str] = ShapeBase.NOT_SET,
    ) -> shapes.GatewayResponse:
        """
        Creates a customization of a GatewayResponse of a specified response type and
        status code on the given RestApi.
        """
        if _request is None:
            _params = {}
            if rest_api_id is not ShapeBase.NOT_SET:
                _params['rest_api_id'] = rest_api_id
            if response_type is not ShapeBase.NOT_SET:
                _params['response_type'] = response_type
            if status_code is not ShapeBase.NOT_SET:
                _params['status_code'] = status_code
            if response_parameters is not ShapeBase.NOT_SET:
                _params['response_parameters'] = response_parameters
            if response_templates is not ShapeBase.NOT_SET:
                _params['response_templates'] = response_templates
            _request = shapes.PutGatewayResponseRequest(**_params)
        response = self._boto_client.put_gateway_response(**_request.to_boto())

        return shapes.GatewayResponse.from_boto(response)

    def put_integration(
        self,
        _request: shapes.PutIntegrationRequest = None,
        *,
        rest_api_id: str,
        resource_id: str,
        http_method: str,
        type: typing.Union[str, shapes.IntegrationType],
        integration_http_method: str = ShapeBase.NOT_SET,
        uri: str = ShapeBase.NOT_SET,
        connection_type: typing.Union[str, shapes.
                                      ConnectionType] = ShapeBase.NOT_SET,
        connection_id: str = ShapeBase.NOT_SET,
        credentials: str = ShapeBase.NOT_SET,
        request_parameters: typing.Dict[str, str] = ShapeBase.NOT_SET,
        request_templates: typing.Dict[str, str] = ShapeBase.NOT_SET,
        passthrough_behavior: str = ShapeBase.NOT_SET,
        cache_namespace: str = ShapeBase.NOT_SET,
        cache_key_parameters: typing.List[str] = ShapeBase.NOT_SET,
        content_handling: typing.
        Union[str, shapes.ContentHandlingStrategy] = ShapeBase.NOT_SET,
        timeout_in_millis: int = ShapeBase.NOT_SET,
    ) -> shapes.Integration:
        """
        Sets up a method's integration.
        """
        if _request is None:
            _params = {}
            if rest_api_id is not ShapeBase.NOT_SET:
                _params['rest_api_id'] = rest_api_id
            if resource_id is not ShapeBase.NOT_SET:
                _params['resource_id'] = resource_id
            if http_method is not ShapeBase.NOT_SET:
                _params['http_method'] = http_method
            if type is not ShapeBase.NOT_SET:
                _params['type'] = type
            if integration_http_method is not ShapeBase.NOT_SET:
                _params['integration_http_method'] = integration_http_method
            if uri is not ShapeBase.NOT_SET:
                _params['uri'] = uri
            if connection_type is not ShapeBase.NOT_SET:
                _params['connection_type'] = connection_type
            if connection_id is not ShapeBase.NOT_SET:
                _params['connection_id'] = connection_id
            if credentials is not ShapeBase.NOT_SET:
                _params['credentials'] = credentials
            if request_parameters is not ShapeBase.NOT_SET:
                _params['request_parameters'] = request_parameters
            if request_templates is not ShapeBase.NOT_SET:
                _params['request_templates'] = request_templates
            if passthrough_behavior is not ShapeBase.NOT_SET:
                _params['passthrough_behavior'] = passthrough_behavior
            if cache_namespace is not ShapeBase.NOT_SET:
                _params['cache_namespace'] = cache_namespace
            if cache_key_parameters is not ShapeBase.NOT_SET:
                _params['cache_key_parameters'] = cache_key_parameters
            if content_handling is not ShapeBase.NOT_SET:
                _params['content_handling'] = content_handling
            if timeout_in_millis is not ShapeBase.NOT_SET:
                _params['timeout_in_millis'] = timeout_in_millis
            _request = shapes.PutIntegrationRequest(**_params)
        response = self._boto_client.put_integration(**_request.to_boto())

        return shapes.Integration.from_boto(response)

    def put_integration_response(
        self,
        _request: shapes.PutIntegrationResponseRequest = None,
        *,
        rest_api_id: str,
        resource_id: str,
        http_method: str,
        status_code: str,
        selection_pattern: str = ShapeBase.NOT_SET,
        response_parameters: typing.Dict[str, str] = ShapeBase.NOT_SET,
        response_templates: typing.Dict[str, str] = ShapeBase.NOT_SET,
        content_handling: typing.
        Union[str, shapes.ContentHandlingStrategy] = ShapeBase.NOT_SET,
    ) -> shapes.IntegrationResponse:
        """
        Represents a put integration.
        """
        if _request is None:
            _params = {}
            if rest_api_id is not ShapeBase.NOT_SET:
                _params['rest_api_id'] = rest_api_id
            if resource_id is not ShapeBase.NOT_SET:
                _params['resource_id'] = resource_id
            if http_method is not ShapeBase.NOT_SET:
                _params['http_method'] = http_method
            if status_code is not ShapeBase.NOT_SET:
                _params['status_code'] = status_code
            if selection_pattern is not ShapeBase.NOT_SET:
                _params['selection_pattern'] = selection_pattern
            if response_parameters is not ShapeBase.NOT_SET:
                _params['response_parameters'] = response_parameters
            if response_templates is not ShapeBase.NOT_SET:
                _params['response_templates'] = response_templates
            if content_handling is not ShapeBase.NOT_SET:
                _params['content_handling'] = content_handling
            _request = shapes.PutIntegrationResponseRequest(**_params)
        response = self._boto_client.put_integration_response(
            **_request.to_boto()
        )

        return shapes.IntegrationResponse.from_boto(response)

    def put_method(
        self,
        _request: shapes.PutMethodRequest = None,
        *,
        rest_api_id: str,
        resource_id: str,
        http_method: str,
        authorization_type: str,
        authorizer_id: str = ShapeBase.NOT_SET,
        api_key_required: bool = ShapeBase.NOT_SET,
        operation_name: str = ShapeBase.NOT_SET,
        request_parameters: typing.Dict[str, bool] = ShapeBase.NOT_SET,
        request_models: typing.Dict[str, str] = ShapeBase.NOT_SET,
        request_validator_id: str = ShapeBase.NOT_SET,
        authorization_scopes: typing.List[str] = ShapeBase.NOT_SET,
    ) -> shapes.Method:
        """
        Add a method to an existing Resource resource.
        """
        if _request is None:
            _params = {}
            if rest_api_id is not ShapeBase.NOT_SET:
                _params['rest_api_id'] = rest_api_id
            if resource_id is not ShapeBase.NOT_SET:
                _params['resource_id'] = resource_id
            if http_method is not ShapeBase.NOT_SET:
                _params['http_method'] = http_method
            if authorization_type is not ShapeBase.NOT_SET:
                _params['authorization_type'] = authorization_type
            if authorizer_id is not ShapeBase.NOT_SET:
                _params['authorizer_id'] = authorizer_id
            if api_key_required is not ShapeBase.NOT_SET:
                _params['api_key_required'] = api_key_required
            if operation_name is not ShapeBase.NOT_SET:
                _params['operation_name'] = operation_name
            if request_parameters is not ShapeBase.NOT_SET:
                _params['request_parameters'] = request_parameters
            if request_models is not ShapeBase.NOT_SET:
                _params['request_models'] = request_models
            if request_validator_id is not ShapeBase.NOT_SET:
                _params['request_validator_id'] = request_validator_id
            if authorization_scopes is not ShapeBase.NOT_SET:
                _params['authorization_scopes'] = authorization_scopes
            _request = shapes.PutMethodRequest(**_params)
        response = self._boto_client.put_method(**_request.to_boto())

        return shapes.Method.from_boto(response)

    def put_method_response(
        self,
        _request: shapes.PutMethodResponseRequest = None,
        *,
        rest_api_id: str,
        resource_id: str,
        http_method: str,
        status_code: str,
        response_parameters: typing.Dict[str, bool] = ShapeBase.NOT_SET,
        response_models: typing.Dict[str, str] = ShapeBase.NOT_SET,
    ) -> shapes.MethodResponse:
        """
        Adds a MethodResponse to an existing Method resource.
        """
        if _request is None:
            _params = {}
            if rest_api_id is not ShapeBase.NOT_SET:
                _params['rest_api_id'] = rest_api_id
            if resource_id is not ShapeBase.NOT_SET:
                _params['resource_id'] = resource_id
            if http_method is not ShapeBase.NOT_SET:
                _params['http_method'] = http_method
            if status_code is not ShapeBase.NOT_SET:
                _params['status_code'] = status_code
            if response_parameters is not ShapeBase.NOT_SET:
                _params['response_parameters'] = response_parameters
            if response_models is not ShapeBase.NOT_SET:
                _params['response_models'] = response_models
            _request = shapes.PutMethodResponseRequest(**_params)
        response = self._boto_client.put_method_response(**_request.to_boto())

        return shapes.MethodResponse.from_boto(response)

    def put_rest_api(
        self,
        _request: shapes.PutRestApiRequest = None,
        *,
        rest_api_id: str,
        body: typing.Any,
        mode: typing.Union[str, shapes.PutMode] = ShapeBase.NOT_SET,
        fail_on_warnings: bool = ShapeBase.NOT_SET,
        parameters: typing.Dict[str, str] = ShapeBase.NOT_SET,
    ) -> shapes.RestApi:
        """
        A feature of the API Gateway control service for updating an existing API with
        an input of external API definitions. The update can take the form of merging
        the supplied definition into the existing API or overwriting the existing API.
        """
        if _request is None:
            _params = {}
            if rest_api_id is not ShapeBase.NOT_SET:
                _params['rest_api_id'] = rest_api_id
            if body is not ShapeBase.NOT_SET:
                _params['body'] = body
            if mode is not ShapeBase.NOT_SET:
                _params['mode'] = mode
            if fail_on_warnings is not ShapeBase.NOT_SET:
                _params['fail_on_warnings'] = fail_on_warnings
            if parameters is not ShapeBase.NOT_SET:
                _params['parameters'] = parameters
            _request = shapes.PutRestApiRequest(**_params)
        response = self._boto_client.put_rest_api(**_request.to_boto())

        return shapes.RestApi.from_boto(response)

    def tag_resource(
        self,
        _request: shapes.TagResourceRequest = None,
        *,
        resource_arn: str,
        tags: typing.Dict[str, str],
    ) -> None:
        """
        Adds or updates a tag on a given resource.
        """
        if _request is None:
            _params = {}
            if resource_arn is not ShapeBase.NOT_SET:
                _params['resource_arn'] = resource_arn
            if tags is not ShapeBase.NOT_SET:
                _params['tags'] = tags
            _request = shapes.TagResourceRequest(**_params)
        response = self._boto_client.tag_resource(**_request.to_boto())

    def test_invoke_authorizer(
        self,
        _request: shapes.TestInvokeAuthorizerRequest = None,
        *,
        rest_api_id: str,
        authorizer_id: str,
        headers: typing.Dict[str, str] = ShapeBase.NOT_SET,
        path_with_query_string: str = ShapeBase.NOT_SET,
        body: str = ShapeBase.NOT_SET,
        stage_variables: typing.Dict[str, str] = ShapeBase.NOT_SET,
        additional_context: typing.Dict[str, str] = ShapeBase.NOT_SET,
    ) -> shapes.TestInvokeAuthorizerResponse:
        """
        Simulate the execution of an Authorizer in your RestApi with headers,
        parameters, and an incoming request body.

        [Enable custom
        authorizers](http://docs.aws.amazon.com/apigateway/latest/developerguide/use-
        custom-authorizer.html)
        """
        if _request is None:
            _params = {}
            if rest_api_id is not ShapeBase.NOT_SET:
                _params['rest_api_id'] = rest_api_id
            if authorizer_id is not ShapeBase.NOT_SET:
                _params['authorizer_id'] = authorizer_id
            if headers is not ShapeBase.NOT_SET:
                _params['headers'] = headers
            if path_with_query_string is not ShapeBase.NOT_SET:
                _params['path_with_query_string'] = path_with_query_string
            if body is not ShapeBase.NOT_SET:
                _params['body'] = body
            if stage_variables is not ShapeBase.NOT_SET:
                _params['stage_variables'] = stage_variables
            if additional_context is not ShapeBase.NOT_SET:
                _params['additional_context'] = additional_context
            _request = shapes.TestInvokeAuthorizerRequest(**_params)
        response = self._boto_client.test_invoke_authorizer(
            **_request.to_boto()
        )

        return shapes.TestInvokeAuthorizerResponse.from_boto(response)

    def test_invoke_method(
        self,
        _request: shapes.TestInvokeMethodRequest = None,
        *,
        rest_api_id: str,
        resource_id: str,
        http_method: str,
        path_with_query_string: str = ShapeBase.NOT_SET,
        body: str = ShapeBase.NOT_SET,
        headers: typing.Dict[str, str] = ShapeBase.NOT_SET,
        client_certificate_id: str = ShapeBase.NOT_SET,
        stage_variables: typing.Dict[str, str] = ShapeBase.NOT_SET,
    ) -> shapes.TestInvokeMethodResponse:
        """
        Simulate the execution of a Method in your RestApi with headers, parameters, and
        an incoming request body.
        """
        if _request is None:
            _params = {}
            if rest_api_id is not ShapeBase.NOT_SET:
                _params['rest_api_id'] = rest_api_id
            if resource_id is not ShapeBase.NOT_SET:
                _params['resource_id'] = resource_id
            if http_method is not ShapeBase.NOT_SET:
                _params['http_method'] = http_method
            if path_with_query_string is not ShapeBase.NOT_SET:
                _params['path_with_query_string'] = path_with_query_string
            if body is not ShapeBase.NOT_SET:
                _params['body'] = body
            if headers is not ShapeBase.NOT_SET:
                _params['headers'] = headers
            if client_certificate_id is not ShapeBase.NOT_SET:
                _params['client_certificate_id'] = client_certificate_id
            if stage_variables is not ShapeBase.NOT_SET:
                _params['stage_variables'] = stage_variables
            _request = shapes.TestInvokeMethodRequest(**_params)
        response = self._boto_client.test_invoke_method(**_request.to_boto())

        return shapes.TestInvokeMethodResponse.from_boto(response)

    def untag_resource(
        self,
        _request: shapes.UntagResourceRequest = None,
        *,
        resource_arn: str,
        tag_keys: typing.List[str],
    ) -> None:
        """
        Removes a tag from a given resource.
        """
        if _request is None:
            _params = {}
            if resource_arn is not ShapeBase.NOT_SET:
                _params['resource_arn'] = resource_arn
            if tag_keys is not ShapeBase.NOT_SET:
                _params['tag_keys'] = tag_keys
            _request = shapes.UntagResourceRequest(**_params)
        response = self._boto_client.untag_resource(**_request.to_boto())

    def update_account(
        self,
        _request: shapes.UpdateAccountRequest = None,
        *,
        patch_operations: typing.List[shapes.PatchOperation
                                     ] = ShapeBase.NOT_SET,
    ) -> shapes.Account:
        """
        Changes information about the current Account resource.
        """
        if _request is None:
            _params = {}
            if patch_operations is not ShapeBase.NOT_SET:
                _params['patch_operations'] = patch_operations
            _request = shapes.UpdateAccountRequest(**_params)
        response = self._boto_client.update_account(**_request.to_boto())

        return shapes.Account.from_boto(response)

    def update_api_key(
        self,
        _request: shapes.UpdateApiKeyRequest = None,
        *,
        api_key: str,
        patch_operations: typing.List[shapes.PatchOperation
                                     ] = ShapeBase.NOT_SET,
    ) -> shapes.ApiKey:
        """
        Changes information about an ApiKey resource.
        """
        if _request is None:
            _params = {}
            if api_key is not ShapeBase.NOT_SET:
                _params['api_key'] = api_key
            if patch_operations is not ShapeBase.NOT_SET:
                _params['patch_operations'] = patch_operations
            _request = shapes.UpdateApiKeyRequest(**_params)
        response = self._boto_client.update_api_key(**_request.to_boto())

        return shapes.ApiKey.from_boto(response)

    def update_authorizer(
        self,
        _request: shapes.UpdateAuthorizerRequest = None,
        *,
        rest_api_id: str,
        authorizer_id: str,
        patch_operations: typing.List[shapes.PatchOperation
                                     ] = ShapeBase.NOT_SET,
    ) -> shapes.Authorizer:
        """
        Updates an existing Authorizer resource.

        [AWS CLI](http://docs.aws.amazon.com/cli/latest/reference/apigateway/update-
        authorizer.html)
        """
        if _request is None:
            _params = {}
            if rest_api_id is not ShapeBase.NOT_SET:
                _params['rest_api_id'] = rest_api_id
            if authorizer_id is not ShapeBase.NOT_SET:
                _params['authorizer_id'] = authorizer_id
            if patch_operations is not ShapeBase.NOT_SET:
                _params['patch_operations'] = patch_operations
            _request = shapes.UpdateAuthorizerRequest(**_params)
        response = self._boto_client.update_authorizer(**_request.to_boto())

        return shapes.Authorizer.from_boto(response)

    def update_base_path_mapping(
        self,
        _request: shapes.UpdateBasePathMappingRequest = None,
        *,
        domain_name: str,
        base_path: str,
        patch_operations: typing.List[shapes.PatchOperation
                                     ] = ShapeBase.NOT_SET,
    ) -> shapes.BasePathMapping:
        """
        Changes information about the BasePathMapping resource.
        """
        if _request is None:
            _params = {}
            if domain_name is not ShapeBase.NOT_SET:
                _params['domain_name'] = domain_name
            if base_path is not ShapeBase.NOT_SET:
                _params['base_path'] = base_path
            if patch_operations is not ShapeBase.NOT_SET:
                _params['patch_operations'] = patch_operations
            _request = shapes.UpdateBasePathMappingRequest(**_params)
        response = self._boto_client.update_base_path_mapping(
            **_request.to_boto()
        )

        return shapes.BasePathMapping.from_boto(response)

    def update_client_certificate(
        self,
        _request: shapes.UpdateClientCertificateRequest = None,
        *,
        client_certificate_id: str,
        patch_operations: typing.List[shapes.PatchOperation
                                     ] = ShapeBase.NOT_SET,
    ) -> shapes.ClientCertificate:
        """
        Changes information about an ClientCertificate resource.
        """
        if _request is None:
            _params = {}
            if client_certificate_id is not ShapeBase.NOT_SET:
                _params['client_certificate_id'] = client_certificate_id
            if patch_operations is not ShapeBase.NOT_SET:
                _params['patch_operations'] = patch_operations
            _request = shapes.UpdateClientCertificateRequest(**_params)
        response = self._boto_client.update_client_certificate(
            **_request.to_boto()
        )

        return shapes.ClientCertificate.from_boto(response)

    def update_deployment(
        self,
        _request: shapes.UpdateDeploymentRequest = None,
        *,
        rest_api_id: str,
        deployment_id: str,
        patch_operations: typing.List[shapes.PatchOperation
                                     ] = ShapeBase.NOT_SET,
    ) -> shapes.Deployment:
        """
        Changes information about a Deployment resource.
        """
        if _request is None:
            _params = {}
            if rest_api_id is not ShapeBase.NOT_SET:
                _params['rest_api_id'] = rest_api_id
            if deployment_id is not ShapeBase.NOT_SET:
                _params['deployment_id'] = deployment_id
            if patch_operations is not ShapeBase.NOT_SET:
                _params['patch_operations'] = patch_operations
            _request = shapes.UpdateDeploymentRequest(**_params)
        response = self._boto_client.update_deployment(**_request.to_boto())

        return shapes.Deployment.from_boto(response)

    def update_documentation_part(
        self,
        _request: shapes.UpdateDocumentationPartRequest = None,
        *,
        rest_api_id: str,
        documentation_part_id: str,
        patch_operations: typing.List[shapes.PatchOperation
                                     ] = ShapeBase.NOT_SET,
    ) -> shapes.DocumentationPart:
        if _request is None:
            _params = {}
            if rest_api_id is not ShapeBase.NOT_SET:
                _params['rest_api_id'] = rest_api_id
            if documentation_part_id is not ShapeBase.NOT_SET:
                _params['documentation_part_id'] = documentation_part_id
            if patch_operations is not ShapeBase.NOT_SET:
                _params['patch_operations'] = patch_operations
            _request = shapes.UpdateDocumentationPartRequest(**_params)
        response = self._boto_client.update_documentation_part(
            **_request.to_boto()
        )

        return shapes.DocumentationPart.from_boto(response)

    def update_documentation_version(
        self,
        _request: shapes.UpdateDocumentationVersionRequest = None,
        *,
        rest_api_id: str,
        documentation_version: str,
        patch_operations: typing.List[shapes.PatchOperation
                                     ] = ShapeBase.NOT_SET,
    ) -> shapes.DocumentationVersion:
        if _request is None:
            _params = {}
            if rest_api_id is not ShapeBase.NOT_SET:
                _params['rest_api_id'] = rest_api_id
            if documentation_version is not ShapeBase.NOT_SET:
                _params['documentation_version'] = documentation_version
            if patch_operations is not ShapeBase.NOT_SET:
                _params['patch_operations'] = patch_operations
            _request = shapes.UpdateDocumentationVersionRequest(**_params)
        response = self._boto_client.update_documentation_version(
            **_request.to_boto()
        )

        return shapes.DocumentationVersion.from_boto(response)

    def update_domain_name(
        self,
        _request: shapes.UpdateDomainNameRequest = None,
        *,
        domain_name: str,
        patch_operations: typing.List[shapes.PatchOperation
                                     ] = ShapeBase.NOT_SET,
    ) -> shapes.DomainName:
        """
        Changes information about the DomainName resource.
        """
        if _request is None:
            _params = {}
            if domain_name is not ShapeBase.NOT_SET:
                _params['domain_name'] = domain_name
            if patch_operations is not ShapeBase.NOT_SET:
                _params['patch_operations'] = patch_operations
            _request = shapes.UpdateDomainNameRequest(**_params)
        response = self._boto_client.update_domain_name(**_request.to_boto())

        return shapes.DomainName.from_boto(response)

    def update_gateway_response(
        self,
        _request: shapes.UpdateGatewayResponseRequest = None,
        *,
        rest_api_id: str,
        response_type: typing.Union[str, shapes.GatewayResponseType],
        patch_operations: typing.List[shapes.PatchOperation
                                     ] = ShapeBase.NOT_SET,
    ) -> shapes.GatewayResponse:
        """
        Updates a GatewayResponse of a specified response type on the given RestApi.
        """
        if _request is None:
            _params = {}
            if rest_api_id is not ShapeBase.NOT_SET:
                _params['rest_api_id'] = rest_api_id
            if response_type is not ShapeBase.NOT_SET:
                _params['response_type'] = response_type
            if patch_operations is not ShapeBase.NOT_SET:
                _params['patch_operations'] = patch_operations
            _request = shapes.UpdateGatewayResponseRequest(**_params)
        response = self._boto_client.update_gateway_response(
            **_request.to_boto()
        )

        return shapes.GatewayResponse.from_boto(response)

    def update_integration(
        self,
        _request: shapes.UpdateIntegrationRequest = None,
        *,
        rest_api_id: str,
        resource_id: str,
        http_method: str,
        patch_operations: typing.List[shapes.PatchOperation
                                     ] = ShapeBase.NOT_SET,
    ) -> shapes.Integration:
        """
        Represents an update integration.
        """
        if _request is None:
            _params = {}
            if rest_api_id is not ShapeBase.NOT_SET:
                _params['rest_api_id'] = rest_api_id
            if resource_id is not ShapeBase.NOT_SET:
                _params['resource_id'] = resource_id
            if http_method is not ShapeBase.NOT_SET:
                _params['http_method'] = http_method
            if patch_operations is not ShapeBase.NOT_SET:
                _params['patch_operations'] = patch_operations
            _request = shapes.UpdateIntegrationRequest(**_params)
        response = self._boto_client.update_integration(**_request.to_boto())

        return shapes.Integration.from_boto(response)

    def update_integration_response(
        self,
        _request: shapes.UpdateIntegrationResponseRequest = None,
        *,
        rest_api_id: str,
        resource_id: str,
        http_method: str,
        status_code: str,
        patch_operations: typing.List[shapes.PatchOperation
                                     ] = ShapeBase.NOT_SET,
    ) -> shapes.IntegrationResponse:
        """
        Represents an update integration response.
        """
        if _request is None:
            _params = {}
            if rest_api_id is not ShapeBase.NOT_SET:
                _params['rest_api_id'] = rest_api_id
            if resource_id is not ShapeBase.NOT_SET:
                _params['resource_id'] = resource_id
            if http_method is not ShapeBase.NOT_SET:
                _params['http_method'] = http_method
            if status_code is not ShapeBase.NOT_SET:
                _params['status_code'] = status_code
            if patch_operations is not ShapeBase.NOT_SET:
                _params['patch_operations'] = patch_operations
            _request = shapes.UpdateIntegrationResponseRequest(**_params)
        response = self._boto_client.update_integration_response(
            **_request.to_boto()
        )

        return shapes.IntegrationResponse.from_boto(response)

    def update_method(
        self,
        _request: shapes.UpdateMethodRequest = None,
        *,
        rest_api_id: str,
        resource_id: str,
        http_method: str,
        patch_operations: typing.List[shapes.PatchOperation
                                     ] = ShapeBase.NOT_SET,
    ) -> shapes.Method:
        """
        Updates an existing Method resource.
        """
        if _request is None:
            _params = {}
            if rest_api_id is not ShapeBase.NOT_SET:
                _params['rest_api_id'] = rest_api_id
            if resource_id is not ShapeBase.NOT_SET:
                _params['resource_id'] = resource_id
            if http_method is not ShapeBase.NOT_SET:
                _params['http_method'] = http_method
            if patch_operations is not ShapeBase.NOT_SET:
                _params['patch_operations'] = patch_operations
            _request = shapes.UpdateMethodRequest(**_params)
        response = self._boto_client.update_method(**_request.to_boto())

        return shapes.Method.from_boto(response)

    def update_method_response(
        self,
        _request: shapes.UpdateMethodResponseRequest = None,
        *,
        rest_api_id: str,
        resource_id: str,
        http_method: str,
        status_code: str,
        patch_operations: typing.List[shapes.PatchOperation
                                     ] = ShapeBase.NOT_SET,
    ) -> shapes.MethodResponse:
        """
        Updates an existing MethodResponse resource.
        """
        if _request is None:
            _params = {}
            if rest_api_id is not ShapeBase.NOT_SET:
                _params['rest_api_id'] = rest_api_id
            if resource_id is not ShapeBase.NOT_SET:
                _params['resource_id'] = resource_id
            if http_method is not ShapeBase.NOT_SET:
                _params['http_method'] = http_method
            if status_code is not ShapeBase.NOT_SET:
                _params['status_code'] = status_code
            if patch_operations is not ShapeBase.NOT_SET:
                _params['patch_operations'] = patch_operations
            _request = shapes.UpdateMethodResponseRequest(**_params)
        response = self._boto_client.update_method_response(
            **_request.to_boto()
        )

        return shapes.MethodResponse.from_boto(response)

    def update_model(
        self,
        _request: shapes.UpdateModelRequest = None,
        *,
        rest_api_id: str,
        model_name: str,
        patch_operations: typing.List[shapes.PatchOperation
                                     ] = ShapeBase.NOT_SET,
    ) -> shapes.Model:
        """
        Changes information about a model.
        """
        if _request is None:
            _params = {}
            if rest_api_id is not ShapeBase.NOT_SET:
                _params['rest_api_id'] = rest_api_id
            if model_name is not ShapeBase.NOT_SET:
                _params['model_name'] = model_name
            if patch_operations is not ShapeBase.NOT_SET:
                _params['patch_operations'] = patch_operations
            _request = shapes.UpdateModelRequest(**_params)
        response = self._boto_client.update_model(**_request.to_boto())

        return shapes.Model.from_boto(response)

    def update_request_validator(
        self,
        _request: shapes.UpdateRequestValidatorRequest = None,
        *,
        rest_api_id: str,
        request_validator_id: str,
        patch_operations: typing.List[shapes.PatchOperation
                                     ] = ShapeBase.NOT_SET,
    ) -> shapes.RequestValidator:
        """
        Updates a RequestValidator of a given RestApi.
        """
        if _request is None:
            _params = {}
            if rest_api_id is not ShapeBase.NOT_SET:
                _params['rest_api_id'] = rest_api_id
            if request_validator_id is not ShapeBase.NOT_SET:
                _params['request_validator_id'] = request_validator_id
            if patch_operations is not ShapeBase.NOT_SET:
                _params['patch_operations'] = patch_operations
            _request = shapes.UpdateRequestValidatorRequest(**_params)
        response = self._boto_client.update_request_validator(
            **_request.to_boto()
        )

        return shapes.RequestValidator.from_boto(response)

    def update_resource(
        self,
        _request: shapes.UpdateResourceRequest = None,
        *,
        rest_api_id: str,
        resource_id: str,
        patch_operations: typing.List[shapes.PatchOperation
                                     ] = ShapeBase.NOT_SET,
    ) -> shapes.Resource:
        """
        Changes information about a Resource resource.
        """
        if _request is None:
            _params = {}
            if rest_api_id is not ShapeBase.NOT_SET:
                _params['rest_api_id'] = rest_api_id
            if resource_id is not ShapeBase.NOT_SET:
                _params['resource_id'] = resource_id
            if patch_operations is not ShapeBase.NOT_SET:
                _params['patch_operations'] = patch_operations
            _request = shapes.UpdateResourceRequest(**_params)
        response = self._boto_client.update_resource(**_request.to_boto())

        return shapes.Resource.from_boto(response)

    def update_rest_api(
        self,
        _request: shapes.UpdateRestApiRequest = None,
        *,
        rest_api_id: str,
        patch_operations: typing.List[shapes.PatchOperation
                                     ] = ShapeBase.NOT_SET,
    ) -> shapes.RestApi:
        """
        Changes information about the specified API.
        """
        if _request is None:
            _params = {}
            if rest_api_id is not ShapeBase.NOT_SET:
                _params['rest_api_id'] = rest_api_id
            if patch_operations is not ShapeBase.NOT_SET:
                _params['patch_operations'] = patch_operations
            _request = shapes.UpdateRestApiRequest(**_params)
        response = self._boto_client.update_rest_api(**_request.to_boto())

        return shapes.RestApi.from_boto(response)

    def update_stage(
        self,
        _request: shapes.UpdateStageRequest = None,
        *,
        rest_api_id: str,
        stage_name: str,
        patch_operations: typing.List[shapes.PatchOperation
                                     ] = ShapeBase.NOT_SET,
    ) -> shapes.Stage:
        """
        Changes information about a Stage resource.
        """
        if _request is None:
            _params = {}
            if rest_api_id is not ShapeBase.NOT_SET:
                _params['rest_api_id'] = rest_api_id
            if stage_name is not ShapeBase.NOT_SET:
                _params['stage_name'] = stage_name
            if patch_operations is not ShapeBase.NOT_SET:
                _params['patch_operations'] = patch_operations
            _request = shapes.UpdateStageRequest(**_params)
        response = self._boto_client.update_stage(**_request.to_boto())

        return shapes.Stage.from_boto(response)

    def update_usage(
        self,
        _request: shapes.UpdateUsageRequest = None,
        *,
        usage_plan_id: str,
        key_id: str,
        patch_operations: typing.List[shapes.PatchOperation
                                     ] = ShapeBase.NOT_SET,
    ) -> shapes.Usage:
        """
        Grants a temporary extension to the remaining quota of a usage plan associated
        with a specified API key.
        """
        if _request is None:
            _params = {}
            if usage_plan_id is not ShapeBase.NOT_SET:
                _params['usage_plan_id'] = usage_plan_id
            if key_id is not ShapeBase.NOT_SET:
                _params['key_id'] = key_id
            if patch_operations is not ShapeBase.NOT_SET:
                _params['patch_operations'] = patch_operations
            _request = shapes.UpdateUsageRequest(**_params)
        response = self._boto_client.update_usage(**_request.to_boto())

        return shapes.Usage.from_boto(response)

    def update_usage_plan(
        self,
        _request: shapes.UpdateUsagePlanRequest = None,
        *,
        usage_plan_id: str,
        patch_operations: typing.List[shapes.PatchOperation
                                     ] = ShapeBase.NOT_SET,
    ) -> shapes.UsagePlan:
        """
        Updates a usage plan of a given plan Id.
        """
        if _request is None:
            _params = {}
            if usage_plan_id is not ShapeBase.NOT_SET:
                _params['usage_plan_id'] = usage_plan_id
            if patch_operations is not ShapeBase.NOT_SET:
                _params['patch_operations'] = patch_operations
            _request = shapes.UpdateUsagePlanRequest(**_params)
        response = self._boto_client.update_usage_plan(**_request.to_boto())

        return shapes.UsagePlan.from_boto(response)

    def update_vpc_link(
        self,
        _request: shapes.UpdateVpcLinkRequest = None,
        *,
        vpc_link_id: str,
        patch_operations: typing.List[shapes.PatchOperation
                                     ] = ShapeBase.NOT_SET,
    ) -> shapes.VpcLink:
        """
        Updates an existing VpcLink of a specified identifier.
        """
        if _request is None:
            _params = {}
            if vpc_link_id is not ShapeBase.NOT_SET:
                _params['vpc_link_id'] = vpc_link_id
            if patch_operations is not ShapeBase.NOT_SET:
                _params['patch_operations'] = patch_operations
            _request = shapes.UpdateVpcLinkRequest(**_params)
        response = self._boto_client.update_vpc_link(**_request.to_boto())

        return shapes.VpcLink.from_boto(response)
