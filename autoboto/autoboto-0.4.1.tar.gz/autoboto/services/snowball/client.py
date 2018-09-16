import datetime
import typing
import boto3
from autoboto import ClientBase, ShapeBase, OutputShapeBase
from . import shapes


class Client(ClientBase):
    def __init__(self, *args, **kwargs):
        super().__init__("snowball", *args, **kwargs)

    def cancel_cluster(
        self,
        _request: shapes.CancelClusterRequest = None,
        *,
        cluster_id: str,
    ) -> shapes.CancelClusterResult:
        """
        Cancels a cluster job. You can only cancel a cluster job while it's in the
        `AwaitingQuorum` status. You'll have at least an hour after creating a cluster
        job to cancel it.
        """
        if _request is None:
            _params = {}
            if cluster_id is not ShapeBase.NOT_SET:
                _params['cluster_id'] = cluster_id
            _request = shapes.CancelClusterRequest(**_params)
        response = self._boto_client.cancel_cluster(**_request.to_boto())

        return shapes.CancelClusterResult.from_boto(response)

    def cancel_job(
        self,
        _request: shapes.CancelJobRequest = None,
        *,
        job_id: str,
    ) -> shapes.CancelJobResult:
        """
        Cancels the specified job. You can only cancel a job before its `JobState` value
        changes to `PreparingAppliance`. Requesting the `ListJobs` or `DescribeJob`
        action returns a job's `JobState` as part of the response element data returned.
        """
        if _request is None:
            _params = {}
            if job_id is not ShapeBase.NOT_SET:
                _params['job_id'] = job_id
            _request = shapes.CancelJobRequest(**_params)
        response = self._boto_client.cancel_job(**_request.to_boto())

        return shapes.CancelJobResult.from_boto(response)

    def create_address(
        self,
        _request: shapes.CreateAddressRequest = None,
        *,
        address: shapes.Address,
    ) -> shapes.CreateAddressResult:
        """
        Creates an address for a Snowball to be shipped to. In most regions, addresses
        are validated at the time of creation. The address you provide must be located
        within the serviceable area of your region. If the address is invalid or
        unsupported, then an exception is thrown.
        """
        if _request is None:
            _params = {}
            if address is not ShapeBase.NOT_SET:
                _params['address'] = address
            _request = shapes.CreateAddressRequest(**_params)
        response = self._boto_client.create_address(**_request.to_boto())

        return shapes.CreateAddressResult.from_boto(response)

    def create_cluster(
        self,
        _request: shapes.CreateClusterRequest = None,
        *,
        job_type: typing.Union[str, shapes.JobType],
        resources: shapes.JobResource,
        address_id: str,
        role_arn: str,
        shipping_option: typing.Union[str, shapes.ShippingOption],
        description: str = ShapeBase.NOT_SET,
        kms_key_arn: str = ShapeBase.NOT_SET,
        snowball_type: typing.Union[str, shapes.SnowballType] = ShapeBase.
        NOT_SET,
        notification: shapes.Notification = ShapeBase.NOT_SET,
        forwarding_address_id: str = ShapeBase.NOT_SET,
    ) -> shapes.CreateClusterResult:
        """
        Creates an empty cluster. Each cluster supports five nodes. You use the
        CreateJob action separately to create the jobs for each of these nodes. The
        cluster does not ship until these five node jobs have been created.
        """
        if _request is None:
            _params = {}
            if job_type is not ShapeBase.NOT_SET:
                _params['job_type'] = job_type
            if resources is not ShapeBase.NOT_SET:
                _params['resources'] = resources
            if address_id is not ShapeBase.NOT_SET:
                _params['address_id'] = address_id
            if role_arn is not ShapeBase.NOT_SET:
                _params['role_arn'] = role_arn
            if shipping_option is not ShapeBase.NOT_SET:
                _params['shipping_option'] = shipping_option
            if description is not ShapeBase.NOT_SET:
                _params['description'] = description
            if kms_key_arn is not ShapeBase.NOT_SET:
                _params['kms_key_arn'] = kms_key_arn
            if snowball_type is not ShapeBase.NOT_SET:
                _params['snowball_type'] = snowball_type
            if notification is not ShapeBase.NOT_SET:
                _params['notification'] = notification
            if forwarding_address_id is not ShapeBase.NOT_SET:
                _params['forwarding_address_id'] = forwarding_address_id
            _request = shapes.CreateClusterRequest(**_params)
        response = self._boto_client.create_cluster(**_request.to_boto())

        return shapes.CreateClusterResult.from_boto(response)

    def create_job(
        self,
        _request: shapes.CreateJobRequest = None,
        *,
        job_type: typing.Union[str, shapes.JobType] = ShapeBase.NOT_SET,
        resources: shapes.JobResource = ShapeBase.NOT_SET,
        description: str = ShapeBase.NOT_SET,
        address_id: str = ShapeBase.NOT_SET,
        kms_key_arn: str = ShapeBase.NOT_SET,
        role_arn: str = ShapeBase.NOT_SET,
        snowball_capacity_preference: typing.
        Union[str, shapes.SnowballCapacity] = ShapeBase.NOT_SET,
        shipping_option: typing.Union[str, shapes.
                                      ShippingOption] = ShapeBase.NOT_SET,
        notification: shapes.Notification = ShapeBase.NOT_SET,
        cluster_id: str = ShapeBase.NOT_SET,
        snowball_type: typing.Union[str, shapes.
                                    SnowballType] = ShapeBase.NOT_SET,
        forwarding_address_id: str = ShapeBase.NOT_SET,
    ) -> shapes.CreateJobResult:
        """
        Creates a job to import or export data between Amazon S3 and your on-premises
        data center. Your AWS account must have the right trust policies and permissions
        in place to create a job for Snowball. If you're creating a job for a node in a
        cluster, you only need to provide the `clusterId` value; the other job
        attributes are inherited from the cluster.
        """
        if _request is None:
            _params = {}
            if job_type is not ShapeBase.NOT_SET:
                _params['job_type'] = job_type
            if resources is not ShapeBase.NOT_SET:
                _params['resources'] = resources
            if description is not ShapeBase.NOT_SET:
                _params['description'] = description
            if address_id is not ShapeBase.NOT_SET:
                _params['address_id'] = address_id
            if kms_key_arn is not ShapeBase.NOT_SET:
                _params['kms_key_arn'] = kms_key_arn
            if role_arn is not ShapeBase.NOT_SET:
                _params['role_arn'] = role_arn
            if snowball_capacity_preference is not ShapeBase.NOT_SET:
                _params['snowball_capacity_preference'
                       ] = snowball_capacity_preference
            if shipping_option is not ShapeBase.NOT_SET:
                _params['shipping_option'] = shipping_option
            if notification is not ShapeBase.NOT_SET:
                _params['notification'] = notification
            if cluster_id is not ShapeBase.NOT_SET:
                _params['cluster_id'] = cluster_id
            if snowball_type is not ShapeBase.NOT_SET:
                _params['snowball_type'] = snowball_type
            if forwarding_address_id is not ShapeBase.NOT_SET:
                _params['forwarding_address_id'] = forwarding_address_id
            _request = shapes.CreateJobRequest(**_params)
        response = self._boto_client.create_job(**_request.to_boto())

        return shapes.CreateJobResult.from_boto(response)

    def describe_address(
        self,
        _request: shapes.DescribeAddressRequest = None,
        *,
        address_id: str,
    ) -> shapes.DescribeAddressResult:
        """
        Takes an `AddressId` and returns specific details about that address in the form
        of an `Address` object.
        """
        if _request is None:
            _params = {}
            if address_id is not ShapeBase.NOT_SET:
                _params['address_id'] = address_id
            _request = shapes.DescribeAddressRequest(**_params)
        response = self._boto_client.describe_address(**_request.to_boto())

        return shapes.DescribeAddressResult.from_boto(response)

    def describe_addresses(
        self,
        _request: shapes.DescribeAddressesRequest = None,
        *,
        max_results: int = ShapeBase.NOT_SET,
        next_token: str = ShapeBase.NOT_SET,
    ) -> shapes.DescribeAddressesResult:
        """
        Returns a specified number of `ADDRESS` objects. Calling this API in one of the
        US regions will return addresses from the list of all addresses associated with
        this account in all US regions.
        """
        if _request is None:
            _params = {}
            if max_results is not ShapeBase.NOT_SET:
                _params['max_results'] = max_results
            if next_token is not ShapeBase.NOT_SET:
                _params['next_token'] = next_token
            _request = shapes.DescribeAddressesRequest(**_params)
        paginator = self.get_paginator("describe_addresses").paginate(
            **_request.to_boto()
        )
        page_generator = (page for page in paginator)
        first_page = next(page_generator)
        result = shapes.DescribeAddressesResult.from_boto(first_page)
        result._page_iterator = page_generator
        return result

        return shapes.DescribeAddressesResult.from_boto(response)

    def describe_cluster(
        self,
        _request: shapes.DescribeClusterRequest = None,
        *,
        cluster_id: str,
    ) -> shapes.DescribeClusterResult:
        """
        Returns information about a specific cluster including shipping information,
        cluster status, and other important metadata.
        """
        if _request is None:
            _params = {}
            if cluster_id is not ShapeBase.NOT_SET:
                _params['cluster_id'] = cluster_id
            _request = shapes.DescribeClusterRequest(**_params)
        response = self._boto_client.describe_cluster(**_request.to_boto())

        return shapes.DescribeClusterResult.from_boto(response)

    def describe_job(
        self,
        _request: shapes.DescribeJobRequest = None,
        *,
        job_id: str,
    ) -> shapes.DescribeJobResult:
        """
        Returns information about a specific job including shipping information, job
        status, and other important metadata.
        """
        if _request is None:
            _params = {}
            if job_id is not ShapeBase.NOT_SET:
                _params['job_id'] = job_id
            _request = shapes.DescribeJobRequest(**_params)
        response = self._boto_client.describe_job(**_request.to_boto())

        return shapes.DescribeJobResult.from_boto(response)

    def get_job_manifest(
        self,
        _request: shapes.GetJobManifestRequest = None,
        *,
        job_id: str,
    ) -> shapes.GetJobManifestResult:
        """
        Returns a link to an Amazon S3 presigned URL for the manifest file associated
        with the specified `JobId` value. You can access the manifest file for up to 60
        minutes after this request has been made. To access the manifest file after 60
        minutes have passed, you'll have to make another call to the `GetJobManifest`
        action.

        The manifest is an encrypted file that you can download after your job enters
        the `WithCustomer` status. The manifest is decrypted by using the `UnlockCode`
        code value, when you pass both values to the Snowball through the Snowball
        client when the client is started for the first time.

        As a best practice, we recommend that you don't save a copy of an `UnlockCode`
        value in the same location as the manifest file for that job. Saving these
        separately helps prevent unauthorized parties from gaining access to the
        Snowball associated with that job.

        The credentials of a given job, including its manifest file and unlock code,
        expire 90 days after the job is created.
        """
        if _request is None:
            _params = {}
            if job_id is not ShapeBase.NOT_SET:
                _params['job_id'] = job_id
            _request = shapes.GetJobManifestRequest(**_params)
        response = self._boto_client.get_job_manifest(**_request.to_boto())

        return shapes.GetJobManifestResult.from_boto(response)

    def get_job_unlock_code(
        self,
        _request: shapes.GetJobUnlockCodeRequest = None,
        *,
        job_id: str,
    ) -> shapes.GetJobUnlockCodeResult:
        """
        Returns the `UnlockCode` code value for the specified job. A particular
        `UnlockCode` value can be accessed for up to 90 days after the associated job
        has been created.

        The `UnlockCode` value is a 29-character code with 25 alphanumeric characters
        and 4 hyphens. This code is used to decrypt the manifest file when it is passed
        along with the manifest to the Snowball through the Snowball client when the
        client is started for the first time.

        As a best practice, we recommend that you don't save a copy of the `UnlockCode`
        in the same location as the manifest file for that job. Saving these separately
        helps prevent unauthorized parties from gaining access to the Snowball
        associated with that job.
        """
        if _request is None:
            _params = {}
            if job_id is not ShapeBase.NOT_SET:
                _params['job_id'] = job_id
            _request = shapes.GetJobUnlockCodeRequest(**_params)
        response = self._boto_client.get_job_unlock_code(**_request.to_boto())

        return shapes.GetJobUnlockCodeResult.from_boto(response)

    def get_snowball_usage(
        self,
        _request: shapes.GetSnowballUsageRequest = None,
    ) -> shapes.GetSnowballUsageResult:
        """
        Returns information about the Snowball service limit for your account, and also
        the number of Snowballs your account has in use.

        The default service limit for the number of Snowballs that you can have at one
        time is 1. If you want to increase your service limit, contact AWS Support.
        """
        if _request is None:
            _params = {}
            _request = shapes.GetSnowballUsageRequest(**_params)
        response = self._boto_client.get_snowball_usage(**_request.to_boto())

        return shapes.GetSnowballUsageResult.from_boto(response)

    def list_cluster_jobs(
        self,
        _request: shapes.ListClusterJobsRequest = None,
        *,
        cluster_id: str,
        max_results: int = ShapeBase.NOT_SET,
        next_token: str = ShapeBase.NOT_SET,
    ) -> shapes.ListClusterJobsResult:
        """
        Returns an array of `JobListEntry` objects of the specified length. Each
        `JobListEntry` object is for a job in the specified cluster and contains a job's
        state, a job's ID, and other information.
        """
        if _request is None:
            _params = {}
            if cluster_id is not ShapeBase.NOT_SET:
                _params['cluster_id'] = cluster_id
            if max_results is not ShapeBase.NOT_SET:
                _params['max_results'] = max_results
            if next_token is not ShapeBase.NOT_SET:
                _params['next_token'] = next_token
            _request = shapes.ListClusterJobsRequest(**_params)
        response = self._boto_client.list_cluster_jobs(**_request.to_boto())

        return shapes.ListClusterJobsResult.from_boto(response)

    def list_clusters(
        self,
        _request: shapes.ListClustersRequest = None,
        *,
        max_results: int = ShapeBase.NOT_SET,
        next_token: str = ShapeBase.NOT_SET,
    ) -> shapes.ListClustersResult:
        """
        Returns an array of `ClusterListEntry` objects of the specified length. Each
        `ClusterListEntry` object contains a cluster's state, a cluster's ID, and other
        important status information.
        """
        if _request is None:
            _params = {}
            if max_results is not ShapeBase.NOT_SET:
                _params['max_results'] = max_results
            if next_token is not ShapeBase.NOT_SET:
                _params['next_token'] = next_token
            _request = shapes.ListClustersRequest(**_params)
        response = self._boto_client.list_clusters(**_request.to_boto())

        return shapes.ListClustersResult.from_boto(response)

    def list_compatible_images(
        self,
        _request: shapes.ListCompatibleImagesRequest = None,
        *,
        max_results: int = ShapeBase.NOT_SET,
        next_token: str = ShapeBase.NOT_SET,
    ) -> shapes.ListCompatibleImagesResult:
        """
        This action returns a list of the different Amazon EC2 Amazon Machine Images
        (AMIs) that are owned by your AWS account that would be supported for use on a
        Snowball Edge device. Currently, supported AMIs are based on the CentOS 7
        (x86_64) - with Updates HVM, Ubuntu Server 14.04 LTS (HVM), and Ubuntu 16.04 LTS
        - Xenial (HVM) images, available on the AWS Marketplace.
        """
        if _request is None:
            _params = {}
            if max_results is not ShapeBase.NOT_SET:
                _params['max_results'] = max_results
            if next_token is not ShapeBase.NOT_SET:
                _params['next_token'] = next_token
            _request = shapes.ListCompatibleImagesRequest(**_params)
        response = self._boto_client.list_compatible_images(
            **_request.to_boto()
        )

        return shapes.ListCompatibleImagesResult.from_boto(response)

    def list_jobs(
        self,
        _request: shapes.ListJobsRequest = None,
        *,
        max_results: int = ShapeBase.NOT_SET,
        next_token: str = ShapeBase.NOT_SET,
    ) -> shapes.ListJobsResult:
        """
        Returns an array of `JobListEntry` objects of the specified length. Each
        `JobListEntry` object contains a job's state, a job's ID, and a value that
        indicates whether the job is a job part, in the case of export jobs. Calling
        this API action in one of the US regions will return jobs from the list of all
        jobs associated with this account in all US regions.
        """
        if _request is None:
            _params = {}
            if max_results is not ShapeBase.NOT_SET:
                _params['max_results'] = max_results
            if next_token is not ShapeBase.NOT_SET:
                _params['next_token'] = next_token
            _request = shapes.ListJobsRequest(**_params)
        paginator = self.get_paginator("list_jobs").paginate(
            **_request.to_boto()
        )
        page_generator = (page for page in paginator)
        first_page = next(page_generator)
        result = shapes.ListJobsResult.from_boto(first_page)
        result._page_iterator = page_generator
        return result

        return shapes.ListJobsResult.from_boto(response)

    def update_cluster(
        self,
        _request: shapes.UpdateClusterRequest = None,
        *,
        cluster_id: str,
        role_arn: str = ShapeBase.NOT_SET,
        description: str = ShapeBase.NOT_SET,
        resources: shapes.JobResource = ShapeBase.NOT_SET,
        address_id: str = ShapeBase.NOT_SET,
        shipping_option: typing.Union[str, shapes.ShippingOption] = ShapeBase.
        NOT_SET,
        notification: shapes.Notification = ShapeBase.NOT_SET,
        forwarding_address_id: str = ShapeBase.NOT_SET,
    ) -> shapes.UpdateClusterResult:
        """
        While a cluster's `ClusterState` value is in the `AwaitingQuorum` state, you can
        update some of the information associated with a cluster. Once the cluster
        changes to a different job state, usually 60 minutes after the cluster being
        created, this action is no longer available.
        """
        if _request is None:
            _params = {}
            if cluster_id is not ShapeBase.NOT_SET:
                _params['cluster_id'] = cluster_id
            if role_arn is not ShapeBase.NOT_SET:
                _params['role_arn'] = role_arn
            if description is not ShapeBase.NOT_SET:
                _params['description'] = description
            if resources is not ShapeBase.NOT_SET:
                _params['resources'] = resources
            if address_id is not ShapeBase.NOT_SET:
                _params['address_id'] = address_id
            if shipping_option is not ShapeBase.NOT_SET:
                _params['shipping_option'] = shipping_option
            if notification is not ShapeBase.NOT_SET:
                _params['notification'] = notification
            if forwarding_address_id is not ShapeBase.NOT_SET:
                _params['forwarding_address_id'] = forwarding_address_id
            _request = shapes.UpdateClusterRequest(**_params)
        response = self._boto_client.update_cluster(**_request.to_boto())

        return shapes.UpdateClusterResult.from_boto(response)

    def update_job(
        self,
        _request: shapes.UpdateJobRequest = None,
        *,
        job_id: str,
        role_arn: str = ShapeBase.NOT_SET,
        notification: shapes.Notification = ShapeBase.NOT_SET,
        resources: shapes.JobResource = ShapeBase.NOT_SET,
        address_id: str = ShapeBase.NOT_SET,
        shipping_option: typing.Union[str, shapes.
                                      ShippingOption] = ShapeBase.NOT_SET,
        description: str = ShapeBase.NOT_SET,
        snowball_capacity_preference: typing.
        Union[str, shapes.SnowballCapacity] = ShapeBase.NOT_SET,
        forwarding_address_id: str = ShapeBase.NOT_SET,
    ) -> shapes.UpdateJobResult:
        """
        While a job's `JobState` value is `New`, you can update some of the information
        associated with a job. Once the job changes to a different job state, usually
        within 60 minutes of the job being created, this action is no longer available.
        """
        if _request is None:
            _params = {}
            if job_id is not ShapeBase.NOT_SET:
                _params['job_id'] = job_id
            if role_arn is not ShapeBase.NOT_SET:
                _params['role_arn'] = role_arn
            if notification is not ShapeBase.NOT_SET:
                _params['notification'] = notification
            if resources is not ShapeBase.NOT_SET:
                _params['resources'] = resources
            if address_id is not ShapeBase.NOT_SET:
                _params['address_id'] = address_id
            if shipping_option is not ShapeBase.NOT_SET:
                _params['shipping_option'] = shipping_option
            if description is not ShapeBase.NOT_SET:
                _params['description'] = description
            if snowball_capacity_preference is not ShapeBase.NOT_SET:
                _params['snowball_capacity_preference'
                       ] = snowball_capacity_preference
            if forwarding_address_id is not ShapeBase.NOT_SET:
                _params['forwarding_address_id'] = forwarding_address_id
            _request = shapes.UpdateJobRequest(**_params)
        response = self._boto_client.update_job(**_request.to_boto())

        return shapes.UpdateJobResult.from_boto(response)
