import json
import logging
import unittest

import six
import structuredlogging


logging.basicConfig()
LOG = logging.getLogger(__name__)
LOG.setLevel(10)


class TestStructuredLogFormatter(unittest.TestCase):
    def test_log_message(self):
        log_buffer = six.StringIO()
        log_handler = logging.StreamHandler(log_buffer)
        log_handler.setFormatter(structuredlogging.StructuredLogFormatter())
        msg_template = "structured string log {arg1} {arg2}"
        msg_args = dict(
            arg1="val1",
            arg2="val2"
        )
        try:
            LOG.addHandler(log_handler)
            LOG.info(msg_template, msg_args)
            log_handler.flush()
            log_buffer.flush()
        finally:
            LOG.removeHandler(log_handler)

        expected = dict(
            level="INFO",
            messageTemplate=msg_template,
            messageArguments=msg_args,
            message=msg_template.format(**msg_args)
        )
        msg = log_buffer.getvalue()
        log_buffer.close()
        msg_json = json.loads(msg)
        for key in expected.keys():
            self.assertIn(key, set(msg_json.keys()))
            self.assertEqual(expected[key], msg_json[key])
