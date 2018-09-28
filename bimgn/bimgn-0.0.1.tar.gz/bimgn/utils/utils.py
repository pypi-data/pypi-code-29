import os
import subprocess
import logging
import coloredlogs
import graypy


def check_input(starting_files):
    """
    Function that checks if a list of input files exists or not

    Parameters
    ----------
    starting_files : list
        List of paths that are going to be evaluated for existance

    Returns
    -------
    None

    """

    # Instance must be a list of files to check
    if not isinstance(starting_files, list):
        raise TypeError("starting_files must be a list of files")

    for in_file in starting_files:
        # Check if file is a path or string
        if not isinstance(in_file, str):
            raise TypeError("file must be a string (" + str(in_file) + ")")

        if not os.path.exists(in_file):
            raise Exception('Input file does not exists -> ' + in_file)

    return None


def check_empty(element_list):
    if len(element_list) == 0:
        raise IndexError("List of files to check format is empty")

    return None


def create_folders(dir_list):
    """
    Create all folders from a list passed by arguments if they do not exist

    Parameters
    ----------
    dir_list : list
        List containing all directories that are going to be created
    """
    # Check if input file_list is indeed a list of strings
    if not isinstance(dir_list, list):
        raise TypeError("Argument given to check format must be a list of string")

    # Check if list if empty. In that case, raise exception
    check_empty(dir_list)

    for folder in dir_list:

        if not isinstance(folder, str):
            raise TypeError("Argument given to check format must be a string, it was " + str(type(file_name)))

        if not os.path.exists(folder):
            cmd = 'mkdir ' + folder
            print('#[LOG]: Created folder -> ' + folder)
            run_cmd(cmd, 1)


def run_cmd(cmd, output=0):
    """
    Function that runs a command given by user
    """

    if output == 0:
        process = subprocess.Popen(cmd, shell=True, executable='/bin/bash', stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        out = process.stdout.readline()
        out = out.decode("utf-8").strip('\n')

        while out != '':
            print(out)
            out = process.stdout.readline()
            out = out.decode("utf-8").strip('\n')

    if output == 1:
        process = subprocess.Popen(cmd, shell=True, executable='/bin/bash', stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        output = []
        out = process.stdout.readline()
        out = out.decode("utf-8").strip('\n')

        while out != '':
            output.append(out)
            out = process.stdout.readline()
            out = out.decode("utf-8").strip('\n')

        return output

    else :
        try:
            os.system(cmd)
        except :
            raise Exception("Command failed: " + cmd + "\n")


def run_cmd_get_output(cmd):
    process = subprocess.Popen(cmd, shell=True, executable='/bin/bash',
                               stdout=subprocess.PIPE, stderr=subprocess.PIPE)

    out = None
    err = None
    lines = []

    while out != "" or err != "":
        out = process.stdout.readline()
        err = process.stderr.readline()
        out = out.decode("utf-8").strip('\n')
        err = err.decode("utf-8").strip('\n')
        lines.append(out)

    return lines


def set_mode(args):
    if args.d is True:
        mode = 'Debug'
    else:
        mode = 'Production'

    return mode


def set_log(name, dirs):

    log = logging.getLogger(name)
    log.setLevel(logging.DEBUG)

    for d in dirs:

        # create a file handler
        handler = logging.FileHandler(d)
        handler.setLevel(logging.DEBUG)
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        handler.setFormatter(formatter)

        log.addHandler(handler)

    # Create stream handler
    coloredlogs.install(level='INFO', logger=log)
    # ch = logging.StreamHandler(sys.stdout)
    # ch.setLevel(logging.INFO)
    # ch.setFormatter(formatter)
    #
    # log.addHandler(ch)

    handler_gp = graypy.GELFHandler('localhost', 12201)
    log.addHandler(handler_gp)

    return log
