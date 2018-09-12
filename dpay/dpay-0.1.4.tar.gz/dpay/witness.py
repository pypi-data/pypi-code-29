from .instance import shared_dpayd_instance

from dpaybase.exceptions import WitnessDoesNotExistsException


class Witness(dict):
    """ Read data about a witness in the chain

        :param str witness: Name of the witness
        :param DPayd dpayd_instance: DPayd() instance to use when
        accessing a RPC

    """

    def __init__(self, witness, dpayd_instance=None):
        self.dpayd = dpayd_instance or shared_dpayd_instance()
        self.witness_name = witness
        self.witness = None
        self.refresh()

    def refresh(self):
        witness = self.dpayd.get_witness_by_account(self.witness_name)
        if not witness:
            raise WitnessDoesNotExistsException
        super(Witness, self).__init__(witness)

    def __getitem__(self, key):
        return super(Witness, self).__getitem__(key)

    def items(self):
        return super(Witness, self).items()
