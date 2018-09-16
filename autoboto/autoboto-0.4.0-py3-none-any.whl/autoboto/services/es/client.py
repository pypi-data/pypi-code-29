import datetime
import typing
import boto3
from autoboto import ClientBase, ShapeBase, OutputShapeBase
from . import shapes


class Client(ClientBase):
    def __init__(self, *args, **kwargs):
        super().__init__("es", *args, **kwargs)

    def add_tags(
        self,
        _request: shapes.AddTagsRequest = None,
        *,
        arn: str,
        tag_list: typing.List[shapes.Tag],
    ) -> None:
        """
        Attaches tags to an existing Elasticsearch domain. Tags are a set of case-
        sensitive key value pairs. An Elasticsearch domain may have up to 10 tags. See [
        Tagging Amazon Elasticsearch Service Domains for more
        information.](http://docs.aws.amazon.com/elasticsearch-
        service/latest/developerguide/es-managedomains.html#es-managedomains-
        awsresorcetagging)
        """
        if _request is None:
            _params = {}
            if arn is not ShapeBase.NOT_SET:
                _params['arn'] = arn
            if tag_list is not ShapeBase.NOT_SET:
                _params['tag_list'] = tag_list
            _request = shapes.AddTagsRequest(**_params)
        response = self._boto_client.add_tags(**_request.to_boto())

    def create_elasticsearch_domain(
        self,
        _request: shapes.CreateElasticsearchDomainRequest = None,
        *,
        domain_name: str,
        elasticsearch_version: str = ShapeBase.NOT_SET,
        elasticsearch_cluster_config: shapes.
        ElasticsearchClusterConfig = ShapeBase.NOT_SET,
        ebs_options: shapes.EBSOptions = ShapeBase.NOT_SET,
        access_policies: str = ShapeBase.NOT_SET,
        snapshot_options: shapes.SnapshotOptions = ShapeBase.NOT_SET,
        vpc_options: shapes.VPCOptions = ShapeBase.NOT_SET,
        cognito_options: shapes.CognitoOptions = ShapeBase.NOT_SET,
        encryption_at_rest_options: shapes.EncryptionAtRestOptions = ShapeBase.
        NOT_SET,
        advanced_options: typing.Dict[str, str] = ShapeBase.NOT_SET,
        log_publishing_options: typing.
        Dict[typing.Union[str, shapes.LogType], shapes.
             LogPublishingOption] = ShapeBase.NOT_SET,
    ) -> shapes.CreateElasticsearchDomainResponse:
        """
        Creates a new Elasticsearch domain. For more information, see [Creating
        Elasticsearch Domains](http://docs.aws.amazon.com/elasticsearch-
        service/latest/developerguide/es-createupdatedomains.html#es-createdomains) in
        the _Amazon Elasticsearch Service Developer Guide_.
        """
        if _request is None:
            _params = {}
            if domain_name is not ShapeBase.NOT_SET:
                _params['domain_name'] = domain_name
            if elasticsearch_version is not ShapeBase.NOT_SET:
                _params['elasticsearch_version'] = elasticsearch_version
            if elasticsearch_cluster_config is not ShapeBase.NOT_SET:
                _params['elasticsearch_cluster_config'
                       ] = elasticsearch_cluster_config
            if ebs_options is not ShapeBase.NOT_SET:
                _params['ebs_options'] = ebs_options
            if access_policies is not ShapeBase.NOT_SET:
                _params['access_policies'] = access_policies
            if snapshot_options is not ShapeBase.NOT_SET:
                _params['snapshot_options'] = snapshot_options
            if vpc_options is not ShapeBase.NOT_SET:
                _params['vpc_options'] = vpc_options
            if cognito_options is not ShapeBase.NOT_SET:
                _params['cognito_options'] = cognito_options
            if encryption_at_rest_options is not ShapeBase.NOT_SET:
                _params['encryption_at_rest_options'
                       ] = encryption_at_rest_options
            if advanced_options is not ShapeBase.NOT_SET:
                _params['advanced_options'] = advanced_options
            if log_publishing_options is not ShapeBase.NOT_SET:
                _params['log_publishing_options'] = log_publishing_options
            _request = shapes.CreateElasticsearchDomainRequest(**_params)
        response = self._boto_client.create_elasticsearch_domain(
            **_request.to_boto()
        )

        return shapes.CreateElasticsearchDomainResponse.from_boto(response)

    def delete_elasticsearch_domain(
        self,
        _request: shapes.DeleteElasticsearchDomainRequest = None,
        *,
        domain_name: str,
    ) -> shapes.DeleteElasticsearchDomainResponse:
        """
        Permanently deletes the specified Elasticsearch domain and all of its data. Once
        a domain is deleted, it cannot be recovered.
        """
        if _request is None:
            _params = {}
            if domain_name is not ShapeBase.NOT_SET:
                _params['domain_name'] = domain_name
            _request = shapes.DeleteElasticsearchDomainRequest(**_params)
        response = self._boto_client.delete_elasticsearch_domain(
            **_request.to_boto()
        )

        return shapes.DeleteElasticsearchDomainResponse.from_boto(response)

    def delete_elasticsearch_service_role(self) -> None:
        """
        Deletes the service-linked role that Elasticsearch Service uses to manage and
        maintain VPC domains. Role deletion will fail if any existing VPC domains use
        the role. You must delete any such Elasticsearch domains before deleting the
        role. See [Deleting Elasticsearch Service
        Role](http://docs.aws.amazon.com/elasticsearch-service/latest/developerguide/es-
        vpc.html#es-enabling-slr) in _VPC Endpoints for Amazon Elasticsearch Service
        Domains_.
        """
        response = self._boto_client.delete_elasticsearch_service_role()

    def describe_elasticsearch_domain(
        self,
        _request: shapes.DescribeElasticsearchDomainRequest = None,
        *,
        domain_name: str,
    ) -> shapes.DescribeElasticsearchDomainResponse:
        """
        Returns domain configuration information about the specified Elasticsearch
        domain, including the domain ID, domain endpoint, and domain ARN.
        """
        if _request is None:
            _params = {}
            if domain_name is not ShapeBase.NOT_SET:
                _params['domain_name'] = domain_name
            _request = shapes.DescribeElasticsearchDomainRequest(**_params)
        response = self._boto_client.describe_elasticsearch_domain(
            **_request.to_boto()
        )

        return shapes.DescribeElasticsearchDomainResponse.from_boto(response)

    def describe_elasticsearch_domain_config(
        self,
        _request: shapes.DescribeElasticsearchDomainConfigRequest = None,
        *,
        domain_name: str,
    ) -> shapes.DescribeElasticsearchDomainConfigResponse:
        """
        Provides cluster configuration information about the specified Elasticsearch
        domain, such as the state, creation date, update version, and update date for
        cluster options.
        """
        if _request is None:
            _params = {}
            if domain_name is not ShapeBase.NOT_SET:
                _params['domain_name'] = domain_name
            _request = shapes.DescribeElasticsearchDomainConfigRequest(
                **_params
            )
        response = self._boto_client.describe_elasticsearch_domain_config(
            **_request.to_boto()
        )

        return shapes.DescribeElasticsearchDomainConfigResponse.from_boto(
            response
        )

    def describe_elasticsearch_domains(
        self,
        _request: shapes.DescribeElasticsearchDomainsRequest = None,
        *,
        domain_names: typing.List[str],
    ) -> shapes.DescribeElasticsearchDomainsResponse:
        """
        Returns domain configuration information about the specified Elasticsearch
        domains, including the domain ID, domain endpoint, and domain ARN.
        """
        if _request is None:
            _params = {}
            if domain_names is not ShapeBase.NOT_SET:
                _params['domain_names'] = domain_names
            _request = shapes.DescribeElasticsearchDomainsRequest(**_params)
        response = self._boto_client.describe_elasticsearch_domains(
            **_request.to_boto()
        )

        return shapes.DescribeElasticsearchDomainsResponse.from_boto(response)

    def describe_elasticsearch_instance_type_limits(
        self,
        _request: shapes.DescribeElasticsearchInstanceTypeLimitsRequest = None,
        *,
        instance_type: typing.Union[str, shapes.ESPartitionInstanceType],
        elasticsearch_version: str,
        domain_name: str = ShapeBase.NOT_SET,
    ) -> shapes.DescribeElasticsearchInstanceTypeLimitsResponse:
        """
        Describe Elasticsearch Limits for a given InstanceType and ElasticsearchVersion.
        When modifying existing Domain, specify the ` DomainName ` to know what Limits
        are supported for modifying.
        """
        if _request is None:
            _params = {}
            if instance_type is not ShapeBase.NOT_SET:
                _params['instance_type'] = instance_type
            if elasticsearch_version is not ShapeBase.NOT_SET:
                _params['elasticsearch_version'] = elasticsearch_version
            if domain_name is not ShapeBase.NOT_SET:
                _params['domain_name'] = domain_name
            _request = shapes.DescribeElasticsearchInstanceTypeLimitsRequest(
                **_params
            )
        response = self._boto_client.describe_elasticsearch_instance_type_limits(
            **_request.to_boto()
        )

        return shapes.DescribeElasticsearchInstanceTypeLimitsResponse.from_boto(
            response
        )

    def describe_reserved_elasticsearch_instance_offerings(
        self,
        _request: shapes.
        DescribeReservedElasticsearchInstanceOfferingsRequest = None,
        *,
        reserved_elasticsearch_instance_offering_id: str = ShapeBase.NOT_SET,
        max_results: int = ShapeBase.NOT_SET,
        next_token: str = ShapeBase.NOT_SET,
    ) -> shapes.DescribeReservedElasticsearchInstanceOfferingsResponse:
        """
        Lists available reserved Elasticsearch instance offerings.
        """
        if _request is None:
            _params = {}
            if reserved_elasticsearch_instance_offering_id is not ShapeBase.NOT_SET:
                _params['reserved_elasticsearch_instance_offering_id'
                       ] = reserved_elasticsearch_instance_offering_id
            if max_results is not ShapeBase.NOT_SET:
                _params['max_results'] = max_results
            if next_token is not ShapeBase.NOT_SET:
                _params['next_token'] = next_token
            _request = shapes.DescribeReservedElasticsearchInstanceOfferingsRequest(
                **_params
            )
        response = self._boto_client.describe_reserved_elasticsearch_instance_offerings(
            **_request.to_boto()
        )

        return shapes.DescribeReservedElasticsearchInstanceOfferingsResponse.from_boto(
            response
        )

    def describe_reserved_elasticsearch_instances(
        self,
        _request: shapes.DescribeReservedElasticsearchInstancesRequest = None,
        *,
        reserved_elasticsearch_instance_id: str = ShapeBase.NOT_SET,
        max_results: int = ShapeBase.NOT_SET,
        next_token: str = ShapeBase.NOT_SET,
    ) -> shapes.DescribeReservedElasticsearchInstancesResponse:
        """
        Returns information about reserved Elasticsearch instances for this account.
        """
        if _request is None:
            _params = {}
            if reserved_elasticsearch_instance_id is not ShapeBase.NOT_SET:
                _params['reserved_elasticsearch_instance_id'
                       ] = reserved_elasticsearch_instance_id
            if max_results is not ShapeBase.NOT_SET:
                _params['max_results'] = max_results
            if next_token is not ShapeBase.NOT_SET:
                _params['next_token'] = next_token
            _request = shapes.DescribeReservedElasticsearchInstancesRequest(
                **_params
            )
        response = self._boto_client.describe_reserved_elasticsearch_instances(
            **_request.to_boto()
        )

        return shapes.DescribeReservedElasticsearchInstancesResponse.from_boto(
            response
        )

    def get_compatible_elasticsearch_versions(
        self,
        _request: shapes.GetCompatibleElasticsearchVersionsRequest = None,
        *,
        domain_name: str = ShapeBase.NOT_SET,
    ) -> shapes.GetCompatibleElasticsearchVersionsResponse:
        """
        Returns a list of upgrade compatible Elastisearch versions. You can optionally
        pass a ` DomainName ` to get all upgrade compatible Elasticsearch versions for
        that specific domain.
        """
        if _request is None:
            _params = {}
            if domain_name is not ShapeBase.NOT_SET:
                _params['domain_name'] = domain_name
            _request = shapes.GetCompatibleElasticsearchVersionsRequest(
                **_params
            )
        response = self._boto_client.get_compatible_elasticsearch_versions(
            **_request.to_boto()
        )

        return shapes.GetCompatibleElasticsearchVersionsResponse.from_boto(
            response
        )

    def get_upgrade_history(
        self,
        _request: shapes.GetUpgradeHistoryRequest = None,
        *,
        domain_name: str,
        max_results: int = ShapeBase.NOT_SET,
        next_token: str = ShapeBase.NOT_SET,
    ) -> shapes.GetUpgradeHistoryResponse:
        """
        Retrieves the complete history of the last 10 upgrades that were performed on
        the domain.
        """
        if _request is None:
            _params = {}
            if domain_name is not ShapeBase.NOT_SET:
                _params['domain_name'] = domain_name
            if max_results is not ShapeBase.NOT_SET:
                _params['max_results'] = max_results
            if next_token is not ShapeBase.NOT_SET:
                _params['next_token'] = next_token
            _request = shapes.GetUpgradeHistoryRequest(**_params)
        response = self._boto_client.get_upgrade_history(**_request.to_boto())

        return shapes.GetUpgradeHistoryResponse.from_boto(response)

    def get_upgrade_status(
        self,
        _request: shapes.GetUpgradeStatusRequest = None,
        *,
        domain_name: str,
    ) -> shapes.GetUpgradeStatusResponse:
        """
        Retrieves the latest status of the last upgrade or upgrade eligibility check
        that was performed on the domain.
        """
        if _request is None:
            _params = {}
            if domain_name is not ShapeBase.NOT_SET:
                _params['domain_name'] = domain_name
            _request = shapes.GetUpgradeStatusRequest(**_params)
        response = self._boto_client.get_upgrade_status(**_request.to_boto())

        return shapes.GetUpgradeStatusResponse.from_boto(response)

    def list_domain_names(self) -> shapes.ListDomainNamesResponse:
        """
        Returns the name of all Elasticsearch domains owned by the current user's
        account.
        """
        response = self._boto_client.list_domain_names()

        return shapes.ListDomainNamesResponse.from_boto(response)

    def list_elasticsearch_instance_types(
        self,
        _request: shapes.ListElasticsearchInstanceTypesRequest = None,
        *,
        elasticsearch_version: str,
        domain_name: str = ShapeBase.NOT_SET,
        max_results: int = ShapeBase.NOT_SET,
        next_token: str = ShapeBase.NOT_SET,
    ) -> shapes.ListElasticsearchInstanceTypesResponse:
        """
        List all Elasticsearch instance types that are supported for given
        ElasticsearchVersion
        """
        if _request is None:
            _params = {}
            if elasticsearch_version is not ShapeBase.NOT_SET:
                _params['elasticsearch_version'] = elasticsearch_version
            if domain_name is not ShapeBase.NOT_SET:
                _params['domain_name'] = domain_name
            if max_results is not ShapeBase.NOT_SET:
                _params['max_results'] = max_results
            if next_token is not ShapeBase.NOT_SET:
                _params['next_token'] = next_token
            _request = shapes.ListElasticsearchInstanceTypesRequest(**_params)
        paginator = self.get_paginator("list_elasticsearch_instance_types"
                                      ).paginate(**_request.to_boto())
        page_generator = (page for page in paginator)
        first_page = next(page_generator)
        result = shapes.ListElasticsearchInstanceTypesResponse.from_boto(
            first_page
        )
        result._page_iterator = page_generator
        return result

        return shapes.ListElasticsearchInstanceTypesResponse.from_boto(response)

    def list_elasticsearch_versions(
        self,
        _request: shapes.ListElasticsearchVersionsRequest = None,
        *,
        max_results: int = ShapeBase.NOT_SET,
        next_token: str = ShapeBase.NOT_SET,
    ) -> shapes.ListElasticsearchVersionsResponse:
        """
        List all supported Elasticsearch versions
        """
        if _request is None:
            _params = {}
            if max_results is not ShapeBase.NOT_SET:
                _params['max_results'] = max_results
            if next_token is not ShapeBase.NOT_SET:
                _params['next_token'] = next_token
            _request = shapes.ListElasticsearchVersionsRequest(**_params)
        paginator = self.get_paginator("list_elasticsearch_versions").paginate(
            **_request.to_boto()
        )
        page_generator = (page for page in paginator)
        first_page = next(page_generator)
        result = shapes.ListElasticsearchVersionsResponse.from_boto(first_page)
        result._page_iterator = page_generator
        return result

        return shapes.ListElasticsearchVersionsResponse.from_boto(response)

    def list_tags(
        self,
        _request: shapes.ListTagsRequest = None,
        *,
        arn: str,
    ) -> shapes.ListTagsResponse:
        """
        Returns all tags for the given Elasticsearch domain.
        """
        if _request is None:
            _params = {}
            if arn is not ShapeBase.NOT_SET:
                _params['arn'] = arn
            _request = shapes.ListTagsRequest(**_params)
        response = self._boto_client.list_tags(**_request.to_boto())

        return shapes.ListTagsResponse.from_boto(response)

    def purchase_reserved_elasticsearch_instance_offering(
        self,
        _request: shapes.
        PurchaseReservedElasticsearchInstanceOfferingRequest = None,
        *,
        reserved_elasticsearch_instance_offering_id: str,
        reservation_name: str,
        instance_count: int = ShapeBase.NOT_SET,
    ) -> shapes.PurchaseReservedElasticsearchInstanceOfferingResponse:
        """
        Allows you to purchase reserved Elasticsearch instances.
        """
        if _request is None:
            _params = {}
            if reserved_elasticsearch_instance_offering_id is not ShapeBase.NOT_SET:
                _params['reserved_elasticsearch_instance_offering_id'
                       ] = reserved_elasticsearch_instance_offering_id
            if reservation_name is not ShapeBase.NOT_SET:
                _params['reservation_name'] = reservation_name
            if instance_count is not ShapeBase.NOT_SET:
                _params['instance_count'] = instance_count
            _request = shapes.PurchaseReservedElasticsearchInstanceOfferingRequest(
                **_params
            )
        response = self._boto_client.purchase_reserved_elasticsearch_instance_offering(
            **_request.to_boto()
        )

        return shapes.PurchaseReservedElasticsearchInstanceOfferingResponse.from_boto(
            response
        )

    def remove_tags(
        self,
        _request: shapes.RemoveTagsRequest = None,
        *,
        arn: str,
        tag_keys: typing.List[str],
    ) -> None:
        """
        Removes the specified set of tags from the specified Elasticsearch domain.
        """
        if _request is None:
            _params = {}
            if arn is not ShapeBase.NOT_SET:
                _params['arn'] = arn
            if tag_keys is not ShapeBase.NOT_SET:
                _params['tag_keys'] = tag_keys
            _request = shapes.RemoveTagsRequest(**_params)
        response = self._boto_client.remove_tags(**_request.to_boto())

    def update_elasticsearch_domain_config(
        self,
        _request: shapes.UpdateElasticsearchDomainConfigRequest = None,
        *,
        domain_name: str,
        elasticsearch_cluster_config: shapes.
        ElasticsearchClusterConfig = ShapeBase.NOT_SET,
        ebs_options: shapes.EBSOptions = ShapeBase.NOT_SET,
        snapshot_options: shapes.SnapshotOptions = ShapeBase.NOT_SET,
        vpc_options: shapes.VPCOptions = ShapeBase.NOT_SET,
        cognito_options: shapes.CognitoOptions = ShapeBase.NOT_SET,
        advanced_options: typing.Dict[str, str] = ShapeBase.NOT_SET,
        access_policies: str = ShapeBase.NOT_SET,
        log_publishing_options: typing.
        Dict[typing.Union[str, shapes.LogType], shapes.
             LogPublishingOption] = ShapeBase.NOT_SET,
    ) -> shapes.UpdateElasticsearchDomainConfigResponse:
        """
        Modifies the cluster configuration of the specified Elasticsearch domain,
        setting as setting the instance type and the number of instances.
        """
        if _request is None:
            _params = {}
            if domain_name is not ShapeBase.NOT_SET:
                _params['domain_name'] = domain_name
            if elasticsearch_cluster_config is not ShapeBase.NOT_SET:
                _params['elasticsearch_cluster_config'
                       ] = elasticsearch_cluster_config
            if ebs_options is not ShapeBase.NOT_SET:
                _params['ebs_options'] = ebs_options
            if snapshot_options is not ShapeBase.NOT_SET:
                _params['snapshot_options'] = snapshot_options
            if vpc_options is not ShapeBase.NOT_SET:
                _params['vpc_options'] = vpc_options
            if cognito_options is not ShapeBase.NOT_SET:
                _params['cognito_options'] = cognito_options
            if advanced_options is not ShapeBase.NOT_SET:
                _params['advanced_options'] = advanced_options
            if access_policies is not ShapeBase.NOT_SET:
                _params['access_policies'] = access_policies
            if log_publishing_options is not ShapeBase.NOT_SET:
                _params['log_publishing_options'] = log_publishing_options
            _request = shapes.UpdateElasticsearchDomainConfigRequest(**_params)
        response = self._boto_client.update_elasticsearch_domain_config(
            **_request.to_boto()
        )

        return shapes.UpdateElasticsearchDomainConfigResponse.from_boto(
            response
        )

    def upgrade_elasticsearch_domain(
        self,
        _request: shapes.UpgradeElasticsearchDomainRequest = None,
        *,
        domain_name: str,
        target_version: str,
        perform_check_only: bool = ShapeBase.NOT_SET,
    ) -> shapes.UpgradeElasticsearchDomainResponse:
        """
        Allows you to either upgrade your domain or perform an Upgrade eligibility check
        to a compatible Elasticsearch version.
        """
        if _request is None:
            _params = {}
            if domain_name is not ShapeBase.NOT_SET:
                _params['domain_name'] = domain_name
            if target_version is not ShapeBase.NOT_SET:
                _params['target_version'] = target_version
            if perform_check_only is not ShapeBase.NOT_SET:
                _params['perform_check_only'] = perform_check_only
            _request = shapes.UpgradeElasticsearchDomainRequest(**_params)
        response = self._boto_client.upgrade_elasticsearch_domain(
            **_request.to_boto()
        )

        return shapes.UpgradeElasticsearchDomainResponse.from_boto(response)
