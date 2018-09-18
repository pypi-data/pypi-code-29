# -*- coding: utf-8 -*-
"""Test RNNCRF"""

import torch
import numpy as np
from torch_tagger.rnn_crf import RNNCRF
from torch_tagger.utils import sequence_mask, START_TAG, STOP_TAG

def same(amat, bmat):
    """Test two matrix is same"""
    return np.abs(np.sum(np.sum(amat - bmat)))

def test_model(batch_size=2, # pylint: disable=too-many-locals
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

    try:
        model = RNNCRF(
            vocab_size,
            tag_to_ix,
            embedding_dim,
            hidden_dim,
            device=device,
            rnn_type='unk'
        )
    except Exception as err: # pylint: disable=broad-except
        assert str(err) == 'Invalid rnn_type'

    scale = 1000.

    model = RNNCRF(
        vocab_size,
        tag_to_ix,
        embedding_dim,
        hidden_dim,
        device=device
    )
    # feats_batch dim: [batch_size, seq_len, target_dim]
    # lengths_batch dim: [batch_size]
    target_dim = len(tag_to_ix)
    feats = torch.randn(batch_size, seq_len, target_dim) * scale

    # sentences = torch.randint(0, vocab_size, (batch_size, seq_len)).long()
    tags = torch.randint(0, target_dim, (batch_size, seq_len)).long()
    lengths = torch.tensor( # pylint: disable=not-callable
        # [seq_len] * batch_size
        np.array(
            sorted(np.random.randint(1, seq_len, size=batch_size).tolist(), reverse=True)
        )
    ).view(-1)
    masks = sequence_mask(lengths, seq_len)

    decode_input = torch.rand(batch_size, seq_len, len(tag_to_ix))
    score, pred = model._viterbi_decode(decode_input, lengths) # pylint: disable=protected-access
    score_b, pred_b = model._viterbi_decode_batch(decode_input, lengths, masks) # pylint: disable=protected-access
    score = score.cpu().detach().numpy()
    score_b = score_b.cpu().detach().numpy()
    assert score.shape == score_b.shape
    assert np.sum(np.sum(score - score_b)) < 1e-7
    assert pred.shape == pred_b.shape, 'batch_size: {} {} {}'.format(
        batch_size,
        pred, pred_b
    )

    diff = [
        np.sum(a - b)
        for a, b in zip(pred, pred_b)
    ]

    assert np.sum(np.sum(diff)) < 1e-7, 'batch_size: {} {} {}'.format(
        batch_size,
        pred, pred_b
    )

    # feats = feats * masks.view(batch_size, seq_len, 1)
    ret = model._forward_alg(feats, lengths) # pylint: disable=protected-access
    retb = model._forward_alg_batch(feats, lengths, masks) # pylint: disable=protected-access
    diff = same(ret.cpu().detach().numpy(), retb.cpu().detach().numpy())
    # print('forward diff', diff, ret[:3])
    assert diff < 1e-7, 'diff: {}'.format(diff)

    rets = model._score_sentence(feats, tags, lengths) # pylint: disable=protected-access
    retsb = model._score_sentence_batch(feats, tags, lengths, masks) # pylint: disable=protected-access
    diff = same(rets.cpu().detach().numpy(), retsb.cpu().detach().numpy())
    # print('score diff', diff, rets[:3])
    assert diff < 1e-7, 'diff: {}'.format(diff)

    # loss = model.neg_log_likelihood(sentences, tags, lengths)
    # loss2 = model.neg_log_likelihood(sentences, tags, lengths)
    # assert abs(loss2 - loss) < 1e-4

    # print(ret[:3] - rets[:3])

def test_models():
    """Test different parameters"""
    test_model(
        2,
        3,
        4,
        5,
        6
    )
    # for batch_size in (1, 3, 9):
    #     for seq_len in (2, 3, 9):
    #         for vocab_size in (1, 3, 9):
    #             for embedding_dim in (10, 100):
    #                 for hidden_dim in (10, 100):
    #                     test_model(
    #                         batch_size,
    #                         seq_len,
    #                         vocab_size,
    #                         embedding_dim,
    #                         hidden_dim
    #                     )

if __name__ == '__main__':
    test_models()
