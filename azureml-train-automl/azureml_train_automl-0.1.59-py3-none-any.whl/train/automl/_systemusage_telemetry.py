# ---------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# ---------------------------------------------------------
"""_systemusage_telemetry.py, A file system usage telemetry classes"""

import os
import subprocess
import sys

from ._timer_utilities import TimerCallback


class SystemResourceUsageTelemetryFactory:
    """System resource usage telemetry collection factory class"""
    @staticmethod
    def get_system_usage_telemetry(logger, interval=10, **kwargs):
        """
        gets system usage telemetry object based on platform
        :param logger: logger
        :param interval: interval in sec
        :return: SystemResourceUsageTelemetry : platform specific object
        """
        if sys.platform == "win32":
            return _WindowsSystemResourceUsageTelemetry(logger, interval=interval, **kwargs)

        return _NonWindowsSystemResourceUsageTelemetry(logger, interval=interval, **kwargs)


class SystemResourceUsageTelemetry:
    """System usage telemetry abstract class"""
    def __init__(self, logger, interval=10, **kwargs):
        """
        initializes system resource usage telemetry class
        :param logger: logger
        :param interval: interval in sec
        :param kwargs: kwargs
        """
        self.logger = logger
        self.interval = interval
        self.kwargs = kwargs
        self._timer = None

    def start(self):
        """
        starts usage collection
        :return:
        """
        pass

    def stop(self):
        """
        stops collection
        :return:
        """
        pass

    def __del__(self):
        """
        cleanup
        :return:
        """
        pass


class _WindowsSystemResourceUsageTelemetry(SystemResourceUsageTelemetry):
    """
    Telemetry Class for collecting system usage
    """

    def __init__(self, logger, interval=10, **kwargs):
        """
        Constructor
        :param logger: logger
        :param interval: collection frequency in seconds
        :param kwargs:
        """
        self._cmd = "tasklist /v /fi \"pid eq {}\" /fo csv".format(os.getpid())
        super(_WindowsSystemResourceUsageTelemetry, self).__init__(logger, interval=interval, **kwargs)

    def start(self):
        """
        starts usage collection
        :return:
        """
        self.logger.info("Starting usage telemetry collection")
        self._timer = TimerCallback(interval=self.interval, logger=self.logger, callback=self._get_usage)

    def _get_usage(self):
        """
        gets usage
        :return:
        """
        try:
            import csv
            from io import StringIO

            proc = subprocess.Popen(self._cmd, stdout=subprocess.PIPE, shell=True)
            (out, err) = proc.communicate()
            data = out.decode('utf-8')

            csv_reader = csv.reader(StringIO(data))
            mem_index = -1
            cpu_index = -1
            lines = 0
            for row in csv_reader:
                lines += 1

                if lines == 1:  # header
                    mem_index = row.index('Mem Usage')
                    cpu_index = row.index('CPU Time')
                    continue

                if mem_index != -1:
                    self.logger.info("memory usage {}".format(row[mem_index]),
                                     extra={'properties': {'Type': 'MemoryUsage',
                                                           'Usage': row[mem_index]}})

                if cpu_index != -1:
                    self.logger.info("cpu time {}".format(row[cpu_index]),
                                     extra={'properties': {'Type': 'CPUUsage',
                                                           'CPUTime': row[cpu_index],
                                                           'Cores': os.cpu_count()}})
        except Exception as e:
            self.logger.info(e)

    def stop(self):
        """
        stops timer
        :return:
        """
        if self._timer is not None:
            self._timer.stop()

    def __del__(self):
        """
        destructor
        :return:
        """
        self.stop()


class _NonWindowsSystemResourceUsageTelemetry(SystemResourceUsageTelemetry):
    """Linux, Mac & other os"""

    def __init__(self, logger=None, interval=10, **kwargs):
        self.logger = logger
        self.interval = interval
        self.kwargs = kwargs
        self._timer = None
        super(_NonWindowsSystemResourceUsageTelemetry, self).__init__(logger=logger, interval=interval, **kwargs)

    def start(self):
        """
        starts usage collection
        :return:
        """
        self.logger.info("Starting usage telemetry collection")
        self._timer = TimerCallback(interval=self.interval, logger=self.logger, callback=self._get_usage)

    def _get_usage(self):
        """
        gets usage
        :return:
        """
        try:
            import resource
            res = resource.getrusage(resource.RUSAGE_SELF)

            self.logger.info("memory usage {}".format(res.ru_maxrss),
                             extra={'properties': {'Type': 'MemoryUsage',
                                                   'Usage': res.ru_maxrss}})

            self.logger.info("cpu time {}".format(res.ru_utime),
                             extra={'properties': {'Type': 'CPUUsage',
                                                   'CPUTime': res.ru_utime,
                                                   'SystemTime': res.ru_stime,
                                                   'Cores': os.cpu_count()}})
        except Exception as e:
            self.logger.info(e)

    def stop(self):
        """
        stops timer
        :return:
        """
        if self._timer is not None:
            self._timer.stop()

    def __del__(self):
        """
        destructor
        :return:
        """
        self.stop()
