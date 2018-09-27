import pandas as pd
import os


def missingDataFiles(file_names: dict):
    missing_files = [key for key, file_name in file_names.items()
                     if not os.path.isfile(str(file_name))]
    return missing_files
