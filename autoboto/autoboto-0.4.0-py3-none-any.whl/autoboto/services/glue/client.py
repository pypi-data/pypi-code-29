import datetime
import typing
import boto3
from autoboto import ClientBase, ShapeBase, OutputShapeBase
from . import shapes


class Client(ClientBase):
    def __init__(self, *args, **kwargs):
        super().__init__("glue", *args, **kwargs)

    def batch_create_partition(
        self,
        _request: shapes.BatchCreatePartitionRequest = None,
        *,
        database_name: str,
        table_name: str,
        partition_input_list: typing.List[shapes.PartitionInput],
        catalog_id: str = ShapeBase.NOT_SET,
    ) -> shapes.BatchCreatePartitionResponse:
        """
        Creates one or more partitions in a batch operation.
        """
        if _request is None:
            _params = {}
            if database_name is not ShapeBase.NOT_SET:
                _params['database_name'] = database_name
            if table_name is not ShapeBase.NOT_SET:
                _params['table_name'] = table_name
            if partition_input_list is not ShapeBase.NOT_SET:
                _params['partition_input_list'] = partition_input_list
            if catalog_id is not ShapeBase.NOT_SET:
                _params['catalog_id'] = catalog_id
            _request = shapes.BatchCreatePartitionRequest(**_params)
        response = self._boto_client.batch_create_partition(
            **_request.to_boto()
        )

        return shapes.BatchCreatePartitionResponse.from_boto(response)

    def batch_delete_connection(
        self,
        _request: shapes.BatchDeleteConnectionRequest = None,
        *,
        connection_name_list: typing.List[str],
        catalog_id: str = ShapeBase.NOT_SET,
    ) -> shapes.BatchDeleteConnectionResponse:
        """
        Deletes a list of connection definitions from the Data Catalog.
        """
        if _request is None:
            _params = {}
            if connection_name_list is not ShapeBase.NOT_SET:
                _params['connection_name_list'] = connection_name_list
            if catalog_id is not ShapeBase.NOT_SET:
                _params['catalog_id'] = catalog_id
            _request = shapes.BatchDeleteConnectionRequest(**_params)
        response = self._boto_client.batch_delete_connection(
            **_request.to_boto()
        )

        return shapes.BatchDeleteConnectionResponse.from_boto(response)

    def batch_delete_partition(
        self,
        _request: shapes.BatchDeletePartitionRequest = None,
        *,
        database_name: str,
        table_name: str,
        partitions_to_delete: typing.List[shapes.PartitionValueList],
        catalog_id: str = ShapeBase.NOT_SET,
    ) -> shapes.BatchDeletePartitionResponse:
        """
        Deletes one or more partitions in a batch operation.
        """
        if _request is None:
            _params = {}
            if database_name is not ShapeBase.NOT_SET:
                _params['database_name'] = database_name
            if table_name is not ShapeBase.NOT_SET:
                _params['table_name'] = table_name
            if partitions_to_delete is not ShapeBase.NOT_SET:
                _params['partitions_to_delete'] = partitions_to_delete
            if catalog_id is not ShapeBase.NOT_SET:
                _params['catalog_id'] = catalog_id
            _request = shapes.BatchDeletePartitionRequest(**_params)
        response = self._boto_client.batch_delete_partition(
            **_request.to_boto()
        )

        return shapes.BatchDeletePartitionResponse.from_boto(response)

    def batch_delete_table(
        self,
        _request: shapes.BatchDeleteTableRequest = None,
        *,
        database_name: str,
        tables_to_delete: typing.List[str],
        catalog_id: str = ShapeBase.NOT_SET,
    ) -> shapes.BatchDeleteTableResponse:
        """
        Deletes multiple tables at once.

        After completing this operation, you will no longer have access to the table
        versions and partitions that belong to the deleted table. AWS Glue deletes these
        "orphaned" resources asynchronously in a timely manner, at the discretion of the
        service.

        To ensure immediate deletion of all related resources, before calling
        `BatchDeleteTable`, use `DeleteTableVersion` or `BatchDeleteTableVersion`, and
        `DeletePartition` or `BatchDeletePartition`, to delete any resources that belong
        to the table.
        """
        if _request is None:
            _params = {}
            if database_name is not ShapeBase.NOT_SET:
                _params['database_name'] = database_name
            if tables_to_delete is not ShapeBase.NOT_SET:
                _params['tables_to_delete'] = tables_to_delete
            if catalog_id is not ShapeBase.NOT_SET:
                _params['catalog_id'] = catalog_id
            _request = shapes.BatchDeleteTableRequest(**_params)
        response = self._boto_client.batch_delete_table(**_request.to_boto())

        return shapes.BatchDeleteTableResponse.from_boto(response)

    def batch_delete_table_version(
        self,
        _request: shapes.BatchDeleteTableVersionRequest = None,
        *,
        database_name: str,
        table_name: str,
        version_ids: typing.List[str],
        catalog_id: str = ShapeBase.NOT_SET,
    ) -> shapes.BatchDeleteTableVersionResponse:
        """
        Deletes a specified batch of versions of a table.
        """
        if _request is None:
            _params = {}
            if database_name is not ShapeBase.NOT_SET:
                _params['database_name'] = database_name
            if table_name is not ShapeBase.NOT_SET:
                _params['table_name'] = table_name
            if version_ids is not ShapeBase.NOT_SET:
                _params['version_ids'] = version_ids
            if catalog_id is not ShapeBase.NOT_SET:
                _params['catalog_id'] = catalog_id
            _request = shapes.BatchDeleteTableVersionRequest(**_params)
        response = self._boto_client.batch_delete_table_version(
            **_request.to_boto()
        )

        return shapes.BatchDeleteTableVersionResponse.from_boto(response)

    def batch_get_partition(
        self,
        _request: shapes.BatchGetPartitionRequest = None,
        *,
        database_name: str,
        table_name: str,
        partitions_to_get: typing.List[shapes.PartitionValueList],
        catalog_id: str = ShapeBase.NOT_SET,
    ) -> shapes.BatchGetPartitionResponse:
        """
        Retrieves partitions in a batch request.
        """
        if _request is None:
            _params = {}
            if database_name is not ShapeBase.NOT_SET:
                _params['database_name'] = database_name
            if table_name is not ShapeBase.NOT_SET:
                _params['table_name'] = table_name
            if partitions_to_get is not ShapeBase.NOT_SET:
                _params['partitions_to_get'] = partitions_to_get
            if catalog_id is not ShapeBase.NOT_SET:
                _params['catalog_id'] = catalog_id
            _request = shapes.BatchGetPartitionRequest(**_params)
        response = self._boto_client.batch_get_partition(**_request.to_boto())

        return shapes.BatchGetPartitionResponse.from_boto(response)

    def batch_stop_job_run(
        self,
        _request: shapes.BatchStopJobRunRequest = None,
        *,
        job_name: str,
        job_run_ids: typing.List[str],
    ) -> shapes.BatchStopJobRunResponse:
        """
        Stops one or more job runs for a specified job definition.
        """
        if _request is None:
            _params = {}
            if job_name is not ShapeBase.NOT_SET:
                _params['job_name'] = job_name
            if job_run_ids is not ShapeBase.NOT_SET:
                _params['job_run_ids'] = job_run_ids
            _request = shapes.BatchStopJobRunRequest(**_params)
        response = self._boto_client.batch_stop_job_run(**_request.to_boto())

        return shapes.BatchStopJobRunResponse.from_boto(response)

    def create_classifier(
        self,
        _request: shapes.CreateClassifierRequest = None,
        *,
        grok_classifier: shapes.CreateGrokClassifierRequest = ShapeBase.NOT_SET,
        xml_classifier: shapes.CreateXMLClassifierRequest = ShapeBase.NOT_SET,
        json_classifier: shapes.CreateJsonClassifierRequest = ShapeBase.NOT_SET,
    ) -> shapes.CreateClassifierResponse:
        """
        Creates a classifier in the user's account. This may be a `GrokClassifier`, an
        `XMLClassifier`, or abbrev `JsonClassifier`, depending on which field of the
        request is present.
        """
        if _request is None:
            _params = {}
            if grok_classifier is not ShapeBase.NOT_SET:
                _params['grok_classifier'] = grok_classifier
            if xml_classifier is not ShapeBase.NOT_SET:
                _params['xml_classifier'] = xml_classifier
            if json_classifier is not ShapeBase.NOT_SET:
                _params['json_classifier'] = json_classifier
            _request = shapes.CreateClassifierRequest(**_params)
        response = self._boto_client.create_classifier(**_request.to_boto())

        return shapes.CreateClassifierResponse.from_boto(response)

    def create_connection(
        self,
        _request: shapes.CreateConnectionRequest = None,
        *,
        connection_input: shapes.ConnectionInput,
        catalog_id: str = ShapeBase.NOT_SET,
    ) -> shapes.CreateConnectionResponse:
        """
        Creates a connection definition in the Data Catalog.
        """
        if _request is None:
            _params = {}
            if connection_input is not ShapeBase.NOT_SET:
                _params['connection_input'] = connection_input
            if catalog_id is not ShapeBase.NOT_SET:
                _params['catalog_id'] = catalog_id
            _request = shapes.CreateConnectionRequest(**_params)
        response = self._boto_client.create_connection(**_request.to_boto())

        return shapes.CreateConnectionResponse.from_boto(response)

    def create_crawler(
        self,
        _request: shapes.CreateCrawlerRequest = None,
        *,
        name: str,
        role: str,
        database_name: str,
        targets: shapes.CrawlerTargets,
        description: str = ShapeBase.NOT_SET,
        schedule: str = ShapeBase.NOT_SET,
        classifiers: typing.List[str] = ShapeBase.NOT_SET,
        table_prefix: str = ShapeBase.NOT_SET,
        schema_change_policy: shapes.SchemaChangePolicy = ShapeBase.NOT_SET,
        configuration: str = ShapeBase.NOT_SET,
        crawler_security_configuration: str = ShapeBase.NOT_SET,
    ) -> shapes.CreateCrawlerResponse:
        """
        Creates a new crawler with specified targets, role, configuration, and optional
        schedule. At least one crawl target must be specified, in the _s3Targets_ field,
        the _jdbcTargets_ field, or the _DynamoDBTargets_ field.
        """
        if _request is None:
            _params = {}
            if name is not ShapeBase.NOT_SET:
                _params['name'] = name
            if role is not ShapeBase.NOT_SET:
                _params['role'] = role
            if database_name is not ShapeBase.NOT_SET:
                _params['database_name'] = database_name
            if targets is not ShapeBase.NOT_SET:
                _params['targets'] = targets
            if description is not ShapeBase.NOT_SET:
                _params['description'] = description
            if schedule is not ShapeBase.NOT_SET:
                _params['schedule'] = schedule
            if classifiers is not ShapeBase.NOT_SET:
                _params['classifiers'] = classifiers
            if table_prefix is not ShapeBase.NOT_SET:
                _params['table_prefix'] = table_prefix
            if schema_change_policy is not ShapeBase.NOT_SET:
                _params['schema_change_policy'] = schema_change_policy
            if configuration is not ShapeBase.NOT_SET:
                _params['configuration'] = configuration
            if crawler_security_configuration is not ShapeBase.NOT_SET:
                _params['crawler_security_configuration'
                       ] = crawler_security_configuration
            _request = shapes.CreateCrawlerRequest(**_params)
        response = self._boto_client.create_crawler(**_request.to_boto())

        return shapes.CreateCrawlerResponse.from_boto(response)

    def create_database(
        self,
        _request: shapes.CreateDatabaseRequest = None,
        *,
        database_input: shapes.DatabaseInput,
        catalog_id: str = ShapeBase.NOT_SET,
    ) -> shapes.CreateDatabaseResponse:
        """
        Creates a new database in a Data Catalog.
        """
        if _request is None:
            _params = {}
            if database_input is not ShapeBase.NOT_SET:
                _params['database_input'] = database_input
            if catalog_id is not ShapeBase.NOT_SET:
                _params['catalog_id'] = catalog_id
            _request = shapes.CreateDatabaseRequest(**_params)
        response = self._boto_client.create_database(**_request.to_boto())

        return shapes.CreateDatabaseResponse.from_boto(response)

    def create_dev_endpoint(
        self,
        _request: shapes.CreateDevEndpointRequest = None,
        *,
        endpoint_name: str,
        role_arn: str,
        security_group_ids: typing.List[str] = ShapeBase.NOT_SET,
        subnet_id: str = ShapeBase.NOT_SET,
        public_key: str = ShapeBase.NOT_SET,
        public_keys: typing.List[str] = ShapeBase.NOT_SET,
        number_of_nodes: int = ShapeBase.NOT_SET,
        extra_python_libs_s3_path: str = ShapeBase.NOT_SET,
        extra_jars_s3_path: str = ShapeBase.NOT_SET,
        security_configuration: str = ShapeBase.NOT_SET,
    ) -> shapes.CreateDevEndpointResponse:
        """
        Creates a new DevEndpoint.
        """
        if _request is None:
            _params = {}
            if endpoint_name is not ShapeBase.NOT_SET:
                _params['endpoint_name'] = endpoint_name
            if role_arn is not ShapeBase.NOT_SET:
                _params['role_arn'] = role_arn
            if security_group_ids is not ShapeBase.NOT_SET:
                _params['security_group_ids'] = security_group_ids
            if subnet_id is not ShapeBase.NOT_SET:
                _params['subnet_id'] = subnet_id
            if public_key is not ShapeBase.NOT_SET:
                _params['public_key'] = public_key
            if public_keys is not ShapeBase.NOT_SET:
                _params['public_keys'] = public_keys
            if number_of_nodes is not ShapeBase.NOT_SET:
                _params['number_of_nodes'] = number_of_nodes
            if extra_python_libs_s3_path is not ShapeBase.NOT_SET:
                _params['extra_python_libs_s3_path'] = extra_python_libs_s3_path
            if extra_jars_s3_path is not ShapeBase.NOT_SET:
                _params['extra_jars_s3_path'] = extra_jars_s3_path
            if security_configuration is not ShapeBase.NOT_SET:
                _params['security_configuration'] = security_configuration
            _request = shapes.CreateDevEndpointRequest(**_params)
        response = self._boto_client.create_dev_endpoint(**_request.to_boto())

        return shapes.CreateDevEndpointResponse.from_boto(response)

    def create_job(
        self,
        _request: shapes.CreateJobRequest = None,
        *,
        name: str,
        role: str,
        command: shapes.JobCommand,
        description: str = ShapeBase.NOT_SET,
        log_uri: str = ShapeBase.NOT_SET,
        execution_property: shapes.ExecutionProperty = ShapeBase.NOT_SET,
        default_arguments: typing.Dict[str, str] = ShapeBase.NOT_SET,
        connections: shapes.ConnectionsList = ShapeBase.NOT_SET,
        max_retries: int = ShapeBase.NOT_SET,
        allocated_capacity: int = ShapeBase.NOT_SET,
        timeout: int = ShapeBase.NOT_SET,
        notification_property: shapes.NotificationProperty = ShapeBase.NOT_SET,
        security_configuration: str = ShapeBase.NOT_SET,
    ) -> shapes.CreateJobResponse:
        """
        Creates a new job definition.
        """
        if _request is None:
            _params = {}
            if name is not ShapeBase.NOT_SET:
                _params['name'] = name
            if role is not ShapeBase.NOT_SET:
                _params['role'] = role
            if command is not ShapeBase.NOT_SET:
                _params['command'] = command
            if description is not ShapeBase.NOT_SET:
                _params['description'] = description
            if log_uri is not ShapeBase.NOT_SET:
                _params['log_uri'] = log_uri
            if execution_property is not ShapeBase.NOT_SET:
                _params['execution_property'] = execution_property
            if default_arguments is not ShapeBase.NOT_SET:
                _params['default_arguments'] = default_arguments
            if connections is not ShapeBase.NOT_SET:
                _params['connections'] = connections
            if max_retries is not ShapeBase.NOT_SET:
                _params['max_retries'] = max_retries
            if allocated_capacity is not ShapeBase.NOT_SET:
                _params['allocated_capacity'] = allocated_capacity
            if timeout is not ShapeBase.NOT_SET:
                _params['timeout'] = timeout
            if notification_property is not ShapeBase.NOT_SET:
                _params['notification_property'] = notification_property
            if security_configuration is not ShapeBase.NOT_SET:
                _params['security_configuration'] = security_configuration
            _request = shapes.CreateJobRequest(**_params)
        response = self._boto_client.create_job(**_request.to_boto())

        return shapes.CreateJobResponse.from_boto(response)

    def create_partition(
        self,
        _request: shapes.CreatePartitionRequest = None,
        *,
        database_name: str,
        table_name: str,
        partition_input: shapes.PartitionInput,
        catalog_id: str = ShapeBase.NOT_SET,
    ) -> shapes.CreatePartitionResponse:
        """
        Creates a new partition.
        """
        if _request is None:
            _params = {}
            if database_name is not ShapeBase.NOT_SET:
                _params['database_name'] = database_name
            if table_name is not ShapeBase.NOT_SET:
                _params['table_name'] = table_name
            if partition_input is not ShapeBase.NOT_SET:
                _params['partition_input'] = partition_input
            if catalog_id is not ShapeBase.NOT_SET:
                _params['catalog_id'] = catalog_id
            _request = shapes.CreatePartitionRequest(**_params)
        response = self._boto_client.create_partition(**_request.to_boto())

        return shapes.CreatePartitionResponse.from_boto(response)

    def create_script(
        self,
        _request: shapes.CreateScriptRequest = None,
        *,
        dag_nodes: typing.List[shapes.CodeGenNode] = ShapeBase.NOT_SET,
        dag_edges: typing.List[shapes.CodeGenEdge] = ShapeBase.NOT_SET,
        language: typing.Union[str, shapes.Language] = ShapeBase.NOT_SET,
    ) -> shapes.CreateScriptResponse:
        """
        Transforms a directed acyclic graph (DAG) into code.
        """
        if _request is None:
            _params = {}
            if dag_nodes is not ShapeBase.NOT_SET:
                _params['dag_nodes'] = dag_nodes
            if dag_edges is not ShapeBase.NOT_SET:
                _params['dag_edges'] = dag_edges
            if language is not ShapeBase.NOT_SET:
                _params['language'] = language
            _request = shapes.CreateScriptRequest(**_params)
        response = self._boto_client.create_script(**_request.to_boto())

        return shapes.CreateScriptResponse.from_boto(response)

    def create_security_configuration(
        self,
        _request: shapes.CreateSecurityConfigurationRequest = None,
        *,
        name: str,
        encryption_configuration: shapes.EncryptionConfiguration,
    ) -> shapes.CreateSecurityConfigurationResponse:
        """
        Creates a new security configuration.
        """
        if _request is None:
            _params = {}
            if name is not ShapeBase.NOT_SET:
                _params['name'] = name
            if encryption_configuration is not ShapeBase.NOT_SET:
                _params['encryption_configuration'] = encryption_configuration
            _request = shapes.CreateSecurityConfigurationRequest(**_params)
        response = self._boto_client.create_security_configuration(
            **_request.to_boto()
        )

        return shapes.CreateSecurityConfigurationResponse.from_boto(response)

    def create_table(
        self,
        _request: shapes.CreateTableRequest = None,
        *,
        database_name: str,
        table_input: shapes.TableInput,
        catalog_id: str = ShapeBase.NOT_SET,
    ) -> shapes.CreateTableResponse:
        """
        Creates a new table definition in the Data Catalog.
        """
        if _request is None:
            _params = {}
            if database_name is not ShapeBase.NOT_SET:
                _params['database_name'] = database_name
            if table_input is not ShapeBase.NOT_SET:
                _params['table_input'] = table_input
            if catalog_id is not ShapeBase.NOT_SET:
                _params['catalog_id'] = catalog_id
            _request = shapes.CreateTableRequest(**_params)
        response = self._boto_client.create_table(**_request.to_boto())

        return shapes.CreateTableResponse.from_boto(response)

    def create_trigger(
        self,
        _request: shapes.CreateTriggerRequest = None,
        *,
        name: str,
        type: typing.Union[str, shapes.TriggerType],
        actions: typing.List[shapes.Action],
        schedule: str = ShapeBase.NOT_SET,
        predicate: shapes.Predicate = ShapeBase.NOT_SET,
        description: str = ShapeBase.NOT_SET,
        start_on_creation: bool = ShapeBase.NOT_SET,
    ) -> shapes.CreateTriggerResponse:
        """
        Creates a new trigger.
        """
        if _request is None:
            _params = {}
            if name is not ShapeBase.NOT_SET:
                _params['name'] = name
            if type is not ShapeBase.NOT_SET:
                _params['type'] = type
            if actions is not ShapeBase.NOT_SET:
                _params['actions'] = actions
            if schedule is not ShapeBase.NOT_SET:
                _params['schedule'] = schedule
            if predicate is not ShapeBase.NOT_SET:
                _params['predicate'] = predicate
            if description is not ShapeBase.NOT_SET:
                _params['description'] = description
            if start_on_creation is not ShapeBase.NOT_SET:
                _params['start_on_creation'] = start_on_creation
            _request = shapes.CreateTriggerRequest(**_params)
        response = self._boto_client.create_trigger(**_request.to_boto())

        return shapes.CreateTriggerResponse.from_boto(response)

    def create_user_defined_function(
        self,
        _request: shapes.CreateUserDefinedFunctionRequest = None,
        *,
        database_name: str,
        function_input: shapes.UserDefinedFunctionInput,
        catalog_id: str = ShapeBase.NOT_SET,
    ) -> shapes.CreateUserDefinedFunctionResponse:
        """
        Creates a new function definition in the Data Catalog.
        """
        if _request is None:
            _params = {}
            if database_name is not ShapeBase.NOT_SET:
                _params['database_name'] = database_name
            if function_input is not ShapeBase.NOT_SET:
                _params['function_input'] = function_input
            if catalog_id is not ShapeBase.NOT_SET:
                _params['catalog_id'] = catalog_id
            _request = shapes.CreateUserDefinedFunctionRequest(**_params)
        response = self._boto_client.create_user_defined_function(
            **_request.to_boto()
        )

        return shapes.CreateUserDefinedFunctionResponse.from_boto(response)

    def delete_classifier(
        self,
        _request: shapes.DeleteClassifierRequest = None,
        *,
        name: str,
    ) -> shapes.DeleteClassifierResponse:
        """
        Removes a classifier from the Data Catalog.
        """
        if _request is None:
            _params = {}
            if name is not ShapeBase.NOT_SET:
                _params['name'] = name
            _request = shapes.DeleteClassifierRequest(**_params)
        response = self._boto_client.delete_classifier(**_request.to_boto())

        return shapes.DeleteClassifierResponse.from_boto(response)

    def delete_connection(
        self,
        _request: shapes.DeleteConnectionRequest = None,
        *,
        connection_name: str,
        catalog_id: str = ShapeBase.NOT_SET,
    ) -> shapes.DeleteConnectionResponse:
        """
        Deletes a connection from the Data Catalog.
        """
        if _request is None:
            _params = {}
            if connection_name is not ShapeBase.NOT_SET:
                _params['connection_name'] = connection_name
            if catalog_id is not ShapeBase.NOT_SET:
                _params['catalog_id'] = catalog_id
            _request = shapes.DeleteConnectionRequest(**_params)
        response = self._boto_client.delete_connection(**_request.to_boto())

        return shapes.DeleteConnectionResponse.from_boto(response)

    def delete_crawler(
        self,
        _request: shapes.DeleteCrawlerRequest = None,
        *,
        name: str,
    ) -> shapes.DeleteCrawlerResponse:
        """
        Removes a specified crawler from the Data Catalog, unless the crawler state is
        `RUNNING`.
        """
        if _request is None:
            _params = {}
            if name is not ShapeBase.NOT_SET:
                _params['name'] = name
            _request = shapes.DeleteCrawlerRequest(**_params)
        response = self._boto_client.delete_crawler(**_request.to_boto())

        return shapes.DeleteCrawlerResponse.from_boto(response)

    def delete_database(
        self,
        _request: shapes.DeleteDatabaseRequest = None,
        *,
        name: str,
        catalog_id: str = ShapeBase.NOT_SET,
    ) -> shapes.DeleteDatabaseResponse:
        """
        Removes a specified Database from a Data Catalog.

        After completing this operation, you will no longer have access to the tables
        (and all table versions and partitions that might belong to the tables) and the
        user-defined functions in the deleted database. AWS Glue deletes these
        "orphaned" resources asynchronously in a timely manner, at the discretion of the
        service.

        To ensure immediate deletion of all related resources, before calling
        `DeleteDatabase`, use `DeleteTableVersion` or `BatchDeleteTableVersion`,
        `DeletePartition` or `BatchDeletePartition`, `DeleteUserDefinedFunction`, and
        `DeleteTable` or `BatchDeleteTable`, to delete any resources that belong to the
        database.
        """
        if _request is None:
            _params = {}
            if name is not ShapeBase.NOT_SET:
                _params['name'] = name
            if catalog_id is not ShapeBase.NOT_SET:
                _params['catalog_id'] = catalog_id
            _request = shapes.DeleteDatabaseRequest(**_params)
        response = self._boto_client.delete_database(**_request.to_boto())

        return shapes.DeleteDatabaseResponse.from_boto(response)

    def delete_dev_endpoint(
        self,
        _request: shapes.DeleteDevEndpointRequest = None,
        *,
        endpoint_name: str,
    ) -> shapes.DeleteDevEndpointResponse:
        """
        Deletes a specified DevEndpoint.
        """
        if _request is None:
            _params = {}
            if endpoint_name is not ShapeBase.NOT_SET:
                _params['endpoint_name'] = endpoint_name
            _request = shapes.DeleteDevEndpointRequest(**_params)
        response = self._boto_client.delete_dev_endpoint(**_request.to_boto())

        return shapes.DeleteDevEndpointResponse.from_boto(response)

    def delete_job(
        self,
        _request: shapes.DeleteJobRequest = None,
        *,
        job_name: str,
    ) -> shapes.DeleteJobResponse:
        """
        Deletes a specified job definition. If the job definition is not found, no
        exception is thrown.
        """
        if _request is None:
            _params = {}
            if job_name is not ShapeBase.NOT_SET:
                _params['job_name'] = job_name
            _request = shapes.DeleteJobRequest(**_params)
        response = self._boto_client.delete_job(**_request.to_boto())

        return shapes.DeleteJobResponse.from_boto(response)

    def delete_partition(
        self,
        _request: shapes.DeletePartitionRequest = None,
        *,
        database_name: str,
        table_name: str,
        partition_values: typing.List[str],
        catalog_id: str = ShapeBase.NOT_SET,
    ) -> shapes.DeletePartitionResponse:
        """
        Deletes a specified partition.
        """
        if _request is None:
            _params = {}
            if database_name is not ShapeBase.NOT_SET:
                _params['database_name'] = database_name
            if table_name is not ShapeBase.NOT_SET:
                _params['table_name'] = table_name
            if partition_values is not ShapeBase.NOT_SET:
                _params['partition_values'] = partition_values
            if catalog_id is not ShapeBase.NOT_SET:
                _params['catalog_id'] = catalog_id
            _request = shapes.DeletePartitionRequest(**_params)
        response = self._boto_client.delete_partition(**_request.to_boto())

        return shapes.DeletePartitionResponse.from_boto(response)

    def delete_security_configuration(
        self,
        _request: shapes.DeleteSecurityConfigurationRequest = None,
        *,
        name: str,
    ) -> shapes.DeleteSecurityConfigurationResponse:
        """
        Deletes a specified security configuration.
        """
        if _request is None:
            _params = {}
            if name is not ShapeBase.NOT_SET:
                _params['name'] = name
            _request = shapes.DeleteSecurityConfigurationRequest(**_params)
        response = self._boto_client.delete_security_configuration(
            **_request.to_boto()
        )

        return shapes.DeleteSecurityConfigurationResponse.from_boto(response)

    def delete_table(
        self,
        _request: shapes.DeleteTableRequest = None,
        *,
        database_name: str,
        name: str,
        catalog_id: str = ShapeBase.NOT_SET,
    ) -> shapes.DeleteTableResponse:
        """
        Removes a table definition from the Data Catalog.

        After completing this operation, you will no longer have access to the table
        versions and partitions that belong to the deleted table. AWS Glue deletes these
        "orphaned" resources asynchronously in a timely manner, at the discretion of the
        service.

        To ensure immediate deletion of all related resources, before calling
        `DeleteTable`, use `DeleteTableVersion` or `BatchDeleteTableVersion`, and
        `DeletePartition` or `BatchDeletePartition`, to delete any resources that belong
        to the table.
        """
        if _request is None:
            _params = {}
            if database_name is not ShapeBase.NOT_SET:
                _params['database_name'] = database_name
            if name is not ShapeBase.NOT_SET:
                _params['name'] = name
            if catalog_id is not ShapeBase.NOT_SET:
                _params['catalog_id'] = catalog_id
            _request = shapes.DeleteTableRequest(**_params)
        response = self._boto_client.delete_table(**_request.to_boto())

        return shapes.DeleteTableResponse.from_boto(response)

    def delete_table_version(
        self,
        _request: shapes.DeleteTableVersionRequest = None,
        *,
        database_name: str,
        table_name: str,
        version_id: str,
        catalog_id: str = ShapeBase.NOT_SET,
    ) -> shapes.DeleteTableVersionResponse:
        """
        Deletes a specified version of a table.
        """
        if _request is None:
            _params = {}
            if database_name is not ShapeBase.NOT_SET:
                _params['database_name'] = database_name
            if table_name is not ShapeBase.NOT_SET:
                _params['table_name'] = table_name
            if version_id is not ShapeBase.NOT_SET:
                _params['version_id'] = version_id
            if catalog_id is not ShapeBase.NOT_SET:
                _params['catalog_id'] = catalog_id
            _request = shapes.DeleteTableVersionRequest(**_params)
        response = self._boto_client.delete_table_version(**_request.to_boto())

        return shapes.DeleteTableVersionResponse.from_boto(response)

    def delete_trigger(
        self,
        _request: shapes.DeleteTriggerRequest = None,
        *,
        name: str,
    ) -> shapes.DeleteTriggerResponse:
        """
        Deletes a specified trigger. If the trigger is not found, no exception is
        thrown.
        """
        if _request is None:
            _params = {}
            if name is not ShapeBase.NOT_SET:
                _params['name'] = name
            _request = shapes.DeleteTriggerRequest(**_params)
        response = self._boto_client.delete_trigger(**_request.to_boto())

        return shapes.DeleteTriggerResponse.from_boto(response)

    def delete_user_defined_function(
        self,
        _request: shapes.DeleteUserDefinedFunctionRequest = None,
        *,
        database_name: str,
        function_name: str,
        catalog_id: str = ShapeBase.NOT_SET,
    ) -> shapes.DeleteUserDefinedFunctionResponse:
        """
        Deletes an existing function definition from the Data Catalog.
        """
        if _request is None:
            _params = {}
            if database_name is not ShapeBase.NOT_SET:
                _params['database_name'] = database_name
            if function_name is not ShapeBase.NOT_SET:
                _params['function_name'] = function_name
            if catalog_id is not ShapeBase.NOT_SET:
                _params['catalog_id'] = catalog_id
            _request = shapes.DeleteUserDefinedFunctionRequest(**_params)
        response = self._boto_client.delete_user_defined_function(
            **_request.to_boto()
        )

        return shapes.DeleteUserDefinedFunctionResponse.from_boto(response)

    def get_catalog_import_status(
        self,
        _request: shapes.GetCatalogImportStatusRequest = None,
        *,
        catalog_id: str = ShapeBase.NOT_SET,
    ) -> shapes.GetCatalogImportStatusResponse:
        """
        Retrieves the status of a migration operation.
        """
        if _request is None:
            _params = {}
            if catalog_id is not ShapeBase.NOT_SET:
                _params['catalog_id'] = catalog_id
            _request = shapes.GetCatalogImportStatusRequest(**_params)
        response = self._boto_client.get_catalog_import_status(
            **_request.to_boto()
        )

        return shapes.GetCatalogImportStatusResponse.from_boto(response)

    def get_classifier(
        self,
        _request: shapes.GetClassifierRequest = None,
        *,
        name: str,
    ) -> shapes.GetClassifierResponse:
        """
        Retrieve a classifier by name.
        """
        if _request is None:
            _params = {}
            if name is not ShapeBase.NOT_SET:
                _params['name'] = name
            _request = shapes.GetClassifierRequest(**_params)
        response = self._boto_client.get_classifier(**_request.to_boto())

        return shapes.GetClassifierResponse.from_boto(response)

    def get_classifiers(
        self,
        _request: shapes.GetClassifiersRequest = None,
        *,
        max_results: int = ShapeBase.NOT_SET,
        next_token: str = ShapeBase.NOT_SET,
    ) -> shapes.GetClassifiersResponse:
        """
        Lists all classifier objects in the Data Catalog.
        """
        if _request is None:
            _params = {}
            if max_results is not ShapeBase.NOT_SET:
                _params['max_results'] = max_results
            if next_token is not ShapeBase.NOT_SET:
                _params['next_token'] = next_token
            _request = shapes.GetClassifiersRequest(**_params)
        paginator = self.get_paginator("get_classifiers").paginate(
            **_request.to_boto()
        )
        page_generator = (page for page in paginator)
        first_page = next(page_generator)
        result = shapes.GetClassifiersResponse.from_boto(first_page)
        result._page_iterator = page_generator
        return result

        return shapes.GetClassifiersResponse.from_boto(response)

    def get_connection(
        self,
        _request: shapes.GetConnectionRequest = None,
        *,
        name: str,
        catalog_id: str = ShapeBase.NOT_SET,
    ) -> shapes.GetConnectionResponse:
        """
        Retrieves a connection definition from the Data Catalog.
        """
        if _request is None:
            _params = {}
            if name is not ShapeBase.NOT_SET:
                _params['name'] = name
            if catalog_id is not ShapeBase.NOT_SET:
                _params['catalog_id'] = catalog_id
            _request = shapes.GetConnectionRequest(**_params)
        response = self._boto_client.get_connection(**_request.to_boto())

        return shapes.GetConnectionResponse.from_boto(response)

    def get_connections(
        self,
        _request: shapes.GetConnectionsRequest = None,
        *,
        catalog_id: str = ShapeBase.NOT_SET,
        filter: shapes.GetConnectionsFilter = ShapeBase.NOT_SET,
        next_token: str = ShapeBase.NOT_SET,
        max_results: int = ShapeBase.NOT_SET,
    ) -> shapes.GetConnectionsResponse:
        """
        Retrieves a list of connection definitions from the Data Catalog.
        """
        if _request is None:
            _params = {}
            if catalog_id is not ShapeBase.NOT_SET:
                _params['catalog_id'] = catalog_id
            if filter is not ShapeBase.NOT_SET:
                _params['filter'] = filter
            if next_token is not ShapeBase.NOT_SET:
                _params['next_token'] = next_token
            if max_results is not ShapeBase.NOT_SET:
                _params['max_results'] = max_results
            _request = shapes.GetConnectionsRequest(**_params)
        paginator = self.get_paginator("get_connections").paginate(
            **_request.to_boto()
        )
        page_generator = (page for page in paginator)
        first_page = next(page_generator)
        result = shapes.GetConnectionsResponse.from_boto(first_page)
        result._page_iterator = page_generator
        return result

        return shapes.GetConnectionsResponse.from_boto(response)

    def get_crawler(
        self,
        _request: shapes.GetCrawlerRequest = None,
        *,
        name: str,
    ) -> shapes.GetCrawlerResponse:
        """
        Retrieves metadata for a specified crawler.
        """
        if _request is None:
            _params = {}
            if name is not ShapeBase.NOT_SET:
                _params['name'] = name
            _request = shapes.GetCrawlerRequest(**_params)
        response = self._boto_client.get_crawler(**_request.to_boto())

        return shapes.GetCrawlerResponse.from_boto(response)

    def get_crawler_metrics(
        self,
        _request: shapes.GetCrawlerMetricsRequest = None,
        *,
        crawler_name_list: typing.List[str] = ShapeBase.NOT_SET,
        max_results: int = ShapeBase.NOT_SET,
        next_token: str = ShapeBase.NOT_SET,
    ) -> shapes.GetCrawlerMetricsResponse:
        """
        Retrieves metrics about specified crawlers.
        """
        if _request is None:
            _params = {}
            if crawler_name_list is not ShapeBase.NOT_SET:
                _params['crawler_name_list'] = crawler_name_list
            if max_results is not ShapeBase.NOT_SET:
                _params['max_results'] = max_results
            if next_token is not ShapeBase.NOT_SET:
                _params['next_token'] = next_token
            _request = shapes.GetCrawlerMetricsRequest(**_params)
        paginator = self.get_paginator("get_crawler_metrics").paginate(
            **_request.to_boto()
        )
        page_generator = (page for page in paginator)
        first_page = next(page_generator)
        result = shapes.GetCrawlerMetricsResponse.from_boto(first_page)
        result._page_iterator = page_generator
        return result

        return shapes.GetCrawlerMetricsResponse.from_boto(response)

    def get_crawlers(
        self,
        _request: shapes.GetCrawlersRequest = None,
        *,
        max_results: int = ShapeBase.NOT_SET,
        next_token: str = ShapeBase.NOT_SET,
    ) -> shapes.GetCrawlersResponse:
        """
        Retrieves metadata for all crawlers defined in the customer account.
        """
        if _request is None:
            _params = {}
            if max_results is not ShapeBase.NOT_SET:
                _params['max_results'] = max_results
            if next_token is not ShapeBase.NOT_SET:
                _params['next_token'] = next_token
            _request = shapes.GetCrawlersRequest(**_params)
        paginator = self.get_paginator("get_crawlers").paginate(
            **_request.to_boto()
        )
        page_generator = (page for page in paginator)
        first_page = next(page_generator)
        result = shapes.GetCrawlersResponse.from_boto(first_page)
        result._page_iterator = page_generator
        return result

        return shapes.GetCrawlersResponse.from_boto(response)

    def get_database(
        self,
        _request: shapes.GetDatabaseRequest = None,
        *,
        name: str,
        catalog_id: str = ShapeBase.NOT_SET,
    ) -> shapes.GetDatabaseResponse:
        """
        Retrieves the definition of a specified database.
        """
        if _request is None:
            _params = {}
            if name is not ShapeBase.NOT_SET:
                _params['name'] = name
            if catalog_id is not ShapeBase.NOT_SET:
                _params['catalog_id'] = catalog_id
            _request = shapes.GetDatabaseRequest(**_params)
        response = self._boto_client.get_database(**_request.to_boto())

        return shapes.GetDatabaseResponse.from_boto(response)

    def get_databases(
        self,
        _request: shapes.GetDatabasesRequest = None,
        *,
        catalog_id: str = ShapeBase.NOT_SET,
        next_token: str = ShapeBase.NOT_SET,
        max_results: int = ShapeBase.NOT_SET,
    ) -> shapes.GetDatabasesResponse:
        """
        Retrieves all Databases defined in a given Data Catalog.
        """
        if _request is None:
            _params = {}
            if catalog_id is not ShapeBase.NOT_SET:
                _params['catalog_id'] = catalog_id
            if next_token is not ShapeBase.NOT_SET:
                _params['next_token'] = next_token
            if max_results is not ShapeBase.NOT_SET:
                _params['max_results'] = max_results
            _request = shapes.GetDatabasesRequest(**_params)
        paginator = self.get_paginator("get_databases").paginate(
            **_request.to_boto()
        )
        page_generator = (page for page in paginator)
        first_page = next(page_generator)
        result = shapes.GetDatabasesResponse.from_boto(first_page)
        result._page_iterator = page_generator
        return result

        return shapes.GetDatabasesResponse.from_boto(response)

    def get_dataflow_graph(
        self,
        _request: shapes.GetDataflowGraphRequest = None,
        *,
        python_script: str = ShapeBase.NOT_SET,
    ) -> shapes.GetDataflowGraphResponse:
        """
        Transforms a Python script into a directed acyclic graph (DAG).
        """
        if _request is None:
            _params = {}
            if python_script is not ShapeBase.NOT_SET:
                _params['python_script'] = python_script
            _request = shapes.GetDataflowGraphRequest(**_params)
        response = self._boto_client.get_dataflow_graph(**_request.to_boto())

        return shapes.GetDataflowGraphResponse.from_boto(response)

    def get_dev_endpoint(
        self,
        _request: shapes.GetDevEndpointRequest = None,
        *,
        endpoint_name: str,
    ) -> shapes.GetDevEndpointResponse:
        """
        Retrieves information about a specified DevEndpoint.
        """
        if _request is None:
            _params = {}
            if endpoint_name is not ShapeBase.NOT_SET:
                _params['endpoint_name'] = endpoint_name
            _request = shapes.GetDevEndpointRequest(**_params)
        response = self._boto_client.get_dev_endpoint(**_request.to_boto())

        return shapes.GetDevEndpointResponse.from_boto(response)

    def get_dev_endpoints(
        self,
        _request: shapes.GetDevEndpointsRequest = None,
        *,
        max_results: int = ShapeBase.NOT_SET,
        next_token: str = ShapeBase.NOT_SET,
    ) -> shapes.GetDevEndpointsResponse:
        """
        Retrieves all the DevEndpoints in this AWS account.
        """
        if _request is None:
            _params = {}
            if max_results is not ShapeBase.NOT_SET:
                _params['max_results'] = max_results
            if next_token is not ShapeBase.NOT_SET:
                _params['next_token'] = next_token
            _request = shapes.GetDevEndpointsRequest(**_params)
        paginator = self.get_paginator("get_dev_endpoints").paginate(
            **_request.to_boto()
        )
        page_generator = (page for page in paginator)
        first_page = next(page_generator)
        result = shapes.GetDevEndpointsResponse.from_boto(first_page)
        result._page_iterator = page_generator
        return result

        return shapes.GetDevEndpointsResponse.from_boto(response)

    def get_job(
        self,
        _request: shapes.GetJobRequest = None,
        *,
        job_name: str,
    ) -> shapes.GetJobResponse:
        """
        Retrieves an existing job definition.
        """
        if _request is None:
            _params = {}
            if job_name is not ShapeBase.NOT_SET:
                _params['job_name'] = job_name
            _request = shapes.GetJobRequest(**_params)
        response = self._boto_client.get_job(**_request.to_boto())

        return shapes.GetJobResponse.from_boto(response)

    def get_job_run(
        self,
        _request: shapes.GetJobRunRequest = None,
        *,
        job_name: str,
        run_id: str,
        predecessors_included: bool = ShapeBase.NOT_SET,
    ) -> shapes.GetJobRunResponse:
        """
        Retrieves the metadata for a given job run.
        """
        if _request is None:
            _params = {}
            if job_name is not ShapeBase.NOT_SET:
                _params['job_name'] = job_name
            if run_id is not ShapeBase.NOT_SET:
                _params['run_id'] = run_id
            if predecessors_included is not ShapeBase.NOT_SET:
                _params['predecessors_included'] = predecessors_included
            _request = shapes.GetJobRunRequest(**_params)
        response = self._boto_client.get_job_run(**_request.to_boto())

        return shapes.GetJobRunResponse.from_boto(response)

    def get_job_runs(
        self,
        _request: shapes.GetJobRunsRequest = None,
        *,
        job_name: str,
        next_token: str = ShapeBase.NOT_SET,
        max_results: int = ShapeBase.NOT_SET,
    ) -> shapes.GetJobRunsResponse:
        """
        Retrieves metadata for all runs of a given job definition.
        """
        if _request is None:
            _params = {}
            if job_name is not ShapeBase.NOT_SET:
                _params['job_name'] = job_name
            if next_token is not ShapeBase.NOT_SET:
                _params['next_token'] = next_token
            if max_results is not ShapeBase.NOT_SET:
                _params['max_results'] = max_results
            _request = shapes.GetJobRunsRequest(**_params)
        paginator = self.get_paginator("get_job_runs").paginate(
            **_request.to_boto()
        )
        page_generator = (page for page in paginator)
        first_page = next(page_generator)
        result = shapes.GetJobRunsResponse.from_boto(first_page)
        result._page_iterator = page_generator
        return result

        return shapes.GetJobRunsResponse.from_boto(response)

    def get_jobs(
        self,
        _request: shapes.GetJobsRequest = None,
        *,
        next_token: str = ShapeBase.NOT_SET,
        max_results: int = ShapeBase.NOT_SET,
    ) -> shapes.GetJobsResponse:
        """
        Retrieves all current job definitions.
        """
        if _request is None:
            _params = {}
            if next_token is not ShapeBase.NOT_SET:
                _params['next_token'] = next_token
            if max_results is not ShapeBase.NOT_SET:
                _params['max_results'] = max_results
            _request = shapes.GetJobsRequest(**_params)
        paginator = self.get_paginator("get_jobs").paginate(
            **_request.to_boto()
        )
        page_generator = (page for page in paginator)
        first_page = next(page_generator)
        result = shapes.GetJobsResponse.from_boto(first_page)
        result._page_iterator = page_generator
        return result

        return shapes.GetJobsResponse.from_boto(response)

    def get_mapping(
        self,
        _request: shapes.GetMappingRequest = None,
        *,
        source: shapes.CatalogEntry,
        sinks: typing.List[shapes.CatalogEntry] = ShapeBase.NOT_SET,
        location: shapes.Location = ShapeBase.NOT_SET,
    ) -> shapes.GetMappingResponse:
        """
        Creates mappings.
        """
        if _request is None:
            _params = {}
            if source is not ShapeBase.NOT_SET:
                _params['source'] = source
            if sinks is not ShapeBase.NOT_SET:
                _params['sinks'] = sinks
            if location is not ShapeBase.NOT_SET:
                _params['location'] = location
            _request = shapes.GetMappingRequest(**_params)
        response = self._boto_client.get_mapping(**_request.to_boto())

        return shapes.GetMappingResponse.from_boto(response)

    def get_partition(
        self,
        _request: shapes.GetPartitionRequest = None,
        *,
        database_name: str,
        table_name: str,
        partition_values: typing.List[str],
        catalog_id: str = ShapeBase.NOT_SET,
    ) -> shapes.GetPartitionResponse:
        """
        Retrieves information about a specified partition.
        """
        if _request is None:
            _params = {}
            if database_name is not ShapeBase.NOT_SET:
                _params['database_name'] = database_name
            if table_name is not ShapeBase.NOT_SET:
                _params['table_name'] = table_name
            if partition_values is not ShapeBase.NOT_SET:
                _params['partition_values'] = partition_values
            if catalog_id is not ShapeBase.NOT_SET:
                _params['catalog_id'] = catalog_id
            _request = shapes.GetPartitionRequest(**_params)
        response = self._boto_client.get_partition(**_request.to_boto())

        return shapes.GetPartitionResponse.from_boto(response)

    def get_partitions(
        self,
        _request: shapes.GetPartitionsRequest = None,
        *,
        database_name: str,
        table_name: str,
        catalog_id: str = ShapeBase.NOT_SET,
        expression: str = ShapeBase.NOT_SET,
        next_token: str = ShapeBase.NOT_SET,
        segment: shapes.Segment = ShapeBase.NOT_SET,
        max_results: int = ShapeBase.NOT_SET,
    ) -> shapes.GetPartitionsResponse:
        """
        Retrieves information about the partitions in a table.
        """
        if _request is None:
            _params = {}
            if database_name is not ShapeBase.NOT_SET:
                _params['database_name'] = database_name
            if table_name is not ShapeBase.NOT_SET:
                _params['table_name'] = table_name
            if catalog_id is not ShapeBase.NOT_SET:
                _params['catalog_id'] = catalog_id
            if expression is not ShapeBase.NOT_SET:
                _params['expression'] = expression
            if next_token is not ShapeBase.NOT_SET:
                _params['next_token'] = next_token
            if segment is not ShapeBase.NOT_SET:
                _params['segment'] = segment
            if max_results is not ShapeBase.NOT_SET:
                _params['max_results'] = max_results
            _request = shapes.GetPartitionsRequest(**_params)
        paginator = self.get_paginator("get_partitions").paginate(
            **_request.to_boto()
        )
        page_generator = (page for page in paginator)
        first_page = next(page_generator)
        result = shapes.GetPartitionsResponse.from_boto(first_page)
        result._page_iterator = page_generator
        return result

        return shapes.GetPartitionsResponse.from_boto(response)

    def get_plan(
        self,
        _request: shapes.GetPlanRequest = None,
        *,
        mapping: typing.List[shapes.MappingEntry],
        source: shapes.CatalogEntry,
        sinks: typing.List[shapes.CatalogEntry] = ShapeBase.NOT_SET,
        location: shapes.Location = ShapeBase.NOT_SET,
        language: typing.Union[str, shapes.Language] = ShapeBase.NOT_SET,
    ) -> shapes.GetPlanResponse:
        """
        Gets code to perform a specified mapping.
        """
        if _request is None:
            _params = {}
            if mapping is not ShapeBase.NOT_SET:
                _params['mapping'] = mapping
            if source is not ShapeBase.NOT_SET:
                _params['source'] = source
            if sinks is not ShapeBase.NOT_SET:
                _params['sinks'] = sinks
            if location is not ShapeBase.NOT_SET:
                _params['location'] = location
            if language is not ShapeBase.NOT_SET:
                _params['language'] = language
            _request = shapes.GetPlanRequest(**_params)
        response = self._boto_client.get_plan(**_request.to_boto())

        return shapes.GetPlanResponse.from_boto(response)

    def get_security_configuration(
        self,
        _request: shapes.GetSecurityConfigurationRequest = None,
        *,
        name: str,
    ) -> shapes.GetSecurityConfigurationResponse:
        """
        Retrieves a specified security configuration.
        """
        if _request is None:
            _params = {}
            if name is not ShapeBase.NOT_SET:
                _params['name'] = name
            _request = shapes.GetSecurityConfigurationRequest(**_params)
        response = self._boto_client.get_security_configuration(
            **_request.to_boto()
        )

        return shapes.GetSecurityConfigurationResponse.from_boto(response)

    def get_security_configurations(
        self,
        _request: shapes.GetSecurityConfigurationsRequest = None,
        *,
        max_results: int = ShapeBase.NOT_SET,
        next_token: str = ShapeBase.NOT_SET,
    ) -> shapes.GetSecurityConfigurationsResponse:
        """
        Retrieves a list of all security configurations.
        """
        if _request is None:
            _params = {}
            if max_results is not ShapeBase.NOT_SET:
                _params['max_results'] = max_results
            if next_token is not ShapeBase.NOT_SET:
                _params['next_token'] = next_token
            _request = shapes.GetSecurityConfigurationsRequest(**_params)
        response = self._boto_client.get_security_configurations(
            **_request.to_boto()
        )

        return shapes.GetSecurityConfigurationsResponse.from_boto(response)

    def get_table(
        self,
        _request: shapes.GetTableRequest = None,
        *,
        database_name: str,
        name: str,
        catalog_id: str = ShapeBase.NOT_SET,
    ) -> shapes.GetTableResponse:
        """
        Retrieves the `Table` definition in a Data Catalog for a specified table.
        """
        if _request is None:
            _params = {}
            if database_name is not ShapeBase.NOT_SET:
                _params['database_name'] = database_name
            if name is not ShapeBase.NOT_SET:
                _params['name'] = name
            if catalog_id is not ShapeBase.NOT_SET:
                _params['catalog_id'] = catalog_id
            _request = shapes.GetTableRequest(**_params)
        response = self._boto_client.get_table(**_request.to_boto())

        return shapes.GetTableResponse.from_boto(response)

    def get_table_version(
        self,
        _request: shapes.GetTableVersionRequest = None,
        *,
        database_name: str,
        table_name: str,
        catalog_id: str = ShapeBase.NOT_SET,
        version_id: str = ShapeBase.NOT_SET,
    ) -> shapes.GetTableVersionResponse:
        """
        Retrieves a specified version of a table.
        """
        if _request is None:
            _params = {}
            if database_name is not ShapeBase.NOT_SET:
                _params['database_name'] = database_name
            if table_name is not ShapeBase.NOT_SET:
                _params['table_name'] = table_name
            if catalog_id is not ShapeBase.NOT_SET:
                _params['catalog_id'] = catalog_id
            if version_id is not ShapeBase.NOT_SET:
                _params['version_id'] = version_id
            _request = shapes.GetTableVersionRequest(**_params)
        response = self._boto_client.get_table_version(**_request.to_boto())

        return shapes.GetTableVersionResponse.from_boto(response)

    def get_table_versions(
        self,
        _request: shapes.GetTableVersionsRequest = None,
        *,
        database_name: str,
        table_name: str,
        catalog_id: str = ShapeBase.NOT_SET,
        next_token: str = ShapeBase.NOT_SET,
        max_results: int = ShapeBase.NOT_SET,
    ) -> shapes.GetTableVersionsResponse:
        """
        Retrieves a list of strings that identify available versions of a specified
        table.
        """
        if _request is None:
            _params = {}
            if database_name is not ShapeBase.NOT_SET:
                _params['database_name'] = database_name
            if table_name is not ShapeBase.NOT_SET:
                _params['table_name'] = table_name
            if catalog_id is not ShapeBase.NOT_SET:
                _params['catalog_id'] = catalog_id
            if next_token is not ShapeBase.NOT_SET:
                _params['next_token'] = next_token
            if max_results is not ShapeBase.NOT_SET:
                _params['max_results'] = max_results
            _request = shapes.GetTableVersionsRequest(**_params)
        paginator = self.get_paginator("get_table_versions").paginate(
            **_request.to_boto()
        )
        page_generator = (page for page in paginator)
        first_page = next(page_generator)
        result = shapes.GetTableVersionsResponse.from_boto(first_page)
        result._page_iterator = page_generator
        return result

        return shapes.GetTableVersionsResponse.from_boto(response)

    def get_tables(
        self,
        _request: shapes.GetTablesRequest = None,
        *,
        database_name: str,
        catalog_id: str = ShapeBase.NOT_SET,
        expression: str = ShapeBase.NOT_SET,
        next_token: str = ShapeBase.NOT_SET,
        max_results: int = ShapeBase.NOT_SET,
    ) -> shapes.GetTablesResponse:
        """
        Retrieves the definitions of some or all of the tables in a given `Database`.
        """
        if _request is None:
            _params = {}
            if database_name is not ShapeBase.NOT_SET:
                _params['database_name'] = database_name
            if catalog_id is not ShapeBase.NOT_SET:
                _params['catalog_id'] = catalog_id
            if expression is not ShapeBase.NOT_SET:
                _params['expression'] = expression
            if next_token is not ShapeBase.NOT_SET:
                _params['next_token'] = next_token
            if max_results is not ShapeBase.NOT_SET:
                _params['max_results'] = max_results
            _request = shapes.GetTablesRequest(**_params)
        paginator = self.get_paginator("get_tables").paginate(
            **_request.to_boto()
        )
        page_generator = (page for page in paginator)
        first_page = next(page_generator)
        result = shapes.GetTablesResponse.from_boto(first_page)
        result._page_iterator = page_generator
        return result

        return shapes.GetTablesResponse.from_boto(response)

    def get_trigger(
        self,
        _request: shapes.GetTriggerRequest = None,
        *,
        name: str,
    ) -> shapes.GetTriggerResponse:
        """
        Retrieves the definition of a trigger.
        """
        if _request is None:
            _params = {}
            if name is not ShapeBase.NOT_SET:
                _params['name'] = name
            _request = shapes.GetTriggerRequest(**_params)
        response = self._boto_client.get_trigger(**_request.to_boto())

        return shapes.GetTriggerResponse.from_boto(response)

    def get_triggers(
        self,
        _request: shapes.GetTriggersRequest = None,
        *,
        next_token: str = ShapeBase.NOT_SET,
        dependent_job_name: str = ShapeBase.NOT_SET,
        max_results: int = ShapeBase.NOT_SET,
    ) -> shapes.GetTriggersResponse:
        """
        Gets all the triggers associated with a job.
        """
        if _request is None:
            _params = {}
            if next_token is not ShapeBase.NOT_SET:
                _params['next_token'] = next_token
            if dependent_job_name is not ShapeBase.NOT_SET:
                _params['dependent_job_name'] = dependent_job_name
            if max_results is not ShapeBase.NOT_SET:
                _params['max_results'] = max_results
            _request = shapes.GetTriggersRequest(**_params)
        paginator = self.get_paginator("get_triggers").paginate(
            **_request.to_boto()
        )
        page_generator = (page for page in paginator)
        first_page = next(page_generator)
        result = shapes.GetTriggersResponse.from_boto(first_page)
        result._page_iterator = page_generator
        return result

        return shapes.GetTriggersResponse.from_boto(response)

    def get_user_defined_function(
        self,
        _request: shapes.GetUserDefinedFunctionRequest = None,
        *,
        database_name: str,
        function_name: str,
        catalog_id: str = ShapeBase.NOT_SET,
    ) -> shapes.GetUserDefinedFunctionResponse:
        """
        Retrieves a specified function definition from the Data Catalog.
        """
        if _request is None:
            _params = {}
            if database_name is not ShapeBase.NOT_SET:
                _params['database_name'] = database_name
            if function_name is not ShapeBase.NOT_SET:
                _params['function_name'] = function_name
            if catalog_id is not ShapeBase.NOT_SET:
                _params['catalog_id'] = catalog_id
            _request = shapes.GetUserDefinedFunctionRequest(**_params)
        response = self._boto_client.get_user_defined_function(
            **_request.to_boto()
        )

        return shapes.GetUserDefinedFunctionResponse.from_boto(response)

    def get_user_defined_functions(
        self,
        _request: shapes.GetUserDefinedFunctionsRequest = None,
        *,
        database_name: str,
        pattern: str,
        catalog_id: str = ShapeBase.NOT_SET,
        next_token: str = ShapeBase.NOT_SET,
        max_results: int = ShapeBase.NOT_SET,
    ) -> shapes.GetUserDefinedFunctionsResponse:
        """
        Retrieves a multiple function definitions from the Data Catalog.
        """
        if _request is None:
            _params = {}
            if database_name is not ShapeBase.NOT_SET:
                _params['database_name'] = database_name
            if pattern is not ShapeBase.NOT_SET:
                _params['pattern'] = pattern
            if catalog_id is not ShapeBase.NOT_SET:
                _params['catalog_id'] = catalog_id
            if next_token is not ShapeBase.NOT_SET:
                _params['next_token'] = next_token
            if max_results is not ShapeBase.NOT_SET:
                _params['max_results'] = max_results
            _request = shapes.GetUserDefinedFunctionsRequest(**_params)
        paginator = self.get_paginator("get_user_defined_functions").paginate(
            **_request.to_boto()
        )
        page_generator = (page for page in paginator)
        first_page = next(page_generator)
        result = shapes.GetUserDefinedFunctionsResponse.from_boto(first_page)
        result._page_iterator = page_generator
        return result

        return shapes.GetUserDefinedFunctionsResponse.from_boto(response)

    def import_catalog_to_glue(
        self,
        _request: shapes.ImportCatalogToGlueRequest = None,
        *,
        catalog_id: str = ShapeBase.NOT_SET,
    ) -> shapes.ImportCatalogToGlueResponse:
        """
        Imports an existing Athena Data Catalog to AWS Glue
        """
        if _request is None:
            _params = {}
            if catalog_id is not ShapeBase.NOT_SET:
                _params['catalog_id'] = catalog_id
            _request = shapes.ImportCatalogToGlueRequest(**_params)
        response = self._boto_client.import_catalog_to_glue(
            **_request.to_boto()
        )

        return shapes.ImportCatalogToGlueResponse.from_boto(response)

    def put_data_catalog_encryption_settings(
        self,
        _request: shapes.PutDataCatalogEncryptionSettingsRequest = None,
        *,
        data_catalog_encryption_settings: shapes.DataCatalogEncryptionSettings,
        catalog_id: str = ShapeBase.NOT_SET,
    ) -> shapes.PutDataCatalogEncryptionSettingsResponse:
        """
        Sets the security configuration for a specified catalog. Once the configuration
        has been set, the specified encryption is applied to every catalog write
        thereafter.
        """
        if _request is None:
            _params = {}
            if data_catalog_encryption_settings is not ShapeBase.NOT_SET:
                _params['data_catalog_encryption_settings'
                       ] = data_catalog_encryption_settings
            if catalog_id is not ShapeBase.NOT_SET:
                _params['catalog_id'] = catalog_id
            _request = shapes.PutDataCatalogEncryptionSettingsRequest(**_params)
        response = self._boto_client.put_data_catalog_encryption_settings(
            **_request.to_boto()
        )

        return shapes.PutDataCatalogEncryptionSettingsResponse.from_boto(
            response
        )

    def reset_job_bookmark(
        self,
        _request: shapes.ResetJobBookmarkRequest = None,
        *,
        job_name: str,
    ) -> shapes.ResetJobBookmarkResponse:
        """
        Resets a bookmark entry.
        """
        if _request is None:
            _params = {}
            if job_name is not ShapeBase.NOT_SET:
                _params['job_name'] = job_name
            _request = shapes.ResetJobBookmarkRequest(**_params)
        response = self._boto_client.reset_job_bookmark(**_request.to_boto())

        return shapes.ResetJobBookmarkResponse.from_boto(response)

    def start_crawler(
        self,
        _request: shapes.StartCrawlerRequest = None,
        *,
        name: str,
    ) -> shapes.StartCrawlerResponse:
        """
        Starts a crawl using the specified crawler, regardless of what is scheduled. If
        the crawler is already running, returns a
        [CrawlerRunningException](https://docs.aws.amazon.com/glue/latest/dg/aws-glue-
        api-exceptions.html#aws-glue-api-exceptions-CrawlerRunningException).
        """
        if _request is None:
            _params = {}
            if name is not ShapeBase.NOT_SET:
                _params['name'] = name
            _request = shapes.StartCrawlerRequest(**_params)
        response = self._boto_client.start_crawler(**_request.to_boto())

        return shapes.StartCrawlerResponse.from_boto(response)

    def start_crawler_schedule(
        self,
        _request: shapes.StartCrawlerScheduleRequest = None,
        *,
        crawler_name: str,
    ) -> shapes.StartCrawlerScheduleResponse:
        """
        Changes the schedule state of the specified crawler to `SCHEDULED`, unless the
        crawler is already running or the schedule state is already `SCHEDULED`.
        """
        if _request is None:
            _params = {}
            if crawler_name is not ShapeBase.NOT_SET:
                _params['crawler_name'] = crawler_name
            _request = shapes.StartCrawlerScheduleRequest(**_params)
        response = self._boto_client.start_crawler_schedule(
            **_request.to_boto()
        )

        return shapes.StartCrawlerScheduleResponse.from_boto(response)

    def start_job_run(
        self,
        _request: shapes.StartJobRunRequest = None,
        *,
        job_name: str,
        job_run_id: str = ShapeBase.NOT_SET,
        arguments: typing.Dict[str, str] = ShapeBase.NOT_SET,
        allocated_capacity: int = ShapeBase.NOT_SET,
        timeout: int = ShapeBase.NOT_SET,
        notification_property: shapes.NotificationProperty = ShapeBase.NOT_SET,
        security_configuration: str = ShapeBase.NOT_SET,
    ) -> shapes.StartJobRunResponse:
        """
        Starts a job run using a job definition.
        """
        if _request is None:
            _params = {}
            if job_name is not ShapeBase.NOT_SET:
                _params['job_name'] = job_name
            if job_run_id is not ShapeBase.NOT_SET:
                _params['job_run_id'] = job_run_id
            if arguments is not ShapeBase.NOT_SET:
                _params['arguments'] = arguments
            if allocated_capacity is not ShapeBase.NOT_SET:
                _params['allocated_capacity'] = allocated_capacity
            if timeout is not ShapeBase.NOT_SET:
                _params['timeout'] = timeout
            if notification_property is not ShapeBase.NOT_SET:
                _params['notification_property'] = notification_property
            if security_configuration is not ShapeBase.NOT_SET:
                _params['security_configuration'] = security_configuration
            _request = shapes.StartJobRunRequest(**_params)
        response = self._boto_client.start_job_run(**_request.to_boto())

        return shapes.StartJobRunResponse.from_boto(response)

    def start_trigger(
        self,
        _request: shapes.StartTriggerRequest = None,
        *,
        name: str,
    ) -> shapes.StartTriggerResponse:
        """
        Starts an existing trigger. See [Triggering
        Jobs](http://docs.aws.amazon.com/glue/latest/dg/trigger-job.html) for
        information about how different types of trigger are started.
        """
        if _request is None:
            _params = {}
            if name is not ShapeBase.NOT_SET:
                _params['name'] = name
            _request = shapes.StartTriggerRequest(**_params)
        response = self._boto_client.start_trigger(**_request.to_boto())

        return shapes.StartTriggerResponse.from_boto(response)

    def stop_crawler(
        self,
        _request: shapes.StopCrawlerRequest = None,
        *,
        name: str,
    ) -> shapes.StopCrawlerResponse:
        """
        If the specified crawler is running, stops the crawl.
        """
        if _request is None:
            _params = {}
            if name is not ShapeBase.NOT_SET:
                _params['name'] = name
            _request = shapes.StopCrawlerRequest(**_params)
        response = self._boto_client.stop_crawler(**_request.to_boto())

        return shapes.StopCrawlerResponse.from_boto(response)

    def stop_crawler_schedule(
        self,
        _request: shapes.StopCrawlerScheduleRequest = None,
        *,
        crawler_name: str,
    ) -> shapes.StopCrawlerScheduleResponse:
        """
        Sets the schedule state of the specified crawler to `NOT_SCHEDULED`, but does
        not stop the crawler if it is already running.
        """
        if _request is None:
            _params = {}
            if crawler_name is not ShapeBase.NOT_SET:
                _params['crawler_name'] = crawler_name
            _request = shapes.StopCrawlerScheduleRequest(**_params)
        response = self._boto_client.stop_crawler_schedule(**_request.to_boto())

        return shapes.StopCrawlerScheduleResponse.from_boto(response)

    def stop_trigger(
        self,
        _request: shapes.StopTriggerRequest = None,
        *,
        name: str,
    ) -> shapes.StopTriggerResponse:
        """
        Stops a specified trigger.
        """
        if _request is None:
            _params = {}
            if name is not ShapeBase.NOT_SET:
                _params['name'] = name
            _request = shapes.StopTriggerRequest(**_params)
        response = self._boto_client.stop_trigger(**_request.to_boto())

        return shapes.StopTriggerResponse.from_boto(response)

    def update_classifier(
        self,
        _request: shapes.UpdateClassifierRequest = None,
        *,
        grok_classifier: shapes.UpdateGrokClassifierRequest = ShapeBase.NOT_SET,
        xml_classifier: shapes.UpdateXMLClassifierRequest = ShapeBase.NOT_SET,
        json_classifier: shapes.UpdateJsonClassifierRequest = ShapeBase.NOT_SET,
    ) -> shapes.UpdateClassifierResponse:
        """
        Modifies an existing classifier (a `GrokClassifier`, `XMLClassifier`, or
        `JsonClassifier`, depending on which field is present).
        """
        if _request is None:
            _params = {}
            if grok_classifier is not ShapeBase.NOT_SET:
                _params['grok_classifier'] = grok_classifier
            if xml_classifier is not ShapeBase.NOT_SET:
                _params['xml_classifier'] = xml_classifier
            if json_classifier is not ShapeBase.NOT_SET:
                _params['json_classifier'] = json_classifier
            _request = shapes.UpdateClassifierRequest(**_params)
        response = self._boto_client.update_classifier(**_request.to_boto())

        return shapes.UpdateClassifierResponse.from_boto(response)

    def update_connection(
        self,
        _request: shapes.UpdateConnectionRequest = None,
        *,
        name: str,
        connection_input: shapes.ConnectionInput,
        catalog_id: str = ShapeBase.NOT_SET,
    ) -> shapes.UpdateConnectionResponse:
        """
        Updates a connection definition in the Data Catalog.
        """
        if _request is None:
            _params = {}
            if name is not ShapeBase.NOT_SET:
                _params['name'] = name
            if connection_input is not ShapeBase.NOT_SET:
                _params['connection_input'] = connection_input
            if catalog_id is not ShapeBase.NOT_SET:
                _params['catalog_id'] = catalog_id
            _request = shapes.UpdateConnectionRequest(**_params)
        response = self._boto_client.update_connection(**_request.to_boto())

        return shapes.UpdateConnectionResponse.from_boto(response)

    def update_crawler(
        self,
        _request: shapes.UpdateCrawlerRequest = None,
        *,
        name: str,
        role: str = ShapeBase.NOT_SET,
        database_name: str = ShapeBase.NOT_SET,
        description: str = ShapeBase.NOT_SET,
        targets: shapes.CrawlerTargets = ShapeBase.NOT_SET,
        schedule: str = ShapeBase.NOT_SET,
        classifiers: typing.List[str] = ShapeBase.NOT_SET,
        table_prefix: str = ShapeBase.NOT_SET,
        schema_change_policy: shapes.SchemaChangePolicy = ShapeBase.NOT_SET,
        configuration: str = ShapeBase.NOT_SET,
        crawler_security_configuration: str = ShapeBase.NOT_SET,
    ) -> shapes.UpdateCrawlerResponse:
        """
        Updates a crawler. If a crawler is running, you must stop it using `StopCrawler`
        before updating it.
        """
        if _request is None:
            _params = {}
            if name is not ShapeBase.NOT_SET:
                _params['name'] = name
            if role is not ShapeBase.NOT_SET:
                _params['role'] = role
            if database_name is not ShapeBase.NOT_SET:
                _params['database_name'] = database_name
            if description is not ShapeBase.NOT_SET:
                _params['description'] = description
            if targets is not ShapeBase.NOT_SET:
                _params['targets'] = targets
            if schedule is not ShapeBase.NOT_SET:
                _params['schedule'] = schedule
            if classifiers is not ShapeBase.NOT_SET:
                _params['classifiers'] = classifiers
            if table_prefix is not ShapeBase.NOT_SET:
                _params['table_prefix'] = table_prefix
            if schema_change_policy is not ShapeBase.NOT_SET:
                _params['schema_change_policy'] = schema_change_policy
            if configuration is not ShapeBase.NOT_SET:
                _params['configuration'] = configuration
            if crawler_security_configuration is not ShapeBase.NOT_SET:
                _params['crawler_security_configuration'
                       ] = crawler_security_configuration
            _request = shapes.UpdateCrawlerRequest(**_params)
        response = self._boto_client.update_crawler(**_request.to_boto())

        return shapes.UpdateCrawlerResponse.from_boto(response)

    def update_crawler_schedule(
        self,
        _request: shapes.UpdateCrawlerScheduleRequest = None,
        *,
        crawler_name: str,
        schedule: str = ShapeBase.NOT_SET,
    ) -> shapes.UpdateCrawlerScheduleResponse:
        """
        Updates the schedule of a crawler using a `cron` expression.
        """
        if _request is None:
            _params = {}
            if crawler_name is not ShapeBase.NOT_SET:
                _params['crawler_name'] = crawler_name
            if schedule is not ShapeBase.NOT_SET:
                _params['schedule'] = schedule
            _request = shapes.UpdateCrawlerScheduleRequest(**_params)
        response = self._boto_client.update_crawler_schedule(
            **_request.to_boto()
        )

        return shapes.UpdateCrawlerScheduleResponse.from_boto(response)

    def update_database(
        self,
        _request: shapes.UpdateDatabaseRequest = None,
        *,
        name: str,
        database_input: shapes.DatabaseInput,
        catalog_id: str = ShapeBase.NOT_SET,
    ) -> shapes.UpdateDatabaseResponse:
        """
        Updates an existing database definition in a Data Catalog.
        """
        if _request is None:
            _params = {}
            if name is not ShapeBase.NOT_SET:
                _params['name'] = name
            if database_input is not ShapeBase.NOT_SET:
                _params['database_input'] = database_input
            if catalog_id is not ShapeBase.NOT_SET:
                _params['catalog_id'] = catalog_id
            _request = shapes.UpdateDatabaseRequest(**_params)
        response = self._boto_client.update_database(**_request.to_boto())

        return shapes.UpdateDatabaseResponse.from_boto(response)

    def update_dev_endpoint(
        self,
        _request: shapes.UpdateDevEndpointRequest = None,
        *,
        endpoint_name: str,
        public_key: str = ShapeBase.NOT_SET,
        add_public_keys: typing.List[str] = ShapeBase.NOT_SET,
        delete_public_keys: typing.List[str] = ShapeBase.NOT_SET,
        custom_libraries: shapes.DevEndpointCustomLibraries = ShapeBase.NOT_SET,
        update_etl_libraries: bool = ShapeBase.NOT_SET,
    ) -> shapes.UpdateDevEndpointResponse:
        """
        Updates a specified DevEndpoint.
        """
        if _request is None:
            _params = {}
            if endpoint_name is not ShapeBase.NOT_SET:
                _params['endpoint_name'] = endpoint_name
            if public_key is not ShapeBase.NOT_SET:
                _params['public_key'] = public_key
            if add_public_keys is not ShapeBase.NOT_SET:
                _params['add_public_keys'] = add_public_keys
            if delete_public_keys is not ShapeBase.NOT_SET:
                _params['delete_public_keys'] = delete_public_keys
            if custom_libraries is not ShapeBase.NOT_SET:
                _params['custom_libraries'] = custom_libraries
            if update_etl_libraries is not ShapeBase.NOT_SET:
                _params['update_etl_libraries'] = update_etl_libraries
            _request = shapes.UpdateDevEndpointRequest(**_params)
        response = self._boto_client.update_dev_endpoint(**_request.to_boto())

        return shapes.UpdateDevEndpointResponse.from_boto(response)

    def update_job(
        self,
        _request: shapes.UpdateJobRequest = None,
        *,
        job_name: str,
        job_update: shapes.JobUpdate,
    ) -> shapes.UpdateJobResponse:
        """
        Updates an existing job definition.
        """
        if _request is None:
            _params = {}
            if job_name is not ShapeBase.NOT_SET:
                _params['job_name'] = job_name
            if job_update is not ShapeBase.NOT_SET:
                _params['job_update'] = job_update
            _request = shapes.UpdateJobRequest(**_params)
        response = self._boto_client.update_job(**_request.to_boto())

        return shapes.UpdateJobResponse.from_boto(response)

    def update_partition(
        self,
        _request: shapes.UpdatePartitionRequest = None,
        *,
        database_name: str,
        table_name: str,
        partition_value_list: typing.List[str],
        partition_input: shapes.PartitionInput,
        catalog_id: str = ShapeBase.NOT_SET,
    ) -> shapes.UpdatePartitionResponse:
        """
        Updates a partition.
        """
        if _request is None:
            _params = {}
            if database_name is not ShapeBase.NOT_SET:
                _params['database_name'] = database_name
            if table_name is not ShapeBase.NOT_SET:
                _params['table_name'] = table_name
            if partition_value_list is not ShapeBase.NOT_SET:
                _params['partition_value_list'] = partition_value_list
            if partition_input is not ShapeBase.NOT_SET:
                _params['partition_input'] = partition_input
            if catalog_id is not ShapeBase.NOT_SET:
                _params['catalog_id'] = catalog_id
            _request = shapes.UpdatePartitionRequest(**_params)
        response = self._boto_client.update_partition(**_request.to_boto())

        return shapes.UpdatePartitionResponse.from_boto(response)

    def update_table(
        self,
        _request: shapes.UpdateTableRequest = None,
        *,
        database_name: str,
        table_input: shapes.TableInput,
        catalog_id: str = ShapeBase.NOT_SET,
        skip_archive: bool = ShapeBase.NOT_SET,
    ) -> shapes.UpdateTableResponse:
        """
        Updates a metadata table in the Data Catalog.
        """
        if _request is None:
            _params = {}
            if database_name is not ShapeBase.NOT_SET:
                _params['database_name'] = database_name
            if table_input is not ShapeBase.NOT_SET:
                _params['table_input'] = table_input
            if catalog_id is not ShapeBase.NOT_SET:
                _params['catalog_id'] = catalog_id
            if skip_archive is not ShapeBase.NOT_SET:
                _params['skip_archive'] = skip_archive
            _request = shapes.UpdateTableRequest(**_params)
        response = self._boto_client.update_table(**_request.to_boto())

        return shapes.UpdateTableResponse.from_boto(response)

    def update_trigger(
        self,
        _request: shapes.UpdateTriggerRequest = None,
        *,
        name: str,
        trigger_update: shapes.TriggerUpdate,
    ) -> shapes.UpdateTriggerResponse:
        """
        Updates a trigger definition.
        """
        if _request is None:
            _params = {}
            if name is not ShapeBase.NOT_SET:
                _params['name'] = name
            if trigger_update is not ShapeBase.NOT_SET:
                _params['trigger_update'] = trigger_update
            _request = shapes.UpdateTriggerRequest(**_params)
        response = self._boto_client.update_trigger(**_request.to_boto())

        return shapes.UpdateTriggerResponse.from_boto(response)

    def update_user_defined_function(
        self,
        _request: shapes.UpdateUserDefinedFunctionRequest = None,
        *,
        database_name: str,
        function_name: str,
        function_input: shapes.UserDefinedFunctionInput,
        catalog_id: str = ShapeBase.NOT_SET,
    ) -> shapes.UpdateUserDefinedFunctionResponse:
        """
        Updates an existing function definition in the Data Catalog.
        """
        if _request is None:
            _params = {}
            if database_name is not ShapeBase.NOT_SET:
                _params['database_name'] = database_name
            if function_name is not ShapeBase.NOT_SET:
                _params['function_name'] = function_name
            if function_input is not ShapeBase.NOT_SET:
                _params['function_input'] = function_input
            if catalog_id is not ShapeBase.NOT_SET:
                _params['catalog_id'] = catalog_id
            _request = shapes.UpdateUserDefinedFunctionRequest(**_params)
        response = self._boto_client.update_user_defined_function(
            **_request.to_boto()
        )

        return shapes.UpdateUserDefinedFunctionResponse.from_boto(response)
