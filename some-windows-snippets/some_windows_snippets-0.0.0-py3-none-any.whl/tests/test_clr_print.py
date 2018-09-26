# -*- coding: utf-8 -*-

### imports ###################################################################
import pprint
import os
import unittest

### imports from ##############################################################
from some_windows_snippets.clr_print import Printer

###############################################################################
class TestLabelPrinter(unittest.TestCase):
    def test_00_print(self):
        ## setup printer
        debug = True
        fullfile = os.path.join('config', 'label.cfg')
        printer = Printer(config=fullfile, debug=debug)
   
        ### print first label
        carbon_unit = 'cm' + u'\u207B' + u'\u00B3'
        carbon_value = 1.23E15
        carbon = '[C] = %9.2E %s' % (carbon_value, carbon_unit)
        
        data = {
            'carbon': carbon,
            'machine': 'AB123',
            'sample': 'C4567 - G6U2I / K1',
            'user': 'Wagner'}

        printer.printLabel(data)

        ### print second label
        data = {
            'carbon': 'another carbon value',
            'machine': 'another machine',
            'sample': 'second sample',
            'user': 'another user'}
    
        printer.printLabel(data)

