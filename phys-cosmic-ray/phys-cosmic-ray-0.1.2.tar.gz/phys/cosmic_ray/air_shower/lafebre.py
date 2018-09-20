

import numpy
import scipy.interpolate
from phys import units

X0 = 36.7*units.g/units.cm**2

electron = -1
positron = 1
total = 0

_A1 = {
    electron: lambda t: 0.485*numpy.exp(0.183*t - 8.17e-4*t**2),
    positron: lambda t: 0.516*numpy.exp(0.201*t - 5.42e-4*t**2),
    total:    lambda t: numpy.exp(0.191*t - 6.91e-4*t**2)
}

_epsilon_1 = {
    electron: lambda t: (3.22 - 0.0068*t)*units.MeV,
    positron: lambda t: (4.36 - 0.0663*t)*units.MeV,
    total:    lambda t: (5.64 - 0.0663*t)*units.MeV
}

_epsilon_2 = {
    electron: lambda t: (106 - 1.00*t)*units.MeV,
    positron: lambda t: (143 - 0.15*t)*units.MeV,
    total:    lambda t: (123 - 0.70*t)*units.MeV
}

_gamma_1 = {
    electron: 1,
    positron: 2,
    total:    1
}

_gamma_2 = {
    electron: lambda t: 1 + 0.0372*t,
    positron: lambda t: 1 + 0.0374*t,
    total:    lambda t: 1 + 0.0374*t
}

def stage(X, Xmax):
    return (X-Xmax)/X0


def electron_distribution(E, t, code=total):
    return _A1[code](t)*E/(E+_epsilon_1[code](t))**_gamma_1[code]/(E+_epsilon_2[code](t))**_gamma_2[code](t)


def theta_distribution(theta, E, t):
    """
    This gives n(t,E,\theta), theta in radians.

    \frac{dN}{dOmega} = n(t,E,\theta)/sin(\theta)
    """
    theta = theta/units.deg
    E = E/units.MeV
    b1 = -3.73 + 0.92*E**0.210
    b2 = 32.9 - 4.84*numpy.log(E)
    alpha1 = -0.399
    alpha2 = -8.36 + 0.440*numpy.log(E)
    sigma = 3
    return ((numpy.exp(b1)*theta**alpha1)**(-1./sigma) + (numpy.exp(b2)*theta**alpha2)**(-1./sigma))**-sigma

def phi_distribution(phi, E, t):
    """
    phi in radians
    """
    E = E/units.MeV
    phi = theta/units.deg
    lambda0 = 0.329 - 0.0174*t + 0.669*numpy.log(E) - 0.0474*numpy.log(E)**2
    lambda1 = 8.10e-3 + 2.79e-3*numpy.log(E)
    lambda2 = 1.10e-4 - 1.14e-5*numpy.log(E)
    return 1 + numpy.exp(lambda0 - lambda1*phi - lambda2*phi**2)



def lateral_distribution(x, E, t):
    """
    x defined as r/r_moliere, where r_moliere ~ \frac{\rho_A(h)}{9.6 g/cm2}
    """
    E = E/units.MeV
    x1 = 0.859- 0.0461 *numpy.log(E)**2 + 0.00428 *numpy.log(E)**3
    At = 0.0263*t
    A0 = At + 1.34 + 0.160*numpy.log(E)- 0.0404*numpy.log(E)**2 + 0.00276*numpy.log(E)**3
    A1 = At - 4.33
    return x**A0*(x1+x)**A1


def delay_distribution(tau, E, t):
    """
    tau defined as ct/r_moliere.
    """
    E = E/units.MeV
    tau1 = numpy.exp(-2.71 + 0.0823*numpy.log(E) - 0.114*numpy.log(E)**2)
    A0 = 1.70 + 0.160*t - 0.142*numpy.log(E)
    A1 = -3.21
    return tau**A0*(tau1 + tau)**A1



def shower_front_shape(tau, x, t, primary='proton'):
    """
    tau defined as ct/r_moliere and x defined as r/r_moliere.
    """
    beta_s = {'proton':0, 'iron':-0.062, 'photon': 0.103}
    a0 = -6.04 + 0.707*numpy.log(x)**2 + 0.210*numpy.log(x)**3 - 0.0215*numpy.log(x)**4 - 0.00269*numpy.log(x)**5;
    a1 = 0.855 + 0.335*numpy.log(x) + 0.0387*numpy.log(x)**2 - 0.00662*numpy.log(x)**3.
    tau2 = tau*numpy.exp(-0.2*t-beta_s)
    return numpy.exp(a0*numpy.log(tau2) - a1*numpy.log(tau2)**2)
