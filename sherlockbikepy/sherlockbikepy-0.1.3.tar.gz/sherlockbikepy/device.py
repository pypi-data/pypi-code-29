# coding: utf-8

from collections import namedtuple

from . import utils


Position = namedtuple('Position', ['latitude', 'longitude', 'last_update'])
SelfTest = namedtuple('SelfTest', ['gps_generic_pass', 'eeprom_generic_pass',
                                   'imu_generic_pass', 'gprs_generic_pass',
                                   'last_update'])


class SherlockDevice(object):
    def __init__(self, controller, json):
        self._controller = controller
        self._json = json

    @property
    def imei(self):
        return self._json.get("imei")

    @property
    def pin(self):
        return self._json.get("pin")

    @property
    def iccid(self):
        return self._json.get("iccid")

    @property
    def sherlock_id(self):
        return self._json.get("sherlock_id")

    @property
    def firmware_version(self):
        return self._json.get("firmware_version")

    @property
    def subscription_type(self):
        return self._json.get("subscription_type")

    @property
    def created_on(self):
        return utils.str2dt(self._json.get("created_on"))

    @property
    def terms_and_condition_status(self):
        return self._json.get("terms_and_condition_status")

    @property
    def battery_level(self):
        return self._json.get("extended_info").get("battery_level")

    @property
    def battery_voltage(self):
        return self._json.get("extended_info").get("battery_voltage")

    @property
    def location(self):
        spos = self._json.get('sherlock_position')
        if not spos:
            return
        pos = spos.get('position')
        return Position(
            pos.get('lat'),
            pos.get('lon'),
            utils.str2dt(spos.get('timestamp_str')))

    @property
    def state(self):
        state_full = self._json.get('sherlock_state').get('state')
        # Remove the leading "SHERLOCK_STATE_" string
        return state_full.replace('SHERLOCK_STATE_', '')

    @property
    def is_on(self):
        return self.state != 'OFF'

    @property
    def last_self_test(self):
        self_test = self._json.get('last_selftest')
        return SelfTest(
            self_test.get('gps_generic_pass'),
            self_test.get('eeprom_generic_pass'),
            self_test.get('imu_generic_pass'),
            self_test.get('gprs_generic_pass'),
            utils.str2dt(self_test.get('timestamp_utc_str')))

    @property
    def picture_url(self):
        for bike in self._controller.get_bikes().get('bikes', {}):
            sherlock_id = bike.get('sherlock', {}).get('sherlock_id', {})
            if sherlock_id == self.sherlock_id:
                return bike.get('master_pic_url')

    def update(self):
        devices = self._controller.devices
        for dev in devices:
            if (dev.sherlock_id == self.sherlock_id and
                    dev.imei == self.imei):
                self._json = dev._json
                break

    def __str__(self):
        return f'<SherlockDevice> (IMEI: {self.imei})'

# vim: set ft=python et ts=4 sw=4 :
