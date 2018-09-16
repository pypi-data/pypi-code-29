import datetime
import typing
import boto3
from autoboto import ClientBase, ShapeBase, OutputShapeBase
from . import shapes


class Client(ClientBase):
    def __init__(self, *args, **kwargs):
        super().__init__("meteringmarketplace", *args, **kwargs)

    def batch_meter_usage(
        self,
        _request: shapes.BatchMeterUsageRequest = None,
        *,
        usage_records: typing.List[shapes.UsageRecord],
        product_code: str,
    ) -> shapes.BatchMeterUsageResult:
        """
        BatchMeterUsage is called from a SaaS application listed on the AWS Marketplace
        to post metering records for a set of customers.

        For identical requests, the API is idempotent; requests can be retried with the
        same records or a subset of the input records.

        Every request to BatchMeterUsage is for one product. If you need to meter usage
        for multiple products, you must make multiple calls to BatchMeterUsage.

        BatchMeterUsage can process up to 25 UsageRecords at a time.
        """
        if _request is None:
            _params = {}
            if usage_records is not ShapeBase.NOT_SET:
                _params['usage_records'] = usage_records
            if product_code is not ShapeBase.NOT_SET:
                _params['product_code'] = product_code
            _request = shapes.BatchMeterUsageRequest(**_params)
        response = self._boto_client.batch_meter_usage(**_request.to_boto())

        return shapes.BatchMeterUsageResult.from_boto(response)

    def meter_usage(
        self,
        _request: shapes.MeterUsageRequest = None,
        *,
        product_code: str,
        timestamp: datetime.datetime,
        usage_dimension: str,
        usage_quantity: int,
        dry_run: bool,
    ) -> shapes.MeterUsageResult:
        """
        API to emit metering records. For identical requests, the API is idempotent. It
        simply returns the metering record ID.

        MeterUsage is authenticated on the buyer's AWS account, generally when running
        from an EC2 instance on the AWS Marketplace.
        """
        if _request is None:
            _params = {}
            if product_code is not ShapeBase.NOT_SET:
                _params['product_code'] = product_code
            if timestamp is not ShapeBase.NOT_SET:
                _params['timestamp'] = timestamp
            if usage_dimension is not ShapeBase.NOT_SET:
                _params['usage_dimension'] = usage_dimension
            if usage_quantity is not ShapeBase.NOT_SET:
                _params['usage_quantity'] = usage_quantity
            if dry_run is not ShapeBase.NOT_SET:
                _params['dry_run'] = dry_run
            _request = shapes.MeterUsageRequest(**_params)
        response = self._boto_client.meter_usage(**_request.to_boto())

        return shapes.MeterUsageResult.from_boto(response)

    def resolve_customer(
        self,
        _request: shapes.ResolveCustomerRequest = None,
        *,
        registration_token: str,
    ) -> shapes.ResolveCustomerResult:
        """
        ResolveCustomer is called by a SaaS application during the registration process.
        When a buyer visits your website during the registration process, the buyer
        submits a registration token through their browser. The registration token is
        resolved through this API to obtain a CustomerIdentifier and product code.
        """
        if _request is None:
            _params = {}
            if registration_token is not ShapeBase.NOT_SET:
                _params['registration_token'] = registration_token
            _request = shapes.ResolveCustomerRequest(**_params)
        response = self._boto_client.resolve_customer(**_request.to_boto())

        return shapes.ResolveCustomerResult.from_boto(response)
