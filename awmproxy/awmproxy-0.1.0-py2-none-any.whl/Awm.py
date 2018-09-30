import requests
from .Exceptions import *


class AwmProxy(object):
    """

    """

    def __init__(self, api_key, ip=None):
        """

        :param api_key: api key, todo: validate
        :type api_key: str

        :param ip: ip
        :type ip: str

        """
        self.api_key = api_key
        if ip is None:
            self.ip = requests.get('https://api.ipify.org').text
        else:
            self.ip = ip
        self.base_url = 'https://awmproxy.net/proxy/'
        self.params = {}
        self.output_format = 'string'
        self._authorize()

    @property
    def ip_set(self):
        """
        This can only check whether the ip is set to an api key, not necessarily THIS api key, it appears.

        :return:
        """
        r = requests.post('https://awmproxy.net/check_ip_for_proxy.php', data={'ip': self.ip})
        if '<font color=red>' in r.text:
            return False
        elif '<font color=green>' in r.text:
            return True
        else:
            raise AwmConnectionException

    def _authorize(self):
        """
        There is a way to register the ip without calling the whole list, but there's no method to grab user-id via
        the api
        :return: responseobject
        """
        return requests.get(self.base_url + self.api_key + '?set_ip=' + self.ip)

    def get_proxy(self, universal_port=None, fast=False, json=False, country_only=None, country_not=None, info=False,
                  show_ip=False, show_country=False, show_city=False, limit=0):

        """
        By default, all of the proxies will be returned as a list in ip:port format

        :param universal_port: universal ports (proxy rotating). note that this will override all other settings here
        and the only valid ports are 777, 888, 999, 701, 3001
        :type universal_port: int

        :param fast: whether fast proxies
        :type fast: bool

        :param json: to return in json
        :type json: bool

        :param country_only: only return these countries, can take list or str, separate countries with comma like
        US,UA if entering string
        :type country_only: str, list

        :param country_not: same as above but opposite
        :type country_not: str, list

        :param info: show full info. note that this and the show_ip, show_country, and show_city will return results
        as lists of tuples or json if json is selected
        :type info: bool

        :param show_ip: shows the public ip of proxy (not the connecting ip)
        :type show_ip: bool

        :param show_country: shows country
        :type show_country: bool

        :param show_city: show city
        :type show_city bool

        :param limit: only return this many results
        :type limit: int

        :return: list of ip:port, (ip:port, any additional param selected), or list of dict
        """
        ports = [777, 888, 999, 701, 3001]

        if self.ip_set:

            if universal_port in ports:
                res = requests.get(self.base_url + self.api_key, params={'port': universal_port})
                return res.text.strip().splitlines()

            else:

                if fast is True:
                    self.params.update({'fast': 1})

                if isinstance(country_only, list):
                    ostp = ''
                    for i in country_only:
                        ostp = ostp + ',' + i

                    self.params.update({'country-only': ostp})

                if isinstance(country_only, str):
                    self.params.update({'country-only': country_only})

                if isinstance(country_not, list):
                    ostj = ''
                    for i in country_not:
                        ostj = ostj + i + ','

                    self.params.update({'country-not': ostj})

                if isinstance(country_not, str):
                    self.params.update({'country-not': country_not})

                if limit > 0:
                    self.params.update({'limit': limit})

                if info is True:
                    self.params.update({'info': 1})
                    self.output_format = 'tuple'

                if show_ip is True:
                    self.params.update({'ip': 1})
                    self.output_format = 'tuple'

                if show_country is True:
                    self.params.update({'country': 1})
                    self.output_format = 'tuple'

                if show_city is True:
                    self.params.update({'city': 1})
                    self.output_format = 'tuple'

                if json is True:
                    self.params.update({'json': 1})
                    self.output_format = 'json'

                with requests.get(self.base_url + self.api_key, params=self.params) as rx:

                    if self.output_format == 'string':
                        return rx.text.strip().splitlines()

                    elif self.output_format == 'tuple':
                        return [tuple(line.split(';')) for line in rx.text.strip().splitlines()]

                    elif self.output_format == 'json':
                        return rx.json()
        else:
            raise AwmKeyException
