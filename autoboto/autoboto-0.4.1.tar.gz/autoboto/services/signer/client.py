import datetime
import typing
import boto3
from autoboto import ClientBase, ShapeBase, OutputShapeBase
from . import shapes


class Client(ClientBase):
    def __init__(self, *args, **kwargs):
        super().__init__("signer", *args, **kwargs)

    def cancel_signing_profile(
        self,
        _request: shapes.CancelSigningProfileRequest = None,
        *,
        profile_name: str,
    ) -> None:
        """
        Changes the state of an `ACTIVE` signing profile to `CANCELED`. A canceled
        profile is still viewable with the `ListSigningProfiles` operation, but it
        cannot perform new signing jobs, and is deleted two years after cancelation.
        """
        if _request is None:
            _params = {}
            if profile_name is not ShapeBase.NOT_SET:
                _params['profile_name'] = profile_name
            _request = shapes.CancelSigningProfileRequest(**_params)
        response = self._boto_client.cancel_signing_profile(
            **_request.to_boto()
        )

    def describe_signing_job(
        self,
        _request: shapes.DescribeSigningJobRequest = None,
        *,
        job_id: str,
    ) -> shapes.DescribeSigningJobResponse:
        """
        Returns information about a specific code signing job. You specify the job by
        using the `jobId` value that is returned by the StartSigningJob operation.
        """
        if _request is None:
            _params = {}
            if job_id is not ShapeBase.NOT_SET:
                _params['job_id'] = job_id
            _request = shapes.DescribeSigningJobRequest(**_params)
        response = self._boto_client.describe_signing_job(**_request.to_boto())

        return shapes.DescribeSigningJobResponse.from_boto(response)

    def get_signing_platform(
        self,
        _request: shapes.GetSigningPlatformRequest = None,
        *,
        platform_id: str,
    ) -> shapes.GetSigningPlatformResponse:
        """
        Returns information on a specific signing platform.
        """
        if _request is None:
            _params = {}
            if platform_id is not ShapeBase.NOT_SET:
                _params['platform_id'] = platform_id
            _request = shapes.GetSigningPlatformRequest(**_params)
        response = self._boto_client.get_signing_platform(**_request.to_boto())

        return shapes.GetSigningPlatformResponse.from_boto(response)

    def get_signing_profile(
        self,
        _request: shapes.GetSigningProfileRequest = None,
        *,
        profile_name: str,
    ) -> shapes.GetSigningProfileResponse:
        """
        Returns information on a specific signing profile.
        """
        if _request is None:
            _params = {}
            if profile_name is not ShapeBase.NOT_SET:
                _params['profile_name'] = profile_name
            _request = shapes.GetSigningProfileRequest(**_params)
        response = self._boto_client.get_signing_profile(**_request.to_boto())

        return shapes.GetSigningProfileResponse.from_boto(response)

    def list_signing_jobs(
        self,
        _request: shapes.ListSigningJobsRequest = None,
        *,
        status: typing.Union[str, shapes.SigningStatus] = ShapeBase.NOT_SET,
        platform_id: str = ShapeBase.NOT_SET,
        requested_by: str = ShapeBase.NOT_SET,
        max_results: int = ShapeBase.NOT_SET,
        next_token: str = ShapeBase.NOT_SET,
    ) -> shapes.ListSigningJobsResponse:
        """
        Lists all your signing jobs. You can use the `maxResults` parameter to limit the
        number of signing jobs that are returned in the response. If additional jobs
        remain to be listed, AWS Signer returns a `nextToken` value. Use this value in
        subsequent calls to `ListSigningJobs` to fetch the remaining values. You can
        continue calling `ListSigningJobs` with your `maxResults` parameter and with new
        values that AWS Signer returns in the `nextToken` parameter until all of your
        signing jobs have been returned.
        """
        if _request is None:
            _params = {}
            if status is not ShapeBase.NOT_SET:
                _params['status'] = status
            if platform_id is not ShapeBase.NOT_SET:
                _params['platform_id'] = platform_id
            if requested_by is not ShapeBase.NOT_SET:
                _params['requested_by'] = requested_by
            if max_results is not ShapeBase.NOT_SET:
                _params['max_results'] = max_results
            if next_token is not ShapeBase.NOT_SET:
                _params['next_token'] = next_token
            _request = shapes.ListSigningJobsRequest(**_params)
        response = self._boto_client.list_signing_jobs(**_request.to_boto())

        return shapes.ListSigningJobsResponse.from_boto(response)

    def list_signing_platforms(
        self,
        _request: shapes.ListSigningPlatformsRequest = None,
        *,
        category: str = ShapeBase.NOT_SET,
        partner: str = ShapeBase.NOT_SET,
        target: str = ShapeBase.NOT_SET,
        max_results: int = ShapeBase.NOT_SET,
        next_token: str = ShapeBase.NOT_SET,
    ) -> shapes.ListSigningPlatformsResponse:
        """
        Lists all signing platforms available in AWS Signer that match the request
        parameters. If additional jobs remain to be listed, AWS Signer returns a
        `nextToken` value. Use this value in subsequent calls to `ListSigningJobs` to
        fetch the remaining values. You can continue calling `ListSigningJobs` with your
        `maxResults` parameter and with new values that AWS Signer returns in the
        `nextToken` parameter until all of your signing jobs have been returned.
        """
        if _request is None:
            _params = {}
            if category is not ShapeBase.NOT_SET:
                _params['category'] = category
            if partner is not ShapeBase.NOT_SET:
                _params['partner'] = partner
            if target is not ShapeBase.NOT_SET:
                _params['target'] = target
            if max_results is not ShapeBase.NOT_SET:
                _params['max_results'] = max_results
            if next_token is not ShapeBase.NOT_SET:
                _params['next_token'] = next_token
            _request = shapes.ListSigningPlatformsRequest(**_params)
        response = self._boto_client.list_signing_platforms(
            **_request.to_boto()
        )

        return shapes.ListSigningPlatformsResponse.from_boto(response)

    def list_signing_profiles(
        self,
        _request: shapes.ListSigningProfilesRequest = None,
        *,
        include_canceled: bool = ShapeBase.NOT_SET,
        max_results: int = ShapeBase.NOT_SET,
        next_token: str = ShapeBase.NOT_SET,
    ) -> shapes.ListSigningProfilesResponse:
        """
        Lists all available signing profiles in your AWS account. Returns only profiles
        with an `ACTIVE` status unless the `includeCanceled` request field is set to
        `true`. If additional jobs remain to be listed, AWS Signer returns a `nextToken`
        value. Use this value in subsequent calls to `ListSigningJobs` to fetch the
        remaining values. You can continue calling `ListSigningJobs` with your
        `maxResults` parameter and with new values that AWS Signer returns in the
        `nextToken` parameter until all of your signing jobs have been returned.
        """
        if _request is None:
            _params = {}
            if include_canceled is not ShapeBase.NOT_SET:
                _params['include_canceled'] = include_canceled
            if max_results is not ShapeBase.NOT_SET:
                _params['max_results'] = max_results
            if next_token is not ShapeBase.NOT_SET:
                _params['next_token'] = next_token
            _request = shapes.ListSigningProfilesRequest(**_params)
        response = self._boto_client.list_signing_profiles(**_request.to_boto())

        return shapes.ListSigningProfilesResponse.from_boto(response)

    def put_signing_profile(
        self,
        _request: shapes.PutSigningProfileRequest = None,
        *,
        profile_name: str,
        signing_material: shapes.SigningMaterial,
        platform_id: str,
        overrides: shapes.SigningPlatformOverrides = ShapeBase.NOT_SET,
        signing_parameters: typing.Dict[str, str] = ShapeBase.NOT_SET,
    ) -> shapes.PutSigningProfileResponse:
        """
        Creates a signing profile. A signing profile is an AWS Signer template that can
        be used to carry out a pre-defined signing job. For more information, see
        <http://docs.aws.amazon.com/signer/latest/developerguide/gs-profile.html>
        """
        if _request is None:
            _params = {}
            if profile_name is not ShapeBase.NOT_SET:
                _params['profile_name'] = profile_name
            if signing_material is not ShapeBase.NOT_SET:
                _params['signing_material'] = signing_material
            if platform_id is not ShapeBase.NOT_SET:
                _params['platform_id'] = platform_id
            if overrides is not ShapeBase.NOT_SET:
                _params['overrides'] = overrides
            if signing_parameters is not ShapeBase.NOT_SET:
                _params['signing_parameters'] = signing_parameters
            _request = shapes.PutSigningProfileRequest(**_params)
        response = self._boto_client.put_signing_profile(**_request.to_boto())

        return shapes.PutSigningProfileResponse.from_boto(response)

    def start_signing_job(
        self,
        _request: shapes.StartSigningJobRequest = None,
        *,
        source: shapes.Source,
        destination: shapes.Destination,
        client_request_token: str,
        profile_name: str = ShapeBase.NOT_SET,
    ) -> shapes.StartSigningJobResponse:
        """
        Initiates a signing job to be performed on the code provided. Signing jobs are
        viewable by the `ListSigningJobs` operation for two years after they are
        performed. Note the following requirements:

          * You must create an Amazon S3 source bucket. For more information, see [Create a Bucket](http://docs.aws.amazon.com/AmazonS3/latest/gsg/CreatingABucket.html) in the _Amazon S3 Getting Started Guide_. 

          * Your S3 source bucket must be version enabled.

          * You must create an S3 destination bucket. AWS Signer uses your S3 destination bucket to write your signed code.

          * You specify the name of the source and destination buckets when calling the `StartSigningJob` operation.

          * You must also specify a request token that identifies your request to AWS Signer. 

        You can call the DescribeSigningJob and the ListSigningJobs actions after you
        call `StartSigningJob`.

        For a Java example that shows how to use this action, see
        <http://docs.aws.amazon.com/acm/latest/userguide/>
        """
        if _request is None:
            _params = {}
            if source is not ShapeBase.NOT_SET:
                _params['source'] = source
            if destination is not ShapeBase.NOT_SET:
                _params['destination'] = destination
            if client_request_token is not ShapeBase.NOT_SET:
                _params['client_request_token'] = client_request_token
            if profile_name is not ShapeBase.NOT_SET:
                _params['profile_name'] = profile_name
            _request = shapes.StartSigningJobRequest(**_params)
        response = self._boto_client.start_signing_job(**_request.to_boto())

        return shapes.StartSigningJobResponse.from_boto(response)
