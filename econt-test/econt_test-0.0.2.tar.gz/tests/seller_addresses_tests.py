import unittest
from unittest.mock import patch

from econt import api
from tests.credentials import USERNAME, PASSWORD


# template dictionary keys if address is present
TEMPLATE_ADDRESS_FORMAT = ('city_post_code', 'city', 'quarter',
                           'street', 'street_num', 'other')
XXX = '''
<response>
    <addresses>
        <e>
            <city_post_code>5800</city_post_code>
            <city>Плевен</city>
            <quarter></quarter>
            <street></street>
            <street_num></street_num>
            <other></other>
        </e>
    </addresses>
</response>
'''


class SellerAddressesTest(unittest.TestCase):
    def setUp(self):
        # assigning the addresses list to testing_instance
        with patch('requests.sessions.Session.post') as mock_post:
            mock_post.return_value.text = XXX
            self.testing_instance = api.Econt(USERNAME,
                                              PASSWORD).get_seller_addresses()
            self.testing_instance = self.testing_instance['data']['addresses']

    def test_if_not_empty_addresses_expect_template(self):
        if self.testing_instance:
            for dict_elem in self.testing_instance:
                self.assertTrue(all (key in dict_elem for key in TEMPLATE_ADDRESS_FORMAT))
