########################################################################################################################
#    File: controller.py
#  Author: Dan Huckson, https://github.com/unodan
#    Date: 2018-10-03
########################################################################################################################

from tkinter import Tk
from tkmvc.models import TellerModel, BankModel
from tkmvc.views import TellerView, BankView, CustomerView


class Controller(Tk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.withdraw()

        self.views = {
            'bank': BankView(self, 'The Bank'),
            'teller': TellerView(self, 'The Teller'),
            'customer': CustomerView(self, 'The Customer'),
        }

        self.view('teller').btn_deposit.config(command=self.make_deposit)
        self.view('teller').btn_withdrawal.config(command=self.make_withdrawal)

        self.account = TellerModel()
        self.account.add_callback(self.update_account)
        self.update_account(self.account.get())

        self.interest = BankModel()
        self.interest.add_callback(self.add_interest)
        self.add_interest(self.interest.set(0))

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
        if amount:
            amount = amount + amount * self.view('bank').get_interest_rate()
            self.view('customer').set_balance(amount)

        self.view('customer').after(self.view('bank').get_interest_period(), self.add_interest)
