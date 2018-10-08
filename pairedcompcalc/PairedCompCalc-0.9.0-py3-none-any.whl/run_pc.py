"""Run Bayesian analysis of data from a paired-comparison experiment.
This script should be used as a template,
to be copied and modified for any particular experiment.

*** Usage, see also explicit template example below

*1: Create a PairedCompFrame instance to define experiment and select input data.

*2: Load a set of data files

*3: Learn Bayesian models for all data files
using either Thurstone Case V or Bradley-Terry-Luce probabilistic choice model:

*4: Display results and save figures and text results to a directory tree
"""

# *** allow interactive user input ???

from pathlib import Path
import pickle
import logging

from PairedCompCalc import pc_logging
from PairedCompCalc.pc_data import PairedCompFrame, PairedCompDataSet
from PairedCompCalc.pc_model import PairedCompResultSet, Thurstone, Bradley

import PairedCompCalc.pc_display as shw

# -----------------------------------
# model_class = Bradley
model_class = Thurstone
# = class of probabilistic choice model

# ---------------------- location of input data:
data_dir = './pc_data'
# = directory with read-only input data files

# ---------------------- location for results:
result_dir = './pc_result'
# = top directory for all result files,
# with sub-directories created as needed.
# NOTE: Existing result files in this directory are OVER-WRITTEN WITHOUT WARNING!!!

assert result_dir != data_dir, 'Result directory must be different from input data directory'

model_result_file = 'pc_result.pkl'
# = name of saved PairedCompResultSet instance

display_file = 'pc_displays.pkl'
# = name of file with saved PairedCompDisplaySet instance

log_file = 'run_pc.log'
# = name of log file

result_path = Path(result_dir)
result_path.mkdir(parents=True, exist_ok=True)

pc_logging.setup(result_path, log_file)
# ---------------------- define experimental structure:

pcf = PairedCompFrame(attributes=['Speech Clarity', 'Pleasantness', 'Preference'],
                      # systems=['System0', 'System1', 'System2'], # may be taken from input data
                      systems_alias=['A', 'B', 'C', 'D'],  # to hide real system names in displays
                      forced_choice=True,
                      test_factors={'model': ['Bradley', 'Thurstone']})

# ---------------------- main work:


logging.info(f'Analysing paired-comparison data in {data_dir}')

ds = PairedCompDataSet.load(pcf, data_dir, groups=['A', 'B'], fmt='json')

# OR, using xlsx files, for example,
# ds = PairedCompDataSet.load(pcf, data_dir, groups=['A', 'B'], fmt='xlsx',
#                             sheets=[f'Subject{i}' for i in range(10)],
#                             subject = 'sheet',
#                             top_row = 2,
#                             attribute = 'A',  # column address
#                             pair = ('B', 'C'),
#                             difference = 'D',
#                             choice = 'E',
#                             Sound = 'G'
#                             )
# *** See pc_file_xlsx for more details about the xlsx file format

logging.info(f'Learning Results with model {model_class}')

pc_result = PairedCompResultSet.learn(ds, rv_class=model_class)

# ------------------------------- save learned result set:

# ****************** increment file name to avoid over-writing ??
with (result_path / model_result_file).open('wb') as f:
    pickle.dump(pc_result, f)

# ------------------------------- generate result displays:
# shw.PERCENTILES = [5., 50., 95.]   # default
# shw.PERCENTILES = [2.5, 50., 97.5]   # or other, as desired
# shw.CREDIBILITY_LIMIT = 0.8   # default = 0.6

pc_display = shw.display(pc_result)
# default display combination, showing estimated results for
# (1) random individual in the population from which participants were recruited,
# (2) the population mean.
# OR
# pc_display = shw.display(pc_result,
#                          percentiles=[2.5, 50., 97.5],
#                          credibility_limit=0.8,
#                          show_intervals=False,
#                          table_format='tab')
# *** See pc_display.FMT and pc_display_format.FMT for available format parameters

# ------------------------------------------------------------------------------
# Alternatives: display other specific combinations of predictive distributions:

# logging.info('Displaying predictive_group_individual and predictive_population_individual')
# pc_display = shw.PairedCompDisplaySet.display(pc_result.predictive_group_individual(),
#                                               pc_result.predictive_population_individual())

# OR
# logging.info('Displaying predictive_group_individual and predictive_population_mean')
# pc_display = shw.PairedCompDisplaySet.display(pc_result.predictive_group_individual(),
#                                               pc_result.predictive_population_mean())
# OR
# logging.info('Displaying only predictive_group_individual')
# pc_display = shw.PairedCompDisplaySet.display(pc_result.predictive_group_individual())

# OR other single predictive distribution or pair of predictive distributions

# ***** Edit display plots or tables here, if needed *****
# Each display element can be accessed and modified by the user, before saving,

# plt.show()
# to show all figures on screen before saving,
# This blocks the program until figure windows are closed by user

# ------------------------------- save result displays:
pc_display.save(result_path)

# if display_file is not None:
#     with (result_path / display_file).open('wb') as f:
#         pickle.dump(pc_display, f)
# *** can be loaded again, modified, and re-saved

logging.info(f'All results saved in {result_path} and sub-dirs.')
logging.shutdown()
