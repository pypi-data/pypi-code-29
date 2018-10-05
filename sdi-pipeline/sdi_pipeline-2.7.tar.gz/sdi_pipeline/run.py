#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct  3 17:45:48 2018

@author: andrew
"""

import get
import align
import combine
import subtract
import extract
import pipeline
import initialize

if __name__ == '__main__':
    print('\n\t -----------------------------------------------------')
    print('\t            SDI Difference Imaging Pipeline          ')
    print('\t                         v.2.6                       ')
    print('\t  Developed for the SDI optical SETI program @ UCSB  ')
    print('\t             http://www.deepspace.ucsb.edu            ')
    print('\tContact andrew.henry.stewart@emory.edu for bug reports')
    print('\t -----------------------------------------------------')
    method = input('-> Enter method: ')
    if method == 'get':
        get.GET()
    elif method == 'align':
        align.ALIGN()
    elif method == 'combine':
        combine.COMBINE()
    elif method == 'subtract':
        subtract.SUBTRACT()
    elif method == 'extract':
        extract.SEXTRACTOR()
    elif method == 'pipeline':
        pipeline.PIPELINE()
    elif method == 'initialize':
        initialize.INITIALIZE()
    else:
        print("-> Error: Method not recognized")