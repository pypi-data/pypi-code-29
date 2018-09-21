import unittest
from xmltest import XMLAssertions

from econt import api
from tests.credentials import USERNAME, PASSWORD


# valid addresses
MELON_SOFIA = {'city': 'Sofia', 'post_code': '1113','street': 'Kosta Lulchev',
               'street_num': '20', 'street_et': '3', }
DIFFERENT_ADDRESS_SOFIA = {'city': 'Sofia', 'post_code': '1113','street': 'Akademik Georgi Bonchev',
                           'street_bl': '8', 'quarter': 'Geo Milev', }
STREET_OTHER_INCLUDED = {'city': 'Sofia', 'post_code': '1505','street': 'Oborishte',
                         'street_num': '48', 'street_other': 'bul. Sitnyakovo', }
DIFFERENT_CITY = {'city': 'Burgas', 'post_code': '8001', 'street_num': '622',
                  'quarter': 'Lazur', }
NO_CITY_YES_PCODE = {'city': '', 'post_code': '8001', 'street_num': '622',
                     'quarter': 'Lazur', }

# invalid addresses
NO_VALUES = {'city': '', 'post_code': '','street': '',
             'street_bl': '', 'quarter': '', }
FAULTY_PCODE = {'city': 'Sofia', 'post_code': '6703','street': 'Oborishte',
                'street_num': '48', 'street_other': 'bul. Sitnyakovo', }
JUST_CITY = {'city': 'Burgas', 'post_code': '','street': '',
             'street_bl': '', 'quarter': '', }
NO_CITY_NO_PCODE = {'city': '', 'post_code': '', 'street_num': '622', 'street':'Akademik Georgi Bonchev',
                    'quarter': 'Lazur', }
NOT_IN_BG = {'city': 'Paris', 'post_code': '1113','street': 'Akademik Georgi Bonchev',
             'street_bl': '8', 'quarter': 'Geo Milev', }
EMPTY_DICT = {}


