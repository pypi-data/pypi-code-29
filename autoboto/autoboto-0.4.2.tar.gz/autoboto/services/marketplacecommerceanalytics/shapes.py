import datetime
import typing
from autoboto import ShapeBase, OutputShapeBase, TypeInfo
import dataclasses


class DataSetType(str):
    customer_subscriber_hourly_monthly_subscriptions = "customer_subscriber_hourly_monthly_subscriptions"
    customer_subscriber_annual_subscriptions = "customer_subscriber_annual_subscriptions"
    daily_business_usage_by_instance_type = "daily_business_usage_by_instance_type"
    daily_business_fees = "daily_business_fees"
    daily_business_free_trial_conversions = "daily_business_free_trial_conversions"
    daily_business_new_instances = "daily_business_new_instances"
    daily_business_new_product_subscribers = "daily_business_new_product_subscribers"
    daily_business_canceled_product_subscribers = "daily_business_canceled_product_subscribers"
    monthly_revenue_billing_and_revenue_data = "monthly_revenue_billing_and_revenue_data"
    monthly_revenue_annual_subscriptions = "monthly_revenue_annual_subscriptions"
    disbursed_amount_by_product = "disbursed_amount_by_product"
    disbursed_amount_by_product_with_uncollected_funds = "disbursed_amount_by_product_with_uncollected_funds"
    disbursed_amount_by_instance_hours = "disbursed_amount_by_instance_hours"
    disbursed_amount_by_customer_geo = "disbursed_amount_by_customer_geo"
    disbursed_amount_by_age_of_uncollected_funds = "disbursed_amount_by_age_of_uncollected_funds"
    disbursed_amount_by_age_of_disbursed_funds = "disbursed_amount_by_age_of_disbursed_funds"
    customer_profile_by_industry = "customer_profile_by_industry"
    customer_profile_by_revenue = "customer_profile_by_revenue"
    customer_profile_by_geography = "customer_profile_by_geography"
    sales_compensation_billed_revenue = "sales_compensation_billed_revenue"
    us_sales_and_use_tax_records = "us_sales_and_use_tax_records"


