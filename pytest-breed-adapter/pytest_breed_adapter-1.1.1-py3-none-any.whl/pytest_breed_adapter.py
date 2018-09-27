from collections import Counter, OrderedDict
from contextlib import contextmanager
import logging
import time
import pytest
import json
import re
import socket
import requests


def get_test_source(CI_address):
    """判断测试来源0：CI 1：本地调试"""
    sc = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sc.connect(('114.114.114.114', 1))
    if str(sc.getsockname()[0]) == CI_address:
        return 'CI'
    else:
        return 'Local'


def meta_generator(docstring: str):
    lines = docstring.splitlines()
    meta = {}
    for line in lines:
        try:
            groups = re.match(r'^\s*@!\s*(\S+)\s*:\s*(.*)', line).groups()
            meta[groups[0]] = groups[1]
        except AttributeError:
            pass
    return meta


def send_to_breed(base_url, json_report):
    s = requests.post(
        f"{base_url}/report/parse",
        headers={"Content-Type": "application/json;charset:UTF-8"},
        data=json.dumps(json_report))
    return s.text


class JSONReport:
    """The JSON report pytest plugin."""

    def __init__(self, config=None):
        self.config = config
        self.start_time = None
        self.tests = OrderedDict()
        self.warnings = []
        self.report = None
        self.logger = logging.getLogger()

    @property
    def want_metadata(self):
        mark = self.config.getini('metadata')
        return mark and mark.lower() == 'true'

    @property
    def report_file(self):
        file = self.config.getini('json_report_file') or ''
        if file == 'auto':
            return time.strftime("%Y-%m-%d-%H.%M.%S.json")

        if file.lower() == 'none' or not file:
            return None
        else:
            return file

    @property
    def test_source(self):
        ip = self.config.getini('CI_server') or ''
        return get_test_source(ip)

    @property
    def breed_server_base_url(self):
        base_url = self.config.getini('breed_server') or ''
        if base_url.lower() == 'none' or not base_url:
            return None
        return base_url

    def pytest_configure(self, config):
        # When the plugin is used directly from code, it may have been
        # initialized without a config.
        if self.config is None:
            self.config = config

    def pytest_addhooks(self, pluginmanager):
        pluginmanager.add_hookspecs(Hooks)

    def pytest_sessionstart(self, session):
        self.start_time = time.time()

    def pytest_runtest_protocol(self, item, nextitem):
        item._json_log = {}

    @contextmanager
    def capture_log(self, item, when):
        handler = LoggingHandler()
        self.logger.addHandler(handler)
        try:
            yield
        finally:
            self.logger.removeHandler(handler)
        item._json_log[when] = handler.records

    @pytest.hookimpl(hookwrapper=True)
    def pytest_runtest_setup(self, item):
        with self.capture_log(item, 'setup'):
            yield

    @pytest.hookimpl(hookwrapper=True)
    def pytest_runtest_call(self, item):
        with self.capture_log(item, 'call'):
            yield

    @pytest.hookimpl(hookwrapper=True)
    def pytest_runtest_teardown(self, item):
        with self.capture_log(item, 'teardown'):
            yield

    @pytest.hookimpl(hookwrapper=True)
    def pytest_runtest_makereport(self, item, call):
        outcome = yield
        report = outcome.get_result()
        try:
            test = self.tests[item]
        except KeyError:
            test = self.json_testitem(item)
            self.tests[item] = test
        # Update total test outcome, if necessary. The total outcome can be
        # different from the outcome of the setup/call/teardown stage.
        outcome = self.config.hook.pytest_report_teststatus(report=report)[0]
        if outcome not in ['passed', '']:
            test['outcome'] = outcome
        test[call.when] = self.json_teststage(item, report)

    def pytest_sessionfinish(self, session):
        # self.add_metadata()
        json_report = dict(
            created=time.time(),
            duration=time.time() - self.start_time,
            exitcode=session.exitstatus,
            root=str(session.fspath),
            environment=getattr(self.config, '_metadata', {}),
            summary=self.json_summary(),
            source=self.test_source,
        )
        json_report['tests'] = list(self.tests.values())

        json_report['warnings'] = self.warnings

        self.config.hook.pytest_json_modifyreport(json_report=json_report)

        if self.report_file:
            self.save_report(json_report)

        if self.breed_server_base_url:
            self.breed_parse_result = send_to_breed(self.breed_server_base_url, json_report)

        # self.report isn't ever used, but it's useful if the report needs to
        # be processed by another script/plugin.
        self.report = json_report

    def pytest_logwarning(self, code, fslocation, message, nodeid):
        self.warnings.append({
            'code': code,
            'path': str(fslocation),
            'nodeid': nodeid,
            'message': message,
        })

    def pytest_terminal_summary(self, terminalreporter):
        if self.report_file:
            terminalreporter.write_sep('-', 'JSON report')
            terminalreporter.write_line(f'report written to: {self.report_file}')
        if self.breed_server_base_url:
            terminalreporter.write_sep('-', 'Sent to Breed server')
            terminalreporter.write_line(f'{self.breed_parse_result}')

    def add_metadata(self, docstring):
        if self.want_metadata:
            return {'metadata': meta_generator(docstring)}
        return {}

    def save_report(self, json_report):
        """Save the JSON report to file."""
        with open(self.report_file, 'w') as f:
            indent = self.config.getini('json_report_indent')
            json.dump(
                json_report,
                f,
                indent=int(indent) if indent else None,
            )

    def json_location(self, node):
        """Return JSON-serializable node location."""
        try:
            path, line, domain = node.location
        except AttributeError:
            return {}
        return {
            'path': path,
            'lineno': line,
            'domain': domain,
        }

    def json_testitem(self, item):
        """Return JSON-serializable test item."""
        return {
            'nodeid': item.nodeid,
            # Adding the location in the collector dict *and* here appears
            # redundant, but the docs say they may be different
            **self.json_location(item),
            **self.add_metadata(item.obj.__doc__ or ''),
            # item.keywords is actually a dict, but we just save the keys
            'keywords': list(item.keywords),
            # The outcome will be overridden in case of failure
            'outcome': 'passed',
        }

    def json_teststage(self, item, report):
        """Return JSON-serializable test stage (setup/call/teardown)."""
        stage = {
            'duration': report.duration,
            'outcome': report.outcome,
            **self.json_streams(item, report.when),
        }
        if report.longreprtext:
            stage['longrepr'] = report.longreprtext
        return stage

    def json_streams(self, item, when):
        """Return JSON-serializable output of the standard streams."""
        return {key: val for when_, key, val in item._report_sections if
                when_ == when and key in ['stdout', 'stderr']}

    def json_summary(self):
        """Return JSON-serializable test result summary."""
        summary = Counter([t['outcome'] for t in self.tests.values()])
        summary['total'] = sum(summary.values())
        return summary


