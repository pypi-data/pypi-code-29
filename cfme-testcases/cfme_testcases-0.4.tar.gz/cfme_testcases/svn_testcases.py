# -*- coding: utf-8 -*-
"""
Testcases data from Polarion SVN repo.
"""

from __future__ import absolute_import, unicode_literals

import logging
import os
import re

from cfme_testcases.exceptions import TestcasesException
from dump2polarion import svn_polarion

# pylint: disable=invalid-name
logger = logging.getLogger(__name__)


class PolarionTestcases(object):
    """Loads and access Polarion testcases."""

    TEST_PARAM = re.compile(r"\[.*\]")

    def __init__(self, repo_dir):
        self.repo_dir = os.path.expanduser(repo_dir)
        self.wi_cache = svn_polarion.WorkItemCache(self.repo_dir)
        self.available_testcases = {}

    def load_active_testcases(self):
        """Creates dict of all active testcase's names and ids."""
        cases = {}
        for item in self.wi_cache.get_all_items():
            if item.get("type") != "testcase":
                continue
            case_status = item.get("status")
            if not case_status or case_status == "inactive":
                continue
            case_title = item.get("title")
            case_id = item.get("work_item_id")
            try:
                cases[case_title].append(case_id)
            except KeyError:
                cases[case_title] = [case_id]

        self.available_testcases = cases

    def strip_parameters(self):
        """Removes parameters from test names."""
        filtered_testcases = {}
        for case_title, case_ids in self.available_testcases.items():
            param_strip = self.TEST_PARAM.sub("", case_title)
            try:
                filtered_testcases[param_strip].extend(case_ids)
            except KeyError:
                filtered_testcases[param_strip] = case_ids
        self.available_testcases = filtered_testcases

    def get_manual_testcases(self):
        """Returns dict of manual testcases names and corresponding IDs."""
        manual_testcases = {}
        for case_title, case_ids in self.available_testcases.items():
            for case_id in case_ids:
                case = self.wi_cache[case_id]
                caseautomation = case.get("caseautomation")
                if caseautomation == "automated":
                    continue
                try:
                    manual_testcases[case_title].append(case_id)
                except KeyError:
                    manual_testcases[case_title] = [case_id]
        return manual_testcases

    @staticmethod
    def _check_automation(case, should_be_automated):
        caseautomation = case.get("caseautomation")
        if should_be_automated:
            return caseautomation == "automated"
        return caseautomation != "automated"

    def get_by_name(self, testcase_name, is_automated=None, is_assigned=None):
        """Gets testcase by it's name."""
        for case_id in self.available_testcases[testcase_name]:
            case = self.wi_cache[case_id]
            tc_assigned = case.get("assignee")
            if is_assigned and not tc_assigned:
                continue
            if is_assigned is False and tc_assigned:
                continue
            if is_automated is None:
                return case
            if self._check_automation(case, is_automated):
                return case
        return None

    def get_by_id(self, testcase_id):
        """Gets testcase by it's id."""
        return self.wi_cache[testcase_id]

    def __getitem__(self, item):
        return self.available_testcases[item]

    def __iter__(self):
        return iter(self.available_testcases)

    def __len__(self):
        return len(self.available_testcases)

    def __contains__(self, item):
        return item in self.available_testcases

    def __repr__(self):
        return "<Testcases {}>".format(self.available_testcases)


def get_missing(repo_dir, testcase_names):
    """Gets set of testcases missing in Polarion."""
    polarion_testcases = PolarionTestcases(repo_dir)
    try:
        polarion_testcases.load_active_testcases()
    except Exception as err:
        raise TestcasesException(
            "Failed to load testcases from SVN repo {}: {}".format(repo_dir, err)
        )
    if not polarion_testcases:
        raise TestcasesException("No testcases loaded from SVN repo {}".format(repo_dir))
    missing = set(testcase_names) - set(polarion_testcases)
    return missing
