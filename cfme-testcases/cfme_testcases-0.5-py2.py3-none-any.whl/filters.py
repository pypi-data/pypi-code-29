# -*- coding: utf-8 -*-
"""
Filter missing testcases and testcases for update.
"""

from __future__ import absolute_import, unicode_literals

import copy
from collections import namedtuple

from cfme_testcases.exceptions import TestcasesException
from dump2polarion import properties

FilteredXMLs = namedtuple("FilteredXMLs", "missing_testcases missing_testsuites updated_testcases")


def get_missing_testcases(testcase_root, missing):
    """Gets testcases missing in Polarion."""
    xml_root = copy.deepcopy(testcase_root)

    if xml_root.tag != "testcases":
        raise TestcasesException("XML file is not in expected format")

    properties.remove_response_property(xml_root)

    testcase_instances = xml_root.findall("testcase")
    # Expect that in ID is the value we want.
    # In case of "lookup-method: name" it's test case title.
    attr = "id"

    for testcase in testcase_instances:
        tc_id = testcase.get(attr)
        if tc_id and tc_id not in missing:
            xml_root.remove(testcase)

    return xml_root


def get_missing_testsuites(testsuites_root, missing):
    """Gets testcases missing in testrun."""
    xml_root = copy.deepcopy(testsuites_root)

    if xml_root.tag != "testsuites":
        raise TestcasesException("XML file is not in expected format")

    properties.remove_response_property(xml_root)

    testsuite = xml_root.find("testsuite")
    testcase_parent = testsuite
    testcase_instances = testcase_parent.findall("testcase")
    attr = "name"

    for testcase in testcase_instances:
        # try to get test case ID first and if it fails, get name
        try:
            tc_id_prop = testcase.xpath('.//property[@name = "polarion-testcase-id"]')[0]
            tc_id = tc_id_prop.get("value")
        except IndexError:
            tc_id = testcase.get(attr)
        if tc_id and tc_id not in missing:
            testcase_parent.remove(testcase)

    testcase_parent.set("tests", str(len(testcase_parent.findall("testcase"))))
    testcase_parent.attrib.pop("errors", None)
    testcase_parent.attrib.pop("failures", None)
    testcase_parent.attrib.pop("skipped", None)

    return xml_root


def get_updated_testcases(testcase_root, missing, trust_source):
    """Gets testcases that will be updated in Polarion."""
    if missing is None:
        missing = []

    xml_root = copy.deepcopy(testcase_root)

    if xml_root.tag != "testcases":
        raise TestcasesException("XML file is not in expected format")

    properties.remove_response_property(xml_root)
    properties.set_lookup_method(xml_root, "name")

    testcase_instances = xml_root.findall("testcase")
    attr = "id"

    for testcase in testcase_instances:
        tc_id = testcase.get(attr)
        if tc_id is not None and tc_id in missing:
            xml_root.remove(testcase)
            continue

        if trust_source:
            continue

        # source not authoritative, don't update custom-fields
        cfields_parent = testcase.find("custom-fields")
        cfields_instances = cfields_parent.findall("custom-field")
        for field in cfields_instances:
            field_id = field.get("id")
            if field_id not in ("automation_script", "caseautomation"):
                cfields_parent.remove(field)

    if not xml_root.findall("testcase"):
        return None

    return xml_root


def get_filtered_xmls(testcases_root, testsuites_root, missing, trust_source=False):
    """Returns modified XMLs with testcases and testsuites."""
    missing_testcases, missing_testsuites = None, None
    if missing:
        missing_testcases = get_missing_testcases(testcases_root, missing)
        missing_testsuites = get_missing_testsuites(testsuites_root, missing)

    updated_testcases = get_updated_testcases(testcases_root, missing, trust_source=trust_source)

    return FilteredXMLs(missing_testcases, missing_testsuites, updated_testcases)
