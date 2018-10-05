#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct  5 14:30:49 2018

@author: andrew
"""
import numpy as np
import glob

pys = glob.glob("/home/andrew/sdi_pipeline/sdi_pipeline/*.py")

with open('/home/andrew/sdi_pipeline/MANIFEST', 'a') as test:
    for i in pys:
        test.write(i[len('/home/andrew/sdi_pipeline/'):] + '\n')
    test.close()
    
#with open('/home/andrew/sdi/targets/TEST/21:40:47.388_+00:28:35.11/B/90/sources/sources.txt', 'r') as source:
#    lines = source.readlines()
#    source.close()
#
#with open('/home/andrew/sdi_pipeline/sdi_pipeline/test_config/test_sources.txt', 'a') as tes:
#    tes.writelines(lines)
#    tes.close()