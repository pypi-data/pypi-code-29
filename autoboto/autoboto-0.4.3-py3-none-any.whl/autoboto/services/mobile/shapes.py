import datetime
import typing
from autoboto import ShapeBase, OutputShapeBase, TypeInfo
import botocore.response
import dataclasses


@dataclasses.dataclass
class AccountActionRequiredException(ShapeBase):
    """
    Account Action is required in order to continue the request.
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

    # The Exception Error Message.
    message: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class BadRequestException(ShapeBase):
    """
    The request cannot be processed because some parameter is not valid or the
    project state prevents the operation from being performed.
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

    # The Exception Error Message.
    message: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class BundleDetails(ShapeBase):
    """
    The details of the bundle.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "bundle_id",
                "bundleId",
                TypeInfo(str),
            ),
            (
                "title",
                "title",
                TypeInfo(str),
            ),
            (
                "version",
                "version",
                TypeInfo(str),
            ),
            (
                "description",
                "description",
                TypeInfo(str),
            ),
            (
                "icon_url",
                "iconUrl",
                TypeInfo(str),
            ),
            (
                "available_platforms",
                "availablePlatforms",
                TypeInfo(typing.List[typing.Union[str, Platform]]),
            ),
        ]

    # Unique bundle identifier.
    bundle_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Title of the download bundle.
    title: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Version of the download bundle.
    version: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Description of the download bundle.
    description: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Icon for the download bundle.
    icon_url: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Developer desktop or mobile app or website platforms.
    available_platforms: typing.List[typing.Union[str, "Platform"]
                                    ] = dataclasses.field(
                                        default=ShapeBase.NOT_SET,
                                    )


class Contents(botocore.response.StreamingBody):
    """
    Binary file data.
    """
    pass


@dataclasses.dataclass
class CreateProjectRequest(ShapeBase):
    """
    Request structure used to request a project be created.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "name",
                "name",
                TypeInfo(str),
            ),
            (
                "region",
                "region",
                TypeInfo(str),
            ),
            (
                "contents",
                "contents",
                TypeInfo(typing.Any),
            ),
            (
                "snapshot_id",
                "snapshotId",
                TypeInfo(str),
            ),
        ]

    # Name of the project.
    name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Default region where project resources should be created.
    region: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # ZIP or YAML file which contains configuration settings to be used when
    # creating the project. This may be the contents of the file downloaded from
    # the URL provided in an export project operation.
    contents: typing.Any = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Unique identifier for an exported snapshot of project configuration. This
    # snapshot identifier is included in the share URL when a project is
    # exported.
    snapshot_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class CreateProjectResult(OutputShapeBase):
    """
    Result structure used in response to a request to create a project.
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
                "details",
                "details",
                TypeInfo(ProjectDetails),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Detailed information about the created AWS Mobile Hub project.
    details: "ProjectDetails" = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DeleteProjectRequest(ShapeBase):
    """
    Request structure used to request a project be deleted.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "project_id",
                "projectId",
                TypeInfo(str),
            ),
        ]

    # Unique project identifier.
    project_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DeleteProjectResult(OutputShapeBase):
    """
    Result structure used in response to request to delete a project.
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
                "deleted_resources",
                "deletedResources",
                TypeInfo(typing.List[Resource]),
            ),
            (
                "orphaned_resources",
                "orphanedResources",
                TypeInfo(typing.List[Resource]),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Resources which were deleted.
    deleted_resources: typing.List["Resource"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Resources which were not deleted, due to a risk of losing potentially
    # important data or files.
    orphaned_resources: typing.List["Resource"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class DescribeBundleRequest(ShapeBase):
    """
    Request structure to request the details of a specific bundle.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "bundle_id",
                "bundleId",
                TypeInfo(str),
            ),
        ]

    # Unique bundle identifier.
    bundle_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DescribeBundleResult(OutputShapeBase):
    """
    Result structure contains the details of the bundle.
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
                "details",
                "details",
                TypeInfo(BundleDetails),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The details of the bundle.
    details: "BundleDetails" = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DescribeProjectRequest(ShapeBase):
    """
    Request structure used to request details about a project.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "project_id",
                "projectId",
                TypeInfo(str),
            ),
            (
                "sync_from_resources",
                "syncFromResources",
                TypeInfo(bool),
            ),
        ]

    # Unique project identifier.
    project_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # If set to true, causes AWS Mobile Hub to synchronize information from other
    # services, e.g., update state of AWS CloudFormation stacks in the AWS Mobile
    # Hub project.
    sync_from_resources: bool = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DescribeProjectResult(OutputShapeBase):
    """
    Result structure used for requests of project details.
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
                "details",
                "details",
                TypeInfo(ProjectDetails),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Detailed information about an AWS Mobile Hub project.
    details: "ProjectDetails" = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ExportBundleRequest(ShapeBase):
    """
    Request structure used to request generation of custom SDK and tool packages
    required to integrate mobile web or app clients with backed AWS resources.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "bundle_id",
                "bundleId",
                TypeInfo(str),
            ),
            (
                "project_id",
                "projectId",
                TypeInfo(str),
            ),
            (
                "platform",
                "platform",
                TypeInfo(typing.Union[str, Platform]),
            ),
        ]

    # Unique bundle identifier.
    bundle_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Unique project identifier.
    project_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Developer desktop or target application platform.
    platform: typing.Union[str, "Platform"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class ExportBundleResult(OutputShapeBase):
    """
    Result structure which contains link to download custom-generated SDK and tool
    packages used to integrate mobile web or app clients with backed AWS resources.
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
                "download_url",
                "downloadUrl",
                TypeInfo(str),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # URL which contains the custom-generated SDK and tool packages used to
    # integrate the client mobile app or web app with the AWS resources created
    # by the AWS Mobile Hub project.
    download_url: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ExportProjectRequest(ShapeBase):
    """
    Request structure used in requests to export project configuration details.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "project_id",
                "projectId",
                TypeInfo(str),
            ),
        ]

    # Unique project identifier.
    project_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ExportProjectResult(OutputShapeBase):
    """
    Result structure used for requests to export project configuration details.
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
                "download_url",
                "downloadUrl",
                TypeInfo(str),
            ),
            (
                "share_url",
                "shareUrl",
                TypeInfo(str),
            ),
            (
                "snapshot_id",
                "snapshotId",
                TypeInfo(str),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # URL which can be used to download the exported project configuation
    # file(s).
    download_url: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # URL which can be shared to allow other AWS users to create their own
    # project in AWS Mobile Hub with the same configuration as the specified
    # project. This URL pertains to a snapshot in time of the project
    # configuration that is created when this API is called. If you want to share
    # additional changes to your project configuration, then you will need to
    # create and share a new snapshot by calling this method again.
    share_url: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Unique identifier for the exported snapshot of the project configuration.
    # This snapshot identifier is included in the share URL.
    snapshot_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class InternalFailureException(ShapeBase):
    """
    The service has encountered an unexpected error condition which prevents it from
    servicing the request.
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

    # The Exception Error Message.
    message: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class LimitExceededException(ShapeBase):
    """
    There are too many AWS Mobile Hub projects in the account or the account has
    exceeded the maximum number of resources in some AWS service. You should create
    another sub-account using AWS Organizations or remove some resources and retry
    your request.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "retry_after_seconds",
                "retryAfterSeconds",
                TypeInfo(str),
            ),
            (
                "message",
                "message",
                TypeInfo(str),
            ),
        ]

    # The Exception Error Message.
    retry_after_seconds: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The Exception Error Message.
    message: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ListBundlesRequest(ShapeBase):
    """
    Request structure to request all available bundles.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "max_results",
                "maxResults",
                TypeInfo(int),
            ),
            (
                "next_token",
                "nextToken",
                TypeInfo(str),
            ),
        ]

    # Maximum number of records to list in a single response.
    max_results: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Pagination token. Set to null to start listing bundles from start. If non-
    # null pagination token is returned in a result, then pass its value in here
    # in another request to list more bundles.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ListBundlesResult(OutputShapeBase):
    """
    Result structure contains a list of all available bundles with details.
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
                "bundle_list",
                "bundleList",
                TypeInfo(typing.List[BundleDetails]),
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

    # A list of bundles.
    bundle_list: typing.List["BundleDetails"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Pagination token. If non-null pagination token is returned in a result,
    # then pass its value in another request to fetch more entries.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    def paginate(self, ) -> typing.Generator["ListBundlesResult", None, None]:
        yield from super()._paginate()


@dataclasses.dataclass
class ListProjectsRequest(ShapeBase):
    """
    Request structure used to request projects list in AWS Mobile Hub.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "max_results",
                "maxResults",
                TypeInfo(int),
            ),
            (
                "next_token",
                "nextToken",
                TypeInfo(str),
            ),
        ]

    # Maximum number of records to list in a single response.
    max_results: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Pagination token. Set to null to start listing projects from start. If non-
    # null pagination token is returned in a result, then pass its value in here
    # in another request to list more projects.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ListProjectsResult(OutputShapeBase):
    """
    Result structure used for requests to list projects in AWS Mobile Hub.
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
                "projects",
                "projects",
                TypeInfo(typing.List[ProjectSummary]),
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

    # List of projects.
    projects: typing.List["ProjectSummary"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Pagination token. Set to null to start listing records from start. If non-
    # null pagination token is returned in a result, then pass its value in here
    # in another request to list more entries.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    def paginate(self, ) -> typing.Generator["ListProjectsResult", None, None]:
        yield from super()._paginate()


@dataclasses.dataclass
class NotFoundException(ShapeBase):
    """
    No entity can be found with the specified identifier.
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

    # The Exception Error Message.
    message: str = dataclasses.field(default=ShapeBase.NOT_SET, )


