import unittest

from econt import api
from tests.credentials import USERNAME, PASSWORD
from unittest.mock import patch

MOCK_RESPONSE_XML_DATA = '''
<response>
   <cities_quarters>
        <e>
            <id>48909</id>
            <name>кв. 11</name>
            <name_en>kv. 11</name_en>
            <city_post_code>6800</city_post_code>
            <id_city>138</id_city>
            <updated_time>2011-06-07 12:35:07</updated_time>
        </e>
        <e>
            <id>48317</id>
            <name>жк Сухата река</name>
            <name_en>jk Suhata reka</name_en>
            <city_post_code>1000</city_post_code>
            <id_city>41</id_city>
            <updated_time>2014-10-13 20:04:23</updated_time>
        </e>
        <e>
            <id>48576</id>
            <name>кв. Момчилград</name>
            <name_en>kv. Momchilgrad</name_en>
            <city_post_code>6800</city_post_code>
            <id_city>138</id_city>
            <updated_time>2009-07-08 18:28:43</updated_time>
        </e>
    </cities_quarters>
</response>'''


class QuartersTest(unittest.TestCase):
    def setUp(self):
        self.sofia_post_code = '1000'
        self.mg_post_code = '6800'
        with patch('requests.sessions.Session.post') as mock_result:
            mock_result.return_value.text = MOCK_RESPONSE_XML_DATA
            self.testing_instance = api.Econt(username=USERNAME,
                                              password=PASSWORD)
            self.all_quarters = self.testing_instance.get_quarters()
            self.filtered_quarters = self.testing_instance.get_quarters_by_post_code(self.mg_post_code)

    def test_non_empty_result(self):
        self.assertIsNotNone(self.all_quarters['data'])

    def test_if_sofia_in_response(self):
        quarters = self.all_quarters['data']['response']['cities_quarters']['e']
        flag = False
        for quarter in quarters:
            if quarter['city_post_code'] == self.sofia_post_code:
                flag = True
        self.assertTrue(flag)

    def test_get_quarters_by_pcode(self):
        for quarter in self.filtered_quarters['data']['quarters']:
            self.assertTrue(quarter['city_post_code'] == self.mg_post_code)

