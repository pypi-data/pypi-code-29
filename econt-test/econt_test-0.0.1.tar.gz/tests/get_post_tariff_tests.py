import unittest

from unittest.mock import patch
from econt import api
from econt.status_codes import StatusCode
from tests.credentials import USERNAME, PASSWORD

MOCK_CORRECT_POST_TARIFF = '''
<response>
    <service_types>
        <e>
            <id>8</id>
            <code>CALLED</code>
            <description>До поискване</description>
            <description_en>By request</description_en>
            <description_ro>Post restant</description_ro>
            <service_type>additional</service_type>
            <additional_services/>
        </e>
    </service_types>
    <general_tariff>
        <e>
            <id>282</id>
            <index>BL0500</index>
            <name>Голямо писмо /  Малък пакет до 0.500 кг.</name>
            <service_type>1</service_type>
            <area>to</area>
            <weight_to>0.500</weight_to>
            <step>-1.00</step>
            <measure>лв</measure>
            <price>1.50000</price>
            <price_type>stable</price_type>
        </e>
    </general_tariff>
</response>'''

MOCK_INVALID_USERNAME_OR_PASSWORD = '''<response>
    <error>
        <code>API_ERR_LOGIN</code>
        <message>Невалидно потребителско име и/или парола.</message>
    </error>
</response>'''


class PostTariffTest(unittest.TestCase):
    INVALID_CREDENTIALS_MESSAGE = 'Невалидно потребителско име и/или парола.'

    def test_invalid_username_and_password_duo(self):
        with patch('requests.sessions.Session.post') as mock_result:
            mock_result.return_value.text = MOCK_INVALID_USERNAME_OR_PASSWORD
            test_instance = api.Econt(USERNAME, PASSWORD).get_post_tariff()
            self.assertIs(test_instance['status'], StatusCode.ECONT_API_XML_ERROR)
            self.assertIn(test_instance['message'], self.INVALID_CREDENTIALS_MESSAGE)
            self.assertIsNone(test_instance['data'])

    def test_any_valid_username_no_password(self):
        with patch('requests.sessions.Session.post') as mock_result:
            mock_result.return_value.text = MOCK_CORRECT_POST_TARIFF
            test_instance = api.Econt('demo', '').get_post_tariff()
            self.assertIs(test_instance['status'], StatusCode.STATUS_OK)
            self.assertIn(test_instance['message'], 'OK')
            self.assertIn('service_types', test_instance['data']['response'])
            self.assertIsNotNone(test_instance['data']['response']['service_types'])
            self.assertIsNotNone(test_instance['data']['response']['general_tariff'])

    def test_any_valid_username_faulty_password(self):
        with patch('requests.sessions.Session.post') as mock_result:
            mock_result.return_value.text = MOCK_INVALID_USERNAME_OR_PASSWORD
            test_instance = api.Econt(USERNAME, 'vvv').get_post_tariff()
            self.assertIs(test_instance['status'], StatusCode.ECONT_API_XML_ERROR)
            self.assertIn(test_instance['message'], self.INVALID_CREDENTIALS_MESSAGE)
            self.assertIsNone(test_instance['data'])

