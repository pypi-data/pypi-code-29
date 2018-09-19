import unittest
from unittest.mock import patch

from econt import api
from econt.status_codes import StatusCode
from tests.credentials import USERNAME, PASSWORD


VALID_INSTANCE = api.Econt(USERNAME, PASSWORD)
VALID_INSTANCE_EXPECTED_ID = '15053708'
VALID_INSTANCE_XML = '''
<response>
    <client_info>
        <id>15053708</id>
    </client_info>
    <addresses>
        <e>
        </e>
    </addresses>
</response>
'''

INVALID_INSTANCE = api.Econt('bamboleo', 'gipsykings')
INVALID_INSTANCE_XML ='''
<response>
    <error>
        <code>API_ERR_LOGIN</code>
        <message>Невалидно потребителско име и/или парола.</message>
    </error>
</response>
'''


class RetrieveProfileTests(unittest.TestCase):
    def test_valid_instance_expect_correct_result(self):
        with patch('requests.sessions.Session.post') as mock_post:
            mock_post.return_value.text = VALID_INSTANCE_XML
            self.assertEqual(dict(VALID_INSTANCE.retrieve_profile()['data']['client_info'])['id'],
                             VALID_INSTANCE_EXPECTED_ID)

    def test_invalid_instance_expect_error(self):
        with patch('requests.sessions.Session.post') as mock_post:
            mock_post.return_value.text = INVALID_INSTANCE_XML
            self.assertEqual(INVALID_INSTANCE.retrieve_profile()['status'], StatusCode.ECONT_API_XML_ERROR)
