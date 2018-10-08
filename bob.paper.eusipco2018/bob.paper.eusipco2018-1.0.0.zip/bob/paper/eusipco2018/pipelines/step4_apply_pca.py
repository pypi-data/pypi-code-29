"""
Template for the config script to train PCA on the features from the training set to reduce their dimensionality.
Steps 1 to 2 should be run first.
"""

from bob.project.savi.extractor import CepstralMouthDeltas
from bob.project.savi.extractor import PCAReduction

mfccenergy = '{{ mfccenergy }}'
pcablocksize = '{{ pcablocksize }}'

preprocessed_directory = '../extracted_openpose_mouthdeltas42_{{ mfccenergy }}_blk{{ pcablocksize }}'
preprocessor = CepstralMouthDeltas()

extracted_directory = '../extracted_openpose_mouthdeltas42_{{ mfccenergy }}_blk{{ pcablocksize }}_pca{{ pcafeaturesize }}'

extractor = PCAReduction(resulted_features_size={{ pcafeaturesize }}, per_modality_pca=False)
extractor_file = 'Extractor_' + db_name + '.hdf5'

sub_directory = 'openpose_mouthdeltas42_{{ mfccenergy }}_blk{{ pcablocksize }}_pca{{ pcafeaturesize }}'
algorithm = "test"

skip_extraction = False
skip_extractor_training = False

