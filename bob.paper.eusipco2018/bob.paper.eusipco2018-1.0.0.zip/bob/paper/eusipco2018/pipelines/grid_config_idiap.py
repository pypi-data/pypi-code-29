# Config script for running algorithms on Idiap's grid

import bob.bio.base

#grid = "modest"

grid = bob.bio.base.grid.Grid(
  number_of_preprocessing_jobs=48,
  number_of_extraction_jobs=48,
  number_of_projection_jobs=48,
  number_of_enrollment_jobs=48,
  number_of_scoring_jobs=1,
  training_queue = '16G',
  # preprocessing
  preprocessing_queue = '4G-io-big',
  # feature extraction
  extraction_queue = '4G-io-big',
  # feature projection
  projection_queue = '4G-io-big',
  # model enrollment
  enrollment_queue = '4G-io-big',
  # scoring
  scoring_queue = '4G-io-big'
)
