import tensorflow as tf
from os import path


class Predicter(object):
    def __init__(self):
        config = tf.ConfigProto()
        config.gpu_options.allow_growth = True
        self.sess = tf.Session(config=config)
        self.saver = tf.train.Saver()

    def init_model(self, model_name="AveragePooling", ckpt_dir=path.join(path.dirname(__file__), "ckpt"), **kwargs):
        with self.sess.as_default():
            Model = getattr(__import__("model"), model_name)
            self.model = Model(**kwargs)

            self.placeholder_dict = self.model.get_predict_placeholders()

            self.ckpt_dir = ckpt_dir
            if path.exists(path.join(ckpt_dir, "checkpoint")):
                print("Restoring Variables from Checkpoint")
                self.saver.restore(self.sess, tf.train.latest_checkpoint(self.ckpt_dir))
            else:
                print('Initializing Variables')
                self.sess.run(tf.global_variables_initializer())

    def predict(self, data, binary=False):
        # if len(text) == 0:
        #     return 0
        # input_dict = {
        #     "input_x": pad_sequences([text], maxlen=self.sequence_len, value=0.),
        #     "input_length": np.array([[len(text)]])
        # }
        feed_dict = {}
        for k in self.placeholder_dict.keys():
            try:
                feed_dict[self.placeholder_dict[k]] = data[k]
            except Exception:
                print("'%s' is acquired!", k)
                exit(1)
        feed_dict[self.model.dropout_keep_prob] = 1.0
        with self.sess.as_default():
            logits = self.sess.run(self.model.logits, feed_dict)
        if binary:
            return [float(p[0]) for p in logits]
        indices = []
        scores = []
        for logit in logits:
            li = logit.tolist()
            score = max(li)
            index = li.index(score)
            indices.append(index)
            scores.append(score)
        return indices, scores
