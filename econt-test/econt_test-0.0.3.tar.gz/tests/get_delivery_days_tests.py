import unittest

from econt.api import Econt
from tests.credentials import USERNAME, PASSWORD
from unittest.mock import patch

MOCK_FULL_RESPONSE = '''<response>
    <delivery_days>
        <e>
            <date>3018-09-19</date>
        </e>
        <e>
            <date>3018-09-21</date>
        </e>
    </delivery_days>
</response>'''

MOCK_EMPTY_RESPONSE = '''<response>
    <delivery_days/>
</response>'''


class GetDeliveryDaysTest(unittest.TestCase):
    def setUp(self):
        self.testing_instance = Econt(USERNAME, PASSWORD)

    def test_full_response(self):
        expected_result = ['3018-09-19', '3018-09-21']
        with patch('requests.sessions.Session.post') as mock_result:
            mock_result.return_value.text = MOCK_FULL_RESPONSE
            result = self.testing_instance.get_delivery_days('3018-09-18')
            self.assertTrue(result['data']['delivery_days'] == expected_result)

    def test_no_response(self):
        expected_result = ['3018-09-06']
        with patch('requests.sessions.Session.post') as mock_result:
            mock_result.return_value.text = MOCK_EMPTY_RESPONSE
            result = self.testing_instance.get_delivery_days('3018-09-05')
            self.assertTrue(result['data']['delivery_days'] == expected_result)