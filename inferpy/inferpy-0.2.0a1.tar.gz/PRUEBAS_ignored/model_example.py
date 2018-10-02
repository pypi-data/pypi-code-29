import inferpy as inf
import pandas as pd
import edward as ed
import numpy as np
import tensorflow.contrib.distributions as tfd

N, K, d = 100, 5, 10



# variables

# option 1:


beta = inf.models.MultivariateNormalDiag(loc=[0,0,0], scale_diag=[1,1,1], dim=3)



with inf.replicate(size = N):
    z =  inf.models.Normal(loc=0, scale=1)   # M,H
    x = inf.models.Bernoulli(z*beta, 1, dim=d, observed=True) # M,d, ... k

# option 2:


beta = inf.models.Normal(loc=0, scale=1)

with inf.replicate(size = N):
    z =  inf.models.Normal(loc=0, scale=1)
    x = inf.models.Binomial(total_count=1, logits= z*beta, dim=d, observed=True)




# model definition
m = inf.ProbModel(varlist=[beta,z,x])
m.compile()


# infer the parameters from data
data = pd.read_csv("inferpy/datasets/test.csv")
m.fit(data)


print(m.posterior(beta).loc)


"""
>>> x.shape
[1000, 10]
>>> x.shape
[1000, 10]
>>> x.dim
10
>>> x.batches
1000
>>> beta.loc
array([0.], dtype=float32)
>>> beta.scale
array([1.], dtype=float32)

"""


