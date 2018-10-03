########################################################################################################################
#    File: bank_view.py
#  Author: Dan Huckson, https://github.com/unodan
#    Date: 2018-10-03
########################################################################################################################

from tkinter import Toplevel, Label, Entry, StringVar, IntVar, LabelFrame


class BankView(Toplevel):  # A View
    def __init__(self, master, title):
        Toplevel.__init__(self, master)
        self.title(title)

        self.protocol('WM_DELETE_WINDOW', self.master.destroy)

        frame = LabelFrame(self, text='Interest')

        self.rate = StringVar()
        self.rate.set('0.0125')
        Label(frame, text=' Rate ').grid(sticky='e')
        self.interest_rate = Entry(frame, width=8, textvariable=self.rate)
        self.interest_rate.grid(padx=(0, 10), pady=(0, 10), row=0, column=1, sticky='w')

        self.period = IntVar()
        self.period.set(1000)
        Label(frame, text=' Time (APR) ').grid()
        self.interest_period = Entry(frame, width=25, textvariable=self.period)
        self.interest_period.grid(padx=(0, 10), pady=(0, 10), row=1, column=1)

        frame.grid(pady=(0, 5), sticky='ew')

    def get_interest_rate(self):
        return float(self.rate.get())

    def get_interest_period(self):
        try:
            period = self.period.get()
        except:
            period = 0

        return int(period)
