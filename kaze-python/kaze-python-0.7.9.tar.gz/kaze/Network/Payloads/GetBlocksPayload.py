import sys
import binascii
from kazecore.IO.Mixins import SerializableMixin
from kazecore.UInt256 import UInt256
from kaze.Core.Size import GetVarSize


class GetBlocksPayload(SerializableMixin):
    HashStart = []
    HashStop = None

    def __init__(self, hash_start=[], hash_stop=UInt256()):
        """
        Create an instance.

        Args:
            hash_start (list): a list of hash values. Each value is of the bytearray type. Note: should actually be UInt256 objects.
            hash_stop (UInt256):
        """
        self.HashStart = hash_start
        self.HashStop = hash_stop

    def Size(self):
        """
        Get the total size in bytes of the object.

        Returns:
            int: size.
        """
        corrected_hashes = list(map(lambda i: UInt256(data=binascii.unhexlify(i)), self.HashStart))
        return GetVarSize(corrected_hashes) + self.hash_stop.Size

    def Deserialize(self, reader):
        """
        Deserialize full object.

        Args:
            reader (kaze.IO.BinaryReader):
        """
        self.HashStart = reader.ReadSerializableArray('kazecore.UInt256.UInt256')
        self.HashStop = reader.ReadUInt256()

    def Serialize(self, writer):
        """
        Serialize object.

        Args:
            writer (kaze.IO.BinaryWriter):
        """
        writer.WriteHashes(self.HashStart)
        if self.HashStop is not None:
            writer.WriteUInt256(self.HashStop)
