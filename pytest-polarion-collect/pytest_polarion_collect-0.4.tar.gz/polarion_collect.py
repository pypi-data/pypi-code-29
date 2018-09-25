# -*- coding: utf-8 -*-
"""pytest plugin for collecting polarion test cases data"""

from __future__ import print_function

import datetime
import json
import re

import pytest
import six

from polarion_docstrings import configuration
from polarion_docstrings import parser as docparser

DUPLICATES = "duplicates.log"
TESTCASES = "test_case_import.json"
TESTRESULTS = "test_run_import.json"

STEP_NUMBERING = re.compile(r"[0-9]+[.)]? ?")
TIMESTAMP = "{:%Y%m%d%H%M%S}".format(datetime.datetime.now())


def get_conf():
    """Loads configuration."""
    tools_cfg = configuration.get_config()
    known_fields = tools_cfg["docstrings"]["known_fields"]
    cfg = {"default_fields": {key: value for key, value in known_fields.items() if value}}
    cfg.update(tools_cfg)
    return cfg


def pytest_addoption(parser):
    """Adds command line options."""
    group = parser.getgroup("Polarion: options related to test cases data collection")
    group.addoption(
        "--generate-jsons",
        action="store_true",
        default=False,
        help="generate JSON files with test cases data",
    )
    group.addoption(
        "--jsons-no-blacklist",
        action="store_true",
        default=False,
        help="don't filter test cases using the built-in blacklist",
    )


def extract_fixtures_values(item):
    """Extracts names and values of all the fixtures that the test has.

    Args:
        item: py.test test item
    Returns:
        :py:class:`dict` with fixtures and their values.
    """
    try:
        return item.callspec.params.copy()  # protect against accidential manipulation of the spec
    except AttributeError:
        # Some of the test items do not have callspec, so fall back
        # This can cause some problems if the fixtures are used in the guards in this case, but
        # that will tell use where is the problem and we can then find it out properly.
        return {}


def get_unicode_str(obj):
    """Makes sure obj is a unicode string."""
    if isinstance(obj, six.text_type):
        return obj
    if isinstance(obj, six.binary_type):
        return obj.decode("utf-8", errors="ignore")
    return six.text_type(obj)


def _get_docstring(item):
    try:
        return get_unicode_str(item.function.__doc__)
    except (AttributeError, UnicodeDecodeError):
        return ""


def _get_caselevel(item, parsed_docstring, caselevels):
    caselevel = parsed_docstring.get("caselevel")
    if caselevel and caselevel.value:
        return caselevel.value

    try:
        tier = int(item.get_marker("tier").args[0])
        tier_id = caselevels[tier]
    except (ValueError, AttributeError):
        tier_id = caselevels[0]

    return tier_id


def _get_caseautomation(item, parsed_docstring):
    if item.get_marker("manual"):
        return "manualonly"

    caseautomation = parsed_docstring.get("caseautomation")
    if caseautomation and caseautomation.value:
        return caseautomation.value

    return "automated"


def _get_automation_script(conf, item):
    # The master here should probably link the latest "commit" eventually
    return "{0}/blob/master/{1}#L{2}".format(
        conf["repo_address"], item.location[0], item.function.__code__.co_firstlineno
    )


def _get_description(item, docstring, automation_script):
    try:
        description = docparser.strip_polarion_data(docstring)
    except ValueError as err:
        print("Cannot parse the description of {}: {}".format(item.location[2], err))
        description = ""

    if automation_script:
        # Description with timestamp and link to test case source.
        # The timestamp will not be visible in Polarion, but will cause Polarion
        # to update the "Updated" field even when there's no other change.
        description = '{0}<br id="{1}"/><br/><a href="{2}">Test Source</a>'.format(
            description, TIMESTAMP, automation_script
        )

    return description


def _get_steps_and_results(parsed_docstring):
    if not parsed_docstring.get("testSteps"):
        return None

    test_steps = []
    expected_results = []

    steps = parsed_docstring.get("testSteps")
    results = parsed_docstring.get("expectedResults")
    steps = [STEP_NUMBERING.sub("", s.value) for s in steps]
    results = [STEP_NUMBERING.sub("", r.value) for r in results]

    for index, step in enumerate(steps):
        test_steps.append(step)

        try:
            result = results[index]
        except IndexError:
            result = ""
        expected_results.append(result)

    return test_steps, expected_results


def _get_assignee(parsed_docstring):
    assignee = parsed_docstring.get("assignee")
    if assignee and assignee.value:
        return assignee.value
    return None


def _get_initial_estimate(parsed_docstring):
    initial_estimate = parsed_docstring.get("initialEstimate")
    if initial_estimate and initial_estimate.value:
        return initial_estimate.value
    return None


def _get_requirement_name(item):
    try:
        return [item.get_marker("requirement").args[0]]
    except AttributeError:
        return None


