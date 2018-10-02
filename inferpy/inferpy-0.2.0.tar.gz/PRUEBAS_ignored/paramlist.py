import inferpy as inf
import edward as ed
import tensorflow as tf




from inferpy.models.params import *


d=4
N=10
K=3

p = [0.2, 0.7, 0.1]
p = inf.models.Dirichlet(np.ones(K))

p = inf.models.Normal(0,1)


with inf.replicate(size=N):
    pl = ParamList(params=["loc"], args_list=[p],  is_simple={"probs": True}, param_dim=d)
    print (pl)
    rd = pl.get_reshaped_param_dict()

    rd

x = inf.models.Normal(loc=1., scale=100, name="x")

with inf.replicate(size=100):
    y = inf.models.Normal(loc=x, scale=0.0001, dim=3, name="y", observed=True)

