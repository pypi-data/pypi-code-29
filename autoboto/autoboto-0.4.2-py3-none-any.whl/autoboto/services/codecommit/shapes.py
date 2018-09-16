import datetime
import typing
from autoboto import ShapeBase, OutputShapeBase, TypeInfo
import botocore.response
import dataclasses


@dataclasses.dataclass
class ActorDoesNotExistException(ShapeBase):
    """
    The specified Amazon Resource Name (ARN) does not exist in the AWS account.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class AuthorDoesNotExistException(ShapeBase):
    """
    The specified Amazon Resource Name (ARN) does not exist in the AWS account.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class BatchGetRepositoriesInput(ShapeBase):
    """
    Represents the input of a batch get repositories operation.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "repository_names",
                "repositoryNames",
                TypeInfo(typing.List[str]),
            ),
        ]

    # The names of the repositories to get information about.
    repository_names: typing.List[str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class BatchGetRepositoriesOutput(OutputShapeBase):
    """
    Represents the output of a batch get repositories operation.
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
                "repositories",
                "repositories",
                TypeInfo(typing.List[RepositoryMetadata]),
            ),
            (
                "repositories_not_found",
                "repositoriesNotFound",
                TypeInfo(typing.List[str]),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A list of repositories returned by the batch get repositories operation.
    repositories: typing.List["RepositoryMetadata"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Returns a list of repository names for which information could not be
    # found.
    repositories_not_found: typing.List[str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class BeforeCommitIdAndAfterCommitIdAreSameException(ShapeBase):
    """
    The before commit ID and the after commit ID are the same, which is not valid.
    The before commit ID and the after commit ID must be different commit IDs.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class BlobIdDoesNotExistException(ShapeBase):
    """
    The specified blob does not exist.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class BlobIdRequiredException(ShapeBase):
    """
    A blob ID is required but was not specified.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class BlobMetadata(ShapeBase):
    """
    Returns information about a specific Git blob object.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "blob_id",
                "blobId",
                TypeInfo(str),
            ),
            (
                "path",
                "path",
                TypeInfo(str),
            ),
            (
                "mode",
                "mode",
                TypeInfo(str),
            ),
        ]

    # The full ID of the blob.
    blob_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The path to the blob and any associated file name, if any.
    path: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The file mode permissions of the blob. File mode permission codes include:

    #   * `100644` indicates read/write

    #   * `100755` indicates read/write/execute

    #   * `160000` indicates a submodule

    #   * `120000` indicates a symlink
    mode: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class BranchDoesNotExistException(ShapeBase):
    """
    The specified branch does not exist.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class BranchInfo(ShapeBase):
    """
    Returns information about a branch.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "branch_name",
                "branchName",
                TypeInfo(str),
            ),
            (
                "commit_id",
                "commitId",
                TypeInfo(str),
            ),
        ]

    # The name of the branch.
    branch_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The ID of the last commit made to the branch.
    commit_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class BranchNameExistsException(ShapeBase):
    """
    The specified branch name already exists.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class BranchNameIsTagNameException(ShapeBase):
    """
    The specified branch name is not valid because it is a tag name. Type the name
    of a current branch in the repository. For a list of valid branch names, use
    ListBranches.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class BranchNameRequiredException(ShapeBase):
    """
    A branch name is required but was not specified.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


class ChangeTypeEnum(str):
    A = "A"
    M = "M"
    D = "D"


@dataclasses.dataclass
class ClientRequestTokenRequiredException(ShapeBase):
    """
    A client request token is required. A client request token is an unique, client-
    generated idempotency token that when provided in a request, ensures the request
    cannot be repeated with a changed parameter. If a request is received with the
    same parameters and a token is included, the request will return information
    about the initial request that used that token.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class Comment(ShapeBase):
    """
    Returns information about a specific comment.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "comment_id",
                "commentId",
                TypeInfo(str),
            ),
            (
                "content",
                "content",
                TypeInfo(str),
            ),
            (
                "in_reply_to",
                "inReplyTo",
                TypeInfo(str),
            ),
            (
                "creation_date",
                "creationDate",
                TypeInfo(datetime.datetime),
            ),
            (
                "last_modified_date",
                "lastModifiedDate",
                TypeInfo(datetime.datetime),
            ),
            (
                "author_arn",
                "authorArn",
                TypeInfo(str),
            ),
            (
                "deleted",
                "deleted",
                TypeInfo(bool),
            ),
            (
                "client_request_token",
                "clientRequestToken",
                TypeInfo(str),
            ),
        ]

    # The system-generated comment ID.
    comment_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The content of the comment.
    content: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The ID of the comment for which this comment is a reply, if any.
    in_reply_to: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The date and time the comment was created, in timestamp format.
    creation_date: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The date and time the comment was most recently modified, in timestamp
    # format.
    last_modified_date: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The Amazon Resource Name (ARN) of the person who posted the comment.
    author_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A Boolean value indicating whether the comment has been deleted.
    deleted: bool = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A unique, client-generated idempotency token that when provided in a
    # request, ensures the request cannot be repeated with a changed parameter.
    # If a request is received with the same parameters and a token is included,
    # the request will return information about the initial request that used
    # that token.
    client_request_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class CommentContentRequiredException(ShapeBase):
    """
    The comment is empty. You must provide some content for a comment. The content
    cannot be null.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class CommentContentSizeLimitExceededException(ShapeBase):
    """
    The comment is too large. Comments are limited to 1,000 characters.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class CommentDeletedException(ShapeBase):
    """
    This comment has already been deleted. You cannot edit or delete a deleted
    comment.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class CommentDoesNotExistException(ShapeBase):
    """
    No comment exists with the provided ID. Verify that you have provided the
    correct ID, and then try again.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class CommentIdRequiredException(ShapeBase):
    """
    The comment ID is missing or null. A comment ID is required.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class CommentNotCreatedByCallerException(ShapeBase):
    """
    You cannot modify or delete this comment. Only comment authors can modify or
    delete their comments.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class CommentsForComparedCommit(ShapeBase):
    """
    Returns information about comments on the comparison between two commits.
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
                "before_commit_id",
                "beforeCommitId",
                TypeInfo(str),
            ),
            (
                "after_commit_id",
                "afterCommitId",
                TypeInfo(str),
            ),
            (
                "before_blob_id",
                "beforeBlobId",
                TypeInfo(str),
            ),
            (
                "after_blob_id",
                "afterBlobId",
                TypeInfo(str),
            ),
            (
                "location",
                "location",
                TypeInfo(Location),
            ),
            (
                "comments",
                "comments",
                TypeInfo(typing.List[Comment]),
            ),
        ]

    # The name of the repository that contains the compared commits.
    repository_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The full commit ID of the commit used to establish the 'before' of the
    # comparison.
    before_commit_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The full commit ID of the commit used to establish the 'after' of the
    # comparison.
    after_commit_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The full blob ID of the commit used to establish the 'before' of the
    # comparison.
    before_blob_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The full blob ID of the commit used to establish the 'after' of the
    # comparison.
    after_blob_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Location information about the comment on the comparison, including the
    # file name, line number, and whether the version of the file where the
    # comment was made is 'BEFORE' or 'AFTER'.
    location: "Location" = dataclasses.field(default=ShapeBase.NOT_SET, )

    # An array of comment objects. Each comment object contains information about
    # a comment on the comparison between commits.
    comments: typing.List["Comment"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class CommentsForPullRequest(ShapeBase):
    """
    Returns information about comments on a pull request.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "pull_request_id",
                "pullRequestId",
                TypeInfo(str),
            ),
            (
                "repository_name",
                "repositoryName",
                TypeInfo(str),
            ),
            (
                "before_commit_id",
                "beforeCommitId",
                TypeInfo(str),
            ),
            (
                "after_commit_id",
                "afterCommitId",
                TypeInfo(str),
            ),
            (
                "before_blob_id",
                "beforeBlobId",
                TypeInfo(str),
            ),
            (
                "after_blob_id",
                "afterBlobId",
                TypeInfo(str),
            ),
            (
                "location",
                "location",
                TypeInfo(Location),
            ),
            (
                "comments",
                "comments",
                TypeInfo(typing.List[Comment]),
            ),
        ]

    # The system-generated ID of the pull request.
    pull_request_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The name of the repository that contains the pull request.
    repository_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The full commit ID of the commit that was the tip of the destination branch
    # when the pull request was created. This commit will be superceded by the
    # after commit in the source branch when and if you merge the source branch
    # into the destination branch.
    before_commit_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # he full commit ID of the commit that was the tip of the source branch at
    # the time the comment was made.
    after_commit_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The full blob ID of the file on which you want to comment on the
    # destination commit.
    before_blob_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The full blob ID of the file on which you want to comment on the source
    # commit.
    after_blob_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Location information about the comment on the pull request, including the
    # file name, line number, and whether the version of the file where the
    # comment was made is 'BEFORE' (destination branch) or 'AFTER' (source
    # branch).
    location: "Location" = dataclasses.field(default=ShapeBase.NOT_SET, )

    # An array of comment objects. Each comment object contains information about
    # a comment on the pull request.
    comments: typing.List["Comment"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class Commit(ShapeBase):
    """
    Returns information about a specific commit.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "commit_id",
                "commitId",
                TypeInfo(str),
            ),
            (
                "tree_id",
                "treeId",
                TypeInfo(str),
            ),
            (
                "parents",
                "parents",
                TypeInfo(typing.List[str]),
            ),
            (
                "message",
                "message",
                TypeInfo(str),
            ),
            (
                "author",
                "author",
                TypeInfo(UserInfo),
            ),
            (
                "committer",
                "committer",
                TypeInfo(UserInfo),
            ),
            (
                "additional_data",
                "additionalData",
                TypeInfo(str),
            ),
        ]

    # The full SHA of the specified commit.
    commit_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Tree information for the specified commit.
    tree_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A list of parent commits for the specified commit. Each parent commit ID is
    # the full commit ID.
    parents: typing.List[str] = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The commit message associated with the specified commit.
    message: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Information about the author of the specified commit. Information includes
    # the date in timestamp format with GMT offset, the name of the author, and
    # the email address for the author, as configured in Git.
    author: "UserInfo" = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Information about the person who committed the specified commit, also known
    # as the committer. Information includes the date in timestamp format with
    # GMT offset, the name of the committer, and the email address for the
    # committer, as configured in Git.

    # For more information about the difference between an author and a committer
    # in Git, see [Viewing the Commit History](http://git-
    # scm.com/book/ch2-3.html) in Pro Git by Scott Chacon and Ben Straub.
    committer: "UserInfo" = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Any additional data associated with the specified commit.
    additional_data: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class CommitDoesNotExistException(ShapeBase):
    """
    The specified commit does not exist or no commit was specified, and the
    specified repository has no default branch.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class CommitIdDoesNotExistException(ShapeBase):
    """
    The specified commit ID does not exist.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class CommitIdRequiredException(ShapeBase):
    """
    A commit ID was not specified.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class CommitMessageLengthExceededException(ShapeBase):
    """
    The commit message is too long. Provide a shorter string.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class CommitRequiredException(ShapeBase):
    """
    A commit was not specified.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class CreateBranchInput(ShapeBase):
    """
    Represents the input of a create branch operation.
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
                "branch_name",
                "branchName",
                TypeInfo(str),
            ),
            (
                "commit_id",
                "commitId",
                TypeInfo(str),
            ),
        ]

    # The name of the repository in which you want to create the new branch.
    repository_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The name of the new branch to create.
    branch_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The ID of the commit to point the new branch to.
    commit_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class CreatePullRequestInput(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "title",
                "title",
                TypeInfo(str),
            ),
            (
                "targets",
                "targets",
                TypeInfo(typing.List[Target]),
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

    # The title of the pull request. This title will be used to identify the pull
    # request to other users in the repository.
    title: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The targets for the pull request, including the source of the code to be
    # reviewed (the source branch), and the destination where the creator of the
    # pull request intends the code to be merged after the pull request is closed
    # (the destination branch).
    targets: typing.List["Target"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A description of the pull request.
    description: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A unique, client-generated idempotency token that when provided in a
    # request, ensures the request cannot be repeated with a changed parameter.
    # If a request is received with the same parameters and a token is included,
    # the request will return information about the initial request that used
    # that token.

    # The AWS SDKs prepopulate client request tokens. If using an AWS SDK, you do
    # not have to generate an idempotency token, as this will be done for you.
    client_request_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class CreatePullRequestOutput(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "pull_request",
                "pullRequest",
                TypeInfo(PullRequest),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Information about the newly created pull request.
    pull_request: "PullRequest" = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class CreateRepositoryInput(ShapeBase):
    """
    Represents the input of a create repository operation.
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
                "repository_description",
                "repositoryDescription",
                TypeInfo(str),
            ),
        ]

    # The name of the new repository to be created.

    # The repository name must be unique across the calling AWS account. In
    # addition, repository names are limited to 100 alphanumeric, dash, and
    # underscore characters, and cannot include certain characters. For a full
    # description of the limits on repository names, see
    # [Limits](http://docs.aws.amazon.com/codecommit/latest/userguide/limits.html)
    # in the AWS CodeCommit User Guide. The suffix ".git" is prohibited.
    repository_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A comment or description about the new repository.

    # The description field for a repository accepts all HTML characters and all
    # valid Unicode characters. Applications that do not HTML-encode the
    # description and display it in a web page could expose users to potentially
    # malicious code. Make sure that you HTML-encode the description field in any
    # application that uses this API to display the repository description on a
    # web page.
    repository_description: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class CreateRepositoryOutput(OutputShapeBase):
    """
    Represents the output of a create repository operation.
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
                "repository_metadata",
                "repositoryMetadata",
                TypeInfo(RepositoryMetadata),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Information about the newly created repository.
    repository_metadata: "RepositoryMetadata" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class DefaultBranchCannotBeDeletedException(ShapeBase):
    """
    The specified branch is the default branch for the repository, and cannot be
    deleted. To delete this branch, you must first set another branch as the default
    branch.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class DeleteBranchInput(ShapeBase):
    """
    Represents the input of a delete branch operation.
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
                "branch_name",
                "branchName",
                TypeInfo(str),
            ),
        ]

    # The name of the repository that contains the branch to be deleted.
    repository_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The name of the branch to delete.
    branch_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DeleteBranchOutput(OutputShapeBase):
    """
    Represents the output of a delete branch operation.
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
                "deleted_branch",
                "deletedBranch",
                TypeInfo(BranchInfo),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Information about the branch deleted by the operation, including the branch
    # name and the commit ID that was the tip of the branch.
    deleted_branch: "BranchInfo" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class DeleteCommentContentInput(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "comment_id",
                "commentId",
                TypeInfo(str),
            ),
        ]

    # The unique, system-generated ID of the comment. To get this ID, use
    # GetCommentsForComparedCommit or GetCommentsForPullRequest.
    comment_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DeleteCommentContentOutput(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "comment",
                "comment",
                TypeInfo(Comment),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Information about the comment you just deleted.
    comment: "Comment" = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DeleteRepositoryInput(ShapeBase):
    """
    Represents the input of a delete repository operation.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "repository_name",
                "repositoryName",
                TypeInfo(str),
            ),
        ]

    # The name of the repository to delete.
    repository_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DeleteRepositoryOutput(OutputShapeBase):
    """
    Represents the output of a delete repository operation.
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
                "repository_id",
                "repositoryId",
                TypeInfo(str),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The ID of the repository that was deleted.
    repository_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DescribePullRequestEventsInput(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "pull_request_id",
                "pullRequestId",
                TypeInfo(str),
            ),
            (
                "pull_request_event_type",
                "pullRequestEventType",
                TypeInfo(typing.Union[str, PullRequestEventType]),
            ),
            (
                "actor_arn",
                "actorArn",
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

    # The system-generated ID of the pull request. To get this ID, use
    # ListPullRequests.
    pull_request_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Optional. The pull request event type about which you want to return
    # information.
    pull_request_event_type: typing.Union[str, "PullRequestEventType"
                                         ] = dataclasses.field(
                                             default=ShapeBase.NOT_SET,
                                         )

    # The Amazon Resource Name (ARN) of the user whose actions resulted in the
    # event. Examples include updating the pull request with additional commits
    # or changing the status of a pull request.
    actor_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # An enumeration token that when provided in a request, returns the next
    # batch of the results.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A non-negative integer used to limit the number of returned results. The
    # default is 100 events, which is also the maximum number of events that can
    # be returned in a result.
    max_results: int = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DescribePullRequestEventsOutput(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "pull_request_events",
                "pullRequestEvents",
                TypeInfo(typing.List[PullRequestEvent]),
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

    # Information about the pull request events.
    pull_request_events: typing.List["PullRequestEvent"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # An enumeration token that can be used in a request to return the next batch
    # of the results.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    def paginate(
        self,
    ) -> typing.Generator["DescribePullRequestEventsOutput", None, None]:
        yield from super()._paginate()


@dataclasses.dataclass
class Difference(ShapeBase):
    """
    Returns information about a set of differences for a commit specifier.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "before_blob",
                "beforeBlob",
                TypeInfo(BlobMetadata),
            ),
            (
                "after_blob",
                "afterBlob",
                TypeInfo(BlobMetadata),
            ),
            (
                "change_type",
                "changeType",
                TypeInfo(typing.Union[str, ChangeTypeEnum]),
            ),
        ]

    # Information about a `beforeBlob` data type object, including the ID, the
    # file mode permission code, and the path.
    before_blob: "BlobMetadata" = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Information about an `afterBlob` data type object, including the ID, the
    # file mode permission code, and the path.
    after_blob: "BlobMetadata" = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Whether the change type of the difference is an addition (A), deletion (D),
    # or modification (M).
    change_type: typing.Union[str, "ChangeTypeEnum"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class DirectoryNameConflictsWithFileNameException(ShapeBase):
    """
    A file cannot be added to the repository because the specified path name has the
    same name as a file that already exists in this repository. Either provide a
    different name for the file, or specify a different path for the file.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class EncryptionIntegrityChecksFailedException(ShapeBase):
    """
    An encryption integrity check failed.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class EncryptionKeyAccessDeniedException(ShapeBase):
    """
    An encryption key could not be accessed.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class EncryptionKeyDisabledException(ShapeBase):
    """
    The encryption key is disabled.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class EncryptionKeyNotFoundException(ShapeBase):
    """
    No encryption key was found.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class EncryptionKeyUnavailableException(ShapeBase):
    """
    The encryption key is not available.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


class FileContent(botocore.response.StreamingBody):
    pass


@dataclasses.dataclass
class FileContentRequiredException(ShapeBase):
    """
    The file cannot be added because it is empty. Empty files cannot be added to the
    repository with this API.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class FileContentSizeLimitExceededException(ShapeBase):
    """
    The file cannot be added because it is too large. The maximum file size that can
    be added using PutFile is 6 MB. For files larger than 6 MB but smaller than 2
    GB, add them using a Git client.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


class FileModeTypeEnum(str):
    EXECUTABLE = "EXECUTABLE"
    NORMAL = "NORMAL"
    SYMLINK = "SYMLINK"


@dataclasses.dataclass
class FileNameConflictsWithDirectoryNameException(ShapeBase):
    """
    A file cannot be added to the repository because the specified file name has the
    same name as a directory in this repository. Either provide another name for the
    file, or add the file in a directory that does not match the file name.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class FileTooLargeException(ShapeBase):
    """
    The specified file exceeds the file size limit for AWS CodeCommit. For more
    information about limits in AWS CodeCommit, see [AWS CodeCommit User
    Guide](http://docs.aws.amazon.com/codecommit/latest/userguide/limits.html).
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class GetBlobInput(ShapeBase):
    """
    Represents the input of a get blob operation.
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
                "blob_id",
                "blobId",
                TypeInfo(str),
            ),
        ]

    # The name of the repository that contains the blob.
    repository_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The ID of the blob, which is its SHA-1 pointer.
    blob_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class GetBlobOutput(OutputShapeBase):
    """
    Represents the output of a get blob operation.
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
                "content",
                "content",
                TypeInfo(typing.Any),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The content of the blob, usually a file.
    content: typing.Any = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class GetBranchInput(ShapeBase):
    """
    Represents the input of a get branch operation.
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
                "branch_name",
                "branchName",
                TypeInfo(str),
            ),
        ]

    # The name of the repository that contains the branch for which you want to
    # retrieve information.
    repository_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The name of the branch for which you want to retrieve information.
    branch_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class GetBranchOutput(OutputShapeBase):
    """
    Represents the output of a get branch operation.
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
                "branch",
                "branch",
                TypeInfo(BranchInfo),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The name of the branch.
    branch: "BranchInfo" = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class GetCommentInput(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "comment_id",
                "commentId",
                TypeInfo(str),
            ),
        ]

    # The unique, system-generated ID of the comment. To get this ID, use
    # GetCommentsForComparedCommit or GetCommentsForPullRequest.
    comment_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class GetCommentOutput(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "comment",
                "comment",
                TypeInfo(Comment),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The contents of the comment.
    comment: "Comment" = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class GetCommentsForComparedCommitInput(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "repository_name",
                "repositoryName",
                TypeInfo(str),
            ),
            (
                "after_commit_id",
                "afterCommitId",
                TypeInfo(str),
            ),
            (
                "before_commit_id",
                "beforeCommitId",
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

    # The name of the repository where you want to compare commits.
    repository_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # To establish the directionality of the comparison, the full commit ID of
    # the 'after' commit.
    after_commit_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # To establish the directionality of the comparison, the full commit ID of
    # the 'before' commit.
    before_commit_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # An enumeration token that when provided in a request, returns the next
    # batch of the results.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A non-negative integer used to limit the number of returned results. The
    # default is 100 comments, and is configurable up to 500.
    max_results: int = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class GetCommentsForComparedCommitOutput(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "comments_for_compared_commit_data",
                "commentsForComparedCommitData",
                TypeInfo(typing.List[CommentsForComparedCommit]),
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

    # A list of comment objects on the compared commit.
    comments_for_compared_commit_data: typing.List["CommentsForComparedCommit"
                                                  ] = dataclasses.field(
                                                      default=ShapeBase.NOT_SET,
                                                  )

    # An enumeration token that can be used in a request to return the next batch
    # of the results.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    def paginate(
        self,
    ) -> typing.Generator["GetCommentsForComparedCommitOutput", None, None]:
        yield from super()._paginate()


@dataclasses.dataclass
class GetCommentsForPullRequestInput(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "pull_request_id",
                "pullRequestId",
                TypeInfo(str),
            ),
            (
                "repository_name",
                "repositoryName",
                TypeInfo(str),
            ),
            (
                "before_commit_id",
                "beforeCommitId",
                TypeInfo(str),
            ),
            (
                "after_commit_id",
                "afterCommitId",
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

    # The system-generated ID of the pull request. To get this ID, use
    # ListPullRequests.
    pull_request_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The name of the repository that contains the pull request.
    repository_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The full commit ID of the commit in the destination branch that was the tip
    # of the branch at the time the pull request was created.
    before_commit_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The full commit ID of the commit in the source branch that was the tip of
    # the branch at the time the comment was made.
    after_commit_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # An enumeration token that when provided in a request, returns the next
    # batch of the results.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A non-negative integer used to limit the number of returned results. The
    # default is 100 comments. You can return up to 500 comments with a single
    # request.
    max_results: int = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class GetCommentsForPullRequestOutput(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "comments_for_pull_request_data",
                "commentsForPullRequestData",
                TypeInfo(typing.List[CommentsForPullRequest]),
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

    # An array of comment objects on the pull request.
    comments_for_pull_request_data: typing.List["CommentsForPullRequest"
                                               ] = dataclasses.field(
                                                   default=ShapeBase.NOT_SET,
                                               )

    # An enumeration token that can be used in a request to return the next batch
    # of the results.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    def paginate(
        self,
    ) -> typing.Generator["GetCommentsForPullRequestOutput", None, None]:
        yield from super()._paginate()


@dataclasses.dataclass
class GetCommitInput(ShapeBase):
    """
    Represents the input of a get commit operation.
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
                "commit_id",
                "commitId",
                TypeInfo(str),
            ),
        ]

    # The name of the repository to which the commit was made.
    repository_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The commit ID. Commit IDs are the full SHA of the commit.
    commit_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class GetCommitOutput(OutputShapeBase):
    """
    Represents the output of a get commit operation.
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
                "commit",
                "commit",
                TypeInfo(Commit),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A commit data type object that contains information about the specified
    # commit.
    commit: "Commit" = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class GetDifferencesInput(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "repository_name",
                "repositoryName",
                TypeInfo(str),
            ),
            (
                "after_commit_specifier",
                "afterCommitSpecifier",
                TypeInfo(str),
            ),
            (
                "before_commit_specifier",
                "beforeCommitSpecifier",
                TypeInfo(str),
            ),
            (
                "before_path",
                "beforePath",
                TypeInfo(str),
            ),
            (
                "after_path",
                "afterPath",
                TypeInfo(str),
            ),
            (
                "max_results",
                "MaxResults",
                TypeInfo(int),
            ),
            (
                "next_token",
                "NextToken",
                TypeInfo(str),
            ),
        ]

    # The name of the repository where you want to get differences.
    repository_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The branch, tag, HEAD, or other fully qualified reference used to identify
    # a commit.
    after_commit_specifier: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The branch, tag, HEAD, or other fully qualified reference used to identify
    # a commit. For example, the full commit ID. Optional. If not specified, all
    # changes prior to the `afterCommitSpecifier` value will be shown. If you do
    # not use `beforeCommitSpecifier` in your request, consider limiting the
    # results with `maxResults`.
    before_commit_specifier: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The file path in which to check for differences. Limits the results to this
    # path. Can also be used to specify the previous name of a directory or
    # folder. If `beforePath` and `afterPath` are not specified, differences will
    # be shown for all paths.
    before_path: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The file path in which to check differences. Limits the results to this
    # path. Can also be used to specify the changed name of a directory or
    # folder, if it has changed. If not specified, differences will be shown for
    # all paths.
    after_path: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A non-negative integer used to limit the number of returned results.
    max_results: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # An enumeration token that when provided in a request, returns the next
    # batch of the results.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class GetDifferencesOutput(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "differences",
                "differences",
                TypeInfo(typing.List[Difference]),
            ),
            (
                "next_token",
                "NextToken",
                TypeInfo(str),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A differences data type object that contains information about the
    # differences, including whether the difference is added, modified, or
    # deleted (A, D, M).
    differences: typing.List["Difference"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # An enumeration token that can be used in a request to return the next batch
    # of the results.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    def paginate(self,
                ) -> typing.Generator["GetDifferencesOutput", None, None]:
        yield from super()._paginate()


@dataclasses.dataclass
class GetMergeConflictsInput(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "repository_name",
                "repositoryName",
                TypeInfo(str),
            ),
            (
                "destination_commit_specifier",
                "destinationCommitSpecifier",
                TypeInfo(str),
            ),
            (
                "source_commit_specifier",
                "sourceCommitSpecifier",
                TypeInfo(str),
            ),
            (
                "merge_option",
                "mergeOption",
                TypeInfo(typing.Union[str, MergeOptionTypeEnum]),
            ),
        ]

    # The name of the repository where the pull request was created.
    repository_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The branch, tag, HEAD, or other fully qualified reference used to identify
    # a commit. For example, a branch name or a full commit ID.
    destination_commit_specifier: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The branch, tag, HEAD, or other fully qualified reference used to identify
    # a commit. For example, a branch name or a full commit ID.
    source_commit_specifier: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The merge option or strategy you want to use to merge the code. The only
    # valid value is FAST_FORWARD_MERGE.
    merge_option: typing.Union[str, "MergeOptionTypeEnum"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class GetMergeConflictsOutput(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "mergeable",
                "mergeable",
                TypeInfo(bool),
            ),
            (
                "destination_commit_id",
                "destinationCommitId",
                TypeInfo(str),
            ),
            (
                "source_commit_id",
                "sourceCommitId",
                TypeInfo(str),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A Boolean value that indicates whether the code is mergable by the
    # specified merge option.
    mergeable: bool = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The commit ID of the destination commit specifier that was used in the
    # merge evaluation.
    destination_commit_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The commit ID of the source commit specifier that was used in the merge
    # evaluation.
    source_commit_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class GetPullRequestInput(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "pull_request_id",
                "pullRequestId",
                TypeInfo(str),
            ),
        ]

    # The system-generated ID of the pull request. To get this ID, use
    # ListPullRequests.
    pull_request_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class GetPullRequestOutput(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "pull_request",
                "pullRequest",
                TypeInfo(PullRequest),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Information about the specified pull request.
    pull_request: "PullRequest" = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class GetRepositoryInput(ShapeBase):
    """
    Represents the input of a get repository operation.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "repository_name",
                "repositoryName",
                TypeInfo(str),
            ),
        ]

    # The name of the repository to get information about.
    repository_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class GetRepositoryOutput(OutputShapeBase):
    """
    Represents the output of a get repository operation.
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
                "repository_metadata",
                "repositoryMetadata",
                TypeInfo(RepositoryMetadata),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Information about the repository.
    repository_metadata: "RepositoryMetadata" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class GetRepositoryTriggersInput(ShapeBase):
    """
    Represents the input of a get repository triggers operation.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "repository_name",
                "repositoryName",
                TypeInfo(str),
            ),
        ]

    # The name of the repository for which the trigger is configured.
    repository_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class GetRepositoryTriggersOutput(OutputShapeBase):
    """
    Represents the output of a get repository triggers operation.
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
                "configuration_id",
                "configurationId",
                TypeInfo(str),
            ),
            (
                "triggers",
                "triggers",
                TypeInfo(typing.List[RepositoryTrigger]),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The system-generated unique ID for the trigger.
    configuration_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The JSON block of configuration information for each trigger.
    triggers: typing.List["RepositoryTrigger"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class IdempotencyParameterMismatchException(ShapeBase):
    """
    The client request token is not valid. Either the token is not in a valid
    format, or the token has been used in a previous request and cannot be re-used.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class InvalidActorArnException(ShapeBase):
    """
    The Amazon Resource Name (ARN) is not valid. Make sure that you have provided
    the full ARN for the user who initiated the change for the pull request, and
    then try again.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class InvalidAuthorArnException(ShapeBase):
    """
    The Amazon Resource Name (ARN) is not valid. Make sure that you have provided
    the full ARN for the author of the pull request, and then try again.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class InvalidBlobIdException(ShapeBase):
    """
    The specified blob is not valid.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class InvalidBranchNameException(ShapeBase):
    """
    The specified reference name is not valid.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class InvalidClientRequestTokenException(ShapeBase):
    """
    The client request token is not valid.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class InvalidCommentIdException(ShapeBase):
    """
    The comment ID is not in a valid format. Make sure that you have provided the
    full comment ID.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class InvalidCommitException(ShapeBase):
    """
    The specified commit is not valid.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class InvalidCommitIdException(ShapeBase):
    """
    The specified commit ID is not valid.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class InvalidContinuationTokenException(ShapeBase):
    """
    The specified continuation token is not valid.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class InvalidDescriptionException(ShapeBase):
    """
    The pull request description is not valid. Descriptions are limited to 1,000
    characters in length.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class InvalidDestinationCommitSpecifierException(ShapeBase):
    """
    The destination commit specifier is not valid. You must provide a valid branch
    name, tag, or full commit ID.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class InvalidEmailException(ShapeBase):
    """
    The specified email address either contains one or more characters that are not
    allowed, or it exceeds the maximum number of characters allowed for an email
    address.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class InvalidFileLocationException(ShapeBase):
    """
    The location of the file is not valid. Make sure that you include the extension
    of the file as well as the file name.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class InvalidFileModeException(ShapeBase):
    """
    The specified file mode permission is not valid. For a list of valid file mode
    permissions, see PutFile.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class InvalidFilePositionException(ShapeBase):
    """
    The position is not valid. Make sure that the line number exists in the version
    of the file you want to comment on.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class InvalidMaxResultsException(ShapeBase):
    """
    The specified number of maximum results is not valid.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class InvalidMergeOptionException(ShapeBase):
    """
    The specified merge option is not valid. The only valid value is
    FAST_FORWARD_MERGE.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class InvalidOrderException(ShapeBase):
    """
    The specified sort order is not valid.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class InvalidParentCommitIdException(ShapeBase):
    """
    The parent commit ID is not valid. The commit ID cannot be empty, and must match
    the head commit ID for the branch of the repository where you want to add or
    update a file.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class InvalidPathException(ShapeBase):
    """
    The specified path is not valid.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class InvalidPullRequestEventTypeException(ShapeBase):
    """
    The pull request event type is not valid.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class InvalidPullRequestIdException(ShapeBase):
    """
    The pull request ID is not valid. Make sure that you have provided the full ID
    and that the pull request is in the specified repository, and then try again.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class InvalidPullRequestStatusException(ShapeBase):
    """
    The pull request status is not valid. The only valid values are `OPEN` and
    `CLOSED`.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class InvalidPullRequestStatusUpdateException(ShapeBase):
    """
    The pull request status update is not valid. The only valid update is from
    `OPEN` to `CLOSED`.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class InvalidReferenceNameException(ShapeBase):
    """
    The specified reference name format is not valid. Reference names must conform
    to the Git references format, for example refs/heads/master. For more
    information, see [Git Internals - Git References](https://git-
    scm.com/book/en/v2/Git-Internals-Git-References) or consult your Git
    documentation.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class InvalidRelativeFileVersionEnumException(ShapeBase):
    """
    Either the enum is not in a valid format, or the specified file version enum is
    not valid in respect to the current file version.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class InvalidRepositoryDescriptionException(ShapeBase):
    """
    The specified repository description is not valid.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class InvalidRepositoryNameException(ShapeBase):
    """
    At least one specified repository name is not valid.

    This exception only occurs when a specified repository name is not valid. Other
    exceptions occur when a required repository parameter is missing, or when a
    specified repository does not exist.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class InvalidRepositoryTriggerBranchNameException(ShapeBase):
    """
    One or more branch names specified for the trigger is not valid.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class InvalidRepositoryTriggerCustomDataException(ShapeBase):
    """
    The custom data provided for the trigger is not valid.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class InvalidRepositoryTriggerDestinationArnException(ShapeBase):
    """
    The Amazon Resource Name (ARN) for the trigger is not valid for the specified
    destination. The most common reason for this error is that the ARN does not meet
    the requirements for the service type.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class InvalidRepositoryTriggerEventsException(ShapeBase):
    """
    One or more events specified for the trigger is not valid. Check to make sure
    that all events specified match the requirements for allowed events.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class InvalidRepositoryTriggerNameException(ShapeBase):
    """
    The name of the trigger is not valid.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class InvalidRepositoryTriggerRegionException(ShapeBase):
    """
    The region for the trigger target does not match the region for the repository.
    Triggers must be created in the same region as the target for the trigger.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class InvalidSortByException(ShapeBase):
    """
    The specified sort by value is not valid.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class InvalidSourceCommitSpecifierException(ShapeBase):
    """
    The source commit specifier is not valid. You must provide a valid branch name,
    tag, or full commit ID.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class InvalidTargetException(ShapeBase):
    """
    The target for the pull request is not valid. A target must contain the full
    values for the repository name, source branch, and destination branch for the
    pull request.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class InvalidTargetsException(ShapeBase):
    """
    The targets for the pull request is not valid or not in a valid format. Targets
    are a list of target objects. Each target object must contain the full values
    for the repository name, source branch, and destination branch for a pull
    request.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class InvalidTitleException(ShapeBase):
    """
    The title of the pull request is not valid. Pull request titles cannot exceed
    100 characters in length.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class ListBranchesInput(ShapeBase):
    """
    Represents the input of a list branches operation.
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
                "next_token",
                "nextToken",
                TypeInfo(str),
            ),
        ]

    # The name of the repository that contains the branches.
    repository_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # An enumeration token that allows the operation to batch the results.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ListBranchesOutput(OutputShapeBase):
    """
    Represents the output of a list branches operation.
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
                "branches",
                "branches",
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

    # The list of branch names.
    branches: typing.List[str] = dataclasses.field(default=ShapeBase.NOT_SET, )

    # An enumeration token that returns the batch of the results.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    def paginate(self, ) -> typing.Generator["ListBranchesOutput", None, None]:
        yield from super()._paginate()


@dataclasses.dataclass
class ListPullRequestsInput(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "repository_name",
                "repositoryName",
                TypeInfo(str),
            ),
            (
                "author_arn",
                "authorArn",
                TypeInfo(str),
            ),
            (
                "pull_request_status",
                "pullRequestStatus",
                TypeInfo(typing.Union[str, PullRequestStatusEnum]),
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

    # The name of the repository for which you want to list pull requests.
    repository_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Optional. The Amazon Resource Name (ARN) of the user who created the pull
    # request. If used, this filters the results to pull requests created by that
    # user.
    author_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Optional. The status of the pull request. If used, this refines the results
    # to the pull requests that match the specified status.
    pull_request_status: typing.Union[str, "PullRequestStatusEnum"
                                     ] = dataclasses.field(
                                         default=ShapeBase.NOT_SET,
                                     )

    # An enumeration token that when provided in a request, returns the next
    # batch of the results.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A non-negative integer used to limit the number of returned results.
    max_results: int = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ListPullRequestsOutput(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "pull_request_ids",
                "pullRequestIds",
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

    # The system-generated IDs of the pull requests.
    pull_request_ids: typing.List[str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # An enumeration token that when provided in a request, returns the next
    # batch of the results.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    def paginate(self,
                ) -> typing.Generator["ListPullRequestsOutput", None, None]:
        yield from super()._paginate()


@dataclasses.dataclass
class ListRepositoriesInput(ShapeBase):
    """
    Represents the input of a list repositories operation.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "next_token",
                "nextToken",
                TypeInfo(str),
            ),
            (
                "sort_by",
                "sortBy",
                TypeInfo(typing.Union[str, SortByEnum]),
            ),
            (
                "order",
                "order",
                TypeInfo(typing.Union[str, OrderEnum]),
            ),
        ]

    # An enumeration token that allows the operation to batch the results of the
    # operation. Batch sizes are 1,000 for list repository operations. When the
    # client sends the token back to AWS CodeCommit, another page of 1,000
    # records is retrieved.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The criteria used to sort the results of a list repositories operation.
    sort_by: typing.Union[str, "SortByEnum"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The order in which to sort the results of a list repositories operation.
    order: typing.Union[str, "OrderEnum"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class ListRepositoriesOutput(OutputShapeBase):
    """
    Represents the output of a list repositories operation.
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
                "repositories",
                "repositories",
                TypeInfo(typing.List[RepositoryNameIdPair]),
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

    # Lists the repositories called by the list repositories operation.
    repositories: typing.List["RepositoryNameIdPair"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # An enumeration token that allows the operation to batch the results of the
    # operation. Batch sizes are 1,000 for list repository operations. When the
    # client sends the token back to AWS CodeCommit, another page of 1,000
    # records is retrieved.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    def paginate(self,
                ) -> typing.Generator["ListRepositoriesOutput", None, None]:
        yield from super()._paginate()


@dataclasses.dataclass
class Location(ShapeBase):
    """
    Returns information about the location of a change or comment in the comparison
    between two commits or a pull request.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "file_path",
                "filePath",
                TypeInfo(str),
            ),
            (
                "file_position",
                "filePosition",
                TypeInfo(int),
            ),
            (
                "relative_file_version",
                "relativeFileVersion",
                TypeInfo(typing.Union[str, RelativeFileVersionEnum]),
            ),
        ]

    # The name of the file being compared, including its extension and
    # subdirectory, if any.
    file_path: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The position of a change within a compared file, in line number format.
    file_position: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # In a comparison of commits or a pull request, whether the change is in the
    # 'before' or 'after' of that comparison.
    relative_file_version: typing.Union[str, "RelativeFileVersionEnum"
                                       ] = dataclasses.field(
                                           default=ShapeBase.NOT_SET,
                                       )


@dataclasses.dataclass
class ManualMergeRequiredException(ShapeBase):
    """
    The pull request cannot be merged automatically into the destination branch. You
    must manually merge the branches and resolve any conflicts.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class MaximumBranchesExceededException(ShapeBase):
    """
    The number of branches for the trigger was exceeded.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class MaximumOpenPullRequestsExceededException(ShapeBase):
    """
    You cannot create the pull request because the repository has too many open pull
    requests. The maximum number of open pull requests for a repository is 1,000.
    Close one or more open pull requests, and then try again.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class MaximumRepositoryNamesExceededException(ShapeBase):
    """
    The maximum number of allowed repository names was exceeded. Currently, this
    number is 25.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class MaximumRepositoryTriggersExceededException(ShapeBase):
    """
    The number of triggers allowed for the repository was exceeded.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class MergeMetadata(ShapeBase):
    """
    Returns information about a merge or potential merge between a source reference
    and a destination reference in a pull request.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "is_merged",
                "isMerged",
                TypeInfo(bool),
            ),
            (
                "merged_by",
                "mergedBy",
                TypeInfo(str),
            ),
        ]

    # A Boolean value indicating whether the merge has been made.
    is_merged: bool = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The Amazon Resource Name (ARN) of the user who merged the branches.
    merged_by: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class MergeOptionRequiredException(ShapeBase):
    """
    A merge option or stategy is required, and none was provided.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


class MergeOptionTypeEnum(str):
    FAST_FORWARD_MERGE = "FAST_FORWARD_MERGE"


@dataclasses.dataclass
class MergePullRequestByFastForwardInput(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "pull_request_id",
                "pullRequestId",
                TypeInfo(str),
            ),
            (
                "repository_name",
                "repositoryName",
                TypeInfo(str),
            ),
            (
                "source_commit_id",
                "sourceCommitId",
                TypeInfo(str),
            ),
        ]

    # The system-generated ID of the pull request. To get this ID, use
    # ListPullRequests.
    pull_request_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The name of the repository where the pull request was created.
    repository_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The full commit ID of the original or updated commit in the pull request
    # source branch. Pass this value if you want an exception thrown if the
    # current commit ID of the tip of the source branch does not match this
    # commit ID.
    source_commit_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class MergePullRequestByFastForwardOutput(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "pull_request",
                "pullRequest",
                TypeInfo(PullRequest),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Information about the specified pull request, including information about
    # the merge.
    pull_request: "PullRequest" = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class MultipleRepositoriesInPullRequestException(ShapeBase):
    """
    You cannot include more than one repository in a pull request. Make sure you
    have specified only one repository name in your request, and then try again.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class NameLengthExceededException(ShapeBase):
    """
    The file name is not valid because it has exceeded the character limit for file
    names. File names, including the path to the file, cannot exceed the character
    limit.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


class OrderEnum(str):
    ascending = "ascending"
    descending = "descending"


@dataclasses.dataclass
class ParentCommitDoesNotExistException(ShapeBase):
    """
    The parent commit ID is not valid. The specified parent commit ID does not exist
    in the specified branch of the repository.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class ParentCommitIdOutdatedException(ShapeBase):
    """
    The file could not be added because the provided parent commit ID is not the
    current tip of the specified branch. To view the full commit ID of the current
    head of the branch, use GetBranch.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class ParentCommitIdRequiredException(ShapeBase):
    """
    A parent commit ID is required. To view the full commit ID of a branch in a
    repository, use GetBranch or a Git command (for example, git pull or git log).
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class PathDoesNotExistException(ShapeBase):
    """
    The specified path does not exist.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class PathRequiredException(ShapeBase):
    """
    The filePath for a location cannot be empty or null.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class PostCommentForComparedCommitInput(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "repository_name",
                "repositoryName",
                TypeInfo(str),
            ),
            (
                "after_commit_id",
                "afterCommitId",
                TypeInfo(str),
            ),
            (
                "content",
                "content",
                TypeInfo(str),
            ),
            (
                "before_commit_id",
                "beforeCommitId",
                TypeInfo(str),
            ),
            (
                "location",
                "location",
                TypeInfo(Location),
            ),
            (
                "client_request_token",
                "clientRequestToken",
                TypeInfo(str),
            ),
        ]

    # The name of the repository where you want to post a comment on the
    # comparison between commits.
    repository_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # To establish the directionality of the comparison, the full commit ID of
    # the 'after' commit.
    after_commit_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The content of the comment you want to make.
    content: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # To establish the directionality of the comparison, the full commit ID of
    # the 'before' commit.
    before_commit_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The location of the comparison where you want to comment.
    location: "Location" = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A unique, client-generated idempotency token that when provided in a
    # request, ensures the request cannot be repeated with a changed parameter.
    # If a request is received with the same parameters and a token is included,
    # the request will return information about the initial request that used
    # that token.
    client_request_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class PostCommentForComparedCommitOutput(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "repository_name",
                "repositoryName",
                TypeInfo(str),
            ),
            (
                "before_commit_id",
                "beforeCommitId",
                TypeInfo(str),
            ),
            (
                "after_commit_id",
                "afterCommitId",
                TypeInfo(str),
            ),
            (
                "before_blob_id",
                "beforeBlobId",
                TypeInfo(str),
            ),
            (
                "after_blob_id",
                "afterBlobId",
                TypeInfo(str),
            ),
            (
                "location",
                "location",
                TypeInfo(Location),
            ),
            (
                "comment",
                "comment",
                TypeInfo(Comment),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The name of the repository where you posted a comment on the comparison
    # between commits.
    repository_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # In the directionality you established, the full commit ID of the 'before'
    # commit.
    before_commit_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # In the directionality you established, the full commit ID of the 'after'
    # commit.
    after_commit_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # In the directionality you established, the blob ID of the 'before' blob.
    before_blob_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # In the directionality you established, the blob ID of the 'after' blob.
    after_blob_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The location of the comment in the comparison between the two commits.
    location: "Location" = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The content of the comment you posted.
    comment: "Comment" = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class PostCommentForPullRequestInput(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "pull_request_id",
                "pullRequestId",
                TypeInfo(str),
            ),
            (
                "repository_name",
                "repositoryName",
                TypeInfo(str),
            ),
            (
                "before_commit_id",
                "beforeCommitId",
                TypeInfo(str),
            ),
            (
                "after_commit_id",
                "afterCommitId",
                TypeInfo(str),
            ),
            (
                "content",
                "content",
                TypeInfo(str),
            ),
            (
                "location",
                "location",
                TypeInfo(Location),
            ),
            (
                "client_request_token",
                "clientRequestToken",
                TypeInfo(str),
            ),
        ]

    # The system-generated ID of the pull request. To get this ID, use
    # ListPullRequests.
    pull_request_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The name of the repository where you want to post a comment on a pull
    # request.
    repository_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The full commit ID of the commit in the destination branch that was the tip
    # of the branch at the time the pull request was created.
    before_commit_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The full commit ID of the commit in the source branch that is the current
    # tip of the branch for the pull request when you post the comment.
    after_commit_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The content of your comment on the change.
    content: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The location of the change where you want to post your comment. If no
    # location is provided, the comment will be posted as a general comment on
    # the pull request difference between the before commit ID and the after
    # commit ID.
    location: "Location" = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A unique, client-generated idempotency token that when provided in a
    # request, ensures the request cannot be repeated with a changed parameter.
    # If a request is received with the same parameters and a token is included,
    # the request will return information about the initial request that used
    # that token.
    client_request_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class PostCommentForPullRequestOutput(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "repository_name",
                "repositoryName",
                TypeInfo(str),
            ),
            (
                "pull_request_id",
                "pullRequestId",
                TypeInfo(str),
            ),
            (
                "before_commit_id",
                "beforeCommitId",
                TypeInfo(str),
            ),
            (
                "after_commit_id",
                "afterCommitId",
                TypeInfo(str),
            ),
            (
                "before_blob_id",
                "beforeBlobId",
                TypeInfo(str),
            ),
            (
                "after_blob_id",
                "afterBlobId",
                TypeInfo(str),
            ),
            (
                "location",
                "location",
                TypeInfo(Location),
            ),
            (
                "comment",
                "comment",
                TypeInfo(Comment),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The name of the repository where you posted a comment on a pull request.
    repository_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The system-generated ID of the pull request.
    pull_request_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The full commit ID of the commit in the source branch used to create the
    # pull request, or in the case of an updated pull request, the full commit ID
    # of the commit used to update the pull request.
    before_commit_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The full commit ID of the commit in the destination branch where the pull
    # request will be merged.
    after_commit_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # In the directionality of the pull request, the blob ID of the 'before'
    # blob.
    before_blob_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # In the directionality of the pull request, the blob ID of the 'after' blob.
    after_blob_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The location of the change where you posted your comment.
    location: "Location" = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The content of the comment you posted.
    comment: "Comment" = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class PostCommentReplyInput(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "in_reply_to",
                "inReplyTo",
                TypeInfo(str),
            ),
            (
                "content",
                "content",
                TypeInfo(str),
            ),
            (
                "client_request_token",
                "clientRequestToken",
                TypeInfo(str),
            ),
        ]

    # The system-generated ID of the comment to which you want to reply. To get
    # this ID, use GetCommentsForComparedCommit or GetCommentsForPullRequest.
    in_reply_to: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The contents of your reply to a comment.
    content: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A unique, client-generated idempotency token that when provided in a
    # request, ensures the request cannot be repeated with a changed parameter.
    # If a request is received with the same parameters and a token is included,
    # the request will return information about the initial request that used
    # that token.
    client_request_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class PostCommentReplyOutput(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "comment",
                "comment",
                TypeInfo(Comment),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Information about the reply to a comment.
    comment: "Comment" = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class PullRequest(ShapeBase):
    """
    Returns information about a pull request.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "pull_request_id",
                "pullRequestId",
                TypeInfo(str),
            ),
            (
                "title",
                "title",
                TypeInfo(str),
            ),
            (
                "description",
                "description",
                TypeInfo(str),
            ),
            (
                "last_activity_date",
                "lastActivityDate",
                TypeInfo(datetime.datetime),
            ),
            (
                "creation_date",
                "creationDate",
                TypeInfo(datetime.datetime),
            ),
            (
                "pull_request_status",
                "pullRequestStatus",
                TypeInfo(typing.Union[str, PullRequestStatusEnum]),
            ),
            (
                "author_arn",
                "authorArn",
                TypeInfo(str),
            ),
            (
                "pull_request_targets",
                "pullRequestTargets",
                TypeInfo(typing.List[PullRequestTarget]),
            ),
            (
                "client_request_token",
                "clientRequestToken",
                TypeInfo(str),
            ),
        ]

    # The system-generated ID of the pull request.
    pull_request_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The user-defined title of the pull request. This title is displayed in the
    # list of pull requests to other users of the repository.
    title: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The user-defined description of the pull request. This description can be
    # used to clarify what should be reviewed and other details of the request.
    description: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The day and time of the last user or system activity on the pull request,
    # in timestamp format.
    last_activity_date: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The date and time the pull request was originally created, in timestamp
    # format.
    creation_date: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The status of the pull request. Pull request status can only change from
    # `OPEN` to `CLOSED`.
    pull_request_status: typing.Union[str, "PullRequestStatusEnum"
                                     ] = dataclasses.field(
                                         default=ShapeBase.NOT_SET,
                                     )

    # The Amazon Resource Name (ARN) of the user who created the pull request.
    author_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The targets of the pull request, including the source branch and
    # destination branch for the pull request.
    pull_request_targets: typing.List["PullRequestTarget"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A unique, client-generated idempotency token that when provided in a
    # request, ensures the request cannot be repeated with a changed parameter.
    # If a request is received with the same parameters and a token is included,
    # the request will return information about the initial request that used
    # that token.
    client_request_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class PullRequestAlreadyClosedException(ShapeBase):
    """
    The pull request status cannot be updated because it is already closed.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class PullRequestCreatedEventMetadata(ShapeBase):
    """
    Metadata about the pull request that is used when comparing the pull request
    source with its destination.
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
                "source_commit_id",
                "sourceCommitId",
                TypeInfo(str),
            ),
            (
                "destination_commit_id",
                "destinationCommitId",
                TypeInfo(str),
            ),
            (
                "merge_base",
                "mergeBase",
                TypeInfo(str),
            ),
        ]

    # The name of the repository where the pull request was created.
    repository_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The commit ID on the source branch used when the pull request was created.
    source_commit_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The commit ID of the tip of the branch specified as the destination branch
    # when the pull request was created.
    destination_commit_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The commit ID of the most recent commit that the source branch and the
    # destination branch have in common.
    merge_base: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class PullRequestDoesNotExistException(ShapeBase):
    """
    The pull request ID could not be found. Make sure that you have specified the
    correct repository name and pull request ID, and then try again.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class PullRequestEvent(ShapeBase):
    """
    Returns information about a pull request event.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "pull_request_id",
                "pullRequestId",
                TypeInfo(str),
            ),
            (
                "event_date",
                "eventDate",
                TypeInfo(datetime.datetime),
            ),
            (
                "pull_request_event_type",
                "pullRequestEventType",
                TypeInfo(typing.Union[str, PullRequestEventType]),
            ),
            (
                "actor_arn",
                "actorArn",
                TypeInfo(str),
            ),
            (
                "pull_request_created_event_metadata",
                "pullRequestCreatedEventMetadata",
                TypeInfo(PullRequestCreatedEventMetadata),
            ),
            (
                "pull_request_status_changed_event_metadata",
                "pullRequestStatusChangedEventMetadata",
                TypeInfo(PullRequestStatusChangedEventMetadata),
            ),
            (
                "pull_request_source_reference_updated_event_metadata",
                "pullRequestSourceReferenceUpdatedEventMetadata",
                TypeInfo(PullRequestSourceReferenceUpdatedEventMetadata),
            ),
            (
                "pull_request_merged_state_changed_event_metadata",
                "pullRequestMergedStateChangedEventMetadata",
                TypeInfo(PullRequestMergedStateChangedEventMetadata),
            ),
        ]

    # The system-generated ID of the pull request.
    pull_request_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The day and time of the pull request event, in timestamp format.
    event_date: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The type of the pull request event, for example a status change event
    # (PULL_REQUEST_STATUS_CHANGED) or update event
    # (PULL_REQUEST_SOURCE_REFERENCE_UPDATED).
    pull_request_event_type: typing.Union[str, "PullRequestEventType"
                                         ] = dataclasses.field(
                                             default=ShapeBase.NOT_SET,
                                         )

    # The Amazon Resource Name (ARN) of the user whose actions resulted in the
    # event. Examples include updating the pull request with additional commits
    # or changing the status of a pull request.
    actor_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Information about the source and destination branches for the pull request.
    pull_request_created_event_metadata: "PullRequestCreatedEventMetadata" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Information about the change in status for the pull request event.
    pull_request_status_changed_event_metadata: "PullRequestStatusChangedEventMetadata" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Information about the updated source branch for the pull request event.
    pull_request_source_reference_updated_event_metadata: "PullRequestSourceReferenceUpdatedEventMetadata" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Information about the change in mergability state for the pull request
    # event.
    pull_request_merged_state_changed_event_metadata: "PullRequestMergedStateChangedEventMetadata" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


class PullRequestEventType(str):
    PULL_REQUEST_CREATED = "PULL_REQUEST_CREATED"
    PULL_REQUEST_STATUS_CHANGED = "PULL_REQUEST_STATUS_CHANGED"
    PULL_REQUEST_SOURCE_REFERENCE_UPDATED = "PULL_REQUEST_SOURCE_REFERENCE_UPDATED"
    PULL_REQUEST_MERGE_STATE_CHANGED = "PULL_REQUEST_MERGE_STATE_CHANGED"


@dataclasses.dataclass
class PullRequestIdRequiredException(ShapeBase):
    """
    A pull request ID is required, but none was provided.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class PullRequestMergedStateChangedEventMetadata(ShapeBase):
    """
    Returns information about the change in the merge state for a pull request
    event.
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
                "destination_reference",
                "destinationReference",
                TypeInfo(str),
            ),
            (
                "merge_metadata",
                "mergeMetadata",
                TypeInfo(MergeMetadata),
            ),
        ]

    # The name of the repository where the pull request was created.
    repository_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The name of the branch that the pull request will be merged into.
    destination_reference: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Information about the merge state change event.
    merge_metadata: "MergeMetadata" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class PullRequestSourceReferenceUpdatedEventMetadata(ShapeBase):
    """
    Information about an update to the source branch of a pull request.
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
                "before_commit_id",
                "beforeCommitId",
                TypeInfo(str),
            ),
            (
                "after_commit_id",
                "afterCommitId",
                TypeInfo(str),
            ),
            (
                "merge_base",
                "mergeBase",
                TypeInfo(str),
            ),
        ]

    # The name of the repository where the pull request was updated.
    repository_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The full commit ID of the commit in the destination branch that was the tip
    # of the branch at the time the pull request was updated.
    before_commit_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The full commit ID of the commit in the source branch that was the tip of
    # the branch at the time the pull request was updated.
    after_commit_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The commit ID of the most recent commit that the source branch and the
    # destination branch have in common.
    merge_base: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class PullRequestStatusChangedEventMetadata(ShapeBase):
    """
    Information about a change to the status of a pull request.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "pull_request_status",
                "pullRequestStatus",
                TypeInfo(typing.Union[str, PullRequestStatusEnum]),
            ),
        ]

    # The changed status of the pull request.
    pull_request_status: typing.Union[str, "PullRequestStatusEnum"
                                     ] = dataclasses.field(
                                         default=ShapeBase.NOT_SET,
                                     )


