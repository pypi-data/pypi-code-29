########################################################################################################################
#    File: teller_view.py
#  Author: Dan Huckson, https://github.com/unodan
#    Date: 2018-10-03
########################################################################################################################

from tkinter import Toplevel, Label, Entry, Button, StringVar, LabelFrame


class TellerView(Toplevel):
    def __init__(self, master, title):
        Toplevel.__init__(self, master)
        self.title(title)

        frame = LabelFrame(self, text='Customer')
        frame.grid(pady=(0, 5), sticky='ew')

        self.id = StringVar()
        self.id.set('4352112-112')
        Label(frame, text=' Account # ').grid(sticky='w')
        self.customer_id = Entry(frame, width=12, textvariable=self.id)
        self.customer_id.grid(padx=(0, 10), pady=(0, 10), row=0, column=1, sticky='w')

        frame = LabelFrame(self, text='Account')
        frame.grid(pady=(0, 5), sticky='ew')

        frame = LabelFrame(self, text='Teller')
        frame.grid(sticky='ew')

        Label(frame, text=' Amount ').grid()
        self.amount = Entry(frame, width=25)
        self.amount.grid(pady=(0, 5), padx=5, sticky='ew', row=0, column=1)

        frame = LabelFrame(frame, text='Transaction Type')
        frame.grid(padx=5, pady=5, columnspan=2, sticky='ew')
        self.btn_deposit = Button(frame, text='Deposit', width=8)
        self.btn_deposit.grid(padx=(5, 0), pady=5, row=2)

        self.btn_withdrawal = Button(frame, text='Withdrawal', width=8)
        self.btn_withdrawal.grid(padx=(5, 0), pady=5, row=2, column=1)
