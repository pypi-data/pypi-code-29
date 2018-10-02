import tensorflow as tf
import os
import inferpy as inf
import numpy as np
import edward as ed
N=10
d=5


with inf.replicate(size=N):
    y = inf.models.Normal(loc=0, scale=1, dim=d) #shape=[N,d]


c = inf.models.Categorical(logits = np.zeros(5), name="c")
yc = inf.models.Normal(loc=2+y[0,c], scale=1)  #shape = [1]



y.dist

c.sample()

c.sample(tf_run=False)

"""

>>> y.dist

<ed.RandomVariable 'inf/Normal_1/' shape=(10, 5) dtype=float32>

>>> c.sample()

array([[3]], dtype=int32)

>>> c.sample(tf_run=False)

<tf.Tensor 'z/sample_2/Reshape_1:0' shape=(1, 1) dtype=int32>

"""

K, d, N, T = 3, 4, 1000, 5000


# toy data generation
x_train = np.vstack([inf.models.Normal(loc=0, scale=1, dim=d).sample(300),
                     inf.models.Normal(loc=10, scale=1, dim=d).sample(700)])


## model definition ##
with inf.ProbModel() as m:

    # prior distributions
    with inf.replicate(size=K):
        mu = inf.models.Normal(loc=0, scale=1, dim=d)
        sigma = inf.models.InverseGamma(1, 1, dim=d)
    p = inf.models.Dirichlet(np.ones(K)/K)

    # define the generative model
    with inf.replicate(size=N):
        z = inf.models.Categorical(probs = p)
        x = inf.models.Normal(mu[z], sigma[z], observed=True, dim=d)


# compile and fit the model with training data
data = {x: x_train}
m.compile(infMethod="MCMC")
m.fit(data)
# print the posterior
print(m.posterior(mu))

######## Edward ##########



## model definition ##
# prior distributions
p = ed.models.Dirichlet(concentration=tf.ones(K)/K)
mu = ed.models.Normal(0.0, 1.0, sample_shape=[K, d])
sigma = ed.models.InverseGamma(concentration=1.0, rate=1.0,
                               sample_shape=[K, d])
# define the generative model
z = ed.models.Categorical(logits=tf.log(p) - tf.log(1.0 - p),
                          sample_shape=N)
x = ed.models.Normal(loc=tf.gather(mu, z), scale=tf.gather(sigma, z))



# compile and fit the model with training data
qp = ed.models.Empirical(params = tf.get_variable( "qp/prm", [T,K],
                    initializer =tf.constant_initializer(1.0 / K)))
qmu = ed.models.Empirical( params= tf.get_variable("qmu/prm",[T,K,d],
                    initializer = tf.zeros_initializer()))
qsigma = ed.models.Empirical(params= tf.get_variable("qsigma/prm", [T,K,d],
                    initializer = tf.ones_initializer()))
qz = ed.models.Empirical( params= tf.get_variable("qz/prm", [T, N],
                    initializer= tf.zeros_initializer(),
                    dtype=tf.int32))

gp = ed.models.Dirichlet(concentration=tf.ones(K))
gmu = ed.models.Normal(loc=tf.ones([K,d]), scale=tf.ones([K,d]))
gsigma = ed.models.InverseGamma(concentration= tf.ones([K,d]), rate=tf.ones([K,d]))
gz = ed.models.Categorical(logits=tf.zeros([N, K]))

inference = ed.MetropolisHastings(
    latent_vars={p: qp, mu: qmu,
                 sigma: qsigma, z: qz},
    proposal_vars={p: gp, mu: gmu,
                   sigma: gsigma, z: gz},
    data={x: x_train})
inference.run()

# print the posterior
print(qmu.params.eval())



######### comp

qmu = ed.models.Empirical(params=tf.get_variable("qmu/prm", [T,K,d],
                                initializer=tf.zeros_initializer()))
gmu = ed.models.Normal(loc=tf.ones([K,d]), scale=tf.ones([K,d]))
