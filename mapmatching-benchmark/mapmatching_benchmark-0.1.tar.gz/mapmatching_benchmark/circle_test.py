from mapmatching_benchmark.init import config

import numpy as np
import matplotlib.pyplot as plt
import roadmaptools.inout

main_dir = r"O:\AIC data\Shared\Map Matching Benchmark\matches\circle_test"
radii = [15, 50, 100, 150, 200, 250]

data = np.zeros(shape=(len(radii), 2))

for index, radius in enumerate(radii):
	csv_filepath = "{}/{}/results.csv".format(main_dir, radius)

	csv_content = list(roadmaptools.inout.load_csv(csv_filepath))

	total_time = 0
	total_accuracy = 0
	total_points = 0
	total_length = 0
	total_cost_count = 0
	count = 0
	for record in csv_content:
		total_accuracy += float(record[1])
		total_time += float(record[2])
		total_points += int(record[3])
		total_length += float(record[4])
		total_cost_count += float(record[5])
		count += 1

	data[index] = [radius, total_cost_count]


# n^2
x = np.arange(0, 250, 1)
y = x * x

# n^3
y_3 = x * x * x / 3

# plot
fig = plt.figure(figsize=(4, 3))
ax = fig.add_subplot(111)

# ax.plot(x, y)
ax.plot(x, y_3, label="x^3 / 3", c="lightgrey")

ax.axhline(y=120000, linewidth=2, color='black', linestyle='--', label='GSMM')
ax.axvline(x=200, linewidth=2, color='blue', linestyle='--', label='Radius proposed in [7]')

ax.plot(data[:, 0], data[:, 1], label="HMM-MM")




ax.set_xlabel('Candidate Radius')
ax.set_ylabel('Cost Computation Count')

ax.legend()

plt.savefig(config.images.circle_test, bbox_inches='tight', transparent=True)

plt.show()