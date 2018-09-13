# -*- coding: utf-8 -*-
"""
__title__ = 'SparkStarter'
__author__ = 'JieYuan'
__mtime__ = '2018/3/16'
"""

import os
from glob import glob
from pathlib import Path

from pyspark.sql import SparkSession


class SparkStarter(object):
    """.bashrc or .bash_profile
    SPARK_HOME=.../spark
    PYTHON_HOME=.../anaconda3
    PYTHONPATH=$SPARK_HOME/python/lib/py4j-0.10.6-src.zip:$SPARK_HOME/python
    PATH=$PYTHON_HOME/bin:$SPARK_HOME/bin:$SPARK_HOME/python:$SPARK_HOME/python/lib/py4j-0.10.4-src.zip:$PATH

    # pyspark (jupyter notebook)
    export PYSPARK_PYTHON=python3
    export PYSPARK_DRIVER_PYTHON=ipython
    export PYSPARK_DRIVER_PYTHON_OPTS="notebook"
    """

    def __init__(self, spark_home=None, python_home=None, enable_hive=False, jars_dir=None):
        self.spark_home = Path(spark_home).as_posix()
        self.python_home = python_home
        self.enable_hive = enable_hive
        self.jars_dir = jars_dir
        self._environ_set()

    @property
    def sc_spark(self):
        _spark = SparkSession.builder \
            .appName("iSpark") \
            .config('log4j.rootCategory', "WARN")
        if self.enable_hive:
            _spark = _spark.enableHiveSupport()
        elif self.jars_dir:
            _spark = _spark.config('spark.jars', os.path.abspath(self.jars_dir))

        spark = _spark.getOrCreate()
        return spark.sparkContext, spark

    def _environ_set(self):
        if self.python_home:
            _ = self.python_home
        elif os.sys.platform == 'linux':
            _ = os.popen('which python').read().strip()
        elif os.environ.get('PYTHON_HOME'):
            _ = os.environ.get('PYTHON_HOME')
        else:
            raise Exception("Please input python_home!!!")

        os.environ["PYSPARK_PYTHON"] = _
        os.environ["SPARK_HOME"] = self.spark_home

        os.sys.path.append("%s/python" % self.spark_home)
        os.sys.path.append(glob("%s/python/lib/py4j*.zip" % self.spark_home)[0])


SPARK = \
    '''
          ____              __
         / __/__  ___ _____/ /__
        _\ \/ _ \/ _ `/ __/  '_/
       /___/ .__/\_,_/_/ /_/\_\    >>> https://pypi.org/project/iSpark
          /_/

    '''
if __name__ == '__main__':
    pass
else:
    print(SPARK)
