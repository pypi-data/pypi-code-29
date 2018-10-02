""" TensorFlow Estimator Base """

import importlib
import tensorflow as tf

def build_model_fn(ops):
  def model_fn(features, labels, mode, params):
    training = mode == tf.estimator.ModeKeys.TRAIN
    predictions = ops.model(features, training, params)

    if mode == tf.estimator.ModeKeys.PREDICT:
      return tf.estimator.EstimatorSpec(
        mode=tf.estimator.ModeKeys.PREDICT,
        predictions=predictions,
        export_outputs=None) #TODO: support export_outputs

    with tf.variable_scope('losses'):
      losses = ops.losses(predictions, labels, params)
      total_loss = tf.losses.get_total_loss()
    with tf.variable_scope('metrics'):
      metric_ops = ops.evaluate(predictions, labels, params)

    #TODO: add summary

    if mode == tf.estimator.ModeKeys.EVAL:
      return tf.estimator.EstimatorSpec(
        mode=tf.estimator.ModeKeys.EVAL,
        loss=total_loss,
        eval_metric_ops=metric_ops)

    global_step = tf.train.get_or_create_global_step()
    update_ops = tf.get_collection(tf.GraphKeys.UPDATE_OPS)
    with tf.variable_scope('optimizer'):
      with tf.control_dependencies(update_ops):
        train_op = ops.train(total_loss, global_step, params)

    if mode == tf.estimator.ModeKeys.TRAIN:
      return tf.estimator.EstimatorSpec(
        mode=tf.estimator.ModeKeys.TRAIN,
        loss=total_loss,
        train_op=train_op)
  return model_fn

class Estimator(tf.estimator.Estimator):
  def __init__(self, ops, config, params):
    #TODO: check to have module some methods.
    super(Estimator, self).__init__(
      model_fn=build_model_fn(ops), config=config, params=params)
