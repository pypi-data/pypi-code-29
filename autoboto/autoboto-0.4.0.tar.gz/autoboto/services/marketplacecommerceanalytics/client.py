import datetime
import typing
import boto3
from autoboto import ClientBase, ShapeBase, OutputShapeBase
from . import shapes


class Client(ClientBase):
    def __init__(self, *args, **kwargs):
        super().__init__("marketplacecommerceanalytics", *args, **kwargs)

    def generate_data_set(
        self,
        _request: shapes.GenerateDataSetRequest = None,
        *,
        data_set_type: typing.Union[str, shapes.DataSetType],
        data_set_publication_date: datetime.datetime,
        role_name_arn: str,
        destination_s3_bucket_name: str,
        sns_topic_arn: str,
        destination_s3_prefix: str = ShapeBase.NOT_SET,
        customer_defined_values: typing.Dict[str, str] = ShapeBase.NOT_SET,
    ) -> shapes.GenerateDataSetResult:
        """
        Given a data set type and data set publication date, asynchronously publishes
        the requested data set to the specified S3 bucket and notifies the specified SNS
        topic once the data is available. Returns a unique request identifier that can
        be used to correlate requests with notifications from the SNS topic. Data sets
        will be published in comma-separated values (CSV) format with the file name
        {data_set_type}_YYYY-MM-DD.csv. If a file with the same name already exists
        (e.g. if the same data set is requested twice), the original file will be
        overwritten by the new file. Requires a Role with an attached permissions policy
        providing Allow permissions for the following actions: s3:PutObject,
        s3:GetBucketLocation, sns:GetTopicAttributes, sns:Publish, iam:GetRolePolicy.
        """
        if _request is None:
            _params = {}
            if data_set_type is not ShapeBase.NOT_SET:
                _params['data_set_type'] = data_set_type
            if data_set_publication_date is not ShapeBase.NOT_SET:
                _params['data_set_publication_date'] = data_set_publication_date
            if role_name_arn is not ShapeBase.NOT_SET:
                _params['role_name_arn'] = role_name_arn
            if destination_s3_bucket_name is not ShapeBase.NOT_SET:
                _params['destination_s3_bucket_name'
                       ] = destination_s3_bucket_name
            if sns_topic_arn is not ShapeBase.NOT_SET:
                _params['sns_topic_arn'] = sns_topic_arn
            if destination_s3_prefix is not ShapeBase.NOT_SET:
                _params['destination_s3_prefix'] = destination_s3_prefix
            if customer_defined_values is not ShapeBase.NOT_SET:
                _params['customer_defined_values'] = customer_defined_values
            _request = shapes.GenerateDataSetRequest(**_params)
        response = self._boto_client.generate_data_set(**_request.to_boto())

        return shapes.GenerateDataSetResult.from_boto(response)

    def start_support_data_export(
        self,
        _request: shapes.StartSupportDataExportRequest = None,
        *,
        data_set_type: typing.Union[str, shapes.SupportDataSetType],
        from_date: datetime.datetime,
        role_name_arn: str,
        destination_s3_bucket_name: str,
        sns_topic_arn: str,
        destination_s3_prefix: str = ShapeBase.NOT_SET,
        customer_defined_values: typing.Dict[str, str] = ShapeBase.NOT_SET,
    ) -> shapes.StartSupportDataExportResult:
        """
        Given a data set type and a from date, asynchronously publishes the requested
        customer support data to the specified S3 bucket and notifies the specified SNS
        topic once the data is available. Returns a unique request identifier that can
        be used to correlate requests with notifications from the SNS topic. Data sets
        will be published in comma-separated values (CSV) format with the file name
        {data_set_type}_YYYY-MM-DD'T'HH-mm-ss'Z'.csv. If a file with the same name
        already exists (e.g. if the same data set is requested twice), the original file
        will be overwritten by the new file. Requires a Role with an attached
        permissions policy providing Allow permissions for the following actions:
        s3:PutObject, s3:GetBucketLocation, sns:GetTopicAttributes, sns:Publish,
        iam:GetRolePolicy.
        """
        if _request is None:
            _params = {}
            if data_set_type is not ShapeBase.NOT_SET:
                _params['data_set_type'] = data_set_type
            if from_date is not ShapeBase.NOT_SET:
                _params['from_date'] = from_date
            if role_name_arn is not ShapeBase.NOT_SET:
                _params['role_name_arn'] = role_name_arn
            if destination_s3_bucket_name is not ShapeBase.NOT_SET:
                _params['destination_s3_bucket_name'
                       ] = destination_s3_bucket_name
            if sns_topic_arn is not ShapeBase.NOT_SET:
                _params['sns_topic_arn'] = sns_topic_arn
            if destination_s3_prefix is not ShapeBase.NOT_SET:
                _params['destination_s3_prefix'] = destination_s3_prefix
            if customer_defined_values is not ShapeBase.NOT_SET:
                _params['customer_defined_values'] = customer_defined_values
            _request = shapes.StartSupportDataExportRequest(**_params)
        response = self._boto_client.start_support_data_export(
            **_request.to_boto()
        )

        return shapes.StartSupportDataExportResult.from_boto(response)
