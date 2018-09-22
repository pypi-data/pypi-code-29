class ApiContext(object):
    def __init__(self, conf):
        self.mode = conf['mode']
        self.url_template = conf['url_template']
        self.version = conf['version']
        self.dict = conf

    @property
    def cache_data(self):
        mode = self.mode()
        return self.dict[mode][self.dict[mode]['cache_driver']]

    def __getattr__(self, attr):
        return self.dict[self.mode()][attr]

    # try:
    #     self.cache_driver = conf[self.mode]['cache_driver']
    # except KeyError:
    #     self.cache_driver = None

    # try:
    #     self.cache_data = conf[self.mode][self.cache_driver]
    # except KeyError:
    #     self.cache_data = None

    # self.timeout = conf[self.mode]['timeout']
    # self.hostname = conf[self.mode]['hostname']
    # self.credentials = conf[self.mode]['credentials']
    # self.base_url = conf[self.mode]['base_url']
    # self.port = conf[self.mode]['port']
