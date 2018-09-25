# -*- coding: utf-8 -*-
"""
Create new testrun and upload missing testcases using Polarion Importers.
"""

from __future__ import absolute_import, unicode_literals

import logging
import os
import threading

from cfme_testcases import cli_utils, consts, gen_xmls, svn_testcases
from cfme_testcases.exceptions import NothingToDoException, TestcasesException
from dump2polarion import parselogs, properties, submit
from dump2polarion import utils as d2p_utils

# pylint: disable=invalid-name
logger = logging.getLogger(__name__)


def get_all_testcases(xml_root):
    """Gets all testcases from XML."""
    if xml_root.tag != "testcases":
        raise TestcasesException("XML file is not in expected format")

    testcase_instances = xml_root.findall("testcase")
    # Expect that in ID is the value we want.
    # In case of "lookup-method: name" it's test case title.
    attr = "id"

    for testcase in testcase_instances:
        tc_id = testcase.get(attr)
        if tc_id:
            yield tc_id


def get_testsuites_xml_root(args, config, testsuites, testsuites_transform_func=None):
    """Returns content of XML files for importers."""
    if not args.testrun_id:
        raise TestcasesException("The testrun id was not specified")

    testsuites_str = gen_xmls.gen_testsuites_xml_str(
        testsuites, args.testrun_id, config, testsuites_transform_func
    )
    testsuites_root = d2p_utils.get_xml_root_from_str(testsuites_str)

    return testsuites_root


def get_testcases_xml_root(config, requirements_mapping, testcases, testcases_transform_func=None):
    """Returns content of XML files for importers."""
    testcases_str = gen_xmls.gen_testcases_xml_str(
        testcases, requirements_mapping, config, testcases_transform_func
    )
    testcases_root = d2p_utils.get_xml_root_from_str(testcases_str)

    return testcases_root


def get_init_logname(args):
    """Returns filename of the message bus log file."""
    if args.job_log:
        job_log = args.job_log
    else:
        job_log = "init-job-{}.log".format(cli_utils.get_filename_str(args))
        job_log = os.path.join(args.output_dir or "", job_log)
    return job_log


def initial_submit(args, submit_args, config, testsuites_root, log):
    """Submits XML to Polarion and saves the log file returned by the message bus."""
    if os.path.isfile(log) and not args.testrun_init:
        # log file already exists, no need to generate one
        return
    elif args.no_submit:
        raise NothingToDoException(
            "Instructed not to submit and as the import log is missing, "
            "there's nothing more to do"
        )

    if args.testrun_init:
        # we want to init new test run
        xml_root = testsuites_root
    else:
        # we want to just get the log file without changing anything
        xml_root = testsuites_root
        properties.set_dry_run(xml_root)

    properties.remove_response_property(xml_root)

    if args.output_dir:
        init_file = cli_utils.get_import_file_name(
            args, consts.TEST_RUN_XML, args.output_dir, "init"
        )
        d2p_utils.write_xml_root(xml_root, init_file)

    if not submit.submit_and_verify(xml_root=xml_root, config=config, log_file=log, **submit_args):
        raise TestcasesException("Failed to do the initial submit")


def _get_job_log(args, prefix):
    job_log = None
    if args.output_dir:
        job_log = "job-{}-{}.log".format(prefix, cli_utils.get_filename_str(args))
        job_log = os.path.join(args.output_dir, job_log)
    return job_log


def update_existing_testcases(args, submit_args, config, filtered_xmls):
    """Updates existing testcases in new thread."""
    output = []
    updating_testcases_t = None
    if not args.no_testcases_update and filtered_xmls.updated_testcases is not None:
        job_log = _get_job_log(args, "update")
        all_submit_args = dict(
            xml_root=filtered_xmls.updated_testcases, config=config, log_file=job_log, **submit_args
        )

        # run it in separate thread so we can continue without waiting
        # for the submit to finish
        def _run_submit(results, args_dict):
            retval = submit.submit_and_verify(**args_dict)
            results.append(retval)

        updating_testcases_t = threading.Thread(target=_run_submit, args=(output, all_submit_args))
        updating_testcases_t.start()

    return updating_testcases_t, output


def create_missing_testcases(args, submit_args, config, filtered_xmls):
    """Creates missing testcases in Polarion."""
    job_log = _get_job_log(args, "testcases")
    retval = submit.submit_and_verify(
        xml_root=filtered_xmls.missing_testcases, config=config, log_file=job_log, **submit_args
    )
    return retval


