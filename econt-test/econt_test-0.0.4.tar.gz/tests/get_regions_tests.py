import unittest

from econt import api
from tests.credentials import USERNAME, PASSWORD
from unittest.mock import patch

MOCK_XML_RESPONSE = '''<response>
   <cities_regions>
        <e>
            <id>307</id>
            <name>КЪРДЖАЛИ</name>
            <code>6600</code>
            <id_city>23</id_city>
            <updated_time>2015-02-05 08:41:59</updated_time>
        </e>
        <e>
            <id>308</id>
            <name>КЪРДЖАЛИ</name>
            <code>6602</code>
            <id_city>23</id_city>
            <updated_time>2015-02-05 08:41:59</updated_time>
        </e>
        <e>
            <id>309</id>
            <name>КЪРДЖАЛИ</name>
            <code>6603</code>
            <id_city>23</id_city>
            <updated_time>2015-02-05 08:41:59</updated_time>
        </e>
        <e>
            <id>41</id>
            <name>Подуене</name>
            <code>1517</code>
            <id_city>41</id_city>
            <updated_time>2010-08-16 16:45:56</updated_time>
        </e>
   </cities_regions>
</response>
'''


class RegionsTest(unittest.TestCase):
    def setUp(self):
        self.sofia_id_city = '41'
        self.kj_id_city = '23'
        with patch('requests.sessions.Session.post') as mock_result:
            mock_result.return_value.text = MOCK_XML_RESPONSE
            self.testing_instance = api.Econt(username=USERNAME,
                                              password=PASSWORD)
            self.all_regions = self.testing_instance.get_regions()['data']['response']['cities_regions']['e']

    def test_non_empty_result(self):
        self.assertIsNotNone(self.all_regions)

    def test_if_sofia_in_response(self):
        flag = False
        for region in self.all_regions:
            if region['id_city'] == self.sofia_id_city:
                flag = True
        self.assertTrue(flag)

    def test_if_kardzhali_occurs_trice(self):
        counter = 0
        for region in self.all_regions:
            if region['id_city'] == self.kj_id_city:
                counter += 1
        self.assertEqual(counter, 3)

