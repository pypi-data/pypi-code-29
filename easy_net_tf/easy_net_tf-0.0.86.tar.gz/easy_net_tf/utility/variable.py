import tensorflow as tf


class UtilityVariable:

    @staticmethod
    def initialize_weight(shape, name=''):
        kernel = tf.truncated_normal(shape, stddev=0.1)
        return tf.Variable(kernel, name=name)

    @staticmethod
    def initialize_bias(shape, name=''):
        initial = tf.constant(0.1, shape=shape)
        return tf.Variable(initial, name=name)