class LoggingHandler(logging.Handler):

    def __init__(self):
        super().__init__()
        self.records = []

    def emit(self, record):
        d = dict(record.__dict__)
        d['msg'] = record.getMessage()
        d['args'] = None
        d['exc_info'] = None
        d.pop('message', None)
        self.records.append(d)


class Hooks:

    def pytest_json_modifyreport(self, json_report):
        """Called after building JSON report and before saving it.
        Plugins can use this hook to modify the report before it's saved.
        """


def pytest_addoption(parser):
    group = parser.getgroup('breed', 'reporting test results as JSON')
    group.addoption('--breed', default=False, action='store_true', help='create JSON report')
    parser.addini('json_report_indent', 'Json report indentation level')
    parser.addini('json_report_file', 'Json file location')
    parser.addini('metadata', 'parse test node metadata')
    parser.addini('CI_server', 'Continues Integration Server Address')
    parser.addini('breed_server', 'Breed server backend API')


def pytest_configure(config):
    if not config.option.breed:
        return
    plugin = JSONReport(config)
    config._json_report = plugin
    config.pluginmanager.register(plugin)


def pytest_unconfigure(config):
    plugin = getattr(config, '_json_report', None)
    if plugin is not None:
        del config._json_report
        config.pluginmanager.unregister(plugin)
