"""This module defines classes for Bayesian learning of probabilistic models
for responses in phoneme-identification tests,
for which results are conventionally presented as confusion matrices.

Raw input data are obtained from a cm_data.StimRespCountSet instance.

*** Class Overview:

ConfMatrixResultSet: Defines posterior distributions of all response probabilities,
    given all selected data from a phoneme-identification experiment.
    Learned from a single cm_data.StimRespCountSet instance

ResponseProbGroup: Container for all individual response probability models,
    for ONE group of test subjects.

ResponseProbIndividual: Posterior distribution of phoneme response probabilities for
    one subject in all selected test conditions,
    given response counts and a single ResponseProbPopulation instance,
    common for all subjects.

ResponseProbPopulation: Joint posterior distribution of
    response probabilities and concentration parameters
    in the population from which ONE group of test subjects was recruited.

PopulationConcPrior: Vague prior distribution of concentration parameters,
    common for ALL groups and all subjects.


*** Model Theory: See
A. Leijon, G. E. Henter, and M. Dahlquist (2016).
Bayesian analysis of phoneme confusion matrices.
*IEEE Trans Audio, Speech, and Language Proc* 24(3):469–482.
doi: 10.1109/TASLP.2015.2512039.


*** Version History:
2018-08-11 first functional version

"""
# *********************************** merge groups ? *******************

import numpy as np
import logging
from collections import OrderedDict
from scipy.stats import dirichlet
from scipy.optimize import minimize
from scipy.special import gammaln, psi

from samppy import hamiltonian_sampler as ham

ham.VECTOR_AXIS = 1

logger = logging.getLogger(__name__)
# logger.setLevel(logging.DEBUG)

N_CONC_SAMPLES = 100
# = number of samples of distribution of concentration vectors


# -----------------------------------------------------------------
# Overall performance measures, functions of stim-resp probabilities:

def prob_correct(u, cmf):
    """Probability of correct response (PC),
    for given stim_range-response probability matrices
    :param u: array of response-probabilities
        u[..., s, r] = P(R=r | S=s) for ...-th matrix case
    :param cmf: a ConfMatrixFrame instance,
        with properties stim_count, correct_resp
        len(cmf.stim_count) == len(cmf.correct_resp) == u.shape[-2]
    :return: array pc; pc[...] = prob. correct response (in percent)
        pc.shape == u.shape[:-2]
    """
    corr_ind = [cmf.resp.index(cmf.correct_resp[s])
                for s in cmf.stim]
    stim_prob = np.array(cmf.stim_count, dtype=float)
    stim_prob /= np.sum(stim_prob)
    pc = 100. * np.sum(u[..., range(len(corr_ind)), corr_ind] * stim_prob,
                       axis=-1)
    return pc


def mutual_information(u, cmf):
    """Mutual Information (MI) between stim_range and response,
    for given stim_range-response probability matrices.
    :param u: array of response-probabilities
        u[..., s, r] = P(R=r | S=s)
    :param cmf: a ConfMatrixFrame instance, with property stim_count
        len(cmf.stim_count) == u.shape[-2]
    :return: array MI; MI[...] = mutual information ( bits / presented sound)
        MI.shape == u.shape[:-2]
    """
    # MI = E{ log (P(R | S) / P(R) } =
    # = sum_{s,r} P(S=s, R=r) * log ( P(R=r | S=s) / P(R=r) )
    stim_prob = np.array(cmf.stim_count, dtype=float)
    stim_prob /= np.sum(stim_prob)
    psr = u * np.asarray(stim_prob).reshape((-1,1))
    # = psr[..., s, r] = joint P(S=s, R=r)
    pr = np.sum(psr, axis=-2, keepdims=True)
    # pr[..., 0, r]= P(R=r)
    # return np.sum(psr * np.log(u / pr),
    #               axis=(-2, -1))
    u = np.maximum(u, np.finfo(0.).tiny)
    # avoid nan in case any u == 0.
    mi = np.sum(psr * np.log2(u / pr),
                axis=(-2, -1))
    return mi


