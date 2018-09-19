import unittest
from unittest.mock import patch

from econt import api
from tests.credentials import USERNAME, PASSWORD


MOMCHILGRAD_XML ='''
<response>
    <offices>
        <e>
            <id>243</id>
            <name_en>Momchilgrad</name_en>
            <office_code>6800</office_code>
            <country_code>BGR</country_code>
            <id_city>138</id_city>
            <post_code>6800</post_code>
            <city_name>Момчилград</city_name>
            <city_name_en>Momchilgrad</city_name_en>
            <address_en> Momchilgrad kv. Momchilgrad ul. Makaza №3</address_en>
            <address_details>
                <id_quarter>48576</id_quarter>
                <quarter_name_en>kv. Momchilgrad</quarter_name_en>
                <id_street>20873</id_street>
                <street_name_en>ul. Makaza</street_name_en>
                <num>3</num>
            </address_details> 
            <phone>+359 879922177</phone>
            <email>momchilgrad@econt.com</email>
            <hub_name_en>Haskovo RC</hub_name_en>
        </e>
    </offices>
</response>
'''

KARDZHALI_XML = '''
<response>
    <offices>
        <e>
            <id>1037</id>
            <name_en>Kyrdzhali RC</name_en>
            <office_code>6604</office_code>
            <country_code>BGR</country_code>
            <id_city>23</id_city>
            <post_code>6600</post_code>
            <city_name_en>Kyrdzhali</city_name_en>
            <address_en> Kyrdzhali Studen kladenec ul. Marin Baturov №5 (База Петрол)</address_en>
            <address_details></address_details>
        </e>
    </offices>
</response>
'''

EMPTY_XML = '''
'''


class OfficeByCityTest(unittest.TestCase):
    def setUp(self):
        self.testing_instance = api.Econt(USERNAME, PASSWORD)

    def test_get_momchilgrad_office_expect_non_empty_list(self):
        with patch('requests.sessions.Session.post') as mock_post:
            mock_post.return_value.text = MOMCHILGRAD_XML
            self.assertTrue(self.testing_instance.get_offices_by_city(6800)['data']['offices'])

    def test_get_kardzhali_offices_expect_city_id(self):
        kardzhali_econt_city_id = '23'
        with patch('requests.sessions.Session.post') as mock_post:
            mock_post.return_value.text = KARDZHALI_XML
            self.assertEqual(self.testing_instance.get_offices_by_city(6600)['data']['offices'][0]['id_city'],
                             kardzhali_econt_city_id)

    def test_invalid_input_expect_empty_list(self):
        with patch('requests.sessions.Session.post') as mock_post:
            mock_post.return_value.text = KARDZHALI_XML
            self.assertListEqual(self.testing_instance.get_offices_by_city('aZ123.123')['data']['offices'], [])

    def test_parameter_exception(self):
        with patch('econt.api.Econt.get_offices_by_city') as mock_result:
            mock_result.side_effect = ValueError('Post can\'t be empty')
            with self.assertRaises(ValueError):
                self.testing_instance.get_offices_by_city('')
