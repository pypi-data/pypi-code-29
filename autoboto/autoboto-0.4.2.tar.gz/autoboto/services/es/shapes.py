import datetime
import typing
from autoboto import ShapeBase, OutputShapeBase, TypeInfo
import dataclasses


@dataclasses.dataclass
class AccessPoliciesStatus(ShapeBase):
    """
    The configured access rules for the domain's document and search endpoints, and
    the current status of those rules.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "options",
                "Options",
                TypeInfo(str),
            ),
            (
                "status",
                "Status",
                TypeInfo(OptionStatus),
            ),
        ]

    # The access policy configured for the Elasticsearch domain. Access policies
    # may be resource-based, IP-based, or IAM-based. See [ Configuring Access
    # Policies](http://docs.aws.amazon.com/elasticsearch-
    # service/latest/developerguide/es-createupdatedomains.html#es-createdomain-
    # configure-access-policies)for more information.
    options: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The status of the access policy for the Elasticsearch domain. See
    # `OptionStatus` for the status information that's included.
    status: "OptionStatus" = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class AddTagsRequest(ShapeBase):
    """
    Container for the parameters to the `AddTags` operation. Specify the tags that
    you want to attach to the Elasticsearch domain.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "arn",
                "ARN",
                TypeInfo(str),
            ),
            (
                "tag_list",
                "TagList",
                TypeInfo(typing.List[Tag]),
            ),
        ]

    # Specify the `ARN` for which you want to add the tags.
    arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # List of `Tag` that need to be added for the Elasticsearch domain.
    tag_list: typing.List["Tag"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class AdditionalLimit(ShapeBase):
    """
    List of limits that are specific to a given InstanceType and for each of it's `
    InstanceRole ` .
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "limit_name",
                "LimitName",
                TypeInfo(str),
            ),
            (
                "limit_values",
                "LimitValues",
                TypeInfo(typing.List[str]),
            ),
        ]

    # Name of Additional Limit is specific to a given InstanceType and for each
    # of it's ` InstanceRole ` etc.
    # Attributes and their details:

    #   * MaximumNumberOfDataNodesSupported
    # This attribute will be present in Master node only to specify how much data
    # nodes upto which given ` ESPartitionInstanceType ` can support as master
    # node.

    #   * MaximumNumberOfDataNodesWithoutMasterNode
    # This attribute will be present in Data node only to specify how much data
    # nodes of given ` ESPartitionInstanceType ` upto which you don't need any
    # master nodes to govern them.
    limit_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Value for given ` AdditionalLimit$LimitName ` .
    limit_values: typing.List[str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class AdvancedOptionsStatus(ShapeBase):
    """
    Status of the advanced options for the specified Elasticsearch domain.
    Currently, the following advanced options are available:

      * Option to allow references to indices in an HTTP request body. Must be `false` when configuring access to individual sub-resources. By default, the value is `true`. See [Configuration Advanced Options](http://docs.aws.amazon.com/elasticsearch-service/latest/developerguide/es-createupdatedomains.html#es-createdomain-configure-advanced-options) for more information.
      * Option to specify the percentage of heap space that is allocated to field data. By default, this setting is unbounded.

    For more information, see [Configuring Advanced
    Options](http://docs.aws.amazon.com/elasticsearch-
    service/latest/developerguide/es-createupdatedomains.html#es-createdomain-
    configure-advanced-options).
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "options",
                "Options",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "status",
                "Status",
                TypeInfo(OptionStatus),
            ),
        ]

    # Specifies the status of advanced options for the specified Elasticsearch
    # domain.
    options: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Specifies the status of `OptionStatus` for advanced options for the
    # specified Elasticsearch domain.
    status: "OptionStatus" = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class BaseException(ShapeBase):
    """
    An error occurred while processing the request.
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

    # A description of the error.
    message: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class CognitoOptions(ShapeBase):
    """
    Options to specify the Cognito user and identity pools for Kibana
    authentication. For more information, see [Amazon Cognito Authentication for
    Kibana](http://docs.aws.amazon.com/elasticsearch-
    service/latest/developerguide/es-cognito-auth.html).
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "enabled",
                "Enabled",
                TypeInfo(bool),
            ),
            (
                "user_pool_id",
                "UserPoolId",
                TypeInfo(str),
            ),
            (
                "identity_pool_id",
                "IdentityPoolId",
                TypeInfo(str),
            ),
            (
                "role_arn",
                "RoleArn",
                TypeInfo(str),
            ),
        ]

    # Specifies the option to enable Cognito for Kibana authentication.
    enabled: bool = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Specifies the Cognito user pool ID for Kibana authentication.
    user_pool_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Specifies the Cognito identity pool ID for Kibana authentication.
    identity_pool_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Specifies the role ARN that provides Elasticsearch permissions for
    # accessing Cognito resources.
    role_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class CognitoOptionsStatus(ShapeBase):
    """
    Status of the Cognito options for the specified Elasticsearch domain.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "options",
                "Options",
                TypeInfo(CognitoOptions),
            ),
            (
                "status",
                "Status",
                TypeInfo(OptionStatus),
            ),
        ]

    # Specifies the Cognito options for the specified Elasticsearch domain.
    options: "CognitoOptions" = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Specifies the status of the Cognito options for the specified Elasticsearch
    # domain.
    status: "OptionStatus" = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class CompatibleVersionsMap(ShapeBase):
    """
    A map from an ` ElasticsearchVersion ` to a list of compatible `
    ElasticsearchVersion ` s to which the domain can be upgraded.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "source_version",
                "SourceVersion",
                TypeInfo(str),
            ),
            (
                "target_versions",
                "TargetVersions",
                TypeInfo(typing.List[str]),
            ),
        ]

    # The current version of Elasticsearch on which a domain is.
    source_version: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # List of supported elastic search versions.
    target_versions: typing.List[str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class CreateElasticsearchDomainRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "domain_name",
                "DomainName",
                TypeInfo(str),
            ),
            (
                "elasticsearch_version",
                "ElasticsearchVersion",
                TypeInfo(str),
            ),
            (
                "elasticsearch_cluster_config",
                "ElasticsearchClusterConfig",
                TypeInfo(ElasticsearchClusterConfig),
            ),
            (
                "ebs_options",
                "EBSOptions",
                TypeInfo(EBSOptions),
            ),
            (
                "access_policies",
                "AccessPolicies",
                TypeInfo(str),
            ),
            (
                "snapshot_options",
                "SnapshotOptions",
                TypeInfo(SnapshotOptions),
            ),
            (
                "vpc_options",
                "VPCOptions",
                TypeInfo(VPCOptions),
            ),
            (
                "cognito_options",
                "CognitoOptions",
                TypeInfo(CognitoOptions),
            ),
            (
                "encryption_at_rest_options",
                "EncryptionAtRestOptions",
                TypeInfo(EncryptionAtRestOptions),
            ),
            (
                "advanced_options",
                "AdvancedOptions",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "log_publishing_options",
                "LogPublishingOptions",
                TypeInfo(
                    typing.Dict[typing.Union[str, LogType], LogPublishingOption]
                ),
            ),
        ]

    # The name of the Elasticsearch domain that you are creating. Domain names
    # are unique across the domains owned by an account within an AWS region.
    # Domain names must start with a letter or number and can contain the
    # following characters: a-z (lowercase), 0-9, and - (hyphen).
    domain_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # String of format X.Y to specify version for the Elasticsearch domain eg.
    # "1.5" or "2.3". For more information, see [Creating Elasticsearch
    # Domains](http://docs.aws.amazon.com/elasticsearch-
    # service/latest/developerguide/es-createupdatedomains.html#es-createdomains)
    # in the _Amazon Elasticsearch Service Developer Guide_.
    elasticsearch_version: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Configuration options for an Elasticsearch domain. Specifies the instance
    # type and number of instances in the domain cluster.
    elasticsearch_cluster_config: "ElasticsearchClusterConfig" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Options to enable, disable and specify the type and size of EBS storage
    # volumes.
    ebs_options: "EBSOptions" = dataclasses.field(default=ShapeBase.NOT_SET, )

    # IAM access policy as a JSON-formatted string.
    access_policies: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Option to set time, in UTC format, of the daily automated snapshot. Default
    # value is 0 hours.
    snapshot_options: "SnapshotOptions" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Options to specify the subnets and security groups for VPC endpoint. For
    # more information, see [Creating a
    # VPC](http://docs.aws.amazon.com/elasticsearch-
    # service/latest/developerguide/es-vpc.html#es-creating-vpc) in _VPC
    # Endpoints for Amazon Elasticsearch Service Domains_
    vpc_options: "VPCOptions" = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Options to specify the Cognito user and identity pools for Kibana
    # authentication. For more information, see [Amazon Cognito Authentication
    # for Kibana](http://docs.aws.amazon.com/elasticsearch-
    # service/latest/developerguide/es-cognito-auth.html).
    cognito_options: "CognitoOptions" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Specifies the Encryption At Rest Options.
    encryption_at_rest_options: "EncryptionAtRestOptions" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Option to allow references to indices in an HTTP request body. Must be
    # `false` when configuring access to individual sub-resources. By default,
    # the value is `true`. See [Configuration Advanced
    # Options](http://docs.aws.amazon.com/elasticsearch-
    # service/latest/developerguide/es-createupdatedomains.html#es-createdomain-
    # configure-advanced-options) for more information.
    advanced_options: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Map of `LogType` and `LogPublishingOption`, each containing options to
    # publish a given type of Elasticsearch log.
    log_publishing_options: typing.Dict[
        typing.
        Union[str, "LogType"], "LogPublishingOption"] = dataclasses.field(
            default=ShapeBase.NOT_SET,
        )


