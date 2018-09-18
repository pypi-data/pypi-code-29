# -*- coding: utf-8 -*-
"""
.. module:: rnn_crf

Based https://pytorch.org/tutorials/beginner/nlp/advanced_tutorial.html

Modified by InfinityFuture

"""

import numpy as np
import torch
from torch import nn
import torch.nn.functional as F
from sklearn.preprocessing import normalize

from torch_tagger.utils import START_TAG, STOP_TAG, DEVICE, sequence_mask

# Transfer disable
NO_TRANS = -100000.

class RNNCRF(nn.Module): # pylint: disable=too-many-instance-attributes
    """
    RNN + CRF
    """

    def __init__(self, # pylint: disable=too-many-arguments
                 vocab_size,
                 tag_to_ix,
                 embedding_dim,
                 hidden_dim,
                 num_layers=1,
                 bidirectional=True,
                 embedding_dropout_p=0.5,
                 rnn_dropout_p=0.5,
                 rnn_type='lstm',
                 device=DEVICE,
                 embedding_trainable=True,
                 batch_size=None,
                 crf=True,
                 debug=False,
                 char_vocab_size=None,
                 char_max_len=None,
                 char_embedding_dim=32,
                 char_dropout_p=0.5):
        """
        Embedding Random Init:

        [He et al.2015] Kaiming He, Xiangyu Zhang, Shaoqing
        Ren, and Jian Sun. 2015. Delving deep into recti-
        fiers: Surpassing human-level performance on ima-
        genet classification. In Proceedings of the IEEE In-
        ternational Conference on Computer Vision, pages
        1026–1034.
        """
        super(RNNCRF, self).__init__()
        self._embedding_dim = embedding_dim
        self._hidden_dim = hidden_dim
        self._vocab_size = vocab_size
        self._tag_to_ix = tag_to_ix
        self._tagset_size = len(tag_to_ix)
        self._num_layers = num_layers
        self._bidirectional = bidirectional
        self._embedding_dropout_p = embedding_dropout_p
        self._rnn_dropout_p = rnn_dropout_p
        self._device = device
        self._rnn_type = rnn_type
        self._embedding_trainable = embedding_trainable
        self._batch_size = batch_size
        self._crf = crf
        self._debug = debug
        self._char_vocab_size = char_vocab_size
        self._char_max_len = char_max_len
        self._char_embedding_dim = char_embedding_dim
        self._char_dropout_p = char_dropout_p
        self._stop_idx = self._tag_to_ix[STOP_TAG]
        self._start_idx = self._tag_to_ix[START_TAG]

        self._cross_entropy_loss = nn.CrossEntropyLoss(ignore_index=0, reduction='sum')

        self._directions = 2 if bidirectional else 1

        # Embedding Layer
        self._word_embeds = nn.Embedding(vocab_size, embedding_dim)
        init_embedding(self._word_embeds)
        self._word_embeds.weight.requires_grad = self._embedding_trainable

        self._char_embeds = None
        self._char_cnn = None
        self._char_rnn = None
        # self._char_pool = None
        char_additional_dim = 0
        if char_vocab_size is not None:
            self._char_embeds = nn.Embedding(
                char_vocab_size,
                char_embedding_dim,
                padding_idx=0
            )
            init_embedding(self._char_embeds)

            self._char_rnn = nn.LSTM(
                char_embedding_dim,
                char_embedding_dim,
                num_layers=1,
                bidirectional=True
            )

            # test input
            testi = torch.randn(char_max_len, 1, char_embedding_dim)
            testi, _ = self._char_rnn(testi)

            testi = testi.view(-1)
            char_additional_dim = testi.size(0)

        # RNN Layer
        if rnn_type == 'lstm':
            self._rnn = nn.LSTM(
                embedding_dim + char_additional_dim,
                hidden_dim // self._directions,
                num_layers=num_layers,
                bidirectional=bidirectional,
                dropout=rnn_dropout_p if num_layers > 1 else 0
            )
        elif rnn_type == 'gru':
            self._rnn = nn.GRU(
                embedding_dim + char_additional_dim,
                hidden_dim // self._directions,
                num_layers=num_layers,
                bidirectional=bidirectional,
                dropout=rnn_dropout_p if num_layers > 1 else 0
            )
        else:
            raise Exception('Invalid rnn_type')
        init_rnn_weight(self._rnn, self._rnn_type)

        # Maps the output of the LSTM into tag space.
        # Output Projection Layer
        self._hidden2tag = nn.Linear(
            hidden_dim,
            self._tagset_size
        )
        init_linear_weight(self._hidden2tag)

        # Matrix of transition parameters.  Entry i,j is the score of
        # transitioning *to* i *from* j.
        # self._transitions = nn.Parameter(
        #     torch.randn(self._tagset_size, self._tagset_size))
        self._transitions = nn.Parameter(
            torch.zeros(self._tagset_size, self._tagset_size)
        )

        # These two statements enforce the constraint that we never transfer
        # to the start tag and we never transfer from the stop tag
        nn.init.constant_(
            self._transitions[tag_to_ix[START_TAG], :],
            NO_TRANS
        )
        nn.init.constant_(
            self._transitions.data[:, tag_to_ix[STOP_TAG]],
            NO_TRANS)

    def load_embedding(self, pretrained_embedding):
        """Load other pre-trained embedding vectors"""
        word_embeds = self._word_embeds
        assert len(pretrained_embedding.shape) == 2
        assert pretrained_embedding.shape[0] == word_embeds.weight.size(0)
        assert pretrained_embedding.shape[1] == word_embeds.weight.size(1)
        pretrained_embedding = normalize(pretrained_embedding)
        print('loaded pre-trained vectors', pretrained_embedding.shape)
        word_embeds.load_state_dict({
            'weight': torch.from_numpy(pretrained_embedding)
        })

    # def _init_hidden(self, batch_size):
    #     """Initilize the hidden for RNN"""
    #     hidden_dim = self._hidden_dim
    #     num_layers = self._num_layers
    #     rnn_type = self._rnn_type
    #     directions = self._directions
    #     if rnn_type == 'lstm':
    #         return (
    #             torch.zeros(
    #                 num_layers * directions,
    #                 batch_size,
    #                 hidden_dim
    #             ).to(self._device),
    #             torch.zeros(
    #                 num_layers * directions,
    #                 batch_size,
    #                 hidden_dim
    #             ).to(self._device),
    #         )
    #     # rnn_type == 'gru'
    #     return torch.zeros(
    #         num_layers * NO_TRANS,
    #         batch_size,
    #         hidden_dim
    #     ).to(self._device)

    def _forward_alg_single(self, feats):
        # Do the forward algorithm to compute the partition function
        init_alphas = torch.full((1, self._tagset_size), NO_TRANS,
            device=self._device)
        # START_TAG has all of the score.
        init_alphas[0][self._start_idx] = 0.

        # Wrap in a variable so that we will get automatic backprop
        forward_var = init_alphas

        # Iterate through the sentence
        for feat in feats:
            alphas_t = []  # The forward tensors at this timestep
            for next_tag in range(self._tagset_size):
                # broadcast the emission score: it is the same regardless of
                # the previous tag
                emit_score = feat[next_tag].view(
                    1, -1).expand(1, self._tagset_size)
                # the ith entry of trans_score is the score of transitioning to
                # next_tag from i
                trans_score = self._transitions[next_tag].view(1, -1)
                # The ith entry of next_tag_var is the value for the
                # edge (i -> next_tag) before we do log-sum-exp
                next_tag_var = forward_var + trans_score + emit_score
                # The forward variable for this tag is log-sum-exp of all the
                # scores.
                alphas_t.append(torch.logsumexp(next_tag_var.view(1, -1), 1).view(1))
            forward_var = torch.cat(alphas_t).view(1, -1)
        terminal_var = forward_var + self._transitions[self._stop_idx]
        alpha = torch.logsumexp(terminal_var.view(1, -1), 1)
        return alpha

    def _forward_alg(self, feats_batch, lengths_batch): # pylint: disable=too-many-locals
        """Get CRF result"""
        # feats_batch dim: [batch_size, seq_len, target_dim]
        # lengths_batch dim: [batch_size]
        batch_size = feats_batch.size(0)
        alpha_batch = []

        for i in range(batch_size):
            length = lengths_batch[i]
            feats = feats_batch[i][:length]
            alpha = self._forward_alg_single(feats)
            alpha_batch.append(alpha)
        return torch.stack(alpha_batch)

    def _forward_alg_batch(self, feats, lengths, masks): # pylint: disable=too-many-locals
        """Get CRF result, batch version"""
        # feats dim: [batch_size, seq_len, target_dim]
        # lengths dim: [batch_size]
        # masks dim: [batch_size, seq_len]
        batch_size, seq_len = feats.size()[:2]

        # Do the forward algorithm to compute the partition function
        init_alphas = torch.full(
            (batch_size, 1, self._tagset_size), NO_TRANS,
            requires_grad=False, device=self._device
        )
        # START_TAG has all of the score.
        init_alphas[:, 0, self._start_idx] = 0.

        # Wrap in a variable so that we will get automatic backprop
        forward_var = init_alphas

        # feats dim: [seq_len, batch_size, target_dim]
        feats = feats.permute(1, 0, 2)
        feats = feats.view(
            seq_len, batch_size, self._tagset_size, 1
        )

        trans_score = self._transitions.view(
            1, self._tagset_size, self._tagset_size
        )

        forward_var_batch = []
        for emit_score in feats:
            forward_var = forward_var.view(batch_size, 1, self._tagset_size)
            next_tag_var = forward_var + \
                trans_score + \
                emit_score
            next_tag_var = torch.logsumexp(next_tag_var, dim=2)
            forward_var = next_tag_var
            forward_var_batch.append(forward_var)

        forward_var_batch = torch.stack(forward_var_batch)
        forward_var = forward_var_batch.gather(
            0,
            (lengths.view(1, batch_size, 1) - 1).expand(
                1, batch_size, self._tagset_size
            )
        ).squeeze()
        forward_var = forward_var.view(batch_size, -1)

        alpha = forward_var + self._transitions[self._stop_idx]
        alpha = torch.logsumexp(alpha, 1)
        return alpha

    def _get_rnn_features(self, sentence, lengths, char_feats=None, is_train=True):
        """Get the output of RNN model"""

        # sentence dim: [batch_size, seq_len]
        batch_size, seq_len = sentence.size()

        # hidden = self._init_hidden(batch_size)

        # embeds dim: [batch_size, seq_len, embedding_size]
        embeds = self._word_embeds(sentence)
        embeds = F.dropout(embeds, p=self._embedding_dropout_p, training=is_train)
        # embeds dim: [seq_len, batch_size, embedding_size]

        if char_feats is not None:
            embeds = torch.cat([embeds, char_feats], 2)

        # embeds = embeds.view(seq_len, batch_size, -1)
        embeds = embeds.permute(1, 0, 2)

        # rnn_out, _ = self._rnn(embeds)
        packed = nn.utils.rnn.pack_padded_sequence(embeds, lengths, batch_first=False)
        rnn_out, _ = self._rnn(packed)
        rnn_out, _ = nn.utils.rnn.pad_packed_sequence(rnn_out, batch_first=False)

        # rnn_out dim: [seq_len, batch_size, hidden_dim]
        rnn_out = rnn_out.permute(1, 0, 2)
        rnn_out = rnn_out.contiguous().view(batch_size * seq_len, -1)

        rnn_out = F.dropout(rnn_out, p=self._rnn_dropout_p, training=is_train)

        # rnn_feats dim: [batch_size, seq_len, target_dim]
        rnn_feats = self._hidden2tag(rnn_out)

        return rnn_feats.view(batch_size, seq_len, -1)

    def _score_sentence_single(self, feats, tags):
        # Gives the score of a provided tag sequence
        score = torch.zeros(1, device=self._device)
        tags = torch.cat([
            torch.tensor( # pylint: disable=not-callable
                [self._start_idx], dtype=torch.long,
                device=self._device
            ),
            tags
        ])
        for i, feat in enumerate(feats):
            score = score + \
                self._transitions[tags[i + 1], tags[i]] + feat[tags[i + 1]]
        score = score + self._transitions[self._stop_idx, tags[-1]]
        return score

    def _score_sentence(self, feats_batch, tags_batch, lengths_batch):
        """Get the gold standard of sentences
        Gives the score of a provided tag sequence
        feats_batch dim: [batch_size, seq_len, target_dim]
        tags_batch dim: [batch_size, seq_len]
        lengths_batch dim: [batch_size]
        """
        batch_size = feats_batch.size(0)
        score_batch = []
        for i in range(batch_size):
            score = torch.zeros(1, device=self._device)
            length = lengths_batch[i]
            feats = feats_batch[i][:length]
            tags = tags_batch[i][:length]
            score = self._score_sentence_single(feats, tags)
            score_batch.append(score)
        score = torch.stack(score_batch).view(-1)
        return score

    def _score_sentence_batch(self, feats, tags, lengths, masks): # pylint: disable=too-many-locals
        """Get the gold standard of sentences, batch version
        Gives the score of a provided tag sequence
        feats dim: [batch_size, seq_len, target_dim]
        tags dim: [batch_size, seq_len]
        lengths dim: [batch_size]
        masks dim: [batch_size, seq_len]
        """

        batch_size = feats.size(0)

        score = torch.zeros(batch_size, requires_grad=True, device=self._device)

        start = torch.tensor([ # pylint: disable=not-callable
            self._start_idx
        ], dtype=torch.long, device=self._device).expand(batch_size, 1)

        tags = torch.cat([
            start,
            tags
        ], dim=1)

        # feats dim: [seq_len, batch_size, hidden_dim]
        feats = feats.permute(1, 0, 2)
        for j, feat in enumerate(feats):
            mask = masks[:, j].contiguous().view(batch_size, 1)
            tag_next, tag_cur = tags[:, j + 1], tags[:, j]
            score = score \
                + self._transitions[tag_next, tag_cur] * mask \
                + feat[:, tag_next] * mask

        ends = tags.gather(1, lengths.view(-1, 1))
        trans = self._transitions[self._stop_idx].expand(
            batch_size, self._tagset_size
        ).gather(1, ends.view(-1, 1))
        score = score + trans.view(-1)

        score = score.diag()
        return score

    def _viterbi_decode_single(self, feats): # pylint: disable=too-many-locals
        backpointers = []

        # Initialize the viterbi variables in log space
        init_vvars = torch.full(
            (1, self._tagset_size),
            NO_TRANS,
            device=self._device
        )
        init_vvars[0][self._start_idx] = 0

        # forward_var at step i holds the viterbi variables for step i-1
        forward_var = init_vvars
        for feat in feats:
            bptrs_t = []  # holds the backpointers for this step
            viterbivars_t = []  # holds the viterbi variables for this step

            for next_tag in range(self._tagset_size):
                # next_tag_var[i] holds the viterbi variable for tag i at the
                # previous step, plus the score of transitioning
                # from tag i to next_tag.
                # We don't include the emission scores here because the max
                # does not depend on them (we add them in below)
                next_tag_var = forward_var + self._transitions[next_tag]
                best_tag_id = torch.argmax(next_tag_var, 1)[0]
                bptrs_t.append(best_tag_id)
                viterbivars_t.append(next_tag_var[0][best_tag_id].view(1))
            # Now add in the emission scores, and assign forward_var to the set
            # of viterbi variables we just computed
            forward_var = (torch.cat(viterbivars_t) + feat).view(1, -1)
            backpointers.append(bptrs_t)

        # Transition to STOP_TAG
        terminal_var = forward_var + \
            self._transitions[self._stop_idx]
        best_tag_id = torch.argmax(terminal_var, 1)[0]
        path_score = terminal_var[0][best_tag_id]

        # Follow the back pointers to decode the best path.
        best_path = [best_tag_id]
        for bptrs_t in reversed(backpointers):
            best_tag_id = bptrs_t[best_tag_id]
            best_path.append(best_tag_id)
        # Pop off the start tag (we dont want to return that to the caller)
        start = best_path.pop()
        assert start == self._start_idx  # Sanity check
        best_path.reverse()
        return path_score, best_path

    def _viterbi_decode(self, feats_batch, lengths): # pylint: disable=too-many-locals
        """Inference result
        feats_batch dim: [batch_size, seq_len, target_dim]
        lengths dim: [batch_size]
        """
        batch_size = feats_batch.size(0)
        path_scores, best_paths = [], []
        for i in range(batch_size):
            length = lengths[i]
            feats = feats_batch[i][:length]
            path_score, best_path = self._viterbi_decode_single(feats)
            path_scores.append(path_score)
            best_paths.append(best_path)
        path_scores = torch.stack(path_scores)
        best_paths = np.asarray([
            np.asarray(x)
            for x in best_paths
        ])
        return path_scores, best_paths

    def _viterbi_decode_batch(self, feats, lengths, masks): # pylint: disable=too-many-locals
        """Inference result"""
        # feats dim: [batch_size, seq_len, target_dim]
        batch_size = feats.size(0)

        backpointers = []

        # Initialize the viterbi variables in log space
        # init_vvars dim: [batch_size, tagset_size]
        init_vvars = torch.full(
            (batch_size, self._tagset_size), NO_TRANS,
            device=self._device)
        init_vvars[:, self._start_idx] = 0

        # forward_var at step i holds the viterbi variables for step i-1
        forward_var = init_vvars

        # feats dim: [seq_len, batch_size, target_dim]
        feats = feats.permute(1, 0, 2)
        # feat dim: [batch_size, target_dim]
        bptrs_t = None
        for i, feat in enumerate(feats):
            mask = masks[:, i]
            # bptrs_t_old = bptrs_
            bptrs_t = []  # holds the backpointers for this step
            viterbivars_t = []  # holds the viterbi variables for this step

            for next_tag in range(self._tagset_size):
                # next_tag_var[i] holds the viterbi variable for tag i at the
                # previous step, plus the score of transitioning
                # from tag i to next_tag.
                # We don't include the emission scores here because the max
                # does not depend on them (we add them in below)
                # next_tag_var dim: [batch_size, tagset_size]
                next_tag_var = forward_var + self._transitions[
                    next_tag
                ].view(1, -1).expand(batch_size, self._tagset_size)
                best_tag_id = torch.argmax(next_tag_var, 1)
                bptrs_t.append(best_tag_id.view(1, -1))
                tmp = next_tag_var.gather(1, best_tag_id.view(-1, 1)).squeeze()
                viterbivars_t.append(tmp.view(1, batch_size))
            # Now add in the emission scores, and assign forward_var to the set
            # of viterbi variables we just computed
            # forward_var dim: [batch_size, tagset_size]
            tmp = torch.cat(viterbivars_t)
            tmp = tmp.permute(1, 0)
            tmp_new_forward_var = (tmp + feat).view(batch_size, -1)

            mask_table = mask.view(-1, 1).expand(-1, self._tagset_size)
            forward_var = tmp_new_forward_var * mask_table + forward_var * (mask_table - 1).abs()

            bptrs_t = torch.cat(bptrs_t)

            # if bptrs_t_old is not None:
            #     mask_table = mask.view(1, -1).expand(self._tagset_size, -1).long()
            #     bptrs_t = bptrs_t * mask_table + bptrs_t_old * (mask_table - 1).abs()

            backpointers.append(bptrs_t)

        # Transition to STOP_TAG
        # terminal_var dim: [1, tagset_size]
        terminal_var = forward_var + \
            self._transitions[self._stop_idx]
        best_tag_id = torch.argmax(terminal_var, 1)
        path_score = [
            terminal_var[i][x]
            for i, x in enumerate(best_tag_id)
        ]

        # Follow the back pointers to decode the best path.
        backpointers = torch.stack(backpointers)
        # backpointers dim: [seq_len, batch_size, tagset_size]
        backpointers = backpointers.permute(0, 2, 1)
        # print('backpointers', backpointers.size())
        best_path = [best_tag_id]
        for bptrs_t in reversed(backpointers):
            if batch_size > 1:
                best_tag_id = bptrs_t.gather(1, best_tag_id.view(-1, 1)).squeeze()
                best_path.append(best_tag_id)
            else:
                best_tag_id = bptrs_t[0][best_tag_id]
                best_path.append(best_tag_id)
        # Pop off the start tag (we dont want to return that to the caller)
        # best_path.pop()
        # check start
        start = best_path.pop()
        assert np.sum(
            start.cpu().detach().numpy() - np.array([
                self._start_idx
            ] * batch_size)
        ) <= 1e-5
        best_path.reverse()

        path_score = torch.stack(path_score)
        best_path = torch.stack(best_path)
        best_path = best_path.permute(1, 0).cpu().detach().numpy()
        best_path = np.asarray([
            np.asarray(x[:i])
            for i, x in zip(lengths, best_path)
        ])

        return path_score, best_path

    def _get_char_features(self, chars, is_train):
        assert len(chars.size()) == 3
        batch_size = chars.size(0)
        seq_len = chars.size(1)
        char_len = chars.size(2)
        num = batch_size * seq_len
        chars = chars.view(num, char_len)

        # chars_lengths = (chars == 0).argmax(1)

        # char_feats dim: [num, char_len, char_embedding_size]
        char_feats = self._char_embeds(chars)
        # dropout char embedding
        char_feats = F.dropout(char_feats, p=self._char_dropout_p, training=is_train)

        char_feats = char_feats.permute(1, 0, 2)
        # packed = nn.utils.rnn.pack_padded_sequence(char_feats, chars_lengths, batch_first=True)
        char_feats, _ = self._char_rnn(char_feats)
        # rnn_out, _ = nn.utils.rnn.pad_packed_sequence(rnn_out, batch_first=True)
        char_feats = char_feats.permute(1, 0, 2)

        # char_feats = char_feats.view(
        #     num, 1,
        #     self._char_max_len, self._char_embedding_dim)
        # char_feats = self._char_cnn(char_feats)
        # char_feats = F.relu(char_feats)
        # # char_feats = self._char_pool(char_feats)
        # char_feats = global_max_pooling(char_feats, 2, 3)
        char_feats = char_feats.contiguous().view(batch_size, seq_len, -1)


        # dropout char feats
        char_feats = F.dropout(char_feats, p=self._char_dropout_p, training=is_train)
        return char_feats

    def neg_log_likelihood(self, sentence, tags, lengths, chars=None):
        """Calculate loss
        sentence dim: [batch_size, seq_len, embedding_dim]
        tags dim: [batch_size, seq_len]
        lengths dim: [batch_size]
        """

        char_feats = None
        if chars is not None:
            char_feats = self._get_char_features(chars, is_train=True)

        rnn_feats = self._get_rnn_features(sentence, lengths, char_feats=char_feats, is_train=True)

        seq_len = rnn_feats.size(1)
        masks = sequence_mask(lengths, seq_len)

        forward_score = self._forward_alg_batch(rnn_feats, lengths, masks)
        # forward_score = self._forward_alg(rnn_feats, lengths)
        gold_score = self._score_sentence_batch(rnn_feats, tags, lengths, masks)

        # Old:
        if self._debug:
            forward_score_nonbatch = self._forward_alg(rnn_feats, lengths)
            gold_score_nonbatch = self._score_sentence(rnn_feats, tags, lengths)
            assert torch.sum(forward_score_nonbatch - forward_score) < 1e-4
            assert torch.sum(gold_score_nonbatch - gold_score) < 1e-4

        loss = torch.sum(forward_score) - torch.sum(gold_score)
        # loss = loss / batch_size
        return loss

    def cross_entropy_loss(self, sentence, tags, lengths, chars=None):
        """Softmax"""

        char_feats = None
        if chars is not None:
            char_feats = self._get_char_features(chars, is_train=True)

        rnn_feats = self._get_rnn_features(sentence, lengths, char_feats=char_feats, is_train=True)

        batch_size, seq_len = rnn_feats.size()[:2]
        seq_len = rnn_feats.size(1)
        masks = sequence_mask(lengths, seq_len)
        rnn_feats = rnn_feats * masks.view(batch_size, seq_len, 1)
        tags = tags * masks.long()
        rnn_feats = rnn_feats.view(batch_size * seq_len, -1)
        tags = tags.view(-1)
        return self._cross_entropy_loss(rnn_feats, tags) # / batch_size

    def forward(self, sentence, lengths, chars=None): # pylint: disable=arguments-differ
        """Main forward function, predict only"""

        char_feats = None
        if chars is not None:
            char_feats = self._get_char_features(chars, is_train=False)

        # Get the emission scores from the BiLSTM
        rnn_feats = self._get_rnn_features(sentence, lengths, char_feats=char_feats, is_train=False)
        seq_len = rnn_feats.size(1)
        masks = sequence_mask(lengths, seq_len)

        if self._crf:
            # Find the best path, given the features.
            score, tag_seq = self._viterbi_decode_batch(rnn_feats, lengths, masks)
            if self._debug:
                score_nonbatch, tag_seq_nonbatch = self._viterbi_decode(rnn_feats, lengths)
                assert torch.sum(score_nonbatch - score) < 1e-4
                for taga, tagb in zip(tag_seq, tag_seq_nonbatch):
                    assert np.sum(taga - tagb) < 1e-4

            return score, tag_seq

        scores = rnn_feats.max(dim=2)
        _, pred = torch.max(rnn_feats, dim=2)
        return scores, pred.cpu().detach().numpy()

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
