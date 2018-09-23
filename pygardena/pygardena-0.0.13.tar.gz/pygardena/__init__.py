import json
import logging
from datetime import datetime, timedelta

import requests
from pygardena.const import DEVICES_URL, LOCATIONS_URL, SESSIONS_URL, REFRESH_TIMEOUT, COMMAND_URL, PROPERTIES_URL, SETTINGS_URL, CMD_POWER_START, CMD_POWER_STOP
from requests import exceptions
from pprint import pformat

_LOGGER = logging.getLogger(__name__)


class PyGardena(object):
    def __init__(self, username=None, password=None):
        self._username = username
        self._password = password

        # sessions params
        self._authenticated = None
        self._auth_token = None
        self._refresh_token = None
        self._user_id = None
        self._refresh_at = None

        self._headers = None
        self._params = None

        # locations params
        self._locations = {}

        # device params
        self._all_devices = {}

        self._debug = False

        self._login()

    def _login(self):
        self._get_sessions()
        self._get_locations()

        self._get_devices()

    def _get_sessions(self):
        """Gardena sessions/login handling."""
        _LOGGER.debug("Creating Gardena session/logging in.")
        credentials = {'sessions': {
            'email': self._username, 'password': self._password}}

        try:
            res = requests.post(SESSIONS_URL, json=credentials)
            sessions = res.json().get('sessions')
            if self._debug:
                _LOGGER.debug(pformat(sessions))
            self._parse_session_data(sessions)
            self._authenticated = True

        except exceptions.RequestException as ex:
            _LOGGER.error("get_session from Gardena failed with %s", ex)

    def _parse_session_data(self, sessions):
        """Parse session data from session json object."""
        self._user_id = sessions.get('user_id')
        self._auth_token = sessions.get('token')
        self._refresh_token = sessions.get('refresh_token')

        self._refresh_at = datetime.now() + REFRESH_TIMEOUT

        _LOGGER.debug('_user_id: %s, _auth_token: %s, _refresh_token: %s, refresh_at: %s',
                      self._user_id, self._auth_token, self._refresh_token, self._refresh_at)

    def _get_locations(self):
        """ Method to get all locations belonging to one user from Gardena."""
        location_params = self.get_location_params()
        locations = {}

        try:
            res = requests.get(
                LOCATIONS_URL, params=location_params, headers=self.get_headers())
            locations = res.json()
            if self._debug:
                _LOGGER.debug(locations)
        except exceptions.RequestException as ex:
            _LOGGER.error("get_locations from Gardena failed with %s", ex)

        for location in locations.get('locations'):
            _LOGGER.debug('{ locationId: %s, locationName: %s }',
                          location.get('id'), location.get('name'))

        self._locations = locations

    def _get_devices(self):
        """ Method to request all devices from Gardena smart home."""
        res = requests.get(
            DEVICES_URL, params=self.get_device_params(), headers=self.get_headers())

        try:
            devices = res.json().get('devices')
            if self._debug:
                _LOGGER.debug('devices: %s', devices)
        except exceptions.RequestException as ex:
            _LOGGER.error("get_devices from Gardena failed with %s", ex)

        self._all_devices = devices

    def get_all_sensors(self):
        """Method to request all devices of category sensor"""
        return self.get_device_by_category('sensor')

    def get_all_switches(self):
        """Method to request all devices of catgory power"""
        return self.get_device_by_category('power')

    def get_device_by_category(self, category):
        """Method to request all devices by category"""
        _devices = []
        for device in self._all_devices:
            if device.get('category') == category:
                _devices.append(device)
        return _devices

    def execute_command(self, command):
        """ Method to execute command on a device of Gardena smart home."""
        self._device_id = None
        command_url = DEVICES_URL + '/' + self._device_id + '/abilities/mower/command'

        try:
            requests.post(command_url, headers=self.get_headers(),
                          params=self.get_device_params(), json=command)
            _LOGGER.debug('Successfully executed: %s for device_id: %s',
                          self.get_command()['name'], self._device_id)
        except exceptions.RequestException as ex:
            _LOGGER.error('Execute command failed with %s', ex)

    def execute_property(self, command):
        """devices/e4047b42-2967-4b8f-be1a-2a97a1fe6bcc/abilities/power/properties/power_timer?locationId=3c3cc3ab-8f71-4850-a426-01d259f4a14b"""
        """devices/device_id/abilities/category/properties/power_timer?locationId=location_id"""

        """/%s/abilities/%s/properties/%s?locationId=%s"""
        # properties_url =  PROPERTIES_URL % ('device_id', 'category', 'property_name', 'location_id')

        try:
            #request.post(properties_url, headers=self.get_headers, params)
            _LOGGER.debug('execute_property')
        except exceptions.RequestException as ex:
            _LOGGER.error('Execute command failed with %s', ex)
    
    def turn_on_switch(self, device_id, device_name, device_category):
        """Method to turn on switch based on device id and category"""
        command_url = PROPERTIES_URL % (device_id, device_category, 'power_timer', self._locations['locations'][0]['id'])

        try:
            requests.put(command_url, data=CMD_POWER_START, headers=self.get_headers())
            _LOGGER.debug("Turn on switch executed for device_name: %s, device_id: %s, device_category: %s", device_name, device_id, device_category)
        except exceptions.RequestException as ex:
            _LOGGER.error('Execute turn on switch failed with %s', ex)

    def turn_off_switch(self, device_id, device_name, device_category):
        """Method to turn off switch based on device id and catetory"""
        command_url = PROPERTIES_URL % (device_id, device_category, 'power_timer', self._locations['locations'][0]['id'])

        try:
            requests.put(command_url, data=CMD_POWER_STOP, headers=self.get_headers())
            _LOGGER.debug("Turn on switch executed for device_name: %s, device_id: %s, device_category: %s", device_name, device_id, device_category)
        except exceptions.RequestException as ex:
            _LOGGER.error('Execute turn on switch failed with %s', ex)

    @property
    def is_autenticated(self):
        """ Returns if the connection is established and authenticated """
        return bool(self._authenticated)

    def get_headers(self):
        return {'content-type': 'application/json', 'x-session': self._auth_token}

    def get_device_params(self):
        location_id = self._locations['locations'][0]['id']
        _LOGGER.debug('location_id: %s', location_id)
        return {'locationId': location_id}

    def get_location_params(self):
        return {'user_id': self._user_id}

    def get_command(self):
        return {'name': 'park_until_next_timer'}

    @property
    def _is_debug(self):
        return bool(self._debug)

    def update(self):
        _LOGGER.debug('Update method called.')
        if self._refresh_at >= datetime.now():
            _LOGGER.debug('Not time to refresh the token, refresh_at: %s, now: %s',
                          self._refresh_at, datetime.now())
            return
        # create new session, location and update devices
        _LOGGER.debug('Time to refresh token and update location and devices, refresh_at: %s, now: %s',
                      self._refresh_at, datetime.now())
        self._login()


