import datetime
import typing
import boto3
from autoboto import ClientBase, ShapeBase, OutputShapeBase
from . import shapes


class Client(ClientBase):
    def __init__(self, *args, **kwargs):
        super().__init__("dynamodb", *args, **kwargs)

    def batch_get_item(
        self,
        _request: shapes.BatchGetItemInput = None,
        *,
        request_items: typing.Dict[str, shapes.KeysAndAttributes],
        return_consumed_capacity: typing.
        Union[str, shapes.ReturnConsumedCapacity] = ShapeBase.NOT_SET,
    ) -> shapes.BatchGetItemOutput:
        """
        The `BatchGetItem` operation returns the attributes of one or more items from
        one or more tables. You identify requested items by primary key.

        A single operation can retrieve up to 16 MB of data, which can contain as many
        as 100 items. `BatchGetItem` will return a partial result if the response size
        limit is exceeded, the table's provisioned throughput is exceeded, or an
        internal processing failure occurs. If a partial result is returned, the
        operation returns a value for `UnprocessedKeys`. You can use this value to retry
        the operation starting with the next item to get.

        If you request more than 100 items `BatchGetItem` will return a
        `ValidationException` with the message "Too many items requested for the
        BatchGetItem call".

        For example, if you ask to retrieve 100 items, but each individual item is 300
        KB in size, the system returns 52 items (so as not to exceed the 16 MB limit).
        It also returns an appropriate `UnprocessedKeys` value so you can get the next
        page of results. If desired, your application can include its own logic to
        assemble the pages of results into one data set.

        If _none_ of the items can be processed due to insufficient provisioned
        throughput on all of the tables in the request, then `BatchGetItem` will return
        a `ProvisionedThroughputExceededException`. If _at least one_ of the items is
        successfully processed, then `BatchGetItem` completes successfully, while
        returning the keys of the unread items in `UnprocessedKeys`.

        If DynamoDB returns any unprocessed items, you should retry the batch operation
        on those items. However, _we strongly recommend that you use an exponential
        backoff algorithm_. If you retry the batch operation immediately, the underlying
        read or write requests can still fail due to throttling on the individual
        tables. If you delay the batch operation using exponential backoff, the
        individual requests in the batch are much more likely to succeed.

        For more information, see [Batch Operations and Error
        Handling](http://docs.aws.amazon.com/amazondynamodb/latest/developerguide/ErrorHandling.html#BatchOperations)
        in the _Amazon DynamoDB Developer Guide_.

        By default, `BatchGetItem` performs eventually consistent reads on every table
        in the request. If you want strongly consistent reads instead, you can set
        `ConsistentRead` to `true` for any or all tables.

        In order to minimize response latency, `BatchGetItem` retrieves items in
        parallel.

        When designing your application, keep in mind that DynamoDB does not return
        items in any particular order. To help parse the response by item, include the
        primary key values for the items in your request in the `ProjectionExpression`
        parameter.

        If a requested item does not exist, it is not returned in the result. Requests
        for nonexistent items consume the minimum read capacity units according to the
        type of read. For more information, see [Capacity Units
        Calculations](http://docs.aws.amazon.com/amazondynamodb/latest/developerguide/WorkingWithTables.html#CapacityUnitCalculations)
        in the _Amazon DynamoDB Developer Guide_.
        """
        if _request is None:
            _params = {}
            if request_items is not ShapeBase.NOT_SET:
                _params['request_items'] = request_items
            if return_consumed_capacity is not ShapeBase.NOT_SET:
                _params['return_consumed_capacity'] = return_consumed_capacity
            _request = shapes.BatchGetItemInput(**_params)
        response = self._boto_client.batch_get_item(**_request.to_boto())

        return shapes.BatchGetItemOutput.from_boto(response)

    def batch_write_item(
        self,
        _request: shapes.BatchWriteItemInput = None,
        *,
        request_items: typing.Dict[str, typing.List[shapes.WriteRequest]],
        return_consumed_capacity: typing.
        Union[str, shapes.ReturnConsumedCapacity] = ShapeBase.NOT_SET,
        return_item_collection_metrics: typing.
        Union[str, shapes.ReturnItemCollectionMetrics] = ShapeBase.NOT_SET,
    ) -> shapes.BatchWriteItemOutput:
        """
        The `BatchWriteItem` operation puts or deletes multiple items in one or more
        tables. A single call to `BatchWriteItem` can write up to 16 MB of data, which
        can comprise as many as 25 put or delete requests. Individual items to be
        written can be as large as 400 KB.

        `BatchWriteItem` cannot update items. To update items, use the `UpdateItem`
        action.

        The individual `PutItem` and `DeleteItem` operations specified in
        `BatchWriteItem` are atomic; however `BatchWriteItem` as a whole is not. If any
        requested operations fail because the table's provisioned throughput is exceeded
        or an internal processing failure occurs, the failed operations are returned in
        the `UnprocessedItems` response parameter. You can investigate and optionally
        resend the requests. Typically, you would call `BatchWriteItem` in a loop. Each
        iteration would check for unprocessed items and submit a new `BatchWriteItem`
        request with those unprocessed items until all items have been processed.

        Note that if _none_ of the items can be processed due to insufficient
        provisioned throughput on all of the tables in the request, then
        `BatchWriteItem` will return a `ProvisionedThroughputExceededException`.

        If DynamoDB returns any unprocessed items, you should retry the batch operation
        on those items. However, _we strongly recommend that you use an exponential
        backoff algorithm_. If you retry the batch operation immediately, the underlying
        read or write requests can still fail due to throttling on the individual
        tables. If you delay the batch operation using exponential backoff, the
        individual requests in the batch are much more likely to succeed.

        For more information, see [Batch Operations and Error
        Handling](http://docs.aws.amazon.com/amazondynamodb/latest/developerguide/ErrorHandling.html#BatchOperations)
        in the _Amazon DynamoDB Developer Guide_.

        With `BatchWriteItem`, you can efficiently write or delete large amounts of
        data, such as from Amazon Elastic MapReduce (EMR), or copy data from another
        database into DynamoDB. In order to improve performance with these large-scale
        operations, `BatchWriteItem` does not behave in the same way as individual
        `PutItem` and `DeleteItem` calls would. For example, you cannot specify
        conditions on individual put and delete requests, and `BatchWriteItem` does not
        return deleted items in the response.

        If you use a programming language that supports concurrency, you can use threads
        to write items in parallel. Your application must include the necessary logic to
        manage the threads. With languages that don't support threading, you must update
        or delete the specified items one at a time. In both situations,
        `BatchWriteItem` performs the specified put and delete operations in parallel,
        giving you the power of the thread pool approach without having to introduce
        complexity into your application.

        Parallel processing reduces latency, but each specified put and delete request
        consumes the same number of write capacity units whether it is processed in
        parallel or not. Delete operations on nonexistent items consume one write
        capacity unit.

        If one or more of the following is true, DynamoDB rejects the entire batch write
        operation:

          * One or more tables specified in the `BatchWriteItem` request does not exist.

          * Primary key attributes specified on an item in the request do not match those in the corresponding table's primary key schema.

          * You try to perform multiple operations on the same item in the same `BatchWriteItem` request. For example, you cannot put and delete the same item in the same `BatchWriteItem` request. 

          * Your request contains at least two items with identical hash and range keys (which essentially is two put operations). 

          * There are more than 25 requests in the batch.

          * Any individual item in a batch exceeds 400 KB.

          * The total request size exceeds 16 MB.
        """
        if _request is None:
            _params = {}
            if request_items is not ShapeBase.NOT_SET:
                _params['request_items'] = request_items
            if return_consumed_capacity is not ShapeBase.NOT_SET:
                _params['return_consumed_capacity'] = return_consumed_capacity
            if return_item_collection_metrics is not ShapeBase.NOT_SET:
                _params['return_item_collection_metrics'
                       ] = return_item_collection_metrics
            _request = shapes.BatchWriteItemInput(**_params)
        response = self._boto_client.batch_write_item(**_request.to_boto())

        return shapes.BatchWriteItemOutput.from_boto(response)

    def create_backup(
        self,
        _request: shapes.CreateBackupInput = None,
        *,
        table_name: str,
        backup_name: str,
    ) -> shapes.CreateBackupOutput:
        """
        Creates a backup for an existing table.

        Each time you create an On-Demand Backup, the entire table data is backed up.
        There is no limit to the number of on-demand backups that can be taken.

        When you create an On-Demand Backup, a time marker of the request is cataloged,
        and the backup is created asynchronously, by applying all changes until the time
        of the request to the last full table snapshot. Backup requests are processed
        instantaneously and become available for restore within minutes.

        You can call `CreateBackup` at a maximum rate of 50 times per second.

        All backups in DynamoDB work without consuming any provisioned throughput on the
        table.

        If you submit a backup request on 2018-12-14 at 14:25:00, the backup is
        guaranteed to contain all data committed to the table up to 14:24:00, and data
        committed after 14:26:00 will not be. The backup may or may not contain data
        modifications made between 14:24:00 and 14:26:00. On-Demand Backup does not
        support causal consistency.

        Along with data, the following are also included on the backups:

          * Global secondary indexes (GSIs)

          * Local secondary indexes (LSIs)

          * Streams

          * Provisioned read and write capacity
        """
        if _request is None:
            _params = {}
            if table_name is not ShapeBase.NOT_SET:
                _params['table_name'] = table_name
            if backup_name is not ShapeBase.NOT_SET:
                _params['backup_name'] = backup_name
            _request = shapes.CreateBackupInput(**_params)
        response = self._boto_client.create_backup(**_request.to_boto())

        return shapes.CreateBackupOutput.from_boto(response)

    def create_global_table(
        self,
        _request: shapes.CreateGlobalTableInput = None,
        *,
        global_table_name: str,
        replication_group: typing.List[shapes.Replica],
    ) -> shapes.CreateGlobalTableOutput:
        """
        Creates a global table from an existing table. A global table creates a
        replication relationship between two or more DynamoDB tables with the same table
        name in the provided regions.

        If you want to add a new replica table to a global table, each of the following
        conditions must be true:

          * The table must have the same primary key as all of the other replicas.

          * The table must have the same name as all of the other replicas.

          * The table must have DynamoDB Streams enabled, with the stream containing both the new and the old images of the item.

          * None of the replica tables in the global table can contain any data.

        If global secondary indexes are specified, then the following conditions must
        also be met:

          * The global secondary indexes must have the same name. 

          * The global secondary indexes must have the same hash key and sort key (if present). 

        Write capacity settings should be set consistently across your replica tables
        and secondary indexes. DynamoDB strongly recommends enabling auto scaling to
        manage the write capacity settings for all of your global tables replicas and
        indexes.

        If you prefer to manage write capacity settings manually, you should provision
        equal replicated write capacity units to your replica tables. You should also
        provision equal replicated write capacity units to matching secondary indexes
        across your global table.
        """
        if _request is None:
            _params = {}
            if global_table_name is not ShapeBase.NOT_SET:
                _params['global_table_name'] = global_table_name
            if replication_group is not ShapeBase.NOT_SET:
                _params['replication_group'] = replication_group
            _request = shapes.CreateGlobalTableInput(**_params)
        response = self._boto_client.create_global_table(**_request.to_boto())

        return shapes.CreateGlobalTableOutput.from_boto(response)

    def create_table(
        self,
        _request: shapes.CreateTableInput = None,
        *,
        attribute_definitions: typing.List[shapes.AttributeDefinition],
        table_name: str,
        key_schema: typing.List[shapes.KeySchemaElement],
        provisioned_throughput: shapes.ProvisionedThroughput,
        local_secondary_indexes: typing.List[shapes.LocalSecondaryIndex
                                            ] = ShapeBase.NOT_SET,
        global_secondary_indexes: typing.List[shapes.GlobalSecondaryIndex
                                             ] = ShapeBase.NOT_SET,
        stream_specification: shapes.StreamSpecification = ShapeBase.NOT_SET,
        sse_specification: shapes.SSESpecification = ShapeBase.NOT_SET,
    ) -> shapes.CreateTableOutput:
        """
        The `CreateTable` operation adds a new table to your account. In an AWS account,
        table names must be unique within each region. That is, you can have two tables
        with same name if you create the tables in different regions.

        `CreateTable` is an asynchronous operation. Upon receiving a `CreateTable`
        request, DynamoDB immediately returns a response with a `TableStatus` of
        `CREATING`. After the table is created, DynamoDB sets the `TableStatus` to
        `ACTIVE`. You can perform read and write operations only on an `ACTIVE` table.

        You can optionally define secondary indexes on the new table, as part of the
        `CreateTable` operation. If you want to create multiple tables with secondary
        indexes on them, you must create the tables sequentially. Only one table with
        secondary indexes can be in the `CREATING` state at any given time.

        You can use the `DescribeTable` action to check the table status.
        """
        if _request is None:
            _params = {}
            if attribute_definitions is not ShapeBase.NOT_SET:
                _params['attribute_definitions'] = attribute_definitions
            if table_name is not ShapeBase.NOT_SET:
                _params['table_name'] = table_name
            if key_schema is not ShapeBase.NOT_SET:
                _params['key_schema'] = key_schema
            if provisioned_throughput is not ShapeBase.NOT_SET:
                _params['provisioned_throughput'] = provisioned_throughput
            if local_secondary_indexes is not ShapeBase.NOT_SET:
                _params['local_secondary_indexes'] = local_secondary_indexes
            if global_secondary_indexes is not ShapeBase.NOT_SET:
                _params['global_secondary_indexes'] = global_secondary_indexes
            if stream_specification is not ShapeBase.NOT_SET:
                _params['stream_specification'] = stream_specification
            if sse_specification is not ShapeBase.NOT_SET:
                _params['sse_specification'] = sse_specification
            _request = shapes.CreateTableInput(**_params)
        response = self._boto_client.create_table(**_request.to_boto())

        return shapes.CreateTableOutput.from_boto(response)

    def delete_backup(
        self,
        _request: shapes.DeleteBackupInput = None,
        *,
        backup_arn: str,
    ) -> shapes.DeleteBackupOutput:
        """
        Deletes an existing backup of a table.

        You can call `DeleteBackup` at a maximum rate of 10 times per second.
        """
        if _request is None:
            _params = {}
            if backup_arn is not ShapeBase.NOT_SET:
                _params['backup_arn'] = backup_arn
            _request = shapes.DeleteBackupInput(**_params)
        response = self._boto_client.delete_backup(**_request.to_boto())

        return shapes.DeleteBackupOutput.from_boto(response)

    def delete_item(
        self,
        _request: shapes.DeleteItemInput = None,
        *,
        table_name: str,
        key: typing.Dict[str, shapes.AttributeValue],
        expected: typing.Dict[str, shapes.
                              ExpectedAttributeValue] = ShapeBase.NOT_SET,
        conditional_operator: typing.
        Union[str, shapes.ConditionalOperator] = ShapeBase.NOT_SET,
        return_values: typing.Union[str, shapes.
                                    ReturnValue] = ShapeBase.NOT_SET,
        return_consumed_capacity: typing.
        Union[str, shapes.ReturnConsumedCapacity] = ShapeBase.NOT_SET,
        return_item_collection_metrics: typing.
        Union[str, shapes.ReturnItemCollectionMetrics] = ShapeBase.NOT_SET,
        condition_expression: str = ShapeBase.NOT_SET,
        expression_attribute_names: typing.Dict[str, str] = ShapeBase.NOT_SET,
        expression_attribute_values: typing.
        Dict[str, shapes.AttributeValue] = ShapeBase.NOT_SET,
    ) -> shapes.DeleteItemOutput:
        """
        Deletes a single item in a table by primary key. You can perform a conditional
        delete operation that deletes the item if it exists, or if it has an expected
        attribute value.

        In addition to deleting an item, you can also return the item's attribute values
        in the same operation, using the `ReturnValues` parameter.

        Unless you specify conditions, the `DeleteItem` is an idempotent operation;
        running it multiple times on the same item or attribute does _not_ result in an
        error response.

        Conditional deletes are useful for deleting items only if specific conditions
        are met. If those conditions are met, DynamoDB performs the delete. Otherwise,
        the item is not deleted.
        """
        if _request is None:
            _params = {}
            if table_name is not ShapeBase.NOT_SET:
                _params['table_name'] = table_name
            if key is not ShapeBase.NOT_SET:
                _params['key'] = key
            if expected is not ShapeBase.NOT_SET:
                _params['expected'] = expected
            if conditional_operator is not ShapeBase.NOT_SET:
                _params['conditional_operator'] = conditional_operator
            if return_values is not ShapeBase.NOT_SET:
                _params['return_values'] = return_values
            if return_consumed_capacity is not ShapeBase.NOT_SET:
                _params['return_consumed_capacity'] = return_consumed_capacity
            if return_item_collection_metrics is not ShapeBase.NOT_SET:
                _params['return_item_collection_metrics'
                       ] = return_item_collection_metrics
            if condition_expression is not ShapeBase.NOT_SET:
                _params['condition_expression'] = condition_expression
            if expression_attribute_names is not ShapeBase.NOT_SET:
                _params['expression_attribute_names'
                       ] = expression_attribute_names
            if expression_attribute_values is not ShapeBase.NOT_SET:
                _params['expression_attribute_values'
                       ] = expression_attribute_values
            _request = shapes.DeleteItemInput(**_params)
        response = self._boto_client.delete_item(**_request.to_boto())

        return shapes.DeleteItemOutput.from_boto(response)

    def delete_table(
        self,
        _request: shapes.DeleteTableInput = None,
        *,
        table_name: str,
    ) -> shapes.DeleteTableOutput:
        """
        The `DeleteTable` operation deletes a table and all of its items. After a
        `DeleteTable` request, the specified table is in the `DELETING` state until
        DynamoDB completes the deletion. If the table is in the `ACTIVE` state, you can
        delete it. If a table is in `CREATING` or `UPDATING` states, then DynamoDB
        returns a `ResourceInUseException`. If the specified table does not exist,
        DynamoDB returns a `ResourceNotFoundException`. If table is already in the
        `DELETING` state, no error is returned.

        DynamoDB might continue to accept data read and write operations, such as
        `GetItem` and `PutItem`, on a table in the `DELETING` state until the table
        deletion is complete.

        When you delete a table, any indexes on that table are also deleted.

        If you have DynamoDB Streams enabled on the table, then the corresponding stream
        on that table goes into the `DISABLED` state, and the stream is automatically
        deleted after 24 hours.

        Use the `DescribeTable` action to check the status of the table.
        """
        if _request is None:
            _params = {}
            if table_name is not ShapeBase.NOT_SET:
                _params['table_name'] = table_name
            _request = shapes.DeleteTableInput(**_params)
        response = self._boto_client.delete_table(**_request.to_boto())

        return shapes.DeleteTableOutput.from_boto(response)

    def describe_backup(
        self,
        _request: shapes.DescribeBackupInput = None,
        *,
        backup_arn: str,
    ) -> shapes.DescribeBackupOutput:
        """
        Describes an existing backup of a table.

        You can call `DescribeBackup` at a maximum rate of 10 times per second.
        """
        if _request is None:
            _params = {}
            if backup_arn is not ShapeBase.NOT_SET:
                _params['backup_arn'] = backup_arn
            _request = shapes.DescribeBackupInput(**_params)
        response = self._boto_client.describe_backup(**_request.to_boto())

        return shapes.DescribeBackupOutput.from_boto(response)

    def describe_continuous_backups(
        self,
        _request: shapes.DescribeContinuousBackupsInput = None,
        *,
        table_name: str,
    ) -> shapes.DescribeContinuousBackupsOutput:
        """
        Checks the status of continuous backups and point in time recovery on the
        specified table. Continuous backups are `ENABLED` on all tables at table
        creation. If point in time recovery is enabled, `PointInTimeRecoveryStatus` will
        be set to ENABLED.

        Once continuous backups and point in time recovery are enabled, you can restore
        to any point in time within `EarliestRestorableDateTime` and
        `LatestRestorableDateTime`.

        `LatestRestorableDateTime` is typically 5 minutes before the current time. You
        can restore your table to any point in time during the last 35 days.

        You can call `DescribeContinuousBackups` at a maximum rate of 10 times per
        second.
        """
        if _request is None:
            _params = {}
            if table_name is not ShapeBase.NOT_SET:
                _params['table_name'] = table_name
            _request = shapes.DescribeContinuousBackupsInput(**_params)
        response = self._boto_client.describe_continuous_backups(
            **_request.to_boto()
        )

        return shapes.DescribeContinuousBackupsOutput.from_boto(response)

    def describe_endpoints(
        self,
        _request: shapes.DescribeEndpointsRequest = None,
    ) -> shapes.DescribeEndpointsResponse:
        if _request is None:
            _params = {}
            _request = shapes.DescribeEndpointsRequest(**_params)
        response = self._boto_client.describe_endpoints(**_request.to_boto())

        return shapes.DescribeEndpointsResponse.from_boto(response)

    def describe_global_table(
        self,
        _request: shapes.DescribeGlobalTableInput = None,
        *,
        global_table_name: str,
    ) -> shapes.DescribeGlobalTableOutput:
        """
        Returns information about the specified global table.
        """
        if _request is None:
            _params = {}
            if global_table_name is not ShapeBase.NOT_SET:
                _params['global_table_name'] = global_table_name
            _request = shapes.DescribeGlobalTableInput(**_params)
        response = self._boto_client.describe_global_table(**_request.to_boto())

        return shapes.DescribeGlobalTableOutput.from_boto(response)

    def describe_global_table_settings(
        self,
        _request: shapes.DescribeGlobalTableSettingsInput = None,
        *,
        global_table_name: str,
    ) -> shapes.DescribeGlobalTableSettingsOutput:
        """
        Describes region specific settings for a global table.
        """
        if _request is None:
            _params = {}
            if global_table_name is not ShapeBase.NOT_SET:
                _params['global_table_name'] = global_table_name
            _request = shapes.DescribeGlobalTableSettingsInput(**_params)
        response = self._boto_client.describe_global_table_settings(
            **_request.to_boto()
        )

        return shapes.DescribeGlobalTableSettingsOutput.from_boto(response)

    def describe_limits(
        self,
        _request: shapes.DescribeLimitsInput = None,
    ) -> shapes.DescribeLimitsOutput:
        """
        Returns the current provisioned-capacity limits for your AWS account in a
        region, both for the region as a whole and for any one DynamoDB table that you
        create there.

        When you establish an AWS account, the account has initial limits on the maximum
        read capacity units and write capacity units that you can provision across all
        of your DynamoDB tables in a given region. Also, there are per-table limits that
        apply when you create a table there. For more information, see
        [Limits](http://docs.aws.amazon.com/amazondynamodb/latest/developerguide/Limits.html)
        page in the _Amazon DynamoDB Developer Guide_.

        Although you can increase these limits by filing a case at [AWS Support
        Center](https://console.aws.amazon.com/support/home#/), obtaining the increase
        is not instantaneous. The `DescribeLimits` action lets you write code to compare
        the capacity you are currently using to those limits imposed by your account so
        that you have enough time to apply for an increase before you hit a limit.

        For example, you could use one of the AWS SDKs to do the following:

          1. Call `DescribeLimits` for a particular region to obtain your current account limits on provisioned capacity there.

          2. Create a variable to hold the aggregate read capacity units provisioned for all your tables in that region, and one to hold the aggregate write capacity units. Zero them both.

          3. Call `ListTables` to obtain a list of all your DynamoDB tables.

          4. For each table name listed by `ListTables`, do the following:

            * Call `DescribeTable` with the table name.

            * Use the data returned by `DescribeTable` to add the read capacity units and write capacity units provisioned for the table itself to your variables.

            * If the table has one or more global secondary indexes (GSIs), loop over these GSIs and add their provisioned capacity values to your variables as well.

          5. Report the account limits for that region returned by `DescribeLimits`, along with the total current provisioned capacity levels you have calculated.

        This will let you see whether you are getting close to your account-level
        limits.

        The per-table limits apply only when you are creating a new table. They restrict
        the sum of the provisioned capacity of the new table itself and all its global
        secondary indexes.

        For existing tables and their GSIs, DynamoDB will not let you increase
        provisioned capacity extremely rapidly, but the only upper limit that applies is
        that the aggregate provisioned capacity over all your tables and GSIs cannot
        exceed either of the per-account limits.

        `DescribeLimits` should only be called periodically. You can expect throttling
        errors if you call it more than once in a minute.

        The `DescribeLimits` Request element has no content.
        """
        if _request is None:
            _params = {}
            _request = shapes.DescribeLimitsInput(**_params)
        response = self._boto_client.describe_limits(**_request.to_boto())

        return shapes.DescribeLimitsOutput.from_boto(response)

    def describe_table(
        self,
        _request: shapes.DescribeTableInput = None,
        *,
        table_name: str,
    ) -> shapes.DescribeTableOutput:
        """
        Returns information about the table, including the current status of the table,
        when it was created, the primary key schema, and any indexes on the table.

        If you issue a `DescribeTable` request immediately after a `CreateTable`
        request, DynamoDB might return a `ResourceNotFoundException`. This is because
        `DescribeTable` uses an eventually consistent query, and the metadata for your
        table might not be available at that moment. Wait for a few seconds, and then
        try the `DescribeTable` request again.
        """
        if _request is None:
            _params = {}
            if table_name is not ShapeBase.NOT_SET:
                _params['table_name'] = table_name
            _request = shapes.DescribeTableInput(**_params)
        response = self._boto_client.describe_table(**_request.to_boto())

        return shapes.DescribeTableOutput.from_boto(response)

    def describe_time_to_live(
        self,
        _request: shapes.DescribeTimeToLiveInput = None,
        *,
        table_name: str,
    ) -> shapes.DescribeTimeToLiveOutput:
        """
        Gives a description of the Time to Live (TTL) status on the specified table.
        """
        if _request is None:
            _params = {}
            if table_name is not ShapeBase.NOT_SET:
                _params['table_name'] = table_name
            _request = shapes.DescribeTimeToLiveInput(**_params)
        response = self._boto_client.describe_time_to_live(**_request.to_boto())

        return shapes.DescribeTimeToLiveOutput.from_boto(response)

    def get_item(
        self,
        _request: shapes.GetItemInput = None,
        *,
        table_name: str,
        key: typing.Dict[str, shapes.AttributeValue],
        attributes_to_get: typing.List[str] = ShapeBase.NOT_SET,
        consistent_read: bool = ShapeBase.NOT_SET,
        return_consumed_capacity: typing.
        Union[str, shapes.ReturnConsumedCapacity] = ShapeBase.NOT_SET,
        projection_expression: str = ShapeBase.NOT_SET,
        expression_attribute_names: typing.Dict[str, str] = ShapeBase.NOT_SET,
    ) -> shapes.GetItemOutput:
        """
        The `GetItem` operation returns a set of attributes for the item with the given
        primary key. If there is no matching item, `GetItem` does not return any data
        and there will be no `Item` element in the response.

        `GetItem` provides an eventually consistent read by default. If your application
        requires a strongly consistent read, set `ConsistentRead` to `true`. Although a
        strongly consistent read might take more time than an eventually consistent
        read, it always returns the last updated value.
        """
        if _request is None:
            _params = {}
            if table_name is not ShapeBase.NOT_SET:
                _params['table_name'] = table_name
            if key is not ShapeBase.NOT_SET:
                _params['key'] = key
            if attributes_to_get is not ShapeBase.NOT_SET:
                _params['attributes_to_get'] = attributes_to_get
            if consistent_read is not ShapeBase.NOT_SET:
                _params['consistent_read'] = consistent_read
            if return_consumed_capacity is not ShapeBase.NOT_SET:
                _params['return_consumed_capacity'] = return_consumed_capacity
            if projection_expression is not ShapeBase.NOT_SET:
                _params['projection_expression'] = projection_expression
            if expression_attribute_names is not ShapeBase.NOT_SET:
                _params['expression_attribute_names'
                       ] = expression_attribute_names
            _request = shapes.GetItemInput(**_params)
        response = self._boto_client.get_item(**_request.to_boto())

        return shapes.GetItemOutput.from_boto(response)

    def list_backups(
        self,
        _request: shapes.ListBackupsInput = None,
        *,
        table_name: str = ShapeBase.NOT_SET,
        limit: int = ShapeBase.NOT_SET,
        time_range_lower_bound: datetime.datetime = ShapeBase.NOT_SET,
        time_range_upper_bound: datetime.datetime = ShapeBase.NOT_SET,
        exclusive_start_backup_arn: str = ShapeBase.NOT_SET,
        backup_type: typing.Union[str, shapes.BackupTypeFilter] = ShapeBase.
        NOT_SET,
    ) -> shapes.ListBackupsOutput:
        """
        List backups associated with an AWS account. To list backups for a given table,
        specify `TableName`. `ListBackups` returns a paginated list of results with at
        most 1MB worth of items in a page. You can also specify a limit for the maximum
        number of entries to be returned in a page.

        In the request, start time is inclusive but end time is exclusive. Note that
        these limits are for the time at which the original backup was requested.

        You can call `ListBackups` a maximum of 5 times per second.
        """
        if _request is None:
            _params = {}
            if table_name is not ShapeBase.NOT_SET:
                _params['table_name'] = table_name
            if limit is not ShapeBase.NOT_SET:
                _params['limit'] = limit
            if time_range_lower_bound is not ShapeBase.NOT_SET:
                _params['time_range_lower_bound'] = time_range_lower_bound
            if time_range_upper_bound is not ShapeBase.NOT_SET:
                _params['time_range_upper_bound'] = time_range_upper_bound
            if exclusive_start_backup_arn is not ShapeBase.NOT_SET:
                _params['exclusive_start_backup_arn'
                       ] = exclusive_start_backup_arn
            if backup_type is not ShapeBase.NOT_SET:
                _params['backup_type'] = backup_type
            _request = shapes.ListBackupsInput(**_params)
        paginator = self.get_paginator("list_backups").paginate(
            **_request.to_boto()
        )
        page_generator = (page for page in paginator)
        first_page = next(page_generator)
        result = shapes.ListBackupsOutput.from_boto(first_page)
        result._page_iterator = page_generator
        return result

        return shapes.ListBackupsOutput.from_boto(response)

    def list_global_tables(
        self,
        _request: shapes.ListGlobalTablesInput = None,
        *,
        exclusive_start_global_table_name: str = ShapeBase.NOT_SET,
        limit: int = ShapeBase.NOT_SET,
        region_name: str = ShapeBase.NOT_SET,
    ) -> shapes.ListGlobalTablesOutput:
        """
        Lists all global tables that have a replica in the specified region.
        """
        if _request is None:
            _params = {}
            if exclusive_start_global_table_name is not ShapeBase.NOT_SET:
                _params['exclusive_start_global_table_name'
                       ] = exclusive_start_global_table_name
            if limit is not ShapeBase.NOT_SET:
                _params['limit'] = limit
            if region_name is not ShapeBase.NOT_SET:
                _params['region_name'] = region_name
            _request = shapes.ListGlobalTablesInput(**_params)
        response = self._boto_client.list_global_tables(**_request.to_boto())

        return shapes.ListGlobalTablesOutput.from_boto(response)

    def list_tables(
        self,
        _request: shapes.ListTablesInput = None,
        *,
        exclusive_start_table_name: str = ShapeBase.NOT_SET,
        limit: int = ShapeBase.NOT_SET,
    ) -> shapes.ListTablesOutput:
        """
        Returns an array of table names associated with the current account and
        endpoint. The output from `ListTables` is paginated, with each page returning a
        maximum of 100 table names.
        """
        if _request is None:
            _params = {}
            if exclusive_start_table_name is not ShapeBase.NOT_SET:
                _params['exclusive_start_table_name'
                       ] = exclusive_start_table_name
            if limit is not ShapeBase.NOT_SET:
                _params['limit'] = limit
            _request = shapes.ListTablesInput(**_params)
        paginator = self.get_paginator("list_tables").paginate(
            **_request.to_boto()
        )
        page_generator = (page for page in paginator)
        first_page = next(page_generator)
        result = shapes.ListTablesOutput.from_boto(first_page)
        result._page_iterator = page_generator
        return result

        return shapes.ListTablesOutput.from_boto(response)

    def list_tags_of_resource(
        self,
        _request: shapes.ListTagsOfResourceInput = None,
        *,
        resource_arn: str,
        next_token: str = ShapeBase.NOT_SET,
    ) -> shapes.ListTagsOfResourceOutput:
        """
        List all tags on an Amazon DynamoDB resource. You can call ListTagsOfResource up
        to 10 times per second, per account.

        For an overview on tagging DynamoDB resources, see [Tagging for
        DynamoDB](http://docs.aws.amazon.com/amazondynamodb/latest/developerguide/Tagging.html)
        in the _Amazon DynamoDB Developer Guide_.
        """
        if _request is None:
            _params = {}
            if resource_arn is not ShapeBase.NOT_SET:
                _params['resource_arn'] = resource_arn
            if next_token is not ShapeBase.NOT_SET:
                _params['next_token'] = next_token
            _request = shapes.ListTagsOfResourceInput(**_params)
        response = self._boto_client.list_tags_of_resource(**_request.to_boto())

        return shapes.ListTagsOfResourceOutput.from_boto(response)

    def put_item(
        self,
        _request: shapes.PutItemInput = None,
        *,
        table_name: str,
        item: typing.Dict[str, shapes.AttributeValue],
        expected: typing.Dict[str, shapes.
                              ExpectedAttributeValue] = ShapeBase.NOT_SET,
        return_values: typing.Union[str, shapes.
                                    ReturnValue] = ShapeBase.NOT_SET,
        return_consumed_capacity: typing.
        Union[str, shapes.ReturnConsumedCapacity] = ShapeBase.NOT_SET,
        return_item_collection_metrics: typing.
        Union[str, shapes.ReturnItemCollectionMetrics] = ShapeBase.NOT_SET,
        conditional_operator: typing.
        Union[str, shapes.ConditionalOperator] = ShapeBase.NOT_SET,
        condition_expression: str = ShapeBase.NOT_SET,
        expression_attribute_names: typing.Dict[str, str] = ShapeBase.NOT_SET,
        expression_attribute_values: typing.
        Dict[str, shapes.AttributeValue] = ShapeBase.NOT_SET,
    ) -> shapes.PutItemOutput:
        """
        Creates a new item, or replaces an old item with a new item. If an item that has
        the same primary key as the new item already exists in the specified table, the
        new item completely replaces the existing item. You can perform a conditional
        put operation (add a new item if one with the specified primary key doesn't
        exist), or replace an existing item if it has certain attribute values. You can
        return the item's attribute values in the same operation, using the
        `ReturnValues` parameter.

        This topic provides general information about the `PutItem` API.

        For information on how to call the `PutItem` API using the AWS SDK in specific
        languages, see the following:

          * [ PutItem in the AWS Command Line Interface ](http://docs.aws.amazon.com/goto/aws-cli/dynamodb-2012-08-10/PutItem)

          * [ PutItem in the AWS SDK for .NET ](http://docs.aws.amazon.com/goto/DotNetSDKV3/dynamodb-2012-08-10/PutItem)

          * [ PutItem in the AWS SDK for C++ ](http://docs.aws.amazon.com/goto/SdkForCpp/dynamodb-2012-08-10/PutItem)

          * [ PutItem in the AWS SDK for Go ](http://docs.aws.amazon.com/goto/SdkForGoV1/dynamodb-2012-08-10/PutItem)

          * [ PutItem in the AWS SDK for Java ](http://docs.aws.amazon.com/goto/SdkForJava/dynamodb-2012-08-10/PutItem)

          * [ PutItem in the AWS SDK for JavaScript ](http://docs.aws.amazon.com/goto/AWSJavaScriptSDK/dynamodb-2012-08-10/PutItem)

          * [ PutItem in the AWS SDK for PHP V3 ](http://docs.aws.amazon.com/goto/SdkForPHPV3/dynamodb-2012-08-10/PutItem)

          * [ PutItem in the AWS SDK for Python ](http://docs.aws.amazon.com/goto/boto3/dynamodb-2012-08-10/PutItem)

          * [ PutItem in the AWS SDK for Ruby V2 ](http://docs.aws.amazon.com/goto/SdkForRubyV2/dynamodb-2012-08-10/PutItem)

        When you add an item, the primary key attribute(s) are the only required
        attributes. Attribute values cannot be null. String and Binary type attributes
        must have lengths greater than zero. Set type attributes cannot be empty.
        Requests with empty values will be rejected with a `ValidationException`
        exception.

        To prevent a new item from replacing an existing item, use a conditional
        expression that contains the `attribute_not_exists` function with the name of
        the attribute being used as the partition key for the table. Since every record
        must contain that attribute, the `attribute_not_exists` function will only
        succeed if no matching item exists.

        For more information about `PutItem`, see [Working with
        Items](http://docs.aws.amazon.com/amazondynamodb/latest/developerguide/WorkingWithItems.html)
        in the _Amazon DynamoDB Developer Guide_.
        """
        if _request is None:
            _params = {}
            if table_name is not ShapeBase.NOT_SET:
                _params['table_name'] = table_name
            if item is not ShapeBase.NOT_SET:
                _params['item'] = item
            if expected is not ShapeBase.NOT_SET:
                _params['expected'] = expected
            if return_values is not ShapeBase.NOT_SET:
                _params['return_values'] = return_values
            if return_consumed_capacity is not ShapeBase.NOT_SET:
                _params['return_consumed_capacity'] = return_consumed_capacity
            if return_item_collection_metrics is not ShapeBase.NOT_SET:
                _params['return_item_collection_metrics'
                       ] = return_item_collection_metrics
            if conditional_operator is not ShapeBase.NOT_SET:
                _params['conditional_operator'] = conditional_operator
            if condition_expression is not ShapeBase.NOT_SET:
                _params['condition_expression'] = condition_expression
            if expression_attribute_names is not ShapeBase.NOT_SET:
                _params['expression_attribute_names'
                       ] = expression_attribute_names
            if expression_attribute_values is not ShapeBase.NOT_SET:
                _params['expression_attribute_values'
                       ] = expression_attribute_values
            _request = shapes.PutItemInput(**_params)
        response = self._boto_client.put_item(**_request.to_boto())

        return shapes.PutItemOutput.from_boto(response)

    def query(
        self,
        _request: shapes.QueryInput = None,
        *,
        table_name: str,
        index_name: str = ShapeBase.NOT_SET,
        select: typing.Union[str, shapes.Select] = ShapeBase.NOT_SET,
        attributes_to_get: typing.List[str] = ShapeBase.NOT_SET,
        limit: int = ShapeBase.NOT_SET,
        consistent_read: bool = ShapeBase.NOT_SET,
        key_conditions: typing.Dict[str, shapes.Condition] = ShapeBase.NOT_SET,
        query_filter: typing.Dict[str, shapes.Condition] = ShapeBase.NOT_SET,
        conditional_operator: typing.
        Union[str, shapes.ConditionalOperator] = ShapeBase.NOT_SET,
        scan_index_forward: bool = ShapeBase.NOT_SET,
        exclusive_start_key: typing.Dict[str, shapes.
                                         AttributeValue] = ShapeBase.NOT_SET,
        return_consumed_capacity: typing.
        Union[str, shapes.ReturnConsumedCapacity] = ShapeBase.NOT_SET,
        projection_expression: str = ShapeBase.NOT_SET,
        filter_expression: str = ShapeBase.NOT_SET,
        key_condition_expression: str = ShapeBase.NOT_SET,
        expression_attribute_names: typing.Dict[str, str] = ShapeBase.NOT_SET,
        expression_attribute_values: typing.
        Dict[str, shapes.AttributeValue] = ShapeBase.NOT_SET,
    ) -> shapes.QueryOutput:
        """
        The `Query` operation finds items based on primary key values. You can query any
        table or secondary index that has a composite primary key (a partition key and a
        sort key).

        Use the `KeyConditionExpression` parameter to provide a specific value for the
        partition key. The `Query` operation will return all of the items from the table
        or index with that partition key value. You can optionally narrow the scope of
        the `Query` operation by specifying a sort key value and a comparison operator
        in `KeyConditionExpression`. To further refine the `Query` results, you can
        optionally provide a `FilterExpression`. A `FilterExpression` determines which
        items within the results should be returned to you. All of the other results are
        discarded.

        A `Query` operation always returns a result set. If no matching items are found,
        the result set will be empty. Queries that do not return results consume the
        minimum number of read capacity units for that type of read operation.

        DynamoDB calculates the number of read capacity units consumed based on item
        size, not on the amount of data that is returned to an application. The number
        of capacity units consumed will be the same whether you request all of the
        attributes (the default behavior) or just some of them (using a projection
        expression). The number will also be the same whether or not you use a
        `FilterExpression`.

        `Query` results are always sorted by the sort key value. If the data type of the
        sort key is Number, the results are returned in numeric order; otherwise, the
        results are returned in order of UTF-8 bytes. By default, the sort order is
        ascending. To reverse the order, set the `ScanIndexForward` parameter to false.

        A single `Query` operation will read up to the maximum number of items set (if
        using the `Limit` parameter) or a maximum of 1 MB of data and then apply any
        filtering to the results using `FilterExpression`. If `LastEvaluatedKey` is
        present in the response, you will need to paginate the result set. For more
        information, see [Paginating the
        Results](http://docs.aws.amazon.com/amazondynamodb/latest/developerguide/Query.html#Query.Pagination)
        in the _Amazon DynamoDB Developer Guide_.

        `FilterExpression` is applied after a `Query` finishes, but before the results
        are returned. A `FilterExpression` cannot contain partition key or sort key
        attributes. You need to specify those attributes in the
        `KeyConditionExpression`.

        A `Query` operation can return an empty result set and a `LastEvaluatedKey` if
        all the items read for the page of results are filtered out.

        You can query a table, a local secondary index, or a global secondary index. For
        a query on a table or on a local secondary index, you can set the
        `ConsistentRead` parameter to `true` and obtain a strongly consistent result.
        Global secondary indexes support eventually consistent reads only, so do not
        specify `ConsistentRead` when querying a global secondary index.
        """
        if _request is None:
            _params = {}
            if table_name is not ShapeBase.NOT_SET:
                _params['table_name'] = table_name
            if index_name is not ShapeBase.NOT_SET:
                _params['index_name'] = index_name
            if select is not ShapeBase.NOT_SET:
                _params['select'] = select
            if attributes_to_get is not ShapeBase.NOT_SET:
                _params['attributes_to_get'] = attributes_to_get
            if limit is not ShapeBase.NOT_SET:
                _params['limit'] = limit
            if consistent_read is not ShapeBase.NOT_SET:
                _params['consistent_read'] = consistent_read
            if key_conditions is not ShapeBase.NOT_SET:
                _params['key_conditions'] = key_conditions
            if query_filter is not ShapeBase.NOT_SET:
                _params['query_filter'] = query_filter
            if conditional_operator is not ShapeBase.NOT_SET:
                _params['conditional_operator'] = conditional_operator
            if scan_index_forward is not ShapeBase.NOT_SET:
                _params['scan_index_forward'] = scan_index_forward
            if exclusive_start_key is not ShapeBase.NOT_SET:
                _params['exclusive_start_key'] = exclusive_start_key
            if return_consumed_capacity is not ShapeBase.NOT_SET:
                _params['return_consumed_capacity'] = return_consumed_capacity
            if projection_expression is not ShapeBase.NOT_SET:
                _params['projection_expression'] = projection_expression
            if filter_expression is not ShapeBase.NOT_SET:
                _params['filter_expression'] = filter_expression
            if key_condition_expression is not ShapeBase.NOT_SET:
                _params['key_condition_expression'] = key_condition_expression
            if expression_attribute_names is not ShapeBase.NOT_SET:
                _params['expression_attribute_names'
                       ] = expression_attribute_names
            if expression_attribute_values is not ShapeBase.NOT_SET:
                _params['expression_attribute_values'
                       ] = expression_attribute_values
            _request = shapes.QueryInput(**_params)
        paginator = self.get_paginator("query").paginate(**_request.to_boto())
        page_generator = (page for page in paginator)
        first_page = next(page_generator)
        result = shapes.QueryOutput.from_boto(first_page)
        result._page_iterator = page_generator
        return result

        return shapes.QueryOutput.from_boto(response)

    def restore_table_from_backup(
        self,
        _request: shapes.RestoreTableFromBackupInput = None,
        *,
        target_table_name: str,
        backup_arn: str,
    ) -> shapes.RestoreTableFromBackupOutput:
        """
        Creates a new table from an existing backup. Any number of users can execute up
        to 4 concurrent restores (any type of restore) in a given account.

        You can call `RestoreTableFromBackup` at a maximum rate of 10 times per second.

        You must manually set up the following on the restored table:

          * Auto scaling policies

          * IAM policies

          * Cloudwatch metrics and alarms

          * Tags

          * Stream settings

          * Time to Live (TTL) settings
        """
        if _request is None:
            _params = {}
            if target_table_name is not ShapeBase.NOT_SET:
                _params['target_table_name'] = target_table_name
            if backup_arn is not ShapeBase.NOT_SET:
                _params['backup_arn'] = backup_arn
            _request = shapes.RestoreTableFromBackupInput(**_params)
        response = self._boto_client.restore_table_from_backup(
            **_request.to_boto()
        )

        return shapes.RestoreTableFromBackupOutput.from_boto(response)

    def restore_table_to_point_in_time(
        self,
        _request: shapes.RestoreTableToPointInTimeInput = None,
        *,
        source_table_name: str,
        target_table_name: str,
        use_latest_restorable_time: bool = ShapeBase.NOT_SET,
        restore_date_time: datetime.datetime = ShapeBase.NOT_SET,
    ) -> shapes.RestoreTableToPointInTimeOutput:
        """
        Restores the specified table to the specified point in time within
        `EarliestRestorableDateTime` and `LatestRestorableDateTime`. You can restore
        your table to any point in time during the last 35 days. Any number of users can
        execute up to 4 concurrent restores (any type of restore) in a given account.

        When you restore using point in time recovery, DynamoDB restores your table data
        to the state based on the selected date and time (day:hour:minute:second) to a
        new table.

        Along with data, the following are also included on the new restored table using
        point in time recovery:

          * Global secondary indexes (GSIs)

          * Local secondary indexes (LSIs)

          * Provisioned read and write capacity

          * Encryption settings

        All these settings come from the current settings of the source table at the
        time of restore.

        You must manually set up the following on the restored table:

          * Auto scaling policies

          * IAM policies

          * Cloudwatch metrics and alarms

          * Tags

          * Stream settings

          * Time to Live (TTL) settings

          * Point in time recovery settings
        """
        if _request is None:
            _params = {}
            if source_table_name is not ShapeBase.NOT_SET:
                _params['source_table_name'] = source_table_name
            if target_table_name is not ShapeBase.NOT_SET:
                _params['target_table_name'] = target_table_name
            if use_latest_restorable_time is not ShapeBase.NOT_SET:
                _params['use_latest_restorable_time'
                       ] = use_latest_restorable_time
            if restore_date_time is not ShapeBase.NOT_SET:
                _params['restore_date_time'] = restore_date_time
            _request = shapes.RestoreTableToPointInTimeInput(**_params)
        response = self._boto_client.restore_table_to_point_in_time(
            **_request.to_boto()
        )

        return shapes.RestoreTableToPointInTimeOutput.from_boto(response)

    def scan(
        self,
        _request: shapes.ScanInput = None,
        *,
        table_name: str,
        index_name: str = ShapeBase.NOT_SET,
        attributes_to_get: typing.List[str] = ShapeBase.NOT_SET,
        limit: int = ShapeBase.NOT_SET,
        select: typing.Union[str, shapes.Select] = ShapeBase.NOT_SET,
        scan_filter: typing.Dict[str, shapes.Condition] = ShapeBase.NOT_SET,
        conditional_operator: typing.
        Union[str, shapes.ConditionalOperator] = ShapeBase.NOT_SET,
        exclusive_start_key: typing.Dict[str, shapes.
                                         AttributeValue] = ShapeBase.NOT_SET,
        return_consumed_capacity: typing.
        Union[str, shapes.ReturnConsumedCapacity] = ShapeBase.NOT_SET,
        total_segments: int = ShapeBase.NOT_SET,
        segment: int = ShapeBase.NOT_SET,
        projection_expression: str = ShapeBase.NOT_SET,
        filter_expression: str = ShapeBase.NOT_SET,
        expression_attribute_names: typing.Dict[str, str] = ShapeBase.NOT_SET,
        expression_attribute_values: typing.
        Dict[str, shapes.AttributeValue] = ShapeBase.NOT_SET,
        consistent_read: bool = ShapeBase.NOT_SET,
    ) -> shapes.ScanOutput:
        """
        The `Scan` operation returns one or more items and item attributes by accessing
        every item in a table or a secondary index. To have DynamoDB return fewer items,
        you can provide a `FilterExpression` operation.

        If the total number of scanned items exceeds the maximum data set size limit of
        1 MB, the scan stops and results are returned to the user as a
        `LastEvaluatedKey` value to continue the scan in a subsequent operation. The
        results also include the number of items exceeding the limit. A scan can result
        in no table data meeting the filter criteria.

        A single `Scan` operation will read up to the maximum number of items set (if
        using the `Limit` parameter) or a maximum of 1 MB of data and then apply any
        filtering to the results using `FilterExpression`. If `LastEvaluatedKey` is
        present in the response, you will need to paginate the result set. For more
        information, see [Paginating the
        Results](http://docs.aws.amazon.com/amazondynamodb/latest/developerguide/Scan.html#Scan.Pagination)
        in the _Amazon DynamoDB Developer Guide_.

        `Scan` operations proceed sequentially; however, for faster performance on a
        large table or secondary index, applications can request a parallel `Scan`
        operation by providing the `Segment` and `TotalSegments` parameters. For more
        information, see [Parallel
        Scan](http://docs.aws.amazon.com/amazondynamodb/latest/developerguide/Scan.html#Scan.ParallelScan)
        in the _Amazon DynamoDB Developer Guide_.

        `Scan` uses eventually consistent reads when accessing the data in a table;
        therefore, the result set might not include the changes to data in the table
        immediately before the operation began. If you need a consistent copy of the
        data, as of the time that the `Scan` begins, you can set the `ConsistentRead`
        parameter to `true`.
        """
        if _request is None:
            _params = {}
            if table_name is not ShapeBase.NOT_SET:
                _params['table_name'] = table_name
            if index_name is not ShapeBase.NOT_SET:
                _params['index_name'] = index_name
            if attributes_to_get is not ShapeBase.NOT_SET:
                _params['attributes_to_get'] = attributes_to_get
            if limit is not ShapeBase.NOT_SET:
                _params['limit'] = limit
            if select is not ShapeBase.NOT_SET:
                _params['select'] = select
            if scan_filter is not ShapeBase.NOT_SET:
                _params['scan_filter'] = scan_filter
            if conditional_operator is not ShapeBase.NOT_SET:
                _params['conditional_operator'] = conditional_operator
            if exclusive_start_key is not ShapeBase.NOT_SET:
                _params['exclusive_start_key'] = exclusive_start_key
            if return_consumed_capacity is not ShapeBase.NOT_SET:
                _params['return_consumed_capacity'] = return_consumed_capacity
            if total_segments is not ShapeBase.NOT_SET:
                _params['total_segments'] = total_segments
            if segment is not ShapeBase.NOT_SET:
                _params['segment'] = segment
            if projection_expression is not ShapeBase.NOT_SET:
                _params['projection_expression'] = projection_expression
            if filter_expression is not ShapeBase.NOT_SET:
                _params['filter_expression'] = filter_expression
            if expression_attribute_names is not ShapeBase.NOT_SET:
                _params['expression_attribute_names'
                       ] = expression_attribute_names
            if expression_attribute_values is not ShapeBase.NOT_SET:
                _params['expression_attribute_values'
                       ] = expression_attribute_values
            if consistent_read is not ShapeBase.NOT_SET:
                _params['consistent_read'] = consistent_read
            _request = shapes.ScanInput(**_params)
        paginator = self.get_paginator("scan").paginate(**_request.to_boto())
        page_generator = (page for page in paginator)
        first_page = next(page_generator)
        result = shapes.ScanOutput.from_boto(first_page)
        result._page_iterator = page_generator
        return result

        return shapes.ScanOutput.from_boto(response)

    def tag_resource(
        self,
        _request: shapes.TagResourceInput = None,
        *,
        resource_arn: str,
        tags: typing.List[shapes.Tag],
    ) -> None:
        """
        Associate a set of tags with an Amazon DynamoDB resource. You can then activate
        these user-defined tags so that they appear on the Billing and Cost Management
        console for cost allocation tracking. You can call TagResource up to 5 times per
        second, per account.

        For an overview on tagging DynamoDB resources, see [Tagging for
        DynamoDB](http://docs.aws.amazon.com/amazondynamodb/latest/developerguide/Tagging.html)
        in the _Amazon DynamoDB Developer Guide_.
        """
        if _request is None:
            _params = {}
            if resource_arn is not ShapeBase.NOT_SET:
                _params['resource_arn'] = resource_arn
            if tags is not ShapeBase.NOT_SET:
                _params['tags'] = tags
            _request = shapes.TagResourceInput(**_params)
        response = self._boto_client.tag_resource(**_request.to_boto())

    def untag_resource(
        self,
        _request: shapes.UntagResourceInput = None,
        *,
        resource_arn: str,
        tag_keys: typing.List[str],
    ) -> None:
        """
        Removes the association of tags from an Amazon DynamoDB resource. You can call
        UntagResource up to 5 times per second, per account.

        For an overview on tagging DynamoDB resources, see [Tagging for
        DynamoDB](http://docs.aws.amazon.com/amazondynamodb/latest/developerguide/Tagging.html)
        in the _Amazon DynamoDB Developer Guide_.
        """
        if _request is None:
            _params = {}
            if resource_arn is not ShapeBase.NOT_SET:
                _params['resource_arn'] = resource_arn
            if tag_keys is not ShapeBase.NOT_SET:
                _params['tag_keys'] = tag_keys
            _request = shapes.UntagResourceInput(**_params)
        response = self._boto_client.untag_resource(**_request.to_boto())

    def update_continuous_backups(
        self,
        _request: shapes.UpdateContinuousBackupsInput = None,
        *,
        table_name: str,
        point_in_time_recovery_specification: shapes.
        PointInTimeRecoverySpecification,
    ) -> shapes.UpdateContinuousBackupsOutput:
        """
        `UpdateContinuousBackups` enables or disables point in time recovery for the
        specified table. A successful `UpdateContinuousBackups` call returns the current
        `ContinuousBackupsDescription`. Continuous backups are `ENABLED` on all tables
        at table creation. If point in time recovery is enabled,
        `PointInTimeRecoveryStatus` will be set to ENABLED.

        Once continuous backups and point in time recovery are enabled, you can restore
        to any point in time within `EarliestRestorableDateTime` and
        `LatestRestorableDateTime`.

        `LatestRestorableDateTime` is typically 5 minutes before the current time. You
        can restore your table to any point in time during the last 35 days..
        """
        if _request is None:
            _params = {}
            if table_name is not ShapeBase.NOT_SET:
                _params['table_name'] = table_name
            if point_in_time_recovery_specification is not ShapeBase.NOT_SET:
                _params['point_in_time_recovery_specification'
                       ] = point_in_time_recovery_specification
            _request = shapes.UpdateContinuousBackupsInput(**_params)
        response = self._boto_client.update_continuous_backups(
            **_request.to_boto()
        )

        return shapes.UpdateContinuousBackupsOutput.from_boto(response)

    def update_global_table(
        self,
        _request: shapes.UpdateGlobalTableInput = None,
        *,
        global_table_name: str,
        replica_updates: typing.List[shapes.ReplicaUpdate],
    ) -> shapes.UpdateGlobalTableOutput:
        """
        Adds or removes replicas in the specified global table. The global table must
        already exist to be able to use this operation. Any replica to be added must be
        empty, must have the same name as the global table, must have the same key
        schema, and must have DynamoDB Streams enabled and must have same provisioned
        and maximum write capacity units.

        Although you can use `UpdateGlobalTable` to add replicas and remove replicas in
        a single request, for simplicity we recommend that you issue separate requests
        for adding or removing replicas.

        If global secondary indexes are specified, then the following conditions must
        also be met:

          * The global secondary indexes must have the same name. 

          * The global secondary indexes must have the same hash key and sort key (if present). 

          * The global secondary indexes must have the same provisioned and maximum write capacity units.
        """
        if _request is None:
            _params = {}
            if global_table_name is not ShapeBase.NOT_SET:
                _params['global_table_name'] = global_table_name
            if replica_updates is not ShapeBase.NOT_SET:
                _params['replica_updates'] = replica_updates
            _request = shapes.UpdateGlobalTableInput(**_params)
        response = self._boto_client.update_global_table(**_request.to_boto())

        return shapes.UpdateGlobalTableOutput.from_boto(response)

    def update_global_table_settings(
        self,
        _request: shapes.UpdateGlobalTableSettingsInput = None,
        *,
        global_table_name: str,
        global_table_provisioned_write_capacity_units: int = ShapeBase.NOT_SET,
        global_table_provisioned_write_capacity_auto_scaling_settings_update:
        shapes.AutoScalingSettingsUpdate = ShapeBase.NOT_SET,
        global_table_global_secondary_index_settings_update: typing.List[
            shapes.GlobalTableGlobalSecondaryIndexSettingsUpdate
        ] = ShapeBase.NOT_SET,
        replica_settings_update: typing.List[shapes.ReplicaSettingsUpdate
                                            ] = ShapeBase.NOT_SET,
    ) -> shapes.UpdateGlobalTableSettingsOutput:
        """
        Updates settings for a global table.
        """
        if _request is None:
            _params = {}
            if global_table_name is not ShapeBase.NOT_SET:
                _params['global_table_name'] = global_table_name
            if global_table_provisioned_write_capacity_units is not ShapeBase.NOT_SET:
                _params['global_table_provisioned_write_capacity_units'
                       ] = global_table_provisioned_write_capacity_units
            if global_table_provisioned_write_capacity_auto_scaling_settings_update is not ShapeBase.NOT_SET:
                _params[
                    'global_table_provisioned_write_capacity_auto_scaling_settings_update'
                ] = global_table_provisioned_write_capacity_auto_scaling_settings_update
            if global_table_global_secondary_index_settings_update is not ShapeBase.NOT_SET:
                _params['global_table_global_secondary_index_settings_update'
                       ] = global_table_global_secondary_index_settings_update
            if replica_settings_update is not ShapeBase.NOT_SET:
                _params['replica_settings_update'] = replica_settings_update
            _request = shapes.UpdateGlobalTableSettingsInput(**_params)
        response = self._boto_client.update_global_table_settings(
            **_request.to_boto()
        )

        return shapes.UpdateGlobalTableSettingsOutput.from_boto(response)

    def update_item(
        self,
        _request: shapes.UpdateItemInput = None,
        *,
        table_name: str,
        key: typing.Dict[str, shapes.AttributeValue],
        attribute_updates: typing.
        Dict[str, shapes.AttributeValueUpdate] = ShapeBase.NOT_SET,
        expected: typing.Dict[str, shapes.
                              ExpectedAttributeValue] = ShapeBase.NOT_SET,
        conditional_operator: typing.
        Union[str, shapes.ConditionalOperator] = ShapeBase.NOT_SET,
        return_values: typing.Union[str, shapes.
                                    ReturnValue] = ShapeBase.NOT_SET,
        return_consumed_capacity: typing.
        Union[str, shapes.ReturnConsumedCapacity] = ShapeBase.NOT_SET,
        return_item_collection_metrics: typing.
        Union[str, shapes.ReturnItemCollectionMetrics] = ShapeBase.NOT_SET,
        update_expression: str = ShapeBase.NOT_SET,
        condition_expression: str = ShapeBase.NOT_SET,
        expression_attribute_names: typing.Dict[str, str] = ShapeBase.NOT_SET,
        expression_attribute_values: typing.
        Dict[str, shapes.AttributeValue] = ShapeBase.NOT_SET,
    ) -> shapes.UpdateItemOutput:
        """
        Edits an existing item's attributes, or adds a new item to the table if it does
        not already exist. You can put, delete, or add attribute values. You can also
        perform a conditional update on an existing item (insert a new attribute name-
        value pair if it doesn't exist, or replace an existing name-value pair if it has
        certain expected attribute values).

        You can also return the item's attribute values in the same `UpdateItem`
        operation using the `ReturnValues` parameter.
        """
        if _request is None:
            _params = {}
            if table_name is not ShapeBase.NOT_SET:
                _params['table_name'] = table_name
            if key is not ShapeBase.NOT_SET:
                _params['key'] = key
            if attribute_updates is not ShapeBase.NOT_SET:
                _params['attribute_updates'] = attribute_updates
            if expected is not ShapeBase.NOT_SET:
                _params['expected'] = expected
            if conditional_operator is not ShapeBase.NOT_SET:
                _params['conditional_operator'] = conditional_operator
            if return_values is not ShapeBase.NOT_SET:
                _params['return_values'] = return_values
            if return_consumed_capacity is not ShapeBase.NOT_SET:
                _params['return_consumed_capacity'] = return_consumed_capacity
            if return_item_collection_metrics is not ShapeBase.NOT_SET:
                _params['return_item_collection_metrics'
                       ] = return_item_collection_metrics
            if update_expression is not ShapeBase.NOT_SET:
                _params['update_expression'] = update_expression
            if condition_expression is not ShapeBase.NOT_SET:
                _params['condition_expression'] = condition_expression
            if expression_attribute_names is not ShapeBase.NOT_SET:
                _params['expression_attribute_names'
                       ] = expression_attribute_names
            if expression_attribute_values is not ShapeBase.NOT_SET:
                _params['expression_attribute_values'
                       ] = expression_attribute_values
            _request = shapes.UpdateItemInput(**_params)
        response = self._boto_client.update_item(**_request.to_boto())

        return shapes.UpdateItemOutput.from_boto(response)

    def update_table(
        self,
        _request: shapes.UpdateTableInput = None,
        *,
        table_name: str,
        attribute_definitions: typing.List[shapes.AttributeDefinition
                                          ] = ShapeBase.NOT_SET,
        provisioned_throughput: shapes.ProvisionedThroughput = ShapeBase.
        NOT_SET,
        global_secondary_index_updates: typing.List[
            shapes.GlobalSecondaryIndexUpdate] = ShapeBase.NOT_SET,
        stream_specification: shapes.StreamSpecification = ShapeBase.NOT_SET,
        sse_specification: shapes.SSESpecification = ShapeBase.NOT_SET,
    ) -> shapes.UpdateTableOutput:
        """
        Modifies the provisioned throughput settings, global secondary indexes, or
        DynamoDB Streams settings for a given table.

        You can only perform one of the following operations at once:

          * Modify the provisioned throughput settings of the table.

          * Enable or disable Streams on the table.

          * Remove a global secondary index from the table.

          * Create a new global secondary index on the table. Once the index begins backfilling, you can use `UpdateTable` to perform other operations.

        `UpdateTable` is an asynchronous operation; while it is executing, the table
        status changes from `ACTIVE` to `UPDATING`. While it is `UPDATING`, you cannot
        issue another `UpdateTable` request. When the table returns to the `ACTIVE`
        state, the `UpdateTable` operation is complete.
        """
        if _request is None:
            _params = {}
            if table_name is not ShapeBase.NOT_SET:
                _params['table_name'] = table_name
            if attribute_definitions is not ShapeBase.NOT_SET:
                _params['attribute_definitions'] = attribute_definitions
            if provisioned_throughput is not ShapeBase.NOT_SET:
                _params['provisioned_throughput'] = provisioned_throughput
            if global_secondary_index_updates is not ShapeBase.NOT_SET:
                _params['global_secondary_index_updates'
                       ] = global_secondary_index_updates
            if stream_specification is not ShapeBase.NOT_SET:
                _params['stream_specification'] = stream_specification
            if sse_specification is not ShapeBase.NOT_SET:
                _params['sse_specification'] = sse_specification
            _request = shapes.UpdateTableInput(**_params)
        response = self._boto_client.update_table(**_request.to_boto())

        return shapes.UpdateTableOutput.from_boto(response)

    def update_time_to_live(
        self,
        _request: shapes.UpdateTimeToLiveInput = None,
        *,
        table_name: str,
        time_to_live_specification: shapes.TimeToLiveSpecification,
    ) -> shapes.UpdateTimeToLiveOutput:
        """
        The UpdateTimeToLive method will enable or disable TTL for the specified table.
        A successful `UpdateTimeToLive` call returns the current
        `TimeToLiveSpecification`; it may take up to one hour for the change to fully
        process. Any additional `UpdateTimeToLive` calls for the same table during this
        one hour duration result in a `ValidationException`.

        TTL compares the current time in epoch time format to the time stored in the TTL
        attribute of an item. If the epoch time value stored in the attribute is less
        than the current time, the item is marked as expired and subsequently deleted.

        The epoch time format is the number of seconds elapsed since 12:00:00 AM January
        1st, 1970 UTC.

        DynamoDB deletes expired items on a best-effort basis to ensure availability of
        throughput for other data operations.

        DynamoDB typically deletes expired items within two days of expiration. The
        exact duration within which an item gets deleted after expiration is specific to
        the nature of the workload. Items that have expired and not been deleted will
        still show up in reads, queries, and scans.

        As items are deleted, they are removed from any Local Secondary Index and Global
        Secondary Index immediately in the same eventually consistent way as a standard
        delete operation.

        For more information, see [Time To
        Live](http://docs.aws.amazon.com/amazondynamodb/latest/developerguide/TTL.html)
        in the Amazon DynamoDB Developer Guide.
        """
        if _request is None:
            _params = {}
            if table_name is not ShapeBase.NOT_SET:
                _params['table_name'] = table_name
            if time_to_live_specification is not ShapeBase.NOT_SET:
                _params['time_to_live_specification'
                       ] = time_to_live_specification
            _request = shapes.UpdateTimeToLiveInput(**_params)
        response = self._boto_client.update_time_to_live(**_request.to_boto())

        return shapes.UpdateTimeToLiveOutput.from_boto(response)
