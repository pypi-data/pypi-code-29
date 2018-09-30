# -*- coding: utf-8 -*-
########################################################################################################################
#    File: main.py
#  Author: Dan Huckson, https://github.com/unodan
#    Date: 2018-09-19
########################################################################################################################


from .models import Model
from .views import View
from .controllers import Controller


class App(Controller):  # The Controller
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.model = Model()
        self.views = {'root': View(self)}

        print(123, self.model.value())

    def view(self, key):
        if key in self.views:
            return self.views[key]

        return False

    def defaults(self, key):
        print(321, key)
