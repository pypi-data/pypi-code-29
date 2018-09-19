import unittest

from econt import api
from econt.status_codes import StatusCode
from tests.credentials import USERNAME, PASSWORD
from unittest.mock import patch

MOCK_XML_RESPONSE = '''<response>
    <zones>
        <e>
            <id>51</id>
            <name>Зона I Гърция</name>
            <name_en>Zone I Gyrtsia</name_en>
            <national>0</national>
            <is_ee>1</is_ee>
            <updated_time>0000-00-00 00:00:00</updated_time>
        </e>
        <e>
            <id>52</id>
            <name>Зона II Беломорска Тракия</name>
            <name_en>Zone II Belomorska Trakia</name_en>
            <national>0</national>
            <is_ee>1</is_ee>
            <updated_time>0000-00-00 00:00:00</updated_time>
        </e>
        <e>
            <id>53</id>
            <name>Зона III Острови</name>
            <name_en>Zone III Ostrovi</name_en>
            <national>0</national>
            <is_ee>1</is_ee>
            <updated_time>0000-00-00 00:00:00</updated_time>
        </e>
   </zones>
</response>
'''


class ZonesTest(unittest.TestCase):
    def setUp(self):
        self.greek_zone_en_name = 'Zone I Gyrtsia'
        self.tatul_pcode = '6835'
        with patch('requests.sessions.Session.post') as mock_result:
            mock_result.return_value.text = MOCK_XML_RESPONSE
            self.test_instance = api.Econt(USERNAME, PASSWORD)
            self.zones = self.test_instance.get_zones()

    def test_non_empty_result_in_data_streets(self):
        self.assertIsNotNone(self.zones['data'])

    def test_if_greece_zone_in_response(self):
        flag = False
        for zone in self.zones['data']['response']['zones']['e']:
            if zone['name_en'] == self.greek_zone_en_name:
                flag = True
        self.assertTrue(flag)