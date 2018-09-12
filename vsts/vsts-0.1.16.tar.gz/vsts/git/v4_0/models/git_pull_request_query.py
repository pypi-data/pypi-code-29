# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------
# Generated file, DO NOT EDIT
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------------------------

from msrest.serialization import Model


class GitPullRequestQuery(Model):
    """GitPullRequestQuery.

    :param queries: The query to perform
    :type queries: list of :class:`GitPullRequestQueryInput <git.v4_0.models.GitPullRequestQueryInput>`
    :param results: The results of the query
    :type results: list of {[GitPullRequest]}
    """

    _attribute_map = {
        'queries': {'key': 'queries', 'type': '[GitPullRequestQueryInput]'},
        'results': {'key': 'results', 'type': '[{[GitPullRequest]}]'}
    }

    def __init__(self, queries=None, results=None):
        super(GitPullRequestQuery, self).__init__()
        self.queries = queries
        self.results = results