@dataclasses.dataclass
class CreateElasticsearchDomainResponse(OutputShapeBase):
    """
    The result of a `CreateElasticsearchDomain` operation. Contains the status of
    the newly created Elasticsearch domain.
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
                "domain_status",
                "DomainStatus",
                TypeInfo(ElasticsearchDomainStatus),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The status of the newly created Elasticsearch domain.
    domain_status: "ElasticsearchDomainStatus" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class DeleteElasticsearchDomainRequest(ShapeBase):
    """
    Container for the parameters to the `DeleteElasticsearchDomain` operation.
    Specifies the name of the Elasticsearch domain that you want to delete.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "domain_name",
                "DomainName",
                TypeInfo(str),
            ),
        ]

    # The name of the Elasticsearch domain that you want to permanently delete.
    domain_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DeleteElasticsearchDomainResponse(OutputShapeBase):
    """
    The result of a `DeleteElasticsearchDomain` request. Contains the status of the
    pending deletion, or no status if the domain and all of its resources have been
    deleted.
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
                "domain_status",
                "DomainStatus",
                TypeInfo(ElasticsearchDomainStatus),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The status of the Elasticsearch domain being deleted.
    domain_status: "ElasticsearchDomainStatus" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class DescribeElasticsearchDomainConfigRequest(ShapeBase):
    """
    Container for the parameters to the `DescribeElasticsearchDomainConfig`
    operation. Specifies the domain name for which you want configuration
    information.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "domain_name",
                "DomainName",
                TypeInfo(str),
            ),
        ]

    # The Elasticsearch domain that you want to get information about.
    domain_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DescribeElasticsearchDomainConfigResponse(OutputShapeBase):
    """
    The result of a `DescribeElasticsearchDomainConfig` request. Contains the
    configuration information of the requested domain.
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
                "domain_config",
                "DomainConfig",
                TypeInfo(ElasticsearchDomainConfig),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The configuration information of the domain requested in the
    # `DescribeElasticsearchDomainConfig` request.
    domain_config: "ElasticsearchDomainConfig" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class DescribeElasticsearchDomainRequest(ShapeBase):
    """
    Container for the parameters to the `DescribeElasticsearchDomain` operation.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "domain_name",
                "DomainName",
                TypeInfo(str),
            ),
        ]

    # The name of the Elasticsearch domain for which you want information.
    domain_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DescribeElasticsearchDomainResponse(OutputShapeBase):
    """
    The result of a `DescribeElasticsearchDomain` request. Contains the status of
    the domain specified in the request.
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
                "domain_status",
                "DomainStatus",
                TypeInfo(ElasticsearchDomainStatus),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The current status of the Elasticsearch domain.
    domain_status: "ElasticsearchDomainStatus" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class DescribeElasticsearchDomainsRequest(ShapeBase):
    """
    Container for the parameters to the `DescribeElasticsearchDomains` operation. By
    default, the API returns the status of all Elasticsearch domains.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "domain_names",
                "DomainNames",
                TypeInfo(typing.List[str]),
            ),
        ]

    # The Elasticsearch domains for which you want information.
    domain_names: typing.List[str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class DescribeElasticsearchDomainsResponse(OutputShapeBase):
    """
    The result of a `DescribeElasticsearchDomains` request. Contains the status of
    the specified domains or all domains owned by the account.
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
                "domain_status_list",
                "DomainStatusList",
                TypeInfo(typing.List[ElasticsearchDomainStatus]),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The status of the domains requested in the `DescribeElasticsearchDomains`
    # request.
    domain_status_list: typing.List["ElasticsearchDomainStatus"
                                   ] = dataclasses.field(
                                       default=ShapeBase.NOT_SET,
                                   )


@dataclasses.dataclass
class DescribeElasticsearchInstanceTypeLimitsRequest(ShapeBase):
    """
    Container for the parameters to ` DescribeElasticsearchInstanceTypeLimits `
    operation.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "instance_type",
                "InstanceType",
                TypeInfo(typing.Union[str, ESPartitionInstanceType]),
            ),
            (
                "elasticsearch_version",
                "ElasticsearchVersion",
                TypeInfo(str),
            ),
            (
                "domain_name",
                "DomainName",
                TypeInfo(str),
            ),
        ]

    # The instance type for an Elasticsearch cluster for which Elasticsearch `
    # Limits ` are needed.
    instance_type: typing.Union[str, "ESPartitionInstanceType"
                               ] = dataclasses.field(
                                   default=ShapeBase.NOT_SET,
                               )

    # Version of Elasticsearch for which ` Limits ` are needed.
    elasticsearch_version: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # DomainName represents the name of the Domain that we are trying to modify.
    # This should be present only if we are querying for Elasticsearch ` Limits `
    # for existing domain.
    domain_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DescribeElasticsearchInstanceTypeLimitsResponse(OutputShapeBase):
    """
    Container for the parameters received from `
    DescribeElasticsearchInstanceTypeLimits ` operation.
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
                "limits_by_role",
                "LimitsByRole",
                TypeInfo(typing.Dict[str, Limits]),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Map of Role of the Instance and Limits that are applicable. Role performed
    # by given Instance in Elasticsearch can be one of the following:

    #   * Data: If the given InstanceType is used as Data node
    #   * Master: If the given InstanceType is used as Master node
    limits_by_role: typing.Dict[str, "Limits"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class DescribeReservedElasticsearchInstanceOfferingsRequest(ShapeBase):
    """
    Container for parameters to `DescribeReservedElasticsearchInstanceOfferings`
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "reserved_elasticsearch_instance_offering_id",
                "ReservedElasticsearchInstanceOfferingId",
                TypeInfo(str),
            ),
            (
                "max_results",
                "MaxResults",
                TypeInfo(int),
            ),
            (
                "next_token",
                "NextToken",
                TypeInfo(str),
            ),
        ]

    # The offering identifier filter value. Use this parameter to show only the
    # available offering that matches the specified reservation identifier.
    reserved_elasticsearch_instance_offering_id: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Set this value to limit the number of results returned. If not specified,
    # defaults to 100.
    max_results: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # NextToken should be sent in case if earlier API call produced result
    # containing NextToken. It is used for pagination.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DescribeReservedElasticsearchInstanceOfferingsResponse(OutputShapeBase):
    """
    Container for results from `DescribeReservedElasticsearchInstanceOfferings`
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
                "next_token",
                "NextToken",
                TypeInfo(str),
            ),
            (
                "reserved_elasticsearch_instance_offerings",
                "ReservedElasticsearchInstanceOfferings",
                TypeInfo(typing.List[ReservedElasticsearchInstanceOffering]),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Provides an identifier to allow retrieval of paginated results.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # List of reserved Elasticsearch instance offerings
    reserved_elasticsearch_instance_offerings: typing.List[
        "ReservedElasticsearchInstanceOffering"] = dataclasses.field(
            default=ShapeBase.NOT_SET,
        )


@dataclasses.dataclass
class DescribeReservedElasticsearchInstancesRequest(ShapeBase):
    """
    Container for parameters to `DescribeReservedElasticsearchInstances`
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "reserved_elasticsearch_instance_id",
                "ReservedElasticsearchInstanceId",
                TypeInfo(str),
            ),
            (
                "max_results",
                "MaxResults",
                TypeInfo(int),
            ),
            (
                "next_token",
                "NextToken",
                TypeInfo(str),
            ),
        ]

    # The reserved instance identifier filter value. Use this parameter to show
    # only the reservation that matches the specified reserved Elasticsearch
    # instance ID.
    reserved_elasticsearch_instance_id: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Set this value to limit the number of results returned. If not specified,
    # defaults to 100.
    max_results: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # NextToken should be sent in case if earlier API call produced result
    # containing NextToken. It is used for pagination.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DescribeReservedElasticsearchInstancesResponse(OutputShapeBase):
    """
    Container for results from `DescribeReservedElasticsearchInstances`
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
                "next_token",
                "NextToken",
                TypeInfo(str),
            ),
            (
                "reserved_elasticsearch_instances",
                "ReservedElasticsearchInstances",
                TypeInfo(typing.List[ReservedElasticsearchInstance]),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Provides an identifier to allow retrieval of paginated results.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # List of reserved Elasticsearch instances.
    reserved_elasticsearch_instances: typing.List[
        "ReservedElasticsearchInstance"] = dataclasses.field(
            default=ShapeBase.NOT_SET,
        )


@dataclasses.dataclass
class DisabledOperationException(ShapeBase):
    """
    An error occured because the client wanted to access a not supported operation.
    Gives http status code of 409.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class DomainInfo(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "domain_name",
                "DomainName",
                TypeInfo(str),
            ),
        ]

    # Specifies the `DomainName`.
    domain_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class EBSOptions(ShapeBase):
    """
    Options to enable, disable, and specify the properties of EBS storage volumes.
    For more information, see [ Configuring EBS-based
    Storage](http://docs.aws.amazon.com/elasticsearch-
    service/latest/developerguide/es-createupdatedomains.html#es-createdomain-
    configure-ebs).
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "ebs_enabled",
                "EBSEnabled",
                TypeInfo(bool),
            ),
            (
                "volume_type",
                "VolumeType",
                TypeInfo(typing.Union[str, VolumeType]),
            ),
            (
                "volume_size",
                "VolumeSize",
                TypeInfo(int),
            ),
            (
                "iops",
                "Iops",
                TypeInfo(int),
            ),
        ]

    # Specifies whether EBS-based storage is enabled.
    ebs_enabled: bool = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Specifies the volume type for EBS-based storage.
    volume_type: typing.Union[str, "VolumeType"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Integer to specify the size of an EBS volume.
    volume_size: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Specifies the IOPD for a Provisioned IOPS EBS volume (SSD).
    iops: int = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class EBSOptionsStatus(ShapeBase):
    """
    Status of the EBS options for the specified Elasticsearch domain.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "options",
                "Options",
                TypeInfo(EBSOptions),
            ),
            (
                "status",
                "Status",
                TypeInfo(OptionStatus),
            ),
        ]

    # Specifies the EBS options for the specified Elasticsearch domain.
    options: "EBSOptions" = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Specifies the status of the EBS options for the specified Elasticsearch
    # domain.
    status: "OptionStatus" = dataclasses.field(default=ShapeBase.NOT_SET, )


