"""This module defines classes and functions to
read files with individual results
from phoneme identification experiments.

Phoneme-identification data may be collected for
several test subjects in one or more groups.
Each subject may be tested in one or more test-conditions.

*** Class Overview:

ConfMatrixFrame: defines structure of a phoneme-identification experiment,
    and specifies test conditions to be included in the analysis.

StimRespCountSet: all phoneme-identification data for
    selected group(s), subjects, and test conditions,
    to be used as input for statistical analysis.
    Each subject should be tested in most (or all) test conditions.

StimRespRecord: defines results from tests with ONE subject,
    tested in ONE combination of test conditions,
    defined by one category label for each Test Factor.
    Several instances may be generated from each input file.


*** Input File Formats:

The simplest file format is a json-serialized version of
a sequence of StimRespRecord objects.
Files in this format should be saved with extension 'json'.

Data can also be imported from Excel workbook (xlsx) files.
Each xlsx file may include data for different subjects,
in one or more test conditions.
Each workbook sheet contains data corresponding to ONE StimRespRecord instance.

The most flexible file format is xlsx.
Here, all data fields may be stored at specified cell locations,
or extracted from workbook sheet names,
as defined by keyword parameters to the reader object.
See module cm_data_xlsx for details.


*** Input Data Files:

All input files with data from an experiment must be stored in one directory tree.
If results are to be analyzed for more than one group of test subjects,
the data files for each group must be stored in separate sub-directory trees
starting on the first level just below the top directory.
All sub-directories in the tree are searched recursively for data files.

Each data file may contain phoneme-identification results
for one or more test subject(s) in one or more test-conditions.
File names are arbitrary, although they may be somehow associated with
the encoded name of the participant, to facilitate data organisation.

Files for different test conditions may be stored in separate sub-directories.
The directory name can then be used to indicate a test-factor category,
if the category is not defined in the data file itself.

Several files may include data for the same subject,
e.g., results obtained in different test conditions,
or simply for replicated test sessions with the same subject.

All input data are collected by a single function call, as
ds = StimRespCountSet.load(cmf, dir, groups, fmt='json', **kwargs)

If fmt='json' is specified, the load method reads only files with the 'json' extension
in the top directory defined by the path-string in parameter dir.

If the fmt argument is left unspecified, or if fmt=None, or fmt='',
StimRespCountSet.load will attempt to read ALL files in the designated directory tree,
and use the files that seem to contain phoneme-identification results.

The parameter groups is an optional list of sub-directory names,
one for each participant group.

The parameter cmf is a PairedCompFrame object that defines
the experimental structure and test conditions to be included in the analysis.

Parameter kwargs includes additional required keyword parameters for the given file format.
See cm_read_xlsx for further details.


*** Version History
2018-09-15, first functional version
"""

# **** require Openpyxl only if xlsx input data are actually used ???

# **** allow user to anonymize test-factor names stored in data files ??? ******

import numpy as np
from pathlib import Path
from collections import OrderedDict, Counter
from itertools import product
import logging
import json

from . import cm_data_json
from . import cm_read_xlsx

from .cm_base import FileReadError


logger = logging.getLogger(__name__)


class FileFormatError(FileReadError):
    """Format error causing non-usable data"""


FILE_RECORDS_FCN = {'json': cm_data_json.StimRespFile,
                    'xlsx': cm_read_xlsx.StimRespFile}
# = mapping of format code to a callable file_reader object,
# that creates an iterator of dicts, each corresponding to a StimRespRecord instance.
# The record_fcn is called as record_generator = record_fcn(file_path, **kw)
# where kw are different keyword parameters as required by the file format.

# If a user implements a new file_reader class or function,
# the FILE_RECORDS_FCN must also link a new format code to the new file_reader.

MISSING_LIMIT = 0.3
# = proportion of missing subject test conditions to trigger a warning


