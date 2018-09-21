from mapmatching_benchmark.init import config

import roadmaptools.inout
import roadmaptools.gpx
import mapmatching_benchmark.common

from typing import Callable
from copy import copy, deepcopy
from gpxpy.gpx import GPXTrackPoint



def get_subsampling_filter(period: int) -> Callable[[GPXTrackPoint, GPXTrackPoint], bool]:
	def subsample(lastpoint: GPXTrackPoint, point: GPXTrackPoint):
		keep = subsample.counter % period == 0
		subsample.counter += 1
		return keep
	subsample.counter = 0

	return subsample


def subsample_record(record_id: str):
	gpx_file_path = "{}/{}/trace.gpx".format(config.records_dir, record_id)
	gpx_content = roadmaptools.inout.load_gpx(gpx_file_path)
	for period in config.subsampling_periods:
		gpx_copy = deepcopy(gpx_content)
		roadmaptools.gpx.filter_gpx(gpx_copy, get_subsampling_filter(period))
		subsampled_gpx_file_path = "{}/{}/trace-period-{}.gpx".format(config.records_dir, record_id, period)
		roadmaptools.inout.save_gpx(gpx_copy, subsampled_gpx_file_path)


# subsample_record("00000000")

mapmatching_benchmark.common.apply_to_all_records(subsample_record)