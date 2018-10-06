#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct  6 12:21:04 2018

@author: andrew
"""

import numpy as np
import math

def flux_ratio(p_laser, p_star, d, lamb):
    f_ratio = (float(p_laser)/float(p_star))*(np.pi)*d**2/(lamb**2)
    return f_ratio