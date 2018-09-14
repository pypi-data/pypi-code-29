from dpaypy.instance import shared_dpay_instance

from .exceptions import BlockDoesNotExistsException
from .utils import parse_time


class Block(dict):
    """ Read a single block from the chain

        :param int block: block number
        :param DPay dpay_instance: DPay() instance to use when accesing a RPC
        :param bool lazy: Use lazy loading

    """
    def __init__(
        self,
        block,
        dpay_instance=None,
        lazy=False
    ):
        self.dpay = dpay_instance or shared_dpay_instance()
        self.cached = False
        self.block = block

        if isinstance(block, Block):
            super(Block, self).__init__(block)
            self.cached = True
        elif not lazy:
            self.refresh()

    def refresh(self):
        block = self.dpay.rpc.get_block(self.block)
        if not block:
            raise BlockDoesNotExistsException
        super(Block, self).__init__(block)
        self.cached = True

    def __getitem__(self, key):
        if not self.cached:
            self.refresh()
        return super(Block, self).__getitem__(key)

    def items(self):
        if not self.cached:
            self.refresh()
        return super(Block, self).items()

    def time(self):
        return parse_time(self['timestamp'])
