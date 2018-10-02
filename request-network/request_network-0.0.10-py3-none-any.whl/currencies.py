import os

from request_network.artifact_manager import (
    ArtifactManager,
)
from request_network.exceptions import (
    UnsupportedCurrency,
)


class Currency(object):
    name = None
    symbol = None
    decimals = None
    request_service_class = None

    def __init__(self, name, symbol, decimals, request_service_class):
        self.name = name
        self.symbol = symbol
        self.decimals = decimals
        self.request_service_class = request_service_class

    @property
    def currency_contract_name(self):
        return 'last-request{}'.format(self.name)

    def get_service_class(self):
        """ :returns An instance of the service for this currency
            :rtype request_network.services.RequestCoreService
        """
        # https://stackoverflow.com/a/547867/394423
        components = 'request_network.services'.split('.')
        mod = __import__(components[0])
        for comp in components[1:]:
            mod = getattr(mod, comp)
        service_class = getattr(mod, self.request_service_class)
        return service_class(**self.get_service_instance_kwargs())

    def get_service_instance_kwargs(self):
        return {}

    def get_currency_contract_data(self):
        """ Get this currency's contract data from the Artifact Manager.

        :return:
        """
        am = ArtifactManager()
        return am.get_contract_data(self.currency_contract_name)


class ERC20Currency(Currency):
    token_address = None

    def __init__(self, name, symbol, decimals, request_service_class, token_address):
        super().__init__(name, symbol, decimals, request_service_class)
        self.token_address = token_address

    def get_service_instance_kwargs(self):
        data = super(ERC20Currency, self).get_service_instance_kwargs()
        data['token_address'] = self.token_address
        return data

    @property
    def currency_contract_name(self):
        return 'last-requesterc20-{}'.format(self.token_address)


currencies = {
    'main': {
        'ETH': Currency('Ethereum', 'ETH', 18, 'RequestEthereumService'),
        'REQ': ERC20Currency(
            name='Request Network',
            symbol='REQ',
            decimals=18,
            request_service_class='RequestERC20Service',
            token_address='0x8f8221afbb33998d8584a2b05749ba73c37a938a'
        ),
        'KNC': ERC20Currency(
            name='Kyber Network',
            symbol='KNC',
            decimals=18,
            request_service_class='RequestERC20Service',
            token_address='0xdd974d5c2e2928dea5f71b9825b8b646686bd200'
        ),
        'DGX': ERC20Currency(
            name='Digix',
            symbol='DGX',
            decimals=9,
            request_service_class='RequestERC20Service',
            token_address='0x4f3afec4e5a3f2a6a1a411def7d7dfe50ee057bf'
        ),
        'DAI': ERC20Currency(
            name='Dai',
            symbol='DAI',
            decimals=18,
            request_service_class='RequestERC20Service',
            token_address='0x89d24a6b4ccb1b6faa2625fe562bdd9a23260359'
        ),
        'OMG': ERC20Currency(
            name='OmiseGO',
            symbol='OMG',
            decimals=18,
            request_service_class='RequestERC20Service',
            token_address='0xd26114cd6ee289accf82350c8d8487fedb8a0c07'
        ),
        'KIN': ERC20Currency(
            name='Kin',
            symbol='KIN',
            decimals=18,
            request_service_class='RequestERC20Service',
            token_address='0x818fc6c2ec5986bc6e2cbf00939d90556ab12ce5'
        ),
        'ZRX': ERC20Currency(
            name='0x Protocol',
            symbol='ZRX',
            decimals=18,
            request_service_class='RequestERC20Service',
            token_address='0xe41d2489571d322189246dafa5ebde1f4699f498'
        ),
        'BAT': ERC20Currency(
            name='Basic Attention Token',
            symbol='BAT',
            decimals=18,
            request_service_class='RequestERC20Service',
            token_address='0x0d8775f648430679a709e98d2b0cb6250d2887ef'
        ),
        'BNB': ERC20Currency(
            name='Binance',
            symbol='BNB',
            decimals=18,
            request_service_class='RequestERC20Service',
            token_address='0xb8c77482e45f1f44de1745f52c74426c631bdd52'
        ),
        'LINK': ERC20Currency(
            name='ChainLink',
            symbol='LINK',
            decimals=18,
            request_service_class='RequestERC20Service',
            token_address='0x514910771af9ca656af840dff83e8264ecf986ca'
        )
    },
    'rinkeby': {
        'ETH': Currency('Ethereum', 'ETH', 18, 'RequestEthereumService'),
        # On Rinkeby, REQ is the test Central Bank Token
        'REQ': ERC20Currency(
            name='Request Network',
            symbol='REQ',
            decimals=18,
            request_service_class='RequestERC20Service',
            token_address='0x995d6a8c21f24be1dd04e105dd0d83758343e258'
        )
    },
    'private': {
        'ETH': Currency('Ethereum', 'ETH', 18, 'RequestEthereumService'),
        # On private, REQ is a local test token
        'REQ': ERC20Currency(
            name='Request Network',
            symbol='REQ',
            decimals=18,
            request_service_class='RequestERC20Service',
            token_address='0x345ca3e014aaf5dca488057592ee47305d9b3e10'
        )
    }
}


def get_currency(symbol):
    network_name = os.environ['ETHEREUM_NETWORK_NAME']
    try:
        return currencies[network_name][symbol]
    except KeyError:
        raise UnsupportedCurrency(
            'Could not find currency "{}" on network "{}"'.format(
                symbol,
                network_name
            )
        )

# TODO refactor as Enum loaded from JSON file?
# TODO how to best manage live and test currency sets? Can we load them from the artifact manager?
# currencies_by_symbol = {
#     'ETH': Currency('Ethereum', 'ETH', 18, 'RequestEthereumService'),
#     'DAI': ERC20Currency(
#         'Dai',
#         'DAI',
#         18,
#         'RequestERC20Service',
#         '0x345ca3e014aaf5dca488057592ee47305d9b3e10'
#     ),
#     # TODO this is the test Central Bank Token
#     'REQ': ERC20Currency(
#         'Request Network',
#         'REQ',
#         18,
#         'RequestERC20Service',
#         '0x995d6a8c21f24be1dd04e105dd0d83758343e258'
#     )
# }
#
# currencies_by_name = {c.name: c for c in currencies_by_symbol.values()}
