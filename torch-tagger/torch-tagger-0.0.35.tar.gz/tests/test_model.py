# -*- coding: utf-8 -*-
"""Test TaggerModel"""

import unittest

import numpy as np
import torch
from torch_tagger.tagger_model import TaggerModel
from torch_tagger.utils import START_TAG, STOP_TAG, sequence_mask


def same(amat, bmat):
    """Test two matrix is same"""
    return np.sum((amat.flatten() - bmat.flatten())**2)


def test_model(batch_size=2,
               seq_len=9,
               vocab_size=10,
               embedding_dim=10,
               hidden_dim=10):
    """Test model entry"""
    device = torch.device('cpu')
    tag_to_ix = {
        'a': 0,
        'b': 1,
        START_TAG: 2,
        STOP_TAG: 3,
    }

    scale = 1000.

    model = TaggerModel(
        vocab_size,
        tag_to_ix,
        embedding_dim,
        hidden_dim,
        num_layers=1,
        bidirectional=True,
        embedding_dropout_p=0,
        rnn_dropout_p=0,
        rnn_type='lstm',
        device=device,
        embedding_trainable=True,
        use_crf=True,
        use_char='lstm',
        char_vocab_size=10,
        char_max_len=10,
        char_embedding_dim=10,
        char_hidden_dim=10,
        char_dropout_p=0,
        char_bidirectional=True,
        average_loss=False)
    # feats_batch dim: [batch_size, seq_len, target_dim]
    # lengths_batch dim: [batch_size]
    target_dim = len(tag_to_ix)
    feats = torch.randn(batch_size, seq_len, target_dim) * scale

    # sentences = torch.randint(0, vocab_size, (batch_size, seq_len)).long()
    tags = torch.randint(0, target_dim, (batch_size, seq_len)).long()
    lengths = torch.tensor(
        # [seq_len] * batch_size
        np.array(
            sorted(
                np.random.randint(1, seq_len, size=batch_size).tolist(),
                reverse=True))).view(-1)
    masks = sequence_mask(lengths, seq_len)

    decode_input = torch.rand(batch_size, seq_len, len(tag_to_ix))
    score, pred = model._decoder._viterbi_decode(decode_input, lengths)
    score_b, pred_b = model._decoder._viterbi_decode_batch(
        decode_input, lengths, masks)
    score = score.cpu().detach().numpy()
    score_b = score_b.cpu().detach().numpy()
    assert score.shape == score_b.shape
    assert np.sum(np.sum((score - score_b)**2)) < 1e-10
    assert pred.shape == pred_b.shape, 'batch_size: {} {} {}'.format(
        batch_size, pred, pred_b)

    diff = [np.sum(a - b) for a, b in zip(pred, pred_b)]

    assert np.sum(np.sum(diff)) < 1e-10, 'batch_size: {} {} {}'.format(
        batch_size, pred, pred_b)

    feats = feats * masks.view(batch_size, seq_len, 1)
    ret = model._decoder._forward_alg(feats, lengths)
    retb = model._decoder._forward_alg_batch(feats, lengths)
    ret, retb = ret.cpu().detach().numpy(), retb.cpu().detach().numpy()
    diff = same(ret, retb)
    # print('forward diff', diff, ret[:3])
    assert diff < 1e-10, 'diff: {}, {}, {}'.format(diff, ret, retb)

    rets = model._decoder._score_sentence(feats, tags, lengths)
    retsb = model._decoder._score_sentence_batch(feats, tags, lengths, masks)
    diff = same(rets.cpu().detach().numpy(), retsb.cpu().detach().numpy())
    # print('score diff', diff, rets[:3])
    assert diff < 1e-10, 'diff: {}'.format(diff)
    return True


class TestTaggerModel(unittest.TestCase):
    def test_models(self):
        """Test different parameters"""
        params = []
        for batch_size in (1, 3, 9):
            for seq_len in (2, 3, 9, 100):
                for vocab_size in (3, 9, 100):
                    for embedding_dim in (10, 100, 500):
                        for hidden_dim in (10, 100, 500):
                            params.append((batch_size, seq_len, vocab_size,
                                           embedding_dim, hidden_dim))
        for param in params:
            self.assertTrue(test_model(*param))


if __name__ == '__main__':
    unittest.main()
