'''
Created on Mar 26, 2014

@author: tmahrt
'''
import os
import subprocess
from os.path import join

from pyacoustics.utilities import utils
from pyacoustics.utilities import sequences
from pyacoustics.signals import audio_scripts
from pyacoustics.utilities import error_utils

MATLAB_EXE_PATH = "/Applications/MATLAB_R2014a.app/bin/matlab"
MATLAB_CODE_PATH = "/Users/tmahrt/Dropbox/matlab"
MATLAB_CODE_PATH = join("/Users/tmahrt/Dropbox/workspace",
                        "AcousticFeatureExtractionSuite/matlabScripts")


def runMatlabFunction(command, printCmd=False):
    error_utils.checkForApplication(MATLAB_EXE_PATH)

    pathCode = "addpath('%s');" % MATLAB_CODE_PATH
    exitCode = "exit;"
    
    codeSequence = pathCode + command + exitCode

    if printCmd is True:
        print(MATLAB_EXE_PATH + ' -nosplash -nodesktop -r "%s"' % codeSequence)
    myProcess = subprocess.Popen([MATLAB_EXE_PATH, "-nosplash",
                                  "-nodesktop", "-r", codeSequence])
    if myProcess.wait():
        exit()  # Something has gone wrong (an error message should be printed)


def matlabVAD(inputPath, outputPath, inputFN, noiseFN, outputFN,
              threshold=0.5, win_dur=0.05, hop_dur=0.025,
              num_sam=-1, do_noise_estimation=0):
    '''
    A front end to a matlab script
    
    I find that for clean recordings, modifying the win_dur and hop_dur
    don't seem to change the results significantly.
    
    do_noise_estimation=1 is worse for clean speech than =0
    
    A higher threshold is better for clean speech but higher than 0.5 didn't
    result in much difference
    '''
    
    fmtStr = "lee_vad('%s', '%s', %f, %f, %f, %d, %d, '%s');"
    vadInst = fmtStr % (join(inputPath, inputFN), join(outputPath, noiseFN),
                        threshold, win_dur, hop_dur, num_sam,
                        do_noise_estimation, join(outputPath, outputFN))

    runMatlabFunction(vadInst)


def parseVADOutput(path, fn, timeStep, timeThreshold,
                   pitchTracks=None, pitchSamplingFrequency=None):
    '''
    Converts the matlab VAD's binary array into a series of speech intervals
    
    VAD reports at each timestep whether speech is occuring or not (1 or 0).
    '''
    vadList = utils.openCSV(path, fn, 0)
    vadList = [int(val) for val in vadList]
    
    vadListComp = sequences.compressList(vadList)
    
    transformedDict = sequences.compressedListTransform(vadListComp, timeStep,
                                                        timeThreshold)
#     nonspeechEntryList = transformedDict[0]
    speechEntryList = transformedDict[1]

    pitchTracks = [float(val) for val in pitchTracks]

    # Optionally filter out speech segments that don't have any
    # pitch values (essentially loud noises)
    if pitchTracks is not None:
        newSpeechEntryList = []
        for entry in speechEntryList:
            startIndex = int(entry[0] * pitchSamplingFrequency)
            endIndex = int(entry[1] * pitchSamplingFrequency)
            f0List = pitchTracks[startIndex:endIndex]
            maxF0 = max(f0List)
            if int(maxF0) != 0:
                newSpeechEntryList.append([entry[0], entry[1]])
        speechEntryList = newSpeechEntryList
        
    return speechEntryList


def doVAD(path, fn, outputPath, timeStep, timeThreshold,
          redoFlag=False, pitchTracks=None, pitchSamplingFreq=None):
    
    utils.makeDir(outputPath)

    name = os.path.splitext(fn)[0]

    silenceFN = name + "_silence.wav"
    csvFN = name + "_vad.csv"
       
    # Create the silence file
    if redoFlag or not os.path.exists(join(outputPath, silenceFN)):
        silenceTuple = audio_scripts.findQuietestSilence(join(path, fn),
                                                         1.0, 0.05)
        startTime, endTime, meanEnergy, silence_duration = silenceTuple
        print("%f, %f, %f, %f" %
              (startTime, endTime, meanEnergy, silence_duration))
        audio_scripts.extractSubwav(join(path, fn),
                                    join(outputPath, silenceFN),
                                    startTime, endTime, True)
           
    # Create the textgrids
    if redoFlag or not os.path.exists(join(outputPath, csvFN)):
        matlabVAD(path, outputPath, fn, silenceFN, csvFN, hop_dur=timeStep)
    
    # Convert the VAD output to timestamped intervals
    entryList = parseVADOutput(outputPath, csvFN, timeStep, timeThreshold,
                               pitchTracks, pitchSamplingFreq)
    
    return entryList