# ------------------------------------------------------------------
class ConfMatrixResultSet:
    """Defines posterior distributions of response probabilities
    for all groups, subjects, test conditions, and test stimuli,
    given all included data from a phoneme-identification experiment.
    Class-method learn creates an instance
    from raw phoneme-identification data
    stored in a cm_data.StimRespCountSet instance.
    """
    def __init__(self, cmf, groups):
        """
        :param cmf: single ConfMatrixFrame instance,
            common for all subjects in all groups.
        :param groups: dict with ResponseProbGroup instances, stored as
            groups[group] = one ResponseProbGroup instance
            groups[group].subjects[subject] = a ResponseProbIndividual instance
            where
            group and subject are string-valued keys
        """
        self.cmf = cmf
        self.groups = groups

    def __repr__(self):
        return f'ConfMatrixResultSet(cmf=cmf, groups=groups)'

    @classmethod
    def learn(cls, ds):
        """Create and learn ResponseProbGroup instances,
        one for each subject group,
        from a given StimRespCountSet instance
        :param ds: a single cm_data.StimRespCountSet instance,
            including observed response counts for all test subjects
            in all test conditions.
        :return: a single cls instance containing all response-probability models
        """
        ds.check_complete()
        # check that subjects have sufficiently complete data
        cmf = ds.cmf
        population_prior = PopulationConcPrior(mode=0.5, mean=10.)
        # = single prior used for all groups and all attributes
        groups = OrderedDict((g, dict()) for g in ds.cmd.keys())
        for (g, g_subjects) in ds.cmd.items():
            groups[g] = ResponseProbGroup.learn(cmf, g_subjects, population_prior)
            logger.info(f'Learned group {repr(g)} with {len(g_subjects)} subjects')
        # if len(groups) > 1:
        #     # create separate new group including all groups merged
        #     # Includes all subject models unchanged, but a new population model
        #     merged_g = tuple(g for g in groups.keys())
        #     groups[merged_g] = ResponseProbGroup.merge([g_models
        #                                                 for g_models in groups.values()])
        return cls(cmf, groups)


# -------------------------------------------------------------------
class ResponseProbGroup:
    """Container for ResponseProbIndividual instances
    for all test subjects in ONE group,
    AND for a single ResponseProbPopulation instance adapted to the group data
    """
    def __init__(self, cmf, subjects, population):
        """
        :param cmf: a ConfMatrixFrame instance.
        :param subjects: dict with (subject_id, ResponseProbIndividual) elements
        :param population: a single ResponseProbPopulation instance
        """
        self.cmf = cmf
        self.subjects = subjects
        self.population = population

    def __repr__(self):
        return ('ResponseProbGroup('+
                '\n\tcmf=cmf,' +
                '\n\tsubjects=subjects'
                f'\n\tpopulation={repr(self.population)})')

    @classmethod
    def learn(cls, cmf, g_subjects, population_prior):
        """Create one ResponseProbIndividual instance for each subject,
        and learn a single ResponseProbPopulation prior for the population
        represented by the subjects, in ONE group of subjects.
        :param cmf: a ConfMatrixFrame object defining experimental layout
        :param g_subjects: a nested dict with elements (subject_id, s_learn_data)
            where s_learn_data is a dict with elements (tc-tuple, result-list)
        :param population_prior: externally pre-calculated single prior,
            same for all groups and attribute models
        :return: a ResponseProbGroup instance
        """
        s_cm = {subject: _get_conf_array(cmf, subject_dict)
                for (subject, subject_dict) in g_subjects.items()}
        # s_cm[subject] = cm = 3D array stored as cm[t, subject, r]
        population = ResponseProbPopulation.learn(r_count=[cm for cm in s_cm.values()],
                                                  prior=population_prior,
                                                  cmf=cmf
                                                  )
        subjects = {s: ResponseProbIndividual(cmf, cm, population)
                    for (s, cm) in s_cm.items()}
        return cls(cmf, subjects, population)

    def rvs(self, n_samples):
        """Random samples of response probability matrices
        for all subjects in the group.
        :param n_samples: number of samples for each subject
        :return: u = 4D array:
            u[n, t, s, r] = n-th sample of probability for
            r-th response to s-th stim_range phoneme
            in t-th test condition.
            len(u) == len(self.subjects) * n_samples
        """
        return np.concatenate((s.rvs(n_samples) for s in self.subjects),
                              axis=0)

    # @classmethod
    # def merge(cls, models):
    #     """Merge a sequence of group models into a single such model.
    #     :param models: list or tuple of ResponseProbGroup instances
    #     :return: single ResponseProbGroup instance
    #
    #     Arne Leijon, 2018-05-19
    #     2018-07-09, remove arbitrary constant in log(cat_width) params, for gauss_gamma population
    #     """
    #     def join(subject_dicts):
    #         """Gather several subject dicts into a single dict
    #         :param subject_dicts: sequence of dicts, each with (s_id, ResponseProbIndividual) elements
    #         :return: all_subjects = single dict with (s_id, ResponseProbIndividual) elements,
    #             union of all s_dicts
    #         """
    #         all_subjects = dict()
    #         # space for result, stored as all_subjects[subject_id] = subject ResponseProbIndividual instance
    #         for s_dict in subject_dicts:
    #             for (s, s_model) in s_dict.items():
    #                 if s in all_subjects:
    #                     all_subjects[s].add(s_model)
    #                 else:
    #                     all_subjects[s] = s_model
    #         return all_subjects
    #     # ----------------------------------------------------
    #
    #     population_prior = models[0].population_prior  # copy reference
    #     cmf = models[0].cmf  # copy reference
    #     population = copy.deepcopy(population_prior)  # new population model
    #     subjects = join(m.subjects for m in models)
    #     x_samples = np.array([s_model.x_samples for s_model in subjects.values()])
    #
    #     n_q = _n_quality_params(cmf)
    #     # remove any arbitrary constant from log(cat_width) params:
    #     x_samples[..., n_q:] -= np.mean(x_samples[..., n_q:], axis=-1, keepdims=True)
    #     population.learn(x_samples, population_prior)
    #     return cls(cmf, subjects, population, population_prior)


