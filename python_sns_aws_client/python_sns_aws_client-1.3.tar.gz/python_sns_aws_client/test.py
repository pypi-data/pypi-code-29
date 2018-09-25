import unittest
from .utils import Client
from botocore.exceptions import ClientError

message = {
    'Type': 'Notification',
    'MessageId': 'id_message',
    'TopicArn': 'my-topic:)',
    'Subject': 'Test',
    'Message': 'test exitoso!!'
}

messagebody = b'{\n "Type": "Notification",\n "MessageId": "id_message",' \
              b'\n "TopicArn": "my-topic:)",\n "Subject": "Test",' \
              b'\n "Message": "test exitoso!!"\n}'

messagesubscribe = b'{\n "Type": "Subscribe",\n "Token": "token_false",' \
                   b'\n "TopicArn": "my-topic:)"\n}'


publish = {
    'subject': 'Test',
    'message': 'test exitoso!!',
}


CliTest = Client()


class TestSNSMethods(unittest.TestCase):

    def test_publish(self):
        publish_bad = {
            'subject': 'Test',
            'Message': 'test exitoso!!',
        }
        self.assertTrue(CliTest.publish(**publish))
        with self.assertRaises(KeyError):
            CliTest.publish(**publish_bad)

    def test_subs(self):
        with self.assertRaises(ClientError):
            CliTest.subscription('topi:c:t:e:s:t','token-invalid')
        with self.assertRaises(ClientError):
            CliTest.validator(messagesubscribe)

    def test_sns(self):
        self.assertTrue(CliTest.validator(messagebody))
        with self.assertRaises(TypeError):
            CliTest.validator(**message)

