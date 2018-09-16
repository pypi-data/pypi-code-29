import datetime
import typing
import boto3
from autoboto import ClientBase, ShapeBase, OutputShapeBase
from . import shapes


class Client(ClientBase):
    def __init__(self, *args, **kwargs):
        super().__init__("cloudsearch", *args, **kwargs)

    def build_suggesters(
        self,
        _request: shapes.BuildSuggestersRequest = None,
        *,
        domain_name: str,
    ) -> shapes.BuildSuggestersResponse:
        """
        Indexes the search suggestions. For more information, see [Configuring
        Suggesters](http://docs.aws.amazon.com/cloudsearch/latest/developerguide/getting-
        suggestions.html#configuring-suggesters) in the _Amazon CloudSearch Developer
        Guide_.
        """
        if _request is None:
            _params = {}
            if domain_name is not ShapeBase.NOT_SET:
                _params['domain_name'] = domain_name
            _request = shapes.BuildSuggestersRequest(**_params)
        response = self._boto_client.build_suggesters(**_request.to_boto())

        return shapes.BuildSuggestersResponse.from_boto(response)

    def create_domain(
        self,
        _request: shapes.CreateDomainRequest = None,
        *,
        domain_name: str,
    ) -> shapes.CreateDomainResponse:
        """
        Creates a new search domain. For more information, see [Creating a Search
        Domain](http://docs.aws.amazon.com/cloudsearch/latest/developerguide/creating-
        domains.html) in the _Amazon CloudSearch Developer Guide_.
        """
        if _request is None:
            _params = {}
            if domain_name is not ShapeBase.NOT_SET:
                _params['domain_name'] = domain_name
            _request = shapes.CreateDomainRequest(**_params)
        response = self._boto_client.create_domain(**_request.to_boto())

        return shapes.CreateDomainResponse.from_boto(response)

    def define_analysis_scheme(
        self,
        _request: shapes.DefineAnalysisSchemeRequest = None,
        *,
        domain_name: str,
        analysis_scheme: shapes.AnalysisScheme,
    ) -> shapes.DefineAnalysisSchemeResponse:
        """
        Configures an analysis scheme that can be applied to a `text` or `text-array`
        field to define language-specific text processing options. For more information,
        see [Configuring Analysis
        Schemes](http://docs.aws.amazon.com/cloudsearch/latest/developerguide/configuring-
        analysis-schemes.html) in the _Amazon CloudSearch Developer Guide_.
        """
        if _request is None:
            _params = {}
            if domain_name is not ShapeBase.NOT_SET:
                _params['domain_name'] = domain_name
            if analysis_scheme is not ShapeBase.NOT_SET:
                _params['analysis_scheme'] = analysis_scheme
            _request = shapes.DefineAnalysisSchemeRequest(**_params)
        response = self._boto_client.define_analysis_scheme(
            **_request.to_boto()
        )

        return shapes.DefineAnalysisSchemeResponse.from_boto(response)

    def define_expression(
        self,
        _request: shapes.DefineExpressionRequest = None,
        *,
        domain_name: str,
        expression: shapes.Expression,
    ) -> shapes.DefineExpressionResponse:
        """
        Configures an `Expression` for the search domain. Used to create new expressions
        and modify existing ones. If the expression exists, the new configuration
        replaces the old one. For more information, see [Configuring
        Expressions](http://docs.aws.amazon.com/cloudsearch/latest/developerguide/configuring-
        expressions.html) in the _Amazon CloudSearch Developer Guide_.
        """
        if _request is None:
            _params = {}
            if domain_name is not ShapeBase.NOT_SET:
                _params['domain_name'] = domain_name
            if expression is not ShapeBase.NOT_SET:
                _params['expression'] = expression
            _request = shapes.DefineExpressionRequest(**_params)
        response = self._boto_client.define_expression(**_request.to_boto())

        return shapes.DefineExpressionResponse.from_boto(response)

    def define_index_field(
        self,
        _request: shapes.DefineIndexFieldRequest = None,
        *,
        domain_name: str,
        index_field: shapes.IndexField,
    ) -> shapes.DefineIndexFieldResponse:
        """
        Configures an `IndexField` for the search domain. Used to create new fields and
        modify existing ones. You must specify the name of the domain you are
        configuring and an index field configuration. The index field configuration
        specifies a unique name, the index field type, and the options you want to
        configure for the field. The options you can specify depend on the
        `IndexFieldType`. If the field exists, the new configuration replaces the old
        one. For more information, see [Configuring Index
        Fields](http://docs.aws.amazon.com/cloudsearch/latest/developerguide/configuring-
        index-fields.html) in the _Amazon CloudSearch Developer Guide_.
        """
        if _request is None:
            _params = {}
            if domain_name is not ShapeBase.NOT_SET:
                _params['domain_name'] = domain_name
            if index_field is not ShapeBase.NOT_SET:
                _params['index_field'] = index_field
            _request = shapes.DefineIndexFieldRequest(**_params)
        response = self._boto_client.define_index_field(**_request.to_boto())

        return shapes.DefineIndexFieldResponse.from_boto(response)

    def define_suggester(
        self,
        _request: shapes.DefineSuggesterRequest = None,
        *,
        domain_name: str,
        suggester: shapes.Suggester,
    ) -> shapes.DefineSuggesterResponse:
        """
        Configures a suggester for a domain. A suggester enables you to display possible
        matches before users finish typing their queries. When you configure a
        suggester, you must specify the name of the text field you want to search for
        possible matches and a unique name for the suggester. For more information, see
        [Getting Search
        Suggestions](http://docs.aws.amazon.com/cloudsearch/latest/developerguide/getting-
        suggestions.html) in the _Amazon CloudSearch Developer Guide_.
        """
        if _request is None:
            _params = {}
            if domain_name is not ShapeBase.NOT_SET:
                _params['domain_name'] = domain_name
            if suggester is not ShapeBase.NOT_SET:
                _params['suggester'] = suggester
            _request = shapes.DefineSuggesterRequest(**_params)
        response = self._boto_client.define_suggester(**_request.to_boto())

        return shapes.DefineSuggesterResponse.from_boto(response)

    def delete_analysis_scheme(
        self,
        _request: shapes.DeleteAnalysisSchemeRequest = None,
        *,
        domain_name: str,
        analysis_scheme_name: str,
    ) -> shapes.DeleteAnalysisSchemeResponse:
        """
        Deletes an analysis scheme. For more information, see [Configuring Analysis
        Schemes](http://docs.aws.amazon.com/cloudsearch/latest/developerguide/configuring-
        analysis-schemes.html) in the _Amazon CloudSearch Developer Guide_.
        """
        if _request is None:
            _params = {}
            if domain_name is not ShapeBase.NOT_SET:
                _params['domain_name'] = domain_name
            if analysis_scheme_name is not ShapeBase.NOT_SET:
                _params['analysis_scheme_name'] = analysis_scheme_name
            _request = shapes.DeleteAnalysisSchemeRequest(**_params)
        response = self._boto_client.delete_analysis_scheme(
            **_request.to_boto()
        )

        return shapes.DeleteAnalysisSchemeResponse.from_boto(response)

    def delete_domain(
        self,
        _request: shapes.DeleteDomainRequest = None,
        *,
        domain_name: str,
    ) -> shapes.DeleteDomainResponse:
        """
        Permanently deletes a search domain and all of its data. Once a domain has been
        deleted, it cannot be recovered. For more information, see [Deleting a Search
        Domain](http://docs.aws.amazon.com/cloudsearch/latest/developerguide/deleting-
        domains.html) in the _Amazon CloudSearch Developer Guide_.
        """
        if _request is None:
            _params = {}
            if domain_name is not ShapeBase.NOT_SET:
                _params['domain_name'] = domain_name
            _request = shapes.DeleteDomainRequest(**_params)
        response = self._boto_client.delete_domain(**_request.to_boto())

        return shapes.DeleteDomainResponse.from_boto(response)

    def delete_expression(
        self,
        _request: shapes.DeleteExpressionRequest = None,
        *,
        domain_name: str,
        expression_name: str,
    ) -> shapes.DeleteExpressionResponse:
        """
        Removes an `Expression` from the search domain. For more information, see
        [Configuring
        Expressions](http://docs.aws.amazon.com/cloudsearch/latest/developerguide/configuring-
        expressions.html) in the _Amazon CloudSearch Developer Guide_.
        """
        if _request is None:
            _params = {}
            if domain_name is not ShapeBase.NOT_SET:
                _params['domain_name'] = domain_name
            if expression_name is not ShapeBase.NOT_SET:
                _params['expression_name'] = expression_name
            _request = shapes.DeleteExpressionRequest(**_params)
        response = self._boto_client.delete_expression(**_request.to_boto())

        return shapes.DeleteExpressionResponse.from_boto(response)

    def delete_index_field(
        self,
        _request: shapes.DeleteIndexFieldRequest = None,
        *,
        domain_name: str,
        index_field_name: str,
    ) -> shapes.DeleteIndexFieldResponse:
        """
        Removes an `IndexField` from the search domain. For more information, see
        [Configuring Index
        Fields](http://docs.aws.amazon.com/cloudsearch/latest/developerguide/configuring-
        index-fields.html) in the _Amazon CloudSearch Developer Guide_.
        """
        if _request is None:
            _params = {}
            if domain_name is not ShapeBase.NOT_SET:
                _params['domain_name'] = domain_name
            if index_field_name is not ShapeBase.NOT_SET:
                _params['index_field_name'] = index_field_name
            _request = shapes.DeleteIndexFieldRequest(**_params)
        response = self._boto_client.delete_index_field(**_request.to_boto())

        return shapes.DeleteIndexFieldResponse.from_boto(response)

    def delete_suggester(
        self,
        _request: shapes.DeleteSuggesterRequest = None,
        *,
        domain_name: str,
        suggester_name: str,
    ) -> shapes.DeleteSuggesterResponse:
        """
        Deletes a suggester. For more information, see [Getting Search
        Suggestions](http://docs.aws.amazon.com/cloudsearch/latest/developerguide/getting-
        suggestions.html) in the _Amazon CloudSearch Developer Guide_.
        """
        if _request is None:
            _params = {}
            if domain_name is not ShapeBase.NOT_SET:
                _params['domain_name'] = domain_name
            if suggester_name is not ShapeBase.NOT_SET:
                _params['suggester_name'] = suggester_name
            _request = shapes.DeleteSuggesterRequest(**_params)
        response = self._boto_client.delete_suggester(**_request.to_boto())

        return shapes.DeleteSuggesterResponse.from_boto(response)

    def describe_analysis_schemes(
        self,
        _request: shapes.DescribeAnalysisSchemesRequest = None,
        *,
        domain_name: str,
        analysis_scheme_names: typing.List[str] = ShapeBase.NOT_SET,
        deployed: bool = ShapeBase.NOT_SET,
    ) -> shapes.DescribeAnalysisSchemesResponse:
        """
        Gets the analysis schemes configured for a domain. An analysis scheme defines
        language-specific text processing options for a `text` field. Can be limited to
        specific analysis schemes by name. By default, shows all analysis schemes and
        includes any pending changes to the configuration. Set the `Deployed` option to
        `true` to show the active configuration and exclude pending changes. For more
        information, see [Configuring Analysis
        Schemes](http://docs.aws.amazon.com/cloudsearch/latest/developerguide/configuring-
        analysis-schemes.html) in the _Amazon CloudSearch Developer Guide_.
        """
        if _request is None:
            _params = {}
            if domain_name is not ShapeBase.NOT_SET:
                _params['domain_name'] = domain_name
            if analysis_scheme_names is not ShapeBase.NOT_SET:
                _params['analysis_scheme_names'] = analysis_scheme_names
            if deployed is not ShapeBase.NOT_SET:
                _params['deployed'] = deployed
            _request = shapes.DescribeAnalysisSchemesRequest(**_params)
        response = self._boto_client.describe_analysis_schemes(
            **_request.to_boto()
        )

        return shapes.DescribeAnalysisSchemesResponse.from_boto(response)

    def describe_availability_options(
        self,
        _request: shapes.DescribeAvailabilityOptionsRequest = None,
        *,
        domain_name: str,
        deployed: bool = ShapeBase.NOT_SET,
    ) -> shapes.DescribeAvailabilityOptionsResponse:
        """
        Gets the availability options configured for a domain. By default, shows the
        configuration with any pending changes. Set the `Deployed` option to `true` to
        show the active configuration and exclude pending changes. For more information,
        see [Configuring Availability
        Options](http://docs.aws.amazon.com/cloudsearch/latest/developerguide/configuring-
        availability-options.html) in the _Amazon CloudSearch Developer Guide_.
        """
        if _request is None:
            _params = {}
            if domain_name is not ShapeBase.NOT_SET:
                _params['domain_name'] = domain_name
            if deployed is not ShapeBase.NOT_SET:
                _params['deployed'] = deployed
            _request = shapes.DescribeAvailabilityOptionsRequest(**_params)
        response = self._boto_client.describe_availability_options(
            **_request.to_boto()
        )

        return shapes.DescribeAvailabilityOptionsResponse.from_boto(response)

    def describe_domains(
        self,
        _request: shapes.DescribeDomainsRequest = None,
        *,
        domain_names: typing.List[str] = ShapeBase.NOT_SET,
    ) -> shapes.DescribeDomainsResponse:
        """
        Gets information about the search domains owned by this account. Can be limited
        to specific domains. Shows all domains by default. To get the number of
        searchable documents in a domain, use the console or submit a `matchall` request
        to your domain's search endpoint:
        `q=matchall&amp;q.parser=structured&amp;size=0`. For more information, see
        [Getting Information about a Search
        Domain](http://docs.aws.amazon.com/cloudsearch/latest/developerguide/getting-
        domain-info.html) in the _Amazon CloudSearch Developer Guide_.
        """
        if _request is None:
            _params = {}
            if domain_names is not ShapeBase.NOT_SET:
                _params['domain_names'] = domain_names
            _request = shapes.DescribeDomainsRequest(**_params)
        response = self._boto_client.describe_domains(**_request.to_boto())

        return shapes.DescribeDomainsResponse.from_boto(response)

    def describe_expressions(
        self,
        _request: shapes.DescribeExpressionsRequest = None,
        *,
        domain_name: str,
        expression_names: typing.List[str] = ShapeBase.NOT_SET,
        deployed: bool = ShapeBase.NOT_SET,
    ) -> shapes.DescribeExpressionsResponse:
        """
        Gets the expressions configured for the search domain. Can be limited to
        specific expressions by name. By default, shows all expressions and includes any
        pending changes to the configuration. Set the `Deployed` option to `true` to
        show the active configuration and exclude pending changes. For more information,
        see [Configuring
        Expressions](http://docs.aws.amazon.com/cloudsearch/latest/developerguide/configuring-
        expressions.html) in the _Amazon CloudSearch Developer Guide_.
        """
        if _request is None:
            _params = {}
            if domain_name is not ShapeBase.NOT_SET:
                _params['domain_name'] = domain_name
            if expression_names is not ShapeBase.NOT_SET:
                _params['expression_names'] = expression_names
            if deployed is not ShapeBase.NOT_SET:
                _params['deployed'] = deployed
            _request = shapes.DescribeExpressionsRequest(**_params)
        response = self._boto_client.describe_expressions(**_request.to_boto())

        return shapes.DescribeExpressionsResponse.from_boto(response)

    def describe_index_fields(
        self,
        _request: shapes.DescribeIndexFieldsRequest = None,
        *,
        domain_name: str,
        field_names: typing.List[str] = ShapeBase.NOT_SET,
        deployed: bool = ShapeBase.NOT_SET,
    ) -> shapes.DescribeIndexFieldsResponse:
        """
        Gets information about the index fields configured for the search domain. Can be
        limited to specific fields by name. By default, shows all fields and includes
        any pending changes to the configuration. Set the `Deployed` option to `true` to
        show the active configuration and exclude pending changes. For more information,
        see [Getting Domain
        Information](http://docs.aws.amazon.com/cloudsearch/latest/developerguide/getting-
        domain-info.html) in the _Amazon CloudSearch Developer Guide_.
        """
        if _request is None:
            _params = {}
            if domain_name is not ShapeBase.NOT_SET:
                _params['domain_name'] = domain_name
            if field_names is not ShapeBase.NOT_SET:
                _params['field_names'] = field_names
            if deployed is not ShapeBase.NOT_SET:
                _params['deployed'] = deployed
            _request = shapes.DescribeIndexFieldsRequest(**_params)
        response = self._boto_client.describe_index_fields(**_request.to_boto())

        return shapes.DescribeIndexFieldsResponse.from_boto(response)

    def describe_scaling_parameters(
        self,
        _request: shapes.DescribeScalingParametersRequest = None,
        *,
        domain_name: str,
    ) -> shapes.DescribeScalingParametersResponse:
        """
        Gets the scaling parameters configured for a domain. A domain's scaling
        parameters specify the desired search instance type and replication count. For
        more information, see [Configuring Scaling
        Options](http://docs.aws.amazon.com/cloudsearch/latest/developerguide/configuring-
        scaling-options.html) in the _Amazon CloudSearch Developer Guide_.
        """
        if _request is None:
            _params = {}
            if domain_name is not ShapeBase.NOT_SET:
                _params['domain_name'] = domain_name
            _request = shapes.DescribeScalingParametersRequest(**_params)
        response = self._boto_client.describe_scaling_parameters(
            **_request.to_boto()
        )

        return shapes.DescribeScalingParametersResponse.from_boto(response)

    def describe_service_access_policies(
        self,
        _request: shapes.DescribeServiceAccessPoliciesRequest = None,
        *,
        domain_name: str,
        deployed: bool = ShapeBase.NOT_SET,
    ) -> shapes.DescribeServiceAccessPoliciesResponse:
        """
        Gets information about the access policies that control access to the domain's
        document and search endpoints. By default, shows the configuration with any
        pending changes. Set the `Deployed` option to `true` to show the active
        configuration and exclude pending changes. For more information, see
        [Configuring Access for a Search
        Domain](http://docs.aws.amazon.com/cloudsearch/latest/developerguide/configuring-
        access.html) in the _Amazon CloudSearch Developer Guide_.
        """
        if _request is None:
            _params = {}
            if domain_name is not ShapeBase.NOT_SET:
                _params['domain_name'] = domain_name
            if deployed is not ShapeBase.NOT_SET:
                _params['deployed'] = deployed
            _request = shapes.DescribeServiceAccessPoliciesRequest(**_params)
        response = self._boto_client.describe_service_access_policies(
            **_request.to_boto()
        )

        return shapes.DescribeServiceAccessPoliciesResponse.from_boto(response)

    def describe_suggesters(
        self,
        _request: shapes.DescribeSuggestersRequest = None,
        *,
        domain_name: str,
        suggester_names: typing.List[str] = ShapeBase.NOT_SET,
        deployed: bool = ShapeBase.NOT_SET,
    ) -> shapes.DescribeSuggestersResponse:
        """
        Gets the suggesters configured for a domain. A suggester enables you to display
        possible matches before users finish typing their queries. Can be limited to
        specific suggesters by name. By default, shows all suggesters and includes any
        pending changes to the configuration. Set the `Deployed` option to `true` to
        show the active configuration and exclude pending changes. For more information,
        see [Getting Search
        Suggestions](http://docs.aws.amazon.com/cloudsearch/latest/developerguide/getting-
        suggestions.html) in the _Amazon CloudSearch Developer Guide_.
        """
        if _request is None:
            _params = {}
            if domain_name is not ShapeBase.NOT_SET:
                _params['domain_name'] = domain_name
            if suggester_names is not ShapeBase.NOT_SET:
                _params['suggester_names'] = suggester_names
            if deployed is not ShapeBase.NOT_SET:
                _params['deployed'] = deployed
            _request = shapes.DescribeSuggestersRequest(**_params)
        response = self._boto_client.describe_suggesters(**_request.to_boto())

        return shapes.DescribeSuggestersResponse.from_boto(response)

    def index_documents(
        self,
        _request: shapes.IndexDocumentsRequest = None,
        *,
        domain_name: str,
    ) -> shapes.IndexDocumentsResponse:
        """
        Tells the search domain to start indexing its documents using the latest
        indexing options. This operation must be invoked to activate options whose
        OptionStatus is `RequiresIndexDocuments`.
        """
        if _request is None:
            _params = {}
            if domain_name is not ShapeBase.NOT_SET:
                _params['domain_name'] = domain_name
            _request = shapes.IndexDocumentsRequest(**_params)
        response = self._boto_client.index_documents(**_request.to_boto())

        return shapes.IndexDocumentsResponse.from_boto(response)

    def list_domain_names(self) -> shapes.ListDomainNamesResponse:
        """
        Lists all search domains owned by an account.
        """
        response = self._boto_client.list_domain_names()

        return shapes.ListDomainNamesResponse.from_boto(response)

    def update_availability_options(
        self,
        _request: shapes.UpdateAvailabilityOptionsRequest = None,
        *,
        domain_name: str,
        multi_az: bool,
    ) -> shapes.UpdateAvailabilityOptionsResponse:
        """
        Configures the availability options for a domain. Enabling the Multi-AZ option
        expands an Amazon CloudSearch domain to an additional Availability Zone in the
        same Region to increase fault tolerance in the event of a service disruption.
        Changes to the Multi-AZ option can take about half an hour to become active. For
        more information, see [Configuring Availability
        Options](http://docs.aws.amazon.com/cloudsearch/latest/developerguide/configuring-
        availability-options.html) in the _Amazon CloudSearch Developer Guide_.
        """
        if _request is None:
            _params = {}
            if domain_name is not ShapeBase.NOT_SET:
                _params['domain_name'] = domain_name
            if multi_az is not ShapeBase.NOT_SET:
                _params['multi_az'] = multi_az
            _request = shapes.UpdateAvailabilityOptionsRequest(**_params)
        response = self._boto_client.update_availability_options(
            **_request.to_boto()
        )

        return shapes.UpdateAvailabilityOptionsResponse.from_boto(response)

    def update_scaling_parameters(
        self,
        _request: shapes.UpdateScalingParametersRequest = None,
        *,
        domain_name: str,
        scaling_parameters: shapes.ScalingParameters,
    ) -> shapes.UpdateScalingParametersResponse:
        """
        Configures scaling parameters for a domain. A domain's scaling parameters
        specify the desired search instance type and replication count. Amazon
        CloudSearch will still automatically scale your domain based on the volume of
        data and traffic, but not below the desired instance type and replication count.
        If the Multi-AZ option is enabled, these values control the resources used per
        Availability Zone. For more information, see [Configuring Scaling
        Options](http://docs.aws.amazon.com/cloudsearch/latest/developerguide/configuring-
        scaling-options.html) in the _Amazon CloudSearch Developer Guide_.
        """
        if _request is None:
            _params = {}
            if domain_name is not ShapeBase.NOT_SET:
                _params['domain_name'] = domain_name
            if scaling_parameters is not ShapeBase.NOT_SET:
                _params['scaling_parameters'] = scaling_parameters
            _request = shapes.UpdateScalingParametersRequest(**_params)
        response = self._boto_client.update_scaling_parameters(
            **_request.to_boto()
        )

        return shapes.UpdateScalingParametersResponse.from_boto(response)

    def update_service_access_policies(
        self,
        _request: shapes.UpdateServiceAccessPoliciesRequest = None,
        *,
        domain_name: str,
        access_policies: str,
    ) -> shapes.UpdateServiceAccessPoliciesResponse:
        """
        Configures the access rules that control access to the domain's document and
        search endpoints. For more information, see [ Configuring Access for an Amazon
        CloudSearch
        Domain](http://docs.aws.amazon.com/cloudsearch/latest/developerguide/configuring-
        access.html).
        """
        if _request is None:
            _params = {}
            if domain_name is not ShapeBase.NOT_SET:
                _params['domain_name'] = domain_name
            if access_policies is not ShapeBase.NOT_SET:
                _params['access_policies'] = access_policies
            _request = shapes.UpdateServiceAccessPoliciesRequest(**_params)
        response = self._boto_client.update_service_access_policies(
            **_request.to_boto()
        )

        return shapes.UpdateServiceAccessPoliciesResponse.from_boto(response)