# -----------------------------------------------------------------
class ConfMatrixFrame:
    """Defines layout of a phoneme-identification experiment,
    and specifies phoneme data to be analysed.
    """
    def __init__(self,
                 stim=None,
                 stim_count=None,
                 resp=None,
                 correct_resp=None,
                 test_factors=list()):
        """
        :param stim: (optional) list of strings, one for each tested phoneme, e.g., a phonetic symbol
            Assigned / extended with stimulus labels found in input files.
        :param stim_count: (optional) list of presentation counts for each stimulus category,
            proportional to probability mass distribution of presented phonemes.
            Estimated from counts when all data have been collected,
            but may also be assigned by user before calculating results.
        :param resp: (optional) list of strings with response categories.
            Usually equal to stim, sometimes with a NoResponse category added.
            Assigned = stim, if not specified
            Assigned / extended with response labels found in input files.
        :param correct_resp: (optional) dict mapping each stim -> single correct response label
            Usually simply s -> s for all stimulus labels s,
            but in some cases different variants of a stim phoneme may have the same correct response
        :param test_factors: iterable with elements (test_factor, category_list), where
            test_factor is a string,
            category_list is a list of labels for allowed categories within test_factor.
        """
        if stim is None:
            stim = list()
        self.stim = stim
        # if stim_count is None:
        #     stim_count = [1 for _ in range(len(self.stim))]
        # self.stim_count = list(stim_count)
        self.stim_count = stim_count
        if resp is None:
            resp = self.stim.copy()
        self.resp = resp
        # if correct_resp is None:
        #     correct_resp = {s: s for s in self.stim}
        self.correct_resp = correct_resp
        self.test_factors = OrderedDict(test_factors)  # **** or just leave it as a list ???

    def __repr__(self):
        return (f'ConfMatrixFrame(\n\t' +
                ',\n\t'.join(f'{key}={repr(v)}'
                             for (key, v) in vars(self).items()) +
                '\n\t)')

    @property
    def n_test_factor_conditions(self):
        """1D list with number of test-condition alternatives in each test factor"""
        return [len(v) for v in self.test_factors.values()]

    @property
    def n_test_conditions(self):
        """Total number of combined test conditions,
        with one category from each test_factor
        """
        return np.prod(self.n_test_factor_conditions, dtype=int)

    @property
    def conf_matrix_shape(self):
        return self.n_test_conditions, len(self.stim), len(self.resp)

    def test_conditions(self):
        """generator of all combinations of (tf, tf_category) pairs from each test factor
        i.e., test_factor label included in all pairs
        len(result) == prod(len(v) for v in self.test_factors.values() )
        """
        return product(*(product([tf], tf_cats)
                         for (tf, tf_cats) in self.test_factors.items())
                       )

    def accept_test_cond(self, tcd):
        """Check if a given test-condition dict should be included for analysis.
            All test-factors in self.test_factors must be defined in tcd,
            but the tcd may include additional (test_factor, tf_category) pairs.
        :param tcd: dict with elements (test_factor, tf_category), where
            test_factor is a string, tf_category is a string or tuple
        :return: boolean, True iff tcd is OK.
            NOTE: this means self.matching_test_cond_tuple(tcd) will give a result
            that is guaranteed to be in self.test_conditions()
        """
        return all(tf in tcd and tcd[tf] in tf_cats
                   for (tf, tf_cats) in self.test_factors.items())

    def matching_test_cond_tuple(self, tcd):
        """Create a test_cond_tuple from a given test-condition dict,
        that matches a required test-condition dict defined in a PairedCompFrame object
        :param tcd: dict with elements (test_factor, tf_cat), where
            test_factor is a string, tf_cat is a string or tuple
        :return: tct = tuple of tuples (tf, tf_cat), where
            tf_cat is the tf_cat from tcd that matched tf.
            Thus, tct is guaranteed to be in self.test_cond_tuples
            len(tct) == len(self.test_factors) = number of required test factors
        """
        return tuple((tf, tf_cats[tf_cats.index(tcd[tf])])
                     for (tf, tf_cats) in self.test_factors.items())

    def set_stim_count(self, sc):
        """Set stim count from given dict
        :param sc: dict with elements (stim, count)
        :return: None
        Result: modified property self.stim_count
        """
        self.stim_count = [sc[s] for s in self.stim]

    def extend_stim_resp(self, sr_count):
        """Update self.stim and self.resp with
        stim and response labels found in file input data.
        :param sr_count: dict with elements (stim, r_dict)
        :return: None
        """
        for (s, r_dict) in sr_count.items():
            if s not in self.stim:
                self.stim.append(s)
            for r in r_dict.keys():
                if r not in self.resp:
                    self.resp.append(r)

    @classmethod
    def load(cls, p):
        """Try to create instance from file saved earlier
        :param p: string file-path or Path instance, identifying a pre-saved json file
        :return: one new PairedCompFrame instance, if successful
        """
        try:
            with open(p, 'rt') as f:
                d = json.load(f)
            return cls(**d['ConfMatrixFrame'])
        except KeyError:
            raise FileFormatError(p + 'is not a saved ConfMatrixFrame object')

    def save(self, f_name='cmf.json', dir='.'):
        """dump self to a json serialized file dir / f_name
        """
        dir = Path(dir)
        dir.mkdir(parents=True, exist_ok=True)
        p = (dir / f_name).with_suffix('.json')
        with p.open('wt') as f:
            json.dump({'ConfMatrixFrame': self.__dict__}, f,
                      indent=1, ensure_ascii=False)

    def check_complete(self):
        """Ensure all properties have complete and matching results.
        """
        if len(self.stim_count) != len(self.stim):
            raise RuntimeError('Property stim_count length must match stim category list')
        if self.correct_resp is None:
            self.correct_resp = {s: s for s in self.stim}
        if len(self.correct_resp) != len(self.stim):
            raise RuntimeError('Property correct_resp length must match stim category list')
        if not all(s in self.stim for s in self.correct_resp.keys()):
            raise RuntimeError('Property correct_resp must identify one response for each stim category')


