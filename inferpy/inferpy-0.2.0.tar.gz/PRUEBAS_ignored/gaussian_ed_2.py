
import edward as ed
import inferpy as inf
import numpy as np
import tensorflow as tf
import random



K, d, N, T = 3, 4, 1000, 5000
x_train = inf.models.Normal(loc=10, scale=100, dim=d).sample(N)


# MODEL
p = ed.models.Dirichlet(concentration=tf.ones(K)/K)
mu = ed.models.Normal(0.0, 1.0, sample_shape=[K, d])
sigma = ed.models.InverseGamma(concentration=1.0, rate=1.0,
                     sample_shape=[K, d])
z = ed.models.Categorical(logits=tf.log(p) - tf.log(1.0 - p), sample_shape=N)
x = ed.models.Normal(loc=tf.gather(mu, z), scale=tf.gather(sigma, z))


# INFERENCE
qp = ed.models.Empirical(params=tf.get_variable(
    "qp/params",
    [T, K],
    initializer=tf.constant_initializer(1.0 / K)))
qmu = ed.models.Empirical(params=tf.get_variable("qmu/params",
                                       [T, K, d],
                                       initializer=tf.zeros_initializer()))
qsigma = ed.models.Empirical(params=tf.get_variable("qsigma/params",
                                          [T, K, d],
                                          initializer=tf.ones_initializer()))
qz = ed.models.Empirical(params=tf.get_variable("qz/params",
                                      [T, N],
                                      initializer=tf.zeros_initializer(),
                                      dtype=tf.int32))


gp = ed.models.Dirichlet(concentration=tf.ones(K))
gmu = ed.models.Normal(loc=tf.ones([K,d]),
             scale=tf.ones([K,d]))
gsigma = ed.models.InverseGamma(concentration=tf.ones([K,d]),
                      rate=tf.ones([K,d]))
gz = ed.models.Categorical(logits=tf.zeros([N, K]))



inference = ed.MetropolisHastings(
    latent_vars={p: qp, mu: qmu, sigma: qsigma, z: qz},
    proposal_vars={p: gp, mu: gmu, sigma: gsigma, z: gz},
    data={x: x_train})

inference.run()


print(qmu.params.eval())