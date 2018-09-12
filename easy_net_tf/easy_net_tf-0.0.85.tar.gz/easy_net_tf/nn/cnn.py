import numpy
import tensorflow as tf
from easy_net_tf.utility.variable import UtilityVariable


class CNN:
    VALID = 'VALID'
    SAME = 'SAME'

    def __init__(self,
                 batch_input,
                 filter_size,
                 channels_out,
                 stride,
                 add_bias,
                 add_residual=False,
                 normalize=False,
                 padding=SAME,
                 name=''):
        """
        :param batch_input: a batch of feature map
        :param filter_size:
        :param channels_out:
        :param stride:
        :param add_bias: True: add; False: not add
        :param add_residual:
        :param normalize: weight normalize
        :param padding:
        :param name: layer name
        """

        """
        prepare
        """
        if batch_input is None:
            assert 'Error: [%s.%s] batch_image can not be ''None''.' % (CNN.__name__,
                                                                        CNN.__init__.__name__)
        else:
            _, _height_in, _width_in, _channels_in = batch_input.shape
            self.height_in = _height_in.value
            self.width_in = _width_in.value
            self.channels_in = _channels_in.value
            assert self.channels_in is not None, '[%s,%s] ' \
                                                 'the channels of input must be explicit, ' \
                                                 'otherwise filters can not be initialized.' % (CNN.__name__,
                                                                                                CNN.__init__.__name__)

        self.filter_size = filter_size
        self.channels_out = channels_out
        self.stride = stride

        if add_residual \
                and (stride != 1
                     or padding is not CNN.SAME):
            add_residual = False
            print('Error: '
                  '[%s.%s] '
                  'if residual added, '
                  'be sure stride = 1 and padding = %s.%s' % (CNN.__name__,
                                                              CNN.__init__.__name__,
                                                              CNN.__name__,
                                                              CNN.SAME))
        self.add_residual = add_residual
        self.add_bias = add_bias
        self.padding = padding
        self.name = name

        """
        initialize variable
        """
        self.cnn_filter, \
        self.residual_filter, \
        self.cnn_bias = self._initialize_variable(name=name)

        """
        normalize
        """
        if normalize:
            self.cnn_filter = tf.nn.l2_normalize(self.cnn_filter,
                                                 2,
                                                 name='cnn_weight')

        """
        calculation
        """
        self.features = self._calculate(batch_input)

    def _initialize_variable(self, name):
        """
        initialize variable
        :return:
        """

        """
        cnn_filter
        """
        cnn_filter = UtilityVariable.initialize_weight(
            [self.filter_size,
             self.filter_size,
             self.channels_in,
             self.channels_out],
            name='%s_cnn/weight' % name
        )

        """
        cnn_bias
        """
        if self.add_bias:
            cnn_bias = UtilityVariable.initialize_bias(
                [self.channels_out],
                name='%s_cnn/bias' % name
            )
        else:
            cnn_bias = None

        """
        residual_filter
        """
        if self.add_residual and self.channels_in != self.channels_out:
            residual_filter = UtilityVariable.initialize_weight(
                [1,
                 1,
                 self.channels_in,
                 self.channels_out],
                name='%s_cnn/residual' % name
            )
        else:
            residual_filter = None

        return cnn_filter, residual_filter, cnn_bias

    def _calculate(self,
                   batch_input):
        """
        No activation function applied on output.
        :param batch_input:
        :return:
        """

        """
        convolution
        """
        convolution_o = tf.nn.conv2d(input=batch_input,
                                     filter=self.cnn_filter,
                                     strides=[1, self.stride, self.stride, 1],
                                     padding=self.padding)

        """
        residual block
        """
        if self.add_residual is True:
            if self.residual_filter is not None:
                batch_input = tf.nn.conv2d(input=batch_input,
                                           filter=self.residual_filter,
                                           strides=[1, 1, 1, 1],
                                           padding='SAME')

            batch_output = tf.add(convolution_o, batch_input)
        else:
            batch_output = convolution_o

        """
        bias
        """
        if self.cnn_bias is not None:
            batch_output += self.cnn_bias

        return batch_output

    def get_features(self):
        """
        :return:
        """
        return self.features

    def get_variables(self, sess=None, save_dir=None):
        """
        :return:
        """
        if sess is None:
            return self.cnn_filter, \
                   self.residual_filter, \
                   self.cnn_bias

        else:
            convolution_filter = None if self.cnn_filter is None else sess.run(self.cnn_filter)
            residual_filter = None if self.residual_filter is None else sess.run(self.residual_filter)
            bias = None if self.cnn_bias is None else sess.run(self.cnn_bias)

            if save_dir is not None:
                if convolution_filter is not None:
                    shape = '[%d,%d,%d,%d]' % convolution_filter.shape
                    numpy.savetxt(fname='%s/cnn-convolution-%s.txt' % (save_dir, shape),
                                  X=numpy.reshape(convolution_filter, [-1]),
                                  header='%s: convolution filter' % CNN.__name__,
                                  footer='shape: %s' % shape)

                    numpy.save(file='%s/cnn-convolution-%s.npy' % (save_dir, shape),
                               arr=convolution_filter)

                if residual_filter is not None:
                    shape = '[%d,%d,%d,%d]' % residual_filter.shape
                    numpy.savetxt(fname='%s/cnn-residual-%s.txt' % (save_dir, shape),
                                  X=numpy.reshape(residual_filter, [-1]),
                                  header='%s: residual filter' % CNN.__name__,
                                  footer='shape: %s' % shape)

                    numpy.save(file='%s/cnn-residual-%s.npy' % (save_dir, shape),
                               arr=residual_filter)

                if bias is not None:
                    shape = '[%d]' % bias.shape
                    numpy.savetxt(fname='%s/cnn-bias-%s.txt' % (save_dir, shape),
                                  X=bias,
                                  header='%s: bias' % CNN.__name__,
                                  footer='shape: %s' % shape)

                    numpy.save(file='%s/cnn-bias-%s.npy' % (save_dir, shape),
                               arr=bias)

            return convolution_filter, \
                   residual_filter, \
                   bias

    def get_config(self):

        multiplication_convolution, \
        multiplication_residual = self.get_multiplication_amount(height_in=self.height_in,
                                                                 width_in=self.width_in,
                                                                 filter_size=self.filter_size,
                                                                 stride=self.stride,
                                                                 channels_in=self.channels_in,
                                                                 channels_out=self.channels_out,
                                                                 padding=self.padding,
                                                                 add_residual=self.add_residual)

        filter_shape = None if self.cnn_filter is None else self.cnn_filter.shape
        residual_shape = None if self.residual_filter is None else self.residual_filter.shape
        bias_shape = None if self.cnn_bias is None else self.cnn_bias.shape

        config = [
            '\n### %s\n' % self.name,
            '- CNN\n',
            '- filter size: %d\n' % self.filter_size,
            '- channels in: %d\n' % self.channels_in,
            '- channels out: %d\n' % self.channels_out,
            '- stride: %d\n' % self.stride,
            '- add residual: %s\n' % self.add_residual,
            '- add bias: %s\n' % self.add_bias,
            '- padding: %s\n' % self.padding,
            '- variables:\n',
            '   - convolution: %s\n' % filter_shape,
            '   - bias: %s\n' % bias_shape,
            '   - residual: %s\n' % residual_shape,
            '- multiplicative amount: %d\n' % (multiplication_convolution + multiplication_residual),
            '   - convolution: %d\n' % multiplication_convolution,
            '   - residual: %d\n' % multiplication_residual
        ]
        return config

    @staticmethod
    def get_multiplication_amount(height_in,
                                  width_in,
                                  filter_size,
                                  stride,
                                  channels_in,
                                  channels_out,
                                  padding,
                                  add_residual):
        if height_in is None or width_in is None:
            return -1, -1

        else:
            if padding == CNN.SAME:
                height_out = round(height_in / stride)
                width_out = round(width_in / stride)
            elif padding == CNN.VALID:
                height_out = round((height_in - filter_size + 1) / stride)
                width_out = round((width_in - filter_size + 1) / stride)
            else:
                height_out = 0
                width_out = 0
                print('Error: '
                      '[%s.%s] '
                      'wrong padding mode.'
                      % (CNN.__name__,
                         CNN.__init__.__name__))

            convolution = height_out * width_out * filter_size * filter_size * channels_in * channels_out

            if add_residual and channels_in != channels_out:
                residual = height_in * width_out * channels_in * channels_out
            else:
                residual = 0

            return convolution, residual


