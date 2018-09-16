import datetime
import typing
from autoboto import ShapeBase, OutputShapeBase, TypeInfo
import dataclasses


@dataclasses.dataclass
class AbortDocumentVersionUploadRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "document_id",
                "DocumentId",
                TypeInfo(str),
            ),
            (
                "version_id",
                "VersionId",
                TypeInfo(str),
            ),
            (
                "authentication_token",
                "AuthenticationToken",
                TypeInfo(str),
            ),
        ]

    # The ID of the document.
    document_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The ID of the version.
    version_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Amazon WorkDocs authentication token. Do not set this field when using
    # administrative API actions, as in accessing the API using AWS credentials.
    authentication_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ActivateUserRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "user_id",
                "UserId",
                TypeInfo(str),
            ),
            (
                "authentication_token",
                "AuthenticationToken",
                TypeInfo(str),
            ),
        ]

    # The ID of the user.
    user_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Amazon WorkDocs authentication token. Do not set this field when using
    # administrative API actions, as in accessing the API using AWS credentials.
    authentication_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ActivateUserResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "user",
                "User",
                TypeInfo(User),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The user information.
    user: "User" = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class Activity(ShapeBase):
    """
    Describes the activity information.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "type",
                "Type",
                TypeInfo(typing.Union[str, ActivityType]),
            ),
            (
                "time_stamp",
                "TimeStamp",
                TypeInfo(datetime.datetime),
            ),
            (
                "organization_id",
                "OrganizationId",
                TypeInfo(str),
            ),
            (
                "initiator",
                "Initiator",
                TypeInfo(UserMetadata),
            ),
            (
                "participants",
                "Participants",
                TypeInfo(Participants),
            ),
            (
                "resource_metadata",
                "ResourceMetadata",
                TypeInfo(ResourceMetadata),
            ),
            (
                "original_parent",
                "OriginalParent",
                TypeInfo(ResourceMetadata),
            ),
            (
                "comment_metadata",
                "CommentMetadata",
                TypeInfo(CommentMetadata),
            ),
        ]

    # The activity type.
    type: typing.Union[str, "ActivityType"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The timestamp when the action was performed.
    time_stamp: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The ID of the organization.
    organization_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The user who performed the action.
    initiator: "UserMetadata" = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The list of users or groups impacted by this action. This is an optional
    # field and is filled for the following sharing activities: DOCUMENT_SHARED,
    # DOCUMENT_SHARED, DOCUMENT_UNSHARED, FOLDER_SHARED, FOLDER_UNSHARED.
    participants: "Participants" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The metadata of the resource involved in the user action.
    resource_metadata: "ResourceMetadata" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The original parent of the resource. This is an optional field and is
    # filled for move activities.
    original_parent: "ResourceMetadata" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Metadata of the commenting activity. This is an optional field and is
    # filled for commenting activities.
    comment_metadata: "CommentMetadata" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


class ActivityType(str):
    DOCUMENT_CHECKED_IN = "DOCUMENT_CHECKED_IN"
    DOCUMENT_CHECKED_OUT = "DOCUMENT_CHECKED_OUT"
    DOCUMENT_RENAMED = "DOCUMENT_RENAMED"
    DOCUMENT_VERSION_UPLOADED = "DOCUMENT_VERSION_UPLOADED"
    DOCUMENT_VERSION_DELETED = "DOCUMENT_VERSION_DELETED"
    DOCUMENT_RECYCLED = "DOCUMENT_RECYCLED"
    DOCUMENT_RESTORED = "DOCUMENT_RESTORED"
    DOCUMENT_REVERTED = "DOCUMENT_REVERTED"
    DOCUMENT_SHARED = "DOCUMENT_SHARED"
    DOCUMENT_UNSHARED = "DOCUMENT_UNSHARED"
    DOCUMENT_SHARE_PERMISSION_CHANGED = "DOCUMENT_SHARE_PERMISSION_CHANGED"
    DOCUMENT_SHAREABLE_LINK_CREATED = "DOCUMENT_SHAREABLE_LINK_CREATED"
    DOCUMENT_SHAREABLE_LINK_REMOVED = "DOCUMENT_SHAREABLE_LINK_REMOVED"
    DOCUMENT_SHAREABLE_LINK_PERMISSION_CHANGED = "DOCUMENT_SHAREABLE_LINK_PERMISSION_CHANGED"
    DOCUMENT_MOVED = "DOCUMENT_MOVED"
    DOCUMENT_COMMENT_ADDED = "DOCUMENT_COMMENT_ADDED"
    DOCUMENT_COMMENT_DELETED = "DOCUMENT_COMMENT_DELETED"
    DOCUMENT_ANNOTATION_ADDED = "DOCUMENT_ANNOTATION_ADDED"
    DOCUMENT_ANNOTATION_DELETED = "DOCUMENT_ANNOTATION_DELETED"
    FOLDER_CREATED = "FOLDER_CREATED"
    FOLDER_DELETED = "FOLDER_DELETED"
    FOLDER_RENAMED = "FOLDER_RENAMED"
    FOLDER_RECYCLED = "FOLDER_RECYCLED"
    FOLDER_RESTORED = "FOLDER_RESTORED"
    FOLDER_SHARED = "FOLDER_SHARED"
    FOLDER_UNSHARED = "FOLDER_UNSHARED"
    FOLDER_SHARE_PERMISSION_CHANGED = "FOLDER_SHARE_PERMISSION_CHANGED"
    FOLDER_SHAREABLE_LINK_CREATED = "FOLDER_SHAREABLE_LINK_CREATED"
    FOLDER_SHAREABLE_LINK_REMOVED = "FOLDER_SHAREABLE_LINK_REMOVED"
    FOLDER_SHAREABLE_LINK_PERMISSION_CHANGED = "FOLDER_SHAREABLE_LINK_PERMISSION_CHANGED"
    FOLDER_MOVED = "FOLDER_MOVED"


@dataclasses.dataclass
class AddResourcePermissionsRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "resource_id",
                "ResourceId",
                TypeInfo(str),
            ),
            (
                "principals",
                "Principals",
                TypeInfo(typing.List[SharePrincipal]),
            ),
            (
                "authentication_token",
                "AuthenticationToken",
                TypeInfo(str),
            ),
            (
                "notification_options",
                "NotificationOptions",
                TypeInfo(NotificationOptions),
            ),
        ]

    # The ID of the resource.
    resource_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The users, groups, or organization being granted permission.
    principals: typing.List["SharePrincipal"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Amazon WorkDocs authentication token. Do not set this field when using
    # administrative API actions, as in accessing the API using AWS credentials.
    authentication_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The notification options.
    notification_options: "NotificationOptions" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class AddResourcePermissionsResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "share_results",
                "ShareResults",
                TypeInfo(typing.List[ShareResult]),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The share results.
    share_results: typing.List["ShareResult"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


class BooleanEnumType(str):
    TRUE = "TRUE"
    FALSE = "FALSE"


@dataclasses.dataclass
class Comment(ShapeBase):
    """
    Describes a comment.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "comment_id",
                "CommentId",
                TypeInfo(str),
            ),
            (
                "parent_id",
                "ParentId",
                TypeInfo(str),
            ),
            (
                "thread_id",
                "ThreadId",
                TypeInfo(str),
            ),
            (
                "text",
                "Text",
                TypeInfo(str),
            ),
            (
                "contributor",
                "Contributor",
                TypeInfo(User),
            ),
            (
                "created_timestamp",
                "CreatedTimestamp",
                TypeInfo(datetime.datetime),
            ),
            (
                "status",
                "Status",
                TypeInfo(typing.Union[str, CommentStatusType]),
            ),
            (
                "visibility",
                "Visibility",
                TypeInfo(typing.Union[str, CommentVisibilityType]),
            ),
            (
                "recipient_id",
                "RecipientId",
                TypeInfo(str),
            ),
        ]

    # The ID of the comment.
    comment_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The ID of the parent comment.
    parent_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The ID of the root comment in the thread.
    thread_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The text of the comment.
    text: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The details of the user who made the comment.
    contributor: "User" = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The time that the comment was created.
    created_timestamp: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The status of the comment.
    status: typing.Union[str, "CommentStatusType"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The visibility of the comment. Options are either PRIVATE, where the
    # comment is visible only to the comment author and document owner and co-
    # owners, or PUBLIC, where the comment is visible to document owners, co-
    # owners, and contributors.
    visibility: typing.Union[str, "CommentVisibilityType"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # If the comment is a reply to another user's comment, this field contains
    # the user ID of the user being replied to.
    recipient_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class CommentMetadata(ShapeBase):
    """
    Describes the metadata of a comment.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "comment_id",
                "CommentId",
                TypeInfo(str),
            ),
            (
                "contributor",
                "Contributor",
                TypeInfo(User),
            ),
            (
                "created_timestamp",
                "CreatedTimestamp",
                TypeInfo(datetime.datetime),
            ),
            (
                "comment_status",
                "CommentStatus",
                TypeInfo(typing.Union[str, CommentStatusType]),
            ),
            (
                "recipient_id",
                "RecipientId",
                TypeInfo(str),
            ),
        ]

    # The ID of the comment.
    comment_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The user who made the comment.
    contributor: "User" = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The timestamp that the comment was created.
    created_timestamp: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The status of the comment.
    comment_status: typing.Union[str, "CommentStatusType"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The ID of the user being replied to.
    recipient_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )


class CommentStatusType(str):
    DRAFT = "DRAFT"
    PUBLISHED = "PUBLISHED"
    DELETED = "DELETED"


class CommentVisibilityType(str):
    PUBLIC = "PUBLIC"
    PRIVATE = "PRIVATE"


@dataclasses.dataclass
class ConcurrentModificationException(ShapeBase):
    """
    The resource hierarchy is changing.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "message",
                "Message",
                TypeInfo(str),
            ),
        ]

    message: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class CreateCommentRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "document_id",
                "DocumentId",
                TypeInfo(str),
            ),
            (
                "version_id",
                "VersionId",
                TypeInfo(str),
            ),
            (
                "text",
                "Text",
                TypeInfo(str),
            ),
            (
                "authentication_token",
                "AuthenticationToken",
                TypeInfo(str),
            ),
            (
                "parent_id",
                "ParentId",
                TypeInfo(str),
            ),
            (
                "thread_id",
                "ThreadId",
                TypeInfo(str),
            ),
            (
                "visibility",
                "Visibility",
                TypeInfo(typing.Union[str, CommentVisibilityType]),
            ),
            (
                "notify_collaborators",
                "NotifyCollaborators",
                TypeInfo(bool),
            ),
        ]

    # The ID of the document.
    document_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The ID of the document version.
    version_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The text of the comment.
    text: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Amazon WorkDocs authentication token. Do not set this field when using
    # administrative API actions, as in accessing the API using AWS credentials.
    authentication_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The ID of the parent comment.
    parent_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The ID of the root comment in the thread.
    thread_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The visibility of the comment. Options are either PRIVATE, where the
    # comment is visible only to the comment author and document owner and co-
    # owners, or PUBLIC, where the comment is visible to document owners, co-
    # owners, and contributors.
    visibility: typing.Union[str, "CommentVisibilityType"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Set this parameter to TRUE to send an email out to the document
    # collaborators after the comment is created.
    notify_collaborators: bool = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class CreateCommentResponse(OutputShapeBase):
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
                "Comment",
                TypeInfo(Comment),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The comment that has been created.
    comment: "Comment" = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class CreateCustomMetadataRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "resource_id",
                "ResourceId",
                TypeInfo(str),
            ),
            (
                "custom_metadata",
                "CustomMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "authentication_token",
                "AuthenticationToken",
                TypeInfo(str),
            ),
            (
                "version_id",
                "VersionId",
                TypeInfo(str),
            ),
        ]

    # The ID of the resource.
    resource_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Custom metadata in the form of name-value pairs.
    custom_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Amazon WorkDocs authentication token. Do not set this field when using
    # administrative API actions, as in accessing the API using AWS credentials.
    authentication_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The ID of the version, if the custom metadata is being added to a document
    # version.
    version_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class CreateCustomMetadataResponse(OutputShapeBase):
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
class CreateFolderRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "parent_folder_id",
                "ParentFolderId",
                TypeInfo(str),
            ),
            (
                "authentication_token",
                "AuthenticationToken",
                TypeInfo(str),
            ),
            (
                "name",
                "Name",
                TypeInfo(str),
            ),
        ]

    # The ID of the parent folder.
    parent_folder_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Amazon WorkDocs authentication token. Do not set this field when using
    # administrative API actions, as in accessing the API using AWS credentials.
    authentication_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The name of the new folder.
    name: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class CreateFolderResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "metadata",
                "Metadata",
                TypeInfo(FolderMetadata),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The metadata of the folder.
    metadata: "FolderMetadata" = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class CreateLabelsRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "resource_id",
                "ResourceId",
                TypeInfo(str),
            ),
            (
                "labels",
                "Labels",
                TypeInfo(typing.List[str]),
            ),
            (
                "authentication_token",
                "AuthenticationToken",
                TypeInfo(str),
            ),
        ]

    # The ID of the resource.
    resource_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # List of labels to add to the resource.
    labels: typing.List[str] = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Amazon WorkDocs authentication token. Do not set this field when using
    # administrative API actions, as in accessing the API using AWS credentials.
    authentication_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class CreateLabelsResponse(OutputShapeBase):
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
class CreateNotificationSubscriptionRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "organization_id",
                "OrganizationId",
                TypeInfo(str),
            ),
            (
                "endpoint",
                "Endpoint",
                TypeInfo(str),
            ),
            (
                "protocol",
                "Protocol",
                TypeInfo(typing.Union[str, SubscriptionProtocolType]),
            ),
            (
                "subscription_type",
                "SubscriptionType",
                TypeInfo(typing.Union[str, SubscriptionType]),
            ),
        ]

    # The ID of the organization.
    organization_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The endpoint to receive the notifications. If the protocol is HTTPS, the
    # endpoint is a URL that begins with "https://".
    endpoint: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The protocol to use. The supported value is https, which delivers JSON-
    # encoded messages using HTTPS POST.
    protocol: typing.Union[str, "SubscriptionProtocolType"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The notification type.
    subscription_type: typing.Union[str, "SubscriptionType"
                                   ] = dataclasses.field(
                                       default=ShapeBase.NOT_SET,
                                   )


@dataclasses.dataclass
class CreateNotificationSubscriptionResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "subscription",
                "Subscription",
                TypeInfo(Subscription),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The subscription.
    subscription: "Subscription" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class CreateUserRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "username",
                "Username",
                TypeInfo(str),
            ),
            (
                "given_name",
                "GivenName",
                TypeInfo(str),
            ),
            (
                "surname",
                "Surname",
                TypeInfo(str),
            ),
            (
                "password",
                "Password",
                TypeInfo(str),
            ),
            (
                "organization_id",
                "OrganizationId",
                TypeInfo(str),
            ),
            (
                "email_address",
                "EmailAddress",
                TypeInfo(str),
            ),
            (
                "time_zone_id",
                "TimeZoneId",
                TypeInfo(str),
            ),
            (
                "storage_rule",
                "StorageRule",
                TypeInfo(StorageRuleType),
            ),
            (
                "authentication_token",
                "AuthenticationToken",
                TypeInfo(str),
            ),
        ]

    # The login name of the user.
    username: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The given name of the user.
    given_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The surname of the user.
    surname: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The password of the user.
    password: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The ID of the organization.
    organization_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The email address of the user.
    email_address: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The time zone ID of the user.
    time_zone_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The amount of storage for the user.
    storage_rule: "StorageRuleType" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Amazon WorkDocs authentication token. Do not set this field when using
    # administrative API actions, as in accessing the API using AWS credentials.
    authentication_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class CreateUserResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "user",
                "User",
                TypeInfo(User),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The user information.
    user: "User" = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class CustomMetadataLimitExceededException(ShapeBase):
    """
    The limit has been reached on the number of custom properties for the specified
    resource.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "message",
                "Message",
                TypeInfo(str),
            ),
        ]

    message: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DeactivateUserRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "user_id",
                "UserId",
                TypeInfo(str),
            ),
            (
                "authentication_token",
                "AuthenticationToken",
                TypeInfo(str),
            ),
        ]

    # The ID of the user.
    user_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Amazon WorkDocs authentication token. Do not set this field when using
    # administrative API actions, as in accessing the API using AWS credentials.
    authentication_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DeactivatingLastSystemUserException(ShapeBase):
    """
    The last user in the organization is being deactivated.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class DeleteCommentRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "document_id",
                "DocumentId",
                TypeInfo(str),
            ),
            (
                "version_id",
                "VersionId",
                TypeInfo(str),
            ),
            (
                "comment_id",
                "CommentId",
                TypeInfo(str),
            ),
            (
                "authentication_token",
                "AuthenticationToken",
                TypeInfo(str),
            ),
        ]

    # The ID of the document.
    document_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The ID of the document version.
    version_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The ID of the comment.
    comment_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Amazon WorkDocs authentication token. Do not set this field when using
    # administrative API actions, as in accessing the API using AWS credentials.
    authentication_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DeleteCustomMetadataRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "resource_id",
                "ResourceId",
                TypeInfo(str),
            ),
            (
                "authentication_token",
                "AuthenticationToken",
                TypeInfo(str),
            ),
            (
                "version_id",
                "VersionId",
                TypeInfo(str),
            ),
            (
                "keys",
                "Keys",
                TypeInfo(typing.List[str]),
            ),
            (
                "delete_all",
                "DeleteAll",
                TypeInfo(bool),
            ),
        ]

    # The ID of the resource, either a document or folder.
    resource_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Amazon WorkDocs authentication token. Do not set this field when using
    # administrative API actions, as in accessing the API using AWS credentials.
    authentication_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The ID of the version, if the custom metadata is being deleted from a
    # document version.
    version_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # List of properties to remove.
    keys: typing.List[str] = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Flag to indicate removal of all custom metadata properties from the
    # specified resource.
    delete_all: bool = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DeleteCustomMetadataResponse(OutputShapeBase):
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
class DeleteDocumentRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "document_id",
                "DocumentId",
                TypeInfo(str),
            ),
            (
                "authentication_token",
                "AuthenticationToken",
                TypeInfo(str),
            ),
        ]

    # The ID of the document.
    document_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Amazon WorkDocs authentication token. Do not set this field when using
    # administrative API actions, as in accessing the API using AWS credentials.
    authentication_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DeleteFolderContentsRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "folder_id",
                "FolderId",
                TypeInfo(str),
            ),
            (
                "authentication_token",
                "AuthenticationToken",
                TypeInfo(str),
            ),
        ]

    # The ID of the folder.
    folder_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Amazon WorkDocs authentication token. Do not set this field when using
    # administrative API actions, as in accessing the API using AWS credentials.
    authentication_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DeleteFolderRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "folder_id",
                "FolderId",
                TypeInfo(str),
            ),
            (
                "authentication_token",
                "AuthenticationToken",
                TypeInfo(str),
            ),
        ]

    # The ID of the folder.
    folder_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Amazon WorkDocs authentication token. Do not set this field when using
    # administrative API actions, as in accessing the API using AWS credentials.
    authentication_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DeleteLabelsRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "resource_id",
                "ResourceId",
                TypeInfo(str),
            ),
            (
                "authentication_token",
                "AuthenticationToken",
                TypeInfo(str),
            ),
            (
                "labels",
                "Labels",
                TypeInfo(typing.List[str]),
            ),
            (
                "delete_all",
                "DeleteAll",
                TypeInfo(bool),
            ),
        ]

    # The ID of the resource.
    resource_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Amazon WorkDocs authentication token. Do not set this field when using
    # administrative API actions, as in accessing the API using AWS credentials.
    authentication_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # List of labels to delete from the resource.
    labels: typing.List[str] = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Flag to request removal of all labels from the specified resource.
    delete_all: bool = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DeleteLabelsResponse(OutputShapeBase):
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
class DeleteNotificationSubscriptionRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "subscription_id",
                "SubscriptionId",
                TypeInfo(str),
            ),
            (
                "organization_id",
                "OrganizationId",
                TypeInfo(str),
            ),
        ]

    # The ID of the subscription.
    subscription_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The ID of the organization.
    organization_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DeleteUserRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "user_id",
                "UserId",
                TypeInfo(str),
            ),
            (
                "authentication_token",
                "AuthenticationToken",
                TypeInfo(str),
            ),
        ]

    # The ID of the user.
    user_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Amazon WorkDocs authentication token. Do not set this field when using
    # administrative API actions, as in accessing the API using AWS credentials.
    authentication_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DescribeActivitiesRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "authentication_token",
                "AuthenticationToken",
                TypeInfo(str),
            ),
            (
                "start_time",
                "StartTime",
                TypeInfo(datetime.datetime),
            ),
            (
                "end_time",
                "EndTime",
                TypeInfo(datetime.datetime),
            ),
            (
                "organization_id",
                "OrganizationId",
                TypeInfo(str),
            ),
            (
                "user_id",
                "UserId",
                TypeInfo(str),
            ),
            (
                "limit",
                "Limit",
                TypeInfo(int),
            ),
            (
                "marker",
                "Marker",
                TypeInfo(str),
            ),
        ]

    # Amazon WorkDocs authentication token. Do not set this field when using
    # administrative API actions, as in accessing the API using AWS credentials.
    authentication_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The timestamp that determines the starting time of the activities. The
    # response includes the activities performed after the specified timestamp.
    start_time: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The timestamp that determines the end time of the activities. The response
    # includes the activities performed before the specified timestamp.
    end_time: datetime.datetime = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The ID of the organization. This is a mandatory parameter when using
    # administrative API (SigV4) requests.
    organization_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The ID of the user who performed the action. The response includes
    # activities pertaining to this user. This is an optional parameter and is
    # only applicable for administrative API (SigV4) requests.
    user_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The maximum number of items to return.
    limit: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The marker for the next set of results.
    marker: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DescribeActivitiesResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "user_activities",
                "UserActivities",
                TypeInfo(typing.List[Activity]),
            ),
            (
                "marker",
                "Marker",
                TypeInfo(str),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The list of activities for the specified user and time period.
    user_activities: typing.List["Activity"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The marker for the next set of results.
    marker: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DescribeCommentsRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "document_id",
                "DocumentId",
                TypeInfo(str),
            ),
            (
                "version_id",
                "VersionId",
                TypeInfo(str),
            ),
            (
                "authentication_token",
                "AuthenticationToken",
                TypeInfo(str),
            ),
            (
                "limit",
                "Limit",
                TypeInfo(int),
            ),
            (
                "marker",
                "Marker",
                TypeInfo(str),
            ),
        ]

    # The ID of the document.
    document_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The ID of the document version.
    version_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Amazon WorkDocs authentication token. Do not set this field when using
    # administrative API actions, as in accessing the API using AWS credentials.
    authentication_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The maximum number of items to return.
    limit: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The marker for the next set of results. This marker was received from a
    # previous call.
    marker: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DescribeCommentsResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "comments",
                "Comments",
                TypeInfo(typing.List[Comment]),
            ),
            (
                "marker",
                "Marker",
                TypeInfo(str),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The list of comments for the specified document version.
    comments: typing.List["Comment"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The marker for the next set of results. This marker was received from a
    # previous call.
    marker: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DescribeDocumentVersionsRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "document_id",
                "DocumentId",
                TypeInfo(str),
            ),
            (
                "authentication_token",
                "AuthenticationToken",
                TypeInfo(str),
            ),
            (
                "marker",
                "Marker",
                TypeInfo(str),
            ),
            (
                "limit",
                "Limit",
                TypeInfo(int),
            ),
            (
                "include",
                "Include",
                TypeInfo(str),
            ),
            (
                "fields",
                "Fields",
                TypeInfo(str),
            ),
        ]

    # The ID of the document.
    document_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Amazon WorkDocs authentication token. Do not set this field when using
    # administrative API actions, as in accessing the API using AWS credentials.
    authentication_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The marker for the next set of results. (You received this marker from a
    # previous call.)
    marker: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The maximum number of versions to return with this call.
    limit: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A comma-separated list of values. Specify "INITIALIZED" to include
    # incomplete versions.
    include: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Specify "SOURCE" to include initialized versions and a URL for the source
    # document.
    fields: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DescribeDocumentVersionsResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "document_versions",
                "DocumentVersions",
                TypeInfo(typing.List[DocumentVersionMetadata]),
            ),
            (
                "marker",
                "Marker",
                TypeInfo(str),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The document versions.
    document_versions: typing.List["DocumentVersionMetadata"
                                  ] = dataclasses.field(
                                      default=ShapeBase.NOT_SET,
                                  )

    # The marker to use when requesting the next set of results. If there are no
    # additional results, the string is empty.
    marker: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    def paginate(
        self,
    ) -> typing.Generator["DescribeDocumentVersionsResponse", None, None]:
        yield from super()._paginate()


@dataclasses.dataclass
class DescribeFolderContentsRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "folder_id",
                "FolderId",
                TypeInfo(str),
            ),
            (
                "authentication_token",
                "AuthenticationToken",
                TypeInfo(str),
            ),
            (
                "sort",
                "Sort",
                TypeInfo(typing.Union[str, ResourceSortType]),
            ),
            (
                "order",
                "Order",
                TypeInfo(typing.Union[str, OrderType]),
            ),
            (
                "limit",
                "Limit",
                TypeInfo(int),
            ),
            (
                "marker",
                "Marker",
                TypeInfo(str),
            ),
            (
                "type",
                "Type",
                TypeInfo(typing.Union[str, FolderContentType]),
            ),
            (
                "include",
                "Include",
                TypeInfo(str),
            ),
        ]

    # The ID of the folder.
    folder_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Amazon WorkDocs authentication token. Do not set this field when using
    # administrative API actions, as in accessing the API using AWS credentials.
    authentication_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The sorting criteria.
    sort: typing.Union[str, "ResourceSortType"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The order for the contents of the folder.
    order: typing.Union[str, "OrderType"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The maximum number of items to return with this call.
    limit: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The marker for the next set of results. This marker was received from a
    # previous call.
    marker: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The type of items.
    type: typing.Union[str, "FolderContentType"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The contents to include. Specify "INITIALIZED" to include initialized
    # documents.
    include: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DescribeFolderContentsResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "folders",
                "Folders",
                TypeInfo(typing.List[FolderMetadata]),
            ),
            (
                "documents",
                "Documents",
                TypeInfo(typing.List[DocumentMetadata]),
            ),
            (
                "marker",
                "Marker",
                TypeInfo(str),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The subfolders in the specified folder.
    folders: typing.List["FolderMetadata"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The documents in the specified folder.
    documents: typing.List["DocumentMetadata"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The marker to use when requesting the next set of results. If there are no
    # additional results, the string is empty.
    marker: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    def paginate(
        self,
    ) -> typing.Generator["DescribeFolderContentsResponse", None, None]:
        yield from super()._paginate()


@dataclasses.dataclass
class DescribeGroupsRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "search_query",
                "SearchQuery",
                TypeInfo(str),
            ),
            (
                "authentication_token",
                "AuthenticationToken",
                TypeInfo(str),
            ),
            (
                "organization_id",
                "OrganizationId",
                TypeInfo(str),
            ),
            (
                "marker",
                "Marker",
                TypeInfo(str),
            ),
            (
                "limit",
                "Limit",
                TypeInfo(int),
            ),
        ]

    # A query to describe groups by group name.
    search_query: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Amazon WorkDocs authentication token. Do not set this field when using
    # administrative API actions, as in accessing the API using AWS credentials.
    authentication_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The ID of the organization.
    organization_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The marker for the next set of results. (You received this marker from a
    # previous call.)
    marker: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The maximum number of items to return with this call.
    limit: int = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DescribeGroupsResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "groups",
                "Groups",
                TypeInfo(typing.List[GroupMetadata]),
            ),
            (
                "marker",
                "Marker",
                TypeInfo(str),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The list of groups.
    groups: typing.List["GroupMetadata"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The marker to use when requesting the next set of results. If there are no
    # additional results, the string is empty.
    marker: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DescribeNotificationSubscriptionsRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "organization_id",
                "OrganizationId",
                TypeInfo(str),
            ),
            (
                "marker",
                "Marker",
                TypeInfo(str),
            ),
            (
                "limit",
                "Limit",
                TypeInfo(int),
            ),
        ]

    # The ID of the organization.
    organization_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The marker for the next set of results. (You received this marker from a
    # previous call.)
    marker: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The maximum number of items to return with this call.
    limit: int = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DescribeNotificationSubscriptionsResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "subscriptions",
                "Subscriptions",
                TypeInfo(typing.List[Subscription]),
            ),
            (
                "marker",
                "Marker",
                TypeInfo(str),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The subscriptions.
    subscriptions: typing.List["Subscription"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The marker to use when requesting the next set of results. If there are no
    # additional results, the string is empty.
    marker: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DescribeResourcePermissionsRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "resource_id",
                "ResourceId",
                TypeInfo(str),
            ),
            (
                "authentication_token",
                "AuthenticationToken",
                TypeInfo(str),
            ),
            (
                "principal_id",
                "PrincipalId",
                TypeInfo(str),
            ),
            (
                "limit",
                "Limit",
                TypeInfo(int),
            ),
            (
                "marker",
                "Marker",
                TypeInfo(str),
            ),
        ]

    # The ID of the resource.
    resource_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Amazon WorkDocs authentication token. Do not set this field when using
    # administrative API actions, as in accessing the API using AWS credentials.
    authentication_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The ID of the principal to filter permissions by.
    principal_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The maximum number of items to return with this call.
    limit: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The marker for the next set of results. (You received this marker from a
    # previous call)
    marker: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DescribeResourcePermissionsResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "principals",
                "Principals",
                TypeInfo(typing.List[Principal]),
            ),
            (
                "marker",
                "Marker",
                TypeInfo(str),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The principals.
    principals: typing.List["Principal"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The marker to use when requesting the next set of results. If there are no
    # additional results, the string is empty.
    marker: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DescribeRootFoldersRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "authentication_token",
                "AuthenticationToken",
                TypeInfo(str),
            ),
            (
                "limit",
                "Limit",
                TypeInfo(int),
            ),
            (
                "marker",
                "Marker",
                TypeInfo(str),
            ),
        ]

    # Amazon WorkDocs authentication token. Do not set this field when using
    # administrative API actions, as in accessing the API using AWS credentials.
    authentication_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The maximum number of items to return.
    limit: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The marker for the next set of results. (You received this marker from a
    # previous call.)
    marker: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DescribeRootFoldersResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "folders",
                "Folders",
                TypeInfo(typing.List[FolderMetadata]),
            ),
            (
                "marker",
                "Marker",
                TypeInfo(str),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The user's special folders.
    folders: typing.List["FolderMetadata"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The marker for the next set of results.
    marker: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DescribeUsersRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "authentication_token",
                "AuthenticationToken",
                TypeInfo(str),
            ),
            (
                "organization_id",
                "OrganizationId",
                TypeInfo(str),
            ),
            (
                "user_ids",
                "UserIds",
                TypeInfo(str),
            ),
            (
                "query",
                "Query",
                TypeInfo(str),
            ),
            (
                "include",
                "Include",
                TypeInfo(typing.Union[str, UserFilterType]),
            ),
            (
                "order",
                "Order",
                TypeInfo(typing.Union[str, OrderType]),
            ),
            (
                "sort",
                "Sort",
                TypeInfo(typing.Union[str, UserSortType]),
            ),
            (
                "marker",
                "Marker",
                TypeInfo(str),
            ),
            (
                "limit",
                "Limit",
                TypeInfo(int),
            ),
            (
                "fields",
                "Fields",
                TypeInfo(str),
            ),
        ]

    # Amazon WorkDocs authentication token. Do not set this field when using
    # administrative API actions, as in accessing the API using AWS credentials.
    authentication_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The ID of the organization.
    organization_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The IDs of the users.
    user_ids: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A query to filter users by user name.
    query: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The state of the users. Specify "ALL" to include inactive users.
    include: typing.Union[str, "UserFilterType"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The order for the results.
    order: typing.Union[str, "OrderType"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The sorting criteria.
    sort: typing.Union[str, "UserSortType"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The marker for the next set of results. (You received this marker from a
    # previous call.)
    marker: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The maximum number of items to return.
    limit: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A comma-separated list of values. Specify "STORAGE_METADATA" to include the
    # user storage quota and utilization information.
    fields: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DescribeUsersResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "users",
                "Users",
                TypeInfo(typing.List[User]),
            ),
            (
                "total_number_of_users",
                "TotalNumberOfUsers",
                TypeInfo(int),
            ),
            (
                "marker",
                "Marker",
                TypeInfo(str),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The users.
    users: typing.List["User"] = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The total number of users included in the results.
    total_number_of_users: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The marker to use when requesting the next set of results. If there are no
    # additional results, the string is empty.
    marker: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    def paginate(self,
                ) -> typing.Generator["DescribeUsersResponse", None, None]:
        yield from super()._paginate()


@dataclasses.dataclass
class DocumentLockedForCommentsException(ShapeBase):
    """
    This exception is thrown when the document is locked for comments and user tries
    to create or delete a comment on that document.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "message",
                "Message",
                TypeInfo(str),
            ),
        ]

    message: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DocumentMetadata(ShapeBase):
    """
    Describes the document.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "id",
                "Id",
                TypeInfo(str),
            ),
            (
                "creator_id",
                "CreatorId",
                TypeInfo(str),
            ),
            (
                "parent_folder_id",
                "ParentFolderId",
                TypeInfo(str),
            ),
            (
                "created_timestamp",
                "CreatedTimestamp",
                TypeInfo(datetime.datetime),
            ),
            (
                "modified_timestamp",
                "ModifiedTimestamp",
                TypeInfo(datetime.datetime),
            ),
            (
                "latest_version_metadata",
                "LatestVersionMetadata",
                TypeInfo(DocumentVersionMetadata),
            ),
            (
                "resource_state",
                "ResourceState",
                TypeInfo(typing.Union[str, ResourceStateType]),
            ),
            (
                "labels",
                "Labels",
                TypeInfo(typing.List[str]),
            ),
        ]

    # The ID of the document.
    id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The ID of the creator.
    creator_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The ID of the parent folder.
    parent_folder_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The time when the document was created.
    created_timestamp: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The time when the document was updated.
    modified_timestamp: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The latest version of the document.
    latest_version_metadata: "DocumentVersionMetadata" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The resource state.
    resource_state: typing.Union[str, "ResourceStateType"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # List of labels on the document.
    labels: typing.List[str] = dataclasses.field(default=ShapeBase.NOT_SET, )


class DocumentSourceType(str):
    ORIGINAL = "ORIGINAL"
    WITH_COMMENTS = "WITH_COMMENTS"


class DocumentStatusType(str):
    INITIALIZED = "INITIALIZED"
    ACTIVE = "ACTIVE"


class DocumentThumbnailType(str):
    SMALL = "SMALL"
    SMALL_HQ = "SMALL_HQ"
    LARGE = "LARGE"


@dataclasses.dataclass
class DocumentVersionMetadata(ShapeBase):
    """
    Describes a version of a document.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "id",
                "Id",
                TypeInfo(str),
            ),
            (
                "name",
                "Name",
                TypeInfo(str),
            ),
            (
                "content_type",
                "ContentType",
                TypeInfo(str),
            ),
            (
                "size",
                "Size",
                TypeInfo(int),
            ),
            (
                "signature",
                "Signature",
                TypeInfo(str),
            ),
            (
                "status",
                "Status",
                TypeInfo(typing.Union[str, DocumentStatusType]),
            ),
            (
                "created_timestamp",
                "CreatedTimestamp",
                TypeInfo(datetime.datetime),
            ),
            (
                "modified_timestamp",
                "ModifiedTimestamp",
                TypeInfo(datetime.datetime),
            ),
            (
                "content_created_timestamp",
                "ContentCreatedTimestamp",
                TypeInfo(datetime.datetime),
            ),
            (
                "content_modified_timestamp",
                "ContentModifiedTimestamp",
                TypeInfo(datetime.datetime),
            ),
            (
                "creator_id",
                "CreatorId",
                TypeInfo(str),
            ),
            (
                "thumbnail",
                "Thumbnail",
                TypeInfo(
                    typing.Dict[typing.Union[str, DocumentThumbnailType], str]
                ),
            ),
            (
                "source",
                "Source",
                TypeInfo(
                    typing.Dict[typing.Union[str, DocumentSourceType], str]
                ),
            ),
        ]

    # The ID of the version.
    id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The name of the version.
    name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The content type of the document.
    content_type: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The size of the document, in bytes.
    size: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The signature of the document.
    signature: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The status of the document.
    status: typing.Union[str, "DocumentStatusType"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The timestamp when the document was first uploaded.
    created_timestamp: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The timestamp when the document was last uploaded.
    modified_timestamp: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The timestamp when the content of the document was originally created.
    content_created_timestamp: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The timestamp when the content of the document was modified.
    content_modified_timestamp: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The ID of the creator.
    creator_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The thumbnail of the document.
    thumbnail: typing.Dict[typing.Union[str, "DocumentThumbnailType"], str
                          ] = dataclasses.field(
                              default=ShapeBase.NOT_SET,
                          )

    # The source of the document.
    source: typing.Dict[typing.Union[str, "DocumentSourceType"], str
                       ] = dataclasses.field(
                           default=ShapeBase.NOT_SET,
                       )


class DocumentVersionStatus(str):
    ACTIVE = "ACTIVE"


@dataclasses.dataclass
class DraftUploadOutOfSyncException(ShapeBase):
    """
    This exception is thrown when a valid checkout ID is not presented on document
    version upload calls for a document that has been checked out from Web client.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "message",
                "Message",
                TypeInfo(str),
            ),
        ]

    message: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class EntityAlreadyExistsException(ShapeBase):
    """
    The resource already exists.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "message",
                "Message",
                TypeInfo(str),
            ),
        ]

    message: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class EntityNotExistsException(ShapeBase):
    """
    The resource does not exist.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "message",
                "Message",
                TypeInfo(str),
            ),
            (
                "entity_ids",
                "EntityIds",
                TypeInfo(typing.List[str]),
            ),
        ]

    message: str = dataclasses.field(default=ShapeBase.NOT_SET, )
    entity_ids: typing.List[str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class FailedDependencyException(ShapeBase):
    """
    The AWS Directory Service cannot reach an on-premises instance. Or a dependency
    under the control of the organization is failing, such as a connected Active
    Directory.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "message",
                "Message",
                TypeInfo(str),
            ),
        ]

    message: str = dataclasses.field(default=ShapeBase.NOT_SET, )


class FolderContentType(str):
    ALL = "ALL"
    DOCUMENT = "DOCUMENT"
    FOLDER = "FOLDER"


@dataclasses.dataclass
class FolderMetadata(ShapeBase):
    """
    Describes a folder.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "id",
                "Id",
                TypeInfo(str),
            ),
            (
                "name",
                "Name",
                TypeInfo(str),
            ),
            (
                "creator_id",
                "CreatorId",
                TypeInfo(str),
            ),
            (
                "parent_folder_id",
                "ParentFolderId",
                TypeInfo(str),
            ),
            (
                "created_timestamp",
                "CreatedTimestamp",
                TypeInfo(datetime.datetime),
            ),
            (
                "modified_timestamp",
                "ModifiedTimestamp",
                TypeInfo(datetime.datetime),
            ),
            (
                "resource_state",
                "ResourceState",
                TypeInfo(typing.Union[str, ResourceStateType]),
            ),
            (
                "signature",
                "Signature",
                TypeInfo(str),
            ),
            (
                "labels",
                "Labels",
                TypeInfo(typing.List[str]),
            ),
            (
                "size",
                "Size",
                TypeInfo(int),
            ),
            (
                "latest_version_size",
                "LatestVersionSize",
                TypeInfo(int),
            ),
        ]

    # The ID of the folder.
    id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The name of the folder.
    name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The ID of the creator.
    creator_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The ID of the parent folder.
    parent_folder_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The time when the folder was created.
    created_timestamp: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The time when the folder was updated.
    modified_timestamp: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The resource state of the folder.
    resource_state: typing.Union[str, "ResourceStateType"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The unique identifier created from the subfolders and documents of the
    # folder.
    signature: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # List of labels on the folder.
    labels: typing.List[str] = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The size of the folder metadata.
    size: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The size of the latest version of the folder metadata.
    latest_version_size: int = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class GetCurrentUserRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "authentication_token",
                "AuthenticationToken",
                TypeInfo(str),
            ),
        ]

    # Amazon WorkDocs authentication token. Do not set this field when using
    # administrative API actions, as in accessing the API using AWS credentials.
    authentication_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class GetCurrentUserResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "user",
                "User",
                TypeInfo(User),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Metadata of the user.
    user: "User" = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class GetDocumentPathRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "document_id",
                "DocumentId",
                TypeInfo(str),
            ),
            (
                "authentication_token",
                "AuthenticationToken",
                TypeInfo(str),
            ),
            (
                "limit",
                "Limit",
                TypeInfo(int),
            ),
            (
                "fields",
                "Fields",
                TypeInfo(str),
            ),
            (
                "marker",
                "Marker",
                TypeInfo(str),
            ),
        ]

    # The ID of the document.
    document_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Amazon WorkDocs authentication token. Do not set this field when using
    # administrative API actions, as in accessing the API using AWS credentials.
    authentication_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The maximum number of levels in the hierarchy to return.
    limit: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A comma-separated list of values. Specify `NAME` to include the names of
    # the parent folders.
    fields: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # This value is not supported.
    marker: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class GetDocumentPathResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "path",
                "Path",
                TypeInfo(ResourcePath),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The path information.
    path: "ResourcePath" = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class GetDocumentRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "document_id",
                "DocumentId",
                TypeInfo(str),
            ),
            (
                "authentication_token",
                "AuthenticationToken",
                TypeInfo(str),
            ),
            (
                "include_custom_metadata",
                "IncludeCustomMetadata",
                TypeInfo(bool),
            ),
        ]

    # The ID of the document.
    document_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Amazon WorkDocs authentication token. Do not set this field when using
    # administrative API actions, as in accessing the API using AWS credentials.
    authentication_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Set this to `TRUE` to include custom metadata in the response.
    include_custom_metadata: bool = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class GetDocumentResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "metadata",
                "Metadata",
                TypeInfo(DocumentMetadata),
            ),
            (
                "custom_metadata",
                "CustomMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The metadata details of the document.
    metadata: "DocumentMetadata" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The custom metadata on the document.
    custom_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class GetDocumentVersionRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "document_id",
                "DocumentId",
                TypeInfo(str),
            ),
            (
                "version_id",
                "VersionId",
                TypeInfo(str),
            ),
            (
                "authentication_token",
                "AuthenticationToken",
                TypeInfo(str),
            ),
            (
                "fields",
                "Fields",
                TypeInfo(str),
            ),
            (
                "include_custom_metadata",
                "IncludeCustomMetadata",
                TypeInfo(bool),
            ),
        ]

    # The ID of the document.
    document_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The version ID of the document.
    version_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Amazon WorkDocs authentication token. Do not set this field when using
    # administrative API actions, as in accessing the API using AWS credentials.
    authentication_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A comma-separated list of values. Specify "SOURCE" to include a URL for the
    # source document.
    fields: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Set this to TRUE to include custom metadata in the response.
    include_custom_metadata: bool = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class GetDocumentVersionResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "metadata",
                "Metadata",
                TypeInfo(DocumentVersionMetadata),
            ),
            (
                "custom_metadata",
                "CustomMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The version metadata.
    metadata: "DocumentVersionMetadata" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The custom metadata on the document version.
    custom_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class GetFolderPathRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "folder_id",
                "FolderId",
                TypeInfo(str),
            ),
            (
                "authentication_token",
                "AuthenticationToken",
                TypeInfo(str),
            ),
            (
                "limit",
                "Limit",
                TypeInfo(int),
            ),
            (
                "fields",
                "Fields",
                TypeInfo(str),
            ),
            (
                "marker",
                "Marker",
                TypeInfo(str),
            ),
        ]

    # The ID of the folder.
    folder_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Amazon WorkDocs authentication token. Do not set this field when using
    # administrative API actions, as in accessing the API using AWS credentials.
    authentication_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The maximum number of levels in the hierarchy to return.
    limit: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A comma-separated list of values. Specify "NAME" to include the names of
    # the parent folders.
    fields: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # This value is not supported.
    marker: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class GetFolderPathResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "path",
                "Path",
                TypeInfo(ResourcePath),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The path information.
    path: "ResourcePath" = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class GetFolderRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "folder_id",
                "FolderId",
                TypeInfo(str),
            ),
            (
                "authentication_token",
                "AuthenticationToken",
                TypeInfo(str),
            ),
            (
                "include_custom_metadata",
                "IncludeCustomMetadata",
                TypeInfo(bool),
            ),
        ]

    # The ID of the folder.
    folder_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Amazon WorkDocs authentication token. Do not set this field when using
    # administrative API actions, as in accessing the API using AWS credentials.
    authentication_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Set to TRUE to include custom metadata in the response.
    include_custom_metadata: bool = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class GetFolderResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "metadata",
                "Metadata",
                TypeInfo(FolderMetadata),
            ),
            (
                "custom_metadata",
                "CustomMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The metadata of the folder.
    metadata: "FolderMetadata" = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The custom metadata on the folder.
    custom_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class GroupMetadata(ShapeBase):
    """
    Describes the metadata of a user group.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "id",
                "Id",
                TypeInfo(str),
            ),
            (
                "name",
                "Name",
                TypeInfo(str),
            ),
        ]

    # The ID of the user group.
    id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The name of the group.
    name: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class IllegalUserStateException(ShapeBase):
    """
    The user is undergoing transfer of ownership.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "message",
                "Message",
                TypeInfo(str),
            ),
        ]

    message: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class InitiateDocumentVersionUploadRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "parent_folder_id",
                "ParentFolderId",
                TypeInfo(str),
            ),
            (
                "authentication_token",
                "AuthenticationToken",
                TypeInfo(str),
            ),
            (
                "id",
                "Id",
                TypeInfo(str),
            ),
            (
                "name",
                "Name",
                TypeInfo(str),
            ),
            (
                "content_created_timestamp",
                "ContentCreatedTimestamp",
                TypeInfo(datetime.datetime),
            ),
            (
                "content_modified_timestamp",
                "ContentModifiedTimestamp",
                TypeInfo(datetime.datetime),
            ),
            (
                "content_type",
                "ContentType",
                TypeInfo(str),
            ),
            (
                "document_size_in_bytes",
                "DocumentSizeInBytes",
                TypeInfo(int),
            ),
        ]

    # The ID of the parent folder.
    parent_folder_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Amazon WorkDocs authentication token. Do not set this field when using
    # administrative API actions, as in accessing the API using AWS credentials.
    authentication_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The ID of the document.
    id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The name of the document.
    name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The timestamp when the content of the document was originally created.
    content_created_timestamp: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The timestamp when the content of the document was modified.
    content_modified_timestamp: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The content type of the document.
    content_type: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The size of the document, in bytes.
    document_size_in_bytes: int = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class InitiateDocumentVersionUploadResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "metadata",
                "Metadata",
                TypeInfo(DocumentMetadata),
            ),
            (
                "upload_metadata",
                "UploadMetadata",
                TypeInfo(UploadMetadata),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The document metadata.
    metadata: "DocumentMetadata" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The upload metadata.
    upload_metadata: "UploadMetadata" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class InvalidArgumentException(ShapeBase):
    """
    The pagination marker or limit fields are not valid.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "message",
                "Message",
                TypeInfo(str),
            ),
        ]

    message: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class InvalidOperationException(ShapeBase):
    """
    The operation is invalid.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "message",
                "Message",
                TypeInfo(str),
            ),
        ]

    message: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class InvalidPasswordException(ShapeBase):
    """
    The password is invalid.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "message",
                "Message",
                TypeInfo(str),
            ),
        ]

    message: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class LimitExceededException(ShapeBase):
    """
    The maximum of 100,000 folders under the parent folder has been exceeded.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "message",
                "Message",
                TypeInfo(str),
            ),
        ]

    message: str = dataclasses.field(default=ShapeBase.NOT_SET, )


