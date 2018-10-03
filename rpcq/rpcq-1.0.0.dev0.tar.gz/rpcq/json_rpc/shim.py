import warnings

from rpcq.json_rpc.client import Client


class Shim(Client):
    """
    For backwards compatibility: Client used to be named "Shim" and timeouts were in milliseconds instead of seconds
    """
    def __init__(self, endpoint: str, timeout: float = None):
        warnings.warn('Shim is deprecated, use rpcq.Client instead and convert the timeout parameter (if specified)'
                      ' into seconds instead of milliseconds', DeprecationWarning, stacklevel=2)
        super().__init__(endpoint, timeout)

    def __setattr__(self, key, value):
        if key == 'timeout':
            value = value / 1000 if value is not None else None

        super().__setattr__(key, value)
