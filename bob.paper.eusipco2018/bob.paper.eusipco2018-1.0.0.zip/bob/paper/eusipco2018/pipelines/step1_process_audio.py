# Config script to preprocess audio for SAVI video

from bob.project.savi.preprocessor import VoiceVAD
from bob.project.savi.database import SAVIPadDatabase


def new_annotations(self, annotation_file):
    pass

funcType = type(database.annotations)
database.annotations = funcType(new_annotations, SAVIPadDatabase)

# save all landmarks
preprocessor = VoiceVAD()

skip_preprocessing = False



