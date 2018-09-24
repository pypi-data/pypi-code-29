# coding: utf-8

import importlib
import tensorflow as tf
import tensorflow_hub as tfhub

def hub_module_wrapper(module_fn):
  def _wrapper(*args, **kwargs):
    for key, spec in six.iteritems(module_fn(*args, **kwargs)):
      tfhub.add_signature(name=key, inputs=spec['inputs'], outputs=['outputs'])
  return _wrapper

def build_model_fn(module):
  def model_fn(features, labels, mode, params):
    training = mode == tf.estimator.ModeKeys.TRAIN
    predictions = module.model(features, training, params)

    if mode == tf.estimator.ModeKeys.PREDICT:
      if 'export_outputs' in module:
        export_outputs = module.export_outputs(predictions)
      else:
        export_outputs = {
          tf.saved_model.signature_constants.
          DEFAULT_SERVING_SIGNATURE_DEF_KEY:
            tf.estimator.export.PredictOutput(predictions),
        }
      return tf.estimator.EstimatorSpec(
        mode=tf.estimator.ModeKeys.PREDICT,
        predictions=predictions,
        export_outputs=export_outputs)

    with tf.variable_scope('losses'):
      losses = module.losses(labels, predictions, params)
      total_loss = tf.losses.get_total_loss()
    with tf.variable_scope('metrics'):
      metric_ops = module.evaluate(labels, predictions, params)

    if mode == tf.estimator.ModeKeys.EVAL:
      return tf.estimator.EstimatorSpec(
        mode=tf.estimator.ModeKeys.EVAL,
        loss=total_loss,
        eval_metric_ops=metric_ops)

    global_step = tf.train.get_or_create_global_step()
    update_ops = tf.get_collection(tf.GraphKeys.UPDATE_OPS)
    with tf.variable_scope('optimizer'):
      with tf.control_dependencies(update_ops):
        train_op = module.train(total_loss, global_step, params)

    if mode == tf.estimator.ModeKeys.TRAIN:
      return tf.estimator.EstimatorSpec(
        mode=tf.estimator.ModeKeys.TRAIN,
        loss=total_loss,
        train_op=train_op)
  return model_fn

class Estimator(tf.estimator.Estimator):
  def __init__(self, module, config, params):
    #TODO: check to have module some methods.
    super(Estimator, self).__init__(
      model_fn=build_model_fn(module), config=config, params=params)
