
__version__= "$Id: deformable_mirror_status.py 26 2018-01-26 19:06:25Z lbusoni $"


class DeformableMirrorStatus(object):

    def __init__(self,
                 actuatorCommands,
                 commandCounter):
        self._actuatorCommands= actuatorCommands
        self._commandCounter= commandCounter


    def commandCounter(self):
        return self._commandCounter


    def actuatorCommands(self):
        return self._actuatorCommands
