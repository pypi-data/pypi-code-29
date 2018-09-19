import unittest


from econt import api
from econt.status_codes import StatusCode
from tests.credentials import USERNAME, PASSWORD
from unittest.mock import patch

MOCK_XML_RESPONSE_FOR_SOFIA = '''<response>
   <post_boxes>
        <e>
            <id>120</id>
            <city_type>2</city_type>
            <city_name>София</city_name>
            <city_name_en>Sofia</city_name_en>
            <post_code>1000</post_code>
            <id_city>41</id_city>
            <num>3</num>
            <location>office</location>
            <address> София жк Лозенец ул. Голо бърдо №10</address>
            <address_en> Sofia zhk Lozenets ul. Golo byrdo №10</address_en>
            <address_details>
                <id_quarter>17761</id_quarter>
                <quarter_name>жк Лозенец</quarter_name>
                <quarter_name_en>zhk Lozenets</quarter_name_en>
                <id_street>12568</id_street>
                <street_name>ул. Голо бърдо</street_name>
                <street_name_en>ul. Golo byrdo</street_name_en>
                <num>10</num>
                <bl/>
                <vh/>
                <et/>
                <ap/>
                <other/>
            </address_details>
        </e>
        <e>
            <id>1688</id>
            <city_type>2</city_type>
            <city_name>София</city_name>
            <city_name_en>Sofia</city_name_en>
            <post_code>1000</post_code>
            <id_city>41</id_city>
            <num>1308</num>
            <location/>
            <address> София жк Лозенец ул. Козяк №32</address>
            <address_en> Sofia zhk Lozenets ul. Kozyak №32</address_en>
            <address_details>
                <id_quarter>17761</id_quarter>
                <quarter_name>жк Лозенец</quarter_name>
                <quarter_name_en>zhk Lozenets</quarter_name_en>
                <id_street>12556</id_street>
                <street_name>ул. Козяк</street_name>
                <street_name_en>ul. Kozyak</street_name_en>
                <num>32</num>
                <bl/>
                <vh/>
                <et/>
                <ap/>
                <other/>
            </address_details>
        </e>
   </post_boxes>
</response>
'''

MOCK_XML_RESPONSE_FOR_VARNA_CHAYKA = '''<response>
   <post_boxes>
        <e>
            <id>1711</id>
            <city_type>2</city_type>
            <city_name>Варна</city_name>
            <city_name_en>Varna</city_name_en>
            <post_code>9000</post_code>
            <id_city>7</id_city>
            <num>1296</num>
            <location/>
            <address> Варна кв. Чайка блок.15</address>
            <address_en> Varna kv. Chayka blk 15</address_en>
            <address_details>
                <id_quarter>649</id_quarter>
                <quarter_name>кв. Чайка</quarter_name>
                <quarter_name_en>kv. Chayka</quarter_name_en>
                <id_street>0</id_street>
                <street_name/>
                <street_name_en/>
                <num/>
                <bl>15</bl>
                <vh/>
                <et/>
                <ap/>
                <other/>
            </address_details>
        </e>
        <e>
            <id>1168</id>
            <city_type>2</city_type>
            <city_name>Варна</city_name>
            <city_name_en>Varna</city_name_en>
            <post_code>9000</post_code>
            <id_city>7</id_city>
            <num>981</num>
            <location>office</location>
            <address> Варна кв. Чайка блок.184</address>
            <address_en> Varna kv. Chayka blk 184</address_en>
            <address_details>
                <id_quarter>649</id_quarter>
                <quarter_name>кв. Чайка</quarter_name>
                <quarter_name_en>kv. Chayka</quarter_name_en>
                <id_street>0</id_street>
                <street_name/>
                <street_name_en/>
                <num/>
                <bl>184</bl>
                <vh/>
                <et/>
                <ap/>
                <other/>
            </address_details>
        </e>
   </post_boxes>
</response>'''


class PostBoxesTest(unittest.TestCase):
    def setUp(self):
        self.test_instance = api.Econt(USERNAME, PASSWORD)

    def test_given_no_param(self):
        with patch('requests.sessions.Session.post') as mock_result:
            mock_result.return_value.text = MOCK_XML_RESPONSE_FOR_SOFIA
            tester = self.test_instance.get_postboxes()
            self.assertEqual(tester.get('status'), StatusCode.STATUS_OK)
            self.assertEqual(tester.get('message'), 'OK')
            for postbox in tester['data']['post_boxes']:
                self.assertIn('city_name', postbox)
                self.assertIn('address_details', postbox)

    def test_given_city_en(self):
        with patch('requests.sessions.Session.post') as mock_result:
            mock_result.return_value.text = MOCK_XML_RESPONSE_FOR_SOFIA
            tester = self.test_instance.get_postboxes(city_name='Sofia')
            self.assertEqual(tester.get('status'), StatusCode.STATUS_OK)
            self.assertEqual(tester.get('message'), 'OK')
            for postbox in tester['data']['post_boxes']:
                self.assertIn('city_name', postbox)
                self.assertEqual(postbox['city_name'], 'София')

    def test_given_quarter_bg(self):
        with self.assertRaises(ValueError):
            self.test_instance.get_postboxes(
                 city_name='', quarter_name='кв. Зла река')

    def test_given_city_bg_quarter_bg(self):
        with patch('requests.sessions.Session.post') as mock_result:
            mock_result.return_value.text = MOCK_XML_RESPONSE_FOR_SOFIA
            tester = self.test_instance.get_postboxes(city_name='София',
                                                      quarter_name='жк Лозенец')
            self.assertEqual(tester.get('status'), StatusCode.STATUS_OK)
            self.assertEqual(tester.get('message'), 'OK')
            for postbox in tester['data']['post_boxes']:
                self.assertIn('address_details', postbox)
                self.assertIn('quarter_name_en', postbox['address_details'])
                self.assertIn('city_name_en', postbox)
                self.assertEqual(postbox['address_details']['quarter_name_en'],
                                 'zhk Lozenets')
                self.assertEqual(postbox['city_name_en'], 'Sofia')

    def test_given_city_bg_quarter_en(self):
        with patch('requests.sessions.Session.post') as mock_result:
            mock_result.return_value.text = MOCK_XML_RESPONSE_FOR_VARNA_CHAYKA
            tester = self.test_instance.get_postboxes(city_name='Варна',
                                                      quarter_name='kv. Chayka')
            self.assertEqual(tester.get('status'), StatusCode.STATUS_OK)
            self.assertEqual(tester.get('message'), 'OK')
            for postbox in tester['data']['post_boxes']:
                self.assertIn('address_details', postbox)
                self.assertIn('quarter_name', postbox['address_details'])
                self.assertIn('city_name_en', postbox)
                self.assertEqual(postbox['address_details']['quarter_name'],
                                 'кв. Чайка')
                self.assertEqual(postbox['city_name_en'], 'Varna')
