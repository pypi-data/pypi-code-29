#!/usr/bin/env python
# vim: set fileencoding=utf-8 :
# @author: Pavle Korshunov <pavel.korshunov@idiap.ch>
# @date: Fri 15 Sep 2017 13:22 CEST

"""Run training on the data saved as a Tensorflow TFRecords file.

Usage:
  %(prog)s [-v...] [options] [--] <tfrecord_files>...
  %(prog)s --help
  %(prog)s --version

Arguments:
  <tfrecord_files>  The tfrecord files with training and validaiton data.

Options:
  -h --help                         Show this help message and exit
  --version                         Show version and exit
  -v, --verbose                     Increases the output verbosity level
  -c, --classes INT                 Number of classes (labels) to test
                                    [default: 2].
  -f, --feature-size INT            Length of the feature vector.
                                    [default: 102].
  -t, --time-steps INT              Number of time steps, i.e., the size of temporal dimension of the input data.
                                    [default: 20].
  -w, --sliding-window-length INT   Length of the sliding window on temporal dimension.
                                    [default: 10].
  -s, --sliding-window-step INT     Shifting step of the sliding window.
                                    [default: 2].
  -b, --train-batch-size INT        The size of the training batch that will be fed in LSTM.
                                    [default: 8].
  -e, --validation-batch-size INT   The size of the validation batch.
                                    [default: 8].
  -i, --training-iterations INT     The number of iterations in the training.
                                    [default: 1000].
  -r, --random-seed INT             The seed used to initialized random number generator.
                                    [default: 10].
  -o, --output-directory STR        The path to output directory.
                                    [default: './temp/lstm'].
  -z, --network-size INT            The internal size parameter of the network, i.e., for LSTM it is
                                    the cell size and for MLP it is the size of the hidden layer.
                                    [default: 64].

  -a, --architecture GROUP...       Specify network architecture or trainer.
                                    It can be one of ('lstm', '2lstm', '3lstm', 'mlp', 'simplecnn', 'lightcnn').
                                    [default: lstm].

  -g, --regularization-param FLOAT  Network regularization parameter. No regularization by default.
                                    [default: 0.0].

  -d, --dropout-param FLOAT         Network dropout parameter (the same for both input and output).
                                    No dropout by default.
                                    [default: 0.0].
"""

from bob.learn.tensorflow.datashuffler import TFRecordSequence
from bob.learn.tensorflow.loss import MeanSoftMaxLoss
from bob.learn.tensorflow.trainers import Trainer, constant
import tensorflow as tf

import bob.core

logger = bob.core.log.setup("bob.project.savi")

slim = tf.contrib.slim


