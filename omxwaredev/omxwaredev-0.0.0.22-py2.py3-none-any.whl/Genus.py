from omxware import omxware
from omxware.Connect import Connection

"""
OMXWare Genus Entity Class
"""


class Genus:
    """Genus Class"""
    omx: omxware

    def __init__(self, connecthdr: Connection, genus):
        """Constructor"""

        if not ("GENUS_NAME" in genus):
            raise Exception("The Genus name is missing in the given Genus object.")

        self._jobj = genus
        self._genusName = genus['GENUS_NAME']
        self._connecthdr = connecthdr

        config = self._connecthdr.getConfig()
        omxtoken = config.getOMXToken()

        self.omx = omxware(omxtoken)

    def __str__(self):
        return "{ 'type': 'genus', 'name': '" + self.get_name() + "'}"

    def get_name(self):
        return str(self._jobj['GENUS_NAME'])
