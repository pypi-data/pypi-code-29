import unittest
from unittest.mock import patch

from econt import api
from tests.credentials import USERNAME, PASSWORD

INVALID_RESPONSE_XML = '''
<response>
    <shipments>
        <e>
            <loading_num>hakithebest</loading_num>
            <errorCode>econt\classes\ExInvalidParam</errorCode>
            <error>Не е намерена пратка с номер hakithebest.</error>
        </e>
    </shipments>
</response>
'''


class RetrieveShipmentInfoTest(unittest.TestCase):
    def setUp(self):
        self.test_instance = api.Econt(USERNAME, PASSWORD)

    def test_invalid_input_expect_none_data(self):
        with patch('requests.sessions.Session.post') as mock_post:
            invalid_input = ['hakithebest']
            result = self.test_instance.retrieve_shipment_info(invalid_input)
            mock_post.return_value.text = INVALID_RESPONSE_XML
            self.assertIsNone(result['data'])