class Platform(str):
    """
    Developer desktop or target mobile app or website platform.
    """
    OSX = "OSX"
    WINDOWS = "WINDOWS"
    LINUX = "LINUX"
    OBJC = "OBJC"
    SWIFT = "SWIFT"
    ANDROID = "ANDROID"
    JAVASCRIPT = "JAVASCRIPT"


@dataclasses.dataclass
class ProjectDetails(ShapeBase):
    """
    Detailed information about an AWS Mobile Hub project.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "name",
                "name",
                TypeInfo(str),
            ),
            (
                "project_id",
                "projectId",
                TypeInfo(str),
            ),
            (
                "region",
                "region",
                TypeInfo(str),
            ),
            (
                "state",
                "state",
                TypeInfo(typing.Union[str, ProjectState]),
            ),
            (
                "created_date",
                "createdDate",
                TypeInfo(datetime.datetime),
            ),
            (
                "last_updated_date",
                "lastUpdatedDate",
                TypeInfo(datetime.datetime),
            ),
            (
                "console_url",
                "consoleUrl",
                TypeInfo(str),
            ),
            (
                "resources",
                "resources",
                TypeInfo(typing.List[Resource]),
            ),
        ]

    # Name of the project.
    name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Unique project identifier.
    project_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Default region to use for AWS resource creation in the AWS Mobile Hub
    # project.
    region: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Synchronization state for a project.
    state: typing.Union[str, "ProjectState"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Date the project was created.
    created_date: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Date of the last modification of the project.
    last_updated_date: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Website URL for this project in the AWS Mobile Hub console.
    console_url: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # List of AWS resources associated with a project.
    resources: typing.List["Resource"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


class ProjectState(str):
    """
    Synchronization state for a project.
    """
    NORMAL = "NORMAL"
    SYNCING = "SYNCING"
    IMPORTING = "IMPORTING"


@dataclasses.dataclass
class ProjectSummary(ShapeBase):
    """
    Summary information about an AWS Mobile Hub project.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "name",
                "name",
                TypeInfo(str),
            ),
            (
                "project_id",
                "projectId",
                TypeInfo(str),
            ),
        ]

    # Name of the project.
    name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Unique project identifier.
    project_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class Resource(ShapeBase):
    """
    Information about an instance of an AWS resource associated with a project.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "type",
                "type",
                TypeInfo(str),
            ),
            (
                "name",
                "name",
                TypeInfo(str),
            ),
            (
                "arn",
                "arn",
                TypeInfo(str),
            ),
            (
                "feature",
                "feature",
                TypeInfo(str),
            ),
            (
                "attributes",
                "attributes",
                TypeInfo(typing.Dict[str, str]),
            ),
        ]

    # Simplified name for type of AWS resource (e.g., bucket is an Amazon S3
    # bucket).
    type: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Name of the AWS resource (e.g., for an Amazon S3 bucket this is the name of
    # the bucket).
    name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # AWS resource name which uniquely identifies the resource in AWS systems.
    arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Identifies which feature in AWS Mobile Hub is associated with this AWS
    # resource.
    feature: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Key-value attribute pairs.
    attributes: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class ServiceUnavailableException(ShapeBase):
    """
    The service is temporarily unavailable. The request should be retried after some
    time delay.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "retry_after_seconds",
                "retryAfterSeconds",
                TypeInfo(str),
            ),
            (
                "message",
                "message",
                TypeInfo(str),
            ),
        ]

    # The Exception Error Message.
    retry_after_seconds: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The Exception Error Message.
    message: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class TooManyRequestsException(ShapeBase):
    """
    Too many requests have been received for this AWS account in too short a time.
    The request should be retried after some time delay.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "retry_after_seconds",
                "retryAfterSeconds",
                TypeInfo(str),
            ),
            (
                "message",
                "message",
                TypeInfo(str),
            ),
        ]

    # The Exception Error Message.
    retry_after_seconds: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The Exception Error Message.
    message: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class UnauthorizedException(ShapeBase):
    """
    Credentials of the caller are insufficient to authorize the request.
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

    # The Exception Error Message.
    message: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class UpdateProjectRequest(ShapeBase):
    """
    Request structure used for requests to update project configuration.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "project_id",
                "projectId",
                TypeInfo(str),
            ),
            (
                "contents",
                "contents",
                TypeInfo(typing.Any),
            ),
        ]

    # Unique project identifier.
    project_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # ZIP or YAML file which contains project configuration to be updated. This
    # should be the contents of the file downloaded from the URL provided in an
    # export project operation.
    contents: typing.Any = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class UpdateProjectResult(OutputShapeBase):
    """
    Result structure used for requests to updated project configuration.
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
                "details",
                "details",
                TypeInfo(ProjectDetails),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Detailed information about the updated AWS Mobile Hub project.
    details: "ProjectDetails" = dataclasses.field(default=ShapeBase.NOT_SET, )
