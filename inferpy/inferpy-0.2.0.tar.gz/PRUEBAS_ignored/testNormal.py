import edward as ed
import tensorflow as tf
import inferpy as inf
import numpy as np

N=10

with inf.ProbModel() as m:
    mu = inf.models.Normal(loc=0.0, scale=1.0, dim=3)

    v = inf.models.Categorical(probs=[0.1,0.8])
    y = inf.models.Multinomial(total_count=2,logits=[0,0])

    with inf.replicate(size=N):
        x = inf.models.Normal(loc=mu, scale=1.0, observed=True, dim=3)



y.event_shape

y.shape

mu.shape



inf.matmul(x,mu, transpose_b=True)
inf.dot(x,mu)


mu2 = np.array([1.,1.,1.], dtype="float32").reshape((3,1))

inf.matmul(x,mu2, transpose_b=False)

inf.matmul(x,tf.constant(mu2), transpose_b=False)

inf.matmul(x,mu2.tolist(), transpose_b=False)


mu3 = np.array([1.,1.,1.], dtype="float32")

inf.dot(x,mu3)
inf.dot(x,tf.constant(mu3))
inf.dot(x,mu3.tolist())


np.shape(mu3.tolist())


tf.matmul(x.dist, mu2, transpose_b=True)


inf.dot(x,mu2)

mu2.shape

mu2.shape

