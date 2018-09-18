from kazecore.IO.Mixins import SerializableMixin
import sys
from kaze.Core.Size import GetVarSize


class AddrPayload(SerializableMixin):
    NetworkAddressesWithTime = []

    def __init__(self, addresses=None):
        """
        Create an instance.

        Args:
            addresses (list): of kaze.Network.Payloads.NetworkAddressWithTime.NetworkAddressWithTime instances.
        """
        self.NetworkAddressesWithTime = addresses if addresses else []

    def Size(self):
        """
        Get the total size in bytes of the object.

        Returns:
            int: size.
        """
        return GetVarSize(self.NetworkAddressesWithTime)

    def Deserialize(self, reader):
        """
        Deserialize full object.

        Args:
            reader (kaze.IO.BinaryReader):
        """
        self.NetworkAddressesWithTime = reader.ReadSerializableArray(
            'kaze.Network.Payloads.NetworkAddressWithTime.NetworkAddressWithTime')

    def Serialize(self, writer):
        """
        Serialize object.

        Args:
            writer (kaze.IO.BinaryWriter):
        """
        writer.WriteVarInt(len(self.NetworkAddressesWithTime))
        for address in self.NetworkAddressesWithTime:
            address.Serialize(writer)
