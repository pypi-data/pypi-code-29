from mapmatching_benchmark.init import config

import os
import roadmaptools.inout
import roadmaptools.utm
import roadmaptools.gpx_shp
import mapmatching_benchmark.common

from abc import ABC, abstractmethod
from typing import List, Dict, Tuple, Callable
from timeit import default_timer as timer
from gpx_lite.gpxtrack import GPXTrack
from geojson.feature import FeatureCollection
from shapely.geometry import Point
from tqdm import tqdm
from networkx import DiGraph
from roadmaptools.printer import print_info
from roadmaptools.graph import RoadGraph
from roadmaptools.road_structures import LinestringEdge
from roadmaptools.utm import CoordinateConvertor


class RoadSegment:

	def __init__(self, id: int, length: int):
		self.length = length
		self.id = id


class TraceMapLoader(ABC):

	@abstractmethod
	def has_more_records(self) -> bool:
		pass

	@abstractmethod
	def load_next_record(self) -> Tuple[str, GPXTrack, FeatureCollection]:
		pass


class GroundTruthLoader(ABC):

	@abstractmethod
	def load_gt(self, id: str) -> FeatureCollection:
		pass


class DefaultDataLoader(TraceMapLoader):

	def has_more_records(self) -> bool:
		return self.current_index < len(self.record_dirs)

	def __init__(self, period: int=None):
		if period:
			self.trace_filename = "trace-period-{}.gpx".format(period)
		else:
			self.trace_filename = "trace.gpx"

		record_dirs = [x[0] for x in os.walk(config.records_dir)]
		self.record_dirs = record_dirs[1:]
		self.current_index = 0

	def load_next_record(self) -> Tuple[str, GPXTrack]:
		record_dir = self.record_dirs[self.current_index]
		gpx_file_path = "{}/{}".format(record_dir, self.trace_filename)
		trace = roadmaptools.inout.load_gpx(gpx_file_path)
		record_id: str = record_dir.split("\\")[-1]
		trace_data = (record_id, trace.tracks[0])

		self.current_index += 1
		return trace_data


class TestDataLoader(TraceMapLoader):

	def has_more_records(self) -> bool:
		depleted = self.depleted
		self.depleted = True
		return not depleted

	def __init__(self, test_id: str, period: int=None):
		self.test_id = test_id
		self.depleted = False
		self.period = period

	def load_next_record(self) -> Tuple[str, GPXTrack]:
		if self.period:
			gpx_file_path = "{}/{}/trace-period-{}.gpx".format(config.records_dir, self.test_id, self.period)
		else:
			gpx_file_path = "{}/{}/trace.gpx".format(config.records_dir, self.test_id)
		gpx_content = roadmaptools.inout.load_gpx(gpx_file_path)
		trace_data = (self.test_id, gpx_content.tracks[0])
		return trace_data


class DefaultGroundTruthLoader(GroundTruthLoader):

	def __init__(self):
		pass

	def load_gt(self, id: str) -> FeatureCollection:
		geojson_filepath = "{}/{}/route.geojson".format(config.records_dir, id)
		gt = roadmaptools.inout.load_geojson(geojson_filepath)
		return gt


class TestGroundTruthLoader(GroundTruthLoader):

	def __init__(self, test_id: str):
		self.test_id = test_id

	def load_gt(self, id: str) -> FeatureCollection:
		geojson_filepath = "{}/{}/route.geojson".format(config.records_dir, self.test_id)
		gt = roadmaptools.inout.load_geojson(geojson_filepath)
		return gt


class MapMatchingProcessor(ABC):

	def __init__(self):
		self.cost_computation_count: int = None

	@abstractmethod
	def prepare(self, trace: GPXTrack, map_filepath: str, trace_id: str):
		self.cost_computation_count = 0

	@abstractmethod
	def match(self):
		pass

	@abstractmethod
	def get_match(self) -> List[int]:
		pass

	@abstractmethod
	def postprocess(self):
		pass

	def get_cost_computation_count(self) -> int:
		return self.cost_computation_count


