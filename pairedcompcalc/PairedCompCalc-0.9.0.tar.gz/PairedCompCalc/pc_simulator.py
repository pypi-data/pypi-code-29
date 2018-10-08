"""class PairedCompSimulator
generates simulated paired-comparison data for a group of subjects,
drawn at random from a population with given perceptual characteristics.

Method run():
simulates all paired-comparison data and saves data in files,
just like data from a real experiment.

Method gen_dataset():
simulates all paired-comparison data, stored in a
PairedCompDataSet object, without saving any data files.
This object can be used directly as input for learning a
PairedCompResultSet with all analysis results.

NOTE: for now, these methods can only simulate ONE population at a time,
i.e., only ONE group and ONE attribute.
More than one (test_factor, tf_category) pair may be given, but
the population distribution will be the same in all test conditions.
This may be extended in future versions.

*** Helper classes
SubjectThurstone simulates a subject's decisions using the Thurstone Case V model
SubjectBradley simulates a subject's decisions using the Bradley-Terry-Luce (BTL) model

*** Version History:
2018-03-18, allow inter-individual variations in simulated population
2018-04-27, changed internal simulator structure and call signatures
2018-08-13, adapted for new simplified PairedCompRecord structure
2018-10-02, modified for PairedCompFile structure
"""

import numpy as np
from scipy.stats import randint, uniform, norm
import itertools
# import string
import logging

from .safe_logistic import logistic

from .pc_data import StimRespItem
from .pc_data import PairedCompDataSet
from .pc_file_json import PairedCompFile
from .pc_base import PairedCompItem

# ******* define default response limits here, allow as arguments ???

LOG_WIDTH_SCALE = 0.2   # ???
# = std.dev of random log relative interval width variations, not used

logger = logging.getLogger(__name__)
# logger.setLevel(logging.DEBUG)  # test


# --------------------------------------- subject response models
class SubjectThurstone:
    """simulate one individual participant in a paired-comparison experiment.
    The subject responds using the Thurstone Case V choice model.
    """
    def __init__(self, q, response_limits):
        """
        :param q: list with system quality values in Thurstone d-prime scale
        :param response_limits: array with non-negative response-interval lower limits,
            in Thurstone d-prime units

        NOTE: in a forced_choice experiment, min(response_limits) == 0.,
        so response == 0 becomes impossible.
        """
        self.quality = q
        # = individual quality params for this subject
        self.response_limits = response_limits

    def __repr__(self):
        return f'SubjectThurstone(q= {repr(self.q)}, response_limits= {repr(self.response_limits)})'

    @property
    def n_response_magn(self):
        return len(self.response_limits)+1

    def response(self, pair):
        """Simulate response to one paired-comparison presentation
        :param pair: tuple (i,j) with indices to self.quality
        :return: scalar integer r
            r is determined by decision variable x, as
            r = 0 iff -self.response_limits[0] < x < +self.response_limits[0]
                (i.e., cannot happen if self.response_limits[0] == 0, i.e., forced_choice)
            r = i iff self.response_limits[i-1] <= x < self.response_limits[i]
            r = -i iff -self.response_limits[i] < x <= -self.response_limits[i-1]
        """
        (i,j) = pair
        d = self.quality[j] - self.quality[i]
        x = self.decision_variable(d)
        return int(sum(abs(x) >= self.response_limits)) * (1 if x > 0 else -1)

    @staticmethod
    def decision_variable(d):
        """Generate one random decision variable from Thurstone model
        Input:
        d = scalar quality difference in Thurstone d-prime units
        """
        return norm.rvs(loc=d, scale=np.sqrt(2))


class SubjectBradley(SubjectThurstone):
    """Simulate one individual participant in a paired-comparison experiment.
    The subject responds using the Bradley-Terry-Luce choice model,
    with parameters defined in the log domain.

    NOTE: to facilitate comparisons, the model is initialized by parameters
    defined in the THURSTONE scale, and transformed internally.
    """
    def __init__(self, q, response_limits):
        """
        :param q: list with system quality values in Thurstone d-prime scale
        :param response_limits: array with non-negative response-interval lower limits,
            in Thurstone d-prime units

        NOTE: in a forced_choice experiment, min(response_limits) == 0.,
        so response == 0 becomes impossible.
        """
        super().__init__(q, response_limits)
        self.quality = thurstone2bradley(self.quality)
        self.response_limits = thurstone2bradley(self.response_limits)

    def __repr__(self):
        return f'SubjectBradley(q= {repr(self.q)}, response_limits= {repr(self.response_limits)})'

    def decision_variable(self, d):
        return logistic.rvs(loc=d)


