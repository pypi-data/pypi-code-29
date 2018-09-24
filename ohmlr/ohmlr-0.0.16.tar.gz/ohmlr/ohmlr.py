from numpy import matlib
import matplotlib.pyplot as plt
import numpy as np
from scipy.sparse.linalg import svds
from scipy.sparse import csc_matrix


class ohmlr(object):
    def __init__(self, x_classes=None, y_classes=None, random_coeff=False):
        self.x_classes = x_classes
        self.y_classes = y_classes
        self.random_coeff = random_coeff

        if x_classes is not None and y_classes is not None:
            n_y_classes = len(y_classes)
            n_features = len(x_classes)
            n_x_classes = np.asarray([len(x_class) for x_class in x_classes])
            n_x_classes_sum = np.sum(n_x_classes)
            y_map = {s: i for i, s in enumerate(np.sort(y_classes))}
            x_map = [{s: i
                      for i, s in enumerate(np.sort(x_class))}
                     for x_class in x_classes]

            if random_coeff:
                v = np.random.normal(size=n_y_classes)
                w = np.array([
                    np.random.normal(size=(n, n_y_classes))
                    for n in n_x_classes
                ])
                v -= v.mean()
                for i in range(n_features):
                    w[i] -= w[i].mean(0)
                    w[i] -= w[i].mean(1)[:, np.newaxis]
            else:
                v = np.zeros(n_y_classes)
                w = np.array(
                    [np.zeros(shape=(n, n_y_classes)) for n in n_x_classes])
            self.n_y_classes = n_y_classes
            self.n_features = n_features
            self.n_x_classes = n_x_classes
            self.n_x_classes_sum = n_x_classes_sum
            self.x_map = x_map
            self.y_map = y_map
            self.v = v
            self.w = w

    # decision_function(X)	Predict confidence scores for samples.

    def categorize_(self, u, u_classes):
        if u_classes is None:
            u_classes = np.unique(u)
        u_map = {s: i for i, s in enumerate(u_classes)}
        u_int = np.asarray([u_map[ui] for ui in u])
        return u_int, u_map

    def predict_proba(self, x, return_weights=False):
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
        h = np.asarray(h)
        p = np.exp(h)
        p /= p.sum(1)[:, np.newaxis]
        if return_weights:
            return p, h
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

    def fit(self,
            x,
            y,
            atol=1e-4,
            rtol=1e-3,
            max_iter=500,
            v_init=None,
            w_init=None):

        x = np.asarray(x)
        y = np.asarray(y)
        n_samples, n_features = x.shape

        x_classes = self.x_classes
        y_classes = self.y_classes

        if x_classes is None:
            x_classes = n_features * [None]
        elif np.asarray(x_classes).ndim == 1:
            x_classes = np.tile(
                np.asarray(x_classes)[:, np.newaxis], n_features).T

        tmp = [self.categorize_(xi, ci) for xi, ci in zip(x.T, x_classes)]
        x_int = np.asarray([t[0] for t in tmp]).T
        x_map = [t[1] for t in tmp]

        n_x_classes = np.asarray([len(m) for m in x_map])
        n_x_classes_sum = np.sum(n_x_classes)
        n_x_classes_cumsum = np.insert(n_x_classes.cumsum(), 0, 0)

        # one-hot encoding of x
        x_oh = csc_matrix((np.ones(n_samples * n_features),
                           (np.repeat(np.arange(n_samples), n_features),
                            (x_int + n_x_classes_cumsum[:-1]).flatten())),
                          shape=(n_samples, n_x_classes_sum))

        y_int, y_map = self.categorize_(y, y_classes)

        n_y_classes = len(y_map)

        # one-hot encoding of y
        y_oh = csc_matrix((np.ones(n_samples), (np.arange(n_samples), y_int)))
        # 'cold' classes
        y_hot = (y_oh.toarray().astype(bool))
        y_cold = ~(y_oh.toarray().astype(bool))

        i1i2 = np.stack([n_x_classes_cumsum[:-1], n_x_classes_cumsum[1:]]).T

        if v_init is None:
            v = matlib.zeros(n_y_classes)
        else:
            v = np.asmatrix(v_init)
        if w_init is None:
            w = matlib.zeros((n_x_classes_sum, n_y_classes))
        else:
            w = np.asmatrix(np.vstack(w_init))

        def solve1(u, pinv):
            w = pinv[2].dot(u)
            w = np.multiply(pinv[1], w)
            w = pinv[0] * w
            return w

        def solve2(u, pinv):
            return solve1(x_oh.T * u, pinv)

        if x_oh.shape[0] < x_oh.shape[1]:
            solve = solve1
            z = x_oh
            k = x_oh.shape[0] - 1
        else:
            solve = solve2
            z = x_oh.T * x_oh
            k = n_x_classes_sum - n_features + 1

        # SVD-based solve of x_oh * w = h
        svd = svds(z, k=k)
        sv_pinv = svd[1].copy()
        zero_sv = np.isclose(sv_pinv, 0)
        sv_pinv[zero_sv] = 0.0
        sv_pinv[~zero_sv] = 1.0 / sv_pinv[~zero_sv]
        pinv = (svd[2].T, sv_pinv[:, np.newaxis], svd[0].T)

        # discrepancy
        disc = [1.0 / float(n_y_classes)**2 + 1]
        err = [1.0 / float(n_y_classes)**2 + 1]
        ll = []

        for it in range(1, max_iter + 1):

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
            disc.append(np.power(p[y_cold], 2).mean())
            err.append((np.asarray(dh)**2).sum(1).mean(0))
            ll.append(-np.log(p[y_hot]).mean())

            # if disc[-1] > disc[-2]:
            #     # print('DISC BREAK !!!!!!', it, '!!!!!!!!!!!!')
            #     break

            # if np.abs(err[-1] - err[-2]) < atol:
            #     # print('AERR BREAK !!!!!!', it, '!!!!!!!!!!!!')
            #     break

            # if np.abs(err[-1] - err[-2]) / err[-2] < rtol:
            #     # print('RERR BREAK !!!!!!', it, '!!!!!!!!!!!!')
            #     break

        # if it == max_iter:
        #     # print('NO BREAKKKKKK', it)

        v = np.asarray(v).squeeze()
        w = np.array([np.asarray(w[i1:i2]) for i1, i2 in i1i2])
        disc = disc[1:]
        err = err[1:]

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
        self.disc = disc
        self.err = err
        self.ll = ll

    # def random(self, n_features=None, n_x_classes=None, n_y_classes=None):

    #     if self.x_classes is not None:
    #         n_features = len(self.x_classes)
    #         n_x_classes = [len(x_class) for x_class in self.x_classes]
    #     if self.y_classes is not None:
    #         n_y_classes = len(self.y_classes)

    #     v = np.random.normal(size=n_y_classes)
    #     w = np.array(
    #         [np.random.normal(size=(n, n_y_classes)) for n in n_x_classes])
    #     v -= v.mean()
    #     for i in range(n_features):
    #         w[i] -= w[i].mean(0)
    #         w[i] -= w[i].mean(1)[:, np.newaxis]

    #     self.n_features = n_features
    #     self.n_x_classes = n_x_classes
    #     self.n_y_classes = n_y_classes
    #     self.v = v
    #     self.w = w
    #     return self

    def generate_data(self, n_samples):

        n_features = self.n_features
        n_x_classes = self.n_x_classes
        n_y_classes = self.n_y_classes
        v = self.v
        w = self.w

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

    def get_params(self, deep=True):
        return dict(
            x_classes=self.x_classes,
            y_classes=self.y_classes,
            random_coeff=self.random_coeff)
