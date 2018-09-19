import unittest
from econt import api
from econt.status_codes import StatusCode
from tests.credentials import USERNAME, PASSWORD
from unittest.mock import patch

CORRECT_USERNAME_PASSWORD_XML = '''
<response>
    <offices>
        <e>
            <id>33701</id>
            <name>ACS AFTHIMERON ATTIKIS</name>
            <name_en>ACS AFTHIMERON ATTIKIS</name_en>
            <office_code>15774</office_code> 
            <country_code>GRC</country_code>
            <id_city>55978</id_city>
            <post_code>10431</post_code>
            <city_name>Атина</city_name>
            <city_name_en>ATHINA</city_name_en>
            <address> Атина Bairaktari 15</address>
            <address_en> ATHINA Bairaktari 15</address_en>
            <latitude>37.9836966666667</latitude>
            <longitude>23.7712683333333</longitude>
            <address_details></address_details>
            <office_details></office_details>  
        </e>
    </offices>
</response>
'''

CORRECT_USERNAME_WRONG_PASSWORD_XML = '''
<response>
    <error>
        <code>API_ERR_LOGIN</code>
        <message>Невалидно потребителско име и/или парола.</message>
    </error>
</response>
'''
ONLY_USERNAME_XML = '''<response>
    <offices>
        <e>
            <id>33703</id>
            <name>ACS AG. PARASKEVI</name>
            <name_en>ACS AG. PARASKEVI</name_en>
            <office_code>15343</office_code>
            <country_code>GRC</country_code>
            <id_city>645046</id_city>
            <post_code>15342</post_code>
            <city_name>ΑΓΙΑ ΠΑΡΑΣΚΕΥΗ</city_name>
            <city_name_en>AG. PARASKEVI</city_name_en>
            <address_details></address_details>
            <office_details></office_details> 
        </e>
    </offices>
</response>
'''
NO_DATA_XML = '''
<response>
    <error>
        <code>API_ERR_LOGIN</code>
        <message>Потребителското име не може да бъде празно!</message>
    </error>
</response>
'''


class OfficesTest(unittest.TestCase):
    def test_correct_password_correct_username_expect_result(self):
        test_instance = api.Econt(USERNAME, PASSWORD)
        with patch('requests.sessions.Session.post') as mock_post:
            mock_post.return_value.text = CORRECT_USERNAME_PASSWORD_XML
            self.assertEqual(test_instance.get_offices().get('status'), StatusCode.STATUS_OK)

    def test_wrong_password_entered_expect_error(self):
        test_instance = api.Econt(USERNAME, 'xxx')
        with patch('requests.sessions.Session.post') as mock_post:
            mock_post.return_value.text = CORRECT_USERNAME_WRONG_PASSWORD_XML
            self.assertEqual(test_instance.get_offices().get('status'), StatusCode.ECONT_API_XML_ERROR)

    def test_only_username_entered_expect_result(self):
        test_instance = api.Econt(USERNAME, '', demo=False)
        with patch('requests.sessions.Session.post') as mock_post:
            mock_post.return_value.text = ONLY_USERNAME_XML
            self.assertEqual(test_instance.get_offices().get('status'), StatusCode.STATUS_OK)

    def test_no_data_entered_expect_error(self):
        test_instance = api.Econt('', '', demo=False)
        with patch('requests.sessions.Session.post') as mock_post:
            mock_post.return_value.text = NO_DATA_XML
            self.assertEqual(test_instance.get_offices().get('status'), StatusCode.ECONT_API_XML_ERROR)
