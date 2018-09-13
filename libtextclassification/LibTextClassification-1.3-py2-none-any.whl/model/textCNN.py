# -*- coding: utf-8 -*-

import tensorflow as tf


class TextCNN:
    def __init__(self, filter_sizes, num_filters, vocab_size, learning_rate, decay_steps, decay_rate, sequence_length, embed_size,
                 is_training, initializer=tf.random_normal_initializer(stddev=0.01), clip_gradients=5.0, decay_rate_big=0.50):
        # set hyperparamter
        self.sequence_length = sequence_length
        self.vocab_size = vocab_size
        self.embed_size = embed_size
        self.is_training = is_training
        self.filter_sizes = filter_sizes
        self.num_filters = num_filters
        self.initializer = initializer
        self.num_filters_total = self.num_filters * len(filter_sizes)
        self.clip_gradients = clip_gradients

        self.input_x = tf.placeholder(tf.int32, [None, self.sequence_length], name="input_x")  # X
        self.input_y = tf.placeholder(tf.float32, [None, 1], name="input_y")
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
            "input_y": self.input_y
        }

    def instantiate_weights(self):
        with tf.name_scope("embedding"):
            self.Embedding = tf.get_variable("Embedding", shape=[self.vocab_size, self.embed_size], initializer=self.initializer)
            self.W_projection = tf.get_variable("W_projection", shape=[self.num_filters_total, 1], initializer=self.initializer)
            self.b_projection = tf.get_variable("b_projection", shape=[1], initializer=self.initializer)

    def inference(self):
        self.embedded_words = tf.nn.embedding_lookup(self.Embedding, self.input_x)
        self.sentence_embeddings_expanded = tf.expand_dims(self.embedded_words, -1)
        pooled_outputs = []
        for i, filter_size in enumerate(self.filter_sizes):
            with tf.name_scope("convolution-pooling-%s" % filter_size):
                filter = tf.get_variable("filter-%s" % filter_size, [filter_size, self.embed_size, 1, self.num_filters], initializer=self.initializer)
                conv = tf.nn.conv2d(self.sentence_embeddings_expanded, filter, strides=[1, 1, 1, 1], padding="VALID", name="conv")
                b = tf.get_variable("b-%s" % filter_size, [self.num_filters])
                h = tf.nn.relu(tf.nn.bias_add(conv, b), "relu")
                pooled = tf.nn.max_pool(h, ksize=[1, self.sequence_length - filter_size + 1, 1, 1],
                                        strides=[1, 1, 1, 1], padding='VALID', name="pool")
                pooled_outputs.append(pooled)
        self.h_pool = tf.concat(pooled_outputs, 3)
        self.h_pool_flat = tf.reshape(self.h_pool, [-1, self.num_filters_total])
        with tf.name_scope("dropout"):
            self.h_drop = tf.nn.dropout(self.h_pool_flat, keep_prob=self.dropout_keep_prob)

        with tf.name_scope("output"):
            logits = tf.nn.sigmoid(tf.matmul(self.h_drop, self.W_projection) + self.b_projection)
        return logits

    def loss(self, l2_lambda=0.00001):
        with tf.name_scope("loss"):
            loss = -tf.reduce_mean(tf.reduce_sum(self.input_y * tf.log(self.logits + 1e-10) + (1 - self.input_y) * tf.log(1 - self.logits + 1e-10), axis=1))
            l2_losses = tf.add_n([tf.nn.l2_loss(v) for v in tf.trainable_variables() if 'bias' not in v.name]) * l2_lambda
            loss = loss + l2_losses
        return loss

    def train(self):
        train_op = tf.contrib.layers.optimize_loss(self.loss_val, global_step=self.global_step,
                                                   learning_rate=self.lr, optimizer="Adam", clip_gradients=self.clip_gradients)
        return train_op
