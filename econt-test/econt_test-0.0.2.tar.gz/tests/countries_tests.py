import unittest
from unittest.mock import patch

from econt import api
from tests.credentials import USERNAME, PASSWORD


BULGARIA_DICT = { 'id': '1033',
                  'country_name': 'България',
                  'country_name_en': 'Bulgaria',
                  'id_zone': '1',
                  'zone_name': 'Зона А',
                  'zone_name_en': 'Зона А'}

MOCK_OBJ_DATA = '''
<response>
        <e>
            <id>1033</id>
            <country_name>България</country_name>
            <country_name_en>Bulgaria</country_name_en>
            <id_zone>1</id_zone>
            <zone_name>Зона А</zone_name>
            <zone_name_en>Зона А</zone_name_en>
        </e>
</response>'''


class CountriesTest(unittest.TestCase):
    def setUp(self):
        # assigning the countries list to testing_instance
        with patch('requests.sessions.Session.post') as mock_result:
            mock_result.return_value.text = MOCK_OBJ_DATA
            self.testing_instance = (api.Econt(username=USERNAME,
                                               password=PASSWORD)).get_countries()

    def test_non_empty_result(self):
        self.assertIsNotNone(self.testing_instance['data'])

    def test_bulgaria_is_present(self):
        self.assertDictEqual(BULGARIA_DICT, self.testing_instance['data']['countries'])

