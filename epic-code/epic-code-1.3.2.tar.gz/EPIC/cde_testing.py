import EPIC
from EPIC.cosmology import cosmic_objects as cosmo, observations
from EPIC.utils import statistics as stat
import EPIC.sim_objects as sim
import numpy as np

datasets = observations.choose_from_datasets({
        'Hz': 'cosmic_chronometers',
        'H0': 'HST_local_H0',
    })

LCDM_std = cosmo.CosmologicalSetup('lcdm', physical=False, derived='lambda')
std_parameters = {
    'Oc0': 0.2,
    'H0': 67,
}
prior_std = {
        'Oc0': [0.2, 0.4],
        'H0': [50, 90]
        }

Omegas = np.linspace(0.25, 0.35, 6)

an_std = stat.Analysis(datasets, LCDM_std, prior_std)
#ll_std = an_std.log_likelihood(parameter_space=std_parameters)
lp_std = [an_std.log_posterior(parameter_space={'Oc0': O, 'H0': 67})[0] for O in Omegas]

#a = np.logspace(-3, 0, 300)
#H_std = LCDM_std.get_Hubble_Friedmann(a, parameter_space=std_parameters)

LCDM_cde = cosmo.CosmologicalSetup('cde', physical=False, derived='ide', interaction_setup={
    'parameter': {'idm': 'xi'},
    'species': ['idm', 'ide'],
    'propto_other': {'ide': 'idm'},
    'sign': {'idm': 1, 'ide': -1},
    'tex': '\\xi'
})
cde_parameters = {
    'Oc0': 0.2,
    'H0': 67,
    'wd': -1,
    'xi': 0
}
prior_cde = {
        'Oc0': [0.2, 0.4],
        'H0': [50, 90],
        }

an_cde = stat.Analysis(datasets, LCDM_cde, prior_cde, fixed={'wd': -1, 'xi': 0})
#ll_cde = an_cde.log_likelihood(parameter_space=cde_parameters)
print('\n\n\ncde')
lp_cde = [an_cde.log_posterior(parameter_space={'Oc0': O, 'H0': 67})[0] for O in Omegas]

#H_cde = LCDM_cde.get_Hubble_Friedmann(a, parameter_space=cde_parameters)

#print(max(abs(H_cde[:-1]/H_std[:-1] - 1)))
#print(ll_std, ll_cde)

import matplotlib.pyplot as plt
fig, ax = plt.subplots()
ax.plot(Omegas, lp_std, label='std')
ax.plot(Omegas, lp_cde, label='cde')
ax.legend()
fig.savefig('Omegas.pdf')
