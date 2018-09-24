from base64 import b64encode
import requests


class ArableClient(object):
    """ A client for connecting to Arable and making data queries.

        >>> from arable.client import ArableClient
        >>> client = ArableClient()
        >>> client.connect(email='user@loremipsum.com', password='#@#SS', tenant='loremipsum')

    """
    _base_url = "https://api-user.arable.cloud/api/v1"
    _param_options = {"devices", "end", "format", "limit", "location", "measure", "order", "select", "start"}

    def __init__(self):
        self.header = None

    def _login(self, email=None, password=None, tenant=None):
        url = "{0}/auth/user/{1}".format(ArableClient._base_url, tenant)
        # utf-8 encode/decode for python3 support
        token = b64encode("{0}:{1}".format(email, password).encode('utf-8')).decode('utf-8')
        headers = {"Authorization": "Basic " + token}

        r = requests.post(url, headers=headers)
        if r.status_code == 200:
            return {"Authorization": "Bearer " + r.json()['access_token']}
        else:
            r.raise_for_status()

    def _check_connection(self):
        """ Returns True if client has auth token, raises an exception if not. """
        if not self.header:
            raise Exception("Authentication exception: not connected.")
        return True

    def connect(self, email=None, password=None, tenant=None, apikey=None):
        """ Logs the client in to the API.

            :param email: user email address
            :param password: user password
            :param tenant: user's tenant name

            >>> client.connect(email='test@loremipsum.com', password='$#$!%', tenant='loremipsum')

        """
        # todo: reinstate apikeys in docs
        # :param apikey: user 's apikey (a UUID string)
        #
        # >> > apikey = "<key>"
        # >> > client.connect(apikey=apikey)

        if apikey:
            self.header = {"Authorization": apikey}
            return
        elif not all([email, password, tenant]):
            raise Exception("Missing parameter; connect requires email, password, and tenant")
        try:
            self.header = self._login(email=email, password=password, tenant=tenant)
        except Exception as e:
            raise Exception("Failed to connect:\n{}".format(str(e)))

    def devices(self, device_id=None, name=None, order=None, limit=None, page=None):
        """ Lists the devices associated with the user's group.

            >>> client.devices()

            :param device_id: optional; look up a single device by id; takes precedence over name, if present

            >>> client.devices(device_id='<object id>')

            :param name: optional; look up a single device by name (serial); ignored if device_id is present

            >>> client.devices(name='A000##')

            :param order: optional; field to order by when looking up multiple devices,
                e.g. "name" for name ascending or "-name" for name descending (default "-last_post")
            :param limit: optional; max number of devices to retrieve when looking up multiple (default 24)
            :param page: optional; results page to retrieve when looking up multiple devices (default 1)
        """

        self._check_connection()

        url = ArableClient._base_url + "/devices"
        if device_id:
            url += "/" + device_id
        elif name:
            url += "?name=" + name

        params = {}
        if order is not None:
            params['sortBy'] = order
        if limit is not None:
            params['limit'] = limit
        if page is not None:
            params['page'] = page

        r = requests.get(url, headers=self.header, params=params)
        if 200 == r.status_code:
            return r.json()
        else:
            r.raise_for_status()

    def query(self, **kwargs):
        """ Query Arable pod data. One of devices or location must be provided, or no data will be retrieved.

            >>> client.query()
            >>> devices=["DeviceName"]
            >>> client.query(select='microclimate', devices=devices, measure="calibrated", limit=10000)
            >>> csv = client.query(format='csv', devices=devices, measure='hourly')

            >>> dt = datetime.datetime.now() - datetime.timedelta(hours=12)
            >>> start = dt.strftime("%Y-%m-%dT%H:%M:%SZ")
            >>> json = client.query(devices=devices, measure='L1_hourly', start=start)


            :param devices: list of device names to retrieve data for
            :param location: optional; id of a location to retrieve data for; devices ignored if this is present
            :param start: optional; beginning of query time range
            :param end: optional; end of query time range
            :param order: optional; "time" (time ascending) or "-time" (time descending)
            :param limit: optional; maximum number of data points to return; defaults to 1000
            :param format: optional; use format=csv to get csv-formatted data; otherwise data is returned as json
            :param select: optional; "all", "spectrometer", "microclimate", or "radiometer"
            :param measure: optional; "calibrated", "hourly", or "daily"
        """

        self._check_connection()

        url = ArableClient._base_url + "/data"
        params = {}
        for param in ArableClient._param_options:
            if kwargs.get(param):
                params[param] = str(kwargs[param])
        if not params.get('order'):
            params['order'] = '-time'
        if not params.get('limit'):
            params['limit'] = '1000'

        r = requests.get(url, headers=self.header, params=params)

        if r.status_code == 200:
            if params.get('format') == 'csv':
                return r.text
            else:
                return r.json()
        else:
            r.raise_for_status()
