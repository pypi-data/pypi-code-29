import unittest
from unittest.mock import patch

from econt import api
from tests.credentials import USERNAME, PASSWORD

SOFIA_XML = '''
<response>
    <cities_quarters>
        <e>
            <id>12464</id>
            <name>Бизнес Парк София - кв. Младост-4</name>
            <name_en>Biznes Park Sofia - kv. Mladost-4</name_en>
            <city_post_code>1000</city_post_code>
            <id_city>41</id_city>
            <updated_time>2016-08-12 14:38:02</updated_time>
        </e>
    </cities_quarters>
</response>
'''

MOMCHIL_XML = '''
<response>
    <cities_quarters>
        <e>
            <id>48577</id>
            <name>кв. Монтана</name>
            <name_en>kv. Montana</name_en>
            <city_post_code>6800</city_post_code>
            <id_city>138</id_city>
            <updated_time>2009-07-08 18:29:25</updated_time>
        </e>
    </cities_quarters>
</response>
'''


class QuartersByPostCodeTest(unittest.TestCase):
    def setUp(self):
        self.test_instance = api.Econt(USERNAME, PASSWORD)

    def test_non_empty_quarters_in_sofia(self):
        with patch('requests.sessions.Session.post') as mock_post:
            mock_post.return_value.text = SOFIA_XML
            sofia_pcode = 1000
            self.assertIsNotNone(self.test_instance.get_quarters_by_post_code(sofia_pcode))

    def test_momchilgrad_post_code(self):
        with patch('requests.sessions.Session.post') as mock_post:
            mock_post.return_value.text = MOMCHIL_XML
            momchilgrad_city_id = '138'
            mom_quarters = self.test_instance.get_quarters_by_post_code(6800)
            mom_quarters = mom_quarters['data']['quarters']
            self.assertTrue(mom_quarters[0]['id_city'] == momchilgrad_city_id)

    def test_invalid_pcode(self):
        with patch('requests.sessions.Session.post') as mock_post:
            mock_post.return_value.text = MOMCHIL_XML
            invalid_pcode = 'invalid_pcode'
            response = self.test_instance.get_quarters_by_post_code(invalid_pcode)
            expected_empty_list = response['data']['quarters']
            self.assertListEqual(expected_empty_list, [])

    def test_parameter_exception(self):
        with patch('econt.api.Econt.get_quarters_by_post_code') as mock_result:
            mock_result.side_effect = ValueError
            with self.assertRaises(ValueError):
                self.test_instance.get_quarters_by_post_code('')

