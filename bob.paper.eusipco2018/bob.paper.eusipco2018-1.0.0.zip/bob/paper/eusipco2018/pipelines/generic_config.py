"""
Template for the generic config file for SAVI. It should be used in combinaiton with other config files.
"""

from bob.project.savi.database import SAVIPadDatabase

db_name = '{{ dbname[0] }}'
location = '{{ location }}'

database = SAVIPadDatabase(db_name=db_name)

# a dummy extractor for protocol
extractor = "test"

# a dummy algorithm for protocol
algorithm = "test"

sub_directory = 'db_name'

preprocessed_directory = '../openpose_preprocessed'
extracted_directory = '../openpose_extracted'

groups = ['dev']

# change the path to the actual audio data inside "path_to_data.txt" file
database_directories_file = "path_to_data_{{ location }}.txt"

verbose = 3

protocol = 'oneset'

allow_missing_files = True
skip_preprocessing = True
skip_extraction = True
skip_extractor_training = True
skip_projector_training = True
skip_projection = True
skip_score_computation = True