def run_mapmatching_benchmark(trace_map_loader: TraceMapLoader, processor: MapMatchingProcessor,
							  gt_loader: GroundTruthLoader, results_folder_path: str,
							  record_filter: Callable[[str, GPXTrack, FeatureCollection], bool]=None):
	score_sum = 0
	time_sum = 0
	point_sum = 0
	gt_total_length = 0
	total_cost_computation_count = 0
	out = []
	while trace_map_loader.has_more_records():

		trace_data = trace_map_loader.load_next_record()
		if not record_filter or record_filter(*trace_data):
			match, time, cost_computation_count = _process_trace_data(trace_data, processor)

			gt_geojson = gt_loader.load_gt(trace_data[0])
			gt = geojson_to_roadsegment_list(gt_geojson)

			# TODO fix for non-graph map matchers
			road_graph = processor.get_road_graph()

			score, gt_length = get_route_mismatch_fraction(match, gt, road_graph)
			point_count = len(trace_data[1].segments[0].points)
			print_info("Score for trace {}: {}".format(trace_data[0], score))
			print_info("Time: {}s".format(time))
			print_info("Trace point count: {}".format(point_count))
			print_info("Grount truth length: {}".format(gt_length))
			print_info("Cost computation count: {}".format(cost_computation_count))
			score_sum += score
			time_sum += time
			point_sum += point_count
			gt_total_length += gt_length
			total_cost_computation_count += cost_computation_count
			out.append([trace_data[0], score, time, point_count, gt_length, cost_computation_count])

	print_info("Tested trace count: {}".format(len(out)))
	print_info("Average score: {}".format(score_sum / len(out)))
	print_info("Total time: {}s".format(time_sum))
	print_info("Trace points total: {}".format(point_sum))
	print_info("Total ground truth length: {}m".format(gt_total_length))
	print_info("Points per second: {}".format(point_sum / time_sum))
	print_info("Km/s per second: {}s".format(gt_total_length / 1000 / time_sum))
	print_info("Total cost computation count: {}".format(total_cost_computation_count))
	roadmaptools.inout.save_csv(out, "{}/results.csv".format(results_folder_path))

# vyndat vse co ma neco spolecneho s processor a pouzit v main!!!!!
def _process_trace_data(trace_data: Tuple[str, GPXTrack, FeatureCollection], processor: MapMatchingProcessor) \
		-> Tuple[List[int], float, int]:
	geojson_filepath = "{}/{}/map.geojson".format(config.records_dir, trace_data[0])
	processor.prepare(trace_data[1], geojson_filepath, trace_data[0])
	start = timer()
	processor.match()
	end = timer()
	match = processor.get_match()
	cost_computation_count = processor.get_cost_computation_count()
	processor.postprocess()
	return match, end - start, cost_computation_count


def geojson_to_roadsegment_list(gt_geojson: FeatureCollection) -> List[int]:
	road_segments = []
	# first_coord = gt_geojson["features"][0]["geometry"]["coordinates"][0]
	# projection = roadmaptools.utm.TransposedUTM(first_coord[1], first_coord[0])
	for edge_feature in gt_geojson["features"]:
		id = edge_feature["id"]
		# node_from =
		# edge = LinestringEdge(edge_feature["geometry"], CoordinateConvertor.convert)

		# from_coord = edge_feature["geometry"]["coordinates"][0]
		# to_coord = edge_feature["geometry"]["coordinates"][0]
		# from_point = Point(roadmaptools.utm.wgs84_to_utm(from_coord[1], first_coord[0], projection))
		# to_point = Point(roadmaptools.utm.wgs84_to_utm(to_coord[1], to_coord[0], projection))
		# length = from_point.distance(to_point)
		# road_segments.append(RoadSegment(id, length))
		road_segments.append(id)

	return road_segments


