try:
    from libdual import * 
except:
    try:
        import os
        os.system("cp /usr/local/lib/python2.7/dist-packages/dualdiff/libboost_python-py27.so.1.65.1 /usr/lib/")
        from libdual import *
    except:
        pass

def dual(x, diff=True, hyper=False):
    if hyper:
        return HyperDual(x, diff, diff, 0)
    else:
        return DualNumber(x, diff)

def ans(x):
    return x.real

def der(x):
    if isinstance(x, HyperDual):
        return x.eps1
    elif isinstance(x, DualNumber):
        return x.dual

def sder(x):
    return x.eps1eps2

def grad(f, x):
    res = [0]*len(x)
    for i in range(len(x)):
        x_t = [dual(x[indx], diff=False) for indx in range(len(x))]
        x_t[i] = dual(x[i])
        res[i] = der(f(x_t))
    return res
