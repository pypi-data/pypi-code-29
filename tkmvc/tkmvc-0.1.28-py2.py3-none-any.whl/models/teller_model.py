########################################################################################################################
#    File: teller_model.py
#  Author: Dan Huckson, https://github.com/unodan
#    Date: 2018-10-03
########################################################################################################################


class TellerModel:
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

    def deposit(self, value):
        self.set(float(self.get()) + float(value))

    def withdrawal(self, value):
        self.set(float(self.get()) - float(value))

