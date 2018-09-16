import datetime
import typing
from autoboto import ShapeBase, OutputShapeBase, TypeInfo
import dataclasses


@dataclasses.dataclass
class AssociateTeamMemberRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "project_id",
                "projectId",
                TypeInfo(str),
            ),
            (
                "user_arn",
                "userArn",
                TypeInfo(str),
            ),
            (
                "project_role",
                "projectRole",
                TypeInfo(str),
            ),
            (
                "client_request_token",
                "clientRequestToken",
                TypeInfo(str),
            ),
            (
                "remote_access_allowed",
                "remoteAccessAllowed",
                TypeInfo(bool),
            ),
        ]

    # The ID of the project to which you will add the IAM user.
    project_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The Amazon Resource Name (ARN) for the IAM user you want to add to the AWS
    # CodeStar project.
    user_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The AWS CodeStar project role that will apply to this user. This role
    # determines what actions a user can take in an AWS CodeStar project.
    project_role: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A user- or system-generated token that identifies the entity that requested
    # the team member association to the project. This token can be used to
    # repeat the request.
    client_request_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Whether the team member is allowed to use an SSH public/private key pair to
    # remotely access project resources, for example Amazon EC2 instances.
    remote_access_allowed: bool = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class AssociateTeamMemberResult(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "client_request_token",
                "clientRequestToken",
                TypeInfo(str),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The user- or system-generated token from the initial request that can be
    # used to repeat the request.
    client_request_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ConcurrentModificationException(ShapeBase):
    """
    Another modification is being made. That modification must complete before you
    can make your change.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class CreateProjectRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "name",
                "name",
                TypeInfo(str),
            ),
            (
                "id",
                "id",
                TypeInfo(str),
            ),
            (
                "description",
                "description",
                TypeInfo(str),
            ),
            (
                "client_request_token",
                "clientRequestToken",
                TypeInfo(str),
            ),
        ]

    # Reserved for future use.
    name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Reserved for future use.
    id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Reserved for future use.
    description: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Reserved for future use.
    client_request_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class CreateProjectResult(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
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
                "client_request_token",
                "clientRequestToken",
                TypeInfo(str),
            ),
            (
                "project_template_id",
                "projectTemplateId",
                TypeInfo(str),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Reserved for future use.
    id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Reserved for future use.
    arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Reserved for future use.
    client_request_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Reserved for future use.
    project_template_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class CreateUserProfileRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "user_arn",
                "userArn",
                TypeInfo(str),
            ),
            (
                "display_name",
                "displayName",
                TypeInfo(str),
            ),
            (
                "email_address",
                "emailAddress",
                TypeInfo(str),
            ),
            (
                "ssh_public_key",
                "sshPublicKey",
                TypeInfo(str),
            ),
        ]

    # The Amazon Resource Name (ARN) of the user in IAM.
    user_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The name that will be displayed as the friendly name for the user in AWS
    # CodeStar.
    display_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The email address that will be displayed as part of the user's profile in
    # AWS CodeStar.
    email_address: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The SSH public key associated with the user in AWS CodeStar. If a project
    # owner allows the user remote access to project resources, this public key
    # will be used along with the user's private key for SSH access.
    ssh_public_key: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class CreateUserProfileResult(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "user_arn",
                "userArn",
                TypeInfo(str),
            ),
            (
                "display_name",
                "displayName",
                TypeInfo(str),
            ),
            (
                "email_address",
                "emailAddress",
                TypeInfo(str),
            ),
            (
                "ssh_public_key",
                "sshPublicKey",
                TypeInfo(str),
            ),
            (
                "created_timestamp",
                "createdTimestamp",
                TypeInfo(datetime.datetime),
            ),
            (
                "last_modified_timestamp",
                "lastModifiedTimestamp",
                TypeInfo(datetime.datetime),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The Amazon Resource Name (ARN) of the user in IAM.
    user_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The name that is displayed as the friendly name for the user in AWS
    # CodeStar.
    display_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The email address that is displayed as part of the user's profile in AWS
    # CodeStar.
    email_address: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The SSH public key associated with the user in AWS CodeStar. This is the
    # public portion of the public/private keypair the user can use to access
    # project resources if a project owner allows the user remote access to those
    # resources.
    ssh_public_key: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The date the user profile was created, in timestamp format.
    created_timestamp: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The date the user profile was last modified, in timestamp format.
    last_modified_timestamp: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class DeleteProjectRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "id",
                "id",
                TypeInfo(str),
            ),
            (
                "client_request_token",
                "clientRequestToken",
                TypeInfo(str),
            ),
            (
                "delete_stack",
                "deleteStack",
                TypeInfo(bool),
            ),
        ]

    # The ID of the project to be deleted in AWS CodeStar.
    id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A user- or system-generated token that identifies the entity that requested
    # project deletion. This token can be used to repeat the request.
    client_request_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Whether to send a delete request for the primary stack in AWS
    # CloudFormation originally used to generate the project and its resources.
    # This option will delete all AWS resources for the project (except for any
    # buckets in Amazon S3) as well as deleting the project itself. Recommended
    # for most use cases.
    delete_stack: bool = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DeleteProjectResult(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "stack_id",
                "stackId",
                TypeInfo(str),
            ),
            (
                "project_arn",
                "projectArn",
                TypeInfo(str),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The ID of the primary stack in AWS CloudFormation that will be deleted as
    # part of deleting the project and its resources.
    stack_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The Amazon Resource Name (ARN) of the deleted project.
    project_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DeleteUserProfileRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "user_arn",
                "userArn",
                TypeInfo(str),
            ),
        ]

    # The Amazon Resource Name (ARN) of the user to delete from AWS CodeStar.
    user_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DeleteUserProfileResult(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "user_arn",
                "userArn",
                TypeInfo(str),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The Amazon Resource Name (ARN) of the user deleted from AWS CodeStar.
    user_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DescribeProjectRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "id",
                "id",
                TypeInfo(str),
            ),
        ]

    # The ID of the project.
    id: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DescribeProjectResult(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "name",
                "name",
                TypeInfo(str),
            ),
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
                "description",
                "description",
                TypeInfo(str),
            ),
            (
                "client_request_token",
                "clientRequestToken",
                TypeInfo(str),
            ),
            (
                "created_time_stamp",
                "createdTimeStamp",
                TypeInfo(datetime.datetime),
            ),
            (
                "stack_id",
                "stackId",
                TypeInfo(str),
            ),
            (
                "project_template_id",
                "projectTemplateId",
                TypeInfo(str),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The display name for the project.
    name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The ID of the project.
    id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The Amazon Resource Name (ARN) for the project.
    arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The description of the project, if any.
    description: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A user- or system-generated token that identifies the entity that requested
    # project creation.
    client_request_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The date and time the project was created, in timestamp format.
    created_time_stamp: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The ID of the primary stack in AWS CloudFormation used to generate
    # resources for the project.
    stack_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The ID for the AWS CodeStar project template used to create the project.
    project_template_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DescribeUserProfileRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "user_arn",
                "userArn",
                TypeInfo(str),
            ),
        ]

    # The Amazon Resource Name (ARN) of the user.
    user_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DescribeUserProfileResult(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "user_arn",
                "userArn",
                TypeInfo(str),
            ),
            (
                "created_timestamp",
                "createdTimestamp",
                TypeInfo(datetime.datetime),
            ),
            (
                "last_modified_timestamp",
                "lastModifiedTimestamp",
                TypeInfo(datetime.datetime),
            ),
            (
                "display_name",
                "displayName",
                TypeInfo(str),
            ),
            (
                "email_address",
                "emailAddress",
                TypeInfo(str),
            ),
            (
                "ssh_public_key",
                "sshPublicKey",
                TypeInfo(str),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The Amazon Resource Name (ARN) of the user.
    user_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The date and time when the user profile was created in AWS CodeStar, in
    # timestamp format.
    created_timestamp: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The date and time when the user profile was last modified, in timestamp
    # format.
    last_modified_timestamp: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The display name shown for the user in AWS CodeStar projects. For example,
    # this could be set to both first and last name ("Mary Major") or a single
    # name ("Mary"). The display name is also used to generate the initial icon
    # associated with the user in AWS CodeStar projects. If spaces are included
    # in the display name, the first character that appears after the space will
    # be used as the second character in the user initial icon. The initial icon
    # displays a maximum of two characters, so a display name with more than one
    # space (for example "Mary Jane Major") would generate an initial icon using
    # the first character and the first character after the space ("MJ", not
    # "MM").
    display_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The email address for the user. Optional.
    email_address: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The SSH public key associated with the user. This SSH public key is
    # associated with the user profile, and can be used in conjunction with the
    # associated private key for access to project resources, such as Amazon EC2
    # instances, if a project owner grants remote access to those resources.
    ssh_public_key: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DisassociateTeamMemberRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "project_id",
                "projectId",
                TypeInfo(str),
            ),
            (
                "user_arn",
                "userArn",
                TypeInfo(str),
            ),
        ]

    # The ID of the AWS CodeStar project from which you want to remove a team
    # member.
    project_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The Amazon Resource Name (ARN) of the IAM user or group whom you want to
    # remove from the project.
    user_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DisassociateTeamMemberResult(OutputShapeBase):
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
class InvalidNextTokenException(ShapeBase):
    """
    The next token is not valid.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class InvalidServiceRoleException(ShapeBase):
    """
    The service role is not valid.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class LimitExceededException(ShapeBase):
    """
    A resource limit has been exceeded.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class ListProjectsRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
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

    # The continuation token to be used to return the next set of results, if the
    # results cannot be returned in one response.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The maximum amount of data that can be contained in a single set of
    # results.
    max_results: int = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ListProjectsResult(OutputShapeBase):
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

    # A list of projects.
    projects: typing.List["ProjectSummary"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The continuation token to use when requesting the next set of results, if
    # there are more results to be returned.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ListResourcesRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "project_id",
                "projectId",
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
        ]

    # The ID of the project.
    project_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The continuation token for the next set of results, if the results cannot
    # be returned in one response.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The maximum amount of data that can be contained in a single set of
    # results.
    max_results: int = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ListResourcesResult(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "resources",
                "resources",
                TypeInfo(typing.List[Resource]),
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

    # An array of resources associated with the project.
    resources: typing.List["Resource"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The continuation token to use when requesting the next set of results, if
    # there are more results to be returned.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ListTagsForProjectRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "id",
                "id",
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
        ]

    # The ID of the project to get tags for.
    id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Reserved for future use.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Reserved for future use.
    max_results: int = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ListTagsForProjectResult(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "tags",
                "tags",
                TypeInfo(typing.Dict[str, str]),
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

    # The tags for the project.
    tags: typing.Dict[str, str] = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Reserved for future use.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ListTeamMembersRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "project_id",
                "projectId",
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
        ]

    # The ID of the project for which you want to list team members.
    project_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The continuation token for the next set of results, if the results cannot
    # be returned in one response.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The maximum number of team members you want returned in a response.
    max_results: int = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ListTeamMembersResult(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "team_members",
                "teamMembers",
                TypeInfo(typing.List[TeamMember]),
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

    # A list of team member objects for the project.
    team_members: typing.List["TeamMember"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The continuation token to use when requesting the next set of results, if
    # there are more results to be returned.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ListUserProfilesRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
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

    # The continuation token for the next set of results, if the results cannot
    # be returned in one response.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The maximum number of results to return in a response.
    max_results: int = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ListUserProfilesResult(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "user_profiles",
                "userProfiles",
                TypeInfo(typing.List[UserProfileSummary]),
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

    # All the user profiles configured in AWS CodeStar for an AWS account.
    user_profiles: typing.List["UserProfileSummary"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The continuation token to use when requesting the next set of results, if
    # there are more results to be returned.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ProjectAlreadyExistsException(ShapeBase):
    """
    An AWS CodeStar project with the same ID already exists in this region for the
    AWS account. AWS CodeStar project IDs must be unique within a region for the AWS
    account.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class ProjectConfigurationException(ShapeBase):
    """
    Project configuration information is required but not specified.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class ProjectCreationFailedException(ShapeBase):
    """
    The project creation request was valid, but a nonspecific exception or error
    occurred during project creation. The project could not be created in AWS
    CodeStar.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class ProjectNotFoundException(ShapeBase):
    """
    The specified AWS CodeStar project was not found.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class ProjectSummary(ShapeBase):
    """
    Information about the metadata for a project.
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
                "project_arn",
                "projectArn",
                TypeInfo(str),
            ),
        ]

    # The ID of the project.
    project_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The Amazon Resource Name (ARN) of the project.
    project_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class Resource(ShapeBase):
    """
    Information about a resource for a project.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "id",
                "id",
                TypeInfo(str),
            ),
        ]

    # The Amazon Resource Name (ARN) of the resource.
    id: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class TagProjectRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "id",
                "id",
                TypeInfo(str),
            ),
            (
                "tags",
                "tags",
                TypeInfo(typing.Dict[str, str]),
            ),
        ]

    # The ID of the project you want to add a tag to.
    id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The tags you want to add to the project.
    tags: typing.Dict[str, str] = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class TagProjectResult(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "tags",
                "tags",
                TypeInfo(typing.Dict[str, str]),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The tags for the project.
    tags: typing.Dict[str, str] = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class TeamMember(ShapeBase):
    """
    Information about a team member in a project.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "user_arn",
                "userArn",
                TypeInfo(str),
            ),
            (
                "project_role",
                "projectRole",
                TypeInfo(str),
            ),
            (
                "remote_access_allowed",
                "remoteAccessAllowed",
                TypeInfo(bool),
            ),
        ]

    # The Amazon Resource Name (ARN) of the user in IAM.
    user_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The role assigned to the user in the project. Project roles have different
    # levels of access. For more information, see [Working with
    # Teams](http://docs.aws.amazon.com/codestar/latest/userguide/working-with-
    # teams.html) in the _AWS CodeStar User Guide_.
    project_role: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Whether the user is allowed to remotely access project resources using an
    # SSH public/private key pair.
    remote_access_allowed: bool = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class TeamMemberAlreadyAssociatedException(ShapeBase):
    """
    The team member is already associated with a role in this project.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class TeamMemberNotFoundException(ShapeBase):
    """
    The specified team member was not found.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class UntagProjectRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "id",
                "id",
                TypeInfo(str),
            ),
            (
                "tags",
                "tags",
                TypeInfo(typing.List[str]),
            ),
        ]

    # The ID of the project to remove tags from.
    id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The tags to remove from the project.
    tags: typing.List[str] = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class UntagProjectResult(OutputShapeBase):
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
class UpdateProjectRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "id",
                "id",
                TypeInfo(str),
            ),
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
        ]

    # The ID of the project you want to update.
    id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The name of the project you want to update.
    name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The description of the project, if any.
    description: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class UpdateProjectResult(OutputShapeBase):
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
class UpdateTeamMemberRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "project_id",
                "projectId",
                TypeInfo(str),
            ),
            (
                "user_arn",
                "userArn",
                TypeInfo(str),
            ),
            (
                "project_role",
                "projectRole",
                TypeInfo(str),
            ),
            (
                "remote_access_allowed",
                "remoteAccessAllowed",
                TypeInfo(bool),
            ),
        ]

    # The ID of the project.
    project_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The Amazon Resource Name (ARN) of the user for whom you want to change team
    # membership attributes.
    user_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The role assigned to the user in the project. Project roles have different
    # levels of access. For more information, see [Working with
    # Teams](http://docs.aws.amazon.com/codestar/latest/userguide/working-with-
    # teams.html) in the _AWS CodeStar User Guide_.
    project_role: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Whether a team member is allowed to remotely access project resources using
    # the SSH public key associated with the user's profile. Even if this is set
    # to True, the user must associate a public key with their profile before the
    # user can access resources.
    remote_access_allowed: bool = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class UpdateTeamMemberResult(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "user_arn",
                "userArn",
                TypeInfo(str),
            ),
            (
                "project_role",
                "projectRole",
                TypeInfo(str),
            ),
            (
                "remote_access_allowed",
                "remoteAccessAllowed",
                TypeInfo(bool),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The Amazon Resource Name (ARN) of the user whose team membership attributes
    # were updated.
    user_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The project role granted to the user.
    project_role: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Whether a team member is allowed to remotely access project resources using
    # the SSH public key associated with the user's profile.
    remote_access_allowed: bool = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class UpdateUserProfileRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "user_arn",
                "userArn",
                TypeInfo(str),
            ),
            (
                "display_name",
                "displayName",
                TypeInfo(str),
            ),
            (
                "email_address",
                "emailAddress",
                TypeInfo(str),
            ),
            (
                "ssh_public_key",
                "sshPublicKey",
                TypeInfo(str),
            ),
        ]

    # The name that will be displayed as the friendly name for the user in AWS
    # CodeStar.
    user_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The name that is displayed as the friendly name for the user in AWS
    # CodeStar.
    display_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The email address that is displayed as part of the user's profile in AWS
    # CodeStar.
    email_address: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The SSH public key associated with the user in AWS CodeStar. If a project
    # owner allows the user remote access to project resources, this public key
    # will be used along with the user's private key for SSH access.
    ssh_public_key: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class UpdateUserProfileResult(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "user_arn",
                "userArn",
                TypeInfo(str),
            ),
            (
                "display_name",
                "displayName",
                TypeInfo(str),
            ),
            (
                "email_address",
                "emailAddress",
                TypeInfo(str),
            ),
            (
                "ssh_public_key",
                "sshPublicKey",
                TypeInfo(str),
            ),
            (
                "created_timestamp",
                "createdTimestamp",
                TypeInfo(datetime.datetime),
            ),
            (
                "last_modified_timestamp",
                "lastModifiedTimestamp",
                TypeInfo(datetime.datetime),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The Amazon Resource Name (ARN) of the user in IAM.
    user_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The name that is displayed as the friendly name for the user in AWS
    # CodeStar.
    display_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The email address that is displayed as part of the user's profile in AWS
    # CodeStar.
    email_address: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The SSH public key associated with the user in AWS CodeStar. This is the
    # public portion of the public/private keypair the user can use to access
    # project resources if a project owner allows the user remote access to those
    # resources.
    ssh_public_key: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The date the user profile was created, in timestamp format.
    created_timestamp: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The date the user profile was last modified, in timestamp format.
    last_modified_timestamp: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class UserProfileAlreadyExistsException(ShapeBase):
    """
    A user profile with that name already exists in this region for the AWS account.
    AWS CodeStar user profile names must be unique within a region for the AWS
    account.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class UserProfileNotFoundException(ShapeBase):
    """
    The user profile was not found.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class UserProfileSummary(ShapeBase):
    """
    Information about a user's profile in AWS CodeStar.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "user_arn",
                "userArn",
                TypeInfo(str),
            ),
            (
                "display_name",
                "displayName",
                TypeInfo(str),
            ),
            (
                "email_address",
                "emailAddress",
                TypeInfo(str),
            ),
            (
                "ssh_public_key",
                "sshPublicKey",
                TypeInfo(str),
            ),
        ]

    # The Amazon Resource Name (ARN) of the user in IAM.
    user_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The display name of a user in AWS CodeStar. For example, this could be set
    # to both first and last name ("Mary Major") or a single name ("Mary"). The
    # display name is also used to generate the initial icon associated with the
    # user in AWS CodeStar projects. If spaces are included in the display name,
    # the first character that appears after the space will be used as the second
    # character in the user initial icon. The initial icon displays a maximum of
    # two characters, so a display name with more than one space (for example
    # "Mary Jane Major") would generate an initial icon using the first character
    # and the first character after the space ("MJ", not "MM").
    display_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The email address associated with the user.
    email_address: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The SSH public key associated with the user in AWS CodeStar. If a project
    # owner allows the user remote access to project resources, this public key
    # will be used along with the user's private key for SSH access.
    ssh_public_key: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ValidationException(ShapeBase):
    """
    The specified input is either not valid, or it could not be validated.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []
