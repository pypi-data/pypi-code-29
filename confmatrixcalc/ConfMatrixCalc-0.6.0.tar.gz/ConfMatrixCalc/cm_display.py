"""This module defines classes and functions to display
estimated results from analysis of confusion-matrix data.

The probabilistic models for display are obtained
from a single cm_model.ConfMatrixResultSet instance.

Results are shown as figures and tables.
Tables can be saved in LaTeX tabular format OR in tab-delimited text files.

*** Main Display Classes:

ConfMatrixDisplaySet: a structured container for all display results

GroupDisplaySet: a container for all results for a single subject group,
    (1) estimated for the population from which subjects were recruited,
    (2) estimated for each individual test participant.

GroupEffectSet: container for result differences between groups,
    if the experiment included more than one group.

PopulationResult: all results estimated for a population, including
    (1) Mutual Information (MI) between stimulus and response phoneme categories.
    (2) Probability of Correct (PC) phoneme recognition.
    (3) Response Probabilities in confusion-matrix cells.
    (4) Credible differences between test conditions for these measures.

IndividualResultSet: results for all subjects in one group of participants:
    (1) Boxplot overview of individual results.
    (2) Individual results for each participant.

SubjectResult: results for one participant

Each display element can be accessed and modified by the user script, before saving.


*** Usage Example:

cm_display = ConfMatrixDisplaySet.display(cm_result, **kwargs)
cm_display.save(result_dir)

Here,
    cm_result is a cm_model.ConfMatrixResultSet instance,
    kwargs are optional keyword arguments controlling display details, e.g.,
    table_format= 'latex',
    figure_format= 'eps'

    result_dir is the top directory where all results are saved.

Display elements of the cm_display object may be modified, if desired,
before saving.

Figures and tables are assigned descriptive names,
and stored in sub-directories and files with names constructed from
names of groups and subjects,
and labels of performance measures.

If there is more than one Group,
one sub-directory is created for each group.


*** Global module parameters that may be changed by user:

credibility_limit: scalar smallest joint credibility to be listed
diff_threshold: scalar difference threshold to prevent spurious random differences
measures: dict with elements (measure_label, measure_fcn)
defining overall performance measures to be calculated and displayed,
    default= {'MI': mutual_information,
              'PC': prob_correct}
A user can add new overall performance measures,
but must then also define a new function to perform the calculation.


*** Version History:
2018-09-14 first functional version
"""
# ********* measure diff credibility plot ??
# ********* tabulate measure-diff for 1, 2, ... all test factors ???

import numpy as np
from pathlib import Path
import logging
from string import whitespace

from . import cm_display_format as fmt
from .cm_model import mutual_information, prob_correct

from samppy.credibility import cred_diff


logger = logging.getLogger(__name__)


# ---------------------------- Measure Labels:
MI = 'MI'
PC = 'PC'

# ---------------------------- Default display parameters
# PERCENTILES = [5., 50., 95.]  # ********** moved to format_display
# MUST have exactly three values, with median in the middle
# ***** set only min-max, always include median ??? ***

# CREDIBILITY_LIMIT = 0.6
# DIFF_THRESHOLD = 0.001

FMT = {'credibility_limit': 0.6,
       'diff_threshold': 0.001,
       'measures': {'MI': mutual_information,
                    'PC': prob_correct}
       }
# dict for display variables

N_SAMPLES = 1000  # ****************************************
# = number of samples used for each ResponseProbModel instance


def set_format_param(credibility_limit=None,
                     diff_threshold=None,
                     measures=None,
                     **kwargs):
    """Set / modify format parameters for this module
    :param credibility_limit: sorted list of percentile values (in percent)
    :param diff_threshold: minimum difference to be counted for phoneme response probabilities
    :param measures: dict with (measure_label, measure_fcn) elements
    :param kwargs: dict with any OTHER formatting variables,
        just passed to module format_display
    :return: None
    """
    if credibility_limit is not None:
        FMT['credibility_limit'] = credibility_limit
    if diff_threshold is not None:
        FMT['diff_threshold'] = diff_threshold
    if measures is not None and len(measures) > 0:
        for (m, m_fcn) in measures.items():
            FMT['measures'][m] = m_fcn
    fmt.set_format_param(**kwargs)


# -------------------------------- Main Module Function Interface
def display(cm_resultset, **kwargs):
    """Main function to display default set of paired-comparison results.
    :param: cm_resultset: a single PairedCompResultSet object
        with learned models saved in a nested dict as
        model = cm_resultset.models[group][attribute][subject]
    :param: kwargs: (optional) any format spec. for format_display module
    :return: single QualityDisplaySet instance with display results
    """
    return ConfMatrixDisplaySet.display(cm_resultset, **kwargs)


# ---------------------------------------------- Elementary Display Classes:

class DisplayNode:
    """Superclass for elements in a ConfMatrixDisplaySet structure
    allowing pretty printing of ConfMatrixDisplaySet contents.
    """
    def __repr__(self, indent=1):
        """Super-method common for all sub-classes,
        with indented repr for object sub-variables.
        :param indent: integer indentation level for object sub-variables.
        :return: string
        """
        def dict_repr(dict_v, indent):
            """ Sub-method for dict variables, which may contain DisplayNode values.
            """
            tabs = '\n' + indent * '\t'
            return ('{' + tabs
                    + (',' + tabs).join(f'{repr(k)}: {sub_repr(v, indent+1)}'
                                        for (k, v) in dict_v.items())
                    + tabs + '}')
        # -------------------------------------------------

        def sub_repr(var, indent):
            if isinstance(var, DisplayNode):
                return var.__repr__(indent+1)
            elif isinstance(var, dict):
                return dict_repr(var, indent+1)
            else:
                return repr(var)
        # -------------------------------------------------

        tabs = '\n' + indent * '\t'
        return (self.__class__.__name__ + '(' + tabs
                + (','+tabs).join(f'{k}={sub_repr(v, indent)}'
                                  for (k, v) in vars(self).items())
                + ')')


class MeasureRange(DisplayNode):
    """Plot and table display of ONE scalar performance measure vs. test conditions.
    """
    def __init__(self, plt=None, tab=None):
        """
        :param plt: (optional) a fmt.FigureRef instance with percentile plot
        :param tab: (optional) a fmt.TableRef instance with corresponding range table
        """
        self.plt = plt
        self.tab = tab

    def save(self, dir):
        """Save self to given directory
        :param dir: string or path
        :return: None
        """
        if self.plt is not None:
            self.plt.save(dir)
        if self.tab is not None:
            self.tab.save(dir)

    @classmethod
    def display(cls, m_samples, m_label, tf_list):
        """Create percentile displays, with
        plt = a plot of percentiles vs. max TWO test_factors
        tab = a table of percentiles vs. ALL test_factors
        :param m_samples: array of samples for this measure
            m_samples[n, t] = n-th sample for t-th combination of test-factor categories
            corresponding to cmf.test_conditions()[t]
        :param m_label: string name of this measure
        :param tf_list: list of one or more tuples (test_factor, tf_category_list), where
            prod(len(tf_category_list)) == m_samples.shape[-1]
        :return: single cls instance with plot and table displays
        """
        # tf_list = list(cmf.test_factors.items())
        return cls(plt=fmt.fig_percentiles(m_samples, tf_list, m_label),
                   tab=fmt.tab_percentiles(m_samples, tf_list, m_label))


class MeasureDiff(DisplayNode):
    """Plot and table of credible differences between test conditions
    for ONE performance measure, with properties
    plt with differences between first test_factor categories,
    pooled across all remaining test factors.
    table of differences between first test_factor categories,
    for ALL combinations of remaining test-factor categories.
    """
    def __init__(self, tab=None):  # ************ plt, tab):
        """
        :param plt: a fmt.FigureRef instance with a credible_diff plot
        :param tab: a fmt.TableRef instance with corresponding table
        """
        # self.plt = plt
        self.tab = tab

    def save(self, dir):
        """
        Save self to given directory
        :param dir: string or path
        :return: None
        """
        # if self.plt is not None:
        #   self.plt.save(dir)  # *****************
        if self.tab is not None:
            self.tab.save(dir)

    @classmethod
    def display(cls, m_samples, m_label, tf_list):
        """Create fig and tab percentile display
        :param m_samples: array of samples for this measure
            m_samples[n, t] = n-th sample for t-th test condition
            identified by cmf.test_conditions()[t]
        :param m_label: string name of this measure
        :param tf_list: list of one or more tuples (test_factor, tf_category_list), where
            prod(len(tf_category_list)) == m_samples.shape[-1]
        :return: single cls instance with plot and table displays
        """
        n_tfc = [len(t[1]) for t in tf_list]
        # prod(n_tfc) == m_samples.shape[-1]
        if m_samples.shape[-1] == 1:
            return cls(tab=None)
        if len(tf_list) == 1:
            diff = cred_diff(m_samples,
                             diff_axis=1, sample_axis=0,
                             p_lim=FMT['credibility_limit'])
        else:
            m_samples = m_samples.T.reshape((n_tfc[0], np.prod(n_tfc[1:], dtype=int), -1))
            # m_samples[t, ..., s] = s-th sample for tf=tf_list[0][0], tf_cat=tf_list[0][1][t]
            diff = cred_diff(m_samples,
                             diff_axis=0, case_axis=1, sample_axis=2,
                             p_lim=FMT['credibility_limit'])
        return cls(tab=fmt.tab_credible_diff(diff, tf_list, m_label))


class CellDiff(DisplayNode):
    """Display groups of phoneme stimulus-response cells with
    jointly credibly different response probabilities
    between categories in the main FIRST test factor,
    for some combination of categories in secondary test factor(s).
    For now, only a table is presented.
    Plot display may be added in a future version.
    """
    def __init__(self, tab):
        # ******************** ? self.plt = plt
        self.tab = tab

    def save(self, dir):
        if self.tab is not None:
            self.tab.save(dir)

    @classmethod
    def display(cls, u, cmf, tf_list=None):
        """Make table of stimulus-response cells with credibly different response probabilities
        among some pair of test-factor categories
        :param u: 4D array of response probabilities
        :param cmf: a ConfMatrixFrame instance
        :param tf_list: (optional) list of one or more tuples (test_factor, tf_category_list), where
            just in case tf_list != list(cmf.test_factors.items())
        :return: a cls instance
        """
        # calc difference indices here because we may want both table and figure display
        # of the same result
        (n, n_t, n_s, n_r) = u.shape
        if n_t == 1:
            return cls(tab=None)
        if tf_list is None:
            tf_list = list(cmf.test_factors.items())
        u_calc = u.reshape((n, len(tf_list[0][1]), -1))
        diff = cred_diff(u_calc,
                         diff_axis=1, sample_axis=0, case_axis=2,
                         p_lim=FMT['credibility_limit'],
                         threshold=FMT['diff_threshold'])
        return cls(tab=fmt.tab_credible_cell_diff(diff, u_calc, cmf, tf_list))


# ---------------------------------------------------------- Main Display Class:
class ConfMatrixDisplaySet(DisplayNode):
    """Root container for all displays from one ConfMatrixResultSet object.
    All display elements can be saved as files within a selected directory tree.
    The complete instance can also be serialized and dumped to a single pickle file,
    then re-loaded, edited if needed, and re-saved.
    """
    def __init__(self, groups, group_effects=None):
        """
        :param groups: dict with (group: GroupDisplaySet) elements
        :param group_effects: (optional) single GroupEffectSet instance,
            showing differences between groups, if there is more than one group
        """
        self.groups = groups
        self.group_effects = group_effects

    def save(self, dir_top):
        """Save all displays in a directory tree
        :param dir_top: Path or string with top directory for all displays
        :return: None
        """
        dir_top = Path(dir_top)  # just in case
        for (g, g_display) in self.groups.items():
            g = _dir_name(g)
            if len(g) == 0 or all(s in whitespace for s in g):
                g_display.save(dir_top)
            else:
                g_display.save(dir_top / g)
        if self.group_effects is not None:
            self.group_effects.save(dir_top)
        logger.info(fig_comments(fmt.FMT['percentiles']))
        logger.info(table_comments())
        logger.info(f'All result displays saved in {dir_top} and sub-directories')

    @classmethod
    def display(cls, cm_result_set, **kwargs):
        """Create displays for all results from a phoneme-identification experiment,
        and store all display elements in a single structured object.
        :param cm_result_set: a cm_model.ConfMatrixResultSet instance, with
            cm[group] = a cm_model.ResponseProbGroup instance
        :param: kwargs: (optional) any keyword format specifications
            just passed on to format_display module
        :return: a single new cls instance
        """
        set_format_param(**kwargs)
        if len(cm_result_set.groups) > 1:
            group_effects = GroupEffectSet.display(cm_result_set.groups)
        else:
            group_effects = None
        # display separate results for each group
        groups = {g: GroupDisplaySet.display(g_model)
                  for (g, g_model) in cm_result_set.groups.items()}
        # including one extra overall group with all groups merged, if more than one

        return cls(groups, group_effects)


# ---------------------------------------------------- Second-level Display Classes:
class GroupDisplaySet(DisplayNode):
    """Container for all displays related to a single group,
    all derived from one cm_model.ConfMatrixResultSet instance.
    """
    def __init__(self, population, individual):
        """
        :param population: PopulationResult instance, showing
            results for the population from which the group was recruited
        :param individual: IndividualResultSet instance showing individual results.
        """
        self.population = population
        self.individual = individual

    def save(self, dir):
        """
        :param dir: Path instance to directory to save displays for this group
        :return: None
        """
        self.population.save(dir)
        if self.individual is not None:
            self.individual.save(dir)

    @classmethod
    def display(cls, g_model):  
        """Generate all displays for a given group
        :param g_model: a cm_model.ResponseProbGroup instance
        :return: a GroupDisplaySet instance with all displays for this group
        """
        population = PopulationResult.display(g_model.population)
        subjects = IndividualResultSet.display(g_model.subjects, g_model.cmf)
        return cls(population, subjects)


# ------------------------------------------ Third-level Display Classes:
class PopulationResult(DisplayNode):
    """Container for all population displays
    """
    def __init__(self, measures, cells):
        """
        :param measures: a dict with (measure_label, MeasureDisplaySet instance)
            default is MI and PC
        :param cells: a CellDisplaySet instance with results for
            phoneme stimulus-response cells in a confusion matrix
        """
        self.measures = measures
        self.cells = cells

    def save(self, dir):
        """Save all stored display objects in specified directory
        :param dir: Path instance for save directory
        :return: None
        """
        for (m, m_data) in self.measures.items():
            m_data.save(dir)
        if self.cells is not None:
            self.cells.save(dir)

    @classmethod
    def display(cls, population):
        """Display results for one population
        :param population: a ResponseProbPopulation object
            = cm_model.ResponseProbGroup.population
        :return: a cls instance
        """
        measures = dict()
        cmf = population.cmf
        # ConfMatrixFrame object, defining contents of u sample array
        u = population.rvs(n_samples=N_SAMPLES)
        tf_list = list(cmf.test_factors.items())
        for (m, m_fcn) in FMT['measures'].items():
            measures[m]= MeasureDisplaySet.display(m_fcn(u, cmf),
                                                   m, tf_list)
        cells = CellDisplaySet.display(u, cmf)
        return cls(measures, cells)


class IndividualResultSet(DisplayNode):
    """Container of displays for individual listeners
    """
    def __init__(self, measures, subjects):
        """
        :param measures: a dict with (measure_label, MeasureDisplaySet instance)
            default is MI and PC
        :param subjects: dict with items (subject, SubjectResult instance)
        """
        self.measures = measures
        self.subjects = subjects

    def __repr__(self, indent=1):
        tabs = '\n' + indent * '\t'
        return (self.__class__.__name__ + '(' +
                ''.join(tabs + f'{m}= {repr(m_data)}'
                        for (m, m_data) in self.measures.items()) +
                tabs + 'subjects=subjects)')

    def save(self, dir):
        """Save all stored display objects in specified directory
        Overall results across subjects stored in group directory.
        Individual subject results stored in sub-directory tree.
        """
        for (m, m_data) in self.measures.items():
            m_data.save(dir)
        dir = dir / 'subjects'
        for (s, s_disp) in self.subjects.items():
            s_disp.save(dir / s)

    @classmethod
    def display(cls, g_subjects, cmf):
        """Display results for group of individual
        :param g_subjects: dict = ResponseProbGroup.individual
        :param cmf: dict = a ConfMatrixFrame instance
        :return: a cls instance
        """
        subjects = dict()
        # subjects[s][XX] = table of credible differences in measure XX for subject s
        s_measures = {m:[] for m in FMT['measures'].keys()}
        # = space for individual point estimates
        measures = dict()
        # space for final boxplots
        for (s, s_model) in g_subjects.items():
            subjects[s] = SubjectResult.display(s_model)
            u = s_model.rvs(N_SAMPLES)  # ******* let SubjectResult do this ******
            for (m, m_fcn) in FMT['measures'].items():
                s_m = _reshape_test_cond_samples(m_fcn(u, cmf), cmf)
                s_measures[m].append(np.median(s_m, axis=-1))

        tf_list = list(cmf.test_factors.items())
        for (m, m_data) in s_measures.items():
            measures[m] = fmt.fig_indiv_boxplot(m_data, tf_list, m)
        return cls(measures, subjects)


# ------------------------------------------------ Fourth-level Display Classes

SubjectResult = PopulationResult


