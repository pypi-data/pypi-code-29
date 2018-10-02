from phys import units
import numpy

class fpe_context(object):
    """
    Temporarily modify floating-point exception handling
    """
    def __init__(self, **kwargs):
        self.new_kwargs = kwargs
    def __enter__(self):
        self.old_kwargs = numpy.seterr(**self.new_kwargs)
    def __exit__(self, *args):
        numpy.seterr(**self.old_kwargs)

elbert_params = {
    'elbert': {'a' : 14.5,
               'p1': 0.757+1,
               'p2': 5.25,
               'p3': 1},
    'mu' :    {'a': 49.41898933142626,
               'p1': 0.62585930096346309+1,
               'p2': 4.9382653076505525,
               'p3': 0.58038589096897897},
    'numu':   {'a': 79.918830537201231,
               'p1': 0.46284463423687988+1,
               'p2': 4.3799061061862314,
               'p3': 0.31657956163506323},
    'nue':    {'a' : 0.80523974705259793,
               'p1': 0.61852327151082975+1,
               'p2': 9.7834540169712252,
               'p3': 0.65126864602268075},
    'charm':  {'a' : 780.35285355003532/1e6,
               'p1': -0.39555243513109928+1,
               'p2': 7.3461490462825703,
               'p3': 0.76688386541155051}
}

def effective_costheta(costheta):
    x = costheta
    p = [0.102573, -0.068287, 0.958633, 0.0407253, 0.817285]
    return numpy.sqrt((x**2 + p[0]**2 + p[1]*x**p[2] + p[3]*x**p[4])/(1 + p[0]**2 + p[1] + p[3]))

def elbert_yield(emin, primary_energy, primary_mass, cos_theta, kind='mu', differential=False):
    params = elbert_params[kind]
    a  = params['a']
    p1 = params['p1']
    p2 = params['p2']
    p3 = params['p3']

    emin /= units.GeV
    primary_energy /= units.GeV

    En = primary_energy/primary_mass
    x = emin/En

    if kind == 'charm':
        decay_prob = 1.
    else:
        decay_prob = 1./(En*effective_costheta(cos_theta))

    with fpe_context(all='ignore'):
        # where x>=1, replace all icdf values by 0 and where x<1, return "a*primary_mass*decay_prob*x**(-p1)*(1-x**p3)**p2"
        icdf = numpy.where(x >= 1, 0., a*primary_mass*decay_prob*x**(-p1)*(1-x**p3)**p2)
        if differential:
            icdf *= (1./En)*numpy.where(x >= 1, 0., (p1/x + p2*p3*x**(p3-1)/(1-x**p3)))

    return icdf
