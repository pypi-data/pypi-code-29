# 3rd party imports
import stellar_base.utils
from stellar_base.exceptions import *
# Local imports
from .constants import *


def is_float_str(string):
    try:
        float(string)
        return True
    except ValueError:
        return False


def is_valid_stellar_public_key(key):
    if key is None:
        return False
    try:
        stellar_base.utils.decode_check('account', key)
        return True
    except DecodeError:
        return False


def is_valid_stellar_private_key(key):
    if key is None:
        return False
    try:
        stellar_base.utils.decode_check('seed', key)
        return True
    except DecodeError:
        return False


def is_valid_stellar_transaction_text_memo(memo):
    return False if len(memo) > STELLAR_MEMO_TEXT_MAX_BYTES else True
