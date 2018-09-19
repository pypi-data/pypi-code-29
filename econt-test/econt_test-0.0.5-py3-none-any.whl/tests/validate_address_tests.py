import unittest
from unittest.mock import patch

from econt import api
from econt.status_codes import StatusCode
from tests.credentials import USERNAME, PASSWORD


# valid addresses
MELON_SOFIA_JSON = {'city': 'Sofia', 'post_code': '1113',
                    'street': 'Kosta Lulchev', 'street_num': '20',
                    'street_et': '3'}
MELON_SOFIA_XML = '''
<response>
    <address>
        <city>Sofia</city>
        <post_code>1000</post_code>
        <office_code></office_code>
        <quarter></quarter>
        <street>ул. Коста Лулчев</street>
        <street_num>20</street_num>
        <street_bl></street_bl>
        <street_vh></street_vh>
        <street_et>3</street_et>
        <street_ap></street_ap>
        <street_other></street_other>
        <validation_status>normal</validation_status>
        <valid>1</valid>
    </address>
</response>
'''

DIFFERENT_ADDRESS_SOFIA_JSON = {'city': 'Sofia', 'post_code': '1113',
                                'street': 'Akademik Georgi Bonchev',
                                'street_bl': '8', 'quarter': 'Geo Milev'}
DIFFERENT_ADDRESS_SOFIA_XML = '''
<response>
    <address>
        <city>Sofia</city>
        <post_code>1000</post_code>
        <office_code></office_code>
        <quarter>zhk Geo Milev</quarter>
        <street>ul. Akad. Georgi Bonchev</street>
        <street_num></street_num>
        <street_bl>8</street_bl>
        <street_vh></street_vh>
        <street_et></street_et>
        <street_ap></street_ap>
        <street_other>akademik</street_other>
        <validation_status>processed</validation_status>
        <valid>1</valid>
    </address>
</response>
'''

STREET_OTHER_INCLUDED_JSON = {'city': 'Sofia', 'post_code': '1505',
                              'street': 'Oborishte', 'street_num': '48',
                              'street_other': 'bul. Sitnyakovo'}
STREET_OTHER_INCLUDED_XML = '''
<response>
    <address>
        <city>Sofia</city>
        <post_code>1000</post_code>
        <office_code></office_code>
        <quarter></quarter>
        <street>ул. Оборище</street>
        <street_num>48</street_num>
        <street_bl></street_bl>
        <street_vh></street_vh>
        <street_et></street_et>
        <street_ap></street_ap>
        <street_other>bul. Sitnyakovo</street_other>
        <validation_status>normal</validation_status>
        <valid>1</valid>
    </address>
</response>
'''

DIFFERENT_CITY_JSON = {'city': 'Burgas', 'post_code': '8001', 'street_num': '622',
                       'quarter': 'Lazur'}
DIFFERENT_CITY__XML = '''
<response>
    <address>
        <city>Burgas</city>
        <post_code>8000</post_code>
        <office_code></office_code>
        <quarter>ж.к. Лазур</quarter>
        <street></street>
        <street_num>622</street_num>
        <street_bl></street_bl>
        <street_vh></street_vh>
        <street_et></street_et>
        <street_ap></street_ap>
        <street_other></street_other>
        <validation_status>normal</validation_status>
        <valid>1</valid>
    </address>
</response>
'''

NO_CITY_YES_PCODE_JSON = {'city': '', 'post_code': '8001', 'street_num': '622',
                          'quarter': 'Lazur'}
NO_CITY_YES_PCODE_XML ='''
<response>
    <address>
        <city>Бургас</city>
        <post_code>8000</post_code>
        <office_code></office_code>
        <quarter>ж.к. Лазур</quarter>
        <street></street>
        <street_num>622</street_num>
        <street_bl></street_bl>
        <street_vh></street_vh>
        <street_et></street_et>
        <street_ap></street_ap>
        <street_other></street_other>
        <validation_status>normal</validation_status>
        <valid>1</valid>
    </address>
</response>
'''

# invalid addresses
NO_VALUES_JSON = {'city': '', 'post_code': '', 'street': '',
                  'street_bl': '', 'quarter': ''}
NO_VALUES_XML = '''
<response>
    <address>
        <city></city>
        <post_code></post_code>
        <street></street>
        <street_bl></street_bl>
        <quarter></quarter>
        <validation_status>invalid</validation_status>
        <error>Невалиднo населено място.</error>
    </address>
</response>
'''

FAULTY_PCODE_JSON = {'city': 'Sofia', 'post_code': '6703', 'street': 'Oborishte',
                     'street_num': '48', 'street_other': 'bul. Sitnyakovo'}
FAULTY_PCODE_XML = '''
<response>
    <address>
        <city>Sofia</city>
        <post_code>6703</post_code>
        <street>Oborishte</street>
        <street_num>48</street_num>
        <street_other>bul. Sitnyakovo</street_other>
        <validation_status>invalid</validation_status>
        <error>Несъответствие между населено място и пощенски код.</error>
    </address>
</response>
'''

JUST_CITY_JSON = {'city': 'Burgas', 'post_code': '', 'street': '',
                  'street_bl': '', 'quarter': ''}
JUST_CITY_XML = '''
<response>
    <address>
        <city>Burgas</city>
        <post_code></post_code>
        <street></street>
        <street_bl></street_bl>
        <quarter></quarter>
        <validation_status>invalid</validation_status>
        <error>Намерени са повече от едно населени места с име Burgas</error>
    </address>
</response>
'''

