'''
Created on May 4, 2016

@author: tmahrt
'''

inputPath = r"C:\Users\Tim\Desktop\noise_filtered_speech2"
soxEXE = r"C:\sox\sox.exe"
outputPath = r"C:\Users\Tim\Desktop\output"
newSampleRate = 16000
import os
for fn in os.listdir(inputPath):
    if os.path.splitext(fn)[1] != ".wav":
        continue
    resampleAudio(soxEXE, newSampleRate, inputPath, fn, outputPath)
    