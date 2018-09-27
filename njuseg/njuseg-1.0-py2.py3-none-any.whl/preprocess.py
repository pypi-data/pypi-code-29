import numpy as np


class Sent(object):
    cUNK = 'UNK'

    def __init__(self, char_seq, spans=None, words=None):
        self.m_char_seq = char_seq
        if spans is not None:
            self.m_spans = spans

            self.m_labels = []
            for s in spans:
                self.m_labels.append('NA')
                for i in range(s[1]-s[0]):
                    self.m_labels.append('AP')

        if words is not None:
            self.m_words = words
        self.m_bigram_seq = self.bigrams()
        self.clen = len(self.m_char_seq)

    def unigrams(self):
        return self.m_char_seq

    def bigrams(self):
        bigrams = []
        pre_unigrams = '<S>'
        for c in self.m_char_seq:
            bigrams.append(pre_unigrams + c)
            pre_unigrams = c
        bigrams.append(pre_unigrams + '</S>')

        return bigrams

    def words(self):
        return self.m_words

    @staticmethod
    def from_file(filename):
        sents = []
        with open(filename, 'r', encoding='utf-8') as f:
            for line in f.readlines():
                # string = unicode(line.decode('utf-8'))
                string = line
                char_seq = []
                words = string.split()
                for w in words:
                    for c in w:
                        char_seq.append(c)

                spans = []
                left = 1
                right = 1
                for w in words:
                    right += len(w)-1
                    spans.append((left, right))
                    left = right + 1
                    right = left
                sent = Sent(char_seq, spans, words)
                sents.append(sent)
        return sents

    @staticmethod
    def from_raw(filename):
        sents = []
        with open(filename, 'r', encoding='utf-8') as f:
            for line in f.readlines():
                # string = unicode(line.decode('utf-8'))
                string = line
                char_seq = []
                for c in string:
                    char_seq.append(c)
                sent = Sent(char_seq)
                sents.append(sent)
        return sents

    def char_seq(self):
        seq = []
        words = self.m_string.split()
        for w in words:
            for c in w:
                seq.append(c)
        return seq

    def feature_seq(self, fm):
        feature_seq = []
        padding_char_seq = ['<S>'] + self.m_char_seq + ['</S>']
        bigram_seq = self.m_bigram_seq

        for i in range(self.clen):
            pre_u = padding_char_seq[i]
            u = padding_char_seq[i+1]
            pos_u = padding_char_seq[i+2]

            pre_bi = bigram_seq[i]
            pos_bi = bigram_seq[i+1]

            f = {}
            f['pre_u'] = fm['unigram_idx_map'].get(pre_u, 0)
            f['u'] = fm['unigram_idx_map'].get(u, 0)
            f['pos_u'] = fm['unigram_idx_map'].get(pos_u, 0)
            f['pre_bi'] = fm['bigram_idx_map'].get(pre_bi, 0)
            f['pos_bi'] = fm['bigram_idx_map'].get(pos_bi, 0)

            dic_feature = 0
            dic_feature += 16*(1 if pre_u in fm['words_vocab'] else 0)
            dic_feature += 8*(1 if pre_u in fm['words_vocab'] else 0)
            dic_feature += 4*(1 if u in fm['words_vocab'] else 0)
            dic_feature += 2*(1 if pre_bi in fm['words_vocab'] else 0)
            dic_feature += 1*(1 if pos_bi in fm['words_vocab'] else 0)
            f['dic_feature'] = dic_feature

            feature_seq.append(f)
        return feature_seq

    def get_UNKed(self, fm, unk_params):

        for i in range(len(self.m_char_seq)):
            u_freq = fm['unigram_freq'][self.m_char_seq[i]]
            drop_prob = unk_params / (unk_params + u_freq)
            r = np.random.random()
            if r < drop_prob:
                self.m_char_seq[i] = Sent.cUNK

        for i in range(len(self.m_bigram_seq)):
            b_freq = fm['bigram_freq'][self.m_bigram_seq[i]]
            drop_prob = unk_params / (unk_params + b_freq)
            r = np.random.random()
            if r < drop_prob:
                self.m_bigram_seq[i] = Sent.cUNK

    def label2idx(self, labels):
        return [['NA', 'AP'].index(l) for l in labels]

    def eval(self, pred):
        gold_spans = self.m_spans
        pred_spans = pred.m_spans

        n_pred_words = len(pred_spans)
        n_gold_words = len(gold_spans)

        n_right_words = 0
        for ps in gold_spans:
            if ps in pred_spans:
                n_right_words += 1
        return FScore(correct=n_right_words, predcount=n_pred_words, goldcount=n_gold_words)

    def seg_string(self):
        padded_char_seq = ['<S>'] + self.m_char_seq + ['</S>']
        s = ''
        for left, right in self.m_spans:
            if left == right:
                s += padded_char_seq[left]
            else:
                for index in range(left, right+1):
                    s += padded_char_seq[index]
            s += ' '

        return s


