# encoding: utf-8
# pylint: disable=missing-docstring

from __future__ import unicode_literals

from polarion_docstrings import checker, configuration

RESULTS = [
    (50, 0, 'P665 Missing "Polarion" section'),
    (54, 0, 'P665 Missing "Polarion" section'),
    (60, 4, 'P665 Missing "Polarion" section'),
    (10, 4, 'P665 Missing "Polarion" section'),
    (14, 8, 'P665 Missing "Polarion" section'),
    (21, 8, 'P669 Missing required field "initialEstimate"'),
    (23, 12, 'P667 Invalid value "nonexistent" of the "casecomponent" field'),
    (39, 12, 'P667 Invalid value "level1" of the "caselevel" field'),
    (39, 12, 'P668 Field "caselevel" should be handled by the "@pytest.mark.tier" marker'),
    (40, 12, 'P668 Field "caseautomation" should be handled by the "@pytest.mark.manual" marker'),
    (
        41,
        12,
        'P668 Field "linkedWorkItems" should be handled by the "@pytest.mark.requirements" marker',
    ),
    (42, 12, 'P666 Unknown field "foo"'),
]


def _strip_func(errors):
    return [(lineno, col, msg) for lineno, col, msg, __ in errors]


def test_checker(source_file):
    config = configuration.get_config()
    errors = checker.run_checks(None, source_file, config)
    errors = _strip_func(errors)
    assert len(errors) == len(RESULTS)
    assert errors == RESULTS