def _create_length_dict(map: FeatureCollection) ->Dict[int,int]:
	length_dict = {}
	projection = None
	for item in tqdm(map['features'], desc="processing features"):
		if item["geometry"]["type"] == "LineString":
			coords = item['geometry']['coordinates']
			if not projection:
				projection = roadmaptools.utm.TransposedUTM(coords[0][1], coords[0][0])

			coord_from = roadmaptools.utm.wgs84_to_utm(coords[0][1], coords[0][0], projection)
			coord_to = roadmaptools.utm.wgs84_to_utm(coords[-1][1], coords[-1][0], projection)

			from_point = Point(coord_from)
			to_point = Point(coord_to)
			length_dict[item["id"]] = from_point.distance(to_point)
	return length_dict


def _create_length_dict_from_networkx(road_graph: RoadGraph) ->Dict[int,int]:
	length_dict = {}
	for from_node, to_node, data in tqdm(road_graph.graph.edges(data=True), desc="processing edges"):
		edge: LinestringEdge = data["edge"]
		length = edge.linestring.length
		# length = edge.node_from.get_point().distance(edge.node_to.get_point())
		length_dict[edge.geojson_linestring["id"]] = length
		# length_dict[edge.id] = length
	return length_dict


def get_route_mismatch_fraction(match: List[int], ground_truth: List[int], map: RoadGraph) -> Tuple[float, float]:
	# length_dict = _create_length_dict(map)
	length_dict = _create_length_dict_from_networkx(map)
	gt_length = 0

	# length of edges in match that are not preset in ground truth
	false_positives_length = 0

	# length of edges in ground truth not present in match
	false_negative_length = 0

	match_index = 0
	gt_index = 0

	while gt_index < len(ground_truth) or match_index < len(match):

		if gt_index >= len(ground_truth):
			false_positives_length += _compute_rest_length(match, match_index, length_dict)
			break
		if match_index >= len(match):
			gt_rest_length = _compute_rest_length(ground_truth, gt_index, length_dict)
			false_negative_length += gt_rest_length
			gt_length += gt_rest_length
			break


		gt_edge = ground_truth[gt_index]
		match_edge = match[match_index]

		if gt_edge == match_edge:
			gt_length += length_dict[gt_edge]
			gt_index +=1
			match_index +=1

		else:
			first_correct_segment = _get_first_correct_edge(match, ground_truth, match_index, gt_index)
			while gt_edge != first_correct_segment and gt_index < len(ground_truth):
				gt_edge = ground_truth[gt_index]
				gt_length += length_dict[gt_edge]
				false_negative_length += length_dict[gt_edge]
				gt_index += 1

			while match_edge != first_correct_segment and match_index < len(match):
				match_edge = match[match_index]
				false_positives_length += length_dict[match_edge]
				match_index += 1

	rmf = (false_positives_length + false_negative_length) / gt_length

	return rmf, gt_length


def _get_first_correct_edge(match: List[int], ground_truth: List[int],
							match_index: int, gt_index: int) -> int:
	gt_undecided = set()
	match_undecided = set()
	while match_index < len(match) or gt_index < len(ground_truth):

		gt_index += 1
		if gt_index < len(ground_truth):
			# get next gt_edge

			gt_edge = ground_truth[gt_index]
			if gt_edge in match_undecided:
				return gt_edge
			gt_undecided.add(gt_edge)

		# get next match edge
		match_index += 1
		if match_index < len(match):
			match_edge = match[match_index]
			if match_edge in gt_undecided:
				return match_edge
			match_undecided.add(match_edge)


def _compute_rest_length(edge_list: List[int], index: int, length_dict: Dict[int, int]) -> int:
	length = 0
	while index < len(edge_list):
		length += length_dict[edge_list[index]]
		index += 1

	return length


def cyclic_trace_filter(id: str, trace: GPXTrack) -> bool:
	try:
		trace_linestring = roadmaptools.gpx_shp.track_to_linestring(trace)
		if trace_linestring.is_simple:
			return True
		else:
			print_info("Trace {} discarded because it contains cycles".format(id))
			return False
	except ValueError:
		print_info("Trace {} discarded because it contains only one point".format(id))
		return False