if __name__ == '__main__':
    from easy_net_tf.utility.file import UtilityFile

    image = numpy.array([[[[1, 1, 1], [1, 1, 1], [1, 1, 1], [1, 1, 1]],
                          [[1, 1, 1], [1, 1, 1], [1, 1, 1], [1, 1, 1]],
                          [[1, 1, 1], [1, 1, 1], [1, 1, 1], [1, 1, 1]],
                          [[1, 1, 1], [1, 1, 1], [1, 1, 1], [1, 1, 1]],
                          [[1, 1, 1], [1, 1, 1], [1, 1, 1], [1, 1, 1]]]],
                        dtype=numpy.float32)

    image_ph = tf.placeholder(dtype=tf.float32, shape=[None, None, None, 3])

    cnn = CNN(batch_input=image_ph,
              filter_size=2,
              channels_out=6,
              stride=1,
              add_bias=True,
              add_residual=True,
              normalize=True,
              padding=CNN.SAME,
              name='l1')

    cnn.get_features()

    UtilityFile.save_str_list('test-cnn.md', cnn.get_config())

    weight_op = tf.constant([[[[1, 1],
                               [2, 1],
                               [3, 1]],
                              [[3, 3],
                               [4, 2],
                               [3, 1]]
                              ],
                             [[[3, 1],
                               [2, 2],
                               [3, 1]],
                              [[3, 3],
                               [4, 2],
                               [3, 1]]
                              ]
                             ],
                            dtype=tf.float32)

    weight_op = tf.nn.l2_normalize(weight_op, 2)

    tem_op = tf.constant(
        [[1, 1, 1],
         [1, 2, 3],
         [2, 2, 2],
         [3, 3, 3]],
        dtype=tf.float32
    )
    tem_op = tf.nn.l2_normalize(tem_op, 1)

    with tf.Session() as sess:
        weight_final = sess.run(weight_op)
        tem_final = sess.run(tem_op)
        print(weight_final)
