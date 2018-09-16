import datetime
import typing
import boto3
from autoboto import ClientBase, ShapeBase, OutputShapeBase
from . import shapes


class Client(ClientBase):
    def __init__(self, *args, **kwargs):
        super().__init__("workmail", *args, **kwargs)

    def associate_delegate_to_resource(
        self,
        _request: shapes.AssociateDelegateToResourceRequest = None,
        *,
        organization_id: str,
        resource_id: str,
        entity_id: str,
    ) -> shapes.AssociateDelegateToResourceResponse:
        """
        Adds a member to the resource's set of delegates.
        """
        if _request is None:
            _params = {}
            if organization_id is not ShapeBase.NOT_SET:
                _params['organization_id'] = organization_id
            if resource_id is not ShapeBase.NOT_SET:
                _params['resource_id'] = resource_id
            if entity_id is not ShapeBase.NOT_SET:
                _params['entity_id'] = entity_id
            _request = shapes.AssociateDelegateToResourceRequest(**_params)
        response = self._boto_client.associate_delegate_to_resource(
            **_request.to_boto()
        )

        return shapes.AssociateDelegateToResourceResponse.from_boto(response)

    def associate_member_to_group(
        self,
        _request: shapes.AssociateMemberToGroupRequest = None,
        *,
        organization_id: str,
        group_id: str,
        member_id: str,
    ) -> shapes.AssociateMemberToGroupResponse:
        """
        Adds a member to the group's set.
        """
        if _request is None:
            _params = {}
            if organization_id is not ShapeBase.NOT_SET:
                _params['organization_id'] = organization_id
            if group_id is not ShapeBase.NOT_SET:
                _params['group_id'] = group_id
            if member_id is not ShapeBase.NOT_SET:
                _params['member_id'] = member_id
            _request = shapes.AssociateMemberToGroupRequest(**_params)
        response = self._boto_client.associate_member_to_group(
            **_request.to_boto()
        )

        return shapes.AssociateMemberToGroupResponse.from_boto(response)

    def create_alias(
        self,
        _request: shapes.CreateAliasRequest = None,
        *,
        organization_id: str,
        entity_id: str,
        alias: str,
    ) -> shapes.CreateAliasResponse:
        """
        Adds an alias to the set of a given member of Amazon WorkMail.
        """
        if _request is None:
            _params = {}
            if organization_id is not ShapeBase.NOT_SET:
                _params['organization_id'] = organization_id
            if entity_id is not ShapeBase.NOT_SET:
                _params['entity_id'] = entity_id
            if alias is not ShapeBase.NOT_SET:
                _params['alias'] = alias
            _request = shapes.CreateAliasRequest(**_params)
        response = self._boto_client.create_alias(**_request.to_boto())

        return shapes.CreateAliasResponse.from_boto(response)

    def create_group(
        self,
        _request: shapes.CreateGroupRequest = None,
        *,
        organization_id: str,
        name: str,
    ) -> shapes.CreateGroupResponse:
        """
        Creates a group that can be used in Amazon WorkMail by calling the
        RegisterToWorkMail operation.
        """
        if _request is None:
            _params = {}
            if organization_id is not ShapeBase.NOT_SET:
                _params['organization_id'] = organization_id
            if name is not ShapeBase.NOT_SET:
                _params['name'] = name
            _request = shapes.CreateGroupRequest(**_params)
        response = self._boto_client.create_group(**_request.to_boto())

        return shapes.CreateGroupResponse.from_boto(response)

    def create_resource(
        self,
        _request: shapes.CreateResourceRequest = None,
        *,
        organization_id: str,
        name: str,
        type: typing.Union[str, shapes.ResourceType],
    ) -> shapes.CreateResourceResponse:
        """
        Creates a new Amazon WorkMail resource. The available types are equipment and
        room.
        """
        if _request is None:
            _params = {}
            if organization_id is not ShapeBase.NOT_SET:
                _params['organization_id'] = organization_id
            if name is not ShapeBase.NOT_SET:
                _params['name'] = name
            if type is not ShapeBase.NOT_SET:
                _params['type'] = type
            _request = shapes.CreateResourceRequest(**_params)
        response = self._boto_client.create_resource(**_request.to_boto())

        return shapes.CreateResourceResponse.from_boto(response)

    def create_user(
        self,
        _request: shapes.CreateUserRequest = None,
        *,
        organization_id: str,
        name: str,
        display_name: str,
        password: str,
    ) -> shapes.CreateUserResponse:
        """
        Creates a user who can be used in Amazon WorkMail by calling the
        RegisterToWorkMail operation.
        """
        if _request is None:
            _params = {}
            if organization_id is not ShapeBase.NOT_SET:
                _params['organization_id'] = organization_id
            if name is not ShapeBase.NOT_SET:
                _params['name'] = name
            if display_name is not ShapeBase.NOT_SET:
                _params['display_name'] = display_name
            if password is not ShapeBase.NOT_SET:
                _params['password'] = password
            _request = shapes.CreateUserRequest(**_params)
        response = self._boto_client.create_user(**_request.to_boto())

        return shapes.CreateUserResponse.from_boto(response)

    def delete_alias(
        self,
        _request: shapes.DeleteAliasRequest = None,
        *,
        organization_id: str,
        entity_id: str,
        alias: str,
    ) -> shapes.DeleteAliasResponse:
        """
        Remove the alias from a set of aliases for a given user.
        """
        if _request is None:
            _params = {}
            if organization_id is not ShapeBase.NOT_SET:
                _params['organization_id'] = organization_id
            if entity_id is not ShapeBase.NOT_SET:
                _params['entity_id'] = entity_id
            if alias is not ShapeBase.NOT_SET:
                _params['alias'] = alias
            _request = shapes.DeleteAliasRequest(**_params)
        response = self._boto_client.delete_alias(**_request.to_boto())

        return shapes.DeleteAliasResponse.from_boto(response)

    def delete_group(
        self,
        _request: shapes.DeleteGroupRequest = None,
        *,
        organization_id: str,
        group_id: str,
    ) -> shapes.DeleteGroupResponse:
        """
        Deletes a group from Amazon WorkMail.
        """
        if _request is None:
            _params = {}
            if organization_id is not ShapeBase.NOT_SET:
                _params['organization_id'] = organization_id
            if group_id is not ShapeBase.NOT_SET:
                _params['group_id'] = group_id
            _request = shapes.DeleteGroupRequest(**_params)
        response = self._boto_client.delete_group(**_request.to_boto())

        return shapes.DeleteGroupResponse.from_boto(response)

    def delete_mailbox_permissions(
        self,
        _request: shapes.DeleteMailboxPermissionsRequest = None,
        *,
        organization_id: str,
        entity_id: str,
        grantee_id: str,
    ) -> shapes.DeleteMailboxPermissionsResponse:
        """
        Deletes permissions granted to a user or group.
        """
        if _request is None:
            _params = {}
            if organization_id is not ShapeBase.NOT_SET:
                _params['organization_id'] = organization_id
            if entity_id is not ShapeBase.NOT_SET:
                _params['entity_id'] = entity_id
            if grantee_id is not ShapeBase.NOT_SET:
                _params['grantee_id'] = grantee_id
            _request = shapes.DeleteMailboxPermissionsRequest(**_params)
        response = self._boto_client.delete_mailbox_permissions(
            **_request.to_boto()
        )

        return shapes.DeleteMailboxPermissionsResponse.from_boto(response)

    def delete_resource(
        self,
        _request: shapes.DeleteResourceRequest = None,
        *,
        organization_id: str,
        resource_id: str,
    ) -> shapes.DeleteResourceResponse:
        """
        Deletes the specified resource.
        """
        if _request is None:
            _params = {}
            if organization_id is not ShapeBase.NOT_SET:
                _params['organization_id'] = organization_id
            if resource_id is not ShapeBase.NOT_SET:
                _params['resource_id'] = resource_id
            _request = shapes.DeleteResourceRequest(**_params)
        response = self._boto_client.delete_resource(**_request.to_boto())

        return shapes.DeleteResourceResponse.from_boto(response)

    def delete_user(
        self,
        _request: shapes.DeleteUserRequest = None,
        *,
        organization_id: str,
        user_id: str,
    ) -> shapes.DeleteUserResponse:
        """
        Deletes a user from Amazon WorkMail and all subsequent systems. The action can't
        be undone. The mailbox is kept as-is for a minimum of 30 days, without any means
        to restore it.
        """
        if _request is None:
            _params = {}
            if organization_id is not ShapeBase.NOT_SET:
                _params['organization_id'] = organization_id
            if user_id is not ShapeBase.NOT_SET:
                _params['user_id'] = user_id
            _request = shapes.DeleteUserRequest(**_params)
        response = self._boto_client.delete_user(**_request.to_boto())

        return shapes.DeleteUserResponse.from_boto(response)

    def deregister_from_work_mail(
        self,
        _request: shapes.DeregisterFromWorkMailRequest = None,
        *,
        organization_id: str,
        entity_id: str,
    ) -> shapes.DeregisterFromWorkMailResponse:
        """
        Mark a user, group, or resource as no longer used in Amazon WorkMail. This
        action disassociates the mailbox and schedules it for clean-up. Amazon WorkMail
        keeps mailboxes for 30 days before they are permanently removed. The
        functionality in the console is _Disable_.
        """
        if _request is None:
            _params = {}
            if organization_id is not ShapeBase.NOT_SET:
                _params['organization_id'] = organization_id
            if entity_id is not ShapeBase.NOT_SET:
                _params['entity_id'] = entity_id
            _request = shapes.DeregisterFromWorkMailRequest(**_params)
        response = self._boto_client.deregister_from_work_mail(
            **_request.to_boto()
        )

        return shapes.DeregisterFromWorkMailResponse.from_boto(response)

    def describe_group(
        self,
        _request: shapes.DescribeGroupRequest = None,
        *,
        organization_id: str,
        group_id: str,
    ) -> shapes.DescribeGroupResponse:
        """
        Returns the data available for the group.
        """
        if _request is None:
            _params = {}
            if organization_id is not ShapeBase.NOT_SET:
                _params['organization_id'] = organization_id
            if group_id is not ShapeBase.NOT_SET:
                _params['group_id'] = group_id
            _request = shapes.DescribeGroupRequest(**_params)
        response = self._boto_client.describe_group(**_request.to_boto())

        return shapes.DescribeGroupResponse.from_boto(response)

    def describe_organization(
        self,
        _request: shapes.DescribeOrganizationRequest = None,
        *,
        organization_id: str,
    ) -> shapes.DescribeOrganizationResponse:
        """
        Provides more information regarding a given organization based on its
        identifier.
        """
        if _request is None:
            _params = {}
            if organization_id is not ShapeBase.NOT_SET:
                _params['organization_id'] = organization_id
            _request = shapes.DescribeOrganizationRequest(**_params)
        response = self._boto_client.describe_organization(**_request.to_boto())

        return shapes.DescribeOrganizationResponse.from_boto(response)

    def describe_resource(
        self,
        _request: shapes.DescribeResourceRequest = None,
        *,
        organization_id: str,
        resource_id: str,
    ) -> shapes.DescribeResourceResponse:
        """
        Returns the data available for the resource.
        """
        if _request is None:
            _params = {}
            if organization_id is not ShapeBase.NOT_SET:
                _params['organization_id'] = organization_id
            if resource_id is not ShapeBase.NOT_SET:
                _params['resource_id'] = resource_id
            _request = shapes.DescribeResourceRequest(**_params)
        response = self._boto_client.describe_resource(**_request.to_boto())

        return shapes.DescribeResourceResponse.from_boto(response)

    def describe_user(
        self,
        _request: shapes.DescribeUserRequest = None,
        *,
        organization_id: str,
        user_id: str,
    ) -> shapes.DescribeUserResponse:
        """
        Provides information regarding the user.
        """
        if _request is None:
            _params = {}
            if organization_id is not ShapeBase.NOT_SET:
                _params['organization_id'] = organization_id
            if user_id is not ShapeBase.NOT_SET:
                _params['user_id'] = user_id
            _request = shapes.DescribeUserRequest(**_params)
        response = self._boto_client.describe_user(**_request.to_boto())

        return shapes.DescribeUserResponse.from_boto(response)

    def disassociate_delegate_from_resource(
        self,
        _request: shapes.DisassociateDelegateFromResourceRequest = None,
        *,
        organization_id: str,
        resource_id: str,
        entity_id: str,
    ) -> shapes.DisassociateDelegateFromResourceResponse:
        """
        Removes a member from the resource's set of delegates.
        """
        if _request is None:
            _params = {}
            if organization_id is not ShapeBase.NOT_SET:
                _params['organization_id'] = organization_id
            if resource_id is not ShapeBase.NOT_SET:
                _params['resource_id'] = resource_id
            if entity_id is not ShapeBase.NOT_SET:
                _params['entity_id'] = entity_id
            _request = shapes.DisassociateDelegateFromResourceRequest(**_params)
        response = self._boto_client.disassociate_delegate_from_resource(
            **_request.to_boto()
        )

        return shapes.DisassociateDelegateFromResourceResponse.from_boto(
            response
        )

    def disassociate_member_from_group(
        self,
        _request: shapes.DisassociateMemberFromGroupRequest = None,
        *,
        organization_id: str,
        group_id: str,
        member_id: str,
    ) -> shapes.DisassociateMemberFromGroupResponse:
        """
        Removes a member from a group.
        """
        if _request is None:
            _params = {}
            if organization_id is not ShapeBase.NOT_SET:
                _params['organization_id'] = organization_id
            if group_id is not ShapeBase.NOT_SET:
                _params['group_id'] = group_id
            if member_id is not ShapeBase.NOT_SET:
                _params['member_id'] = member_id
            _request = shapes.DisassociateMemberFromGroupRequest(**_params)
        response = self._boto_client.disassociate_member_from_group(
            **_request.to_boto()
        )

        return shapes.DisassociateMemberFromGroupResponse.from_boto(response)

    def list_aliases(
        self,
        _request: shapes.ListAliasesRequest = None,
        *,
        organization_id: str,
        entity_id: str,
        next_token: str = ShapeBase.NOT_SET,
        max_results: int = ShapeBase.NOT_SET,
    ) -> shapes.ListAliasesResponse:
        """
        Creates a paginated call to list the aliases associated with a given entity.
        """
        if _request is None:
            _params = {}
            if organization_id is not ShapeBase.NOT_SET:
                _params['organization_id'] = organization_id
            if entity_id is not ShapeBase.NOT_SET:
                _params['entity_id'] = entity_id
            if next_token is not ShapeBase.NOT_SET:
                _params['next_token'] = next_token
            if max_results is not ShapeBase.NOT_SET:
                _params['max_results'] = max_results
            _request = shapes.ListAliasesRequest(**_params)
        paginator = self.get_paginator("list_aliases").paginate(
            **_request.to_boto()
        )
        page_generator = (page for page in paginator)
        first_page = next(page_generator)
        result = shapes.ListAliasesResponse.from_boto(first_page)
        result._page_iterator = page_generator
        return result

        return shapes.ListAliasesResponse.from_boto(response)

    def list_group_members(
        self,
        _request: shapes.ListGroupMembersRequest = None,
        *,
        organization_id: str,
        group_id: str,
        next_token: str = ShapeBase.NOT_SET,
        max_results: int = ShapeBase.NOT_SET,
    ) -> shapes.ListGroupMembersResponse:
        """
        Returns an overview of the members of a group.
        """
        if _request is None:
            _params = {}
            if organization_id is not ShapeBase.NOT_SET:
                _params['organization_id'] = organization_id
            if group_id is not ShapeBase.NOT_SET:
                _params['group_id'] = group_id
            if next_token is not ShapeBase.NOT_SET:
                _params['next_token'] = next_token
            if max_results is not ShapeBase.NOT_SET:
                _params['max_results'] = max_results
            _request = shapes.ListGroupMembersRequest(**_params)
        paginator = self.get_paginator("list_group_members").paginate(
            **_request.to_boto()
        )
        page_generator = (page for page in paginator)
        first_page = next(page_generator)
        result = shapes.ListGroupMembersResponse.from_boto(first_page)
        result._page_iterator = page_generator
        return result

        return shapes.ListGroupMembersResponse.from_boto(response)

    def list_groups(
        self,
        _request: shapes.ListGroupsRequest = None,
        *,
        organization_id: str,
        next_token: str = ShapeBase.NOT_SET,
        max_results: int = ShapeBase.NOT_SET,
    ) -> shapes.ListGroupsResponse:
        """
        Returns summaries of the organization's groups.
        """
        if _request is None:
            _params = {}
            if organization_id is not ShapeBase.NOT_SET:
                _params['organization_id'] = organization_id
            if next_token is not ShapeBase.NOT_SET:
                _params['next_token'] = next_token
            if max_results is not ShapeBase.NOT_SET:
                _params['max_results'] = max_results
            _request = shapes.ListGroupsRequest(**_params)
        paginator = self.get_paginator("list_groups").paginate(
            **_request.to_boto()
        )
        page_generator = (page for page in paginator)
        first_page = next(page_generator)
        result = shapes.ListGroupsResponse.from_boto(first_page)
        result._page_iterator = page_generator
        return result

        return shapes.ListGroupsResponse.from_boto(response)

    def list_mailbox_permissions(
        self,
        _request: shapes.ListMailboxPermissionsRequest = None,
        *,
        organization_id: str,
        entity_id: str,
        next_token: str = ShapeBase.NOT_SET,
        max_results: int = ShapeBase.NOT_SET,
    ) -> shapes.ListMailboxPermissionsResponse:
        """
        Lists the mailbox permissions associated with a mailbox.
        """
        if _request is None:
            _params = {}
            if organization_id is not ShapeBase.NOT_SET:
                _params['organization_id'] = organization_id
            if entity_id is not ShapeBase.NOT_SET:
                _params['entity_id'] = entity_id
            if next_token is not ShapeBase.NOT_SET:
                _params['next_token'] = next_token
            if max_results is not ShapeBase.NOT_SET:
                _params['max_results'] = max_results
            _request = shapes.ListMailboxPermissionsRequest(**_params)
        response = self._boto_client.list_mailbox_permissions(
            **_request.to_boto()
        )

        return shapes.ListMailboxPermissionsResponse.from_boto(response)

    def list_organizations(
        self,
        _request: shapes.ListOrganizationsRequest = None,
        *,
        next_token: str = ShapeBase.NOT_SET,
        max_results: int = ShapeBase.NOT_SET,
    ) -> shapes.ListOrganizationsResponse:
        """
        Returns summaries of the customer's non-deleted organizations.
        """
        if _request is None:
            _params = {}
            if next_token is not ShapeBase.NOT_SET:
                _params['next_token'] = next_token
            if max_results is not ShapeBase.NOT_SET:
                _params['max_results'] = max_results
            _request = shapes.ListOrganizationsRequest(**_params)
        paginator = self.get_paginator("list_organizations").paginate(
            **_request.to_boto()
        )
        page_generator = (page for page in paginator)
        first_page = next(page_generator)
        result = shapes.ListOrganizationsResponse.from_boto(first_page)
        result._page_iterator = page_generator
        return result

        return shapes.ListOrganizationsResponse.from_boto(response)

    def list_resource_delegates(
        self,
        _request: shapes.ListResourceDelegatesRequest = None,
        *,
        organization_id: str,
        resource_id: str,
        next_token: str = ShapeBase.NOT_SET,
        max_results: int = ShapeBase.NOT_SET,
    ) -> shapes.ListResourceDelegatesResponse:
        """
        Lists the delegates associated with a resource. Users and groups can be resource
        delegates and answer requests on behalf of the resource.
        """
        if _request is None:
            _params = {}
            if organization_id is not ShapeBase.NOT_SET:
                _params['organization_id'] = organization_id
            if resource_id is not ShapeBase.NOT_SET:
                _params['resource_id'] = resource_id
            if next_token is not ShapeBase.NOT_SET:
                _params['next_token'] = next_token
            if max_results is not ShapeBase.NOT_SET:
                _params['max_results'] = max_results
            _request = shapes.ListResourceDelegatesRequest(**_params)
        response = self._boto_client.list_resource_delegates(
            **_request.to_boto()
        )

        return shapes.ListResourceDelegatesResponse.from_boto(response)

    def list_resources(
        self,
        _request: shapes.ListResourcesRequest = None,
        *,
        organization_id: str,
        next_token: str = ShapeBase.NOT_SET,
        max_results: int = ShapeBase.NOT_SET,
    ) -> shapes.ListResourcesResponse:
        """
        Returns summaries of the organization's resources.
        """
        if _request is None:
            _params = {}
            if organization_id is not ShapeBase.NOT_SET:
                _params['organization_id'] = organization_id
            if next_token is not ShapeBase.NOT_SET:
                _params['next_token'] = next_token
            if max_results is not ShapeBase.NOT_SET:
                _params['max_results'] = max_results
            _request = shapes.ListResourcesRequest(**_params)
        paginator = self.get_paginator("list_resources").paginate(
            **_request.to_boto()
        )
        page_generator = (page for page in paginator)
        first_page = next(page_generator)
        result = shapes.ListResourcesResponse.from_boto(first_page)
        result._page_iterator = page_generator
        return result

        return shapes.ListResourcesResponse.from_boto(response)

    def list_users(
        self,
        _request: shapes.ListUsersRequest = None,
        *,
        organization_id: str,
        next_token: str = ShapeBase.NOT_SET,
        max_results: int = ShapeBase.NOT_SET,
    ) -> shapes.ListUsersResponse:
        """
        Returns summaries of the organization's users.
        """
        if _request is None:
            _params = {}
            if organization_id is not ShapeBase.NOT_SET:
                _params['organization_id'] = organization_id
            if next_token is not ShapeBase.NOT_SET:
                _params['next_token'] = next_token
            if max_results is not ShapeBase.NOT_SET:
                _params['max_results'] = max_results
            _request = shapes.ListUsersRequest(**_params)
        paginator = self.get_paginator("list_users").paginate(
            **_request.to_boto()
        )
        page_generator = (page for page in paginator)
        first_page = next(page_generator)
        result = shapes.ListUsersResponse.from_boto(first_page)
        result._page_iterator = page_generator
        return result

        return shapes.ListUsersResponse.from_boto(response)

    def put_mailbox_permissions(
        self,
        _request: shapes.PutMailboxPermissionsRequest = None,
        *,
        organization_id: str,
        entity_id: str,
        grantee_id: str,
        permission_values: typing.List[typing.Union[str, shapes.PermissionType]
                                      ],
    ) -> shapes.PutMailboxPermissionsResponse:
        """
        Sets permissions for a user or group. This replaces any pre-existing permissions
        set for the entity.
        """
        if _request is None:
            _params = {}
            if organization_id is not ShapeBase.NOT_SET:
                _params['organization_id'] = organization_id
            if entity_id is not ShapeBase.NOT_SET:
                _params['entity_id'] = entity_id
            if grantee_id is not ShapeBase.NOT_SET:
                _params['grantee_id'] = grantee_id
            if permission_values is not ShapeBase.NOT_SET:
                _params['permission_values'] = permission_values
            _request = shapes.PutMailboxPermissionsRequest(**_params)
        response = self._boto_client.put_mailbox_permissions(
            **_request.to_boto()
        )

        return shapes.PutMailboxPermissionsResponse.from_boto(response)

    def register_to_work_mail(
        self,
        _request: shapes.RegisterToWorkMailRequest = None,
        *,
        organization_id: str,
        entity_id: str,
        email: str,
    ) -> shapes.RegisterToWorkMailResponse:
        """
        Registers an existing and disabled user, group, or resource/entity for Amazon
        WorkMail use by associating a mailbox and calendaring capabilities. It performs
        no change if the entity is enabled and fails if the entity is deleted. This
        operation results in the accumulation of costs. For more information, see
        [Pricing](http://aws.amazon.com/workmail/pricing). The equivalent console
        functionality for this operation is _Enable_. Users can either be created by
        calling the CreateUser API or they can be synchronized from your directory. For
        more information, see DeregisterFromWorkMail.
        """
        if _request is None:
            _params = {}
            if organization_id is not ShapeBase.NOT_SET:
                _params['organization_id'] = organization_id
            if entity_id is not ShapeBase.NOT_SET:
                _params['entity_id'] = entity_id
            if email is not ShapeBase.NOT_SET:
                _params['email'] = email
            _request = shapes.RegisterToWorkMailRequest(**_params)
        response = self._boto_client.register_to_work_mail(**_request.to_boto())

        return shapes.RegisterToWorkMailResponse.from_boto(response)

    def reset_password(
        self,
        _request: shapes.ResetPasswordRequest = None,
        *,
        organization_id: str,
        user_id: str,
        password: str,
    ) -> shapes.ResetPasswordResponse:
        """
        Allows the administrator to reset the password for a user.
        """
        if _request is None:
            _params = {}
            if organization_id is not ShapeBase.NOT_SET:
                _params['organization_id'] = organization_id
            if user_id is not ShapeBase.NOT_SET:
                _params['user_id'] = user_id
            if password is not ShapeBase.NOT_SET:
                _params['password'] = password
            _request = shapes.ResetPasswordRequest(**_params)
        response = self._boto_client.reset_password(**_request.to_boto())

        return shapes.ResetPasswordResponse.from_boto(response)

    def update_primary_email_address(
        self,
        _request: shapes.UpdatePrimaryEmailAddressRequest = None,
        *,
        organization_id: str,
        entity_id: str,
        email: str,
    ) -> shapes.UpdatePrimaryEmailAddressResponse:
        """
        Updates the primary email for an entity. The current email is moved into the
        list of aliases (or swapped between an existing alias and the current primary
        email) and the email provided in the input is promoted as the primary.
        """
        if _request is None:
            _params = {}
            if organization_id is not ShapeBase.NOT_SET:
                _params['organization_id'] = organization_id
            if entity_id is not ShapeBase.NOT_SET:
                _params['entity_id'] = entity_id
            if email is not ShapeBase.NOT_SET:
                _params['email'] = email
            _request = shapes.UpdatePrimaryEmailAddressRequest(**_params)
        response = self._boto_client.update_primary_email_address(
            **_request.to_boto()
        )

        return shapes.UpdatePrimaryEmailAddressResponse.from_boto(response)

    def update_resource(
        self,
        _request: shapes.UpdateResourceRequest = None,
        *,
        organization_id: str,
        resource_id: str,
        name: str = ShapeBase.NOT_SET,
        booking_options: shapes.BookingOptions = ShapeBase.NOT_SET,
    ) -> shapes.UpdateResourceResponse:
        """
        Updates data for the resource. It must be preceded by a describe call in order
        to have the latest information. The dataset in the request should be the one
        expected when performing another describe call.
        """
        if _request is None:
            _params = {}
            if organization_id is not ShapeBase.NOT_SET:
                _params['organization_id'] = organization_id
            if resource_id is not ShapeBase.NOT_SET:
                _params['resource_id'] = resource_id
            if name is not ShapeBase.NOT_SET:
                _params['name'] = name
            if booking_options is not ShapeBase.NOT_SET:
                _params['booking_options'] = booking_options
            _request = shapes.UpdateResourceRequest(**_params)
        response = self._boto_client.update_resource(**_request.to_boto())

        return shapes.UpdateResourceResponse.from_boto(response)
