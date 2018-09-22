# coding: utf-8

import logging

import requests

from . import utils
from .device import SherlockDevice


APP_SECRET = "d1b47135142d94fce09e46c6911638442219fae714639b1b04508304e8a48df9"
BASE_URL = "https://20160322-bike2-api-dot-api-sherlock-00.appspot.com"

LOGGER = logging.getLogger(__name__)


class Sherlock(object):
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.user = self._login()

    @property
    def user_id(self):
        return self.user.get('user_id')

    @property
    def name(self):
        return self.user.get('name')

    @property
    def surname(self):
        return self.user.get('surname')

    @property
    def email(self):
        return self.user.get('email')

    @property
    def profile_pic_url(self):
        return self.user.get('url_profile_pic')

    @property
    def devices(self):
        return [SherlockDevice(self, x.get('sherlock')) for x in
                self.get_bikes().get('bikes')]

    @property
    def primary_device(self):
        return self.devices[0]

    def _login(self):
        LOGGER.debug("Logging in as %s", self.username)
        url = f"{BASE_URL}/login"
        data = {"app_secret": APP_SECRET,
                "email": self.username,
                "password": utils.sha256(self.password)}
        res = requests.post(url, json=data)
        if not res.ok:
            LOGGER.error("Login failed: %s", res.text)
            return
        jres = res.json()
        if jres.get("status") != "ok":
            LOGGER.error("Login failed: %s (%s)", jres, res.text)
            return
        LOGGER.info("Login successful! User id: %s", jres.get('user_id'))
        # Discard the status key
        return {k: v for k, v in jres.items() if k != 'status'}

    def _get_signature(self, data, ts):
        return utils.sha256(f'{data}{ts}{APP_SECRET}')

    def get_bikes(self):
        LOGGER.debug("Get bikes")
        url = f"{BASE_URL}/bikes/{self.user_id}"
        ts = utils.timestamp()
        data = {'time_stamp': ts,
                'signature': self._get_signature(self.user_id, ts)}
        return utils.request(url, params=data)

    def get_location(self, imei):
        LOGGER.debug("Get location of device %s", imei)
        url = f"{BASE_URL}/sherlockdevices/position/{imei}"
        ts = utils.timestamp()
        data = {'time_stamp': ts,
                'signature': self._get_signature(imei, ts)}
        return utils.request(url, params=data)


# vim: set ft=python et ts=4 sw=4 :
