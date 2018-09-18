import datetime
import typing
import boto3
from autoboto import ClientBase, ShapeBase, OutputShapeBase
from . import shapes


class Client(ClientBase):
    def __init__(self, *args, **kwargs):
        super().__init__("lambda", *args, **kwargs)

    def add_permission(
        self,
        _request: shapes.AddPermissionRequest = None,
        *,
        function_name: str,
        statement_id: str,
        action: str,
        principal: str,
        source_arn: str = ShapeBase.NOT_SET,
        source_account: str = ShapeBase.NOT_SET,
        event_source_token: str = ShapeBase.NOT_SET,
        qualifier: str = ShapeBase.NOT_SET,
        revision_id: str = ShapeBase.NOT_SET,
    ) -> shapes.AddPermissionResponse:
        """
        Adds a permission to the resource policy associated with the specified AWS
        Lambda function. You use resource policies to grant permissions to event sources
        that use _push_ model. In a _push_ model, event sources (such as Amazon S3 and
        custom applications) invoke your Lambda function. Each permission you add to the
        resource policy allows an event source, permission to invoke the Lambda
        function.

        For information about the push model, see [Lambda
        Functions](http://docs.aws.amazon.com/lambda/latest/dg/lambda-
        introduction.html).

        If you are using versioning, the permissions you add are specific to the Lambda
        function version or alias you specify in the `AddPermission` request via the
        `Qualifier` parameter. For more information about versioning, see [AWS Lambda
        Function Versioning and
        Aliases](http://docs.aws.amazon.com/lambda/latest/dg/versioning-aliases.html).

        This operation requires permission for the `lambda:AddPermission` action.
        """
        if _request is None:
            _params = {}
            if function_name is not ShapeBase.NOT_SET:
                _params['function_name'] = function_name
            if statement_id is not ShapeBase.NOT_SET:
                _params['statement_id'] = statement_id
            if action is not ShapeBase.NOT_SET:
                _params['action'] = action
            if principal is not ShapeBase.NOT_SET:
                _params['principal'] = principal
            if source_arn is not ShapeBase.NOT_SET:
                _params['source_arn'] = source_arn
            if source_account is not ShapeBase.NOT_SET:
                _params['source_account'] = source_account
            if event_source_token is not ShapeBase.NOT_SET:
                _params['event_source_token'] = event_source_token
            if qualifier is not ShapeBase.NOT_SET:
                _params['qualifier'] = qualifier
            if revision_id is not ShapeBase.NOT_SET:
                _params['revision_id'] = revision_id
            _request = shapes.AddPermissionRequest(**_params)
        response = self._boto_client.add_permission(**_request.to_boto())

        return shapes.AddPermissionResponse.from_boto(response)

    def create_alias(
        self,
        _request: shapes.CreateAliasRequest = None,
        *,
        function_name: str,
        name: str,
        function_version: str,
        description: str = ShapeBase.NOT_SET,
        routing_config: shapes.AliasRoutingConfiguration = ShapeBase.NOT_SET,
    ) -> shapes.AliasConfiguration:
        """
        Creates an alias that points to the specified Lambda function version. For more
        information, see [Introduction to AWS Lambda
        Aliases](http://docs.aws.amazon.com/lambda/latest/dg/aliases-intro.html).

        Alias names are unique for a given function. This requires permission for the
        lambda:CreateAlias action.
        """
        if _request is None:
            _params = {}
            if function_name is not ShapeBase.NOT_SET:
                _params['function_name'] = function_name
            if name is not ShapeBase.NOT_SET:
                _params['name'] = name
            if function_version is not ShapeBase.NOT_SET:
                _params['function_version'] = function_version
            if description is not ShapeBase.NOT_SET:
                _params['description'] = description
            if routing_config is not ShapeBase.NOT_SET:
                _params['routing_config'] = routing_config
            _request = shapes.CreateAliasRequest(**_params)
        response = self._boto_client.create_alias(**_request.to_boto())

        return shapes.AliasConfiguration.from_boto(response)

    def create_event_source_mapping(
        self,
        _request: shapes.CreateEventSourceMappingRequest = None,
        *,
        event_source_arn: str,
        function_name: str,
        enabled: bool = ShapeBase.NOT_SET,
        batch_size: int = ShapeBase.NOT_SET,
        starting_position: typing.
        Union[str, shapes.EventSourcePosition] = ShapeBase.NOT_SET,
        starting_position_timestamp: datetime.datetime = ShapeBase.NOT_SET,
    ) -> shapes.EventSourceMappingConfiguration:
        """
        Identifies a poll-based event source for a Lambda function. It can be either an
        Amazon Kinesis or DynamoDB stream, or an Amazon SQS queue. AWS Lambda invokes
        the specified function when records are posted to the event source.

        This association between a poll-based source and a Lambda function is called the
        event source mapping.

        You provide mapping information (for example, which stream or SQS queue to read
        from and which Lambda function to invoke) in the request body.

        Amazon Kinesis or DynamoDB stream event sources can be associated with multiple
        AWS Lambda functions and a given Lambda function can be associated with multiple
        AWS event sources. For Amazon SQS, you can configure multiple queues as event
        sources for a single Lambda function, but an SQS queue can be mapped only to a
        single Lambda function.

        If you are using versioning, you can specify a specific function version or an
        alias via the function name parameter. For more information about versioning,
        see [AWS Lambda Function Versioning and
        Aliases](http://docs.aws.amazon.com/lambda/latest/dg/versioning-aliases.html).

        This operation requires permission for the `lambda:CreateEventSourceMapping`
        action.
        """
        if _request is None:
            _params = {}
            if event_source_arn is not ShapeBase.NOT_SET:
                _params['event_source_arn'] = event_source_arn
            if function_name is not ShapeBase.NOT_SET:
                _params['function_name'] = function_name
            if enabled is not ShapeBase.NOT_SET:
                _params['enabled'] = enabled
            if batch_size is not ShapeBase.NOT_SET:
                _params['batch_size'] = batch_size
            if starting_position is not ShapeBase.NOT_SET:
                _params['starting_position'] = starting_position
            if starting_position_timestamp is not ShapeBase.NOT_SET:
                _params['starting_position_timestamp'
                       ] = starting_position_timestamp
            _request = shapes.CreateEventSourceMappingRequest(**_params)
        response = self._boto_client.create_event_source_mapping(
            **_request.to_boto()
        )

        return shapes.EventSourceMappingConfiguration.from_boto(response)

    def create_function(
        self,
        _request: shapes.CreateFunctionRequest = None,
        *,
        function_name: str,
        runtime: typing.Union[str, shapes.Runtime],
        role: str,
        handler: str,
        code: shapes.FunctionCode,
        description: str = ShapeBase.NOT_SET,
        timeout: int = ShapeBase.NOT_SET,
        memory_size: int = ShapeBase.NOT_SET,
        publish: bool = ShapeBase.NOT_SET,
        vpc_config: shapes.VpcConfig = ShapeBase.NOT_SET,
        dead_letter_config: shapes.DeadLetterConfig = ShapeBase.NOT_SET,
        environment: shapes.Environment = ShapeBase.NOT_SET,
        kms_key_arn: str = ShapeBase.NOT_SET,
        tracing_config: shapes.TracingConfig = ShapeBase.NOT_SET,
        tags: typing.Dict[str, str] = ShapeBase.NOT_SET,
    ) -> shapes.FunctionConfiguration:
        """
        Creates a new Lambda function. The function metadata is created from the request
        parameters, and the code for the function is provided by a .zip file in the
        request body. If the function name already exists, the operation will fail. Note
        that the function name is case-sensitive.

        If you are using versioning, you can also publish a version of the Lambda
        function you are creating using the `Publish` parameter. For more information
        about versioning, see [AWS Lambda Function Versioning and
        Aliases](http://docs.aws.amazon.com/lambda/latest/dg/versioning-aliases.html).

        This operation requires permission for the `lambda:CreateFunction` action.
        """
        if _request is None:
            _params = {}
            if function_name is not ShapeBase.NOT_SET:
                _params['function_name'] = function_name
            if runtime is not ShapeBase.NOT_SET:
                _params['runtime'] = runtime
            if role is not ShapeBase.NOT_SET:
                _params['role'] = role
            if handler is not ShapeBase.NOT_SET:
                _params['handler'] = handler
            if code is not ShapeBase.NOT_SET:
                _params['code'] = code
            if description is not ShapeBase.NOT_SET:
                _params['description'] = description
            if timeout is not ShapeBase.NOT_SET:
                _params['timeout'] = timeout
            if memory_size is not ShapeBase.NOT_SET:
                _params['memory_size'] = memory_size
            if publish is not ShapeBase.NOT_SET:
                _params['publish'] = publish
            if vpc_config is not ShapeBase.NOT_SET:
                _params['vpc_config'] = vpc_config
            if dead_letter_config is not ShapeBase.NOT_SET:
                _params['dead_letter_config'] = dead_letter_config
            if environment is not ShapeBase.NOT_SET:
                _params['environment'] = environment
            if kms_key_arn is not ShapeBase.NOT_SET:
                _params['kms_key_arn'] = kms_key_arn
            if tracing_config is not ShapeBase.NOT_SET:
                _params['tracing_config'] = tracing_config
            if tags is not ShapeBase.NOT_SET:
                _params['tags'] = tags
            _request = shapes.CreateFunctionRequest(**_params)
        response = self._boto_client.create_function(**_request.to_boto())

        return shapes.FunctionConfiguration.from_boto(response)

    def delete_alias(
        self,
        _request: shapes.DeleteAliasRequest = None,
        *,
        function_name: str,
        name: str,
    ) -> None:
        """
        Deletes the specified Lambda function alias. For more information, see
        [Introduction to AWS Lambda
        Aliases](http://docs.aws.amazon.com/lambda/latest/dg/aliases-intro.html).

        This requires permission for the lambda:DeleteAlias action.
        """
        if _request is None:
            _params = {}
            if function_name is not ShapeBase.NOT_SET:
                _params['function_name'] = function_name
            if name is not ShapeBase.NOT_SET:
                _params['name'] = name
            _request = shapes.DeleteAliasRequest(**_params)
        response = self._boto_client.delete_alias(**_request.to_boto())

    def delete_event_source_mapping(
        self,
        _request: shapes.DeleteEventSourceMappingRequest = None,
        *,
        uuid: str,
    ) -> shapes.EventSourceMappingConfiguration:
        """
        Removes an event source mapping. This means AWS Lambda will no longer invoke the
        function for events in the associated source.

        This operation requires permission for the `lambda:DeleteEventSourceMapping`
        action.
        """
        if _request is None:
            _params = {}
            if uuid is not ShapeBase.NOT_SET:
                _params['uuid'] = uuid
            _request = shapes.DeleteEventSourceMappingRequest(**_params)
        response = self._boto_client.delete_event_source_mapping(
            **_request.to_boto()
        )

        return shapes.EventSourceMappingConfiguration.from_boto(response)

    def delete_function(
        self,
        _request: shapes.DeleteFunctionRequest = None,
        *,
        function_name: str,
        qualifier: str = ShapeBase.NOT_SET,
    ) -> None:
        """
        Deletes the specified Lambda function code and configuration.

        If you are using the versioning feature and you don't specify a function version
        in your `DeleteFunction` request, AWS Lambda will delete the function, including
        all its versions, and any aliases pointing to the function versions. To delete a
        specific function version, you must provide the function version via the
        `Qualifier` parameter. For information about function versioning, see [AWS
        Lambda Function Versioning and
        Aliases](http://docs.aws.amazon.com/lambda/latest/dg/versioning-aliases.html).

        When you delete a function the associated resource policy is also deleted. You
        will need to delete the event source mappings explicitly.

        This operation requires permission for the `lambda:DeleteFunction` action.
        """
        if _request is None:
            _params = {}
            if function_name is not ShapeBase.NOT_SET:
                _params['function_name'] = function_name
            if qualifier is not ShapeBase.NOT_SET:
                _params['qualifier'] = qualifier
            _request = shapes.DeleteFunctionRequest(**_params)
        response = self._boto_client.delete_function(**_request.to_boto())

    def delete_function_concurrency(
        self,
        _request: shapes.DeleteFunctionConcurrencyRequest = None,
        *,
        function_name: str,
    ) -> None:
        """
        Removes concurrent execution limits from this function. For more information,
        see concurrent-executions.
        """
        if _request is None:
            _params = {}
            if function_name is not ShapeBase.NOT_SET:
                _params['function_name'] = function_name
            _request = shapes.DeleteFunctionConcurrencyRequest(**_params)
        response = self._boto_client.delete_function_concurrency(
            **_request.to_boto()
        )

    def get_account_settings(
        self,
        _request: shapes.GetAccountSettingsRequest = None,
    ) -> shapes.GetAccountSettingsResponse:
        """
        Returns a customer's account settings.

        You can use this operation to retrieve Lambda limits information, such as code
        size and concurrency limits. For more information about limits, see [AWS Lambda
        Limits](http://docs.aws.amazon.com/lambda/latest/dg/limits.html). You can also
        retrieve resource usage statistics, such as code storage usage and function
        count.
        """
        if _request is None:
            _params = {}
            _request = shapes.GetAccountSettingsRequest(**_params)
        response = self._boto_client.get_account_settings(**_request.to_boto())

        return shapes.GetAccountSettingsResponse.from_boto(response)

    def get_alias(
        self,
        _request: shapes.GetAliasRequest = None,
        *,
        function_name: str,
        name: str,
    ) -> shapes.AliasConfiguration:
        """
        Returns the specified alias information such as the alias ARN, description, and
        function version it is pointing to. For more information, see [Introduction to
        AWS Lambda Aliases](http://docs.aws.amazon.com/lambda/latest/dg/aliases-
        intro.html).

        This requires permission for the `lambda:GetAlias` action.
        """
        if _request is None:
            _params = {}
            if function_name is not ShapeBase.NOT_SET:
                _params['function_name'] = function_name
            if name is not ShapeBase.NOT_SET:
                _params['name'] = name
            _request = shapes.GetAliasRequest(**_params)
        response = self._boto_client.get_alias(**_request.to_boto())

        return shapes.AliasConfiguration.from_boto(response)

    def get_event_source_mapping(
        self,
        _request: shapes.GetEventSourceMappingRequest = None,
        *,
        uuid: str,
    ) -> shapes.EventSourceMappingConfiguration:
        """
        Returns configuration information for the specified event source mapping (see
        CreateEventSourceMapping).

        This operation requires permission for the `lambda:GetEventSourceMapping`
        action.
        """
        if _request is None:
            _params = {}
            if uuid is not ShapeBase.NOT_SET:
                _params['uuid'] = uuid
            _request = shapes.GetEventSourceMappingRequest(**_params)
        response = self._boto_client.get_event_source_mapping(
            **_request.to_boto()
        )

        return shapes.EventSourceMappingConfiguration.from_boto(response)

    def get_function(
        self,
        _request: shapes.GetFunctionRequest = None,
        *,
        function_name: str,
        qualifier: str = ShapeBase.NOT_SET,
    ) -> shapes.GetFunctionResponse:
        """
        Returns the configuration information of the Lambda function and a presigned URL
        link to the .zip file you uploaded with CreateFunction so you can download the
        .zip file. Note that the URL is valid for up to 10 minutes. The configuration
        information is the same information you provided as parameters when uploading
        the function.

        Using the optional `Qualifier` parameter, you can specify a specific function
        version for which you want this information. If you don't specify this
        parameter, the API uses unqualified function ARN which return information about
        the `$LATEST` version of the Lambda function. For more information, see [AWS
        Lambda Function Versioning and
        Aliases](http://docs.aws.amazon.com/lambda/latest/dg/versioning-aliases.html).

        This operation requires permission for the `lambda:GetFunction` action.
        """
        if _request is None:
            _params = {}
            if function_name is not ShapeBase.NOT_SET:
                _params['function_name'] = function_name
            if qualifier is not ShapeBase.NOT_SET:
                _params['qualifier'] = qualifier
            _request = shapes.GetFunctionRequest(**_params)
        response = self._boto_client.get_function(**_request.to_boto())

        return shapes.GetFunctionResponse.from_boto(response)

    def get_function_configuration(
        self,
        _request: shapes.GetFunctionConfigurationRequest = None,
        *,
        function_name: str,
        qualifier: str = ShapeBase.NOT_SET,
    ) -> shapes.FunctionConfiguration:
        """
        Returns the configuration information of the Lambda function. This the same
        information you provided as parameters when uploading the function by using
        CreateFunction.

        If you are using the versioning feature, you can retrieve this information for a
        specific function version by using the optional `Qualifier` parameter and
        specifying the function version or alias that points to it. If you don't provide
        it, the API returns information about the $LATEST version of the function. For
        more information about versioning, see [AWS Lambda Function Versioning and
        Aliases](http://docs.aws.amazon.com/lambda/latest/dg/versioning-aliases.html).

        This operation requires permission for the `lambda:GetFunctionConfiguration`
        operation.
        """
        if _request is None:
            _params = {}
            if function_name is not ShapeBase.NOT_SET:
                _params['function_name'] = function_name
            if qualifier is not ShapeBase.NOT_SET:
                _params['qualifier'] = qualifier
            _request = shapes.GetFunctionConfigurationRequest(**_params)
        response = self._boto_client.get_function_configuration(
            **_request.to_boto()
        )

        return shapes.FunctionConfiguration.from_boto(response)

    def get_policy(
        self,
        _request: shapes.GetPolicyRequest = None,
        *,
        function_name: str,
        qualifier: str = ShapeBase.NOT_SET,
    ) -> shapes.GetPolicyResponse:
        """
        Returns the resource policy associated with the specified Lambda function.

        If you are using the versioning feature, you can get the resource policy
        associated with the specific Lambda function version or alias by specifying the
        version or alias name using the `Qualifier` parameter. For more information
        about versioning, see [AWS Lambda Function Versioning and
        Aliases](http://docs.aws.amazon.com/lambda/latest/dg/versioning-aliases.html).

        You need permission for the `lambda:GetPolicy action.`
        """
        if _request is None:
            _params = {}
            if function_name is not ShapeBase.NOT_SET:
                _params['function_name'] = function_name
            if qualifier is not ShapeBase.NOT_SET:
                _params['qualifier'] = qualifier
            _request = shapes.GetPolicyRequest(**_params)
        response = self._boto_client.get_policy(**_request.to_boto())

        return shapes.GetPolicyResponse.from_boto(response)

    def invoke(
        self,
        _request: shapes.InvocationRequest = None,
        *,
        function_name: str,
        invocation_type: typing.Union[str, shapes.InvocationType] = ShapeBase.
        NOT_SET,
        log_type: typing.Union[str, shapes.LogType] = ShapeBase.NOT_SET,
        client_context: str = ShapeBase.NOT_SET,
        payload: typing.Any = ShapeBase.NOT_SET,
        qualifier: str = ShapeBase.NOT_SET,
    ) -> shapes.InvocationResponse:
        """
        Invokes a specific Lambda function. For an example, see [Create the Lambda
        Function and Test It Manually](http://docs.aws.amazon.com/lambda/latest/dg/with-
        dynamodb-create-function.html#with-dbb-invoke-manually).

        If you are using the versioning feature, you can invoke the specific function
        version by providing function version or alias name that is pointing to the
        function version using the `Qualifier` parameter in the request. If you don't
        provide the `Qualifier` parameter, the `$LATEST` version of the Lambda function
        is invoked. Invocations occur at least once in response to an event and
        functions must be idempotent to handle this. For information about the
        versioning feature, see [AWS Lambda Function Versioning and
        Aliases](http://docs.aws.amazon.com/lambda/latest/dg/versioning-aliases.html).

        This operation requires permission for the `lambda:InvokeFunction` action.

        The `TooManyRequestsException` noted below will return the following:
        `ConcurrentInvocationLimitExceeded` will be returned if you have no functions
        with reserved concurrency and have exceeded your account concurrent limit or if
        a function without reserved concurrency exceeds the account's unreserved
        concurrency limit. `ReservedFunctionConcurrentInvocationLimitExceeded` will be
        returned when a function with reserved concurrency exceeds its configured
        concurrency limit.
        """
        if _request is None:
            _params = {}
            if function_name is not ShapeBase.NOT_SET:
                _params['function_name'] = function_name
            if invocation_type is not ShapeBase.NOT_SET:
                _params['invocation_type'] = invocation_type
            if log_type is not ShapeBase.NOT_SET:
                _params['log_type'] = log_type
            if client_context is not ShapeBase.NOT_SET:
                _params['client_context'] = client_context
            if payload is not ShapeBase.NOT_SET:
                _params['payload'] = payload
            if qualifier is not ShapeBase.NOT_SET:
                _params['qualifier'] = qualifier
            _request = shapes.InvocationRequest(**_params)
        response = self._boto_client.invoke(**_request.to_boto())

        return shapes.InvocationResponse.from_boto(response)

    def invoke_async(
        self,
        _request: shapes.InvokeAsyncRequest = None,
        *,
        function_name: str,
        invoke_args: typing.Any,
    ) -> shapes.InvokeAsyncResponse:
        """
        This API is deprecated. We recommend you use `Invoke` API (see Invoke).

        Submits an invocation request to AWS Lambda. Upon receiving the request, Lambda
        executes the specified function asynchronously. To see the logs generated by the
        Lambda function execution, see the CloudWatch Logs console.

        This operation requires permission for the `lambda:InvokeFunction` action.
        """
        if _request is None:
            _params = {}
            if function_name is not ShapeBase.NOT_SET:
                _params['function_name'] = function_name
            if invoke_args is not ShapeBase.NOT_SET:
                _params['invoke_args'] = invoke_args
            _request = shapes.InvokeAsyncRequest(**_params)
        response = self._boto_client.invoke_async(**_request.to_boto())

        return shapes.InvokeAsyncResponse.from_boto(response)

    def list_aliases(
        self,
        _request: shapes.ListAliasesRequest = None,
        *,
        function_name: str,
        function_version: str = ShapeBase.NOT_SET,
        marker: str = ShapeBase.NOT_SET,
        max_items: int = ShapeBase.NOT_SET,
    ) -> shapes.ListAliasesResponse:
        """
        Returns list of aliases created for a Lambda function. For each alias, the
        response includes information such as the alias ARN, description, alias name,
        and the function version to which it points. For more information, see
        [Introduction to AWS Lambda
        Aliases](http://docs.aws.amazon.com/lambda/latest/dg/aliases-intro.html).

        This requires permission for the lambda:ListAliases action.
        """
        if _request is None:
            _params = {}
            if function_name is not ShapeBase.NOT_SET:
                _params['function_name'] = function_name
            if function_version is not ShapeBase.NOT_SET:
                _params['function_version'] = function_version
            if marker is not ShapeBase.NOT_SET:
                _params['marker'] = marker
            if max_items is not ShapeBase.NOT_SET:
                _params['max_items'] = max_items
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

    def list_event_source_mappings(
        self,
        _request: shapes.ListEventSourceMappingsRequest = None,
        *,
        event_source_arn: str = ShapeBase.NOT_SET,
        function_name: str = ShapeBase.NOT_SET,
        marker: str = ShapeBase.NOT_SET,
        max_items: int = ShapeBase.NOT_SET,
    ) -> shapes.ListEventSourceMappingsResponse:
        """
        Returns a list of event source mappings you created using the
        `CreateEventSourceMapping` (see CreateEventSourceMapping).

        For each mapping, the API returns configuration information. You can optionally
        specify filters to retrieve specific event source mappings.

        If you are using the versioning feature, you can get list of event source
        mappings for a specific Lambda function version or an alias as described in the
        `FunctionName` parameter. For information about the versioning feature, see [AWS
        Lambda Function Versioning and
        Aliases](http://docs.aws.amazon.com/lambda/latest/dg/versioning-aliases.html).

        This operation requires permission for the `lambda:ListEventSourceMappings`
        action.
        """
        if _request is None:
            _params = {}
            if event_source_arn is not ShapeBase.NOT_SET:
                _params['event_source_arn'] = event_source_arn
            if function_name is not ShapeBase.NOT_SET:
                _params['function_name'] = function_name
            if marker is not ShapeBase.NOT_SET:
                _params['marker'] = marker
            if max_items is not ShapeBase.NOT_SET:
                _params['max_items'] = max_items
            _request = shapes.ListEventSourceMappingsRequest(**_params)
        paginator = self.get_paginator("list_event_source_mappings").paginate(
            **_request.to_boto()
        )
        page_generator = (page for page in paginator)
        first_page = next(page_generator)
        result = shapes.ListEventSourceMappingsResponse.from_boto(first_page)
        result._page_iterator = page_generator
        return result

        return shapes.ListEventSourceMappingsResponse.from_boto(response)

    def list_functions(
        self,
        _request: shapes.ListFunctionsRequest = None,
        *,
        master_region: str = ShapeBase.NOT_SET,
        function_version: typing.Union[str, shapes.FunctionVersion] = ShapeBase.
        NOT_SET,
        marker: str = ShapeBase.NOT_SET,
        max_items: int = ShapeBase.NOT_SET,
    ) -> shapes.ListFunctionsResponse:
        """
        Returns a list of your Lambda functions. For each function, the response
        includes the function configuration information. You must use GetFunction to
        retrieve the code for your function.

        This operation requires permission for the `lambda:ListFunctions` action.

        If you are using the versioning feature, you can list all of your functions or
        only `$LATEST` versions. For information about the versioning feature, see [AWS
        Lambda Function Versioning and
        Aliases](http://docs.aws.amazon.com/lambda/latest/dg/versioning-aliases.html).
        """
        if _request is None:
            _params = {}
            if master_region is not ShapeBase.NOT_SET:
                _params['master_region'] = master_region
            if function_version is not ShapeBase.NOT_SET:
                _params['function_version'] = function_version
            if marker is not ShapeBase.NOT_SET:
                _params['marker'] = marker
            if max_items is not ShapeBase.NOT_SET:
                _params['max_items'] = max_items
            _request = shapes.ListFunctionsRequest(**_params)
        paginator = self.get_paginator("list_functions").paginate(
            **_request.to_boto()
        )
        page_generator = (page for page in paginator)
        first_page = next(page_generator)
        result = shapes.ListFunctionsResponse.from_boto(first_page)
        result._page_iterator = page_generator
        return result

        return shapes.ListFunctionsResponse.from_boto(response)

    def list_tags(
        self,
        _request: shapes.ListTagsRequest = None,
        *,
        resource: str,
    ) -> shapes.ListTagsResponse:
        """
        Returns a list of tags assigned to a function when supplied the function ARN
        (Amazon Resource Name). For more information on Tagging, see [Tagging Lambda
        Functions](http://docs.aws.amazon.com/lambda/latest/dg/tagging.html) in the
        **AWS Lambda Developer Guide**.
        """
        if _request is None:
            _params = {}
            if resource is not ShapeBase.NOT_SET:
                _params['resource'] = resource
            _request = shapes.ListTagsRequest(**_params)
        response = self._boto_client.list_tags(**_request.to_boto())

        return shapes.ListTagsResponse.from_boto(response)

    def list_versions_by_function(
        self,
        _request: shapes.ListVersionsByFunctionRequest = None,
        *,
        function_name: str,
        marker: str = ShapeBase.NOT_SET,
        max_items: int = ShapeBase.NOT_SET,
    ) -> shapes.ListVersionsByFunctionResponse:
        """
        List all versions of a function. For information about the versioning feature,
        see [AWS Lambda Function Versioning and
        Aliases](http://docs.aws.amazon.com/lambda/latest/dg/versioning-aliases.html).
        """
        if _request is None:
            _params = {}
            if function_name is not ShapeBase.NOT_SET:
                _params['function_name'] = function_name
            if marker is not ShapeBase.NOT_SET:
                _params['marker'] = marker
            if max_items is not ShapeBase.NOT_SET:
                _params['max_items'] = max_items
            _request = shapes.ListVersionsByFunctionRequest(**_params)
        response = self._boto_client.list_versions_by_function(
            **_request.to_boto()
        )

        return shapes.ListVersionsByFunctionResponse.from_boto(response)

    def publish_version(
        self,
        _request: shapes.PublishVersionRequest = None,
        *,
        function_name: str,
        code_sha256: str = ShapeBase.NOT_SET,
        description: str = ShapeBase.NOT_SET,
        revision_id: str = ShapeBase.NOT_SET,
    ) -> shapes.FunctionConfiguration:
        """
        Publishes a version of your function from the current snapshot of $LATEST. That
        is, AWS Lambda takes a snapshot of the function code and configuration
        information from $LATEST and publishes a new version. The code and configuration
        cannot be modified after publication. For information about the versioning
        feature, see [AWS Lambda Function Versioning and
        Aliases](http://docs.aws.amazon.com/lambda/latest/dg/versioning-aliases.html).
        """
        if _request is None:
            _params = {}
            if function_name is not ShapeBase.NOT_SET:
                _params['function_name'] = function_name
            if code_sha256 is not ShapeBase.NOT_SET:
                _params['code_sha256'] = code_sha256
            if description is not ShapeBase.NOT_SET:
                _params['description'] = description
            if revision_id is not ShapeBase.NOT_SET:
                _params['revision_id'] = revision_id
            _request = shapes.PublishVersionRequest(**_params)
        response = self._boto_client.publish_version(**_request.to_boto())

        return shapes.FunctionConfiguration.from_boto(response)

    def put_function_concurrency(
        self,
        _request: shapes.PutFunctionConcurrencyRequest = None,
        *,
        function_name: str,
        reserved_concurrent_executions: int,
    ) -> shapes.Concurrency:
        """
        Sets a limit on the number of concurrent executions available to this function.
        It is a subset of your account's total concurrent execution limit per region.
        Note that Lambda automatically reserves a buffer of 100 concurrent executions
        for functions without any reserved concurrency limit. This means if your account
        limit is 1000, you have a total of 900 available to allocate to individual
        functions. For more information, see concurrent-executions.
        """
        if _request is None:
            _params = {}
            if function_name is not ShapeBase.NOT_SET:
                _params['function_name'] = function_name
            if reserved_concurrent_executions is not ShapeBase.NOT_SET:
                _params['reserved_concurrent_executions'
                       ] = reserved_concurrent_executions
            _request = shapes.PutFunctionConcurrencyRequest(**_params)
        response = self._boto_client.put_function_concurrency(
            **_request.to_boto()
        )

        return shapes.Concurrency.from_boto(response)

    def remove_permission(
        self,
        _request: shapes.RemovePermissionRequest = None,
        *,
        function_name: str,
        statement_id: str,
        qualifier: str = ShapeBase.NOT_SET,
        revision_id: str = ShapeBase.NOT_SET,
    ) -> None:
        """
        You can remove individual permissions from an resource policy associated with a
        Lambda function by providing a statement ID that you provided when you added the
        permission.

        If you are using versioning, the permissions you remove are specific to the
        Lambda function version or alias you specify in the `AddPermission` request via
        the `Qualifier` parameter. For more information about versioning, see [AWS
        Lambda Function Versioning and
        Aliases](http://docs.aws.amazon.com/lambda/latest/dg/versioning-aliases.html).

        Note that removal of a permission will cause an active event source to lose
        permission to the function.

        You need permission for the `lambda:RemovePermission` action.
        """
        if _request is None:
            _params = {}
            if function_name is not ShapeBase.NOT_SET:
                _params['function_name'] = function_name
            if statement_id is not ShapeBase.NOT_SET:
                _params['statement_id'] = statement_id
            if qualifier is not ShapeBase.NOT_SET:
                _params['qualifier'] = qualifier
            if revision_id is not ShapeBase.NOT_SET:
                _params['revision_id'] = revision_id
            _request = shapes.RemovePermissionRequest(**_params)
        response = self._boto_client.remove_permission(**_request.to_boto())

    def tag_resource(
        self,
        _request: shapes.TagResourceRequest = None,
        *,
        resource: str,
        tags: typing.Dict[str, str],
    ) -> None:
        """
        Creates a list of tags (key-value pairs) on the Lambda function. Requires the
        Lambda function ARN (Amazon Resource Name). If a key is specified without a
        value, Lambda creates a tag with the specified key and a value of null. For more
        information, see [Tagging Lambda
        Functions](http://docs.aws.amazon.com/lambda/latest/dg/tagging.html) in the
        **AWS Lambda Developer Guide**.
        """
        if _request is None:
            _params = {}
            if resource is not ShapeBase.NOT_SET:
                _params['resource'] = resource
            if tags is not ShapeBase.NOT_SET:
                _params['tags'] = tags
            _request = shapes.TagResourceRequest(**_params)
        response = self._boto_client.tag_resource(**_request.to_boto())

    def untag_resource(
        self,
        _request: shapes.UntagResourceRequest = None,
        *,
        resource: str,
        tag_keys: typing.List[str],
    ) -> None:
        """
        Removes tags from a Lambda function. Requires the function ARN (Amazon Resource
        Name). For more information, see [Tagging Lambda
        Functions](http://docs.aws.amazon.com/lambda/latest/dg/tagging.html) in the
        **AWS Lambda Developer Guide**.
        """
        if _request is None:
            _params = {}
            if resource is not ShapeBase.NOT_SET:
                _params['resource'] = resource
            if tag_keys is not ShapeBase.NOT_SET:
                _params['tag_keys'] = tag_keys
            _request = shapes.UntagResourceRequest(**_params)
        response = self._boto_client.untag_resource(**_request.to_boto())

    def update_alias(
        self,
        _request: shapes.UpdateAliasRequest = None,
        *,
        function_name: str,
        name: str,
        function_version: str = ShapeBase.NOT_SET,
        description: str = ShapeBase.NOT_SET,
        routing_config: shapes.AliasRoutingConfiguration = ShapeBase.NOT_SET,
        revision_id: str = ShapeBase.NOT_SET,
    ) -> shapes.AliasConfiguration:
        """
        Using this API you can update the function version to which the alias points and
        the alias description. For more information, see [Introduction to AWS Lambda
        Aliases](http://docs.aws.amazon.com/lambda/latest/dg/aliases-intro.html).

        This requires permission for the lambda:UpdateAlias action.
        """
        if _request is None:
            _params = {}
            if function_name is not ShapeBase.NOT_SET:
                _params['function_name'] = function_name
            if name is not ShapeBase.NOT_SET:
                _params['name'] = name
            if function_version is not ShapeBase.NOT_SET:
                _params['function_version'] = function_version
            if description is not ShapeBase.NOT_SET:
                _params['description'] = description
            if routing_config is not ShapeBase.NOT_SET:
                _params['routing_config'] = routing_config
            if revision_id is not ShapeBase.NOT_SET:
                _params['revision_id'] = revision_id
            _request = shapes.UpdateAliasRequest(**_params)
        response = self._boto_client.update_alias(**_request.to_boto())

        return shapes.AliasConfiguration.from_boto(response)

    def update_event_source_mapping(
        self,
        _request: shapes.UpdateEventSourceMappingRequest = None,
        *,
        uuid: str,
        function_name: str = ShapeBase.NOT_SET,
        enabled: bool = ShapeBase.NOT_SET,
        batch_size: int = ShapeBase.NOT_SET,
    ) -> shapes.EventSourceMappingConfiguration:
        """
        You can update an event source mapping. This is useful if you want to change the
        parameters of the existing mapping without losing your position in the stream.
        You can change which function will receive the stream records, but to change the
        stream itself, you must create a new mapping.

        If you are using the versioning feature, you can update the event source mapping
        to map to a specific Lambda function version or alias as described in the
        `FunctionName` parameter. For information about the versioning feature, see [AWS
        Lambda Function Versioning and
        Aliases](http://docs.aws.amazon.com/lambda/latest/dg/versioning-aliases.html).

        If you disable the event source mapping, AWS Lambda stops polling. If you enable
        again, it will resume polling from the time it had stopped polling, so you don't
        lose processing of any records. However, if you delete event source mapping and
        create it again, it will reset.

        This operation requires permission for the `lambda:UpdateEventSourceMapping`
        action.
        """
        if _request is None:
            _params = {}
            if uuid is not ShapeBase.NOT_SET:
                _params['uuid'] = uuid
            if function_name is not ShapeBase.NOT_SET:
                _params['function_name'] = function_name
            if enabled is not ShapeBase.NOT_SET:
                _params['enabled'] = enabled
            if batch_size is not ShapeBase.NOT_SET:
                _params['batch_size'] = batch_size
            _request = shapes.UpdateEventSourceMappingRequest(**_params)
        response = self._boto_client.update_event_source_mapping(
            **_request.to_boto()
        )

        return shapes.EventSourceMappingConfiguration.from_boto(response)

    def update_function_code(
        self,
        _request: shapes.UpdateFunctionCodeRequest = None,
        *,
        function_name: str,
        zip_file: typing.Any = ShapeBase.NOT_SET,
        s3_bucket: str = ShapeBase.NOT_SET,
        s3_key: str = ShapeBase.NOT_SET,
        s3_object_version: str = ShapeBase.NOT_SET,
        publish: bool = ShapeBase.NOT_SET,
        dry_run: bool = ShapeBase.NOT_SET,
        revision_id: str = ShapeBase.NOT_SET,
    ) -> shapes.FunctionConfiguration:
        """
        Updates the code for the specified Lambda function. This operation must only be
        used on an existing Lambda function and cannot be used to update the function
        configuration.

        If you are using the versioning feature, note this API will always update the
        $LATEST version of your Lambda function. For information about the versioning
        feature, see [AWS Lambda Function Versioning and
        Aliases](http://docs.aws.amazon.com/lambda/latest/dg/versioning-aliases.html).

        This operation requires permission for the `lambda:UpdateFunctionCode` action.
        """
        if _request is None:
            _params = {}
            if function_name is not ShapeBase.NOT_SET:
                _params['function_name'] = function_name
            if zip_file is not ShapeBase.NOT_SET:
                _params['zip_file'] = zip_file
            if s3_bucket is not ShapeBase.NOT_SET:
                _params['s3_bucket'] = s3_bucket
            if s3_key is not ShapeBase.NOT_SET:
                _params['s3_key'] = s3_key
            if s3_object_version is not ShapeBase.NOT_SET:
                _params['s3_object_version'] = s3_object_version
            if publish is not ShapeBase.NOT_SET:
                _params['publish'] = publish
            if dry_run is not ShapeBase.NOT_SET:
                _params['dry_run'] = dry_run
            if revision_id is not ShapeBase.NOT_SET:
                _params['revision_id'] = revision_id
            _request = shapes.UpdateFunctionCodeRequest(**_params)
        response = self._boto_client.update_function_code(**_request.to_boto())

        return shapes.FunctionConfiguration.from_boto(response)

    def update_function_configuration(
        self,
        _request: shapes.UpdateFunctionConfigurationRequest = None,
        *,
        function_name: str,
        role: str = ShapeBase.NOT_SET,
        handler: str = ShapeBase.NOT_SET,
        description: str = ShapeBase.NOT_SET,
        timeout: int = ShapeBase.NOT_SET,
        memory_size: int = ShapeBase.NOT_SET,
        vpc_config: shapes.VpcConfig = ShapeBase.NOT_SET,
        environment: shapes.Environment = ShapeBase.NOT_SET,
        runtime: typing.Union[str, shapes.Runtime] = ShapeBase.NOT_SET,
        dead_letter_config: shapes.DeadLetterConfig = ShapeBase.NOT_SET,
        kms_key_arn: str = ShapeBase.NOT_SET,
        tracing_config: shapes.TracingConfig = ShapeBase.NOT_SET,
        revision_id: str = ShapeBase.NOT_SET,
    ) -> shapes.FunctionConfiguration:
        """
        Updates the configuration parameters for the specified Lambda function by using
        the values provided in the request. You provide only the parameters you want to
        change. This operation must only be used on an existing Lambda function and
        cannot be used to update the function's code.

        If you are using the versioning feature, note this API will always update the
        $LATEST version of your Lambda function. For information about the versioning
        feature, see [AWS Lambda Function Versioning and
        Aliases](http://docs.aws.amazon.com/lambda/latest/dg/versioning-aliases.html).

        This operation requires permission for the `lambda:UpdateFunctionConfiguration`
        action.
        """
        if _request is None:
            _params = {}
            if function_name is not ShapeBase.NOT_SET:
                _params['function_name'] = function_name
            if role is not ShapeBase.NOT_SET:
                _params['role'] = role
            if handler is not ShapeBase.NOT_SET:
                _params['handler'] = handler
            if description is not ShapeBase.NOT_SET:
                _params['description'] = description
            if timeout is not ShapeBase.NOT_SET:
                _params['timeout'] = timeout
            if memory_size is not ShapeBase.NOT_SET:
                _params['memory_size'] = memory_size
            if vpc_config is not ShapeBase.NOT_SET:
                _params['vpc_config'] = vpc_config
            if environment is not ShapeBase.NOT_SET:
                _params['environment'] = environment
            if runtime is not ShapeBase.NOT_SET:
                _params['runtime'] = runtime
            if dead_letter_config is not ShapeBase.NOT_SET:
                _params['dead_letter_config'] = dead_letter_config
            if kms_key_arn is not ShapeBase.NOT_SET:
                _params['kms_key_arn'] = kms_key_arn
            if tracing_config is not ShapeBase.NOT_SET:
                _params['tracing_config'] = tracing_config
            if revision_id is not ShapeBase.NOT_SET:
                _params['revision_id'] = revision_id
            _request = shapes.UpdateFunctionConfigurationRequest(**_params)
        response = self._boto_client.update_function_configuration(
            **_request.to_boto()
        )

        return shapes.FunctionConfiguration.from_boto(response)
