import datetime
import typing
import boto3
from autoboto import ClientBase, ShapeBase, OutputShapeBase
from . import shapes


class Client(ClientBase):
    def __init__(self, *args, **kwargs):
        super().__init__("codecommit", *args, **kwargs)

    def batch_get_repositories(
        self,
        _request: shapes.BatchGetRepositoriesInput = None,
        *,
        repository_names: typing.List[str],
    ) -> shapes.BatchGetRepositoriesOutput:
        """
        Returns information about one or more repositories.

        The description field for a repository accepts all HTML characters and all valid
        Unicode characters. Applications that do not HTML-encode the description and
        display it in a web page could expose users to potentially malicious code. Make
        sure that you HTML-encode the description field in any application that uses
        this API to display the repository description on a web page.
        """
        if _request is None:
            _params = {}
            if repository_names is not ShapeBase.NOT_SET:
                _params['repository_names'] = repository_names
            _request = shapes.BatchGetRepositoriesInput(**_params)
        response = self._boto_client.batch_get_repositories(
            **_request.to_boto()
        )

        return shapes.BatchGetRepositoriesOutput.from_boto(response)

    def create_branch(
        self,
        _request: shapes.CreateBranchInput = None,
        *,
        repository_name: str,
        branch_name: str,
        commit_id: str,
    ) -> None:
        """
        Creates a new branch in a repository and points the branch to a commit.

        Calling the create branch operation does not set a repository's default branch.
        To do this, call the update default branch operation.
        """
        if _request is None:
            _params = {}
            if repository_name is not ShapeBase.NOT_SET:
                _params['repository_name'] = repository_name
            if branch_name is not ShapeBase.NOT_SET:
                _params['branch_name'] = branch_name
            if commit_id is not ShapeBase.NOT_SET:
                _params['commit_id'] = commit_id
            _request = shapes.CreateBranchInput(**_params)
        response = self._boto_client.create_branch(**_request.to_boto())

    def create_pull_request(
        self,
        _request: shapes.CreatePullRequestInput = None,
        *,
        title: str,
        targets: typing.List[shapes.Target],
        description: str = ShapeBase.NOT_SET,
        client_request_token: str = ShapeBase.NOT_SET,
    ) -> shapes.CreatePullRequestOutput:
        """
        Creates a pull request in the specified repository.
        """
        if _request is None:
            _params = {}
            if title is not ShapeBase.NOT_SET:
                _params['title'] = title
            if targets is not ShapeBase.NOT_SET:
                _params['targets'] = targets
            if description is not ShapeBase.NOT_SET:
                _params['description'] = description
            if client_request_token is not ShapeBase.NOT_SET:
                _params['client_request_token'] = client_request_token
            _request = shapes.CreatePullRequestInput(**_params)
        response = self._boto_client.create_pull_request(**_request.to_boto())

        return shapes.CreatePullRequestOutput.from_boto(response)

    def create_repository(
        self,
        _request: shapes.CreateRepositoryInput = None,
        *,
        repository_name: str,
        repository_description: str = ShapeBase.NOT_SET,
    ) -> shapes.CreateRepositoryOutput:
        """
        Creates a new, empty repository.
        """
        if _request is None:
            _params = {}
            if repository_name is not ShapeBase.NOT_SET:
                _params['repository_name'] = repository_name
            if repository_description is not ShapeBase.NOT_SET:
                _params['repository_description'] = repository_description
            _request = shapes.CreateRepositoryInput(**_params)
        response = self._boto_client.create_repository(**_request.to_boto())

        return shapes.CreateRepositoryOutput.from_boto(response)

    def delete_branch(
        self,
        _request: shapes.DeleteBranchInput = None,
        *,
        repository_name: str,
        branch_name: str,
    ) -> shapes.DeleteBranchOutput:
        """
        Deletes a branch from a repository, unless that branch is the default branch for
        the repository.
        """
        if _request is None:
            _params = {}
            if repository_name is not ShapeBase.NOT_SET:
                _params['repository_name'] = repository_name
            if branch_name is not ShapeBase.NOT_SET:
                _params['branch_name'] = branch_name
            _request = shapes.DeleteBranchInput(**_params)
        response = self._boto_client.delete_branch(**_request.to_boto())

        return shapes.DeleteBranchOutput.from_boto(response)

    def delete_comment_content(
        self,
        _request: shapes.DeleteCommentContentInput = None,
        *,
        comment_id: str,
    ) -> shapes.DeleteCommentContentOutput:
        """
        Deletes the content of a comment made on a change, file, or commit in a
        repository.
        """
        if _request is None:
            _params = {}
            if comment_id is not ShapeBase.NOT_SET:
                _params['comment_id'] = comment_id
            _request = shapes.DeleteCommentContentInput(**_params)
        response = self._boto_client.delete_comment_content(
            **_request.to_boto()
        )

        return shapes.DeleteCommentContentOutput.from_boto(response)

    def delete_repository(
        self,
        _request: shapes.DeleteRepositoryInput = None,
        *,
        repository_name: str,
    ) -> shapes.DeleteRepositoryOutput:
        """
        Deletes a repository. If a specified repository was already deleted, a null
        repository ID will be returned.

        Deleting a repository also deletes all associated objects and metadata. After a
        repository is deleted, all future push calls to the deleted repository will
        fail.
        """
        if _request is None:
            _params = {}
            if repository_name is not ShapeBase.NOT_SET:
                _params['repository_name'] = repository_name
            _request = shapes.DeleteRepositoryInput(**_params)
        response = self._boto_client.delete_repository(**_request.to_boto())

        return shapes.DeleteRepositoryOutput.from_boto(response)

    def describe_pull_request_events(
        self,
        _request: shapes.DescribePullRequestEventsInput = None,
        *,
        pull_request_id: str,
        pull_request_event_type: typing.
        Union[str, shapes.PullRequestEventType] = ShapeBase.NOT_SET,
        actor_arn: str = ShapeBase.NOT_SET,
        next_token: str = ShapeBase.NOT_SET,
        max_results: int = ShapeBase.NOT_SET,
    ) -> shapes.DescribePullRequestEventsOutput:
        """
        Returns information about one or more pull request events.
        """
        if _request is None:
            _params = {}
            if pull_request_id is not ShapeBase.NOT_SET:
                _params['pull_request_id'] = pull_request_id
            if pull_request_event_type is not ShapeBase.NOT_SET:
                _params['pull_request_event_type'] = pull_request_event_type
            if actor_arn is not ShapeBase.NOT_SET:
                _params['actor_arn'] = actor_arn
            if next_token is not ShapeBase.NOT_SET:
                _params['next_token'] = next_token
            if max_results is not ShapeBase.NOT_SET:
                _params['max_results'] = max_results
            _request = shapes.DescribePullRequestEventsInput(**_params)
        paginator = self.get_paginator("describe_pull_request_events").paginate(
            **_request.to_boto()
        )
        page_generator = (page for page in paginator)
        first_page = next(page_generator)
        result = shapes.DescribePullRequestEventsOutput.from_boto(first_page)
        result._page_iterator = page_generator
        return result

        return shapes.DescribePullRequestEventsOutput.from_boto(response)

    def get_blob(
        self,
        _request: shapes.GetBlobInput = None,
        *,
        repository_name: str,
        blob_id: str,
    ) -> shapes.GetBlobOutput:
        """
        Returns the base-64 encoded content of an individual blob within a repository.
        """
        if _request is None:
            _params = {}
            if repository_name is not ShapeBase.NOT_SET:
                _params['repository_name'] = repository_name
            if blob_id is not ShapeBase.NOT_SET:
                _params['blob_id'] = blob_id
            _request = shapes.GetBlobInput(**_params)
        response = self._boto_client.get_blob(**_request.to_boto())

        return shapes.GetBlobOutput.from_boto(response)

    def get_branch(
        self,
        _request: shapes.GetBranchInput = None,
        *,
        repository_name: str = ShapeBase.NOT_SET,
        branch_name: str = ShapeBase.NOT_SET,
    ) -> shapes.GetBranchOutput:
        """
        Returns information about a repository branch, including its name and the last
        commit ID.
        """
        if _request is None:
            _params = {}
            if repository_name is not ShapeBase.NOT_SET:
                _params['repository_name'] = repository_name
            if branch_name is not ShapeBase.NOT_SET:
                _params['branch_name'] = branch_name
            _request = shapes.GetBranchInput(**_params)
        response = self._boto_client.get_branch(**_request.to_boto())

        return shapes.GetBranchOutput.from_boto(response)

    def get_comment(
        self,
        _request: shapes.GetCommentInput = None,
        *,
        comment_id: str,
    ) -> shapes.GetCommentOutput:
        """
        Returns the content of a comment made on a change, file, or commit in a
        repository.
        """
        if _request is None:
            _params = {}
            if comment_id is not ShapeBase.NOT_SET:
                _params['comment_id'] = comment_id
            _request = shapes.GetCommentInput(**_params)
        response = self._boto_client.get_comment(**_request.to_boto())

        return shapes.GetCommentOutput.from_boto(response)

    def get_comments_for_compared_commit(
        self,
        _request: shapes.GetCommentsForComparedCommitInput = None,
        *,
        repository_name: str,
        after_commit_id: str,
        before_commit_id: str = ShapeBase.NOT_SET,
        next_token: str = ShapeBase.NOT_SET,
        max_results: int = ShapeBase.NOT_SET,
    ) -> shapes.GetCommentsForComparedCommitOutput:
        """
        Returns information about comments made on the comparison between two commits.
        """
        if _request is None:
            _params = {}
            if repository_name is not ShapeBase.NOT_SET:
                _params['repository_name'] = repository_name
            if after_commit_id is not ShapeBase.NOT_SET:
                _params['after_commit_id'] = after_commit_id
            if before_commit_id is not ShapeBase.NOT_SET:
                _params['before_commit_id'] = before_commit_id
            if next_token is not ShapeBase.NOT_SET:
                _params['next_token'] = next_token
            if max_results is not ShapeBase.NOT_SET:
                _params['max_results'] = max_results
            _request = shapes.GetCommentsForComparedCommitInput(**_params)
        paginator = self.get_paginator("get_comments_for_compared_commit"
                                      ).paginate(**_request.to_boto())
        page_generator = (page for page in paginator)
        first_page = next(page_generator)
        result = shapes.GetCommentsForComparedCommitOutput.from_boto(first_page)
        result._page_iterator = page_generator
        return result

        return shapes.GetCommentsForComparedCommitOutput.from_boto(response)

    def get_comments_for_pull_request(
        self,
        _request: shapes.GetCommentsForPullRequestInput = None,
        *,
        pull_request_id: str,
        repository_name: str = ShapeBase.NOT_SET,
        before_commit_id: str = ShapeBase.NOT_SET,
        after_commit_id: str = ShapeBase.NOT_SET,
        next_token: str = ShapeBase.NOT_SET,
        max_results: int = ShapeBase.NOT_SET,
    ) -> shapes.GetCommentsForPullRequestOutput:
        """
        Returns comments made on a pull request.
        """
        if _request is None:
            _params = {}
            if pull_request_id is not ShapeBase.NOT_SET:
                _params['pull_request_id'] = pull_request_id
            if repository_name is not ShapeBase.NOT_SET:
                _params['repository_name'] = repository_name
            if before_commit_id is not ShapeBase.NOT_SET:
                _params['before_commit_id'] = before_commit_id
            if after_commit_id is not ShapeBase.NOT_SET:
                _params['after_commit_id'] = after_commit_id
            if next_token is not ShapeBase.NOT_SET:
                _params['next_token'] = next_token
            if max_results is not ShapeBase.NOT_SET:
                _params['max_results'] = max_results
            _request = shapes.GetCommentsForPullRequestInput(**_params)
        paginator = self.get_paginator("get_comments_for_pull_request"
                                      ).paginate(**_request.to_boto())
        page_generator = (page for page in paginator)
        first_page = next(page_generator)
        result = shapes.GetCommentsForPullRequestOutput.from_boto(first_page)
        result._page_iterator = page_generator
        return result

        return shapes.GetCommentsForPullRequestOutput.from_boto(response)

    def get_commit(
        self,
        _request: shapes.GetCommitInput = None,
        *,
        repository_name: str,
        commit_id: str,
    ) -> shapes.GetCommitOutput:
        """
        Returns information about a commit, including commit message and committer
        information.
        """
        if _request is None:
            _params = {}
            if repository_name is not ShapeBase.NOT_SET:
                _params['repository_name'] = repository_name
            if commit_id is not ShapeBase.NOT_SET:
                _params['commit_id'] = commit_id
            _request = shapes.GetCommitInput(**_params)
        response = self._boto_client.get_commit(**_request.to_boto())

        return shapes.GetCommitOutput.from_boto(response)

    def get_differences(
        self,
        _request: shapes.GetDifferencesInput = None,
        *,
        repository_name: str,
        after_commit_specifier: str,
        before_commit_specifier: str = ShapeBase.NOT_SET,
        before_path: str = ShapeBase.NOT_SET,
        after_path: str = ShapeBase.NOT_SET,
        max_results: int = ShapeBase.NOT_SET,
        next_token: str = ShapeBase.NOT_SET,
    ) -> shapes.GetDifferencesOutput:
        """
        Returns information about the differences in a valid commit specifier (such as a
        branch, tag, HEAD, commit ID or other fully qualified reference). Results can be
        limited to a specified path.
        """
        if _request is None:
            _params = {}
            if repository_name is not ShapeBase.NOT_SET:
                _params['repository_name'] = repository_name
            if after_commit_specifier is not ShapeBase.NOT_SET:
                _params['after_commit_specifier'] = after_commit_specifier
            if before_commit_specifier is not ShapeBase.NOT_SET:
                _params['before_commit_specifier'] = before_commit_specifier
            if before_path is not ShapeBase.NOT_SET:
                _params['before_path'] = before_path
            if after_path is not ShapeBase.NOT_SET:
                _params['after_path'] = after_path
            if max_results is not ShapeBase.NOT_SET:
                _params['max_results'] = max_results
            if next_token is not ShapeBase.NOT_SET:
                _params['next_token'] = next_token
            _request = shapes.GetDifferencesInput(**_params)
        paginator = self.get_paginator("get_differences").paginate(
            **_request.to_boto()
        )
        page_generator = (page for page in paginator)
        first_page = next(page_generator)
        result = shapes.GetDifferencesOutput.from_boto(first_page)
        result._page_iterator = page_generator
        return result

        return shapes.GetDifferencesOutput.from_boto(response)

    def get_merge_conflicts(
        self,
        _request: shapes.GetMergeConflictsInput = None,
        *,
        repository_name: str,
        destination_commit_specifier: str,
        source_commit_specifier: str,
        merge_option: typing.Union[str, shapes.MergeOptionTypeEnum],
    ) -> shapes.GetMergeConflictsOutput:
        """
        Returns information about merge conflicts between the before and after commit
        IDs for a pull request in a repository.
        """
        if _request is None:
            _params = {}
            if repository_name is not ShapeBase.NOT_SET:
                _params['repository_name'] = repository_name
            if destination_commit_specifier is not ShapeBase.NOT_SET:
                _params['destination_commit_specifier'
                       ] = destination_commit_specifier
            if source_commit_specifier is not ShapeBase.NOT_SET:
                _params['source_commit_specifier'] = source_commit_specifier
            if merge_option is not ShapeBase.NOT_SET:
                _params['merge_option'] = merge_option
            _request = shapes.GetMergeConflictsInput(**_params)
        response = self._boto_client.get_merge_conflicts(**_request.to_boto())

        return shapes.GetMergeConflictsOutput.from_boto(response)

    def get_pull_request(
        self,
        _request: shapes.GetPullRequestInput = None,
        *,
        pull_request_id: str,
    ) -> shapes.GetPullRequestOutput:
        """
        Gets information about a pull request in a specified repository.
        """
        if _request is None:
            _params = {}
            if pull_request_id is not ShapeBase.NOT_SET:
                _params['pull_request_id'] = pull_request_id
            _request = shapes.GetPullRequestInput(**_params)
        response = self._boto_client.get_pull_request(**_request.to_boto())

        return shapes.GetPullRequestOutput.from_boto(response)

    def get_repository(
        self,
        _request: shapes.GetRepositoryInput = None,
        *,
        repository_name: str,
    ) -> shapes.GetRepositoryOutput:
        """
        Returns information about a repository.

        The description field for a repository accepts all HTML characters and all valid
        Unicode characters. Applications that do not HTML-encode the description and
        display it in a web page could expose users to potentially malicious code. Make
        sure that you HTML-encode the description field in any application that uses
        this API to display the repository description on a web page.
        """
        if _request is None:
            _params = {}
            if repository_name is not ShapeBase.NOT_SET:
                _params['repository_name'] = repository_name
            _request = shapes.GetRepositoryInput(**_params)
        response = self._boto_client.get_repository(**_request.to_boto())

        return shapes.GetRepositoryOutput.from_boto(response)

    def get_repository_triggers(
        self,
        _request: shapes.GetRepositoryTriggersInput = None,
        *,
        repository_name: str,
    ) -> shapes.GetRepositoryTriggersOutput:
        """
        Gets information about triggers configured for a repository.
        """
        if _request is None:
            _params = {}
            if repository_name is not ShapeBase.NOT_SET:
                _params['repository_name'] = repository_name
            _request = shapes.GetRepositoryTriggersInput(**_params)
        response = self._boto_client.get_repository_triggers(
            **_request.to_boto()
        )

        return shapes.GetRepositoryTriggersOutput.from_boto(response)

    def list_branches(
        self,
        _request: shapes.ListBranchesInput = None,
        *,
        repository_name: str,
        next_token: str = ShapeBase.NOT_SET,
    ) -> shapes.ListBranchesOutput:
        """
        Gets information about one or more branches in a repository.
        """
        if _request is None:
            _params = {}
            if repository_name is not ShapeBase.NOT_SET:
                _params['repository_name'] = repository_name
            if next_token is not ShapeBase.NOT_SET:
                _params['next_token'] = next_token
            _request = shapes.ListBranchesInput(**_params)
        paginator = self.get_paginator("list_branches").paginate(
            **_request.to_boto()
        )
        page_generator = (page for page in paginator)
        first_page = next(page_generator)
        result = shapes.ListBranchesOutput.from_boto(first_page)
        result._page_iterator = page_generator
        return result

        return shapes.ListBranchesOutput.from_boto(response)

    def list_pull_requests(
        self,
        _request: shapes.ListPullRequestsInput = None,
        *,
        repository_name: str,
        author_arn: str = ShapeBase.NOT_SET,
        pull_request_status: typing.
        Union[str, shapes.PullRequestStatusEnum] = ShapeBase.NOT_SET,
        next_token: str = ShapeBase.NOT_SET,
        max_results: int = ShapeBase.NOT_SET,
    ) -> shapes.ListPullRequestsOutput:
        """
        Returns a list of pull requests for a specified repository. The return list can
        be refined by pull request status or pull request author ARN.
        """
        if _request is None:
            _params = {}
            if repository_name is not ShapeBase.NOT_SET:
                _params['repository_name'] = repository_name
            if author_arn is not ShapeBase.NOT_SET:
                _params['author_arn'] = author_arn
            if pull_request_status is not ShapeBase.NOT_SET:
                _params['pull_request_status'] = pull_request_status
            if next_token is not ShapeBase.NOT_SET:
                _params['next_token'] = next_token
            if max_results is not ShapeBase.NOT_SET:
                _params['max_results'] = max_results
            _request = shapes.ListPullRequestsInput(**_params)
        paginator = self.get_paginator("list_pull_requests").paginate(
            **_request.to_boto()
        )
        page_generator = (page for page in paginator)
        first_page = next(page_generator)
        result = shapes.ListPullRequestsOutput.from_boto(first_page)
        result._page_iterator = page_generator
        return result

        return shapes.ListPullRequestsOutput.from_boto(response)

    def list_repositories(
        self,
        _request: shapes.ListRepositoriesInput = None,
        *,
        next_token: str = ShapeBase.NOT_SET,
        sort_by: typing.Union[str, shapes.SortByEnum] = ShapeBase.NOT_SET,
        order: typing.Union[str, shapes.OrderEnum] = ShapeBase.NOT_SET,
    ) -> shapes.ListRepositoriesOutput:
        """
        Gets information about one or more repositories.
        """
        if _request is None:
            _params = {}
            if next_token is not ShapeBase.NOT_SET:
                _params['next_token'] = next_token
            if sort_by is not ShapeBase.NOT_SET:
                _params['sort_by'] = sort_by
            if order is not ShapeBase.NOT_SET:
                _params['order'] = order
            _request = shapes.ListRepositoriesInput(**_params)
        paginator = self.get_paginator("list_repositories").paginate(
            **_request.to_boto()
        )
        page_generator = (page for page in paginator)
        first_page = next(page_generator)
        result = shapes.ListRepositoriesOutput.from_boto(first_page)
        result._page_iterator = page_generator
        return result

        return shapes.ListRepositoriesOutput.from_boto(response)

    def merge_pull_request_by_fast_forward(
        self,
        _request: shapes.MergePullRequestByFastForwardInput = None,
        *,
        pull_request_id: str,
        repository_name: str,
        source_commit_id: str = ShapeBase.NOT_SET,
    ) -> shapes.MergePullRequestByFastForwardOutput:
        """
        Closes a pull request and attempts to merge the source commit of a pull request
        into the specified destination branch for that pull request at the specified
        commit using the fast-forward merge option.
        """
        if _request is None:
            _params = {}
            if pull_request_id is not ShapeBase.NOT_SET:
                _params['pull_request_id'] = pull_request_id
            if repository_name is not ShapeBase.NOT_SET:
                _params['repository_name'] = repository_name
            if source_commit_id is not ShapeBase.NOT_SET:
                _params['source_commit_id'] = source_commit_id
            _request = shapes.MergePullRequestByFastForwardInput(**_params)
        response = self._boto_client.merge_pull_request_by_fast_forward(
            **_request.to_boto()
        )

        return shapes.MergePullRequestByFastForwardOutput.from_boto(response)

    def post_comment_for_compared_commit(
        self,
        _request: shapes.PostCommentForComparedCommitInput = None,
        *,
        repository_name: str,
        after_commit_id: str,
        content: str,
        before_commit_id: str = ShapeBase.NOT_SET,
        location: shapes.Location = ShapeBase.NOT_SET,
        client_request_token: str = ShapeBase.NOT_SET,
    ) -> shapes.PostCommentForComparedCommitOutput:
        """
        Posts a comment on the comparison between two commits.
        """
        if _request is None:
            _params = {}
            if repository_name is not ShapeBase.NOT_SET:
                _params['repository_name'] = repository_name
            if after_commit_id is not ShapeBase.NOT_SET:
                _params['after_commit_id'] = after_commit_id
            if content is not ShapeBase.NOT_SET:
                _params['content'] = content
            if before_commit_id is not ShapeBase.NOT_SET:
                _params['before_commit_id'] = before_commit_id
            if location is not ShapeBase.NOT_SET:
                _params['location'] = location
            if client_request_token is not ShapeBase.NOT_SET:
                _params['client_request_token'] = client_request_token
            _request = shapes.PostCommentForComparedCommitInput(**_params)
        response = self._boto_client.post_comment_for_compared_commit(
            **_request.to_boto()
        )

        return shapes.PostCommentForComparedCommitOutput.from_boto(response)

    def post_comment_for_pull_request(
        self,
        _request: shapes.PostCommentForPullRequestInput = None,
        *,
        pull_request_id: str,
        repository_name: str,
        before_commit_id: str,
        after_commit_id: str,
        content: str,
        location: shapes.Location = ShapeBase.NOT_SET,
        client_request_token: str = ShapeBase.NOT_SET,
    ) -> shapes.PostCommentForPullRequestOutput:
        """
        Posts a comment on a pull request.
        """
        if _request is None:
            _params = {}
            if pull_request_id is not ShapeBase.NOT_SET:
                _params['pull_request_id'] = pull_request_id
            if repository_name is not ShapeBase.NOT_SET:
                _params['repository_name'] = repository_name
            if before_commit_id is not ShapeBase.NOT_SET:
                _params['before_commit_id'] = before_commit_id
            if after_commit_id is not ShapeBase.NOT_SET:
                _params['after_commit_id'] = after_commit_id
            if content is not ShapeBase.NOT_SET:
                _params['content'] = content
            if location is not ShapeBase.NOT_SET:
                _params['location'] = location
            if client_request_token is not ShapeBase.NOT_SET:
                _params['client_request_token'] = client_request_token
            _request = shapes.PostCommentForPullRequestInput(**_params)
        response = self._boto_client.post_comment_for_pull_request(
            **_request.to_boto()
        )

        return shapes.PostCommentForPullRequestOutput.from_boto(response)

    def post_comment_reply(
        self,
        _request: shapes.PostCommentReplyInput = None,
        *,
        in_reply_to: str,
        content: str,
        client_request_token: str = ShapeBase.NOT_SET,
    ) -> shapes.PostCommentReplyOutput:
        """
        Posts a comment in reply to an existing comment on a comparison between commits
        or a pull request.
        """
        if _request is None:
            _params = {}
            if in_reply_to is not ShapeBase.NOT_SET:
                _params['in_reply_to'] = in_reply_to
            if content is not ShapeBase.NOT_SET:
                _params['content'] = content
            if client_request_token is not ShapeBase.NOT_SET:
                _params['client_request_token'] = client_request_token
            _request = shapes.PostCommentReplyInput(**_params)
        response = self._boto_client.post_comment_reply(**_request.to_boto())

        return shapes.PostCommentReplyOutput.from_boto(response)

    def put_file(
        self,
        _request: shapes.PutFileInput = None,
        *,
        repository_name: str,
        branch_name: str,
        file_content: typing.Any,
        file_path: str,
        file_mode: typing.Union[str, shapes.FileModeTypeEnum] = ShapeBase.
        NOT_SET,
        parent_commit_id: str = ShapeBase.NOT_SET,
        commit_message: str = ShapeBase.NOT_SET,
        name: str = ShapeBase.NOT_SET,
        email: str = ShapeBase.NOT_SET,
    ) -> shapes.PutFileOutput:
        """
        Adds or updates a file in a branch in an AWS CodeCommit repository, and
        generates a commit for the addition in the specified branch.
        """
        if _request is None:
            _params = {}
            if repository_name is not ShapeBase.NOT_SET:
                _params['repository_name'] = repository_name
            if branch_name is not ShapeBase.NOT_SET:
                _params['branch_name'] = branch_name
            if file_content is not ShapeBase.NOT_SET:
                _params['file_content'] = file_content
            if file_path is not ShapeBase.NOT_SET:
                _params['file_path'] = file_path
            if file_mode is not ShapeBase.NOT_SET:
                _params['file_mode'] = file_mode
            if parent_commit_id is not ShapeBase.NOT_SET:
                _params['parent_commit_id'] = parent_commit_id
            if commit_message is not ShapeBase.NOT_SET:
                _params['commit_message'] = commit_message
            if name is not ShapeBase.NOT_SET:
                _params['name'] = name
            if email is not ShapeBase.NOT_SET:
                _params['email'] = email
            _request = shapes.PutFileInput(**_params)
        response = self._boto_client.put_file(**_request.to_boto())

        return shapes.PutFileOutput.from_boto(response)

    def put_repository_triggers(
        self,
        _request: shapes.PutRepositoryTriggersInput = None,
        *,
        repository_name: str,
        triggers: typing.List[shapes.RepositoryTrigger],
    ) -> shapes.PutRepositoryTriggersOutput:
        """
        Replaces all triggers for a repository. This can be used to create or delete
        triggers.
        """
        if _request is None:
            _params = {}
            if repository_name is not ShapeBase.NOT_SET:
                _params['repository_name'] = repository_name
            if triggers is not ShapeBase.NOT_SET:
                _params['triggers'] = triggers
            _request = shapes.PutRepositoryTriggersInput(**_params)
        response = self._boto_client.put_repository_triggers(
            **_request.to_boto()
        )

        return shapes.PutRepositoryTriggersOutput.from_boto(response)

    def test_repository_triggers(
        self,
        _request: shapes.TestRepositoryTriggersInput = None,
        *,
        repository_name: str,
        triggers: typing.List[shapes.RepositoryTrigger],
    ) -> shapes.TestRepositoryTriggersOutput:
        """
        Tests the functionality of repository triggers by sending information to the
        trigger target. If real data is available in the repository, the test will send
        data from the last commit. If no data is available, sample data will be
        generated.
        """
        if _request is None:
            _params = {}
            if repository_name is not ShapeBase.NOT_SET:
                _params['repository_name'] = repository_name
            if triggers is not ShapeBase.NOT_SET:
                _params['triggers'] = triggers
            _request = shapes.TestRepositoryTriggersInput(**_params)
        response = self._boto_client.test_repository_triggers(
            **_request.to_boto()
        )

        return shapes.TestRepositoryTriggersOutput.from_boto(response)

    def update_comment(
        self,
        _request: shapes.UpdateCommentInput = None,
        *,
        comment_id: str,
        content: str,
    ) -> shapes.UpdateCommentOutput:
        """
        Replaces the contents of a comment.
        """
        if _request is None:
            _params = {}
            if comment_id is not ShapeBase.NOT_SET:
                _params['comment_id'] = comment_id
            if content is not ShapeBase.NOT_SET:
                _params['content'] = content
            _request = shapes.UpdateCommentInput(**_params)
        response = self._boto_client.update_comment(**_request.to_boto())

        return shapes.UpdateCommentOutput.from_boto(response)

    def update_default_branch(
        self,
        _request: shapes.UpdateDefaultBranchInput = None,
        *,
        repository_name: str,
        default_branch_name: str,
    ) -> None:
        """
        Sets or changes the default branch name for the specified repository.

        If you use this operation to change the default branch name to the current
        default branch name, a success message is returned even though the default
        branch did not change.
        """
        if _request is None:
            _params = {}
            if repository_name is not ShapeBase.NOT_SET:
                _params['repository_name'] = repository_name
            if default_branch_name is not ShapeBase.NOT_SET:
                _params['default_branch_name'] = default_branch_name
            _request = shapes.UpdateDefaultBranchInput(**_params)
        response = self._boto_client.update_default_branch(**_request.to_boto())

    def update_pull_request_description(
        self,
        _request: shapes.UpdatePullRequestDescriptionInput = None,
        *,
        pull_request_id: str,
        description: str,
    ) -> shapes.UpdatePullRequestDescriptionOutput:
        """
        Replaces the contents of the description of a pull request.
        """
        if _request is None:
            _params = {}
            if pull_request_id is not ShapeBase.NOT_SET:
                _params['pull_request_id'] = pull_request_id
            if description is not ShapeBase.NOT_SET:
                _params['description'] = description
            _request = shapes.UpdatePullRequestDescriptionInput(**_params)
        response = self._boto_client.update_pull_request_description(
            **_request.to_boto()
        )

        return shapes.UpdatePullRequestDescriptionOutput.from_boto(response)

    def update_pull_request_status(
        self,
        _request: shapes.UpdatePullRequestStatusInput = None,
        *,
        pull_request_id: str,
        pull_request_status: typing.Union[str, shapes.PullRequestStatusEnum],
    ) -> shapes.UpdatePullRequestStatusOutput:
        """
        Updates the status of a pull request.
        """
        if _request is None:
            _params = {}
            if pull_request_id is not ShapeBase.NOT_SET:
                _params['pull_request_id'] = pull_request_id
            if pull_request_status is not ShapeBase.NOT_SET:
                _params['pull_request_status'] = pull_request_status
            _request = shapes.UpdatePullRequestStatusInput(**_params)
        response = self._boto_client.update_pull_request_status(
            **_request.to_boto()
        )

        return shapes.UpdatePullRequestStatusOutput.from_boto(response)

    def update_pull_request_title(
        self,
        _request: shapes.UpdatePullRequestTitleInput = None,
        *,
        pull_request_id: str,
        title: str,
    ) -> shapes.UpdatePullRequestTitleOutput:
        """
        Replaces the title of a pull request.
        """
        if _request is None:
            _params = {}
            if pull_request_id is not ShapeBase.NOT_SET:
                _params['pull_request_id'] = pull_request_id
            if title is not ShapeBase.NOT_SET:
                _params['title'] = title
            _request = shapes.UpdatePullRequestTitleInput(**_params)
        response = self._boto_client.update_pull_request_title(
            **_request.to_boto()
        )

        return shapes.UpdatePullRequestTitleOutput.from_boto(response)

    def update_repository_description(
        self,
        _request: shapes.UpdateRepositoryDescriptionInput = None,
        *,
        repository_name: str,
        repository_description: str = ShapeBase.NOT_SET,
    ) -> None:
        """
        Sets or changes the comment or description for a repository.

        The description field for a repository accepts all HTML characters and all valid
        Unicode characters. Applications that do not HTML-encode the description and
        display it in a web page could expose users to potentially malicious code. Make
        sure that you HTML-encode the description field in any application that uses
        this API to display the repository description on a web page.
        """
        if _request is None:
            _params = {}
            if repository_name is not ShapeBase.NOT_SET:
                _params['repository_name'] = repository_name
            if repository_description is not ShapeBase.NOT_SET:
                _params['repository_description'] = repository_description
            _request = shapes.UpdateRepositoryDescriptionInput(**_params)
        response = self._boto_client.update_repository_description(
            **_request.to_boto()
        )

    def update_repository_name(
        self,
        _request: shapes.UpdateRepositoryNameInput = None,
        *,
        old_name: str,
        new_name: str,
    ) -> None:
        """
        Renames a repository. The repository name must be unique across the calling AWS
        account. In addition, repository names are limited to 100 alphanumeric, dash,
        and underscore characters, and cannot include certain characters. The suffix
        ".git" is prohibited. For a full description of the limits on repository names,
        see [Limits](http://docs.aws.amazon.com/codecommit/latest/userguide/limits.html)
        in the AWS CodeCommit User Guide.
        """
        if _request is None:
            _params = {}
            if old_name is not ShapeBase.NOT_SET:
                _params['old_name'] = old_name
            if new_name is not ShapeBase.NOT_SET:
                _params['new_name'] = new_name
            _request = shapes.UpdateRepositoryNameInput(**_params)
        response = self._boto_client.update_repository_name(
            **_request.to_boto()
        )
