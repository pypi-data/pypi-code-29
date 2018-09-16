import datetime
import typing
import boto3
from autoboto import ClientBase, ShapeBase, OutputShapeBase
from . import shapes


class Client(ClientBase):
    def __init__(self, *args, **kwargs):
        super().__init__("cloudfront", *args, **kwargs)

    def create_cloud_front_origin_access_identity(
        self,
        _request: shapes.CreateCloudFrontOriginAccessIdentityRequest = None,
        *,
        cloud_front_origin_access_identity_config: shapes.
        CloudFrontOriginAccessIdentityConfig,
    ) -> shapes.CreateCloudFrontOriginAccessIdentityResult:
        """
        Creates a new origin access identity. If you're using Amazon S3 for your origin,
        you can use an origin access identity to require users to access your content
        using a CloudFront URL instead of the Amazon S3 URL. For more information about
        how to use origin access identities, see [Serving Private Content through
        CloudFront](http://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/PrivateContent.html)
        in the _Amazon CloudFront Developer Guide_.
        """
        if _request is None:
            _params = {}
            if cloud_front_origin_access_identity_config is not ShapeBase.NOT_SET:
                _params['cloud_front_origin_access_identity_config'
                       ] = cloud_front_origin_access_identity_config
            _request = shapes.CreateCloudFrontOriginAccessIdentityRequest(
                **_params
            )
        response = self._boto_client.create_cloud_front_origin_access_identity(
            **_request.to_boto()
        )

        return shapes.CreateCloudFrontOriginAccessIdentityResult.from_boto(
            response
        )

    def create_distribution(
        self,
        _request: shapes.CreateDistributionRequest = None,
        *,
        distribution_config: shapes.DistributionConfig,
    ) -> shapes.CreateDistributionResult:
        """
        Creates a new web distribution. Send a `POST` request to the `/ _CloudFront API
        version_ /distribution`/`distribution ID` resource.
        """
        if _request is None:
            _params = {}
            if distribution_config is not ShapeBase.NOT_SET:
                _params['distribution_config'] = distribution_config
            _request = shapes.CreateDistributionRequest(**_params)
        response = self._boto_client.create_distribution(**_request.to_boto())

        return shapes.CreateDistributionResult.from_boto(response)

    def create_distribution_with_tags(
        self,
        _request: shapes.CreateDistributionWithTagsRequest = None,
        *,
        distribution_config_with_tags: shapes.DistributionConfigWithTags,
    ) -> shapes.CreateDistributionWithTagsResult:
        """
        Create a new distribution with tags.
        """
        if _request is None:
            _params = {}
            if distribution_config_with_tags is not ShapeBase.NOT_SET:
                _params['distribution_config_with_tags'
                       ] = distribution_config_with_tags
            _request = shapes.CreateDistributionWithTagsRequest(**_params)
        response = self._boto_client.create_distribution_with_tags(
            **_request.to_boto()
        )

        return shapes.CreateDistributionWithTagsResult.from_boto(response)

    def create_field_level_encryption_config(
        self,
        _request: shapes.CreateFieldLevelEncryptionConfigRequest = None,
        *,
        field_level_encryption_config: shapes.FieldLevelEncryptionConfig,
    ) -> shapes.CreateFieldLevelEncryptionConfigResult:
        """
        Create a new field-level encryption configuration.
        """
        if _request is None:
            _params = {}
            if field_level_encryption_config is not ShapeBase.NOT_SET:
                _params['field_level_encryption_config'
                       ] = field_level_encryption_config
            _request = shapes.CreateFieldLevelEncryptionConfigRequest(**_params)
        response = self._boto_client.create_field_level_encryption_config(
            **_request.to_boto()
        )

        return shapes.CreateFieldLevelEncryptionConfigResult.from_boto(response)

    def create_field_level_encryption_profile(
        self,
        _request: shapes.CreateFieldLevelEncryptionProfileRequest = None,
        *,
        field_level_encryption_profile_config: shapes.
        FieldLevelEncryptionProfileConfig,
    ) -> shapes.CreateFieldLevelEncryptionProfileResult:
        """
        Create a field-level encryption profile.
        """
        if _request is None:
            _params = {}
            if field_level_encryption_profile_config is not ShapeBase.NOT_SET:
                _params['field_level_encryption_profile_config'
                       ] = field_level_encryption_profile_config
            _request = shapes.CreateFieldLevelEncryptionProfileRequest(
                **_params
            )
        response = self._boto_client.create_field_level_encryption_profile(
            **_request.to_boto()
        )

        return shapes.CreateFieldLevelEncryptionProfileResult.from_boto(
            response
        )

    def create_invalidation(
        self,
        _request: shapes.CreateInvalidationRequest = None,
        *,
        distribution_id: str,
        invalidation_batch: shapes.InvalidationBatch,
    ) -> shapes.CreateInvalidationResult:
        """
        Create a new invalidation.
        """
        if _request is None:
            _params = {}
            if distribution_id is not ShapeBase.NOT_SET:
                _params['distribution_id'] = distribution_id
            if invalidation_batch is not ShapeBase.NOT_SET:
                _params['invalidation_batch'] = invalidation_batch
            _request = shapes.CreateInvalidationRequest(**_params)
        response = self._boto_client.create_invalidation(**_request.to_boto())

        return shapes.CreateInvalidationResult.from_boto(response)

    def create_public_key(
        self,
        _request: shapes.CreatePublicKeyRequest = None,
        *,
        public_key_config: shapes.PublicKeyConfig,
    ) -> shapes.CreatePublicKeyResult:
        """
        Add a new public key to CloudFront to use, for example, for field-level
        encryption. You can add a maximum of 10 public keys with one AWS account.
        """
        if _request is None:
            _params = {}
            if public_key_config is not ShapeBase.NOT_SET:
                _params['public_key_config'] = public_key_config
            _request = shapes.CreatePublicKeyRequest(**_params)
        response = self._boto_client.create_public_key(**_request.to_boto())

        return shapes.CreatePublicKeyResult.from_boto(response)

    def create_streaming_distribution(
        self,
        _request: shapes.CreateStreamingDistributionRequest = None,
        *,
        streaming_distribution_config: shapes.StreamingDistributionConfig,
    ) -> shapes.CreateStreamingDistributionResult:
        """
        Creates a new RMTP distribution. An RTMP distribution is similar to a web
        distribution, but an RTMP distribution streams media files using the Adobe Real-
        Time Messaging Protocol (RTMP) instead of serving files using HTTP.

        To create a new web distribution, submit a `POST` request to the _CloudFront API
        version_ /distribution resource. The request body must include a document with a
        _StreamingDistributionConfig_ element. The response echoes the
        `StreamingDistributionConfig` element and returns other information about the
        RTMP distribution.

        To get the status of your request, use the _GET StreamingDistribution_ API
        action. When the value of `Enabled` is `true` and the value of `Status` is
        `Deployed`, your distribution is ready. A distribution usually deploys in less
        than 15 minutes.

        For more information about web distributions, see [Working with RTMP
        Distributions](http://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/distribution-
        rtmp.html) in the _Amazon CloudFront Developer Guide_.

        Beginning with the 2012-05-05 version of the CloudFront API, we made substantial
        changes to the format of the XML document that you include in the request body
        when you create or update a web distribution or an RTMP distribution, and when
        you invalidate objects. With previous versions of the API, we discovered that it
        was too easy to accidentally delete one or more values for an element that
        accepts multiple values, for example, CNAMEs and trusted signers. Our changes
        for the 2012-05-05 release are intended to prevent these accidental deletions
        and to notify you when there's a mismatch between the number of values you say
        you're specifying in the `Quantity` element and the number of values specified.
        """
        if _request is None:
            _params = {}
            if streaming_distribution_config is not ShapeBase.NOT_SET:
                _params['streaming_distribution_config'
                       ] = streaming_distribution_config
            _request = shapes.CreateStreamingDistributionRequest(**_params)
        response = self._boto_client.create_streaming_distribution(
            **_request.to_boto()
        )

        return shapes.CreateStreamingDistributionResult.from_boto(response)

    def create_streaming_distribution_with_tags(
        self,
        _request: shapes.CreateStreamingDistributionWithTagsRequest = None,
        *,
        streaming_distribution_config_with_tags: shapes.
        StreamingDistributionConfigWithTags,
    ) -> shapes.CreateStreamingDistributionWithTagsResult:
        """
        Create a new streaming distribution with tags.
        """
        if _request is None:
            _params = {}
            if streaming_distribution_config_with_tags is not ShapeBase.NOT_SET:
                _params['streaming_distribution_config_with_tags'
                       ] = streaming_distribution_config_with_tags
            _request = shapes.CreateStreamingDistributionWithTagsRequest(
                **_params
            )
        response = self._boto_client.create_streaming_distribution_with_tags(
            **_request.to_boto()
        )

        return shapes.CreateStreamingDistributionWithTagsResult.from_boto(
            response
        )

    def delete_cloud_front_origin_access_identity(
        self,
        _request: shapes.DeleteCloudFrontOriginAccessIdentityRequest = None,
        *,
        id: str,
        if_match: str = ShapeBase.NOT_SET,
    ) -> None:
        """
        Delete an origin access identity.
        """
        if _request is None:
            _params = {}
            if id is not ShapeBase.NOT_SET:
                _params['id'] = id
            if if_match is not ShapeBase.NOT_SET:
                _params['if_match'] = if_match
            _request = shapes.DeleteCloudFrontOriginAccessIdentityRequest(
                **_params
            )
        response = self._boto_client.delete_cloud_front_origin_access_identity(
            **_request.to_boto()
        )

    def delete_distribution(
        self,
        _request: shapes.DeleteDistributionRequest = None,
        *,
        id: str,
        if_match: str = ShapeBase.NOT_SET,
    ) -> None:
        """
        Delete a distribution.
        """
        if _request is None:
            _params = {}
            if id is not ShapeBase.NOT_SET:
                _params['id'] = id
            if if_match is not ShapeBase.NOT_SET:
                _params['if_match'] = if_match
            _request = shapes.DeleteDistributionRequest(**_params)
        response = self._boto_client.delete_distribution(**_request.to_boto())

    def delete_field_level_encryption_config(
        self,
        _request: shapes.DeleteFieldLevelEncryptionConfigRequest = None,
        *,
        id: str,
        if_match: str = ShapeBase.NOT_SET,
    ) -> None:
        """
        Remove a field-level encryption configuration.
        """
        if _request is None:
            _params = {}
            if id is not ShapeBase.NOT_SET:
                _params['id'] = id
            if if_match is not ShapeBase.NOT_SET:
                _params['if_match'] = if_match
            _request = shapes.DeleteFieldLevelEncryptionConfigRequest(**_params)
        response = self._boto_client.delete_field_level_encryption_config(
            **_request.to_boto()
        )

    def delete_field_level_encryption_profile(
        self,
        _request: shapes.DeleteFieldLevelEncryptionProfileRequest = None,
        *,
        id: str,
        if_match: str = ShapeBase.NOT_SET,
    ) -> None:
        """
        Remove a field-level encryption profile.
        """
        if _request is None:
            _params = {}
            if id is not ShapeBase.NOT_SET:
                _params['id'] = id
            if if_match is not ShapeBase.NOT_SET:
                _params['if_match'] = if_match
            _request = shapes.DeleteFieldLevelEncryptionProfileRequest(
                **_params
            )
        response = self._boto_client.delete_field_level_encryption_profile(
            **_request.to_boto()
        )

    def delete_public_key(
        self,
        _request: shapes.DeletePublicKeyRequest = None,
        *,
        id: str,
        if_match: str = ShapeBase.NOT_SET,
    ) -> None:
        """
        Remove a public key you previously added to CloudFront.
        """
        if _request is None:
            _params = {}
            if id is not ShapeBase.NOT_SET:
                _params['id'] = id
            if if_match is not ShapeBase.NOT_SET:
                _params['if_match'] = if_match
            _request = shapes.DeletePublicKeyRequest(**_params)
        response = self._boto_client.delete_public_key(**_request.to_boto())

    def delete_streaming_distribution(
        self,
        _request: shapes.DeleteStreamingDistributionRequest = None,
        *,
        id: str,
        if_match: str = ShapeBase.NOT_SET,
    ) -> None:
        """
        Delete a streaming distribution. To delete an RTMP distribution using the
        CloudFront API, perform the following steps.

        **To delete an RTMP distribution using the CloudFront API** :

          1. Disable the RTMP distribution.

          2. Submit a `GET Streaming Distribution Config` request to get the current configuration and the `Etag` header for the distribution. 

          3. Update the XML document that was returned in the response to your `GET Streaming Distribution Config` request to change the value of `Enabled` to `false`.

          4. Submit a `PUT Streaming Distribution Config` request to update the configuration for your distribution. In the request body, include the XML document that you updated in Step 3. Then set the value of the HTTP `If-Match` header to the value of the `ETag` header that CloudFront returned when you submitted the `GET Streaming Distribution Config` request in Step 2.

          5. Review the response to the `PUT Streaming Distribution Config` request to confirm that the distribution was successfully disabled.

          6. Submit a `GET Streaming Distribution Config` request to confirm that your changes have propagated. When propagation is complete, the value of `Status` is `Deployed`.

          7. Submit a `DELETE Streaming Distribution` request. Set the value of the HTTP `If-Match` header to the value of the `ETag` header that CloudFront returned when you submitted the `GET Streaming Distribution Config` request in Step 2.

          8. Review the response to your `DELETE Streaming Distribution` request to confirm that the distribution was successfully deleted.

        For information about deleting a distribution using the CloudFront console, see
        [Deleting a
        Distribution](http://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/HowToDeleteDistribution.html)
        in the _Amazon CloudFront Developer Guide_.
        """
        if _request is None:
            _params = {}
            if id is not ShapeBase.NOT_SET:
                _params['id'] = id
            if if_match is not ShapeBase.NOT_SET:
                _params['if_match'] = if_match
            _request = shapes.DeleteStreamingDistributionRequest(**_params)
        response = self._boto_client.delete_streaming_distribution(
            **_request.to_boto()
        )

    def get_cloud_front_origin_access_identity(
        self,
        _request: shapes.GetCloudFrontOriginAccessIdentityRequest = None,
        *,
        id: str,
    ) -> shapes.GetCloudFrontOriginAccessIdentityResult:
        """
        Get the information about an origin access identity.
        """
        if _request is None:
            _params = {}
            if id is not ShapeBase.NOT_SET:
                _params['id'] = id
            _request = shapes.GetCloudFrontOriginAccessIdentityRequest(
                **_params
            )
        response = self._boto_client.get_cloud_front_origin_access_identity(
            **_request.to_boto()
        )

        return shapes.GetCloudFrontOriginAccessIdentityResult.from_boto(
            response
        )

    def get_cloud_front_origin_access_identity_config(
        self,
        _request: shapes.GetCloudFrontOriginAccessIdentityConfigRequest = None,
        *,
        id: str,
    ) -> shapes.GetCloudFrontOriginAccessIdentityConfigResult:
        """
        Get the configuration information about an origin access identity.
        """
        if _request is None:
            _params = {}
            if id is not ShapeBase.NOT_SET:
                _params['id'] = id
            _request = shapes.GetCloudFrontOriginAccessIdentityConfigRequest(
                **_params
            )
        response = self._boto_client.get_cloud_front_origin_access_identity_config(
            **_request.to_boto()
        )

        return shapes.GetCloudFrontOriginAccessIdentityConfigResult.from_boto(
            response
        )

    def get_distribution(
        self,
        _request: shapes.GetDistributionRequest = None,
        *,
        id: str,
    ) -> shapes.GetDistributionResult:
        """
        Get the information about a distribution.
        """
        if _request is None:
            _params = {}
            if id is not ShapeBase.NOT_SET:
                _params['id'] = id
            _request = shapes.GetDistributionRequest(**_params)
        response = self._boto_client.get_distribution(**_request.to_boto())

        return shapes.GetDistributionResult.from_boto(response)

    def get_distribution_config(
        self,
        _request: shapes.GetDistributionConfigRequest = None,
        *,
        id: str,
    ) -> shapes.GetDistributionConfigResult:
        """
        Get the configuration information about a distribution.
        """
        if _request is None:
            _params = {}
            if id is not ShapeBase.NOT_SET:
                _params['id'] = id
            _request = shapes.GetDistributionConfigRequest(**_params)
        response = self._boto_client.get_distribution_config(
            **_request.to_boto()
        )

        return shapes.GetDistributionConfigResult.from_boto(response)

    def get_field_level_encryption(
        self,
        _request: shapes.GetFieldLevelEncryptionRequest = None,
        *,
        id: str,
    ) -> shapes.GetFieldLevelEncryptionResult:
        """
        Get the field-level encryption configuration information.
        """
        if _request is None:
            _params = {}
            if id is not ShapeBase.NOT_SET:
                _params['id'] = id
            _request = shapes.GetFieldLevelEncryptionRequest(**_params)
        response = self._boto_client.get_field_level_encryption(
            **_request.to_boto()
        )

        return shapes.GetFieldLevelEncryptionResult.from_boto(response)

    def get_field_level_encryption_config(
        self,
        _request: shapes.GetFieldLevelEncryptionConfigRequest = None,
        *,
        id: str,
    ) -> shapes.GetFieldLevelEncryptionConfigResult:
        """
        Get the field-level encryption configuration information.
        """
        if _request is None:
            _params = {}
            if id is not ShapeBase.NOT_SET:
                _params['id'] = id
            _request = shapes.GetFieldLevelEncryptionConfigRequest(**_params)
        response = self._boto_client.get_field_level_encryption_config(
            **_request.to_boto()
        )

        return shapes.GetFieldLevelEncryptionConfigResult.from_boto(response)

    def get_field_level_encryption_profile(
        self,
        _request: shapes.GetFieldLevelEncryptionProfileRequest = None,
        *,
        id: str,
    ) -> shapes.GetFieldLevelEncryptionProfileResult:
        """
        Get the field-level encryption profile information.
        """
        if _request is None:
            _params = {}
            if id is not ShapeBase.NOT_SET:
                _params['id'] = id
            _request = shapes.GetFieldLevelEncryptionProfileRequest(**_params)
        response = self._boto_client.get_field_level_encryption_profile(
            **_request.to_boto()
        )

        return shapes.GetFieldLevelEncryptionProfileResult.from_boto(response)

    def get_field_level_encryption_profile_config(
        self,
        _request: shapes.GetFieldLevelEncryptionProfileConfigRequest = None,
        *,
        id: str,
    ) -> shapes.GetFieldLevelEncryptionProfileConfigResult:
        """
        Get the field-level encryption profile configuration information.
        """
        if _request is None:
            _params = {}
            if id is not ShapeBase.NOT_SET:
                _params['id'] = id
            _request = shapes.GetFieldLevelEncryptionProfileConfigRequest(
                **_params
            )
        response = self._boto_client.get_field_level_encryption_profile_config(
            **_request.to_boto()
        )

        return shapes.GetFieldLevelEncryptionProfileConfigResult.from_boto(
            response
        )

    def get_invalidation(
        self,
        _request: shapes.GetInvalidationRequest = None,
        *,
        distribution_id: str,
        id: str,
    ) -> shapes.GetInvalidationResult:
        """
        Get the information about an invalidation.
        """
        if _request is None:
            _params = {}
            if distribution_id is not ShapeBase.NOT_SET:
                _params['distribution_id'] = distribution_id
            if id is not ShapeBase.NOT_SET:
                _params['id'] = id
            _request = shapes.GetInvalidationRequest(**_params)
        response = self._boto_client.get_invalidation(**_request.to_boto())

        return shapes.GetInvalidationResult.from_boto(response)

    def get_public_key(
        self,
        _request: shapes.GetPublicKeyRequest = None,
        *,
        id: str,
    ) -> shapes.GetPublicKeyResult:
        """
        Get the public key information.
        """
        if _request is None:
            _params = {}
            if id is not ShapeBase.NOT_SET:
                _params['id'] = id
            _request = shapes.GetPublicKeyRequest(**_params)
        response = self._boto_client.get_public_key(**_request.to_boto())

        return shapes.GetPublicKeyResult.from_boto(response)

    def get_public_key_config(
        self,
        _request: shapes.GetPublicKeyConfigRequest = None,
        *,
        id: str,
    ) -> shapes.GetPublicKeyConfigResult:
        """
        Return public key configuration informaation
        """
        if _request is None:
            _params = {}
            if id is not ShapeBase.NOT_SET:
                _params['id'] = id
            _request = shapes.GetPublicKeyConfigRequest(**_params)
        response = self._boto_client.get_public_key_config(**_request.to_boto())

        return shapes.GetPublicKeyConfigResult.from_boto(response)

    def get_streaming_distribution(
        self,
        _request: shapes.GetStreamingDistributionRequest = None,
        *,
        id: str,
    ) -> shapes.GetStreamingDistributionResult:
        """
        Gets information about a specified RTMP distribution, including the distribution
        configuration.
        """
        if _request is None:
            _params = {}
            if id is not ShapeBase.NOT_SET:
                _params['id'] = id
            _request = shapes.GetStreamingDistributionRequest(**_params)
        response = self._boto_client.get_streaming_distribution(
            **_request.to_boto()
        )

        return shapes.GetStreamingDistributionResult.from_boto(response)

    def get_streaming_distribution_config(
        self,
        _request: shapes.GetStreamingDistributionConfigRequest = None,
        *,
        id: str,
    ) -> shapes.GetStreamingDistributionConfigResult:
        """
        Get the configuration information about a streaming distribution.
        """
        if _request is None:
            _params = {}
            if id is not ShapeBase.NOT_SET:
                _params['id'] = id
            _request = shapes.GetStreamingDistributionConfigRequest(**_params)
        response = self._boto_client.get_streaming_distribution_config(
            **_request.to_boto()
        )

        return shapes.GetStreamingDistributionConfigResult.from_boto(response)

    def list_cloud_front_origin_access_identities(
        self,
        _request: shapes.ListCloudFrontOriginAccessIdentitiesRequest = None,
        *,
        marker: str = ShapeBase.NOT_SET,
        max_items: str = ShapeBase.NOT_SET,
    ) -> shapes.ListCloudFrontOriginAccessIdentitiesResult:
        """
        Lists origin access identities.
        """
        if _request is None:
            _params = {}
            if marker is not ShapeBase.NOT_SET:
                _params['marker'] = marker
            if max_items is not ShapeBase.NOT_SET:
                _params['max_items'] = max_items
            _request = shapes.ListCloudFrontOriginAccessIdentitiesRequest(
                **_params
            )
        paginator = self.get_paginator(
            "list_cloud_front_origin_access_identities"
        ).paginate(**_request.to_boto())
        page_generator = (page for page in paginator)
        first_page = next(page_generator)
        result = shapes.ListCloudFrontOriginAccessIdentitiesResult.from_boto(
            first_page
        )
        result._page_iterator = page_generator
        return result

        return shapes.ListCloudFrontOriginAccessIdentitiesResult.from_boto(
            response
        )

    def list_distributions(
        self,
        _request: shapes.ListDistributionsRequest = None,
        *,
        marker: str = ShapeBase.NOT_SET,
        max_items: str = ShapeBase.NOT_SET,
    ) -> shapes.ListDistributionsResult:
        """
        List distributions.
        """
        if _request is None:
            _params = {}
            if marker is not ShapeBase.NOT_SET:
                _params['marker'] = marker
            if max_items is not ShapeBase.NOT_SET:
                _params['max_items'] = max_items
            _request = shapes.ListDistributionsRequest(**_params)
        paginator = self.get_paginator("list_distributions").paginate(
            **_request.to_boto()
        )
        page_generator = (page for page in paginator)
        first_page = next(page_generator)
        result = shapes.ListDistributionsResult.from_boto(first_page)
        result._page_iterator = page_generator
        return result

        return shapes.ListDistributionsResult.from_boto(response)

    def list_distributions_by_web_acl_id(
        self,
        _request: shapes.ListDistributionsByWebACLIdRequest = None,
        *,
        web_acl_id: str,
        marker: str = ShapeBase.NOT_SET,
        max_items: str = ShapeBase.NOT_SET,
    ) -> shapes.ListDistributionsByWebACLIdResult:
        """
        List the distributions that are associated with a specified AWS WAF web ACL.
        """
        if _request is None:
            _params = {}
            if web_acl_id is not ShapeBase.NOT_SET:
                _params['web_acl_id'] = web_acl_id
            if marker is not ShapeBase.NOT_SET:
                _params['marker'] = marker
            if max_items is not ShapeBase.NOT_SET:
                _params['max_items'] = max_items
            _request = shapes.ListDistributionsByWebACLIdRequest(**_params)
        response = self._boto_client.list_distributions_by_web_acl_id(
            **_request.to_boto()
        )

        return shapes.ListDistributionsByWebACLIdResult.from_boto(response)

    def list_field_level_encryption_configs(
        self,
        _request: shapes.ListFieldLevelEncryptionConfigsRequest = None,
        *,
        marker: str = ShapeBase.NOT_SET,
        max_items: str = ShapeBase.NOT_SET,
    ) -> shapes.ListFieldLevelEncryptionConfigsResult:
        """
        List all field-level encryption configurations that have been created in
        CloudFront for this account.
        """
        if _request is None:
            _params = {}
            if marker is not ShapeBase.NOT_SET:
                _params['marker'] = marker
            if max_items is not ShapeBase.NOT_SET:
                _params['max_items'] = max_items
            _request = shapes.ListFieldLevelEncryptionConfigsRequest(**_params)
        response = self._boto_client.list_field_level_encryption_configs(
            **_request.to_boto()
        )

        return shapes.ListFieldLevelEncryptionConfigsResult.from_boto(response)

    def list_field_level_encryption_profiles(
        self,
        _request: shapes.ListFieldLevelEncryptionProfilesRequest = None,
        *,
        marker: str = ShapeBase.NOT_SET,
        max_items: str = ShapeBase.NOT_SET,
    ) -> shapes.ListFieldLevelEncryptionProfilesResult:
        """
        Request a list of field-level encryption profiles that have been created in
        CloudFront for this account.
        """
        if _request is None:
            _params = {}
            if marker is not ShapeBase.NOT_SET:
                _params['marker'] = marker
            if max_items is not ShapeBase.NOT_SET:
                _params['max_items'] = max_items
            _request = shapes.ListFieldLevelEncryptionProfilesRequest(**_params)
        response = self._boto_client.list_field_level_encryption_profiles(
            **_request.to_boto()
        )

        return shapes.ListFieldLevelEncryptionProfilesResult.from_boto(response)

    def list_invalidations(
        self,
        _request: shapes.ListInvalidationsRequest = None,
        *,
        distribution_id: str,
        marker: str = ShapeBase.NOT_SET,
        max_items: str = ShapeBase.NOT_SET,
    ) -> shapes.ListInvalidationsResult:
        """
        Lists invalidation batches.
        """
        if _request is None:
            _params = {}
            if distribution_id is not ShapeBase.NOT_SET:
                _params['distribution_id'] = distribution_id
            if marker is not ShapeBase.NOT_SET:
                _params['marker'] = marker
            if max_items is not ShapeBase.NOT_SET:
                _params['max_items'] = max_items
            _request = shapes.ListInvalidationsRequest(**_params)
        paginator = self.get_paginator("list_invalidations").paginate(
            **_request.to_boto()
        )
        page_generator = (page for page in paginator)
        first_page = next(page_generator)
        result = shapes.ListInvalidationsResult.from_boto(first_page)
        result._page_iterator = page_generator
        return result

        return shapes.ListInvalidationsResult.from_boto(response)

    def list_public_keys(
        self,
        _request: shapes.ListPublicKeysRequest = None,
        *,
        marker: str = ShapeBase.NOT_SET,
        max_items: str = ShapeBase.NOT_SET,
    ) -> shapes.ListPublicKeysResult:
        """
        List all public keys that have been added to CloudFront for this account.
        """
        if _request is None:
            _params = {}
            if marker is not ShapeBase.NOT_SET:
                _params['marker'] = marker
            if max_items is not ShapeBase.NOT_SET:
                _params['max_items'] = max_items
            _request = shapes.ListPublicKeysRequest(**_params)
        response = self._boto_client.list_public_keys(**_request.to_boto())

        return shapes.ListPublicKeysResult.from_boto(response)

    def list_streaming_distributions(
        self,
        _request: shapes.ListStreamingDistributionsRequest = None,
        *,
        marker: str = ShapeBase.NOT_SET,
        max_items: str = ShapeBase.NOT_SET,
    ) -> shapes.ListStreamingDistributionsResult:
        """
        List streaming distributions.
        """
        if _request is None:
            _params = {}
            if marker is not ShapeBase.NOT_SET:
                _params['marker'] = marker
            if max_items is not ShapeBase.NOT_SET:
                _params['max_items'] = max_items
            _request = shapes.ListStreamingDistributionsRequest(**_params)
        paginator = self.get_paginator("list_streaming_distributions").paginate(
            **_request.to_boto()
        )
        page_generator = (page for page in paginator)
        first_page = next(page_generator)
        result = shapes.ListStreamingDistributionsResult.from_boto(first_page)
        result._page_iterator = page_generator
        return result

        return shapes.ListStreamingDistributionsResult.from_boto(response)

    def list_tags_for_resource(
        self,
        _request: shapes.ListTagsForResourceRequest = None,
        *,
        resource: str,
    ) -> shapes.ListTagsForResourceResult:
        """
        List tags for a CloudFront resource.
        """
        if _request is None:
            _params = {}
            if resource is not ShapeBase.NOT_SET:
                _params['resource'] = resource
            _request = shapes.ListTagsForResourceRequest(**_params)
        response = self._boto_client.list_tags_for_resource(
            **_request.to_boto()
        )

        return shapes.ListTagsForResourceResult.from_boto(response)

    def tag_resource(
        self,
        _request: shapes.TagResourceRequest = None,
        *,
        resource: str,
        tags: shapes.Tags,
    ) -> None:
        """
        Add tags to a CloudFront resource.
        """
        if _request is None:
            _params = {}
            if resource is not ShapeBase.NOT_SET:
                _params['resource'] = resource
            if tags is not ShapeBase.NOT_SET:
                _params['tags'] = tags
            _request = shapes.TagResourceRequest(**_params)
        response = self._boto_client.tag_resource(**_request.to_boto())

    def untag_resource(
        self,
        _request: shapes.UntagResourceRequest = None,
        *,
        resource: str,
        tag_keys: shapes.TagKeys,
    ) -> None:
        """
        Remove tags from a CloudFront resource.
        """
        if _request is None:
            _params = {}
            if resource is not ShapeBase.NOT_SET:
                _params['resource'] = resource
            if tag_keys is not ShapeBase.NOT_SET:
                _params['tag_keys'] = tag_keys
            _request = shapes.UntagResourceRequest(**_params)
        response = self._boto_client.untag_resource(**_request.to_boto())

    def update_cloud_front_origin_access_identity(
        self,
        _request: shapes.UpdateCloudFrontOriginAccessIdentityRequest = None,
        *,
        cloud_front_origin_access_identity_config: shapes.
        CloudFrontOriginAccessIdentityConfig,
        id: str,
        if_match: str = ShapeBase.NOT_SET,
    ) -> shapes.UpdateCloudFrontOriginAccessIdentityResult:
        """
        Update an origin access identity.
        """
        if _request is None:
            _params = {}
            if cloud_front_origin_access_identity_config is not ShapeBase.NOT_SET:
                _params['cloud_front_origin_access_identity_config'
                       ] = cloud_front_origin_access_identity_config
            if id is not ShapeBase.NOT_SET:
                _params['id'] = id
            if if_match is not ShapeBase.NOT_SET:
                _params['if_match'] = if_match
            _request = shapes.UpdateCloudFrontOriginAccessIdentityRequest(
                **_params
            )
        response = self._boto_client.update_cloud_front_origin_access_identity(
            **_request.to_boto()
        )

        return shapes.UpdateCloudFrontOriginAccessIdentityResult.from_boto(
            response
        )

    def update_distribution(
        self,
        _request: shapes.UpdateDistributionRequest = None,
        *,
        distribution_config: shapes.DistributionConfig,
        id: str,
        if_match: str = ShapeBase.NOT_SET,
    ) -> shapes.UpdateDistributionResult:
        """
        Updates the configuration for a web distribution. Perform the following steps.

        For information about updating a distribution using the CloudFront console, see
        [Creating or Updating a Web Distribution Using the CloudFront Console
        ](http://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/distribution-
        web-creating-console.html) in the _Amazon CloudFront Developer Guide_.

        **To update a web distribution using the CloudFront API**

          1. Submit a GetDistributionConfig request to get the current configuration and an `Etag` header for the distribution.

        If you update the distribution again, you need to get a new `Etag` header.

          2. Update the XML document that was returned in the response to your `GetDistributionConfig` request to include the desired changes. You can't change the value of `CallerReference`. If you try to change this value, CloudFront returns an `IllegalUpdate` error. Note that you must strip out the ETag parameter that is returned.

        The new configuration replaces the existing configuration; the values that you
        specify in an `UpdateDistribution` request are not merged into the existing
        configuration. When you add, delete, or replace values in an element that allows
        multiple values (for example, `CNAME`), you must specify all of the values that
        you want to appear in the updated distribution. In addition, you must update the
        corresponding `Quantity` element.

          3. Submit an `UpdateDistribution` request to update the configuration for your distribution:

            * In the request body, include the XML document that you updated in Step 2. The request body must include an XML document with a `DistributionConfig` element.

            * Set the value of the HTTP `If-Match` header to the value of the `ETag` header that CloudFront returned when you submitted the `GetDistributionConfig` request in Step 1.

          4. Review the response to the `UpdateDistribution` request to confirm that the configuration was successfully updated.

          5. Optional: Submit a GetDistribution request to confirm that your changes have propagated. When propagation is complete, the value of `Status` is `Deployed`.

        Beginning with the 2012-05-05 version of the CloudFront API, we made substantial
        changes to the format of the XML document that you include in the request body
        when you create or update a distribution. With previous versions of the API, we
        discovered that it was too easy to accidentally delete one or more values for an
        element that accepts multiple values, for example, CNAMEs and trusted signers.
        Our changes for the 2012-05-05 release are intended to prevent these accidental
        deletions and to notify you when there's a mismatch between the number of values
        you say you're specifying in the `Quantity` element and the number of values
        you're actually specifying.
        """
        if _request is None:
            _params = {}
            if distribution_config is not ShapeBase.NOT_SET:
                _params['distribution_config'] = distribution_config
            if id is not ShapeBase.NOT_SET:
                _params['id'] = id
            if if_match is not ShapeBase.NOT_SET:
                _params['if_match'] = if_match
            _request = shapes.UpdateDistributionRequest(**_params)
        response = self._boto_client.update_distribution(**_request.to_boto())

        return shapes.UpdateDistributionResult.from_boto(response)

    def update_field_level_encryption_config(
        self,
        _request: shapes.UpdateFieldLevelEncryptionConfigRequest = None,
        *,
        field_level_encryption_config: shapes.FieldLevelEncryptionConfig,
        id: str,
        if_match: str = ShapeBase.NOT_SET,
    ) -> shapes.UpdateFieldLevelEncryptionConfigResult:
        """
        Update a field-level encryption configuration.
        """
        if _request is None:
            _params = {}
            if field_level_encryption_config is not ShapeBase.NOT_SET:
                _params['field_level_encryption_config'
                       ] = field_level_encryption_config
            if id is not ShapeBase.NOT_SET:
                _params['id'] = id
            if if_match is not ShapeBase.NOT_SET:
                _params['if_match'] = if_match
            _request = shapes.UpdateFieldLevelEncryptionConfigRequest(**_params)
        response = self._boto_client.update_field_level_encryption_config(
            **_request.to_boto()
        )

        return shapes.UpdateFieldLevelEncryptionConfigResult.from_boto(response)

    def update_field_level_encryption_profile(
        self,
        _request: shapes.UpdateFieldLevelEncryptionProfileRequest = None,
        *,
        field_level_encryption_profile_config: shapes.
        FieldLevelEncryptionProfileConfig,
        id: str,
        if_match: str = ShapeBase.NOT_SET,
    ) -> shapes.UpdateFieldLevelEncryptionProfileResult:
        """
        Update a field-level encryption profile.
        """
        if _request is None:
            _params = {}
            if field_level_encryption_profile_config is not ShapeBase.NOT_SET:
                _params['field_level_encryption_profile_config'
                       ] = field_level_encryption_profile_config
            if id is not ShapeBase.NOT_SET:
                _params['id'] = id
            if if_match is not ShapeBase.NOT_SET:
                _params['if_match'] = if_match
            _request = shapes.UpdateFieldLevelEncryptionProfileRequest(
                **_params
            )
        response = self._boto_client.update_field_level_encryption_profile(
            **_request.to_boto()
        )

        return shapes.UpdateFieldLevelEncryptionProfileResult.from_boto(
            response
        )

    def update_public_key(
        self,
        _request: shapes.UpdatePublicKeyRequest = None,
        *,
        public_key_config: shapes.PublicKeyConfig,
        id: str,
        if_match: str = ShapeBase.NOT_SET,
    ) -> shapes.UpdatePublicKeyResult:
        """
        Update public key information. Note that the only value you can change is the
        comment.
        """
        if _request is None:
            _params = {}
            if public_key_config is not ShapeBase.NOT_SET:
                _params['public_key_config'] = public_key_config
            if id is not ShapeBase.NOT_SET:
                _params['id'] = id
            if if_match is not ShapeBase.NOT_SET:
                _params['if_match'] = if_match
            _request = shapes.UpdatePublicKeyRequest(**_params)
        response = self._boto_client.update_public_key(**_request.to_boto())

        return shapes.UpdatePublicKeyResult.from_boto(response)

    def update_streaming_distribution(
        self,
        _request: shapes.UpdateStreamingDistributionRequest = None,
        *,
        streaming_distribution_config: shapes.StreamingDistributionConfig,
        id: str,
        if_match: str = ShapeBase.NOT_SET,
    ) -> shapes.UpdateStreamingDistributionResult:
        """
        Update a streaming distribution.
        """
        if _request is None:
            _params = {}
            if streaming_distribution_config is not ShapeBase.NOT_SET:
                _params['streaming_distribution_config'
                       ] = streaming_distribution_config
            if id is not ShapeBase.NOT_SET:
                _params['id'] = id
            if if_match is not ShapeBase.NOT_SET:
                _params['if_match'] = if_match
            _request = shapes.UpdateStreamingDistributionRequest(**_params)
        response = self._boto_client.update_streaming_distribution(
            **_request.to_boto()
        )

        return shapes.UpdateStreamingDistributionResult.from_boto(response)