class ESPartitionInstanceType(str):
    m3_medium_elasticsearch = "m3.medium.elasticsearch"
    m3_large_elasticsearch = "m3.large.elasticsearch"
    m3_xlarge_elasticsearch = "m3.xlarge.elasticsearch"
    m3_2xlarge_elasticsearch = "m3.2xlarge.elasticsearch"
    m4_large_elasticsearch = "m4.large.elasticsearch"
    m4_xlarge_elasticsearch = "m4.xlarge.elasticsearch"
    m4_2xlarge_elasticsearch = "m4.2xlarge.elasticsearch"
    m4_4xlarge_elasticsearch = "m4.4xlarge.elasticsearch"
    m4_10xlarge_elasticsearch = "m4.10xlarge.elasticsearch"
    t2_micro_elasticsearch = "t2.micro.elasticsearch"
    t2_small_elasticsearch = "t2.small.elasticsearch"
    t2_medium_elasticsearch = "t2.medium.elasticsearch"
    r3_large_elasticsearch = "r3.large.elasticsearch"
    r3_xlarge_elasticsearch = "r3.xlarge.elasticsearch"
    r3_2xlarge_elasticsearch = "r3.2xlarge.elasticsearch"
    r3_4xlarge_elasticsearch = "r3.4xlarge.elasticsearch"
    r3_8xlarge_elasticsearch = "r3.8xlarge.elasticsearch"
    i2_xlarge_elasticsearch = "i2.xlarge.elasticsearch"
    i2_2xlarge_elasticsearch = "i2.2xlarge.elasticsearch"
    d2_xlarge_elasticsearch = "d2.xlarge.elasticsearch"
    d2_2xlarge_elasticsearch = "d2.2xlarge.elasticsearch"
    d2_4xlarge_elasticsearch = "d2.4xlarge.elasticsearch"
    d2_8xlarge_elasticsearch = "d2.8xlarge.elasticsearch"
    c4_large_elasticsearch = "c4.large.elasticsearch"
    c4_xlarge_elasticsearch = "c4.xlarge.elasticsearch"
    c4_2xlarge_elasticsearch = "c4.2xlarge.elasticsearch"
    c4_4xlarge_elasticsearch = "c4.4xlarge.elasticsearch"
    c4_8xlarge_elasticsearch = "c4.8xlarge.elasticsearch"
    r4_large_elasticsearch = "r4.large.elasticsearch"
    r4_xlarge_elasticsearch = "r4.xlarge.elasticsearch"
    r4_2xlarge_elasticsearch = "r4.2xlarge.elasticsearch"
    r4_4xlarge_elasticsearch = "r4.4xlarge.elasticsearch"
    r4_8xlarge_elasticsearch = "r4.8xlarge.elasticsearch"
    r4_16xlarge_elasticsearch = "r4.16xlarge.elasticsearch"
    i3_large_elasticsearch = "i3.large.elasticsearch"
    i3_xlarge_elasticsearch = "i3.xlarge.elasticsearch"
    i3_2xlarge_elasticsearch = "i3.2xlarge.elasticsearch"
    i3_4xlarge_elasticsearch = "i3.4xlarge.elasticsearch"
    i3_8xlarge_elasticsearch = "i3.8xlarge.elasticsearch"
    i3_16xlarge_elasticsearch = "i3.16xlarge.elasticsearch"


