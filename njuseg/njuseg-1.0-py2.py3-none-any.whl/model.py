import sys
import time
from njuseg import preprocess
from njuseg.preprocess import Sent, FScore, init_map_from_file
import json
import dynet as dy
import numpy as np
import copy
import os
import zipfile


class Segmenter(object):

    class State(object):
        def __init__(self, n):
            self.stack = []
            self.i = 0
            self.n = n
            self.pred_labels = []

        def take_action(self, action):
            if action == 'NA':
                self.stack.append((self.i, self.i))
            elif action == 'AP':
                l, r = self.stack.pop()
                self.stack.append((l, r+1))
            self.i += 1
            self.pred_labels.append(action)

        def s_features(self):
            lefts = []
            rights = []

            lefts.append(1)
            if len(self.stack) < 2:
                rights.append(0)
            else:
                s1_left = self.stack[-1][0] + 1
                rights.append(s1_left - 1)

            s1_left = self.stack[-1][0] + 1
            lefts.append(s1_left)
            s1_right = self.stack[-1][1] + 1
            rights.append(s1_right)

            lefts.append(self.i+1)
            rights.append(self.i+1)

            if self.i+2 > self.n+1:
                lefts.append(self.n+1)
            else:
                lefts.append(self.i+2)
            rights.append(self.n)

            return tuple(lefts), tuple(rights)

    def __init__(self, config, fm=None):
        self.config = config
        if fm is None:
            # vocab_file_name = config['vocab_file_name']
            # if vocab_file_name is not None and not os.path.exists(vocab_file_name):
            #     self.fm = init_map_from_file(config['train_file'])
            #     np.save(vocab_file_name,self.fm)
            # else:
            #     self.fm = np.load(vocab_file_name).item()
            self.fm = init_map_from_file(config['train_file'])
        else:
            self.fm = fm
        self.config['unigram_size'] = self.fm['unigram_size']
        self.config['bigram_size'] = self.fm['bigram_size']
        model = dy.Model()

        self.model = model
        self.uni_embed = model.add_subcollection()
        self.bi_embed = model.add_subcollection()
        self.params = self.initParams(model, config)
        self.initEmbeddings(config)
        self.trainer = dy.AdadeltaTrainer(self.model, eps=1e-7, rho=0.99)
        self.trainer.learning_rate = 0.2
        self.droprate = config['droprate']
        self.activation = dy.rectify

    def initEmbeddings(self, config):

        self.params['unigram_embed'] = self.uni_embed.add_lookup_parameters(
            (config['unigram_size'], config['unigram_dim']),

        )
        self.params['bigram_embed'] = self.bi_embed.add_lookup_parameters(
            (config['bigram_size'], config['bigram_dim']),
        )

        if config['uni_embed'] is not None:
            pretrain_char = np.load(config['uni_embed']).item()
            cnt = 0
            for c in self.fm['unigram_idx_map']:
                if c not in pretrain_char:
                    continue
                self.params['unigram_embed'].init_row(
                    self.fm['unigram_idx_map'][c], pretrain_char[c])
                cnt += 1
            print(cnt)
            print(' Loaded unigram embedding from file : {}'.format(
                config['uni_embed']))

    def initParams(self, model, config):
        params = dict()

        params['e2l'] = model.add_parameters(
            (config['lstm_input_dim'], 3 *
             config['unigram_dim']+2*config['bigram_dim']),
            dy.UniformInitializer(0.01)
        )

        params['lb'] = model.add_parameters(
            (config['lstm_input_dim']),
            dy.ConstInitializer(0)
        )
        params['fwd_lstm1'] = dy.LSTMBuilder(
            config['lstm_layer'],
            config['lstm_input_dim'],
            config['lstm_hidden_dim'],
            model
        )
        params['back_lstm1'] = dy.LSTMBuilder(
            config['lstm_layer'],
            config['lstm_input_dim'],
            config['lstm_hidden_dim'],
            model
        )
        params['fwd_lstm2'] = dy.LSTMBuilder(
            config['lstm_layer'],
            2*config['lstm_hidden_dim'],
            config['lstm_hidden_dim'],
            model
        )
        params['back_lstm2'] = dy.LSTMBuilder(
            config['lstm_layer'],
            2*config['lstm_hidden_dim'],
            config['lstm_hidden_dim'],
            model
        )
        params['l2h'] = model.add_parameters(
            (config['hidden_dim'], 4*4 * config['lstm_hidden_dim']),
            dy.UniformInitializer(0.01)
        )
        params['hb'] = model.add_parameters(
            (config['hidden_dim']),
            dy.ConstInitializer(0)
        )
        params['h2o'] = model.add_parameters(
            (config['label_size'], config['hidden_dim']),
            dy.UniformInitializer(0.01)
        )
        params['ob'] = model.add_parameters(
            (config['label_size']),
            dy.ConstInitializer(0)
        )
        params['bos'] = model.add_parameters(
            (config['lstm_input_dim'])
        )
        return params

    def initExprs(self):

        param_exprs = dict()
        param_exprs['unigram_embed'] = dy.parameter(
            self.params['unigram_embed'])
        param_exprs['bigram_embed'] = dy.parameter(self.params['bigram_embed'])
        # param_exprs['u2l'] = dy.parameter(self.params['u2l'])
        # param_exprs['b2l'] = dy.parameter(self.params['b2l'])
        param_exprs['e2l'] = dy.parameter(self.params['e2l'])
        param_exprs['lb'] = dy.parameter(self.params['lb'])
        param_exprs['l2h'] = dy.parameter(self.params['l2h'])
        param_exprs['hb'] = dy.parameter(self.params['hb'])
        param_exprs['h2o'] = dy.parameter(self.params['h2o'])
        param_exprs['ob'] = dy.parameter(self.params['ob'])
        param_exprs['bos'] = dy.parameter(self.params['bos'])
        self.param_exprs = param_exprs

    def save(self, filename):
        with open(filename + '.config', 'w+') as f:
            json.dump(self.config, f)
        np.save(filename+'.vocab', self.fm)
        self.model.save(filename + '.model')

        # self.uni_embed.save(filename + '.uni')
        # self.bi_embed.save(filename + '.bi')

    @staticmethod
    def load(filename):
        f_zip = zipfile.ZipFile(filename, 'r')
        namelist = f_zip.namelist()
        config_file = namelist[0]
        vocab_file = namelist[1]
        model_file = namelist[2]
        f_zip.extract(config_file, '.')
        f_zip.extract(vocab_file, '.')
        f_zip.extract(model_file, '.')
        with open(config_file, 'r') as f:
            config = json.load(f)
        fm = np.load(vocab_file).item()
        segmenter = Segmenter(config, fm)
        segmenter.model.populate(model_file)
        os.remove(vocab_file)
        os.remove(config_file)
        os.remove(model_file)

        return segmenter

    @staticmethod
    def feature_oracle(sent):

        labels = sent.labels()
        state = Segmenter.State(sent.clen)
        gold_features = []
        for index in range(sent.clen):
            if index == 0:
                action = 'NA'
            else:
                gold_feature = state.s_features()
                gold_features.append(gold_feature)
                action = labels[index]
            state.take_action(action)
        return gold_features

    def combine_unigram(self, u1, u2):
        chars = dy.concatenate([u1, u2])
        reset_gate = dy.logistic(
            self.param_exprs['reset_gate_W']*chars +
            self.param_exprs['reset_gate_b']
        )
        word = dy.tanh(
            self.param_exprs['com_W'] * dy.cmult(reset_gate, chars)
            + self.param_exprs['com_b']
        )

        return word

    def evaluate_recurrent(self, feature_seq, test=False):
        input = []
        for i in range(len(feature_seq)):
            pre_u1 = dy.lookup(
                self.params['unigram_embed'], feature_seq[i]['pre_u'])
            u1 = dy.lookup(self.params['unigram_embed'], feature_seq[i]['u'])
            pos_u1 = dy.lookup(
                self.params['unigram_embed'], feature_seq[i]['pos_u'])

            pre_bi = dy.lookup(
                self.params['bigram_embed'], feature_seq[i]['pre_bi']
            )
            pos_bi = dy.lookup(
                self.params['bigram_embed'], feature_seq[i]['pos_bi']
            )

            input_vec = dy.concatenate([pre_u1, u1, pos_u1, pre_bi, pos_bi])
            if not test:
                input_vec = dy.dropout(input_vec, self.droprate)
            input.append(self.activation(
                dy.affine_transform([dy.parameter(self.params['lb']), dy.parameter(self.params['e2l']), input_vec])))

        input = [dy.parameter(self.params['bos'])] + \
            input + [dy.parameter(self.params['bos'])]
        fwd1 = self.params['fwd_lstm1'].initial_state()
        back1 = self.params['back_lstm1'].initial_state()
        fwd2 = self.params['fwd_lstm2'].initial_state()
        back2 = self.params['back_lstm2'].initial_state()

        fwd1_out = []
        back1_out = []

        for i in input:
            fwd1 = fwd1.add_input(i)
            output = fwd1.output()
            fwd1_out.append(output)

        for i in reversed(input):
            back1 = back1.add_input(i)
            output = back1.output()
            back1_out.append(output)

        lstm2_input = []
        for (f, b) in zip(fwd1_out, reversed(back1_out)):
            lstm2_input.append(dy.concatenate([f, b]))

        fwd2_out = []
        back2_out = []

        for vec in lstm2_input:
            if self.droprate > 0 and not test:
                vec = dy.dropout(vec, self.droprate)
            fwd2 = fwd2.add_input(vec)
            fwd2_vec = fwd2.output()
            fwd2_out.append(fwd2_vec)

        for vec in reversed(lstm2_input):
            if self.droprate > 0 and not test:
                vec = dy.dropout(vec, self.droprate)
            back2 = back2.add_input(vec)
            back2_vec = back2.output()
            back2_out.append(back2_vec)

        fwd_out = [dy.concatenate([f1, f2])
                   for (f1, f2) in zip(fwd1_out, fwd2_out)]
        back_out = [dy.concatenate([b1, b2])
                    for (b1, b2) in zip(back1_out, back2_out)]

        return fwd_out, back_out[::-1]

    def evaluate_label(self, fwd, back, left, right, test=False):
        # hidden_input = dy.concatenate([fwd[index],back[index]])
        fwd_span_out = []
        for left_index, right_index in zip(left, right):
            fwd_span_out.append(fwd[right_index] - fwd[left_index - 1])
        fwd_span_vec = dy.concatenate(fwd_span_out)

        back_span_out = []
        for left_index, right_index in zip(left, right):
            back_span_out.append(back[left_index] - back[right_index+1])
        back_span_vec = dy.concatenate(back_span_out)

        hidden_input = dy.concatenate([fwd_span_vec, back_span_vec])
        if not test:
            hidden_input = dy.dropout(hidden_input, self.droprate)
        hidden_output = self.activation(
            dy.affine_transform([dy.parameter(self.params['hb']), dy.parameter(self.params['l2h']), hidden_input]))

        scores = dy.affine_transform([dy.parameter(
            self.params['ob']), dy.parameter(self.params['h2o']), hidden_output])

        return scores

    def supervised_loss(self, sent):

        label = sent.m_labels

        feature_seq = sent.feature_seq(self.fm)
        label_idx = sent.label2idx(label)

        state = Segmenter.State(sent.clen)

        loss = []
        fwd, back = self.evaluate_recurrent(feature_seq, test=False)
        for index in range(sent.clen):
            if index == 0:
                action = 'NA'
            else:
                left, right = state.s_features()
                score = self.evaluate_label(
                    fwd,
                    back,
                    left,
                    right,
                    test=False
                )
                loss.append(dy.pickneglogsoftmax(score, label_idx[index]))
                pred_idx = np.argmax(score.npvalue())
                action = ['NA', 'AP'][pred_idx]
            state.take_action(action)
        pred = Sent(sent.m_char_seq, [(l+1, r+1) for (l, r) in state.stack])
        acc = sent.eval(pred)
        return loss, acc

    def segment(self, sent):
        dy.renew_cg()

        feature_seq = sent.feature_seq(self.fm)
        state = self.State(sent.clen)
        fwd, back = self.evaluate_recurrent(feature_seq, test=True)
        for index in range(sent.clen):
            if index == 0:
                action = 'NA'
            else:
                left, right = state.s_features()
