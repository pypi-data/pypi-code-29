from __future__ import absolute_import

from aiotstudio._core.types import mql_result_to_dataframe
from aiotstudio._core.logger import Logger
from aiotstudio._core.client import get_default_client
from aiotstudio._core import services

_client = get_default_client()
log = Logger.get_logger(feature="datasource")


def search(query):
    # type: (dict) -> dict
    return services.restitution_search(_client, query)


def search_df(query):
    # type: (dict) -> pandas.DataFrame
    return mql_result_to_dataframe(search(query))[:100000]


def blob_store_fetch(bucket_name, object_name):
    # type: (str, str) -> object
    return services.blob_store_fetch(_client, bucket_name, object_name)


def blob_store_bucket_names():
    # type: () -> List[str]
    return services.blob_store_bucket_names(_client)