def main(argv=None):
    from docopt import docopt
    import os
    import sys
    print(sys.argv)
    prog = os.path.basename(sys.argv[0])
    args = docopt(__doc__ % {'prog': prog}, argv=argv, version='0.0.1')
    print(args)
    tfrecord_files = args['<tfrecord_files>']
    num_classes = int(args['--classes'])
    feature_size = int(args['--feature-size'])
    num_time_steps = int(args['--time-steps'])
    sliding_win_len = int(args['--sliding-window-length'])
    sliding_win_step = int(args['--sliding-window-step'])
    input_shape = [None, num_time_steps, feature_size, 1]
    batch_size = int(args['--train-batch-size'])
    validation_batch_size = int(args['--validation-batch-size'])
    iterations = int(args['--training-iterations'])
    seed = int(args['--random-seed'])
    directory = args['--output-directory']
    network_size = int(args['--network-size'])
    architecture = args['--architecture']
    regularizer = float(args['--regularization-param'])
    dropout = float(args['--dropout-param'])

    # Sets-up logging
    verbosity = int(args['--verbose'])
    bob.core.log.set_verbosity_level(logger, verbosity)

    # Creating the tf record
    tfrecords_filename = tfrecord_files[0]
    filename_queue = tf.train.string_input_producer([tfrecords_filename], num_epochs=5000, name="input")

    if len(tfrecord_files) > 1:
        tfrecords_filename_val = tfrecord_files[1]
        filename_queue_val = tf.train.string_input_producer([tfrecords_filename_val], num_epochs=4000,
                                                            name="input_validation")
    # import ipdb; ipdb.set_trace()
    # Creating TFRecord
    train_data_shuffler = TFRecordSequence(filename_queue=filename_queue,
                                           input_shape=input_shape,
                                           batch_size=batch_size,
                                           prefetch_threads=4,
                                           prefetch_capacity=3000,
                                           sliding_win_len=sliding_win_len,
                                           sliding_win_step=sliding_win_step,
                                           min_after_dequeue=200)

    validation_data_shuffler = None
    if len(tfrecord_files) > 1:
        validation_data_shuffler = TFRecordSequence(filename_queue=filename_queue_val,
                                                    input_shape=input_shape,
                                                    batch_size=validation_batch_size,
                                                    prefetch_threads=4,
                                                    prefetch_capacity=3000,
                                                    sliding_win_len=sliding_win_len,
                                                    sliding_win_step=sliding_win_step,
                                                    min_after_dequeue=200)

    num_sliding_wins = (num_time_steps - sliding_win_len) // sliding_win_step + 1
    # after we generate sliding windows, the num_time_steps is the same as sliding windwos length
    num_time_steps = sliding_win_len

    graph = None
    validation_graph = None
    if architecture == '2lstm':
        from bob.learn.tensorflow.network import double_lstm_network
        is_dropout = False
        if dropout > 0.0:
            is_dropout = True
        graph = double_lstm_network(train_data_shuffler,
                                    batch_size=num_sliding_wins * batch_size,
                                    lstm_cell_size=network_size,
                                    num_time_steps=num_time_steps,
                                    seed=seed,
                                    num_classes=num_classes,
                                    dropout=is_dropout,
                                    input_dropout=dropout,
                                    output_dropout=dropout)
        if validation_data_shuffler:
            validation_graph = double_lstm_network(validation_data_shuffler,
                                                   batch_size=num_sliding_wins * validation_batch_size,
                                                   num_time_steps=num_time_steps,
                                                   lstm_cell_size=network_size,
                                                   seed=seed,
                                                   num_classes=num_classes,
                                                   reuse=True)
    elif architecture == '3lstm':
        from bob.learn.tensorflow.network import triple_lstm_network
        is_dropout = False
        if dropout > 0.0:
            is_dropout = True
        graph = triple_lstm_network(train_data_shuffler,
                                    batch_size=num_sliding_wins * batch_size,
                                    lstm_cell_size=network_size,
                                    num_time_steps=num_time_steps,
                                    seed=seed,
                                    num_classes=num_classes,
                                    dropout=is_dropout,
                                    input_dropout=dropout,
                                    output_dropout=dropout)
        if validation_data_shuffler:
            validation_graph = triple_lstm_network(validation_data_shuffler,
                                                   batch_size=num_sliding_wins * validation_batch_size,
                                                   num_time_steps=num_time_steps,
                                                   lstm_cell_size=network_size,
                                                   seed=seed,
                                                   num_classes=num_classes,
                                                   reuse=True)
    elif architecture == 'lstm':
        from bob.learn.tensorflow.network import simple_lstm_network
        is_dropout = False
        if dropout > 0.0:
            is_dropout = True
        graph = simple_lstm_network(train_data_shuffler,
                                    batch_size=num_sliding_wins * batch_size,
                                    lstm_cell_size=network_size,
                                    num_time_steps=num_time_steps,
                                    seed=seed,
                                    num_classes=num_classes,
                                    dropout=is_dropout,
                                    input_dropout=dropout,
                                    output_dropout=dropout)
        if validation_data_shuffler:
            validation_graph = simple_lstm_network(validation_data_shuffler,
                                                   batch_size=num_sliding_wins * validation_batch_size,
                                                   num_time_steps=num_time_steps,
                                                   lstm_cell_size=network_size,
                                                   seed=seed,
                                                   num_classes=num_classes,
                                                   reuse=True)
    elif architecture == 'mlp':
        from bob.learn.tensorflow.network import mlp_network
        graph = mlp_network(train_data_shuffler,
                            hidden_layer_size=network_size,
                            num_time_steps=num_time_steps,
                            seed=seed,
                            num_classes=num_classes)
        if validation_data_shuffler:
            validation_graph = mlp_network(validation_data_shuffler,
                                           hidden_layer_size=network_size,
                                           num_time_steps=num_time_steps,
                                           seed=seed,
                                           num_classes=num_classes,
                                           reuse=True)
    elif architecture == 'simplecnn':
        from bob.learn.tensorflow.network import simple2Dcnn_network
        graph = simple2Dcnn_network(train_data_shuffler,
                                    seed=seed,
                                    num_classes=num_classes)
        if validation_data_shuffler:
            validation_graph = simple2Dcnn_network(validation_data_shuffler,
                                                   seed=seed,
                                                   num_classes=num_classes,
                                                   reuse=True)
    elif architecture == 'lightcnn':
        from bob.learn.tensorflow.network import LightCNN9
        net = LightCNN9(n_classes=num_classes, device="/cpu:0")
        input_pl = train_data_shuffler("data", from_queue=True)
        graph = net(input_pl)
        if validation_data_shuffler:
            valid_input_pl = validation_data_shuffler("data", from_queue=True)
            validation_graph = net(valid_input_pl, reuse=True)

    # Which loss function to use
    if regularizer > 0.0:
        from bob.learn.tensorflow.network import RegularizedLoss
        loss = RegularizedLoss(regularizing_coeff=regularizer)
    else:
        loss = MeanSoftMaxLoss()

    # One graph trainer
    trainer = Trainer(train_data_shuffler,
                      validation_data_shuffler=validation_data_shuffler,
                      iterations=iterations,  # It is supper fast
                      analizer=None,
                      snapshot=1000,
                      validation_snapshot=100,
                      temp_dir=directory)

    learning_rate = constant(0.001, name="regular_lr")

    trainer.create_network_from_scratch(graph=graph,
                                        validation_graph=validation_graph,
                                        loss=loss,
                                        learning_rate=learning_rate,
                                        optimizer=tf.train.AdamOptimizer(learning_rate),
                                        )

    trainer.train()


if __name__ == '__main__':
    main()
