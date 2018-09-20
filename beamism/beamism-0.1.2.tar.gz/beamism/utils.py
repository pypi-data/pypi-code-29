# -*- coding: utf-8 -*-


import json
import jsonschema
import copy
from pymongo import MongoClient


def save_to_mongo(mongo_uri, db_name, collection_name, data, ssl=True):
    # copy data since coll.insert_one function will generate new object in the data, and cannot serialize it
    cp_data = copy.copy(data)
    client = MongoClient(mongo_uri, ssl=ssl)
    db = client[db_name]
    coll = db[collection_name]
    insert_result = coll.insert_one(cp_data)
    return insert_result.acknowledged


def parse_json_message(json_as_str):
    try:
        input_json = json.loads(json_as_str)
        return input_json
    except:
        return None


def validate_json_based_on_schema(input_json, schema):
    try:
        jsonschema.validate(input_json, schema)
        return None
    except jsonschema.ValidationError as validation_error:
        return validation_error


def pubsub_packing(json_datas):
    '''
    How to Pack:
        convert msgs as list(json) => msgs as list[str(json style)]
    Note:
        When return string as message, pubsub treat it as list of chars. But, in many cases, we do not want such behaviour.
    '''
    if type(json_datas) != list:
        json_datas = [json_datas]
    return [json.dumps(json_data) for json_data in json_datas]


def merge_jsons(params_json, result_json):
    """
    Merge two jsons: the first one should be the parameters for the job, and the other should be the results of the job
    """
    # make sure keys not change
    if set(params_json.keys()).intersection(result_json.keys()):
        err_msg = "[BUG] When merge two jsons, some keys are modified"
        print(err_msg)

    merged_json = copy.copy(result_json)
    merged_json.update(params_json)
    return merged_json