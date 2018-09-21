
import fconfig.configuration

from fconfig.config import Config
from mapmatching_benchmark.config.images import Images
import roadmaptools.config.roadmaptools_config
from roadmaptools.config.roadmaptools_config import RoadmaptoolsConfig

class MachineLearningBenchmarkConfig(Config):
    def __init__(self, properties: dict=None):
        self.records_dir = properties.get("records_dir")
        self.networx_cache_dir = properties.get("networx_cache_dir")

        self.images = Images(properties.get("images"))
        self.roadmaptools = RoadmaptoolsConfig(properties.get("roadmaptools"))
        roadmaptools.config.roadmaptools_config.config = self.roadmaptools

        self.subsampling_periods = properties.get("subsampling_periods")
        pass

config: MachineLearningBenchmarkConfig = fconfig.configuration.load((RoadmaptoolsConfig, 'roadmaptools'), (MachineLearningBenchmarkConfig, None))


