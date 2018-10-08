"""This module defines classes to hold paired-comparison experimental data,
and methods and functions to read and write such data.
Data may be stored in several file formats.

*** Class Overview:

PairedCompFrame: defines layout of a paired-comparison experiment.

pc_base.PairedCompItem: basic input file data block, specifying
    ONE response to ONE pair of test stimuli,
    by ONE subject, judging ONE perceptual attribute,
    in ONE test condition, defined by one category label for each Test Factor.

PairedCompFile: interface to input data file in an allowed format,
    and iterator yielding PairedCompItem instances.

StimRespItem: container for a single stimulus, response, test-condition

PairedCompDataSet: all data for selected group(s), subjects, attributes, and test conditions,
    to be used as input for statistical analysis.
    Each subject must be tested in ALL test conditions,
    but not necessarily for all perceptual attributes.

*** Input File Formats:

* json: The simplest file structure is pc_file_json.PairedCompFile.
This is a serialized sequence of PairedCompItem objects.
Files in this format must be saved with extension '.json'.

* xlsx: Data can also be imported from Excel workbook (xlsx) files,
with data stored in one or more worksheets,
in a quite flexible format.
Files in this format must be saved with extension '.json'.

Data elements are stored in specified locations,
as defined by keyword parameters to the pc_file_xlsx.PairedCompFile object.
See module pc_file_xlsx for details.

* res: For backward compatibility,
input data files may also be stored in an older text format,
used by Dahlquist and Leijon (2003).
Files in this format are saved with extension '.res'.
See module pc_file_res for details.


*** Input Data Files:

All input files from an experiment must be stored in one directory tree.

If results are to be analyzed for more than one group of test subjects,
the data for each group must be stored in separate sub-directory trees
on the first level just below the top directory.
All sub-directories in the tree are searched recursively for data files.

Each data file may contain paired-comparison results
for one or more test subjects judging one or more perceptual attributes,
in one or more test conditions.
File names are arbitrary, although they may be somehow associated with
the encoded name of the participant, to facilitate data organisation.

Files for different test conditions may be stored in separate sub-directories.
The directory name can then be used to indicate some test-factor categories,
if the test-factor is not defined within the data file itself.

Several files may include data for the same subject,
e.g., results obtained in different test conditions,
or simply for replicated test sessions with the same subject.

All input data are collected by a single function call, as
ds = PairedCompDataSet.load(pcf, dir, groups, fmt='xlsx',...)

If parameter fmt is specified,
the load method reads only files with suffix fmt
in the directory tree defined by the top-directory path-string in parameter dir.

If the fmt argument is left unspecified,
PairedCompDataSet.load will attempt to read ALL files in the designated directory tree,
assuming the format is indicated by the file suffix,
and use the files that seem to contain paired-comparison data.

The parameter groups is an optional list of sub-directory names,
one for each participant group.

The parameter pcf is a PairedCompFrame object that defines the experimental layout.
Some properties of this object can define selection criteria
for a subset of data to be included for analysis.

*** Example Directory Tree:

Assume we have data files in the following directory structure:
~/sessions / NH / Low,   containing files Subject0.json, ..., Subject20.json
~/sessions / NH / High,  containing files Subject0.json, ..., Subject20.json
~/sessions / HI / Low,  containing files test0.json, ..., test10.json
~/sessions / HI / High, containing files test0.json, ..., test10.json

Directories 'NH' and 'HI' may contain data for different groups of test participants,
e.g, individuals with normal hearing (NH) or with impaired hearing (HI).

Sub-directories named 'Low' and 'High' may include data files collected
in two different noise conditions, with 'Low' or 'High' signal-to-noise ratio,
in case the noise condition is not recorded by some field the file itself.

Data for the SAME subjects should then be found in BOTH sub-directories 'Low' and 'High'.
because each subject should be tested in all test conditions.

If tests have been done for different perceptual Attributes,
each subject should ideally be tested with all Attributes,
to allow the most accurate estimation of correlations between Attributes.

** Accessing Input Data för Analysis:

*1: Create a PairedCompFrame object defining the experimental layout, e.g., as:
pcf = PairedCompFrame(systems = ['testA', 'testB', 'testC'],  # three sound processors
        attributes = ['Preference'],  # only a single perceptual attribute in this case
        test_factors = {'Sound': ['speech', 'music'],  # test factor 'Sound' with two categories
                            'SNR': ['Low', 'High']}  #  test factor 'SNR' with two categories
        )
NOTE: attribute labels must be strings that can be used as directory names.
NOTE: Letter CASE is distinctive, i.e., 'Low' and 'low' are different categories.

*2: Load all test results into a PairedCompDataSet object:

ds = PairedCompDataSet.load(pcf, path='~/sessions', groups=['NH', 'HI'], fmt='json')

The loaded data structure ds can then be used as input for analysis.

If fmt='xlsx' is specified, the load method reads only files with the 'xlsx' extension
in the directory tree defined by the top-directory path-string in parameter dir.

If the fmt argument is left unspecified, or if fmt=None, or fmt='',
PairedCompDataSet.load will attempt to read ALL files in the designated directory tree,
and use the files that seem to contain paired-comparison data.

The parameter groups is an optional list of sub-directory names,
one for each participant group.

The parameter pcf is a PairedCompFrame object that defines the experimental layout.
Some properties of this object can define selection criteria
for a subset of data to be included for analysis.

With data files saved in the 'json' or 'xlsx' formats,
the test-factor categories may be defined in the file.
If so, the sub-directory names 'Low' and 'High' are not significant,
and need not agree with any test-condition labels in the PairedCompFrame object.

However, if a desired test factor is NOT defined in the file data,
the file-reading methods will attempt to find the test-factor category
as a sub-string of the full path string.

Files in the older 'res' format can NOT define test factors.
For these files all test factors must be deduced from the path-string.

Therefore, in this case the category labels defined for test-factors
MUST be UNIQUE in the file paths.
For example, test_factors = {'SNR': ['Low', 'High', 'Higher']}
can NOT be used if the categories are defined by the path string.
Test-condition labels can not be sub-strings of a group name,
because the group directory name is also included in the path-string.

*** Selecting Subsets of Data for Analysis:

It is possible to define a data set including only a subset of experimental data.
For example, assume we want to analyse only group 'HI':

ds_HI = PairedCompDataSet.load(pcf, groups=['HI'])

Or perhaps we want to look at results for only one test condition,
and only two of the three sound systems that have been tested.
Then we must define a new PairedCompFrame object before loading the data:

small_pcf = PairedCompFrame(systems = ['testA', 'testB'],  # only two of the sound processors
        attributes = ['Preference'],  # same single perceptual attribute
        test_factors = {'SNR': ['High']}  # test factor SNR, now with only ONE category
        )
ds_AB_HI_High = PairedCompDataSet.load(small_pcf, groups =  ['HI'])

This will include all data with 'SNR' 'High', regardless of the 'pair' category.

If there are data for other perceptual attributes in addition to 'Preference',
the analysis is restricted to the specified subset of attributes.

Any paired-comparisons for OTHER SYSTEMS, not explicitly named in small_pcf, will be DISREGARDED.
Any results for OTHER ATTRIBUTES, not explicitly specified in small_pcf, will be DISREGARDED.
Any results having a desired test-factor category will be INCLUDED,
regardless of the category within any other test factor.

*** Version History:

2018-03-30, changed nesting structure to PairedCompDataSet.pcd[group][attribute][subject]
    because we learn one separate PairedCompGroupModel for each group and attribute.
    Allow missing subjects for some attributes;
    identical subjects needed only for attribute correlations.
2018-04-12, Allow systems_alias labels in PairedCompFrame
2018-08-10, renamed classes PairedCompRecord and new class StimRespItem
2018-08-10, include test condition in each StimRespItem, to facilitate EMA data input
2018-08-12, simplified PairedCompRecord structure: no redundant data,
    all general experimental info given only in PairedCompFrame
2018-08-13, simplified PairedCompDataSet structure

Changes in version 0.9.0:
2018-09-21, changed property name PairedCompFrame.test_factors, and some method names
2018-09-24, generalized class structure, to allow flexible new file formats
2018-09-25, using new PairedCompFile class, containing PairedCompItem instances
2018-09-30, changed signature of PairedCompFile
"""
# ****** assert UNIQUE systems, attributes

