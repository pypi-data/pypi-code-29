"""Package ConfMatrixCalc implements probabilistic Bayesian analysis
of phoneme identification test results recorded in the form of confusion matrices.
The analysis method was presented and validated in (Leijon et al., 2016).

This package estimates the *overall performance* by two measures:

1. Probability of Correct identification (PC), averaged across all presented phonemes.

2. The Mutual Information (MI) between stimulus and response,
    sometimes called "transmitted information".
    This measure was first applied to phoneme identification data by Miller and Nicely (1955).
    It indicates the average amount of information about the stimulus category,
    obtained by the listener for each presented phoneme.

The package also identifies credible confusion patterns as a set of
stimulus-response pairs where listeners' response probabilities are
jointly credibly different between test conditions.

*** Usage

Copy the template script `run_cm.py` to your working directory, rename it, and
edit the copy as suggested in the template, to specify
    - your experimental layout,
    - the top input data directory,
    - a directory where all output result files will be stored.

See module cm_data for information about input files and data format.
Analysis results are saved as figures and tables in the designated result directory.
After running an analysis, the logging output briefly explains
the analysis results presented in figures and tables.

*** References

A. Leijon, G. E. Henter, and M. Dahlquist (2016).
Bayesian analysis of phoneme confusion matrices.
IEEE Trans Audio, Speech, and Language Proc 24(3):469–482.
doi: 10.1109/TASLP.2015.2512039.

G. A. Miller and P. E. Nicely (1955).
An analysis of perceptual confusions among some English consonants.
J Acoust Soc Amer 27(2):338–352, 1955.
doi: 10.1121/1.1907526.

H. Fletcher and J. Steinberg (1929). Articulation testing methods.
Bell System Technical Journal 8:806–854.
doi: 10.1002/j.1538-7305.1929.tb01246.x.

This Python package is a re-implementation and generalization of a similar MatLab package,
developed by Arne Leijon for ORCA Europe, Widex A/S, Stockholm, Sweden.
The MatLab development was financially supported by *Widex A/S, Denmark*.

*** Version History

2018-09-15, first functional version
"""

__name__ = 'ConfMatrixCalc'
__version__ = '0.6.0'
__all__ = ['__version__', 'run_cm']


