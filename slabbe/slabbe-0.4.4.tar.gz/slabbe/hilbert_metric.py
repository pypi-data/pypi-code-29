import itertools
from sage.functions.log import log
from sage.rings.infinity import Infinity
from sage.modules.free_module_element import vector
from collections import defaultdict


def hilbert_metric(v,w):
    r"""

    EXAMPLES::

        sage: hilbert_metric([1,2,3], [1,1,1])
        log(3)
        sage: hilbert_metric([1,2,3], [1,1,0])
        +Infinity

    """
    assert len(v) == len(w)
    indices = range(len(v))
    if any(a < 0 for a in v) or any(a < 0 for a in w):
        raise ValueError('defined only for nonnegative coordinates')
    if any(a == 0 for a in v) or any(a == 0 for a in w):
        return Infinity
    return max(log((v[i]*w[j]) / (v[j]*w[i])) 
               for i,j in itertools.product(indices, repeat=2))

def hilbert_metric_arg_max(v,w):
    r"""

    EXAMPLES::

        sage: hilbert_metric_arg_max([1,2,3], [1,1,1])
        (2, 0)

    """
    assert len(v) == len(w)
    indices = range(len(v))
    if any(a < 0 for a in v) or any(a < 0 for a in w):
        raise ValueError('defined only for nonnegative coordinates')
    if any(a == 0 for a in v) or any(a == 0 for a in w):
        raise NotImplementedError
    L = list(itertools.product(indices, repeat=2))
    #s = sorted(L, key=lambda t:log((v[t[0]]*w[t[1]]) / (v[t[1]]*w[t[0]])), reverse=True)
    #if s[0] == s[1]:
    #    print "yo"
    return max(L, key=lambda t:log((v[t[0]]*w[t[1]]) / (v[t[1]]*w[t[0]])))

def plot_regions(n, M=None):
    r"""

    EXAMPLES::

        sage: plot_regions(10000)

    """
    d = 3
    if M is None:
        M = identity_matrix(d)
    indices = range(d)
    L = list(itertools.product(indices, repeat=2))
    def trans(x):
        return 2-2/(x+1)
    P = defaultdict(list)
    Q = defaultdict(list)
    for _ in range(n):
        v = vector([random() for _ in range(d)])
        w = vector([random() for _ in range(d)])
        Mv = M*v
        Mw = M*w
        arg = hilbert_metric_arg_max(Mv,Mw)
        a,b,c = v
        ap,bp,cp = w
        x = trans(a * cp / (ap * c))
        y = trans(b * cp / (bp * c))
        P[arg].append( (x,y) )
        Q[arg].append( hilbert_metric(Mv,Mw) / hilbert_metric(v,w))
    G = Graphics()
    color_dict = dict(zip(P.keys(), rainbow(len(P))))
    for key in P:
        G += points(P[key], color=color_dict[key])
    for i,key in enumerate(Q):
        G += text("{}:{}".format(key, max(Q[key])), (2,1+i/10.),
                color=color_dict[key], horizontal_alignment='left')
    return G

def contraction_factor(M):
    r"""
    """
    dx,dy = M.dimensions()
    assert dx == dy
    d = dx
    v = vector([random() for _ in range(d)])
    w = vector([random() for _ in range(d)])
    print "v=",v
    print "w=",w
    print "M*v=",M*v
    print "M*w=",M*w
    h = hilbert_metric(v,w)
    print "d(v,w)=",h
    Mh = hilbert_metric(M*v,M*w)
    print "d(Mv,Mw)=",Mh
    return Mh/h

def contraction_factor(M, verbose=False):
    r"""
    EXAMPLES::

        sage: M = matrix(3,3,range(9))
        sage: contraction_factor(M)
        (0.25136420887239963,
         (1.0222576147041504, 1.0116592356864682, 2.9845190561103863, 4.021533594865607, 3.9802754613362716, 4.8679086019143885))

    """
    dx,dy = M.dimensions()
    assert dx == dy
    d = dx
    from sage.modules.free_module_element import vector
    from sage.numerical.optimize import minimize_constrained
    def func(arg):
        v = vector(arg[:d])
        w = vector(arg[d:])
        if any(a<0 for a in v) or any(a<0 for a in w):
            return 0
        h = hilbert_metric(v,w)
        Mh = hilbert_metric(M*v,M*w)
        if h == 0:
            return Infinity
        else:
            return -Mh/h
    cons = [lambda z: z[i] for i in range(2*d)]
    x0 = [random() for _ in range(2*d)]
    rep = minimize_constrained(func, cons, x0)
    v = vector(rep[:d])
    v /= min(v)
    w = vector(rep[d:])
    w /= min(w)
    if verbose:
        print("M=")
        print(M)
        print("v={}".format(v))
        print("w={}".format(w))
        print(-func(rep))
    return -func(rep), rep

def test(k):
    a = random()
    b = random()
    ap = random()
    bp = random()
    print a,b,ap,bp
    ratio = (a+b+1) / (ap+bp+1)
    ratiok = (k*(a+b+1)+b) / (k*(ap+bp+1)+bp)
    L = [ratio, ratiok, 1/ratiok, 1/ratio]
    indices = range(4)
    indices.sort(key=lambda val:L[val])
    print L
    return indices

    