@dataclasses.dataclass
class ElasticsearchClusterConfig(ShapeBase):
    """
    Specifies the configuration for the domain cluster, such as the type and number
    of instances.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "instance_type",
                "InstanceType",
                TypeInfo(typing.Union[str, ESPartitionInstanceType]),
            ),
            (
                "instance_count",
                "InstanceCount",
                TypeInfo(int),
            ),
            (
                "dedicated_master_enabled",
                "DedicatedMasterEnabled",
                TypeInfo(bool),
            ),
            (
                "zone_awareness_enabled",
                "ZoneAwarenessEnabled",
                TypeInfo(bool),
            ),
            (
                "dedicated_master_type",
                "DedicatedMasterType",
                TypeInfo(typing.Union[str, ESPartitionInstanceType]),
            ),
            (
                "dedicated_master_count",
                "DedicatedMasterCount",
                TypeInfo(int),
            ),
        ]

    # The instance type for an Elasticsearch cluster.
    instance_type: typing.Union[str, "ESPartitionInstanceType"
                               ] = dataclasses.field(
                                   default=ShapeBase.NOT_SET,
                               )

    # The number of instances in the specified domain cluster.
    instance_count: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A boolean value to indicate whether a dedicated master node is enabled. See
    # [About Dedicated Master Nodes](http://docs.aws.amazon.com/elasticsearch-
    # service/latest/developerguide/es-managedomains.html#es-managedomains-
    # dedicatedmasternodes) for more information.
    dedicated_master_enabled: bool = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A boolean value to indicate whether zone awareness is enabled. See [About
    # Zone Awareness](http://docs.aws.amazon.com/elasticsearch-
    # service/latest/developerguide/es-managedomains.html#es-managedomains-
    # zoneawareness) for more information.
    zone_awareness_enabled: bool = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The instance type for a dedicated master node.
    dedicated_master_type: typing.Union[str, "ESPartitionInstanceType"
                                       ] = dataclasses.field(
                                           default=ShapeBase.NOT_SET,
                                       )

    # Total number of dedicated master nodes, active and on standby, for the
    # cluster.
    dedicated_master_count: int = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ElasticsearchClusterConfigStatus(ShapeBase):
    """
    Specifies the configuration status for the specified Elasticsearch domain.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "options",
                "Options",
                TypeInfo(ElasticsearchClusterConfig),
            ),
            (
                "status",
                "Status",
                TypeInfo(OptionStatus),
            ),
        ]

    # Specifies the cluster configuration for the specified Elasticsearch domain.
    options: "ElasticsearchClusterConfig" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Specifies the status of the configuration for the specified Elasticsearch
    # domain.
    status: "OptionStatus" = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ElasticsearchDomainConfig(ShapeBase):
    """
    The configuration of an Elasticsearch domain.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "elasticsearch_version",
                "ElasticsearchVersion",
                TypeInfo(ElasticsearchVersionStatus),
            ),
            (
                "elasticsearch_cluster_config",
                "ElasticsearchClusterConfig",
                TypeInfo(ElasticsearchClusterConfigStatus),
            ),
            (
                "ebs_options",
                "EBSOptions",
                TypeInfo(EBSOptionsStatus),
            ),
            (
                "access_policies",
                "AccessPolicies",
                TypeInfo(AccessPoliciesStatus),
            ),
            (
                "snapshot_options",
                "SnapshotOptions",
                TypeInfo(SnapshotOptionsStatus),
            ),
            (
                "vpc_options",
                "VPCOptions",
                TypeInfo(VPCDerivedInfoStatus),
            ),
            (
                "cognito_options",
                "CognitoOptions",
                TypeInfo(CognitoOptionsStatus),
            ),
            (
                "encryption_at_rest_options",
                "EncryptionAtRestOptions",
                TypeInfo(EncryptionAtRestOptionsStatus),
            ),
            (
                "advanced_options",
                "AdvancedOptions",
                TypeInfo(AdvancedOptionsStatus),
            ),
            (
                "log_publishing_options",
                "LogPublishingOptions",
                TypeInfo(LogPublishingOptionsStatus),
            ),
        ]

    # String of format X.Y to specify version for the Elasticsearch domain.
    elasticsearch_version: "ElasticsearchVersionStatus" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Specifies the `ElasticsearchClusterConfig` for the Elasticsearch domain.
    elasticsearch_cluster_config: "ElasticsearchClusterConfigStatus" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Specifies the `EBSOptions` for the Elasticsearch domain.
    ebs_options: "EBSOptionsStatus" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # IAM access policy as a JSON-formatted string.
    access_policies: "AccessPoliciesStatus" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Specifies the `SnapshotOptions` for the Elasticsearch domain.
    snapshot_options: "SnapshotOptionsStatus" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The `VPCOptions` for the specified domain. For more information, see [VPC
    # Endpoints for Amazon Elasticsearch Service
    # Domains](http://docs.aws.amazon.com/elasticsearch-
    # service/latest/developerguide/es-vpc.html).
    vpc_options: "VPCDerivedInfoStatus" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The `CognitoOptions` for the specified domain. For more information, see
    # [Amazon Cognito Authentication for
    # Kibana](http://docs.aws.amazon.com/elasticsearch-
    # service/latest/developerguide/es-cognito-auth.html).
    cognito_options: "CognitoOptionsStatus" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Specifies the `EncryptionAtRestOptions` for the Elasticsearch domain.
    encryption_at_rest_options: "EncryptionAtRestOptionsStatus" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Specifies the `AdvancedOptions` for the domain. See [Configuring Advanced
    # Options](http://docs.aws.amazon.com/elasticsearch-
    # service/latest/developerguide/es-createupdatedomains.html#es-createdomain-
    # configure-advanced-options) for more information.
    advanced_options: "AdvancedOptionsStatus" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Log publishing options for the given domain.
    log_publishing_options: "LogPublishingOptionsStatus" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class ElasticsearchDomainStatus(ShapeBase):
    """
    The current status of an Elasticsearch domain.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "domain_id",
                "DomainId",
                TypeInfo(str),
            ),
            (
                "domain_name",
                "DomainName",
                TypeInfo(str),
            ),
            (
                "arn",
                "ARN",
                TypeInfo(str),
            ),
            (
                "elasticsearch_cluster_config",
                "ElasticsearchClusterConfig",
                TypeInfo(ElasticsearchClusterConfig),
            ),
            (
                "created",
                "Created",
                TypeInfo(bool),
            ),
            (
                "deleted",
                "Deleted",
                TypeInfo(bool),
            ),
            (
                "endpoint",
                "Endpoint",
                TypeInfo(str),
            ),
            (
                "endpoints",
                "Endpoints",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "processing",
                "Processing",
                TypeInfo(bool),
            ),
            (
                "upgrade_processing",
                "UpgradeProcessing",
                TypeInfo(bool),
            ),
            (
                "elasticsearch_version",
                "ElasticsearchVersion",
                TypeInfo(str),
            ),
            (
                "ebs_options",
                "EBSOptions",
                TypeInfo(EBSOptions),
            ),
            (
                "access_policies",
                "AccessPolicies",
                TypeInfo(str),
            ),
            (
                "snapshot_options",
                "SnapshotOptions",
                TypeInfo(SnapshotOptions),
            ),
            (
                "vpc_options",
                "VPCOptions",
                TypeInfo(VPCDerivedInfo),
            ),
            (
                "cognito_options",
                "CognitoOptions",
                TypeInfo(CognitoOptions),
            ),
            (
                "encryption_at_rest_options",
                "EncryptionAtRestOptions",
                TypeInfo(EncryptionAtRestOptions),
            ),
            (
                "advanced_options",
                "AdvancedOptions",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "log_publishing_options",
                "LogPublishingOptions",
                TypeInfo(
                    typing.Dict[typing.Union[str, LogType], LogPublishingOption]
                ),
            ),
        ]

    # The unique identifier for the specified Elasticsearch domain.
    domain_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The name of an Elasticsearch domain. Domain names are unique across the
    # domains owned by an account within an AWS region. Domain names start with a
    # letter or number and can contain the following characters: a-z (lowercase),
    # 0-9, and - (hyphen).
    domain_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The Amazon resource name (ARN) of an Elasticsearch domain. See [Identifiers
    # for IAM
    # Entities](http://docs.aws.amazon.com/IAM/latest/UserGuide/index.html?Using_Identifiers.html)
    # in _Using AWS Identity and Access Management_ for more information.
    arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The type and number of instances in the domain cluster.
    elasticsearch_cluster_config: "ElasticsearchClusterConfig" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The domain creation status. `True` if the creation of an Elasticsearch
    # domain is complete. `False` if domain creation is still in progress.
    created: bool = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The domain deletion status. `True` if a delete request has been received
    # for the domain but resource cleanup is still in progress. `False` if the
    # domain has not been deleted. Once domain deletion is complete, the status
    # of the domain is no longer returned.
    deleted: bool = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The Elasticsearch domain endpoint that you use to submit index and search
    # requests.
    endpoint: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Map containing the Elasticsearch domain endpoints used to submit index and
    # search requests. Example `key, value`: `'vpc','vpc-
    # endpoint-h2dsd34efgyghrtguk5gt6j2foh4.us-east-1.es.amazonaws.com'`.
    endpoints: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The status of the Elasticsearch domain configuration. `True` if Amazon
    # Elasticsearch Service is processing configuration changes. `False` if the
    # configuration is active.
    processing: bool = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The status of an Elasticsearch domain version upgrade. `True` if Amazon
    # Elasticsearch Service is undergoing a version upgrade. `False` if the
    # configuration is active.
    upgrade_processing: bool = dataclasses.field(default=ShapeBase.NOT_SET, )
    elasticsearch_version: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The `EBSOptions` for the specified domain. See [Configuring EBS-based
    # Storage](http://docs.aws.amazon.com/elasticsearch-
    # service/latest/developerguide/es-createupdatedomains.html#es-createdomain-
    # configure-ebs) for more information.
    ebs_options: "EBSOptions" = dataclasses.field(default=ShapeBase.NOT_SET, )

    # IAM access policy as a JSON-formatted string.
    access_policies: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Specifies the status of the `SnapshotOptions`
    snapshot_options: "SnapshotOptions" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The `VPCOptions` for the specified domain. For more information, see [VPC
    # Endpoints for Amazon Elasticsearch Service
    # Domains](http://docs.aws.amazon.com/elasticsearch-
    # service/latest/developerguide/es-vpc.html).
    vpc_options: "VPCDerivedInfo" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The `CognitoOptions` for the specified domain. For more information, see
    # [Amazon Cognito Authentication for
    # Kibana](http://docs.aws.amazon.com/elasticsearch-
    # service/latest/developerguide/es-cognito-auth.html).
    cognito_options: "CognitoOptions" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Specifies the status of the `EncryptionAtRestOptions`.
    encryption_at_rest_options: "EncryptionAtRestOptions" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Specifies the status of the `AdvancedOptions`
    advanced_options: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Log publishing options for the given domain.
    log_publishing_options: typing.Dict[
        typing.
        Union[str, "LogType"], "LogPublishingOption"] = dataclasses.field(
            default=ShapeBase.NOT_SET,
        )


@dataclasses.dataclass
class ElasticsearchVersionStatus(ShapeBase):
    """
    Status of the Elasticsearch version options for the specified Elasticsearch
    domain.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "options",
                "Options",
                TypeInfo(str),
            ),
            (
                "status",
                "Status",
                TypeInfo(OptionStatus),
            ),
        ]

    # Specifies the Elasticsearch version for the specified Elasticsearch domain.
    options: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Specifies the status of the Elasticsearch version options for the specified
    # Elasticsearch domain.
    status: "OptionStatus" = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class EncryptionAtRestOptions(ShapeBase):
    """
    Specifies the Encryption At Rest Options.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "enabled",
                "Enabled",
                TypeInfo(bool),
            ),
            (
                "kms_key_id",
                "KmsKeyId",
                TypeInfo(str),
            ),
        ]

    # Specifies the option to enable Encryption At Rest.
    enabled: bool = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Specifies the KMS Key ID for Encryption At Rest options.
    kms_key_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class EncryptionAtRestOptionsStatus(ShapeBase):
    """
    Status of the Encryption At Rest options for the specified Elasticsearch domain.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "options",
                "Options",
                TypeInfo(EncryptionAtRestOptions),
            ),
            (
                "status",
                "Status",
                TypeInfo(OptionStatus),
            ),
        ]

    # Specifies the Encryption At Rest options for the specified Elasticsearch
    # domain.
    options: "EncryptionAtRestOptions" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Specifies the status of the Encryption At Rest options for the specified
    # Elasticsearch domain.
    status: "OptionStatus" = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class GetCompatibleElasticsearchVersionsRequest(ShapeBase):
    """
    Container for request parameters to ` GetCompatibleElasticsearchVersions `
    operation.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "domain_name",
                "DomainName",
                TypeInfo(str),
            ),
        ]

    # The name of an Elasticsearch domain. Domain names are unique across the
    # domains owned by an account within an AWS region. Domain names start with a
    # letter or number and can contain the following characters: a-z (lowercase),
    # 0-9, and - (hyphen).
    domain_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class GetCompatibleElasticsearchVersionsResponse(OutputShapeBase):
    """
    Container for response returned by ` GetCompatibleElasticsearchVersions `
    operation.
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
                "compatible_elasticsearch_versions",
                "CompatibleElasticsearchVersions",
                TypeInfo(typing.List[CompatibleVersionsMap]),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A map of compatible Elasticsearch versions returned as part of the `
    # GetCompatibleElasticsearchVersions ` operation.
    compatible_elasticsearch_versions: typing.List["CompatibleVersionsMap"
                                                  ] = dataclasses.field(
                                                      default=ShapeBase.NOT_SET,
                                                  )


@dataclasses.dataclass
class GetUpgradeHistoryRequest(ShapeBase):
    """
    Container for request parameters to ` GetUpgradeHistory ` operation.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "domain_name",
                "DomainName",
                TypeInfo(str),
            ),
            (
                "max_results",
                "MaxResults",
                TypeInfo(int),
            ),
            (
                "next_token",
                "NextToken",
                TypeInfo(str),
            ),
        ]

    # The name of an Elasticsearch domain. Domain names are unique across the
    # domains owned by an account within an AWS region. Domain names start with a
    # letter or number and can contain the following characters: a-z (lowercase),
    # 0-9, and - (hyphen).
    domain_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Set this value to limit the number of results returned.
    max_results: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Paginated APIs accepts NextToken input to returns next page results and
    # provides a NextToken output in the response which can be used by the client
    # to retrieve more results.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class GetUpgradeHistoryResponse(OutputShapeBase):
    """
    Container for response returned by ` GetUpgradeHistory ` operation.
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
                "upgrade_histories",
                "UpgradeHistories",
                TypeInfo(typing.List[UpgradeHistory]),
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

    # A list of ` UpgradeHistory ` objects corresponding to each Upgrade or
    # Upgrade Eligibility Check performed on a domain returned as part of `
    # GetUpgradeHistoryResponse ` object.
    upgrade_histories: typing.List["UpgradeHistory"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Pagination token that needs to be supplied to the next call to get the next
    # page of results
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class GetUpgradeStatusRequest(ShapeBase):
    """
    Container for request parameters to ` GetUpgradeStatus ` operation.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "domain_name",
                "DomainName",
                TypeInfo(str),
            ),
        ]

    # The name of an Elasticsearch domain. Domain names are unique across the
    # domains owned by an account within an AWS region. Domain names start with a
    # letter or number and can contain the following characters: a-z (lowercase),
    # 0-9, and - (hyphen).
    domain_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class GetUpgradeStatusResponse(OutputShapeBase):
    """
    Container for response returned by ` GetUpgradeStatus ` operation.
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
                "upgrade_step",
                "UpgradeStep",
                TypeInfo(typing.Union[str, UpgradeStep]),
            ),
            (
                "step_status",
                "StepStatus",
                TypeInfo(typing.Union[str, UpgradeStatus]),
            ),
            (
                "upgrade_name",
                "UpgradeName",
                TypeInfo(str),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Represents one of 3 steps that an Upgrade or Upgrade Eligibility Check does
    # through:

    #   * PreUpgradeCheck
    #   * Snapshot
    #   * Upgrade
    upgrade_step: typing.Union[str, "UpgradeStep"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # One of 4 statuses that a step can go through returned as part of the `
    # GetUpgradeStatusResponse ` object. The status can take one of the following
    # values:

    #   * In Progress
    #   * Succeeded
    #   * Succeeded with Issues
    #   * Failed
    step_status: typing.Union[str, "UpgradeStatus"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A string that describes the update briefly
    upgrade_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class InstanceCountLimits(ShapeBase):
    """
    InstanceCountLimits represents the limits on number of instances that be created
    in Amazon Elasticsearch for given InstanceType.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "minimum_instance_count",
                "MinimumInstanceCount",
                TypeInfo(int),
            ),
            (
                "maximum_instance_count",
                "MaximumInstanceCount",
                TypeInfo(int),
            ),
        ]

    # Minimum number of Instances that can be instantiated for given
    # InstanceType.
    minimum_instance_count: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Maximum number of Instances that can be instantiated for given
    # InstanceType.
    maximum_instance_count: int = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class InstanceLimits(ShapeBase):
    """
    InstanceLimits represents the list of instance related attributes that are
    available for given InstanceType.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "instance_count_limits",
                "InstanceCountLimits",
                TypeInfo(InstanceCountLimits),
            ),
        ]

    # InstanceCountLimits represents the limits on number of instances that be
    # created in Amazon Elasticsearch for given InstanceType.
    instance_count_limits: "InstanceCountLimits" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class InternalException(ShapeBase):
    """
    The request processing has failed because of an unknown error, exception or
    failure (the failure is internal to the service) . Gives http status code of
    500.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class InvalidTypeException(ShapeBase):
    """
    An exception for trying to create or access sub-resource that is either invalid
    or not supported. Gives http status code of 409.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class LimitExceededException(ShapeBase):
    """
    An exception for trying to create more than allowed resources or sub-resources.
    Gives http status code of 409.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class Limits(ShapeBase):
    """
    Limits for given InstanceType and for each of it's role.  
    Limits contains following ` StorageTypes, ` ` InstanceLimits ` and `
    AdditionalLimits `
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "storage_types",
                "StorageTypes",
                TypeInfo(typing.List[StorageType]),
            ),
            (
                "instance_limits",
                "InstanceLimits",
                TypeInfo(InstanceLimits),
            ),
            (
                "additional_limits",
                "AdditionalLimits",
                TypeInfo(typing.List[AdditionalLimit]),
            ),
        ]

    # StorageType represents the list of storage related types and attributes
    # that are available for given InstanceType.
    storage_types: typing.List["StorageType"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # InstanceLimits represents the list of instance related attributes that are
    # available for given InstanceType.
    instance_limits: "InstanceLimits" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # List of additional limits that are specific to a given InstanceType and for
    # each of it's ` InstanceRole ` .
    additional_limits: typing.List["AdditionalLimit"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class ListDomainNamesResponse(OutputShapeBase):
    """
    The result of a `ListDomainNames` operation. Contains the names of all
    Elasticsearch domains owned by this account.
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
                "domain_names",
                "DomainNames",
                TypeInfo(typing.List[DomainInfo]),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # List of Elasticsearch domain names.
    domain_names: typing.List["DomainInfo"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class ListElasticsearchInstanceTypesRequest(ShapeBase):
    """
    Container for the parameters to the ` ListElasticsearchInstanceTypes `
    operation.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "elasticsearch_version",
                "ElasticsearchVersion",
                TypeInfo(str),
            ),
            (
                "domain_name",
                "DomainName",
                TypeInfo(str),
            ),
            (
                "max_results",
                "MaxResults",
                TypeInfo(int),
            ),
            (
                "next_token",
                "NextToken",
                TypeInfo(str),
            ),
        ]

    # Version of Elasticsearch for which list of supported elasticsearch instance
    # types are needed.
    elasticsearch_version: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # DomainName represents the name of the Domain that we are trying to modify.
    # This should be present only if we are querying for list of available
    # Elasticsearch instance types when modifying existing domain.
    domain_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Set this value to limit the number of results returned. Value provided must
    # be greater than 30 else it wont be honored.
    max_results: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # NextToken should be sent in case if earlier API call produced result
    # containing NextToken. It is used for pagination.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ListElasticsearchInstanceTypesResponse(OutputShapeBase):
    """
    Container for the parameters returned by ` ListElasticsearchInstanceTypes `
    operation.
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
                "elasticsearch_instance_types",
                "ElasticsearchInstanceTypes",
                TypeInfo(
                    typing.List[typing.Union[str, ESPartitionInstanceType]]
                ),
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

    # List of instance types supported by Amazon Elasticsearch service for given
    # ` ElasticsearchVersion `
    elasticsearch_instance_types: typing.List[
        typing.Union[str, "ESPartitionInstanceType"]] = dataclasses.field(
            default=ShapeBase.NOT_SET,
        )

    # In case if there are more results available NextToken would be present,
    # make further request to the same API with received NextToken to paginate
    # remaining results.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    def paginate(
        self,
    ) -> typing.Generator["ListElasticsearchInstanceTypesResponse", None, None]:
        yield from super()._paginate()


