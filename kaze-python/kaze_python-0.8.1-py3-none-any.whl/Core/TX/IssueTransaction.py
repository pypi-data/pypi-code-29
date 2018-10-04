"""
Description:
    Issue Transaction
Usage:
    from kaze.Core.TX.IssueTransaction import IssueTransaction
"""
from kaze.Core.TX.Transaction import Transaction, TransactionType
from kazecore.Fixed8 import Fixed8
from kaze.Blockchain import GetSystemCoin, GetSystemShare


class IssueTransaction(Transaction):
    Nonce = None

    """docstring for IssueTransaction"""

    def __init__(self, *args, **kwargs):
        """
        Create an instance.

        Args:
            *args:
            **kwargs:
        """
        super(IssueTransaction, self).__init__(*args, **kwargs)
        self.Type = TransactionType.IssueTransaction  # 0x40

    def SystemFee(self):
        """
        Get the system fee.

        Returns:
            Fixed8:
        """
        if self.Version >= 1:
            return Fixed8.Zero()

        # if all outputs are kaze or stream, return 0
        all_kaze_stream = True
        for output in self.outputs:
            if output.AssetId != GetSystemCoin().Hash and output.AssetId != GetSystemShare().Hash:
                all_kaze_stream = False
        if all_kaze_stream:
            return Fixed8.Zero()

        return super(IssueTransaction, self).SystemFee()

    def GetScriptHashesForVerifying(self):
        pass

    def DeserializeExclusiveData(self, reader):
        """
        Deserialize full object.

        Args:
            reader (kaze.IO.BinaryReader):
        """

        self.Type = TransactionType.IssueTransaction

        if self.Version > 1:
            raise Exception('Invalid TX Type')

    def SerializeExclusiveData(self, writer):
        pass