# class SubjectResult(DisplayNode):   # ****** different from PopulationResult ???
#     """
#     Result displays for ONE test participant
#     """
#     # **** include diff ?
#     # **** include plots ?
#     # *** i.e., use complete MeasureRange, MeasureDiff ???
#
#     def __init__(self, mi, pc):   # ****** cells ? diff ?
#         """
#         :param mi: TableRef with percentile table
#         :param pc: TableRef with percentile table
#         """
#         self.mi = mi
#         self.pc = pc
#
#     def save(self, dir):
#         """
#         :param dir: directory for saving results for this subject
#         :return: None
#         """
#         self.mi.save(dir)
#         self.pc.save(dir)
#
#     @classmethod
#     def display(cls, u, cmf):
#         """Create result tables for one given test participant.
#         :param s_model: one ResponseProbIndividual instance
#         :param u: array of ResponseProb samples
#         :return: a cls instance
#         """
#         tf_list = list(cmf.test_factors.items())
#         # u = s_model.rvs(N_SAMPLES)
#         s_mi = mutual_information(u, cmf)
#         s_pc = prob_correct(u, cmf)
#         return cls(mi=fmt.tab_percentiles(s_mi, tf_list, MI),
#                    pc=fmt.tab_percentiles(s_pc, tf_list, PC)
#                    )


class MeasureDisplaySet(DisplayNode):
    """Container of displays for one performance measure
    """
    def __init__(self, range, diff=None):
        """
        :param range: single MeasureRange object with results vs. test conditions
            showing credible-range plot and corresponding table
        :param diff: (optional) MeasureDiff object with credible differences
            between test conditions, or between groups,
            showing plot and table of credibly different test conditions
        """
        self.range = range
        self.diff = diff

    def save(self, dir):
        """Save display objects in specified directory
        :param dir: path to directory for saving
        :return: None
        """
        self.range.save(dir)
        if self.diff is not None:
            self.diff.save(dir)

    @classmethod
    def display(cls, m_samples, m_label, tf_list):
        """Create all displays for one performance measure
        :param m_samples: array of samples for this measure
            m_samples[n, t] = n-th sample for t-th test condition
            identified by cmf.test_conditions()[t]
        :param m_label: string name of this measure
        :param tf_list: list of one or more tuples (test_factor, tf_category_list), where
            prod(len(tf_category_list)) == m_samples.shape[-1]
        :return: single cls instance with all displays
        """
        if m_samples.shape[-1] > 1:
            return cls(MeasureRange.display(m_samples, m_label, tf_list),
                       MeasureDiff.display(m_samples, m_label, tf_list))
        else:
            return cls(MeasureRange.display(m_samples, m_label, tf_list))


class CellDisplaySet(DisplayNode):
    """Container for displays illustrating response-probability matrices,
    and jointly credible groups of matrix-cell differences
    among test conditions or groups
    """
    def __init__(self, cm=None, diff=None):
        """
        :param cm: a ResponseProb instance with display of
            response-prob figs and tables for each test condition ??? NOT IMPLEMENTED ******
        :param diff: a CellDiff instance identifying a group of cells
        with jointly credible differences between any pair of main test-factor categories,
        in some combination of sub-test-factor categories, if there is more than one test factor.
        """
        self.cm = cm
        self.diff = diff

    def save(self, dir):
        if self.cm is not None:
            self.cm.save(dir)
        if self.diff is not None:
            self.diff.save(dir)

    @classmethod
    def display(cls, u, cmf, tf_list=None):
        """Display overall confusion-matrices with
        a response-probability estimate for each cell
        :param u: array of response-prob samples, stored as
            u[n, t, s, r] = n-th sample of probability of
            r-th response to s-th stim_range in t-th test condition
        :param cmf: a ConfMatrixFrame instance
        :param tf_list: (optional) list of one or more tuples (test_factor, tf_category_list), where
            just in case tf_list != list(cmf.test_factors.items())
        :return: a single cls instance
        """
        if tf_list is None:
            tf_list = list(cmf.test_factors.items())
        # cm display *********** ?
        return cls(diff=CellDiff.display(u, cmf, tf_list))


# --------------------------------------------

