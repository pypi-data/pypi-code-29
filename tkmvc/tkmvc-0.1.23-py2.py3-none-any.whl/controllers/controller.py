########################################################################################################################
#    File: controller.py
#  Author: Dan Huckson, https://github.com/unodan
#    Date: 2018-09-19
########################################################################################################################

from tkinter import Tk
from tkmvc.models import Account, Interest
from tkmvc.views import AccountView, BankView, CustomerView


class Controller(Tk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.withdraw()

        self.views = {
            'bank': BankView(self, 'The Bank'),
            'teller': AccountView(self, 'The Teller'),
            'customer': CustomerView(self, 'The Customer'),
        }

        self.view('teller').btn_deposit.config(command=self.make_deposit)
        self.view('teller').btn_withdrawal.config(command=self.make_withdrawal)

        self.account = Account()
        self.account.transaction.add_callback(self.update_account)
        self.update_account(self.account.transaction.get())

        self.interest = Interest()
        self.interest.transaction.add_callback(self.add_interest)
        self.add_interest(self.interest.transaction.set(0))

    def view(self, key):
        if key in self.views:
            return self.views[key]

        return False

    def make_deposit(self):
        self.account.deposit(int(self.view('teller').amount.get()))

    def make_withdrawal(self):
        self.account.withdrawal(int(self.view('teller').amount.get()))

    def update_account(self, amount):
        self.view('customer').set_balance(amount)

    def add_interest(self, amount=0):
        amount = self.view('customer').get_balance()
        amount = amount + amount * self.view('bank').get_interest_rate()
        self.view('customer').set_balance(amount)
        self.view('customer').after(self.view('bank').get_interest_period(), self.add_interest)
