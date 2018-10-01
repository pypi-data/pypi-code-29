########################################################################################################################
#    File: bank.py
#  Author: Dan Huckson, https://github.com/unodan
#    Date: 2018-09-20
########################################################################################################################

from tkinter import Toplevel, Label, Entry


class Bank(Toplevel):  # A View
    def __init__(self, master, title):
        Toplevel.__init__(self, master)
        self.title(title)

        self.protocol('WM_DELETE_WINDOW', self.master.destroy)

        Label(self, text='Account Balance').pack(side='left')
        self.balance = Entry(self, width=8)
        self.balance.pack(side='left')

    def set_balance(self, amount):
        self.balance.delete(0, 'end')
        self.balance.insert('end', str(amount))

