import json
import time
from enum import Enum

import requests
from cachecontrol import CacheControl

from ..exceptions import ServerStatus, ServerUpdating
from .cache_heuristics import OneHourHeuristic

REQUEST_SESSION = CacheControl(requests.session(), heuristic=OneHourHeuristic())


class HTTPStatus(Enum):
    OK = 200


class CallookStatus(Enum):
    Updating = "UPDATING"
    Invalid = "INVALID"
    Valid = "VALID"


def license_is_expired(expiry_date: str) -> bool:
    # Turn dates into YYYYMMDD - comparable integers
    expdata = expiry_date.split("/")
    expdate = int(expdata[2] + expdata[0] + expdata[1])
    currdate = int(time.strftime("%Y%m%d", time.gmtime(time.time())))
    return currdate > expdate


def fetch_license(callsign: str) -> dict:
    # Fetch license data.
    page = REQUEST_SESSION.get("http://callook.info/{}/json".format(callsign))

    # Hardcode since they always return 200
    if page.status_code != HTTPStatus.OK.value:
        raise ServerStatus("HTTP {}".format(page.status_code))

    data = json.loads(page.text)
    status = (data["status"]).upper()

    if status not in [status.value for status in CallookStatus]:
        # Something wierd is up server-side. Discontinue.
        raise ServerStatus("Unknown Status: {}".format(data["status"]))

    if status is CallookStatus.Updating.value:
        raise ServerUpdating

    return data
