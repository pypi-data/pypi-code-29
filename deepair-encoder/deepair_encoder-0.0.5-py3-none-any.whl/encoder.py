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

"""encoder process"""


import pandas as pd
import numpy as np
import datetime
import time

from tqdm import tqdm
from deepair_encoder.utils.logger import _log_with_timestamp as log
from deepair_encoder.utils.encoder_tools import one_hot_encoder


def encode_username(df, drop_field=True):
    '''
        Username one-hot encoder.
        inputs:
            df: Dataframe which have username column (pandas df series)
            drop_field: a flag if the usename column should be dropped or not after encoding (bool)
        return:
            df: Dataframe which have only username indicator [0/1] (pandas df series)
    '''
    df.loc[df.username != 'default', 'username_flag'] = 1
    df.loc[df.username == 'default', 'username_flag'] = 0
    if drop_field:
        df = df.drop(columns='username')
    return df


def encode_discounts(df, drop_field=True):
    '''
        Discounts encoder.
        inputs:
            df: dataframe which has discounts column (pandas df series)
            drop_field: a flag if the discounts column should be dropped or not after encoding (bool)
        return:
            df: a dataframe with 3 new columns 'PROMOCODE', 'RES', 'LFG' and discounts droped if drop_field = True
    '''

    df['discounts'] = df['discounts'].apply(lambda x: str(x).upper())
    # Encode PROMOCODE
    df['promo_flag'] = 0
    df.loc[df['discounts'].str.contains('PROMOCODE'), 'promo_flag'] = 1

    # Encode RESIDENT FLAG
    df['resident_flag'] = 0
    df.loc[df['discounts'].str.contains(': RES'), 'resident_flag'] = 1

    # Encode LFG FLAG
    df['lfg_flag'] = 0
    df.loc[df['discounts'].str.contains('LFG'), 'lfg_flag'] = 1

    if drop_field:
        df = df.drop(columns='discounts')

    return df


def encode_bagprice(df):
    '''
        bag price encoder.
        inputs:
            field: Dataframe which have bag_price column (pandas df series)
        return:
            field: Dataframe with a score for bagprice  (pandas df series)
    '''
    '''
    #create a temporary dataframe with fields of interest
    temp = df[['requestid', 'direction','bag_price']]

    #min / max total price for whole requestid direction
    temp1 = temp.groupby(by = ['requestid', 'direction'], as_index = False).agg({'bag_price' : ['min', 'max']})
    temp1.columns = ['requestid', 'direction', 'bag_price_min', 'bag_price_max']

    #merge the temp dataframes
    temp = pd.merge(temp, temp1, on = ['requestid', 'direction'])


    # Small number to avoid NAN
    epsilon = 1e-8

    #calculate scores
    temp['bag_price_score'] = (temp['bag_price_max'] - temp['bag_price'])/(temp['bag_price_max'] - temp['bag_price_min'] + epsilon)

    #drop redundent columns
    temp = temp.drop(columns = ['bag_price','bag_price_max', 'bag_price_min'])

    #merge to master df before returning
    df = pd.merge(df, temp,
                 on = ['requestid', 'direction'])
    '''

    return df


def minmax_score(df, fields, keyval=['requestid', 'direction_onward'], drop_field=True, verbose=True):
    '''
        scorer function to normalize from 0-1 inversely to the value.
        inputs:
            df: Dataframe which contains fields (pandas df series)
            fields: Dataframe columns on which the score is calculated (list)
            keyval: Group the data by this key values (list)
            drop_field: Indicator to replace fields by normalized new fields (bool)
            verbose: Progress bar indicator (bool)
        return:
            field: Dataframe with a score for totalprice relative to whole requestid-direction, by index, by faregroup  (pandas df series)
    '''

    # Each field iteration
    for field in tqdm(iterable=fields,
                      total=len(fields),
                      desc='minmax score',
                      disable=not verbose):

        # Small number to avoid NAN
        epsilon = 1e-8

        def minmax_norm(x): return (x.max() - x) / (x.max() - x.min() + epsilon)

        if drop_field:
            df[field] = df.groupby(keyval)[field].transform(minmax_norm)
        else:
            df[str(field) + str('_score')] = df.groupby(keyval)[field].transform(minmax_norm)

    return df


