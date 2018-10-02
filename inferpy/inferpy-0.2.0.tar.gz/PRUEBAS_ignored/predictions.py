
import inferpy as inf
import edward as ed
import tensorflow as tf
import numpy as np
from six import iteritems


sess = ed.get_session()

flag_y = True
f = 2
# graph



N = 1000 # number of observations
# model definition
with inf.ProbModel() as m:
    # prior (latent variable)
    beta = inf.models.Normal(loc=0, scale=1, name="beta")
    w = inf.models.Normal(loc=0, scale=1, name = "w")
    b = inf.models.Normal(loc=0, scale=1, name="b")


    # observed variable
    with inf.replicate(size=N):
        x = inf.models.Normal(loc=beta, scale=1, observed=True, name="x")
        y = inf.models.Normal(loc = w*x+b, scale=1, observed=True, name="y")



# toy data generation

x_train = inf.models.Normal(loc=10, scale=3, dim=1).sample(N)
y_train = x_train*f + inf.models.Normal(loc=1, scale=0.1, dim=1).sample(N)


data = {x.name : x_train, y.name : y_train}

m.compile()
m.fit(data)

qbeta = m.posterior(beta)
qw = m.posterior(w)
qb = m.posterior(b)





sess = ed.get_session()

sess.run([qw.dist])


#####
x_test = inf.models.Normal(loc=10, scale=3, dim=1).sample(N)
y_test = x_test*f + inf.models.Normal(loc=1, scale=0.1, dim=1).sample(N)

x_pred = m.predict(x, data={y:y_test})

x_pred.loc


inf.evaluate("mean_squared_error", n_samples=1000, data={x_pred:x_test}) #0.35903236

inf.criticism.evaluate("log_lik", n_samples=1000, data={x_pred:x_test}) #-1.0081486


inf.evaluate()