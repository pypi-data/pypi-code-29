import datetime
import typing
import boto3
from autoboto import ClientBase, ShapeBase, OutputShapeBase
from . import shapes


class Client(ClientBase):
    def __init__(self, *args, **kwargs):
        super().__init__("ecr", *args, **kwargs)

    def batch_check_layer_availability(
        self,
        _request: shapes.BatchCheckLayerAvailabilityRequest = None,
        *,
        repository_name: str,
        layer_digests: typing.List[str],
        registry_id: str = ShapeBase.NOT_SET,
    ) -> shapes.BatchCheckLayerAvailabilityResponse:
        """
        Check the availability of multiple image layers in a specified registry and
        repository.

        This operation is used by the Amazon ECR proxy, and it is not intended for
        general use by customers for pulling and pushing images. In most cases, you
        should use the `docker` CLI to pull, tag, and push images.
        """
        if _request is None:
            _params = {}
            if repository_name is not ShapeBase.NOT_SET:
                _params['repository_name'] = repository_name
            if layer_digests is not ShapeBase.NOT_SET:
                _params['layer_digests'] = layer_digests
            if registry_id is not ShapeBase.NOT_SET:
                _params['registry_id'] = registry_id
            _request = shapes.BatchCheckLayerAvailabilityRequest(**_params)
        response = self._boto_client.batch_check_layer_availability(
            **_request.to_boto()
        )

        return shapes.BatchCheckLayerAvailabilityResponse.from_boto(response)

    def batch_delete_image(
        self,
        _request: shapes.BatchDeleteImageRequest = None,
        *,
        repository_name: str,
        image_ids: typing.List[shapes.ImageIdentifier],
        registry_id: str = ShapeBase.NOT_SET,
    ) -> shapes.BatchDeleteImageResponse:
        """
        Deletes a list of specified images within a specified repository. Images are
        specified with either `imageTag` or `imageDigest`.

        You can remove a tag from an image by specifying the image's tag in your
        request. When you remove the last tag from an image, the image is deleted from
        your repository.

        You can completely delete an image (and all of its tags) by specifying the
        image's digest in your request.
        """
        if _request is None:
            _params = {}
            if repository_name is not ShapeBase.NOT_SET:
                _params['repository_name'] = repository_name
            if image_ids is not ShapeBase.NOT_SET:
                _params['image_ids'] = image_ids
            if registry_id is not ShapeBase.NOT_SET:
                _params['registry_id'] = registry_id
            _request = shapes.BatchDeleteImageRequest(**_params)
        response = self._boto_client.batch_delete_image(**_request.to_boto())

        return shapes.BatchDeleteImageResponse.from_boto(response)

    def batch_get_image(
        self,
        _request: shapes.BatchGetImageRequest = None,
        *,
        repository_name: str,
        image_ids: typing.List[shapes.ImageIdentifier],
        registry_id: str = ShapeBase.NOT_SET,
        accepted_media_types: typing.List[str] = ShapeBase.NOT_SET,
    ) -> shapes.BatchGetImageResponse:
        """
        Gets detailed information for specified images within a specified repository.
        Images are specified with either `imageTag` or `imageDigest`.
        """
        if _request is None:
            _params = {}
            if repository_name is not ShapeBase.NOT_SET:
                _params['repository_name'] = repository_name
            if image_ids is not ShapeBase.NOT_SET:
                _params['image_ids'] = image_ids
            if registry_id is not ShapeBase.NOT_SET:
                _params['registry_id'] = registry_id
            if accepted_media_types is not ShapeBase.NOT_SET:
                _params['accepted_media_types'] = accepted_media_types
            _request = shapes.BatchGetImageRequest(**_params)
        response = self._boto_client.batch_get_image(**_request.to_boto())

        return shapes.BatchGetImageResponse.from_boto(response)

    def complete_layer_upload(
        self,
        _request: shapes.CompleteLayerUploadRequest = None,
        *,
        repository_name: str,
        upload_id: str,
        layer_digests: typing.List[str],
        registry_id: str = ShapeBase.NOT_SET,
    ) -> shapes.CompleteLayerUploadResponse:
        """
        Informs Amazon ECR that the image layer upload has completed for a specified
        registry, repository name, and upload ID. You can optionally provide a `sha256`
        digest of the image layer for data validation purposes.

        This operation is used by the Amazon ECR proxy, and it is not intended for
        general use by customers for pulling and pushing images. In most cases, you
        should use the `docker` CLI to pull, tag, and push images.
        """
        if _request is None:
            _params = {}
            if repository_name is not ShapeBase.NOT_SET:
                _params['repository_name'] = repository_name
            if upload_id is not ShapeBase.NOT_SET:
                _params['upload_id'] = upload_id
            if layer_digests is not ShapeBase.NOT_SET:
                _params['layer_digests'] = layer_digests
            if registry_id is not ShapeBase.NOT_SET:
                _params['registry_id'] = registry_id
            _request = shapes.CompleteLayerUploadRequest(**_params)
        response = self._boto_client.complete_layer_upload(**_request.to_boto())

        return shapes.CompleteLayerUploadResponse.from_boto(response)

    def create_repository(
        self,
        _request: shapes.CreateRepositoryRequest = None,
        *,
        repository_name: str,
    ) -> shapes.CreateRepositoryResponse:
        """
        Creates an image repository.
        """
        if _request is None:
            _params = {}
            if repository_name is not ShapeBase.NOT_SET:
                _params['repository_name'] = repository_name
            _request = shapes.CreateRepositoryRequest(**_params)
        response = self._boto_client.create_repository(**_request.to_boto())

        return shapes.CreateRepositoryResponse.from_boto(response)

    def delete_lifecycle_policy(
        self,
        _request: shapes.DeleteLifecyclePolicyRequest = None,
        *,
        repository_name: str,
        registry_id: str = ShapeBase.NOT_SET,
    ) -> shapes.DeleteLifecyclePolicyResponse:
        """
        Deletes the specified lifecycle policy.
        """
        if _request is None:
            _params = {}
            if repository_name is not ShapeBase.NOT_SET:
                _params['repository_name'] = repository_name
            if registry_id is not ShapeBase.NOT_SET:
                _params['registry_id'] = registry_id
            _request = shapes.DeleteLifecyclePolicyRequest(**_params)
        response = self._boto_client.delete_lifecycle_policy(
            **_request.to_boto()
        )

        return shapes.DeleteLifecyclePolicyResponse.from_boto(response)

    def delete_repository(
        self,
        _request: shapes.DeleteRepositoryRequest = None,
        *,
        repository_name: str,
        registry_id: str = ShapeBase.NOT_SET,
        force: bool = ShapeBase.NOT_SET,
    ) -> shapes.DeleteRepositoryResponse:
        """
        Deletes an existing image repository. If a repository contains images, you must
        use the `force` option to delete it.
        """
        if _request is None:
            _params = {}
            if repository_name is not ShapeBase.NOT_SET:
                _params['repository_name'] = repository_name
            if registry_id is not ShapeBase.NOT_SET:
                _params['registry_id'] = registry_id
            if force is not ShapeBase.NOT_SET:
                _params['force'] = force
            _request = shapes.DeleteRepositoryRequest(**_params)
        response = self._boto_client.delete_repository(**_request.to_boto())

        return shapes.DeleteRepositoryResponse.from_boto(response)

    def delete_repository_policy(
        self,
        _request: shapes.DeleteRepositoryPolicyRequest = None,
        *,
        repository_name: str,
        registry_id: str = ShapeBase.NOT_SET,
    ) -> shapes.DeleteRepositoryPolicyResponse:
        """
        Deletes the repository policy from a specified repository.
        """
        if _request is None:
            _params = {}
            if repository_name is not ShapeBase.NOT_SET:
                _params['repository_name'] = repository_name
            if registry_id is not ShapeBase.NOT_SET:
                _params['registry_id'] = registry_id
            _request = shapes.DeleteRepositoryPolicyRequest(**_params)
        response = self._boto_client.delete_repository_policy(
            **_request.to_boto()
        )

        return shapes.DeleteRepositoryPolicyResponse.from_boto(response)

    def describe_images(
        self,
        _request: shapes.DescribeImagesRequest = None,
        *,
        repository_name: str,
        registry_id: str = ShapeBase.NOT_SET,
        image_ids: typing.List[shapes.ImageIdentifier] = ShapeBase.NOT_SET,
        next_token: str = ShapeBase.NOT_SET,
        max_results: int = ShapeBase.NOT_SET,
        filter: shapes.DescribeImagesFilter = ShapeBase.NOT_SET,
    ) -> shapes.DescribeImagesResponse:
        """
        Returns metadata about the images in a repository, including image size, image
        tags, and creation date.

        Beginning with Docker version 1.9, the Docker client compresses image layers
        before pushing them to a V2 Docker registry. The output of the `docker images`
        command shows the uncompressed image size, so it may return a larger image size
        than the image sizes returned by DescribeImages.
        """
        if _request is None:
            _params = {}
            if repository_name is not ShapeBase.NOT_SET:
                _params['repository_name'] = repository_name
            if registry_id is not ShapeBase.NOT_SET:
                _params['registry_id'] = registry_id
            if image_ids is not ShapeBase.NOT_SET:
                _params['image_ids'] = image_ids
            if next_token is not ShapeBase.NOT_SET:
                _params['next_token'] = next_token
            if max_results is not ShapeBase.NOT_SET:
                _params['max_results'] = max_results
            if filter is not ShapeBase.NOT_SET:
                _params['filter'] = filter
            _request = shapes.DescribeImagesRequest(**_params)
        paginator = self.get_paginator("describe_images").paginate(
            **_request.to_boto()
        )
        page_generator = (page for page in paginator)
        first_page = next(page_generator)
        result = shapes.DescribeImagesResponse.from_boto(first_page)
        result._page_iterator = page_generator
        return result

        return shapes.DescribeImagesResponse.from_boto(response)

    def describe_repositories(
        self,
        _request: shapes.DescribeRepositoriesRequest = None,
        *,
        registry_id: str = ShapeBase.NOT_SET,
        repository_names: typing.List[str] = ShapeBase.NOT_SET,
        next_token: str = ShapeBase.NOT_SET,
        max_results: int = ShapeBase.NOT_SET,
    ) -> shapes.DescribeRepositoriesResponse:
        """
        Describes image repositories in a registry.
        """
        if _request is None:
            _params = {}
            if registry_id is not ShapeBase.NOT_SET:
                _params['registry_id'] = registry_id
            if repository_names is not ShapeBase.NOT_SET:
                _params['repository_names'] = repository_names
            if next_token is not ShapeBase.NOT_SET:
                _params['next_token'] = next_token
            if max_results is not ShapeBase.NOT_SET:
                _params['max_results'] = max_results
            _request = shapes.DescribeRepositoriesRequest(**_params)
        paginator = self.get_paginator("describe_repositories").paginate(
            **_request.to_boto()
        )
        page_generator = (page for page in paginator)
        first_page = next(page_generator)
        result = shapes.DescribeRepositoriesResponse.from_boto(first_page)
        result._page_iterator = page_generator
        return result

        return shapes.DescribeRepositoriesResponse.from_boto(response)

    def get_authorization_token(
        self,
        _request: shapes.GetAuthorizationTokenRequest = None,
        *,
        registry_ids: typing.List[str] = ShapeBase.NOT_SET,
    ) -> shapes.GetAuthorizationTokenResponse:
        """
        Retrieves a token that is valid for a specified registry for 12 hours. This
        command allows you to use the `docker` CLI to push and pull images with Amazon
        ECR. If you do not specify a registry, the default registry is assumed.

        The `authorizationToken` returned for each registry specified is a base64
        encoded string that can be decoded and used in a `docker login` command to
        authenticate to a registry. The AWS CLI offers an `aws ecr get-login` command
        that simplifies the login process.
        """
        if _request is None:
            _params = {}
            if registry_ids is not ShapeBase.NOT_SET:
                _params['registry_ids'] = registry_ids
            _request = shapes.GetAuthorizationTokenRequest(**_params)
        response = self._boto_client.get_authorization_token(
            **_request.to_boto()
        )

        return shapes.GetAuthorizationTokenResponse.from_boto(response)

    def get_download_url_for_layer(
        self,
        _request: shapes.GetDownloadUrlForLayerRequest = None,
        *,
        repository_name: str,
        layer_digest: str,
        registry_id: str = ShapeBase.NOT_SET,
    ) -> shapes.GetDownloadUrlForLayerResponse:
        """
        Retrieves the pre-signed Amazon S3 download URL corresponding to an image layer.
        You can only get URLs for image layers that are referenced in an image.

        This operation is used by the Amazon ECR proxy, and it is not intended for
        general use by customers for pulling and pushing images. In most cases, you
        should use the `docker` CLI to pull, tag, and push images.
        """
        if _request is None:
            _params = {}
            if repository_name is not ShapeBase.NOT_SET:
                _params['repository_name'] = repository_name
            if layer_digest is not ShapeBase.NOT_SET:
                _params['layer_digest'] = layer_digest
            if registry_id is not ShapeBase.NOT_SET:
                _params['registry_id'] = registry_id
            _request = shapes.GetDownloadUrlForLayerRequest(**_params)
        response = self._boto_client.get_download_url_for_layer(
            **_request.to_boto()
        )

        return shapes.GetDownloadUrlForLayerResponse.from_boto(response)

    def get_lifecycle_policy(
        self,
        _request: shapes.GetLifecyclePolicyRequest = None,
        *,
        repository_name: str,
        registry_id: str = ShapeBase.NOT_SET,
    ) -> shapes.GetLifecyclePolicyResponse:
        """
        Retrieves the specified lifecycle policy.
        """
        if _request is None:
            _params = {}
            if repository_name is not ShapeBase.NOT_SET:
                _params['repository_name'] = repository_name
            if registry_id is not ShapeBase.NOT_SET:
                _params['registry_id'] = registry_id
            _request = shapes.GetLifecyclePolicyRequest(**_params)
        response = self._boto_client.get_lifecycle_policy(**_request.to_boto())

        return shapes.GetLifecyclePolicyResponse.from_boto(response)

    def get_lifecycle_policy_preview(
        self,
        _request: shapes.GetLifecyclePolicyPreviewRequest = None,
        *,
        repository_name: str,
        registry_id: str = ShapeBase.NOT_SET,
        image_ids: typing.List[shapes.ImageIdentifier] = ShapeBase.NOT_SET,
        next_token: str = ShapeBase.NOT_SET,
        max_results: int = ShapeBase.NOT_SET,
        filter: shapes.LifecyclePolicyPreviewFilter = ShapeBase.NOT_SET,
    ) -> shapes.GetLifecyclePolicyPreviewResponse:
        """
        Retrieves the results of the specified lifecycle policy preview request.
        """
        if _request is None:
            _params = {}
            if repository_name is not ShapeBase.NOT_SET:
                _params['repository_name'] = repository_name
            if registry_id is not ShapeBase.NOT_SET:
                _params['registry_id'] = registry_id
            if image_ids is not ShapeBase.NOT_SET:
                _params['image_ids'] = image_ids
            if next_token is not ShapeBase.NOT_SET:
                _params['next_token'] = next_token
            if max_results is not ShapeBase.NOT_SET:
                _params['max_results'] = max_results
            if filter is not ShapeBase.NOT_SET:
                _params['filter'] = filter
            _request = shapes.GetLifecyclePolicyPreviewRequest(**_params)
        response = self._boto_client.get_lifecycle_policy_preview(
            **_request.to_boto()
        )

        return shapes.GetLifecyclePolicyPreviewResponse.from_boto(response)

    def get_repository_policy(
        self,
        _request: shapes.GetRepositoryPolicyRequest = None,
        *,
        repository_name: str,
        registry_id: str = ShapeBase.NOT_SET,
    ) -> shapes.GetRepositoryPolicyResponse:
        """
        Retrieves the repository policy for a specified repository.
        """
        if _request is None:
            _params = {}
            if repository_name is not ShapeBase.NOT_SET:
                _params['repository_name'] = repository_name
            if registry_id is not ShapeBase.NOT_SET:
                _params['registry_id'] = registry_id
            _request = shapes.GetRepositoryPolicyRequest(**_params)
        response = self._boto_client.get_repository_policy(**_request.to_boto())

        return shapes.GetRepositoryPolicyResponse.from_boto(response)

    def initiate_layer_upload(
        self,
        _request: shapes.InitiateLayerUploadRequest = None,
        *,
        repository_name: str,
        registry_id: str = ShapeBase.NOT_SET,
    ) -> shapes.InitiateLayerUploadResponse:
        """
        Notify Amazon ECR that you intend to upload an image layer.

        This operation is used by the Amazon ECR proxy, and it is not intended for
        general use by customers for pulling and pushing images. In most cases, you
        should use the `docker` CLI to pull, tag, and push images.
        """
        if _request is None:
            _params = {}
            if repository_name is not ShapeBase.NOT_SET:
                _params['repository_name'] = repository_name
            if registry_id is not ShapeBase.NOT_SET:
                _params['registry_id'] = registry_id
            _request = shapes.InitiateLayerUploadRequest(**_params)
        response = self._boto_client.initiate_layer_upload(**_request.to_boto())

        return shapes.InitiateLayerUploadResponse.from_boto(response)

    def list_images(
        self,
        _request: shapes.ListImagesRequest = None,
        *,
        repository_name: str,
        registry_id: str = ShapeBase.NOT_SET,
        next_token: str = ShapeBase.NOT_SET,
        max_results: int = ShapeBase.NOT_SET,
        filter: shapes.ListImagesFilter = ShapeBase.NOT_SET,
    ) -> shapes.ListImagesResponse:
        """
        Lists all the image IDs for a given repository.

        You can filter images based on whether or not they are tagged by setting the
        `tagStatus` parameter to `TAGGED` or `UNTAGGED`. For example, you can filter
        your results to return only `UNTAGGED` images and then pipe that result to a
        BatchDeleteImage operation to delete them. Or, you can filter your results to
        return only `TAGGED` images to list all of the tags in your repository.
        """
        if _request is None:
            _params = {}
            if repository_name is not ShapeBase.NOT_SET:
                _params['repository_name'] = repository_name
            if registry_id is not ShapeBase.NOT_SET:
                _params['registry_id'] = registry_id
            if next_token is not ShapeBase.NOT_SET:
                _params['next_token'] = next_token
            if max_results is not ShapeBase.NOT_SET:
                _params['max_results'] = max_results
            if filter is not ShapeBase.NOT_SET:
                _params['filter'] = filter
            _request = shapes.ListImagesRequest(**_params)
        paginator = self.get_paginator("list_images").paginate(
            **_request.to_boto()
        )
        page_generator = (page for page in paginator)
        first_page = next(page_generator)
        result = shapes.ListImagesResponse.from_boto(first_page)
        result._page_iterator = page_generator
        return result

        return shapes.ListImagesResponse.from_boto(response)

    def put_image(
        self,
        _request: shapes.PutImageRequest = None,
        *,
        repository_name: str,
        image_manifest: str,
        registry_id: str = ShapeBase.NOT_SET,
        image_tag: str = ShapeBase.NOT_SET,
    ) -> shapes.PutImageResponse:
        """
        Creates or updates the image manifest and tags associated with an image.

        This operation is used by the Amazon ECR proxy, and it is not intended for
        general use by customers for pulling and pushing images. In most cases, you
        should use the `docker` CLI to pull, tag, and push images.
        """
        if _request is None:
            _params = {}
            if repository_name is not ShapeBase.NOT_SET:
                _params['repository_name'] = repository_name
            if image_manifest is not ShapeBase.NOT_SET:
                _params['image_manifest'] = image_manifest
            if registry_id is not ShapeBase.NOT_SET:
                _params['registry_id'] = registry_id
            if image_tag is not ShapeBase.NOT_SET:
                _params['image_tag'] = image_tag
            _request = shapes.PutImageRequest(**_params)
        response = self._boto_client.put_image(**_request.to_boto())

        return shapes.PutImageResponse.from_boto(response)

    def put_lifecycle_policy(
        self,
        _request: shapes.PutLifecyclePolicyRequest = None,
        *,
        repository_name: str,
        lifecycle_policy_text: str,
        registry_id: str = ShapeBase.NOT_SET,
    ) -> shapes.PutLifecyclePolicyResponse:
        """
        Creates or updates a lifecycle policy. For information about lifecycle policy
        syntax, see [Lifecycle Policy
        Template](http://docs.aws.amazon.com/AmazonECR/latest/userguide/LifecyclePolicies.html).
        """
        if _request is None:
            _params = {}
            if repository_name is not ShapeBase.NOT_SET:
                _params['repository_name'] = repository_name
            if lifecycle_policy_text is not ShapeBase.NOT_SET:
                _params['lifecycle_policy_text'] = lifecycle_policy_text
            if registry_id is not ShapeBase.NOT_SET:
                _params['registry_id'] = registry_id
            _request = shapes.PutLifecyclePolicyRequest(**_params)
        response = self._boto_client.put_lifecycle_policy(**_request.to_boto())

        return shapes.PutLifecyclePolicyResponse.from_boto(response)

    def set_repository_policy(
        self,
        _request: shapes.SetRepositoryPolicyRequest = None,
        *,
        repository_name: str,
        policy_text: str,
        registry_id: str = ShapeBase.NOT_SET,
        force: bool = ShapeBase.NOT_SET,
    ) -> shapes.SetRepositoryPolicyResponse:
        """
        Applies a repository policy on a specified repository to control access
        permissions.
        """
        if _request is None:
            _params = {}
            if repository_name is not ShapeBase.NOT_SET:
                _params['repository_name'] = repository_name
            if policy_text is not ShapeBase.NOT_SET:
                _params['policy_text'] = policy_text
            if registry_id is not ShapeBase.NOT_SET:
                _params['registry_id'] = registry_id
            if force is not ShapeBase.NOT_SET:
                _params['force'] = force
            _request = shapes.SetRepositoryPolicyRequest(**_params)
        response = self._boto_client.set_repository_policy(**_request.to_boto())

        return shapes.SetRepositoryPolicyResponse.from_boto(response)

    def start_lifecycle_policy_preview(
        self,
        _request: shapes.StartLifecyclePolicyPreviewRequest = None,
        *,
        repository_name: str,
        registry_id: str = ShapeBase.NOT_SET,
        lifecycle_policy_text: str = ShapeBase.NOT_SET,
    ) -> shapes.StartLifecyclePolicyPreviewResponse:
        """
        Starts a preview of the specified lifecycle policy. This allows you to see the
        results before creating the lifecycle policy.
        """
        if _request is None:
            _params = {}
            if repository_name is not ShapeBase.NOT_SET:
                _params['repository_name'] = repository_name
            if registry_id is not ShapeBase.NOT_SET:
                _params['registry_id'] = registry_id
            if lifecycle_policy_text is not ShapeBase.NOT_SET:
                _params['lifecycle_policy_text'] = lifecycle_policy_text
            _request = shapes.StartLifecyclePolicyPreviewRequest(**_params)
        response = self._boto_client.start_lifecycle_policy_preview(
            **_request.to_boto()
        )

        return shapes.StartLifecyclePolicyPreviewResponse.from_boto(response)

    def upload_layer_part(
        self,
        _request: shapes.UploadLayerPartRequest = None,
        *,
        repository_name: str,
        upload_id: str,
        part_first_byte: int,
        part_last_byte: int,
        layer_part_blob: typing.Any,
        registry_id: str = ShapeBase.NOT_SET,
    ) -> shapes.UploadLayerPartResponse:
        """
        Uploads an image layer part to Amazon ECR.

        This operation is used by the Amazon ECR proxy, and it is not intended for
        general use by customers for pulling and pushing images. In most cases, you
        should use the `docker` CLI to pull, tag, and push images.
        """
        if _request is None:
            _params = {}
            if repository_name is not ShapeBase.NOT_SET:
                _params['repository_name'] = repository_name
            if upload_id is not ShapeBase.NOT_SET:
                _params['upload_id'] = upload_id
            if part_first_byte is not ShapeBase.NOT_SET:
                _params['part_first_byte'] = part_first_byte
            if part_last_byte is not ShapeBase.NOT_SET:
                _params['part_last_byte'] = part_last_byte
            if layer_part_blob is not ShapeBase.NOT_SET:
                _params['layer_part_blob'] = layer_part_blob
            if registry_id is not ShapeBase.NOT_SET:
                _params['registry_id'] = registry_id
            _request = shapes.UploadLayerPartRequest(**_params)
        response = self._boto_client.upload_layer_part(**_request.to_boto())

        return shapes.UploadLayerPartResponse.from_boto(response)
