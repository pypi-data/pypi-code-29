########################################################################################################################
#    File: models.py
#  Author: Dan Huckson, https://github.com/unodan
#    Date: 2018-09-20
########################################################################################################################
import threading


class Transaction:
    def __init__(self):
        self.value = 0
        self.callbacks = {}

    def add_callback(self, func):
        self.callbacks[func] = None

    def _callbacks(self):
        for func in self.callbacks:
            func(self.value)

    def set(self, value):
        self.value = value
        self._callbacks()

    def get(self):
        return self.value


class Interest:  # A Model
    def __init__(self):
        self.transaction = Transaction()
