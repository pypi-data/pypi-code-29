import datetime
import typing
import boto3
from autoboto import ClientBase, ShapeBase, OutputShapeBase
from . import shapes


class Client(ClientBase):
    def __init__(self, *args, **kwargs):
        super().__init__("codestar", *args, **kwargs)

    def associate_team_member(
        self,
        _request: shapes.AssociateTeamMemberRequest = None,
        *,
        project_id: str,
        user_arn: str,
        project_role: str,
        client_request_token: str = ShapeBase.NOT_SET,
        remote_access_allowed: bool = ShapeBase.NOT_SET,
    ) -> shapes.AssociateTeamMemberResult:
        """
        Adds an IAM user to the team for an AWS CodeStar project.
        """
        if _request is None:
            _params = {}
            if project_id is not ShapeBase.NOT_SET:
                _params['project_id'] = project_id
            if user_arn is not ShapeBase.NOT_SET:
                _params['user_arn'] = user_arn
            if project_role is not ShapeBase.NOT_SET:
                _params['project_role'] = project_role
            if client_request_token is not ShapeBase.NOT_SET:
                _params['client_request_token'] = client_request_token
            if remote_access_allowed is not ShapeBase.NOT_SET:
                _params['remote_access_allowed'] = remote_access_allowed
            _request = shapes.AssociateTeamMemberRequest(**_params)
        response = self._boto_client.associate_team_member(**_request.to_boto())

        return shapes.AssociateTeamMemberResult.from_boto(response)

    def create_project(
        self,
        _request: shapes.CreateProjectRequest = None,
        *,
        name: str,
        id: str,
        description: str = ShapeBase.NOT_SET,
        client_request_token: str = ShapeBase.NOT_SET,
    ) -> shapes.CreateProjectResult:
        """
        Reserved for future use. To create a project, use the AWS CodeStar console.
        """
        if _request is None:
            _params = {}
            if name is not ShapeBase.NOT_SET:
                _params['name'] = name
            if id is not ShapeBase.NOT_SET:
                _params['id'] = id
            if description is not ShapeBase.NOT_SET:
                _params['description'] = description
            if client_request_token is not ShapeBase.NOT_SET:
                _params['client_request_token'] = client_request_token
            _request = shapes.CreateProjectRequest(**_params)
        response = self._boto_client.create_project(**_request.to_boto())

        return shapes.CreateProjectResult.from_boto(response)

    def create_user_profile(
        self,
        _request: shapes.CreateUserProfileRequest = None,
        *,
        user_arn: str,
        display_name: str,
        email_address: str,
        ssh_public_key: str = ShapeBase.NOT_SET,
    ) -> shapes.CreateUserProfileResult:
        """
        Creates a profile for a user that includes user preferences, such as the display
        name and email address assocciated with the user, in AWS CodeStar. The user
        profile is not project-specific. Information in the user profile is displayed
        wherever the user's information appears to other users in AWS CodeStar.
        """
        if _request is None:
            _params = {}
            if user_arn is not ShapeBase.NOT_SET:
                _params['user_arn'] = user_arn
            if display_name is not ShapeBase.NOT_SET:
                _params['display_name'] = display_name
            if email_address is not ShapeBase.NOT_SET:
                _params['email_address'] = email_address
            if ssh_public_key is not ShapeBase.NOT_SET:
                _params['ssh_public_key'] = ssh_public_key
            _request = shapes.CreateUserProfileRequest(**_params)
        response = self._boto_client.create_user_profile(**_request.to_boto())

        return shapes.CreateUserProfileResult.from_boto(response)

    def delete_project(
        self,
        _request: shapes.DeleteProjectRequest = None,
        *,
        id: str,
        client_request_token: str = ShapeBase.NOT_SET,
        delete_stack: bool = ShapeBase.NOT_SET,
    ) -> shapes.DeleteProjectResult:
        """
        Deletes a project, including project resources. Does not delete users associated
        with the project, but does delete the IAM roles that allowed access to the
        project.
        """
        if _request is None:
            _params = {}
            if id is not ShapeBase.NOT_SET:
                _params['id'] = id
            if client_request_token is not ShapeBase.NOT_SET:
                _params['client_request_token'] = client_request_token
            if delete_stack is not ShapeBase.NOT_SET:
                _params['delete_stack'] = delete_stack
            _request = shapes.DeleteProjectRequest(**_params)
        response = self._boto_client.delete_project(**_request.to_boto())

        return shapes.DeleteProjectResult.from_boto(response)

    def delete_user_profile(
        self,
        _request: shapes.DeleteUserProfileRequest = None,
        *,
        user_arn: str,
    ) -> shapes.DeleteUserProfileResult:
        """
        Deletes a user profile in AWS CodeStar, including all personal preference data
        associated with that profile, such as display name and email address. It does
        not delete the history of that user, for example the history of commits made by
        that user.
        """
        if _request is None:
            _params = {}
            if user_arn is not ShapeBase.NOT_SET:
                _params['user_arn'] = user_arn
            _request = shapes.DeleteUserProfileRequest(**_params)
        response = self._boto_client.delete_user_profile(**_request.to_boto())

        return shapes.DeleteUserProfileResult.from_boto(response)

    def describe_project(
        self,
        _request: shapes.DescribeProjectRequest = None,
        *,
        id: str,
    ) -> shapes.DescribeProjectResult:
        """
        Describes a project and its resources.
        """
        if _request is None:
            _params = {}
            if id is not ShapeBase.NOT_SET:
                _params['id'] = id
            _request = shapes.DescribeProjectRequest(**_params)
        response = self._boto_client.describe_project(**_request.to_boto())

        return shapes.DescribeProjectResult.from_boto(response)

    def describe_user_profile(
        self,
        _request: shapes.DescribeUserProfileRequest = None,
        *,
        user_arn: str,
    ) -> shapes.DescribeUserProfileResult:
        """
        Describes a user in AWS CodeStar and the user attributes across all projects.
        """
        if _request is None:
            _params = {}
            if user_arn is not ShapeBase.NOT_SET:
                _params['user_arn'] = user_arn
            _request = shapes.DescribeUserProfileRequest(**_params)
        response = self._boto_client.describe_user_profile(**_request.to_boto())

        return shapes.DescribeUserProfileResult.from_boto(response)

    def disassociate_team_member(
        self,
        _request: shapes.DisassociateTeamMemberRequest = None,
        *,
        project_id: str,
        user_arn: str,
    ) -> shapes.DisassociateTeamMemberResult:
        """
        Removes a user from a project. Removing a user from a project also removes the
        IAM policies from that user that allowed access to the project and its
        resources. Disassociating a team member does not remove that user's profile from
        AWS CodeStar. It does not remove the user from IAM.
        """
        if _request is None:
            _params = {}
            if project_id is not ShapeBase.NOT_SET:
                _params['project_id'] = project_id
            if user_arn is not ShapeBase.NOT_SET:
                _params['user_arn'] = user_arn
            _request = shapes.DisassociateTeamMemberRequest(**_params)
        response = self._boto_client.disassociate_team_member(
            **_request.to_boto()
        )

        return shapes.DisassociateTeamMemberResult.from_boto(response)

    def list_projects(
        self,
        _request: shapes.ListProjectsRequest = None,
        *,
        next_token: str = ShapeBase.NOT_SET,
        max_results: int = ShapeBase.NOT_SET,
    ) -> shapes.ListProjectsResult:
        """
        Lists all projects in AWS CodeStar associated with your AWS account.
        """
        if _request is None:
            _params = {}
            if next_token is not ShapeBase.NOT_SET:
                _params['next_token'] = next_token
            if max_results is not ShapeBase.NOT_SET:
                _params['max_results'] = max_results
            _request = shapes.ListProjectsRequest(**_params)
        response = self._boto_client.list_projects(**_request.to_boto())

        return shapes.ListProjectsResult.from_boto(response)

    def list_resources(
        self,
        _request: shapes.ListResourcesRequest = None,
        *,
        project_id: str,
        next_token: str = ShapeBase.NOT_SET,
        max_results: int = ShapeBase.NOT_SET,
    ) -> shapes.ListResourcesResult:
        """
        Lists resources associated with a project in AWS CodeStar.
        """
        if _request is None:
            _params = {}
            if project_id is not ShapeBase.NOT_SET:
                _params['project_id'] = project_id
            if next_token is not ShapeBase.NOT_SET:
                _params['next_token'] = next_token
            if max_results is not ShapeBase.NOT_SET:
                _params['max_results'] = max_results
            _request = shapes.ListResourcesRequest(**_params)
        response = self._boto_client.list_resources(**_request.to_boto())

        return shapes.ListResourcesResult.from_boto(response)

    def list_tags_for_project(
        self,
        _request: shapes.ListTagsForProjectRequest = None,
        *,
        id: str,
        next_token: str = ShapeBase.NOT_SET,
        max_results: int = ShapeBase.NOT_SET,
    ) -> shapes.ListTagsForProjectResult:
        """
        Gets the tags for a project.
        """
        if _request is None:
            _params = {}
            if id is not ShapeBase.NOT_SET:
                _params['id'] = id
            if next_token is not ShapeBase.NOT_SET:
                _params['next_token'] = next_token
            if max_results is not ShapeBase.NOT_SET:
                _params['max_results'] = max_results
            _request = shapes.ListTagsForProjectRequest(**_params)
        response = self._boto_client.list_tags_for_project(**_request.to_boto())

        return shapes.ListTagsForProjectResult.from_boto(response)

    def list_team_members(
        self,
        _request: shapes.ListTeamMembersRequest = None,
        *,
        project_id: str,
        next_token: str = ShapeBase.NOT_SET,
        max_results: int = ShapeBase.NOT_SET,
    ) -> shapes.ListTeamMembersResult:
        """
        Lists all team members associated with a project.
        """
        if _request is None:
            _params = {}
            if project_id is not ShapeBase.NOT_SET:
                _params['project_id'] = project_id
            if next_token is not ShapeBase.NOT_SET:
                _params['next_token'] = next_token
            if max_results is not ShapeBase.NOT_SET:
                _params['max_results'] = max_results
            _request = shapes.ListTeamMembersRequest(**_params)
        response = self._boto_client.list_team_members(**_request.to_boto())

        return shapes.ListTeamMembersResult.from_boto(response)

    def list_user_profiles(
        self,
        _request: shapes.ListUserProfilesRequest = None,
        *,
        next_token: str = ShapeBase.NOT_SET,
        max_results: int = ShapeBase.NOT_SET,
    ) -> shapes.ListUserProfilesResult:
        """
        Lists all the user profiles configured for your AWS account in AWS CodeStar.
        """
        if _request is None:
            _params = {}
            if next_token is not ShapeBase.NOT_SET:
                _params['next_token'] = next_token
            if max_results is not ShapeBase.NOT_SET:
                _params['max_results'] = max_results
            _request = shapes.ListUserProfilesRequest(**_params)
        response = self._boto_client.list_user_profiles(**_request.to_boto())

        return shapes.ListUserProfilesResult.from_boto(response)

    def tag_project(
        self,
        _request: shapes.TagProjectRequest = None,
        *,
        id: str,
        tags: typing.Dict[str, str],
    ) -> shapes.TagProjectResult:
        """
        Adds tags to a project.
        """
        if _request is None:
            _params = {}
            if id is not ShapeBase.NOT_SET:
                _params['id'] = id
            if tags is not ShapeBase.NOT_SET:
                _params['tags'] = tags
            _request = shapes.TagProjectRequest(**_params)
        response = self._boto_client.tag_project(**_request.to_boto())

        return shapes.TagProjectResult.from_boto(response)

    def untag_project(
        self,
        _request: shapes.UntagProjectRequest = None,
        *,
        id: str,
        tags: typing.List[str],
    ) -> shapes.UntagProjectResult:
        """
        Removes tags from a project.
        """
        if _request is None:
            _params = {}
            if id is not ShapeBase.NOT_SET:
                _params['id'] = id
            if tags is not ShapeBase.NOT_SET:
                _params['tags'] = tags
            _request = shapes.UntagProjectRequest(**_params)
        response = self._boto_client.untag_project(**_request.to_boto())

        return shapes.UntagProjectResult.from_boto(response)

    def update_project(
        self,
        _request: shapes.UpdateProjectRequest = None,
        *,
        id: str,
        name: str = ShapeBase.NOT_SET,
        description: str = ShapeBase.NOT_SET,
    ) -> shapes.UpdateProjectResult:
        """
        Updates a project in AWS CodeStar.
        """
        if _request is None:
            _params = {}
            if id is not ShapeBase.NOT_SET:
                _params['id'] = id
            if name is not ShapeBase.NOT_SET:
                _params['name'] = name
            if description is not ShapeBase.NOT_SET:
                _params['description'] = description
            _request = shapes.UpdateProjectRequest(**_params)
        response = self._boto_client.update_project(**_request.to_boto())

        return shapes.UpdateProjectResult.from_boto(response)

    def update_team_member(
        self,
        _request: shapes.UpdateTeamMemberRequest = None,
        *,
        project_id: str,
        user_arn: str,
        project_role: str = ShapeBase.NOT_SET,
        remote_access_allowed: bool = ShapeBase.NOT_SET,
    ) -> shapes.UpdateTeamMemberResult:
        """
        Updates a team member's attributes in an AWS CodeStar project. For example, you
        can change a team member's role in the project, or change whether they have
        remote access to project resources.
        """
        if _request is None:
            _params = {}
            if project_id is not ShapeBase.NOT_SET:
                _params['project_id'] = project_id
            if user_arn is not ShapeBase.NOT_SET:
                _params['user_arn'] = user_arn
            if project_role is not ShapeBase.NOT_SET:
                _params['project_role'] = project_role
            if remote_access_allowed is not ShapeBase.NOT_SET:
                _params['remote_access_allowed'] = remote_access_allowed
            _request = shapes.UpdateTeamMemberRequest(**_params)
        response = self._boto_client.update_team_member(**_request.to_boto())

        return shapes.UpdateTeamMemberResult.from_boto(response)

    def update_user_profile(
        self,
        _request: shapes.UpdateUserProfileRequest = None,
        *,
        user_arn: str,
        display_name: str = ShapeBase.NOT_SET,
        email_address: str = ShapeBase.NOT_SET,
        ssh_public_key: str = ShapeBase.NOT_SET,
    ) -> shapes.UpdateUserProfileResult:
        """
        Updates a user's profile in AWS CodeStar. The user profile is not project-
        specific. Information in the user profile is displayed wherever the user's
        information appears to other users in AWS CodeStar.
        """
        if _request is None:
            _params = {}
            if user_arn is not ShapeBase.NOT_SET:
                _params['user_arn'] = user_arn
            if display_name is not ShapeBase.NOT_SET:
                _params['display_name'] = display_name
            if email_address is not ShapeBase.NOT_SET:
                _params['email_address'] = email_address
            if ssh_public_key is not ShapeBase.NOT_SET:
                _params['ssh_public_key'] = ssh_public_key
            _request = shapes.UpdateUserProfileRequest(**_params)
        response = self._boto_client.update_user_profile(**_request.to_boto())

        return shapes.UpdateUserProfileResult.from_boto(response)
