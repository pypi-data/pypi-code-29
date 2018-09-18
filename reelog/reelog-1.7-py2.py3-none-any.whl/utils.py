# -*- coding:utf-8 -*-
import os
import sys
import inspect


def get_program_name():
    return os.path.basename(inspect.stack()[-1][1])


def get_log_file_path(file_name=None):
    if not file_name:
        log_directory = os.path.join(os.path.dirname(sys.argv[0]), "log")
        if not os.path.exists(log_directory):
            os.mkdir(log_directory)
        log_name = ".".join(os.path.basename(sys.argv[0]).split(".")[:-1]) + ".log"
        file_name = os.path.join(log_directory,  log_name)
    return file_name
