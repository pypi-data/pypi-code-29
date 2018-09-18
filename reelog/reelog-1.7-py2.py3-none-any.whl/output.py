# -*- coding:utf-8 -*-
import os
import sys
import logging
import logging.handlers
from .formatter import TEXT_FORMATTER
from .handler import TTYHandler


OUTPUT_STDOUT = 1
OUTPUT_FILE = 2
OUTPUT_ROTATE_FILE = 3


def get_log_file_path(file_name=None):
    if not file_name:
        log_directory = os.path.join(os.path.dirname(sys.argv[0]), "log")
        if not os.path.exists(log_directory):
            os.mkdir(log_directory)
        log_name = ".".join(os.path.basename(sys.argv[0]).split(".")[:-1]) + "-" + str(os.getpid()) + ".log"
        file_name = os.path.join(log_directory,  log_name)
    return file_name


class Output(object):
    def __init__(self, handler, formatter=TEXT_FORMATTER, level=logging.INFO):
        self.handler = handler
        self.handler.setFormatter(formatter)
        self.handler.setLevel(level)


class Stream(Output):
    def __init__(self, stream=sys.stdout, formatter=TEXT_FORMATTER, level=logging.INFO):
        super(Stream, self).__init__(TTYHandler(stream), formatter, level)


class File(Output):
    def __init__(self, filename=None, formatter=TEXT_FORMATTER, level=logging.INFO):
        log_file_path = get_log_file_path(file_name=filename)
        handler = logging.FileHandler(filename=log_file_path)
        super(File, self).__init__(handler, formatter, level)


class RotatingFile(Output):
    def __init__(self, filename=None, formatter=TEXT_FORMATTER, level=logging.INFO):
        log_file_path = get_log_file_path(file_name=filename)
        handler = logging.handlers.RotatingFileHandler(filename=log_file_path, maxBytes=10*1024*1024, backupCount=10)
        super(RotatingFile, self).__init__(handler, formatter, level)


OUTPUT_MAPPING = {
    OUTPUT_STDOUT: "Stream()",
    OUTPUT_FILE: "File()",
    OUTPUT_ROTATE_FILE: "RotatingFile()",
}

def get_output_obj_list(outputs):
    output_list = list(map(eval, [OUTPUT_MAPPING.get(output, None) for output in outputs]))
    if output_list and all(output_list):
        return output_list
    else:
        raise ValueError