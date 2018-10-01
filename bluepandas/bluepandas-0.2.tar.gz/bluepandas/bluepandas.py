"""
Module to access Azure Blob Storage objects in CSV format with Pandas
"""
from __future__ import print_function

from azure.storage.blob import BlockBlobService 

import sys
import os
import re
import pandas as pd

from io import BytesIO, StringIO

class DataFrame(pd.DataFrame):
    def plain_to_csv(self, path_or_buf=None, **kwargs):
        return super(DataFrame, self).to_csv(path_or_buf=path_or_buf, **kwargs)

    def to_csv(self, path_or_buf=None, **kwargs):
        try:
            container, storage_account_name, blob_name = parse_url(path_or_buf)    
        except (URLParsingError, TypeError):
            return self.plain_to_csv(path_or_buf=path_or_buf, **kwargs)
        else:
            conn_string = get_connection_string(storage_account_name)
            blob = BlockBlobService(connection_string=conn_string)

            def progressbar(x, y):
                x = 0 if x is None else x
                y = 0 if y is None else y

                print("{0:0.2f} kB of {1:0.2f} kB downloaded.".format(x / 1024.0, y / 1024.0), end="\r")

            text = self.plain_to_csv(**kwargs)
            
            blob.create_blob_from_text(container,
                                            blob_name,
                                            text,
                                            progress_callback=progressbar
                                        )



class ConnectionStringError(Exception):
    """
    Raised when Azure Storage Connection String is not found
    """
    pass

class URLParsingError(Exception):
    """
    Raised if bluepandas is unable to parse the WASB(S) URL
    """
    pass

def parse_url(az_url):
    """
    Returns the names of the container, the storage account and the blob from
    a WASB(S) url.

    Args:
        az_url (str): WASBS URL

    Returns
        tuple: (container, storage account name, blob name)

    Raises:
        :class:`~bluepandas.bluepandas.URLParsingError`: When the tuple above
            cannot be extracted from the URL.

    """
    url_regex = re.compile("wasbs?://([a-z0-9\\-]*(?=@))@([a-z0-9]*)\\.blob\\.core\\.windows\\.net/([^\\s]+)")

    match = re.match(url_regex, az_url)

    if match is None:
        raise URLParsingError("Please check the URL provided.")
    else:
        return match.groups()



def get_connection_string(storage_account_name):
    """
    Checks the environment for variable named AZ_<STORAGE_ACCOUNT_NAME> and
    returns the corresponding connection string. Raises a 
    ``ConnectionStringNotFound`` exception if environment variable is missing
    """

    conn_string = os.environ.get("AZ_" + storage_account_name.upper(), None)

    if conn_string is None:
        raise ConnectionStringError(
            "Environment variable AZ_" + storage_account_name.upper() + " not found!")
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
        print("{0:0.2f} kB of {1:0.2f} kB downloaded.".format(x / 1024.0, y / 1024.0), end="\r")

    csvstr = blob.get_blob_to_text(container_name,
                                   blob_name,
                                   progress_callback=progressbar
                                   ).content

    df = pd.read_csv(StringIO(csvstr), **kwargs)
    
    return DataFrame(df.values, columns = df.columns)




    







