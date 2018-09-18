# -*- coding: utf-8 -*-
"""Main tagger class
"""

import os
import math
import pickle
import torch
from torch import nn
from torch import optim
from tqdm import tqdm
from sklearn.base import BaseEstimator
import numpy as np

from torch_tagger.rnn_crf import RNNCRF
from torch_tagger.utils import build_vocabulary, prepare_sequence, batch_flow, DEVICE
from torch_tagger.utils import extrat_entities, pad_seq
from torch_tagger.nadam import Nadam

class Tagger(BaseEstimator):
    """scikit-learn compatible Tagger"""

    def __init__(self, # pylint: disable=too-many-arguments,too-many-locals
                 embedding_dim=100,
                 hidden_dim=100,
                 weight_decay=0.0,
                 epochs=10,
                 verbose=1,
                 batch_size=32,
                 device='auto',
                 embedding_dropout_p=0.0,
                 rnn_dropout_p=0.0,
                 bidirectional=True,
                 rnn_type='lstm',
                 num_layers=1,
                 optimizer='Adam',
                 learning_rate=None,
                 learning_rate_decay=0,
                 embedding_trainable=True,
                 crf=True,
                 debug=False,
                 char_max_len=30,
                 char_embedding_dim=30,
                 clip_grad_norm=5.,
                 _model=None,
                 _optimizer=None,
                 _word_to_ix=None,
                 _ix_to_word=None,
                 _tag_to_ix=None,
                 _ix_to_tag=None,
                 _char_to_ix=None,
                 _ix_to_char=None):
        """init"""
        self.params = {
            'embedding_dim': embedding_dim,
            'hidden_dim': hidden_dim,
            'weight_decay': weight_decay,
            'epochs': epochs,
            'verbose': verbose,
            'batch_size': batch_size,
            'device': device,
            'embedding_dropout_p': embedding_dropout_p,
            'rnn_dropout_p': rnn_dropout_p,
            'bidirectional': bidirectional,
            'rnn_type': rnn_type,
            'num_layers': num_layers,
            'optimizer': optimizer,
            'learning_rate': learning_rate,
            'learning_rate_decay': learning_rate_decay,
            'embedding_trainable': embedding_trainable,
            'crf': crf,
            'debug': debug,
            'char_max_len': char_max_len,
            'char_embedding_dim': char_embedding_dim,
            'clip_grad_norm': clip_grad_norm,
        }
        self._model = _model
        self._optimizer = _optimizer
        self._word_to_ix = _word_to_ix
        self._ix_to_word = _ix_to_word
        self._tag_to_ix = _tag_to_ix
        self._ix_to_tag = _ix_to_tag
        self._char_to_ix = _char_to_ix
        self._ix_to_char = _ix_to_char

    def _get_learning_rate(self):
        optimizer = self.params['optimizer']
        learning_rate = self.params['learning_rate']
        if learning_rate is not None:
            return learning_rate
        if optimizer.upper() == 'SGD':
            return 1e-2
        if optimizer.upper() == 'ADAM':
            return 1e-3
        if optimizer.upper() == 'NADAM':
            return 2e-3
        return 1e-3

    def get_params(self, deep=True):
        """Get params for scikit-learn compatible"""
        params = self.params
        if deep:
            params['_model'] = self._model.state_dict() if self._model is not None else None
            params['_optimizer'] = self._optimizer.state_dict() \
                if self._optimizer is not None else None
            params['_word_to_ix'] = self._word_to_ix
            params['_ix_to_word'] = self._ix_to_word
            params['_tag_to_ix'] = self._tag_to_ix
            params['_ix_to_tag'] = self._ix_to_tag
            params['_char_to_ix'] = self._char_to_ix
            params['_ix_to_char'] = self._ix_to_char
        return params

    def set_params(self, **parameters):
        """Set params for scikit-learn compatible"""
        for key, value in parameters.items():
            if key in self.params:
                self.params[key] = value
        return self

    def __getstate__(self):
        """Get state for pickle"""
        state = {
            'params': self.params,
            '_model': self._model.state_dict() if self._model is not None else None,
            '_optimizer': self._optimizer.state_dict() if self._optimizer is not None else None,
            '_word_to_ix': self._word_to_ix,
            '_ix_to_word': self._ix_to_word,
            '_tag_to_ix': self._tag_to_ix,
            '_ix_to_tag': self._ix_to_tag,
            '_char_to_ix': self._char_to_ix,
            '_ix_to_char': self._ix_to_char
        }
        return state

    def __setstate__(self, state):
        """Get state for pickle"""
        self.params = state['params']
        if state['_model'] is not None:
            self._word_to_ix = state['_word_to_ix']
            self._ix_to_word = state['_ix_to_word']
            self._tag_to_ix = state['_tag_to_ix']
            self._ix_to_tag = state['_ix_to_tag']
            self._char_to_ix = state['_char_to_ix']
            self._ix_to_char = state['_ix_to_char']
            self.apply_params()
            self._model.load_state_dict(state['_model'])
            self._optimizer.load_state_dict(state['_optimizer'])

    def _get_device(self):
        """Get device to predict or train"""
        device = self.params['device']
        if device == 'auto':
            return DEVICE
        if device in ('gpu', 'cuda'):
            return torch.device('cuda')
        return torch.device('cpu')

    def apply_params(self): # pylint: disable=too-many-locals
        """Apply params and build RNN-CRF model"""

        embedding_dim = self.params['embedding_dim']
        hidden_dim = self.params['hidden_dim']
        weight_decay = self.params['weight_decay']
        embedding_dropout_p = self.params['embedding_dropout_p']
        rnn_dropout_p = self.params['rnn_dropout_p']
        bidirectional = self.params['bidirectional']
        rnn_type = self.params['rnn_type']
        num_layers = self.params['num_layers']
        optimizer = self.params['optimizer']
        embedding_trainable = self.params['embedding_trainable']
        batch_size = self.params['batch_size']
        crf = self.params['crf']
        debug = self.params['debug']
        char_max_len = self.params['char_max_len']
        char_embedding_dim = self.params['char_embedding_dim']

        word_to_ix = self._word_to_ix
        tag_to_ix = self._tag_to_ix
        char_to_ix = self._char_to_ix

        model = RNNCRF(
            len(word_to_ix),
            tag_to_ix,
            embedding_dim,
            hidden_dim,
            num_layers=num_layers,
            bidirectional=bidirectional,
            device=self._get_device(),
            embedding_dropout_p=embedding_dropout_p,
            rnn_dropout_p=rnn_dropout_p,
            rnn_type=rnn_type,
            embedding_trainable=embedding_trainable,
            batch_size=batch_size,
            crf=crf,
            debug=debug,
            char_max_len=char_max_len,
            char_embedding_dim=char_embedding_dim,
            char_vocab_size=len(char_to_ix)
        ).to(self._get_device())

        if optimizer.upper() == 'ADAM':
            optimizer = optim.Adam(
                model.parameters(),
                lr=self._get_learning_rate(),
                weight_decay=weight_decay
            )
        elif optimizer.upper() == 'SGD':
            optimizer = optim.SGD(
                model.parameters(),
                lr=self._get_learning_rate(),
                weight_decay=weight_decay,
                momentum=0.0
            )
        elif optimizer.upper() == 'NADAM':
            optimizer = Nadam(
                model.parameters(),
                lr=self._get_learning_rate(),
                weight_decay=weight_decay
            )

        self._model = model
        self._optimizer = optimizer

    def fit(self, # pylint: disable=invalid-name,too-many-arguments,too-many-locals,too-many-statements,too-many-branches
            X, y,
            X_dev=None, y_dev=None, patient_dev=None,
            save_best=None,
            pretrained_embedding=None,
            predict_batch_size=32):
        """Fit the model"""

        assert len(X) >= self.params['batch_size'], 'X must size >= batch_size'
        assert len(y) >= self.params['batch_size'], 'y must size >= batch_size'
        assert len(X) == len(y), 'X must size equal to y'

        # Autommatic build vocabulary
        vocabulary = build_vocabulary(X, y)
        self._char_to_ix = vocabulary['char_to_ix']
        self._ix_to_char = vocabulary['ix_to_char']
        if self._word_to_ix is None and self._tag_to_ix is None:
            self._word_to_ix = vocabulary['word_to_ix']
            self._ix_to_word = vocabulary['ix_to_word']
            self._tag_to_ix = vocabulary['tag_to_ix']
            self._ix_to_tag = vocabulary['ix_to_tag']
        elif self._word_to_ix is None:
            self._word_to_ix = vocabulary['word_to_ix']
            self._ix_to_word = vocabulary['ix_to_word']
        elif self._tag_to_ix is None:
            self._tag_to_ix = vocabulary['tag_to_ix']
            self._ix_to_tag = vocabulary['ix_to_tag']

        epochs = self.params['epochs']
        verbose = self.params['verbose']
        batch_size = self.params['batch_size']
        learning_rate_decay = self.params['learning_rate_decay']
        crf = self.params['crf']
        char_max_len = self.params['char_max_len']
        clip_grad_norm = self.params['clip_grad_norm']

        predict_batch_size = max(predict_batch_size, batch_size)

        word_to_ix = self._word_to_ix
        tag_to_ix = self._tag_to_ix
        # ix_to_tag = self._ix_to_tag
        char_to_ix = self._char_to_ix

        self.apply_params()
        model, optimizer = self._model, self._optimizer
        if pretrained_embedding is not None:
            model.load_embedding(pretrained_embedding) # pylint: disable=protected-access

        # Check predictions before training
        # with torch.no_grad():
        #     precheck_sent = prepare_sequence(X[0], word_to_ix)
        #     precheck_sent = torch.from_numpy(np.asarray([precheck_sent]))
        #     precheck_sent = precheck_sent.to(self._get_device())
        #     _, pred = model(precheck_sent, torch.Tensor([len(X[0])]).long().to(self._get_device()))
        #     assert len([ix_to_tag[tag_to_ix[t]] for t in y[0]]) == len(pred[0]), \
        #         'checking before training error'

        dev_best = float('inf')
        dev_best_round = 0
        # Make sure prepare_sequence from earlier in the LSTM section is loaded
        for epoch in range(epochs):
            lnrt = self._get_learning_rate()
            if learning_rate_decay > 0:
                lnrt = self._get_learning_rate() / (1 + epoch * learning_rate_decay)
                for param_group in optimizer.param_groups:
                    param_group['lr'] = lnrt
            pbar = range(math.ceil(len(X) / batch_size))
            flow = batch_flow(
                X, y, word_to_ix, tag_to_ix,
                batch_size=batch_size,
                char_max_len=char_max_len,
                char_to_ix=char_to_ix
            )
            losses = []
            if verbose > 0:
                pbar = tqdm(pbar, ncols=0)
                pbar.set_description('epoch: {}/{} loss: {:.4f}'.format(epoch + 1, epochs, 0))
            for _ in pbar:
                optimizer.zero_grad()

                x_b, y_b, l_b, l_c = next(flow)
                x_b = x_b.to(self._get_device())
                y_b = y_b.to(self._get_device())
                l_b = l_b.to(self._get_device())
                if l_c is not None:
                    l_c = l_c.to(self._get_device())
                if crf:
                    loss = model.neg_log_likelihood(x_b, y_b, l_b, chars=l_c)
                else:
                    loss = model.cross_entropy_loss(x_b, y_b, l_b, chars=l_c)

                losses.append(loss.item())
                loss.backward()
                nn.utils.clip_grad_norm_(model.parameters(), clip_grad_norm)
                optimizer.step()
                if verbose > 0:
                    pbar.set_description(
                        'epoch: {}/{} loss: {:.4f} lr: {:.4f}'.format(
                            epoch + 1, epochs, np.mean(losses), lnrt
                        )
                    )
            train_score = self.score(X, y, batch_size=predict_batch_size)
            dev_score = None
            if X_dev is None:
                if verbose > 0:
                    print('train: {:.4f}'.format(train_score))
            else:
                with torch.no_grad():

                    dev_score = self.score(X_dev, y_dev, batch_size=predict_batch_size)
                    flow = batch_flow(
                        X_dev, y_dev, word_to_ix, tag_to_ix,
                        batch_size=predict_batch_size,
                        char_max_len=char_max_len,
                        char_to_ix=char_to_ix
                    )
                    dev_losses = []
                    for _ in range(math.ceil(len(X_dev) / predict_batch_size)):
                        x_b, y_b, l_b, l_c = next(flow)
                        x_b = x_b.to(self._get_device())
                        y_b = y_b.to(self._get_device())
                        l_b = l_b.to(self._get_device())
                        if l_c is not None:
                            l_c = l_c.to(self._get_device())
                        if crf:
                            loss = model.neg_log_likelihood(x_b, y_b, l_b, chars=l_c)
                        else:
                            loss = model.cross_entropy_loss(x_b, y_b, l_b, chars=l_c)
                        dev_losses.append(loss.item())
                    dev_loss = np.mean(dev_losses) / (predict_batch_size / batch_size)

                if verbose > 0:
                    print('dev loss: {:.4f}, train f1: {:.4f}, dev f1: {:.4f}'.format(
                        dev_loss, train_score, dev_score))
                if isinstance(save_best, str):
                    if dev_loss < dev_best:
                        print('save best {:.4f} > {:.4f}'.format(
                            dev_best, dev_loss
                        ))
                        dev_best = dev_loss
                        dev_best_round = 0
                        save_dir = os.path.realpath(os.path.dirname(save_best))
                        if not os.path.exists(save_dir):
                            os.makedirs(save_dir)
                        with open(save_best, 'wb') as fobj:
                            pickle.dump(self, fobj)
                    else:
                        dev_best_round += 1
                        print('no better {:.4f} <= {:.4f} {}/{}'.format(
                            dev_best, dev_loss, dev_best_round, patient_dev
                        ))
                        if isinstance(patient_dev, int) and dev_best_round >= patient_dev:
                            return
                print()

    def predict(self, X, batch_size=None, verbose=0): # pylint: disable=invalid-name,too-many-locals
        """Predict tags"""
        model = self._model
        word_to_ix = self._word_to_ix
        ix_to_tag = self._ix_to_tag
        char_to_ix = self._char_to_ix
        if batch_size is None:
            batch_size = self.params['batch_size']
        char_max_len = self.params['char_max_len']
        # Check predictions after training
        data = list(enumerate(X))
        data = sorted(data, key=lambda t: len(t[1]), reverse=True)
        inds = [i for i, _ in data]
        X = [x for _, x in data]
        ret = [None] * len(X)
        with torch.no_grad():
            batch_total = math.ceil(len(X) / batch_size)
            pbar = range(batch_total)
            if verbose > 0:
                pbar = tqdm(pbar, ncols=0)
            for i in pbar:
                ind_batch = inds[i * batch_size : (i + 1) * batch_size]
                x_batch = X[i * batch_size : (i + 1) * batch_size]
                lens = [len(x) for x in x_batch]
                max_len = np.max(lens)

                char_batch = None
                if char_to_ix is not None:
                    char_batch = []
                    for xseq in x_batch:
                        sentence_char = []
                        for char in xseq:
                            char = char[:char_max_len]
                            char = prepare_sequence(char, char_to_ix)
                            char = pad_seq(char, char_max_len)
                            sentence_char.append(char)
                        while len(sentence_char) < max_len:
                            sentence_char.append([0] * char_max_len)
                        char_batch.append(sentence_char)
                    char_batch = np.array(char_batch)
                    char_batch = torch.from_numpy(char_batch).to(self._get_device())

                x_batch = [
                    prepare_sequence(sent, word_to_ix)
                    for sent in x_batch
                ]
                x_batch = [pad_seq(x, max_len) for x in x_batch]

                sent = torch.from_numpy(np.asarray(x_batch))
                sent = sent.to(self._get_device())
                _, predicts = model(
                    sent,
                    torch.Tensor(lens).long().to(self._get_device()),
                    char_batch
                )
                # print(predicts)
                for ind, tag_len, tags in zip(ind_batch, lens, predicts):
                    tags = [ix_to_tag[i] for i in tags[:tag_len]]
                    ret[ind] = tags
        return ret

    def score(self, X, y, batch_size=None, verbose=0, detail=False): # pylint: disable=invalid-name,too-many-locals
        """Calculate NER F1
        Based CONLL 2003 standard
        """
        def _get_sets():
            preds = self.predict(X, verbose=verbose, batch_size=batch_size)
            pbar = enumerate(zip(preds, y))
            if verbose > 0:
                pbar = tqdm(pbar, ncols=0, total=len(y))

            apset = []
            arset = []
            for i, (pred, y_true) in pbar:
                pset = extrat_entities(pred)
                rset = extrat_entities(y_true)
                for item in pset:
                    apset.append(tuple(
                        [i] + list(item)
                    ))
                for item in rset:
                    arset.append(tuple(
                        [i] + list(item)
                    ))
            return apset, arset

        apset, arset = _get_sets()
        pset = set(apset)
        rset = set(arset)
        inter = pset.intersection(rset)
        precision = len(inter) / len(pset) if pset else 1
        recall = len(inter) / len(rset) if rset else 1
        f1score = 0 
        if precision + recall > 0:
            f1score = 2 * ((precision * recall) / (precision + recall))
        if detail:
            return precision, recall, f1score
        return f1score
