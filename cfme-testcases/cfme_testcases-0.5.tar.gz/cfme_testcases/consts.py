# -*- coding: utf-8 -*-
"""
Constants.
"""

from __future__ import unicode_literals

TEST_RUN_XML = "test_run_import.xml"
TEST_CASE_XML = "test_case_import.xml"
REQUIREMENTS_XML = "test_requirements_import.xml"
TEST_RUN_JSON = "test_run_import.json"
TEST_CASE_JSON = "test_case_import.json"
PYTEST_CMD = (
    "miq-runtest -qq --collect-only --long-running --perf --runxfail --include-manual "
    "--disablemetaplugins blockers --use-provider complete --generate-jsons"
)
