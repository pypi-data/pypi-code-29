import datetime
import typing
import boto3
from autoboto import ClientBase, ShapeBase, OutputShapeBase
from . import shapes


class Client(ClientBase):
    def __init__(self, *args, **kwargs):
        super().__init__("cloudhsmv2", *args, **kwargs)

    def copy_backup_to_region(
        self,
        _request: shapes.CopyBackupToRegionRequest = None,
        *,
        destination_region: str,
        backup_id: str,
    ) -> shapes.CopyBackupToRegionResponse:
        """
        Copy an AWS CloudHSM cluster backup to a different region.
        """
        if _request is None:
            _params = {}
            if destination_region is not ShapeBase.NOT_SET:
                _params['destination_region'] = destination_region
            if backup_id is not ShapeBase.NOT_SET:
                _params['backup_id'] = backup_id
            _request = shapes.CopyBackupToRegionRequest(**_params)
        response = self._boto_client.copy_backup_to_region(**_request.to_boto())

        return shapes.CopyBackupToRegionResponse.from_boto(response)

    def create_cluster(
        self,
        _request: shapes.CreateClusterRequest = None,
        *,
        subnet_ids: typing.List[str],
        hsm_type: str,
        source_backup_id: str = ShapeBase.NOT_SET,
    ) -> shapes.CreateClusterResponse:
        """
        Creates a new AWS CloudHSM cluster.
        """
        if _request is None:
            _params = {}
            if subnet_ids is not ShapeBase.NOT_SET:
                _params['subnet_ids'] = subnet_ids
            if hsm_type is not ShapeBase.NOT_SET:
                _params['hsm_type'] = hsm_type
            if source_backup_id is not ShapeBase.NOT_SET:
                _params['source_backup_id'] = source_backup_id
            _request = shapes.CreateClusterRequest(**_params)
        response = self._boto_client.create_cluster(**_request.to_boto())

        return shapes.CreateClusterResponse.from_boto(response)

    def create_hsm(
        self,
        _request: shapes.CreateHsmRequest = None,
        *,
        cluster_id: str,
        availability_zone: str,
        ip_address: str = ShapeBase.NOT_SET,
    ) -> shapes.CreateHsmResponse:
        """
        Creates a new hardware security module (HSM) in the specified AWS CloudHSM
        cluster.
        """
        if _request is None:
            _params = {}
            if cluster_id is not ShapeBase.NOT_SET:
                _params['cluster_id'] = cluster_id
            if availability_zone is not ShapeBase.NOT_SET:
                _params['availability_zone'] = availability_zone
            if ip_address is not ShapeBase.NOT_SET:
                _params['ip_address'] = ip_address
            _request = shapes.CreateHsmRequest(**_params)
        response = self._boto_client.create_hsm(**_request.to_boto())

        return shapes.CreateHsmResponse.from_boto(response)

    def delete_backup(
        self,
        _request: shapes.DeleteBackupRequest = None,
        *,
        backup_id: str,
    ) -> shapes.DeleteBackupResponse:
        """
        Deletes a specified AWS CloudHSM backup. A backup can be restored up to 7 days
        after the DeleteBackup request. For more information on restoring a backup, see
        RestoreBackup
        """
        if _request is None:
            _params = {}
            if backup_id is not ShapeBase.NOT_SET:
                _params['backup_id'] = backup_id
            _request = shapes.DeleteBackupRequest(**_params)
        response = self._boto_client.delete_backup(**_request.to_boto())

        return shapes.DeleteBackupResponse.from_boto(response)

    def delete_cluster(
        self,
        _request: shapes.DeleteClusterRequest = None,
        *,
        cluster_id: str,
    ) -> shapes.DeleteClusterResponse:
        """
        Deletes the specified AWS CloudHSM cluster. Before you can delete a cluster, you
        must delete all HSMs in the cluster. To see if the cluster contains any HSMs,
        use DescribeClusters. To delete an HSM, use DeleteHsm.
        """
        if _request is None:
            _params = {}
            if cluster_id is not ShapeBase.NOT_SET:
                _params['cluster_id'] = cluster_id
            _request = shapes.DeleteClusterRequest(**_params)
        response = self._boto_client.delete_cluster(**_request.to_boto())

        return shapes.DeleteClusterResponse.from_boto(response)

    def delete_hsm(
        self,
        _request: shapes.DeleteHsmRequest = None,
        *,
        cluster_id: str,
        hsm_id: str = ShapeBase.NOT_SET,
        eni_id: str = ShapeBase.NOT_SET,
        eni_ip: str = ShapeBase.NOT_SET,
    ) -> shapes.DeleteHsmResponse:
        """
        Deletes the specified HSM. To specify an HSM, you can use its identifier (ID),
        the IP address of the HSM's elastic network interface (ENI), or the ID of the
        HSM's ENI. You need to specify only one of these values. To find these values,
        use DescribeClusters.
        """
        if _request is None:
            _params = {}
            if cluster_id is not ShapeBase.NOT_SET:
                _params['cluster_id'] = cluster_id
            if hsm_id is not ShapeBase.NOT_SET:
                _params['hsm_id'] = hsm_id
            if eni_id is not ShapeBase.NOT_SET:
                _params['eni_id'] = eni_id
            if eni_ip is not ShapeBase.NOT_SET:
                _params['eni_ip'] = eni_ip
            _request = shapes.DeleteHsmRequest(**_params)
        response = self._boto_client.delete_hsm(**_request.to_boto())

        return shapes.DeleteHsmResponse.from_boto(response)

    def describe_backups(
        self,
        _request: shapes.DescribeBackupsRequest = None,
        *,
        next_token: str = ShapeBase.NOT_SET,
        max_results: int = ShapeBase.NOT_SET,
        filters: typing.Dict[str, typing.List[str]] = ShapeBase.NOT_SET,
        sort_ascending: bool = ShapeBase.NOT_SET,
    ) -> shapes.DescribeBackupsResponse:
        """
        Gets information about backups of AWS CloudHSM clusters.

        This is a paginated operation, which means that each response might contain only
        a subset of all the backups. When the response contains only a subset of
        backups, it includes a `NextToken` value. Use this value in a subsequent
        `DescribeBackups` request to get more backups. When you receive a response with
        no `NextToken` (or an empty or null value), that means there are no more backups
        to get.
        """
        if _request is None:
            _params = {}
            if next_token is not ShapeBase.NOT_SET:
                _params['next_token'] = next_token
            if max_results is not ShapeBase.NOT_SET:
                _params['max_results'] = max_results
            if filters is not ShapeBase.NOT_SET:
                _params['filters'] = filters
            if sort_ascending is not ShapeBase.NOT_SET:
                _params['sort_ascending'] = sort_ascending
            _request = shapes.DescribeBackupsRequest(**_params)
        paginator = self.get_paginator("describe_backups").paginate(
            **_request.to_boto()
        )
        page_generator = (page for page in paginator)
        first_page = next(page_generator)
        result = shapes.DescribeBackupsResponse.from_boto(first_page)
        result._page_iterator = page_generator
        return result

        return shapes.DescribeBackupsResponse.from_boto(response)

    def describe_clusters(
        self,
        _request: shapes.DescribeClustersRequest = None,
        *,
        filters: typing.Dict[str, typing.List[str]] = ShapeBase.NOT_SET,
        next_token: str = ShapeBase.NOT_SET,
        max_results: int = ShapeBase.NOT_SET,
    ) -> shapes.DescribeClustersResponse:
        """
        Gets information about AWS CloudHSM clusters.

        This is a paginated operation, which means that each response might contain only
        a subset of all the clusters. When the response contains only a subset of
        clusters, it includes a `NextToken` value. Use this value in a subsequent
        `DescribeClusters` request to get more clusters. When you receive a response
        with no `NextToken` (or an empty or null value), that means there are no more
        clusters to get.
        """
        if _request is None:
            _params = {}
            if filters is not ShapeBase.NOT_SET:
                _params['filters'] = filters
            if next_token is not ShapeBase.NOT_SET:
                _params['next_token'] = next_token
            if max_results is not ShapeBase.NOT_SET:
                _params['max_results'] = max_results
            _request = shapes.DescribeClustersRequest(**_params)
        paginator = self.get_paginator("describe_clusters").paginate(
            **_request.to_boto()
        )
        page_generator = (page for page in paginator)
        first_page = next(page_generator)
        result = shapes.DescribeClustersResponse.from_boto(first_page)
        result._page_iterator = page_generator
        return result

        return shapes.DescribeClustersResponse.from_boto(response)

    def initialize_cluster(
        self,
        _request: shapes.InitializeClusterRequest = None,
        *,
        cluster_id: str,
        signed_cert: str,
        trust_anchor: str,
    ) -> shapes.InitializeClusterResponse:
        """
        Claims an AWS CloudHSM cluster by submitting the cluster certificate issued by
        your issuing certificate authority (CA) and the CA's root certificate. Before
        you can claim a cluster, you must sign the cluster's certificate signing request
        (CSR) with your issuing CA. To get the cluster's CSR, use DescribeClusters.
        """
        if _request is None:
            _params = {}
            if cluster_id is not ShapeBase.NOT_SET:
                _params['cluster_id'] = cluster_id
            if signed_cert is not ShapeBase.NOT_SET:
                _params['signed_cert'] = signed_cert
            if trust_anchor is not ShapeBase.NOT_SET:
                _params['trust_anchor'] = trust_anchor
            _request = shapes.InitializeClusterRequest(**_params)
        response = self._boto_client.initialize_cluster(**_request.to_boto())

        return shapes.InitializeClusterResponse.from_boto(response)

    def list_tags(
        self,
        _request: shapes.ListTagsRequest = None,
        *,
        resource_id: str,
        next_token: str = ShapeBase.NOT_SET,
        max_results: int = ShapeBase.NOT_SET,
    ) -> shapes.ListTagsResponse:
        """
        Gets a list of tags for the specified AWS CloudHSM cluster.

        This is a paginated operation, which means that each response might contain only
        a subset of all the tags. When the response contains only a subset of tags, it
        includes a `NextToken` value. Use this value in a subsequent `ListTags` request
        to get more tags. When you receive a response with no `NextToken` (or an empty
        or null value), that means there are no more tags to get.
        """
        if _request is None:
            _params = {}
            if resource_id is not ShapeBase.NOT_SET:
                _params['resource_id'] = resource_id
            if next_token is not ShapeBase.NOT_SET:
                _params['next_token'] = next_token
            if max_results is not ShapeBase.NOT_SET:
                _params['max_results'] = max_results
            _request = shapes.ListTagsRequest(**_params)
        paginator = self.get_paginator("list_tags").paginate(
            **_request.to_boto()
        )
        page_generator = (page for page in paginator)
        first_page = next(page_generator)
        result = shapes.ListTagsResponse.from_boto(first_page)
        result._page_iterator = page_generator
        return result

        return shapes.ListTagsResponse.from_boto(response)

    def restore_backup(
        self,
        _request: shapes.RestoreBackupRequest = None,
        *,
        backup_id: str,
    ) -> shapes.RestoreBackupResponse:
        """
        Restores a specified AWS CloudHSM backup that is in the `PENDING_DELETION`
        state. For more information on deleting a backup, see DeleteBackup.
        """
        if _request is None:
            _params = {}
            if backup_id is not ShapeBase.NOT_SET:
                _params['backup_id'] = backup_id
            _request = shapes.RestoreBackupRequest(**_params)
        response = self._boto_client.restore_backup(**_request.to_boto())

        return shapes.RestoreBackupResponse.from_boto(response)

    def tag_resource(
        self,
        _request: shapes.TagResourceRequest = None,
        *,
        resource_id: str,
        tag_list: typing.List[shapes.Tag],
    ) -> shapes.TagResourceResponse:
        """
        Adds or overwrites one or more tags for the specified AWS CloudHSM cluster.
        """
        if _request is None:
            _params = {}
            if resource_id is not ShapeBase.NOT_SET:
                _params['resource_id'] = resource_id
            if tag_list is not ShapeBase.NOT_SET:
                _params['tag_list'] = tag_list
            _request = shapes.TagResourceRequest(**_params)
        response = self._boto_client.tag_resource(**_request.to_boto())

        return shapes.TagResourceResponse.from_boto(response)

    def untag_resource(
        self,
        _request: shapes.UntagResourceRequest = None,
        *,
        resource_id: str,
        tag_key_list: typing.List[str],
    ) -> shapes.UntagResourceResponse:
        """
        Removes the specified tag or tags from the specified AWS CloudHSM cluster.
        """
        if _request is None:
            _params = {}
            if resource_id is not ShapeBase.NOT_SET:
                _params['resource_id'] = resource_id
            if tag_key_list is not ShapeBase.NOT_SET:
                _params['tag_key_list'] = tag_key_list
            _request = shapes.UntagResourceRequest(**_params)
        response = self._boto_client.untag_resource(**_request.to_boto())

        return shapes.UntagResourceResponse.from_boto(response)
