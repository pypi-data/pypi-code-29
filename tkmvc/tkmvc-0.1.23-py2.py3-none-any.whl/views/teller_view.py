########################################################################################################################
#    File: main.py
#  Author: Dan Huckson, https://github.com/unodan
#    Date: 2018-09-19
# Purpose: MVC (Model View Controller) Demo
########################################################################################################################

from tkinter import Toplevel, Label, Entry, Button


class TellerView(Toplevel):  # A View
    def __init__(self, master, title):
        Toplevel.__init__(self, master)
        self.title(title)

        Label(self, text='Amount').pack(side='left')
        self.amount = Entry(self, width=8)
        self.amount.pack(side='left')

        self.btn_deposit = Button(self, text='Deposit', width=8)
        self.btn_deposit.pack(side='left')

        self.btn_withdrawal = Button(self, text='Withdrawal', width=8)
        self.btn_withdrawal.pack(side='left')
