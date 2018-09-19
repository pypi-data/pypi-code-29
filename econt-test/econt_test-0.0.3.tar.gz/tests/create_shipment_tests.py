import unittest

from unittest.mock import patch
from econt import api
from econt.status_codes import StatusCode
from tests.credentials import USERNAME, PASSWORD


SENDER_DATA = {
    'city_en': 'Ruse',
    'post_code': '7000',
    'office_code': '7000',
    'name': 'Иван Иванов',
    'phone_num': '08888888888'
}
RECEIVER_DATA = {
    'city_en': 'Sofia',
    'post_code': '1505',
    'name': 'Петър Иванов',
    'phone_num': '08888888888',
    'street': 'Славянска',
    'street_num': '16'
}
SHIPMENT_DATA = {
    'envelope_num': '111111,22222,3332342',
    'shipment_type': 'PACK',
    'description': 'description of the content content',
    'pack_count': '3',
    'weight': '1',
    'tariff_sub_code': 'OFFICE_DOOR',
    'pay_after_accept': '1',
    'pay_after_test': '0'
}
SERVICES_DATA = {
    'dc': 'ON',
    'oc': '44.99',
    'cd': '44.99',
    'cd_currency': 'BGN',
    'cd_pay_options': {
        'name': 'Иван Иванов',
        'phone': '08888888888',
        'money_transfer': '0',
        'method': 'door',
        'city': 'Sofia',
        'post_code': '1505',
        'quarter': 'gk Suhata Reka',
        'street': 'bul. Botevgradsko Shose',
        'street_num': '49'
    }
}
PAYMENT_DATA = {
    'side': 'SENDER',
    'method': 'CASH'
}
INSTRUCTIONS_DATA = {
    'e': {
        'type': 'return',
        'delivery_fail_action': 'return_to_office',
        'return_name': 'Марин Маринов',
        'return_phone': '088888888',
        'return_email': 'ddd@ddd.dd',
        'return_city': 'Русе',
        'return_post_code': '7000',
        'return_office_code': '7004',
        'reject_delivery_payment_side': 'receiver',
        'reject_return_payment_side': 'sender'
    }
}

MOCK_CORRECT_INFO_DATA = '''<response>
    <result>
        <e>
            <loading_id>2018090000003116</loading_id>
            <loading_num>1051601425135</loading_num>
            <courier_request_id></courier_request_id>
            <delivery_date>2018-09-12</delivery_date>
            <loading_price>
                <C>6.3</C>
                <DC>3.5</DC>
                <OC>0.11</OC>
                <CD>1.08</CD>
                <total>10.99</total>
                <sender_total>10.99</sender_total>
                <receiver_total>0</receiver_total>
                <other_total>0</other_total>
                <currency>лв</currency>
                <currency_code>BGN</currency_code>
            </loading_price>
            <loading_discount/>
            <CD_percent>2.4</CD_percent>
            <error></error>
            <error_code></error_code>
            <pdf_url>http://demo.econt.com/ee/api_export.php?exportMethod=printLoading&amp;loading_num=1051601425135&amp;_key=eda82e9392910a376c4a53102d5390381ce5dcd7&amp;</pdf_url>
            <return_reason/>
            <prev_parcel_num/>
            <next_parcels/>
        </e>
    </result>
    <pdf>
        <blank_yes>
            <![CDATA[
http://demo.econt.com/e-econt/api/api_pdf_shipment.php?user=demo&print_media=template&nums[]=1051601425135
]]>
        </blank_yes>
        <blank_no>
            <![CDATA[
http://demo.econt.com/e-econt/api/api_pdf_shipment.php?user=demo&print_media=double&nums[]=1051601425135
]]>
        </blank_no>
    </pdf>
</response>'''

MOCK_VALIDATE_OR_CALC_IS_1_DATA = '''<response>
    <result>
        <e>
            <loading_id></loading_id>
            <loading_num></loading_num>
            <courier_request_id></courier_request_id>
            <delivery_date>2018-09-12</delivery_date>
            <loading_price>
                <C>6.3</C>
                <DC>3.5</DC>
                <OC>0.11</OC>
                <CD>1.08</CD>
                <total>10.99</total>
                <sender_total>10.99</sender_total>
                <receiver_total>0</receiver_total>
                <other_total>0</other_total>
                <currency>лв</currency>
                <currency_code>BGN</currency_code>
            </loading_price>
            <loading_discount/>
            <CD_percent>2.4</CD_percent>
            <error></error>
            <error_code></error_code>
            <pdf_url/>
            <return_reason/>
            <prev_parcel_num/>
            <next_parcels/>
        </e>
    </result>
    <pdf/>
</response>'''

MOCK_FAULTY_REQUEST_SENDER_PCODE = '''<response>
    <result>
        <e>
            <loading_id></loading_id>
            <loading_num></loading_num>
            <courier_request_id></courier_request_id>
            <delivery_date></delivery_date>
            <loading_price>
                <total>0</total>
                <sender_total>0</sender_total>
                <receiver_total>0</receiver_total>
                <other_total>0</other_total>
                <currency/>
                <currency_code/>
            </loading_price>
            <loading_discount/>
            <error>Условия за изплащане на наложен платеж: Несъответствие между населено място и пощенски код.</error>
            <error_code>econt\classes\ExInvalidParam</error_code>
            <pdf_url/>
            <return_reason/>
            <prev_parcel_num/>
            <next_parcels/>
        </e>
    </result>
    <pdf/>
</response>'''

MOCK_ERROR_CASE_GIVEN_EMAIL = '''<response>
    <result>
        <message>Request is accepted for processing</message>
    </result>
</response>'''

