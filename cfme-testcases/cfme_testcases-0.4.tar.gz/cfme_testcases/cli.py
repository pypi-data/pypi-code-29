# -*- coding: utf-8 -*-
"""
Main CLI.
"""

from __future__ import absolute_import, unicode_literals

import argparse
import logging

from cfme_testcases import (
    cli_requirements,
    cli_testcases,
    cli_utils,
    collect,
    configuration,
    consts,
    filters,
)
from cfme_testcases.exceptions import Dump2PolarionException, NothingToDoException
from dump2polarion import utils as d2p_utils

# pylint: disable=invalid-name
logger = logging.getLogger(__name__)


def get_args(args=None):
    """Get command line arguments."""
    parser = argparse.ArgumentParser(description="cfme-testcases")
    parser.add_argument("-t", "--testrun-id", help="Polarion test run id")
    parser.add_argument("-o", "--output_dir", help="Directory for saving generated XML files")
    parser.add_argument(
        "-n", "--no-submit", action="store_true", help="Don't submit generated XML files"
    )
    parser.add_argument(
        "--testrun-init", action="store_true", help="Create and initialize new testrun"
    )
    parser.add_argument(
        "--trust-source",
        action="store_true",
        help="Source code is an authoritative source of data.",
    )
    parser.add_argument("--user", help="Username to use to submit to Polarion")
    parser.add_argument("--password", help="Password to use to submit to Polarion")
    parser.add_argument("--testcases", help="Path to JSON file with testcases")
    parser.add_argument("--testsuites", help="Path to XUnit JSON file with testsuites")
    parser.add_argument("--dump2polarion-config", help="Path to dump2polarion config YAML")
    parser.add_argument("--job-log", help="Path to an existing job log file")
    parser.add_argument("--dry-run", action="store_true", help="Dry run, don't update anything")
    parser.add_argument("--no-requirements", action="store_true", help="Don't import requirements")
    parser.add_argument(
        "--no-testrun-update", action="store_true", help="Don't add new testcases to testrun"
    )
    parser.add_argument(
        "--no-testcases-update", action="store_true", help="Don't update existing testcases"
    )
    parser.add_argument("--no-verify", action="store_true", help="Don't verify submission success")
    parser.add_argument(
        "--verify-timeout",
        type=int,
        default=600,
        metavar="SEC",
        help="How long to wait (in seconds) for verification of submission success"
        " (default: %(default)s)",
    )
    parser.add_argument(
        "--use-svn", metavar="SVN_REPO", help="Path to SVN repo with Polarion project"
    )
    parser.add_argument("--log-level", help="Set logging to specified level")
    return parser.parse_args(args)


def main(args=None):
    """Main function for cli."""
    args = get_args(args)
    submit_args = cli_utils.get_submit_args(args)

    d2p_utils.init_log(args.log_level)
    config = configuration.get_config(args.dump2polarion_config)

    testcases = args.testcases or consts.TEST_CASE_JSON
    testsuites = args.testsuites or consts.TEST_RUN_JSON

    try:
        if not (args.testcases and args.testsuites):
            collect.run_pytest(config)

        requirements_root = cli_requirements.get_requirements_xml_root(config)
        requirements_mapping = cli_requirements.get_requirements_mapping(
            args, submit_args, config, requirements_root
        )

        testsuite_root, testcases_root = cli_testcases.get_pytest_xmls(
            args, config, requirements_mapping, testcases=testcases, testsuites=testsuites
        )

        if args.use_svn:
            missing = cli_testcases.get_missing_from_svn(testcases_root, args.use_svn)
        else:
            missing = cli_testcases.get_missing_from_log(args, submit_args, config, testsuite_root)
        filtered_xmls = filters.get_filtered_xmls(
            testcases_root, testsuite_root, missing, trust_source=args.trust_source
        )

        cli_utils.save_generated_xmls(args, filtered_xmls, requirements_root)
        cli_testcases.submit_filtered_xmls(args, submit_args, config, filtered_xmls)
    except NothingToDoException as einfo:
        logger.info(einfo)
        return 0
    except Dump2PolarionException as err:
        logger.fatal(err)
        return 1
    return 0
