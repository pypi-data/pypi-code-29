
import edward as ed
import inferpy as inf
import numpy as np
import tensorflow as tf
import random



K, d, N = 3, 4, 10
x_train = inf.models.Normal(loc=10, scale=100, dim=d).sample(N)

T=100

# MODEL
p2 = ed.models.Dirichlet(concentration=tf.ones(K)/K)
mu2 = ed.models.Normal(0.0, 1.0, sample_shape=[K, d])
sigma2 = ed.models.InverseGamma(concentration=1.0, rate=1.0,
                     sample_shape=[K, d])
z2 = ed.models.Categorical(logits=tf.log(p2) - tf.log(1.0 - p2), sample_shape=N)
z2 = ed.models.Categorical(probs=p2+1e-5, sample_shape=N)
x2 = ed.models.Normal(loc=tf.gather(mu2, z2), scale=tf.gather(sigma2, z2))



id = str(random.randint(0,100000))

def checknan(t):
    return tf.where(tf.is_nan(t), tf.zeros_like(t), t)
    #return t

# INFERENCE
qp_dist = ed.models.Dirichlet(concentration=checknan(tf.get_variable(
    "qp/params" + id,
    [K],
    initializer=tf.constant_initializer(1.0 / K))),allow_nan_stats=False)
qmu_dist = ed.models.Normal(loc=tf.get_variable("qmu/loc" + id,
                                       [K, d],
                                       initializer=tf.zeros_initializer()),
                       scale=tf.get_variable("qmu/scale" + id,
                                           [K, d],
                                           initializer=tf.zeros_initializer()),allow_nan_stats=False)
qsigma_dist = ed.models.InverseGamma(concentration=tf.get_variable("qsigma/conc"+id,
                                          [K,d],
                                          initializer=tf.ones_initializer()),
                                rate=tf.get_variable("qsigma/rate" + id,
                                                              sigma2.rate.shape,
                                                              initializer=tf.ones_initializer()),allow_nan_stats=False)
qz_dist = ed.models.Categorical(logits=
                                checknan(
                                           tf.get_variable("qz/params"+id,
                                      z2.logits.shape,
                                      #initializer=tf.constant([0.2, 0.2, 0.6]),
                                      initializer=tf.zeros_initializer(),
                                      dtype=tf.float32),
                                ),
    sample_shape=N, allow_nan_stats=False)


# en algún momento prob toma el valor nan y muestrea 3

#sess = ed.get_session()
#sess.run(tf.get_default_graph().get_operation_by_name("qz/params" + id))
#qz_dist.logits.eval()
# Tras inicializar la variable siempre muestrea el 3



latent_vars = {z2: qz_dist,
 p2: qp_dist,
 sigma2: qsigma_dist,
 mu2: qmu_dist}

#ed.KLpq(latent_vars=latent_vars, data={x2:x_train}).run()
ed.Laplace(latent_vars=latent_vars, data={x2:x_train}).run()


qz_dist.probs.eval()
qp_dist.concentration.eval()


[v.shape for v in latent_vars.keys()]
[v.shape for v in latent_vars.values()]

