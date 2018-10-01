import unittest
from unittest.mock import create_autospec, call

from botworks.chat.InteractionDefinition import InteractionDefinition
from botworks.chat.Response import Response, Responses
from botworks.chat.Trigger import Or, Trigger
from botworks.slack.Clack import Clack
from botworks.slack.Payload import Payload


def basic_pass(**kwargs):
    pass


def generate_payload(content="hello world"):
    p = Payload()
    p.lower_message = content
    p.channel = "rawr"
    return p


def mock_clack():
    clack_autospec = create_autospec(Clack.__class__)
    clack_autospec.post_message = create_autospec(basic_pass)
    clack_autospec.react = create_autospec(basic_pass)
    clack_autospec.ephemeral_message = create_autospec(basic_pass)
    clack_autospec.thread_reply = create_autospec(basic_pass)
    return clack_autospec


class ResponseTest(unittest.TestCase):

    def test_simpleTrigger_writesSingleTextResponse(self):
        clack_autospec = mock_clack()
        i = InteractionDefinition(
                trigger=Trigger(match_phrases=Or("sample")),
                response=Response(text="sample response")
        )

        i.respond(clack_autospec, generate_payload())
        clack_autospec.post_message.assert_called_once_with(channel='rawr', message='sample response')

    def test_simpleTrigger_writesSingleEmoji(self):
        clack_autospec = mock_clack()
        payload = generate_payload()
        i = InteractionDefinition(
                trigger=Trigger(match_phrases=Or("sample")),
                response=Response(emoji="here")
        )

        i.respond(clack_autospec, payload)
        clack_autospec.react.assert_called_once_with(payload=payload, reaction='here')

    def test_simpleTrigger_writesSingleEphemeral(self):
        clack_autospec = mock_clack()
        payload = generate_payload()
        i = InteractionDefinition(
                trigger=Trigger(match_phrases=Or("sample")),
                response=Response(ephemeral="I'm a ghoooost")
        )

        i.respond(clack_autospec, payload)
        clack_autospec.ephemeral_message.assert_called_once_with(payload=payload, message='I\'m a ghoooost')

    def test_simpleTrigger_writesSingleThreaded(self):
        clack_autospec = mock_clack()
        payload = generate_payload()
        i = InteractionDefinition(
                trigger=Trigger(match_phrases=Or("sample")),
                response=Response(threaded="I'm a threaaaad")
        )

        i.respond(clack_autospec, payload)
        clack_autospec.thread_reply.assert_called_once_with(payload=payload, message="I'm a threaaaad")

    def test_simpleTrigger_writesMultipleEverything(self):
        clack_autospec = mock_clack()
        payload = generate_payload()
        i = InteractionDefinition(
                trigger=Trigger(match_phrases=Or("sample")),
                response=Response(text=["sample response", "response 2"], emoji=["here", "pinged"],
                                  ephemeral=["I'm a ghoooost", "punk"], threaded=["I'm", "a threaaaad"])
        )

        i.respond(clack_autospec, payload)

        self.assertEqual(2, len(clack_autospec.post_message.call_args_list))
        self.assertEqual(clack_autospec.post_message.call_args_list[0], call(message="sample response", channel='rawr'))
        self.assertEqual(clack_autospec.post_message.call_args_list[1], call(message="response 2", channel='rawr'))

        self.assertEqual(2, len(clack_autospec.react.call_args_list))
        self.assertEqual(clack_autospec.react.call_args_list[0], call(reaction="here", payload=payload))
        self.assertEqual(clack_autospec.react.call_args_list[1], call(reaction="pinged", payload=payload))

        self.assertEqual(2, len(clack_autospec.ephemeral_message.call_args_list))
        self.assertEqual(clack_autospec.ephemeral_message.call_args_list[0], call(message="I'm a ghoooost", payload=payload))
        self.assertEqual(clack_autospec.ephemeral_message.call_args_list[1], call(message="punk", payload=payload))

        self.assertEqual(2, len(clack_autospec.thread_reply.call_args_list))
        self.assertEqual(clack_autospec.thread_reply.call_args_list[0], call(message="I'm", payload=payload))
        self.assertEqual(clack_autospec.thread_reply.call_args_list[1], call(message="a threaaaad", payload=payload))

    def test_simpleTrigger_picksFromMultipleResponses(self):
        clack_autospec = mock_clack()
        payload = generate_payload()
        i = InteractionDefinition(
            trigger=Trigger(match_phrases=Or("sample")),
            response=Responses([
                Response(text="sample response"), Response(text="response 2"), Response(text="here"),
                Response(text="pinged"), Response(text="I'm a ghoooost"), Response(text="punk"),
                Response(text="I'm"), Response(text="a threaaaad")])
        )

        i.respond(clack_autospec, payload)
        clack_autospec.post_message.assert_called_once()


if __name__ == '__main__':
    unittest.main()
