import pandas as pd 
import numpy as np
A=np.asarray(['hi']*10).reshape(1,10)
col = ['col']*10
print A
print col
df= pd.DataFrame(A,columns=col)
print df