# -------------------------------------------------------------------------
class PairedCompSimulator:
    """Defines a simulated paired-comparison experiment.
    Method run() generates and saves simulated data for one group of participants
    drawn from a population with given properties.
    Method gen_dataset() generates a PairedCompDataSet without saving any files.
    """
    # ******* Let user define response limits here, too !!!

    def __init__(self, pcf,
                 quality_mean,
                 quality_std=0.,
                 n_replications=3,  # i.e., 3 for (A, B) and 3 for (B, A)
                 lapse_prob=0.,
                 pair_different=True):
        """
        :param pcf: PairedCompFrame instance, defining experimental structure
        :param quality_mean: 1D array-like list with mean model parameters, one for each tested system,
            in the simulated population.
        :param quality_std: scalar inter-indiviual standard deviation of quality parameters
            in the simulated population.
        :param n_replications: number of presentations of each ordered pair
            NOTE: pair (A,B) and (B,A) are counted separately, so total number of
            unordered A vs. B comparisons is 2 * n_replications
        :param lapse_prob: probability of random lapse response
        :param pair_different: boolean, allow only different systems to be compared
        """
        self.pcf = pcf
        if len(quality_mean) != self.pcf.n_systems:
            raise RuntimeError('Length mismatch for systems and quality parameters')
        self.quality_mean = np.array(quality_mean)
        self.quality_std = quality_std
        self.quality = None
        # = list of actual values for individual participants
        #   to be calculated later when group size is defined.
        if self.pcf.forced_choice:
            self.response_limits = np.arange(0., pcf.n_response_labels, 1.)
            # = upper limits of response intervals,
            #   i.e. empty interval (-0., 0.) for non-allowed "zero" response
        else:
            self.response_limits = 0.5 + np.arange(0., pcf.n_response_labels - 1, 1.)
            # interval for "zero" difference is (-0.5, +0.5)
        self.n_replications = n_replications
        self.lapse_prob = lapse_prob
        self.pair_different = pair_different

    def __repr__(self):
        return ('PairedCompSimulator(' +
                f'\n\tpcf= {repr(self.pcf)}, ' +
                f'\n\tquality_mean= {repr(self.quality_mean)}' +
                f'\n\tquality_std= {repr(self.quality_std)}, ' +
                f'\n\tn_replictations= {repr(self.n_replications)}, ' +
                f'\n\tlapse_prob= {repr(self.lapse_prob)}, ' +
                f'\n\tpair_different= {repr(self.pair_different)}' +
                '\n\t)')

    @property
    def n_systems(self):
        return self.pcf.n_systems

    @property
    def n_response_labels(self):
        return self.pcf.n_response_labels

    def gen_group_params(self, n_subjects):
        """Generate random subject parameters for one group of subjects
        :param n_subjects: integer number of subjects in the group
        :return: None
        Result: calculated parameters
            self.quality = array of quality parameters
            self.quality.shape == (n_subjects, len(self.quality_mean))
        """
        # ************* response_limits should also be individually randomized ???

        m = self.quality_mean
        s = self.quality_std
        self.quality = m + s * norm.rvs(size=(n_subjects, len(m)))
        self.quality -= self.quality[..., :1]

    def gen_dataset(self, n_subjects=1,
                    subject_class=SubjectThurstone,
                    group=''):
        """Generate a complete PairedCompDataSet for one experiment,
        with ONE group of subjects drawn from given population,
        and ONE session for each subject.
        :param n_subjects: number of participants
        :param subject_class: probability model for decision variable
        :param group: (optional) string name of this subject group
        :return: a single PairedCompDataSet object

        NOTE: ****** for now, SAME quality parameters in all test conditions
        2018-08-13, simplified PairedCompDataSet dict nesting
        """
        def sim_one_subject(q):
            """Generate data for ONE subject in all test conditions
            for ONE externally known attribute
            :param q: actual quality vector for this subject
            :return: list of StimRespItem objects, one for each replication,
                for all required test conditions
            """
            # res = {tc: self.run_one_session(subject_class(q,
            #                                               self.response_limits))
            #        for tc in self.pcf.test_conditions()}  # **************************
            res = self.run_one_session(subject_class(q, self.response_limits))
            # convert test-cond dicts to tuples:
            return [StimRespItem(r.S, r.R, tuple(r.T.values()))
                    for r in res]
        # ----------------------------------------------------------------

        subjects = [f'Subject{i}' for i in range(n_subjects)]
        self.gen_group_params(n_subjects)
        pcd_g = {a: {s_id: sim_one_subject(q)
                     for (s_id, q) in zip(subjects, self.quality)}
                 for a in self.pcf.attributes}
        return PairedCompDataSet(self.pcf, {group: pcd_g})

    def run(self, n_subjects=1,
            subject_class=SubjectThurstone,
            result_path='./test'):
        """run a complete simulated experiment
        with ONE group of subjects drawn from given population,
        and ONE session for each subject.
        :param n_subjects: number of participants
        :param subject_class: probablity model for decision variable
        :param result_path: (optional) Path or string name of directory for result files,
            incl group sub-directory if desired.
        :return: None

        Result: one PairedCompRecord file saved in result_path for each subject
        """
        self.gen_group_params(n_subjects)
        for n in range(n_subjects):
            # self.set_random_response_limits()
            # session = PairedCompRecord(subject=f'Subject{n}',
            #                            # response_labels=self.pcf.response_labels,
            #                            # systems=self.pcf.systems,
            #                            attribute=self.pcf.attributes[0],
            #                            # forced_choice=self.pcf.forced_choice,
            #                            comment='Simulated test')
            s = subject_class(self.quality[n], self.response_limits)
            # session.result = self.run_one_session(s)
            # session.save(result_path)  # default format ='json'
            result = self.run_one_session(s)
            subject = f'Subject{n}'
            items =[PairedCompItem(subject=subject,
                                   attribute=self.pcf.attributes[0],
                                   pair=r.S,
                                   response=r.R,
                                   test_cond=r.T)
                    for r in result]
            file = PairedCompFile(items).save(dir=result_path, file_name=subject+'.json')
            logger.info(f'quality params. in {subject} = {s.quality}')

    def run_one_session(self, s):
        """run_one_session wih one simulated subject in ALL test conditions
        :param s: single SubjectThurstone or SubjectBradley instance
        :return: list of StimRespItem objects with a simulated responses
        """
        res = []
        # = list of StimRespItem objects
        for tc in self.pcf.gen_test_factor_category_tuples():
            for ij in self.system_pairs():
                sys_pair = (self.pcf.systems[ij[0]], self.pcf.systems[ij[1]])  # pair labels
                res.extend([StimRespItem(sys_pair, self.sim_result(s, ij), dict(tc))
                            for _ in range(self.n_replications)])
        return res

    def system_pairs(self):
        """generator of all allowed pairs to be presented
        Each pair is a tuple (i, j) with indices into self.quality and self.pcf.systems
        """
        if self.pair_different:
            return itertools.permutations(range(self.n_systems), 2)
            # no pairs presented with equal system indices, like (1, 1)
        else:
            return itertools.product(range(self.n_systems), 2)
            # pairs may include tuples with equal system indices, like (1, 1)

    def sim_result(self, s, pair):
        """Simulate a single paired-comparison result from presented pair.
        :param s: single SubjectThurstone or SubjectBradley instance
        :param pair: tuple (i,j) with indices into self.quality
        :return: scalar integer r in {- self.n_response_labels, ..., + self.n_response_labels }
            except excluding 0 if self.pcf.forced_choice
        """
        if self.lapse():
            return self.lapse_result()
        else:
            return s.response(pair)

    def lapse(self):
        """Generate True with prob = self.lapse_prob
        """
        return uniform.rvs(0, 1.) < self.lapse_prob

    def lapse_result(self):
        """Generate a random result, disregarding quality parameters
        :return: scalar integer
            in {-n_response_labels, ...,-1, +1,..., + n_response_labels}, if forced_choice
            in {-n_response_labels+1, ...,0, ...,  + n_response_labels-1}, if not forced_choice
            i.e., excluding 0 if self.pcf.forced_choice
        """
        if self.pcf.forced_choice:
            return ((-1 if uniform.rvs() < 0.5 else +1) *
                    randint.rvs(low=1, high=self.n_response_labels + 1))
        else:
            return randint.rvs(low=-self.n_response_labels + 1,
                               high=self.n_response_labels)


# ------------------------------------- internal help function:
def thurstone2bradley(x):
    """transform parameters defined on Thurstone d-prime scale,
    to equivalent parameters on the BTL model scale
    :param: x = array or array-like list of values
    :return: array with transformed values
    """
    return logistic.ppf(norm(scale=np.sqrt(2)).cdf(x))


