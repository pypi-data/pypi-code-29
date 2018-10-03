########################################################################################################################
#    File: customer_view.py
#  Author: Dan Huckson, https://github.com/unodan
#    Date: 2018-10-03
########################################################################################################################

from tkinter import Toplevel, Label, Entry, StringVar, LabelFrame


class CustomerView(Toplevel):  # A View
    def __init__(self, master, title):
        Toplevel.__init__(self, master)
        self.title(title)

        frame = LabelFrame(self, text='Customer')

        self.id = StringVar()
        self.id.set('4352112-112')
        Label(frame, text=' Account # ').grid(sticky='w')
        self.customer_id = Entry(frame, width=12, textvariable=self.id)
        self.customer_id.grid(padx=(0, 10), pady=(0, 10), row=0, column=1, sticky='w')

        self.first_name = StringVar()
        self.first_name.set('John')
        Label(frame, text=' First Name ').grid(sticky='w')
        self.customer_first_name = Entry(frame, width=20, textvariable=self.first_name)
        self.customer_first_name.grid(padx=(0, 10), pady=(0, 10), row=1, column=1)

        self.last_name = StringVar()
        self.last_name.set('Doe')
        Label(frame, text=' Last Name ').grid(sticky='w')
        self.customer_last_name = Entry(frame, width=20, textvariable=self.last_name)
        self.customer_last_name.grid(padx=(0, 10), pady=(0, 10), row=2, column=1)

        frame.grid(pady=(0, 5), sticky='ew')

        frame = LabelFrame(self, text='Account')

        self.balance = StringVar()
        self.balance.set(0)
        Label(frame, text=' Balance ').grid()
        self.account_balance = Entry(frame, width=25, textvariable=self.balance)
        self.account_balance.grid(pady=(0, 10), padx=(0, 10), sticky='ew', row=0, column=1)

        frame.grid(row=3, pady=(0, 5), sticky='ew')

    def get_customer_id(self):
        return self.customer_id.get()

    def set_balance(self, amount):
        self.account_balance.delete(0, 'end')
        self.account_balance.insert('insert', str(amount))

    def get_balance(self):
        return float(self.balance.get())

