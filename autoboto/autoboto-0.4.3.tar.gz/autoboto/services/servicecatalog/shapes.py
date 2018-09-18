import datetime
import typing
from autoboto import ShapeBase, OutputShapeBase, TypeInfo
import dataclasses


@dataclasses.dataclass
class AcceptPortfolioShareInput(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "portfolio_id",
                "PortfolioId",
                TypeInfo(str),
            ),
            (
                "accept_language",
                "AcceptLanguage",
                TypeInfo(str),
            ),
        ]

    # The portfolio identifier.
    portfolio_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The language code.

    #   * `en` \- English (default)

    #   * `jp` \- Japanese

    #   * `zh` \- Chinese
    accept_language: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class AcceptPortfolioShareOutput(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class AccessLevelFilter(ShapeBase):
    """
    The access level to use to filter results.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "key",
                "Key",
                TypeInfo(typing.Union[str, AccessLevelFilterKey]),
            ),
            (
                "value",
                "Value",
                TypeInfo(str),
            ),
        ]

    # The access level.

    #   * `Account` \- Filter results based on the account.

    #   * `Role` \- Filter results based on the federated role of the specified user.

    #   * `User` \- Filter results based on the specified user.
    key: typing.Union[str, "AccessLevelFilterKey"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The user to which the access level applies. The only supported value is
    # `Self`.
    value: str = dataclasses.field(default=ShapeBase.NOT_SET, )


class AccessLevelFilterKey(str):
    Account = "Account"
    Role = "Role"
    User = "User"


@dataclasses.dataclass
class AssociatePrincipalWithPortfolioInput(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "portfolio_id",
                "PortfolioId",
                TypeInfo(str),
            ),
            (
                "principal_arn",
                "PrincipalARN",
                TypeInfo(str),
            ),
            (
                "principal_type",
                "PrincipalType",
                TypeInfo(typing.Union[str, PrincipalType]),
            ),
            (
                "accept_language",
                "AcceptLanguage",
                TypeInfo(str),
            ),
        ]

    # The portfolio identifier.
    portfolio_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The ARN of the principal (IAM user, role, or group).
    principal_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The principal type. The supported value is `IAM`.
    principal_type: typing.Union[str, "PrincipalType"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The language code.

    #   * `en` \- English (default)

    #   * `jp` \- Japanese

    #   * `zh` \- Chinese
    accept_language: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class AssociatePrincipalWithPortfolioOutput(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class AssociateProductWithPortfolioInput(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "product_id",
                "ProductId",
                TypeInfo(str),
            ),
            (
                "portfolio_id",
                "PortfolioId",
                TypeInfo(str),
            ),
            (
                "accept_language",
                "AcceptLanguage",
                TypeInfo(str),
            ),
            (
                "source_portfolio_id",
                "SourcePortfolioId",
                TypeInfo(str),
            ),
        ]

    # The product identifier.
    product_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The portfolio identifier.
    portfolio_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The language code.

    #   * `en` \- English (default)

    #   * `jp` \- Japanese

    #   * `zh` \- Chinese
    accept_language: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The identifier of the source portfolio.
    source_portfolio_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class AssociateProductWithPortfolioOutput(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class AssociateTagOptionWithResourceInput(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "resource_id",
                "ResourceId",
                TypeInfo(str),
            ),
            (
                "tag_option_id",
                "TagOptionId",
                TypeInfo(str),
            ),
        ]

    # The resource identifier.
    resource_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The TagOption identifier.
    tag_option_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class AssociateTagOptionWithResourceOutput(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


class ChangeAction(str):
    ADD = "ADD"
    MODIFY = "MODIFY"
    REMOVE = "REMOVE"


@dataclasses.dataclass
class CloudWatchDashboard(ShapeBase):
    """
    Information about a CloudWatch dashboard.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "name",
                "Name",
                TypeInfo(str),
            ),
        ]

    # The name of the CloudWatch dashboard.
    name: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ConstraintDetail(ShapeBase):
    """
    Information about a constraint.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "constraint_id",
                "ConstraintId",
                TypeInfo(str),
            ),
            (
                "type",
                "Type",
                TypeInfo(str),
            ),
            (
                "description",
                "Description",
                TypeInfo(str),
            ),
            (
                "owner",
                "Owner",
                TypeInfo(str),
            ),
        ]

    # The identifier of the constraint.
    constraint_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The type of constraint.

    #   * `LAUNCH`

    #   * `NOTIFICATION`

    #   * `TEMPLATE`
    type: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The description of the constraint.
    description: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The owner of the constraint.
    owner: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ConstraintSummary(ShapeBase):
    """
    Summary information about a constraint.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "type",
                "Type",
                TypeInfo(str),
            ),
            (
                "description",
                "Description",
                TypeInfo(str),
            ),
        ]

    # The type of constraint.

    #   * `LAUNCH`

    #   * `NOTIFICATION`

    #   * `TEMPLATE`
    type: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The description of the constraint.
    description: str = dataclasses.field(default=ShapeBase.NOT_SET, )


class CopyOption(str):
    CopyTags = "CopyTags"


@dataclasses.dataclass
class CopyProductInput(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "source_product_arn",
                "SourceProductArn",
                TypeInfo(str),
            ),
            (
                "idempotency_token",
                "IdempotencyToken",
                TypeInfo(str),
            ),
            (
                "accept_language",
                "AcceptLanguage",
                TypeInfo(str),
            ),
            (
                "target_product_id",
                "TargetProductId",
                TypeInfo(str),
            ),
            (
                "target_product_name",
                "TargetProductName",
                TypeInfo(str),
            ),
            (
                "source_provisioning_artifact_identifiers",
                "SourceProvisioningArtifactIdentifiers",
                TypeInfo(
                    typing.List[typing.Dict[
                        typing.
                        Union[str, ProvisioningArtifactPropertyName], str]]
                ),
            ),
            (
                "copy_options",
                "CopyOptions",
                TypeInfo(typing.List[typing.Union[str, CopyOption]]),
            ),
        ]

    # The Amazon Resource Name (ARN) of the source product.
    source_product_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A unique identifier that you provide to ensure idempotency. If multiple
    # requests differ only by the idempotency token, the same response is
    # returned for each repeated request.
    idempotency_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The language code.

    #   * `en` \- English (default)

    #   * `jp` \- Japanese

    #   * `zh` \- Chinese
    accept_language: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The identifier of the target product. By default, a new product is created.
    target_product_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A name for the target product. The default is the name of the source
    # product.
    target_product_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The identifiers of the provisioning artifacts (also known as versions) of
    # the product to copy. By default, all provisioning artifacts are copied.
    source_provisioning_artifact_identifiers: typing.List[
        typing.Dict[typing.Union[str, "ProvisioningArtifactPropertyName"], str]
    ] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The copy options. If the value is `CopyTags`, the tags from the source
    # product are copied to the target product.
    copy_options: typing.List[typing.Union[str, "CopyOption"]
                             ] = dataclasses.field(
                                 default=ShapeBase.NOT_SET,
                             )


@dataclasses.dataclass
class CopyProductOutput(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "copy_product_token",
                "CopyProductToken",
                TypeInfo(str),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The token to use to track the progress of the operation.
    copy_product_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )


class CopyProductStatus(str):
    SUCCEEDED = "SUCCEEDED"
    IN_PROGRESS = "IN_PROGRESS"
    FAILED = "FAILED"


