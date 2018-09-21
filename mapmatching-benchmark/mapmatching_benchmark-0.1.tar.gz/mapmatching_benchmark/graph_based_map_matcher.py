from mapmatching_benchmark.init import config

import roadmaptools.utm
import roadmaptools.geometry

from abc import ABC, abstractmethod
from typing import List, Dict, Tuple, Callable
from geojson import FeatureCollection
from gpx_lite.gpxtrack import GPXTrack
from networkx import DiGraph
from scipy.spatial.kdtree import KDTree
from tqdm import tqdm

from roadmaptools.printer import print_info
from roadmaptools.utm import CoordinateConvertor
from mapmatching_benchmark.tester import MapMatchingProcessor
from roadmaptools.road_structures import LinestringEdge, Node
from roadmaptools.graph import RoadGraph


class GraphBasedMapMatcher(MapMatchingProcessor, ABC):
    def __init__(self, single_map: bool, use_map_cache: bool = True, cache_dir: str = config.networx_cache_dir,
                 node_creator: Callable[[float, float, int], Node] = roadmaptools.graph._create_node):
        super().__init__()
        self.single_map: bool = single_map
        self.use_map_cache = use_map_cache
        self.cache_dir = cache_dir
        self.node_creator = node_creator
        self.trace: GPXTrack = None
        self.graph: RoadGraph = None


        # Dict of nodes indexed by coordinates. It has to be here, because nodes itself cannot be stored in KDTree
        self.coordinate_to_node: Dict[Tuple[float, float], Node] = None

    def get_road_graph(self):
        return self.graph

    def prepare(self, trace: GPXTrack, map_filepath: str, trace_id: str):
        super().prepare(trace, map_filepath, trace_id)
        self.trace = trace

        if not self.graph or not self.single_map:
            if self.use_map_cache:
                cache_filepath = "{}/{}.pickle".format(self.cache_dir, trace_id)
                self.graph = RoadGraph(cache_filepath=cache_filepath, node_creator=self.node_creator)
            else:
                self.graph = RoadGraph(use_cache=False, node_creator=self.node_creator)
            self.graph.load_from_geojson(map_filepath)
    # self.kdtree = self._build_kdtree()

    @abstractmethod
    def match(self):
        pass

    @abstractmethod
    def get_match(self) -> List[int]:
        pass

    def postprocess(self):
        pass

    def _build_kdtree(self):
        self.coordinate_to_node = {}
        coord_list = []
        print_info("Building KDTree")
        for node in tqdm(self.graph.nodes(), desc="Creating coord list"):
            coords = (node.x, node.y)
            coord_list.append(coords)
            self.coordinate_to_node[coords] = node

        return KDTree(coord_list)