class FScore(object):

    def __init__(self, correct=0, predcount=0, goldcount=0):
        self.correct = correct
        self.predcount = predcount
        self.goldcount = goldcount

    def precision(self):
        if self.predcount > 0:
            return (100.0 * self.correct) / self.predcount
        else:
            return 0.0

    def recall(self):
        if self.goldcount > 0:
            return (100.0 * self.correct) / self.goldcount
        else:
            return 0.0

    def fscore(self):
        precision = self.precision()
        recall = self.recall()
        if (precision + recall) > 0:
            return (2 * precision * recall) / (precision + recall)
        else:
            return 0.0

    def __str__(self):
        precision = self.precision()
        recall = self.recall()
        fscore = self.fscore()
        return '(P = {:0.2f}, R = {:0.2f}, F = {:0.2f})'.format(
            precision,
            recall,
            fscore
        )

    def __iadd__(self, other):
        self.correct += other.correct
        self.predcount += other.predcount
        self.goldcount += other.goldcount
        return self

    def __cmp__(self, other):
        return cmp(self.fscore, other.fscore)

    def __add__(self, other):
        return FScore(self.correct + other.correct,
                      self.predcount + other.predcount,
                      self.goldcount + other.goldcount)


def init_map_from_file(filename, thr=5., dic_file_name=None):
    from collections import OrderedDict
    unigrams_freq = OrderedDict()
    bigrams_freq = OrderedDict()
    words_freq = OrderedDict()

    sents = Sent.from_file(filename)
    for sent in sents:
        for u in sent.unigrams():
            if u in unigrams_freq:
                unigrams_freq[u] += 1
            else:
                unigrams_freq[u] = 1

        for b in sent.bigrams():
            if b in bigrams_freq:
                bigrams_freq[b] += 1
            else:
                bigrams_freq[b] = 1

        for w in sent.words():
            if w in words_freq:
                words_freq[w] += 1
            else:
                words_freq[w] = 1

    bigrams_vocab = []
    unigrams_vocab = []
    words_vocab = set()
    for u in unigrams_freq:
        unigrams_vocab.append(u)
    for b in bigrams_freq:
        bigrams_vocab.append(b)

    for w in words_freq:
        words_vocab.add(w)

    unigrams_idx_map = {'<S>': 1, '</S>': 2}
    bigrams_idx_map = {}
    idx = 3
    for u in unigrams_vocab:
        unigrams_idx_map[u] = idx
        idx += 1
    idx = 1
    for b in bigrams_vocab:
        bigrams_idx_map[b] = idx
        idx += 1
    return {
        'unigram_idx_map': unigrams_idx_map,
        'bigram_idx_map': bigrams_idx_map,
        'unigram_size': len(unigrams_vocab) + 3,
        'bigram_size': len(bigrams_vocab) + 1,
        'unigram_freq': unigrams_freq,
        'bigram_freq': bigrams_freq,
        'words_vocab': words_vocab, }
