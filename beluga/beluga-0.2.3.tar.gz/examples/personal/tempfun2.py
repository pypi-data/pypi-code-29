from beluga.liepack.domain.liealgebras import so, rn
from beluga.liepack import Adjoint, Commutator, exp
import numpy as np
a = so(3)
b = so(3)
c = so(3)

x = rn(3)
y = rn(3)
z = rn(3)

x.set_vector([1,0,0])
y.set_vector([0,1,0])
z.set_vector([0,0,1])

a.set_vector([1,0,0])
b.set_vector([0,1,0])
c.set_vector([0,0,1])

X = exp(x)

print(X.data)

# X = exp(y*np.pi/2)
# print(x.get_vector())
# print(X.data)
#
# Ad = Adjoint(X)
#
# print(Ad(x).get_vector())

# y.set_vector([0,1,0,1])

# print((x*y).get_vector())

from fractions import Fraction as R

def choose(n, k):
    """
    chosen / adapted from:

    http://www.velocityreviews.com/forums/t502438-combination-function-in-python.html
    """
    ntok = 1
    for t in range(min(k, n-k)):
        ntok = ntok*(n-t)//(t+1)
    return ntok

def Bernoulli():
    """
    Bernoulli Numbers using Fraction type numbers
    http://en.wikipedia.org/wiki/Bernoulli_number#Recursive_definition
    http://oeis.org/A027641
    http://oeis.org/A027642
    """
    B = [R(1,1)]

    def Sum(m):
        total = R(0,1)
        for k in range(0,m):
            total +=  choose(m, k) * R(B[k],m-k+1)
        return 1 - total

    m = 1
    while True:
        B.append(Sum(m))
        yield B[-1]
        m += 1

thegen = Bernoulli()
print(next(thegen))
print(next(thegen))
