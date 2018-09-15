'''
Created on Jul 1, 2015

@author: tmahrt

Refactored out of audio_scripts.  Doesn't seem to work very well at
distinguishing silences from noise.

Originally written for doing noise detection without relying on
external libraries.
'''

import math
import wave
import struct


def findQuietestSilence(fn, duration, windowDuration):
    '''
    Finds the quietest silence of length /duration/
    
    The actual duration of the quietest silence will not be the same
    as /duration/
    
    duration and windowDuration are both in seconds
    '''
    
    audiofile = wave.open(fn, "r")
    
    params = audiofile.getparams()
    sampwidth = params[1]
    framerate = params[2]
    
    # Number of blocks that will fit into the duration
    blockSize = int(framerate * windowDuration)
    rmsIntensityList = []
    while True:
        waveData = audiofile.readframes(blockSize)
        if len(waveData) == 0:
            break

        actualNumFrames = int(len(waveData) / float(sampwidth))
        audioFrameList = struct.unpack("<" + "h" * actualNumFrames, waveData)
        
        rmsIntensityList.append(_rms(audioFrameList))
    
    # A 'block' here refers to one segment that is /duration/ long
    numSamplesPerBlock = int(round((duration) / windowDuration))
    
    # Calculate the sum of RMS values for every chunk
    sumList = [sum(rmsIntensityList[i:i + numSamplesPerBlock])
               for i in range(0, len(rmsIntensityList) - numSamplesPerBlock)]
    
    # Select the quietest chunk and convert to time
    startIndex = sumList.index(min(sumList))
    endIndex = startIndex + numSamplesPerBlock

    startTime = (startIndex * blockSize) / float(framerate)
    endTime = (endIndex * blockSize) / float(framerate)

    # The mean energy for this region
    meanRMSEnergy = sumList[startIndex]
    
    actualSilenceDuration = endTime - startTime
    
    return startTime, endTime, meanRMSEnergy, actualSilenceDuration


def findIntensityThreshold(fn, windowDuration, percentile):
    '''
    
    
    /percentile/ - percentage.  A value between 0 and 1.
    '''
    audiofile = wave.open(fn, "r")
    
    params = audiofile.getparams()
    sampwidth = params[1]
    framerate = params[2]
    
    # Number of blocks that will fit into the duration
    blockSize = int(framerate * windowDuration)
    rmsIntensityList = []
    while True:
        waveData = audiofile.readframes(blockSize)
        if len(waveData) == 0:
            break

        actualNumFrames = int(len(waveData) / float(sampwidth))
        audioFrameList = struct.unpack("<" + "h" * actualNumFrames, waveData)
        
        rmsIntensityList.append(_rms(audioFrameList))
    
    rmsIntensityList.sort()
    
    return rmsIntensityList[int(len(rmsIntensityList) * percentile)]


def findSilences(fn, silenceRMSThreshold, startTime=0):
    '''
    
    '''
    silenceList = []
    
    # Seed the search - we don't know if the audio begins with noise or silence
    findSilence = False
    firstEventTime = _findNextEvent(fn, startTime, silenceRMSThreshold,
                                    findSilence)
    if firstEventTime == 0:
        findSilence = True
        firstEventTime = _findNextEvent(fn, startTime, silenceRMSThreshold,
                                        findSilence)
    else:
        silenceList.append((0, firstEventTime))
    
    # Find all of the silences until the end of the file
    currentTime = firstEventTime
    
    while True:
        findSilence = not findSilence
        endTime = _findNextEvent(fn, currentTime, silenceRMSThreshold,
                                 findSilence)
        if endTime == currentTime:
            break
        if findSilence is True:
            silenceList.append((currentTime, endTime))
        currentTime = endTime
        
    return silenceList
        
    
def _findNextEvent(fn, startTime, silenceThreshold, findSilence=True):
    '''
    Accumulates wavdata until it hits the next silence/noise
    
    if findSilence=False then search for sound
    '''
    
    stepSize = 0.15  # in seconds
    numSteps = 3  # Number of steps required to be silence / noise
    
    audiofile = wave.open(fn, "r")
    
    params = audiofile.getparams()
    sampwidth = params[1]
    framerate = params[2]
    
    # Extract the audio frames
    i = 0
    currentSequenceNum = 0
    audiofile.setpos(int(framerate * startTime))
    while currentSequenceNum < numSteps:
        waveData = audiofile.readframes(int(framerate * stepSize))

        if len(waveData) == 0:
            break

        actualNumFrames = int(len(waveData) / float(sampwidth))
        audioFrameList = struct.unpack("<" + "h" * actualNumFrames, waveData)

        rmsEnergy = _rms(audioFrameList)
        if ((findSilence is True and rmsEnergy < silenceThreshold) or
           (findSilence is False and rmsEnergy > silenceThreshold)):
            currentSequenceNum += 1
        else:
            currentSequenceNum = 0
        i += 1
    
    endTime = startTime + (i - numSteps) * stepSize
    
    return endTime


def _rms(audioFrameList):
    audioFrameList = [val ** 2 for val in audioFrameList]
    meanVal = sum(audioFrameList) / len(audioFrameList)
    return math.sqrt(meanVal)
