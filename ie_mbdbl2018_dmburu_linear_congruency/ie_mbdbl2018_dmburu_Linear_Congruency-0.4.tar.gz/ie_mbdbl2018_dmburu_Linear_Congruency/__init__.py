# -*- coding: utf-8 -*-
"""
Created on Tue Sep 11 13:46:39 2018

@author: mburud
"""
""" Functions to return the Linear Congruency & the random number 1 or 0 generated through it!! """
	
#--------------------------------MY FUNCTIONS for the IPE--------------------------------------#
def linear_congruency(x):   #returns the value obtained from linear congruency caclulation
    a,b,m=22695477,1,2**32
    x = (a*x + b) % m
    return x

def zero_or_one(x):   #returns a zero or one for the linear congruency value
    if x >= 1 and x <= 2**31:
        choice = 0
    else:
        choice = 1
    return choice