class PullRequestStatusEnum(str):
    OPEN = "OPEN"
    CLOSED = "CLOSED"


@dataclasses.dataclass
class PullRequestStatusRequiredException(ShapeBase):
    """
    A pull request status is required, but none was provided.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class PullRequestTarget(ShapeBase):
    """
    Returns information about a pull request target.
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
                "source_reference",
                "sourceReference",
                TypeInfo(str),
            ),
            (
                "destination_reference",
                "destinationReference",
                TypeInfo(str),
            ),
            (
                "destination_commit",
                "destinationCommit",
                TypeInfo(str),
            ),
            (
                "merge_base",
                "mergeBase",
                TypeInfo(str),
            ),
            (
                "source_commit",
                "sourceCommit",
                TypeInfo(str),
            ),
            (
                "merge_metadata",
                "mergeMetadata",
                TypeInfo(MergeMetadata),
            ),
        ]

    # The name of the repository that contains the pull request source and
    # destination branches.
    repository_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The branch of the repository that contains the changes for the pull
    # request. Also known as the source branch.
    source_reference: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The branch of the repository where the pull request changes will be merged
    # into. Also known as the destination branch.
    destination_reference: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The full commit ID that is the tip of the destination branch. This is the
    # commit where the pull request was or will be merged.
    destination_commit: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The commit ID of the most recent commit that the source branch and the
    # destination branch have in common.
    merge_base: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The full commit ID of the tip of the source branch used to create the pull
    # request. If the pull request branch is updated by a push while the pull
    # request is open, the commit ID will change to reflect the new tip of the
    # branch.
    source_commit: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Returns metadata about the state of the merge, including whether the merge
    # has been made.
    merge_metadata: "MergeMetadata" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class PutFileInput(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "repository_name",
                "repositoryName",
                TypeInfo(str),
            ),
            (
                "branch_name",
                "branchName",
                TypeInfo(str),
            ),
            (
                "file_content",
                "fileContent",
                TypeInfo(typing.Any),
            ),
            (
                "file_path",
                "filePath",
                TypeInfo(str),
            ),
            (
                "file_mode",
                "fileMode",
                TypeInfo(typing.Union[str, FileModeTypeEnum]),
            ),
            (
                "parent_commit_id",
                "parentCommitId",
                TypeInfo(str),
            ),
            (
                "commit_message",
                "commitMessage",
                TypeInfo(str),
            ),
            (
                "name",
                "name",
                TypeInfo(str),
            ),
            (
                "email",
                "email",
                TypeInfo(str),
            ),
        ]

    # The name of the repository where you want to add or update the file.
    repository_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The name of the branch where you want to add or update the file. If this is
    # an empty repository, this branch will be created.
    branch_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The content of the file, in binary object format.
    file_content: typing.Any = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The name of the file you want to add or update, including the relative path
    # to the file in the repository.

    # If the path does not currently exist in the repository, the path will be
    # created as part of adding the file.
    file_path: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The file mode permissions of the blob. Valid file mode permissions are
    # listed below.
    file_mode: typing.Union[str, "FileModeTypeEnum"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The full commit ID of the head commit in the branch where you want to add
    # or update the file. If this is an empty repository, no commit ID is
    # required. If this is not an empty repository, a commit ID is required.

    # The commit ID must match the ID of the head commit at the time of the
    # operation, or an error will occur, and the file will not be added or
    # updated.
    parent_commit_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A message about why this file was added or updated. While optional, adding
    # a message is strongly encouraged in order to provide a more useful commit
    # history for your repository.
    commit_message: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The name of the person adding or updating the file. While optional, adding
    # a name is strongly encouraged in order to provide a more useful commit
    # history for your repository.
    name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # An email address for the person adding or updating the file.
    email: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class PutFileOutput(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "commit_id",
                "commitId",
                TypeInfo(str),
            ),
            (
                "blob_id",
                "blobId",
                TypeInfo(str),
            ),
            (
                "tree_id",
                "treeId",
                TypeInfo(str),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The full SHA of the commit that contains this file change.
    commit_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The ID of the blob, which is its SHA-1 pointer.
    blob_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The full SHA-1 pointer of the tree information for the commit that contains
    # this file change.
    tree_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class PutRepositoryTriggersInput(ShapeBase):
    """
    Represents the input ofa put repository triggers operation.
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
                "triggers",
                "triggers",
                TypeInfo(typing.List[RepositoryTrigger]),
            ),
        ]

    # The name of the repository where you want to create or update the trigger.
    repository_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The JSON block of configuration information for each trigger.
    triggers: typing.List["RepositoryTrigger"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class PutRepositoryTriggersOutput(OutputShapeBase):
    """
    Represents the output of a put repository triggers operation.
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
                "configuration_id",
                "configurationId",
                TypeInfo(str),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The system-generated unique ID for the create or update operation.
    configuration_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ReferenceDoesNotExistException(ShapeBase):
    """
    The specified reference does not exist. You must provide a full commit ID.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class ReferenceNameRequiredException(ShapeBase):
    """
    A reference name is required, but none was provided.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class ReferenceTypeNotSupportedException(ShapeBase):
    """
    The specified reference is not a supported type.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


class RelativeFileVersionEnum(str):
    BEFORE = "BEFORE"
    AFTER = "AFTER"


@dataclasses.dataclass
class RepositoryDoesNotExistException(ShapeBase):
    """
    The specified repository does not exist.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class RepositoryLimitExceededException(ShapeBase):
    """
    A repository resource limit was exceeded.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class RepositoryMetadata(ShapeBase):
    """
    Information about a repository.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "account_id",
                "accountId",
                TypeInfo(str),
            ),
            (
                "repository_id",
                "repositoryId",
                TypeInfo(str),
            ),
            (
                "repository_name",
                "repositoryName",
                TypeInfo(str),
            ),
            (
                "repository_description",
                "repositoryDescription",
                TypeInfo(str),
            ),
            (
                "default_branch",
                "defaultBranch",
                TypeInfo(str),
            ),
            (
                "last_modified_date",
                "lastModifiedDate",
                TypeInfo(datetime.datetime),
            ),
            (
                "creation_date",
                "creationDate",
                TypeInfo(datetime.datetime),
            ),
            (
                "clone_url_http",
                "cloneUrlHttp",
                TypeInfo(str),
            ),
            (
                "clone_url_ssh",
                "cloneUrlSsh",
                TypeInfo(str),
            ),
            (
                "arn",
                "Arn",
                TypeInfo(str),
            ),
        ]

    # The ID of the AWS account associated with the repository.
    account_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The ID of the repository.
    repository_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The repository's name.
    repository_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A comment or description about the repository.
    repository_description: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The repository's default branch name.
    default_branch: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The date and time the repository was last modified, in timestamp format.
    last_modified_date: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The date and time the repository was created, in timestamp format.
    creation_date: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The URL to use for cloning the repository over HTTPS.
    clone_url_http: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The URL to use for cloning the repository over SSH.
    clone_url_ssh: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The Amazon Resource Name (ARN) of the repository.
    arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class RepositoryNameExistsException(ShapeBase):
    """
    The specified repository name already exists.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class RepositoryNameIdPair(ShapeBase):
    """
    Information about a repository name and ID.
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
                "repository_id",
                "repositoryId",
                TypeInfo(str),
            ),
        ]

    # The name associated with the repository.
    repository_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The ID associated with the repository.
    repository_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class RepositoryNameRequiredException(ShapeBase):
    """
    A repository name is required but was not specified.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class RepositoryNamesRequiredException(ShapeBase):
    """
    A repository names object is required but was not specified.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class RepositoryNotAssociatedWithPullRequestException(ShapeBase):
    """
    The repository does not contain any pull requests with that pull request ID.
    Check to make sure you have provided the correct repository name for the pull
    request.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class RepositoryTrigger(ShapeBase):
    """
    Information about a trigger for a repository.
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
                "destination_arn",
                "destinationArn",
                TypeInfo(str),
            ),
            (
                "events",
                "events",
                TypeInfo(
                    typing.List[typing.Union[str, RepositoryTriggerEventEnum]]
                ),
            ),
            (
                "custom_data",
                "customData",
                TypeInfo(str),
            ),
            (
                "branches",
                "branches",
                TypeInfo(typing.List[str]),
            ),
        ]

    # The name of the trigger.
    name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The ARN of the resource that is the target for a trigger. For example, the
    # ARN of a topic in Amazon Simple Notification Service (SNS).
    destination_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The repository events that will cause the trigger to run actions in another
    # service, such as sending a notification through Amazon Simple Notification
    # Service (SNS).

    # The valid value "all" cannot be used with any other values.
    events: typing.List[typing.Union[str, "RepositoryTriggerEventEnum"]
                       ] = dataclasses.field(
                           default=ShapeBase.NOT_SET,
                       )

    # Any custom data associated with the trigger that will be included in the
    # information sent to the target of the trigger.
    custom_data: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The branches that will be included in the trigger configuration. If you
    # specify an empty array, the trigger will apply to all branches.

    # While no content is required in the array, you must include the array
    # itself.
    branches: typing.List[str] = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class RepositoryTriggerBranchNameListRequiredException(ShapeBase):
    """
    At least one branch name is required but was not specified in the trigger
    configuration.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class RepositoryTriggerDestinationArnRequiredException(ShapeBase):
    """
    A destination ARN for the target service for the trigger is required but was not
    specified.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


