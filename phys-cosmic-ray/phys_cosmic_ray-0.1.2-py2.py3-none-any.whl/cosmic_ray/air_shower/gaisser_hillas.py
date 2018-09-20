import numpy

def gaisser_hillas(x,p):
    """
    parameters (p0, p1, p2, p3) are (Nmax, Xmax, X0, lambda)
    p0 * ((x-p2)/(p1-p2))^((p1-p2)/p3) * \exp((p1-x)/p3)
    """
    x = numpy.atleast_1d(x)
    n = numpy.zeros_like(x)
    n[x>p[2]] = p[0]*((x[x>p[2]]-p[2])/(p[1]-p[2]))**((p[1]-p[2])/p[3])*numpy.exp((p[1]-x[x>p[2]])/p[3])
    return n
