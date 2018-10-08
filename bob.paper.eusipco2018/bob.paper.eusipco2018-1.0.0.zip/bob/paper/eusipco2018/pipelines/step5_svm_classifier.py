"""
Template for the config script to train two-class SVM and use it to compute scores for SAVI.
Steps 1 to 2 (or 3) should be run first.
"""


from bob.pad.base.algorithm import SVM

# make sure that extractor of PCAReduction class returns a features
extractor.list_of_feature_blocks = False

algorithm = SVM(
    n_samples=1000,
    mean_std_norm_flag=True,
    trainer_grid_search_params={
        'cost': [2 ** p for p in range(-3, 14, 2)],
        'gamma': [2 ** p for p in range(-15, 0, 2)]},
    reduced_train_data_flag=True,
    n_train_samples=10000,
)

projector_file = 'SVMProjector.hdf5'
score_directories = ['svm']

skip_extraction = True
skip_preprocessing = True
skip_extractor_training = True
skip_projector_training = False
skip_projection = False
skip_score_computation = False

