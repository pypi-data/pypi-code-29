# -*- coding: utf-8 -*-
"""
Created on Wed Sep 12 22:50:21 2018

@author: letic
"""
""" Function of linear congruences for random bid of computer  """
	

####function of linear congruences for random bid of computer
def random_bid(prev_random_numb):
   """Function to obtain the random number""" 
   new_random_numb = (22695477 * prev_random_numb + 1) % 2**32 #Method of linear congruences
   if new_random_numb > 2**31:
      rbid = 1
   else:
      rbid = 0
   return(new_random_numb, rbid)