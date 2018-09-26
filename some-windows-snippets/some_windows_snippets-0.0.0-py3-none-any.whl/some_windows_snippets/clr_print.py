# -*- coding: utf-8 -*-

### imports ###################################################################
import clr
import logging
import yaml

### dotNet imports ############################################################
clr.AddReference('System.Drawing')
from System.Drawing import Brushes, Font, FontStyle, GraphicsUnit
from System.Drawing.Printing import PrintDocument, PrinterSettings
from System.Drawing.Printing import StandardPrintController

### logger ####################################################################
logging.getLogger('clr_printer').addHandler(logging.NullHandler())

###############################################################################
class Printer(PrintDocument):
    def __init__(self, config, debug=False):
        self.debug = debug
        self.logger = logging.getLogger('clr_printer')
        self.name = 'Brother QL-700'
        self.parameterDict = {}
        self.PrintController = StandardPrintController()
        self.printer = None

        self.readConfig(config)

        for i in range(PrinterSettings.InstalledPrinters.Count):
            printer = PrinterSettings.InstalledPrinters[i]
    
            if printer.find(self.name) >= 0:
                self.PrinterSettings.PrinterName = self.printer = printer
                self.DefaultPageSettings.Landscape = False

    def printLabel(self, data):
        pdLabel = PrintLabel(config=self.parameterDict, debug=self.debug)
        pdLabel.printLabel(data)
        
    def readConfig(self, filename):
        with open(filename) as f:
            self.parameterDict = yaml.load(f)

        for key, value in self.parameterDict.items():
            if key == 'name':
                self.name = value

###############################################################################                  
class Label:
    def __init__(self, parameterDict):
        self.brushes = {}
        self.brushesList = []
        self.label_strings = []
        self.fonts = {}
        self.fontsDict = {}
        self.params = parameterDict

        for key, value in parameterDict.items():
            if key == 'fonts':
                self.fontsDict = value
            elif key == 'label':
                self.label_strings = value

        self.init_brushes()
        self.init_fonts()

    def init_brushes(self):        
        self.brushes['black'] = Brushes.Black

    def init_fonts(self):
        for key, value in self.fontsDict.items():
            family = value['family']
            size = value['size']
            style_name = value['style']

            style = FontStyle.Regular
                
            if style_name == 'regular':
                style = FontStyle.Regular
            elif style_name == 'bold':
                style = FontStyle.Bold

            self.fonts[key] = Font(family, size, style)

    def handler(self, source, args):
        args.Graphics.PageUnit = GraphicsUnit.Millimeter

        for l in self.label_strings:
            text = ''
            
            for key, value in l.items():
                if key == 'brush':
                    brush = self.brushes[value]
                elif key == 'font':
                    font = self.fonts[value]
                elif key == 'name':
                    name = value
                elif key == 'text':
                    text = value

            if not text:
                text = self.params[name]

            args.Graphics.DrawString(
                text, font, brush, l['x'], l['y'])

###############################################################################
class PrintLabel(PrintDocument):
    def __init__(self, config, debug=False):
        self.debug = debug
        self.logger = logging.getLogger('clr_printer')
        self.name = 'Brother QL-700'
        self.parameterDict = {}
        self.PrintController = StandardPrintController()
        self.printer = None

        self.parameterDict = config

        for i in range(PrinterSettings.InstalledPrinters.Count):
            printer = PrinterSettings.InstalledPrinters[i]
    
            if printer.find(self.name) >= 0:
                self.PrinterSettings.PrinterName = self.printer = printer
                self.DefaultPageSettings.Landscape = False
                
    def printLabel(self, data):
        label_params = dict(self.parameterDict)
        label_params.update(data)
        
        label = Label(label_params)
        self.PrintPage += label.handler
        
        if self.debug:
            self.logger.debug('label not printed in debug mode')

            print()
            print('Label')
            print('=====')
            
            for l in label.label_strings:
                if 'text' not in l.keys():
                    name = l['name']
                    print("%7s: %s" % (name, label_params[name]))

            print('')
            
        else:
            self.logger.debug('printing label')
            self.Print()
            
        return label_params    
        