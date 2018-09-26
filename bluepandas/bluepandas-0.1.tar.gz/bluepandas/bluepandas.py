"""
Module to access Azure Blob Storage objects in CSV format with Pandas
"""
from __future__ import print_function

import sys
import os

if sys.version_info.major == 3:
    from io import StringIO
else:
    from StringIO import StringIO

from azure.storage.blob import BlockBlobService 

import re
import pandas as pd

class ConnectionStringError(Exception):
    """
    Raised when Azure Storage Connection String is not found
    """
    pass

def parse_url(az_url):
    """
    Returns the names of the container, the storage account and the blob from
    a WASB(S) url. 
    """
    url_regex = re.compile("wasbs?://([a-z0-9\\-]*(?=@))@([a-z0-9]*)\\.blob\\.core\\.windows\\.net/(.*)")

    return re.match(url_regex, az_url).groups()

def get_connection_string(storage_account_name):
    """
    Checks the environment for variable named AZ_<STORAGE_ACCOUNT_NAME> and
    returns the corresponding connection string. Raises a 
    ``ConnectionStringNotFound`` exception if environment variable is missing
    """
    
    conn_string = os.environ.get("AZ_"+storage_account_name.upper(), None)

    if conn_string is None:
        raise ConnectionStringError("Environment variable AZ_"+storage_account_name.upper()+" not found!")
    else:
        return conn_string

def read_csv(az_url, **kwargs):
    """
    Returns the CSV file in Azure Blob Storage as a pandas dataframe
    """

    container_name, storage_account_name, blob_name = parse_url(az_url)
    conn_string = get_connection_string(storage_account_name)
    blob = BlockBlobService(connection_string=conn_string)

    def progressbar(x, y):
        print("{0:0.2f} kB of {1:0.2f} kB downloaded.".format(x/1024.0,y/1024.0), end="\r")

    csvstr = blob.get_blob_to_text( 
                        container_name,
                        blob_name,
                        progress_callback=progressbar
                        ).content

    return pd.read_csv(StringIO(csvstr), **kwargs)

    