def _get_linked_items(parsed_docstring):
    linked_items = parsed_docstring.get("linkedWorkItems")
    if linked_items and linked_items.value:
        return linked_items.value.split(",")
    return None


def get_testcase_data(conf, test_name, tests, processed_tests, item):
    """Gets data for single test case entry."""
    if test_name in processed_tests:
        return
    processed_tests.append(test_name)

    testcase_data = conf["default_fields"].copy()

    docstring = _get_docstring(item)
    parsed_docstring = docparser.parse_docstring(docstring) or {}

    testcase_data["caseautomation"] = _get_caseautomation(item, parsed_docstring)

    if testcase_data["caseautomation"] == "automated":
        testcase_data["automation_script"] = _get_automation_script(conf, item)

    testcase_title = parsed_docstring.get("title")
    testcase_title = testcase_title.value if testcase_title else test_name
    testcase_data["title"] = testcase_title

    test_steps = _get_steps_and_results(parsed_docstring)
    if test_steps:
        testcase_data["testSteps"], testcase_data["expectedResults"] = test_steps

    for field, record in parsed_docstring.items():
        if field in conf["docstrings"]["custom_fields"]:
            testcase_data[field] = record.value

    testcase_data["id"] = testcase_title
    testcase_data["assignee-id"] = _get_assignee(parsed_docstring)
    testcase_data["caselevel"] = _get_caselevel(
        item, parsed_docstring, conf["docstrings"]["valid_values"]["caselevel"]
    )
    testcase_data["description"] = _get_description(
        item, docstring, testcase_data.get("automation_script")
    )
    testcase_data["id"] = test_name
    testcase_data["initial-estimate"] = _get_initial_estimate(parsed_docstring)
    testcase_data["linked-items"] = _get_requirement_name(item) or _get_linked_items(
        parsed_docstring
    )
    testcase_data["params"] = list(extract_fixtures_values(item).keys()) or None

    tests.append(testcase_data)


def _get_name(obj):
    if hasattr(obj, "_param_name"):
        # pylint: disable=protected-access
        return obj._param_name
    elif hasattr(obj, "name"):
        return obj.name
    return str(obj)


def get_testresult_data(test_name, tests, processed_tests, item):
    """Gets data for single test result entry."""
    if test_name in processed_tests:
        return
    processed_tests.append(test_name)

    testresult_data = {"title": test_name, "verdict": "waiting"}

    try:
        params = item.callspec.params
    except AttributeError:
        params = {}

    parameters = {p: _get_name(v) for p, v in params.items()}
    if parameters:
        testresult_data["params"] = parameters

    tests.append(testresult_data)


def gen_duplicates_log(items):
    """Generates log file containing non-unique test cases names."""
    test_param = re.compile(r"\[.*\]")
    names = {}
    duplicates = set()

    for item in items:
        name = test_param.sub("", item.location[2])
        path = item.location[0]

        name_record = names.get(name)
        if name_record:
            name_record.add(path)
        else:
            names[name] = {path}

    for name, paths in names.items():
        if len(paths) > 1:
            duplicates.add(name)

    with open(DUPLICATES, "w") as outfile:
        for test in sorted(duplicates):
            outfile.write("{}\n".format(test))


def write_json(data_list, out_file):
    """Outputs data as JSON."""
    data_dict = {"results": data_list}
    with open(out_file, "w") as out:
        json.dump(data_dict, out, indent=4)


def is_whitelisted(whitelist, blacklist, nodeid):
    """Checks if the nodeid is whitelisted."""
    if whitelist and whitelist.search(nodeid):
        return True
    if blacklist and blacklist.search(nodeid):
        return False
    return True


@pytest.mark.trylast
def pytest_collection_modifyitems(config, items):
    """Generates the JSON files using collected items."""
    if not (config.getoption("generate_jsons") and config.getoption("--collect-only")):
        return

    gen_duplicates_log(items)

    no_blacklist = config.getoption("jsons_no_blacklist")

    tc_processed = []
    testcases = []
    tr_processed = []
    testresults = []

    conf = get_conf()

    compiled_whitelist = None
    compiled_blacklist = None
    if conf.get("whitelisted_tests"):
        compiled_whitelist = re.compile("(" + ")|(".join(conf.get("whitelisted_tests")) + ")")
    if conf.get("blacklisted_tests"):
        compiled_blacklist = re.compile("(" + ")|(".join(conf.get("blacklisted_tests")) + ")")

    tests_relative_path = conf.get("tests_relative_path", "tests")

    for item in items:
        if tests_relative_path not in item.nodeid:
            continue
        if not (
            no_blacklist or is_whitelisted(compiled_whitelist, compiled_blacklist, item.nodeid)
        ):
            continue

        name = item.location[2]

        get_testcase_data(conf, name, testcases, tc_processed, item)
        get_testresult_data(name, testresults, tr_processed, item)

    write_json(testcases, TESTCASES)
    write_json(testresults, TESTRESULTS)
