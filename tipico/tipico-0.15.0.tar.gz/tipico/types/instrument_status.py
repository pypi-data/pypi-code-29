

class InstrumentStatus(object):

    def __init__(self,
                 actuatorCommands,
                 commandCounter):
        self._actuatorCommands= actuatorCommands
        self._commandCounter= commandCounter


    def commandCounter(self):
        return self._commandCounter


    def actuatorCommands(self):
        return self._actuatorCommands
