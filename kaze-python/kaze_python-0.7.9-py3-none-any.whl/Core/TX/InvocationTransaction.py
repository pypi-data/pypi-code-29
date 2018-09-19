from kaze.Core.TX.Transaction import Transaction, TransactionType
import sys
from kazecore.Fixed8 import Fixed8
from kaze.Core.Size import GetVarSize


class InvocationTransaction(Transaction):
    Script = None
    stream = None

    def SystemFee(self):
        """
        Get the system fee.

        Returns:
            Fixed8:
        """
        return self.stream // Fixed8.FD()

    def __init__(self, *args, **kwargs):
        """
        Create an instance.

        Args:
            *args:
            **kwargs:
        """
        super(InvocationTransaction, self).__init__(*args, **kwargs)
        self.stream = Fixed8(0)
        self.Type = TransactionType.InvocationTransaction

    def Size(self):
        """
        Get the total size in bytes of the object.

        Returns:
            int: size.
        """
        return super(InvocationTransaction, self).Size() + GetVarSize(self.Script)

    def DeserializeExclusiveData(self, reader):
        """
        Deserialize full object.

        Args:
            reader (kaze.IO.BinaryReader):

        Raises:
            Exception: If the version read is incorrect.
        """
        if self.Version > 1:
            raise Exception('Invalid format')

        self.Script = reader.ReadVarBytes()

        if len(self.Script) == 0:
            raise Exception('Invalid Format')

        if self.Version >= 1:
            self.stream = reader.ReadFixed8()
            if self.stream < Fixed8.Zero():
                raise Exception("Invalid Format")
        else:
            self.stream = Fixed8(0)

    def SerializeExclusiveData(self, writer):
        """
        Serialize object.

        Args:
            writer (kaze.IO.BinaryWriter):
        """
        writer.WriteVarBytes(self.Script)
        if self.Version >= 1:
            writer.WriteFixed8(self.stream)

    def Verify(self, mempool):
        """
        Verify the transaction.

        Args:
            mempool:

        Returns:
            bool: True if verified. False otherwise.
        """
        if self.stream.value % 100000000 != 0:
            return False
        return super(InvocationTransaction, self).Verify(mempool)

    def ToJson(self):
        """
        Convert object members to a dictionary that can be parsed as JSON.

        Returns:
             dict:
        """
        jsn = super(InvocationTransaction, self).ToJson()
        jsn['script'] = self.Script.hex()
        jsn['stream'] = self.stream.value
        return jsn
