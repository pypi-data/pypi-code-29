"""
Template for the generic config file for SAVI. It should be used in combinaiton with other config files. [default: 0]

"""

import os
# import sys

from bob.pad.base.tools.command_line import is_idiap
import bob.io.base

if is_idiap():
    temp_dir = '/idiap/temp/{}/{}'.format(os.environ['USER'], db_name)
else:
    temp_dir = 'temp/{}/..'.format(db_name)

data_extension = '.hdf5'

groups = ['{{ tfgroups }}']
protocol = 'oneset'

TF_DB_FILE = os.path.join(temp_dir, sub_directory, '{{ tfgroups }}_{{ tfwinsize }}-' + db_name + '.tfrecords')
DATA_DIR = os.path.join(temp_dir, db_name)
if not os.path.exists(DATA_DIR):
    bob.io.base.create_directories_safe(DATA_DIR)

DATA_DIR = os.path.join(DATA_DIR, extracted_directory)

#   window-size INT    The number of features in the output sample [default: 32].
window_size = {{ tfwinsize }}
#   sliding-step INT        The shifting step for the sliding window. By default, windows do not overlap.
sliding_step = {{ tfslidestep }}
#   file-mean-std STR       The file with mean and std normalization parameters.
# for train subset, it should not exist yet, so it will be created
# for dev subset, the file should already exist, so it will be loaded and used
mean_std_filename = os.path.join(temp_dir, sub_directory, 'train_{{ tfwinsize }}-' + db_name + '.tfrecords.meanstd')
#   a, --sampling-attacks FLOAT  The portion of data that will be randomly sampled from attack
attacks_sampling = {{ tfattacksportion }}

verbose = 1
override_existing_record = False