@dataclasses.dataclass
class ListElasticsearchVersionsRequest(ShapeBase):
    """
    Container for the parameters to the ` ListElasticsearchVersions ` operation.

    Use ` MaxResults ` to control the maximum number of results to retrieve in a
    single call.

    Use ` NextToken ` in response to retrieve more results. If the received response
    does not contain a NextToken, then there are no more results to retrieve.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "max_results",
                "MaxResults",
                TypeInfo(int),
            ),
            (
                "next_token",
                "NextToken",
                TypeInfo(str),
            ),
        ]

    # Set this value to limit the number of results returned. Value provided must
    # be greater than 10 else it wont be honored.
    max_results: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Paginated APIs accepts NextToken input to returns next page results and
    # provides a NextToken output in the response which can be used by the client
    # to retrieve more results.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ListElasticsearchVersionsResponse(OutputShapeBase):
    """
    Container for the parameters for response received from `
    ListElasticsearchVersions ` operation.
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
                "elasticsearch_versions",
                "ElasticsearchVersions",
                TypeInfo(typing.List[str]),
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

    # List of supported elastic search versions.
    elasticsearch_versions: typing.List[str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Paginated APIs accepts NextToken input to returns next page results and
    # provides a NextToken output in the response which can be used by the client
    # to retrieve more results.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    def paginate(
        self,
    ) -> typing.Generator["ListElasticsearchVersionsResponse", None, None]:
        yield from super()._paginate()


