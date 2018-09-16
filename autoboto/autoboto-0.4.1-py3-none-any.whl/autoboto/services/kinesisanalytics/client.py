import datetime
import typing
import boto3
from autoboto import ClientBase, ShapeBase, OutputShapeBase
from . import shapes


class Client(ClientBase):
    def __init__(self, *args, **kwargs):
        super().__init__("kinesisanalytics", *args, **kwargs)

    def add_application_cloud_watch_logging_option(
        self,
        _request: shapes.AddApplicationCloudWatchLoggingOptionRequest = None,
        *,
        application_name: str,
        current_application_version_id: int,
        cloud_watch_logging_option: shapes.CloudWatchLoggingOption,
    ) -> shapes.AddApplicationCloudWatchLoggingOptionResponse:
        """
        Adds a CloudWatch log stream to monitor application configuration errors. For
        more information about using CloudWatch log streams with Amazon Kinesis
        Analytics applications, see [Working with Amazon CloudWatch
        Logs](http://docs.aws.amazon.com/kinesisanalytics/latest/dev/cloudwatch-
        logs.html).
        """
        if _request is None:
            _params = {}
            if application_name is not ShapeBase.NOT_SET:
                _params['application_name'] = application_name
            if current_application_version_id is not ShapeBase.NOT_SET:
                _params['current_application_version_id'
                       ] = current_application_version_id
            if cloud_watch_logging_option is not ShapeBase.NOT_SET:
                _params['cloud_watch_logging_option'
                       ] = cloud_watch_logging_option
            _request = shapes.AddApplicationCloudWatchLoggingOptionRequest(
                **_params
            )
        response = self._boto_client.add_application_cloud_watch_logging_option(
            **_request.to_boto()
        )

        return shapes.AddApplicationCloudWatchLoggingOptionResponse.from_boto(
            response
        )

    def add_application_input(
        self,
        _request: shapes.AddApplicationInputRequest = None,
        *,
        application_name: str,
        current_application_version_id: int,
        input: shapes.Input,
    ) -> shapes.AddApplicationInputResponse:
        """
        Adds a streaming source to your Amazon Kinesis application. For conceptual
        information, see [Configuring Application
        Input](http://docs.aws.amazon.com/kinesisanalytics/latest/dev/how-it-works-
        input.html).

        You can add a streaming source either when you create an application or you can
        use this operation to add a streaming source after you create an application.
        For more information, see CreateApplication.

        Any configuration update, including adding a streaming source using this
        operation, results in a new version of the application. You can use the
        DescribeApplication operation to find the current application version.

        This operation requires permissions to perform the
        `kinesisanalytics:AddApplicationInput` action.
        """
        if _request is None:
            _params = {}
            if application_name is not ShapeBase.NOT_SET:
                _params['application_name'] = application_name
            if current_application_version_id is not ShapeBase.NOT_SET:
                _params['current_application_version_id'
                       ] = current_application_version_id
            if input is not ShapeBase.NOT_SET:
                _params['input'] = input
            _request = shapes.AddApplicationInputRequest(**_params)
        response = self._boto_client.add_application_input(**_request.to_boto())

        return shapes.AddApplicationInputResponse.from_boto(response)

    def add_application_input_processing_configuration(
        self,
        _request: shapes.
        AddApplicationInputProcessingConfigurationRequest = None,
        *,
        application_name: str,
        current_application_version_id: int,
        input_id: str,
        input_processing_configuration: shapes.InputProcessingConfiguration,
    ) -> shapes.AddApplicationInputProcessingConfigurationResponse:
        """
        Adds an InputProcessingConfiguration to an application. An input processor
        preprocesses records on the input stream before the application's SQL code
        executes. Currently, the only input processor available is [AWS
        Lambda](https://aws.amazon.com/documentation/lambda/).
        """
        if _request is None:
            _params = {}
            if application_name is not ShapeBase.NOT_SET:
                _params['application_name'] = application_name
            if current_application_version_id is not ShapeBase.NOT_SET:
                _params['current_application_version_id'
                       ] = current_application_version_id
            if input_id is not ShapeBase.NOT_SET:
                _params['input_id'] = input_id
            if input_processing_configuration is not ShapeBase.NOT_SET:
                _params['input_processing_configuration'
                       ] = input_processing_configuration
            _request = shapes.AddApplicationInputProcessingConfigurationRequest(
                **_params
            )
        response = self._boto_client.add_application_input_processing_configuration(
            **_request.to_boto()
        )

        return shapes.AddApplicationInputProcessingConfigurationResponse.from_boto(
            response
        )

    def add_application_output(
        self,
        _request: shapes.AddApplicationOutputRequest = None,
        *,
        application_name: str,
        current_application_version_id: int,
        output: shapes.Output,
    ) -> shapes.AddApplicationOutputResponse:
        """
        Adds an external destination to your Amazon Kinesis Analytics application.

        If you want Amazon Kinesis Analytics to deliver data from an in-application
        stream within your application to an external destination (such as an Amazon
        Kinesis stream, an Amazon Kinesis Firehose delivery stream, or an Amazon Lambda
        function), you add the relevant configuration to your application using this
        operation. You can configure one or more outputs for your application. Each
        output configuration maps an in-application stream and an external destination.

        You can use one of the output configurations to deliver data from your in-
        application error stream to an external destination so that you can analyze the
        errors. For conceptual information, see [Understanding Application Output
        (Destination)](http://docs.aws.amazon.com/kinesisanalytics/latest/dev/how-it-
        works-output.html).

        Note that any configuration update, including adding a streaming source using
        this operation, results in a new version of the application. You can use the
        DescribeApplication operation to find the current application version.

        For the limits on the number of application inputs and outputs you can
        configure, see
        [Limits](http://docs.aws.amazon.com/kinesisanalytics/latest/dev/limits.html).

        This operation requires permissions to perform the
        `kinesisanalytics:AddApplicationOutput` action.
        """
        if _request is None:
            _params = {}
            if application_name is not ShapeBase.NOT_SET:
                _params['application_name'] = application_name
            if current_application_version_id is not ShapeBase.NOT_SET:
                _params['current_application_version_id'
                       ] = current_application_version_id
            if output is not ShapeBase.NOT_SET:
                _params['output'] = output
            _request = shapes.AddApplicationOutputRequest(**_params)
        response = self._boto_client.add_application_output(
            **_request.to_boto()
        )

        return shapes.AddApplicationOutputResponse.from_boto(response)

    def add_application_reference_data_source(
        self,
        _request: shapes.AddApplicationReferenceDataSourceRequest = None,
        *,
        application_name: str,
        current_application_version_id: int,
        reference_data_source: shapes.ReferenceDataSource,
    ) -> shapes.AddApplicationReferenceDataSourceResponse:
        """
        Adds a reference data source to an existing application.

        Amazon Kinesis Analytics reads reference data (that is, an Amazon S3 object) and
        creates an in-application table within your application. In the request, you
        provide the source (S3 bucket name and object key name), name of the in-
        application table to create, and the necessary mapping information that
        describes how data in Amazon S3 object maps to columns in the resulting in-
        application table.

        For conceptual information, see [Configuring Application
        Input](http://docs.aws.amazon.com/kinesisanalytics/latest/dev/how-it-works-
        input.html). For the limits on data sources you can add to your application, see
        [Limits](http://docs.aws.amazon.com/kinesisanalytics/latest/dev/limits.html).

        This operation requires permissions to perform the
        `kinesisanalytics:AddApplicationOutput` action.
        """
        if _request is None:
            _params = {}
            if application_name is not ShapeBase.NOT_SET:
                _params['application_name'] = application_name
            if current_application_version_id is not ShapeBase.NOT_SET:
                _params['current_application_version_id'
                       ] = current_application_version_id
            if reference_data_source is not ShapeBase.NOT_SET:
                _params['reference_data_source'] = reference_data_source
            _request = shapes.AddApplicationReferenceDataSourceRequest(
                **_params
            )
        response = self._boto_client.add_application_reference_data_source(
            **_request.to_boto()
        )

        return shapes.AddApplicationReferenceDataSourceResponse.from_boto(
            response
        )

    def create_application(
        self,
        _request: shapes.CreateApplicationRequest = None,
        *,
        application_name: str,
        application_description: str = ShapeBase.NOT_SET,
        inputs: typing.List[shapes.Input] = ShapeBase.NOT_SET,
        outputs: typing.List[shapes.Output] = ShapeBase.NOT_SET,
        cloud_watch_logging_options: typing.List[shapes.CloudWatchLoggingOption
                                                ] = ShapeBase.NOT_SET,
        application_code: str = ShapeBase.NOT_SET,
    ) -> shapes.CreateApplicationResponse:
        """
        Creates an Amazon Kinesis Analytics application. You can configure each
        application with one streaming source as input, application code to process the
        input, and up to three destinations where you want Amazon Kinesis Analytics to
        write the output data from your application. For an overview, see [How it
        Works](http://docs.aws.amazon.com/kinesisanalytics/latest/dev/how-it-
        works.html).

        In the input configuration, you map the streaming source to an in-application
        stream, which you can think of as a constantly updating table. In the mapping,
        you must provide a schema for the in-application stream and map each data column
        in the in-application stream to a data element in the streaming source.

        Your application code is one or more SQL statements that read input data,
        transform it, and generate output. Your application code can create one or more
        SQL artifacts like SQL streams or pumps.

        In the output configuration, you can configure the application to write data
        from in-application streams created in your applications to up to three
        destinations.

        To read data from your source stream or write data to destination streams,
        Amazon Kinesis Analytics needs your permissions. You grant these permissions by
        creating IAM roles. This operation requires permissions to perform the
        `kinesisanalytics:CreateApplication` action.

        For introductory exercises to create an Amazon Kinesis Analytics application,
        see [Getting
        Started](http://docs.aws.amazon.com/kinesisanalytics/latest/dev/getting-
        started.html).
        """
        if _request is None:
            _params = {}
            if application_name is not ShapeBase.NOT_SET:
                _params['application_name'] = application_name
            if application_description is not ShapeBase.NOT_SET:
                _params['application_description'] = application_description
            if inputs is not ShapeBase.NOT_SET:
                _params['inputs'] = inputs
            if outputs is not ShapeBase.NOT_SET:
                _params['outputs'] = outputs
            if cloud_watch_logging_options is not ShapeBase.NOT_SET:
                _params['cloud_watch_logging_options'
                       ] = cloud_watch_logging_options
            if application_code is not ShapeBase.NOT_SET:
                _params['application_code'] = application_code
            _request = shapes.CreateApplicationRequest(**_params)
        response = self._boto_client.create_application(**_request.to_boto())

        return shapes.CreateApplicationResponse.from_boto(response)

    def delete_application(
        self,
        _request: shapes.DeleteApplicationRequest = None,
        *,
        application_name: str,
        create_timestamp: datetime.datetime,
    ) -> shapes.DeleteApplicationResponse:
        """
        Deletes the specified application. Amazon Kinesis Analytics halts application
        execution and deletes the application, including any application artifacts (such
        as in-application streams, reference table, and application code).

        This operation requires permissions to perform the
        `kinesisanalytics:DeleteApplication` action.
        """
        if _request is None:
            _params = {}
            if application_name is not ShapeBase.NOT_SET:
                _params['application_name'] = application_name
            if create_timestamp is not ShapeBase.NOT_SET:
                _params['create_timestamp'] = create_timestamp
            _request = shapes.DeleteApplicationRequest(**_params)
        response = self._boto_client.delete_application(**_request.to_boto())

        return shapes.DeleteApplicationResponse.from_boto(response)

    def delete_application_cloud_watch_logging_option(
        self,
        _request: shapes.DeleteApplicationCloudWatchLoggingOptionRequest = None,
        *,
        application_name: str,
        current_application_version_id: int,
        cloud_watch_logging_option_id: str,
    ) -> shapes.DeleteApplicationCloudWatchLoggingOptionResponse:
        """
        Deletes a CloudWatch log stream from an application. For more information about
        using CloudWatch log streams with Amazon Kinesis Analytics applications, see
        [Working with Amazon CloudWatch
        Logs](http://docs.aws.amazon.com/kinesisanalytics/latest/dev/cloudwatch-
        logs.html).
        """
        if _request is None:
            _params = {}
            if application_name is not ShapeBase.NOT_SET:
                _params['application_name'] = application_name
            if current_application_version_id is not ShapeBase.NOT_SET:
                _params['current_application_version_id'
                       ] = current_application_version_id
            if cloud_watch_logging_option_id is not ShapeBase.NOT_SET:
                _params['cloud_watch_logging_option_id'
                       ] = cloud_watch_logging_option_id
            _request = shapes.DeleteApplicationCloudWatchLoggingOptionRequest(
                **_params
            )
        response = self._boto_client.delete_application_cloud_watch_logging_option(
            **_request.to_boto()
        )

        return shapes.DeleteApplicationCloudWatchLoggingOptionResponse.from_boto(
            response
        )

    def delete_application_input_processing_configuration(
        self,
        _request: shapes.
        DeleteApplicationInputProcessingConfigurationRequest = None,
        *,
        application_name: str,
        current_application_version_id: int,
        input_id: str,
    ) -> shapes.DeleteApplicationInputProcessingConfigurationResponse:
        """
        Deletes an InputProcessingConfiguration from an input.
        """
        if _request is None:
            _params = {}
            if application_name is not ShapeBase.NOT_SET:
                _params['application_name'] = application_name
            if current_application_version_id is not ShapeBase.NOT_SET:
                _params['current_application_version_id'
                       ] = current_application_version_id
            if input_id is not ShapeBase.NOT_SET:
                _params['input_id'] = input_id
            _request = shapes.DeleteApplicationInputProcessingConfigurationRequest(
                **_params
            )
        response = self._boto_client.delete_application_input_processing_configuration(
            **_request.to_boto()
        )

        return shapes.DeleteApplicationInputProcessingConfigurationResponse.from_boto(
            response
        )

    def delete_application_output(
        self,
        _request: shapes.DeleteApplicationOutputRequest = None,
        *,
        application_name: str,
        current_application_version_id: int,
        output_id: str,
    ) -> shapes.DeleteApplicationOutputResponse:
        """
        Deletes output destination configuration from your application configuration.
        Amazon Kinesis Analytics will no longer write data from the corresponding in-
        application stream to the external output destination.

        This operation requires permissions to perform the
        `kinesisanalytics:DeleteApplicationOutput` action.
        """
        if _request is None:
            _params = {}
            if application_name is not ShapeBase.NOT_SET:
                _params['application_name'] = application_name
            if current_application_version_id is not ShapeBase.NOT_SET:
                _params['current_application_version_id'
                       ] = current_application_version_id
            if output_id is not ShapeBase.NOT_SET:
                _params['output_id'] = output_id
            _request = shapes.DeleteApplicationOutputRequest(**_params)
        response = self._boto_client.delete_application_output(
            **_request.to_boto()
        )

        return shapes.DeleteApplicationOutputResponse.from_boto(response)

    def delete_application_reference_data_source(
        self,
        _request: shapes.DeleteApplicationReferenceDataSourceRequest = None,
        *,
        application_name: str,
        current_application_version_id: int,
        reference_id: str,
    ) -> shapes.DeleteApplicationReferenceDataSourceResponse:
        """
        Deletes a reference data source configuration from the specified application
        configuration.

        If the application is running, Amazon Kinesis Analytics immediately removes the
        in-application table that you created using the
        AddApplicationReferenceDataSource operation.

        This operation requires permissions to perform the
        `kinesisanalytics.DeleteApplicationReferenceDataSource` action.
        """
        if _request is None:
            _params = {}
            if application_name is not ShapeBase.NOT_SET:
                _params['application_name'] = application_name
            if current_application_version_id is not ShapeBase.NOT_SET:
                _params['current_application_version_id'
                       ] = current_application_version_id
            if reference_id is not ShapeBase.NOT_SET:
                _params['reference_id'] = reference_id
            _request = shapes.DeleteApplicationReferenceDataSourceRequest(
                **_params
            )
        response = self._boto_client.delete_application_reference_data_source(
            **_request.to_boto()
        )

        return shapes.DeleteApplicationReferenceDataSourceResponse.from_boto(
            response
        )

    def describe_application(
        self,
        _request: shapes.DescribeApplicationRequest = None,
        *,
        application_name: str,
    ) -> shapes.DescribeApplicationResponse:
        """
        Returns information about a specific Amazon Kinesis Analytics application.

        If you want to retrieve a list of all applications in your account, use the
        ListApplications operation.

        This operation requires permissions to perform the
        `kinesisanalytics:DescribeApplication` action. You can use `DescribeApplication`
        to get the current application versionId, which you need to call other
        operations such as `Update`.
        """
        if _request is None:
            _params = {}
            if application_name is not ShapeBase.NOT_SET:
                _params['application_name'] = application_name
            _request = shapes.DescribeApplicationRequest(**_params)
        response = self._boto_client.describe_application(**_request.to_boto())

        return shapes.DescribeApplicationResponse.from_boto(response)

    def discover_input_schema(
        self,
        _request: shapes.DiscoverInputSchemaRequest = None,
        *,
        resource_arn: str = ShapeBase.NOT_SET,
        role_arn: str = ShapeBase.NOT_SET,
        input_starting_position_configuration: shapes.
        InputStartingPositionConfiguration = ShapeBase.NOT_SET,
        s3_configuration: shapes.S3Configuration = ShapeBase.NOT_SET,
        input_processing_configuration: shapes.
        InputProcessingConfiguration = ShapeBase.NOT_SET,
    ) -> shapes.DiscoverInputSchemaResponse:
        """
        Infers a schema by evaluating sample records on the specified streaming source
        (Amazon Kinesis stream or Amazon Kinesis Firehose delivery stream) or S3 object.
        In the response, the operation returns the inferred schema and also the sample
        records that the operation used to infer the schema.

        You can use the inferred schema when configuring a streaming source for your
        application. For conceptual information, see [Configuring Application
        Input](http://docs.aws.amazon.com/kinesisanalytics/latest/dev/how-it-works-
        input.html). Note that when you create an application using the Amazon Kinesis
        Analytics console, the console uses this operation to infer a schema and show it
        in the console user interface.

        This operation requires permissions to perform the
        `kinesisanalytics:DiscoverInputSchema` action.
        """
        if _request is None:
            _params = {}
            if resource_arn is not ShapeBase.NOT_SET:
                _params['resource_arn'] = resource_arn
            if role_arn is not ShapeBase.NOT_SET:
                _params['role_arn'] = role_arn
            if input_starting_position_configuration is not ShapeBase.NOT_SET:
                _params['input_starting_position_configuration'
                       ] = input_starting_position_configuration
            if s3_configuration is not ShapeBase.NOT_SET:
                _params['s3_configuration'] = s3_configuration
            if input_processing_configuration is not ShapeBase.NOT_SET:
                _params['input_processing_configuration'
                       ] = input_processing_configuration
            _request = shapes.DiscoverInputSchemaRequest(**_params)
        response = self._boto_client.discover_input_schema(**_request.to_boto())

        return shapes.DiscoverInputSchemaResponse.from_boto(response)

    def list_applications(
        self,
        _request: shapes.ListApplicationsRequest = None,
        *,
        limit: int = ShapeBase.NOT_SET,
        exclusive_start_application_name: str = ShapeBase.NOT_SET,
    ) -> shapes.ListApplicationsResponse:
        """
        Returns a list of Amazon Kinesis Analytics applications in your account. For
        each application, the response includes the application name, Amazon Resource
        Name (ARN), and status. If the response returns the `HasMoreApplications` value
        as true, you can send another request by adding the
        `ExclusiveStartApplicationName` in the request body, and set the value of this
        to the last application name from the previous response.

        If you want detailed information about a specific application, use
        DescribeApplication.

        This operation requires permissions to perform the
        `kinesisanalytics:ListApplications` action.
        """
        if _request is None:
            _params = {}
            if limit is not ShapeBase.NOT_SET:
                _params['limit'] = limit
            if exclusive_start_application_name is not ShapeBase.NOT_SET:
                _params['exclusive_start_application_name'
                       ] = exclusive_start_application_name
            _request = shapes.ListApplicationsRequest(**_params)
        response = self._boto_client.list_applications(**_request.to_boto())

        return shapes.ListApplicationsResponse.from_boto(response)

    def start_application(
        self,
        _request: shapes.StartApplicationRequest = None,
        *,
        application_name: str,
        input_configurations: typing.List[shapes.InputConfiguration],
    ) -> shapes.StartApplicationResponse:
        """
        Starts the specified Amazon Kinesis Analytics application. After creating an
        application, you must exclusively call this operation to start your application.

        After the application starts, it begins consuming the input data, processes it,
        and writes the output to the configured destination.

        The application status must be `READY` for you to start an application. You can
        get the application status in the console or using the DescribeApplication
        operation.

        After you start the application, you can stop the application from processing
        the input by calling the StopApplication operation.

        This operation requires permissions to perform the
        `kinesisanalytics:StartApplication` action.
        """
        if _request is None:
            _params = {}
            if application_name is not ShapeBase.NOT_SET:
                _params['application_name'] = application_name
            if input_configurations is not ShapeBase.NOT_SET:
                _params['input_configurations'] = input_configurations
            _request = shapes.StartApplicationRequest(**_params)
        response = self._boto_client.start_application(**_request.to_boto())

        return shapes.StartApplicationResponse.from_boto(response)

    def stop_application(
        self,
        _request: shapes.StopApplicationRequest = None,
        *,
        application_name: str,
    ) -> shapes.StopApplicationResponse:
        """
        Stops the application from processing input data. You can stop an application
        only if it is in the running state. You can use the DescribeApplication
        operation to find the application state. After the application is stopped,
        Amazon Kinesis Analytics stops reading data from the input, the application
        stops processing data, and there is no output written to the destination.

        This operation requires permissions to perform the
        `kinesisanalytics:StopApplication` action.
        """
        if _request is None:
            _params = {}
            if application_name is not ShapeBase.NOT_SET:
                _params['application_name'] = application_name
            _request = shapes.StopApplicationRequest(**_params)
        response = self._boto_client.stop_application(**_request.to_boto())

        return shapes.StopApplicationResponse.from_boto(response)

    def update_application(
        self,
        _request: shapes.UpdateApplicationRequest = None,
        *,
        application_name: str,
        current_application_version_id: int,
        application_update: shapes.ApplicationUpdate,
    ) -> shapes.UpdateApplicationResponse:
        """
        Updates an existing Amazon Kinesis Analytics application. Using this API, you
        can update application code, input configuration, and output configuration.

        Note that Amazon Kinesis Analytics updates the `CurrentApplicationVersionId`
        each time you update your application.

        This operation requires permission for the `kinesisanalytics:UpdateApplication`
        action.
        """
        if _request is None:
            _params = {}
            if application_name is not ShapeBase.NOT_SET:
                _params['application_name'] = application_name
            if current_application_version_id is not ShapeBase.NOT_SET:
                _params['current_application_version_id'
                       ] = current_application_version_id
            if application_update is not ShapeBase.NOT_SET:
                _params['application_update'] = application_update
            _request = shapes.UpdateApplicationRequest(**_params)
        response = self._boto_client.update_application(**_request.to_boto())

        return shapes.UpdateApplicationResponse.from_boto(response)
