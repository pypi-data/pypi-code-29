########################################################################################################################
#    File: view.py
#  Author: Dan Huckson, https://github.com/unodan
#    Date: 2018-09-20
########################################################################################################################

from tkinter import Toplevel, Label, Entry


class View(Toplevel):  # View
    def __init__(self, master):
        Toplevel.__init__(self, master)
        self.protocol('WM_DELETE_WINDOW', self.master.destroy)

        Label(self, text='Account Balance').pack(side='left')
        self.balance = Entry(self, width=8)
        self.balance.pack(side='left')

