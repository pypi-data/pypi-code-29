import os
import csv
import datetime
import gpxpy.gpx
import roadmaptools.inout

from typing import List, Dict, Tuple
from geojson import Point, Feature, LineString, FeatureCollection
from tqdm import tqdm
from roadmaptools.printer import print_info
from mapmatching_benchmark.init import config

# maps node id tuple to edge id
nodes_to_edge_dict = None

# map duplicate edge id to primary edge id
edge_duplicates = None

def _raw_nodes_to_geojson_points(nodes: List[List[str]]) -> (List[Feature], Dict[int, Tuple[float, float]]):
	point_features = []
	node_dict = {}
	for id, node in tqdm(enumerate(nodes), desc="Creating point features"):
		coord = (float(node[0]), float(node[1]))
		point = Point(coord)
		feature = Feature(geometry=point, id=id)
		point_features.append(feature)
		node_dict[id] = coord
	return point_features, node_dict


def _raw_edges_to_geojson_linestrings(edges: List[List[str]], node_dict: Dict[int, Tuple[float, float]])\
		-> Tuple[List[Feature], Dict[int, Tuple[int,int]]]:
	linestring_features = []
	edge_dict = {}
	for id, edge in tqdm(enumerate(edges), desc="Creating linestring features"):
		from_id = int(edge[0])
		to_id = int(edge[1])

		# duplicate check
		id_tupple = (from_id, to_id)
		if id_tupple in nodes_to_edge_dict:
			# print("Edge between ids {} already defined - it will be discarded".format(id_tupple))
			edge_duplicates[id] = nodes_to_edge_dict[id_tupple]
			continue
		nodes_to_edge_dict[id_tupple] = id

		coords = (node_dict[from_id], node_dict[to_id])
		line_string = LineString(coords)
		feature = Feature(geometry=line_string, id=id)
		linestring_features.append(feature)
		edge_dict[id] = (from_id, to_id)

	return linestring_features, edge_dict


def convert_graph(record_id: str) -> Tuple[Dict[int, Tuple[float, float]], Dict[int, Tuple[int,int]]]:
	global nodes_to_edge_dict, edge_duplicates

	print_info("Converting graph")
	node_file_path = "{}/{}/{}.nodes".format(config.records_dir, record_id, record_id)
	edge_file_path = "{}/{}/{}.arcs".format(config.records_dir, record_id, record_id)

	with open(node_file_path, "r") as node_file:
		reader = csv.reader(node_file, delimiter="	")
		nodes = []
		for line in reader:
			nodes.append(line)

	with open(edge_file_path, "r") as edge_file:
		reader = csv.reader(edge_file, delimiter="	")
		edges = []
		for line in reader:
			edges.append(line)

	nodes_to_edge_dict = {}
	edge_duplicates = {}

	feature_collection_content = []
	print_info("Converting nodes")
	node_features, node_dict = _raw_nodes_to_geojson_points(nodes)
	feature_collection_content.extend(node_features)
	print_info("Converting edges")
	edge_features, edge_dict = _raw_edges_to_geojson_linestrings(edges, node_dict)
	feature_collection_content.extend(edge_features)
	print_info("Number of duplicate edges: {}".format(len(edge_duplicates)))

	print_info("Saving graph to geojson")
	geojson_filepath = "{}/{}/map.geojson".format(config.records_dir, record_id)
	roadmaptools.inout.save_geojson(FeatureCollection(feature_collection_content), geojson_filepath)

	return node_dict, edge_dict


def convert_track(record_id: str):
	trace_file_path = "{}/{}/{}.track".format(config.records_dir, record_id, record_id)
	with open(trace_file_path, "r") as trace_file:
		reader = csv.reader(trace_file, delimiter="	")
		gpx = gpxpy.gpx.GPX()
		gpx_track = gpxpy.gpx.GPXTrack(number=record_id)
		gpx.tracks.append(gpx_track)
		gpx_segment = gpxpy.gpx.GPXTrackSegment()
		gpx_track.segments.append(gpx_segment)
		for line in tqdm(reader, desc="Processing tracepoints"):
			gpx_segment.points.append(gpxpy.gpx.GPXTrackPoint(
				float(line[1]), float(line[0]), time=datetime.datetime.fromtimestamp(float(line[2]) + 86400)))

		gpx_file_path = "{}/{}/trace.gpx".format(config.records_dir, record_id)
	roadmaptools.inout.save_gpx(gpx, gpx_file_path)


def convert_route(record_id: str, node_dict: Dict[int, Tuple[float, float]], edge_dict: Dict[int, Tuple[int, int]]):
	route_file_path = "{}/{}/{}.route".format(config.records_dir, record_id, record_id)
	with open(route_file_path, "r") as route_file:
		feature_collection_content = []
		for line in route_file.readlines():
			edge_id = int(line)

			# duplicate edge handeling
			if edge_id in edge_duplicates:
				edge_id = edge_duplicates[edge_id]

			edge = edge_dict[edge_id]
			line_string = LineString(coordinates=(node_dict[edge[0]], node_dict[edge[1]]))
			feature = Feature(geometry=line_string, id=edge_id)
			feature_collection_content.append(feature)

		geojson_filepath = "{}/{}/route.geojson".format(config.records_dir, record_id)
		roadmaptools.inout.save_geojson(FeatureCollection(feature_collection_content), geojson_filepath)


def convert_record(record_id: str):
	print_info("Converting record number {}".format(record_id))
	node_dict, edge_dict = convert_graph(record_id)
	convert_track(record_id)
	convert_route(record_id, node_dict, edge_dict)


def convert_records():
	record_dirs = [x[0] for x in os.walk(config.records_dir)]
	record_dirs = record_dirs[1:]
	for recor_dir in tqdm(record_dirs, desc="Processing records"):
		record_id = recor_dir.split("\\")[-1]
		convert_record(record_id)

convert_records()