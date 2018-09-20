import pandas as pd
import numpy as np
import os
#import io
import sys

import json

def __datasource_getinfo(localpath):
    """
    Private method (CSV supported)
    TODO: excel, ...
    Requires pip install python-magic
    Return fileinfo and holdout subset (dataframe)
    """
    #mimetype = magic.from_file(localpath, mime=True)

    template = {
        'columns': []
    }

    try:
        data = pd.read_csv(localpath, index_col=0) # header = None
        template['size'] = 1./1024*os.stat(localpath).st_size # size in kB
        template['filetype'] = 'csv'
        template['num_columns'] = data.shape[1]
        print('data shape', data.shape)

    except:
        print('File format not recognized (Try with csv, excel, txt)')
        return False, False

    # Collect stats of original data
    for idx, name in enumerate(data.columns):
        template['columns'].append(extract_field(idx, name, extract_field_type(data[name]), len(set(data[name]))))

    # Prepare holdout set
    # TODO let's get rid of this with container authentication and verification
    # at data provider side
    holdout_set = data.sample(frac=0.1, replace=False)

    return holdout_set, template


def extract_field(sequence, name, type, unique_values):
    return {
        'name': name,
        'type': type,
        'sequence': sequence,
        'unique_values': unique_values
    }


def extract_field_type(data):
    type = data.dtype

    if type == np.bool_: return "boolean"
    elif type == np.float16 or type == np.float32 or type == np.float64 or type == np.float128: return "decimal"
    elif type == np.int8 or type == np.int16 or type == np.int32 or type == np.int64: return "integer"
    elif type == np.complex64 or type == np.complex128 or type == np.complex256: return "complex"
    else: return "string"


def extract(sourcepath):
    """
    Post file at localpath (raw data) or file at remotepath (S3 supported)
    """
    # Prepare holdout set and send
    holdout_set, info = __datasource_getinfo(sourcepath)

    if holdout_set is not None and info:
        print('[AMX HOLDOUT START]')
        holdout_set.to_csv(sys.stdout)
        print('[AMX HOLDOUT END]')

        print('[AMX INFO START]')
        print(json.dumps(info, ensure_ascii=False))
        print('[AMX INFO END]')

extract(sys.argv[1])
