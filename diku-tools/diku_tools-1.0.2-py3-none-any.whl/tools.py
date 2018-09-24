import os
import platform
import re
from datetime import timedelta


def create_dir(path):
    if not os.path.exists(path):
        os.makedirs(path)


def clean_dir(dir_name):
    dir_name = dir_name \
        .replace(':', ' -') \
        .replace('/', '-') \
        .replace('...', '') \
        .replace('<', '') \
        .replace('>', '') \
        .replace('\'', '') \
        .replace('\"', '') \
        .replace('`', '') \
        .strip()
    return re.sub(r'/*$', '/', dir_name)


def clean_file(file_name):
    return file_name \
        .replace(':', ' -') \
        .replace('/', '-') \
        .replace('...', '') \
        .replace('<', '') \
        .replace('>', '') \
        .replace('\'', '') \
        .replace('\"', '') \
        .replace('`', '') \
        .strip()


def create_shortcut(path, url):
    if os.path.isfile(path + ".bat") or os.path.isfile(path + ".sh"):
        return

    if platform.system() == "Windows":
        file = open(path + ".bat", "w")
    else:
        file = open(path + ".sh", "w")

    file.write('start "" "%s"' % url)
    file.close()


def timedelta_string(delta: timedelta):
    secs = delta.seconds % (60 * 60 * 24)
    hours = int(secs / (60 * 60))
    secs %= (60 * 60)
    minutes = int(secs / 60)
    return "%02d:%02d" % (hours, minutes)
