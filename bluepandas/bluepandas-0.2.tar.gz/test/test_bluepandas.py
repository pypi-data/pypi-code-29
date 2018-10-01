# -*- coding: utf-8 -*-

from __future__ import unicode_literals
from __future__ import absolute_import

import pandas as pd

from os import path, environ
import pytest

import bluepandas

from test.secrets import secret_conn_string

test_assets_path = path.abspath(path.join(path.dirname(__file__), "data"))

my_urls = [
    "wasb://test-container@bluepandas.blob.core.windows.net/banklist.csv",
    "wasbs://test-container@bluepandas.blob.core.windows.net/banklist.csv",
    "wasbs://test-container@bluepandas.blob.core.windows.net/dir/long/CrAzyT3xt%&¤&.csv",    
    "wasbs://test-container@greenpandas.blob.core.windows.net/banklist.csv",
    "wasbs://test-container@bluepandas.blob.core.windows.net/Monthly-train.csv",
    "wasb://test-container@bluepandas.blob.core.windows.net/ ",
    "wasbs://test-container@bluepandas.blob.core.windows.net/",
    "wasbs://test-container@bluepandas.blob.core.windows.net/banklist_written.csv"
    ]

account_conn_string = "DefaultEndpointsProtocol=https;AccountName=bluepandas;AccountKey=xxxx;EndpointSuffix=core.windows.net"
sas_conn_string = "BlobEndpoint=https://bluepandas.blob.core.windows.net/;QueueEndpoint=https://bluepandas.queue.core.windows.net/;FileEndpoint=https://bluepandas.file.core.windows.net/;TableEndpoint=https://bluepandas.table.core.windows.net/;SharedAccessSignature=xxxx"


def test_parse_urls():
    assert bluepandas.parse_url(my_urls[0]) == ("test-container", "bluepandas",
                                                "banklist.csv")

    assert bluepandas.parse_url(my_urls[1]) == ("test-container", "bluepandas",
                                                "banklist.csv")

    assert bluepandas.parse_url(my_urls[2]) == ("test-container", "bluepandas",
                                                "dir/long/CrAzyT3xt%&¤&.csv")
    with pytest.raises(bluepandas.URLParsingError):
        bluepandas.parse_url(my_urls[5])
        bluepandas.parse_url(my_urls[6])
    
def test_get_connection_string():
    with pytest.raises(bluepandas.ConnectionStringError):
        environ.pop("AZ_GREENPANDAS", None)  # In case environment contains this 
        bluepandas.get_connection_string("greenpandas")
    
    environ["AZ_BLUEPANDAS"] = account_conn_string
    conn_string = bluepandas.get_connection_string("bluepandas")
    keys1 = [m.split("=")[0] for m in conn_string.split(";")]

    environ["AZ_BLUEPANDAS"] = sas_conn_string
    conn_string = bluepandas.get_connection_string("bluepandas")
    keys2 = [m.split("=")[0] for m in conn_string.split(";")]

    assert ("AccountKey" in keys1) or ("SharedAccessSignature" in keys2) 


def test_read_csv():
    environ["AZ_BLUEPANDAS"] = secret_conn_string

    df_reference = pd.read_csv(path.join(test_assets_path, "banklist.csv"))
    df_reference = bluepandas.DataFrame(df_reference.values,
                                        columns=df_reference.columns)

    df_test = bluepandas.read_csv(my_urls[1])

    assert df_reference.equals(df_test)


def test_write_csv():
    df = bluepandas.DataFrame([(1,2), (3,4)], columns = ['A', 'B'])
    assert df.to_csv() == ",A,B\n0,1,2\n1,3,4\n"
    assert df.to_csv(index=False) == "A,B\n1,2\n3,4\n"
    
    df.to_csv(my_urls[7], index=False)
    df_test = bluepandas.read_csv(my_urls[7])
    assert df.equals(df_test)
    
    