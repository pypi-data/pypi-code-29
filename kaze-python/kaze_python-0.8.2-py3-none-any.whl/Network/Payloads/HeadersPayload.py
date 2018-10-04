from kazecore.IO.Mixins import SerializableMixin
import sys
from kaze.Core.Size import GetVarSize
from kazecore.IO.BinaryWriter import BinaryWriter


class HeadersPayload(SerializableMixin):
    Headers = []

    def __init__(self, headers=None):
        """
        Create an instance.

        Args:
            headers (list): of kaze.Core.Header.Header objects.
        """
        self.Headers = headers if headers else []

    def Size(self):
        """
        Get the total size in bytes of the object.

        Returns:
            int: size.
        """
        return GetVarSize(self.Headers)

    def Deserialize(self, reader):
        """
        Deserialize full object.

        Args:
            reader (kaze.IO.BinaryReader):
        """
        self.Headers = reader.ReadSerializableArray('kaze.Core.Header.Header')

    def Serialize(self, writer: BinaryWriter):
        """
        Serialize object.

        Args:
            writer (kaze.IO.BinaryWriter):
        """
        writer.WriteSerializableArray(self.Headers)
