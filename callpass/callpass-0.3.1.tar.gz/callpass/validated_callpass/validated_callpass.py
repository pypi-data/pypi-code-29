import re

from ..callpass import Callpass
from ..exceptions import ExpiredLicense, InvalidLicense, MalformedCallsign
from .license_validation_tools import CallookStatus, fetch_license, license_is_expired


class ValidatedCallpass(Callpass):

    callsign: str
    callsign_pattern = r"^([Aa]|[Kk]|[Nn]|[Ww])[A-Za-z]*\d+[A-Za-z]+(-[A-Z0-9]{1,2})?$"

    def __post_init__(self):
        assert self.valid_format()
        assert self.valid_license()
        self.callpass = self._generate_callpass(self.bare_callsign)

    def valid_format(self) -> bool:
        if not re.match(self.callsign_pattern, self.bare_callsign):
            raise MalformedCallsign
        return True

    def valid_license(self) -> bool:
        data = fetch_license(self.bare_callsign)
        status = str(data["status"]).upper()

        # Check reported validity
        if status == CallookStatus.Invalid.value:
            raise InvalidLicense

        # Check expiry
        if license_is_expired(data["otherInfo"]["expiryDate"]):
            raise ExpiredLicense

        return True