def minmax_normalize(df, fields, keyval=['requestid', 'direction_onward'], drop_field=True, verbose=True):
    '''
        normalizer function to normalize from 0-1 proportional to the value.
        inputs:
            df: Dataframe which contains fields (pandas df series)
            fields: Dataframe columns on which the score is calculated (list)
            keyval: Group the data by this key values (list)
            drop_field: Indicator to replace fields by normalized new fields (bool)
            verbose: Progress bar indicator (bool)
        return:
            field: Dataframe with a score for totalprice relative to whole requestid-direction, by index, by faregroup  (pandas df series)
    '''

    # Each field iteration
    for field in tqdm(iterable=fields,
                      total=len(fields),
                      desc='minmax normalize',
                      disable=not verbose):

        # Small number to avoid NAN
        epsilon = 1e-8

        def minmax_norm(x): return (x - x.min()) / (x.max() - x.min() + epsilon)

        if drop_field:
            df[field] = df.groupby(keyval)[field].transform(minmax_norm)
        else:
            df[str(field) + str('_normalized')] = df.groupby(keyval)[field].transform(minmax_norm)

    return df


def encode_totalprice(df):
    '''
        total price encoder.
        inputs:
            df: Dataframe which have totalprice and totaltaxes column (pandas df series)
        return:
            df: Dataframe with a score for totalprice relative to whole requestid-direction, by index, by faregroup  (pandas df series)
    '''

    # Calculate totalprice
    df['totalprice'] = df['totalprice'] + df['totaltaxes']
    df = df.drop(columns='totaltaxes')

    # create a temporary dataframe with fields of interest
    temp = df[['requestid', 'direction', 'index', 'faregroup', 'totalprice']]

    # min / max total price for whole requestid direction
    temp1 = temp.groupby(by=['requestid', 'direction'], as_index=False).agg({'totalprice': ['min', 'max']})
    temp1.columns = ['requestid', 'direction', 'totalprice_min', 'totalprice_max']

    # min / max total price for whole requestid-direction-index (across all faregroups)
    temp2 = temp.groupby(by=['requestid', 'direction', 'index'], as_index=False).agg({'totalprice': ['min', 'max']})
    temp2.columns = ['requestid', 'direction', 'index', 'totalprice_index_min', 'totalprice_index_max']

    # min / max total price for whole requestid-direction-faregroup (across all indices)
    temp3 = temp.groupby(by=['requestid', 'direction', 'faregroup'], as_index=False).agg({'totalprice': ['min', 'max']})
    temp3.columns = ['requestid', 'direction', 'faregroup', 'totalprice_faregroup_min', 'totalprice_faregroup_max']

    # merge the temp dataframes
    temp = pd.merge(temp, temp1, on=['requestid', 'direction'])
    temp = pd.merge(temp, temp2, on=['requestid', 'direction', 'index'])
    temp = pd.merge(temp, temp3, on=['requestid', 'direction', 'faregroup'])

    # Small number to avoid NAN
    epsilon = 1e-8

    # calculate scores
    temp['totalprice_score'] = (temp['totalprice_max'] - temp['totalprice']) / (temp['totalprice_max'] - temp['totalprice_min'] + epsilon)
    temp['totalprice_index_score'] = (temp['totalprice_index_max'] - temp['totalprice']) / (temp['totalprice_index_max'] - temp['totalprice_index_min'] + epsilon)
    temp['totalprice_faregroup_score'] = (temp['totalprice_faregroup_max'] - temp['totalprice']) / (temp['totalprice_faregroup_max'] - temp['totalprice_faregroup_min'] + epsilon)

    # drop redundent columns
    temp = temp.drop(columns=['totalprice', 'totalprice_max', 'totalprice_min',
                              'totalprice_index_max', 'totalprice_index_min',
                              'totalprice_faregroup_max', 'totalprice_faregroup_min'])

    # merge to master df before returning
    df = pd.merge(df, temp,
                  on=['requestid', 'direction', 'index', 'faregroup'])

    return df


