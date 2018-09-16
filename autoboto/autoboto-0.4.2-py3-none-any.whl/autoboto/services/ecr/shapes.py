import datetime
import typing
from autoboto import ShapeBase, OutputShapeBase, TypeInfo
import botocore.response
import dataclasses


@dataclasses.dataclass
class AuthorizationData(ShapeBase):
    """
    An object representing authorization data for an Amazon ECR registry.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "authorization_token",
                "authorizationToken",
                TypeInfo(str),
            ),
            (
                "expires_at",
                "expiresAt",
                TypeInfo(datetime.datetime),
            ),
            (
                "proxy_endpoint",
                "proxyEndpoint",
                TypeInfo(str),
            ),
        ]

    # A base64-encoded string that contains authorization data for the specified
    # Amazon ECR registry. When the string is decoded, it is presented in the
    # format `user:password` for private registry authentication using `docker
    # login`.
    authorization_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The Unix time in seconds and milliseconds when the authorization token
    # expires. Authorization tokens are valid for 12 hours.
    expires_at: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The registry URL to use for this authorization token in a `docker login`
    # command. The Amazon ECR registry URL format is
    # `https://aws_account_id.dkr.ecr.region.amazonaws.com`. For example,
    # `https://012345678910.dkr.ecr.us-east-1.amazonaws.com`..
    proxy_endpoint: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class BatchCheckLayerAvailabilityRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "repository_name",
                "repositoryName",
                TypeInfo(str),
            ),
            (
                "layer_digests",
                "layerDigests",
                TypeInfo(typing.List[str]),
            ),
            (
                "registry_id",
                "registryId",
                TypeInfo(str),
            ),
        ]

    # The name of the repository that is associated with the image layers to
    # check.
    repository_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The digests of the image layers to check.
    layer_digests: typing.List[str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The AWS account ID associated with the registry that contains the image
    # layers to check. If you do not specify a registry, the default registry is
    # assumed.
    registry_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class BatchCheckLayerAvailabilityResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "layers",
                "layers",
                TypeInfo(typing.List[Layer]),
            ),
            (
                "failures",
                "failures",
                TypeInfo(typing.List[LayerFailure]),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A list of image layer objects corresponding to the image layer references
    # in the request.
    layers: typing.List["Layer"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Any failures associated with the call.
    failures: typing.List["LayerFailure"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class BatchDeleteImageRequest(ShapeBase):
    """
    Deletes specified images within a specified repository. Images are specified
    with either the `imageTag` or `imageDigest`.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "repository_name",
                "repositoryName",
                TypeInfo(str),
            ),
            (
                "image_ids",
                "imageIds",
                TypeInfo(typing.List[ImageIdentifier]),
            ),
            (
                "registry_id",
                "registryId",
                TypeInfo(str),
            ),
        ]

    # The repository that contains the image to delete.
    repository_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A list of image ID references that correspond to images to delete. The
    # format of the `imageIds` reference is `imageTag=tag` or
    # `imageDigest=digest`.
    image_ids: typing.List["ImageIdentifier"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The AWS account ID associated with the registry that contains the image to
    # delete. If you do not specify a registry, the default registry is assumed.
    registry_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class BatchDeleteImageResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "image_ids",
                "imageIds",
                TypeInfo(typing.List[ImageIdentifier]),
            ),
            (
                "failures",
                "failures",
                TypeInfo(typing.List[ImageFailure]),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The image IDs of the deleted images.
    image_ids: typing.List["ImageIdentifier"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Any failures associated with the call.
    failures: typing.List["ImageFailure"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class BatchGetImageRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "repository_name",
                "repositoryName",
                TypeInfo(str),
            ),
            (
                "image_ids",
                "imageIds",
                TypeInfo(typing.List[ImageIdentifier]),
            ),
            (
                "registry_id",
                "registryId",
                TypeInfo(str),
            ),
            (
                "accepted_media_types",
                "acceptedMediaTypes",
                TypeInfo(typing.List[str]),
            ),
        ]

    # The repository that contains the images to describe.
    repository_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A list of image ID references that correspond to images to describe. The
    # format of the `imageIds` reference is `imageTag=tag` or
    # `imageDigest=digest`.
    image_ids: typing.List["ImageIdentifier"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The AWS account ID associated with the registry that contains the images to
    # describe. If you do not specify a registry, the default registry is
    # assumed.
    registry_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The accepted media types for the request.

    # Valid values: `application/vnd.docker.distribution.manifest.v1+json` |
    # `application/vnd.docker.distribution.manifest.v2+json` |
    # `application/vnd.oci.image.manifest.v1+json`
    accepted_media_types: typing.List[str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class BatchGetImageResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "images",
                "images",
                TypeInfo(typing.List[Image]),
            ),
            (
                "failures",
                "failures",
                TypeInfo(typing.List[ImageFailure]),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A list of image objects corresponding to the image references in the
    # request.
    images: typing.List["Image"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Any failures associated with the call.
    failures: typing.List["ImageFailure"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class CompleteLayerUploadRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "repository_name",
                "repositoryName",
                TypeInfo(str),
            ),
            (
                "upload_id",
                "uploadId",
                TypeInfo(str),
            ),
            (
                "layer_digests",
                "layerDigests",
                TypeInfo(typing.List[str]),
            ),
            (
                "registry_id",
                "registryId",
                TypeInfo(str),
            ),
        ]

    # The name of the repository to associate with the image layer.
    repository_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The upload ID from a previous InitiateLayerUpload operation to associate
    # with the image layer.
    upload_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The `sha256` digest of the image layer.
    layer_digests: typing.List[str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The AWS account ID associated with the registry to which to upload layers.
    # If you do not specify a registry, the default registry is assumed.
    registry_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class CompleteLayerUploadResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "registry_id",
                "registryId",
                TypeInfo(str),
            ),
            (
                "repository_name",
                "repositoryName",
                TypeInfo(str),
            ),
            (
                "upload_id",
                "uploadId",
                TypeInfo(str),
            ),
            (
                "layer_digest",
                "layerDigest",
                TypeInfo(str),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The registry ID associated with the request.
    registry_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The repository name associated with the request.
    repository_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The upload ID associated with the layer.
    upload_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The `sha256` digest of the image layer.
    layer_digest: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class CreateRepositoryRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "repository_name",
                "repositoryName",
                TypeInfo(str),
            ),
        ]

    # The name to use for the repository. The repository name may be specified on
    # its own (such as `nginx-web-app`) or it can be prepended with a namespace
    # to group the repository into a category (such as `project-a/nginx-web-
    # app`).
    repository_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class CreateRepositoryResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "repository",
                "repository",
                TypeInfo(Repository),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The repository that was created.
    repository: "Repository" = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DeleteLifecyclePolicyRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "repository_name",
                "repositoryName",
                TypeInfo(str),
            ),
            (
                "registry_id",
                "registryId",
                TypeInfo(str),
            ),
        ]

    # The name of the repository.
    repository_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The AWS account ID associated with the registry that contains the
    # repository. If you do not specify a registry, the default registry is
    # assumed.
    registry_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DeleteLifecyclePolicyResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "registry_id",
                "registryId",
                TypeInfo(str),
            ),
            (
                "repository_name",
                "repositoryName",
                TypeInfo(str),
            ),
            (
                "lifecycle_policy_text",
                "lifecyclePolicyText",
                TypeInfo(str),
            ),
            (
                "last_evaluated_at",
                "lastEvaluatedAt",
                TypeInfo(datetime.datetime),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The registry ID associated with the request.
    registry_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The repository name associated with the request.
    repository_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The JSON lifecycle policy text.
    lifecycle_policy_text: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The time stamp of the last time that the lifecycle policy was run.
    last_evaluated_at: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class DeleteRepositoryPolicyRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "repository_name",
                "repositoryName",
                TypeInfo(str),
            ),
            (
                "registry_id",
                "registryId",
                TypeInfo(str),
            ),
        ]

    # The name of the repository that is associated with the repository policy to
    # delete.
    repository_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The AWS account ID associated with the registry that contains the
    # repository policy to delete. If you do not specify a registry, the default
    # registry is assumed.
    registry_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DeleteRepositoryPolicyResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "registry_id",
                "registryId",
                TypeInfo(str),
            ),
            (
                "repository_name",
                "repositoryName",
                TypeInfo(str),
            ),
            (
                "policy_text",
                "policyText",
                TypeInfo(str),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The registry ID associated with the request.
    registry_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The repository name associated with the request.
    repository_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The JSON repository policy that was deleted from the repository.
    policy_text: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DeleteRepositoryRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "repository_name",
                "repositoryName",
                TypeInfo(str),
            ),
            (
                "registry_id",
                "registryId",
                TypeInfo(str),
            ),
            (
                "force",
                "force",
                TypeInfo(bool),
            ),
        ]

    # The name of the repository to delete.
    repository_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The AWS account ID associated with the registry that contains the
    # repository to delete. If you do not specify a registry, the default
    # registry is assumed.
    registry_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # If a repository contains images, forces the deletion.
    force: bool = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DeleteRepositoryResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "repository",
                "repository",
                TypeInfo(Repository),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The repository that was deleted.
    repository: "Repository" = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DescribeImagesFilter(ShapeBase):
    """
    An object representing a filter on a DescribeImages operation.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "tag_status",
                "tagStatus",
                TypeInfo(typing.Union[str, TagStatus]),
            ),
        ]

    # The tag status with which to filter your DescribeImages results. You can
    # filter results based on whether they are `TAGGED` or `UNTAGGED`.
    tag_status: typing.Union[str, "TagStatus"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class DescribeImagesRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "repository_name",
                "repositoryName",
                TypeInfo(str),
            ),
            (
                "registry_id",
                "registryId",
                TypeInfo(str),
            ),
            (
                "image_ids",
                "imageIds",
                TypeInfo(typing.List[ImageIdentifier]),
            ),
            (
                "next_token",
                "nextToken",
                TypeInfo(str),
            ),
            (
                "max_results",
                "maxResults",
                TypeInfo(int),
            ),
            (
                "filter",
                "filter",
                TypeInfo(DescribeImagesFilter),
            ),
        ]

    # A list of repositories to describe. If this parameter is omitted, then all
    # repositories in a registry are described.
    repository_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The AWS account ID associated with the registry that contains the
    # repository in which to describe images. If you do not specify a registry,
    # the default registry is assumed.
    registry_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The list of image IDs for the requested repository.
    image_ids: typing.List["ImageIdentifier"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The `nextToken` value returned from a previous paginated `DescribeImages`
    # request where `maxResults` was used and the results exceeded the value of
    # that parameter. Pagination continues from the end of the previous results
    # that returned the `nextToken` value. This value is `null` when there are no
    # more results to return. This option cannot be used when you specify images
    # with `imageIds`.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The maximum number of repository results returned by `DescribeImages` in
    # paginated output. When this parameter is used, `DescribeImages` only
    # returns `maxResults` results in a single page along with a `nextToken`
    # response element. The remaining results of the initial request can be seen
    # by sending another `DescribeImages` request with the returned `nextToken`
    # value. This value can be between 1 and 100. If this parameter is not used,
    # then `DescribeImages` returns up to 100 results and a `nextToken` value, if
    # applicable. This option cannot be used when you specify images with
    # `imageIds`.
    max_results: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The filter key and value with which to filter your `DescribeImages`
    # results.
    filter: "DescribeImagesFilter" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class DescribeImagesResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "image_details",
                "imageDetails",
                TypeInfo(typing.List[ImageDetail]),
            ),
            (
                "next_token",
                "nextToken",
                TypeInfo(str),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A list of ImageDetail objects that contain data about the image.
    image_details: typing.List["ImageDetail"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The `nextToken` value to include in a future `DescribeImages` request. When
    # the results of a `DescribeImages` request exceed `maxResults`, this value
    # can be used to retrieve the next page of results. This value is `null` when
    # there are no more results to return.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    def paginate(self,
                ) -> typing.Generator["DescribeImagesResponse", None, None]:
        yield from super()._paginate()


@dataclasses.dataclass
class DescribeRepositoriesRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "registry_id",
                "registryId",
                TypeInfo(str),
            ),
            (
                "repository_names",
                "repositoryNames",
                TypeInfo(typing.List[str]),
            ),
            (
                "next_token",
                "nextToken",
                TypeInfo(str),
            ),
            (
                "max_results",
                "maxResults",
                TypeInfo(int),
            ),
        ]

    # The AWS account ID associated with the registry that contains the
    # repositories to be described. If you do not specify a registry, the default
    # registry is assumed.
    registry_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A list of repositories to describe. If this parameter is omitted, then all
    # repositories in a registry are described.
    repository_names: typing.List[str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The `nextToken` value returned from a previous paginated
    # `DescribeRepositories` request where `maxResults` was used and the results
    # exceeded the value of that parameter. Pagination continues from the end of
    # the previous results that returned the `nextToken` value. This value is
    # `null` when there are no more results to return. This option cannot be used
    # when you specify repositories with `repositoryNames`.

    # This token should be treated as an opaque identifier that is only used to
    # retrieve the next items in a list and not for other programmatic purposes.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The maximum number of repository results returned by `DescribeRepositories`
    # in paginated output. When this parameter is used, `DescribeRepositories`
    # only returns `maxResults` results in a single page along with a `nextToken`
    # response element. The remaining results of the initial request can be seen
    # by sending another `DescribeRepositories` request with the returned
    # `nextToken` value. This value can be between 1 and 100. If this parameter
    # is not used, then `DescribeRepositories` returns up to 100 results and a
    # `nextToken` value, if applicable. This option cannot be used when you
    # specify repositories with `repositoryNames`.
    max_results: int = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DescribeRepositoriesResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "repositories",
                "repositories",
                TypeInfo(typing.List[Repository]),
            ),
            (
                "next_token",
                "nextToken",
                TypeInfo(str),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A list of repository objects corresponding to valid repositories.
    repositories: typing.List["Repository"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The `nextToken` value to include in a future `DescribeRepositories`
    # request. When the results of a `DescribeRepositories` request exceed
    # `maxResults`, this value can be used to retrieve the next page of results.
    # This value is `null` when there are no more results to return.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    def paginate(
        self,
    ) -> typing.Generator["DescribeRepositoriesResponse", None, None]:
        yield from super()._paginate()


@dataclasses.dataclass
class EmptyUploadException(ShapeBase):
    """
    The specified layer upload does not contain any layer parts.
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

    # The error message associated with the exception.
    message: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class GetAuthorizationTokenRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "registry_ids",
                "registryIds",
                TypeInfo(typing.List[str]),
            ),
        ]

    # A list of AWS account IDs that are associated with the registries for which
    # to get authorization tokens. If you do not specify a registry, the default
    # registry is assumed.
    registry_ids: typing.List[str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class GetAuthorizationTokenResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "authorization_data",
                "authorizationData",
                TypeInfo(typing.List[AuthorizationData]),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A list of authorization token data objects that correspond to the
    # `registryIds` values in the request.
    authorization_data: typing.List["AuthorizationData"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class GetDownloadUrlForLayerRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "repository_name",
                "repositoryName",
                TypeInfo(str),
            ),
            (
                "layer_digest",
                "layerDigest",
                TypeInfo(str),
            ),
            (
                "registry_id",
                "registryId",
                TypeInfo(str),
            ),
        ]

    # The name of the repository that is associated with the image layer to
    # download.
    repository_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The digest of the image layer to download.
    layer_digest: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The AWS account ID associated with the registry that contains the image
    # layer to download. If you do not specify a registry, the default registry
    # is assumed.
    registry_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class GetDownloadUrlForLayerResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "download_url",
                "downloadUrl",
                TypeInfo(str),
            ),
            (
                "layer_digest",
                "layerDigest",
                TypeInfo(str),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The pre-signed Amazon S3 download URL for the requested layer.
    download_url: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The digest of the image layer to download.
    layer_digest: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class GetLifecyclePolicyPreviewRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "repository_name",
                "repositoryName",
                TypeInfo(str),
            ),
            (
                "registry_id",
                "registryId",
                TypeInfo(str),
            ),
            (
                "image_ids",
                "imageIds",
                TypeInfo(typing.List[ImageIdentifier]),
            ),
            (
                "next_token",
                "nextToken",
                TypeInfo(str),
            ),
            (
                "max_results",
                "maxResults",
                TypeInfo(int),
            ),
            (
                "filter",
                "filter",
                TypeInfo(LifecyclePolicyPreviewFilter),
            ),
        ]

    # The name of the repository.
    repository_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The AWS account ID associated with the registry that contains the
    # repository. If you do not specify a registry, the default registry is
    # assumed.
    registry_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The list of imageIDs to be included.
    image_ids: typing.List["ImageIdentifier"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The `nextToken` value returned from a previous paginated
    # `GetLifecyclePolicyPreviewRequest` request where `maxResults` was used and
    # the results exceeded the value of that parameter. Pagination continues from
    # the end of the previous results that returned the `nextToken` value. This
    # value is `null` when there are no more results to return. This option
    # cannot be used when you specify images with `imageIds`.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The maximum number of repository results returned by
    # `GetLifecyclePolicyPreviewRequest` in paginated output. When this parameter
    # is used, `GetLifecyclePolicyPreviewRequest` only returns `maxResults`
    # results in a single page along with a `nextToken` response element. The
    # remaining results of the initial request can be seen by sending another
    # `GetLifecyclePolicyPreviewRequest` request with the returned `nextToken`
    # value. This value can be between 1 and 100. If this parameter is not used,
    # then `GetLifecyclePolicyPreviewRequest` returns up to 100 results and a
    # `nextToken` value, if applicable. This option cannot be used when you
    # specify images with `imageIds`.
    max_results: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # An optional parameter that filters results based on image tag status and
    # all tags, if tagged.
    filter: "LifecyclePolicyPreviewFilter" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class GetLifecyclePolicyPreviewResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "registry_id",
                "registryId",
                TypeInfo(str),
            ),
            (
                "repository_name",
                "repositoryName",
                TypeInfo(str),
            ),
            (
                "lifecycle_policy_text",
                "lifecyclePolicyText",
                TypeInfo(str),
            ),
            (
                "status",
                "status",
                TypeInfo(typing.Union[str, LifecyclePolicyPreviewStatus]),
            ),
            (
                "next_token",
                "nextToken",
                TypeInfo(str),
            ),
            (
                "preview_results",
                "previewResults",
                TypeInfo(typing.List[LifecyclePolicyPreviewResult]),
            ),
            (
                "summary",
                "summary",
                TypeInfo(LifecyclePolicyPreviewSummary),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The registry ID associated with the request.
    registry_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The repository name associated with the request.
    repository_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The JSON lifecycle policy text.
    lifecycle_policy_text: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The status of the lifecycle policy preview request.
    status: typing.Union[str, "LifecyclePolicyPreviewStatus"
                        ] = dataclasses.field(
                            default=ShapeBase.NOT_SET,
                        )

    # The `nextToken` value to include in a future `GetLifecyclePolicyPreview`
    # request. When the results of a `GetLifecyclePolicyPreview` request exceed
    # `maxResults`, this value can be used to retrieve the next page of results.
    # This value is `null` when there are no more results to return.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The results of the lifecycle policy preview request.
    preview_results: typing.List["LifecyclePolicyPreviewResult"
                                ] = dataclasses.field(
                                    default=ShapeBase.NOT_SET,
                                )

    # The list of images that is returned as a result of the action.
    summary: "LifecyclePolicyPreviewSummary" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class GetLifecyclePolicyRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "repository_name",
                "repositoryName",
                TypeInfo(str),
            ),
            (
                "registry_id",
                "registryId",
                TypeInfo(str),
            ),
        ]

    # The name of the repository.
    repository_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The AWS account ID associated with the registry that contains the
    # repository. If you do not specify a registry, the default registry is
    # assumed.
    registry_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class GetLifecyclePolicyResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "registry_id",
                "registryId",
                TypeInfo(str),
            ),
            (
                "repository_name",
                "repositoryName",
                TypeInfo(str),
            ),
            (
                "lifecycle_policy_text",
                "lifecyclePolicyText",
                TypeInfo(str),
            ),
            (
                "last_evaluated_at",
                "lastEvaluatedAt",
                TypeInfo(datetime.datetime),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The registry ID associated with the request.
    registry_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The repository name associated with the request.
    repository_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The JSON lifecycle policy text.
    lifecycle_policy_text: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The time stamp of the last time that the lifecycle policy was run.
    last_evaluated_at: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class GetRepositoryPolicyRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "repository_name",
                "repositoryName",
                TypeInfo(str),
            ),
            (
                "registry_id",
                "registryId",
                TypeInfo(str),
            ),
        ]

    # The name of the repository with the policy to retrieve.
    repository_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The AWS account ID associated with the registry that contains the
    # repository. If you do not specify a registry, the default registry is
    # assumed.
    registry_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class GetRepositoryPolicyResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "registry_id",
                "registryId",
                TypeInfo(str),
            ),
            (
                "repository_name",
                "repositoryName",
                TypeInfo(str),
            ),
            (
                "policy_text",
                "policyText",
                TypeInfo(str),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The registry ID associated with the request.
    registry_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The repository name associated with the request.
    repository_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The JSON repository policy text associated with the repository.
    policy_text: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class Image(ShapeBase):
    """
    An object representing an Amazon ECR image.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "registry_id",
                "registryId",
                TypeInfo(str),
            ),
            (
                "repository_name",
                "repositoryName",
                TypeInfo(str),
            ),
            (
                "image_id",
                "imageId",
                TypeInfo(ImageIdentifier),
            ),
            (
                "image_manifest",
                "imageManifest",
                TypeInfo(str),
            ),
        ]

    # The AWS account ID associated with the registry containing the image.
    registry_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The name of the repository associated with the image.
    repository_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # An object containing the image tag and image digest associated with an
    # image.
    image_id: "ImageIdentifier" = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The image manifest associated with the image.
    image_manifest: str = dataclasses.field(default=ShapeBase.NOT_SET, )


class ImageActionType(str):
    EXPIRE = "EXPIRE"


@dataclasses.dataclass
class ImageAlreadyExistsException(ShapeBase):
    """
    The specified image has already been pushed, and there were no changes to the
    manifest or image tag after the last push.
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

    # The error message associated with the exception.
    message: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ImageDetail(ShapeBase):
    """
    An object that describes an image returned by a DescribeImages operation.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "registry_id",
                "registryId",
                TypeInfo(str),
            ),
            (
                "repository_name",
                "repositoryName",
                TypeInfo(str),
            ),
            (
                "image_digest",
                "imageDigest",
                TypeInfo(str),
            ),
            (
                "image_tags",
                "imageTags",
                TypeInfo(typing.List[str]),
            ),
            (
                "image_size_in_bytes",
                "imageSizeInBytes",
                TypeInfo(int),
            ),
            (
                "image_pushed_at",
                "imagePushedAt",
                TypeInfo(datetime.datetime),
            ),
        ]

    # The AWS account ID associated with the registry to which this image
    # belongs.
    registry_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The name of the repository to which this image belongs.
    repository_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The `sha256` digest of the image manifest.
    image_digest: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The list of tags associated with this image.
    image_tags: typing.List[str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The size, in bytes, of the image in the repository.

    # Beginning with Docker version 1.9, the Docker client compresses image
    # layers before pushing them to a V2 Docker registry. The output of the
    # `docker images` command shows the uncompressed image size, so it may return
    # a larger image size than the image sizes returned by DescribeImages.
    image_size_in_bytes: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The date and time, expressed in standard JavaScript date format, at which
    # the current image was pushed to the repository.
    image_pushed_at: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class ImageFailure(ShapeBase):
    """
    An object representing an Amazon ECR image failure.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "image_id",
                "imageId",
                TypeInfo(ImageIdentifier),
            ),
            (
                "failure_code",
                "failureCode",
                TypeInfo(typing.Union[str, ImageFailureCode]),
            ),
            (
                "failure_reason",
                "failureReason",
                TypeInfo(str),
            ),
        ]

    # The image ID associated with the failure.
    image_id: "ImageIdentifier" = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The code associated with the failure.
    failure_code: typing.Union[str, "ImageFailureCode"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The reason for the failure.
    failure_reason: str = dataclasses.field(default=ShapeBase.NOT_SET, )


class ImageFailureCode(str):
    InvalidImageDigest = "InvalidImageDigest"
    InvalidImageTag = "InvalidImageTag"
    ImageTagDoesNotMatchDigest = "ImageTagDoesNotMatchDigest"
    ImageNotFound = "ImageNotFound"
    MissingDigestAndTag = "MissingDigestAndTag"


@dataclasses.dataclass
class ImageIdentifier(ShapeBase):
    """
    An object with identifying information for an Amazon ECR image.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "image_digest",
                "imageDigest",
                TypeInfo(str),
            ),
            (
                "image_tag",
                "imageTag",
                TypeInfo(str),
            ),
        ]

    # The `sha256` digest of the image manifest.
    image_digest: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The tag used for the image.
    image_tag: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ImageNotFoundException(ShapeBase):
    """
    The image requested does not exist in the specified repository.
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

    message: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class InitiateLayerUploadRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "repository_name",
                "repositoryName",
                TypeInfo(str),
            ),
            (
                "registry_id",
                "registryId",
                TypeInfo(str),
            ),
        ]

    # The name of the repository to which you intend to upload layers.
    repository_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The AWS account ID associated with the registry to which you intend to
    # upload layers. If you do not specify a registry, the default registry is
    # assumed.
    registry_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class InitiateLayerUploadResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "upload_id",
                "uploadId",
                TypeInfo(str),
            ),
            (
                "part_size",
                "partSize",
                TypeInfo(int),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The upload ID for the layer upload. This parameter is passed to further
    # UploadLayerPart and CompleteLayerUpload operations.
    upload_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The size, in bytes, that Amazon ECR expects future layer part uploads to
    # be.
    part_size: int = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class InvalidLayerException(ShapeBase):
    """
    The layer digest calculation performed by Amazon ECR upon receipt of the image
    layer does not match the digest specified.
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

    # The error message associated with the exception.
    message: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class InvalidLayerPartException(ShapeBase):
    """
    The layer part size is not valid, or the first byte specified is not consecutive
    to the last byte of a previous layer part upload.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "registry_id",
                "registryId",
                TypeInfo(str),
            ),
            (
                "repository_name",
                "repositoryName",
                TypeInfo(str),
            ),
            (
                "upload_id",
                "uploadId",
                TypeInfo(str),
            ),
            (
                "last_valid_byte_received",
                "lastValidByteReceived",
                TypeInfo(int),
            ),
            (
                "message",
                "message",
                TypeInfo(str),
            ),
        ]

    # The registry ID associated with the exception.
    registry_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The repository name associated with the exception.
    repository_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The upload ID associated with the exception.
    upload_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The last valid byte received from the layer part upload that is associated
    # with the exception.
    last_valid_byte_received: int = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The error message associated with the exception.
    message: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class InvalidParameterException(ShapeBase):
    """
    The specified parameter is invalid. Review the available parameters for the API
    request.
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

    # The error message associated with the exception.
    message: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class Layer(ShapeBase):
    """
    An object representing an Amazon ECR image layer.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "layer_digest",
                "layerDigest",
                TypeInfo(str),
            ),
            (
                "layer_availability",
                "layerAvailability",
                TypeInfo(typing.Union[str, LayerAvailability]),
            ),
            (
                "layer_size",
                "layerSize",
                TypeInfo(int),
            ),
            (
                "media_type",
                "mediaType",
                TypeInfo(str),
            ),
        ]

    # The `sha256` digest of the image layer.
    layer_digest: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The availability status of the image layer.
    layer_availability: typing.Union[str, "LayerAvailability"
                                    ] = dataclasses.field(
                                        default=ShapeBase.NOT_SET,
                                    )

    # The size, in bytes, of the image layer.
    layer_size: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The media type of the layer, such as
    # `application/vnd.docker.image.rootfs.diff.tar.gzip` or
    # `application/vnd.oci.image.layer.v1.tar+gzip`.
    media_type: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class LayerAlreadyExistsException(ShapeBase):
    """
    The image layer already exists in the associated repository.
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

    # The error message associated with the exception.
    message: str = dataclasses.field(default=ShapeBase.NOT_SET, )


class LayerAvailability(str):
    AVAILABLE = "AVAILABLE"
    UNAVAILABLE = "UNAVAILABLE"


@dataclasses.dataclass
class LayerFailure(ShapeBase):
    """
    An object representing an Amazon ECR image layer failure.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "layer_digest",
                "layerDigest",
                TypeInfo(str),
            ),
            (
                "failure_code",
                "failureCode",
                TypeInfo(typing.Union[str, LayerFailureCode]),
            ),
            (
                "failure_reason",
                "failureReason",
                TypeInfo(str),
            ),
        ]

    # The layer digest associated with the failure.
    layer_digest: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The failure code associated with the failure.
    failure_code: typing.Union[str, "LayerFailureCode"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The reason for the failure.
    failure_reason: str = dataclasses.field(default=ShapeBase.NOT_SET, )


class LayerFailureCode(str):
    InvalidLayerDigest = "InvalidLayerDigest"
    MissingLayerDigest = "MissingLayerDigest"


@dataclasses.dataclass
class LayerInaccessibleException(ShapeBase):
    """
    The specified layer is not available because it is not associated with an image.
    Unassociated image layers may be cleaned up at any time.
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

    # The error message associated with the exception.
    message: str = dataclasses.field(default=ShapeBase.NOT_SET, )


class LayerPartBlob(botocore.response.StreamingBody):
    pass


@dataclasses.dataclass
class LayerPartTooSmallException(ShapeBase):
    """
    Layer parts must be at least 5 MiB in size.
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

    # The error message associated with the exception.
    message: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class LayersNotFoundException(ShapeBase):
    """
    The specified layers could not be found, or the specified layer is not valid for
    this repository.
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

    # The error message associated with the exception.
    message: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class LifecyclePolicyNotFoundException(ShapeBase):
    """
    The lifecycle policy could not be found, and no policy is set to the repository.
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

    message: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class LifecyclePolicyPreviewFilter(ShapeBase):
    """
    The filter for the lifecycle policy preview.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "tag_status",
                "tagStatus",
                TypeInfo(typing.Union[str, TagStatus]),
            ),
        ]

    # The tag status of the image.
    tag_status: typing.Union[str, "TagStatus"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class LifecyclePolicyPreviewInProgressException(ShapeBase):
    """
    The previous lifecycle policy preview request has not completed. Please try
    again later.
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

    message: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class LifecyclePolicyPreviewNotFoundException(ShapeBase):
    """
    There is no dry run for this repository.
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

    message: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class LifecyclePolicyPreviewResult(ShapeBase):
    """
    The result of the lifecycle policy preview.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "image_tags",
                "imageTags",
                TypeInfo(typing.List[str]),
            ),
            (
                "image_digest",
                "imageDigest",
                TypeInfo(str),
            ),
            (
                "image_pushed_at",
                "imagePushedAt",
                TypeInfo(datetime.datetime),
            ),
            (
                "action",
                "action",
                TypeInfo(LifecyclePolicyRuleAction),
            ),
            (
                "applied_rule_priority",
                "appliedRulePriority",
                TypeInfo(int),
            ),
        ]

    # The list of tags associated with this image.
    image_tags: typing.List[str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The `sha256` digest of the image manifest.
    image_digest: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The date and time, expressed in standard JavaScript date format, at which
    # the current image was pushed to the repository.
    image_pushed_at: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The type of action to be taken.
    action: "LifecyclePolicyRuleAction" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The priority of the applied rule.
    applied_rule_priority: int = dataclasses.field(default=ShapeBase.NOT_SET, )


class LifecyclePolicyPreviewStatus(str):
    IN_PROGRESS = "IN_PROGRESS"
    COMPLETE = "COMPLETE"
    EXPIRED = "EXPIRED"
    FAILED = "FAILED"


@dataclasses.dataclass
class LifecyclePolicyPreviewSummary(ShapeBase):
    """
    The summary of the lifecycle policy preview request.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "expiring_image_total_count",
                "expiringImageTotalCount",
                TypeInfo(int),
            ),
        ]

    # The number of expiring images.
    expiring_image_total_count: int = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class LifecyclePolicyRuleAction(ShapeBase):
    """
    The type of action to be taken.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "type",
                "type",
                TypeInfo(typing.Union[str, ImageActionType]),
            ),
        ]

    # The type of action to be taken.
    type: typing.Union[str, "ImageActionType"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class LimitExceededException(ShapeBase):
    """
    The operation did not succeed because it would have exceeded a service limit for
    your account. For more information, see [Amazon ECR Default Service
    Limits](http://docs.aws.amazon.com/AmazonECR/latest/userguide/service_limits.html)
    in the Amazon Elastic Container Registry User Guide.
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

    # The error message associated with the exception.
    message: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ListImagesFilter(ShapeBase):
    """
    An object representing a filter on a ListImages operation.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "tag_status",
                "tagStatus",
                TypeInfo(typing.Union[str, TagStatus]),
            ),
        ]

    # The tag status with which to filter your ListImages results. You can filter
    # results based on whether they are `TAGGED` or `UNTAGGED`.
    tag_status: typing.Union[str, "TagStatus"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class ListImagesRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "repository_name",
                "repositoryName",
                TypeInfo(str),
            ),
            (
                "registry_id",
                "registryId",
                TypeInfo(str),
            ),
            (
                "next_token",
                "nextToken",
                TypeInfo(str),
            ),
            (
                "max_results",
                "maxResults",
                TypeInfo(int),
            ),
            (
                "filter",
                "filter",
                TypeInfo(ListImagesFilter),
            ),
        ]

    # The repository with image IDs to be listed.
    repository_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The AWS account ID associated with the registry that contains the
    # repository in which to list images. If you do not specify a registry, the
    # default registry is assumed.
    registry_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The `nextToken` value returned from a previous paginated `ListImages`
    # request where `maxResults` was used and the results exceeded the value of
    # that parameter. Pagination continues from the end of the previous results
    # that returned the `nextToken` value. This value is `null` when there are no
    # more results to return.

    # This token should be treated as an opaque identifier that is only used to
    # retrieve the next items in a list and not for other programmatic purposes.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The maximum number of image results returned by `ListImages` in paginated
    # output. When this parameter is used, `ListImages` only returns `maxResults`
    # results in a single page along with a `nextToken` response element. The
    # remaining results of the initial request can be seen by sending another
    # `ListImages` request with the returned `nextToken` value. This value can be
    # between 1 and 100. If this parameter is not used, then `ListImages` returns
    # up to 100 results and a `nextToken` value, if applicable.
    max_results: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The filter key and value with which to filter your `ListImages` results.
    filter: "ListImagesFilter" = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ListImagesResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "image_ids",
                "imageIds",
                TypeInfo(typing.List[ImageIdentifier]),
            ),
            (
                "next_token",
                "nextToken",
                TypeInfo(str),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The list of image IDs for the requested repository.
    image_ids: typing.List["ImageIdentifier"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The `nextToken` value to include in a future `ListImages` request. When the
    # results of a `ListImages` request exceed `maxResults`, this value can be
    # used to retrieve the next page of results. This value is `null` when there
    # are no more results to return.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    def paginate(self, ) -> typing.Generator["ListImagesResponse", None, None]:
        yield from super()._paginate()


@dataclasses.dataclass
class PutImageRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "repository_name",
                "repositoryName",
                TypeInfo(str),
            ),
            (
                "image_manifest",
                "imageManifest",
                TypeInfo(str),
            ),
            (
                "registry_id",
                "registryId",
                TypeInfo(str),
            ),
            (
                "image_tag",
                "imageTag",
                TypeInfo(str),
            ),
        ]

    # The name of the repository in which to put the image.
    repository_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The image manifest corresponding to the image to be uploaded.
    image_manifest: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The AWS account ID associated with the registry that contains the
    # repository in which to put the image. If you do not specify a registry, the
    # default registry is assumed.
    registry_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The tag to associate with the image. This parameter is required for images
    # that use the Docker Image Manifest V2 Schema 2 or OCI formats.
    image_tag: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class PutImageResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "image",
                "image",
                TypeInfo(Image),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Details of the image uploaded.
    image: "Image" = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class PutLifecyclePolicyRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "repository_name",
                "repositoryName",
                TypeInfo(str),
            ),
            (
                "lifecycle_policy_text",
                "lifecyclePolicyText",
                TypeInfo(str),
            ),
            (
                "registry_id",
                "registryId",
                TypeInfo(str),
            ),
        ]

    # The name of the repository to receive the policy.
    repository_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The JSON repository policy text to apply to the repository.
    lifecycle_policy_text: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The AWS account ID associated with the registry that contains the
    # repository. If you do not specify a registry, the default registry is
    # assumed.
    registry_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class PutLifecyclePolicyResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "registry_id",
                "registryId",
                TypeInfo(str),
            ),
            (
                "repository_name",
                "repositoryName",
                TypeInfo(str),
            ),
            (
                "lifecycle_policy_text",
                "lifecyclePolicyText",
                TypeInfo(str),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The registry ID associated with the request.
    registry_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The repository name associated with the request.
    repository_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The JSON repository policy text.
    lifecycle_policy_text: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class Repository(ShapeBase):
    """
    An object representing a repository.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "repository_arn",
                "repositoryArn",
                TypeInfo(str),
            ),
            (
                "registry_id",
                "registryId",
                TypeInfo(str),
            ),
            (
                "repository_name",
                "repositoryName",
                TypeInfo(str),
            ),
            (
                "repository_uri",
                "repositoryUri",
                TypeInfo(str),
            ),
            (
                "created_at",
                "createdAt",
                TypeInfo(datetime.datetime),
            ),
        ]

    # The Amazon Resource Name (ARN) that identifies the repository. The ARN
    # contains the `arn:aws:ecr` namespace, followed by the region of the
    # repository, AWS account ID of the repository owner, repository namespace,
    # and repository name. For example,
    # `arn:aws:ecr:region:012345678910:repository/test`.
    repository_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The AWS account ID associated with the registry that contains the
    # repository.
    registry_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The name of the repository.
    repository_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The URI for the repository. You can use this URI for Docker `push` or
    # `pull` operations.
    repository_uri: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The date and time, in JavaScript date format, when the repository was
    # created.
    created_at: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class RepositoryAlreadyExistsException(ShapeBase):
    """
    The specified repository already exists in the specified registry.
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

    # The error message associated with the exception.
    message: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class RepositoryNotEmptyException(ShapeBase):
    """
    The specified repository contains images. To delete a repository that contains
    images, you must force the deletion with the `force` parameter.
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

    # The error message associated with the exception.
    message: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class RepositoryNotFoundException(ShapeBase):
    """
    The specified repository could not be found. Check the spelling of the specified
    repository and ensure that you are performing operations on the correct
    registry.
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

    # The error message associated with the exception.
    message: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class RepositoryPolicyNotFoundException(ShapeBase):
    """
    The specified repository and registry combination does not have an associated
    repository policy.
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

    # The error message associated with the exception.
    message: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ServerException(ShapeBase):
    """
    These errors are usually caused by a server-side issue.
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

    # The error message associated with the exception.
    message: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class SetRepositoryPolicyRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "repository_name",
                "repositoryName",
                TypeInfo(str),
            ),
            (
                "policy_text",
                "policyText",
                TypeInfo(str),
            ),
            (
                "registry_id",
                "registryId",
                TypeInfo(str),
            ),
            (
                "force",
                "force",
                TypeInfo(bool),
            ),
        ]

    # The name of the repository to receive the policy.
    repository_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The JSON repository policy text to apply to the repository.
    policy_text: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The AWS account ID associated with the registry that contains the
    # repository. If you do not specify a registry, the default registry is
    # assumed.
    registry_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # If the policy you are attempting to set on a repository policy would
    # prevent you from setting another policy in the future, you must force the
    # SetRepositoryPolicy operation. This is intended to prevent accidental
    # repository lock outs.
    force: bool = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class SetRepositoryPolicyResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "registry_id",
                "registryId",
                TypeInfo(str),
            ),
            (
                "repository_name",
                "repositoryName",
                TypeInfo(str),
            ),
            (
                "policy_text",
                "policyText",
                TypeInfo(str),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The registry ID associated with the request.
    registry_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The repository name associated with the request.
    repository_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The JSON repository policy text applied to the repository.
    policy_text: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class StartLifecyclePolicyPreviewRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "repository_name",
                "repositoryName",
                TypeInfo(str),
            ),
            (
                "registry_id",
                "registryId",
                TypeInfo(str),
            ),
            (
                "lifecycle_policy_text",
                "lifecyclePolicyText",
                TypeInfo(str),
            ),
        ]

    # The name of the repository to be evaluated.
    repository_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The AWS account ID associated with the registry that contains the
    # repository. If you do not specify a registry, the default registry is
    # assumed.
    registry_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The policy to be evaluated against. If you do not specify a policy, the
    # current policy for the repository is used.
    lifecycle_policy_text: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class StartLifecyclePolicyPreviewResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "registry_id",
                "registryId",
                TypeInfo(str),
            ),
            (
                "repository_name",
                "repositoryName",
                TypeInfo(str),
            ),
            (
                "lifecycle_policy_text",
                "lifecyclePolicyText",
                TypeInfo(str),
            ),
            (
                "status",
                "status",
                TypeInfo(typing.Union[str, LifecyclePolicyPreviewStatus]),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The registry ID associated with the request.
    registry_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The repository name associated with the request.
    repository_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The JSON repository policy text.
    lifecycle_policy_text: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The status of the lifecycle policy preview request.
    status: typing.Union[str, "LifecyclePolicyPreviewStatus"
                        ] = dataclasses.field(
                            default=ShapeBase.NOT_SET,
                        )


class TagStatus(str):
    TAGGED = "TAGGED"
    UNTAGGED = "UNTAGGED"


@dataclasses.dataclass
class UploadLayerPartRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "repository_name",
                "repositoryName",
                TypeInfo(str),
            ),
            (
                "upload_id",
                "uploadId",
                TypeInfo(str),
            ),
            (
                "part_first_byte",
                "partFirstByte",
                TypeInfo(int),
            ),
            (
                "part_last_byte",
                "partLastByte",
                TypeInfo(int),
            ),
            (
                "layer_part_blob",
                "layerPartBlob",
                TypeInfo(typing.Any),
            ),
            (
                "registry_id",
                "registryId",
                TypeInfo(str),
            ),
        ]

    # The name of the repository to which you are uploading layer parts.
    repository_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The upload ID from a previous InitiateLayerUpload operation to associate
    # with the layer part upload.
    upload_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The integer value of the first byte of the layer part.
    part_first_byte: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The integer value of the last byte of the layer part.
    part_last_byte: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The base64-encoded layer part payload.
    layer_part_blob: typing.Any = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The AWS account ID associated with the registry to which you are uploading
    # layer parts. If you do not specify a registry, the default registry is
    # assumed.
    registry_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class UploadLayerPartResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "registry_id",
                "registryId",
                TypeInfo(str),
            ),
            (
                "repository_name",
                "repositoryName",
                TypeInfo(str),
            ),
            (
                "upload_id",
                "uploadId",
                TypeInfo(str),
            ),
            (
                "last_byte_received",
                "lastByteReceived",
                TypeInfo(int),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The registry ID associated with the request.
    registry_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The repository name associated with the request.
    repository_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The upload ID associated with the request.
    upload_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The integer value of the last byte received in the request.
    last_byte_received: int = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class UploadNotFoundException(ShapeBase):
    """
    The upload could not be found, or the specified upload id is not valid for this
    repository.
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

    # The error message associated with the exception.
    message: str = dataclasses.field(default=ShapeBase.NOT_SET, )
