import os

def file_exists_q(full_filename:str) -> bool:
    exists_q = os.path.isfile(full_filename)
    if not exists_q:
        raise FileNotFoundError(f'''File {full_filename} does not exist.''')
    return exists_q


def basename_no_ext(filename):
    return os.path.basename(filename).split('.')[0]

def filelines(full_filename):
    """
    Quickly returns the number of lines in a file.
    Returns None if an error is raised.
    """
    if file_exists_q(full_filename):
        with open(full_filename, 'r') as file:
            return sum(1 for line in file)
    return None

def linesplit(line, delim='\t', newline='\n'):
    return line.rstrip(newline).split(delim)