MOCK_ERROR_CASE_GIVEN_EMAIL_AND_VALID_OR_CALC_IS_1 = '''<response>
    <result>
        <e>
            <loading_id></loading_id>
            <loading_num></loading_num>
            <courier_request_id></courier_request_id>
            <delivery_date></delivery_date>
            <loading_price>
                <total>0</total>
                <sender_total>0</sender_total>
                <receiver_total>0</receiver_total>
                <other_total>0</other_total>
                <currency/>
                <currency_code/>
            </loading_price>
            <loading_discount/>
            <error>Условия за изплащане на наложен платеж: Несъответствие между населено място и пощенски код.</error>
            <error_code>econt\classes\ExInvalidParam</error_code>
            <pdf_url/>
            <return_reason/>
            <prev_parcel_num/>
            <next_parcels/>
        </e>
    </result>
    <pdf/>
</response>'''


class ShipmentTest(unittest.TestCase):
    def setUp(self):
        self.test_instance = api.Econt(USERNAME, PASSWORD)
        self.faulty_services_data = {
            'dc': 'ON',
            'oc': '44.99',
            'cd': '44.99',
            'cd_currency': 'BGN',
            'cd_pay_options': {
                'name': 'Иван Иванов',
                'phone': '08888888888',
                'money_transfer': '0',
                'method': 'door',
                'city': 'Sofia',
                'post_code': '6800',
                'quarter': 'gk Suhata Reka',
                'street': 'bul. Botevgradsko Shose',
                'street_num': '49'
            }
        }

    def test_correct_info_given(self):
        with patch('requests.sessions.Session.post') as mock_result:
            mock_result.return_value.text = MOCK_CORRECT_INFO_DATA
            test_shipment = self.test_instance.create_shipment(
                SENDER_DATA, RECEIVER_DATA, SHIPMENT_DATA, SERVICES_DATA,
                PAYMENT_DATA, INSTRUCTIONS_DATA)
            self.assertIsNotNone(test_shipment['data']['pdf'])

    def test_validate_is_1(self):
        with patch('requests.sessions.Session.post') as mock_result:
            mock_result.return_value.text = MOCK_VALIDATE_OR_CALC_IS_1_DATA
            test_shipment = self.test_instance.validate_shipment(
                SENDER_DATA, RECEIVER_DATA, SHIPMENT_DATA, SERVICES_DATA,
                PAYMENT_DATA, INSTRUCTIONS_DATA)
            self.assertIsNotNone(test_shipment['data']['result'])
            self.assertIsNone(test_shipment['data']['pdf'])

    def test_calculate_is_1(self):
        with patch('requests.sessions.Session.post') as mock_result:
            mock_result.return_value.text = MOCK_VALIDATE_OR_CALC_IS_1_DATA
            test_shipment = self.test_instance.calculate_shipment_price(
                SENDER_DATA, RECEIVER_DATA, SHIPMENT_DATA, SERVICES_DATA,
                PAYMENT_DATA, INSTRUCTIONS_DATA)
            self.assertIsNotNone(test_shipment['data']['result'])
            self.assertIsNone(test_shipment['data']['pdf'])

    def test_faulty_request_sender_pcode(self):
        with patch('requests.sessions.Session.post') as mock_result:
            mock_result.return_value.text = MOCK_FAULTY_REQUEST_SENDER_PCODE
            test_shipment = self.test_instance.create_shipment(
                SENDER_DATA, RECEIVER_DATA, SHIPMENT_DATA,
                self.faulty_services_data, PAYMENT_DATA, INSTRUCTIONS_DATA)
            self.assertIsNone(test_shipment['data'])
            self.assertEqual(test_shipment['status'],
                             StatusCode.ECONT_API_XML_ERROR)

    def test_error_case_given_email(self):
        with patch('requests.sessions.Session.post') as mock_result:
            mock_result.return_value.text = MOCK_ERROR_CASE_GIVEN_EMAIL
            test_shipment = self.test_instance.create_shipment(
                SENDER_DATA, RECEIVER_DATA, SHIPMENT_DATA,
                self.faulty_services_data, PAYMENT_DATA, INSTRUCTIONS_DATA,
                error_email='error_email@gmail.com')
            self.assertNotEqual(test_shipment['message'], 'OK')

    def test_error_case_given_email_valid_1(self):
        with patch('requests.sessions.Session.post') as mock_result:
            mock_result.return_value.text = MOCK_ERROR_CASE_GIVEN_EMAIL_AND_VALID_OR_CALC_IS_1
            test_shipment = self.test_instance.validate_shipment(
                SENDER_DATA, RECEIVER_DATA, SHIPMENT_DATA,
                self.faulty_services_data,
                PAYMENT_DATA, INSTRUCTIONS_DATA,
                error_email='error_email@gmail.com')
            self.assertEqual(StatusCode.ECONT_API_XML_ERROR,
                             test_shipment['status'])
            self.assertNotEqual(test_shipment['message'], 'OK')

    def test_error_case_given_email_calc_1(self):
        with patch('requests.sessions.Session.post') as mock_result:
                mock_result.return_value.text = MOCK_ERROR_CASE_GIVEN_EMAIL_AND_VALID_OR_CALC_IS_1
                test_shipment = self.test_instance.calculate_shipment_price(
                    SENDER_DATA, RECEIVER_DATA, SHIPMENT_DATA,
                    self.faulty_services_data,
                    PAYMENT_DATA, INSTRUCTIONS_DATA,
                    error_email='error_email@gmail.com')
                self.assertEqual(StatusCode.ECONT_API_XML_ERROR,
                                 test_shipment['status'])
                self.assertNotEqual(test_shipment['message'], 'OK')
