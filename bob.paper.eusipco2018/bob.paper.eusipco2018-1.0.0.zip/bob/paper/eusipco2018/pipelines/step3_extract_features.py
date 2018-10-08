"""
Template for the config script to process Audio and extract features for SAVI
Step 1 should be run first.
"""

from bob.project.savi.extractor import CepstralMouthDeltas

mfccenergy = '{{ mfccenergy }}'

extracted_directory = '../extracted_openpose_mouthdeltas42_{{ mfccenergy }}_blk{{ pcablocksize }}'
sub_directory = 'openpose_mouthdeltas42_{{ mfccenergy }}_blk{{ pcablocksize }}'


if mfccenergy == 'mfcc40':
    with_energy = True
else:
    with_energy = False

extractor = CepstralMouthDeltas(n_ceps=13,
                                n_filters=40,
                                f_min=300,
                                f_max=3700,
                                num_video_frames_per_block={{ pcablocksize }},
                                frame_dim=({{ dbname[1] }}, {{ dbname[2] }}),
                                for_frontal_faces_only=True,
                                with_energy=with_energy)

algorithm = "test"

skip_preprocessing = True
skip_extraction = False