# ------------------------------------------------------------------
class ResponseProbModel:
    """Superclass for models that can generate
    random samples of response-probability arrays
    from a posterior distribution of
    response probabilities in phoneme-identification tests,
    """
    def __init__(self, cmf):
        """
        :param cmf: a single ConfusionMatrixFrame
        """
        self.cmf = cmf

    @property
    def mean(self):
        a = np.mean(self.conc(), axis=0)
        return a / np.sum(a, axis=-1, keepdims=True)

    def conc(self):
        """Concentration parameters for Dirichlet distribution.
        Abstract method, must be implemented by sub-class
        :return: 4D array a, stored as
            a[i, t, s, r] = i-th sample of concentration parameter vector
            for cmf.stim_range[s] -> response cmf.resp_range[r]
            in cmf.test_factors[t].
        """
        raise NotImplementedError

    def rvs(self, n_samples):
        """Generate random arrays of response probabilities
        from the Dirichlet distribution for each stim_range in each test-condition.
        :param n_samples: desired number of sample arrays
        :return: u = 4D array of equally probable sample arrays, with
            u[n, t, s, r] = n-th sample of probability
            for event cmf.stim_range[s] -> response cmf.resp_range[r]
            in cmf.test_factors[t].
            len(u) == n_samples (approximately)
        """
        a = self.conc().transpose((1, 2, 0, 3))
        # a[t, s, i, :] = i-th sample of concentration vector
        # for responses to s-th stim_range in t-th test condition
        n_u = max(1, n_samples // a.shape[-2])
        # = n of samples from each dirichlet distribution
        u = np.array([[[dirichlet.rvs(alpha=a_tsi, size=n_u)
                        for a_tsi in a_ts]
                       for a_ts in a_t]
                      for a_t in a]
                     )
        # u[t, s, i, n, r] = n-th u sample for i-th conc sample, must transpose
        u = u.transpose((2, 3, 0, 1, 4))
        return u.reshape((-1, *u.shape[2:]))

    def fcn_rvs(self, fcn, n_samples, *args, **kwargs):
        """Generate random samples of any scalar function of
        a response-probability matrix,
        e.g., prob-correct or mutual-information
        :param fcn: function with signature fcn(U, *args, **kwargs)-> array, where
            u = array of response-probability matrices
            return value.shape == u.shape[:-2]
        :param n_samples: desired number of samples
        :param args: any positional arguments to fcn
        :param kwargs: any keyword arguments to fcn
        :return: fcn_values = 2D array
            fcn_values[n, t] = n-th sample for t-th test condition
            fcn_values.shape == (n_samples, n_test_conditions)
        """
        return fcn(self.rvs(n_samples), *args, **kwargs)


# -------------------------------------------------------------------
class ResponseProbIndividual(ResponseProbModel):
    """A ResponseProbIndividual instance represents the distribution of
    response probabilities in phoneme-identification tests
    with ONE listener in all selected test conditions.
    The vector of response probabilities for each presented phoneme category
    is a Dirichlet RV, given observed counts and prior concentration param.

    Observed response counts are modeled by a multinomial-Dirichlet distribution:

    Define U as a probability vector with elemetns U[t, s, r] = P(R=r | t, s)
    for r-th response to the s-th stim_range in the t-th test condition.
    The probability density for U[t,s] is then
    p_U(u) \propto \prod_r u_r**(a_r - 1), with prior concentration parameters
    a_r = x_r + prior.a_r, where x_r is the observed response count,
    """
    def __init__(self, cmf, cm, population):
        """
        :param cmf: reference to a ConfMatrixFrame instance,
            common for all model instances.
        :param cm: 3D array or array-like list of response counts
            cm[t, s, r] = number of responses cmf.resp_range[r]
            to presentation cmf.stim_range[s] in cmf.test_factors[t]
        :param population: ResponseProbPopulation instance, common for all subjects,
            defining the probability distribution of concentration parameters
            in the population from which this subject was recruited.
         """
        super().__init__(cmf=cmf)
        self.cm = cm
        self.population = population

    def __repr__(self):
        return ('ResponseProbIndividual('+
                '\n\tcmf=cmf,' +
                '\n\tpopulation=population,' +
                '\n\tcm=cm')

    def conc(self):
        """Posterior distribution of concentration parameters,
        represented by an array of samples.
        Used by super().rvs
        :return: 4D array a, stored as
            a[i, t, s, r] = i-th sample of concentration parameter
            for probability distribution of
            U[t, s, r] = probability mass
            for event cmf.stim_range[s] -> response cmf.resp_range[r]
            in cmf.test_factors[t].
        """
        return self.population.conc() + self.cm


# ------------------------------------------ population models:

class ResponseProbPopulationPoint(ResponseProbModel):
    """Posterior distribution of concentration vectors for
    Dirichlet distribution of phoneme response probabilities,
    AND for response probabilities, given self.conf()
    for all stim_range phonemes, in all test conditions.
    This version uses only a POINT estimate for the concentrations,
    determined by MAP type II, given observed response counts.

    This population model was used in Leijon et al. (2016).
    """
    def __init__(self, cmf, a, prior):
        """
        :param cmf: a ConfMatrixFrame instance, needed by super-class.
        :param a: 3D array or array-like list of concentration parameters
            a[t, s, r] for the r-th response
            to the s-th stim_range in the t-th test condition
        :param prior: a PopulationConcPrior instance.
        """
        super().__init__(cmf=cmf)
        self.a = np.asarray(a)
        self.prior = prior

    def __repr__(self):
        return ('ResponseProbPopulationPoint(' +
                f'\n\ta={repr(self.a)},' +
                f'\n\tcmf={repr(self.cmf)})')

    def conc(self):
        """Posterior distribution of concentration parameters,
        represented by sample array self.a
        Used by super().rvs()
        :return: 4D array self.a, stored as
            a[0, t, s, :] = point estimate of concentration parameter vector
            for s-th stimulus phoneme in t-th test condition
        """
        return self.a[np.newaxis, ...]

    @classmethod
    def learn(cls, cmf, r_count, prior):
        """Learn a MAP point estimate of concentration parameters,
        given an array of observed response counts.

        The probability of ONE observed response-count row vector x is
        P(x | u, a) \propto \prod_i u_i**(x_i+a_i), where
            a_i is the i-th element of the concentration vector a,
            x is the observed vector of response counts.
        By integrating over u (Leijon et al, 2016) we get
        P(x, a) \propto prior.pdf(a) * C(a) / C(x+a) \propto pdf(a | x), where
        C(a) = normalization factor of Dirichlet distribution
        This log_likelihood(a | x) is used for ML estimation.

        Reference: Leijon et al.(2016).

        :param cmf: a ConfMatrixFrame instance
        :param r_count: 4D array-like list of response counts, stored as
            x[n, t, s, r] = number of responses cmf.resp_range[r] to cmf.stim_range[s]
            in t-th test condition by n-th subject of a group
        :param prior: single PopulationConcPrior instance
        :return: a single cls instance adapted to input data
        """
        r_count = np.array(r_count).transpose((1, 2, 0, 3))
        # r_count[t, s, l, r] = response counts for l-th listener
        a = [[cls.conc_point_estimate(x_ts, prior)
              for x_ts in x_t]
             for x_t in r_count]
        return cls(cmf, a, prior)

    @classmethod
    def conc_point_estimate(cls, x_lr, prior):
        """Point estimate of ONE concentration row vector,
        common for all subjects.
        :param x_lr: 2D array of response counts,
            x_lr[l, r] = count for r-th response of l-th listener
        :return: 1D vector of optimal concentration params
        """
        def neg_ll(a, x_lr):
            """
            negative log-likelihood for a single tentative concentration ROW vector
            :param a: 1D row vector, with concentration parameters for
                ONE stimulus in ONE test condition
                a[i] = concentration param vector for i-th response probability
            :param x_lr: 2D array with with response counts
                x_lr.shape[-1] = len(a)
            :return: nll = scalar neg. log-likelihood values
            """
            nll = - (_conc_ll(a, x_lr) +
                     np.sum(prior.conc_ll(a)))
            return nll

        def grad_neg_ll(a, x_lr):
            """gradient of neg_ll
            """
            d_nll = - (_grad_conc_ll(a, x_lr) +
                       prior.d_conc_ll(a))
            return d_nll
        # ----------------------------------------------------------

        n_resp = len(x_lr[0])
        bounds = [(0.000001, None) for _ in range(n_resp)]
        # to prevent inf log-likelihood
        res = minimize(fun=neg_ll,
                       jac=grad_neg_ll,
                       args=(x_lr,),
                       bounds=bounds,
                       x0=np.ones(n_resp) * prior.mode)
        if res.success:
            return res.x
        else:
            logger.error(f'ResponseProbPopulation.learn minimize res= {res}')
            raise RuntimeError('MAP search did not converge. *** Should not happen ***')


# ------------------------------------------------------------------
class ResponseProbPopulationSampled(ResponseProbPopulationPoint):
    """Posterior distribution of concentration vectors for
    Dirichlet distribution of phoneme response probabilities,
    AND for response probabilities, given self.conf()
    for all stimulus phonemes, in all test conditions.
    This version uses SAMPLED distribution of concentration parameters,
    calculated by Hamiltonian sampling, given observed response counts.

    This population model is theoretically better than the one in Leijon et al. (2016),
    which approximated the population response probability distribution
    by a SINGLE prior Dirichlet distribution.
    Instead, this model uses a sampled approximation of the distribution
    of Dirichlet concentration parameters.
    This implies a MIXTURE of Dirichlet distributions
    for the population response probability vector for each stimulus.
    """

    def conc(self):
        """Posterior distribution of concentration parameters,
        represented by sample array self.a
        :return: 4D array self.a, stored as
            a[n, t, s, :] = n-th sample of concentration parameter vector
            for s-th stimulus phoneme in t-th test condition
        """
        return self.a

    @classmethod
    def learn(cls, cmf, r_count, prior):
        """Learn sampled distribution of concentration parameters,
        given an array of observed response counts.

        The probability of ONE observed response-count row vector x is
        P(x | u, a) \propto \prod_i u_i**(x_i+a_i), where
            a_i is the i-th element of the concentration vector a,
            x is the observed vector of response counts.
        By integrating over u (Leijon et al, 2016) we get
        P(x, a) \propto prior.pdf(a) * C(a) / C(x+a) \propto pdf(a | x), where
        C(a) = normalization factor of Dirichlet distribution
        This log_likelihood(a | x) is used for ML estimation.

        Reference: Leijon, Henter, Dahlquist, 2016.

        :param cmf: a ConfMatrixFrame instance
        :param r_count: 4D array-like list of response counts, stored as
            x[n, t, s, r] = number of responses cmf.resp_range[r] to cmf.stim_range[s]
            in t-th test condition by n-th subject of a group
        :param prior: single PopulationConcPrior instance
        :return: a single cls instance adapted to input data
        """
        # def neg_ll(a, x_lr):
        #     """
        #     negative log-likelihood for an array of concentration ROW vectors
        #     :param a: 2D array, with tentative concentration-parameter samples for
        #         ONE stimulus in ONE test condition
        #         a[n, i] = n-th sample of concentration param for i-th response probability
        #     :param x_lr: 3D array with with response counts
        #         x_lr.shape[-1] = a.shape[-1], broadcast-compatible with conc-param a
        #         x[l, 0, i] = response count for l-th listener for i-th response category
        #     :return: nll = scalar neg. log-likelihood values
        #     """
        #     nll = - (_conc_ll(a, x_lr) +
        #              np.sum(prior.conc_ll(a), axis=-1))
        #     return nll
        #
        # def grad_neg_ll(a, x_lr):
        #     """gradient of neg_ll
        #     """
        #     d_nll = - (_grad_conc_ll(a, x_lr) +
        #                prior.d_conc_ll(a))
        #     return d_nll
        #
        # def conc_samples(x_lr):
        #     """Samples of distribution of ONE concentration row vector,
        #     common for all subjects.
        #     :param x_lr: 2D array of response counts,
        #         x_lr[l, r] = count for r-th response of l-th listener
        #     :return: 1D vector of optimal concentration params
        #     """
        #     a0 = cls.conc_point_estimate(x_lr, prior).reshape((1, -1))
        #     n_resp = x_lr.shape[-1]
        #     x_lr = x_lr[:, np.newaxis, :]
        #     bounds = [(0.000001, None) for _ in range(n_resp)]
        #     # to prevent inf log-likelihood
        #     sampler = ham.HamiltonianBoundedSampler(x=a0,
        #                                             fun=neg_ll,
        #                                             jac=grad_neg_ll,
        #                                             args=(x_lr,),
        #                                             epsilon=0.005,
        #                                             bounds=bounds
        #                                             )
        #     sampler.safe_sample(n_samples=N_CONC_SAMPLES, min_steps=2)
        #     logger.debug(f'sampler accept_rate = {sampler.accept_rate:.1%}, ' +
        #                  f'n_steps = {sampler.n_steps:.0f}, ' +
        #                  f'epsilon = {sampler.epsilon:.4f}')
        #     return sampler.x
        def neg_ll(ln_a, x_lr):
            """negative log-likelihood for an array of concentration ROW vectors
            Samples are represented by the LOG of concentration params.
            :param ln_a: 2D array, with tentative log-concentration-parameter samples for
                ONE stimulus in ONE test condition
                ln_a[n, i] = n-th sample of log(concentration param) for i-th response probability
            :param x_lr: 3D array with with response counts
                x[l, 0, i] = response count for l-th listener for i-th response category
                x_lr.shape[-1] = a.shape[-1], broadcast-compatible with conc-param a
            :return: nll = scalar neg. log-likelihood values for each conc. vector
                nll.shape == ln_a.shape[:-1]
            """
            # if any(ln_a.flatten() > 100.):
            #     logger.warning(f'Near-inf conc param encountered')
            a = np.exp(ln_a)
            # if any(a.flatten() == 0.):
            #     logger.warning(f'Zero conc param encountered')
            nll = - (_conc_ll(a, x_lr) +
                     np.sum(prior.conc_ll(a), axis=-1))
            return nll

        def grad_neg_ll(ln_a, x_lr):
            """gradient of neg_ll
            :param ln_a: as for net_ll
            :param x_lr: as for neg_ll
            :return: d_nll = gradient
                d_nll.shape == ln_a.shape
            """
            # if any(ln_a.flatten() > 100.):
            #     logger.warning(f'Near-inf conc param encountered')
            a = np.exp(ln_a)
            # if any(a.flatten() == 0.):
            #     logger.warning(f'Zero conc param encountered')
            d_nll = - (_grad_conc_ll(a, x_lr) +
                       prior.d_conc_ll(a)) * a
            # d a / d ln_a = a
            return d_nll

        def conc_samples(x_lr):
            """Samples of distribution of concentration row vector,
            common for all subjects.
            Sampling is done for log-concentration params,
            i.e., with fixed RELATIVE stepsize.
            :param x_lr: 2D array of response counts,
                x_lr[l, r] = count for r-th response of l-th listener
            :return: 1D vector of optimal concentration params
            """
            ln_a0 = np.log(cls.conc_point_estimate(x_lr, prior).reshape((1, -1)))
            n_resp = x_lr.shape[-1]
            x_lr = x_lr[:, np.newaxis, :]
            near_zero = np.log(0.000001)
            near_inf = np.log(1000.)
            # must limit Hamiltonian sample trajectories to avoid numerical overflow
            bounds = [(near_zero, near_inf) for _ in range(n_resp)]
            sampler = ham.HamiltonianBoundedSampler(x=ln_a0,
                                                    fun=neg_ll,
                                                    jac=grad_neg_ll,
                                                    args=(x_lr,),
                                                    epsilon=0.2,
                                                    bounds=bounds
                                                    )
            a = np.exp(sampler.safe_sample(n_samples=N_CONC_SAMPLES, min_steps=5))
            logger.debug(f'sampler accept_rate = {sampler.accept_rate:.1%}, ' +
                         f'n_steps = {sampler.n_steps:.0f}, ' +
                         f'epsilon = {sampler.epsilon:.4f}')
            return a

        # ---------------------------------------------------------

        # r_count[l, t, s, r] = response counts for l-th listener
        r_count = np.array(r_count).transpose((1, 2, 0, 3))
        # r_count[t, s, l, r] = response counts for l-th listener
        a = np.array([[conc_samples(x_ts)
                       for x_ts in x_t]
                      for x_t in r_count])
        # a[t, s, n, r]
        a = a.transpose((2, 0, 1, 3))
        # a[n, t, s, r]
        return cls(cmf, a, prior)


# ResponseProbPopulation = ResponseProbPopulationPoint
ResponseProbPopulation = ResponseProbPopulationSampled
# = Selected model class for population


class PopulationConcPrior:
    """Broad prior distribution of concentration parameters,
    same for all groups, test-conditions and stimuli
    Implemented as a single scalar gamma(a, b) distribution
    """
    def __init__(self, mode, mean):
        """Scalar prior for all concentration params
        :param mode: scalar gamma distribution mode
        :param mean: scalar gamma distribution mean
        """
        # mode = (a-1) / b
        # mean = a / b
        # (a-1 / a = mode / mean
        self.a = 1. / (1. - mode / mean)
        self.b = self.a / mean

    @property
    def mode(self):
        return (self.a - 1.) / self.b

    @property
    def mean(self):
        return self.a / self.b

    def __repr__(self):
        return f'PopulationConcPrior(mode={self.mode}, mean={self.mean})'

    def conc_ll(self, x):
        """NON-normalized logpdf of gamma distribution
        :param x: array or array-like list of sample values
        :return: ll = log-likelihood
            ll.shape == x.shape
        """
        return (self.a - 1.) * np.log(x) - self.b * x

    def d_conc_ll(self, x):
        """Derivative of conc_ll()
        :param x: array or array-like list of sample values
        :return: d_ll = d conc_ll(x_[...]) / d x[...]
            d_ll.shape == x.shape
        """
        return (self.a - 1.) / x - self.b


# --------------------------------------------- module help functions:

def _get_conf_array(cmf, subject_dict):
    """Collect response counts in an array for ONE subject
    :param subject_dict: nested dict with structure
        subject_dict[t][s][r] = number of responses cmf.resp[r]
        for presented phoneme cmf.stim[s] in cmf.test_conditions()[t]
        NOTE: some test-conditions and/or stim categories might be missing
    :return: 3D array cm with counts stored as
        cm[t, s, r] = subject_dict[t][s][r], OR zero if missing
    """
    def gen_rows(tc_dict):
        """generator of 1D arrays with all response counts for given stim
        :param tc_dict: nested dict with tc_dict[s][r] = count
        :return: generator yielding 1D arrays with counts for all responses to one stim
        """
        for s in cmf.stim:
            if s in tc_dict:
                yield [0 if r not in tc_dict[s] else tc_dict[s][r]
                       for r in cmf.resp]
            else:
                yield np.zeros(len(cmf.resp))
    # -------------------------------------------------------

    def gen_conf_matrices():
        """generator yielding one 2D conf matrix for each test-cond
        in external subject_dict
        """
        for tc in cmf.test_conditions():
            if tc in subject_dict:
                yield [cm_row
                       for cm_row in gen_rows(subject_dict[tc])]
            else:
                yield np.zeros(cmf.conf_matrix_shape[1:])
    # --------------------------------------------------------

    cm = [cm_tc
          for cm_tc in gen_conf_matrices()]
    return np.array(cm)


def _log_C(a):
    """log normalization factor for Dirichlet distribution,
    given concentration vector,
    = - log_partition_function
    Leijon et al, 2018, Eq. B.3.
    :param a: tentative array of concentration parameters,
        a[..., :] = ...-th concentration row vector
    :return: _log_C(a[..., :] = log normalization factor
        _log_C.shape == a.shape[:-1]
    """
    return gammaln(np.sum(a, axis=-1)) - np.sum(gammaln(a), axis=-1)


def _grad_log_C(a):
    """Gradient of _log_C
    :param a: tentative array of concentration parameters,
        a[..., :] = ...-th concentration row vector
    :return: g = gradient with elements
        g[..., i] = d _log_C(a[..., :]) / d a[..., i]
        g.shape == a.shape
    """
    return psi(np.sum(a, axis=-1, keepdims=True)) - psi(a)


def _conc_ll(a, x):
    """log-likelihood of Dirichlet concentration parameter vector
    for a multinomial-Dirichlet model of observed response counts
    :param a: 1D or 2D array of concentration parameters
        a[..., i] = concentration param for i-th response
    :param x: 2D or 3D array with response counts
        x[l, ..., i] for i-th response by l-th listener
        broadcast-compatible with a
        x.shape[-1] = len(a)
    :return: LL = log-likelihood for a, given x
        LL.shape == a.shape[:-1]

    Reference: Leijon, Henter, Dahlquist, 2016, Eq. B.3.
    """
    return np.sum(_log_C(a) - _log_C(a + x),
                  axis=0)


def _grad_conc_ll(a, x):
    """gradient of _conc_ll w.r.t a, given same observed count x
    :param a: 1D or 2D array of concentration parameters
        a[..., i] = concentration param for i-th response
    :param x: 2D or 3D array with response counts
        x[l, ..., i] for i-th response by l-th listener
        broadcast-compatible with a
        x.shape[-1] = len(a)
    :return: d_ll = 1D or 2D array with elements
        d_ll[..., i] = d _conc_ll(a[..., :]) / d a[..., i]
        d_ll.shape == a.shape
    """
    return np.sum(_grad_log_C(a) - _grad_log_C(a + x),
                  axis=0)


# ------------------------------------------------- TEST:


if __name__ == '__main__':
    from scipy.optimize import approx_fprime, check_grad

    # -------------------------------- check _grad_log_C
    n_r = 5
    a = 0.5 * np.ones(n_r)
    a = 1.+ np.arange(10)

    print('*** Checking _grad_log_C:')

    print(f'_log_C({a}) = {_log_C(a)}')

    eps = 1.e-6

    print('approx gradient = ', approx_fprime(a, _log_C, epsilon=1e-6))
    print('exact  gradient = ', _grad_log_C(a))

    err = check_grad(_log_C, _grad_log_C, a, epsilon=1e-6)
    print('check_grad err = ', err)

    # print('\n*** Checking _grad_conc_ll:')
