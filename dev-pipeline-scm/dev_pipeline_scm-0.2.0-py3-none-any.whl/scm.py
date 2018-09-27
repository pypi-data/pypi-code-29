#!/usr/bin/python3
"""This module implements some helper functions and a simple SCM tool."""

import devpipeline_core.plugin
import devpipeline_core.toolsupport

import devpipeline_scm


def _nothing_scm(current_target):
    # Unused variables
    del current_target

    class _NothingScm:
        def checkout(self, repo_dir):
            # pylint: disable=missing-docstring
            pass

        def update(self, repo_dir):
            # pylint: disable=missing-docstring
            pass

    return _NothingScm()


_NOTHING_SCM = (_nothing_scm, "Do nothing.")


def _make_scm(current_target):
    """
    Create an Scm for a component.

    Arguments
    component - The component being operated on.
    """
    return devpipeline_core.toolsupport.tool_builder(
        current_target["current_config"], "scm",
        devpipeline_scm.SCMS, current_target)


def scm_task(current_target):
    """
    Update or a local checkout.

    Arguments
    target - The target to operate on.
    """
    scm = _make_scm(current_target)

    src_dir = current_target["current_config"].get("dp.src_dir")
    scm.checkout(src_dir)
    scm.update(src_dir)