@dataclasses.dataclass
class ListTagsRequest(ShapeBase):
    """
    Container for the parameters to the `ListTags` operation. Specify the `ARN` for
    the Elasticsearch domain to which the tags are attached that you want to view
    are attached.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "arn",
                "ARN",
                TypeInfo(str),
            ),
        ]

    # Specify the `ARN` for the Elasticsearch domain to which the tags are
    # attached that you want to view.
    arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ListTagsResponse(OutputShapeBase):
    """
    The result of a `ListTags` operation. Contains tags for all requested
    Elasticsearch domains.
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
                "tag_list",
                "TagList",
                TypeInfo(typing.List[Tag]),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # List of `Tag` for the requested Elasticsearch domain.
    tag_list: typing.List["Tag"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class LogPublishingOption(ShapeBase):
    """
    Log Publishing option that is set for given domain.  
    Attributes and their details:

      * CloudWatchLogsLogGroupArn: ARN of the Cloudwatch log group to which log needs to be published.
      * Enabled: Whether the log publishing for given log type is enabled or not
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "cloud_watch_logs_log_group_arn",
                "CloudWatchLogsLogGroupArn",
                TypeInfo(str),
            ),
            (
                "enabled",
                "Enabled",
                TypeInfo(bool),
            ),
        ]

    # ARN of the Cloudwatch log group to which log needs to be published.
    cloud_watch_logs_log_group_arn: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Specifies whether given log publishing option is enabled or not.
    enabled: bool = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class LogPublishingOptionsStatus(ShapeBase):
    """
    The configured log publishing options for the domain and their current status.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "options",
                "Options",
                TypeInfo(
                    typing.Dict[typing.Union[str, LogType], LogPublishingOption]
                ),
            ),
            (
                "status",
                "Status",
                TypeInfo(OptionStatus),
            ),
        ]

    # The log publishing options configured for the Elasticsearch domain.
    options: typing.Dict[typing.Union[str, "LogType"], "LogPublishingOption"
                        ] = dataclasses.field(
                            default=ShapeBase.NOT_SET,
                        )

    # The status of the log publishing options for the Elasticsearch domain. See
    # `OptionStatus` for the status information that's included.
    status: "OptionStatus" = dataclasses.field(default=ShapeBase.NOT_SET, )


class LogType(str):
    """
    Type of Log File, it can be one of the following:

      * INDEX_SLOW_LOGS: Index slow logs contain insert requests that took more time than configured index query log threshold to execute.
      * SEARCH_SLOW_LOGS: Search slow logs contain search queries that took more time than configured search query log threshold to execute.
      * ES_APPLICATION_LOGS: Elasticsearch application logs contain information about errors and warnings raised during the operation of the service and can be useful for troubleshooting.
    """
    INDEX_SLOW_LOGS = "INDEX_SLOW_LOGS"
    SEARCH_SLOW_LOGS = "SEARCH_SLOW_LOGS"
    ES_APPLICATION_LOGS = "ES_APPLICATION_LOGS"


class OptionState(str):
    """
    The state of a requested change. One of the following:

      * Processing: The request change is still in-process.
      * Active: The request change is processed and deployed to the Elasticsearch domain.
    """
    RequiresIndexDocuments = "RequiresIndexDocuments"
    Processing = "Processing"
    Active = "Active"