def add_missing_testcases_to_testrun(args, submit_args, config, filtered_xmls):
    """Adds missing testcases to testrun."""
    job_log = _get_job_log(args, "testrun")
    retval = submit.submit_and_verify(
        xml_root=filtered_xmls.missing_testsuites, config=config, log_file=job_log, **submit_args
    )
    return retval


def submit_filtered_xmls(args, submit_args, config, filtered_xmls):
    """Submits filtered XMLs to Polarion Importers."""
    if args.no_submit:
        return

    succeeded = []
    failed = []

    def _append_msg(retval, msg):
        if retval:
            succeeded.append(msg)
        else:
            failed.append(msg)

    # start update of existing testcases in separate thread
    updating_testcases_t, output = update_existing_testcases(
        args, submit_args, config, filtered_xmls
    )

    # create missing testcases in Polarion
    missing_testcases_submitted = False
    if filtered_xmls.missing_testcases is not None:
        missing_testcases_submitted = create_missing_testcases(
            args, submit_args, config, filtered_xmls
        )
        _append_msg(missing_testcases_submitted, "add missing testcases")

    # add missing testcases to testrun
    if (
        missing_testcases_submitted
        and not args.no_testrun_update
        and filtered_xmls.missing_testsuites is not None
    ):
        missing_testcases_added = add_missing_testcases_to_testrun(
            args, submit_args, config, filtered_xmls
        )
        _append_msg(missing_testcases_added, "update testrun")

    # wait for update of existing testcases to finish
    if updating_testcases_t:
        updating_testcases_t.join()
        _append_msg(output.pop(), "update existing testcases")

    if succeeded and failed:
        logger.info("SUCCEEDED to %s", ", ".join(succeeded))
    if failed:
        raise TestcasesException("FAILED to {}".format(", ".join(failed)))

    logger.info("DONE - RECORDS SUCCESSFULLY UPDATED!")


def get_missing_from_log(args, submit_args, config, testsuites_root):
    """Gets missing testcases from log file."""
    lookup_method = config.get("xunit_import_properties") or {}
    lookup_method = lookup_method.get("polarion-lookup-method") or "id"
    init_logname = get_init_logname(args)
    initial_submit(args, submit_args, config, testsuites_root, init_logname)
    parsed_log = parselogs.parse(init_logname)

    if lookup_method == "name":
        missing = [item.name for item in parsed_log.new_items]
    elif lookup_method == "custom":
        missing = [item.custom_id for item in parsed_log.new_items]
    elif lookup_method == "id":
        missing = [item.id for item in parsed_log.new_items]

    return missing


def get_missing_from_svn(config, all_testcases, repo_dir):
    """Gets missing testcases using SVN repo."""
    import_props = config.get("testcase_import_properties") or {}
    lookup_by = import_props.get("lookup-method") or "id"
    if lookup_by == "name":
        lookup_by = "title"
    elif lookup_by == "custom":
        lookup_by = import_props.get("polarion-custom-lookup-method-field-id") or "testCaseID"
    elif lookup_by == "id":
        lookup_by = "work_item_id"

    missing = svn_testcases.get_missing(repo_dir, all_testcases, lookup_by=lookup_by)
    return missing


def check_lookup_methods(config):
    """Checks that lookup methods are configured correctly."""
    xunit_props = config.get("xunit_import_properties") or {}
    xunit_lookup = xunit_props.get("polarion-lookup-method") or "id"

    testcase_props = config.get("testcase_import_properties") or {}
    testcase_lookup = testcase_props.get("lookup-method") or "id"

    if xunit_lookup != testcase_lookup:
        raise TestcasesException("The lookup-method for test cases and XUnit must be the same.")

    if xunit_lookup != "custom":
        return

    xunit_custom = xunit_props.get("polarion-custom-lookup-method-field-id")
    testcase_custom = testcase_props.get("polarion-custom-lookup-method-field-id")
    if xunit_custom != testcase_custom:
        raise TestcasesException(
            "The polarion-custom-lookup-method-field-id for test cases and XUnit must be the same."
        )


def get_missing(args, submit_args, config, testsuites_root, testcases_root):
    """Returns list of missing testcases."""
    check_lookup_methods(config)
    if args.use_svn and not args.testrun_init:
        all_testcases = get_all_testcases(testcases_root)
        missing = get_missing_from_svn(config, all_testcases, args.use_svn)
    else:
        missing = get_missing_from_log(args, submit_args, config, testsuites_root)
    return missing
