
from kaze.Core.Mixins import VerifiableMixin


class InventoryMixin(VerifiableMixin):

    Hash = None
    InventoryType = None

    def Verify(self):
        pass
