# -*- coding: utf-8 -*-
"""
Checks Polarion docstrings.
"""

from __future__ import absolute_import, print_function, unicode_literals

import os
import sys
from collections import namedtuple

from pkg_resources import get_distribution

from polarion_docstrings import configuration, parser

DocstringsError = namedtuple("DocstringsError", "lineno column message func")
FieldRecord = namedtuple("FieldRecord", "lineno column field")

MISSING_SECTION = "P665"
UNKNOWN_FIELD = "P666"
INVALID_VALUE = "P667"
MARKER_FIELD = "P668"
MISSING_FIELD = "P669"


def _validate(docstring_dict, key, valid_values):
    record = docstring_dict.get(key)
    if record is not None:
        return record.value in valid_values[key]
    return True


def _get_unknown_fields(docstring_dict, known_fields):
    unknown = [
        FieldRecord(docstring_dict[key].lineno, docstring_dict[key].column, key)
        for key in docstring_dict
        if key not in known_fields
    ]
    return unknown


def _get_invalid_fields(docstring_dict, valid_values):
    results = {key: _validate(docstring_dict, key, valid_values) for key in valid_values}
    invalid = [
        FieldRecord(docstring_dict[key].lineno, docstring_dict[key].column, key)
        for key, result in results.items()
        if not result
    ]
    return invalid


def _get_missing_fields(docstring_dict, required_keys):
    if not required_keys:
        return []
    missing = [key for key in required_keys if key not in docstring_dict]
    return missing


def _get_markers_fields(docstring_dict, marker_fields):
    if not marker_fields:
        return []
    markers = [
        FieldRecord(docstring_dict[key].lineno, docstring_dict[key].column, key)
        for key in marker_fields
        if key in docstring_dict
    ]
    return markers


def validate_docstring(docstring_dict, config):
    """Returns tuple with lists of problematic fields."""
    cfg_docstrings = config["docstrings"]
    unknown = _get_unknown_fields(docstring_dict, cfg_docstrings.get("known_fields"))
    invalid = _get_invalid_fields(docstring_dict, cfg_docstrings.get("valid_values"))
    missing = _get_missing_fields(docstring_dict, cfg_docstrings.get("required_fields"))
    markers = _get_markers_fields(docstring_dict, cfg_docstrings.get("marker_fields"))
    return unknown, invalid, missing, markers


def get_fields_errors(validated_docstring, docstring_dict, marker_fields, lineno=0, column=0):
    """Produces fields errors for the flake8 checker."""
    errors = []
    func = polarion_checks492
    unknown, invalid, missing, markers = validated_docstring

    for num, col, field in unknown:
        errors.append(
            DocstringsError(
                lineno + num, col, '{} Unknown field "{}"'.format(UNKNOWN_FIELD, field), func
            )
        )
    for num, col, field in invalid:
        errors.append(
            DocstringsError(
                lineno + num,
                col,
                '{} Invalid value "{}" of the "{}" field'.format(
                    INVALID_VALUE, docstring_dict[field].value, field
                ),
                func,
            )
        )
    for num, col, field in markers:
        errors.append(
            DocstringsError(
                lineno + num,
                col,
                '{} Field "{}" should be handled by the "{}" marker'.format(
                    MARKER_FIELD, field, marker_fields.get(field)
                ),
                func,
            )
        )
    for field in missing:
        errors.append(
            DocstringsError(
                lineno, column, '{} Missing required field "{}"'.format(MISSING_FIELD, field), func
            )
        )

    if errors:
        errors = sorted(errors, key=lambda tup: tup[0])
    return errors


def print_errors(errors):
    """Prints errors without using flake8."""
    for err in errors:
        print("line: {}:{}: {}".format(err.lineno, err.column, err.message), file=sys.stderr)


def check_docstrings(docstrings, config):
    """Runs checks on each docstring."""
    errors = []
    for record in docstrings:
        if record.value:
            valdoc = validate_docstring(record.value, config)
            errors.extend(
                get_fields_errors(
                    valdoc,
                    record.value,
                    config["docstrings"].get("marker_fields") or {},
                    record.lineno,
                    record.column,
                )
            )
        else:
            errors.append(
                DocstringsError(
                    record.lineno,
                    record.column,
                    '{} Missing "Polarion" section'.format(MISSING_SECTION),
                    polarion_checks492,
                )
            )
    return errors


def run_checks(tree, filename, config):
    """Checks docstrings in python source file."""
    docstrings = parser.get_docstrings_in_file(tree, filename)
    errors = check_docstrings(docstrings, config)
    return errors


def polarion_checks492(tree, filename):
    """The flake8 entry point."""
    abs_filename = os.path.abspath(filename)
    __, tail = os.path.split(abs_filename)

    config = configuration.get_config()
    cfg_valid = config.get("docstrings") or {}
    cfg_valid = cfg_valid.get("valid_values")
    if not cfg_valid:
        return []  # must be iterable

    cfg_tests_path = config.get("tests_relative_path")
    if not cfg_tests_path:
        return []
    cfg_tests_path = cfg_tests_path.strip("./ ")

    # check only test files under tests path
    if not (cfg_tests_path in abs_filename and tail.startswith("test_")):
        return []

    return run_checks(tree, filename, config)


try:
    # __package__ is not in python 2.7
    __version__ = get_distribution(__name__.split(".")[0]).version
# pylint: disable=broad-except
except Exception:
    # package is not installed
    __version__ = "0.0"

polarion_checks492.name = "polarion_checks"
polarion_checks492.version = __version__
