import numpy
import tensorflow as tf
from easy_net_tf.utility.variable import UtilityVariable


class FCN:
    def __init__(self,
                 batch_input,
                 nodes_out,
                 add_bias=True,
                 normalize=False,
                 name=''):

        """

        :param batch_input: a Tensor [?, nodes_in]
        :param nodes_out: output nodes number
        :param add_bias:
        :param normalize:
        :param name: layer name
        """

        if batch_input is None:
            assert 'Error: [%s.%s] batch_image can not be ''None''.' % (FCN.__name__,
                                                                        FCN.__init__.__name__)
        else:
            _, _nodes_in = batch_input.shape
            self.nodes_in = _nodes_in.value
            assert self.nodes_in is not None, '[%s,%s] ' \
                                              'the dimension of input must be explicit, ' \
                                              'otherwise filters can not be initialized.' % (FCN.__name__,
                                                                                             FCN.__init__.__name__)

        self.nodes_out = nodes_out
        self.name = name

        """
        initialize variable
        """
        self.weight, \
        self.bias = self._initialize_variable(
            add_bias=add_bias,
            name=name
        )

        """
        normalize variable
        """
        if normalize:
            self.weight = tf.nn.l2_normalize(self.weight,
                                             0,
                                             name='fcn_weight')

        """
        calculate
        """
        self.features = self._calculate(batch_input=batch_input)

    def _initialize_variable(self, add_bias, name=''):
        """

        :param name:
        :return:
        """
        weight = UtilityVariable.initialize_weight(
            [self.nodes_in,
             self.nodes_out],
            name='%s_fcn/weight' % name
        )

        bias = UtilityVariable.initialize_bias(
            [self.nodes_out],
            name='%s_fcn/bias' % name
        ) if add_bias else None

        return weight, bias

    def _calculate(self,
                   batch_input):
        """

        :param batch_input:
        :return: features
        """

        if self.bias is None:
            batch_output = tf.matmul(batch_input, self.weight)
        else:
            batch_output = tf.matmul(batch_input, self.weight) + self.bias

        return batch_output

    def get_features(self):
        """

        :return: features
        """
        return self.features

    def get_variables(self, sess=None, save_dir=None):
        """

        :return: weight, bias
        """

        if sess is None:
            return self.weight, self.bias
        else:
            weight = None if self.weight is None else sess.run(self.weight)
            bias = None if self.bias is None else sess.run(self.bias)

            if save_dir is not None:
                if weight is not None:
                    shape = '[%d,%d]' % weight.shape
                    numpy.savetxt(fname='%s/fcn-weight-%s.txt' % (save_dir, shape),
                                  X=weight,
                                  header='%s: weight' % FCN.__name__,
                                  footer='shape: %s' % shape)

                    numpy.save(file='%s/fcn-weight-%s.npy' % (save_dir, shape),
                               arr=weight)

                if bias is not None:
                    shape = '[%d]' % bias.shape
                    numpy.savetxt(fname='%s/fcn-bias-%s.txt' % (save_dir, shape),
                                  X=bias,
                                  header='%s: bias' % FCN.__name__,
                                  footer='shape: %s' % shape)

                    numpy.save(file='%s/fcn-bias-%s.npy' % (save_dir, shape),
                               arr=bias)

            return weight, bias

    def get_config(self):
        """
        export config as a list
        :return:
        """

        weight_shape = None if self.weight is None else self.weight.shape
        bias_shape = None if self.bias is None else self.bias.shape

        config = [
            '\n### %s\n' % self.name,
            '- Fully Connect Net\n',
            '- nodes in: %d\n' % self.nodes_in,
            '- nodes out: %d\n' % self.nodes_out,
            '- variables:\n',
            '   - weight: %s\n' % weight_shape,
            '   - bias: %s\n' % bias_shape,
            '- multiplicative amount: %d\n' % (self.nodes_in * self.nodes_out)
        ]
        return config


if __name__ == '__main__':
    from easy_net_tf.utility.file import UtilityFile
    from pathlib import Path

    image = numpy.array([[[[1, 1, 1], [1, 1, 1], [1, 1, 1], [1, 1, 1]],
                          [[1, 1, 1], [1, 1, 1], [1, 1, 1], [1, 1, 1]],
                          [[1, 1, 1], [1, 1, 1], [1, 1, 1], [1, 1, 1]],
                          [[1, 1, 1], [1, 1, 1], [1, 1, 1], [1, 1, 1]],
                          [[1, 1, 1], [1, 1, 1], [1, 1, 1], [1, 1, 1]]]],
                        dtype=numpy.float32)

    image_ph = tf.placeholder(dtype=tf.float32, shape=[None, 60])

    fcn = FCN(batch_input=image_ph,
              nodes_out=30,
              add_bias=False,
              normalize=False,
              name='test')

    UtilityFile.save_str_list('test-fcn.md', fcn.get_config())
