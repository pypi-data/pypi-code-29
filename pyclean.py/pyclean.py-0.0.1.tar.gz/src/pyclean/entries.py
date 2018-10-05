#!/usr/bin/env python
# -*- coding: utf-8 -*-

import logging
import os


logger = logging.getLogger(__name__)


COMPILED_EXTENSIONS = [".pyc", ".pyo"]


def find_compiled_files(parent, source_name):
    stem, ext = os.path.splitext(source_name)
    if ext != ".py":
        return

    # Find in the current directory.
    for ext in COMPILED_EXTENSIONS:
        path = os.path.join(parent, stem + ext)
        if os.path.exists(path):
            yield path

    # Look for matching names in __pycache__.
    pycache = os.path.join(parent, "__pycache__")
    if os.path.isdir(pycache):
        prefix = stem + "."
        for filename in os.listdir(pycache):
            if not filename.startswith(prefix):
                continue
            if not any(filename.endswith(ext) for ext in COMPILED_EXTENSIONS):
                continue
            yield os.path.join(pycache, filename)


def iter_compiled_files(source):
    """Yield built files to remove (e.g. .pyc, .pyo) related to the entry.

    The entry may be either a file or directory.
    """
    if not os.path.isdir(source):
        dirpath, filename = os.path.split(source)
        for fn in find_compiled_files(dirpath, filename):
            yield fn
        return
    for parent, dirnames, filenames in os.walk(source):
        for filename in filenames:
            for fn in find_compiled_files(parent, filename):
                yield fn
        try:    # Optimization: Don't look into __pycache__.
            dirnames.remove("__pycache__")
        except ValueError:
            pass


def remove_file(path):
    logger.debug("removing %s", path)
    try:
        os.unlink(path)
    except OSError as e:
        logger.error("failed to remove file %s", path)
        logger.debug("exception: %s", e)
        return 0
    return 1


def clean(entries):
    counter = 0
    for entry in entries:
        for path in iter_compiled_files(entry):
            counter += remove_file(path)
    logger.info("removed files: %s", counter)
    return counter
