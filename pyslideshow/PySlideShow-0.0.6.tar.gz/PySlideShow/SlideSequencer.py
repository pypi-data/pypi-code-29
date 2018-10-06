import time
from enum import Enum
from Slide import *

class SlideSequencer:
    class StateType(Enum):
        slide = 0
        blend = 1

    blendTime = 1.5
    slideList = list()
    state = None
    lastStateChangeTime = None
    primarySlideId = None
    secondarySlideId = None
    timeSinceStateChange = None
    paused = False

    def __init__(self, display, configuration, configuration_directory):
        for slide_index in range(len(configuration)):
            self.slideList.append(Slide(slide_index, configuration[slide_index], display, configuration_directory))

    def set_paused(self, paused):
        self.paused = paused

    def get_paused(self):
        return self.paused

    def getSlide(self, slide_id):
        return self.slideList[slide_id]

    def updateState(self, newState, newPrimarySlideId, newSecondarySlideId):
        self.state = newState
        self.lastStateChangeTime = time.time()
        self.timeSinceStateChange = 0

        self.primarySlideId = newPrimarySlideId
        self.secondarySlideId = newSecondarySlideId

        print "State change to '" + newState.name + "'. PrimaryId=%d  SecondaryId=%d." % (self.primarySlideId, self.secondarySlideId)

        if newState == self.StateType.blend and self.secondarySlideId >= 0:
            self.slideList[self.secondarySlideId].appearanceTime = self.lastStateChangeTime

    def start(self):
        print 'Blending in ...'
        self.updateState(self.StateType.blend, -1, 0)

    def forward(self, distance=1):
        if distance > 1:
            # do not jump bejon the end
            distance = min(distance, len(self.slideList) - self.primarySlideId - 1)
        # forward can not be used to skip backwards
        assert distance >= 1
        if self.primarySlideId + distance >= len(self.slideList):
            # at last slide so blend out
            print 'Blending out ...'
            self.updateState(self.StateType.blend, self.primarySlideId, -1)
        else:
            # start blending into next slide
            self.updateState(self.StateType.blend, self.primarySlideId, self.primarySlideId + distance)

    def backward(self, distance=1):
        # do not jump below zero
        distance = min(distance, self.primarySlideId)
        self.updateState(self.StateType.blend, self.primarySlideId, self.primarySlideId - distance)

    def run(self):
        thisIterationTime = time.time()
        self.timeSinceStateChange = thisIterationTime - self.lastStateChangeTime

        primarySlide = self.slideList[self.primarySlideId]

        # time triggered transitions
        if not self.paused:
            # end of slide section
            if self.state == self.StateType.slide and self.timeSinceStateChange > primarySlide.duration:
                self.forward()

            # end of blend section - make the previously secondary slide the new primary slide
            if self.state == self.StateType.blend and self.timeSinceStateChange > self.blendTime:
                if self.secondarySlideId >= len(self.slideList) or self.secondarySlideId == -1:
                    print 'Reached end.'
                    return False # end sequence
                # primary slide id still can be -1 during blend in
                assert self.secondarySlideId >= 0
                self.updateState(self.StateType.slide, self.secondarySlideId, -1)

        # calculate opacities during blending
        primaryOpacity = 1
        secondaryOpacity = 0
        if self.state == self.StateType.blend:
            secondaryOpacity = self.timeSinceStateChange / self.blendTime
            primaryOpacity = 1 - secondaryOpacity

        if self.primarySlideId >= 0:
            primarySlide = self.slideList[self.primarySlideId]
            nt = (thisIterationTime - primarySlide.appearanceTime) / (primarySlide.duration + 2 * self.blendTime)
            primarySlide.normalizedTime = max(0.0, min(1.0, nt))
            primarySlide.render(primaryOpacity)
        if self.secondarySlideId >= 0:
            secondarySlide = self.slideList[self.secondarySlideId]
            nt = (thisIterationTime - secondarySlide.appearanceTime) / (secondarySlide.duration + 2 * self.blendTime)
            secondarySlide.normalizedTime = max(0.0, min (1.0, nt))
            secondarySlide.render(secondaryOpacity)

        return True # continue sequence


if __name__ == '__main__':
    display = tuple([1024, 768])
    sequencer = SlideSequencer(display, True)
    sequencer.start()
    for i in range(500):
        if not sequencer.run():
            break
