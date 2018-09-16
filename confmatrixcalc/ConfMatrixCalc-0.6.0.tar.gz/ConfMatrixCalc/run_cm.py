"""Template script to run analysis of phoneme-identification test results.
Copy this script and edit as guided by comments below.
"""

# -----------------------------------------------------------------------------------
from pathlib import Path
import logging

from ConfMatrixCalc import cm_logging

from ConfMatrixCalc.cm_data import ConfMatrixFrame, StimRespCountSet
from ConfMatrixCalc.cm_model import ConfMatrixResultSet
from ConfMatrixCalc.cm_display import ConfMatrixDisplaySet

logger = logging.getLogger(__name__)
# -----------------------------------------------------------------------------------

# --------- Define data and result directories relative to current working directory:

work_dir = Path.cwd()
data_dir = work_dir / 'MyPhonemeData'
# = top directory containing all input data files

result_dir = work_dir / 'MyPhonemeResults'
# = top directory for all result files, with sub-directories created as needed.

result_dir.mkdir(parents=True, exist_ok=False)
# NOTE: exist_ok=True means that any existing files are OVER-WRITTEN WITHOUT WARNING!!!

cm_logging.setup(log_file='run_cm_log.txt', result_path=result_dir)

# --------- Define test conditions:

cons_labels = ['p', 'b', 't', 'd', 'k', 'g', 'm', 'n', 'ng', 'f', 'v', 's', 'sh', 'r', 'h', 'l']
# Optional list of stimulus consonant labels as used in data files.
# Needed only if a pre-defined sorting is desired.
# If not specified, the stimulus labels will be sorted in the order they are found in data files.

response_labels = cons_labels.copy()
response_labels.append('No Response')
# Optional list of response labels

# correct_response={s:s for s in cons_labels}
# Optional, needed only if correct-response labels are different from stimulus labels.

cmf = ConfMatrixFrame(# stim=cons_labels, # Optional
                      # resp=response_labels,  # Optional
                      # correct_response={s:s for s in cons_labels},  # Optional
                      test_factors={'HA':['A', 'B', 'Unaided'],
                                    'SNR': ['Quiet', 'High', 'Low', ]}
                      )
# *** NOTE: Data for the required test_factors 'HA' and 'SNR'
# must be represented in the data files.
# The test-factor category must agree with one of the required categories,
# for a test result to be included in the analysis.
# If input files include data for additional test factors,
# those test results are also included in the analysis,
# and handled as replications for the required test factors.


# -------- Load a complete set of identification test results:

# *** Example using Excel (xlsx) workbook files:

cc_set = StimRespCountSet.load(cmf, dir=data_dir, fmt='xlsx',
                               groups=['Young', 'Old'],
                               # sheets=[f'Sheet{i}' for i in range(3, 20)],  # optional
                               subject='A1',        # cell address for the subject ID,
                               stim_range='C4:C20', # a column with stimulus labels
                               resp_range='D3:U3',  # a row with response labels,
                               count_range='D4:U20', # cell range with response counts for each stim
                               HA='A2'  # cell defining HA category
                               )

# *** NOTE: If separate groups are defined, each group label must be
# a sub-directory under the top input directory 'data_dir'.
# If no sheets list is given, all workbook sheets will be searched for data.

# In the example, no cell address is defined for the 'SNR' test factor:
# The category must then be found as a matching sub-string in the file path string,
# e.g., as a directory name, assuming data files for different SNRs are saved
# in separate directories.

# *** Another example using input data saved in json file format:

# cc_set = StimRespCountSet.load(cmf, dir=data_dir, fmt='json',
#                                groups=['Mild', 'Moderate', 'Severe'],
#                                )

# -------- If needed, cmf properties can be updated manually here:

# cmf.stim_count = a list of counts for each stim.
# in case the test presentation counts do NOT reflect the real probability distribution of stimuli.
# cmf.correct_resp = ...,
# in case correct response labels are NOT all identical to the stimulus category label.


# -------- Learn a probabilistic model, adapted to all input data:

cm_result = ConfMatrixResultSet.learn(cc_set)

# -------- Save learned result set (optional):
# with (result_dir / 'cm_result.pkl').open('wb') as f:
#     pickle.dump(cm_result, f)


# -------- Display figures and tables showing all analysis results:

cm_display = ConfMatrixDisplaySet.display(cm_result,
                                          # percentiles=[2.5, 50., 95.],  # (optional) other than default
                                          table_format='latex',
                                          figure_format='eps')
# Keyword parameters are used to control display details.
# For possible alternatives, see cm_display.FMT and cm_display_format.FMT

# -------- Edit display plots or tables here, if needed:

# Each display element can be accessed and modified by the user, before saving.
# See cm_display.ConfMatrixDisplaySet for a description of the data structure.

cm_display.save(result_dir)
# Saved all display elements to 'result_dir' and sub-directories.

logging.shutdown()