# ----------------------------------------------------------
class StimRespCountSet:
    """Container for all observed confusion-count data
    from one experiment, i.e., for ALL listeners
    in ALL Main Test Conditions at ALL Difficulty Levels.
    """
    def __init__(self, cmf, cmd):
        """
        :param cmf: reference to a single ConfMatrixFrame instance for all listeners
        :param cmd: nested dict with individual stim-response dicts, stored as
            cm = cmd[group][subject][test_cond]
            = ONE stim-response dict with elements (stim, r_dict), where
            r_dict is a dict with elements (resp, count)
            cm.shape == (len(cmf.stim), len(cmf.resp)), same for all matrices
        """
        self.cmf = cmf
        self.cmd = cmd

    def __repr__(self):
        return 'StimRespCountSet(cmf=cmf, cmd=cmd)'

    def __str__(self):
        n_g = len(self.cmd)
        return ('StimRespCountSet with ' + f'{n_g} '
                + ('groups' if n_g > 1 else 'group')
                + ' including ' + ('\n\t' if n_g > 1 else '')
                + '\n\t'.join([f'{len(g_subjects)} subjects'
                             + (f' in group {repr(g)}' if n_g > 1 else '')
                             for (g, g_subjects) in self.cmd.items()
                             ])
                + '\n')

    @classmethod
    def load(cls, cmf, dir, fmt='json', groups=None, **kwargs):
        """Read all data files and store results
        :param cmf: single ConfDataFrame
        :param dir: string or Path identifying directory containing all input files
        :param fmt: (optional) string = suffix of file names to be tried for input
        :param groups: (optional) list of group-name strings,
            identifying file directories for separate listener groups
        :param kwargs: (optional) any additional parameters for file-reading function
        :return: single cls instance
        """
        def gen_records(g):
            for f_path in _gen_file_paths(dir, g):   # *****, fmt)):
                try:
                    for rec in file_reader(f_path,
                                           test_factors=cmf.test_factors,
                                           **kwargs):
                        yield StimRespRecord(**rec)
                except FileReadError as e:
                    logger.warning(f'{e}')
        # --------------------------------------------------------

        # assert (fmt in FILE_RECORDS_FCN or
        #         fmt in ['', None]), 'Unknown input file format: ' + fmt
        file_reader = _get_file_reader(fmt)
        dir = Path(dir)
        assert dir.exists(), f'{dir} does not exist'
        assert dir.is_dir(), f'{dir} is not a directory'
        if groups is None or len(groups) == 0:
            groups = ['']  # must have at least one empty group name
        cmd = dict()
        for g in groups:
            cmd[g] = dict()
            for cc_rec in gen_records(g):
                if cc_rec.subject not in cmd[g]:
                    cmd[g][cc_rec.subject] = dict()
                    # new empty subject
                if cmf.accept_test_cond(cc_rec.test_cond):
                    tct = cmf.matching_test_cond_tuple(cc_rec.test_cond)
                    if tct not in cmd[g][cc_rec.subject]:
                        cmd[g][cc_rec.subject][tct] = dict()
                    cmf.extend_stim_resp(cc_rec.stim_resp_count)
                    _accum_stim_resp_dict(cmd[g][cc_rec.subject][tct],
                                          cc_rec.stim_resp_count)
            logger.info(f'Collected group {repr(g)} with {len(cmd[g])} subjects')
        c = _count_stim(cmd)
        stim_count = Counter({s:0 for s in cmf.stim})
        for g_count in c.values():
            for subject_count in g_count.values():
                for tc_count in subject_count.values():
                    stim_count = stim_count + Counter(tc_count)
        cmf.set_stim_count(stim_count)
        return cls(cmf, cmd)

    def save(self, dir):
        """
        Save all data to one directory, one file for each subject
        :param dir: string or path to directory for saving
        :return: None
        2018-09-09, NOT TESTED
        """
        for (g, g_subjects) in self.cmd:
            if len(self.cmd) > 1 and len(g) > 0:
                group_dir = dir / g
            else:
                group_dir = dir
            for (s, s_dict) in g_subjects:
                records = [StimRespRecord(s, tc, sr)
                           for (tc, sr) in s_dict.items()]
                cm_data_json.StimRespFile(records).save(s, dir=group_dir)

    def check_complete(self):
        """Check that most subjects have complete data
        for most test conditions.
        Ensure all ConfMatrixFrame properties are consistent.
        """
        tfc_tuples = [tc for tc in self.cmf.test_conditions()]
        n_tfc = self.cmf.n_test_conditions
        n_groups = len(self.cmd)
        for (g, g_subjects) in self.cmd.items():
            n_subjects = len(g_subjects)
            incomplete_subjects = Counter()
            for (s, s_data) in g_subjects.items():
                for tc in tfc_tuples:
                    if (tc not in s_data.keys()) or len(s_data[tc]) == 0:
                        logger.debug(f'Missing {tc} for subject {repr(s)} in {repr(g)}')
                        incomplete_subjects.update({s: 1})
            for (s, c) in incomplete_subjects.items():
                logger.warning(f'Missing {c} of {n_tfc} test conditions for {repr(s)}' +
                               (f'in group {repr(g)}' if n_groups > 1 else ''))
            if sum(c for c in incomplete_subjects.values()) > MISSING_LIMIT * n_tfc * n_subjects:
                logger.warning('*** Too much missing data. Results may be unreliable. ***')
        self.cmf.check_complete()
        return True


