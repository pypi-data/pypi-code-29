# Config script to extracts Video features for SAVI video

from bob.project.savi.preprocessor import VideoMouthRegion

database.original_extension = ".avi"

# save all landmarks
preprocessor = VideoMouthRegion(landmarks_range=(0, 68))

skip_preprocessing = False

# force = True
