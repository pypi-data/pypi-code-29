import unittest

from betdaq.apiclient import APIClient
from betdaq.endpoints import Betting, Account, MarketData, Trading


class APIClientTest(unittest.TestCase):

    def test_api_client_init(self):
        client = APIClient('username', 'password')
        self.assertEqual(str(client), 'APIClient')
        self.assertEqual(repr(client), '<APIClient [username]>')
        self.assertIsInstance(client.betting, Betting)
        self.assertIsInstance(client.account, Account)
        self.assertIsInstance(client.marketdata, MarketData)
        self.assertIsInstance(client.trading, Trading)
