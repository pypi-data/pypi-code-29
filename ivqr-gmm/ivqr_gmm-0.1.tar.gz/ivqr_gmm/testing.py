'''
This file applies the GMM_IVQR method to the Fulton fish market data
The data is collected by Kathryn Graddy available at 
http://people.brandeis.edu/~kgraddy/datasets/fish.out. 
It consists of 111 observation on the price and quantity of whiting transactions everyday. 
The dependent variable Y is the logarithm of total amount of whitings sold each day. 
The endogenous explanatory variable D is the logarithm of the average daily price. 
The exogenous explanatory variables are the day indicators (Monday, Tuesday, Wednesday and Thursday). 
The instrumental variables are weather indicators (Stormy and Mixed).
'''

import numpy as np
import pandas as pd
from . import *


df = pd.read_csv('test_NYfishmarket.csv')
#print(df)
tots = df[['qty']]
#print(tots.values)
#print(tots)
covariate = df[['price']]
instruments = df[['stormy', 'mixed']]
#y = np.array([tots.values],dtype=np.dtype(Dec)).T
#w = np.array(np.concatenate((np.ones((tots.shape[0],1)), covariate.values), axis = 1), dtype=np.dtype(Dec))
#z = np.array(np.concatenate((np.ones((tots.shape[0],1)), instruments.values),axis=1), dtype=np.dtype(Dec))
y = np.array(tots.values)
w = np.concatenate((np.ones((tots.shape[0],1)), covariate.values), axis=1)
z = np.concatenate((np.ones((tots.shape[0],1)), instruments.values),axis=1)
#IVQR_MIO(y, w, Q, tau, T, abgap, bnd, method)
intercept = False
###Some Tuning values to make the program converges faster###
T = 15000
abgap = 1e-2
bnd = np.array([[6,13],[-1,2]])
for tau in [0.25,0.5,0.75]:
   print ('IV reg %g' % tau)
   print (IVQR_GMM(y, w, z, tau, T, abgap, bnd))