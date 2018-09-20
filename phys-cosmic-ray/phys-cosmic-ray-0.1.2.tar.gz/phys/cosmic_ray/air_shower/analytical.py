from phys import units
import numpy
import scipy

b = 0.0135
sigma_0 = 7./9 - b/3

gamma = 0
electron = 1

def age(t, tmax):
    return 3*t/(t + 2*tmax)

def A(s):
    return (2*b + 4./3)*(scipy.special.digamma(1+s) + units.kEuler) -  s*(7 + 5*s + 12*b*(2+s))/(6*(1+s)*(2+s))

def B(s):
    return 2*(14+11*s+3*s**2-6*b*(1+s))/(3*(1+s)*(2+s)*(3+s))

def C(s):
    return (8+7*s+3*s**2+6*b*(2+s))/(3*s*(2+3*s+s**2))

def Lambda_1(s):
    return (-(A(s) + sigma_0) + numpy.sqrt((A(s) - sigma_0)**2 + 4*B(s)*C(s)))/2
def Lambda_2(s):
    return (-(A(s) + sigma_0) - numpy.sqrt((A(s) - sigma_0)**2 + 4*B(s)*C(s)))/2

def lambda_1(s):
    return (s-1-3*numpy.log(s))/2

#def r_gamma_e(s):
#    return C(s)/(sigma_0+lambda_1(s))

_g_ = {
        (1,1): lambda s: (sigma_0 + Lambda_1(s))/(Lambda_1(s)-Lambda_2(s)),
        (1,0): lambda s: C(s)/(Lambda_1(s)-Lambda_2(s)),
        (0,1): lambda s: -(1/C(s))*(sigma_0 + Lambda_1(s))(sigma_0 + Lambda_2(s))/(Lambda_1(s)-Lambda_2(s)),
        (0,0): lambda s: (sigma_0 + Lambda_2(s))/(Lambda_1(s)-Lambda_2(s)),
}

_m_ = {
        (1,1): 0
        (1,0): -0.5
        (0,1): -0.5
        (0,0): 0
}

def G(primary, secondary, s):
    return _g_[primary, decondary](s)

def n_approx_a(primary, secondary, E0, t, E):
    s = 3*t/(t - 2*numpy.log(E/E0))
    return (1./E0/numpy.sqrt(2*numpy.pi))*(G(primary, secondary, s)/numpy.sqrt((3*t-_m_[(primary, secondary)])/s**2))*(E/E0)**(-(s+1))*numpy.exp(lambda_1(s)*t)

# approx B one of these days...
