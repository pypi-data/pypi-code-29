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

"""Encoders"""

from numpy import array
from numpy import argmax
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import OneHotEncoder
from pandas import DataFrame

import numpy
import pandas as pd
from tqdm import tqdm


def intersection(lst1, lst2):
    return list(set(lst1) - set(lst2))


def one_hot_encoder(df, fields, fields_drop=True, verbose=True, classes=None):
    '''
        Converts the fields into one hot encoding.
        inputs:
            df: Dataframe containing all those fields (pandas df)
            fields: Dataframe columns that you want to convert to one hot (string)
            verbose: Indicator for progress bar (bool)
            classes: Dictionary for the desired columns (dict)
        return:
            df: updated dataframe (pandas df)
    '''
    # reindexing the dataframe
    df = df.reset_index(drop=True)

    # Each field iteration
    for field in tqdm(iterable=fields,
                      total=len(fields),
                      desc='one_hot',
                      disable=not verbose):

        # Encoding
        label_encoder = LabelEncoder()
        integer_encoded = label_encoder.fit_transform(df[field])
        onehot_encoder = OneHotEncoder(sparse=False)
        integer_encoded = integer_encoded.reshape(len(integer_encoded), 1)
        onehot_encoded = onehot_encoder.fit_transform(integer_encoded)

        # Converting into DF
        table = DataFrame(data=onehot_encoded)
        # DF column headers
        table.columns = [field + '_' + x for x in label_encoder.inverse_transform(numpy.arange(onehot_encoded.shape[1]))]

        if classes is not None:
            skipped_fields = intersection(classes[field], table.columns.tolist())
            if len(skipped_fields):
                for skipped_field in skipped_fields:
                    table[skipped_field] = 0

            table = table[classes[field]]

        if fields_drop:
            # Dropping the field
            df = df.drop([field], axis=1)

        # Concatinating the new (one hot encoded) fields
        df = pd.concat([df, table], axis=1)
    return df


def integer_encoder(df, fields, verbose=True):
    '''
        Converts the fields into integer encoding.
        inputs:
            df: Dataframe containing all those fields (pandas df)
            fields: Dataframe columns that you want to convert to one hot (string)
            verbose: Indicator for progress bar (bool)
        returns:
            df: updated dataframe (pandas df)
    '''
    # reindexing the dataframe
    df = df.reset_index(drop=True)

    # Each field iteration
    for field in tqdm(iterable=fields,
                      total=len(fields),
                      desc='integer',
                      disable=not verbose):

        # Encoding
        label_encoder = LabelEncoder()
        integer_encoded = label_encoder.fit_transform(df[field])

        # Converting into DF
        table = DataFrame(data=integer_encoded[:])
        # DF column headers
        table.columns = [field]

        # Dropping the field
        df = df.drop([field], axis=1)
        # Concatinating the new (integer encoded) fields
        df = pd.concat([df, table], axis=1)

    return df


def get_wom(field):
    '''
        Function for week of the month.
        inputs:
            field: Dataframe column which have timestamp (pandas df series)
        return:
            field: Dataframe column which have wom (pandas df series)
    '''
    # Converting into datetime format
    f = pd.to_datetime(field, format='%Y-%m-%d %H:%M:%S')
    return f.dt.weekday


def get_dow(field):
    '''
        Function for day of the week.
        inputs:
            field: Dataframe column which have timestamp (pandas df series)
        return:
            field: Dataframe column which have dow (pandas df series)
    '''
    # Converting into datetime format
    f = pd.to_datetime(field, format='%Y-%m-%d %H:%M:%S')
    return f.apply(lambda d: (d.day - 1) // 7 + 1)


def get_month(field):
    '''
        Function for month.
        inputs:
            field: Dataframe column which have timestamp (pandas df series)
        return:
            field: Dataframe column which have only month (pandas df series)
    '''
    # Converting into datetime format
    f = pd.to_datetime(field, format='%Y-%m-%d %H:%M:%S')
    return f.dt.month


def get_year(field):
    '''
        Function for year.
        inputs:
            field: Dataframe column which have timestamp (pandas df series)
        return:
            field: Dataframe column which have only year (pandas df series)
    '''
    # Converting into datetime format
    f = pd.to_datetime(field, format='%Y-%m-%d %H:%M:%S')
    return f.dt.year


def obj2num(df, fields, verbose=True):
    '''
        Converts the fields into numeric from obj data type.
        inputs:
            df: Dataframe containing all those fields (pandas df)
            fields: Dataframe columns that you want to convert to numeric (string)
            verbose: Indicator for progress bar (bool)
        returns:
            df: updated dataframe (pandas df)
    '''

    for field in tqdm(iterable=fields,
                      total=len(fields),
                      desc='obj2num',
                      disable=not verbose):
        df[field] = pd.to_numeric(df[field])

    return df