class GroupEffectSet(DisplayNode):
    """Container for all displays illustrating differences between subject groups.
    """
    def __init__(self, measures, cells):
        """
        :param measures: a dict with (measure_label, MeasureDisplaySet instance)
        :param cells: CellDisplaySet instance showing results for (stim_range, resp_range) pairs
        """
        self.measures = measures
        self.cells = cells

    def save(self, dir):
        """Save all stored display objects in specified directory
        :param dir: Path instance for save directory
        :return: None
        """
        for (m, m_data) in self.measures.items():
            m_data.save(dir)
        if self.cells is not None:
            self.cells.save(dir)

    @classmethod
    def display(cls, groups):
        """Create displays to show differences between groups
        :param groups: dict with elements (group_label, g_model),
            = ConfMatrixResultSet.groups instance
        :return: a single cls instance
        """
        g_labels = [g for g in groups.keys()
                    if type(g) is not tuple]
        u = np.array([g.population.rvs(n_samples=N_SAMPLES) for g in groups.values()
                      if type(g) is not tuple])
        (n_g, n, n_t, n_s, n_r) = u.shape
        u = u.transpose((1, 0, 2, 3, 4)).reshape((n, n_g * n_t, n_s, n_r))
        cmf = groups[g_labels[0]].cmf
        tf_list = [('Groups', g_labels)] + list(cmf.test_factors.items())
        # Now using groups as the main test factor
        measures = dict()
        for (m, m_fcn) in FMT['measures'].items():
            measures[m]= MeasureDisplaySet.display(m_fcn(u, cmf),
                                                   m, tf_list)
        cells = CellDisplaySet.display(u, cmf, tf_list)
        # must have separate tf_list, because it may include groups
        return cls(measures=measures, cells=cells)


# ---------------------------------- Module-internal Help Functions:

def _reshape_test_cond_samples(m_samples, cmf):
    """Re-arrange sample array with max ONE or TWO test-factor dimensions
    suitable for plot displays.
    :param m_samples: 2D array of samples of one performance measure
        m_samples[n, t] = n-th sample for t-th test condition
        m_samples.shape[-1] == prod(cmf.n_test_factor_conditions)
    :param cmf: a ConfMatrixFrame instance, providing test-condition labels
    :return: measures[t0, n] or [t0, t1, n] for n-th sample value
        in cmf.test_factors[0][t0] (and cmf.test_factors[1][t1], if more than one)
    """
    n_tfc = cmf.n_test_factor_conditions
    if len(cmf.test_factors) > 1:
        return m_samples.T.reshape((*n_tfc[:2], -1))
    else:
        return m_samples.T


def _dir_name(g):
    """make sure group name is a possible directory name
    :param g: string or tuple of strings
    :return: string to be used as directory
    """
    if type(g) is tuple:  # several strings
        g = '+'.join(s for s in g)
    return g


def fig_comments(perc):
    """Generate figure explanations.
    :param perc: vector with percentile values
    :return: long comment string
    """
    p_min = np.amin(perc)
    p_max = np.amax(perc)
    c = f"""Figure Explanations:
    
Figure files with names like XX_TF.eps 
display medians (middle marker symbol) and credible intervals (vertical bars) 
for performance measure XX vs. test factors TF, 
estimated for the population from which test individual were recruited.
Vertical bars show the range between {p_min:.1f}- and {p_max:.1f}- percentiles.

The credible ranges include all uncertainty
caused both by real inter-individual perceptual differences
and by the limited number of phoneme presentations for each listener.

Figure files with names like XX-boxplot_TF.eps 
show similar boxplots of point-estimated (median) individual results
for performance measure XX vs. test factors TF.

If there are more than one test-factor, plots are shown 
only for the first and second test factor,
with percentile values averaged across other test factor categories.
"""
    return c


def table_comments():
    c = """Table Explanations:

*** Tables of Percentiles:
Figure files with names like XX_TF.txt or XX_TF.tex  
show numerical versions of the information in percentile plots,
including all test factors if there are more than one.

*** Tables of Credible Differences:
Files with names like XX-diff_TF.tex or XX-diff_TF.txt 
show a list of test-condition pairs, where
the XX results are ALL JOINTLY credibly different between test conditions.
The credibility value in each row is the JOINT probability
for the pairs in the same row and all rows above it.

*** Tables of Credibly Different Response Probabilities:
Files with names like Cell-diff_TF.tex or Cell-diff_TF.txt 
show a list of stimulus-response pairs, for which 
the response probabilities are JOINTLY credibly different
between some test conditions.
Each row in the table shows
a phoneme pair, a pair of first test-factor categories,
with median response probabilities (in percent) for each such category,
additional test-conditions, if there is more than one test factor,
and, finally, a credibility value in percent.

The credibility value in each row is the JOINT probability
for the pairs in the same row AND all rows above it.
"""
    return c