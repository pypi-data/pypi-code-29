import datetime
import typing
import boto3
from autoboto import ClientBase, ShapeBase, OutputShapeBase
from . import shapes


class Client(ClientBase):
    def __init__(self, *args, **kwargs):
        super().__init__("workdocs", *args, **kwargs)

    def abort_document_version_upload(
        self,
        _request: shapes.AbortDocumentVersionUploadRequest = None,
        *,
        document_id: str,
        version_id: str,
        authentication_token: str = ShapeBase.NOT_SET,
    ) -> None:
        """
        Aborts the upload of the specified document version that was previously
        initiated by InitiateDocumentVersionUpload. The client should make this call
        only when it no longer intends to upload the document version, or fails to do
        so.
        """
        if _request is None:
            _params = {}
            if document_id is not ShapeBase.NOT_SET:
                _params['document_id'] = document_id
            if version_id is not ShapeBase.NOT_SET:
                _params['version_id'] = version_id
            if authentication_token is not ShapeBase.NOT_SET:
                _params['authentication_token'] = authentication_token
            _request = shapes.AbortDocumentVersionUploadRequest(**_params)
        response = self._boto_client.abort_document_version_upload(
            **_request.to_boto()
        )

    def activate_user(
        self,
        _request: shapes.ActivateUserRequest = None,
        *,
        user_id: str,
        authentication_token: str = ShapeBase.NOT_SET,
    ) -> shapes.ActivateUserResponse:
        """
        Activates the specified user. Only active users can access Amazon WorkDocs.
        """
        if _request is None:
            _params = {}
            if user_id is not ShapeBase.NOT_SET:
                _params['user_id'] = user_id
            if authentication_token is not ShapeBase.NOT_SET:
                _params['authentication_token'] = authentication_token
            _request = shapes.ActivateUserRequest(**_params)
        response = self._boto_client.activate_user(**_request.to_boto())

        return shapes.ActivateUserResponse.from_boto(response)

    def add_resource_permissions(
        self,
        _request: shapes.AddResourcePermissionsRequest = None,
        *,
        resource_id: str,
        principals: typing.List[shapes.SharePrincipal],
        authentication_token: str = ShapeBase.NOT_SET,
        notification_options: shapes.NotificationOptions = ShapeBase.NOT_SET,
    ) -> shapes.AddResourcePermissionsResponse:
        """
        Creates a set of permissions for the specified folder or document. The resource
        permissions are overwritten if the principals already have different
        permissions.
        """
        if _request is None:
            _params = {}
            if resource_id is not ShapeBase.NOT_SET:
                _params['resource_id'] = resource_id
            if principals is not ShapeBase.NOT_SET:
                _params['principals'] = principals
            if authentication_token is not ShapeBase.NOT_SET:
                _params['authentication_token'] = authentication_token
            if notification_options is not ShapeBase.NOT_SET:
                _params['notification_options'] = notification_options
            _request = shapes.AddResourcePermissionsRequest(**_params)
        response = self._boto_client.add_resource_permissions(
            **_request.to_boto()
        )

        return shapes.AddResourcePermissionsResponse.from_boto(response)

    def create_comment(
        self,
        _request: shapes.CreateCommentRequest = None,
        *,
        document_id: str,
        version_id: str,
        text: str,
        authentication_token: str = ShapeBase.NOT_SET,
        parent_id: str = ShapeBase.NOT_SET,
        thread_id: str = ShapeBase.NOT_SET,
        visibility: typing.Union[str, shapes.CommentVisibilityType] = ShapeBase.
        NOT_SET,
        notify_collaborators: bool = ShapeBase.NOT_SET,
    ) -> shapes.CreateCommentResponse:
        """
        Adds a new comment to the specified document version.
        """
        if _request is None:
            _params = {}
            if document_id is not ShapeBase.NOT_SET:
                _params['document_id'] = document_id
            if version_id is not ShapeBase.NOT_SET:
                _params['version_id'] = version_id
            if text is not ShapeBase.NOT_SET:
                _params['text'] = text
            if authentication_token is not ShapeBase.NOT_SET:
                _params['authentication_token'] = authentication_token
            if parent_id is not ShapeBase.NOT_SET:
                _params['parent_id'] = parent_id
            if thread_id is not ShapeBase.NOT_SET:
                _params['thread_id'] = thread_id
            if visibility is not ShapeBase.NOT_SET:
                _params['visibility'] = visibility
            if notify_collaborators is not ShapeBase.NOT_SET:
                _params['notify_collaborators'] = notify_collaborators
            _request = shapes.CreateCommentRequest(**_params)
        response = self._boto_client.create_comment(**_request.to_boto())

        return shapes.CreateCommentResponse.from_boto(response)

    def create_custom_metadata(
        self,
        _request: shapes.CreateCustomMetadataRequest = None,
        *,
        resource_id: str,
        custom_metadata: typing.Dict[str, str],
        authentication_token: str = ShapeBase.NOT_SET,
        version_id: str = ShapeBase.NOT_SET,
    ) -> shapes.CreateCustomMetadataResponse:
        """
        Adds one or more custom properties to the specified resource (a folder,
        document, or version).
        """
        if _request is None:
            _params = {}
            if resource_id is not ShapeBase.NOT_SET:
                _params['resource_id'] = resource_id
            if custom_metadata is not ShapeBase.NOT_SET:
                _params['custom_metadata'] = custom_metadata
            if authentication_token is not ShapeBase.NOT_SET:
                _params['authentication_token'] = authentication_token
            if version_id is not ShapeBase.NOT_SET:
                _params['version_id'] = version_id
            _request = shapes.CreateCustomMetadataRequest(**_params)
        response = self._boto_client.create_custom_metadata(
            **_request.to_boto()
        )

        return shapes.CreateCustomMetadataResponse.from_boto(response)

    def create_folder(
        self,
        _request: shapes.CreateFolderRequest = None,
        *,
        parent_folder_id: str,
        authentication_token: str = ShapeBase.NOT_SET,
        name: str = ShapeBase.NOT_SET,
    ) -> shapes.CreateFolderResponse:
        """
        Creates a folder with the specified name and parent folder.
        """
        if _request is None:
            _params = {}
            if parent_folder_id is not ShapeBase.NOT_SET:
                _params['parent_folder_id'] = parent_folder_id
            if authentication_token is not ShapeBase.NOT_SET:
                _params['authentication_token'] = authentication_token
            if name is not ShapeBase.NOT_SET:
                _params['name'] = name
            _request = shapes.CreateFolderRequest(**_params)
        response = self._boto_client.create_folder(**_request.to_boto())

        return shapes.CreateFolderResponse.from_boto(response)

    def create_labels(
        self,
        _request: shapes.CreateLabelsRequest = None,
        *,
        resource_id: str,
        labels: typing.List[str],
        authentication_token: str = ShapeBase.NOT_SET,
    ) -> shapes.CreateLabelsResponse:
        """
        Adds the specified list of labels to the given resource (a document or folder)
        """
        if _request is None:
            _params = {}
            if resource_id is not ShapeBase.NOT_SET:
                _params['resource_id'] = resource_id
            if labels is not ShapeBase.NOT_SET:
                _params['labels'] = labels
            if authentication_token is not ShapeBase.NOT_SET:
                _params['authentication_token'] = authentication_token
            _request = shapes.CreateLabelsRequest(**_params)
        response = self._boto_client.create_labels(**_request.to_boto())

        return shapes.CreateLabelsResponse.from_boto(response)

    def create_notification_subscription(
        self,
        _request: shapes.CreateNotificationSubscriptionRequest = None,
        *,
        organization_id: str,
        endpoint: str,
        protocol: typing.Union[str, shapes.SubscriptionProtocolType],
        subscription_type: typing.Union[str, shapes.SubscriptionType],
    ) -> shapes.CreateNotificationSubscriptionResponse:
        """
        Configure WorkDocs to use Amazon SNS notifications.

        The endpoint receives a confirmation message, and must confirm the subscription.
        For more information, see [Confirm the
        Subscription](http://docs.aws.amazon.com/sns/latest/dg/SendMessageToHttp.html#SendMessageToHttp.confirm)
        in the _Amazon Simple Notification Service Developer Guide_.
        """
        if _request is None:
            _params = {}
            if organization_id is not ShapeBase.NOT_SET:
                _params['organization_id'] = organization_id
            if endpoint is not ShapeBase.NOT_SET:
                _params['endpoint'] = endpoint
            if protocol is not ShapeBase.NOT_SET:
                _params['protocol'] = protocol
            if subscription_type is not ShapeBase.NOT_SET:
                _params['subscription_type'] = subscription_type
            _request = shapes.CreateNotificationSubscriptionRequest(**_params)
        response = self._boto_client.create_notification_subscription(
            **_request.to_boto()
        )

        return shapes.CreateNotificationSubscriptionResponse.from_boto(response)

    def create_user(
        self,
        _request: shapes.CreateUserRequest = None,
        *,
        username: str,
        given_name: str,
        surname: str,
        password: str,
        organization_id: str = ShapeBase.NOT_SET,
        email_address: str = ShapeBase.NOT_SET,
        time_zone_id: str = ShapeBase.NOT_SET,
        storage_rule: shapes.StorageRuleType = ShapeBase.NOT_SET,
        authentication_token: str = ShapeBase.NOT_SET,
    ) -> shapes.CreateUserResponse:
        """
        Creates a user in a Simple AD or Microsoft AD directory. The status of a newly
        created user is "ACTIVE". New users can access Amazon WorkDocs.
        """
        if _request is None:
            _params = {}
            if username is not ShapeBase.NOT_SET:
                _params['username'] = username
            if given_name is not ShapeBase.NOT_SET:
                _params['given_name'] = given_name
            if surname is not ShapeBase.NOT_SET:
                _params['surname'] = surname
            if password is not ShapeBase.NOT_SET:
                _params['password'] = password
            if organization_id is not ShapeBase.NOT_SET:
                _params['organization_id'] = organization_id
            if email_address is not ShapeBase.NOT_SET:
                _params['email_address'] = email_address
            if time_zone_id is not ShapeBase.NOT_SET:
                _params['time_zone_id'] = time_zone_id
            if storage_rule is not ShapeBase.NOT_SET:
                _params['storage_rule'] = storage_rule
            if authentication_token is not ShapeBase.NOT_SET:
                _params['authentication_token'] = authentication_token
            _request = shapes.CreateUserRequest(**_params)
        response = self._boto_client.create_user(**_request.to_boto())

        return shapes.CreateUserResponse.from_boto(response)

    def deactivate_user(
        self,
        _request: shapes.DeactivateUserRequest = None,
        *,
        user_id: str,
        authentication_token: str = ShapeBase.NOT_SET,
    ) -> None:
        """
        Deactivates the specified user, which revokes the user's access to Amazon
        WorkDocs.
        """
        if _request is None:
            _params = {}
            if user_id is not ShapeBase.NOT_SET:
                _params['user_id'] = user_id
            if authentication_token is not ShapeBase.NOT_SET:
                _params['authentication_token'] = authentication_token
            _request = shapes.DeactivateUserRequest(**_params)
        response = self._boto_client.deactivate_user(**_request.to_boto())

    def delete_comment(
        self,
        _request: shapes.DeleteCommentRequest = None,
        *,
        document_id: str,
        version_id: str,
        comment_id: str,
        authentication_token: str = ShapeBase.NOT_SET,
    ) -> None:
        """
        Deletes the specified comment from the document version.
        """
        if _request is None:
            _params = {}
            if document_id is not ShapeBase.NOT_SET:
                _params['document_id'] = document_id
            if version_id is not ShapeBase.NOT_SET:
                _params['version_id'] = version_id
            if comment_id is not ShapeBase.NOT_SET:
                _params['comment_id'] = comment_id
            if authentication_token is not ShapeBase.NOT_SET:
                _params['authentication_token'] = authentication_token
            _request = shapes.DeleteCommentRequest(**_params)
        response = self._boto_client.delete_comment(**_request.to_boto())

    def delete_custom_metadata(
        self,
        _request: shapes.DeleteCustomMetadataRequest = None,
        *,
        resource_id: str,
        authentication_token: str = ShapeBase.NOT_SET,
        version_id: str = ShapeBase.NOT_SET,
        keys: typing.List[str] = ShapeBase.NOT_SET,
        delete_all: bool = ShapeBase.NOT_SET,
    ) -> shapes.DeleteCustomMetadataResponse:
        """
        Deletes custom metadata from the specified resource.
        """
        if _request is None:
            _params = {}
            if resource_id is not ShapeBase.NOT_SET:
                _params['resource_id'] = resource_id
            if authentication_token is not ShapeBase.NOT_SET:
                _params['authentication_token'] = authentication_token
            if version_id is not ShapeBase.NOT_SET:
                _params['version_id'] = version_id
            if keys is not ShapeBase.NOT_SET:
                _params['keys'] = keys
            if delete_all is not ShapeBase.NOT_SET:
                _params['delete_all'] = delete_all
            _request = shapes.DeleteCustomMetadataRequest(**_params)
        response = self._boto_client.delete_custom_metadata(
            **_request.to_boto()
        )

        return shapes.DeleteCustomMetadataResponse.from_boto(response)

    def delete_document(
        self,
        _request: shapes.DeleteDocumentRequest = None,
        *,
        document_id: str,
        authentication_token: str = ShapeBase.NOT_SET,
    ) -> None:
        """
        Permanently deletes the specified document and its associated metadata.
        """
        if _request is None:
            _params = {}
            if document_id is not ShapeBase.NOT_SET:
                _params['document_id'] = document_id
            if authentication_token is not ShapeBase.NOT_SET:
                _params['authentication_token'] = authentication_token
            _request = shapes.DeleteDocumentRequest(**_params)
        response = self._boto_client.delete_document(**_request.to_boto())

    def delete_folder(
        self,
        _request: shapes.DeleteFolderRequest = None,
        *,
        folder_id: str,
        authentication_token: str = ShapeBase.NOT_SET,
    ) -> None:
        """
        Permanently deletes the specified folder and its contents.
        """
        if _request is None:
            _params = {}
            if folder_id is not ShapeBase.NOT_SET:
                _params['folder_id'] = folder_id
            if authentication_token is not ShapeBase.NOT_SET:
                _params['authentication_token'] = authentication_token
            _request = shapes.DeleteFolderRequest(**_params)
        response = self._boto_client.delete_folder(**_request.to_boto())

    def delete_folder_contents(
        self,
        _request: shapes.DeleteFolderContentsRequest = None,
        *,
        folder_id: str,
        authentication_token: str = ShapeBase.NOT_SET,
    ) -> None:
        """
        Deletes the contents of the specified folder.
        """
        if _request is None:
            _params = {}
            if folder_id is not ShapeBase.NOT_SET:
                _params['folder_id'] = folder_id
            if authentication_token is not ShapeBase.NOT_SET:
                _params['authentication_token'] = authentication_token
            _request = shapes.DeleteFolderContentsRequest(**_params)
        response = self._boto_client.delete_folder_contents(
            **_request.to_boto()
        )

    def delete_labels(
        self,
        _request: shapes.DeleteLabelsRequest = None,
        *,
        resource_id: str,
        authentication_token: str = ShapeBase.NOT_SET,
        labels: typing.List[str] = ShapeBase.NOT_SET,
        delete_all: bool = ShapeBase.NOT_SET,
    ) -> shapes.DeleteLabelsResponse:
        """
        Deletes the specified list of labels from a resource.
        """
        if _request is None:
            _params = {}
            if resource_id is not ShapeBase.NOT_SET:
                _params['resource_id'] = resource_id
            if authentication_token is not ShapeBase.NOT_SET:
                _params['authentication_token'] = authentication_token
            if labels is not ShapeBase.NOT_SET:
                _params['labels'] = labels
            if delete_all is not ShapeBase.NOT_SET:
                _params['delete_all'] = delete_all
            _request = shapes.DeleteLabelsRequest(**_params)
        response = self._boto_client.delete_labels(**_request.to_boto())

        return shapes.DeleteLabelsResponse.from_boto(response)

    def delete_notification_subscription(
        self,
        _request: shapes.DeleteNotificationSubscriptionRequest = None,
        *,
        subscription_id: str,
        organization_id: str,
    ) -> None:
        """
        Deletes the specified subscription from the specified organization.
        """
        if _request is None:
            _params = {}
            if subscription_id is not ShapeBase.NOT_SET:
                _params['subscription_id'] = subscription_id
            if organization_id is not ShapeBase.NOT_SET:
                _params['organization_id'] = organization_id
            _request = shapes.DeleteNotificationSubscriptionRequest(**_params)
        response = self._boto_client.delete_notification_subscription(
            **_request.to_boto()
        )

    def delete_user(
        self,
        _request: shapes.DeleteUserRequest = None,
        *,
        user_id: str,
        authentication_token: str = ShapeBase.NOT_SET,
    ) -> None:
        """
        Deletes the specified user from a Simple AD or Microsoft AD directory.
        """
        if _request is None:
            _params = {}
            if user_id is not ShapeBase.NOT_SET:
                _params['user_id'] = user_id
            if authentication_token is not ShapeBase.NOT_SET:
                _params['authentication_token'] = authentication_token
            _request = shapes.DeleteUserRequest(**_params)
        response = self._boto_client.delete_user(**_request.to_boto())

    def describe_activities(
        self,
        _request: shapes.DescribeActivitiesRequest = None,
        *,
        authentication_token: str = ShapeBase.NOT_SET,
        start_time: datetime.datetime = ShapeBase.NOT_SET,
        end_time: datetime.datetime = ShapeBase.NOT_SET,
        organization_id: str = ShapeBase.NOT_SET,
        user_id: str = ShapeBase.NOT_SET,
        limit: int = ShapeBase.NOT_SET,
        marker: str = ShapeBase.NOT_SET,
    ) -> shapes.DescribeActivitiesResponse:
        """
        Describes the user activities in a specified time period.
        """
        if _request is None:
            _params = {}
            if authentication_token is not ShapeBase.NOT_SET:
                _params['authentication_token'] = authentication_token
            if start_time is not ShapeBase.NOT_SET:
                _params['start_time'] = start_time
            if end_time is not ShapeBase.NOT_SET:
                _params['end_time'] = end_time
            if organization_id is not ShapeBase.NOT_SET:
                _params['organization_id'] = organization_id
            if user_id is not ShapeBase.NOT_SET:
                _params['user_id'] = user_id
            if limit is not ShapeBase.NOT_SET:
                _params['limit'] = limit
            if marker is not ShapeBase.NOT_SET:
                _params['marker'] = marker
            _request = shapes.DescribeActivitiesRequest(**_params)
        response = self._boto_client.describe_activities(**_request.to_boto())

        return shapes.DescribeActivitiesResponse.from_boto(response)

    def describe_comments(
        self,
        _request: shapes.DescribeCommentsRequest = None,
        *,
        document_id: str,
        version_id: str,
        authentication_token: str = ShapeBase.NOT_SET,
        limit: int = ShapeBase.NOT_SET,
        marker: str = ShapeBase.NOT_SET,
    ) -> shapes.DescribeCommentsResponse:
        """
        List all the comments for the specified document version.
        """
        if _request is None:
            _params = {}
            if document_id is not ShapeBase.NOT_SET:
                _params['document_id'] = document_id
            if version_id is not ShapeBase.NOT_SET:
                _params['version_id'] = version_id
            if authentication_token is not ShapeBase.NOT_SET:
                _params['authentication_token'] = authentication_token
            if limit is not ShapeBase.NOT_SET:
                _params['limit'] = limit
            if marker is not ShapeBase.NOT_SET:
                _params['marker'] = marker
            _request = shapes.DescribeCommentsRequest(**_params)
        response = self._boto_client.describe_comments(**_request.to_boto())

        return shapes.DescribeCommentsResponse.from_boto(response)

    def describe_document_versions(
        self,
        _request: shapes.DescribeDocumentVersionsRequest = None,
        *,
        document_id: str,
        authentication_token: str = ShapeBase.NOT_SET,
        marker: str = ShapeBase.NOT_SET,
        limit: int = ShapeBase.NOT_SET,
        include: str = ShapeBase.NOT_SET,
        fields: str = ShapeBase.NOT_SET,
    ) -> shapes.DescribeDocumentVersionsResponse:
        """
        Retrieves the document versions for the specified document.

        By default, only active versions are returned.
        """
        if _request is None:
            _params = {}
            if document_id is not ShapeBase.NOT_SET:
                _params['document_id'] = document_id
            if authentication_token is not ShapeBase.NOT_SET:
                _params['authentication_token'] = authentication_token
            if marker is not ShapeBase.NOT_SET:
                _params['marker'] = marker
            if limit is not ShapeBase.NOT_SET:
                _params['limit'] = limit
            if include is not ShapeBase.NOT_SET:
                _params['include'] = include
            if fields is not ShapeBase.NOT_SET:
                _params['fields'] = fields
            _request = shapes.DescribeDocumentVersionsRequest(**_params)
        paginator = self.get_paginator("describe_document_versions").paginate(
            **_request.to_boto()
        )
        page_generator = (page for page in paginator)
        first_page = next(page_generator)
        result = shapes.DescribeDocumentVersionsResponse.from_boto(first_page)
        result._page_iterator = page_generator
        return result

        return shapes.DescribeDocumentVersionsResponse.from_boto(response)

    def describe_folder_contents(
        self,
        _request: shapes.DescribeFolderContentsRequest = None,
        *,
        folder_id: str,
        authentication_token: str = ShapeBase.NOT_SET,
        sort: typing.Union[str, shapes.ResourceSortType] = ShapeBase.NOT_SET,
        order: typing.Union[str, shapes.OrderType] = ShapeBase.NOT_SET,
        limit: int = ShapeBase.NOT_SET,
        marker: str = ShapeBase.NOT_SET,
        type: typing.Union[str, shapes.FolderContentType] = ShapeBase.NOT_SET,
        include: str = ShapeBase.NOT_SET,
    ) -> shapes.DescribeFolderContentsResponse:
        """
        Describes the contents of the specified folder, including its documents and
        subfolders.

        By default, Amazon WorkDocs returns the first 100 active document and folder
        metadata items. If there are more results, the response includes a marker that
        you can use to request the next set of results. You can also request initialized
        documents.
        """
        if _request is None:
            _params = {}
            if folder_id is not ShapeBase.NOT_SET:
                _params['folder_id'] = folder_id
            if authentication_token is not ShapeBase.NOT_SET:
                _params['authentication_token'] = authentication_token
            if sort is not ShapeBase.NOT_SET:
                _params['sort'] = sort
            if order is not ShapeBase.NOT_SET:
                _params['order'] = order
            if limit is not ShapeBase.NOT_SET:
                _params['limit'] = limit
            if marker is not ShapeBase.NOT_SET:
                _params['marker'] = marker
            if type is not ShapeBase.NOT_SET:
                _params['type'] = type
            if include is not ShapeBase.NOT_SET:
                _params['include'] = include
            _request = shapes.DescribeFolderContentsRequest(**_params)
        paginator = self.get_paginator("describe_folder_contents").paginate(
            **_request.to_boto()
        )
        page_generator = (page for page in paginator)
        first_page = next(page_generator)
        result = shapes.DescribeFolderContentsResponse.from_boto(first_page)
        result._page_iterator = page_generator
        return result

        return shapes.DescribeFolderContentsResponse.from_boto(response)

    def describe_groups(
        self,
        _request: shapes.DescribeGroupsRequest = None,
        *,
        search_query: str,
        authentication_token: str = ShapeBase.NOT_SET,
        organization_id: str = ShapeBase.NOT_SET,
        marker: str = ShapeBase.NOT_SET,
        limit: int = ShapeBase.NOT_SET,
    ) -> shapes.DescribeGroupsResponse:
        """
        Describes the groups specified by query.
        """
        if _request is None:
            _params = {}
            if search_query is not ShapeBase.NOT_SET:
                _params['search_query'] = search_query
            if authentication_token is not ShapeBase.NOT_SET:
                _params['authentication_token'] = authentication_token
            if organization_id is not ShapeBase.NOT_SET:
                _params['organization_id'] = organization_id
            if marker is not ShapeBase.NOT_SET:
                _params['marker'] = marker
            if limit is not ShapeBase.NOT_SET:
                _params['limit'] = limit
            _request = shapes.DescribeGroupsRequest(**_params)
        response = self._boto_client.describe_groups(**_request.to_boto())

        return shapes.DescribeGroupsResponse.from_boto(response)

    def describe_notification_subscriptions(
        self,
        _request: shapes.DescribeNotificationSubscriptionsRequest = None,
        *,
        organization_id: str,
        marker: str = ShapeBase.NOT_SET,
        limit: int = ShapeBase.NOT_SET,
    ) -> shapes.DescribeNotificationSubscriptionsResponse:
        """
        Lists the specified notification subscriptions.
        """
        if _request is None:
            _params = {}
            if organization_id is not ShapeBase.NOT_SET:
                _params['organization_id'] = organization_id
            if marker is not ShapeBase.NOT_SET:
                _params['marker'] = marker
            if limit is not ShapeBase.NOT_SET:
                _params['limit'] = limit
            _request = shapes.DescribeNotificationSubscriptionsRequest(
                **_params
            )
        response = self._boto_client.describe_notification_subscriptions(
            **_request.to_boto()
        )

        return shapes.DescribeNotificationSubscriptionsResponse.from_boto(
            response
        )

    def describe_resource_permissions(
        self,
        _request: shapes.DescribeResourcePermissionsRequest = None,
        *,
        resource_id: str,
        authentication_token: str = ShapeBase.NOT_SET,
        principal_id: str = ShapeBase.NOT_SET,
        limit: int = ShapeBase.NOT_SET,
        marker: str = ShapeBase.NOT_SET,
    ) -> shapes.DescribeResourcePermissionsResponse:
        """
        Describes the permissions of a specified resource.
        """
        if _request is None:
            _params = {}
            if resource_id is not ShapeBase.NOT_SET:
                _params['resource_id'] = resource_id
            if authentication_token is not ShapeBase.NOT_SET:
                _params['authentication_token'] = authentication_token
            if principal_id is not ShapeBase.NOT_SET:
                _params['principal_id'] = principal_id
            if limit is not ShapeBase.NOT_SET:
                _params['limit'] = limit
            if marker is not ShapeBase.NOT_SET:
                _params['marker'] = marker
            _request = shapes.DescribeResourcePermissionsRequest(**_params)
        response = self._boto_client.describe_resource_permissions(
            **_request.to_boto()
        )

        return shapes.DescribeResourcePermissionsResponse.from_boto(response)

    def describe_root_folders(
        self,
        _request: shapes.DescribeRootFoldersRequest = None,
        *,
        authentication_token: str,
        limit: int = ShapeBase.NOT_SET,
        marker: str = ShapeBase.NOT_SET,
    ) -> shapes.DescribeRootFoldersResponse:
        """
        Describes the current user's special folders; the `RootFolder` and the
        `RecycleBin`. `RootFolder` is the root of user's files and folders and
        `RecycleBin` is the root of recycled items. This is not a valid action for SigV4
        (administrative API) clients.
        """
        if _request is None:
            _params = {}
            if authentication_token is not ShapeBase.NOT_SET:
                _params['authentication_token'] = authentication_token
            if limit is not ShapeBase.NOT_SET:
                _params['limit'] = limit
            if marker is not ShapeBase.NOT_SET:
                _params['marker'] = marker
            _request = shapes.DescribeRootFoldersRequest(**_params)
        response = self._boto_client.describe_root_folders(**_request.to_boto())

        return shapes.DescribeRootFoldersResponse.from_boto(response)

    def describe_users(
        self,
        _request: shapes.DescribeUsersRequest = None,
        *,
        authentication_token: str = ShapeBase.NOT_SET,
        organization_id: str = ShapeBase.NOT_SET,
        user_ids: str = ShapeBase.NOT_SET,
        query: str = ShapeBase.NOT_SET,
        include: typing.Union[str, shapes.UserFilterType] = ShapeBase.NOT_SET,
        order: typing.Union[str, shapes.OrderType] = ShapeBase.NOT_SET,
        sort: typing.Union[str, shapes.UserSortType] = ShapeBase.NOT_SET,
        marker: str = ShapeBase.NOT_SET,
        limit: int = ShapeBase.NOT_SET,
        fields: str = ShapeBase.NOT_SET,
    ) -> shapes.DescribeUsersResponse:
        """
        Describes the specified users. You can describe all users or filter the results
        (for example, by status or organization).

        By default, Amazon WorkDocs returns the first 24 active or pending users. If
        there are more results, the response includes a marker that you can use to
        request the next set of results.
        """
        if _request is None:
            _params = {}
            if authentication_token is not ShapeBase.NOT_SET:
                _params['authentication_token'] = authentication_token
            if organization_id is not ShapeBase.NOT_SET:
                _params['organization_id'] = organization_id
            if user_ids is not ShapeBase.NOT_SET:
                _params['user_ids'] = user_ids
            if query is not ShapeBase.NOT_SET:
                _params['query'] = query
            if include is not ShapeBase.NOT_SET:
                _params['include'] = include
            if order is not ShapeBase.NOT_SET:
                _params['order'] = order
            if sort is not ShapeBase.NOT_SET:
                _params['sort'] = sort
            if marker is not ShapeBase.NOT_SET:
                _params['marker'] = marker
            if limit is not ShapeBase.NOT_SET:
                _params['limit'] = limit
            if fields is not ShapeBase.NOT_SET:
                _params['fields'] = fields
            _request = shapes.DescribeUsersRequest(**_params)
        paginator = self.get_paginator("describe_users").paginate(
            **_request.to_boto()
        )
        page_generator = (page for page in paginator)
        first_page = next(page_generator)
        result = shapes.DescribeUsersResponse.from_boto(first_page)
        result._page_iterator = page_generator
        return result

        return shapes.DescribeUsersResponse.from_boto(response)

    def get_current_user(
        self,
        _request: shapes.GetCurrentUserRequest = None,
        *,
        authentication_token: str,
    ) -> shapes.GetCurrentUserResponse:
        """
        Retrieves details of the current user for whom the authentication token was
        generated. This is not a valid action for SigV4 (administrative API) clients.
        """
        if _request is None:
            _params = {}
            if authentication_token is not ShapeBase.NOT_SET:
                _params['authentication_token'] = authentication_token
            _request = shapes.GetCurrentUserRequest(**_params)
        response = self._boto_client.get_current_user(**_request.to_boto())

        return shapes.GetCurrentUserResponse.from_boto(response)

    def get_document(
        self,
        _request: shapes.GetDocumentRequest = None,
        *,
        document_id: str,
        authentication_token: str = ShapeBase.NOT_SET,
        include_custom_metadata: bool = ShapeBase.NOT_SET,
    ) -> shapes.GetDocumentResponse:
        """
        Retrieves details of a document.
        """
        if _request is None:
            _params = {}
            if document_id is not ShapeBase.NOT_SET:
                _params['document_id'] = document_id
            if authentication_token is not ShapeBase.NOT_SET:
                _params['authentication_token'] = authentication_token
            if include_custom_metadata is not ShapeBase.NOT_SET:
                _params['include_custom_metadata'] = include_custom_metadata
            _request = shapes.GetDocumentRequest(**_params)
        response = self._boto_client.get_document(**_request.to_boto())

        return shapes.GetDocumentResponse.from_boto(response)

    def get_document_path(
        self,
        _request: shapes.GetDocumentPathRequest = None,
        *,
        document_id: str,
        authentication_token: str = ShapeBase.NOT_SET,
        limit: int = ShapeBase.NOT_SET,
        fields: str = ShapeBase.NOT_SET,
        marker: str = ShapeBase.NOT_SET,
    ) -> shapes.GetDocumentPathResponse:
        """
        Retrieves the path information (the hierarchy from the root folder) for the
        requested document.

        By default, Amazon WorkDocs returns a maximum of 100 levels upwards from the
        requested document and only includes the IDs of the parent folders in the path.
        You can limit the maximum number of levels. You can also request the names of
        the parent folders.
        """
        if _request is None:
            _params = {}
            if document_id is not ShapeBase.NOT_SET:
                _params['document_id'] = document_id
            if authentication_token is not ShapeBase.NOT_SET:
                _params['authentication_token'] = authentication_token
            if limit is not ShapeBase.NOT_SET:
                _params['limit'] = limit
            if fields is not ShapeBase.NOT_SET:
                _params['fields'] = fields
            if marker is not ShapeBase.NOT_SET:
                _params['marker'] = marker
            _request = shapes.GetDocumentPathRequest(**_params)
        response = self._boto_client.get_document_path(**_request.to_boto())

        return shapes.GetDocumentPathResponse.from_boto(response)

    def get_document_version(
        self,
        _request: shapes.GetDocumentVersionRequest = None,
        *,
        document_id: str,
        version_id: str,
        authentication_token: str = ShapeBase.NOT_SET,
        fields: str = ShapeBase.NOT_SET,
        include_custom_metadata: bool = ShapeBase.NOT_SET,
    ) -> shapes.GetDocumentVersionResponse:
        """
        Retrieves version metadata for the specified document.
        """
        if _request is None:
            _params = {}
            if document_id is not ShapeBase.NOT_SET:
                _params['document_id'] = document_id
            if version_id is not ShapeBase.NOT_SET:
                _params['version_id'] = version_id
            if authentication_token is not ShapeBase.NOT_SET:
                _params['authentication_token'] = authentication_token
            if fields is not ShapeBase.NOT_SET:
                _params['fields'] = fields
            if include_custom_metadata is not ShapeBase.NOT_SET:
                _params['include_custom_metadata'] = include_custom_metadata
            _request = shapes.GetDocumentVersionRequest(**_params)
        response = self._boto_client.get_document_version(**_request.to_boto())

        return shapes.GetDocumentVersionResponse.from_boto(response)

    def get_folder(
        self,
        _request: shapes.GetFolderRequest = None,
        *,
        folder_id: str,
        authentication_token: str = ShapeBase.NOT_SET,
        include_custom_metadata: bool = ShapeBase.NOT_SET,
    ) -> shapes.GetFolderResponse:
        """
        Retrieves the metadata of the specified folder.
        """
        if _request is None:
            _params = {}
            if folder_id is not ShapeBase.NOT_SET:
                _params['folder_id'] = folder_id
            if authentication_token is not ShapeBase.NOT_SET:
                _params['authentication_token'] = authentication_token
            if include_custom_metadata is not ShapeBase.NOT_SET:
                _params['include_custom_metadata'] = include_custom_metadata
            _request = shapes.GetFolderRequest(**_params)
        response = self._boto_client.get_folder(**_request.to_boto())

        return shapes.GetFolderResponse.from_boto(response)

    def get_folder_path(
        self,
        _request: shapes.GetFolderPathRequest = None,
        *,
        folder_id: str,
        authentication_token: str = ShapeBase.NOT_SET,
        limit: int = ShapeBase.NOT_SET,
        fields: str = ShapeBase.NOT_SET,
        marker: str = ShapeBase.NOT_SET,
    ) -> shapes.GetFolderPathResponse:
        """
        Retrieves the path information (the hierarchy from the root folder) for the
        specified folder.

        By default, Amazon WorkDocs returns a maximum of 100 levels upwards from the
        requested folder and only includes the IDs of the parent folders in the path.
        You can limit the maximum number of levels. You can also request the parent
        folder names.
        """
        if _request is None:
            _params = {}
            if folder_id is not ShapeBase.NOT_SET:
                _params['folder_id'] = folder_id
            if authentication_token is not ShapeBase.NOT_SET:
                _params['authentication_token'] = authentication_token
            if limit is not ShapeBase.NOT_SET:
                _params['limit'] = limit
            if fields is not ShapeBase.NOT_SET:
                _params['fields'] = fields
            if marker is not ShapeBase.NOT_SET:
                _params['marker'] = marker
            _request = shapes.GetFolderPathRequest(**_params)
        response = self._boto_client.get_folder_path(**_request.to_boto())

        return shapes.GetFolderPathResponse.from_boto(response)

    def initiate_document_version_upload(
        self,
        _request: shapes.InitiateDocumentVersionUploadRequest = None,
        *,
        parent_folder_id: str,
        authentication_token: str = ShapeBase.NOT_SET,
        id: str = ShapeBase.NOT_SET,
        name: str = ShapeBase.NOT_SET,
        content_created_timestamp: datetime.datetime = ShapeBase.NOT_SET,
        content_modified_timestamp: datetime.datetime = ShapeBase.NOT_SET,
        content_type: str = ShapeBase.NOT_SET,
        document_size_in_bytes: int = ShapeBase.NOT_SET,
    ) -> shapes.InitiateDocumentVersionUploadResponse:
        """
        Creates a new document object and version object.

        The client specifies the parent folder ID and name of the document to upload.
        The ID is optionally specified when creating a new version of an existing
        document. This is the first step to upload a document. Next, upload the document
        to the URL returned from the call, and then call UpdateDocumentVersion.

        To cancel the document upload, call AbortDocumentVersionUpload.
        """
        if _request is None:
            _params = {}
            if parent_folder_id is not ShapeBase.NOT_SET:
                _params['parent_folder_id'] = parent_folder_id
            if authentication_token is not ShapeBase.NOT_SET:
                _params['authentication_token'] = authentication_token
            if id is not ShapeBase.NOT_SET:
                _params['id'] = id
            if name is not ShapeBase.NOT_SET:
                _params['name'] = name
            if content_created_timestamp is not ShapeBase.NOT_SET:
                _params['content_created_timestamp'] = content_created_timestamp
            if content_modified_timestamp is not ShapeBase.NOT_SET:
                _params['content_modified_timestamp'
                       ] = content_modified_timestamp
            if content_type is not ShapeBase.NOT_SET:
                _params['content_type'] = content_type
            if document_size_in_bytes is not ShapeBase.NOT_SET:
                _params['document_size_in_bytes'] = document_size_in_bytes
            _request = shapes.InitiateDocumentVersionUploadRequest(**_params)
        response = self._boto_client.initiate_document_version_upload(
            **_request.to_boto()
        )

        return shapes.InitiateDocumentVersionUploadResponse.from_boto(response)

    def remove_all_resource_permissions(
        self,
        _request: shapes.RemoveAllResourcePermissionsRequest = None,
        *,
        resource_id: str,
        authentication_token: str = ShapeBase.NOT_SET,
    ) -> None:
        """
        Removes all the permissions from the specified resource.
        """
        if _request is None:
            _params = {}
            if resource_id is not ShapeBase.NOT_SET:
                _params['resource_id'] = resource_id
            if authentication_token is not ShapeBase.NOT_SET:
                _params['authentication_token'] = authentication_token
            _request = shapes.RemoveAllResourcePermissionsRequest(**_params)
        response = self._boto_client.remove_all_resource_permissions(
            **_request.to_boto()
        )

    def remove_resource_permission(
        self,
        _request: shapes.RemoveResourcePermissionRequest = None,
        *,
        resource_id: str,
        principal_id: str,
        authentication_token: str = ShapeBase.NOT_SET,
        principal_type: typing.Union[str, shapes.PrincipalType] = ShapeBase.
        NOT_SET,
    ) -> None:
        """
        Removes the permission for the specified principal from the specified resource.
        """
        if _request is None:
            _params = {}
            if resource_id is not ShapeBase.NOT_SET:
                _params['resource_id'] = resource_id
            if principal_id is not ShapeBase.NOT_SET:
                _params['principal_id'] = principal_id
            if authentication_token is not ShapeBase.NOT_SET:
                _params['authentication_token'] = authentication_token
            if principal_type is not ShapeBase.NOT_SET:
                _params['principal_type'] = principal_type
            _request = shapes.RemoveResourcePermissionRequest(**_params)
        response = self._boto_client.remove_resource_permission(
            **_request.to_boto()
        )

    def update_document(
        self,
        _request: shapes.UpdateDocumentRequest = None,
        *,
        document_id: str,
        authentication_token: str = ShapeBase.NOT_SET,
        name: str = ShapeBase.NOT_SET,
        parent_folder_id: str = ShapeBase.NOT_SET,
        resource_state: typing.Union[str, shapes.ResourceStateType] = ShapeBase.
        NOT_SET,
    ) -> None:
        """
        Updates the specified attributes of a document. The user must have access to
        both the document and its parent folder, if applicable.
        """
        if _request is None:
            _params = {}
            if document_id is not ShapeBase.NOT_SET:
                _params['document_id'] = document_id
            if authentication_token is not ShapeBase.NOT_SET:
                _params['authentication_token'] = authentication_token
            if name is not ShapeBase.NOT_SET:
                _params['name'] = name
            if parent_folder_id is not ShapeBase.NOT_SET:
                _params['parent_folder_id'] = parent_folder_id
            if resource_state is not ShapeBase.NOT_SET:
                _params['resource_state'] = resource_state
            _request = shapes.UpdateDocumentRequest(**_params)
        response = self._boto_client.update_document(**_request.to_boto())

    def update_document_version(
        self,
        _request: shapes.UpdateDocumentVersionRequest = None,
        *,
        document_id: str,
        version_id: str,
        authentication_token: str = ShapeBase.NOT_SET,
        version_status: typing.Union[str, shapes.
                                     DocumentVersionStatus] = ShapeBase.NOT_SET,
    ) -> None:
        """
        Changes the status of the document version to ACTIVE.

        Amazon WorkDocs also sets its document container to ACTIVE. This is the last
        step in a document upload, after the client uploads the document to an
        S3-presigned URL returned by InitiateDocumentVersionUpload.
        """
        if _request is None:
            _params = {}
            if document_id is not ShapeBase.NOT_SET:
                _params['document_id'] = document_id
            if version_id is not ShapeBase.NOT_SET:
                _params['version_id'] = version_id
            if authentication_token is not ShapeBase.NOT_SET:
                _params['authentication_token'] = authentication_token
            if version_status is not ShapeBase.NOT_SET:
                _params['version_status'] = version_status
            _request = shapes.UpdateDocumentVersionRequest(**_params)
        response = self._boto_client.update_document_version(
            **_request.to_boto()
        )

    def update_folder(
        self,
        _request: shapes.UpdateFolderRequest = None,
        *,
        folder_id: str,
        authentication_token: str = ShapeBase.NOT_SET,
        name: str = ShapeBase.NOT_SET,
        parent_folder_id: str = ShapeBase.NOT_SET,
        resource_state: typing.Union[str, shapes.ResourceStateType] = ShapeBase.
        NOT_SET,
    ) -> None:
        """
        Updates the specified attributes of the specified folder. The user must have
        access to both the folder and its parent folder, if applicable.
        """
        if _request is None:
            _params = {}
            if folder_id is not ShapeBase.NOT_SET:
                _params['folder_id'] = folder_id
            if authentication_token is not ShapeBase.NOT_SET:
                _params['authentication_token'] = authentication_token
            if name is not ShapeBase.NOT_SET:
                _params['name'] = name
            if parent_folder_id is not ShapeBase.NOT_SET:
                _params['parent_folder_id'] = parent_folder_id
            if resource_state is not ShapeBase.NOT_SET:
                _params['resource_state'] = resource_state
            _request = shapes.UpdateFolderRequest(**_params)
        response = self._boto_client.update_folder(**_request.to_boto())

    def update_user(
        self,
        _request: shapes.UpdateUserRequest = None,
        *,
        user_id: str,
        authentication_token: str = ShapeBase.NOT_SET,
        given_name: str = ShapeBase.NOT_SET,
        surname: str = ShapeBase.NOT_SET,
        type: typing.Union[str, shapes.UserType] = ShapeBase.NOT_SET,
        storage_rule: shapes.StorageRuleType = ShapeBase.NOT_SET,
        time_zone_id: str = ShapeBase.NOT_SET,
        locale: typing.Union[str, shapes.LocaleType] = ShapeBase.NOT_SET,
        grant_poweruser_privileges: typing.
        Union[str, shapes.BooleanEnumType] = ShapeBase.NOT_SET,
    ) -> shapes.UpdateUserResponse:
        """
        Updates the specified attributes of the specified user, and grants or revokes
        administrative privileges to the Amazon WorkDocs site.
        """
        if _request is None:
            _params = {}
            if user_id is not ShapeBase.NOT_SET:
                _params['user_id'] = user_id
            if authentication_token is not ShapeBase.NOT_SET:
                _params['authentication_token'] = authentication_token
            if given_name is not ShapeBase.NOT_SET:
                _params['given_name'] = given_name
            if surname is not ShapeBase.NOT_SET:
                _params['surname'] = surname
            if type is not ShapeBase.NOT_SET:
                _params['type'] = type
            if storage_rule is not ShapeBase.NOT_SET:
                _params['storage_rule'] = storage_rule
            if time_zone_id is not ShapeBase.NOT_SET:
                _params['time_zone_id'] = time_zone_id
            if locale is not ShapeBase.NOT_SET:
                _params['locale'] = locale
            if grant_poweruser_privileges is not ShapeBase.NOT_SET:
                _params['grant_poweruser_privileges'
                       ] = grant_poweruser_privileges
            _request = shapes.UpdateUserRequest(**_params)
        response = self._boto_client.update_user(**_request.to_boto())

        return shapes.UpdateUserResponse.from_boto(response)
