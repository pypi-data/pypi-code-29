# system modules
import logging
import json
import io
import math
import time
import re
import inspect
import functools
from posixpath import join as urljoin

# internal modules
from sensemapi import paths
from sensemapi.reprobject import ReprObject
from sensemapi.senseBox import senseBox
from sensemapi.senseBoxSensorData import senseBoxSensorData
from sensemapi.errors import *
from sensemapi.utils import *
from sensemapi import compat

# external modules
import requests

logger = logging.getLogger(__name__)

class SenseMapClient(ReprObject):
    """
    Client to interface the `OpenSenseMap API <https://api.opensensemap.org>`_

    Args:
        api (str, optional): the api server to use. You may use
            :any:`OPENSENSEMAP_API_LIVE` (default) or
            :any:`OPENSENSEMAP_API_TEST` for testing purposes.
    """
    def __init__(self, api = paths.OPENSENSEMAP_API_LIVE):
        frame = inspect.currentframe()
        args = inspect.getargvalues(frame)[0]
        for arg in args[1:]:
            val = locals().get(arg)
            if val is not None:
                setattr(self, arg, val)

    RETRY_AFTER_HEADER_REGEX = re.compile("retry.*after$", re.IGNORECASE)
    """
    Regex used to determine the header field containing the time to wait until
    issuing the next request
    """

    @simplegetter
    def api(self):
        return None

    @simplesetter(api)
    def api(self, new):
        return new

    def retry_after_time_if_too_many_requests(decorated_function):
        """
        Decorator to call a decorated method, catching an
        :any:`OpenSenseMapAPITooManyRequestsError`, trying to determine how
        long to wait from the error message, waiting that time and then
        retries.
        """
        @functools.wraps(decorated_function)
        def wrapper(self, *args, **kwargs):
            try:
                return decorated_function(self, *args, **kwargs)
            except OpenSenseMapAPITooManyRequestsError as e:
                logger.debug(e)
                m = re.search(pattern=
                    "(?:(?P<seconds>\d+\.\d+)\s*s)|"
                    "(?:(?P<milliseconds>\d+\.\d+)\s*ms)"
                    ,string=str(e))
                try:
                    d = m.groupdict()
                    retry_after_seconds = 0
                    seconds = d.get("seconds")
                    milliseconds = d.get("milliseconds")
                    if seconds:
                        retry_after_seconds += float(seconds)
                    if milliseconds:
                        retry_after_seconds += float(milliseconds) / 1000
                except (AttributeError, ValueError, KeyError, IndexError):
                    raise OpenSenseMapAPITooManyRequestsError(
                        "Could not determine "
                        "time to wait until next retry.")
                logger.debug("Waiting {} seconds until retry..."
                    .format(retry_after_seconds))
                time.sleep(retry_after_seconds)
            logger.debug("Now trying again to call {}"
                .format(decorated_function))
            return decorated_function(self, *args, **kwargs)
        return wrapper

    @retry_after_time_if_too_many_requests
    def request(self, method, *args, **kwargs):
        """
        Wrapper around corresponding methods of :mod:`requests`, raising
        specific exceptions depending of the response.

        Args:
            method (str): the method to use. Needs to be a method of
                :any:`requests`.
            args, kwargs : arguments passed to the method

        Returns:
            requests.models.Response : the request response

        Raises:
            OpenSenseMapAPITooManyRequestsError : if the client issued too many
                requests
        """
        # perform the request
        method = getattr(requests, method)
        response = method(*args, **kwargs)
        logger.debug("API responded [status code {}]:\n{}".format(
            response.status_code, response.text))
        # too many requests
        if response.status_code == 429:
            headers = response.headers.copy()
            retry_after_header = next(
                filter(self.RETRY_AFTER_HEADER_REGEX.search, headers.keys()),
                None)
            retry_after = headers.get(retry_after_header)
            raise OpenSenseMapAPITooManyRequestsError(
                "retry after {}".format(retry_after) if retry_after else "")
        try:
            logger.debug("API responded JSON [status code {}]:\n{}".format(
                response.status_code, response.json()))
        except compat.JSONDecodeError:
            pass
        return response

    def _get_box(self, id, format = None):
        """
        Issue the request to retreive a single senseBox

        Args:
            id (str) : the senseBox id to retreive
            format (str, optional): one of ``"json"`` and ``"geojson"``

        Returns:
            dict : the API response
        """
        response = self.request("get",
            urljoin(self.api,paths.BOXES,id),
            params = {"format":format} if format else {}
            )
        response_json = response.json()
        if response.status_code == 200:
            return response_json
        else:
            message = response_json.get("message")
            raise OpenSenseMapAPIError("Could not retreive with id '{}'{}"
                .format(id, ": {}".format(message) if message else ""))

    def get_box(self, id):
        """
        Retreive one :any:`senseBox`

        Args:
            id (str) : the senseBox id to retreive

        Returns:
            senseBox : the retreived senseBox
        """
        box = senseBox.from_json(self._get_box(id = id, format = "json"))
        box.client = self
        return box

    def _post_measurement(self, box_id, sensor_id, value, time = None,
        lat = None, lon = None, height = None):
        """
        Issue a request to upload a new measurement

        Args:
            box_id (str) : the senseBox id
            sensor_id (str) : the sensor's id
            value (float) : the current measurement value
            time (datetime.datetime, optional) : the time of the measurement
            lat, lon, height (float,optional) : the current position

        Returns:
            True : on success
        """
        assert box_id is not None, "box_id must  be defined"
        assert sensor_id is not None, "sensor_id must  be defined"
        d = {}
        d["value"] = float(value)
        if time:
            d["createdAt"] = date2str(time)
        try:
            d["location"] = location_dict(lat, lon, height)
        except ValueError:
            pass
        logger.debug("Sending Request with JSON:\n{}"
            .format(pretty_json(d)))
        response = self.request("post",
            urljoin(self.api,paths.BOXES,box_id,sensor_id),
            json = d,
            )
        try:
            response_json = response.json()
        except compat.JSONDecodeError:
            raise OpenSenseMapAPIError("Posting measurement didn't work: {}"
                .format(response.text))
        if hasattr(response_json, "get"): # is a dict
            message = response_json.get("message")
            raise OpenSenseMapAPIError("Posting measurement didn't work{}"
                .format(": "+ message or ""))
        else: # no dict
            if re.search("measurement\s+saved\s+in\s+box",response_json):
                return True

    def post_measurement(self, sensor):
        """
        Upload the current measurement of a given :any:`senseBoxSensor`.

        Args:
            sensor (senseBoxSensor) : the sensor
        """
        assert sensor.id, "the given sensor does not have an id"
        assert sensor.box, "the given sensor does not know its senseBox"
        assert sensor.box.id, "the given sensor's senseBox does not have an id"
        assert sensor.last_value, "the given sensor does not have a last_value"
        post_kwargs = {}
        post_kwargs.update(
            box_id = sensor.box.id,
            sensor_id = sensor.id,
            value = float(sensor.last_value),
            )
        if sensor.box.exposure == "mobile":
            post_kwargs.update(
                lat = box.current_lat,
                lon = box.current_lon,
                height = box.current_height,
                )
        if sensor.last_time:
            post_kwargs.update(time = sensor.last_time)
        return self._post_measurement(**post_kwargs)

    def get_measurements(self, box_id, sensor_id,
        from_date = None, to_date = None,
        format = None, download = None, outliers = None,
        outlier_window = None, delimiter = None,
        ):
        """
        Retrieve the 10000 latest measurements for a sensor

        Args:
            box_id (str): the senseBox id
            sensor_id (str): the sensor id
            from_date (datetime.datetime, optional): beginning date of
                measurement data (default: 48 hours ago from now)
            to_date (datetime.datetime, optional): end date of measurement data
                (default: now)
            format (str, optional): either ``"json"`` (default) or ``"csv"``
            outliers (bool, optional): add outlier marker `isOutlier` to data?
            outlier_window (int, optional):
                outlier window size (1-50, default: 15)
            delimiter (str, optional): either ``"comma"`` (default) or
                ``"semicolon"``

        Returns:
            senseBoxSensorData : the retrieved data
        """
        assert box_id is not None, "box_id must  be defined"
        assert sensor_id is not None, "sensor_id must  be defined"
        d = {}
        if from_date is not None:
            d["from-date"] = date2str(from_date)
        if to_date is not None:
            d["to-date"] = date2str(to_date)
        if format is not None:
            d["format"] = str(format)
        if outliers is not None:
            d["outliers"] = bool(outliers)
        if outlier_window is not None:
            d["outlier-window"] = int(outlier_window)
        logger.debug("Sending GET request with parameters:\n{}"
            .format(pretty_json(d)))
        response = self.request("get",
            urljoin(self.api,paths.BOXES,box_id,"data",sensor_id),
            params = d,
            )
        try:
            response_json = response.json()
            raise NotImplementedError("Parsing JSON-formatted measurements "
                "is not yet implemented. Use format='csv'")
        except compat.JSONDecodeError:
            return senseBoxSensorData.from_csv(io.StringIO(response.text))
