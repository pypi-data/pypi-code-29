# -*- coding: utf-8 -*-

import time
import requests
from decimal import Decimal
from xml.etree import ElementTree

from .utils import password_to_hash
from .exceptions import (
    TenetBaseException,
    TenetBadRequest,
    TenetServerError
)


class TenetAPI(object):
    ACC_STATE_URL = "https://stats.tenet.ua/utl/!gadgapi.ls_state_evpkt"
    BONUS_CHECK_URL = "https://stats.tenet.ua/utl/!gadgapi.ev_bonus_check"
    BONUS_SWITCH_URL = "https://stats.tenet.ua/utl/!gadgapi.ev_bonus_switch"

    ACC_STATE_NORMAL = "Normal"
    ACC_STATE_LOCKED = "Locked"
    ACC_STATE_WARNING = "Warning"

    BONUS_ENABLED = "Enabled"
    BONUS_DISABLED = "Disabled"
    BONUS_ENDED = "Ended"

    USER_AGENT = "TenetAPI/1.0"

    def __init__(self, **kwargs):
        all_opts = [('username', 'passcode'), ('username', 'md5passcode')]
        is_ok = any([set(opts).issubset(kwargs.keys()) for opts in all_opts])
        assert is_ok, TenetBaseException(
            "Usage: TenetAPI(username='user', passcode='pass')"
            " or TenetAPI(username='user', md5passcode='hash')"
        )

        # account id number
        self._account_id = None
        # debtor, creditor or someone else?
        self._account_state = None
        # is account on or off?
        self._account_enabled = None
        # saldo
        self._saldo = None
        # tariff
        self._service_name = None
        # is "Good day" enabled?
        self._good_day = None
        # on, off, end
        self._bonus_state = None
        # traffic left in megabytes
        self._bonus_rest = None

        self._username = kwargs.get('username')
        self._passcode = kwargs.get('md5passcode')
        if not self._passcode:
            self._passcode = password_to_hash(kwargs.get('passcode'))

        self._session = requests.Session()
        self._session.headers.update({
            'User-Agent': self.USER_AGENT
        })

    @property
    def account_id(self):
        return self._account_id

    @account_id.setter
    def account_id(self, value):
        self._account_id = value

    @property
    def account_state(self):
        return self._account_state

    @account_state.setter
    def account_state(self, value):
        value = value.lower()
        if value == 'n':
            self._account_state = self.ACC_STATE_NORMAL
        elif value == 'l':
            self._account_state = self.ACC_STATE_LOCKED
        else:
            self._account_state = self.ACC_STATE_WARNING

    @property
    def account_enabled(self):
        return self._account_enabled

    @account_enabled.setter
    def account_enabled(self, value):
        self._account_enabled = False
        if value.upper() == "ON":
            self._account_enabled = True

    @property
    def saldo(self):
        return self._saldo

    @saldo.setter
    def saldo(self, value):
        self._saldo = "%.2f" % Decimal(value.replace(',', '.'))

    @property
    def service_name(self):
        return self._service_name

    @service_name.setter
    def service_name(self, value):
        self._service_name = value

    @property
    def good_day(self):
        return self._good_day

    @good_day.setter
    def good_day(self, value):
        self._good_day = False
        if value.upper() == 'YES':
            self._good_day = True

    @property
    def bonus_state(self):
        return self._bonus_state

    @bonus_state.setter
    def bonus_state(self, value):
        if value.upper() == 'ON':
            self._bonus_state = self.BONUS_ENABLED
        elif value.upper() == 'OFF':
            self._bonus_state = self.BONUS_DISABLED
        elif value.upper() == 'END':
            self._bonus_state = self.BONUS_ENDED

    @property
    def bonus_rest(self):
        return self._bonus_rest

    @bonus_rest.setter
    def bonus_rest(self, value):
        # Convert MBytes to Bytes
        value = float(str(value).replace(',', '.')) * 1024 * 1024
        self._bonus_rest = value

    def _request(self, url):
        try:
            payload = {
                'login': self._username,
                'md5pass': self._passcode,
                't': int(time.time())
            }
            r = self._session.post(url, data=payload, timeout=5)
            r.raise_for_status()
            return r.content
        except IOError as e:
            raise TenetBadRequest(str(e))

    def _check_account(self):
        # Get account info
        xml_body = self._request(self.ACC_STATE_URL)
        etree = ElementTree.fromstring(xml_body)

        result = etree.findtext("./result")
        if result != "OK":
            error_msg = etree.findtext("./error_desc") or "Unknown Error"
            raise TenetServerError(error_msg.strip())

        self.account_id = etree.findtext("./LS")
        self.account_state = etree.findtext("./lsstate")
        self.account_enabled = etree.findtext("./usrstate")
        self.saldo = etree.findtext("./saldo")
        self.service_name = etree.findtext("./evpkt")
        self.good_day = etree.findtext("./good_day")

    def _check_bonus(self):
        # Check bonus state
        xml_body = self._request(self.BONUS_CHECK_URL)
        etree = ElementTree.fromstring(xml_body)

        result = etree.findtext("./result")
        if result != "OK":
            error_msg = etree.findtext("./error_desc") or "Unknown Error"
            raise TenetServerError(error_msg.strip())

        self.bonus_state = etree.findtext("./bonus")
        self.bonus_rest = etree.findtext("./rest")

    def update(self):
        self._check_account()
        self._check_bonus()

    def toggle_bonus(self):
        xml_body = self._request(self.BONUS_SWITCH_URL)
        etree = ElementTree.fromstring(xml_body)

        # The API will return "Unknown error" when bonus traffic is over
        # and we are trying to disable bonus.
        # Let's ignore all errors for now.
        if etree.findtext("./result") == "OK":
            self._check_bonus()
