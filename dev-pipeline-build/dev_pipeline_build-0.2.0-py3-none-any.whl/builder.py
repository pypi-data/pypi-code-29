#!/usr/bin/python3
"""This modules aggregates the available builders that can be used."""

import os.path
import os

import devpipeline_core.toolsupport

import devpipeline_build


def _nothing_builder(current_config):
    # Unused variables
    del current_config

    class _NothingBuilder:
        def configure(self, src_dir, build_dir):
            # pylint: disable=missing-docstring
            pass

        def build(self, build_dir):
            # pylint: disable=missing-docstring
            pass

        def install(self, build_dir, path):
            # pylint: disable=missing-docstring
            pass

    return _NothingBuilder()


_NOTHING_BUILDER = (_nothing_builder, "Do nothing.")


def _make_builder(current_target):
    """
    Create and return a Builder for a component.

    Arguments
    component - The component the builder should be created for.
    """
    return devpipeline_core.toolsupport.tool_builder(
        current_target["current_config"], "build", devpipeline_build.BUILDERS,
        current_target)


def build_task(current_target):
    """
    Build a target.

    Arguments
    target - The target to build.
    """

    target = current_target["current_config"]
    build_path = target.get("dp.build_dir")
    if not os.path.exists(build_path):
        os.makedirs(build_path)
    builder = _make_builder(current_target)
    builder.configure(target.get("dp.src_dir"), build_path)
    builder.build(build_path)
    if "no_install" not in target:
        builder.install(build_path, path=target.get("install_path",
                                                    "install"))
