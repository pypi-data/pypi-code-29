
import os
from os.path import join

def loadCSV(fn):

    with open(fn, "r") as fd:
        data = fd.read()
    dataList = data.splitlines()
    dataList = [row.split(",") for row in dataList]
    return dataList


def transfer(dataFN, codeFN, outputFN):

    dataList = loadCSV(dataFN)
    codeList = loadCSV(codeFN)

    # Associate each group with a list of images
    codeList = codeList[1:] # Remove first row
    groupDict = {}
    for image, group in codeList:
        groupDict.setdefault(group, [])
        groupDict[group].append(image)

    groupKeyList = groupDict.keys()
    groupKeyList.sort()

    for group in groupDict.keys():
        print(group, groupDict[group])

    invGroupDict = {}
    for group, imageList in groupDict.items():
        for image in imageList:
            invGroupDict[image] = group

    # Create the output key list
    # Each row in outputKeyList contains one image name
    # for each of the groups.  Groups with fewer image
    # names than others, will have a null name '' for
    # the final few rows
    outputKeyList = []
    while True:
        oneNewValFlag = False
        outputKeyList.append([])
        for key in groupKeyList:
            newVal = ''
            if len(groupDict[key]) > 0:
                newVal = groupDict[key].pop(0)
                oneNewVal = True
            outputKeyList[-1].append(newVal)
        
        if not oneNewVal:
            break
        else:
            oneNewVal = False

    # Process user data
    # Associate each image name with the set of users responses
    dataDict = {'':['',]}

    tDataList = zip(*dataList)

    for row in tDataList[1:]:
        dataDict[row[0]] = row[1:]
    
    #
    tCombinedOutputDict = {}
    for subList in outputKeyList:
        for i, imageCode in enumerate(subList):
            key = ''
            if imageCode != '':
                key = invGroupDict[imageCode]
            tCombinedOutputDict.setdefault(key, [])
            tCombinedOutputDict[key].extend(dataDict[imageCode])
            
    tCombinedOutputList = []
    for groupKey in groupKeyList:
        tCombinedOutputList.append([groupKey,] + tCombinedOutputDict[groupKey])
#         tOutputList = [dataDict[imageCode] for imageCode in subList]

    maxLen = max([len(subList) for subList in tCombinedOutputList])
    for subList in tCombinedOutputList:
        subList.extend(["",]*(maxLen - len(subList)))

        
        #combinedOutputList.append(outputList)
    combinedOutputList = zip(*tCombinedOutputList)

    print(combinedOutputList[0])
        
    combinedOutputList = [",".join(row) for row in combinedOutputList]
    outputTxt = "\n".join(combinedOutputList)

    with open(outputFN, "w") as fd:
        fd.write(outputTxt)
        

if __name__ == "__main__":

    path = "/Users/tmahrt/Downloads"
    fn1 = "Tum_Preference_data_07232015.csv"
    fn2 = "Tum_Preference_data_07232015_data.csv"
    fn3 = "PostHocDesigner.csv"

    transfer(join(path, fn1),
             join(path, fn2),
             join(path, fn3))