NO_CITY_NO_PCODE_JSON = {'city': '', 'post_code': '', 'street_num': '622',
                         'street': 'Akademik Georgi Bonchev', 'quarter': 'Lazur'}
NO_CITY_NO_PCODE_XML = '''
<response>
    <address>
        <city></city>
        <post_code></post_code>
        <street_num>622</street_num>
        <street>Akademik Georgi Bonchev</street>
        <quarter>Lazur</quarter>
        <validation_status>invalid</validation_status>
        <error>Невалиднo населено място.</error>
    </address>
</response>
'''

NOT_IN_BG_JSON = {'city': 'Paris', 'post_code': '1113',
                  'street': 'Akademik Georgi Bonchev',
                  'street_bl': '8', 'quarter': 'Geo Milev'}
NOT_IN_BG_XML = '''
<response>
    <address>
        <city>Paris</city>
        <post_code>1113</post_code>
        <street>Akademik Georgi Bonchev</street>
        <street_bl>8</street_bl>
        <quarter>Geo Milev</quarter>
        <validation_status>invalid</validation_status>
        <error>Несъответствие между населено място и пощенски код.</error>
    </address>
</response>
'''

EMPTY_DICT_JSON = {}
EMPTY_DICT_XML = ''''''


class AddressValidationTest(unittest.TestCase):
    def setUp(self):
        self.test_instance = api.Econt(USERNAME, PASSWORD)
        
    def test_when_address_of_melon_is_given_expect_status_0(self):
        with patch('requests.sessions.Session.post') as mock_post:
            mock_post.return_value.text = MELON_SOFIA_XML
            self.assertEqual(
                self.test_instance.validate_address(MELON_SOFIA_JSON)['status'],
                StatusCode.STATUS_OK)

    def test_when_another_address_in_sofia_is_given_expect_status_0(self):
        with patch('requests.sessions.Session.post') as mock_post:
            mock_post.return_value.text = DIFFERENT_ADDRESS_SOFIA_XML
            self.assertEqual(
                self.test_instance.validate_address(DIFFERENT_ADDRESS_SOFIA_JSON)['status'],
                StatusCode.STATUS_OK)

    def test_when_extra_data_is_inserted_as_other_expect_status_0(self):
        with patch('requests.sessions.Session.post') as mock_post:
            mock_post.return_value.text = STREET_OTHER_INCLUDED_XML
            self.assertEqual(
                self.test_instance.validate_address(STREET_OTHER_INCLUDED_JSON)['status'],
                StatusCode.STATUS_OK)

    def test_when_address_is_in_different_city_expect_status_0(self):
        with patch('requests.sessions.Session.post') as mock_post:
            mock_post.return_value.text = DIFFERENT_CITY__XML
            self.assertEqual(
                self.test_instance.validate_address(DIFFERENT_CITY_JSON)['status'],
                StatusCode.STATUS_OK)

    def test_when_just_pcode_is_given_expect_status_0(self):
        with patch('requests.sessions.Session.post') as mock_post:
            mock_post.return_value.text = NO_CITY_YES_PCODE_XML
            self.assertEqual(
                self.test_instance.validate_address(NO_CITY_YES_PCODE_JSON)['status'],
                StatusCode.STATUS_OK)

    # testing invalid addresses
    def test_when_no_values_given_expect_status_not_0(self):
        with patch('requests.sessions.Session.post') as mock_post:
            mock_post.return_value.text = NO_VALUES_XML
            self.assertEqual(
                self.test_instance.validate_address(NO_VALUES_JSON)['status'],
                StatusCode.ECONT_API_XML_ERROR)

    def test_when_pcode_does_not_match_city_expect_status_not_0(self):
        with patch('requests.sessions.Session.post') as mock_post:
            mock_post.return_value.text = FAULTY_PCODE_XML
            self.assertNotEqual(
                self.test_instance.validate_address(FAULTY_PCODE_JSON)['status'],
                StatusCode.STATUS_OK)

    def test_when_only_city_is_given_expect_status_not_0(self):
        with patch('requests.sessions.Session.post') as mock_post:
            mock_post.return_value.text = JUST_CITY_XML
            self.assertNotEqual(
                self.test_instance.validate_address(JUST_CITY_JSON)['status'],
                StatusCode.STATUS_OK)
    
    def test_when_no_pcode_and_no_city_is_given_expect_status_not_0(self):
        with patch('requests.sessions.Session.post') as mock_post:
            mock_post.return_value.text = NO_CITY_NO_PCODE_XML
            self.assertNotEqual(
                self.test_instance.validate_address(NO_CITY_NO_PCODE_JSON)['status'],
                StatusCode.STATUS_OK)

    def test_when_city_is_not_in_bg_expect_status_not_0(self):
        with patch('requests.sessions.Session.post') as mock_post:
            mock_post.return_value.text = NOT_IN_BG_XML
            self.assertNotEqual(
                self.test_instance.validate_address(NOT_IN_BG_JSON)['status'],
                StatusCode.STATUS_OK)

    def test_when_dict_is_empty_expect_status_not_0(self):
        with patch('requests.sessions.Session.post') as mock_post:
            mock_post.return_value.text = EMPTY_DICT_XML
            self.assertNotEqual(
                self.test_instance.validate_address(EMPTY_DICT_JSON)['status'],
                StatusCode.STATUS_OK)
