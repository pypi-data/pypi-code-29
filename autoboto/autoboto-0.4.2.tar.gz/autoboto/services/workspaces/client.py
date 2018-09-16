import datetime
import typing
import boto3
from autoboto import ClientBase, ShapeBase, OutputShapeBase
from . import shapes


class Client(ClientBase):
    def __init__(self, *args, **kwargs):
        super().__init__("workspaces", *args, **kwargs)

    def associate_ip_groups(
        self,
        _request: shapes.AssociateIpGroupsRequest = None,
        *,
        directory_id: str,
        group_ids: typing.List[str],
    ) -> shapes.AssociateIpGroupsResult:
        """
        Associates the specified IP access control group with the specified directory.
        """
        if _request is None:
            _params = {}
            if directory_id is not ShapeBase.NOT_SET:
                _params['directory_id'] = directory_id
            if group_ids is not ShapeBase.NOT_SET:
                _params['group_ids'] = group_ids
            _request = shapes.AssociateIpGroupsRequest(**_params)
        response = self._boto_client.associate_ip_groups(**_request.to_boto())

        return shapes.AssociateIpGroupsResult.from_boto(response)

    def authorize_ip_rules(
        self,
        _request: shapes.AuthorizeIpRulesRequest = None,
        *,
        group_id: str,
        user_rules: typing.List[shapes.IpRuleItem],
    ) -> shapes.AuthorizeIpRulesResult:
        """
        Adds one or more rules to the specified IP access control group.

        This action gives users permission to access their WorkSpaces from the CIDR
        address ranges specified in the rules.
        """
        if _request is None:
            _params = {}
            if group_id is not ShapeBase.NOT_SET:
                _params['group_id'] = group_id
            if user_rules is not ShapeBase.NOT_SET:
                _params['user_rules'] = user_rules
            _request = shapes.AuthorizeIpRulesRequest(**_params)
        response = self._boto_client.authorize_ip_rules(**_request.to_boto())

        return shapes.AuthorizeIpRulesResult.from_boto(response)

    def create_ip_group(
        self,
        _request: shapes.CreateIpGroupRequest = None,
        *,
        group_name: str,
        group_desc: str = ShapeBase.NOT_SET,
        user_rules: typing.List[shapes.IpRuleItem] = ShapeBase.NOT_SET,
    ) -> shapes.CreateIpGroupResult:
        """
        Creates an IP access control group.

        An IP access control group provides you with the ability to control the IP
        addresses from which users are allowed to access their WorkSpaces. To specify
        the CIDR address ranges, add rules to your IP access control group and then
        associate the group with your directory. You can add rules when you create the
        group or at any time using AuthorizeIpRules.

        There is a default IP access control group associated with your directory. If
        you don't associate an IP access control group with your directory, the default
        group is used. The default group includes a default rule that allows users to
        access their WorkSpaces from anywhere. You cannot modify the default IP access
        control group for your directory.
        """
        if _request is None:
            _params = {}
            if group_name is not ShapeBase.NOT_SET:
                _params['group_name'] = group_name
            if group_desc is not ShapeBase.NOT_SET:
                _params['group_desc'] = group_desc
            if user_rules is not ShapeBase.NOT_SET:
                _params['user_rules'] = user_rules
            _request = shapes.CreateIpGroupRequest(**_params)
        response = self._boto_client.create_ip_group(**_request.to_boto())

        return shapes.CreateIpGroupResult.from_boto(response)

    def create_tags(
        self,
        _request: shapes.CreateTagsRequest = None,
        *,
        resource_id: str,
        tags: typing.List[shapes.Tag],
    ) -> shapes.CreateTagsResult:
        """
        Creates the specified tags for the specified WorkSpace.
        """
        if _request is None:
            _params = {}
            if resource_id is not ShapeBase.NOT_SET:
                _params['resource_id'] = resource_id
            if tags is not ShapeBase.NOT_SET:
                _params['tags'] = tags
            _request = shapes.CreateTagsRequest(**_params)
        response = self._boto_client.create_tags(**_request.to_boto())

        return shapes.CreateTagsResult.from_boto(response)

    def create_workspaces(
        self,
        _request: shapes.CreateWorkspacesRequest = None,
        *,
        workspaces: typing.List[shapes.WorkspaceRequest],
    ) -> shapes.CreateWorkspacesResult:
        """
        Creates one or more WorkSpaces.

        This operation is asynchronous and returns before the WorkSpaces are created.
        """
        if _request is None:
            _params = {}
            if workspaces is not ShapeBase.NOT_SET:
                _params['workspaces'] = workspaces
            _request = shapes.CreateWorkspacesRequest(**_params)
        response = self._boto_client.create_workspaces(**_request.to_boto())

        return shapes.CreateWorkspacesResult.from_boto(response)

    def delete_ip_group(
        self,
        _request: shapes.DeleteIpGroupRequest = None,
        *,
        group_id: str,
    ) -> shapes.DeleteIpGroupResult:
        """
        Deletes the specified IP access control group.

        You cannot delete an IP access control group that is associated with a
        directory.
        """
        if _request is None:
            _params = {}
            if group_id is not ShapeBase.NOT_SET:
                _params['group_id'] = group_id
            _request = shapes.DeleteIpGroupRequest(**_params)
        response = self._boto_client.delete_ip_group(**_request.to_boto())

        return shapes.DeleteIpGroupResult.from_boto(response)

    def delete_tags(
        self,
        _request: shapes.DeleteTagsRequest = None,
        *,
        resource_id: str,
        tag_keys: typing.List[str],
    ) -> shapes.DeleteTagsResult:
        """
        Deletes the specified tags from the specified WorkSpace.
        """
        if _request is None:
            _params = {}
            if resource_id is not ShapeBase.NOT_SET:
                _params['resource_id'] = resource_id
            if tag_keys is not ShapeBase.NOT_SET:
                _params['tag_keys'] = tag_keys
            _request = shapes.DeleteTagsRequest(**_params)
        response = self._boto_client.delete_tags(**_request.to_boto())

        return shapes.DeleteTagsResult.from_boto(response)

    def describe_ip_groups(
        self,
        _request: shapes.DescribeIpGroupsRequest = None,
        *,
        group_ids: typing.List[str] = ShapeBase.NOT_SET,
        next_token: str = ShapeBase.NOT_SET,
        max_results: int = ShapeBase.NOT_SET,
    ) -> shapes.DescribeIpGroupsResult:
        """
        Describes one or more of your IP access control groups.
        """
        if _request is None:
            _params = {}
            if group_ids is not ShapeBase.NOT_SET:
                _params['group_ids'] = group_ids
            if next_token is not ShapeBase.NOT_SET:
                _params['next_token'] = next_token
            if max_results is not ShapeBase.NOT_SET:
                _params['max_results'] = max_results
            _request = shapes.DescribeIpGroupsRequest(**_params)
        response = self._boto_client.describe_ip_groups(**_request.to_boto())

        return shapes.DescribeIpGroupsResult.from_boto(response)

    def describe_tags(
        self,
        _request: shapes.DescribeTagsRequest = None,
        *,
        resource_id: str,
    ) -> shapes.DescribeTagsResult:
        """
        Describes the specified tags for the specified WorkSpace.
        """
        if _request is None:
            _params = {}
            if resource_id is not ShapeBase.NOT_SET:
                _params['resource_id'] = resource_id
            _request = shapes.DescribeTagsRequest(**_params)
        response = self._boto_client.describe_tags(**_request.to_boto())

        return shapes.DescribeTagsResult.from_boto(response)

    def describe_workspace_bundles(
        self,
        _request: shapes.DescribeWorkspaceBundlesRequest = None,
        *,
        bundle_ids: typing.List[str] = ShapeBase.NOT_SET,
        owner: str = ShapeBase.NOT_SET,
        next_token: str = ShapeBase.NOT_SET,
    ) -> shapes.DescribeWorkspaceBundlesResult:
        """
        Describes the available WorkSpace bundles.

        You can filter the results using either bundle ID or owner, but not both.
        """
        if _request is None:
            _params = {}
            if bundle_ids is not ShapeBase.NOT_SET:
                _params['bundle_ids'] = bundle_ids
            if owner is not ShapeBase.NOT_SET:
                _params['owner'] = owner
            if next_token is not ShapeBase.NOT_SET:
                _params['next_token'] = next_token
            _request = shapes.DescribeWorkspaceBundlesRequest(**_params)
        paginator = self.get_paginator("describe_workspace_bundles").paginate(
            **_request.to_boto()
        )
        page_generator = (page for page in paginator)
        first_page = next(page_generator)
        result = shapes.DescribeWorkspaceBundlesResult.from_boto(first_page)
        result._page_iterator = page_generator
        return result

        return shapes.DescribeWorkspaceBundlesResult.from_boto(response)

    def describe_workspace_directories(
        self,
        _request: shapes.DescribeWorkspaceDirectoriesRequest = None,
        *,
        directory_ids: typing.List[str] = ShapeBase.NOT_SET,
        next_token: str = ShapeBase.NOT_SET,
    ) -> shapes.DescribeWorkspaceDirectoriesResult:
        """
        Describes the available AWS Directory Service directories that are registered
        with Amazon WorkSpaces.
        """
        if _request is None:
            _params = {}
            if directory_ids is not ShapeBase.NOT_SET:
                _params['directory_ids'] = directory_ids
            if next_token is not ShapeBase.NOT_SET:
                _params['next_token'] = next_token
            _request = shapes.DescribeWorkspaceDirectoriesRequest(**_params)
        paginator = self.get_paginator("describe_workspace_directories"
                                      ).paginate(**_request.to_boto())
        page_generator = (page for page in paginator)
        first_page = next(page_generator)
        result = shapes.DescribeWorkspaceDirectoriesResult.from_boto(first_page)
        result._page_iterator = page_generator
        return result

        return shapes.DescribeWorkspaceDirectoriesResult.from_boto(response)

    def describe_workspaces(
        self,
        _request: shapes.DescribeWorkspacesRequest = None,
        *,
        workspace_ids: typing.List[str] = ShapeBase.NOT_SET,
        directory_id: str = ShapeBase.NOT_SET,
        user_name: str = ShapeBase.NOT_SET,
        bundle_id: str = ShapeBase.NOT_SET,
        limit: int = ShapeBase.NOT_SET,
        next_token: str = ShapeBase.NOT_SET,
    ) -> shapes.DescribeWorkspacesResult:
        """
        Describes the specified WorkSpaces.

        You can filter the results using bundle ID, directory ID, or owner, but you can
        specify only one filter at a time.
        """
        if _request is None:
            _params = {}
            if workspace_ids is not ShapeBase.NOT_SET:
                _params['workspace_ids'] = workspace_ids
            if directory_id is not ShapeBase.NOT_SET:
                _params['directory_id'] = directory_id
            if user_name is not ShapeBase.NOT_SET:
                _params['user_name'] = user_name
            if bundle_id is not ShapeBase.NOT_SET:
                _params['bundle_id'] = bundle_id
            if limit is not ShapeBase.NOT_SET:
                _params['limit'] = limit
            if next_token is not ShapeBase.NOT_SET:
                _params['next_token'] = next_token
            _request = shapes.DescribeWorkspacesRequest(**_params)
        paginator = self.get_paginator("describe_workspaces").paginate(
            **_request.to_boto()
        )
        page_generator = (page for page in paginator)
        first_page = next(page_generator)
        result = shapes.DescribeWorkspacesResult.from_boto(first_page)
        result._page_iterator = page_generator
        return result

        return shapes.DescribeWorkspacesResult.from_boto(response)

    def describe_workspaces_connection_status(
        self,
        _request: shapes.DescribeWorkspacesConnectionStatusRequest = None,
        *,
        workspace_ids: typing.List[str] = ShapeBase.NOT_SET,
        next_token: str = ShapeBase.NOT_SET,
    ) -> shapes.DescribeWorkspacesConnectionStatusResult:
        """
        Describes the connection status of the specified WorkSpaces.
        """
        if _request is None:
            _params = {}
            if workspace_ids is not ShapeBase.NOT_SET:
                _params['workspace_ids'] = workspace_ids
            if next_token is not ShapeBase.NOT_SET:
                _params['next_token'] = next_token
            _request = shapes.DescribeWorkspacesConnectionStatusRequest(
                **_params
            )
        response = self._boto_client.describe_workspaces_connection_status(
            **_request.to_boto()
        )

        return shapes.DescribeWorkspacesConnectionStatusResult.from_boto(
            response
        )

    def disassociate_ip_groups(
        self,
        _request: shapes.DisassociateIpGroupsRequest = None,
        *,
        directory_id: str,
        group_ids: typing.List[str],
    ) -> shapes.DisassociateIpGroupsResult:
        """
        Disassociates the specified IP access control group from the specified
        directory.
        """
        if _request is None:
            _params = {}
            if directory_id is not ShapeBase.NOT_SET:
                _params['directory_id'] = directory_id
            if group_ids is not ShapeBase.NOT_SET:
                _params['group_ids'] = group_ids
            _request = shapes.DisassociateIpGroupsRequest(**_params)
        response = self._boto_client.disassociate_ip_groups(
            **_request.to_boto()
        )

        return shapes.DisassociateIpGroupsResult.from_boto(response)

    def modify_workspace_properties(
        self,
        _request: shapes.ModifyWorkspacePropertiesRequest = None,
        *,
        workspace_id: str,
        workspace_properties: shapes.WorkspaceProperties,
    ) -> shapes.ModifyWorkspacePropertiesResult:
        """
        Modifies the specified WorkSpace properties.
        """
        if _request is None:
            _params = {}
            if workspace_id is not ShapeBase.NOT_SET:
                _params['workspace_id'] = workspace_id
            if workspace_properties is not ShapeBase.NOT_SET:
                _params['workspace_properties'] = workspace_properties
            _request = shapes.ModifyWorkspacePropertiesRequest(**_params)
        response = self._boto_client.modify_workspace_properties(
            **_request.to_boto()
        )

        return shapes.ModifyWorkspacePropertiesResult.from_boto(response)

    def modify_workspace_state(
        self,
        _request: shapes.ModifyWorkspaceStateRequest = None,
        *,
        workspace_id: str,
        workspace_state: typing.Union[str, shapes.TargetWorkspaceState],
    ) -> shapes.ModifyWorkspaceStateResult:
        """
        Sets the state of the specified WorkSpace.

        To maintain a WorkSpace without being interrupted, set the WorkSpace state to
        `ADMIN_MAINTENANCE`. WorkSpaces in this state do not respond to requests to
        reboot, stop, start, or rebuild. An AutoStop WorkSpace in this state is not
        stopped. Users can log into a WorkSpace in the `ADMIN_MAINTENANCE` state.
        """
        if _request is None:
            _params = {}
            if workspace_id is not ShapeBase.NOT_SET:
                _params['workspace_id'] = workspace_id
            if workspace_state is not ShapeBase.NOT_SET:
                _params['workspace_state'] = workspace_state
            _request = shapes.ModifyWorkspaceStateRequest(**_params)
        response = self._boto_client.modify_workspace_state(
            **_request.to_boto()
        )

        return shapes.ModifyWorkspaceStateResult.from_boto(response)

    def reboot_workspaces(
        self,
        _request: shapes.RebootWorkspacesRequest = None,
        *,
        reboot_workspace_requests: typing.List[shapes.RebootRequest],
    ) -> shapes.RebootWorkspacesResult:
        """
        Reboots the specified WorkSpaces.

        You cannot reboot a WorkSpace unless its state is `AVAILABLE` or `UNHEALTHY`.

        This operation is asynchronous and returns before the WorkSpaces have rebooted.
        """
        if _request is None:
            _params = {}
            if reboot_workspace_requests is not ShapeBase.NOT_SET:
                _params['reboot_workspace_requests'] = reboot_workspace_requests
            _request = shapes.RebootWorkspacesRequest(**_params)
        response = self._boto_client.reboot_workspaces(**_request.to_boto())

        return shapes.RebootWorkspacesResult.from_boto(response)

    def rebuild_workspaces(
        self,
        _request: shapes.RebuildWorkspacesRequest = None,
        *,
        rebuild_workspace_requests: typing.List[shapes.RebuildRequest],
    ) -> shapes.RebuildWorkspacesResult:
        """
        Rebuilds the specified WorkSpace.

        You cannot rebuild a WorkSpace unless its state is `AVAILABLE`, `ERROR`, or
        `UNHEALTHY`.

        Rebuilding a WorkSpace is a potentially destructive action that can result in
        the loss of data. For more information, see [Rebuild a
        WorkSpace](http://docs.aws.amazon.com/workspaces/latest/adminguide/reset-
        workspace.html).

        This operation is asynchronous and returns before the WorkSpaces have been
        completely rebuilt.
        """
        if _request is None:
            _params = {}
            if rebuild_workspace_requests is not ShapeBase.NOT_SET:
                _params['rebuild_workspace_requests'
                       ] = rebuild_workspace_requests
            _request = shapes.RebuildWorkspacesRequest(**_params)
        response = self._boto_client.rebuild_workspaces(**_request.to_boto())

        return shapes.RebuildWorkspacesResult.from_boto(response)

    def revoke_ip_rules(
        self,
        _request: shapes.RevokeIpRulesRequest = None,
        *,
        group_id: str,
        user_rules: typing.List[str],
    ) -> shapes.RevokeIpRulesResult:
        """
        Removes one or more rules from the specified IP access control group.
        """
        if _request is None:
            _params = {}
            if group_id is not ShapeBase.NOT_SET:
                _params['group_id'] = group_id
            if user_rules is not ShapeBase.NOT_SET:
                _params['user_rules'] = user_rules
            _request = shapes.RevokeIpRulesRequest(**_params)
        response = self._boto_client.revoke_ip_rules(**_request.to_boto())

        return shapes.RevokeIpRulesResult.from_boto(response)

    def start_workspaces(
        self,
        _request: shapes.StartWorkspacesRequest = None,
        *,
        start_workspace_requests: typing.List[shapes.StartRequest],
    ) -> shapes.StartWorkspacesResult:
        """
        Starts the specified WorkSpaces.

        You cannot start a WorkSpace unless it has a running mode of `AutoStop` and a
        state of `STOPPED`.
        """
        if _request is None:
            _params = {}
            if start_workspace_requests is not ShapeBase.NOT_SET:
                _params['start_workspace_requests'] = start_workspace_requests
            _request = shapes.StartWorkspacesRequest(**_params)
        response = self._boto_client.start_workspaces(**_request.to_boto())

        return shapes.StartWorkspacesResult.from_boto(response)

    def stop_workspaces(
        self,
        _request: shapes.StopWorkspacesRequest = None,
        *,
        stop_workspace_requests: typing.List[shapes.StopRequest],
    ) -> shapes.StopWorkspacesResult:
        """
        Stops the specified WorkSpaces.

        You cannot stop a WorkSpace unless it has a running mode of `AutoStop` and a
        state of `AVAILABLE`, `IMPAIRED`, `UNHEALTHY`, or `ERROR`.
        """
        if _request is None:
            _params = {}
            if stop_workspace_requests is not ShapeBase.NOT_SET:
                _params['stop_workspace_requests'] = stop_workspace_requests
            _request = shapes.StopWorkspacesRequest(**_params)
        response = self._boto_client.stop_workspaces(**_request.to_boto())

        return shapes.StopWorkspacesResult.from_boto(response)

    def terminate_workspaces(
        self,
        _request: shapes.TerminateWorkspacesRequest = None,
        *,
        terminate_workspace_requests: typing.List[shapes.TerminateRequest],
    ) -> shapes.TerminateWorkspacesResult:
        """
        Terminates the specified WorkSpaces.

        Terminating a WorkSpace is a permanent action and cannot be undone. The user's
        data is destroyed. If you need to archive any user data, contact Amazon Web
        Services before terminating the WorkSpace.

        You can terminate a WorkSpace that is in any state except `SUSPENDED`.

        This operation is asynchronous and returns before the WorkSpaces have been
        completely terminated.
        """
        if _request is None:
            _params = {}
            if terminate_workspace_requests is not ShapeBase.NOT_SET:
                _params['terminate_workspace_requests'
                       ] = terminate_workspace_requests
            _request = shapes.TerminateWorkspacesRequest(**_params)
        response = self._boto_client.terminate_workspaces(**_request.to_boto())

        return shapes.TerminateWorkspacesResult.from_boto(response)

    def update_rules_of_ip_group(
        self,
        _request: shapes.UpdateRulesOfIpGroupRequest = None,
        *,
        group_id: str,
        user_rules: typing.List[shapes.IpRuleItem],
    ) -> shapes.UpdateRulesOfIpGroupResult:
        """
        Replaces the current rules of the specified IP access control group with the
        specified rules.
        """
        if _request is None:
            _params = {}
            if group_id is not ShapeBase.NOT_SET:
                _params['group_id'] = group_id
            if user_rules is not ShapeBase.NOT_SET:
                _params['user_rules'] = user_rules
            _request = shapes.UpdateRulesOfIpGroupRequest(**_params)
        response = self._boto_client.update_rules_of_ip_group(
            **_request.to_boto()
        )

        return shapes.UpdateRulesOfIpGroupResult.from_boto(response)