class LocaleType(str):
    en = "en"
    fr = "fr"
    ko = "ko"
    de = "de"
    es = "es"
    ja = "ja"
    ru = "ru"
    zh_CN = "zh_CN"
    zh_TW = "zh_TW"
    pt_BR = "pt_BR"
    default = "default"


@dataclasses.dataclass
class NotificationOptions(ShapeBase):
    """
    Set of options which defines notification preferences of given action.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "send_email",
                "SendEmail",
                TypeInfo(bool),
            ),
            (
                "email_message",
                "EmailMessage",
                TypeInfo(str),
            ),
        ]

    # Boolean value to indicate an email notification should be sent to the
    # receipients.
    send_email: bool = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Text value to be included in the email body.
    email_message: str = dataclasses.field(default=ShapeBase.NOT_SET, )


class OrderType(str):
    ASCENDING = "ASCENDING"
    DESCENDING = "DESCENDING"


@dataclasses.dataclass
class Participants(ShapeBase):
    """
    Describes the users or user groups.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "users",
                "Users",
                TypeInfo(typing.List[UserMetadata]),
            ),
            (
                "groups",
                "Groups",
                TypeInfo(typing.List[GroupMetadata]),
            ),
        ]

    # The list of users.
    users: typing.List["UserMetadata"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The list of user groups.
    groups: typing.List["GroupMetadata"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class PermissionInfo(ShapeBase):
    """
    Describes the permissions.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "role",
                "Role",
                TypeInfo(typing.Union[str, RoleType]),
            ),
            (
                "type",
                "Type",
                TypeInfo(typing.Union[str, RolePermissionType]),
            ),
        ]

    # The role of the user.
    role: typing.Union[str, "RoleType"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The type of permissions.
    type: typing.Union[str, "RolePermissionType"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class Principal(ShapeBase):
    """
    Describes a resource.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "id",
                "Id",
                TypeInfo(str),
            ),
            (
                "type",
                "Type",
                TypeInfo(typing.Union[str, PrincipalType]),
            ),
            (
                "roles",
                "Roles",
                TypeInfo(typing.List[PermissionInfo]),
            ),
        ]

    # The ID of the resource.
    id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The type of resource.
    type: typing.Union[str, "PrincipalType"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The permission information for the resource.
    roles: typing.List["PermissionInfo"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


class PrincipalType(str):
    USER = "USER"
    GROUP = "GROUP"
    INVITE = "INVITE"
    ANONYMOUS = "ANONYMOUS"
    ORGANIZATION = "ORGANIZATION"


@dataclasses.dataclass
class ProhibitedStateException(ShapeBase):
    """
    The specified document version is not in the INITIALIZED state.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "message",
                "Message",
                TypeInfo(str),
            ),
        ]

    message: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class RemoveAllResourcePermissionsRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "resource_id",
                "ResourceId",
                TypeInfo(str),
            ),
            (
                "authentication_token",
                "AuthenticationToken",
                TypeInfo(str),
            ),
        ]

    # The ID of the resource.
    resource_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Amazon WorkDocs authentication token. Do not set this field when using
    # administrative API actions, as in accessing the API using AWS credentials.
    authentication_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class RemoveResourcePermissionRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "resource_id",
                "ResourceId",
                TypeInfo(str),
            ),
            (
                "principal_id",
                "PrincipalId",
                TypeInfo(str),
            ),
            (
                "authentication_token",
                "AuthenticationToken",
                TypeInfo(str),
            ),
            (
                "principal_type",
                "PrincipalType",
                TypeInfo(typing.Union[str, PrincipalType]),
            ),
        ]

    # The ID of the resource.
    resource_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The principal ID of the resource.
    principal_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Amazon WorkDocs authentication token. Do not set this field when using
    # administrative API actions, as in accessing the API using AWS credentials.
    authentication_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The principal type of the resource.
    principal_type: typing.Union[str, "PrincipalType"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class ResourceAlreadyCheckedOutException(ShapeBase):
    """
    The resource is already checked out.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "message",
                "Message",
                TypeInfo(str),
            ),
        ]

    message: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ResourceMetadata(ShapeBase):
    """
    Describes the metadata of a resource.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "type",
                "Type",
                TypeInfo(typing.Union[str, ResourceType]),
            ),
            (
                "name",
                "Name",
                TypeInfo(str),
            ),
            (
                "original_name",
                "OriginalName",
                TypeInfo(str),
            ),
            (
                "id",
                "Id",
                TypeInfo(str),
            ),
            (
                "version_id",
                "VersionId",
                TypeInfo(str),
            ),
            (
                "owner",
                "Owner",
                TypeInfo(UserMetadata),
            ),
            (
                "parent_id",
                "ParentId",
                TypeInfo(str),
            ),
        ]

    # The type of resource.
    type: typing.Union[str, "ResourceType"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The name of the resource.
    name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The original name of the resource before a rename operation.
    original_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The ID of the resource.
    id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The version ID of the resource. This is an optional field and is filled for
    # action on document version.
    version_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The owner of the resource.
    owner: "UserMetadata" = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The parent ID of the resource before a rename operation.
    parent_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ResourcePath(ShapeBase):
    """
    Describes the path information of a resource.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "components",
                "Components",
                TypeInfo(typing.List[ResourcePathComponent]),
            ),
        ]

    # The components of the resource path.
    components: typing.List["ResourcePathComponent"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class ResourcePathComponent(ShapeBase):
    """
    Describes the resource path.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "id",
                "Id",
                TypeInfo(str),
            ),
            (
                "name",
                "Name",
                TypeInfo(str),
            ),
        ]

    # The ID of the resource path.
    id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The name of the resource path.
    name: str = dataclasses.field(default=ShapeBase.NOT_SET, )


class ResourceSortType(str):
    DATE = "DATE"
    NAME = "NAME"


class ResourceStateType(str):
    ACTIVE = "ACTIVE"
    RESTORING = "RESTORING"
    RECYCLING = "RECYCLING"
    RECYCLED = "RECYCLED"


class ResourceType(str):
    FOLDER = "FOLDER"
    DOCUMENT = "DOCUMENT"


class RolePermissionType(str):
    DIRECT = "DIRECT"
    INHERITED = "INHERITED"


class RoleType(str):
    VIEWER = "VIEWER"
    CONTRIBUTOR = "CONTRIBUTOR"
    OWNER = "OWNER"
    COOWNER = "COOWNER"


@dataclasses.dataclass
class ServiceUnavailableException(ShapeBase):
    """
    One or more of the dependencies is unavailable.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "message",
                "Message",
                TypeInfo(str),
            ),
        ]

    message: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class SharePrincipal(ShapeBase):
    """
    Describes the recipient type and ID, if available.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "id",
                "Id",
                TypeInfo(str),
            ),
            (
                "type",
                "Type",
                TypeInfo(typing.Union[str, PrincipalType]),
            ),
            (
                "role",
                "Role",
                TypeInfo(typing.Union[str, RoleType]),
            ),
        ]

    # The ID of the recipient.
    id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The type of the recipient.
    type: typing.Union[str, "PrincipalType"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The role of the recipient.
    role: typing.Union[str, "RoleType"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class ShareResult(ShapeBase):
    """
    Describes the share results of a resource.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "principal_id",
                "PrincipalId",
                TypeInfo(str),
            ),
            (
                "role",
                "Role",
                TypeInfo(typing.Union[str, RoleType]),
            ),
            (
                "status",
                "Status",
                TypeInfo(typing.Union[str, ShareStatusType]),
            ),
            (
                "share_id",
                "ShareId",
                TypeInfo(str),
            ),
            (
                "status_message",
                "StatusMessage",
                TypeInfo(str),
            ),
        ]

    # The ID of the principal.
    principal_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The role.
    role: typing.Union[str, "RoleType"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The status.
    status: typing.Union[str, "ShareStatusType"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The ID of the resource that was shared.
    share_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The status message.
    status_message: str = dataclasses.field(default=ShapeBase.NOT_SET, )


class ShareStatusType(str):
    SUCCESS = "SUCCESS"
    FAILURE = "FAILURE"


@dataclasses.dataclass
class StorageLimitExceededException(ShapeBase):
    """
    The storage limit has been exceeded.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "message",
                "Message",
                TypeInfo(str),
            ),
        ]

    message: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class StorageLimitWillExceedException(ShapeBase):
    """
    The storage limit will be exceeded.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "message",
                "Message",
                TypeInfo(str),
            ),
        ]

    message: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class StorageRuleType(ShapeBase):
    """
    Describes the storage for a user.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "storage_allocated_in_bytes",
                "StorageAllocatedInBytes",
                TypeInfo(int),
            ),
            (
                "storage_type",
                "StorageType",
                TypeInfo(typing.Union[str, StorageType]),
            ),
        ]

    # The amount of storage allocated, in bytes.
    storage_allocated_in_bytes: int = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The type of storage.
    storage_type: typing.Union[str, "StorageType"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


class StorageType(str):
    UNLIMITED = "UNLIMITED"
    QUOTA = "QUOTA"


@dataclasses.dataclass
class Subscription(ShapeBase):
    """
    Describes a subscription.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "subscription_id",
                "SubscriptionId",
                TypeInfo(str),
            ),
            (
                "end_point",
                "EndPoint",
                TypeInfo(str),
            ),
            (
                "protocol",
                "Protocol",
                TypeInfo(typing.Union[str, SubscriptionProtocolType]),
            ),
        ]

    # The ID of the subscription.
    subscription_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The endpoint of the subscription.
    end_point: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The protocol of the subscription.
    protocol: typing.Union[str, "SubscriptionProtocolType"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


class SubscriptionProtocolType(str):
    HTTPS = "HTTPS"


class SubscriptionType(str):
    ALL = "ALL"


@dataclasses.dataclass
class TooManyLabelsException(ShapeBase):
    """
    The limit has been reached on the number of labels for the specified resource.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "message",
                "Message",
                TypeInfo(str),
            ),
        ]

    message: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class TooManySubscriptionsException(ShapeBase):
    """
    You've reached the limit on the number of subscriptions for the WorkDocs
    instance.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "message",
                "Message",
                TypeInfo(str),
            ),
        ]

    message: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class UnauthorizedOperationException(ShapeBase):
    """
    The operation is not permitted.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class UnauthorizedResourceAccessException(ShapeBase):
    """
    The caller does not have access to perform the action on the resource.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "message",
                "Message",
                TypeInfo(str),
            ),
        ]

    message: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class UpdateDocumentRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "document_id",
                "DocumentId",
                TypeInfo(str),
            ),
            (
                "authentication_token",
                "AuthenticationToken",
                TypeInfo(str),
            ),
            (
                "name",
                "Name",
                TypeInfo(str),
            ),
            (
                "parent_folder_id",
                "ParentFolderId",
                TypeInfo(str),
            ),
            (
                "resource_state",
                "ResourceState",
                TypeInfo(typing.Union[str, ResourceStateType]),
            ),
        ]

    # The ID of the document.
    document_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Amazon WorkDocs authentication token. Do not set this field when using
    # administrative API actions, as in accessing the API using AWS credentials.
    authentication_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The name of the document.
    name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The ID of the parent folder.
    parent_folder_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The resource state of the document. Only ACTIVE and RECYCLED are supported.
    resource_state: typing.Union[str, "ResourceStateType"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class UpdateDocumentVersionRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "document_id",
                "DocumentId",
                TypeInfo(str),
            ),
            (
                "version_id",
                "VersionId",
                TypeInfo(str),
            ),
            (
                "authentication_token",
                "AuthenticationToken",
                TypeInfo(str),
            ),
            (
                "version_status",
                "VersionStatus",
                TypeInfo(typing.Union[str, DocumentVersionStatus]),
            ),
        ]

    # The ID of the document.
    document_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The version ID of the document.
    version_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Amazon WorkDocs authentication token. Do not set this field when using
    # administrative API actions, as in accessing the API using AWS credentials.
    authentication_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The status of the version.
    version_status: typing.Union[str, "DocumentVersionStatus"
                                ] = dataclasses.field(
                                    default=ShapeBase.NOT_SET,
                                )


