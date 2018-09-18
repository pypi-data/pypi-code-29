import datetime
import typing
from autoboto import ShapeBase, OutputShapeBase, TypeInfo
import dataclasses


@dataclasses.dataclass
class Entitlement(ShapeBase):
    """
    An entitlement represents capacity in a product owned by the customer. For
    example, a customer might own some number of users or seats in an SaaS
    application or some amount of data capacity in a multi-tenant database.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "product_code",
                "ProductCode",
                TypeInfo(str),
            ),
            (
                "dimension",
                "Dimension",
                TypeInfo(str),
            ),
            (
                "customer_identifier",
                "CustomerIdentifier",
                TypeInfo(str),
            ),
            (
                "value",
                "Value",
                TypeInfo(EntitlementValue),
            ),
            (
                "expiration_date",
                "ExpirationDate",
                TypeInfo(datetime.datetime),
            ),
        ]

    # The product code for which the given entitlement applies. Product codes are
    # provided by AWS Marketplace when the product listing is created.
    product_code: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The dimension for which the given entitlement applies. Dimensions represent
    # categories of capacity in a product and are specified when the product is
    # listed in AWS Marketplace.
    dimension: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The customer identifier is a handle to each unique customer in an
    # application. Customer identifiers are obtained through the ResolveCustomer
    # operation in AWS Marketplace Metering Service.
    customer_identifier: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The EntitlementValue represents the amount of capacity that the customer is
    # entitled to for the product.
    value: "EntitlementValue" = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The expiration date represents the minimum date through which this
    # entitlement is expected to remain valid. For contractual products listed on
    # AWS Marketplace, the expiration date is the date at which the customer will
    # renew or cancel their contract. Customers who are opting to renew their
    # contract will still have entitlements with an expiration date.
    expiration_date: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class EntitlementValue(ShapeBase):
    """
    The EntitlementValue represents the amount of capacity that the customer is
    entitled to for the product.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "integer_value",
                "IntegerValue",
                TypeInfo(int),
            ),
            (
                "double_value",
                "DoubleValue",
                TypeInfo(float),
            ),
            (
                "boolean_value",
                "BooleanValue",
                TypeInfo(bool),
            ),
            (
                "string_value",
                "StringValue",
                TypeInfo(str),
            ),
        ]

    # The IntegerValue field will be populated with an integer value when the
    # entitlement is an integer type. Otherwise, the field will not be set.
    integer_value: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The DoubleValue field will be populated with a double value when the
    # entitlement is a double type. Otherwise, the field will not be set.
    double_value: float = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The BooleanValue field will be populated with a boolean value when the
    # entitlement is a boolean type. Otherwise, the field will not be set.
    boolean_value: bool = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The StringValue field will be populated with a string value when the
    # entitlement is a string type. Otherwise, the field will not be set.
    string_value: str = dataclasses.field(default=ShapeBase.NOT_SET, )


class GetEntitlementFilterName(str):
    CUSTOMER_IDENTIFIER = "CUSTOMER_IDENTIFIER"
    DIMENSION = "DIMENSION"


@dataclasses.dataclass
class GetEntitlementsRequest(ShapeBase):
    """
    The GetEntitlementsRequest contains parameters for the GetEntitlements
    operation.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "product_code",
                "ProductCode",
                TypeInfo(str),
            ),
            (
                "filter",
                "Filter",
                TypeInfo(
                    typing.Dict[typing.Union[str, GetEntitlementFilterName],
                                typing.List[str]]
                ),
            ),
            (
                "next_token",
                "NextToken",
                TypeInfo(str),
            ),
            (
                "max_results",
                "MaxResults",
                TypeInfo(int),
            ),
        ]

    # Product code is used to uniquely identify a product in AWS Marketplace. The
    # product code will be provided by AWS Marketplace when the product listing
    # is created.
    product_code: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Filter is used to return entitlements for a specific customer or for a
    # specific dimension. Filters are described as keys mapped to a lists of
    # values. Filtered requests are _unioned_ for each value in the value list,
    # and then _intersected_ for each filter key.
    filter: typing.Dict[typing.Union[str, "GetEntitlementFilterName"], typing.
                        List[str]] = dataclasses.field(
                            default=ShapeBase.NOT_SET,
                        )

    # For paginated calls to GetEntitlements, pass the NextToken from the
    # previous GetEntitlementsResult.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The maximum number of items to retrieve from the GetEntitlements operation.
    # For pagination, use the NextToken field in subsequent calls to
    # GetEntitlements.
    max_results: int = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class GetEntitlementsResult(OutputShapeBase):
    """
    The GetEntitlementsRequest contains results from the GetEntitlements operation.
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
                "entitlements",
                "Entitlements",
                TypeInfo(typing.List[Entitlement]),
            ),
            (
                "next_token",
                "NextToken",
                TypeInfo(str),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The set of entitlements found through the GetEntitlements operation. If the
    # result contains an empty set of entitlements, NextToken might still be
    # present and should be used.
    entitlements: typing.List["Entitlement"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # For paginated results, use NextToken in subsequent calls to
    # GetEntitlements. If the result contains an empty set of entitlements,
    # NextToken might still be present and should be used.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class InternalServiceErrorException(ShapeBase):
    """
    An internal error has occurred. Retry your request. If the problem persists,
    post a message with details on the AWS forums.
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
class InvalidParameterException(ShapeBase):
    """
    One or more parameters in your request was invalid.
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
class ThrottlingException(ShapeBase):
    """
    The calls to the GetEntitlements API are throttled.
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
