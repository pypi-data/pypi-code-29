import os

from web3.auto import (
    w3,
)

from request_network.constants import (
    PRIVATE_KEY_ENVIRONMENT_VARIABLE,
)
from request_network.exceptions import (
    ImproperlyConfigured,
)


def environment_variable_hash_signer(message_hash, address):
    """ Sign a message hash using a private key stored in an environment variable.
    """
    formatted_env_var = PRIVATE_KEY_ENVIRONMENT_VARIABLE.format(address)
    try:
        private_key = os.environ[formatted_env_var]
    except KeyError:
        raise ImproperlyConfigured('The {} environment variable is not set'.format(
            formatted_env_var
        ))

    return w3.eth.account.signHash(message_hash, private_key)


def environment_variable_transaction_signer(tx, address):
    """ Sign a message hash using a private key stored in an environment variable.
    """
    formatted_env_var = PRIVATE_KEY_ENVIRONMENT_VARIABLE.format(address)
    try:
        private_key = os.environ[formatted_env_var]
    except KeyError:
        raise ImproperlyConfigured('The {} environment variable is not set'.format(
            formatted_env_var
        ))

    return w3.eth.account.signTransaction(tx, private_key)
