import pandas as pd
import os


def missingDataFiles(file_names: dict):
    '''
    file_names: dict - dictionary of file names to check if it exists
    '''
    missing_files = [key for key, file_name in file_names.items()
                     if not os.path.isfile(str(file_name))]
    return missing_files