# ****** save .res files like pc_file_2002 ???

import numpy as np
from pathlib import Path
from collections import OrderedDict, namedtuple
from itertools import product
import json
import logging

from . import pc_file_json
from . import pc_file_res
from . import pc_file_xlsx

from .pc_base import FileReadError


FILE_READER = {'json': pc_file_json.PairedCompFile,
               'xlsx': pc_file_xlsx.PairedCompFile,
               'res': pc_file_res.PairedCompFile}
# = mapping of file format suffix to file interface class

logger = logging.getLogger(__name__)


# ----------------------------------------------------------------------
StimRespItem = namedtuple('StimRespItem', 'S R T')
# S = a tuple of two strings identifying the test systems compared.
# R = an integer in  (-M, ..., 0, ..., +M), except that
#     R = 0 is allowed only in experiments with property forced_choice == False.
# T = a dict defining a Test Condition,
#     with zero or more elements (test_factor, tf_category),
#     where test_factor is a string label, and
#     tf_category is a string label identifying one category within test_factor.
# in python v 3.7: T may be omitted, using arg default=dict()


# ------------------------------------------------------------------
class PairedCompFrame:
    """Defines structure of one Paired-Comparison analysis calculation.
    Data about test participants are NOT included.
    """
    def __init__(self,
                 attributes,
                 response_labels,
                 forced_choice=False,
                 systems=None,
                 systems_alias=None,
                 test_factors=list()
                 ):
        """
        :param attributes: list of string labels for selected perceptual attributes
            Attribute labels must be strings that can be used as directory names.
        :param response_labels: (optional) list with ordinal difference-magnitude rating labels
            mainly informational, but the number of labels is needed for model learning
        :param forced_choice: (optional) boolean indicator that response NO Difference is not allowed.
        :param systems: (optional) list with unique string labels of systems being evaluated
            initialized from the first encountered data file, if not specified here
        :param systems_alias: (optional) sequence of systems labels used for displays
        :param test_factors: (optional) iterable with elements (test_factor, category_list),
            where
            test_factor is a string,
            category_list is a list of labels for allowed categories within test_factor.
            A category label is normally just a single string,
                but may be a tuple of strings, for use by pc_file_2002.
            May be left empty, if only one test condition is used.

        NOTE: systems, attributes, and test_factors may define a subset of
            data present in input data files.
        """
        if systems is not None:
            assert len(set(systems)) == len(systems), 'System labels must be unique'
        self.systems = systems
        self.systems_alias = systems_alias
        assert len(set(attributes)) == len(attributes), 'Attribute labels must be unique'
        self.attributes = attributes
        self.response_labels = response_labels
        self.forced_choice = forced_choice
        self.test_factors = OrderedDict(test_factors)

    def __repr__(self):
        return (f'PairedCompFrame(\n\t' +
                ',\n\t'.join(f'{key}={repr(v)}'
                             for (key, v) in vars(self).items()) +
                '\n\t)')

    @property
    def n_systems(self):
        return len(self.systems)

    @property
    def systems_disp(self):
        """Systems labels for display"""
        if self.systems_alias is None:
            return self.systems
        else:
            return self.systems_alias[:self.n_systems]

    @property
    def n_attributes(self):
        return len(self.attributes)

    @property
    def n_response_labels(self):
        """number of ranked magnitudes of perceived pair-difference,
        including the "equal" category if forced_choice == False,
        but not including negative differences
        """
        return len(self.response_labels)

    @property
    def n_test_factors(self):
        return len(self.test_factors)

    @property
    def n_test_factor_categories(self):
        """1D list with number of test-condition alternatives in each test factor"""
        return [len(v) for v in self.test_factors.values()]

    @property
    def n_test_conditions(self):
        return np.prod(self.n_test_factor_categories, dtype=int)

    def test_conditions(self):
        """generator of all combinations of (tf, tf_category) pairs from each test factor
        i.e., test_factor label included in all pairs
        len(result) == prod(len(v) for v in self.test_factors.values() )
        """
        return product(*(product([tf], tf_cats)
                         for (tf, tf_cats) in self.test_factors.items())
                       )

    def gen_test_factor_category_tuples(self):  # ***** == test_conditions (new)
        """generator of dicts, with one dict for
        every combination of one category from each test_factor,
        needed by pc_simulator
        """
        tc_pairs = ([(tf, tf_c) for tf_c in tf_cats]
                    for (tf, tf_cats) in self.test_factors.items())
        return product(*tc_pairs)

    @classmethod
    def load(cls, p):
        """Try to create instance from file saved earlier
        :param p: string file-path or Path instance, identifying a pre-saved json file
        :return: one new PairedCompFrame instance, if successful
        """
        try:
            with open(p, 'rt') as f:
                d = json.load(f)
            return cls(**d['PairedCompFrame'])
        except KeyError:
            raise FileReadError(p + 'is not a saved PairedCompFrame object')

    def save(self, dir, file_name='pcf.json'):
        """dump self to a json serialized file dir / file_name
        """
        dir = Path(dir)
        dir.mkdir(parents=True, exist_ok=True)
        p = (dir / file_name).with_suffix('.json')
        with p.open('wt') as f:
            json.dump({'PairedCompFrame': self.__dict__}, f,
                      indent=1, ensure_ascii=False)

    def accept(self, pc_item):
        """Check that pc_item properties agree with self properties,
        such that pc_item should be included in desired PairedCompDataSet instance.
        :param pc_item: one PairedCompItem instance
        :return: boolean True if pc_item is accepted
        """
        if self.systems is not None:
            if any(s not in self.systems for s in pc_item.pair):
                return False
        if self._response_outside_range(pc_item.response):
            w = (f'Response {pc_item.response} out of range ' +
                 f'for subject {repr(pc_item.subject)}, ' +
                 f'attribute {repr(pc_item.attribute)}')
            logger.warning(w)
            return False
        return pc_item.attribute in self.attributes

    def _response_outside_range(self, r):
        """Check if a response is unacceptable
        :param r: scalar integer response value
        :return: boolean True if r is NOT acceptable
        """
        if self.forced_choice:
            return r == 0 or abs(r) > self.n_response_labels
        else:
            return abs(r) >= self.n_response_labels


