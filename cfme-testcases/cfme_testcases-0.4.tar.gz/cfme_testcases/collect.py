# -*- coding: utf-8 -*-
"""
Run pytest --collect-only and generate JSONs.
"""

from __future__ import absolute_import, unicode_literals

import logging
import os
import subprocess
import sys

from cfme_testcases import consts
from cfme_testcases.exceptions import TestcasesException

# pylint: disable=invalid-name
logger = logging.getLogger(__name__)


_JSON_FILES = (consts.TEST_CASE_JSON, consts.TEST_RUN_JSON)


def _check_environment(tests_path):
    # check that launched in tests repo
    if not os.path.exists(tests_path):
        raise TestcasesException("Not running in tests repo")
    # check that running in virtualenv
    if not hasattr(sys, "real_prefix"):
        raise TestcasesException("Not running in virtual environment")


def _cleanup():
    for fname in _JSON_FILES:
        try:
            os.remove(fname)
        except OSError:
            pass


def run_pytest(config):
    """Runs the pytest command."""
    pytest_retval = None
    _check_environment(config.get("tests_relative_path"))
    _cleanup()

    pytest_cmd = config.get("pytest_collect")
    pytest_args = pytest_cmd.split(" ")

    logger.info("Generating the JSONs using '%s'", pytest_cmd)
    with open(os.devnull, "w") as devnull:
        pytest_proc = subprocess.Popen(pytest_args, stdout=devnull, stderr=devnull)
        try:
            pytest_retval = pytest_proc.wait()
        # pylint: disable=broad-except
        except Exception:
            try:
                pytest_proc.terminate()
            except OSError:
                pass
            pytest_proc.wait()
            return None

    missing_files = []
    for fname in _JSON_FILES:
        if not os.path.exists(fname):
            missing_files.append(fname)
    if missing_files:
        raise TestcasesException(
            "The JSON files {} were not generated".format(" and ".join(missing_files))
        )

    return pytest_retval
