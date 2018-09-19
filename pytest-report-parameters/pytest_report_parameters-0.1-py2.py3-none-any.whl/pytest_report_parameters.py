# -*- coding: utf-8 -*-
"""Plugin for adding test parameters to junit report."""

import pytest
import six


def get_unicode_str(obj):
    """Makes sure obj is a unicode string."""
    if isinstance(obj, six.text_type):
        return obj
    if isinstance(obj, six.binary_type):
        return obj.decode("utf-8", errors="ignore")
    return six.text_type(obj)


def extract_parameters(item):
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


@pytest.mark.tryfirst
def pytest_collection_modifyitems(config, items):
    xml = getattr(config, "_xml", None)
    if xml is None:
        return
    config.pluginmanager.register(
        ReportParametersToJunitPlugin(
            xml=xml, node_map={item.nodeid: extract_parameters(item) for item in items}
        )
    )


class ReportParametersToJunitPlugin(object):
    def __init__(self, xml, node_map):
        self.xml = xml
        self.node_map = node_map

    @pytest.mark.tryfirst
    def pytest_runtest_logreport(self, report):
        """Adds the parameters to the junit report as a property."""
        if report.when != "setup":
            return
        reporter = self.xml.node_reporter(report)
        polarion_ids = self.node_map.get(report.nodeid) or {}
        for param, value in six.iteritems(polarion_ids):
            reporter.add_property("polarion-parameter-{}".format(param), get_unicode_str(value))