def encode_bookingid(df):
    '''
        Bookingid flag one-hot encoder.
        inputs:
            df: Dataframe which have Bookingid column (pandas df series)
        return:
            df: Dataframe which have only Bookingid indicator [0/1] (pandas df series)
    '''
    indx = df['bookingid'].isna()
    df.loc[indx, 'bookingid'] = 0
    df.loc[~indx, 'bookingid'] = 1
    return df


def encode_faregroup(raw_file, df, verbose=False):
    '''
        Faregroup encoder.
        inputs:
            raw_file: raw_file location where the faregroup_definition is available
            df: Dataframe which have faregroup column (pandas df series)
            verbose: Optional, if more detailed log is needed
        return:
            field: Dataframe with extra fields with faregroup attributes [-1/0/1] (pandas df series)
            Note: -1 = not available, 0 = available for a fee, 1 = available for free (at no charge)
    '''
    if verbose:
        log('encoding faregroup on df with shape: ' + str(df.shape))

    # TODO: check if file is available

    # read faregroup definition and transpose
    fare_group = pd.read_csv(raw_file)
    fare_group = fare_group.transpose()
    fare_group.columns = fare_group.iloc[0]
    fare_group = fare_group[1:]
    fare_group = fare_group.reset_index()
    fare_group = fare_group.rename(columns={'index': 'faregroup'})
    if verbose:
        log('faregroup definition read : ' + str(fare_group.shape))

    # decorate df with faregroup attributes
    df = pd.merge(df, fare_group, on='faregroup', how='left')
    if verbose:
        log('shape of df after faregroup encoding : ' + str(df.shape))

    return df


def encode_datetime(df, field, verbose=False):
    '''
        Datetime encoder.
        inputs:
            df: Dataframe which have 'field' column (pandas df series)
            field: the field that has to be encoded
        return:
            df: Dataframe with 6 ecoded values capturing TOD, DOW and WOY
    '''
    if verbose:
        log('datetime encoding started for ' + field + '...')
        log('input dataframe shape: ' + str(df.shape))

    df[field] = pd.to_datetime(df[field], format='%Y-%m-%d %H:%M:%S')

    # TIME(HOUR) OF DAY ENCODER
    hours_in_day = 24
    df[field + '_sin_tod'] = np.sin(2 * np.pi * df[field].dt.hour / hours_in_day)
    df[field + '_cos_tod'] = np.cos(2 * np.pi * df[field].dt.hour / hours_in_day)

    # DAY OF WEEK ENCODER
    days_in_week = 7
    df[field + '_sin_dow'] = np.sin(2 * np.pi * df[field].dt.weekday / days_in_week)
    df[field + '_cos_dow'] = np.cos(2 * np.pi * df[field].dt.weekday / days_in_week)

    # WEEK OF YEAR ENCODER
    weeks_in_year = 52
    df[field + '_sin_woy'] = np.sin(2 * np.pi * df[field].dt.week / weeks_in_year)
    df[field + '_cos_woy'] = np.cos(2 * np.pi * df[field].dt.week / weeks_in_year)

    if verbose:
        log('input dataframe shape after encoding: ' + str(df.shape))
        log('datetime encoding done for ' + field + '...')

    return df


def encode_advanced_purchase(df, dptr_field='departuredate', sales_field='utctimestamp'):
    '''
        advanced purchase encoder.
        inputs:
            df: Dataframe which have dptr_field and sales_field column (pandas df series)
        return:
            df: Dataframe advanced purchase column
    '''
    df[dptr_field] = pd.to_datetime(df[dptr_field], format='%Y-%m-%d %H:%M:%S')
    df[sales_field] = pd.to_datetime(df[sales_field], format='%Y-%m-%d %H:%M:%S')
    df['advanced_purchase'] = ((df[dptr_field] - df[sales_field]).dt.days) / 365

    return df


