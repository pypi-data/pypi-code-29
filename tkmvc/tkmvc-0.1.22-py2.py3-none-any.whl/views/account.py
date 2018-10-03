########################################################################################################################
#    File: account_model.py
#  Author: Dan Huckson, https://github.com/unodan
#    Date: 2018-09-20
########################################################################################################################

from tkinter import Toplevel, Label, Entry


class Account(Toplevel):  # A View
    def __init__(self, master, title):
        Toplevel.__init__(self, master)
        self.title(title)

        Label(self, text='Balance').pack(side='left')
        self.balance = Entry(self, width=8)
        self.balance.pack(side='left')

    def set_balance(self, amount):
        self.balance.delete(0, 'end')
        self.balance.insert('end', str(amount))

