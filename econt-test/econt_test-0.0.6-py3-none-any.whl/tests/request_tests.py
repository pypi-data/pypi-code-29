import unittest
import requests
from unittest.mock import patch
from xml.parsers.expat import ExpatError

from econt import api
from econt.status_codes import StatusCode
from tests.credentials import USERNAME, PASSWORD


# Required because request is a method of Econt class
TESTING_INSTANCE = api.Econt(USERNAME, PASSWORD)

# STATUS MESSAGE DICTIONARIES
STATUS_ERROR_URL = {
    'status': StatusCode.EMPTY_URL_ERROR,
    'message': 'Please provide http:// or https://!',
    'data': None
}
STATUS_ERROR_XML = {
    'status': StatusCode.XML_PARSE_ERROR,
    'message': 'invalid XML',
    'data': None
}
CONNECTION_ERROR = {
    'data': None,
    'message': 'There has been a connection error!',
    'status': StatusCode.CONNECTION_ERROR
}
XML_PARSE_ERROR = {
    'data': None,
    'message': 'XML parsing failed!',
    'status': StatusCode.XML_PARSE_ERROR
}
UNEXPECTED_ERROR = {
    'data': None,
    'message': 'An unexpected error occurred!',
    'status': StatusCode.UNEXPECTED_ERROR
}
ECONT_API_XML_ERROR = {
    'data': None,
    'message': 'Съдържанието на файла е некоректно!',
    'status': 5
}

# invalid url
INVALID_URL = 'loremipsum'
EMPTY_URL=''

# valid XML
MELON_SOFIA_ADDRESS = ''' 
<request>
  <client>
    <username>demo_django</username>
    <password>djangoshoptestpassword</password>
  </client>
  <request_type>check_address</request_type>
  <address>
    <city>Sofia</city>
    <post_code>1113</post_code>
    <street>Kosta Lulchev</street>
    <street_num>20</street_num>
    <street_et>3</street_et>
  </address>
  <system>
    <validate>
        <response_type>xml</response_type>
    </validate>
  </system>
</request> 
'''

# invalid XML
EMPTY_XML = ''
INVALID_XML = 'FORKBOMBAAAAAAAAAAAA'

# expected
EXPECTED_MELON_SOFIA_ADDRESS_RESPONSE_FROM_ECONT = ''' <?xml version='1.0' encoding='UTF-8'?>
<response>
  <address>
    <city>Sofia</city>
    <post_code>1000</post_code>
    <office_code></office_code>
    <quarter></quarter>
    <street>ul. Kosta Lulchev</street>
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
EXPECTED_INVALID_XML_RESPONSE_FROM_ECONT = '''<?xml version='1.0' encoding='UTF-8'?>
<response>
  <error>
    <code>API_ERR_INVALID_XML1</code>
    <message>Съдържанието на файла е некоректно!</message>
  </error>
</response>
'''


class RequestTest(unittest.TestCase):
    def test_when_invalid_url_is_given_expect_status_error_url(self):
        with patch('requests.sessions.Session.post') as mock_post:
            mock_post.side_effect = requests.exceptions.MissingSchema
            self.assertDictEqual(TESTING_INSTANCE.request(INVALID_URL, MELON_SOFIA_ADDRESS), STATUS_ERROR_URL)

    def test_when_empty_XML_is_given_expect_value_error(self):
        with self.assertRaises(ValueError):
            TESTING_INSTANCE.request(api.ECONT_SERVICE_DEMO_URL, EMPTY_XML)

    def test_when_empty_strings_are_given_expect_status_error_url(self):
        with patch('requests.sessions.Session.post') as mock_post:
            mock_post.side_effect = requests.exceptions.MissingSchema
            self.assertDictEqual(TESTING_INSTANCE.request(EMPTY_URL, INVALID_XML), STATUS_ERROR_URL)

    def test_when_invalid_xml_is_given_expect_status_error_xml(self):
        with patch('requests.sessions.Session.post') as mock_post:
            mock_post.return_value.text = INVALID_XML
            self.assertNotEqual(TESTING_INSTANCE.request(api.ECONT_SERVICE_DEMO_URL, INVALID_XML),
                                EXPECTED_INVALID_XML_RESPONSE_FROM_ECONT)

    def test_when_melon_address_is_given_expect_validation(self):
        with patch('requests.sessions.Session.post') as mock_post:
            mock_post.return_value.text = MELON_SOFIA_ADDRESS
            self.assertNotEqual(TESTING_INSTANCE.request(api.ECONT_SERVICE_DEMO_URL, MELON_SOFIA_ADDRESS),
                                EXPECTED_MELON_SOFIA_ADDRESS_RESPONSE_FROM_ECONT)

    def test_connection_error(self):
        with patch('requests.sessions.Session.post') as mock_post:
            mock_post.side_effect = requests.exceptions.ConnectionError
            self.assertDictEqual(TESTING_INSTANCE.request(api.ECONT_SERVICE_DEMO_URL, MELON_SOFIA_ADDRESS),
                                 CONNECTION_ERROR)

    def test_xml_parse_error(self):
        with patch('requests.sessions.Session.post') as mock_post:
            mock_post.side_effect = ExpatError
            self.assertDictEqual(TESTING_INSTANCE.request(api.ECONT_SERVICE_DEMO_URL, MELON_SOFIA_ADDRESS),
                                 XML_PARSE_ERROR)

    def test_econt_api_xml_error(self):
        with patch('requests.sessions.Session.post') as mock_post:
            mock_post.return_value.text = EXPECTED_INVALID_XML_RESPONSE_FROM_ECONT
            self.assertDictEqual(TESTING_INSTANCE.request(api.ECONT_SERVICE_URL, MELON_SOFIA_ADDRESS),
                                 ECONT_API_XML_ERROR)

    def test_unexpected_error(self):
        with patch('requests.sessions.Session.post') as mock_post:
            mock_post.return_value.text = {'dict_key': 'dict_value'}
            self.assertDictEqual(TESTING_INSTANCE.request(api.ECONT_SERVICE_DEMO_URL, MELON_SOFIA_ADDRESS),
                                 UNEXPECTED_ERROR)
