from .LINE import LINE
from PIL import Image
import requests
from io import BytesIO
import numpy as np
from matplotlib import pyplot as pt
import cv2
import _thread

try:
    from . import pi
except:
    #print('If you want to use Raspberry Pi module, pip install pigpio')
    pass

def to_onehot(target):
    targets = sorted(list(set(target)))
    idx = [targets.index(t) for t in target]
    return np.eye(len(targets), dtype='uint8')[idx]

def imread(url):
  try:
    response = requests.get(url)
    return Image.open(BytesIO(response.content))
  except:
    return Image.open(url)

def imshow(im):
  pt.figure()
  pt.imshow(im)
  pt.grid(False)
  pt.axis('off')

class VideoCapture_thread:
    def __init__(self, src=0):
        self.cap = cv2.VideoCapture(src)
        (self.grabbed, self.frame) = self.cap.read()
        self.stopped = False

    def start(self):
        _thread.start_new_thread(self.getframe, ())
        return self

    def getframe(self):
        while True:
            if self.stopped:
                self.cap.release()
                return
            (self.grabbed, self.frame) = self.cap.read()

    def read(self):
        return self.grabbed, self.frame

    def release(self):
        self.stopped = True