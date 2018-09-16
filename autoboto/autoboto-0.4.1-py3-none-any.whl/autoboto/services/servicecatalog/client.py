import datetime
import typing
import boto3
from autoboto import ClientBase, ShapeBase, OutputShapeBase
from . import shapes


class Client(ClientBase):
    def __init__(self, *args, **kwargs):
        super().__init__("servicecatalog", *args, **kwargs)

    def accept_portfolio_share(
        self,
        _request: shapes.AcceptPortfolioShareInput = None,
        *,
        portfolio_id: str,
        accept_language: str = ShapeBase.NOT_SET,
    ) -> shapes.AcceptPortfolioShareOutput:
        """
        Accepts an offer to share the specified portfolio.
        """
        if _request is None:
            _params = {}
            if portfolio_id is not ShapeBase.NOT_SET:
                _params['portfolio_id'] = portfolio_id
            if accept_language is not ShapeBase.NOT_SET:
                _params['accept_language'] = accept_language
            _request = shapes.AcceptPortfolioShareInput(**_params)
        response = self._boto_client.accept_portfolio_share(
            **_request.to_boto()
        )

        return shapes.AcceptPortfolioShareOutput.from_boto(response)

    def associate_principal_with_portfolio(
        self,
        _request: shapes.AssociatePrincipalWithPortfolioInput = None,
        *,
        portfolio_id: str,
        principal_arn: str,
        principal_type: typing.Union[str, shapes.PrincipalType],
        accept_language: str = ShapeBase.NOT_SET,
    ) -> shapes.AssociatePrincipalWithPortfolioOutput:
        """
        Associates the specified principal ARN with the specified portfolio.
        """
        if _request is None:
            _params = {}
            if portfolio_id is not ShapeBase.NOT_SET:
                _params['portfolio_id'] = portfolio_id
            if principal_arn is not ShapeBase.NOT_SET:
                _params['principal_arn'] = principal_arn
            if principal_type is not ShapeBase.NOT_SET:
                _params['principal_type'] = principal_type
            if accept_language is not ShapeBase.NOT_SET:
                _params['accept_language'] = accept_language
            _request = shapes.AssociatePrincipalWithPortfolioInput(**_params)
        response = self._boto_client.associate_principal_with_portfolio(
            **_request.to_boto()
        )

        return shapes.AssociatePrincipalWithPortfolioOutput.from_boto(response)

    def associate_product_with_portfolio(
        self,
        _request: shapes.AssociateProductWithPortfolioInput = None,
        *,
        product_id: str,
        portfolio_id: str,
        accept_language: str = ShapeBase.NOT_SET,
        source_portfolio_id: str = ShapeBase.NOT_SET,
    ) -> shapes.AssociateProductWithPortfolioOutput:
        """
        Associates the specified product with the specified portfolio.
        """
        if _request is None:
            _params = {}
            if product_id is not ShapeBase.NOT_SET:
                _params['product_id'] = product_id
            if portfolio_id is not ShapeBase.NOT_SET:
                _params['portfolio_id'] = portfolio_id
            if accept_language is not ShapeBase.NOT_SET:
                _params['accept_language'] = accept_language
            if source_portfolio_id is not ShapeBase.NOT_SET:
                _params['source_portfolio_id'] = source_portfolio_id
            _request = shapes.AssociateProductWithPortfolioInput(**_params)
        response = self._boto_client.associate_product_with_portfolio(
            **_request.to_boto()
        )

        return shapes.AssociateProductWithPortfolioOutput.from_boto(response)

    def associate_tag_option_with_resource(
        self,
        _request: shapes.AssociateTagOptionWithResourceInput = None,
        *,
        resource_id: str,
        tag_option_id: str,
    ) -> shapes.AssociateTagOptionWithResourceOutput:
        """
        Associate the specified TagOption with the specified portfolio or product.
        """
        if _request is None:
            _params = {}
            if resource_id is not ShapeBase.NOT_SET:
                _params['resource_id'] = resource_id
            if tag_option_id is not ShapeBase.NOT_SET:
                _params['tag_option_id'] = tag_option_id
            _request = shapes.AssociateTagOptionWithResourceInput(**_params)
        response = self._boto_client.associate_tag_option_with_resource(
            **_request.to_boto()
        )

        return shapes.AssociateTagOptionWithResourceOutput.from_boto(response)

    def copy_product(
        self,
        _request: shapes.CopyProductInput = None,
        *,
        source_product_arn: str,
        idempotency_token: str,
        accept_language: str = ShapeBase.NOT_SET,
        target_product_id: str = ShapeBase.NOT_SET,
        target_product_name: str = ShapeBase.NOT_SET,
        source_provisioning_artifact_identifiers: typing.
        List[typing.Dict[typing.Union[str, shapes.
                                      ProvisioningArtifactPropertyName], str]
            ] = ShapeBase.NOT_SET,
        copy_options: typing.List[typing.Union[str, shapes.CopyOption]
                                 ] = ShapeBase.NOT_SET,
    ) -> shapes.CopyProductOutput:
        """
        Copies the specified source product to the specified target product or a new
        product.

        You can copy a product to the same account or another account. You can copy a
        product to the same region or another region.

        This operation is performed asynchronously. To track the progress of the
        operation, use DescribeCopyProductStatus.
        """
        if _request is None:
            _params = {}
            if source_product_arn is not ShapeBase.NOT_SET:
                _params['source_product_arn'] = source_product_arn
            if idempotency_token is not ShapeBase.NOT_SET:
                _params['idempotency_token'] = idempotency_token
            if accept_language is not ShapeBase.NOT_SET:
                _params['accept_language'] = accept_language
            if target_product_id is not ShapeBase.NOT_SET:
                _params['target_product_id'] = target_product_id
            if target_product_name is not ShapeBase.NOT_SET:
                _params['target_product_name'] = target_product_name
            if source_provisioning_artifact_identifiers is not ShapeBase.NOT_SET:
                _params['source_provisioning_artifact_identifiers'
                       ] = source_provisioning_artifact_identifiers
            if copy_options is not ShapeBase.NOT_SET:
                _params['copy_options'] = copy_options
            _request = shapes.CopyProductInput(**_params)
        response = self._boto_client.copy_product(**_request.to_boto())

        return shapes.CopyProductOutput.from_boto(response)

    def create_constraint(
        self,
        _request: shapes.CreateConstraintInput = None,
        *,
        portfolio_id: str,
        product_id: str,
        parameters: str,
        type: str,
        idempotency_token: str,
        accept_language: str = ShapeBase.NOT_SET,
        description: str = ShapeBase.NOT_SET,
    ) -> shapes.CreateConstraintOutput:
        """
        Creates a constraint.
        """
        if _request is None:
            _params = {}
            if portfolio_id is not ShapeBase.NOT_SET:
                _params['portfolio_id'] = portfolio_id
            if product_id is not ShapeBase.NOT_SET:
                _params['product_id'] = product_id
            if parameters is not ShapeBase.NOT_SET:
                _params['parameters'] = parameters
            if type is not ShapeBase.NOT_SET:
                _params['type'] = type
            if idempotency_token is not ShapeBase.NOT_SET:
                _params['idempotency_token'] = idempotency_token
            if accept_language is not ShapeBase.NOT_SET:
                _params['accept_language'] = accept_language
            if description is not ShapeBase.NOT_SET:
                _params['description'] = description
            _request = shapes.CreateConstraintInput(**_params)
        response = self._boto_client.create_constraint(**_request.to_boto())

        return shapes.CreateConstraintOutput.from_boto(response)

    def create_portfolio(
        self,
        _request: shapes.CreatePortfolioInput = None,
        *,
        display_name: str,
        provider_name: str,
        idempotency_token: str,
        accept_language: str = ShapeBase.NOT_SET,
        description: str = ShapeBase.NOT_SET,
        tags: typing.List[shapes.Tag] = ShapeBase.NOT_SET,
    ) -> shapes.CreatePortfolioOutput:
        """
        Creates a portfolio.
        """
        if _request is None:
            _params = {}
            if display_name is not ShapeBase.NOT_SET:
                _params['display_name'] = display_name
            if provider_name is not ShapeBase.NOT_SET:
                _params['provider_name'] = provider_name
            if idempotency_token is not ShapeBase.NOT_SET:
                _params['idempotency_token'] = idempotency_token
            if accept_language is not ShapeBase.NOT_SET:
                _params['accept_language'] = accept_language
            if description is not ShapeBase.NOT_SET:
                _params['description'] = description
            if tags is not ShapeBase.NOT_SET:
                _params['tags'] = tags
            _request = shapes.CreatePortfolioInput(**_params)
        response = self._boto_client.create_portfolio(**_request.to_boto())

        return shapes.CreatePortfolioOutput.from_boto(response)

    def create_portfolio_share(
        self,
        _request: shapes.CreatePortfolioShareInput = None,
        *,
        portfolio_id: str,
        account_id: str,
        accept_language: str = ShapeBase.NOT_SET,
    ) -> shapes.CreatePortfolioShareOutput:
        """
        Shares the specified portfolio with the specified account.
        """
        if _request is None:
            _params = {}
            if portfolio_id is not ShapeBase.NOT_SET:
                _params['portfolio_id'] = portfolio_id
            if account_id is not ShapeBase.NOT_SET:
                _params['account_id'] = account_id
            if accept_language is not ShapeBase.NOT_SET:
                _params['accept_language'] = accept_language
            _request = shapes.CreatePortfolioShareInput(**_params)
        response = self._boto_client.create_portfolio_share(
            **_request.to_boto()
        )

        return shapes.CreatePortfolioShareOutput.from_boto(response)

    def create_product(
        self,
        _request: shapes.CreateProductInput = None,
        *,
        name: str,
        owner: str,
        product_type: typing.Union[str, shapes.ProductType],
        provisioning_artifact_parameters: shapes.ProvisioningArtifactProperties,
        idempotency_token: str,
        accept_language: str = ShapeBase.NOT_SET,
        description: str = ShapeBase.NOT_SET,
        distributor: str = ShapeBase.NOT_SET,
        support_description: str = ShapeBase.NOT_SET,
        support_email: str = ShapeBase.NOT_SET,
        support_url: str = ShapeBase.NOT_SET,
        tags: typing.List[shapes.Tag] = ShapeBase.NOT_SET,
    ) -> shapes.CreateProductOutput:
        """
        Creates a product.
        """
        if _request is None:
            _params = {}
            if name is not ShapeBase.NOT_SET:
                _params['name'] = name
            if owner is not ShapeBase.NOT_SET:
                _params['owner'] = owner
            if product_type is not ShapeBase.NOT_SET:
                _params['product_type'] = product_type
            if provisioning_artifact_parameters is not ShapeBase.NOT_SET:
                _params['provisioning_artifact_parameters'
                       ] = provisioning_artifact_parameters
            if idempotency_token is not ShapeBase.NOT_SET:
                _params['idempotency_token'] = idempotency_token
            if accept_language is not ShapeBase.NOT_SET:
                _params['accept_language'] = accept_language
            if description is not ShapeBase.NOT_SET:
                _params['description'] = description
            if distributor is not ShapeBase.NOT_SET:
                _params['distributor'] = distributor
            if support_description is not ShapeBase.NOT_SET:
                _params['support_description'] = support_description
            if support_email is not ShapeBase.NOT_SET:
                _params['support_email'] = support_email
            if support_url is not ShapeBase.NOT_SET:
                _params['support_url'] = support_url
            if tags is not ShapeBase.NOT_SET:
                _params['tags'] = tags
            _request = shapes.CreateProductInput(**_params)
        response = self._boto_client.create_product(**_request.to_boto())

        return shapes.CreateProductOutput.from_boto(response)

    def create_provisioned_product_plan(
        self,
        _request: shapes.CreateProvisionedProductPlanInput = None,
        *,
        plan_name: str,
        plan_type: typing.Union[str, shapes.ProvisionedProductPlanType],
        product_id: str,
        provisioned_product_name: str,
        provisioning_artifact_id: str,
        idempotency_token: str,
        accept_language: str = ShapeBase.NOT_SET,
        notification_arns: typing.List[str] = ShapeBase.NOT_SET,
        path_id: str = ShapeBase.NOT_SET,
        provisioning_parameters: typing.List[shapes.UpdateProvisioningParameter
                                            ] = ShapeBase.NOT_SET,
        tags: typing.List[shapes.Tag] = ShapeBase.NOT_SET,
    ) -> shapes.CreateProvisionedProductPlanOutput:
        """
        Creates a plan. A plan includes the list of resources to be created (when
        provisioning a new product) or modified (when updating a provisioned product)
        when the plan is executed.

        You can create one plan per provisioned product. To create a plan for an
        existing provisioned product, the product status must be AVAILBLE or TAINTED.

        To view the resource changes in the change set, use
        DescribeProvisionedProductPlan. To create or modify the provisioned product, use
        ExecuteProvisionedProductPlan.
        """
        if _request is None:
            _params = {}
            if plan_name is not ShapeBase.NOT_SET:
                _params['plan_name'] = plan_name
            if plan_type is not ShapeBase.NOT_SET:
                _params['plan_type'] = plan_type
            if product_id is not ShapeBase.NOT_SET:
                _params['product_id'] = product_id
            if provisioned_product_name is not ShapeBase.NOT_SET:
                _params['provisioned_product_name'] = provisioned_product_name
            if provisioning_artifact_id is not ShapeBase.NOT_SET:
                _params['provisioning_artifact_id'] = provisioning_artifact_id
            if idempotency_token is not ShapeBase.NOT_SET:
                _params['idempotency_token'] = idempotency_token
            if accept_language is not ShapeBase.NOT_SET:
                _params['accept_language'] = accept_language
            if notification_arns is not ShapeBase.NOT_SET:
                _params['notification_arns'] = notification_arns
            if path_id is not ShapeBase.NOT_SET:
                _params['path_id'] = path_id
            if provisioning_parameters is not ShapeBase.NOT_SET:
                _params['provisioning_parameters'] = provisioning_parameters
            if tags is not ShapeBase.NOT_SET:
                _params['tags'] = tags
            _request = shapes.CreateProvisionedProductPlanInput(**_params)
        response = self._boto_client.create_provisioned_product_plan(
            **_request.to_boto()
        )

        return shapes.CreateProvisionedProductPlanOutput.from_boto(response)

    def create_provisioning_artifact(
        self,
        _request: shapes.CreateProvisioningArtifactInput = None,
        *,
        product_id: str,
        parameters: shapes.ProvisioningArtifactProperties,
        idempotency_token: str,
        accept_language: str = ShapeBase.NOT_SET,
    ) -> shapes.CreateProvisioningArtifactOutput:
        """
        Creates a provisioning artifact (also known as a version) for the specified
        product.

        You cannot create a provisioning artifact for a product that was shared with
        you.
        """
        if _request is None:
            _params = {}
            if product_id is not ShapeBase.NOT_SET:
                _params['product_id'] = product_id
            if parameters is not ShapeBase.NOT_SET:
                _params['parameters'] = parameters
            if idempotency_token is not ShapeBase.NOT_SET:
                _params['idempotency_token'] = idempotency_token
            if accept_language is not ShapeBase.NOT_SET:
                _params['accept_language'] = accept_language
            _request = shapes.CreateProvisioningArtifactInput(**_params)
        response = self._boto_client.create_provisioning_artifact(
            **_request.to_boto()
        )

        return shapes.CreateProvisioningArtifactOutput.from_boto(response)

    def create_tag_option(
        self,
        _request: shapes.CreateTagOptionInput = None,
        *,
        key: str,
        value: str,
    ) -> shapes.CreateTagOptionOutput:
        """
        Creates a TagOption.
        """
        if _request is None:
            _params = {}
            if key is not ShapeBase.NOT_SET:
                _params['key'] = key
            if value is not ShapeBase.NOT_SET:
                _params['value'] = value
            _request = shapes.CreateTagOptionInput(**_params)
        response = self._boto_client.create_tag_option(**_request.to_boto())

        return shapes.CreateTagOptionOutput.from_boto(response)

    def delete_constraint(
        self,
        _request: shapes.DeleteConstraintInput = None,
        *,
        id: str,
        accept_language: str = ShapeBase.NOT_SET,
    ) -> shapes.DeleteConstraintOutput:
        """
        Deletes the specified constraint.
        """
        if _request is None:
            _params = {}
            if id is not ShapeBase.NOT_SET:
                _params['id'] = id
            if accept_language is not ShapeBase.NOT_SET:
                _params['accept_language'] = accept_language
            _request = shapes.DeleteConstraintInput(**_params)
        response = self._boto_client.delete_constraint(**_request.to_boto())

        return shapes.DeleteConstraintOutput.from_boto(response)

    def delete_portfolio(
        self,
        _request: shapes.DeletePortfolioInput = None,
        *,
        id: str,
        accept_language: str = ShapeBase.NOT_SET,
    ) -> shapes.DeletePortfolioOutput:
        """
        Deletes the specified portfolio.

        You cannot delete a portfolio if it was shared with you or if it has associated
        products, users, constraints, or shared accounts.
        """
        if _request is None:
            _params = {}
            if id is not ShapeBase.NOT_SET:
                _params['id'] = id
            if accept_language is not ShapeBase.NOT_SET:
                _params['accept_language'] = accept_language
            _request = shapes.DeletePortfolioInput(**_params)
        response = self._boto_client.delete_portfolio(**_request.to_boto())

        return shapes.DeletePortfolioOutput.from_boto(response)

    def delete_portfolio_share(
        self,
        _request: shapes.DeletePortfolioShareInput = None,
        *,
        portfolio_id: str,
        account_id: str,
        accept_language: str = ShapeBase.NOT_SET,
    ) -> shapes.DeletePortfolioShareOutput:
        """
        Stops sharing the specified portfolio with the specified account.
        """
        if _request is None:
            _params = {}
            if portfolio_id is not ShapeBase.NOT_SET:
                _params['portfolio_id'] = portfolio_id
            if account_id is not ShapeBase.NOT_SET:
                _params['account_id'] = account_id
            if accept_language is not ShapeBase.NOT_SET:
                _params['accept_language'] = accept_language
            _request = shapes.DeletePortfolioShareInput(**_params)
        response = self._boto_client.delete_portfolio_share(
            **_request.to_boto()
        )

        return shapes.DeletePortfolioShareOutput.from_boto(response)

    def delete_product(
        self,
        _request: shapes.DeleteProductInput = None,
        *,
        id: str,
        accept_language: str = ShapeBase.NOT_SET,
    ) -> shapes.DeleteProductOutput:
        """
        Deletes the specified product.

        You cannot delete a product if it was shared with you or is associated with a
        portfolio.
        """
        if _request is None:
            _params = {}
            if id is not ShapeBase.NOT_SET:
                _params['id'] = id
            if accept_language is not ShapeBase.NOT_SET:
                _params['accept_language'] = accept_language
            _request = shapes.DeleteProductInput(**_params)
        response = self._boto_client.delete_product(**_request.to_boto())

        return shapes.DeleteProductOutput.from_boto(response)

    def delete_provisioned_product_plan(
        self,
        _request: shapes.DeleteProvisionedProductPlanInput = None,
        *,
        plan_id: str,
        accept_language: str = ShapeBase.NOT_SET,
        ignore_errors: bool = ShapeBase.NOT_SET,
    ) -> shapes.DeleteProvisionedProductPlanOutput:
        """
        Deletes the specified plan.
        """
        if _request is None:
            _params = {}
            if plan_id is not ShapeBase.NOT_SET:
                _params['plan_id'] = plan_id
            if accept_language is not ShapeBase.NOT_SET:
                _params['accept_language'] = accept_language
            if ignore_errors is not ShapeBase.NOT_SET:
                _params['ignore_errors'] = ignore_errors
            _request = shapes.DeleteProvisionedProductPlanInput(**_params)
        response = self._boto_client.delete_provisioned_product_plan(
            **_request.to_boto()
        )

        return shapes.DeleteProvisionedProductPlanOutput.from_boto(response)

    def delete_provisioning_artifact(
        self,
        _request: shapes.DeleteProvisioningArtifactInput = None,
        *,
        product_id: str,
        provisioning_artifact_id: str,
        accept_language: str = ShapeBase.NOT_SET,
    ) -> shapes.DeleteProvisioningArtifactOutput:
        """
        Deletes the specified provisioning artifact (also known as a version) for the
        specified product.

        You cannot delete a provisioning artifact associated with a product that was
        shared with you. You cannot delete the last provisioning artifact for a product,
        because a product must have at least one provisioning artifact.
        """
        if _request is None:
            _params = {}
            if product_id is not ShapeBase.NOT_SET:
                _params['product_id'] = product_id
            if provisioning_artifact_id is not ShapeBase.NOT_SET:
                _params['provisioning_artifact_id'] = provisioning_artifact_id
            if accept_language is not ShapeBase.NOT_SET:
                _params['accept_language'] = accept_language
            _request = shapes.DeleteProvisioningArtifactInput(**_params)
        response = self._boto_client.delete_provisioning_artifact(
            **_request.to_boto()
        )

        return shapes.DeleteProvisioningArtifactOutput.from_boto(response)

    def delete_tag_option(
        self,
        _request: shapes.DeleteTagOptionInput = None,
        *,
        id: str,
    ) -> shapes.DeleteTagOptionOutput:
        """
        Deletes the specified TagOption.

        You cannot delete a TagOption if it is associated with a product or portfolio.
        """
        if _request is None:
            _params = {}
            if id is not ShapeBase.NOT_SET:
                _params['id'] = id
            _request = shapes.DeleteTagOptionInput(**_params)
        response = self._boto_client.delete_tag_option(**_request.to_boto())

        return shapes.DeleteTagOptionOutput.from_boto(response)

    def describe_constraint(
        self,
        _request: shapes.DescribeConstraintInput = None,
        *,
        id: str,
        accept_language: str = ShapeBase.NOT_SET,
    ) -> shapes.DescribeConstraintOutput:
        """
        Gets information about the specified constraint.
        """
        if _request is None:
            _params = {}
            if id is not ShapeBase.NOT_SET:
                _params['id'] = id
            if accept_language is not ShapeBase.NOT_SET:
                _params['accept_language'] = accept_language
            _request = shapes.DescribeConstraintInput(**_params)
        response = self._boto_client.describe_constraint(**_request.to_boto())

        return shapes.DescribeConstraintOutput.from_boto(response)

    def describe_copy_product_status(
        self,
        _request: shapes.DescribeCopyProductStatusInput = None,
        *,
        copy_product_token: str,
        accept_language: str = ShapeBase.NOT_SET,
    ) -> shapes.DescribeCopyProductStatusOutput:
        """
        Gets the status of the specified copy product operation.
        """
        if _request is None:
            _params = {}
            if copy_product_token is not ShapeBase.NOT_SET:
                _params['copy_product_token'] = copy_product_token
            if accept_language is not ShapeBase.NOT_SET:
                _params['accept_language'] = accept_language
            _request = shapes.DescribeCopyProductStatusInput(**_params)
        response = self._boto_client.describe_copy_product_status(
            **_request.to_boto()
        )

        return shapes.DescribeCopyProductStatusOutput.from_boto(response)

    def describe_portfolio(
        self,
        _request: shapes.DescribePortfolioInput = None,
        *,
        id: str,
        accept_language: str = ShapeBase.NOT_SET,
    ) -> shapes.DescribePortfolioOutput:
        """
        Gets information about the specified portfolio.
        """
        if _request is None:
            _params = {}
            if id is not ShapeBase.NOT_SET:
                _params['id'] = id
            if accept_language is not ShapeBase.NOT_SET:
                _params['accept_language'] = accept_language
            _request = shapes.DescribePortfolioInput(**_params)
        response = self._boto_client.describe_portfolio(**_request.to_boto())

        return shapes.DescribePortfolioOutput.from_boto(response)

    def describe_product(
        self,
        _request: shapes.DescribeProductInput = None,
        *,
        id: str,
        accept_language: str = ShapeBase.NOT_SET,
    ) -> shapes.DescribeProductOutput:
        """
        Gets information about the specified product.
        """
        if _request is None:
            _params = {}
            if id is not ShapeBase.NOT_SET:
                _params['id'] = id
            if accept_language is not ShapeBase.NOT_SET:
                _params['accept_language'] = accept_language
            _request = shapes.DescribeProductInput(**_params)
        response = self._boto_client.describe_product(**_request.to_boto())

        return shapes.DescribeProductOutput.from_boto(response)

    def describe_product_as_admin(
        self,
        _request: shapes.DescribeProductAsAdminInput = None,
        *,
        id: str,
        accept_language: str = ShapeBase.NOT_SET,
    ) -> shapes.DescribeProductAsAdminOutput:
        """
        Gets information about the specified product. This operation is run with
        administrator access.
        """
        if _request is None:
            _params = {}
            if id is not ShapeBase.NOT_SET:
                _params['id'] = id
            if accept_language is not ShapeBase.NOT_SET:
                _params['accept_language'] = accept_language
            _request = shapes.DescribeProductAsAdminInput(**_params)
        response = self._boto_client.describe_product_as_admin(
            **_request.to_boto()
        )

        return shapes.DescribeProductAsAdminOutput.from_boto(response)

    def describe_product_view(
        self,
        _request: shapes.DescribeProductViewInput = None,
        *,
        id: str,
        accept_language: str = ShapeBase.NOT_SET,
    ) -> shapes.DescribeProductViewOutput:
        """
        Gets information about the specified product.
        """
        if _request is None:
            _params = {}
            if id is not ShapeBase.NOT_SET:
                _params['id'] = id
            if accept_language is not ShapeBase.NOT_SET:
                _params['accept_language'] = accept_language
            _request = shapes.DescribeProductViewInput(**_params)
        response = self._boto_client.describe_product_view(**_request.to_boto())

        return shapes.DescribeProductViewOutput.from_boto(response)

    def describe_provisioned_product(
        self,
        _request: shapes.DescribeProvisionedProductInput = None,
        *,
        id: str,
        accept_language: str = ShapeBase.NOT_SET,
    ) -> shapes.DescribeProvisionedProductOutput:
        """
        Gets information about the specified provisioned product.
        """
        if _request is None:
            _params = {}
            if id is not ShapeBase.NOT_SET:
                _params['id'] = id
            if accept_language is not ShapeBase.NOT_SET:
                _params['accept_language'] = accept_language
            _request = shapes.DescribeProvisionedProductInput(**_params)
        response = self._boto_client.describe_provisioned_product(
            **_request.to_boto()
        )

        return shapes.DescribeProvisionedProductOutput.from_boto(response)

    def describe_provisioned_product_plan(
        self,
        _request: shapes.DescribeProvisionedProductPlanInput = None,
        *,
        plan_id: str,
        accept_language: str = ShapeBase.NOT_SET,
        page_size: int = ShapeBase.NOT_SET,
        page_token: str = ShapeBase.NOT_SET,
    ) -> shapes.DescribeProvisionedProductPlanOutput:
        """
        Gets information about the resource changes for the specified plan.
        """
        if _request is None:
            _params = {}
            if plan_id is not ShapeBase.NOT_SET:
                _params['plan_id'] = plan_id
            if accept_language is not ShapeBase.NOT_SET:
                _params['accept_language'] = accept_language
            if page_size is not ShapeBase.NOT_SET:
                _params['page_size'] = page_size
            if page_token is not ShapeBase.NOT_SET:
                _params['page_token'] = page_token
            _request = shapes.DescribeProvisionedProductPlanInput(**_params)
        response = self._boto_client.describe_provisioned_product_plan(
            **_request.to_boto()
        )

        return shapes.DescribeProvisionedProductPlanOutput.from_boto(response)

    def describe_provisioning_artifact(
        self,
        _request: shapes.DescribeProvisioningArtifactInput = None,
        *,
        provisioning_artifact_id: str,
        product_id: str,
        accept_language: str = ShapeBase.NOT_SET,
        verbose: bool = ShapeBase.NOT_SET,
    ) -> shapes.DescribeProvisioningArtifactOutput:
        """
        Gets information about the specified provisioning artifact (also known as a
        version) for the specified product.
        """
        if _request is None:
            _params = {}
            if provisioning_artifact_id is not ShapeBase.NOT_SET:
                _params['provisioning_artifact_id'] = provisioning_artifact_id
            if product_id is not ShapeBase.NOT_SET:
                _params['product_id'] = product_id
            if accept_language is not ShapeBase.NOT_SET:
                _params['accept_language'] = accept_language
            if verbose is not ShapeBase.NOT_SET:
                _params['verbose'] = verbose
            _request = shapes.DescribeProvisioningArtifactInput(**_params)
        response = self._boto_client.describe_provisioning_artifact(
            **_request.to_boto()
        )

        return shapes.DescribeProvisioningArtifactOutput.from_boto(response)

    def describe_provisioning_parameters(
        self,
        _request: shapes.DescribeProvisioningParametersInput = None,
        *,
        product_id: str,
        provisioning_artifact_id: str,
        accept_language: str = ShapeBase.NOT_SET,
        path_id: str = ShapeBase.NOT_SET,
    ) -> shapes.DescribeProvisioningParametersOutput:
        """
        Gets information about the configuration required to provision the specified
        product using the specified provisioning artifact.

        If the output contains a TagOption key with an empty list of values, there is a
        TagOption conflict for that key. The end user cannot take action to fix the
        conflict, and launch is not blocked. In subsequent calls to ProvisionProduct, do
        not include conflicted TagOption keys as tags, or this causes the error
        "Parameter validation failed: Missing required parameter in Tags[ _N_ ]: _Value_
        ". Tag the provisioned product with the value `sc-tagoption-conflict-
        portfolioId-productId`.
        """
        if _request is None:
            _params = {}
            if product_id is not ShapeBase.NOT_SET:
                _params['product_id'] = product_id
            if provisioning_artifact_id is not ShapeBase.NOT_SET:
                _params['provisioning_artifact_id'] = provisioning_artifact_id
            if accept_language is not ShapeBase.NOT_SET:
                _params['accept_language'] = accept_language
            if path_id is not ShapeBase.NOT_SET:
                _params['path_id'] = path_id
            _request = shapes.DescribeProvisioningParametersInput(**_params)
        response = self._boto_client.describe_provisioning_parameters(
            **_request.to_boto()
        )

        return shapes.DescribeProvisioningParametersOutput.from_boto(response)

    def describe_record(
        self,
        _request: shapes.DescribeRecordInput = None,
        *,
        id: str,
        accept_language: str = ShapeBase.NOT_SET,
        page_token: str = ShapeBase.NOT_SET,
        page_size: int = ShapeBase.NOT_SET,
    ) -> shapes.DescribeRecordOutput:
        """
        Gets information about the specified request operation.

        Use this operation after calling a request operation (for example,
        ProvisionProduct, TerminateProvisionedProduct, or UpdateProvisionedProduct).
        """
        if _request is None:
            _params = {}
            if id is not ShapeBase.NOT_SET:
                _params['id'] = id
            if accept_language is not ShapeBase.NOT_SET:
                _params['accept_language'] = accept_language
            if page_token is not ShapeBase.NOT_SET:
                _params['page_token'] = page_token
            if page_size is not ShapeBase.NOT_SET:
                _params['page_size'] = page_size
            _request = shapes.DescribeRecordInput(**_params)
        response = self._boto_client.describe_record(**_request.to_boto())

        return shapes.DescribeRecordOutput.from_boto(response)

    def describe_tag_option(
        self,
        _request: shapes.DescribeTagOptionInput = None,
        *,
        id: str,
    ) -> shapes.DescribeTagOptionOutput:
        """
        Gets information about the specified TagOption.
        """
        if _request is None:
            _params = {}
            if id is not ShapeBase.NOT_SET:
                _params['id'] = id
            _request = shapes.DescribeTagOptionInput(**_params)
        response = self._boto_client.describe_tag_option(**_request.to_boto())

        return shapes.DescribeTagOptionOutput.from_boto(response)

    def disassociate_principal_from_portfolio(
        self,
        _request: shapes.DisassociatePrincipalFromPortfolioInput = None,
        *,
        portfolio_id: str,
        principal_arn: str,
        accept_language: str = ShapeBase.NOT_SET,
    ) -> shapes.DisassociatePrincipalFromPortfolioOutput:
        """
        Disassociates a previously associated principal ARN from a specified portfolio.
        """
        if _request is None:
            _params = {}
            if portfolio_id is not ShapeBase.NOT_SET:
                _params['portfolio_id'] = portfolio_id
            if principal_arn is not ShapeBase.NOT_SET:
                _params['principal_arn'] = principal_arn
            if accept_language is not ShapeBase.NOT_SET:
                _params['accept_language'] = accept_language
            _request = shapes.DisassociatePrincipalFromPortfolioInput(**_params)
        response = self._boto_client.disassociate_principal_from_portfolio(
            **_request.to_boto()
        )

        return shapes.DisassociatePrincipalFromPortfolioOutput.from_boto(
            response
        )

    def disassociate_product_from_portfolio(
        self,
        _request: shapes.DisassociateProductFromPortfolioInput = None,
        *,
        product_id: str,
        portfolio_id: str,
        accept_language: str = ShapeBase.NOT_SET,
    ) -> shapes.DisassociateProductFromPortfolioOutput:
        """
        Disassociates the specified product from the specified portfolio.
        """
        if _request is None:
            _params = {}
            if product_id is not ShapeBase.NOT_SET:
                _params['product_id'] = product_id
            if portfolio_id is not ShapeBase.NOT_SET:
                _params['portfolio_id'] = portfolio_id
            if accept_language is not ShapeBase.NOT_SET:
                _params['accept_language'] = accept_language
            _request = shapes.DisassociateProductFromPortfolioInput(**_params)
        response = self._boto_client.disassociate_product_from_portfolio(
            **_request.to_boto()
        )

        return shapes.DisassociateProductFromPortfolioOutput.from_boto(response)

    def disassociate_tag_option_from_resource(
        self,
        _request: shapes.DisassociateTagOptionFromResourceInput = None,
        *,
        resource_id: str,
        tag_option_id: str,
    ) -> shapes.DisassociateTagOptionFromResourceOutput:
        """
        Disassociates the specified TagOption from the specified resource.
        """
        if _request is None:
            _params = {}
            if resource_id is not ShapeBase.NOT_SET:
                _params['resource_id'] = resource_id
            if tag_option_id is not ShapeBase.NOT_SET:
                _params['tag_option_id'] = tag_option_id
            _request = shapes.DisassociateTagOptionFromResourceInput(**_params)
        response = self._boto_client.disassociate_tag_option_from_resource(
            **_request.to_boto()
        )

        return shapes.DisassociateTagOptionFromResourceOutput.from_boto(
            response
        )

    def execute_provisioned_product_plan(
        self,
        _request: shapes.ExecuteProvisionedProductPlanInput = None,
        *,
        plan_id: str,
        idempotency_token: str,
        accept_language: str = ShapeBase.NOT_SET,
    ) -> shapes.ExecuteProvisionedProductPlanOutput:
        """
        Provisions or modifies a product based on the resource changes for the specified
        plan.
        """
        if _request is None:
            _params = {}
            if plan_id is not ShapeBase.NOT_SET:
                _params['plan_id'] = plan_id
            if idempotency_token is not ShapeBase.NOT_SET:
                _params['idempotency_token'] = idempotency_token
            if accept_language is not ShapeBase.NOT_SET:
                _params['accept_language'] = accept_language
            _request = shapes.ExecuteProvisionedProductPlanInput(**_params)
        response = self._boto_client.execute_provisioned_product_plan(
            **_request.to_boto()
        )

        return shapes.ExecuteProvisionedProductPlanOutput.from_boto(response)

    def list_accepted_portfolio_shares(
        self,
        _request: shapes.ListAcceptedPortfolioSharesInput = None,
        *,
        accept_language: str = ShapeBase.NOT_SET,
        page_token: str = ShapeBase.NOT_SET,
        page_size: int = ShapeBase.NOT_SET,
        portfolio_share_type: typing.
        Union[str, shapes.PortfolioShareType] = ShapeBase.NOT_SET,
    ) -> shapes.ListAcceptedPortfolioSharesOutput:
        """
        Lists all portfolios for which sharing was accepted by this account.
        """
        if _request is None:
            _params = {}
            if accept_language is not ShapeBase.NOT_SET:
                _params['accept_language'] = accept_language
            if page_token is not ShapeBase.NOT_SET:
                _params['page_token'] = page_token
            if page_size is not ShapeBase.NOT_SET:
                _params['page_size'] = page_size
            if portfolio_share_type is not ShapeBase.NOT_SET:
                _params['portfolio_share_type'] = portfolio_share_type
            _request = shapes.ListAcceptedPortfolioSharesInput(**_params)
        paginator = self.get_paginator("list_accepted_portfolio_shares"
                                      ).paginate(**_request.to_boto())
        page_generator = (page for page in paginator)
        first_page = next(page_generator)
        result = shapes.ListAcceptedPortfolioSharesOutput.from_boto(first_page)
        result._page_iterator = page_generator
        return result

        return shapes.ListAcceptedPortfolioSharesOutput.from_boto(response)

    def list_constraints_for_portfolio(
        self,
        _request: shapes.ListConstraintsForPortfolioInput = None,
        *,
        portfolio_id: str,
        accept_language: str = ShapeBase.NOT_SET,
        product_id: str = ShapeBase.NOT_SET,
        page_size: int = ShapeBase.NOT_SET,
        page_token: str = ShapeBase.NOT_SET,
    ) -> shapes.ListConstraintsForPortfolioOutput:
        """
        Lists the constraints for the specified portfolio and product.
        """
        if _request is None:
            _params = {}
            if portfolio_id is not ShapeBase.NOT_SET:
                _params['portfolio_id'] = portfolio_id
            if accept_language is not ShapeBase.NOT_SET:
                _params['accept_language'] = accept_language
            if product_id is not ShapeBase.NOT_SET:
                _params['product_id'] = product_id
            if page_size is not ShapeBase.NOT_SET:
                _params['page_size'] = page_size
            if page_token is not ShapeBase.NOT_SET:
                _params['page_token'] = page_token
            _request = shapes.ListConstraintsForPortfolioInput(**_params)
        paginator = self.get_paginator("list_constraints_for_portfolio"
                                      ).paginate(**_request.to_boto())
        page_generator = (page for page in paginator)
        first_page = next(page_generator)
        result = shapes.ListConstraintsForPortfolioOutput.from_boto(first_page)
        result._page_iterator = page_generator
        return result

        return shapes.ListConstraintsForPortfolioOutput.from_boto(response)

    def list_launch_paths(
        self,
        _request: shapes.ListLaunchPathsInput = None,
        *,
        product_id: str,
        accept_language: str = ShapeBase.NOT_SET,
        page_size: int = ShapeBase.NOT_SET,
        page_token: str = ShapeBase.NOT_SET,
    ) -> shapes.ListLaunchPathsOutput:
        """
        Lists the paths to the specified product. A path is how the user has access to a
        specified product, and is necessary when provisioning a product. A path also
        determines the constraints put on the product.
        """
        if _request is None:
            _params = {}
            if product_id is not ShapeBase.NOT_SET:
                _params['product_id'] = product_id
            if accept_language is not ShapeBase.NOT_SET:
                _params['accept_language'] = accept_language
            if page_size is not ShapeBase.NOT_SET:
                _params['page_size'] = page_size
            if page_token is not ShapeBase.NOT_SET:
                _params['page_token'] = page_token
            _request = shapes.ListLaunchPathsInput(**_params)
        paginator = self.get_paginator("list_launch_paths").paginate(
            **_request.to_boto()
        )
        page_generator = (page for page in paginator)
        first_page = next(page_generator)
        result = shapes.ListLaunchPathsOutput.from_boto(first_page)
        result._page_iterator = page_generator
        return result

        return shapes.ListLaunchPathsOutput.from_boto(response)

    def list_portfolio_access(
        self,
        _request: shapes.ListPortfolioAccessInput = None,
        *,
        portfolio_id: str,
        accept_language: str = ShapeBase.NOT_SET,
    ) -> shapes.ListPortfolioAccessOutput:
        """
        Lists the account IDs that have access to the specified portfolio.
        """
        if _request is None:
            _params = {}
            if portfolio_id is not ShapeBase.NOT_SET:
                _params['portfolio_id'] = portfolio_id
            if accept_language is not ShapeBase.NOT_SET:
                _params['accept_language'] = accept_language
            _request = shapes.ListPortfolioAccessInput(**_params)
        response = self._boto_client.list_portfolio_access(**_request.to_boto())

        return shapes.ListPortfolioAccessOutput.from_boto(response)

    def list_portfolios(
        self,
        _request: shapes.ListPortfoliosInput = None,
        *,
        accept_language: str = ShapeBase.NOT_SET,
        page_token: str = ShapeBase.NOT_SET,
        page_size: int = ShapeBase.NOT_SET,
    ) -> shapes.ListPortfoliosOutput:
        """
        Lists all portfolios in the catalog.
        """
        if _request is None:
            _params = {}
            if accept_language is not ShapeBase.NOT_SET:
                _params['accept_language'] = accept_language
            if page_token is not ShapeBase.NOT_SET:
                _params['page_token'] = page_token
            if page_size is not ShapeBase.NOT_SET:
                _params['page_size'] = page_size
            _request = shapes.ListPortfoliosInput(**_params)
        paginator = self.get_paginator("list_portfolios").paginate(
            **_request.to_boto()
        )
        page_generator = (page for page in paginator)
        first_page = next(page_generator)
        result = shapes.ListPortfoliosOutput.from_boto(first_page)
        result._page_iterator = page_generator
        return result

        return shapes.ListPortfoliosOutput.from_boto(response)

    def list_portfolios_for_product(
        self,
        _request: shapes.ListPortfoliosForProductInput = None,
        *,
        product_id: str,
        accept_language: str = ShapeBase.NOT_SET,
        page_token: str = ShapeBase.NOT_SET,
        page_size: int = ShapeBase.NOT_SET,
    ) -> shapes.ListPortfoliosForProductOutput:
        """
        Lists all portfolios that the specified product is associated with.
        """
        if _request is None:
            _params = {}
            if product_id is not ShapeBase.NOT_SET:
                _params['product_id'] = product_id
            if accept_language is not ShapeBase.NOT_SET:
                _params['accept_language'] = accept_language
            if page_token is not ShapeBase.NOT_SET:
                _params['page_token'] = page_token
            if page_size is not ShapeBase.NOT_SET:
                _params['page_size'] = page_size
            _request = shapes.ListPortfoliosForProductInput(**_params)
        paginator = self.get_paginator("list_portfolios_for_product").paginate(
            **_request.to_boto()
        )
        page_generator = (page for page in paginator)
        first_page = next(page_generator)
        result = shapes.ListPortfoliosForProductOutput.from_boto(first_page)
        result._page_iterator = page_generator
        return result

        return shapes.ListPortfoliosForProductOutput.from_boto(response)

    def list_principals_for_portfolio(
        self,
        _request: shapes.ListPrincipalsForPortfolioInput = None,
        *,
        portfolio_id: str,
        accept_language: str = ShapeBase.NOT_SET,
        page_size: int = ShapeBase.NOT_SET,
        page_token: str = ShapeBase.NOT_SET,
    ) -> shapes.ListPrincipalsForPortfolioOutput:
        """
        Lists all principal ARNs associated with the specified portfolio.
        """
        if _request is None:
            _params = {}
            if portfolio_id is not ShapeBase.NOT_SET:
                _params['portfolio_id'] = portfolio_id
            if accept_language is not ShapeBase.NOT_SET:
                _params['accept_language'] = accept_language
            if page_size is not ShapeBase.NOT_SET:
                _params['page_size'] = page_size
            if page_token is not ShapeBase.NOT_SET:
                _params['page_token'] = page_token
            _request = shapes.ListPrincipalsForPortfolioInput(**_params)
        paginator = self.get_paginator("list_principals_for_portfolio"
                                      ).paginate(**_request.to_boto())
        page_generator = (page for page in paginator)
        first_page = next(page_generator)
        result = shapes.ListPrincipalsForPortfolioOutput.from_boto(first_page)
        result._page_iterator = page_generator
        return result

        return shapes.ListPrincipalsForPortfolioOutput.from_boto(response)

    def list_provisioned_product_plans(
        self,
        _request: shapes.ListProvisionedProductPlansInput = None,
        *,
        accept_language: str = ShapeBase.NOT_SET,
        provision_product_id: str = ShapeBase.NOT_SET,
        page_size: int = ShapeBase.NOT_SET,
        page_token: str = ShapeBase.NOT_SET,
        access_level_filter: shapes.AccessLevelFilter = ShapeBase.NOT_SET,
    ) -> shapes.ListProvisionedProductPlansOutput:
        """
        Lists the plans for the specified provisioned product or all plans to which the
        user has access.
        """
        if _request is None:
            _params = {}
            if accept_language is not ShapeBase.NOT_SET:
                _params['accept_language'] = accept_language
            if provision_product_id is not ShapeBase.NOT_SET:
                _params['provision_product_id'] = provision_product_id
            if page_size is not ShapeBase.NOT_SET:
                _params['page_size'] = page_size
            if page_token is not ShapeBase.NOT_SET:
                _params['page_token'] = page_token
            if access_level_filter is not ShapeBase.NOT_SET:
                _params['access_level_filter'] = access_level_filter
            _request = shapes.ListProvisionedProductPlansInput(**_params)
        response = self._boto_client.list_provisioned_product_plans(
            **_request.to_boto()
        )

        return shapes.ListProvisionedProductPlansOutput.from_boto(response)

    def list_provisioning_artifacts(
        self,
        _request: shapes.ListProvisioningArtifactsInput = None,
        *,
        product_id: str,
        accept_language: str = ShapeBase.NOT_SET,
    ) -> shapes.ListProvisioningArtifactsOutput:
        """
        Lists all provisioning artifacts (also known as versions) for the specified
        product.
        """
        if _request is None:
            _params = {}
            if product_id is not ShapeBase.NOT_SET:
                _params['product_id'] = product_id
            if accept_language is not ShapeBase.NOT_SET:
                _params['accept_language'] = accept_language
            _request = shapes.ListProvisioningArtifactsInput(**_params)
        response = self._boto_client.list_provisioning_artifacts(
            **_request.to_boto()
        )

        return shapes.ListProvisioningArtifactsOutput.from_boto(response)

    def list_record_history(
        self,
        _request: shapes.ListRecordHistoryInput = None,
        *,
        accept_language: str = ShapeBase.NOT_SET,
        access_level_filter: shapes.AccessLevelFilter = ShapeBase.NOT_SET,
        search_filter: shapes.ListRecordHistorySearchFilter = ShapeBase.NOT_SET,
        page_size: int = ShapeBase.NOT_SET,
        page_token: str = ShapeBase.NOT_SET,
    ) -> shapes.ListRecordHistoryOutput:
        """
        Lists the specified requests or all performed requests.
        """
        if _request is None:
            _params = {}
            if accept_language is not ShapeBase.NOT_SET:
                _params['accept_language'] = accept_language
            if access_level_filter is not ShapeBase.NOT_SET:
                _params['access_level_filter'] = access_level_filter
            if search_filter is not ShapeBase.NOT_SET:
                _params['search_filter'] = search_filter
            if page_size is not ShapeBase.NOT_SET:
                _params['page_size'] = page_size
            if page_token is not ShapeBase.NOT_SET:
                _params['page_token'] = page_token
            _request = shapes.ListRecordHistoryInput(**_params)
        response = self._boto_client.list_record_history(**_request.to_boto())

        return shapes.ListRecordHistoryOutput.from_boto(response)

    def list_resources_for_tag_option(
        self,
        _request: shapes.ListResourcesForTagOptionInput = None,
        *,
        tag_option_id: str,
        resource_type: str = ShapeBase.NOT_SET,
        page_size: int = ShapeBase.NOT_SET,
        page_token: str = ShapeBase.NOT_SET,
    ) -> shapes.ListResourcesForTagOptionOutput:
        """
        Lists the resources associated with the specified TagOption.
        """
        if _request is None:
            _params = {}
            if tag_option_id is not ShapeBase.NOT_SET:
                _params['tag_option_id'] = tag_option_id
            if resource_type is not ShapeBase.NOT_SET:
                _params['resource_type'] = resource_type
            if page_size is not ShapeBase.NOT_SET:
                _params['page_size'] = page_size
            if page_token is not ShapeBase.NOT_SET:
                _params['page_token'] = page_token
            _request = shapes.ListResourcesForTagOptionInput(**_params)
        paginator = self.get_paginator("list_resources_for_tag_option"
                                      ).paginate(**_request.to_boto())
        page_generator = (page for page in paginator)
        first_page = next(page_generator)
        result = shapes.ListResourcesForTagOptionOutput.from_boto(first_page)
        result._page_iterator = page_generator
        return result

        return shapes.ListResourcesForTagOptionOutput.from_boto(response)

    def list_tag_options(
        self,
        _request: shapes.ListTagOptionsInput = None,
        *,
        filters: shapes.ListTagOptionsFilters = ShapeBase.NOT_SET,
        page_size: int = ShapeBase.NOT_SET,
        page_token: str = ShapeBase.NOT_SET,
    ) -> shapes.ListTagOptionsOutput:
        """
        Lists the specified TagOptions or all TagOptions.
        """
        if _request is None:
            _params = {}
            if filters is not ShapeBase.NOT_SET:
                _params['filters'] = filters
            if page_size is not ShapeBase.NOT_SET:
                _params['page_size'] = page_size
            if page_token is not ShapeBase.NOT_SET:
                _params['page_token'] = page_token
            _request = shapes.ListTagOptionsInput(**_params)
        paginator = self.get_paginator("list_tag_options").paginate(
            **_request.to_boto()
        )
        page_generator = (page for page in paginator)
        first_page = next(page_generator)
        result = shapes.ListTagOptionsOutput.from_boto(first_page)
        result._page_iterator = page_generator
        return result

        return shapes.ListTagOptionsOutput.from_boto(response)

    def provision_product(
        self,
        _request: shapes.ProvisionProductInput = None,
        *,
        product_id: str,
        provisioning_artifact_id: str,
        provisioned_product_name: str,
        provision_token: str,
        accept_language: str = ShapeBase.NOT_SET,
        path_id: str = ShapeBase.NOT_SET,
        provisioning_parameters: typing.List[shapes.ProvisioningParameter
                                            ] = ShapeBase.NOT_SET,
        tags: typing.List[shapes.Tag] = ShapeBase.NOT_SET,
        notification_arns: typing.List[str] = ShapeBase.NOT_SET,
    ) -> shapes.ProvisionProductOutput:
        """
        Provisions the specified product.

        A provisioned product is a resourced instance of a product. For example,
        provisioning a product based on a CloudFormation template launches a
        CloudFormation stack and its underlying resources. You can check the status of
        this request using DescribeRecord.

        If the request contains a tag key with an empty list of values, there is a tag
        conflict for that key. Do not include conflicted keys as tags, or this causes
        the error "Parameter validation failed: Missing required parameter in Tags[ _N_
        ]: _Value_ ".
        """
        if _request is None:
            _params = {}
            if product_id is not ShapeBase.NOT_SET:
                _params['product_id'] = product_id
            if provisioning_artifact_id is not ShapeBase.NOT_SET:
                _params['provisioning_artifact_id'] = provisioning_artifact_id
            if provisioned_product_name is not ShapeBase.NOT_SET:
                _params['provisioned_product_name'] = provisioned_product_name
            if provision_token is not ShapeBase.NOT_SET:
                _params['provision_token'] = provision_token
            if accept_language is not ShapeBase.NOT_SET:
                _params['accept_language'] = accept_language
            if path_id is not ShapeBase.NOT_SET:
                _params['path_id'] = path_id
            if provisioning_parameters is not ShapeBase.NOT_SET:
                _params['provisioning_parameters'] = provisioning_parameters
            if tags is not ShapeBase.NOT_SET:
                _params['tags'] = tags
            if notification_arns is not ShapeBase.NOT_SET:
                _params['notification_arns'] = notification_arns
            _request = shapes.ProvisionProductInput(**_params)
        response = self._boto_client.provision_product(**_request.to_boto())

        return shapes.ProvisionProductOutput.from_boto(response)

    def reject_portfolio_share(
        self,
        _request: shapes.RejectPortfolioShareInput = None,
        *,
        portfolio_id: str,
        accept_language: str = ShapeBase.NOT_SET,
    ) -> shapes.RejectPortfolioShareOutput:
        """
        Rejects an offer to share the specified portfolio.
        """
        if _request is None:
            _params = {}
            if portfolio_id is not ShapeBase.NOT_SET:
                _params['portfolio_id'] = portfolio_id
            if accept_language is not ShapeBase.NOT_SET:
                _params['accept_language'] = accept_language
            _request = shapes.RejectPortfolioShareInput(**_params)
        response = self._boto_client.reject_portfolio_share(
            **_request.to_boto()
        )

        return shapes.RejectPortfolioShareOutput.from_boto(response)

    def scan_provisioned_products(
        self,
        _request: shapes.ScanProvisionedProductsInput = None,
        *,
        accept_language: str = ShapeBase.NOT_SET,
        access_level_filter: shapes.AccessLevelFilter = ShapeBase.NOT_SET,
        page_size: int = ShapeBase.NOT_SET,
        page_token: str = ShapeBase.NOT_SET,
    ) -> shapes.ScanProvisionedProductsOutput:
        """
        Lists the provisioned products that are available (not terminated).

        To use additional filtering, see SearchProvisionedProducts.
        """
        if _request is None:
            _params = {}
            if accept_language is not ShapeBase.NOT_SET:
                _params['accept_language'] = accept_language
            if access_level_filter is not ShapeBase.NOT_SET:
                _params['access_level_filter'] = access_level_filter
            if page_size is not ShapeBase.NOT_SET:
                _params['page_size'] = page_size
            if page_token is not ShapeBase.NOT_SET:
                _params['page_token'] = page_token
            _request = shapes.ScanProvisionedProductsInput(**_params)
        response = self._boto_client.scan_provisioned_products(
            **_request.to_boto()
        )

        return shapes.ScanProvisionedProductsOutput.from_boto(response)

    def search_products(
        self,
        _request: shapes.SearchProductsInput = None,
        *,
        accept_language: str = ShapeBase.NOT_SET,
        filters: typing.Dict[typing.Union[str, shapes.ProductViewFilterBy],
                             typing.List[str]] = ShapeBase.NOT_SET,
        page_size: int = ShapeBase.NOT_SET,
        sort_by: typing.Union[str, shapes.ProductViewSortBy] = ShapeBase.
        NOT_SET,
        sort_order: typing.Union[str, shapes.SortOrder] = ShapeBase.NOT_SET,
        page_token: str = ShapeBase.NOT_SET,
    ) -> shapes.SearchProductsOutput:
        """
        Gets information about the products to which the caller has access.
        """
        if _request is None:
            _params = {}
            if accept_language is not ShapeBase.NOT_SET:
                _params['accept_language'] = accept_language
            if filters is not ShapeBase.NOT_SET:
                _params['filters'] = filters
            if page_size is not ShapeBase.NOT_SET:
                _params['page_size'] = page_size
            if sort_by is not ShapeBase.NOT_SET:
                _params['sort_by'] = sort_by
            if sort_order is not ShapeBase.NOT_SET:
                _params['sort_order'] = sort_order
            if page_token is not ShapeBase.NOT_SET:
                _params['page_token'] = page_token
            _request = shapes.SearchProductsInput(**_params)
        response = self._boto_client.search_products(**_request.to_boto())

        return shapes.SearchProductsOutput.from_boto(response)

    def search_products_as_admin(
        self,
        _request: shapes.SearchProductsAsAdminInput = None,
        *,
        accept_language: str = ShapeBase.NOT_SET,
        portfolio_id: str = ShapeBase.NOT_SET,
        filters: typing.Dict[typing.Union[str, shapes.ProductViewFilterBy],
                             typing.List[str]] = ShapeBase.NOT_SET,
        sort_by: typing.Union[str, shapes.
                              ProductViewSortBy] = ShapeBase.NOT_SET,
        sort_order: typing.Union[str, shapes.SortOrder] = ShapeBase.NOT_SET,
        page_token: str = ShapeBase.NOT_SET,
        page_size: int = ShapeBase.NOT_SET,
        product_source: typing.Union[str, shapes.ProductSource] = ShapeBase.
        NOT_SET,
    ) -> shapes.SearchProductsAsAdminOutput:
        """
        Gets information about the products for the specified portfolio or all products.
        """
        if _request is None:
            _params = {}
            if accept_language is not ShapeBase.NOT_SET:
                _params['accept_language'] = accept_language
            if portfolio_id is not ShapeBase.NOT_SET:
                _params['portfolio_id'] = portfolio_id
            if filters is not ShapeBase.NOT_SET:
                _params['filters'] = filters
            if sort_by is not ShapeBase.NOT_SET:
                _params['sort_by'] = sort_by
            if sort_order is not ShapeBase.NOT_SET:
                _params['sort_order'] = sort_order
            if page_token is not ShapeBase.NOT_SET:
                _params['page_token'] = page_token
            if page_size is not ShapeBase.NOT_SET:
                _params['page_size'] = page_size
            if product_source is not ShapeBase.NOT_SET:
                _params['product_source'] = product_source
            _request = shapes.SearchProductsAsAdminInput(**_params)
        paginator = self.get_paginator("search_products_as_admin").paginate(
            **_request.to_boto()
        )
        page_generator = (page for page in paginator)
        first_page = next(page_generator)
        result = shapes.SearchProductsAsAdminOutput.from_boto(first_page)
        result._page_iterator = page_generator
        return result

        return shapes.SearchProductsAsAdminOutput.from_boto(response)

    def search_provisioned_products(
        self,
        _request: shapes.SearchProvisionedProductsInput = None,
        *,
        accept_language: str = ShapeBase.NOT_SET,
        access_level_filter: shapes.AccessLevelFilter = ShapeBase.NOT_SET,
        filters: typing.
        Dict[typing.Union[str, shapes.ProvisionedProductViewFilterBy], typing.
             List[str]] = ShapeBase.NOT_SET,
        sort_by: str = ShapeBase.NOT_SET,
        sort_order: typing.Union[str, shapes.SortOrder] = ShapeBase.NOT_SET,
        page_size: int = ShapeBase.NOT_SET,
        page_token: str = ShapeBase.NOT_SET,
    ) -> shapes.SearchProvisionedProductsOutput:
        """
        Gets information about the provisioned products that meet the specified
        criteria.
        """
        if _request is None:
            _params = {}
            if accept_language is not ShapeBase.NOT_SET:
                _params['accept_language'] = accept_language
            if access_level_filter is not ShapeBase.NOT_SET:
                _params['access_level_filter'] = access_level_filter
            if filters is not ShapeBase.NOT_SET:
                _params['filters'] = filters
            if sort_by is not ShapeBase.NOT_SET:
                _params['sort_by'] = sort_by
            if sort_order is not ShapeBase.NOT_SET:
                _params['sort_order'] = sort_order
            if page_size is not ShapeBase.NOT_SET:
                _params['page_size'] = page_size
            if page_token is not ShapeBase.NOT_SET:
                _params['page_token'] = page_token
            _request = shapes.SearchProvisionedProductsInput(**_params)
        response = self._boto_client.search_provisioned_products(
            **_request.to_boto()
        )

        return shapes.SearchProvisionedProductsOutput.from_boto(response)

    def terminate_provisioned_product(
        self,
        _request: shapes.TerminateProvisionedProductInput = None,
        *,
        terminate_token: str,
        provisioned_product_name: str = ShapeBase.NOT_SET,
        provisioned_product_id: str = ShapeBase.NOT_SET,
        ignore_errors: bool = ShapeBase.NOT_SET,
        accept_language: str = ShapeBase.NOT_SET,
    ) -> shapes.TerminateProvisionedProductOutput:
        """
        Terminates the specified provisioned product.

        This operation does not delete any records associated with the provisioned
        product.

        You can check the status of this request using DescribeRecord.
        """
        if _request is None:
            _params = {}
            if terminate_token is not ShapeBase.NOT_SET:
                _params['terminate_token'] = terminate_token
            if provisioned_product_name is not ShapeBase.NOT_SET:
                _params['provisioned_product_name'] = provisioned_product_name
            if provisioned_product_id is not ShapeBase.NOT_SET:
                _params['provisioned_product_id'] = provisioned_product_id
            if ignore_errors is not ShapeBase.NOT_SET:
                _params['ignore_errors'] = ignore_errors
            if accept_language is not ShapeBase.NOT_SET:
                _params['accept_language'] = accept_language
            _request = shapes.TerminateProvisionedProductInput(**_params)
        response = self._boto_client.terminate_provisioned_product(
            **_request.to_boto()
        )

        return shapes.TerminateProvisionedProductOutput.from_boto(response)

    def update_constraint(
        self,
        _request: shapes.UpdateConstraintInput = None,
        *,
        id: str,
        accept_language: str = ShapeBase.NOT_SET,
        description: str = ShapeBase.NOT_SET,
    ) -> shapes.UpdateConstraintOutput:
        """
        Updates the specified constraint.
        """
        if _request is None:
            _params = {}
            if id is not ShapeBase.NOT_SET:
                _params['id'] = id
            if accept_language is not ShapeBase.NOT_SET:
                _params['accept_language'] = accept_language
            if description is not ShapeBase.NOT_SET:
                _params['description'] = description
            _request = shapes.UpdateConstraintInput(**_params)
        response = self._boto_client.update_constraint(**_request.to_boto())

        return shapes.UpdateConstraintOutput.from_boto(response)

    def update_portfolio(
        self,
        _request: shapes.UpdatePortfolioInput = None,
        *,
        id: str,
        accept_language: str = ShapeBase.NOT_SET,
        display_name: str = ShapeBase.NOT_SET,
        description: str = ShapeBase.NOT_SET,
        provider_name: str = ShapeBase.NOT_SET,
        add_tags: typing.List[shapes.Tag] = ShapeBase.NOT_SET,
        remove_tags: typing.List[str] = ShapeBase.NOT_SET,
    ) -> shapes.UpdatePortfolioOutput:
        """
        Updates the specified portfolio.

        You cannot update a product that was shared with you.
        """
        if _request is None:
            _params = {}
            if id is not ShapeBase.NOT_SET:
                _params['id'] = id
            if accept_language is not ShapeBase.NOT_SET:
                _params['accept_language'] = accept_language
            if display_name is not ShapeBase.NOT_SET:
                _params['display_name'] = display_name
            if description is not ShapeBase.NOT_SET:
                _params['description'] = description
            if provider_name is not ShapeBase.NOT_SET:
                _params['provider_name'] = provider_name
            if add_tags is not ShapeBase.NOT_SET:
                _params['add_tags'] = add_tags
            if remove_tags is not ShapeBase.NOT_SET:
                _params['remove_tags'] = remove_tags
            _request = shapes.UpdatePortfolioInput(**_params)
        response = self._boto_client.update_portfolio(**_request.to_boto())

        return shapes.UpdatePortfolioOutput.from_boto(response)

    def update_product(
        self,
        _request: shapes.UpdateProductInput = None,
        *,
        id: str,
        accept_language: str = ShapeBase.NOT_SET,
        name: str = ShapeBase.NOT_SET,
        owner: str = ShapeBase.NOT_SET,
        description: str = ShapeBase.NOT_SET,
        distributor: str = ShapeBase.NOT_SET,
        support_description: str = ShapeBase.NOT_SET,
        support_email: str = ShapeBase.NOT_SET,
        support_url: str = ShapeBase.NOT_SET,
        add_tags: typing.List[shapes.Tag] = ShapeBase.NOT_SET,
        remove_tags: typing.List[str] = ShapeBase.NOT_SET,
    ) -> shapes.UpdateProductOutput:
        """
        Updates the specified product.
        """
        if _request is None:
            _params = {}
            if id is not ShapeBase.NOT_SET:
                _params['id'] = id
            if accept_language is not ShapeBase.NOT_SET:
                _params['accept_language'] = accept_language
            if name is not ShapeBase.NOT_SET:
                _params['name'] = name
            if owner is not ShapeBase.NOT_SET:
                _params['owner'] = owner
            if description is not ShapeBase.NOT_SET:
                _params['description'] = description
            if distributor is not ShapeBase.NOT_SET:
                _params['distributor'] = distributor
            if support_description is not ShapeBase.NOT_SET:
                _params['support_description'] = support_description
            if support_email is not ShapeBase.NOT_SET:
                _params['support_email'] = support_email
            if support_url is not ShapeBase.NOT_SET:
                _params['support_url'] = support_url
            if add_tags is not ShapeBase.NOT_SET:
                _params['add_tags'] = add_tags
            if remove_tags is not ShapeBase.NOT_SET:
                _params['remove_tags'] = remove_tags
            _request = shapes.UpdateProductInput(**_params)
        response = self._boto_client.update_product(**_request.to_boto())

        return shapes.UpdateProductOutput.from_boto(response)

    def update_provisioned_product(
        self,
        _request: shapes.UpdateProvisionedProductInput = None,
        *,
        update_token: str,
        accept_language: str = ShapeBase.NOT_SET,
        provisioned_product_name: str = ShapeBase.NOT_SET,
        provisioned_product_id: str = ShapeBase.NOT_SET,
        product_id: str = ShapeBase.NOT_SET,
        provisioning_artifact_id: str = ShapeBase.NOT_SET,
        path_id: str = ShapeBase.NOT_SET,
        provisioning_parameters: typing.List[shapes.UpdateProvisioningParameter
                                            ] = ShapeBase.NOT_SET,
    ) -> shapes.UpdateProvisionedProductOutput:
        """
        Requests updates to the configuration of the specified provisioned product.

        If there are tags associated with the object, they cannot be updated or added.
        Depending on the specific updates requested, this operation can update with no
        interruption, with some interruption, or replace the provisioned product
        entirely.

        You can check the status of this request using DescribeRecord.
        """
        if _request is None:
            _params = {}
            if update_token is not ShapeBase.NOT_SET:
                _params['update_token'] = update_token
            if accept_language is not ShapeBase.NOT_SET:
                _params['accept_language'] = accept_language
            if provisioned_product_name is not ShapeBase.NOT_SET:
                _params['provisioned_product_name'] = provisioned_product_name
            if provisioned_product_id is not ShapeBase.NOT_SET:
                _params['provisioned_product_id'] = provisioned_product_id
            if product_id is not ShapeBase.NOT_SET:
                _params['product_id'] = product_id
            if provisioning_artifact_id is not ShapeBase.NOT_SET:
                _params['provisioning_artifact_id'] = provisioning_artifact_id
            if path_id is not ShapeBase.NOT_SET:
                _params['path_id'] = path_id
            if provisioning_parameters is not ShapeBase.NOT_SET:
                _params['provisioning_parameters'] = provisioning_parameters
            _request = shapes.UpdateProvisionedProductInput(**_params)
        response = self._boto_client.update_provisioned_product(
            **_request.to_boto()
        )

        return shapes.UpdateProvisionedProductOutput.from_boto(response)

    def update_provisioning_artifact(
        self,
        _request: shapes.UpdateProvisioningArtifactInput = None,
        *,
        product_id: str,
        provisioning_artifact_id: str,
        accept_language: str = ShapeBase.NOT_SET,
        name: str = ShapeBase.NOT_SET,
        description: str = ShapeBase.NOT_SET,
        active: bool = ShapeBase.NOT_SET,
    ) -> shapes.UpdateProvisioningArtifactOutput:
        """
        Updates the specified provisioning artifact (also known as a version) for the
        specified product.

        You cannot update a provisioning artifact for a product that was shared with
        you.
        """
        if _request is None:
            _params = {}
            if product_id is not ShapeBase.NOT_SET:
                _params['product_id'] = product_id
            if provisioning_artifact_id is not ShapeBase.NOT_SET:
                _params['provisioning_artifact_id'] = provisioning_artifact_id
            if accept_language is not ShapeBase.NOT_SET:
                _params['accept_language'] = accept_language
            if name is not ShapeBase.NOT_SET:
                _params['name'] = name
            if description is not ShapeBase.NOT_SET:
                _params['description'] = description
            if active is not ShapeBase.NOT_SET:
                _params['active'] = active
            _request = shapes.UpdateProvisioningArtifactInput(**_params)
        response = self._boto_client.update_provisioning_artifact(
            **_request.to_boto()
        )

        return shapes.UpdateProvisioningArtifactOutput.from_boto(response)

    def update_tag_option(
        self,
        _request: shapes.UpdateTagOptionInput = None,
        *,
        id: str,
        value: str = ShapeBase.NOT_SET,
        active: bool = ShapeBase.NOT_SET,
    ) -> shapes.UpdateTagOptionOutput:
        """
        Updates the specified TagOption.
        """
        if _request is None:
            _params = {}
            if id is not ShapeBase.NOT_SET:
                _params['id'] = id
            if value is not ShapeBase.NOT_SET:
                _params['value'] = value
            if active is not ShapeBase.NOT_SET:
                _params['active'] = active
            _request = shapes.UpdateTagOptionInput(**_params)
        response = self._boto_client.update_tag_option(**_request.to_boto())

        return shapes.UpdateTagOptionOutput.from_boto(response)