@dataclasses.dataclass
class OptionStatus(ShapeBase):
    """
    Provides the current status of the entity.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "creation_date",
                "CreationDate",
                TypeInfo(datetime.datetime),
            ),
            (
                "update_date",
                "UpdateDate",
                TypeInfo(datetime.datetime),
            ),
            (
                "state",
                "State",
                TypeInfo(typing.Union[str, OptionState]),
            ),
            (
                "update_version",
                "UpdateVersion",
                TypeInfo(int),
            ),
            (
                "pending_deletion",
                "PendingDeletion",
                TypeInfo(bool),
            ),
        ]

    # Timestamp which tells the creation date for the entity.
    creation_date: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Timestamp which tells the last updated time for the entity.
    update_date: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Provides the `OptionState` for the Elasticsearch domain.
    state: typing.Union[str, "OptionState"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Specifies the latest version for the entity.
    update_version: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Indicates whether the Elasticsearch domain is being deleted.
    pending_deletion: bool = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class PurchaseReservedElasticsearchInstanceOfferingRequest(ShapeBase):
    """
    Container for parameters to `PurchaseReservedElasticsearchInstanceOffering`
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "reserved_elasticsearch_instance_offering_id",
                "ReservedElasticsearchInstanceOfferingId",
                TypeInfo(str),
            ),
            (
                "reservation_name",
                "ReservationName",
                TypeInfo(str),
            ),
            (
                "instance_count",
                "InstanceCount",
                TypeInfo(int),
            ),
        ]

    # The ID of the reserved Elasticsearch instance offering to purchase.
    reserved_elasticsearch_instance_offering_id: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A customer-specified identifier to track this reservation.
    reservation_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The number of Elasticsearch instances to reserve.
    instance_count: int = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class PurchaseReservedElasticsearchInstanceOfferingResponse(OutputShapeBase):
    """
    Represents the output of a `PurchaseReservedElasticsearchInstanceOffering`
    operation.
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
                "reserved_elasticsearch_instance_id",
                "ReservedElasticsearchInstanceId",
                TypeInfo(str),
            ),
            (
                "reservation_name",
                "ReservationName",
                TypeInfo(str),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Details of the reserved Elasticsearch instance which was purchased.
    reserved_elasticsearch_instance_id: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The customer-specified identifier used to track this reservation.
    reservation_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class RecurringCharge(ShapeBase):
    """
    Contains the specific price and frequency of a recurring charges for a reserved
    Elasticsearch instance, or for a reserved Elasticsearch instance offering.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "recurring_charge_amount",
                "RecurringChargeAmount",
                TypeInfo(float),
            ),
            (
                "recurring_charge_frequency",
                "RecurringChargeFrequency",
                TypeInfo(str),
            ),
        ]

    # The monetary amount of the recurring charge.
    recurring_charge_amount: float = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The frequency of the recurring charge.
    recurring_charge_frequency: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class RemoveTagsRequest(ShapeBase):
    """
    Container for the parameters to the `RemoveTags` operation. Specify the `ARN`
    for the Elasticsearch domain from which you want to remove the specified
    `TagKey`.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "arn",
                "ARN",
                TypeInfo(str),
            ),
            (
                "tag_keys",
                "TagKeys",
                TypeInfo(typing.List[str]),
            ),
        ]

    # Specifies the `ARN` for the Elasticsearch domain from which you want to
    # delete the specified tags.
    arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Specifies the `TagKey` list which you want to remove from the Elasticsearch
    # domain.
    tag_keys: typing.List[str] = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ReservedElasticsearchInstance(ShapeBase):
    """
    Details of a reserved Elasticsearch instance.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "reservation_name",
                "ReservationName",
                TypeInfo(str),
            ),
            (
                "reserved_elasticsearch_instance_id",
                "ReservedElasticsearchInstanceId",
                TypeInfo(str),
            ),
            (
                "reserved_elasticsearch_instance_offering_id",
                "ReservedElasticsearchInstanceOfferingId",
                TypeInfo(str),
            ),
            (
                "elasticsearch_instance_type",
                "ElasticsearchInstanceType",
                TypeInfo(typing.Union[str, ESPartitionInstanceType]),
            ),
            (
                "start_time",
                "StartTime",
                TypeInfo(datetime.datetime),
            ),
            (
                "duration",
                "Duration",
                TypeInfo(int),
            ),
            (
                "fixed_price",
                "FixedPrice",
                TypeInfo(float),
            ),
            (
                "usage_price",
                "UsagePrice",
                TypeInfo(float),
            ),
            (
                "currency_code",
                "CurrencyCode",
                TypeInfo(str),
            ),
            (
                "elasticsearch_instance_count",
                "ElasticsearchInstanceCount",
                TypeInfo(int),
            ),
            (
                "state",
                "State",
                TypeInfo(str),
            ),
            (
                "payment_option",
                "PaymentOption",
                TypeInfo(
                    typing.
                    Union[str, ReservedElasticsearchInstancePaymentOption]
                ),
            ),
            (
                "recurring_charges",
                "RecurringCharges",
                TypeInfo(typing.List[RecurringCharge]),
            ),
        ]

    # The customer-specified identifier to track this reservation.
    reservation_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The unique identifier for the reservation.
    reserved_elasticsearch_instance_id: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The offering identifier.
    reserved_elasticsearch_instance_offering_id: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The Elasticsearch instance type offered by the reserved instance offering.
    elasticsearch_instance_type: typing.Union[str, "ESPartitionInstanceType"
                                             ] = dataclasses.field(
                                                 default=ShapeBase.NOT_SET,
                                             )

    # The time the reservation started.
    start_time: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The duration, in seconds, for which the Elasticsearch instance is reserved.
    duration: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The upfront fixed charge you will paid to purchase the specific reserved
    # Elasticsearch instance offering.
    fixed_price: float = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The rate you are charged for each hour for the domain that is using this
    # reserved instance.
    usage_price: float = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The currency code for the reserved Elasticsearch instance offering.
    currency_code: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The number of Elasticsearch instances that have been reserved.
    elasticsearch_instance_count: int = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The state of the reserved Elasticsearch instance.
    state: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The payment option as defined in the reserved Elasticsearch instance
    # offering.
    payment_option: typing.Union[
        str, "ReservedElasticsearchInstancePaymentOption"] = dataclasses.field(
            default=ShapeBase.NOT_SET,
        )

    # The charge to your account regardless of whether you are creating any
    # domains using the instance offering.
    recurring_charges: typing.List["RecurringCharge"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class ReservedElasticsearchInstanceOffering(ShapeBase):
    """
    Details of a reserved Elasticsearch instance offering.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "reserved_elasticsearch_instance_offering_id",
                "ReservedElasticsearchInstanceOfferingId",
                TypeInfo(str),
            ),
            (
                "elasticsearch_instance_type",
                "ElasticsearchInstanceType",
                TypeInfo(typing.Union[str, ESPartitionInstanceType]),
            ),
            (
                "duration",
                "Duration",
                TypeInfo(int),
            ),
            (
                "fixed_price",
                "FixedPrice",
                TypeInfo(float),
            ),
            (
                "usage_price",
                "UsagePrice",
                TypeInfo(float),
            ),
            (
                "currency_code",
                "CurrencyCode",
                TypeInfo(str),
            ),
            (
                "payment_option",
                "PaymentOption",
                TypeInfo(
                    typing.
                    Union[str, ReservedElasticsearchInstancePaymentOption]
                ),
            ),
            (
                "recurring_charges",
                "RecurringCharges",
                TypeInfo(typing.List[RecurringCharge]),
            ),
        ]

    # The Elasticsearch reserved instance offering identifier.
    reserved_elasticsearch_instance_offering_id: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The Elasticsearch instance type offered by the reserved instance offering.
    elasticsearch_instance_type: typing.Union[str, "ESPartitionInstanceType"
                                             ] = dataclasses.field(
                                                 default=ShapeBase.NOT_SET,
                                             )

    # The duration, in seconds, for which the offering will reserve the
    # Elasticsearch instance.
    duration: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The upfront fixed charge you will pay to purchase the specific reserved
    # Elasticsearch instance offering.
    fixed_price: float = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The rate you are charged for each hour the domain that is using the
    # offering is running.
    usage_price: float = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The currency code for the reserved Elasticsearch instance offering.
    currency_code: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Payment option for the reserved Elasticsearch instance offering
    payment_option: typing.Union[
        str, "ReservedElasticsearchInstancePaymentOption"] = dataclasses.field(
            default=ShapeBase.NOT_SET,
        )

    # The charge to your account regardless of whether you are creating any
    # domains using the instance offering.
    recurring_charges: typing.List["RecurringCharge"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


class ReservedElasticsearchInstancePaymentOption(str):
    ALL_UPFRONT = "ALL_UPFRONT"
    PARTIAL_UPFRONT = "PARTIAL_UPFRONT"
    NO_UPFRONT = "NO_UPFRONT"


@dataclasses.dataclass
class ResourceAlreadyExistsException(ShapeBase):
    """
    An exception for creating a resource that already exists. Gives http status code
    of 400.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class ResourceNotFoundException(ShapeBase):
    """
    An exception for accessing or deleting a resource that does not exist. Gives
    http status code of 400.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class SnapshotOptions(ShapeBase):
    """
    Specifies the time, in UTC format, when the service takes a daily automated
    snapshot of the specified Elasticsearch domain. Default value is `0` hours.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "automated_snapshot_start_hour",
                "AutomatedSnapshotStartHour",
                TypeInfo(int),
            ),
        ]

    # Specifies the time, in UTC format, when the service takes a daily automated
    # snapshot of the specified Elasticsearch domain. Default value is `0` hours.
    automated_snapshot_start_hour: int = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class SnapshotOptionsStatus(ShapeBase):
    """
    Status of a daily automated snapshot.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "options",
                "Options",
                TypeInfo(SnapshotOptions),
            ),
            (
                "status",
                "Status",
                TypeInfo(OptionStatus),
            ),
        ]

    # Specifies the daily snapshot options specified for the Elasticsearch
    # domain.
    options: "SnapshotOptions" = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Specifies the status of a daily automated snapshot.
    status: "OptionStatus" = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class StorageType(ShapeBase):
    """
    StorageTypes represents the list of storage related types and their attributes
    that are available for given InstanceType.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "storage_type_name",
                "StorageTypeName",
                TypeInfo(str),
            ),
            (
                "storage_sub_type_name",
                "StorageSubTypeName",
                TypeInfo(str),
            ),
            (
                "storage_type_limits",
                "StorageTypeLimits",
                TypeInfo(typing.List[StorageTypeLimit]),
            ),
        ]

    # Type of the storage. List of available storage options:

    #   1. instance
    # Inbuilt storage available for the given Instance

    #   2. ebs
    # Elastic block storage that would be attached to the given Instance
    storage_type_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # SubType of the given storage type. List of available sub-storage options:
    # For "instance" storageType we wont have any storageSubType, in case of
    # "ebs" storageType we will have following valid storageSubTypes

    #   1. standard
    #   2. gp2
    #   3. io1

    # Refer `VolumeType` for more information regarding above EBS storage
    # options.
    storage_sub_type_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # List of limits that are applicable for given storage type.
    storage_type_limits: typing.List["StorageTypeLimit"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class StorageTypeLimit(ShapeBase):
    """
    Limits that are applicable for given storage type.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "limit_name",
                "LimitName",
                TypeInfo(str),
            ),
            (
                "limit_values",
                "LimitValues",
                TypeInfo(typing.List[str]),
            ),
        ]

    # Name of storage limits that are applicable for given storage type. If `
    # StorageType ` is ebs, following storage options are applicable

    #   1. MinimumVolumeSize
    # Minimum amount of volume size that is applicable for given storage type.It
    # can be empty if it is not applicable.

    #   2. MaximumVolumeSize
    # Maximum amount of volume size that is applicable for given storage type.It
    # can be empty if it is not applicable.

    #   3. MaximumIops
    # Maximum amount of Iops that is applicable for given storage type.It can be
    # empty if it is not applicable.

    #   4. MinimumIops
    # Minimum amount of Iops that is applicable for given storage type.It can be
    # empty if it is not applicable.
    limit_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Values for the ` StorageTypeLimit$LimitName ` .
    limit_values: typing.List[str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class Tag(ShapeBase):
    """
    Specifies a key value pair for a resource tag.
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

    # Specifies the `TagKey`, the name of the tag. Tag keys must be unique for
    # the Elasticsearch domain to which they are attached.
    key: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Specifies the `TagValue`, the value assigned to the corresponding tag key.
    # Tag values can be null and do not have to be unique in a tag set. For
    # example, you can have a key value pair in a tag set of `project : Trinity`
    # and `cost-center : Trinity`
    value: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class UpdateElasticsearchDomainConfigRequest(ShapeBase):
    """
    Container for the parameters to the `UpdateElasticsearchDomain` operation.
    Specifies the type and number of instances in the domain cluster.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "domain_name",
                "DomainName",
                TypeInfo(str),
            ),
            (
                "elasticsearch_cluster_config",
                "ElasticsearchClusterConfig",
                TypeInfo(ElasticsearchClusterConfig),
            ),
            (
                "ebs_options",
                "EBSOptions",
                TypeInfo(EBSOptions),
            ),
            (
                "snapshot_options",
                "SnapshotOptions",
                TypeInfo(SnapshotOptions),
            ),
            (
                "vpc_options",
                "VPCOptions",
                TypeInfo(VPCOptions),
            ),
            (
                "cognito_options",
                "CognitoOptions",
                TypeInfo(CognitoOptions),
            ),
            (
                "advanced_options",
                "AdvancedOptions",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "access_policies",
                "AccessPolicies",
                TypeInfo(str),
            ),
            (
                "log_publishing_options",
                "LogPublishingOptions",
                TypeInfo(
                    typing.Dict[typing.Union[str, LogType], LogPublishingOption]
                ),
            ),
        ]

    # The name of the Elasticsearch domain that you are updating.
    domain_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The type and number of instances to instantiate for the domain cluster.
    elasticsearch_cluster_config: "ElasticsearchClusterConfig" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Specify the type and size of the EBS volume that you want to use.
    ebs_options: "EBSOptions" = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Option to set the time, in UTC format, for the daily automated snapshot.
    # Default value is `0` hours.
    snapshot_options: "SnapshotOptions" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Options to specify the subnets and security groups for VPC endpoint. For
    # more information, see [Creating a
    # VPC](http://docs.aws.amazon.com/elasticsearch-
    # service/latest/developerguide/es-vpc.html#es-creating-vpc) in _VPC
    # Endpoints for Amazon Elasticsearch Service Domains_
    vpc_options: "VPCOptions" = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Options to specify the Cognito user and identity pools for Kibana
    # authentication. For more information, see [Amazon Cognito Authentication
    # for Kibana](http://docs.aws.amazon.com/elasticsearch-
    # service/latest/developerguide/es-cognito-auth.html).
    cognito_options: "CognitoOptions" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Modifies the advanced option to allow references to indices in an HTTP
    # request body. Must be `false` when configuring access to individual sub-
    # resources. By default, the value is `true`. See [Configuration Advanced
    # Options](http://docs.aws.amazon.com/elasticsearch-
    # service/latest/developerguide/es-createupdatedomains.html#es-createdomain-
    # configure-advanced-options) for more information.
    advanced_options: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # IAM access policy as a JSON-formatted string.
    access_policies: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Map of `LogType` and `LogPublishingOption`, each containing options to
    # publish a given type of Elasticsearch log.
    log_publishing_options: typing.Dict[
        typing.
        Union[str, "LogType"], "LogPublishingOption"] = dataclasses.field(
            default=ShapeBase.NOT_SET,
        )


@dataclasses.dataclass
class UpdateElasticsearchDomainConfigResponse(OutputShapeBase):
    """
    The result of an `UpdateElasticsearchDomain` request. Contains the status of the
    Elasticsearch domain being updated.
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
                "domain_config",
                "DomainConfig",
                TypeInfo(ElasticsearchDomainConfig),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The status of the updated Elasticsearch domain.
    domain_config: "ElasticsearchDomainConfig" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class UpgradeElasticsearchDomainRequest(ShapeBase):
    """
    Container for request parameters to ` UpgradeElasticsearchDomain ` operation.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "domain_name",
                "DomainName",
                TypeInfo(str),
            ),
            (
                "target_version",
                "TargetVersion",
                TypeInfo(str),
            ),
            (
                "perform_check_only",
                "PerformCheckOnly",
                TypeInfo(bool),
            ),
        ]

    # The name of an Elasticsearch domain. Domain names are unique across the
    # domains owned by an account within an AWS region. Domain names start with a
    # letter or number and can contain the following characters: a-z (lowercase),
    # 0-9, and - (hyphen).
    domain_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The version of Elasticsearch that you intend to upgrade the domain to.
    target_version: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # This flag, when set to True, indicates that an Upgrade Eligibility Check
    # needs to be performed. This will not actually perform the Upgrade.
    perform_check_only: bool = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class UpgradeElasticsearchDomainResponse(OutputShapeBase):
    """
    Container for response returned by ` UpgradeElasticsearchDomain ` operation.
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
                "domain_name",
                "DomainName",
                TypeInfo(str),
            ),
            (
                "target_version",
                "TargetVersion",
                TypeInfo(str),
            ),
            (
                "perform_check_only",
                "PerformCheckOnly",
                TypeInfo(bool),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The name of an Elasticsearch domain. Domain names are unique across the
    # domains owned by an account within an AWS region. Domain names start with a
    # letter or number and can contain the following characters: a-z (lowercase),
    # 0-9, and - (hyphen).
    domain_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The version of Elasticsearch that you intend to upgrade the domain to.
    target_version: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # This flag, when set to True, indicates that an Upgrade Eligibility Check
    # needs to be performed. This will not actually perform the Upgrade.
    perform_check_only: bool = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class UpgradeHistory(ShapeBase):
    """
    History of the last 10 Upgrades and Upgrade Eligibility Checks.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "upgrade_name",
                "UpgradeName",
                TypeInfo(str),
            ),
            (
                "start_timestamp",
                "StartTimestamp",
                TypeInfo(datetime.datetime),
            ),
            (
                "upgrade_status",
                "UpgradeStatus",
                TypeInfo(typing.Union[str, UpgradeStatus]),
            ),
            (
                "steps_list",
                "StepsList",
                TypeInfo(typing.List[UpgradeStepItem]),
            ),
        ]

    # A string that describes the update briefly
    upgrade_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # UTC Timestamp at which the Upgrade API call was made in "yyyy-MM-
    # ddTHH:mm:ssZ" format.
    start_timestamp: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The overall status of the update. The status can take one of the following
    # values:

    #   * In Progress
    #   * Succeeded
    #   * Succeeded with Issues
    #   * Failed
    upgrade_status: typing.Union[str, "UpgradeStatus"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A list of ` UpgradeStepItem ` s representing information about each step
    # performed as pard of a specific Upgrade or Upgrade Eligibility Check.
    steps_list: typing.List["UpgradeStepItem"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


class UpgradeStatus(str):
    IN_PROGRESS = "IN_PROGRESS"
    SUCCEEDED = "SUCCEEDED"
    SUCCEEDED_WITH_ISSUES = "SUCCEEDED_WITH_ISSUES"
    FAILED = "FAILED"


class UpgradeStep(str):
    PRE_UPGRADE_CHECK = "PRE_UPGRADE_CHECK"
    SNAPSHOT = "SNAPSHOT"
    UPGRADE = "UPGRADE"


@dataclasses.dataclass
class UpgradeStepItem(ShapeBase):
    """
    Represents a single step of the Upgrade or Upgrade Eligibility Check workflow.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "upgrade_step",
                "UpgradeStep",
                TypeInfo(typing.Union[str, UpgradeStep]),
            ),
            (
                "upgrade_step_status",
                "UpgradeStepStatus",
                TypeInfo(typing.Union[str, UpgradeStatus]),
            ),
            (
                "issues",
                "Issues",
                TypeInfo(typing.List[str]),
            ),
            (
                "progress_percent",
                "ProgressPercent",
                TypeInfo(float),
            ),
        ]

    # Represents one of 3 steps that an Upgrade or Upgrade Eligibility Check does
    # through:

    #   * PreUpgradeCheck
    #   * Snapshot
    #   * Upgrade
    upgrade_step: typing.Union[str, "UpgradeStep"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The status of a particular step during an upgrade. The status can take one
    # of the following values:

    #   * In Progress
    #   * Succeeded
    #   * Succeeded with Issues
    #   * Failed
    upgrade_step_status: typing.Union[str, "UpgradeStatus"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A list of strings containing detailed information about the errors
    # encountered in a particular step.
    issues: typing.List[str] = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The Floating point value representing progress percentage of a particular
    # step.
    progress_percent: float = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class VPCDerivedInfo(ShapeBase):
    """
    Options to specify the subnets and security groups for VPC endpoint. For more
    information, see [ VPC Endpoints for Amazon Elasticsearch Service
    Domains](http://docs.aws.amazon.com/elasticsearch-
    service/latest/developerguide/es-vpc.html).
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "vpc_id",
                "VPCId",
                TypeInfo(str),
            ),
            (
                "subnet_ids",
                "SubnetIds",
                TypeInfo(typing.List[str]),
            ),
            (
                "availability_zones",
                "AvailabilityZones",
                TypeInfo(typing.List[str]),
            ),
            (
                "security_group_ids",
                "SecurityGroupIds",
                TypeInfo(typing.List[str]),
            ),
        ]

    # The VPC Id for the Elasticsearch domain. Exists only if the domain was
    # created with VPCOptions.
    vpc_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Specifies the subnets for VPC endpoint.
    subnet_ids: typing.List[str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The availability zones for the Elasticsearch domain. Exists only if the
    # domain was created with VPCOptions.
    availability_zones: typing.List[str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Specifies the security groups for VPC endpoint.
    security_group_ids: typing.List[str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class VPCDerivedInfoStatus(ShapeBase):
    """
    Status of the VPC options for the specified Elasticsearch domain.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "options",
                "Options",
                TypeInfo(VPCDerivedInfo),
            ),
            (
                "status",
                "Status",
                TypeInfo(OptionStatus),
            ),
        ]

    # Specifies the VPC options for the specified Elasticsearch domain.
    options: "VPCDerivedInfo" = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Specifies the status of the VPC options for the specified Elasticsearch
    # domain.
    status: "OptionStatus" = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class VPCOptions(ShapeBase):
    """
    Options to specify the subnets and security groups for VPC endpoint. For more
    information, see [ VPC Endpoints for Amazon Elasticsearch Service
    Domains](http://docs.aws.amazon.com/elasticsearch-
    service/latest/developerguide/es-vpc.html).
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "subnet_ids",
                "SubnetIds",
                TypeInfo(typing.List[str]),
            ),
            (
                "security_group_ids",
                "SecurityGroupIds",
                TypeInfo(typing.List[str]),
            ),
        ]

    # Specifies the subnets for VPC endpoint.
    subnet_ids: typing.List[str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Specifies the security groups for VPC endpoint.
    security_group_ids: typing.List[str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class ValidationException(ShapeBase):
    """
    An exception for missing / invalid input fields. Gives http status code of 400.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


class VolumeType(str):
    """
    The type of EBS volume, standard, gp2, or io1. See [Configuring EBS-based
    Storage](http://docs.aws.amazon.com/elasticsearch-
    service/latest/developerguide/es-createupdatedomains.html#es-createdomain-
    configure-ebs)for more information.
    """
    standard = "standard"
    gp2 = "gp2"
    io1 = "io1"
