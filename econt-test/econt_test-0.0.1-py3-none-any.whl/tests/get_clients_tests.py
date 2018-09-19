import unittest

from unittest.mock import patch
from econt.api import Econt
from tests.credentials import USERNAME, PASSWORD

# template dictionary keys if address is present
TEMPLATE_CLIENTS_SET = {'id', 'ein', 'name',
                           'name_en', 'client_type', 'key_word',
                           'cd_agreements', 'instructions'}

MOCK_XML_RESPONSE_DATA = '''<response>
    <clients>
        <client>
            <id>15053708</id>
            <ein>8308074005</ein>
            <name>Ангел Антонов Данаилов</name>
            <name_en>Angel Antonov Danailov</name_en>
            <client_type>private</client_type>
            <key_word></key_word>
            <cd_agreements>
                <cd_agreement>
                    <id>15375</id>
                    <num>CD38791</num>
                    <is_bank>0</is_bank>
                </cd_agreement>
                <cd_agreement>
                    <id>16668</id>
                    <num>CD38833</num>
                    <is_bank>0</is_bank>
                </cd_agreement>
            </cd_agreements>
            <instructions>
                <e>
                    <id>107382</id>
                    <type>return</type>
                    <template>за връщане</template>
                    <delivery_fail_action>return_to_office</delivery_fail_action>
                    <dp_payment_side>sender</dp_payment_side>
                    <reject_delivery_payment_side>receiver</reject_delivery_payment_side>
                    <reject_return_payment_side>receiver</reject_return_payment_side>
                    <return_ap></return_ap>
                    <return_bl></return_bl>
                    <return_city>София</return_city>
                    <return_city_id>41</return_city_id>
                    <return_post_code>1000</return_post_code>
                    <return_email></return_email>
                    <return_et></return_et>
                    <return_face>лице име пешо</return_face>
                    <return_name>фирма име оод</return_name>
                    <return_office>София Студентски град</return_office>
                    <return_office_id>163</return_office_id>
                    <return_office_code>1009</return_office_code>
                    <return_other></return_other>
                    <return_phone>08864231423</return_phone>
                    <return_quarter></return_quarter>
                    <return_quarter_id>0</return_quarter_id>
                    <return_street></return_street>
                    <return_street_id>0</return_street_id>
                    <return_street_num></return_street_num>
                    <return_vh></return_vh>
                </e>
            </instructions>
        </client>
    </clients>
</response>'''


class GetClientsTest(unittest.TestCase):
    def setUp(self):
        # assigning the addresses list to testing_instance
        with patch('requests.sessions.Session.post') as mock_result:
            mock_result.return_value.text = MOCK_XML_RESPONSE_DATA
            self.all_clients_dict = Econt(username=USERNAME,
                                          password=PASSWORD).get_clients()

    def test_if_not_empty_clients_expect_template(self):
        single_client_dict = self.all_clients_dict['data']['clients']['client']
        if self.all_clients_dict['data']:
            self.assertTrue(set(single_client_dict).intersection(TEMPLATE_CLIENTS_SET) == TEMPLATE_CLIENTS_SET)