# ------------------------------------------------------------
class PairedCompDataSet:
    """All result data for one complete paired-comparison analysis.
    Includes two properties:
    pcf = a PairedCompFrame instance, defining the experimental layout,
    pcd = a nested dict containing result data for all participants.
    """
    def __init__(self, pcf, pcd):
        """
        :param pcf: a single PairedCompFrame instance,
        :param pcd: nested dict with elements (group_id: group_data), where
            group_id s a group-name string equal to a directory name, and
            group_data is a dict with elements {attribute: attr_results}, where
            attribute is one of the string labels specified in pcf,
            attr_results is a dict with elements (subject_id: res), where
            subject_id is a string, and
            res is a list of StimRespItem objects, one for each presentation

        Thus, a single result list may be extracted from the pcd by nested dict indexing, e.g.,
        result = self.pcd[group][attr][subject]
        2018-08-14, simplified pcd nested dict structure; test-cond now inside StimRespItem
        """
        self.pcf = pcf
        self.pcd = pcd

    def __repr__(self):
        return 'PairedCompDataSet(pcf=pcf, pcd=pcd)'

    def __str__(self):
        n_subjects = {g: {a: sum(len(r) > 0 for (s, r) in a_subjects.items())
                          for (a, a_subjects) in g_attr.items()}
                      for (g, g_attr) in self.pcd.items()}
        # = subjects with non-empty pc result lists
        n_g = len(self.pcd)
        return ('PairedCompDataSet with ' + f'{n_g} '
                + ('groups' if n_g > 1 else 'group')
                + ' with data from \n'
                + '\n'.join([f' {n_s} subjects for attribute {repr(a)}'
                             + (f' in group {repr(g)}' if n_g > 1 else '')
                             for (g, g_attributes) in n_subjects.items()
                             for (a, n_s) in g_attributes.items()
                             ])
                + '\n')

    @classmethod
    def load(cls, pcf, dir, groups=None, fmt=None, **file_args):
        """Create one class instance from selected session results.
        :param pcf: PairedCompFrame instance
        :param dir: string or Path defining top of directory tree with all data files
        :param groups: (optional) list of group names,
            each element MUST be name of one immediate sub-directory of dir
        :param fmt: (optional) string with file suffix for data files.
            If undefined, all files are tried, so mixed file formats can be used as input.
        :param file_args: dict with keyword arguments, as needed for selected file type.
        :return: a single cls object

        Arne Leijon, 2018-03-29, changed pcd nesting order
        2018-08-14, using simplified PairedCompRecord structure
        2018-09-23, using PairedCompFile iterator of PairedCompItem instances
        """
        def gen_pc_items(dir, group):
            """generator of items to be included.
            :param dir: Path to directory containing PairedCompFile-readable files.
            :param group: sub-directory name in dir, OR None
            :return: iterator of PairedCompItem instances,
                yielding only items accepted by pcf
            """
            for p in _gen_file_paths(dir, group, fmt):
                p_fmt = p.suffix.lstrip('.')
                try:
                    pc_file = FILE_READER[p_fmt](file_path=p, pcf=pcf,
                                                 **file_args)
                    for pc_item in pc_file:
                        tct = _matching_test_cond_tuple(pc_item.test_cond, pcf)  # *************
                        # tct = pcf.matching_test_cond_tuple(pc_item.test_cond)  # *************
                        if tct is not None and pcf.accept(pc_item):
                            pc_item.test_cond = tct
                            yield pc_item
                except (KeyError, FileReadError):
                    logger.warning(f'Can not read {p}')
                    # try next file

        # ----------------------------------------------------------
        assert (fmt in FILE_READER.keys() or
                fmt in ['', None]), 'Unknown session file format: ' + fmt
        dir = Path(dir)
        assert dir.exists(), f'{dir} does not exist'
        # assert dir.is_dir(), f'{dir} is not a directory'
        # ************** allow single file input ***************************
        if groups is None or len(groups) == 0:
            groups = ['']  # must be a list with at least one group label
        pcd = OrderedDict()
        # = space for all record results
        systems = set()
        # = accum systems labels, to be used in case pcf.systems undefined
        for g in groups:
            pcd[g] = {a: dict()
                      for a in pcf.attributes}
            for pc_item in gen_pc_items(dir, g):
                systems.update(pc_item.pair)
                srt = StimRespItem(pc_item.pair,
                                   pc_item.response,
                                   pc_item.test_cond)
                if pc_item.subject not in pcd[g][pc_item.attribute].keys():
                    pcd[g][pc_item.attribute][pc_item.subject] = [srt]
                    # first item for this subject
                else:
                    pcd[g][pc_item.attribute][pc_item.subject].append(srt)

        for (g, g_attributes) in pcd.items():
            for (a, a_subjects) in g_attributes.items():
                n_items = np.mean([len(s_res)
                                  for s_res in a_subjects.values()])
                log_str = (f'Collected group {repr(g)}, ' +
                           f'attribute {repr(a)}, ' +
                           f'with {len(a_subjects)} subjects, ' +
                           f'mean {n_items:.1f} items per subject')
                logger.info(log_str)
        if pcf.systems is None:
            pcf.systems = sorted(list(systems))
        return PairedCompDataSet(pcf, pcd)

    # def save(self, dir):  # ********** pickle ?
    #     """
    #     Save self.pcd in a directory tree with sub-trees for groups and attributes.
    #     :param dir: Path or string defining the top directory where files are saved
    #     :return: None
    #     """
    #     raise NotImplementedError

    def ensure_complete(self):
        """Check that every subject has data for at least SOME test_factors.
        NOTE: This condition is relaxed with current hierarchical population prior.
        Analysis results are calculated even if there are NO data for some test_factors.
        Quality estimates for missing data are influenced only by the population prior.
        Non-matching subject sets are allowed for different attributes.
        :return: None

        Result:
        self.pcd reduced: subjects with no results are deleted
        logger warnings for missing data.

        Arne Leijon, 2018-04-12
        2018-08-14, simplified test with simplified nested dict pcd
        """
        # *** check responses against pcf.response_labels and forced_choice, and log warning !

        for (g, g_attributes) in self.pcd.items():
            for (a, ga_subjects) in g_attributes.items():
                incomplete_subjects = set(s for (s, item_list) in ga_subjects.items()
                                          if len(item_list) == 0)
                for s in incomplete_subjects:
                    del self.pcd[g][a][s]
                    logger.warning(f'Subject {s} in group {repr(g)} excluded for attribute {repr(a)}; no data')
            # check if all attributes include the same subjects
            all_subjects = set.union(*(set(ss)
                                       for ss in g_attributes.values()))
            for (a, ga_subjects) in g_attributes.items():
                if len(ga_subjects) == 0:
                    raise RuntimeError(f'No subjects in group {repr(g)} for attribute {repr(a)}')
                missing_subjects = all_subjects - set(ga_subjects)
                if len(missing_subjects) > 0:
                    logger.warning(f'{missing_subjects} missing for attribute {repr(a)} in group {repr(g)}')
                # ***** delete all missing subjects ???
                # ***** NO, we need matching subjects only for attribute correlations


