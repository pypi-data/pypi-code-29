# -*- coding:utf-8 -*-
import logging
import weakref

from .output import get_output_obj_list, OUTPUT_STDOUT, OUTPUT_FILE, OUTPUT_ROTATE_FILE


_REE_LOGGERS = weakref.WeakValueDictionary()


def get_logger(name="root", stdout=True, file=False, rotate_file=False, level=logging.INFO):
    if not name:
        name = "root"
    logger = _REE_LOGGERS.get(name)
    if not logger:
        outputs = []
        if stdout is False and file is False and rotate_file is False:
            raise ValueError("reelog out type is None.")
        elif file is True and rotate_file is True:
            raise  ValueError("reelog out type file and rotate_file can not coexist")
        if stdout is True:
            outputs.append(OUTPUT_STDOUT)
        if file is True:
            outputs.append(OUTPUT_FILE)
        if rotate_file is True:
            outputs.append(OUTPUT_ROTATE_FILE)
        logger = _init_logger(name, outputs, level)
        _REE_LOGGERS[name] = logger

    return logger


def _init_logger(name, outputs, level):
    logger = logging.getLogger(name)
    logger.setLevel(level)
    [logger.removeHandler(handler) for handler in logger.handlers]
    [logger.addHandler(output_obj.handler) for output_obj in get_output_obj_list(outputs)]
    return logger
