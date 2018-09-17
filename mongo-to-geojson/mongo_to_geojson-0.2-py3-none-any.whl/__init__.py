import json
import numbers
from bson import ObjectId
from datetime import datetime
from pymongo import MongoClient


class JSONEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, ObjectId):
            return str(o)
        if isinstance(o, datetime):
            return o.timestamp()
        return json.JSONEncoder.default(self, o)


def _get_numeric_val(d, property):
    '''
    Attempts to extract a dict value as a number, regardless of its native type
    :param d: dict object
    :param property: property containing numeric value of interest
    :return: a numeric value if successful, None otherwise
    '''
    val = d.get(property)
    if val and isinstance(val, numbers.Number):
        return val
    try:
        return float(str(val))
    except:
        return None


def _find_geojson_geometry(d, possible_names, infer):
    '''
    Attempts to extract a geojson geometry object from a dict object
    :param d: dict object
    :param possible_names: dict keys to search for geometry object
    :param infer: if geometry not found in possible_names keys, search all other keys
    for geometry
    :return: a 2 value tuple where 1st value is geometry object (or None) and 2nd value
    is a boolean indicating if the geometry was inferred
    '''
    for possible_geometry_field in possible_names:
        possible_geometry = d.get(possible_geometry_field)
        if possible_geometry and isinstance(possible_geometry, dict) and all(
                k in possible_geometry for k in ("type", "coordinates")):
            d.pop(possible_geometry_field)
            return (possible_geometry, False)

    if infer:
        for key in d:
            if d[key] and isinstance(d[key], dict) and all(k in d[key] for k in ("type", "coordinates")):
                return (d.pop(key), True)

    return (None, False)


def _find_xy_geometry(d, possible_x_names, possible_y_names, infer):
    '''
    Attempts to build a geojson point geometry from coordinate values contained in
    a dict object
    :param d: dict object
    :param possible_x_names: dict keys to search for the x coordinate value
    :param possible_y_names: dict keys to search for the y coordinate value
    :param infer: if coordinates were not found in possible_x_names and possible_y_names,
    search other keys with common coordinate names for x and y coordinate values
    :return: a 2 value tuple where 1st value is geometry object (or None) and 2nd value
    is a boolean indicating if the geometry was inferred
    '''
    x, y = None, None
    for possible_x_field in possible_x_names:
        possible_x = _get_numeric_val(d, possible_x_field)
        if possible_x:
            x = possible_x
    # dont bother looking for y if no x found
    if x:
        for possible_y_field in possible_y_names:
            possible_y = _get_numeric_val(d, possible_y_field)
            if possible_y:
                y = possible_y
    if x and y:
        geometry = {
            "type": "Point",
            "coordinates": [x, y]
        }
        return (geometry, False)

    if infer:
        x, y = None, None
        doc_keys = list(d.keys())
        for k in doc_keys:
            if k.lower() in ['x', 'long', 'lng', 'longitude', 'lon']:
                possible_x = _get_numeric_val(d, k)
                if possible_x:
                    x = possible_x
                    break
        if x:
            for k in doc_keys:
                if k.lower() in ['y', 'lat', 'latitude']:
                    possible_y = _get_numeric_val(d, k)
                    if possible_y:
                        y = possible_y
                        break

        if x and y:
            geometry = {
                "type": "Point",
                "coordinates": [x, y]
            }
            return (geometry, True)

    return (None, False)


def mongo_to_geojson(mongo_uri, collection, output_geojson, query=None,
                     projection=None, pipeline=None, pipeline_opts=None,
                     geometry_possible_fields=[], x_possible_fields=[],
                     y_possible_fields=[], infer=True, no_cursor_timeout=False):
    '''
    Extract data from MongoDB to a GeoJSON file
    :param mongo_uri:  Mongo connection string in URI format
    :param collection:  collection
    :param output_geojson: output geojson file
    :param query: document (dict)  defining filter to be applied to Mongo collection. see https://docs.mongodb.com/manual/reference/method/db.collection.find/
    :param projection: document (dict) defining what fields will be returned for a given query. see https://docs.mongodb.com/manual/reference/method/db.collection.find/#find-projection
    :param pipeline: array (list of dicts) defining Mongo aggregation pipeline.  see https://docs.mongodb.com/manual/reference/operator/aggregation-pipeline/
    :param pipeline_opts:  document (dict)  with additional arguments passed to aggregate command
    :param geometry_possible_fields: list of keys to search for geojson geometry object
    :param x_possible_fields: list of keys to search for point geometry longitude value
    :param y_possible_fields: list of keys to search for point geometry latitude value
    :param infer: if geometry not found/created from the possible_names parameters, try using
    all keys
    :param no_cursor_timeout: blocks cursor timeouts if set to True.  Use with caution
    :return:
    '''
    db = MongoClient(mongo_uri).get_database()
    if pipeline:
        cursor = db[collection].aggregate(pipeline, pipeline_opts)
    else:
        cursor = db[collection].find(filter=query, projection=projection, no_cursor_timeout=no_cursor_timeout)

    with open(output_geojson, 'w') as out:
        first_feature = True
        out.write('{"type":"FeatureCollection","features":[')
        for item in cursor:

            feature = {
                "type": "Feature",
                "geometry": None,
                "properties": item
            }

            geojson_geom, geojson_geom_inferred = _find_geojson_geometry(item, geometry_possible_fields, infer)
            xy_geom, xy_geom_inferred = _find_xy_geometry(item, x_possible_fields, y_possible_fields, infer)

            if geojson_geom and not geojson_geom_inferred:
                feature['geometry'] = geojson_geom
            elif xy_geom and not xy_geom_inferred:
                feature['geometry'] = xy_geom
            elif geojson_geom:
                feature['geometry'] = geojson_geom
            elif xy_geom:
                feature['geometry'] = xy_geom

            if first_feature:
                out.write(json.dumps(feature, cls=JSONEncoder))
                first_feature = False
            else:
                out.write("," + json.dumps(feature, cls=JSONEncoder))

        out.write("]}")
