'''
Created on Oct 16, 2014

@author: tmahrt
'''

from os.path import join


from pyacoustics.utilities import utils


def cleanDejongSpeechRate(path):
    '''
    nsyll,
    npause,
    dur (s),
    phonationtime (s),
    speechrate (nsyll/dur),
    articulation rate (nsyll / phonationtime),
    ASD (speakingtime/nsyll)
    '''
    outputPath = join(path, "cleaned")
    utils.makeDir(outputPath)
    
    for fn in utils.findFiles(path, filterExt=".txt"):
        dataList = utils.openCSV(path, fn)
        dataList = [[item.strip() for item in row[1:]] for row in dataList]
        
        dataList = [",".join(row) for row in dataList]
        
        outputTxt = "\n".join(dataList)
        with open(join(outputPath, fn), "w") as fd:
            fd.write(outputTxt)
        
        
def untangleDejongOutput(path, fn):
    
    outputPath = join(path, "dejong_speech_rate")
    utils.makeDir(outputPath)
    
    rowList = utils.openCSV(path, fn)

    dataDict = {}
    
    for row in rowList:
        name = row[0].rsplit("_", 1)[0]
        dataDict.setdefault(name, [])
        dataDict[name].append(",".join(row[1:]))
        
    nameList = dataDict.keys()
    nameList.sort()
    
    for name in nameList:
        outputList = dataDict[name]
        with open(join(outputPath, name + ".txt"), "w") as fd:
            fd.write("\n".join(outputList))
