import argparse
import configparser
import importlib
import json
import logging
import os
import sys
from pathlib import Path
import numpy as np

from session import Session

# ------------------ CONFIG ----------------------
parser = argparse.ArgumentParser()
parser.add_argument("--log", help="See the log output in the terminal.", action="store_true")
arg = parser.parse_args()

config = configparser.ConfigParser()
config.read('settings.ini')

logger = logging.getLogger('reports')

if arg.log:
    logging.basicConfig(level=logging.INFO)
else:
    logpath = os.path.expanduser(config['LOGS']['LOG_PATH'] + config['LOGS']['LOG_FILENAME'])
    logging.basicConfig(filename=logpath, level=logging.INFO)

CURRENT_PATH = os.getcwd()
HIDDEN_FILE_NAME = config['PATHS']['HIDDEN_FILE_NAME']
HIDDEN_FILE_PATH = config['PATHS']['HIDDEN_FILE_PATH']
PLOTS_PATH = config['PATHS']['PLOTS_DIR']

# -----------------------------------------------
def main_inputs(func):
    """
    This method will be used to decorate main. Its purpose is so that
    it accepts both a single string (for use within BPOD) and a list of 
    strings (for manual report generation) as input.
    """
    def wrapper(path):
        if type(path) is str:
            path = [path]
        func(path)
    return wrapper

def manage_directories(subject_name: str):    
    """ 
    If necessary, it creates the daily_reports file inside the HOME folder 
    and the animal subdir.
    """    
    if not os.path.exists(os.path.expanduser(HIDDEN_FILE_PATH)): 
        os.makedirs(os.path.expanduser(HIDDEN_FILE_PATH))
        logging.info("Daily_report directory not found. Creating it...")
    if not os.path.exists(os.path.expanduser(HIDDEN_FILE_PATH + subject_name)): 
        os.makedirs(os.path.expanduser(HIDDEN_FILE_PATH + subject_name))
        logging.info("Directory for this subject not found. Creating it...")
    os.chdir(os.path.expanduser(HIDDEN_FILE_PATH + subject_name))

def write_json(session_info: dict, subject_name: str) -> list:
    """ 
    Reads the hidden file with all the data, or creates it if it doesn't exist.
    Returns: a list of dicts that contains the data of all past sessions ordered by
    dates.
    """    

    def date_parser(session_list: list, current_session_date: str) -> int:
        """
        This function takes a list of dicts, each representing a saved session, and a 
        date. Returns the index that corresponds to the position of the date
        inside the list. Returns None if the exact same date is found already in the
        session_list.
        """
        dates_list = [session['day'] for session in session_list]
        if current_session_date in dates_list:
            logging.info("This session already exists.")
            return None
        else:
            for i, date in enumerate(dates_list):
                if current_session_date < date:
                    index = i
                    break
            else:
                index = len(dates_list)
        return index 

    file_name = f".{subject_name}_{HIDDEN_FILE_NAME}"
    file_path = Path(file_name)
    if not file_path.exists(): #  if it doesn't exist yet, create it for the first time
        logger.warning("Creating hidden file for the first time.")
        with open(file_name, 'w+') as file:
            multi_session_info = [session_info]
            json.dump(multi_session_info, file, sort_keys=True, indent=4)
    else: #  if it already exists, put the current session in the appropiate place
        with open(file_name, 'r+') as file:
            logger.warning("Existing record found.")
            multi_session_info = json.load(file)
            # Look for the correct index, depending on the session date:
            index = date_parser(multi_session_info, session_info['day'])
            if index is not None:
                file.seek(0)
                # Insert it at the proper place:
                multi_session_info.insert(index, session_info)
                json.dump(multi_session_info, file, sort_keys=True, indent=4)
                file.truncate()

    return multi_session_info

def serialize(inc_dict: dict) -> dict:
    """
    Takes a dict made of non-serializable objects and returns a dict with the
    objects, but serialized so that they can be saved inside the JSON file.
    """
    return {key: list(value) for key, value in inc_dict.items()}

def load_plots(session_data, cumulative_data: list):
    """
    Accesses the plots folder and loads the modules for the plots.
    """
    check = lambda name, start, end: name.startswith(start) and name.endswith(end)

    # Add the reports folder to path:
    sys.path.append(os.path.expanduser(PLOTS_PATH))
    # Look for all the modules inside:
    reports = os.listdir(os.path.expanduser(PLOTS_PATH))
    # Proper reports will start with "report" and end with the .py extension:
    valid_rep = [module.split('.')[0] for module in reports if check(module, "report", ".py")]
    for report in valid_rep:
        module = importlib.import_module(report)
        module.plot(session_data, cumulative_data)

@main_inputs           
def main(csv_paths):
    """
    The logic of the report program. In order: creates a Session object which holds
    the session data; decides which variables will be written in the JSON file
    (for persistence); creates the report directories and switches the cwd there;
    writes the JSON file or reads it; loads the plot scripts inside the PLOTS_PATH 
    folder.
    """
    
    for path in csv_paths:
        try:
            logger.info("Starting reports.")
            session_data = Session(path)

            data_to_save = {'trial_num': len(session_data), 
                           'correct_trials': session_data.performance.corrects_total,
                           'invalid_trials': session_data.performance.invalids_total, 
                           'total_perf': session_data.performance.absolute_total,
                           'L_perf': session_data.performance.absolute_L, 
                           'R_perf': session_data.performance.absolute_R, 
                           'day': f"{session_data.metadata.day}/{ session_data.metadata.time}", 
                           'response_time': session_data.raw_data.response_time, 
                           'stage_number': session_data.metadata.stage_number} 

            if session_data.has_psych_curve:
                # Note: the JSON can't save numpy arrays because they can't be pickled. We have
                # to serialize them (convert them to a native Python type such as lists) first.
                psych_curve_dict = serialize(session_data.psych_curve._asdict())
                data_to_save.update(psych_curve_dict)
                
            manage_directories(session_data.metadata.subject_name)
            cumulative_data = write_json(data_to_save, session_data.metadata.subject_name)
            
            load_plots(session_data, cumulative_data)            

            logger.info("Finished successfully.")

        except Exception as error:
            logger.critical("Finished with error.")
            logger.critical(error)
        finally:
            logger.info("-" * 30)
            os.chdir(CURRENT_PATH)

if __name__ == "__main__": 
    # Manual report generation.
    file_list = []
    for root, _, files in os.walk(config['PATHS']['PATH_TO_CSV']):
        for file in files:
            if file.endswith('.csv'):
                file_list.append(os.path.join(root, file))
    assert file_list, "I couldn't find the CSV files. Exiting ..."
    main(file_list)
