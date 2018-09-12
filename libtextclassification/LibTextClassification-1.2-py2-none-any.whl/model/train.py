# -*- coding: utf-8 -*-
import tensorflow as tf
import numpy as np
# from model import model
from gensim.models import KeyedVectors
from os import path
import time


class Trainer(object):
    def __init__(self, epoch_num=10, batch_size=256):
        self.epoch_num = epoch_num
        self.batch_size = batch_size

        config = tf.ConfigProto()
        config.gpu_options.allow_growth = True
        self.sess = tf.Session(config=config)
        self.saver = tf.train.Saver()

    def init_model(self, model_name="AveragePooling", ckpt_dir="ckpt", **kwargs):
        with self.sess.as_default():
            Model = getattr(__import__("model"), model_name)
            self.model = Model(**kwargs)

            self.placeholder_dict = self.model.get_train_placeholders()

            self.ckpt_dir = ckpt_dir
            self.sess.run(tf.global_variables_initializer())
            if path.exists(path.join(ckpt_dir, "checkpoint")):
                print("Restoring Variables from Checkpoint")
                self.saver.restore(self.sess, tf.train.latest_checkpoint(self.ckpt_dir))
            else:
                print('Initializing Variables')
                self.sess.run(tf.global_variables_initializer())
            self.curr_epoch = self.sess.run(self.model.epoch_step)

    # def _train(self, batch):
    #     feed_dict = {}
    #     for key in self.placeholder_dict.keys():
    #         feed_dict[self.placeholder_dict[key]] = batch[key]
    #     feed_dict[self.model.dropout_keep_prob] = 0.5
    #     logits, loss, _ = self.sess.run([self.model.logits, self.model.loss_val, self.model.train_op], feed_dict)
    #     return logits, loss

    def eval(self, eval_set):
        eval_size = eval_set["size"]
        loss_sum, batch_num = 0.0, 0
        matrix = 0
        for start, end in zip(range(0, eval_size, self.batch_size), range(self.batch_size, eval_size + self.batch_size, self.batch_size)):
            # end = eval_size if end > eval_size else end
            feed_dict = {}
            for key in self.placeholder_dict.keys():
                feed_dict[self.placeholder_dict[key]] = eval_set[key][start:end]
            feed_dict[self.model.dropout_keep_prob] = 1
            with self.sess.as_default():
                logits, loss = self.sess.run([self.model.logits, self.model.loss_val], feed_dict)
            loss_sum += loss
            matrix += confusion_matrix(logits, eval_set["input_y"][start:end])
            # hit_sum += hit_counter(logits, eval_set["input_y"][start:end])
            batch_num += 1
        return loss_sum / batch_num, matrix

    # def eval(self, datasize, *args, **kwargs):
    #     keys = tuple(self.placeholder_dict.keys())
    #     if len(args) >= len(self.placeholder_dict):
    #         eval_set = {k: v for k, v in zip(keys, args)}
    #     else:
    #         eval_set = {k: kwargs[k] for k in keys}

    #     loss_sum, batch_num, data_num = 0.0, 0, 0

    #     matrix = np.zeros([3, 3])
    #     for start, end in zip(range(0, datasize, self.batch_size), range(self.batch_size, datasize + self.batch_size, self.batch_size)):
    #         # end = eval_size if end > eval_size else end
    #         feed_dict = {}
    #         for key in self.placeholder_dict.keys():
    #             feed_dict[self.placeholder_dict[key]] = eval_set[key][start:end]
    #         feed_dict[self.model.dropout_keep_prob] = 1
    #         logits, loss = self.sess.run([self.model.logits, self.model.loss_val], feed_dict)
    #         loss_sum += loss
    #         confusion_matrix(logits, eval_set["input_y"][start:end], matrix)
    #         # hit_sum += hit_counter(logits, eval_set["input_y"][start:end])
    #         batch_num += 1
    #         data_num += len(logits)
    #     return loss_sum / batch_num, matrix

    def train(self, dataset):
        train, validation, test = dataset
        keys = set(train.keys())
        if "size" not in keys:
            print("Field 'size' is acquired in dataset")
            exit(1)
        for k in self.placeholder_dict.keys():
            if k not in keys:
                print("Field '%s' is acquired in dataset" % k)
                exit(1)

        # num_batchs = int(train_size / batch_size) + 1
        print("Training...")
        print("Start time: {}".format(time.asctime(time.localtime(time.time()))))
        train_size = train["size"]
        for epoch in range(self.curr_epoch, self.epoch_num):
            print("Epoch: %d\tlr: %.3f" % (epoch, self.model.lr))
            loss_sum, hit_sum, batch_num, data_num = 0.0, 0, 0, 0
            for start, end in zip(range(0, train_size, self.batch_size), range(self.batch_size, train_size + self.batch_size, self.batch_size)):
                # end = train_size if end > train_size else end
                feed_dict = {}
                for key in self.placeholder_dict.keys():
                    feed_dict[self.placeholder_dict[key]] = train[key][start:end]
                feed_dict[self.model.dropout_keep_prob] = 0.5
                with self.sess.as_default():
                    logits, loss, _ = self.sess.run([self.model.logits, self.model.loss_val, self.model.train_op], feed_dict)
                loss_sum += loss
                hit_sum += hit_counter(logits, train["input_y"][start:end])
                batch_num += 1
                data_num += len(logits)
                if batch_num % 10 == 0:
                    print("Batch %d\tTrain Loss:%.3f\tAccuracy:%.3f\t" % (batch_num, loss_sum / batch_num, hit_sum / data_num))

            eval_loss, eval_matrix = self.eval(validation)
            print("Validation Loss:%.3f" % eval_loss)
            print("Validation Matrix:\n{}".format(str(eval_matrix)))
            # save model to checkpoint
            with self.sess.as_default():
                _, lr = self.sess.run([self.model.epoch_increment, self.model.lr_decay])
            self.model.lr = lr
            save_path = path.join(self.ckpt_dir, "model.ckpt")
            self.saver.save(self.sess, save_path, global_step=epoch)
        print("End time: {}".format(time.asctime(time.localtime(time.time()))))
        test_loss, test_matrix = self.eval(test)
        print("Test Loss:%.3f" % test_loss)
        print("Test Matrix:\n{}".format(str(test_matrix)))

    def load_wv(self, vocab, embed_size, wv_path):
        print("Load pre-trained word emebedding from: ", wv_path)
        wv = KeyedVectors.load(wv_path)
        wv2list = []
        bound = np.sqrt(6.0) / np.sqrt(len(vocab))
        count_exist = 0
        for word in vocab:
            embedding = None
            try:
                embedding = wv[word]
            except Exception:
                pass
            if embedding is not None:
                wv2list.append(embedding)
                count_exist = count_exist + 1
            else:
                wv2list.append(np.random.uniform(-bound, bound, embed_size))
        wv2list[0] = np.zeros(embed_size)
        word_embedding = tf.constant(np.array(wv2list), dtype=tf.float32)
        with self.sess.as_default():
            self.sess.run(tf.assign(self.model.Embedding, word_embedding))
        print("Words exists embedding: %d" % count_exist)


def hit_counter(logits, input_y, binary=False):
    count = 0
    batch_size = len(logits)
    pred_list = np.zeros([batch_size])
    actual_list = np.zeros([batch_size])
    if binary:
        for i, logit in enumerate(logits):
            pred_list[i] = 1 if logit[0] >= 0.5 else 0
            actual_list[i] = input_y[0]
    else:
        for i, logit in enumerate(logits):
            li = logit.tolist()
            pred_list[i] = li.index(max(li))
            actual_list[i] = input_y[i].tolist().index(1)
    for pred, actual in zip(pred_list, actual_list):
        if pred == actual:
            count += 1
    return count

def confusion_matrix(logits, input_y):
    matrix = np.zeros([logits.shape[1], logits.shape[1]])
    for i, logit in enumerate(logits):
        li = logit.tolist()
        pred = li.index(max(li))
        actual = input_y[i].tolist().index(1)
        matrix[pred, actual] += 1
    return matrix
