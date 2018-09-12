import tensorflow as tf


class AveragePooling(object):
    def __init__(self, *args, **kwargs):
        try:
            self.vocab_size = kwargs.get('vocab_size', 10000)
            self.class_num = kwargs.get('class_num', 2)
            self.embed_size = kwargs.get('embed_size', 128)
            self.sequence_length = kwargs.get('sequence_length', 100)
            self.is_training = kwargs.get('is_training', True)
            self.learning_rate = kwargs.get('learning_rate', 0.01)
            self.decay_steps = kwargs.get('decay_steps', 1)
            self.decay_rate = kwargs.get('decay_rate', 1.0)
        except Exception:
            print("Model AveragePooling acquires 'vocab_size', 'class_num', 'embed_size', 'sequence_length', 'is_training'")

        self.initializer = tf.random_normal_initializer(stddev=0.01)
        self.clip_gradients = 5.0
        # self.count = 0
        # add placeholder (X,label)
        self.input_x = tf.placeholder(tf.int32, [None, self.sequence_length], name="input_x")  # X
        self.input_length = tf.placeholder(tf.float32, [None, 1], name="input_length")  # X
        self.input_y = tf.placeholder(tf.float32, [None, self.class_num], name="input_y")
        # self.actual = tf.placeholder(tf.float32, [None, 1], name="actual")
        self.dropout_keep_prob = tf.placeholder(tf.float32, name="dropout_keep_prob")

        # self.pred = tf.placeholder(tf.int32, [None, 1], name="pred")  # X

        self.global_step = tf.Variable(0, trainable=False, name="Global_Step")
        self.epoch_step = tf.Variable(0, trainable=False, name="Epoch_Step")
        self.epoch_increment = tf.assign(self.epoch_step, tf.add(self.epoch_step, tf.constant(1)))

        self.init_weights()
        self.logits = self.inference()
        if not self.is_training:
            return
        self.loss_val = self.loss()
        self.lr = self.learning_rate
        self.lr_decay = tf.train.exponential_decay(
            self.learning_rate, self.epoch_step, self.decay_steps, self.decay_rate, staircase=False)
        self.train_op = self.train()

    def get_train_placeholders(self):
        return {
            "input_x": self.input_x,
            "input_length": self.input_length,
            "input_y": self.input_y
        }

    def get_predict_placeholders(self):
        return {
            "input_x": self.input_x,
            "input_length": self.input_length
        }

    def init_weights(self):
        with tf.name_scope("embedding"):
            self.Embedding = tf.get_variable("Embedding", shape=[
                                             self.vocab_size, self.embed_size], initializer=self.initializer)
            self.W_projection = tf.get_variable("W_projection", shape=[self.embed_size,
                                                                       self.class_num], initializer=self.initializer)
            self.b_projection = tf.get_variable(
                "b_projection", shape=[self.class_num], initializer=self.initializer)


    def inference(self):
        embedded_words = tf.nn.embedding_lookup(self.Embedding, self.input_x)

        average = tf.div(tf.reduce_sum(embedded_words, axis=1), self.input_length)
        # embedded_words = tf.expand_dims(embedded_words, -1)
        # max = tf.reshape(tf.nn.max_pool(embedded_words, ksize=[1, self.sequence_length, 1, 1],
        #                      strides=[1, 1, 1, 1], padding='VALID', name="maxpool"), [-1, self.embed_size])
        with tf.name_scope("dropout"):
            # h = tf.nn.dropout(tf.concat([average, max], 1), keep_prob=self.dropout_keep_prob)
            h = tf.nn.dropout(average, keep_prob=self.dropout_keep_prob)
        logits = tf.nn.sigmoid(tf.matmul(h, self.W_projection) + self.b_projection)
        return logits

    def loss(self, l2_lambda=0.00001):
        with tf.name_scope("loss"):
            # losses = tf.nn.sigmoid_cross_entropy_with_logits(labels=self.input_y, logits=self.logits)
            # losses = tf.reduce_sum(losses, axis=1)  # shape=(?,). loss for all data in the batch
            # print("Use sigmoid_cross_entropy_with_logits.")
            # losses = tf.nn.softmax_cross_entropy_with_logits(labels=self.input_y, logits=self.logits)
            # print("Use softmax_cross_entropy_with_logits.")
            # loss = tf.reduce_mean(losses)  # shape=().   average loss in the batch
            loss = -tf.reduce_mean(tf.reduce_sum(self.input_y * tf.log(self.logits + 1e-10) +
                                                 (1 - self.input_y) * tf.log(1 - self.logits + 1e-10), axis=1))
            l2_losses = tf.add_n([tf.nn.l2_loss(v) for v in tf.trainable_variables() if 'bias' not in v.name]) * l2_lambda
            loss = loss + l2_losses
            # self.count += 1
        return loss

    def train(self):
        """based on the loss, use SGD to update parameter"""
        train_op = tf.contrib.layers.optimize_loss(self.loss_val, global_step=self.global_step,
                                                   learning_rate=self.lr, optimizer="Adam", clip_gradients=self.clip_gradients)
        return train_op
