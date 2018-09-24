import re
from functools import wraps

import requests

from . import currency_to_ufoshi
from .meta import Unspent

DEFAULT_TIMEOUT = 10


class NoAPIKey(Exception):
    pass


def requires_key(f):
    @wraps(f)
    def decorator(*args, **kwargs):
        if not config['api_key']:
            raise NoAPIKey('Set ufobit.config["api_key"] to your CryptoID API key.')
        return f(*args, **kwargs)
    return decorator


def set_service_timeout(seconds):
    global DEFAULT_TIMEOUT
    DEFAULT_TIMEOUT = seconds


class UFO(CryptoidAPI):
    MAIN_ENDPOINT = 'https://explorer.ufobject.com/api'

    @classmethod
    def broadcast_tx(cls, tx_hex):
        r = requests.post(
            cls.MAIN_ENDPOINT + '/tx/send',
            headers={"Content-Type": "application/x-www-form-urlencoded"},
            data={'rawtx': tx_hex}
        )
        r.raise_for_status()
        if r.text == '0':
            return False
        return r.json()['txid']

    @classmethod
    def get_tx(cls, txid):
        r = requests.get(cls.MAIN_ENDPOINT + f'/tx/{txid}')
        r.raise_for_status()
        if r.text == '0':
            return False
        return r.json()

    @classmethod
    def get_unspent(cls, address):
        r = requests.get(cls.MAIN_ENDPOINT + f'/addr/{address}/utxo')
        r.raise_for_status()
        return [
                   Unspent(int(tx['satoshis']),
                           tx['confirmations'],
                           tx['scriptPubKey'],
                           tx['txid'],
                           tx['vout'],
                           True if tx['address'][0] == 'U' else False)  # sic! typo in api itself
                   for tx in r.json()
               ][::-1]

    @classmethod
    def get_balance(cls, address):
        r = requests.get(cls.MAIN_ENDPOINT + f'/addr/{address}/balance')
        r.raise_for_status()
        print(r.json())
        return r.json()

    @classmethod
    def get_transactions(cls, address):
        r = requests.get(cls.MAIN_ENDPOINT + f'addr/{address}')
        r.raise_for_status()
        return [tx['txid'] for tx in r.json()['txs']]


class NetworkAPI:
    IGNORED_ERRORS = (ConnectionError,
                      requests.exceptions.ConnectionError,
                      requests.exceptions.Timeout,
                      requests.exceptions.ReadTimeout)

    GET_BALANCE_MAIN = [UFO.get_balance]
    GET_TRANSACTIONS_MAIN = [UFO.get_transactions]
    GET_UNSPENT_MAIN = [UFO.get_unspent]
    BROADCAST_TX_MAIN = [UFO.broadcast_tx]
    GET_TX_MAIN = [UFO.get_tx]

    @classmethod
    def get_tx(cls, txid):
        for api_call in cls.GET_TX_MAIN:
            try:
                return api_call(txid)
            except cls.IGNORED_ERRORS:
                pass

        raise ConnectionError('All APIs are unreachable.')

    @classmethod
    def get_balance(cls, address):
        """Gets the balance of an address in satoshi.

        :param address: The address in question.
        :type address: ``str``
        :raises ConnectionError: If all API services fail.
        :rtype: ``int``
        """

        for api_call in cls.GET_BALANCE_MAIN:
            try:
                return api_call(address)
            except cls.IGNORED_ERRORS:
                pass

        raise ConnectionError('All APIs are unreachable.')

    @classmethod
    def get_transactions(cls, address):
        """Gets the ID of all transactions related to an address.

        :param address: The address in question.
        :type address: ``str``
        :raises ConnectionError: If all API services fail.
        :rtype: ``list`` of ``str``
        """

        for api_call in cls.GET_TRANSACTIONS_MAIN:
            try:
                return api_call(address)
            except cls.IGNORED_ERRORS:
                pass

        raise ConnectionError('All APIs are unreachable.')

    @classmethod
    def get_unspent(cls, address):
        """Gets all unspent transaction outputs belonging to an address.

        :param address: The address in question.
        :type address: ``str``
        :raises ConnectionError: If all API services fail.
        :rtype: ``list`` of :class:`~bit.network.meta.Unspent`
        """

        for api_call in cls.GET_UNSPENT_MAIN:
            try:
                return api_call(address)
            except cls.IGNORED_ERRORS:
                pass

        raise ConnectionError('All APIs are unreachable.')

    @classmethod
    def broadcast_tx(cls, tx_hex):  # pragma: no cover
        """Broadcasts a transaction to the blockchain.

        :param tx_hex: A signed transaction in hex form.
        :type tx_hex: ``str``
        :raises ConnectionError: If all API services fail.
        """
        success = None

        for api_call in cls.BROADCAST_TX_MAIN:
            try:
                c = api_call(tx_hex)
                if not c:
                    continue
                return c
            except cls.IGNORED_ERRORS:
                pass

        if success is False:
            raise ConnectionError('Transaction broadcast failed, or '
                                  'Unspents were already used.')

        raise ConnectionError('All APIs are unreachable.')