class RepositoryTriggerEventEnum(str):
    all = "all"
    updateReference = "updateReference"
    createReference = "createReference"
    deleteReference = "deleteReference"


@dataclasses.dataclass
class RepositoryTriggerEventsListRequiredException(ShapeBase):
    """
    At least one event for the trigger is required but was not specified.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class RepositoryTriggerExecutionFailure(ShapeBase):
    """
    A trigger failed to run.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "trigger",
                "trigger",
                TypeInfo(str),
            ),
            (
                "failure_message",
                "failureMessage",
                TypeInfo(str),
            ),
        ]

    # The name of the trigger that did not run.
    trigger: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Additional message information about the trigger that did not run.
    failure_message: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class RepositoryTriggerNameRequiredException(ShapeBase):
    """
    A name for the trigger is required but was not specified.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class RepositoryTriggersListRequiredException(ShapeBase):
    """
    The list of triggers for the repository is required but was not specified.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class SameFileContentException(ShapeBase):
    """
    The file was not added or updated because the content of the file is exactly the
    same as the content of that file in the repository and branch that you
    specified.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


class SortByEnum(str):
    repositoryName = "repositoryName"
    lastModifiedDate = "lastModifiedDate"


@dataclasses.dataclass
class SourceAndDestinationAreSameException(ShapeBase):
    """
    The source branch and the destination branch for the pull request are the same.
    You must specify different branches for the source and destination.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class Target(ShapeBase):
    """
    Returns information about a target for a pull request.
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
                "source_reference",
                "sourceReference",
                TypeInfo(str),
            ),
            (
                "destination_reference",
                "destinationReference",
                TypeInfo(str),
            ),
        ]

    # The name of the repository that contains the pull request.
    repository_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The branch of the repository that contains the changes for the pull
    # request. Also known as the source branch.
    source_reference: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The branch of the repository where the pull request changes will be merged
    # into. Also known as the destination branch.
    destination_reference: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class TargetRequiredException(ShapeBase):
    """
    A pull request target is required. It cannot be empty or null. A pull request
    target must contain the full values for the repository name, source branch, and
    destination branch for the pull request.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class TargetsRequiredException(ShapeBase):
    """
    An array of target objects is required. It cannot be empty or null.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class TestRepositoryTriggersInput(ShapeBase):
    """
    Represents the input of a test repository triggers operation.
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
                "triggers",
                "triggers",
                TypeInfo(typing.List[RepositoryTrigger]),
            ),
        ]

    # The name of the repository in which to test the triggers.
    repository_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The list of triggers to test.
    triggers: typing.List["RepositoryTrigger"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class TestRepositoryTriggersOutput(OutputShapeBase):
    """
    Represents the output of a test repository triggers operation.
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
                "successful_executions",
                "successfulExecutions",
                TypeInfo(typing.List[str]),
            ),
            (
                "failed_executions",
                "failedExecutions",
                TypeInfo(typing.List[RepositoryTriggerExecutionFailure]),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The list of triggers that were successfully tested. This list provides the
    # names of the triggers that were successfully tested, separated by commas.
    successful_executions: typing.List[str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The list of triggers that were not able to be tested. This list provides
    # the names of the triggers that could not be tested, separated by commas.
    failed_executions: typing.List["RepositoryTriggerExecutionFailure"
                                  ] = dataclasses.field(
                                      default=ShapeBase.NOT_SET,
                                  )


@dataclasses.dataclass
class TipOfSourceReferenceIsDifferentException(ShapeBase):
    """
    The tip of the source branch in the destination repository does not match the
    tip of the source branch specified in your request. The pull request might have
    been updated. Make sure that you have the latest changes.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class TipsDivergenceExceededException(ShapeBase):
    """
    The divergence between the tips of the provided commit specifiers is too great
    to determine whether there might be any merge conflicts. Locally compare the
    specifiers using `git diff` or a diff tool.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class TitleRequiredException(ShapeBase):
    """
    A pull request title is required. It cannot be empty or null.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class UpdateCommentInput(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "comment_id",
                "commentId",
                TypeInfo(str),
            ),
            (
                "content",
                "content",
                TypeInfo(str),
            ),
        ]

    # The system-generated ID of the comment you want to update. To get this ID,
    # use GetCommentsForComparedCommit or GetCommentsForPullRequest.
    comment_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The updated content with which you want to replace the existing content of
    # the comment.
    content: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class UpdateCommentOutput(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "comment",
                "comment",
                TypeInfo(Comment),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Information about the updated comment.
    comment: "Comment" = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class UpdateDefaultBranchInput(ShapeBase):
    """
    Represents the input of an update default branch operation.
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
                "default_branch_name",
                "defaultBranchName",
                TypeInfo(str),
            ),
        ]

    # The name of the repository to set or change the default branch for.
    repository_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The name of the branch to set as the default.
    default_branch_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class UpdatePullRequestDescriptionInput(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "pull_request_id",
                "pullRequestId",
                TypeInfo(str),
            ),
            (
                "description",
                "description",
                TypeInfo(str),
            ),
        ]

    # The system-generated ID of the pull request. To get this ID, use
    # ListPullRequests.
    pull_request_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The updated content of the description for the pull request. This content
    # will replace the existing description.
    description: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class UpdatePullRequestDescriptionOutput(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "pull_request",
                "pullRequest",
                TypeInfo(PullRequest),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Information about the updated pull request.
    pull_request: "PullRequest" = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class UpdatePullRequestStatusInput(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "pull_request_id",
                "pullRequestId",
                TypeInfo(str),
            ),
            (
                "pull_request_status",
                "pullRequestStatus",
                TypeInfo(typing.Union[str, PullRequestStatusEnum]),
            ),
        ]

    # The system-generated ID of the pull request. To get this ID, use
    # ListPullRequests.
    pull_request_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The status of the pull request. The only valid operations are to update the
    # status from `OPEN` to `OPEN`, `OPEN` to `CLOSED` or from from `CLOSED` to
    # `CLOSED`.
    pull_request_status: typing.Union[str, "PullRequestStatusEnum"
                                     ] = dataclasses.field(
                                         default=ShapeBase.NOT_SET,
                                     )


@dataclasses.dataclass
class UpdatePullRequestStatusOutput(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "pull_request",
                "pullRequest",
                TypeInfo(PullRequest),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Information about the pull request.
    pull_request: "PullRequest" = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class UpdatePullRequestTitleInput(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "pull_request_id",
                "pullRequestId",
                TypeInfo(str),
            ),
            (
                "title",
                "title",
                TypeInfo(str),
            ),
        ]

    # The system-generated ID of the pull request. To get this ID, use
    # ListPullRequests.
    pull_request_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The updated title of the pull request. This will replace the existing
    # title.
    title: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class UpdatePullRequestTitleOutput(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "pull_request",
                "pullRequest",
                TypeInfo(PullRequest),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Information about the updated pull request.
    pull_request: "PullRequest" = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class UpdateRepositoryDescriptionInput(ShapeBase):
    """
    Represents the input of an update repository description operation.
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
                "repository_description",
                "repositoryDescription",
                TypeInfo(str),
            ),
        ]

    # The name of the repository to set or change the comment or description for.
    repository_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The new comment or description for the specified repository. Repository
    # descriptions are limited to 1,000 characters.
    repository_description: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class UpdateRepositoryNameInput(ShapeBase):
    """
    Represents the input of an update repository description operation.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "old_name",
                "oldName",
                TypeInfo(str),
            ),
            (
                "new_name",
                "newName",
                TypeInfo(str),
            ),
        ]

    # The existing name of the repository.
    old_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The new name for the repository.
    new_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class UserInfo(ShapeBase):
    """
    Information about the user who made a specified commit.
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
                "email",
                "email",
                TypeInfo(str),
            ),
            (
                "date",
                "date",
                TypeInfo(str),
            ),
        ]

    # The name of the user who made the specified commit.
    name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The email address associated with the user who made the commit, if any.
    email: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The date when the specified commit was commited, in timestamp format with
    # GMT offset.
    date: str = dataclasses.field(default=ShapeBase.NOT_SET, )


class blob(botocore.response.StreamingBody):
    pass
