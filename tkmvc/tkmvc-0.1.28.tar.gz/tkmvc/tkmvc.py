# -*- coding: utf-8 -*-
########################################################################################################################
#    File: main.py
#  Author: Dan Huckson, https://github.com/unodan
#    Date: 2018-09-19
########################################################################################################################

from tkmvc.controllers import Controller


class App(Controller):  # Main Controller
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
