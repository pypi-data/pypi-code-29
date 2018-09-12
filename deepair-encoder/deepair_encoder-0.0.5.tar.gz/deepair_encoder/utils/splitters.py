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

"""Splitters : currently  works only for passengertypes"""

from pandas import DataFrame
import pandas as pd
import os


def _getindex(s, search=['ADT', 'CHD', 'INF']):
    '''
        Finds the smallest index of all the elements in search (list)
            present in the s (string).
        inputs:
            s: Parent string to search in (string)
            search: list of sub-strings to search for (list)
        returns:
            index: list of all indices (list)
    '''
    index = []
    for value in search:
        index.append(int(s.find(value)))
    return index


def _getvalue(s, index, length=6):
    '''
        Finds the value for the located field by index.
        inputs:
            s: Parent string to search in (string)
            index: base index of the found field (int)
            length: distance between value and the base (int)
        returns:
            value: value of the field (int)
    '''
    return int(s[index + length])


def type_splitter(data, keys=['passengertypes'], newheadings=[['ADT', 'CHD', 'INF']]):
    '''
        Split the column (need to make it more generic).
        inputs:
            data: dataframe which contain this column (pd dataframe)
            keys: list of column fields to split(list)
            newheadings: list of list for header columns in keys (list)
        returns:
            data: updated dataframe (pandas df)
    '''
    table = []
    merged = 0

    # Each key
    for key in keys:
        # row wise iteration
        for row in data[key]:
            index = _getindex(row)
            val1 = val2 = val3 = 0

            # NOTE: change this logic for generic implementation
            if (index[0] != -1):
                val1 += _getvalue(row, index[0])
            if (index[1] != -1):
                val2 += _getvalue(row, index[1])
            if (index[2] != -1):
                val3 += _getvalue(row, index[2])

            table.append([val1, val2, val3])

        # Converting into DF
        df = DataFrame(table)
        # DF column headers
        df.columns = newheadings[merged]

        # Dropping the field
        data = data.drop([key], axis=1)

        # Concatinating the new (one hot encoded) fields
        data = pd.concat([data, df], axis=1)

        # incrementing merge counter
        merged += 1
    return data


def split_datewise(df, directory='', postfix='', mode='w'):
    '''
        Split a Dataframe according to dates in UTC-Timestamp:

        input :-
            DF          : dataframe which contain this column (pd dataframe)
            directory   : path to the target directory (string)
            postfix     : any postfix you want to add (string)
            mode        : writing mode ('w':writing, 'a': append)
    '''
    df['utctimestamp'] = pd.to_datetime(df['utctimestamp'], format='%Y-%m-%d %H:%M:%S')
    df['just_date'] = df['utctimestamp'].dt.date
    unq = df['just_date'].unique()

    counter = 0
    if not os.path.exists(directory):
        os.makedirs(directory)
    for date in unq:

        counter += 1
        print('converting: %d/%d' % (counter, len(unq)))
        indicator = df['just_date'] == (date)
        selected = df[indicator]

        selected.to_csv(directory + '/' + str(date) + '_' + postfix + '.csv', mode=mode, header=False, index=False)
