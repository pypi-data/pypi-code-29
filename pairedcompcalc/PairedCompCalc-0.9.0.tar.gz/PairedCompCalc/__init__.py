"""This package implements Bayesian probabilistic models
for the analysis of Paired-Comparison data,
for example, for the Sound Quality of different hearing aid processing systems.

A probabilistic model is adapted to the observed data for each participant,
assuming that the responses were determined by a perceptual choice model,
either the Thurstone-Case-V model (Thurstone, 1927)
or the BTL model (Bradley and Terry, 1952).

As a result, the model can also present a predictive probability distribution for
A: a random individual in the population from which participants were recruited,
B: the mean quality parameters in that population.

Mathematical model details and learning methods are presented in (Leijon et al., 2018).

NOTE: All model parameters are estimated using sampling.
Therefore, the numerical results may deviate slightly between runs,
even if exactly the same input data are used.
It is recommended to run the analysis twice to see these variations.

*** Main Script Template:

run_pc: Bayesian analysis of paired-comparison data,
    using either the Thurstone-case-V or the BTL model.

*** Other Useful Script Templates:

run_sim: Generate simulated paired-comparison data files,
    to be used for preliminary testing of the analysis.

run_power: Calculate approximate power of a planned future experiment,
    indicating the required number of test participants
    to reach a desired reliability of the test results.

*** Usage: Copy and rename a template script,
    and edit the script as needed for your experiment,
    with guidance from comments in the script.

    The organisation and available formats of input data files
    are described in the doc-comment of module pc_data.py

*** Main Package Modules:

pc_data: classes and load/save functions for raw input data
pc_model: classes and functions for Bayesian probabilistic model definition and learning
pc_display: classes and functions producing figures and tables from analysis results
format_display: classes and functions for figure and table formatting

All modules are distributed as python source files.
Users can rather easily modify input and output modules if needed.
However, for the central mathematical module pc_model,
it is recommended to discuss any changes with the package author.

*** Main Classes:

pc_data.PairedCompFrame: defines layout of a paired-comparison experiment
pc_data.PairedCompRecord: container for raw paired-comparison data for one test subject,
    corresponding to one input data file.
pc_data.PairedCompDataSet: container for all input data to be analysed

pc_display.PairedCompDisplaySet: container for all user-readable analysis results

pc_model.PairedCompResultSet: container for posterior Bayesian models learned from
    all observed subject data in one PairedCompDataSet instance.
pc_model.PredictiveResultSet: predictive probabilistic models,
    for a random individual in the participant group,
    or for the population, from which test participants were recruited,
    derived from the PairedCompResultSet instance.
pc_model.Thurstone: choice model according to Thurstone Case V
pc_model.Bradley: Bradley-Terry-Luce (BTL) choice model
pc_model.PairedCompIndModel: central model for the multivariate distribution
    of all quality parameters of ONE participant for ONE perceptual attribute,
    represented by Hamiltonian sampling of the posterior distribution of model parameters.

*** References:

A. Leijon, M. Dahlquist, and K. Smeds (2018).
Bayesian analysis of paired-comparison sound quality ratings.
*Manuscript in preparation*. Contact the author for info.

K. Smeds, F. Wolters, J. Larsson, P. Herrlin, and M. Dahlquist (2018).
Ecological momentary assessments for evaluation of hearing-aid preference.
*J Acoust Soc Amer* 143(3):1742–1742.

M. Dahlquist and A. Leijon (2003).
Paired-comparison rating of sound quality using MAP parameter estimation for data analysis.
In *1st ISCA Tutorial and Research Workshop on Auditory Quality of Systems*,
Mont-Cenis, Germany.

L. L. Thurstone (1927). A law of comparative judgment.
*Psychological Review* 34(4), 273–286, doi: 10.1037/h0070288.

R. A. Bradley and M. E. Terry (1952).
Rank analysis of incomplete block designs. I. The method of paired comparisons.
*Biometrika* 39, 324–345, doi: 10.2307/2334029.

NOTE: This python package includes some extensions relative to the similar MatLab package:

* Allows the use of either Thurstone Case V or BTL response models.
* Can use input data saved in either the old 2002 res format or in json format.
* Allows missing subject data for some perceptual attributes.
* Allows missing subject data for some test-conditions in some subjects.
* Parameters for missing individual data are automatically adapted to the population model.
* Test-condition labels may be single strings or tuples of strings.
* All result displays are stored as a class instance, which is saved in a structured directory tree.
* The internal prior distribution for model parameters is hierarchical, more advanced.


*** Version history:

** New in version 0.9.0, 2018-10-08:

Allow xlsx input, new basic file-item structure,
    common for all file formats.
Result displays show response-interval limits,
    if display parameter show_intervals=True.
Several minor fixes in display formatting.
Changed convention for display file names.



** Version 0.8.3:
2018-02-18, First functional version
2018-03-28, Modified internal structure of pc_model.PairedCompResultSet
2018-04-03, Use all available subject data for quality estimates, even if some data are missing,
    except that attribute correlations are calculated only within each subject,
    i.e., using only subjects with complete results for all attributes.
2018-04-27, first hierarchical analysis model tested
    Use PairedCompFrame.systems_alias labels for all displays.
2018-05-21, allow choice among three types of predictive distributions
2018-08-05, using prior gauss_gamma module for population distribution, tested pc_power
2018-08-14, simplified internal structure of PairedCompDataSet
2018-08-15, First public version 0.8.3
"""

__name__ = 'PairedCompCalc'
__version__ = '0.9.0'
__all__ = ['__version__', 'run_pc', 'run_power', 'run_sim']