def _gen_file_paths(p, sub_dir=None, suffix=None):
    """generator of all file Paths in directory tree p, recursively, with desired name pattern
    :param p: Path instance defining top directory to be searched
    :param sub_dir: (optional) sub-directory name
    :param suffix: (optional) file suffix of desired files
    :return: iterator of Path objects, each defining one existing data file

    Arne Leijon, 2018-09-30
    """
    if p.is_file():
        return [p]  # allow a single file
    if sub_dir is not None and len(sub_dir) > 0:
        p = p / sub_dir  # search only in sub_dir
    if suffix is not None and len(suffix) > 0 and p.with_suffix('.'+suffix).is_file():
        return [p]  # allow a single file for this group
    if suffix is None or suffix == '':
        glob_pattern = '*.*'  # read any file types
    else:
        glob_pattern = '*.' + suffix  # require suffix
    return (f for f in p.rglob(glob_pattern)
            if f.is_file() and f.name[0] != '.')


def _matching_test_cond_tuple(tcd, pcf):
    """Create a test_cond_tuple from a given test-condition dict from a PairedCompItem,
    that matches a required test-condition dict defined in a PairedCompFrame object
    :param tcd: dict with elements (test_factor, tf_cat), where
        test_factor is a string, tf_cat is a string or tuple
    :param pcf: a PairedCompFrame object, with
        pcf.test_factors = an OrderedDict with elements (test_factor, list of tf_cat items)
    :return: tct = tuple ((tf0, tf_cat_0), (tf1, tf_cat_1), ...),
        where tf_n is n-th test_factor, and
        tf_cat_n is the tf_cat from tcd matching one of the n-th test_factor categories
        len(tct) == len(pcf.test_factors)
        All test-factors required in pcf must be defined in tcd,
        but the tcd may include additional (test_factor, category) pairs.
        tct = None if not all required test-factors were found.
    NOTE: this implies that tct is guaranteed to be one element of pcf.test_cond_tuples()
    """
    try:
        tct = [(tf, tf_cats[tf_cats.index(tcd[tf])])
               for (tf, tf_cats) in pcf.test_factors.items()]
        # tcd[tf] raises KeyError if tf is not present in tcd
        # tf_cats.index(...) raises ValueError if tcd[tf] does not match
        return tuple(tct)
    except (KeyError, ValueError):
        return None
