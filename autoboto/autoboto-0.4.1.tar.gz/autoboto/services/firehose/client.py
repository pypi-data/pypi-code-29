import datetime
import typing
import boto3
from autoboto import ClientBase, ShapeBase, OutputShapeBase
from . import shapes


class Client(ClientBase):
    def __init__(self, *args, **kwargs):
        super().__init__("firehose", *args, **kwargs)

    def create_delivery_stream(
        self,
        _request: shapes.CreateDeliveryStreamInput = None,
        *,
        delivery_stream_name: str,
        delivery_stream_type: typing.
        Union[str, shapes.DeliveryStreamType] = ShapeBase.NOT_SET,
        kinesis_stream_source_configuration: shapes.
        KinesisStreamSourceConfiguration = ShapeBase.NOT_SET,
        s3_destination_configuration: shapes.
        S3DestinationConfiguration = ShapeBase.NOT_SET,
        extended_s3_destination_configuration: shapes.
        ExtendedS3DestinationConfiguration = ShapeBase.NOT_SET,
        redshift_destination_configuration: shapes.
        RedshiftDestinationConfiguration = ShapeBase.NOT_SET,
        elasticsearch_destination_configuration: shapes.
        ElasticsearchDestinationConfiguration = ShapeBase.NOT_SET,
        splunk_destination_configuration: shapes.
        SplunkDestinationConfiguration = ShapeBase.NOT_SET,
    ) -> shapes.CreateDeliveryStreamOutput:
        """
        Creates a Kinesis Data Firehose delivery stream.

        By default, you can create up to 50 delivery streams per AWS Region.

        This is an asynchronous operation that immediately returns. The initial status
        of the delivery stream is `CREATING`. After the delivery stream is created, its
        status is `ACTIVE` and it now accepts data. Attempts to send data to a delivery
        stream that is not in the `ACTIVE` state cause an exception. To check the state
        of a delivery stream, use DescribeDeliveryStream.

        A Kinesis Data Firehose delivery stream can be configured to receive records
        directly from providers using PutRecord or PutRecordBatch, or it can be
        configured to use an existing Kinesis stream as its source. To specify a Kinesis
        data stream as input, set the `DeliveryStreamType` parameter to
        `KinesisStreamAsSource`, and provide the Kinesis stream Amazon Resource Name
        (ARN) and role ARN in the `KinesisStreamSourceConfiguration` parameter.

        A delivery stream is configured with a single destination: Amazon S3, Amazon ES,
        Amazon Redshift, or Splunk. You must specify only one of the following
        destination configuration parameters: **ExtendedS3DestinationConfiguration** ,
        **S3DestinationConfiguration** , **ElasticsearchDestinationConfiguration** ,
        **RedshiftDestinationConfiguration** , or **SplunkDestinationConfiguration**.

        When you specify **S3DestinationConfiguration** , you can also provide the
        following optional values: **BufferingHints** , **EncryptionConfiguration** ,
        and **CompressionFormat**. By default, if no **BufferingHints** value is
        provided, Kinesis Data Firehose buffers data up to 5 MB or for 5 minutes,
        whichever condition is satisfied first. **BufferingHints** is a hint, so there
        are some cases where the service cannot adhere to these conditions strictly. For
        example, record boundaries might be such that the size is a little over or under
        the configured buffering size. By default, no encryption is performed. We
        strongly recommend that you enable encryption to ensure secure data storage in
        Amazon S3.

        A few notes about Amazon Redshift as a destination:

          * An Amazon Redshift destination requires an S3 bucket as intermediate location. Kinesis Data Firehose first delivers data to Amazon S3 and then uses `COPY` syntax to load data into an Amazon Redshift table. This is specified in the **RedshiftDestinationConfiguration.S3Configuration** parameter.

          * The compression formats `SNAPPY` or `ZIP` cannot be specified in `RedshiftDestinationConfiguration.S3Configuration` because the Amazon Redshift `COPY` operation that reads from the S3 bucket doesn't support these compression formats.

          * We strongly recommend that you use the user name and password you provide exclusively with Kinesis Data Firehose, and that the permissions for the account are restricted for Amazon Redshift `INSERT` permissions.

        Kinesis Data Firehose assumes the IAM role that is configured as part of the
        destination. The role should allow the Kinesis Data Firehose principal to assume
        the role, and the role should have permissions that allow the service to deliver
        the data. For more information, see [Grant Kinesis Data Firehose Access to an
        Amazon S3
        Destination](http://docs.aws.amazon.com/firehose/latest/dev/controlling-
        access.html#using-iam-s3) in the _Amazon Kinesis Data Firehose Developer Guide_.
        """
        if _request is None:
            _params = {}
            if delivery_stream_name is not ShapeBase.NOT_SET:
                _params['delivery_stream_name'] = delivery_stream_name
            if delivery_stream_type is not ShapeBase.NOT_SET:
                _params['delivery_stream_type'] = delivery_stream_type
            if kinesis_stream_source_configuration is not ShapeBase.NOT_SET:
                _params['kinesis_stream_source_configuration'
                       ] = kinesis_stream_source_configuration
            if s3_destination_configuration is not ShapeBase.NOT_SET:
                _params['s3_destination_configuration'
                       ] = s3_destination_configuration
            if extended_s3_destination_configuration is not ShapeBase.NOT_SET:
                _params['extended_s3_destination_configuration'
                       ] = extended_s3_destination_configuration
            if redshift_destination_configuration is not ShapeBase.NOT_SET:
                _params['redshift_destination_configuration'
                       ] = redshift_destination_configuration
            if elasticsearch_destination_configuration is not ShapeBase.NOT_SET:
                _params['elasticsearch_destination_configuration'
                       ] = elasticsearch_destination_configuration
            if splunk_destination_configuration is not ShapeBase.NOT_SET:
                _params['splunk_destination_configuration'
                       ] = splunk_destination_configuration
            _request = shapes.CreateDeliveryStreamInput(**_params)
        response = self._boto_client.create_delivery_stream(
            **_request.to_boto()
        )

        return shapes.CreateDeliveryStreamOutput.from_boto(response)

    def delete_delivery_stream(
        self,
        _request: shapes.DeleteDeliveryStreamInput = None,
        *,
        delivery_stream_name: str,
    ) -> shapes.DeleteDeliveryStreamOutput:
        """
        Deletes a delivery stream and its data.

        You can delete a delivery stream only if it is in `ACTIVE` or `DELETING` state,
        and not in the `CREATING` state. While the deletion request is in process, the
        delivery stream is in the `DELETING` state.

        To check the state of a delivery stream, use DescribeDeliveryStream.

        While the delivery stream is `DELETING` state, the service might continue to
        accept the records, but it doesn't make any guarantees with respect to
        delivering the data. Therefore, as a best practice, you should first stop any
        applications that are sending records before deleting a delivery stream.
        """
        if _request is None:
            _params = {}
            if delivery_stream_name is not ShapeBase.NOT_SET:
                _params['delivery_stream_name'] = delivery_stream_name
            _request = shapes.DeleteDeliveryStreamInput(**_params)
        response = self._boto_client.delete_delivery_stream(
            **_request.to_boto()
        )

        return shapes.DeleteDeliveryStreamOutput.from_boto(response)

    def describe_delivery_stream(
        self,
        _request: shapes.DescribeDeliveryStreamInput = None,
        *,
        delivery_stream_name: str,
        limit: int = ShapeBase.NOT_SET,
        exclusive_start_destination_id: str = ShapeBase.NOT_SET,
    ) -> shapes.DescribeDeliveryStreamOutput:
        """
        Describes the specified delivery stream and gets the status. For example, after
        your delivery stream is created, call `DescribeDeliveryStream` to see whether
        the delivery stream is `ACTIVE` and therefore ready for data to be sent to it.
        """
        if _request is None:
            _params = {}
            if delivery_stream_name is not ShapeBase.NOT_SET:
                _params['delivery_stream_name'] = delivery_stream_name
            if limit is not ShapeBase.NOT_SET:
                _params['limit'] = limit
            if exclusive_start_destination_id is not ShapeBase.NOT_SET:
                _params['exclusive_start_destination_id'
                       ] = exclusive_start_destination_id
            _request = shapes.DescribeDeliveryStreamInput(**_params)
        response = self._boto_client.describe_delivery_stream(
            **_request.to_boto()
        )

        return shapes.DescribeDeliveryStreamOutput.from_boto(response)

    def list_delivery_streams(
        self,
        _request: shapes.ListDeliveryStreamsInput = None,
        *,
        limit: int = ShapeBase.NOT_SET,
        delivery_stream_type: typing.
        Union[str, shapes.DeliveryStreamType] = ShapeBase.NOT_SET,
        exclusive_start_delivery_stream_name: str = ShapeBase.NOT_SET,
    ) -> shapes.ListDeliveryStreamsOutput:
        """
        Lists your delivery streams.

        The number of delivery streams might be too large to return using a single call
        to `ListDeliveryStreams`. You can limit the number of delivery streams returned,
        using the **Limit** parameter. To determine whether there are more delivery
        streams to list, check the value of `HasMoreDeliveryStreams` in the output. If
        there are more delivery streams to list, you can request them by specifying the
        name of the last delivery stream returned in the call in the
        `ExclusiveStartDeliveryStreamName` parameter of a subsequent call.
        """
        if _request is None:
            _params = {}
            if limit is not ShapeBase.NOT_SET:
                _params['limit'] = limit
            if delivery_stream_type is not ShapeBase.NOT_SET:
                _params['delivery_stream_type'] = delivery_stream_type
            if exclusive_start_delivery_stream_name is not ShapeBase.NOT_SET:
                _params['exclusive_start_delivery_stream_name'
                       ] = exclusive_start_delivery_stream_name
            _request = shapes.ListDeliveryStreamsInput(**_params)
        response = self._boto_client.list_delivery_streams(**_request.to_boto())

        return shapes.ListDeliveryStreamsOutput.from_boto(response)

    def list_tags_for_delivery_stream(
        self,
        _request: shapes.ListTagsForDeliveryStreamInput = None,
        *,
        delivery_stream_name: str,
        exclusive_start_tag_key: str = ShapeBase.NOT_SET,
        limit: int = ShapeBase.NOT_SET,
    ) -> shapes.ListTagsForDeliveryStreamOutput:
        """
        Lists the tags for the specified delivery stream. This operation has a limit of
        five transactions per second per account.
        """
        if _request is None:
            _params = {}
            if delivery_stream_name is not ShapeBase.NOT_SET:
                _params['delivery_stream_name'] = delivery_stream_name
            if exclusive_start_tag_key is not ShapeBase.NOT_SET:
                _params['exclusive_start_tag_key'] = exclusive_start_tag_key
            if limit is not ShapeBase.NOT_SET:
                _params['limit'] = limit
            _request = shapes.ListTagsForDeliveryStreamInput(**_params)
        response = self._boto_client.list_tags_for_delivery_stream(
            **_request.to_boto()
        )

        return shapes.ListTagsForDeliveryStreamOutput.from_boto(response)

    def put_record(
        self,
        _request: shapes.PutRecordInput = None,
        *,
        delivery_stream_name: str,
        record: shapes.Record,
    ) -> shapes.PutRecordOutput:
        """
        Writes a single data record into an Amazon Kinesis Data Firehose delivery
        stream. To write multiple data records into a delivery stream, use
        PutRecordBatch. Applications using these operations are referred to as
        producers.

        By default, each delivery stream can take in up to 2,000 transactions per
        second, 5,000 records per second, or 5 MB per second. If you use PutRecord and
        PutRecordBatch, the limits are an aggregate across these two operations for each
        delivery stream. For more information about limits and how to request an
        increase, see [Amazon Kinesis Data Firehose
        Limits](http://docs.aws.amazon.com/firehose/latest/dev/limits.html).

        You must specify the name of the delivery stream and the data record when using
        PutRecord. The data record consists of a data blob that can be up to 1,000 KB in
        size, and any kind of data. For example, it can be a segment from a log file,
        geographic location data, website clickstream data, and so on.

        Kinesis Data Firehose buffers records before delivering them to the destination.
        To disambiguate the data blobs at the destination, a common solution is to use
        delimiters in the data, such as a newline (`\n`) or some other character unique
        within the data. This allows the consumer application to parse individual data
        items when reading the data from the destination.

        The `PutRecord` operation returns a `RecordId`, which is a unique string
        assigned to each record. Producer applications can use this ID for purposes such
        as auditability and investigation.

        If the `PutRecord` operation throws a `ServiceUnavailableException`, back off
        and retry. If the exception persists, it is possible that the throughput limits
        have been exceeded for the delivery stream.

        Data records sent to Kinesis Data Firehose are stored for 24 hours from the time
        they are added to a delivery stream as it tries to send the records to the
        destination. If the destination is unreachable for more than 24 hours, the data
        is no longer available.
        """
        if _request is None:
            _params = {}
            if delivery_stream_name is not ShapeBase.NOT_SET:
                _params['delivery_stream_name'] = delivery_stream_name
            if record is not ShapeBase.NOT_SET:
                _params['record'] = record
            _request = shapes.PutRecordInput(**_params)
        response = self._boto_client.put_record(**_request.to_boto())

        return shapes.PutRecordOutput.from_boto(response)

    def put_record_batch(
        self,
        _request: shapes.PutRecordBatchInput = None,
        *,
        delivery_stream_name: str,
        records: typing.List[shapes.Record],
    ) -> shapes.PutRecordBatchOutput:
        """
        Writes multiple data records into a delivery stream in a single call, which can
        achieve higher throughput per producer than when writing single records. To
        write single data records into a delivery stream, use PutRecord. Applications
        using these operations are referred to as producers.

        By default, each delivery stream can take in up to 2,000 transactions per
        second, 5,000 records per second, or 5 MB per second. If you use PutRecord and
        PutRecordBatch, the limits are an aggregate across these two operations for each
        delivery stream. For more information about limits, see [Amazon Kinesis Data
        Firehose Limits](http://docs.aws.amazon.com/firehose/latest/dev/limits.html).

        Each PutRecordBatch request supports up to 500 records. Each record in the
        request can be as large as 1,000 KB (before 64-bit encoding), up to a limit of 4
        MB for the entire request. These limits cannot be changed.

        You must specify the name of the delivery stream and the data record when using
        PutRecord. The data record consists of a data blob that can be up to 1,000 KB in
        size, and any kind of data. For example, it could be a segment from a log file,
        geographic location data, website clickstream data, and so on.

        Kinesis Data Firehose buffers records before delivering them to the destination.
        To disambiguate the data blobs at the destination, a common solution is to use
        delimiters in the data, such as a newline (`\n`) or some other character unique
        within the data. This allows the consumer application to parse individual data
        items when reading the data from the destination.

        The PutRecordBatch response includes a count of failed records,
        **FailedPutCount** , and an array of responses, **RequestResponses**. Each entry
        in the **RequestResponses** array provides additional information about the
        processed record. It directly correlates with a record in the request array
        using the same ordering, from the top to the bottom. The response array always
        includes the same number of records as the request array. **RequestResponses**
        includes both successfully and unsuccessfully processed records. Kinesis Data
        Firehose tries to process all records in each PutRecordBatch request. A single
        record failure does not stop the processing of subsequent records.

        A successfully processed record includes a **RecordId** value, which is unique
        for the record. An unsuccessfully processed record includes **ErrorCode** and
        **ErrorMessage** values. **ErrorCode** reflects the type of error, and is one of
        the following values: `ServiceUnavailable` or `InternalFailure`.
        **ErrorMessage** provides more detailed information about the error.

        If there is an internal server error or a timeout, the write might have
        completed or it might have failed. If **FailedPutCount** is greater than 0,
        retry the request, resending only those records that might have failed
        processing. This minimizes the possible duplicate records and also reduces the
        total bytes sent (and corresponding charges). We recommend that you handle any
        duplicates at the destination.

        If PutRecordBatch throws **ServiceUnavailableException** , back off and retry.
        If the exception persists, it is possible that the throughput limits have been
        exceeded for the delivery stream.

        Data records sent to Kinesis Data Firehose are stored for 24 hours from the time
        they are added to a delivery stream as it attempts to send the records to the
        destination. If the destination is unreachable for more than 24 hours, the data
        is no longer available.
        """
        if _request is None:
            _params = {}
            if delivery_stream_name is not ShapeBase.NOT_SET:
                _params['delivery_stream_name'] = delivery_stream_name
            if records is not ShapeBase.NOT_SET:
                _params['records'] = records
            _request = shapes.PutRecordBatchInput(**_params)
        response = self._boto_client.put_record_batch(**_request.to_boto())

        return shapes.PutRecordBatchOutput.from_boto(response)

    def tag_delivery_stream(
        self,
        _request: shapes.TagDeliveryStreamInput = None,
        *,
        delivery_stream_name: str,
        tags: typing.List[shapes.Tag],
    ) -> shapes.TagDeliveryStreamOutput:
        """
        Adds or updates tags for the specified delivery stream. A tag is a key-value
        pair (the value is optional) that you can define and assign to AWS resources. If
        you specify a tag that already exists, the tag value is replaced with the value
        that you specify in the request. Tags are metadata. For example, you can add
        friendly names and descriptions or other types of information that can help you
        distinguish the delivery stream. For more information about tags, see [Using
        Cost Allocation
        Tags](https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/cost-alloc-
        tags.html) in the _AWS Billing and Cost Management User Guide_.

        Each delivery stream can have up to 50 tags.

        This operation has a limit of five transactions per second per account.
        """
        if _request is None:
            _params = {}
            if delivery_stream_name is not ShapeBase.NOT_SET:
                _params['delivery_stream_name'] = delivery_stream_name
            if tags is not ShapeBase.NOT_SET:
                _params['tags'] = tags
            _request = shapes.TagDeliveryStreamInput(**_params)
        response = self._boto_client.tag_delivery_stream(**_request.to_boto())

        return shapes.TagDeliveryStreamOutput.from_boto(response)

    def untag_delivery_stream(
        self,
        _request: shapes.UntagDeliveryStreamInput = None,
        *,
        delivery_stream_name: str,
        tag_keys: typing.List[str],
    ) -> shapes.UntagDeliveryStreamOutput:
        """
        Removes tags from the specified delivery stream. Removed tags are deleted, and
        you can't recover them after this operation successfully completes.

        If you specify a tag that doesn't exist, the operation ignores it.

        This operation has a limit of five transactions per second per account.
        """
        if _request is None:
            _params = {}
            if delivery_stream_name is not ShapeBase.NOT_SET:
                _params['delivery_stream_name'] = delivery_stream_name
            if tag_keys is not ShapeBase.NOT_SET:
                _params['tag_keys'] = tag_keys
            _request = shapes.UntagDeliveryStreamInput(**_params)
        response = self._boto_client.untag_delivery_stream(**_request.to_boto())

        return shapes.UntagDeliveryStreamOutput.from_boto(response)

    def update_destination(
        self,
        _request: shapes.UpdateDestinationInput = None,
        *,
        delivery_stream_name: str,
        current_delivery_stream_version_id: str,
        destination_id: str,
        s3_destination_update: shapes.S3DestinationUpdate = ShapeBase.NOT_SET,
        extended_s3_destination_update: shapes.
        ExtendedS3DestinationUpdate = ShapeBase.NOT_SET,
        redshift_destination_update: shapes.
        RedshiftDestinationUpdate = ShapeBase.NOT_SET,
        elasticsearch_destination_update: shapes.
        ElasticsearchDestinationUpdate = ShapeBase.NOT_SET,
        splunk_destination_update: shapes.SplunkDestinationUpdate = ShapeBase.
        NOT_SET,
    ) -> shapes.UpdateDestinationOutput:
        """
        Updates the specified destination of the specified delivery stream.

        Use this operation to change the destination type (for example, to replace the
        Amazon S3 destination with Amazon Redshift) or change the parameters associated
        with a destination (for example, to change the bucket name of the Amazon S3
        destination). The update might not occur immediately. The target delivery stream
        remains active while the configurations are updated, so data writes to the
        delivery stream can continue during this process. The updated configurations are
        usually effective within a few minutes.

        Switching between Amazon ES and other services is not supported. For an Amazon
        ES destination, you can only update to another Amazon ES destination.

        If the destination type is the same, Kinesis Data Firehose merges the
        configuration parameters specified with the destination configuration that
        already exists on the delivery stream. If any of the parameters are not
        specified in the call, the existing values are retained. For example, in the
        Amazon S3 destination, if EncryptionConfiguration is not specified, then the
        existing `EncryptionConfiguration` is maintained on the destination.

        If the destination type is not the same, for example, changing the destination
        from Amazon S3 to Amazon Redshift, Kinesis Data Firehose does not merge any
        parameters. In this case, all parameters must be specified.

        Kinesis Data Firehose uses **CurrentDeliveryStreamVersionId** to avoid race
        conditions and conflicting merges. This is a required field, and the service
        updates the configuration only if the existing configuration has a version ID
        that matches. After the update is applied successfully, the version ID is
        updated, and can be retrieved using DescribeDeliveryStream. Use the new version
        ID to set **CurrentDeliveryStreamVersionId** in the next call.
        """
        if _request is None:
            _params = {}
            if delivery_stream_name is not ShapeBase.NOT_SET:
                _params['delivery_stream_name'] = delivery_stream_name
            if current_delivery_stream_version_id is not ShapeBase.NOT_SET:
                _params['current_delivery_stream_version_id'
                       ] = current_delivery_stream_version_id
            if destination_id is not ShapeBase.NOT_SET:
                _params['destination_id'] = destination_id
            if s3_destination_update is not ShapeBase.NOT_SET:
                _params['s3_destination_update'] = s3_destination_update
            if extended_s3_destination_update is not ShapeBase.NOT_SET:
                _params['extended_s3_destination_update'
                       ] = extended_s3_destination_update
            if redshift_destination_update is not ShapeBase.NOT_SET:
                _params['redshift_destination_update'
                       ] = redshift_destination_update
            if elasticsearch_destination_update is not ShapeBase.NOT_SET:
                _params['elasticsearch_destination_update'
                       ] = elasticsearch_destination_update
            if splunk_destination_update is not ShapeBase.NOT_SET:
                _params['splunk_destination_update'] = splunk_destination_update
            _request = shapes.UpdateDestinationInput(**_params)
        response = self._boto_client.update_destination(**_request.to_boto())

        return shapes.UpdateDestinationOutput.from_boto(response)
