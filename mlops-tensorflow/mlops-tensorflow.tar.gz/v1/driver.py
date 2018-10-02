""" TensorFlow Driver v1 """

import tensorflow as tf

from mlops.core.util import import_module
from mlops.driver.tensorflow.v1.estimator import Estimator
from mlops.driver.tensorflow.v1.util import load_ops, load_config

def run(metadata, params, config, args, **kwargs):
  if 'ops' not in args:
    raise 'mlops.driver.tensorflow: Required arguments is missing: `{}`'.format('ops')
  user_module = import_module(args['ops'])
  ops = load_ops(user_module, params)
  rc, ts, es = load_config(ops, config)
  e = Estimator(ops, rc, params)
  tf.estimator.train_and_evaluate(e, ts, es)
