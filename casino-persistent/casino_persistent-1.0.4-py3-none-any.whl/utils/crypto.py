from enum import Enum
from casino_persistent.exceptions.api_errors import ApiError
from enum import Enum

from casino_persistent.exceptions.api_errors import ApiError


class Crypto(Enum):
    BTC = 'BTC'
    ETH = 'ETH'
    BCH = 'BCH'
    USDT = 'USDT'
    XRP = 'XRP'
    NEO = 'NEO'
    DOGE = 'DOGE'
    DASH = 'DASH'
    LTC = 'LTC'
    XVG = 'XVG'
    XMR = 'XMR'
    STRAT = 'STRAT'

    @classmethod
    def from_name(cls, name) -> Enum:
        for crypto in Crypto:
            if crypto.value == name.upper():
                return crypto
            raise ApiError(f'{name} is not a valid crypto name. Crypto in ({[e.value for e in Crypto]})')
