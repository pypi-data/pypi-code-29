from .instance import shared_cread_instance

from creabase.exceptions import WitnessDoesNotExistsException


class Witness(dict):
    """ Read data about a witness in the chain

        :param str witness: Name of the witness
        :param Cread cread_instance: Cread() instance to use when
        accessing a RPC

    """

    def __init__(self, witness, cread_instance=None):
        self.cread = cread_instance or shared_cread_instance()
        self.witness_name = witness
        self.witness = None
        self.refresh()

    def refresh(self):
        witness = self.cread.get_witness_by_account(self.witness_name)
        if not witness:
            raise WitnessDoesNotExistsException
        super(Witness, self).__init__(witness)

    def __getitem__(self, key):
        return super(Witness, self).__getitem__(key)

    def items(self):
        return super(Witness, self).items()
