import numpy as np
from beluga.ivpsol import Propagator
from beluga.bvpsol.algorithms import Shooting
from beluga.bvpsol import Solution
tol = 1e-3
pi = np.pi


def odefun(t, x, p, const, arc):
    return -x[1], x[0]


def quadfun(t, x, p, const, arc):
    return x[0]


def bcfun(t0, X0, q0, tf, Xf, qf, params, aux):
    return X0[0], X0[1] - 1, qf[0] - 1.0 + params[0]


algo = Shooting(odefun, quadfun, bcfun)
solinit = Solution()
solinit.t = np.linspace(0, np.pi / 2, 2)
solinit.y = np.array([[1, 0], [1, 0]])  # Ends at [0, 1] # q is y[:,1]
solinit.q = np.array([[0], [0]])
solinit.parameters = np.array([0])
out = algo.solve(solinit)