# ---------------------------------------------------------
class StimRespRecord:
    """Container of phoneme-identification responses
    from ONE listener, in ONE test condition, for all presented phonemes.
    This is the basic block of phoneme-identification data obtained from a data file,
    regardless of file format.
    """
    def __init__(self, subject, test_cond, stim_resp_count, **othr):
        """
        :param subject: string with listener code name
        :param test_cond: dict with (test_factor, test_factor_category) elements
        :param stim_resp_count: dict with elements (s, r_dict), where
            s = a string with one stimulus label
            r_dict = a dict with elements (response_label, count)
        :param othr: dict with other data, not used for analysis
        """
        self.subject = subject
        self.test_cond = dict(test_cond)
        self.stim_resp_count = stim_resp_count
        self.othr = othr

    def __repr__(self):
        return (f'StimRespRecord(\n\t' +
                ',\n\t'.join(f'{key}={repr(v)}'
                            for (key, v) in vars(self).items()) +
                '\n\t)')


# ----------------------------------------------- help functions

def _gen_file_paths(p, sub_dir=None, suffix=None):
    """generator of all file Paths in directory tree p,
    recursively, with desired name pattern
    :param p: Path instance defining top directory to be searched
    :param sub_dir: (optional) sub-directory name
    :param suffix: (optional) file suffix of desired files, without dot
    :return: iterator of Path objects, each defining one existing data file
    """
    p = Path(p)  # just in case
    if sub_dir is not None and len(sub_dir) > 0:
        p = p / sub_dir  # search only in sub_dir
    if suffix is None:
        glob_pattern = '*.*'  # read any file types
    elif suffix == 'ost':  # special private file format
        glob_pattern = '*.txt'
    else:
        glob_pattern = '*.' + suffix  # require suffix
    return (f for f in p.rglob(glob_pattern)
            if f.is_file() and f.stem[0] != '.')


def _get_file_reader(fmt):
    """Select class / function that can read data files
    stored iin the selected format.
    :param fmt: file format code
    :return: a callable object that can read files of selected format
    """
    try:
        return FILE_RECORDS_FCN[fmt]
    except KeyError:
        if fmt == 'ost':  # special private file format
            import cm_read_ost
            return cm_read_ost.StimRespFile
        else:
            raise FileReadError(f'File format {repr(fmt)} not implemented')


def _accum_stim_resp_dict(save_dict, add_dict):
    """
    Accumulate add_dict into cm_dict, for phonemes selected in ConfMatrixFrame
    :param save_dict: accumulator dict with elements (stim, r_dict)
    :param add_dict: new dict with (stim, r_dict) elements
    :return: None, save_dict updated with add_dict contents
    """
    # sel_dict = {s: {r: c
    #                 for (r, c) in r_dict.items() if r in cmf.resp}
    #             for (s, r_dict) in add_dict.items() if s in cmf.stim}
    # for (s, r_dict) in sel_dict.items():
    for (s, r_dict) in add_dict.items():
        if s not in save_dict:
            save_dict[s] = dict()
        for (r, c) in r_dict.items():
            if r in save_dict[s]:
                save_dict[s][r] += c
            else:
                save_dict[s][r] = c


def _count_stim(cmd):
    """Count number of presented stim sounds
    for all groups, subjects, test conditions, and stim categories
    :param cmd: nested dict cmd[group][subject][tc][stim] = dict with (r, count) elements
    :return: count = nested dict with same structure
    """
    count = {g: {s: {tc: {st: sum(r_dict.values())
                          for (st, r_dict) in sr_dict.items()}
                     for (tc, sr_dict) in s_result.items()}
                 for (s, s_result) in g_subjects.items()}
             for (g, g_subjects) in cmd.items()}
    return count
