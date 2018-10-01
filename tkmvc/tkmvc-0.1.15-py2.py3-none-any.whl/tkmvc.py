# -*- coding: utf-8 -*-
########################################################################################################################
#    File: main.py
#  Author: Dan Huckson, https://github.com/unodan
#    Date: 2018-09-19
########################################################################################################################


from .models import Account
from .views import Bank, Teller
from .controllers import Controller


class App(Controller):  # The Controller
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.account = Account()
        self.account.transaction.add_callback(self.update_account)

        self.views = {'bank': Bank(self, 'The Bank'), 'teller': Teller(self, 'The Teller')}

        self.views['teller'].btn_deposit.config(command=self.make_deposit)
        self.views['teller'].btn_withdrawal.config(command=self.make_withdrawal)

        self.update_account(self.account.transaction.get())

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
