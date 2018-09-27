from fastkml import kml
from shapely.geometry import shape, Polygon, MultiPolygon, Point


__version__ = '0.0.1'
__author__ = 'Herbert Kruitbosch'


def as_gabmap_kml(geojson, document_name='Python Generated gabmap KML', name_property='gemeente_en_wijk_naam'):
    """Creates a string with kml, accepted by gabmap, based on the (multi)polygons and points in a GeoJSON.
    If a feature in the geojson is a (Multi)Polygon, then both the (multi)polygon and the centroid point are
    added to the KML output. `name_property` is used as the key in `'properties'` of the geojson to determine
    the name used in the Placemarks of the KML. `document_name` is the name used in the Document element of the
    KML."""
    document = kml.Document(name=document_name, ns='')
    
    illigal_symbols = set('"\'&')
    intersection = set(document_name).intersection(illigal_symbols) == set()
    assert intersection, (
        "Gabmap cannot deal with some symbols ({}) in the document_name: {}".format(intersection, document_name))
    
    names = set()
    for feature in geojson['features']:
        shape_ = shape(feature['geometry'])
        name = feature['properties'][name_property]
        
        assert isinstance(shape_, Polygon) or isinstance(shape_, MultiPolygon) or isinstance(shape_, Point), (
            "gabmap.as_gabmap_kml was only tested on Polygons, Multipolygons and "
            "Points, not on {}:  ".format(type(shape_), name)
        )
        
        assert name not in names, "Gabmap cannot deal with duplicate names: {}".format(name)
        
        intersection = set(name).intersection(illigal_symbols) == set()
        assert intersection, (
            "Gabmap cannot deal with some symbols ({}) in a name: {}".format(intersection, name))
        
        if isinstance(shape_, Polygon) or isinstance(shape_, MultiPolygon):
            names.add(name)
            point_placemark = kml.Placemark(name=name, ns='')
            point_placemark.geometry=shape_.centroid
            document.append(point_placemark)
        
        polygon_placemark = kml.Placemark(name=name, ns='')
        polygon_placemark.geometry=shape_
        document.append(polygon_placemark)
        
    k = kml.KML()
    k.append(document)
    return (
        """<?xml version="1.0" encoding="utf-8" ?>
""" +
        k.to_string(prettyprint=True) 
        # prettyprint is important, as gabmap requires the name-attributes of (multi)polygon-placemarkers to have a newline after the closing tag.
    )

