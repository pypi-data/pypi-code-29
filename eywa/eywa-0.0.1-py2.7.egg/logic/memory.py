from ..lang import Document
from ..math import euclid_similarity, vector_sequence_similarity
from ..lang import stop_words
import numpy as np


class Memory(object):

    def __init__(self):
        self.docs = []
        self.weights = np.array([0.5, .1, .1, 1., .0])

    def add(self, x):
        if type(x) in (tuple, list):
            self.docs += [Document(i) for i in x]
        else:
            self.docs.append(Document(x))

    def clear(self):
        self.docs = []

    def ask(self, q):
        q = Document(q)
        docs = self.docs
        sim = self.similarity
        best_doc = max(docs, key=lambda x: sim(q, x))
        ans = self.extract_answer(q, best_doc)
        return ans, best_doc
        ##
        candidates = [d[0] for d in enumerate(docs) if sim(q, d[1]) > 0]
        ext = self.extract_answer
        answers = [ext(q, docs[i]) for i in candidates]
        for i in range(len(answers) - 1, -1, -1):
            ans = answers[i]
            if ans:
                return ans, docs[candidates[i]]
        return None

    def _similarity(self, x1, x2):
        #if x1 == x2:
        #    return 1
        if len(x1) == 0 or len(x2) == 0:
            return 0
        score1 = lambda : euclid_similarity(x1.embedding, x2.embedding)
        score2 = lambda : np.dot(x1.embedding, x2.embedding)
        score3 = lambda : vector_sequence_similarity(x1.embeddings, x2.embeddings, self.weights[0], 'dot')
        score4 = lambda : vector_sequence_similarity(x1.embeddings, x2.embeddings, self.weights[0], 'euclid')
        scores = [score1, score2, score3, score4]
        score_weights = self.weights[1:5]
        score = 0.
        for s, w in zip(scores, score_weights):
            if w > 0.05:
                score += s()
        return score * 0.25
    def similarity(self, x, y):
        # for now we simply count common words
        if not len(x):
            return 0
        if not len(y):
            return 0
        sim = 0.
        for wx in x:
            for wy in y:
                if wx not in stop_words and wy not in stop_words:
                    sim += np.dot(wx.embedding, wy.embedding)
        sim *= (2. / (len(x) + len(y)))
        return sim

    def extract_answer(self, q, d):
        answers = []
        for w in d:
            if w not in q and w not in stop_words:
                answers.append(w)
        return min(answers, key=lambda x: x.frequency)
        