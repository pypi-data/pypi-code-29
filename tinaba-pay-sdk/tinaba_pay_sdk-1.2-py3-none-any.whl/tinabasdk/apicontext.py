
example = {'mode': 'sandbox',
           'version': 'v1',
           'url_template': '{hostname}{base_url}{route}',
           'sandbox': {'timeout': 10,
                       'merchant_id': 'merch',
                       'secret': 'secret',
                       'hostname': 'https://valid.tinaba.tv',
                       'base_url': '/WebApi/tinaba/checkout',
                       'port': 443},
           'live': {'timeout': 10,
                    'merchant_id': 'merch',
                    'secret': 'secret',
                    'hostname': 'https://tfull.bancaprofilo.it',
                    'base_url': '/WebApi/tinaba/checkout',
                    'port': 443}}


class ApiContext(object):
    def __init__(self, conf):
        self.mode = conf['mode']
        self.version = conf['version']
        self.url_template = conf['url_template']
        self.timeout = conf[self.mode]['timeout']
        self.secret = conf[self.mode]['secret']
        self.base_url = conf[self.mode]['base_url']
        self.port = conf[self.mode]['port']
        self.hostname = conf[self.mode]['hostname']
        self.merchant_id = conf[self.mode]['merchant_id']