@dataclasses.dataclass
class GenerateDataSetRequest(ShapeBase):
    """
    Container for the parameters to the GenerateDataSet operation.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "data_set_type",
                "dataSetType",
                TypeInfo(typing.Union[str, DataSetType]),
            ),
            (
                "data_set_publication_date",
                "dataSetPublicationDate",
                TypeInfo(datetime.datetime),
            ),
            (
                "role_name_arn",
                "roleNameArn",
                TypeInfo(str),
            ),
            (
                "destination_s3_bucket_name",
                "destinationS3BucketName",
                TypeInfo(str),
            ),
            (
                "sns_topic_arn",
                "snsTopicArn",
                TypeInfo(str),
            ),
            (
                "destination_s3_prefix",
                "destinationS3Prefix",
                TypeInfo(str),
            ),
            (
                "customer_defined_values",
                "customerDefinedValues",
                TypeInfo(typing.Dict[str, str]),
            ),
        ]

    # The desired data set type.

    #   * **customer_subscriber_hourly_monthly_subscriptions**

    # From 2014-07-21 to present: Available daily by 5:00 PM Pacific Time.

    #   * **customer_subscriber_annual_subscriptions**

    # From 2014-07-21 to present: Available daily by 5:00 PM Pacific Time.

    #   * **daily_business_usage_by_instance_type**

    # From 2015-01-26 to present: Available daily by 5:00 PM Pacific Time.

    #   * **daily_business_fees**

    # From 2015-01-26 to present: Available daily by 5:00 PM Pacific Time.

    #   * **daily_business_free_trial_conversions**

    # From 2015-01-26 to present: Available daily by 5:00 PM Pacific Time.

    #   * **daily_business_new_instances**

    # From 2015-01-26 to present: Available daily by 5:00 PM Pacific Time.

    #   * **daily_business_new_product_subscribers**

    # From 2015-01-26 to present: Available daily by 5:00 PM Pacific Time.

    #   * **daily_business_canceled_product_subscribers**

    # From 2015-01-26 to present: Available daily by 5:00 PM Pacific Time.

    #   * **monthly_revenue_billing_and_revenue_data**

    # From 2015-02 to 2017-06: Available monthly on the 4th day of the month by
    # 5:00pm Pacific Time. Data includes metered transactions (e.g. hourly) from
    # two months prior.

    # From 2017-07 to present: Available monthly on the 15th day of the month by
    # 5:00pm Pacific Time. Data includes metered transactions (e.g. hourly) from
    # one month prior.

    #   * **monthly_revenue_annual_subscriptions**

    # From 2015-02 to 2017-06: Available monthly on the 4th day of the month by
    # 5:00pm Pacific Time. Data includes up-front software charges (e.g. annual)
    # from one month prior.

    # From 2017-07 to present: Available monthly on the 15th day of the month by
    # 5:00pm Pacific Time. Data includes up-front software charges (e.g. annual)
    # from one month prior.

    #   * **disbursed_amount_by_product**

    # From 2015-01-26 to present: Available every 30 days by 5:00 PM Pacific
    # Time.

    #   * **disbursed_amount_by_product_with_uncollected_funds**

    # From 2012-04-19 to 2015-01-25: Available every 30 days by 5:00 PM Pacific
    # Time.

    # From 2015-01-26 to present: This data set was split into three data sets:
    # disbursed_amount_by_product, disbursed_amount_by_age_of_uncollected_funds,
    # and disbursed_amount_by_age_of_disbursed_funds.

    #   * **disbursed_amount_by_instance_hours**

    # From 2012-09-04 to present: Available every 30 days by 5:00 PM Pacific
    # Time.

    #   * **disbursed_amount_by_customer_geo**

    # From 2012-04-19 to present: Available every 30 days by 5:00 PM Pacific
    # Time.

    #   * **disbursed_amount_by_age_of_uncollected_funds**

    # From 2015-01-26 to present: Available every 30 days by 5:00 PM Pacific
    # Time.

    #   * **disbursed_amount_by_age_of_disbursed_funds**

    # From 2015-01-26 to present: Available every 30 days by 5:00 PM Pacific
    # Time.

    #   * **customer_profile_by_industry**

    # From 2015-10-01 to 2017-06-29: Available daily by 5:00 PM Pacific Time.

    # From 2017-06-30 to present: This data set is no longer available.

    #   * **customer_profile_by_revenue**

    # From 2015-10-01 to 2017-06-29: Available daily by 5:00 PM Pacific Time.

    # From 2017-06-30 to present: This data set is no longer available.

    #   * **customer_profile_by_geography**

    # From 2015-10-01 to 2017-06-29: Available daily by 5:00 PM Pacific Time.

    # From 2017-06-30 to present: This data set is no longer available.

    #   * **sales_compensation_billed_revenue**

    # From 2016-12 to 2017-06: Available monthly on the 4th day of the month by
    # 5:00pm Pacific Time. Data includes metered transactions (e.g. hourly) from
    # two months prior, and up-front software charges (e.g. annual) from one
    # month prior.

    # From 2017-06 to present: Available monthly on the 15th day of the month by
    # 5:00pm Pacific Time. Data includes metered transactions (e.g. hourly) from
    # one month prior, and up-front software charges (e.g. annual) from one month
    # prior.

    #   * **us_sales_and_use_tax_records**

    # From 2017-02-15 to present: Available monthly on the 15th day of the month
    # by 5:00 PM Pacific Time.
    data_set_type: typing.Union[str, "DataSetType"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The date a data set was published. For daily data sets, provide a date with
    # day-level granularity for the desired day. For weekly data sets, provide a
    # date with day-level granularity within the desired week (the day value will
    # be ignored). For monthly data sets, provide a date with month-level
    # granularity for the desired month (the day value will be ignored).
    data_set_publication_date: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The Amazon Resource Name (ARN) of the Role with an attached permissions
    # policy to interact with the provided AWS services.
    role_name_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The name (friendly name, not ARN) of the destination S3 bucket.
    destination_s3_bucket_name: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Amazon Resource Name (ARN) for the SNS Topic that will be notified when the
    # data set has been published or if an error has occurred.
    sns_topic_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # (Optional) The desired S3 prefix for the published data set, similar to a
    # directory path in standard file systems. For example, if given the bucket
    # name "mybucket" and the prefix "myprefix/mydatasets", the output file
    # "outputfile" would be published to
    # "s3://mybucket/myprefix/mydatasets/outputfile". If the prefix directory
    # structure does not exist, it will be created. If no prefix is provided, the
    # data set will be published to the S3 bucket root.
    destination_s3_prefix: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # (Optional) Key-value pairs which will be returned, unmodified, in the
    # Amazon SNS notification message and the data set metadata file. These key-
    # value pairs can be used to correlated responses with tracking information
    # from other systems.
    customer_defined_values: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class GenerateDataSetResult(OutputShapeBase):
    """
    Container for the result of the GenerateDataSet operation.
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
                "data_set_request_id",
                "dataSetRequestId",
                TypeInfo(str),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A unique identifier representing a specific request to the GenerateDataSet
    # operation. This identifier can be used to correlate a request with
    # notifications from the SNS topic.
    data_set_request_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class MarketplaceCommerceAnalyticsException(ShapeBase):
    """
    This exception is thrown when an internal service error occurs.
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

    # This message describes details of the error.
    message: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class StartSupportDataExportRequest(ShapeBase):
    """
    Container for the parameters to the StartSupportDataExport operation.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "data_set_type",
                "dataSetType",
                TypeInfo(typing.Union[str, SupportDataSetType]),
            ),
            (
                "from_date",
                "fromDate",
                TypeInfo(datetime.datetime),
            ),
            (
                "role_name_arn",
                "roleNameArn",
                TypeInfo(str),
            ),
            (
                "destination_s3_bucket_name",
                "destinationS3BucketName",
                TypeInfo(str),
            ),
            (
                "sns_topic_arn",
                "snsTopicArn",
                TypeInfo(str),
            ),
            (
                "destination_s3_prefix",
                "destinationS3Prefix",
                TypeInfo(str),
            ),
            (
                "customer_defined_values",
                "customerDefinedValues",
                TypeInfo(typing.Dict[str, str]),
            ),
        ]

    # Specifies the data set type to be written to the output csv file. The data
    # set types customer_support_contacts_data and
    # test_customer_support_contacts_data both result in a csv file containing
    # the following fields: Product Id, Product Code, Customer Guid, Subscription
    # Guid, Subscription Start Date, Organization, AWS Account Id, Given Name,
    # Surname, Telephone Number, Email, Title, Country Code, ZIP Code, Operation
    # Type, and Operation Time.

    #   * _customer_support_contacts_data_ Customer support contact data. The data set will contain all changes (Creates, Updates, and Deletes) to customer support contact data from the date specified in the from_date parameter.
    #   * _test_customer_support_contacts_data_ An example data set containing static test data in the same format as customer_support_contacts_data
    data_set_type: typing.Union[str, "SupportDataSetType"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The start date from which to retrieve the data set in UTC. This parameter
    # only affects the customer_support_contacts_data data set type.
    from_date: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The Amazon Resource Name (ARN) of the Role with an attached permissions
    # policy to interact with the provided AWS services.
    role_name_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The name (friendly name, not ARN) of the destination S3 bucket.
    destination_s3_bucket_name: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Amazon Resource Name (ARN) for the SNS Topic that will be notified when the
    # data set has been published or if an error has occurred.
    sns_topic_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # (Optional) The desired S3 prefix for the published data set, similar to a
    # directory path in standard file systems. For example, if given the bucket
    # name "mybucket" and the prefix "myprefix/mydatasets", the output file
    # "outputfile" would be published to
    # "s3://mybucket/myprefix/mydatasets/outputfile". If the prefix directory
    # structure does not exist, it will be created. If no prefix is provided, the
    # data set will be published to the S3 bucket root.
    destination_s3_prefix: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # (Optional) Key-value pairs which will be returned, unmodified, in the
    # Amazon SNS notification message and the data set metadata file.
    customer_defined_values: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class StartSupportDataExportResult(OutputShapeBase):
    """
    Container for the result of the StartSupportDataExport operation.
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
                "data_set_request_id",
                "dataSetRequestId",
                TypeInfo(str),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A unique identifier representing a specific request to the
    # StartSupportDataExport operation. This identifier can be used to correlate
    # a request with notifications from the SNS topic.
    data_set_request_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )


class SupportDataSetType(str):
    customer_support_contacts_data = "customer_support_contacts_data"
    test_customer_support_contacts_data = "test_customer_support_contacts_data"
