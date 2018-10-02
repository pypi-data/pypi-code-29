import numpy

def response_function(enu, emu, cos_theta, kind='numu'):
    enu, emu, cos_theta = map(numpy.asarray, (enu, emu, cos_theta))
    shape = numpy.broadcast(enu, emu, cos_theta).shape
    contrib = numpy.zeros(shape+(100,))
    muyield = numpy.zeros(shape+(100,))
    energy_per_nucleon = logspace(numpy.log10(enu), numpy.log10(enu)+3, 101) # shape = (20, 101, 101)
    a = 1
    penergy = a*energy_per_nucleon  # for proton only
    de = numpy.diff(penergy)
    pe = penergy[...,:-1] + de/2.
    weights = gaisser_flux_new(pe) # this flux is new flux formula given to me by Tom
    numu_yield = elbert_yield(enu[...,None],pe, a, cos_theta[...,None],kind='numu',differential=True)
    nue_yield = elbert_yield(enu[...,None], pe, a, cos_theta[...,None], kind='nue', differential=True)
    charm_yield = elbert_yield(enu[...,None], pe, a, cos_theta[...,None], kind='charm', differential=True)
    #ey = numu_yield + nue_yield + charm_yield
    ey = elbert_yield(enu[...,None], pe, a, cos_theta[...,None], kind=kind, differential=True)
    contrib = ey*weights*de
    muyield = elbert_yield(emu[...,None], pe, a, cos_theta[...,None], kind='mu', differential=False)

    return contrib, muyield, energy_per_nucleon[...,:-1] + numpy.diff(energy_per_nucleon)/2., weights


def response(e_prim_bins, e_mu_bins):
    from .gaisser import gaisser_flux
    from .elbert import elbert_yield
    de = numpy.diff(e_prim_bins, axis=0)
    e_prim = e_prim_bins[:-1] + de/2
    de_mu = numpy.diff(e_mu_bins, axis=1)
    e_mu = e_mu_bins[:,:-1] + de_mu*0.5
    y = elbert_yield(e_mu, e_prim, 1, 1, differential=True)
    w = gaisser_flux(e_prim)
    res = numpy.sum(w*y*de, axis=0)
    return res
