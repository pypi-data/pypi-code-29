import os
from datetime import datetime

class LoggerFileHandler(object):
    def __init__(self, dirPath, filePath):
        self.filePath = filePath + '.log'
        self.dirPath = './' + dirPath
        self.fullPath = self.dirPath + '/' + self.filePath

    def checkFolder(self):
        return os.path.isdir(self.dirPath)

    def checkFile(self):
        return os.path.isfile(self.fullPath)

    def makeDir(self):
        try:
            os.mkdir(self.dirPath)
        except:
            print("Could not Create Dir.")

    def writeToFile(self, msg, level):
        try:
            date = f'{datetime.now():%Y-%m-%d %H:%M:%S%z}'
            file = open(self.fullPath, 'w+')
            file.write(f'Date: {date} - Level: {level} - Message: {msg} \n')
            file.close()
        except:
            print("Could not Write to File.")

    def appendToFile(self, msg, level):
        try:
            date = f'{datetime.now():%Y-%m-%d %H:%M:%S%z}'
            file = open(self.fullPath, 'a+')
            file.write(f'Date: {date} - Level: {level} - Message: {msg} \n')
            file.close()
        except:
            print("Could not Append to File.")
