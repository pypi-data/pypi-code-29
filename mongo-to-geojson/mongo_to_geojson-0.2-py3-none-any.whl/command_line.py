from mongo_to_geojson import mongo_to_geojson
from pymongo import MongoClient
import click
import logging
import os
import json


def check_mongo(mongo_uri, collection):
    '''
    Utility method to verify that mongo_uri actually works and the collection
    exists in the database that the uri connects to
    :param mongo_uri:
    :param collection:
    :return: True if connection to mongo was successful and collection exists, False otherwise
    '''
    try:
        client = MongoClient(mongo_uri)
        db = client.get_database()
        collections = db.list_collection_names()
        client.close()
        return True if collection in collections else False
    except:
        return False


def decode_param(raw_param):
    '''
    Converts json string or file containing json into python dict object
    :param raw_param: raw json string or file containing json
    :return: python dict
    '''
    if os.path.exists(raw_param):
        with open(raw_param,'r') as f:
            raw_param = f.read()
    raw_param = raw_param.replace("'", r"\'")
    return json.loads(raw_param)

def parse_list_param(ctx, param, value):
    if value:
        return value.split(",")
    else:
        return param.default

@click.command()
@click.argument('mongouri')
@click.argument('collection')
@click.argument('outfile')
@click.option('--query', '-q',
              help="Document defining filter to be applied to Mongo collection.  Can be a JSON String or file containing json.  See https://docs.mongodb.com/manual/reference/method/db.collection.find/")
@click.option('--projection', '-p',
              help='Document defining what fields will be returned for a given query.  Can be a JSON String or file containing json.  See https://docs.mongodb.com/manual/reference/method/db.collection.find/#find-projection')
@click.option('--agg_pipeline', '-a',
              help='Mongo aggregation pipeline.  Can be a JSON String or file containing json.  See https://docs.mongodb.com/manual/reference/operator/aggregation-pipeline/')
@click.option('--agg_pipeline_opts', '-o',
              help='Additional aggregation arguments.  Can be a JSON String or file containing json.  See https://docs.mongodb.com/manual/reference/operator/aggregation-pipeline/')
@click.option('--geom_possible_names', '-g', default=[],callback=parse_list_param,
              help="Comma delimited list of document properties to look for standard geojson geometry")
@click.option('--x_possible_names', '-x', default=[],callback=parse_list_param,
              help="Comma delimited list of document properties to look for point geometry longitude value")
@click.option('--y_possible_names', '-y', default=[],callback=parse_list_param,
              help="Comma delimited list of document properties to look for point geometry latitude value")
@click.option('--dont-infer', is_flag=True,
              help="Don't try to infer geometry if one isn't found from geom_possible_names/x_possible_names/y_possible_names")
@click.option('--no_cursor_timeout', is_flag=True,
              help='Prevents mongo cursor from closing automatically after some period of time.  use with caution')
@click.option('--delete_existing', is_flag=True, help='Delete outfile if it already exists')
def main(mongouri, collection, outfile, query, projection, agg_pipeline, agg_pipeline_opts,
         geom_possible_names, x_possible_names, y_possible_names, dont_infer, no_cursor_timeout,
         delete_existing):
    if not os.path.exists(os.path.dirname(outfile)):
        logging.error('invalid directory for output geojson file')
        raise SystemExit

    if os.path.exists(outfile):
        if delete_existing:
            os.remove(outfile)
        else:
            logging.error('outfile already exists.  add --delete_existing_flag to the command to auto delete')
            raise SystemExit

    if not check_mongo(mongouri, collection):
        logging.error('unable to connect to mongo using uri: %s', mongouri)
        raise SystemExit

    if agg_pipeline:
        agg_pipeline = decode_param(agg_pipeline)
        if agg_pipeline_opts:
            agg_pipeline_opts = decode_param(agg_pipeline_opts)
        mongo_to_geojson(mongouri, collection, outfile, pipeline=agg_pipeline, pipeline_opts=agg_pipeline_opts,
                         geometry_possible_fields=geom_possible_names,x_possible_fields=x_possible_names,
                         y_possible_fields=y_possible_names,infer=not dont_infer, no_cursor_timeout=no_cursor_timeout)
    else:
        if query:
            query = decode_param(query)

        if projection:
            projection = decode_param(projection)
        mongo_to_geojson(mongouri, collection, outfile, query=query, projection=projection,
                         geometry_possible_fields=geom_possible_names, x_possible_fields=x_possible_names,
                         y_possible_fields=y_possible_names, infer=not dont_infer, no_cursor_timeout=no_cursor_timeout)


if __name__ == '__main__':
    main()