@dataclasses.dataclass
class UpdateFolderRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "folder_id",
                "FolderId",
                TypeInfo(str),
            ),
            (
                "authentication_token",
                "AuthenticationToken",
                TypeInfo(str),
            ),
            (
                "name",
                "Name",
                TypeInfo(str),
            ),
            (
                "parent_folder_id",
                "ParentFolderId",
                TypeInfo(str),
            ),
            (
                "resource_state",
                "ResourceState",
                TypeInfo(typing.Union[str, ResourceStateType]),
            ),
        ]

    # The ID of the folder.
    folder_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Amazon WorkDocs authentication token. Do not set this field when using
    # administrative API actions, as in accessing the API using AWS credentials.
    authentication_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The name of the folder.
    name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The ID of the parent folder.
    parent_folder_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The resource state of the folder. Only ACTIVE and RECYCLED are accepted
    # values from the API.
    resource_state: typing.Union[str, "ResourceStateType"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class UpdateUserRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "user_id",
                "UserId",
                TypeInfo(str),
            ),
            (
                "authentication_token",
                "AuthenticationToken",
                TypeInfo(str),
            ),
            (
                "given_name",
                "GivenName",
                TypeInfo(str),
            ),
            (
                "surname",
                "Surname",
                TypeInfo(str),
            ),
            (
                "type",
                "Type",
                TypeInfo(typing.Union[str, UserType]),
            ),
            (
                "storage_rule",
                "StorageRule",
                TypeInfo(StorageRuleType),
            ),
            (
                "time_zone_id",
                "TimeZoneId",
                TypeInfo(str),
            ),
            (
                "locale",
                "Locale",
                TypeInfo(typing.Union[str, LocaleType]),
            ),
            (
                "grant_poweruser_privileges",
                "GrantPoweruserPrivileges",
                TypeInfo(typing.Union[str, BooleanEnumType]),
            ),
        ]

    # The ID of the user.
    user_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Amazon WorkDocs authentication token. Do not set this field when using
    # administrative API actions, as in accessing the API using AWS credentials.
    authentication_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The given name of the user.
    given_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The surname of the user.
    surname: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The type of the user.
    type: typing.Union[str, "UserType"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The amount of storage for the user.
    storage_rule: "StorageRuleType" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The time zone ID of the user.
    time_zone_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The locale of the user.
    locale: typing.Union[str, "LocaleType"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Boolean value to determine whether the user is granted Poweruser
    # privileges.
    grant_poweruser_privileges: typing.Union[str, "BooleanEnumType"
                                            ] = dataclasses.field(
                                                default=ShapeBase.NOT_SET,
                                            )


@dataclasses.dataclass
class UpdateUserResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "user",
                "User",
                TypeInfo(User),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The user information.
    user: "User" = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class UploadMetadata(ShapeBase):
    """
    Describes the upload.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "upload_url",
                "UploadUrl",
                TypeInfo(str),
            ),
            (
                "signed_headers",
                "SignedHeaders",
                TypeInfo(typing.Dict[str, str]),
            ),
        ]

    # The URL of the upload.
    upload_url: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The signed headers.
    signed_headers: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class User(ShapeBase):
    """
    Describes a user.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "id",
                "Id",
                TypeInfo(str),
            ),
            (
                "username",
                "Username",
                TypeInfo(str),
            ),
            (
                "email_address",
                "EmailAddress",
                TypeInfo(str),
            ),
            (
                "given_name",
                "GivenName",
                TypeInfo(str),
            ),
            (
                "surname",
                "Surname",
                TypeInfo(str),
            ),
            (
                "organization_id",
                "OrganizationId",
                TypeInfo(str),
            ),
            (
                "root_folder_id",
                "RootFolderId",
                TypeInfo(str),
            ),
            (
                "recycle_bin_folder_id",
                "RecycleBinFolderId",
                TypeInfo(str),
            ),
            (
                "status",
                "Status",
                TypeInfo(typing.Union[str, UserStatusType]),
            ),
            (
                "type",
                "Type",
                TypeInfo(typing.Union[str, UserType]),
            ),
            (
                "created_timestamp",
                "CreatedTimestamp",
                TypeInfo(datetime.datetime),
            ),
            (
                "modified_timestamp",
                "ModifiedTimestamp",
                TypeInfo(datetime.datetime),
            ),
            (
                "time_zone_id",
                "TimeZoneId",
                TypeInfo(str),
            ),
            (
                "locale",
                "Locale",
                TypeInfo(typing.Union[str, LocaleType]),
            ),
            (
                "storage",
                "Storage",
                TypeInfo(UserStorageMetadata),
            ),
        ]

    # The ID of the user.
    id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The login name of the user.
    username: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The email address of the user.
    email_address: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The given name of the user.
    given_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The surname of the user.
    surname: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The ID of the organization.
    organization_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The ID of the root folder.
    root_folder_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The ID of the recycle bin folder.
    recycle_bin_folder_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The status of the user.
    status: typing.Union[str, "UserStatusType"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The type of user.
    type: typing.Union[str, "UserType"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The time when the user was created.
    created_timestamp: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The time when the user was modified.
    modified_timestamp: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The time zone ID of the user.
    time_zone_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The locale of the user.
    locale: typing.Union[str, "LocaleType"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The storage for the user.
    storage: "UserStorageMetadata" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


class UserFilterType(str):
    ALL = "ALL"
    ACTIVE_PENDING = "ACTIVE_PENDING"


@dataclasses.dataclass
class UserMetadata(ShapeBase):
    """
    Describes the metadata of the user.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "id",
                "Id",
                TypeInfo(str),
            ),
            (
                "username",
                "Username",
                TypeInfo(str),
            ),
            (
                "given_name",
                "GivenName",
                TypeInfo(str),
            ),
            (
                "surname",
                "Surname",
                TypeInfo(str),
            ),
            (
                "email_address",
                "EmailAddress",
                TypeInfo(str),
            ),
        ]

    # The ID of the user.
    id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The name of the user.
    username: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The given name of the user before a rename operation.
    given_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The surname of the user.
    surname: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The email address of the user.
    email_address: str = dataclasses.field(default=ShapeBase.NOT_SET, )


class UserSortType(str):
    USER_NAME = "USER_NAME"
    FULL_NAME = "FULL_NAME"
    STORAGE_LIMIT = "STORAGE_LIMIT"
    USER_STATUS = "USER_STATUS"
    STORAGE_USED = "STORAGE_USED"


class UserStatusType(str):
    ACTIVE = "ACTIVE"
    INACTIVE = "INACTIVE"
    PENDING = "PENDING"


@dataclasses.dataclass
class UserStorageMetadata(ShapeBase):
    """
    Describes the storage for a user.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "storage_utilized_in_bytes",
                "StorageUtilizedInBytes",
                TypeInfo(int),
            ),
            (
                "storage_rule",
                "StorageRule",
                TypeInfo(StorageRuleType),
            ),
        ]

    # The amount of storage used, in bytes.
    storage_utilized_in_bytes: int = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The storage for a user.
    storage_rule: "StorageRuleType" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


class UserType(str):
    USER = "USER"
    ADMIN = "ADMIN"
    POWERUSER = "POWERUSER"
    MINIMALUSER = "MINIMALUSER"
    WORKSPACESUSER = "WORKSPACESUSER"
