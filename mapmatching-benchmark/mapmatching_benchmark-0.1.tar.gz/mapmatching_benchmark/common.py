from mapmatching_benchmark.init import config

import os

from typing import Callable
from tqdm import tqdm


def apply_to_all_records(function: Callable[[str], None]):
	record_dirs = [x[0] for x in os.walk(config.records_dir)]
	record_dirs = record_dirs[1:]
	for recor_dir in tqdm(record_dirs, desc="Processing records"):
		record_id = recor_dir.split("\\")[-1]
		function(record_id)