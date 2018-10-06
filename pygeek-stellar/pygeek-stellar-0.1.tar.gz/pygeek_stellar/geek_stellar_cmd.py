# System imports
from cmd import Cmd
import os
import shlex
# Local imports
from .stellar_requests import *


class GeekStellarCmd(Cmd):

    def __init__(self, session):
        super(GeekStellarCmd, self).__init__()
        self.session = session
        self.prompt = '> '

    def cmdloop(self, intro=None):
        """
        Extend the base class cmdloop method to call do_quit() when a KeyboardInterrupt
        (ctr+c) is received
        """
        while True:
            try:
                super(GeekStellarCmd, self).cmdloop()
            except KeyboardInterrupt:
                self.do_quit(None)

    def do_current_account(self, args):
        """
        Prints information regarding the current Stellar account being used
        """
        print('{}'.format(self.session.to_str()))

    def do_xlm_balance(self, args):
        """
        Requests the current XLM (Stellar Lumens) balance from the Stellar Horizon server.
        """
        balance = get_xlm_balance(self.session)
        if balance != -1:
            print('XLM Balance: {}'.format(balance))

    def do_magnet_balance(self, args):
        """
        Requests the current MAG (Magnets) balance from the Stellar Horizon server.
        """
        balance = get_magnet_balance(self.session)
        if balance != -1:
            print('Magnet Balance: {}'.format(balance))

    def do_request_funds(self, args):
        """
        Requests funds from the Stellar Testnet Friendbot. This request will only be successful
        a single time for each Stellar Testnet address. The request will fail if the address
        belongs to the real Stellar network.
        """
        result = fund_using_friendbot(self.session)
        print('Friendbot funding result: ' + result)

    def do_send_xlm_payment(self, args):
        """
        Sends a XLM payment to the given destination address
        Usage: send_xlm_payment {destination_address} {amount} {transaction_memo: optional}
        """
        args = shlex.split(args)
        if len(args) < 2:
            print('A destination address and an amount are mandatory')
            return

        destination = args[0]
        amount = args[1].replace(',','.')
        memo = '' if len(args) < 3 else args[2]  # memo is optional

        if not is_float_str(amount):
            print('The amount to transfer must but a valid value')
            return

        send_xlm_payment(self.session, destination, amount, memo)

    @staticmethod
    def do_cls(args):
        """
        Clear the screen
        """
        os.system('cls' if os.name == 'nt' else 'clear')  # Use cls for Windows and clear for Unix

    @staticmethod
    def do_quit(args):
        """
        Quits the program.
        """
        print("Quitting.")
        raise SystemExit

