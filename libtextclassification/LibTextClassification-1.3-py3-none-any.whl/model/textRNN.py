# -*- coding: utf-8 -*-
import tensorflow as tf
from tensorflow.contrib import rnn


class TextRNN:
    def __init__(self, vocab_size, learning_rate, decay_steps, decay_rate, embed_size, sequence_length,
                 is_training, initializer=tf.random_normal_initializer(stddev=0.01), clip_gradients=5.0, decay_rate_big=0.50):

        # set hyperparamter
        self.sequence_length = sequence_length
        self.vocab_size = vocab_size
        self.embed_size = embed_size
        self.hidden_size = embed_size
        self.is_training = is_training
        self.initializer = initializer
        self.clip_gradients = clip_gradients

        # add placeholder (X,label)
        self.input_x = tf.placeholder(tf.int32, [None, self.sequence_length], name="input_x")  # X
        self.input_length = tf.placeholder(tf.int32, [None], name="input_length")  # X
        self.input_y = tf.placeholder(tf.float32, [None, 1], name="input_y")  # y [None,num_classes]
        self.dropout_keep_prob = tf.placeholder(tf.float32, name="dropout_keep_prob")

        self.global_step = tf.Variable(0, trainable=False, name="Global_Step")
        self.epoch_step = tf.Variable(0, trainable=False, name="Epoch_Step")
        self.epoch_increment = tf.assign(self.epoch_step, tf.add(self.epoch_step, tf.constant(1)))
        self.decay_steps, self.decay_rate = decay_steps, decay_rate

        self.instantiate_weights()
        self.logits = self.inference()
        if not is_training:
            return
        self.lr = learning_rate
        self.lr_decay = tf.train.exponential_decay(learning_rate, self.epoch_step, self.decay_steps, self.decay_rate, staircase=False)
        self.loss_val = self.loss()
        self.train_op = self.train()

    def get_placeholders(self):
        return {
            "input_x": self.input_x,
            "input_length": self.input_length,
            "input_y": self.input_y
        }

    def instantiate_weights(self):
        with tf.name_scope("embedding"):
            self.Embedding = tf.get_variable("Embedding", shape=[self.vocab_size, self.embed_size], initializer=self.initializer)
            self.W_projection = tf.get_variable("W_projection", shape=[self.hidden_size * 2,
                                                                       1], initializer=self.initializer)
            self.b_projection = tf.get_variable("b_projection", shape=[1], initializer=self.initializer)

    def inference(self):
        self.embedded_words = tf.nn.embedding_lookup(self.Embedding, self.input_x)
        lstm_fw_cell = rnn.BasicLSTMCell(self.hidden_size)
        lstm_bw_cell = rnn.BasicLSTMCell(self.hidden_size)
        if self.dropout_keep_prob is not None:
            lstm_fw_cell = rnn.DropoutWrapper(lstm_fw_cell, output_keep_prob=self.dropout_keep_prob)
            lstm_bw_cell = rnn.DropoutWrapper(lstm_bw_cell, output_keep_prob=self.dropout_keep_prob)
        outputs, _ = tf.nn.bidirectional_dynamic_rnn(lstm_fw_cell, lstm_bw_cell, self.embedded_words,
                                                     sequence_length=self.input_length, dtype=tf.float32)
        output_rnn = tf.concat(outputs, axis=2)
        self.output_rnn_last = tf.reduce_mean(output_rnn, axis=1)
        with tf.name_scope("output"):
            logits = tf.nn.sigmoid(tf.matmul(self.output_rnn_last, self.W_projection) + self.b_projection)
        return logits

    def loss(self, l2_lambda=0.00001):
        with tf.name_scope("loss"):
            loss = -tf.reduce_mean(tf.reduce_sum(self.input_y * tf.log(self.logits + 1e-10) +
                                                 (1 - self.input_y) * tf.log(1 - self.logits + 1e-10), axis=1))
            l2_losses = tf.add_n([tf.nn.l2_loss(v) for v in tf.trainable_variables() if 'bias' not in v.name]) * l2_lambda
            loss = loss + l2_losses
        return loss

    def train(self):
        train_op = tf.contrib.layers.optimize_loss(self.loss_val, learning_rate=self.lr,
                                                   global_step=self.global_step, optimizer="Adam", clip_gradients=self.clip_gradients)
        return train_op
