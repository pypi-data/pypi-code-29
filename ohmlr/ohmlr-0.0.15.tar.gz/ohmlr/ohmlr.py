from numpy import matlib
import matplotlib.pyplot as plt
import numpy as np
from scipy.sparse.linalg import svds
from scipy.sparse import csc_matrix


class ohmlr(object):
    def __init__(self, tol=1e-4, max_iter=100):
        self.tol = tol
        self.max_iter = max_iter

    # decision_function(X)	Predict confidence scores for samples.

    def categorize_(self, u):
        u_map = {s: i for i, s in enumerate(np.unique(u))}
        u_int = np.asarray([u_map[ui] for ui in u])
        return u_int, u_map

    def predict_proba(self, x):
        n_features = self.n_features
        v = self.v
        w = self.w
        x_map = self.x_map

        x = np.asarray(x)
        n_samples = x.shape[0]
        x_int = np.asarray(
            [[x_map[j][xij] for j, xij in enumerate(xi)] for xi in x])
        h = v + np.asarray([
            np.sum([w[j][x_int[i, j]] for j in range(n_features)], 0)
            for i in range(n_samples)
        ])
        p = np.exp(h)
        p /= p.sum(1)[:, np.newaxis]
        return p

    def predict_log_proba(self, x):
        return np.log(self.predict_proba(x))

    def predict(self, x):
        y_map = self.y_map

        p = self.predict_proba(x)
        y_int = p.argmax(1)
        y = np.asarray([y_map[yi] for yi in y_int])
        return y

    def score(self, x, y):
        return (self.predict(x) == y).mean()

    def fit(self, x, y):

        tol = self.tol
        max_iter = self.max_iter

        x = np.asarray(x)
        y = np.asarray(y)
        n_samples, n_features = x.shape

        tmp = [self.categorize_(xi) for xi in x.T]
        x_int = np.asarray([t[0] for t in tmp]).T
        x_map = [t[1] for t in tmp]

        n_x_classes = np.asarray([len(m) for m in x_map])
        n_x_classes_sum = np.sum(n_x_classes)
        n_x_classes_cumsum = np.insert(n_x_classes.cumsum(), 0, 0)

        # one-hot encoding of x
        x_oh = csc_matrix((np.ones(n_samples * n_features), (np.repeat(
            np.arange(n_samples),
            n_features), (x_int + n_x_classes_cumsum[:-1]).flatten())))

        y_int, y_map = self.categorize_(y)

        n_y_classes = len(y_map)

        # one-hot encoding of y
        y_oh = csc_matrix((np.ones(n_samples), (np.arange(n_samples), y_int)))
        # 'cold' classes
        y_cold = ~(y_oh.toarray().astype(bool))

        i1i2 = np.stack([n_x_classes_cumsum[:-1], n_x_classes_cumsum[1:]]).T

        v = matlib.zeros(n_y_classes)
        w = matlib.zeros((n_x_classes_sum, n_y_classes))

        def solve1(u, pinv):
            w = pinv[2].dot(u)
            w = np.multiply(pinv[1], w)
            w = pinv[0] * w
            return w

        def solve2(u, pinv):
            return solve1(x_oh.T * u, pinv)

        if x_oh.shape[0] > x_oh.shape[1]:
            solve = solve1
            z = x_oh
        else:
            solve = solve2
            z = x_oh.T * x_oh

        # SVD-based solve of x_oh * w = h
        svd = svds(z, k=n_x_classes_sum - n_features + 1)
        sv_pinv = svd[1].copy()
        zero_sv = np.isclose(sv_pinv, 0)
        sv_pinv[zero_sv] = 0.0
        sv_pinv[~zero_sv] = 1.0 / sv_pinv[~zero_sv]
        pinv = (svd[2].T, sv_pinv[:, np.newaxis], svd[0].T)

        # discrepancy
        d = [1.0 / float(n_y_classes)**2 + 1]

        for it in range(1, max_iter):

            h0 = v
            h1 = x_oh * w
            p = np.exp(h0 + h1)
            p /= p.sum(1)

            # additive update
            dh = y_oh - p
            v = (h0 + dh).mean(0)
            w = solve(h1 + dh, pinv)

            v -= v.mean()
            w -= w.mean(1)
            for i1, i2 in i1i2:
                w[i1:i2] -= w[i1:i2].mean(0)

            # discrepancy: avg 2-norm squared of cold entries
            d.append(np.power(p[y_cold], 2).mean())

        v = np.asarray(v)
        w = np.array([np.asarray(w[i1:i2]) for i1, i2 in i1i2])
        d = d[1:]

        self.n_samples = n_samples
        self.n_features = n_features
        self.n_x_classes = n_x_classes
        self.n_y_classes = n_y_classes
        self.x = x
        self.x_int = x_int
        self.x_map = x_map
        self.x_oh = x_oh
        self.y = y
        self.y_int = y_int
        self.y_map = y_map
        self.y_oh = y_oh
        self.pinv = pinv
        self.v = v
        self.w = w
        self.d = d
        return self

    def random(self, n_features, n_x_classes, n_y_classes):
        v = np.random.normal(size=n_y_classes)
        w = np.array(
            [np.random.normal(size=(n, n_y_classes)) for n in n_x_classes])
        v -= v.mean()
        for i in range(n_features):
            w[i] -= w[i].mean(0)
            w[i] -= w[i].mean(1)[:, np.newaxis]

        self.n_features = n_features
        self.n_x_classes = n_x_classes
        self.n_y_classes = n_y_classes
        self.v = v
        self.w = w
        return self

    def generate_data(self, n_samples):

        n_features = self.n_features
        v = self.v
        w = self.w
        n_x_classes = self.n_x_classes
        n_y_classes = self.n_y_classes

        x = np.hstack([
            np.random.randint(n, size=(n_samples, 1), dtype=int)
            for n in n_x_classes
        ])
        h = v + np.array([
            np.sum([w[j][x[i, j]] for j in range(n_features)], 0)
            for i in range(n_samples)
        ])
        p = np.exp(h)
        p /= p.sum(1)[:, np.newaxis]
        y = (p.cumsum(1) < np.random.uniform(size=(n_samples, 1))).sum(1)

        return x, y
