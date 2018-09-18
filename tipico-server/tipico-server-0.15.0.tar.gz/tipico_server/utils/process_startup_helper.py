import os

__version__= "$Id: process_startup_helper.py 26 2018-01-26 19:06:25Z lbusoni $"


class ProcessStartUpHelper(object):

    def __init__(self):
        self._moduleRoot= 'tipico_server'


    def instrumentStartUpScriptPath(self):
        return os.path.join(self._moduleRoot,
                            'instrument_controller',
                            'tipico_run_instrument_controller.py')


    def killAllProcessesStartUpScriptPath(self):
        return os.path.join(self._moduleRoot,
                            'utils',
                            'tipico_kill_processes.py')


    def processProcessMonitorStartUpScriptPath(self):
        return os.path.join(self._moduleRoot,
                            'process_monitor',
                            'tipico_run_process_monitor.py')


    def processProcessMonitorStopScriptPath(self):
        return os.path.join(self._moduleRoot,
                            'utils',
                            'tipico_server_stop.py')
