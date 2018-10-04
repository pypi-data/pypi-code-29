from kazecore.IO.Mixins import SerializableMixin
from kazecore.IO.BinaryWriter import BinaryWriter
from kaze.IO.MemoryStream import StreamManager
from kaze.Core.Size import Size as s


class StateBase(SerializableMixin):
    StateVersion = 0

    def Size(self):
        """
        Get the total size in bytes of the object.

        Returns:
            int: size.
        """
        return s.uint8

    @staticmethod
    def DeserializeFromDB(buffer):
        """
        Deserialize full object.

        Args:
            buffer (bytes, bytearray, BytesIO): (Optional) data to create the stream from.
        """
        pass

    def Deserialize(self, reader):
        """
        Deserialize full object.

        Args:
            reader (kazecore.IO.BinaryReader):

        Raises:
            Exception: if the state version is incorrect.
        """
        sv = reader.ReadByte()
        if sv != self.StateVersion:
            raise Exception("Incorrect State format")

    def Serialize(self, writer):
        """
        Serialize full object.

        Args:
            writer (kaze.IO.BinaryWriter):
        """
        writer.WriteByte(self.StateVersion)

    def ToByteArray(self):
        """
        Serialize self and get the byte stream.

        Returns:
            bytes: serialized object.
        """
        ms = StreamManager.GetStream()
        writer = BinaryWriter(ms)
        self.Serialize(writer)

        retval = ms.ToArray()
        StreamManager.ReleaseStream(ms)

        return retval

    def ToJson(self):
        """
        Convert object members to a dictionary that can be parsed as JSON.

        Returns:
             dict:
        """
        return {
            'version': self.StateVersion
        }
