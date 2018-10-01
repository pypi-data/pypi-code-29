import logging
import unittest

from botworks.chat.Trigger import Trigger, Or, And
from botworks.slack.Payload import Payload

log = logging.getLogger(__name__)
log.setLevel(logging.WARNING)


def generate_payload(content="hello world"):
    p = Payload()
    p.lower_message = content
    p.channel = "rawr"
    return p


class TriggerTest(unittest.TestCase):

    def test_Phrase_SingleOr(self):
        t = Trigger(match_phrases=Or("Hello"))
        self.assertTrue(t.check(generate_payload()))

    def test_Phrase_SingleAnd(self):
        t = Trigger(match_phrases=And("Hello"))
        self.assertTrue(t.check(generate_payload()))

    def test_Phrase_MultipleAnd(self):
        t = Trigger(match_phrases=And("Hello", "world"))
        self.assertTrue(t.check(generate_payload()))

    def test_Phrase_MultipleOr(self):
        t = Trigger(match_phrases=Or("Hello", "Hola"))
        self.assertTrue(t.check(generate_payload()))

    def test_Phrase_MixedAndOr(self):
        t = Trigger(match_phrases=And(Or("Hello", "Hola"), Or("world", "mundo")))
        self.assertTrue(t.check(generate_payload()))

    def test_Phrase_MixedOrAnd(self):
        t = Trigger(match_phrases=Or(And("Hello", "world"), And("hola", "mundo")))
        self.assertTrue(t.check(generate_payload()))


if __name__ == '__main__':
    unittest.main()
