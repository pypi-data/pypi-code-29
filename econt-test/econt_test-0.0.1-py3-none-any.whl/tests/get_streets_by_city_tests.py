import unittest

from econt import api
from tests.credentials import USERNAME, PASSWORD
from unittest.mock import patch

MOCK_XML_RESPONSE = '''<response>
   <cities_streets>
        <e>
            <id>137337</id>
            <name>ул. Татул</name>
            <name_en>str Tatul</name_en>
            <city_post_code>6835</city_post_code>
            <id_city>26616</id_city>
            <updated_time>2012-01-24 14:48:12</updated_time>
        </e>
   </cities_streets>
</response>
'''


class GetStreetsByCityTests(unittest.TestCase):
    def setUp(self):
        self.tatul_pcode = '6835'
        with patch('requests.sessions.Session.post') as mock_result:
            mock_result.return_value.text = MOCK_XML_RESPONSE
            self.test_instance = api.Econt(USERNAME, PASSWORD)
            self.tatul_streets = self.test_instance.get_streets_by_city(self.tatul_pcode)

    def test_non_empty_result_in_data_streets(self):
        self.assertIsNotNone(self.tatul_streets['data']['streets'])
    
    def test_if_tatul_in_response(self):
        self.assertTrue(self.tatul_streets['data']['streets'][0]['city_post_code'] == self.tatul_pcode)

    def test_parameter_exception(self):
        with patch('econt.api.Econt.get_streets_by_city') as mock_result:
            mock_result.side_effect = ValueError('Post can\'t be empty')
            with self.assertRaises(ValueError):
                self.test_instance.get_streets_by_city('')



        