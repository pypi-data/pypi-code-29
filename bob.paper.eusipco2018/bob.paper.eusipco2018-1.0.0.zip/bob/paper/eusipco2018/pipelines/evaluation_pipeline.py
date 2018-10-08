# Config script to extract Audio features for SAVI audio

# run like this:
#

import os
import sys
import bob.bio.base
import bob.pad.voice

dir = os.path.dirname(__file__)
sys.path.append(os.path.abspath(dir))
from bob.project.savi.database import SAVIBioDatabase
from bob.project.savi.database import SAVIPadDatabase
from bob.project.savi.preprocessor import VoiceVAD
from bob.project.savi.extractor import CepstralOpticalFlow

database = SAVIPadDatabase()

# change the path to the actual audio data inside "path_to_data.txt" file
database_directories_file = "path_to_data.txt"

preprocessor = VoiceVAD()

extractor = CepstralOpticalFlow()

verbose = 3

algorithm = "gmm"

grid = "modest"

# # a grid for testing on a local machine
# grid = bob.bio.base.grid.Grid(
#   grid_type='local',
#   number_of_parallel_processes=1
# )
# run_local_scheduler = True
# nice = 10

projector_file = "Projector_gmm_mfcc20_histfof_spoof.hdf5"
skip_extraction = True
skip_preprocessing = True
skip_projector_training = True

#sub_directory = "savi"
groups = ['train', 'dev']



