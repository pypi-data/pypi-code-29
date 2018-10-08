"""
Template for the config script to train one-class GMM and use it to compute scores for SAVI.
Steps 1 to 2 (or 3) should be run first
"""

from bob.pad.face.algorithm import VideoGmmPadAlgorithm

algorithm = VideoGmmPadAlgorithm(n_components={{ gmmcomponents }})

sub_directory = 'mouthdeltas42_{{ mfccenergy }}__blk{{ pcablocksize }}_pca{{ pcafeaturesize }}_gmm{{ gmmcomponents }}'

skip_extraction = True
skip_preprocessing = True
skip_extractor_training = True
skip_projector_training = True
skip_projection = True
skip_score_computation = False



