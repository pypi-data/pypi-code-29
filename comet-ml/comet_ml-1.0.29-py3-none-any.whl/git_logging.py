# -*- coding: utf-8 -*-
# *******************************************************
#   ____                     _               _
#  / ___|___  _ __ ___   ___| |_   _ __ ___ | |
# | |   / _ \| '_ ` _ \ / _ \ __| | '_ ` _ \| |
# | |__| (_) | | | | | |  __/ |_ _| | | | | | |
#  \____\___/|_| |_| |_|\___|\__(_)_| |_| |_|_|
#
#  Sign up for free at http://www.comet.ml
#  Copyright (C) 2015-2019 Comet ML INC
#  This file can not be copied and/or distributed without the express
#  permission of Comet ML Inc.
# *******************************************************

"""
This module contains git related functions

"""

import logging
import os.path
import sys

import dulwich.errors
import dulwich.porcelain
import dulwich.repo
from six.moves.urllib.parse import urlparse

LOGGER = logging.getLogger(__name__)


def _patched_path_to_tree_path(repopath, path):
    """Convert a path to a path usable in e.g. an index.
    :param repopath: Repository
    :param path: A path
    :return: A path formatted for use in e.g. an index
    """
    if os.path.isabs(path):
        path = os.path.relpath(path, repopath)
    if os.path.sep != "/":
        path = path.replace(os.path.sep, "/")
    return path.encode(sys.getfilesystemencoding())


def to_utf8(str_or_bytes):
    if hasattr(str_or_bytes, "decode"):
        return str_or_bytes.decode("utf-8", errors="replace")

    return str_or_bytes


def get_user(repo):
    """ Retrieve the configured user from a dulwich git repository
    """
    try:
        # The user name might not be valid UTF-8
        return to_utf8(repo.get_config_stack().get("user", "name"))

    except KeyError:
        return None


def get_root(repo):
    """ Retrieve the hash of the repo root to uniquely identify the git
    repository
    """

    # Check if the repository is empty
    if len(repo.get_refs()) == 0:
        return None

    # Get walker needs at least the HEAD ref to be present
    walker = repo.get_walker()

    entry = None

    # Iterate on the lazy iterator to get to the last one
    for entry in walker:
        pass

    assert entry is not None

    # SHA should always be valid utf-8
    return to_utf8(entry.commit.id)


def get_branch(repo):
    """ Retrieve the current branch of a dulwich repository
    """
    refs = repo.get_refs()

    # Check if the repository is empty
    if len(repo.get_refs()) == 0:
        return None

    head = repo.head()

    for ref, sha in refs.items():
        if sha == head and ref != b"HEAD":
            return to_utf8(ref)


def get_git_commit(repo):
    try:
        # SHA should always be valid utf-8
        return to_utf8(repo.head())

    except KeyError:
        return None


def git_status(repo):
    try:
        # Monkey-patch a dulwich method, see
        # https://github.com/dulwich/dulwich/pull/601 for an explanation why
        original = dulwich.porcelain.path_to_tree_path
        dulwich.porcelain.path_to_tree_path = _patched_path_to_tree_path

        status = dulwich.porcelain.status(repo)

        staged = {
            key: [to_utf8(path) for path in items]
            for (key, items) in status.staged.items()
        }
        unstaged = [to_utf8(path) for path in status.unstaged]
        untracked = [to_utf8(path) for path in status.untracked]

        return {"staged": staged, "unstaged": unstaged, "untracked": untracked}

    finally:
        dulwich.porcelain.path_to_tree_path = original


def get_origin_url(repo):
    repo_config = repo.get_config()
    try:
        # The origin url might not be valid UTF-8
        return to_utf8(repo_config.get((b"remote", b"origin"), "url"))

    except KeyError:
        return None


def get_repo_name(origin_url):
    if origin_url is None:
        return None

    # First parse the url to get rid of possible HTTP comments or arguments
    parsed_url = urlparse(origin_url)
    # Remove potential leading /
    path = parsed_url.path.rstrip("/")
    repo_name = path.split("/")[-1]

    # Remove potential leading .git
    if repo_name.endswith(".git"):
        repo_name = repo_name[:-4]
    return repo_name


def find_git_repo(repo_path):
    # Early-exit if repo_path is repo root
    try:
        return dulwich.repo.Repo(repo_path)

    except dulwich.errors.NotGitRepository:
        pass

    path = repo_path
    while path:
        parent_path = os.path.dirname(path)
        # Avoid infinite loop
        if parent_path == path:
            break

        path = parent_path
        try:
            return dulwich.repo.Repo(path)

        except dulwich.errors.NotGitRepository:
            pass


def get_git_metadata(path):
    # First find the repo
    repo = find_git_repo(path)

    if not repo:
        return None

    origin = get_origin_url(repo)
    repo_name = get_repo_name(origin)

    return {
        "user": get_user(repo),
        "root": get_root(repo),
        "branch": get_branch(repo),
        "parent": get_git_commit(repo),
        "status": git_status(repo),
        "origin": origin,
        "repo_name": repo_name,
    }