"""     @property
    def devices(self):
        if self._all_devices:
            return self._all_devices

        something = {}
        something['mylist'] = []
        
        #self._all_devices["gateway"] = [ GardenaGateway('idididididid', 'namenamename')]
        #self._all_devices['mower'] = []
        #self._all_devices['power'] = []
        #self._all_devices['watering_computer'] = []
        #self._all_devices['sensor'] = []

        self.get_devices()
        devices = self._all_devices

        for device in devices:
            deviceCategory = device.get('category')
            deviceId = device.get('id')
            deviceName = device.get('name')
            if (deviceCategory == 'gateway'):
                _LOGGER.debug('Found { category: %s, id: %s, name: %s }', deviceCategory, deviceId, deviceName)
                #gateway = GardenaGateway(deviceId, deviceName)
                gateways = self._all_devices['gateway']
                gateways.append('someString')
            elif (deviceCategory == 'mower'):
                 _LOGGER.debug('Found { category: %s, id: %s, name: %s }', deviceCategory, deviceId, deviceName)
            elif (deviceCategory == 'power'):
                _LOGGER.debug('Found { category: %s, id: %s, name: %s }', deviceCategory, deviceId, deviceName)
                power = GardenaPower(deviceId, deviceName)
                self._all_devices['power'].append(power)
            elif (deviceCategory == "watering_computer"):
                _LOGGER.debug('Found { category: %s, id: %s, name: %s }', deviceCategory, deviceId, deviceName)
            elif (deviceCategory == 'sensor'):
                _LOGGER.debug('Found { category: %s, id: %s, name: %s }', deviceCategory, deviceId, deviceName)
            else:
                _LOGGER.debug('Found unknow category: %s', deviceCategory)
        
        return self._all_devices
 """
"""    @property
   def gateways(self):
       return self.devices.get('gateways')

   @property
   def mowers(self):
       return self.devices.get('mowers')
    
   @property
   def powers(self):
       return self.devices.get('powers')

   @property
   def watering_computers(self):
       return self.devices.get('watering_computers')

   @property
   def sensors(self):
       return self.devices.get('sensors')
 """

"""     def clean_headers(self):
        headers = {'Content-Type':'application/json'}
        headers['x-session'] = self._auth_token

        self._headers = headers

        params = {'sessions':{'email':self._username,'password':self._password}}
        params['user_id'] = self._user_id
        params['locationId'] = self._location_id

        self._params = params
 """
"""     def query(self,
                url,
                method='GET',
                extra_params=None,
                extra_headers=None,
                retry=3,
                raw=False,
                stream=False):
        
        response = None
        loop = 0

        self.clean_headers()

        while loop <= retry:

            if extra_params:
                params = self._params
                params.update(extra_params)
            else:
                params = self._params
            _LOGGER.debug('Params: %s', params)

            if extra_headers:
                headers = self._headers
                headers.update(extra_headers)
            else:
                headers = self._headers
            _LOGGER.debug('Headers: %s', headers)

            _LOGGER.debug('Request: %s on attempt: %s of %s', url, loop, retry)

            loop += 1

            req = None
            
            if method == 'GET':
                req = self.session.get(url, headers=headers, stream=stream)
            elif method == 'PUT':
                req = self.session.put(url, json=params, headers=headers)
            elif method == 'POST':
                req = self.session.post(url, json=params, headers=headers)

            if req and (req.ok):
                if raw:
                    _LOGGER.debug('Raw object requested')
                    response =  req
                else:
                    response = req.json()
                
                break
        return response
 """
