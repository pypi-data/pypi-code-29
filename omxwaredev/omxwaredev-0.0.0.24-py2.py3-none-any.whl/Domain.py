from omxware import omxware
from omxware.Connect import Connection

"""
OMXWare Domain Entity Class
"""

class Domain:
    """Domain Class"""
    __omx_token = ''


    def __init__(self, connecthdr: Connection, domain):
        """Constructor"""

        if not ("DOMAIN_UID_KEY" in domain):
            raise Exception("The DOMAIN_UID_KEY is missing in the given Domain object.")

        self._jobj = domain
        self._domainUidKey = domain['DOMAIN_UID_KEY']
        self._connecthdr = connecthdr

        config = self._connecthdr.getConfig()
        self.__omx_token = config.getOMXToken()

    def get_uid(self):
        return str(self._domainUidKey)

    def __str__(self):
        return "{ 'type': 'domain', 'uid': '" + self.get_uid() + "'}"