#                left,right = feature_oracle[index-1]
                score = self.evaluate_label(
                    fwd,
                    back,
                    left,
                    right,
                    test=True
                )
                pred_idx = np.argmax(score.npvalue())
                action = ['NA', 'AP'][pred_idx]
            state.take_action(action)

        pred = Sent(sent.m_char_seq, [(l+1, r+1) for (l, r) in state.stack])
        return pred

    def seg(self, sentence):
        char_seq = []
        for c in sentence:
            char_seq.append(c)
        sent = Sent(char_seq)
        return self.segment(sent).seg_string()

    def evaluate_corpus(self, sents):
        acc = FScore()
        for sent in sents:
            pred = self.segment(sent)
            acc += sent.eval(pred)
        return acc

    @staticmethod
    def write_predicted(src_file, target_file, model_file):
        start_time = time.time()
        test_sents = Sent.from_raw(src_file)
        segmenter_model = Segmenter.load(model_file)
        print(' Loaded model from file : {}'.format(model_file))
        fout = open(target_file, 'w+')
        total_chars = 0
        for sent in test_sents:
            pred = segmenter_model.segment(sent)
            # fout.write(pred.seg_string().encode('utf-8') + '\n')
            fout.write(pred.seg_string() + '\n')
            total_chars += sent.clen
        fout.close()
        end_time = time.time()
        print(' Write segmented result to {}'.format(target_file))
        print(' Total processed chars : {}, average speed : {}'.format(
            total_chars, total_chars*1.0/(end_time-start_time)))

    @staticmethod
    def zipmodel(model):
        f = zipfile.ZipFile(model, 'w', zipfile.ZIP_DEFLATED)
        f.write(model+'.config')
        f.write(model+'.vocab.npy')
        f.write(model+'.model')
        f.close()
        print(model)
        os.remove(model+'.config')
        os.remove(model+'.vocab.npy')
        os.remove(model+'.model')

    @staticmethod
    def test(test_file, model_file):
        test_sents = Sent.from_file(test_file)
        segmenter_model = Segmenter.load(model_file)
        print(' Loaded model from file : {}'.format(model_file))
        acc = segmenter_model.evaluate_corpus(test_sents)
        return acc

    @staticmethod
    def train(
            train_file,
            dev_file,
            model_save_file,
            unigram_dim=50,
            bigram_dim=50,
            lstm_input_dim=50,
            lstm_hidden_dim=50,
            hidden_dim=50,
            label_dim=32,
            label_size=2,
            droprate=0.2,
            uni_embed=None,
            bi_embed=None,
            epoch=10,
            batch_size=32,
            lstm_layer=2,
            unk_params=0.2,
            vocab_file_name=None
    ):
        print(' program Segmenter: ')
        print('     unigram dim = {}, bigram_dim = {},'.format(
            unigram_dim, bigram_dim))
        print('     lstm_input_dim = {}, lstm_hidden_dim = {}'.format(
            lstm_input_dim, lstm_hidden_dim))
        print('     hidden_dim = {}, label_dim = {}'.format(
            hidden_dim, label_dim))

        config = locals().copy()
        segmenter = Segmenter(config)

        raw_training_sents = Sent.from_file(train_file)
        dev_sents = Sent.from_file(dev_file)

        num_batched = -(-len(raw_training_sents) // batch_size)
        seg_every = -(-num_batched // 4)
        print(' total {} training sentences in {} batches'.format(
            len(raw_training_sents), num_batched))
        print(' total dev sentences: {}'.format(len(dev_sents)))

        best_acc = FScore()
        print(' Start training : ')
        start_time = time.time()

        for i in range(1, epoch+1):
            print('\n----------- epoch {} ----------'.format(i))
            training_acc = FScore()
            training_sents = copy.deepcopy(raw_training_sents)
            for sent in training_sents:
                sent.get_UNKed(segmenter.fm, unk_params)

            np.random.shuffle(training_sents)

            for b in range(num_batched):
                dy.renew_cg()

                batch = training_sents[(b*batch_size):(b+1)*batch_size]

                errors = []
                for sent in batch:
                    loss, acc = segmenter.supervised_loss(sent)
                    training_acc += acc
                    errors.extend(loss)
                # print ('after supervised loss')
                batch_error = dy.esum(errors)
                batch_error.backward()
                segmenter.trainer.update()

                print(
                    '\rBatch {} [Train: {}]'.format(
                        b,
                        training_acc
                    ),
                    end=''
                )
                sys.stdout.flush()
                if ((b+1) % seg_every) == 0 or b == (num_batched - 1):
                    dev_acc = segmenter.evaluate_corpus(
                        dev_sents,
                    )
                    print(' [Dev : {}]'.format(dev_acc))
                    if dev_acc.fscore() > best_acc.fscore():
                        best_acc = dev_acc
                        segmenter.save(model_save_file)
                        print('        [ Saved model: {}]'.format(
                            model_save_file))
                        Segmenter.zipmodel(model_save_file)

            current_time = time.time()
            elapsed_time = (current_time-start_time) / 60
            print('Elapsed time : {}'.format(elapsed_time))
