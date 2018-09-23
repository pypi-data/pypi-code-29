"""This is the main layer provider module
This module contains a class Provider which
contains all methods provided in Layer
"""
import time
import json
import datetime
from layer import common
from layer.signer import Signer
from layer.layernode import DEFAULT_LAYERNODE_ENDPOINT
import requests


class Provider:
    """Provider class which provides handy methods of Layer
    Attributes:
        address (str): An ethereum address setten in constructor
        private_key (str): An ethereum private key matched with above address
    """

    address = None  # ETH address
    private_key = None  # ETH private key matched with the address
    signer = None
    layernode_endpoint = None

    def __init__(self, address, private_key, layernode_endpoint=DEFAULT_LAYERNODE_ENDPOINT, signer_endpoint=None):
        """Provider constructor
        Args:
            address (str): An ethereum address
            private_key (str): An ethereum private key
                                matched with address
        """
        self.address = address.lower()
        self.private_key = private_key
        self.signer = Signer(signer_endpoint)
        self.layernode_endpoint = layernode_endpoint

    def sign(self, msg):
        """Message sign function with current private key
        Args:
            msg (str): A message to sign
        Returns:
            str: The signature.
        """
        return common.web3_sign(msg, self.private_key)

    def recover_address(self, msg, signature):
        """Recover address from message and signature
        Args:
            msg (str): A message to recover
            signature (str): A signature to generated with
                                private key and above message
        Returns:
            str: The recovered address.
        """
        return common.web3_recover_address(msg, signature)

    def verify(self, msg, signature):
        """Verify message and siganture using private key
        Args:
            msg (str): A message to verify
            signature (str): A signature to verify
        Returns:
            bool: True if successfully verify the message, False otherwise.
        """
        return common.web3_verify(msg, signature, self.address)

    def get_key_hashes(self):
        """Get key hashes array from signer server
        Returns:
            array: Array of key hashes.
        """
        return self.signer.get_key_hashes()

    def get_key_detail(self, key_hash):
        """Get key details from a key hash
        Args:
            key_hash (str): A hash of a key to get detail
        Returns:
            map: A map object which contains public key, algorithm ...
        """
        return self.signer.get_key_detail(key_hash)

        # try:
        #     res = self.signer.get_key_detail(key_hash)
        #     if res['status'] == 200:
        #         return {
        #             'hash': res['data']['hash'],
        #             'algorithm': res['data']['algorithm'],
        #             'public_key': base64.b64decode(res['data']['publicKey'].encode()).decode(),
        #             'created_at': res['data']['createdAt'],
        #         }
        #     else:
        #         return None
        # except Exception as e:
        #     return None

    def get_key_hash(self, type):
        """Get key_hash to generate signer_sig"""
        return self.signer.get_key_by_type(type)
        # try:
        #     res = self.signer.get_key_by_type(type)
        #     if res['status'] == 200:
        #         return res['data']
        #     else:
        #         return None
        # except Exception as e:
        #     return None

    def submit_identity(self, identity_hash: str, key_hash: str) -> map:
        """Send identity registeration request to layer node"""

        # Provider raw identity request
        provider_request = {
            "hash": identity_hash,
            "address": self.address,
            "keyHash": key_hash,
            # "timestamp": datetime.datetime.utcnow().replace(tzinfo=datetime.timezone.utc).isoformat()
        }

        # Sign with provider's private key
        provider_sig = self.sign(provider_request)

        # Signing request to signer
        signer_request = {
            'provider_request': provider_request,
            'provider_sig': provider_sig
        }

        # Get signer signature
        signer_sig = self.signer.get_signature(
            json.dumps(signer_request, sort_keys=True), key_hash)

        if not signer_sig:
            return None

        # Final request to layer node
        full_request = {
            'signer_request': signer_request,
            'signer_sig': signer_sig
        }
        # print(full_request)

        # {
        #     'signer_request': {
        #         'provider_request': {
        #             'address': '0x011a28420578a06728dd537754d0f3d9b73e5f57',
        #             'keyHash': '1413f5327216dca7ed7b7f8632d2a203a0892aba',
        #             'hash': 'Hello World'
        #         },
        #         'provider_sig': '0xa2f74a9f636da1ccc37e193a27564939aeb9692694b69b4ddd6a21e964de6686417934225e06ecab3c4693b6364d2078e03f1989e52c595b079b66fcf7b10bdd1b'
        #     },
        #     'signer_sig': '3065023100fbe668f78bc6ef9ecf078d9aacf40617883a1d6dc079222d01cc1aa92f1c9e7542858fa2ad75253cbe1bc1476de181f5023079d92b41b2f0c3ec4a4fef96bb33b06b4b75040e45851716ec531d625c17d536dcee1f79aab28e109f385b867dfc520d'
        # }

        res = requests.post(
            self.layernode_endpoint + '/add_identity',
            data=json.dumps(full_request, sort_keys=True),
            headers={'content-type': 'application/json'}
        )

        return res.json()
        # return full_request

    def submit_score(self, identity_hash: str, key_hash: str, score: int, category: str) -> map:
        """Send score registeration request to layer node"""

        # Provider raw identity request
        provider_request = {
            "hash": identity_hash,
            "address": self.address,
            "keyHash": key_hash,
            "score": score,
            "category": category
            # "timestamp": datetime.datetime.utcnow().replace(tzinfo=datetime.timezone.utc).isoformat()
        }

        # Sign with provider's private key
        provider_sig = self.sign(provider_request)

        # Signing request to signer
        signer_request = {
            'provider_request': provider_request,
            'provider_sig': provider_sig
        }

        # Get signer signature
        signer_sig = self.signer.get_signature(
            json.dumps(signer_request, sort_keys=True), key_hash)

        if not signer_sig:
            return None

        # Final request to layer node
        full_request = {
            'signer_request': signer_request,
            'signer_sig': signer_sig
        }

        # print(full_request)
        # {
        #     'signer_request': {
        #         'provider_request': {
        #             'address': '0x011a28420578a06728dd537754d0f3d9b73e5f57',
        #             'keyHash': '1413f5327216dca7ed7b7f8632d2a203a0892aba',
        #             'hash': 'Hello World'
        #             "score":2,
        #             "category":"ProviderTransactionCategory"
        #         },
        #         'provider_sig': '0xa2f74a9f636da1ccc37e193a27564939aeb9692694b69b4ddd6a21e964de6686417934225e06ecab3c4693b6364d2078e03f1989e52c595b079b66fcf7b10bdd1b'
        #     },
        #     'signer_sig': '3065023100fbe668f78bc6ef9ecf078d9aacf40617883a1d6dc079222d01cc1aa92f1c9e7542858fa2ad75253cbe1bc1476de181f5023079d92b41b2f0c3ec4a4fef96bb33b06b4b75040e45851716ec531d625c17d536dcee1f79aab28e109f385b867dfc520d'
        # }

        res = requests.post(
            self.layernode_endpoint + '/add_score',
            data=json.dumps(full_request, sort_keys=True),
            headers={'content-type': 'application/json'}
        )

        return res.json()
        # return full_request

    def get_score(self, hash: str) -> map:
        """Send score get request to layer node"""

        # Provider raw identity request
        provider_request = {
            "hash": hash,
            "address": self.address,
            "timestamp": int(time.time())
        }

        # Sign with provider's private key
        provider_sig = self.sign(provider_request)

        # Signing request to signer
        full_request = {
            'provider_request': provider_request,
            'provider_sig': provider_sig
        }

        # {
        #     "provider_request": {
        #         "hash": "9ds03290dsalk3jkidka23lsfjomvio3zxpoiu0dsajfi",
        #         "address": "0xProviderAddressFromSdk",
        #         "timestamp": 1527764842,
        #     }
        #     "provider_sig": "0d9sa90f/d9sa0f09dsa89d0sa8/fd90sa8f9-08s9df0-as 7d89f7890?fsd89/0xvhuionv"
        # }

        res = requests.post(
            self.layernode_endpoint + '/get_score',
            data=json.dumps(full_request, sort_keys=True),
            headers={'content-type': 'application/json'}
        )

        return res.json()
        # return full_request
