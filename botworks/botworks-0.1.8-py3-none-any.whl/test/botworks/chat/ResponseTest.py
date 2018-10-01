import logging
import unittest
from unittest.mock import MagicMock

from botworks.chat.Response import Response
from botworks.chat.Trigger import Trigger, Or, And
from botworks.slack.Clack import Clack
from botworks.slack.Payload import Payload

log = logging.getLogger(__name__)
log.setLevel(logging.WARNING)


def mock_clack():
    return MagicMock(Clack)


def generate_payload(content="hello world"):
    p = Payload()
    p.lower_message = content
    p.channel = "rawr"
    return p


class ResponseTest(unittest.TestCase):

    def test_textResponse_singleResponse(self):
        c = mock_clack()
        r = Response(text="Hi back")
        r.respond(c, generate_payload())

        c.assert_called_once()

if __name__ == '__main__':
    unittest.main()
