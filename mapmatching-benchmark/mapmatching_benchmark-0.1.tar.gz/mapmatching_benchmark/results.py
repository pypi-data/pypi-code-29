from mapmatching_benchmark.init import config

import numpy as np
import roadmaptools.inout

from typing import Tuple
from enum import Enum



class Algorithm(Enum):
	HMM = ("hmm", u'x', "r", "HMM-MM")
	# INCREMENTAL = ("incremental", u'+', "g", "Incremental")
	PROPOSED = ("", u'o', "b", "GSMM")

	def __init__(self, name: str, symbol: str, color: str, label: str):
		self.alg_name = name
		self.symbol = symbol
		self.color = color
		self.label = label


matches_dir = r"O:\AIC data\Shared\Map Matching Benchmark\matches"
# algorithm_names = ["incremental", "hmm", ""]
# symbols = {"incremental": u'+', "hmm": u'+', u'o'}
periods = [1] + list(config.subsampling_periods)

acyclic_traces = ["00000007", "00000009", "00000012", "00000020", "00000023", "00000024", "00000025", "00000027",
				  "00000037", "00000041", "00000044", "00000050", "00000058", "00000059", "00000060", "00000064",
				  "00000076", "00000082"]

# load all data files
plot_data = {}
for algorithm in Algorithm:
	plot_data_per_alg = np.zeros(shape=(len(periods), 4))
	index = 0
	for period in periods:
		if algorithm.alg_name:
			csv_filepath = "{}/period-{}-{}/results.csv".format(matches_dir, period, algorithm.alg_name)
		else:
			csv_filepath = "{}/period-{}/results.csv".format(matches_dir, period)

		try:
			csv_content = list(roadmaptools.inout.load_csv(csv_filepath))

			if len(csv_content[0]) < 5:
				continue

			# prepare points for plot, x axis accuracy, y axis length per second, symbol the algorithm type, number the period length
			total_time = 0
			total_accuracy = 0
			total_points = 0
			total_length = 0
			total_cost_count = 0
			count = 0
			for record in csv_content:
				if record[0] in acyclic_traces:
					total_accuracy += float(record[1])
					total_time += float(record[2])
					total_points += int(record[3])
					total_length += float(record[4])
					# total_cost_count += float(record[5])
					count += 1

			avg_accuracy = total_accuracy / count
			length_per_second = total_length / total_time
			plot_data_per_alg[index] = [avg_accuracy, length_per_second, period, total_cost_count]
		except FileNotFoundError:
			print("Data not found in: {}".format(csv_filepath))
			plot_data_per_alg[index] = [0,0,0]

		index += 1
	plot_data[algorithm] = plot_data_per_alg