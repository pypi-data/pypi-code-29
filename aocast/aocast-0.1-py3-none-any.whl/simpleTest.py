import aocast as ac
import numpy as np
import pandas as pd


#CREATE ADAPTATIVE OPERATOR
ao=ac.AdaptativeOperator()


# =============================================================================
# Simple sin data
# =============================================================================
t = np.linspace((-np.pi), (np.pi), 1000).reshape(-1,1)
y=np.sin(t*100)
x1=np.sin(t*0.1)

window=100
lc=np.asarray([2, 1])

delta=2
crossValidations=100

target,simulation=ao.predict(y,x1,lc,window,delta,crossValidations)
ao.plotPerformance(target,simulation,delta)