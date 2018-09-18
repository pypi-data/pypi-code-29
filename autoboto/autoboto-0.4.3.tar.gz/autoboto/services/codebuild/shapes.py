import datetime
import typing
from autoboto import ShapeBase, OutputShapeBase, TypeInfo
import dataclasses


@dataclasses.dataclass
class AccountLimitExceededException(ShapeBase):
    """
    An AWS service limit was exceeded for the calling AWS account.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


class ArtifactNamespace(str):
    NONE = "NONE"
    BUILD_ID = "BUILD_ID"


class ArtifactPackaging(str):
    NONE = "NONE"
    ZIP = "ZIP"


class ArtifactsType(str):
    CODEPIPELINE = "CODEPIPELINE"
    S3 = "S3"
    NO_ARTIFACTS = "NO_ARTIFACTS"


@dataclasses.dataclass
class BatchDeleteBuildsInput(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "ids",
                "ids",
                TypeInfo(typing.List[str]),
            ),
        ]

    # The IDs of the builds to delete.
    ids: typing.List[str] = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class BatchDeleteBuildsOutput(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "builds_deleted",
                "buildsDeleted",
                TypeInfo(typing.List[str]),
            ),
            (
                "builds_not_deleted",
                "buildsNotDeleted",
                TypeInfo(typing.List[BuildNotDeleted]),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The IDs of the builds that were successfully deleted.
    builds_deleted: typing.List[str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Information about any builds that could not be successfully deleted.
    builds_not_deleted: typing.List["BuildNotDeleted"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class BatchGetBuildsInput(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "ids",
                "ids",
                TypeInfo(typing.List[str]),
            ),
        ]

    # The IDs of the builds.
    ids: typing.List[str] = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class BatchGetBuildsOutput(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "builds",
                "builds",
                TypeInfo(typing.List[Build]),
            ),
            (
                "builds_not_found",
                "buildsNotFound",
                TypeInfo(typing.List[str]),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Information about the requested builds.
    builds: typing.List["Build"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The IDs of builds for which information could not be found.
    builds_not_found: typing.List[str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class BatchGetProjectsInput(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "names",
                "names",
                TypeInfo(typing.List[str]),
            ),
        ]

    # The names of the build projects.
    names: typing.List[str] = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class BatchGetProjectsOutput(OutputShapeBase):
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
                TypeInfo(typing.List[Project]),
            ),
            (
                "projects_not_found",
                "projectsNotFound",
                TypeInfo(typing.List[str]),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Information about the requested build projects.
    projects: typing.List["Project"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The names of build projects for which information could not be found.
    projects_not_found: typing.List[str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class Build(ShapeBase):
    """
    Information about a build.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "id",
                "id",
                TypeInfo(str),
            ),
            (
                "arn",
                "arn",
                TypeInfo(str),
            ),
            (
                "start_time",
                "startTime",
                TypeInfo(datetime.datetime),
            ),
            (
                "end_time",
                "endTime",
                TypeInfo(datetime.datetime),
            ),
            (
                "current_phase",
                "currentPhase",
                TypeInfo(str),
            ),
            (
                "build_status",
                "buildStatus",
                TypeInfo(typing.Union[str, StatusType]),
            ),
            (
                "source_version",
                "sourceVersion",
                TypeInfo(str),
            ),
            (
                "project_name",
                "projectName",
                TypeInfo(str),
            ),
            (
                "phases",
                "phases",
                TypeInfo(typing.List[BuildPhase]),
            ),
            (
                "source",
                "source",
                TypeInfo(ProjectSource),
            ),
            (
                "secondary_sources",
                "secondarySources",
                TypeInfo(typing.List[ProjectSource]),
            ),
            (
                "secondary_source_versions",
                "secondarySourceVersions",
                TypeInfo(typing.List[ProjectSourceVersion]),
            ),
            (
                "artifacts",
                "artifacts",
                TypeInfo(BuildArtifacts),
            ),
            (
                "secondary_artifacts",
                "secondaryArtifacts",
                TypeInfo(typing.List[BuildArtifacts]),
            ),
            (
                "cache",
                "cache",
                TypeInfo(ProjectCache),
            ),
            (
                "environment",
                "environment",
                TypeInfo(ProjectEnvironment),
            ),
            (
                "service_role",
                "serviceRole",
                TypeInfo(str),
            ),
            (
                "logs",
                "logs",
                TypeInfo(LogsLocation),
            ),
            (
                "timeout_in_minutes",
                "timeoutInMinutes",
                TypeInfo(int),
            ),
            (
                "build_complete",
                "buildComplete",
                TypeInfo(bool),
            ),
            (
                "initiator",
                "initiator",
                TypeInfo(str),
            ),
            (
                "vpc_config",
                "vpcConfig",
                TypeInfo(VpcConfig),
            ),
            (
                "network_interface",
                "networkInterface",
                TypeInfo(NetworkInterface),
            ),
            (
                "encryption_key",
                "encryptionKey",
                TypeInfo(str),
            ),
        ]

    # The unique ID for the build.
    id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The Amazon Resource Name (ARN) of the build.
    arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # When the build process started, expressed in Unix time format.
    start_time: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # When the build process ended, expressed in Unix time format.
    end_time: datetime.datetime = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The current build phase.
    current_phase: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The current status of the build. Valid values include:

    #   * `FAILED`: The build failed.

    #   * `FAULT`: The build faulted.

    #   * `IN_PROGRESS`: The build is still in progress.

    #   * `STOPPED`: The build stopped.

    #   * `SUCCEEDED`: The build succeeded.

    #   * `TIMED_OUT`: The build timed out.
    build_status: typing.Union[str, "StatusType"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Any version identifier for the version of the source code to be built.
    source_version: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The name of the AWS CodeBuild project.
    project_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Information about all previous build phases that are completed and
    # information about any current build phase that is not yet complete.
    phases: typing.List["BuildPhase"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Information about the source code to be built.
    source: "ProjectSource" = dataclasses.field(default=ShapeBase.NOT_SET, )

    # An array of `ProjectSource` objects.
    secondary_sources: typing.List["ProjectSource"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # An array of `ProjectSourceVersion` objects. Each `ProjectSourceVersion`
    # must be one of:

    #   * For AWS CodeCommit: the commit ID to use.

    #   * For GitHub: the commit ID, pull request ID, branch name, or tag name that corresponds to the version of the source code you want to build. If a pull request ID is specified, it must use the format `pr/pull-request-ID` (for example `pr/25`). If a branch name is specified, the branch's HEAD commit ID will be used. If not specified, the default branch's HEAD commit ID will be used.

    #   * For Bitbucket: the commit ID, branch name, or tag name that corresponds to the version of the source code you want to build. If a branch name is specified, the branch's HEAD commit ID will be used. If not specified, the default branch's HEAD commit ID will be used.

    #   * For Amazon Simple Storage Service (Amazon S3): the version ID of the object representing the build input ZIP file to use.
    secondary_source_versions: typing.List["ProjectSourceVersion"
                                          ] = dataclasses.field(
                                              default=ShapeBase.NOT_SET,
                                          )

    # Information about the output artifacts for the build.
    artifacts: "BuildArtifacts" = dataclasses.field(default=ShapeBase.NOT_SET, )

    # An array of `ProjectArtifacts` objects.
    secondary_artifacts: typing.List["BuildArtifacts"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Information about the cache for the build.
    cache: "ProjectCache" = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Information about the build environment for this build.
    environment: "ProjectEnvironment" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The name of a service role used for this build.
    service_role: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Information about the build's logs in Amazon CloudWatch Logs.
    logs: "LogsLocation" = dataclasses.field(default=ShapeBase.NOT_SET, )

    # How long, in minutes, for AWS CodeBuild to wait before timing out this
    # build if it does not get marked as completed.
    timeout_in_minutes: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Whether the build has finished. True if completed; otherwise, false.
    build_complete: bool = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The entity that started the build. Valid values include:

    #   * If AWS CodePipeline started the build, the pipeline's name (for example, `codepipeline/my-demo-pipeline`).

    #   * If an AWS Identity and Access Management (IAM) user started the build, the user's name (for example `MyUserName`).

    #   * If the Jenkins plugin for AWS CodeBuild started the build, the string `CodeBuild-Jenkins-Plugin`.
    initiator: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # If your AWS CodeBuild project accesses resources in an Amazon VPC, you
    # provide this parameter that identifies the VPC ID and the list of security
    # group IDs and subnet IDs. The security groups and subnets must belong to
    # the same VPC. You must provide at least one security group and one subnet
    # ID.
    vpc_config: "VpcConfig" = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Describes a network interface.
    network_interface: "NetworkInterface" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The AWS Key Management Service (AWS KMS) customer master key (CMK) to be
    # used for encrypting the build output artifacts.

    # This is expressed either as the CMK's Amazon Resource Name (ARN) or, if
    # specified, the CMK's alias (using the format `alias/ _alias-name_ `).
    encryption_key: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class BuildArtifacts(ShapeBase):
    """
    Information about build output artifacts.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "location",
                "location",
                TypeInfo(str),
            ),
            (
                "sha256sum",
                "sha256sum",
                TypeInfo(str),
            ),
            (
                "md5sum",
                "md5sum",
                TypeInfo(str),
            ),
            (
                "override_artifact_name",
                "overrideArtifactName",
                TypeInfo(bool),
            ),
            (
                "encryption_disabled",
                "encryptionDisabled",
                TypeInfo(bool),
            ),
            (
                "artifact_identifier",
                "artifactIdentifier",
                TypeInfo(str),
            ),
        ]

    # Information about the location of the build artifacts.
    location: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The SHA-256 hash of the build artifact.

    # You can use this hash along with a checksum tool to confirm both file
    # integrity and authenticity.

    # This value is available only if the build project's `packaging` value is
    # set to `ZIP`.
    sha256sum: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The MD5 hash of the build artifact.

    # You can use this hash along with a checksum tool to confirm both file
    # integrity and authenticity.

    # This value is available only if the build project's `packaging` value is
    # set to `ZIP`.
    md5sum: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # If this flag is set, a name specified in the buildspec file overrides the
    # artifact name. The name specified in a buildspec file is calculated at
    # build time and uses the Shell Command Language. For example, you can append
    # a date and time to your artifact name so that it is always unique.
    override_artifact_name: bool = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Information that tells you if encryption for build artifacts is disabled.
    encryption_disabled: bool = dataclasses.field(default=ShapeBase.NOT_SET, )

    # An identifier for this artifact definition.
    artifact_identifier: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class BuildNotDeleted(ShapeBase):
    """
    Information about a build that could not be successfully deleted.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "id",
                "id",
                TypeInfo(str),
            ),
            (
                "status_code",
                "statusCode",
                TypeInfo(str),
            ),
        ]

    # The ID of the build that could not be successfully deleted.
    id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Additional information about the build that could not be successfully
    # deleted.
    status_code: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class BuildPhase(ShapeBase):
    """
    Information about a stage for a build.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "phase_type",
                "phaseType",
                TypeInfo(typing.Union[str, BuildPhaseType]),
            ),
            (
                "phase_status",
                "phaseStatus",
                TypeInfo(typing.Union[str, StatusType]),
            ),
            (
                "start_time",
                "startTime",
                TypeInfo(datetime.datetime),
            ),
            (
                "end_time",
                "endTime",
                TypeInfo(datetime.datetime),
            ),
            (
                "duration_in_seconds",
                "durationInSeconds",
                TypeInfo(int),
            ),
            (
                "contexts",
                "contexts",
                TypeInfo(typing.List[PhaseContext]),
            ),
        ]

    # The name of the build phase. Valid values include:

    #   * `BUILD`: Core build activities typically occur in this build phase.

    #   * `COMPLETED`: The build has been completed.

    #   * `DOWNLOAD_SOURCE`: Source code is being downloaded in this build phase.

    #   * `FINALIZING`: The build process is completing in this build phase.

    #   * `INSTALL`: Installation activities typically occur in this build phase.

    #   * `POST_BUILD`: Post-build activities typically occur in this build phase.

    #   * `PRE_BUILD`: Pre-build activities typically occur in this build phase.

    #   * `PROVISIONING`: The build environment is being set up.

    #   * `SUBMITTED`: The build has been submitted.

    #   * `UPLOAD_ARTIFACTS`: Build output artifacts are being uploaded to the output location.
    phase_type: typing.Union[str, "BuildPhaseType"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The current status of the build phase. Valid values include:

    #   * `FAILED`: The build phase failed.

    #   * `FAULT`: The build phase faulted.

    #   * `IN_PROGRESS`: The build phase is still in progress.

    #   * `STOPPED`: The build phase stopped.

    #   * `SUCCEEDED`: The build phase succeeded.

    #   * `TIMED_OUT`: The build phase timed out.
    phase_status: typing.Union[str, "StatusType"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # When the build phase started, expressed in Unix time format.
    start_time: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # When the build phase ended, expressed in Unix time format.
    end_time: datetime.datetime = dataclasses.field(default=ShapeBase.NOT_SET, )

    # How long, in seconds, between the starting and ending times of the build's
    # phase.
    duration_in_seconds: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Additional information about a build phase, especially to help troubleshoot
    # a failed build.
    contexts: typing.List["PhaseContext"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


class BuildPhaseType(str):
    SUBMITTED = "SUBMITTED"
    PROVISIONING = "PROVISIONING"
    DOWNLOAD_SOURCE = "DOWNLOAD_SOURCE"
    INSTALL = "INSTALL"
    PRE_BUILD = "PRE_BUILD"
    BUILD = "BUILD"
    POST_BUILD = "POST_BUILD"
    UPLOAD_ARTIFACTS = "UPLOAD_ARTIFACTS"
    FINALIZING = "FINALIZING"
    COMPLETED = "COMPLETED"


class CacheType(str):
    NO_CACHE = "NO_CACHE"
    S3 = "S3"


class ComputeType(str):
    BUILD_GENERAL1_SMALL = "BUILD_GENERAL1_SMALL"
    BUILD_GENERAL1_MEDIUM = "BUILD_GENERAL1_MEDIUM"
    BUILD_GENERAL1_LARGE = "BUILD_GENERAL1_LARGE"


@dataclasses.dataclass
class CreateProjectInput(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "name",
                "name",
                TypeInfo(str),
            ),
            (
                "source",
                "source",
                TypeInfo(ProjectSource),
            ),
            (
                "artifacts",
                "artifacts",
                TypeInfo(ProjectArtifacts),
            ),
            (
                "environment",
                "environment",
                TypeInfo(ProjectEnvironment),
            ),
            (
                "service_role",
                "serviceRole",
                TypeInfo(str),
            ),
            (
                "description",
                "description",
                TypeInfo(str),
            ),
            (
                "secondary_sources",
                "secondarySources",
                TypeInfo(typing.List[ProjectSource]),
            ),
            (
                "secondary_artifacts",
                "secondaryArtifacts",
                TypeInfo(typing.List[ProjectArtifacts]),
            ),
            (
                "cache",
                "cache",
                TypeInfo(ProjectCache),
            ),
            (
                "timeout_in_minutes",
                "timeoutInMinutes",
                TypeInfo(int),
            ),
            (
                "encryption_key",
                "encryptionKey",
                TypeInfo(str),
            ),
            (
                "tags",
                "tags",
                TypeInfo(typing.List[Tag]),
            ),
            (
                "vpc_config",
                "vpcConfig",
                TypeInfo(VpcConfig),
            ),
            (
                "badge_enabled",
                "badgeEnabled",
                TypeInfo(bool),
            ),
        ]

    # The name of the build project.
    name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Information about the build input source code for the build project.
    source: "ProjectSource" = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Information about the build output artifacts for the build project.
    artifacts: "ProjectArtifacts" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Information about the build environment for the build project.
    environment: "ProjectEnvironment" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The ARN of the AWS Identity and Access Management (IAM) role that enables
    # AWS CodeBuild to interact with dependent AWS services on behalf of the AWS
    # account.
    service_role: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A description that makes the build project easy to identify.
    description: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # An array of `ProjectSource` objects.
    secondary_sources: typing.List["ProjectSource"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # An array of `ProjectArtifacts` objects.
    secondary_artifacts: typing.List["ProjectArtifacts"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Stores recently used information so that it can be quickly accessed at a
    # later time.
    cache: "ProjectCache" = dataclasses.field(default=ShapeBase.NOT_SET, )

    # How long, in minutes, from 5 to 480 (8 hours), for AWS CodeBuild to wait
    # until timing out any build that has not been marked as completed. The
    # default is 60 minutes.
    timeout_in_minutes: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The AWS Key Management Service (AWS KMS) customer master key (CMK) to be
    # used for encrypting the build output artifacts.

    # You can specify either the CMK's Amazon Resource Name (ARN) or, if
    # available, the CMK's alias (using the format `alias/ _alias-name_ `).
    encryption_key: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A set of tags for this build project.

    # These tags are available for use by AWS services that support AWS CodeBuild
    # build project tags.
    tags: typing.List["Tag"] = dataclasses.field(default=ShapeBase.NOT_SET, )

    # VpcConfig enables AWS CodeBuild to access resources in an Amazon VPC.
    vpc_config: "VpcConfig" = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Set this to true to generate a publicly-accessible URL for your project's
    # build badge.
    badge_enabled: bool = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class CreateProjectOutput(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "project",
                "project",
                TypeInfo(Project),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Information about the build project that was created.
    project: "Project" = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class CreateWebhookInput(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "project_name",
                "projectName",
                TypeInfo(str),
            ),
            (
                "branch_filter",
                "branchFilter",
                TypeInfo(str),
            ),
        ]

    # The name of the AWS CodeBuild project.
    project_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A regular expression used to determine which branches in a repository are
    # built when a webhook is triggered. If the name of a branch matches the
    # regular expression, then it is built. If it doesn't match, then it is not.
    # If branchFilter is empty, then all branches are built.
    branch_filter: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class CreateWebhookOutput(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "webhook",
                "webhook",
                TypeInfo(Webhook),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Information about a webhook in GitHub that connects repository events to a
    # build project in AWS CodeBuild.
    webhook: "Webhook" = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DeleteProjectInput(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "name",
                "name",
                TypeInfo(str),
            ),
        ]

    # The name of the build project.
    name: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DeleteProjectOutput(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class DeleteWebhookInput(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "project_name",
                "projectName",
                TypeInfo(str),
            ),
        ]

    # The name of the AWS CodeBuild project.
    project_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DeleteWebhookOutput(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class EnvironmentImage(ShapeBase):
    """
    Information about a Docker image that is managed by AWS CodeBuild.
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
                "description",
                "description",
                TypeInfo(str),
            ),
            (
                "versions",
                "versions",
                TypeInfo(typing.List[str]),
            ),
        ]

    # The name of the Docker image.
    name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The description of the Docker image.
    description: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A list of environment image versions.
    versions: typing.List[str] = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class EnvironmentLanguage(ShapeBase):
    """
    A set of Docker images that are related by programming language and are managed
    by AWS CodeBuild.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "language",
                "language",
                TypeInfo(typing.Union[str, LanguageType]),
            ),
            (
                "images",
                "images",
                TypeInfo(typing.List[EnvironmentImage]),
            ),
        ]

    # The programming language for the Docker images.
    language: typing.Union[str, "LanguageType"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The list of Docker images that are related by the specified programming
    # language.
    images: typing.List["EnvironmentImage"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class EnvironmentPlatform(ShapeBase):
    """
    A set of Docker images that are related by platform and are managed by AWS
    CodeBuild.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "platform",
                "platform",
                TypeInfo(typing.Union[str, PlatformType]),
            ),
            (
                "languages",
                "languages",
                TypeInfo(typing.List[EnvironmentLanguage]),
            ),
        ]

    # The platform's name.
    platform: typing.Union[str, "PlatformType"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The list of programming languages that are available for the specified
    # platform.
    languages: typing.List["EnvironmentLanguage"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


class EnvironmentType(str):
    WINDOWS_CONTAINER = "WINDOWS_CONTAINER"
    LINUX_CONTAINER = "LINUX_CONTAINER"


@dataclasses.dataclass
class EnvironmentVariable(ShapeBase):
    """
    Information about an environment variable for a build project or a build.
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
                "value",
                "value",
                TypeInfo(str),
            ),
            (
                "type",
                "type",
                TypeInfo(typing.Union[str, EnvironmentVariableType]),
            ),
        ]

    # The name or key of the environment variable.
    name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The value of the environment variable.

    # We strongly discourage using environment variables to store sensitive
    # values, especially AWS secret key IDs and secret access keys. Environment
    # variables can be displayed in plain text using tools such as the AWS
    # CodeBuild console and the AWS Command Line Interface (AWS CLI).
    value: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The type of environment variable. Valid values include:

    #   * `PARAMETER_STORE`: An environment variable stored in Amazon EC2 Systems Manager Parameter Store.

    #   * `PLAINTEXT`: An environment variable in plaintext format.
    type: typing.Union[str, "EnvironmentVariableType"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


class EnvironmentVariableType(str):
    PLAINTEXT = "PLAINTEXT"
    PARAMETER_STORE = "PARAMETER_STORE"


@dataclasses.dataclass
class InvalidInputException(ShapeBase):
    """
    The input value that was provided is not valid.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class InvalidateProjectCacheInput(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "project_name",
                "projectName",
                TypeInfo(str),
            ),
        ]

    # The name of the AWS CodeBuild build project that the cache will be reset
    # for.
    project_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class InvalidateProjectCacheOutput(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


class LanguageType(str):
    JAVA = "JAVA"
    PYTHON = "PYTHON"
    NODE_JS = "NODE_JS"
    RUBY = "RUBY"
    GOLANG = "GOLANG"
    DOCKER = "DOCKER"
    ANDROID = "ANDROID"
    DOTNET = "DOTNET"
    BASE = "BASE"


@dataclasses.dataclass
class ListBuildsForProjectInput(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "project_name",
                "projectName",
                TypeInfo(str),
            ),
            (
                "sort_order",
                "sortOrder",
                TypeInfo(typing.Union[str, SortOrderType]),
            ),
            (
                "next_token",
                "nextToken",
                TypeInfo(str),
            ),
        ]

    # The name of the AWS CodeBuild project.
    project_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The order to list build IDs. Valid values include:

    #   * `ASCENDING`: List the build IDs in ascending order by build ID.

    #   * `DESCENDING`: List the build IDs in descending order by build ID.
    sort_order: typing.Union[str, "SortOrderType"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # During a previous call, if there are more than 100 items in the list, only
    # the first 100 items are returned, along with a unique string called a _next
    # token_. To get the next batch of items in the list, call this operation
    # again, adding the next token to the call. To get all of the items in the
    # list, keep calling this operation with each subsequent next token that is
    # returned, until no more next tokens are returned.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ListBuildsForProjectOutput(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "ids",
                "ids",
                TypeInfo(typing.List[str]),
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

    # A list of build IDs for the specified build project, with each build ID
    # representing a single build.
    ids: typing.List[str] = dataclasses.field(default=ShapeBase.NOT_SET, )

    # If there are more than 100 items in the list, only the first 100 items are
    # returned, along with a unique string called a _next token_. To get the next
    # batch of items in the list, call this operation again, adding the next
    # token to the call.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    def paginate(self,
                ) -> typing.Generator["ListBuildsForProjectOutput", None, None]:
        yield from super()._paginate()


@dataclasses.dataclass
class ListBuildsInput(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "sort_order",
                "sortOrder",
                TypeInfo(typing.Union[str, SortOrderType]),
            ),
            (
                "next_token",
                "nextToken",
                TypeInfo(str),
            ),
        ]

    # The order to list build IDs. Valid values include:

    #   * `ASCENDING`: List the build IDs in ascending order by build ID.

    #   * `DESCENDING`: List the build IDs in descending order by build ID.
    sort_order: typing.Union[str, "SortOrderType"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # During a previous call, if there are more than 100 items in the list, only
    # the first 100 items are returned, along with a unique string called a _next
    # token_. To get the next batch of items in the list, call this operation
    # again, adding the next token to the call. To get all of the items in the
    # list, keep calling this operation with each subsequent next token that is
    # returned, until no more next tokens are returned.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ListBuildsOutput(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "ids",
                "ids",
                TypeInfo(typing.List[str]),
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

    # A list of build IDs, with each build ID representing a single build.
    ids: typing.List[str] = dataclasses.field(default=ShapeBase.NOT_SET, )

    # If there are more than 100 items in the list, only the first 100 items are
    # returned, along with a unique string called a _next token_. To get the next
    # batch of items in the list, call this operation again, adding the next
    # token to the call.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    def paginate(self, ) -> typing.Generator["ListBuildsOutput", None, None]:
        yield from super()._paginate()


@dataclasses.dataclass
class ListCuratedEnvironmentImagesInput(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class ListCuratedEnvironmentImagesOutput(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "platforms",
                "platforms",
                TypeInfo(typing.List[EnvironmentPlatform]),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Information about supported platforms for Docker images that are managed by
    # AWS CodeBuild.
    platforms: typing.List["EnvironmentPlatform"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class ListProjectsInput(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "sort_by",
                "sortBy",
                TypeInfo(typing.Union[str, ProjectSortByType]),
            ),
            (
                "sort_order",
                "sortOrder",
                TypeInfo(typing.Union[str, SortOrderType]),
            ),
            (
                "next_token",
                "nextToken",
                TypeInfo(str),
            ),
        ]

    # The criterion to be used to list build project names. Valid values include:

    #   * `CREATED_TIME`: List the build project names based on when each build project was created.

    #   * `LAST_MODIFIED_TIME`: List the build project names based on when information about each build project was last changed.

    #   * `NAME`: List the build project names based on each build project's name.

    # Use `sortOrder` to specify in what order to list the build project names
    # based on the preceding criteria.
    sort_by: typing.Union[str, "ProjectSortByType"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The order in which to list build projects. Valid values include:

    #   * `ASCENDING`: List the build project names in ascending order.

    #   * `DESCENDING`: List the build project names in descending order.

    # Use `sortBy` to specify the criterion to be used to list build project
    # names.
    sort_order: typing.Union[str, "SortOrderType"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # During a previous call, if there are more than 100 items in the list, only
    # the first 100 items are returned, along with a unique string called a _next
    # token_. To get the next batch of items in the list, call this operation
    # again, adding the next token to the call. To get all of the items in the
    # list, keep calling this operation with each subsequent next token that is
    # returned, until no more next tokens are returned.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ListProjectsOutput(OutputShapeBase):
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
                "nextToken",
                TypeInfo(str),
            ),
            (
                "projects",
                "projects",
                TypeInfo(typing.List[str]),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # If there are more than 100 items in the list, only the first 100 items are
    # returned, along with a unique string called a _next token_. To get the next
    # batch of items in the list, call this operation again, adding the next
    # token to the call.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The list of build project names, with each build project name representing
    # a single build project.
    projects: typing.List[str] = dataclasses.field(default=ShapeBase.NOT_SET, )

    def paginate(self, ) -> typing.Generator["ListProjectsOutput", None, None]:
        yield from super()._paginate()


@dataclasses.dataclass
class LogsLocation(ShapeBase):
    """
    Information about build logs in Amazon CloudWatch Logs.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "group_name",
                "groupName",
                TypeInfo(str),
            ),
            (
                "stream_name",
                "streamName",
                TypeInfo(str),
            ),
            (
                "deep_link",
                "deepLink",
                TypeInfo(str),
            ),
        ]

    # The name of the Amazon CloudWatch Logs group for the build logs.
    group_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The name of the Amazon CloudWatch Logs stream for the build logs.
    stream_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The URL to an individual build log in Amazon CloudWatch Logs.
    deep_link: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class NetworkInterface(ShapeBase):
    """
    Describes a network interface.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "subnet_id",
                "subnetId",
                TypeInfo(str),
            ),
            (
                "network_interface_id",
                "networkInterfaceId",
                TypeInfo(str),
            ),
        ]

    # The ID of the subnet.
    subnet_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The ID of the network interface.
    network_interface_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class OAuthProviderException(ShapeBase):
    """
    There was a problem with the underlying OAuth provider.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class PhaseContext(ShapeBase):
    """
    Additional information about a build phase that has an error. You can use this
    information to help troubleshoot a failed build.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "status_code",
                "statusCode",
                TypeInfo(str),
            ),
            (
                "message",
                "message",
                TypeInfo(str),
            ),
        ]

    # The status code for the context of the build phase.
    status_code: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # An explanation of the build phase's context. This explanation might include
    # a command ID and an exit code.
    message: str = dataclasses.field(default=ShapeBase.NOT_SET, )


class PlatformType(str):
    DEBIAN = "DEBIAN"
    AMAZON_LINUX = "AMAZON_LINUX"
    UBUNTU = "UBUNTU"
    WINDOWS_SERVER = "WINDOWS_SERVER"


@dataclasses.dataclass
class Project(ShapeBase):
    """
    Information about a build project.
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
                "arn",
                "arn",
                TypeInfo(str),
            ),
            (
                "description",
                "description",
                TypeInfo(str),
            ),
            (
                "source",
                "source",
                TypeInfo(ProjectSource),
            ),
            (
                "secondary_sources",
                "secondarySources",
                TypeInfo(typing.List[ProjectSource]),
            ),
            (
                "artifacts",
                "artifacts",
                TypeInfo(ProjectArtifacts),
            ),
            (
                "secondary_artifacts",
                "secondaryArtifacts",
                TypeInfo(typing.List[ProjectArtifacts]),
            ),
            (
                "cache",
                "cache",
                TypeInfo(ProjectCache),
            ),
            (
                "environment",
                "environment",
                TypeInfo(ProjectEnvironment),
            ),
            (
                "service_role",
                "serviceRole",
                TypeInfo(str),
            ),
            (
                "timeout_in_minutes",
                "timeoutInMinutes",
                TypeInfo(int),
            ),
            (
                "encryption_key",
                "encryptionKey",
                TypeInfo(str),
            ),
            (
                "tags",
                "tags",
                TypeInfo(typing.List[Tag]),
            ),
            (
                "created",
                "created",
                TypeInfo(datetime.datetime),
            ),
            (
                "last_modified",
                "lastModified",
                TypeInfo(datetime.datetime),
            ),
            (
                "webhook",
                "webhook",
                TypeInfo(Webhook),
            ),
            (
                "vpc_config",
                "vpcConfig",
                TypeInfo(VpcConfig),
            ),
            (
                "badge",
                "badge",
                TypeInfo(ProjectBadge),
            ),
        ]

    # The name of the build project.
    name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The Amazon Resource Name (ARN) of the build project.
    arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A description that makes the build project easy to identify.
    description: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Information about the build input source code for this build project.
    source: "ProjectSource" = dataclasses.field(default=ShapeBase.NOT_SET, )

    # An array of `ProjectSource` objects.
    secondary_sources: typing.List["ProjectSource"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Information about the build output artifacts for the build project.
    artifacts: "ProjectArtifacts" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # An array of `ProjectArtifacts` objects.
    secondary_artifacts: typing.List["ProjectArtifacts"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Information about the cache for the build project.
    cache: "ProjectCache" = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Information about the build environment for this build project.
    environment: "ProjectEnvironment" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The ARN of the AWS Identity and Access Management (IAM) role that enables
    # AWS CodeBuild to interact with dependent AWS services on behalf of the AWS
    # account.
    service_role: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # How long, in minutes, from 5 to 480 (8 hours), for AWS CodeBuild to wait
    # before timing out any related build that did not get marked as completed.
    # The default is 60 minutes.
    timeout_in_minutes: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The AWS Key Management Service (AWS KMS) customer master key (CMK) to be
    # used for encrypting the build output artifacts.

    # This is expressed either as the CMK's Amazon Resource Name (ARN) or, if
    # specified, the CMK's alias (using the format `alias/ _alias-name_ `).
    encryption_key: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The tags for this build project.

    # These tags are available for use by AWS services that support AWS CodeBuild
    # build project tags.
    tags: typing.List["Tag"] = dataclasses.field(default=ShapeBase.NOT_SET, )

    # When the build project was created, expressed in Unix time format.
    created: datetime.datetime = dataclasses.field(default=ShapeBase.NOT_SET, )

    # When the build project's settings were last modified, expressed in Unix
    # time format.
    last_modified: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Information about a webhook in GitHub that connects repository events to a
    # build project in AWS CodeBuild.
    webhook: "Webhook" = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Information about the VPC configuration that AWS CodeBuild will access.
    vpc_config: "VpcConfig" = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Information about the build badge for the build project.
    badge: "ProjectBadge" = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ProjectArtifacts(ShapeBase):
    """
    Information about the build output artifacts for the build project.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "type",
                "type",
                TypeInfo(typing.Union[str, ArtifactsType]),
            ),
            (
                "location",
                "location",
                TypeInfo(str),
            ),
            (
                "path",
                "path",
                TypeInfo(str),
            ),
            (
                "namespace_type",
                "namespaceType",
                TypeInfo(typing.Union[str, ArtifactNamespace]),
            ),
            (
                "name",
                "name",
                TypeInfo(str),
            ),
            (
                "packaging",
                "packaging",
                TypeInfo(typing.Union[str, ArtifactPackaging]),
            ),
            (
                "override_artifact_name",
                "overrideArtifactName",
                TypeInfo(bool),
            ),
            (
                "encryption_disabled",
                "encryptionDisabled",
                TypeInfo(bool),
            ),
            (
                "artifact_identifier",
                "artifactIdentifier",
                TypeInfo(str),
            ),
        ]

    # The type of build output artifact. Valid values include:

    #   * `CODEPIPELINE`: The build project will have build output generated through AWS CodePipeline.

    #   * `NO_ARTIFACTS`: The build project will not produce any build output.

    #   * `S3`: The build project will store build output in Amazon Simple Storage Service (Amazon S3).
    type: typing.Union[str, "ArtifactsType"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Information about the build output artifact location, as follows:

    #   * If `type` is set to `CODEPIPELINE`, then AWS CodePipeline will ignore this value if specified. This is because AWS CodePipeline manages its build output locations instead of AWS CodeBuild.

    #   * If `type` is set to `NO_ARTIFACTS`, then this value will be ignored if specified, because no build output will be produced.

    #   * If `type` is set to `S3`, this is the name of the output bucket.
    location: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Along with `namespaceType` and `name`, the pattern that AWS CodeBuild will
    # use to name and store the output artifact, as follows:

    #   * If `type` is set to `CODEPIPELINE`, then AWS CodePipeline will ignore this value if specified. This is because AWS CodePipeline manages its build output names instead of AWS CodeBuild.

    #   * If `type` is set to `NO_ARTIFACTS`, then this value will be ignored if specified, because no build output will be produced.

    #   * If `type` is set to `S3`, this is the path to the output artifact. If `path` is not specified, then `path` will not be used.

    # For example, if `path` is set to `MyArtifacts`, `namespaceType` is set to
    # `NONE`, and `name` is set to `MyArtifact.zip`, then the output artifact
    # would be stored in the output bucket at `MyArtifacts/MyArtifact.zip`.
    path: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Along with `path` and `name`, the pattern that AWS CodeBuild will use to
    # determine the name and location to store the output artifact, as follows:

    #   * If `type` is set to `CODEPIPELINE`, then AWS CodePipeline will ignore this value if specified. This is because AWS CodePipeline manages its build output names instead of AWS CodeBuild.

    #   * If `type` is set to `NO_ARTIFACTS`, then this value will be ignored if specified, because no build output will be produced.

    #   * If `type` is set to `S3`, then valid values include:

    #     * `BUILD_ID`: Include the build ID in the location of the build output artifact.

    #     * `NONE`: Do not include the build ID. This is the default if `namespaceType` is not specified.

    # For example, if `path` is set to `MyArtifacts`, `namespaceType` is set to
    # `BUILD_ID`, and `name` is set to `MyArtifact.zip`, then the output artifact
    # would be stored in `MyArtifacts/ _build-ID_ /MyArtifact.zip`.
    namespace_type: typing.Union[str, "ArtifactNamespace"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Along with `path` and `namespaceType`, the pattern that AWS CodeBuild will
    # use to name and store the output artifact, as follows:

    #   * If `type` is set to `CODEPIPELINE`, then AWS CodePipeline will ignore this value if specified. This is because AWS CodePipeline manages its build output names instead of AWS CodeBuild.

    #   * If `type` is set to `NO_ARTIFACTS`, then this value will be ignored if specified, because no build output will be produced.

    #   * If `type` is set to `S3`, this is the name of the output artifact object. If you set the name to be a forward slash ("/"), then the artifact is stored in the root of the output bucket.

    # For example:

    #   * If `path` is set to `MyArtifacts`, `namespaceType` is set to `BUILD_ID`, and `name` is set to `MyArtifact.zip`, then the output artifact would be stored in `MyArtifacts/ _build-ID_ /MyArtifact.zip`.

    #   * If `path` is empty, `namespaceType` is set to `NONE`, and `name` is set to "`/`", then the output artifact would be stored in the root of the output bucket.

    #   * If `path` is set to `MyArtifacts`, `namespaceType` is set to `BUILD_ID`, and `name` is set to "`/`", then the output artifact would be stored in `MyArtifacts/ _build-ID_ `.
    name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The type of build output artifact to create, as follows:

    #   * If `type` is set to `CODEPIPELINE`, then AWS CodePipeline will ignore this value if specified. This is because AWS CodePipeline manages its build output artifacts instead of AWS CodeBuild.

    #   * If `type` is set to `NO_ARTIFACTS`, then this value will be ignored if specified, because no build output will be produced.

    #   * If `type` is set to `S3`, valid values include:

    #     * `NONE`: AWS CodeBuild will create in the output bucket a folder containing the build output. This is the default if `packaging` is not specified.

    #     * `ZIP`: AWS CodeBuild will create in the output bucket a ZIP file containing the build output.
    packaging: typing.Union[str, "ArtifactPackaging"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # If this flag is set, a name specified in the buildspec file overrides the
    # artifact name. The name specified in a buildspec file is calculated at
    # build time and uses the Shell Command Language. For example, you can append
    # a date and time to your artifact name so that it is always unique.
    override_artifact_name: bool = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Set to true if you do not want your output artifacts encrypted. This option
    # is only valid if your artifacts type is Amazon S3. If this is set with
    # another artifacts type, an invalidInputException will be thrown.
    encryption_disabled: bool = dataclasses.field(default=ShapeBase.NOT_SET, )

    # An identifier for this artifact definition.
    artifact_identifier: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ProjectBadge(ShapeBase):
    """
    Information about the build badge for the build project.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "badge_enabled",
                "badgeEnabled",
                TypeInfo(bool),
            ),
            (
                "badge_request_url",
                "badgeRequestUrl",
                TypeInfo(str),
            ),
        ]

    # Set this to true to generate a publicly-accessible URL for your project's
    # build badge.
    badge_enabled: bool = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The publicly-accessible URL through which you can access the build badge
    # for your project.
    badge_request_url: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ProjectCache(ShapeBase):
    """
    Information about the cache for the build project.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "type",
                "type",
                TypeInfo(typing.Union[str, CacheType]),
            ),
            (
                "location",
                "location",
                TypeInfo(str),
            ),
        ]

    # The type of cache used by the build project. Valid values include:

    #   * `NO_CACHE`: The build project will not use any cache.

    #   * `S3`: The build project will read and write from/to S3.
    type: typing.Union[str, "CacheType"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Information about the cache location, as follows:

    #   * `NO_CACHE`: This value will be ignored.

    #   * `S3`: This is the S3 bucket name/prefix.
    location: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ProjectEnvironment(ShapeBase):
    """
    Information about the build environment of the build project.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "type",
                "type",
                TypeInfo(typing.Union[str, EnvironmentType]),
            ),
            (
                "image",
                "image",
                TypeInfo(str),
            ),
            (
                "compute_type",
                "computeType",
                TypeInfo(typing.Union[str, ComputeType]),
            ),
            (
                "environment_variables",
                "environmentVariables",
                TypeInfo(typing.List[EnvironmentVariable]),
            ),
            (
                "privileged_mode",
                "privilegedMode",
                TypeInfo(bool),
            ),
            (
                "certificate",
                "certificate",
                TypeInfo(str),
            ),
        ]

    # The type of build environment to use for related builds.
    type: typing.Union[str, "EnvironmentType"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The ID of the Docker image to use for this build project.
    image: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Information about the compute resources the build project will use.
    # Available values include:

    #   * `BUILD_GENERAL1_SMALL`: Use up to 3 GB memory and 2 vCPUs for builds.

    #   * `BUILD_GENERAL1_MEDIUM`: Use up to 7 GB memory and 4 vCPUs for builds.

    #   * `BUILD_GENERAL1_LARGE`: Use up to 15 GB memory and 8 vCPUs for builds.
    compute_type: typing.Union[str, "ComputeType"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A set of environment variables to make available to builds for this build
    # project.
    environment_variables: typing.List["EnvironmentVariable"
                                      ] = dataclasses.field(
                                          default=ShapeBase.NOT_SET,
                                      )

    # Enables running the Docker daemon inside a Docker container. Set to true
    # only if the build project is be used to build Docker images, and the
    # specified build environment image is not provided by AWS CodeBuild with
    # Docker support. Otherwise, all associated builds that attempt to interact
    # with the Docker daemon will fail. Note that you must also start the Docker
    # daemon so that builds can interact with it. One way to do this is to
    # initialize the Docker daemon during the install phase of your build spec by
    # running the following build commands. (Do not run the following build
    # commands if the specified build environment image is provided by AWS
    # CodeBuild with Docker support.)

    # If the operating system's base image is Ubuntu Linux:

    # `- nohup /usr/local/bin/dockerd --host=unix:///var/run/docker.sock
    # --host=tcp://0.0.0.0:2375 --storage-driver=overlay& - timeout 15 sh -c
    # "until docker info; do echo .; sleep 1; done"`

    # If the operating system's base image is Alpine Linux, add the `-t` argument
    # to `timeout`:

    # `- nohup /usr/local/bin/dockerd --host=unix:///var/run/docker.sock
    # --host=tcp://0.0.0.0:2375 --storage-driver=overlay& - timeout 15 -t sh -c
    # "until docker info; do echo .; sleep 1; done"`
    privileged_mode: bool = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The certificate to use with this build project.
    certificate: str = dataclasses.field(default=ShapeBase.NOT_SET, )


class ProjectSortByType(str):
    NAME = "NAME"
    CREATED_TIME = "CREATED_TIME"
    LAST_MODIFIED_TIME = "LAST_MODIFIED_TIME"


@dataclasses.dataclass
class ProjectSource(ShapeBase):
    """
    Information about the build input source code for the build project.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "type",
                "type",
                TypeInfo(typing.Union[str, SourceType]),
            ),
            (
                "location",
                "location",
                TypeInfo(str),
            ),
            (
                "git_clone_depth",
                "gitCloneDepth",
                TypeInfo(int),
            ),
            (
                "buildspec",
                "buildspec",
                TypeInfo(str),
            ),
            (
                "auth",
                "auth",
                TypeInfo(SourceAuth),
            ),
            (
                "report_build_status",
                "reportBuildStatus",
                TypeInfo(bool),
            ),
            (
                "insecure_ssl",
                "insecureSsl",
                TypeInfo(bool),
            ),
            (
                "source_identifier",
                "sourceIdentifier",
                TypeInfo(str),
            ),
        ]

    # The type of repository that contains the source code to be built. Valid
    # values include:

    #   * `BITBUCKET`: The source code is in a Bitbucket repository.

    #   * `CODECOMMIT`: The source code is in an AWS CodeCommit repository.

    #   * `CODEPIPELINE`: The source code settings are specified in the source action of a pipeline in AWS CodePipeline.

    #   * `GITHUB`: The source code is in a GitHub repository.

    #   * `S3`: The source code is in an Amazon Simple Storage Service (Amazon S3) input bucket.
    type: typing.Union[str, "SourceType"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Information about the location of the source code to be built. Valid values
    # include:

    #   * For source code settings that are specified in the source action of a pipeline in AWS CodePipeline, `location` should not be specified. If it is specified, AWS CodePipeline will ignore it. This is because AWS CodePipeline uses the settings in a pipeline's source action instead of this value.

    #   * For source code in an AWS CodeCommit repository, the HTTPS clone URL to the repository that contains the source code and the build spec (for example, `https://git-codecommit. _region-ID_.amazonaws.com/v1/repos/ _repo-name_ `).

    #   * For source code in an Amazon Simple Storage Service (Amazon S3) input bucket, the path to the ZIP file that contains the source code (for example, ` _bucket-name_ / _path_ / _to_ / _object-name_.zip`)

    #   * For source code in a GitHub repository, the HTTPS clone URL to the repository that contains the source and the build spec. Also, you must connect your AWS account to your GitHub account. To do this, use the AWS CodeBuild console to begin creating a build project. When you use the console to connect (or reconnect) with GitHub, on the GitHub **Authorize application** page that displays, for **Organization access** , choose **Request access** next to each repository you want to allow AWS CodeBuild to have access to. Then choose **Authorize application**. (After you have connected to your GitHub account, you do not need to finish creating the build project, and you may then leave the AWS CodeBuild console.) To instruct AWS CodeBuild to then use this connection, in the `source` object, set the `auth` object's `type` value to `OAUTH`.

    #   * For source code in a Bitbucket repository, the HTTPS clone URL to the repository that contains the source and the build spec. Also, you must connect your AWS account to your Bitbucket account. To do this, use the AWS CodeBuild console to begin creating a build project. When you use the console to connect (or reconnect) with Bitbucket, on the Bitbucket **Confirm access to your account** page that displays, choose **Grant access**. (After you have connected to your Bitbucket account, you do not need to finish creating the build project, and you may then leave the AWS CodeBuild console.) To instruct AWS CodeBuild to then use this connection, in the `source` object, set the `auth` object's `type` value to `OAUTH`.
    location: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Information about the git clone depth for the build project.
    git_clone_depth: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The build spec declaration to use for the builds in this build project.

    # If this value is not specified, a build spec must be included along with
    # the source code to be built.
    buildspec: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Information about the authorization settings for AWS CodeBuild to access
    # the source code to be built.

    # This information is for the AWS CodeBuild console's use only. Your code
    # should not get or set this information directly (unless the build project's
    # source `type` value is `BITBUCKET` or `GITHUB`).
    auth: "SourceAuth" = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Set to true to report the status of a build's start and finish to your
    # source provider. This option is only valid when your source provider is
    # GitHub. If this is set and you use a different source provider, an
    # invalidInputException is thrown.
    report_build_status: bool = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Enable this flag to ignore SSL warnings while connecting to the project
    # source code.
    insecure_ssl: bool = dataclasses.field(default=ShapeBase.NOT_SET, )

    # An identifier for this project source.
    source_identifier: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ProjectSourceVersion(ShapeBase):
    """
    A source identifier and its corresponding version.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "source_identifier",
                "sourceIdentifier",
                TypeInfo(str),
            ),
            (
                "source_version",
                "sourceVersion",
                TypeInfo(str),
            ),
        ]

    # An identifier for a source in the build project.
    source_identifier: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The source version for the corresponding source identifier. If specified,
    # must be one of:

    #   * For AWS CodeCommit: the commit ID to use.

    #   * For GitHub: the commit ID, pull request ID, branch name, or tag name that corresponds to the version of the source code you want to build. If a pull request ID is specified, it must use the format `pr/pull-request-ID` (for example `pr/25`). If a branch name is specified, the branch's HEAD commit ID will be used. If not specified, the default branch's HEAD commit ID will be used.

    #   * For Bitbucket: the commit ID, branch name, or tag name that corresponds to the version of the source code you want to build. If a branch name is specified, the branch's HEAD commit ID will be used. If not specified, the default branch's HEAD commit ID will be used.

    #   * For Amazon Simple Storage Service (Amazon S3): the version ID of the object representing the build input ZIP file to use.
    source_version: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ResourceAlreadyExistsException(ShapeBase):
    """
    The specified AWS resource cannot be created, because an AWS resource with the
    same settings already exists.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class ResourceNotFoundException(ShapeBase):
    """
    The specified AWS resource cannot be found.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


class SortOrderType(str):
    ASCENDING = "ASCENDING"
    DESCENDING = "DESCENDING"


@dataclasses.dataclass
class SourceAuth(ShapeBase):
    """
    Information about the authorization settings for AWS CodeBuild to access the
    source code to be built.

    This information is for the AWS CodeBuild console's use only. Your code should
    not get or set this information directly (unless the build project's source
    `type` value is `BITBUCKET` or `GITHUB`).
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "type",
                "type",
                TypeInfo(typing.Union[str, SourceAuthType]),
            ),
            (
                "resource",
                "resource",
                TypeInfo(str),
            ),
        ]

    # The authorization type to use. The only valid value is `OAUTH`, which
    # represents the OAuth authorization type.
    type: typing.Union[str, "SourceAuthType"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The resource value that applies to the specified authorization type.
    resource: str = dataclasses.field(default=ShapeBase.NOT_SET, )


class SourceAuthType(str):
    OAUTH = "OAUTH"


class SourceType(str):
    CODECOMMIT = "CODECOMMIT"
    CODEPIPELINE = "CODEPIPELINE"
    GITHUB = "GITHUB"
    S3 = "S3"
    BITBUCKET = "BITBUCKET"
    GITHUB_ENTERPRISE = "GITHUB_ENTERPRISE"
    NO_SOURCE = "NO_SOURCE"


@dataclasses.dataclass
class StartBuildInput(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "project_name",
                "projectName",
                TypeInfo(str),
            ),
            (
                "secondary_sources_override",
                "secondarySourcesOverride",
                TypeInfo(typing.List[ProjectSource]),
            ),
            (
                "secondary_sources_version_override",
                "secondarySourcesVersionOverride",
                TypeInfo(typing.List[ProjectSourceVersion]),
            ),
            (
                "source_version",
                "sourceVersion",
                TypeInfo(str),
            ),
            (
                "artifacts_override",
                "artifactsOverride",
                TypeInfo(ProjectArtifacts),
            ),
            (
                "secondary_artifacts_override",
                "secondaryArtifactsOverride",
                TypeInfo(typing.List[ProjectArtifacts]),
            ),
            (
                "environment_variables_override",
                "environmentVariablesOverride",
                TypeInfo(typing.List[EnvironmentVariable]),
            ),
            (
                "source_type_override",
                "sourceTypeOverride",
                TypeInfo(typing.Union[str, SourceType]),
            ),
            (
                "source_location_override",
                "sourceLocationOverride",
                TypeInfo(str),
            ),
            (
                "source_auth_override",
                "sourceAuthOverride",
                TypeInfo(SourceAuth),
            ),
            (
                "git_clone_depth_override",
                "gitCloneDepthOverride",
                TypeInfo(int),
            ),
            (
                "buildspec_override",
                "buildspecOverride",
                TypeInfo(str),
            ),
            (
                "insecure_ssl_override",
                "insecureSslOverride",
                TypeInfo(bool),
            ),
            (
                "report_build_status_override",
                "reportBuildStatusOverride",
                TypeInfo(bool),
            ),
            (
                "environment_type_override",
                "environmentTypeOverride",
                TypeInfo(typing.Union[str, EnvironmentType]),
            ),
            (
                "image_override",
                "imageOverride",
                TypeInfo(str),
            ),
            (
                "compute_type_override",
                "computeTypeOverride",
                TypeInfo(typing.Union[str, ComputeType]),
            ),
            (
                "certificate_override",
                "certificateOverride",
                TypeInfo(str),
            ),
            (
                "cache_override",
                "cacheOverride",
                TypeInfo(ProjectCache),
            ),
            (
                "service_role_override",
                "serviceRoleOverride",
                TypeInfo(str),
            ),
            (
                "privileged_mode_override",
                "privilegedModeOverride",
                TypeInfo(bool),
            ),
            (
                "timeout_in_minutes_override",
                "timeoutInMinutesOverride",
                TypeInfo(int),
            ),
            (
                "idempotency_token",
                "idempotencyToken",
                TypeInfo(str),
            ),
        ]

    # The name of the AWS CodeBuild build project to start running a build.
    project_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # An array of `ProjectSource` objects.
    secondary_sources_override: typing.List["ProjectSource"
                                           ] = dataclasses.field(
                                               default=ShapeBase.NOT_SET,
                                           )

    # An array of `ProjectSourceVersion` objects that specify one or more
    # versions of the project's secondary sources to be used for this build only.
    secondary_sources_version_override: typing.List[
        "ProjectSourceVersion"] = dataclasses.field(
            default=ShapeBase.NOT_SET,
        )

    # A version of the build input to be built, for this build only. If not
    # specified, the latest version will be used. If specified, must be one of:

    #   * For AWS CodeCommit: the commit ID to use.

    #   * For GitHub: the commit ID, pull request ID, branch name, or tag name that corresponds to the version of the source code you want to build. If a pull request ID is specified, it must use the format `pr/pull-request-ID` (for example `pr/25`). If a branch name is specified, the branch's HEAD commit ID will be used. If not specified, the default branch's HEAD commit ID will be used.

    #   * For Bitbucket: the commit ID, branch name, or tag name that corresponds to the version of the source code you want to build. If a branch name is specified, the branch's HEAD commit ID will be used. If not specified, the default branch's HEAD commit ID will be used.

    #   * For Amazon Simple Storage Service (Amazon S3): the version ID of the object representing the build input ZIP file to use.
    source_version: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Build output artifact settings that override, for this build only, the
    # latest ones already defined in the build project.
    artifacts_override: "ProjectArtifacts" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # An array of `ProjectArtifacts` objects.
    secondary_artifacts_override: typing.List["ProjectArtifacts"
                                             ] = dataclasses.field(
                                                 default=ShapeBase.NOT_SET,
                                             )

    # A set of environment variables that overrides, for this build only, the
    # latest ones already defined in the build project.
    environment_variables_override: typing.List["EnvironmentVariable"
                                               ] = dataclasses.field(
                                                   default=ShapeBase.NOT_SET,
                                               )

    # A source input type for this build that overrides the source input defined
    # in the build project
    source_type_override: typing.Union[str, "SourceType"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A location that overrides for this build the source location for the one
    # defined in the build project.
    source_location_override: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # An authorization type for this build that overrides the one defined in the
    # build project. This override applies only if the build project's source is
    # BitBucket or GitHub.
    source_auth_override: "SourceAuth" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The user-defined depth of history, with a minimum value of 0, that
    # overrides, for this build only, any previous depth of history defined in
    # the build project.
    git_clone_depth_override: int = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A build spec declaration that overrides, for this build only, the latest
    # one already defined in the build project.
    buildspec_override: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Enable this flag to override the insecure SSL setting that is specified in
    # the build project. The insecure SSL setting determines whether to ignore
    # SSL warnings while connecting to the project source code. This override
    # applies only if the build's source is GitHub Enterprise.
    insecure_ssl_override: bool = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Set to true to report to your source provider the status of a build's start
    # and completion. If you use this option with a source provider other than
    # GitHub, an invalidInputException is thrown.
    report_build_status_override: bool = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A container type for this build that overrides the one specified in the
    # build project.
    environment_type_override: typing.Union[str, "EnvironmentType"
                                           ] = dataclasses.field(
                                               default=ShapeBase.NOT_SET,
                                           )

    # The name of an image for this build that overrides the one specified in the
    # build project.
    image_override: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The name of a compute type for this build that overrides the one specified
    # in the build project.
    compute_type_override: typing.Union[str, "ComputeType"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The name of a certificate for this build that overrides the one specified
    # in the build project.
    certificate_override: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A ProjectCache object specified for this build that overrides the one
    # defined in the build project.
    cache_override: "ProjectCache" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The name of a service role for this build that overrides the one specified
    # in the build project.
    service_role_override: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Enable this flag to override privileged mode in the build project.
    privileged_mode_override: bool = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The number of build timeout minutes, from 5 to 480 (8 hours), that
    # overrides, for this build only, the latest setting already defined in the
    # build project.
    timeout_in_minutes_override: int = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A unique, case sensitive identifier you provide to ensure the idempotency
    # of the StartBuild request. The token is included in the StartBuild request
    # and is valid for 12 hours. If you repeat the StartBuild request with the
    # same token, but change a parameter, AWS CodeBuild returns a parameter
    # mismatch error.
    idempotency_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class StartBuildOutput(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "build",
                "build",
                TypeInfo(Build),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Information about the build to be run.
    build: "Build" = dataclasses.field(default=ShapeBase.NOT_SET, )


class StatusType(str):
    SUCCEEDED = "SUCCEEDED"
    FAILED = "FAILED"
    FAULT = "FAULT"
    TIMED_OUT = "TIMED_OUT"
    IN_PROGRESS = "IN_PROGRESS"
    STOPPED = "STOPPED"


@dataclasses.dataclass
class StopBuildInput(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "id",
                "id",
                TypeInfo(str),
            ),
        ]

    # The ID of the build.
    id: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class StopBuildOutput(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "build",
                "build",
                TypeInfo(Build),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Information about the build.
    build: "Build" = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class Tag(ShapeBase):
    """
    A tag, consisting of a key and a value.

    This tag is available for use by AWS services that support tags in AWS
    CodeBuild.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "key",
                "key",
                TypeInfo(str),
            ),
            (
                "value",
                "value",
                TypeInfo(str),
            ),
        ]

    # The tag's key.
    key: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The tag's value.
    value: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class UpdateProjectInput(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "name",
                "name",
                TypeInfo(str),
            ),
            (
                "description",
                "description",
                TypeInfo(str),
            ),
            (
                "source",
                "source",
                TypeInfo(ProjectSource),
            ),
            (
                "secondary_sources",
                "secondarySources",
                TypeInfo(typing.List[ProjectSource]),
            ),
            (
                "artifacts",
                "artifacts",
                TypeInfo(ProjectArtifacts),
            ),
            (
                "secondary_artifacts",
                "secondaryArtifacts",
                TypeInfo(typing.List[ProjectArtifacts]),
            ),
            (
                "cache",
                "cache",
                TypeInfo(ProjectCache),
            ),
            (
                "environment",
                "environment",
                TypeInfo(ProjectEnvironment),
            ),
            (
                "service_role",
                "serviceRole",
                TypeInfo(str),
            ),
            (
                "timeout_in_minutes",
                "timeoutInMinutes",
                TypeInfo(int),
            ),
            (
                "encryption_key",
                "encryptionKey",
                TypeInfo(str),
            ),
            (
                "tags",
                "tags",
                TypeInfo(typing.List[Tag]),
            ),
            (
                "vpc_config",
                "vpcConfig",
                TypeInfo(VpcConfig),
            ),
            (
                "badge_enabled",
                "badgeEnabled",
                TypeInfo(bool),
            ),
        ]

    # The name of the build project.

    # You cannot change a build project's name.
    name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A new or replacement description of the build project.
    description: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Information to be changed about the build input source code for the build
    # project.
    source: "ProjectSource" = dataclasses.field(default=ShapeBase.NOT_SET, )

    # An array of `ProjectSource` objects.
    secondary_sources: typing.List["ProjectSource"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Information to be changed about the build output artifacts for the build
    # project.
    artifacts: "ProjectArtifacts" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # An array of `ProjectSource` objects.
    secondary_artifacts: typing.List["ProjectArtifacts"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Stores recently used information so that it can be quickly accessed at a
    # later time.
    cache: "ProjectCache" = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Information to be changed about the build environment for the build
    # project.
    environment: "ProjectEnvironment" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The replacement ARN of the AWS Identity and Access Management (IAM) role
    # that enables AWS CodeBuild to interact with dependent AWS services on
    # behalf of the AWS account.
    service_role: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The replacement value in minutes, from 5 to 480 (8 hours), for AWS
    # CodeBuild to wait before timing out any related build that did not get
    # marked as completed.
    timeout_in_minutes: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The replacement AWS Key Management Service (AWS KMS) customer master key
    # (CMK) to be used for encrypting the build output artifacts.

    # You can specify either the CMK's Amazon Resource Name (ARN) or, if
    # available, the CMK's alias (using the format `alias/ _alias-name_ `).
    encryption_key: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The replacement set of tags for this build project.

    # These tags are available for use by AWS services that support AWS CodeBuild
    # build project tags.
    tags: typing.List["Tag"] = dataclasses.field(default=ShapeBase.NOT_SET, )

    # VpcConfig enables AWS CodeBuild to access resources in an Amazon VPC.
    vpc_config: "VpcConfig" = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Set this to true to generate a publicly-accessible URL for your project's
    # build badge.
    badge_enabled: bool = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class UpdateProjectOutput(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "project",
                "project",
                TypeInfo(Project),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Information about the build project that was changed.
    project: "Project" = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class UpdateWebhookInput(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "project_name",
                "projectName",
                TypeInfo(str),
            ),
            (
                "branch_filter",
                "branchFilter",
                TypeInfo(str),
            ),
            (
                "rotate_secret",
                "rotateSecret",
                TypeInfo(bool),
            ),
        ]

    # The name of the AWS CodeBuild project.
    project_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A regular expression used to determine which branches in a repository are
    # built when a webhook is triggered. If the name of a branch matches the
    # regular expression, then it is built. If it doesn't match, then it is not.
    # If branchFilter is empty, then all branches are built.
    branch_filter: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A boolean value that specifies whether the associated repository's secret
    # token should be updated.
    rotate_secret: bool = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class UpdateWebhookOutput(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "webhook",
                "webhook",
                TypeInfo(Webhook),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Information about a repository's webhook that is associated with a project
    # in AWS CodeBuild.
    webhook: "Webhook" = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class VpcConfig(ShapeBase):
    """
    Information about the VPC configuration that AWS CodeBuild will access.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "vpc_id",
                "vpcId",
                TypeInfo(str),
            ),
            (
                "subnets",
                "subnets",
                TypeInfo(typing.List[str]),
            ),
            (
                "security_group_ids",
                "securityGroupIds",
                TypeInfo(typing.List[str]),
            ),
        ]

    # The ID of the Amazon VPC.
    vpc_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A list of one or more subnet IDs in your Amazon VPC.
    subnets: typing.List[str] = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A list of one or more security groups IDs in your Amazon VPC.
    security_group_ids: typing.List[str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class Webhook(ShapeBase):
    """
    Information about a webhook in GitHub that connects repository events to a build
    project in AWS CodeBuild.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "url",
                "url",
                TypeInfo(str),
            ),
            (
                "payload_url",
                "payloadUrl",
                TypeInfo(str),
            ),
            (
                "secret",
                "secret",
                TypeInfo(str),
            ),
            (
                "branch_filter",
                "branchFilter",
                TypeInfo(str),
            ),
            (
                "last_modified_secret",
                "lastModifiedSecret",
                TypeInfo(datetime.datetime),
            ),
        ]

    # The URL to the webhook.
    url: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The CodeBuild endpoint where webhook events are sent.
    payload_url: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The secret token of the associated repository.
    secret: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A regular expression used to determine which branches in a repository are
    # built when a webhook is triggered. If the name of a branch matches the
    # regular expression, then it is built. If it doesn't match, then it is not.
    # If branchFilter is empty, then all branches are built.
    branch_filter: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A timestamp indicating the last time a repository's secret token was
    # modified.
    last_modified_secret: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )
