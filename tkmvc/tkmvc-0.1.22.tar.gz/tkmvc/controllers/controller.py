########################################################################################################################
#    File: controller.py
#  Author: Dan Huckson, https://github.com/unodan
#    Date: 2018-09-19
########################################################################################################################

import threading
from tkinter import Tk
from tkmvc.models import Account, Interest
from tkmvc.views import TellerView, BankView


class Controller(Tk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.withdraw()

        self.views = {
            'bank': BankView(self, 'The Bank'),
            'teller': TellerView(self, 'The Teller'),
        }

        self.views['teller'].btn_deposit.config(command=self.make_deposit)
        self.views['teller'].btn_withdrawal.config(command=self.make_withdrawal)

        self.account = Account()
        self.account.transaction.add_callback(self.update_account)
        self.update_account(self.account.transaction.get())

        self.interest = Interest()
        self.interest.transaction.add_callback(self.update_interest)
        self.update_interest(self.interest.transaction.set(0))

    def view(self, key):
        if key in self.views:
            return self.views[key]

        return False

    def make_deposit(self):
        self.account.deposit(int(self.views['teller'].amount.get()))

    def make_withdrawal(self):
        self.account.withdrawal(int(self.views['teller'].amount.get()))

    def update_account(self, amount):
        self.views['bank'].set_balance(amount)

    def update_interest(self, amount=0):
        amount = self.views['bank'].get_balance()
        amount = amount + amount * self.views['bank'].get_interest_rate()
        self.views['bank'].set_balance(amount)
        self.views['bank'].after(self.views['bank'].get_interest_period(), self.update_interest)
