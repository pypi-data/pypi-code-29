import hashlib
import requests
import json
from web3 import Web3
from eth_account.messages import defunct_hash_message
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes, serialization
from cryptography.hazmat.primitives.asymmetric import ec

w3 = Web3()


def web3_sign(msg, private_key):
    """Message sign function with current private key
    Args:
        msg (str): A message to sign
    Returns:
        str: The signature.
    """
    if isinstance(msg, dict):
        msg = json.dumps(msg, sort_keys=True)

    if isinstance(msg, bytes):
        message_hash = defunct_hash_message(data=msg)
    else:
        message_hash = defunct_hash_message(text=msg)

    signed_message = w3.eth.account.signHash(
        message_hash, private_key=private_key
    )
    str_sign = '0x' + ''.join('{:02x}'.format(x)
                              for x in signed_message.signature)
    return str_sign


def web3_recover_address(msg, signature):
    """Recover address from message and signature
    Args:
        msg (str): A message to recover
        signature (str): A signature to generated with
                            private key and above message
    Returns:
        str: The recovered address.
    """
    if isinstance(msg, dict):
        msg = json.dumps(msg, sort_keys=True)

    message_hash = defunct_hash_message(text=msg)
    address = w3.eth.account.recoverHash(message_hash, signature=signature)
    return address


def web3_verify(msg, signature, address):
    """Verify message and siganture using private key
    Args:
        msg (str): A message to verify
        signature (str): A signature to verify
    Returns:
        bool: True if successfully verify the message, False otherwise.
    """
    if isinstance(msg, dict):
        msg = json.dumps(msg, sort_keys=True)

    _address = web3_recover_address(msg, signature)
    return _address.lower() == address.lower()


def signer_verify(msg, signature, public_key_data):
    """Verify ECDSA signature and message using public key

    Args:
        msg (str or dict): A message to verify
        signature (str or bytes): A ECDSA signature to verify
        public_key (str or bytes): Public key to use for verification

    Returns:
        bool: True if successfully verify the message, False otherwise.
    """
    try:
        if isinstance(msg, dict):
            msg = json.dumps(msg, sort_keys=True)
        elif not isinstance(msg, str):
            raise Exception("Invalid msg type")

        if isinstance(signature, str):
            signature = bytes.fromhex(signature)
        elif not isinstance(signature, bytes):
            raise Exception("Invalide signature type")

        if isinstance(public_key_data, str):
            public_key_data = public_key_data.encode()
        elif not isinstance(public_key_data, bytes):
            raise Exception("Invalid public key data type")

        # Genereate public key instance
        public_key = serialization.load_pem_public_key(
            public_key_data, backend=default_backend())
        if not isinstance(public_key, ec.EllipticCurvePublicKey):
            raise Exception("Invalid public key")

        # Verify message and signature
        public_key.verify(signature, msg.encode(), ec.ECDSA(hashes.SHA256()))
    except Exception as e:
        print(str(e))
        return False

    return True


def hash(msg):
    if isinstance(msg, dict):
        msg = json.dumps(msg, sort_keys=True)

    message_hash = defunct_hash_message(text=msg) # hex value
    str_msg = '0x' + ''.join('{:02x}'.format(x)
                              for x in message_hash)
    return str_msg