class XMLBuilderTest(unittest.TestCase, XMLAssertions):
    def setUp(self):
        self.test_instance = api.Econt(USERNAME, PASSWORD)

    # authenticate=True
    def test_given_melon_address(self):
        melon_sofia_xml = self.test_instance.xml_builder(MELON_SOFIA, authenticate=True)
        self.assertXPathNodeText(melon_sofia_xml, MELON_SOFIA.get('city'), 'city')
        self.assertXPathNodeText(melon_sofia_xml, MELON_SOFIA.get('post_code'), 'post_code')
        self.assertXPathNodeText(melon_sofia_xml, MELON_SOFIA.get('street'), 'street')
        self.assertXPathNodeText(melon_sofia_xml, MELON_SOFIA.get('street_num'), 'street_num')
        self.assertXPathNodeText(melon_sofia_xml, MELON_SOFIA.get('street_et'), 'street_et')

    def test_given_another_address_in_sofia(self):
        different_address_sofia_xml = self.test_instance.xml_builder(DIFFERENT_ADDRESS_SOFIA, authenticate=True)
        self.assertXPathNodeText(different_address_sofia_xml, DIFFERENT_ADDRESS_SOFIA.get('city'), 'city')
        self.assertXPathNodeText(different_address_sofia_xml, DIFFERENT_ADDRESS_SOFIA.get('post_code'), 'post_code')
        self.assertXPathNodeText(different_address_sofia_xml, DIFFERENT_ADDRESS_SOFIA.get('street'), 'street')
        self.assertXPathNodeText(different_address_sofia_xml, DIFFERENT_ADDRESS_SOFIA.get('street_bl'), 'street_bl')
        self.assertXPathNodeText(different_address_sofia_xml, DIFFERENT_ADDRESS_SOFIA.get('quarter'), 'quarter')

    # authenticate=False
    def test_given_extra_data_as_other(self):
        street_other_included_xml = self.test_instance.xml_builder(STREET_OTHER_INCLUDED)
        self.assertXPathNodeText(street_other_included_xml, STREET_OTHER_INCLUDED.get('city'), 'city')
        self.assertXPathNodeText(street_other_included_xml, STREET_OTHER_INCLUDED.get('post_code'), 'post_code')
        self.assertXPathNodeText(street_other_included_xml, STREET_OTHER_INCLUDED.get('street'), 'street')
        self.assertXPathNodeText(street_other_included_xml, STREET_OTHER_INCLUDED.get('street_num'), 'street_num')
        self.assertXPathNodeText(street_other_included_xml, STREET_OTHER_INCLUDED.get('street_other'), 'street_other')

    def test_given_address_in_different_city(self):
        different_city_xml = self.test_instance.xml_builder(DIFFERENT_CITY)
        self.assertXPathNodeText(different_city_xml, DIFFERENT_CITY.get('city'), 'city')
        self.assertXPathNodeText(different_city_xml, DIFFERENT_CITY.get('post_code'), 'post_code')
        self.assertXPathNodeText(different_city_xml, DIFFERENT_CITY.get('quarter'), 'quarter')

    def test_given_just_pcode(self):
        no_city_yes_pcode_xml = self.test_instance.xml_builder(NO_CITY_YES_PCODE)
        self.assertXPathNodeText(no_city_yes_pcode_xml, NO_CITY_YES_PCODE.get('city'), 'city')
        self.assertXPathNodeText(no_city_yes_pcode_xml, NO_CITY_YES_PCODE.get('post_code'), 'post_code')
        self.assertXPathNodeText(no_city_yes_pcode_xml, NO_CITY_YES_PCODE.get('quarter'), 'quarter')

    def test_given_no_values(self):
        no_values_xml = self.test_instance.xml_builder(NO_VALUES)
        self.assertXPathNodeText(no_values_xml, NO_VALUES.get('city'), 'city')
        self.assertXPathNodeText(no_values_xml, NO_VALUES.get('post_code'), 'post_code')
        self.assertXPathNodeText(no_values_xml, NO_VALUES.get('street'), 'street')
        self.assertXPathNodeText(no_values_xml, NO_VALUES.get('street_bl'), 'street_bl')
        self.assertXPathNodeText(no_values_xml, NO_VALUES.get('quarter'), 'quarter')

    def test_given_pcode_does_not_match_city(self):
        faulty_pcode_xml = self.test_instance.xml_builder(FAULTY_PCODE)
        self.assertXPathNodeText(faulty_pcode_xml, FAULTY_PCODE.get('city'), 'city')
        self.assertXPathNodeText(faulty_pcode_xml, FAULTY_PCODE.get('post_code'), 'post_code')
        self.assertXPathNodeText(faulty_pcode_xml, FAULTY_PCODE.get('street'), 'street')
        self.assertXPathNodeText(faulty_pcode_xml, FAULTY_PCODE.get('street_num'), 'street_num')
        self.assertXPathNodeText(faulty_pcode_xml, FAULTY_PCODE.get('street_other'), 'street_other')

    def test_given_only_city(self):
        just_city_xml = self.test_instance.xml_builder(JUST_CITY)
        self.assertXPathNodeText(just_city_xml, JUST_CITY.get('city'), 'city')
        self.assertXPathNodeText(just_city_xml, JUST_CITY.get('post_code'), 'post_code')
        self.assertXPathNodeText(just_city_xml, JUST_CITY.get('street'), 'street')
        self.assertXPathNodeText(just_city_xml, JUST_CITY.get('street_bl'), 'street_bl')
        self.assertXPathNodeText(just_city_xml, JUST_CITY.get('quarter'), 'quarter')

    def test_given_no_pcode_and_no_city(self):
        no_city_no_pcode_xml = self.test_instance.xml_builder(NO_CITY_NO_PCODE)
        self.assertXPathNodeText(no_city_no_pcode_xml, NO_CITY_NO_PCODE.get('city'), 'city')
        self.assertXPathNodeText(no_city_no_pcode_xml, NO_CITY_NO_PCODE.get('post_code'), 'post_code')
        self.assertXPathNodeText(no_city_no_pcode_xml, NO_CITY_NO_PCODE.get('street'), 'street')
        self.assertXPathNodeText(no_city_no_pcode_xml, NO_CITY_NO_PCODE.get('street_num'), 'street_num')
        self.assertXPathNodeText(no_city_no_pcode_xml, NO_CITY_NO_PCODE.get('quarter'), 'quarter')

    def test_given_city_not_in_bg(self):
        not_in_bg_xml = self.test_instance.xml_builder(NOT_IN_BG)
        self.assertXPathNodeText(not_in_bg_xml, NOT_IN_BG.get('city'), 'city')
        self.assertXPathNodeText(not_in_bg_xml, NOT_IN_BG.get('post_code'), 'post_code')
        self.assertXPathNodeText(not_in_bg_xml, NOT_IN_BG.get('street'), 'street')
        self.assertXPathNodeText(not_in_bg_xml, NOT_IN_BG.get('street_bl'), 'street_bl')
        self.assertXPathNodeText(not_in_bg_xml, NOT_IN_BG.get('quarter'), 'quarter')

    def test_given_empty_dict(self):
        empty_dict_xml = self.test_instance.xml_builder(EMPTY_DICT)
        empty_xml = b'<?xml version="1.0" encoding="UTF-8" ?><request></request>'
        self.assertEqual(empty_dict_xml, empty_xml)