@dataclasses.dataclass
class CreateConstraintInput(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "portfolio_id",
                "PortfolioId",
                TypeInfo(str),
            ),
            (
                "product_id",
                "ProductId",
                TypeInfo(str),
            ),
            (
                "parameters",
                "Parameters",
                TypeInfo(str),
            ),
            (
                "type",
                "Type",
                TypeInfo(str),
            ),
            (
                "idempotency_token",
                "IdempotencyToken",
                TypeInfo(str),
            ),
            (
                "accept_language",
                "AcceptLanguage",
                TypeInfo(str),
            ),
            (
                "description",
                "Description",
                TypeInfo(str),
            ),
        ]

    # The portfolio identifier.
    portfolio_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The product identifier.
    product_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The constraint parameters, in JSON format. The syntax depends on the
    # constraint type as follows:

    # LAUNCH

    # Specify the `RoleArn` property as follows:

    # \"RoleArn\" : \"arn:aws:iam::123456789012:role/LaunchRole\"

    # NOTIFICATION

    # Specify the `NotificationArns` property as follows:

    # \"NotificationArns\" : [\"arn:aws:sns:us-east-1:123456789012:Topic\"]

    # TEMPLATE

    # Specify the `Rules` property. For more information, see [Template
    # Constraint
    # Rules](http://docs.aws.amazon.com/servicecatalog/latest/adminguide/reference-
    # template_constraint_rules.html).
    parameters: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The type of constraint.

    #   * `LAUNCH`

    #   * `NOTIFICATION`

    #   * `TEMPLATE`
    type: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A unique identifier that you provide to ensure idempotency. If multiple
    # requests differ only by the idempotency token, the same response is
    # returned for each repeated request.
    idempotency_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The language code.

    #   * `en` \- English (default)

    #   * `jp` \- Japanese

    #   * `zh` \- Chinese
    accept_language: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The description of the constraint.
    description: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class CreateConstraintOutput(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "constraint_detail",
                "ConstraintDetail",
                TypeInfo(ConstraintDetail),
            ),
            (
                "constraint_parameters",
                "ConstraintParameters",
                TypeInfo(str),
            ),
            (
                "status",
                "Status",
                TypeInfo(typing.Union[str, Status]),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Information about the constraint.
    constraint_detail: "ConstraintDetail" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The constraint parameters.
    constraint_parameters: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The status of the current request.
    status: typing.Union[str, "Status"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class CreatePortfolioInput(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "display_name",
                "DisplayName",
                TypeInfo(str),
            ),
            (
                "provider_name",
                "ProviderName",
                TypeInfo(str),
            ),
            (
                "idempotency_token",
                "IdempotencyToken",
                TypeInfo(str),
            ),
            (
                "accept_language",
                "AcceptLanguage",
                TypeInfo(str),
            ),
            (
                "description",
                "Description",
                TypeInfo(str),
            ),
            (
                "tags",
                "Tags",
                TypeInfo(typing.List[Tag]),
            ),
        ]

    # The name to use for display purposes.
    display_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The name of the portfolio provider.
    provider_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A unique identifier that you provide to ensure idempotency. If multiple
    # requests differ only by the idempotency token, the same response is
    # returned for each repeated request.
    idempotency_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The language code.

    #   * `en` \- English (default)

    #   * `jp` \- Japanese

    #   * `zh` \- Chinese
    accept_language: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The description of the portfolio.
    description: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # One or more tags.
    tags: typing.List["Tag"] = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class CreatePortfolioOutput(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "portfolio_detail",
                "PortfolioDetail",
                TypeInfo(PortfolioDetail),
            ),
            (
                "tags",
                "Tags",
                TypeInfo(typing.List[Tag]),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Information about the portfolio.
    portfolio_detail: "PortfolioDetail" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Information about the tags associated with the portfolio.
    tags: typing.List["Tag"] = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class CreatePortfolioShareInput(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "portfolio_id",
                "PortfolioId",
                TypeInfo(str),
            ),
            (
                "account_id",
                "AccountId",
                TypeInfo(str),
            ),
            (
                "accept_language",
                "AcceptLanguage",
                TypeInfo(str),
            ),
        ]

    # The portfolio identifier.
    portfolio_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The AWS account ID.
    account_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The language code.

    #   * `en` \- English (default)

    #   * `jp` \- Japanese

    #   * `zh` \- Chinese
    accept_language: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class CreatePortfolioShareOutput(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class CreateProductInput(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "name",
                "Name",
                TypeInfo(str),
            ),
            (
                "owner",
                "Owner",
                TypeInfo(str),
            ),
            (
                "product_type",
                "ProductType",
                TypeInfo(typing.Union[str, ProductType]),
            ),
            (
                "provisioning_artifact_parameters",
                "ProvisioningArtifactParameters",
                TypeInfo(ProvisioningArtifactProperties),
            ),
            (
                "idempotency_token",
                "IdempotencyToken",
                TypeInfo(str),
            ),
            (
                "accept_language",
                "AcceptLanguage",
                TypeInfo(str),
            ),
            (
                "description",
                "Description",
                TypeInfo(str),
            ),
            (
                "distributor",
                "Distributor",
                TypeInfo(str),
            ),
            (
                "support_description",
                "SupportDescription",
                TypeInfo(str),
            ),
            (
                "support_email",
                "SupportEmail",
                TypeInfo(str),
            ),
            (
                "support_url",
                "SupportUrl",
                TypeInfo(str),
            ),
            (
                "tags",
                "Tags",
                TypeInfo(typing.List[Tag]),
            ),
        ]

    # The name of the product.
    name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The owner of the product.
    owner: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The type of product.
    product_type: typing.Union[str, "ProductType"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The configuration of the provisioning artifact.
    provisioning_artifact_parameters: "ProvisioningArtifactProperties" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A unique identifier that you provide to ensure idempotency. If multiple
    # requests differ only by the idempotency token, the same response is
    # returned for each repeated request.
    idempotency_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The language code.

    #   * `en` \- English (default)

    #   * `jp` \- Japanese

    #   * `zh` \- Chinese
    accept_language: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The description of the product.
    description: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The distributor of the product.
    distributor: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The support information about the product.
    support_description: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The contact email for product support.
    support_email: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The contact URL for product support.
    support_url: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # One or more tags.
    tags: typing.List["Tag"] = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class CreateProductOutput(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "product_view_detail",
                "ProductViewDetail",
                TypeInfo(ProductViewDetail),
            ),
            (
                "provisioning_artifact_detail",
                "ProvisioningArtifactDetail",
                TypeInfo(ProvisioningArtifactDetail),
            ),
            (
                "tags",
                "Tags",
                TypeInfo(typing.List[Tag]),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Information about the product view.
    product_view_detail: "ProductViewDetail" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Information about the provisioning artifact.
    provisioning_artifact_detail: "ProvisioningArtifactDetail" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Information about the tags associated with the product.
    tags: typing.List["Tag"] = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class CreateProvisionedProductPlanInput(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "plan_name",
                "PlanName",
                TypeInfo(str),
            ),
            (
                "plan_type",
                "PlanType",
                TypeInfo(typing.Union[str, ProvisionedProductPlanType]),
            ),
            (
                "product_id",
                "ProductId",
                TypeInfo(str),
            ),
            (
                "provisioned_product_name",
                "ProvisionedProductName",
                TypeInfo(str),
            ),
            (
                "provisioning_artifact_id",
                "ProvisioningArtifactId",
                TypeInfo(str),
            ),
            (
                "idempotency_token",
                "IdempotencyToken",
                TypeInfo(str),
            ),
            (
                "accept_language",
                "AcceptLanguage",
                TypeInfo(str),
            ),
            (
                "notification_arns",
                "NotificationArns",
                TypeInfo(typing.List[str]),
            ),
            (
                "path_id",
                "PathId",
                TypeInfo(str),
            ),
            (
                "provisioning_parameters",
                "ProvisioningParameters",
                TypeInfo(typing.List[UpdateProvisioningParameter]),
            ),
            (
                "tags",
                "Tags",
                TypeInfo(typing.List[Tag]),
            ),
        ]

    # The name of the plan.
    plan_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The plan type.
    plan_type: typing.Union[str, "ProvisionedProductPlanType"
                           ] = dataclasses.field(
                               default=ShapeBase.NOT_SET,
                           )

    # The product identifier.
    product_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A user-friendly name for the provisioned product. This value must be unique
    # for the AWS account and cannot be updated after the product is provisioned.
    provisioned_product_name: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The identifier of the provisioning artifact.
    provisioning_artifact_id: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A unique identifier that you provide to ensure idempotency. If multiple
    # requests differ only by the idempotency token, the same response is
    # returned for each repeated request.
    idempotency_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The language code.

    #   * `en` \- English (default)

    #   * `jp` \- Japanese

    #   * `zh` \- Chinese
    accept_language: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Passed to CloudFormation. The SNS topic ARNs to which to publish stack-
    # related events.
    notification_arns: typing.List[str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The path identifier of the product. This value is optional if the product
    # has a default path, and required if the product has more than one path. To
    # list the paths for a product, use ListLaunchPaths.
    path_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Parameters specified by the administrator that are required for
    # provisioning the product.
    provisioning_parameters: typing.List["UpdateProvisioningParameter"
                                        ] = dataclasses.field(
                                            default=ShapeBase.NOT_SET,
                                        )

    # One or more tags.
    tags: typing.List["Tag"] = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class CreateProvisionedProductPlanOutput(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "plan_name",
                "PlanName",
                TypeInfo(str),
            ),
            (
                "plan_id",
                "PlanId",
                TypeInfo(str),
            ),
            (
                "provision_product_id",
                "ProvisionProductId",
                TypeInfo(str),
            ),
            (
                "provisioned_product_name",
                "ProvisionedProductName",
                TypeInfo(str),
            ),
            (
                "provisioning_artifact_id",
                "ProvisioningArtifactId",
                TypeInfo(str),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The name of the plan.
    plan_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The plan identifier.
    plan_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The product identifier.
    provision_product_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The user-friendly name of the provisioned product.
    provisioned_product_name: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The identifier of the provisioning artifact.
    provisioning_artifact_id: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class CreateProvisioningArtifactInput(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "product_id",
                "ProductId",
                TypeInfo(str),
            ),
            (
                "parameters",
                "Parameters",
                TypeInfo(ProvisioningArtifactProperties),
            ),
            (
                "idempotency_token",
                "IdempotencyToken",
                TypeInfo(str),
            ),
            (
                "accept_language",
                "AcceptLanguage",
                TypeInfo(str),
            ),
        ]

    # The product identifier.
    product_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The configuration for the provisioning artifact.
    parameters: "ProvisioningArtifactProperties" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A unique identifier that you provide to ensure idempotency. If multiple
    # requests differ only by the idempotency token, the same response is
    # returned for each repeated request.
    idempotency_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The language code.

    #   * `en` \- English (default)

    #   * `jp` \- Japanese

    #   * `zh` \- Chinese
    accept_language: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class CreateProvisioningArtifactOutput(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "provisioning_artifact_detail",
                "ProvisioningArtifactDetail",
                TypeInfo(ProvisioningArtifactDetail),
            ),
            (
                "info",
                "Info",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "status",
                "Status",
                TypeInfo(typing.Union[str, Status]),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Information about the provisioning artifact.
    provisioning_artifact_detail: "ProvisioningArtifactDetail" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The URL of the CloudFormation template in Amazon S3, in JSON format.
    info: typing.Dict[str, str] = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The status of the current request.
    status: typing.Union[str, "Status"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class CreateTagOptionInput(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "key",
                "Key",
                TypeInfo(str),
            ),
            (
                "value",
                "Value",
                TypeInfo(str),
            ),
        ]

    # The TagOption key.
    key: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The TagOption value.
    value: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class CreateTagOptionOutput(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "tag_option_detail",
                "TagOptionDetail",
                TypeInfo(TagOptionDetail),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Information about the TagOption.
    tag_option_detail: "TagOptionDetail" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class DeleteConstraintInput(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "id",
                "Id",
                TypeInfo(str),
            ),
            (
                "accept_language",
                "AcceptLanguage",
                TypeInfo(str),
            ),
        ]

    # The identifier of the constraint.
    id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The language code.

    #   * `en` \- English (default)

    #   * `jp` \- Japanese

    #   * `zh` \- Chinese
    accept_language: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DeleteConstraintOutput(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class DeletePortfolioInput(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "id",
                "Id",
                TypeInfo(str),
            ),
            (
                "accept_language",
                "AcceptLanguage",
                TypeInfo(str),
            ),
        ]

    # The portfolio identifier.
    id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The language code.

    #   * `en` \- English (default)

    #   * `jp` \- Japanese

    #   * `zh` \- Chinese
    accept_language: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DeletePortfolioOutput(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class DeletePortfolioShareInput(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "portfolio_id",
                "PortfolioId",
                TypeInfo(str),
            ),
            (
                "account_id",
                "AccountId",
                TypeInfo(str),
            ),
            (
                "accept_language",
                "AcceptLanguage",
                TypeInfo(str),
            ),
        ]

    # The portfolio identifier.
    portfolio_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The AWS account ID.
    account_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The language code.

    #   * `en` \- English (default)

    #   * `jp` \- Japanese

    #   * `zh` \- Chinese
    accept_language: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DeletePortfolioShareOutput(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class DeleteProductInput(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "id",
                "Id",
                TypeInfo(str),
            ),
            (
                "accept_language",
                "AcceptLanguage",
                TypeInfo(str),
            ),
        ]

    # The product identifier.
    id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The language code.

    #   * `en` \- English (default)

    #   * `jp` \- Japanese

    #   * `zh` \- Chinese
    accept_language: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DeleteProductOutput(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class DeleteProvisionedProductPlanInput(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "plan_id",
                "PlanId",
                TypeInfo(str),
            ),
            (
                "accept_language",
                "AcceptLanguage",
                TypeInfo(str),
            ),
            (
                "ignore_errors",
                "IgnoreErrors",
                TypeInfo(bool),
            ),
        ]

    # The plan identifier.
    plan_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The language code.

    #   * `en` \- English (default)

    #   * `jp` \- Japanese

    #   * `zh` \- Chinese
    accept_language: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # If set to true, AWS Service Catalog stops managing the specified
    # provisioned product even if it cannot delete the underlying resources.
    ignore_errors: bool = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DeleteProvisionedProductPlanOutput(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class DeleteProvisioningArtifactInput(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "product_id",
                "ProductId",
                TypeInfo(str),
            ),
            (
                "provisioning_artifact_id",
                "ProvisioningArtifactId",
                TypeInfo(str),
            ),
            (
                "accept_language",
                "AcceptLanguage",
                TypeInfo(str),
            ),
        ]

    # The product identifier.
    product_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The identifier of the provisioning artifact.
    provisioning_artifact_id: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The language code.

    #   * `en` \- English (default)

    #   * `jp` \- Japanese

    #   * `zh` \- Chinese
    accept_language: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DeleteProvisioningArtifactOutput(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class DeleteTagOptionInput(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "id",
                "Id",
                TypeInfo(str),
            ),
        ]

    # The TagOption identifier.
    id: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DeleteTagOptionOutput(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class DescribeConstraintInput(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "id",
                "Id",
                TypeInfo(str),
            ),
            (
                "accept_language",
                "AcceptLanguage",
                TypeInfo(str),
            ),
        ]

    # The identifier of the constraint.
    id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The language code.

    #   * `en` \- English (default)

    #   * `jp` \- Japanese

    #   * `zh` \- Chinese
    accept_language: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DescribeConstraintOutput(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "constraint_detail",
                "ConstraintDetail",
                TypeInfo(ConstraintDetail),
            ),
            (
                "constraint_parameters",
                "ConstraintParameters",
                TypeInfo(str),
            ),
            (
                "status",
                "Status",
                TypeInfo(typing.Union[str, Status]),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Information about the constraint.
    constraint_detail: "ConstraintDetail" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The constraint parameters.
    constraint_parameters: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The status of the current request.
    status: typing.Union[str, "Status"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class DescribeCopyProductStatusInput(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "copy_product_token",
                "CopyProductToken",
                TypeInfo(str),
            ),
            (
                "accept_language",
                "AcceptLanguage",
                TypeInfo(str),
            ),
        ]

    # The token for the copy product operation. This token is returned by
    # CopyProduct.
    copy_product_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The language code.

    #   * `en` \- English (default)

    #   * `jp` \- Japanese

    #   * `zh` \- Chinese
    accept_language: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DescribeCopyProductStatusOutput(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "copy_product_status",
                "CopyProductStatus",
                TypeInfo(typing.Union[str, CopyProductStatus]),
            ),
            (
                "target_product_id",
                "TargetProductId",
                TypeInfo(str),
            ),
            (
                "status_detail",
                "StatusDetail",
                TypeInfo(str),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The status of the copy product operation.
    copy_product_status: typing.Union[str, "CopyProductStatus"
                                     ] = dataclasses.field(
                                         default=ShapeBase.NOT_SET,
                                     )

    # The identifier of the copied product.
    target_product_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The status message.
    status_detail: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DescribePortfolioInput(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "id",
                "Id",
                TypeInfo(str),
            ),
            (
                "accept_language",
                "AcceptLanguage",
                TypeInfo(str),
            ),
        ]

    # The portfolio identifier.
    id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The language code.

    #   * `en` \- English (default)

    #   * `jp` \- Japanese

    #   * `zh` \- Chinese
    accept_language: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DescribePortfolioOutput(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "portfolio_detail",
                "PortfolioDetail",
                TypeInfo(PortfolioDetail),
            ),
            (
                "tags",
                "Tags",
                TypeInfo(typing.List[Tag]),
            ),
            (
                "tag_options",
                "TagOptions",
                TypeInfo(typing.List[TagOptionDetail]),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Information about the portfolio.
    portfolio_detail: "PortfolioDetail" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Information about the tags associated with the portfolio.
    tags: typing.List["Tag"] = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Information about the TagOptions associated with the portfolio.
    tag_options: typing.List["TagOptionDetail"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class DescribeProductAsAdminInput(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "id",
                "Id",
                TypeInfo(str),
            ),
            (
                "accept_language",
                "AcceptLanguage",
                TypeInfo(str),
            ),
        ]

    # The product identifier.
    id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The language code.

    #   * `en` \- English (default)

    #   * `jp` \- Japanese

    #   * `zh` \- Chinese
    accept_language: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DescribeProductAsAdminOutput(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "product_view_detail",
                "ProductViewDetail",
                TypeInfo(ProductViewDetail),
            ),
            (
                "provisioning_artifact_summaries",
                "ProvisioningArtifactSummaries",
                TypeInfo(typing.List[ProvisioningArtifactSummary]),
            ),
            (
                "tags",
                "Tags",
                TypeInfo(typing.List[Tag]),
            ),
            (
                "tag_options",
                "TagOptions",
                TypeInfo(typing.List[TagOptionDetail]),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Information about the product view.
    product_view_detail: "ProductViewDetail" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Information about the provisioning artifacts (also known as versions) for
    # the specified product.
    provisioning_artifact_summaries: typing.List["ProvisioningArtifactSummary"
                                                ] = dataclasses.field(
                                                    default=ShapeBase.NOT_SET,
                                                )

    # Information about the tags associated with the product.
    tags: typing.List["Tag"] = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Information about the TagOptions associated with the product.
    tag_options: typing.List["TagOptionDetail"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class DescribeProductInput(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "id",
                "Id",
                TypeInfo(str),
            ),
            (
                "accept_language",
                "AcceptLanguage",
                TypeInfo(str),
            ),
        ]

    # The product identifier.
    id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The language code.

    #   * `en` \- English (default)

    #   * `jp` \- Japanese

    #   * `zh` \- Chinese
    accept_language: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DescribeProductOutput(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "product_view_summary",
                "ProductViewSummary",
                TypeInfo(ProductViewSummary),
            ),
            (
                "provisioning_artifacts",
                "ProvisioningArtifacts",
                TypeInfo(typing.List[ProvisioningArtifact]),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Summary information about the product view.
    product_view_summary: "ProductViewSummary" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Information about the provisioning artifacts for the specified product.
    provisioning_artifacts: typing.List["ProvisioningArtifact"
                                       ] = dataclasses.field(
                                           default=ShapeBase.NOT_SET,
                                       )


@dataclasses.dataclass
class DescribeProductViewInput(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "id",
                "Id",
                TypeInfo(str),
            ),
            (
                "accept_language",
                "AcceptLanguage",
                TypeInfo(str),
            ),
        ]

    # The product view identifier.
    id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The language code.

    #   * `en` \- English (default)

    #   * `jp` \- Japanese

    #   * `zh` \- Chinese
    accept_language: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DescribeProductViewOutput(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "product_view_summary",
                "ProductViewSummary",
                TypeInfo(ProductViewSummary),
            ),
            (
                "provisioning_artifacts",
                "ProvisioningArtifacts",
                TypeInfo(typing.List[ProvisioningArtifact]),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Summary information about the product.
    product_view_summary: "ProductViewSummary" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Information about the provisioning artifacts for the product.
    provisioning_artifacts: typing.List["ProvisioningArtifact"
                                       ] = dataclasses.field(
                                           default=ShapeBase.NOT_SET,
                                       )


@dataclasses.dataclass
class DescribeProvisionedProductInput(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "id",
                "Id",
                TypeInfo(str),
            ),
            (
                "accept_language",
                "AcceptLanguage",
                TypeInfo(str),
            ),
        ]

    # The provisioned product identifier.
    id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The language code.

    #   * `en` \- English (default)

    #   * `jp` \- Japanese

    #   * `zh` \- Chinese
    accept_language: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DescribeProvisionedProductOutput(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "provisioned_product_detail",
                "ProvisionedProductDetail",
                TypeInfo(ProvisionedProductDetail),
            ),
            (
                "cloud_watch_dashboards",
                "CloudWatchDashboards",
                TypeInfo(typing.List[CloudWatchDashboard]),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Information about the provisioned product.
    provisioned_product_detail: "ProvisionedProductDetail" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Any CloudWatch dashboards that were created when provisioning the product.
    cloud_watch_dashboards: typing.List["CloudWatchDashboard"
                                       ] = dataclasses.field(
                                           default=ShapeBase.NOT_SET,
                                       )


@dataclasses.dataclass
class DescribeProvisionedProductPlanInput(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "plan_id",
                "PlanId",
                TypeInfo(str),
            ),
            (
                "accept_language",
                "AcceptLanguage",
                TypeInfo(str),
            ),
            (
                "page_size",
                "PageSize",
                TypeInfo(int),
            ),
            (
                "page_token",
                "PageToken",
                TypeInfo(str),
            ),
        ]

    # The plan identifier.
    plan_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The language code.

    #   * `en` \- English (default)

    #   * `jp` \- Japanese

    #   * `zh` \- Chinese
    accept_language: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The maximum number of items to return with this call.
    page_size: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The page token for the next set of results. To retrieve the first set of
    # results, use null.
    page_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DescribeProvisionedProductPlanOutput(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "provisioned_product_plan_details",
                "ProvisionedProductPlanDetails",
                TypeInfo(ProvisionedProductPlanDetails),
            ),
            (
                "resource_changes",
                "ResourceChanges",
                TypeInfo(typing.List[ResourceChange]),
            ),
            (
                "next_page_token",
                "NextPageToken",
                TypeInfo(str),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Information about the plan.
    provisioned_product_plan_details: "ProvisionedProductPlanDetails" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Information about the resource changes that will occur when the plan is
    # executed.
    resource_changes: typing.List["ResourceChange"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The page token to use to retrieve the next set of results. If there are no
    # additional results, this value is null.
    next_page_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DescribeProvisioningArtifactInput(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "provisioning_artifact_id",
                "ProvisioningArtifactId",
                TypeInfo(str),
            ),
            (
                "product_id",
                "ProductId",
                TypeInfo(str),
            ),
            (
                "accept_language",
                "AcceptLanguage",
                TypeInfo(str),
            ),
            (
                "verbose",
                "Verbose",
                TypeInfo(bool),
            ),
        ]

    # The identifier of the provisioning artifact.
    provisioning_artifact_id: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The product identifier.
    product_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The language code.

    #   * `en` \- English (default)

    #   * `jp` \- Japanese

    #   * `zh` \- Chinese
    accept_language: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Indicates whether a verbose level of detail is enabled.
    verbose: bool = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DescribeProvisioningArtifactOutput(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "provisioning_artifact_detail",
                "ProvisioningArtifactDetail",
                TypeInfo(ProvisioningArtifactDetail),
            ),
            (
                "info",
                "Info",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "status",
                "Status",
                TypeInfo(typing.Union[str, Status]),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Information about the provisioning artifact.
    provisioning_artifact_detail: "ProvisioningArtifactDetail" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The URL of the CloudFormation template in Amazon S3.
    info: typing.Dict[str, str] = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The status of the current request.
    status: typing.Union[str, "Status"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class DescribeProvisioningParametersInput(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "product_id",
                "ProductId",
                TypeInfo(str),
            ),
            (
                "provisioning_artifact_id",
                "ProvisioningArtifactId",
                TypeInfo(str),
            ),
            (
                "accept_language",
                "AcceptLanguage",
                TypeInfo(str),
            ),
            (
                "path_id",
                "PathId",
                TypeInfo(str),
            ),
        ]

    # The product identifier.
    product_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The identifier of the provisioning artifact.
    provisioning_artifact_id: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The language code.

    #   * `en` \- English (default)

    #   * `jp` \- Japanese

    #   * `zh` \- Chinese
    accept_language: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The path identifier of the product. This value is optional if the product
    # has a default path, and required if the product has more than one path. To
    # list the paths for a product, use ListLaunchPaths.
    path_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DescribeProvisioningParametersOutput(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "provisioning_artifact_parameters",
                "ProvisioningArtifactParameters",
                TypeInfo(typing.List[ProvisioningArtifactParameter]),
            ),
            (
                "constraint_summaries",
                "ConstraintSummaries",
                TypeInfo(typing.List[ConstraintSummary]),
            ),
            (
                "usage_instructions",
                "UsageInstructions",
                TypeInfo(typing.List[UsageInstruction]),
            ),
            (
                "tag_options",
                "TagOptions",
                TypeInfo(typing.List[TagOptionSummary]),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Information about the parameters used to provision the product.
    provisioning_artifact_parameters: typing.List[
        "ProvisioningArtifactParameter"] = dataclasses.field(
            default=ShapeBase.NOT_SET,
        )

    # Information about the constraints used to provision the product.
    constraint_summaries: typing.List["ConstraintSummary"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Any additional metadata specifically related to the provisioning of the
    # product. For example, see the `Version` field of the CloudFormation
    # template.
    usage_instructions: typing.List["UsageInstruction"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Information about the TagOptions associated with the resource.
    tag_options: typing.List["TagOptionSummary"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class DescribeRecordInput(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "id",
                "Id",
                TypeInfo(str),
            ),
            (
                "accept_language",
                "AcceptLanguage",
                TypeInfo(str),
            ),
            (
                "page_token",
                "PageToken",
                TypeInfo(str),
            ),
            (
                "page_size",
                "PageSize",
                TypeInfo(int),
            ),
        ]

    # The record identifier of the provisioned product. This identifier is
    # returned by the request operation.
    id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The language code.

    #   * `en` \- English (default)

    #   * `jp` \- Japanese

    #   * `zh` \- Chinese
    accept_language: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The page token for the next set of results. To retrieve the first set of
    # results, use null.
    page_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The maximum number of items to return with this call.
    page_size: int = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DescribeRecordOutput(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "record_detail",
                "RecordDetail",
                TypeInfo(RecordDetail),
            ),
            (
                "record_outputs",
                "RecordOutputs",
                TypeInfo(typing.List[RecordOutput]),
            ),
            (
                "next_page_token",
                "NextPageToken",
                TypeInfo(str),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Information about the product.
    record_detail: "RecordDetail" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Information about the product created as the result of a request. For
    # example, the output for a CloudFormation-backed product that creates an S3
    # bucket would include the S3 bucket URL.
    record_outputs: typing.List["RecordOutput"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The page token to use to retrieve the next set of results. If there are no
    # additional results, this value is null.
    next_page_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DescribeTagOptionInput(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "id",
                "Id",
                TypeInfo(str),
            ),
        ]

    # The TagOption identifier.
    id: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DescribeTagOptionOutput(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "tag_option_detail",
                "TagOptionDetail",
                TypeInfo(TagOptionDetail),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Information about the TagOption.
    tag_option_detail: "TagOptionDetail" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class DisassociatePrincipalFromPortfolioInput(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "portfolio_id",
                "PortfolioId",
                TypeInfo(str),
            ),
            (
                "principal_arn",
                "PrincipalARN",
                TypeInfo(str),
            ),
            (
                "accept_language",
                "AcceptLanguage",
                TypeInfo(str),
            ),
        ]

    # The portfolio identifier.
    portfolio_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The ARN of the principal (IAM user, role, or group).
    principal_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The language code.

    #   * `en` \- English (default)

    #   * `jp` \- Japanese

    #   * `zh` \- Chinese
    accept_language: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DisassociatePrincipalFromPortfolioOutput(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class DisassociateProductFromPortfolioInput(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "product_id",
                "ProductId",
                TypeInfo(str),
            ),
            (
                "portfolio_id",
                "PortfolioId",
                TypeInfo(str),
            ),
            (
                "accept_language",
                "AcceptLanguage",
                TypeInfo(str),
            ),
        ]

    # The product identifier.
    product_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The portfolio identifier.
    portfolio_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The language code.

    #   * `en` \- English (default)

    #   * `jp` \- Japanese

    #   * `zh` \- Chinese
    accept_language: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DisassociateProductFromPortfolioOutput(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class DisassociateTagOptionFromResourceInput(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "resource_id",
                "ResourceId",
                TypeInfo(str),
            ),
            (
                "tag_option_id",
                "TagOptionId",
                TypeInfo(str),
            ),
        ]

    # The resource identifier.
    resource_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The TagOption identifier.
    tag_option_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DisassociateTagOptionFromResourceOutput(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class DuplicateResourceException(ShapeBase):
    """
    The specified resource is a duplicate.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


class EvaluationType(str):
    STATIC = "STATIC"
    DYNAMIC = "DYNAMIC"


@dataclasses.dataclass
class ExecuteProvisionedProductPlanInput(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "plan_id",
                "PlanId",
                TypeInfo(str),
            ),
            (
                "idempotency_token",
                "IdempotencyToken",
                TypeInfo(str),
            ),
            (
                "accept_language",
                "AcceptLanguage",
                TypeInfo(str),
            ),
        ]

    # The plan identifier.
    plan_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A unique identifier that you provide to ensure idempotency. If multiple
    # requests differ only by the idempotency token, the same response is
    # returned for each repeated request.
    idempotency_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The language code.

    #   * `en` \- English (default)

    #   * `jp` \- Japanese

    #   * `zh` \- Chinese
    accept_language: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ExecuteProvisionedProductPlanOutput(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "record_detail",
                "RecordDetail",
                TypeInfo(RecordDetail),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Information about the result of provisioning the product.
    record_detail: "RecordDetail" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class InvalidParametersException(ShapeBase):
    """
    One or more parameters provided to the operation are not valid.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class InvalidStateException(ShapeBase):
    """
    An attempt was made to modify a resource that is in a state that is not valid.
    Check your resources to ensure that they are in valid states before retrying the
    operation.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class LaunchPathSummary(ShapeBase):
    """
    Summary information about a product path for a user.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "id",
                "Id",
                TypeInfo(str),
            ),
            (
                "constraint_summaries",
                "ConstraintSummaries",
                TypeInfo(typing.List[ConstraintSummary]),
            ),
            (
                "tags",
                "Tags",
                TypeInfo(typing.List[Tag]),
            ),
            (
                "name",
                "Name",
                TypeInfo(str),
            ),
        ]

    # The identifier of the product path.
    id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The constraints on the portfolio-product relationship.
    constraint_summaries: typing.List["ConstraintSummary"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The tags associated with this product path.
    tags: typing.List["Tag"] = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The name of the portfolio to which the user was assigned.
    name: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class LimitExceededException(ShapeBase):
    """
    The current limits of the service would have been exceeded by this operation.
    Decrease your resource use or increase your service limits and retry the
    operation.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class ListAcceptedPortfolioSharesInput(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "accept_language",
                "AcceptLanguage",
                TypeInfo(str),
            ),
            (
                "page_token",
                "PageToken",
                TypeInfo(str),
            ),
            (
                "page_size",
                "PageSize",
                TypeInfo(int),
            ),
            (
                "portfolio_share_type",
                "PortfolioShareType",
                TypeInfo(typing.Union[str, PortfolioShareType]),
            ),
        ]

    # The language code.

    #   * `en` \- English (default)

    #   * `jp` \- Japanese

    #   * `zh` \- Chinese
    accept_language: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The page token for the next set of results. To retrieve the first set of
    # results, use null.
    page_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The maximum number of items to return with this call.
    page_size: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The type of shared portfolios to list. The default is to list imported
    # portfolios.

    #   * `AWS_SERVICECATALOG` \- List default portfolios

    #   * `IMPORTED` \- List imported portfolios
    portfolio_share_type: typing.Union[str, "PortfolioShareType"
                                      ] = dataclasses.field(
                                          default=ShapeBase.NOT_SET,
                                      )


@dataclasses.dataclass
class ListAcceptedPortfolioSharesOutput(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "portfolio_details",
                "PortfolioDetails",
                TypeInfo(typing.List[PortfolioDetail]),
            ),
            (
                "next_page_token",
                "NextPageToken",
                TypeInfo(str),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Information about the portfolios.
    portfolio_details: typing.List["PortfolioDetail"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The page token to use to retrieve the next set of results. If there are no
    # additional results, this value is null.
    next_page_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    def paginate(
        self,
    ) -> typing.Generator["ListAcceptedPortfolioSharesOutput", None, None]:
        yield from super()._paginate()


@dataclasses.dataclass
class ListConstraintsForPortfolioInput(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "portfolio_id",
                "PortfolioId",
                TypeInfo(str),
            ),
            (
                "accept_language",
                "AcceptLanguage",
                TypeInfo(str),
            ),
            (
                "product_id",
                "ProductId",
                TypeInfo(str),
            ),
            (
                "page_size",
                "PageSize",
                TypeInfo(int),
            ),
            (
                "page_token",
                "PageToken",
                TypeInfo(str),
            ),
        ]

    # The portfolio identifier.
    portfolio_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The language code.

    #   * `en` \- English (default)

    #   * `jp` \- Japanese

    #   * `zh` \- Chinese
    accept_language: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The product identifier.
    product_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The maximum number of items to return with this call.
    page_size: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The page token for the next set of results. To retrieve the first set of
    # results, use null.
    page_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ListConstraintsForPortfolioOutput(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "constraint_details",
                "ConstraintDetails",
                TypeInfo(typing.List[ConstraintDetail]),
            ),
            (
                "next_page_token",
                "NextPageToken",
                TypeInfo(str),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Information about the constraints.
    constraint_details: typing.List["ConstraintDetail"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The page token to use to retrieve the next set of results. If there are no
    # additional results, this value is null.
    next_page_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    def paginate(
        self,
    ) -> typing.Generator["ListConstraintsForPortfolioOutput", None, None]:
        yield from super()._paginate()


@dataclasses.dataclass
class ListLaunchPathsInput(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "product_id",
                "ProductId",
                TypeInfo(str),
            ),
            (
                "accept_language",
                "AcceptLanguage",
                TypeInfo(str),
            ),
            (
                "page_size",
                "PageSize",
                TypeInfo(int),
            ),
            (
                "page_token",
                "PageToken",
                TypeInfo(str),
            ),
        ]

    # The product identifier.
    product_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The language code.

    #   * `en` \- English (default)

    #   * `jp` \- Japanese

    #   * `zh` \- Chinese
    accept_language: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The maximum number of items to return with this call.
    page_size: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The page token for the next set of results. To retrieve the first set of
    # results, use null.
    page_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ListLaunchPathsOutput(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "launch_path_summaries",
                "LaunchPathSummaries",
                TypeInfo(typing.List[LaunchPathSummary]),
            ),
            (
                "next_page_token",
                "NextPageToken",
                TypeInfo(str),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Information about the launch path.
    launch_path_summaries: typing.List["LaunchPathSummary"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The page token to use to retrieve the next set of results. If there are no
    # additional results, this value is null.
    next_page_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    def paginate(self,
                ) -> typing.Generator["ListLaunchPathsOutput", None, None]:
        yield from super()._paginate()


@dataclasses.dataclass
class ListPortfolioAccessInput(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "portfolio_id",
                "PortfolioId",
                TypeInfo(str),
            ),
            (
                "accept_language",
                "AcceptLanguage",
                TypeInfo(str),
            ),
        ]

    # The portfolio identifier.
    portfolio_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The language code.

    #   * `en` \- English (default)

    #   * `jp` \- Japanese

    #   * `zh` \- Chinese
    accept_language: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ListPortfolioAccessOutput(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "account_ids",
                "AccountIds",
                TypeInfo(typing.List[str]),
            ),
            (
                "next_page_token",
                "NextPageToken",
                TypeInfo(str),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Information about the AWS accounts with access to the portfolio.
    account_ids: typing.List[str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The page token to use to retrieve the next set of results. If there are no
    # additional results, this value is null.
    next_page_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ListPortfoliosForProductInput(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "product_id",
                "ProductId",
                TypeInfo(str),
            ),
            (
                "accept_language",
                "AcceptLanguage",
                TypeInfo(str),
            ),
            (
                "page_token",
                "PageToken",
                TypeInfo(str),
            ),
            (
                "page_size",
                "PageSize",
                TypeInfo(int),
            ),
        ]

    # The product identifier.
    product_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The language code.

    #   * `en` \- English (default)

    #   * `jp` \- Japanese

    #   * `zh` \- Chinese
    accept_language: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The page token for the next set of results. To retrieve the first set of
    # results, use null.
    page_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The maximum number of items to return with this call.
    page_size: int = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ListPortfoliosForProductOutput(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "portfolio_details",
                "PortfolioDetails",
                TypeInfo(typing.List[PortfolioDetail]),
            ),
            (
                "next_page_token",
                "NextPageToken",
                TypeInfo(str),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Information about the portfolios.
    portfolio_details: typing.List["PortfolioDetail"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The page token to use to retrieve the next set of results. If there are no
    # additional results, this value is null.
    next_page_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    def paginate(
        self,
    ) -> typing.Generator["ListPortfoliosForProductOutput", None, None]:
        yield from super()._paginate()


@dataclasses.dataclass
class ListPortfoliosInput(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "accept_language",
                "AcceptLanguage",
                TypeInfo(str),
            ),
            (
                "page_token",
                "PageToken",
                TypeInfo(str),
            ),
            (
                "page_size",
                "PageSize",
                TypeInfo(int),
            ),
        ]

    # The language code.

    #   * `en` \- English (default)

    #   * `jp` \- Japanese

    #   * `zh` \- Chinese
    accept_language: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The page token for the next set of results. To retrieve the first set of
    # results, use null.
    page_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The maximum number of items to return with this call.
    page_size: int = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ListPortfoliosOutput(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "portfolio_details",
                "PortfolioDetails",
                TypeInfo(typing.List[PortfolioDetail]),
            ),
            (
                "next_page_token",
                "NextPageToken",
                TypeInfo(str),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Information about the portfolios.
    portfolio_details: typing.List["PortfolioDetail"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The page token to use to retrieve the next set of results. If there are no
    # additional results, this value is null.
    next_page_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    def paginate(self,
                ) -> typing.Generator["ListPortfoliosOutput", None, None]:
        yield from super()._paginate()


@dataclasses.dataclass
class ListPrincipalsForPortfolioInput(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "portfolio_id",
                "PortfolioId",
                TypeInfo(str),
            ),
            (
                "accept_language",
                "AcceptLanguage",
                TypeInfo(str),
            ),
            (
                "page_size",
                "PageSize",
                TypeInfo(int),
            ),
            (
                "page_token",
                "PageToken",
                TypeInfo(str),
            ),
        ]

    # The portfolio identifier.
    portfolio_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The language code.

    #   * `en` \- English (default)

    #   * `jp` \- Japanese

    #   * `zh` \- Chinese
    accept_language: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The maximum number of items to return with this call.
    page_size: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The page token for the next set of results. To retrieve the first set of
    # results, use null.
    page_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ListPrincipalsForPortfolioOutput(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "principals",
                "Principals",
                TypeInfo(typing.List[Principal]),
            ),
            (
                "next_page_token",
                "NextPageToken",
                TypeInfo(str),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The IAM principals (users or roles) associated with the portfolio.
    principals: typing.List["Principal"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The page token to use to retrieve the next set of results. If there are no
    # additional results, this value is null.
    next_page_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    def paginate(
        self,
    ) -> typing.Generator["ListPrincipalsForPortfolioOutput", None, None]:
        yield from super()._paginate()


@dataclasses.dataclass
class ListProvisionedProductPlansInput(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "accept_language",
                "AcceptLanguage",
                TypeInfo(str),
            ),
            (
                "provision_product_id",
                "ProvisionProductId",
                TypeInfo(str),
            ),
            (
                "page_size",
                "PageSize",
                TypeInfo(int),
            ),
            (
                "page_token",
                "PageToken",
                TypeInfo(str),
            ),
            (
                "access_level_filter",
                "AccessLevelFilter",
                TypeInfo(AccessLevelFilter),
            ),
        ]

    # The language code.

    #   * `en` \- English (default)

    #   * `jp` \- Japanese

    #   * `zh` \- Chinese
    accept_language: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The product identifier.
    provision_product_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The maximum number of items to return with this call.
    page_size: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The page token for the next set of results. To retrieve the first set of
    # results, use null.
    page_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The access level to use to obtain results. The default is `User`.
    access_level_filter: "AccessLevelFilter" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class ListProvisionedProductPlansOutput(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "provisioned_product_plans",
                "ProvisionedProductPlans",
                TypeInfo(typing.List[ProvisionedProductPlanSummary]),
            ),
            (
                "next_page_token",
                "NextPageToken",
                TypeInfo(str),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Information about the plans.
    provisioned_product_plans: typing.List["ProvisionedProductPlanSummary"
                                          ] = dataclasses.field(
                                              default=ShapeBase.NOT_SET,
                                          )

    # The page token to use to retrieve the next set of results. If there are no
    # additional results, this value is null.
    next_page_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ListProvisioningArtifactsInput(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "product_id",
                "ProductId",
                TypeInfo(str),
            ),
            (
                "accept_language",
                "AcceptLanguage",
                TypeInfo(str),
            ),
        ]

    # The product identifier.
    product_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The language code.

    #   * `en` \- English (default)

    #   * `jp` \- Japanese

    #   * `zh` \- Chinese
    accept_language: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ListProvisioningArtifactsOutput(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "provisioning_artifact_details",
                "ProvisioningArtifactDetails",
                TypeInfo(typing.List[ProvisioningArtifactDetail]),
            ),
            (
                "next_page_token",
                "NextPageToken",
                TypeInfo(str),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Information about the provisioning artifacts.
    provisioning_artifact_details: typing.List["ProvisioningArtifactDetail"
                                              ] = dataclasses.field(
                                                  default=ShapeBase.NOT_SET,
                                              )

    # The page token to use to retrieve the next set of results. If there are no
    # additional results, this value is null.
    next_page_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ListRecordHistoryInput(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "accept_language",
                "AcceptLanguage",
                TypeInfo(str),
            ),
            (
                "access_level_filter",
                "AccessLevelFilter",
                TypeInfo(AccessLevelFilter),
            ),
            (
                "search_filter",
                "SearchFilter",
                TypeInfo(ListRecordHistorySearchFilter),
            ),
            (
                "page_size",
                "PageSize",
                TypeInfo(int),
            ),
            (
                "page_token",
                "PageToken",
                TypeInfo(str),
            ),
        ]

    # The language code.

    #   * `en` \- English (default)

    #   * `jp` \- Japanese

    #   * `zh` \- Chinese
    accept_language: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The access level to use to obtain results. The default is `User`.
    access_level_filter: "AccessLevelFilter" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The search filter to scope the results.
    search_filter: "ListRecordHistorySearchFilter" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The maximum number of items to return with this call.
    page_size: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The page token for the next set of results. To retrieve the first set of
    # results, use null.
    page_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ListRecordHistoryOutput(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "record_details",
                "RecordDetails",
                TypeInfo(typing.List[RecordDetail]),
            ),
            (
                "next_page_token",
                "NextPageToken",
                TypeInfo(str),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The records, in reverse chronological order.
    record_details: typing.List["RecordDetail"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The page token to use to retrieve the next set of results. If there are no
    # additional results, this value is null.
    next_page_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ListRecordHistorySearchFilter(ShapeBase):
    """
    The search filter to use when listing history records.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "key",
                "Key",
                TypeInfo(str),
            ),
            (
                "value",
                "Value",
                TypeInfo(str),
            ),
        ]

    # The filter key.

    #   * `product` \- Filter results based on the specified product identifier.

    #   * `provisionedproduct` \- Filter results based on the provisioned product identifier.
    key: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The filter value.
    value: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ListResourcesForTagOptionInput(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "tag_option_id",
                "TagOptionId",
                TypeInfo(str),
            ),
            (
                "resource_type",
                "ResourceType",
                TypeInfo(str),
            ),
            (
                "page_size",
                "PageSize",
                TypeInfo(int),
            ),
            (
                "page_token",
                "PageToken",
                TypeInfo(str),
            ),
        ]

    # The TagOption identifier.
    tag_option_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The resource type.

    #   * `Portfolio`

    #   * `Product`
    resource_type: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The maximum number of items to return with this call.
    page_size: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The page token for the next set of results. To retrieve the first set of
    # results, use null.
    page_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ListResourcesForTagOptionOutput(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "resource_details",
                "ResourceDetails",
                TypeInfo(typing.List[ResourceDetail]),
            ),
            (
                "page_token",
                "PageToken",
                TypeInfo(str),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Information about the resources.
    resource_details: typing.List["ResourceDetail"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The page token for the next set of results. To retrieve the first set of
    # results, use null.
    page_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    def paginate(
        self,
    ) -> typing.Generator["ListResourcesForTagOptionOutput", None, None]:
        yield from super()._paginate()


@dataclasses.dataclass
class ListTagOptionsFilters(ShapeBase):
    """
    Filters to use when listing TagOptions.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "key",
                "Key",
                TypeInfo(str),
            ),
            (
                "value",
                "Value",
                TypeInfo(str),
            ),
            (
                "active",
                "Active",
                TypeInfo(bool),
            ),
        ]

    # The TagOption key.
    key: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The TagOption value.
    value: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The active state.
    active: bool = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ListTagOptionsInput(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "filters",
                "Filters",
                TypeInfo(ListTagOptionsFilters),
            ),
            (
                "page_size",
                "PageSize",
                TypeInfo(int),
            ),
            (
                "page_token",
                "PageToken",
                TypeInfo(str),
            ),
        ]

    # The search filters. If no search filters are specified, the output includes
    # all TagOptions.
    filters: "ListTagOptionsFilters" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The maximum number of items to return with this call.
    page_size: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The page token for the next set of results. To retrieve the first set of
    # results, use null.
    page_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ListTagOptionsOutput(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "tag_option_details",
                "TagOptionDetails",
                TypeInfo(typing.List[TagOptionDetail]),
            ),
            (
                "page_token",
                "PageToken",
                TypeInfo(str),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Information about the TagOptions.
    tag_option_details: typing.List["TagOptionDetail"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The page token for the next set of results. To retrieve the first set of
    # results, use null.
    page_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    def paginate(self,
                ) -> typing.Generator["ListTagOptionsOutput", None, None]:
        yield from super()._paginate()


@dataclasses.dataclass
class ParameterConstraints(ShapeBase):
    """
    The constraints that the administrator has put on the parameter.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "allowed_values",
                "AllowedValues",
                TypeInfo(typing.List[str]),
            ),
        ]

    # The values that the administrator has allowed for the parameter.
    allowed_values: typing.List[str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class PortfolioDetail(ShapeBase):
    """
    Information about a portfolio.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "id",
                "Id",
                TypeInfo(str),
            ),
            (
                "arn",
                "ARN",
                TypeInfo(str),
            ),
            (
                "display_name",
                "DisplayName",
                TypeInfo(str),
            ),
            (
                "description",
                "Description",
                TypeInfo(str),
            ),
            (
                "created_time",
                "CreatedTime",
                TypeInfo(datetime.datetime),
            ),
            (
                "provider_name",
                "ProviderName",
                TypeInfo(str),
            ),
        ]

    # The portfolio identifier.
    id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The ARN assigned to the portfolio.
    arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The name to use for display purposes.
    display_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The description of the portfolio.
    description: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The UTC time stamp of the creation time.
    created_time: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The name of the portfolio provider.
    provider_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )


class PortfolioShareType(str):
    IMPORTED = "IMPORTED"
    AWS_SERVICECATALOG = "AWS_SERVICECATALOG"


@dataclasses.dataclass
class Principal(ShapeBase):
    """
    Information about a principal.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "principal_arn",
                "PrincipalARN",
                TypeInfo(str),
            ),
            (
                "principal_type",
                "PrincipalType",
                TypeInfo(typing.Union[str, PrincipalType]),
            ),
        ]

    # The ARN of the principal (IAM user, role, or group).
    principal_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The principal type. The supported value is `IAM`.
    principal_type: typing.Union[str, "PrincipalType"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


class PrincipalType(str):
    IAM = "IAM"


class ProductSource(str):
    ACCOUNT = "ACCOUNT"


class ProductType(str):
    CLOUD_FORMATION_TEMPLATE = "CLOUD_FORMATION_TEMPLATE"
    MARKETPLACE = "MARKETPLACE"


@dataclasses.dataclass
class ProductViewAggregationValue(ShapeBase):
    """
    A single product view aggregation value/count pair, containing metadata about
    each product to which the calling user has access.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "value",
                "Value",
                TypeInfo(str),
            ),
            (
                "approximate_count",
                "ApproximateCount",
                TypeInfo(int),
            ),
        ]

    # The value of the product view aggregation.
    value: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # An approximate count of the products that match the value.
    approximate_count: int = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ProductViewDetail(ShapeBase):
    """
    Information about a product view.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "product_view_summary",
                "ProductViewSummary",
                TypeInfo(ProductViewSummary),
            ),
            (
                "status",
                "Status",
                TypeInfo(typing.Union[str, Status]),
            ),
            (
                "product_arn",
                "ProductARN",
                TypeInfo(str),
            ),
            (
                "created_time",
                "CreatedTime",
                TypeInfo(datetime.datetime),
            ),
        ]

    # Summary information about the product view.
    product_view_summary: "ProductViewSummary" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The status of the product.

    #   * `AVAILABLE` \- The product is ready for use.

    #   * `CREATING` \- Product creation has started; the product is not ready for use.

    #   * `FAILED` \- An action failed.
    status: typing.Union[str, "Status"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The ARN of the product.
    product_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The UTC time stamp of the creation time.
    created_time: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


class ProductViewFilterBy(str):
    FullTextSearch = "FullTextSearch"
    Owner = "Owner"
    ProductType = "ProductType"
    SourceProductId = "SourceProductId"


class ProductViewSortBy(str):
    Title = "Title"
    VersionCount = "VersionCount"
    CreationDate = "CreationDate"


@dataclasses.dataclass
class ProductViewSummary(ShapeBase):
    """
    Summary information about a product view.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "id",
                "Id",
                TypeInfo(str),
            ),
            (
                "product_id",
                "ProductId",
                TypeInfo(str),
            ),
            (
                "name",
                "Name",
                TypeInfo(str),
            ),
            (
                "owner",
                "Owner",
                TypeInfo(str),
            ),
            (
                "short_description",
                "ShortDescription",
                TypeInfo(str),
            ),
            (
                "type",
                "Type",
                TypeInfo(typing.Union[str, ProductType]),
            ),
            (
                "distributor",
                "Distributor",
                TypeInfo(str),
            ),
            (
                "has_default_path",
                "HasDefaultPath",
                TypeInfo(bool),
            ),
            (
                "support_email",
                "SupportEmail",
                TypeInfo(str),
            ),
            (
                "support_description",
                "SupportDescription",
                TypeInfo(str),
            ),
            (
                "support_url",
                "SupportUrl",
                TypeInfo(str),
            ),
        ]

    # The product view identifier.
    id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The product identifier.
    product_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The name of the product.
    name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The owner of the product. Contact the product administrator for the
    # significance of this value.
    owner: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Short description of the product.
    short_description: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The product type. Contact the product administrator for the significance of
    # this value. If this value is `MARKETPLACE`, the product was created by AWS
    # Marketplace.
    type: typing.Union[str, "ProductType"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The distributor of the product. Contact the product administrator for the
    # significance of this value.
    distributor: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Indicates whether the product has a default path. If the product does not
    # have a default path, call ListLaunchPaths to disambiguate between paths.
    # Otherwise, ListLaunchPaths is not required, and the output of
    # ProductViewSummary can be used directly with
    # DescribeProvisioningParameters.
    has_default_path: bool = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The email contact information to obtain support for this Product.
    support_email: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The description of the support for this Product.
    support_description: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The URL information to obtain support for this Product.
    support_url: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ProvisionProductInput(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "product_id",
                "ProductId",
                TypeInfo(str),
            ),
            (
                "provisioning_artifact_id",
                "ProvisioningArtifactId",
                TypeInfo(str),
            ),
            (
                "provisioned_product_name",
                "ProvisionedProductName",
                TypeInfo(str),
            ),
            (
                "provision_token",
                "ProvisionToken",
                TypeInfo(str),
            ),
            (
                "accept_language",
                "AcceptLanguage",
                TypeInfo(str),
            ),
            (
                "path_id",
                "PathId",
                TypeInfo(str),
            ),
            (
                "provisioning_parameters",
                "ProvisioningParameters",
                TypeInfo(typing.List[ProvisioningParameter]),
            ),
            (
                "tags",
                "Tags",
                TypeInfo(typing.List[Tag]),
            ),
            (
                "notification_arns",
                "NotificationArns",
                TypeInfo(typing.List[str]),
            ),
        ]

    # The product identifier.
    product_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The identifier of the provisioning artifact.
    provisioning_artifact_id: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A user-friendly name for the provisioned product. This value must be unique
    # for the AWS account and cannot be updated after the product is provisioned.
    provisioned_product_name: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # An idempotency token that uniquely identifies the provisioning request.
    provision_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The language code.

    #   * `en` \- English (default)

    #   * `jp` \- Japanese

    #   * `zh` \- Chinese
    accept_language: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The path identifier of the product. This value is optional if the product
    # has a default path, and required if the product has more than one path. To
    # list the paths for a product, use ListLaunchPaths.
    path_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Parameters specified by the administrator that are required for
    # provisioning the product.
    provisioning_parameters: typing.List["ProvisioningParameter"
                                        ] = dataclasses.field(
                                            default=ShapeBase.NOT_SET,
                                        )

    # One or more tags.
    tags: typing.List["Tag"] = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Passed to CloudFormation. The SNS topic ARNs to which to publish stack-
    # related events.
    notification_arns: typing.List[str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class ProvisionProductOutput(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "record_detail",
                "RecordDetail",
                TypeInfo(RecordDetail),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Information about the result of provisioning the product.
    record_detail: "RecordDetail" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class ProvisionedProductAttribute(ShapeBase):
    """
    Information about a provisioned product.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "name",
                "Name",
                TypeInfo(str),
            ),
            (
                "arn",
                "Arn",
                TypeInfo(str),
            ),
            (
                "type",
                "Type",
                TypeInfo(str),
            ),
            (
                "id",
                "Id",
                TypeInfo(str),
            ),
            (
                "status",
                "Status",
                TypeInfo(typing.Union[str, ProvisionedProductStatus]),
            ),
            (
                "status_message",
                "StatusMessage",
                TypeInfo(str),
            ),
            (
                "created_time",
                "CreatedTime",
                TypeInfo(datetime.datetime),
            ),
            (
                "idempotency_token",
                "IdempotencyToken",
                TypeInfo(str),
            ),
            (
                "last_record_id",
                "LastRecordId",
                TypeInfo(str),
            ),
            (
                "tags",
                "Tags",
                TypeInfo(typing.List[Tag]),
            ),
            (
                "physical_id",
                "PhysicalId",
                TypeInfo(str),
            ),
            (
                "product_id",
                "ProductId",
                TypeInfo(str),
            ),
            (
                "provisioning_artifact_id",
                "ProvisioningArtifactId",
                TypeInfo(str),
            ),
            (
                "user_arn",
                "UserArn",
                TypeInfo(str),
            ),
            (
                "user_arn_session",
                "UserArnSession",
                TypeInfo(str),
            ),
        ]

    # The user-friendly name of the provisioned product.
    name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The ARN of the provisioned product.
    arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The type of provisioned product. The supported value is `CFN_STACK`.
    type: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The identifier of the provisioned product.
    id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The current status of the provisioned product.

    #   * `AVAILABLE` \- Stable state, ready to perform any operation. The most recent operation succeeded and completed.

    #   * `UNDER_CHANGE` \- Transitive state, operations performed might not have valid results. Wait for an `AVAILABLE` status before performing operations.

    #   * `TAINTED` \- Stable state, ready to perform any operation. The stack has completed the requested operation but is not exactly what was requested. For example, a request to update to a new version failed and the stack rolled back to the current version.

    #   * `ERROR` \- An unexpected error occurred, the provisioned product exists but the stack is not running. For example, CloudFormation received a parameter value that was not valid and could not launch the stack.
    status: typing.Union[str, "ProvisionedProductStatus"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The current status message of the provisioned product.
    status_message: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The UTC time stamp of the creation time.
    created_time: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A unique identifier that you provide to ensure idempotency. If multiple
    # requests differ only by the idempotency token, the same response is
    # returned for each repeated request.
    idempotency_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The record identifier of the last request performed on this provisioned
    # product.
    last_record_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # One or more tags.
    tags: typing.List["Tag"] = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The assigned identifier for the resource, such as an EC2 instance ID or an
    # S3 bucket name.
    physical_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The product identifier.
    product_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The identifier of the provisioning artifact.
    provisioning_artifact_id: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The Amazon Resource Name (ARN) of the IAM user.
    user_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The ARN of the IAM user in the session. This ARN might contain a session
    # ID.
    user_arn_session: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ProvisionedProductDetail(ShapeBase):
    """
    Information about a provisioned product.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "name",
                "Name",
                TypeInfo(str),
            ),
            (
                "arn",
                "Arn",
                TypeInfo(str),
            ),
            (
                "type",
                "Type",
                TypeInfo(str),
            ),
            (
                "id",
                "Id",
                TypeInfo(str),
            ),
            (
                "status",
                "Status",
                TypeInfo(typing.Union[str, ProvisionedProductStatus]),
            ),
            (
                "status_message",
                "StatusMessage",
                TypeInfo(str),
            ),
            (
                "created_time",
                "CreatedTime",
                TypeInfo(datetime.datetime),
            ),
            (
                "idempotency_token",
                "IdempotencyToken",
                TypeInfo(str),
            ),
            (
                "last_record_id",
                "LastRecordId",
                TypeInfo(str),
            ),
        ]

    # The user-friendly name of the provisioned product.
    name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The ARN of the provisioned product.
    arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The type of provisioned product. The supported value is `CFN_STACK`.
    type: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The identifier of the provisioned product.
    id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The current status of the provisioned product.

    #   * `AVAILABLE` \- Stable state, ready to perform any operation. The most recent operation succeeded and completed.

    #   * `UNDER_CHANGE` \- Transitive state, operations performed might not have valid results. Wait for an `AVAILABLE` status before performing operations.

    #   * `TAINTED` \- Stable state, ready to perform any operation. The stack has completed the requested operation but is not exactly what was requested. For example, a request to update to a new version failed and the stack rolled back to the current version.

    #   * `ERROR` \- An unexpected error occurred, the provisioned product exists but the stack is not running. For example, CloudFormation received a parameter value that was not valid and could not launch the stack.
    status: typing.Union[str, "ProvisionedProductStatus"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The current status message of the provisioned product.
    status_message: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The UTC time stamp of the creation time.
    created_time: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A unique identifier that you provide to ensure idempotency. If multiple
    # requests differ only by the idempotency token, the same response is
    # returned for each repeated request.
    idempotency_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The record identifier of the last request performed on this provisioned
    # product.
    last_record_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ProvisionedProductPlanDetails(ShapeBase):
    """
    Information about a plan.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "created_time",
                "CreatedTime",
                TypeInfo(datetime.datetime),
            ),
            (
                "path_id",
                "PathId",
                TypeInfo(str),
            ),
            (
                "product_id",
                "ProductId",
                TypeInfo(str),
            ),
            (
                "plan_name",
                "PlanName",
                TypeInfo(str),
            ),
            (
                "plan_id",
                "PlanId",
                TypeInfo(str),
            ),
            (
                "provision_product_id",
                "ProvisionProductId",
                TypeInfo(str),
            ),
            (
                "provision_product_name",
                "ProvisionProductName",
                TypeInfo(str),
            ),
            (
                "plan_type",
                "PlanType",
                TypeInfo(typing.Union[str, ProvisionedProductPlanType]),
            ),
            (
                "provisioning_artifact_id",
                "ProvisioningArtifactId",
                TypeInfo(str),
            ),
            (
                "status",
                "Status",
                TypeInfo(typing.Union[str, ProvisionedProductPlanStatus]),
            ),
            (
                "updated_time",
                "UpdatedTime",
                TypeInfo(datetime.datetime),
            ),
            (
                "notification_arns",
                "NotificationArns",
                TypeInfo(typing.List[str]),
            ),
            (
                "provisioning_parameters",
                "ProvisioningParameters",
                TypeInfo(typing.List[UpdateProvisioningParameter]),
            ),
            (
                "tags",
                "Tags",
                TypeInfo(typing.List[Tag]),
            ),
            (
                "status_message",
                "StatusMessage",
                TypeInfo(str),
            ),
        ]

    # The UTC time stamp of the creation time.
    created_time: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The path identifier of the product. This value is optional if the product
    # has a default path, and required if the product has more than one path. To
    # list the paths for a product, use ListLaunchPaths.
    path_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The product identifier.
    product_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The name of the plan.
    plan_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The plan identifier.
    plan_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The product identifier.
    provision_product_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The user-friendly name of the provisioned product.
    provision_product_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The plan type.
    plan_type: typing.Union[str, "ProvisionedProductPlanType"
                           ] = dataclasses.field(
                               default=ShapeBase.NOT_SET,
                           )

    # The identifier of the provisioning artifact.
    provisioning_artifact_id: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The status.
    status: typing.Union[str, "ProvisionedProductPlanStatus"
                        ] = dataclasses.field(
                            default=ShapeBase.NOT_SET,
                        )

    # The time when the plan was last updated.
    updated_time: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Passed to CloudFormation. The SNS topic ARNs to which to publish stack-
    # related events.
    notification_arns: typing.List[str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Parameters specified by the administrator that are required for
    # provisioning the product.
    provisioning_parameters: typing.List["UpdateProvisioningParameter"
                                        ] = dataclasses.field(
                                            default=ShapeBase.NOT_SET,
                                        )

    # One or more tags.
    tags: typing.List["Tag"] = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The status message.
    status_message: str = dataclasses.field(default=ShapeBase.NOT_SET, )


class ProvisionedProductPlanStatus(str):
    CREATE_IN_PROGRESS = "CREATE_IN_PROGRESS"
    CREATE_SUCCESS = "CREATE_SUCCESS"
    CREATE_FAILED = "CREATE_FAILED"
    EXECUTE_IN_PROGRESS = "EXECUTE_IN_PROGRESS"
    EXECUTE_SUCCESS = "EXECUTE_SUCCESS"
    EXECUTE_FAILED = "EXECUTE_FAILED"


@dataclasses.dataclass
class ProvisionedProductPlanSummary(ShapeBase):
    """
    Summary information about a plan.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "plan_name",
                "PlanName",
                TypeInfo(str),
            ),
            (
                "plan_id",
                "PlanId",
                TypeInfo(str),
            ),
            (
                "provision_product_id",
                "ProvisionProductId",
                TypeInfo(str),
            ),
            (
                "provision_product_name",
                "ProvisionProductName",
                TypeInfo(str),
            ),
            (
                "plan_type",
                "PlanType",
                TypeInfo(typing.Union[str, ProvisionedProductPlanType]),
            ),
            (
                "provisioning_artifact_id",
                "ProvisioningArtifactId",
                TypeInfo(str),
            ),
        ]

    # The name of the plan.
    plan_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The plan identifier.
    plan_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The product identifier.
    provision_product_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The user-friendly name of the provisioned product.
    provision_product_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The plan type.
    plan_type: typing.Union[str, "ProvisionedProductPlanType"
                           ] = dataclasses.field(
                               default=ShapeBase.NOT_SET,
                           )

    # The identifier of the provisioning artifact.
    provisioning_artifact_id: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


class ProvisionedProductPlanType(str):
    CLOUDFORMATION = "CLOUDFORMATION"


class ProvisionedProductStatus(str):
    AVAILABLE = "AVAILABLE"
    UNDER_CHANGE = "UNDER_CHANGE"
    TAINTED = "TAINTED"
    ERROR = "ERROR"
    PLAN_IN_PROGRESS = "PLAN_IN_PROGRESS"


class ProvisionedProductViewFilterBy(str):
    SearchQuery = "SearchQuery"


@dataclasses.dataclass
class ProvisioningArtifact(ShapeBase):
    """
    Information about a provisioning artifact. A provisioning artifact is also known
    as a product version.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "id",
                "Id",
                TypeInfo(str),
            ),
            (
                "name",
                "Name",
                TypeInfo(str),
            ),
            (
                "description",
                "Description",
                TypeInfo(str),
            ),
            (
                "created_time",
                "CreatedTime",
                TypeInfo(datetime.datetime),
            ),
        ]

    # The identifier of the provisioning artifact.
    id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The name of the provisioning artifact.
    name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The description of the provisioning artifact.
    description: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The UTC time stamp of the creation time.
    created_time: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class ProvisioningArtifactDetail(ShapeBase):
    """
    Information about a provisioning artifact (also known as a version) for a
    product.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "id",
                "Id",
                TypeInfo(str),
            ),
            (
                "name",
                "Name",
                TypeInfo(str),
            ),
            (
                "description",
                "Description",
                TypeInfo(str),
            ),
            (
                "type",
                "Type",
                TypeInfo(typing.Union[str, ProvisioningArtifactType]),
            ),
            (
                "created_time",
                "CreatedTime",
                TypeInfo(datetime.datetime),
            ),
            (
                "active",
                "Active",
                TypeInfo(bool),
            ),
        ]

    # The identifier of the provisioning artifact.
    id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The name of the provisioning artifact.
    name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The description of the provisioning artifact.
    description: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The type of provisioning artifact.

    #   * `CLOUD_FORMATION_TEMPLATE` \- AWS CloudFormation template

    #   * `MARKETPLACE_AMI` \- AWS Marketplace AMI

    #   * `MARKETPLACE_CAR` \- AWS Marketplace Clusters and AWS Resources
    type: typing.Union[str, "ProvisioningArtifactType"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The UTC time stamp of the creation time.
    created_time: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Indicates whether the product version is active.
    active: bool = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ProvisioningArtifactParameter(ShapeBase):
    """
    Information about a parameter used to provision a product.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "parameter_key",
                "ParameterKey",
                TypeInfo(str),
            ),
            (
                "default_value",
                "DefaultValue",
                TypeInfo(str),
            ),
            (
                "parameter_type",
                "ParameterType",
                TypeInfo(str),
            ),
            (
                "is_no_echo",
                "IsNoEcho",
                TypeInfo(bool),
            ),
            (
                "description",
                "Description",
                TypeInfo(str),
            ),
            (
                "parameter_constraints",
                "ParameterConstraints",
                TypeInfo(ParameterConstraints),
            ),
        ]

    # The parameter key.
    parameter_key: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The default value.
    default_value: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The parameter type.
    parameter_type: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # If this value is true, the value for this parameter is obfuscated from view
    # when the parameter is retrieved. This parameter is used to hide sensitive
    # information.
    is_no_echo: bool = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The description of the parameter.
    description: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Constraints that the administrator has put on a parameter.
    parameter_constraints: "ParameterConstraints" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class ProvisioningArtifactProperties(ShapeBase):
    """
    Information about a provisioning artifact (also known as a version) for a
    product.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "info",
                "Info",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "name",
                "Name",
                TypeInfo(str),
            ),
            (
                "description",
                "Description",
                TypeInfo(str),
            ),
            (
                "type",
                "Type",
                TypeInfo(typing.Union[str, ProvisioningArtifactType]),
            ),
        ]

    # The URL of the CloudFormation template in Amazon S3. Specify the URL in
    # JSON format as follows:

    # `"LoadTemplateFromURL": "https://s3.amazonaws.com/cf-templates-
    # ozkq9d3hgiq2-us-east-1/..."`
    info: typing.Dict[str, str] = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The name of the provisioning artifact (for example, v1 v2beta). No spaces
    # are allowed.
    name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The description of the provisioning artifact, including how it differs from
    # the previous provisioning artifact.
    description: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The type of provisioning artifact.

    #   * `CLOUD_FORMATION_TEMPLATE` \- AWS CloudFormation template

    #   * `MARKETPLACE_AMI` \- AWS Marketplace AMI

    #   * `MARKETPLACE_CAR` \- AWS Marketplace Clusters and AWS Resources
    type: typing.Union[str, "ProvisioningArtifactType"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


class ProvisioningArtifactPropertyName(str):
    Id = "Id"


@dataclasses.dataclass
class ProvisioningArtifactSummary(ShapeBase):
    """
    Summary information about a provisioning artifact (also known as a version) for
    a product.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "id",
                "Id",
                TypeInfo(str),
            ),
            (
                "name",
                "Name",
                TypeInfo(str),
            ),
            (
                "description",
                "Description",
                TypeInfo(str),
            ),
            (
                "created_time",
                "CreatedTime",
                TypeInfo(datetime.datetime),
            ),
            (
                "provisioning_artifact_metadata",
                "ProvisioningArtifactMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
        ]

    # The identifier of the provisioning artifact.
    id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The name of the provisioning artifact.
    name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The description of the provisioning artifact.
    description: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The UTC time stamp of the creation time.
    created_time: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The metadata for the provisioning artifact. This is used with AWS
    # Marketplace products.
    provisioning_artifact_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


class ProvisioningArtifactType(str):
    CLOUD_FORMATION_TEMPLATE = "CLOUD_FORMATION_TEMPLATE"
    MARKETPLACE_AMI = "MARKETPLACE_AMI"
    MARKETPLACE_CAR = "MARKETPLACE_CAR"


@dataclasses.dataclass
class ProvisioningParameter(ShapeBase):
    """
    Information about a parameter used to provision a product.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "key",
                "Key",
                TypeInfo(str),
            ),
            (
                "value",
                "Value",
                TypeInfo(str),
            ),
        ]

    # The parameter key.
    key: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The parameter value.
    value: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class RecordDetail(ShapeBase):
    """
    Information about a request operation.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "record_id",
                "RecordId",
                TypeInfo(str),
            ),
            (
                "provisioned_product_name",
                "ProvisionedProductName",
                TypeInfo(str),
            ),
            (
                "status",
                "Status",
                TypeInfo(typing.Union[str, RecordStatus]),
            ),
            (
                "created_time",
                "CreatedTime",
                TypeInfo(datetime.datetime),
            ),
            (
                "updated_time",
                "UpdatedTime",
                TypeInfo(datetime.datetime),
            ),
            (
                "provisioned_product_type",
                "ProvisionedProductType",
                TypeInfo(str),
            ),
            (
                "record_type",
                "RecordType",
                TypeInfo(str),
            ),
            (
                "provisioned_product_id",
                "ProvisionedProductId",
                TypeInfo(str),
            ),
            (
                "product_id",
                "ProductId",
                TypeInfo(str),
            ),
            (
                "provisioning_artifact_id",
                "ProvisioningArtifactId",
                TypeInfo(str),
            ),
            (
                "path_id",
                "PathId",
                TypeInfo(str),
            ),
            (
                "record_errors",
                "RecordErrors",
                TypeInfo(typing.List[RecordError]),
            ),
            (
                "record_tags",
                "RecordTags",
                TypeInfo(typing.List[RecordTag]),
            ),
        ]

    # The identifier of the record.
    record_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The user-friendly name of the provisioned product.
    provisioned_product_name: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The status of the provisioned product.

    #   * `CREATED` \- The request was created but the operation has not started.

    #   * `IN_PROGRESS` \- The requested operation is in progress.

    #   * `IN_PROGRESS_IN_ERROR` \- The provisioned product is under change but the requested operation failed and some remediation is occurring. For example, a rollback.

    #   * `SUCCEEDED` \- The requested operation has successfully completed.

    #   * `FAILED` \- The requested operation has unsuccessfully completed. Investigate using the error messages returned.
    status: typing.Union[str, "RecordStatus"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The UTC time stamp of the creation time.
    created_time: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The time when the record was last updated.
    updated_time: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The type of provisioned product. The supported value is `CFN_STACK`.
    provisioned_product_type: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The record type.

    #   * `PROVISION_PRODUCT`

    #   * `UPDATE_PROVISIONED_PRODUCT`

    #   * `TERMINATE_PROVISIONED_PRODUCT`
    record_type: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The identifier of the provisioned product.
    provisioned_product_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The product identifier.
    product_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The identifier of the provisioning artifact.
    provisioning_artifact_id: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The path identifier.
    path_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The errors that occurred.
    record_errors: typing.List["RecordError"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # One or more tags.
    record_tags: typing.List["RecordTag"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class RecordError(ShapeBase):
    """
    The error code and description resulting from an operation.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "code",
                "Code",
                TypeInfo(str),
            ),
            (
                "description",
                "Description",
                TypeInfo(str),
            ),
        ]

    # The numeric value of the error.
    code: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The description of the error.
    description: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class RecordOutput(ShapeBase):
    """
    The output for the product created as the result of a request. For example, the
    output for a CloudFormation-backed product that creates an S3 bucket would
    include the S3 bucket URL.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "output_key",
                "OutputKey",
                TypeInfo(str),
            ),
            (
                "output_value",
                "OutputValue",
                TypeInfo(str),
            ),
            (
                "description",
                "Description",
                TypeInfo(str),
            ),
        ]

    # The output key.
    output_key: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The output value.
    output_value: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The description of the output.
    description: str = dataclasses.field(default=ShapeBase.NOT_SET, )


class RecordStatus(str):
    CREATED = "CREATED"
    IN_PROGRESS = "IN_PROGRESS"
    IN_PROGRESS_IN_ERROR = "IN_PROGRESS_IN_ERROR"
    SUCCEEDED = "SUCCEEDED"
    FAILED = "FAILED"


@dataclasses.dataclass
class RecordTag(ShapeBase):
    """
    Information about a tag, which is a key-value pair.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "key",
                "Key",
                TypeInfo(str),
            ),
            (
                "value",
                "Value",
                TypeInfo(str),
            ),
        ]

    # The key for this tag.
    key: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The value for this tag.
    value: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class RejectPortfolioShareInput(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "portfolio_id",
                "PortfolioId",
                TypeInfo(str),
            ),
            (
                "accept_language",
                "AcceptLanguage",
                TypeInfo(str),
            ),
        ]

    # The portfolio identifier.
    portfolio_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The language code.

    #   * `en` \- English (default)

    #   * `jp` \- Japanese

    #   * `zh` \- Chinese
    accept_language: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class RejectPortfolioShareOutput(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


class Replacement(str):
    TRUE = "TRUE"
    FALSE = "FALSE"
    CONDITIONAL = "CONDITIONAL"


class RequiresRecreation(str):
    NEVER = "NEVER"
    CONDITIONALLY = "CONDITIONALLY"
    ALWAYS = "ALWAYS"


class ResourceAttribute(str):
    PROPERTIES = "PROPERTIES"
    METADATA = "METADATA"
    CREATIONPOLICY = "CREATIONPOLICY"
    UPDATEPOLICY = "UPDATEPOLICY"
    DELETIONPOLICY = "DELETIONPOLICY"
    TAGS = "TAGS"


@dataclasses.dataclass
class ResourceChange(ShapeBase):
    """
    Information about a resource change that will occur when a plan is executed.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "action",
                "Action",
                TypeInfo(typing.Union[str, ChangeAction]),
            ),
            (
                "logical_resource_id",
                "LogicalResourceId",
                TypeInfo(str),
            ),
            (
                "physical_resource_id",
                "PhysicalResourceId",
                TypeInfo(str),
            ),
            (
                "resource_type",
                "ResourceType",
                TypeInfo(str),
            ),
            (
                "replacement",
                "Replacement",
                TypeInfo(typing.Union[str, Replacement]),
            ),
            (
                "scope",
                "Scope",
                TypeInfo(typing.List[typing.Union[str, ResourceAttribute]]),
            ),
            (
                "details",
                "Details",
                TypeInfo(typing.List[ResourceChangeDetail]),
            ),
        ]

    # The change action.
    action: typing.Union[str, "ChangeAction"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The ID of the resource, as defined in the CloudFormation template.
    logical_resource_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The ID of the resource, if it was already created.
    physical_resource_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The type of resource.
    resource_type: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # If the change type is `Modify`, indicates whether the existing resource is
    # deleted and replaced with a new one.
    replacement: typing.Union[str, "Replacement"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The change scope.
    scope: typing.List[typing.Union[str, "ResourceAttribute"]
                      ] = dataclasses.field(
                          default=ShapeBase.NOT_SET,
                      )

    # Information about the resource changes.
    details: typing.List["ResourceChangeDetail"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class ResourceChangeDetail(ShapeBase):
    """
    Information about a change to a resource attribute.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "target",
                "Target",
                TypeInfo(ResourceTargetDefinition),
            ),
            (
                "evaluation",
                "Evaluation",
                TypeInfo(typing.Union[str, EvaluationType]),
            ),
            (
                "causing_entity",
                "CausingEntity",
                TypeInfo(str),
            ),
        ]

    # Information about the resource attribute to be modified.
    target: "ResourceTargetDefinition" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # For static evaluations, the value of the resource attribute will change and
    # the new value is known. For dynamic evaluations, the value might change,
    # and any new value will be determined when the plan is updated.
    evaluation: typing.Union[str, "EvaluationType"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The ID of the entity that caused the change.
    causing_entity: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ResourceDetail(ShapeBase):
    """
    Information about a resource.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "id",
                "Id",
                TypeInfo(str),
            ),
            (
                "arn",
                "ARN",
                TypeInfo(str),
            ),
            (
                "name",
                "Name",
                TypeInfo(str),
            ),
            (
                "description",
                "Description",
                TypeInfo(str),
            ),
            (
                "created_time",
                "CreatedTime",
                TypeInfo(datetime.datetime),
            ),
        ]

    # The identifier of the resource.
    id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The ARN of the resource.
    arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The name of the resource.
    name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The description of the resource.
    description: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The creation time of the resource.
    created_time: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class ResourceInUseException(ShapeBase):
    """
    A resource that is currently in use. Ensure that the resource is not in use and
    retry the operation.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class ResourceNotFoundException(ShapeBase):
    """
    The specified resource was not found.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class ResourceTargetDefinition(ShapeBase):
    """
    Information about a change to a resource attribute.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "attribute",
                "Attribute",
                TypeInfo(typing.Union[str, ResourceAttribute]),
            ),
            (
                "name",
                "Name",
                TypeInfo(str),
            ),
            (
                "requires_recreation",
                "RequiresRecreation",
                TypeInfo(typing.Union[str, RequiresRecreation]),
            ),
        ]

    # The attribute to be changed.
    attribute: typing.Union[str, "ResourceAttribute"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # If the attribute is `Properties`, the value is the name of the property.
    # Otherwise, the value is null.
    name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # If the attribute is `Properties`, indicates whether a change to this
    # property causes the resource to be re-created.
    requires_recreation: typing.Union[str, "RequiresRecreation"
                                     ] = dataclasses.field(
                                         default=ShapeBase.NOT_SET,
                                     )


@dataclasses.dataclass
class ScanProvisionedProductsInput(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "accept_language",
                "AcceptLanguage",
                TypeInfo(str),
            ),
            (
                "access_level_filter",
                "AccessLevelFilter",
                TypeInfo(AccessLevelFilter),
            ),
            (
                "page_size",
                "PageSize",
                TypeInfo(int),
            ),
            (
                "page_token",
                "PageToken",
                TypeInfo(str),
            ),
        ]

    # The language code.

    #   * `en` \- English (default)

    #   * `jp` \- Japanese

    #   * `zh` \- Chinese
    accept_language: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The access level to use to obtain results. The default is `User`.
    access_level_filter: "AccessLevelFilter" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The maximum number of items to return with this call.
    page_size: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The page token for the next set of results. To retrieve the first set of
    # results, use null.
    page_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ScanProvisionedProductsOutput(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "provisioned_products",
                "ProvisionedProducts",
                TypeInfo(typing.List[ProvisionedProductDetail]),
            ),
            (
                "next_page_token",
                "NextPageToken",
                TypeInfo(str),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Information about the provisioned products.
    provisioned_products: typing.List["ProvisionedProductDetail"
                                     ] = dataclasses.field(
                                         default=ShapeBase.NOT_SET,
                                     )

    # The page token to use to retrieve the next set of results. If there are no
    # additional results, this value is null.
    next_page_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class SearchProductsAsAdminInput(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "accept_language",
                "AcceptLanguage",
                TypeInfo(str),
            ),
            (
                "portfolio_id",
                "PortfolioId",
                TypeInfo(str),
            ),
            (
                "filters",
                "Filters",
                TypeInfo(
                    typing.Dict[typing.Union[str, ProductViewFilterBy], typing.
                                List[str]]
                ),
            ),
            (
                "sort_by",
                "SortBy",
                TypeInfo(typing.Union[str, ProductViewSortBy]),
            ),
            (
                "sort_order",
                "SortOrder",
                TypeInfo(typing.Union[str, SortOrder]),
            ),
            (
                "page_token",
                "PageToken",
                TypeInfo(str),
            ),
            (
                "page_size",
                "PageSize",
                TypeInfo(int),
            ),
            (
                "product_source",
                "ProductSource",
                TypeInfo(typing.Union[str, ProductSource]),
            ),
        ]

    # The language code.

    #   * `en` \- English (default)

    #   * `jp` \- Japanese

    #   * `zh` \- Chinese
    accept_language: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The portfolio identifier.
    portfolio_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The search filters. If no search filters are specified, the output includes
    # all products to which the administrator has access.
    filters: typing.Dict[typing.Union[str, "ProductViewFilterBy"], typing.
                         List[str]] = dataclasses.field(
                             default=ShapeBase.NOT_SET,
                         )

    # The sort field. If no value is specified, the results are not sorted.
    sort_by: typing.Union[str, "ProductViewSortBy"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The sort order. If no value is specified, the results are not sorted.
    sort_order: typing.Union[str, "SortOrder"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The page token for the next set of results. To retrieve the first set of
    # results, use null.
    page_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The maximum number of items to return with this call.
    page_size: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Access level of the source of the product.
    product_source: typing.Union[str, "ProductSource"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class SearchProductsAsAdminOutput(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "product_view_details",
                "ProductViewDetails",
                TypeInfo(typing.List[ProductViewDetail]),
            ),
            (
                "next_page_token",
                "NextPageToken",
                TypeInfo(str),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Information about the product views.
    product_view_details: typing.List["ProductViewDetail"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The page token to use to retrieve the next set of results. If there are no
    # additional results, this value is null.
    next_page_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    def paginate(
        self,
    ) -> typing.Generator["SearchProductsAsAdminOutput", None, None]:
        yield from super()._paginate()


@dataclasses.dataclass
class SearchProductsInput(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "accept_language",
                "AcceptLanguage",
                TypeInfo(str),
            ),
            (
                "filters",
                "Filters",
                TypeInfo(
                    typing.Dict[typing.Union[str, ProductViewFilterBy], typing.
                                List[str]]
                ),
            ),
            (
                "page_size",
                "PageSize",
                TypeInfo(int),
            ),
            (
                "sort_by",
                "SortBy",
                TypeInfo(typing.Union[str, ProductViewSortBy]),
            ),
            (
                "sort_order",
                "SortOrder",
                TypeInfo(typing.Union[str, SortOrder]),
            ),
            (
                "page_token",
                "PageToken",
                TypeInfo(str),
            ),
        ]

    # The language code.

    #   * `en` \- English (default)

    #   * `jp` \- Japanese

    #   * `zh` \- Chinese
    accept_language: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The search filters. If no search filters are specified, the output includes
    # all products to which the caller has access.
    filters: typing.Dict[typing.Union[str, "ProductViewFilterBy"], typing.
                         List[str]] = dataclasses.field(
                             default=ShapeBase.NOT_SET,
                         )

    # The maximum number of items to return with this call.
    page_size: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The sort field. If no value is specified, the results are not sorted.
    sort_by: typing.Union[str, "ProductViewSortBy"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The sort order. If no value is specified, the results are not sorted.
    sort_order: typing.Union[str, "SortOrder"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The page token for the next set of results. To retrieve the first set of
    # results, use null.
    page_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class SearchProductsOutput(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "product_view_summaries",
                "ProductViewSummaries",
                TypeInfo(typing.List[ProductViewSummary]),
            ),
            (
                "product_view_aggregations",
                "ProductViewAggregations",
                TypeInfo(
                    typing.Dict[str, typing.List[ProductViewAggregationValue]]
                ),
            ),
            (
                "next_page_token",
                "NextPageToken",
                TypeInfo(str),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Information about the product views.
    product_view_summaries: typing.List["ProductViewSummary"
                                       ] = dataclasses.field(
                                           default=ShapeBase.NOT_SET,
                                       )

    # The product view aggregations.
    product_view_aggregations: typing.Dict[
        str, typing.List["ProductViewAggregationValue"]] = dataclasses.field(
            default=ShapeBase.NOT_SET,
        )

    # The page token to use to retrieve the next set of results. If there are no
    # additional results, this value is null.
    next_page_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class SearchProvisionedProductsInput(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "accept_language",
                "AcceptLanguage",
                TypeInfo(str),
            ),
            (
                "access_level_filter",
                "AccessLevelFilter",
                TypeInfo(AccessLevelFilter),
            ),
            (
                "filters",
                "Filters",
                TypeInfo(
                    typing.
                    Dict[typing.Union[str, ProvisionedProductViewFilterBy],
                         typing.List[str]]
                ),
            ),
            (
                "sort_by",
                "SortBy",
                TypeInfo(str),
            ),
            (
                "sort_order",
                "SortOrder",
                TypeInfo(typing.Union[str, SortOrder]),
            ),
            (
                "page_size",
                "PageSize",
                TypeInfo(int),
            ),
            (
                "page_token",
                "PageToken",
                TypeInfo(str),
            ),
        ]

    # The language code.

    #   * `en` \- English (default)

    #   * `jp` \- Japanese

    #   * `zh` \- Chinese
    accept_language: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The access level to use to obtain results. The default is `User`.
    access_level_filter: "AccessLevelFilter" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The search filters.

    # When the key is `SearchQuery`, the searchable fields are `arn`,
    # `createdTime`, `id`, `lastRecordId`, `idempotencyToken`, `name`,
    # `physicalId`, `productId`, `provisioningArtifact`, `type`, `status`,
    # `tags`, `userArn`, and `userArnSession`.

    # Example: `"SearchQuery":["status:AVAILABLE"]`
    filters: typing.Dict[typing.Union[str, "ProvisionedProductViewFilterBy"],
                         typing.List[str]] = dataclasses.field(
                             default=ShapeBase.NOT_SET,
                         )

    # The sort field. If no value is specified, the results are not sorted. The
    # valid values are `arn`, `id`, `name`, and `lastRecordId`.
    sort_by: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The sort order. If no value is specified, the results are not sorted.
    sort_order: typing.Union[str, "SortOrder"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The maximum number of items to return with this call.
    page_size: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The page token for the next set of results. To retrieve the first set of
    # results, use null.
    page_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class SearchProvisionedProductsOutput(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "provisioned_products",
                "ProvisionedProducts",
                TypeInfo(typing.List[ProvisionedProductAttribute]),
            ),
            (
                "total_results_count",
                "TotalResultsCount",
                TypeInfo(int),
            ),
            (
                "next_page_token",
                "NextPageToken",
                TypeInfo(str),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Information about the provisioned products.
    provisioned_products: typing.List["ProvisionedProductAttribute"
                                     ] = dataclasses.field(
                                         default=ShapeBase.NOT_SET,
                                     )

    # The number of provisioned products found.
    total_results_count: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The page token to use to retrieve the next set of results. If there are no
    # additional results, this value is null.
    next_page_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )


class SortOrder(str):
    ASCENDING = "ASCENDING"
    DESCENDING = "DESCENDING"


class Status(str):
    AVAILABLE = "AVAILABLE"
    CREATING = "CREATING"
    FAILED = "FAILED"


@dataclasses.dataclass
class Tag(ShapeBase):
    """
    Information about a tag. A tag is a key-value pair. Tags are propagated to the
    resources created when provisioning a product.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "key",
                "Key",
                TypeInfo(str),
            ),
            (
                "value",
                "Value",
                TypeInfo(str),
            ),
        ]

    # The tag key.
    key: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The value for this key.
    value: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class TagOptionDetail(ShapeBase):
    """
    Information about a TagOption.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "key",
                "Key",
                TypeInfo(str),
            ),
            (
                "value",
                "Value",
                TypeInfo(str),
            ),
            (
                "active",
                "Active",
                TypeInfo(bool),
            ),
            (
                "id",
                "Id",
                TypeInfo(str),
            ),
        ]

    # The TagOption key.
    key: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The TagOption value.
    value: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The TagOption active state.
    active: bool = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The TagOption identifier.
    id: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class TagOptionNotMigratedException(ShapeBase):
    """
    An operation requiring TagOptions failed because the TagOptions migration
    process has not been performed for this account. Please use the AWS console to
    perform the migration process before retrying the operation.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class TagOptionSummary(ShapeBase):
    """
    Summary information about a TagOption.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "key",
                "Key",
                TypeInfo(str),
            ),
            (
                "values",
                "Values",
                TypeInfo(typing.List[str]),
            ),
        ]

    # The TagOption key.
    key: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The TagOption value.
    values: typing.List[str] = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class TerminateProvisionedProductInput(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "terminate_token",
                "TerminateToken",
                TypeInfo(str),
            ),
            (
                "provisioned_product_name",
                "ProvisionedProductName",
                TypeInfo(str),
            ),
            (
                "provisioned_product_id",
                "ProvisionedProductId",
                TypeInfo(str),
            ),
            (
                "ignore_errors",
                "IgnoreErrors",
                TypeInfo(bool),
            ),
            (
                "accept_language",
                "AcceptLanguage",
                TypeInfo(str),
            ),
        ]

    # An idempotency token that uniquely identifies the termination request. This
    # token is only valid during the termination process. After the provisioned
    # product is terminated, subsequent requests to terminate the same
    # provisioned product always return **ResourceNotFound**.
    terminate_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The name of the provisioned product. You cannot specify both
    # `ProvisionedProductName` and `ProvisionedProductId`.
    provisioned_product_name: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The identifier of the provisioned product. You cannot specify both
    # `ProvisionedProductName` and `ProvisionedProductId`.
    provisioned_product_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # If set to true, AWS Service Catalog stops managing the specified
    # provisioned product even if it cannot delete the underlying resources.
    ignore_errors: bool = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The language code.

    #   * `en` \- English (default)

    #   * `jp` \- Japanese

    #   * `zh` \- Chinese
    accept_language: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class TerminateProvisionedProductOutput(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "record_detail",
                "RecordDetail",
                TypeInfo(RecordDetail),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Information about the result of this request.
    record_detail: "RecordDetail" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class UpdateConstraintInput(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "id",
                "Id",
                TypeInfo(str),
            ),
            (
                "accept_language",
                "AcceptLanguage",
                TypeInfo(str),
            ),
            (
                "description",
                "Description",
                TypeInfo(str),
            ),
        ]

    # The identifier of the constraint.
    id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The language code.

    #   * `en` \- English (default)

    #   * `jp` \- Japanese

    #   * `zh` \- Chinese
    accept_language: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The updated description of the constraint.
    description: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class UpdateConstraintOutput(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "constraint_detail",
                "ConstraintDetail",
                TypeInfo(ConstraintDetail),
            ),
            (
                "constraint_parameters",
                "ConstraintParameters",
                TypeInfo(str),
            ),
            (
                "status",
                "Status",
                TypeInfo(typing.Union[str, Status]),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Information about the constraint.
    constraint_detail: "ConstraintDetail" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The constraint parameters.
    constraint_parameters: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The status of the current request.
    status: typing.Union[str, "Status"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class UpdatePortfolioInput(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "id",
                "Id",
                TypeInfo(str),
            ),
            (
                "accept_language",
                "AcceptLanguage",
                TypeInfo(str),
            ),
            (
                "display_name",
                "DisplayName",
                TypeInfo(str),
            ),
            (
                "description",
                "Description",
                TypeInfo(str),
            ),
            (
                "provider_name",
                "ProviderName",
                TypeInfo(str),
            ),
            (
                "add_tags",
                "AddTags",
                TypeInfo(typing.List[Tag]),
            ),
            (
                "remove_tags",
                "RemoveTags",
                TypeInfo(typing.List[str]),
            ),
        ]

    # The portfolio identifier.
    id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The language code.

    #   * `en` \- English (default)

    #   * `jp` \- Japanese

    #   * `zh` \- Chinese
    accept_language: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The name to use for display purposes.
    display_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The updated description of the portfolio.
    description: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The updated name of the portfolio provider.
    provider_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The tags to add.
    add_tags: typing.List["Tag"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The tags to remove.
    remove_tags: typing.List[str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class UpdatePortfolioOutput(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "portfolio_detail",
                "PortfolioDetail",
                TypeInfo(PortfolioDetail),
            ),
            (
                "tags",
                "Tags",
                TypeInfo(typing.List[Tag]),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Information about the portfolio.
    portfolio_detail: "PortfolioDetail" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Information about the tags associated with the portfolio.
    tags: typing.List["Tag"] = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class UpdateProductInput(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "id",
                "Id",
                TypeInfo(str),
            ),
            (
                "accept_language",
                "AcceptLanguage",
                TypeInfo(str),
            ),
            (
                "name",
                "Name",
                TypeInfo(str),
            ),
            (
                "owner",
                "Owner",
                TypeInfo(str),
            ),
            (
                "description",
                "Description",
                TypeInfo(str),
            ),
            (
                "distributor",
                "Distributor",
                TypeInfo(str),
            ),
            (
                "support_description",
                "SupportDescription",
                TypeInfo(str),
            ),
            (
                "support_email",
                "SupportEmail",
                TypeInfo(str),
            ),
            (
                "support_url",
                "SupportUrl",
                TypeInfo(str),
            ),
            (
                "add_tags",
                "AddTags",
                TypeInfo(typing.List[Tag]),
            ),
            (
                "remove_tags",
                "RemoveTags",
                TypeInfo(typing.List[str]),
            ),
        ]

    # The product identifier.
    id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The language code.

    #   * `en` \- English (default)

    #   * `jp` \- Japanese

    #   * `zh` \- Chinese
    accept_language: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The updated product name.
    name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The updated owner of the product.
    owner: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The updated description of the product.
    description: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The updated distributor of the product.
    distributor: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The updated support description for the product.
    support_description: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The updated support email for the product.
    support_email: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The updated support URL for the product.
    support_url: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The tags to add to the product.
    add_tags: typing.List["Tag"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The tags to remove from the product.
    remove_tags: typing.List[str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class UpdateProductOutput(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "product_view_detail",
                "ProductViewDetail",
                TypeInfo(ProductViewDetail),
            ),
            (
                "tags",
                "Tags",
                TypeInfo(typing.List[Tag]),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Information about the product view.
    product_view_detail: "ProductViewDetail" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Information about the tags associated with the product.
    tags: typing.List["Tag"] = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class UpdateProvisionedProductInput(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "update_token",
                "UpdateToken",
                TypeInfo(str),
            ),
            (
                "accept_language",
                "AcceptLanguage",
                TypeInfo(str),
            ),
            (
                "provisioned_product_name",
                "ProvisionedProductName",
                TypeInfo(str),
            ),
            (
                "provisioned_product_id",
                "ProvisionedProductId",
                TypeInfo(str),
            ),
            (
                "product_id",
                "ProductId",
                TypeInfo(str),
            ),
            (
                "provisioning_artifact_id",
                "ProvisioningArtifactId",
                TypeInfo(str),
            ),
            (
                "path_id",
                "PathId",
                TypeInfo(str),
            ),
            (
                "provisioning_parameters",
                "ProvisioningParameters",
                TypeInfo(typing.List[UpdateProvisioningParameter]),
            ),
        ]

    # The idempotency token that uniquely identifies the provisioning update
    # request.
    update_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The language code.

    #   * `en` \- English (default)

    #   * `jp` \- Japanese

    #   * `zh` \- Chinese
    accept_language: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The updated name of the provisioned product. You cannot specify both
    # `ProvisionedProductName` and `ProvisionedProductId`.
    provisioned_product_name: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The identifier of the provisioned product. You cannot specify both
    # `ProvisionedProductName` and `ProvisionedProductId`.
    provisioned_product_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The identifier of the provisioned product.
    product_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The identifier of the provisioning artifact.
    provisioning_artifact_id: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The new path identifier. This value is optional if the product has a
    # default path, and required if the product has more than one path.
    path_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The new parameters.
    provisioning_parameters: typing.List["UpdateProvisioningParameter"
                                        ] = dataclasses.field(
                                            default=ShapeBase.NOT_SET,
                                        )


@dataclasses.dataclass
class UpdateProvisionedProductOutput(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "record_detail",
                "RecordDetail",
                TypeInfo(RecordDetail),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Information about the result of the request.
    record_detail: "RecordDetail" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class UpdateProvisioningArtifactInput(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "product_id",
                "ProductId",
                TypeInfo(str),
            ),
            (
                "provisioning_artifact_id",
                "ProvisioningArtifactId",
                TypeInfo(str),
            ),
            (
                "accept_language",
                "AcceptLanguage",
                TypeInfo(str),
            ),
            (
                "name",
                "Name",
                TypeInfo(str),
            ),
            (
                "description",
                "Description",
                TypeInfo(str),
            ),
            (
                "active",
                "Active",
                TypeInfo(bool),
            ),
        ]

    # The product identifier.
    product_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The identifier of the provisioning artifact.
    provisioning_artifact_id: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The language code.

    #   * `en` \- English (default)

    #   * `jp` \- Japanese

    #   * `zh` \- Chinese
    accept_language: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The updated name of the provisioning artifact.
    name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The updated description of the provisioning artifact.
    description: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Indicates whether the product version is active.
    active: bool = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class UpdateProvisioningArtifactOutput(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "provisioning_artifact_detail",
                "ProvisioningArtifactDetail",
                TypeInfo(ProvisioningArtifactDetail),
            ),
            (
                "info",
                "Info",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "status",
                "Status",
                TypeInfo(typing.Union[str, Status]),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Information about the provisioning artifact.
    provisioning_artifact_detail: "ProvisioningArtifactDetail" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The URL of the CloudFormation template in Amazon S3.
    info: typing.Dict[str, str] = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The status of the current request.
    status: typing.Union[str, "Status"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class UpdateProvisioningParameter(ShapeBase):
    """
    The parameter key-value pair used to update a provisioned product.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "key",
                "Key",
                TypeInfo(str),
            ),
            (
                "value",
                "Value",
                TypeInfo(str),
            ),
            (
                "use_previous_value",
                "UsePreviousValue",
                TypeInfo(bool),
            ),
        ]

    # The parameter key.
    key: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The parameter value.
    value: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # If set to true, `Value` is ignored and the previous parameter value is
    # kept.
    use_previous_value: bool = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class UpdateTagOptionInput(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "id",
                "Id",
                TypeInfo(str),
            ),
            (
                "value",
                "Value",
                TypeInfo(str),
            ),
            (
                "active",
                "Active",
                TypeInfo(bool),
            ),
        ]

    # The TagOption identifier.
    id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The updated value.
    value: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The updated active state.
    active: bool = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class UpdateTagOptionOutput(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "tag_option_detail",
                "TagOptionDetail",
                TypeInfo(TagOptionDetail),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Information about the TagOption.
    tag_option_detail: "TagOptionDetail" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class UsageInstruction(ShapeBase):
    """
    Additional information provided by the administrator.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "type",
                "Type",
                TypeInfo(str),
            ),
            (
                "value",
                "Value",
                TypeInfo(str),
            ),
        ]

    # The usage instruction type for the value.
    type: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The usage instruction value for this type.
    value: str = dataclasses.field(default=ShapeBase.NOT_SET, )
