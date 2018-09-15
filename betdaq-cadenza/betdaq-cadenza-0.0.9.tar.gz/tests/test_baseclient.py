
import unittest
from zeep import Client

from betdaq.baseclient import BaseClient


class BaseClientTest(unittest.TestCase):

    def test_base_client_init(self):
        client = BaseClient(username='username', password='password')
        self.assertEqual(client.username, 'username')
        self.assertEqual(client.password, 'password')
        self.assertEqual(client.wsdl_file, 'https://api.betdaq.com/v2.0/API.wsdl')
        self.assertDictEqual(client.external_headers, {"version": 2.0, "languageCode": 'en', "username": 'username',
                                                       "password": 'password', "applicationIdentifier": None})

        self.assertIsInstance(client.secure_client, Client)
        self.assertIsInstance(client.readonly_client, Client)
