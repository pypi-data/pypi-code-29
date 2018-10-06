# log everything
from greenjay.fileHandler import LoggerFileHandler
from greenjay.outputConsole import OutputConsole

class Logger(object):

    LEVELS = [
        "Emergency",
        "Error",
        "Alert",
        "Warning",
        "Info",
        "Debug",
        "Trivial"
    ]

    def __init__(self, options):
        self.options = options

    def sendToLogging(self, msg, level):
        # write to file handler
        write = LoggerFileHandler(self.options['dirPath'], self.options['filePath'])

        if not write.checkFolder():
            write.makeDir()

        if write.checkFile():
            write.appendToFile(msg, self.LEVELS[level])
        else:
            write.writeToFile(msg, self.LEVELS[level])
        # send to console
        console = OutputConsole()
        console.writeToConsole(msg, self.LEVELS[level])

    def emergency(self, msg):
        level = 0
        self.sendToLogging(msg, level)

    def error(self, msg):
        level = 1
        self.sendToLogging(msg, level)

    def alert(self, msg):
        level = 2
        self.sendToLogging(msg, level)

    def warning(self, msg):
        level = 3
        self.sendToLogging(msg, level)

    def info(self, msg):
        level = 4
        self.sendToLogging(msg, level)

    def debug(self, msg):
        level = 5
        self.sendToLogging(msg, level)

    def trivial(self, msg):
        level = 6
        self.sendToLogging(msg, level)
