import os
import re
from .app_tools import get_executable_folder


def find_filename_in_folder(root_path, filename):
    for dirpath, dirnames, filenames in os.walk(root_path):
        if filename in filenames:
            print('find file:', os.path.join(dirpath, filename))
            return os.path.join(dirpath, filename)
    return None


def find_filename_in_app_folder(filename):
    return find_filename_in_folder(get_executable_folder(), filename)


def find_filename_with_pattern_in_folder(root_folder, pattern):
    print('current path:', root_folder, 'pattern', pattern)
    for dirpath, dirnames, filenames in os.walk(root_folder):
        for i in filenames:
            res = re.search(pattern, i)
            # print pattern, i
            if res is None:
                continue
                # print 'found item:', pattern, i
            return os.path.join(dirpath, i)
    print("path not found", pattern)
    return None


def find_file_with_pattern_in_app_folder(pattern):
    return find_filename_with_pattern_in_folder(get_executable_folder(), pattern)
