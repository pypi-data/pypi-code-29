

class CameraStatus(object):

    def __init__(self,
                 name,
                 frameWidth,
                 frameHeight,
                 dtype,
                 binning,
                 exposureTimeInMilliSec,
                 frameRate):
        self.name= name
        self.frameWidth= frameWidth
        self.frameHeight= frameHeight
        self.dtype= dtype
        self.binning= binning
        self.exposureTimeInMilliSec= exposureTimeInMilliSec
        self.frameRate= frameRate
