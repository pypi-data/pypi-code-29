import numpy as np
import roadmaptools.inout

from mapmatching_benchmark.results import Algorithm, matches_dir, periods

for algorithm in Algorithm:
	plot_data_per_alg = np.zeros(shape=(len(periods), 4))
	index = 0
	for period in periods:
		if algorithm.alg_name:
			csv_filepath = "{}/period-{}-{}/results.csv".format(matches_dir, period, algorithm.alg_name)
		else:
			csv_filepath = "{}/period-{}/results.csv".format(matches_dir, period)

		csv_content = list(roadmaptools.inout.load_csv(csv_filepath))
		new_content = [list(row) for row in csv_content]
		for index in range(len(csv_content)):
			if index > 0:
				new_content[index][5] = str(int(csv_content[index][5]) - int(csv_content[index - 1][5]))

		roadmaptools.inout.save_csv(new_content, csv_filepath)