def encode_los(df, verbose=False):
    '''
        los and trip_type encoder.
        inputs:
            df: Dataframe which have departuredate, requestid and direction column (pandas df series)
        return:
            df: Dataframe los and trip_type encodes column
    '''
    # departure dates
    df['ddate'] = df['departuredate'].dt.date
    df['ddate'] = pd.to_datetime(df['ddate'], format='%Y-%m-%d')

    # split into onward and return
    los = df[['requestid', 'direction', 'ddate']].drop_duplicates()
    los_onward = los[los['direction'] == 'onward']
    los_return = los[los['direction'] == 'return']
    if verbose:
        log('unique keys identified : ' + str(los.shape))
        log('onward keys identified : ' + str(los_onward.shape))
        log('return keys identified : ' + str(los_return.shape))

    # create unqiue set
    los = pd.merge(los_onward.drop(columns='direction'),
                   los_return.drop(columns='direction'),
                   on='requestid',
                   how='outer',
                   suffixes=['_onward', '_return'])
    if verbose:
        log('unique keys identified : ' + str(los.shape))

    # Assign Trip Type
    los['trip_type'] = 'roundtrip'
    los.loc[los['ddate_return'].isna(), 'trip_type'] = 'oneway'

    # Calculate Length of Stay
    los['los_days'] = 0
    los.loc[los['trip_type'] == 'roundtrip', 'los_days'] = ((los['ddate_return'] - los['ddate_onward']).dt.days) / 30

    # One-Hot Encode Trip_Type
    los = one_hot_encoder(los, ['trip_type'], fields_drop=True)

    # Merge keys and data with master
    df = pd.merge(df, los,
                  on='requestid',
                  how='left')

    # Drop some unneccesary columns
    df = df.drop(columns=['ddate', 'ddate_onward', 'ddate_return'])

    if verbose:
        log('LOS and TripType Fields added : ' + str(df.shape))

    return df


def encode_airports(df, fields, reference_file_path, verbose=True):
    '''
        encode the airports.
        inputs:
            df                      : Dataframe which have airports (pandas df series)
            fields                  : list of fields that you want to run this
                                        function on (list)
            reference_file_path     : path to the codes file (string)
            verbose                 : Indicator for progress bar (bool)
        return:
            df: Dataframe encoded with airports values
    '''
    # Airport to index mapping
    codes = pd.read_csv(reference_file_path)
    codes = codes[['airport_code']]
    d = codes.to_dict()
    code_dict = dict((v, k) for k, v in d['airport_code'].items())

    # Mapping
    try:
        for field in tqdm(iterable=fields,
                          total=len(fields),
                          desc='encoding airports',
                          disable=not verbose):
            df[field].replace(code_dict, inplace=True)
        return df
    except:
        print('Error : returning dataframe as it is. check df once again.')
        return df


def encode_city(df, fields, reference_file_path, verbose=True):
    '''
        encode the airports.
        inputs:
            df                      : Dataframe which have city (pandas df series)
            fields                  : list of fields that you want to run this
                                        function on (list)
            reference_file_path     : path to the codes file (string)
            verbose                 : Indicator for progress bar (bool)
        return:
            df: Dataframe encoded with airports values
    '''
    # City to index mapping
    codes = pd.read_csv(reference_file_path)
    codes = codes[['city_code']]
    codes = codes['city_code'].drop_duplicates()
    d = codes.to_dict()
    code_dict = dict((v, k) for k, v in d.items())

    # Mapping
    try:
        for field in tqdm(iterable=fields,
                          total=len(fields),
                          desc='encoding cities',
                          disable=not verbose):
            df[field].replace(code_dict, inplace=True)
        return df
    except:
        print('Error : returning dataframe as it is. check df once again.')
        return df
