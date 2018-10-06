from pathlib import Path

CLI_BANNER_TEXT = 'PYGEEK-STELLAR'

# Config file related constants
DEFAULT_CONFIG_FILE = '{}/.pygeek-stellar.config'.format(str(Path.home()))
JSON_ACCOUNTS_TAG = 'accounts'
JSON_ACCOUNT_NAME_TAG = 'account_name'
JSON_PUBLIC_KEY_TAG = 'public_key'
JSON_PRIVATE_KEY_TAG = 'private_key'

# Stellar related constants
STELLAR_HORIZON_TESTNET_URL = 'https://horizon-testnet.stellar.org'
STELLAR_ASSET_TYPE_XLM = 'native'
STELLAR_ASSET_TYPE_MAGNET = 'magnet'
STELLAR_MEMO_TEXT_MAX_BYTES = 28
