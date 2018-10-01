# Copyright 2018 Deep Air. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS-IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""loader -tools"""

import time
import datetime
import numpy as np
import pandas as pd
from tqdm import tqdm
from datetime import timedelta, date
from abc import ABCMeta, abstractmethod


def _daterange(s_date, e_date):
    for n in range(int((e_date - s_date).days)):
        yield s_date + timedelta(n)


def log(message):
    '''
        prints message on console
        input :
            message     : msg to print (string)
    '''
    print('[' + datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S') + ']:'
          + message)


class Handler(object):
    __metaclass__ = ABCMeta

    def __init__(self, verbose=True):
        '''
            Handlder (class) constructor.
            inputs:
                verbose: Indicator for log and progress bar (bool)
        '''

        self.test_size = None
        self.features = None
        self.verbose = verbose

    def get_data(self, path):
        '''
            Singe file loader from exact path.
            inputs:
                path: Excat path to load the dataframe (string)
            return:
                df: Dataframe loaded [empty in case of non existance] (pandas df series)
                indicator: load success indicator (bool)
        '''

        try:
            df = pd.read_csv(path)
            return df, True
        except:
            log('error: No file name ' + path)
            return pd.DataFrame(), False

    @abstractmethod
    def _load_action(self, df):
        '''
            @abstractmethod
            User defined Bottle neck pipeline within load.
            NOTE -> Default job of this function is pass i.e. do nothing
            inputs:
                df:  Dataframe to apply this method on (pandas df)
            return:
                df:  Modified dataframe (pandas df)
        '''
        return df

    def loader(self, dir_path, start_date, end_date,
               prefix='', postfix='', ext='.csv'):
        '''
            Primary loader function to load the data from start date to
            end date in concatinated (single dataframe) format.
            inputs:
                dir_path    : absolute path to the directory path (series)
                start_date  : load start date in dd-mm-yyyy format (string)
                end_date    : load end date in dd-mm-yyyy format (string)
                prefix      : file prefix [if necessary] (string)
                postfix     : file postfix [if necessary] (string)
                ext         : file extension [default is .csv] (string)
            return:
                df:  loaded concatenated dataframe (pandas df)
        '''

        # init data
        data = pd.DataFrame()

        # LOADING DATES INFORMATION
        str_date = start_date.split('-')
        start_date = date(int(str_date[2]), int(str_date[1]), int(str_date[0]))

        str_date = end_date.split('-')
        end_date = date(int(str_date[2]), int(str_date[1]), int(str_date[0]))

        # LOADER LOOP
        for single_date in tqdm(iterable=_daterange(start_date, end_date),
                                total=int(((end_date) - (start_date)).days),
                                desc='Loading Files',
                                disable=not self.verbose):

            # Paths and simgle load
            date_str = single_date.strftime("%Y-%m-%d")
            load_data_file = dir_path + prefix + date_str + postfix + ext
            df_read, load_indicator = self.get_data(load_data_file)

            # User defined bottle neck pipeline (default is pass)
            df_read = self._load_action(df_read)

            # Concatinating
            data = pd.concat([data, df_read], ignore_index=True)

        return data

    def single_file_loader(self, dir_path, start_date, end_date,
                           prefix='', postfix='', ext='.csv'):
        '''
            Single loader function to load the data from start date to
            end date in individual datewise (each dataframe is of one date)
            format.
            inputs:
                dir_path    : absolute path to the directory path (series)
                start_date  : load start date in dd-mm-yyyy format (string)
                end_date    : load end date in dd-mm-yyyy format (string)
                prefix      : file prefix [if necessary] (string)
                postfix     : file postfix [if necessary] (string)
                ext         : file extension [default is .csv] (string)
            return:
                data:  list of data frames datewise (list)
        '''

        # init data
        data = []

        # LOADING DATES INFORMATION
        str_date = start_date.split('-')
        start_date = date(int(str_date[2]), int(str_date[1]), int(str_date[0]))

        str_date = end_date.split('-')
        end_date = date(int(str_date[2]), int(str_date[1]), int(str_date[0]))

        for single_date in tqdm(iterable=_daterange(start_date, end_date),
                                total=int(((end_date) - (start_date)).days),
                                desc='Loading Files (Single)',
                                disable=not self.verbose):

            # Paths
            date_str = single_date.strftime("%Y-%m-%d")

            load_data_file = dir_path + prefix + date_str + postfix + ext

            df_read, load_indicator = self.get_data(load_data_file)

            df_read = self._load_action(df_read)

            # Appending list
            data.append(df_read)

        return data

    def single_loader(self, dir_path, start_date, end_date,
                      prefix='', postfix='', ext='.csv'):
        '''
            Single loader function to load the data from start date to
            end date in individual datewise (each dataframe is of one date)
            format.
            inputs:
                dir_path    : absolute path to the directory path (series)
                start_date  : load start date in dd-mm-yyyy format (string)
                end_date    : load end date in dd-mm-yyyy format (string)
                prefix      : file prefix [if necessary] (string)
                postfix     : file postfix [if necessary] (string)
                ext         : file extension [default is .csv] (string)
            return:
                data:  list of data frames datewise (list)
        '''

        # init data
        data = []

        # LOADING DATES INFORMATION
        str_date = start_date.split('-')
        start_date = date(int(str_date[2]), int(str_date[1]), int(str_date[0]))

        str_date = end_date.split('-')
        end_date = date(int(str_date[2]), int(str_date[1]), int(str_date[0]))

        for single_date in tqdm(iterable=_daterange(start_date, end_date),
                                total=int(((end_date) - (start_date)).days),
                                desc='Loading Files (Single)',
                                disable=not self.verbose):

            # Paths
            date_str = single_date.strftime("%Y-%m-%d")

            load_data_file = dir_path + prefix + date_str + postfix + ext

            df_read, load_indicator = self.get_data(load_data_file)

            df_read = self._load_action(df_read)

            # Appending list
            data.append(df_read)

        return data

    def batch_loader(self, dir_path, start_date, end_date,
                     batch_size=1, prefix='', postfix='', ext='.csv'):
        '''
            Batch loader function to load the data from start date to
            end date in batches (each dataframe is in the form of batch datewise)
            format.
            inputs:
                dir_path    : absolute path to the directory path (series)
                start_date  : load start date in dd-mm-yyyy format (string)
                end_date    : load end date in dd-mm-yyyy format (string)
                batch_size  : batch size (int)
                prefix      : file prefix [if necessary] (string)
                postfix     : file postfix [if necessary] (string)
                ext         : file extension [default is .csv] (string)
            return:
                data:  list of data frames datewise (list)
        '''

        # init data
        counter = 0
        data_batch = []
        data = pd.DataFrame()

        # LOADING DATES INFORMATION
        str_date = start_date.split('-')
        start_date = date(int(str_date[2]), int(str_date[1]), int(str_date[0]))

        str_date = end_date.split('-')
        end_date = date(int(str_date[2]), int(str_date[1]), int(str_date[0]))

        for single_date in tqdm(iterable=_daterange(start_date, end_date),
                                total=int(((end_date) - (start_date)).days),
                                desc='Loading Files (Batch)',
                                disable=not self.verbose):

            # Paths
            date_str = single_date.strftime("%Y-%m-%d")

            load_data_file = dir_path + prefix + date_str + postfix + ext

            df_read, load_indicator = self.get_data(load_data_file)

            df_read = self._load_action(df_read)

            # Concatinating
            data = pd.concat([data, df_read], ignore_index=True)
            counter += 1

            if counter == batch_size:
                counter = 0
                # Appending list
                data_batch.append(data)

        if counter:
            # Appending last data to list
            data_batch.append(data)

        return data_batch
