# -*- coding: utf-8 -*-
"""
.. module:: helpers

Created by InfinityFuture

"""

import numpy as np
import torch
from torch import nn

def global_max_pooling(tensor, dim, topk):
    """Global max pooling"""
    ret, _ = torch.topk(tensor, topk, dim)
    return ret

def init_embedding(word_embeds):
    """Init embedding variable"""
    scope = np.sqrt(3. / word_embeds.weight.size(1))
    nn.init.uniform_(word_embeds.weight, -scope, scope)

def get_weight(weight, ratio0=1., ratio1=1.):
    """Weight random parameter:

    [Glorot and Bengio2010] Xavier Glorot and Yoshua
    Bengio. 2010. Understanding the difficulty of
    training deep feedforward neural networks. In In-
    ternational conference on artificial intelligence and
    statistics, pages 249–256.
    """
    dim0, dim1 = weight.size()[:2]
    scope = np.sqrt(6. / (dim0 / ratio0 + dim1 / ratio1))
    nn.init.uniform_(weight, -scope, scope)

def get_bias(bias):
    """Init bias"""
    nn.init.zeros_(bias)

def get_lstm_bias(bias):
    """Init bias for LSTM

    (b_ii|b_if|b_ig|b_io), of shape (4*hidden_size)

    set f-gate is ones, zeros for others
    """
    dim = bias.size(0)
    assert dim % 4 == 0
    hdim = dim // 4
    nn.init.zeros_(bias)
    nn.init.ones_(bias[hdim:2*hdim])

def init_linear_weight(layer):
    """init weight for nn.Linear"""
    get_weight(layer.weight)
    if layer.bias is not None:
        get_bias(layer.bias)

def init_rnn_weight(layer, rnn_type):
    """init weight for nn.LSTM and nn.GRU"""
    for weight_name in dir(layer):
        if weight_name.startswith('weight_') or weight_name.startswith('bias_'):
            if weight_name.startswith('weight'):
                weight = getattr(layer, weight_name)
                if rnn_type == 'lstm':
                    get_weight(weight, 4.)
                elif rnn_type == 'gru':
                    get_weight(weight, 3.)
                else:
                    get_weight(weight)
            if weight_name.startswith('bias'):
                bias = getattr(layer, weight_name)
                if rnn_type == 'lstm':
                    get_lstm_bias(bias)
                else:
                    get_bias(bias)
