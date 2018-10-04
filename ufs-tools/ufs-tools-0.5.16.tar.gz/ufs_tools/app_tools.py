import os
import sys


def get_executable():
    """
    Get the executable position, if the application is called without path, then this function will fail.
    :return:
    """
    # print sys.argv
    # stack = inspect.stack()
    # s = stack[-1][1]
    # for i in stack:
    #     print i
    s = os.path.abspath(sys.argv[0])
    # print s
    return s


def get_executable_folder():
    executable_folder = os.path.dirname(get_executable())
    if executable_folder == "":
        print("!!!!!!!!!", executable_folder)
        executable_folder = os.getcwd()
    return executable_folder


if __name__ == '__main__':
    print(get_executable_folder())
