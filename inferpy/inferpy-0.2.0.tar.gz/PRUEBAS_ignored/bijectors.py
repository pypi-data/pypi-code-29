import edward as ed

import tensorflow as tf

import tensorflow.contrib.distributions as ds

import inferpy as inf


[c.__name__ for c in tf.contrib.distributions.Distribution.__subclasses__()]

getattr(tf.contrib.distributions, "PointMass")
getattr(getattr(ed.models, "PointMass"), "__init__")(params=1.)


d = inf.models.PointMass(params=1.)

d.base_object