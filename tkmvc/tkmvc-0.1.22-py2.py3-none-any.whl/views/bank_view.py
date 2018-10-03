########################################################################################################################
#    File: account_model.py
#  Author: Dan Huckson, https://github.com/unodan
#    Date: 2018-09-20
########################################################################################################################

from tkinter import Toplevel, Label, Entry, StringVar, IntVar


class BankView(Toplevel):  # A View
    def __init__(self, master, title):
        Toplevel.__init__(self, master)
        self.title(title)

        self.protocol('WM_DELETE_WINDOW', self.master.destroy)

        self.balance = StringVar()
        self.balance.set(0)
        Label(self, text=' Balance ').pack(side='left')
        self.account_balance = Entry(self, width=20, textvariable=self.balance)
        self.account_balance.pack(side='left')

        self.rate = StringVar()
        self.rate.set('0.0125')
        Label(self, text=' Interest Rate ').pack(side='left')
        self.interest_rate = Entry(self, width=8, textvariable=self.rate)
        self.interest_rate.pack(side='left')

        self.period = IntVar()
        self.period.set(1000)
        Label(self, text=' Interest Period ').pack(side='left')
        self.interest_period = Entry(self, width=15, textvariable=self.period)
        self.interest_period.pack(side='left')

    def set_balance(self, amount):
        self.account_balance.delete(0, 'end')
        self.account_balance.insert('insert', str(amount))

    def get_balance(self):
        return float(self.balance.get())

    def get_interest_rate(self):
        return float(self.rate.get())

    def get_interest_period(self):
        try:
            period = self.period.get()
        except:
            period = 0

        return int(period)
