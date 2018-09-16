import datetime
import typing
import boto3
from autoboto import ClientBase, ShapeBase, OutputShapeBase
from . import shapes


class Client(ClientBase):
    def __init__(self, *args, **kwargs):
        super().__init__("s3", *args, **kwargs)

    def abort_multipart_upload(
        self,
        _request: shapes.AbortMultipartUploadRequest = None,
        *,
        bucket: str,
        key: str,
        upload_id: str,
        request_payer: typing.Union[str, shapes.RequestPayer] = ShapeBase.
        NOT_SET,
    ) -> shapes.AbortMultipartUploadOutput:
        """
        Aborts a multipart upload.

        To verify that all parts have been removed, so you don't get charged for the
        part storage, you should call the List Parts operation and ensure the parts list
        is empty.
        """
        if _request is None:
            _params = {}
            if bucket is not ShapeBase.NOT_SET:
                _params['bucket'] = bucket
            if key is not ShapeBase.NOT_SET:
                _params['key'] = key
            if upload_id is not ShapeBase.NOT_SET:
                _params['upload_id'] = upload_id
            if request_payer is not ShapeBase.NOT_SET:
                _params['request_payer'] = request_payer
            _request = shapes.AbortMultipartUploadRequest(**_params)
        response = self._boto_client.abort_multipart_upload(
            **_request.to_boto()
        )

        return shapes.AbortMultipartUploadOutput.from_boto(response)

    def complete_multipart_upload(
        self,
        _request: shapes.CompleteMultipartUploadRequest = None,
        *,
        bucket: str,
        key: str,
        upload_id: str,
        multipart_upload: shapes.CompletedMultipartUpload = ShapeBase.NOT_SET,
        request_payer: typing.Union[str, shapes.RequestPayer] = ShapeBase.
        NOT_SET,
    ) -> shapes.CompleteMultipartUploadOutput:
        """
        Completes a multipart upload by assembling previously uploaded parts.
        """
        if _request is None:
            _params = {}
            if bucket is not ShapeBase.NOT_SET:
                _params['bucket'] = bucket
            if key is not ShapeBase.NOT_SET:
                _params['key'] = key
            if upload_id is not ShapeBase.NOT_SET:
                _params['upload_id'] = upload_id
            if multipart_upload is not ShapeBase.NOT_SET:
                _params['multipart_upload'] = multipart_upload
            if request_payer is not ShapeBase.NOT_SET:
                _params['request_payer'] = request_payer
            _request = shapes.CompleteMultipartUploadRequest(**_params)
        response = self._boto_client.complete_multipart_upload(
            **_request.to_boto()
        )

        return shapes.CompleteMultipartUploadOutput.from_boto(response)

    def copy_object(
        self,
        _request: shapes.CopyObjectRequest = None,
        *,
        bucket: str,
        copy_source: str,
        key: str,
        acl: typing.Union[str, shapes.ObjectCannedACL] = ShapeBase.NOT_SET,
        cache_control: str = ShapeBase.NOT_SET,
        content_disposition: str = ShapeBase.NOT_SET,
        content_encoding: str = ShapeBase.NOT_SET,
        content_language: str = ShapeBase.NOT_SET,
        content_type: str = ShapeBase.NOT_SET,
        copy_source_if_match: str = ShapeBase.NOT_SET,
        copy_source_if_modified_since: datetime.datetime = ShapeBase.NOT_SET,
        copy_source_if_none_match: str = ShapeBase.NOT_SET,
        copy_source_if_unmodified_since: datetime.datetime = ShapeBase.NOT_SET,
        expires: datetime.datetime = ShapeBase.NOT_SET,
        grant_full_control: str = ShapeBase.NOT_SET,
        grant_read: str = ShapeBase.NOT_SET,
        grant_read_acp: str = ShapeBase.NOT_SET,
        grant_write_acp: str = ShapeBase.NOT_SET,
        metadata: typing.Dict[str, str] = ShapeBase.NOT_SET,
        metadata_directive: typing.Union[str, shapes.
                                         MetadataDirective] = ShapeBase.NOT_SET,
        tagging_directive: typing.Union[str, shapes.
                                        TaggingDirective] = ShapeBase.NOT_SET,
        server_side_encryption: typing.
        Union[str, shapes.ServerSideEncryption] = ShapeBase.NOT_SET,
        storage_class: typing.Union[str, shapes.
                                    StorageClass] = ShapeBase.NOT_SET,
        website_redirect_location: str = ShapeBase.NOT_SET,
        sse_customer_algorithm: str = ShapeBase.NOT_SET,
        sse_customer_key: str = ShapeBase.NOT_SET,
        sse_customer_key_md5: str = ShapeBase.NOT_SET,
        ssekms_key_id: str = ShapeBase.NOT_SET,
        copy_source_sse_customer_algorithm: str = ShapeBase.NOT_SET,
        copy_source_sse_customer_key: str = ShapeBase.NOT_SET,
        copy_source_sse_customer_key_md5: str = ShapeBase.NOT_SET,
        request_payer: typing.Union[str, shapes.
                                    RequestPayer] = ShapeBase.NOT_SET,
        tagging: str = ShapeBase.NOT_SET,
    ) -> shapes.CopyObjectOutput:
        """
        Creates a copy of an object that is already stored in Amazon S3.
        """
        if _request is None:
            _params = {}
            if bucket is not ShapeBase.NOT_SET:
                _params['bucket'] = bucket
            if copy_source is not ShapeBase.NOT_SET:
                _params['copy_source'] = copy_source
            if key is not ShapeBase.NOT_SET:
                _params['key'] = key
            if acl is not ShapeBase.NOT_SET:
                _params['acl'] = acl
            if cache_control is not ShapeBase.NOT_SET:
                _params['cache_control'] = cache_control
            if content_disposition is not ShapeBase.NOT_SET:
                _params['content_disposition'] = content_disposition
            if content_encoding is not ShapeBase.NOT_SET:
                _params['content_encoding'] = content_encoding
            if content_language is not ShapeBase.NOT_SET:
                _params['content_language'] = content_language
            if content_type is not ShapeBase.NOT_SET:
                _params['content_type'] = content_type
            if copy_source_if_match is not ShapeBase.NOT_SET:
                _params['copy_source_if_match'] = copy_source_if_match
            if copy_source_if_modified_since is not ShapeBase.NOT_SET:
                _params['copy_source_if_modified_since'
                       ] = copy_source_if_modified_since
            if copy_source_if_none_match is not ShapeBase.NOT_SET:
                _params['copy_source_if_none_match'] = copy_source_if_none_match
            if copy_source_if_unmodified_since is not ShapeBase.NOT_SET:
                _params['copy_source_if_unmodified_since'
                       ] = copy_source_if_unmodified_since
            if expires is not ShapeBase.NOT_SET:
                _params['expires'] = expires
            if grant_full_control is not ShapeBase.NOT_SET:
                _params['grant_full_control'] = grant_full_control
            if grant_read is not ShapeBase.NOT_SET:
                _params['grant_read'] = grant_read
            if grant_read_acp is not ShapeBase.NOT_SET:
                _params['grant_read_acp'] = grant_read_acp
            if grant_write_acp is not ShapeBase.NOT_SET:
                _params['grant_write_acp'] = grant_write_acp
            if metadata is not ShapeBase.NOT_SET:
                _params['metadata'] = metadata
            if metadata_directive is not ShapeBase.NOT_SET:
                _params['metadata_directive'] = metadata_directive
            if tagging_directive is not ShapeBase.NOT_SET:
                _params['tagging_directive'] = tagging_directive
            if server_side_encryption is not ShapeBase.NOT_SET:
                _params['server_side_encryption'] = server_side_encryption
            if storage_class is not ShapeBase.NOT_SET:
                _params['storage_class'] = storage_class
            if website_redirect_location is not ShapeBase.NOT_SET:
                _params['website_redirect_location'] = website_redirect_location
            if sse_customer_algorithm is not ShapeBase.NOT_SET:
                _params['sse_customer_algorithm'] = sse_customer_algorithm
            if sse_customer_key is not ShapeBase.NOT_SET:
                _params['sse_customer_key'] = sse_customer_key
            if sse_customer_key_md5 is not ShapeBase.NOT_SET:
                _params['sse_customer_key_md5'] = sse_customer_key_md5
            if ssekms_key_id is not ShapeBase.NOT_SET:
                _params['ssekms_key_id'] = ssekms_key_id
            if copy_source_sse_customer_algorithm is not ShapeBase.NOT_SET:
                _params['copy_source_sse_customer_algorithm'
                       ] = copy_source_sse_customer_algorithm
            if copy_source_sse_customer_key is not ShapeBase.NOT_SET:
                _params['copy_source_sse_customer_key'
                       ] = copy_source_sse_customer_key
            if copy_source_sse_customer_key_md5 is not ShapeBase.NOT_SET:
                _params['copy_source_sse_customer_key_md5'
                       ] = copy_source_sse_customer_key_md5
            if request_payer is not ShapeBase.NOT_SET:
                _params['request_payer'] = request_payer
            if tagging is not ShapeBase.NOT_SET:
                _params['tagging'] = tagging
            _request = shapes.CopyObjectRequest(**_params)
        response = self._boto_client.copy_object(**_request.to_boto())

        return shapes.CopyObjectOutput.from_boto(response)

    def create_bucket(
        self,
        _request: shapes.CreateBucketRequest = None,
        *,
        bucket: str,
        acl: typing.Union[str, shapes.BucketCannedACL] = ShapeBase.NOT_SET,
        create_bucket_configuration: shapes.
        CreateBucketConfiguration = ShapeBase.NOT_SET,
        grant_full_control: str = ShapeBase.NOT_SET,
        grant_read: str = ShapeBase.NOT_SET,
        grant_read_acp: str = ShapeBase.NOT_SET,
        grant_write: str = ShapeBase.NOT_SET,
        grant_write_acp: str = ShapeBase.NOT_SET,
    ) -> shapes.CreateBucketOutput:
        """
        Creates a new bucket.
        """
        if _request is None:
            _params = {}
            if bucket is not ShapeBase.NOT_SET:
                _params['bucket'] = bucket
            if acl is not ShapeBase.NOT_SET:
                _params['acl'] = acl
            if create_bucket_configuration is not ShapeBase.NOT_SET:
                _params['create_bucket_configuration'
                       ] = create_bucket_configuration
            if grant_full_control is not ShapeBase.NOT_SET:
                _params['grant_full_control'] = grant_full_control
            if grant_read is not ShapeBase.NOT_SET:
                _params['grant_read'] = grant_read
            if grant_read_acp is not ShapeBase.NOT_SET:
                _params['grant_read_acp'] = grant_read_acp
            if grant_write is not ShapeBase.NOT_SET:
                _params['grant_write'] = grant_write
            if grant_write_acp is not ShapeBase.NOT_SET:
                _params['grant_write_acp'] = grant_write_acp
            _request = shapes.CreateBucketRequest(**_params)
        response = self._boto_client.create_bucket(**_request.to_boto())

        return shapes.CreateBucketOutput.from_boto(response)

    def create_multipart_upload(
        self,
        _request: shapes.CreateMultipartUploadRequest = None,
        *,
        bucket: str,
        key: str,
        acl: typing.Union[str, shapes.ObjectCannedACL] = ShapeBase.NOT_SET,
        cache_control: str = ShapeBase.NOT_SET,
        content_disposition: str = ShapeBase.NOT_SET,
        content_encoding: str = ShapeBase.NOT_SET,
        content_language: str = ShapeBase.NOT_SET,
        content_type: str = ShapeBase.NOT_SET,
        expires: datetime.datetime = ShapeBase.NOT_SET,
        grant_full_control: str = ShapeBase.NOT_SET,
        grant_read: str = ShapeBase.NOT_SET,
        grant_read_acp: str = ShapeBase.NOT_SET,
        grant_write_acp: str = ShapeBase.NOT_SET,
        metadata: typing.Dict[str, str] = ShapeBase.NOT_SET,
        server_side_encryption: typing.
        Union[str, shapes.ServerSideEncryption] = ShapeBase.NOT_SET,
        storage_class: typing.Union[str, shapes.
                                    StorageClass] = ShapeBase.NOT_SET,
        website_redirect_location: str = ShapeBase.NOT_SET,
        sse_customer_algorithm: str = ShapeBase.NOT_SET,
        sse_customer_key: str = ShapeBase.NOT_SET,
        sse_customer_key_md5: str = ShapeBase.NOT_SET,
        ssekms_key_id: str = ShapeBase.NOT_SET,
        request_payer: typing.Union[str, shapes.
                                    RequestPayer] = ShapeBase.NOT_SET,
        tagging: str = ShapeBase.NOT_SET,
    ) -> shapes.CreateMultipartUploadOutput:
        """
        Initiates a multipart upload and returns an upload ID.

        **Note:** After you initiate multipart upload and upload one or more parts, you
        must either complete or abort multipart upload in order to stop getting charged
        for storage of the uploaded parts. Only after you either complete or abort
        multipart upload, Amazon S3 frees up the parts storage and stops charging you
        for the parts storage.
        """
        if _request is None:
            _params = {}
            if bucket is not ShapeBase.NOT_SET:
                _params['bucket'] = bucket
            if key is not ShapeBase.NOT_SET:
                _params['key'] = key
            if acl is not ShapeBase.NOT_SET:
                _params['acl'] = acl
            if cache_control is not ShapeBase.NOT_SET:
                _params['cache_control'] = cache_control
            if content_disposition is not ShapeBase.NOT_SET:
                _params['content_disposition'] = content_disposition
            if content_encoding is not ShapeBase.NOT_SET:
                _params['content_encoding'] = content_encoding
            if content_language is not ShapeBase.NOT_SET:
                _params['content_language'] = content_language
            if content_type is not ShapeBase.NOT_SET:
                _params['content_type'] = content_type
            if expires is not ShapeBase.NOT_SET:
                _params['expires'] = expires
            if grant_full_control is not ShapeBase.NOT_SET:
                _params['grant_full_control'] = grant_full_control
            if grant_read is not ShapeBase.NOT_SET:
                _params['grant_read'] = grant_read
            if grant_read_acp is not ShapeBase.NOT_SET:
                _params['grant_read_acp'] = grant_read_acp
            if grant_write_acp is not ShapeBase.NOT_SET:
                _params['grant_write_acp'] = grant_write_acp
            if metadata is not ShapeBase.NOT_SET:
                _params['metadata'] = metadata
            if server_side_encryption is not ShapeBase.NOT_SET:
                _params['server_side_encryption'] = server_side_encryption
            if storage_class is not ShapeBase.NOT_SET:
                _params['storage_class'] = storage_class
            if website_redirect_location is not ShapeBase.NOT_SET:
                _params['website_redirect_location'] = website_redirect_location
            if sse_customer_algorithm is not ShapeBase.NOT_SET:
                _params['sse_customer_algorithm'] = sse_customer_algorithm
            if sse_customer_key is not ShapeBase.NOT_SET:
                _params['sse_customer_key'] = sse_customer_key
            if sse_customer_key_md5 is not ShapeBase.NOT_SET:
                _params['sse_customer_key_md5'] = sse_customer_key_md5
            if ssekms_key_id is not ShapeBase.NOT_SET:
                _params['ssekms_key_id'] = ssekms_key_id
            if request_payer is not ShapeBase.NOT_SET:
                _params['request_payer'] = request_payer
            if tagging is not ShapeBase.NOT_SET:
                _params['tagging'] = tagging
            _request = shapes.CreateMultipartUploadRequest(**_params)
        response = self._boto_client.create_multipart_upload(
            **_request.to_boto()
        )

        return shapes.CreateMultipartUploadOutput.from_boto(response)

    def delete_bucket(
        self,
        _request: shapes.DeleteBucketRequest = None,
        *,
        bucket: str,
    ) -> None:
        """
        Deletes the bucket. All objects (including all object versions and Delete
        Markers) in the bucket must be deleted before the bucket itself can be deleted.
        """
        if _request is None:
            _params = {}
            if bucket is not ShapeBase.NOT_SET:
                _params['bucket'] = bucket
            _request = shapes.DeleteBucketRequest(**_params)
        response = self._boto_client.delete_bucket(**_request.to_boto())

    def delete_bucket_analytics_configuration(
        self,
        _request: shapes.DeleteBucketAnalyticsConfigurationRequest = None,
        *,
        bucket: str,
        id: str,
    ) -> None:
        """
        Deletes an analytics configuration for the bucket (specified by the analytics
        configuration ID).
        """
        if _request is None:
            _params = {}
            if bucket is not ShapeBase.NOT_SET:
                _params['bucket'] = bucket
            if id is not ShapeBase.NOT_SET:
                _params['id'] = id
            _request = shapes.DeleteBucketAnalyticsConfigurationRequest(
                **_params
            )
        response = self._boto_client.delete_bucket_analytics_configuration(
            **_request.to_boto()
        )

    def delete_bucket_cors(
        self,
        _request: shapes.DeleteBucketCorsRequest = None,
        *,
        bucket: str,
    ) -> None:
        """
        Deletes the cors configuration information set for the bucket.
        """
        if _request is None:
            _params = {}
            if bucket is not ShapeBase.NOT_SET:
                _params['bucket'] = bucket
            _request = shapes.DeleteBucketCorsRequest(**_params)
        response = self._boto_client.delete_bucket_cors(**_request.to_boto())

    def delete_bucket_encryption(
        self,
        _request: shapes.DeleteBucketEncryptionRequest = None,
        *,
        bucket: str,
    ) -> None:
        """
        Deletes the server-side encryption configuration from the bucket.
        """
        if _request is None:
            _params = {}
            if bucket is not ShapeBase.NOT_SET:
                _params['bucket'] = bucket
            _request = shapes.DeleteBucketEncryptionRequest(**_params)
        response = self._boto_client.delete_bucket_encryption(
            **_request.to_boto()
        )

    def delete_bucket_inventory_configuration(
        self,
        _request: shapes.DeleteBucketInventoryConfigurationRequest = None,
        *,
        bucket: str,
        id: str,
    ) -> None:
        """
        Deletes an inventory configuration (identified by the inventory ID) from the
        bucket.
        """
        if _request is None:
            _params = {}
            if bucket is not ShapeBase.NOT_SET:
                _params['bucket'] = bucket
            if id is not ShapeBase.NOT_SET:
                _params['id'] = id
            _request = shapes.DeleteBucketInventoryConfigurationRequest(
                **_params
            )
        response = self._boto_client.delete_bucket_inventory_configuration(
            **_request.to_boto()
        )

    def delete_bucket_lifecycle(
        self,
        _request: shapes.DeleteBucketLifecycleRequest = None,
        *,
        bucket: str,
    ) -> None:
        """
        Deletes the lifecycle configuration from the bucket.
        """
        if _request is None:
            _params = {}
            if bucket is not ShapeBase.NOT_SET:
                _params['bucket'] = bucket
            _request = shapes.DeleteBucketLifecycleRequest(**_params)
        response = self._boto_client.delete_bucket_lifecycle(
            **_request.to_boto()
        )

    def delete_bucket_metrics_configuration(
        self,
        _request: shapes.DeleteBucketMetricsConfigurationRequest = None,
        *,
        bucket: str,
        id: str,
    ) -> None:
        """
        Deletes a metrics configuration (specified by the metrics configuration ID) from
        the bucket.
        """
        if _request is None:
            _params = {}
            if bucket is not ShapeBase.NOT_SET:
                _params['bucket'] = bucket
            if id is not ShapeBase.NOT_SET:
                _params['id'] = id
            _request = shapes.DeleteBucketMetricsConfigurationRequest(**_params)
        response = self._boto_client.delete_bucket_metrics_configuration(
            **_request.to_boto()
        )

    def delete_bucket_policy(
        self,
        _request: shapes.DeleteBucketPolicyRequest = None,
        *,
        bucket: str,
    ) -> None:
        """
        Deletes the policy from the bucket.
        """
        if _request is None:
            _params = {}
            if bucket is not ShapeBase.NOT_SET:
                _params['bucket'] = bucket
            _request = shapes.DeleteBucketPolicyRequest(**_params)
        response = self._boto_client.delete_bucket_policy(**_request.to_boto())

    def delete_bucket_replication(
        self,
        _request: shapes.DeleteBucketReplicationRequest = None,
        *,
        bucket: str,
    ) -> None:
        """
        Deletes the replication configuration from the bucket.
        """
        if _request is None:
            _params = {}
            if bucket is not ShapeBase.NOT_SET:
                _params['bucket'] = bucket
            _request = shapes.DeleteBucketReplicationRequest(**_params)
        response = self._boto_client.delete_bucket_replication(
            **_request.to_boto()
        )

    def delete_bucket_tagging(
        self,
        _request: shapes.DeleteBucketTaggingRequest = None,
        *,
        bucket: str,
    ) -> None:
        """
        Deletes the tags from the bucket.
        """
        if _request is None:
            _params = {}
            if bucket is not ShapeBase.NOT_SET:
                _params['bucket'] = bucket
            _request = shapes.DeleteBucketTaggingRequest(**_params)
        response = self._boto_client.delete_bucket_tagging(**_request.to_boto())

    def delete_bucket_website(
        self,
        _request: shapes.DeleteBucketWebsiteRequest = None,
        *,
        bucket: str,
    ) -> None:
        """
        This operation removes the website configuration from the bucket.
        """
        if _request is None:
            _params = {}
            if bucket is not ShapeBase.NOT_SET:
                _params['bucket'] = bucket
            _request = shapes.DeleteBucketWebsiteRequest(**_params)
        response = self._boto_client.delete_bucket_website(**_request.to_boto())

    def delete_object(
        self,
        _request: shapes.DeleteObjectRequest = None,
        *,
        bucket: str,
        key: str,
        mfa: str = ShapeBase.NOT_SET,
        version_id: str = ShapeBase.NOT_SET,
        request_payer: typing.Union[str, shapes.RequestPayer] = ShapeBase.
        NOT_SET,
    ) -> shapes.DeleteObjectOutput:
        """
        Removes the null version (if there is one) of an object and inserts a delete
        marker, which becomes the latest version of the object. If there isn't a null
        version, Amazon S3 does not remove any objects.
        """
        if _request is None:
            _params = {}
            if bucket is not ShapeBase.NOT_SET:
                _params['bucket'] = bucket
            if key is not ShapeBase.NOT_SET:
                _params['key'] = key
            if mfa is not ShapeBase.NOT_SET:
                _params['mfa'] = mfa
            if version_id is not ShapeBase.NOT_SET:
                _params['version_id'] = version_id
            if request_payer is not ShapeBase.NOT_SET:
                _params['request_payer'] = request_payer
            _request = shapes.DeleteObjectRequest(**_params)
        response = self._boto_client.delete_object(**_request.to_boto())

        return shapes.DeleteObjectOutput.from_boto(response)

    def delete_object_tagging(
        self,
        _request: shapes.DeleteObjectTaggingRequest = None,
        *,
        bucket: str,
        key: str,
        version_id: str = ShapeBase.NOT_SET,
    ) -> shapes.DeleteObjectTaggingOutput:
        """
        Removes the tag-set from an existing object.
        """
        if _request is None:
            _params = {}
            if bucket is not ShapeBase.NOT_SET:
                _params['bucket'] = bucket
            if key is not ShapeBase.NOT_SET:
                _params['key'] = key
            if version_id is not ShapeBase.NOT_SET:
                _params['version_id'] = version_id
            _request = shapes.DeleteObjectTaggingRequest(**_params)
        response = self._boto_client.delete_object_tagging(**_request.to_boto())

        return shapes.DeleteObjectTaggingOutput.from_boto(response)

    def delete_objects(
        self,
        _request: shapes.DeleteObjectsRequest = None,
        *,
        bucket: str,
        delete: shapes.Delete,
        mfa: str = ShapeBase.NOT_SET,
        request_payer: typing.Union[str, shapes.RequestPayer] = ShapeBase.
        NOT_SET,
    ) -> shapes.DeleteObjectsOutput:
        """
        This operation enables you to delete multiple objects from a bucket using a
        single HTTP request. You may specify up to 1000 keys.
        """
        if _request is None:
            _params = {}
            if bucket is not ShapeBase.NOT_SET:
                _params['bucket'] = bucket
            if delete is not ShapeBase.NOT_SET:
                _params['delete'] = delete
            if mfa is not ShapeBase.NOT_SET:
                _params['mfa'] = mfa
            if request_payer is not ShapeBase.NOT_SET:
                _params['request_payer'] = request_payer
            _request = shapes.DeleteObjectsRequest(**_params)
        response = self._boto_client.delete_objects(**_request.to_boto())

        return shapes.DeleteObjectsOutput.from_boto(response)

    def get_bucket_accelerate_configuration(
        self,
        _request: shapes.GetBucketAccelerateConfigurationRequest = None,
        *,
        bucket: str,
    ) -> shapes.GetBucketAccelerateConfigurationOutput:
        """
        Returns the accelerate configuration of a bucket.
        """
        if _request is None:
            _params = {}
            if bucket is not ShapeBase.NOT_SET:
                _params['bucket'] = bucket
            _request = shapes.GetBucketAccelerateConfigurationRequest(**_params)
        response = self._boto_client.get_bucket_accelerate_configuration(
            **_request.to_boto()
        )

        return shapes.GetBucketAccelerateConfigurationOutput.from_boto(response)

    def get_bucket_acl(
        self,
        _request: shapes.GetBucketAclRequest = None,
        *,
        bucket: str,
    ) -> shapes.GetBucketAclOutput:
        """
        Gets the access control policy for the bucket.
        """
        if _request is None:
            _params = {}
            if bucket is not ShapeBase.NOT_SET:
                _params['bucket'] = bucket
            _request = shapes.GetBucketAclRequest(**_params)
        response = self._boto_client.get_bucket_acl(**_request.to_boto())

        return shapes.GetBucketAclOutput.from_boto(response)

    def get_bucket_analytics_configuration(
        self,
        _request: shapes.GetBucketAnalyticsConfigurationRequest = None,
        *,
        bucket: str,
        id: str,
    ) -> shapes.GetBucketAnalyticsConfigurationOutput:
        """
        Gets an analytics configuration for the bucket (specified by the analytics
        configuration ID).
        """
        if _request is None:
            _params = {}
            if bucket is not ShapeBase.NOT_SET:
                _params['bucket'] = bucket
            if id is not ShapeBase.NOT_SET:
                _params['id'] = id
            _request = shapes.GetBucketAnalyticsConfigurationRequest(**_params)
        response = self._boto_client.get_bucket_analytics_configuration(
            **_request.to_boto()
        )

        return shapes.GetBucketAnalyticsConfigurationOutput.from_boto(response)

    def get_bucket_cors(
        self,
        _request: shapes.GetBucketCorsRequest = None,
        *,
        bucket: str,
    ) -> shapes.GetBucketCorsOutput:
        """
        Returns the cors configuration for the bucket.
        """
        if _request is None:
            _params = {}
            if bucket is not ShapeBase.NOT_SET:
                _params['bucket'] = bucket
            _request = shapes.GetBucketCorsRequest(**_params)
        response = self._boto_client.get_bucket_cors(**_request.to_boto())

        return shapes.GetBucketCorsOutput.from_boto(response)

    def get_bucket_encryption(
        self,
        _request: shapes.GetBucketEncryptionRequest = None,
        *,
        bucket: str,
    ) -> shapes.GetBucketEncryptionOutput:
        """
        Returns the server-side encryption configuration of a bucket.
        """
        if _request is None:
            _params = {}
            if bucket is not ShapeBase.NOT_SET:
                _params['bucket'] = bucket
            _request = shapes.GetBucketEncryptionRequest(**_params)
        response = self._boto_client.get_bucket_encryption(**_request.to_boto())

        return shapes.GetBucketEncryptionOutput.from_boto(response)

    def get_bucket_inventory_configuration(
        self,
        _request: shapes.GetBucketInventoryConfigurationRequest = None,
        *,
        bucket: str,
        id: str,
    ) -> shapes.GetBucketInventoryConfigurationOutput:
        """
        Returns an inventory configuration (identified by the inventory ID) from the
        bucket.
        """
        if _request is None:
            _params = {}
            if bucket is not ShapeBase.NOT_SET:
                _params['bucket'] = bucket
            if id is not ShapeBase.NOT_SET:
                _params['id'] = id
            _request = shapes.GetBucketInventoryConfigurationRequest(**_params)
        response = self._boto_client.get_bucket_inventory_configuration(
            **_request.to_boto()
        )

        return shapes.GetBucketInventoryConfigurationOutput.from_boto(response)

    def get_bucket_lifecycle(
        self,
        _request: shapes.GetBucketLifecycleRequest = None,
        *,
        bucket: str,
    ) -> shapes.GetBucketLifecycleOutput:
        """
        Deprecated, see the GetBucketLifecycleConfiguration operation.
        """
        if _request is None:
            _params = {}
            if bucket is not ShapeBase.NOT_SET:
                _params['bucket'] = bucket
            _request = shapes.GetBucketLifecycleRequest(**_params)
        response = self._boto_client.get_bucket_lifecycle(**_request.to_boto())

        return shapes.GetBucketLifecycleOutput.from_boto(response)

    def get_bucket_lifecycle_configuration(
        self,
        _request: shapes.GetBucketLifecycleConfigurationRequest = None,
        *,
        bucket: str,
    ) -> shapes.GetBucketLifecycleConfigurationOutput:
        """
        Returns the lifecycle configuration information set on the bucket.
        """
        if _request is None:
            _params = {}
            if bucket is not ShapeBase.NOT_SET:
                _params['bucket'] = bucket
            _request = shapes.GetBucketLifecycleConfigurationRequest(**_params)
        response = self._boto_client.get_bucket_lifecycle_configuration(
            **_request.to_boto()
        )

        return shapes.GetBucketLifecycleConfigurationOutput.from_boto(response)

    def get_bucket_location(
        self,
        _request: shapes.GetBucketLocationRequest = None,
        *,
        bucket: str,
    ) -> shapes.GetBucketLocationOutput:
        """
        Returns the region the bucket resides in.
        """
        if _request is None:
            _params = {}
            if bucket is not ShapeBase.NOT_SET:
                _params['bucket'] = bucket
            _request = shapes.GetBucketLocationRequest(**_params)
        response = self._boto_client.get_bucket_location(**_request.to_boto())

        return shapes.GetBucketLocationOutput.from_boto(response)

    def get_bucket_logging(
        self,
        _request: shapes.GetBucketLoggingRequest = None,
        *,
        bucket: str,
    ) -> shapes.GetBucketLoggingOutput:
        """
        Returns the logging status of a bucket and the permissions users have to view
        and modify that status. To use GET, you must be the bucket owner.
        """
        if _request is None:
            _params = {}
            if bucket is not ShapeBase.NOT_SET:
                _params['bucket'] = bucket
            _request = shapes.GetBucketLoggingRequest(**_params)
        response = self._boto_client.get_bucket_logging(**_request.to_boto())

        return shapes.GetBucketLoggingOutput.from_boto(response)

    def get_bucket_metrics_configuration(
        self,
        _request: shapes.GetBucketMetricsConfigurationRequest = None,
        *,
        bucket: str,
        id: str,
    ) -> shapes.GetBucketMetricsConfigurationOutput:
        """
        Gets a metrics configuration (specified by the metrics configuration ID) from
        the bucket.
        """
        if _request is None:
            _params = {}
            if bucket is not ShapeBase.NOT_SET:
                _params['bucket'] = bucket
            if id is not ShapeBase.NOT_SET:
                _params['id'] = id
            _request = shapes.GetBucketMetricsConfigurationRequest(**_params)
        response = self._boto_client.get_bucket_metrics_configuration(
            **_request.to_boto()
        )

        return shapes.GetBucketMetricsConfigurationOutput.from_boto(response)

    def get_bucket_notification(
        self,
        _request: shapes.GetBucketNotificationConfigurationRequest = None,
        *,
        bucket: str,
    ) -> shapes.NotificationConfigurationDeprecated:
        """
        Deprecated, see the GetBucketNotificationConfiguration operation.
        """
        if _request is None:
            _params = {}
            if bucket is not ShapeBase.NOT_SET:
                _params['bucket'] = bucket
            _request = shapes.GetBucketNotificationConfigurationRequest(
                **_params
            )
        response = self._boto_client.get_bucket_notification(
            **_request.to_boto()
        )

        return shapes.NotificationConfigurationDeprecated.from_boto(response)

    def get_bucket_notification_configuration(
        self,
        _request: shapes.GetBucketNotificationConfigurationRequest = None,
        *,
        bucket: str,
    ) -> shapes.NotificationConfiguration:
        """
        Returns the notification configuration of a bucket.
        """
        if _request is None:
            _params = {}
            if bucket is not ShapeBase.NOT_SET:
                _params['bucket'] = bucket
            _request = shapes.GetBucketNotificationConfigurationRequest(
                **_params
            )
        response = self._boto_client.get_bucket_notification_configuration(
            **_request.to_boto()
        )

        return shapes.NotificationConfiguration.from_boto(response)

    def get_bucket_policy(
        self,
        _request: shapes.GetBucketPolicyRequest = None,
        *,
        bucket: str,
    ) -> shapes.GetBucketPolicyOutput:
        """
        Returns the policy of a specified bucket.
        """
        if _request is None:
            _params = {}
            if bucket is not ShapeBase.NOT_SET:
                _params['bucket'] = bucket
            _request = shapes.GetBucketPolicyRequest(**_params)
        response = self._boto_client.get_bucket_policy(**_request.to_boto())

        return shapes.GetBucketPolicyOutput.from_boto(response)

    def get_bucket_replication(
        self,
        _request: shapes.GetBucketReplicationRequest = None,
        *,
        bucket: str,
    ) -> shapes.GetBucketReplicationOutput:
        """
        Returns the replication configuration of a bucket.
        """
        if _request is None:
            _params = {}
            if bucket is not ShapeBase.NOT_SET:
                _params['bucket'] = bucket
            _request = shapes.GetBucketReplicationRequest(**_params)
        response = self._boto_client.get_bucket_replication(
            **_request.to_boto()
        )

        return shapes.GetBucketReplicationOutput.from_boto(response)

    def get_bucket_request_payment(
        self,
        _request: shapes.GetBucketRequestPaymentRequest = None,
        *,
        bucket: str,
    ) -> shapes.GetBucketRequestPaymentOutput:
        """
        Returns the request payment configuration of a bucket.
        """
        if _request is None:
            _params = {}
            if bucket is not ShapeBase.NOT_SET:
                _params['bucket'] = bucket
            _request = shapes.GetBucketRequestPaymentRequest(**_params)
        response = self._boto_client.get_bucket_request_payment(
            **_request.to_boto()
        )

        return shapes.GetBucketRequestPaymentOutput.from_boto(response)

    def get_bucket_tagging(
        self,
        _request: shapes.GetBucketTaggingRequest = None,
        *,
        bucket: str,
    ) -> shapes.GetBucketTaggingOutput:
        """
        Returns the tag set associated with the bucket.
        """
        if _request is None:
            _params = {}
            if bucket is not ShapeBase.NOT_SET:
                _params['bucket'] = bucket
            _request = shapes.GetBucketTaggingRequest(**_params)
        response = self._boto_client.get_bucket_tagging(**_request.to_boto())

        return shapes.GetBucketTaggingOutput.from_boto(response)

    def get_bucket_versioning(
        self,
        _request: shapes.GetBucketVersioningRequest = None,
        *,
        bucket: str,
    ) -> shapes.GetBucketVersioningOutput:
        """
        Returns the versioning state of a bucket.
        """
        if _request is None:
            _params = {}
            if bucket is not ShapeBase.NOT_SET:
                _params['bucket'] = bucket
            _request = shapes.GetBucketVersioningRequest(**_params)
        response = self._boto_client.get_bucket_versioning(**_request.to_boto())

        return shapes.GetBucketVersioningOutput.from_boto(response)

    def get_bucket_website(
        self,
        _request: shapes.GetBucketWebsiteRequest = None,
        *,
        bucket: str,
    ) -> shapes.GetBucketWebsiteOutput:
        """
        Returns the website configuration for a bucket.
        """
        if _request is None:
            _params = {}
            if bucket is not ShapeBase.NOT_SET:
                _params['bucket'] = bucket
            _request = shapes.GetBucketWebsiteRequest(**_params)
        response = self._boto_client.get_bucket_website(**_request.to_boto())

        return shapes.GetBucketWebsiteOutput.from_boto(response)

    def get_object(
        self,
        _request: shapes.GetObjectRequest = None,
        *,
        bucket: str,
        key: str,
        if_match: str = ShapeBase.NOT_SET,
        if_modified_since: datetime.datetime = ShapeBase.NOT_SET,
        if_none_match: str = ShapeBase.NOT_SET,
        if_unmodified_since: datetime.datetime = ShapeBase.NOT_SET,
        range: str = ShapeBase.NOT_SET,
        response_cache_control: str = ShapeBase.NOT_SET,
        response_content_disposition: str = ShapeBase.NOT_SET,
        response_content_encoding: str = ShapeBase.NOT_SET,
        response_content_language: str = ShapeBase.NOT_SET,
        response_content_type: str = ShapeBase.NOT_SET,
        response_expires: datetime.datetime = ShapeBase.NOT_SET,
        version_id: str = ShapeBase.NOT_SET,
        sse_customer_algorithm: str = ShapeBase.NOT_SET,
        sse_customer_key: str = ShapeBase.NOT_SET,
        sse_customer_key_md5: str = ShapeBase.NOT_SET,
        request_payer: typing.Union[str, shapes.RequestPayer] = ShapeBase.
        NOT_SET,
        part_number: int = ShapeBase.NOT_SET,
    ) -> shapes.GetObjectOutput:
        """
        Retrieves objects from Amazon S3.
        """
        if _request is None:
            _params = {}
            if bucket is not ShapeBase.NOT_SET:
                _params['bucket'] = bucket
            if key is not ShapeBase.NOT_SET:
                _params['key'] = key
            if if_match is not ShapeBase.NOT_SET:
                _params['if_match'] = if_match
            if if_modified_since is not ShapeBase.NOT_SET:
                _params['if_modified_since'] = if_modified_since
            if if_none_match is not ShapeBase.NOT_SET:
                _params['if_none_match'] = if_none_match
            if if_unmodified_since is not ShapeBase.NOT_SET:
                _params['if_unmodified_since'] = if_unmodified_since
            if range is not ShapeBase.NOT_SET:
                _params['range'] = range
            if response_cache_control is not ShapeBase.NOT_SET:
                _params['response_cache_control'] = response_cache_control
            if response_content_disposition is not ShapeBase.NOT_SET:
                _params['response_content_disposition'
                       ] = response_content_disposition
            if response_content_encoding is not ShapeBase.NOT_SET:
                _params['response_content_encoding'] = response_content_encoding
            if response_content_language is not ShapeBase.NOT_SET:
                _params['response_content_language'] = response_content_language
            if response_content_type is not ShapeBase.NOT_SET:
                _params['response_content_type'] = response_content_type
            if response_expires is not ShapeBase.NOT_SET:
                _params['response_expires'] = response_expires
            if version_id is not ShapeBase.NOT_SET:
                _params['version_id'] = version_id
            if sse_customer_algorithm is not ShapeBase.NOT_SET:
                _params['sse_customer_algorithm'] = sse_customer_algorithm
            if sse_customer_key is not ShapeBase.NOT_SET:
                _params['sse_customer_key'] = sse_customer_key
            if sse_customer_key_md5 is not ShapeBase.NOT_SET:
                _params['sse_customer_key_md5'] = sse_customer_key_md5
            if request_payer is not ShapeBase.NOT_SET:
                _params['request_payer'] = request_payer
            if part_number is not ShapeBase.NOT_SET:
                _params['part_number'] = part_number
            _request = shapes.GetObjectRequest(**_params)
        response = self._boto_client.get_object(**_request.to_boto())

        return shapes.GetObjectOutput.from_boto(response)

    def get_object_acl(
        self,
        _request: shapes.GetObjectAclRequest = None,
        *,
        bucket: str,
        key: str,
        version_id: str = ShapeBase.NOT_SET,
        request_payer: typing.Union[str, shapes.RequestPayer] = ShapeBase.
        NOT_SET,
    ) -> shapes.GetObjectAclOutput:
        """
        Returns the access control list (ACL) of an object.
        """
        if _request is None:
            _params = {}
            if bucket is not ShapeBase.NOT_SET:
                _params['bucket'] = bucket
            if key is not ShapeBase.NOT_SET:
                _params['key'] = key
            if version_id is not ShapeBase.NOT_SET:
                _params['version_id'] = version_id
            if request_payer is not ShapeBase.NOT_SET:
                _params['request_payer'] = request_payer
            _request = shapes.GetObjectAclRequest(**_params)
        response = self._boto_client.get_object_acl(**_request.to_boto())

        return shapes.GetObjectAclOutput.from_boto(response)

    def get_object_tagging(
        self,
        _request: shapes.GetObjectTaggingRequest = None,
        *,
        bucket: str,
        key: str,
        version_id: str = ShapeBase.NOT_SET,
    ) -> shapes.GetObjectTaggingOutput:
        """
        Returns the tag-set of an object.
        """
        if _request is None:
            _params = {}
            if bucket is not ShapeBase.NOT_SET:
                _params['bucket'] = bucket
            if key is not ShapeBase.NOT_SET:
                _params['key'] = key
            if version_id is not ShapeBase.NOT_SET:
                _params['version_id'] = version_id
            _request = shapes.GetObjectTaggingRequest(**_params)
        response = self._boto_client.get_object_tagging(**_request.to_boto())

        return shapes.GetObjectTaggingOutput.from_boto(response)

    def get_object_torrent(
        self,
        _request: shapes.GetObjectTorrentRequest = None,
        *,
        bucket: str,
        key: str,
        request_payer: typing.Union[str, shapes.RequestPayer] = ShapeBase.
        NOT_SET,
    ) -> shapes.GetObjectTorrentOutput:
        """
        Return torrent files from a bucket.
        """
        if _request is None:
            _params = {}
            if bucket is not ShapeBase.NOT_SET:
                _params['bucket'] = bucket
            if key is not ShapeBase.NOT_SET:
                _params['key'] = key
            if request_payer is not ShapeBase.NOT_SET:
                _params['request_payer'] = request_payer
            _request = shapes.GetObjectTorrentRequest(**_params)
        response = self._boto_client.get_object_torrent(**_request.to_boto())

        return shapes.GetObjectTorrentOutput.from_boto(response)

    def head_bucket(
        self,
        _request: shapes.HeadBucketRequest = None,
        *,
        bucket: str,
    ) -> None:
        """
        This operation is useful to determine if a bucket exists and you have permission
        to access it.
        """
        if _request is None:
            _params = {}
            if bucket is not ShapeBase.NOT_SET:
                _params['bucket'] = bucket
            _request = shapes.HeadBucketRequest(**_params)
        response = self._boto_client.head_bucket(**_request.to_boto())

    def head_object(
        self,
        _request: shapes.HeadObjectRequest = None,
        *,
        bucket: str,
        key: str,
        if_match: str = ShapeBase.NOT_SET,
        if_modified_since: datetime.datetime = ShapeBase.NOT_SET,
        if_none_match: str = ShapeBase.NOT_SET,
        if_unmodified_since: datetime.datetime = ShapeBase.NOT_SET,
        range: str = ShapeBase.NOT_SET,
        version_id: str = ShapeBase.NOT_SET,
        sse_customer_algorithm: str = ShapeBase.NOT_SET,
        sse_customer_key: str = ShapeBase.NOT_SET,
        sse_customer_key_md5: str = ShapeBase.NOT_SET,
        request_payer: typing.Union[str, shapes.RequestPayer] = ShapeBase.
        NOT_SET,
        part_number: int = ShapeBase.NOT_SET,
    ) -> shapes.HeadObjectOutput:
        """
        The HEAD operation retrieves metadata from an object without returning the
        object itself. This operation is useful if you're only interested in an object's
        metadata. To use HEAD, you must have READ access to the object.
        """
        if _request is None:
            _params = {}
            if bucket is not ShapeBase.NOT_SET:
                _params['bucket'] = bucket
            if key is not ShapeBase.NOT_SET:
                _params['key'] = key
            if if_match is not ShapeBase.NOT_SET:
                _params['if_match'] = if_match
            if if_modified_since is not ShapeBase.NOT_SET:
                _params['if_modified_since'] = if_modified_since
            if if_none_match is not ShapeBase.NOT_SET:
                _params['if_none_match'] = if_none_match
            if if_unmodified_since is not ShapeBase.NOT_SET:
                _params['if_unmodified_since'] = if_unmodified_since
            if range is not ShapeBase.NOT_SET:
                _params['range'] = range
            if version_id is not ShapeBase.NOT_SET:
                _params['version_id'] = version_id
            if sse_customer_algorithm is not ShapeBase.NOT_SET:
                _params['sse_customer_algorithm'] = sse_customer_algorithm
            if sse_customer_key is not ShapeBase.NOT_SET:
                _params['sse_customer_key'] = sse_customer_key
            if sse_customer_key_md5 is not ShapeBase.NOT_SET:
                _params['sse_customer_key_md5'] = sse_customer_key_md5
            if request_payer is not ShapeBase.NOT_SET:
                _params['request_payer'] = request_payer
            if part_number is not ShapeBase.NOT_SET:
                _params['part_number'] = part_number
            _request = shapes.HeadObjectRequest(**_params)
        response = self._boto_client.head_object(**_request.to_boto())

        return shapes.HeadObjectOutput.from_boto(response)

    def list_bucket_analytics_configurations(
        self,
        _request: shapes.ListBucketAnalyticsConfigurationsRequest = None,
        *,
        bucket: str,
        continuation_token: str = ShapeBase.NOT_SET,
    ) -> shapes.ListBucketAnalyticsConfigurationsOutput:
        """
        Lists the analytics configurations for the bucket.
        """
        if _request is None:
            _params = {}
            if bucket is not ShapeBase.NOT_SET:
                _params['bucket'] = bucket
            if continuation_token is not ShapeBase.NOT_SET:
                _params['continuation_token'] = continuation_token
            _request = shapes.ListBucketAnalyticsConfigurationsRequest(
                **_params
            )
        response = self._boto_client.list_bucket_analytics_configurations(
            **_request.to_boto()
        )

        return shapes.ListBucketAnalyticsConfigurationsOutput.from_boto(
            response
        )

    def list_bucket_inventory_configurations(
        self,
        _request: shapes.ListBucketInventoryConfigurationsRequest = None,
        *,
        bucket: str,
        continuation_token: str = ShapeBase.NOT_SET,
    ) -> shapes.ListBucketInventoryConfigurationsOutput:
        """
        Returns a list of inventory configurations for the bucket.
        """
        if _request is None:
            _params = {}
            if bucket is not ShapeBase.NOT_SET:
                _params['bucket'] = bucket
            if continuation_token is not ShapeBase.NOT_SET:
                _params['continuation_token'] = continuation_token
            _request = shapes.ListBucketInventoryConfigurationsRequest(
                **_params
            )
        response = self._boto_client.list_bucket_inventory_configurations(
            **_request.to_boto()
        )

        return shapes.ListBucketInventoryConfigurationsOutput.from_boto(
            response
        )

    def list_bucket_metrics_configurations(
        self,
        _request: shapes.ListBucketMetricsConfigurationsRequest = None,
        *,
        bucket: str,
        continuation_token: str = ShapeBase.NOT_SET,
    ) -> shapes.ListBucketMetricsConfigurationsOutput:
        """
        Lists the metrics configurations for the bucket.
        """
        if _request is None:
            _params = {}
            if bucket is not ShapeBase.NOT_SET:
                _params['bucket'] = bucket
            if continuation_token is not ShapeBase.NOT_SET:
                _params['continuation_token'] = continuation_token
            _request = shapes.ListBucketMetricsConfigurationsRequest(**_params)
        response = self._boto_client.list_bucket_metrics_configurations(
            **_request.to_boto()
        )

        return shapes.ListBucketMetricsConfigurationsOutput.from_boto(response)

    def list_buckets(self) -> shapes.ListBucketsOutput:
        """
        Returns a list of all buckets owned by the authenticated sender of the request.
        """
        response = self._boto_client.list_buckets()

        return shapes.ListBucketsOutput.from_boto(response)

    def list_multipart_uploads(
        self,
        _request: shapes.ListMultipartUploadsRequest = None,
        *,
        bucket: str,
        delimiter: str = ShapeBase.NOT_SET,
        encoding_type: typing.Union[str, shapes.EncodingType] = ShapeBase.
        NOT_SET,
        key_marker: str = ShapeBase.NOT_SET,
        max_uploads: int = ShapeBase.NOT_SET,
        prefix: str = ShapeBase.NOT_SET,
        upload_id_marker: str = ShapeBase.NOT_SET,
    ) -> shapes.ListMultipartUploadsOutput:
        """
        This operation lists in-progress multipart uploads.
        """
        if _request is None:
            _params = {}
            if bucket is not ShapeBase.NOT_SET:
                _params['bucket'] = bucket
            if delimiter is not ShapeBase.NOT_SET:
                _params['delimiter'] = delimiter
            if encoding_type is not ShapeBase.NOT_SET:
                _params['encoding_type'] = encoding_type
            if key_marker is not ShapeBase.NOT_SET:
                _params['key_marker'] = key_marker
            if max_uploads is not ShapeBase.NOT_SET:
                _params['max_uploads'] = max_uploads
            if prefix is not ShapeBase.NOT_SET:
                _params['prefix'] = prefix
            if upload_id_marker is not ShapeBase.NOT_SET:
                _params['upload_id_marker'] = upload_id_marker
            _request = shapes.ListMultipartUploadsRequest(**_params)
        paginator = self.get_paginator("list_multipart_uploads").paginate(
            **_request.to_boto()
        )
        page_generator = (page for page in paginator)
        first_page = next(page_generator)
        result = shapes.ListMultipartUploadsOutput.from_boto(first_page)
        result._page_iterator = page_generator
        return result

        return shapes.ListMultipartUploadsOutput.from_boto(response)

    def list_object_versions(
        self,
        _request: shapes.ListObjectVersionsRequest = None,
        *,
        bucket: str,
        delimiter: str = ShapeBase.NOT_SET,
        encoding_type: typing.Union[str, shapes.EncodingType] = ShapeBase.
        NOT_SET,
        key_marker: str = ShapeBase.NOT_SET,
        max_keys: int = ShapeBase.NOT_SET,
        prefix: str = ShapeBase.NOT_SET,
        version_id_marker: str = ShapeBase.NOT_SET,
    ) -> shapes.ListObjectVersionsOutput:
        """
        Returns metadata about all of the versions of objects in a bucket.
        """
        if _request is None:
            _params = {}
            if bucket is not ShapeBase.NOT_SET:
                _params['bucket'] = bucket
            if delimiter is not ShapeBase.NOT_SET:
                _params['delimiter'] = delimiter
            if encoding_type is not ShapeBase.NOT_SET:
                _params['encoding_type'] = encoding_type
            if key_marker is not ShapeBase.NOT_SET:
                _params['key_marker'] = key_marker
            if max_keys is not ShapeBase.NOT_SET:
                _params['max_keys'] = max_keys
            if prefix is not ShapeBase.NOT_SET:
                _params['prefix'] = prefix
            if version_id_marker is not ShapeBase.NOT_SET:
                _params['version_id_marker'] = version_id_marker
            _request = shapes.ListObjectVersionsRequest(**_params)
        paginator = self.get_paginator("list_object_versions").paginate(
            **_request.to_boto()
        )
        page_generator = (page for page in paginator)
        first_page = next(page_generator)
        result = shapes.ListObjectVersionsOutput.from_boto(first_page)
        result._page_iterator = page_generator
        return result

        return shapes.ListObjectVersionsOutput.from_boto(response)

    def list_objects(
        self,
        _request: shapes.ListObjectsRequest = None,
        *,
        bucket: str,
        delimiter: str = ShapeBase.NOT_SET,
        encoding_type: typing.Union[str, shapes.
                                    EncodingType] = ShapeBase.NOT_SET,
        marker: str = ShapeBase.NOT_SET,
        max_keys: int = ShapeBase.NOT_SET,
        prefix: str = ShapeBase.NOT_SET,
        request_payer: typing.Union[str, shapes.RequestPayer] = ShapeBase.
        NOT_SET,
    ) -> shapes.ListObjectsOutput:
        """
        Returns some or all (up to 1000) of the objects in a bucket. You can use the
        request parameters as selection criteria to return a subset of the objects in a
        bucket.
        """
        if _request is None:
            _params = {}
            if bucket is not ShapeBase.NOT_SET:
                _params['bucket'] = bucket
            if delimiter is not ShapeBase.NOT_SET:
                _params['delimiter'] = delimiter
            if encoding_type is not ShapeBase.NOT_SET:
                _params['encoding_type'] = encoding_type
            if marker is not ShapeBase.NOT_SET:
                _params['marker'] = marker
            if max_keys is not ShapeBase.NOT_SET:
                _params['max_keys'] = max_keys
            if prefix is not ShapeBase.NOT_SET:
                _params['prefix'] = prefix
            if request_payer is not ShapeBase.NOT_SET:
                _params['request_payer'] = request_payer
            _request = shapes.ListObjectsRequest(**_params)
        paginator = self.get_paginator("list_objects").paginate(
            **_request.to_boto()
        )
        page_generator = (page for page in paginator)
        first_page = next(page_generator)
        result = shapes.ListObjectsOutput.from_boto(first_page)
        result._page_iterator = page_generator
        return result

        return shapes.ListObjectsOutput.from_boto(response)

    def list_objects_v2(
        self,
        _request: shapes.ListObjectsV2Request = None,
        *,
        bucket: str,
        delimiter: str = ShapeBase.NOT_SET,
        encoding_type: typing.Union[str, shapes.
                                    EncodingType] = ShapeBase.NOT_SET,
        max_keys: int = ShapeBase.NOT_SET,
        prefix: str = ShapeBase.NOT_SET,
        continuation_token: str = ShapeBase.NOT_SET,
        fetch_owner: bool = ShapeBase.NOT_SET,
        start_after: str = ShapeBase.NOT_SET,
        request_payer: typing.Union[str, shapes.RequestPayer] = ShapeBase.
        NOT_SET,
    ) -> shapes.ListObjectsV2Output:
        """
        Returns some or all (up to 1000) of the objects in a bucket. You can use the
        request parameters as selection criteria to return a subset of the objects in a
        bucket. Note: ListObjectsV2 is the revised List Objects API and we recommend you
        use this revised API for new application development.
        """
        if _request is None:
            _params = {}
            if bucket is not ShapeBase.NOT_SET:
                _params['bucket'] = bucket
            if delimiter is not ShapeBase.NOT_SET:
                _params['delimiter'] = delimiter
            if encoding_type is not ShapeBase.NOT_SET:
                _params['encoding_type'] = encoding_type
            if max_keys is not ShapeBase.NOT_SET:
                _params['max_keys'] = max_keys
            if prefix is not ShapeBase.NOT_SET:
                _params['prefix'] = prefix
            if continuation_token is not ShapeBase.NOT_SET:
                _params['continuation_token'] = continuation_token
            if fetch_owner is not ShapeBase.NOT_SET:
                _params['fetch_owner'] = fetch_owner
            if start_after is not ShapeBase.NOT_SET:
                _params['start_after'] = start_after
            if request_payer is not ShapeBase.NOT_SET:
                _params['request_payer'] = request_payer
            _request = shapes.ListObjectsV2Request(**_params)
        paginator = self.get_paginator("list_objects_v2").paginate(
            **_request.to_boto()
        )
        page_generator = (page for page in paginator)
        first_page = next(page_generator)
        result = shapes.ListObjectsV2Output.from_boto(first_page)
        result._page_iterator = page_generator
        return result

        return shapes.ListObjectsV2Output.from_boto(response)

    def list_parts(
        self,
        _request: shapes.ListPartsRequest = None,
        *,
        bucket: str,
        key: str,
        upload_id: str,
        max_parts: int = ShapeBase.NOT_SET,
        part_number_marker: int = ShapeBase.NOT_SET,
        request_payer: typing.Union[str, shapes.RequestPayer] = ShapeBase.
        NOT_SET,
    ) -> shapes.ListPartsOutput:
        """
        Lists the parts that have been uploaded for a specific multipart upload.
        """
        if _request is None:
            _params = {}
            if bucket is not ShapeBase.NOT_SET:
                _params['bucket'] = bucket
            if key is not ShapeBase.NOT_SET:
                _params['key'] = key
            if upload_id is not ShapeBase.NOT_SET:
                _params['upload_id'] = upload_id
            if max_parts is not ShapeBase.NOT_SET:
                _params['max_parts'] = max_parts
            if part_number_marker is not ShapeBase.NOT_SET:
                _params['part_number_marker'] = part_number_marker
            if request_payer is not ShapeBase.NOT_SET:
                _params['request_payer'] = request_payer
            _request = shapes.ListPartsRequest(**_params)
        paginator = self.get_paginator("list_parts").paginate(
            **_request.to_boto()
        )
        page_generator = (page for page in paginator)
        first_page = next(page_generator)
        result = shapes.ListPartsOutput.from_boto(first_page)
        result._page_iterator = page_generator
        return result

        return shapes.ListPartsOutput.from_boto(response)

    def put_bucket_accelerate_configuration(
        self,
        _request: shapes.PutBucketAccelerateConfigurationRequest = None,
        *,
        bucket: str,
        accelerate_configuration: shapes.AccelerateConfiguration,
    ) -> None:
        """
        Sets the accelerate configuration of an existing bucket.
        """
        if _request is None:
            _params = {}
            if bucket is not ShapeBase.NOT_SET:
                _params['bucket'] = bucket
            if accelerate_configuration is not ShapeBase.NOT_SET:
                _params['accelerate_configuration'] = accelerate_configuration
            _request = shapes.PutBucketAccelerateConfigurationRequest(**_params)
        response = self._boto_client.put_bucket_accelerate_configuration(
            **_request.to_boto()
        )

    def put_bucket_acl(
        self,
        _request: shapes.PutBucketAclRequest = None,
        *,
        bucket: str,
        acl: typing.Union[str, shapes.BucketCannedACL] = ShapeBase.NOT_SET,
        access_control_policy: shapes.AccessControlPolicy = ShapeBase.NOT_SET,
        content_md5: str = ShapeBase.NOT_SET,
        grant_full_control: str = ShapeBase.NOT_SET,
        grant_read: str = ShapeBase.NOT_SET,
        grant_read_acp: str = ShapeBase.NOT_SET,
        grant_write: str = ShapeBase.NOT_SET,
        grant_write_acp: str = ShapeBase.NOT_SET,
    ) -> None:
        """
        Sets the permissions on a bucket using access control lists (ACL).
        """
        if _request is None:
            _params = {}
            if bucket is not ShapeBase.NOT_SET:
                _params['bucket'] = bucket
            if acl is not ShapeBase.NOT_SET:
                _params['acl'] = acl
            if access_control_policy is not ShapeBase.NOT_SET:
                _params['access_control_policy'] = access_control_policy
            if content_md5 is not ShapeBase.NOT_SET:
                _params['content_md5'] = content_md5
            if grant_full_control is not ShapeBase.NOT_SET:
                _params['grant_full_control'] = grant_full_control
            if grant_read is not ShapeBase.NOT_SET:
                _params['grant_read'] = grant_read
            if grant_read_acp is not ShapeBase.NOT_SET:
                _params['grant_read_acp'] = grant_read_acp
            if grant_write is not ShapeBase.NOT_SET:
                _params['grant_write'] = grant_write
            if grant_write_acp is not ShapeBase.NOT_SET:
                _params['grant_write_acp'] = grant_write_acp
            _request = shapes.PutBucketAclRequest(**_params)
        response = self._boto_client.put_bucket_acl(**_request.to_boto())

    def put_bucket_analytics_configuration(
        self,
        _request: shapes.PutBucketAnalyticsConfigurationRequest = None,
        *,
        bucket: str,
        id: str,
        analytics_configuration: shapes.AnalyticsConfiguration,
    ) -> None:
        """
        Sets an analytics configuration for the bucket (specified by the analytics
        configuration ID).
        """
        if _request is None:
            _params = {}
            if bucket is not ShapeBase.NOT_SET:
                _params['bucket'] = bucket
            if id is not ShapeBase.NOT_SET:
                _params['id'] = id
            if analytics_configuration is not ShapeBase.NOT_SET:
                _params['analytics_configuration'] = analytics_configuration
            _request = shapes.PutBucketAnalyticsConfigurationRequest(**_params)
        response = self._boto_client.put_bucket_analytics_configuration(
            **_request.to_boto()
        )

    def put_bucket_cors(
        self,
        _request: shapes.PutBucketCorsRequest = None,
        *,
        bucket: str,
        cors_configuration: shapes.CORSConfiguration,
        content_md5: str = ShapeBase.NOT_SET,
    ) -> None:
        """
        Sets the cors configuration for a bucket.
        """
        if _request is None:
            _params = {}
            if bucket is not ShapeBase.NOT_SET:
                _params['bucket'] = bucket
            if cors_configuration is not ShapeBase.NOT_SET:
                _params['cors_configuration'] = cors_configuration
            if content_md5 is not ShapeBase.NOT_SET:
                _params['content_md5'] = content_md5
            _request = shapes.PutBucketCorsRequest(**_params)
        response = self._boto_client.put_bucket_cors(**_request.to_boto())

    def put_bucket_encryption(
        self,
        _request: shapes.PutBucketEncryptionRequest = None,
        *,
        bucket: str,
        server_side_encryption_configuration: shapes.
        ServerSideEncryptionConfiguration,
        content_md5: str = ShapeBase.NOT_SET,
    ) -> None:
        """
        Creates a new server-side encryption configuration (or replaces an existing one,
        if present).
        """
        if _request is None:
            _params = {}
            if bucket is not ShapeBase.NOT_SET:
                _params['bucket'] = bucket
            if server_side_encryption_configuration is not ShapeBase.NOT_SET:
                _params['server_side_encryption_configuration'
                       ] = server_side_encryption_configuration
            if content_md5 is not ShapeBase.NOT_SET:
                _params['content_md5'] = content_md5
            _request = shapes.PutBucketEncryptionRequest(**_params)
        response = self._boto_client.put_bucket_encryption(**_request.to_boto())

    def put_bucket_inventory_configuration(
        self,
        _request: shapes.PutBucketInventoryConfigurationRequest = None,
        *,
        bucket: str,
        id: str,
        inventory_configuration: shapes.InventoryConfiguration,
    ) -> None:
        """
        Adds an inventory configuration (identified by the inventory ID) from the
        bucket.
        """
        if _request is None:
            _params = {}
            if bucket is not ShapeBase.NOT_SET:
                _params['bucket'] = bucket
            if id is not ShapeBase.NOT_SET:
                _params['id'] = id
            if inventory_configuration is not ShapeBase.NOT_SET:
                _params['inventory_configuration'] = inventory_configuration
            _request = shapes.PutBucketInventoryConfigurationRequest(**_params)
        response = self._boto_client.put_bucket_inventory_configuration(
            **_request.to_boto()
        )

    def put_bucket_lifecycle(
        self,
        _request: shapes.PutBucketLifecycleRequest = None,
        *,
        bucket: str,
        content_md5: str = ShapeBase.NOT_SET,
        lifecycle_configuration: shapes.LifecycleConfiguration = ShapeBase.
        NOT_SET,
    ) -> None:
        """
        Deprecated, see the PutBucketLifecycleConfiguration operation.
        """
        if _request is None:
            _params = {}
            if bucket is not ShapeBase.NOT_SET:
                _params['bucket'] = bucket
            if content_md5 is not ShapeBase.NOT_SET:
                _params['content_md5'] = content_md5
            if lifecycle_configuration is not ShapeBase.NOT_SET:
                _params['lifecycle_configuration'] = lifecycle_configuration
            _request = shapes.PutBucketLifecycleRequest(**_params)
        response = self._boto_client.put_bucket_lifecycle(**_request.to_boto())

    def put_bucket_lifecycle_configuration(
        self,
        _request: shapes.PutBucketLifecycleConfigurationRequest = None,
        *,
        bucket: str,
        lifecycle_configuration: shapes.
        BucketLifecycleConfiguration = ShapeBase.NOT_SET,
    ) -> None:
        """
        Sets lifecycle configuration for your bucket. If a lifecycle configuration
        exists, it replaces it.
        """
        if _request is None:
            _params = {}
            if bucket is not ShapeBase.NOT_SET:
                _params['bucket'] = bucket
            if lifecycle_configuration is not ShapeBase.NOT_SET:
                _params['lifecycle_configuration'] = lifecycle_configuration
            _request = shapes.PutBucketLifecycleConfigurationRequest(**_params)
        response = self._boto_client.put_bucket_lifecycle_configuration(
            **_request.to_boto()
        )

    def put_bucket_logging(
        self,
        _request: shapes.PutBucketLoggingRequest = None,
        *,
        bucket: str,
        bucket_logging_status: shapes.BucketLoggingStatus,
        content_md5: str = ShapeBase.NOT_SET,
    ) -> None:
        """
        Set the logging parameters for a bucket and to specify permissions for who can
        view and modify the logging parameters. To set the logging status of a bucket,
        you must be the bucket owner.
        """
        if _request is None:
            _params = {}
            if bucket is not ShapeBase.NOT_SET:
                _params['bucket'] = bucket
            if bucket_logging_status is not ShapeBase.NOT_SET:
                _params['bucket_logging_status'] = bucket_logging_status
            if content_md5 is not ShapeBase.NOT_SET:
                _params['content_md5'] = content_md5
            _request = shapes.PutBucketLoggingRequest(**_params)
        response = self._boto_client.put_bucket_logging(**_request.to_boto())

    def put_bucket_metrics_configuration(
        self,
        _request: shapes.PutBucketMetricsConfigurationRequest = None,
        *,
        bucket: str,
        id: str,
        metrics_configuration: shapes.MetricsConfiguration,
    ) -> None:
        """
        Sets a metrics configuration (specified by the metrics configuration ID) for the
        bucket.
        """
        if _request is None:
            _params = {}
            if bucket is not ShapeBase.NOT_SET:
                _params['bucket'] = bucket
            if id is not ShapeBase.NOT_SET:
                _params['id'] = id
            if metrics_configuration is not ShapeBase.NOT_SET:
                _params['metrics_configuration'] = metrics_configuration
            _request = shapes.PutBucketMetricsConfigurationRequest(**_params)
        response = self._boto_client.put_bucket_metrics_configuration(
            **_request.to_boto()
        )

    def put_bucket_notification(
        self,
        _request: shapes.PutBucketNotificationRequest = None,
        *,
        bucket: str,
        notification_configuration: shapes.NotificationConfigurationDeprecated,
        content_md5: str = ShapeBase.NOT_SET,
    ) -> None:
        """
        Deprecated, see the PutBucketNotificationConfiguraiton operation.
        """
        if _request is None:
            _params = {}
            if bucket is not ShapeBase.NOT_SET:
                _params['bucket'] = bucket
            if notification_configuration is not ShapeBase.NOT_SET:
                _params['notification_configuration'
                       ] = notification_configuration
            if content_md5 is not ShapeBase.NOT_SET:
                _params['content_md5'] = content_md5
            _request = shapes.PutBucketNotificationRequest(**_params)
        response = self._boto_client.put_bucket_notification(
            **_request.to_boto()
        )

    def put_bucket_notification_configuration(
        self,
        _request: shapes.PutBucketNotificationConfigurationRequest = None,
        *,
        bucket: str,
        notification_configuration: shapes.NotificationConfiguration,
    ) -> None:
        """
        Enables notifications of specified events for a bucket.
        """
        if _request is None:
            _params = {}
            if bucket is not ShapeBase.NOT_SET:
                _params['bucket'] = bucket
            if notification_configuration is not ShapeBase.NOT_SET:
                _params['notification_configuration'
                       ] = notification_configuration
            _request = shapes.PutBucketNotificationConfigurationRequest(
                **_params
            )
        response = self._boto_client.put_bucket_notification_configuration(
            **_request.to_boto()
        )

    def put_bucket_policy(
        self,
        _request: shapes.PutBucketPolicyRequest = None,
        *,
        bucket: str,
        policy: str,
        content_md5: str = ShapeBase.NOT_SET,
        confirm_remove_self_bucket_access: bool = ShapeBase.NOT_SET,
    ) -> None:
        """
        Replaces a policy on a bucket. If the bucket already has a policy, the one in
        this request completely replaces it.
        """
        if _request is None:
            _params = {}
            if bucket is not ShapeBase.NOT_SET:
                _params['bucket'] = bucket
            if policy is not ShapeBase.NOT_SET:
                _params['policy'] = policy
            if content_md5 is not ShapeBase.NOT_SET:
                _params['content_md5'] = content_md5
            if confirm_remove_self_bucket_access is not ShapeBase.NOT_SET:
                _params['confirm_remove_self_bucket_access'
                       ] = confirm_remove_self_bucket_access
            _request = shapes.PutBucketPolicyRequest(**_params)
        response = self._boto_client.put_bucket_policy(**_request.to_boto())

    def put_bucket_replication(
        self,
        _request: shapes.PutBucketReplicationRequest = None,
        *,
        bucket: str,
        replication_configuration: shapes.ReplicationConfiguration,
        content_md5: str = ShapeBase.NOT_SET,
    ) -> None:
        """
        Creates a new replication configuration (or replaces an existing one, if
        present).
        """
        if _request is None:
            _params = {}
            if bucket is not ShapeBase.NOT_SET:
                _params['bucket'] = bucket
            if replication_configuration is not ShapeBase.NOT_SET:
                _params['replication_configuration'] = replication_configuration
            if content_md5 is not ShapeBase.NOT_SET:
                _params['content_md5'] = content_md5
            _request = shapes.PutBucketReplicationRequest(**_params)
        response = self._boto_client.put_bucket_replication(
            **_request.to_boto()
        )

    def put_bucket_request_payment(
        self,
        _request: shapes.PutBucketRequestPaymentRequest = None,
        *,
        bucket: str,
        request_payment_configuration: shapes.RequestPaymentConfiguration,
        content_md5: str = ShapeBase.NOT_SET,
    ) -> None:
        """
        Sets the request payment configuration for a bucket. By default, the bucket
        owner pays for downloads from the bucket. This configuration parameter enables
        the bucket owner (only) to specify that the person requesting the download will
        be charged for the download. Documentation on requester pays buckets can be
        found at
        http://docs.aws.amazon.com/AmazonS3/latest/dev/RequesterPaysBuckets.html
        """
        if _request is None:
            _params = {}
            if bucket is not ShapeBase.NOT_SET:
                _params['bucket'] = bucket
            if request_payment_configuration is not ShapeBase.NOT_SET:
                _params['request_payment_configuration'
                       ] = request_payment_configuration
            if content_md5 is not ShapeBase.NOT_SET:
                _params['content_md5'] = content_md5
            _request = shapes.PutBucketRequestPaymentRequest(**_params)
        response = self._boto_client.put_bucket_request_payment(
            **_request.to_boto()
        )

    def put_bucket_tagging(
        self,
        _request: shapes.PutBucketTaggingRequest = None,
        *,
        bucket: str,
        tagging: shapes.Tagging,
        content_md5: str = ShapeBase.NOT_SET,
    ) -> None:
        """
        Sets the tags for a bucket.
        """
        if _request is None:
            _params = {}
            if bucket is not ShapeBase.NOT_SET:
                _params['bucket'] = bucket
            if tagging is not ShapeBase.NOT_SET:
                _params['tagging'] = tagging
            if content_md5 is not ShapeBase.NOT_SET:
                _params['content_md5'] = content_md5
            _request = shapes.PutBucketTaggingRequest(**_params)
        response = self._boto_client.put_bucket_tagging(**_request.to_boto())

    def put_bucket_versioning(
        self,
        _request: shapes.PutBucketVersioningRequest = None,
        *,
        bucket: str,
        versioning_configuration: shapes.VersioningConfiguration,
        content_md5: str = ShapeBase.NOT_SET,
        mfa: str = ShapeBase.NOT_SET,
    ) -> None:
        """
        Sets the versioning state of an existing bucket. To set the versioning state,
        you must be the bucket owner.
        """
        if _request is None:
            _params = {}
            if bucket is not ShapeBase.NOT_SET:
                _params['bucket'] = bucket
            if versioning_configuration is not ShapeBase.NOT_SET:
                _params['versioning_configuration'] = versioning_configuration
            if content_md5 is not ShapeBase.NOT_SET:
                _params['content_md5'] = content_md5
            if mfa is not ShapeBase.NOT_SET:
                _params['mfa'] = mfa
            _request = shapes.PutBucketVersioningRequest(**_params)
        response = self._boto_client.put_bucket_versioning(**_request.to_boto())

    def put_bucket_website(
        self,
        _request: shapes.PutBucketWebsiteRequest = None,
        *,
        bucket: str,
        website_configuration: shapes.WebsiteConfiguration,
        content_md5: str = ShapeBase.NOT_SET,
    ) -> None:
        """
        Set the website configuration for a bucket.
        """
        if _request is None:
            _params = {}
            if bucket is not ShapeBase.NOT_SET:
                _params['bucket'] = bucket
            if website_configuration is not ShapeBase.NOT_SET:
                _params['website_configuration'] = website_configuration
            if content_md5 is not ShapeBase.NOT_SET:
                _params['content_md5'] = content_md5
            _request = shapes.PutBucketWebsiteRequest(**_params)
        response = self._boto_client.put_bucket_website(**_request.to_boto())

    def put_object(
        self,
        _request: shapes.PutObjectRequest = None,
        *,
        bucket: str,
        key: str,
        acl: typing.Union[str, shapes.ObjectCannedACL] = ShapeBase.NOT_SET,
        body: typing.Any = ShapeBase.NOT_SET,
        cache_control: str = ShapeBase.NOT_SET,
        content_disposition: str = ShapeBase.NOT_SET,
        content_encoding: str = ShapeBase.NOT_SET,
        content_language: str = ShapeBase.NOT_SET,
        content_length: int = ShapeBase.NOT_SET,
        content_md5: str = ShapeBase.NOT_SET,
        content_type: str = ShapeBase.NOT_SET,
        expires: datetime.datetime = ShapeBase.NOT_SET,
        grant_full_control: str = ShapeBase.NOT_SET,
        grant_read: str = ShapeBase.NOT_SET,
        grant_read_acp: str = ShapeBase.NOT_SET,
        grant_write_acp: str = ShapeBase.NOT_SET,
        metadata: typing.Dict[str, str] = ShapeBase.NOT_SET,
        server_side_encryption: typing.
        Union[str, shapes.ServerSideEncryption] = ShapeBase.NOT_SET,
        storage_class: typing.Union[str, shapes.
                                    StorageClass] = ShapeBase.NOT_SET,
        website_redirect_location: str = ShapeBase.NOT_SET,
        sse_customer_algorithm: str = ShapeBase.NOT_SET,
        sse_customer_key: str = ShapeBase.NOT_SET,
        sse_customer_key_md5: str = ShapeBase.NOT_SET,
        ssekms_key_id: str = ShapeBase.NOT_SET,
        request_payer: typing.Union[str, shapes.
                                    RequestPayer] = ShapeBase.NOT_SET,
        tagging: str = ShapeBase.NOT_SET,
    ) -> shapes.PutObjectOutput:
        """
        Adds an object to a bucket.
        """
        if _request is None:
            _params = {}
            if bucket is not ShapeBase.NOT_SET:
                _params['bucket'] = bucket
            if key is not ShapeBase.NOT_SET:
                _params['key'] = key
            if acl is not ShapeBase.NOT_SET:
                _params['acl'] = acl
            if body is not ShapeBase.NOT_SET:
                _params['body'] = body
            if cache_control is not ShapeBase.NOT_SET:
                _params['cache_control'] = cache_control
            if content_disposition is not ShapeBase.NOT_SET:
                _params['content_disposition'] = content_disposition
            if content_encoding is not ShapeBase.NOT_SET:
                _params['content_encoding'] = content_encoding
            if content_language is not ShapeBase.NOT_SET:
                _params['content_language'] = content_language
            if content_length is not ShapeBase.NOT_SET:
                _params['content_length'] = content_length
            if content_md5 is not ShapeBase.NOT_SET:
                _params['content_md5'] = content_md5
            if content_type is not ShapeBase.NOT_SET:
                _params['content_type'] = content_type
            if expires is not ShapeBase.NOT_SET:
                _params['expires'] = expires
            if grant_full_control is not ShapeBase.NOT_SET:
                _params['grant_full_control'] = grant_full_control
            if grant_read is not ShapeBase.NOT_SET:
                _params['grant_read'] = grant_read
            if grant_read_acp is not ShapeBase.NOT_SET:
                _params['grant_read_acp'] = grant_read_acp
            if grant_write_acp is not ShapeBase.NOT_SET:
                _params['grant_write_acp'] = grant_write_acp
            if metadata is not ShapeBase.NOT_SET:
                _params['metadata'] = metadata
            if server_side_encryption is not ShapeBase.NOT_SET:
                _params['server_side_encryption'] = server_side_encryption
            if storage_class is not ShapeBase.NOT_SET:
                _params['storage_class'] = storage_class
            if website_redirect_location is not ShapeBase.NOT_SET:
                _params['website_redirect_location'] = website_redirect_location
            if sse_customer_algorithm is not ShapeBase.NOT_SET:
                _params['sse_customer_algorithm'] = sse_customer_algorithm
            if sse_customer_key is not ShapeBase.NOT_SET:
                _params['sse_customer_key'] = sse_customer_key
            if sse_customer_key_md5 is not ShapeBase.NOT_SET:
                _params['sse_customer_key_md5'] = sse_customer_key_md5
            if ssekms_key_id is not ShapeBase.NOT_SET:
                _params['ssekms_key_id'] = ssekms_key_id
            if request_payer is not ShapeBase.NOT_SET:
                _params['request_payer'] = request_payer
            if tagging is not ShapeBase.NOT_SET:
                _params['tagging'] = tagging
            _request = shapes.PutObjectRequest(**_params)
        response = self._boto_client.put_object(**_request.to_boto())

        return shapes.PutObjectOutput.from_boto(response)

    def put_object_acl(
        self,
        _request: shapes.PutObjectAclRequest = None,
        *,
        bucket: str,
        key: str,
        acl: typing.Union[str, shapes.ObjectCannedACL] = ShapeBase.NOT_SET,
        access_control_policy: shapes.AccessControlPolicy = ShapeBase.NOT_SET,
        content_md5: str = ShapeBase.NOT_SET,
        grant_full_control: str = ShapeBase.NOT_SET,
        grant_read: str = ShapeBase.NOT_SET,
        grant_read_acp: str = ShapeBase.NOT_SET,
        grant_write: str = ShapeBase.NOT_SET,
        grant_write_acp: str = ShapeBase.NOT_SET,
        request_payer: typing.Union[str, shapes.RequestPayer] = ShapeBase.
        NOT_SET,
        version_id: str = ShapeBase.NOT_SET,
    ) -> shapes.PutObjectAclOutput:
        """
        uses the acl subresource to set the access control list (ACL) permissions for an
        object that already exists in a bucket
        """
        if _request is None:
            _params = {}
            if bucket is not ShapeBase.NOT_SET:
                _params['bucket'] = bucket
            if key is not ShapeBase.NOT_SET:
                _params['key'] = key
            if acl is not ShapeBase.NOT_SET:
                _params['acl'] = acl
            if access_control_policy is not ShapeBase.NOT_SET:
                _params['access_control_policy'] = access_control_policy
            if content_md5 is not ShapeBase.NOT_SET:
                _params['content_md5'] = content_md5
            if grant_full_control is not ShapeBase.NOT_SET:
                _params['grant_full_control'] = grant_full_control
            if grant_read is not ShapeBase.NOT_SET:
                _params['grant_read'] = grant_read
            if grant_read_acp is not ShapeBase.NOT_SET:
                _params['grant_read_acp'] = grant_read_acp
            if grant_write is not ShapeBase.NOT_SET:
                _params['grant_write'] = grant_write
            if grant_write_acp is not ShapeBase.NOT_SET:
                _params['grant_write_acp'] = grant_write_acp
            if request_payer is not ShapeBase.NOT_SET:
                _params['request_payer'] = request_payer
            if version_id is not ShapeBase.NOT_SET:
                _params['version_id'] = version_id
            _request = shapes.PutObjectAclRequest(**_params)
        response = self._boto_client.put_object_acl(**_request.to_boto())

        return shapes.PutObjectAclOutput.from_boto(response)

    def put_object_tagging(
        self,
        _request: shapes.PutObjectTaggingRequest = None,
        *,
        bucket: str,
        key: str,
        tagging: shapes.Tagging,
        version_id: str = ShapeBase.NOT_SET,
        content_md5: str = ShapeBase.NOT_SET,
    ) -> shapes.PutObjectTaggingOutput:
        """
        Sets the supplied tag-set to an object that already exists in a bucket
        """
        if _request is None:
            _params = {}
            if bucket is not ShapeBase.NOT_SET:
                _params['bucket'] = bucket
            if key is not ShapeBase.NOT_SET:
                _params['key'] = key
            if tagging is not ShapeBase.NOT_SET:
                _params['tagging'] = tagging
            if version_id is not ShapeBase.NOT_SET:
                _params['version_id'] = version_id
            if content_md5 is not ShapeBase.NOT_SET:
                _params['content_md5'] = content_md5
            _request = shapes.PutObjectTaggingRequest(**_params)
        response = self._boto_client.put_object_tagging(**_request.to_boto())

        return shapes.PutObjectTaggingOutput.from_boto(response)

    def restore_object(
        self,
        _request: shapes.RestoreObjectRequest = None,
        *,
        bucket: str,
        key: str,
        version_id: str = ShapeBase.NOT_SET,
        restore_request: shapes.RestoreRequest = ShapeBase.NOT_SET,
        request_payer: typing.Union[str, shapes.RequestPayer] = ShapeBase.
        NOT_SET,
    ) -> shapes.RestoreObjectOutput:
        """
        Restores an archived copy of an object back into Amazon S3
        """
        if _request is None:
            _params = {}
            if bucket is not ShapeBase.NOT_SET:
                _params['bucket'] = bucket
            if key is not ShapeBase.NOT_SET:
                _params['key'] = key
            if version_id is not ShapeBase.NOT_SET:
                _params['version_id'] = version_id
            if restore_request is not ShapeBase.NOT_SET:
                _params['restore_request'] = restore_request
            if request_payer is not ShapeBase.NOT_SET:
                _params['request_payer'] = request_payer
            _request = shapes.RestoreObjectRequest(**_params)
        response = self._boto_client.restore_object(**_request.to_boto())

        return shapes.RestoreObjectOutput.from_boto(response)

    def select_object_content(
        self,
        _request: shapes.SelectObjectContentRequest = None,
        *,
        bucket: str,
        key: str,
        expression: str,
        expression_type: typing.Union[str, shapes.ExpressionType],
        input_serialization: shapes.InputSerialization,
        output_serialization: shapes.OutputSerialization,
        sse_customer_algorithm: str = ShapeBase.NOT_SET,
        sse_customer_key: str = ShapeBase.NOT_SET,
        sse_customer_key_md5: str = ShapeBase.NOT_SET,
        request_progress: shapes.RequestProgress = ShapeBase.NOT_SET,
    ) -> shapes.SelectObjectContentOutput:
        """
        This operation filters the contents of an Amazon S3 object based on a simple
        Structured Query Language (SQL) statement. In the request, along with the SQL
        expression, you must also specify a data serialization format (JSON or CSV) of
        the object. Amazon S3 uses this to parse object data into records, and returns
        only records that match the specified SQL expression. You must also specify the
        data serialization format for the response.
        """
        if _request is None:
            _params = {}
            if bucket is not ShapeBase.NOT_SET:
                _params['bucket'] = bucket
            if key is not ShapeBase.NOT_SET:
                _params['key'] = key
            if expression is not ShapeBase.NOT_SET:
                _params['expression'] = expression
            if expression_type is not ShapeBase.NOT_SET:
                _params['expression_type'] = expression_type
            if input_serialization is not ShapeBase.NOT_SET:
                _params['input_serialization'] = input_serialization
            if output_serialization is not ShapeBase.NOT_SET:
                _params['output_serialization'] = output_serialization
            if sse_customer_algorithm is not ShapeBase.NOT_SET:
                _params['sse_customer_algorithm'] = sse_customer_algorithm
            if sse_customer_key is not ShapeBase.NOT_SET:
                _params['sse_customer_key'] = sse_customer_key
            if sse_customer_key_md5 is not ShapeBase.NOT_SET:
                _params['sse_customer_key_md5'] = sse_customer_key_md5
            if request_progress is not ShapeBase.NOT_SET:
                _params['request_progress'] = request_progress
            _request = shapes.SelectObjectContentRequest(**_params)
        response = self._boto_client.select_object_content(**_request.to_boto())

        return shapes.SelectObjectContentOutput.from_boto(response)

    def upload_part(
        self,
        _request: shapes.UploadPartRequest = None,
        *,
        bucket: str,
        key: str,
        part_number: int,
        upload_id: str,
        body: typing.Any = ShapeBase.NOT_SET,
        content_length: int = ShapeBase.NOT_SET,
        content_md5: str = ShapeBase.NOT_SET,
        sse_customer_algorithm: str = ShapeBase.NOT_SET,
        sse_customer_key: str = ShapeBase.NOT_SET,
        sse_customer_key_md5: str = ShapeBase.NOT_SET,
        request_payer: typing.Union[str, shapes.RequestPayer] = ShapeBase.
        NOT_SET,
    ) -> shapes.UploadPartOutput:
        """
        Uploads a part in a multipart upload.

        **Note:** After you initiate multipart upload and upload one or more parts, you
        must either complete or abort multipart upload in order to stop getting charged
        for storage of the uploaded parts. Only after you either complete or abort
        multipart upload, Amazon S3 frees up the parts storage and stops charging you
        for the parts storage.
        """
        if _request is None:
            _params = {}
            if bucket is not ShapeBase.NOT_SET:
                _params['bucket'] = bucket
            if key is not ShapeBase.NOT_SET:
                _params['key'] = key
            if part_number is not ShapeBase.NOT_SET:
                _params['part_number'] = part_number
            if upload_id is not ShapeBase.NOT_SET:
                _params['upload_id'] = upload_id
            if body is not ShapeBase.NOT_SET:
                _params['body'] = body
            if content_length is not ShapeBase.NOT_SET:
                _params['content_length'] = content_length
            if content_md5 is not ShapeBase.NOT_SET:
                _params['content_md5'] = content_md5
            if sse_customer_algorithm is not ShapeBase.NOT_SET:
                _params['sse_customer_algorithm'] = sse_customer_algorithm
            if sse_customer_key is not ShapeBase.NOT_SET:
                _params['sse_customer_key'] = sse_customer_key
            if sse_customer_key_md5 is not ShapeBase.NOT_SET:
                _params['sse_customer_key_md5'] = sse_customer_key_md5
            if request_payer is not ShapeBase.NOT_SET:
                _params['request_payer'] = request_payer
            _request = shapes.UploadPartRequest(**_params)
        response = self._boto_client.upload_part(**_request.to_boto())

        return shapes.UploadPartOutput.from_boto(response)

    def upload_part_copy(
        self,
        _request: shapes.UploadPartCopyRequest = None,
        *,
        bucket: str,
        copy_source: str,
        key: str,
        part_number: int,
        upload_id: str,
        copy_source_if_match: str = ShapeBase.NOT_SET,
        copy_source_if_modified_since: datetime.datetime = ShapeBase.NOT_SET,
        copy_source_if_none_match: str = ShapeBase.NOT_SET,
        copy_source_if_unmodified_since: datetime.datetime = ShapeBase.NOT_SET,
        copy_source_range: str = ShapeBase.NOT_SET,
        sse_customer_algorithm: str = ShapeBase.NOT_SET,
        sse_customer_key: str = ShapeBase.NOT_SET,
        sse_customer_key_md5: str = ShapeBase.NOT_SET,
        copy_source_sse_customer_algorithm: str = ShapeBase.NOT_SET,
        copy_source_sse_customer_key: str = ShapeBase.NOT_SET,
        copy_source_sse_customer_key_md5: str = ShapeBase.NOT_SET,
        request_payer: typing.Union[str, shapes.RequestPayer] = ShapeBase.
        NOT_SET,
    ) -> shapes.UploadPartCopyOutput:
        """
        Uploads a part by copying data from an existing object as data source.
        """
        if _request is None:
            _params = {}
            if bucket is not ShapeBase.NOT_SET:
                _params['bucket'] = bucket
            if copy_source is not ShapeBase.NOT_SET:
                _params['copy_source'] = copy_source
            if key is not ShapeBase.NOT_SET:
                _params['key'] = key
            if part_number is not ShapeBase.NOT_SET:
                _params['part_number'] = part_number
            if upload_id is not ShapeBase.NOT_SET:
                _params['upload_id'] = upload_id
            if copy_source_if_match is not ShapeBase.NOT_SET:
                _params['copy_source_if_match'] = copy_source_if_match
            if copy_source_if_modified_since is not ShapeBase.NOT_SET:
                _params['copy_source_if_modified_since'
                       ] = copy_source_if_modified_since
            if copy_source_if_none_match is not ShapeBase.NOT_SET:
                _params['copy_source_if_none_match'] = copy_source_if_none_match
            if copy_source_if_unmodified_since is not ShapeBase.NOT_SET:
                _params['copy_source_if_unmodified_since'
                       ] = copy_source_if_unmodified_since
            if copy_source_range is not ShapeBase.NOT_SET:
                _params['copy_source_range'] = copy_source_range
            if sse_customer_algorithm is not ShapeBase.NOT_SET:
                _params['sse_customer_algorithm'] = sse_customer_algorithm
            if sse_customer_key is not ShapeBase.NOT_SET:
                _params['sse_customer_key'] = sse_customer_key
            if sse_customer_key_md5 is not ShapeBase.NOT_SET:
                _params['sse_customer_key_md5'] = sse_customer_key_md5
            if copy_source_sse_customer_algorithm is not ShapeBase.NOT_SET:
                _params['copy_source_sse_customer_algorithm'
                       ] = copy_source_sse_customer_algorithm
            if copy_source_sse_customer_key is not ShapeBase.NOT_SET:
                _params['copy_source_sse_customer_key'
                       ] = copy_source_sse_customer_key
            if copy_source_sse_customer_key_md5 is not ShapeBase.NOT_SET:
                _params['copy_source_sse_customer_key_md5'
                       ] = copy_source_sse_customer_key_md5
            if request_payer is not ShapeBase.NOT_SET:
                _params['request_payer'] = request_payer
            _request = shapes.UploadPartCopyRequest(**_params)
        response = self._boto_client.upload_part_copy(**_request.to_boto())

        return shapes.UploadPartCopyOutput.from_boto(response)
