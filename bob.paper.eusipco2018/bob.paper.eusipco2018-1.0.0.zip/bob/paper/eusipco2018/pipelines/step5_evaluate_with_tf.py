# Config script to extract Audio features for SAVI audio

# run like this:
#

import os

from bob.pad.voice.algorithm import TensorflowEval
from bob.pad.base.tools.command_line import is_idiap

if is_idiap():
    temp_dir = '/idiap/temp/{}/{}'.format(os.environ['USER'], db_name)
else:
    temp_dir = 'temp/'

projector_file = 'model.ckp'

normalization_file = os.path.join(temp_dir, sub_directory, 'train_{{ tfwinsize }}-' + db_name + '.tfrecords.meanstd.npz')

sub_directory = 'tf_' + db_name + '_' + mfccenergy + '_blk' + pcablocksize + '_pca{{ pcafeaturesize }}_win{{ tfwinsize }}_{{ tfarchitecure[0] }}_{{ tfarchitecure[1] }}'

print (normalization_file)
algorithm = TensorflowEval(architecture_name="{{ tfarchitecure[0] }}",
                           input_shape=[{{ tfwinsize }}, {{ pcafeaturesize }}],  # [temporal_length, feature_size]
                           network_size={{ tfarchitecure[1] }},  # the output size of LSTM cell
                           normalization_file=normalization_file,  # file with normalization parameters from train set
                           )

skip_preprocessing = True
skip_extraction = True
skip_extractor_training = True
skip_projector_training = True
skip_projection = False
skip_score_computation = False
